---
title: "macOS"
linkTitle: "macOS"
description: https://www.apple.com/macos/what-is/
date: 2020-05-16T16:17:52+09:00
weight: 410
---

旧称 Mac OS X.  
Apple社のPCに搭載されているOS.  
BSD系のUnixを元に作られているらしい。

関連ページ:

- [Software > パッケージ管理 > Homebrew]({{<ref "/a/software/pkg-man/brew.md">}})

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

## Configuration
### Touch Bar

ボタン配置を変える方法:

- 「システム環境設定 > キーボード > Touch Barをカスタマイズ」
  - 2020-05-18 macOS Mojaveで確認

参考:

- [macOSで画面ロック/スクリーンセーバ起動を 1 操作で実行する 3 通りの方法 | Developers.IO](https://dev.classmethod.jp/articles/macos-screen-lock-by-touch-bar/)

## 機能
### Quick Look（クイックルック）

Tips:

- GIFアニメや動画ファイルをFinderなどで選択し、スペースキーを押すと簡単に再生画面が見られる
- 他のファイルにも対応しており、色々便利っぽい

参考:

- [Quick Look（クイックルック）について押さえておきたい基礎知識｜Mac - 週刊アスキー](https://weekly.ascii.jp/elem/000/002/615/2615764/)
- [MacでGIFアニメを簡単に再生する方法 | iTea4.0](http://itea40.jp/technic/mac-tips-summary/how-to-play-gif-animation-easily-with-mac/)

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

- [KeyCastr](https://github.com/keycastr/keycastr)というソフトを使うと、キー入力を動画に入れることができる。

参考:

- [ttygifでターミナルを録画してgifにする - Qiita](https://qiita.com/okamos/items/33f46de83485d744fd4b)
- 2019-10-28 [Macでのキー入力をディスプレイ上に表示してくれるオープンソースのキーストロークビジュアライザー「KeyCastr」がダークモードに対応し、GPU切り替えの不具合を修正。 | AAPL Ch.](https://applech2.com/archives/20191028-keycastr-for-mac-support-dark-mode-and-fix-gpu-bug.html)

### GNUコマンドを使う

macOSのコマンドは慣れ親しんでいるLinuxのコマンドと微妙なオプション差異があってハマることが度々ある。

下記表のHomebrewパッケージを入れることで、多くのLinuxで使われているGNU版のコマンドが使えるようになる。

※()内がGNU版の対応するコマンド。prefix `g` がつくことが多い

 パッケージ | 使えるコマンド
----------|--------------
 coreutils | realpath, cp, mv, ls, ...
 gnu-sed | gsed (sed)
 gawk | gawk (awk)
 gzip |
 gnu-tar |
 gnu-time |
 gnu-getopt |
 binutils | ar, gar, ...
 diffutils | diff, cmp, ...
 findutils | find, locate, xargs, ...
 moreutils | pee, ...

参考:

- [Homebrewを用いてGNU系コマンドをインストール（macOS） - Qiita](https://qiita.com/kkdd/items/e9c8b46a89dea7862661)
- [macで使いにくいコマンドをLinuxに合わせる - Qiita](https://qiita.com/toyama0919/items/661437d86a95b02484a2)

## Spec

システム仕様、内部仕様などをここに記す。

### ファイルシステム

- APFS (Apple File System) ... Hi Sierra (10.13) 以降
  - タイムスタンプの精度がナノ秒になった
- HFS+ ... APFS以前
  - タイムスタンプの精度が秒単位だった

参考:

- [ファイルシステムがAPFSになった事による変更点 - ナレッジ | フォーカスシステムズ サイバーフォレンジックセンター](https://cyberforensic.focus-s.com/knowledge/articles_detail/356/)
- [macos - How to return millisecond information for File Access on Mac Os X (in Java)? - Stack Overflow](https://stackoverflow.com/questions/18403588/how-to-return-millisecond-information-for-file-access-on-mac-os-x-in-java)
