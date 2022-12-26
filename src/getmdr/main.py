from fastapi import FastAPI

from getmdr import schemas

app = FastAPI()


@app.post('/', response_model=schemas.MarkdownRecipe)
def md_recipe(url: schemas.RecipeUrl):
    return {'markdown': 'hi'}
