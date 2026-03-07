from logger.logger import logger

import json
import requests

# api_base, api_key, model_name来源于环境变量，环境变量文件即设置是团队另外的人在搭建。
class LLMClient:
    def __init__(self, model_name: str, api_key: str, api_base: str):
        self.model_name = model_name
        self.api_key = api_key
        self.api_base = api_base
        self.abilities_list = self._get_abilities_list()
        self.system_prompt = self._get_system_prompt()
        
        self.assistant_prompt = '' # Agent的系统提示词等待Agent示例创建代码完成再编写
        self.context = [] # Agent的上下文短期对话记录等待Message模块完成再编写
        self.history_file_path = '' # Agent的上下文长期对话记录文件路径等待Message模块完成再编写
        if self.model_name is None:
            logger.error("Model name must be provided")
            raise ValueError("Model name must be provided")
        if self.api_key is None:
            logger.error("API key must be provided")
            raise ValueError("API key must be provided")
        if self.api_base is None:
            logger.error("API base must be provided")
            raise ValueError("API base must be provided")

    def chat(self, user_prompt: str) -> dict:
        """
        与大模型进行对话的基础方法，用于与模型进行一次对话，返回模型的回复。
        :param user_prompt: 用户的输入提示词
        :return: 模型的回复
        """
        messages = self._assemble_message(user_prompt)
        response = self._send_message(messages)
        return response

    def _get_system_prompt(self) -> str:
        """
        获取系统提示词。
        :return: 系统提示词
        """
        system_prompt = f"""
        Your abilities are: {self.abilities_list}
        Your long-term conversation history is stored in the folder {self.history_file_path}, each file represents a conversation segment, with the filename format: history_<number>.json, where higher numbers indicate newer conversations.
        In general, you don't need to check long-term conversation history unless the user explicitly requests it.
        """
        return system_prompt

    
    def _get_abilities_list(self) -> list:
        """
        获取工具列表。
        :return: 工具列表
        """
        pass

    def _send_message(self, messages: list, timeout: int = 60) -> dict:
        """
        发送消息给大模型并返回模型的回复。
        :param messages: 要发送的消息列表
        :return: 模型的回复
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "model": self.model_name,
            "messages": messages
        }
        try:
            response = requests.post(self.api_base, headers=headers, data=json.dumps(data), timeout=timeout)
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            return {"error": str(e)}

    def _assemble_message(self, user_prompt: str) -> list:
        """
        组装消息，将系统提示词、上下文和用户提示词合并为消息列表。
        :param user_prompt: 用户提示词
        :return: 组装后的消息列表
        """
        messages = []
        if self.system_prompt:
            messages.append({"role": "system", "content": f"{self.system_prompt}\n{self.assistant_prompt}"})
        if self.context:
            context_obj = {
                "type": "context",
                "description": "Short-term conversation history",
                "history": self.context
            }
            messages.append({"role": "system", "content": json.dumps(context_obj, ensure_ascii=False)})
        if user_prompt:
            messages.append({"role": "user", "content": user_prompt})
        return messages


