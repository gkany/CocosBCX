## BIP

-----------

# 1. BIP 介绍

## 1.1 BIP 源头

比特币改进提案（BIP）是一项提议改进比特币协议的标准，由Amir Taaki于2011年在BIP 0001中提出，并由Luke Dash Jr.在BIP 0002中对其进行了扩展。

BIP流程严重依赖于Python改进提案（Python Enhancement Proposal ，PEP 0001），甚至直接复制了其中的一些文本。它还提到了一个名为“On Consensus and Humming in the IETF”的文件，这是一套来自互联网工程任务组的开源协作原则。

## 1.2 BIP的功能

**BIP流程的目标是允许任何人对比特币协议提出改进的想法，但在实施任何可能威胁到网络稳定性的代码之前，还要彻底审查这些想法的安全性和可行性。**

该流程旨在让社区围绕提出的想法建立粗略的共识。 P. Resnick将粗略共识定义如下：

``` text
粗略的共识已经在很多方面被定义过了：
一个简单的版本是，粗略共识意味着强烈提出的反对意见必须经历辩论，直到大多数人都认为这些反对意见是错误的。
```

赋予社区能够提出想法、同行评审想法以及围绕它们达成共识的能力，对于像比特币这样没有领导者的分布式协议的发展至关重要。自BIP流程建立以来，已经有190多个BIP Github代码仓库贡献者。

## 1.3 BIP分类

有三种不同类型的BIP：

- **标准追踪BIP**：提议了对比特币进行更改，包括更改网络协议、区块或交易有效性规则，或影响使用比特币的应用程序互操作性的任何更改。
- **信息BIP**：描述了协议中的设计问题或向社区提供信息。他们不建议为协议执行新的功能。
- **流程BIP**：提出围绕开发比特币的流程，或建议对流程进行更改。它们不直接影响比特币的代码库，但它们可能包括新程序、开发决策的变化或者比特币开发中使用工具的变化。

## 1.4 BIP实施流程

每个BIP必须经过几个不同的阶段才能实施。这是BIP 001中描述该工作流程的图像：

