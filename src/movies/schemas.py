from pydantic import BaseModel
from typing import Optional

class DvdBase(BaseModel):
    dvdtitle: Optional[str]
    dvdgenre:Optional[ str]
    dvditems: Optional[int]
    id: Optional[int] = None #efoson to id einai autoincrement


class Dvd(DvdBase):
    id: int
    dvdtitle: str
    dvdgenre: str
    dvditems: int
    class Config:
        orm_mode = True
    