# Passage relevance annotation

Annotator: 

Enter your name or agreed identifier after `Annotator:`.

Judge whether each passage helps answer the question, including useful partial evidence. Topic overlap alone is insufficient.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Preserve all content and record numbers. Work independently; do not exchange labels before submission. Algorithm sources are disclosed.

## Question 0081

Paper: DuTongChuan: Context-aware Translation Model for Simultaneous Interpreting

> Do they compare against a system that does not use streaming text, but has the entire text at disposal?

### Common Retrieved Chunks

#### Passage 741

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this paper, we propose DuTongChuan, a novel context-aware translation model for simultaneous interpreting. This model is able to constantly read streaming text from the ASR model, and simultaneously determine the boundaries of information units one after another. The detected IU is then translated into a fluent translation with two simple yet effective decoding strategies: partial decoding and context-aware decoding. We also release a novel speech translation corpus, BSTC, to boost the research on robust speech translation task.
> 
> With elaborate comparison, our model obtains superior translation quality against the wait-k model, but also presents competitive performance in latency. Assessment from human translators reveals that our system achieves promising translation quality (85.71% for Chinese-English, and 86.36% for English-Chinese), specially in the sense of surprisingly good discourse coherence. Our system also presents superior performance in latency (delayed in less 3 seconds at most times) in a speech-to-speech simultaneous translation. We also deploy our simultaneous machine translation model in our AI platform, and welcome the other users to enjoy it.
> 
> In the future, we will conduct research on novel method to evaluate the interpreting.

#### Relevance 741

Label: 

#### Passage 742

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> criteria are designed for evaluating written translation and have a special emphasis on adequacy and faithfulness. But in simultaneous interpreting, human interpreters routinely omit less-important information to overcome their limitations in working memory. As the last column in Table 6 shows, human interpreters' oral translations have more omissions than machine's and receive lower acceptability. The evaluation results do not mean that machines have exceeded human interpreters in simultaneous interpreting. Instead, it means we need machine translation criteria that suit simultaneous interpreting. We also find that the BSTC dataset is extremely difficult as the best human interpreter obtains a lower Acceptability 73.04%. Although the NMT model obtains impressive translation quality, we do not compare the latency of machine translation and human interpreting in this paper, and leave it to the future work.
> 
> To better understand the contribution of our model on generating coherent translation, we select one representative running example for analysis. As the red text in Figure FIGREF73 demonstrates that machine translation model generates coherent translation “its own grid” for the sub-sentence “这个网络”, and “corresponds actually to” for the subsequence “...对应的,就是每个...”. Compared to the human interpretation, our model presents comparable translation quality. In details, our model treats segments as IUs, and generates translation for each IU consecutively. While the human interpreter splits the entire source text into two sub-sentences, and produces the translation respectively.
> 
> In the final deployment, we train DuTongChuan on the large-scale training corpus. We also utilize techniques to enhance the robustness of the translation model, such as normalization of the speech irregularities, dealing with abnormal ASR errors, and content censorship, etc (see Appendix). We successfully deploy DuTongChuan in the Baidu Create 2019 (Baidu AI Developer Conference) .
> 
> As shown in Table TABREF74 , it is clear that DuTongChuan achieves promising acceptability on both translation tasks (85.71% for Chinese-English, and 86.36 % for English-Chinese). We also elaborately analyze the error types in the final translations, and we find that apart from errors occurring in translation and ASR, a majority of errors come from IU boundary detection, which account for nearly a half of errors. In the future, we should concentrate on improving the translation quality by enhancing the robustness of our IU boundary

#### Relevance 742

Label: 

#### Passage 743

Retrieved by: BM25, Dense, Hybrid RRF

> We firstly conduct our experiments on the NIST Chinese-English translation task.
> 
> To validate the effectiveness of our translation model, we run two baseline models, baseline and sub-sentence. We also compare the translation quality as well as latency of our models with the wait-k model.
> 
> Effectiveness on Translation Quality. As shown in Table TABREF49 , there is a great deal of difference between the sub-sentence and the baseline model. On an average the sub-sentence shows weaker performance by a 3.08 drop in BLEU score (40.39 INLINEFORM0 37.31). Similarly, the wait-k model also brings an obvious decrease in translation quality, even with the best wait-15 policy, its performance is still worse than the baseline system, with a 2.15 drop, averagely, in BLEU (40.39 INLINEFORM1 38.24). For a machine translation product, a large degradation in translation quality will largely affect the use experience even if it has low latency.
> 
> Unsurprisingly, when treating sub-sentences as IUs, our proposed model significantly improves the translation quality by an average of 2.35 increase in BLEU score (37.31 INLINEFORM0 39.66), and its performance is slightly lower than the baseline system with a 0.73 lower average BLEU score (40.39 INLINEFORM1 39.66). Moreover, as we allow the model to discard a few previously generated tokens, the performance can be further improved to 39.82 ( INLINEFORM2 0.16), at a small cost of longer latency (see Figure FIGREF58 ). It is consistent with our intuition that our novel partial decoding strategy can bring stable improvement on each testing dataset. It achieves an average improvement of 0.44 BLEU score (39.22 INLINEFORM3 39.66) compared to the context-aware system in which we do not fine-tune the trained model when using partial decoding strategy. An interesting finding is that our translation model performs better than the baseline system on the NIST08 testing set. We analyze the translation results and find that the sentences in NIST08 are extremely long, which affect the standard Transformer to learn better representation BIBREF23 . Using context-aware decoding strategy to generate consistent and coherent translation, our model performs better by focusing on generating translation for relatively shorter sub-sentences.
> 
> Investigation on Decoding Based on Segment. Intuitively, treating one segment as an IU will reduce the latency in waiting

#### Relevance 743

Label: 

#### Passage 744

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> the preceding sub-sentence.
> 
> To make the simultaneous machine translation more accessible and producible, we borrow SI strategies used by human interpreters to create our model. As shown in Figure FIGREF3 , this model is able to constantly read streaming text from the ASR model, and simultaneously determine the boundaries of Information Units (IUs) one after another. Each detected IU is then translated into a fluent translation with two simple yet effective decoding strategies: partial decoding and context-aware decoding. Specifically, IUs at the beginning of each sentence are sent to the partial decoding module. Other information units, either appearing in the middle or at the end of a sentence, are translated into target language by the context-aware decoding module. Notice that this module is able to exploit additional context from the history so that the model can generate coherent translation. This method is derived from the “salami technique” BIBREF13 , BIBREF14 , or “chunking”, one of the most commonly used strategies by human interpreters to cope with the linearity constraint in simultaneous interpreting. Having severely limited access to source speech structure in SI, interpreters tend to slice up the incoming speech into smaller meaningful pieces that can be directly rendered or locally reformulated without having to wait for the entire sentence to unfold.
> 
> In general, there are several remarkable novel advantages that differ our model from the previous work:
> 
> For a comprehensive evaluation of our system, we use two evaluation metrics: translation quality and latency. According to the automatic evaluation metric, our system presents excellent performance both in translation quality and latency. In the speech-to-speech scenario, our model achieves an acceptability of 85.71% for Chinese-English translation, and 86.36% for English-Chinese translation in human evaluation. Moreover, the output speech lags behind the source speech by an average of less than 3 seconds, which presents surprisingly good experience for machine translation users BIBREF15 , BIBREF16 , BIBREF17 . We also ask three interpreters with SI experience to simultaneously interpret the test speech in a mock conference setting. However, the target texts transcribed from human SI obtain worse BLEU scores as the reference in the test set are actually from written translating rather than simultaneous interpreting. More importantly, when

#### Relevance 744

Label: 

#### Passage 745

Retrieved by: Dense, Hybrid RRF

> of all models.
> 
> In all settings, the best system in context-aware model beats the wait-15 model.
> 
> Pre-trained models are not sensitive to errors from Auto IU, while fine-tuned models are.
> 
> Another interesting work is to compare machine translation with human interpretation. We request three simultaneous interpreters (S, A and B) with years of interpreting experience ranging from three to seven years, to interpret the talks in BSTC testing dataset, in a mock conference setting .
> 
> We concatenate the translation of each talk into one big sentence, and then evaluate it by BLEU score. From Table TABREF69 , we find that machine translation beats the human interpreters significantly. Moreover, the length of interpretations are relatively short, and results in a high length penalty provided by the evaluation script. The result is unsurprising, because human interpreters often deliberately skip non-primary information to keep a reasonable ear-voice span, which may bring a loss of adequacy and yet a shorter lag time, whereas the machine translation model translates the content adequately. We also use human interpreting results as references. As Table TABREF69 indicates, our model achieves a higher BLEU score, 28.08.
> 
> Furthermore, we ask human translators to evaluate the quality between interpreting and machine translation. To evaluate the performance of our final system, we select one Chinese talk as well as one English talk consisting of about 110 sentences, and have human translators to assess the translation from multiple aspects: adequacy, fluency and correctness. The detailed measurements are:
> 
> Bad: Typically, the mark Bad indicates that the translation is incorrect and unacceptable.
> 
> OK: If a translation is comprehensible and adequate, but with minor errors such as incorrect function words and less fluent phrases, then it will be marked as OK.
> 
> Good: A translation will be marked as Good if it contains no obvious errors.
> 
> As shown in Table TABREF70 , the performance of our model is comparable to the interpreting. It is worth mentioning that both automatic and human evaluation criteria are designed for evaluating written translation and have a special emphasis on adequacy and faithfulness. But in simultaneous interpreting, human interpreters routinely omit less-important information to overcome their limitations in working memory. As the last column in Table 6

#### Relevance 745

Label: 

### BM25

#### Passage 740

Retrieved by: BM25

> Recent progress in Automatic Speech Recognition (ASR) and Neural Machine Translation (NMT), has facilitated the research on automatic speech translation with applications to live and streaming scenarios such as Simultaneous Interpreting (SI). In contrast to non-real time speech translation, simultaneous interpreting involves starting translating source speech, before the speaker finishes speaking (translating the on-going speech while listening to it). Because of this distinguishing feature, simultaneous interpreting is widely used by multilateral organizations (UN/EU), international summits (APEC/G-20), legal proceedings, and press conferences. Despite of recent advance BIBREF0 , BIBREF1 , the research on simultaneous interpreting is notoriously difficult BIBREF0 due to well known challenging requirements: high-quality translation and low latency.
> 
> Many studies present methods to improve the translation quality by enhancing the robustness of translation model against ASR errors BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 , BIBREF6 , BIBREF7 . On the other hand, to reduce latency, some researchers propose models that start translating after reading a few source tokens BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 , BIBREF1 . As one representative work related to this topic, recently, we present a translation model using prefix-to-prefix framework with INLINEFORM0 policy BIBREF0 . This model is simple yet effective in practice, achieving impressive performance both on translation quality and latency.
> 
> However, existing work pays less attention to the fluency of translation, which is extremely important in the context of simultaneous translation. For example, we have a sub-sentence NMT model that starts to translate after reading a sub-sentence rather than waiting until the end of a sentence like the full-sentence models does. This will definitely reduce the time waiting for the source language speech. However, as shown in the Figure FIGREF2 , the translation for each sub-sentence is barely adequate, whereas the translation of the entire source sentence lacks coherence and fluency. Moreover, it is clear that the model produces an inappropriate translation “your own” for the source token “自己” due to the absence of the preceding sub-sentence.
> 
> To make the simultaneous machine translation more accessible and producible, we borrow SI strategies used by human interpreters to create our model. As shown in Figure FIGREF3 , this model is able to constantly read streaming text

#### Relevance 740

Label: 

### Dense

#### Passage 746

Retrieved by: Dense

> To preprocess the Chinese and the English texts, we use an open source Chinese Segmenter and Moses Tokenizer . After tokenization, we convert all English letters into lower case. And we use the “multi-bleu.pl” script to calculate BLEU scores. Except in the large-scale experiments, we conduct byte-pair encoding (BPE) BIBREF22 for both Chinese and English by setting the vocabulary size to 20K and 18K for Chinese and English, respectively. But in the large-scale experiments, we utilize a joint vocabulary for both Chinese-English and English-Chinese translation tasks, with a vocabulary size of 40K.

#### Relevance 746

Label: 

#### Passage 747

Retrieved by: Dense

> interpret the test speech in a mock conference setting. However, the target texts transcribed from human SI obtain worse BLEU scores as the reference in the test set are actually from written translating rather than simultaneous interpreting. More importantly, when evaluated by human translators, the performance of NMT model is comparable to the professional human interpreter.
> 
> The contributions of this paper can be concluded into the following aspects:

#### Relevance 747

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 748

Retrieved by: Hybrid RRF followed by BGE reranking

> We use a subset of the data available for NIST OpenMT08 task . The parallel training corpus contains approximate 2 million sentence pairs. We choose NIST 2006 (NIST06) dataset as our development set, and the NIST 2002 (NIST02), 2003 (NIST03), 2004 (NIST04) 2005 (NIST05), and 2008 (NIST08) datasets as our test sets. We will use this dataset to evaluate the performance of our partial decoding and context-aware decoding strategy from the perspective of translation quality and latency.
> 
> Recently, we release Baidu Speech Translation Corpus (BSTC) for open research . This dataset covers speeches in a wide range of domains, including IT, economy, culture, biology, arts, etc. We transcribe the talks carefully, and have professional translators to produce the English translations. This procedure is extremely difficult due to the large number of domain-specific terminologies, speech redundancies and speakers' accents. We expect that this dataset will help the researchers to develop robust NMT models on the speech translation. In summary, there are many features that distinguish this dataset to the previously related resources:
> 
> Speech irregularities are kept in transcription while omitted in translation (eg. filler words like “嗯, 呃, 啊”, and unconscious repetitions like “这个这个呢”), which can be used to evaluate the robustness of the NMT model dealing with spoken language.
> 
> Each talk's transcription is translated into English by a single translator, and then segmented into bilingual sentence pairs according to the sentence boundaries in the English translations. Therefore, every sentence is translated based on the understanding of the entire talk and is translated faithfully and coherently in global sense.
> 
> We use the streaming multi-layer truncated attention model (SMLTA) trained on the large-scale speech corpus (more than 10,000 hours) and fine-tuned on a number of talk related corpora (more than 1,000 hours), to generate the 5-best automatic recognized text for each acoustic speech.
> 
> The test dataset includes interpretations produced by simultaneous interpreters with professional experience. This dataset contributes an essential resource for the comparison between translation and interpretation.
> 
> We randomly extract several talks from the dataset, and divide them into the development and test set. In Table TABREF34 , we summarize the statistics of our dataset. The average number of utterances per talk is 152.6 in the

#### Relevance 748

Label: 

#### Passage 749

Retrieved by: Hybrid RRF followed by BGE reranking

> human simultaneous interpreters.
> 
> For better generation of coherent translations, gong2011cache propose a memory based approach to capture contextual information to make the statistical translation model generate discourse coherent translations. kuang2017cache,tu2018learning,P18-1118 extend similar memory based approach to the NMT framework. wang2017exploiting present a novel document RNN to learn the representation of the entire text, and treated the external context as the auxiliary context which will be retrieved by the hidden state in the decoder. tiedemann2017neural and P18-1117 propose to encode global context through extending the current sentence with one preceding adjacent sentence. Notably, the former is conducted on the recurrent based models while the latter is implemented on the Transformer model. Recently, we also propose a reinforcement learning strategy to deliberate the translation so that the model can generate more coherent translations BIBREF43 .

#### Relevance 749

Label: 

## Question 0082

Paper: Adversarial NLI: A New Benchmark for Natural Language Understanding

> What are the weaknesses found by non-expert annotators of current state-of-the-art NLI models?

### Common Retrieved Chunks

#### Passage 750

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this work, we used a human-and-model-in-the-loop entailment training method to collect a new benchmark for natural language understanding. The benchmark is designed to be challenging to current state of the art models. Annotators were employed to act as adversaries, and encouraged to find vulnerabilities that fool the model into predicting the wrong label, but that another person would correctly classify. We found that non-expert annotators, in this gamified setting and with appropriate incentives to fool the model, are remarkably creative at finding and exploiting weaknesses in models. We collected three rounds, and as the rounds progressed, the models became more robust and the test sets for each round became more difficult. Training on this new data yielded the state of the art on existing NLI benchmarks.
> 
> The ANLI benchmark presents a new challenge to the community. It was carefully constructed to mitigate issues with previous datasets, and was designed from first principles to last longer—if the test set saturates, the field can simply train up a new model, collect more data and find itself confronted yet again with a difficult challenge.
> 
> The dataset also presents many opportunities for further study. For instance, we collected annotator-provided explanations for each example that the model got wrong. We provided inference labels for the development set, opening up possibilities for interesting more fine-grained studies of NLI model performance. While we verified the development and test examples, we did not verify the correctness of each training example, which means there is probably some room for improvement there.
> 
> The benchmark is meant to be a challenge for measuring NLU progress, even for as yet undiscovered models and architectures. We plan for the benchmark itself to adapt to these new models by continuing to build new challenge rounds. As a first next step, it would be interesting to examine results when annotators are confronted with a wide variety of model architectures. We hope that the dataset will prove to be an interesting new challenge for the community. Luckily, if it does turn out to saturate quickly, we will always be able to collect a new round.

#### Relevance 750

Label: 

#### Passage 751

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Progress in AI has been driven by, among other things, the development of challenging large-scale benchmarks like ImageNet BIBREF0 in computer vision, and SNLI BIBREF1, SQuAD BIBREF2, and others in natural language processing (NLP). Recently, for natural language understanding (NLU) in particular, the focus has shifted to combined benchmarks like SentEval BIBREF3 and GLUE BIBREF4, which track model performance on multiple tasks and provide a unified platform for analysis.
> 
> With the rapid pace of advancement in AI, however, NLU benchmarks struggle to keep up with model improvement. Whereas it took around 15 years to achieve “near-human performance” on MNIST BIBREF5, BIBREF6, BIBREF7 and approximately 7 years to surpass humans on ImageNet BIBREF8, BIBREF0, BIBREF9, the GLUE benchmark did not last as long as we would have hoped after the advent of BERT BIBREF10, and rapidly had to be extended into SuperGLUE BIBREF11. This raises an important question: Can we collect a large benchmark dataset that can last longer?
> 
> The speed with which benchmarks become obsolete raises another important question: are current NLU models genuinely as good as their high performance on benchmarks suggests? A growing body of evidence shows that state-of-the-art models learn to exploit spurious statistical patterns in datasets BIBREF12, BIBREF13, BIBREF14, BIBREF15, BIBREF16, BIBREF17, instead of learning meaning in the flexible and generalizable way that humans do. Given this, human annotators—be they seasoned NLP researchers or non-experts—might easily be able to construct examples that expose model brittleness.
> 
> We propose an iterative, adversarial human-and-model-in-the-loop solution for NLU dataset collection that addresses both benchmark longevity and robustness issues. In the first stage, human annotators devise examples that our current best models cannot determine the correct label for. These resulting hard examples—which should expose additional model weaknesses—can be added to the training set and used to train a stronger model. We then subject the strengthened model to human interference and collect more weaknesses over several rounds. After each round, we both train a new model, and set aside a new test set. The process can be iteratively repeated in a never-ending learning BIBREF18 setting, with the model getting stronger and the test set getting harder in each new round.This process yields a “moving post” dynamic target

#### Relevance 751

Label: 

#### Passage 752

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> set aside a new test set. The process can be iteratively repeated in a never-ending learning BIBREF18 setting, with the model getting stronger and the test set getting harder in each new round.This process yields a “moving post” dynamic target for NLU systems, rather than a static benchmark that will eventually saturate.
> 
> Our approach draws inspiration from recent efforts that gamify collaborative training of machine learning agents over multiple rounds BIBREF19 and pit “builders” against “breakers” to learn better models BIBREF20. Recently, Dinan2019build showed that a similar approach can be used to make dialogue safety classifiers more robust. Here, we focus on natural language inference (NLI), arguably the most canonical task in NLU. We collected three rounds of data, and call our new dataset Adversarial NLI (ANLI).
> 
> Our contributions are as follows: 1) We introduce a novel human-and-model-in-the-loop dataset, currently consisting of three rounds that progressively increase in difficulty and complexity, that includes annotator-provided explanations. 2) We show that training models on this new dataset leads to state-of-the-art performance on a variety of popular NLI benchmarks. 3) We provide a detailed analysis of the collected data that sheds light on the shortcomings of current models, categorizes the data by inference type to examine weaknesses, and demonstrates good performance on NLI stress tests. The ANLI dataset is available at github.com/facebookresearch/anli/. A demo of the annotation procedure can be viewed at adversarialnli.com.

#### Relevance 752

Label: 

#### Passage 755

Retrieved by: Dense, Hybrid RRF

> However, the base (RoBERTa) models for rounds 2 and 3 are outperformed by both BERT and XLNet. This shows that annotators have managed to write examples that RoBERTa generally struggles with, and more training data alone cannot easily mitigated these shortcomings. It also implies that BERT, XLNet, and RoBERTa all have different weaknesses, possibly as a function of their training data (BERT, XLNet and RoBERTa were trained on very different data sets, which might or might not have contained information relevant to the weaknesses)—an additional round with a wider model variety would thus be interesting to investigate as a next step.

#### Relevance 755

Label: 

#### Passage 757

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The primary aim of this work is to create a new large-scale NLI benchmark on which current state-of-the-art models fail. This constitutes a new target for the field to work towards, and can elucidate model capabilities and limitations. As noted, however, static benchmarks do not last very long these days. If continuously deployed, the data collection procedure we introduce here can pose a dynamic challenge that allows for never-ending learning.

#### Relevance 757

Label: 

### BM25

#### Passage 753

Retrieved by: BM25

> For the second round, we used a more powerful RoBERTa model BIBREF25 trained on SNLI, MNLI, an NLI-version of FEVER BIBREF26, and the training data from the previous round (A1). After a hyperparameter search, we selected the model with the best performance on the A1 development set. Then, using the hyperparameters selected from this search, we created a final set of models by training several models with different random seeds. During annotation, we constructed an ensemble by randomly picking a model from the model set as the adversary each turn. This helps us avoid annotators exploiting vulnerabilities in one single model. A new non-overlapping set of contexts was again constructed from Wikipedia via HotpotQA using the same method as Round 1.

#### Relevance 753

Label: 

#### Passage 754

Retrieved by: BM25

> A dynamically evolving dataset offers the unique opportunity to track how model error rates change over time. Since each round's development set contains only verified examples, we can investigate two interesting questions: which types of inference do writers employ to fool the models, and are base models differentially sensitive to different types of reasoning? The results are summarized in Table TABREF27.
> 
> We employed an expert linguist annotator to devise an ontology of inference types that would be specific to NLI. While designing an appropriate ontology of types of inference is far from straightforward, we found that a unified ontology could be utilized to characterize examples from all three rounds, which suggests that it has at least some generalizeable applicability. The ontology was used to label 500 examples from each ANLI development set.
> 
> The inference ontology contains six types of inference: Numerical & Quantitative (i.e., reasoning about cardinal and ordinal numbers, inferring dates and ages from numbers, etc.), Reference & Names (coreferences between pronouns and forms of proper names, knowing facts about name gender, etc.), Basic Inferences (conjunctions, negations, cause-and-effect, comparatives and superlatives etc.), Lexical Inference (inferences made possible by lexical information about synonyms, antonyms, etc.), Tricky Inferences (wordplay, linguistic strategies such as syntactic transformations/reorderings, or inferring writer intentions from contexts), and reasoning from outside knowledge or additional facts (e.g., “You can't reach the sea directly from Djibouti”). The quality of annotations was also tracked; if a pair was ambiguous or had a label that seemed incorrect (from the expert annotator's perspective), it was flagged. Round 1–3 development sets contained few `Quality' tags; the incidence of quality issues was stable at between 3% and 4% per round. Any one example can have multiple types, and every example contained at least one tag.
> 
> As rounds 1 and 2 were both built with contexts from the same genre (Wikipedia), we might expect writers to arrive at similar strategies. However, since the model architectures used in the first two rounds differ, writers might be sufficiently creative in finding different exploits in each. For round 3, we expect some difference in reasoning types to be present, because we used source material from several domains as our contexts. In sum, any

#### Relevance 754

Label: 

### Dense

#### Passage 756

Retrieved by: Dense

> The ANLI dataset improves upon previous work in several ways. First, and most obviously, the dataset is collected to be more difficult than previous datasets, by design. Second, it remedies a problem with SNLI, namely that its contexts (or premises) are very short, because they were selected from the image captioning domain. We believe longer contexts should naturally lead to harder examples, and so we constructed ANLI contexts from longer, multi-sentence source material.
> 
> Following previous observations that models might exploit spurious biases in NLI hypotheses, BIBREF12, BIBREF13, we conduct a study of the performance of hypothesis-only models on our dataset. We show that such models perform poorly on our test sets.
> 
> With respect to data generation with naïve annotators, Geva2019taskorannotator noted that models might pick up on annotator bias, modelling the annotators themselves rather than capturing the intended reasoning phenomenon. To counter this, we selected a subset of annotators (i.e., the “exclusive” workers) whose data would only be included in the test set. This enables us to avoid overfitting to the writing style biases of particular annotators, and also to determine how much individual annotator bias is present for the main portion of the data. Examples from each round of dataset collection are provided in Table TABREF2.
> 
> Furthermore, our dataset poses new challenges to the community that were less relevant for previous work, such as: can we improve performance online without having to train a new model from scratch every round, how can we overcome catastrophic forgetting, how do we deal with mixed model biases, etc. Because the training set includes examples that the model got right but were not verified, it might be noisy, posing filtering as an additional interesting problem.

#### Relevance 756

Label: 

#### Passage 758

Retrieved by: Dense

> To paraphrase the great bard BIBREF21, there is something rotten in the state of the art. We propose Human-And-Model-in-the-Loop Entailment Training (HAMLET), a training procedure to automatically mitigate problems with current dataset collection procedures (see Figure FIGREF1).
> 
> In our setup, our starting point is a base model, trained on NLI data. Rather than employing automated adversarial methods, here the model's “adversary” is a human annotator. Given a context (also often called a “premise” in NLI), and a desired target label, we ask the human writer to provide a hypothesis that fools the model into misclassifying the label. One can think of the writer as a “white hat” hacker, trying to identify vulnerabilities in the system. For each human-generated example that is misclassified, we also ask the writer to provide a reason why they believe it was misclassified.
> 
> For examples that the model misclassified, it is necessary to verify that they are actually correct —i.e., that the given context-hypothesis pairs genuinely have their specified target label. The best way to do this is to have them checked by another human. Hence, we provide the example to human verifiers. If two human verifiers agree with the writer, the example is considered a good example. If they disagree, we ask a third human verifier to break the tie. If there is still disagreement between the writer and the verifiers, the example is discarded. Occasionally, verifiers will overrule the original label of the writer.
> 
> Once data collection for the current round is finished, we construct a new training set from the collected data, with accompanying development and test sets. While the training set includes correctly classified examples, the development and tests sets are built solely from them. The test set was further restricted so as to: 1) include pairs from “exclusive” annotators that are never included in the training data; and 2) be balanced by label classes (and genres, where applicable). We subsequently train a new model on this and other existing data, and repeat the procedure three times.

#### Relevance 758

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 759

Retrieved by: Hybrid RRF followed by BGE reranking

> We perform two types of model error analysis. First we evaluate two popular existing test sets that were created to expose model weaknesses, and show that our dataset discourages models from learning spurious statistical facts, relative to other large popular datasets (e.g., SNLI and MNLI). Secondly, we explore, by round, the types of inferences our writers successfully employed to stump models, by performing hand-annotation on 500 examples from each round's development set.

#### Relevance 759

Label: 

## Question 0083

Paper: Question Answering for Privacy Policies: Combining Computational and Legal Perspectives

> Who were the experts used for annotation?

### Common Retrieved Chunks

#### Passage 760

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> When do experts disagree? We would like to analyze the reasons for potential disagreement on the annotation task, to ensure disagreements arise due to valid differences in opinion rather than lack of adequate specification in annotation guidelines. It is important to note that the annotators are experts rather than crowdworkers. Accordingly, their judgements can be considered valid, legally-informed opinions even when their perspectives differ. For the sake of this question we randomly sample 100 instances in the test data and analyze them for likely reasons for disagreements. We consider a disagreement to have occurred when more than one expert does not agree with the majority consensus. By disagreement we mean there is no overlap between the text identified as relevant by one expert and another.
> 
> We find that the annotators agree on the answer for 74% of the questions, even if the supporting evidence they identify is not identical i.e full overlap. They disagree on the remaining 26%. Sources of apparent disagreement correspond to situations when different experts: have differing interpretations of question intent (11%) (for example, when a user asks 'who can contact me through the app', the questions admits multiple interpretations, including seeking information about the features of the app, asking about first party collection/use of data or asking about third party collection/use of data), identify different sources of evidence for questions that ask if a practice is performed or not (4%), have differing interpretations of policy content (3%), identify a partial answer to a question in the privacy policy (2%) (for example, when the user asks `who is allowed to use the app' a majority of our annotators decline to answer, but the remaining annotators highlight partial evidence in the privacy policy which states that children under the age of 13 are not allowed to use the app), and other legitimate sources of disagreement (6%) which include personal subjective views of the annotators (for example, when the user asks `is my DNA information used in any way other than what is specified', some experts consider the boilerplate text of the privacy policy which states that it abides to practices described in the policy document as sufficient evidence to answer this question, whereas

