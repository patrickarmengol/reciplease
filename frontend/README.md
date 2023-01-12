# reciplease frontend

Vue.js frontend for **reciplease**

[live demo](https://reciplease-frontend.up.railway.app/)

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
(if you want to modify the backend API URL, add --build-arg VITE_API_URL="<API URL here>", or use a .env)
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

submit a recipe URL like https://www.allrecipes.com/recipe/190276/easy-shakshuka/ to the form and view/edit response markdown in the pane that appears below

## License

`reciplease` is distributed under the terms of any of the following licenses:

- [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html)
- [MIT](https://spdx.org/licenses/MIT.html)