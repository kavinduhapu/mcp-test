# mcp-test
Tutorials on mcp server integration with LLM apps. Using https://github.com/langchain-ai/langchain-mcp-adapters

## To setup & run
* Create venv and install dependencies on `requirements.txt`
* Create .env file with relavant with API keys for example `GOOGLE_API_KEY`
* Start weather mcp server by
```bash
python3 weather_server.py
```
* Run client using 
```bash
python3 multiple_client.py
```

## To list the tools using MCP inspector

* Make sure NodeJs and npm are installed https://nodejs.org/en/download
* Install MCP cli using pip `pip install mcp-cli`
* Run the server using `python weather_server.py`
* In another terminal run mcp inspector using `mcp dev weather_server.py`
* This will open up web UI in your browser.
* Go to tools section and click on list tools
![alt text](<Screenshot from 2025-11-03 22-33-26.png>)

