from pydantic import BaseModel, constr
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CompanyOrm(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), index=True, nullable=False, unique=True)
    name = Column(String(63), unique=True)
    domains = Column(ARRAY(String(255)))


class CompanyModel(BaseModel):
    id: int
    public_key: constr(max_length=20)
    name: constr(max_length=63)
    domains: list[constr(max_length=255)]

    class Config:
        orm_mode = True


co_orm = CompanyOrm(
    id=123, public_key="foobar", name="Testing", domains=["example.com", "foobar.com"]
)
print(co_orm)  # <__main__.CompanyOrm object at 0x10fc2cb90>

co_model = CompanyModel.from_orm(co_orm)
print(
    co_model
)  # id=123 public_key='foobar' name='Testing' domains=['example.com', 'foobar.com']
