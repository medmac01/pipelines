from typing import List, Union, Generator, Iterator
from schemas import OpenAIChatMessage
import subprocess
import requests

class Pipeline:
    def __init__(self):
        # Optionally, you can set the id and name of the pipeline.
        # Best practice is to not specify the id so that it can be automatically inferred from the filename, so that users can install multiple versions of the same pipeline.
        # The identifier must be unique across all pipelines.
        # The identifier must be an alphanumeric string that can include underscores or hyphens. It cannot contain spaces, special characters, slashes, or backslashes.
        # self.id = "python_code_pipeline"
        self.name = "Threat Hunting Assistant"
        pass

    async def on_startup(self):
        # This function is called when the server is started.
        print(f"on_startup:{__name__}")
        pass

    async def on_shutdown(self):
        # This function is called when the server is stopped.
        print(f"on_shutdown:{__name__}")
        pass

    def invoke_agents(self, input:str):
        base_url = "threat_hunt_agents_api-sonic_ai-1:3333/api/answer_v2/"
        headers = {
          'Content-Type': 'application/json',
          'Authorization': 'Token 42af1c549bd22daaa542ef9436903260b472c370'
        }
        body = { "query": input }
      
        try:
            response = requests.post(base_url, headers=headers, json=body)
            if response.status_code != 200:
                  return "An error has occured, consider trying again"
            
            resp = response.json()
            return resp['output']['output']
              
          
        except:
            return 'An exception occured'

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, Generator, Iterator]:
        # This is where you can add your custom pipelines like RAG.
        print(f"pipe:{__name__}")

        print(messages)
        print(user_message)

        if body.get("title", False):
            print("Title Generation")
            return "New conversation"
        else:
            response = self.invoke_agents(user_message)
            return response
