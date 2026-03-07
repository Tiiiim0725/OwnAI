
from typing import List

def create_agent(agent_name: str, agent_type: str, agent_settings: dict) -> dict:
    """
    创建一个新的Agent实例。

    :param agent_name: Agent的名称，必须是唯一的。
    :param agent_type: Agent的类型，必须是预定义的类型之一。当前预定义的类型有：system-Agent、sub-Agent。
    :param agent_settings: Agent的设置字典，包含Agent的配置参数，主要是权限等级设置。可以根据后续需求添加其他配置参数。
    :return: 创建的Agent实例的字典表示，包含agent_name、agent_type、agent_settings。
    """
    pass

def delete_agent(agent_name: str) -> None:
    """
    删除指定名称的Agent实例。

    :param agent_name: 要删除的Agent的名称。
    :return: None
    """
    pass

def list_agents() -> List[dict]:
    """
    列出所有已注册的Agent实例。

    :return: 包含所有Agent实例的字典列表，每个字典包含agent_name、agent_type、agent_settings。
    """
    pass