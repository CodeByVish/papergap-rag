# Passage relevance annotation

Annotator: 

Enter your name or agreed identifier after `Annotator:`.

Judge whether each passage helps answer the question, including useful partial evidence. Topic overlap alone is insufficient.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Preserve all content and record numbers. Work independently; do not exchange labels before submission. Algorithm sources are disclosed.

## Question 0021

Paper: BERT-Based Multi-Head Selection for Joint Entity-Relation Extraction

> How is BERT optimized for this task?

### Common Retrieved Chunks

#### Passage 180

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> and relation extraction simultaneously, without the need of any manually extracted features or the use of any external tool. They model the entity recognition task using a CRF (Conditional Random Fields) layer and the relation extraction task as a multi-head selection problem since one entity can have multiple relations. The model adopted BiLSTM to extract contextual feature and propose a label embedding layer to connect the entity recognition branch and the relation classification branch. Our model is based on this framework and make three improvements:
> 
> (1) BERT BIBREF14 is introduced as a feature extraction layer in place of BiLSTM. We also optimize the pre-training process of BERT by introducing a semantic-enhanced task.
> 
> (2) A large-scale Baidu Baike corpus is introduced for entity recognition pre-training, which is of weekly supervised learning since there is no actual named entity label.
> 
> (3) Soft label embedding is proposed to effectively transmit information between entity recognition and relation extraction.

#### Relevance 180

Label: 

#### Passage 181

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> NER (Named Entity Recognition) is the first task in the joint multi-head selection model. It is usually formulated as a sequence labeling problem using the BIO (Beginning, Inside, Outside) encoding scheme. Since there are different entity types, the tags are extended to B-type, I-type and O. Linear-chain CRF BIBREF15 is widely used for sequence labeling in deep models. In our method, CRF is built on the top of BERT. Supposed $y\in {\left\lbrace B-type,I-type,O \right\rbrace }$ is the label, score function $ s(X,i)_{y_{i}} $ is the output of BERT at $ i_{th}$ character and $ b_{y_{i-1}y_{i}} $ is trainable parameters, the probability of a possible label sequence is formalized as:
> 
> By solving Eq DISPLAY_FORM11 we can obtain the optimal sequence tags:

#### Relevance 181

Label: 

#### Passage 182

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Original google BERT is pre-trained using two unsupervised tasks, masked language model (MLM) and next sentence prediction (NSP). MLM task enables the model to capture the discriminative contextual feature. NSP task makes it possible to understand the relationship between sentence pairs, which is not directly captured by language modeling. We further design a semantic-enhanced task to enhance the performance of BERT. It incorporate previous sentence prediction and document level prediction. We pre-train BERT by combining MLM, NSP and the semantic-enhanced task together.

#### Relevance 182

Label: 

#### Passage 184

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> BERT (Bidirectional Encoder Representations from Transformers) BIBREF14 is a new language representation model, which uses bidirectional transformers to pre-train a large unlabeled corpus, and fine-tunes the pre-trained model on other tasks. BERT has been widely used and shows great improvement on various natural language processing tasks, e.g., word segmentation, named entity recognition, sentiment analysis, and question answering. We use BERT to extract contextual feature for each character instead of BiLSTM in the original work BIBREF13. To further improve the performance, we optimize the pre-training process of BERT by introducing a semantic-enhanced task.

#### Relevance 184

Label: 

#### Passage 186

Retrieved by: Dense, Hybrid RRF

> In this paper, we report our solution to the information extraction task in 2019 Language and Intelligence Challenge. We first analyze the problem and find that most entities are involved in multiple triplets. To solve this problem, we incorporate BERT into the multi-head selection framework for joint entity-relation extraction. Enhanced BERT pre-training, soft label embedding and NER pre-training are three main technologies we introduce to further improve the performance. Experimental results show that our method achieves competitive performance: F1 score 0.892 (1st place) on the test set 1 and F1 score 0.8924 (2nd place) on the test set 2.

#### Relevance 186

Label: 

### BM25

#### Passage 183

Retrieved by: BM25

> Two examples of our model fail to predict are shown in figure FIGREF32. For example 1, the triplet can not be drawn from the given sentence. However, the triplet is actually in the trainset. Our model may overfit to the trainset in this situation. For example 2, there is complicate family relationships mentioned in the sentence, which is too hard for the model to capture. To solve this problem, a more robust model should be proposed and we leave this as future work.

#### Relevance 183

Label: 

### Dense

#### Passage 185

Retrieved by: Dense

> Results on SKE dataset are presented in Table 1. The baseline model is based on the Google BERT, use hard label embedding and train on only SKE dataset without NER pretraining. As shown in table 1, the F1 score increase from 0.864 to 0.871 when combined with our enhanced BERT. NER pretraining using the extra corpus, soft label embedding and auxiliary sentence-level relation classification prediction also improve the F1 score. Combined all of these contributions, we achieve F1-score 0.876 with the single model on test set 1.

#### Relevance 185

Label: 

#### Passage 187

Retrieved by: Dense

> We select the following four variant model to further conduct model ensembling. The ensemble model is XGBoost binary classifier, which is very fast during training. Since the base models are trained on the training set, we perform cross-validation on development set, figure FIGREF29 shows the PR curve of the ensemble model. By model ensembling the F1 score increase from 0.876 to 0.892.
> 
> $\cdot $ Google BERT + Soft Label Embedding + Global Relation Prediction
> 
> $\cdot $ Enhanced BERT + Soft Label Embedding + Global Relation Prediction
> 
> $\cdot $ Google BERT + Soft Label Embedding + Global Relation Prediction + NER Pretraining
> 
> $\cdot $ Enhance BERT + Soft Label Embedding + Global Relation Prediction + NER Pretraining

#### Relevance 187

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 188

Retrieved by: Hybrid RRF followed by BGE reranking

> Figure FIGREF6 summarizes the proposed model architecture. The model takes character sequence as input and captures contextual features using BERT. A CRF layer is applied to extract entities from the sentence. To effectively transmit information between entity recognition and relation extraction, soft label embedding is built on the top of CRF logits. To solve the problem that one entity belongs to multiple triplets, a multi-sigmoid layer is applied. We find that adding an auxiliary global relation prediction task also improve the performance.

#### Relevance 188

Label: 

## Question 0022

Paper: State-of-the-Art Vietnamese Word Segmentation

> What are the limitations of existing Vietnamese word segmentation systems?

### Common Retrieved Chunks

#### Passage 189

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> This study reviewed state-of-the-art approaches and systems of Vietnamese word segmentation. The review pointed out common features and methods used in Vietnamese word segmentation studies. This study also had an evaluation of the existing Vietnamese word segmentation toolkits based on a same corpus to show advantages and disadvantages as to shed some lights on system enhancement.
> 
> There are several challenges on supervised learning approaches in future work. The first challenge is to acquire very large Vietnamese corpus and to use them in building a classifier, which could further improve accuracy. In addition, applying linguistics knowledge on word context to extract useful features also enhances prediction performance. The second challenge is design and development of big data warehouse and analytic framework for Vietnamese documents, which corresponds to the rapid and continuous growth of gigantic volume of articles and/or documents from Web 2.0 applications, such as, Facebook, Twitter, and so on. It should be addressed that there are many kinds of Vietnamese documents, for example, Han - Nom documents and old and modern Vietnamese documents that are essential and still needs further analysis. According to our study, there is no a powerful Vietnamese language processing used for processing Vietnamese big data as well as understanding such language. The final challenge relates to building a system, which is able to incrementally learn new corpora and interactively process feedback. In particular, it is feasible to build an advance NLP system for Vietnamese based on Hadoop platform to improve system performance and to address existing limitations.

#### Relevance 189

Label: 

#### Passage 190

Retrieved by: BM25, Dense, Hybrid RRF

> has the most studies on the word segmentation issue. However, there is a lack of survey of word segmentation studies on Asian languages and Vietnamese as well. This paper aims reviewing state-of-the-art word segmentation approaches and systems applying for Vietnamese. This study will be a foundation for studies on Vietnamese word segmentation and other following Vietnamese tasks as well, such as part-of-speech tagger, chunker, or parser systems.
> 
> There are several studies about the Vietnamese word segmentation task over the last decade. Dinh et al. started this task with Weighted Finite State Transducer (WFST) approach and Neural Network approach BIBREF9 . In addition, machine learning approaches are studied and widely applied to natural language processing and word segmentation as well. In fact, several studies used support vector machines (SVM) and conditional random fields (CRF) for the word segmentation task BIBREF7 , BIBREF8 . Based on annotated corpora and token-based features, studies used machine learning approaches to build word segmentation systems with accuracy about 94%-97%.
> 
> According to our observation, we found that is lacks of complete review approaches, datasets and toolkits which we recently used in Vietnamese word segmentation. A all sided review of word segmentation will help next studies on Vietnamese natural language processing tasks have an up-to-date guideline and choose the most suitable solution for the task. The remaining part of the paper is organized as follows. Section II discusses building corpus in Vietnamese, containing linguistic issues and the building progress. Section III briefly mentions methods to model sentences and text in machine learning systems. Next, learning models and approaches for labeling and segmenting sequence data will be presented in Section IV. Section V mainly addresses two existing toolkits, vnTokenizer and JVnSegmenter, for Vietnamese word segmentation. Several experiments based on mentioned approaches and toolkits are described in Section VI. Finally, conclusions and future works are given in Section VII.

#### Relevance 190

Label: 

#### Passage 191

Retrieved by: BM25, Dense, Hybrid RRF

> This research gathers the results of Vietnamese word segmentation of several methods into one table as show in Table II. It is noted that they are not evaluated on a same corpus. The purpose of the result illustration is to provide an overview of the results of current Vietnamese word segmentation systems based on their individual features. All studies mentioned in the table have accuracy around 94-97% based on their provided corpus.
> 
> This study also evaluates the Vietnamese word segmentation based on existing toolkits using the same annotated Vietnamese word segmentation corpus. There are two available toolkits to evaluate and to segment. To be neutral to both toolkits, we use the EVBNews Vietnamese corpus, a part of EVBCorpus, to evaluate Vietnamese word segmentation. The EVBNews corpus contains over 45,000 segmented Vietnamese sentences extracted from 1,000 general news articles (as shown in Table III) BIBREF16 . We used the same training set which has 1000 files and 45,531 sentences. vnTokenizer outputs 831,455 Vietnamese words and 1,206,475 tokens. JVnSegmenter outputs 840,387 words and 1,201,683. We correct tags (BIO), and compare to previous outputs, we have rate from vnTokenizer is 95.6% and from JVnsegmenter is 93.4%. The result of both vnTokenizer and JVnSegmenter testing on the EVBNews Vietnamese Corpus are provided in Table IV.

#### Relevance 191

Label: 

#### Passage 192

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> There are several studies for Vietnamese Word Segmentation during last decade. For instance, Dinh et al. started the word segmentation task for Vietnamese with Neural Network and Weighted Finite State Transducer (WFST) BIBREF9 . Nguyen et al. continued with machine learning approaches, Conditional Random Fields and Support Vector Machine BIBREF7 . Most of statistical approaches are based on the architecture as shown in Figure 2. According to the architecture, recent studies and systems focus on either improving or modifying difference learning models to get the highest accuracy. Features used in word segmentation systems are syllable, dictionary, and entity name. The detail of all widely used techniques applied are collected and described in following subsections.

#### Relevance 192

Label: 

#### Passage 193

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Lexical analysis, syntactic analysis, semantic analysis, disclosure analysis and pragmatic analysis are five main steps in natural language processing BIBREF0 , BIBREF1 . While morphology is a basic task in lexical analysis of English, word segmentation is considered a basic task in lexical analysis of Vietnamese and other East Asian languages processing. This task is to determine borders between words in a sentence. In other words, it is segmenting a list of tokens into a list of words such that words are meaningful.
> 
> Word segmentation is the primary step in prior to other natural language processing tasks i. e., term extraction and linguistic analysis (as shown in Figure 1). It identifies the basic meaningful units in input texts which will be processed in the next steps of several applications. For named entity recognization BIBREF2 , word segmentation chunks sentences in input documents into sequences of words before they are further classified in to named entity classes. For Vietnamese language, words and candidate terms can be extracted from Vietnamese copora (such as books, novels, news, and so on) by using a word segmentation tool. Conformed features and context of these words and terms are used to identify named entity tags, topic of documents, or function words. For linguistic analysis, several linguistic features from dictionaries can be used either to annotating POS tags or to identifying the answer sentences. Moreover, language models can be trained by using machine learning approaches and be used in tagging systems, like the named entity recognization system of Tran et al. BIBREF2 .
> 
> Many studies forcus on word segmentation for Asian languages, such as: Chinese, Japanese, Burmese (Myanmar) and Thai BIBREF3 , BIBREF4 , BIBREF5 , BIBREF6 . Approaches for word segmentation task are variety, from lexicon-based to machine learning-based methods. Recently, machine learning-based methods are used widely to solve this issue, such as: Support Vector Machine or Conditional Random Fields BIBREF7 , BIBREF8 . In general, Chinese is a language which has the most studies on the word segmentation issue. However, there is a lack of survey of word segmentation studies on Asian languages and Vietnamese as well. This paper aims reviewing state-of-the-art word segmentation approaches and systems applying for Vietnamese.

#### Relevance 193

Label: 

### BM25

None

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 194

Retrieved by: Hybrid RRF followed by BGE reranking

> vnTokenizer and JVnSegmenter are two famous segmentation toolkits for Vietnamese word segmentation. Both two word segmentation toolkits are implemented the word segmentation data process in Figure 2. This section gives more details of these Vietnamese word toolkits.

#### Relevance 194

Label: 

#### Passage 195

Retrieved by: Hybrid RRF followed by BGE reranking

> In Vietnamese, not all of meaningful proper names are in the dictionary. Identifying proper names in input text are also important issue in word segmentation. This issue is sometimes included into unknown word issue to be solved. In addition, named entity recognition has to classify it into several types such as person, location, organization, time, money, number, and so on.
> 
> Proper name identification can be solved by characteristics. For example, systems use beginning characters of proper names which are uppercase characters. Moreover, a list of proper names is also used to identify names in the text. In particular, a list of 2000 personal names extracted from VietnamGiaPha, and a list of 707 names of locations in Vietnam extracted from vi.wikipedia.org are used in the study of Nguyen et al. for Vietnamese word segmentation BIBREF7 .

#### Relevance 195

Label: 

## Question 0023

Paper: Improving Neural Text Simplification Model with Simplified Corpora

> what are the sizes of both datasets?

### Common Retrieved Chunks

#### Passage 197

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this paper, we propose one simple method to use simplified corpora during training of NMT systems, with no changes to the network architecture. In the experiments on two datasets, we achieve substantial gains in all tasks, and new SOTA results, via back-translation of simplified sentences into the ordinary sentences, and treating this synthetic data as additional training data. Because we do not change the neural network architecture to integrate simplified corpora, our method can be easily applied to other Neural Text Simplification (NTS) systems. We expect that the effectiveness of our method not only varies with the quality of the NTS system used for back-translation, but also depends on the amount of available parallel and simplified corpora. In the paper, we have only utilized data from Wikipedia for simplified sentences. In the future, many other text sources are available and the impact of not only size, but also of domain should be investigated.

#### Relevance 197

Label: 

#### Passage 198

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We evaluate the performance of text simplification using neural machine translation on available parallel sentences and additional simplified sentences.
> 
> Dataset. We use two simplification datasets (WikiSmall and WikiLarge). WikiSmall consists of ordinary and simplified sentences from the ordinary and simple English Wikipedias, which has been used as benchmark for evaluating text simplification BIBREF17 , BIBREF18 , BIBREF8 . The training set has 89,042 sentence pairs, and the test set has 100 pairs. WikiLarge is also from Wikipedia corpus whose training set contains 296,402 sentence pairs BIBREF19 , BIBREF20 . WikiLarge includes 8 (reference) simplifications for 2,359 sentences split into 2,000 for development and 359 for testing.
> 
> Metrics. Three metrics in text simplification are chosen in this paper. BLEU BIBREF5 is one traditional machine translation metric to assess the degree to which translated simplifications differed from reference simplifications. FKGL measures the readability of the output BIBREF23 . A small FKGL represents simpler output. SARI is a recent text-simplification metric by comparing the output against the source and reference simplifications BIBREF20 .
> 
> We evaluate the output of all systems using human evaluation. The metric is denoted as Simplicity BIBREF8 . The three non-native fluent English speakers are shown reference sentences and output sentences. They are asked whether the output sentence is much simpler (+2), somewhat simpler (+1), equally (0), somewhat more difficult (-1), and much more difficult (-2) than the reference sentence.
> 
> Methods. We use OpenNMT BIBREF24 as the implementation of the NMT system for all experiments BIBREF5 . We generally follow the default settings and training procedure described by Klein et al.(2017). We replace out-of-vocabulary words with a special UNK symbol. At prediction time, we replace UNK words with the highest probability score from the attention layer. OpenNMT system used on parallel data is the baseline system. To obtain a synthetic parallel training set, we back-translate a random sample of 100K sentences from the collected simplified corpora. OpenNMT used on parallel data and synthetic data is our model. The benchmarks are run on a Intel(R) Core(TM) i7-5930K CPU@3.50GHz, 32GB Mem, trained on 1 GPU GeForce GTX 1080 (Pascal) with CUDA v. 8.0.
> 
> We choose three statistical text simplification systems. PBMT-R is a phrase-based method with a

#### Relevance 198

Label: 

#### Passage 199

Retrieved by: BM25, Hybrid RRF

> models can be typically improved when trained on more data. Therefore, we expect simplified corpora to be especially helpful for NMT models.
> 
> In contrast to previous work, which uses the existing NMT models, we explore strategy to include simplified training corpora in the training process without changing the neural network architecture. We first propose to pair simplified training sentences with synthetic ordinary sentences during training, and treat this synthetic data as additional training data. We obtain synthetic ordinary sentences through back-translation, i.e. an automatic translation of the simplified sentence into the ordinary sentence BIBREF11 . Then, we mix the synthetic data into the original (simplified-ordinary) data to train NMT model. Experimental results on two publicly available datasets show that we can improve the text simplification quality of NMT models by mixing simplified sentences into the training set over NMT model only using the original training data.

#### Relevance 199

Label: 

#### Passage 201

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We collected a simplified dataset from Simple English Wikipedia that are freely available, which has been previously used for many text simplification methods BIBREF0 , BIBREF10 , BIBREF3 . The simple English Wikipedia is pretty easy to understand than normal English Wikipedia. We downloaded all articles from Simple English Wikipedia. For these articles, we removed stubs, navigation pages and any article that consisted of a single sentence. We then split them into sentences with the Stanford CorNLP BIBREF21 , and deleted these sentences whose number of words are smaller than 10 or large than 40. After removing repeated sentences, we chose 600K sentences as the simplified data with 11.6M words, and the size of vocabulary is 82K.

#### Relevance 201

Label: 

#### Passage 202

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> for text simplification task, and achieved good results BIBREF8 , BIBREF4 , BIBREF20 . The main limitation of the aforementioned NMT models for text simplification depended on the parallel ordinary-simplified sentence pairs. Because ordinary-simplified sentence pairs are expensive and time-consuming to build, the available largest data is EW-SEW that only have 296,402 sentence pairs. The dataset is insufficiency for NMT model if we want to NMT model can obtain the best parameters. Considering simplified data plays an important role in boosting fluency for phrase-based text simplification, and we investigate the use of simplified data for text simplification. We are the first to show that we can effectively adapt neural translation models for text simplifiation with simplified corpora.

#### Relevance 202

Label: 

#### Passage 204

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> our model. The benchmarks are run on a Intel(R) Core(TM) i7-5930K CPU@3.50GHz, 32GB Mem, trained on 1 GPU GeForce GTX 1080 (Pascal) with CUDA v. 8.0.
> 
> We choose three statistical text simplification systems. PBMT-R is a phrase-based method with a reranking post-processing step BIBREF18 . Hybrid performs sentence splitting and deletion operations based on discourse representation structures, and then simplifies sentences with PBMT-R BIBREF25 . SBMT-SARI BIBREF19 is syntax-based translation model using PPDB paraphrase database BIBREF26 and modifies tuning function (using SARI). We choose two neural text simplification systems. NMT is a basic attention-based encoder-decoder model which uses OpenNMT framework to train with two LSTM layers, hidden states of size 500 and 500 hidden units, SGD optimizer, and a dropout rate of 0.3 BIBREF8 . Dress is an encoder-decoder model coupled with a deep reinforcement learning framework, and the parameters are chosen according to the original paper BIBREF20 . For the experiments with synthetic parallel data, we back-translate a random sample of 60 000 sentences from the collected simplified sentences into ordinary sentences. Our model is trained on synthetic data and the available parallel data, denoted as NMT+synthetic.
> 
> Results. Table 1 shows the results of all models on WikiLarge dataset. We can see that our method (NMT+synthetic) can obtain higher BLEU, lower FKGL and high SARI compared with other models, except Dress on FKGL and SBMT-SARI on SARI. It verified that including synthetic data during training is very effective, and yields an improvement over our baseline NMF by 2.11 BLEU, 1.7 FKGL and 1.07 SARI. We also substantially outperform Dress, who previously reported SOTA result. The results of our human evaluation using Simplicity are also presented in Table 1. NMT on synthetic data is significantly better than PBMT-R, Dress, and SBMT-SARI on Simplicity. It indicates that our method with simplified data is effective at creating simpler output.
> 
> Results on WikiSmall dataset are shown in Table 2. We see substantial improvements (6.37 BLEU) than NMT from adding simplified training data with synthetic ordinary sentences. Compared with statistical machine translation models (PBMT-R, Hybrid, SBMT-SARI), our method (NMT+synthetic) still have better results, but slightly worse FKGL and SARI. Similar to the results in WikiLarge, the results of our

#### Relevance 204

Label: 

### BM25

#### Passage 196

Retrieved by: BM25

> We train an auxiliary system using NMT model from the simplified sentence to the ordinary sentence, which is first trained on the available parallel data. For leveraging simplified sentences to improve the quality of NMT model for text simplification, we propose to adapt the back-translation approach proposed by Sennrich et al. BIBREF11 to our scenario. More concretely, Given one sentence in simplified sentences, we use the simplified-ordinary system in translate mode with greedy decoding to translate it to the ordinary sentences, which is denoted as back-translation. This way, we obtain a synthetic parallel simplified-ordinary sentences. Both the synthetic sentences and the available parallel data are used as training data for the original NMT system.

#### Relevance 196

Label: 

#### Passage 200

Retrieved by: BM25

> Text simplification aims to reduce the lexical and structural complexity of a text, while still retaining the semantic meaning, which can help children, non-native speakers, and people with cognitive disabilities, to understand text better. One of the methods of automatic text simplification can be generally divided into three categories: lexical simplification (LS) BIBREF0 , BIBREF1 , rule-based BIBREF2 , and machine translation (MT) BIBREF3 , BIBREF4 . LS is mainly used to simplify text by substituting infrequent and difficult words with frequent and easier words. However, there are several challenges for the LS approach: a great number of transformation rules are required for reasonable coverage and should be applied based on the specific context; third, the syntax and semantic meaning of the sentence is hard to retain. Rule-based approaches use hand-crafted rules for lexical and syntactic simplification, for example, substituting difficult words in a predefined vocabulary. However, such approaches need a lot of human-involvement to manually define these rules, and it is impossible to give all possible simplification rules. MT-based approach has attracted great attention in the last several years, which addresses text simplification as a monolingual machine translation problem translating from 'ordinary' and 'simplified' sentences.
> 
> In recent years, neural Machine Translation (NMT) is a newly-proposed deep learning approach and achieves very impressive results BIBREF5 , BIBREF6 , BIBREF7 . Unlike the traditional phrased-based machine translation system which operates on small components separately, NMT system is being trained end-to-end, without the need to have external decoders, language models or phrase tables. Therefore, the existing architectures in NMT are used for text simplification BIBREF8 , BIBREF4 . However, most recent work using NMT is limited to the training data that are scarce and expensive to build. Language models trained on simplified corpora have played a central role in statistical text simplification BIBREF9 , BIBREF10 . One main reason is the amount of available simplified corpora typically far exceeds the amount of parallel data. The performance of models can be typically improved when trained on more data. Therefore, we expect simplified corpora to be especially helpful for NMT models.
> 
> In contrast to previous work, which uses the existing NMT models, we explore strategy to include simplified training

#### Relevance 200

Label: 

### Dense

#### Passage 203

Retrieved by: Dense

> adding simplified training data with synthetic ordinary sentences. Compared with statistical machine translation models (PBMT-R, Hybrid, SBMT-SARI), our method (NMT+synthetic) still have better results, but slightly worse FKGL and SARI. Similar to the results in WikiLarge, the results of our human evaluation using Simplicity outperforms the other models. In conclusion, Our method produces better results comparing with the baselines, which demonstrates the effectiveness of adding simplified training data.

#### Relevance 203

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0024

Paper: Using Monolingual Data in Neural Machine Translation: a Systematic Study

> what language is the data in?

### Common Retrieved Chunks

#### Passage 205

Retrieved by: BM25, Hybrid RRF

> BT requires the availability of an MT system in the reverse translation direction. We consider here three MT systems of increasing quality:
> 
> backtrans-bad: this is a very poor SMT system trained using only 50k parallel sentences from the out-of-domain data, and no additional monolingual data. For this system as for the next one, we use Moses BIBREF17 out-of-the-box, computing alignments with Fastalign BIBREF18 , with a minimal pre-processing (basic tokenization). This setting provides us with a pessimistic estimate of what we could get in low-resource conditions.
> 
> backtrans-good: these are much larger SMT systems, which use the same parallel data as the baseline NMTs (see § SECREF4 ) and all the English monolingual data available for the WMT 2017 shared tasks, totalling approximately 174M sentences. These systems are strong, yet relatively cheap to build.
> 
> backtrans-nmt: these are the best NMT systems we could train, using settings that replicate the forward translation NMTs.
> 
> Note that we do not use any in-domain (Europarl) data to train these systems. Their performance is reported in Table TABREF7 , where we observe a 12 BLEU points gap between the worst and best systems (for both languages).
> 
> As noted eg. in BIBREF19 , BIBREF20 , artificial parallel data obtained through forward-translation (FT) can also prove advantageous and we also consider a FT system (fwdtrans-nmt): in this case the target side of the corpus is artificial and is generated using the baseline NMT applied to a natural source.
> 
> Our results (see Table TABREF6 ) replicate the findings of BIBREF2 : large gains can be obtained from BT (nearly INLINEFORM0 BLEU in French and German); better artificial data yields better translation systems. Interestingly, our best Moses system is almost as good as the NMT and an order of magnitude faster to train. Improvements obtained with the bad system are much smaller; contrary to the better MTs, this system is even detrimental for the out-of-domain test.
> 
> Gains with forward translation are significant, as in BIBREF21 , albeit about half as good as with BT, and result in small improvements for the in-domain and for the out-of-domain tests. Experiments combining forward and backward translation (backfwdtrans-nmt), each using a half of the available artificial data, do not

