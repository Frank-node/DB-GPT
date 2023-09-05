from multiagents.registry import Registry
agent_registry = Registry(name="AgentRegistry")

from .base import BaseAgent
from .conversation_agent import ConversationAgent
from .tool_agent import ToolAgent