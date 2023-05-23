from pydantic import BaseModel, ValidationError, validator


class User(BaseModel):
    name: str
    username: str
    password1: str
    password2: str

    # value: 검증할 필드로, 변수명은 내가 하고 싶은 거 하면 됨
    # values: 검증 이전에 name-to-value로 매핑된 딕셔너리
    # config: 모델 설정 값 (class Config로 설정된 값들)
    @validator("name")
    def name_must_contain_space(cls, value: str):
        if " " not in value:
            raise ValueError("must contain a space")
        return value.title()

    # 검증은 정의된 순서대로 진행됨
    # 만약 앞에서 검증 실패가 되면, 해당 필드는 values에 저장이 안 됨
    def passwords_match(cls, value, values, **kwargs):
        if "password1" in values and value != values["password1"]:
            raise ValueError("passwords do not match")
        return value

    @validator("username")
    def username_alphanumeric(cls, value: str):
        assert value.isalnum(), "must be alphanumeric"
        return value


user = User(
    name="samuel colvin", username="scolvin", password1="asdf", password2="asdf"
)
print(user)  # name='Samuel Colvin' username='scolvin' password1='asdf' password2='asdf'

try:
    User(name="samuel", username="scolvin", password1="asdf", password2="qwerty")
except ValidationError as err:
    print(err)
    # 2 validation errors for User
    # name
    #   must contain a space (type=value_error)
    # password2
    #   passwords do not match (type=value_error)
