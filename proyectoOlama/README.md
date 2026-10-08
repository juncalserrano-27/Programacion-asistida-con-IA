# private_local_llm

https://gitlab.abatgroup.de/artificial-intelligence/private_local_llm.git

# Installation guide

1. Install the environment with uv (uv sync).
2. Download Ollama from ollama.ai
3. Run ollama
4. Download the Qwen2.5:7b model with 'ollama pull qwen2.5:7b'
    - Once ollama is installed, you can run the command from the url provided in the terminal to download the model.

Your installed model names can be retrieved using the following command:
    ```
    ollama list
    ``` 
The default server of running ollama (when it is used from cmd) is http://localhost:11434

# Run

Make sure that the ollama service is up.

Activate the venv.
```
.venv\Scripts\activate
```

Run
```python
streamlit run src/llm_runner.py
``` 

MCP run: Once you have configured your MCP server, run it with (run this before the streamlit command):
```python
python src/mcp_server/my_mcp_server.py
```