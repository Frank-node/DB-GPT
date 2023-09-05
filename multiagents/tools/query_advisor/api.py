import warnings
from multiagents.utils.database import DBArgs, Database
from multiagents.utils.core import read_yaml

import sys
import json
import os
import requests
import numpy as np
import openai
import paramiko
import pdb
from multiagents.tools.metrics import prometheus_metrics, benchserver_conf, postgresql_conf


executor_url = "http://8.131.229.55:5114/rewrite/single_rule"

# tranformation rules (45)
# ['AGGREGATE_ANY_PULL_UP_CONSTANTS', 'AGGREGATE_EXPAND_DISTINCT_AGGREGATES', 'AGGREGATE_EXPAND_DISTINCT_AGGREGATES_TO_JOIN', 'AGGREGATE_JOIN_REMOVE', 'AGGREGATE_JOIN_TRANSPOSE_EXTENDED', 'AGGREGATE_UNION_TRANSPOSE', 'AGGREGATE_UNION_AGGREGATE', 'AGGREGATE_VALUES', 'AGGREGATE_PROJECT_MERGE', 'FILTER_INTO_JOIN', 'FILTER_MERGE', 'FILTER_AGGREGATE_TRANSPOSE', 'FILTER_PROJECT_TRANSPOSE', 'FILTER_TABLE_FUNCTION_TRANSPOSE', 'FILTER_SCAN', 'FILTER_CORRELATE', 'FILTER_SET_OP_TRANSPOSE', 'FILTER_REDUCE_EXPRESSIONS', 'JOIN_CONDITION_PUSH', 'JOIN_EXTRACT_FILTER', 'JOIN_PROJECT_BOTH_TRANSPOSE', 'JOIN_PROJECT_LEFT_TRANSPOSE', 'JOIN_PROJECT_RIGHT_TRANSPOSE', 'JOIN_REDUCE_EXPRESSIONS', 'JOIN_LEFT_UNION_TRANSPOSE', 'JOIN_RIGHT_UNION_TRANSPOSE', 'SEMI_JOIN_REMOVE', 'PROJECT_CALC_MERGE', 'PROJECT_CORRELATE_TRANSPOSE', 'PROJECT_REDUCE_EXPRESSIONS', 'PROJECT_SUB_QUERY_TO_CORRELATE', 'PROJECT_MERGE', 'PROJECT_REMOVE', 'PROJECT_TO_CALC', 'CALC_MERGE', 'CALC_REMOVE', 'SORT_UNION_TRANSPOSE', 'SORT_REMOVE', 'SORT_REMOVE_CONSTANT_KEYS', 'SORT_JOIN_TRANSPOSE', 'SORT_PROJECT_TRANSPOSE', 'UNION_MERGE', 'UNION_REMOVE', 'UNION_PULL_UP_CONSTANTS', 'UNION_TO_DISTINCT']