#### Relevance 760

Label: 

#### Passage 762

Retrieved by: BM25, Dense, Hybrid RRF

> Disagreements are analyzed based on the OPP-115 categories of each question (Table.TABREF34). We compare our best performing BERT variant against the NA model and human performance. We observe significant room for improvement across all categories of questions but especially for first party, third party and data retention categories.
> 
> We analyze the performance of our strongest BERT variant, to identify classes of errors and directions for future improvement (Table.8). We observe that a majority of answerability mistakes made by the BERT model are questions which are in fact answerable, but are identified as unanswerable by BERT. We observe that BERT makes 124 such mistakes on the test set. We collect expert judgments on relevance, subjectivity , silence and information about how likely the question is to be answered from the privacy policy from our experts. We find that most of these mistakes are relevant questions. However many of them were identified as subjective by the annotators, and at least one annotator marked 19 of these questions as having no answer within the privacy policy. However, only 6 of these questions were unexpected or do not usually have an answer in privacy policies. These findings suggest that a more nuanced understanding of answerability might help improve model performance in his challenging domain.

#### Relevance 762

Label: 

#### Passage 763

Retrieved by: BM25, Dense, Hybrid RRF

> To identify legally sound answers, we recruit seven experts with legal training to construct answers to Turker questions. Experts identify relevant evidence within the privacy policy, as well as provide meta-annotation on the question's relevance, subjectivity, OPP-115 category BIBREF49, and how likely any privacy policy is to contain the answer to the question asked.

#### Relevance 763

Label: 

#### Passage 765

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Questions are organized under nine categories from the OPP-115 Corpus annotation scheme BIBREF49:
> 
> First Party Collection/Use: What, why and how information is collected by the service provider
> 
> Third Party Sharing/Collection: What, why and how information shared with or collected by third parties
> 
> Data Security: Protection measures for user information
> 
> Data Retention: How long user information will be stored
> 
> User Choice/Control: Control options available to users
> 
> User Access, Edit and Deletion: If/how users can access, edit or delete information
> 
> Policy Change: Informing users if policy information has been changed
> 
> International and Specific Audiences: Practices pertaining to a specific group of users
> 
> Other: General text, contact information or practices not covered by other categories.
> 
> For each question, domain experts indicate one or more relevant OPP-115 categories. We mark a category as relevant to a question if it is identified as such by at least two annotators. If no such category exists, the category is marked as `Other' if atleast one annotator has identified the `Other' category to be relevant. If neither of these conditions is satisfied, we label the question as having no agreement. The distribution of questions in the corpus across OPP-115 categories is as shown in Table.TABREF16. First party and third party related questions are the largest categories, forming nearly 66.4% of all questions asked to the privacy assistant.

#### Relevance 765

Label: 

#### Passage 767

Retrieved by: Hybrid RRF, Hybrid RRF followed by BGE reranking

> Table.TABREF17 presents aggregate statistics of the PrivacyQA dataset. 1750 questions are posed to our imaginary privacy assistant over 35 mobile applications and their associated privacy documents. As an initial step, we formulate the problem of answering user questions as an extractive sentence selection task, ignoring for now background knowledge, statistical data and legal expertise that could otherwise be brought to bear. The dataset is partitioned into a training set featuring 27 mobile applications and 1350 questions, and a test set consisting of 400 questions over 8 policy documents. This ensures that documents in training and test splits are mutually exclusive. Every question is answered by at least one expert. In addition, in order to estimate annotation reliability and provide for better evaluation, every question in the test set is answered by at least two additional experts.
> 
> Table TABREF14 describes the distribution over first words of questions posed by crowdworkers. We also observe low redundancy in the questions posed by crowdworkers over each policy, with each policy receiving ~49.94 unique questions despite crowdworkers independently posing questions. Questions are on average 8.4 words long. As declining to answer a question can be a legally sound response but is seldom practically useful, answers to questions where a minority of experts abstain to answer are filtered from the dataset. Privacy policies are ~3000 words long on average. The answers to the question asked by the users typically have ~100 words of evidence in the privacy policy document.

#### Relevance 767

Label: 

### BM25

#### Passage 761

Retrieved by: BM25

