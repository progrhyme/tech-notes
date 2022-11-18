---
title: "PowerShell"
linkTitle: "PowerShell"
date: 2022-11-18T10:22:58+09:00
weight: 800
---

## About

[PowerShell とは - PowerShell | Microsoft Learn](https://learn.microsoft.com/ja-jp/powershell/scripting/overview) より

> PowerShell は、コマンドライン シェル、スクリプト言語、および構成管理フレームワークで構成されるクロスプラットフォームのタスク自動化ソリューションです。 PowerShell は Windows、Linux、および macOS 上で実行されます。

## Documentation

https://learn.microsoft.com/ja-jp/powershell/

## How-to
### CSV, TSVの読み込み

```PowerShell
$csv = Import-Csv .¥test.csv
# TSV読み込み
$csv = Import-Csv .¥test.tsv -Delimiter "`t"
# Shift-JISのコンテンツを読み込み
$csv = Import-Csv .¥test.csv -Encoding Default
```

参考:
- [PowerShellでタブ区切りのcsvファイルを読み込む - Qiita](https://qiita.com/sukakako/items/4a17db13730934766abb)
- [【Windows】Powershell の import-csv コマンドレットで文字化けする場合の対処](https://www.tensorflowz.com/WindowsUpdate/doc/Windows/import-csv-mojibake.html)

### CSVデータのソート

`Sort-Object (sort)` を使う。

```PowerShell
$csv = Import-Csv .¥test.csv

# 昇順ソート
$csv | Sort-Object -Property Name
# 複数プロパティで降順ソート
$csv | Sort-Object -Property Name,Role -Descending
# IDを数値としてソート
$csv | sort @{Expression={[int]$_.ID}}
```

Tips:
- `Sort-Object` => `sort` と記述可
- `-Property` 省略可
- `-Descending` => `-desc` と記述可

参考:
- [PowerShellでcsvファイルの値を昇順、降順に並べて出力する | 新米Plog](https://plog.shinmaiblog.com/powershell-csv-sort/)
- [PowerShell の Sort-Object Tips](http://www.vwnet.jp/windows/PowerShell/2017032901/Sort-Object_Tips.htm)
