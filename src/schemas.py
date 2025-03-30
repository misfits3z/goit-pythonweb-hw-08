from datetime import date, datetime
from typing import  Optional
from pydantic import BaseModel, Field, EmailStr, constr, ConfigDict


# Модель для створення контакту
class ContactCreate(BaseModel):
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    email: EmailStr
    phone_number: str = constr(regex=r"^\+?[1-9]\d{1,14}$")  
    birth_date: date
    note: Optional[str] = Field(max_length=250)

    class Config:
        orm_mode = True


# Модель для відповіді, що містить дані про контакт
class ContactResponse(ContactCreate):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birth_date: datetime
    note: str
    created_at: datetime | None  
    updated_at: Optional[
        datetime
    ] 
    model_config = ConfigDict(from_attributes=True)  
