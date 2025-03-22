import httpx
import os

NOTION_API_URL = "https://api.notion.com/v1/pages"
NOTION_VERSION = "2022-06-28"
NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
DATABASE_ID = os.environ.get("DATABASE_ID")


headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json"
}

def create_notion_page(data):
    payload = {
        "parent": {"database_id": DATABASE_ID},
     "properties": {
    "title": {"title": [{"text": {"content": data.title}}]},
    "category": {"select": {"name": data.category}},
    "goal": {"rich_text": [{"text": {"content": data.goal}}]},
    "character": {"rich_text": [{"text": {"content": data.character}}]},
    "prompt": {"rich_text": [{"text": {"content": data.prompt}}]},
    "input_data": {"rich_text": [{"text": {"content": data.input_data}}]},
    "notes": {"rich_text": [{"text": {"content": data.notes}}]},
    "output_format": {"select": {"name": data.output_format}},
    "status": {"select": {"name": data.status}}
}
    }
    response = httpx.post(NOTION_API_URL, headers=headers, json=payload, timeout=20.0)

    return response.status_code, response.json()
