from pydantic import BaseModel

#fastapi接口的数据模型
class User(BaseModel):
    first_name: str
    last_name: str
    age: int

    class Config:
        orm_mode = True




