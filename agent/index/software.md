# docs/software/ のインデックス

`software/index.md` — ソフトウェア製品の入口。GUI の HTTP クライアント(Postman など)
`software/argo/index.md` — Argo Project の概要。Workflow、CD、Rollouts、Events
`software/argo/cd.md` — Argo CD の機能、デモ、仕様
`software/docker/index.md` — Docker の使い方、ナレッジ、Registry、Docker Hub
`software/docker/dockerfile.md` — Dockerfile のベストプラクティス、.dockerignore、構文
`software/docker/cmd.md` — docker コマンド。v17 のコマンド体系再編、チートシート
`software/docker/image.md` — Docker イメージ。汎用、プログラム言語系
`software/elasticsearch/index.md` — Elasticsearch の Architecture、Kubernetes、Mapping、運用
`software/embulk/index.md` — Embulk の仕様、設定、CLI、トラブル
`software/embulk/plugin.md` — Embulk のプラグイン。Input、Output、File Formatter、Executor
`software/git/index.md` — Git のプロトコル、config、使い方
`software/git/cli.md` — git サブコマンド別の使用例(branch、commit、log、rebase、remote、tag など)
`software/infra-as-code.md` — Infrastructure as Code のソフトウェア。Pulumi、Go CDK、Terraform
`software/k8s/index.md` — Kubernetes のベストプラクティス、ケーススタディ、バージョン、使い方
`software/k8s/concept.md` — Kubernetes の概念。アーキテクチャー、リソースオブジェクト、認証認可、Storage
`software/k8s/ecosystem.md` — Kubernetes の関連ソフトウェア。マニフェスト管理、クラスタ構築、CI/CD
`software/k8s/configmap.md` — ConfigMap の概要
`software/k8s/container.md` — コンテナの設定。CPU・メモリの割当て、コマンドと引数、probe、Lifecycle Hooks
`software/k8s/cronjob.md` — CronJob の仕様と Issues
`software/k8s/deployment.md` — Deployment の spec
`software/k8s/kubectl.md` — kubectl の周辺ツール、設定、ユースケース、サブコマンド、使い方
`software/k8s/kustomize.md` — kustomize の情報源、CLI の使い方
`software/k8s/namespace.md` — Namespace のリソース管理
`software/k8s/pod.md` — Pod のスケジューリングとライフサイクル
`software/k8s/secret.md` — Secret の概要、作成、参照
`software/k8s/service.md` — Service の概要、仕様、type
`software/mysql/index.md` — MySQL の Docker、InnoDB、CLI オプション、仕様、機能、バージョン
`software/mysql/sql.md` — MySQL の SQL。DML、DDL、関数
`software/mysql/client.md` — MySQL クライアントの設定と CLI
`software/systemd/index.md` — systemd(System and Service Manager)の設定と systemctl
`software/systemd/journalctl.md` — journalctl(systemd のログを調べる CLI)の使用例
`software/terraform/index.md` — Terraform の仕様、Examples、ベストプラクティス、バージョン、Tools
`software/terraform/config/index.md` — Terraform の設定。基本文法、変数、型、式、関数、Module など
`software/terraform/config/v0.11.md` — Terraform v0.11 以前の構文
`software/terraform/cli.md` — terraform コマンド。import、output、plan、state、workspace
`software/terraform/backend.md` — Terraform の Backend。gcs、s3
`software/terraform/provider/index.md` — Terraform の Provider。HTTP、Kubernetes、Local、Random、Template
`software/terraform/provider/aws.md` — Terraform の AWS Provider。設定、Data Sources、Resources
`software/terraform/provider/google.md` — Terraform の Google Provider。バージョン、設定、Resources
`software/terraform/editor.md` — Terraform 用のエディタ設定。IntelliJ IDEA、VS Code
`software/terraform/terraformer.md` — terraformer のインストールと使い方
`software/editor/index.md` — エディタ・IDE の入口(本文なし)
`software/editor/idea.md` — IntelliJ IDEA の使い方、プラグイン、アップグレード
`software/editor/vim/index.md` — Vim のインストール、パッケージ管理、プラグインマネージャー、仕様
`software/editor/vim/edit.md` — Vim 起動後のファイル編集操作。全行の削除、インデント、検索、改行の置換
`software/editor/vim/vimrc.md` — vimrc。読み込まれるファイル、colorscheme、filetype、キーマッピング
`software/editor/vim/plugin.md` — Vim プラグイン。ctrlp.vim、NERDTree、yankround.vim など
`software/editor/vscode.md` — Visual Studio Code の機能、設定、ショートカットキー、拡張機能
`software/job-man/index.md` — ジョブ管理システムの分類。ビルドシステム、ワークフローエンジン など
`software/job-man/cron.md` — cron の仕様、ツール、Pitfalls
`software/job-man/make.md` — GNU make の Makefile 構文、make コマンド、Cookbooks
`software/job-man/jenkins/index.md` — Jenkins の Pipeline と Plugins
`software/job-man/jenkins/jx.md` — Jenkins X(Git・Docker・Kubernetes 前提で、環境構築や CI/CD を簡単にする)の概要
`software/job-man/spinnaker/index.md` — Spinnaker のコンセプト、コンポーネント、仕様、使い方、GCP(GKE)
`software/job-man/spinnaker/halyard/index.md` — Halyard のインストールと使い方
`software/job-man/spinnaker/halyard/hal.md` — hal コマンド。backup、config、deploy
`software/job-man/spinnaker/pipeline.md` — Spinnaker のパイプライン設定
`software/terminal/index.md` — ターミナルソフトウェア。macOS、使い方、トピック
`software/terminal/iterm2.md` — iTerm2 のショートカットキー、設定、使い方、機能
`software/terminal/tmux.md` — tmux の設定と CLI
`software/test/index.md` — ソフトウェアテスト。負荷テストツール(ab、JMeter、Gatling)
`software/test/locust.md` — Locust(負荷テストツール)の locust コマンド、設定、機能
`software/pkg-man/index.md` — パッケージマネージャーの入口(本文なし)
`software/pkg-man/anyenv.md` — anyenv で管理できるものと、使い方
`software/pkg-man/dpkg.md` — dpkg(Debian 系 Linux のパッケージマネージャー)のコマンド
`software/pkg-man/brew.md` — Homebrew の macOS・Linux での使い方、brew コマンド、Tap
`software/pkg-man/snap.md` — Snap の snap コマンド、Snapcraft、トピック
`software/static-site-generator/index.md` — 静的サイトジェネレーターの入口。Sphinx、Jekyll など
`software/static-site-generator/gitbook.md` — GitBook のドキュメントとプラグイン
`software/static-site-generator/hugo/index.md` — Hugo の設定、コンテンツ管理、Shortcodes、既知の問題
`software/static-site-generator/hugo/theme/index.md` — Hugo のテーマ。テーマサイト、自作テーマの掲載
`software/static-site-generator/hugo/theme/docsy.md` — Hugo のテーマ Docsy の導入と設定
`software/static-site-generator/hugo/theme/learn.md` — Hugo のテーマ LEARN のコンテンツ管理と拡張記法
`software/static-site-generator/mdbook.md` — mdBook の CLI とクイックスタート
`software/static-site-generator/mkdocs.md` — MkDocs の使い方、テーマ、mkdocs-material
`software/static-site-generator/vitepress.md` — VitePress の設定、サイドバーの自動生成、動作のメモ
`software/static-site-generator/zensical.md` — Zensical の設定、GitHub Pages へのデプロイ、動作のメモ
