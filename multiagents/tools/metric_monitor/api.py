import warnings
import sys
import os
import numpy as np
import paramiko
import pdb

from multiagents.knowledge.knowledge_extraction import KnowledgeExtraction
from multiagents.utils.database import DBArgs, Database
from multiagents.utils.core import read_yaml

from multiagents.tools.metric_monitor.anomaly_detection import prometheus
from multiagents.tools.metric_monitor.anomaly_detection import detect_anomalies
from multiagents.tools.metrics import prometheus_metrics, benchserver_conf, postgresql_conf, obtain_values_of_metrics

'''

def obtain_values_of_metrics(start_time, end_time, metrics):

    if end_time - start_time > 11000 * \
            3:     # maximum resolution of 11,000 points per timeseries
        #raise Exception("The time range is too large, please reduce the time range")
        warnings.warn(
            "The time range ({}, {}) is too large, please reduce the time range".format(
                start_time, end_time))

    required_values = {}

    print(" ====> metrics: ", metrics)
    for metric in metrics:
        metric_values = prometheus('api/v1/query_range',
                                   {'query': metric,
                                    'start': start_time,
                                    'end': end_time,
                                    'step': '3'})
        if metric_values["data"]["result"] != []:
            metric_values = metric_values["data"]["result"][0]["values"]
        else:
            raise Exception("No metric values found for the given time range")

        # compute the average value of the metric
        max_value = np.max(np.array([float(value)
                           for _, value in metric_values]))

        required_values[metric] = max_value

    return required_values

def find_abnormal_metrics(start_time, end_time, monitoring_metrics, resource):

    resource_keys = ["memory", "cpu", "disk", "network"]

    abnormal_metrics = []
    for metric_name in monitoring_metrics:

        interval_time = 5
        metric_values = prometheus('api/v1/query_range',
                                   {'query': metric_name,
                                    'start': start_time - interval_time * 60,
                                    'end': end_time + interval_time * 60,
                                    'step': '3'})

        if metric_values["data"]["result"] != []:
            metric_values = metric_values["data"]["result"][0]["values"]
        else:
            continue

        if detect_anomalies(np.array([float(value)
                            for _, value in metric_values])):

            success = True
            for key in resource_keys:
                if key in metric_name and key != resource:
                    success = False
                    break
            if success:
                abnormal_metrics.append(metric_name)

    return abnormal_metrics

# load knowlege extractor
knowledge_matcher = KnowledgeExtraction(
    "/bmtools/tools/db_diag/root_causes_dbmind.jsonl")

# load db settings
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
script_dir = os.path.dirname(script_dir)
dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
db = Database(dbargs, timeout=-1)

monitoring_metrics = []
with open(str(os.getcwd()) + "/bmtools/tools/db_diag/database_monitoring_metrics", 'r') as f:
    monitoring_metrics = f.read()
monitoring_metrics = eval(monitoring_metrics)

'''

# apis

def obtain_start_and_end_time_of_anomaly(input: str = 'json dict string'):

    # 读取tool_learning/bmtools/diag_time.txt文件，获取最后一行异常时间段
    with open(str(os.getcwd()) + "/diag_time.txt", 'r') as f:
        last_line = f.readlines()[-1].replace("\n", "")
        print("-----------last_line: ", last_line)
        diag_start_time = last_line.split('-')[0]
        diag_end_time = last_line.split('-')[1]
    print("diag_start_time: ", diag_start_time)
    print("diag_end_time: ", diag_end_time)

    if not diag_start_time or not diag_end_time:
        raise Exception("No start and end time of anomaly!")
    
    return {"start_time": diag_start_time, "end_time": diag_end_time}

def whether_is_abnormal_metric(
        start_time: int,
        end_time: int,
        metric_name: str = "cpu_usage"):

    metric_values = prometheus('api/v1/query_range',
                                {'query': prometheus_metrics[metric_name],
                                'start': start_time,
                                'end': end_time,
                                'step': '3'})

    if metric_values["data"]["result"] != []:
        metric_values = metric_values["data"]["result"][0]["values"]
    else:
        raise Exception("No metric values found for the given time range")

    is_abnormal = detect_anomalies(
        np.array([float(value) for _, value in metric_values]))

    if is_abnormal:
        print(f"{metric_name} is abnormal")
        return "The metric is abnormal"
    else:
        print(f"{metric_name} is normal")
        return "The metric is normal"
    

def match_diagnose_knowledge(
        start_time: int,
        end_time: int,
        metric_name: str = "cpu"):

    dbargs = DBArgs("postgresql", config=postgresql_conf) # todo switch databases
    db = Database(dbargs, timeout=-1)
    knowledge_matcher = KnowledgeExtraction(
        "/multiagents/knowledge/root_causes_dbmind.jsonl")

    if "cpu" in metric_name:
        metric_prefix = "cpu"
    else:
        metric_prefix = "memory"

    metrics_list = prometheus_metrics[f"{metric_prefix}_metrics"]

    detailed_metrics = obtain_values_of_metrics(
        start_time, end_time, metrics_list)

    slow_queries = db.obtain_historical_slow_queries()

    slow_query_state = ""
    for i, query in enumerate(slow_queries):
        slow_query_state += str(i + 1) + '. ' + str(query) + "\n"

    docs_str = knowledge_matcher.match(detailed_metrics)

    knowledge_str=  """The {} relevant metric values from Prometheus are: 
    {} 
    
    The slow queries are:
    {}

    The matched knowledge is:
    {}""".format(metric_prefix,
        detailed_metrics,
        slow_query_state,
        docs_str)

    return knowledge_str