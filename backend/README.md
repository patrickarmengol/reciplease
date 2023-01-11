# reciplease backend

FastAPI backend for **reciplease**

-----

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

with docker:
```console
git clone git@github.com:patrickarmengol/reciplease.git
cd reciplease/backend

docker build -t reciplease-backend .
docker run -it -p 5000:5000 --rm reciplease-backend
```

without docker:
```console
git clone git@github.com:patrickarmengol/reciplease.git
cd reciplease/backend

python -m venv venv
source venv/bin/activate
pip install --upgrade build hatchling && pip install .

uvicorn reciplease.main:app --host 0.0.0.0 --port 5000
```

## Usage

see generated docs after installation at http://0.0.0.0:5000/docs

or view the [live demo docs]()

## License

`reciplease` is distributed under the terms of any of the following licenses:

- [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html)
- [MIT](https://spdx.org/licenses/MIT.html)