#### Relevance 205

Label: 

#### Passage 207

Retrieved by: BM25, Hybrid RRF

> The new generation of Neural Machine Translation (NMT) systems is known to be extremely data hungry BIBREF0 . Yet, most existing NMT training pipelines fail to fully take advantage of the very large volume of monolingual source and/or parallel data that is often available. Making a better use of data is particularly critical in domain adaptation scenarios, where parallel adaptation data is usually assumed to be small in comparison to out-of-domain parallel data, or to in-domain monolingual texts. This situation sharply contrasts with the previous generation of statistical MT engines BIBREF1 , which could seamlessly integrate very large amounts of non-parallel documents, usually with a large positive effect on translation quality.
> 
> Such observations have been made repeatedly and have led to many innovative techniques to integrate monolingual data in NMT, that we review shortly. The most successful approach to date is the proposal of BIBREF2 , who use monolingual target texts to generate artificial parallel data via backward translation (BT). This technique has since proven effective in many subsequent studies. It is however very computationally costly, typically requiring to translate large sets of data. Determining the “right” amount (and quality) of BT data is another open issue, but we observe that experiments reported in the literature only use a subset of the available monolingual resources. This suggests that standard recipes for BT might be sub-optimal.
> 
> This paper aims to better understand the strengths and weaknesses of BT and to design more principled techniques to improve its effects. More specifically, we seek to answer the following questions: since there are many ways to generate pseudo parallel corpora, how important is the quality of this data for MT performance? Which properties of back-translated sentences actually matter for MT quality? Does BT act as some kind of regularizer BIBREF3 ? Can BT be efficiently simulated? Does BT data play the same role as a target-side language modeling, or are they complementary? BT is often used for domain adaptation: can the effect of having more in-domain data be sorted out from the mere increase of training material BIBREF2 ? For studies related to the impact of varying the size of BT data, we refer the readers to the recent

#### Relevance 207

Label: 

#### Passage 209

Retrieved by: BM25, Dense, Hybrid RRF

> The literature devoted to the use of monolingual data is large, and quickly expanding. We already alluded to several possible ways to use such data: using back- or forward-translation or using a target language model. The former approach is mostly documented in BIBREF2 , and recently analyzed in BIBREF19 , which focus on fully artificial settings as well as pivot-based artificial data; and BIBREF4 , which studies the effects of increasing the size of BT data. The studies of BIBREF20 , BIBREF19 also consider forward translation and BIBREF21 expand these results to domain adaptation scenarios. Our results are complementary to these earlier studies.
> 
> As shown above, many alternatives to BT exist. The most obvious is to use target LMs BIBREF3 , BIBREF29 , as we have also done here; but attempts to improve the encoder using multi-task learning also exist BIBREF30 .
> 
> This investigation is also related to recent attempts to consider supplementary data with a valid target side, such as multi-lingual NMT BIBREF31 , where source texts in several languages are fed in the same encoder-decoder architecture, with partial sharing of the layers. This is another realistic scenario where additional resources can be used to selectively improve parts of the model.
> 
> Round trip training is another important source of inspiration, as it can be viewed as a way to use BT to perform semi-unsupervised BIBREF32 or unsupervised BIBREF33 training of NMT. The most convincing attempt to date along these lines has been proposed by BIBREF26 , who propose to use GANs to mitigate the difference between artificial and natural data.

#### Relevance 209

Label: 

#### Passage 210

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> A simple way to use monolingual data in MT is to turn it into synthetic parallel data and let the training procedure run as usual BIBREF16 . In this section, we explore various ways to implement this strategy. We first reproduce results of BIBREF2 with BT of various qualities, that we then analyze thoroughly.

#### Relevance 210

Label: 

#### Passage 211

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We are mostly interested with the following training scenario: a large out-of-domain parallel corpus, and limited monolingual in-domain data. We focus here on the Europarl domain, for which we have ample data in several languages, and use as in-domain training data the Europarl corpus BIBREF5 for two translation directions: English INLINEFORM0 German and English INLINEFORM1 French. As we study the benefits of monolingual data, most of our experiments only use the target side of this corpus. The rationale for choosing this domain is to (i) to perform large scale comparisons of synthetic and natural parallel corpora; (ii) to study the effect of BT in a well-defined domain-adaptation scenario. For both language pairs, we use the Europarl tests from 2007 and 2008 for evaluation purposes, keeping test 2006 for development. When measuring out-of-domain performance, we will use the WMT newstest 2014.

#### Relevance 211

Label: 

#### Passage 212

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> Comparing the natural and artificial sources of our parallel data wrt. several linguistic and distributional properties, we observe that (see Fig. FIGREF21 - FIGREF22 ):
> 
> artificial sources are on average shorter than natural ones: when using BT, cases where the source is shorter than the target are rarer; cases when they have the same length are more frequent.
> 
> automatic word alignments between artificial sources tend to be more monotonic than when using natural sources, as measured by the average Kendall INLINEFORM0 of source-target alignments BIBREF22 : for French-English the respective numbers are 0.048 (natural) and 0.018 (artificial); for German-English 0.068 and 0.053. Using more monotonic sentence pairs turns out to be a facilitating factor for NMT, as also noted by BIBREF20 .
> 
> syntactically, artificial sources are simpler than real data; We observe significant differences in the distributions of tree depths.
> 
> distributionally, plain word occurrences in artificial sources are more concentrated; this also translates into both a slower increase of the number of types wrt. the number of sentences and a smaller number of rare events.
> 
> The intuition is that properties (i) and (ii) should help translation as compared to natural source, while property (iv) should be detrimental. We checked (ii) by building systems with only 10M words from the natural parallel data selecting these data either randomly or based on the regularity of their word alignments. Results in Table TABREF23 show that the latter is much preferable for the overall performance. This might explain that the mostly monotonic BT from Moses are almost as good as the fluid BT from NMT and that both boost the baseline.

#### Relevance 212

Label: 

#### Passage 213

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> can the effect of having more in-domain data be sorted out from the mere increase of training material BIBREF2 ? For studies related to the impact of varying the size of BT data, we refer the readers to the recent work of BIBREF4 .
> 
> To answer these questions, we have reimplemented several strategies to use monolingual data in NMT and have run experiments on two language pairs in a very controlled setting (see § SECREF2 ). Our main results (see § SECREF4 and § SECREF5 ) suggest promising directions for efficient domain adaptation with cheaper techniques than conventional BT.

#### Relevance 213

Label: 

### BM25

#### Passage 206

Retrieved by: BM25

> We observe that the copy setup has only a small impact on the English-French system, for which the baseline is already strong. This is less true for English-German where simple copies yield a significant improvement. Performance drops for both language pairs in the copy-dummies setup.
> 
> We achieve our best gains with the copy-marked setup, which is the best way to use a copy of the target (although the performance on the out-of-domain tests is at most the same as the baseline). Such gains may look surprising, since the NMT model does not need to learn to translate but only to copy the source. This is indeed what happens: to confirm this, we built a fake test set having identical source and target side (in French). The average cross-entropy for this test set is 0.33, very close to 0, to be compared with an average cost of 58.52 when we process an actual source (in English). This means that the model has learned to copy words from source to target with no difficulty, even for sentences not seen in training. A follow-up question is whether training a copying task instead of a translation task limits the improvement: would the NMT learn better if the task was harder? To measure this, we introduce noise in the target sentences copied onto the source, following the procedure of BIBREF26 : it deletes random words and performs a small random permutation of the remaining words. Results (+ Source noise) show no difference for the French in-domain test sets, but bring the out-of-domain score to the level of the baseline. Finally, we observe a significant improvement on German in-domain test sets, compared to the baseline (about +1.5 BLEU). This last setup is even almost as good as the backtrans-nmt condition (see § SECREF8 ) for German. This shows that learning to reorder and predict missing words can more effectively serve our purposes than simply learning to copy.

#### Relevance 206

Label: 

#### Passage 208

Retrieved by: BM25

> As a follow up of previous discussions, we analyze the effect of BT on the internals of the network. Arguably, using a copy of the target sentence instead of a natural source should not be helpful for the encoder, but is it also the case with a strong BT? What are the effects on the attention model?

#### Relevance 208

Label: 

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 214

Retrieved by: Hybrid RRF followed by BGE reranking

> In this section, we compare the previous methods with the use of a target side Language Model (LM). Several proposals exist in the literature to integrate LMs in NMT: for instance, BIBREF3 strengthen the decoder by integrating an extra, source independent, RNN layer in a conventional NMT architecture. Training is performed either with parallel, or monolingual data. In the latter case, word prediction only relies on the source independent part of the network.

#### Relevance 214

Label: 

## Question 0025

Paper: Visual Question: Predicting If a Crowd Will Agree on the Answer

> What is the model architecture used?

### Common Retrieved Chunks

#### Passage 215

Retrieved by: BM25, Hybrid RRF

> a 12 percentage point improvement with respect to AP. This is interesting because it shows there is value in learning the disagreement task specifically, rather than employing an algorithm's confidence in its answers. More generally, our results demonstrate it is possible to predict whether a crowd will agree on a single answer from a given image and associated question. Despite the significant variety of questions and image content, and despite the variety of reasons for which the crowd can disagree, our learned model is able to produce quite accurate results.
> 
> We observe our Random Forest classifier outperforms our deep learning classifier; e.g., Ours: RF yields a three percentage point improvement with respect to AP while consistently yielding improved precision-recall values over Ours: LSTM-CNN (Figure FIGREF8 a). In general, deep learning systems hold promise to replace handcrafted features to pick out the discriminative features. Our baselines highlight a possible value in developing a different deep learning architecture for the problem of learning answer disagreement than applied for predicting answers to visual questions.
> 
> We show examples of prediction results where our top-performing RF classifier makes its most confident predictions (Figure FIGREF8 b). In these examples, the predictor expects human agreement for “what room... ?" visual questions and disagreement for “why... ?" visual questions. These examples highlight that the classifier may have a strong language prior towards making predictions, as we will discuss in the next section.
> 
> We now explore what makes a visual question lead to crowd answer agreement versus disagreement. We examine the influence of whether visual questions lead to the three types of answers (“yes/no", “number", “other") for both our random forest (RF) and deep learning (DL) classification systems. We enrich our analysis by examining the predictive performance of both classifiers when they are trained and tested exclusively with image and question features respectively. Figure FIGREF9 shows precision-recall curves for both classification systems with question features alone (Q), image features alone (I), and both question and image features together (Q+I).
> 
> When comparing AP scores (Figure FIGREF9 ), we observe our Q+I predictors yield the greatest predictive performance for visual questions that lead to “other" answers, followed by “number" answers, and finally “yes/no" answers. One possible

#### Relevance 215

Label: 

#### Passage 216

Retrieved by: BM25, Hybrid RRF

> region of interest. Moreover, we hypothesize this feature will capture our observation from the previous study that counting problems typically leads to disagreement for images showing many objects, and agreement otherwise.
> 
> We employ a 2,492-dimensional feature vector to represent the question-based features. One feature is the number of words in the question. Intuitively, a longer question offers more information and we hypothesize additional information makes a question more precise. The remaining features come from two one-hot vectors describing each of the first two words in the question. Each one-hot vector is created using the learned vocabularies that define all possible words at the first and second word location of a question respectively (using training data, as described in the next section). Intuitively, early words in a question inform the type of answers that might be possible and, in turn, possible reasons/frequency for answer disagreement. For example, we expect “why is" to regularly elicit many opinions and so disagreement. This intuition about the beginning words of a question is also supported by our analysis in the previous section which shows that different answer types yield different biases of eliciting answer agreement versus disagreement.
> 
> We leverage a random forest classification model BIBREF23 to predict an answer (dis)agreement label for a given visual question. This model consists of an ensemble of decision tree classifiers. We train the system to learn the unique weighted combinations of the aforementioned 2,497 features that each decision tree applies to make a prediction. At test time, given a novel visual question, the trained system converts a 2,497 feature descriptor of the visual question into a final prediction that reflects the majority vote prediction from the ensemble of decision trees. The system returns the final prediction along with a probability indicating the system's confidence in that prediction. We employ the Matlab implementation of random forests, using 25 trees and the default parameters.
> 
> We next adapt a VQA deep learning architecture BIBREF24 to learn the predictive combination of visual and textual features. The question is encoded with a 1024-dimensional LSTM model that takes in a one-hot descriptor of each word in the question. The image is described with the 4096-dimensional output from the last fully

#### Relevance 216

Label: 

#### Passage 217

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> predictive combination of visual and textual features. The question is encoded with a 1024-dimensional LSTM model that takes in a one-hot descriptor of each word in the question. The image is described with the 4096-dimensional output from the last fully connected layer of the Convolutional Neural Network (CNN), VGG16 BIBREF25 . The system performs an element-wise multiplication of the image and question features, after linearly transforming the image descriptor to 1024 dimensions. The final layer of the architecture is a softmax layer.
> 
> We train the system to predict (dis)agreement labels with training examples, where each example includes an image and question. At test time, given a novel visual question, the system outputs an unnormalized log probability indicating its belief in both the agreement and disagreement label. For our system's prediction, we convert the belief in the disagreement label into a normalized probability. Consequently, predicted values range from 0 to 1 with lower values reflecting greater likelihood for crowd agreement.

#### Relevance 217

Label: 

#### Passage 220

Retrieved by: Dense, Hybrid RRF

> and image features together (Q+I).
> 
> When comparing AP scores (Figure FIGREF9 ), we observe our Q+I predictors yield the greatest predictive performance for visual questions that lead to “other" answers, followed by “number" answers, and finally “yes/no" answers. One possible reason for this finding is that the question wording strongly drives whether a crowd will disagree for “other" visual questions, whereas some notion of common sense may be required to learn whether a crowd will agree for “yes/no" visual questions (e.g., Figure FIGREF7 a vs Figure FIGREF7 g).
> 
> We observe that question-based features yield greater predictive performance than image-based features for all visual questions, when comparing AP scores for Q and I classification results (Figure FIGREF9 ). In fact, image features contribute to performance improvements only for our random forest classifier for visual questions that lead to “number" answers, as illustrated by comparing AP scores for Our RF: Q+I and Our RF: Q (Figure FIGREF9 b). Our overall finding that most of the predictive power stems from language-based features parallels feature analysis findings in the automated VQA literature BIBREF2 , BIBREF21 . This does not mean, however, that the image content is not predictive. Further work improving visual content cues for VQA agreement is warranted.
> 
> Our findings suggest that our Random Forest classifier's overall advantage over our deep learning system arises because of counting questions, as indicated by higher AP scores (Figure FIGREF9 ). For example, the advantage of the initial higher precision (Figure FIGREF8 a; Ours: RF vs Ours: DL) is also observed for counting questions (Figure FIGREF9 b; Ours: RF - Q+I vs Ours: DL - Q+I). We hypothesize this advantage arises due to the strength of the Random Forest classifier in pairing the question prior (“How many?") with the image-based SOS features that indicates the number of objects in an image. Specifically, we expect “how many" to lead to agreement only for small counting problems.

#### Relevance 220

Label: 

#### Passage 221

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> run-time. Towards satisfying existing users, gaining new users, and supporting a wide range of applications, a crowd-powered VQA system should be low cost, have fast response times, and yield high quality answers. Today's status quo is to assume a fixed number of human responses per visual question and so a fixed cost, delay, and potential diversity of answers for every visual question BIBREF2 , BIBREF0 , BIBREF4 . We instead propose to dynamically solicit the number of human responses based on each visual question. In particular, we aim to accrue additional costs and delays from collecting extra answers only when extra responses are needed to discover all plausible answers. We show in our experiments that our system saves 19 40-hour work weeks and $1800 to answer 121,512 visual questions, compared to today's status quo approach BIBREF0 .
> 
> Our work is also inspired by the goal to improve how to employ crowds to produce the information needed to train and evaluate automated methods. Specifically, researchers in fields as diverse as computer vision BIBREF2 , computational linguistics BIBREF1 , and machine learning BIBREF3 rely on large datasets to improve their VQA algorithms. These datasets include visual questions and human-supplied answers. Such data is critical for teaching machine learning algorithms how to answer questions by example. Such data is also critical for evaluating how well VQA algorithms perform. In general, “bigger" data is better. Current methods to create these datasets assume a fixed number of human answers per visual question BIBREF2 , BIBREF4 , thereby either compromising on quality by not collecting all plausible answers or cost by collecting additional answers when they are redundant. We offer an economical way to spend a human budget to collect answers from crowd workers. In particular, we aim to actively allocate additional answers only to visual questions likely to have multiple answers.
> 
> The key contributions of our work are as follows:

#### Relevance 221

Label: 

#### Passage 222

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> We now describe our studies to assess the predictive power of our classification systems to decide whether visual questions will lead to answer (dis)agreement.
> 
> We capitalize on today's largest visual question answering dataset BIBREF2 to evaluate our prediction system, which includes 369,861 visual questions about real images. Of these, 248,349 visual questions (i.e., Training questions 2015 v1.0) are kept for for training and the remaining 121,512 visual questions (i.e., Validation questions 2015 v1.0) are employed for testing our classification system. This separation of training and testing samples enables us to estimate how well a classifier will generalize when applied to an unseen, independent set of visual questions.
> 
> To our knowledge, no prior work has directly addressed predicting answer (dis)agreement for visual questions. Therefore, we employ as a baseline a related VQA algorithm BIBREF24 , BIBREF2 which produces for a given visual question an answer with a confidence score. This system parallels the deep learning architecture we adapt. However, it predicts the system's uncertainty in its own answer, whereas we are interested in the humans' collective disagreement on the answer. Still, it is a useful baseline to see if an existing algorithm could serve our purpose.
> 
> We evaluate the predictive power of the classification systems based on each classifier's predictions for the 121,512 visual questions in the test dataset. We first show performance of the baseline and our two prediction systems using precision-recall curves. The goals are to achieve a high precision, to minimize wasting crowd effort when their efforts will be redundant, and a high recall, to avoid missing out on collecting the diversity of accepted answers from a crowd. We also report the average precision (AP), which indicates the area under a precision-recall curve. AP values range from 0 to 1 with better-performing prediction systems having larger values.
> 
> Figure FIGREF8 a shows precision-recall curves for all prediction systems. Both our proposed classification systems outperform the VQA Algorithm BIBREF2 baseline; e.g., Ours - RF yields a 12 percentage point improvement with respect to AP. This is interesting because it shows there is value in learning the disagreement task specifically, rather than employing an algorithm's confidence in its answers. More generally, our results demonstrate it is

#### Relevance 222

Label: 

#### Passage 223

Retrieved by: Dense, Hybrid RRF

> We now describe our studies to assess the benefit of our allocation system to reduce human effort to capture the diversity of all answers to visual questions.
> 
> We evaluate the impact of actively allocating extra human effort to answer visual questions as a function of the available budget of human effort. Specifically, for a range of budget levels, we compute the total measured answer diversity (as defined below) resulting for the batch of visual questions. The goal is to capture a large amount of answer diversity with little human effort.
> 
> We conduct our studies on the 121,512 test visual questions about real images (i.e., Validation questions 2015 v1.0). For each visual question, we establish the set of true answers as all unique answers which are observed at least twice in the 10 crowdsourced answers per visual question. We require agreement by two workers to avoid the possibility that “careless/spam" answers are treated as ground truth.
> 
> We collect either the minimum of INLINEFORM0 answer per visual question or the maximum of INLINEFORM1 answers per visual question. Our number of answers roughly aligns with existing crowd-powered VQA systems, for example with VizWiz, “On average, participants received 3.3 (SD=1.8) answers for each question" BIBREF0 . Our maximum number of answers also supports the possibility of capturing the maximum of three unique, valid answers typically observed in practice (recall study above). While more elaborate schemes for distributing responses may be possible, we will show this approach already proves quite effective in our experiments. We simulate answer collection by randomly selecting answers from the 10 crowd answers per visual question.
> 
> We compare our approach to the following baselines:
> 
> As in the previous section, we leverage the output confidence score from the publicly-shared model BIBREF24 learned from a LSTM-CNN deep learning architecture to rank the order of priority for visual questions to receive redundancy.
> 
> The system randomly prioritizes which images receive redundancy. This predictor illustrates the best a user can achieve today with crowd-powered systems BIBREF0 , BIBREF5 or with current dataset collection methods BIBREF2 , BIBREF4 .
> 
> We quantify the total diversity of answers captured by a resource allocation system for a batch of visual questions INLINEFORM0 as follows: DISPLAYFORM0

#### Relevance 223

Label: 

### BM25

#### Passage 218

Retrieved by: BM25

> The remainder of the paper is organized into four sections. We first describe a study where we investigate: 1) How much answer diversity arises for visual questions? and 2) Why do people disagree (Section SECREF4 )? Next, we explore the following two questions: 1) Given a novel visual question, can a machine correctly predict whether multiple independent members of a crowd would supply the same answer? and 2) If so, what insights does our machine-learned system reveal regarding what humans are most likely to agree about (Section SECREF5 )? In the following section, we propose a novel resource allocation system for efficiently capturing the diversity of all answers for a set of visual questions (Section SECREF6 ). Finally, we end with concluding remarks (Section SECREF7 ).

#### Relevance 218

Label: 

#### Passage 219

Retrieved by: BM25

> We now explore the following two questions: 1) Given a novel visual question, can a machine correctly predict whether multiple independent members of a crowd would supply the same answer? and 2) If so, what insights does our machine-learned system reveal regarding what humans are most likely to agree about?

#### Relevance 219

Label: 

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 224

Retrieved by: Hybrid RRF followed by BGE reranking

> We pose the prediction task as a binary classification problem. Specifically, given an image and associated question, a system outputs a binary label indicating whether a crowd will agree on the same answer. Our goal is to design a system that can detect which visual questions to assign a disagreement label, regardless of the disagreement cause (e.g., subjectivity, ambiguity, difficulty). We implement both random forest and deep learning classifiers.
> 
> A visual question is assigned either an answer agreement or disagreement label. To assign labels, we employ 10 crowdsourced answers for each visual question. A visual question is assigned an answer agreement label when there is an exact string match for 9 of the 10 crowdsourced answers (after answer pre-preprocessing, as discussed in the previous section) and an answer disagreement label otherwise. Our rationale is to permit the possibility of up to one “careless/spam" answer per visual question. The outcome of our labeling scheme is that a disagreement label is agnostic to the specific cause of disagreement and rather represents the many causes (described above).
> 
> For our first system, we use domain knowledge to guide the learning process. We compile a set of features that we hypothesize inform whether a crowd will arrive at an undisputed, single answer. Then we apply a machine learning tool to reveal the significance of each feature. We propose features based on the observation that answer agreement often arises when 1) a lay person's attention can be easily concentrated to a single, undisputed region in an image and 2) a lay person would find the requested task easy to address.
> 
> We employ five image-based features coming from the salient object subitizing BIBREF22 (SOS) method, which produces five probabilities that indicate whether an image contains 0, 1, 2, 3, or 4+ salient objects. Intuitively, the number of salient objects shows how many regions in an image are competing for an observer's attention, and so may correlate with the ease in identifying a region of interest. Moreover, we hypothesize this feature will capture our observation from the previous study that counting problems typically leads to disagreement for images showing many objects, and agreement otherwise.
> 
> We employ a 2,492-dimensional feature vector to represent the

#### Relevance 224

Label: 

#### Passage 225

Retrieved by: Hybrid RRF followed by BGE reranking

> Our first aim is to answer the following questions: 1) How much answer diversity arises for visual questions? and 2) Why do people disagree?

#### Relevance 225

Label: 

## Question 0026

Paper: Attention-based Wav2Text with Feature Transfer Learning

> Which dataset do they use?

### Common Retrieved Chunks

#### Passage 226

Retrieved by: BM25, Hybrid RRF

> The encoder-decoder model is a neural network that directly models conditional probability INLINEFORM0 where INLINEFORM1 is the source sequence with length INLINEFORM2 and INLINEFORM3 is the target sequence with length INLINEFORM4 . It consists of encoder, decoder and attention modules. The encoder task processes an input sequence INLINEFORM5 and outputs representative information INLINEFORM6 for the decoder. The attention module is an extension scheme that assists the decoder to find relevant information on the encoder side based on the current decoder hidden states BIBREF12 , BIBREF13 . Usually, the attention module produces context information INLINEFORM7 at time INLINEFORM8 based on the encoder and decoder hidden states: DISPLAYFORM0
> 
> There are several variations for score function : DISPLAYFORM0
> 
> where INLINEFORM0 , INLINEFORM1 is the number of hidden units for the encoder and INLINEFORM2 is the number of hidden units for the decoder. Finally, the decoder task, which predicts the target sequence probability at time INLINEFORM3 based on previous output and context information INLINEFORM4 , can be formulated as: DISPLAYFORM0
> 
> The most common input INLINEFORM0 for speech recognition tasks is a sequence of feature vectors such as log Mel-spectral spectrogram and/or MFCC. Therefore, INLINEFORM1 where D is the number of the features and S is the total length of the utterance in frames. The output INLINEFORM2 can be either phoneme or grapheme (character) sequence.
> 
> In this work, we use the raw waveform as the input representation instead of spectral-based features and a grapheme (character) sequence as the output representation. In contrast to most encoder-decoder architectures, which are purely based on recurrent neural network (RNNs) framework, we construct an encoder with several convolutional layers BIBREF14 followed by NIN layers BIBREF15 as the lower part in the encoder and integrate them with deep bidirectional long short-term memory (Bi-LSTM) BIBREF16 at the higher part. We use convolutional layers because they are suitable for extracting local information from raw speech. We use a striding mechanism to reduce the dimension from the input frames BIBREF17 , while the NIN layer represents more complex structures on the top of the convolutional layers. On the decoder side, we use a standard deep unidirectional LSTM with global attention BIBREF13 that is calculated by a multi-layer perceptron (MLP)

#### Relevance 226

Label: 

#### Passage 227

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Transfer learning is the ability of a learning algorithm to convey knowledge across different tasks. The initial idea is to reuse previously obtained knowledge to enhance the learning for new things. The standard procedure are : first, train the model on a base dataset and task, then the learned features and/or parameters are reused for learning a second target dataset and task. Bengio et al. BIBREF25 provided deep reviews about multi-task and transfer learning on deep learning models. Jason et al. BIBREF26 showed that a model with transferred parameter consistently outperformed a randomly initialized one.
> 
> In speech recognition research, transfer learning has been studied for many years, including successful cases of speaker adaptation and cross-lingual acoustic modeling BIBREF27 . One popular scheme for utilizing DNNs for transfer learning within ASR frameworks is a tandem approach BIBREF28 . This idea first trains a DNN with a narrow hidden bottleneck layer to perform phoneme classification at the frame level and then reuses the activations from the narrow hidden bottleneck layer as discriminative features in conventional GMM-HMM or hybrid DNN-HMM models BIBREF29 . Another study introduced a convolutional bottleneck network as an alternative tandem bottleneck feature architecture BIBREF30 . However, although such a feature transfer learning framework provides many advantages in ASR, the usage in an end-to-end attention-based ASR framework has not been explored.
> 
> This study performs feature transfer learning on the encoder part of the end-to-end attention-based ASR architecture. We train the convolutional encoder to predict the spectral features given the corresponding raw speech waveform. After that, we transfer the trained layers and parameters, integrate them with the LSTM encoder-decoder, and eventually optimize the whole structure to predict the correct output text transcription given the raw speech waveform.

