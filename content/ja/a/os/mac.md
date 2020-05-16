---
title: "macOS"
linkTitle: "macOS"
description: https://www.apple.com/macos/what-is/
date: 2020-05-16T16:17:52+09:00
---

旧称 Mac OS X.  
Apple社のPCに搭載されているOS.  
BSD系のUnixを元に作られているらしい。

## ショートカットキー（Touch Bar登場前）

凡例

| 略記 | 意味 |
|:------:|:-------|
| {電源} | 電源キーまたはメディア取り出しキー |

| Key | 機能 |
|:-----:|:-------|
| Ctrl + Shift + {電源} | ディスプレイをスリープにする。画面ロック |
| Ctrl + {電源} | 「再起動・スリープ・システム終了」ダイアログを表示 |

参考:
- [Mac のキーボードショートカット - Apple サポート](https://support.apple.com/ja-jp/HT201236 "Mac のキーボードショートカット - Apple サポート")
- [Macの起動・スリープ・再起動・終了のキーボードショートカットまとめ（27種類） / Inforati](http://inforati.jp/apple/mac-tips-techniques/system-hints/how-to-start-up-reboot-shutdown-sleep-logout-with-mac-keyboard-shortcut.html "Macの起動・スリープ・再起動・終了のキーボードショートカットまとめ（27種類） / Inforati")

## ごみ箱

`~/.Trash` にある。

## How-to
### JIS キーボードでの `\` の入力方法

`option + ¥` で `\` が入力できる。  
後述の方法も参照。

参考:

- [Macにおけるバックスラッシュ（\）の入力方法 - Qiita](http://qiita.com/miyohide/items/6cb8967282d4b2db0f61 "Macにおけるバックスラッシュ（\）の入力方法 - Qiita")

#### IMEの設定で「¥」キーで入力する文字を変える

Google日本語入力の場合、「環境設定 > 一般 > ¥キーで入力する文字」で「バックスラッシュ（\）」を選べば良い。

### 画面を動画で撮影してGIFアニメに変換

動画のキャプチャについて:

- OS VersionがMojave以上 -> macOSの機能でできる
- OS VersionがMojave未満 -> QuickTime Playerで撮影

動画 -> GIF変換ツール:

- [Gifted](https://apps.apple.com/jp/app/gifted/id771955779?mt=12)
- [PicGIF Lite](https://apps.apple.com/jp/app/picgif-lite/id844918735?mt=12)

キャプチャして直接GIFに保存できるもの:

- [LICEcap](https://apps.apple.com/jp/app/picgif-lite/id844918735?mt=12)

参考:

- [【小ネタ】Macの画面を録画して、GIFアニメにする方法 | Developers.IO](https://dev.classmethod.jp/articles/mac-screen-gif-anime/)
- [【Mac】自分の画面を録画して、即gif動画化する方法 - Qiita](https://qiita.com/YosukeItabashi/items/5722395218e6e592fd39)
- [Macでキー入力表示しつつターミナル操作をアニメーションGIFにする - くりにっき](https://sue445.hatenablog.com/entry/2014/08/13/121512)

#### ターミナルアプリの場合

ttyrecというツールがある。

Tips:

- [KeyCastr](https://download.cnet.com/KeyCastr/3000-2075_4-125977.html)というソフトを使うと、キー入力を動画に入れることができる。

参考:

- [ttygifでターミナルを録画してgifにする - Qiita](https://qiita.com/okamos/items/33f46de83485d744fd4b)