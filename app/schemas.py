from pydantic import BaseModel

class LoginRequest(BaseModel):
    phone: str
    password: str

class LoginResponse(BaseModel):
    message: str

class FormDataResponse(BaseModel):
    id: int
    name: str
    value: str

    class Config:
        orm_mode = True