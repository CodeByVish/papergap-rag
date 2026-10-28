# Passage relevance annotation

Annotator: 

Judge whether the passage provides information that helps answer the question, including useful partial evidence. Topic overlap alone is not sufficient. Judge only the supplied question and passage.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Do not change record numbers, questions or passages. Work independently without consulting another annotator or reference answers.

## Record 0201

Paper: Concurrent Parsing of Constituency and Dependency

### Question

> How is dependency parsing empirically verified?

### Passage

> Constituent and dependency are two typical syntactic structure representation forms as shown in Figure FIGREF1, which have been well studied from both linguistic and computational perspective BIBREF0, BIBREF1. In earlier time, linguists and NLP researchers discussed how to encode lexical dependencies in phrase structures, like Tree-adjoining grammar (TAG) BIBREF2 and head-driven phrase structure grammar (HPSG) BIBREF3.
> 
> Typical dependency treebanks are usually converted from constituent treebanks, though they may be independently annotated as well for the same languages. Meanwhile, constituent parsing can be accurately converted to dependencies (SD) representation by grammatical rules or machine learning methods BIBREF4, BIBREF5. Such mutual convertibility shows a close relation between constituent and dependency representation for the same sentence. Thus, it is a natural idea to study the relationship between constituent and dependency structures, and the joint learning of constituent and dependency parsing BIBREF6, BIBREF7, BIBREF8, BIBREF9, BIBREF10, BIBREF11, BIBREF12, BIBREF13, BIBREF14.
> 
> For further exploit both strengths of the two representation forms for even better parsing, in this work, we propose a new model that is capable of synchronously parsing constituent and dependency.
> 
> Multitask learning (MTL) is a natural solution in neural models for multiple inputs and multiple outputs, which is adopted in this work to decode constituent and dependency in a single model. BIBREF15 indicates that when tasks are sufficiently similar, especially with syntactic nature, MTL would be useful. In contrast to previous work on deep MTL BIBREF16, BIBREF17, our model focuses on more related tasks and benefits from the strong inherent relation. At last, our model is evaluated on two benchmark treebanks for both constituent and dependency parsing. The empirical results show that our parser reaches new state-of-the-art for all parsing tasks.

### Relevance

Label: 

## Record 0202

Paper: Concurrent Parsing of Constituency and Dependency

### Question

> How is dependency parsing empirically verified?

### Passage

> In our model, token representation $x_i$ is composed by character, word and part-of-speech (POS) embeddings. For character-level representation, we explore two types of encoders, CharCNNs BIBREF19, BIBREF20 and CharLSTM BIBREF18, as both types have been verified their effectiveness. For word-level representation, we concatenate randomly initialized and pre-trained word embeddings. We consider two ways to compose the final token representation, summing and concatenation, $x_i$=$x_{char}$+$x_{word}$+$x_{POS}$, $x_i$=[$x_{char}$;$x_{word}$;$x_{POS}$].

### Relevance

Label: 

## Record 0203

Paper: Concurrent Parsing of Constituency and Dependency

### Question

> How is dependency parsing empirically verified?

### Passage

> All experiments in this subsection are running from token representation with summing setting.
> 
> Token Representation Different token representation combinations are evaluated in Table TABREF13. We find that CharLSTM performs a little better than CharCNNs. Moreover, POS tags on parsing performance show that predicted POS tags decreases parsing accuracy, especially without word information. If POS tags are replaced by word embeddings, the performance increases. Finally, we apply word and CharLSTM as token representation setting for our full model.
> 
> Shared Self-attention Layers As our model providing two outputs from one input, there is a bifurcation setting for how much shared part should be determined. Both constituent and dependency parsers share token representation and 8 self-attention layers at most. Assuming that either parser always takes input information flow through 8 self-attention layers as shown in Figure FIGREF4, then the number of shared self-attention layers varying from 0 to 8 may reflect the shared degree in the model. When the number is set to 0, it indicates only token representation is shared for both parsers trained for the joint loss through each own 8 self-attention layers. When the number is set to less than 8, for example, 6, then it means that both parsers first shared 6 layers from token representation then have individual 2 self-attention layers.
> 
> For different numbers of shared layers, the results are in Table TABREF14. We respectively disable the constituent and the dependency parser to obtain a separate learning setting for both parsers in our model. The comparison in Table TABREF14 indicates that even though without any shared self-attention layers, joint training of our model may significantly outperform separate learning mode. At last, the best performance is still obtained from sharing full 8 self-attention layers.
> 
> Besides, comparing UAS and LAS to F1 score, dependency parsing is shown more beneficial from our model which has more than 1% gain in UAS and LAS from parsing constituent together.

### Relevance

Label: 

## Record 0204

Paper: Concurrent Parsing of Constituency and Dependency

### Question

> How is dependency parsing empirically verified?

### Passage

> This paper presents a joint model with the constituent and dependency parsing which achieves new state-of-the-art results on both Chinese and English benchmark treebanks. Our ablation studies show that joint learning of both constituent and dependency is indeed superior to separate learning mode. Also, experiments show that dependency parsing is much more beneficial from knowing the constituent structure. Our parser predicts phrase structure and head-word simultaneously which can be regarded as an effective HPSG BIBREF3 parser.

### Relevance

Label: 

## Record 0205

Paper: Concurrent Parsing of Constituency and Dependency

### Question

> How is dependency parsing empirically verified?

### Passage

> Using an encoder-decoder backbone, our model may be regarded as an extension of the constituent parsing model of BIBREF18 as shown in Figure FIGREF4. The difference is that in our model both constituent and dependency parsing share the same token representation and shared self-attention layers and each has its own individual Self-Attention Layers and subsequent processing layers. Our model includes four modules: token representation, self-attention encoder, constituent and dependency parsing decoder.

### Relevance

Label: 

## Record 0206

Paper: Text Summarization using Abstract Meaning Representation

### Question

> Which other methods do they compare with?

### Passage

> For the evaluation of summaries we use the standard ROGUE metric. For comparison with previous AMR based summarization methods, we report the Recall, Precision and INLINEFORM0 scores for ROGUE-1. Since most of the literature on summarization uses INLINEFORM1 scores for ROGUE-2 and ROGUE-L for comparison, we also report INLINEFORM2 scores for ROGUE-2 and ROGUE-L for our method. ROGUE-1 Recall and Precision are measured for uni-gram overlap between the reference and the predicted summary. On the other hand, ROGUE-2 uses bi-gram overlap while ROGUE-L uses the longest common sequence between the target and the predicted summaries for evaluation. In rest of this section, we provide methods to analyze and evaluate our pipeline at each step.
> 
> Step-1: AMR parsing To understand the effects of using an AMR parser on the results, we compare the final scores after the following two cases- first, when we use the gold-standard AMR graphs and second when we used the AMR graphs generated by JAMR-Parser in the pipeline. Section SECREF19 contains a comparison between the two.
> 
> Step-2: Summary graph extraction For evaluating the effectiveness of the summary graph extraction step we compare the final scores with the Lead-n-AMR baselines described in section SECREF12 .
> 
> In order to compare our summary graph extraction step with the previous work ( BIBREF0 ), we generate the final summary using the same generation method as used by them. Their method uses a simple module based on alignments for generating summary after step-2. The alignments simply map the words in the original sentence with the node or edge in the AMR graph. To generate the summary we find the words aligned with the sentence in the selected graph and output them in no particular order as the predicted summary. Though this does not generate grammatically correct sentences, we can still use the ROGUE-1 metric similar to BIBREF0 , as it is based on comparing uni-grams between the target and predicted summaries.
> 
> Step-3: Generation For evaluating the quality of the sentences generated by our method, we compare the summaries generated by the first-1 model and Lead-1-AMR model on the gold-standard dataset. However, when we looked at the scores given by ROGUE, we decided to do get the above

### Relevance

Label: 

## Record 0207

Paper: Text Summarization using Abstract Meaning Representation

### Question

> Which other methods do they compare with?

### Passage

> of the sentences generated by our method, we compare the summaries generated by the first-1 model and Lead-1-AMR model on the gold-standard dataset. However, when we looked at the scores given by ROGUE, we decided to do get the above summaries evaluated by humans. This produced interesting results which are given in more detail in section SECREF20 .

### Relevance

Label: 

## Record 0208

Paper: Text Summarization using Abstract Meaning Representation

### Question

> Which other methods do they compare with?

### Passage

> In this subsection we evaluate the effectiveness of the sentence generation step. For fair comparison at the generation step we use the gold-standard AMRs and don't perform any extraction in step-2 instead we use full AMRs, this allows to remove any errors that might have been generated in step-1 and step-2. In order to compare the quality of sentences generated by the AMR, we need a gold-standard for sentence generation step. For this, we simply use the original sentence as gold-standard for sentence generation. Thus, we compare the quality of summary generated by Lead-1 and Lead-1-AMR. The scores using the ROGUE metric are given in bottom two rows of table TABREF17 . The results show that there is significant drop in Lead-1-AMR when compared to Lead-1.
> 
> We perform human evaluation to check whether the drop in ROGUE scores is because of drop in information contained, and human readability or is it because of the inability of the ROGUE metric to judge. To perform this evaluation we randomly select ten test examples from the thirty- three test cases of the proxy report section. For each example, we show the summaries generated by four different models side by side to the human evaluators. The human evaluator does not know which summaries come from which model. A score from 1 to 10 is then assigned to each summary on the basis of readability, and information contained of summary, where 1 corresponds to the lower level and 10 to the highest. In table TABREF17 we compare the scores of these four cases as given by ROGUE along with human evaluation. The parser-generator pairs for the four cases are gold-JAMR(generator), JAMR(parser)-neural, gold-neural, and the original sentence respectively. Here gold parser means that we have used the gold-standard AMR graphs.
> 
> The scores given by the humans do not correlate with ROGUE. Human evaluators gives almost similarly scores to summary generated by the Lead-1 and Lead-1-AMR with Lead-1-AMR actually performing better on readability though it dropped some information as clear from the scores on information contained. On the other hand, ROGUE gives very high score to Lead-1 while models 1,2 and 4 get almost same scores. The similar scores of model 2

### Relevance

Label: 

## Record 0209

Paper: Text Summarization using Abstract Meaning Representation

### Question

> Which other methods do they compare with?

### Passage

> We used two datasets for the task - AMR Bank BIBREF10 and CNN-Dailymail ( BIBREF11 BIBREF12 ). We use the proxy report section of the AMR Bank, as it is the only one that is relevant for the task because it contains the gold-standard (human generated) AMR graphs for news articles, and the summaries. In the training set the stories and summaries contain 17.5 sentences and 1.5 sentences on an average respectively. The training and test sets contain 298 and 33 summary document pairs respectively.
> 
> CNN-Dailymail corpus is better suited for summarization as the average summary size is around 3 or 4 sentences. This dataset has around 300k document summary pairs with stories having 39 sentences on average. The dataset comes in 2 versions, one is the anonymized version, which has been preprocessed to replace named entities, e.g., The Times of India, with a unique identifier for example @entity1. Second is the non-anonymized which has the original text. We use the non-anonymized version of the dataset as it is more suitable for AMR parsing as most of the parsers have been trained on non-anonymized text. The dataset does not have gold-standard AMR graphs. We use automatic parsers to get the AMR graphs but they are not gold-standard and will effect the quality of final summary. To get an idea of the error introduced by using automatic parsers, we compare the results after using gold-standard and automatically generated AMR graphs on the gold-standard dataset.

### Relevance

Label: 

## Record 0210

Paper: Text Summarization using Abstract Meaning Representation

### Question

> Which other methods do they compare with?

### Passage

> Summarization of large texts is still an open problem in language processing. People nowadays have lesser time and patience to go through large pieces of text which make automatic summarization important. Automatic summarization has significant applications in summarizing large texts like stories, journal papers, news articles and even larger texts like books.
> 
> Existing methods for summarization can be broadly categorized into two categories Extractive and Abstractive. Extractive methods picks up words and sometimes directly sentences from the text. These methods are inherently limited in the sense that they can never generate human level summaries for large and complicated documents which require rephrasing sentences and incorporating information from full text to generate summaries. Most of the work done on summarization in past has been extractive.
> 
> On the other hand most Abstractive methods take advantages of the recent developments in deep learning. Specifically the recent success of the sequence to sequence learning models where recurrent networks read the text, encodes it and then generate target text. Though these methods have recently shown to be competitive with the extractive methods they are still far away from reaching human level quality in summary generation.
> 
> The work on summarization using AMR was started by BIBREF0 . Abstract Meaning Representation (AMR) was as introduced by BIBREF1 . AMR focuses on capturing the meaning of the text, by giving a specific meaning representation to the text. AMR tries to capture the "who is doing what to whom" in a sentence. The formalism aims to give same representation to sentences which have the same underlying meaning. For example "He likes apple" and "Apples are liked by him" should be assigned the same AMR.
> 
> BIBREF0 's approach aimed to produce a summary for a story by extracting a summary subgraph from the story graph and finally generate a summary from this extracted graph. But, because of the unavailability of AMR to text generator at that time their work was limited till extracting the summary graph. This method extracts a single summary graph from the story graph. Extracting a single summary graph assumes that all of the important information from the graph can be extracted from a single subgraph. But, it can be difficult in

### Relevance

Label: 

## Record 0211

Paper: A Deep Neural Architecture for Sentence-level Sentiment Classification in Twitter Social Networking

### Question

> Which three Twitter sentiment classification datasets are used for experiments?

### Passage

> Twitter sentiment classification have intensively researched in recent years BIBREF0 BIBREF1 . Different approaches were developed for Twitter sentiment classification by using machine learning such as Support Vector Machine (SVM) with rule-based features BIBREF2 and the combination of SVMs and Naive Bayes (NB) BIBREF3 . In addition, hybrid approaches combining lexicon-based and machine learning methods also achieved high performance described in BIBREF4 . However, a problem of traditional machine learning is how to define a feature extractor for a specific domain in order to extract important features.
> 
> Deep learning models are different from traditional machine learning methods in that a deep learning model does not depend on feature extractors because features are extracted during training progress. The use of deep learning methods becomes to achieve remarkable results for sentiment analysis BIBREF5 BIBREF6 BIBREF7 . Some researchers used Convolutional Neural Network (CNN) for sentiment classification. CNN models have been shown to be effective for NLP. For example, BIBREF6 proposed various kinds of CNN to learn sentiment-bearing sentence vectors, BIBREF5 adopted two CNNs in character-level to sentence-level representation for sentiment analysis. BIBREF7 constructs experiments on a character-level CNN for several large-scale datasets. In addition, Long Short-Term Memory (LSTM) is another state-of-the-art semantic composition model for sentiment classification with many variants described in BIBREF8 . The studies reveal that using a CNN is useful in extracting information and finding feature detectors from texts. In addition, a LSTM can be good in maintaining word order and the context of words. However, in some important aspects, the use of CNN or LSTM separately may not capture enough information.
> 
> Inspired by the models above, the goal of this research is using a Deep Convolutional Neural Network (DeepCNN) to exploit the information of characters of words in order to support word-level embedding. A Bi-LSTM produces a sentence-wide feature representation based on these embeddings. The Bi-LSTM is a version of BIBREF9 with Full Gradient described in BIBREF10 . In addition, the rules-based approach also effects classification accuracy by focusing on important sub-sentences expressing the main sentiment of a tweet while removing unnecessary parts of a tweet. The paper makes the following contributions:
> 
> The organization of the present paper is as follows: In section

### Relevance

Label: 

## Record 0212

Paper: A Deep Neural Architecture for Sentence-level Sentiment Classification in Twitter Social Networking

### Question

> Which three Twitter sentiment classification datasets are used for experiments?

### Passage

> As can be seen, the models with SR outperforms the model with no SR. Semantic rules is effective in order to increase classification accuracy. We evaluate the efficiency of SR for the model in Table V of our full paper . We also conduct two experiments on two separate models: DeepCNN and Bi-LSTM in order to show the effectiveness of combination of DeepCNN and Bi-LSTM. In addition, the model using TwitterGlove outperform the model using GoogleW2V because TwitterGlove captures more information in Twitter than GoogleW2V. These results show that the character-level information and SR have a great impact on Twitter Data. The pre-train word vectors are good, universal feature extractors. The difference between our model and other approaches is the ability of our model to capture important features by using SR and combine these features at high benefit. The use of DeepCNN can learn a representation of words in higher abstract level. The combination of global character fixed-sized feature vectors and a word embedding helps the model to find important detectors for particles such as 'not' that negate sentiment and potentiate sentiment such as 'too', 'so' standing beside expected features. The model not only learns to recognize single n-grams, but also patterns in n-grams lead to form a structure significance of a sentence.

### Relevance

Label: 

## Record 0213

Paper: A Deep Neural Architecture for Sentence-level Sentiment Classification in Twitter Social Networking

### Question

> Which three Twitter sentiment classification datasets are used for experiments?

### Passage

> In Twitter social networking, people express their opinions containing sub-sentences. These sub-sentences using specific PoS particles (Conjunction and Conjunctive adverbs), like "but, while, however, despite, however" have different polarities. However, the overall sentiment of tweets often focus on certain sub-sentences. For example:
> 
> @lonedog bwahahah...you are amazing! However, it was quite the letdown.
> 
> @kirstiealley my dentist is great but she's expensive...=(
> 
> In two tweets above, the overall sentiment is negative. However, the main sentiment is only in the sub-sentences following but and however. This inspires a processing step to remove unessential parts in a tweet. Rule-based approach can assists these problems in handling negation and dealing with specific PoS particles led to effectively affect the final output of classification BIBREF11 BIBREF16 . BIBREF11 summarized a full presentation of their semantic rules approach and devised ten semantic rules in their hybrid approach based on the presentation of BIBREF16 . We use five rules in the semantic rules set because other five rules are only used to compute polarity of words after POS tagging or Parsing steps. We follow the same naming convention for rules utilized by BIBREF11 to represent the rules utilized in our proposed method. The rules utilized in the proposed method are displayed in Table TABREF15 in which is included examples from STS Corpus and output after using the rules. Table TABREF16 illustrates the number of processed sentences on each dataset.

