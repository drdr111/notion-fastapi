from pydantic import BaseModel
from typing import Optional

class PromptData(BaseModel):
    title: str
    category: str
    goal: str
    character: str
    prompt: str
    output_format: str
    input_data: str
    notes: Optional[str] = ""
    status: str
