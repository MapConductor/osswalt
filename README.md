# osswalt

## What `osswalt` is

`osswalt` is AI agent to generate SDK documents from code repository or code diff.

## Documents

- [Design doc](https://docs.google.com/document/d/1lI8GuOGahWlk0jQ8x-Gb125Z_F0iXcjUAE6Npvk0miQ/edit?tab=t.0)

## Environment

- Python 3.13.7
- Ruff (linter)

## Get started

Install packages

```
uv run pip install -r requirements.txt
```

Set `GOOGLE_APPLICATION_CREDENTIALS`

1. Set authentication via terminal ([link](https://cloud.google.com/vertex-ai/docs/authentication?hl=ja#local-development))
2. Add environment variable.

```
export GOOGLE_APPLICATION_CREDENTIALS="$HOME/.config/gcloud/application_default_credentials.json"
```

Run

```
PYTHONPATH=. python src/main.py
```
