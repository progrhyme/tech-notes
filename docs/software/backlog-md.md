# Backlog.md

[Backlog.md](https://github.com/MrLesk/Backlog.md) は、Git リポジトリの中の Markdown ファイルで、タスクを管理するツール。
CLI と、ローカルの Web UI（かんばんボード）を備える。MIT ライセンス。

2026-11-23 時点で、バージョン 1.57.4 を試した。GitHub のスター数は約 7,500。最終プッシュは 2026-11-22 で、活発に開発されている。

## 特徴

- 1タスク1ファイルの Markdown（YAML frontmatter 付き）で、プロジェクトの中に置く。Git で履歴を追える。
- CLI（`backlog`）で、タスクの作成、一覧、編集、検索ができる。`--json` で機械可読な出力を、`--plain` でプレーンテキストの出力を得られる。
- `backlog browser` で、ローカルの Web UI を起動する。かんばんボード、タスクの一覧、マイルストーンの画面がある。
- 子タスク（サブタスク）、マイルストーン、タスク間の依存を持てる。
- AI エージェント向けの連携（MCP サーバ、CLI の指示文の出力）がある。

## インストールと初期化

npm のパッケージ `backlog.md` として配布されている。プロジェクトに入れる場合は、`devDependencies` に追加し、`npx backlog` で実行する。

```sh
npm install -D backlog.md
npx backlog init "プロジェクト名" --defaults --integration-mode none --backlog-dir .backlog
```

- `--defaults`: 対話をせず、既定値で初期化する。
- `--integration-mode`: AI 連携の方式（`cli`、`mcp`、`none`）。既定は `cli` で、エージェント向けの指示ファイル（`AGENTS.md` など）を書き込む。書き換えさせたくなければ、`none` にする。
- `--backlog-dir`: データを置くディレクトリ。`backlog`、`.backlog`、または任意のプロジェクト内のパス。
- `--task-prefix`: タスク ID の接頭辞（英字のみ。既定は `task`）。初期化のあとは変えられない。
- `--no-git`: Git と連携せず、ファイルシステムだけで使う。

## ディレクトリ構成

データのディレクトリの下に、種類ごとのサブディレクトリができる。

| ディレクトリ | 内容 |
| :--- | :--- |
| `tasks/` | タスク |
| `milestones/` | マイルストーン |
| `drafts/` | 下書きのタスク |
| `decisions/` | 決定記録 |
| `docs/` | ドキュメント |
| `archive/` | アーカイブしたもの |

- 設定ファイルの場所は、データのディレクトリによって変わる。
    - 既定の `backlog/` や `.backlog/` では、その中の `config.yml`。
    - `--backlog-dir` で任意のパスにしたときは、プロジェクトのルートの `backlog.config.yml`（設定の `backlog_directory` で、データの場所を指す）。

## タスクのファイル

ファイル名は `<ID> - <タイトルから作った名前>.md`（例: `task-10.1 - Add-login-screen.md`）。frontmatter には、次のようなキーが入る。

```yaml
id: TASK-10.1
title: Add login screen
status: To Do
assignee: []
created_date: '2026-11-22T23:20:40Z'
labels: []
milestone: m-1
dependencies: []
parent_task_id: TASK-10
ordinal: 16000
```

`status` の既定の値は、`To Do`、`In Progress`、`Done`。
本文は、`<!-- SECTION:DESCRIPTION:BEGIN -->` などのコメントで区切られた節に入る。

## CLI

```sh
npx backlog task create "タイトル" -d "説明" -s "To Do" --parent 10 -m m-1
npx backlog task list --plain
npx backlog task view 10.1 --plain
npx backlog task edit 10.1 -s "In Progress"
npx backlog milestone add "マイルストーン名"
npx backlog milestone list
npx backlog search "キーワード"
npx backlog browser --no-open --port 6420
```

- `task create` と `task edit` の主なオプション: `-d`（説明）、`-s`（ステータス）、`-m`（マイルストーン）、`--parent`（親タスク）、`-t`（タイトル）。
- `task edit` に `--clear-milestone` を付けると、マイルストーンの割り当てを外す。
- そのほかのサブコマンド: `task archive`、`task delete`、`milestone rename`、`milestone remove`、`milestone archive`、`config`、`board`（ターミナル上のかんばんボード）。
- `backlog config set <キー> <値>` で、設定を変える。

## 子タスク（階層）

- `task create --parent <ID>` で、子タスクを作る。子タスクの ID は、親の ID にドット区切りで連なる（`TASK-1`、`TASK-1.1`、`TASK-1.1.1`）。
- 4階層（`TASK-1.1.1.1`）まで作れることを確認した。上限は未確認。
- ファイルの上では、階層はディレクトリではなく、frontmatter の `parent_task_id` で表す。すべてのタスクが `tasks/` に平らに置かれる。

## マイルストーン

- `milestone add` で作ると、`m-0`、`m-1` のような ID が付く。タスクは `task edit -m <ID>` で割り当てる。
- 1つのタスクが入れるマイルストーンは、1つだけ。
- `milestone list` で、マイルストーンごとの進捗（完了数 / 全体）が見える。全タスクが Done になったマイルストーンは、完了済みの欄に移る。
- Web UI のマイルストーンの画面には、割り当てのないタスクの欄が出る。

## Web UI

- `backlog browser` で起動する。既定のポートは 6420。待ち受けは `127.0.0.1` だけで、LAN の他の端末からは見えない。
- `--no-open` を付けると、ブラウザを自動で開かない。`--port` でポートを変える。
- `backlog browser export <ディレクトリ>` で、静的なファイルに書き出せる。
- 画面は、かんばんボード、タスクの一覧、マイルストーン、ドラフト、統計。かんばんボードは、ドラッグ&ドロップでステータスを変えられる。

## 制限事項と注意点

冒頭に書いた時点とバージョンで、試してわかったこと。

### 階層の表示

- かんばんボードとタスクの一覧は、階層を表さず、タスクが平らに並ぶ。親子関係を木として見るビューはない。
- 階層が見えるのは、タスクの詳細の「Subtasks」欄だけ。直下の子だけが出て、クリックで子に移る。

### ファイル名

- ファイル名は、`<ID> - <タイトル>.md` の形に、コードで決め打ちされている。設定では変えられない。
- タイトルから除かれる文字: `' ( ) , ! @ # $ % ^ & + = [ ] { } ;`
- パスに使えない文字（`<>:"/\|?*`）と空白は、`-` に置き換わる。
- 日本語とバッククォートは、そのまま残る。
- ファイル名を `task-4.md` や `task-10.1 - login-screen.md` に直接変えても、読み込める。状態やタイトルを編集しても、変えた名前は保たれる。
- ただし、新しく作るタスクは、タイトルから作った名前になる。名前をそろえたいときは、作成のあとに、改名する処理（スクリプトなど）が要る。

### マイルストーンの指定

- `task edit -m "<タイトル>"` のようにタイトルで指定すると、別のマイルストーンに割り当たることがあった。ID（`m-1`）で指定すると、意図どおりに動いた。
- `milestone rename` を ID で指定して連続で実行したところ、意図と違うマイルストーンのタイトルが書き換わった。原因は調べていない。`milestone rename` には、頼らないほうがよい。

### その他

- `remoteOperations`（既定で有効）のままで、Git のリモートがないと、警告が出る。`backlog config set remoteOperations false` で消せる。
- Backlog.md が管理するタスクの内容（frontmatter と本文）は、手で編集せず、CLI で操作するのがよい。ファイル名の直接の変更は、上に書いたとおり、許容される。

## 参考

- [Backlog.md の GitHub リポジトリ](https://github.com/MrLesk/Backlog.md)
- [2026-11-23 のメモ](../memo/2026/20261123.md): TODO 管理の OSS の比較と、Backlog.md を試した作業ログ
