# drf-doc-demo

[DjangoCongress JP 2022](https://djangocongress.jp/)
「OAI3を使ったDjango REST frameworkのドキュメント生成とカスタマイズ」
のサンプルコードです。


## Setting

install packages with poetry

```bash
git clone git@github.com:shihono/drf-doc-demo.git
cd drf-doc-demo
poetry install
```

django set up

```bash
cd drf_doc_demo
poetry run python manage.py migrate
```

## Usage

```bash
poetry run python manage.py runserver
```

Starting server at http://127.0.0.1:8000/

### drf-spectacularを使ったドキュメント生成

[drf-spectacular](https://github.com/tfranzel/drf-spectacular)

- oai http://127.0.0.1:8000/api/schema/
- swagger-ui http://127.0.0.1:8000/api/schema/swagger-ui/
