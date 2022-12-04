import pydantic


class Action(pydantic.BaseModel):
    text: str
    num_objects: int


class Object(pydantic.BaseModel):
    text: str
