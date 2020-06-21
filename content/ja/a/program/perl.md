---
title: "Perl"
linkTitle: "Perl"
description: https://www.perl.org/
date: 2020-05-08T22:34:00+09:00
weight: 700
---

## Documentation

https://perldoc.perl.org/

- 邦訳: https://perldoc.jp/

### PODの書き方

- https://perldoc.perl.org/5.30.0/perlpod.html
- 邦訳: https://perldoc.jp/docs/perl/5.26.1/perlpod.pod

## CPANモジュール

- https://metacpan.org/

### App::cpanminus

https://metacpan.org/pod/App::cpanminus

`cpanm` のためにまずこれを入れる。

ユーザ環境のperl（plenvなど）にインストールするには、下のコマンドでよい:

```sh
curl -L https://cpanmin.us | perl - App::cpanminus
```

使い方:

```sh
# モジュールインストール
cpanm Foo::Bar
```

### Pod::Markdown

https://metacpan.org/release/Pod-Markdown

pod2markdown コマンドを提供してくれる。

```sh
pod2markdown Foo.pm > Foo.md
```

## Topics
### CPANモジュールのメンテに関する備忘録

- [comaint(1)でCPAN moduleのcomaintainerを追加する - Islands in the byte stream](http://d.hatena.ne.jp/gfx/20140823/1408750107)
- [Minilla を使って CPAN にモジュールを上げてみた - weblog of key_amb](http://keyamb.hatenablog.com/entry/2014/03/15/204118)
- [久しぶりにCPANリリース / 20170509 - progrhyme's Tech Wiki](https://sites.google.com/site/progrhymetechwiki/home/memo/2017/20170509#TOC-CPAN-)

## History

参考:

- [Perl - Wikipedia](https://ja.wikipedia.org/wiki/Perl)
- http://history.perl.org/PerlTimeline.html