### Relevance

Label: 

## Record 0214

Paper: A Deep Neural Architecture for Sentence-level Sentiment Classification in Twitter Social Networking

### Question

> Which three Twitter sentiment classification datasets are used for experiments?

### Passage

> Our proposed model consists of a deep learning classifier and a tweet processor. The deep learning classifier is a combination of DeepCNN and Bi-LSTM. The tweet processor standardizes tweets and then applies semantic rules on datasets. We construct a framework that treats the deep learning classifier and the tweet processor as two distinct components. We believe that standardizing data is an important step to achieve high accuracy. To formulate our problem in increasing the accuracy of the classifier, we illustrate our model in Figure. FIGREF4 as follows:
> 
> Tweets are firstly considered via a processor based on preprocessing steps BIBREF0 and the semantic rules-based method BIBREF11 in order to standardize tweets and capture only important information containing the main sentiment of a tweet.
> 
> We use DeepCNN with Wide convolution for character-level embeddings. A wide convolution can learn to recognize specific n-grams at every position in a word that allows features to be extracted independently of these positions in the word. These features maintain the order and relative positions of characters. A DeepCNN is constructed by two wide convolution layers and the need of multiple wide convolution layers is widely accepted that a model constructing by multiple processing layers have the ability to learn representations of data with higher levels of abstraction BIBREF12 . Therefore, we use DeepCNN for character-level embeddings to support morphological and shape information for a word. The DeepCNN produces INLINEFORM0 global fixed-sized feature vectors for INLINEFORM1 words.
> 
> A combination of the global fixed-size feature vectors and word-level embedding is fed into Bi-LSTM. The Bi-LSTM produces a sentence-level representation by maintaining the order of words.
> 
> Our work is philosophically similar to BIBREF5 . However, our model is distinguished with their approaches in two aspects:
> 
> Using DeepCNN with two wide convolution layers to increase representation with multiple levels of abstraction.
> 
> Integrating global character fixed-sized feature vectors with word-level embedding to extract a sentence-wide feature set via Bi-LSTM. This deals with three main problems: (i) Sentences have any different size; (ii) The semantic and the syntactic of words in a sentence are captured in order to increase information for a word; (iii) Important information of characters that can appear at any position in a word are

### Relevance

Label: 

## Record 0215

Paper: A Deep Neural Architecture for Sentence-level Sentiment Classification in Twitter Social Networking

### Question

> Which three Twitter sentiment classification datasets are used for experiments?

### Passage

> Table IV shows the result of our model for sentiment classification against other models. We compare our model performance with the approaches of BIBREF0 BIBREF5 on STS Corpus. BIBREF0 reported the results of Maximum Entropy (MaxEnt), NB, SVM on STS Corpus having good performance in previous time. The model of BIBREF5 is a state-of-the-art so far by using a CharSCNN. As can be seen, 86.63 is the best prediction accuracy of our model so far for the STS Corpus.
> 
> For Sanders and HCR datasets, we compare results with the model of BIBREF14 that used a ensemble of multiple base classifiers (ENS) such as NB, Random Forest (RF), SVM and Logistic Regression (LR). The ENS model is combined with bag-of-words (BoW), feature hashing (FH) and lexicons. The model of BIBREF14 is a state-of-the-art on Sanders and HCR datasets. Our models outperform the model of BIBREF14 for the Sanders dataset and HCR dataset.

### Relevance

Label: 

## Record 0216

Paper: Correcting Length Bias in Neural Machine Translation

### Question

> What methods are used to correct the brevity problem?

### Passage

> Although highly successful, neural machine translation (NMT) systems continue to be plagued by a number of problems. We focus on two here: the beam problem and the brevity problem.
> 
> First, machine translation systems rely on heuristics to search through the intractably large space of possible translations. Most commonly, beam search is used during the decoding process. Traditional statistical machine translation systems often rely on large beams to find good translations. However, in neural machine translation, increasing the beam size has been shown to degrade performance. This is the last of the six challenges identified by BIBREF0 .
> 
> The second problem, noted by several authors, is that NMT tends to generate translations that are too short. BIBREF1 and BIBREF0 address this by dividing translation scores by their length, inspired by work on audio chords BIBREF2 . A similar method is also used by Google's production system BIBREF3 . A third simple method used by various authors BIBREF4 , BIBREF5 , BIBREF6 is a tunable reward added for each output word. BIBREF7 and BIBREF8 propose variations of this reward that enable better guarantees during search.
> 
> In this paper, we argue that these two problems are related (as hinted at by BIBREF0 ) and that both stem from label bias, an undesirable property of models that generate sentences word by word instead of all at once.
> 
> The typical solution is to introduce a sentence-level correction to the model. We show that making such a correction almost completely eliminates the beam problem. We compare two commonly-used corrections, length normalization and a word reward, and show that the word reward is slightly better.
> 
> Finally, instead of tuning the word reward using grid search, we introduce a way to learn it using a perceptron-like tuning method. We show that the optimal value is sensitive both to task and beam size, implying that it is important to tune for every model trained. Fortunately, tuning is a quick post-training step.

### Relevance

Label: 

## Record 0217

Paper: Correcting Length Bias in Neural Machine Translation

### Question

> What methods are used to correct the brevity problem?

### Passage

> Above, we have shown that fixing the length problem with a word reward score fixes the beam problem. However these results are contingent upon choosing an adequate word reward score, which we have done in our experiments by optimization using a perceptron loss. Here, we show the sensitivity of systems to the value of this penalty, as well as the fact that there is not one correct penalty for all tasks. It is dependent on a myriad of factors including, beam size, dataset, and language pair.
> 
> In order to investigate how sensitive a system is to the reward score, we varied values of INLINEFORM0 from 0 to INLINEFORM1 on both our German–English and Russian–English systems with a beam size of 50. BLEU scores and length ratios on 1000 heldout development sentences are shown in Figure FIGREF27 . The length ratio is correlated with the word reward as expected, and the BLEU score varies by more than 5 points for German–English and over 4.5 points for Russian–English. On German–English, our method found a value of INLINEFORM2 , which is slightly higher than optimal; this is because the heldout sentences have a slightly shorter length ratio than the training sentences. Conversely, on Russian–English, our found value of INLINEFORM3 is slightly lower than optimal as these heldout sentences have a slightly higher length ratio than the sentences used in training.
> 
> Tuning the reward penalty using the method described in Section SECREF6 resulted in consistent improvements in METEOR scores and length ratios across all of our systems and language pairs. Tables TABREF10 , TABREF11 , and TABREF12 show the optimized value of INLINEFORM0 for each beam size. Within a language pair, the optimal value of INLINEFORM1 is different for every beam size. Likewise, for a given beam size, the optimal value is different for every system. Our French–English and English–French systems in Table TABREF12 have the exact same architecture, data, and training criteria. Yet, even for the same beam size, the tuned word reward scores are very different.
> 
> Low-resource neural machine translation performs significantly worse than high-resource machine translation BIBREF0 . Table TABREF26 looks at the impact of training data size on BLEU scores and the beam problem by

### Relevance

Label: 

## Record 0218

Paper: Correcting Length Bias in Neural Machine Translation

### Question

> What methods are used to correct the brevity problem?

### Passage

> scores for reward and norm also increase over the baseline in most cases, despite BLEU's inherent bias towards shorter sentences. Most notably, whereas the baseline Russian–English system lost more than 20 BLEU points when the beam was increased to 1000, our tuned reward score resulted in a BLEU gain over any baseline beam size. Whereas in our baseline systems, the length ratio decreases with larger beam sizes, our tuned word reward results in length ratios of nearly 1.0 across all language pairs, mitigating many of the issues of the brevity problem.
> 
> We note that the beam problem in NMT exists for relatively small beam sizes – especially when compared to traditional beam sizes in SMT systems. On our medium-resource Russian–English system, we investigate the full impact of this problem using a much larger beam size of 1000. In Table TABREF10 , we can see that the beam problem is particularly pronounced. The first row of the table shows the uncorrected, baseline score. From a beam of 10 to a beam of 1000, the drop in BLEU scores is over 20 points. This is largely due to the brevity problem discussed earlier. The second row of the table shows the length of the translated outputs compared to the lengths of the correct translations. Though the problem persists even at a beam size of 10, at a beam size of 1000, our baseline system generates less than one third the number of words that are in the correct translations. Furthermore, 37.3% of our translated outputs have sentences of length 0. In other words, the most likely translation is to immediately generate the stop symbol. This is the problem visualized in Figure FIGREF4 .
> 
> However, when we tune our word reward score with a beam of 1000, the problem mostly goes away. Over the uncorrected baseline, we see a 22.0 BLEU point difference for a beam of 1000. Over the uncorrected baseline with a beam of 10, the corrected beam of 1000 gets a BLEU gain of 0.8 BLEU. However, the beam of 1000 still sees a drop of less than 1.0 BLEU over the best corrected version. The word reward method beats the uncorrected baseline and the

### Relevance

Label: 

## Record 0219

Paper: Correcting Length Bias in Neural Machine Translation

### Question

> What methods are used to correct the brevity problem?

### Passage

> Here, we first show that the beam problem is indeed the brevity problem. We then demonstrate that solving the length problem does solve the beam problem. Tables TABREF10 , TABREF11 , and TABREF12 show the results of our German–English, Russian–English, and French–English systems respectively. Each table looks at the impact on BLEU, METEOR, and the ratio of the lengths of generated sentences compared to the gold lengths BIBREF22 , BIBREF23 . The baseline method is a standard model without any length correction. The reward method is the tuned constant word reward discussed in the previous section. Norm refers to the normalization method, where a hypothesis' score is divided by its length.
> 
> The top sections of Tables TABREF10 , TABREF11 , TABREF12 illustrate the brevity and beam problems in the baseline models. As beam size increases, the BLEU and METEOR scores drop significantly. This is due to the brevity problem, which is illustrated by the length ratio numbers that also drop with increased beam size. For larger beam sizes, the length of the generated output sentences are a fraction of the lengths of the correct translations. For the lower-resource French–English task, the drop is more than 8 BLEU when increasing the beam size from 10 to 150. The issue is even more evident in our Russian-English system where we increase the beam to 1000 and BLEU scores drop by more than 20 points.
> 
> The results of tuning the word reward, INLINEFORM0 , as described in Section SECREF6 , is shown in the second section of Tables TABREF10 , TABREF11 , and TABREF12 . In contrast to our baseline systems, our tuned word reward always fixes the brevity problem (length ratios are approximately 1.0), and generally fixes the beam problem. An optimized word reward score always leads to improvements in METEOR scores over any of the best baselines. Across all language pairs, reward and norm have close METEOR scores, though the reward method wins out slightly. BLEU scores for reward and norm also increase over the baseline in most cases, despite BLEU's inherent bias towards shorter sentences. Most notably, whereas the baseline Russian–English system lost more than 20 BLEU points when the beam was increased to 1000,

### Relevance

Label: 

## Record 0220

Paper: Correcting Length Bias in Neural Machine Translation

### Question

> What methods are used to correct the brevity problem?

### Passage

> Without any length correction, the standard model score (higher is better) is: INLINEFORM0
> 
> To our knowledge, there are three methods in common use for adjusting the model to favor longer sentences.
> 
> Length normalization divides the score by INLINEFORM0 BIBREF0 , BIBREF1 , BIBREF2 : INLINEFORM1
> 
> Google's NMT system BIBREF3 relies on a more complicated correction: INLINEFORM0
> 
> Finally, some systems add a constant word reward BIBREF5 : INLINEFORM0
> 
> If INLINEFORM0 , this reduces to the baseline model. The advantage of this simple reward is that it can be computed on partial translations, making it easier to integrate into beam search.

### Relevance

Label: 

## Record 0221

Paper: Language Technology Programme for Icelandic 2019-2023

### Question

> What concrete software is planned to be developed by the end of the programme?

### Passage

> The Spanish LT programme Plan for Advancement of Language Technology started in 2016, and is scheduled to finish in 2020. Its aims are to develop infrastructure for LT in Spain, specifically for Spanish and the co-official languages, Basque, Catalan, Galician and Aranese. Furthermore, to promote the LT industry by boosting knowledge transfer between research and industry actors, and to improve the quality and capacity of public services by employing NLP and machine translation (MT) technology. Government should be the leading participant in LT with high-profile projects in healthcare, as well as in the judicial and educational systems, and in tourism BIBREF4.
> 
> The plan was to facilitate the development of tools and linguistic resources. Examples of tools are named entity recognisers, word-sense disambiguation, tools for computing semantic similarity and text classification, automatic summarisation and MT. Examples of linguistic resources to be developed in the programme are parallel corpora, lists of proper nouns, terminology lists and dictionaries.
> 
> The estimated total cost of the programme was 90 million euros. As the programme had just recently started when the Icelandic programme was being planned, we did not have any information on what went well and what could have been done better.

### Relevance

Label: 

## Record 0222

Paper: Language Technology Programme for Icelandic 2019-2023

### Question

> What concrete software is planned to be developed by the end of the programme?

### Passage

> A wide variety of NLP tools are to be developed or improved upon within the programme. It is of vital importance to develop quality NLP tools, as many tools often form a pipeline that analyses data and delivers the results to tools used by end users, and, in the pipeline, errors can accumulate and perpetuate.
> 
> When the programme started, there were a few available tools for Icelandic. IceNLP BIBREF27 is a suite of NLP tools containing modules for tokenisation, PoS-tagging, lemmatising, parsing and named entity recognition. Greynir BIBREF22 is a full parser which also includes a tokeniser and recognises some types of named entities. Nefnir BIBREF28 is a lemmatiser which uses suffix substitution rules, derived from the Database of Icelandic Morphology BIBREF29, giving results that outperform IceNLP. ABLTagger BIBREF30 is a PoS tagger that outperforms other taggers that have been trained for tagging Icelandic texts.
> 
> Some of these tools give good results, but can be improved upon. For other tasks, new tools need to be built. As part of the release process care will be taken to ensure all resulting software are up to high quality standards, and well documented to facilitate use by third parties. Where applicable, RESTful APIs will also be set up to further promote the usage of the products.
> 
> Tokeniser. A basic step in NLP is to segment text into units, normally sentences and tokens. Since any errors made at this stage will cascade through the process, it is important that the tokeniser is as accurate as possible. A tokeniser for Icelandic needs to be able to correctly recognises abbreviations, time units, dates, etc. It must also be adjustable and able to run using different settings, since its output must be adaptable to different projects and different uses.
> 
> Previously, two tokenisers have been built for Icelandic, one is a part of IceNLP and the other a part of Greynir. As Greynir is still in active development, it will be used as a base for the LT project's development. In order to be able to test the tokenisers' accuracy, a test set that takes different tokeniser settings into account will be developed.
> 
> PoS tagger. Precise PoS-tagging is important in many LT projects

### Relevance

Label: 

## Record 0223

Paper: Language Technology Programme for Icelandic 2019-2023

### Question

> What concrete software is planned to be developed by the end of the programme?

### Passage

> a base for the LT project's development. In order to be able to test the tokenisers' accuracy, a test set that takes different tokeniser settings into account will be developed.
> 
> PoS tagger. Precise PoS-tagging is important in many LT projects because information on word class or morphological features is often needed in later stages of an NLP pipeline. Improved tagging accuracy, thus often results in an improvement in the overall quality of LT software.
> 
> A number of PoS-taggers have been developed for Icelandic, with the best results achieved by a recent bidirectional LSTM tagging model BIBREF30. While developing PoS taggers for Icelandic further using state-of-the-art methods, we will also study and try to estimate how much accuracy can theoretically be reached in tagging a variety of Icelandic text styles, using the tag set chosen for the LT programme (see Section SECREF7).
> 
> Lemmatiser. A new lemmatiser for Icelandic, Nefnir, has recently been published BIBREF28. It has been shown to be quite accurate, although a standardised test set is not available to compare it to other lemmatisers, like Lemmald BIBREF31. Its main weakness is in lemmatising unknown words, which is a hard problem for inflected languages. We will study if its accuracy can be improved in that regard.
> 
> Parser. Three parsers have previously been developed for Icelandic. IceNLP includes a shallow parser based on a cascade of finite-state transducers BIBREF32. Greynir, on the other hand, fully parses sentences according to a hand-crafted context-free grammar. A parsing pipeline for Icelandic based on the IcePaHC corpus and the Berkeley-parser has also been released BIBREF33. No Universal Dependencies (UD) parser is available for Icelandic and no UD treebank, but in a project that started in 2019, independent of the LT programme, IcePaHC BIBREF34 will be converted to a UD treebank.
> 
> The IceNLP and Greynir parsers will be evaluated and either one of them or both developed further. We will also adapt a UD-parser to Icelandic UD-grammar.
> 
> Named entity recogniser. Some work has been carried out on named entity recognition for Icelandic. IceNLP contains a rule-based module that has achieved 71-79% accuracy and a recent tool based on a bidirectional LSTM BIBREF35 obtained an F1 score of 81.3%. There is also

### Relevance

Label: 

## Record 0224

Paper: Language Technology Programme for Icelandic 2019-2023

### Question

> What concrete software is planned to be developed by the end of the programme?

### Passage

