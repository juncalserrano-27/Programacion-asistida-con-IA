# -*- coding: utf-8 -*-
# @Author: Lilia Juncal Serrano Duran
# @Date:   2026-09-18 14:00:42
# @Last Modified by:   Lilia Juncal Serrano Duran
# @Last Modified time: 2026-09-24 16:03:45
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Developer: Miguel Jara Maldonado.
Creation Date: 2025-04-10.
Description: Interface for all system agents to ensure consistent structure.
"""

import logging

from pydantic_ai import Agent
from pydantic_ai.mcp import MCPToolset
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider

MCP_SERVER_URL = "http://127.0.0.1:8080/mcp"
logger = logging.getLogger(__name__)


class OllamaAgent:

    def __init__(self, model_name: str, base_url: str):
        self.model = OllamaModel(
            model_name=model_name,
            provider=OllamaProvider(base_url=base_url),
        )

        self.mcp_server = MCPToolset(MCP_SERVER_URL)

        self.agent = Agent(
            self.model,
            toolsets=[self.mcp_server],
            system_prompt=(
                "You are chat bot assistant. "
                "You can use available tools to help users when required. "
                "Start all your responses with '[Answer ahead]:'."
            ),
        )

    def run(self, prompt: str):
        logger.info(f"Running AI for: {prompt}.")

        result = self.agent.run_sync(prompt)
        return result