#### Relevance 227

Label: 

#### Passage 228

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> outperformed MFCC-based TDNN on the Wall Street Journal (WSJ) BIBREF5 task. But despite significant progress that has been made, the successful models were mostly demonstrated only within the hybrid DNN-HMM speech recognition frameworks.
> 
> On the other hand, some existing works constructed end-to-end neural network models for ASR and replaced the acoustic model, the lexicon model, and the language model with a single integrated model, thus simplifying the pipeline. Graves et al. BIBREF6 , BIBREF7 successfully built an end-to-end ASR based on the connectionist temporal classification (CTC) framework. Amodei et al. BIBREF8 also constructed an end-to-end CTC-based ASR that directly produced character strings instead of phoneme sequences. But the CTC-based architecture still predicts the target outputs for every frame without any implicit knowledge about the language model. Another approach uses a sequence-to-sequence attention-based encoder-decoder that explicitly uses the history of previous outputs. Chorowski et al. BIBREF9 and Chan et al. BIBREF10 has successfully demonstrated encoder-decoder based ASR frameworks. Unfortunately, most of these works still used the standard spectral features (i.e., Mel-scale spectrogram, MFCC) as the input. The only attempt on end-to-end speech recognition for a raw waveform was recently proposed by BIBREF11 . Their system used a deep CNN and was trained with the automatic segmentation criterion (ASG) as an alternative to CTC. However, similar with CTC, the model did not explicitly use the history of the previous outputs assuming they were conditionally independent of each other. Furthermore, its performance was only reported using a very large data set (about 1000h of audio files).
> 
> To the best of our knowledge, few studies have explored a single end-to-end ASR architecture trained on raw speech waveforms to directly output text transcription, and none of those models were built based on an encoder-decoder architecture. In this paper, we take a step forward to construct an end-to-end ASR using an attentional-based encoder-decoder model for processing raw speech waveform, naming it as “Attention-based Wav2Text". We investigate the performance of our proposed models on standard ASR datasets. In practice, optimizing an encoder-decoder framework is more difficult than a standard neural network architecture BIBREF10 . Therefore, we propose a feature transfer learning method to assist the training process for our end-to-end attention-based ASR

#### Relevance 228

Label: 

#### Passage 229

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> An example of our transfer learning results is shown in Figure FIGREF8 , and Table TABREF14 shows the speech recognition performance in CER for both the WSJ-SI84 and WSJ-SI284 datasets. We compared our method with several published models like CTC, Attention Encoder-Decoder and Joint CTC-Attention model that utilize CTC for training the encoder part. Besides, we also train our own baseline Attention Encoder-Decoder with Mel-scale spectrogram. The difference between our Attention Encoder-Decoder (“Att Enc-Dec (ours)", “Att Enc-Dec Wav2Text") with Attention Encoder-Decoder from BIBREF24 (“Att Enc-Dec Content", “Att Enc-Dec Location") is we used the current hidden states to generate the attention vector instead of the previous hidden states. Another addition is we utilized “input feedback" method BIBREF13 by concatenating the previous context vector into the current input along with the character embedding vector. By using those modifications, we are able to improve the baseline performance.
> 
> Our proposed Wav2Text models without any transfer learning failed to converge. In contrast, with transfer learning, they significantly surpassed the performance of the CTC and encoder-decoder from Mel-scale spectrogram features. This suggests that by using transfer learning for initializing the lower part of the encoder parameters, our model also performed better then their original features.

#### Relevance 229

Label: 

#### Passage 232

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> models on standard ASR datasets. In practice, optimizing an encoder-decoder framework is more difficult than a standard neural network architecture BIBREF10 . Therefore, we propose a feature transfer learning method to assist the training process for our end-to-end attention-based ASR model.

#### Relevance 232

Label: 

#### Passage 233

Retrieved by: Dense, Hybrid RRF

> Our attention-based Wav2Text architecture uses four convolutional layers, followed by two NIN layers at the lower part of the encoder module. For all the convolutional layers, we used a leaky rectifier unit (LReLU) BIBREF20 activation function with leakiness INLINEFORM0 . Inside the first NIN layers, we stacked three consecutive filters with LReLU activation function. For the second NIN layers, we stacked two consecutive filters with tanh and identity activation function. For the feature transfer learning training phase, we used Momentum SGD with a learning rate of 0.01 and momentum of 0.9. Table TABREF11 summarizes the details of the layer settings for the convolutional and NIN layers.
> 
> On the top layers of the encoder after the transferred convolutional and NIN layers, we put three bidirectional LSTMs (Bi-LSTM) with 256 hidden units (total 512 units for both directions). To reduce the computational time, we used hierarchical subsampling BIBREF21 , BIBREF22 , BIBREF10 . We applied subsampling on all the Bi-LSTM layers and reduced the length by a factor of 8.
> 
> On the decoder side, the previous input phonemes / characters were converted into real vectors by a 128-dimensional embedding matrix. We used one unidirectional LSTM with 512 hidden units and followed by a softmax layer to output the character probability. For the end-to-end training phase, we froze the parameter values from the transferred layers from epoch 0 to epoch 10, and after epoch 10 we jointly optimized all the parameters together until the end of training (a total 40 epochs). We used an Adam BIBREF23 optimizer with a learning rate of 0.0005.
> 
> In the decoding phase, we used a beam search strategy with beam size INLINEFORM0 and we adjusted the score by dividing with the transcription length to prevent the decoder from favoring shorter transcriptions. We did not use any language model or lexicon dictionary for decoding. All of our models were implemented on the PyTorch framework .
> 
> For comparison, we also evaluated the standard attention-based encoder decoder with Mel-scale spectrogram input as the baseline. Here, we used similar settings as the proposed model, except we replaced the convolutional and NIN layers with a feedforward layer (512 hidden units).

#### Relevance 233

Label: 

#### Passage 234

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> Conventional large-vocabulary continuous speech recognition (LVCSR) systems typically perform multi-level pattern recognition tasks that map the acoustic speech waveform into a hierarchy of speech units such as sub-words (phonemes), words, and strings of words (sentences). Such systems basically consist of several sub-components (feature extractor, acoustic model, pronunciation lexicon, language model) that are trained and tuned separately BIBREF0 . First, the speech signal is processed into a set of observation features based on a carefully hand-crafted feature extractor, such as Mel frequency cepstral coefficients (MFCC) or Mel-scale spectrogram. Then the acoustic model classifies the observation features into sub-unit or phoneme classes. Finally, the search algorithm finds the most probable word sequence based on the evidence of the acoustic model, the lexicon, and the language model. But, it is widely known that information loss in the earlier stage can propagate through the later stages.
> 
> Deep learning algorithms have produced many state-of-the-art performances in various tasks that have revitalized the use of neural networks for ASR. One of the important factors behind the popularity of deep learning is the possibility of simplifying many complicated hand-engineered models by letting DNNs find their way to map from input to output spaces. Interest has emerged recently in the possibility of learning DNN-based acoustic models directly from the raw speech waveform without any predefined alignments and hand-engineered models. In this way, the feature extractor and acoustic model can be integrated into a single architecture. Palaz et al. BIBREF1 , BIBREF2 proposed a convolutional neural network (CNN) to directly train an acoustic model from the raw speech waveform. Sainath et al. BIBREF3 used time-convolutional layers over raw speech and trained them jointly with the long short-term memory deep neural network (CLDNN) acoustic model. The results showed that raw waveform CLDNNs matched the performance of log-mel CLDNNs on a voice search task. Ghahremani et al. BIBREF4 recently proposed a CNN time-delay neural network (CNN-TDNN) with network-in-network (NIN) architecture, and also showed that their model outperformed MFCC-based TDNN on the Wall Street Journal (WSJ) BIBREF5 task. But despite significant progress that has been made, the successful models were mostly demonstrated only within the hybrid DNN-HMM speech recognition frameworks.
> 
> On the other hand, some existing works

#### Relevance 234

Label: 

### BM25

#### Passage 230

Retrieved by: BM25

> BIBREF17 , while the NIN layer represents more complex structures on the top of the convolutional layers. On the decoder side, we use a standard deep unidirectional LSTM with global attention BIBREF13 that is calculated by a multi-layer perceptron (MLP) as described in Eq. EQREF2 . For more details, we illustrate our architecture in Figure FIGREF4 .

#### Relevance 230

Label: 

### Dense

#### Passage 231

Retrieved by: Dense

> In this study, we investigate the performance of our proposed models on WSJ BIBREF5 . We used the same definitions of the training, development and test set as the Kaldi s5 recipe BIBREF18 . The raw speech waveforms were segmented into multiple frames with a 25ms window size and a 10ms step size. We normalized the raw speech waveform into the range -1 to 1. For spectral based features such as MFCC and log Mel-spectrogram, we normalized the features for each dimension into zero mean and unit variance. For WSJ, we separated into two experiments by using WSJ-SI84 only and WSJ-SI284 data. We used dev_93 for our validation set and eval_92 for our test set. We used the character sequence as our decoder target and followed the preprocessing step proposed by BIBREF19 . The text from all the utterances was mapped into a 32-character set: 26 (a-z) alphabet, apostrophe, period, dash, space, noise, and “eos".

#### Relevance 231

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0027

Paper: Semantic Product Search

> What dataset is used for training?

### Common Retrieved Chunks

#### Passage 235

Retrieved by: BM25, Hybrid RRF

> In this section, we present the durable learnings from thousands of experiments. We fix the embedding dimension to 256, weight matrix initialization to Xavier initialization BIBREF29 , batch size to 8192, and the optimizer to ADAM with the configuration INLINEFORM0 for all the results presented. We refer to the hinge losses defined in Section SECREF10 with INLINEFORM1 and INLINEFORM2 as the L1 and L2 variants respectively. Unigram tokenization is used in Table TABREF26 and Table TABREF27 , as the relative ordering of results does not change with other more sophisticated tokenizations.
> 
> We present the results of different loss functions in Table TABREF26 . We see that the L2 variant of each loss consistently outperforms the L1. We hypothesize that L2 variants are robust to outliers in cosine similarity. The 3-part hinge loss outperforms the 2-part hinge loss in matching metrics in all experiments although the two loss functions have similar ranking performance. By considering impressed negatives, whose text is usually more similar to positives than negatives, separately from random negatives in the 3-part hinge loss, the scores for positives and random negatives become better separated, as shown in Section SECREF10 . The model can better differentiate between positives and random negatives, improving Recall and MAP. Because the ranking task is not distinguishing between relevant and random products but instead focuses on ordering purchased and impressed products, it is not surprising that the 2-part and 3-part loss functions have similar performance.
> 
> In Table TABREF27 , we present the results of using LSTM, GRU, and averaging to aggregate the token embeddings. Averaging performs similar to or slightly better than recurrent units with significantly less training time. As mentioned in Section SECREF8 , in the product search setting, queries and product titles tend to be relatively short, so averaging is sufficient to capture the short-range dependencies that exist in queries and product titles. Furthermore, recurrent methods are more expressive but introduce specialization between the query and title. Consequently, local word-level matching between the query and the product title may not be not captured as well.
> 
> In Table TABREF28 , we compare the performance of using different tokenization methods. We use average pooling and the 3-part L2 hinge loss.

#### Relevance 235

Label: 

#### Passage 236

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> There is a rich literature in natural language processing (NLP) and information retrieval (IR) on capturing the semantics of queries and documents. Word2vec BIBREF4 garnered significant attention by demonstrating the use of word embeddings to capture semantic structure; synonyms cluster together in the embedding space. This technique was successfully applied to document ranking for web search with the DESM model BIBREF5 . Building from the ideas in word2vec, BIBREF6 trained neural word embeddings to find neighboring words to expand queries with synonyms. Ultimately, based on these recent advancements and other key insights, the state-of-the-art models for semantic search can generally be classified into three categories:
> 
> BIBREF7 introduced Latent Semantic Analysis (LSA), which computes a low-rank factorization of a term-document matrix to identify semantic concepts and was further refined by BIBREF8 , BIBREF9 and extended by ideas from Latent Dirichlet Allocation (LDA) BIBREF10 in BIBREF11 . In 2013, BIBREF12 published the seminal paper in the space of factorized models by introducing the Deep Semantic Similarity Model (DSSM). Inspired by LSA and Semantic Hashing BIBREF13 , DSSM involves training an end-to-end deep neural network with a discriminative loss to learn a fixed-width representation for queries and documents. Fully connected units in the DSSM architecture were subsequently replaced with Convolutional Neural Networks (CNNs) BIBREF14 , BIBREF15 and Recurrent Neural Networks (RNNs) BIBREF16 to respect word ordering. In an alternate approach, which articulated the idea of interaction models, BIBREF17 introduced the Deep Relevance Matching Model (DRMM) which leverages an interaction matrix to capture local term matching within neural approaches which has been successfully extended by MatchPyramid BIBREF18 and other techniques BIBREF19 , BIBREF20 , BIBREF21 , BIBREF22 , BIBREF23 . Nevertheless, these interaction methods require memory and computation proportional to the number of words in the document and hence are prohibitively expensive for online inference. In addition, Duet BIBREF24 combines the approaches of DSSM and DRMM to balance the importance of semantic and lexical matching. Despite obtaining state-of-the-art results for ranking, these methods report limited success on ad hoc retrieval tasks BIBREF24 and only achieve a sub-50% Recall@100 and MAP on our product matching dataset, as shown with the ARC-II and Match Pyramid baselines in Table TABREF30 .
> 
> While

#### Relevance 236

Label: 

#### Passage 237

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> for ranking, these methods report limited success on ad hoc retrieval tasks BIBREF24 and only achieve a sub-50% Recall@100 and MAP on our product matching dataset, as shown with the ARC-II and Match Pyramid baselines in Table TABREF30 .
> 
> While we frequently evaluate our hypotheses on interaction matrix-based methods, we find that a factorized model architecture achieves comparable performance while only requiring constant memory per product. Hence, we only present our experiments as it pertains to factorized models in this paper. Although latent factor models improve ranking metrics due to their ability to memorize associations between the query and the product, we exclude it from this paper as we focus on the matching task. Our choice of model architecture was informed by empirical experiments while constrained by the cost per query and our ability to respond within 20 milliseconds for thousands of queries per second.

#### Relevance 237

Label: 

#### Passage 238

Retrieved by: BM25, Dense, Hybrid RRF

> We use 11 months of search logs as training data and 1 month as evaluation. We sample 54 billion query-product training pairs. We preprocess these sampled pairs to 650 million rows by grouping the training data by query-product pairs over the entire time period and using the aggregated counts as weights for the pairs. We also decrease the training time by 3X by preprocessing the training data into tokens and using mmap to store the tokens. More details on our best practices for reducing training time can be found in Section SECREF6 .
> 
> For a given customer query, each product is in exactly one of three categories: purchased, impressed but not purchased, or random. For each query, we target a ratio of 6 impressed and 7 random products for every query-product purchase. We sample this way to train the model for both matching and ranking, although in this paper we focus on matching. Intuitively, matching should differentiate purchased and impressed products from random ones; ranking should differentiate purchased products from impressed ones.
> 
> We choose the most frequent words to build our vocabulary, referred to as INLINEFORM0 . Each token in the vocabulary is assigned a unique numeric token id, while remaining tokens are assigned 0 or a hashing based identifier. Queries are lowercased, split on whitespace, and converted into a sequence of token ids. We truncate the query tokens at the 99th percentile by length. Token vectors that are smaller than the predetermined length are padded to the right.
> 
> Products have multiple attributes, like title, brand, and color, that are material to the matching process. We evaluated architectures to embed every attribute independently and concatenate them to obtain the final product representation. However, large variability in the accuracy and availability of structured data across products led to 5% lower recall than simply concatenating the attributes. Hence, we decided to use an ordered bag of words of these attributes.

#### Relevance 238

Label: 

#### Passage 239

Retrieved by: BM25, Dense, Hybrid RRF

> Our neural network architecture is shown in Figure FIGREF9 . As in the distributed arm of the Duet model, our first model component is an embedding layer that consists of INLINEFORM0 parameters where INLINEFORM1 is the vocabulary and INLINEFORM2 is the embedding dimension. Each row corresponds to the parameters for a word. Unlike Duet, we share our embeddings across the query and product. Intuitively, sharing the embedding layer in a Siamese network works well, capturing local word-level matching even before training these networks. Our experiments in Table UID37 confirm this intuition. We discuss the specifics of our query and product representation in Section SECREF4 .
> 
> To generate a fixed length embedding for the query ( INLINEFORM0 ) and the product ( INLINEFORM1 ) from individual word embeddings, we use average pooling after observing little difference (<0.5%) in both MAP and Recall@100 relative to recurrent approaches like LSTM and GRU (see Table TABREF27 ). Average pooling also requires far less computation, reducing training time and inference latency. We reconciled this departure from state-of-the-art solutions for Question Answering and other NLP tasks through an analysis that showed that, unlike web search, both query and product information tend to be shorter, without long-range dependencies. Additionally, product search queries do not contain stop words and typically require every query word (or its synonym) to be present in the product.
> 
> Queries typically have fewer words than the product content. Because of this, we observed a noticeable difference in the magnitude of query and product embeddings. This was expected as the query and the product models were shared with no additional parameters to account for this variance. Hence, we introduced Batch Normalization layers BIBREF25 after the pooling layers for the query and the product arms. Finally, we compute the cosine similarity between INLINEFORM0 and INLINEFORM1 . During online A/B testing, we precompute INLINEFORM2 for all the products in the catalog and use a INLINEFORM3 -Nearest Neighbors algorithm to retrieve the most similar products to a given query INLINEFORM4 .

#### Relevance 239

Label: 

#### Passage 240

Retrieved by: Dense, Hybrid RRF

> Finally, in Table TABREF30 , we compare the results of our model to four baselines: DSSM BIBREF12 , Match Pyramid BIBREF18 , ARC-II BIBREF15 , and our model with frozen, randomly initialized embeddings. We only use word unigrams or character trigrams in our model, as it is not immediately clear how to extend the bag-of-tokens approach to methods that incorporate ordering. We compare the performance of using the 3-part L2 hinge loss to the original loss presented for each model. Across all baselines, matching performance of the model improves using the 3-part L2 hinge loss. ARC-II and Match Pyramid ranking performance is similar or lower when using the 3-part loss. Ranking performance improves for DSSM, possibly because the original approach uses only random negatives to approximate the softmax normalization. More complex models, like Match Pyramid and ARC-II, had significantly lower matching and ranking performance while taking significantly longer to train and evaluate. These models are also much harder to tune and tend to overfit.
> 
> The embeddings in our model are trained end-to-end. Previous experiments using other methods, including Glove and word2vec, to initialize the embeddings yielded poorer results than end-to-end training. When comparing our model with randomly initialized to one with trained embeddings, we see that end-to-end training results in over a 3X improvement in Recall@100 and MAP.

#### Relevance 240

Label: 

#### Passage 241

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> A critical decision when employing a vector space model is defining a match, especially in product search where there is an important tradeoff between precision and recall. For example, accessories like mounts may also be relevant for the query “led tv.”
> 
> Pruning results based on a threshold is a common practice to identify the match set. Pointwise loss functions, such as mean squared error (MSE) or mean absolute error (MAE), require an additional step post-training to identify the threshold. Pairwise loss functions do not provide guarantees on the magnitude of scores (only on relative ordering) and thus do not work well in practice with threshold-based pruning. Hence, we started with a pointwise 2-part hinge loss function as shown in Equation ( EQREF11 ) that maximizes the similarity between the query and a purchased product while minimizing the similarity between a query and random products. Define INLINEFORM0 , and let INLINEFORM1 if product INLINEFORM2 is purchased in response to query INLINEFORM3 , and INLINEFORM4 otherwise. Furthermore let INLINEFORM5 , and INLINEFORM6 for some predefined thresholds INLINEFORM7 and INLINEFORM8 and INLINEFORM9 . The two part hinge loss can be defined as DISPLAYFORM0
> 
> Intuitively, the loss ensures that when INLINEFORM0 then INLINEFORM1 is less than INLINEFORM2 and when INLINEFORM3 then INLINEFORM4 is above INLINEFORM5 . After some empirical tuning on a validation set, we set INLINEFORM6 and INLINEFORM7 .
> 
> As shown in Table TABREF26 , the 2-part hinge loss improved offline matching performance by more than 2X over the MSE baseline. However in Figure FIGREF12 , a large overlap in score distribution between positives and negatives can be seen. Furthermore, the score distribution for negatives appeared bimodal. After manually inspecting the negative training examples that fell in this region, we uncovered that these were products that were impressed but not purchased by the customer. From a matching standpoint, these products are usually valid results to show to customers. To improve the model's ability to distinguish positives and negatives considering these two classes of negatives, we introduced a 3-part hinge loss: DISPLAYFORM0
> 
> where INLINEFORM0 , INLINEFORM1 , and INLINEFORM2 denote indicators signifying if the product INLINEFORM3 was purchased, not impressed and not purchased, and impressed (but not purchased) in

#### Relevance 241

Label: 

### BM25

None

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 242

Retrieved by: Hybrid RRF followed by BGE reranking

> In this section we describe our metrics, training procedure, and the results, including the impact of our method in production.

#### Relevance 242

Label: 

#### Passage 243

Retrieved by: Hybrid RRF followed by BGE reranking

