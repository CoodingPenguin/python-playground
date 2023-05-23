from pydantic import BaseModel, Field
from sqlalchemy import JSON, Column, Integer
from sqlalchemy.orm import declarative_base


class MyModel(BaseModel):
    # SQLAlchemy의 metadata_를 alias할 수 있음
    metadata: dict[str, str] = Field(alias="metadata_")

    class Config:
        orm_mode = True


Base = declarative_base()


class SQLModel(Base):
    __tablename__ = "my_table"
    id = Column("id", Integer, primary_key=True)
    # "metadata"는 SQLAlchemy의 예약어라서 _를 뒤에 붙임
    metadata_ = Column("metadata", JSON)


sql_model = SQLModel(metadata_={"key": "value"}, id=1)

pydantic_model = MyModel.from_orm(sql_model)

print(pydantic_model.dict())
print(pydantic_model.dict(by_alias=True))
