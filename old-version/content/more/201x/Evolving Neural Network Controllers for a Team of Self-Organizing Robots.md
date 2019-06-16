---
title: "Evolving Neural Network Controllers for a Team of Self-Organizing Robots"
photo: "![image](https://user-images.githubusercontent.com/22371492/56648995-3ece3980-66bf-11e9-8611-b5b4bf92c64d.png)"
info:
  title: "Evolving Neural Network Controllers for a Team of Self-Organizing Robots"
  authors: "Istvan Fehervari, Wilfried Elemenreich"
  labs: "Mobile Systems Group/Lakeside Labs, Institute for Networked and Embedded Systems,
University of Klagenfurt, 9020 Klagenfurt, Austria"
  conference: "Journal of Robotics"
  sport: "Football"
  sport_icon: "futbol"
  url: "https://www.hindawi.com/journals/jr/2010/841286/"
authors:
- Atom Scott
date: 2019-01-01T00:00:00+09:00
description: "Summary"
type: technical_note
draft: false
---
 
## 要旨 Abstract
*論文のアブストラクトを日本語で軽く*

協調性のあるロボットのチームを成長させるGAとNNを混合させた手法を提案．
その手法のケーススタディとしてロボカップサッカーに似たシミュレーションツールを用いる．

{{ < youtube cP035M_w82s > }}

## リサーチ課題

２Dの自律型ロボットにどうサッカーを教えるか

## リサーチ課題に対する結論

ニューラルネットワークコントローラーの重みやバイアスを進化アルゴリズムで更新すると，数百世代で自律型ロボットはサッカーらしい動きを見せるようになった．

## 手法
**まずは一言で**

ガイダンス付きの進化アルゴリズムでエージェントを動かすニューラルネットワークを成長させる．

**手法の具体的な説明**

![image](https://user-images.githubusercontent.com/22371492/56800390-d9f91780-6855-11e9-9043-2090a74bffbf.png)

Back Propが使えないFully Connected ANN と記載があったので，Boltzaman Machine ？と上記に書きましたが，正確には分かりません．

Back Propが使えないからEAを使うといいつつ，どのようなEAを使ったかは明確な説明がないのでわからない．
※[Genetic Evolution of a Neural Network for the Autonomous Control of a Four-Wheeled Robot](https://mobile.aau.at/~welmenre/papers/elmenreich-2007-genetic-evolution-of-a-neural-network-for-the-autonomous-control-of-a-four-wheeled-robot.pdf)のEAを基にしたとは書いてある．

- シミュレーター

ロボカップサッカーのシミュレーターと似ているが，いくかの相違点がある．

本研究で用いたシミュレーターでは，審判とゴールキーパーはいなく，ピッチの周りに仮想の境界が設定されているためボールは外に出ない．

さらに，リアルタイムで実行されるロボカップサッカーのシミュレーターとは違い，本研究のものは計算パワーを最大限に活かすことが可能である．

選手はボールに向かって，定められた加速度で動くことができ，ボールに十分近づけば蹴る動作も可能になる．

1試合のシミュレーションは300ステップ・約60秒要する．

- [FREVO](http://frevo.sourceforge.net/)

![image](https://user-images.githubusercontent.com/22371492/56794183-9350f080-6848-11e9-966b-6b68a5e36208.png)

FREVOは本研究の進化デザインを行うために，筆者らが以前開発をしたオープンソースのフレームワークである．

**従来のアプローチとはどのように異なるか**

本研究ではBack Propができないニューラルネットワークを活用している．

これは，サッカーのように報酬が遅延して与えられることを考慮して判断したそうだ．

## 結果

６つの隠れニューロンを持ったFully Connected なネットワーク＆直行座標系の入出力（直行・曲座標系の入出力の比較実験も行っている）を活用したロボットを400世代以上まで進化させることで一番良いパフォーマンス（ほかのモデルと戦わせて勝敗を見たときに）を得ることができた．

![image](https://user-images.githubusercontent.com/22371492/56800830-edf14900-6856-11e9-8967-2ea945f784b3.png)


## コメント
*問題点や議論できることがあれば*

本研究ではBack Propができないニューラルネットワークのほうが，MLPよりも結果的によかったとしている．しかし，MLPをEAでパラメータを更新しても，うーんっていう感じはする．


## その他
**リサーチクエスチョンに関する論文**

**手法に関する論文**
