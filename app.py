import os
from langchain import HuggingFaceHub
os.environ['HUGGINGFACEHUB_API_TOKEN'] = "your_huggingface_api_key"
flan_t5 = HuggingFaceHub(
    repo_id="google/flan-t5-xxl",
    model_kwargs={"temperature": 0.8, "max_length": 1000}
)
print("Flan-T5-XXL model has been successfully initialized!")
