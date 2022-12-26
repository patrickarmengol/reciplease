from fastapi import FastAPI

from getmdr import schemas
from getmdr.conversion import convert_info_to_markdown
from getmdr.scraping import scrape_recipe_url

app = FastAPI()


@app.post('/', response_model=schemas.RecipeMarkdown)
def md_recipe(recipe_in: schemas.RecipeIn):
    scraped_info = scrape_recipe_url(recipe_in.url)
    return convert_info_to_markdown(scraped_info, front_matter=recipe_in.front_matter)
