#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Developer: Miguel Jara Maldonado.
Creation Date: 2025-04-10.
Description: .
"""

import logging

import streamlit as st
from pydantic import BaseModel

from mcp_server.ollama_agent_class import OllamaAgent

MCP_SERVER_URL = "http://localhost:4000/sse"
AGENT_URL = "http://localhost:11434/v1"
MODEL_NAME = "qwen2.5:7b"
logger = logging.getLogger(__name__)


class FreeFormResponse(BaseModel):
    content: str


def main():

    # Initialize the Ollama agent
    agent = OllamaAgent(
        model_name=MODEL_NAME,
        base_url=AGENT_URL,
    )

    # Streamlit session state for conversation history
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "Hello! How can I assist you today?"}
        ]

    st.title("💬 Chat with Ollama Agent")
    st.caption("🚀 A chatbot powered by Ollama Agent")

    # Display conversation history
    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

    # Input box for user query at the bottom
    if user_query := st.chat_input("Type your message here..."):
        # Add user message to the history session state
        st.session_state["messages"].append({"role": "user", "content": user_query})
        st.chat_message("user").write(user_query)

        # Agent response
        with st.spinner("Agent is thinking..."):
            try:
                # Run the agent and get the result
                # result = asyncio.run(agent.run(user_query))
                result = agent.run(user_query)

                # Extract the 'content' field from the JSON response
                response_content = result.output
                logger.info("Full response:\n" + response_content)

                response_content = response_content.split("[Answer ahead]:")[-1]

                logger.info("Answer:\n" + response_content)
                # Add agent response to session state
                st.session_state["messages"].append(
                    {"role": "assistant", "content": response_content}
                )
                st.chat_message("assistant").write(response_content)

            except Exception as e:
                error_message = f"An error occurred: {e}"
                st.session_state["messages"].append(
                    {"role": "assistant", "content": error_message}
                )
                st.chat_message("assistant").write(error_message)


if __name__ == "__main__":
    main()
