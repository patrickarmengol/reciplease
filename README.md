# reciplease

API to scrape recipes from your favorite site and output to simple, clean markdown

[live demo](https://web-production-b827.up.railway.app)
[live demo docs](https://web-production-b827.up.railway.app/docs)

-----

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

with docker:
```console
git clone git@github.com:patrickarmengol/reciplease.git
cd reciplease

docker build -t reciplease .
docker run -d -e PORT=8000 -p 8000:8000 reciplease
```

without docker:
```console
git clone git@github.com:patrickarmengol/reciplease.git
cd reciplease

python -m venv venv
source venv/bin/activate
pip install --upgrade build hatchling && pip install .

uvicorn reciplease.main:app --host 0.0.0.0 --port 8000
```

## Usage

see generated docs after installation at http://0.0.0.0:8000/docs

or view the [live demo docs](https://web-production-b827.up.railway.app/docs)

## License

`reciplease` is distributed under the terms of any of the following licenses:

- [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html)
- [MIT](https://spdx.org/licenses/MIT.html)
