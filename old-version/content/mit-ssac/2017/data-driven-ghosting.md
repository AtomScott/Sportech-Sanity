---
title: "Data-Driven Ghosting using Deep Imitation Learning"
photo: fig1.png
info:
  title: "Data-Driven	Ghosting	using	Deep	Imitation	Learning"
  authors: "Hoang	M.	Le,	Peter	Carr,	Yisong	Yue,	and	Patrick	Lucey"
  labs: "California	Institute	of	Technology,	Disney	Research,	and	STATS	LLC"
  conference: "MIT Sloan Sports Analytics Conference"
  sport: "Soccer"
  sport_icon: "futbol"
  url: "http://www.sloansportsconference.com/wp-content/uploads/2017/02/1671-2.pdf"
authors:
- Atom Scott
date: 2019-02-20T11:53:49-07:00
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

{{< youtube WI-WL2cj0CA >}}

## リサーチ課題

きめ細かく守備をスケーラブルに定量化し，分析するにはどうすればよいか？

ある選手・チームはある試合状況において、どのように動くべきなのか？

## リサーチ課題に対する結論
データ駆動ゴーストを使用して，選手が取った守備と理想的な守備との差を求める。

## 手法
**まずは一言で**

深層模倣学習とゴースティング

**手法の具体的な説明**

- 深層模倣学習

役割別で単一選手のモデルを学習してから、全役割で複数選手のモデルを学習する。
モデルはLSTMを使う。

![](fig9.png)
![](fig10.png)

## 結果
ゴーストの動きがゴール確率を低下させる特定の状況を示すことができた。
また、リーグ全体のデータを学習したゴーストと、特定のチームのデータのみで学習したゴーストを比較することで異なる動きをするゴーストができるので比較が可能になった。
![](fig1.png)

## コメント
*問題点や議論できることがあれば*
{{< youtube 130r0XQIKq0 >}}
## その他
**リサーチクエスチョンに関する論文**

**手法に関する論文**
