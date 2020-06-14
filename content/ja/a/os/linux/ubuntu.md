---
title: "Ubuntu"
linkTitle: "Ubuntu"
description: https://ubuntu.com/
date: 2020-06-15T00:43:34+09:00
---

## About

- 日本語サイト https://www.ubuntulinux.jp/

## パッケージ

- [Ubuntu – Ubuntu パッケージ検索](https://packages.ubuntu.com/ja/)

参考:

- [Software > パッケージ管理 > Snap]({{<ref "/a/software/pkg-man/snap.md">}})

## Firewall

Ubuntu 18.04だとufwが標準で入っている。

SYNOPSIS:

```Bash
## 状態表示
sudo ufw status

## 有効化
sudo ufw enable
```

参考:

- [Ubuntu 18.04でUbuntuファイアウォール（UFW）を設定する | tottio](https://server.tottio.net/archives/296)


## セキュリティ
### AppArmor

いつからかUbuntuに標準で組み込まれたSELinux的なやつ。

SYNOPSIS:

```Bash
## 現在の状態を表示
aa-enabled
apparmor_status

## 起動
/etc/init.d/apparmor start

## 停止
/etc/init.d/apparmor stop
/etc/init.d/apparmor teardown
```

参考:
- [AppArmor - ArchWiki](https://wiki.archlinux.jp/index.php/AppArmor)
- [\[手順\] AppArmor を無効化するには – ヘルプセンター](https://support.plesk.com/hc/ja/articles/213909965--%E6%89%8B%E9%A0%86-AppArmor-%E3%82%92%E7%84%A1%E5%8A%B9%E5%8C%96%E3%81%99%E3%82%8B%E3%81%AB%E3%81%AF)

## How-to
### ファイラで隠しファイルを表示

`Ctrl-H` を押す。
これノーヒントだとわからんがな。。ヘルプでも見つからないし。。

参考:

- [Ubuntu/ファイルマネージャで隠しファイル・隠しフォルダを表示する方法 - Linuxと過ごす](https://linux.just4fun.biz/?Ubuntu/%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%83%9E%E3%83%8D%E3%83%BC%E3%82%B8%E3%83%A3%E3%81%A7%E9%9A%A0%E3%81%97%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%83%BB%E9%9A%A0%E3%81%97%E3%83%95%E3%82%A9%E3%83%AB%E3%83%80%E3%82%92%E8%A1%A8%E7%A4%BA%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95)

### 画面キャプチャのショートカットキー

- `PrintScreen` ... 全画面キャプチャ
- `Shift + PrintScreen` ... 範囲指定キャプチャ
- `Alt + PrintScreen` ... ウィンドウ指定キャプチャ

参考:
- [Ubuntuで端末からスクリーンショットを撮る方法まとめ - Qiita](http://qiita.com/yas-nyan/items/80f2db8c4bdf4c8e87b8)
  - コマンドラインで実行する方法も載ってる。

## 歴史
### デスクトップ
#### Unity

※Ubuntu 17からUnityが廃止されてGNOMEになった。

- https://ja.wikipedia.org/wiki/Unity_(ユーザインタフェース)

Tips:
- [UbuntuTips/Desktop/KeyboardShortcutOnUnity - Ubuntu Japanese Wiki](https://wiki.ubuntulinux.jp/UbuntuTips/Desktop/KeyboardShortcutOnUnity)
  - Unity のショートカット一覧

