from pydantic import BaseModel, PydanticValueError, ValidationError, validator


# Pydantic Error를 상속 받아 커스텀 에러 정의 가능
class NotABarError(PydanticValueError):
    code = "not_a_bar"
    msg_template = "value is not 'bar', got '{wrong_value}'"  # 인자로 주입


class Model(BaseModel):
    foo: str

    @validator("foo")
    def value_must_equal_bar(cls, value):
        if value != "bar":
            raise NotABarError(wrong_value=value)
        return value


try:
    Model(foo="ber")
except ValidationError as err:
    print(err.json())
    # [
    #   {
    #     "loc": [
    #       "foo"
    #     ],
    #     "msg": "value is not 'bar', got 'ber'",
    #     "type": "value_error.not_a_bar",
    #     "ctx": {
    #       "wrong_value": "ber"
    #     }
    #   }
    # ]