def AGGREGATE_ANY_PULL_UP_CONSTANTS_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "AGGREGATE_ANY_PULL_UP_CONSTANTS"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def AGGREGATE_EXPAND_DISTINCT_AGGREGATES_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "AGGREGATE_EXPAND_DISTINCT_AGGREGATES"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def AGGREGATE_EXPAND_DISTINCT_AGGREGATES_TO_JOIN_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "AGGREGATE_EXPAND_DISTINCT_AGGREGATES_TO_JOIN"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def AGGREGATE_JOIN_REMOVE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "AGGREGATE_JOIN_REMOVE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def AGGREGATE_JOIN_TRANSPOSE_EXTENDED_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "AGGREGATE_JOIN_TRANSPOSE_EXTENDED"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def AGGREGATE_UNION_TRANSPOSE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "AGGREGATE_UNION_TRANSPOSE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def AGGREGATE_UNION_AGGREGATE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "AGGREGATE_UNION_AGGREGATE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def AGGREGATE_VALUES_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "AGGREGATE_VALUES"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def AGGREGATE_PROJECT_MERGE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "AGGREGATE_PROJECT_MERGE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def FILTER_INTO_JOIN_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "FILTER_INTO_JOIN"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def FILTER_MERGE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "FILTER_MERGE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def FILTER_AGGREGATE_TRANSPOSE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "FILTER_AGGREGATE_TRANSPOSE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def FILTER_PROJECT_TRANSPOSE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "FILTER_PROJECT_TRANSPOSE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def FILTER_TABLE_FUNCTION_TRANSPOSE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "FILTER_TABLE_FUNCTION_TRANSPOSE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def FILTER_SCAN_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "FILTER_SCAN"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def FILTER_CORRELATE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "FILTER_CORRELATE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def FILTER_SET_OP_TRANSPOSE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "FILTER_SET_OP_TRANSPOSE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def FILTER_REDUCE_EXPRESSIONS_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "FILTER_REDUCE_EXPRESSIONS"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def JOIN_CONDITION_PUSH_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "JOIN_CONDITION_PUSH"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def JOIN_EXTRACT_FILTER_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "JOIN_EXTRACT_FILTER"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def JOIN_PROJECT_BOTH_TRANSPOSE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "JOIN_PROJECT_BOTH_TRANSPOSE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def JOIN_PROJECT_LEFT_TRANSPOSE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "JOIN_PROJECT_LEFT_TRANSPOSE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def JOIN_PROJECT_RIGHT_TRANSPOSE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "JOIN_PROJECT_RIGHT_TRANSPOSE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def JOIN_REDUCE_EXPRESSIONS_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "JOIN_REDUCE_EXPRESSIONS"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def JOIN_LEFT_UNION_TRANSPOSE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "JOIN_LEFT_UNION_TRANSPOSE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def JOIN_RIGHT_UNION_TRANSPOSE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "JOIN_RIGHT_UNION_TRANSPOSE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def SEMI_JOIN_REMOVE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "SEMI_JOIN_REMOVE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def PROJECT_CALC_MERGE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "PROJECT_CALC_MERGE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def PROJECT_CORRELATE_TRANSPOSE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "PROJECT_CORRELATE_TRANSPOSE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def PROJECT_REDUCE_EXPRESSIONS_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "PROJECT_REDUCE_EXPRESSIONS"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def PROJECT_SUB_QUERY_TO_CORRELATE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "PROJECT_SUB_QUERY_TO_CORRELATE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def PROJECT_MERGE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "PROJECT_MERGE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def PROJECT_REMOVE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "PROJECT_REMOVE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def PROJECT_TO_CALC_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "PROJECT_TO_CALC"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def CALC_MERGE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "CALC_MERGE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def CALC_REMOVE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "CALC_REMOVE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def SORT_UNION_TRANSPOSE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "SORT_UNION_TRANSPOSE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def SORT_REMOVE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "SORT_REMOVE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def SORT_REMOVE_CONSTANT_KEYS_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "SORT_REMOVE_CONSTANT_KEYS"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def SORT_JOIN_TRANSPOSE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "SORT_JOIN_TRANSPOSE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def SORT_PROJECT_TRANSPOSE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "SORT_PROJECT_TRANSPOSE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def UNION_MERGE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "UNION_MERGE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def UNION_REMOVE_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "UNION_REMOVE"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def UNION_PULL_UP_CONSTANTS_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "UNION_PULL_UP_CONSTANTS"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

