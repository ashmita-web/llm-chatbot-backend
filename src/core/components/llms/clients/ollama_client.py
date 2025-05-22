# src/core/components/llms/clients/ollama_client.py

from src.core.components.llms.base import BaseLLMClient
import requests

class OllamaClient(BaseLLMClient):
    def __init__(self, config):
        self.model = config.base_model_name or "phi"
        self.base_url = "http://localhost:11434"

    def chat(self, messages, **kwargs):
        prompt = messages[-1]["content"] if messages else "Hello"
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={"model": self.model, "prompt": prompt, "stream": False}
        )
        if response.status_code == 200:
            raw_response = response.json()
            print(f"Ollama raw response JSON: {raw_response}")  # Or use logger.info
            return {"content": raw_response.get("response", "")}
        else:
            raise Exception(f"Ollama error: {response.text}")

    def complete(self, prompt, **kwargs):
        return self.chat([{"role": "user", "content": prompt}], **kwargs)

    def get_model_info(self):
        return {
            "model": self.model,
            "base_url": self.base_url,
            "type": "ollama"
        }

    def bind_tools(self, tools):
        pass
