---
title: "Gait Recognition Based on Constraint Mutual Subspace Method with CNN Features"
info:
  title: "Gait Recognition Based on Constraint Mutual Subspace Method with CNN Features"
  authors: "Akinari Sakai, Naoya Sogi, Kazuhiro Fukui "
  labs: "CV lab, University of Tsukuba"
  conference: "PRMU BioX"
  sport: "all"
  sport_icon: "running"
  url: "https://www.ieice.org/ken/paper/2019031831KJ/"
authors:
- Atom Scott
date: 2019-01-01T00:00:00+09:00
description: "Summary"
type: technical_note
draft: false
---

## 要旨 Abstract
*論文のアブストラクトを日本語で軽く*

歩行認証は、カメラから離れた場所からでも動作を測定可能であるため、認識対象の協力を必要とせず識別を実行できる。
そのため、歩容認証に基づくシステムは、街中の監視や犯罪捜査など実問題に対して有効に機能することが期待されている。

従来の歩容認証手法の多くは、歩行シーケンスを集約したGEIと呼ばれる特徴量を利用している。
これに対し、相互部分空間法（MSM）に基づく手法では、歩行シーケンスの構造情報をコンパクトかつ高精度に表現可能であることが知られている。

本論文では、MSMに基づく手法を強化するために、次の２つの機能を導入する。

1. 一般化差分部分空間（GDS）への射影によるクラス部分空間の準直交化
2. 畳み込みニューラルネットワーク（CNN)を用いた各入力画像からの特徴抽出

GDSへの射影を導入した手法は、制約相互部分空間法（CMSM）と呼ばれ、画像セットに基づく識別に有効な手法として広く知られている。

提案手法は、大規模部公開データベースであるOU-ISIR Large Population Databaseを用いた1000人規模の評価実験において、98.%の精度を示した。

## リサーチ課題

歩容認証のフレームワークとしてGEIなどの手法があるが、GEIは時間変化による動きの方向や大きさのより細密構造情報を取り込むことが困難である。

もっと良い歩用認証のフレームワークはないのか。

## リサーチ課題に対する結論

相互部分空間法（MSM）に基づく手法が有効であった。

## 手法
**まずは一言で**

MSMを

1. 一般化差分部分空間（GDS）への射影によるクラス部分空間の準直交化
2. 畳み込みニューラルネットワーク（CNN)を用いた各入力画像からの特徴抽出

で強化した手法

**手法の具体的な説明**


**従来のアプローチとはどのように異なるか**

- **Gait energy image**

Gait Energy Image(GEI) は，1 つの歩行シーケンスを集約することで得られる特徴量である.
![GEI](GEI.png)

## 結果
ゴーストの動きがゴール確率を低下させる特定の状況を示した。

## コメント
*問題点や議論できることがあれば*

## その他
**リサーチクエスチョンに関する論文**

**手法に関する論文**
