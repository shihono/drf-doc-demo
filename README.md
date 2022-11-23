# drf-doc-demo

[DjangoCongress JP 2022](https://djangocongress.jp/)
「OAI3を使ったDjango REST frameworkのドキュメント生成とカスタマイズ」
のサンプルコードです。

## 発表資料
- [Speaker Deck](https://speakerdeck.com/shihono/djangocongress-jp-2022)
- [PDF](https://shihono.github.io/pdfs/djangocongress_jp_2022_oai3_drf.pdf)

資料のfooterに記載しているブランチ名とこのレポジトリのブランチ名が対応しています。

ブランチごと異なる方法でドキュメント生成を実装しています。

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