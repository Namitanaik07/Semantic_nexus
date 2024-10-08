import os
from langchain import HuggingFaceHub
os.environ['HUGGINGFACEHUB_API_TOKEN'] = "your_huggingface_api_key"
flan_t5 = HuggingFaceHub(
    repo_id="google/flan-t5-xxl",
    model_kwargs={"temperature": 0.8, "max_length": 1000}
)
print("Flan-T5-XXL model has been successfully initialized!")
from langchain.prompts import PromptTemplate
from langchain import LLMChain
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="You are an expert in explaining concepts. Please answer the following question in a clear and concise manner: {question}"
)
llm_chain = LLMChain(llm=flan_t5, prompt=prompt_template)
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()


templates = Jinja2Templates(directory="templates")
