import urllib.parse

from getmdr.schemas import RecipeInfo, RecipeMarkdown


def convert_info_to_markdown(info: RecipeInfo, front_matter: str | None = None) -> RecipeMarkdown:
    match front_matter:
        case 'yaml':
            fm = f"""---
title: {info.title}
description: {info.description if info.description else ''}
author: {info.author if info.author else ''}
language: {info.language if info.language else ''}
category: {info.category if info.category else ''}
yields: {info.yields if info.yields else ''}
total_time: {info.total_time if info.total_time else ''}
prep_time: {info.prep_time if info.prep_time else ''}
cook_time: {info.cook_time if info.cook_time else ''}
---
"""
        case 'toml':
            fm = f"""+++
title = "{info.title}"
description = "{info.description if info.description else ''}"
author = "{info.author if info.author else ''}"
language = "{info.language if info.language else ''}"
category = "{info.category if info.category else ''}"
yields = "{info.yields if info.yields else ''}"
total_time = "{info.total_time if info.total_time else ''}"
prep_time = "{info.prep_time if info.prep_time else ''}"
cook_time = "{info.cook_time if info.cook_time else ''}"
+++
"""
        case _:
            fm = ''

    NL = '\n'

    bd = f"""
# {info.title}

{f'![{info.title}]({urllib.parse.quote(info.image)})' if info.image else ''}

{info.description or ''}

---

{f'- Prep time: {info.prep_time}' if info.prep_time else ''}
{f'- Cook time: {info.cook_time}' if info.prep_time else ''}
{f'- Servings: {info.yields}' if info.prep_time else ''}

---

## Ingredients

{NL.join(f'- {i}' for i in info.ingredients)}

---

## Instructions

{NL.join(f'{n}. {i}' for n, i in enumerate(info.instructions_list, start=1))}

---

Source: [{info.site_name}]({urllib.parse.quote(info.source_url)})
"""
    return RecipeMarkdown(markdown=fm+bd)