> During the last decade, we have witnessed enormous advances in language technology (LT). Applications that allow users to interact with technology via spoken or written natural language are emerging in all areas, and access to language resources and open-source software libraries enables faster development for new domains and languages.
> 
> However, LT is highly language dependent and it takes considerable resources to develop LT for new languages. The recent LT development has focused on languages that have both a large number of speakers and huge amounts of digitized language resources, like English, German, Spanish, Japanese, etc. Other languages, that have few speakers and/or lack digitized language resources, run the risk of being left behind.
> 
> Icelandic is an example of a language with almost a negligible number of speakers, in terms of market size, since only about 350,000 people speak Icelandic as their native language. Icelandic is therefore seldom on the list of supported languages in LT software and applications.
> 
> The Icelandic Government decided in 2017 to fund a five-year programme for Icelandic LT, based on a report written by a group of LT experts BIBREF0. After more than two years of preparation, a consortium consisting of universities, institutions, associations, and private companies started the work on the programme on the 1st of October 2019. The goal of the programme is to ensure that Icelandic can be made available in LT applications, and thus will be usable in all areas of communication. Furthermore, that access to information and other language-based communication and interaction in Icelandic will be accessible to all, e.g. via speech synthesis or speech-to-text systems.
> 
> The focus of the programme will be on the development of text and speech-based language resources, on the development of core natural language processing (NLP) tools like tokenisers, taggers and parsers, and finally, to publish open-source software in the areas of speech recognition, speech synthesis, machine translation, and spell and grammar checking. All deliverables of the programme will be published under open licenses, to encourage use of resources and software in commercial products.
> 
> While the government-funded programme for the development of resources and infrastructure software builds the backbone of the Icelandic LT programme, another branch is a competitive fund for

### Relevance

Label: 

## Record 0225

Paper: Language Technology Programme for Icelandic 2019-2023

### Question

> What concrete software is planned to be developed by the end of the programme?

### Passage

> 3.5 million sentence pairs which is rather small in relation to parallel corpora in general. The goal of this phase is to create an aligned and filtered parallel corpus of translated documents from the European Economic Area (EEA) domain (e.g. regulations and directives). As of 2017, around 7,000 documents were available in Icelandic with corresponding documents in English. The aim is to pair all accessible documents in the course of the project.
> 
> Back-translation. In order to augment the training data, back-translated texts will be used. Monolingual Icelandic texts will be selected and translated to English with one of the baseline system (see below). By doing so, more training data can be obtained for the en$\rightarrow $is direction. An important part of using back-translated texts during training is filtering out translations that may otherwise lead to poor quality of the augmented part.
> 
> Baseline system. In this part, three baseline MT systems will be developed. First, a statistical phrase-based MT system based on Moses BIBREF41, second, a bidirectional LSTM model using the neural translation system OpenNMT BIBREF42, and, third, a system based on an attention-based neural network BIBREF43 using Tensor2Tensor. All the three systems will be trained on ParIce, and the additional data from tasks 1 and 2 above. Eventually, the goal is to choose the best performing MT-system for further development of MT for Icelandic.
> 
> MT interface. An API and a web user interface for the three baseline systems, mentioned in item 3 above, will be developed to give interested parties access to the systems under development, and to establish a testing environment in which members of the public can submit their own text. Thus, results from the three systems can be compared directly, as well as to the translations produced by Google Translate. Moreover, in this part, a crowd-sourcing mechanism will be developed, i.e. a functionality to allow users to submit improved translations back to the system for inclusion in the training corpus.
> 
> Pre- and postprocessing. Preprocessing in MT is the task of changing the training corpus/source text in some manner for the purpose of making the translation task easier or mark particular words/phrases that should not be translated. Postprocessing is then the task of

### Relevance

Label: 

## Record 0226

Paper: Knowledge Authoring and Question Answering with KALM

### Question

> What was their accuracy score?

### Passage

> appropriate role-filler words based on the APE parses.
> 
> Role-filler Disambiguation. Based on the extracted frame instance, the role-filler disambiguation module disambiguates the meaning of each role-filler word for the corresponding frame role a BabelNet Synset ID. A complex algorithm BIBREF5 was proposed to measure the semantic similarity between a candidate BabelNet synset that contains the role-filler word and the frame-role synset. The algorithm also has optimizations that improve the efficiency of the algorithm e.g., priority-based search, caching, and so on. In addition to disambiguating the meaning of the role-fillers, this module is also used to prune the extracted frame instances where the role-filler word and the frame role are semantically incompatible.
> 
> Constructing ULR. The extracted frame instances are translated into the corresponding logical representations, unique logical representation (ULR). Examples can be found in reference BIBREF5 .

### Relevance

Label: 

## Record 0227

Paper: Knowledge Authoring and Question Answering with KALM

### Question

> What was their accuracy score?

### Passage

> As is described in Section SECREF1 , CNL systems were proposed as the technology for knowledge representation and reasoning. Related works also include knowledge extraction tools, e.g., OpenIE BIBREF9 , SEMEFOR BIBREF10 , SLING BIBREF11 , and Standford KBP system BIBREF12 . These knowledge extraction tools are designed to extract semantic relations from English sentences that capture the meaning. The limitations of these tools are two-fold: first, they lack sufficient accuracy to extract the correct semantic relations and entities while KRR is very sensitive to incorrect data; second, these systems are not able to map the semantic relations to logical forms and therefore not capable of doing KRR. Other related works include the question answering frameworks, e.g., Memory Network BIBREF13 , Variational Reasoning Network BIBREF14 , ATHENA BIBREF15 , PowerAqua BIBREF16 . The first two belong to end-to-end learning approaches based on machine learning models. The last two systems have implemented semantic parsers which translate natural language sentences into intermediate query languages and then query the knowledge base to get the answers. For the machine learning based approaches, the results are not explainable. Besides, their accuracy is not high enough to provide correct answers. For ATHENA and PowerAqua, these systems perform question answering based on a priori knowledge bases. Therefore, they do not support knowledge authoring while KALM is able to support both knowledge authoring and question answering.

### Relevance

Label: 

## Record 0228

Paper: Knowledge Authoring and Question Answering with KALM

### Question

> What was their accuracy score?

### Passage

> This section provides a summary of the evaluation of KALM and KALM-QA, where KALM is evaluated for knowledge authoring and KALM-QA is evaluated for question answering. We have created a total of 50 logical frames, mostly derived from FrameNet but also some that FrameNet is missing (like Restaurant, Human_Gender) for representing the meaning of English sentences. Based on the 50 frames, we have manually constructed 250 sentences that are adapted from FrameNet exemplar sentences and evaluate these sentences on KALM, SEMAFOR, SLING, and Stanford KBP system. KALM achieves an accuracy of 95.6%—much higher than the other systems.
> 
> For KALM-QA, we evaluate it on two datasets. The first dataset is manually constructed general questions based on the 50 logical frames. KALM-QA achieves an accuracy of 95% for parsing the queries. The second dataset we use is MetaQA dataset BIBREF14 , which contains contains almost 29,000 test questions and over 260,000 training questions. KALM-QA achieves 100% accuracy—much higher than the state-of-the-art machine learning approach BIBREF14 . Details of the evaluations can be found in BIBREF5 and BIBREF6 .

### Relevance

Label: 

## Record 0229

Paper: Knowledge Authoring and Question Answering with KALM

### Question

> What was their accuracy score?

### Passage

> This thesis proposal provides an overview of KALM, a system for knowledge authoring. In addition, it introduces KALM-QA, the question answering part of KALM. Experimental results show that both KALM and KALM-QA achieve superior accuracy as compared to the state-of-the-art systems.

### Relevance

Label: 

## Record 0230

Paper: Knowledge Authoring and Question Answering with KALM

### Question

> What was their accuracy score?

### Passage

> system for knowledge authoring and question answering. KALM is superior to the current CNL systems in that KALM has a complex frame-semantic parser which can standardize the semantics of the sentences that express the same meaning via different linguistic structures. The frame-semantic parser is built based on FrameNet BIBREF7 and BabelNet BIBREF8 where FrameNet is used to capture the meaning of the sentence and BabelNet BIBREF8 is used to disambiguate the meaning of the extracted entities from the sentence. Experiment results show that KALM achieves superior accuracy in knowledge authoring and question answering as compared to the state-of-the-art systems.
> 
> The rest parts are organized as follows: Section SECREF2 discusses the related works, Section SECREF3 presents the KALM architecture, Section SECREF4 presents KALM-QA, the question answering part of KALM, Section SECREF5 shows the evaluation results, Section SECREF6 shows the future work beyond the thesis, and Section SECREF7 concludes the paper.

### Relevance

Label: 

## Record 0231

Paper: A Computational Approach to Automatic Prediction of Drunk Texting

### Question

> Is the data acquired under distant supervision verified by humans at any stage?

### Passage

> The ubiquity of communication devices has made social media highly accessible. The content on these media reflects a user's day-to-day activities. This includes content created under the influence of alcohol. In popular culture, this has been referred to as `drunk-texting'. In this paper, we introduce automatic `drunk-texting prediction' as a computational task. Given a tweet, the goal is to automatically identify if it was written by a drunk user. We refer to tweets written under the influence of alcohol as `drunk tweets', and the opposite as `sober tweets'.
> 
> A key challenge is to obtain an annotated dataset. We use hashtag-based supervision so that the authors of the tweets mention if they were drunk at the time of posting a tweet. We create three datasets by using different strategies that are related to the use of hashtags. We then present SVM-based classifiers that use N-gram and stylistic features such as capitalisation, spelling errors, etc. Through our experiments, we make subtle points related to: (a) the performance of our features, (b) how our approach compares against human ability to detect drunk-texting, (c) most discriminative stylistic features, and (d) an error analysis that points to future work. To the best of our knowledge, this is a first study that shows the feasibility of text-based analysis for drunk-texting prediction.

### Relevance

Label: 

## Record 0232

Paper: A Computational Approach to Automatic Prediction of Drunk Texting

### Question

> Is the data acquired under distant supervision verified by humans at any stage?

### Passage

> Using held-out dataset H, we evaluate how our system performs in comparison to humans. Three annotators, A1-A3, mark each tweet in the Dataset H as drunk or sober. Table TABREF19 shows a moderate agreement between our annotators (for example, it is 0.42 for A1 and A2). Table TABREF20 compares our classifier with humans. Our human annotators perform the task with an average accuracy of 68.8%, while our classifier (with all features) trained on Dataset 2 reaches 64%. The classifier trained on Dataset 2 is better than which is trained on Dataset 1.

### Relevance

Label: 

## Record 0233

Paper: A Computational Approach to Automatic Prediction of Drunk Texting

### Question

> Is the data acquired under distant supervision verified by humans at any stage?

### Passage

> Past studies show the relation between alcohol abuse and unsociable behaviour such as aggression BIBREF0 , crime BIBREF1 , suicide attempts BIBREF2 , drunk driving BIBREF3 , and risky sexual behaviour BIBREF4 . suicide state that “those responsible for assessing cases of attempted suicide should be adept at detecting alcohol misuse”. Thus, a drunk-texting prediction system can be used to identify individuals susceptible to these behaviours, or for investigative purposes after an incident.
> 
> Drunk-texting may also cause regret. Mail Goggles prompts a user to solve math questions before sending an email on weekend evenings. Some Android applications avoid drunk-texting by blocking outgoing texts at the click of a button. However, to the best of our knowledge, these tools require a user command to begin blocking. An ongoing text-based analysis will be more helpful, especially since it offers a more natural setting by monitoring stream of social media text and not explicitly seeking user input. Thus, automatic drunk-texting prediction will improve systems aimed to avoid regrettable drunk-texting. To the best of our knowledge, ours is the first study that does a quantitative analysis, in terms of prediction of the drunk state by using textual clues.
> 
> Several studies have studied linguistic traits associated with emotion expression and mental health issues, suicidal nature, criminal status, etc. BIBREF5 , BIBREF6 . NLP techniques have been used in the past to address social safety and mental health issues BIBREF7 .

### Relevance

Label: 

## Record 0234

Paper: A Computational Approach to Automatic Prediction of Drunk Texting

### Question

> Is the data acquired under distant supervision verified by humans at any stage?

### Passage

> Some categories of errors that occur are:
> 
> Incorrect hashtag supervision: The tweet `Can't believe I lost my bag last night, literally had everything in! Thanks god the bar man found it' was marked with`#Drunk'. However, this tweet is not likely to be a drunk tweet, but describes a drunk episode in retrospective. Our classifier predicts it as sober.
> 
> Seemingly sober tweets: Human annotators as well as our classifier could not identify whether `Will you take her on a date? But really she does like you' was drunk, although the author of the tweet had marked it so. This example also highlights the difficulty of drunk-texting prediction.
> 
> Pragmatic difficulty: The tweet `National dress of Ireland is one's one vomit.. my family is lovely' was correctly identified by our human annotators as a drunk tweet. This tweet contains an element of humour and topic change, but our classifier could not capture it.

### Relevance

Label: 

## Record 0235

Paper: A Computational Approach to Automatic Prediction of Drunk Texting

### Question

> Is the data acquired under distant supervision verified by humans at any stage?

### Passage