> At a high level, as shown in Figure FIGREF4 , a product search engine works as follows: a customer issues a query, which is passed to a lexical matching engine (typically an inverted index BIBREF0 , BIBREF1 ) to retrieve all products that contain words in the query, producing a match set. The match set passes through stages of ranking, wherein top results from the previous stage are re-ranked before the most relevant items are finally displayed. It is imperative that the match set contain a relevant and diverse set of products that match the customer intent in order for the subsequent rankers to succeed. However, inverted index-based lexical matching falls short in several key aspects:
> 
> In this paper, we address the question: Given rich customer behavior data, can we train a deep learning model to retrieve matching products in response to a query? Intuitively, there is reason to believe that customer behavior logs contain semantic information; customers who are intent on purchasing a product circumvent the limitations of lexical matching by query reformulation or by deeper exploration of the search results. The challenge is the sheer magnitude of the data as well as the presence of noise, a challenge that modern deep learning techniques address very effectively.
> 
> Product search is different from web search as the queries tend to be shorter and the positive signals (purchases) are sparser than clicks. Models based on conversion rates or click-through-rates may incorrectly favor accessories (like a phone cover) over the main product (like a cell phone). This is further complicated by shoppers maintaining multiple intents during a single search session: a customer may be looking for a specific television model while also looking for accessories for this item at the lowest price and browsing additional products to qualify for free shipping. A product search engine should reduce the effort needed from a customer with a specific mission (narrow queries) while allowing shoppers to explore when they are looking for inspiration (broad queries).
> 
> As mentioned, product search typically operates in two stages: matching and ranking. Products that contain words in the query ( INLINEFORM0 ) are the primary candidates. Products that have prior behavioral associations (products bought or

#### Relevance 243

Label: 

## Question 0028

Paper: Selecting Artificially-Generated Sentences for Fine-Tuning Neural Machine Translation

> Which data-selection algorithms do they use?

### Common Retrieved Chunks

#### Passage 244

Retrieved by: BM25, Hybrid RRF

> The improvement of NMT models can be performed by fine-tuning BIBREF7, BIBREF8, i.e. train the models for additional epochs using a small set of in-domain data. Alternatively, BIBREF9 train models using smaller but more in-domain sentences in each epoch of the training process.
> 
> The use of the test set to retrieve relevant sentences for fine-tuning the model has been explored by BIBREF10, adapting a different model for each sentence in the test set, or BIBREF11, BIBREF12 where they adapt the model for the complete test set using transductive data-selection algorithms.

#### Relevance 244

Label: 

#### Passage 245

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The data used for training Machine Translation (MT) models consist mainly of a set of parallel sentences (a set of sentence-pairs in which each sentence is paired with its translation). As Neural Machine Translation (NMT) models typically achieve best performance when using large sets of parallel sentences, they can benefit from the sentences created by Natural Language Generation (NLG) systems. Although artificial data is expected to be of lower quality than authentic sentences, it still can help the model to learn how to better generalize over the training instances and produce better translations.
> 
> A popular technique used to create artificial data is the back-translation technique BIBREF0, BIBREF1. This consists of generating sentences in the source language by translating monolingual sentences in the target language. Then, these sentences in both languages are paired and can be used to augment the original parallel training set used to build better NMT models.
> 
> Nonetheless, if synthetic data are not in the same domain as the test set, it can also hurt the performance. For this reason, we explore an alternative approach to better use the artificially-generated training instances to improve NMT models. In particular, we propose that instead of blindly adding back-translated sentences into the training set they can be considered as candidate sentences for a data-selection algorithm to decide which sentence-pairs should be used to fine-tune the NMT model. By doing that, instead of increasing the number of training instances in a motivated manner, the generated sentences provide us with more chances of obtaining relevant parallel sentences (and still use smaller sets for fine-tuning).
> 
> As we want to build task-specific NMT models, in this work we explore two data-selection algorithms that are classified as Transductive Algorithms (TA): Infrequent N-gram Recovery (INR) and Feature Decay Algorithms (FDA). These methods use the test set $S_{test}$ (the document to be translated) as the seed to retrieve sentences. In transductive learning BIBREF2 the goal is to identify the best training instances to learn how to classify a given test set. In order to select these sentences, the TAs search for those n-grams in the test set that are also present in the source side of the candidate sentences.
> 
> Although augmenting the candidate

#### Relevance 245

Label: 

#### Passage 246

Retrieved by: BM25, Dense, Hybrid RRF

> In this work, we have presented how artificially generated sentences can be used to augment a set of candidate sentences so data-selection algorithms have a wider variety of sentences to select from. The TA-selected sets have been evaluated according to how useful they are for improving NMT models.
> 
> We have presented three methods of creating such hybrid data: (i) by allowing the TA decide whether to select authentic or synthetic data (hybr); (ii) by performing independent executions of the TA on authentic and synthetic sets (batch); and (iii) using an MT-generated seed to select monolingual sentences so only the extracted subset is back-translated (online).
> 
> The experiments showed that artificially-generated sentences can be as competitive as authentic data, as models built with different proportions of authentic and synthetic data achieve similar or even better performance than those fine-tuned with authentic pairs only. On one hand, those sentences whose target-sides could hurt the performance of NMT (such as sentences in a different language to that expected) causes the back-translated sentence to also contain unnatural n-grams and so TAs would not select them. On the other hand, if the source-side sentence is not an accurate translation of the target side (the problem of comparable corpus), the back-translated counterpart can be a better alternative to use as training data.
> 
> In the future, we want to explore other language pairs and other transductive algorithms. Another limitation of this work is that we have augmented the candidate pool with synthetic sentences generated by a single model. We propose to explore whether using several models for generating the synthetic sentences (including different approaches such as combining statistical and neural model BIBREF30) to augment the candidate pool can cause the selected data to further improve NMT models.

#### Relevance 246

Label: 

#### Passage 248

Retrieved by: BM25, Hybrid RRF

> The work presented in this paper is based on two main concepts: the generation of synthetic sentences, and the selection of sentences from a set $S$ of candidates.

#### Relevance 248

Label: 

#### Passage 249

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> In order to fine-tune models with hybrid data, we propose three methods of creating these sets: hybr, batch and online. These methods can be classified depending on whether the combination is performed before or after the execution of the TA.

#### Relevance 249

Label: 

#### Passage 250

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> In this paper, the sentences used to fine-tune the model are retrieved using INR and FDA. These methods select sentences by scoring each sentence $s$ from the candidate pool $S$, and adding that with the highest score to a selected pool $L$. This process is performed iteratively until the selected pool contains $N$ sentences.

#### Relevance 250

Label: 

#### Passage 251

Retrieved by: Dense, Hybrid RRF

> learn how to classify a given test set. In order to select these sentences, the TAs search for those n-grams in the test set that are also present in the source side of the candidate sentences.
> 
> Although augmenting the candidate pool with more sentences should be beneficial, as the TAs select the sentences based on overlapping n-gram the mistakes produced by the model used for back-translation (which are those commonly addressed in NLG such as the generated word order or word choice) can be a disadvantage.
> 
> In this work, we explore whether TAs are more inclined to select authentic or artificial sentences. In addition, we propose three different methods of how they can be combined into a single hybrid set. Finally, we investigate whether the hybrid sets retrieved by TAs can be more useful than the authentic set of sentences to fine-tune NMT models.

#### Relevance 251

Label: 

### BM25

#### Passage 247

Retrieved by: BM25

> The proposal of BIBREF0 showed that NMT models can be improved by back-translating a set of (monolingual) sentences in the target side into the source side using an MT model. Other uses of monolingual target-side sentences include building the parallel set by using a NULL token in the source side BIBREF0 or creating language models to improve the decoder BIBREF3.
> 
> BIBREF4 improve the model used for back-translation by training this model with increasing amounts of artificial sentences. They iteratively improve the models creating artificial sentences of better quality.
> 
> Similarly to this paper, the use of artificially-generated sentences to fine-tuned models has also been explored by BIBREF5 where they select monolingual authentic sentences in the source-side and translate them into the target language, or the work of BIBREF6 where they use back-translated sentences only to adapt the models.

#### Relevance 247

Label: 

### Dense

#### Passage 252

Retrieved by: Dense

> (INR) BIBREF13, BIBREF14: This method selects those sentences that contain n-grams from the test set that are infrequent (ignoring frequent words such as stop words or general-domain terms). A candidate sentence $s \in S$ is scored according to the number of infrequent n-grams shared with the set of sentences of the test set $S_{test}$, computed as in (DISPLAY_FORM4):
> 
> where $t$ is the threshold that indicates the number of occurrences of an n-gram to be considered infrequent. If the number of occurrences of $ngr$ in the selected pool ($C_L(ngr)$) is above the threshold $t$, then the component $max(0,t-C_S(ngr))$ is 0 and so the n-gram does not contribute to scoring the sentence.

#### Relevance 252

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 253

Retrieved by: Hybrid RRF followed by BGE reranking

> This approach consists of selecting from a hybrid set (hybr). This involves concatenating both the authentic candidate $S_{auth}$ and artificial $S_{synth}$ sentences as a first step and then executing the TAs with the new candidate set $S_{auth+synth}$.

#### Relevance 253

Label: 

#### Passage 254

Retrieved by: Hybrid RRF followed by BGE reranking

> In the first set of experiments we explore the hybr approach, i.e. the TAs are executed on a mixture of authentic and synthetic data (combined before the execution of the TA). We present the results of the models trained with these sets in Table TABREF20 (for INR) and Table TABREF21 (for FDA). In the first column, we include as the baseline the fine-tuned models presented in Table TABREF18.
> 
> The results in the tables show that increasing the size of the candidate pool is beneficial. We see that most scores are better (marked in bold) than the model fine-tuned with only authentic data. However, the performance is also dependent on the domain. When comparing BIO and NEWS subtables we see that the models adapted for the latter domain tend to achieve better performances as most of the scores are statistically significant improvements.
> 
> When analyzing the selected dataset we find that the authentic sentences constitute slightly above half (between 51% and 64% of the sentences). This is an indicator that artificially-generated sentences contain n-grams that can be found by TA and are as useful as authentic sentences.
> 
> In addition, the amount of duplicated target-side sentences is very low (between 10% and 13%). This indicates that the MT-generated sentences contain n-grams that are different from the authentic counterpart, which increases the variety of the candidates that are useful for the TA to select.
> 
> In Table TABREF22 and Table TABREF23 we present the results of the models when fine-tuned with a combination of authentic and synthetic data following the Combine Before Selection approaches in Section SECREF7. The tables are structured in two subtables showing the results of batch and online approaches. Each subtable present the results of three values of $\gamma $: 0.75, 0.50 and 0.25.
> 
> In these tables, we see that the performance of the models following the batch and online approaches is similar. These results are also in accord with those obtained following the hybr approach, as the improvements depend more on the domain (most evaluation scores in the NEWS test set indicate statistically significant improvements whereas for the BIO test set most of them are not) than the TA used, or the value of $\gamma $.

#### Relevance 254

Label: 

## Question 0029

Paper: Neural Collective Entity Linking

> How effective is their NCEL approach overall?

### Common Retrieved Chunks

#### Passage 255

Retrieved by: BM25, Hybrid RRF

> Local features focus on how compatible the entity is mentioned in a piece of text (i.e., the mention and the context words). Except for the prior probability (Section SECREF9 ), we define two types of local features for each candidate entity INLINEFORM0 :
> 
> String Similarity Similar to BIBREF16 , we define string based features as follows: the edit distance between mention's surface form and entity title, and boolean features indicating whether they are equivalent, whether the mention is inside, starts with or ends with entity title and vice versa.
> 
> Compatibility We also measure the compatibility of INLINEFORM0 with the mention's context words INLINEFORM1 by computing their similarities based on joint embeddings: INLINEFORM2 and INLINEFORM3 , where INLINEFORM4 is the context embedding of INLINEFORM5 conditioned on candidate INLINEFORM6 and is defined as the average sum of word global vectors weighted by attentions: INLINEFORM7
> 
> where INLINEFORM0 is the INLINEFORM1 -th word's attention from INLINEFORM2 . In this way, we automatically select informative words by assigning higher attention weights, and filter out irrelevant noise through small weights. The attention INLINEFORM3 is computed as follows: INLINEFORM4
> 
> where INLINEFORM0 is the similarity measurement, and we use cosine similarity in the presented work. We concatenate the prior probability, string based similarities, compatibility similarities and the embeddings of contexts as well as the entity as the local feature vectors.

#### Relevance 255

Label: 

#### Passage 256

Retrieved by: BM25, Dense, Hybrid RRF

> In this section, we investigate the effectiveness of NCEL in the “easy" and “hard" datasets, respectively. Particularly, TAC2010, which has two mentions per document on average (Section SECREF19 ) and high prior probabilities of correct candidates (Figure FIGREF28 ), is regarded as the “easy" case for EL, and WW is the “hard" case since it has the most mentions with balanced prior probabilities BIBREF19 . Besides, we further compare the impact of key modules by removing the following part from NCEL: global features (NCEL-local), attention (NCEL-noatt), embedding features (NCEL-noemb), and the impact of the prior probability (prior).
> 
> The results are shown in Table FIGREF28 and Table FIGREF28 . We can see the average linking precision (Micro) of WW is lower than that of TAC2010, and NCEL outperforms all baseline methods in both easy and hard cases. In the “easy" case, local models have similar performance with global models since only little global information is available (2 mentions per document). Besides, NN-based models, NTEE and NCEL-local, perform significantly better than others including most global models, demonstrating that the effectiveness of neural models deals with the first limitation in the introduction.
> 
> Impact of NCEL Modules
> 
> As shown in Figure FIGREF28 , the prior probability performs quite well in TAC2010 but poorly in WW. Compared with NCEL-local, the global module in NCEL brings more improvements in the “hard" case than that for “easy" dataset, because local features are discriminative enough in most cases of TAC2010, and global information becomes quite helpful when local features cannot handle. That is, our propose collective model is robust and shows a good generalization ability to difficult EL. The improvements by each main module are relatively small in TAC2010, while the modules of attention and embedding features show non-negligible impacts in WW (even worse than local model), mainly because WW contains much noise, and these two modules are effective in improving the robustness to noise and the ability of generalization by selecting informative words and providing more accurate semantics, respectively.

#### Relevance 256

Label: 

#### Passage 257

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> the coherence information of consistent topic “cricket" among adjacent mentions England, Hussain, and Essex. Although the global model has achieved significant improvements, its limitation is threefold:
> 
> To mitigate the first limitation, recent EL studies introduce neural network (NN) models due to its amazing feature abstraction and generalization ability. In such models, words/entities are represented by low dimensional vectors in a continuous space, and features for mention as well as candidate entities are automatically learned from data BIBREF4 . However, existing NN-based methods for EL are either local models BIBREF16 , BIBREF17 or merely use word/entity embeddings for feature extraction and rely on another modules for collective disambiguation, which thus cannot fully utilize the power of NN models for collective EL BIBREF18 , BIBREF19 , BIBREF20 .
> 
> The second drawback of the global approach has been alleviated through approximate optimization techniques, such as PageRank/random walks BIBREF21 , graph pruning BIBREF22 , ranking SVMs BIBREF23 , or loopy belief propagation (LBP) BIBREF18 , BIBREF24 . However, these methods are not differentiable and thus difficult to be integrated into neural network models (the solution for the first limitation).
> 
> To overcome the third issue of inadequate training data, BIBREF17 has explored a massive amount of hyperlinks in Wikipedia, but these potential annotations for EL contain much noise, which may distract a naive disambiguation model BIBREF6 .
> 
> In this paper, we propose a novel Neural Collective Entity Linking model (NCEL), which performs global EL combining deep neural networks with Graph Convolutional Network (GCN) BIBREF25 , BIBREF26 that allows flexible encoding of entity graphs. It integrates both local contextual information and global interdependence of mentions in a document, and is efficiently trainable in an end-to-end fashion. Particularly, we introduce attention mechanism to robustly model local contextual information by selecting informative words and filtering out the noise. On the other hand, we apply GCNs to improve discriminative signals of candidate entities by exploiting the rich structure underlying the correct entities. To alleviate the global computations, we propose to convolute on the subgraph of adjacent mentions. Thus, the overall coherence shall be achieved in a chain-like way via a sliding window over the document. To the best of our knowledge, this is the

#### Relevance 257

Label: 

#### Passage 258

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> NCEL incorporates GCN into a deep neural network to utilize structured graph information for collectively feature abstraction, while differs from conventional GCN in the way of applying the graph. Instead of the entire graph, only a subset of nodes is “visible" to each node in our proposed method, and then the overall structured information shall be reached in a chain-like way. Fixing the size of the subset, NCEL is further speeded up by batch techniques and GPUs, and is efficient to large-scale data.

#### Relevance 258

Label: 

#### Passage 261

Retrieved by: Dense, Hybrid RRF

> The results of example in Figure FIGREF1 are shown in Table TABREF30 , which is from CoNLL testa dataset. For mention Essex, although both NCEL and NCEL-local correctly identify entity Essex County Cricket Club, NCEL outputs higher probability due to the enhancement of neighbor mentions. Moreover, for mention England, NCEL-local cannot find enough disambiguation clues from its context words, such as surplus and requirements, and thus assigns a higher probability of 0.42 to the country England according to the prior probability. Collectively, NCEL correctly identifies England cricket team with a probability of 0.72 as compared with 0.20 in NCEL-local with the help of its neighbor mention Essex.

#### Relevance 261

Label: 

#### Passage 263

Retrieved by: Hybrid RRF, Hybrid RRF followed by BGE reranking

> the global computations, we propose to convolute on the subgraph of adjacent mentions. Thus, the overall coherence shall be achieved in a chain-like way via a sliding window over the document. To the best of our knowledge, this is the first effort to develop a unified model for neural collective entity linking.
> 
> In experiments, we first verify the efficiency of NCEL via theoretically comparing its time complexity with other collective alternatives. Afterwards, we train our neural model using collected Wikipedia hyperlinks instead of dataset-specific annotations, and perform evaluations on five public available benchmarks. The results show that NCEL consistently outperforms various baselines with a favorable generalization ability. Finally, we further present the performance on a challenging dataset WW BIBREF19 as well as qualitative results, investigating the effectiveness of each key module.

#### Relevance 263

Label: 

### BM25

#### Passage 259

Retrieved by: BM25

> similarities between INLINEFORM0 and all neighbor mentions: INLINEFORM1 , where INLINEFORM2 is the mention embedding by averaging the global vectors of words in its surface form: INLINEFORM3 , where INLINEFORM4 are tokenized words of mention INLINEFORM5 .
> 
> Subgraph Structure The above features reflect the consistent semantics in texts (i.e., mentions). We now extract structured global features using the relations in KB, which facilitates the inference among candidates to find the most topical coherent subset. For each document, we obtain the entity graph INLINEFORM0 by taking candidate entities of all mentions INLINEFORM1 as nodes, and using entity embeddings to compute their similarities as edges INLINEFORM2 . Then, we extract the subgraph structured features INLINEFORM3 for each entity INLINEFORM4 for efficiency.
> 
> Formally, we define the subgraph as: INLINEFORM0 , where INLINEFORM1 . For example (Figure FIGREF1 ), for entity England cricket team, the subgraph contains the relation from it to all candidates of neighbor mentions: England cricket team, Nasser Hussain (rugby union), Nasser Hussain, Essex, Essex County Cricket Club and Essex, New York. To support batch-wise acceleration, we represent INLINEFORM2 in the form of adjacency table based vectors: INLINEFORM3 , where INLINEFORM4 is the number of candidates per mention.
> 
> Finally, for each candidate INLINEFORM0 , we concatenate local features and neighbor mention compatibility scores as the feature vector INLINEFORM1 , and construct the subgraph structure representation INLINEFORM2 as the inputs of NCEL.

#### Relevance 259

Label: 

### Dense

#### Passage 260

Retrieved by: Dense

> To avoid overfitting with some dataset, we train NCEL using collected Wikipedia hyperlinks instead of specific annotated data. We then evaluate the trained model on five different benchmarks to verify the linking precision as well as the generalization ability. Furthermore, we investigate the effectiveness of key modules in NCEL and give qualitative results for comprehensive analysis.

#### Relevance 260

Label: 

#### Passage 262

Retrieved by: Dense

> Training We collect 50,000 Wikipedia articles according to the number of its hyperlinks as our training data. For efficiency, we trim the articles to the first three paragraphs leading to 1,035,665 mentions in total. Using CoNLL-Test A as the development set, we evaluate the trained NCEL on the above benchmarks. We set context window to 20, neighbor mention window to 6, and top INLINEFORM0 candidates for each mention. We use two layers with 2000 and 1 hidden units in MLP encoder, and 3 layers in sub-GCN. We use early stop and fine tune the embeddings. With a batch size of 16, nearly 3 epochs cost less than 15 minutes on the server with 20 core CPU and the GeForce GTX 1080Ti GPU with 12Gb memory. We use standard Precision, Recall and F1 at mention level (Micro) and at the document level (Macro) as measurements.
> 
> Complexity Analysis Compared with local methods, the main disadvantage of collective methods is high complexity and expensive costs. Suppose there are INLINEFORM0 mentions in documents on average, among these global models, NCEL not surprisingly has the lowest time complexity INLINEFORM1 since it only considers adjacent mentions, where INLINEFORM2 is the number of sub-GCN layers indicating the iterations until convergence. AIDA has the highest time complexity INLINEFORM3 in worst case due to exhaustive iteratively finding and sorting the graph. The LBP and PageRank/random walk based methods achieve similar high time complexity of INLINEFORM4 mainly because of the inference on the entire graph.

#### Relevance 262

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 264

Retrieved by: Hybrid RRF followed by BGE reranking

> The main goal of NCEL is to find a solution for collective entity linking using an end-to-end neural model, rather than to improve the measurements of local textual similarity or global mention/entity relatedness. Therefore, we use joint embeddings of words and entities at sense level BIBREF28 to represent mentions and its contexts for feature extraction. In this section, we give a brief description of our embeddings followed by our features used in the neural model.

#### Relevance 264

Label: 

#### Passage 265

Retrieved by: Hybrid RRF followed by BGE reranking

> The key idea of collective EL is to utilize the topical coherence throughout the entire document. The consistency assumption behind it is that: all mentions in a document shall be on the same topic. However, this leads to exhaustive computations if the number of mentions is large. Based on the observation that the consistency attenuates along with the distance between two mentions, we argue that the adjacent mentions might be sufficient for supporting the assumption efficiently.
> 
> Formally, we define neighbor mentions as INLINEFORM0 adjacent mentions before and after current mention INLINEFORM1 : INLINEFORM2 , where INLINEFORM3 is the pre-defined window size. Thus, the topical coherence at document level shall be achieved in a chain-like way. As shown in Figure FIGREF10 ( INLINEFORM4 ), mentions Hussain and Essex, a cricket player and the cricket club, provide adequate disambiguation clues to induce the underlying topic “cricket" for the current mention England, which impacts positively on identifying the mention surrey as another cricket club via the common neighbor mention Essex.
> 
> A degraded case happens if INLINEFORM0 is large enough to cover the entire document, and the mentions used for global features become the same as the previous work, such as BIBREF21 . In experiments, we heuristically found a suitable INLINEFORM1 which is much smaller than the total number of mentions. The benefits of efficiency are in two ways: (i) to decrease time complexity, and (ii) to trim the entity graph into a fixed size of subgraph that facilitates computation acceleration through GPUs and batch techniques, which will be discussed in Section SECREF24 .
> 
> Given neighbor mentions INLINEFORM0 , we extract two types of vectorial global features and structured global features for each candidate INLINEFORM1 :
> 
> Neighbor Mention Compatibility Suppose neighbor mentions are topical coherent, a candidate entity shall also be compatible with neighbor mentions if it has a high compatibility score with the current mention, otherwise not. That is, we extract the vectorial global features by computing the similarities between INLINEFORM0 and all neighbor mentions: INLINEFORM1 , where INLINEFORM2 is the mention embedding by averaging the global vectors of words in its surface form: INLINEFORM3 , where INLINEFORM4 are tokenized words of mention INLINEFORM5 .
> 
> Subgraph Structure The

#### Relevance 265

Label: 

## Question 0030

Paper: Identifying Nuances in Fake News vs. Satire: Using Semantic and Linguistic Cues

> What nuances between fake news and satire were discovered?

### Common Retrieved Chunks

#### Passage 266

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We addressed the challenge of identifying nuances between fake news and satire. Inspired by the humor and social message aspects of satire articles, we tested two classification approaches based on a state-of-the-art contextual language model, and linguistic features of textual coherence. Evaluation of our methods pointed to the existence of semantic and linguistic differences between fake news and satire. In particular, both methods achieved a significantly better performance than the baseline language-based method. Lastly, we studied the feature importance of our linguistic-based method to help shed light on the nuances between fake news and satire. For instance, we observed that satire articles are more sophisticated, or less easy to read, than fake news articles.
> 
> Overall, our contributions, with the improved classification accuracy and towards the understanding of nuances between fake news and satire, carry great implications with regard to the delicate balance of fighting misinformation while protecting free speech.
> 
> For future work, we plan to study additional linguistic cues, and specifically humor related features, such as absurdity and incongruity, which were shown to be good indicators of satire in previous work. Another interesting line of research would be to investigate techniques of identifying whether a story carries a political or social message, for example, by comparing it with timely news information.

#### Relevance 266

Label: 

#### Passage 267

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> fake news can be distinguished with a word-based classification approach, our work is focused on the semantic and linguistic properties of the content. Inspired by the distinctive aspects of satire with regard to humor and social message, our hypothesis is that using semantic and linguistic cues can help to capture these nuances.
> 
> Our main research questions are therefore, RQ1) are there semantic and linguistic differences between fake news and satire stories that can help to tell them apart?; and RQ2) can these semantic and linguistic differences contribute to the understanding of nuances between fake news and satire beyond differences in the language being used?
> 
> The rest of paper is organized as follows: in section SECREF2, we briefly review studies on fake news and satire articles which are the most relevant to our work. In section SECREF3, we present the methods we use to investigate semantic and linguistic differences between fake and satire articles. Next, we evaluate these methods and share insights on nuances between fake news and satire in section SECREF4. Finally, we conclude the paper in section SECREF5 and outline next steps and future work.

#### Relevance 267

Label: 

#### Passage 268

Retrieved by: BM25, Hybrid RRF

> Previous work addressed the challenge of identifying fake news BIBREF3, BIBREF4, or identifying satire BIBREF5, BIBREF6, BIBREF7, in isolation, compared to real news stories.
> 
> The most relevant work to ours is that of Golbeck et al. BIBREF1. They introduced a dataset of fake news and satirical articles, which we also employ in this work. The dataset includes the full text of 283 fake news stories and 203 satirical stories, that were verified manually, and such that each fake news article is paired with a rebutting article from a reliable source. Albeit relatively small, this data carries two desirable properties. First, the labeling is based on the content and not the source, and the stories spread across a diverse set of sources. Second, both fake news and satire articles focus on American politics and were posted between January 2016 and October 2017, minimizing the possibility that the topic of the article will influence the classification.
> 
> In their work, Golbeck et al. studied whether there are differences in the language of fake news and satirical articles on the same topic that could be utilized with a word-based classification approach. A model using the Naive Bayes Multinomial algorithm is proposed in their paper which serves as the baseline in our experiments.

#### Relevance 268

Label: 

#### Passage 269

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The efforts by social media platforms to reduce the exposure of users to misinformation have resulted, on several occasions, in flagging legitimate satire stories. To avoid penalizing publishers of satire, which is a protected form of speech, the platforms have begun to add more nuance to their flagging systems. Facebook, for instance, added an option to mark content items as “Satire”, if “the content is posted by a page or domain that is a known satire publication, or a reasonable person would understand the content to be irony or humor with a social message” BIBREF0. This notion of humor and social message is also echoed in the definition of satire by Oxford dictionary as “the use of humour, irony, exaggeration, or ridicule to expose and criticize people's stupidity or vices, particularly in the context of contemporary politics and other topical issues”.
> 
> The distinction between fake news and satire carries implications with regard to the exposure of content on social media platforms. While fake news stories are algorithmically suppressed in the news feed, the satire label does not decrease the reach of such posts. This also has an effect on the experience of users and publishers. For users, incorrectly classifying satire as fake news may deprive them from desirable entertainment content, while identifying a fake news story as legitimate satire may expose them to misinformation. For publishers, the distribution of a story has an impact on their ability to monetize content.
> 
> Moreover, in response to these efforts to demote misinformation, fake news purveyors have begun to masquerade as legitimate satire sites, for instance, carrying small badges at the footer of each page denoting the content as satire BIBREF1. The disclaimers are usually small such that the stories are still being spread as though they were real news BIBREF2.
> 
> This gives rise to the challenge of classifying fake news versus satire based on the content of a story. While previous work BIBREF1 have shown that satire and fake news can be distinguished with a word-based classification approach, our work is focused on the semantic and linguistic properties of the content. Inspired by the distinctive aspects of satire with regard to humor and social message, our hypothesis is

#### Relevance 269

Label: 

#### Passage 270

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> With regard to research question RQ2 on the understanding of semantic and linguistic nuances between fake news and satire - a key advantage of studying the coherence metrics is explainability. While the pre-trained model of BERT gives the best result, it is not easily interpretable. The coherence metrics allow us to study the differences between fake news and satire in a straightforward manner.
> 
> Observing the significant features, in bold in Table TABREF3, we see a combination of surface level related features, such as sentence length and average word frequency, as well as semantic features including LSA (Latent Semantic Analysis) overlaps between verbs and between adjacent sentences. Semantic features which are associated with the gist representation of content are particularly interesting to see among the predictors since based on Fuzzy-trace theory BIBREF13, a well-known theory of decision making under risk, gist representation of content drives individual's decision to spread misinformation online. Also among the significant features, we observe the causal connectives, that are proven to be important in text comprehension, and two indices related to the text easability and readability, both suggesting that satire articles are more sophisticated, or less easy to read, than fake news articles.

#### Relevance 270

Label: 

### BM25

None

### Dense

#### Passage 271

Retrieved by: Dense

> In the following subsections, we investigate the semantic and linguistic differences of satire and fake news articles.

#### Relevance 271

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 272

Retrieved by: Hybrid RRF followed by BGE reranking

> To study the semantic nuances between fake news and satire, we use BERT BIBREF8, which stands for Bidirectional Encoder Representations from Transformers, and represents a state-of-the-art contextual language model. BERT is a method for pre-training language representations, meaning that it is pre-trained on a large text corpus and then used for downstream NLP tasks. Word2Vec BIBREF9 showed that we can use vectors to properly represent words in a way that captures semantic or meaning-related relationships. While Word2Vec is a context-free model that generates a single word-embedding for each word in the vocabulary, BERT generates a representation of each word that is based on the other words in the sentence. It was built upon recent work in pre-training contextual representations, such as ELMo BIBREF10 and ULMFit BIBREF11, and is deeply bidirectional, representing each word using both its left and right context. We use the pre-trained models of BERT and fine-tune it on the dataset of fake news and satire articles using Adam optimizer with 3 types of decay and 0.01 decay rate. Our BERT-based binary classifier is created by adding a single new layer in BERT's neural network architecture that will be trained to fine-tune BERT to our task of classifying fake news and satire articles.

#### Relevance 272

Label: 

## Question 0031

Paper: A Framework for the Computational Linguistic Analysis of Dehumanization

> How do they identify discussions of LGBTQ people in the New York Times?

### Common Retrieved Chunks

