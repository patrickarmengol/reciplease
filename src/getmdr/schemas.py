from pydantic import AnyHttpUrl, BaseModel


class RecipeUrl(BaseModel):
    recipe_url: AnyHttpUrl


class MarkdownRecipe(BaseModel):
    markdown: str
