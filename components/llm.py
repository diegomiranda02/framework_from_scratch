import requests
import json

class OllamaModel:
    def __init__(self, model, 
                 system_prompt, 
                 temperature=0, 
                 stop=None,
                 headers=None,
                 format=None,
                 inference_server=None):
        """
        Initializes the OllamaModel with the given parameters.
        Example:
        headers = {"Content-Type": "application/json"}
        format = json
        """
        self.model_endpoint = inference_server + "/api/generate"
        self.temperature = temperature
        self.model = model
        self.system_prompt = system_prompt
        self.headers = headers
        self.stop = stop
        self.format = format

    def generate_text(self, prompt):
        """
        Generates a response from the Ollama model based on the provided prompt.
        """
        payload = {
            "model": self.model,
            "format": self.format,
            "prompt": prompt,
            "system": self.system_prompt,
            "stream": False,
            "temperature": self.temperature,
            "stop": self.stop
        }

        #print(f"PROMPT: {prompt}")

        try:
            request_response = requests.post(
                self.model_endpoint, 
                headers=self.headers, 
                data=json.dumps(payload)
            )
            
            # Debug log
            #print(f"REQUEST RESPONSE STATUS: {request_response.status_code}")
            #print(f"REQUEST RESPONSE TEXT: {request_response.text}")

            
            request_response_json = request_response.json()

            if self.format == "json":
                # Ensure that 'response' key exists in the JSON response
                if 'response' in request_response_json:
                    response = request_response_json['response']
                    response_dict = json.loads(response)
                    print(f"\n\nResponse from Ollama model: {response_dict}")
                    return response_dict
                else:
                    # If no response key is found, return an empty response or error
                    return {"error": "No valid response from Ollama model!"}
            
            else:
                return request_response_json['response']
                
        except requests.RequestException as e:
            # Handle request exception
            return {"error": f"Error in invoking model! {str(e)}"}

    def __call__(self, prompt):
        """
        Makes the class callable, directly invoking the generate_text method when called.

        Parameters:
        prompt (str): The user query to generate a response for.

        Returns:
        dict: The response from the model as a dictionary.
        """
        return self.generate_text(prompt)
