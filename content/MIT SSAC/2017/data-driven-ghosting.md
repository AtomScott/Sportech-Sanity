---
title: "Data-Driven Ghosting using Deep Imitation Learning"
info:
  title: "Data-Driven	Ghosting	using	Deep	Imitation	Learning"
  authors: "Hoang	M.	Le,	Peter	Carr,	Yisong	Yue,	and	Patrick	Lucey"
  labs: "California	Institute	of	Technology,	Disney	Research,	and	STATS	LLC"
  conference: "MIT Sloan Sports Analytics Conference"
  url: "http://www.sloansportsconference.com/wp-content/uploads/2017/02/1671-2.pdf"
authors:
- Atom Scott
date: 2017-02-20T11:53:49-07:00
description: "Summary"
type: technical_note
draft: false
---

## 要旨 Abstract
*論文のアブストラクトを日本語で軽く*

ゴール期待値などといった現在のSoTAである測定値は、パフォーマンス分析において頻繁に使われるようになった。しかし、シュートという離散的なイベントに紐付けられているため、本質的な制約がある。

選手・ボールのトラッキングデータを用いることで、細かな行動パターンを定量的に分析することができるのではないか。

本研究では、ゴースティングと深層模倣学習を用いてサッカーの1シーズン分のトラッキングデータに適応した、自動データ駆動ゴースティングという手法を提案する。

このゴースティング手法を活用することで、「ある選手・チームはある試合状況において、どのように動くべきなのか」という問いに答えることができる。さらに異なるチームがある状況に対してどうアプローチしたかも予想することができる。

## リサーチ課題

きめ細かく守備をスケーラブルに定量化し，分析するにはどうすればよいか？

ある選手・チームはある試合状況において、どのように動くべきなのか？

## リサーチ課題に対する結論
データ駆動ゴーストを使用して，選手が取った守備と理想的な守備との差を求める。

## 手法
*まずは一言で*

深層模倣学習（アルファゴー）とゴースティング（トロントラプターズ）

**手法の具体的な説明**

**従来のアプローチとはどのように異なるか**

## 検証方法 Methods
ゴーストの動きがゴール確率を低下させる特定の状況を示した。

## コメント Comment
*問題点や議論できることがあれば*

## その他
**リサーチクエスチョンに関する論文**

**手法に関する論文**