> We use hashtag-based supervision to create our datasets, similar to tasks like emotion classification BIBREF8 . The tweets are downloaded using Twitter API (https://dev.twitter.com/). We remove non-Unicode characters, and eliminate tweets that contain hyperlinks and also tweets that are shorter than 6 words in length. Finally, hashtags used to indicate drunk or sober tweets are removed so that they provide labels, but do not act as features. The dataset is available on request. As a result, we create three datasets, each using a different strategy for sober tweets, as follows:
> 
> The drunk tweets for Datasets 1 and 2 are the same. Figure FIGREF9 shows a word-cloud for these drunk tweets (with stop words and forms of the word `drunk' removed), created using WordItOut. The size of a word indicates its frequency. In addition to topical words such as `bar', `bottle' and `wine', the word-cloud shows sentiment words such as `love' or `damn', along with profane words.
> 
> Heuristics other than these hashtags could have been used for dataset creation. For example, timestamps were a good option to account for time at which a tweet was posted. However, this could not be used because user's local times was not available, since very few users had geolocation enabled.

### Relevance

Label: 

## Record 0236

Paper: We Built a Fake News&Click-bait Filter: What Happened Next Will Blow Your Mind!

### Question

> what types of features were used?

### Passage

> grammatical features. First, we evaluate how often stop words are used in the content of the article. Extensive usage of stop words may indicate irregularities in the text, which would be missed by the above features. Additionally, we extract ten coarse-grained part-of-speech tags from the content of the article and we use part-of-speech occurrence ratios as features. This makes a total of twenty features, as we have separate features for the title and for the contents.
> 
> All the above features are hand-crafted, evaluating a specific text metric or checking whether specific words highly correlate with one of the classes. However, we lack features that target the semantic representation of the text itself. Thus, we further use two types of word representations.
> 
> Word embeddings (601 features). As we said above, we trained domain-specific word embeddings. In order to incorporate them as features, we calculate the average vector for the title and separately for the content of the news article. We end up with two 300-dimensional embedding representations of the semantics of the articles, which we use as 300+300=600 features. We also compute the cosine similarity between the average vector of the title and the average vector of the content, because we believe that this is a highly indicative measure for at least click-bait articles, whose content differs from what their title says.
> 
> Task-specific embeddings. As a more advanced representation, we feed the text into an attention-based deep neural network, which we train to produce a task-specific embedding of the news articles. The network is designed to recognize words and sentences that contribute to the click-bait class attribution. The architecture is described in details in Section UID15

### Relevance

Label: 

## Record 0237

Paper: We Built a Fake News&Click-bait Filter: What Happened Next Will Blow Your Mind!

### Question

> what types of features were used?

### Passage

> and in the content; the fraction of capital letters to all letters in the title and in the content; the number of URLs in the content; the overlap between the words from the title and the words of the content, relying on the fact that click-baits tend to have content that does not quite match their title. These features can be very effective for modelling the author's style.
> 
> Use of irregular vocabulary (4 features): During the initial analysis of our training dataset, we noticed the presence of a high number of foreign words. As it is not common in Bulgarian news articles to use words in another language, we thought that their presence could be a valuable feature to use. One of the reasons for their occurrence might be that they were translated from a foreign resource, or that they were borrowed. We further found that many articles that were labelled as fake news contained a high number of slang words, and we added this as a feature as well. Finally, we have a feature that counts the typos in the text.
> 
> General lexical features are often used in natural language processing as they are somewhat task-independent and reasonably effective in terms of classification accuracy. In our experiments, we used TF.IDF-based features over the title and over the content of the article we wanted to classify. We had these features twice – once for the title and once for the the content of the article, as we wanted to have two different representations of the same article. Thus, we used a total of 1,100 TF.IDF-weighted features (800 content + 300 title), limiting the vocabulary to the top 800 and 300 words, respectively (which occurred in more than five articles). We should note that TF.IDF features should be used with caution as they may not remain relevant over time or in different contexts without retraining.
> 
> The last type of hand-crafted features that we used are the grammatical features. First, we evaluate how often stop words are used in the content of the article. Extensive usage of stop words may indicate irregularities in the text, which would be missed by the above features. Additionally, we extract ten

### Relevance

Label: 

## Record 0238

Paper: We Built a Fake News&Click-bait Filter: What Happened Next Will Blow Your Mind!

### Question

> what types of features were used?

### Passage

> Our framework for fake news detection is comprised of two components, which are used one after the other. First, we have an attention-based deep neural network model, which focuses on the segments of the text that are most indicative of the target class identification, and as a side effect learns task-specific representations of the news articles. We extract these representations from the last hidden layer in the network, and we feed it to the SVM classifier together with the hand-crafted features.
> 
> The attention network BIBREF31 , BIBREF32 is a powerful mechanism, inspired by the human ability to spot important sections in images or text. We adopt the approach used in BIBREF33 and employ an attention neural networks to build attention over the text of a piece of news with respect to the title it has. As far as it is in the nature of click-baits to have titles that are different from the text of the news, the attentional layers of the neural network should spot when the two texts talk about the same thing and when they are not corresponding or accurate. We implemented the attention mechanism using Keras BIBREF34 with the Tensorflow back-end BIBREF35 .
> 
> The architecture of the network with attention layers is shown in Figure FIGREF16 . Our neural model is based on Gated Recurrent Units (GRUs). GRUs are gating mechanism in RNNs which provide the ability to learn long-term dependencies and were first introduced in BIBREF36 . Given the document embedding, the GRUs build representations using input and forget gates, which help storing the valuable information through time. They build embeddings of the title and the text of the news, where at each step the unit has information only about the output from the previous step. This can be considered as a drawback, as far as we would considerably benefit if each step could construct its decision based not only on the previous step's output, but on all of the words that were processed so far. To improve this, the attention layer, for each step in the text sequence, uses the output of the steps in the title sequence. Thus, the layer learns weights, designating the strength of the relatedness

### Relevance

Label: 

## Record 0239

Paper: We Built a Fake News&Click-bait Filter: What Happened Next Will Blow Your Mind!

### Question

> what types of features were used?

### Passage

> Fake news are written and published with the intent to mislead in order to gain financially or politically, often targeting specific user groups. Another type of harmful content on the Internet are the so-called click-baits, which are distinguished by their sensational, exaggerated, or deliberately false headlines that grab attention and deceive the user into clicking an article with questionable content.
> 
> While the motives behind these two types of fake news are different, they constitute a growing problem as they constitute a sizable fraction of the online news that users encounter on a daily basis. With the recent boom of Internet, mobile, and social networks, the spread of fake news increases exponentially. Using on-line methods for spreading harmful content makes the task of keeping the Internet clean significantly harder as it is very easy to publish an article and there is no easy way to verify its veracity. Currently, domains that consistently spread misinformation are being banned from various platforms, but this is a rather inefficient way to deal with fake news as websites that specialize in spreading misinformation are reappearing with different domain names. That is why our method is based purely on text analysis, without taking into account the domain name or website's reliability as a source of information. Our work is focused on exploring various stylistic and lexical features in order to detect misleading content, and on experiments with neural network architectures in order to evaluate how deep learning can be used for detecting fake news. Moreover, we created various language-specific resources that could be used in future work on fake news and clickbait detection for Bulgarian, including task-specific word embeddings and various lexicons and dictionaries extracted from the training data.

### Relevance

Label: 

## Record 0240

Paper: We Built a Fake News&Click-bait Filter: What Happened Next Will Blow Your Mind!

### Question

> what types of features were used?

### Passage

> words that were processed so far. To improve this, the attention layer, for each step in the text sequence, uses the output of the steps in the title sequence. Thus, the layer learns weights, designating the strength of the relatedness between each word in the title and each word in the content.
> 
> For the neural network, we take the first 50 symbols of the title and the content of the news, which we choose after experiments. We train the neural network for 20 epochs and the final classification is derived with sigmoid activation. The optimizer used for the training is Adam optimizer. We feed the neural network with the embedding of the words we built earlier with word2vec.
> 
> As we will see below, the neural network is inferior in terms of performance to a feature-rich SVM (even though it performs well above the baseline). This is because it only has access to word embeddings, and does not use the manually-crafted features. Yet, its hidden layer represents a 128-dimensional task-specific embedding of the input article, and it turns out that using it as a list of 128 features in the SVM classifier yields even further great improvement, as we will see below. In this way, we combine a deep neural network with an attention mechanism with kernel-based SVM.
> 
> We feed the above-described hand-crafted features together with the task-specific embeddings learned by the deep neural neural network (a total of 1,892 attributes combined) into a Support Vector Machines (SVM) classifier BIBREF37 . SVMs have proven to perform well in different classification settings, including in the case of small and noisy datasets.

### Relevance

Label: 

## Record 0241

Paper: Learning High-order Structural and Attribute information by Knowledge Graph Attention Networks for Enhancing Knowledge Graph Embedding

### Question

> What are recent works on knowedge graph embeddings authors mention?

### Passage

> Many recent works have demonstrated the benefits of knowledge graph embedding in knowledge graph completion, such as relation extraction. However, We argue that knowledge graph embedding method still have room for improvement. First, TransE and its most extensions only take direct relations between entities into consideration. Second, most existing knowledge graph embedding methods just leverage relation triples of KGs while ignoring a large number of attribute triples. In order to overcome these limitation, inspired by the recent developments of graph convolutional networks, we propose a new knowledge graph embedding methods, named KANE. The key ideal of KANE is to aggregate all attribute triples with bias and perform embedding propagation based on relation triples when calculating the representations of given entity. Empirical results on three datasets show that KANE significantly outperforms seven state-of-arts methods.

### Relevance

Label: 

## Record 0242

Paper: Learning High-order Structural and Attribute information by Knowledge Graph Attention Networks for Enhancing Knowledge Graph Embedding

### Question

> What are recent works on knowedge graph embeddings authors mention?

### Passage

> Experimental results of entity classification on the test sets of all the datasets is shown in Table TABREF25. The results is clearly demonstrate that our proposed method significantly outperforms state-of-art results on accuracy for three datasets. For more in-depth performance analysis, we note: (1) Among all baselines, Path-based methods and Attribute-incorporated methods outperform three typical methods. This indicates that incorporating extra information can improve the knowledge graph embedding performance; (2) Four variants of KANE always outperform baseline methods. The main reasons why KANE works well are two fold: 1) KANE can capture high-order structural information of KGs in an efficient, explicit manner and passe these information to their neighboring; 2) KANE leverages rich information encoded in attribute triples. These rich semantic information can further improve the performance of knowledge graph; (3) The variant of KANE that use LSTM Encoder and Concatenation aggregator outperform other variants. The main reasons is that LSTM encoder can distinguish the word order and concatenation aggregator combine all embedding of multi-head attention in a higher leaver feature space, which can obtain sufficient expressive power.

### Relevance

Label: 

## Record 0243

Paper: Learning High-order Structural and Attribute information by Knowledge Graph Attention Networks for Enhancing Knowledge Graph Embedding

### Question

> What are recent works on knowedge graph embeddings authors mention?

### Passage

> In recent years, there are many efforts in Knowledge Graph Embeddings for KGs aiming to encode entities and relations into a continuous low-dimensional embedding spaces. Knowledge Graph Embedding provides a very simply and effective methods to apply KGs in various artificial intelligence applications. Hence, Knowledge Graph Embeddings has attracted many research attentions in recent years. The general methodology is to define a score function for the triples and finally learn the representations of entities and relations by minimizing the loss function $f_r(h,t)$, which implies some types of transformations on $\textbf {h}$ and $\textbf {t}$. TransE BIBREF7 is a seminal work in knowledge graph embedding, which assumes the embedding $\textbf {t}$ of tail entity should be close to the head entity's embedding $\textbf {r}$ plus the relation vector $\textbf {t}$ when $(h, r, t)$ holds as mentioned in section “Introduction". Hence, TransE defines the following loss function:
> 
> TransE regarding the relation as a translation between head entity and tail entity is inspired by the word2vec BIBREF21, where relationships between words often correspond to translations in latent feature space. This model achieves a good trade-off between computational efficiency and accuracy in KGs with thousands of relations. but this model has flaws in dealing with one-to-many, many-to-one and many-to-many relations.
> 
> In order to address this issue, TransH BIBREF8 models a relation as a relation-specific hyperplane together with a translation on it, allowing entities to have distinct representation in different relations. TransR BIBREF9 models entities and relations in separate spaces, i.e., entity space and relation spaces, and performs translation from entity spaces to relation spaces. TransD BIBREF22 captures the diversity of relations and entities simultaneously by defining dynamic mapping matrix. Recent attempts can be divided into two categories: (i) those which tries to incorporate additional information to further improve the performance of knowledge graph embedding, e.g., entity types or concepts BIBREF13, relations paths BIBREF17, textual descriptions BIBREF11, BIBREF12 and logical rules BIBREF23; (ii) those which tries to design more complicated strategies, e.g., deep neural network models BIBREF24.
> 
> Except for TransE and its extensions, some efforts measure plausibility by matching latent semantics of entities and relations. The basic idea behind these models is that the plausible triples of a KG

### Relevance

Label: 

## Record 0244

Paper: Learning High-order Structural and Attribute information by Knowledge Graph Attention Networks for Enhancing Knowledge Graph Embedding

### Question

> What are recent works on knowedge graph embeddings authors mention?

### Passage

> are a huge number of attribute triples in real KGs, for example the statistical results in BIBREF3 shows attribute triples are three times as many as relationship triples in English DBpedia (2016-04). Recent a few attempts try to incorporate attribute triples BIBREF11, BIBREF12. However, these are two limitations existing in these methods. One is that only a part of attribute triples are used in the existing methods, such as only entity description is used in BIBREF12. The other is some attempts try to jointly model the attribute triples and relation triples in one unified optimization problem. The loss of two kinds triples has to be carefully balanced during optimization. For example, BIBREF3 use hyper-parameters to weight the loss of two kinds triples in their models.
> 
> Considering limitations of existing knowledge graph embedding methods, we believe it is of critical importance to develop a model that can capture both high-order structural and attribute information of KGs in an efficient, explicit and unified manner. Towards this end, inspired by the recent developments of graph convolutional networks (GCN) BIBREF19, which have the potential of achieving the goal but have not been explored much for knowledge graph embedding, we propose Knowledge Graph Attention Networks for Enhancing Knowledge Graph Embedding (KANE). The key ideal of KANE is to aggregate all attribute triples with bias and perform embedding propagation based on relation triples when calculating the representations of given entity. Specifically, two carefully designs are equipped in KANE to correspondingly address the above two challenges: 1) recursive embedding propagation based on relation triples, which updates a entity embedding. Through performing such recursively embedding propagation, the high-order structural information of kGs can be successfully captured in a linear time complexity; and 2) multi-head attention-based aggregation. The weight of each attribute triples can be learned through applying the neural attention mechanism BIBREF20.
> 
> In experiments, we evaluate our model on two KGs tasks including knowledge graph completion and entity classification. Experimental results on three datasets shows that our method can significantly outperforms state-of-arts methods.
> 
> The main contributions of this study are as follows:
> 
> 1) We highlight the importance of explicitly modeling the high-order structural and attribution information of KGs to provide better knowledge graph

### Relevance

Label: 

## Record 0245

Paper: Learning High-order Structural and Attribute information by Knowledge Graph Attention Networks for Enhancing Knowledge Graph Embedding

### Question

> What are recent works on knowedge graph embeddings authors mention?

### Passage

> This model provide a flexible way to improve the ability in completing the KGs, such as predicating the missing items in knowledge graph. Since then, several methods like TransH BIBREF8 and TransR BIBREF9, which represent the relational translation in other effective forms, have been proposed. Recent attempts focused on either incorporating extra information beyond KG triples BIBREF10, BIBREF11, BIBREF12, BIBREF13, or designing more complicated strategies BIBREF14, BIBREF15, BIBREF16.
> 
> While these methods have achieved promising results in KG completion and link predication, existing knowledge graph embedding methods still have room for improvement. First, TransE and its most extensions only take direct relations between entities into consideration. We argue that the high-order structural relationship between entities also contain rich semantic relationships and incorporating these information can improve model performance. For example the fact $\textit {Donald Trump}\stackrel{Father of}{\longrightarrow }\textit {Ivanka Trump}\stackrel{Spouse}{\longrightarrow }\textit {Jared Kushner} $ indicates the relationship between entity Donald Trump and entity Jared Kushner. Several path-based methods have attempted to take multiple-step relation paths into consideration for learning high-order structural information of KGs BIBREF17, BIBREF18. But note that huge number of paths posed a critical complexity challenge on these methods. In order to enable efficient path modeling, these methods have to make approximations by sampling or applying path selection algorithm. We argue that making approximations has a large impact on the final performance.
> 
> Second, to the best of our knowledge, most existing knowledge graph embedding methods just leverage relation triples of KGs while ignoring a large number of attribute triples. Therefore, these methods easily suffer from sparseness and incompleteness of knowledge graph. Even worse, structure information usually cannot distinguish the different meanings of relations and entities in different triples. We believe that these rich information encoded in attribute triples can help explore rich semantic information and further improve the performance of knowledge graph. For example, we can learn date of birth and abstraction from values of Born and Abstract about Donald Trump in Figure FIGREF2. There are a huge number of attribute triples in real KGs, for example the statistical results in BIBREF3 shows attribute triples are three times as many as relationship triples in English DBpedia (2016-04). Recent a few attempts try to incorporate attribute

### Relevance

Label: 

## Record 0246

Paper: Modeling Event Background for If-Then Commonsense Reasoning Using Context-aware Variational Autoencoder

### Question

> How does the context-aware variational autoencoder learn event background information?

### Passage

> Traditional CVAE can model the event-target relation. In other words, given an observed event, CVAE can generate its corresponding targets. While in this paper we model the If-Then reasoning as a [(background), event]-target process. It means that in addition to the observed event, we also want to involve the event background knowledge (which can be learned from event contexts) to generate the reasonable targets.
> 
> To this end, we propose a context-aware variational autoencoder (CWVAE), with two additional latent variables: a context-acquiring latent variable $z_c$ to directly acquire context information, and a context-aware latent variable $z_{c^{\prime }}$ to learn background knowledge from $z_c$, as shown in Figure FIGREF6 (a). However, the event context information is absent in the Event2Mind and Atomic dataset. To learn from the external event context information, we design the following two-stage training procedure for CWVAE.
> 
> Pretrain: Learning Event Background Knowledge from Auxiliary Dataset In the pretrain stage, CWVAE is trained on three narrative story corpora with rich event context information. As shown in Figure FIGREF6 (a), context-acquiring latent variable $z_c$ is directly conditioned on the context $c$. Hence, $z_c$ could be employed for acquiring background knowledge from event contexts. Then, we minimize the distance between $z_c$ and the context-aware latent variable $z_{c^{\prime }}$, by which the event background knowledge is transferred from $z_c$ to $z_{c^{\prime }}$.
> 
> Finetune: Adapt Event Background Knowledge to Each Inference Dimension In the finetune stage, as shown in Figure FIGREF6 (b), CWVAE is trained on the Event2Mind and Atomic dataset without the event context information. Pretrained CWVAE is finetuned to learn the specific inferential knowledge of each inference dimension. After the training procedure, as shown in Figure FIGREF6 (c), samples of $z$ is generated based on $x$ and samples of $z_{c^{\prime }}$, where $z_{c^{\prime }}$ contains rich event background knowledge helpful for If-Then reasoning.

### Relevance

Label: 

## Record 0247

Paper: Modeling Event Background for If-Then Commonsense Reasoning Using Context-aware Variational Autoencoder

### Question

> How does the context-aware variational autoencoder learn event background information?

### Passage

> Recently, event-centered commonsense knowledge has attracted much attention BIBREF0, BIBREF1, BIBREF2, BIBREF3, because of understanding events is an important component of NLP. Given a daily-life event, human can easily understand it and reason about its causes, effects, and so on. However, it still remains a challenging task for NLP systems. This is partly due to most of them are trained for task-specific datasets or objectives, which results in models that are adapt at finding task-specific underlying correlation patterns but have limited capability in simple and explainable commonsense reasoning BIBREF4.
> 
> To facilitate this, BIBREF5 (BIBREF5) build the Event2Mind dataset and BIBREF4 (BIBREF4) present the Atomic dataset, mainly focus on nine If-Then reasoning types to describe causes, effects, intents and participant characteristic about events. Together with these datasets, a simple RNN-based encoder-decoder framework is proposed to conduct the If-Then reasoning.
> 
> However, there still remains two challenging problems. First, as illustrated in Figure FIGREF1, given an event “PersonX finds a new job”, the plausible feeling of PersonX about that event could be multiple (such as “needy/stressed out” and “relieved/joyful”). Previous work showed that for the one-to-many problem, conventional RNN-based encoder-decoder models tend to generate generic responses, rather than meaningful and specific answers BIBREF6, BIBREF7.
> 
> Second, as a commonsense reasoning problem, rich background knowledge is necessary for generating reasonable inferences. For example, as shown in Figure FIGREF1, the feeling of PersonX upon the event “PersonX finds a new job” could be multiple. However, after given a context “PersonX was fired”, the plausible inferences would be narrowed down to “needy” or “stressed out”.
> 
> To better solve these problems, we propose a context-aware variational autoencoder (CWVAE) together with a two-stage training procedure. Variational Autoencoder (VAE) based models have shown great potential in modeling the one-to-many problem and generate diversified inferences BIBREF8, BIBREF9.
> 
> In addition to the traditional VAE structure, we introduces an extra context-aware latent variable in CWVAE to learn the event background knowledge. In the pretrain stage, CWVAE is trained on an auxiliary dataset (consists of three narrative story corpora and contains rich event background knowledge), to learn the event background information by using the context-aware latent variable. Subsequently, in the finetune stage, CWVAE is trained on the task-specific dataset

### Relevance

Label: 

## Record 0248

Paper: Modeling Event Background for If-Then Commonsense Reasoning Using Context-aware Variational Autoencoder

### Question

> How does the context-aware variational autoencoder learn event background information?

### Passage

> on an auxiliary dataset (consists of three narrative story corpora and contains rich event background knowledge), to learn the event background information by using the context-aware latent variable. Subsequently, in the finetune stage, CWVAE is trained on the task-specific dataset to adapt the event background information to each specific aspect of If-Then inferential target (e.g., intents, reactions, etc.).
> 
> Experiments on the Event2Mind and Atomic dataset show that our proposed approach outperforms baseline methods in both the accuracy and diversity of inferences. The code is released at https://github.com/sjcfr/CWVAE.

