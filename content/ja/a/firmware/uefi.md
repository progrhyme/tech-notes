---
title: "UEFI"
linkTitle: "UEFI"
description: >
  Unified Extensible Firmware Interface.
  https://uefi.org/
date: 2020-05-04T08:45:22+09:00
weight: 800
---

## About

[UEFI（EFI）とは - IT用語辞典 e-Words](http://e-words.jp/w/UEFI.html)より:

> コンピュータ内の各装置を制御するファームウェアとオペレーティングシステム（OS）の間の通信仕様を定めた標準規格の一つ。従来のBIOSに代わるもの。UEFI対応ファームウェアを指してUEFIと呼ぶこともある。

- 業界団体: UEFIフォーラム https://uefi.org/

参考:

- [Unified Extensible Firmware Interface - Wikipedia](https://ja.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface)

## 仕様

https://uefi.org/specifications

2020-05-04時点の最新版: [UEFI Specification Version 2.8 (Errata A) (released February 2020)](https://uefi.org/sites/default/files/resources/UEFI_Spec_2_8_A_Feb14.pdf)

### セキュアブート

[Shielded VM | ドキュメント | Google Cloud](https://cloud.google.com/security/shielded-cloud/shielded-vm?hl=ja)より:

> すべてのブートコンポーネントのデジタル署名を検証し、署名検証が失敗した場合にブートプロセスを停止することで、システムが正規のソフトウェアのみを実行することを保証します。

参考:

- [セキュア ブート | Microsoft Docs](https://docs.microsoft.com/ja-jp/windows-hardware/design/device-experiences/oem-secure-boot)

## 歴史

[UEFI（EFI）とは - IT用語辞典 e-Words](http://e-words.jp/w/UEFI.html)より:

> 従来使われてきたBIOSは、16ビットマイクロプロセッサの時代に設計されたもので、マルチタスク環境で利用されることを想定していない点や、メインメモリの位置640KB〜1MBわずか384KBの領域にしか配置できない点など、現在のハードウェアやOSから見ると時代遅れで窮屈な制約が多い。

> これを克服するため、64ビット環境を想定して新たに設計された近代的で拡張可能なファームウェアのインターフェース仕様としてUEFIの開発が始まった。

MEMO:

- 開発当初は「EFI」（Extensible Firmware Interface）という名称だった。
- 2005年、業界団体のUEFIフォーラムへ移管され、同時に名称もUEFI（Unified EFI）に改められた。

