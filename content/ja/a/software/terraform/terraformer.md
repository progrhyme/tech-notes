---
title: "terraformer"
linkTitle: "terraformer"
description: https://github.com/GoogleCloudPlatform/terraformer
date: 2020-05-08T10:26:09+09:00
weight: 2800
---

既存のクラウドインフラなどからTerraformの設定ファイルを生成してくれるもの。

GCPが出してるけど、AWS, Azureなど他のクラウドのほかKubernetes, Datadog, GitHubなどTerraformの多くのプロバイダに対応している。

## Install

Homebrew:

```sh
brew install terraformer
```

※Terraformプロバイダをプラグインとして `~/.terraform.d/plugins/{darwin,linux}_amd64/` に配置する必要がある。

## Usage

Examples:

```sh
terraformer import google --projects=prj1,prj2 \
  --regions=asia-northeast1,asia-northeast2 \
  --resources=networks,subnetworks,gcs
```

`./generated/` 以下にリソースの定義ファイルとtfstateファイルが生成される。