### Relevance

Label: 

## Record 0249

Paper: Modeling Event Background for If-Then Commonsense Reasoning Using Context-aware Variational Autoencoder

### Question

> How does the context-aware variational autoencoder learn event background information?

### Passage

> With the incorporation of $z_{c^{\prime }}$, the original loglikelihood could be decomposed as:
> 
> Then following traditional CVAE, the ELBO of CWVAE is defined as follows:
> 
> which is the objective function at the finetune stage.
> 
> While in the pretrain stage, as we aim to learn background knowledge through minimizing the distance between $z_c$ and $z_{c^{\prime }}$, in addition to $L^{ELBO}$, a context-aware regulation term is introduced:
> 
> where the context aware regularization term is the KL distance between $z$ and $z_{c^{\prime }}$. Through minimizing the context aware regularization term, we aim to pass event context knowledge from $z_c$ to the context aware latent variable $z_{c^{\prime }}$.

### Relevance

Label: 

## Record 0250

Paper: Modeling Event Background for If-Then Commonsense Reasoning Using Context-aware Variational Autoencoder

### Question

> How does the context-aware variational autoencoder learn event background information?

### Passage

> In this paper, we propose a novel context-aware VAE (CWVAE) framework with two training stages for If-Then commonsense reasoning. By introducing an additional context-aware latent variable, CWVAE is able to learn external background knowledge, and conduct If-Then reasoning under its guidance. In the pretrain stage, CWVAE learns event background knowledge, then in the finetune stage CWVAE adapts such knowledge to each inference dimension. Experimental results demonstrate that CWVAE outperforms baseline methods in both the accuracy and diversity of generations.

### Relevance

Label: 

## Record 0251

Paper: Medication Regimen Extraction From Clinical Conversations

### Question

> Is the data de-identified?

### Passage

> We thank: University of Pittsburgh Medical Center (UPMC), and Abridge AI Inc. for providing access to the de-identified data corpus; Dr. Shivdev Rao, a faculty member and practicing cardiologist in UPMC's Heart and Vascular Institute and Prof. Florian Metze, Associate Research Professor, Carnegie Mellon University for helpful discussions; Ben Schloss, Steven Coleman, and Deborah Osakue for data business development and annotation management.

### Relevance

Label: 

## Record 0252

Paper: Medication Regimen Extraction From Clinical Conversations

### Question

> Is the data de-identified?

### Passage

> Our dataset consists of a total of 6,693 real doctor-patient conversations recorded in a clinical setting using distant microphones of varying quality. The recordings have an average duration of 9min 28s and have a verbatim transcript of 1,500 words on average (written by the experts). Both the audio and the transcript are de-identified (by removing the identifying information) with digital zeros and [de-identified] tags, respectively. The sentences in the transcript are grounded to the audio with the timestamps of its first and last word.
> 
> The transcript of the conversations are annotated with summaries and Medication Regimen tags (MR tags), both grounded using the timestamps of the sentences from the transcript deemed relevant by the expert annotators, refer to Table TABREF1. The transcript for a typical conversation can be quite long, and not easy for many of the high performing deep learning models to act on. Moreover, the medical information about a concept/condition/entity can change during the conversation after a significant time gap. For example, dosage of a medication can be different when discussing current medication the patient is on vs when they are prescribed a different dosage. Hence, we have annotations, that are grounded to a short segment of the transcript.
> 
> The summaries (#words - $\mu = 9.7; \sigma = 10.1$) are medically relevant and local. The MR tags are also local and are of the form {Medication Name, Dosage, Frequency}. If dosage ($\mu = 2.0; \sigma = 0$) or frequency ($\mu = 2.1; \sigma = 1.07$) information for a medication is not present in a grounded sentence, the corresponding field in the MR tag will be marked as `none'.
> 
> In the MR tags, Medication Name and Dosage (usually a quantity followed by its units) can be relatively easily extracted from the transcript except for the units of the dosage which is sometimes inferred. In contrast, due to high degree of linguistic variation with which Frequency is often expressed, extracting Frequency requires an additional inference step. For example, `take one in the morning and at noon' from the transcript is tagged as `twice a day' in the frequency tag, likewise `take it before sleeping' is tagged as `at night time'.
> 
> Out of overall 6,693 files,

### Relevance

Label: 

## Record 0253

Paper: Medication Regimen Extraction From Clinical Conversations

### Question

> Is the data de-identified?

### Passage

> To test the performance of our models on real-world conditions, we use commercially available ASR services (Google and IBM) to transcribe the $\mathcal {D}_{test}$ files and measure the performance of our models without assuming any annotations (except when calculating the metrics). It should be noted that this is not the case in our previous evaluations using `10% test' dataset where we use the segmentation information. For ground truth annotations on ASR transcripts, we aligned the MR tags from human written transcripts to the ASR transcript using their grounded timing information. Additionally, since ASR is prone to errors, during the alignment, if a medication from an MR tag is not recognized correctly in the ASR transcript, we remove the corresponding MR tag.
> 
> In our evaluations, we use Google Cloud Speech-to-Text (G-STT) and IBM Watson Speech to Text (IBM-STT) as these were among the top-performing ASR APIs on medical speech BIBREF19 and were readily available to us. We used G-STT, with the `video model' with punctuation settings. Unlike our human written transcripts, the transcript provided by G-STT is not verbatim and does not have disfluencies. IBM-STT, on the other hand, does not give punctuation so we used the speaker changes to add end-of-sentence punctuation.
> 
> In our $\mathcal {D}_{test}$ dataset, on initial study we see a Word Error Rate of $\sim $50% for the ASR APIs and this number is not accurate because, 1) of the de-identification, 2) disfluencies (verbatim) difference between the human written and ASR transcript, and 3) minor alignment differences between the audio and the ground truth transcript.
> 
> During this evaluation, we followed the same preprocessing methods we used during training. Then, we auto segment the transcript into small contiguous segments similar to the grounded sentences in the annotations for tags extraction. To segment the transcript, we follow a simple procedure. First, we detected all the medications in a transcript using RxNorm BIBREF20 via string matching. For all the detected medications, we selected $2 \le x \le 5$ nearby sentences as the input to our model. We increased $x$ iteratively until we encountered a quantity entity – detected using spaCy's entity recognizer, and we set $x$ as 2 if we did not detect any entities

### Relevance

Label: 

## Record 0254

Paper: Medication Regimen Extraction From Clinical Conversations

### Question

> Is the data de-identified?

### Passage

> dialogues, covers a variety of speech patterns, and the vocabulary can range from colloquial to complex domain-specific language. With recent advancements in Conversational Speech Recognition BIBREF7 rendering the systems less prone to errors, the subsequent challenge of understanding and extracting relevant information from the conversations is receiving increasing research focus BIBREF4, BIBREF8.
> 
> In this paper, we focus on local information extraction in transcribed clinical conversations. Specifically, we extract dosage (e.g. 5mg) and frequency (e.g. once a day) for the medications (e.g. aspirin) from these transcripts, collectively referred to as Medication Regimen (MR) extraction. The information extraction is local as we extract the information from a segment of the transcript and not the entire transcript since doing the latter is difficult owing to the long meandering nature of the conversations often with multiple medication regimens and care plans being discussed.
> 
> The challenges associated with the Medication Regimen (MR) extraction task include understanding the spontaneous dialog with clinical vocabulary and understanding the relationship between different entities as the discussion can contain multiple medications and dosages (e.g. doctor revising a dosage or reviewing all the current medications).
> 
> We frame this problem as a Question Answering (QA) task by generating questions using templates. We base the QA model on pointer-generator networks BIBREF9 augmented with Co-Attentions BIBREF10. In addition, we develop models combining QA and Information Extraction frameworks using multi-decoder (one each for dosage and frequency) architecture.
> 
> Lack of availability of a large volume of data is a typical challenge in healthcare. A conversation corpus by itself is a rare commodity in the healthcare data space because of the cost and difficulty in handing (because of data privacy concerns). Moreover, transcribing and labeling the conversations is a costly process as it requires domain-specific medical annotation expertise. To address data shortage and improve the model performance, we investigate different high-performance contextual embeddings (ELMO BIBREF11, BERT BIBREF12 and ClinicalBERT BIBREF13), and pretrain the models on a clinical summarization task. We further investigate the effects of training data size on our models.
> 
> On the MR extraction task, ELMo with encoder multi-decoder architecture and BERT with encoder-decoder with encoders pretrained on the summarization task perform the best. The best-performing models improve our baseline's dosage

### Relevance

Label: 

## Record 0255

Paper: Medication Regimen Extraction From Clinical Conversations

### Question

> Is the data de-identified?

### Passage

> We categorize the 10% test dataset into different categories based on the complexity and type of the data and analyze the breakdown of the system's performance in Table TABREF11. We breakdown the Frequency extraction into two categories, 1) None: ground truth Frequency tag is `none', and 2) NN (Not None): ground truth Frequency tag is not `none'. Similarly, the Dosage extraction into 5 categories, 1) None: ground truth dosage tag is `none', 2) MM (Multiple Medicine): input segment has more than one Medication mentioned, 3) MN (Multiple Numbers): input segment has more than one number present, and 4) NBM (Number between correct Dosage and Medicine) : between the Medication Name and the correct Dosage in the input segment there are other numbers present. Note that the categories of the Dosage extraction task are not exhaustive, and one tag can belong to multiple categories.
> 
> From the performance breakdown of Dosage extraction task, we see that 1) the models predict `none' better than other categories, i.e., the models are correctly able to identify when a medication's dosage is absent, 2) there is performance dip in hard cases (MM, MN, and NBM), 3) the models are able to figure out the correct dosage (decently) for a medication even when there are multiple numbers/dosage present, and 4) the model struggles the most in the NBM category. The models' low performance in NBM could be because we have a comparatively lower number of examples to train in this category. The Frequency extraction task performs equally well when the tag is `none` or not. In most categories, we see an increase in performance when using pretrained encoders.

### Relevance

Label: 

## Record 0256

Paper: Digital Stylometry: Linking Profiles Across Social Networks

### Question

> what elements of each profile did they use?

### Passage

> For the purposes of this paper, we focused on matching accounts between two of the largest social networks: Twitter and Facebook. In order to proceed with our study, we needed a sizeable (few thousand) number of English speaking users with accounts on both Twitter and Facebook. We also needed to know the precise matching between the Twitter and Facebook accounts for our ground truth.
> 
> To that end, we crawled publicly available, English-language, Google Plus accounts using the Google Plus API and scraped links to the users' other social media profiles. (Note that one of the reasons why we used Twitter and Facebook is that they were two of the most common sites linked to on Google Plus). We used a third party social media site (i.e., Google Plus), one that was not used in our analysis to compile our ground truth in order to limit selection bias in our data collection.
> 
> We discarded all users who did not link to an account for both Twitter and Facebook and those whose accounts on either of these sites were not public. We then used the APIs of Twitter and Facebook to collect posts made by the users on these sites. We only collected the linguistic content and the date and time at the which the posts were made. For technical and privacy reasons, we did not collect any information from the profile of the users, such as the location, screen name, or birthday.
> 
> Our analysis focused on activity of users for one whole year, from February 1st, 2014 to February 1st, 2015. Since we can not reliably model the behaviour patterns of users with scarce data, users with less than 20 posts in that time period on either site were discarded. Overall, we collected a dataset of $5,612$ users with each having a Facebook and Twitter account for a total of $11,224$ accounts.
> 
> Figure 1 shows the distribution of the number of posts per user for Twitter and Facebook for our collected dataset. In the figure, the data for the number of posts has been divided into 500 bins. For the Twitter data, each bin corresponds to 80 tweets, while for the Facebook data, it corresponds to

### Relevance

Label: 

## Record 0257

Paper: Digital Stylometry: Linking Profiles Across Social Networks

### Question

> what elements of each profile did they use?

### Passage

> Matching profiles across social networks is a hard task for humans. It is a task on par with detecting plagiarism, something a non-trained person (or sometimes even a trained person) cannot easily accomplish. (Hence the need for the development of the field of stylometry in early Renaissance.) Be that as it may, we wanted to evaluate our model against humans to make sure that it is indeed outperforming them.
> 
> We designed an experiment to compare the performance of human judges to our best model, the temporal-linguistic confusion model. The task had to be simple enough so that human judges could attempt it with ease. For example, it would have been ludicrous to ask the judges to sort $11,224$ accounts into $5,612$ matching pairs.
> 
> Thus, we randomly selected 100 accounts from distinct users from our collection of $11,224$ accounts. A unique list of 10 candidate accounts was created for each of the 100 accounts. Each list contained the correct matching account mixed in with 9 other randomly selected accounts. The judges were then presented with the 100 accounts one at a time and asked to pick the correct matching account from the list of 10 candidate accounts. For simplicity, we did not ask the judges to do any ranking other than picking the one account that they thought matched the original account. We then measured the accuracy of the judges based on how many of the 100 accounts they correctly matched. We had our model do the exact same task with the same dataset. A random baseline model would have a one in ten chance of getting the correct answer, giving it an accuracy of $0.10$ .
> 
> We had a total of 3 English speaking human judges from Amazon Mechanical Turk (which is an tool for crowd-sourcing of human annotation tasks) . For each task, the judges were shown the link to one of the 100 account, and its 10 corresponding candidate account links. The judges were allowed to explore each of the accounts as much as they wanted to make their decision (since all these accounts were public, there were no privacy concerns).
> 
> Table 5 shows the performance of each of the three human judges,

### Relevance

Label: 

## Record 0258

Paper: Digital Stylometry: Linking Profiles Across Social Networks

### Question

> what elements of each profile did they use?

### Passage

> There are several recent works that attempt to match profiles across different Internet services. Some of these works utilize private user data, while some, like ours, use publicly available data. An example of a work that uses private data is Balduzzi et al. BIBREF8 . They use data from the Friend Finder system (which includes some private data) provided by various social networks to link users across services. Though one can achieve a relatively high level of success by using private data to link user accounts, we are interested in using only publicly available data for this task. In fact, as mentioned earlier, we do not even consider publicly available information that could explicitly identify a user, such as names, birthdays and locations.
> 
> Several methods have been proposed for matching user profiles using public data BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 , BIBREF13 , BIBREF14 , BIBREF15 , BIBREF16 . These works differ from ours in two main aspects. First, in some of these works, the ground truth data is collected by assuming that all profiles that have the same screen name are from the same users BIBREF15 , BIBREF16 . This is not a valid assumption. In fact, it has been suggested that close to $20\%$ of accounts with the same screen name in Twitter and Facebook are not matching BIBREF17 . Second, almost all of these works use features extracted from the user profiles BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 , BIBREF13 , BIBREF14 , BIBREF15 . Our work, on the other hand, is blind to the profile information and only utilizes users' activity patterns (linguistic and temporal) to match their accounts across different social networks. Using profile information to match accounts is contrary to the best practices of stylometry since it assumes and relies on the honesty, consistency and willingness of the users to explicitly share identifiable information about themselves (such as location).

### Relevance

Label: 

## Record 0259

Paper: Digital Stylometry: Linking Profiles Across Social Networks

### Question

> what elements of each profile did they use?

### Passage

> of the probability distributions were calculated using Witten-Bell smoothing. We used the same four methods as in the last section to create our temporal models.
> 
> Table 3 shows the performance of each of these models. Although the performance of the temporal models were not as strong as the linguistic ones, they all vastly outperformed the baseline. Also, note that here as with the linguistic models, the confusion model greatly outperformed the other models.

### Relevance

Label: 

## Record 0260

Paper: Digital Stylometry: Linking Profiles Across Social Networks

### Question

> what elements of each profile did they use?

### Passage

> were allowed to explore each of the accounts as much as they wanted to make their decision (since all these accounts were public, there were no privacy concerns).
> 
> Table 5 shows the performance of each of the three human judges, our model and the random baseline. Since the task is so much simpler than pairing $11,224$ accounts, our combined confusion model had a much greater accuracy than reported in the last section. With an accuracy of $0.86$ , our model vastly outperformed even the best human judge, at $0.69$ . Overall, our model beat the average human performance by $0.26$ ( $0.86$ to $0.60$ respectively) which is a $43\%$ relative (and $26\%$ absolute) improvement.

### Relevance

Label: 

## Record 0261

Paper: Language Transfer of Audio Word2Vec: Learning Audio Segment Representations without Target Language Data

### Question

> Which pairs of languages do they consider similar enough to capture phonetic structure?

### Passage

> In the study of linguistic, scholars define a set of universal phonetic rules which describe how sounds are commonly organized across different languages. Actually, in real life, we often find languages sharing similar phonemes especially the ones spoken in nearby regions. These facts implies that when switching target languages, we do not need to learn the new audio pattern from scratch due to the transferability in spoken languages. Language transfer has shown to be helpful in STD BIBREF38 , BIBREF39 , BIBREF40 , BIBREF41 , BIBREF42 , BIBREF43 , BIBREF44 , BIBREF45 . In this paper, we focus on studying the capability of transfer learning of Audio Word2Vec.
> 
> In the proposed approach, we first train an INLINEFORM0 using the high-resource source language, as shown in the upper part of Fig. FIGREF4 , and then the encoder is used to transform the audio segment of a low-resource target language. It is also possible to fine-tune the parameters of INLINEFORM1 with the target language. In the following experiments, we found that in some cases the STD performance of the encoder without fine-tuning with the low-resource target language can be as good as the one with fine-tuning.

### Relevance

Label: 

## Record 0262

Paper: Language Transfer of Audio Word2Vec: Learning Audio Segment Representations without Target Language Data

