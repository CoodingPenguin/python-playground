from typing import Any
from xml.etree.ElementTree import fromstring

from pydantic import BaseModel
from pydantic.utils import GetterDict

xml_string = """
<User Id="2138">
    <FirstName />
    <LoggedIn Value="true" />
</User>
"""


class UserGetter(GetterDict):
    def get(self, key: str, default: Any) -> Any:
        if key in {"Id", "Status"}:
            return self._obj.attrib.get(key, default)
        else:
            try:
                return self._obj.find(key).attrib["Value"]
            except (AttributeError, KeyError):
                return default


class User(BaseModel):
    Id: int
    Status: str | None
    FirstName: str | None
    LastName: str | None
    LoggedIn: bool

    class Config:
        orm_mode = True
        getter_dict = UserGetter  # 딕셔너리와 유사한 인터페이스를 파싱할 수 있도록 함


user = User.from_orm(fromstring(xml_string))
print(user)  # Id=2138 Status=None FirstName=None LastName=None LoggedIn=True
