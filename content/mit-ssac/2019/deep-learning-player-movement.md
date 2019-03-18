---
title: "Using Deep Learning to Understand Patterns of Player Movement in the NBA"
info:
  title: "Using	Deep	Learning	to	Understand	Patterns	of	Player Movement	in	the	NBA"
  authors: "Akhil	Nistala,	John	Guttag"
  labs: ""
  conference: "MIT SSAC 2018"
  sport: "Basketball"
  sport_icon: "basketball-ball"
  url: "http://www.sloansportsconference.com/wp-content/uploads/2019/02/Using-Deep-Learning-to-Understand-Patterns-of-Player-Movement-in-the-NBA.pdf"
authors:
- Atom Scott
date: 2019-03-18T00:00:00+09:00
description: "Summary"
type: technical_note
draft: false
---

## 要旨 Abstract
*論文のアブストラクトを日本語で軽く*
Trajectory embedding と呼ばれる、オフェンス時の選手の動きを32次元ベクトルで表現し、それらのユークリッドを距離を使うことがプレー類似度を示すために有効である。
この発見により、Similar	Possessions Finder（類似ポゼッション検索器）を開発することができた。
Similar	Possessions Finderによって、
- 	"How much	more	 frequently	did	Andre Drummond	establish	position on the right block than on the	left block during	the	2015-2016 regular season?"
などの検索に素早く答えを見るけることができるようになった。

## リサーチ課題
どうすれば、オフェンス時の自動でプレーを比較して、分析するフレームワークが作れるか。

## リサーチ課題に対する結論
トラッキングデータ使ったデータベースの作成

→NLP的な要素はなかったので、上記の"How much	more	 frequently	did	Andre Drummond	establish	position on the right block than on the	left block during	the	2015-2016 regular season?"の質問はなんらかの形に変えて、検索しているだろうと考えている。

## 手法
**まずは一言で**

自動で類似プレーを検索する方法
1. 選手のトラッキングデータを画像に変換
2. Autoencoderにより次元圧縮した画像を生成
!()[fig3.png]
3. 次元圧縮した画像のユークリッド距離を用いて、近傍する画像を検索する

選手のプレースタイルを分析する方法
1. 次元圧縮した画像をクラスタリングする
2. クラスタの中心となる画像を見て、クラスタを特徴づける
!()[fig6.png]
3. クラスタ内にある画像の比率を比較して、プレースタイルを分析する
!()[fig11.png]
!()[fig10.png]


## 結果
画像検索の精度は著者による10段階評価のようであるので、定量的な評価ができていない。
!()[fig4.png]

## コメント
*問題点や議論できることがあれば*
{{< youtube DNWWi8RYzhM> }}
軌道画像をそのまま使うのは計算リソース的に厳しかったために、Autoencoderによる次元圧縮を行ったそうなのだが、トラッキングデータを画像にする必要はあるのか。
（検証したい気持ちがある）

クラスタリング方法がk=20が良いとしているのにもかかわらず、下記のようにクラスタをまとめて言語化しているので、もっと最適クラスタリング方法があるはず。

## その他
**リサーチクエスチョンに関する論文**
(Chalkboarding: A New Spatiotemporal Query Paradigm for Sports Play Retrieval)[https://atomscott.github.io/Sports-Lab/other/201x/chalkboarding/]
**手法に関する論文**