#### Passage 273

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> they are important to a newspaper's framing of an issue, as particular quotes representing specific stances are intentionally included or excluded from any given article BIBREF69. However, this approach is sometimes problematic when the newspaper quotes clearly extreme positions that they are unlikely to agree with, and we discuss this issue throughout our qualitative analysis.
> 
> We refer to the remaining subset of the New York Times data after filtering as the LGBTQ corpus. The LGBTQ corpus consists of 93,977 paragraphs and 7.36 million tokens. However, a large increase in reporting on LGBTQ-related issues has led to a highly skewed distribution in the amount of data over years, with 1986 containing the least data (1144 paragraphs and 73,549 tokens) and 2012 containing the most (5924 paragraphs and 465,254 tokens).
> 
> For all experiments, we also include results for the terms American and Americans. Our primary motivation for including American(s) is to contrast changes in LGBTQ labels' representation in the New York Times with another social group label that appears in sufficiently different contexts. This ensures that the changes we find in dehumanizing language towards LGBTQ groups do not apply uniformly to all social groups, and are thus not merely an artifact of the publication's overall language change. While a natural “control" variable would be labels such as straight or heterosexual, we found that these terms only occurred within discussions of LGBTQ communities, likely because they name socially unmarked categories. We also considered comparing LGBTQ labels to person/people, but we found that the word embedding-based experiments were particularly sensitive to syntactic forms, so we selected a word that behaves more similarly syntactically to gay and homosexual, particularly by having both nominal and adjectival uses. Nevertheless, it is important to note that American(s) is by no means a neutral control variable. Because of its in-group status for the New York Times (a U.S. institution), we expect our measurements to show that American(s) appears in more humanizing contexts than LGBTQ group labels; however, we do not expect to find substantial changes in the use of American(s) over time.
> 
> Figure FIGREF20 shows the counts of group labels for each year in the New York Times from 1986 to 2015. For visualization

#### Relevance 273

Label: 

#### Passage 274

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Because we apply our framework to study dehumanizing language in discussions about LGBTQ communities in the New York Times, some background is necessary. Overall, the American public has become more accepting of LGBTQ people and supportive of their rights. In 1977, equal percentages of respondents (43%) agreed and disagreed with the statement that gay or lesbian relations between consenting adults should be legal BIBREF2. Approval of gay and lesbian relations then decreased in the 1980s; in 1986, only 32% of respondents believed they should be legal. According to Gallup, attitudes have become increasingly positive since the 1990s, and in 2019, 73% responded that gay or lesbian relations should be legal. The Pew Research center began surveying Americans about their beliefs about same-sex marriage in 2001 and found similar trends BIBREF51. Between 2001 and 2019, support for same-sex marriage among respondents jumped from 35% to 61%.
> 
> In addition to the public's overall attitudes, it is important to consider variation and change in the specific words used to refer to LGBTQ people. Because these labels potentially convey many different social meanings and have different relationships with dehumanization in the media, a primary focus of this study involves comparing different LGBTQ labels, specifically gay and homosexual. The Gallup survey asked for opinions on legality of “homosexual relations" until 2008, but then changed the wording to “gay and lesbian relations". This was likely because many people who identify as gay and lesbian find the word homosexual to be outdated and derogatory. According to the LGBTQ media monitoring organization GLAAD, homosexual's offensiveness originates in the word's dehumanizing clinical history, which had falsely suggested that “people attracted to the same sex are somehow diseased or psychologically/emotionally disordered" . Beyond its outdated clinical associations, some argue that the word homosexual is more closely associated with sex and all of its negative connotations simply by virtue of containing the word sex, while terms such as gay and lesbian avoid such connotations BIBREF52. Most newspapers, including the New York Times, almost exclusively used the word homosexual in articles about gay and lesbian people until the late 1980s BIBREF53. The New York Times began using the word gay in non-quoted text in 1987. Many major

#### Relevance 274

Label: 

#### Passage 275

Retrieved by: BM25, Hybrid RRF

> Drawing upon this rich body of literature, we first identify clear linguistic analogs for these components and propose several computational techniques to measure these linguistic correlates. We then apply this general framework to explore changing representations of LGBTQ groups in the New York Times over the span of three decades. We additionally use this lens of dehumanization to investigate differences in social meaning between the denotationally-similar labels gay and homosexual.
> 
> This paper aims to bridge the gaps between computational modeling, sociolinguistics, and dehumanization research with implications for several disciplines. In addition to enabling large-scale studies of dehumanizing language and media representation of marginalized social groups, these techniques can be built into systems that seek to capture both conscious and unconscious biases in text. Furthermore, this work has implications for improving machines' abilities to automatically detect hate speech and abusive language online, which are typically underpinned by dehumanizing language. Finally, our case study demonstrates that such computational analyses of discussions about marginalized groups can provide unique insights into language variation and change within sensitive sociopolitical contexts, and help us understand how people (and institutions) use language to express their ideologies and attitudes towards certain social groups.

#### Relevance 275

Label: 

#### Passage 276

Retrieved by: BM25, Dense, Hybrid RRF

> newspapers, including the New York Times, almost exclusively used the word homosexual in articles about gay and lesbian people until the late 1980s BIBREF53. The New York Times began using the word gay in non-quoted text in 1987. Many major newspapers began restricting the use of the word homosexual in 2006 BIBREF52. As of 2013, the New York Times has confined the use of homosexual to specific references to sexual activity or clinical orientation, in addition to direct quotes and paraphrases .
> 
> Beyond differences in how LGBTQ people perceive the terms gay or lesbian relative to homosexual, it has been shown that the specific choice of label can also have an effect on attitudes towards LGBTQ people. In 2012, BIBREF54 asked survey respondents about either “gay and lesbian rights" or “homosexual rights". Respondents who read the word “homosexual" tended to show less support for LGBTQ rights. This effect was primarily driven by high authoritarians, people who show high sensitivity to intergroup distinctions. The authors posit that homosexual makes social group distinctions more blatant than gay or lesbian, which then leads to a greater degree of psychological distancing, thus enabling participants to further remove LGBTQ people from their realm of moral consideration BIBREF54. Based on prior research and evolving media guidelines, we expect our computational analysis to show that homosexual occurs in more dehumanizing contexts than other LGBTQ labels, such as gay.

#### Relevance 276

Label: 

#### Passage 278

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The data for our case study spans over thirty years of articles from the New York Times, from January 1986 to December 2015, and was originally collected by BIBREF68 BIBREF68. The articles come from all sections of the newspaper, such as “World", “New York & Region", “Opinion", “Style", and “Sports". Our distributional semantic methods rely on all of the available data in order to obtain the most fine-grained understanding of the relationships between words possible. For the other techniques, we extract paragraphs containing any word from a predetermined list of LGTBQ terms (shown in Table TABREF19).
> 
> Each acronym label was matched insensitive to case and punctuation. Some currently prominent LGBTQ terms, such as queer and trans were not included in this study, as other senses of these words were considerably more frequent in earlier years. We further filtered out paragraphs from sections that typically did not pertain to news, such as “Arts", “Theater", and “Movies". While these sections could provide valuable information, we decided to focus on representation of LGBTQ groups in more news-related contexts. Furthermore, due to the original newspaper layout and subsequent digital processing, Arts sections often contained extremely long paragraphs containing numerous listings and schedules. Removing these sections substantially simplified data processing.
> 
> A challenging question when analyzing mass media for subjective attitudes is deciding whose perspective we want to capture: an individual reporter, the institution, or society at large? In this case study, we aim to identify the institution's dehumanizing attitudes towards LGBTQ people. We represent the New York Times institution as a combination of the journalists' words in news articles, direct quotes, paraphrases from interviews, and published opinion articles. Therefore, despite our news focus, we include data from “Opinion" sections; while opinion articles are stylistically different from traditional journalistic reporting due to more overt biases and arguments, these articles are important in constructing the institution's perspective. In addition, we consider all text in each relevant paragraph, including quotes and paraphrases, because they are important to a newspaper's framing of an issue, as particular quotes representing specific stances are intentionally included or excluded from any given article BIBREF69. However, this approach is sometimes problematic when the newspaper quotes clearly extreme positions that

#### Relevance 278

Label: 

### BM25

#### Passage 277

Retrieved by: BM25

> Metaphors comparing humans to vermin have been especially prominent in dehumanizing groups throughout history BIBREF4, BIBREF15. Although no New York Times writers directly compare LGBTQ people to vermin, this metaphor may be invoked in more subtle ways. Furthermore, several paragraphs in the data demonstrate that people explicitly mention the metaphor in order to argue against it. These examples, shown in Table TABREF62, further point to the existence of LGBTQ people-as-vermin metaphors, even if they are not frequently directly invoked.

#### Relevance 277

Label: 

### Dense

#### Passage 279

Retrieved by: Dense

> significantly increases in paragraph-level valence, while homosexual may be trending downward, although this trend does not reach significance in our data ($p = 0.078$).
> 
> The paragraph-level valence analysis shown in Figure FIGREF27 suggests that LGBTQ groups have become increasingly positively evaluated over time, and have thus likely been less dehumanized in the New York Times. However, the lack of a statistically significant increase (rather, a slight downward trend) in average valence for paragraphs containing homosexual between 2001 and 2015 suggests that attitudes towards and evaluations of people described as homosexual have not improved in the same way as those described by other LGBTQ labels.
> 
> Finally, this measurement does not support our initial hypothesis that LGBTQ groups have been more negatively evaluated than the other social group American(s), but does reveal that the observed trend for LGBTQ labels is not merely an artifact of changing reporting styles, since paragraphs containing American(s) show a very different pattern. Overall, this result demonstrates substantial language change in the New York Times's discussion of LGBTQ people as well as variation in the contexts where different group labels appear, particularly homosexual.

#### Relevance 279

Label: 

#### Passage 280

Retrieved by: Dense

> have its own biases and does not capture the entirety of media discourse about LGBTQ people. Furthermore, we only studied newspaper articles written in (Standard) American English. Future work could assess how well these linguistic cues we measure generalize to other languages and focus on cross-linguistic comparisons of dehumanizing language. Finally, most of our case study involved analysis of an aggregated LGBTQ representation,with a specific focus on the labels gay and homosexual, primarily due to the amount of data available. However, as a result, we still have little understanding about the nuanced differences and changes in the representation of LGBTQ people who don't identify with (or aren't identified as) these labels.

#### Relevance 280

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 281

Retrieved by: Hybrid RRF followed by BGE reranking

> makes them categorically and fundamentally different), and denial of subjectivity (neglect of a target group member's personal feelings and experiences). BIBREF75, BIBREF21, BIBREF76, BIBREF3. Scholars also often differentiate between two forms of dehumanization, animalistic (likening humans to animals) and mechanistic (likening humans to inanimate objects or machines), and the linguistic signals underpinning each of these forms could substantially differ from one another BIBREF4.
> 
> For simplicity and ease of interpretation, we focus on quantifying lexical cues of dehumanization. However, our understanding of the language of dehumanization would be enriched by considering linguistic features beyond the lexicon. For example, BIBREF77 has shown that definite plurals in English (e.g. the gays) have a unique social and pragmatic effect compared to bare plurals (e.g. gays) by packaging individual entities into one monolith and setting this group apart from the speaker. Indexing a speaker's non-membership in the group being discussed creates social distance between the speaker and group BIBREF77, which makes it likely that using definite plurals to label marginalized social groups plays an important role in dehumanization. Similarly, examining non-lexical signals could help us capture elements of dehumanization that we could not easily identify only through lexical resources. For example, the part of speech of a group label (such as gay as a noun or adjective) could have implications for essentialism, as adjectives simply name attributes to some entity, while nouns explicitly state the entity's category membership and encapsulates other stereotypes associated with that category BIBREF78, BIBREF79, BIBREF76, BIBREF80. We furthermore believe that incorporating discourse-level analysis, such as examining the role of direct quotes in an article and who is being quoted, could provide informative insights that could address some limitations discussed earlier.
> 
> We supported our proposed framework with a case study of LGBTQ representation in the New York Times. This case study had a number of limitations as an analysis of the dehumanization of LGBTQ people in the media. We only looked at one data source, which may have its own biases and does not capture the entirety of media discourse about LGBTQ people. Furthermore, we only studied newspaper articles written in (Standard) American English. Future work could assess how well these linguistic cues we measure generalize to

#### Relevance 281

Label: 

#### Passage 282

Retrieved by: Hybrid RRF followed by BGE reranking

> Despite the American public's increasing acceptance of LGBTQ people and recent legal successes, LGBTQ individuals frequently remain the targets of hate and violence BIBREF0, BIBREF1, BIBREF2. At the core of this issue is dehumanization, “the act of perceiving or treating people as less than human” BIBREF3, a process that heavily contributes to extreme intergroup bias BIBREF4. Language is central to studying this phenomenon; like other forms of bias BIBREF5, BIBREF6, BIBREF7, BIBREF8, BIBREF9, dehumanizing attitudes are expressed through subtle linguistic manipulations, even in carefully-edited texts. It is crucial to understand the use of such linguistic signals in mainstream media, as the media's representation of marginalized social groups has far-reaching implications for social acceptance, policy, and safety.
> 
> While small-scale studies of dehumanization and media representation of marginalized communities provide valuable insights (e.g. BIBREF10), there exist no known large-scale analyses, likely due to difficulties in quantifying such a subjective and multidimensional psychological process. However, the ability to do large-scale analysis is crucial for understanding how dehumanizing attitudes have evolved over long periods of time. Furthermore, by being able to account for a greater amount of media discourse at once, large-scale techniques can provide a more complete view of the media environment to which the public is exposed.
> 
> Linguistics and computer science offer valuable methods and insights on which such large-scale techniques might be developed for the study of dehumanization. By leveraging more information about the contexts in which marginalized groups are discussed, computational linguistic methods not only enable large-scale study of a complex psychological phenomenon, but can even reveal linguistic variations and changes that are not easily identifiable through qualitative analysis alone.
> 
> In this work, we develop a computational linguistic framework for analyzing dehumanizing language, with a focus on lexical signals of dehumanization. Social psychologists have identified numerous components of dehumanization, such as negative evaluations of a target group, denial of agency, moral disgust, and likening members of a target group to non-human entities such as vermin. Drawing upon this rich body of literature, we first identify clear linguistic analogs for these components and propose several computational techniques to measure these linguistic correlates. We then apply this general framework to explore changing representations of LGBTQ groups in

#### Relevance 282

Label: 

## Question 0032

Paper: Incremental Improvement of a Question Answering System by Re-ranking Answer Candidates using Machine Learning

> What QA system was used in this work?

### Common Retrieved Chunks

#### Passage 283

Retrieved by: BM25, Dense, Hybrid RRF

> In this work, we include two corpora: one for training the baseline system and another for evaluating the performance of the QA pipeline and our re-ranking approach. In the following, we describe the creation of the training corpus and the structure of the test corpus. Both corpora have been anonymised.
> 
> Training Corpus. The customer care department provides 877 answers to common user questions. Each answer is tagged with a variable amount of keywords or key-phrases ( INLINEFORM0 , INLINEFORM1 ), 3338 in total. We asked students to augment the training corpus with, in total, two additional natural example queries. This process can be scaled by crowdsourcing for an application in productive systems that might include more answers or that requires more sample question per answer or both. The full dataset contains, on average, INLINEFORM2 sample queries per answer totalling in 5092 queries overall. For model training, all questions (including keywords) are used as input with the corresponding answer as output. We generated three versions of the training corpus: keywords only (kw, INLINEFORM3 ), keywords with samples from 1 user (kw+1u, INLINEFORM4 ) and keywords with samples from 2 users (kw+2u, INLINEFORM5 ).
> 
> Evaluation Corpus.
> 
> The performance of the implemented QA system and of our re-ranking approach is assessed using a separate test corpus. It includes 3084 real user requests from a chat-log of T-Mobile Austria, which are assigned to suitable answers from the training corpus (at most three). The assignment was performed manually by domain experts of the wireless network provider. We use this corpus for estimating the baseline performance of the QA pipeline using different pipeline configurations and different versions of the training corpus. In addition, we use the corpus for evaluating our re-ranking approach per cross-validation: we regard the expert annotations as offline human feedback. The queries in this corpus contain a lot of spelling mistakes. We address this in our QA pipeline generation by implementing a custom spell-checking component.

#### Relevance 283

Label: 

#### Passage 284

Retrieved by: BM25, Dense, Hybrid RRF

> In this work, we examine the problem of incrementally improving deployed QA systems in an industrial setting. We consider the domain of customer care of a wireless network provider and focus on answering frequent questions (focussing on the long tail of the question distribution BIBREF0 ). In this setting, the most frequent topics are covered by a separate industry-standard chatbot based on hand-crafted rules by dialogue engineers. Our proposed process is based on the augmented cross-industry standard process for data mining BIBREF1 (augmented CRISP data mining cycle). In particular, we are interested in methods for improving a model after its deployment through re-ranking of the initial ranking results. In advance, we follow the steps of the CRISP cycle towards deployment for generating a state-of-the-art baseline QA model. First, we examine existing data (data understanding) and prepare a corpus for training (data preparation). Second, we implement and train a QA pipeline using state-of-the-art open source components (modelling). We perform an evaluation using different amounts of data and different pipeline configurations (evaluation), also to understand the nature of the data and the application (business understanding). Third, we investigate the effectiveness and efficiency of re-ranking in improving our QA pipeline after the deployment phase of CRISP. Adaptivity after deployment is modelled as (automatic) operationalisation step with external reflection based on, e.g., user feedback. This could be replaced by introspective meta-models that allow the system to enhance itself by metacognition BIBREF1 . The QA system and the re-ranking approach are evaluated using a separate test set that maps actual user queries from a chat-log to answers of the QA corpus. Sample queries from the evaluation set with one correct and one incorrect sample are shown in Table TABREF1 .
> 
> With this work, we want to answer the question whether a deployed QA system that is difficult to adapt and that provides a top-10 ranking of answer candidates, can be improved by an additional re-ranking step that corresponds to the operationalisation step of the augmented CRISP cycle. It is also important to know the potential gain and the limitations of such a method that works on top of an existing system. We hypothesise that our proposed re-ranking approach can effectively

#### Relevance 284

Label: 

#### Passage 285

Retrieved by: BM25, Hybrid RRF

> The broad field of QA includes research ranging from retrieval-based BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 to generative BIBREF6 , BIBREF7 , as well as, from closed-domain BIBREF8 , BIBREF9 to open-domain QA BIBREF7 , BIBREF10 , BIBREF11 , BIBREF12 . We focus on the notion of improving an already deployed system.
> 
> For QA dialogues based on structured knowledge representations, this can be achieved by maintaining and adapting the knowledgebase BIBREF13 , BIBREF14 , BIBREF15 . In addition, BIBREF1 proposes metacognition models for building self-reflective and adaptive AI systems, e.g., dialogue systems, that improve by introspection. Buck et al. present a method for reformulating user questions: their method automatically adapts user queries with the goal to improve the answer selection of an existing QA model BIBREF16 .
> 
> Other works suggest humans-in-the-loop for improving QA systems. Savenkov and Agichtein use crowdsourcing for re-ranking retrieved answer candidates in a real-time QA framework BIBREF17 . In Guardian, crowdworkers prepare a dialogue system based on a certain web API and, after deployment, manage actual conversations with users BIBREF18 . EVORUS learns to select answers from multiple chatbots via crowdsourcing BIBREF19 . The result is a chatbot ensemble excels the performance of each individual chatbot. Williams et al. present a dialogue architecture that continuously learns from user interaction and feedback BIBREF20 .
> 
> We propose a re-ranking algorithm similar to BIBREF17 : we train a similarity model using n-gram based features of QA pairs for improving the answer selection of a retrieval-based QA system.

#### Relevance 285

Label: 

#### Passage 286

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We implemented a simple re-ranking method and showed that it can effectively improve the performance of QA systems after deployment. Our approach includes the top-10 answer candidates and confidences of the initial ranking for selecting better answers. Promising directions for future work include the investigation of more advanced ranking approaches for increasing the performance gain and continuous improvements through crowdsourcing and active learning.

#### Relevance 286

Label: 

#### Passage 287

Retrieved by: BM25, Dense, Hybrid RRF

> Our re-ranking approach compares a user query with the top-10 results of the baseline QA system. In contrast to the initial ranking, our re-ranking takes the content of the answer candidates into account instead of encoding the user query only. Our algorithm compares the text of the recent user query to each result. We include the answer text and the confidence value of the baseline system for computing a similarity estimate. Finally, we re-rank the results by their similarity to the query (see Algorithm SECREF5 ).
> 
> a user query INLINEFORM0 ; the corresponding list of top-10 results INLINEFORM1 including an answer INLINEFORM2 and the baseline confidence INLINEFORM3 ; an updated ranking INLINEFORM4 INLINEFORM5 INLINEFORM6 INLINEFORM7 INLINEFORM8 sort R' by confidences c', descending INLINEFORM9 INLINEFORM10 Re-Ranking Algorithm
> 
> We consider a data-driven similarity function that compares linguistic features of the user query and answer candidates and also takes into account the confidence of the baseline QA system. This similarity estimate shall enhance the baseline by using an extended data and feature space, but without neglecting the learned patterns of the baseline system. The possible improvement in top-1 accuracy is limited by the top-10 accuracy of the baseline system ( INLINEFORM0 ), because our re-ranking cannot choose from the remaining answers. Figure FIGREF12 shows how the re-ranking model is connected to the deployed QA system: it requires access to its in- and outputs for the additional ranking step.
> 
> We consider the gradient boosted regression tree for learning a similarity function for re-ranking similar to BIBREF17 . The features for model training are extracted from pre-processed query-answer pairs. Pre-processing includes tokenization and stemming of query and answer and the extraction of uni-, bi- and tri-grams from both token sequences. We include three distance metrics as feature: the Jaccard distance, the cosine similarity, and the plain number of n-gram matches between n-grams of a query and an answer.
> 
> a train- and test split of the evaluation corpus INLINEFORM0 , each including QA-pairs as tuples INLINEFORM1 ; the pre-trained baseline QA model for initial ranking INLINEFORM2 and the untrained re-ranking model INLINEFORM3 . evaluation metrics. training of the re-ranking model INLINEFORM4 INLINEFORM5 INLINEFORM6 INLINEFORM7 *R contains top-10 results INLINEFORM8 continue with

#### Relevance 287

Label: 

#### Passage 288

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> operationalisation step of the augmented CRISP cycle. It is also important to know the potential gain and the limitations of such a method that works on top of an existing system. We hypothesise that our proposed re-ranking approach can effectively improve ranking-based QA systems.

#### Relevance 288

Label: 

### BM25

None

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 289

Retrieved by: Hybrid RRF followed by BGE reranking

> analysed using such a meta-model to guide the sample selection for costly human data augmentation and creation. An example of a crowdsourcing approach that could be applied to our QA system and data, with search logs can be found in BIBREF0 .

#### Relevance 289

Label: 

#### Passage 290

Retrieved by: Hybrid RRF followed by BGE reranking

> including QA-pairs as tuples INLINEFORM1 ; the pre-trained baseline QA model for initial ranking INLINEFORM2 and the untrained re-ranking model INLINEFORM3 . evaluation metrics. training of the re-ranking model INLINEFORM4 INLINEFORM5 INLINEFORM6 INLINEFORM7 *R contains top-10 results INLINEFORM8 continue with next QA pair add positive sample INLINEFORM9 *confidence for INLINEFORM10 INLINEFORM11 INLINEFORM12 add negative sample INLINEFORM13 random INLINEFORM14 INLINEFORM15 INLINEFORM16 INLINEFORM17 INLINEFORM18 evaluation of the re-ranking model INLINEFORM19 INLINEFORM20 INLINEFORM21 *top-10 baseline ranking INLINEFORM22 *apply re-ranking INLINEFORM23 INLINEFORM24 Evaluation Procedure (per Data Split)

#### Relevance 290

Label: 

#### Passage 291

Retrieved by: Hybrid RRF followed by BGE reranking

> word embedding model). The pre-processing step of the tensorflow_embedding pipeline uses a simple whitespace tokenizer for token extraction. The tokens are used for the feature encoding step that is based on Scikit-learn's CountVectorizer. It returns a bag of words histogram with words being the tokens (1-grams).
> 
> Text Classification. The spacy_sklearn pipeline relies on Scikit-learn for text classification using a support vector classifier (SVC). The model confidences are used for ranking all answer candidates; the top-10 results are returned.
> 
> Text classification for tensorflow_embedding is done using TensorFlow with an implementation of the StarSpace algorithm BIBREF24 . This component learns (and later applies) one embedding model for user queries and one for the answer id. It minimizes the distance between embeddings of QA training samples. The distances between a query and all answer ids are used for ranking.

#### Relevance 291

Label: 

## Question 0033

Paper: MetaLDA: a Topic Model that Efficiently Incorporates Meta information

> Which data augmentation techniques do they use?

### Common Retrieved Chunks

#### Passage 292

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this paper, we have presented a topic modelling framework named MetaLDA that can efficiently incorporate document and word meta information. This gains a significant improvement over others in terms of perplexity and topic quality. With two data augmentation techniques, MetaLDA enjoys full local conjugacy, allowing efficient Gibbs sampling, demonstrated by superiority in the per-iteration running time. Furthermore, without losing generality, MetaLDA can work with both regular texts and short texts. The improvement of MetaLDA over other models that also use meta information is more remarkable, particularly when the word-occurrence information is insufficient. As MetaLDA takes a particular approach for incorporating meta information on topic models, it is possible to apply the same approach to other Bayesian probabilistic models, where Dirichlet priors are used. Moreover, it would be interesting to extend our method to use real-valued meta information directly, which is the subject of future work.

#### Relevance 292

Label: 

#### Passage 293

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Unlike most existing methods, our way of incorporating the meta information facilitates the derivation of an efficient Gibbs sampling algorithm. With two data augmentation techniques (i.e., the introduction of auxiliary variables), MetaLDA admits the local conjugacy and a close-form Gibbs sampling algorithm can be derived. Note that MetaLDA incorporates the meta information on the Dirichlet priors, so we can still use LDA's collapsed Gibbs sampling algorithm for the topic assignment INLINEFORM0 . Moreover, Step UID12 and UID9 show that one only needs to consider the non-zero entries of INLINEFORM1 and INLINEFORM2 in computing the full conditionals, which further reduces the inference complexity.
> 
> Similar to LDA, the complete model likelihood (i.e., joint distribution) of MetaLDA is: +rCl+x* k=1K v=1V k,vnk,v d=1D k=1K d,kmd,k where INLINEFORM0 , INLINEFORM1 , and INLINEFORM2 is the indicator function.

#### Relevance 293

Label: 