def UNION_TO_DISTINCT_rule(query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    param = {
        "sql": query,
        "rule": "UNION_TO_DISTINCT"
    }
    print("Rule param:", param)

    headers = {'Content-Type': 'application/json'}
    res_completion = requests.post(
        executor_url,
        data=json.dumps(param),
        headers=headers)

    #print("============ res_completion", res_completion.text)

    data = json.loads(res_completion.text.strip())
    data = data.get('data')
    new_query = data.get('rewritten_sql')

    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        text_output = f"Failed to optimize the query. The new query is still {query}"
    else:
        total_cost, operators = db.query_plan_statistics(new_query_plan)
        text_output = f"New query is {new_query}\nNew query plan statistics: total cost is {total_cost}, and the operators are {operators}"

    return text_output

# query hints (15)
# ["bitmapscan",
# "gathermerge",
# "hashagg",
# "hashjoin",
# "indexonlyscan",
# "indexscan",
# "material",
# "mergejoin",
# "nestloop",
# "parallel_append",
# "parallel_hash",
# "partition_pruning",
# "seqscan",
# "sort",
# "tidscan",]

def enable_or_disable_bitmapscan_operator(action: str, query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    # add hint to the query
    new_query = f"set enable_bitmapscan to \"{action}\"; " + query.replace("\n","")

    # execute the new query
    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        # raise error
        raise Exception(
            status_code=400,
            detail=f"Failed to explain the query after changing the enable_bitmapscan knob.")
    else:
        if action == "ON":
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after enabling the bitmapscan operator."
        else:
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators}, after disabling the bitmapscan operator."

    return text_output

def enable_or_disable_gathermerge_operator(action: str, query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    # add hint to the query
    new_query = f"set enable_gathermerge to \"{action}\"; " + query.replace("\n","")

    # execute the new query
    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        # raise error
        raise Exception(
            status_code=400,
            detail=f"Failed to explain the query after changing the enable_gathermerge knob.")
    else:
        if action == "ON":
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after enabling the gathermerge operator."
        else:
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after disabling the gathermerge operator."

    return text_output

def enable_or_disable_hashagg_operator(action: str, query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    # add hint to the query
    new_query = f"set enable_hashagg to \"{action}\"; " + query.replace("\n","")

    # execute the new query
    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        # raise error
        raise Exception(
            status_code=400,
            detail=f"Failed to explain the query after changing the enable_hashagg knob.")
    else:
        if action == "ON":
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after enabling the hashagg operator."
        else:
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after disabling the hashagg operator."

    return text_output

def enable_or_disable_hashjoin_operator(action: str, query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    # add hint to the query
    new_query = f"set enable_hashjoin to \"{action}\"; " + query.replace("\n","")

    # execute the new query
    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        # raise error
        raise Exception(
            status_code=400,
            detail=f"Failed to explain the query after changing the enable_hashjoin knob.")
    else:
        if action == "ON":
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after enabling the hashjoin operator."
        else:
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after disabling the hashjoin operator."

    return text_output

def enable_or_disable_indexonlyscan_operator(action: str, query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    # add hint to the query
    new_query = f"set enable_indexonlyscan to \"{action}\"; " + query.replace("\n","")

    # execute the new query
    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        # raise error
        raise Exception(
            status_code=400,
            detail=f"Failed to explain the query after changing the enable_indexonlyscan knob.")
    else:
        if action == "ON":
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after enabling the indexonlyscan operator."
        else:
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after disabling the indexonlyscan operator."

    return text_output

def enable_or_disable_indexscan_operator(action: str, query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    # add hint to the query
    new_query = f"set enable_indexscan to \"{action}\"; " + query.replace("\n","")

    # execute the new query
    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        # raise error
        raise Exception(
            status_code=400,
            detail=f"Failed to explain the query after changing the enable_indexscan knob.")
    else:
        if action == "ON":
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after enabling the indexscan operator."
        else:
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after disabling the indexscan operator."

    return text_output

def enable_or_disable_material_operator(action: str, query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    # add hint to the query
    new_query = f"set enable_material to \"{action}\"; " + query.replace("\n","")

    # execute the new query
    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        # raise error
        raise Exception(
            status_code=400,
            detail=f"Failed to explain the query after changing the enable_material knob.")
    else:
        if action == "ON":
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after enabling the material operator."
        else:
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after disabling the material operator."

    return text_output

def enable_or_disable_mergejoin_operator(action: str, query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    # add hint to the query
    new_query = f"set enable_mergejoin to \"{action}\"; " + query.replace("\n","")

    # execute the new query
    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        # raise error
        raise Exception(
            status_code=400,
            detail=f"Failed to explain the query after changing the enable_mergejoin knob.")
    else:
        if action == "ON":
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after enabling the mergejoin operator."
        else:
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after disabling the mergejoin operator."

    return text_output

def enable_or_disable_nestloop_operator(action: str, query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    # add hint to the query
    new_query = f"set enable_nestloop to \"{action}\"; " + query.replace("\n","")

    # execute the new query
    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        # raise error
        raise Exception(
            status_code=400,
            detail=f"Failed to explain the query after changing the enable_nestloop knob.")
    else:
        if action == "ON":
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after enabling the nestloop operator."
        else:
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after disabling the nestloop operator."

    return text_output

def enable_or_disable_parallel_append_operator(action: str, query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    # add hint to the query
    new_query = f"set enable_parallel_append to \"{action}\"; " + query.replace("\n","")

    # execute the new query
    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        # raise error
        raise Exception(
            status_code=400,
            detail=f"Failed to explain the query after changing the enable_parallel_append knob.")
    else:
        if action == "ON":
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after enabling the parallel_append operator."
        else:
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after disabling the parallel_append operator."

    return text_output

def enable_or_disable_parallel_hash_operator(action: str, query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    # add hint to the query
    new_query = f"set enable_parallel_hash to \"{action}\"; " + query.replace("\n","")

    # execute the new query
    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        # raise error
        raise Exception(
            status_code=400,
            detail=f"Failed to explain the query after changing the enable_parallel_hash knob.")
    else:
        if action == "ON":
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after enabling the parallel_hash operator."
        else:
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after disabling the parallel_hash operator."

    return text_output

def enable_or_disable_partition_pruning_operator(action: str, query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    # add hint to the query
    new_query = f"set enable_partition_pruning to \"{action}\"; " + query.replace("\n","")

    # execute the new query
    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        # raise error
        raise Exception(
            status_code=400,
            detail=f"Failed to explain the query after changing the enable_partition_pruning knob.")
    else:
        if action == "ON":
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after enabling the partition_pruning operator."
        else:
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after disabling the partition_pruning operator."

    return text_output

def enable_or_disable_seqscan_operator(action: str, query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    # add hint to the query
    new_query = f"set enable_seqscan to \"{action}\"; " + query.replace("\n","")

    # execute the new query
    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        # raise error
        raise Exception(
            status_code=400,
            detail=f"Failed to explain the query after changing the enable_seqscan knob.")
    else:
        if action == "ON":
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after enabling the seqscan operator."
        else:
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after disabling the seqscan operator."

    return text_output

def enable_or_disable_sort_operator(action: str, query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    # add hint to the query
    new_query = f"set enable_sort to \"{action}\"; " + query.replace("\n","")

    # execute the new query
    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        # raise error
        raise Exception(
            status_code=400,
            detail=f"Failed to explain the query after changing the enable_sort knob.")
    else:
        if action == "ON":
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after enabling the sort operator."
        else:
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after disabling the sort operator."

    return text_output


def enable_or_disable_tidscan_operator(action: str, query: str):

    dbargs = DBArgs("postgresql", config=postgresql_conf)  # todo assign database name
    db = Database(dbargs, timeout=-1)
    # add hint to the query
    new_query = f"set enable_tidscan to \"{action}\"; " + query.replace("\n"," ")

    # execute the new query
    new_query_plan = db.pgsql_query_plan(new_query)

    if new_query_plan is None:
        # raise error
        raise Exception(
            status_code=400,
            detail=f"Failed to explain the query after changing the enable_tidscan knob.")
    else:
        if action == "ON":
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after enabling the tidscan operator."
        else:
            total_cost, operators = db.query_plan_statistics(
                new_query_plan)
            text_output = f"The new query plan statistics: total cost is {total_cost} and the operators are {operators},  after disabling the tidscan operator."

    return text_output
