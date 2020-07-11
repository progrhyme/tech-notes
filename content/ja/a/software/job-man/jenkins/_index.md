---
title: "Jenkins"
linkTitle: "Jenkins"
description: https://jenkins.io/
date: 2020-05-28T11:12:22+09:00
weight: 290
---

CI/CDなどの自動化ツール。  
何でもできる英国紳士。

## Documentation

https://jenkins.io/doc/

- Pipeline機能: https://jenkins.io/doc/book/pipeline/
  - Syntax: https://jenkins.io/doc/book/pipeline/syntax/

## Pipeline

- Declarative Pipeline ... 比較的新しい。 `pipeline { ... }` で定義する。
- Scripted Pipeline ... やや古い。 `node { ... }` で定義する。

参考:

- [Jenkinsのpipelineのスクリプトの書き方まとめ \- ぴよぴよ\.py](http://cocodrips.hateblo.jp/entry/2017/10/23/205801)

### Steps Reference

https://jenkins.io/doc/pipeline/steps/

- [Pipeline: Nodes and Processes](https://jenkins.io/doc/pipeline/steps/workflow-durable-task-step/)
  - `sh` 等

#### Basic Steps

https://jenkins.io/doc/pipeline/steps/workflow-basic-steps/

##### `withEnv`

環境変数をセットしたブロックを作る。

```groovy
node {
  withEnv(['MYTOOL_HOME=/usr/local/mytool']) {
    sh '$MYTOOL_HOME/bin/start'
  }
}
```

`withEnv(['PATH+WHATEVER=/something'])` のようにすることで、 `/something` を `$PATH` エントリの前に加えることができる。

参考:

- [path \- Export command in Jenkins pipeline \- Stack Overflow](https://stackoverflow.com/questions/44378221/export-command-in-jenkins-pipeline/44380495#44380495)


## Plugins
### CloudBees Folders

- [User Guide](https://go.cloudbees.com/docs/cloudbees-documentation/cje-user-guide/index.html#folder)
- https://plugins.jenkins.io/cloudbees-folder
- https://wiki.jenkins.io/display/JENKINS/CloudBees+Folders+Plugin

ジョブをフォルダという単位に整理することができる。  
UI上はタブで表示される。

#### 使い方

- ジョブの編集(フォルダへの追加・削除)
  1. タブをクリックすると `/view/xxx` というパスに遷移する。
  1. 左列メニューの「ビューの変更」(英語だと「Edit View」)をクリック
  1. ジョブをチェックボックスで選択し、「保存」

参考:

- [Jenkinsで既存のジョブを別のビューに移動するにはどうすればいいですか？ | CODE Q&amp;A \[日本語\]](https://code.i-harness.com/ja/q/1b3d4ea "Jenkinsで既存のジョブを別のビューに移動するにはどうすればいいですか？ | CODE Q&amp;A [日本語]")
