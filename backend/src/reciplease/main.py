from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from reciplease import schemas
from reciplease.conversion import convert_info_to_markdown
from reciplease.scraping import scrape_recipe_url

app = FastAPI()


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/', response_model=schemas.RecipeOut)
def md_recipe(recipe_in: schemas.RecipeIn):
    scraped_info = scrape_recipe_url(recipe_in.url)
    return convert_info_to_markdown(scraped_info, front_matter=recipe_in.front_matter)