### Question

> Which pairs of languages do they consider similar enough to capture phonetic structure?

### Passage

> Besides analyzing the cosine similarity of the learned representations, we also apply them to the query-by-example STD task. Here we compare the retrieval performance in MAP of INLINEFORM0 with different levels of accessibility to the low-resource target language along with two baseline models, INLINEFORM1 and INLINEFORM2 trained purely by the target languages. For the four target languages, the total available amount of audio word segments in the training set were 4 thousands for each language. In Table TABREF20 , we took different partitions of the target language training sets to fine tune the INLINEFORM3 pretrained by the source languages. The amount of audio word segments in these partitions are: 1K, 2K, 3K, 4K, and 0, which means no fine-tuning.
> 
> From Table TABREF20 , INLINEFORM0 trained by source language generally outperforms the INLINEFORM1 trained by the limited amount of target language (" INLINEFORM2 No Transfer"), proving that with enough audio segments, INLINEFORM3 can identify and encode universal phonetic structure. Comparing with NE, INLINEFORM4 surpasses INLINEFORM5 in German and French even without fine-tuning, whereas in Czech, INLINEFORM6 also achieves better score than INLINEFORM7 with fine-tuning. However, in Spanish, INLINEFORM8 achieved a MAP score of 0.13 with fine-tuning, slightly lower than 0.17 obtained by INLINEFORM9 . Back to Fig. FIGREF14 , the gap between phoneme sequence edit distances 2 and 3 in Spanish is smaller than other languages. Also, as discussed earlier in Section 6.2, the variance in Spanish is also bigger. The smaller gap and bigger variance together indicate that the model is weaker on Spanish at identifying audio segments of different words and thus affects the MAP performance in Spanish.

### Relevance

Label: 

## Record 0263

Paper: Language Transfer of Audio Word2Vec: Learning Audio Segment Representations without Target Language Data

### Question

> Which pairs of languages do they consider similar enough to capture phonetic structure?

### Passage

> To evaluate the quality of language transfer, we trained the Audio Word2Vec model by INLINEFORM0 from the source language, English, and applied it on different target languages, French (FRE), German (GER), Czech (CZE), and Spanish (ESP). We computed the average cosine similarity of the vector representations for each pair of the audio segments in the retrieval database of the target languages (20K segments for each language), and compare it with the phoneme sequence edit distance (PSED). The average and variance (the length of the black line on each bar) of the cosine similarity for groups of pairs clustered by the phoneme sequence edit distances (PSED) between the two words are shown in Fig. FIGREF14 . For comparison, we also provide the results obtained from the English retrieval database (250K segments), where the segments were not seen by the model in training procedure.
> 
> In Fig. FIGREF14 , the cosine similarities of the segment pairs get smaller as the edit distances increase, and the trend is observed in all languages. The gap between each edit distance groups, i.e. (0,1), (1,2), (2,3), (3,4), is obvious. This means that INLINEFORM0 learned from English can successfully encode the sequential phonetic structures into fixed-length vector for the target languages to some good extend even though it has never seen any audio data of the target languages. Another interesting fact is the corresponding variance between languages. In the source language, English, the variances of the five edit distance groups are fixed at 0.030, which means that the cosine similarity in each edit distance group is centralized. However, the variances of the groups in the target languages vary. In French and German, the variance grows from 0.030 to 0.060 as the edit distance increases from 0 to 4. For Czech/Spanish, the variance starts at a larger value of 0.040/0.050 and increases to 0.050/0.073. We suspect that the fluctuating variance is related to the similarity between languages. English, German and French are more similar compared with Czech and Spanish. Among the four target languages, German has the highest lexical similarity with English (0.60) and the second highest is French (0.27), while for Czech and Spanish, the lexical similarity scores is 0 BIBREF48 .

### Relevance

Label: 

## Record 0264

Paper: Language Transfer of Audio Word2Vec: Learning Audio Segment Representations without Target Language Data

### Question

> Which pairs of languages do they consider similar enough to capture phonetic structure?

### Passage

> In this section, we first examine how changing the hidden layer size of the RNN Encoder/Decoder, the dimension of Audio Word2Vec, affects the MAP performance of query-by-example STD (Section 6.1). After obtaining the best hidden layer size, we analyze the transferability of the Audio Word2Vec by comparing the cosine similarity of the learned representations to phoneme sequence edit distance (Section 6.2) . Visualization of multiple word pairs in different target languages is also provided (Section 6.3). Last but not least, we performed the query-by-example STD on target languages (Section 6.4). These experiments together verify that INLINEFORM0 is capable of extracting common phonetic structure in human language and thus is transferable to various languages.

### Relevance

Label: 

## Record 0265

Paper: Language Transfer of Audio Word2Vec: Learning Audio Segment Representations without Target Language Data

### Question

> Which pairs of languages do they consider similar enough to capture phonetic structure?

### Passage

> the Audio Word2Vec model learned from a high-resource language into a model targeted at a low-resource language. While this problem is not yet to be fully examined in Audio Word2Vec, works in neural machine translation (NMT) successfully transfer the model learned on high-resource languages to low-resource languages. In BIBREF15 , BIBREF16 , the authors first train a source model with high-resource language pair. The source model is used to initialize the target model which is then trained by low-resource language pairs.
> 
> For audio, all languages are uttered by human beings with a similar vocal tract structure, and therefore share some common acoustic patterns. This fact implies that knowledge obtained from one spoken language can be transferred onto other languages. This paper verifies that sequence-to-sequence autoencoder is not only able to transform audio word segments into fixed-length vectors, the model is also transferable to the languages it has never heard before. We also demonstrate its promising applications with a query-by-example spoken term detection (STD) experiment. In the query-by-example STD experiment, even without tunning with partial low-resource language segments, the autoencoder can still produce high-quality vectors.

### Relevance

Label: 

## Record 0266

Paper: Transformer-based Cascaded Multimodal Speech Translation

### Question

> What dataset was used in this work?

### Passage

> This work was supported by the MultiMT (H2020 ERC Starting Grant No. 678017) and MMVC (Newton Fund Institutional Links Grant, ID 352343575) projects.

### Relevance

Label: 

## Record 0267

Paper: Transformer-based Cascaded Multimodal Speech Translation

### Question

> What dataset was used in this work?

### Passage

> We stick to the default training/validation/test splits and the pre-extracted speech features for the How2 dataset, as provided by the organizers. As for the pre-processing, we lowercase the sentences and then tokenise them using Moses BIBREF26. We then apply subword segmentation BIBREF27 by learning separate English and Portuguese models with 20,000 merge operations each. The English corpus used when training the subword model consists of both the ground-truth video subtitles and the noisy transcripts produced by the underlying ASR system. We do not share vocabularies between the source and target domains. Finally for the post-processing step, we merge the subword tokens, apply recasing and detokenisation. The recasing model is a standard Moses baseline trained again on the parallel How2 corpus.
> 
> The baseline ASR system is trained on the How2 dataset as well. This system is then used to obtain noisy transcripts for the whole dataset, using beam-search with beam size of 10. The pre-processing pipeline for the ASR is different from the MT pipeline in the sense that the punctuations are removed and the subword segmentation is performed using SentencePiece BIBREF28 with a vocabulary size of 5,000. The test-set performance of this ASR is around 19% WER.

### Relevance

Label: 

## Record 0268

Paper: Transformer-based Cascaded Multimodal Speech Translation

### Question

> What dataset was used in this work?

### Passage

> We experiment with three types of video features, namely average-pooled vector representations (), convolutional layer outputs (), and Ten-Hot action category embeddings (). The features are provided by the How2 dataset using the following approach: a video is segmented into smaller parts of 16 frames each, and the segments are fed to a 3D ResNeXt-101 CNN BIBREF22, trained to recognise 400 action classes BIBREF23. The 2048-D fully-connected features are then averaged across the segments to obtain a single feature vector for the overall video.
> 
> In order to obtain the features, 16 equi-distant frames are sampled from a video, and they are then used as input to an inflated 3D ResNet-50 CNN BIBREF24 fine-tuned on the Moments in Time action video dataset. The CNN hence takes in a video and classifies it into one of 339 categories. The features, taken at the CONV$_4$ layer of the network, has a $7 \times 7 \times 2048$ dimensionality.
> 
> Higher-level semantic information can be more helpful than convolutional features. We apply the same CNN to a video as we do for features, but this time the focus is on the softmax layer output: we process the embedding matrix to keep the 10 most probable category embeddings intact while zeroing out the remaining ones. We call this representation ten-hot action category embeddings ().

### Relevance

Label: 

## Record 0269

Paper: Transformer-based Cascaded Multimodal Speech Translation

### Question

> What dataset was used in this work?

### Passage

> The recently introduced How2 dataset BIBREF2 has stimulated research around multimodal language understanding through the availability of 300h instructional videos, English subtitles and their Portuguese translations. For example, BIBREF3 successfully demonstrates that semantically rich action-based visual features are helpful in the context of machine translation (MT), especially in the presence of input noise that manifests itself as missing source words. Therefore, we hypothesize that a speech-to-text translation (STT) system may also benefit from the visual context, especially in the traditional cascaded framework BIBREF4, BIBREF5 where noisy automatic transcripts are obtained from an automatic speech recognition system (ASR) and further translated into the target language using a machine translation (MT) component. The dataset enables the design of such multimodal STT systems, since we have access to a bilingual corpora as well as the corresponding audio-visual stream. Hence, in this paper, we propose a cascaded multimodal STT with two components: (i) an English ASR system trained on the How2 dataset and (ii) a transformer-based BIBREF0 visually grounded MMT system.
> 
> MMT is a relatively new research topic which is interested in leveraging auxiliary modalities such as audio or vision in order to improve translation performance BIBREF6. MMT has proved effective in scenarios such as for disambiguation BIBREF7 or when the source sentences are corrupted BIBREF8. So far, MMT has mostly focused on integrating visual features into neural MT (NMT) systems using visual attention through convolutional feature maps BIBREF9, BIBREF10 or visual conditioning of encoder/decoder blocks through fully-connected features BIBREF11, BIBREF12, BIBREF13, BIBREF14.
> 
> Inspired by previous research in MMT, we explore several multimodal integration schemes using action-level video features. Specifically, we experiment with visually conditioning the encoder output and adding visual attention to the decoder. We further extend the proposed schemes to the deliberation variant BIBREF1 of the canonical transformer in two ways: additive and cascade multimodal deliberation, which are distinct in their textual attention regimes. Overall, the results show that multimodality in general leads to performance degradation for the canonical transformer and the additive deliberation variant, but can result in substantial improvements for the cascade deliberation. Our incongruence analysis BIBREF15 reveals that the transformer and cascade deliberation are more sensitive to and therefore more reliant on visual features

### Relevance

Label: 

## Record 0270

Paper: Transformer-based Cascaded Multimodal Speech Translation

### Question

> What dataset was used in this work?

### Passage

> The vanilla text-only transformer (-) is used as a baseline, and we design two variants: with additive visual conditioning (-) and with attention to visual features (-). A -features a -and a vanilla transformer decoder (-), therefore utilising visual information only at the encoder side. In contrast, a -is configured with a -and a –, exploiting visual cues only at the decoder. Figure FIGREF7 summarises the two approaches.

### Relevance

Label: 

## Record 0271

Paper: Open-World Knowledge Graph Completion

### Question

> Can the model add new relations to the knowledge graph, or just new entities?

### Passage

> set, relationship set, and triple set respectively, Closed-World Knowledge Graph Completion completes $\mathcal {G}$ by finding a set of missing triples $\mathbf {T^\prime }=\lbrace \langle h,r,t\rangle | h\in \mathbf {E}, r \in \mathbf {R}, t \in \mathbf {E}, \langle h,r,t\rangle \notin \mathbf {T}\rbrace $ in the incomplete Knowledge Graph $\mathcal {G}$ .
> 
> Closed-world KGC models heavily rely on the connectivity of the existing KG and are best able to predict relationships between existing, well-connected entities. Unfortunately, because of their strict reliance on the connectivity of the existing KG, closed-world KGC models are unable to predict the relationships of poorly connected or new entities. Therefore, we assess that closed-world KGC is most suitable for fixed or slowly evolving KGs.
> 
> However, most real-world KGs evolve quickly with new entities and relationships being added by the minute. For example, in the 6 months between DBPedia's October 2015 release and its April 2016 release $36,340$ new English entities were added – a rate of 200 new entities per day. Recall that DBPedia merely tracks changes to Wikipedia infoboxes, so these updates do not include newly added articles without valid infobox data. Because of the accelerated growth of online information, repeatedly re-training closed-world models every day (or hour) has become impractical.
> 
> In the present work we borrow the idea of open-world assumption from probabilistic database literature BIBREF8 and relax the closed-world assumption to develop an Open-World Knowledge Graph Completion model capable of predicting relationships involving unseen entities or those entities that have only a few connections. Formally we define the open-world KGC task as follows:
> 
> Definition 2 Given an incomplete Knowledge Graph $\mathcal {G}=(\mathbf {E},\mathbf {R},\mathbf {T})$ , where $\mathbf {E}$ , $\mathbf {R}$ , and $\mathbf {T}$ are the entity set, relationship set, and triple set respectively, Open-World Knowledge Graph Completion completes $\mathcal {G}$ by finding a set of missing triples $\mathbf {T^\prime }=\lbrace \langle h,r,t\rangle | \langle h,r,t\rangle \notin \mathbf {T}, h \in \mathbf {E}^i, t\in \mathbf {E}^i, r \in \mathbf {R} \rbrace $ in the incomplete Knowledge Graph $\mathcal {G}$ where $\mathbf {E}^i$ is an entity superset.
> 
> In Defn. "Closed-World Knowledge Graph Completion" we relax the constraint on the triple set $\mathbf {T^\prime }$ so that triples

### Relevance

Label: 

## Record 0272

Paper: Open-World Knowledge Graph Completion

### Question

> Can the model add new relations to the knowledge graph, or just new entities?

### Passage

> In the present work we introduced a new open-world Knowledge Graph Completion model ConMask that uses relationship-dependent content masking, fully convolutional neural networks, and semantic averaging to extract relationship-dependent embeddings from the textual features of entities and relationships in KGs. Experiments on both open-world and closed-world KGC tasks show that the ConMask model has good performance in both tasks. Because of problems found in the standard KGC data sets, we also released two new DBPedia data sets for KGC research and development.
> 
> The ConMask model is an extraction model which currently can only predict relationships if the requisite information is expressed in the entity's description. The goal for future work is to extend ConMask with the ability to find new or implicit relationships.

### Relevance

Label: 

## Record 0273

Paper: Open-World Knowledge Graph Completion

### Question

> Can the model add new relations to the knowledge graph, or just new entities?

### Passage

> r \in \mathbf {R} \rbrace $ in the incomplete Knowledge Graph $\mathcal {G}$ where $\mathbf {E}^i$ is an entity superset.
> 
> In Defn. "Closed-World Knowledge Graph Completion" we relax the constraint on the triple set $\mathbf {T^\prime }$ so that triples in $\mathbf {T^\prime }$ can contain entities that are absent from the original entity set $\mathbf {E}$ .
> 
> Closed-world KGC models learn entity and relationship embedding vectors by updating an initially random vector based on the KG's topology. Therefore, any triple $\langle h,r,t\rangle \in \mathbf {T^\prime }$ such that $h\notin \mathbf {E}$ or $t\notin \mathbf {E}$ will only ever be represented by its initial random vector because its absence does not permit updates from any inference function. In order to predict the missing connections for unseen entities, it is necessary to develop alternative features to replace the topological features used by closed-world models.
> 
> Text content is a natural substitute for the missing topological features of disconnected or newly added entities. Indeed, most KGs such as FreeBase BIBREF9 , DBPedia BIBREF0 , and SemMedDB BIBREF10 were either directly extracted from BIBREF11 , BIBREF12 , or are built in parallel to some underlying textual descriptions. However, open-world KGC differs from the standard information extraction task because 1) Rather than extracting triples from a large text corpus, the goal of open-world KGC is to discover missing relationships; and 2) Rather than a pipeline of independent subtasks like Entity Linking BIBREF13 and Slotfilling BIBREF14 , etc., open-world KGC is a holistic task that operates as a single model.
> 
> Although it may seem intuitive to simply include an entity's description into an existing KGC model, we find that learning useful vector embeddings from unstructured text is much more challenging than learning topology-embeddings as in the closed-world task. First, in closed-world KGC models, each entity will have a unique embedding, which is learned from its directly connected neighbors; whereas open-world KGC models must fuse entity embeddings with the word embeddings of the entity's description. These word embeddings must be updated by entities sharing the same words regardless of their connectivity status. Second, because of the inclusion of unstructured content, open-world models are likely to include noisy or redundant information.
> 
> With respect

### Relevance

Label: 

## Record 0274

Paper: Open-World Knowledge Graph Completion

### Question

> Can the model add new relations to the knowledge graph, or just new entities?

### Passage

