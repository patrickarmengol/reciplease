from typing import Any, Callable

from recipe_scrapers import scrape_me

from reciplease.schemas import RecipeInfo

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
}


def get_field(field: Callable[[], Any]) -> Any:
    try:
        return field()
    except Exception as _:
        # print(e)
        return None


def scrape_recipe_url(url: str) -> RecipeInfo:
    # TODO: validate url; exists and points to recipe

    scraper = scrape_me(url)

    try:
        info = RecipeInfo(
            source_url=url,
            site_name=get_field(scraper.site_name),

            title=get_field(scraper.title),
            description=get_field(scraper.description),
            author=get_field(scraper.author),
            image=get_field(scraper.image),

            language=get_field(scraper.language),
            category=get_field(scraper.category),
            yields=get_field(scraper.yields),
            total_time=get_field(scraper.total_time),
            prep_time=get_field(scraper.prep_time),
            cook_time=get_field(scraper.cook_time),
            nutrients=get_field(scraper.nutrients),

            ingredients=get_field(scraper.ingredients),
            instructions_list=get_field(scraper.instructions_list),
        )
    except Exception as e:
        raise Exception(f'error scraping recipe: {e}')

    return info
