from fastapi import FastAPI

from reciplease import schemas
from reciplease.conversion import convert_info_to_markdown
from reciplease.scraping import scrape_recipe_url

app = FastAPI()


@app.post('/', response_model=schemas.RecipeMarkdown)
def md_recipe(recipe_in: schemas.RecipeIn):
    scraped_info = scrape_recipe_url(recipe_in.url)
    return convert_info_to_markdown(scraped_info, front_matter=recipe_in.front_matter)
