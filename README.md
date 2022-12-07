# maj2p

清一色二人麻将

## 简介

这个项目是对经典 Flash 游戏 “Bamboo 麻雀” 的复刻。Bamboo 麻雀是一种麻将变体，由两位玩家使用一种花色的麻将牌进行对局。每局流程极短，但考验玩家对麻将牌型的分析能力。详细的规则与流程见 [gamerule.md](/gamerule.md) 。

本项目使用 Python 进行编写。

## 文件结构

```
maj2p
├── main.py
├── maj2p.py
├── util.py
└── yaku.py
```

`maj2p.py` 是主文件。其中定义了一局游戏中的主要元素：
* `class Hand`：手牌类
* `class HandAuto(Hand)`：由电脑控制的手牌类
* `class Wall`：牌山类
* `class MahjongError(builtins.Exception)`：与麻将逻辑有关的异常类

`util.py` 定义了一些命令行交互时的常用功能，如将麻将牌序号转换为对应的 Unicode 麻将符号等。

`yaku.py` 定义了和牌判定方法和番数、分数的计算方法。包括下列类：
* `class Han`：工具类，用于计算番数
* `class Yaku`：役种类（役满除外）
* `class Yakuman`：役满类

## 游戏流程

游戏按照 [gamerule.md#游戏流程](/gamerule.md#游戏流程) 中的流程进行。尽管一些预期内容还没能具体实现，但是游戏总体流程已经完成了。