---
title: "Data-Driven Ghosting using Deep Imitation Learning"
publisher: "MIT SSAC"
authors: Atom Scott
date: 2017-02-20T11:53:49-07:00
description: "Summary"
type: technical_note
draft: false
---

**url : http://www.sloansportsconference.com/wp-content/uploads/2017/02/1671-2.pdf**


## 要旨 Abstract
*論文のアブストラクトを日本語で*

Current state-of-the-art sports metrics such as “Wins-above-Replacement” in baseball, “Expected Point Value” in basketball, and “Expected Goal Value” in soccer and hockey are now commonplace in performance analysis. These measures have enhanced our ability to compare and value performance in sport.  But they are inherently limited because they are tied to a discrete outcome of a specific event. With the widespread (and growing) availability of player and ball tracking data comes the potential to quantitatively analyze and compare fine-grain movement patterns. An excellent example of this was the “ghosting” system developed by the Toronto Raptors to analyze player decision-making in STATS SportVU tracking data. Specifically, the Raptors created software to predict what a defensive player should have done instead of what they actually did. Motivated by the original “ghosting” work, we showcase an automatic “data-driven ghosting” method using advanced machine learning methodologies called “deep imitation learning”, applied to a season’s worth of tracking data from a recent professional league in soccer. Our ghosting method, which avoids substantial manual human annotation, results in a data-driven system that allows us to answer the question “how should this player or team have played in a given game situation compare to the league average?”. In addition, by “fine-tuning” our league average model to the tracking data from a particular team, our ghosting technique can estimate how each team might have approached the situation. Our method enables counterfactual analysis of effectiveness of defensive positioning as both a measurable and viewable quantity for the first time.

## リサーチ課題
**
きめ細かく守備をスケーラブルに定量化し，分析するにはどうすればよいか？

## リサーチ課題に対する結論
データ駆動ゴーストを使用して，選手が取った守備と理想的な守備との差を求める。

## 手法
*まずは一言で*

模倣学習（アルファゴー）とゴースティング（トロントラプターズ）

**手法の具体的な説明**

**従来のアプローチとはどのように異なるか**

## 検証方法 Methods
ゴーストの動きがゴール確率を低下させる特定の状況を示した。

## コメント Comment
*問題点や議論できることがあれば*

## その他
**リサーチクエスチョンに関する論文**

**手法に関する論文**
