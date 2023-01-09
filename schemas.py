from pydantic import BaseModel, Field
class Message(BaseModel):
    message: str = Field(min_length=1)
    number: str = Field(min_length=1, max_length=30)