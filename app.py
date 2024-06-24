# -*- coding: utf-8 -*-
"""redis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VF1AND3ucPE1GDpHDVfM2YQD8n8owwpD
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from redis import Redis
from rq import Queue
from llama_cpp import Llama

# Initialize the FastAPI app and Redis Queue
app = FastAPI()
redis_conn = Redis(host="localhost", port=6379, db=0)
q = Queue(connection=redis_conn)

# Load the LLM model
model_path = "models/llava-v1.6-mistral-7b.Q4_K_M.gguf"
llm = Llama(model_path=model_path)


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str


def handle_query(question):
    system_message = "You are a helpful assistant"
    user_message = f"Q: {question} A: "
    prompt = f"""<s>[INST] <<SYS>>
{system_message}
<</SYS>>
{user_message} [/INST]"""
    output = llm(prompt, max_tokens=2000, stop=["Q:", "\n"], echo=False)
    response_text = output["choices"][0]["text"].strip()
    response_text = response_text.split("[/INST]")[-1].strip()
    return response_text


@app.post("/query", response_model=QueryResponse)
async def query_llm(request: QueryRequest):
    job = q.enqueue(handle_query, request.question)
    try:
        response_text = job.result
        return QueryResponse(answer=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)