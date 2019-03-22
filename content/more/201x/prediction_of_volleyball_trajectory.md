---
title: "Prediction of Volleyball Trajectory Using Skeletal Motions of Setter Player"
photo: "https://user-images.githubusercontent.com/22371492/54799864-60906700-4ca2-11e9-9f4f-52311b9e1180.png"
info:
  title: "Prediction of Volleyball Trajectory Using Skeletal Motions of Setter Player"
  authors: "Shuya Suda, Yasutoshi Makino, Hiroyuki Shinoda"
  labs: "Graduate School of Information Science and Technology, The University of Tokyo"
  conference: ""
  sport: "Volleyball"
  sport_icon: "volleyball-ball"
  url: "https://dl.acm.org/citation.cfm?id=3311844"
authors:
- Atom Scott
date: 2019-03-022T00:00:00+09:00
description: "Summary"
type: technical_note
draft: false
---

## 要旨 Abstract
*論文のアブストラクトを日本語で軽く*

本論文では、バレーボールのトスの0.3秒前にボールの軌道を予測する手法を提案する。
入力には、Kinectより得られる関節の３次元データと比較用にOpenPoseを用いて得られた２次元のデータを用いる。

さらに、この手法を使って異なる選手におけるトス方法の違いやどの体の部位がトスの予測とか関わっているのが分かる。

## リサーチ課題
バレーボールにおいて、セッターのトス前の動きからボールの軌道を予測できるか

## リサーチ課題に対する結論
ニューラルネットを用いて、ある程度の軌道予測ができた。

## 手法
**まずは一言で**

kinectとOpenposeより得られた2種類の関節データを使って計算した重心を入力に、5層の全結合ニューラルネットワークを学習させて予測を行った。

また、入力に使う関節を変更するとRMSE誤差が変化することを用いて、予測をするために重要な入力＝関節がどれなのかが分かる。

**手法の具体的な説明**

![Screenshot from 2019-03-22 13-30-42](https://user-images.githubusercontent.com/22371492/54800793-18277800-4ca7-11e9-915e-05e576dd6b1b.png)

![Screenshot from 2019-03-22 13-44-35](https://user-images.githubusercontent.com/22371492/54801110-ac460f00-4ca8-11e9-9341-0a8aa5ca2c6b.png)

![Screenshot from 2019-03-22 13-31-09](https://user-images.githubusercontent.com/22371492/54800795-1a89d200-4ca7-11e9-9e56-1fabb67ba9f7.png)

全結合のネットワークを使っているので、入力層を工夫しないと時系列情報を扱うことができないが、本文では10フレーム分の関節座標を25関節（x,y,z）、そしてそれぞれのフレームで計算した重心のz座標を含んでいる。10*25*3+10=760なので、上記の図の入力層と一致する。

**従来のアプローチとはどのように異なるか**

体の関節からボール軌道を予測する研究は少ないので、新しい。

## 結果
ボールの軌道をある程度予測することができた。
結果は以下の表の通り。
![Screenshot from 2019-03-22 13-36-27](https://user-images.githubusercontent.com/22371492/54800966-e531b400-4ca7-11e9-9d50-9f18256ec021.png)

![Screenshot from 2019-03-22 13-36-34](https://user-images.githubusercontent.com/22371492/54800973-ed89ef00-4ca7-11e9-9997-c0ce8b4de1f6.png)


{{ < youtube tqnvM2L86-I > }}

## コメント
*問題点や議論できることがあれば*

サッカーのPK予想につかいたい！
あとネットワークのモデルはもっと工夫できるはずだと思う！

## その他
**リサーチクエスチョンに関する論文**

**手法に関する論文**

Y Horiuchi, Y Makino, H Shinoda (2017) Computational Foresight: Forecasting Human Body Motion in Real-time for Reducing Delays in Interactive System, ISS ’17 Proceedings of the 2017 ACM International Conference on Interactive Surfaces and Spaces，312-317.
