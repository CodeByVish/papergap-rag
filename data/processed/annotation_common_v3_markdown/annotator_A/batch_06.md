# Passage relevance annotation

Annotator: Jingshuai Qian

Enter your name or agreed identifier after `Annotator:`.

Judge whether each passage helps answer the question, including useful partial evidence. Topic overlap alone is insufficient.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Preserve all content and record numbers. Work independently; do not exchange labels before submission. Algorithm sources are disclosed.

## Question 0101

Paper: Linguistic Input Features Improve Neural Machine Translation

> What morphological features are considered?

### Common Retrieved Chunks

#### Passage 914

Retrieved by: BM25, Hybrid RRF

> Using lemmas as input features guarantees sharing of information between word forms that share the same base form. In principle, neural models can learn that inflectional variants are semantically related, and represent them as similar points in the continuous vector space BIBREF9 . However, while this has been demonstrated for high-frequency words, we expect that a lemmatized representation increases data efficiency; low-frequency variants may even be unknown to word-level models. With character- or subword-level models, it is unclear to what extent they can learn the similarity between low-frequency word forms that share a lemma, especially if the word forms are superficially dissimilar. Consider the following two German word forms, which share the lemma liegen `lie':
> 
> liegt `lies' (3.p.sg. present)
> 
> läge `lay' (3.p.sg. subjunctive II)
> 
> The lemmatisers we use are based on finite-state methods, which ensures a large coverage, even for infrequent word forms. We use the Zmorge analyzer for German BIBREF10 , BIBREF11 , and the lemmatiser in the Stanford CoreNLP toolkit for English BIBREF6 .

#### Relevance 914

Label: 1
> Reason
> - Summary of question: Which morphological features are considered?
> - Summary of passage: Lemmas share information across inflected word forms.
> - Judgement: Lemmatization and inflection examples provide morphological clues, even without a full feature list.
> 原因
> - 问题概述：研究考虑哪些形态特征？
> - Passage 概述：词元使不同屈折词形共享信息。
> - 判断：词元化与屈折变化示例提供形态线索，虽未列出完整特征。

#### Passage 915

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> For German INLINEFORM0 English, the parser annotates the German input with morphological features. Different word types have different sets of features – for instance, nouns have case, number and gender, while verbs have person, number, tense and aspect – and features may be underspecified. We treat the concatenation of all morphological features of a word, using a special symbol for underspecified features, as a string, and treat each such string as a separate feature value.

#### Relevance 915

Label: 1
> Reason
> - Summary of question: Which morphological features are considered?
> - Summary of passage: Nouns use case, number and gender; verbs use person, number, tense and aspect.
> - Judgement: It explicitly lists the morphological features considered.
> 原因
> - 问题概述：研究考虑哪些形态特征？
> - Passage 概述：名词使用格、数、性，动词使用人称、数、时态和体。
> - 判断：它直接列出了所考虑的形态特征。

#### Passage 916

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this paper we investigate whether linguistic input features are beneficial to neural machine translation, and our empirical evidence suggests that this is the case.
> 
> We describe a generalization of the encoder in the popular attentional encoder-decoder architecture for neural machine translation that allows for the inclusion of an arbitrary number of input features. We empirically test the inclusion of various linguistic features, including lemmas, part-of-speech tags, syntactic dependency labels, and morphological features, into English INLINEFORM0 German, and English INLINEFORM1 Romanian neural MT systems. Our experiments show that the linguistic features yield improvements over our baseline, resulting in improvements on newstest2016 of 1.5 Bleu for German INLINEFORM2 English, 0.6 Bleu for English INLINEFORM3 German, and 1.0 Bleu for English INLINEFORM4 Romanian.
> 
> In the future, we expect several developments that will shed more light on the usefulness of linguistic (or other) input features, and whether they will establish themselves as a core component of neural machine translation. On the one hand, the machine learning capability of neural architectures is likely to increase, decreasing the benefit provided by the features we tested. On the other hand, there is potential to explore the inclusion of novel features for neural MT, which might prove to be even more helpful than the ones we investigated, and the features we investigated may prove especially helpful for some translation settings, such as very low-resourced settings and/or translation settings with a highly inflected source language.

#### Relevance 916

Label: 1
> Reason
> - Summary of question: Which morphological features are considered?
> - Summary of passage: Linguistic input features improve translation scores.
> - Judgement: It confirms morphological features are included and places them among the linguistic inputs.
> 原因
> - 问题概述：研究考虑哪些形态特征？
> - Passage 概述：语言学输入特征提高了翻译分数。
> - 判断：它确认采用形态特征，并说明其在语言学输入中的位置。

#### Passage 917

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Table TABREF32 shows our main results for German INLINEFORM0 English, and English INLINEFORM1 German. The baseline system is a neural MT system with only one input feature, the (sub)words themselves. For both translation directions, linguistic features improve the best perplexity on the development data (47.3 INLINEFORM2 46.2, and 54.9 INLINEFORM3 52.9, respectively). For German INLINEFORM4 English, the linguistic features lead to an increase of 1.5 Bleu (31.4 INLINEFORM5 32.9) and 0.5 chrF3 (58.0 INLINEFORM6 58.5), on the newstest2016 test set. For English INLINEFORM7 German, we observe improvements of 0.6 Bleu (27.8 INLINEFORM8 28.4) and 1.2 chrF3 (56.0 INLINEFORM9 57.2).
> 
> To evaluate the effectiveness of different linguistic features in isolation, we performed contrastive experiments in which only a single feature was added to the baseline. Results are shown in Table TABREF33 . Unsurprisingly, the combination of all features (Table TABREF32 ) gives the highest improvement, averaged over metrics and test sets, but most features are beneficial on their own. Subword tags give small improvements for English INLINEFORM0 German, but not for German INLINEFORM1 English. All other features outperform the baseline in terms of perplexity, and yield significant improvements in Bleu on at least one test set. The gain from different features is not fully cumulative; we note that the information encoded in different features overlaps. For instance, both the dependency labels and the morphological features encode the distinction between German subjects and accusative objects, the former through different labels (subj and obja), the latter through grammatical case (nominative and accusative).
> 
> We also evaluated adding linguistic features to a stronger baseline, which includes synthetic parallel training data. In addition, we compare our neural systems against phrase-based (PBSMT) and syntax-based (SBSMT) systems by BIBREF18 , all of which make use of linguistic annotation on the source and/or target side. Results are shown in Table TABREF34 . For German INLINEFORM0 English, we observe similar improvements in the best development perplexity (45.2 INLINEFORM1 44.1), test set Bleu (37.5 INLINEFORM2 38.5) and chrF3 (62.2 INLINEFORM3 62.8). Our test set Bleu is on par to the best submitted system to this year's WMT 16 shared translation task, which is similar to our baseline MT system, but which also uses a right-to-left decoder

#### Relevance 917

Label: 1
> Reason
> - Summary of question: Which morphological features are considered?
> - Summary of passage: Feature ablations discuss grammatical case, including nominative and accusative.
> - Judgement: Grammatical case is explicitly identified as a morphological feature, providing partial evidence.
> 原因
> - 问题概述：研究考虑哪些形态特征？
> - Passage 概述：特征消融讨论语法格，包括主格和宾格。
> - 判断：它明确说明语法格属于形态特征，提供部分答案。

#### Passage 919

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> English, especially for prose in the news domain. A syntactic annotation of the source sentence could support the attentional encoder-decoder in learning which words in the German source to attend (and translate) first.
> 
> We will investigate the usefulness of linguistic features for the language pair German INLINEFORM0 English, considering the following linguistic features:
> 
> The inclusion of lemmas is motivated by the hope for a better generalization over inflectional variants of the same word form. The other linguistic features are motivated by disambiguation, as discussed in our introductory examples.

#### Relevance 919

Label: 1
> Reason
> - Summary of question: Which morphological features are considered?
> - Summary of passage: Lemmas aid generalization and other features aid disambiguation.
> - Judgement: Its discussion of inflectional variants and lemmas provides partial morphological context.
> 原因
> - 问题概述：研究考虑哪些形态特征？
> - Passage 概述：词元有助于泛化，其他特征帮助消歧。
> - 判断：关于屈折变体和词元的讨论提供部分形态信息。

#### Passage 920

Retrieved by: Dense, Hybrid RRF

> Our generalized model of the previous section supports an arbitrary number of input features. In this paper, we will focus on a number of well-known linguistic features. Our main empirical question is if providing linguistic features to the encoder improves the translation quality of neural machine translation systems, or if the information emerges from training encoder-decoder models on raw text, making its inclusion via explicit features redundant. All linguistic features are predicted automatically; we use Stanford CoreNLP BIBREF5 , BIBREF6 , BIBREF7 to annotate the English input for English INLINEFORM0 German, and ParZu BIBREF8 to annotate the German input for German INLINEFORM1 English. We here discuss the individual features in more detail.

#### Relevance 920

Label: 1
> Reason
> - Summary of question: Which morphological features are considered?
> - Summary of passage: CoreNLP and ParZu automatically annotate linguistic input features.
> - Judgement: It identifies the annotation tools and language directions used to obtain linguistic features.
> 原因
> - 问题概述：研究考虑哪些形态特征？
> - Passage 概述：CoreNLP 和 ParZu 自动标注语言学输入特征。
> - 判断：它指出获取语言学特征所用的标注工具和翻译方向，可作为辅助线索。

### BM25

#### Passage 918

Retrieved by: BM25

> Linguistic features have been used in neural language modelling BIBREF4 , and are also used in other tasks for which neural models have recently been employed, such as syntactic parsing BIBREF7 . This paper addresses the question whether linguistic features on the source side are beneficial for neural machine translation. On the target side, linguistic features are harder to obtain for a generation task such as machine translation, since this would require incremental parsing of the hypotheses at test time, and this is possible future work.
> 
> Among others, our model incorporates information from a dependency annotation, but is still a sequence-to-sequence model. 2016arXiv160306075E propose a tree-to-sequence model whose encoder computes vector representations for each phrase in the source tree. Their focus is on exploiting the (unlabelled) structure of a syntactic annotation, whereas we are focused on the disambiguation power of the functional dependency labels.
> 
> Factored translation models are often used in phrase-based SMT BIBREF21 as a means to incorporate extra linguistic information. However, neural MT can provide a much more flexible mechanism for adding such information. Because phrase-based models cannot easily generalize to new feature combinations, the individual models either treat each feature combination as an atomic unit, resulting in data sparsity, or assume independence between features, for instance by having separate language models for words and POS tags. In contrast, we exploit the strong generalization ability of neural networks, and expect that even new feature combinations, e.g. a word that appears in a novel syntactic function, are handled gracefully.
> 
> One could consider the lemmatized representation of the input as a second source text, and perform multi-source translation BIBREF22 . The main technical difference is that in our approach, the encoder and attention layers are shared between features, which we deem appropriate for the types of features that we tested.

#### Relevance 918

Label: 1
> Reason
> - Summary of question: Which morphological features are considered?
> - Summary of passage: Related work compares dependency features and factored translation models.
> - Judgement: The discussion of factored linguistic inputs and feature sharing provides supporting context for the feature design.
> 原因
> - 问题概述：研究考虑哪些形态特征？
> - Passage 概述：相关工作比较依存特征与因子化翻译模型。
> - 判断：因子化语言学输入和特征共享的讨论为特征设计提供辅助线索。

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 921

Retrieved by: Hybrid RRF followed by BGE reranking

> Neural machine translation has recently achieved impressive results BIBREF0 , BIBREF1 , while learning from raw, sentence-aligned parallel text and using little in the way of external linguistic information. However, we hypothesize that various levels of linguistic annotation can be valuable for neural machine translation. Lemmatisation can reduce data sparseness, and allow inflectional variants of the same word to explicitly share a representation in the model. Other types of annotation, such as parts-of-speech (POS) or syntactic dependency labels, can help in disambiguation. In this paper we investigate whether linguistic information is beneficial to neural translation models, or whether their strong learning capability makes explicit linguistic features redundant.
> 
> Let us motivate the use of linguistic features using examples of actual translation errors by neural MT systems. In translation out of English, one problem is that the same surface word form may be shared between several word types, due to homonymy or word formation processes such as conversion. For instance, close can be a verb, adjective, or noun, and these different meanings often have distinct translations into other languages. Consider the following English INLINEFORM0 German example:
> 
> For the English source sentence in Example SECREF4 (our translation in Example SECREF5 ), a neural MT system (our baseline system from Section SECREF4 ) mistranslates close as a verb, and produces the German verb schließen (Example SECREF6 ), even though close is an adjective in this sentence, which has the German translation nah. Intuitively, part-of-speech annotation of the English input could disambiguate between verb, noun, and adjective meanings of close.
> 
> As a second example, consider the following German INLINEFORM0 English example:
> 
> German main clauses have a verb-second (V2) word order, whereas English word order is generally SVO. The German sentence (Example UID7 ; English reference in Example UID8 ) topicalizes the predicate gefährlich 'dangerous', putting the subject die Route 'the route' after the verb. Our baseline system (Example UID9 ) retains the original word order, which is highly unusual in English, especially for prose in the news domain. A syntactic annotation of the source sentence could support the attentional encoder-decoder in learning which words in the German source to attend (and translate) first.
> 
> We will investigate the usefulness of linguistic

#### Relevance 921

Label: 1
> Reason
> - Summary of question: Which morphological features are considered?
> - Summary of passage: Examples motivate lemma, POS and syntactic annotations.
> - Judgement: The lemmatization discussion links linguistic inputs to inflectional variation.
> 原因
> - 问题概述：研究考虑哪些形态特征？
> - Passage 概述：示例说明词元、词性和句法标注的动机。
> - 判断：词元化讨论将语言学输入与屈折变化联系起来。

## Question 0102

Paper: Active Learning for Speech Recognition: the Power of Gradients

> How much data samples do they start with before obtaining the initial model labels?

### Common Retrieved Chunks

#### Passage 922

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> State-of-the-art automatic speech recognition (ASR) systems BIBREF0 have large model capacities and require significant quantities of training data to generalize. Labeling thousands of hours of audio, however, is expensive and time-consuming. A natural question to ask is how to achieve better generalization with fewer training examples. Active learning studies this problem by identifying and labeling only the most informative data, potentially reducing sample complexity. How much active learning can help in large-scale, end-to-end ASR systems, however, is still an open question.
> 
> The speech recognition community has generally identified the informativeness of samples by calculating confidence scores. In particular, an utterance is considered informative if the most likely prediction has small probability BIBREF1 , or if the predictions are distributed very uniformly over the labels BIBREF2 . Though confidence-based measures work well in practice, less attention has been focused on gradient-based methods like Expected Gradient Length (EGL) BIBREF3 , where the informativeness is measured by the norm of the gradient incurred by the instance. EGL has previously been justified as intuitively measuring the expected change in a model's parameters BIBREF3 .We formalize this intuition from the perspective of asymptotic variance reduction, and experimentally, we show EGL to be superior to confidence-based methods on speech recognition tasks. Additionally, we observe that the ranking of samples scored by EGL is not correlated with that of confidence scoring, suggesting EGL identifies aspects of an instance that confidence scores cannot capture.
> 
> In BIBREF3 , EGL was applied to active learning on sequence labeling tasks, but our work is the first we know of to apply EGL to speech recognition in particular. Gradient-based methods have also found applications outside active learning. For example, BIBREF4 suggests that in stochastic gradient descent, sampling training instances with probabilities proportional to their gradient lengths can speed up convergence. From the perspective of variance reduction, this importance sampling problem shares many similarities to problems found in active learning.

#### Relevance 922

Label: 1
> Reason
> - Summary of question: How many samples train the initial model?
> - Summary of passage: EGL active learning is motivated and compared with confidence scoring.
> - Judgement: The labeled-data cost and active-learning motivation provide context for the starting labeled sample and later acquisition.
> 原因
> - 问题概述：初始模型使用多少训练样本？
> - Passage 概述：介绍 EGL 主动学习动机并与置信度方法比较。
> - 判断：标注成本与主动学习动机为初始标注样本及后续数据获取提供背景。

#### Passage 924

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Assume the joint distribution of INLINEFORM0 has the following form, DISPLAYFORM0
> 
> where INLINEFORM0 is the true parameter, and INLINEFORM1 is independent of INLINEFORM2 . By selecting a subset of the training data, we are essentially choosing another distribution INLINEFORM3 so that the INLINEFORM4 pairs are drawn from INLINEFORM5
> 
> Statistical signal processing theory BIBREF5 states the following asymptotic distribution of INLINEFORM0 , DISPLAYFORM0
> 
> where INLINEFORM0 is the Fisher Information Matrix with respect to INLINEFORM1 . Using first order approximation at INLINEFORM2 , we have asymptotically, DISPLAYFORM0
> 
> Eq. ( EQREF7 ) indicates that to reduce INLINEFORM0 on test data, we need to minimize the expected variance INLINEFORM1 over the test set. This is called Fisher Information Ratio criteria in BIBREF6 , which itself is hard to optimize. An easier surrogate is to maximize INLINEFORM2 . Substituting Eq. ( EQREF5 ) into INLINEFORM3 , we have INLINEFORM4
> 
> which is equivalent to INLINEFORM0
> 
> A practical issue is that we do not know INLINEFORM0 in advance. We could instead substitute an estimate INLINEFORM1 from a pre-trained model, where it is reasonable to assume the INLINEFORM2 to be close to the true INLINEFORM3 . The batch selection then works by taking the samples that have largest gradient norms, DISPLAYFORM0
> 
> For RNNs, the gradients for each potential label can be obtained by back-propagation. Another practical issue is that EGL marginalizes over all possible labelings, but in speech recognition, the number of labelings scales exponentially in the number of timesteps. Therefore, we only marginalize over the INLINEFORM0 most probable labelings. They are obtained by beam search decoding, as in BIBREF7 . The EGL method in BIBREF3 is almost the same as Eq. ( EQREF8 ), except the gradient's norm is not squared in BIBREF3 .
> 
> Here we have provided a more formal characterization of EGL to complement its intuitive interpretation as “expected model change” in BIBREF3 . For notational convenience, we denote Eq. ( EQREF8 ) as EGL in subsequent sections.

#### Relevance 924

Label: 1
> Reason
> - Summary of question: How many samples train the initial model?
> - Summary of passage: EGL is derived using variance reduction and a pretrained model.
> - Judgement: The pretrained-model assumption and training-subset formulation clarify the setup preceding additional label acquisition.
> 原因
> - 问题概述：初始模型使用多少训练样本？
> - Passage 概述：通过方差降低和预训练模型推导 EGL。
> - 判断：预训练模型假设和训练子集表述说明追加标签前的设置。

#### Passage 925

Retrieved by: BM25, Dense, Hybrid RRF

> We formally explained EGL from a variance reduction perspective and experimentally tested its performance on end-to-end speech recognition systems. Initial experiments show a notable gain over random selection, and that it outperforms confidence score methods used in the ASR community. We also show EGL measures sample informativeness in a very different way from confidence scores, giving rise to open research questions. All the experiments reported here query all samples in a single batch. It is also worth considering the effects of querying samples in a sequential manner. In the future, we will further validate the approach with sequential queries and seek to make the informativeness measure robust to outliers.

#### Relevance 925

Label: 1
> Reason
> - Summary of question: How many samples train the initial model?
> - Summary of passage: The conclusion summarizes EGL gains and future sequential querying.
> - Judgement: The single-batch querying setup helps distinguish the initial model stage from subsequent data acquisition.
> 原因
> - 问题概述：初始模型使用多少训练样本？
> - Passage 概述：结论概述 EGL 收益及未来顺序查询计划。
> - 判断：单批查询设置有助于区分初始模型阶段与后续数据获取。

#### Passage 926

Retrieved by: BM25, Dense, Hybrid RRF

> Confidence scoring has been used extensively as a proxy for the informativeness of training samples. Specifically, an INLINEFORM0 is considered informative if the predictions are uniformly distributed over all the labels BIBREF2 , or if the best prediction of its label is with low probability BIBREF1 . By taking the instances which “confuse” the model, these methods may effectively explore under-sampled regions of the input space.

#### Relevance 926

Label: 1
> Reason
> - Summary of question: How many samples train the initial model?
> - Summary of passage: Confidence methods select uncertain predictions.
> - Judgement: Confidence-based querying describes how additional samples are selected after the starting model exists.
> 原因
> - 问题概述：初始模型使用多少训练样本？
> - Passage 概述：置信度方法选择预测不确定的样本。
> - 判断：基于置信度的查询说明在已有初始模型后如何选择追加样本。

#### Passage 927

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Denote INLINEFORM0 as an utterance and INLINEFORM1 the corresponding label (transcription). A speech recognition system models the conditional distribution INLINEFORM2 , where INLINEFORM3 are the parameters in the model, and INLINEFORM4 is typically implemented by a Recurrent Neural Network (RNN). A training set is a collection of INLINEFORM5 pairs, denoted as INLINEFORM6 . The parameters of the model are estimated by minimizing the negative log-likelihood on the training set: DISPLAYFORM0
> 
> Active learning seeks to augment the training set with a new set of utterances and labels INLINEFORM0 in order to achieve good generalization on a held-out test dataset. In many applications, there is an unlabeled pool INLINEFORM1 which is costly to label in its entirety. INLINEFORM2 is queried for the “most informative” instance(s) INLINEFORM3 , for which the label(s) INLINEFORM4 are then obtained. We discuss several such query strategies below.

#### Relevance 927

Label: 1
> Reason
> - Summary of question: How many samples train the initial model?
> - Summary of passage: Active learning augments a labeled set from an unlabeled pool.
> - Judgement: It explains the initial labeled-set and subsequent unlabeled-pool setup, supporting interpretation of the requested starting size.
> 原因
> - 问题概述：初始模型使用多少训练样本？
> - Passage 概述：主动学习从未标注池扩充已标注集。
> - 判断：它说明初始已标注集与后续未标注池的关系，有助于理解所问初始规模。

### BM25

#### Passage 923

Retrieved by: BM25

> It is useful to understand how the three active learning methods differ in measuring the informativeness of an instance. To compare any two methods, we take rankings of informativeness given by these two methods, and plot them in a 2-D ranking-vs-ranking coordinate system. A plot close to the diagonal implies that these two methods evaluate informativeness in a very similar way.
> 
> Fig. FIGREF11 shows the ranking-vs-ranking plots between pCTC and entropy, EGL and entropy. We observe that pCTC rankings and entropy rankings (Fig. FIGREF11 ) are very correlated. This is likely because they are both related to model uncertainty. In contrast, EGL gives very different rankings from entropy (Fig. FIGREF11 ). This suggests EGL is able to identify aspects of an instance that uncertainty-based measurements cannot capture.
> 
> We further investigate the samples for which EGL and entropy yield vastly different estimates of informativeness, e.g., the elements in the red circle in Fig. FIGREF11 . These particular samples consist of short utterances containing silence (with background noise) or filler words. Further investigation is required to understand whether these samples are noisy outliers or whether they are in fact important for training end-to-end speech recognition systems.

#### Relevance 923

Label: 1
> Reason
> - Summary of question: How many samples train the initial model?
> - Summary of passage: Ranking comparisons show EGL selects different utterances from entropy.
> - Judgement: The queried-utterance analysis explains the sample selection stage following the initial labeled set.
> 原因
> - 问题概述：初始模型使用多少训练样本？
> - Passage 概述：排序比较表明 EGL 与熵方法选择不同语音样本。
> - 判断：查询话语分析说明初始标注集之后的样本选择阶段。

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 928

Retrieved by: Hybrid RRF followed by BGE reranking

> We empirically validate EGL on speech recognition tasks. In our experiments, the RNN takes in spectrograms of utterances, passing them through two 2D-convolutional layers, followed by seven bi-directional recurrent layers and a fully-connected layer with softmax activation. All recurrent layers are batch normalized. At each timestep, the softmax activations give a probability distribution over the characters. CTC loss BIBREF8 is then computed from the timestep-wise probabilities.
> 
> A base model, INLINEFORM0 , is trained on 190 hours ( INLINEFORM1 100K instances) of transcribed speech data. Then, it selects a subset of a 1,700-hour ( INLINEFORM2 1.1M instances) unlabeled dataset. We query labels for the selected subset and incorporate them into training. Learning rates are tuned on a small validation set of 2048 instances. The trained model is then tested on a 156-hour ( INLINEFORM3 100K instances) test set and we report CTC loss, Character Error Rate (CER) and Word Error Rate (WER).
> 
> The confidence score methods BIBREF1 , BIBREF2 can be easily extended to our setup. Specifically, from the probabilities over the characters, we can compute an entropy per timestep and then average them. This method is denoted as entropy. We could also take the most likely prediction and calculate its CTC loss, normalized by number of timesteps. This method is denoted as pCTC (predicted CTC) in the following sections.
> 
> We implement EGL by marginalizing over the most likely 100 labels, and compare it with: 1) a random selection baseline, 2) entropy, and 3) pCTC. Using the same base model, each method queries a variable percentage of the unlabeled dataset. The queries are then included into training set, and the model continues training until convergence. Fig. FIGREF9 reports the metrics (Exact values are reported in Table TABREF12 in the Appendix) on the test set as the query percentage varies. All the active learning methods outperform the random baseline. Moreover, EGL shows a steeper, more rapid reduction in error than all other approaches. Specifically, when querying 20% of the unlabeled dataset, EGL has 11.58% lower CER and 11.09% lower WER relative to random. The performance of EGL at querying 20% is on par with random at 40%, suggesting that using EGL can lead to an approximate 50%

#### Relevance 928

Label: 1
> Reason
> - Summary of question: How many samples train the initial model?
> - Summary of passage: The base model uses 190 hours of transcribed speech, about 100K instances.
> - Judgement: It directly states the labeled data size used before querying additional labels.
> 原因
> - 问题概述：初始模型使用多少训练样本？
> - Passage 概述：基础模型使用 190 小时转写语音，约 10 万个样本。
> - 判断：它直接给出查询更多标签前的初始已标注数据规模。

#### Passage 929

Retrieved by: Hybrid RRF followed by BGE reranking

> of the unlabeled dataset, EGL has 11.58% lower CER and 11.09% lower WER relative to random. The performance of EGL at querying 20% is on par with random at 40%, suggesting that using EGL can lead to an approximate 50% decrease in data labeling.

#### Relevance 929

Label: 1
> Reason
> - Summary of question: How many samples train the initial model?
> - Summary of passage: EGL at 20% querying matches random selection at 40%.
> - Judgement: Query percentages quantify subsequent labeling demand and help contextualize the initial data budget.
> 原因
> - 问题概述：初始模型使用多少训练样本？
> - Passage 概述：EGL 查询 20% 数据达到随机选择 40% 的效果。
> - 判断：查询百分比量化后续标注需求，有助于理解初始数据预算。

## Question 0103

Paper: Iterative Policy Learning in End-to-End Trainable Task-Oriented Neural Dialog Models

> Which neural network architecture do they use for the dialog agent and user simulator?

### Common Retrieved Chunks

#### Passage 930

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> RL policy optimization is performed on top of the supervised pre-trained networks. The system architecture is shown in Figure FIGREF10 . We defines the state, action, and reward in our RL training setting and present the training details.
> 
> State For RL policy learning, states of the dialog agent and the user simulator at the INLINEFORM0 th turn are the dialog-level LSTM state INLINEFORM1 and INLINEFORM2 respectively. Both INLINEFORM3 and INLINEFORM4 captures the dialog history up till current turn. The user state INLINEFORM5 also encodes the user's goal.
> 
> Action Actions of the dialog agent and user simulator are the system action outputs INLINEFORM0 and INLINEFORM1 . An action is sampled by the agent based on a stochastic representation of the policy, which produces a probability distribution over actions given a dialog state. Action space is finite and discrete for both the dialog agent and the user simulator.
> 
> Reward Reward is calculated based on the level of task completion. A turn level reward INLINEFORM0 is applied based on the progress that the agent and user made in completing the predefined task over the past turn. At the end of each turn, a score INLINEFORM1 is calculated indicating to what extend the agent has fulfilled the user's request so far. The turn level reward INLINEFORM2 is then calculated by the difference of the scores received in two consecutive turns: DISPLAYFORM0
> 
> where INLINEFORM0 is the scoring function. INLINEFORM1 and INLINEFORM2 are the true user's goal and the agent's estimation of the user's goal, both are represented by slot-value pairs. Alternatively, the turn level reward INLINEFORM3 can be obtained by using the discounted reward received at the end of the dialog (positive reward for task success, and negative reward for task failure).
> 
> Policy Gradient RL For policy optimization with RL, policy gradient method is preferred over Q-learning in our system as the policy network parameters can be initialized with the INLINEFORM0 parameters learnied during supervised pre-training stage. With REINFORCE BIBREF39 , the objective function can be written as INLINEFORM1 , with INLINEFORM2 being the discount factor. We optimize parameter sets INLINEFORM3 and INLINEFORM4 for the dialog agent and the user simulator to maximize INLINEFORM5 . For the dialog agent, with

#### Relevance 930

Label: 1
> Reason
> - Summary of question: Which neural architectures implement the dialog agent and user simulator?
> - Summary of passage: Both agents use dialog-level LSTM states during reinforcement learning.
> - Judgement: It identifies LSTM as an architectural component for both agents.
> 原因
> - 问题概述：对话代理和用户模拟器使用什么神经网络架构？
> - Passage 概述：两个代理在强化学习中均使用对话级 LSTM 状态。
> - 判断：它明确两个代理都使用 LSTM，提供架构信息。

#### Passage 932

Retrieved by: BM25, Hybrid RRF

> Popular approaches for developing task-oriented dialog systems include treating the problem as a partially observable Markov Decision Process (POMDP) BIBREF6 . RL methods BIBREF23 can be applied to optimize the dialog policy online with the feedback collected via interacting with users. In order to make the RL policy learning tractable, dialog state and system actions have to be carefully designed.
> 
> Recently, people have proposed neural network based methods for task-oriented dialogs, motivated by their superior performance in modeling chit-chat type of conversations BIBREF24 , BIBREF1 , BIBREF2 , BIBREF25 . Bordes and Weston BIBREF26 proposed modeling task-oriented dialogs with a reasoning approach using end-to-end memory networks. Their model skips the belief tracking stage and selects the final system response directly from a list of response candidates. Comparing to this approach, our model explicitly tracks dialog belief state over the sequence of turns, as robust dialog state tracking has been shown BIBREF27 to boost the success rate in task completion. Wen et al. BIBREF16 proposed an end-to-end trainable neural network model with modularity connected system components. This system is trained in supervised manner, and thus may not be robust enough to handle diverse dialog situations due to the limited varieties in dialog corpus. Our system is trained by a combination of SL and deep RL methods, as it is shown that RL training may effectively improved the system robustness and dialog success rate BIBREF28 , BIBREF19 , BIBREF29 . Moreover, other than having separated dialog components as in BIBREF16 , we use a unified network for belief tracking, knowledge base (KB) operation, and dialog management, to fully explore the knowledge that can be shared among different tasks.
> 
> In many of the recent work on using RL for dialog policy learning BIBREF18 , BIBREF30 , BIBREF19 , hand-designed user simulators are used to interact with the dialog agent. Designing a good performing user simulator is not easy. A too basic user simulator as in BIBREF18 may only be able to produce short and simple utterances with limited variety, making the final system lack of robustness against noise in real world user inputs. Advanced user simulators BIBREF31 , BIBREF22 may demonstrate coherent user behavior, but they typically require

#### Relevance 932

Label: 1
> Reason
> - Summary of question: Which neural architectures implement the dialog agent and user simulator?
> - Summary of passage: The agent unifies belief tracking, KB operations and dialog management in one network.
> - Judgement: This supplies partial architectural evidence, although the recurrent cell type is not specified.
> 原因
> - 问题概述：对话代理和用户模拟器使用什么神经网络架构？
> - Passage 概述：代理用统一网络完成信念跟踪、知识库操作和对话管理。
> - 判断：它提供部分架构证据，尽管未说明循环单元类型。

#### Passage 933

Retrieved by: BM25, Dense, Hybrid RRF

> be able to produce short and simple utterances with limited variety, making the final system lack of robustness against noise in real world user inputs. Advanced user simulators BIBREF31 , BIBREF22 may demonstrate coherent user behavior, but they typically require designing complex rules with domain expertise. We address this challenge using a hybrid learning method, where we firstly bootstrapping a basic functioning user simulator with SL on human annotated corpora, and continuously improving it together with the dialog agent during dialog simulations with deep RL.
> 
> Jointly optimizing policies for dialog agent and user simulator with RL has also been studied in literature. Chandramohan et al. BIBREF32 proposed a co-adaptation framework for dialog systems by jointly optimizing the policies for multiple agents. Georgila et al. BIBREF33 discussed applying multi-agent RL for policy learning in a resource allocation negotiation scenario. Barlier et al. BIBREF34 modeled non-cooperative task dialog as a stochastic game and learned jointly the strategies of both agents. Comparing to these previous work, our proposed framework focuses on task-oriented dialogs where the user and the agent positively collaborate to achieve the user's goal. More importantly, we work towards building end-to-end models for task-oriented dialogs that can handle noises and ambiguities in natural language understanding and belief tracking, which is not taken into account in previous work.

#### Relevance 933

Label: 1
> Reason
> - Summary of question: Which neural architectures implement the dialog agent and user simulator?
> - Summary of passage: Supervised initialization and joint reinforcement learning improve both agents.
> - Judgement: It explains how both end-to-end agents are built and trained together, providing supporting model context.
> 原因
> - 问题概述：对话代理和用户模拟器使用什么神经网络架构？
> - Passage 概述：监督初始化和联合强化学习改进两个代理。
> - 判断：它说明两个端到端代理的构建和联合训练方式，提供模型背景线索。

#### Passage 934

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> , the objective function can be written as INLINEFORM1 , with INLINEFORM2 being the discount factor. We optimize parameter sets INLINEFORM3 and INLINEFORM4 for the dialog agent and the user simulator to maximize INLINEFORM5 . For the dialog agent, with likelihood ratio gradient estimator, gradient of INLINEFORM6 can be derived as: DISPLAYFORM0
> 
> This last expression above gives us an unbiased gradient estimator. We sample agent action and user action at each dialog turn and compute the policy gradient. Similarly, gradient on the user simulator side can be derived as: DISPLAYFORM0
> 
> A potential drawback of using REINFORCE is that the policy gradient might have high variance, since the agent may take many steps over the course of a dialog episode. We also explore using Advantage Actor-Critic (A2C) in our study, in which we approximate a state-value function using a feed forward neural network.
> 
> During model training, we use softmax policy for both the dialog agent and the user simulator to encourage exploration. Softmax policy samples action from the action probability distribution calculated by the INLINEFORM0 in the system action output. During evaluation, we apply greedy policy to the dialog agent, and still apply softmax policy to the user simulator. This is to increase randomness and diversity in the user simulator behavior, which is closer to the realistic dialog system evaluation settings with human users. This also prevents the two agents from fully cooperating with each other and exploiting the game.

#### Relevance 934

Label: 1
> Reason
> - Summary of question: Which neural architectures implement the dialog agent and user simulator?
> - Summary of passage: Policy gradients, A2C value estimation and action sampling are described.
> - Judgement: The feedforward value network and action-output policies provide partial network-design information.
> 原因
> - 问题概述：对话代理和用户模拟器使用什么神经网络架构？
> - Passage 概述：介绍策略梯度、A2C 价值估计和动作采样。
> - 判断：前馈价值网络和动作输出策略提供部分网络设计信息。

#### Passage 935

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> of dialog policy learning. Designing a reliable user simulator, however, is not trivial, often as difficult as building a good dialog agent. User simulators used in most of the recent RL based dialog models BIBREF18 , BIBREF22 , BIBREF19 are designed with expert knowledge and complex rules.
> 
> To address the challenge of lacking a reliable user simulator for dialog agent policy learning, we propose a method in jointly optimizing the dialog agent policy and the user simulator policy with deep RL. We first bootstrap a basic neural dialog agent and a basic neural user simulator by learning directly from dialog corpora with supervised training. We then improve them further by simulating task-oriented dialogs between the two agents and iteratively optimizing their dialog policies with deep RL. The intuition is that we model task-oriented dialog as a goal fulfilling task, in which we let the dialog agent and the user simulator to positively collaborate to achieve the goal. The user simulator is given a goal to complete, and it is expected to demonstrate coherent but diverse user behavior. The dialog agent attempts to estimate the user's goal and fulfill his request by conducting meaningful conversations. Both the two agents aim to learn to collaborate with each other to complete the task but without exploiting the game.
> 
> Our contribution in this work is two-fold. Firstly, we propose an iterative dialog policy learning method that jointly optimizes the dialog agent and the user simulator in end-to-end trainable neural dialog systems. Secondly, we design a novel neural network based user simulator for task-oriented dialogs that can be trained in a data-driven manner without requiring the design of complex rules.
> 
> The remainder of the paper is organized as follows. In section 2, we discuss related work on end-to-end trainable task-oriented dialog systems and RL policy learning methods. In section 3, we describe the proposed framework and learning methods in detail. In Section 4, we discuss the experiment setup and analyze the results. Section 5 gives the conclusions.

#### Relevance 935

Label: 1
> Reason
> - Summary of question: Which neural architectures implement the dialog agent and user simulator?
> - Summary of passage: A jointly optimized neural agent and user simulator are proposed.
> - Judgement: It identifies both agents as learned neural models rather than hand-designed rule systems.
> 原因
> - 问题概述：对话代理和用户模拟器使用什么神经网络架构？
> - Passage 概述：提出联合优化神经对话代理和用户模拟器。
> - 判断：它说明两个代理均为学习得到的神经模型，可辅助确定模型设计。

#### Passage 936

Retrieved by: Dense, Hybrid RRF

> In this work, we propose a reinforcement learning framework for dialog policy optimization in end-to-end task-oriented dialog systems. The proposed method addresses the challenge of lacking a reliable user simulator for policy learning in task-oriented dialog systems. We present an iterative policy learning method that jointly optimizes the dialog agent and the user simulator with deep RL by simulating dialogs between the two agents. Both the dialog agent and the user simulator are designed with neural network models that can be trained end-to-end. Experiment results show that our proposed method leads to promising improvements on task success rate and task reward over the supervised training and single-agent RL training baseline models.

#### Relevance 936

Label: 1
> Reason
> - Summary of question: Which neural architectures implement the dialog agent and user simulator?
> - Summary of passage: End-to-end neural agents improve task success through iterative learning.
> - Judgement: It establishes that both agents use end-to-end trainable neural networks, a partial architectural description.
> 原因
> - 问题概述：对话代理和用户模拟器使用什么神经网络架构？
> - Passage 概述：端到端神经代理通过迭代学习提高任务成功率。
> - 判断：它说明两个代理均使用可端到端训练的神经网络，提供部分架构描述。

#### Passage 937

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> In supervised pre-training, the dialog agent and the user simulator are trained separately against dialog corpus. We use the same set of neural network model configurations for both agents. Hidden layer sizes of the dialog-level LSTM for dialog modeling and utterance-level LSTM for utterance encoding are both set as 150. We perform mini-batch training using Adam optimization method BIBREF41 . Initial learning rate is set as 1e-3. Dropout BIBREF42 ( INLINEFORM0 ) is applied during model training to prevent to model from over-fitting.
> 
> In deep RL training stage, the policy network parameters are initialized with INLINEFORM0 parameters from the SL training. State-value function network parameters in A2C are initialized randomly. To ameliorate the non-stationarity problem when jointly training the two agents, we update the two agents iteratively during RL training. We take 100 episodes as a RL training cycle, in which we fix one agent and only update the other, and switch the training agent in the next cycle until convergence. In dialog simulation, we end the dialog if the dialog length exceeds the maximum turn size (20 in our experiment) or the user simulator emits the end of dialog action.

#### Relevance 937

Label: 1
> Reason
> - Summary of question: Which neural architectures implement the dialog agent and user simulator?
> - Summary of passage: Both agents use utterance-level and dialog-level LSTMs with hidden size 150.
> - Judgement: It explicitly specifies the shared recurrent architecture and dimensions.
> 原因
> - 问题概述：对话代理和用户模拟器使用什么神经网络架构？
> - Passage 概述：两个代理均使用隐藏层大小为 150 的话语级和对话级 LSTM。
> - 判断：它明确给出双方共用的循环网络架构及维度。

### BM25

#### Passage 931

Retrieved by: BM25

> Figure 2 shows the design of the user simulator. User simulator is given a randomly sampled goal at the beginning of the conversation. Similar to the design of the dialog agent, state of the user simulator is maintained in the state of an LSTM. At the INLINEFORM0 th turn of a dialog, the user simulator takes in (1) the goal encoding INLINEFORM1 , (2) the previous user output encoding INLINEFORM2 , (3) the current turn agent input encoding INLINEFORM3 , and updates its internal state conditioning on the previous user state INLINEFORM4 . On the output side, the user simulator firstly emits a user action INLINEFORM5 based on the updated state INLINEFORM6 . Conditioning on this emitted user action and the user dialog state INLINEFORM7 , a set of slot values are emitted. The user action and slot values are then passed to an NLG module to generate the final user utterance.
> 
> User Goal We define a user's goal INLINEFORM0 using a list of informable and requestable slots BIBREF38 . Informable slots are the slots that users can provide a value for to describe their goal (e.g. slots for food type, area, etc.). Requestable slots are the slots that users want to request the value for, such as requesting the address of a restaurant. We treat informable slots as discrete type of inputs that can take multiple values, and treat requestable slots as inputs that take binary values (i.e. a slot is either requested or not). In this work, once the a goal is sampled at the beginning of the conversation, we fix the user goal and do not change it during the conversation.
> 
> Action Selection Similar to the action modeling in dialog agent, we treat user action modeling as a multi-class classification problem conditioning on the dialog context encoded in the dialog-level LSTM state INLINEFORM0 on the user simulator side: DISPLAYFORM0
> 
> Once user action is generated at turn INLINEFORM0 , it is used together with the current user dialog state INLINEFORM1 to generate value for each informable slot: DISPLAYFORM0
> 
> Similar to the design of the dialog agent, INLINEFORM0 and INLINEFORM1 are MLPs with a single hidden layer and use INLINEFORM2 activation over their corresponding

#### Relevance 931

Label: 1
> Reason
> - Summary of question: Which neural architectures implement the dialog agent and user simulator?
> - Summary of passage: The simulator maintains an LSTM state and predicts actions and slots with MLPs.
> - Judgement: It directly describes the simulator architecture and relates it to the dialog agent.
> 原因
> - 问题概述：对话代理和用户模拟器使用什么神经网络架构？
> - Passage 概述：模拟器使用 LSTM 维护状态，并用 MLP 预测动作和槽值。
> - 判断：它直接描述模拟器架构，并说明与对话代理的对应关系。

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 938

Retrieved by: Hybrid RRF followed by BGE reranking

> with the current user dialog state INLINEFORM1 to generate value for each informable slot: DISPLAYFORM0
> 
> Similar to the design of the dialog agent, INLINEFORM0 and INLINEFORM1 are MLPs with a single hidden layer and use INLINEFORM2 activation over their corresponding outputs.
> 
> Utterance Generation We use a template-based NLG module to convert the user simulator's outputs (action and slot values) to the natural language surface form.

#### Relevance 938

Label: 1
> Reason
> - Summary of question: Which neural architectures implement the dialog agent and user simulator?
> - Summary of passage: Single-hidden-layer MLPs predict outputs, followed by template-based NLG.
> - Judgement: It identifies output-network components used by the simulator and dialog agent.
> 原因
> - 问题概述：对话代理和用户模拟器使用什么神经网络架构？
> - Passage 概述：单隐藏层 MLP 预测输出，再使用模板生成语言。
> - 判断：它说明模拟器和对话代理使用的输出网络组件。

## Question 0104

Paper: Learning Concept Embeddings for Efficient Bag-of-Concepts Densification

> What is the benchmark dataset?

### Common Retrieved Chunks

#### Passage 939

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We evaluate the "goodness" of our concept embeddings on measuring entity semantic relatedness as an intrinsic evaluation. Entity relatedness has been recently used to model entity coherence in many named entity disambiguation systems.
> 
> We use a benchmark dataset created by ceccarelli2013learning from the CoNLL 2003 data. As in previous studies BIBREF16 , BIBREF15 , we model measuring entity relatedness as a ranking problem. We use the test split of the dataset to create 3,314 queries. Each query has a query entity and INLINEFORM0 91 response entities labeled as related or unrelated. The quality is measured by the ability of the system to rank related entities on top of unrelated ones.
> 
> We compare our models with two prior methods:
> 
> yamada2016joint who used the skip-gram model to learn embeddings of words and entities jointly. The authors also utilized Wikipedia link graph to better model entity-entity relatedness.
> 
> witten2008effective who proposed Wikipedia Link-based Measure (WLM) as a simple mechanism for modeling the semantic relatedness between Wikipedia concepts. The authors utilized Wikipedia link structure under the assumption that related concepts would have similar incoming links.
> 
> We report Mean Average Precision (MAP) and Normalized Discounted Cumulative Gain (nDCG) scores as commonly used measures for evaluating the ranking quality. Table 1 shows the performance of our CRC and 3C models compared to previous models. As we can see, the 3C model performs poorly on this task compared to prior models. On the other hand, our CRC model outperforms all the other methods by 2-4% in terms of nDCG and by 3% percent in terms of MAP.

#### Relevance 939

Label: 1
> Reason
> - Summary of question: Which benchmark dataset is used?
> - Summary of passage: Entity relatedness uses a benchmark derived from CoNLL 2003.
> - Judgement: It directly identifies the intrinsic evaluation dataset.
> 原因
> - 问题概述：使用哪个基准数据集？
> - Passage 概述：实体相关性使用源自 CoNLL 2003 的基准。
> - 判断：它直接指出内部评估所用的数据集。

#### Passage 940

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> chang2008importance proposed dataless classification as a learning protocol to perform text categorization without the need for labeled data to train a classifier. Given only label names and few descriptive keywords of each label, classification is performed on the fly by mapping each label into a BOC representation using ESA. Likewise, each data instance is mapped into the same BOC semantic space and assigned to the most similar label using a proper similarity measure such as cosine. Formally, given a set of INLINEFORM0 labels INLINEFORM1 , a text document INLINEFORM2 , a BOC mapping model INLINEFORM3 , and a similarity function INLINEFORM4 , then INLINEFORM5 is assigned to the INLINEFORM6 th label INLINEFORM7 such that INLINEFORM8 . We evaluate the effectiveness of our concept embedding models on the dataless classification task as an extrinsic evaluation. We demonstrate through empirical results the efficiency and effectiveness of our proposed BOC densification scheme in obtaining better classification results compared to the original sparse BOC representation.
> 
> We use the 20 Newsgroups dataset (20NG) BIBREF17 which is commonly used for benchmarking text classification algorithms. The dataset contains 20 categories each has INLINEFORM0 1000 news posts. We obtained the BOC representations using ESA from song2014dataless who utilized a Wikipedia index containing pages with 100+ words and 5+ outgoing links to create ESA mappings of 500 dimensions for both the categories and news posts of the 20NG. We designed two types of classification tasks: 1) fine-grained classification involving closely related classes such as Hockey vs. Baseball, Autos vs. Motorcycles, and Guns vs. Mideast vs. Misc, and 2) coarse-grained classification involving top-level categories such as Sport vs. Politics and Sport vs. Religion. The top-level categories are created by combining instances of the fine-grained categories as shown in Table 2.
> 
> We compare our models with three prior methods:
> 
> ESA which computes the cosine similarity using the sparse BOC vectors.
> 
> WE INLINEFORM0 & WE INLINEFORM1 which were proposed by songunsupervised for BOC densification using embeddings obtained from Word2Vec. As the authors reported, we fix the minimum similarity threshold to 0.85. WE INLINEFORM2 finds the best match for each concept, while WE INLINEFORM3 utilizes the Hungarian algorithm to find the best concept-concept alignment on one-to-one basis. Both

#### Relevance 940

Label: 1
> Reason
> - Summary of question: Which benchmark dataset is used?
> - Summary of passage: Dataless classification is evaluated on 20 Newsgroups.
> - Judgement: It explicitly names an experimental benchmark dataset.
> 原因
> - 问题概述：使用哪个基准数据集？
> - Passage 概述：无数据分类在 20 Newsgroups 上评估。
> - 判断：它明确给出实验基准数据集名称。

#### Passage 943

Retrieved by: BM25, Hybrid RRF

> In addition, compared to yamada2016joint model, we utilize contexts generated from both surrounding words and concepts. Therefore, we can better capture local contextual information of each target word/concept. Moreover, our proposed models are computationally less costly than hu2015entity and yamada2016joint models as they require few hours rather than days to train on similar computing resources.
> 
> BOC Densification: distributed concept vectors have been used by BOC densification mechanisms to overcome the BOC sparsity problem. songunsupervised proposed three different mechanisms for aligning the concepts at different indices given a sparse BOC pair ( INLINEFORM0 ) in order to increase their similarity score.
> 
> The many-to-many mechanism works by averaging all pairwise similarities. The many-to-one mechanism works by aligning each concept in INLINEFORM0 with the most similar concept in INLINEFORM1 (i.e., its best match). Clearly, the complexity of these two mechanisms is quadratic. The third mechanism is the one-to-one. It utilizes the Hungarian method in order to find an optimal alignment on a one-to-one basis BIBREF13 . This mechanism performed the best on dataless classification and was also utilized by li2016joint. However, the Hungarian method is a combinatorial optimization algorithm whose complexity is polynomial. Our proposed densification mechanism is more efficient than these three mechanisms as its complexity is linear with respect to the number of non-zero elements in the BOC vector. Additionally, it is simpler as it does not require tuning a cut off threshold for the minimum similarity between two aligned concepts as in prior work.

#### Relevance 943

Label: 0
> Reason
> - Summary of question: Which benchmark dataset is used?
> - Summary of passage: Densification methods differ in alignment cost and contextual information.
> - Judgement: No benchmark dataset is identified.
> 原因
> - 问题概述：使用哪个基准数据集？
> - Passage 概述：稠密化方法在对齐成本和上下文信息上存在差异。
> - 判断：它未指出任何基准数据集。

#### Passage 944

Retrieved by: Dense, Hybrid RRF

> Results of coarse-grained classification are presented in Table 4. Classification at the top level is easier than the fine-grained level. Nevertheless, as with fine-grained classification, ESA still peaks with a few hundred dimensions of the sparse BOC vector. Both the CRC & 3C models achieve equal performance to ESA at very few dimensions ( INLINEFORM0 ). Densification using the CRC model embeddings still performs the best on both tasks. Interestingly, the 3C model gives very close F1 scores to the CRC model at less dimensions (@4 with Sport vs. Politics, and @60 with Sport vs. Religion) indicating its competitive advantage when computational cost is a decisive criteria. The 3C model, still performs better than ESA, WE INLINEFORM1 , and WE INLINEFORM2 on both tasks.
> 
> Figure 2 shows F1 scores of coarse-grained classification when varying the # of BOC dimensions used for densification. The same pattern of achieving near-peak performance at very few dimensions recur with the CRC & 3C models. ESA using the sparse BOC vectors achieves low F1 up until few hundred dimensions are considered. Even with the costly WE INLINEFORM0 and WE INLINEFORM1 densifications, performance sometimes decreases.

#### Relevance 944

Label: 1
> Reason
> - Summary of question: Which benchmark dataset is used?
> - Summary of passage: Coarse classification results compare Sport, Politics and Religion categories.
> - Judgement: The named coarse-grained category pairs provide clues to the benchmark's identity and scope.
> 原因
> - 问题概述：使用哪个基准数据集？
> - Passage 概述：粗粒度分类结果比较体育、政治和宗教类别。
> - 判断：具名粗粒度类别组合为基准身份和范围提供线索。

#### Passage 945

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> from Word2Vec. As the authors reported, we fix the minimum similarity threshold to 0.85. WE INLINEFORM2 finds the best match for each concept, while WE INLINEFORM3 utilizes the Hungarian algorithm to find the best concept-concept alignment on one-to-one basis. Both mechanisms have polynomial time complexity.
> 
> Table 3 presents the results of fine-grained dataless classification measured in micro-averaged F1. As we can notice, ESA achieves its peak performance with a few hundred dimensions of the sparse BOC vector. Using our densification mechanism, both the CRC & 3C models achieve equal performance to ESA at much less dimensions. Densification using the CRC model embeddings gives the best F1 scores on the three tasks. Interestingly, the CRC model improves the F1 score by INLINEFORM0 7% using only 14 concepts on Autos vs. Motorcycles, and by INLINEFORM1 3% using 70 concepts on Guns vs. Mideast vs. Misc. The 3C model, still performs better than ESA on 2 out of the 3 tasks. Both WE INLINEFORM2 and WE INLINEFORM3 improve the performance over ESA but not as our CRC model.
> 
> In order to better illustrate the robustness of our densification mechanism when varying the # of BOC dimensions, we measured F1 scores of each task as a function of the # of BOC dimensions used for densification. As we see in Figure 1, with one concept we can achieve high F1 scores compared to ESA which achieves zero or very low F1. Moreover, near-peak performance is achievable with the top 50 or less dimensions. We can also notice that, as we increase the # of dimensions, both WE INLINEFORM0 and WE INLINEFORM1 densification methods have the same undesired monotonic pattern like ESA. Actually, the imposed threshold by these methods does not allow for full dense representation of the BOC vector and therefore at low dimensions we still see low overall F1 score. Our proposed densification mechanisms besides their low cost, produce fully densified representations allowing good similarities at low dimensions.
> 
> Results of coarse-grained classification are presented in Table 4. Classification at the top level is easier than the fine-grained level. Nevertheless, as with fine-grained classification, ESA still peaks with a few hundred dimensions of the sparse BOC vector. Both the

#### Relevance 945

Label: 1
> Reason
> - Summary of question: Which benchmark dataset is used?
> - Summary of passage: Fine-grained classification results compare several category pairs.
> - Judgement: The named fine-grained categories and benchmark comparisons help identify the classification dataset.
> 原因
> - 问题概述：使用哪个基准数据集？
> - Passage 概述：细粒度分类结果比较多个类别组合。
> - 判断：具名细粒度类别及基准比较有助于识别分类数据集。

#### Passage 947

Retrieved by: Hybrid RRF, Hybrid RRF followed by BGE reranking

> Vector-based semantic mapping models are used to represent textual structures (words, phrases, and documents) as high-dimensional meaning vectors. Typically, these models utilize textual corpora and/or Knowledge Bases (KBs) to acquire world knowledge, which is then used to generate a vector representation for the given text in the semantic space. The goal is thus to accurately place semantically similar structures close to each other in that semantic space. On the other hand, dissimilar structures should be far apart.
> 
> Explicit concept space models are motivated by the idea that high level cognitive tasks such learning and reasoning are supported by the knowledge we acquire from concepts BIBREF0 . Therefore, such models utilize concept vectors (a.k.a bag-of-concepts (BOC)) as the underlying semantic representation of a given text through a process called conceptualization, which is mapping the text into relevant concepts capturing its main topics. The concept space typically include concepts obtained from KBs such as Wikipedia, Probase BIBREF1 , and others. Once the concept vectors are generated, similarity between two concept vectors can be computed using a suitable similarity/distance measure such as cosine.
> 
> The BOC representation has proven efficacy for semantic analysis of textual data especially short texts where contextual information is missing or insufficient. For example, measuring semantic similarity/relatedness BIBREF2 , BIBREF3 , BIBREF4 , dataless classification BIBREF5 , BIBREF6 , BIBREF7 , BIBREF8 , short text clustering BIBREF0 , search and relevancy ranking BIBREF9 , event detection and coreference resolution BIBREF10 .
> 
> Similar to the traditional bag-of-words representation, the BOC vector is a high dimensional sparse vector whose dimensionality is the same as the number of concepts in the employed KB (typically millions). Consequently, it suffers from data sparsity causing low similarity scores between similar texts due to low concept overlap. Formally, given a text snippet INLINEFORM0 of INLINEFORM1 terms where INLINEFORM2 , and a concept space INLINEFORM3 of size INLINEFORM4 . The BOC vector INLINEFORM5 = INLINEFORM6 of INLINEFORM7 is a vector of weights of each concept where each INLINEFORM8 of concept INLINEFORM9 is calculated as in equation 1: DISPLAYFORM0
> 
> Here INLINEFORM0 is a scoring function which indicates the degree of association between term INLINEFORM1 and concept INLINEFORM2 . For example, gabrilovich2007computing proposed Explicit Semantic

#### Relevance 947

Label: 0
> Reason
> - Summary of question: Which benchmark dataset is used?
> - Summary of passage: Concept spaces use knowledge bases such as Wikipedia and Probase.
> - Judgement: These are representation resources, not identified experimental benchmarks.
> 原因
> - 问题概述：使用哪个基准数据集？
> - Passage 概述：概念空间使用 Wikipedia 和 Probase 等知识库。
> - 判断：这些是表示所用资源，并未被指明为实验基准。

### BM25

#### Passage 941

Retrieved by: BM25

> A main objective of learning concept embeddings is to overcome the inherent problem of data sparsity associated with the BOC representation. Here we try to learn continuous concept vectors by building upon the skip-gram embedding model BIBREF11 . In the conventional skip-gram model, a set of contexts are generated by sliding a context window of predefined size over sentences of a given text corpus. Vector representation of a target word is learned with the objective to maximize the ability of predicting surrounding words of that target word.
> 
> Formally, given a training corpus of INLINEFORM0 words INLINEFORM1 . The skip-gram model aims to maximize the average log probability: DISPLAYFORM0
> 
> where INLINEFORM0 is the context window size, INLINEFORM1 is the target word, and INLINEFORM2 is a surrounding context word. The softmax function is used to estimate the probability INLINEFORM3 as follows: DISPLAYFORM0
> 
> where INLINEFORM0 and INLINEFORM1 are the input and output vectors respectively and INLINEFORM2 is the vocabulary size. mikolov2013distributed proposed hierarchical softmax and negative sampling as efficient alternatives to approximate the softmax function which becomes computationally intractable when INLINEFORM3 becomes huge.
> 
> Our approach genuinely learns distributed concept representations by generating concept contexts from mentions of those concepts in large encyclopedic KBs such as Wikipedia. Utilizing such annotated KBs eliminates the need to manually annotate concept mentions and thus comes at no cost.

#### Relevance 941

Label: 0
> Reason
> - Summary of question: Which benchmark dataset is used?
> - Summary of passage: Skip-gram learns concept embeddings from encyclopedic contexts.
> - Judgement: Training resources do not identify the evaluation benchmark.
> 原因
> - 问题概述：使用哪个基准数据集？
> - Passage 概述：Skip-gram 从百科上下文学习概念嵌入。
> - 判断：训练资源不能说明评估基准数据集。

#### Passage 942

Retrieved by: BM25

> Inspired by the distributional hypothesis BIBREF14 , we, in this model, hypothesize that "similar concepts tend to appear in similar conceptual contexts". In order to test this hypothesis, we learn concept embeddings by training a skip-gram model on contexts generated solely from concept mentions. As in the CRC model, we start by identifying all concept mentions in the given corpus. Then, contexts are generated from only surrounding concepts. Formally, given a training corpus of INLINEFORM0 words INLINEFORM1 . We iterate over the corpus identifying concept mentions and thus generating a sequence of INLINEFORM2 concept tokens INLINEFORM3 where INLINEFORM4 . Afterwards we train the skip-gram model aiming to maximize: DISPLAYFORM0
> 
> where INLINEFORM0 is the context window size, INLINEFORM1 is the target concept, and INLINEFORM2 is a surrounding concept mention within INLINEFORM3 mentions.
> 
> This model is different from li2016joint and hu2015entity as they define the context of a target concept by all the other concepts which appear in the concept's corresponding article. Clearly, some of these concepts might be irrelevant especially for very long articles which cite hundreds of other concepts. Our 3C model, alternatively, learns concept semantics from surrounding concepts and not only from those that are cited in its article. We also extend the context window beyond pairs of concepts allowing more influence to other nearby concepts.
> 
> The main advantage of the 3C model over the CRC model is its computational efficiency where the model vocabulary is limited to the corpus concepts (Wikipedia in our case). One the other hand, the CRC model is advantageous because it jointly learns the embeddings of words and concepts and is therefore expected to generate higher quality vectors. In other words, the CRC model can capture more contextual signals such as actions, times, and relationships at the expense of training computational cost.

#### Relevance 942

Label: 0
> Reason
> - Summary of question: Which benchmark dataset is used?
> - Summary of passage: The 3C model learns embeddings from neighboring concept mentions.
> - Judgement: It describes training contexts rather than benchmark data.
> 原因
> - 问题概述：使用哪个基准数据集？
> - Passage 概述：3C 模型从相邻概念提及学习嵌入。
> - 判断：它描述训练上下文，未说明基准数据集。

### Dense

#### Passage 946

Retrieved by: Dense

> As we mentioned in the related work section, the current mechanisms for BOC densification are inefficient as their complexity is least quadratic with respect to the number of non-zero elements in the BOC vector. Here, we propose simple and efficient vector aggregation method to obtain fully densified BOC vectors in linear time. Our mechanism works by performing a weighted average of the embedding vectors of all concepts in the given BOC. This operation scales linearly with the number of non-zero dimensions in the BOC vector. In addition, it produces a fully dense vector representing the semantics of the original concepts and considering their weights. Formally, given a sparse BOC vector INLINEFORM0 where INLINEFORM1 is weight of concept INLINEFORM2 . We can obtain the dense representation of INLINEFORM3 as in equation 8: DISPLAYFORM0
> 
> where INLINEFORM0 is the embedding vector of concept INLINEFORM1 . Once we have this dense BOC vector, we can apply the cosine measure to compute the similarity between a pair of dense BOC vectors.
> 
> As we can notice, this weighted average is done once and for all for a given BOC vector. Other mechanisms that rely on concept alignment BIBREF7 , require realignment every time a given BOC vector is compared to another BOC vector. Our approach improves the efficiency especially in the context of dataless classification with large number of classes. Using our densification mechanism, we apply the weighted average for each class vector and for each instance once.
> 
> Interestingly, our densification mechanism allows us to densify the sparse BOC vector using only the top few dimensions. As we will show in the experiments section, we can get (near-)best results using these few dimensions compared to densifying with all the dimensions in the original sparse vector. This property reduces the cost of obtaining a BOC vector with a few hundred dimensions in the first place.

#### Relevance 946

Label: 0
> Reason
> - Summary of question: Which benchmark dataset is used?
> - Summary of passage: Weighted averaging produces dense BOC representations in linear time.
> - Judgement: The densification algorithm does not identify the evaluation dataset.
> 原因
> - 问题概述：使用哪个基准数据集？
> - Passage 概述：加权平均在线性时间内生成稠密 BOC 表示。
> - 判断：稠密化算法未说明评估数据集。

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 948

Retrieved by: Hybrid RRF followed by BGE reranking

> each concept where each INLINEFORM8 of concept INLINEFORM9 is calculated as in equation 1: DISPLAYFORM0
> 
> Here INLINEFORM0 is a scoring function which indicates the degree of association between term INLINEFORM1 and concept INLINEFORM2 . For example, gabrilovich2007computing proposed Explicit Semantic Analysis (ESA) which uses Wikipedia articles as concepts and the TF-IDF score of the terms in these article as the association score. Another scoring function might be the co-occurrence count or Pearson correlation score between INLINEFORM3 and INLINEFORM4 . As we can notice, only very small subset of the concept space would have non-zero scores with the given terms. Moreover, the BOC vector is generated from the INLINEFORM5 concepts which have relatively high association scores with the input terms (typically few hundreds). Thus each text snippet is mapped to a very sparse vector of millions of dimensions having only few hundreds non-zero values BIBREF10 .
> 
> Typically, the cosine similarity measure is used compute the similarity between a pair of BOC vectors INLINEFORM0 and INLINEFORM1 . Because the concept vectors are very sparse, we can rewrite each vector as a vector of tuples INLINEFORM2 . Suppose that INLINEFORM3 and INLINEFORM4 , where INLINEFORM5 and INLINEFORM6 are the corresponding weights of concepts INLINEFORM7 and INLINEFORM8 respectively. And INLINEFORM9 , INLINEFORM10 are the indices of these concepts in the concept space INLINEFORM11 such that INLINEFORM12 . Then, the relatedness score can be written as in equation 2: DISPLAYFORM0
> 
> where INLINEFORM0 is the indicator function which returns 1 if INLINEFORM1 and 0 otherwise. Having such sparse representation and using exact match similarity scoring measure, we can expect that two very similar text snippets might have zero similarity score if they map to different but very related set of concepts BIBREF7 .
> 
> Neural embedding models have been proposed to overcome the BOC sparsity problem. The basic idea is to learn fixed size continuous vectors for each concept. These vectors can then be used to compute concept-concept similarity and thus overcome the concept mismatch problem.
> 
> In this paper we propose two neural embedding models in order to learn continuous concept vectors based on the skip-gram model BIBREF11 . Our first model is the Concept Raw Context model (CRC) which utilizes concept

#### Relevance 948

Label: 0
> Reason
> - Summary of question: Which benchmark dataset is used?
> - Summary of passage: ESA and neural embeddings address sparse concept-vector mismatch.
> - Judgement: It explains representations without specifying benchmark data.
> 原因
> - 问题概述：使用哪个基准数据集？
> - Passage 概述：ESA 和神经嵌入处理稀疏概念向量不匹配。
> - 判断：它解释表示方法，未说明基准数据。

## Question 0105

Paper: Automated News Suggestions for Populating Wikipedia Entity Pages

> What baseline model is used?

### Common Retrieved Chunks

#### Passage 949

Retrieved by: BM25, Dense, Hybrid RRF

> Here we show the evaluation setup for ASP task and discuss the results with a focus on three main aspects, (i) the overall performance across the years, (ii) the entity class specific performance, and (iii) the impact on entity profile expansion by suggesting missing sections to entities based on the pre-computed templates.
> 
> Baselines. To the best of our knowledge, we are not aware of any comparable approach for this task. Therefore, the baselines we consider are the following:
> 
> S1: Pick the section from template INLINEFORM0 with the highest lexical similarity to INLINEFORM1 : S1 INLINEFORM2
> 
> S2: Place the news into the most frequent section in INLINEFORM0
> 
> Learning Models. We use Random Forests (RF) BIBREF23 and Support Vector Machines (SVM) BIBREF24 . The models are optimized taking into account the features in Table TABREF31 . In contrast to the AEP task, here the scale of the number of instances allows us to learn the SVM models. The SVM model is optimized using the INLINEFORM0 loss function and uses the Gaussian kernels.
> 
> Metrics. We compute precision P as the ratio of news for which we pick a section INLINEFORM0 from INLINEFORM1 and INLINEFORM2 conforms to the one in our ground-truth (see Section SECREF40 ). The definition of recall R and F1 score follows from that of precision.
> 
> Figure FIGREF66 shows the overall performance and a comparison of our approach (when INLINEFORM0 is optimized using SVM) against the best performing baseline S2. With the increase in the number of training instances for the ASP task the performance is a monotonically non-decreasing function. For the year 2009, we optimize the learning objective of INLINEFORM1 with around 8% of the total instances, and evaluate on the rest. The performance on average is around P=0.66 across all classes. Even though for many classes the performance is already stable (as we will see in the next section), for some classes we improve further. If we take into account the years between 2010 and 2012, we have an increase of INLINEFORM2 P=0.17, with around 70% of instances used for training and the remainder for evaluation. For the remaining years the total improvement is INLINEFORM3 P=0.18 in contrast to the performance at year 2009.

#### Relevance 949

Label: 1
> Reason
> - Summary of question: Which baseline model is used?
> - Summary of passage: ASP baselines choose the most similar or most frequent template section.
> - Judgement: It directly defines section-placement baselines S1 and S2.
> 原因
> - 问题概述：使用什么基线模型？
> - Passage 概述：ASP 基线选择最相似或最常见的模板章节。
> - 判断：它直接定义章节放置基线 S1 和 S2。

#### Passage 952

Retrieved by: BM25, Dense, Hybrid RRF

> and 2012, we have an increase of INLINEFORM2 P=0.17, with around 70% of instances used for training and the remainder for evaluation. For the remaining years the total improvement is INLINEFORM3 P=0.18 in contrast to the performance at year 2009.
> 
> On the other hand, the baseline S1 has an average precision of P=0.12. The performance across the years varies slightly, with the year 2011 having the highest average precision of P=0.13. Always picking the most frequent section as in S2, as shown in Figure FIGREF66 , results in an average precision of P=0.17, with a uniform distribution across the years.
> 
> Here we show the performance of INLINEFORM0 decomposed for the different entity classes. Specifically we analyze the 27 classes in Figure FIGREF42 . In Table TABREF68 , we show the results for a range of years (we omit showing all years due to space constraints). For illustration purposes only, we group them into four main classes ( INLINEFORM1 Person, Organization, Location, Event INLINEFORM2 ) and into the specific sub-classes shown in the second column in Table TABREF68 . For instance, the entity classes OfficeHolder and Politician are aggregated into Person–Politics.
> 
> It is evident that in the first year the performance is lower in contrast to the later years. This is due to the fact that as we proceed, we can better generalize and accurately determine the correct fit of an article INLINEFORM0 into one of the sections from the pre-computed templates INLINEFORM1 . The results are already stable for the year range INLINEFORM2 . For a few Person sub-classes, e.g. Politics, Entertainment, we achieve an F1 score above 0.9. These additionally represent classes with a sufficient number of training instances for the years INLINEFORM3 . The lowest F1 score is for the Criminal and Television classes. However, this is directly correlated with the insufficient number of instances.
> 
> The baseline approaches for the ASP task perform poorly. S1, based on lexical similarity, has a varying performance for different entity classes. The best performance is achieved for the class Person – Politics, with P=0.43. This highlights the importance of our feature choice and that the ASP cannot be considered as a linear function, where the maximum similarity

#### Relevance 952

Label: 1
> Reason
> - Summary of question: Which baseline model is used?
> - Summary of passage: S1 uses lexical similarity and S2 always chooses the most frequent section.
> - Judgement: It identifies the baseline decision rules while reporting their performance.
> 原因
> - 问题概述：使用什么基线模型？
> - Passage 概述：S1 使用词汇相似度，S2 总是选择最常见章节。
> - 判断：它在报告性能时说明基线的决策规则。

#### Passage 953

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> between the language models INLINEFORM5 and the entity overlap in INLINEFORM6 and INLINEFORM7 .
> 
> Here we introduce the evaluation setup and analyze the results for the article–entity (AEP) placement task. We only report the evaluation metrics for the `relevant' news-entity pairs. A detailed explanation on why we focus on the `relevant' pairs is provided in Section SECREF16 .
> 
> Baselines. We consider the following baselines for this task.
> 
> B1. The first baseline uses only the salience-based features by Dunietz and Gillick BIBREF11 .
> 
> B2. The second baseline assigns the value relevant to a pair INLINEFORM0 , if and only if INLINEFORM1 appears in the title of INLINEFORM2 .
> 
> Learning Models. We use Random Forests (RF) BIBREF23 . We learn the RF on all computed features in Table TABREF21 . The optimization on RF is done by splitting the feature space into multiple trees that are considered as ensemble classifiers. Consequently, for each classifier it computes the margin function as a measure of the average count of predicting the correct class in contrast to any other class. The higher the margin score the more robust the model.
> 
> Metrics. We compute precision P, recall R and F1 score for the relevant class. For example, precision is the number of news-entity pairs we correctly labeled as relevant compared to our ground truth divided by the number of all news-entity pairs we labeled as relevant.
> 
> The following results measure the effectiveness of our approach in three main aspects: (i) overall performance of INLINEFORM0 and comparison to baselines, (ii) robustness across the years, and (iii) optimal model for the AEP placement task.
> 
> Performance. Figure FIGREF55 shows the results for the years 2009 and 2013, where we optimized the learning objective with instances from year INLINEFORM0 and evaluate on the years INLINEFORM1 (see Section SECREF46 ). The results show the precision–recall curve. The red curve shows baseline B1 BIBREF11 , and the blue one shows the performance of INLINEFORM2 . The curve shows for varying confidence scores (high to low) the precision on labeling the pair INLINEFORM3 as `relevant'. In addition, at each confidence score we can compute the corresponding recall for the `relevant' label. For high confidence scores on labeling the

#### Relevance 953

Label: 1
> Reason
> - Summary of question: Which baseline model is used?
> - Summary of passage: AEP baselines use salience features or entity occurrence in the article title.
> - Judgement: It directly defines baselines B1 and B2.
> 原因
> - 问题概述：使用什么基线模型？
> - Passage 概述：AEP 基线使用显著性特征或检查实体是否出现在文章标题。
> - 判断：它直接定义基线 B1 和 B2。

#### Passage 954

Retrieved by: Dense, Hybrid RRF

> shows for varying confidence scores (high to low) the precision on labeling the pair INLINEFORM3 as `relevant'. In addition, at each confidence score we can compute the corresponding recall for the `relevant' label. For high confidence scores on labeling the news-entity pairs, the baseline B1 achieves on average a precision score of P=0.50, while INLINEFORM4 has P=0.93. We note that with the drop in the confidence score the corresponding precision and recall values drop too, and the overall F1 score for B1 is around F1=0.2, in contrast we achieve an average score of F1=0.67.
> 
> It is evident from Figure FIGREF55 that for the years 2009 and 2013, INLINEFORM0 significantly outperforms the baseline B1. We measure the significance through the t-test statistic and get a p-value of INLINEFORM1 . The improvement we achieve over B1 in absolute numbers, INLINEFORM2 P=+0.5 in terms of precision for the years between 2009 and 2014, and a similar improvement in terms of F1 score. The improvement for recall is INLINEFORM3 R=+0.4. The relative improvement over B1 for P and F1 is almost 1.8 times better, while for recall we are 3.5 times better. In Table TABREF58 we show the overall scores for the evaluation metrics for B1 and INLINEFORM4 . Finally, for B2 we achieve much poorer performance, with average scores of P=0.21, R=0.20 and F1=0.21.
> 
> Robustness. In Table TABREF58 , we show the overall performance for the years between 2009 and 2013. An interesting observation we make is that we have a very robust performance and the results are stable across the years. If we consider the experimental setup, where for year INLINEFORM0 we optimize the learning objective with only 74k training instances and evaluate on the rest of the instances, it achieves a very good performance. We predict with F1=0.68 the remaining 469k instances for the years INLINEFORM1 .
> 
> The results are particularly promising considering the fact that the distribution between our two classes is highly skewed. On average the number of `relevant' pairs account for only around INLINEFORM0 of all pairs. A good indicator to support such a statement is the kappa (denoted by INLINEFORM1 ) statistic. INLINEFORM2 measures agreement between the algorithm and the gold standard

#### Relevance 954

Label: 1
> Reason
> - Summary of question: Which baseline model is used?
> - Summary of passage: AEP results compare performance with B1 and B2.
> - Judgement: B1 and B2 identify baseline variants and their reported results, which can be combined with their definitions elsewhere.
> 原因
> - 问题概述：使用什么基线模型？
> - Passage 概述：AEP 结果比较所提方法与 B1、B2 的性能。
> - 判断：B1、B2 编号及结果可与其他片段中的定义结合，辅助确认基线。

#### Passage 955

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> for different entity classes. The best performance is achieved for the class Person – Politics, with P=0.43. This highlights the importance of our feature choice and that the ASP cannot be considered as a linear function, where the maximum similarity yields the best results. For different entity classes different features and combination of features is necessary. Considering that S2 is the overall best performing baseline, through our approach INLINEFORM0 we have a significant improvement of over INLINEFORM1 P=+0.64.
> 
> The models we learn are very robust and obtain high accuracy, fulfilling our pre-condition for accurate news suggestions into the entity sections. We measure the robustness of INLINEFORM0 through the INLINEFORM1 statistic. In this case, we have a model with roughly 10 labels (corresponding to the number of sections in a template INLINEFORM2 ). The score we achieve shows that our model predicts with high confidence with INLINEFORM3 .
> 
> The last analysis is the impact we have on expanding entity profiles INLINEFORM0 with new sections. Figure FIGREF70 shows the ratio of sections for which we correctly suggest an article INLINEFORM1 to the right section in the section template INLINEFORM2 . The ratio here corresponds to sections that are not present in the entity profile at year INLINEFORM3 , that is INLINEFORM4 . However, given the generated templates INLINEFORM5 , we can expand the entity profile INLINEFORM6 with a new section at time INLINEFORM7 . In details, in the absence of a section at time INLINEFORM8 , our model trains well on similar sections from the section template INLINEFORM9 , hence we can predict accurately the section and in this case suggest its addition to the entity profile. With time, it is obvious that the expansion rate decreases at later years as the entity profiles become more `complete'.
> 
> This is particularly interesting for expanding the entity profiles of long-tail entities as well as updating entities with real-world emerging events that are added constantly. In many cases such missing sections are present at one of the entities of the respective entity class INLINEFORM0 . An obvious case is the example taken in Section SECREF16 , where the `Accidents' is rather common for entities of type Airline. However, it is

#### Relevance 955

Label: 1
> Reason
> - Summary of question: Which baseline model is used?
> - Summary of passage: ASP performance exceeds S2 and supports entity-profile expansion.
> - Judgement: It identifies S2 as the strongest ASP baseline, providing a clue to the relevant comparator.
> 原因
> - 问题概述：使用什么基线模型？
> - Passage 概述：ASP 性能超过 S2，并支持实体页面扩充。
> - 判断：它指出 S2 是最强的 ASP 基线，为确认对比方法提供线索。

### BM25

#### Passage 950

Retrieved by: BM25

> In this section we outline the evaluation plan to verify the effectiveness of our learning approaches. To evaluate the news suggestion problem we are faced with two challenges.
> 
> What comprises the ground truth for such a task ?
> 
> How do we construct training and test splits given that entity pages consists of text added at different points in time ?
> 
> Consider the ground truth challenge. Evaluating if an arbitrary news article should be included in Wikipedia is both subjective and difficult for a human if she is not an expert. An invasive approach, which was proposed by Barzilay and Sauper BIBREF8 , adds content directly to Wikipedia and expects the editors or other users to redact irrelevant content over a period of time. The limitations of such an evaluation technique is that content added to long-tail entities might not be evaluated by informed users or editors in the experiment time frame. It is hard to estimate how much time the added content should be left on the entity page. A more non-invasive approach could involve crowdsourcing of entity and news article pairs in an IR style relevance assessment setup. The problem of such an approach is again finding knowledgeable users or experts for long-tail entities. Thus the notion of relevance of a news recommendation is challenging to evaluate in a crowd setup.
> 
> We take a slightly different approach by making an assumption that the news articles already present in Wikipedia entity pages are relevant. To this extent, we extract a dataset comprising of all news articles referenced in entity pages (details in Section SECREF40 ). At the expense of not evaluating the space comprising of news articles absent in Wikipedia, we succeed in (i) avoiding restrictive assumptions about the quality of human judgments, (ii) being invasive and polluting Wikipedia, and (iii) deriving a reusable test bed for quicker experimentation.
> 
> The second challenge of construction of training and test set separation is slightly easier and is addressed in Section SECREF46 .

#### Relevance 950

Label: 0
> Reason
> - Summary of question: Which baseline model is used?
> - Summary of passage: Existing Wikipedia citations provide ground truth for evaluation.
> - Judgement: Ground-truth construction does not define a baseline model.
> 原因
> - 问题概述：使用什么基线模型？
> - Passage 概述：已有 Wikipedia 引用被用作评估真值。
> - 判断：真值构建未定义基线模型。

#### Passage 951

Retrieved by: BM25

> case, we consider the comparative relevance of the news article to the different entities occurring in it. As an example, let us consider the meeting of the Sudanese bishop Elias Taban with Hillary Clinton. Both entities are salient for the meeting. However, in Taban's Wikipedia page, this meeting is discussed prominently with a corresponding news reference, whereas in Hillary Clinton's Wikipedia page it is not reported at all. We believe this is not just an omission in Clinton's page but mirrors the fact that for the lesser known Taban the meeting is big news whereas for the more famous Clinton these kind of meetings are a regular occurrence, not all of which can be reported in what is supposed to be a selection of the most important events for her. Therefore, if two entities co-occur, the news is more relevant for the entity with the lower a priori authority.
> 
> The a priori authority of an entity (denoted by INLINEFORM0 ) can be measured in several ways. We opt for two approaches: (i) probability of entity INLINEFORM1 occurring in the corpus INLINEFORM2 , and (ii) authority assessed through centrality measures like PageRank BIBREF16 . For the second case we construct the graph INLINEFORM3 consisting of entities in INLINEFORM4 and news articles in INLINEFORM5 as vertices. The edges are established between INLINEFORM6 and entities in INLINEFORM7 , that is INLINEFORM8 , and the out-links from INLINEFORM9 , that is INLINEFORM10 (arrows present the edge direction).
> 
> Starting from a priori authority, we proceed to relative authority by comparing the a priori authority of co-occurring entities in INLINEFORM0 . We define the relative authority of INLINEFORM1 as the proportion of co-occurring entities INLINEFORM2 that have a higher a priori authority than INLINEFORM3 (see Equation EQREF28 . DISPLAYFORM0
> 
> As we might run the danger of not suggesting any news articles for entities with very high a priori authority (such as Clinton) due to the strict inequality constraint, we can relax the constraint such that the authority of co-occurring entities is above a certain threshold.
> 
> News Domain Authority. The news domain authority addresses two main aspects. Firstly, if bundled together with the relative authority feature, we can ensure that dependent on

#### Relevance 951

Label: 0
> Reason
> - Summary of question: Which baseline model is used?
> - Summary of passage: Relative entity authority uses occurrence probabilities and PageRank.
> - Judgement: These proposed features are not identified as baseline models.
> 原因
> - 问题概述：使用什么基线模型？
> - Passage 概述：相对实体权威度使用出现概率和 PageRank。
> - 判断：这些提出的特征未被指明为基线模型。

### Dense

#### Passage 956

Retrieved by: Dense

> We evaluate the generated supervised models for the two tasks, AEP and ASP, by splitting the train and testing instances. It is important to note that for the pairs INLINEFORM0 and the triple INLINEFORM1 , the news article INLINEFORM2 is referenced at time INLINEFORM3 by entity INLINEFORM4 , while the features take into account the entity profile at time INLINEFORM5 . This avoids any `overlapping' content between the news article and the entity page, which could affect the learning task of the functions INLINEFORM6 and INLINEFORM7 . Table TABREF47 shows the statistics of train and test instances. We learn the functions at year INLINEFORM8 and test on instances for the years greater than INLINEFORM9 . Please note that we do not show the performance for year 2014 as we do not have data for 2015 for evaluation.

#### Relevance 956

Label: 1
> Reason
> - Summary of question: Which baseline model is used?
> - Summary of passage: Temporal train-test splits prevent content overlap.
> - Judgement: The train-test design supplies the shared experimental setting in which baseline and proposed models are compared.
> 原因
> - 问题概述：使用什么基线模型？
> - Passage 概述：按时间划分训练测试集以避免内容重叠。
> - 判断：训练与测试设计说明基线和所提模型比较时的共同实验设置。

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 957

Retrieved by: Hybrid RRF followed by BGE reranking

> making INLINEFORM3 important for INLINEFORM4
> 
> Novelty: news article INLINEFORM0 should provide novel information for entity INLINEFORM1 taking into account its profile INLINEFORM2
> 
> Baseline Features. As discussed in Section SECREF2 , a variety of features that measure salience of an entity in text are available from the NLP community. We reimplemented the ones in Dunietz and Gillick BIBREF11 . This includes a variety of features, e.g. positional features, occurrence frequency and the internal POS structure of the entity and the sentence it occurs in. Table 2 in BIBREF11 gives details.
> 
> Relative Entity Frequency. Although frequency of mention and positional features play some role in baseline features, their interaction is not modeled by a single feature nor do the positional features encode more than sentence position. We therefore suggest a novel feature called relative entity frequency, INLINEFORM0 , that has three properties.: (i) It rewards entities for occurring throughout the text instead of only in some parts of the text, measured by the number of paragraphs it occurs in (ii) it rewards entities that occur more frequently in the opening paragraphs of an article as we model INLINEFORM1 as an exponential decay function. The decay corresponds to the positional index of the news paragraph. This is inspired by the news-specific discourse structure that tends to give short summaries of the most important facts and entities in the opening paragraphs. (iii) it compares entity frequency to the frequency of its co-occurring mentions as the weight of an entity appearing in a specific paragraph, normalized by the sum of the frequencies of other entities in INLINEFORM2 . DISPLAYFORM0
> 
> where, INLINEFORM0 represents a news paragraph from INLINEFORM1 , and with INLINEFORM2 we indicate the set of all paragraphs in INLINEFORM3 . The frequency of INLINEFORM4 in a paragraph INLINEFORM5 is denoted by INLINEFORM6 . With INLINEFORM7 and INLINEFORM8 we indicate the number of paragraphs in which entity INLINEFORM9 occurs, and the total number of paragraphs, respectively.
> 
> Relative Authority. In this case, we consider the comparative relevance of the news article to the different entities occurring in it. As an example, let us consider the meeting of the Sudanese bishop Elias Taban with Hillary Clinton. Both entities are salient for the

#### Relevance 957

Label: 1
> Reason
> - Summary of question: Which baseline model is used?
> - Summary of passage: Baseline features reimplement Dunietz and Gillick's entity salience measures.
> - Judgement: It identifies the prior baseline approach and its feature types.
> 原因
> - 问题概述：使用什么基线模型？
> - Passage 概述：基线特征复现 Dunietz 和 Gillick 的实体显著性指标。
> - 判断：它说明所用既有基线方法及特征类型。

#### Passage 958

Retrieved by: Hybrid RRF followed by BGE reranking

> Wikipedia is the largest source of open and collaboratively curated knowledge in the world. Introduced in 2001, it has evolved into a reference work with around 5m pages for the English Wikipedia alone. In addition, entities and event pages are updated quickly via collaborative editing and all edits are encouraged to include source citations, creating a knowledge base which aims at being both timely as well as authoritative. As a result, it has become the preferred source of information consumption about entities and events. Moreso, this knowledge is harvested and utilized in building knowledge bases like YAGO BIBREF0 and DBpedia BIBREF1 , and used in applications like text categorization BIBREF2 , entity disambiguation BIBREF3 , entity ranking BIBREF4 and distant supervision BIBREF5 , BIBREF6 .
> 
> However, not all Wikipedia pages referring to entities (entity pages) are comprehensive: relevant information can either be missing or added with a delay. Consider the city of New Orleans and the state of Odisha which were severely affected by cyclones Hurricane Katrina and Odisha Cyclone, respectively. While Katrina finds extensive mention in the entity page for New Orleans, Odisha Cyclone which has 5 times more human casualties (cf. Figure FIGREF2 ) is not mentioned in the page for Odisha. Arguably Katrina and New Orleans are more popular entities, but Odisha Cyclone was also reported extensively in national and international news outlets. This highlights the lack of important facts in trunk and long-tail entity pages, even in the presence of relevant sources. In addition, previous studies have shown that there is an inherent delay or lag when facts are added to entity pages BIBREF7 .
> 
> To remedy these problems, it is important to identify information sources that contain novel and salient facts to a given entity page. However, not all information sources are equal. The online presence of major news outlets is an authoritative source due to active editorial control and their articles are also a timely container of facts. In addition, their use is in line with current Wikipedia editing practice, as is shown in BIBREF7 that almost 20% of current citations in all entity pages are news articles. We therefore propose news suggestion as a novel task that enhances

#### Relevance 958

Label: 0
> Reason
> - Summary of question: Which baseline model is used?
> - Summary of passage: Missing information in Wikipedia motivates automated news suggestions.
> - Judgement: The motivation does not identify a baseline model.
> 原因
> - 问题概述：使用什么基线模型？
> - Passage 概述：Wikipedia 信息缺失促使研究自动新闻推荐。
> - 判断：研究动机未说明基线模型。

#### Passage 959

Retrieved by: Hybrid RRF followed by BGE reranking

> average the number of `relevant' pairs account for only around INLINEFORM0 of all pairs. A good indicator to support such a statement is the kappa (denoted by INLINEFORM1 ) statistic. INLINEFORM2 measures agreement between the algorithm and the gold standard on both labels while correcting for chance agreement (often expected due to extreme distributions). The INLINEFORM3 scores for B1 across the years is on average INLINEFORM4 , while for INLINEFORM5 we achieve a score of INLINEFORM6 (the maximum score for INLINEFORM7 is 1).
> 
> In Figure FIGREF60 we show the impact of the individual feature groups that contribute to the superior performance in comparison to the baselines. Relative entity frequency from the salience feature, models the entity salience as an exponentially decaying function based on the positional index of the paragraph where the entity appears. The performance of INLINEFORM0 with relative entity frequency from the salience feature group is close to that of all the features combined. The authority and novelty features account to a further improvement in terms of precision, by adding roughly a 7%-10% increase. However, if both feature groups are considered separately, they significantly outperform the baseline B1.

#### Relevance 959

Label: 1
> Reason
> - Summary of question: Which baseline model is used?
> - Summary of passage: Kappa and feature ablations compare the proposed system with B1.
> - Judgement: The B1 comparisons and salience-feature ablations provide supporting clues about the baseline comparison.
> 原因
> - 问题概述：使用什么基线模型？
> - Passage 概述：Kappa 和特征消融比较所提系统与 B1。
> - 判断：B1 比较及显著性特征消融为理解基线比较提供辅助线索。

## Question 0106

Paper: Automatic Detection of Cyberbullying in Social Media Text

> What is the source of the data?

### Common Retrieved Chunks

#### Passage 963

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> As pre-processing, we applied tokenisation, PoS-tagging and lemmatisation to the data using the LeTs Preprocess Toolkit BIBREF60 . In supervised learning, a machine learning algorithm takes a set of training instances (of which the label is known) and seeks to build a model that generates a desired prediction for an unseen instance. To enable the model construction, all instances are represented as a vector of features (i.e., inherent characteristics of the data) that contain information that is potentially useful to distinguish cyberbullying from non-cyberbullying content.
> 
> We experimentally tested whether cyberbullying events can be recognised automatically by lexical markers in a post. To this end, all posts were represented by a number of information sources (or features) including lexical features like bags-of-words, sentiment lexicon features and topic model features, which are described in more detail below. Prior to feature extraction, some data cleaning steps were executed, such as the replacement of hyperlinks and @-replies, removal of superfluous white spaces, and the replacement of abbreviations by their full form (based on an existing mapping dictionary ). Additionally, tokenisation was applied before INLINEFORM0 -gram extraction and sentiment lexicon matching, and stemming was applied prior to extracting topic model features.
> 
> After pre-processing of the corpus, the following feature types were extracted:
> 
> Word INLINEFORM0 -gram bag-of-words: binary features indicating the presence of word unigrams, bigrams and trigrams.
> 
> Character INLINEFORM0 -gram bag-of-words: binary features indicating the presence of character bigrams, trigrams and fourgrams (without crossing word boundaries). Character INLINEFORM1 -grams provide some abstraction from the word level and provide robustness to the spelling variation that characterises social media data.
> 
> Term lists: one binary feature derived for each one out of six lists, indicating the presence of an item from the list in a post: proper names, `allness' indicators (e.g. always, everybody), diminishers (e.g. slightly, relatively), intensifiers (e.g. absolutely, amazingly), negation words and aggressive language and profanity words. Person alternation is a binary feature indicating whether the combination of a first and second person pronoun occurs in order to capture interpersonal intent.
> 
> Subjectivity lexicon features: positive and negative opinion word ratios, as well as the overall post polarity were calculated using existing sentiment lexicons. For Dutch, we made use of the Duoman

#### Relevance 963

Label: 1
> Reason
> - Summary of question: Where does the data come from?
> - Summary of passage: Preprocessing and lexical, sentiment and topic features are described.
> - Judgement: Its description of social-media posts provides partial information about the kind of source data.
> 原因
> - 问题概述：数据来自哪里？
> - Passage 概述：介绍预处理及词汇、情感和主题特征。
> - 判断：它描述社交媒体帖子，提供来源数据类型的部分信息。

#### Passage 964

Retrieved by: BM25, Hybrid RRF

> TABREF37 ). Model selection was done using 10-fold cross validation in grid search over all possible feature types (i.e., groups of similar features, like different orders of INLINEFORM0 -gram bag-of-words features) and hyperparameter configurations. The best performing hyperparameters are selected by F INLINEFORM1 -score on the positive class. The winning model is then retrained on all held-in data and subsequently tested on a hold-out test set to assess whether the classifier is over- or under-fitting. The holdout represents a random sample ( INLINEFORM2 ) of all data. The folds were randomly stratified splits over the hold-in class distribution. Testing all feature type combinations is a rudimentary form of feature selection and provides insight into which types of features work best for this particular task.
> 
> Feature selection over all individual features was not performed because of the large feature space (NL: 795,072 and EN: 871,296 individual features). BIBREF59 , among other researchers, demonstrated the importance of joint optimisation, where feature selection and hyperparameter optimisation are performed simultaneously, since the techniques mutually influence each other.
> 
> The optimised models are evaluated against two baseline systems: i) an unoptimised linear-kernel SVM (configured with default parameter settings) based on word INLINEFORM0 -grams only and, ii) a keyword-based system that marks posts as positive for cyberbullying if they contain a word from existing vocabulary lists composed by aggressive language and profanity terms.

#### Relevance 964

Label: 0
> Reason
> - Summary of question: Where does the data come from?
> - Summary of passage: Model selection uses cross-validation and two baseline systems.
> - Judgement: Training and evaluation procedures do not reveal data provenance.
> 原因
> - 问题概述：数据来自哪里？
> - Passage 概述：模型选择使用交叉验证和两个基线系统。
> - 判断：训练和评估流程未说明数据来源。

#### Passage 965

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Two corpora were constructed by collecting data from the social networking site ASKfm, where users can create profiles and ask or answer questions, with the option of doing so anonymously. ASKfm data typically consists of question-answer pairs published on a user's profile. The data were retrieved by crawling a number of seed profiles using the GNU Wget software in April and October, 2013. After language filtering (i.e., non-English or non-Dutch content was removed), the experimental corpora comprised 113,698 and 78,387 posts for English and Dutch, respectively.

#### Relevance 965

Label: 1
> Reason
> - Summary of question: Where does the data come from?
> - Summary of passage: English and Dutch posts were crawled from ASKfm using GNU Wget in 2013.
> - Judgement: It directly states the website, collection method and corpus sizes.
> 原因
> - 问题概述：数据来自哪里？
> - Passage 概述：2013 年使用 GNU Wget 从 ASKfm 抓取英文和荷兰文帖子。
> - 判断：它直接给出来源网站、采集方法和语料规模。

#### Passage 967

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> detection in social media data by making use of a varied set of features. Most of them have, however, focussed on cyberbullying `attacks', or posts written by a bully. Moreover, it is not entirely clear if different forms of cyberbullying have been taken into account (e.g. sexual intimidation or harassment, or psychological threats), in addition to derogatory language or insults.
> 
> In the research described in this paper, cyberbullying is considered a complex phenomenon consisting of different forms of harmful behaviour online, which are described in more detail in our annotation scheme BIBREF30 . Purposing to facilitate manual monitoring efforts on social networks, we develop a system that automatically detects signals of cyberbullying, including attacks from bullies, as well as victim and bystander reactions. Similarly, BIBREF42 investigated bullying traces posted by different author roles (accuser, bully, reporter, victim). However, they collected tweets by using specific keywords (i.e., bully, bullied and bullying). As a result, their corpus contains many reports or testimonials of a cyberbullying incident (example 1), instead of actual signals that cyberbullying is going on. Moreover, their method implies that cyberbullying-related content devoid of such keywords will not be part of the training corpus.
> 
> `Some tweens got violent on the n train, the one boy got off after blows 2 the chest... Saw him cryin as he walkd away :( bullying not cool' BIBREF42
> 
> For this research, English and Dutch social media data were annotated for different forms of cyberbullying, based on the actors involved in a cyberbullying incident. After preliminary experiments for Dutch BIBREF37 , BIBREF40 , we currently explore the viability of detecting cyberbullying-related posts in Dutch and English social media. To this end, binary classification experiments are performed exploiting a rich feature set and optimised hyperparameters.
> 
> font=footnotesize,sc,justification=centering,labelsep=period

#### Relevance 967

Label: 1
> Reason
> - Summary of question: Where does the data come from?
> - Summary of passage: This study annotates English and Dutch social-media data; prior work used tweets.
> - Judgement: It partially identifies this study's data as social-media posts; the tweet source belongs to prior work.
> 原因
> - 问题概述：数据来自哪里？
> - Passage 概述：本研究标注英文和荷兰文社交媒体数据，既有研究使用推文。
> - 判断：它部分说明本研究使用社交媒体帖子，推文来源属于既有研究。

### BM25

#### Passage 960

Retrieved by: BM25

> Cyberbullying has been a widely covered research topic recently and studies have shed light on direct and indirect types of cyberbullying, implicit and explicit forms, verbal and non-verbal cyberbullying, and so on. This is important from a sociolinguistic point of view, but knowing what cyberbullying involves is also crucial to build models for automatic cyberbullying detection. In the following paragraphs, we present our data annotation guidelines BIBREF30 and focus on different types and roles related to the phenomenon.

#### Relevance 960

Label: 0
> Reason
> - Summary of question: Where does the data come from?
> - Summary of passage: Cyberbullying annotation guidelines distinguish forms and participant roles.
> - Judgement: The passage does not identify the data source.
> 原因
> - 问题概述：数据来自哪里？
> - Passage 概述：网络欺凌标注指南区分不同形式和参与角色。
> - 判断：该片段未说明数据来源。

#### Passage 961

Retrieved by: BM25

> characteristics of the Web: once defamatory or confidential information about a person is made public through the Internet, it is hard, if not impossible, to remove.
> 
> Finally, while arguing that repetition is a criterion to distinguish cyberbullying from single acts of aggression, BIBREF23 himself states that such a single aggressive action can be considered bullying under certain circumstances, although it is not entirely clear what these circumstances involve. Accordingly, BIBREF27 claim that repetition in cyberbullying is problematic to operationalise, as it is unclear what the consequences are of a single derogatory message on a public page. A single act of aggression or humiliation may result in continued distress and humiliation for the victim if it is shared or liked by multiple perpetrators or read by a large audience. BIBREF29 compare this with a `snowball effect': one post may be repeated or distributed by other people so that it becomes out of the control of the initial bully and has larger effects than was originally intended.
> 
> Given these arguments, a number of less `strict' definitions of cyberbullying were postulated by among others BIBREF6 , BIBREF5 , BIBREF1 , where a power imbalance and repetition are not deemed necessary conditions for cyberbullying.
> 
> The above paragraphs demonstrate that defining cyberbullying is far from trivial, and varying prevalence rates (cf. Section SECREF1 ) confirm that a univocal definition of the phenomenon is still lacking in the literature BIBREF1 . Based on existing conceptualisations, we define cyberbullying as content that is published online by an individual and that is aggressive or hurtful against a victim. Based on this definition, an annotation scheme was developed (see BIBREF30 ) to signal textual characteristics of cyberbullying, including posts from bullies, as well as reactions by victims and bystanders.

#### Relevance 961

Label: 0
> Reason
> - Summary of question: Where does the data come from?
> - Summary of passage: Cyberbullying is defined to include harmful posts and participant reactions.
> - Judgement: The definition does not establish where posts were collected.
> 原因
> - 问题概述：数据来自哪里？
> - Passage 概述：网络欺凌定义涵盖有害帖子及参与者反应。
> - 判断：定义未说明帖子从何处收集。

#### Passage 962

Retrieved by: BM25

> As mentioned earlier, although research on cyberbullying detection is more limited than social studies on the phenomenon, some important advances have been made in recent years. In what follows, we present a brief overview of the most important natural language processing approaches to cyberbullying detection.
> 
> Although some studies have investigated the effectiveness of rule-based modelling BIBREF31 , the dominant approach to cyberbullying detection involves machine learning. Most machine learning approaches are based on supervised BIBREF32 , BIBREF33 , BIBREF34 or semi-supervised learning BIBREF35 . The former involves the construction of a classifier based on labeled training data, whereas semi-supervised approaches rely on classifiers that are built from a training corpus containing a small set of labeled and a large set of unlabelled instances (a method that is often used to handle data sparsity). As cyberbullying detection essentially involves the distinction between bullying and non-bullying posts, the problem is generally approached as a binary classification task where the positive class is represented by instances containing (textual) cyberbullying, while the negative class includes instances containing non-cyberbullying or `innocent' text.
> 
> A key challenge in cyberbullying research is the availability of suitable data, which is necessary to develop models that characterise cyberbullying. In recent years, only a few datasets have become publicly available for this particular task, such as the training sets provided in the context of the CAW 2.0 workshop and more recently, the Twitter Bullying Traces dataset BIBREF36 . As a result, several studies have worked with the former or have constructed their own corpus from social media websites that are prone to bullying content, such as YouTube BIBREF32 , BIBREF33 , Formspring BIBREF33 , and ASKfm BIBREF37 (the latter two are social networking sites where users can send each other questions or respond to them). Despite the bottleneck of data availability, existing approaches to cyberbullying detection have shown its potential, and the relevance of automatic text analysis techniques to ensure child safety online has been recognised BIBREF38 , BIBREF39 .
> 
> Among the first studies on cyberbullying detection are BIBREF34 , BIBREF31 , BIBREF33 , who explored the predictive power of INLINEFORM0 -grams (with and without tf-idf weighting), part-of-speech information (e.g. first and second pronouns), and sentiment

#### Relevance 962

Label: 1
> Reason
> - Summary of question: Where does the data come from?
> - Summary of passage: Prior studies use YouTube, Formspring, ASKfm and public bullying datasets.
> - Judgement: It identifies candidate data sources in related work, including ASKfm and the authors' earlier work, supporting source tracing.
> 原因
> - 问题概述：数据来自哪里？
> - Passage 概述：既有研究使用 YouTube、Formspring、ASKfm 及公开欺凌数据集。
> - 判断：它提到 ASKfm 及作者早期工作等相关数据来源，有助于追溯来源。

### Dense

#### Passage 966

Retrieved by: Dense

> To be able to build representative models for cyberbullying, a suitable dataset is required. This section describes the construction of two corpora, English and Dutch, containing social media posts that are manually annotated for cyberbullying according to our fine-grained annotation scheme. This allows us to develop a detection system covering different forms and participants (or roles) involved in a cyberbullying event.

#### Relevance 966

Label: 1
> Reason
> - Summary of question: Where does the data come from?
> - Summary of passage: Two corpora contain manually annotated English and Dutch social-media posts.
> - Judgement: It gives partial source information: social-media posts, although no platform is named.
> 原因
> - 问题概述：数据来自哪里？
> - Passage 概述：两个语料库包含人工标注的英文和荷兰文社交媒体帖子。
> - 判断：它提供社交媒体帖子这一部分来源信息，但未指明平台。

#### Passage 968

Retrieved by: Dense

> annotation scheme describes two levels of annotation. Firstly, the annotators were asked to indicate, at the post level, whether the post under investigation was related to cyberbullying. If the post was considered a signal of cyberbullying, annotators identified the author's role. Secondly, at the subsentence level, the annotators were tasked with the identification of a number of fine-grained text categories related to cyberbullying. More concretely, they identified all text spans corresponding to one of the categories described in the annotation scheme. To provide the annotators with some context, all posts were presented within their original conversation when possible. All annotations were done using the Brat rapid annotation tool BIBREF52 , some examples of which are presented in Table TABREF33 .
> 
> font=footnotesize,sc,justification=centering,labelsep=period

#### Relevance 968

Label: 1
> Reason
> - Summary of question: Where does the data come from?
> - Summary of passage: Brat supports post-level and span-level annotations within conversation context.
> - Judgement: The annotation workflow explains how source conversations become the labeled corpus, complementing collection provenance.
> 原因
> - 问题概述：数据来自哪里？
> - Passage 概述：Brat 支持在对话上下文中标注帖子和文本片段。
> - 判断：标注流程说明来源对话如何转为带标签语料，补充数据生成过程。

#### Passage 969

Retrieved by: Dense

> The English and Dutch corpora were independently annotated for cyberbullying by trained linguists. All were Dutch native speakers and English second-language speakers. To demonstrate the validity of our guidelines, inter-annotator agreement scores were calculated using Kappa on a subset of each corpus. Inter-rater agreement for Dutch (2 raters) is calculated using Cohen's Kappa BIBREF53 . Fleiss' Kappa BIBREF54 is used for the English corpus ( INLINEFORM0 2 raters). Kappa scores for the identification of cyberbullying are INLINEFORM1 = 0.69 (Dutch) and INLINEFORM2 = 0.59 (English).
> 
> As shown in Table TABREF35 , inter-annotator agreement for the identification of the more fine-grained categories for English varies from fair to substantial BIBREF55 , except for defamation, which appears to be more difficult to recognise. No encouragements to the harasser were present in this subset of the corpus. For Dutch, the inter-annotator agreement is fair to substantial, except for curse and defamation. Analysis revealed that one of both annotators often annotated the latter as an insult, and in some cases even did not consider it as cyberbullying-related.
> 
> In short, the inter-rater reliability study shows that the annotation of cyberbullying is not trivial and that more fine-grained categories like defamation, curse and encouragements are sometimes hard to recognise. It appears that defamations were sometimes hard to distinguish from insults, whereas curses and exclusions were sometimes considered insults or threats. The analysis further reveals that encouragements to the harasser are subject to interpretation. Some are straightforward (e.g. `I agree we should send her hate'), whereas others are subject to the annotator's judgement and interpretation (e.g. `hahaha', `LOL').

#### Relevance 969

Label: 1
> Reason
> - Summary of question: Where does the data come from?
> - Summary of passage: Linguists annotate the two corpora and agreement is measured with Kappa.
> - Judgement: It describes the English and Dutch corpora's annotation provenance, complementing collection-source information.
> 原因
> - 问题概述：数据来自哪里？
> - Passage 概述：语言学人员标注两个语料库，并用 Kappa 衡量一致性。
> - 判断：它说明英文和荷兰文语料的标注来源，可补充采集来源信息。

### Hybrid RRF

#### Passage 970

Retrieved by: Hybrid RRF

> BIBREF38 , BIBREF39 .
> 
> Among the first studies on cyberbullying detection are BIBREF34 , BIBREF31 , BIBREF33 , who explored the predictive power of INLINEFORM0 -grams (with and without tf-idf weighting), part-of-speech information (e.g. first and second pronouns), and sentiment information based on profanity lexicons for this task. Similar features were also exploited for the detection of cyberbullying events and fine-grained text categories related to cyberbullying BIBREF37 , BIBREF40 . More recent studies have demonstrated the added value of combining such content-based features with user-based information, such as including users' activities on a social network (i.e., the number of posts), their age, gender, location, number of friends and followers, and so on BIBREF32 , BIBREF35 , BIBREF41 . Moreover, semantic features have been explored to further improve classification performance of the task. To this end, topic model information BIBREF42 , as well as semantic relations between INLINEFORM1 -grams (according to a Word2Vec model BIBREF43 ) have been integrated.
> 
> As mentioned earlier, data collection remains a bottleneck in cyberbullying research. Although cyberbullying has been recognised as a serious problem (cf. Section SECREF1 ), real-world examples are often hard to find in public platforms. Naturally, the vast majority of communications do not contain traces of verbal aggression or transgressive behaviour. When constructing a corpus for machine learning purposes, this results in imbalanced datasets, meaning that one class (e.g. cyberbullying posts) is much less represented in the corpus than the other (e.g. non-cyberbullying posts). To tackle this problem, several studies have adopted resampling techniques BIBREF35 , BIBREF41 , BIBREF31 that create synthetic minority class examples or reduce the number of negative class examples (i.e., minority class oversampling and majority class undersampling BIBREF44 ).
> 
> Table TABREF9 presents a number of recent studies on cyberbullying detection, providing insight into the state of the art in cyberbullying research and the contribution of the current research to the domain.
> 
> The studies discussed in this section have demonstrated the feasibility of automatic cyberbullying detection in social media data by making use of a varied set of features. Most of them have, however, focussed on cyberbullying `attacks', or posts written by a bully. Moreover, it is not entirely clear if different forms of cyberbullying

#### Relevance 970

Label: 1
> Reason
> - Summary of question: Where does the data come from?
> - Summary of passage: Related work discusses features, social-network metadata and class imbalance.
> - Judgement: Its discussion of social-network posts and corpus construction provides supporting data-source context.
> 原因
> - 问题概述：数据来自哪里？
> - Passage 概述：相关工作讨论特征、社交网络元数据和类别不平衡。
> - 判断：它讨论社交网络帖子和语料构建，为数据来源提供辅助背景。

### Hybrid RRF followed by BGE reranking

#### Passage 971

Retrieved by: Hybrid RRF followed by BGE reranking

> and subjectivity lexicons prove to be strong features for this task. In effect, adding character INLINEFORM2 -grams always improved classification performance for both languages. They likely provide robustness to lexical variation in social media text, as compared to word INLINEFORM3 -grams. While subjectivity lexicons appear to be discriminative features, term lists perform badly on their own as well as in combinations for both languages. This shows once again (cf. profanity baseline) that cyberbullying detection requires more sophisticated information sources than profanity lists. Topic models seem to do badly for both languages on their own, but in combination, they improve Dutch performance consistently. A possible explanation for their varying performance in both languages would be that the topic models trained on the Dutch background corpus are of better quality than the English ones. In effect, a random selection of background corpus texts reveals that the English scrape contains more noisy data (i.e., low word-count posts and non-English posts) than the Dutch data.
> 
> A shallow qualitative analysis of the classification output provided insight into some of the classification mistakes.
> 
> Table TABREF52 gives an overview of the error rates per cyberbullying category of the best performing and baseline systems. This could give an indication of which types of bullying the current system has trouble classifying. All categories are always considered positive for cyberbullying (i.e., the error rate equals the false negative rate), except for Sexual and Insult which can also be negative (in case of harmless sexual talk and `socially acceptable' insulting language like `hi bitches, in for a movie?' the corresponding category was indicated, but the post itself was not annotated as cyberbullying) and Not cyberbullying, which is always negative. Error rates often being lowest for the profanity baseline confirms that it performs particularly well in terms of recall (at the expense of precision, see Table TABREF47 ) When looking at the best system for both languages, we see that Defense is the hardest category to correctly classify. This should not be a surprise as the category comprises defensive posts from bystanders and victims, which contain less aggressive language than cyberbullying attacks and are often shorter in length than the latter. Assertive defensive posts (i.e., a subcategory

#### Relevance 971

Label: 1
> Reason
> - Summary of question: Where does the data come from?
> - Summary of passage: Feature performance and annotation-category error rates are analyzed.
> - Judgement: The references to scraped background corpora and their contents provide partial provenance clues.
> 原因
> - 问题概述：数据来自哪里？
> - Passage 概述：分析特征性能及各标注类别的错误率。
> - 判断：它提到抓取的背景语料及内容，提供部分来源线索。

#### Passage 972

Retrieved by: Hybrid RRF followed by BGE reranking

> Cyberbullying research is mainly centered around the conceptualisation, occurrence and prevention of the phenomenon BIBREF16 , BIBREF0 , BIBREF17 . Additionally, different forms of cyberbullying have been identified BIBREF18 , BIBREF12 , BIBREF20 and compared with forms of traditional or offline bullying BIBREF19 . Like traditional bullying, direct and indirect forms of cyberbullying have been identified. Direct cyberbullying refers to actions in which the victim is directly involved (e.g. sending a virus-infected file, excluding someone from an online group, insulting and threatening), whereas indirect cyberbullying can take place without awareness of the victim (e.g. outing or publishing confidential information, spreading gossip, creating a hate page on social networking sites) BIBREF19 .
> 
> The present annotation scheme describes some specific textual categories related to cyberbullying, including threats, insults, defensive statements from a victim, encouragements to the harasser, etc. (see Section SECREF15 for a complete overview). All of these forms were inspired by social studies on cyberbullying BIBREF7 , BIBREF19 and manual inspection of cyberbullying examples.

#### Relevance 972

Label: 0
> Reason
> - Summary of question: Where does the data come from?
> - Summary of passage: Direct and indirect cyberbullying motivate textual annotation categories.
> - Judgement: Cyberbullying types do not identify the dataset source.
> 原因
> - 问题概述：数据来自哪里？
> - Passage 概述：直接和间接网络欺凌为文本标注类别提供依据。
> - 判断：欺凌类型未说明数据集来源。

## Question 0107

Paper: Short Text Language Identification for Under Resourced Languages

> What is the approach of previous work?

### Common Retrieved Chunks

#### Passage 973

Retrieved by: BM25, Dense, Hybrid RRF

> BIBREF13, BIBREF14, SVMs BIBREF15 and similar models work very well for doing LID. The DSL 2017 paper BIBREF1, for example, gives an overview of the solutions of all of the teams that competed on the shared task and the winning approach BIBREF16 used an SVM with character n-gram, parts of speech tag features and some other engineered features. The winning approach for DSL 2015 used an ensemble naive Bayes classifier. The fasttext classifier BIBREF17 is perhaps one of the best known efficient 'shallow' text classifiers that have been used for LID .
> 
> Multiple papers have proposed hierarchical stacked classifiers (including lexicons) that would for example first classify a piece of text by language group and then by exact language BIBREF18, BIBREF19, BIBREF8, BIBREF0. Some work has also been done on classifying surnames between Tshivenda, Xitsonga and Sepedi BIBREF20. Additionally, data augmentation BIBREF21 and adversarial training BIBREF22 approaches are potentially very useful to reduce the requirement for data.
> 
> Researchers have investigated deeper LID models like bidirectional recurrent neural networks BIBREF23 or ensembles of recurrent neural networks BIBREF24. The latter is reported to achieve 95.12% in the DSL 2015 shared task. In these models text features can include character and word n-grams as well as informative character and word-level features learnt BIBREF25 from the training data. The neural methods seem to work well in tasks where more training data is available.
> 
> In summary, LID of short texts, informal styles and similar languages remains a difficult problem which is actively being researched. Increased confusion can in general be expected between shorter pieces of text and languages that are more closely related. Shallow methods still seem to work well compared to deeper models for LID. Other remaining research opportunities seem to be data harvesting, building standardised datasets and creating shared tasks for South Africa and Africa. Support for language codes that include more languages seems to be growing and discoverability of research is improving with more survey papers coming out. Paywalls also seem to no longer be a problem; the references used in this paper was either openly published or available as preprint papers.

#### Relevance 973

Label: 1
> Reason
> - Summary of question: What approaches did previous work use?
> - Summary of passage: Prior LID systems use SVMs, naive Bayes, FastText, hierarchies and recurrent networks.
> - Judgement: It directly surveys previous methods and their features.
> 原因
> - 问题概述：既有研究使用什么方法？
> - Passage 概述：既有语言识别系统使用 SVM、朴素贝叶斯、FastText、分层模型和循环网络。
> - 判断：它直接综述既有方法及其特征。

#### Passage 974

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Accurate language identification (LID) is the first step in many natural language processing and machine comprehension pipelines. If the language of a piece of text is known then the appropriate downstream models like parts of speech taggers and language models can be applied as required.
> 
> LID is further also an important step in harvesting scarce language resources. Harvested data can be used to bootstrap more accurate LID models and in doing so continually improve the quality of the harvested data. Availability of data is still one of the big roadblocks for applying data driven approaches like supervised machine learning in developing countries.
> 
> Having 11 official languages of South Africa has lead to initiatives (discussed in the next section) that have had positive effect on the availability of language resources for research. However, many of the South African languages are still under resourced from the point of view of building data driven models for machine comprehension and process automation.
> 
> Table TABREF2 shows the percentages of first language speakers for each of the official languages of South Africa. These are four conjunctively written Nguni languages (zul, xho, nbl, ssw), Afrikaans (afr) and English (eng), three disjunctively written Sotho languages (nso, sot, tsn), as well as tshiVenda (ven) and Xitsonga (tso). The Nguni languages are similar to each other and harder to distinguish. The same is true of the Sotho languages.
> 
> This paper presents a hierarchical naive Bayesian and lexicon based classifier for LID of short pieces of text of 15-20 characters long. The algorithm is evaluated against recent approaches using existing test sets from previous works on South African languages as well as the Discriminating between Similar Languages (DSL) 2015 and 2017 shared tasks.
> 
> Section SECREF2 reviews existing works on the topic and summarises the remaining research problems. Section SECREF3 of the paper discusses the proposed algorithm and Section SECREF4 presents comparative results.

#### Relevance 974

Label: 1
> Reason
> - Summary of question: What approaches did previous work use?
> - Summary of passage: The introduction presents this paper's hierarchical Bayesian and lexicon classifier.
> - Judgement: The introduction positions the proposed method against existing LID research and points to its prior-work survey.
> 原因
> - 问题概述：既有研究使用什么方法？
> - Passage 概述：引言介绍本研究的分层贝叶斯与词典分类器。
> - 判断：引言将所提方法置于既有语言识别研究中，并指向相关工作综述。

#### Passage 975

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The proposed LID algorithm builds on the work in BIBREF8 and BIBREF26. We apply a naive Bayesian classifier with character (2, 4 & 6)-grams, word unigram and word bigram features with a hierarchical lexicon based classifier.
> 
> The naive Bayesian classifier is trained to predict the specific language label of a piece of text, but used to first classify text as belonging to either the Nguni family, the Sotho family, English, Afrikaans, Xitsonga or Tshivenda. The scikit-learn multinomial naive Bayes classifier is used for the implementation with an alpha smoothing value of 0.01 and hashed text features.
> 
> The lexicon based classifier is then used to predict the specific language within a language group. For the South African languages this is done for the Nguni and Sotho groups. If the lexicon prediction of the specific language has high confidence then its result is used as the final label else the naive Bayesian classifier's specific language prediction is used as the final result. The lexicon is built over all the data and therefore includes the vocabulary from both the training and testing sets.
> 
> The lexicon based classifier is designed to trade higher precision for lower recall. The proposed implementation is considered confident if the number of words from the winning language is at least one more than the number of words considered to be from the language scored in second place.
> 
> The stacked classifier is tested against three public LID implementations BIBREF17, BIBREF23, BIBREF8. The LID implementation described in BIBREF17 is available on GitHub and is trained and tested according to a post on the fasttext blog. Character (5-6)-gram features with 16 dimensional vectors worked the best. The implementation discussed in BIBREF23 is available from https://github.com/tomkocmi/LanideNN. Following the instructions for an OSX pip install of an old r0.8 release of TensorFlow, the LanideNN code could be executed in Python 3.7.4. Settings were left at their defaults and a learning rate of 0.001 was used followed by a refinement with learning rate of 0.0001. Only one code modification was applied to return the results from a method that previously just printed to screen. The LID algorithm described in BIBREF8 is also available on GitHub.
> 
> The stacked classifier is also

#### Relevance 975

Label: 1
> Reason
> - Summary of question: What approaches did previous work use?
> - Summary of passage: The proposed stack is compared with FastText and LanideNN implementations.
> - Judgement: It supplies previous-system details, including FastText n-gram features.
> 原因
> - 问题概述：既有研究使用什么方法？
> - Passage 概述：所提堆叠模型与 FastText、LanideNN 等实现比较。
> - 判断：它提供既有系统细节，包括 FastText 的 n-gram 特征。

#### Passage 976

Retrieved by: BM25, Dense, Hybrid RRF

> The focus of this section is on recently published datasets and LID research applicable to the South African context. An in depth survey of algorithms, features, datasets, shared tasks and evaluation methods may be found in BIBREF0.
> 
> The datasets for the DSL 2015 & DSL 2017 shared tasks BIBREF1 are often used in LID benchmarks and also available on Kaggle . The DSL datasets, like other LID datasets, consists of text sentences labelled by language. The 2017 dataset, for example, contains 14 languages over 6 language groups with 18000 training samples and 1000 testing samples per language.
> 
> The recently published JW300 parallel corpus BIBREF2 covers over 300 languages with around 100 thousand parallel sentences per language pair on average. In South Africa, a multilingual corpus of academic texts produced by university students with different mother tongues is being developed BIBREF3. The WiLI-2018 benchmark dataset BIBREF4 for monolingual written natural language identification includes around 1000 paragraphs of 235 languages. A possibly useful link can also be made BIBREF5 between Native Language Identification (NLI) (determining the native language of the author of a text) and Language Variety Identification (LVI) (classification of different varieties of a single language) which opens up more datasets. The Leipzig Corpora Collection BIBREF6, the Universal Declaration of Human Rights and Tatoeba are also often used sources of data.
> 
> The NCHLT text corpora BIBREF7 is likely a good starting point for a shared LID task dataset for the South African languages BIBREF8. The NCHLT text corpora contains enough data to have 3500 training samples and 600 testing samples of 300+ character sentences per language. Researchers have recently started applying existing algorithms for tasks like neural machine translation in earnest to such South African language datasets BIBREF9.
> 
> Existing NLP datasets, models and services BIBREF10 are available for South African languages. These include an LID algorithm BIBREF11 that uses a character level n-gram language model. Multiple papers have shown that 'shallow' naive Bayes classifiers BIBREF12, BIBREF8, BIBREF13, BIBREF14, SVMs BIBREF15 and similar models work very well for doing LID. The DSL 2017 paper BIBREF1, for example, gives an overview of the solutions of all of the teams that competed on the shared task and the winning

#### Relevance 976

Label: 1
> Reason
> - Summary of question: What approaches did previous work use?
> - Summary of passage: Related work includes character n-gram language models, naive Bayes and SVMs.
> - Judgement: It explicitly identifies approaches used in previous research.
> 原因
> - 问题概述：既有研究使用什么方法？
> - Passage 概述：相关工作包括字符 n-gram 语言模型、朴素贝叶斯和 SVM。
> - 判断：它明确指出既有研究采用的方法。

#### Passage 977

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> The average classification accuracy results are summarised in Table TABREF9. The accuracies reported are for classifying a piece of text by its specific language label. Classifying text only by language group or family is a much easier task as reported in BIBREF8.
> 
> Different variations of the proposed classifier were evaluated. A single NB classifier (NB), a stack of two NB classifiers (NB+NB), a stack of a NB classifier and lexicon (NB+Lex) and a lexicon (Lex) by itself. A lexicon with a 50% training token dropout is also listed to show the impact of the lexicon support on the accuracy.
> 
> From the results it seems that the DSL 2017 task might be harder than the DSL 2015 and NCHLT tasks. Also, the results for the implementation discussed in BIBREF23 might seem low, but the results reported in that paper is generated on longer pieces of text so lower scores on the shorter pieces of text derived from the NCHLT corpora is expected.
> 
> The accuracy of the proposed algorithm seems to be dependent on the support of the lexicon. Without a good lexicon a non-stacked naive Bayesian classifier might even perform better.
> 
> The execution performance of some of the LID implementations are shown in Table TABREF10. Results were generated on an early 2015 13-inch Retina MacBook Pro with a 2.9 GHz CPU (Turbo Boosted to 3.4 GHz) and 8GB RAM. The C++ implementation in BIBREF17 is the fastest. The implementation in BIBREF8 makes use of un-hashed feature representations which causes it to be slower than the proposed sklearn implementation. The execution performance of BIBREF23 might improve by a factor of five to ten when executed on a GPU.

#### Relevance 977

Label: 1
> Reason
> - Summary of question: What approaches did previous work use?
> - Summary of passage: Accuracy and runtime comparisons discuss several unnamed referenced implementations.
> - Judgement: It gives implementation details for earlier systems, including unhashed features, supporting comparison of their approaches.
> 原因
> - 问题概述：既有研究使用什么方法？
> - Passage 概述：准确率和运行时间比较讨论若干以引用编号指代的实现。
> - 判断：它给出早期系统的实现细节，包括未哈希特征，可辅助理解既有方法。

#### Passage 978

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> LID of short texts, informal styles and similar languages remains a difficult problem which is actively being researched. The proposed algorithm was evaluated on three existing datasets and compared to the implementations of three public LID implementations as well as to reported results of four other algorithms. It performed well relative to the other methods beating their results. However, the performance is dependent on the support of the lexicon.
> 
> We would like to investigate the value of a lexicon in a production system and how to possibly maintain it using self-supervised learning. We are investigating the application of deeper language models some of which have been used in more recent DSL shared tasks. We would also like to investigate data augmentation strategies to reduce the amount of training data that is required.
> 
> Further research opportunities include data harvesting, building standardised datasets and shared tasks for South Africa as well as the rest of Africa. In general, the support for language codes that include more languages seems to be growing, discoverability of research is improving and paywalls seem to no longer be a big problem in getting access to published research.

#### Relevance 978

Label: 1
> Reason
> - Summary of question: What approaches did previous work use?
> - Summary of passage: The conclusion summarizes lexicon dependence and future research.
> - Judgement: Comparisons with public implementations and reported algorithms provide pointers to the previous approaches.
> 原因
> - 问题概述：既有研究使用什么方法？
> - Passage 概述：结论概述词典依赖性和未来研究方向。
> - 判断：与公开实现及既有算法结果的比较为此前方法提供定位线索。

#### Passage 979

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> with learning rate of 0.0001. Only one code modification was applied to return the results from a method that previously just printed to screen. The LID algorithm described in BIBREF8 is also available on GitHub.
> 
> The stacked classifier is also tested against the results reported for four other algorithms BIBREF16, BIBREF26, BIBREF24, BIBREF15. All the comparisons are done using the NCHLT BIBREF7, DSL 2015 BIBREF19 and DSL 2017 BIBREF1 datasets discussed in Section SECREF2.

#### Relevance 979

Label: 1
> Reason
> - Summary of question: What approaches did previous work use?
> - Summary of passage: Four referenced algorithms are compared on NCHLT and DSL datasets.
> - Judgement: It points to the earlier algorithms and comparison datasets, providing references for reconstructing prior approaches.
> 原因
> - 问题概述：既有研究使用什么方法？
> - Passage 概述：在 NCHLT 和 DSL 数据集上比较四个引用算法。
> - 判断：它指出既有算法及对比数据集，为还原既有方法提供引用线索。

### BM25

None

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0108

Paper: One Single Deep Bidirectional LSTM Network for Word Sense Disambiguation of Text Data

> How many layers does their model have?

### Common Retrieved Chunks

#### Passage 980

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Given a document and the position of a target word, our model computes a probability distribution over possible senses related to that word. The architecture of our model, depicted in Fig. FIGREF4 , consist of 6 layers which are a sigmoid layer (at the top), a fully-connected layer, a concatenation layer, a BLSTM layer, a cosine layer, and a sense and word embeddings layer (on the bottom).
> 
> In contrast to other supervised neural WSD networks in which generally a softmax layer - with a cross entropy or hinge loss - is parameterized by the context words and selects the corresponding weight matrix and bias vector for each ambiguous word's senses BIBREF15 BIBREF16 , our network shares parameters over all words' senses. While remaining computationally efficient, this structure aims to encode statistical information across different words enabling the network to select the true sense (or even a proper word) in a blank space within a context.
> 
> Due to the replacement of their softmax layers with a sigmoid layer in our network, we need to impose a modification in the input of the model. For this purpose, not only the contextual features are going to make the input of the network, but also, the sense for which we are interested to find out whether that given context makes sense or not (no pun intended) would be provided to the network. Next, the context words would be transferred to a sequence of word embeddings while the sense would be represented as a sense embedding (the shaded embeddings in Fig. FIGREF4 ). For a set of candidate senses (i.e. INLINEFORM0 ) for an ambiguous term, after computing cosine similarities of each sense embedding with the word embeddings of the context words, we expect the sequence result of similarities between the true sense and the surrounding context communicate a pattern-like information that can be encoded through our BLSTM network; for the incorrect senses this premise does not hold. Several WSD studies already incorporated the idea of sense-context cosine similarities in their models BIBREF17 BIBREF18 .

#### Relevance 980

Label: 1
> Reason
> - Summary of question: How many layers does the proposed model have?
> - Summary of passage: The architecture contains six explicitly listed layers.
> - Judgement: It directly states the requested total layer count.
> 原因
> - 问题概述：所提模型共有多少层？
> - Passage 概述：该架构包含明确列出的六层。
> - 判断：它直接给出所问的总层数。

#### Passage 981

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Between-all-models comparisons - When SensEval-3 task was launched 47 submissions (supervised and unsupervised algorithms) were received addressing this task. Afterward, some other papers tried to work on this data and reported their results in separate articles as well. We compare the result of our model with the top-performing and low-performing algorithms (supervised). We show our single model sits among the 5 top-performing algorithms, considering that in other algorithms for each ambiguous word one separate classifier is trained (i.e. in the same number of ambiguous words in a language there have to be classifiers; which means 57 classifiers for this specific task). Table TABREF19 shows the results of the top-performing and low-performing supervised algorithms.
> 
> The first two algorithms represent the state-of-the-art models of supervised WSD when evaluated on SensEval-3. Multi-classifier BLSTM BIBREF15 consists of deep neural networks which make use of pre-trained word embeddings. While the lower layers of these networks are shared, upper layers of each network are responsible to individually classify the ambiguous that word the network is associated with. IMS+adapted CW BIBREF16 is another WSD model that considers deep neural networks and also uses pre-trained word embeddings as inputs. In contrast to Multi-classifier BLSTM, this model relies on features such as POS tags, collocations, and surrounding words to achieve their result. For these two models, softmax constitutes the output layers of all networks. htsa3 BIBREF22 was the winner of the SensEval-3 lexical sample. It is a Naive Bayes system applied mainly to raw words, lemmas, and POS tags with correction of the a-priori frequencies. IRST-Kernels BIBREF23 utilizes kernel methods for pattern abstraction, paradigmatic and syntagmatic information and unsupervised term proximity on British National Corpus (BNC), in SVM classifiers. Likewise, nusels BIBREF24 makes use of SVM classifiers with a combination of knowledge sources (part-of-speech of neighboring words, words in context, local collocations, syntactic relations. The second part of the table lists the low-performing supervised algorithms BIBREF3 . Considering their ranking scores we see that there are unsupervised methods that outperform these supervised algorithms.
> 
> Within-our-model comparisons - Besides several internal experiments to examine the importance of some hyper-parameters to our network, we investigated if the sequential follow of cosine similarities computed between a true sense

#### Relevance 981

Label: 1
> Reason
> - Summary of question: How many layers does the proposed model have?
> - Summary of passage: The model is compared with supervised WSD systems and their classifier designs.
> - Judgement: The architectural comparison situates the single proposed network relative to shared and classifier-specific layers.
> 原因
> - 问题概述：所提模型共有多少层？
> - Passage 概述：将模型与监督式词义消歧系统及其分类器设计比较。
> - 判断：架构比较将所提单网络与共享层、分类器专属层联系起来，提供结构线索。

#### Passage 983

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Dropout BIBREF20 is a regularization technique for neural network models where randomly selected neurons are ignored during training. This means that their contribution to the activation of downstream neurons is temporally removed on the forward pass, and any weight updates are not applied to the neuron on the backward pass. The effect is that the network becomes less sensitive to the specific weights of neurons, resulting in better generalization, and a network that is less likely to overfit the training data. In our network, dropout is applied to the embeddings as well as the outputs of the merge and fully-connected layers.
> 
> Following the dropout logic, dropword BIBREF21 is the word level generalizations of it, but in word dropout the word is set to zero while in dropword it is replaced with a specific tag. The tag is subsequently treated just like one word in the vocabulary. The motivation for doing dropword and word dropout is to decrease the dependency on individual words in the training context. Since by replacing word dropout with dropword we observed no change in the results, only word dropout was applied to the sequence of context words during training.

#### Relevance 983

Label: 1
> Reason
> - Summary of question: How many layers does the proposed model have?
> - Summary of passage: Dropout is applied to embeddings, merge outputs and fully connected outputs.
> - Judgement: It names embedding, merge and fully connected components, contributing to a layer inventory.
> 原因
> - 问题概述：所提模型共有多少层？
> - Passage 概述：对嵌入、合并输出和全连接输出应用 dropout。
> - 判断：它指出嵌入、合并和全连接组件，可补充层结构清单。

#### Passage 985

Retrieved by: Dense, Hybrid RRF

> there are unsupervised methods that outperform these supervised algorithms.
> 
> Within-our-model comparisons - Besides several internal experiments to examine the importance of some hyper-parameters to our network, we investigated if the sequential follow of cosine similarities computed between a true sense and its preceding and succeeding context words carries a pattern-like information that can be encoded with BLSTM. Table TABREF20 presents the results of these experiments.
> 
> The first row shows the best result of the network that we described above (and depicted in Fig. FIGREF4 ). Each of the other rows shows one change that we applied to the network to see the behavior of the network in terms of F-measure. In the middle part, we are specifically concerned about the importance of the presence of a BLSTM layer in our network. So, we introduced some fundamental changes in the input or in the structure of the network. Generally, it is expected that the cosine similarities of closer words (in the context) to the true sense be larger than the incorrect senses' BIBREF17 ; however, if a series of cosine similarities can be encoded through an LSTM (or BLSTM) network should be experimented. We observe if reverse the sequential follow of information into our Bidirectional LSTM, we shuffle the order of the context words, or even replace our Bidirectional LSTMs with two different fully-connected networks of the same size 50 (the size of the LSTMs outputs), the achieved results were notably less than 72.5%.
> 
> In the third section of the table, we report our changes to the hyper-parameters. Specifically, we see the importance of using GloVe as pre-trained word embeddings, how word dropout improves generalization, and how context size plays an important role in the final classification result (showing one of our experiments).

#### Relevance 985

Label: 1
> Reason
> - Summary of question: How many layers does the proposed model have?
> - Summary of passage: Ablations replace BLSTMs and vary embeddings, dropout and context size.
> - Judgement: It identifies the BLSTM layer and replacement networks, providing useful clues about the model's composition.
> 原因
> - 问题概述：所提模型共有多少层？
> - Passage 概述：消融替换 BLSTM，并改变嵌入、dropout 和上下文大小。
> - 判断：它指出 BLSTM 层及替代网络，为模型组成提供有效线索。

#### Passage 986

Retrieved by: Dense, Hybrid RRF

> and results in Section 4 supported by a discussion on how to avoid some drawbacks of the current model in order to achieve higher accuracies and demand less number of training data which is desirable. Finally, in Section 5, we conclude with some future research directions for the construction of sense embeddings as well as applications of such model in other domains such as biomedicine.

#### Relevance 986

Label: 0
> Reason
> - Summary of question: How many layers does the proposed model have?
> - Summary of passage: The paper outline mentions results, limitations and future applications.
> - Judgement: It contains no architectural count.
> 原因
> - 问题概述：所提模型共有多少层？
> - Passage 概述：论文结构提及结果、局限和未来应用。
> - 判断：它没有任何架构层数信息。

#### Passage 987

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> embeddings; in this work, GloVe vectors are used.
> 
> On the other hand, the output of the network that is examining sense INLINEFORM0 is DISPLAYFORM0
> 
> where INLINEFORM0 and INLINEFORM1 are the weights and the bias of the classification layer (sigmoid), and INLINEFORM2 is the result of the merge layer (concatenation).
> 
> When we train the network, for an instance with the correct sense and the given context as inputs, INLINEFORM0 is set to be 1.0, and for incorrect senses they are set to be 0.0. During testing, however, among all the senses, the output of the network for a sense that gives the highest value of INLINEFORM1 will be considered as the true sense of the ambiguous term, in other words, the correct sense would be: DISPLAYFORM0
> 
> By applying softmax to the result of estimated classification values, INLINEFORM0 , we can show them as probabilities; this facilitates interpretation of the results.
> 
> Further, the hidden layer INLINEFORM0 is computed as DISPLAYFORM0
> 
> where INLINEFORM0 means rectified linear unit; INLINEFORM1 is the concatenated outputs of the right and left traversing LSTMs of the BLSTM when the last context components are met. INLINEFORM2 and INLINEFORM3 are the weights and bias for the hidden layer.

#### Relevance 987

Label: 1
> Reason
> - Summary of question: How many layers does the proposed model have?
> - Summary of passage: Equations describe sigmoid, merge and hidden-layer computations.
> - Judgement: It describes classification, concatenation and hidden-layer computations, supplying partial layer information.
> 原因
> - 问题概述：所提模型共有多少层？
> - Passage 概述：公式描述 sigmoid、合并和隐藏层计算。
> - 判断：它描述分类、拼接和隐藏层计算，提供部分层结构信息。

### BM25

#### Passage 982

Retrieved by: BM25

> In contrast to common one-classifier-per-each-word supervised WSD algorithms, we developed our single network of BLSTM that is able to effectively exploit word orders and achieve comparable results with the best-performing supervised algorithms. This single WSD BLSTM network is language and domain independent and can be applied to resource-poor languages (or domains) as well. As an ongoing project, we also provided a direction which can lead us to the improvement of the results of the current network using pre-trained sense embeddings.
> 
> For future work, besides following the discussed direction in order to resolve the inadequacy of the network regarding having two non-overlapping vector spaces of the embeddings, we plan to examine the network on technical domains such as biomedicine as well. In this case, our model will be evaluated on MSH WSD dataset prepared by National Library of Medicine (NLM). Also, construction of sense embeddings using (extended) definitions of senses BIBREF25 BIBREF26 can be tested. Moreover, considering that for many senses we have at least one (lexically) unambiguous word representing that sense, we also aim to experiment with unsupervised (pre-)training of our network which benefits form quarry management by which more training data will be automatically collected from the web.

#### Relevance 982

Label: 1
> Reason
> - Summary of question: How many layers does the proposed model have?
> - Summary of passage: A single BLSTM network is proposed, with future sense-embedding work.
> - Judgement: Identifying the model as a single BLSTM network provides partial structural context for interpreting its depth.
> 原因
> - 问题概述：所提模型共有多少层？
> - Passage 概述：提出单个 BLSTM 网络，并计划研究义项嵌入。
> - 判断：它指出模型为单个 BLSTM 网络，为理解其深度提供部分结构背景。

#### Passage 984

Retrieved by: BM25

> From the results of Table TABREF19 , we notice our single WSD network, despite eliminating the problem of having a large number of WSD classifiers, still falls short when is compared with the state-of-the-art WSD algorithms. Based on our intuition and supported by some of our preliminary experiments, this deficiency stems from an important factor in our BLSTM network. Since no sense embedding is made publicly available for use, the sense embeddings are initialized randomly; yet, word embeddings are initialized by pre-trained GloVe vectors in order to benefit from the semantic and syntactic properties of the context words conveyed by these embeddings. That is to say, the separate spaces that the sense embeddings and the (context) word embeddings come from enforces some delay for the alignment of these spaces which in turn demands more training data. Furthermore, this early misalignment does not allow the BLSTM fully take advantage of larger context sizes which can be helpful. Our first attempt to deal with such problem was to pre-train the sense embeddings by some techniques - such as taking the average of the GloVe embeddings of the (informative) definition content words of senses, or taking the average of the GloVe embeddings of the (informative) context words in their training samples - did not give us a better result than our random initialization. Our preliminary experiments though in which we replaced all GloVe embeddings in the network with sense embeddings (using a method proposed by Chen et al. BIBREF11 ), showed considerable improvements in the results of some ambiguous words. That means both senses and context words (while they can be ambiguous by themselves) come from one vector space. In other words, the context would also be represented by the possible senses that its words can take. This idea not only can help to improve the results of the current model, it can also avoid the need for a large amount of training data since senses can be seen in both places, center and context, to be trained.

#### Relevance 984

Label: 1
> Reason
> - Summary of question: How many layers does the proposed model have?
> - Summary of passage: Sense and word embeddings have misaligned spaces that require more training.
> - Judgement: Its description of sense and word embeddings identifies lower-level model components relevant to reconstructing the architecture.
> 原因
> - 问题概述：所提模型共有多少层？
> - Passage 概述：义项和词嵌入空间不对齐，需要更多训练。
> - 判断：它描述义项和词嵌入，为还原架构中的底层组件提供线索。

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 988

Retrieved by: Hybrid RRF followed by BGE reranking

> Long Short-Term Memory (LSTM), introduced by Hochreiter and Schmidhuber (1997) BIBREF13 , is a gated recurrent neural network (RNN) architecture that has been designed to address the vanishing and exploding gradient problems of conventional RNNs. Unlike feedforward neural networks, RNNs have cyclic connections making them powerful for modeling sequences. A Bidirectional LSTM is made up of two reversed unidirectional LSTMs BIBREF14 . For WSD this means we are able to encode information of both preceding and succeeding words within context of an ambiguous word, which is necessary to correctly classify its sense.

#### Relevance 988

Label: 1
> Reason
> - Summary of question: How many layers does the proposed model have?
> - Summary of passage: A bidirectional LSTM combines two opposite-direction LSTMs.
> - Judgement: The two directional LSTM components help interpret the BLSTM portion of the architecture, without giving the total depth.
> 原因
> - 问题概述：所提模型共有多少层？
> - Passage 概述：双向 LSTM 组合两个方向相反的 LSTM。
> - 判断：两个方向的 LSTM 组件有助于理解架构中的 BLSTM 部分，虽未给出总层数。

## Question 0109

Paper: Arabic Offensive Language on Twitter: Analysis and Experiments

> How did they analyze which topics, dialects and gender are most associated with tweets?

### Common Retrieved Chunks

#### Passage 989

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Given the annotated tweets, we wanted to ascertain the distribution of: types of offensive language, genres where it is used, the dialects used, and the gender of users using such language.
> 
> Figure FIGREF13 shows the distribution of topics associated with offensive tweets. As the figure shows, sports and politics are most dominant for offensive language including vulgar and hate speech. As for dialect, we looked at MSA and four major dialects, namely Egyptian (EGY), Leventine (LEV), Maghrebi (MGR), and Gulf (GLF). Figure FIGREF14 shows that 71% of vulgar tweets were written in EGY followed by GLF, which accounted for 13% of vulgar tweets. MSA was not used in any of the vulgar tweets. As for offensive tweets in general, EGY and GLF were used in 36% and 35% of the offensive tweets respectively. Unlike the case of vulgar language where MSA was non-existent, 15% of the offensive tweets were in fact written in MSA. For hate speech, GLF and EGY were again dominant and MSA consistuted 21% of the tweets. This is consistent with findings for other languages such as English and Italian where vulgar language was more frequently associated with colloquial language BIBREF24, BIBREF25. Regarding the gender, Figure FIGREF15 shows that the vast majority of offensive tweets, including vulgar and hate speech, were authored by males. Female Twitter users accounted for 14% of offensive tweets in general and 6% and 9% of vulgar and hate speech respectively. Figure FIGREF16 shows a detailed categorization of hate speech types, where the top three include insulting groups based on their political ideology, origin, and sport affiliation. Religious hate speech appeared in only 15% of all hate speech tweets.
> 
> Next, we analyzed all tweets labeled as offensive to better understand how Arabic speakers use offensive language. Here is a breakdown of usage:
> 
> Direct name calling: The most frequent attack is to call a person an animal name, and the most used animals were كلب> (“klb” – “dog”), حمار> (“HmAr” – “donkey”), and بهيم> (“bhym” – “beast”). The second most common was insulting mental abilities using words such as غبي> (“gby” – “stupid”) and عبيط> (“EbyT” –“idiot”). Some culture-specific differences should be considered. Not all animal names are used

#### Relevance 989

Label: 1
> Reason
> - Summary of question: How are topic, dialect and gender associations with tweets analyzed?
> - Summary of passage: Annotated tweets are broken down by topic, dialect and author gender.
> - Judgement: It directly demonstrates distributional analysis and reports the dominant groups.
> 原因
> - 问题概述：如何分析推文与主题、方言和性别的关联？
> - Passage 概述：将已标注推文按主题、方言和作者性别分类统计。
> - 判断：它直接展示分布分析，并报告占主导的群体。

#### Passage 990

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Disclaimer: Due to the nature of the paper, some examples contain highly offensive language and hate speech. They don't reflect the views of the authors in any way, and the point of the paper is to help fight such speech. Much recent interest has focused on the detection of offensive language and hate speech in online social media. Such language is often associated with undesirable online behaviors such as trolling, cyberbullying, online extremism, political polarization, and propaganda. Thus, offensive language detection is instrumental for a variety of application such as: quantifying polarization BIBREF0, BIBREF1, trolls and propaganda account detection BIBREF2, detecting the likelihood of hate crimes BIBREF3; and predicting conflict BIBREF4. In this paper, we describe our methodology for building a large dataset of Arabic offensive tweets. Given that roughly 1-2% of all Arabic tweets are offensive BIBREF5, targeted annotation is essential for efficiently building a large dataset. Since our methodology does not use a seed list of offensive words, it is not biased by topic, target, or dialect. Using our methodology, we tagged 10,000 Arabic tweet dataset for offensiveness, where offensive tweets account for roughly 19% of the tweets. Further, we labeled tweets as vulgar or hate speech. To date, this is the largest available dataset, which we plan to make publicly available along with annotation guidelines. We use this dataset to characterize Arabic offensive language to ascertain the topics, dialects, and users' gender that are most associated with the use of offensive language. Though we suspect that there are common features that span different languages and cultures, some characteristics of Arabic offensive language is language and culture specific. Thus, we conduct a thorough analysis of how Arabic users use offensive language. Next, we use the dataset to train strong Arabic offensive language classifiers using state-of-the-art representations and classification techniques. Specifically, we experiment with static and contextualized embeddings for representation along with a variety of classifiers such as a deep neural network classifier and Support Vector Machine (SVM).
> 
> The contributions of this paper are as follows:
> 
> We built the largest Arabic offensive language dataset to date that includes special tags for vulgar language and hate speech. We describe the methodology for building it along

#### Relevance 990

Label: 1
> Reason
> - Summary of question: How are topic, dialect and gender associations with tweets analyzed?
> - Summary of passage: A 10,000-tweet annotated corpus is used to characterize topic, dialect and gender.
> - Judgement: It partially explains the analysis basis: an annotated corpus with offensive subtypes.
> 原因
> - 问题概述：如何分析推文与主题、方言和性别的关联？
> - Passage 概述：使用一万条已标注推文分析主题、方言和性别。
> - 判断：它部分说明分析依据，即带有冒犯子类别的已标注语料。

#### Passage 991

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this paper we presented a systematic method for building an Arabic offensive language tweet dataset that does not favor specific dialects, topics, or genres. We developed detailed guidelines for tagging the tweets as clean or offensive, including special tags for vulgar tweets and hate speech. We tagged 10,000 tweets, which we plan to release publicly and would constitute the largest available Arabic offensive language dataset. We characterized the offensive tweets in the dataset to determine the topics that illicit such language, the dialects that are most often used, the common modes of offensiveness, and the gender distribution of their authors. We performed this breakdown for offensive tweets in general and for vulgar and hate speech tweets separately. We believe that this is the first detailed analysis of its kind. Lastly, we conducted a large battery of experiments on the dataset, using cross-validation, to establish a strong system for Arabic offensive language detection. We showed that using static embeddings produced a competitive results on the dataset.
> 
> For future work, we plan to pursue several directions. First, we want explore target specific offensive language, where attacks against an entity or a group may employ certain expressions that are only offensive within the context of that target and completely innocuous otherwise. Second, we plan to examine the effectiveness of cross dialectal and cross lingual learning of offensive language.

#### Relevance 991

Label: 1
> Reason
> - Summary of question: How are topic, dialect and gender associations with tweets analyzed?
> - Summary of passage: Topic, dialect and gender breakdowns are computed separately for offensive subtypes.
> - Judgement: It states that the analysis uses separate category-wise breakdowns.
> 原因
> - 问题概述：如何分析推文与主题、方言和性别的关联？
> - Passage 概述：分别统计一般冒犯、粗俗和仇恨推文的主题、方言及性别分布。
> - 判断：它说明通过分类别统计进行分析。

#### Passage 992

Retrieved by: BM25, Dense, Hybrid RRF

> Our target was to build a large Arabic offensive language dataset that is representative of their appearance on Twitter and is hopefully not biased to specific dialects, topics, or targets. One of the main challenges is that offensive tweets constitute a very small portion of overall tweets. To quantify their proportion, we took 3 random samples of tweets from different days, with each sample composed of 1,000 tweets, and we found that between 1% and 2% of them were in fact offensive (including pornographic advertisement). This percentage is consistent with previously reported percentages BIBREF19. Thus, annotating random tweets is grossly inefficient. One way to overcome this problem is to use a seed list of offensive words to filter tweets. However, doing so is problematic as it would skew the dataset to particular types of offensive language or to specific dialects. Offensiveness is often dialect and country specific.
> 
> After inspecting many tweets, we observed that many offensive tweets have the vocative particle يا> (“yA” – meaning “O”), which is mainly used in directing the speech to a specific person or group. The ratio of offensive tweets increases to 5% if each tweet contains one vocative particle and to 19% if has at least two vocative particles. Users often repeat this particle for emphasis, as in: يا أمي يا حنونة> (“yA Amy yA Hnwnp” – O my mother, O kind one), which is endearing and non-offensive, and يا كلب يا قذر> (“yA klb yA q*r” – “O dog, O dirty one”), which is offensive. We decided to use this pattern to increase our chances of finding offensive tweets. One of the main advantages of the pattern يا ... يا> (“yA ... yA”) is that it is not associated with any specific topic or genre, and it appears in all Arabic dialects. Though the use of offensive language does not necessitate the appearance of the vocative particle, the particle does not favor any specific offensive expressions and greatly improves our chances of finding offensive tweets. It is clear, the dataset is more biased toward positive class. Using the dataset for real-life application may require de-biasing it by boosting negative class or random sampling additional data from Twitter BIBREF22.Using

#### Relevance 992

Label: 1
> Reason
> - Summary of question: How are topic, dialect and gender associations with tweets analyzed?
> - Summary of passage: Repeated vocative particles guide offensive-tweet sampling.
> - Judgement: The sampling strategy explains how topic and dialect bias are reduced before association analysis.
> 原因
> - 问题概述：如何分析推文与主题、方言和性别的关联？
> - Passage 概述：通过重复呼语助词筛选冒犯推文。
> - 判断：采样策略说明在关联分析前如何减少主题和方言偏差。

#### Passage 993

Retrieved by: BM25, Dense, Hybrid RRF

> improves our chances of finding offensive tweets. It is clear, the dataset is more biased toward positive class. Using the dataset for real-life application may require de-biasing it by boosting negative class or random sampling additional data from Twitter BIBREF22.Using the Twitter API, we collected 660k Arabic tweets having this pattern between April 15, 2019 and May 6, 2019. To increase diversity, we sorted the word sequences between the vocative particles and took the most frequent 10,000 unique sequences. For each word sequence, we took a random tweet containing each sequence. Then we annotated those tweets, ending up with 1,915 offensive tweets which represent roughly 19% of all tweets. Each tweet was labeled as: offensive, which could additionally be labeled as vulgar and/or hate speech, or Clean. We describe in greater detail our annotation guidelines, which we made sure that they are compatible with the OffensEval2019 annotation guidelines BIBREF15. For example, if a tweet has insults or threats targeting a group based on their nationality, ethnicity, gender, political affiliation, religious belief, or other common characteristics, this is considered as hate speech BIBREF15. It is worth mentioning that we also considered insulting groups based on their sport affiliation as a form of hate speech. In most Arab countries, being a fan of a particularly sporting club is considered as part of the personality and ideology which rarely changes over time (similar to political affiliation). Many incidents of violence have occurred among fans of rival clubs.

#### Relevance 993

Label: 1
> Reason
> - Summary of question: How are topic, dialect and gender associations with tweets analyzed?
> - Summary of passage: Tweets are sampled and labeled as offensive, vulgar, hate speech or clean.
> - Judgement: The sampling and offensive-subtype labels explain the groups on which later association breakdowns are based.
> 原因
> - 问题概述：如何分析推文与主题、方言和性别的关联？
> - Passage 概述：对推文采样并标注冒犯、粗俗、仇恨或干净类别。
> - 判断：采样方式和冒犯子类别标签说明后续关联统计所依据的分组。

### BM25

None

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 994

Retrieved by: Hybrid RRF followed by BGE reranking

> had two types:
> 
> [leftmargin=*]
> 
> Mixture of offensiveness and admiration: ex. calling a girl a puppy يا كلبوبة> (“yA klbwbp” – “O puppy”) in a flirtatious manner.
> 
> Implicit offensiveness: ex. calling for cure while implying sanity in: وتشفي حكام قطر من المرض> (“wt$fy HkAm qTr mn AlmrD” – “and cure Qatar rulers from illness”).
> 
> Many errors stem from heavy use of dialectal Arabic as well as ambiguity. Since BERT was trained on Wikipedia (MSA) and Google books, the model failed to classify tweets with dialectal cues. Conversely, Mazajak/SVM is more biased towards dialects, often failing to classify MSA tweets.

#### Relevance 994

Label: 1
> Reason
> - Summary of question: How are topic, dialect and gender associations with tweets analyzed?
> - Summary of passage: Classifier errors involve ambiguity and dialectal versus standard Arabic.
> - Judgement: Its dialect-specific error analysis supplies further evidence about dialect associations in the tweet data.
> 原因
> - 问题概述：如何分析推文与主题、方言和性别的关联？
> - Passage 概述：分类器错误涉及歧义及方言与标准阿拉伯语差异。
> - 判断：方言相关的错误分析为推文数据中的方言关联提供补充证据。

#### Passage 995

Retrieved by: Hybrid RRF followed by BGE reranking

> الله يلعنك> (“Allh ylEnk” – “may Allah/God curse you”), and روح في داهية> (“rwH fy dAhyp” – equivalent to “go to hell”).
> 
> Name alteration: One common way to insult others is to change a letter or two in their names to produce new offensive words that rhyme with the original names. Some examples of such include changing الجزيرة> (“Aljzyrp” – “Aljazeera (channel)”) to الخنزيرة> (“Alxnzyrp” – “the pig”) and خلفان> (“xlfAn” – “Khalfan (person name)”) to خرفان> (“xrfAn” – “crazed”).
> 
> Societal stratification: Some insults are associated with: certain jobs such as بواب> (“bwAb” – “doorman”) or خادم> (“xAdm” – “servant”); and specific societal components such بدوي> (“bdwy” – “bedouin”) and فلاح> (“flAH” – “farmer”).
> 
> Immoral behavior: These insults are associated with negative moral traits or behaviors such as حقير> (“Hqyr” – “vile”), خاين> (“xAyn” – “traitor”), and منافق> (“mnAfq” – “hypocrite”).
> 
> Sexually related: They include expressions such as خول> (“xwl” – “gay”), وسخة> (“wsxp” – “prostitute”), and عرص> (“ErS” – “pimp”).
> 
> Figure FIGREF17 shows top words with the highest valance score for individual words in the offensive tweets. Larger fonts are used to highlight words with highest score and align as well with the categories mentioned ahead in the breakdown for the offensive languages. We modified the valence score described by BIBREF1 conover2011political to magnify its value based on frequency of occurrence. The score is computed as follows:
> 
> $V(I) = 2 \frac{ \frac{tf(I, C_off)}{total(C_off)}}{\frac{tf(I, C_off)}{total(C_off)} + \frac{tf(I, C_cln)}{total(C_cln)} } - 1$
> 
> where
> 
> $tf(I, C_i) = \sum _{a \in I \bigcap C_i} [ln(Cnt(a, C_i)) + 1]$
> 
> $total(C_i) = \sum _{I} tf(I, C_i)$
> 
> $Cnt(a, C_i)$ is the number of times word $a$ was used in offensive or clean tweets tweets $C_i$. In essence, we are replacing term frequencies with the natural log of the term frequencies.

#### Relevance 995

Label: 1
> Reason
> - Summary of question: How are topic, dialect and gender associations with tweets analyzed?
> - Summary of passage: Insult types and a word-level valence score are described.
> - Judgement: The lexical-category and valence analysis provides complementary clues to how offensive-tweet patterns are characterized.
> 原因
> - 问题概述：如何分析推文与主题、方言和性别的关联？
> - Passage 概述：介绍辱骂类型和词级倾向分数。
> - 判断：词汇类别和倾向分析补充说明如何刻画冒犯推文的模式。

## Question 0110

Paper: Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks

> What transfer learning tasks are evaluated?

### Common Retrieved Chunks

#### Passage 996

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> SentEval BIBREF6 is a popular toolkit to evaluate the quality of sentence embeddings. Sentence embeddings are used as features for a logistic regression classifier. The logistic regression classifier is trained on various tasks in a 10-fold cross-validation setup and the prediction accuracy is computed for the test-fold.
> 
> The purpose of SBERT sentence embeddings are not to be used for transfer learning for other tasks. Here, we think fine-tuning BERT as described by devlin2018bert for new tasks is the more suitable method, as it updates all layers of the BERT network. However, SentEval can still give an impression on the quality of our sentence embeddings for various tasks.
> 
> We compare the SBERT sentence embeddings to other sentence embeddings methods on the following seven SentEval transfer tasks:
> 
> MR: Sentiment prediction for movie reviews snippets on a five start scale BIBREF25.
> 
> CR: Sentiment prediction of customer product reviews BIBREF26.
> 
> SUBJ: Subjectivity prediction of sentences from movie reviews and plot summaries BIBREF27.
> 
> MPQA: Phrase level opinion polarity classification from newswire BIBREF28.
> 
> SST: Stanford Sentiment Treebank with binary labels BIBREF29.
> 
> TREC: Fine grained question-type classification from TREC BIBREF30.
> 
> MRPC: Microsoft Research Paraphrase Corpus from parallel news sources BIBREF31.
> 
> The results can be found in Table TABREF15. SBERT is able to achieve the best performance in 5 out of 7 tasks. The average performance increases by about 2 percentage points compared to InferSent as well as the Universal Sentence Encoder. Even though transfer learning is not the purpose of SBERT, it outperforms other state-of-the-art sentence embeddings methods on this task.
> 
> It appears that the sentence embeddings from SBERT capture well sentiment information: We observe large improvements for all sentiment tasks (MR, CR, and SST) from SentEval in comparison to InferSent and Universal Sentence Encoder.
> 
> The only dataset where SBERT is significantly worse than Universal Sentence Encoder is the TREC dataset. Universal Sentence Encoder was pre-trained on question-answering data, which appears to be beneficial for the question-type classification task of the TREC dataset.
> 
> Average BERT embeddings or using the CLS-token output from a BERT network achieved bad results for various STS tasks (Table TABREF6), worse than average GloVe embeddings. However, for SentEval, average BERT embeddings and the BERT CLS-token output achieves decent

#### Relevance 996

Label: 1
> Reason
> - Summary of question: Which transfer-learning tasks are evaluated?
> - Summary of passage: SentEval evaluates MR, CR, SUBJ, MPQA, SST, TREC and MRPC.
> - Judgement: It explicitly lists and describes all seven transfer tasks.
> 原因
> - 问题概述：评估了哪些迁移学习任务？
> - Passage 概述：SentEval 评估 MR、CR、SUBJ、MPQA、SST、TREC 和 MRPC。
> - 判断：它明确列出并解释七项迁移任务。

#### Passage 997

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> dataset.
> 
> Average BERT embeddings or using the CLS-token output from a BERT network achieved bad results for various STS tasks (Table TABREF6), worse than average GloVe embeddings. However, for SentEval, average BERT embeddings and the BERT CLS-token output achieves decent results (Table TABREF15), outperforming average GloVe embeddings. The reason for this are the different setups. For the STS tasks, we used cosine-similarity to estimate the similarities between sentence embeddings. Cosine-similarity treats all dimensions equally. In contrast, SentEval fits a logistic regression classifier to the sentence embeddings. This allows that certain dimensions can have higher or lower impact on the classification result.
> 
> We conclude that average BERT embeddings / CLS-token output from BERT return sentence embeddings that are infeasible to be used with cosine-similarity or with Manhatten / Euclidean distance. For transfer learning, they yield slightly worse results than InferSent or Universal Sentence Encoder. However, using the described fine-tuning setup with a siamese network structure on NLI datasets yields sentence embeddings that achieve a new state-of-the-art for the SentEval toolkit.

#### Relevance 997

Label: 1
> Reason
> - Summary of question: Which transfer-learning tasks are evaluated?
> - Summary of passage: SentEval classification and STS similarity evaluation use different setups.
> - Judgement: It identifies SentEval's classifier-based transfer evaluation, helping interpret the task list in other passages.
> 原因
> - 问题概述：评估了哪些迁移学习任务？
> - Passage 概述：SentEval 分类与 STS 相似度评估采用不同设置。
> - 判断：它指出 SentEval 基于分类器的迁移评估方式，有助于理解其他片段中的任务列表。

#### Passage 999

Retrieved by: BM25, Dense, Hybrid RRF

> We have demonstrated strong empirical results for the quality of SBERT sentence embeddings. In this section, we perform an ablation study of different aspects of SBERT in order to get a better understanding of their relative importance.
> 
> We evaluated different pooling strategies (MEAN, MAX, and CLS). For the classification objective function, we evaluate different concatenation methods. For each possible configuration, we train SBERT with 10 different random seeds and average the performances.
> 
> The objective function (classification vs. regression) depends on the annotated dataset. For the classification objective function, we train SBERT-base on the SNLI and the Multi-NLI dataset. For the regression objective function, we train on the training set of the STS benchmark dataset. Performances are measured on the development split of the STS benchmark dataset. Results are shown in Table TABREF23.
> 
> When trained with the classification objective function on NLI data, the pooling strategy has a rather minor impact. The impact of the concatenation mode is much larger. InferSent BIBREF4 and Universal Sentence Encoder BIBREF5 both use $(u, v, |u-v|, u*v)$ as input for a softmax classifier. However, in our architecture, adding the element-wise $u*v$ decreased the performance.
> 
> The most important component is the element-wise difference $|u-v|$. Note, that the concatenation mode is only relevant for training the softmax classifier. At inference, when predicting similarities for the STS benchmark dataset, only the sentence embeddings $u$ and $v$ are used in combination with cosine-similarity. The element-wise difference measures the distance between the dimensions of the two sentence embeddings, ensuring that similar pairs are closer and dissimilar pairs are further apart.
> 
> When trained with the regression objective function, we observe that the pooling strategy has a large impact. There, the MAX strategy perform significantly worse than MEAN or CLS-token strategy. This is in contrast to BIBREF4, who found it beneficial for the BiLSTM-layer of InferSent to use MAX instead of MEAN pooling.

#### Relevance 999

Label: 1
> Reason
> - Summary of question: Which transfer-learning tasks are evaluated?
> - Summary of passage: Ablations train on NLI or STS and vary pooling and concatenation.
> - Judgement: NLI and STS training ablations clarify the source and target tasks relevant to interpreting transfer evaluation.
> 原因
> - 问题概述：评估了哪些迁移学习任务？
> - Passage 概述：消融在 NLI 或 STS 上训练，并改变池化和拼接。
> - 判断：NLI 与 STS 训练消融说明理解迁移评价所需的源任务与目标任务。

#### Passage 1000

Retrieved by: BM25, Hybrid RRF

> We first introduce BERT, then, we discuss state-of-the-art sentence embedding methods.
> 
> BERT BIBREF0 is a pre-trained transformer network BIBREF9, which set for various NLP tasks new state-of-the-art results, including question answering, sentence classification, and sentence-pair regression. The input for BERT for sentence-pair regression consists of the two sentences, separated by a special [SEP] token. Multi-head attention over 12 (base-model) or 24 layers (large-model) is applied and the output is passed to a simple regression function to derive the final label. Using this setup, BERT set a new state-of-the-art performance on the Semantic Textual Semilarity (STS) benchmark BIBREF10. RoBERTa BIBREF1 showed, that the performance of BERT can further improved by small adaptations to the pre-training process. We also tested XLNet BIBREF11, but it led in general to worse results than BERT.
> 
> A large disadvantage of the BERT network structure is that no independent sentence embeddings are computed, which makes it difficult to derive sentence embeddings from BERT. To bypass this limitations, researchers passed single sentences through BERT and then derive a fixed sized vector by either averaging the outputs (similar to average word embeddings) or by using the output of the special CLS token (for example: bertsentenceembeddings1,bertsentenceembeddings2,bertsentenceembeddings3). These two options are also provided by the popular bert-as-a-service-repository. Up to our knowledge, there is so far no evaluation if these methods lead to useful sentence embeddings.
> 
> Sentence embeddings are a well studied area with dozens of proposed methods. Skip-Thought BIBREF12 trains an encoder-decoder architecture to predict the surrounding sentences. InferSent BIBREF4 uses labeled data of the Stanford Natural Language Inference dataset BIBREF13 and the Multi-Genre NLI dataset BIBREF14 to train a siamese BiLSTM network with max-pooling over the output. Conneau et al. showed, that InferSent consistently outperforms unsupervised methods like SkipThought. Universal Sentence Encoder BIBREF5 trains a transformer network and augments unsupervised learning with training on SNLI. hill-etal-2016-learning showed, that the task on which sentence embeddings are trained significantly impacts their quality. Previous work BIBREF4, BIBREF5 found that the SNLI datasets are suitable for training sentence embeddings. yang-2018-learning presented a method to train on conversations from Reddit using siamese DAN and siamese transformer networks, which yielded good results on the STS benchmark dataset.
> 
> polyencoders addresses the run-time

#### Relevance 1000

Label: 1
> Reason
> - Summary of question: Which transfer-learning tasks are evaluated?
> - Summary of passage: Related work describes BERT and other sentence-embedding models.
> - Judgement: Prior sentence-embedding tasks provide context for the task families used to assess transferred representations.
> 原因
> - 问题概述：评估了哪些迁移学习任务？
> - Passage 概述：相关工作介绍 BERT 和其他句子嵌入模型。
> - 判断：既有句嵌入任务为评价迁移表示所用的任务类别提供背景。

#### Passage 1001

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> The STS benchmark (STSb) BIBREF10 provides is a popular dataset to evaluate supervised STS systems. The data includes 8,628 sentence pairs from the three categories captions, news, and forums. It is divided into train (5,749), dev (1,500) and test (1,379). BERT set a new state-of-the-art performance on this dataset by passing both sentences to the network and using a simple regression method for the output.
> 
> We use the training set to fine-tune SBERT using the regression objective function. At prediction time, we compute the cosine-similarity between the sentence embeddings. All systems are trained with 10 random seeds to counter variances BIBREF23.
> 
> The results are depicted in Table TABREF10. We experimented with two setups: Only training on STSb, and first training on NLI, then training on STSb. We observe that the later strategy leads to a slight improvement of 1-2 points. This two-step approach had an especially large impact for the BERT cross-encoder, which improved the performance by 3-4 points. We do not observe a significant difference between BERT and RoBERTa.

#### Relevance 1001

Label: 1
> Reason
> - Summary of question: Which transfer-learning tasks are evaluated?
> - Summary of passage: SBERT is fine-tuned and evaluated on the STS benchmark.
> - Judgement: It describes transfer from NLI training to STS fine-tuning, providing a related evaluated transfer setting.
> 原因
> - 问题概述：评估了哪些迁移学习任务？
> - Passage 概述：在 STS 基准上微调和评估 SBERT。
> - 判断：它描述从 NLI 训练迁移到 STS 微调，提供相关迁移评估设置。

#### Passage 1002

Retrieved by: Dense, Hybrid RRF

> We evaluate the performance of SBERT for STS without using any STS specific training data. We use the STS tasks 2012 - 2016 BIBREF16, BIBREF17, BIBREF18, BIBREF19, BIBREF20, the STS benchmark BIBREF10, and the SICK-Relatedness dataset BIBREF21. These datasets provide labels between 0 and 5 on the semantic relatedness of sentence pairs. We showed in BIBREF22 that Pearson correlation is badly suited for STS. Instead, we compute the Spearman's rank correlation between the cosine-similarity of the sentence embeddings and the gold labels. The setup for the other sentence embedding methods is equivalent, the similarity is computed by cosine-similarity. The results are depicted in Table TABREF6.
> 
> The results shows that directly using the output of BERT leads to rather poor performances. Averaging the BERT embeddings achieves an average correlation of only 54.81, and using the CLS-token output only achieves an average correlation of 29.19. Both are worse than computing average GloVe embeddings.
> 
> Using the described siamese network structure and fine-tuning mechanism substantially improves the correlation, outperforming both InferSent and Universal Sentence Encoder substantially. The only dataset where SBERT performs worse than Universal Sentence Encoder is SICK-R. Universal Sentence Encoder was trained on various datasets, including news, question-answer pages and discussion forums, which appears to be more suitable to the data of SICK-R. In contrast, SBERT was pre-trained only on Wikipedia (via BERT) and on NLI data.
> 
> While RoBERTa was able to improve the performance for several supervised tasks, we only observe minor difference between SBERT and SRoBERTa for generating sentence embeddings.

#### Relevance 1002

Label: 1
> Reason
> - Summary of question: Which transfer-learning tasks are evaluated?
> - Summary of passage: Unsupervised STS evaluation uses STS 2012–2016, STSb and SICK-R.
> - Judgement: The named STS benchmarks show where NLI-trained sentence embeddings are evaluated without task-specific training.
> 原因
> - 问题概述：评估了哪些迁移学习任务？
> - Passage 概述：无监督 STS 评估使用 STS 2012–2016、STSb 和 SICK-R。
> - 判断：具名 STS 基准说明 NLI 训练的句子嵌入在无任务专属训练时接受哪些评估。

### BM25

#### Passage 998

Retrieved by: BM25

> We showed that BERT out-of-the-box maps sentences to a vector space that is rather unsuitable to be used with common similarity measures like cosine-similarity. The performance for seven STS tasks was below the performance of average GloVe embeddings.
> 
> To overcome this shortcoming, we presented Sentence-BERT (SBERT). SBERT fine-tunes BERT in a siamese / triplet network architecture. We evaluated the quality on various common benchmarks, where it could achieve a significant improvement over state-of-the-art sentence embeddings methods. Replacing BERT with RoBERTa did not yield a significant improvement in our experiments.
> 
> SBERT is computationally efficient. On a GPU, it is about 9% faster than InferSent and about 55% faster than Universal Sentence Encoder. SBERT can be used for tasks which are computationally not feasible to be modeled with BERT. For example, clustering of 10,000 sentences with hierarchical clustering requires with BERT about 65 hours, as around 50 Million sentence combinations must be computed. With SBERT, we were able to reduce the effort to about 5 seconds.

#### Relevance 998

Label: 1
> Reason
> - Summary of question: Which transfer-learning tasks are evaluated?
> - Summary of passage: SBERT improves embedding quality and clustering efficiency.
> - Judgement: Similarity and clustering benchmarks give partial task-level clues about where learned sentence representations are evaluated.
> 原因
> - 问题概述：评估了哪些迁移学习任务？
> - Passage 概述：SBERT 改善嵌入质量和聚类效率。
> - 判断：相似度与聚类基准为学习所得句表示的评价任务提供部分线索。

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1003

Retrieved by: Hybrid RRF followed by BGE reranking

> We evaluate the performance of SBERT for common Semantic Textual Similarity (STS) tasks. State-of-the-art methods often learn a (complex) regression function that maps sentence embeddings to a similarity score. However, these regression functions work pair-wise and due to the combinatorial explosion those are often not scalable if the collection of sentences reaches a certain size. Instead, we always use cosine-similarity to compare the similarity between two sentence embeddings. We ran our experiments also with negative Manhatten and negative Euclidean distances as similarity measures, but the results for all approaches remained roughly the same.

#### Relevance 1003

Label: 1
> Reason
> - Summary of question: Which transfer-learning tasks are evaluated?
> - Summary of passage: STS evaluation compares embeddings with cosine similarity and other distances.
> - Judgement: It identifies semantic textual similarity as an evaluated task, supplying partial task-level evidence.
> 原因
> - 问题概述：评估了哪些迁移学习任务？
> - Passage 概述：STS 评估使用余弦相似度及其他距离比较嵌入。
> - 判断：它指出语义文本相似度这一评估任务，提供部分任务线索。

#### Passage 1004

Retrieved by: Hybrid RRF followed by BGE reranking

> same claims and provide the same reasoning. BERT is able to use attention to compare directly both sentences (e.g. word-by-word comparison), while SBERT must map individual sentences from an unseen topic to a vector space such that arguments with similar claims and reasons are close. This is a much more challenging task, which appears to require more than just two topics for training to work on-par with BERT.

#### Relevance 1004

Label: 1
> Reason
> - Summary of question: Which transfer-learning tasks are evaluated?
> - Summary of passage: Argument similarity across unseen topics is challenging for SBERT.
> - Judgement: It describes argument similarity on unseen topics, a partial clue to cross-topic transfer evaluation.
> 原因
> - 问题概述：评估了哪些迁移学习任务？
> - Passage 概述：SBERT 难以处理未见主题上的论证相似度。
> - 判断：它描述未见主题上的论证相似度，为跨主题迁移评估提供部分线索。

## Question 0111

Paper: Towards Better Understanding of Spontaneous Conversations: Overcoming Automatic Speech Recognition Errors With Intent Recognition

> How do they use extracted intent to rescore?

### Common Retrieved Chunks

#### Passage 1005

Retrieved by: BM25, Hybrid RRF

> A commonly known limitation of the current ASR systems is their inability to recognize long sequences of words precisely. In this paper, we propose a new method of incorporating domain knowledge into automatic speech recognition which alleviates this weakness. Our approach allows performing fast ASR domain adaptation by providing a library of intent examples used for lattice rescoring. The method guides the best lattice path selection process by increasing the probability of intent recognition. At the same time, the method does not rescore paths of unessential turns which do not contain intent examples. As a result, our approach improves the understanding of spontaneous conversations by recognizing semantically important transcription segments while adding minimal computational overhead. Our method is domain agnostic and can be easily adapted to a new one by providing the library of intent examples expected to appear in the new domain. The increased intent annotation coverage allows us to train more sophisticated models for downstream tasks, opening the prospects of true spoken language understanding.

#### Relevance 1005

Label: 1
> Reason
> - Summary of question: How are recognized intents used for ASR rescoring?
> - Summary of passage: Intent examples guide best lattice-path selection; non-intent turns are unchanged.
> - Judgement: It directly summarizes how intent evidence guides rescoring.
> 原因
> - 问题概述：如何利用识别出的意图对语音识别结果重新评分？
> - Passage 概述：意图示例引导最优词图路径选择，无意图的话轮不调整。
> - 判断：它直接概述意图证据如何指导重新评分。

#### Passage 1007

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this section, we present a quantitative analysis of the proposed algorithm. The baseline algorithm annotates only the best ASR hypothesis. We perform the experiments with an intent library comprised of 313 intents in total, each of which is expressed using 169 examples on average. The annotations are performed on more than 70 000 US English phone conversations with an average duration of 11 minutes, but some of them take even over one hour. The topics of these conversations span across several domains, such as inquiry for account information or instructions, refund requests or service cancellations. Each domain uses a relevant subset of the intent library (typically 100-150 intents are active).
> 
> To evaluate the effectiveness of the proposed algorithm, we have sampled a dataset of 500 rescored intent annotations found in the lattices in cancellations and refunds domain. The correctness of the rescoring was judged by two annotators, who labeled 250 examples each. The annotators read the whole conversation transcript and listened to the recording to establish whether the rescoring is meaningful. In cases when a rescored word was technically incorrect (e.g., mistaken tense of a verb), but the rescoring led to the recognition of the correct intent, we labeled the intent annotation as correct. The results are shown in Table TABREF22. Please note that every result above 50% indicates an improvement over the ASR best path recognition, since we correct more ASR errors than we introduce new mistakes.
> 
> The results confirm our assumptions presented in Section SECREF20. The longer the intent annotation, the more likely it is to be correct due to stronger contextuality of the annotation. Intent annotations which span at least three words are more likely to rescore the lattice correctly than to introduce a false positive. These results also lead us to a practical heuristic, that an intent annotation which spans only one or two words should not be considered for rescoring. Application of this heuristic results in an estimated accuracy of 77%. We use this heuristic in further experiments. A stricter heuristic would require at least four words span, with an accuracy of 87.7%. Calibration of this threshold is helpful when the algorithm is adapted to a downstream task, where

#### Relevance 1007

Label: 1
> Reason
> - Summary of question: How are recognized intents used for ASR rescoring?
> - Summary of passage: Rescoring ignores intent annotations spanning only one or two words.
> - Judgement: It gives an explicit heuristic controlling which intent matches can trigger rescoring.
> 原因
> - 问题概述：如何利用识别出的意图对语音识别结果重新评分？
> - Passage 概述：重新评分时忽略仅覆盖一两个词的意图标注。
> - 判断：它给出决定哪些意图匹配可触发重新评分的明确规则。

#### Passage 1008

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> $n$ of filler words can be inserted between words constituting an intent example, while still allowing to match the intent annotation. We add wildcard arcs between each of the intent-matching words, to provide the matching capacity of 0 to $n$ matches of any word in the alphabet. The example of such an index is shown in Figure FIGREF15.
> 
> The naive implementation allowing for $n$ superfluous (non-intent) words appearing between intent-matching words would lead to a significant explosion of the annotations spans. Instead, we employ a post-processing filtering step to prune lattice paths where the number of allowed non-intent word is exceeded. Our filtering step has a computational complexity of $\mathcal {O}(|S| + |A|)$, where $|S|$ is the number of states and $|A|$ is the number of arcs in the non-pruned annotated lattice $\mathcal {L^{\prime }}$.
> 
> The pruning algorithm is based on the depth-first search (DFS) traversal of the lattice $\mathcal {L^{\prime }}$ and marks each state in $\mathcal {L^{\prime }}$ as either new, visited, or pruned. Only new states are entered and each state is entered at most once. The FST arcs are only marked as either visited or pruned. Each FST state keeps track of whether an intent annotation parsing has begun (i.e., a begin symbol $\iota _B$ has been encountered but the end symbol $\iota _E$ has not appeared yet) and how many wildcard words have been matched so far.
> 
> The traversal of the lattice $\mathcal {L^{\prime }}$ is stateful. It starts in a non-matching state and remains in this state until encountering the intent begin symbol $\iota _B$. Then the state becomes matching and remains such until encountering the intent end symbol $\iota _E$. A state is marked as pruned when the traversal state is matching and the number of wildcard words exceeds the blank quota for the given intent example. Any arc incident with a pruned state is not entered during further traversal, leading to a significant speed-up of lattice processing. After every possible path in the lattice $\mathcal {L^{\prime }}$ has been either traversed or pruned, all redundant (i.e., pruned or not visited) FST states are removed from the lattice, along with all incident arcs.
> 
> The annotated lattice $\mathcal {A}$

#### Relevance 1008

Label: 1
> Reason
> - Summary of question: How are recognized intents used for ASR rescoring?
> - Summary of passage: Wildcard matching and DFS pruning remove paths exceeding filler-word quotas.
> - Judgement: It describes how intent constraints filter candidate paths before final selection.
> 原因
> - 问题概述：如何利用识别出的意图对语音识别结果重新评分？
> - Passage 概述：通配符匹配和深度优先剪枝删除填充词超限路径。
> - 判断：它说明意图约束如何在最终选择前过滤候选路径。

#### Passage 1009

Retrieved by: BM25, Dense, Hybrid RRF

> The lattice $\mathcal {L}$ is an acceptor, where each arc contains a symbol representing a single word in the current hypothesis (see Figure FIGREF12). We employ a closed ASR vocabulary assumption and operate on word-level, rather than character- or phoneme- level FST. Note that this assumption is not a limitation of our method. Should the ASR have an unlimited vocabulary (as some end-to-end ASR systems do), it is possible to dynamically construct the lattice symbol table and merge it with the symbol table of intent definitions.
> 
> To perform intent annotation (i.e., to recognize and mark the position of intent instances in the transcript), we first create the FST index $\mathcal {I}$ of all intent examples. This index is a transducer which maps the alphabet of words (input symbols) onto the alphabet of intents (output symbols). We construct index $\mathcal {I}$ in such a way that its composition with the lattice results in another transducer $\mathcal {A} = \mathcal {L} \circ \mathcal {I}$ representing the annotated lattice.
> 
> We begin by creating a single FST state which serves as both the initial and the final state and contains a single loop wildcard arc. A wildcard arc accepts any input symbol and transduces it to an empty $\epsilon $ output symbol. The wildcard arc can be efficiently implemented with special $\sigma $-matchers, available in the OpenFST framework BIBREF47. Composition with the singleton FST maps every input symbol in $\mathcal {L}$ to $\epsilon $, which denotes the lack of intent annotations. For each intent example, we construct an additional branch (i.e. a set of paths) in the index $\mathcal {I}$ which maps multiple sequences of words to a set of symbols representing this particular intent example (see Figure FIGREF13).
> 
> We use three types of symbols: an intent symbol $\iota $ (including begin $\iota _B$, continuation $\iota _C$ and end $\iota _E$ symbols), an entity symbol $\omega $ (including an entity placeholder symbol $\omega ^*$), and a null symbol $\epsilon $.
> 
> The intent symbol $\iota $ is the delimiter of the intent annotation and it demarcates the words constituting the intent. The begin ($\iota _B$) and continuation ($\iota _C$) symbols are mapped onto arcs with words as input symbols, and

#### Relevance 1009

Label: 1
> Reason
> - Summary of question: How are recognized intents used for ASR rescoring?
> - Summary of passage: An intent-example FST is composed with the ASR lattice to mark matching paths.
> - Judgement: It explains the intent-annotation step that supplies path evidence for rescoring.
> 原因
> - 问题概述：如何利用识别出的意图对语音识别结果重新评分？
> - Passage 概述：将意图示例有限状态转换器与语音词图组合，标记匹配路径。
> - 判断：它解释为重新评分提供路径证据的意图标注步骤。

#### Passage 1011

Retrieved by: Dense, Hybrid RRF

> $.
> 
> The intent symbol $\iota $ is the delimiter of the intent annotation and it demarcates the words constituting the intent. The begin ($\iota _B$) and continuation ($\iota _C$) symbols are mapped onto arcs with words as input symbols, and the end ($\iota _E$) symbol is inserted in an additional arc with an $\epsilon $ input symbol after the annotated fragment of text. It is important that the begin symbol $\iota _B$ does not introduce an extra input of $\epsilon $. Otherwise, the FST composition is inefficient, as it tries to enter this path on every arc in the lattice $\mathcal {L}$.
> 
> The entity symbol $\omega $ marks the presence of an entity in the intent annotation. Each entity in the intent index $\mathcal {I}$ is constructed as a non-terminal entity placeholder $\omega ^*$, which allows using the FST lazy replacement algorithm to enter a separate FST grammar ${E}$ describing a set of possible values for a given entity. We use the ${E}$ transducer when it is possible to provide a comprehensive list of entity instances. Otherwise, we provide an approximation of this list by running a named entity recognition model predictions on an n-best list (see Figure FIGREF14). Finally, the null symbol $\epsilon $ means that either no intent was recognized, or the word spanned by the intent annotation did not contribute to the annotation itself.
> 
> This procedure successfully performs exact matching of the transcription to intent index, when all words present in the current lattice path are also found in the intent example. Unfortunately, this approach is highly impractical when real transcriptions are considered. Sequences of significant words are interwoven with filler phonemes and words, for instance the utterance "I want uhm to order like um three yyh three tickets" could not be matched with the intent example "I want to order __NUMBER__ tickets".
> 
> To overcome this limitation we adapt the intent index $\mathcal {I}$ to enable fuzzy matching so that some number $n$ of filler words can be inserted between words constituting an intent example, while still allowing to match the intent annotation. We add wildcard arcs between each of the intent-matching words, to provide the matching capacity of 0 to $n$

#### Relevance 1011

Label: 1
> Reason
> - Summary of question: How are recognized intents used for ASR rescoring?
> - Summary of passage: Intent boundaries, entity placeholders and fuzzy matching annotate lattice paths.
> - Judgement: It provides matching mechanics used to obtain intent evidence for rescoring.
> 原因
> - 问题概述：如何利用识别出的意图对语音识别结果重新评分？
> - Passage 概述：意图边界、实体占位符和模糊匹配用于标注词图路径。
> - 判断：它提供获取重新评分所需意图证据的匹配机制。

### BM25

#### Passage 1006

Retrieved by: BM25

> The power of some of the best conversational assistants lies in domain-dependent human knowledge. Amazon's Alexa is improving with the user generated data it gathers BIBREF10. Some of the most common human knowledge base structures used in NLP are word lists such as dictionaries for ASR BIBREF11, sentiment lexicons BIBREF12 knowledge graphs such as WordNet BIBREF13, BIBREF14 and ConceptNet BIBREF15. Conceptually, our work is similar to BIBREF16, however, they do not allow for fuzzy search through the lattice.

#### Relevance 1006

Label: 1
> Reason
> - Summary of question: How are recognized intents used for ASR rescoring?
> - Summary of passage: Human knowledge resources and related fuzzy-search work are discussed.
> - Judgement: The comparison with prior lattice search clarifies that fuzzy matching is a component of the proposed rescoring approach.
> 原因
> - 问题概述：如何利用识别出的意图对语音识别结果重新评分？
> - Passage 概述：讨论人工知识资源和相关模糊搜索研究。
> - 判断：与既有词图搜索的比较说明模糊匹配是所提重新评分方法的一部分。

### Dense

#### Passage 1010

Retrieved by: Dense

> of 77%. We use this heuristic in further experiments. A stricter heuristic would require at least four words span, with an accuracy of 87.7%. Calibration of this threshold is helpful when the algorithm is adapted to a downstream task, where a different precision/recall ratio may be required. We present some examples of successful lattice rescoring in Table TABREF19.
> 
> The proposed algorithm finds 658 549 intents in all conversations, covering 4.1% of all (62 450 768) words, whereas the baseline algorithm finds 526 356 intents, covering 3.3% of all words. Therefore, the increase in intent recognition of the method is 25.1% by rescoring 8.3% of all annotated words (0.34% of all words). Particular intents achieve different improvements ranging from no improvement up to 1062% – ranked percentile results are presented in Table TABREF23. We see that half of intents gain at least 35.7% of improvement, while 20% of all intents gain at least 83.5%.

#### Relevance 1010

Label: 1
> Reason
> - Summary of question: How are recognized intents used for ASR rescoring?
> - Summary of passage: Results quantify annotation gains and mention threshold calibration.
> - Judgement: The minimum-span threshold provides an actionable clue about which intent annotations are used for rescoring.
> 原因
> - 问题概述：如何利用识别出的意图对语音识别结果重新评分？
> - Passage 概述：结果量化意图标注收益，并提到阈值校准。
> - 判断：最小跨度阈值为哪些意图标注可用于重新评分提供可操作线索。

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1012

Retrieved by: Hybrid RRF followed by BGE reranking

> After every possible path in the lattice $\mathcal {L^{\prime }}$ has been either traversed or pruned, all redundant (i.e., pruned or not visited) FST states are removed from the lattice, along with all incident arcs.
> 
> The annotated lattice $\mathcal {A}$ is obtained after final traversal of the lattice $\mathcal {L^{\prime }}$ which prunes arcs representing unmatched word alternatives. If no intent has been matched on any of the parallel arcs, the traversal retains only the best path hypothesis. Figure FIGREF16 presents an example of the annotated lattice before and after pruning.

#### Relevance 1012

Label: 1
> Reason
> - Summary of question: How are recognized intents used for ASR rescoring?
> - Summary of passage: Unmatched alternatives are pruned; regions without intents retain the ASR best path.
> - Judgement: It directly explains how intent matches change candidate-path retention.
> 原因
> - 问题概述：如何利用识别出的意图对语音识别结果重新评分？
> - Passage 概述：剪除未匹配候选，无意图区域保留原语音识别最优路径。
> - 判断：它直接说明意图匹配如何改变候选路径保留。

#### Passage 1013

Retrieved by: Hybrid RRF followed by BGE reranking

> Despite significant pruning described in the previous section, the annotated lattice $\mathcal {A}$ still contains competing variants of the transcript. The next step consists in selecting the "best" variant and traversing all paths in $\mathcal {A}$ which correspond to this transcript. The key concept of our method is to guide the selection of the "best" variant by intents rather than word probabilities. We observe that the likelihood of a particular longer sequence of words in the language is lower than the likelihood of a particular shorter sequence of words. Since a priori longer intent examples are less likely to appear in the lattice $\mathcal {A}$ purely by chance, the presence of a lattice path containing a longer intent example provides strong evidence for that path.
> 
> The complete set of heuristics applied sequentially to the annotated lattice $\mathcal {A}$ in search of the best path is the following: (a) select the path with the longest intent annotation; (b) select the path with the largest number of intent annotations; (c) select the path with the intent annotation with the longest span (i.e. consider also blank words), (d) select the path with the highest original ASR likelihood. The chosen best path is composed with the annotated lattice $\mathcal {A}$ to produce the annotated lattice $\mathcal {A^*}$ with the final variant of the transcript. The output intent annotations are retrieved by traversing every path in $\mathcal {A^*}$.

#### Relevance 1013

Label: 1
> Reason
> - Summary of question: How are recognized intents used for ASR rescoring?
> - Summary of passage: Paths are ranked by intent length, count, span and finally original ASR likelihood.
> - Judgement: It explicitly gives the complete sequential rescoring heuristics.
> 原因
> - 问题概述：如何利用识别出的意图对语音识别结果重新评分？
> - Passage 概述：依次按意图长度、数量、跨度及原语音识别概率选择路径。
> - 判断：它明确给出完整且依次应用的重新评分规则。

#### Passage 1014

Retrieved by: Hybrid RRF followed by BGE reranking

> As hinted in Section SECREF1, most NLP tasks are performed on the turn level, which naturally corresponds to the turn-taking patterns in a typical human-machine dialogue. This approach yields good results for chatbot conversational interfaces or information retrieval systems, but for spontaneous human-human dialogues, the demarcation of turns is much more difficult due to the presence of fillers, interjections, ellipsis, backchannels, etc. Thus, we cannot expect those intent examples would align with ASR segments which capture a single speaker turn. We address this issue by concatenating turn-level lattices of all utterances of a person throughout the conversation into a conversation-lattice $\mathcal {L^C}$. This lattice can still be effectively annotated and pruned using algorithms presented in Section SECREF11 to obtain the annotated conversation-lattice $\mathcal {A^C}$.
> 
> Unfortunately, the annotated conversation-lattice $\mathcal {A^C}$ cannot be parsed in search of the best path using the algorithm presented in Section SECREF20, because the computational cost of every path traversal in $\mathcal {A^C}$ is exponential in the number of words. Fortunately, we can exploit the structure of the conversation-lattice $\mathcal {A^C}$ to identify the best path. We observe that $\mathcal {A^C}$ is a sequence of segments organized either in series or in parallel. Segments with no intent annotations are series of linear word hypotheses, which branch to parallel word hypotheses whenever an intent annotation is matched (because the original path with no intent annotation is retained in the lattice). The parallel segment ends with the end of the intent annotation. These series and parallel segments can be detected by inspecting the cumulative sum of the difference of out-degree and in-degree of each state in a topologically sorted conversation-lattice $\mathcal {A^C}$. For series regions, this sum will be equal to 0, and greater than 0 in parallel regions. The computational cost of performing this segmentation is $\mathcal {O}(|S| + |A|)$, i.e., linear in the number of states and arcs in the annotated conversation-lattice $\mathcal {A^C}$. After having performed the segmentation, the partial best path search in parallel segments is resolved using the method presented in Section SECREF20.

#### Relevance 1014

Label: 1
> Reason
> - Summary of question: How are recognized intents used for ASR rescoring?
> - Summary of passage: Conversation lattices are segmented and intent-bearing parallel regions undergo best-path search.
> - Judgement: It explains how intent-based rescoring is applied efficiently across conversations.
> 原因
> - 问题概述：如何利用识别出的意图对语音识别结果重新评分？
> - Passage 概述：对话词图被分段，对含意图的并行区域搜索最优路径。
> - 判断：它说明如何在完整对话中高效应用基于意图的重新评分。

## Question 0112

Paper: Reinforcing an Image Caption Generator Using Off-Line Human Feedback

> What are the baseline models?

### Common Retrieved Chunks

#### Passage 1015

Retrieved by: BM25, Hybrid RRF

> The results from the side-by-side evaluations are are shown in Table TABREF39. The OffPG method achieves significant improvements on all three different dimensions. This is an important result, considering that we trained the model using a caption ratings dataset that contains single-scalar scores for generic 'goodness' (as opposed to the well-defined dimensions along which the OffPG method scores have improved). These results demonstrate that the single-caption 'goodness' ratings encapsulate a signal for all these dimensions into its scalar value. Note that we observe the same tendency consistently under a variety of hyperparameter settings in our internal experiments.
> 
> Figure FIGREF44 highlights the way in which the OffPG method achieves its superiority over the Baseline model, compared to the other alternative models (using the 'Corectness' scores). For instance, over 75% of the captions for both Baseline$+(t)$ models receive a 0.0 score (equal quality), and more than half of them are exactly identical to their corresponding Baseline captions. In contrast, OffPG makes a strong impact by explicitly penalizing the captions with negative feedback: less than 16% captions are identical to the corresponding Baseline captions. Moreover, we observe a large portion of captions with scores of 1.0 in favor of OffPG, indicating that many captions are significantly enhanced. We observe similar trends in all the three metrics.

#### Relevance 1015

Label: 1
> Reason
> - Summary of question: Which baseline models are used?
> - Summary of passage: Human evaluations compare OffPG with Baseline and Baseline+(t).
> - Judgement: It names the baseline variants and compares their caption behavior, providing clues to the baseline set.
> 原因
> - 问题概述：使用哪些基线模型？
> - Passage 概述：人工评估比较 OffPG、Baseline 和 Baseline+(t)。
> - 判断：它列出基线变体并比较其描述行为，为基线集合提供线索。

#### Passage 1016

Retrieved by: BM25, Dense, Hybrid RRF

> Table TABREF38 shows the goodness scores from the single-caption evaluation. Both “average” and “voting” metrics clearly indicate that OffPG significantly improves over Baseline, while the other methods achieve only marginal gains, all of which are within the error range. Baseline$+(t)$ models use only 1.5% and 2.2% additional data, at $t=0.7$ and $t=0.5$, respectively, with insignificant impact. Moreover, these methods only maximize the likelihood of the additional captions, which are already generated with high likelihood by previous models trained on the same dataset, which results in self-reinforcement. In contrast, the policy gradient methods are allowed to utilize the negative feedback to directly penalize incorrect captions. However, OnPG fails to improve the quality, most likely because it relies on a noisy caption ratings estimator that fails to generalize well over the large space of possible captions.

#### Relevance 1016

Label: 1
> Reason
> - Summary of question: Which baseline models are used?
> - Summary of passage: Baseline+(t) maximizes likelihood on additional positively rated captions.
> - Judgement: It explains the positive-caption fine-tuning baseline and threshold variants.
> 原因
> - 问题概述：使用哪些基线模型？
> - Passage 概述：Baseline+(t) 在新增正面评分描述上最大化似然。
> - 判断：它解释正面描述微调基线及其阈值变体。

#### Passage 1017

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We first train an MLE model as our baseline, trained on the Conceptual Captions training split alone. We referred to this model as Baseline. For a baseline approach that utilizes (some of) the Caption-Quality data, we merge positively-rated captions from the Caption-Quality training split with the Conceptual Captions examples and finetune the baseline model. We call this model Baseline$+(t)$, where $t \in [0,1]$ is the rating threshold for the included positive captions. We train models for two variants, $t\in \lbrace 0.5, 0.7\rbrace $, which results in $\sim $72K and $\sim $51K additional (pseudo-)ground-truth captions, respectively. Note that the Baseline$+(t)$ approaches attempt to make use of the same additional dataset as our two reinforced models, OnPG and OffPG, but they need to exclude below-threshold captions due to the constraints in MLE.
> 
> In addition to the baselines, we train two reinforced models: one based on the on-policy policy gradient method with a rating estimator (OnPG), and the other based on the off-policy policy gradient method with the true ratings (OffPG). The differences between the methods are shown in Figure FIGREF27.

#### Relevance 1017

Label: 1
> Reason
> - Summary of question: Which baseline models are used?
> - Summary of passage: Baselines are an MLE captioner and positive-caption fine-tuning at thresholds 0.5 and 0.7.
> - Judgement: It directly defines the baseline models and distinguishes reinforced alternatives.
> 原因
> - 问题概述：使用哪些基线模型？
> - Passage 概述：基线为最大似然描述模型，以及阈值为 0.5 和 0.7 的正面描述微调模型。
> - 判断：它直接定义基线模型，并区分强化学习对比方法。

#### Passage 1019

Retrieved by: BM25, Hybrid RRF

> We compare the OnPG and OffPG methods in more depth, by performing ablation experiments for the $\alpha $ hyper-parameter (the weight for the policy gradient). Figure FIGREF45 shows the results of these ablation experiments, for which we performed side-by-side comparisons over a 200-image subset from the T2 dataset. The results indicate that a very small $\alpha $ limits the impact of the additional signal for both models, since the regularization effect from the original loss term becomes too strong. By allowing updates using policy gradient with a larger $\alpha $ value, OffPG improves the performances along all three dimensions, whereas the performance of OnPG starts degrading at higher $\alpha $ values. At $\alpha =100$, OnPG drastically suffers from mode collapse and ends up generating a single caption for every image. This mode collapse is a result of poor generalization of the rating estimator: the collapsed captions are structurally ill-formed (e.g., an empty string, or a string with simply a period `.'), but they receive high rating estimates ($>0.9$) from the estimator. Although we can (and did) introduce some heuristics to avoid some of these failure cases in the estimator, we observe that OnPG training would continue to suffer from the estimator failing to generalize well over the vast space of possible captions. This observation is similar to the mode collapsing phenomenon seen when training generative adversarial networks (GANs), but even more severe as the estimator in OnPG is fixed (unlike the discriminators in GANs which are trained simultaneously).
> 
> Another drawback of OnPG is that it increases the computational complexity significantly during training. In terms of the memory usage, the rating estimator introduces 65% additional parameters, and uses more than double the memory for gradient computation compared to the other models. Also, the sequential caption sampling in OnPG slows down the training procedure, by breaking the parallelism in the Transformer computations, in addition to the time complexity incurred by the rating estimator. Empirically, OnPG is over 10 times slower than the others in processing the same number of examples in training. In contrast, the time and space complexities of OffPG remain the same as Baseline and Baseline$+(t)$, since the only difference is the use of scalar

#### Relevance 1019

Label: 1
> Reason
> - Summary of question: Which baseline models are used?
> - Summary of passage: OnPG ablations reveal mode collapse and high computational cost.
> - Judgement: The OnPG rating-estimator description identifies an important comparison model alongside the baseline variants.
> 原因
> - 问题概述：使用哪些基线模型？
> - Passage 概述：OnPG 消融显示模式崩溃和较高计算成本。
> - 判断：OnPG 评分估计器描述说明基线变体之外的重要对比模型。

#### Passage 1020

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In the other type of evaluation, we measure the relative improvement of a model against the Baseline model; Three professional raters are shown the input image and two captions (anonymized and randomly shuffled with respect to their left/right position) side-by-side. One of the captions is from a candidate model and the other always from Baseline. We ask for relative judgments on three dimensions – Informativeness, Correctness and Fluency, using their corresponding questions shown in Table TABREF32. Each of these dimensions allows a 5-way choice, shown below together with their corresponding scores:
> 
> Each model is evaluated by the average rating scores from 3 distinct raters. As a result, we obtain 3 values for each model in the range $[-1, 1]$, where a negative score means a performance degradation in the given dimension with respect to Baseline. For every human evaluation, we report confidence intervals based on bootstrap resampling BIBREF35.

#### Relevance 1020

Label: 1
> Reason
> - Summary of question: Which baseline models are used?
> - Summary of passage: Raters compare model captions against Baseline on three quality dimensions.
> - Judgement: It identifies Baseline as the fixed comparison model in human evaluation, clarifying its experimental role.
> 原因
> - 问题概述：使用哪些基线模型？
> - Passage 概述：标注者在三个质量维度上将模型描述与 Baseline 比较。
> - 判断：它指出 Baseline 是人工评估中的固定对比模型，说明其在实验中的作用。

#### Passage 1022

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> Figure FIGREF46 presents some qualitative example outputs for our models, showcasing the effectiveness of the OffPG method. We observe that the OffPG model is often successful at correcting arbitrary qualifiers present in the baseline outputs (e.g., `half marathon' and `most beautiful' in the second and third examples, respectively).

#### Relevance 1022

Label: 1
> Reason
> - Summary of question: Which baseline models are used?
> - Summary of passage: Qualitative examples show OffPG correcting baseline caption qualifiers.
> - Judgement: Examples explicitly contrast OffPG and baseline outputs, helping characterize the baseline comparator.
> 原因
> - 问题概述：使用哪些基线模型？
> - Passage 概述：定性示例展示 OffPG 修正基线描述中的修饰语。
> - 判断：示例明确对比 OffPG 与基线输出，有助于刻画基线对照模型。

### BM25

#### Passage 1018

Retrieved by: BM25

> the best of our knowledge, our work is the first to propose using human caption ratings directly for training captioning models.
> 
> Our goal is to leverage the signals from a pre-collected caption ratings dataset BIBREF13 for training an image captioning model. We propose a method based on policy gradient, where the human ratings are considered as rewards for generating captions (seen as taking actions) in an RL framework. Since the dataset provides ratings only for a small set of images and captions, we do not have a generic reward function for random image-caption pairs. Therefore, it is not straightforward to apply policy gradient method that requires a reward for randomly sampled captions. To address this challenge, we use an off-policy technique and force the network to sample captions for which ratings are available in the dataset. We evaluate the effectiveness of our method using human evaluation studies on the T2 test set used for the Conceptual Captions Challenge, using both a similar human evaluation methodology and an additional, multi-dimensional side-by-side human evaluation strategy. Additionally, the human raters in our evaluation study are different from the ones that provided the caption ratings in BIBREF13, thereby ensuring that the results are independent of using a specific human-evaluator pool. The results of our human evaluations indicate that the proposed method improves the image captioning quality, by effectively leveraging both the positive and negative signals from the captions ratings dataset.
> 
> The main contributions of this paper are the following:
> 
> We propose to train captioning models using human ratings produced during evaluations of previous models.
> 
> We propose an off-policy policy gradient method to cope with the sparsity in available caption ratings.
> 
> We present a set of experiments using human evaluations that demonstrates the effectiveness of our approach.

#### Relevance 1018

Label: 0
> Reason
> - Summary of question: Which baseline models are used?
> - Summary of passage: Off-policy learning uses pre-collected human caption ratings as rewards.
> - Judgement: The proposed method is described without defining baselines.
> 原因
> - 问题概述：使用哪些基线模型？
> - Passage 概述：离策略学习将预先收集的人工描述评分作为奖励。
> - 判断：它描述所提方法，未定义基线。

### Dense

#### Passage 1021

Retrieved by: Dense

> We train Baseline using the Adam optimizer BIBREF34 on the training split of the Conceptual dataset for 3M iterations with the batch size of 4,096 and the learning rate of $3.2\times 10^{-5}$. The learning rate is warmed up for 20 epochs and exponentially decayed by a factor of 0.95 every 25 epochs. Baseline$+(t)$ are obtained by fine-tuning Baseline on the merged dataset for 1M iterations, with the learning rate of $3.2\times 10^{-7}$ and the same decaying factor. For OnPG, because its memory footprint is increased significantly due to the additional parameters for the rating estimator, we reduce the batch size for training this model by a 0.25 factor; the value of $b$ in Eq. (DISPLAY_FORM12) is set to the moving average of the rating estimates. During OffPG training, for each batch, we sample half of the examples from the Conceptual dataset and the other half from Caption-Quality dataset; $b$ is set to the average of the ratings in the dataset.

#### Relevance 1021

Label: 1
> Reason
> - Summary of question: Which baseline models are used?
> - Summary of passage: Baseline trains on Conceptual Captions; Baseline+(t) fine-tunes on merged data.
> - Judgement: It specifies how the baseline variants are trained.
> 原因
> - 问题概述：使用哪些基线模型？
> - Passage 概述：Baseline 在 Conceptual Captions 上训练，Baseline+(t) 在合并数据上微调。
> - 判断：它说明基线变体的训练方式。

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1023

Retrieved by: Hybrid RRF followed by BGE reranking

> We run two sets of human evaluation studies to evaluate the performance of our models and baselines, using the T2 dataset (1K images). For every evaluation, we generate captions using beam search (beam size of 5).

#### Relevance 1023

Label: 1
> Reason
> - Summary of question: Which baseline models are used?
> - Summary of passage: Human evaluation uses T2 images and beam-search captions.
> - Judgement: The shared beam-search decoding setup provides partial information about how the baselines generate captions.
> 原因
> - 问题概述：使用哪些基线模型？
> - Passage 概述：人工评估使用 T2 图像和束搜索描述。
> - 判断：共用的束搜索解码设置提供基线如何生成描述的部分信息。

#### Passage 1024

Retrieved by: Hybrid RRF followed by BGE reranking

> 10 times slower than the others in processing the same number of examples in training. In contrast, the time and space complexities of OffPG remain the same as Baseline and Baseline$+(t)$, since the only difference is the use of scalar weights ($r(c|I)$ and $\eta $) to gradients of each caption likelihood ($\bigtriangledown _\theta \ln p_\theta (c|I)$), as shown in Figure FIGREF8.

#### Relevance 1024

Label: 1
> Reason
> - Summary of question: Which baseline models are used?
> - Summary of passage: OffPG matches baseline computational complexity while reweighting gradients.
> - Judgement: The gradient comparison explains how the likelihood-based baseline relates to OffPG, providing partial model information.
> 原因
> - 问题概述：使用哪些基线模型？
> - Passage 概述：OffPG 重加权梯度，同时与基线具有相同计算复杂度。
> - 判断：梯度比较说明基于似然的基线与 OffPG 的关系，提供部分模型信息。

## Question 0113

Paper: Identifying Dogmatism in Social Media: Signals and Models

> What predictive model do they build?

### Common Retrieved Chunks

#### Passage 1025

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> “I'm supposed to trust the opinion of a MS minion? The people that produced Windows ME, Vista and 8? They don't even understand people, yet they think they can predict the behavior of new, self-guiding AI?” –anonymous
> 
> “I think an AI would make it easier for Patients to confide their information because by nature, a robot cannot judge them. Win-win? :D”' –anonymous
> 
> Dogmatism describes the tendency to lay down opinions as incontrovertibly true, without respect for conflicting evidence or the opinions of others BIBREF0 . Which user is more dogmatic in the examples above? This question is simple for humans. Phrases like “they think” and “they don't even understand,” suggest an intractability of opinion, while “I think” and “win-win?” suggest the opposite. Can we train computers to draw similar distinctions? Work in psychology has called out many aspects of dogmatism that can be modeled computationally via natural language, such as over-confidence and strong emotions BIBREF1 .
> 
> We present a statistical model of dogmatism that addresses two complementary goals. First, we validate psychological theories by examining the predictive power of feature sets that guide the model's predictions. For example, do linguistic signals of certainty help to predict a post is dogmatic, as theory would suggest? Second, we apply our model to answer four questions:
> 
> R1: What kinds of topics (e.g., guns, LGBT) attract the highest levels of dogmatism?
> 
> R2: How do dogmatic beliefs cluster?
> 
> R3: How does dogmatism influence a conversation on social media? R4: How do other user behaviors (e.g., frequency and breadth of posts) relate to dogmatism?
> 
> We train a predictive model to classify dogmatic posts from Reddit, one of the most popular discussion communities on the web. Posts on Reddit capture discussion and debate across a diverse set of domains and topics – users talk about everything from climate change and abortion, to world news and relationship advice, to the future of artificial intelligence. As a prerequisite to training our model, we have created a corpus of 5,000 Reddit posts annotated with levels of dogmatism, which we are releasing to share with other researchers.
> 
> Using the model, we operationalize key domain-independent aspects of psychological theories of dogmatism drawn from the literature. We find

#### Relevance 1025

Label: 1
> Reason
> - Summary of question: What predictive model is built?
> - Summary of passage: A statistical classifier predicts dogmatism in Reddit posts from linguistic signals.
> - Judgement: It identifies the prediction target, text input and statistical modeling approach.
> 原因
> - 问题概述：构建什么预测模型？
> - Passage 概述：统计分类器根据语言信号预测 Reddit 帖子的教条性。
> - 判断：它指出预测目标、文本输入及统计建模方式。

#### Passage 1026

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We have constructed the first corpus of social media posts annotated with dogmatism scores, allowing us to explore linguistic features of dogmatism and build a predictive model that analyzes new content. We apply this model to Reddit, where we discover behavioral predictors of dogmatism and topical patterns in the comments of dogmatic users.
> 
> Could we use this computational model to help users shed their dogmatic beliefs? Looking forward, our work makes possible new avenues for encouraging pro-social behavior in online communities.

#### Relevance 1026

Label: 1
> Reason
> - Summary of question: What predictive model is built?
> - Summary of passage: An annotated corpus supports a linguistic predictive model for new social-media content.
> - Judgement: It partially identifies the model as predicting textual dogmatism, without an algorithm name.
> 原因
> - 问题概述：构建什么预测模型？
> - Passage 概述：已标注语料支持用于新社交媒体内容的语言预测模型。
> - 判断：它部分说明模型预测文本教条性，但未给出算法名称。

#### Passage 1027

Retrieved by: BM25, Dense, Hybrid RRF

> We now show how we can use the linguistic feature sets we have described to build a classifier that predicts dogmatism in comments. A predictive model further validates our feature sets, and also allows us to analyze dogmatism in millions of other Reddit comments in a scalable way, with multiple uses in ongoing, downstream analyses.
> 
> Prediction task. Our goal is (1) to understand how well we can use the strategies in Section 3 to predict dogmatism, and (2) to test the domain-independence of these strategies. First, we test the performance of our model under cross-validation within the Reddit comment dataset. We then evaluate the Reddit-based model on a held out corpus of New York Times comments annotated using the technique in Section 2. We did not refer to this second dataset during feature construction.
> 
> For classification, we consider two classes of comments: dogmatic and non-dogmatic. As in the prior analysis, we draw these comments from the top and bottom quartiles of the dogmatism distribution. This means the classes are balanced, with 2,500 total comments in the Reddit training data and 500 total comments in the New York Times testing data.
> 
> We compare the predictions of logistic regression models based on unigram bag-of-words features (BOW), sentiment signals (SENT), the linguistic features from our earlier analyses (LING), and combinations of these features. BOW and SENT provide baselines for the task. We compute BOW features using term frequency-inverse document frequency (TF-IDF) and category-based features by normalizing counts for each category by the number of words in each document. The BOW classifiers are trained with regularization (L2 penalties of 1.5).
> 
> Classification results. We present classification accuracy in Table 2 . BOW shows an AUC of 0.853 within Reddit and 0.776 on the held out New York Times comments. The linguistic features boost classification results within Reddit (0.881) and on the held out New York Times comments (0.791). While linguistic signals by themselves provide strong predictive power (0.801 AUC within domain), sentiment signals are much less predictive.
> 
> These results suggest that linguistic features inspired by prior efforts in psychology are useful for predicting dogmatism in practice and generalize across new domains.

#### Relevance 1027

Label: 1
> Reason
> - Summary of question: What predictive model is built?
> - Summary of passage: Logistic regression classifies dogmatic versus non-dogmatic comments using BOW and linguistic features.
> - Judgement: It directly specifies the classifier, feature sets and binary labels.
> 原因
> - 问题概述：构建什么预测模型？
> - Passage 概述：逻辑回归使用词袋和语言特征区分教条与非教条评论。
> - 判断：它直接说明分类器、特征集和二元标签。

#### Passage 1028

Retrieved by: BM25, Hybrid RRF

> In contrast to the computational models we have presented, dogmatism is usually measured in psychology through survey scales, in which study participants answer questions designed to reveal underlying personality attributes BIBREF1 . Over time, these surveys have been updated BIBREF14 and improved to meet standards of psychometric validity BIBREF15 .
> 
> These surveys are often used to study the relationship between dogmatism and other psychological phenomena. For example, dogmatic people tend to show an increased tendency for confrontation BIBREF16 or moral conviction and religiosity BIBREF17 , and less likelihood of cognitive flexibility BIBREF18 , even among stereotypically non-dogmatic groups like atheists BIBREF19 . From a behavioral standpoint, dogmatic people solve problems differently, spending less time framing a problem and expressing more certainty in their solution BIBREF20 . Here we similarly examine how user behaviors on Reddit relate to a language model of dogmatism.
> 
> Ertel sought to capture dogmatism linguistically, though a small lexicon of words that correspond with high-level concepts like certainty and compromise dota. McKenny then used this dictionary to relate dogmatism to argument quality in student essays dogmatism-essays. Our work expands on this approach, applying supervised models based on a broader set of linguistic categories to identify dogmatism in text.
> 
> Other researchers have studied topics similar to dogmatism, such as signals of cognitive style in right-wing political thought BIBREF21 , the language used by trolls on social media BIBREF22 , or what makes for impartial language on twitter BIBREF23 . A similar flavor of work has examined linguistic models that capture politeness BIBREF2 , deception BIBREF24 , and authority BIBREF8 . We took inspiration from these models when constructing the feature sets in our work.
> 
> Finally, while we examine what makes an opinion dogmatic, other work has pushed further into the structure of arguments, for example classifying their justifications BIBREF25 , or what makes an argument likely to win BIBREF26 . Our model may allow future researchers to probe these questions more deeply.

#### Relevance 1028

Label: 1
> Reason
> - Summary of question: What predictive model is built?
> - Summary of passage: The work uses supervised models with broad linguistic categories to identify dogmatism.
> - Judgement: It supplies partial evidence about the model's supervision and inputs.
> 原因
> - 问题概述：构建什么预测模型？
> - Passage 概述：本文使用基于多类语言特征的监督模型识别教条性。
> - 判断：它提供模型监督方式和输入的部分证据。

#### Passage 1029

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We have shown dogmatism is captured by many linguistic features, but can we discover other high-level user behaviors that are similarly predictive?
> 
> To find out, we compute metrics of user behavior using the data sample of 1000 users and 10 million posts described in Section 5.2. Specifically, we calculate (1) activity: a user's total number of posts, (2) breadth: the number of subreddits a user has posted in, (3) focus: the proportion of a user's posts that appear in the subreddit where they are most active, and (4) engagement: the average number of posts a user contributes to each discussion they engage in. We then fit these behavioral features to a linear regression model where we predict each user's average dogmatism level. Positive coefficients in this model are positively predictive of dogmatism, while negative coefficients are negatively predictive. We find this model is significantly predicitive of dogmatism ( $R^2=0.1$ , $p<0.001$ ), with all features reaching statistical significance ( $p<0.001$ ). Activity and focus are positively associated with dogmatism, while breadth and engagement are negatively associated (Table 5 ). Together, these results suggest dogmatic users tend to post frequently and in specific communities, but are not as inclined to continue to engage with a discussion, once it has begun.

#### Relevance 1029

Label: 1
> Reason
> - Summary of question: What predictive model is built?
> - Summary of passage: A linear regression predicts users' average dogmatism from behavioral features.
> - Judgement: It describes an additional predictive model built in the paper, at user level.
> 原因
> - 问题概述：构建什么预测模型？
> - Passage 概述：线性回归根据行为特征预测用户平均教条性。
> - 判断：它描述论文构建的另一预测模型，预测粒度为用户。

### BM25

None

### Dense

#### Passage 1030

Retrieved by: Dense

> We now apply our dogmatism classifier to a larger dataset of posts, examining how dogmatic language shapes the Reddit community. Concretely, we apply the BOW+LING model trained on the full Reddit dataset to millions of new unannotated posts, labeling these posts with a probability of dogmatism according to the classifier (0=non-dogmatic, 1=dogmatic). We then use these dogmatism annotations to address four research questions.

#### Relevance 1030

Label: 1
> Reason
> - Summary of question: What predictive model is built?
> - Summary of passage: The BOW+LING classifier assigns dogmatism probabilities to new Reddit posts.
> - Judgement: It identifies the deployed predictive model's features and output.
> 原因
> - 问题概述：构建什么预测模型？
> - Passage 概述：BOW+LING 分类器为新 Reddit 帖子赋予教条性概率。
> - 判断：它说明实际应用的预测模型特征和输出。

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1031

Retrieved by: Hybrid RRF followed by BGE reranking

> How does interacting with a dogmatic comment impact a conversation? Are users able to shrug it off? Or do otherwise non-dogmatic users become more dogmatic themselves?
> 
> To answer this question, we sample 600,000 conversations triples from Reddit. These conversations consist of two people (A and B) talking, with the structure: A1 $\rightarrow $ B $\rightarrow $ A2. This allows us to measure the impact of B's dogmatism on A's response, while also controlling for the dogmatism level initially set by A. Concretely, we model the impact of dogmatism on these conversations through a linear regression. This model takes two features, the dogmatism levels of A1 and B, and predicts the dogmatism response of A2. If B's dogmatism has no effect on A's response, the coefficient that corresponds to B will not be significant in the model. Alternatively, if B's dogmatism does have some effect, it will be captured by the model's coefficient.
> 
> We find the coefficient of the B feature in the model is positively associated with dogmatism ( $p<0.001$ ). In other words, engagement with a dogmatic comment tends to make a user more dogmatic themselves. This effect holds when we run the same model on data subsets consisting only of dogmatic or non-dogmatic users, and also when we conservatively remove all words used by B from A's response (i.e., controlling for quoting effects).

#### Relevance 1031

Label: 1
> Reason
> - Summary of question: What predictive model is built?
> - Summary of passage: A linear regression predicts reply dogmatism from the initial comment and partner response.
> - Judgement: It identifies a further predictive regression model used for conversation analysis.
> 原因
> - 问题概述：构建什么预测模型？
> - Passage 概述：线性回归根据初始评论和对方回复预测后续回复的教条性。
> - 判断：它说明用于对话分析的另一预测回归模型。

#### Passage 1032

Retrieved by: Hybrid RRF followed by BGE reranking

> created a corpus of 5,000 Reddit posts annotated with levels of dogmatism, which we are releasing to share with other researchers.
> 
> Using the model, we operationalize key domain-independent aspects of psychological theories of dogmatism drawn from the literature. We find these features have predictive power that largely supports the underlying theory. For example, posts that use less confident language tend to be less dogmatic. We also discover evidence for new attributes of dogmatism. For example, dogmatic posts tend not to verbalize cognition, through terms such as “I think,” “possibly,” or “might be.”
> 
> Our model is trained on only 5,000 annotated posts, but once trained, we use it to analyze millions of other Reddit posts to answer our research questions. We find a diverse set of topics are colored by dogmatic language (e.g., people are dogmatic about religion, but also about LGBT issues). Further, we find some evidence for dogmatism as a deeper personality trait – people who are strongly dogmatic about one topic are more likely to express dogmatic views about others as well. Finally, in conversation, we discover that one user's dogmatism tends to bring out dogmatism in their conversational partner, forming a vicious cycle.

#### Relevance 1032

Label: 1
> Reason
> - Summary of question: What predictive model is built?
> - Summary of passage: A model trained on annotated posts predicts dogmatism in millions of Reddit posts.
> - Judgement: It gives partial evidence about the learned target and training data, but not the algorithm.
> 原因
> - 问题概述：构建什么预测模型？
> - Passage 概述：模型在已标注帖子上训练，预测数百万条 Reddit 帖子的教条性。
> - 判断：它提供学习目标和训练数据的部分证据，但未给出算法。

## Question 0114

Paper: Polyglot Semantic Role Labeling

> what languages are explored in this paper?

### Common Retrieved Chunks

#### Passage 1033

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this work, we have explored a straightforward method for polyglot training in SRL: use multilingual word vectors and combine training data across languages. This allows sharing without crosslingual alignments, shared annotation, or parallel data. We demonstrate that a polyglot model can outperform a monolingual one for semantic analysis, particularly for languages with less data.

#### Relevance 1033

Label: 1
> Reason
> - Summary of question: Which languages are investigated?
> - Summary of passage: Multilingual word vectors enable polyglot SRL training.
> - Judgement: Cross-language training and low-resource performance describe the study's multilingual scope without enumerating languages.
> 原因
> - 问题概述：研究涉及哪些语言？
> - Passage 概述：多语言词向量支持多语言语义角色标注训练。
> - 判断：跨语言训练和低资源表现说明研究的多语言范围，虽未列全语言。

#### Passage 1035

Retrieved by: BM25, Dense, Hybrid RRF

> The standard approach to multilingual NLP is to design a single architecture, but tune and train a separate model for each language. While this method allows for customizing the model to the particulars of each language and the available data, it also presents a problem when little data is available: extensive language-specific annotation is required. The reality is that most languages have very little annotated data for most NLP tasks.
> 
> ammar2016malopa found that using training data from multiple languages annotated with Universal Dependencies BIBREF1 , and represented using multilingual word vectors, outperformed monolingual training. Inspired by this, we apply the idea of training one model on multiple languages—which we call polyglot training—to PropBank-style semantic role labeling (SRL). We train several parsers for each language in the CoNLL 2009 dataset BIBREF0 : a traditional monolingual version, and variants which additionally incorporate supervision from English portion of the dataset. To our knowledge, this is the first multilingual SRL approach to combine supervision from several languages.
> 
> The CoNLL 2009 dataset includes seven different languages, allowing study of trends across the same. Unlike the Universal Dependencies dataset, however, the semantic label spaces are entirely language-specific, making our task more challenging. Nonetheless, the success of polyglot training in this setting demonstrates that sharing of statistical strength across languages does not depend on explicit alignment in annotation conventions, and can be done simply through parameter sharing. We show that polyglot training can result in better labeling accuracy than a monolingual parser, especially for low-resource languages. We find that even a simple combination of data is as effective as more complex kinds of polyglot training. We include a breakdown into label categories of the differences between the monolingual and polyglot models. Our findings indicate that polyglot training consistently improves label accuracy for common labels.

#### Relevance 1035

Label: 1
> Reason
> - Summary of question: Which languages are investigated?
> - Summary of passage: CoNLL-2009's seven languages are studied with added English supervision.
> - Judgement: It explicitly identifies English as one studied language and gives the dataset scope.
> 原因
> - 问题概述：研究涉及哪些语言？
> - Passage 概述：研究 CoNLL-2009 的七种语言，并增加英语监督。
> - 判断：它明确指出英语是研究语言之一，并给出数据集范围。

#### Passage 1036

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> We thank Luke Zettlemoyer, Luheng He, and the anonymous reviewers for helpful comments and feedback. This research was supported in part by the Defense Advanced Research Projects Agency (DARPA) Information Innovation Office (I2O) under the Low Resource Languages for Emergent Incidents (LORELEI) program issued by DARPA/I2O under contract HR001115C0113 to BBN. Views expressed are those of the authors alone.

#### Relevance 1036

Label: 0
> Reason
> - Summary of question: Which languages are investigated?
> - Summary of passage: Acknowledgments identify funding and contributors.
> - Judgement: The funding program's language focus does not identify experimental languages.
> 原因
> - 问题概述：研究涉及哪些语言？
> - Passage 概述：致谢列出资助和贡献者。
> - 判断：资助项目的语言主题不能说明实验语言。

#### Passage 1037

Retrieved by: BM25, Dense, Hybrid RRF

> In the first polyglot variant, we consider multilingual sharing between each language and English by using pretrained multilingual embeddings. This polyglot model is trained on the union of annotations in the two languages. We use stratified sampling to give the two datasets equal effective weight in training, and we ensure that every training instance is seen at least once per epoch.
> 
> The basis of our polyglot training is the use of pretrained multilingual word vectors, which allow representing entirely distinct vocabularies (such as the tokens of different languages) in a shared representation space, allowing crosslingual learning BIBREF9 . We produced multilingual embeddings from the monolingual embeddings using the method of ammar2016massively: for each non-English language, a small crosslingual dictionary and canonical correlation analysis was used to find a transformation of the non-English vectors into the English vector space BIBREF10 .
> 
> Unlike multilingual word representations, argument label sets are disjoint between language pairs, and correspondences are not clearly defined. Hence, we use separate label representations for each language's labels. Similarly, while (for example) eng:look and spa:mira may be semantically connected, the senses look.01 and mira.01 may not correspond. Hence, predicate sense representations are also language-specific.

#### Relevance 1037

Label: 1
> Reason
> - Summary of question: Which languages are investigated?
> - Summary of passage: Each language is paired with English; English and Spanish examples illustrate labels.
> - Judgement: It identifies English's role and provides partial evidence of the language coverage.
> 原因
> - 问题概述：研究涉及哪些语言？
> - Passage 概述：每种语言与英语配对，并以英语和西班牙语示例说明标签。
> - 判断：它指出英语的作用，并提供语言范围的部分证据。

#### Passage 1038

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We present our results in Table TABREF11 . We observe that simple polyglot training improves over monolingual training, with the exception of Czech, where we observe no change in performance. The languages with the fewest training examples (German, Japanese, Catalan) show the most improvement, while large-dataset languages such as Czech or Chinese see little or no improvement (Figure FIGREF10 ).
> 
> The language ID model performs inconsistently; it is better than the simple polyglot model in some cases, including Czech, but not in all. The language-specific LSTMs model performs best on a few languages, such as Catalan and Chinese, but worst on others. While these results may reflect differences between languages in the optimal amount of crosslingual sharing, we focus on the simple polyglot results in our analysis, which sufficiently demonstrate that polyglot training can improve performance over monolingual training.
> 
> We also report performance of state-of-the-art systems in each of these languages, all of which make explicit use of syntactic features, marcheggiani2017lstm excepted. While this results in better performance on many languages, our model has the advantage of not relying on a syntactic parser, and is hence more applicable to languages with lower resources. However, the results suggest that syntactic information is critical for strong performance on German, which has the fewest predicates and thus the least semantic annotation for a semantics-only model to learn from. Nevertheless, our baseline is on par with the best published scores for Chinese, and it shows strong performance on most languages.

#### Relevance 1038

Label: 1
> Reason
> - Summary of question: Which languages are investigated?
> - Summary of passage: Results discuss Czech, German, Japanese, Catalan and Chinese.
> - Judgement: These are explicitly evaluated languages, yielding a partial list.
> 原因
> - 问题概述：研究涉及哪些语言？
> - Passage 概述：结果讨论捷克语、德语、日语、加泰罗尼亚语和汉语。
> - 判断：这些是明确接受评估的语言，构成部分列表。

#### Passage 1039

Retrieved by: Dense, Hybrid RRF

> We evaluate our system on the semantic role labeling portion of the CoNLL-2009 shared task BIBREF0 , on all seven languages, namely Catalan, Chinese, Czech, English, German, Japanese and Spanish. For each language, certain tokens in each sentence in the dataset are marked as predicates. Each predicate takes as arguments other words in the same sentence, their relationship marked by labeled dependency arcs. Sentences may contain no predicates.
> 
> Despite the consistency of this format, there are significant differences between the training sets across languages. English uses PropBank role labels BIBREF2 . Catalan, Chinese, English, German, and Spanish include (but are not limited to) labels such as “arg INLINEFORM0 -agt” (for “agent”) or “A INLINEFORM1 ” that may correspond to some degree to each other and to the English roles. Catalan and Spanish share most labels (being drawn from the same source corpus, AnCora; BIBREF3 ), and English and German share some labels. Czech and Japanese each have their own distinct sets of argument labels, most of which do not have clear correspondences to English or to each other.
> 
> We also note that, due to semi-automatic projection of annotations to construct the German dataset, more than half of German sentences do not include labeled predicate and arguments. Thus while German has almost as many sentences as Czech, it has by far the fewest training examples (predicate-argument structures); see Table TABREF3 .

#### Relevance 1039

Label: 1
> Reason
> - Summary of question: Which languages are investigated?
> - Summary of passage: The seven languages are Catalan, Chinese, Czech, English, German, Japanese and Spanish.
> - Judgement: It directly lists every investigated language.
> 原因
> - 问题概述：研究涉及哪些语言？
> - Passage 概述：七种语言为加泰罗尼亚语、汉语、捷克语、英语、德语、日语和西班牙语。
> - 判断：它直接列出所有研究语言。

### BM25

#### Passage 1034

Retrieved by: BM25

> This third variant takes inspiration from the “frustratingly easy” architecture of daumeiii2007easy for domain adaptation. In addition to processing every example with a shared biLSTM as in previous models, we add language-specific biLSTMs that are trained only on the examples belonging to one language. Each of these language-specific biLSTMs is two layers deep, and is combined with the shared biSLTM in the input to the third layer. This adds a greater degree of language-specific processing while still sharing representations across languages. It also uses the language identification vector and multilingual word vectors in the input.

#### Relevance 1034

Label: 1
> Reason
> - Summary of question: Which languages are investigated?
> - Summary of passage: Shared and language-specific BiLSTMs form a polyglot architecture.
> - Judgement: Language-specific branches and language identifiers explain how the studied languages are represented within the polyglot model.
> 原因
> - 问题概述：研究涉及哪些语言？
> - Passage 概述：共享及语言专属 BiLSTM 构成多语言架构。
> - 判断：语言专用分支和语言标识说明受研究语言在多语言模型中的表示方式。

### Dense

#### Passage 1040

Retrieved by: Dense

> Recent improvements in multilingual SRL can be attributed to neural architectures. Swayamdipta2016-qt present a transition-based stack LSTM model that predicts syntax and semantics jointly, as a remedy to the reliance on pipelined models. Guo2016-zc and BIBREF11 use deep biLSTM architectures which use syntactic information to guide the composition. marcheggiani2017lstm use a simple LSTM model over word tokens to tag semantic dependencies, like our model. Their model predicts a token's label based on the combination of the token vector and the predicate vector, and saw benefits from using POS tags, both improvements that could be added to our model. marcheggiani2017gcn apply the recently-developed graph convolutional networks to SRL, obtaining state of the art results on English and Chinese. All of these approaches are orthogonal to ours, and might benefit from polyglot training.
> 
> Other polyglot models have been proposed for semantics. Richardson2018-ov-naacl train on multiple (natural language)-(programming language) pairs to improve a model that translates API text into code signature representations. Duong2017-qy treat English and German semantic parsing as a multi-task learning problem and saw improvement over monolingual baselines, especially for small datasets. Most relevant to our work is Johannsen2015-nb, which trains a polyglot model for frame-semantic parsing. In addition to sharing features with multilingual word vectors, they use them to find word translations of target language words for additional lexical features.

#### Relevance 1040

Label: 1
> Reason
> - Summary of question: Which languages are investigated?
> - Summary of passage: Prior SRL and semantic-parsing studies include English, Chinese and German.
> - Judgement: Earlier multilingual SRL systems supply context for the language coverage being extended; cited language lists are not the paper's final list.
> 原因
> - 问题概述：研究涉及哪些语言？
> - Passage 概述：既有语义角色标注和语义解析研究涉及英语、汉语和德语。
> - 判断：此前多语言 SRL 系统为理解语言覆盖扩展提供背景，但引用研究的语言列表并非本文最终列表。

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1041

Retrieved by: Hybrid RRF followed by BGE reranking

> corresponding senses, making the set of available senses at test time quite small (less than five senses/predicate on average across all languages). If a particular lemma was not observed in training, we heuristically predict it as the first sense of that predicate. For Czech and Japanese, the predicate sense annotation is simply the lemmatized token of the predicate, giving a one-to-one predicate-“sense” mapping.
> 
> For argument labeling, every token in the sentence is assigned one of the argument labels, or INLINEFORM0 if the model predicts it is not an argument to the indicated predicate.

#### Relevance 1041

Label: 1
> Reason
> - Summary of question: Which languages are investigated?
> - Summary of passage: Czech and Japanese predicate senses are represented by lemmatized tokens.
> - Judgement: It explicitly describes language-specific processing in the studied system.
> 原因
> - 问题概述：研究涉及哪些语言？
> - Passage 概述：捷克语和日语的谓词义项由词元表示。
> - 判断：它明确描述所研究系统中两种语言的专门处理。

#### Passage 1042

Retrieved by: Hybrid RRF followed by BGE reranking

> We use pretrained word embeddings as input to the model. For each of the shared task languages, we produced GloVe vectors BIBREF7 from the news, web, and Wikipedia text of the Leipzig Corpora Collection BIBREF8 . We trained 300-dimensional vectors, then reduced them to 100 dimensions with principal component analysis for efficiency.

#### Relevance 1042

Label: 1
> Reason
> - Summary of question: Which languages are investigated?
> - Summary of passage: GloVe embeddings are trained for each shared-task language.
> - Judgement: It ties the system to the shared task's language set and describes their common input preparation.
> 原因
> - 问题概述：研究涉及哪些语言？
> - Passage 概述：为每种共享任务语言训练 GloVe 嵌入。
> - 判断：它将系统与共享任务的语言集合关联，并描述共用输入准备方式。

## Question 0115

Paper: Categorization in the Wild: Generalizing Cognitive Models to Naturalistic Data across Languages

> do language share categories? 

### Common Retrieved Chunks

#### Passage 1046

Retrieved by: BM25, Hybrid RRF

> Even though much empirical research glosses over this observation, there is strong evidence that human conceptual representations are structured (see BIBREF37 for a recent critique and overview of cognitive studies of categorization). Categories mentally represent the complex structure of the environment. They allow to make inferences about concepts or categories that go beyond their perceived similarities capturing abstract and potentially complex properties (for example, the nutritional value of food items, or the emotional benefits of pets). Much research on human categorization is based on laboratory experiments where subjects are presented with artificial stimuli represented by a restricted set of task-relevant features. Observations of natural concepts, however, are often noisy or incomplete so that a notion of systematic relations among features might be more important here than under artificial conditions in the lab BIBREF38 .
> 
> The existence of structured features has received support through behavioral results from a variety of categorization related tasks, such as typicality rating BIBREF38 or category-based inductive inference BIBREF39 , BIBREF32 . Experimental evidence suggests that categories which on the surface do not seem to contain a coherent set of members (e.g., the category pets) are represented by an underlying set of abstract features which explain the coherence of the category (e.g., {keeps_company, lives_in_the_house}). Varying the types of available features (e.g., providing functional information in addition to objects' appearance) leads to different categorization behavior both in adults BIBREF39 and children BIBREF40 , BIBREF41 , and different feature types vary in their predictive value across categories. For example, 2-4-year old children categorize food items based on their color, however, toys are classified based on their shape BIBREF42 .
> 
> The structured nature of category features manifests itself in feature norms. Feature norms are verbalized lists of properties that humans associate with a particular concept BIBREF31 . Features collected in norming studies naturally fall into different types such as behavior, appearance or function. This suggests that structure also emerges from verbalized representations of concepts and features such as mentions in natural language corpora, used as stimuli in this work. McRae et al. BIBREF31 collected a large set of feature norms for more than 500 concepts in a multi-year study, and classified these using a variety

#### Relevance 1046

Label: 1
> Reason
> - Summary of question: Do languages share categories?
> - Summary of passage: Abstract structured features explain conceptual category coherence.
> - Judgement: Structured conceptual categories and feature norms supply background for comparing category organization across languages.
> 原因
> - 问题概述：不同语言是否共享概念类别？
> - Passage 概述：抽象结构化特征解释概念类别的连贯性。
> - 判断：结构化概念类别与特征规范为比较不同语言的类别组织提供背景。

#### Passage 1047

Retrieved by: BM25, Dense, Hybrid RRF

> in a broader context. We simulate the acquisition of categories comprising hundreds of concepts by approximating the learning environment with natural language text. Language has been shown to redundantly encode much of the non-linguistic information in the natural environment BIBREF20 , as well as human-like biases BIBREF33 , and to influence the emergence of categories BIBREF4 , BIBREF5 . Text corpora are a prime example of naturally occurring large-scale data sets BIBREF34 , BIBREF35 , BIBREF36 . In analogy to real-world situations, they encapsulate rich, diverse, and potentially noisy, information. The wide availability of corpora allows us to train and evaluate cognitive models on data from diverse languages and cultures. We test our model on corpora from five languages, derived from the online encyclopedia Wikipedia in Arabic, Chinese, French, English, and German. Wikipedia is a valuable resource for our study because it (a) discusses concepts and their properties explicitly and can thus serve as a proxy for the environment speakers of a language are exposed to; and (b) allows us to construct corpora which are highly comparable in their content across languages, controlling for effects of genre or style.
> 
> We present a series of evaluations investigating the quality of the induced categories and features. Leveraging a reference comprising hundreds of concepts and more than 30 categories, we demonstrate that our model learns meaningful categories in all five target languages. We furthermore show, through crowd-sourced evaluations involving native speakers of each target language, that the induced feature types are (a) each thematically coherent and interpretable; and (b) are associated with categories in comprehensible ways. We discuss language-specific idiosyncrasies emerging from the induced representations.
> 
> In the remainder of this article, we first review related literature, before we present a cognitively motivated model for learning categories and their structured representations from large natural language corpora. We then evaluate the quality of the emerging representations, as well as the generalizability of our model across languages. Note that the primary goal of this work is not to characterize differences in categories and features arising from different languages (even though this would be an interesting avenue for future work). Rather, we aim to demonstrate the utility of large-scale naturalistic datasets for

#### Relevance 1047

Label: 1
> Reason
> - Summary of question: Do languages share categories?
> - Summary of passage: Meaningful categories are learned in five languages against a common reference.
> - Judgement: The shared reference provides partial evidence of comparable categories, not identical realizations.
> 原因
> - 问题概述：不同语言是否共享概念类别？
> - Passage 概述：在五种语言中对照共同参考类别学习出有意义的类别。
> - 判断：共同参考提供类别可比较的部分证据，但不证明具体实现完全相同。

#### Passage 1048

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> Categories such as animal or furniture are fundamental cognitive building blocks allowing humans to efficiently represent and communicate the complex world around them. Concepts (e.g., dog, table) are grouped into categories based on shared properties pertaining, for example, to their behavior, appearance, or function. Categorization underlies other cognitive functions such as perception BIBREF0 , BIBREF1 or language BIBREF2 , BIBREF3 , and there is evidence that categories are not only shaped by the world they represent, but also by the language through which they are communicated BIBREF4 , BIBREF5 . Although mental categories exist across communities and cultures, their exact manifestations differ BIBREF6 , BIBREF7 , BIBREF8 , BIBREF9 . For example, American English speakers prefer taxonomic categorizations (e.g., mouse,squirrel) while Chinese speakers tend to prefer to categorize objects relationally (e.g., tree, squirrel; BIBREF7 ).
> 
> Given their prevalent function in human cognition, the acquisition and representation of categories has attracted considerable attention in cognitive science, and numerous theories have emerged BIBREF10 , BIBREF11 , BIBREF12 , BIBREF13 . Empirical studies of category acquisition and representation, have been predominantly based on small-scale laboratory experiments. In a typical experiment, human subjects are presented with small sets of often artificial concepts, such as binary strings BIBREF14 or colored shapes BIBREF15 , with strictly controlled features BIBREF16 , BIBREF17 , BIBREF18 . Hypotheses and principles of human categorization are established based on the processes and characteristics of the categorizations produced by the participants. The distribution of subjects participating in such studies is often skewed towards members of cultural and socioeconomic groups which are prevalent in the environment where the research is conducted, and typically consists to a large proportion of western, educated, wealthy and English-speaking participants often sampled from the even more specific population of college students. The demographic and socioeconomic bias has been long recognized, and the question of how this bias might impact conclusions about human cognition in general BIBREF19 and category learning specifically is under active debate BIBREF9 . Although laboratory studies are invaluable for understanding categorization phenomena in a controlled environment, they are also expensive and time-consuming to conduct, and consequently problematic to scale.
> 
> In this work, we scale the investigation of category learning and

#### Relevance 1048

Label: 1
> Reason
> - Summary of question: Do languages share categories?
> - Summary of passage: Mental categories exist across cultures, but English and Chinese grouping preferences differ.
> - Judgement: It directly explains shared category existence alongside language-specific manifestations.
> 原因
> - 问题概述：不同语言是否共享概念类别？
> - Passage 概述：心理类别跨文化存在，但英语和汉语的分组偏好不同。
> - 判断：它直接说明类别的共同存在及其语言特有表现。

#### Passage 1049

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> debate BIBREF9 . Although laboratory studies are invaluable for understanding categorization phenomena in a controlled environment, they are also expensive and time-consuming to conduct, and consequently problematic to scale.
> 
> In this work, we scale the investigation of category learning and representation along two axes: (1) the complexity of the learning environment, and consequently the richness of learnable concept and category representations, and (2) the diversity of languages and cultures considered in evaluation. We present a novel knowledge-lean, cognitively motivated Bayesian model which learns categories and their structured features jointly from large natural language text corpora in five diverse languages: Arabic, Chinese, English, French, and German. We approximate the learning environment using large corpora of natural language text. Language has been shown to redundantly encode much of the non-linguistic information in the natural environment BIBREF20 , and to influence the emergence of categories BIBREF4 , BIBREF5 . Besides text corpora can cover arbitrarily semantically complex domains, and are available across languages, providing an ideal test environment for studying categorization at scale.
> 
> Figure 1 illustrates example input to our model, and Figure 2 shows example categories and associated features as induced by our model from the English Wikipedia. Following prior work BIBREF21 , BIBREF22 , we create language-specific sets of stimuli, each consisting of a mention of target concept (e.g., apple), within its local linguistic context (e.g., {contains, seeds}; cf., Figure 1 ). We consider each stimulus an observation of the concept, i.e., the word referring to the concept is an instance of the concept itself, and its context words are a representation of its features. Our model infers categories as groups of concepts occurring with similar features; and it infers feature types as groups of features which co-occur with each other. The output of our model (cf., Figure 2 ) are categories as clusters of concepts, each associated with a set of feature types, i.e., thematically coherent groups of features. We train a separate model on each of our target languages, each time presenting the model with input stimuli from the relevant language.
> 
> Computational models in general, and Bayesian models in particular, allow to investigate hypotheses about cognitive phenomena by systematically modifying the learning mechanism or

#### Relevance 1049

Label: 1
> Reason
> - Summary of question: Do languages share categories?
> - Summary of passage: Separate Bayesian models learn categories from five language-specific corpora.
> - Judgement: Independent learning from comparable language corpora explains how cross-language categories can be examined.
> 原因
> - 问题概述：不同语言是否共享概念类别？
> - Passage 概述：独立贝叶斯模型从五种语言各自的语料学习类别。
> - 判断：从可比语言语料独立学习，说明如何考察跨语言类别。

#### Passage 1050

Retrieved by: Dense, Hybrid RRF

> Can we simulate category acquisition from large amounts of textual data using cognitively motivated computational models, and infer meaningful representations across languages?
> 
> We approach this question by applying BCF to data sets in five languages: English, French, German, Arabic, and Chinese. We train five models in total, one per language, each time using stimuli from the respective language alone. We evaluate induced categories by comparison against a human-created reference categorization; and collect judgments on the coherence of learnt feature types, and their relevance to their associated categories from large crowds of native speakers.
> 
> Is the structure and architecture of BCF appropriate and necessary for category and structured feature learning? We answer this question by comparing BCF against a variety of related models. First, we report a random baseline which assigns concepts to categories at random. Secondly, we compare against a model entirely based on word co-occurrence. Unlike BCF, the co-occurrence model cannot learn categories and features jointly, and has no notion of feature structure. It uses $k$ -means clustering BIBREF66 to group concepts into categories, and, subsequently, group features into feature types for each category (see Section UID27 ). Finally, we compare BCF against BayesCat, a cognitively motivated Bayesian model of category acquisition BIBREF22 . Like BCF, it draws inspiration from topic modeling, however, BayesCat does not learn categories and features jointly, and does not acquire structured feature representations.
> 
> In the following we describe our data set, as well as the set of models we compare BCF against. Next, we present a series of simulations evaluating the quality of the induced categories, their features, and their relevance to the associated categories.

#### Relevance 1050

Label: 1
> Reason
> - Summary of question: Do languages share categories?
> - Summary of passage: Five monolingual models are evaluated against human categorization and native judgments.
> - Judgement: The common human reference and per-language models provide a basis for assessing shared categories.
> 原因
> - 问题概述：不同语言是否共享概念类别？
> - Passage 概述：五个单语模型通过人工类别和母语者判断评估。
> - 判断：共同人工参考和各语言模型为判断类别共享提供依据。

#### Passage 1051

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> In this work we leverage large-scale computational simulations to advance our understanding of categories and features across languages and cultures. Our research touches on the representation of categories, concepts, and their features; the mechanisms with which these are learnt; and the use of computational models and large-scale naturalistic data sets to investigate these questions.

#### Relevance 1051

Label: 1
> Reason
> - Summary of question: Do languages share categories?
> - Summary of passage: The study investigates category learning across languages and cultures.
> - Judgement: It explicitly frames category representations across languages and cultures as the study's target.
> 原因
> - 问题概述：不同语言是否共享概念类别？
> - Passage 概述：研究探讨跨语言和文化的类别学习。
> - 判断：它明确将跨语言和文化的类别表示列为研究对象，提供问题背景。

### BM25

#### Passage 1043

Retrieved by: BM25

> The output clusters of an unsupervised learner do not have a natural interpretation. Cluster evaluation in this case involves mapping the induced clusters to a gold standard and measuring to what extent the two clusterings (induced and gold) agree BIBREF71 . Purity ( $pu$ ) measures the extent to which each induced category contains concepts that share the same gold category. Let $G_{j}$ denote the set of concepts belonging to the $j$ -th gold category and $C_{i}$ the set of concepts belonging to the $i$ -th cluster. Purity is calculated as the member overlap between an induced category and its mapped gold category. The scores are aggregated across all induced categories $i$ , and normalized by the total number of category members $N$ :
> 
> $$\text{pu} = \frac{1}{N} \sum _i \max \limits _j |C_i \cap G_j|$$   (Eq. 34)
> 
> Inversely, collocation ( $co$ ) measures the extent to which all members of a gold category are present in an induced category. For each gold category we determine the induced category with the highest concept overlap and then compute the number of shared concepts. Overlap scores are aggregated over all gold categories $j$ , and normalized by the total number of category members $N$ :
> 
> $$\text{co} = \frac{1}{N} \sum _j \max \limits _i |C_i \cap G_j|$$   (Eq. 35)
> 
> Finally, the harmonic mean of purity and collocation can be used to report a single measure of clustering quality. If $\beta $ is greater than 1, purity is weighted more strongly in the calculation, if $\beta $ is less than 1, collocation is weighted more strongly:
> 
> $$\text{F}_{\beta } = \frac{(1+\beta ) \cdot pu \cdot co}{(\beta \cdot pu) +co}$$   (Eq. 36)
> 
> We additionally report results in terms of V-Measure (VM, BIBREF72 ) which is an information-theoretic measure. VM is analogous to F-measure, in that it is defined as the weighted harmonic mean of two values, homogeneity (VH, the precision analogue) and completeness (VC, the recall analogue):
> 
> $$\text{VH} &=& 1-\frac{H(G|C)}{H(G)}\\
> \text{VC} &=& 1-\frac{H(C|G)}{H(C)}\\
> \text{VM} &=& 1-\frac{(1+\beta ) \cdot VH \cdot VC}{(\beta \cdot VH)+VC}$$   (Eq. 37)
> 
> where $H(\cdot )$ is the entropy function; $H(C|G)$ denotes the conditional entropy of the induced class $C$ given the gold standard class $G$ and quantifies the amount

#### Relevance 1043

Label: 1
> Reason
> - Summary of question: Do languages share categories?
> - Summary of passage: Purity, collocation and V-measure evaluate induced clusters against gold categories.
> - Judgement: Mapping induced clusters to common gold categories explains a comparison method relevant to category correspondence.
> 原因
> - 问题概述：不同语言是否共享概念类别？
> - Passage 概述：纯度、完整聚集度和 V-measure 衡量聚类与标准类别的一致性。
> - 判断：将归纳簇映射到共同金标准类别，说明与类别对应关系有关的比较方法。

#### Passage 1044

Retrieved by: BM25

> Our simulations focused on 491 basic-level concepts of living and non-living things, taken from two previous studies of concept representation BIBREF31 , BIBREF67 , for which we learn (a) a categorization and (b) structured feature representations. Human-created gold standard categorizations of the concepts into 33 categories are available BIBREF67 , BIBREF68 . Since the original studies were conducted in English, we collected translations of the target concepts and their categories into Arabic, Chinese, French, and German, created by native speakers of the target language. The final number of concepts differs across languages, because some English concepts do not exist (or do not have the same translation) in the target language. Concept sets and categorizations for all languages were made available as part of this submission.
> 
> We created language specific sets of input stimuli (as illustrated in Figure 1 ). For each target language we created a corpus as follows: We used a subset of articles from the Linguatools Wikipedia dump; we tokenized, POS-tagged and lemmatized the corpus, and removed stopwords using language-specific lists. From this data set we derived a set of input stimuli as mentions of a concept from the reference set of concepts in sentence context (cf., Figure 1 ). In order to obtain balanced data sets, we automatically filtered words of low importance to a concept from contexts, using the term-frequency-inverse-document-frequency (tf-idf) metric. After filtering, we only kept stimuli with $3 \le n \le 20$ context words and at most 1,000 stimuli per target concept. Table 2 summarizes the statistics of the resulting data sets. The number of stimuli varies across languages as a function of the number of target concepts, and the size of the respective Wikipedia corpus.

#### Relevance 1044

Label: 1
> Reason
> - Summary of question: Do languages share categories?
> - Summary of passage: English concepts and 33 categories are translated; some concepts lack equivalent translations.
> - Judgement: It supports cross-language category correspondence while explicitly noting language-specific gaps.
> 原因
> - 问题概述：不同语言是否共享概念类别？
> - Passage 概述：将英语概念及 33 个类别翻译为其他语言，部分概念缺少对等翻译。
> - 判断：它支持跨语言类别对应，同时明确指出语言差异造成的缺口。

#### Passage 1045

Retrieved by: BM25

> of involved prior knowledge (such as syntactic parses or manually defined patterns), and (b) the two stage extraction-and-filtering process which they adopt. Humans arguably do not first learn a large set of potential features for concepts, before they infer their relevance. The systems discussed above learn features for individual concepts rather than categories.
> 
> To our knowledge, we propose the first Bayesian model that jointly learns categories and their features from large sets of naturalistic input data. Our model is knowledge-lean, it learns from raw text in a single process, without relying on parsing resources, manually crafted rule patterns, or post-processing steps; it is more plausible from a cognitive point of view, and language agnostic. We present simulations with the same model on several languages varying in word order, morphology, and phonology.

#### Relevance 1045

Label: 1
> Reason
> - Summary of question: Do languages share categories?
> - Summary of passage: A language-agnostic model jointly learns categories and features from raw text.
> - Judgement: The language-agnostic model applied to diverse languages provides context for investigating common category structure.
> 原因
> - 问题概述：不同语言是否共享概念类别？
> - Passage 概述：语言无关模型从原始文本联合学习类别和特征。
> - 判断：将语言无关模型应用于多种语言，为研究共同类别结构提供背景。

### Dense

None

### Hybrid RRF

#### Passage 1052

Retrieved by: Hybrid RRF

> We presented the first large-scale, cross-linguistic analysis of categorization using naturally occurring data. We showed that rational Bayesian models of categorization can learn meaningful categories and their features from complex environments resembling the natural world more closely than limited laboratory settings.
> 
> We developed BCF, a cognitively motivated Bayesian model, and investigated its ability to learn categories (for hundreds of concepts) and their structured features from corpora in five languages. Like humans `in the wild', our model learns categories and relevant features jointly BIBREF28 , BIBREF29 , and induces structured representations of categories BIBREF30 , BIBREF31 , BIBREF32 . Compared to a simpler co-occurrence model and a Bayesian model with no access to these mechanisms BCF learns better categories and features which are rated as more relevant and coherent by humans. BCF models category acquisition as a general, language-independent process. It neither utilizes language-specific knowledge nor requires language-specific tuning, and as such paves the way for future investigations involving more languages, or different kinds of corpora.
> 
> Our study sheds light on the acquisition of concrete concepts and their features from text, and as such adopts a constrained view of both the learning environment and the learning target. It suggests a number of interesting suggestions for future research. First, this article considered natural language input as an approximation of the environment from which categories and their representations are learnt. While we showed that the linguistic environment is a useful approximation of the full multimodal input a learner has access to, it is clear that language cannot capture this multimodal environment is not captured in its entirety. Computational models of word learning have been trained on multimodal input data (albeit on smaller-scale problems; BIBREF75 , BIBREF76 ). Advantageously, Bayesian models are flexible with respect to the input data they receive, so we expect the application of our model to multimodal data to be a feasible avenue for future work. Applying our models to such data sets would allow to compare the category acquisition process as well as the acquired representations from multimodal input against those emerging from language data alone.
> 
> A second direction for future work concerns the cognitive assumptions underlying the learning setup. The models discussed in

#### Relevance 1052

Label: 1
> Reason
> - Summary of question: Do languages share categories?
> - Summary of passage: BCF learns meaningful categories through a language-independent acquisition process.
> - Judgement: The common category-learning mechanism across five languages provides supporting evidence of cross-language generality.
> 原因
> - 问题概述：不同语言是否共享概念类别？
> - Passage 概述：BCF 通过语言无关的习得过程学习有意义的类别。
> - 判断：五种语言中的共同类别学习机制为跨语言普适性提供辅助证据。

### Hybrid RRF followed by BGE reranking

#### Passage 1053

Retrieved by: Hybrid RRF followed by BGE reranking

> goal of this work is not to characterize differences in categories and features arising from different languages (even though this would be an interesting avenue for future work). Rather, we aim to demonstrate the utility of large-scale naturalistic datasets for cognitive modeling, and to verify mechanisms of categorization known from laboratory studies at scale and across communities.

#### Relevance 1053

Label: 1
> Reason
> - Summary of question: Do languages share categories?
> - Summary of passage: Characterizing category differences across languages is outside the primary goal.
> - Judgement: It limits the conclusions: cross-language category differences are not the primary characterization goal.
> 原因
> - 问题概述：不同语言是否共享概念类别？
> - Passage 概述：刻画跨语言类别差异并非研究主要目标。
> - 判断：它限定结论范围：刻画跨语言类别差异并非主要目标。

#### Passage 1054

Retrieved by: Hybrid RRF followed by BGE reranking

> Computational models as simulators of cognitive processes have been used successfully to shed light on a wide variety of phenomena BIBREF61 , including language acquisition BIBREF27 , generalization, and reasoning BIBREF62 . Bayesian models in particular are amenable towards this goal, because they allow the modeler to formalize hypotheses rigorously through sets of random variables and their relations. They use the principled rules of Bayesian probability to select “good” models which explain the observed data well. We present a Bayesian model to investigate cognitive processes of categorization, in correspondence to Marr's BIBREF63 computational level of analysis, i.e., abstracting away from the algorithms and biological substrates in which these processes are situated. Starting from Anderson's BIBREF14 pioneering work on rational models of categorization, a variety of models, both Bayesian BIBREF50 , BIBREF52 , BIBREF22 and non-Bayesian BIBREF18 , BIBREF21 have been proposed. Our work advances prior research by investigating for the first time joint category and feature learning from noisy stimuli, across diverse languages.
> 
> We present BCF, a cognitively motivated Bayesian model for learning Categories and structured Features from large sets of concept mentions and their linguistic contexts (see Figure 1 ). Our model induces categories (as groups of concepts), feature types which are shared across categories (as groups of features or context words), and category-feature type associations. Figure 2 shows example output of BCF as learnt from the English Wikipedia, and Figure 21 shows example categories and features learnt for five additional languages.
> 
> BCF is a statistical Bayesian model. Given a large set of stimuli, it learns meaningful categories and features from a countably infinite set of all possible categorizations and representations. The probability (or `meaningfulness') of any hypothetical categorization and representation $h$ under the stimuli data $d$ can be evaluated using Bayes' rule:
> 
> $$p(h|d) \propto p(d|h) p(h),$$   (Eq. 8)
> 
> where $p(h)$ is the prior probability of $h$ under the specified model and its assumptions; and $p(d|h)$ is the likelihood to observe data $d$ given that hypothesis $h$ holds.

#### Relevance 1054

Label: 1
> Reason
> - Summary of question: Do languages share categories?
> - Summary of passage: BCF jointly induces categories, feature types and their associations.
> - Judgement: It points to categories and features induced across languages, which can inform comparison of shared structure.
> 原因
> - 问题概述：不同语言是否共享概念类别？
> - Passage 概述：BCF 联合归纳类别、特征类型及二者关联。
> - 判断：它提到跨语言归纳出的类别和特征，可为共同结构比较提供线索。

## Question 0116

Paper: Automated News Suggestions for Populating Wikipedia Entity Pages

> What features are used to represent the novelty of news articles to entity pages?

### Common Retrieved Chunks

#### Passage 1056

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> only. As Sauper and Barzilay concentrate on empty entity pages, the problem of novelty of their content is not an issue in their work whereas it is in our case which focuses more on updating entities. Updating entities will be more and more important the bigger an existing reference work is. Both the approaches in BIBREF8 and BIBREF12 (finding paragraphs and summarization) could then be used to process the documents we suggest further. Our concentration on news is also novel.
> 
> Knowledge Base Acceleration. In this task, given specific information extraction templates, a given corpus is analyzed in order to find worthwhile mentions of an entity or snippets that match the templates. Balog BIBREF9 , BIBREF10 recommend news citations for an entity. Prior to that, the news articles are classified for their appropriateness for an entity, where as features for the classification task they use entity, document, entity-document and temporal features. The best performing features are those that measure similarity between an entity and the news document. West et al. BIBREF13 consider the problem of knowledge base completion, through question answering and complete missing facts in Freebase based on templates, i.e. Frank_Zappa bornIn Baltymore, Maryland.
> 
> In contrast, we do not extract facts for pre-defined templates but rather suggest news articles based on their relevance to an entity. In cases of long-tail entities, we can suggest to add a novel section through our abstraction and generation of section templates at entity class level.
> 
> Entity Salience. Determining which entities are prominent or salient in a given text has a long history in NLP, sparked by the linguistic theory of Centering BIBREF14 . Salience has been used in pronoun and co-reference resolution BIBREF15 , or to predict which entities will be included in an abstract of an article BIBREF11 . Frequent features to measure salience include the frequency of an entity in a document, positioning of an entity, grammatical function or internal entity structure (POS tags, head nouns etc.). These approaches are not currently aimed at knowledge base generation or Wikipedia coverage extension but we postulate that an entity's salience in a news article is a prerequisite to the news article being relevant enough to be included in an

#### Relevance 1056

Label: 1
> Reason
> - Summary of question: Which features measure news novelty relative to entity pages?
> - Summary of passage: Related work covers page generation, knowledge-base acceleration and entity salience.
> - Judgement: Its contrast between empty-page generation and updating explains why existing-page content must inform novelty.
> 原因
> - 问题概述：用什么特征衡量新闻相对于实体页面的新颖性？
> - Passage 概述：相关工作涉及页面生成、知识库加速和实体显著性。
> - 判断：它对比空白页面生成与更新，说明为何新颖性需要考虑已有页面内容。

#### Passage 1058

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> addition, their use is in line with current Wikipedia editing practice, as is shown in BIBREF7 that almost 20% of current citations in all entity pages are news articles. We therefore propose news suggestion as a novel task that enhances entity pages and reduces delay while keeping its pages authoritative.
> 
> Existing efforts to populate Wikipedia BIBREF8 start from an entity page and then generate candidate documents about this entity using an external search engine (and then post-process them). However, such an approach lacks in (a) reproducibility since rankings vary with time with obvious bias to recent news (b) maintainability since document acquisition for each entity has to be periodically performed. To this effect, our news suggestion considers a news article as input, and determines if it is valuable for Wikipedia. Specifically, given an input news article INLINEFORM0 and a state of Wikipedia, the news suggestion problem identifies the entities mentioned in INLINEFORM1 whose entity pages can improve upon suggesting INLINEFORM2 . Most of the works on knowledge base acceleration BIBREF9 , BIBREF10 , BIBREF11 , or Wikipedia page generation BIBREF8 rely on high quality input sources which are then utilized to extract textual facts for Wikipedia page population. In this work, we do not suggest snippets or paraphrases but rather entire articles which have a high potential importance for entity pages. These suggested news articles could be consequently used for extraction, summarization or population either manually or automatically – all of which rely on high quality and relevant input sources.
> 
> We identify four properties of good news recommendations: salience, relative authority, novelty and placement. First, we need to identify the most salient entities in a news article. This is done to avoid pollution of entity pages with only marginally related news. Second, we need to determine whether the news is important to the entity as only the most relevant news should be added to a precise reference work. To do this, we compute the relative authority of all entities in the news article: we call an entity more authoritative than another if it is more popular or noteworthy in the real world. Entities with very high authority have many news items associated with them and

#### Relevance 1058

Label: 1
> Reason
> - Summary of question: Which features measure news novelty relative to entity pages?
> - Summary of passage: News suggestions depend on salience, authority, novelty and placement.
> - Judgement: It places novelty among the explicit recommendation criteria, helping locate its role in feature design.
> 原因
> - 问题概述：用什么特征衡量新闻相对于实体页面的新颖性？
> - Passage 概述：新闻推荐依赖显著性、权威度、新颖性和放置位置。
> - 判断：它将新颖性列为明确推荐标准，有助于确定其在特征设计中的作用。

#### Passage 1060

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> These approaches are not currently aimed at knowledge base generation or Wikipedia coverage extension but we postulate that an entity's salience in a news article is a prerequisite to the news article being relevant enough to be included in an entity page. We therefore use the salience features in BIBREF11 as part of our model. However, these features are document-internal — we will show that they are not sufficient to predict news inclusion into an entity page and add features of entity authority, news authority and novelty that measure the relations between several entities, between entity and news article as well as between several competing news articles.

#### Relevance 1060

Label: 1
> Reason
> - Summary of question: Which features measure news novelty relative to entity pages?
> - Summary of passage: Novelty features supplement document-internal entity salience features.
> - Judgement: It characterizes novelty as relational information beyond document-internal salience, giving partial feature-design clues.
> 原因
> - 问题概述：用什么特征衡量新闻相对于实体页面的新颖性？
> - Passage 概述：新颖性特征补充文档内部实体显著性特征。
> - 判断：它将新颖性描述为文档内部显著性之外的关系信息，提供部分特征设计线索。

#### Passage 1061

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this work, we have proposed an automated approach for the novel task of suggesting news articles to Wikipedia entity pages to facilitate Wikipedia updating. The process consists of two stages. In the first stage, article–entity placement, we suggest news articles to entity pages by considering three main factors, such as entity salience in a news article, relative authority and novelty of news articles for an entity page. In the second stage, article–section placement, we determine the best fitting section in an entity page. Here, we remedy the problem of incomplete entity section profiles by constructing section templates for specific entity classes. This allows us to add missing sections to entity pages. We carry out an extensive experimental evaluation on 351,983 news articles and 73,734 entities coming from 27 distinct entity classes. For the first stage, we achieve an overall performance with P=0.93, R=0.514 and F1=0.676, outperforming our baseline competitors significantly. For the second stage, we show that we can learn incrementally to determine the correct section for a news article based on section templates. The overall performance across different classes is P=0.844, R=0.885 and F1=0.860.
> 
> In the future, we will enhance our work by extracting facts from the suggested news articles. Results suggest that the news content cited in entity pages comes from the first paragraphs. However, challenging task such as the canonicalization and chronological ordering of facts, still remain.

#### Relevance 1061

Label: 1
> Reason
> - Summary of question: Which features measure news novelty relative to entity pages?
> - Summary of passage: A two-stage recommender considers novelty and section placement.
> - Judgement: It identifies novelty as an article-to-entity-page factor in the first-stage model.
> 原因
> - 问题概述：用什么特征衡量新闻相对于实体页面的新颖性？
> - Passage 概述：两阶段推荐系统考虑新颖性和章节放置。
> - 判断：它指出新颖性是第一阶段模型中新闻相对于实体页面的因素。

#### Passage 1062

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> authority of all entities in the news article: we call an entity more authoritative than another if it is more popular or noteworthy in the real world. Entities with very high authority have many news items associated with them and only the most relevant of these should be included in Wikipedia whereas for entities of lower authority the threshold for inclusion of a news article will be lower. Third, a good recommendation should be able to identify novel news by minimizing redundancy coming from multiple news articles. Finally, addition of facts is facilitated if the recommendations are fine-grained, i.e., recommendations are made on the section level rather than the page level (placement).
> 
> Approach and Contributions. We propose a two-stage news suggestion approach to entity pages. In the first stage, we determine whether a news article should be suggested for an entity, based on the entity's salience in the news article, its relative authority and the novelty of the article to the entity page. The second stage takes into account the class of the entity for which the news is suggested and constructs section templates from entities of the same class. The generation of such templates has the advantage of suggesting and expanding entity pages that do not have a complete section structure in Wikipedia, explicitly addressing long-tail and trunk entities. Afterwards, based on the constructed template our method determines the best fit for the news article with one of the sections.
> 
> We evaluate the proposed approach on a news corpus consisting of 351,982 articles crawled from the news external references in Wikipedia from 73,734 entity pages. Given the Wikipedia snapshot at a given year (in our case [2009-2014]), we suggest news articles that might be cited in the coming years. The existing news references in the entity pages along with their reference date act as our ground-truth to evaluate our approach. In summary, we make the following contributions.

#### Relevance 1062

Label: 1
> Reason
> - Summary of question: Which features measure news novelty relative to entity pages?
> - Summary of passage: Novel recommendations minimize redundancy among news articles.
> - Judgement: The explicit redundancy-minimization objective helps interpret the novelty features, although their formulas are absent.
> 原因
> - 问题概述：用什么特征衡量新闻相对于实体页面的新颖性？
> - Passage 概述：新颖推荐减少新闻文章之间的冗余。
> - 判断：明确的冗余最小化目标有助于理解新颖性特征，虽未给出公式。

### BM25

#### Passage 1055

Retrieved by: BM25

> the discussion on entity profile expansion in Section UID69 ).
> 
> Topic. We use topic similarities to ensure (i) that the content of INLINEFORM0 fits topic-wise with a specific section text and (ii) that it has a similar topic to previously referred news articles in that section. In a pre-processing stage we compute the topic models for the news articles, entity sections INLINEFORM1 and the aggregated class-based sections in INLINEFORM2 . The topic models are computed using LDA BIBREF20 . We only computed a single topic per article/section as we are only interested in topic term overlaps between article and sections. We distinguish two main features: the first feature measures the overlap of topic terms between INLINEFORM3 and the entity section INLINEFORM4 and INLINEFORM5 , and the second feature measures the overlap of the topic model of INLINEFORM6 against referred news articles in INLINEFORM7 at time INLINEFORM8 .
> 
> Syntactic. These features represent a mechanism for conveying the importance of a specific text snippet, solely based on the frequency of specific POS tags (i.e. NNP, CD etc.), as commonly used in text summarization tasks. Following the same intuition as in BIBREF8 , we weigh the importance of articles by the count of specific POS tags. We expect that for different sections, the importance of POS tags will vary. We measure the similarity of POS tags in a news article against the section text. Additionally, we consider bi-gram and tri-gram POS tag overlap. This exploits similarity in syntactical patterns between the news and section text.
> 
> Lexical. As lexical features, we measure the similarity of INLINEFORM0 against the entity section text INLINEFORM1 and the aggregate section text INLINEFORM2 . Further, we distinguish between the overall similarity of INLINEFORM3 and that of the different news paragraphs ( INLINEFORM4 which denotes the paragraphs of INLINEFORM5 up to the 5th paragraph). A higher similarity on the first paragraphs represents a more confident indicator that INLINEFORM6 should be suggested to a specific section INLINEFORM7 . We measure the similarity based on two metrics: (i) the KL-divergence between the computed language models and (ii) cosine similarity of the corresponding paragraph text INLINEFORM8 and section text.
> 
> Entity-based. Another feature set we consider is the overlap

#### Relevance 1055

Label: 1
> Reason
> - Summary of question: Which features measure news novelty relative to entity pages?
> - Summary of passage: Section-placement features use LDA topic overlap, POS patterns and lexical similarity.
> - Judgement: Article-to-section topic, lexical and entity comparisons are related page-comparison features that contextualize novelty; they are not confirmed as the novelty feature set.
> 原因
> - 问题概述：用什么特征衡量新闻相对于实体页面的新颖性？
> - Passage 概述：章节放置特征使用 LDA 主题重叠、词性模式和词汇相似度。
> - 判断：文章与章节的主题、词汇和实体比较为新颖性提供页面比较背景，但未被确认为新颖性特征集。

#### Passage 1057

Retrieved by: BM25

> In this section we outline the evaluation plan to verify the effectiveness of our learning approaches. To evaluate the news suggestion problem we are faced with two challenges.
> 
> What comprises the ground truth for such a task ?
> 
> How do we construct training and test splits given that entity pages consists of text added at different points in time ?
> 
> Consider the ground truth challenge. Evaluating if an arbitrary news article should be included in Wikipedia is both subjective and difficult for a human if she is not an expert. An invasive approach, which was proposed by Barzilay and Sauper BIBREF8 , adds content directly to Wikipedia and expects the editors or other users to redact irrelevant content over a period of time. The limitations of such an evaluation technique is that content added to long-tail entities might not be evaluated by informed users or editors in the experiment time frame. It is hard to estimate how much time the added content should be left on the entity page. A more non-invasive approach could involve crowdsourcing of entity and news article pairs in an IR style relevance assessment setup. The problem of such an approach is again finding knowledgeable users or experts for long-tail entities. Thus the notion of relevance of a news recommendation is challenging to evaluate in a crowd setup.
> 
> We take a slightly different approach by making an assumption that the news articles already present in Wikipedia entity pages are relevant. To this extent, we extract a dataset comprising of all news articles referenced in entity pages (details in Section SECREF40 ). At the expense of not evaluating the space comprising of news articles absent in Wikipedia, we succeed in (i) avoiding restrictive assumptions about the quality of human judgments, (ii) being invasive and polluting Wikipedia, and (iii) deriving a reusable test bed for quicker experimentation.
> 
> The second challenge of construction of training and test set separation is slightly easier and is addressed in Section SECREF46 .

#### Relevance 1057

Label: 0
> Reason
> - Summary of question: Which features measure news novelty relative to entity pages?
> - Summary of passage: Existing Wikipedia news citations provide evaluation ground truth.
> - Judgement: Ground-truth construction does not specify novelty features.
> 原因
> - 问题概述：用什么特征衡量新闻相对于实体页面的新颖性？
> - Passage 概述：已有 Wikipedia 新闻引用提供评估真值。
> - 判断：真值构建未说明新颖性特征。

#### Passage 1059

Retrieved by: BM25

> Wikipedia is the largest source of open and collaboratively curated knowledge in the world. Introduced in 2001, it has evolved into a reference work with around 5m pages for the English Wikipedia alone. In addition, entities and event pages are updated quickly via collaborative editing and all edits are encouraged to include source citations, creating a knowledge base which aims at being both timely as well as authoritative. As a result, it has become the preferred source of information consumption about entities and events. Moreso, this knowledge is harvested and utilized in building knowledge bases like YAGO BIBREF0 and DBpedia BIBREF1 , and used in applications like text categorization BIBREF2 , entity disambiguation BIBREF3 , entity ranking BIBREF4 and distant supervision BIBREF5 , BIBREF6 .
> 
> However, not all Wikipedia pages referring to entities (entity pages) are comprehensive: relevant information can either be missing or added with a delay. Consider the city of New Orleans and the state of Odisha which were severely affected by cyclones Hurricane Katrina and Odisha Cyclone, respectively. While Katrina finds extensive mention in the entity page for New Orleans, Odisha Cyclone which has 5 times more human casualties (cf. Figure FIGREF2 ) is not mentioned in the page for Odisha. Arguably Katrina and New Orleans are more popular entities, but Odisha Cyclone was also reported extensively in national and international news outlets. This highlights the lack of important facts in trunk and long-tail entity pages, even in the presence of relevant sources. In addition, previous studies have shown that there is an inherent delay or lag when facts are added to entity pages BIBREF7 .
> 
> To remedy these problems, it is important to identify information sources that contain novel and salient facts to a given entity page. However, not all information sources are equal. The online presence of major news outlets is an authoritative source due to active editorial control and their articles are also a timely container of facts. In addition, their use is in line with current Wikipedia editing practice, as is shown in BIBREF7 that almost 20% of current citations in all entity pages are news articles. We therefore propose news suggestion as a novel task that enhances

#### Relevance 1059

Label: 1
> Reason
> - Summary of question: Which features measure news novelty relative to entity pages?
> - Summary of passage: Incomplete Wikipedia pages motivate timely news recommendations.
> - Judgement: The discussion of missing facts and novel information clarifies what novelty is intended to capture relative to a page.
> 原因
> - 问题概述：用什么特征衡量新闻相对于实体页面的新颖性？
> - Passage 概述：Wikipedia 页面不完整促使研究及时新闻推荐。
> - 判断：对缺失事实和新信息的讨论说明新颖性旨在捕捉相对页面的什么内容。

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0117

Paper: A multi-layer approach to disinformation detection on Twitter

> How is the political bias of different sources included in the model?

### Common Retrieved Chunks

#### Passage 1063

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> number of strong/weak connected components and diameter, and more elaborated ones such as main K-core number BIBREF13 and structural virality BIBREF14. Our main research question is whether the use of a multi-layer, disentangled network yields a significant advance in terms of classification accuracy over a conventional single-layer diffusion network. Additionally, we are interested in understanding which of the above features, and in which layer, are most effective in the classification task.
> 
> We perform classification experiments with an off-the-shelf Logistic Regression model on two different datasets of mainstream and disinformation news shared on Twitter respectively in the United States and in Italy during 2019. In the former case we also account for political biases inherent to different news sources, referring to the procedure proposed in BIBREF2 to label different outlets. Overall we show that we are able to classify credible vs non-credible diffusion networks (and consequently news articles) with high accuracy (AUROC up to 94%), even when accounting for the political bias of sources (and training only on left-biased or right-biased articles). We observe that the layer of mentions alone conveys useful information for the classification, denoting a different usage of this functionality when sharing news belonging to the two news domains. We also show that most discriminative features, which are relative to the breadth and depth of largest cascades in different layers, are the same across the two countries.
> 
> The outline of this paper is the following: we first formulate the problem and describe data collection, network representation and structural properties employed for the classification; then we provide experimental results–classification performances, layer and feature importance analyses and a temporal classification evaluation–and finally we draw conclusions and future directions.

#### Relevance 1063

Label: 1
> Reason
> - Summary of question: How is sources' political bias accounted for in the model?
> - Summary of passage: US outlets receive bias labels and models train on only one political side.
> - Judgement: It explains that political bias is controlled through labeled training subsets.
> 原因
> - 问题概述：模型如何考虑不同来源的政治倾向？
> - Passage 概述：为美国媒体赋予倾向标签，并仅用单侧政治倾向数据训练模型。
> - 判断：它说明通过带倾向标签的训练子集控制政治偏向。

#### Passage 1064

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We collected tweets associated to a dozen US mainstream news websites, i.e. most trusted sources described in BIBREF18, with the Streaming API, and we referred to Hoaxy API BIBREF16 for what concerns tweets containing links to 100+ US disinformation outlets. We filtered out articles associated to less than 50 tweets. The resulting dataset contains overall $\sim $1.7 million tweets for mainstream news, collected in a period of three weeks (February 25th, 2019-March 18th, 2019), which are associated to 6,978 news articles, and $\sim $1.6 million tweets for disinformation, collected in a period of three months (January 1st, 2019-March 18th, 2019) for sake of balance of the two classes, which hold 5,775 distinct articles. Diffusion censoring effects BIBREF14 were correctly taken into account in both collection procedures. We provide in Figure FIGREF4 the distribution of articles by source and political bias for both news domains.
> 
> As it is reported that conservatives and liberals exhibit different behaviors on online social platforms BIBREF19BIBREF20BIBREF21, we further assigned a political bias label to different US outlets (and therefore news articles) following the procedure described in BIBREF2. In order to assess the robustness of our method, we performed classification experiments by training only on left-biased (or right-biased) outlets of both disinformation and mainstream domains and testing on the entire set of sources, as well as excluding particular sources that outweigh the others in terms of samples to avoid over-fitting.

#### Relevance 1064

Label: 1
> Reason
> - Summary of question: How is sources' political bias accounted for in the model?
> - Summary of passage: Outlets and articles receive political labels; side-specific training is tested on all sources.
> - Judgement: It directly describes bias assignment and robustness experiments.
> 原因
> - 问题概述：模型如何考虑不同来源的政治倾向？
> - Passage 概述：为媒体和文章标注政治倾向，单侧训练后在全部来源上测试。
> - 判断：它直接描述倾向标注和稳健性实验。

#### Passage 1065

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In Table 3 we first provide classification performances on the US dataset for the LR classifier evaluated on the size class described in Table 1. We can observe that in all instances our methodology performs better than a random classifier (50% AUROC), with AUROC values above 85% in all cases.
> 
> For what concerns political biases, as the classes of mainstream and disinformation networks are not balanced (e.g., 1,292 mainstream and 4,149 disinformation networks with right bias) we employ a Balanced Random Forest with default parameters (as provided in imblearn Python package BIBREF35). In order to test the robustness of our methodology, we trained only on left-biased networks or right-biased networks and tested on the entire set of sources (relative to the US dataset); we provide a comparison of AUROC values for both biases in Figure 4. We can notice that our multi-layer approach still entails significant results, thus showing that it can accurately distinguish mainstream news from disinformation regardless of the political bias. We further corroborated this result with additional classification experiments, that show similar performances, in which we excluded from the training/test set two specific sources (one at a time and both at the same time) that outweigh the others in terms of data samples–respectively "breitbart.com" for right-biased sources and "politicususa.com" for left-biased ones.
> 
> We performed classification experiments on the Italian dataset using the LR classifier and different size classes (we excluded $[1000, +\infty )$ which is empty); we show results for different evaluation metrics in Table 3. We can see that despite the limited number of samples (one order of magnitude smaller than the US dataset) the performances are overall in accordance with the US scenario. As shown in Table 4, we obtain results which are much better than our baseline in all size classes (see Table 4):
> 
> In the US dataset our multi-layer methodology performs much better in all size classes except for large networks ($[1000, +\infty )$ size class), reaching up to 13% improvement on smaller networks ($[0, 100)$ size class);
> 
> In the IT dataset our multi-layer methodology outperforms the baseline in all size classes, with the maximum performance gain (20%) on medium networks ($[100, 1000)$ size class); the baseline generally

#### Relevance 1065

Label: 1
> Reason
> - Summary of question: How is sources' political bias accounted for in the model?
> - Summary of passage: Balanced Random Forest handles imbalance in left-only or right-only training experiments.
> - Judgement: It details the classifier and bias-controlled train-test design.
> 原因
> - 问题概述：模型如何考虑不同来源的政治倾向？
> - Passage 概述：在仅左倾或仅右倾训练实验中使用平衡随机森林处理类别不平衡。
> - 判断：它详细说明分类器及控制政治倾向的训练测试设计。

#### Passage 1066

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this work we tackled the problem of the automatic classification of news articles in two domains, namely mainstream and disinformation news, with a language-independent approach which is based solely on the diffusion of news items on Twitter social platform. We disentangled different types of interactions on Twitter to accordingly build a multi-layer representation of news diffusion networks, and we computed a set of global network properties–separately for each layer–in order to encode each network with a tuple of features. Our goal was to investigate whether a multi-layer representation performs better than one layer BIBREF11, and to understand which of the features, observed at given layers, are most effective in the classification task.
> 
> Experiments with an off-the-shelf classifier such as Logistic Regression on datasets pertaining to two different media landscapes (US and Italy) yield very accurate classification results (AUROC up to 94%), even when accounting for the different political bias of news sources, which are far better than our baseline BIBREF11 with improvements up to 20%. Classification performances using single layers show that the layer of mentions alone entails better performance w.r.t other layers in both countries.
> 
> We also highlighted the most discriminative features across different layers in both countries; the results suggest that differences between the two news domains might be country-independent but rather due only to the typology of content shared, and that disinformation news shape broader and deeper cascades.
> 
> Additional experiments involving the temporal evolution of Twitter diffusion networks show that our methodology can accurate classify mainstream and disinformation news after a few hours of propagation on the platform.
> 
> Overall, our results prove that the topological features of multi-layer diffusion networks might be effectively exploited to detect online disinformation. We do not deny the presence of deceptive efforts to orchestrate the regular spread of information on social media via content amplification and manipulation BIBREF37BIBREF38. On the contrary, we postulate that such hidden forces might play to accentuate the discrepancies between the diffusion patterns of disinformation and mainstream news (and thus to make our methodology effective).
> 
> In the future we aim to further investigate three directions: (1) employ temporal networks to represent news diffusion and apply classification techniques that take into account the

#### Relevance 1066

Label: 1
> Reason
> - Summary of question: How is sources' political bias accounted for in the model?
> - Summary of passage: The conclusion reports robust diffusion-network classification despite political bias.
> - Judgement: It states that source political bias is accounted for in the experiments, supporting interpretation of the detailed controls elsewhere.
> 原因
> - 问题概述：模型如何考虑不同来源的政治倾向？
> - Passage 概述：结论报告扩散网络分类在政治倾向下仍稳健。
> - 判断：它说明实验考虑来源政治倾向，可辅助理解其他片段中的具体控制方式。

#### Passage 1068

Retrieved by: Dense, Hybrid RRF

> In recent years there has been increasing interest on the issue of disinformation spreading on online social media. Global concern over false (or "fake") news as a threat to modern democracies has been frequently raised–ever since 2016 US Presidential elections–in correspondence of events of political relevance, where the proliferation of manipulated and low-credibility content attempts to drive and influence people opinions BIBREF0BIBREF1BIBREF2BIBREF3.
> 
> Researchers have highlighted several drivers for the diffusion of such malicious phenomenon, which include human factors (confirmation bias BIBREF4, naive realism BIBREF5), algorithmic biases (filter bubble effect BIBREF0), the presence of deceptive agents on social platforms (bots and trolls BIBREF6) and, lastly, the formation of echo chambers BIBREF7 where people polarize their opinions as they are insulated from contrary perspectives.
> 
> The problem of automatically detecting online disinformation news has been typically formulated as a binary classification task (i.e. credible vs non-credible articles), and tackled with a variety of different techniques, based on traditional machine learning and/or deep learning, which mainly differ in the dataset and the features they employ to perform the classification. We may distinguish three approaches: those built on content-based features, those based on features extracted from the social context, and those which combine both aspects. A few main challenges hinder the task, namely the impossibility to manually verify all news items, the lack of gold-standard datasets and the adversarial setting in which malicious content is created BIBREF3BIBREF6.
> 
> In this work we follow the direction pointed out in a few recent contributions on the diffusion of disinformation compared to traditional and objective information. These have shown that false news spread faster and deeper than true news BIBREF8, and that social bots and echo chambers play an important role in the diffusion of malicious content BIBREF6, BIBREF7. Therefore we focus on the analysis of spreading patterns which naturally arise on social platforms as a consequence of multiple interactions between users, due to the increasing trend in online sharing of news BIBREF0.
> 
> A deep learning framework for detection of fake news cascades is provided in BIBREF9, where the authors refer to BIBREF8 in order to collect Twitter cascades pertaining to verified false and true rumors. They employ geometric deep learning, a novel paradigm

#### Relevance 1068

Label: 1
> Reason
> - Summary of question: How is sources' political bias accounted for in the model?
> - Summary of passage: The introduction reviews disinformation drivers and diffusion-based detection.
> - Judgement: Politically driven disinformation and source differences motivate the bias controls investigated in the model.
> 原因
> - 问题概述：模型如何考虑不同来源的政治倾向？
> - Passage 概述：引言回顾虚假信息成因和基于扩散的检测。
> - 判断：政治驱动的虚假信息和来源差异说明模型中偏见控制的研究动机。

### BM25

#### Passage 1067

Retrieved by: BM25

> We used a set of global network indicators which allow us to encode each network layer by a tuple of features. Then we simply concatenated tuples as to represent each multi-layer network with a single feature vector. We used the following global network properties:
> 
> Number of Strongly Connected Components (SCC): a Strongly Connected Component of a directed graph is a maximal (sub)graph where for each pair of vertices $u,v$ there is a path in each direction ($u\rightarrow v$, $v\rightarrow u$).
> 
> Size of the Largest Strongly Connected Component (LSCC): the number of nodes in the largest strongly connected component of a given graph.
> 
> Number of Weakly Connected Components (WCC): a Weakly Connected Component of a directed graph is a maximal (sub)graph where for each pair of vertices $(u, v)$ there is a path $u \leftrightarrow v$ ignoring edge directions.
> 
> Size of the Largest Weakly Connected Component (LWCC): the number of nodes in the largest weakly connected component of a given graph.
> 
> Diameter of the Largest Weakly Connected Component (DWCC): the largest distance (length of the shortest path) between two nodes in the (undirected version of) largest weakly connected component of a graph.
> 
> Average Clustering Coefficient (CC): the average of the local clustering coefficients of all nodes in a graph; the local clustering coefficient of a node quantifies how close its neighbours are to being a complete graph (or a clique). It is computed according to BIBREF28.
> 
> Main K-core Number (KC): a K-core BIBREF13 of a graph is a maximal sub-graph that contains nodes of internal degree $k$ or more; the main K-core number is the highest value of $k$ (in directed graphs the total degree is considered).
> 
> Density (d): the density for directed graphs is $d=\frac{|E|}{|V||V-1|}$, where $|E|$ is the number of edges and $|N|$ is the number of vertices in the graph; the density equals 0 for a graph without edges and 1 for a complete graph.
> 
> Structural virality of the largest weakly connected component (SV): this measure is defined in BIBREF14 as the average distance between all pairs of nodes in a cascade tree or, equivalently, as the average depth of nodes, averaged over all nodes in turn acting as a root; for $|V|

#### Relevance 1067

Label: 0
> Reason
> - Summary of question: How is sources' political bias accounted for in the model?
> - Summary of passage: Network layers are represented by concatenated structural indicators.
> - Judgement: The topology features do not describe treatment of political bias.
> 原因
> - 问题概述：模型如何考虑不同来源的政治倾向？
> - Passage 概述：使用拼接的结构指标表示网络各层。
> - 判断：拓扑特征未说明如何处理政治倾向。

### Dense

#### Passage 1069

Retrieved by: Dense

> In this work we formulate our classification problem as follows: given two classes of news articles, respectively $D$ (disinformation) and $M$ (mainstream), a set of news articles $A_i$ and associated class labels $C_i \in \lbrace D,M\rbrace $, and a set of tweets $\Pi _i=\lbrace T_i^1, T_i^2, ...\rbrace $ each of which contains an Uniform Resource Locator (URL) pointing explicitly to article $A_i$, predict the class $C_i$ of each article $A_i$. There is huge debate and controversy on a proper taxonomy of malicious and deceptive information BIBREF1BIBREF2BIBREF15BIBREF16BIBREF17BIBREF3BIBREF11. In this work we prefer the term disinformation to the more specific fake news to refer to a variety of misleading and harmful information. Therefore, we follow a source-based approach, a consolidated strategy also adopted by BIBREF6BIBREF16BIBREF2BIBREF1, in order to obtain relevant data for our analysis. We collected:
> 
> Disinformation articles, published by websites which are well-known for producing low-credibility content, false and misleading news reports as well as extreme propaganda and hoaxes and flagged as such by reputable journalists and fact-checkers;
> 
> Mainstream news, referring to traditional news outlets which deliver factual and credible information.
> 
> We believe that this is currently the most reliable classification approach, but it entails obvious limitations, as disinformation outlets may also publish true stories and likewise misinformation is sometimes reported on mainstream media. Also, given the choice of news sources, we cannot test whether our methodology is able to classify disinformation vs factual but not mainstream news which are published on niche, non-disinformation outlets.

#### Relevance 1069

Label: 1
> Reason
> - Summary of question: How is sources' political bias accounted for in the model?
> - Summary of passage: Source credibility assigns mainstream and disinformation class labels.
> - Judgement: Source-based class assignment explains the outlet-labeling setup needed to interpret the separate political-bias controls.
> 原因
> - 问题概述：模型如何考虑不同来源的政治倾向？
> - Passage 概述：按来源可信度赋予主流及虚假信息类别标签。
> - 判断：基于来源的类别分配说明理解另行政治偏见控制所需的媒体标记设置。

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1070

Retrieved by: Hybrid RRF followed by BGE reranking

> patterns of disinformation and mainstream news (and thus to make our methodology effective).
> 
> In the future we aim to further investigate three directions: (1) employ temporal networks to represent news diffusion and apply classification techniques that take into account the sequential aspect of data (e.g. recurrent neural networks); (2) carry out an extensive comparison of the diffusion of disinformation and mainstream news across countries to investigate deeper the presence of differences and similarities in sharing patterns; (3) leverage our network-based features in addition to state-of-the-art text-based approaches for "fake news" dete ction in order to deliver a real-world system to detect misleading and harmful information spreading on social media.

#### Relevance 1070

Label: 0
> Reason
> - Summary of question: How is sources' political bias accounted for in the model?
> - Summary of passage: Future work proposes temporal models, country comparisons and text features.
> - Judgement: It does not explain how source political bias is included.
> 原因
> - 问题概述：模型如何考虑不同来源的政治倾向？
> - Passage 概述：未来工作提出时序模型、国家比较和文本特征。
> - 判断：它未解释如何考虑来源政治倾向。

## Question 0118

Paper: Multilingual and Multi-Aspect Hate Speech Analysis

> What is their definition of hate speech?

### Common Retrieved Chunks

#### Passage 1071

Retrieved by: BM25, Hybrid RRF

> We claim that the choice of a suitable emotion representation model is key to this sub-task, given the subjective nature and social ground of the annotator's sentiment analysis. After collecting the annotation results of the pilot dataset regarding how people feel about the tweets, and observing the added categories, we adopted a range of sentiments that are in the negative and neutral scales of the hourglass of emotions introduced by BIBREF29. This model includes sentiments that are connected to objectively assessed natural language opinions, and excludes what is known as self-conscious or moral emotions such as shame and guilt. Our labels include shock, sadness, disgust, anger, fear, confusion in case of ambivalence, and indifference. This is the second multilabel task of our model.
> 
> Table TABREF20 shows more tweets making the annotators feel disgusted and angry in English, while annotators show more indifference in both French and Arabic. A relatively more frequent label in both French and Arabic is shock, therefore reflecting what some of the annotators were feeling during the labeling process.

#### Relevance 1071

Label: 1
> Reason
> - Summary of question: How does the paper define hate speech?
> - Summary of passage: Annotator reactions are labeled with negative and neutral emotions.
> - Judgement: Annotator emotions form one aspect of the paper's operational hate-speech analysis.
> 原因
> - 问题概述：论文如何定义仇恨言论？
> - Passage 概述：用负面和中性情绪标注标注者的反应。
> - 判断：标注者情绪构成论文操作性仇恨言论分析的一个方面。

#### Passage 1072

Retrieved by: BM25, Dense, Hybrid RRF

> There is little consensus on the difference between profanity and hate speech and, how to define the latter BIBREF17. As shown in Figure FIGREF11, slurs are not an unequivocal indicator of hate speech and can be part of a non-aggressive conversation, while some of the most offensive comments may come in the form of subtle metaphors or sarcasm BIBREF18. Consequently, there is no existing human annotated vocabulary that explicitly reveals the presence of hate speech, which makes the available hate speech corpora sparse and noisy BIBREF19.
> 
> Given the subjectivity and the complexity of such data, annotation schemes have rarely been made fine-grained. Table TABREF10 compares different labelsets that exist in the literature. For instance, BIBREF12 use racist, sexist, and normal as labels; BIBREF13 label their data as hateful, offensive (but not hateful), and neither, while BIBREF16 present an English dataset that records the target category based on which hate speech discriminates against people, such as ethnicity, gender, or sexual orientation and ask human annotators to classify the tweets as hate and non hate. BIBREF15 label their data as offensive, abusive, hateful, aggressive, cyberbullying, spam, and normal. On the other hand, BIBREF20 have chosen to detect ideologies of hate speech counting 40 different hate ideologies among 13 extremist hate groups.
> 
> The detection of hate speech targets is yet another challenging aspect of the annotation. BIBREF21 report the bias that exists in the current datasets towards identity words, such as women, which may later cause false predictions. They propose to debias gender identity word embeddings with additional data for training and tuning their binary classifier. We address this false positive bias problem and the common ambiguity of target detection by asking the annotators to label target attributes such as origin, gender, or religious affiliation within 16 named target groups such as refugees, or immigrants.
> 
> Furthermore, BIBREF22 have reproduced the experiment of BIBREF12 in order to study how hate speech affects the popularity of a tweet, but discovered that some tweets have been deleted. For replication purposes, we provide the community with anonymized tweet texts rather than IDs.
> 
> Non-English hate speech datasets include Italian, German, Dutch, and Arabic corpora. BIBREF6 present a dataset of Italian tweets, in which

#### Relevance 1072

Label: 1
> Reason
> - Summary of question: How does the paper define hate speech?
> - Summary of passage: Profanity is neither necessary nor sufficient; target attributes and groups aid annotation.
> - Judgement: It clarifies the paper's conceptual boundaries and target-based interpretation of hate speech.
> 原因
> - 问题概述：论文如何定义仇恨言论？
> - Passage 概述：粗口既非必要也非充分条件，标注还考虑目标属性和群体。
> - 判断：它澄清论文对仇恨言论的概念边界及基于目标的理解。

#### Passage 1073

Retrieved by: BM25, Dense, Hybrid RRF

> We rely on the general public opinion and common linguistic knowledge to assess how people view and react to hate speech. Given the subjectivity and difficulty of the task, we reminded the annotators not to let their personal opinions about the topics being discussed in the tweets influence their annotation decisions.
> 
> Our annotation guidelines explained the fact that offensive comments and hate do not necessarily come in the form of profanity. Since different degrees of discrimination work on the dehumanization of individuals or groups of people in distinct ways, we chose not to annotate the tweets within two or three classes. For instance, a sexist comment can be disrespectful, hateful, or offensive towards women. Our initial labelset was established in conformity with the prevalent anti-social behaviors people tend to deal with. We also chose to address the problem of false positives caused by the misleading use of identity words by asking the annotators to label both the target attributes and groups.

#### Relevance 1073

Label: 1
> Reason
> - Summary of question: How does the paper define hate speech?
> - Summary of passage: Guidelines describe discrimination and dehumanization without requiring profanity.
> - Judgement: It directly explains the study's operational understanding of hate and offensive speech.
> 原因
> - 问题概述：论文如何定义仇恨言论？
> - Passage 概述：指南描述歧视和非人化行为，且不要求存在粗口。
> - 判断：它直接解释研究对仇恨和冒犯言论的操作性理解。

#### Passage 1074

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> With the expanding amount of text data generated on different social media platforms, current filters are insufficient to prevent the spread of hate speech. Most internet users involved in a study conducted by the Pew Research Center report having been subjected to offensive name calling online or witnessed someone being physically threatened or harassed online. Additionally, Amnesty International within Element AI have lately reported that many women politicians and journalists are assaulted every 30 seconds on Twitter. This is despite the Twitter policy condemning the promotion of violence against people on the basis of race, ethnicity, national origin, sexual orientation, gender identity, religious affiliation, age, disability, or serious disease. Hate speech may not represent the general opinion, yet it promotes the dehumanization of people who are typically from minority groups BIBREF0, BIBREF1 and can incite hate crime BIBREF2.
> 
> Moreover, although people of various linguistic backgrounds are exposed to hate speech BIBREF3, BIBREF2, English is still at the center of existing work on toxic language analysis. Recently, some research studies have been conducted on languages such as German BIBREF4, Arabic BIBREF5, and Italian BIBREF6. However, such studies usually use monolingual corpora and do not contrast, or examine the correlations between online hate speech in different languages. On the other hand, tasks involving more than one language such as the hatEval task, which covers English and Spanish, include only separate classification tasks, namely (a) women and immigrants as target groups, (b) individual or generic hate and, (c) aggressive or non-aggressive hate speech.
> 
> Treating hate speech classification as a binary task may not be enough to inspect the motivation and the behavior of the users promoting it and, how people would react to it. For instance, the hateful tweets presented in Figure FIGREF5 show toxicity directed towards different targets, with or without using slurs, and generating several types of reactions. We believe that, in order to balance between truth and subjectivity, there are at least five important aspects in hate speech analysis. Hence, our annotations indicate (a) whether the text is direct or indirect; (b) if it is offensive, disrespectful, hateful, fearful out of ignorance, abusive, or normal; (c) the attribute based on which it discriminates against an

#### Relevance 1074

Label: 1
> Reason
> - Summary of question: How does the paper define hate speech?
> - Summary of passage: Hate speech dehumanizes people, often minorities, and may incite hate crime.
> - Judgement: It directly characterizes the defining harm and targets.
> 原因
> - 问题概述：论文如何定义仇恨言论？
> - Passage 概述：仇恨言论将人非人化，常针对少数群体，并可能煽动仇恨犯罪。
> - 判断：它直接说明界定仇恨言论的伤害性质和目标。

#### Passage 1076

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> in hate speech analysis. Hence, our annotations indicate (a) whether the text is direct or indirect; (b) if it is offensive, disrespectful, hateful, fearful out of ignorance, abusive, or normal; (c) the attribute based on which it discriminates against an individual or a group of people; (d) the name of this group; and (e) how the annotators feel about its content within a range of negative to neutral sentiments. To the best of our knowledge there are no other hate speech datasets that attempt to capture fear out of ignorance in hateful tweets or examine how people react to hate speech. We claim that our multi-aspect annotation schema would provide a valuable insight into several linguistic and cultural differences and bias in hate speech.
> 
> We use Amazon Mechanical Turk to label around 13,000 potentially derogatory tweets in English, French, and Arabic based on the above mentioned aspects and, regard each aspect as a prediction task. Since in natural language processing, there is a peculiar interest in multitask learning, where different tasks can be used to help each other BIBREF7, BIBREF8, BIBREF9, we use a unified model to handle the annotated data in all three languages and five tasks. We adopt BIBREF8 as a learning algorithm adapted to loosely related tasks such as our five annotated aspects and, use the Babylon cross-lingual embeddings BIBREF10 to align the three languages. We compare the multilingual multitask learning settings with monolingual multitask, multilingual single-task, and monolingual single-task learning settings respectively. Then, we report the performance results of the different settings and discuss how each task affects the remaining ones. We release our dataset and code to the community to extend research work on multilingual hate speech detection and classification.

#### Relevance 1076

Label: 1
> Reason
> - Summary of question: How does the paper define hate speech?
> - Summary of passage: Annotations capture directness, hostility, discriminatory attributes, target groups and reactions.
> - Judgement: It partially specifies how hate speech is operationalized through multiple aspects.
> 原因
> - 问题概述：论文如何定义仇恨言论？
> - Passage 概述：标注涵盖直接性、敌意、歧视属性、目标群体和反应。
> - 判断：它部分说明如何通过多个方面操作化界定仇恨言论。

### BM25

#### Passage 1075

Retrieved by: BM25

> After annotating the pilot dataset, we noticed common misconceptions regarding race, ethnicity, and nationality, therefore we merged these attributes into one label origin. Then, we asked the annotators to determine whether the tweet insults or discriminates against people based on their (1) origin, (2) religious affiliation, (3) gender, (4) sexual orientation, (5) special needs or (6) other. Table TABREF20 shows there are fewer tweets targeting disability in Arabic compared to English and French and no tweets insulting people based on their sexual orientation which may be due to the fact that the labels of gender, gender identity, and sexual orientation use almost the same wording. On the other hand, French contains a small number of tweets targeting people based on their gender in comparison to English and Arabic. We have observed significant differences in terms of target attributes in the three languages. More data may help us examine the problems affecting targets of different linguistic backgrounds.

#### Relevance 1075

Label: 1
> Reason
> - Summary of question: How does the paper define hate speech?
> - Summary of passage: Annotators identify insults or discrimination based on origin, religion, gender and other attributes.
> - Judgement: It supplies the target-based criteria used to operationalize hate speech.
> 原因
> - 问题概述：论文如何定义仇恨言论？
> - Passage 概述：标注者识别基于出身、宗教、性别等属性的侮辱或歧视。
> - 判断：它提供界定仇恨言论的目标属性标准。

### Dense

#### Passage 1077

Retrieved by: Dense

> that some tweets have been deleted. For replication purposes, we provide the community with anonymized tweet texts rather than IDs.
> 
> Non-English hate speech datasets include Italian, German, Dutch, and Arabic corpora. BIBREF6 present a dataset of Italian tweets, in which the annotations capture the degree of intensity of offensive and aggressive tweets, in addition to whether the tweets are ironic and contain stereotypes or not. BIBREF2 have collected more than 500 German tweets against refugees, and annotated them as hateful and not hateful. BIBREF23 detect bullies and victims among youngsters in Dutch comments on AskFM, and classify cyberbullying comments as insults or threats. Moreover, BIBREF5 provide a corpus of Arabic sectarian speech.
> 
> Another predominant phenomenon in hate speech corpora is code switching. BIBREF24 present a dataset of code mixed Hindi-English tweets, while BIBREF25 report the presence of Hindi tokens in English data and use multilingual word embeddings to deal with this issue when detecting toxicity. Similarly, we use such embeddings to take advantage of the multilinguality and comparability of our corpora during the classification.
> 
> Our dataset is the first trilingual dataset comprising English, French, and Arabic tweets that encompasses various targets and hostility types. Additionally, to the best of our knowledge, this is the first work that examines how annotators react to hate speech comments.
> 
> To fully exploit the collected annotations, we tested multitask learning on our dataset. Multitask learning BIBREF7 allows neural networks to share parameters with one another and, thus, learn from related tasks. It has been used in different NLP tasks such as parsing BIBREF9, dependency parsing BIBREF26, neural machine translation BIBREF27, sentiment analysis BIBREF28, and other tasks. Multitask learning architectures tackle challenges that include sharing the label space and the question of private and shared space for loosely related tasks BIBREF8, for which techniques may involve a massive space of potential parameter sharing architectures.

#### Relevance 1077

Label: 1
> Reason
> - Summary of question: How does the paper define hate speech?
> - Summary of passage: Related multilingual corpora and multitask learning methods are reviewed.
> - Judgement: The dataset's target and hostility types provide partial clues to the scope of hate speech studied.
> 原因
> - 问题概述：论文如何定义仇恨言论？
> - Passage 概述：回顾相关多语言语料和多任务学习方法。
> - 判断：数据集涵盖的目标和敌意类型为所研究仇恨言论范围提供部分线索。

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1078

Retrieved by: Hybrid RRF followed by BGE reranking

> Considering the cultural differences and commonly debated topics in the main geographic regions where English, French, and Arabic are spoken, searching for equivalent terms in the three languages led to different results at first. Therefore, after looking for 1,000 tweets per 15 more or less equivalent phrases in the three languages, we revised our search words three times by questioning the results, adding phrases, and taking off unlikely ones in each of the languages. In fact, we started our data collection by searching for common slurs and demeaning expressions such as “go back to where you come from”. Then, we observed that discussions about controversial topics, such as feminism in general, illegal immigrants in English, Islamo-gauchisme (“Islamic leftism") in French, or Iran in Arabic were more likely to provoke disputes, comments filled with toxicity and thus, notable insult patterns that we looked for in subsequent search rounds.

#### Relevance 1078

Label: 1
> Reason
> - Summary of question: How does the paper define hate speech?
> - Summary of passage: Slurs and controversial topics guide iterative tweet collection.
> - Judgement: Slurs and demeaning examples illustrate the kinds of potentially hateful speech sought, complementing the guidelines.
> 原因
> - 问题概述：论文如何定义仇恨言论？
> - Passage 概述：通过辱骂词和争议主题迭代收集推文。
> - 判断：辱骂和贬损示例说明筛选哪些潜在仇恨言论，可补充标注指南。

#### Passage 1079

Retrieved by: Hybrid RRF followed by BGE reranking

> We initially put samples of 100 tweets in each of the three languages on Amazon Mechanical Turk. We showed the annotators the tweet along with lists of labels describing (a) whether it is direct or indirect hate speech; (b) if the tweet is dangerous, offensive, hateful, disrespectful, confident or supported by some URL, fearful out of ignorance, or other; (c) the target attribute based on which it discriminates against people, specifically, race, ethnicity, nationality, gender, gender identity, sexual orientation, religious affiliation, disability, and other (“other” could refer to political ideologies or social classes.); (d) the name of its target group, and (e) whether the annotators feel anger, sadness, fear or nothing about the tweets.
> 
> Each tweet has been labeled by three annotators. We have provided them with additional text fields to fill in with labels or adjectives that would (1) better describe the tweet, (2) describe how they feel about it more accurately, and (3) name the group of people the tweet shows bias against. We kept the most commonly used labels from our initial labelset, took off some of the initial class names and added frequently introduced labels, especially the emotions of the annotators when reading the tweets and the names of the target groups. For instance, after this step, we have ended up merging race, ethnicity, nationality into one label origin given common confusions we noticed and; added disgust and shock to the emotion labelset; and introduced socialists as a target group label since many annotators have suggested these labels.

#### Relevance 1079

Label: 1
> Reason
> - Summary of question: How does the paper define hate speech?
> - Summary of passage: Pilot labels describe hostility and discrimination against identity-based target groups.
> - Judgement: It supplies operational annotation criteria while documenting their refinement.
> 原因
> - 问题概述：论文如何定义仇恨言论？
> - Passage 概述：试标标签描述敌意及针对身份群体的歧视。
> - 判断：它在说明标签修订时给出操作性标注标准。

#### Passage 1080

Retrieved by: Hybrid RRF followed by BGE reranking

> We report and discuss the results of five classification tasks: (1) the directness of the speech, (2) the hostility type of the tweet, (3) the discriminating target attribute, (4) the target group, and (5) the annotator's sentiment.

#### Relevance 1080

Label: 1
> Reason
> - Summary of question: How does the paper define hate speech?
> - Summary of passage: Five tasks cover directness, hostility, discriminatory attributes, targets and sentiment.
> - Judgement: This gives partial evidence of the multi-aspect operational characterization, though no full definition.
> 原因
> - 问题概述：论文如何定义仇恨言论？
> - Passage 概述：五项任务涵盖直接性、敌意、歧视属性、目标和情绪。
> - 判断：它部分说明多方面操作性刻画方式，但未给出完整定义。

## Question 0119

Paper: A Context-Aware Approach for Detecting Check-Worthy Claims in Political Debates

> Does the baseline use any contextual information?

### Common Retrieved Chunks

#### Passage 1081

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> Table TABREF21 shows the performance of our models when using all features described in Section SECREF4: see the SVM$_{All}$ and the FNN$_{All}$ rows. In order to put the numbers in perspective, we also show the results for five increasingly competitive baselines.
> 
> First, there is a random baseline, followed by an SVM classifier based on a bag-of-words representation with TF.IDF weights learned on the training data. Then come three versions of the ClaimBuster system: CB-Platform uses scores from the online demo, which we accessed on December 20, 2016, and SVM$_{CBfeat}$ and FNN$_{CBfeat}$ are our re-implementations, trained on our dataset.
> 
> We can see that all systems perform well above the random baseline. The three versions of ClaimBuster also outperform the TF.IDF baseline on most measures. Moreover, our reimplementation of ClaimBuster performs better than the online platform in terms of MAP. This is expected as their system is trained on a different dataset and it may suffer from testing on slightly out-of-domain data. At the same time, this is reassuring for our implementation of the features, and allows for a more realistic comparison to the ClaimBuster system.
> 
> More importantly, both the SVM and the FNN versions of our system consistently outperform all three versions of ClaimBuster on all measures. This means that the extra information coded in our model, mainly more linguistic, structural, and contextual features, has an important contribution to the overall performance.
> 
> We can further see that the neural network model, FNN$_{All}$, clearly outperforms the SVM model: consistently on all measures. As an example, with the precision values achieved by FNN$_{All}$, the system would rank on average 4 positive examples in the list of its top-5 choices, and also 14-15 in the top-20 list. Considering the recall at the first $R$ sentences, we will be able to encounter 43% of the total number of check-worthy sentences. This is quite remarkable given the difficulty of the task.

#### Relevance 1081

Label: 1
> Reason
> - Summary of question: Does the baseline use contextual information?
> - Summary of passage: ClaimBuster and TF-IDF baselines are contrasted with added contextual features.
> - Judgement: It provides indirect evidence that contextual features are additions beyond these baselines.
> 原因
> - 问题概述：基线是否使用上下文信息？
> - Passage 概述：将 ClaimBuster 和 TF-IDF 基线与新增上下文特征比较。
> - 判断：它间接表明上下文特征是在这些基线之外新增的信息。

#### Passage 1082

Retrieved by: BM25, Dense, Hybrid RRF

> We created a new dataset called CW-USPD-2016 (check-worthiness in the US presidential debates 2016) for finding check-worthy claims in context. In particular, we used four transcripts of the 2016 US election: one vice-presidential and three presidential debates. For each debate, we used the publicly-available manual analysis about it from nine reputable fact-checking sources, as shown in Table TABREF7. This could include not just a statement about factuality, but any free text that journalists decided to add, e.g., links to biographies or behavioral analysis of the opponents and moderators. We converted this to binary annotation about whether a particular sentence was annotated for factuality by a given source. Whenever one or more annotations were about part of a sentence, we selected the entire sentence, and when an annotation spanned over multiple sentences, we selected each of them.
> 
> Ultimately, we ended up with a dataset of four debates, with a total of 5,415 sentences. The agreement between the sources was low as Table TABREF8 shows: only one sentence was selected by all nine sources, 57 sentences by at least five, 197 by at least three, 388 by at least two, and 880 by at least one. The reason for this is that the different media aimed at annotating sentences according to their own editorial line, rather than trying to be exhaustive in any way. This suggests that the task of predicting which sentence would contain check-worthy claims will be challenging. Thus, below we focus on a ranking task rather than on absolute predictions. Moreover, we predict which sentence would be selected (i) by at least one of the media, or (ii) by a specific medium.
> 
> Note that the investigative journalists did not select the check-worthy claims in isolation. Our analysis shows that these include claims that were highly disputed during the debate, that were relevant to the topic introduced by the moderator, etc. We will make use of these contextual dependencies below, which is something that was not previously tried in related work.

#### Relevance 1082

Label: 1
> Reason
> - Summary of question: Does the baseline use contextual information?
> - Summary of passage: The dataset discussion says exploiting contextual dependencies was not tried in prior work.
> - Judgement: It provides supporting evidence that prior systems omit the proposed context modeling.
> 原因
> - 问题概述：基线是否使用上下文信息？
> - Passage 概述：数据集讨论指出既有工作未利用这些上下文依赖。
> - 判断：它支持既有系统未采用所提上下文建模的判断。

#### Passage 1083

Retrieved by: BM25, Dense, Hybrid RRF

> The feature groups in this subsection contain a mixture of sentence- and of contextual-level features. For example, if we use a discourse parser to parse the target sentence only, any features we extract from the parse would be sentence-level. However, if we parse an entire segment, we would also have contextual features.
> 
> Topics (300+3 S+C features): Some topics are more likely to be associated with check-worthy claims, and thus we have features modeling the topics in the target sentence as well as in the surrounding context. We trained a Latent Dirichlet Allocation (LDA) topic model BIBREF22 on all political speeches and debates in The American Presidency Project using all US presidential debates in the 2007–2016 period. We had 300 topics, and we used the distribution over the topics as a representation for the target sentence. We further modeled the context using cosines with such representations for the previous, the current, and the next segment.
> 
> Embeddings (300+3 S+C features): We also modeled semantics using word embeddings. We used the pre-trained 300-dimensional Google News word embeddings by BIBREF23 to compute an average embedding vector for the target sentence, and we used the 300 coordinates of that vector. We also modeled the context as the cosine between that vector and the vectors for three segments: the previous, the current, and the following one.
> 
> Discourse (2+18 S+C features): We saw above that contradiction can signal the presence of check-worthy claims, and contradiction can be expressed by a discourse relation such as Contrast. As other discourse relations such as Background, Cause, and Elaboration can also be useful, we used a discourse parser BIBREF24 to parse the entire segment, and we focused on the relationship between the target sentence and the other sentences in its segment; this gave rise to 18 contextual indicator features. We further analyzed the internal structure of the target sentence —how many nuclei and how many satellites it contains—, which gave rise to two sentence-level features.
> 
> Contradictions (1+4 S+C features): Many claims selected for fact-checking contain contradictions to what has been said earlier, as in the example below (from the 3rd presidential debate):
> 
> We model this by counting the negations in the target sentence as found in

#### Relevance 1083

Label: 1
> Reason
> - Summary of question: Does the baseline use contextual information?
> - Summary of passage: The proposed model uses topic, embedding, discourse and contradiction context features.
> - Judgement: The sentence-versus-context feature distinction helps compare the proposed context modeling with baseline inputs.
> 原因
> - 问题概述：基线是否使用上下文信息？
> - Passage 概述：所提模型使用主题、嵌入、篇章和矛盾上下文特征。
> - 判断：句内与上下文特征的区分有助于比较所提上下文建模与基线输入。

#### Passage 1084

Retrieved by: BM25, Dense, Hybrid RRF

> Position (3 C features): A sentence on the boundaries of a speaker's segment could contain a reaction to another statement or could provoke a reaction, which in turn could signal a check-worthy claim. Thus, we added information about the position of the target sentence in its segment: whether it is first/last, as well as its reciprocal rank in the list of sentences in that segment.
> 
> Segment sizes (3 C features): The size of the segment belonging to one speaker might indicate whether the target sentence is part of a long speech, makes a short comment or is in the middle of a discussion with lots of interruptions. The size of the previous and of the next segments is also important in modeling the dialogue flow. Thus, we include three features with the sizes of the previous, the current and the next segments.
> 
> Metadata (8 C features): Check-worthy claims often contain mutual accusations between the opponents, as the following example shows (from the 2nd presidential debate):
> 
> Thus, we use a feature that indicates whether the target sentence mentions the name of the opponent, whether the speaker is the moderator, and also who is speaking (3 features). We further use three binary features, indicating whether the target sentence is followed by a system message: applause, laugh, or cross-talk.

#### Relevance 1084

Label: 1
> Reason
> - Summary of question: Does the baseline use contextual information?
> - Summary of passage: Context features include sentence position, segment size and speaker metadata.
> - Judgement: The explicit context-feature inventory provides comparison evidence when assessing what the baseline omits.
> 原因
> - 问题概述：基线是否使用上下文信息？
> - Passage 概述：上下文特征包括句子位置、片段大小和说话者元数据。
> - 判断：明确的上下文特征清单可用于比较基线缺少哪些信息。

#### Passage 1085

Retrieved by: BM25, Hybrid RRF

> CNN, NPR, and PolitiFact, and which we release to the research community.
> 
> Modeling the context: We develop a novel approach for automatically predicting which claims should be prioritized for fact-checking, based on a rich input representation. In particular, we model not only the textual content, but also the context: how the target claim relates to the current segment, to neighboring segments and sentences, and to the debate as a whole, and also how the opponents and the public react to it.
> 
> State-of-the-art results: We achieve state-of-the-art results, outperforming a strong rivaling system by a margin, while also demonstrating that this improvement is due primarily to our modeling of the context.
> 
> We model the problem as a ranking task, and we train both Support Vector Machines (SVM) and Feed-forward Neural Networks (FNN) obtaining state-of-the-art results. We also analyze the relevance of the specific feature groups and we show that modeling the context yields a significant boost in performance. Finally, we also analyze whether we can learn to predict which facts are check-worthy with respect to each of the individual media sources, thus capturing their biases. It is worth noting that while trained on political debates, many features of our model can be potentially applied to other kinds of information sources, e.g., interviews and news.
> 
> The rest of the paper is organized as follows: Section SECREF2 discusses related work. Section SECREF3 describes the process of gathering and annotating our political debates dataset. Section SECREF4 presents our supervised approach to predicting fact-checking worthiness, including the explanation of the model and the information sources we use. Section SECREF5 presents the evaluation setup and discusses the results. Section SECREF6 provides further analysis. Finally, Section SECREF7 presents the conclusions and outlines some possible directions for future research.

#### Relevance 1085

Label: 1
> Reason
> - Summary of question: Does the baseline use contextual information?
> - Summary of passage: The proposed system models surrounding statements, debate structure and audience reactions.
> - Judgement: It connects the advantage over a rival system to context modeling, supporting the baseline comparison.
> 原因
> - 问题概述：基线是否使用上下文信息？
> - Passage 概述：所提系统建模相邻陈述、辩论结构和观众反应。
> - 判断：它将超越对比系统的收益与上下文建模联系，支持基线比较。

#### Passage 1086

Retrieved by: Dense, Hybrid RRF

> Table TABREF27 shows the results when using all features vs. excluding the contextual features vs. using the contextual features only. We can see that the contextual features have a major impact on performance: excluding them yields major drop for all measures, e.g., MAP drops from .427 to .385, and P@5 drops from .800 to .550. The last two rows in the table show that using contextual features only performs about the same as CB Platform (which uses no contextual features at all).

#### Relevance 1086

Label: 1
> Reason
> - Summary of question: Does the baseline use contextual information?
> - Summary of passage: The analysis explicitly says CB Platform uses no contextual features.
> - Judgement: It directly answers the question: the ClaimBuster baseline does not use context.
> 原因
> - 问题概述：基线是否使用上下文信息？
> - Passage 概述：分析明确指出 CB Platform 完全不使用上下文特征。
> - 判断：它直接回答问题：ClaimBuster 基线不使用上下文。

### BM25

None

### Dense

#### Passage 1087

Retrieved by: Dense

> In the experiments above, we have been trying to predict whether a sentence is check-worthy in general, i.e., with respect to at least one source; this is how we trained and this is how we evaluated our models. Here, we want to evaluate how well our models perform at finding sentences that contain claims that would be judged as worthy for fact-checking with respect to each of the individual sources. The purpose is to see to what extent we can make our system potentially useful for a particular medium.
> 
> Another interesting question is whether we should use our generic system or we should retrain with respect to the target medium. Table TABREF31 shows the results for such a comparison, and it further compares to CB Platform. We can see that for all nine media, our model outperforms CB Platform in terms of MAP and P@50; this is also true for the other measures in most cases.
> 
> Moreover, we can see that training on all media is generally preferable to training on the target medium only, which shows that they do follow some common principles for selecting what is check-worthy; this means that a general system could serve journalists in all nine, and possibly other, media. Overall, our model works best on PolitiFact, which is a reputable source for fact checking, as this is their primary expertise. We also do well on NPR, NYT, Guardian, and FactCheck, which is quite encouraging.

#### Relevance 1087

Label: 1
> Reason
> - Summary of question: Does the baseline use contextual information?
> - Summary of passage: Generic and source-specific training are compared against CB Platform.
> - Judgement: It identifies CB Platform as the comparator across media, helping connect baseline identity with its feature description elsewhere.
> 原因
> - 问题概述：基线是否使用上下文信息？
> - Passage 概述：将通用和来源专属训练与 CB Platform 比较。
> - 判断：它指出 CB Platform 是跨媒体对比基线，有助于与其他片段中的特征描述对应。

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1088

Retrieved by: Hybrid RRF followed by BGE reranking

> In this section, we present some in-depth analysis and further discussion.

#### Relevance 1088

Label: 0
> Reason
> - Summary of question: Does the baseline use contextual information?
> - Summary of passage: The sentence introduces an analysis and discussion section.
> - Judgement: It contains no baseline or contextual-feature information.
> 原因
> - 问题概述：基线是否使用上下文信息？
> - Passage 概述：该句引出分析讨论章节。
> - 判断：它不包含基线或上下文特征信息。

#### Passage 1089

Retrieved by: Hybrid RRF followed by BGE reranking

> The current coverage of the political landscape in the press and in social media has led to an unprecedented situation. Like never before, a statement in an interview, a press release, a blog note, or a tweet can spread almost instantaneously and reach the public in no time. This proliferation speed has left little time for double-checking claims against the facts, which has proven critical in politics, e.g., during the 2016 presidential campaign in the USA, which was arguably impacted by fake news in social media and by false claims.
> 
> Investigative journalists and volunteers have been working hard trying to get to the root of a claim and to present solid evidence in favor or against it. Manual fact-checking has proven very time-consuming, and thus automatic methods have been proposed as a way to speed-up the process. For instance, there has been work on checking the factuality/credibility of a claim, of a news article, or of an information source BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, BIBREF5, BIBREF6, BIBREF7. However, less attention has been paid to other steps of the fact-checking pipeline, which is shown in Figure FIGREF1.
> 
> The process starts when a document is made public. First, an intrinsic analysis is carried out in which check-worthy text fragments are identified. Then, other documents that might support or rebut a claim in the document are retrieved from various sources. Finally, by comparing a claim against the retrieved evidence, a system can determine whether the claim is likely true or likely false. For instance, BIBREF8 do this on the basis of a knowledge graph derived from Wikipedia. The outcome could then be presented to a human expert for final judgment.
> 
> In this paper, we focus on the first step: predicting check-worthiness of claims. Our contributions can be summarized as follows:
> 
> New dataset: We build a new dataset of manually-annotated claims, extracted from the 2016 US presidential and vice-presidential debates, which we gathered from nine reputable sources such as CNN, NPR, and PolitiFact, and which we release to the research community.
> 
> Modeling the context: We develop a novel approach for automatically predicting which claims should be prioritized for fact-checking, based on a rich input representation. In particular, we model

#### Relevance 1089

Label: 1
> Reason
> - Summary of question: Does the baseline use contextual information?
> - Summary of passage: The introduction motivates check-worthiness prediction and a new debate dataset.
> - Judgement: The introduction explicitly presents context modeling, providing the proposed side of the baseline-context comparison.
> 原因
> - 问题概述：基线是否使用上下文信息？
> - Passage 概述：引言说明核查价值预测及新辩论数据集的动机。
> - 判断：引言明确介绍上下文建模，提供基线是否使用上下文这一对比的所提方法一侧信息。

#### Passage 1090

Retrieved by: Hybrid RRF followed by BGE reranking

> We have developed a novel approach for automatically finding check-worthy claims in political debates, which is an understudied problem, despite its importance. Unlike previous work, which has looked primarily at sentences in isolation, here we have focused on the context: relationship between the target statement and the larger context of the debate, interaction between the opponents, and reaction by the moderator and by the public.
> 
> Our models have achieved state-of-the-art results, outperforming a strong rivaling system by a margin, while also confirming the importance of the contextual information. We further compiled, and we are making freely available, a new dataset of manually-annotated claims, extracted from the 2016 US presidential and vice-presidential debates, which we gathered from nine reputable sources including FactCheck, PolitiFact, CNN, NYT, WP, and NPR.
> 
> In future work, we plan to extend our dataset with additional debates, e.g., from other elections, but also with interviews and general discussions. We would also like to experiment with distant supervision, which would allow us to gather more training data, thus facilitating deep learning. We further plan to extend our system with finding claims at the sub-sentence level, as well as with automatic fact-checking of the identified claims.

#### Relevance 1090

Label: 1
> Reason
> - Summary of question: Does the baseline use contextual information?
> - Summary of passage: Previous work considers sentences in isolation, unlike the contextual proposed approach.
> - Judgement: It supplies a direct prior-work contrast supporting the baseline's lack of context.
> 原因
> - 问题概述：基线是否使用上下文信息？
> - Passage 概述：既有工作孤立处理句子，而本文方法考虑上下文。
> - 判断：它通过既有工作对比，支持基线不考虑上下文的判断。

#### Passage 1091

Retrieved by: Hybrid RRF followed by BGE reranking

> (1+4 S+C features): Many claims selected for fact-checking contain contradictions to what has been said earlier, as in the example below (from the 3rd presidential debate):
> 
> We model this by counting the negations in the target sentence as found in a dictionary of negation cues such as not, didn't, and never. We further model the context as the number of such cues in the two neighboring sentences from the same segment and the two neighboring segments.
> 
> Similarity to known positive/negative examples (kNN) (2+1 S+C features): We used three more features inspired by $k$-nearest neighbor (kNN) classification. The first one (sentence-level) uses the maximum over the training sentences of the number of matching words between the testing and the training sentence, which is further multiplied by $-1$ if the latter was not check-worthy. We also used another version of the feature, where we multiplied it by 0 if the speakers were different (contextual). A third version took as a training set all claims checked by PolitiFact (excluding the target sentence).

#### Relevance 1091

Label: 1
> Reason
> - Summary of question: Does the baseline use contextual information?
> - Summary of passage: The proposed features count contextual negations and compare nearby examples.
> - Judgement: The sentence-level versus contextual feature variants help reconstruct the context comparison with baselines.
> 原因
> - 问题概述：基线是否使用上下文信息？
> - Passage 概述：所提特征统计上下文否定词，并比较相关示例。
> - 判断：句内和上下文特征变体有助于还原与基线的上下文比较。

## Question 0120

Paper: Why We Need New Evaluation Metrics for NLG

> What NLG tasks were considered?

### Common Retrieved Chunks

#### Passage 1092

Retrieved by: BM25, Hybrid RRF

> To collect human rankings, we presented the MR together with 2 utterances generated by different systems side-by-side to crowdworkers, which were asked to score each utterance on a 6-point Likert scale for:
> 
> $\bullet $ Informativeness: Does the utterance provide all the useful information from the meaning representation?
> 
> $\bullet $ Naturalness: Could the utterance have been produced by a native speaker?
> 
> $\bullet $ Quality: How do you judge the overall quality of the utterance in terms of its grammatical correctness and fluency? Each system output (see Table 1 ) was scored by 3 different crowdworkers. To reduce participants' bias, the order of appearance of utterances produced by each system was randomised and crowdworkers were restricted to evaluate a maximum of 20 utterances. The crowdworkers were selected from English-speaking countries only, based on their IP addresses, and asked to confirm that English was their native language.
> 
> To assess the reliability of ratings, we calculated the intra-class correlation coefficient (ICC), which measures inter-observer reliability on ordinal data for more than two raters BIBREF30 . The overall ICC across all three datasets is 0.45 ( $p<0.001$ ), which corresponds to a moderate agreement. In general, we find consistent differences in inter-annotator agreement per system and dataset, with lower agreements for lols than for rnnlg and TGen. Agreement is highest for the SFHotel dataset, followed by SFRest and Bagel (details provided in supplementary material).

#### Relevance 1092

Label: 1
> Reason
> - Summary of question: Which NLG tasks are considered?
> - Summary of passage: Generated dialogue utterances are judged against meaning representations on three datasets.
> - Judgement: It provides partial evidence of meaning-representation-to-utterance generation in dialogue domains.
> 原因
> - 问题概述：研究考虑哪些自然语言生成任务？
> - Passage 概述：对三个数据集中的对话生成话语，参照语义表示进行评价。
> - 判断：它提供对话领域中从语义表示生成话语的部分证据。

#### Passage 1093

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Word-based metrics make two strong assumptions: They treat human-generated references as a gold standard, which is correct and complete. We argue that these assumptions are invalid for corpus-based NLG, especially when using crowdsourced datasets. Grammar-based metrics, on the other hand, do not rely on human-generated references and are not influenced by their quality. However, these metrics can be easily manipulated with grammatically correct and easily readable output that is unrelated to the input. We have experimented with combining WBMs and GBMs using ensemble-based learning. However, while our model achieved high correlation with humans within a single domain, its cross-domain performance is insufficient.
> 
> Our paper clearly demonstrates the need for more advanced metrics, as used in related fields, including: assessing output quality within the dialogue context, e.g. BIBREF40 ; extrinsic evaluation metrics, such as NLG's contribution to task success, e.g. BIBREF41 , BIBREF42 , BIBREF43 ; building discriminative models, e.g. BIBREF34 , BIBREF36 ; or reference-less quality prediction as used in MT, e.g. BIBREF33 . We see our paper as a first step towards reference-less evaluation for NLG by introducing grammar-based metrics. In current work BIBREF44 , we investigate a reference-less quality estimation approach based on recurrent neural networks, which predicts a quality score for a NLG system output by comparing it to the source meaning representation only.
> 
> Finally, note that the datasets considered in this study are fairly small (between 404 and 2.3k human references per domain). To remedy this, systems train on de-lexicalised versions BIBREF10 , which bears the danger of ungrammatical lexicalisation BIBREF13 and a possible overlap between testing and training set BIBREF15 . There are ongoing efforts to release larger and more diverse data sets, e.g. BIBREF16 , BIBREF45 .

#### Relevance 1093

Label: 1
> Reason
> - Summary of question: Which NLG tasks are considered?
> - Summary of passage: The discussion critiques metrics and proposes future reference-free evaluation.
> - Judgement: Corpus-based generation and dataset limitations provide context for the NLG setting whose tasks are being identified.
> 原因
> - 问题概述：研究考虑哪些自然语言生成任务？
> - Passage 概述：讨论批评现有指标，并提出未来无参考评估。
> - 判断：基于语料的生成和数据集局限为识别所问 NLG 任务提供场景背景。

#### Passage 1094

Retrieved by: BM25, Hybrid RRF

> Table 6 summarises results published by previous studies in related fields which investigate the relation between human scores and automatic metrics. These studies mainly considered WBMs, while we are the first study to consider GBMs. Some studies ask users to provide separate ratings for surface realisation (e.g. asking about `clarity' or `fluency'), whereas other studies focus only on sentence planning (e.g. `accuracy', `adequacy', or `correctness'). In general, correlations reported by previous work range from weak to strong. The results confirm that metrics can be reliable indicators at system-level BIBREF4 , while they perform less reliably at sentence-level BIBREF2 . Also, the results show that the metrics capture realization better than sentence planning. There is a general trend showing that best-performing metrics tend to be the more complex ones, combining word-overlap, semantic similarity and term frequency weighting. Note, however, that the majority of previous works do not report whether any of the metric correlations are significantly different from each other.

#### Relevance 1094

Label: 1
> Reason
> - Summary of question: Which NLG tasks are considered?
> - Summary of passage: Previous evaluation studies separately assess surface realization and sentence planning.
> - Judgement: Sentence planning and surface realization identify NLG subtask categories relevant to interpreting the study, while the cited results concern earlier work.
> 原因
> - 问题概述：研究考虑哪些自然语言生成任务？
> - Passage 概述：既有评估研究分别考察表层实现和句子规划。
> - 判断：句子规划和表层实现指出理解本文所需的 NLG 子任务类别，但所引结果来自此前研究。

#### Passage 1096

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Automatic evaluation measures, such as bleu BIBREF0 , are used with increasing frequency to evaluate Natural Language Generation (NLG) systems: Up to 60% of NLG research published between 2012–2015 relies on automatic metrics BIBREF1 . Automatic evaluation is popular because it is cheaper and faster to run than human evaluation, and it is needed for automatic benchmarking and tuning of algorithms. The use of such metrics is, however, only sensible if they are known to be sufficiently correlated with human preferences. This is rarely the case, as shown by various studies in NLG ( BIBREF2 ; BIBREF3 , BIBREF4 ), as well as in related fields, such as dialogue systems BIBREF5 , machine translation (MT) BIBREF6 , and image captioning BIBREF7 , BIBREF8 . This paper follows on from the above previous work and presents another evaluation study into automatic metrics with the aim to firmly establish the need for new metrics. We consider this paper to be the most complete study to date, across metrics, systems, datasets and domains, focusing on recent advances in data-driven NLG. In contrast to previous work, we are the first to:
> 
> $\bullet $ Target end-to-end data-driven NLG, where we compare 3 different approaches. In contrast to NLG methods evaluated in previous work, our systems can produce ungrammatical output by (a) generating word-by-word, and (b) learning from noisy data.
> 
> $\bullet $ Compare a large number of 21 automated metrics, including novel grammar-based ones.
> 
> $\bullet $ Report results on two different domains and three different datasets, which allows us to draw more general conclusions.
> 
> $\bullet $ Conduct a detailed error analysis, which suggests that, while metrics can be reasonable indicators at the system-level, they are not reliable at the sentence-level.
> 
> $\bullet $ Make all associated code and data publicly available, including detailed analysis results.

#### Relevance 1096

Label: 1
> Reason
> - Summary of question: Which NLG tasks are considered?
> - Summary of passage: The study targets end-to-end data-driven NLG across two domains and three datasets.
> - Judgement: It explicitly identifies the broad generation task evaluated.
> 原因
> - 问题概述：研究考虑哪些自然语言生成任务？
> - Passage 概述：研究针对端到端数据驱动自然语言生成，覆盖两个领域和三个数据集。
> - 判断：它明确指出评估的总体生成任务。

#### Passage 1097

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this paper, we focus on recent end-to-end, data-driven NLG methods, which jointly learn sentence planning and surface realisation from non-aligned data ( BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 ; BIBREF13 , BIBREF13 ; BIBREF14 , BIBREF15 ). These approaches do not require costly semantic alignment between Meaning Representations (MR) and human references (also referred to as “ground truth" or “targets"), but are based on parallel datasets, which can be collected in sufficient quality and quantity using effective crowdsourcing techniques, e.g. BIBREF16 , and as such, enable rapid development of NLG components in new domains. In particular, we compare the performance of the following systems:
> 
> $\bullet $ rnnlg: The system by BIBREF10 uses a Long Short-term Memory (LSTM) network to jointly address sentence planning and surface realisation. It augments each LSTM cell with a gate that conditions it on the input MR, which allows it to keep track of MR contents generated so far.
> 
> $\bullet $ TGen: The system by BIBREF9 learns to incrementally generate deep-syntax dependency trees of candidate sentence plans (i.e. which MR elements to mention and the overall sentence structure). Surface realisation is performed using a separate, domain-independent rule-based module.
> 
> $\bullet $ lols: The system by BIBREF15 learns sentence planning and surface realisation using Locally Optimal Learning to Search (lols), an imitation learning framework which learns using bleu and rouge as non-decomposable loss functions.

#### Relevance 1097

Label: 1
> Reason
> - Summary of question: Which NLG tasks are considered?
> - Summary of passage: Three systems jointly learn sentence planning and surface realization from meaning representations.
> - Judgement: It directly describes the NLG subtasks and the evaluated systems.
> 原因
> - 问题概述：研究考虑哪些自然语言生成任务？
> - Passage 概述：三个系统从语义表示联合学习句子规划和表层实现。
> - 判断：它直接描述自然语言生成子任务及评估系统。

#### Passage 1099

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> Grammar-based measures have been explored in related fields, such as MT BIBREF25 or grammatical error correction BIBREF26 , and, in contrast to WBMs, do not rely on ground-truth references. To our knowledge, we are the first to consider GBMs for sentence-level NLG evaluation. We focus on two important properties of texts here – readability and grammaticality:
> 
> $\bullet $ Readability quantifies the difficulty with which a reader understands a text, as used for e.g. evaluating summarisation BIBREF27 or text simplification BIBREF28 . We measure readability by the Flesch Reading Ease score (re) BIBREF29 , which calculates a ratio between the number of characters per sentence, the number of words per sentence, and the number of syllables per word. Higher re score indicates a less complex utterance that is easier to read and understand. We also consider related measures, such as characters per utterance (len) and per word (cpw), words per sentence (wps), syllables per sentence (sps) and per word (spw), as well as polysyllabic words per utterance (pol) and per word (ppw). The higher these scores, the more complex the utterance.
> 
> $\bullet $ Grammaticality: In contrast to previous NLG methods, our corpus-based end-to-end systems can produce ungrammatical output by (a) generating word-by-word, and (b) learning from noisy data. As a first approximation of grammaticality, we measure the number of misspellings (msp) and the parsing score as returned by the Stanford parser (prs). The lower the msp, the more grammatically correct an utterance is. The Stanford parser score is not designed to measure grammaticality, however, it will generally prefer a grammatical parse to a non-grammatical one. Thus, lower parser scores indicate less grammatically-correct utterances. In future work, we aim to use specifically designed grammar-scoring functions, e.g. BIBREF26 , once they become publicly available.

#### Relevance 1099

Label: 1
> Reason
> - Summary of question: Which NLG tasks are considered?
> - Summary of passage: Grammar-based evaluation measures readability and grammaticality.
> - Judgement: The description of word-by-word, corpus-trained end-to-end generation supplies partial information about the NLG setting.
> 原因
> - 问题概述：研究考虑哪些自然语言生成任务？
> - Passage 概述：基于语法的评估衡量可读性和语法正确性。
> - 判断：对逐词、语料训练的端到端生成的描述提供部分生成任务设置信息。

### BM25

#### Passage 1095

Retrieved by: BM25

> We consider the following crowdsourced datasets, which target utterance generation for spoken dialogue systems. Table 1 shows the number of system outputs for each dataset. Each data instance consists of one MR and one or more natural language references as produced by humans, such as the following example, taken from the Bagel dataset:
> 
> MR: inform(name=X, area=X, pricerange=moderate, type=restaurant)
> 
> Reference: “X is a moderately priced restaurant in X.”
> 
> $\bullet $ SFHotel & SFRest BIBREF10 provide information about hotels and restaurants in San Francisco. There are 8 system dialogue act types, such as inform, confirm, goodbye etc. Each domain contains 12 attributes, where some are common to both domains, such as name, type, pricerange, address, area, etc., and the others are domain-specific, e.g. food and kids-allowed for restaurants; hasinternet and dogs-allowed for hotels. For each domain, around 5K human references were collected with 2.3K unique human utterances for SFHotel and 1.6K for SFRest. The number of unique system outputs produced is 1181 for SFRest and 875 for SFHotel.
> 
> $\bullet $ Bagel BIBREF17 provides information about restaurants in Cambridge. The dataset contains 202 aligned pairs of MRs and 2 corresponding references each. The domain is a subset of SFRest, including only the inform act and 8 attributes.

#### Relevance 1095

Label: 1
> Reason
> - Summary of question: Which NLG tasks are considered?
> - Summary of passage: Spoken-dialogue utterance generation uses hotel and restaurant information datasets.
> - Judgement: It directly identifies the application task, domains and dialogue acts.
> 原因
> - 问题概述：研究考虑哪些自然语言生成任务？
> - Passage 概述：口语对话话语生成使用酒店和餐馆信息数据集。
> - 判断：它直接指出应用任务、领域及对话行为。

### Dense

#### Passage 1098

Retrieved by: Dense

> This paper shows that state-of-the-art automatic evaluation metrics for NLG systems do not sufficiently reflect human ratings, which stresses the need for human evaluations. This result is opposed to the current trend of relying on automatic evaluation identified in BIBREF1 .
> 
> A detailed error analysis suggests that automatic metrics are particularly weak in distinguishing outputs of medium and good quality, which can be partially attributed to the fact that human judgements and metrics are given on different scales. We also show that metric performance is data- and system-specific.
> 
> Nevertheless, our results also suggest that automatic metrics can be useful for error analysis by helping to find cases where the system is performing poorly. In addition, we find reliable results on system-level, which suggests that metrics can be useful for system development.

#### Relevance 1098

Label: 0
> Reason
> - Summary of question: Which NLG tasks are considered?
> - Summary of passage: Automatic metrics poorly reflect human ratings, especially at sentence level.
> - Judgement: Evaluation findings do not identify the generation tasks.
> 原因
> - 问题概述：研究考虑哪些自然语言生成任务？
> - Passage 概述：自动指标难以反映人工评价，句子层面尤为明显。
> - 判断：评估发现未说明生成任务。

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1100

Retrieved by: Hybrid RRF followed by BGE reranking

> NLG evaluation has borrowed a number of automatic metrics from related fields, such as MT, summarisation or image captioning, which compare output texts generated by systems to ground-truth references produced by humans. We refer to this group as word-based metrics. In general, the higher these scores are, the better or more similar to the human references the output is. The following order reflects the degree these metrics move from simple $n$ -gram overlap to also considering term frequency (TF-IDF) weighting and semantically similar words.
> 
> $\bullet $ Word-overlap Metrics (WOMs): We consider frequently used metrics, including ter BIBREF18 , bleu BIBREF0 , rouge BIBREF19 , nist BIBREF20 , lepor BIBREF21 , cider BIBREF22 , and meteor BIBREF23 .
> 
> $\bullet $ Semantic Similarity (sim): We calculate the Semantic Text Similarity measure designed by BIBREF24 . This measure is based on distributional similarity and Latent Semantic Analysis (LSA) and is further complemented with semantic relations extracted from WordNet.

#### Relevance 1100

Label: 0
> Reason
> - Summary of question: Which NLG tasks are considered?
> - Summary of passage: Word-based metrics compare generated text with human references.
> - Judgement: MT, summarization and captioning are metric-source fields, not the tasks evaluated here.
> 原因
> - 问题概述：研究考虑哪些自然语言生成任务？
> - Passage 概述：基于词的指标将生成文本与人工参考比较。
> - 判断：翻译、摘要和图像描述是指标借鉴领域，并非本文评估任务。
