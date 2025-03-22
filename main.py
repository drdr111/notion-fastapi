from fastapi import FastAPI
from models import PromptData
from notion_client import create_notion_page

app = FastAPI()

@app.post("/add-prompt/")
async def add_prompt(prompt: PromptData):
    status_code, response = create_notion_page(prompt)
    return {"status_code": status_code, "response": response}
