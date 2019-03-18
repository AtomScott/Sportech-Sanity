---
title: "Decomposing	the	Immeasurable Sport:
A deep learning	expected possession	value framework
for soccer"
photo: "eq1.jpeg"
info:
  title: "Decomposing the Immeasurable Sport:
	A deep learning	expected possession	value framework
	for soccer"
  authors: "Javier Fernández, Luke Bornn, Dan Cervone"
  labs: "F.C. Barcelona, Simon Fraser University, Los Angeles Dodgers"
  conference: "MIT Sloan Sports Analytics Conference"
  sport: "Soccer"
  sport_icon: "futbol"
  url: "http://www.sloansportsconference.com/wp-content/uploads/2019/02/Decomposing-the-Immeasurable-Sport.pdf"
authors:
- Saeru Yamamuro
date: 2019-01-01T00:00:00+09:00
description: "Summary"
type: technical_note
draft: false
---

## 要旨 Abstract
<!-- *論文のアブストラクトを日本語で軽く* -->
サッカーというスポーツが持つ複雑な側面の詳細な、
そして柔軟な解釈を提供するために、
コーチが興味を持つ幅広いイベントを要約する
分析手法が求められている。
そこで、本論文では深層学習を用いたポゼッションの期待値
（EPV : Expected Possession Value）推定
フレームワークを提案する。

このフレームワークを活用することで、
試合中の文脈におけるパスやドリブルといった
イベントの貢献を推定するだけでなく、
その他の選択肢の提案など
様々な分析を行うことができる。

## リサーチ課題
サッカーというスポーツが持つ
各イベントや各選手間の相互作用生を
柔軟に表現すること

## リサーチ課題に対する結論
深層学習で高次元なトラッキングデータを特徴圧縮し、
パス、ドリブル、ゴールの期待値を組み合わせることで、
解釈可能な推定値を算出することができた

## 手法
**まずは一言で**

畳み込みニューラルネットワーク（CNN : Convolutional Neural Network）
を用いたトラッキングデータの特徴抽出と、パス・ゴール・ドリブルの各イベントの
期待値を統合したポゼッションの期待値（EPV）推定モデル

**手法の具体的な説明**

ポゼッションの期待値（EPV : Expected Possession Value）は
目的地に応じたパスとドリブルの期待値モデルとゴール期待値モデルを統合した
以下の式で定義される。
![](eq1.jpeg)

- **パスとドリブルの期待値モデル**:  
著者が[SSAC2018で発表した論文](http://www.lukebornn.com/papers/fernandez_ssac_2018.pdf)で提案している統計モデルをCNNで拡張した確率モデルを採用

- **ゴール期待値モデル**:  
すでに研究されているxGモデルで算出されるゴール期待値を採用

**従来のアプローチとはどのように異なるか**

パス・ゴール・ドリブルの各イベントを独立したモデルで定義し、
またそれらを組み合わせている点

## 結果
データから解釈可能な情報を導き出すことで
以下のような分析や可視化を可能とした

- ポゼッションの期待値を加味した動的なパスマップ
- 試合の文脈に応じたパスの分析
- ポジションごとのオフザボールの動きの需要とマップ化
- 意思決定の時系列的な分析

## コメント
<!-- *問題点や議論できることがあれば* -->

考察が非常にリッチなので、手法の説明だけでなく
実験結果の章を読み込むことにも価値がある。

## その他
**リサーチクエスチョンに関する論文**

**手法に関する論文**

- [『A Multiresolution Stochastic Process Model for Predicting Basketball Possession Outcomes』](https://arxiv.org/pdf/1408.0777.pdf)
- [『Wide Open Spaces: A statistical technique for measuring
space creation in professional soccer』](http://www.lukebornn.com/papers/fernandez_ssac_2018.pdf)