> We further ask legal experts to identify potential causes of unanswerability of questions. This analysis has considerable implications. While past work BIBREF17 has treated unanswerable questions as homogeneous, a question answering system might wish to have different treatments for different categories of `unanswerable' questions. The following factors were identified to play a role in unanswerability:
> 
> Incomprehensibility: If a question is incomprehensible to the extent that its meaning is not intelligible.
> 
> Relevance: Is this question in the scope of what could be answered by reading the privacy policy.
> 
> Ill-formedness: Is this question ambiguous or vague. An ambiguous statement will typically contain expressions that can refer to multiple potential explanations, whereas a vague statement carries a concept with an unclear or soft definition.
> 
> Silence: Other policies answer this type of question but this one does not.
> 
> Atypicality: The question is of a nature such that it is unlikely for any policy policy to have an answer to the question.
> 
> Our experts attempt to identify the different `unanswerable' factors for all 573 such questions in the corpus. 4.18% of the questions were identified as being incomprehensible (for example, `any difficulties to occupy the privacy assistant'). Amongst the comprehendable questions, 50% were identified as likely to have an answer within the privacy policy, 33.1% were identified as being privacy-related questions but not within the scope of a privacy policy (e.g., 'has Viber had any privacy breaches in the past?') and 16.9% of questions were identified as completely out-of-scope (e.g., `'will the app consume much space?'). In the questions identified as relevant, 32% were ill-formed questions that were phrased by the user in a manner considered vague or ambiguous. Of the questions that were both relevant as well as `well-formed', 95.7% of the questions were not answered by the policy in question but it was reasonable to expect that a privacy policy would contain an answer. The remaining 4.3% were described as reasonable questions, but of a nature generally not discussed in privacy policies. This suggests that the answerability of questions over privacy policies is a complex issue, and future systems should consider each of these factors when serving user's information seeking intent.
> 
> We examine a large-scale dataset of “natural”

#### Relevance 761

Label: 

#### Passage 764

Retrieved by: BM25

> We describe the data collection methodology used to construct PrivacyQA. With the goal of achieving broad coverage across application types, we collect privacy policies from 35 mobile applications representing a number of different categories in the Google Play Store. One of our goals is to include both policies from well-known applications, which are likely to have carefully-constructed privacy policies, and lesser-known applications with smaller install bases, whose policies might be considerably less sophisticated. Thus, setting 5 million installs as a threshold, we ensure each category includes applications with installs on both sides of this threshold. All policies included in the corpus are in English, and were collected before April 1, 2018, predating many companies' GDPR-focused BIBREF41 updates. We leave it to future studies BIBREF42 to look at the impact of the GDPR (e.g., to what extent GDPR requirements contribute to making it possible to provide users with more informative answers, and to what extent their disclosures continue to omit issues that matter to users).

#### Relevance 764

Label: 

### Dense

#### Passage 766

Retrieved by: Dense

> We describe baselines on this task, including a human performance baseline.
> 
> No-Answer Baseline (NA) : Most of the questions we receive are difficult to answer in a legally-sound way on the basis of information present in the privacy policy. We establish a simple baseline to quantify the effect of identifying every question as unanswerable.
> 
> Word Count Baseline : To quantify the effect of using simple lexical matching to answer the questions, we retrieve the top candidate policy sentences for each question using a word count baseline BIBREF53, which counts the number of question words that also appear in a sentence. We include the top 2, 3 and 5 candidates as baselines.
> 
> BERT: We implement two BERT-based baselines BIBREF51 for evidence identification. First, we train BERT on each query-policy sentence pair as a binary classification task to identify if the sentence is evidence for the question or not (Bert). We also experiment with a two-stage classifier, where we separately train the model on questions only to predict answerability. At inference time, if the answerable classifier predicts the question is answerable, the evidence identification classifier produces a set of candidate sentences (Bert + Unanswerable).
> 
> Human Performance: We pick each reference answer provided by an annotator, and compute the F1 with respect to the remaining references, as described in section 4.2.1. Each reference answer is treated as the prediction, and the remaining n-1 answers are treated as the gold reference. The average of the maximum F1 across all reference answers is computed as the human baseline.

#### Relevance 766

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 768

Retrieved by: Hybrid RRF followed by BGE reranking

> This research was supported in part by grants from the National Science Foundation Secure and Trustworthy Computing program (CNS-1330596, CNS-1330214, CNS-15-13957, CNS-1801316, CNS-1914486, CNS-1914444) and a DARPA Brandeis grant on Personalized Privacy Assistants (FA8750-15-2-0277). The US Government is authorized to reproduce and distribute reprints for Governmental purposes not withstanding any copyright notation. The views and conclusions contained herein are those of the authors and should not be interpreted as necessarily representing the official policies or endorsements, either expressed or implied, of the NSF, DARPA, or the US Government. The authors would like to extend their gratitude to Elias Wright, Gian Mascioli, Kiara Pillay, Harrison Kay, Eliel Talo, Alexander Fagella and N. Cameron Russell for providing their valuable expertise and insight to this effort. The authors are also grateful to Eduard Hovy, Lorrie Cranor, Florian Schaub, Joel Reidenberg, Aditya Potukuchi and Igor Shalyminov for helpful discussions related to this work, and to the three anonymous reviewers of this draft for their constructive feedback. Finally, the authors would like to thank all crowdworkers who consented to participate in this study.

#### Relevance 768

Label: 

#### Passage 769

Retrieved by: Hybrid RRF followed by BGE reranking

> discussed in privacy policies. This suggests that the answerability of questions over privacy policies is a complex issue, and future systems should consider each of these factors when serving user's information seeking intent.
> 
> We examine a large-scale dataset of “natural” unanswerable questions BIBREF54 based on real user search engine queries to identify if similar unanswerability factors exist. It is important to note that these questions have previously been filtered, according to a criteria for bad questions defined as “(questions that are) ambiguous, incomprehensible, dependent on clear false presuppositions, opinion-seeking, or not clearly a request for factual information.” Annotators made the decision based on the content of the question without viewing the equivalent Wikipedia page. We randomly sample 100 questions from the development set which were identified as unanswerable, and find that 20% of the questions are not questions (e.g., “all I want for christmas is you mariah carey tour”). 12% of questions are unlikely to ever contain an answer on Wikipedia, corresponding closely to our atypicality category. 3% of questions are unlikely to have an answer anywhere (e.g., `what guides Santa home after he has delivered presents?'). 7% of questions are incomplete or open-ended (e.g., `the south west wind blows across nigeria between'). 3% of questions have an unresolvable coreference (e.g., `how do i get to Warsaw Missouri from here'). 4% of questions are vague, and a further 7% have unknown sources of error. 2% still contain false presuppositions (e.g., `what is the only fruit that does not have seeds?') and the remaining 42% do not have an answer within the document. This reinforces our belief that though they have been understudied in past work, any question answering system interacting with real users should expect to receive such unanticipated and unanswerable questions.

#### Relevance 769

Label: 

## Question 0084

Paper: Transcribing Lyrics From Commercial Song Audio: The First Step Towards Singing Content Processing

> What was the baseline?

### Common Retrieved Chunks

#### Passage 770

Retrieved by: BM25, Hybrid RRF

> From the data, we found errors frequently occurred under some specific circumstances, such as high-pitched voice, widely varying phone duration, overlapping verses (multiple people sing simultaneously), and residual background music.
> 
> Figure FIGREF15 shows a sample recognition results obtained with Model E-4 as in row(7) of Table. TABREF14 , showing the error caused by high-pitched voice and overlapping verses. At first, the model successfully decoded the words, "what doesn't kill you makes", but afterward the pitch went high and a lower pitch harmony was added, the recognition results then went totally wrong.

#### Relevance 770

Label: 

#### Passage 771

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The primary recognition results are listed in Table. TABREF14 . Word error rate (WER) is taken as the major performance measure, while phone error rate (PER) is also listed as references. Rows (1)(2) on the top are for the language model trained with LibriSpeech data, while rows (3)-(16) for the language model trained with lyrics corpus. In addition, in rows (4)-(16) the lexicon was extended with possible repetition of vowels as explained in subsection UID8 . Rows (1)-(8) are for GMM-HMM only, while rows (9)-(16) with DNNs, BLSTMs and TDNN-LSTMs.
> 
> Row(1) is for Model A in Fig. FIGREF5 taken as the baseline, which was trained on LibriSpeech data with SAT, together with the language model also trained with LibriSpeech. The extremely high WER (96.21%) indicated the wide mismatch between speech and song audio, and the high difficulties in transcribing song audio. This is taken as the baseline of this work. After going through the series of Alignments a, b, c, d and training the series of Models B, C, D, we finally obtained the best GMM-HMM model, Model E-4 in Model E with fMLLR on the fragment level, as explained in section SECREF3 and shown in Fig. FIGREF5 . As shown in row(2) of Table. TABREF14 , with the same LibriSpeech LM, Model E-4 reduced WER to 88.26%, and brought an absolute improvement of 7.95% (rows (2) vs. (1)), which shows the achievements by the series of GMM-HMM alone. When we replaced the LibriSpeech language model with Lyrics language model but with the same Model E-4, we obtained an WER of 80.40% or an absolute improvement of 7.86% (rows (3) vs. (2)). This shows the achievement by the Lyrics language model alone.
> 
> We then substituted the normal lexicon with the extended one (with vowels repeated or not as described in subsection UID8 ), while using exactly the same model E-4, the WER of 77.08% in row (7) indicated the extended lexicon alone brought an absolute improvement of 3.32% (rows (7) vs. (3)). Furthermore, the increased self-looped transition probability ( INLINEFORM0 ) in subsection UID9 for vowel HMMs also brought an 0.46% improvement when applied on top of the extended lexicon (rows (8) vs. (7)). The

#### Relevance 771

Label: 

#### Passage 772

Retrieved by: BM25, Dense, Hybrid RRF

> Fig. FIGREF5 shows the overall structure based on Kaldi BIBREF22 for training the acoustic models used in this work. The right-most block is the vocal data, and the series of blocks on the left are the feature extraction processes over the vocal data. Features I, II, III, IV represent four different versions of features used here. For example, Feature IV was derived from splicing Feature III with 4 left-context and 4 right-context frames, and Feature III was obtained by performing fMLLR transformation over Feature II, while Feature I has been mean and variance normalized, etc.
> 
> The series of second right boxes are forced alignment processes performed over the various versions of features of the vocal data. The results are denoted as Alignment a, b, c, d, e. For example, Alignment a is the forced alignment results obtained by aligning Feature I of the vocal data with the LibriSpeech SAT triphone model (denoted as Model A at the top middle).
> 
> The series of blocks in the middle of Fig. FIGREF5 are the different versions of trained acoustic models. For example, model B is a monophone model trained with Feature I of the vocal data based on alignment a. Model C is very similar, except based on alignment b which is obtained with Model B, etc. Another four sets of Models E, F, G, H are below. For example Model E includes models E-1, 2, 3, 4, Models F,G and H include F-1,2 , G-1,2,3, and H-1,2,3.
> 
> We take Model E-4 with fragment-level adaptation within model E as the example. Here every fragment of song (10-35 sec long) was used to train a distinct fragment-level fMLLR matrix, with which Feature III was obtained. Using all these fragment-level fMLLR features, a single Model E-4 was trained with Alignment d. Similarly for Models E-1, 2, 3 on genre, singer and song levels. The fragment-level Model E-4 turned out to be the best in model E in the experiments.

#### Relevance 772

Label: 

#### Passage 774

Retrieved by: BM25, Dense, Hybrid RRF

> improvement of 3.32% (rows (7) vs. (3)). Furthermore, the increased self-looped transition probability ( INLINEFORM0 ) in subsection UID9 for vowel HMMs also brought an 0.46% improvement when applied on top of the extended lexicon (rows (8) vs. (7)). The results show that prolonged vowels did cause problems in recognition, and the proposed approaches did help.
> 
> Rows (4)(5)(6) for Models B, C, D show the incremental improvements when training the acoustic models with a series of improved alignments a, b, c, which led to the Model E-4 in row (7). Some preliminary tests with p-norm DNN with varying parameters were then performed. The best results for the moment were obtained with 4 hidden layers, 600 and 150 hidden units for p-norm nonlinearity BIBREF26 . The result in rows (9) shows absolute improvements of 1.52% (row (9) for Model F-1 vs. row (7)) for regular DNN. Rows(10) is for Models F-1 DNN (multi-target).
> 
> Rows (11)(12)(13) show the results of BLSTMs with different factors of data augmentation described in SECREF6 . Models G-1,2,3 used three layers with 400 hidden states and 100 units for recurrent and projection layer, however, since the amount of training data were different, the number of training epoches were 15, 7 and 5 respectively. Data augmentation brought much improvement of 5.62% (rows (12) v.s.(11)), while 3-fold BLSTM outperformed 5-fold by 1.03%. Trend for Model H (rows (14)(15)(16)) is the same as Model G, 3-fold turned out to be the best. Row (15) of Model TDNN-LSTM achieved the lowest WER(%) of 73.90%, with architecture INLINEFORM0 , while INLINEFORM1 and INLINEFORM2 denotes that the size of TDNN layer was INLINEFORM3 and the size of hidden units of forward LSTM was INLINEFORM4 . The WER achieved here are relatively high, indicating the difficulties and the need for further research.

#### Relevance 774

Label: 

#### Passage 776

Retrieved by: Dense, Hybrid RRF

> We analyzed the perplexity and out-of-vocabulary(OOV) rate of the two language models (trained with LibriSpeech and Lyrics respectively) tested on the transcriptions of the testing set of vocal data. Both models are 3-gram, pruned with SRILM with the same threshold. LM trained with lyrics was found to have a significantly lower perplexity(123.92 vs 502.06) and a much lower OOV rate (0.55% vs 1.56%).
> 
> Fig. FIGREF12 depicts the histogram for pitch distribution for speech and different genders of vocal. We can see the pitch values of vocal are significantly higher with a much wider range, and female singers produce slightly higher pitch values than male singers and groups.

#### Relevance 776

Label: 

### BM25

#### Passage 773

Retrieved by: BM25

> Consider the many errors caused by the frequently appearing prolonged vowels in song audio, we considered two approaches below.
> 
> The previously proposed approach BIBREF15 was adopted here as shown by the example in Fig. FIGREF10 (a). For the word “apple”, each vowel within the word ( but not the consonants) can be either repeated or not, so for a word with INLINEFORM0 vowels, INLINEFORM1 pronunciations become possible. In the experiments below, we only did it for words with INLINEFORM2 .
> 
> This is also shown in Fig. FIGREF10 . Assume an vowel HMM have INLINEFORM0 states (including an end state). Let the original self-looped probability of state INLINEFORM1 is denoted INLINEFORM2 and the probability of transition to the next state is INLINEFORM3 . We increased the self-looped transition probabilities by replacing INLINEFORM4 by INLINEFORM5 . This was also done for vowel HMMs only but not for consonants.

#### Relevance 773

Label: 

### Dense

#### Passage 775

Retrieved by: Dense

> In Fig. FIGREF5 Model E includes different models obtained with fMLLR over different levels, Models E-1,2,3,4. But in Table. TABREF14 only Model E-4 is listed. Complete results for Models E-1,2,3,4 are listed in Table. TABREF19 , all for Lyrics Language Model with extended lexicon. Row (4) here is for Model E-4, or fMLLR over fragment level, exactly row (7) of Table. TABREF14 . Rows (1)(2)(3) are the same as row (5) here, except over levels of genre, singer and song. We see fragment level is the best, probably because fragment(10-35 sec long) is the smallest unit and the acoustic characteristic of signals within a fragment is almost uniform (same genre, same singer and the same song).

#### Relevance 775

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 777

Retrieved by: Hybrid RRF followed by BGE reranking

> in singing voice.
> 
> Applying ASR technologies to singing voice has been studied for long. However, not too much work has been reported, probably because the recognition accuracy remained to be relatively low compared to the experiences for speech. But such low accuracy is actually natural considering the various difficulties caused by the significant differences between singing voice and speech. An extra major problem is probably the lack of singing voice database, which pushed the researchers to collect their own closed datasets BIBREF12 , BIBREF15 , BIBREF17 , which made it difficult to compare results from different works.
> 
> Having the language model learned from a data set of lyrics is definitely helpful BIBREF15 , BIBREF17 . Hosoya et al. BIBREF16 achieved this with finite state automaton. Sasou et al. BIBREF12 actually prepared a language model for each song. In order to cope with the acoustic characteristics of singing voice, Sasou et al. BIBREF12 , BIBREF14 proposed AR-HMM to take care of the high-pitched sounds and prolonged vowels, while recently Kawai et al. BIBREF15 handled the prolonged vowels by extending the vowel parts in the lexicon, both achieving good improvement. Adaptation from models trained with speech was attractive, and various approaches were compared by Mesaros el al. BIBREF18 .
> 
> In this paper, we wish our work can be compatible to more available singing content, therefore in the initial effort we collected about five hours of music-removed version of English songs directly from commercial singing content on YouTube. The descriptive term "music-removed" implies the background music have been removed somehow. Because many very impressive works were based on Japanese songs BIBREF12 , BIBREF13 , BIBREF14 , BIBREF15 , BIBREF16 , the comparison is difficult. We analyzed various approaches with HMM, deep learning with data augmentation, and acoustic adaptation on fragment, song, singer, and genre levels, primarily based on fMLLR BIBREF19 . We also trained the language model with a corpus of lyrics, and modify the pronunciation lexicon and increase the transition probability of HMM for prolonged vowels. Initial results are reported.

#### Relevance 777

Label: 

#### Passage 778

Retrieved by: Hybrid RRF followed by BGE reranking

> To make our work easier and compatible to more available singing content, we collected 130 music-removed (or vocal-only) English songs from www.youtube.com so as to consider only the vocal line.The music-removing processes are conducted by the video owners, containing the original vocal recordings by the singers and vocal elements for remix purpose.
> 
> After initial test by speech recognition system trained with LibriSpeech BIBREF20 , we dropped 20 songs, with WERs exceeding 95%. The remaining 110 pieces of music-removed version of commercial English popular songs were produced by 15 male singers, 28 female singers and 19 groups. The term group means by more than one person. No any further preprocessing was performed on the data, so the data preserves many characteristics of the vocal extracted from commercial polyphonic music, such as harmony, scat, and silent parts. Some pieces also contain overlapping verses and residual background music, and some frequency components may be truncated. Below this database is called vocal data here.
> 
> These songs were manually segmented into fragments with duration ranging from 10 to 35 sec primarily at the end of the verses. Then we randomly divided the vocal data by the singer and split it into training and testing sets. We got a total of 640 fragments in the training set and 97 fragments in the testing set. The singers in the two sets do not overlap. The details of the vocal data are listed in Table. TABREF3 .
> 
> Because music genre may affect the singing style and the audio, for example, hiphop has some rap parts, and rock has some shouting vocal, we obtained five frequently observed genre labels of the vocal data from wikipedia BIBREF21 : pop, electronic, rock, hiphop, and R&B/soul. The details are also listed in Table. TABREF3 . Note that a song may belong to multiple genres.
> 
> To train initial models for speech for adaptation to singing voice, we used 100 hrs of English clean speech data of LibriSpeech.

#### Relevance 778

Label: 

#### Passage 779

Retrieved by: Hybrid RRF followed by BGE reranking

> The exploding multimedia content over the Internet, has created a new world of spoken content processing, for example the retrieval BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 , BIBREF4 , browsing BIBREF5 , summarization BIBREF0 , BIBREF5 , BIBREF6 , BIBREF7 , and comprehension BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 of spoken content. On the other hand, we may realize there still exists a huge part of multimedia content not yet taken care of, i.e., the singing content or those with audio including songs. Songs are human voice carrying plenty of semantic information just as speech. It will be highly desired if the huge quantities of singing content can be similarly retrieved, browsed, summarized or comprehended by machine based on the lyrics just as speech. For example, it is highly desired if song retrieval can be achieved based on the lyrics in addition.
> 
> Singing voice can be considered as a special type of speech with highly flexible and artistically designed prosody: the rhythm as artistically designed duration, pause and energy patterns, the melody as artistically designed pitch contours with much wider range, the lyrics as artistically authored sentences to be uttered by the singer. So transcribing lyrics from song audio is an extended version of automatic speech recognition (ASR) taking into account these differences.
> 
> On the other hand, singing voice and speech differ widely in both acoustic and linguistic characteristics. Singing signals are often accompanied with some extra music and harmony, which are noisy for recognition. The highly flexible pitch contours with much wider range BIBREF12 , BIBREF13 , the significantly changing phone durations in songs, including the prolonged vowels BIBREF14 , BIBREF15 over smoothly varying pitch contours, create much more problems not existing in speech. The falsetto in singing voice may be an extra type of human voice not present in normal speech. Regarding linguistic characteristics BIBREF16 , BIBREF17 , word repetition and meaningless words (e.g.oh) frequently appear in the artistically authored lyrics in singing voice.
> 
> Applying ASR technologies to singing voice has been studied for long. However, not too much work has been reported, probably because the recognition accuracy remained to be relatively low compared to the experiences for speech. But such

#### Relevance 779

Label: 

#### Passage 780

Retrieved by: Hybrid RRF followed by BGE reranking

> In this paper we report some initial results of transcribing lyrics from commercial song audio using different sets of acoustic models, adaptation approaches, language models and lexicons. Techniques for special characteristics of song audio were considered. The achieved WER was relatively high compared to experiences in speech recognition. However, considering the much more difficult problems in song audio and the wide difference between speech and singing voice, the results here may serve as good references for future work to be continued.

#### Relevance 780

Label: 

## Question 0085

Paper: QuaRTz: An Open-Domain Dataset of Qualitative Relationship Questions

> What are state-of-the-art models on this dataset?

### Common Retrieved Chunks

#### Passage 781

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Understanding and applying qualitative knowledge is a fundamental facet of intelligence. For example, we may read that exercise improves health, and thus decide to spend more time at the gym; or that larger cars cause more pollution, and thus decide to buy a smaller car to be environmentally sensitive. These skills require understanding the underlying qualitative relationships, and being able to apply them in specific contexts.
> 
> To promote research in this direction, we present the first open-domain dataset of qualitative relationship questions, called QuaRTz (“Qualitative Relationship Test set”). Unlike earlier work in qualitative reasoning, e.g., BIBREF0, the dataset is not restricted to a small, fixed set of relationships. Each question $Q_i$ (2-way multiple choice) is grounded in a particular situation, and is paired with a sentence $K_i$ expressing the general qualitative knowledge needed to answer it. $Q_i$ and $K_i$ are also annotated with the properties being compared (Figure FIGREF1). The property annotations serve as supervision for a potential semantic parsing based approach. The overall task is to answer the $Q_i$ given the corpus $K = \lbrace K_i\rbrace $.
> 
> We test several state-of-the-art (BERT-based) models and find that they are still substantially (20%) below human performance. Our contributions are thus (1) the dataset, containing 3864 richly annotated questions plus a background corpus of 400 qualitative knowledge sentences; and (2) an analysis of the dataset, performance of BERT-based models, and a catalog of the challenges it poses, pointing the way towards solutions.

#### Relevance 781

Label: 

#### Passage 782

Retrieved by: BM25, Dense, Hybrid RRF

> Despite rapid progress in general question-answering (QA), e.g., BIBREF1, and formal models for qualitative reasoning (QR), e.g., BIBREF2, BIBREF3, there has been little work on reasoning with textual qualitative knowledge, and no dataset available in this area. Although many datasets include a few qualitative questions, e.g., BIBREF4, BIBREF5, the only one directly probing QR is QuaRel BIBREF0. However, although QuaRel contains 2700 qualitative questions, its underlying qualitative knowledge was specified formally, using a small, fixed ontology of 19 properties. As a result, systems trained on QuaRel are limited to only questions about those properties. Likewise, although the QR community has performed some work on extracting qualitative models from text, e.g., BIBREF6, BIBREF7, and interpreting questions about identifying qualitative processes, e.g., BIBREF8, there is no dataset available for the NLP community to study textual qualitative reasoning. QuaRTz addresses this need.

#### Relevance 782

Label: 

#### Passage 783

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The results are shown in Table TABREF10, and provide insights into both the data and the models:
> 
> 1. The dataset is hard. Our best model, BERT-PFT (IR), scores only 73.7, over 20 points behind human performance (95.0), suggesting there are significant linguistic and semantic challenges to overcome (Section SECREF7).
> 
> 2. A general science-trained QA system has not learned this style of reasoning. BERT-Sci only scores 54.6, just a little above random (50.0).
> 
> 3. Pre-Fine-Tuning is important. Fine-tuning only on QuaRTz does signficantly worse (64.4) than pre-fine-tuning on RACE before fine-tuning on QuaRTz (73.7). Pre-fine-tuning appears to teach BERT something about multiple choice questions in general, helping it more effectively fine-tune on QuaRTz.
> 
> 4. BERT already “knows” some qualitative knowledge. Interestingly, BERT-PFT (no knowledge) scores 68.8, significantly above random, suggesting that BERT already “knows” some kind of qualitative knowledge. To rule out annotation artifacts, we we experimented with balancing the distributions of positive and negative influences, and different train/test splits to ensure no topical overlap between train and test, but the scores remained consistent.
> 
> 5. BERT can apply general qualitative knowledge to QA, but only partially. The model for the full task, BERT-PFT (IR) outperforms the no knowledge version (73.7, vs. 68.8), but still over 20 points below human performance. Even given the ideal knowledge (IR upper bound), it is still substantially behind (at 79.8) human performance. This suggests more sophisticated ways of training and/or reasoning with the knowledge are needed.

#### Relevance 783

Label: 

#### Passage 784

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The QuaRTz task is to answer the questions given the corpus $K$ of qualitative background knowledge. We also examine a “no knowledge” (questions only) task and a “perfect knowledge” task (each question paired with the qualitative sentence $K_i$ it was based on). We report results using two baselines and several strong models built with BERT-large BIBREF9 as follows:
> 
> 1. Random: always 50% (2-way MC).
> 
> 2. BERT-Sci: BERT fine-tuned on a large, general set of science questions BIBREF5.
> 
> 3. BERT (IR): This model performs the full task. First, a sentence $K_i$ is retrieved from $K$ using $Q_i$ as a search query. This is then supplied to BERT as [CLS] $K_i$ [SEP] question-stem [SEP] answer-option [SEP] for each option. The [CLS] output token is projected to a single logit and fed through a softmax layer across answer options, using cross entropy loss, the highest being selected. This model is fine-tuned using QuaRTz (only).
> 
> 4. BERT (IR upper bound): Same, but using the ideal (annotated) $K_i$ rather than retrieved $K_i$.
> 
> 5. BERT-PFT (no knowledge): BERT first fine-tuned (“pre-fine-tuned”) on the RACE dataset BIBREF10, BIBREF11, and then fine-tuned on QuaRTz (questions only, no $K$, both train and test). Questions are supplied as [CLS] question-stem [SEP] answer-option [SEP].
> 
> 6. BERT-PFT (IR): Same as BERT (IR), except starting with the pre-fine-tuned BERT.
> 
> All models were implemented using AllenNLP BIBREF12.

#### Relevance 784

Label: 

#### Passage 786

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> QuaRTz includes a rich set of annotations on all the knowledge sentences and questions, marking the properties being compared, and the linguistic and semantic comparatives employed (Figure FIGREF1). This provides a laboratory for exploring semantic parsing approaches, e.g., BIBREF13, BIBREF14, where the underlying qualitative comparisons are extracted and can be reasoned about.

#### Relevance 786

Label: 

### BM25

#### Passage 785

Retrieved by: BM25

> Understanding and applying textual qualitative knowledge is an important skill for question-answering, but has received limited attention, in part due the lack of a broad-coverage dataset to study the task. QuaRTz aims to fill this gap by providing the first open-domain dataset of qualitative relationship questions, along with the requisite qualitative knowledge and a rich set of annotations. Specifically, QuaRTz removes the requirement, present in all previous qualitative reasoning work, that a fixed set of qualitative relationships be formally pre-specified. Instead, QuaRTz tests the ability of a system to find and apply an arbitrary relationship on the fly to answer a question, including when simple reasoning (arguments, polarities) is required.
> 
> As the QuaRTz task involves using a general corpus $K$ of textual qualitative knowledge, a high-performing system would be close to a fully general system where $K$ was much larger (e.g., the Web or a filtered subset), encompassing many more qualitative relationships, and able to answer arbitrary questions of this kind. Scaling further would thus require more sophisticated retrieval over a larger corpus, and (sometimes) chaining across influences, when a direct connection was not described in the corpus. QuaRTz thus provides a dataset towards this end, allowing controlled experiments while still covering a substantial number of textual relations in an open setting. QuaRTz is available at http://data.allenai.org/quartz/.

#### Relevance 785

Label: 

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 787

Retrieved by: Hybrid RRF followed by BGE reranking

> QuaRTz was constructed as follows. First, 400 sentences expressing general qualitative relations were manually extracted by the authors from a large corpus using keyword search (“increase”, “faster”, etc.). Examples ($K_i$) are in Table TABREF3.
> 
> Second, crowdworkers were shown a seed sentence $K_i$, and asked to annotate the two properties being compared using the template below, illustrated using $K_2$ from Table TABREF3:
> 
> [vskip=0mm,leftmargin=3mm]
> 
> "The smaller its mass is, the greater its acceleration for a given amount of force."
> 
> They were then asked to author a situated, 2-way multiple-choice (MC) question that tested this relationship, guided by multiple illustrations. Examples of their questions ($Q_i$) are in Table TABREF3.
> 
> Third, a second set of workers was shown an authored question, asked to validate its answer and quality, and asked to annotate how the properties of $K_i$ identified earlier were expressed. To do this, they filled a second template, illustrated for $Q_2$:
> 
> Finally these workers were asked to generate a new question by “flipping” the original so the answer switched. Flipping means inverting comparatives (e.g., “more” $\rightarrow $ “less”), values, and other edits as needed to change the answer, e.g.,
> 
> K: More rain causes damper surfaces.
> 
> Q:More rain causes (A) wetter land (B) drier land
> 
> Q-flipped: Less rain causes (A) wetter land (B)
> 
> drier land
> 
> Flipped questions are created to counteract the tendency of workers to use the same comparison direction (e.g., “more”) in their question as in the seed sentence $K_i$, potentially answerable by simply matching $Q_i$ and $K_i$. Flipped questions are more challenging as they demand more qualitative reasoning (Section SECREF11).
> 
> Questions marked by workers as poor quality were reviewed by the authors and rejected/modified as appropriate. The dataset was then split into train/dev/test partitions such that questions from the same seed $K_i$ were all in the same partition. Statistics are in Table TABREF9.
> 
> To determine if the questions are correct and answerable given the general knowledge, a human baseline was computed. Three annotators independently answered a random sample of 100 questions given the supporting sentence $K_i$ for each. The mean score was 95.0%.

#### Relevance 787

Label: 

## Question 0086

Paper: GameWikiSum: a Novel Large Multi-Document Summarization Dataset

> What extractive models were trained on this dataset?

### Common Retrieved Chunks

#### Passage 788

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We build GameWikiSum corpus by considering English reviews and Wikipedia pages. Table TABREF11 describes its overall properties. Most samples contain several reviews, whose cumulative size is too large for extractive or abstractive models to be trained in an end-to-end manner. The total vocabulary is composed of $282\,992$ words. Our dataset also comes from a diverse set of sources: over 480 video game websites appear as source documents in at least 6 video games; they are responsible for $99.95\%$ of the reviews.
> 
> Following wiki2018, a subset of the input has to be therefore first coarsely selected, using extractive summarization, before training an extractive or abstractive model that generates the Wikipedia gameplay text while conditioning on this extraction. Additionally, half of the summaries contain more than three hundred words (see Table TABREF11), which is larger than previous work.
> 
> To validate our hypothesis that professional game reviews focus heavily on gameplay mechanics, we compute the proportion of unigrams and bigrams of the output given the input. We observe a significant overlap ($20\%$ documents containing $67.7\%$ of the words mentioned in the summary, and at least $27.4\%$ bigrams in half of the documents), emphasizing the extractive nature of GameWikiSum. Several examples of summaries are shown in Section SECREF20
> 
> https://www-nlpir.nist.gov/projects/duc/guidelines.html http://www.nist.gov/tac/
> 
> Table TABREF12 shows a comparison between GameWikiSum and other single and multi-document summarization datasets. GameWikiSum has larger input and output size than single document summarization corpora (used in extractive and abstractive models) while sharing similar word overlap ratios. Compared to DUC and TAC (news domain), GameWikiSum is also domain-specific and has two orders of magnitude more examples, facilitating the use of more powerful models. Finally, WikiSum has more samples but is more suitable for general abstractive summarization, as its articles cover a wide range of areas and have a lower word overlap ratio.
> 
> We divide GameWikiSum into train, validation and testing sets with a rough ratio of 80/10/10, resulting in $11\,744$, $1\,454$ and $1\,454$ examples respectively. If a game has been released on several platforms (represented by different samples), we group them in the same subset to avoid review overlap between training, validation, and testing. The distribution of samples per platform is shown in Table TABREF13. We compute in

#### Relevance 788

Label: 

#### Passage 789

Retrieved by: BM25, Dense, Hybrid RRF

> Table TABREF19 contains the results. LEAD-5 achieves less than 20 for ROUGE-L as well as ROUGE-1 and less than $3.5$ for ROUGE-2. Taking only 3 sentences leads to even worse results: below 13 and 3 respectively. Unlike in other datasets, these results are significantly outperformed by all other extractive models but surprisingly, abstractive models perform worse on average. This demonstrates the difficulty of the task in GameWikiSum compared to nallapati2016abstractive and graff2003.
> 
> For extractive models, TextRank and LexRank perform worse than other models. The frequency-based model SumBasic performs slightly better but does not achieve comparable results with embedding-based models. Best results are obtained with C_SKIP and SemSentSum, showing that more sophisticated models can be trained on GameWikiSum and improve results significantly. Interestingly, taking into account the context of a sentence and hence better capturing the semantics, SemSentSum achieves only slightly better scores than C_SKIP, which relies solely on word embedding. We show in Section SECREF20 several examples with their original summaries and generated ones with the best model.
> 
> Overall, the abstractive performance of sequence-to-sequence and language models are significantly lower than C_SKIP and SemSentSum in terms of ROUGE-L and ROUGE-1. However, Conv2Conv obtains only $0.05$ less ROUGE-2 score compared to C_SKIP and $0.36$ to SemSentSum. We suspect ROUGE-2 to be easier for abstractive sequence-to-sequence models, as half of the samples only have a ROUGE-2 around $27.00$ without any limitation of the input size (see Table TABREF11). Consequently, copying sentences from a small subset of the whole input documents for extractive models leads to worse ROUGE-2 recall. A normal transformer underperforms compared to Conv2Conv, and its language model variant achieves significantly worse results than other models due to a lack of data.
> 
> We highlight that GameWikiSum has two orders of magnitude fewer samples (see Table TABREF12) compared to wiki2018. Therefore, it is necessary to have either additional annotated data or pre-train TransformerLM on another corpus.

#### Relevance 789

Label: 

#### Passage 790

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> In this work, we introduce a new multi-document summarization dataset, GameWikiSum, based on professional video game reviews, which is one hundred times larger than commonly used datasets. We conclude that the size of GameWikiSum and its domain-specificity makes the training of abstractive and extractive models possible. In future work, we could increase the dataset with other languages and use it for multilingual multi-document summarization. We release GameWikiSum for further research: https://github.com/Diego999/GameWikiSum.

#### Relevance 790

Label: 

#### Passage 791

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> With the growth of the internet in the last decades, users are faced with an increasing amount of information and have to find ways to summarize it. However, producing summaries in a multi-document setting is a challenging task; the language used to display the same information in a sentence can vary significantly, making it difficult for summarization models to capture. Thus large corpora are needed to develop efficient models. There exist two types of summarization: extractive and abstractive. Extractive summarization outputs summaries in two steps, namely via sentence ranking, where an importance score is assigned to each sentence, and via the subsequent sentence selection, where the most appropriate sentence is chosen. In abstractive summarization, summaries are generated word by word auto-regressively, using sequence-to-sequence or language models. Given the complexity of multi-document summarization and the lack of datasets, most researchers use extractive summarization and rely on hand-crafted features or additional annotated data, both needing human expertise.
> 
> To our knowledge, wiki2018 is the only work that has proposed a large dataset for multi-document summarization. By considering Wikipedia entries as a collection of summaries on various topics given by their title (e.g., Machine Learning, Stephen King), they create a dataset of significant size, where the lead section of an article is defined as the reference summary and input documents are a mixture of pages obtained from the article's reference section and a search engine. While this approach benefits from the large number of Wikipedia articles, in many cases, articles contain only a few references that tend to be of the desired high quality, and most input documents end up being obtained via a search engine, which results in noisy data. Moreover, at testing time no references are provided, as they have to be provided by human contributors. wiki2018 showed that in this case, generated summaries based on search engine results alone are of poor quality and cannot be used.
> 
> In contrast, we propose a novel domain-specific dataset containing $14\,652$ samples, based on professional video game reviews obtained via Metacritic and gameplay sections from Wikipedia. By using Metacritic reviews in addition to Wikipedia articles, we benefit from a number of factors. First, the set of aspects used to assess

#### Relevance 791

Label: 

#### Passage 792

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> For extractive models, we include LEAD-$k$ which is a strong baseline for single document summarization tasks and takes the first $k$ sentences in the document as summary BIBREF5. TextRank BIBREF6 and LexRank BIBREF7 are two graph-based methods, where nodes are text units and edges are defined by a similarity measure. SumBasic BIBREF8 is a frequency-based sentence selection method, which uses a component to re-weigh the word probabilities in order to minimize redundancy. The last extractive baselines are the near state-of-the-art models C_SKIP from rossiello2017centroid and SemSenSum from antognini2019. The former exploits the capability of word embeddings to leverage semantics, whereas the latter aggregates two types of sentence embeddings using a sentence semantic relation graph, followed by a graph convolution.
> 
> We use common abstractive sequence-to-sequence baselines such as Conv2Conv BIBREF9, Transformer BIBREF10 and its language model variant, TransformerLM BIBREF3. We use implementations from fairseq and tensor2tensor. As the corpus size is too large to train extractive and abstractive models in an end-to-end manner due to hardware constraints, we use Tf-Idf to coarsely select sentences before training similarly to wiki2018. We limit the input size to 2K tokens so that all models can be trained on a Titan Xp GPU (12GB GPU RAM). We run all models with their best reported parameters.

#### Relevance 792

Label: 

#### Passage 793

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We use the standard ROUGE BIBREF4 used in summarization and report the ROUGE-L F1 score. ROUGE-L F1 is more appropriate to measure the quality of generated summaries in this context because summary lengths are longer than usual (see Table TABREF12) and vary across the dataset (see Table TABREF11). Another motivation to use ROUGE-L F1 is to compare abstractive models with extractive ones, as the output length is unknown a priori for the former, but not for the latter. We report in addition ROUGE-1 and ROUGE-2 recall scores.
> 
> To ensure consistent results across all comparative experiments, extractive models generate summaries of the same length as reference summaries. In realistic scenarios, summary lengths are not pre-defined and can be adjusted to produce different types of summaries (e.g., short, medium or long). We do not explicitly constrain the output length for abstractive models, as each summary is auto-regressively generated.

#### Relevance 793

Label: 

### BM25

None

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0087

Paper: Bayesian Models for Unit Discovery on a Very Low Resource Language

> What bayesian model is trained?

### Common Retrieved Chunks

#### Passage 794

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The AUD model described in BIBREF0 , BIBREF1 is a non-parametric Bayesian Hidden Markov Model (HMM). This model is topologically equivalent to a phone-loop model with two major differences:
> 
> In this work, we have used two variants of this original model. The first one (called HMM model in the remainder of this paper), following the analysis led in BIBREF8 , approximates the Dirichlet Process prior by a mere symmetric Dirichlet prior. This approximation, while retaining the sparsity constraint, avoids the complication of dealing with the variational treatment of the stick breaking process frequent in Bayesian non-parametric models. The second variant, which we shall denote Structured Variational AutoEncoder (SVAE) AUD, is based upon the work of BIBREF4 and embeds the HMM model into the Variational AutoEncoder framework BIBREF9 . A very similar version of the SVAE for AUD was developed independently and presented in BIBREF5 . The main noteworthy difference between BIBREF5 and our model is that we consider a fully Bayesian version of the HMM embedded in the VAE; and the posterior distribution and the VAE parameters are trained jointly using the Stochastic Variational Bayes BIBREF4 , BIBREF10 . For both variants, the prior over the HMM parameters were set to the conjugate of the likelihood density: Normal-Gamma prior for the mean and variance of the Gaussian components, symmetric Dirichlet prior over the HMM's state mixture's weights and symmetric Dirichlet prior over the acoustic units' weights. For the case of the uninformative prior, the prior was set to be vague prior with one pseudo-observation BIBREF11 .

#### Relevance 794

Label: 

#### Passage 795

Retrieved by: BM25, Dense, Hybrid RRF

> First, we evaluated the standard HMM model with an uninformative prior (this will be our baseline) for the two different input features: MFCC (and derivatives) and MBN. Results are shown in Table TABREF20 . Surprisingly, the MBN features perform relatively poorly compared to the standard MFCC. These results are contradictory to those reported in BIBREF3 . Two factors may explain this discrepancy: the Mboshi5k data being different from the training data of the MBN neural network, the neural network may not generalize well. Another possibility may be that the initialization scheme of the model is not suitable for this type of features. Indeed, Variational Bayesian Inference algorithm converges only to a local optimum of the objective function and is therefore dependent of the initialization. We believe the second explanation is the more likely since, as we shall see shortly, the best results in term of word segmentation and NMI are eventually obtained with the MBN features when the inference is done with the informative prior. Next, we compared the HMM and the SVAE models when trained with an uninformative prior (lines with "Inf. Prior" set to "no" in Table TABREF23 ). The SVAE significantly improves the NMI and the precision showing that it extracts more consistent units than the HMM model. However, it also degrades the segmentation in terms of recall. We further investigated this behavior by looking at the duration of the units found by both models compared to the true phones (Table TABREF22 ). We observe that the SVAE model favors longer units than the HMM model hence leading to fewer boundaries and consequently smaller recall.
> 
> We then evaluated the effect of the informative prior on the acoustic unit discovery (Table TABREF23 ). On all 4 combinations (2 features sets INLINEFORM0 2 models) we observe an improvement in terms of precision and NMI but a degradation of the recall. This result is encouraging since the informative prior was trained on English data (TIMIT) which is very different from Mboshi. Indeed, this suggests that even speech from an unrelated language can be of some help in the design of an ASR for a very low resource language. Finally, similarly to the SVAE/HMM case described

#### Relevance 795

Label: 

#### Passage 796

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> is that it naturally leads to a sequential inference. Therefore, model training can be summarized as:
> 
> Practically, the computation of the informative prior as well as the final posterior distribution is intractable and we seek for an approximation by means of the well known Variational Bayes Inference BIBREF12 . The approximate informative prior INLINEFORM0 is estimated by optimizing the variational lower bound of the evidence of the prior data INLINEFORM1 : DISPLAYFORM0
> 
> where INLINEFORM0 is the Kullback-Leibler divergence. Then, the posterior distribution of the parameters given the target data INLINEFORM1 can be estimated by optimizing the evidence of the target data INLINEFORM2 : DISPLAYFORM0
> 
> Note that when the model is trained with an uninformative prior the loss function is the as in Eq. EQREF13 but with INLINEFORM0 instead of the INLINEFORM1 . For the case of the uninformative prior, the Variational Bayes Inference was initialized as described in BIBREF1 . In the informative prior case, we initialized the algorithm by setting INLINEFORM2 .

#### Relevance 796

Label: 

#### Passage 797

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Bayesian Inference differs from other machine learning techniques by introducing a distribution INLINEFORM0 over the parameters of the model. A major concern in Bayesian Inference is usually to define a prior that makes as little assumption as possible. Such a prior is usually known as uninformative prior. Having a completely uninformative prior has the practical advantage that the prior distribution will have a minimal impact on the outcome of the inference leading to a model which bases its prediction purely and solely on the data. In the present work, we aim at the opposite behavior, we wish our AUD model to learn phone-like units from the unlabeled speech data of a target language given the knowledge that was previously accumulated from another resourceful language. More formally, the original AUD model training consists in estimate the a posteriori distribution of the parameters given the unlabeled speech data of a target language INLINEFORM1 : DISPLAYFORM0
> 
> The parameters are divided into two subgroups INLINEFORM0 where INLINEFORM1 are the global parameters of the model, and INLINEFORM2 are the latent variables which, in our case, correspond to the sequences of acoustic units. The global parameters are separated into two independent subsets : INLINEFORM3 , corresponding to the acoustic parameters ( INLINEFORM4 ) and the "phonotactic" language model parameters ( INLINEFORM5 ). Replacing INLINEFORM6 and following the conditional independence of the variable induced by the model (see BIBREF1 for details) leads to: DISPLAYFORM0
> 
> If we further assume that we have at our disposal speech data in a different language than the target one, denoted INLINEFORM0 , along with its phonetic transcription INLINEFORM1 , it is then straightforward to show that: DISPLAYFORM0
> 
> which is the same as Eq. EQREF8 but for the distribution of the acoustic parameters which is based on the data of the resourceful language. In contrast of the term uninformative prior we denote INLINEFORM0 as an informative prior. As illustrated by Eq. EQREF9 , a characteristic of Bayesian inference is that it naturally leads to a sequential inference. Therefore, model training can be summarized as:
> 
> Practically, the computation of the informative prior as well as the final posterior distribution is intractable and we seek for an approximation by means

#### Relevance 797

Label: 

#### Passage 798

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Out of nearly 7000 languages spoken worldwide, current speech (ASR, TTS, voice search, etc.) technologies barely address 200 of them. Broadening ASR technologies to ideally all possible languages is a challenge with very high stakes in many areas and is at the heart of several fundamental research problems ranging from psycholinguistic (how humans learn to recognize speech) to pure machine learning (how to extract knowledge from unlabeled data). The present work focuses on the narrow but important problem of unsupervised Acoustic Unit Discovery (AUD). It takes place as the continuation of an ongoing effort to develop a Bayesian model suitable for this task, which stems from the seminal work of BIBREF0 later refined and made scalable in BIBREF1 . This model, while rather crude, has shown that it can provide a clustering accurate enough to be used in topic identification of spoken document in unknown languages BIBREF2 . It was also shown that this model can be further improved by incorporating a Bayesian "phonotactic" language model learned jointly with the acoustic units BIBREF3 . Finally, following the work in BIBREF4 it has been combined successfully with variational auto-encoders leading to a model combining the potential of both deep neural networks and Bayesian models BIBREF5 . The contribution of this work is threefold:

#### Relevance 798

Label: 

### BM25

None

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 799

Retrieved by: Hybrid RRF followed by BGE reranking

> We have conducted an analysis of the state-of-the-art Bayesian approach for acoustic unit discovery on a real case of low-resource language. This analysis was focused on the quality of the discovered units compared to the gold standard phone alignments. Outcomes of the analysis are i) the combination of neural network and Bayesian model (SVAE) yields a significant improvement in the AUD in term of consistency ii) Bayesian models can naturally embed information from a resourceful language and consequently improve the consistency of the discovered units. Finally, we hope this work can serve as a baseline for future research on unsupervised acoustic unit discovery in very low resource scenarios.

#### Relevance 799

Label: 

## Question 0088

Paper: SAMSum Corpus: A Human-annotated Dialogue Dataset for Abstractive Summarization

> How is human evaluators' judgement measured, what was the criteria?

### Common Retrieved Chunks

#### Passage 800

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> ROUGE is a standard way of evaluating the quality of machine generated summaries by comparing them with reference ones. The metric based on n-gram overlapping, however, may not be very informative for abstractive summarization, where paraphrasing is a keypoint in producing high-quality sentences. To quantify this conjecture, we manually evaluated summaries generated by the models for 150 news and 100 dialogues. We asked two linguists to mark the quality of every summary on the scale of $-1$, 0, 1, where $-1$ means that a summarization is poor, extracts irrelevant information or does not make sense at all, 1 – it is understandable and gives a brief overview of the text, and 0 stands for a summarization that extracts only a part of relevant information, or makes some mistakes in the produced summary.
> 
> We noticed a few annotations (7 for news and 4 for dialogues) with opposite marks (i.e. one annotator judgement was $-1$, whereas the second one was 1) and decided to have them annotated once again by another annotator who had to resolve conflicts. For the rest, we calculated the linear weighted Cohen's kappa coefficient BIBREF22 between annotators' scores. For news examples, we obtained agreement on the level of $0.371$ and for dialogues – $0.506$. The annotators' agreement is higher on dialogues than on news, probably because of structures of those data – articles are often long and it is difficult to decide what the key-point of the text is; dialogues, on the contrary, are rather short and focused mainly on one topic.
> 
> For manually evaluated samples, we calculated ROUGE metrics and the mean of two human ratings; the prepared statistics is presented in Table TABREF27. As we can see, models generating dialogue summaries can obtain high ROUGE results, but their outputs are marked as poor by human annotators. Our conclusion is that the ROUGE metric corresponds with the quality of generated summaries for news much better than for dialogues, confirmed by Pearson's correlation between human evaluation and the ROUGE metric, shown in Table TABREF28.

#### Relevance 800

Label: 

#### Passage 801

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> This paper is a step towards abstractive summarization of dialogues by (1) introducing a new dataset, created for this task, (2) comparison with news summarization by the means of automated (ROUGE) and human evaluation.
> 
> Most of the tools and the metrics measuring the quality of text summarization have been developed for a single-speaker document, such as news; as such, they are not necessarily the best choice for conversations with several speakers.
> 
> We test a few general-purpose summarization models. In terms of human evaluation, the results of dialogues summarization are worse than the results of news summarization. This is connected with the fact that the dialogue structure is more complex – information is spread in multiple utterances, discussions, questions, more typos and slang words appear there, posing new challenges for summarization. On the other hand, dialogues are divided into utterances, and for each utterance its author is assigned. We demonstrate in experiments that the models benefit from the introduction of separators, which mark utterances for each person. This suggests that dedicated models having some architectural changes, taking into account the assignation of a person to an utterance in a systematic manner, could improve the quality of dialogue summarization.
> 
> We show that the most popular summarization metric ROUGE does not reflect the quality of a summary. Looking at the ROUGE scores, one concludes that the dialogue summarization models perform better than the ones for news summarization. In fact, this hypothesis is not true – we performed an independent, manual analysis of summaries and we demonstrated that high ROUGE results, obtained for automatically-generated dialogue summaries, correspond with lower evaluation marks given by human annotators. An interesting example of the misleading behavior of the ROUGE metrics is presented in Table TABREF35 for Dialogue 4, where a wrong summary – 'paul and cindy don't like red roses.' – obtained all ROUGE values higher than a correct summary – 'paul asks cindy what color flowers should buy.'. Despite lower ROUGE values, news summaries were scored higher by human evaluators. We conclude that when measuring the quality of model-generated summaries, the ROUGE metrics are more indicative for news than for dialogues, and a new metric should be designed to measure the quality

#### Relevance 801

Label: 

#### Passage 802

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> news summaries were scored higher by human evaluators. We conclude that when measuring the quality of model-generated summaries, the ROUGE metrics are more indicative for news than for dialogues, and a new metric should be designed to measure the quality of abstractive dialogue summaries.

#### Relevance 802

Label: 

#### Passage 803

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The paper is structured as follows: in Section SECREF2 we present details about the new corpus and describe how it was created, validated and cleaned. Brief description of baselines used in the summarization task can be found in Section SECREF3. In Section SECREF4, we describe our experimental setup and parameters of models. Both evaluations of summarization models, the automatic with ROUGE metric and the linguistic one, are reported in Section SECREF5 and Section SECREF6, respectively. Examples of models' outputs and some errors they make are described in Section SECREF7. Finally, discussion, conclusions and ideas for further research are presented in sections SECREF8 and SECREF9.

#### Relevance 803

Label: 

#### Passage 805

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We evaluate models with the standard ROUGE metric BIBREF21, reporting the $F_1$ scores (with stemming) for ROUGE-1, ROUGE-2 and ROUGE-L following previous works BIBREF5, BIBREF4. We obtain scores using the py-rouge package.

#### Relevance 805

Label: 

### BM25

#### Passage 804

Retrieved by: BM25

> The goal of the summarization task is condensing a piece of text into a shorter version that covers the main points succinctly. In the abstractive approach important pieces of information are presented using words and phrases not necessarily appearing in the source text. This requires natural language generation techniques with high level of semantic understanding BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, BIBREF5, BIBREF6.
> 
> Major research efforts have focused so far on summarization of single-speaker documents like news (e.g., BIBREF7) or scientific publications (e.g., BIBREF8). One of the reasons is the availability of large, high-quality news datasets with annotated summaries, e.g., CNN/Daily Mail BIBREF9, BIBREF7. Such a comprehensive dataset for dialogues is lacking.
> 
> The challenges posed by the abstractive dialogue summarization task have been discussed in the literature with regard to AMI meeting corpus BIBREF10, e.g. BIBREF11, BIBREF12, BIBREF13. Since the corpus has a low number of summaries (for 141 dialogues), BIBREF13 proposed to use assigned topic descriptions as gold references. These are short, label-like goals of the meeting, e.g., costing evaluation of project process; components, materials and energy sources; chitchat. Such descriptions, however, are very general, lacking the messenger-like structure and any information about the speakers.
> 
> To benefit from large news corpora, BIBREF14 built a dialogue summarization model that first converts a conversation into a structured text document and later applies an attention-based pointer network to create an abstractive summary. Their model, trained on structured text documents of CNN/Daily Mail dataset, was evaluated on the Argumentative Dialogue Summary Corpus BIBREF15, which, however, contains only 45 dialogues.
> 
> In the present paper, we further investigate the problem of abstractive dialogue summarization. With the growing popularity of online conversations via applications like Messenger, WhatsApp and WeChat, summarization of chats between a few participants is a new interesting direction of summarization research. For this purpose we have created the SAMSum Corpus which contains over 16k chat dialogues with manually annotated summaries. The dataset is freely available for the research community.
> 
> The paper is structured as follows: in Section SECREF2 we present details about the new corpus and describe how it was created, validated and cleaned. Brief description of baselines used in the summarization task can be found in Section SECREF3.

#### Relevance 804

Label: 

### Dense

#### Passage 806

Retrieved by: Dense

> This section contains a description of setting used in the experiments carried out.

#### Relevance 806

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0089

Paper: Forget Me Not: Reducing Catastrophic Forgetting for Domain Adaptation in Reading Comprehension

> Does regularization of the fine-tuning process hurt performance in the target domain?

### Common Retrieved Chunks

#### Passage 807

Retrieved by: BM25, Hybrid RRF

> to predict 2 indices), while decaNLP is a generative model (goal is to generate the correct word sequence). Also, unlike QANet and decaNLP, BERT is not designed specifically for RC. It represents a growing trend in the literature where large models are pre-trained on big corpora and further adapted to downstream tasks.
> 
> To reduce the forgetting of source domain knowledge, we introduce auxiliary penalty terms to regularise the fine-tuning process. We favour this approach as it does not require storing data samples from the source domain. In general, there are two types of penalty: selective and non-selective. The former penalises the model when certain parameters diverge significantly from the source model, while the latter uses a pre-defined distance function to measure the change of all parameters.
> 
> For selective penalty, we use elastic weight consolidation (EWC: BIBREF8), which weighs the importance of a parameter based on its gradient when training the source model. For non-selective penalty, we explore L2 BIBREF7 and cosine distance. We detail the methods below.
> 
> Given a source and target domain, we pre-train the model first on the source domain and fine-tune it further on the target domain. We denote the optimised parameters of the source model as ${\theta ^*}$ and that of the target model as ${\theta }$. For vanilla fine-tuning (finetune), the loss function is:
> 
> where $\mathcal {L}_{ce}$ is the cross-entropy loss.
> 
> For non-selective penalty, we measure the change of parameters based on a distance function (treating all parameters as equally important), and add it as a loss term in addition to the cross-entropy loss. One distance function we test is the L2 distance:
> 
> where $\lambda _{l2}$ is a scaling hyper-parameter to weigh the contribution of the penalty. Henceforth all scaling hyper-parameters are denoted using $\lambda $.
> 
> We also experiment with cosine distance, based on the idea that we want to encourage the parameters to be in the same direction after fine-tuning. In this case, we group parameters by the variables they are defined in, and measure the cosine distance between variables:
> 
> where $\theta _v$ denotes the vector of parameters belonging to variable $v$.
> 
> For selective penalty, EWC uses the Fisher matrix $F$ to measure the importance of parameter $i$ in

#### Relevance 807

Label: 

#### Passage 809

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Reading comprehension (RC) is the task of answering a question given a context passage. Related to Question-Answering (QA), RC is seen as a module in the full QA pipeline, where it assumes a related context passage has been extracted and the goal is to produce an answer based on the context. In recent years, the creation of large-scale open domain comprehension data sets BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, BIBREF5 has spurred the development of a host of end-to-end neural comprehension systems with promising results.
> 
> In spite of these successes, it is difficult to train these modern comprehension systems on narrow domain data (e.g. biomedical), as these models often have a large number of parameters. A better approach is to transfer knowledge via fine-tuning, i.e. by first pre-training the model using data from a large source domain and continue training it with examples from the small target domain. It is an effective strategy, although a fine-tuned model often performs poorly when it is re-applied to the source domain, a phenomenon known as catastrophic forgetting BIBREF6, BIBREF7, BIBREF8, BIBREF9. This is generally not an issue if the goal is to optimise purely for the target domain, but in real-word applications where model robustness is an important quality, over-optimising for a development set often leads to unexpected poor performance when applied to test cases in the wild.
> 
> In this paper, we explore strategies to reduce forgetting for comprehension systems during domain adaption. Our goal is to preserve the source domain's performance as much as possible, while keeping target domain's performance optimal and assuming no access to the source data. We experiment with a number of auxiliary penalty terms to regularise the fine-tuning process for three modern RC models: QANet BIBREF10, decaNLP BIBREF11 and BERT BIBREF12. We observe that combining different auxiliary penalty terms results in the best performance, outperforming benchmark methods that require source data.
> 
> Technically speaking, the methods we propose are not limited to domain transfer for reading comprehension. We also show that the methodology can be used for transferring to entirely different tasks. With that said, we focus on comprehension here because it is a practical problem in real world applications, where the target domain often

#### Relevance 809

Label: 

#### Passage 811

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> substantially better, on average 2.86 points more for QANet and 5.57 points more BERT. For decaNLP, the improvement is minute (0.02); generally gem has the upper hand for most domains but the advantage is cancelled out by its poor performance in one domain (ms -fn). As gem requires storing training data from the source domain (squad training examples in this case), the auxiliary penalty techniques are more favourable for real world applications.
> 
> Does adding these penalty terms harm target performance? Looking at the “Test” performance between finetune and +all, we see that they are generally comparable. We found that the average performance difference (+all-finetune) is 0.23, $-$0.42 and 0.34 for QANet, decaNLP and BERT respectively, implying that it does not (in fact, it has a small positive net impact for QANet and BERT). In some cases it improves target performance substantially, e.g. in bioasq for BERT, the target performance is improved from 71.62 to 76.93, when +all is applied.
> 
> Based on these observations, we see benefits for incorporating these penalties when adapting comprehension models, as it produces a more robust model that preserves its source performance (to a certain extent) without trading off its target performance. In some cases, it can even improve the target performance.

#### Relevance 811

Label: 

#### Passage 812

Retrieved by: Dense, Hybrid RRF

> In previous experiments, we fine-tune a pre-trained model to each domain independently. With continuous learning, we seek to investigate the performance of finetune and its four variants (+l2, +cd, +ewcn and +all) when they are applied to a series of fine-tuning on multiple domains. For the remainder of experiments in the paper, we test only with decaNLP.
> 
> When computing the penalties, we consider the last trained model as the source model. Figure FIGREF11 demonstrates the performance of the models on the development set of squad and test sets of ms -bm and ms -cp when they are adapted to ms -bm, ms -cp, ms -fn, ms -ms, ms -fm and ms -lw in sequence. We exclude plots for the latter domains as they are similar to that of ms -cp.
> 
> Including the pre-training on squad, all models are trained for a total of 170K iterations: squad from 0–44K, ms -bm from 45K–65K, ms -cp from 66K–86K, ms -fn from 87K–107K, ms -ms from 108K–128K, ms -fm from 129K–149K and ms -lw from 150K–170K.
> 
> We first look at the recovery for squad in Figure FIGREF11. +all (black line; legend in Figure FIGREF11) trails well above all other models after a series of fine-tuning, followed by +ewcn and +cd, while finetune produces the most forgetting. At the end of the continuous learning, +all recovers more than 5 F1 points compared to finetune. We see a similar trend for ms -bm (Figure FIGREF11), although the difference is less pronounced. The largest gap between finetune and +all occurs when we fine-tune for ms -fm (iteration 129K–149K). Note that we are not trading off target performance when we first tune for ms -bm (iteration 45K–65K), where finetune and +all produces comparable F1.
> 
> For ms -cp (Figure FIGREF11), we first notice that there is considerably less forgetting overall (ms -cp performance ranges from 65–75 F1, while squad performance in Figure FIGREF11 ranges from 45–75 F1). This is perhaps unsurprising, as the model is already generally well-tuned (e.g. it takes less iterations to reach optimal performance for ms -cp compared to ms -bm and squad). Most models perform similarly here. +all produces stronger recovery when fine-tuning on ms -fm (129K–149K) and ms

#### Relevance 812

Label: 

#### Passage 814

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> (“Test”). We first compare the performance between scratch and finetune. Across all domains for QANet, decaNLP and BERT, finetune substantially improves the target domain's performance compared to scratch. The largest improvement is seen in bioasq for QANet, where its F1 improves two-fold (from 29.83 to 65.81). Among the three RC models, BERT has the best performance for both scratch and finetune in most target domains (with a few exceptions such as ms -fn and ms -lw). Between QANet and decaNLP, we see that decaNLP tends to have better scratch performance but the pattern is reversed in finetune, where QANet produces higher F1 than decaNLP in all domains except for ms -lw.
> 
> In terms of squad performance, we see that finetune degrades it considerably compared to its pre-trained performance. The average drop across all domains compared to their pre-trained performance is 20.30, 15.30 and 15.07 points for QANet, decaNLP and BERT, respectively. For most domains, F1 scores drop by 10-20 points, while for ms -cp the performance is much worse for QANet, with a drop of 41.34. Interestingly, we see BERT suffers from catastrophic forgetting just as much as the other models, even though it is a larger model with orders of magnitude more parameters.
> 
> We now turn to the fine-tuning results with auxiliary penalties (+ewc, +ewcn, +cd and +l2). Between +ewc and +ewcn, the normalised versions consistently produces better recovery for the source domain (one exception is ms -ms for decaNLP), demonstrating that normalisation helps. Between +ewcn, +cd and +l2, performance among the three models vary depending on the domain and there's no clear winner. Combining all of these losses (+all) however, produces the best squad performance for all models across most domains. The average recovery (+all- finetune) of squad performance is 4.54, 3.93 and 8.77 F1 points for QANet, decaNLP and BERT respectively, implying that BERT benefits from these auxiliary penalties more than decaNLP and QANet.
> 
> When compared to gem, +all preserves squad performance substantially better, on average 2.86 points more for QANet and 5.57 points more BERT. For decaNLP, the improvement is minute (0.02); generally gem has the upper hand for most domains but the advantage is cancelled out by its poor performance

#### Relevance 814

Label: 

#### Passage 815

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> To reduce catastrophic forgetting when adapting comprehension models, we explore several auxiliary penalty terms to regularise the fine-tuning process. We experiment with selective and non-selective penalties, and found that a combination of them consistently produces the best recovery for the source domain without harming its performance in the target domain. We also found similar observations when we apply our approach for adaptation to other tasks, demonstrating its general applicability. To test our approach, we develop and release six narrow domain reading comprehension data sets for the research community.

#### Relevance 815

Label: 

### BM25

#### Passage 808

Retrieved by: BM25

> In decaNLP, curriculum learning was used to train models for different NLP tasks. More specifically, decaNLP was first pre-trained on squad and then fine-tuned on 10 tasks (including squad) jointly. During the training process, each minibatch consists of examples from a particular task, and they are sampled in an alternating fashion among different tasks.
> 
> In situations where we do not have access to training data from previous tasks, catastrophic forgetting occurs when we adapt the model for a new task. In this section, we test our methods for task transfer (as opposed to domain transfer in previous sections). To this end, we experiment with decaNLP and monitor its squad performance when we fine-tune it for other tasks, including semantic role labelling (SRL), summarisation (SUM), semantic parsing (SP), machine translation (MT), and sentiment analysis (SA). Note that we are not doing joint or continuous learning here: we are taking the pre-trained model (on squad) and adapting it to the new tasks independently. Description of these tasks are detailed in BIBREF11.
> 
> A core novelty of decaNLP is that its design allows it to generate words by extracting them from the question, context or its vocabulary, and this decision is made by the pointer-generator network. Based on the pointer-generator analysis in BIBREF11, we know that the pointer-generator network favours generating words using: (1) context for SRL, SUM, and SP; (2) question for SA; and (3) vocabulary for MT.
> 
> As before, finetune serves as our baseline, and we have 5 variants with auxiliary penalty terms. Table TABREF25 displays the F1 performance on squad and the target task; the table shares the same format as Table TABREF10.
> 
> In terms of target task performance (“Test”), we see similar performances for all models. This is a similar observation we saw in previously, and it shows that the incorporation of the auxiliary penalty terms does not harm target task or domain performance.
> 
> For the source task squad, +all produces substantial recovery for SUM, SRL, SP and SA, but not for MT. We hypothesise that this is due to the difference in nature between the target task and the source task: i.e. for SUM, SRL and SP, the output is generated by selecting words

#### Relevance 808

Label: 

#### Passage 810

Retrieved by: BM25

> We first pre-train QANet and decaNLP on squad, tuning their hyper-parameters based on its development partition. For BERT, we fine-tune the released pre-trained model on squad by adding 2 additional output layers to predict the start/end indices (we made no changes to the hyper-parameters). We initialise word vectors of QANet and decaNLP with pre-trained GloVe embeddings BIBREF27 and keep them fixed during training. We also freeze the input embeddings for BERT. To measure performance, we use the standard macro-averaged F1 as the evaluation metric, which measures the average overlap of word tokens between prediction and ground truth answer. Our pre-trained QANet, decaNLP and BERT achieve an F1 score of 80.47, 75.50 and 87.62 respectively on the development partition of squad. Note that the test partition of squad is not released publicly, and so all reported squad performance in the paper is on the development set.
> 
> Given the pre-trained squad models, we fine-tune them on the msmarco and bioasq domains. We test vanilla fine-tuning (finetune) and 5 variants of fine-tuning with auxiliary penalty terms: (1) EWC (+ewc); normalised EWC (+ewcn); cosine distance (+cd); L2 (+l2); and combined normalised EWC, cosine distance and L2 (+all). As a benchmark, we also perform fine-tuning with gradient episodic memory (gem), noting that this approach uses the first $m$ examples from squad ($m = 256$ in our experiments).
> 
> To find the best hyper-parameter configuration, we tune it based on the development partition for each target domain. For a given domain, finetune and its variants (+ewc, +ewcn, +cd, +l2 and +all) all share the same hyper-parameter configuration. Detailed hyper-parameter settings are given in the supplementary material.
> 
> As a baseline, we train QANet, decaNLP and BERT from scratch (scratch) using the target domain data. As before, we tune their hyper-parameters based on development performance. We present the full results in Table TABREF10.
> 
> For each target domain, we display two F1 scores: the source squad development performance (“squad”); and the target domain's test performance (“Test”). We first compare the performance between scratch and finetune. Across all domains for QANet, decaNLP and BERT, finetune substantially improves the target domain's performance compared to scratch. The largest improvement is seen in bioasq for QANet, where its F1

#### Relevance 810

Label: 

### Dense

#### Passage 813

Retrieved by: Dense

> Observing that the model tends to focus on optimising for the target domain/task in early iterations (as the penalty term has a very small value), we explore using a dynamic $\lambda $ scale that starts at a larger value that decays over time. With just simple linear decay, we found substantial improvement in +ewc for recovering squad's performance, although the results are mixed for other penalties (particularly for +ewcn). We therefore only report results that are based on static $\lambda $ values in this paper. With that said, we contend that this might be an interesting avenue for further research, e.g. by exploring more complex decay functions.
> 
> To validate the assumption made by gem BIBREF20, we conduct gradient analysis for the auxiliary penalty terms. During fine-tuning, at each step $t$, we calculate the gradient cosine similarity $sim(g_t, g_t^{\prime })$, where $g_t=\frac{\partial \mathcal {L}(f_{\theta _t}, M)}{\partial \theta _t}$, $g_t^{\prime }=\frac{\partial \mathcal {L}(f_{\theta _t}, (x, y))}{\partial \theta _t}$, $M$ is a memory containing squad examples, and $x$/$y$ is training data/label from the current domain. We smooth the scores by averaging over every 1K steps, resulting in 20 cosine similarity values for 20K steps. Figure FIGREF26 plots the gradient cosine similarity for our models in ms -fn.
> 
> Curiously, our best performing model +all produces the lowest cosine similarity at most steps (the only exception is between 0-1K steps). finetune, on the other hand, maintains relatively high similarity throughout. Similar trends are found for other domains. These observations imply that the inspiration gem draw on — i.e. catastrophic forgetting can be reduced by constraining a positive dot product between $g_t$ and $g_t^{\prime }$ — is perhaps not as empirically effective as intuition might tell us, and that our auxiliary penalty methods represent an alternative (and very different) direction to preserving source performance.

#### Relevance 813

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 816

Retrieved by: Hybrid RRF followed by BGE reranking

> We first pre-train a general domain RC model on squad, our source domain. Given the pre-trained model, we then perform fine-tuning (finetune) on the msmarco and bioasq data sets: 7 target domains in total. By fine-tuning we mean taking the pre-trained model parameters as initial parameters and update them accordingly based on data from the new domain. To reduce forgetting on the source domain (squad), we experiment with incorporating auxiliary penalty terms (e.g. L2 between new and old parameters) to the standard cross entropy loss to regularise the fine-tuning process.
> 
> We explore 3 modern RC models in our experiments: QANet BIBREF10; decaNLP BIBREF11; and BERT BIBREF12. QANet is a Transformer-based BIBREF26 comprehension model, where the encoder consists of stacked convolution and self-attention layers. The objective of the model is to predict the position of the starting and ending indices of the answer words in the context. decaNLP is a recurrent network-based comprehension model trained on ten NLP tasks simultaneously, all casted as a question-answer problem. Much of decaNLP's flexibility is due to its pointer-generator network, which allows it to generate words by extracting them from the question or context passages, or by drawing them from a vocabulary. BERT is a deep bi-directional encoder model based on Transformers. It is pre-trained on a large corpus in an unsupervised fashion using a masked language model and next-sentence prediction objective. To apply BERT to a specific task, the standard practice is to add additional output layers on top of the pre-trained BERT and fine-tune the whole model for the task. In our case for RC, 2 output layers are added: one for predicting the start index and another the end index. BIBREF12 demonstrates that this transfer learning strategy produces state-of-the-art performance on a range of NLP tasks. For RC specifically, BERT (BERT-Large) achieved an F1 score of 93.2 on squad, outperforming human performance by 2 points.
> 
> Note that BERT and QANet RC models are extractive models (goal is to predict 2 indices), while decaNLP is a generative model (goal is to generate the correct word sequence). Also, unlike QANet and decaNLP, BERT is not designed specifically for RC. It represents a growing trend in the literature where large

#### Relevance 816

Label: 

## Question 0090

Paper: Going Beneath the Surface: Evaluating Image Captioning for Grammaticality, Truthfulness and Diversity

> Are the images from a specific domain?

### Common Retrieved Chunks

#### Passage 817

Retrieved by: BM25, Hybrid RRF

> We develop a variety of ShapeWorldICE datasets, with a similar idea to the “skill tasks” in the bAbI framework BIBREF22. Table TABREF4 gives an overview for different ShapeWorldICE datasets we use in this paper. We consider three different types of captioning tasks, each of which focuses on a distinct aspect of reasoning abilities. Existential descriptions examine whether a certain object is present in an image. Spatial descriptions identify spatial relationships among visual objects. Quantification descriptions involve count-based and ratio-based statements, with an explicit focus on inspecting models for their counting ability. We develop two variants for each type of dataset to enable different levels of visual complexity or specific aspects of the same reasoning type. All the training and test captions sampled in this work are in English.
> 
> Each dataset variant consists of around 200k training instances and 4,096 validation instances, plus 4,096 test instances. Each training instance consists of an image and a reference caption. At test time, only the test images are available to the evaluated models. Underlying world models are kept from the models and are used for later GTD evaluation. For each test instance, we sample ten reference captions of the same distribution as the training captions to enable the comparison of our proposed metrics to BLEU and SPICE. We fine-tune our model hyperparameters based on the performance on the validation set. All reported results are measured on the test split with the parameters yielding the best validation performance.

#### Relevance 817

Label: 

#### Passage 818

Retrieved by: BM25, Dense, Hybrid RRF

> using a set of reference captions to approximate the content of an image. We argue that, while existing metrics have undeniably been useful for real-world captioning evaluation, their focus on approximate surface comparison limits deeper insights into the learning process and eventual behavior of captioning models.
> 
> To address this problem, we propose a set of principled evaluation criteria which evaluate image captioning models for grammaticality, truthfulness and diversity (GTD). These criteria correspond to necessary requirements for image captioning systems: (a) that the output is grammatical, (b) that the output statement is true with respect to the image, and (c) that outputs are diverse and mirror the variability of training captions.
> 
> Practical evaluation of GTD is currently only possible on synthetic data. We construct a range of datasets designed for image captioning evaluation. We call this diagnostic evaluation benchmark ShapeWorldICE (ShapeWorld for Image Captioning Evaluation). We illustrate the evaluation of specific image captioning models on ShapeWorldICE. We empirically demonstrate that the existing metrics BLEU and SPICE do not capture true caption-image agreement in all scenarios, while the GTD framework allows a fine-grained investigation of how well existing models cope with varied visual situations and linguistic constructions.
> 
> We believe that as a supplementary evaluation method to real-world metrics, the GTD framework provides evaluation insights that are sufficiently interesting to motivate future work.

#### Relevance 818

Label: 

#### Passage 819

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Automatically generating text to describe the content of images, also known as image captioning, is a multimodal task of considerable interest in both the computer vision and the NLP communities. Image captioning can be framed as a translation task from an image to a descriptive natural language statement. Many existing captioning models BIBREF0, BIBREF1, BIBREF2, BIBREF3 follow the typical encoder-decoder framework where a convolutional network is used to condense images into visual feature representations, combined with a recurrent network for language generation. While these models demonstrate promising results, quantifying image captioning performance remains a challenging problem, in a similar way to other generative tasks BIBREF4, BIBREF5.
> 
> Evaluating candidate captions for human preference is slow and laborious. To alleviate this problem, many automatic evaluation metrics have been proposed, such as BLEU BIBREF6, METEOR BIBREF7, ROUGE BIBREF8 and CIDEr BIBREF9. These n-gram-based metrics evaluate captioning performance based on surface similarity between a candidate caption and reference statements. A more recent evaluation metric for image captioning is SPICE BIBREF10, which takes into account semantic propositional content of generated captions by scoring a caption based upon a graph-based semantic representation transformed from reference captions.
> 
> The rationale behind these evaluation metrics is that human reference captions serve as an approximate target and comparing model outputs to this target is a proxy for how well a system performs. Thus, a candidate caption is not directly evaluated with respect to image content, but compared to a set of human statements about that image.
> 
> However, in image captioning, visual scenes with multiple objects and relations correspond to a diversity of valid descriptions. Consider the example image and captions from the ShapeWorld framework BIBREF11 shown in Figure FIGREF1. The first three captions are true statements about the image and express relevant ideas, but describe different objects, attributes and spatial relationships, while the fourth caption is wrong despite referring to the same objects as in the third caption. This casts doubt on the sufficiency of using a set of reference captions to approximate the content of an image. We argue that, while existing metrics have undeniably been useful for real-world captioning evaluation, their focus on approximate surface comparison limits deeper insights into the learning process

#### Relevance 819

Label: 

#### Passage 820

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> While grammaticality and truthfulness are essential requirements for image captions, these criteria alone can easily be “gamed” by specializing on a small set of generic statements which are true most of the time. In the context of abstract shapes, such captions include examples like “There is a shape” or “At least zero shapes are blue” (which is technically true even if there is no blue shape). This motivates the third fundamental requirement of captioning output to be diverse.
> 
> As ShapeWorldICE exploits a limited size of open-class words, we emphasize the diversity in ShapeWorldICE at the sentence level rather than the word level. Since the ground-truth reference captions in ShapeWorld are randomly sampled, we take the sampled captions accompanying the test images as a proxy for optimal caption diversity, and compare it with the empirical output diversity of the evaluated model on these test images. Practically, we look at language constructions used and compute the corresponding diversity score as the ratio of observed number versus optimal number:
> 
> Language constructions here correspond to reduced caption representations which only record whether an object is described by shape (e.g., “square”), color (e.g., “red shape”) or color-shape combination (e.g., “red square”). So the statement “A square is red” and “A circle is blue” are considered the same, while “A shape is red” is different.

#### Relevance 820

Label: 

#### Passage 822

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> An essential criterion for an image captioning model is that the captions generated are grammatically well-formed. Fully accurate assessment of grammaticality in a general context is itself a difficult task, but becomes more feasible in a very constrained context like our diagnostic language data. We take parseability with the English Resource Grammar BIBREF23 as a surrogate for grammaticality, meaning that a sentence is considered grammatically well-formed if we obtain a parse using the ERG.
> 
> The ERG is a broad-coverage grammar based on the head-driven phrase structure grammar (HPSG) framework. It is linguistically precise: sentences only parse if they are valid according to its hand-built rules. It is designed to be general-purpose: verified coverage is around 80% for Wikipedia, and over 90% for corpora with shorter sentences and more limited vocabulary (for details see BIBREF24 flickinger2011accuracy). Since the ShapeWorld training data – the only language source for models to learn from – is generated using the same grammar, the ERG has $\sim $100% coverage of grammaticality in the model output space.

#### Relevance 822

Label: 

### BM25

#### Passage 821

Retrieved by: BM25

> In the following we introduce GTD in more detail, consider it as an evaluation protocol covering necessary aspects of the multifaceted captioning task, rather than a specific metric.

#### Relevance 821

Label: 

### Dense

#### Passage 823

Retrieved by: Dense

> The second aspect we investigate is truthfulness, that is, whether a candidate caption is compatible with the content of the image it is supposed to describe. We evaluate caption truthfulness on the basis of a linguistically-motivated approach using formal semantics. We convert the output of the ERG parse for a grammatical caption to a Dependency Minimal Recursion Semantics (DMRS) graph using the pydmrs tool BIBREF25. Each converted DMRS is a logical semantic graph representation corresponding to the caption. We construct a logical proposition from the DMRS graph, and evaluate it against the actual world model of the corresponding image. A caption can be said to agree with an image only if the proposition evaluates as true on the basis of the world model. By examining the logical agreement between a caption representation and a world model, we can check whether the semantics of this caption agrees with the visual content which the world model represents. Thus we do not rely on a set of captions as a surrogate for the content of an image, but instead leverage the fact that we have the ground truth, thus enabling the evaluation of true image-caption agreement.

#### Relevance 823

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 824

Retrieved by: Hybrid RRF followed by BGE reranking

> Recently, many synthetic datasets have been proposed as diagnostic tools for deep learning models, such as CLEVR BIBREF21 for visual question answering (VQA), the bAbI tasks BIBREF22 for text understanding and reasoning, and ShapeWorld BIBREF11 for visually grounded language understanding. The primary motivation is to reduce complexity which is considered irrelevant to the evaluation focus, to enable better control over the data, and to provide more detailed insights into strengths and limitations of existing models.
> 
> In this work, we develop the evaluation datasets within the ShapeWorld framework. ShapeWorld is a controlled data generation framework consisting of abstract colored shapes (see Figure FIGREF1 for an example). We use ShapeWorld to generate training and evaluation data for two major reasons. ShapeWorld supports customized data generation according to user specification, which enables a variety of model inspections in terms of language construction, visual complexity and reasoning ability. Another benefit is that each training and test instance generated in ShapeWorld is returned as a triplet of $<$image, caption, world model$>$. The world model stores information about the underlying microworld used to generate an image and a descriptive caption, internally represented as a list of entities with their attributes, such as shape, color, position. During data generation, ShapeWorld randomly samples a world model from a set of available entities and attributes. The generated world model is then used to realize a corresponding instance consisting of image and caption. The world model gives the actual semantic information contained in an image, which allows evaluation of caption truthfulness.

#### Relevance 824

Label: 

#### Passage 825

Retrieved by: Hybrid RRF followed by BGE reranking

> scores in fewer than 5,000 iterations, suggesting that the model quickly learns to generate grammatically well-formed sentences.
> 
> Failure to learn complex spatial relationships. While CNNs can produce rich visual representations that can be used for a variety of vision tasks BIBREF27, it remains an open question whether these condensed visual representations are rich enough for multimodal tasks that require higher-level abilities of scene understanding and visual reasoning. From Figure FIGREF16, we can see that while the model performs rather well on Existential datasets, it exhibits a worse performance on Spatial data. The caption agreement ratio in the simple Spatial-TwoShapes scenario is relatively high, but drops significantly on Spatial-MultiShapes, demonstrating the deficiencies of the model in learning spatial relationships from complex visual scenes.
> 
> The counting task is non-trivial. Counting has long been considered to be a challenging task in multimodal reasoning BIBREF28, BIBREF29. To explore how well the LRCN1u model copes with counting tasks, we generated two Quantification datasets. The Quant-Count captions describe the number of objects with certain attributes that appear in an image (e.g. “Exactly four shapes are crosses”), while the Quant-Ratio captions describe the ratio of certain objects (e.g. “A third of the shapes are blue squares”).
> 
> From Figure FIGREF16, we notice that the LRCN1u model performs poorly on these datasets in terms of truthfulness, reflected in the 0.50 and 0.46 scores achieved by the model on the Quant-Count and Quant-Ratio tasks respectively. The learning curve for Quant-Ratio exhibits a more gradual rise as the training progresses, suggesting a greater complexity for the ratio-based task.
> 
> Caption diversity benefits from varied language constructions in the training data. The diversity ratios of generated captions for different ShapeWorldICE datasets are illustrated in Figure FIGREF17. We can see that the diversity of inferred captions is largely sensitive to the caption variability in the dataset itself. For simple datasets (such as Existential-OneShape) where language constructions in the training set are less diverse, the output captions tend to have uniform sentence structures. The high diversity ratios of generated Spatial and Quantification captions suggest that caption diversity benefits from heterogeneous language constructions in complex datasets.

#### Relevance 825

Label: 

## Question 0091

Paper: Character n-gram Embeddings to Improve RNN Language Models

> Which dataset do they evaluate on for headline generation?

### Common Retrieved Chunks

#### Passage 826

Retrieved by: BM25, Hybrid RRF

> Neural language models have played a crucial role in recent advances of neural network based methods in natural language processing (NLP). For example, neural encoder-decoder models, which are becoming the de facto standard for various natural language generation tasks including machine translation BIBREF1 , summarization BIBREF2 , dialogue BIBREF3 , and caption generation BIBREF4 can be interpreted as conditional neural language models. Moreover, neural language models can be used for rescoring outputs from traditional methods, and they significantly improve the performance of automatic speech recognition BIBREF5 . This implies that better neural language models improve the performance of application tasks.
> 
> In general, neural language models require word embeddings as an input BIBREF6 . However, as described by BIBREF7 , this approach cannot make use of the internal structure of words although the internal structure is often an effective clue for considering the meaning of a word. For example, we can comprehend that the word `causal' is related to `cause' immediately because both words include the same character sequence `caus'. Thus, if we incorporate a method that handles the internal structure such as character information, we can improve the quality of neural language models and probably make them robust to infrequent words.
> 
> To incorporate the internal structure, BIBREF7 concatenated character embeddings with an input word embedding. They demonstrated that incorporating character embeddings improved the performance of RNN language models. Moreover, BIBREF8 and BIBREF9 applied Convolutional Neural Networks (CNN) to construct word embeddings from character embeddings.
> 
> On the other hand, in the field of word embedding construction, some previous researchers found that character INLINEFORM0 -grams are more useful than single characters BIBREF0 , BIBREF10 . In particular, BIBREF0 demonstrated that constructing word embeddings from character INLINEFORM1 -gram embeddings outperformed the methods that construct word embeddings from character embeddings by using CNN or a Long Short-Term Memory (LSTM).
> 
> Based on their reports, in this paper, we propose a neural language model that utilizes character INLINEFORM0 -gram embeddings. Our proposed method encodes character INLINEFORM1 -gram embeddings to a word embedding with simplified Multi-dimensional Self-attention (MS) BIBREF11 . We refer to this constructed embedding as char INLINEFORM2 -MS-vec. The proposed method regards char INLINEFORM3 -MS-vec as an input in addition

#### Relevance 826

Label: 

#### Passage 827

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We used the standard benchmark datasets for the word-level language modeling: Penn Treebank (PTB) BIBREF16 , WikiText-2 (WT2), and WikiText-103 (WT103) BIBREF17 . BIBREF18 and BIBREF17 published pre-processed PTB, WT2, and WT103. Following the previous studies, we used these pre-processed datasets for our experiments.
> 
> Table TABREF14 describes the statistics of the datasets. Table TABREF14 demonstrates that the vocabulary size of WT103 is too large, and thus it is impractical to compute char INLINEFORM0 -MS-vec for all words at every step. Therefore, we did not use INLINEFORM1 for word tying. In other words, we used only word embeddings INLINEFORM2 as the weight matrix INLINEFORM3 in WT103.
> 
> For machine translation, we used two kinds of language pairs: English-French and English-German sentences in the IWSLT 2016 dataset. The dataset contains about 208K English-French pairs and 189K English-German pairs. We conducted four translation tasks: from English to each language (En-Fr and En-De), and their reverses (Fr-En and De-En).
> 
> For headline generation, we used sentence-headline pairs extracted from the annotated English Gigaword corpus BIBREF35 in the same manner as BIBREF2 . The training set contains about 3.8M sentence-headline pairs. For evaluation, we exclude the test set constructed by BIBREF2 because it contains some invalid instances, as reported in BIBREF33 . We instead used the test sets constructed by BIBREF33 and BIBREF34 .

#### Relevance 827

Label: 

#### Passage 828

Retrieved by: BM25, Dense, Hybrid RRF

> BIBREF14 and BIBREF15 proposed a word tying method (WT) that shares the word embedding matrix ( INLINEFORM0 in Equation ) with the weight matrix to compute probability distributions ( INLINEFORM1 in Equation EQREF3 ). They demonstrated that WT significantly improves the performance of RNN language models.
> 
> In this study, we adopt char INLINEFORM0 -MS-vec as the weight matrix in language modeling. Concretely, we use INLINEFORM1 instead of INLINEFORM2 in Equation EQREF3 , where INLINEFORM3 contains char INLINEFORM4 -MS-vec for all words in the vocabulary.

#### Relevance 828

Label: 

#### Passage 830

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> proposed method encodes character INLINEFORM1 -gram embeddings to a word embedding with simplified Multi-dimensional Self-attention (MS) BIBREF11 . We refer to this constructed embedding as char INLINEFORM2 -MS-vec. The proposed method regards char INLINEFORM3 -MS-vec as an input in addition to a word embedding.
> 
> We conduct experiments on the well-known benchmark datasets: Penn Treebank, WikiText-2, and WikiText-103. Our experiments indicate that the proposed method outperforms neural language models trained with well-tuned hyperparameters and achieves state-of-the-art scores on each dataset. In addition, we incorporate our proposed method into a standard neural encoder-decoder model and investigate its effect on machine translation and headline generation. We indicate that the proposed method also has a positive effect on such tasks.

#### Relevance 830

Label: 

#### Passage 831

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We employed the neural encoder-decoder with attention mechanism described in BIBREF34 as the base model. Its encoder consists of a 2-layer bidirectional LSTM and its decoder consists of a 2-layer LSTM with attention mechanism proposed by BIBREF36 . We refer to this neural encoder-decoder as EncDec. To investigate the effect of the proposed method, we introduced char3-MS-vec into EncDec. Here, we applied char3-MS-vec to both the encoder and decoder. Moreover, we did not apply word tying technique to EncDec because it is default setting in the widely-used encoder-decoder implementation.
> 
> We set the embedding size and dimension of the LSTM hidden state to 500 for machine translation and 400 for headline generation. The mini-batch size is 64 for machine translation and 256 for headline generation. For other hyperparameters, we followed the configurations described in BIBREF34 . We constructed the vocabulary set by using Byte-Pair-Encoding (BPE) BIBREF37 because BPE is a currently widely-used technique for vocabulary construction. We set the number of BPE merge operations to 16K for machine translation and 5K for headline generation.

#### Relevance 831

Label: 

### BM25

#### Passage 829

Retrieved by: BM25

> Table TABREF15 shows perplexities of the baselines and the proposed method. We varied INLINEFORM0 for char INLINEFORM1 -MS-vec from 2 to 4. For the baseline, we also applied two word embeddings to investigate the performance in the case where we use more kinds of word embeddings. In detail, we prepared INLINEFORM2 and used INLINEFORM3 instead of INLINEFORM4 in Equation . Table TABREF15 also shows the number of character INLINEFORM5 -grams in each dataset. This table indicates that char INLINEFORM6 -MS-vec improved the performance of state-of-the-art models except for char4-MS-vec on WT103. These results indicate that char INLINEFORM7 -MS-vec can raise the quality of word-level language models. In particular, Table TABREF15 shows that char3-MS-vec achieved the best scores consistently. In contrast, an additional word embedding did not improve the performance. This fact implies that the improvement of char INLINEFORM8 -MS-vec is caused by using character INLINEFORM9 -grams. Thus, we answer yes to the first research question.
> 
> Table TABREF16 shows the training time spent on each epoch. We calculated it on the NVIDIA Tesla P100. Table TABREF16 indicates that the proposed method requires more computational time than the baseline unfortunately. We leave exploring a faster structure for our future work.
> 
> Table TABREF17 shows perplexities on the PTB dataset where the frequency of an input word is lower than 2,000 in the training data. This table indicates that the proposed method can improve the performance even if an input word is infrequent. In other words, char INLINEFORM0 -MS-vec helps represent the meanings of infrequent words. Therefore, we answer yes to the second research question in the case of our experimental settings.
> 
> We explored the effectiveness of multi-dimensional self-attention for word embedding construction. Table TABREF24 shows perplexities of using several encoders on the PTB dataset. As in BIBREF8 , we applied CNN to construct word embeddings (charCNN in Table TABREF24 ). Moreover, we applied the summation and standard self-attention, which computes the scalar value as a weight for a character INLINEFORM0 -gram embedding, to construct word embeddings (char INLINEFORM1 -Sum-vec and char INLINEFORM2 -SS-vec, respectively). For CNN, we used hyperparameters identical to BIBREF8 (“Original Settings” in Table TABREF24 ) but the setting has two differences from other architectures: 1.

#### Relevance 829

Label: 

### Dense

#### Passage 832

Retrieved by: Dense

> In this paper, we incorporated character information with RNN language models. Based on the research in the field of word embedding construction BIBREF0 , we focused on character INLINEFORM0 -gram embeddings to construct word embeddings. We used multi-dimensional self-attention BIBREF11 to encode character INLINEFORM1 -gram embeddings. Our proposed char INLINEFORM2 -MS-vec improved the performance of state-of-the-art RNN language models and achieved the best perplexities on Penn Treebank, WikiText-2, and WikiText-103. Moreover, we investigated the effect of char INLINEFORM3 -MS-vec on application tasks, specifically, machine translation and headline generation. Our experiments show that char INLINEFORM4 -MS-vec also improved the performance of a neural encoder-decoder on both tasks.

#### Relevance 832

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 833

Retrieved by: Hybrid RRF followed by BGE reranking

> word embeddings INLINEFORM2 ” in Table TABREF24 . Table TABREF24 shows cahr3-MS-vec and char4-MS-vec are superior to char2-MS-vec. In the view of perplexity, char3-MS-vec and char4-MS-vec achieved comparable scores to each other. On the other hand, char3-MS-vec is composed of much smaller parameters. Furthermore, we decreased the embedding size INLINEFORM3 to adjust the number of parameters to the same size as the baseline (“Same #Params as baseline” in Table TABREF24 ). In this setting, char3-MS-vec achieved the best perplexity. Therefore, we consider that char3-MS-vec is more useful than char4-MS-vec, which is the answer to the fourth research question. We use the combination of the char3-MS-vec INLINEFORM4 and word embedding INLINEFORM5 in the following experiments.
> 
> Finally, we compare the proposed method with the published scores reported in previous studies. Tables TABREF25 , TABREF26 , and TABREF27 , respectively, show perplexities of the proposed method and previous studies on PTB, WT2, and WT103. Since AWD-LSTM-MoS BIBREF28 and AWD-LSTM-DOC BIBREF29 achieved the state-of-the-art scores on PTB and WT2, we combined char3-MS-vec with them. These tables show that the proposed method improved the performance of the base model and outperformed the state-of-the-art scores on all datasets. In particular, char3-MS-vec improved perplexity by at least 1 point from current best scores on the WT103 dataset.
> 
> Tables TABREF31 and TABREF32 show the results of machine translation and headline generation, respectively. These tables show that EncDec+char3-MS-vec outperformed EncDec in all test data. In other words, these results indicate that our proposed method also has a positive effect on the neural encoder-decoder model. Moreover, it is noteworthy that char3-MS-vec improved the performance of EncDec even though the vocabulary set constructed by BPE contains subwords. This implies that character INLINEFORM0 -gram embeddings improve the quality of not only word embeddings but also subword embeddings.
> 
> In addition to the results of our implementations, the lower portion of Table TABREF32 contains results reported in previous studies. Table TABREF32 shows that EncDec+char3-MS-vec also outperformed the methods proposed in previous studies. Therefore, EncDec+char3-MS-vec achieved the top scores in the test sets constructed by BIBREF33 and BIBREF34 even though it does not have a task-specific architecture such as the selective gate proposed by BIBREF33 .
> 
> In these experiments, we

#### Relevance 833

Label: 

#### Passage 834

Retrieved by: Hybrid RRF followed by BGE reranking

> As described in Section SECREF1 , neural encoder-decoder models can be interpreted as conditional neural language models. Therefore, to investigate if the proposed method contributes to encoder-decoder models, we conduct experiments on machine translation and headline generation tasks.

#### Relevance 834

Label: 

## Question 0092

Paper: Shallow reading with Deep Learning: Predicting popularity of online content using only its title

> What evaluation metrics are used?

### Common Retrieved Chunks

#### Passage 835

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this section, we evaluate our method and compare its performance against the competitive approaches. We use INLINEFORM0 -fold evaluation protocol with INLINEFORM1 with random dataset split. We measure the performance using standard accuracy metric which we define as a ratio between correctly classified data samples from test dataset and all test samples.

#### Relevance 835

Label: 

#### Passage 836

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> In this paper we present a novel approach to the problem of online article popularity prediction. To our knowledge, this is the first attempt of predicting the performance of content on social media using only textual information from its title. We show that our method consistently outperforms benchmark models. Additionally, the proposed method could not only be used to compare competing titles with regard to their estimated probability, but also to gain insights about what constitutes a good title. Future work includes modeling popularity prediction problem with multiple data modalities, such as images or videos. Furthermore, all of the evaluated models function at the word level, which could be problematic due to idiosyncratic nature of social media and Internet content. It is, therefore, worth investigating, whether combining models that operate at the character level to learn and generate vector representation of titles with visual features could improve the overall performance.

#### Relevance 836

Label: 

#### Passage 837

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We cast the problem of popularity prediction as a binary classification task. We assume our data points contain a string of characters representing article title and a popularity metric, such as number of comments or views. The input of our classification is the character string, while the output is the binary label corresponding to popular or unpopular class. To enable the comparison of the methods on datasets containing content published on different websites and with different audience sizes, we determine that a video is popular if its popularity metric exceeds the median value of the corresponding metric for other points in the set, otherwise - it is labeled as unpopular. The details of the labeling procedure are discussed separately in the Datasets section.

#### Relevance 837

Label: 

#### Passage 838

Retrieved by: BM25, Hybrid RRF

> Our method for popularity prediction using article's title is inspired by a bidirectional LSTM architecture. The overview of the model can be seen in Fig. FIGREF8 .
> 
> Let INLINEFORM0 be INLINEFORM1 -dimensional word vector corresponding to the INLINEFORM2 -the word in the headline, then a variable length sequence: INLINEFORM3 represents a headline. A recurrent neural network (RNN) processes this sequence by recursively applying a transformation function to the current element of sequence INLINEFORM4 and its previous hidden internal state INLINEFORM5 (optionally outputting INLINEFORM6 ). At each time step INLINEFORM7 , the hidden state is updated by: DISPLAYFORM0
> 
> where INLINEFORM0 is a non-linear activation function. LSTM network BIBREF17 updates its internal state differently, at each step INLINEFORM1 it calculates: DISPLAYFORM0
> 
> where INLINEFORM0 is the sigmoid activation function, tanh is the hyperbolic tangent function and INLINEFORM1 denotes component-wise multiplication. In our experiments we used 128, 256 for the dimensionality of hidden layer in both LSTM and BiLSTM. The term in equation EQREF10 INLINEFORM2 , is called the input gate and it uses the input word and the past hidden state to determine whether the input is worth remembering or not. The amount of information that is being discarded is controlled by forget gate INLINEFORM3 , while INLINEFORM4 is the output gate that controls the amount of information that leaks from memory cell INLINEFORM5 to the hidden state INLINEFORM6 . In the context of classification, we typically treat the output of the hidden state at the last time step of LSTM as the document representation and feed it to sigmoid layer to perform classification BIBREF18 .
> 
> Due to its sequential nature, a recurrent neural network puts more emphasis on the recent elements. To circumvent this problem BIBREF19 introduced a bidirectional RNN in which each training sequence is presented forwards and backwards to two separate recurrent nets, both of which are connected to the same output layer. Therefore, at any time-step we have the whole information about the sequence. This is shown by the following equation: DISPLAYFORM0
> 
> In our method, we use the bidirectional LSTM architecture for content popularity prediction using only textual cues. We have to therefore map the neural network outputs from a set of hidden states

#### Relevance 838

Label: 

#### Passage 840

Retrieved by: Dense, Hybrid RRF

> In this section we present two datasets used in our experiments: The NowThisNews dataset, collected for the purpose of this paper, and The BreakingNews dataset BIBREF4 , publicly available dataset of news articles.
> 
> contains 4090 posts with associated videos from NowThisNews Facebook page collected between 07/2015 and 07/2016. For each post we collected its title and the number of views of the corresponding video, which we consider our popularity metric. Due to a fairly lengthy data collection process, we decided to normalize our data by first grouping posts according to their publication month and then labeling the posts for which the popularity metric exceeds the median monthly value as popular, the remaining part as unpopular.
> 
> BIBREF4 contains a variety of news-related information such as images, captions, geo-location information and comments which could be used as a proxy for article popularity. The articles in this dataset were collected between January and December 2014. Although we tried to retrieve the entire dataset, we were able to download only 38,182 articles due to the dead links published in the dataset. The retrieved articles were published in main news channels, such as Yahoo News, The Guardian or The Washington Post. Similarly, to The NowThisNews dataset we normalize the data by grouping articles per publisher, and classifying them as popular, when the number of comments exceeds the median value for given publisher.

#### Relevance 840

Label: 

#### Passage 841

Retrieved by: Dense, Hybrid RRF

> The results of our experiments can be seen in Tab. TABREF21 and TABREF22 . Our proposed BiLSTM approach outperforms the competing methods consistently across both datasets. The performance improvement is especially visible for The NowThisNews dataset and reaches over 15% with respect to the shallow architecture in terms of of accuracy. Although the improvement with respect to the other methods based on deep neural network is less evident, the recurrent nature of our method provides much more intuitive interpretation of the results and allow for parsing the contribution of each single word to the overall score.
> 
> To present how our model works in practice, we show in Tab. TABREF23 a list of 3 headlines from NowThisNews dataset that are scored with the highest probability of belonging to a popular class, as well as 3 headlines with the lowest score. As can be seen, our model correctly detected videos that become viral at the same time assigning low score to content that underperformed. We believe that BiLSTM could be successfully applied in real-life scenarios.

#### Relevance 841

Label: 

#### Passage 842

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> As a text embedding in our experiments, we use publicly available GloVe word vectors BIBREF16 pre-trained on two datasets: Wikipedia 2014 with Gigaword5 (W+G5) and Common Crawl (CC). Since their output dimensionality can be modified, we show the results for varying dimensionality sizes. On top of that, we evaluate two training approaches: using static word vectors and fine-tuning them during training phase.

#### Relevance 842

Label: 

### BM25

#### Passage 839

Retrieved by: BM25

> As a first baseline we use Bag-of-Words, a well-known and robust text representations used in various domains BIBREF21 , combined with a standard shallow classifier, namely, a Support Vector Machine with linear kernel. We used LIBSVM implementation of SVM.
> 
> Our second baseline is a deep Convectional Neural Network applied on word embeddings. This baseline represents state-of-the-art method presented in BIBREF4 with minor adjustments to the binary classification task. The architecture of the CNN benchmark we use is the following: the embedding layer transforms one-hot encoded words to their dense vector representations, followed by the convolution layer of 256 filters with width equal to 5 followed by max pooling layer (repeated three times), fully-connected layer with dropout and INLINEFORM0 regularization and finally, sigmoid activation layer. For fair comparison, both baselines were trained using the same training procedure as our method.

#### Relevance 839

Label: 

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 843

Retrieved by: Hybrid RRF followed by BGE reranking

> In our experiments we minimize the binary cross-entropy loss using Stochastic Gradient Descent on randomly shuffled mini-batches with the Adam optimization algorithm BIBREF20 . We reduce the learning rate by a factor of 0.2 once learning plateaus. We also employ early stopping strategy, i.e. stopping the training algorithm before convergence based on the values of loss function on the validation set.

#### Relevance 843

Label: 

## Question 0093

Paper: Neural Joking Machine : Humorous image captioning

> How big is the self-collected corpus?

### Common Retrieved Chunks

#### Passage 844

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We are currently posting funny captions generated by the NJM to the Bokete Ogiri website in order to evaluate the proposed method. Here, we compare the proposed method with STAIR captions. As reported by Bokete users, the funny captions generated by STAIR caption averaged 1.71 stars, whereas the NJM averaged 3.23 stars. Thus, the NJM is funnier than the baseline STAIR caption according to Bokete users. We believe that this difference is the result of using (i) Funny Score to effectively train the generator regarding funny captions and (ii) the self-collected BoketeDB, which is a large-scale database for funny captions.

#### Relevance 844

Label: 

#### Passage 846

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We have downloaded pairs of images and funny captions in order to construct a Bokete Database (BoketeDB). As of March 2018, 60M funny captions and 3.4M images have been posted on the Bokete Ogiri website. In the present study, we consider 999,571 funny captions for 70,981 images. A number of pair between image and funny caption is posted in temporal order on the Ogiri website Bokete. We collected images and funny captions to make corresponding image and caption pairs. Thus, we obtained a database for generating funny captions like an image caption one.
> 
> Comparison with MS COCO BIBREF5 . MS COCO contains a correspondence for each of 160,000 images to one of five types of captions. In comparison with MS COCO, BoketeDB has approximately half the number of the images and 124% the number of captions.

#### Relevance 846

Label: 

#### Passage 847

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The Bokete Ogiri website uses the number of stars to evaluate the degree of funniness of a caption. The user evaluates the “funniness” of a posted caption and assigns one to three stars to the caption. Therefore, funnier captions tend to be assigned a lot of stars. We focus on the number of stars in order to propose an effective training method, in which the Funny Score enables us to evaluate the funniness of a caption. Based on the results of our pre-experiment, a Funny Score of 100 stars is treated as a threshold. In other words, the Funny Score outputs a loss value INLINEFORM0 when #star is less than 100. In contrast, the Funny Score returns INLINEFORM1 when #star is over 100. The loss value INLINEFORM2 is calculated with the LSTM as an average of each mini-batch.

#### Relevance 847

Label: 

#### Passage 848

Retrieved by: BM25, Hybrid RRF

> Laughter is a special, higher-order function that only humans possess. In the analysis of laughter, as Wikipedia says, “Laughter is thought to be a shift of composition (schema)", and laughter frequently occurs when there is a change from a composition of receiver. However, the viewpoint of laughter differs greatly depending on the position of the receiver. Therefore, the quantitative measurement of laughter is very difficult. Image Ogiri on web services such as "Bokete" BIBREF0 have recently appeared, where users post funny captions for thematic images and the captions are evaluated in an SNS-like environment. Users compete to obtain the greatest number of “stars”. Although quantification of laughter is considered to be a very difficult task, the correspondence between evaluations and images on Bokete allows us to treat laughter quantitatively. Image captioning is an active topic in computer vision, and we believe that humorous image captioning can be realized. The main contributions of the present paper are as follows:
> 
> BoketeDB
> 
> In the experimental section, we compare the proposed method based on Funny Score and BoketeDB pre-trained parameters with a baseline provided by MS COCO Pre-trained CNN+LSTM. We also compare the results of the NJM with funny captions provided by humans. In an evaluation by humans, the results provided by the proposed method were ranked lower than those provided by humans (22.59% vs. 67.99%) but were ranked higher than the baseline (9.41%). Finally, we show the generated funny captions for several images.

#### Relevance 848

Label: 

#### Passage 849

Retrieved by: Dense, Hybrid RRF

> In this subsection, we present the experimental results along with a discussion. Table TABREF10 shows the experimental results of the questionnaire. A total of 16 personal questionnaires were completed. Table TABREF10 shows the percentages of captions of each rank for each method of caption generation considered herein. Captions generated by humans were ranked “funniest” 67.99% of the time, followed by the NJM at 22.59%. The baseline captions, STAIR caption, were ranked “funniest” 9.41% of the time. These results suggest that captions generated by the NJM are less funny than those generated by humans. However, the NJM is ranked much higher than STAIR caption.

#### Relevance 849

Label: 

### BM25

#### Passage 845

Retrieved by: BM25

> The flow of the proposed method is shown in Figure FIGREF2 . Basically, we adopted the CNN+LSTM model used in Show and Tell, but the CNN is replaced by ResNet-152 as an image feature extraction method. In the next subsection, we describe in detail how to calculate a loss function with a Funny Score. The function appropriately evaluates the number of stars and its “funniness”.

#### Relevance 845

Label: 

### Dense

#### Passage 850

Retrieved by: Dense

> Here, we describe the experimental method used to validate the effectiveness of the NJM. We compare the proposed method with two other methods of generating funny captions: 1) human generated captions, which are highly ranked on Bokete (indicated by “Human" in Table TABREF10 ), and 2) Japanese image caption generation using CNN+LSTM pre-trained by STAIR caption BIBREF7 . Based on the captions provided by MS COCO, the STAIR caption is translated from English to Japanese (indicated by “STAIR caption” in Table TABREF10 ). We use a questionnaire as the evaluation method. We selected a total of 30 themes from the Bokete Ogiri website that included “people”, “two or more people”, “animals”, “landscape”, “inorganics”, and “illustrations”. The questionnaire asks respondents to rank the captions provided by humans, the NJM, and STAIR caption in order of “funniness”. The questionnaire does not reveal the origins of the captions.

#### Relevance 850

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 851

Retrieved by: Hybrid RRF followed by BGE reranking

> In the present paper, we proposed a method by which to generate captions that draw laughter. We built the BoketeDB, which contains pairs comprising a theme (image) and a corresponding funny caption (text) posted on the Bokete Ogiri website. We effectively trained a funny caption generator with the proposed Funny Score by weight evaluation. Although we adopted CNN+LSTM as a baseline, we have been exploring an effective scoring function and database construction. The experiments of the present study suggested that the NJM was much funnier than the baseline STAIR caption.

#### Relevance 851

Label: 

#### Passage 852

Retrieved by: Hybrid RRF followed by BGE reranking

> Finally, we present the visual results in Figure FIGREF14 , which includes examples of funny captions obtained using NJM. Although the original caption is in Japanese, we also translated the captions into English. Enjoy!

#### Relevance 852

Label: 

## Question 0094

Paper: FacTweet: Profiling Fake News Twitter Accounts

> How is a "chunk of posts" defined in this work?

### Common Retrieved Chunks

#### Passage 853

Retrieved by: BM25, Hybrid RRF

> they obtain a result near to the majority class ($0.18$). Another finding from our experiments shows that the performance of the Tweet2vec is weak. This demonstrates that tweets' hashtags are not informative to detect non-factual accounts. In Table TABREF25, we present ablation tests so as to quantify the contribution of subset of features. The results indicate that most performance gains come from words embeddings, style, and morality features. Other features (emotion and sentiment) show lower importance: nevertheless, they still improve the overall system performance (on average 0.35% Macro-F$_1$ improvement). These performance figures suggest that non-factual accounts use semantic and stylistic hidden signatures mostly while tweeting news, so as to be able to mislead the readers and behave as reputable (i.e., factual) sources. We leave a more fine-grained, diachronic analysis of semantic and stylistic features – how semantic and stylistic signature evolve across time and change across the accounts' timelines – for future work.

#### Relevance 853

Label: 

#### Passage 854

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Social media platforms have made the spreading of fake news easier, faster as well as able to reach a wider audience. Social media offer another feature which is the anonymity for the authors, and this opens the door to many suspicious individuals or organizations to utilize these platforms. Recently, there has been an increased number of spreading fake news and rumors over the web and social media BIBREF0. Fake news in social media vary considering the intention to mislead. Some of these news are spread with the intention to be ironic or to deliver the news in an ironic way (satirical news). Others, such as propaganda, hoaxes, and clickbaits, are spread to mislead the audience or to manipulate their opinions. In the case of Twitter, suspicious news annotations should be done on a tweet rather than an account level, since some accounts mix fake with real news. However, these annotations are extremely costly and time consuming – i.e., due to high volume of available tweets Consequently, a first step in this direction, e.g., as a pre-filtering step, can be viewed as the task of detecting fake news at the account level.
> 
> The main obstacle for detecting suspicious Twitter accounts is due to the behavior of mixing some real news with the misleading ones. Consequently, we investigate ways to detect suspicious accounts by considering their tweets in groups (chunks). Our hypothesis is that suspicious accounts have a unique pattern in posting tweet sequences. Since their intention is to mislead, the way they transition from one set of tweets to the next has a hidden signature, biased by their intentions. Therefore, reading these tweets in chunks has the potential to improve the detection of the fake news accounts.
> 
> In this work, we investigate the problem of discriminating between factual and non-factual accounts in Twitter. To this end, we collect a large dataset of tweets using a list of propaganda, hoax and clickbait accounts and compare different versions of sequential chunk-based approaches using a variety of feature sets against several baselines. Several approaches have been proposed for news verification, whether in social media (rumors detection) BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, or in news claims BIBREF5, BIBREF6, BIBREF7, BIBREF8.

#### Relevance 854

Label: 

#### Passage 855

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Given a news Twitter account, we read its tweets from the account's timeline. Then we sort the tweets by the posting date in ascending way and we split them into $N$ chunks. Each chunk consists of a sorted sequence of tweets labeled by the label of its corresponding account. We extract a set of features from each chunk and we feed them into a recurrent neural network to model the sequential flow of the chunks' tweets. We use an attention layer with dropout to attend over the most important tweets in each chunk. Finally, the representation is fed into a softmax layer to produce a probability distribution over the account types and thus predict the factuality of the accounts. Since we have many chunks for each account, the label for an account is obtained by taking the majority class of the account's chunks.
> 
> Input Representation. Let $t$ be a Twitter account that contains $m$ tweets. These tweets are sorted by date and split into a sequence of chunks $ck = \langle ck_1, \ldots , ck_n \rangle $, where each $ck_i$ contains $s$ tweets. Each tweet in $ck_i$ is represented by a vector $v \in {\rm I\!R}^d$ , where $v$ is the concatenation of a set of features' vectors, that is $v = \langle f_1, \ldots , f_n \rangle $. Each feature vector $f_i$ is built by counting the presence of tweet's words in a set of lexical lists. The final representation of the tweet is built by averaging the single word vectors.
> 
> Features. We argue that different kinds of features like the sentiment of the text, morality, and other text-based features are critical to detect the nonfactual Twitter accounts by utilizing their occurrence during reporting the news in an account's timeline. We employ a rich set of features borrowed from previous works in fake news, bias, and rumors detection BIBREF0, BIBREF1, BIBREF8, BIBREF9.
> 
> [leftmargin=4mm]
> 
> Emotion: We build an emotions vector using word occurrences of 15 emotion types from two available emotional lexicons. We use the NRC lexicon BIBREF10, which contains $\sim $14K words labeled using the eight Plutchik's emotions BIBREF11. The other lexicon is SentiSense BIBREF12 which is a concept-based affective lexicon that attaches emotional

#### Relevance 855

Label: 

#### Passage 856

Retrieved by: BM25, Dense, Hybrid RRF

> of sequential chunk-based approaches using a variety of feature sets against several baselines. Several approaches have been proposed for news verification, whether in social media (rumors detection) BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, or in news claims BIBREF5, BIBREF6, BIBREF7, BIBREF8. The main orientation in the previous works is to verify the textual claims/tweets but not their sources. To the best of our knowledge, this is the first work aiming to detect factuality at the account level, and especially from a textual perspective. Our contributions are:
> 
> [leftmargin=4mm]
> 
> We propose an approach to detect non-factual Twitter accounts by treating post streams as a sequence of tweets' chunks. We test several semantic and dictionary-based features together with a neural sequential approach, and apply an ablation test to investigate their contribution.
> 
> We benchmark our approach against other approaches that discard the chronological order of the tweets or read the tweets individually. The results show that our approach produces superior results at detecting non-factual accounts.

#### Relevance 856

Label: 

#### Passage 857

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> Data. We build a dataset of Twitter accounts based on two lists annotated in previous works. For the non-factual accounts, we rely on a list of 180 Twitter accounts from BIBREF1. This list was created based on public resources where suspicious Twitter accounts were annotated with the main fake news types (clickbait, propaganda, satire, and hoax). We discard the satire labeled accounts since their intention is not to mislead or deceive. On the other hand, for the factual accounts, we use a list with another 32 Twitter accounts from BIBREF19 that are considered trustworthy by independent third parties. We discard some accounts that publish news in languages other than English (e.g., Russian or Arabic). Moreover, to ensure the quality of the data, we remove the duplicate, media-based, and link-only tweets. For each account, we collect the maximum amount of tweets allowed by Twitter API. Table TABREF13 presents statistics on our dataset.
> 
> Baselines. We compare our approach (FacTweet) to the following set of baselines:
> 
> [leftmargin=4mm]
> 
> LR + Bag-of-words: We aggregate the tweets of a feed and we use a bag-of-words representation with a logistic regression (LR) classifier.
> 
> Tweet2vec: We use the Bidirectional Gated recurrent neural network model proposed in BIBREF20. We keep the default parameters that were provided with the implementation. To represent the tweets, we use the decoded embedding produced by the model. With this baseline we aim at assessing if the tweets' hashtags may help detecting the non-factual accounts.
> 
> LR + All Features (tweet-level): We extract all our features from each tweet and feed them into a LR classifier. Here, we do not aggregate over tweets and thus view each tweet independently.
> 
> LR + All Features (chunk-level): We concatenate the features' vectors of the tweets in a chunk and feed them into a LR classifier.
> 
> FacTweet (tweet-level): Similar to the FacTweet approach, but at tweet-level; the sequential flow of the tweets is not utilized. We aim at investigating the importance of the sequential flow of tweets.
> 
> Top-$k$ replies, likes, or re-tweets: Some approaches in rumors detection use the number of replies, likes, and re-tweets to detect rumors BIBREF21. Thus, we extract top $k$ replied, liked or re-tweeted tweets from each account to assess the

#### Relevance 857

Label: 

#### Passage 858

Retrieved by: Dense, Hybrid RRF

> In this paper, we proposed a model that utilizes chunked timelines of tweets and a recurrent neural model in order to infer the factuality of a Twitter news account. Our experimental results indicate the importance of analyzing tweet stream into chunks, as well as the benefits of heterogeneous knowledge source (i.e., lexica as well as text) in order to capture factuality. In future work, we would like to extend this line of research with further in-depth analysis to understand the flow change of the used features in the accounts' streams. Moreover, we would like to take our approach one step further incorporating explicit temporal information, e.g., using timestamps. Crucially, we are also interested in developing a multilingual version of our approach, for instance by leveraging the now ubiquitous cross-lingual embeddings BIBREF22, BIBREF23.

#### Relevance 858

Label: 

#### Passage 859

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> of tweets.
> 
> Top-$k$ replies, likes, or re-tweets: Some approaches in rumors detection use the number of replies, likes, and re-tweets to detect rumors BIBREF21. Thus, we extract top $k$ replied, liked or re-tweeted tweets from each account to assess the accounts factuality. We tested different $k$ values between 10 tweets to the max number of tweets from each account. Figure FIGREF24 shows the macro-F1 values for different $k$ values. It seems that $k=500$ for the top replied tweets achieves the highest result. Therefore, we consider this as a baseline.
> 
> Experimental Setup. We apply a 5 cross-validation on the account's level. For the FacTweet model, we experiment with 25% of the accounts for validation and parameters selection. We use hyperopt library to select the hyper-parameters on the following values: LSTM layer size (16, 32, 64), dropout ($0.0-0.9$), activation function ($relu$, $selu$, $tanh$), optimizer ($sgd$, $adam$, $rmsprop$) with varying the value of the learning rate (1e-1,..,-5), and batch size (4, 8, 16). The validation split is extracted on the class level using stratified sampling: we took a random 25% of the accounts from each class since the dataset is unbalanced. Discarding the classes' size in the splitting process may affect the minority classes (e.g. hoax). For the baselines' classifier, we tested many classifiers and the LR showed the best overall performance.
> 
> Results. Table TABREF25 presents the results. We present the results using a chunk size of 20, which was found to be the best size on the held-out data. Figure FIGREF24 shows the results of different chunks sizes. FacTweet performs better than the proposed baselines and obtains the highest macro-F1 value of $0.565$. Our results indicate the importance of taking into account the sequence of the tweets in the accounts' timelines. The sequence of these tweets is better captured by our proposed model sequence-agnostic or non-neural classifiers. Moreover, the results demonstrate that the features at tweet-level do not perform well to detect the Twitter accounts factuality, since they obtain a result near to the majority class ($0.18$). Another finding from our experiments shows that the performance of the Tweet2vec is weak. This demonstrates that tweets' hashtags are not informative to detect non-factual accounts. In Table TABREF25, we

#### Relevance 859

Label: 

### BM25

None

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 860

Retrieved by: Hybrid RRF followed by BGE reranking

> emotion types from two available emotional lexicons. We use the NRC lexicon BIBREF10, which contains $\sim $14K words labeled using the eight Plutchik's emotions BIBREF11. The other lexicon is SentiSense BIBREF12 which is a concept-based affective lexicon that attaches emotional meanings to concepts from the WordNet lexical database. It has $\sim $5.5 words labeled with emotions from a set of 14 emotional categories We use the categories that do not exist in the NRC lexicon.
> 
> Sentiment: We extract the sentiment of the tweets by employing EffectWordNet BIBREF13, SenticNet BIBREF14, NRC BIBREF10, and subj_lexicon BIBREF15, where each has the two sentiment classes, positive and negative.
> 
> Morality: Features based on morality foundation theory BIBREF16 where words are labeled in one of the following 10 categories (care, harm, fairness, cheating, loyalty, betrayal, authority, subversion, sanctity, and degradation).
> 
> Style: We use canonical stylistic features, such as the count of question marks, exclamation marks, consecutive characters and letters, links, hashtags, users' mentions. In addition, we extract the uppercase ratio and the tweet length.
> 
> Words embeddings: We extract words embeddings of the words of the tweet using $Glove\-840B-300d$ BIBREF17 pretrained model. The tweet final representation is obtained by averaging its words embeddings.
> 
> Model. To account for chunk sequences we make use of a de facto standard approach and opt for a recurrent neural model using long short-term memory (LSTM) BIBREF18. In our model, the sequence consists of a sequence of tweets belonging to one chunk (Figure FIGREF11). The LSTM learns the hidden state $h\textsubscript {t}$ by capturing the previous timesteps (past tweets). The produced hidden state $h\textsubscript {t}$ at each time step is passed to the attention layer which computes a `context' vector $c\textsubscript {t}$ as the weighted mean of the state sequence $h$ by:
> 
> Where $T$ is the total number of timesteps in the input sequence and $\alpha \textsubscript {tj}$ is a weight computed at each time step $j$ for each state hj.

#### Relevance 860

Label: 

## Question 0095

Paper: Predicting the Industry of Users on Social Media

> How many users do they look at?

### Common Retrieved Chunks

#### Passage 861

Retrieved by: BM25, Dense, Hybrid RRF

> To conduct a qualitative exploration of which words indicate the industry of a user, Table TABREF14 shows the three top-ranking content words for the different industries using the AFR method.
> 
> Not surprisingly, the top ranked words align well with what we would intuitively expect for each industry. Even though most of these words are potentially used by many users regardless of their industry in our dataset, they are still distinguished by the AFR method because of the different frequencies of these words in the text of each industry.

#### Relevance 861

Label: 

#### Passage 862

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We compile our industry-annotated dataset by identifying blogger profiles located in the U.S. on the profile finder on http://www.blogger.com, and scraping only those users that had the industry profile element completed.
> 
> For each of these bloggers, we retrieve all their blogs, and for each of these blogs we download the 21 most recent blog postings. We then clean these blog posts of HTML tags and tokenize them, and drop those bloggers whose cumulative textual content in their posts is less than 600 characters. Following these guidelines, we identified all the U.S. bloggers with completed industry information.
> 
> Traditionally, standardized industry taxonomies organize economic activities into groups based on similar production processes, products or services, delivery systems or behavior in financial markets. Following such assumptions and regardless of their many similarities, a tomato farmer would be categorized into a distinct industry from a tobacco farmer. As demonstrated in Preotiuc-Pietro et al. Preoctiuc15 such groupings can cause unwarranted misclassifications.
> 
> The Blogger platform provides a total of 39 different industry options. Even though a completed industry value is an implicit text annotation, we acknowledge the same problem noted in previous studies: some categories are too broad, while others are very similar. To remedy this and following Guibert et al. Guibert71, who argued that the denominations used in a classification must reflect the purpose of the study, we group the different Blogger industries based on similar educational background and similar technical terminology. To do that, we exclude very general categories and merge conceptually similar ones. Examples of broad categories are the Education and the Student options: a teacher could be teaching in any concentration, while a student could be enrolled in any discipline. Examples of conceptually similar categories are the Investment Banking and the Banking options.
> 
> The final set of categories is shown in Table TABREF1 , along with the number of users in each category. The resulting dataset consists of 22,880 users, 41,094 blogs, and 561,003 posts. Table TABREF2 presents additional statistics of our dataset.

#### Relevance 862

Label: 

#### Passage 864

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Over the past two decades, the emergence of social media has enabled the proliferation of traceable human behavior. The content posted by users can reflect who their friends are, what topics they are interested in, or which company they are working for. At the same time, users are listing a number of profile fields to define themselves to others. The utilization of such metadata has proven important in facilitating further developments of applications in advertising BIBREF0 , personalization BIBREF1 , and recommender systems BIBREF2 . However, profile information can be limited, depending on the platform, or it is often deliberately omitted BIBREF3 . To uncloak this information, a number of studies have utilized social media users' footprints to approximate their profiles.
> 
> This paper explores the potential of predicting a user's industry –the aggregate of enterprises in a particular field– by identifying industry indicative text in social media. The accurate prediction of users' industry can have a big impact on targeted advertising by minimizing wasted advertising BIBREF4 and improved personalized user experience. A number of studies in the social sciences have associated language use with social factors such as occupation, social class, education, and income BIBREF5 , BIBREF6 , BIBREF7 , BIBREF8 . An additional goal of this paper is to examine such findings, and in particular the link between language and occupational class, through a data-driven approach.
> 
> In addition, we explore how meaning changes depending on the occupational context. By leveraging word embeddings, we seek to quantify how, for example, cloud might mean a separate concept (e.g., condensed water vapor) in the text written by users that work in environmental jobs while it might be used differently by users in technology occupations (e.g., Internet-based computing).
> 
> Specifically, this paper makes four main contributions. First, we build a large, industry-annotated dataset that contains over 20,000 blog users. In addition to their posted text, we also link a number of user metadata including their gender, location, occupation, introduction and interests.
> 
> Second, we build content-based classifiers for the industry prediction task and study the effect of incorporating textual features from the users' profile metadata using various meta-classification techniques, significantly improving both the overall accuracy and the average per industry

#### Relevance 864

Label: 

#### Passage 866

Retrieved by: Dense, Hybrid RRF

> Alongside the wide adoption of social media by the public, researchers have been leveraging the newly available data to create and refine models of users' behavior and profiling. There exists a myriad research that analyzes language in order to profile social media users. Some studies sought to characterize users' personality BIBREF9 , BIBREF10 , while others sequenced the expressed emotions BIBREF11 , studied mental disorders BIBREF12 , and the progression of health conditions BIBREF13 . At the same time, a number of researchers sought to predict the social media users' age and/or gender BIBREF14 , BIBREF15 , BIBREF16 , while others targeted and analyzed the ethnicity, nationality, and race of the users BIBREF17 , BIBREF18 , BIBREF19 . One of the profile fields that has drawn a great deal of attention is the location of a user. Among others, Hecht et al. Hecht11 predicted Twitter users' locations using machine learning on nationwide and state levels. Later, Han et al. Han14 identified location indicative words to predict the location of Twitter users down to the city level.
> 
> As a separate line of research, a number of studies have focused on discovering the political orientation of users BIBREF15 , BIBREF20 , BIBREF21 . Finally, Li et al. Li14a proposed a way to model major life events such as getting married, moving to a new place, or graduating. In a subsequent study, BIBREF22 described a weakly supervised information extraction method that was used in conjunction with social network information to identify the name of a user's spouse, the college they attended, and the company where they are employed.
> 
> The line of work that is most closely related to our research is the one concerned with understanding the relation between people's language and their industry. Previous research from the fields of psychology and economics have explored the potential for predicting one's occupation from their ability to use math and verbal symbols BIBREF23 and the relationship between job-types and demographics BIBREF24 . More recently, Huang et al. Huang15 used machine learning to classify Sina Weibo users to twelve different platform-defined occupational classes highlighting the effect of homophily in user interactions. This work examined only users that have been verified by

#### Relevance 866

Label: 

#### Passage 867

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> BIBREF24 . More recently, Huang et al. Huang15 used machine learning to classify Sina Weibo users to twelve different platform-defined occupational classes highlighting the effect of homophily in user interactions. This work examined only users that have been verified by the Sina Weibo platform, introducing a potential bias in the resulting dataset. Finally, Preotiuc-Pietro et al. Preoctiuc15 predicted the occupational class of Twitter users using the Standard Occupational Classification (SOC) system, which groups the different jobs based on skill requirements. In that work, the data collection process was limited to only users that specifically mentioned their occupation in their self-description in a way that could be directly mapped to a SOC occupational class. The mapping between a substring of their self-description and a SOC occupational class was done manually. Because of the manual annotation step, their method was not scalable; moreover, because they identified the occupation class inside a user self-description, only a very small fraction of the Twitter users could be included (in their case, 5,191 users).
> 
> Both of these recent studies are based on micro-blogging platforms, which inherently restrict the number of characters that a post can have, and consequently the way that users can express themselves.
> 
> Moreover, both studies used off-the-shelf occupational taxonomies (rather than self-declared occupation categories), resulting in classes that are either too generic (e.g., media, welfare and electronic are three of the twelve Sina Weibo categories), or too intermixed (e.g., an assistant accountant is in a different class from an accountant in SOC). To address these limitations, we investigate the industry prediction task in a large blog corpus consisting of over 20K American users, 40K web-blogs, and 560K blog posts.

#### Relevance 867

Label: 

#### Passage 868

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> After collecting our dataset, we split it into three sets: a train set, a development set, and a test set. The sizes of these sets are 17,880, 2,500, and 2,500 users, respectively, with users randomly assigned to these sets. In all the experiments that follow, we evaluate our classifiers by training them on the train set, configure the parameters and measure performance on the development set, and finally report the prediction accuracy and results on the test set. Note that all the experiments are performed at user level, i.e., all the data for one user is compiled into one instance in our data sets.
> 
> To measure the performance of our classifiers, we use the prediction accuracy. However, as shown in Table TABREF1 , the available data is skewed across categories, which could lead to somewhat distorted accuracy numbers depending on how well a model learns to predict the most populous classes. Moreover, accuracy alone does not provide a great deal of insight into the individual performance per industry, which is one of the main objectives in this study. Therefore, in our results below, we report: (1) micro-accuracy ( INLINEFORM0 ), calculated as the percentage of correctly classified instances out of all the instances in the development (test) data; and (2) macro-accuracy ( INLINEFORM1 ), calculated as the average of the per-category accuracies, where the per-category accuracy is the percentage of correctly classified instances out of the instances belonging to one category in the development (test) data.

#### Relevance 868

Label: 

### BM25

#### Passage 863

Retrieved by: BM25

> and interests.
> 
> Second, we build content-based classifiers for the industry prediction task and study the effect of incorporating textual features from the users' profile metadata using various meta-classification techniques, significantly improving both the overall accuracy and the average per industry accuracy.
> 
> Next, after examining which words are indicative for each industry, we build vector-space representations of word meanings and calculate one deviation for each industry, illustrating how meaning is differentiated based on the users' industries. We qualitatively examine the resulting industry-informed semantic representations of words by listing the words per industry that are most similar to job related and general interest terms.
> 
> Finally, we rank the different industries based on the normalized relative frequencies of emotionally charged words (positive and negative) and, in addition, discover that, for both genders, these frequencies do not statistically significantly correlate with an industry's gender dominance ratio.
> 
> After discussing related work in Section SECREF2 , we present the dataset used in this study in Section SECREF3 . In Section SECREF4 we evaluate two feature selection methods and examine the industry inference problem using the text of the users' postings. We then augment our content-based classifier by building an ensemble that incorporates several metadata classifiers. We list the most industry indicative words and expose how each industrial semantic field varies with respect to a variety of terms in Section SECREF5 . We explore how the frequencies of emotionally charged words in each gender correlate with the industries and their respective gender dominance ratio and, finally, conclude in Section SECREF6 .

#### Relevance 863

Label: 

#### Passage 865

Retrieved by: BM25

> This material is based in part upon work supported by the National Science Foundation (#1344257) and by the John Templeton Foundation (#48503). Any opinions, findings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National Science Foundation or the John Templeton Foundation.

#### Relevance 865

Label: 

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 869

Retrieved by: Hybrid RRF followed by BGE reranking

> In this paper, we examined the task of predicting a social media user's industry. We introduced an annotated dataset of over 20,000 blog users and applied a content-based classifier in conjunction with two feature selection methods for an overall accuracy of up to 0.534, which represents a large improvement over the majority class baseline of 0.188.
> 
> We also demonstrated how the user metadata can be incorporated in our classifiers. Although concatenation of features drawn both from blog content and profile elements did not yield any clear improvements over the best individual classifiers, we found that stacking improves the prediction accuracy to an overall accuracy of 0.643, as measured on our test dataset. A more in-depth analysis showed that not all industries are equally easy to predict: while industries such as Real Estate and Religion are clearly distinguishable with accuracy figures over 0.80, others such as Banking are much harder to predict.
> 
> Finally, we presented a qualitative analysis to provide some insights into the language of different industries, which highlighted differences in the top-ranked words in each industry, word semantic similarities, and the relative frequency of emotionally charged words.

#### Relevance 869

Label: 

## Question 0096

Paper: Natural Language Generation for Spoken Dialogue System using RNN Encoder-Decoder Networks

> Does the model evaluated on NLG datasets or dialog datasets?

### Common Retrieved Chunks

#### Passage 870

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Natural Language Generation (NLG) plays a critical role in Spoken Dialogue Systems (SDS) with task is to convert a meaning representation produced by the Dialogue Manager into natural language utterances. Conventional approaches still rely on comprehensive hand-tuning templates and rules requiring expert knowledge of linguistic representation, including rule-based BIBREF0 , corpus-based n-gram models BIBREF1 , and a trainable generator BIBREF2 .
> 
> Recently, Recurrent Neural Networks (RNNs) based approaches have shown promising performance in tackling the NLG problems. The RNN-based models have been applied for NLG as a joint training model BIBREF3 , BIBREF4 and an end-to-end training model BIBREF5 . A recurring problem in such systems is requiring annotated datasets for particular dialogue acts (DAs). To ensure that the generated utterance representing the intended meaning of the given DA, the previous RNN-based models were further conditioned on a 1-hot vector representation of the DA. BIBREF3 introduced a heuristic gate to ensure that all the slot-value pair was accurately captured during generation. BIBREF4 subsequently proposed a Semantically Conditioned Long Short-term Memory generator (SC-LSTM) which jointly learned the DA gating signal and language model.
> 
> More recently, Encoder-Decoder networks BIBREF6 , BIBREF7 , especially the attentional based models BIBREF8 , BIBREF9 have been explored to solve the NLG tasks. The Attentional RNN Encoder-Decoder BIBREF10 (ARED) based approaches have also shown improved performance on a variety of tasks, e.g., image captioning BIBREF11 , BIBREF12 , text summarization BIBREF13 , BIBREF14 .
> 
> While the RNN-based generators with DA gating-vector can prevent the undesirable semantic repetitions, the ARED-based generators show signs of better adapting to a new domain. However, none of the models show significant advantage from out-of-domain data. To better analyze model generalization to an unseen, new domain as well as model leveraging the out-of-domain sources, we propose a new architecture which is an extension of the ARED model. In order to better select, aggregate and control the semantic information, a Refinement Adjustment LSTM-based component (RALSTM) is introduced to the decoder side. The proposed model can learn from unaligned data by jointly training the sentence planning and surface realization to produce natural language sentences. We conducted experiments on four different NLG domains and found that the proposed methods significantly outperformed

#### Relevance 870

Label: 

#### Passage 871

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> decoder side. The proposed model can learn from unaligned data by jointly training the sentence planning and surface realization to produce natural language sentences. We conducted experiments on four different NLG domains and found that the proposed methods significantly outperformed the state-of-the-art methods regarding BLEU BIBREF15 and slot error rate ERR scores BIBREF4 . The results also showed that our generators could scale to new domains by leveraging the out-of-domain data. To sum up, we make three key contributions in this paper:
> 
> We review related works in Section "Related Work" . Following a detail of proposed model in Section "Recurrent Neural Language Generator" , Section "Experiments" describes datasets, experimental setups, and evaluation metrics. The resulting analysis is presented in Section "Results and Analysis" . We conclude with a brief summary and future work in Section "Conclusion and Future Work" .

#### Relevance 871

Label: 

#### Passage 872

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We assessed the proposed models on four different NLG domains: finding a restaurant, finding a hotel, buying a laptop, and buying a television. The Restaurant and Hotel were collected in BIBREF4 , while the Laptop and TV datasets have been released by BIBREF22 with a much larger input space but only one training example for each DA so that the system must learn partial realization of concepts and be able to recombine and apply them to unseen DAs. This makes the NLG tasks for the Laptop and TV domains become much harder. The dataset statistics are shown in Table 1 .

#### Relevance 872

Label: 

#### Passage 873

Retrieved by: BM25, Dense, Hybrid RRF

> greater ERR score comparing to the two models.
> 
> A comparison of top responses generated for some input DAs between different models are shown in Table 4 . While the previous models still produce some errors (missing and misplaced information), the proposed models (RALSTM and the models All2* trained by pooling all datasets together) can generate appropriate sentences. We also found that the proposed models tend to generate more complete and concise sentences than the other models.
> 
> All these prove the importance of the proposed components: the Refinement cell in aggregating and selecting the attentive information, and the Adjustment cell in controlling the feature vector (see Examples in Figure 6 ).
> 
> Figure 4 shows a comparison performance of general models as described in Section "Experimental Setups" . The results are consistent with the Figure 3 , in which the RALSTM has better performance than the Enc-Dec and SCLSTM on all domains in terms of the BLEU and the ERR scores, while the Enc-Dec has difficulties in reducing the ERR score. This indicates the relevant contribution of the proposed component Refinement and Adjustment cells to the original ARED architecture, in which the Refinement with attentional gating can effectively select and aggregate the information before putting them into the traditional LSTM cell, while the Adjustment with gating DA vector can effectively control the information flow during generation.
> 
> Figure 5 shows domain scalability of the three models in which the models were first trained on the merging out-of-domain Restaurant and Hotel datasets, then fine tuned the parameters with varied amount of in-domain training data (laptop domain). The RALSTM model outperforms the previous model in both cases where the sufficient in-domain data is used (as in Figure 5 -left) and the limited in-domain data is used (Figure 5 -right). The Figure 5 -right also indicates that the RALSTM model can adapt to a new, unseen domain faster than the previous models.

#### Relevance 873

Label: 

#### Passage 875

Retrieved by: Dense, Hybrid RRF

> We present an extension of ARED model, in which an RALSTM component is introduced to select and aggregate semantic elements produced by the Encoder, and to generate the required sentence. We assessed the proposed models on four NLG domains and compared to the state-of-the-art generators. The proposed models empirically show consistent improvement over the previous methods in both the BLEU and ERR evaluation metrics. The proposed models also show an ability to extend to a new, unseen domain no matter how much the in-domain training data was fed. In the future, it would be interesting to apply the proposed model to other tasks that can be modeled based on the encoder-decoder architecture, i.e., image captioning, reading comprehension, and machine translation.

#### Relevance 875

Label: 

### BM25

#### Passage 874

Retrieved by: BM25

> We extensively conducted a set of experiments to assess the effectiveness of the proposed models by using several metrics, datasets, and model architectures, in order to compare to prior methods.

#### Relevance 874

Label: 

### Dense

#### Passage 876

Retrieved by: Dense

> The generators were implemented using the TensorFlow library BIBREF31 and trained with training, validation and testing ratio as 3:1:1. The hidden layer size, beam size were set to be 80 and 10, respectively, and the generators were trained with a $70\%$ of dropout rate. We performed 5 runs with different random initialization of the network and the training is terminated by using early stopping. We then chose a model that yields the highest BLEU score on the validation set as shown in Table 2 . Since the trained models can differ depending on the initialization, we also report the results which were averaged over 5 randomly initialized networks. Note that, except the results reported in Table 2 , all the results shown were averaged over 5 randomly initialized networks. We set $\lambda $ to 1000 to severely discourage the reranker from selecting utterances which contain either redundant or missing slots. For each DA, we over-generated 20 candidate sentences and selected the top 5 realizations after reranking. Moreover, in order to better understand the effectiveness of our proposed methods, we: (i) performed an ablation experiments to demonstrate the contribution of each proposed cells (Tables 2 , 3 ), (ii) trained the models on the Laptop domain with varied proportion of training data, starting from $10\%$ to $100\%$ (Figure 3 ), (iii) trained general models by merging all the data from four domains together and tested them in each individual domain (Figure 4 ), and (iv) trained adaptation models on merging data from restaurant and hotel domains, then fine tuned the model on laptop domain with varied amount of adaptation data (Figure 5 ).

#### Relevance 876

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 877

Retrieved by: Hybrid RRF followed by BGE reranking

> Recently, RNNs-based models have shown promising performance in tackling the NLG problems. BIBREF16 proposed a generator using RNNs to create Chinese poetry. BIBREF11 , BIBREF17 , BIBREF18 also used RNNs in a multi-modal setting to solve image captioning tasks. The RNN-based Sequence to Sequence models have applied to solve variety of tasks: conversational modeling BIBREF6 , BIBREF7 , BIBREF19 , machine translation BIBREF20 , BIBREF21
> 
> For task-oriented dialogue systems, BIBREF3 combined a forward RNN generator, a CNN reranker, and a backward RNN reranker to generate utterances. BIBREF4 proposed SC-LSTM generator which introduced a control sigmoid gate to the LSTM cell to jointly learn the gating mechanism and language model. A recurring problem in such systems is the lack of sufficient domain-specific annotated data. BIBREF22 proposed an out-of-domain model which was trained on counterfeited data by using semantically similar slots from the target domain instead of the slots belonging to the out-of-domain dataset. The results showed that the model can achieve a satisfactory performance with a small amount of in-domain data by fine tuning the target domain on the out-of-domain trained model.
> 
> More recently, RNN encoder-decoder based models with attention mechanism BIBREF10 have shown improved performances in various tasks. BIBREF12 proposed a review network to the image captioning, which reviews all the information encoded by the encoder and produces a compact thought vector. BIBREF9 proposed RNN encoder-decoder-based model by using two attention layers to jointly train content selection and surface realization. More close to our work, BIBREF8 proposed an attentive encoder-decoder based generator which computed the attention mechanism over the slot-value pairs. The model showed a domain scalability when a very limited amount of data is available.
> 
> Moving from a limited domain dialogue system to an open domain dialogue system raises some issues. Therefore, it is important to build an open domain dialogue system that can make as much use of existing abilities of functioning from other domains. There have been several works to tackle this problem, such as BIBREF23 using RNN-based networks for multi-domain dialogue state tracking, BIBREF22 using a procedure to train multi-domain via multiple adaptation steps, or BIBREF24 , BIBREF25 adapting of SDS components to new domains.

#### Relevance 877

Label: 

#### Passage 878

Retrieved by: Hybrid RRF followed by BGE reranking

> The generator performance was assessed on the two evaluation metrics: the BLEU and the slot error rate ERR by adopting code from an open source benchmark toolkit for Natural Language Generation. We compared the proposed models against three strong baselines which have been recently published as state-of-the-art NLG benchmarks[]. https://github.com/shawnwun/RNNLG
> 
> HLSTM proposed by BIBREF3 thwsjy15 which used a heuristic gate to ensure that all of the slot-value information was accurately captured when generating.
> 
> SCLSTM proposed by BIBREF4 wensclstm15 which can jointly learn the gating signal and language model.
> 
> Enc-Dec proposed by BIBREF8 wentoward which applied the attention-based encoder-decoder architecture.

#### Relevance 878

Label: 

## Question 0097

Paper: Identifying Visible Actions in Lifestyle Vlogs

> How many actions are present in the dataset?

### Common Retrieved Chunks

#### Passage 879

Retrieved by: BM25, Dense, Hybrid RRF

> There has been a surge of recent interest in detecting human actions in videos. Work in this space has mainly focused on learning actions from articulated human pose BIBREF7 , BIBREF8 , BIBREF9 or mining spatial and temporal information from videos BIBREF10 , BIBREF11 . A number of resources have been produced, including Action Bank BIBREF12 , NTU RGB+D BIBREF13 , SBU Kinect Interaction BIBREF14 , and PKU-MMD BIBREF15 .
> 
> Most research on video action detection has gathered video information for a set of pre-defined actions BIBREF2 , BIBREF16 , BIBREF1 , an approach known as explicit data gathering BIBREF0 . For instance, given an action such as “open door,” a system would identify videos that include a visual depiction of this action. While this approach is able to detect a specific set of actions, whose choice may be guided by downstream applications, it achieves high precision at the cost of low recall. In many cases, the set of predefined actions is small (e.g., 203 activity classes in BIBREF2 ), and for some actions, the number of visual depictions is very small.
> 
> An alternative approach is to start with a set of videos, and identify all the actions present in these videos BIBREF17 , BIBREF18 . This approach has been referred to as implicit data gathering, and it typically leads to the identification of a larger number of actions, possibly with a small number of examples per action.
> 
> In this paper, we use an implicit data gathering approach to label human activities in videos. To the best of our knowledge, we are the first to explore video action recognition using both transcribed audio and video information. We focus on the popular genre of lifestyle vlogs, which consist of videos of people demonstrating routine actions while verbally describing them. We use these videos to develop methods to identify if actions are visually present.
> 
> The paper makes three main contributions. First, we introduce a novel dataset consisting of 1,268 short video clips paired with sets of actions mentioned in the video transcripts, as well as manual annotations of whether the actions are visible or not. The dataset includes a total of 14,769 actions, 4,340 of which are

#### Relevance 879

Label: 

#### Passage 880

Retrieved by: BM25, Hybrid RRF

> We collect a dataset of routine and do-it-yourself (DIY) videos from YouTube, consisting of people performing daily activities, such as making breakfast or cleaning the house. These videos also typically include a detailed verbal description of the actions being depicted. We choose to focus on these lifestyle vlogs because they are very popular, with tens of millions having been uploaded on YouTube; tab:nbresultssearchqueries shows the approximate number of videos available for several routine queries. Vlogs also capture a wide range of everyday activities; on average, we find thirty different visible human actions in five minutes of video.
> 
> By collecting routine videos, instead of searching explicitly for actions, we do implicit data gathering, a form of data collection introduced by BIBREF0 . Because everyday actions are common and not unusual, searching for them directly does not return many results. In contrast, by collecting routine videos, we find many everyday activities present in these videos.

#### Relevance 880

Label: 

#### Passage 881

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> visibility in a video. We use a dataset of words with associated concreteness scores from BIBREF46 . Each word is labeled by a human annotator with a value between 1 (very abstract) and 5 (very concrete). The percentage of actions from our dataset that have at least one word in the concreteness dataset is 99.8%. For each action, we use the concreteness scores of the verbs and nouns in the action. We consider the concreteness score of an action to be the highest concreteness score of its corresponding verbs and nouns. tab:concr1 shows several sample actions along with their concreteness scores and their visiblity.
> 
> Video Representations. We use Yolo9000 BIBREF47 to identify objects present in each miniclip. We choose YOLO9000 for its high and diverse number of labels (9,000 unique labels). We sample the miniclips at a rate of 1 frame-per-second, and we use the Yolo9000 model pre-trained on COCO BIBREF48 and ImageNet BIBREF49 .
> 
> We represent a video both at the frame level and the sequence level. For frame-level video features, we use the Inception V3 model BIBREF37 pre-trained on ImageNet. We extract the output of the very last layer before the Flatten operation (the “bottleneck layer"); we choose this layer because the following fully connected layers are too specialized for the original task they were trained for. We extract Inception V3 features from miniclips sampled at 1 frame-per-second.
> 
> For sequence-level video features, we use the C3D model BIBREF27 pre-trained on the Sports-1M dataset BIBREF23 . Similarly, we take the feature map of the sixth fully connected layer. Because C3D captures motion information, it is important that it is applied on consecutive frames. We take each frame used to extract the Inception features and extract C3D features from the 16 consecutive frames around it.
> 
> We use this approach because combining Inception V3 and C3D features has been shown to work well in other video-based models BIBREF30 , BIBREF25 , BIBREF1 .

#### Relevance 881

Label: 

#### Passage 882

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The goal of our dataset is to capture naturally-occurring, routine actions. Because the same action can be identified in different ways (e.g., “pop into the freezer”, “stick into the freezer"), our dataset has a complex and diverse set of action labels. These labels demonstrate the language used by humans in everyday scenarios; because of that, we choose not to group our labels into a pre-defined set of actions. Table TABREF1 shows the number of unique verbs, which can be considered a lower bound for the number of unique actions in our dataset. On average, a single verb is used in seven action labels, demonstrating the richness of our dataset.
> 
> The action labels extracted from the transcript are highly dependent on the performance of the constituency parser. This can introduce noise or ill-defined action labels. Some acions contain extra words (e.g., “brush my teeth of course”), or lack words (e.g., “let me just”). Some of this noise is handled during the annotation process; for example, most actions that lack words are labeled as “not visible” or “not an action” because they are hard to interpret.

#### Relevance 882

Label: 

#### Passage 883

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> In this paper, we address the task of identifying human actions visible in online videos. We focus on the genre of lifestyle vlogs, and construct a new dataset consisting of 1,268 miniclips and 14,769 actions out of which 4,340 have been labeled as visible. We describe and evaluate several text-based and video-based baselines, and introduce a multimodal neural model that leverages visual and linguistic information as well as additional information available in the input data. We show that the multimodal model outperforms the use of one modality at a time.
> 
> A distinctive aspect of this work is that we label actions in videos based on the language that accompanies the video. This has the potential to create a large repository of visual depictions of actions, with minimal human intervention, covering a wide spectrum of actions that typically occur in everyday life.
> 
> In future work, we plan to explore additional representations and architectures to improve the accuracy of our model, and to identify finer-grained alignments between visual actions and their verbal descriptions. The dataset and the code introduced in this paper are publicly available at http://lit.eecs.umich.edu/downloads.html.

#### Relevance 883

Label: 

#### Passage 884

Retrieved by: Dense, Hybrid RRF

> There has been substantial work on action recognition in the computer vision community, focusing on creating datasets BIBREF22 , BIBREF23 , BIBREF5 , BIBREF2 or introducing new methods BIBREF24 , BIBREF25 , BIBREF26 , BIBREF27 . Table TABREF1 compares our dataset with previous action recognition datasets.
> 
> The largest datasets that have been compiled to date are based on YouTube videos BIBREF2 , BIBREF16 , BIBREF1 . These actions cover a broad range of classes including human-object interactions such as cooking BIBREF28 , BIBREF29 , BIBREF6 and playing tennis BIBREF23 , as well as human-human interactions such as shaking hands and hugging BIBREF4 .
> 
> Similar to our work, some of these previous datasets have considered everyday routine actions BIBREF2 , BIBREF16 , BIBREF1 . However, because these datasets rely on videos uploaded on YouTube, it has been observed they can be potentially biased towards unusual situations BIBREF1 . For example, searching for videos with the query “drinking tea" results mainly in unusual videos such as dogs or birds drinking tea. This bias can be addressed by paying people to act out everyday scenarios BIBREF5 , but this can end up being very expensive. In our work, we address this bias by changing the approach used to search for videos. Instead of searching for actions in an explicit way, using queries such as “opening a fridge” or “making the bed,” we search for more general videos using queries such as “my morning routine.” This approach has been referred to as implicit (as opposed to explicit) data gathering, and was shown to result in a greater number of videos with more realistic action depictions BIBREF0 .
> 
> Although we use implicit data gathering as proposed in the past, unlike BIBREF0 and other human action recognition datasets, we search for routine videos that contain rich audio descriptions of the actions being performed, and we use this transcribed audio to extract actions. In these lifestyle vlogs, a vlogger typically performs an action while also describing it in detail. To the best of our knowledge, we are the first to build a video action recognition dataset using both transcribed audio and video information.
> 
> Another important difference between our methodology and previously proposed

#### Relevance 884

Label: 

#### Passage 886

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> of 1,268 short video clips paired with sets of actions mentioned in the video transcripts, as well as manual annotations of whether the actions are visible or not. The dataset includes a total of 14,769 actions, 4,340 of which are visible. Second, we propose a set of strong baselines to determine whether an action is visible or not. Third, we introduce a multimodal neural architecture that combines information drawn from visual and linguistic clues, and show that it improves over models that rely on one modality at a time.
> 
> By making progress towards automatic action recognition, in addition to contributing to video understanding, this work has a number of important and exciting applications, including sports analytics BIBREF19 , human-computer interaction BIBREF20 , and automatic analysis of surveillance video footage BIBREF21 .
> 
> The paper is organized as follows. We begin by discussing related work, then describe our data collection and annotation process. We next overview our experimental set-up and introduce a multimodal method for identifying visible actions in videos. Finally, we discuss our results and conclude with general directions for future work.

#### Relevance 886

Label: 

#### Passage 887

Retrieved by: Hybrid RRF, Hybrid RRF followed by BGE reranking

> Our goal is to identify which of the actions extracted from the transcripts are visually depicted in the videos. We create an annotation task on Amazon Mechanical Turk (AMT) to identify actions that are visible.
> 
> We give each AMT turker a HIT consisting of five miniclips with up to seven actions generated from each miniclip. The turker is asked to assign a label (visible in the video; not visible in the video; not an action) to each action. Because it is difficult to reliably separate not visible and not an action, we group these labels together.
> 
> Each miniclip is annotated by three different turkers. For the final annotation, we use the label assigned by the majority of turkers, i.e., visible or not visible / not an action.
> 
> To help detect spam, we identify and reject the turkers that assign the same label for every action in all five miniclips that they annotate. Additionally, each HIT contains a ground truth miniclip that has been pre-labeled by two reliable annotators. Each ground truth miniclip has more than four actions with labels that were agreed upon by both reliable annotators. We compute accuracy between a turker's answers and the ground truth annotations; if this accuracy is less than 20%, we reject the HIT as spam.
> 
> After spam removal, we compute the agreement score between the turkers using Fleiss kappa BIBREF43 . Over the entire data set, the Fleiss agreement score is 0.35, indicating fair agreement. On the ground truth data, the Fleiss kappa score is 0.46, indicating moderate agreement. This fair to moderate agreement indicates that the task is difficult, and there are cases where the visibility of the actions is hard to label. To illustrate, Figure FIGREF9 shows examples where the annotators had low agreement.
> 
> Table TABREF8 shows statistics for our final dataset of videos labeled with actions, and Figure 2 shows a sample video and transcript, with annotations.
> 
> For our experiments, we use the first eight YouTube channels from our dataset as train data, the ninth channel as validation data and the last channel as test data. Statistics for this split are shown in Table TABREF10 .

#### Relevance 887

Label: 

### BM25

None

### Dense

#### Passage 885

Retrieved by: Dense

> action while also describing it in detail. To the best of our knowledge, we are the first to build a video action recognition dataset using both transcribed audio and video information.
> 
> Another important difference between our methodology and previously proposed methods is that we extract action labels from the transcripts. By gathering data before annotating the actions, our action labels are post-defined (as in BIBREF0 ). This is unlike the majority of the existing human action datasets that use pre-defined labels BIBREF5 , BIBREF2 , BIBREF16 , BIBREF1 , BIBREF4 , BIBREF29 , BIBREF6 , BIBREF3 . Post-defined labels allow us to use a larger set of labels, expanding on the simplified label set used in earlier datasets. These action labels are more inline with everyday scenarios, where people often use different names for the same action. For example, when interacting with a robot, a user could refer to an action in a variety of ways; our dataset includes the actions “stick it into the freezer,” “freeze it,” “pop into the freezer,” and “put into the freezer,” variations, which would not be included in current human action recognition datasets.
> 
> In addition to human action recognition, our work relates to other multimodal tasks such as visual question answering BIBREF30 , BIBREF31 , video summarization BIBREF32 , BIBREF33 , and mapping text descriptions to video content BIBREF34 , BIBREF35 . Specifically, we use an architecture similar to BIBREF30 , where an LSTM BIBREF36 is used together with frame-level visual features such as Inception BIBREF37 , and sequence-level features such as C3D BIBREF27 . However, unlike BIBREF30 who encode the textual information (question-answers pairs) using an LSTM, we chose instead to encode our textual information (action descriptions and their contexts) using a large-scale language model ELMo BIBREF38 .
> 
> Similar to previous research on multimodal methods BIBREF39 , BIBREF40 , BIBREF41 , BIBREF30 , we also perform feature ablation to determine the role played by each modality in solving the task. Consistent with earlier work, we observe that the textual modality leads to the highest performance across individual modalities, and that the multimodal model combining textual and visual clues has the best overall performance.

#### Relevance 885

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0098

Paper: FacTweet: Profiling Fake News Twitter Accounts

> How did they obtain the dataset?

### Common Retrieved Chunks

#### Passage 888

Retrieved by: BM25, Dense, Hybrid RRF

> they obtain a result near to the majority class ($0.18$). Another finding from our experiments shows that the performance of the Tweet2vec is weak. This demonstrates that tweets' hashtags are not informative to detect non-factual accounts. In Table TABREF25, we present ablation tests so as to quantify the contribution of subset of features. The results indicate that most performance gains come from words embeddings, style, and morality features. Other features (emotion and sentiment) show lower importance: nevertheless, they still improve the overall system performance (on average 0.35% Macro-F$_1$ improvement). These performance figures suggest that non-factual accounts use semantic and stylistic hidden signatures mostly while tweeting news, so as to be able to mislead the readers and behave as reputable (i.e., factual) sources. We leave a more fine-grained, diachronic analysis of semantic and stylistic features – how semantic and stylistic signature evolve across time and change across the accounts' timelines – for future work.

#### Relevance 888

Label: 

#### Passage 889

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> of tweets.
> 
> Top-$k$ replies, likes, or re-tweets: Some approaches in rumors detection use the number of replies, likes, and re-tweets to detect rumors BIBREF21. Thus, we extract top $k$ replied, liked or re-tweeted tweets from each account to assess the accounts factuality. We tested different $k$ values between 10 tweets to the max number of tweets from each account. Figure FIGREF24 shows the macro-F1 values for different $k$ values. It seems that $k=500$ for the top replied tweets achieves the highest result. Therefore, we consider this as a baseline.
> 
> Experimental Setup. We apply a 5 cross-validation on the account's level. For the FacTweet model, we experiment with 25% of the accounts for validation and parameters selection. We use hyperopt library to select the hyper-parameters on the following values: LSTM layer size (16, 32, 64), dropout ($0.0-0.9$), activation function ($relu$, $selu$, $tanh$), optimizer ($sgd$, $adam$, $rmsprop$) with varying the value of the learning rate (1e-1,..,-5), and batch size (4, 8, 16). The validation split is extracted on the class level using stratified sampling: we took a random 25% of the accounts from each class since the dataset is unbalanced. Discarding the classes' size in the splitting process may affect the minority classes (e.g. hoax). For the baselines' classifier, we tested many classifiers and the LR showed the best overall performance.
> 
> Results. Table TABREF25 presents the results. We present the results using a chunk size of 20, which was found to be the best size on the held-out data. Figure FIGREF24 shows the results of different chunks sizes. FacTweet performs better than the proposed baselines and obtains the highest macro-F1 value of $0.565$. Our results indicate the importance of taking into account the sequence of the tweets in the accounts' timelines. The sequence of these tweets is better captured by our proposed model sequence-agnostic or non-neural classifiers. Moreover, the results demonstrate that the features at tweet-level do not perform well to detect the Twitter accounts factuality, since they obtain a result near to the majority class ($0.18$). Another finding from our experiments shows that the performance of the Tweet2vec is weak. This demonstrates that tweets' hashtags are not informative to detect non-factual accounts. In Table TABREF25, we

#### Relevance 889

Label: 

#### Passage 890

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Social media platforms have made the spreading of fake news easier, faster as well as able to reach a wider audience. Social media offer another feature which is the anonymity for the authors, and this opens the door to many suspicious individuals or organizations to utilize these platforms. Recently, there has been an increased number of spreading fake news and rumors over the web and social media BIBREF0. Fake news in social media vary considering the intention to mislead. Some of these news are spread with the intention to be ironic or to deliver the news in an ironic way (satirical news). Others, such as propaganda, hoaxes, and clickbaits, are spread to mislead the audience or to manipulate their opinions. In the case of Twitter, suspicious news annotations should be done on a tweet rather than an account level, since some accounts mix fake with real news. However, these annotations are extremely costly and time consuming – i.e., due to high volume of available tweets Consequently, a first step in this direction, e.g., as a pre-filtering step, can be viewed as the task of detecting fake news at the account level.
> 
> The main obstacle for detecting suspicious Twitter accounts is due to the behavior of mixing some real news with the misleading ones. Consequently, we investigate ways to detect suspicious accounts by considering their tweets in groups (chunks). Our hypothesis is that suspicious accounts have a unique pattern in posting tweet sequences. Since their intention is to mislead, the way they transition from one set of tweets to the next has a hidden signature, biased by their intentions. Therefore, reading these tweets in chunks has the potential to improve the detection of the fake news accounts.
> 
> In this work, we investigate the problem of discriminating between factual and non-factual accounts in Twitter. To this end, we collect a large dataset of tweets using a list of propaganda, hoax and clickbait accounts and compare different versions of sequential chunk-based approaches using a variety of feature sets against several baselines. Several approaches have been proposed for news verification, whether in social media (rumors detection) BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, or in news claims BIBREF5, BIBREF6, BIBREF7, BIBREF8.

#### Relevance 890

Label: 

#### Passage 891

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Data. We build a dataset of Twitter accounts based on two lists annotated in previous works. For the non-factual accounts, we rely on a list of 180 Twitter accounts from BIBREF1. This list was created based on public resources where suspicious Twitter accounts were annotated with the main fake news types (clickbait, propaganda, satire, and hoax). We discard the satire labeled accounts since their intention is not to mislead or deceive. On the other hand, for the factual accounts, we use a list with another 32 Twitter accounts from BIBREF19 that are considered trustworthy by independent third parties. We discard some accounts that publish news in languages other than English (e.g., Russian or Arabic). Moreover, to ensure the quality of the data, we remove the duplicate, media-based, and link-only tweets. For each account, we collect the maximum amount of tweets allowed by Twitter API. Table TABREF13 presents statistics on our dataset.
> 
> Baselines. We compare our approach (FacTweet) to the following set of baselines:
> 
> [leftmargin=4mm]
> 
> LR + Bag-of-words: We aggregate the tweets of a feed and we use a bag-of-words representation with a logistic regression (LR) classifier.
> 
> Tweet2vec: We use the Bidirectional Gated recurrent neural network model proposed in BIBREF20. We keep the default parameters that were provided with the implementation. To represent the tweets, we use the decoded embedding produced by the model. With this baseline we aim at assessing if the tweets' hashtags may help detecting the non-factual accounts.
> 
> LR + All Features (tweet-level): We extract all our features from each tweet and feed them into a LR classifier. Here, we do not aggregate over tweets and thus view each tweet independently.
> 
> LR + All Features (chunk-level): We concatenate the features' vectors of the tweets in a chunk and feed them into a LR classifier.
> 
> FacTweet (tweet-level): Similar to the FacTweet approach, but at tweet-level; the sequential flow of the tweets is not utilized. We aim at investigating the importance of the sequential flow of tweets.
> 
> Top-$k$ replies, likes, or re-tweets: Some approaches in rumors detection use the number of replies, likes, and re-tweets to detect rumors BIBREF21. Thus, we extract top $k$ replied, liked or re-tweeted tweets from each account to assess the

#### Relevance 891

Label: 

#### Passage 892

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> emotion types from two available emotional lexicons. We use the NRC lexicon BIBREF10, which contains $\sim $14K words labeled using the eight Plutchik's emotions BIBREF11. The other lexicon is SentiSense BIBREF12 which is a concept-based affective lexicon that attaches emotional meanings to concepts from the WordNet lexical database. It has $\sim $5.5 words labeled with emotions from a set of 14 emotional categories We use the categories that do not exist in the NRC lexicon.
> 
> Sentiment: We extract the sentiment of the tweets by employing EffectWordNet BIBREF13, SenticNet BIBREF14, NRC BIBREF10, and subj_lexicon BIBREF15, where each has the two sentiment classes, positive and negative.
> 
> Morality: Features based on morality foundation theory BIBREF16 where words are labeled in one of the following 10 categories (care, harm, fairness, cheating, loyalty, betrayal, authority, subversion, sanctity, and degradation).
> 
> Style: We use canonical stylistic features, such as the count of question marks, exclamation marks, consecutive characters and letters, links, hashtags, users' mentions. In addition, we extract the uppercase ratio and the tweet length.
> 
> Words embeddings: We extract words embeddings of the words of the tweet using $Glove\-840B-300d$ BIBREF17 pretrained model. The tweet final representation is obtained by averaging its words embeddings.
> 
> Model. To account for chunk sequences we make use of a de facto standard approach and opt for a recurrent neural model using long short-term memory (LSTM) BIBREF18. In our model, the sequence consists of a sequence of tweets belonging to one chunk (Figure FIGREF11). The LSTM learns the hidden state $h\textsubscript {t}$ by capturing the previous timesteps (past tweets). The produced hidden state $h\textsubscript {t}$ at each time step is passed to the attention layer which computes a `context' vector $c\textsubscript {t}$ as the weighted mean of the state sequence $h$ by:
> 
> Where $T$ is the total number of timesteps in the input sequence and $\alpha \textsubscript {tj}$ is a weight computed at each time step $j$ for each state hj.

#### Relevance 892

Label: 

#### Passage 893

Retrieved by: Dense, Hybrid RRF

> Given a news Twitter account, we read its tweets from the account's timeline. Then we sort the tweets by the posting date in ascending way and we split them into $N$ chunks. Each chunk consists of a sorted sequence of tweets labeled by the label of its corresponding account. We extract a set of features from each chunk and we feed them into a recurrent neural network to model the sequential flow of the chunks' tweets. We use an attention layer with dropout to attend over the most important tweets in each chunk. Finally, the representation is fed into a softmax layer to produce a probability distribution over the account types and thus predict the factuality of the accounts. Since we have many chunks for each account, the label for an account is obtained by taking the majority class of the account's chunks.
> 
> Input Representation. Let $t$ be a Twitter account that contains $m$ tweets. These tweets are sorted by date and split into a sequence of chunks $ck = \langle ck_1, \ldots , ck_n \rangle $, where each $ck_i$ contains $s$ tweets. Each tweet in $ck_i$ is represented by a vector $v \in {\rm I\!R}^d$ , where $v$ is the concatenation of a set of features' vectors, that is $v = \langle f_1, \ldots , f_n \rangle $. Each feature vector $f_i$ is built by counting the presence of tweet's words in a set of lexical lists. The final representation of the tweet is built by averaging the single word vectors.
> 
> Features. We argue that different kinds of features like the sentiment of the text, morality, and other text-based features are critical to detect the nonfactual Twitter accounts by utilizing their occurrence during reporting the news in an account's timeline. We employ a rich set of features borrowed from previous works in fake news, bias, and rumors detection BIBREF0, BIBREF1, BIBREF8, BIBREF9.
> 
> [leftmargin=4mm]
> 
> Emotion: We build an emotions vector using word occurrences of 15 emotion types from two available emotional lexicons. We use the NRC lexicon BIBREF10, which contains $\sim $14K words labeled using the eight Plutchik's emotions BIBREF11. The other lexicon is SentiSense BIBREF12 which is a concept-based affective lexicon that attaches emotional

#### Relevance 893

Label: 

### BM25

None

### Dense

#### Passage 894

Retrieved by: Dense

> In this paper, we proposed a model that utilizes chunked timelines of tweets and a recurrent neural model in order to infer the factuality of a Twitter news account. Our experimental results indicate the importance of analyzing tweet stream into chunks, as well as the benefits of heterogeneous knowledge source (i.e., lexica as well as text) in order to capture factuality. In future work, we would like to extend this line of research with further in-depth analysis to understand the flow change of the used features in the accounts' streams. Moreover, we would like to take our approach one step further incorporating explicit temporal information, e.g., using timestamps. Crucially, we are also interested in developing a multilingual version of our approach, for instance by leveraging the now ubiquitous cross-lingual embeddings BIBREF22, BIBREF23.

#### Relevance 894

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 895

Retrieved by: Hybrid RRF followed by BGE reranking

> of sequential chunk-based approaches using a variety of feature sets against several baselines. Several approaches have been proposed for news verification, whether in social media (rumors detection) BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, or in news claims BIBREF5, BIBREF6, BIBREF7, BIBREF8. The main orientation in the previous works is to verify the textual claims/tweets but not their sources. To the best of our knowledge, this is the first work aiming to detect factuality at the account level, and especially from a textual perspective. Our contributions are:
> 
> [leftmargin=4mm]
> 
> We propose an approach to detect non-factual Twitter accounts by treating post streams as a sequence of tweets' chunks. We test several semantic and dictionary-based features together with a neural sequential approach, and apply an ablation test to investigate their contribution.
> 
> We benchmark our approach against other approaches that discard the chronological order of the tweets or read the tweets individually. The results show that our approach produces superior results at detecting non-factual accounts.

#### Relevance 895

Label: 

## Question 0099

Paper: Is change the only constant? Profile change perspective on #LokSabhaElections2019

> How do profile changes vary for influential leads and their followers over the social movement?

### Common Retrieved Chunks

#### Passage 896

Retrieved by: BM25, Hybrid RRF

> The role of Social Media during social movements have been studied very extensively BIBREF14, BIBREF18, BIBREF19, BIBREF15. With the help of Social Media, participation and ease to express oneself becomes easy BIBREF1. There have been many studies where Twitter has been used to gather the insight of online users in the form of tweets BIBREF1, BIBREF14, BIBREF15. The authors in BIBREF14 study the tweets to understand how people reacted to decriminalization of LGBT in India. The study of Gezi Park protest shows how the protest took a political turn, as people changed their usernames to show support to their political leaders BIBREF1.
> 
> The success of the party “Alternative for Deutschland(AFD)” in German Federal Elections, 2017 can be catered to its large online presence BIBREF18. The authors in BIBREF18 study the tweets and retweets networks during the German elections and analyze how users are organized into communities and how information flows between them. The role of influential leaders during elections has also been studied in detail in studies like BIBREF20. This brings us to the study of how influential leaders contribute to spread and adaptation of events.

#### Relevance 896

Label: 

#### Passage 897

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The real and virtual world are intertwined in a way that any speech, event, or action of leaders may trigger the changes is behavior of people online BIBREF1, BIBREF21. Opinion leaders have been defined as `the individuals who were likely to influence other persons in their immediate environment.' BIBREF22 Opinion leaders on social media platforms help in adoption of behavior by followers easily BIBREF9, BIBREF6. The performance and effectiveness of the opinion leader directly affect the contagion of the leader BIBREF9. On Twitter, opinion leaders show high motivation for information seeking and public expression. Moreover, they make a significant contribution to people's political involvement BIBREF21.
> 
> Our work contributes to this literature in two major ways. First, we investigate how profile attribute changes are similar or different from the influential leaders in the country and how much of these changes are the result of the same. Then we see how the users change their profile information in the midst of election in the largest democracy in the world.

#### Relevance 897

Label: 

#### Passage 898

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> To characterize the profile changing behavior amongst the followers , we study the profile snapshots of all the users in set $S$ over 9 snapshots.
> 
> Of all the active user accounts, $1,363,499$ users made at least one change to their profile attributes over all the snapshots. Thus, over $3\%$ of all the active users engaged in some form of profile change activity over the 9 snapshots. Of these $1,363,499$ users, more than $95\%$ of the users made only 1 change to their profile, and around 275 users made more than 20 changes. On an average, each one of these $1,363,499$ users made about 2 changes to their profiles with a standard deviation of $1.42$.
> 
> In order to compare the profile change behavior of political accounts and follower accounts, we analyzed the profile changes of set $\mathbf {P}$ over the 9 snapshots only. For the same 9 snapshots, $54.9\%$ of all users in set $\mathbf {P}$ made at least one change to their profile attributes. This is in sharp contrast to the the users of set $\mathbf {S}$, where only $3\%$ of users made any changes to their profile attributes. Similarly, users of set $\mathbf {P}$ made $75.32\%$ changes to their profiles on an average, which is 25 times more than the set $\mathbf {S}$.
> 
> INSIGHT 1: Political handles are more likely to engage in profile changing behavior as compared to their followers.
> 
> In Figure FIGREF15, we plot the number of changes in given attributes over all the snapshots for the users in set $S$. From this plot, we find that not all the attributes are modified at an equal rate. Profile image and Location are the most changed profile attributes and account for nearly $34\%$ and $25\%$ respectively of the total profile changes in our dataset. We analyze the trends in Figure FIGREF12 and find that the political handles do not change their usernames at all. This is in contrast to the trend in Figure FIGREF15 where we see that there are a lot of handles that change their usernames multiple times. The most likely reason for the same is that most of the follower handles are not verified and would not loose their verified

#### Relevance 898

Label: 

#### Passage 899

Retrieved by: BM25, Dense, Hybrid RRF

> To analyze the importance of user-profiles in elections, we need to distinguish between the profile change behavior of political accounts and follower accounts. This brings us to the first research question:
> 
> RQ1 [Comparison]: How often do political accounts and common user accounts change their profile information and which profile attributes are changed the most.
> 
> The political inclination of Twitter users can be classified based on the content of their past tweets and community detection methods BIBREF5. However, the same analysis has not been extended to the study of user-profiles in detail. We thus, study the following:
> 
> RQ2 [Political Inclination]: Do users reveal their political inclination on Twitter directly/indirectly using their user profiles only?
> 
> Behavior contagion is a phenomenon where individuals adopt a behavior if one of their opinion leaders adopts it BIBREF6. We analyze the profile change behavior of accounts based on the “Chowkidar” movement with the intent to find behavior contagion of an opinion leader. Thus, our third research question is:
> 
> RQ3 [Behavior Contagion]: Can profile change behavior be catered to behavior contagion effect where followers tend to adopt an opinion as their opinion leader adopts it?
> 
> We are interested in knowing the common attributes of the people who took part in the chowkidar movement. To characterize these users, we need to analyze the major topic patterns that these users engage in. Thus, we ask the question:
> 
> RQ4 [Topic Modelling]: What are the most discussed topics amongst the users that were part of the Chowkidar campaign?

#### Relevance 899

Label: 

#### Passage 900

Retrieved by: BM25, Hybrid RRF

> In summary, our main contributions are:
> 
> We collect daily and weekly profile snapshots of $1,293$ political handles on Twitter and over 55 million of their followers respectively over a period of two months during and after the #LokSabhaElections2019. We will make the data and code available on our website.
> 
> We analyze the political and follower handles for profile changes over the snapshots and show that the political handles engage in more profile change behavior. We also show that certain profile attributes are changed more frequently than others with subtle differences in the behavior of political and follower accounts.
> 
> We show users display support for a political party on Twitter through both organic means like party name mentions on their profile, and inorganic means such as showing support for a movement like #MainBhiChowkidar. We analyze the Chowkidar movement in detail and demonstrate that it illustrates a contagion behavior.
> 
> We perform topic modelling of the users who took part in the Chowkidar movement and show that they were most likely Narendra Modi supporters and mostly discussed political topics on Twitter.

#### Relevance 900

Label: 

#### Passage 901

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> In this section we characterize the profile change behavior of political accounts (Set $P$) and follower accounts (Set $S$).

#### Relevance 901

Label: 

### BM25

None

### Dense

#### Passage 902

Retrieved by: Dense

> Social Media profiles are a way to present oneself and to cultivate relationship with like minded or desired audience. BIBREF0, BIBREF12. With change in time and interest, users on Twitter change their profile names, description, screen names, location or language BIBREF2. Some of these changes are organic BIBREF13, BIBREF2, while other changes can be triggered by certain events BIBREF14, BIBREF15. In this section, we look into the previous literature which are related to user profile attribute's change behavior. We further look into how Twitter has been used to initiate or sustain movements BIBREF14, BIBREF15, BIBREF1. Finally we investigate how the contagion behavior adaptation spread through opinion leaders BIBREF6, BIBREF9 and conclude with our work's contribution to the literature.

#### Relevance 902

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 903

Retrieved by: Hybrid RRF followed by BGE reranking

> Change in an attribute in the profile involves replacing an existing attribute with a new one. We analyze the similarity between the current, new display names and usernames used by users in set $\mathbf {P}$ and $\mathbf {S}$ respectively. For this analysis, we consider only the users who have changed their username or display name at least once in all 9 snapshots. We use the Longest Common Subsequence (LCS) to compute the similarity between two strings. Thus, for each user, we compute the average LCS score between all possible pairs of unique display names and usernames adopted by them. A high average LCS score indicates that the newer username or display name were not significantly different from the previous ones.
> 
> The graph in Figure FIGREF18 shows that nearly $80\%$ of the users in set $S$ made more significant changes to their Display Names as compared to the political handles. (This can be seen by considering a horizontal line on the graph. For any given fraction of users, the average LCS score of set $S$ (Followers) is lesser than set $P$ (Politicians) for approximately $80\%$ percent of users). For around $10\%$ of the users in set $P$, the new and old profile attributes were unrelated (LCS score < $0.5$) and for users in set $S$, this value went up to $30\%$.
> 
> INSIGHT 3: Political handles tend to make new changes related to previous attribute values. However, the followers make comparatively less related changes to previous attribute values.

#### Relevance 903

Label: 

#### Passage 904

Retrieved by: Hybrid RRF followed by BGE reranking

> Increase in the Internet user-base and widespread adoption of smartphones in the country has led to an increase in the importance of social media campaigns during the elections. This is evident by the fact that in our dataset (Set $U$), we found that a total of 54 handles got verified throughout 61 snapshots. Moreover the average number of followers of handles in set $P$ increased from $3,08,716.84$ to $3,19,881.09$ over the 61 snapshots. Given that the average followers of set $P$ increased by approximately $3\%$ and 54 profile handles got verified in the span of 61 days, we believe that efforts of leaders on social media campaign can't be denied.
> 
> We consider 5 major profile attributes for further analysis. These attributes are username, display name, profile image, location and description respectively. The username is a unique handle or screen name associated with each twitter user that appears on the profile URL and is used to communicate with each other on Twitter. Some username examples are $@narendramodi$, $@RahulGandhi$ etc. The display name on the other hand, is merely a personal identifier that is displayed on the profile page of a user, e.g. `Narendra Modi', `Rahul Gandhi', etc. The description is a string to describe the account, while the location is user-defined profile location. We considered the 5 profile attributes as stated above since these attributes are key elements of a users identity and saliently define users likes and values BIBREF2.
> 
> For the set of users in $P$, the total number of changes in these 5 profile attributes over 61 snapshots is 974. Figure FIGREF12 shows the distribution of profile changes for specific attributes over all the 61 snapshots. The most changed attribute among the political handles is the profile image followed by display name. In the same Figure, there is a sharp increase in the number of changes to the display name attribute on 23rd May, 2019. The increase is because @narendramodi removed Chowkidar from the display name of his Twitter handle which resulted in many other political handles doing the same. Another interesting trend is that none of the handles changed their username over all the snapshots. This could be attributed to the fact that

#### Relevance 904

Label: 

## Question 0100

Paper: autoNLP: NLP Feature Recommendations for Text Analytics Applications

> How this system recommend features for the new application?

### Common Retrieved Chunks

#### Passage 905

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Figure FIGREF23 depicts overall process flow for enabling automated feature recommendations.
> 
> For a new text analytics application requiring feature engineering, it starts with estimating its semantic proximity (from the perspective of a NLP data scientist) with existing applications with known features. Based upon these proximity estimates as well as expected relevance of features for existing applications, system would recommend features for the new application in a ranked order. Furthermore, if user's selections are not aligned with system's recommendations, system gradually adapts its recommendation so that eventually it can achieve alignment with user preferences.
> 
> Towards that let us start with characterizing text analytics applications. A TA application's details should include following fields:
> 
> Text based description of an TA application (or problem). For example, “identify medical procedures being referenced in a discharge summary” or “what are the input and output entities mentioned in a software requirements specification”.
> 
> Analysis unit at which features are to be specified and training annotations are available, and ML model is designed to give outcomes. Options include word, phrase, sentence, paragraph, or document.
> 
> Specifies technical classification of the underlying ML challenge with respect to a well-defined ontology. E.g., Classification (with details), Clustering, etc.
> 
> Specifies how performance of the ML model is to be measured - again should be specified as per some well defined ontology.
> 
> Knowledge base of text analytics applications contains details for text analytics applications in above specified format. Each application is further assumed to be associated with a set of Features (or feature types) specified in nlpFSpL together with their relevance scores against a performance metric. Relevance score of a feature is a measure of the extent to which this feature contributes to achieve overall performance of ML model while solving the underlying application. Relevance score may be estimated using any of the known feature selection metrics BIBREF25.
> 
> To specify knowledge base formally, let us assume that there are $m$ different applications and $k$ unique feature specifications across these applications applying same performance metric. Let us denote these as follows: $APPS=\lbrace App_1,\ldots , App_m\rbrace $ and ${\mathit {\Theta }}_F$ = $\left\lbrace F_1,F_2,\dots ,F_k\right\rbrace $ respectively. Knowledge base is then represented as a feature co-occurrence matrix $PF_{m\times k}$ such that $PF[i,j]

#### Relevance 905

Label: 

#### Passage 907

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> There are two different modes in which user may provide feedback to the system with respect to recommended features: one where it ranks features differently and second where user provides different relevance scores (e.g., based upon alternate design or by applying feature selection techniques). Aim is to use these feed-backs to learn an updated similarity scoring function $\Delta _{new}:APPS \times APPS$ $\rightarrow $ $[0,1]$.
> 
> In relation to $NewP$, let $Rank:{\mathrm {\Theta }}_F\times \left\lbrace system,user\right\rbrace \rightarrow \lbrace 1,\dots ,k\rbrace ~$ return rank of a feature and $Rel:{\mathrm {\Theta }}_F\times \left\lbrace system,user\right\rbrace \rightarrow [0,1]$ return relevance score of a feature based upon type – `system' or `user'.
> 
> Next, for each $App\in APPS$, let ${Ch}\left[App\right]$ $\leftarrow $ $\emptyset $ be a hash table with keys as application ids and values as list of numbers estimated next. Also let $NewSim_{FE}\left[.\right]\leftarrow 0$ contain updated similarity scores between $NewP$ and existing applications in $APPS$.
> 
> For each feature specification $f\in \Theta _F$, determine whether `user' given rank is different from `system' given rank, i.e., $Rank(f,`system^{\prime }) \ne Rank(f,`user^{\prime })$. If so, execute steps next.
> 
> Let $\mathit {Bind}(f_j) \subseteq APPS$ be the list of applications, which contributed in estimating collective relevance for feature $f_j \in \Theta _F$. For example, when aggressive or conservative policy is considered, $\mathit {Bind}(f_j)$ = $\lbrace App_r \mid Relevance(NewP,f_j)$ = $\mathit {NorSim[r,j]}\rbrace $.
> 
> For each $App_i\in Bind\left(f_j\right)$: Add $x$ to $Ch[App_i]$, where $x$ is estimated as follows: If user provides explicit relevance scores for $App_i$,
> 
> Otherwise if user re-ranks features
> 
> For each $App_i\in Bind\left(f_j\right)$: $NewSim_{FE}\left[App_i\right]\leftarrow Average(Ch[App_i])$. If $|NewSim_{FE}[App_i]$-${\alpha }_i|$ $\ge \epsilon {\alpha }_i$ i.e., when the difference between old and new similarity scores is more than $\epsilon $ fraction of original similarity, add $(\Delta (NewP,App_i),NewSim_{FE}[App_i])$ to training set $Tr_{rpls}$ so that it used to train a regression model for $\Delta _{new}(.,.)$ by applying partial recursive PLS BIBREF28 with $\Delta (NewP,App_i)$ as set of predictor or independent variables and $NewSim_{FE}[App_i]$ as response variable. Existing proximity scores between applications in $APPS$ (ref. Section SECREF31) are also added to training set $Tr_{rpls}$ before generating the regression model.
> 
> Note that $\epsilon $ is a small fraction $>$ 0 which controls when should similarity model be retrained. For example, $\epsilon = 0.05$ would imply

#### Relevance 907

Label: 

#### Passage 908

Retrieved by: BM25, Hybrid RRF

> Figure FIGREF1 depicts typical design life cycle of a (traditional) ML based solution for the TA applications, which involves steps to manually define relevant features and implement code components to extract those feature from input text corpus during training, validation, testing and actual usage of the application. In traditional ML based solutions, feature interactions also need to be explicitly specified, though this step is largely automated when using deep neural network based solutions BIBREF9.
> 
> As the process of defining features is manual, prior experience and expertize of the designer affects which features to extract and how to extract these features from input text. Current practice lacks standardization and automation in feature definition process, provides partial automation in extraction process, and does not enable automated reuse of features across related application.
> 
> Next, let us consider scenarios when features are specified as elements of a language. Let us refer to this language as NLP Feature Specification Language (nlpFSpL) such that a program in nlpFSpL would specify which features should be used by the underlying ML based solution to achieve goals of the target application. Given a corpus of unstructured natural language text data and a specifications in the nlpFSpL, an interpreter can be implemented as feature extraction system (FExSys) to automatically generate feature matrix which can be directly used by underlying ML technique.
> 
> In contrast to the life-cycle view in the Figure FIGREF1, this would result into refined solution life cycle of ML based TA applications as depicted in the Figure FIGREF2.

#### Relevance 908

Label: 

#### Passage 909

Retrieved by: BM25, Dense

> Let $NewP$ be new application for which features need to be specified in nlpFSpL. Represent fields of $NewP$ similar to existing applications in the knowledge base (as described earlier in the Section SECREF30).
> 
> Next, create a degree-1 ego-similarity network for $NewP$ to represent how close is $NewP$ with existing applications in $APPS$. Let this be represented as a diagonal matrix $\Delta _{m\times m}$ such that $\Delta [r,r] = \alpha _i =$ proximity between $NewP$ and $i^{th}$ application in the knowledge base (by applying steps in the Section SECREF31).
> 
> Thereafter, let $NorSim_{m\times k}=\Delta _{m\times m} \times PF_{m \times k}$ such that $NorSim[i,j]= \alpha _i \delta _{i,F_j}$ measures probable relevance of feature $F_j$ for $NewP$ w.r.t. performance metric $M$ based upon its relevance for $App_i \in APPS$. When there are multiple applications in $APPS$, we need to define a policy to determine collective probable relevance of a feature specification in $\mathit {\Theta }_F$ for $NewP$ based upon its probable relevance scores with respect to different applications.
> 
> To achieve that, let $Relevance$ $(NewP, f_j)$ be the relevance of $f_j$ for $NewP$ based upon a policy, which can be estimated in different ways including following:
> 
> Next, consider there different example policies:
> 
> Weakest relevance across applications is considered: $Relevance(NewP,F_j) = \min _{i\in 1..m}{NorSim[i,j]}$
> 
> Strongest relevance across applications is considered: $Relevance(NewP,F_j) = \max _{i\in 1..m}{NorSim[i,j]}$
> 
> Most likely relevance across applications is considered: $Relevance(NewP,F_j) = \frac{1}{m}\Sigma _{i\in 1..m}{NorSim[i,j]}$
> 
> Rank feature specifications in $\mathit {\Theta }_F$ decreasing order based upon $Relevance(NewP,.)$, which are suggested to the NLP Data Scientist together with the supporting evidence.

#### Relevance 909

Label: 

#### Passage 910

Retrieved by: Dense, Hybrid RRF

> In this paper, we have presented high level overview of a feature specification language for ML based TA applications and an approach to enable reuse of feature specifications across semantically related applications. Currently, there is no generic method or approach, which can be applied during TA applications' design process to define and extract features for any arbitrary application in an automated or semi-automated manner primarily because there is no standard way to specify wide range of features which can be extracted and used. We considered different classes of features including linguistic, semantic, and statistical for various levels of analysis including words, phrases, sentences, paragraphs, documents, and corpus. As a next step, we presented an approach for building a recommendation system for enabling automated reuse of features for new application scenarios which improves its underlying similarity model based upon user feedback.
> 
> To take this work forward, it is essential to have it integrated to a ML platform, which is being used by large user base for building TA applications so that to be able to populate a repository of statistically significant number of TA applications with details as specified in Section SECREF5 and thereafter refine the proposed approach so that eventually it rightly enables reuse of features across related applications.

#### Relevance 910

Label: 

#### Passage 911

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> it is possible that that these features might have been identified independently. This, in turn, supports the hypothesis that if adequate details of any one or two of these applications are fed to a system described in this work, which is designed to estimate semantic similarities across applications, system can automatically suggest potential features for consideration for the remaining applications to start with without requiring manual knowledge of the semantically related applications.

#### Relevance 911

Label: 

### BM25

#### Passage 906

Retrieved by: BM25

> Figure FIGREF8 depicts two levels of taxonomy for features considered as linguistic.
> 
> To illustrate, let us consider context based features: Table FIGREF9 gives various options which need to be specified for directing how context for an SU should be extracted. For example, Context_Window := [2, Sentence] will extract all tokens within current sentence, which are present within a distance of 2 on both sides from the current SU. However, Context_Window := [2, Sentence]; POSContext := NN$\mid $VB will extract only those tokens within current sentence, which are present within a distance of 2 on both sides from the current SU and have POS tag either NN (noun singular) or VB (verb, base form).
> 
> Table FIGREF10 illustrates how to specify the way head directionality of current SU should be extracted.

#### Relevance 906

Label: 

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 912

Retrieved by: Hybrid RRF followed by BGE reranking

> feature engineering. We start with an outline of a language for expressing NLP features abstracting over the feature extraction process, which often implicitly captures intent of the NLP data scientist to extract specific features from given input text. We next discuss a method to enable automated reuse of features across semantically related applications when a corpus of feature specifications for related applications is available. Proposed language and system would help achieving reduction in manual effort towards design and extraction of features, would ensure standardization in feature specification process, and could enable effective reuse of features across similar and/or related applications.

#### Relevance 912

Label: 

#### Passage 913

Retrieved by: Hybrid RRF followed by BGE reranking

> To begin, for each text based field in each TA application, pre-process text and perform term normalization (i.e., replacing all equivalent terms with one representative term in the whole corpus) including stemming, short-form and long-form (e.g., ‘IP’ and ‘Intellectual Property’), language thesaurus based synonyms (e.g., WordNet based `goal' and `objective').

#### Relevance 913

Label: 