> Knowledge Graphs (KGs) are a special type of information network that represents knowledge using RDF-style triples $\langle h$ , $r$ , $t\rangle $ , where $h$ represents some head entity and $r$ represents some relationship that connects $h$ to some tail entity $t$ . In this formalism a statement like “Springfield is the capital of Illinois” can be represented as $\langle $ Springfield, capitalOf, Illinois $\rangle $ . Recently, a variety of KGs, such as DBPedia BIBREF0 , and ConceptNet BIBREF1 , have been curated in the service of fact checking BIBREF2 , question answering BIBREF3 , entity linking BIBREF4 , and for many other tasks BIBREF5 . Despite their usefulness and popularity, KGs are often noisy and incomplete. For example, DBPedia, which is generated from Wikipedia's infoboxes, contains $4.6$ million entities, but half of these entities contain less than 5 relationships.
> 
> Based on this observation, researchers aim to improve the accuracy and reliability of KGs by predicting the existence (or probability) of relationships. This task is often called Knowledge Graph Completion (KGC). Continuing the example from above, suppose the relationship capitalOf is missing between Indianapolis and Indiana; the KGC task might predict this missing relationship based on the topological similarity between this part of the KG and the part containing Springfield and Illinois. Progress in vector embeddings originating with word2vec has produced major advancements in the KGC task. Typical embedding-based KGC algorithms like TransE BIBREF6 and others learn low-dimensional representations (i.e., embeddings) for entities and relationships using topological features. These models are able to predict the existence of missing relationships thereby “completing” the KG.
> 
> Existing KGC models implicitly operate under the Closed-World Assumption BIBREF7 in which all entities and relationships in the KG cannot be changed – only discovered. We formally define the Closed-word KGC task as follows:
> 
> Definition 1 Given an incomplete Knowledge Graph $\mathcal {G}=(\mathbf {E},\mathbf {R},\mathbf {T})$ , where $\mathbf {E}$ , $\mathbf {R}$ , and $\mathbf {T}$ are the entity set, relationship set, and triple set respectively, Closed-World Knowledge Graph Completion completes $\mathcal {G}$ by finding a set of missing triples $\mathbf {T^\prime }=\lbrace \langle h,r,t\rangle | h\in \mathbf {E}, r \in \mathbf {R}, t \in \mathbf {E}, \langle h,r,t\rangle

### Relevance

Label: 

## Record 0275

Paper: Open-World Knowledge Graph Completion

### Question

> Can the model add new relations to the knowledge graph, or just new entities?

### Passage

> The Freebase 15K (FB15k) data set is widely used in KGC. But FB15k is fraught with reversed- or synonym-triples BIBREF30 and does not provide sufficient textual information for content-based KGC methods to use. Due to the limited text content and the redundancy found in the FB15K data set, we introduce two new data sets DBPedia50k and DBPedia500k for both open-world and closed-world KGC tasks. Statistics of all data sets are shown in Tab. 2 .
> 
> The methodology used to evaluate the open-world and closed-world KGC tasks is similar to the related work. Specifically, we randomly selected $90\%$ of the entities in the KG and induced a KG subgraph using the selected entities, and from this reduced KG, we further removed $10\%$ of the relationships, i.e., graph-edges, to create KG $_\textrm {train}$ . All other triples not included in KG $_\textrm {train}$ are held out for the test set.

### Relevance

Label: 

## Record 0276

Paper: DP-LSTM: Differential Privacy-inspired LSTM for Stock Prediction Using Financial News

### Question

> What is the dataset used in the paper?

### Passage

> The data for this project are two parts, the first part is the historical S&P 500 component stocks, which are downloaded from the Yahoo Finance. We use the data over the period of from 12/07/2017 to 06/01/2018. The second part is the news article from financial domain are collected with the same time period as stock data. Since our paper illustrates the relationship between the sentiment of the news articles and stocks' price. Hence, only news article from financial domain are collected. The data is mainly taken from Webhose archived data, which consists of 306242 news articles present in JSON format, dating from December 2017 up to end of June 2018. The former 85% of the dataset is used as the training data and the remainder 15% is used as the testing data. The News publishers for this data are CNBC.com, Reuters.com, WSJ.com, Fortune.com. The Wall Street Journal is one of the largest newspapers in the United States, which coverage of breaking news and current headlines from the US and around the world include top stories, photos, videos, detailed analysis and in-depth thoughts; CNBC primarily carries business day coverage of U.S. and international financial markets, which following the end of the business day and on non-trading days; Fortune is an American multinational business magazine; Reuters is an international news organization. We preprocess the raw article body and use NLTK sentiment package alence Aware Dictionary and Sentiment Reasoner (VADER) to extract sentiment scores.
> 
> The stocks with missing data are deleted, and the dataset we used eventually contains 451 stocks and 4 news resources (CNBC.com, Reuters.com, WSJ.comFortune.com.). Each stock records the adjust close price and news compound scores of 121 trading days.
> 
> A rolling window with size 10 is used to separate data, that is, We predict the stock price of the next trading day based on historical data from the previous 10 days, hence resulting in a point-by-point prediction [15]. In particular, the training window is initialized with all real training data. Then we shift the window and add the next real point to the last point of training window to predict the next point and so forth. Then, according to the length of the window,

### Relevance

Label: 

## Record 0277

Paper: DP-LSTM: Differential Privacy-inspired LSTM for Stock Prediction Using Financial News

### Question

> What is the dataset used in the paper?

### Passage

> Differential privacy is one of privacy's most popular definitions today, which is a system for publicly sharing information about a dataset by describing the patterns of groups within the dataset while withholding information about individuals in the dataset. It intuitively requires that the mechanism that outputs information about an underlying dataset is robust to one sample's any change, thus protecting privacy. A mechanism ${f}$ is a random function that takes a dataset $\mathcal {N}$ as input, and outputs a random variable ${f}(\mathcal {N})$. For example, suppose $\mathcal {N}$ is a news articles dataset, then the function that outputs compound score of articles in $\mathcal {N}$ plus noise from the standard normal distribution is a mechanism [7].
> 
> Although differential privacy was originally developed to facilitate secure analysis over sensitive data, it can also enhance the robustness of the data. Note that finance data, especially news data and stock data, is unstable with a lot of noise, with a more robust data the accuracy of prediction will be improved. Since we predict stock price by fusing news come from different sources, which might include fake news. Involving differential privacy in the training to improve the robustness of the finance news is meaningful.

### Relevance

Label: 

## Record 0278

Paper: DP-LSTM: Differential Privacy-inspired LSTM for Stock Prediction Using Financial News

### Question

> What is the dataset used in the paper?

### Passage

> talking positively or negatively about the financial market, get key insights about the stock's future trend market.
> 
> We use valence aware dictionary and sentiment reasoner (VADER) to extract sentiment scores. VADER is a lexicon and rule-based sentiment analysis tool attuned to sentiments that are expressed in social media specifically [6]. VADER has been found to be quite successful when dealing with NY Times editorials and social media texts. This is because VADER not only tells about the negativity score and positively but also tells us about how positive or negative a sentiment is.
> 
> However, news reports are not all objective. We may increase bias because of some non-objective reports, if we rely on the information that is extracted from the news for prediction fully. Therefore, in order to enhance the prediction model's robustness, we will adopt differential privacy (DP) method. DP is a system for sharing information about a dataset publicly by describing groups' patterns within the dataset while withholding information about individuals in the dataset. DP can be achieved if the we are willing to add random noise to the result. For example, rather than simply reporting the sum, we can inject noise from a Laplace or gaussian distribution, producing a result that’s not quite exact, that masks the contents of any given row.
> 
> In the last several years a promising approach to private data analysis has emerged, based on DP, which ensures that an analysis outcome is "roughly as likely" to occur independent of whether any individual opts in to, or to opts out of, the database. In consequence, any one individual's specific data can never greatly affect the results. General techniques for ensuring DP have now been proposed, and a lot of datamining tasks can be carried out in a DP method, frequently with very accurate results [21]. We proposed a DP-LSTM neural network, which increase the accuracy of prediction and robustness of model at the same time.
> 
> The remainder of the paper is organized as follows. In Section 2, we introduce stock price model, the sentiment analysis and differential privacy method. In Section 3, we develop the different privacy-inspired LSTM (DP-LSTM) deep neural network and present the training details. Prediction results

### Relevance

Label: 

## Record 0279

Paper: DP-LSTM: Differential Privacy-inspired LSTM for Stock Prediction Using Financial News

### Question

> What is the dataset used in the paper?

### Passage

> To take the sentiment analysis results of the financial news into account, we introduce the sentiment-ARMA model as follows
> 
> where $\alpha $ and $\lambda $ are weighting factors; $c$ is a constant; and $f_2(\cdot )$ is similar to $f_1(\cdot )$ in the ARMA model (DISPLAY_FORM2) and is used to describe the prediction problem.
> 
> In this paper, the LSTM neural network is used to predict the stock price, the input data is the previous stock price and the sentiment analysis results. Hence, the sentiment based LSTM neural network (named sentiment-LSTM) is aimed to minimize the following loss function:
> 
> where $T$ denotes the number of prediction time slots, i.e., $t = 1,...,p$ are the observations (training input data), $t = p+1,...,p+T$ are the predicts (training output data); and $\hat{X}_t$ is given in (DISPLAY_FORM7).

### Relevance

Label: 

## Record 0280

Paper: DP-LSTM: Differential Privacy-inspired LSTM for Stock Prediction Using Financial News

### Question

> What is the dataset used in the paper?

### Passage

> The LSTM model in figure FIGREF10 has six layers, followed by an LSTM layer, a dropout layer, an LSTM layer, an LSTM layer, a dropout layer, a dense layer, respectively. The dropout layers (with dropout rate 0.2) prevent the network from overfitting. The dense layer is used to reshape the output. Since a network will be difficult to train if it contains a large number of LSTM layers [16], we use three LSTM layers here.
> 
> In each LSTM layer, the loss function is the mean square error (MSE), which is the sum of the squared distances between our target variable and the predicted value. In addition, the ADAM [17] is used as optimizer, since it is straightforward to implement, computationally efficient and well suited for problems with large data set and parameters.
> 
> There are many methods and algorithms to implement sentiment analysis systems. In this paper, we use rule-based systems that perform sentiment analysis based on a set of manually crafted rules. Usually, rule-based approaches define a set of rules in some kind of scripting language that identify subjectivity, polarity, or the subject of an opinion. We use VADER, a simple rule-based model for general sentiment analysis.

### Relevance

Label: 

## Record 0281

Paper: Casting Light on Invisible Cities: Computationally Engaging with Literary Criticism

### Question

> How do they model a city description using embeddings?

### Passage

> We compare clusters computed on different representations using community purity; additionally, we compare these computational methods to humans by their accuracy on the odd-one-out task.
> 
> City representations computed using language model-based representation (ELMo and BERT) achieve significantly higher purity than a clustering induced from random representations, indicating that there is at least some meaningful coherence to Calvino's thematic groups (first row of Table TABREF11 ). ELMo representations yield the highest purity among the three methods, which is surprising as BERT is a bigger model trained on data from books (among other domains). Both ELMo and BERT outperform GloVe, which intuitively makes sense because the latter do not model the order or structure of the words in each description.
> 
> While the purity of our methods is higher than that of a random clustering, it is still far below 1. To provide additional context to these results, we now switch to our “odd-one-out” task and compare directly to human performance. For each triplet of cities, we identify the intruder as the city with the maximum Euclidean distance from the other two. Interestingly, crowd workers achieve only slightly higher accuracy than ELMo city representations; their interannotator agreement is also low, which indicates that close reading to analyze literary coherence between multiple texts is a difficult task, even for human annotators. Overall, results from both computational and human approaches suggests that the author-assigned labels are not entirely arbitrary, as we can reliably recover some of the thematic groups.

### Relevance

Label: 

## Record 0282

Paper: Casting Light on Invisible Cities: Computationally Engaging with Literary Criticism

### Question

> How do they model a city description using embeddings?

### Passage

> While each of the city descriptions is relatively short, Calvino's writing is filled with rare words, complex syntactic structures, and figurative language. Capturing the essential components of each city in a single vector is thus not as simple as it is with more standard forms of text. Nevertheless, we hope that representations from language models trained over billions of words of text can extract some meaningful semantics from these descriptions. We experiment with three different pretrained representations: ELMo BIBREF5 , BERT BIBREF6 , and GloVe BIBREF18 . To produce a single city embedding, we compute the TF-IDF weighted element-wise mean of the token-level representations. For all pretrained methods, we additionally reduce the dimensionality of the city embeddings to 40 using PCA for increased compatibility with our clustering algorithm.

### Relevance

Label: 

## Record 0283

Paper: Casting Light on Invisible Cities: Computationally Engaging with Literary Criticism

### Question

> How do they model a city description using embeddings?

### Passage

> Our work takes a first step towards computationally engaging with literary criticism on a single book using state-of-the-art text representation methods. While we demonstrate that NLP techniques can be used to support literary analyses and obtain new insights, they also have clear limitations (e.g., in understanding abstract themes). As text representation methods become more powerful, we hope that (1) computational tools will become useful for analyzing novels with more conventional structures, and (2) literary criticism will be used as a testbed for evaluating representations.

### Relevance

Label: 

## Record 0284

Paper: Casting Light on Invisible Cities: Computationally Engaging with Literary Criticism

### Question

> How do they model a city description using embeddings?

### Passage

> Given 55 city representations, how do we group them into eleven clusters of five cities each? Initially, we experimented with a graph-based community detection algorithm that maximizes cluster modularity BIBREF20 , but we found no simple way to constrain this method to produce a specific number of equally-sized clusters. The brute force approach of enumerating all possible cluster assignments is intractable given the large search space ( INLINEFORM0 possible assignments). We devise a simple clustering algorithm to approximate this process. First, we initialize with random cluster assignments and define “cluster strength” to be the relative difference between “intra-group” Euclidean distance and “inter-group” Euclidean distance. Then, we iteratively propose random exchanges of memberships, only accepting these proposals when the cluster strength increases, until convergence. To evaluate the quality of the computationally-derived clusters against those of Calvino, we measure cluster purity BIBREF21 : given a set of predicted clusters INLINEFORM1 and ground-truth clusters INLINEFORM2 that both partition a set of INLINEFORM3 data points, INLINEFORM4

### Relevance

Label: 

## Record 0285

Paper: Casting Light on Invisible Cities: Computationally Engaging with Literary Criticism

### Question

> How do they model a city description using embeddings?

### Passage

> Literary critics form interpretations of meaning in works of literature. Building computational models that can help form and test these interpretations is a fundamental goal of digital humanities research BIBREF0 . Within natural language processing, most previous work that engages with literature relies on “distant reading” BIBREF1 , which involves discovering high-level patterns from large collections of stories BIBREF2 , BIBREF3 . We depart from this trend by showing that computational techniques can also engage with literary criticism at a closer distance: concretely, we use recent advances in text representation learning to test a single literary theory about the novel Invisible Cities by Italo Calvino.
> 
> Framed as a dialogue between the traveler Marco Polo and the emperor Kublai Khan, Invisible Cities consists of 55 prose poems, each of which describes an imaginary city. Calvino categorizes these cities into eleven thematic groups that deal with human emotions (e.g., desires, memories), general objects (eyes, sky, signs), and unusual properties (continuous, hidden, thin). Many critics argue that Calvino's labels are not meaningful, while others believe that there is a distinct thematic separation between the groups, including the author himself BIBREF4 . The unique structure of this novel — each city's description is short and self-contained (Figure FIGREF1 ) — allows us to computationally examine this debate.
> 
> As the book is too small to train any models, we leverage recent advances in large-scale language model-based representations BIBREF5 , BIBREF6 to compute a representation of each city. We feed these representations into a clustering algorithm that produces exactly eleven clusters of five cities each and evaluate them against both Calvino's original labels and crowdsourced human judgments. While the overall correlation with Calvino's labels is low, both computers and humans can reliably identify some thematic groups associated with concrete objects.
> 
> While prior work has computationally analyzed a single book BIBREF7 , our work goes beyond simple word frequency or n-gram counts by leveraging the power of pretrained language models to engage with literary criticism. Admittedly, our approach and evaluations are specific to Invisible Cities, but we believe that similar analyses of more conventionally-structured novels could become possible as text representation methods improve. We also highlight two challenges of applying computational methods

### Relevance

Label: 

## Record 0286

Paper: How to Ask Better Questions? A Large-Scale Multi-Domain Dataset for Rewriting Ill-Formed Questions

### Question

> What characterizes the 303 domains? e.g. is this different subject tags?

### Passage

> To better evaluate model performance, we conduct a human evaluation on the model rewritten questions following the same guidelines from the “Dataset Quality” subsection. Among the 300 questions annotated earlier, we chose the ill-formed questions from the TEST split, which yields 75 questions. We evaluate questions rewritten by three methods (Transformer (MQR + Quora), GEC, and Transformer (MQR + Quora) $\rightarrow $ GEC), and ask annotators to determine the qualities of the rewritten questions. To understand if question meanings change after rewriting, we also annotate whether a model rewritten question is semantically equivalent to the ill-formed question or equivalent to the well-formed one.
> 
> Table TABREF33 shows the annotations from two annotators. When the two annotators disagree, a judge makes a final decision. Note that the examples annotated here are a subset of those annotated in Table TABREF15, so the first row is different from the ill-formed questions in Table TABREF15. According to the annotations, the GEC method slightly improves the question quality scores. Although Table TABREF30 shows that GEC improves the question quality by some automatic metrics, it simply corrects a few grammatical errors and the rewritten questions still do not meet the standards of human annotators. However, the GEC model is good at preserving question semantics.
> 
> The Transformer (MQR + Quora) model and Transformer (MQR + Quora) $\rightarrow $ GEC excel at improving question quality in all three aspects, but they suffer from semantic drift. This suggests that future work should focus on solving the problem of semantic drift when building question rewriting models.
> 
> Table TABREF34 shows two example questions rewritten by different methods. The questions rewritten by GEC remain unchanged but are still of low quality, whereas ParaNMT and round trip NMT make a variety of changes, resulting in large variations in question quality and semantics. Methods trained on MQR excel at converting ill-formed questions into explicit ones (e.g., adding “What is” in the first example and “How to” in the second example), but sometimes make grammatical errors (e.g., Trans. (MQR + Quora) misses “a” in the second example). According to Table TABREF32, combining neural models trained on MQR and GEC achieves the best results in automatic metrics. However, they still suffer from

