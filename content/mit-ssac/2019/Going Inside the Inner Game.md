---
title: "Going Inside the Inner Game: Predicting the Emotions of Professional Tennis Players from Match Broadcasts"
info:
  title: "Going Inside the Inner Game: Predicting the Emotions of Professional Tennis Players from Match Broadcasts"
  authors: "Stephanie Kovalchik and Machar Reid"
  labs: "Game Insight  Group, Tennis Australia"
  conference: "MIT Sloan Sports Analytics Conference"
  sport: "Tennis"
  sport_icon: "tennis"
  url: "http://www.sloansportsconference.com/wp-content/uploads/2018/02/2005.pdf"
authors:
- Saeru Yamamuro
date: 2019-01-01T00:00:00+09:00
description: "Summary"
type: technical_note
draft: false
---

## 要旨 Abstract

<!-- *論文のアブストラクトを日本語で軽く* -->

テニスというスポーツは、
試合時間の80%が準備時間であると言われており、
"テニスはメンタルの試合だ"とよく言われる。

また、他のポピュラーなスポーツでも
"メンタル"をトレーニングの対象とすることも
増えている中、本論文では
全豪オープンの試合映像から選手の感情を
推定するフレームワークを提案する。

具体的には、
試合映像から選手の表情を検出し、
その各種画像特徴を
いくつかの機械学習アルゴリズムで学習することで
選手の感情を予測する。

## リサーチ課題

テニスというスポーツが持つ
"メンタル"という重要な側面を
試合映像のみから定量化する。
## リサーチ課題に対する結論
テニス全豪オープンの試合映像から
選手の感情を予測し、かつ
その定量的な指標と試合結果の
関係性が考察された。

## 手法

**まずは一言で**

試合映像からOpenFaceによってトリミングされた選手の表情から各種画像特徴を抽出し、
機械学習のさまざまなな手法で学習を行うことで、
選手の感情を推定する。

**手法の具体的な説明**

提案手法のフレームワークは以下のようになっており、
「特徴抽出」部と「感情予測」部に分けられる。

![framework](https://user-images.githubusercontent.com/22371492/58749792-43a7b980-84c5-11e9-9561-a04a18013914.jpg)

- **特徴抽出**:

OpenFaceが算出する表情に関する17の特徴（FAU）と、
その主要な特徴から予測される基本的な感情（FACS）を抽出する。

- **感情予測**:

特徴抽出部で抽出された2つの特徴を入力として
機械学習の様々な手法（SVM、判別分析、Neural Network、
Boosting、Bagging、正則化付き回帰モデル）で学習を行い、
分類精度が最良な手法を用いて予測を行う。

**従来のアプローチとはどのように異なるか**

## 結果

70%を訓練、残りの30%をテストデータとして学習と評価を行なったところ、
全体的にはSVMの予測精度が高いという結果になった。
また、全豪オープンのビッグ4のデータに対して予測された、
感情の割合を下に示す。

各選手で感情の割合が異なり、
例えばナダルはよく"anxiety（心配）"だったことや、
フェデラーは逆に"focus（集中）"や"neutral（自然）"
であったことを表情から予測されている。

![result](https://user-images.githubusercontent.com/22371492/58749797-47d3d700-84c5-11e9-8955-55938dba5630.jpg)

## コメント

<!-- *問題点や議論できることがあれば* -->

選手の「感情」は他のスポーツでも
共通している側面であるため、応用可能であるが
同時にその使い方にはまだ課題を残す。

具体的には選手のメンタルは
非常にセンシティブな要素であるために、
解析結果のフィードバックは慎重に、そして
専門家が行う必要があるように思う。

## その他

**リサーチクエスチョンに関する論文**

**手法に関する論文**
