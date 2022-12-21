from pydantic import BaseModel

class URLBase(BaseModel):
    target_url: str

class URL(URLBase):
    is_active: bool
    num_clicks: int

    class Config:
        orm_mode = True

class URLInfo(URL):
    url: str
    pwd: str

