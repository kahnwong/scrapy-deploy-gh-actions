# scrapy-deploy-gh-actions

## Setup
1. Install prereqs:
```
pipenv install

pipenv shell
pipenv run pip freeze > requirements.txt # for deployment only

scrapy startproject tutorial
```

2. Move the content inside newly created `tutorial` folder to root.

3. Create `scrapinghub.yml` with following config;
```yml
project: ${PROJECT_ID}

requirements:
  file: requirements.txt

stack: scrapy:${YOUR_SCRAPY_VERSION_IN_PIPFILE}
apikey: null
```

See [here](https://github.com/scrapinghub/scrapinghub-stack-scrapy/releases) for list of available versions.

## Notes
Run `shub deploy` locally once so it would generate `setup.py`, that way you can edit config to add extra resources to deployment.
