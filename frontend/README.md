# reciplease frontend

Vue.js frontend for **reciplease**

-----

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)


## Installation

with docker:
```console
git clone git@github.com:patrickarmengol/reciplease.git
cd reciplease/frontend

docker build -t reciplease-frontend .
docker run -it -p 8080:80 --rm reciplease-frontend
```

without docker:
```console
git clone git@github.com:patrickarmengol/reciplease.git
cd reciplease/frontend

npm install
npm install -g http-server
npm run build
http-server dist
```

## Usage

submit a recipe URL like https://www.allrecipes.com/recipe/190276/easy-shakshuka/ to the form and view/edit response markdown in the pane below the form

## License

`reciplease` is distributed under the terms of any of the following licenses:

- [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html)
- [MIT](https://spdx.org/licenses/MIT.html)