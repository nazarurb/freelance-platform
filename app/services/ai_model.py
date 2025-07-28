import os
import urllib.request

from llama_cpp import Llama

from app.core.config import config


class AIModel:

    MODEL_URL = config.MODEL_URL
    MODEL_FILENAME = config.MODEL_FILENAME

    def __init__(self):
        self.download_model()
        self.llm = Llama(model_path=self.MODEL_FILENAME, n_ctx=2048, max_tokens=2048, n_batch=126)

    def download_model(self):
        if not os.path.isfile(self.MODEL_FILENAME):
            print("🔽 Loading AI model...")
            urllib.request.urlretrieve(self.MODEL_URL, self.MODEL_FILENAME)
            print("✅ Model successfully loaded!")
        else:
            print("✅ The model already exists, no download required.")

    def generate_text(
            self,
            prompt,
            max_tokens=256,
            temperature=0.1,
            top_p=0.5,
            echo=False,
            stop=["#"]
    ):
        output = self.llm(
            prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            echo=echo,
            stop=stop,
        )
        output_text = output["choices"][0]["text"].strip()
        return output_text
