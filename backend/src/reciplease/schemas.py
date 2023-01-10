from enum import Enum

from pydantic import AnyHttpUrl, BaseModel


class FMFormat(str, Enum):
    yaml = 'yaml'
    toml = 'toml'


class RecipeIn(BaseModel):
    url: AnyHttpUrl
    front_matter: FMFormat | None = None


class RecipeOut(BaseModel):
    message: str


class RecipeInfo(BaseModel):
    # at least title, ingredients, and instructions need to exist

    source_url: str
    site_name: str | None

    title: str
    description: str | None
    author: str | None
    image: str | None

    language: str | None
    category: str | None
    yields: str | None
    total_time: int | None
    prep_time: int | None
    cook_time: int | None
    nutrients: dict[str, str] | None

    ingredients: list[str]
    instructions_list: list[str]