### Relevance

Label: 

## Record 0287

Paper: How to Ask Better Questions? A Large-Scale Multi-Domain Dataset for Rewriting Ill-Formed Questions

### Question

> What characterizes the 303 domains? e.g. is this different subject tags?

### Passage

> but sometimes make grammatical errors (e.g., Trans. (MQR + Quora) misses “a” in the second example). According to Table TABREF32, combining neural models trained on MQR and GEC achieves the best results in automatic metrics. However, they still suffer from semantic drift. In the first example of Table TABREF34, the last two rewrites show significant semantic mistakes, generating non-existent words “widebutcherblock” and “widebitcherblock”.

### Relevance

Label: 

## Record 0288

Paper: How to Ask Better Questions? A Large-Scale Multi-Domain Dataset for Rewriting Ill-Formed Questions

### Question

> What characterizes the 303 domains? e.g. is this different subject tags?

### Passage

> We construct our Multi-Domain Question Rewriting (MQR) dataset from human contributed Stack Exchange question edit histories. Stack Exchange is a question answering platform where users post and answer questions as a community. Stack Exchange has its own standard of good questions, and their standard aligns well with our definition of well-formed questions. If questions on Stack Exchange do not meet their quality standards, members of the community often volunteer to edit the questions. Such edits typically correct spelling and grammatical errors while making the question more explicit and easier to understand.
> 
> We use 303 sub areas from Stack Exchange data dumps. The full list of area names is in the appendix. We do not include Stack Overflow because it is too specific to programming related questions. We also exclude all questions under the following language sub areas: Chinese, German, Spanish, Russian, Japanese, Korean, Latin, Ukrainian. This ensures that the questions in MQR are mostly English sentences. Having questions from 303 Stack Exchange sites makes the MQR dataset cover a broad range of domains.
> 
> We use “PostHistory.xml” and “Posts.xml” tables of each Stack Exchange site data dump. If a question appears in both “PostHistory.xml” and “Posts.xml”, it means the question was modified. We treat the most up-to-date Stack Exchange questions as a well formed-question and treat its version from “PostHistory.xml” as ill-formed. “PostHistory.xml” only keeps one edit for each question, so the MQR dataset does not contain duplicated questions.
> 
> The questions in the Stack Exchange raw data dumps do not always fulfill our data quality requirements. For example, some questions after rewriting are still not explicit. Sometimes rewriting introduces or deletes new information and cannot be done correctly without more context or the question description. We thus perform the following steps to filter the question pairs:
> 
> All well-formed questions in the pairs must start with “how”, “why”, “when”, “what”, “which”, “who”, “whose”, “do”, “where”, “does”, “is”, “are”, “must”, “may”, “need”, “did”, “was”, “were”, “can”, “has”, “have”, “are”. This step is performed to make sure the questions are explicit questions but not statements or commands.
> 
> To ensure there are no sentences written in non-English languages, we keep questions that contain 80% or more of valid English characters,

### Relevance

Label: 

## Record 0289

Paper: How to Ask Better Questions? A Large-Scale Multi-Domain Dataset for Rewriting Ill-Formed Questions

### Question

> What characterizes the 303 domains? e.g. is this different subject tags?

### Passage

> As the MQR dataset is constructed from 303 sub areas of the Stack Exchange networks, it covers a wide range of question domains. Table TABREF16 summarizes the number of categories in the TRAIN and DEVTEST portions of the MQR dataset, as well as the mean, standard deviation, minimum, and maximum number of instances per categories.
> 
> The number of questions from each sub area is not evenly distributed due to the fact that some sub areas are more popular and have more questions than the others, but the DEV/TEST splits still cover a reasonably large range of domains.
> 
> The most common categories in DEV and TEST are “diy”(295), “askubuntu”(288), “math”(250), “gaming”(189), and “physics”(140). The least common categories are mostly “Meta Stack Exchange” websites where people ask questions regarding the policies of posting questions on Stack Exchange sites. The most common categories in TRAIN are “askubuntu”(6237), “math”(5933), “gaming”(3938), “diy”(2791), and “2604”(scifi).

### Relevance

Label: 

## Record 0290

Paper: How to Ask Better Questions? A Large-Scale Multi-Domain Dataset for Rewriting Ill-Formed Questions

### Question

> What characterizes the 303 domains? e.g. is this different subject tags?

### Passage

> We also benchmark other methods involving different training datasets and models. All the methods in this subsection use transformer models.

### Relevance

Label: 

## Record 0291

Paper: Is change the only constant? Profile change perspective on #LokSabhaElections2019

### Question

> What are the organic and inorganic ways to show political affiliation through profile changes?

### Passage

> In this paper, we study the use of profile attributes on Twitter as the major endorsement during #LokSabhaElectios2019. We identify $1,293$ verified political leader's profile and extract $49,433,640$ unique followers. We collect the daily and weekly snapshots of the political leaders and the follower handles from 5th April, 2019 to 5th June, 2019. With the constraint of Twitter API, we collected a total of 9 snapshots of the follower's profile and 61 snapshots of Political handles. We consider the 5 major attributes for the analysis, including, Profile Name, Username, Description, Profile Image, and Location.
> 
> Firstly, we analyze the most changed attributes among the 5 major attributes. We find that most of the users made at-most 4 changes during the election campaign, with profile image being the most changed attribute for both the political as well as follower handles. We also show that political handles made more changes to profile attributes than the follower handles. About $80\%$ changes made by the followers in the period of data collection was related to #LokSabhaElectios2019. While the profile handles made changes, the changes mostly included going back and forth to same profile attribute, with the change in attribute being active support to a political party or political leader.
> 
> We argue that we can predict the political inclination of a user using just the profile attribute of the users. We further show that the presence of party name in the profile attribute can be considered as an organic behavior and signals support to a party. However, we argue that the addition of election campaign related keywords to the profile is a form of inorganic behavior. The inorganic behavior analysis falls inline with behavior contagion, where the followers tend to adapt to the behavior of their opinion leaders. The “Chowkidar movement” showed a similar effect in the #LokSabhaElectios2019, which was evident by how the other political leaders and followers of BJP party added chowkidar to their profile attributes after @narendramodi did. We thus, argue that people don't shy away from showing support to political parties through profile information.
> 
> We believe our analysis will be helpful to understand how social movement like election are perceived and sustained through profile attributes on social

### Relevance

Label: 

## Record 0292

Paper: Is change the only constant? Profile change perspective on #LokSabhaElections2019

### Question

> What are the organic and inorganic ways to show political affiliation through profile changes?

### Passage

> In summary, our main contributions are:
> 
> We collect daily and weekly profile snapshots of $1,293$ political handles on Twitter and over 55 million of their followers respectively over a period of two months during and after the #LokSabhaElections2019. We will make the data and code available on our website.
> 
> We analyze the political and follower handles for profile changes over the snapshots and show that the political handles engage in more profile change behavior. We also show that certain profile attributes are changed more frequently than others with subtle differences in the behavior of political and follower accounts.
> 
> We show users display support for a political party on Twitter through both organic means like party name mentions on their profile, and inorganic means such as showing support for a movement like #MainBhiChowkidar. We analyze the Chowkidar movement in detail and demonstrate that it illustrates a contagion behavior.
> 
> We perform topic modelling of the users who took part in the Chowkidar movement and show that they were most likely Narendra Modi supporters and mostly discussed political topics on Twitter.

### Relevance

Label: 

## Record 0293

Paper: Is change the only constant? Profile change perspective on #LokSabhaElections2019

### Question

> What are the organic and inorganic ways to show political affiliation through profile changes?

### Passage

> The real and virtual world are intertwined in a way that any speech, event, or action of leaders may trigger the changes is behavior of people online BIBREF1, BIBREF21. Opinion leaders have been defined as `the individuals who were likely to influence other persons in their immediate environment.' BIBREF22 Opinion leaders on social media platforms help in adoption of behavior by followers easily BIBREF9, BIBREF6. The performance and effectiveness of the opinion leader directly affect the contagion of the leader BIBREF9. On Twitter, opinion leaders show high motivation for information seeking and public expression. Moreover, they make a significant contribution to people's political involvement BIBREF21.
> 
> Our work contributes to this literature in two major ways. First, we investigate how profile attribute changes are similar or different from the influential leaders in the country and how much of these changes are the result of the same. Then we see how the users change their profile information in the midst of election in the largest democracy in the world.

### Relevance

Label: 

## Record 0294

Paper: Is change the only constant? Profile change perspective on #LokSabhaElections2019

### Question

> What are the organic and inorganic ways to show political affiliation through profile changes?

### Passage

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

### Relevance

Label: 

## Record 0295

Paper: Is change the only constant? Profile change perspective on #LokSabhaElections2019

### Question

> What are the organic and inorganic ways to show political affiliation through profile changes?

### Passage

> Social Media profiles are a way to present oneself and to cultivate relationship with like minded or desired audience. BIBREF0, BIBREF12. With change in time and interest, users on Twitter change their profile names, description, screen names, location or language BIBREF2. Some of these changes are organic BIBREF13, BIBREF2, while other changes can be triggered by certain events BIBREF14, BIBREF15. In this section, we look into the previous literature which are related to user profile attribute's change behavior. We further look into how Twitter has been used to initiate or sustain movements BIBREF14, BIBREF15, BIBREF1. Finally we investigate how the contagion behavior adaptation spread through opinion leaders BIBREF6, BIBREF9 and conclude with our work's contribution to the literature.

### Relevance

Label: 

## Record 0296

Paper: Building a robust sentiment lexicon with (almost) no resource

### Question

> Do they compare against manually-created lexicons?

### Passage

> Sentiment analysis is a task that aims at recognizing in text the opinion of the writer. It is often modeled as a classification problem which relies on features extracted from the text in order to feed a classifier. Relevant features proposed in the literature span from microblogging artifacts including hashtags, emoticons BIBREF0 , BIBREF1 , intensifiers like all-caps words and character repetitions BIBREF2 , sentiment-topic features BIBREF3 , to the inclusion of polarity lexicons.
> 
> The objective of the work presented in this paper is the creation of sentiment polarity lexicons. They are word lists or phrase lists with positive and negative sentiment labels. Sentiment lexicons allow to increase the feature space with more relevant and generalizing characteristics of the input. Unfortunately, creating sentiment lexicons requires human expertise, is time consuming, and often results in limited coverage when dealing with new domains.
> 
> In the literature, it has been proposed to extend existing lexicons without supervision BIBREF4 , BIBREF5 , or to automatically translate existing lexicons from resourceful languages with statistical machine translation (SMT) systems BIBREF6 . While the former requires seed lexicons, the later are very interesting because they can automate the process of generating sentiment lexicons without any human expertise. But automatically translating sentiment lexicons leads to two problems: (1) out-of-vocabulary words, such as mis-spellings, morphological variants and slang, cannot be translated, and (2) machine translation performance strongly depends on available training resources such as bi-texts.
> 
> In this paper, we propose to apply the method proposed in BIBREF7 for automatically mapping word embeddings across languages and use them to translate sentiment lexicons only given a small, general bilingual dictionary. After creating monolingual word embeddings in the source and target language, we train a linear transform on the bilingual dictionary and apply that transform to words for which we don't have a translation.
> 
> We perform experiments on 3-class polarity classification in tweets, and report results on four different languages: French, Italian, Spanish and German. Existing English sentiment lexicons are translated to the target languages through the proposed approach, given gs trained on the respective Wikipedia of each language. Then, a SVM-based classifier is fed with lexicon features, comparing machine translation with embedding transfer.
> 
> After presenting related

### Relevance

Label: 

## Record 0297

Paper: Building a robust sentiment lexicon with (almost) no resource

### Question

> Do they compare against manually-created lexicons?

### Passage

> Table TABREF2 reports the results of the system and different baselines. The No Sentiment Lexicon system does not have any lexicon feature. It obtains a macro-fmeasure of 60.65 on the four corpora.
> 
> Systems denoted BIBREF21 , BIBREF22 , BIBREF23 are baselines that correspond respectively to unsupervised, supervised and semi-supervised approaches for generating the lexicon. We observe that adding sentiment lexicons improves performance.
> 
> The Moses system consists in translating the different sentiment lexicons with the Moses SMT toolkit. It is trained on the Europarl bi-texts. The approach based on translation obtains better results than the Baseline systems. In our experiments, we observe that some words have not been correctly translated (for example: slang words). The main drawback on this approach is that for correctly translating sentiment lexica, the SMT system must be trained on in-domain bi-texts..
> 
> The BWE (Bilingual Word Embeddings) system consists in translating the sentiment lexicons with our method. This approach obtains results comparable to the SMT approach. The main advantage of this approach is to be able to generalize on words unknown to the SMT system.
> 
> Moses and BWE can be combined by creating a lexicon from the union of the lexicons obtained by those systems. This combination yields even better results than translation or mapping alone.
> 
> Our second experiment consists in varying the size of the bilingual dictionary used to train INLINEFORM0 . Figure FIGREF20 shows the evolution of average macro f-measure (over the four languages) when the INLINEFORM1 most frequent words from Wikipedia are part of the bilingual dictionary. It can be observed that using the 50k most frequent words leads to the best performance (an average macro-fmeasure of 61.72) while only 1,000 words already brings nice improvements.
> 
> In a last experiment, we look into the gains that can be obtained by manually translating a small part of the lexicon and use it as bilingual dictionary when training the transformation matrix. Figure FIGREF21 shows average macro-fmeasure on the four languages when translating up to 2,000 words from the MPQA lexicon (out of 8k). It can be observed that from 600 words on, performance is better than that of the statistical translation system.

### Relevance

Label: 

## Record 0298

Paper: Building a robust sentiment lexicon with (almost) no resource

### Question

> Do they compare against manually-created lexicons?

### Passage

> In order to test the value of the create lexicons, we use them in a typical sentiment polarity classification system BIBREF31 . We first tokenize the tweets with a tokenizer based on macaon BIBREF32 . Then, hashtags and usertags are mapped to generic tokens. Each tweet is represented with the following features and an SVM classifier with a linear kernel is trained to perform the task.
> 
> Words n-grams
> 
> All-caps: the number of words with all characters in upper case
> 
> Hashtags: the number of hashtags
> 
> Lexicons: number of words present in each lexicon
> 
> Punctuation: the number of contiguous sequences of exclamation marks, question marks, and both exclamation and question marks
> 
> Last punctuation: whether the last token contains an exclamation or question mark
> 
> Emoticons: presence or absence of positive and negative emoticons at any position in the tweet
> 
> Last emoticon: whether the last token is a positive or negative emoticon
> 
> Elongated words: the number of words with one character repeated more than three times, for example : “loooool"
> 
> We did not implement part-of-speech and cluster features as they cannot be assumed to be available in the target languages. This system was part of the system combination that obtained the best results at the TASS 2015 BIBREF25 , BIBREF33 and DEFT 2015 BIBREF34 , BIBREF35 evaluation campaigns.

### Relevance

Label: 

## Record 0299

Paper: Building a robust sentiment lexicon with (almost) no resource

### Question

> Do they compare against manually-created lexicons?

### Passage

> Our approach consists in creating distributional word representations in the source and target languages, and map them to each other with a linear transform trained given a small bilingual dictionary of frequent words. Then, source language words from the polarity lexicon can be projected in the target language embedding. The closest words to the projecting are used as translation.
> 
> In our experiments, word embeddings are estimated on the source and target language Wikipedia corpora using the word2vec toolkit BIBREF19 . The embeddings are trained using skip-gram approach with a window of size 7 and 5 iterations. The dimension of the embeddings is fixed to 200.
> 
> BIBREF20 have shown that the skip-gram word embedding model is in fact a linear decomposition of the cooccurrence matrix. This decomposition is unique up to a linear transformation. Therefore, given two word representations created from the same cooccurrence matrix, a linear transform can be devised to map words from the first to the second. Assuming that cooccurrence matrices for the source and target languages are sampled from the same language-independent cooccurrent matrix, one can find a linear transform for mapping source words to target words, up to an error component which represents sampling error. This assumption is realistic for comparable corpora, such as embeddings trained on wikipedia in various languages. In our experiments, we preferred to estimate word embeddings on Wikipedia rather than Twitter corpora because across languages, Tweets can cover different event from different countries, reducing the overlap.
> 
> However, word embeddings represent a mixture from the senses of each word, making the cross-language mapping non bijective (a word can have multiple translations), which will probably contribute to the residual. Therefore, it should be reasonable to train a linear transform to map words between the source and target languages. Note that a linear transform would conserve the translations associated to linguistic regularities observed in the vector spaces.
> 
> The idea is to translate words in another language in the goal to generate sentiment lexicon. In BIBREF7 , the authors propose to estimate a transformation matrix INLINEFORM0 such that INLINEFORM1 , where INLINEFORM2 is the embedding of a word in the source language and INLINEFORM3 is the embedding of its translation in

### Relevance

Label: 

## Record 0300

Paper: Building a robust sentiment lexicon with (almost) no resource

### Question

> Do they compare against manually-created lexicons?

### Passage

> Many methods have been proposed for extending polarity lexicons: propagate polarity along thesaurus relations BIBREF8 , BIBREF9 , BIBREF10 or use cooccurrence statistics to identify similar words BIBREF11 , BIBREF12 .
> 
> Porting lexicons to other languages has also been studied: use aligned thesauri and propagate at the sense level BIBREF13 , BIBREF14 , translate the lexicon directly BIBREF15 , BIBREF16 , take advantage of off-the-shelf translation and include sample word context to get better translations BIBREF17 or use crowd sourcing to quickly bootstrap lexicons in non-english languages BIBREF18 .

### Relevance

Label: 
