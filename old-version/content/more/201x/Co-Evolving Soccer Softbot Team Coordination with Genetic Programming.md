---
title: "Co-Evolving Soccer Softbot Team Coordination with Genetic Programming"
photo: "![image](https://user-images.githubusercontent.com/22371492/56633572-a1144380-6699-11e9-9f04-59da2ea62b21.png)"
info:
  title: "Co-Evolving Soccer Softbot Team Coordination with Genetic Programming"
  authors: "Sean Luke, Charles Hohn, et al."
  labs: "Department of Computer Science University of Maryland"
  conference: "IJCAI-97"
  sport: "Football"
  sport_icon: "futbol"
  url: "https://cs.gmu.edu/~sean/papers/robocupc.pdf"
authors:
- Atom Scott
date: 2019-04-24T00:00:00+09:00
description: "Summary"
type: technical_note
draft: false
---

## 要旨 Abstract
*論文のアブストラクトを日本語で軽く*

この論文ではロボカップサッカーにおける，遺伝的プログラミングを用いたチーム戦術の獲得方法について記されている．
最終的には遺伝的プログラミングにより，共同プレーを学習させることができた．

## リサーチ課題
進化計算によってサッカーエージェントは簡単な共同プレーをできるようになるのか．

## リサーチ課題に対する結論
サッカーエージェントはピッチ上で分散して，パス・ドリブル・ゴールを守るなど様々なプレーを獲得する様子が見られた．

## 手法
**まずは一言で**
遺伝的プログラミング（GP）

**手法の具体的な説明**
遺伝的プログラミングとは遺伝的アルゴリズムの種類の1つであり，進化を用いてプログラムやアルゴリズムを最適化させてあるタスクを達成させることを目標にしている．

以下のような手順を追いながら，ある方法で評価をしたあとに，決められた割合で選択・変異・交配によって次の世代のエージェントをつくるということを繰り返します．
![image](https://user-images.githubusercontent.com/22371492/56640438-0114e500-66ae-11e9-99a0-dd4f030d9fd7.png)

例えば，交配や変異によって，部分木はこのように変わっていきます．
![image](https://user-images.githubusercontent.com/22371492/56642354-36233680-66b2-11e9-9879-07830126f226.png)

![image](https://user-images.githubusercontent.com/22371492/56642243-f2303180-66b1-11e9-8e73-021defeee81a.png)


**従来のアプローチとはどのように異なるか**
ロボカップサッカーサーバーのモデルのダイナミック性を考慮して，相手の行動に応じて動くルールベースの手法が取られることが多い（当時は特に）．

しかし，行動の種類が多いサッカーのような競技ではすべての行動・ルールを手でコーディングすることは不可能であるため，それらを学習する遺伝的プログラミングのようなアプローチは魅力的である．

また，本文ではニューラルネットワークに関して

> Most learning Strategies (neural networks, decision trees, etc.) are designed not to develop algorithmic behaviours but to learn a nonlinear function over a discrete set of variables.  These strategies are effective for learning low-level soccer -player functions such as ball interception, etc., but may not be as well suited for learning emergent, high-level player coordination.

と述べており，
ニューラルネットワークのような学習戦略は離散的な変数の集合をカバーする非線形関数を作ることを目標にしているため，サッカーにおける高いレベルでの協調を学習することに適していないとしている．

反対に，GPはシンボリック関数やアルゴリズムを学習することに適しているため，ロボカップサッカーのようなドメインで使用するのは自然な選択だとしている．

本研究ではGPの中でも，Strongly Typed GPを利用している．
Strongly Typed GPは自分たちで関数を最初に書くことで，探索する空間を制限しつつ，最適解を求めれる手法だ．

![image](https://user-images.githubusercontent.com/22371492/56642796-3839c500-66b3-11e9-80e0-f750338809c3.png)

筆者たちは多くの工夫をこらしながら，エージェントをうまく学習させていたので大きな壁となった「評価項目の設定」と「イテレーション速度」とその改善方法について説明したい．
より具体的な説明やほかの工夫については原論文を参考にしてほしい．

「評価項目の設定」
少し複雑な評価目に設定したところ，エージェントはボールに近づいて相手ゴール方向に向かってボールを蹴るお団子サッカー戦略を部分最適解としてしまった．

![image](https://user-images.githubusercontent.com/22371492/56643826-63251880-66b5-11e9-9092-2a249a37a585.png)

そこで評価項目をよりシンプルにゴール（得失点両方か片方かはわからない）にのみ絞ったところでこの部分最適解から抜け出すことができたようだ．

「イテレーション数」
ロボカップサッカーはシミュレーションリーグであっても，リアルタイムにすべての試合がおこなれる．
筆者らによる以前の研究では，より簡単なドメインで良い戦略を得るために少なとも100,000回の世代が必要だったいう．
ロボカップサッカーで同じ回数の試合を行うと数年かかる可能性があったため，短い時間でイテレーションの回数を増やす工夫が複数使われた．

- 共進化
- 異なるゲノムを持ったエージェントで並列計算
- 32試合の並列計算

などの工夫をしたが，サッカーっぽい戦術の獲得にはそれでも数か月の時間を使ったということだった．

## 結果
プレーヤーはフィールド上で分散し、適切なチームメイトにパスしてゴールにまっすぐ進めるようになった．
ロボカップに間に合わなかったため，まだ進化が続いてる様子も見られたのにもかかわらずプロジェクトは打ち切られたが，筆者らは時間がもっとあればさらに良い戦略を生み出せたのではないかとしている．
![image](https://user-images.githubusercontent.com/22371492/56645095-f95a3e00-66b7-11e9-9c33-7172ac181913.png)

## コメント
*問題点や議論できることがあれば*

古い論文なので，このあとどうなったのか知りたい！

## その他
**リサーチクエスチョンに関する論文**
Model-Based Reinforcement Learning For Evolving Soccer Strategies
Learning Team Strategies: Soccer Case Studies
Evolving Neural Network Controllers for a Team of Self-Organizing Robots
[Real-Time Training of Team Soccer Behaviors](https://cs.gmu.edu/~sean/papers/robocup12training.pdf)

**手法に関する論文**

[Strongly Typed Genetic Programming](http://davidmontana.net/papers/stgp.pdf)