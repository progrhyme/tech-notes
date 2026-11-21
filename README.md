# progrhyme's Tech Notes

IT技術についての個人的なメモ。https://progrhy.me/tech-notes/ で公開している。

[Zensical](https://zensical.org/) でビルドし、GitHub Pages に GitHub Actions でデプロイする。
Python の依存は [uv](https://docs.astral.sh/uv/) で管理する。

## 使い方

```sh
uv sync            # 依存を入れる
uv run zensical serve   # ローカルでプレビュー(http://localhost:8000/)
uv run zensical build --clean   # site/ にビルド
```

## 構成

- `docs/`: 記事(Markdown)
- `zensical.toml`: サイトの設定。`nav` に全ページを明記する
- `.github/workflows/deploy.yml`: デプロイ
- `.github/workflows/ci.yml`: `scripts/`、`tests/`、`pyproject.toml`、`uv.lock` の変更を、pytest で検査する

旧 Hugo 版は `archive/hugo-doxy` ブランチに残している。