![img](https://appserversrc.8btc.com/newpost/201904181732094.)

要实施到话，BIP必须从草案阶段，到提议阶段，再到最终阶段。

- **草案（Draft）**：BIP作为草案提交给比特币开发邮件列表和BIP Github代码仓库。
- **提议（Proposed）**：BIP包括了一个含有部署BIP计划的工作执行方案。
- **最终（ Final）**：BIP符合现实世界的采用标准。且必须客观地验证这一点。

在此过程中，BIP可以被社区拒绝、撤回或替换：

- **延期（Deferred）**：BIP的提交人可以在没有取得任何进展的情况下将其状态更改为延期。
- **撤回（Withdrawn）**：BIP的提交人也可以选择完全撤回BIP。
- **被拒绝（Rejected）**：如果三年内没有取得任何进展，任何人都可以请求将BIP移至被拒绝状态。
- **替换（Replaced）**：如果先前的最终BIP变得无关紧要，则将其标记为已替换。例如，这种情况可能发生在，当一个在软分叉中实施的BIP，而在三个月之后却被硬分叉倾覆的时候。

### 1.4.1  草案和提议

下面，我们将详细介绍此过程的两个主要阶段。
**草案** 
草案阶段的目标是将关于比特币的新想法格式化为标准化的BIP，并尽快开始征求社区的反馈意见。

1. BIP的提交人负责审查社区的想法，以评估该想法的可行性，并围绕它建立社区共识。他们应该与比特币开发者邮件列表以及Bitcoin Talk技术论坛分享想法。这有助于确定该想法是否原创、可行并保证了一个独立的BIP。
2. 提交人创建了一份BIP草案，并将其提交给比特币开发邮件列表进行讨论。这允许作者以BIP的标准格式呈现该想法并处理来自社区的其他任何问题。
3. 在讨论之后，提交人将提议作为拉取请求提交给BIP github代码仓库。 BIP代码仓库的编辑器为提案分配一个数字，根据类型对其进行标记，然后将其添加到代码存储库中。 BIP编辑只有在不符合特定标准的情况下才能拒绝BIP——例如，如果提出的更新情况不清晰，或者在技术上不合理。
4. 为了推动草案进入提议，当提交人处理完社区中存在的任何异议时，BIP会认为草案已经完成并且其中包含了提议的工作执行方案。

草案阶段旨在允许提交者征求社区的反馈意见并修改BIP以处理在此阶段提出的任何异议。一旦完成草案阶段并提交BIP后，它将被移至提议阶段。

**提议** 

当BIP的状态更改为提议时，它现在已准备好从讨论状态转移到实际比特币协议中的部署。为此，每个BIP都需要包含具体标准，概述如何客观地建立起现实世界的采用。

通常，这意味着需要通过软分叉或硬分叉将BIP执行到代码中。

软分叉引入了向后兼容的协议更改，这意味着运行最新版本软件的节点仍然与运行旧版本的节点兼容。

与软分叉不同的是，硬叉引入了不向后兼容的协议更改。这意味着如果大量节点不升级包含新软件的客户端，则链会被一分为二，就像比特币现金（Bitcoin Cash）硬分叉一样。因此，硬分叉是比BIP实施风险更高的方式。

BIP 002为确认如何通过软分叉或硬分叉最终确定一个BIP，提供了一些指导原则：

- 一个软分叉BIP需要通过“明显处于多数的矿工”来激活。建立此“多数”的建议指南是说，95％的节点通过升级包含BIP的新软件来批准它。软分叉所激活的BIP必须包含一个BIP将在网络上的活跃时间。
- 另一方面，硬分叉BIP需要整个社区采用。网络上的节点需要升级到包含了BIP的客户端软件。 BIP 002指出硬叉BIP“需要被整个比特币经济中采用”，包括比特币的持有者，以及那些用比特币提供服务的人。它承认这可能难以实现。

鉴于难以满足硬分叉BIP的要求，实际上没有一个BIP是通过硬分叉实现的。

![img](https://appserversrc.8btc.com/newpost/201904181732107.)

*图表显示了BIP 91的激活，其中获得了超过93%的节点信号支持。（图片来源: Bitcoin Magazine.）*

只有当BIP成功地通过硬分叉或软分叉发起执行，并且在比特币协议中被实现时，才会被认为是达到了“最终”阶段。



## 1.5 BIP提交及审核过程

想要提交BIP，首先应该把自己的想法或文件发布到邮件列表。在经过讨论之后，发起者需要通过电子邮件联系Luke Dashjr <`luke_bipeditor@dashjr.org`>。经过Luke Dashjr的编辑和通过之后，BIP就会在 https://github.com/bitcoin/bips 发布了。

根据规则，任何人都是可以提交BIP的，注意，在https://github.com/bitcoin/bips 页面上发布一个BIP，并不代表它已被正式接受，当其状态变为激活（Active）时才算正式被接受。而**想要让一个BIP正式激活，这需要经过开发者社区的协商同意。**

而当前BIP的状态一共可分为9种，它们分别是：

* `Proposed` （提出）
* `Draft`（草案）
* `Active`（激活）
* `Final`（落地）
* `Replaced`（被替代）
* `Withdrawn`（撤掉）
* `Deferred`（推迟）
* `BIP number allocated` （BIP编号被分配）
* `Rejected`（拒绝）

巴比特论坛版主玛雅则根据他自己的理解将这个过程分为了[7步](http://8btc.com/thread-50193-1-2.html)：

> 第1步：**想法**，任何一个人都可以通过任何途径渠道，如论坛，推特等等，提出自己改进初步想法，来争取更多人支持认同。
> 第2步：**提案**，可以汇总社区讨论的建议，以较规范的格式，详细地描述方案，形成一个BIP提案文件提交。
> 第3步：**正式提案**，对较重要或者认可的人较多的BIP提案分配序号。以便方便大家讨论区分这个提案，有序号的提案算是正式提案。
> 第4步：**落实代码**，一些开发者会依据BIP正式提案的构思，落实成具体的代码。并且在测试网络上进行严格的测试。以确保代码尽量没有Bug。
> 第5步：**激活设定**，代码没有问题后，根据《BIP9升级规范》，设定激活门槛，分配激活标记位，缓冲时间等。
> 第6步：**发布版本**，若足够多的人签名同意，那么会吸纳此BIP代码在最新版本中发布包含这个BIP代码的版本，但是处于未激活状态。
> 第7步：**激活**，等待达到BIP9设的激活门槛后，方案正式激活生效。实测是否方案成功。若出现问题可能回到上一版本。

而当前极具争议的BIP 148，目前只是处在草案阶段（Draft），并且根据多位开发者的反应，这一草案能够激活的可能性非常低。

BIP我们应该要理性对待，只有在进入`Active`（激活）状态时，我们才认为它是被Core接受的。



## 1.6 BIP地址

``` text
https://github.com/bitcoin/bips
```

# 2. 当前BIP

## [2.1 BIP列表](https://github.com/bitcoin/bips/blob/master/README.mediawiki)

| Number                                                       | Layer                 | Title                                                        | Owner                                                        | Type          | Status               |
| ------------------------------------------------------------ | --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------- | -------------------- |
| [1](https://github.com/bitcoin/bips/blob/master/bip-0001.mediawiki) |                       | BIP Purpose and Guidelines                                   | Amir Taaki                                                   | Process       | Replaced             |
| [2](https://github.com/bitcoin/bips/blob/master/bip-0002.mediawiki) |                       | BIP process, revised                                         | Luke Dashjr                                                  | Process       | Active               |
| [8](https://github.com/bitcoin/bips/blob/master/bip-0008.mediawiki) |                       | Version bits with lock-in by height                          | Shaolin Fry                                                  | Informational | Rejected             |
| [9](https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki) |                       | Version bits with timeout and delay                          | Pieter Wuille, Peter Todd, Greg Maxwell, Rusty Russell       | Informational | Final                |
| [10](https://github.com/bitcoin/bips/blob/master/bip-0010.mediawiki) | Applications          | Multi-Sig Transaction Distribution                           | Alan Reiner                                                  | Informational | Withdrawn            |
| [11](https://github.com/bitcoin/bips/blob/master/bip-0011.mediawiki) | Applications          | M-of-N Standard Transactions                                 | Gavin Andresen                                               | Standard      | Final                |
| [12](https://github.com/bitcoin/bips/blob/master/bip-0012.mediawiki) | Consensus (soft fork) | OP_EVAL                                                      | Gavin Andresen                                               | Standard      | Withdrawn            |
| [13](https://github.com/bitcoin/bips/blob/master/bip-0013.mediawiki) | Applications          | Address Format for pay-to-script-hash                        | Gavin Andresen                                               | Standard      | Final                |
| [14](https://github.com/bitcoin/bips/blob/master/bip-0014.mediawiki) | Peer Services         | Protocol Version and User Agent                              | Amir Taaki, Patrick Strateman                                | Standard      | Final                |
| [15](https://github.com/bitcoin/bips/blob/master/bip-0015.mediawiki) | Applications          | Aliases                                                      | Amir Taaki                                                   | Standard      | Deferred             |
| [16](https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki) | Consensus (soft fork) | Pay to Script Hash                                           | Gavin Andresen                                               | Standard      | Final                |
| [17](https://github.com/bitcoin/bips/blob/master/bip-0017.mediawiki) | Consensus (soft fork) | OP_CHECKHASHVERIFY (CHV)                                     | Luke Dashjr                                                  | Standard      | Withdrawn            |
| [18](https://github.com/bitcoin/bips/blob/master/bip-0018.mediawiki) | Consensus (soft fork) | hashScriptCheck                                              | Luke Dashjr                                                  | Standard      | Proposed             |
| [19](https://github.com/bitcoin/bips/blob/master/bip-0019.mediawiki) | Applications          | M-of-N Standard Transactions (Low SigOp)                     | Luke Dashjr                                                  | Standard      | Rejected             |
| [20](https://github.com/bitcoin/bips/blob/master/bip-0020.mediawiki) | Applications          | URI Scheme                                                   | Luke Dashjr                                                  | Standard      | Replaced             |
| [21](https://github.com/bitcoin/bips/blob/master/bip-0021.mediawiki) | Applications          | URI Scheme                                                   | Nils Schneider, Matt Corallo                                 | Standard      | Final                |
| [22](https://github.com/bitcoin/bips/blob/master/bip-0022.mediawiki) | API/RPC               | getblocktemplate - Fundamentals                              | Luke Dashjr                                                  | Standard      | Final                |
| [23](https://github.com/bitcoin/bips/blob/master/bip-0023.mediawiki) | API/RPC               | getblocktemplate - Pooled Mining                             | Luke Dashjr                                                  | Standard      | Final                |
| [30](https://github.com/bitcoin/bips/blob/master/bip-0030.mediawiki) | Consensus (soft fork) | Duplicate transactions                                       | Pieter Wuille                                                | Standard      | Final                |
| [31](https://github.com/bitcoin/bips/blob/master/bip-0031.mediawiki) | Peer Services         | Pong message                                                 | Mike Hearn                                                   | Standard      | Final                |
| [32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki) | Applications          | Hierarchical Deterministic Wallets                           | Pieter Wuille                                                | Informational | Final                |
| [33](https://github.com/bitcoin/bips/blob/master/bip-0033.mediawiki) | Peer Services         | Stratized Nodes                                              | Amir Taaki                                                   | Standard      | Rejected             |
| [34](https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki) | Consensus (soft fork) | Block v2, Height in Coinbase                                 | Gavin Andresen                                               | Standard      | Final                |
| [35](https://github.com/bitcoin/bips/blob/master/bip-0035.mediawiki) | Peer Services         | mempool message                                              | Jeff Garzik                                                  | Standard      | Final                |
| [36](https://github.com/bitcoin/bips/blob/master/bip-0036.mediawiki) | Peer Services         | Custom Services                                              | Stefan Thomas                                                | Standard      | Rejected             |
| [37](https://github.com/bitcoin/bips/blob/master/bip-0037.mediawiki) | Peer Services         | Connection Bloom filtering                                   | Mike Hearn, Matt Corallo                                     | Standard      | Final                |
| [38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) | Applications          | Passphrase-protected private key                             | Mike Caldwell, Aaron Voisine                                 | Standard      | Draft                |
| [39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) | Applications          | Mnemonic code for generating deterministic keys              | Marek Palatinus, Pavol Rusnak, Aaron Voisine, Sean Bowe      | Standard      | Proposed             |
| 40                                                           | API/RPC               | Stratum wire protocol                                        | Marek Palatinus                                              | Standard      | BIP number allocated |
| 41                                                           | API/RPC               | Stratum mining protocol                                      | Marek Palatinus                                              | Standard      | BIP number allocated |
| [42](https://github.com/bitcoin/bips/blob/master/bip-0042.mediawiki) | Consensus (soft fork) | A finite monetary supply for Bitcoin                         | Pieter Wuille                                                | Standard      | Final                |
| [43](https://github.com/bitcoin/bips/blob/master/bip-0043.mediawiki) | Applications          | Purpose Field for Deterministic Wallets                      | Marek Palatinus, Pavol Rusnak                                | Informational | Final                |
| [44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki) | Applications          | Multi-Account Hierarchy for Deterministic Wallets            | Marek Palatinus, Pavol Rusnak                                | Standard      | Proposed             |
| [45](https://github.com/bitcoin/bips/blob/master/bip-0045.mediawiki) | Applications          | Structure for Deterministic P2SH Multisignature Wallets      | Manuel Araoz, Ryan X. Charles, Matias Alejo Garcia           | Standard      | Proposed             |
| [47](https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki) | Applications          | Reusable Payment Codes for Hierarchical Deterministic Wallets | Justus Ranvier                                               | Informational | Draft                |
| [49](https://github.com/bitcoin/bips/blob/master/bip-0049.mediawiki) | Applications          | Derivation scheme for P2WPKH-nested-in-P2SH based accounts   | Daniel Weigl                                                 | Informational | Final                |
| [50](https://github.com/bitcoin/bips/blob/master/bip-0050.mediawiki) |                       | March 2013 Chain Fork Post-Mortem                            | Gavin Andresen                                               | Informational | Final                |
| [60](https://github.com/bitcoin/bips/blob/master/bip-0060.mediawiki) | Peer Services         | Fixed Length "version" Message (Relay-Transactions Field)    | Amir Taaki                                                   | Standard      | Draft                |
| [61](https://github.com/bitcoin/bips/blob/master/bip-0061.mediawiki) | Peer Services         | Reject P2P message                                           | Gavin Andresen                                               | Standard      | Final                |
| [62](https://github.com/bitcoin/bips/blob/master/bip-0062.mediawiki) | Consensus (soft fork) | Dealing with malleability                                    | Pieter Wuille                                                | Standard      | Withdrawn            |
| 63                                                           | Applications          | Stealth Addresses                                            | Peter Todd                                                   | Standard      | BIP number allocated |
| [64](https://github.com/bitcoin/bips/blob/master/bip-0064.mediawiki) | Peer Services         | getutxo message                                              | Mike Hearn                                                   | Standard      | Draft                |
| [65](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) | Consensus (soft fork) | OP_CHECKLOCKTIMEVERIFY                                       | Peter Todd                                                   | Standard      | Final                |
| [66](https://github.com/bitcoin/bips/blob/master/bip-0066.mediawiki) | Consensus (soft fork) | Strict DER signatures                                        | Pieter Wuille                                                | Standard      | Final                |
| [67](https://github.com/bitcoin/bips/blob/master/bip-0067.mediawiki) | Applications          | Deterministic Pay-to-script-hash multi-signature addresses through public key sorting | Thomas Kerin, Jean-Pierre Rupp, Ruben de Vries               | Standard      | Proposed             |
| [68](https://github.com/bitcoin/bips/blob/master/bip-0068.mediawiki) | Consensus (soft fork) | Relative lock-time using consensus-enforced sequence numbers | Mark Friedenbach, BtcDrak, Nicolas Dorier, kinoshitajona     | Standard      | Final                |
| [69](https://github.com/bitcoin/bips/blob/master/bip-0069.mediawiki) | Applications          | Lexicographical Indexing of Transaction Inputs and Outputs   | Kristov Atlas                                                | Informational | Proposed             |
| [70](https://github.com/bitcoin/bips/blob/master/bip-0070.mediawiki) | Applications          | Payment Protocol                                             | Gavin Andresen, Mike Hearn                                   | Standard      | Final                |
| [71](https://github.com/bitcoin/bips/blob/master/bip-0071.mediawiki) | Applications          | Payment Protocol MIME types                                  | Gavin Andresen                                               | Standard      | Final                |
| [72](https://github.com/bitcoin/bips/blob/master/bip-0072.mediawiki) | Applications          | bitcoin: uri extensions for Payment Protocol                 | Gavin Andresen                                               | Standard      | Final                |
| [73](https://github.com/bitcoin/bips/blob/master/bip-0073.mediawiki) | Applications          | Use "Accept" header for response type negotiation with Payment Request URLs | Stephen Pair                                                 | Standard      | Final                |
| [74](https://github.com/bitcoin/bips/blob/master/bip-0074.mediawiki) | Applications          | Allow zero value OP_RETURN in Payment Protocol               | Toby Padilla                                                 | Standard      | Rejected             |
| [75](https://github.com/bitcoin/bips/blob/master/bip-0075.mediawiki) | Applications          | Out of Band Address Exchange using Payment Protocol Encryption | Justin Newton, Matt David, Aaron Voisine, James MacWhyte     | Standard      | Final                |
| [79](https://github.com/bitcoin/bips/blob/master/bip-0079.mediawiki) | Applications          | Bustapay :: a practical coinjoin protocol                    | Ryan Havar                                                   | Informational | Proposed             |
| [80](https://github.com/bitcoin/bips/blob/master/bip-0080.mediawiki) |                       | Hierarchy for Non-Colored Voting Pool Deterministic Multisig Wallets | Justus Ranvier, Jimmy Song                                   | Informational | Deferred             |
| [81](https://github.com/bitcoin/bips/blob/master/bip-0081.mediawiki) |                       | Hierarchy for Colored Voting Pool Deterministic Multisig Wallets | Justus Ranvier, Jimmy Song                                   | Informational | Deferred             |
| [83](https://github.com/bitcoin/bips/blob/master/bip-0083.mediawiki) | Applications          | Dynamic Hierarchical Deterministic Key Trees                 | Eric Lombrozo                                                | Standard      | Draft                |
| [84](https://github.com/bitcoin/bips/blob/master/bip-0084.mediawiki) | Applications          | Derivation scheme for P2WPKH based accounts                  | Pavol Rusnak                                                 | Informational | Draft                |
| [90](https://github.com/bitcoin/bips/blob/master/bip-0090.mediawiki) |                       | Buried Deployments                                           | Suhas Daftuar                                                | Informational | Draft                |
| [91](https://github.com/bitcoin/bips/blob/master/bip-0091.mediawiki) | Consensus (soft fork) | Reduced threshold Segwit MASF                                | James Hilliard                                               | Standard      | Final                |
| [98](https://github.com/bitcoin/bips/blob/master/bip-0098.mediawiki) | Consensus (soft fork) | Fast Merkle Trees                                            | Mark Friedenbach, Kalle Alm, BtcDrak                         | Standard      | Draft                |
| [99](https://github.com/bitcoin/bips/blob/master/bip-0099.mediawiki) |                       | Motivation and deployment of consensus rule changes ([soft/hard]forks) | Jorge Timón                                                  | Informational | Draft                |
| [100](https://github.com/bitcoin/bips/blob/master/bip-0100.mediawiki) | Consensus (hard fork) | Dynamic maximum block size by miner vote                     | Jeff Garzik, Tom Harding, Dagur Valberg Johannsson           | Standard      | Rejected             |
| [101](https://github.com/bitcoin/bips/blob/master/bip-0101.mediawiki) | Consensus (hard fork) | Increase maximum block size                                  | Gavin Andresen                                               | Standard      | Withdrawn            |
| [102](https://github.com/bitcoin/bips/blob/master/bip-0102.mediawiki) | Consensus (hard fork) | Block size increase to 2MB                                   | Jeff Garzik                                                  | Standard      | Rejected             |
| [103](https://github.com/bitcoin/bips/blob/master/bip-0103.mediawiki) | Consensus (hard fork) | Block size following technological growth                    | Pieter Wuille                                                | Standard      | Withdrawn            |
| [104](https://github.com/bitcoin/bips/blob/master/bip-0104.mediawiki) | Consensus (hard fork) | 'Block75' - Max block size like difficulty                   | t.khan                                                       | Standard      | Draft                |
| [105](https://github.com/bitcoin/bips/blob/master/bip-0105.mediawiki) | Consensus (hard fork) | Consensus based block size retargeting algorithm             | BtcDrak                                                      | Standard      | Draft                |
| [106](https://github.com/bitcoin/bips/blob/master/bip-0106.mediawiki) | Consensus (hard fork) | Dynamically Controlled Bitcoin Block Size Max Cap            | Upal Chakraborty                                             | Standard      | Draft                |
| [107](https://github.com/bitcoin/bips/blob/master/bip-0107.mediawiki) | Consensus (hard fork) | Dynamic limit on the block size                              | Washington Y. Sanchez                                        | Standard      | Draft                |
| [109](https://github.com/bitcoin/bips/blob/master/bip-0109.mediawiki) | Consensus (hard fork) | Two million byte size limit with sigop and sighash limits    | Gavin Andresen                                               | Standard      | Rejected             |
| [111](https://github.com/bitcoin/bips/blob/master/bip-0111.mediawiki) | Peer Services         | NODE_BLOOM service bit                                       | Matt Corallo, Peter Todd                                     | Standard      | Proposed             |
| [112](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) | Consensus (soft fork) | CHECKSEQUENCEVERIFY                                          | BtcDrak, Mark Friedenbach, Eric Lombrozo                     | Standard      | Final                |
| [113](https://github.com/bitcoin/bips/blob/master/bip-0113.mediawiki) | Consensus (soft fork) | Median time-past as endpoint for lock-time calculations      | Thomas Kerin, Mark Friedenbach                               | Standard      | Final                |
| [114](https://github.com/bitcoin/bips/blob/master/bip-0114.mediawiki) | Consensus (soft fork) | Merkelized Abstract Syntax Tree                              | Johnson Lau                                                  | Standard      | Draft                |
| [115](https://github.com/bitcoin/bips/blob/master/bip-0115.mediawiki) | Consensus (soft fork) | Generic anti-replay protection using Script                  | Luke Dashjr                                                  | Standard      | Draft                |
| [116](https://github.com/bitcoin/bips/blob/master/bip-0116.mediawiki) | Consensus (soft fork) | MERKLEBRANCHVERIFY                                           | Mark Friedenbach, Kalle Alm, BtcDrak                         | Standard      | Draft                |
| [117](https://github.com/bitcoin/bips/blob/master/bip-0117.mediawiki) | Consensus (soft fork) | Tail Call Execution Semantics                                | Mark Friedenbach, Kalle Alm, BtcDrak                         | Standard      | Draft                |
| [118](https://github.com/bitcoin/bips/blob/master/bip-0118.mediawiki) | Consensus (soft fork) | SIGHASH_NOINPUT                                              | Christian Decker                                             | Standard      | Draft                |
| [119](https://github.com/bitcoin/bips/blob/master/bip-0119.mediawiki) | Consensus (soft fork) | CHECKTEMPLATEVERIFY                                          | Jeremy Rubin                                                 | Standard      | Draft                |
| [120](https://github.com/bitcoin/bips/blob/master/bip-0120.mediawiki) | Applications          | Proof of Payment                                             | Kalle Rosenbaum                                              | Standard      | Withdrawn            |
| [121](https://github.com/bitcoin/bips/blob/master/bip-0121.mediawiki) | Applications          | Proof of Payment URI scheme                                  | Kalle Rosenbaum                                              | Standard      | Withdrawn            |
| [122](https://github.com/bitcoin/bips/blob/master/bip-0122.mediawiki) | Applications          | URI scheme for Blockchain references / exploration           | Marco Pontello                                               | Standard      | Draft                |
| [123](https://github.com/bitcoin/bips/blob/master/bip-0123.mediawiki) |                       | BIP Classification                                           | Eric Lombrozo                                                | Process       | Active               |
| [124](https://github.com/bitcoin/bips/blob/master/bip-0124.mediawiki) | Applications          | Hierarchical Deterministic Script Templates                  | Eric Lombrozo, William Swanson                               | Informational | Draft                |
| [125](https://github.com/bitcoin/bips/blob/master/bip-0125.mediawiki) | Applications          | Opt-in Full Replace-by-Fee Signaling                         | David A. Harding, Peter Todd                                 | Standard      | Proposed             |
| [126](https://github.com/bitcoin/bips/blob/master/bip-0126.mediawiki) |                       | Best Practices for Heterogeneous Input Script Transactions   | Kristov Atlas                                                | Informational | Draft                |
| [127](https://github.com/bitcoin/bips/blob/master/bip-0127.mediawiki) | Applications          | Simple Proof-of-Reserves Transactions                        | Steven Roose                                                 | Standard      | Draft                |
| [130](https://github.com/bitcoin/bips/blob/master/bip-0130.mediawiki) | Peer Services         | sendheaders message                                          | Suhas Daftuar                                                | Standard      | Proposed             |
| [131](https://github.com/bitcoin/bips/blob/master/bip-0131.mediawiki) | Consensus (hard fork) | "Coalescing Transaction" Specification (wildcard inputs)     | Chris Priest                                                 | Standard      | Draft                |
| [132](https://github.com/bitcoin/bips/blob/master/bip-0132.mediawiki) |                       | Committee-based BIP Acceptance Process                       | Andy Chase                                                   | Process       | Withdrawn            |
| [133](https://github.com/bitcoin/bips/blob/master/bip-0133.mediawiki) | Peer Services         | feefilter message                                            | Alex Morcos                                                  | Standard      | Draft                |
| [134](https://github.com/bitcoin/bips/blob/master/bip-0134.mediawiki) | Consensus (hard fork) | Flexible Transactions                                        | Tom Zander                                                   | Standard      | Draft                |
| [135](https://github.com/bitcoin/bips/blob/master/bip-0135.mediawiki) |                       | Generalized version bits voting                              | Sancho Panza                                                 | Informational | Draft                |
| [136](https://github.com/bitcoin/bips/blob/master/bip-0136.mediawiki) | Applications          | Bech32 Encoded Tx Position References                        | Велеслав, Jonas Schnelli, Daniel Pape                        | Informational | Draft                |
| [137](https://github.com/bitcoin/bips/blob/master/bip-0137.mediawiki) | Applications          | Signatures of Messages using Private Keys                    | Christopher Gilliard                                         | Standard      | Final                |
| [140](https://github.com/bitcoin/bips/blob/master/bip-0140.mediawiki) | Consensus (soft fork) | Normalized TXID                                              | Christian Decker                                             | Standard      | Draft                |
| [141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki) | Consensus (soft fork) | Segregated Witness (Consensus layer)                         | Eric Lombrozo, Johnson Lau, Pieter Wuille                    | Standard      | Final                |
| [142](https://github.com/bitcoin/bips/blob/master/bip-0142.mediawiki) | Applications          | Address Format for Segregated Witness                        | Johnson Lau                                                  | Standard      | Withdrawn            |
| [143](https://github.com/bitcoin/bips/blob/master/bip-0143.mediawiki) | Consensus (soft fork) | Transaction Signature Verification for Version 0 Witness Program | Johnson Lau, Pieter Wuille                                   | Standard      | Final                |
| [144](https://github.com/bitcoin/bips/blob/master/bip-0144.mediawiki) | Peer Services         | Segregated Witness (Peer Services)                           | Eric Lombrozo, Pieter Wuille                                 | Standard      | Final                |
| [145](https://github.com/bitcoin/bips/blob/master/bip-0145.mediawiki) | API/RPC               | getblocktemplate Updates for Segregated Witness              | Luke Dashjr                                                  | Standard      | Final                |
| [146](https://github.com/bitcoin/bips/blob/master/bip-0146.mediawiki) | Consensus (soft fork) | Dealing with signature encoding malleability                 | Johnson Lau, Pieter Wuille                                   | Standard      | Draft                |
| [147](https://github.com/bitcoin/bips/blob/master/bip-0147.mediawiki) | Consensus (soft fork) | Dealing with dummy stack element malleability                | Johnson Lau                                                  | Standard      | Final                |
| [148](https://github.com/bitcoin/bips/blob/master/bip-0148.mediawiki) | Consensus (soft fork) | Mandatory activation of segwit deployment                    | Shaolin Fry                                                  | Standard      | Final                |
| [149](https://github.com/bitcoin/bips/blob/master/bip-0149.mediawiki) | Consensus (soft fork) | Segregated Witness (second deployment)                       | Shaolin Fry                                                  | Standard      | Withdrawn            |
| [150](https://github.com/bitcoin/bips/blob/master/bip-0150.mediawiki) | Peer Services         | Peer Authentication                                          | Jonas Schnelli                                               | Standard      | Draft                |
| [151](https://github.com/bitcoin/bips/blob/master/bip-0151.mediawiki) | Peer Services         | Peer-to-Peer Communication Encryption                        | Jonas Schnelli                                               | Standard      | Withdrawn            |
| [152](https://github.com/bitcoin/bips/blob/master/bip-0152.mediawiki) | Peer Services         | Compact Block Relay                                          | Matt Corallo                                                 | Standard      | Final                |
| [154](https://github.com/bitcoin/bips/blob/master/bip-0154.mediawiki) | Peer Services         | Rate Limiting via peer specified challenges                  | Karl-Johan Alm                                               | Standard      | Withdrawn            |
| [155](https://github.com/bitcoin/bips/blob/master/bip-0155.mediawiki) | Peer Services         | addrv2 message                                               | Wladimir J. van der Laan                                     | Standard      | Draft                |
| [156](https://github.com/bitcoin/bips/blob/master/bip-0156.mediawiki) | Peer Services         | Dandelion - Privacy Enhancing Routing                        | Brad Denby, Andrew Miller, Giulia Fanti, Surya Bakshi, Shaileshh Bojja Venkatakrishnan, Pramod Viswanath | Standard      | Draft                |
| [157](https://github.com/bitcoin/bips/blob/master/bip-0157.mediawiki) | Peer Services         | Client Side Block Filtering                                  | Olaoluwa Osuntokun, Alex Akselrod, Jim Posen                 | Standard      | Draft                |
| [158](https://github.com/bitcoin/bips/blob/master/bip-0158.mediawiki) | Peer Services         | Compact Block Filters for Light Clients                      | Olaoluwa Osuntokun, Alex Akselrod                            | Standard      | Draft                |
| [159](https://github.com/bitcoin/bips/blob/master/bip-0159.mediawiki) | Peer Services         | NODE_NETWORK_LIMITED service bit                             | Jonas Schnelli                                               | Standard      | Draft                |
| [171](https://github.com/bitcoin/bips/blob/master/bip-0171.mediawiki) | Applications          | Currency/exchange rate information API                       | Luke Dashjr                                                  | Standard      | Draft                |
| [173](https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki) | Applications          | Base32 address format for native v0-16 witness outputs       | Pieter Wuille, Greg Maxwell                                  | Informational | Final                |
| [174](https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki) | Applications          | Partially Signed Bitcoin Transaction Format                  | Andrew Chow                                                  | Standard      | Proposed             |
| [175](https://github.com/bitcoin/bips/blob/master/bip-0175.mediawiki) | Applications          | Pay to Contract Protocol                                     | Omar Shibli, Nicholas Gregory                                | Informational | Draft                |
| [176](https://github.com/bitcoin/bips/blob/master/bip-0176.mediawiki) |                       | Bits Denomination                                            | Jimmy Song                                                   | Informational | Draft                |
| [178](https://github.com/bitcoin/bips/blob/master/bip-0178.mediawiki) | Applications          | Version Extended WIF                                         | Karl-Johan Alm                                               | Standard      | Draft                |
| [179](https://github.com/bitcoin/bips/blob/master/bip-0179.mediawiki) |                       | Name for payment recipient identifiers                       | Emil Engler, MarcoFalke, Luke Dashjr                         | Informational | Draft                |
| [180](https://github.com/bitcoin/bips/blob/master/bip-0180.mediawiki) | Peer Services         | Block size/weight fraud proof                                | Luke Dashjr                                                  | Standard      | Draft                |
| [197](https://github.com/bitcoin/bips/blob/master/bip-0197.mediawiki) | Applications          | Hashed Time-Locked Collateral Contract                       | Matthew Black, Tony Cai                                      | Standard      | Draft                |
| [199](https://github.com/bitcoin/bips/blob/master/bip-0199.mediawiki) | Applications          | Hashed Time-Locked Contract transactions                     | Sean Bowe, Daira Hopwood                                     | Standard      | Draft                |
| [300](https://github.com/bitcoin/bips/blob/master/bip-0300.mediawiki) | Consensus (soft fork) | Hashrate Escrows (Consensus layer)                           | Paul Sztorc, CryptAxe                                        | Standard      | Draft                |
| [301](https://github.com/bitcoin/bips/blob/master/bip-0301.mediawiki) | Consensus (soft fork) | Blind Merged Mining (Consensus layer)                        | Paul Sztorc, CryptAxe                                        | Standard      | Draft                |
| [310](https://github.com/bitcoin/bips/blob/master/bip-0310.mediawiki) | Applications          | Stratum protocol extensions                                  | Pavel Moravec, Jan Čapek                                     | Informational | Draft                |
| [320](https://github.com/bitcoin/bips/blob/master/bip-0320.mediawiki) |                       | nVersion bits for general purpose use                        | BtcDrak                                                      | Standard      | Draft                |
| [322](https://github.com/bitcoin/bips/blob/master/bip-0322.mediawiki) | Applications          | Generic Signed Message Format                                | Karl-Johan Alm                                               | Standard      | Draft                |
| [325](https://github.com/bitcoin/bips/blob/master/bip-0325.mediawiki) | Applications          | Signet                                                       | Karl-Johan Alm                                               | Standard      | Draft                |
| [330](https://github.com/bitcoin/bips/blob/master/bip-0330.mediawiki) | Peer Services         | Transaction announcements reconciliation                     | Gleb Naumenko, Pieter Wuille                                 | Standard      | Draft                |
| [340](https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki) |                       | Schnorr Signatures for secp256k1                             | Pieter Wuille, Jonas Nick, Tim Ruffing                       | Standard      | Draft                |
| [341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) | Consensus (soft fork) | Taproot: SegWit version 1 spending rules                     | Pieter Wuille, Jonas Nick, Anthony Towns                     | Standard      | Draft                |
| [342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki) | Consensus (soft fork) | Validation of Taproot Scripts                                | Pieter Wuille, Jonas Nick, Anthony Towns                     | Standard      | Draft                |

## 2.2 bips 
### 2.2.1 bip-0001 -- Replaced

对bip进行介绍，包括：什么是bip、bip的类型、工作流程等。[详细](https://github.com/bitcoin/bips/blob/master/bip-0001.mediawiki)

### 2.2.2 bip-0002  --  Active

对bip-0001进行补充， [详细](https://github.com/bitcoin/bips/blob/master/bip-0002.mediawiki)

### 2.2.3 bip-0008 -- Rejected

对BIP9的更改，该更改将基于时间的激活替换为块高度，并保证了向后兼容的更改（又称为“软分叉”）的激活。

### 2.2.4 bip-0009 -- Final

[软分叉升级规则](https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki)

软分叉升级主要是在原有的主链上增加共识规则。

软分叉的目的是为了让老版本的客户端能够兼容。我们人为设定一个开始时间和结束时间，表示在这个范围内，我们进行软分叉升级，我们规定每到 2016 的整数倍作为一个升级的周期，那么在这个周期内，如果有 80% 的算力认可我的提议，那么就代表升级成功，将该提议添加为共识规则的一部分，如果不够 80%，就进入下一个周期，也就是，在结束时间到达之前，我有可能已经升级成功，也有可能升级不成功。在升级过程中，没有成功的 block，我按照原先的规则保留，但是升级成功之后，假设我又来了之前的一个 block，我会进行check，然后将其抛弃掉。

### 2.2.5 bip-0010 -- Withdrawn

[交易多重签名](https://github.com/bitcoin/bips/blob/master/bip-0010.mediawiki)

### 2.2.6 bip-0011 -- Final

[多重签名](https://github.com/bitcoin/bips/blob/master/bip-0011.mediawiki)

交易需要用M中的N个私钥来签名(多重签名)，并把它作为新的“标准”交易类型。

### 2.2.7 bip-0012 -- Withdrawn

在共识层上的Bitcoin脚本系统中，增加OP_EVAL指令，[详细](https://github.com/bitcoin/bips/blob/master/bip-0012.mediawiki)

应用：小蚁链根据此提案，实现了图灵完备的比特币脚本系统

### 2.2.8 bip-0013 -- Final

[支持复杂交易的新型Bitcoin地址](https://github.com/bitcoin/bips/blob/master/bip-0013.mediawiki)

### 2.2.9 bip-0014 -- Final

将协议版本与客户端版本分开，[详细](https://github.com/bitcoin/bips/blob/master/bip-0014.mediawiki)

### 2.2.10 bip--0015 -- Deferred

付款协议，比特币别名系统，[详细](https://github.com/bitcoin/bips/blob/master/bip-0015.mediawiki)

### 2.2.11 bip-0016 -- Final

给Bitcoin脚本系统增加新的标准交易类型:`OP_HASH160`，`Pay to Script Hash(P2SH)`，[详细](https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki)

### 2.2.12 bip-0017 -- Withdrawn

新增标准交易类型：`OP_CHECKHASHVERIFY`，[详细](https://github.com/bitcoin/bips/blob/master/bip-0017.mediawiki)

### 2.2.13 bip-0018 -- Proposed

[详细](https://github.com/bitcoin/bips/blob/master/bip-0018.mediawiki)

### 2.2.14 bip-0019 -- Rejected

M-of-N 多签

### 2.2.15 bip-0020 -- Replaced

该BIP提出了用于进行比特币付款的URI方案。[详细](https://github.com/bitcoin/bips/blob/master/bip-0020.mediawiki)

### 2.2.16 bip-0021 -- Final

类似于bip-0020，该BIP提出了用于进行比特币付款的URI方案。[详细](https://github.com/bitcoin/bips/blob/master/bip-0021.mediawiki)

### 2.2.17 bip-0022 -- Final

rpc-api: getblocktemplate - Fundamentals，[详细](https://github.com/bitcoin/bips/blob/master/bip-0022.mediawiki)

### 2.2.18 bip-0023 -- Final

rpc-api: getblocktemplate - Pooled Mining，[详细](https://github.com/bitcoin/bips/blob/master/bip-0023.mediawiki)

### 2.2.19 bip-0024