#### Passage 295

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> labels are binary and INLINEFORM0 is involved in computing INLINEFORM1 iff INLINEFORM2 . Extracting all the terms related to INLINEFORM3 in Eq. ( SECREF17 ), we get the marginal posterior of INLINEFORM4 : +rCl+x* e- l,k d=1:fd,l=1D 1qd d,kl,k l,k d=1D fd,l td,k where INLINEFORM5 is the value of INLINEFORM6 with INLINEFORM7 removed when INLINEFORM8 . With the data augmentation techniques, the posterior is transformed into a form that is conjugate to the gamma prior of INLINEFORM9 . Therefore, it is straightforward to yield the following sampling strategy for INLINEFORM10 : +rCl+x* l,k Ga( ', 1/”)
> 
> ' = 0 + d=1: fd,l = 1D td,k
> 
> ” = 1/0 - d=1:fd,l=1D d,kl,k qd
> 
> We can compute and cache the value of INLINEFORM0 first. After INLINEFORM1 is sampled, INLINEFORM2 can be updated by: +rCl+x* d,k d,k 'l,kl,k 1 d D : fd,l = 1 where INLINEFORM3 is the newly-sampled value of INLINEFORM4 .
> 
> To sample/compute Eqs. ( SECREF17 )-( SECREF17 ), one only iterates over the documents where label INLINEFORM0 is active (i.e., INLINEFORM1 ). Thus, the sampling for all INLINEFORM2 takes INLINEFORM3 where INLINEFORM4 is the average number of documents where a label is active (i.e., the column-wise sparsity of INLINEFORM5 ). It is usually that INLINEFORM6 because if a label exists in nearly all the documents, it provides little discriminative information. This demonstrates how the sparsity of document meta information is leveraged. Moreover, sampling all the tables INLINEFORM7 takes INLINEFORM8 ( INLINEFORM9 is the total number of words in INLINEFORM10 ) which can be accelerated with the window sampling technique explained above.

#### Relevance 295

Label: 

#### Passage 296

Retrieved by: BM25, Hybrid RRF

> words so that similar words are close to each other in the embedding space. It seems reasonable to expect that these word embedding will improve topic modelling BIBREF4 , BIBREF5 .
> 
> Conventional topic models can suffer from a large performance degradation over short texts (e.g., tweets and news headlines) because of insufficient word co-occurrence information. In such cases, meta information of documents and words can play an important role in analysing short texts by compensating the lost information in word co-occurrences. At the document level, for example, tweets are usually associated with hashtags, users, locations, and timestamps, which can be used to alleviate the data sparsity problem. At the word level, word semantic similarity and embeddings obtained or trained on large external corpus (e.g., Google News or Wikipedia) have been proven useful in learning meaningful topics from short texts BIBREF6 , BIBREF7 .
> 
> The benefit of using document and word meta information separately is shown in several models such as BIBREF8 , BIBREF9 , BIBREF5 . However, in existing models this is usually not efficient enough due to non-conjugacy and/or complex model structures. Moreover, only one kind of meta information (either at document level or at word level) is used in most existing models. In this paper, we propose MetaLDA, a topic model that can effectively and efficiently leverage arbitrary document and word meta information encoded in binary form. Specifically, the labels of a document in MetaLDA are incorporated in the prior of the per-document topic distributions. If two documents have similar labels, their topic distributions should be generated with similar Dirichlet priors. Analogously, at the word level, the features of a word are incorporated in the prior of the per-topic word distributions, which encourages words with similar features to have similar weights across topics. Therefore, both document and word meta information, if and when they are available, can be flexibly and simultaneously incorporated using MetaLDA. MetaLDA has the following key properties:
> 
> We conduct extensive experiments with several real datasets including regular and short texts in various domains. The experimental results demonstrate that MetaLDA achieves improved performance in terms of perplexity, topic coherence, and running time.

#### Relevance 296

Label: 

#### Passage 297

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> In this section, we evaluate the proposed MetaLDA against several recent advances that also incorporate meta information on 6 real datasets including both regular and short texts. The goal of the experimental work is to evaluate the effectiveness and efficiency of MetaLDA's incorporation of document and word meta information both separately and jointly compared with other methods. We report the performance in terms of perplexity, topic coherence, and running time per iteration.

#### Relevance 297

Label: 

#### Passage 298

Retrieved by: Dense, Hybrid RRF

> that models usually gained improved perplexity, if INLINEFORM0 is sampled/optimised, in line with BIBREF23 .
> 
> On the AN dataset, there is no statistically significant difference between MetaLDA and DMR. On NYT, a similar trend is observed: the improvement in the models with the document labels over LDA is obvious but not in the models with the word features. Given the number of the document labels (194 of AN and 545 of NYT), it is possible that the document labels already offer enough information and the word embeddings have little contribution in the two datasets.
> 
> To test the hypothesis that the incorporation of meta information in MetaLDA can significantly improve the modelling accuracy in the cases where the corpus is sparse, we varied the proportion of documents used in training from 20% to 80% and used the remaining for testing. It is natural that when the proportion is small, the number of unseen words in testing documents will be large. Instead of simply excluding the unseen words in the previous experiments, here we compute the perplexity with unseen words for LDA, DMR, WF-LDA and the proposed MetaLDA. For perplexity calculation, INLINEFORM0 for each topic INLINEFORM1 and each token INLINEFORM2 in the test documents is needed. If INLINEFORM3 occurs in the training documents, INLINEFORM4 can be directly obtained. While if INLINEFORM5 is unseen, INLINEFORM6 can be estimated by the prior: INLINEFORM7 . For LDA and DMR which do not use word features, INLINEFORM8 ; For WF-LDA and MetaLDA which are with word features, INLINEFORM9 is computed with the features of the unseen token. Following Step UID9 , for MetaLDA, INLINEFORM10 .
> 
> Figure FIGREF51 shows the perplexity scores on Reuters, 20NG, TMN and WS with 200, 200, 100 and 50 topics respectively. MetaLDA outperformed the other models significantly with a lower proportion of training documents and relatively higher proportion of unseen words. The gap between MetaLDA and the other three models increases while the training proportion decreases. It indicates that the meta information helps MetaLDA to achieve better modelling accuracy on predicting unseen words.

#### Relevance 298

Label: 

### BM25

#### Passage 294

Retrieved by: BM25

> With the rapid growth of the internet, huge amounts of text data are generated in social networks, online shopping and news websites, etc. These data create demand for powerful and efficient text analysis techniques. Probabilistic topic models such as Latent Dirichlet Allocation (LDA) BIBREF0 are popular approaches for this task, by discovering latent topics from text collections. Many conventional topic models discover topics purely based on the word-occurrences, ignoring the meta information (a.k.a., side information) associated with the content. In contrast, when we humans read text it is natural to leverage meta information to improve our comprehension, which includes categories, authors, timestamps, the semantic meanings of the words, etc. Therefore, topic models capable of using meta information should yield improved modelling accuracy and topic quality.
> 
> In practice, various kinds of meta information are available at the document level and the word level in many corpora. At the document level, labels of documents can be used to guide topic learning so that more meaningful topics can be discovered. Moreover, it is highly likely that documents with common labels discuss similar topics, which could further result in similar topic distributions. For example, if we use authors as labels for scientific papers, the topics of the papers published by the same researcher can be closely related.
> 
> At the word level, different semantic/syntactic features are also accessible. For example, there are features regarding word relationships, such as synonyms obtained from WordNet BIBREF1 , word co-occurrence patterns obtained from a large corpus, and linked concepts from knowledge graphs. It is preferable that words having similar meaning but different morphological forms, like “dog” and “puppy”, are assigned to the same topic, even if they barely co-occur in the modelled corpus. Recently, word embeddings generated by GloVe BIBREF2 and word2vec BIBREF3 , have attracted a lot of attention in natural language processing and related fields. It has been shown that the word embeddings can capture both the semantic and syntactic features of words so that similar words are close to each other in the embedding space. It seems reasonable to expect that these word embedding will improve topic modelling BIBREF4 , BIBREF5 .
> 
> Conventional topic models can suffer from a large performance

#### Relevance 294

Label: 

### Dense

#### Passage 299

Retrieved by: Dense

> We evaluate the performance of the following models:
> 
> MetaLDA and its variants: the proposed model and its variants. Here we use MetaLDA to indicate the model considering both document labels and word features. Several variants of MetaLDA with document labels and word features separately were also studied, which are shown in Table TABREF32 . These variants differ in the method of estimating INLINEFORM0 and INLINEFORM1 . All the models listed in Table TABREF32 were implemented on top of Mallet. The hyper-parameters INLINEFORM2 and INLINEFORM3 were set to INLINEFORM4 .
> 
> LDA BIBREF0 : the baseline model. The Mallet implementation of SparseLDA BIBREF30 is used.
> 
> LLDA, Labelled LDA BIBREF11 and PLLDA, Partially Labelled LDA BIBREF9 : two models that make use of multiple document labels. The original implementation is used.
> 
> DMR, LDA with Dirichlet Multinomial Regression BIBREF8 : a model that can use multiple document labels. The Mallet implementation of DMR based on SparseLDA was used. Following Mallet, we set the mean of INLINEFORM0 to 0.0 and set the variances of INLINEFORM1 for the default label and the document labels to 100.0 and 1.0 respectively.
> 
> WF-LDA, Word Feature LDA BIBREF16 : a model with word features. We implemented it on top of Mallet and used the default settings in Mallet for the optimisation.
> 
> LF-LDA, Latent Feature LDA BIBREF5 : a model that incorporates word embeddings. The original implementation was used. Following the paper, we used 1500 and 500 MCMC iterations for initialisation and sampling respectively and set INLINEFORM0 to 0.6, and used the original 50-dimensional GloVe word embeddings as word features.
> 
> GPU-DMM, Generalized Pólya Urn DMM BIBREF7 : a model that incorporates word semantic similarity. The original implementation was used. The word similarity was generated from the distances of the word embeddings. Following the paper, we set the hyper-parameters INLINEFORM0 and INLINEFORM1 to 0.1 and 0.7 respectively, and the symmetric document Dirichlet prior to INLINEFORM2 .
> 
> PTM, Pseudo document based Topic Model BIBREF18 : a model for short text analysis. The original implementation was used. Following the paper, we set the number of pseudo documents to 1000 and INLINEFORM0 to 0.1.
> 
> All the models, except where noted, the symmetric parameters of the document and the topic Dirichlet

#### Relevance 299

Label: 

### Hybrid RRF

#### Passage 300

Retrieved by: Hybrid RRF

> and 500 topics are reported. (3) The number of latent topics in LLDA must equal to the number of document labels. (4) For PLLDA, we varied the number of topics per label from 5 to 50 (2 and 5 topics on NYT). The number of topics in PPLDA is the product of the numbers of labels and topics per label.
> 
> The results show that MetaLDA outperformed all the competitors in terms of perplexity on nearly all the datasets, showing the benefit of using both document and word meta information. Specifically, we have the following remarks:
> 
> By looking at the models using only the document-level meta information, we can see the significant improvement of these models over LDA, which indicates that document labels can play an important role in guiding topic modelling. Although the performance of the two variants of MetaLDA with document labels and DMR is comparable, our models runs much faster than DMR, which will be studied later in Section SECREF67 .
> 
> It is interesting that PLLDA with 50 topics for each label has better perplexity than MetaLDA with 200 topics in the 20NG dataset. With the 20 unique labels, the actual number of topics in PLLDA is 1000. However, if 10 topics for each label in PLLDA are used, which is equivalent to 200 topics in MetaLDA, PLLDA is outperformed by MetaLDA significantly.
> 
> At the word level, MetaLDA-def-wf performed the best among the models with word features only. Moreover, our model has obvious advantage in running speed (see Table TABREF66 ). Furthermore, comparing MetaLDA-def-wf with MetaLDA-def-def and MetaLDA-0.1-wf with LDA, we can see using the word features indeed improved perplexity.
> 
> The scores show that the improvement gained by MetaLDA over LDA on the short text datasets is larger than that on the regular text datasets. This is as expected because meta information serves as complementary information in MetaLDA and can have more significant impact when the data is sparser.
> 
> It can be observed that models usually gained improved perplexity, if INLINEFORM0 is sampled/optimised, in line with BIBREF23 .
> 
> On the AN dataset, there is no statistically significant difference between MetaLDA and DMR. On NYT, a similar trend is observed: the improvement in the

#### Relevance 300

Label: 

### Hybrid RRF followed by BGE reranking

#### Passage 301

Retrieved by: Hybrid RRF followed by BGE reranking

> Perplexity is a measure that is widely used BIBREF23 to evaluate the modelling accuracy of topic models. The lower the score, the higher the modelling accuracy. To compute perplexity, we randomly selected some documents in a dataset as the training set and the remaining as the test set. We first trained a topic model on the training set to get the word distributions of each topic INLINEFORM0 ( INLINEFORM1 ). Each test document INLINEFORM2 was split into two halves containing every first and every second words respectively. We then fixed the topics and trained the models on the first half to get the topic proportions ( INLINEFORM3 ) of test document INLINEFORM4 and compute perplexity for predicting the second half. In regard to MetaLDA, we fixed the matrices INLINEFORM5 and INLINEFORM6 output from the training procedure. On the first half of test document INLINEFORM7 , we computed the Dirichlet prior INLINEFORM8 with INLINEFORM9 and the labels INLINEFORM10 of test document INLINEFORM11 (See Step UID12 ), and then point-estimated INLINEFORM12 . We ran all the models 5 times with different random number seeds and report the average scores and the standard deviations.
> 
> In testing, we may encounter words that never occur in the training documents (a.k.a., unseen words or out-of-vocabulary words). There are two strategies for handling unseen words for calculating perplexity on test documents: ignoring them or keeping them in computing the perplexity. Here we investigate both strategies:
> 
> In this experiment, the perplexity is computed only on the words that appear in the training vocabulary. Here we used 80% documents in each dataset as the training set and the remaining 20% as the test set.
> 
> Tables TABREF48 and TABREF49 show: the average perplexity scores with standard deviations for all the models. Note that: (1) The scores on AN with 150 and 200 topics are not reported due to overfitting observed in all the compared models. (2) Given the size of NYT, the scores of 200 and 500 topics are reported. (3) The number of latent topics in LLDA must equal to the number of document labels. (4) For PLLDA, we varied the number of topics per label from 5 to 50 (2 and 5 topics

#### Relevance 301

Label: 

## Question 0034

Paper: Abstractive Summarization with Combination of Pre-trained Sequence-to-Sequence and Saliency Models

> What is the previous state-of-the-art?

### Common Retrieved Chunks

#### Passage 302

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> blackWe used BART$_{\mathrm {LARGE}}$ BIBREF1, which is one of the state-of-the-art models, as the pre-trained seq-to-seq model and RoBERTa$_\mathrm {BASE}$ BIBREF11 as the initial model of the extractor. In the extractor of CIT, stop words and duplicate tokens are ignored for the XSum dataset.
> 
> We used fairseq for the implementation of the seq-to-seq model. For fine-tuning of BART$_\mathrm {LARGE}$ and the combination models, we used the same parameters as the official code. For fine-tuning of RoBERTa$_\mathrm {BASE}$, we used Transformers. We set the learning rate to 0.00005 and the batch size to 32.

#### Relevance 302

Label: 

#### Passage 303

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Pre-trained language models such as BERT BIBREF0 have significantly improved the accuracy of various language processing tasks. However, we cannot apply BERT to language generation tasks as is because its model structure is not suitable for language generation. Several pre-trained seq-to-seq models for language generation BIBREF1, BIBREF2 based on an encoder-decoder Transformer model, which is a standard model for language generation, have recently been proposed. These models have achieved blackstate-of-the-art results in various language generation tasks, including abstractive summarization.
> 
> However, when generating a summary, it is essential to correctly predict which part of the source text should be included in the summary. Some previous studies without pre-training have examined combining extractive summarization with abstractive summarization BIBREF3, BIBREF4. Although pre-trained seq-to-seq models have achieved higher accuracy compared to previous models, it is not clear whether modeling “Which part of the source text is important?” can be learned through pre-training.
> 
> blackThe purpose of this study is to clarify the blackeffectiveness of combining saliency models that identify the important part of the source text with a pre-trained seq-to-seq model in the abstractive summarization task. Our main contributions are as follows:
> 
> We investigated nine combinations of pre-trained seq-to-seq and token-level saliency models, where the saliency models share the parameters with the encoder of the seq-to-seq model or extract important tokens independently of the encoder.
> 
> We proposed a new combination model, the conditional summarization model with important tokens (CIT), in which a token sequence extracted by a saliency model is explicitly given to a seq-to-seq model as an additional input text.
> 
> We evaluated the combination models on the CNN/DM BIBREF5 and XSum BIBREF6 datasets. Our CIT model outperformed a simple fine-tuned model in terms of ROUGE scores on both datasets.

#### Relevance 303

Label: 

#### Passage 305

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> BIBREF18 used BERT for their sentence-level extractive summarization model. BIBREF19 proposed a new pre-trained model that considers document-level information for sentence-level extractive summarization. Several researchers have published pre-trained encoder-decoder models very recently BIBREF20, BIBREF1, BIBREF2. BIBREF20 pre-trained a Transformer-based pointer-generator model. BIBREF1 pre-trained a standard Transformer-based encoder-decoder model using large unlabeled data and achieved state-of-the-art results. BIBREF8 and BIBREF16 extended the BERT structure to handle seq-to-seq tasks.
> 
> All the studies above focused on how to learn a universal pre-trained model; they did not consider the combination of pre-trained and saliency models for an abstractive summarization model.

#### Relevance 305

Label: 

#### Passage 307

Retrieved by: Dense, Hybrid RRF

> Rouge scores of the combined models on the XSum dataset are shown in Table TABREF52. The CIT model performed the best, although its improvement was smaller than on the CNN/DM dataset. Moreover, the accuracy of the MT, SE + MT, and SEG models decreased on the XSum dataset. These results were very different from those on the CNN/DM dataset.
> 
> One reason for the difference can be traced to the quality of the pseudo saliency labels. CNN/DM is a highly extractive dataset, so it is relatively easy to create token alignments for generating pseudo saliency labels, while in contrast, a summary in XSum is highly abstractive and short, which makes it difficult to create pseudo labels with high quality by simple token alignment. To improve the accuracy of summarization in this dataset, we have to improve the quality of the pseudo saliency labels and the accuracy of the saliency model.

#### Relevance 307

Label: 

### BM25

#### Passage 304

Retrieved by: BM25

> The decoder consists of $M$ layer decoder blocks. The inputs of the decoder are the output of the encoder $H_e^M$ and the output of the previous step of the decoder $\lbrace y_1,...,y_{t-1} \rbrace $. The output through the $M$ layer Transformer decoder blocks is defined as
> 
> In each step $t$, the $h_{dt}^M$ is projected to blackthe vocabulary space and the decoder outputs the highest probability token as the next token. The Transformer decoder block consists of a self-attention module, a context-attention module, and a two-layer feed-forward network.

#### Relevance 304

Label: 

#### Passage 306

Retrieved by: BM25

> The shared encoder blackshares the parameters of black$\rm Encoder_{sal}$ and the encoder of the seq-to-seq model. This model is jointly trained with the seq-to-seq model and the saliency score is used to bias the representations of the seq-to-seq model.

#### Relevance 306

Label: 

### Dense

#### Passage 308

Retrieved by: Dense

> Several studies have proposed the combination of a token-level saliency model and a seq-to-seq model, blackwhich is not pre-trained, and reported its effectiveness BIBREF3, BIBREF10. We also use a simple token-level saliency model blackas a basic model in this study.

#### Relevance 308

Label: 

#### Passage 309

Retrieved by: Dense

> Our study focuses on the combinations of saliency models and the pre-trained seq-to-seq model. However, there are several studies that focus more on the pre-training strategy. We compared the CIT model with those models. Their ROUGE scores are shown in Tables TABREF57 and TABREF58. From Table TABREF57, we can see that our model outperformed the recent pre-trained models on the CNN/DM dataset. Even though PEGASUS$_\mathrm {HugeNews}$ was pre-trained on the largest corpus comprised of news-like articles, the accuracy of abstractive summarization was not improved much. Our model improved the accuracy without any additional pre-training. This result indicates that it is more effective to combine saliency models with the seq-to-seq model for generating a highly extractive summary.
> 
> On the other hand, on the XSum dataset, PEGASUS$_\mathrm {HugeNews}$ improved the ROUGE scores and achieved the best results. In the XSum dataset, summaries often include the expressions that are not written in the source text. Therefore, increasing the pre-training data and learning more patterns were effective. However, by improving the quality of the pseudo saliency labels, we should be able to improve the accuracy of the CIT model.

#### Relevance 309

Label: 

#### Passage 310

Retrieved by: Dense

> We analyzed the quality of the tokens extracted by the extractor in CIT. The results are summarized in Table TABREF55. On the CNN/DM dataset, the ROUGE-1 and ROUGE-2 scores of our extractor (Top-$K$ tokens) were higher than other models, while the ROUGE-L score was lower than the other sentence-based extraction method. This is because that our token-level extractor finds the important tokens whereas the seq-to-seq model learns how to generate a fluent summary incorporating these important tokens.
> 
> On the other hand, the extractive result on the XSum dataset was lower. For highly abstractive datasets, there is little overlap between the tokens. We need to consider how to make the high-quality pseudo saliency labels and how to evaluate the similarity of these two sequences.

#### Relevance 310

Label: 

### Hybrid RRF

#### Passage 311

Retrieved by: Hybrid RRF

> This model uses the saliency score to weight the shared encoder output. Specifically, the final output $h_{el}^M$ of the shared encoder is weighted as
> 
> Then, we replace the input of the decoder $h_{el}^M$ with $\tilde{h}_{el}^{M}$. Although BIBREF10 used BiGRU, we use Transformer for fair comparison. The loss function of this model is $L_\mathrm {abs} = L_\mathrm {sum}.$

#### Relevance 311

Label: 

### Hybrid RRF followed by BGE reranking

#### Passage 312

Retrieved by: Hybrid RRF followed by BGE reranking

> In this study, we use two types of saliency model for combination: a shared encoder and an extractor. Each model structure is based on the basic saliency model. We describe them below.

#### Relevance 312

Label: 

#### Passage 313

Retrieved by: Hybrid RRF followed by BGE reranking

> This model has the same structure as the SA. The loss function of this model is $L_\mathrm {abs} = L_\mathrm {sum} + L_\mathrm {sal}$.

#### Relevance 313

Label: 

## Question 0035

Paper: Affect-LM: A Neural Language Model for Customizable Affective Text Generation

> How to extract affect attributes from the sentence?

### Common Retrieved Chunks

#### Passage 314

Retrieved by: BM25, Dense, Hybrid RRF

> Affect-LM can be used to generate sentences conditioned on the input affect category, the affect strength $\beta $ , and the context words. For our experiments, we have chosen the following affect categories - positive emotion, anger, sad, anxiety, and negative emotion (which is a superclass of anger, sad and anxiety). As described in Section "Conclusions and Future Work" , the affect strength $\beta $ defines the degree of dominance of the affect-dependent energy term on the word prediction in the language model, consequently after model training we can change $\beta $ to control the degree of how “emotionally colored" a generated utterance is, varying from $\beta =0$ (neutral; baseline model) to $\beta =\infty $ (the generated sentences only consist of emotionally colored words, with no grammatical structure). When Affect-LM is used for generation, the affect categories could be either (1) inferred from the context using LIWC (this occurs when we provide sentence beginnings which are emotionally colored themselves), or (2) set to an input emotion descriptor $\mathbf {e}$ (this is obtained by setting $\mathbf {e}$ to a binary vector encoding the desired emotion and works even for neutral sentence beginnings). Given an initial starting set of $M$ words $w_1,w_2,...,w_M$ to complete, affect strength $\beta $ , and the number of words $\beta $0 to generate each $\beta $1 -th generated word is obtained by sampling from $\beta $2 for $\beta $3 .

#### Relevance 314

Label: 

#### Passage 316

Retrieved by: BM25, Hybrid RRF

> We assess Affect-LM's ability to generate emotionally colored text of varying degrees without severely deteriorating grammatical correctness, by conducting an extensive perception study on Amazon's Mechanical Turk (MTurk) platform. The MTurk platform has been successfully used in the past for a wide range of perception experiments and has been shown to be an excellent resource to collect human ratings for large studies BIBREF27 . Specifically, we generated more than 200 sentences for four sentence beginnings (namely the three sentence beginnings listed in Table 2 as well as an end of sentence token indicating that the model should generate a new sentence) in five affect categories happy(positive emotion), angry, sad, anxiety, and negative emotion. The Affect-LM model trained on the Fisher corpus was used for sentence generation. Each sentence was evaluated by two human raters that have a minimum approval rating of 98% and are located in the United States. The human raters were instructed that the sentences should be considered to be taken from a conversational rather than a written context: repetitions and pause fillers (e.g., um, uh) are common and no punctuation is provided. The human raters evaluated each sentence on a seven-point Likert scale for the five affect categories, overall affective valence as well as the sentence's grammatical correctness and were paid 0.05USD per sentence. We measured inter-rater agreement using Krippendorff’s $\alpha $ and observed considerable agreement between raters across all categories (e.g., for valence $\alpha = 0.510$ and grammatical correctness $\alpha = 0.505$ ).
> 
> For each target emotion (i.e., intended emotion of generated sentences) we conducted an initial MANOVA, with human ratings of affect categories the DVs (dependent variables) and the affect strength parameter $\beta $ the IV (independent variable). We then conducted follow-up univariate ANOVAs to identify which DV changes significantly with $\beta $ . In total we conducted 5 MANOVAs and 30 follow-up ANOVAs, which required us to update the significance level to p $<$ 0.001 following a Bonferroni correction.

#### Relevance 316

Label: 

#### Passage 317

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> In Section "Affect-LM for Emotional Text Generation" we have described the process of sampling text from the model conditioned on input affective information (research question Q1). Table 2 shows three sentences generated by the model for input sentence beginnings I feel so ..., Why did you ... and I told him to ... for each of five affect categories - happy(positive emotion), angry, sad anxiety, and neutral(no emotion). They have been selected from a pool of 20 generated sentences for each category and sentence beginning.

#### Relevance 317

Label: 

#### Passage 318

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Our proposed model learns a generative model of the next word $w_t$ conditioned not only on the previous words $w_1,w_2,...,w_{t-1}$ but also on the affect category $\mathbf {e_{t-1}}$ which is additional information about emotional content. During model training, the affect category is inferred from the context data itself. Thus we define a suitable feature extractor which can utilize an affective lexicon to infer emotion in the context. For our experiments, we have utilized the Linguistic Inquiry and Word Count (LIWC) text analysis program for feature extraction through keyword spotting. Introduced by BIBREF11 pennebaker2001linguistic, LIWC is based on a dictionary, where each word is assigned to a predefined LIWC category. The categories are chosen based on their association with social, affective, and cognitive processes. For example, the dictionary word worry is assigned to LIWC category anxiety. In our work, we have utilized all word categories of LIWC corresponding to affective processes: positive emotion, angry, sad, anxious, and negative emotion. Thus the descriptor $\mathbf {e_{t-1}}$ has five features with each feature denoting presence or absence of a specific emotion, which is obtained by binary thresholding of the features extracted from LIWC. For example, the affective representation of the sentence i will fight in the war is $\mathbf {e_{t-1}}=$ {“sad":0, “angry":1, “anxiety":0, “negative emotion":1, “positive emotion":0}.

#### Relevance 318

Label: 

#### Passage 319

Retrieved by: Dense, Hybrid RRF

> on conversational speech corpora, common in language modeling for speech recognition applications BIBREF10 . Figure 1 provides an overview of our Affect-LM and its ability to generate emotionally colored conversational text in a number of affect categories with varying affect strengths. While these parameters can be manually tuned to generate conversational text, the affect category can also be automatically inferred from preceding context words. Specifically for model training, the affect category is derived from features generated using keyword spotting from a dictionary of emotional words, such as the LIWC (Linguistic Inquiry and Word Count) tool BIBREF11 . Our primary research questions in this paper are:
> 
> Q1:Can Affect-LM be used to generate affective sentences for a target emotion with varying degrees of affect strength through a customizable model parameter?
> 
> Q2:Are these generated sentences rated as emotionally expressive as well as grammatically correct in an extensive crowd-sourced perception experiment?
> 
> Q3:Does the automatic inference of affect category from the context words improve language modeling performance of the proposed Affect-LM over the baseline as measured by perplexity?
> 
> The remainder of this paper is organized as follows. In Section "Related Work" , we discuss prior work in the fields of neural language modeling, and generation of affective conversational text. In Section "LSTM Language Model" we describe the baseline LSTM model and our proposed Affect-LM model. Section "Experimental Setup" details the experimental setup, and in Section "Results" , we discuss results for customizable emotional text generation, perception studies for each affect category, and perplexity improvements over the baseline model before concluding the paper in Section "Conclusions and Future Work" .

#### Relevance 319

Label: 

#### Passage 320

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Affect is a term that subsumes emotion and longer term constructs such as mood and personality and refers to the experience of feeling or emotion BIBREF0 . BIBREF1 picard1997affective provides a detailed discussion of the importance of affect analysis in human communication and interaction. Within this context the analysis of human affect from text is an important topic in natural language understanding, examples of which include sentiment analysis from Twitter BIBREF2 , affect analysis from poetry BIBREF3 and studies of correlation between function words and social/psychological processes BIBREF4 . People exchange verbal messages which not only contain syntactic information, but also information conveying their mental and emotional states. Examples include the use of emotionally colored words (such as furious and joy) and swear words. The automated processing of affect in human verbal communication is of great importance to understanding spoken language systems, particularly for emerging applications such as dialogue systems and conversational agents.
> 
> Statistical language modeling is an integral component of speech recognition systems, with other applications such as machine translation and information retrieval. There has been a resurgence of research effort in recurrent neural networks for language modeling BIBREF5 , which have yielded performances far superior to baseline language models based on n-gram approaches. However, there has not been much effort in building neural language models of text that leverage affective information. Current literature on deep learning for language understanding focuses mainly on representations based on word semantics BIBREF6 , encoder-decoder models for sentence representations BIBREF7 , language modeling integrated with symbolic knowledge BIBREF8 and neural caption generation BIBREF9 , but to the best of our knowledge there has been no work on augmenting neural language modeling with affective information, or on data-driven approaches to generate emotional text.
> 
> Motivated by these advances in neural language modeling and affective analysis of text, in this paper we propose a model for representation and generation of emotional text, which we call the Affect-LM. Our model is trained on conversational speech corpora, common in language modeling for speech recognition applications BIBREF10 . Figure 1 provides an overview of our Affect-LM and its ability to generate emotionally colored conversational text in a number of affect categories with varying affect

#### Relevance 320

Label: 

#### Passage 321

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> In Equation 7 , Affect-LM learns a weight matrix $\mathbf {V}$ which captures the correlation between the predicted word $w_t$ , and the affect category $\mathbf {e_{t-1}}$ . Thus, each row of the matrix $\mathbf {V_i}$ is an emotionally meaningful embedding of the $i$ -th word in the vocabulary. In Figure 4 , we present a visualization of these embeddings, where each data point is a separate word, and words which appear in the LIWC dictionary are colored based on which affect category they belong to (we have labeled only words in categories positive emotion, negative emotion, anger, sad and anxiety since these categories contain the most frequent words). Words colored grey are those not in the LIWC dictionary. In Figure 4 , we observe that the embeddings contain affective information, where the positive emotion is highly separated from the negative emotions (sad, angry, anxiety) which are clustered together.

#### Relevance 321

Label: 

### BM25

#### Passage 315

Retrieved by: BM25

> Language modeling is an integral component of spoken language systems, and traditionally n-gram approaches have been used BIBREF12 with the shortcoming that they are unable to generalize to word sequences which are not in the training set, but are encountered in unseen data. BIBREF13 bengio2003neural proposed neural language models, which address this shortcoming by generalizing through word representations. BIBREF5 mikolov2010recurrent and BIBREF14 sundermeyer2012lstm extend neural language models to a recurrent architecture, where a target word $w_t$ is predicted from a context of all preceding words $w_1, w_2,..., w_{t-1}$ with an LSTM (Long Short-Term Memory) neural network. There also has been recent effort on building language models conditioned on other modalities or attributes of the data. For example, BIBREF9 Vinyals2015CVPR introduced the neural image caption generator, where representations learnt from an input image by a CNN (Convolutional Neural Network) are fed to an LSTM language model to generate image captions. BIBREF15 kiros2014multimodal used an LBL model (Log-Bilinear language model) for two applications - image retrieval given sentence queries, and image captioning. Lower perplexity was achieved on text conditioned on images rather than language models trained only on text.
> 
> In contrast, previous literature on affective language generation has not focused sufficiently on customizable state-of-the-art neural network techniques to generate emotional text, nor have they quantitatively evaluated their models on multiple emotionally colored corpora. BIBREF16 mahamood2011generating use several NLG (natural language generation) strategies for producing affective medical reports for parents of neonatal infants undergoing healthcare. While they study the difference between affective and non-affective reports, their work is limited only to heuristic based systems and do not include conversational text. BIBREF17 mairesse2007personage developed PERSONAGE, a system for dialogue generation conditioned on extraversion dimensions. They trained regression models on ground truth judge's selections to automatically determine which of the sentences selected by their model exhibit appropriate extroversion attributes. In BIBREF18 keshtkar2011pattern, the authors use heuristics and rule-based approaches for emotional sentence generation. Their generation system is not training on large corpora and they use additional syntactic knowledge of parts of speech to create simple affective sentences. In contrast, our proposed approach builds on state-of-the-art approaches for neural language modeling, utilizes no syntactic prior knowledge, and generates expressive emotional text.

#### Relevance 315

Label: 

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 322

Retrieved by: Hybrid RRF followed by BGE reranking

> In this paper, we have introduced a novel language model Affect-LM for generating affective conversational text conditioned on context words, an affective category and an affective strength parameter. MTurk perception studies show that the model can generate expressive text at varying degrees of emotional strength without affecting grammatical correctness. We also evaluate Affect-LM as a language model and show that it achieves lower perplexity than a baseline LSTM model when the affect category is obtained from the words in the context. For future work, we wish to extend this model by investigating language generation conditioned on other modalities such as facial images and speech, and to applications such as dialogue generation for virtual agents.

#### Relevance 322

Label: 

## Question 0036

Paper: Augmenting End-to-End Dialog Systems with Commonsense Knowledge

> Which commonsense knowledge base are they using?

### Common Retrieved Chunks

#### Passage 323

Retrieved by: BM25, Dense, Hybrid RRF

> Our main approach to integrating commonsense knowledge into the conversational model involves using another LSTM for encoding all assertions $a$ in $A_x$ , as illustrated in Figure 3 . Each $a$ , originally in the form of $<c_1,r,c_2 >$ , is transformed into a sequence of tokens by chunking $c_1$ , $c_2$ , concepts which are potentially multi-word phrases, into $[c_{11},c_{12},c_{13}...]$ and $[c_{21},c_{22},c_{23}...]$ . Thus, $a=[c_{11},c_{12},c_{13}...,r,c_{21},c_{22},c_{23}...]$ .
> 
> We add $R$ to vocabulary $V$ , that is, each $r$ in $R$ will be treated like any regular word in $V$ during encoding. We decide not to use each concept $c$ as a unit for encoding $a$ because $C$ is typically too large ( $>$ 1M). $a$ is encoded as embedding representation $V$0 using another LSTM. Note that this encoding scheme is suitable for any natural utterances containing commonsense knowledge in addition to well-structured assertions. We define the match score of assertion $V$1 and response $V$2 as:
> 
> $$m(a,y) = \vec{a}^{T}W_a\vec{y},$$   (Eq. 16)
> 
> where $W_a \in \mathcal {R}^{D\times D}$ is learned during training. Commonsense assertions $A_x$ associated with a message is usually large ( $>$ 100 in our experiment). We observe that in a lot of cases of open-domain conversation, response $y$ can be seen as triggered by certain perception of message $x$ defined by one or more assertions in $A_x$ , as illustrated in Figure 4 . We can see the difference between message and response pair when commonsense knowledge is used. For example, the word `Insomnia' in the message is mapped to the commonsense assertion `Insomnia, IsA, sleep $\_$ problem'. The appropriate response is then matched to `sleep $\_$ problem' that is `go to bed'. Similarly, the word `Hawaii' in the message is mapped to the commonsense assertion `Hawaii, UsedFor, tourism'. The appropriate response is then matched to `tourism' that is `enjoy vacation'. In this way, new words can be mapped to the commonly used vocabulary and improve response accuracy.
> 
> Our assumption is that $A_x$ is helpful in selecting an appropriate response $y$ . However, usually very few assertions in $A_x$ are related to a particular response $y$ in the open-domain setting. As a result, we define the match score of $A_x$ and $y$ as
> 
> $$m(A_x,y)=\mathop

#### Relevance 323

Label: 

#### Passage 325

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> To the best of our knowledge, there is currently no well-established open-domain response selection benchmark dataset available, although certain Twitter datasets have been used in the response generation setting BIBREF29 , BIBREF30 . We thus evaluate our method against state-of-the-art approaches in the response selection task on Twitter dialogues.
> 
> 1.4M Twitter <message, response $>$ pairs are used for our experiments. They were extracted over a 5-month period, from February through July in 2011. 1M Twitter <message, response $>$ pairs are used for training. With the original response as ground truth, we construct 1M <message, response, label=1 $>$ triples as positive instances. Another 1M negative instances <message, response, label=0 $>$ are constructed by replacing the ground truth response with a random response in the training set.
> 
> For tuning and evaluation, we use 20K <message, response $>$ pairs that constitute the validation set (10K) and test set (10K). They are selected by a criterion that encourages interestingness and relevance: both the message and response have to be at least 3 tokens long and contain at least one non-stopword. For every message, at least one concept has to be found in the commonsense knowledge base. For each instance, we collect another 9 random responses from elsewhere to constitute the response candidates.
> 
> Preprocessing of the dataset includes normalizing hashtags, “@User”, URLs, emoticons. Vocabulary $V$ is built out of the training set with 5 as minimum word frequency, containing 62535 words and an extra $<UNK >$ token representing all unknown words.

#### Relevance 325

Label: 

#### Passage 326

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> Data-driven conversational models generally fall into two categories: retrieval-based methods BIBREF6 , BIBREF7 , BIBREF8 , which select a response from a predefined repository, and generation-based methods BIBREF9 , BIBREF10 , BIBREF11 , which employ an encoder-decoder framework where the message is encoded into a vector representation and, then, fed to the decoder to generate the response. The latter is more natural (as it does not require a response repository) yet suffers from generating dull or vague responses and generally needs a great amount of training data.
> 
> The use of an external memory module in natural language processing (NLP) tasks has received considerable attention recently, such as in question answering BIBREF12 and language modeling BIBREF13 . It has also been employed in dialogue modeling in several limited settings. With memory networks, BIBREF14 used a set of fact triples about movies as long-term memory when modeling reddit dialogues, movie recommendation and factoid question answering. Similarly in a restaurant reservation setting, BIBREF2 provided local restaurant information to the conversational model.
> 
> Researchers have also proposed several methods to incorporate knowledge as external memory into the Seq2Seq framework. BIBREF15 incorporated the topic words of the message obtained from a pre-trained latent Dirichlet allocation (LDA) model into the context vector through a joint attention mechanism. BIBREF1 mined FoodSquare tips to be searched by an input message in the food domain and encoded such tips into the context vector through one-turn hop. The model we propose in this work shares similarities with BIBREF16 , which encoded unstructured textual knowledge with a recurrent neural network (RNN). Our work distinguishes itself from previous research in that we consider a large heterogeneous commonsense knowledge base in an open-domain retrieval-based dialogue setting.

#### Relevance 326

Label: 

#### Passage 327

Retrieved by: BM25, Hybrid RRF

> In this work, we concentrate on integrating commonsense knowledge into retrieval-based conversational models, because they are easier to evaluate BIBREF24 , BIBREF7 and generally take a lot less data to train. We leave the generation-based scenario to future work.
> 
> Message (context) $x$ and response $y$ are a sequence of tokens from vocabulary $V$ . Given $x$ and a set of response candidates $[y_1,y_2,y_3...,y_K]\in Y$ , the model chooses the most appropriate response $\hat{y}$ according to:
> 
> $$\hat{y}=\mathop {\arg \max }_{y\in {Y}}f(x,y),$$   (Eq. 6)
> 
> where $f(x,y)$ is a scoring function measuring the “compatibility” of $x$ and $y$ . The model is trained on $<message, response, label >$ triples with cross entropy loss, where $label$ is binary indicating whether the $<message, response >$ pair comes from real data or is randomly combined.

#### Relevance 327

Label: 

#### Passage 328

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Several commonsense knowledge bases have been constructed during the past decade, such as ConceptNet BIBREF17 and SenticNet BIBREF18 . The aim of commonsense knowledge representation and reasoning is to give a foundation of real-world knowledge to a variety of AI applications, e.g., sentiment analysis BIBREF19 , handwriting recognition BIBREF20 , e-health BIBREF21 , aspect extraction BIBREF22 , and many more. Typically, a commonsense knowledge base can be seen as a semantic network where concepts are nodes in the graph and relations are edges (Figure 2 ). Each $<concept1, relation, concept2 >$ triple is termed an assertion.
> 
> Based on the Open Mind Common Sense project BIBREF23 , ConceptNet not only contains objective facts such as “Paris is the capital of France” that are constantly true, but also captures informal relations between common concepts that are part of everyday knowledge such as “A dog is a pet”. This feature of ConceptNet is desirable in our experiments, because the ability to recognize the informal relations between common concepts is necessary in the open-domain conversation setting we are considering in this paper.

#### Relevance 328

Label: 

#### Passage 329

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this paper, we assume that a commonsense knowledge base is composed of assertions $A$ about concepts $C$ . Each assertion $a \in A$ takes the form of a triple $<c_1,r,c_2 >$ , where $r \in R$ is a relation between $c_1$ and $c_2$ , such as IsA, CapableOf, etc. $c_1,c_2$ are concepts in $C$ . The relation set $R$ is typically much smaller than $C$0 . $C$1 can either be a single word (e.g., “dog” and “book”) or a multi-word expression (e.g., “take_a_stand” and “go_shopping”). We build a dictionary $C$2 out of $C$3 where every concept $C$4 is a key and a list of all assertions in $C$5 concerning $C$6 , i.e., $C$7 or $C$8 , is the value. Our goal is to retrieve commonsense knowledge about every concept covered in the message.
> 
> We define $A_x$ as the set of commonsense assertions concerned with message $x$ . To recover concepts in message $x$ , we use simple $n$ -gram matching ( $n\le N$ ). Every $n$ -gram in $c$ is considered a potential concept. If the $n$ -gram is a key in $x$0 , the corresponding value, i.e., all assertions in $x$1 concerning the concept, is added to $x$2 (Figure 4 ).

#### Relevance 329

Label: 

#### Passage 331

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In our experiment, ConceptNet is used as the commonsense knowledge base. Preprocessing of this knowledge base involves removing assertions containing non-English characters or any word outside vocabulary $V$ . 1.4M concepts remain. 0.8M concepts are unigrams, 0.43M are bi-grams and the other 0.17M are tri-grams or more. Each concept is associated with an average of 4.3 assertions. More than half of the concepts are associated with only one assertion.
> 
> An average of 2.8 concepts can be found in ConceptNet for each message in our Twitter Dialogue Dataset, yielding an average of 150 commonsense assertions (the size of $A_x$ ). Unsurprisingly, common concepts with more assertions associated are favored in actual human conversations.
> 
> It is worth noting that ConceptNet is also noisy due to uncertainties in the constructing process, where 15.5% of all assertions are considered “false” or “vague” by human evaluators BIBREF17 . Our max-pooling strategy used in Tri-LSTM encoder and supervised word embeddings is partly designed to alleviate this weakness.

#### Relevance 331

Label: 

### BM25

#### Passage 324

Retrieved by: BM25

> We follow BIBREF2 , BIBREF14 and use supervised word embeddings as a baseline. Word embeddings are most well-known in the context of unsupervised training on raw text as in BIBREF27 , yet they can also be used to score message-response pairs. The embedding vectors are trained directly for this goal. In this setting, the “compatibility” function of $x$ and $y$ is defined as:
> 
> $$f(x,y)=\vec{x}^T\vec{y}$$   (Eq. 21)
> 
> In this setting, $\vec{x},\vec{y}$ are bag-of-words embeddings. With retrieved commonsense assertions $A_x$ , we embed each $a\in {A_x}$ to bag-of-words representation $\vec{a}$ and have:
> 
> $$f(x,y)=\vec{x}^T\vec{y}+\mathop {\max }_{a\in {A_x}} \ \ \vec{a}^T\vec{y}.$$   (Eq. 22)
> 
> This linear model differs from Tri-LSTM encoder in that it represents an utterance with its bag-of-words embedding instead of RNNs.
> 
> Memory networks BIBREF13 , BIBREF28 are a class of models that perform language understanding by incorporating a memory component. They perform attention over memory to retrieve all relevant information that may help with the task. In our dialogue modeling setting, we use $A_x$ as the memory component. Our implementation of memory networks, similar to BIBREF2 , BIBREF14 , differs from supervised word embeddings described above in only one aspect: how to treat multiple entries in memory. In memory networks, output memory representation $\vec{o}=\sum _{i}p_i\vec{a}_i$ , where $\vec{a}_i$ is the bag-of-words embedding of $a_i\in {A_x}$ and $p_i$ is the attention signal over memory $A_x$ calculated by $p_i=softmax(\vec{x}^T\vec{a_i})$ . The “compatibility” function of $x$ and $y$ is defined as:
> 
> $$f(x,y)=(\vec{x}+\vec{o})^T\vec{y}=\vec{x}^T\vec{y}+(\sum _{i}p_i\vec{a}_i)^T\vec{y}$$   (Eq. 24)
> 
> In contrast to supervised word embeddings described above, attention over memory is determined by message $x$ . This mechanism was originally designed to retrieve information from memory that is relevant to the context, which in our setting is already achieved during commonsense knowledge retrieval. As speculated, the attention over multiple memory entries is better determined by response $y$ in our setting. We empirically prove this point below.

#### Relevance 324

Label: 

### Dense

#### Passage 330

Retrieved by: Dense

> In recent years, data-driven approaches to building conversation models have been made possible by the proliferation of social media conversation data and the increase of computing power. By relying on a large number of message-response pairs, the Seq2Seq framework BIBREF0 attempts to produce an appropriate response based solely on the message itself, without any memory module.
> 
> In human-to-human conversations, however, people respond to each other's utterances in a meaningful way not only by paying attention to the latest utterance of the conversational partner itself, but also by recalling relevant information about the concepts covered in the dialogue and integrating it into their responses. Such information may contain personal experience, recent events, commonsense knowledge and more (Figure 1 ). As a result, it is speculated that a conversational model with a “memory look-up” module can mimic human conversations more closely BIBREF1 , BIBREF2 . In open-domain human-computer conversation, where the model is expected to respond to human utterances in an interesting and engaging way, commonsense knowledge has to be integrated into the model effectively.
> 
> In the context of artificial intelligence (AI), commonsense knowledge is the set of background information that an individual is intended to know or assume and the ability to use it when appropriate BIBREF3 , BIBREF4 , BIBREF5 . Due to the vastness of such kind of knowledge, we speculate that this goal is better suited by employing an external memory module containing commonsense knowledge rather than forcing the system to encode it in model parameters as in traditional methods.
> 
> In this paper, we investigate how to improve end-to-end dialogue systems by augmenting them with commonsense knowledge, integrated in the form of external memory. The remainder of this paper is as follows: next section proposes related work in the context of conversational models and commonsense knowledge; following, a section describes the proposed model in detail; later, a section illustrates experimental results; finally, the last section proposes concluding remarks and future work.

#### Relevance 330

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0037

Paper: Identifying Nuances in Fake News vs. Satire: Using Semantic and Linguistic Cues

> What is the baseline?

### Common Retrieved Chunks

#### Passage 332

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Previous work addressed the challenge of identifying fake news BIBREF3, BIBREF4, or identifying satire BIBREF5, BIBREF6, BIBREF7, in isolation, compared to real news stories.
> 
> The most relevant work to ours is that of Golbeck et al. BIBREF1. They introduced a dataset of fake news and satirical articles, which we also employ in this work. The dataset includes the full text of 283 fake news stories and 203 satirical stories, that were verified manually, and such that each fake news article is paired with a rebutting article from a reliable source. Albeit relatively small, this data carries two desirable properties. First, the labeling is based on the content and not the source, and the stories spread across a diverse set of sources. Second, both fake news and satire articles focus on American politics and were posted between January 2016 and October 2017, minimizing the possibility that the topic of the article will influence the classification.
> 
> In their work, Golbeck et al. studied whether there are differences in the language of fake news and satirical articles on the same topic that could be utilized with a word-based classification approach. A model using the Naive Bayes Multinomial algorithm is proposed in their paper which serves as the baseline in our experiments.

#### Relevance 332

Label: 

#### Passage 333

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We evaluate the performance of our method based on the dataset of fake news and satire articles and using the F1 score with a ten-fold cross-validation as in the baseline work BIBREF1.
> 
> First, we consider the semantic representation with BERT. Our experiments included multiple pre-trained models of BERT with different sizes and cases sensitivity, among which the large uncased model, bert_uncased_L-24_H-1024_A-16, gave the best results. We use the recommended settings of hyper-parameters in BERT's Github repository and use the fake news and satire data to fine-tune the model. Furthermore, we tested separate models based on the headline and body text of a story, and in combination. Results are shown in Table TABREF6. The models based on the headline and text body give a similar F1 score. However, while the headline model performs poorly on precision, perhaps due to the short text, the model based on the text body performs poorly on recall. The model based on the full text of headline and body gives the best performance.
> 
> To investigate the predictive power of the linguistic cues, we use those Coh-Metrix indices that were significant in both the logistic and step-wise backward elimination regression models, and train a classifier on fake news and satire articles. We tested a few classification models, including Naive Bayes, Support Vector Machine (SVM), logistic regression, and gradient boosting - among which the SVM classifier gave the best results.
> 
> Table TABREF7 provides a summary of the results. We compare the results of our methods of the pre-trained BERT, using both the headline and text body, and the Coh-Mertix approach, to the language-based baseline with Multinomial Naive Bayes from BIBREF1. Both the semantic cues with BERT and the linguistic cues with Coh-Metrix significantly outperform the baseline on the F1 score. The two-tailed paired t-test with a 0.05 significance level was used for testing statistical significance of performance differences. The best result is given by the BERT model. Overall, these results provide an answer to research question RQ1 regarding the existence of semantic and linguistic difference between fake news and satire.

#### Relevance 333

Label: 

#### Passage 334

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We addressed the challenge of identifying nuances between fake news and satire. Inspired by the humor and social message aspects of satire articles, we tested two classification approaches based on a state-of-the-art contextual language model, and linguistic features of textual coherence. Evaluation of our methods pointed to the existence of semantic and linguistic differences between fake news and satire. In particular, both methods achieved a significantly better performance than the baseline language-based method. Lastly, we studied the feature importance of our linguistic-based method to help shed light on the nuances between fake news and satire. For instance, we observed that satire articles are more sophisticated, or less easy to read, than fake news articles.
> 
> Overall, our contributions, with the improved classification accuracy and towards the understanding of nuances between fake news and satire, carry great implications with regard to the delicate balance of fighting misinformation while protecting free speech.
> 
> For future work, we plan to study additional linguistic cues, and specifically humor related features, such as absurdity and incongruity, which were shown to be good indicators of satire in previous work. Another interesting line of research would be to investigate techniques of identifying whether a story carries a political or social message, for example, by comparing it with timely news information.

#### Relevance 334

Label: 

#### Passage 335

Retrieved by: BM25, Dense, Hybrid RRF

> The efforts by social media platforms to reduce the exposure of users to misinformation have resulted, on several occasions, in flagging legitimate satire stories. To avoid penalizing publishers of satire, which is a protected form of speech, the platforms have begun to add more nuance to their flagging systems. Facebook, for instance, added an option to mark content items as “Satire”, if “the content is posted by a page or domain that is a known satire publication, or a reasonable person would understand the content to be irony or humor with a social message” BIBREF0. This notion of humor and social message is also echoed in the definition of satire by Oxford dictionary as “the use of humour, irony, exaggeration, or ridicule to expose and criticize people's stupidity or vices, particularly in the context of contemporary politics and other topical issues”.
> 
> The distinction between fake news and satire carries implications with regard to the exposure of content on social media platforms. While fake news stories are algorithmically suppressed in the news feed, the satire label does not decrease the reach of such posts. This also has an effect on the experience of users and publishers. For users, incorrectly classifying satire as fake news may deprive them from desirable entertainment content, while identifying a fake news story as legitimate satire may expose them to misinformation. For publishers, the distribution of a story has an impact on their ability to monetize content.
> 
> Moreover, in response to these efforts to demote misinformation, fake news purveyors have begun to masquerade as legitimate satire sites, for instance, carrying small badges at the footer of each page denoting the content as satire BIBREF1. The disclaimers are usually small such that the stories are still being spread as though they were real news BIBREF2.
> 
> This gives rise to the challenge of classifying fake news versus satire based on the content of a story. While previous work BIBREF1 have shown that satire and fake news can be distinguished with a word-based classification approach, our work is focused on the semantic and linguistic properties of the content. Inspired by the distinctive aspects of satire with regard to humor and social message, our hypothesis is

#### Relevance 335

Label: 

#### Passage 337

Retrieved by: Dense, Hybrid RRF

> Inspired by previous work on satire detection, and specifically Rubin et al. BIBREF7 who studied the humor and absurdity aspects of satire by comparing the final sentence of a story to the first one, and to the rest of the story - we hypothesize that metrics of text coherence will be useful to capture similar aspects of semantic relatedness between different sentences of a story.
> 
> Consequently, we use the set of text coherence metrics as implemented by Coh-Metrix BIBREF12. Coh-Metrix is a tool for producing linguistic and discourse representations of a text. As a result of applying the Coh-Metrix to the input documents, we have 108 indices related to text statistics, such as the number of words and sentences; referential cohesion, which refers to overlap in content words between sentences; various text readability formulas; different types of connective words and more. To account for multicollinearity among the different features, we first run a Principal Component Analysis (PCA) on the set of Coh-Metrix indices. Note that we do not apply dimensionality reduction, such that the features still correspond to the Coh-Metrix indices and are thus explainable. Then, we use the PCA scores as independent variables in a logistic regression model with the fake and satire labels as our dependent variable. Significant features of the logistic regression model are shown in Table TABREF3 with the respective significance levels. We also run a step-wise backward elimination regression. Those components that are also significant in the step-wise model appear in bold.

#### Relevance 337

Label: 

### BM25

#### Passage 336

Retrieved by: BM25

> To study the semantic nuances between fake news and satire, we use BERT BIBREF8, which stands for Bidirectional Encoder Representations from Transformers, and represents a state-of-the-art contextual language model. BERT is a method for pre-training language representations, meaning that it is pre-trained on a large text corpus and then used for downstream NLP tasks. Word2Vec BIBREF9 showed that we can use vectors to properly represent words in a way that captures semantic or meaning-related relationships. While Word2Vec is a context-free model that generates a single word-embedding for each word in the vocabulary, BERT generates a representation of each word that is based on the other words in the sentence. It was built upon recent work in pre-training contextual representations, such as ELMo BIBREF10 and ULMFit BIBREF11, and is deeply bidirectional, representing each word using both its left and right context. We use the pre-trained models of BERT and fine-tune it on the dataset of fake news and satire articles using Adam optimizer with 3 types of decay and 0.01 decay rate. Our BERT-based binary classifier is created by adding a single new layer in BERT's neural network architecture that will be trained to fine-tune BERT to our task of classifying fake news and satire articles.

#### Relevance 336

Label: 

### Dense

#### Passage 338

Retrieved by: Dense

> With regard to research question RQ2 on the understanding of semantic and linguistic nuances between fake news and satire - a key advantage of studying the coherence metrics is explainability. While the pre-trained model of BERT gives the best result, it is not easily interpretable. The coherence metrics allow us to study the differences between fake news and satire in a straightforward manner.
> 
> Observing the significant features, in bold in Table TABREF3, we see a combination of surface level related features, such as sentence length and average word frequency, as well as semantic features including LSA (Latent Semantic Analysis) overlaps between verbs and between adjacent sentences. Semantic features which are associated with the gist representation of content are particularly interesting to see among the predictors since based on Fuzzy-trace theory BIBREF13, a well-known theory of decision making under risk, gist representation of content drives individual's decision to spread misinformation online. Also among the significant features, we observe the causal connectives, that are proven to be important in text comprehension, and two indices related to the text easability and readability, both suggesting that satire articles are more sophisticated, or less easy to read, than fake news articles.

#### Relevance 338

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 339

Retrieved by: Hybrid RRF followed by BGE reranking

> In the following subsections, we investigate the semantic and linguistic differences of satire and fake news articles.

#### Relevance 339

Label: 

#### Passage 340

Retrieved by: Hybrid RRF followed by BGE reranking

> In the following sub sections, we evaluate our classification model and share insights on the nuances between fake news and satire, while addressing our two research questions.

#### Relevance 340

Label: 

## Question 0038

Paper: Lexical Bias In Essay Level Prediction

> what model is used?

### Common Retrieved Chunks

#### Passage 341

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this work I presented the feature extraction, feature engineering and model evaluation steps I followed while developing balikasg for CAp 2018 that was ranked first among 14 other systems. I evaluated the efficiency of the different feature groups and found that readbility and complexity scores as well as topic models to be effective predictors. Further, I evaluated the the effectiveness of different classification algorithms and found that Gradient Boosted Trees outperform the rest of the models in this problem.
> 
> While in terms of accuracy the system performed excellent achieving 98.2% in the test data, the question raised is whether there are any types of biases in the process. For instance, topic distributions learned with LDA were valuable features. One, however, needs to deeply investigate whether this is due to the expressiveness and modeling power of LDA or an artifact of the dataset used. In the latter case, given that the candidates are asked to write an essay given a subject BIBREF0 that depends on their level, the hypothesis that needs be studied is whether LDA was just a clever way to model this information leak in the given data or not. I believe that further analysis and validation can answer this question if the topics of the essays are released so that validation splits can be done on the basis of these topics.

#### Relevance 341

Label: 

#### Passage 342

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In order to approach the language-level prediction task as a supervised classification problem, I frame it as an ordinal classification problem. In particular, given a written essay INLINEFORM0 from a candidate, the goal is to associate the essay with the level INLINEFORM1 of English according to the Common European Framework of Reference for languages (CEFR) system. Under CEFR there are six language levels INLINEFORM2 , such that INLINEFORM3 . In this notation, INLINEFORM4 is the beginner level while INLINEFORM5 is the most advanced level. Notice that the levels of INLINEFORM6 are ordered, thus defining an ordered classification problem. In this sense, care must be taken both during the phase of model selection and during the phase of evaluation. In the latter, predicting a class far from the true should incur a higher penalty. In other words, given a INLINEFORM7 essay, predicting INLINEFORM8 is worse than predicting INLINEFORM9 , and this difference must be captured by the evaluation metrics.
> 
> In order to capture this explicit ordering of INLINEFORM0 , the organisers proposed a cost measure that uses the confusion matrix of the prediction and prior knowledge in order to evaluate the performance of the system. In particular, the meaures uses writes as: DISPLAYFORM0
> 
> where INLINEFORM0 is a cost matrix that uses prior knowledge to calculate the misclassification errors and INLINEFORM1 is the number of observations of class INLINEFORM2 classified with category INLINEFORM3 . The cost matrix INLINEFORM4 is given in Table TABREF3 . Notice that, as expected, moving away from the diagonal (correct classification) the misclassification costs are higher. The biggest error (44) occurs when a INLINEFORM5 essay is classified as INLINEFORM6 . On the contrary, the classification error is lower (6) when the opposite happens and an INLINEFORM7 essay is classified as INLINEFORM8 . Since INLINEFORM9 is not symmetric and the costs of the lower diagonal are higher, the penalties for misclassification are worse when essays of upper languages levels (e.g., INLINEFORM10 ) are classified as essays of lower levels.

#### Relevance 342

Label: 

#### Passage 343

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Automatically predicting the level of English of non-native speakers from their written text is an interesting text mining task. Systems that perform well in the task can be useful components for online, second-language learning platforms as well as for organisations that tutor students for this purpose. In this paper I present the system balikasg that achieved the state-of-the-art performance in the CAp 2018 data science challenge among 14 systems. In order to achieve the best performance in the challenge, I decided to use a variety of features that describe an essay's readability and syntactic complexity as well as its content. For the prediction step, I found Gradient Boosted Trees, whose efficiency is proven in several data science challenges, to be the most efficient across a variety of classifiers.
> 
> The rest of the paper is organized as follows: in Section 2 I frame the problem of language level as an ordinal classification problem and describe the available data. Section 3 presents the feature extaction and engineering techniques used. Section 4 describes the machine learning algorithms for prediction as well as the achieved results. Finally, Section 5 concludes with discussion and avenues for future research.

#### Relevance 343

Label: 

#### Passage 344

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> As the class distribution in the training data is not balanced, I have used stratified cross-validation for validation purposes and for hyper-parameter selection. As a classification1 algorithm, I have used gradient boosted trees trained with gradient-based one-side sampling as implemented in the Light Gradient Boosting Machine toolkit released by Microsoft.. The depth of the trees was set to 3, the learning rate to 0.06 and the number of trees to 4,000. Also, to combat the class imbalance in the training labels I assigned class weights at each class so that errors in the frequent classes incur less penalties than error in the infrequent.

#### Relevance 344

Label: 

#### Passage 345

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this section I present the extracted features partitioned in six groups and detail each of them separately.

#### Relevance 345

Label: 

### BM25

None

### Dense

#### Passage 346

Retrieved by: Dense

> I would like to thank the organisers of the challenge and NVidia for sponsoring the prize of the challenge. The views expressed in this paper belong solely to the author, and not necessarily to the author's employer.

#### Relevance 346

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0039

Paper: Speech Model Pre-training for End-to-End Spoken Language Understanding

> How was the dataset collected?

### Common Retrieved Chunks

#### Passage 347

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The data was collected using crowdsourcing. Each speaker was recorded saying each wording for each intent twice. The phrases to record were presented in a random order. Participants consented to data being released and provided demographic information about themselves. The demographic information about these anonymized speakers (age range, gender, speaking ability, etc.) is included along with the dataset.
> 
> The data was validated by a separate set of crowdsourcers. All audios deemed by the crowdsourcers to be unintelligible or contain the wrong phrase were removed. The total number of speakers, utterances, and hours of audio remaining is shown in Table TABREF12 .

#### Relevance 347

Label: 

#### Passage 349

Retrieved by: BM25, Hybrid RRF

> To simulate a smaller dataset, we randomly selected 10% of the training set, and used this instead of the entire training set. Fig. shows the validation accuracy (on the entire validation set, not a subset) over time. A similar trend is observed as for the entire dataset: unfreezing the word layers works best. The gap in final test accuracy between the randomly initialized model and the pre-trained models increases (Table TABREF28 , “10%” column); the final test accuracy for the pre-trained models drops only slightly, further highlighting the advantage of our proposed method.

#### Relevance 349

Label: 

#### Passage 350

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The dataset is composed of 16 kHz single-channel .wav audio files. Each audio file contains a recording of a single command that one might use for a smart home or virtual assistant, like “put on the music” or “turn up the heat in the kitchen”.
> 
> Each audio is labeled with three slots: action, object, and location. A slot takes on one of multiple values: for instance, the “location” slot can take on the values “none”, “kitchen”, “bedroom”, or “washroom”. We refer to the combination of slot values as the intent of the utterance. The dataset has 31 unique intents in total. We do not distinguish between domain, intent, and slot prediction, as is sometimes done in SLU BIBREF25 .
> 
> The dataset can be used as a multi-label classification task, where the goal is to predict the action, object, and location labels. Since the slots are not actually independent of each other, a more careful approach would model the relationship between slots, e.g. using an autoregressive model, as in BIBREF7 . We use the simpler multi-label classification approach in this paper, so as to avoid the issues sometimes encountered training autoregressive models and instead focus on questions related to generalization using a simpler model. Alternately, the 31 distinct intents can be “flattened” and used as 31 distinct labels for a single-label classification task.
> 
> For each intent, there are multiple possible wordings: for example, the intent {action: "activate", object: "lights", location: "none"} can be expressed as “turn on the lights”, “switch the lights on”, “lights on”, etc.. These phrases were decided upon before data collection by asking employees at Fluent.ai, including both native and non-native English speakers, for various ways in which they might express a particular intent. There are 248 different phrases in total.

#### Relevance 350

Label: 

#### Passage 352

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The utterances are randomly divided into train, valid, and test splits in such a way that no speaker appears in more than one split. Each split contains all possible wordings for each intent, though our code has the option to include data for only certain wordings for different sets, to test the model's ability to recognize wordings not heard during training. The dataset has a .csv file for each split that lists the speaker ID, file path, transcription, and slots for all the .wav files in that split.

#### Relevance 352

Label: 

#### Passage 354

Retrieved by: Dense, Hybrid RRF

> Here we review some related public datasets and show the gap that Fluent Speech Commands fills.
> 
> The Google Speech Commands dataset BIBREF26 (to which the name “Fluent Speech Commands” is an homage) is a free dataset of 30 single-word spoken commands (“yes”, “no”, “stop”, “go”, etc.). This dataset is suitable for keyword spotting experiments, but not for SLU.
> 
> ATIS is an SLU dataset consisting of utterances related to travel planning. This dataset can only be obtained expensively from the Linguistic Data Consortium.
> 
> The Snips NLU Benchmark BIBREF2 has a rich set of virtual assistant commands, but contains only text, with no audio, and hence is not suitable for end-to-end SLU experiments.
> 
> The Grabo, Domotica, and Patcor datasets are three related datasets of spoken commands for robot control and card games developed by KU Leuven and used in BIBREF8 . These datasets are free, but have only a small number of speakers and phrases.
> 
> In contrast to these datasets, Fluent Speech Commands is simultaneously audio-based, reasonably large, and free, and contains several multiple-word commands corresponding to each of the intents.

#### Relevance 354

Label: 

### BM25

#### Passage 348

Retrieved by: BM25

> What happens if new wordings appear in the test data that never appear in the training data? This is an important question, since it is generally impractical to try to imagine every possible wording for a particular intent while gathering training data.
> 
> To test this, we trained models on three specific phrases, “turn on the lights”, “turn off the lights”, and “switch on the lights” (273 utterances total), and tested on those same phrases, as well as a new phrase: “switch off the lights”. If the model incorrectly infers that utterances that contain “switch” always correspond to turning on the lights, it will incorrectly guess that “switch off the lights” corresponds to turning on the lights; if the model infers that the presence of the word “off” corresponds to turning off the lights, it will generalize to the new phrase. The randomly initialized model was unable to fit this tiny training set, even with a very low learning rate and no regularization. The pre-trained models were able to generalize to the new wording (with 97% accuracy on the validation set, which contains more examples of the new phrase than of the training phrases).
> 
> However, there are many situations in which our model does not correctly generalize. For example, if the model is trained only with examples containing “bedroom” and “washroom”, but then tested on an example containing “bathroom”, it will guess the intent corresponding to “bedroom” because “bedroom” sounds more similar to “bathroom” than to “washroom”, even though “washroom” is the correct meaning. In text-based NLU, this scenario can be handled using word embeddings, which represent words in such a way that words with similar meanings have similar vector representations BIBREF1 , BIBREF38 . It may be possible to teach the pre-trained part of the model to output “embedding-like” word representations so that the intent module can recognize the meaning of phrases with synonyms.

#### Relevance 348

Label: 

#### Passage 351

Retrieved by: BM25

> Three key papers describing end-to-end SLU were written by Qian et al. BIBREF4 , Serdyuk et al. BIBREF5 , and Chen et al. BIBREF6 . Serdyuk et al. in BIBREF5 use no pre-training whatsoever. Qian et al. in BIBREF4 use an auto-encoder to initialize the SLU model. Chen et al. BIBREF6 pre-train the first stage of an SLU model to recognize graphemes; the softmax outputs of the first stage are then fed to a classifier second stage. The model proposed in this paper is similar to theirs, but removes the restriction of the softmax bottleneck and uses alternative training targets, as we will describe later.
> 
> More recently, Haghani et al. in BIBREF7 compare four types of sequence-to-sequence models for SLU, including a direct model (end-to-end with no pre-training) and a multi-task model (uses a shared encoder whose output is ingested by a separate ASR decoder and SLU decoder). The model proposed here is somewhat similar to their multi-task model, although we do not use or require the ASR targets during SLU training.
> 
> The work listed above deals with very high resource SLU—in BIBREF7 , for instance, the Google Home BIBREF23 dataset consists of 24 million labeled utterances. In contrast, Renkens et al. in BIBREF8 consider the problem of end-to-end SLU with limited training data, and find that capsule networks BIBREF24 , compared to conventional neural network models, are more easily capable of learning end-to-end SLU from scratch. However, they do not consider the effect of pre-training on other speech data.
> 
> This previous work has all been conducted on datasets that are closed-source or too small to test hypotheses about the amount of data required to generalize well. The lack of a good open-source dataset for end-to-end SLU experiments makes it difficult for most people to perform high-quality, reproducible research on this topic. We therefore created a new SLU dataset, the “Fluent Speech Commands” dataset, which Fluent.ai releases along with this paper.

#### Relevance 351

Label: 

### Dense

#### Passage 353

Retrieved by: Dense

> Here we report results for three experiments on Fluent Speech Commands: using the full dataset, using a subset of the dataset, and using a subset of wordings.

#### Relevance 353

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 355

Retrieved by: Hybrid RRF followed by BGE reranking

> The model proposed in this paper, shown in Fig. FIGREF17 , is a deep neural network consisting of a stack of modules, where the first modules are pre-trained to predict phonemes and words. The word and phoneme classifiers are discarded, and the entire model is then trained end-to-end on the supervised SLU task. In what follows, we justify these design decisions and give more details about the model hyperparameters.

#### Relevance 355

Label: 

#### Passage 356

Retrieved by: Hybrid RRF followed by BGE reranking

> The first module takes as input the audio signal INLINEFORM0 and outputs INLINEFORM1 , a sequence of hidden representations that are pre-trained to predict phonemes. The phoneme-level logits are computed using a linear classifier: DISPLAYFORM0
> 
> The phoneme module is implemented using a SincNet layer BIBREF36 , BIBREF37 , which processes the raw input waveform, followed by multiple convolutional layers and recurrent layers with pooling and dropout. More detailed hyperparameters can be found in our code.

#### Relevance 356

Label: 

## Question 0040

Paper: Hierarchical Transformers for Long Document Classification

> On top of BERT does the RNN layer work better or the transformer layer?

### Common Retrieved Chunks

#### Passage 357

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> that these models introduce a hierarchy of representations (segment-wise and document-wise), we refer to them as Hierarchical Transformers. To the best of our knowledge, no attempt has been done before to use the Transformer architecture for classification of such long sequences.
> 
> Our novel contributions are:
> 
> Two extensions - RoBERT and ToBERT - to the BERT model, which enable its application in classification of long texts by performing segmentation and using another layer on top of the segment representations.
> 
> State-of-the-art results on the Fisher topic classification task.
> 
> Significant improvement on the CSAT prediction task over the MS-CNN model.

#### Relevance 357

Label: 

#### Passage 358

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Because our work builds heavily upon BERT, we provide a brief summary of its features. BERT is built upon the Transformer architecture BIBREF0, which uses self-attention, feed-forward layers, residual connections and layer normalization as the main building blocks. It has two pre-training objectives:
> 
> Masked language modelling - some of the words in a sentence are being masked and the model has to predict them based on the context (note the difference from the typical autoregressive language model training objective);
> 
> Next sentence prediction - given two input sequences, decide whether the second one is the next sentence or not.
> 
> BERT has been shown to beat the state-of-the-art performance on 11 tasks with no modifications to the model architecture, besides adding a task-specific output layer BIBREF1. We follow same procedure suggested in BIBREF1 for our tasks. Fig. FIGREF8 shows the BERT model for classification. We obtain two kinds of representation from BERT: pooled output from last transformer block, denoted by H, and posterior probabilities, denoted by P. There are two variants of BERT - BERT-Base and BERT-Large. In this work we are using BERT-Base for faster training and experimentation, however, our methods are applicable to BERT-Large as well. BERT-Base and BERT-Large are different in model parameters such as number of transformer blocks, number of self-attention heads. Total number of parameters in BERT-Base are 110M and 340M in BERT-Large.
> 
> BERT suffers from major limitations in terms of handling long sequences. Firstly, the self-attention layer has a quadratic complexity $O(n^2)$ in terms of the sequence length $n$ BIBREF0. Secondly, BERT uses a learned positional embeddings scheme BIBREF1, which means that it won't likely be able to generalize to positions beyond those seen in the training data.
> 
> To investigate the effect of fine-tuning BERT on task performance, we use either the pre-trained BERT weights, or the weights from a BERT fine-tuned on the task-specific dataset on a segment-level (i.e. we preserve the original label but fine-tune on each segment separately instead of on the whole text sequence). We compare these results to using the fine-tuned segment-level BERT predictions directly as inputs to the next layer.

#### Relevance 358

Label: 

#### Passage 359

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Given that Transformers' edge over recurrent networks is their ability to effectively capture long distance relationships between words in a sequence BIBREF0, we experiment with replacing the LSTM recurrent layer in favor of a small Transformer model (2 layers of transformer building block containing self-attention, fully connected, etc.). To investigate if preserving the information about the input sequence order is important, we also build a variant of ToBERT which learns positional embeddings at the segment-level representations (but is limited to sequences of length seen during the training).
> 
> ToBERT's computational complexity $O(\frac{n^2}{k^2})$ is asymptotically inferior to RoBERT, as the top-level Transformer model again suffers from quadratic complexity in the number of segments. However, in practice this number is much smaller than the input sequence length (${\frac{n}{k}} << n$), so we haven't observed performance or memory issues with our datasets.

#### Relevance 359

Label: 

#### Passage 360

Retrieved by: BM25, Hybrid RRF

> In this paper, we presented two methods for long documents using BERT model: RoBERT and ToBERT. We evaluated our experiments on two classification tasks - customer satisfaction prediction and topic identification - using 3 datasets: CSAT, 20newsgroups and Fisher. We observed that ToBERT outperforms RoBERT on pre-trained BERT features and fine-tuned BERT features for all our tasks. Also, we noticed that fine-tuned BERT performs better than pre-trained BERT. We have shown that both RoBERT and ToBERT improved the simple baselines of taking an average (or the most frequent) of segment-wise predictions for long documents to obtain final prediction. Position embeddings did not significantly affect our models performance, but slightly improved the accuracy on the CSAT task. We obtained the best results on Fisher dataset and good improvements for CSAT task compared to the CNN baseline. It is interesting to note that the longer the average input in a given task, the bigger improvement we observe w.r.t. the baseline for that task. Our results confirm that both RoBERT and ToBERT can be used for long sequences with competitive performance and quick fine-tuning procedure. For future work, we shall focus on training models on long documents directly (i.e. in an end-to-end manner).

#### Relevance 360

Label: 

#### Passage 361

Retrieved by: BM25, Dense, Hybrid RRF

> Given that BERT is limited to a particular input length, we split the input sequence into segments of a fixed size with overlap. For each of these segments, we obtain H or P from BERT model. We then stack these segment-level representations into a sequence, which serves as input to a small (100-dimensional) LSTM layer. Its output serves as a document embedding. Finally, we use two fully connected layers with ReLU (30-dimensional) and softmax (the same dimensionality as the number of classes) activations to obtain the final predictions.
> 
> With this approach, we overcome BERT's computational complexity, reducing it to $O(n/k * k^2) = O(nk)$ for RoBERT, with $k$ denoting the segment size (the LSTM component has negligible linear complexity $O(k)$). The positional embeddings are also no longer an issue.

#### Relevance 361

Label: 

#### Passage 362

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> Bidirectional Encoder Representations from Transformers (BERT) is a novel Transformer BIBREF0 model, which recently achieved state-of-the-art performance in several language understanding tasks, such as question answering, natural language inference, semantic similarity, sentiment analysis, and others BIBREF1. While well-suited to dealing with relatively short sequences, Transformers suffer from a major issue that hinders their applicability in classification of long sequences, i.e. they are able to consume only a limited context of symbols as their input BIBREF2.
> 
> There are several natural language (NLP) processing tasks that involve such long sequences. Of particular interest are topic identification of spoken conversations BIBREF3, BIBREF4, BIBREF5 and call center customer satisfaction prediction BIBREF6, BIBREF7, BIBREF8, BIBREF9. Call center conversations, while usually quite short and to the point, often involve agents trying to solve very complex issues that the customers experience, resulting in some calls taking even an hour or more. For speech analytics purposes, these calls are typically transcribed using an automatic speech recognition (ASR) system, and processed in textual representations further down the NLP pipeline. These transcripts sometimes exceed the length of 5000 words. Furthermore, temporal information might play an important role in tasks like CSAT. For example, a customer may be angry at the beginning of the call, but after her issue is resolved, she would be very satisfied with the way it was handled. Therefore, simple bag of words models, or any model that does not include temporal dependencies between the inputs, may not be well-suited to handle this category of tasks. This motivates us to employ model such as BERT in this task.
> 
> In this paper, we propose a method that builds upon BERT's architecture. We split the input text sequence into shorter segments in order to obtain a representation for each of them using BERT. Then, we use either a recurrent LSTM BIBREF10 network, or another Transformer, to perform the actual classification. We call these techniques Recurrence over BERT (RoBERT) and Transformer over BERT (ToBERT). Given that these models introduce a hierarchy of representations (segment-wise and document-wise), we refer to them as Hierarchical Transformers. To the best of our knowledge, no attempt has been done before to use the Transformer architecture for classification of such long

#### Relevance 362

Label: 

### BM25

None

### Dense

#### Passage 363

Retrieved by: Dense

> Table TABREF25 presents results using pre-trained BERT features. We extracted features from the pooled output of final transformer block as these were shown to be working well for most of the tasks BIBREF1. The features extracted from a pre-trained BERT model without any fine-tuning lead to a sub-par performance. However, We also notice that ToBERT model exploited the pre-trained BERT features better than RoBERT. It also converged faster than RoBERT. Table TABREF26 shows results using features extracted after fine-tuning BERT model with our datasets. Significant improvements can be observed compared to using pre-trained BERT features. Also, it can be noticed that ToBERT outperforms RoBERT on Fisher and 20newsgroups dataset by 13.63% and 0.81% respectively. On CSAT, ToBERT performs slightly worse than RoBERT but it is not statistically significant as this dataset is small.
> 
> Table TABREF27 presents results using fine-tuned BERT predictions instead of the pooled output from final transformer block. For each document, having obtained segment-wise predictions we can obtain final prediction for the whole document in three ways:
> 
> Compute the average of all segment-wise predictions and find the most probable class;
> 
> Find the most frequently predicted class;
> 
> Train a classification model.
> 
> It can be observed from Table TABREF27 that a simple averaging operation or taking most frequent predicted class works competitively for CSAT and 20newsgroups but not for the Fisher dataset. We believe the improvements from using RoBERT or ToBERT, compared to simple averaging or most frequent operations, are proportional to the fraction of long documents in the dataset. CSAT and 20newsgroups have (on average) significantly shorter documents than Fisher, as seen in Fig. FIGREF21. Also, significant improvements for Fisher could be because of less confident predictions from BERT model as this dataset has 40 classes. Fig. FIGREF31 presents the comparison of average voting and ToBERT for various document length ranges for Fisher dataset. We used fine-tuned BERT segment-level predictions (P) for this analysis. It can be observed that ToBERT outperforms average voting in every interval. To the best of our knowledge, this is a state-of-the-art result reported on the Fisher dataset.
> 
> Table TABREF32 presents the effect of position embeddings on the model performance. It can be observed that position embeddings did not significantly

#### Relevance 363

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 364

Retrieved by: Hybrid RRF followed by BGE reranking

> Several dimensionality reduction algorithms such as RBM, autoencoders, subspace multinomial models (SMM) are used to obtain a low dimensional representation of documents from a simple BOW representation and then classify it using a simple linear classifiers BIBREF11, BIBREF12, BIBREF13, BIBREF4. In BIBREF14 hierarchical attention networks are used for document classification. They evaluate their model on several datasets with average number of words around 150. Character-level CNN are explored in BIBREF15 but it is prohibitive for very long documents. In BIBREF16, dataset collected from arXiv papers is used for classification. For classification, they sample random blocks of words and use them together for classification instead of using full document which may work well as arXiv papers are usually coherent and well written on a well defined topic. Their method may not work well on spoken conversations as random block of words usually do not represent topic of full conversation.
> 
> Several researchers addressed the problem of predicting customer satisfaction BIBREF6, BIBREF7, BIBREF8, BIBREF9. In most of these works, logistic regression, SVM, CNN are applied on different kinds of representations.
> 
> In BIBREF17, authors use BERT for document classification but the average document length is less than BERT maximum length 512. TransformerXL BIBREF2 is an extension to the Transformer architecture that allows it to better deal with long inputs for the language modelling task. It relies on the auto-regressive property of the model, which is not the case in our tasks.

#### Relevance 364

Label: 
