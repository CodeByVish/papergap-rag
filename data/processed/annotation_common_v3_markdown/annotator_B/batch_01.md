# Passage relevance annotation

Annotator: Changyan Xu

Enter your name or agreed identifier after `Annotator:`.

Judge whether each passage helps answer the question, including useful partial evidence. Topic overlap alone is insufficient.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Preserve all content and record numbers. Work independently; do not exchange labels before submission. Algorithm sources are disclosed.

## Question 0001

Paper: Performance Comparison of Crowdworkers and NLP Tools onNamed-Entity Recognition and Sentiment Analysis of Political Tweets

> What measures are used for evaluation?

### Common Retrieved Chunks

#### Passage 1

Retrieved by: BM25, Hybrid RRF

> As social media, specially Twitter, takes on an influential role in presidential elections in the U.S., natural language processing of political tweets BIBREF0 has the potential to help with nowcasting and forecasting of election results as well as identifying the main issues with a candidate – tasks of much interest to journalists, political scientists, and campaign organizers BIBREF1. As a methodology to obtain training data for a machine learning system that analyzes political tweets, BIBREF2 devised a crowdsourcing scheme with variable crowdworker numbers based on the difficulty of the annotation task. They provided a dataset of tweets where the sentiments towards political candidates were labeled both by experts in political communication and by crowdworkers who were likely not domain experts. BIBREF2 revealed that crowdworkers can match expert performance relatively accurately and in a budget-efficient manner. Given this result, the authors envisioned future work in which groundtruth labels would be crowdsourced for a large number of tweets and then used to design an automated NLP tool for political tweet analysis.
> 
> The question we address here is: How accurate are existing NLP tools for political tweet analysis? These tools would provide a baseline performance that any new machine learning system for political tweet analysis would compete against. We here explore whether existing NLP systems can answer the questions "What sentiment?" and "Towards whom?" accurately for the dataset of political tweets provided by BIBREF2. In our analysis, we include NLP tools with publicly-available APIs, even if the tools were not specifically designed for short texts like tweets, and, in particular, political tweets.
> 
> Our experiments reveal that the task of entity-level sentiment analysis is difficult for existing tools to answer accurately while the recognition of the entity, here, which politician, was easier.

#### Relevance 1

Label: 0

#### Passage 2

Retrieved by: BM25, Dense, Hybrid RRF

> We used the 1,000-tweet dataset by BIBREF2 that contains the named-entities labels and entity-level sentiments for each of the four 2016 presidential primary candidates Bernie Sanders, Donald Trump, Hillary Clinton, and Ted Cruz, provided by crowdworkers, and by experts in political communication, whose labels are considered groundtruth. The crowdworkers were located in the US and hired on the BIBREF22 platform. For the task of entity-level sentiment analysis, a 3-scale rating of "negative," "neutral," and "positive" was used by the annotators.
> 
> BIBREF2 proposed a decision tree approach for computing the number of crowdworkers who should analyze a tweet based on the difficulty of the task. Tweets are labeled by 2, 3, 5, or 7 workers based on the difficulty of the task and the level of disagreement between the crowdworkers. The model computes the number of workers based on how long a tweet is, the presence of a link in a tweet, and the number of present sarcasm signals. Sarcasm is often used in political tweets and causes disagreement between the crowdworkers. The tweets that are deemed to be sarcastic by the decision tree model, are expected to be more difficult to annotate, and hence are allocated more crowdworkers to work on.
> 
> We conducted two sets of experiments. In the first set, we used BIBREF23, BIBREF17, and BIBREF18, for entity-level sentiment analysis; in the second set, BIBREF17, BIBREF19, BIBREF24, BIBREF25, and BIBREF26, BIBREF18 for named-entity recognition.
> 
> In the experiments that we conducted with TwitterNLP for named-entity recognition, we worked with the default values of the model. Furthermore, we selected the 3-class Stanford NER model, which uses the classes “person,” “organization,” and “location” because it resulted in higher accuracy compared to the 7-class model. For CogComp-NLP NER we used Ontonotes 5.0 NER model BIBREF27. For spaCy NER we used the `en_core_web_lg' model.
> 
> We report the experimental results for our two tasks in terms of the correct classification rate (CCR). For sentiment analysis, we have a three-class problem (positive, negative, and neutral), where the classes are mutually exclusive. The CCR, averaged for a set of tweets, is defined to be the number of correctly-predicted sentiments over the number of groundtruth sentiments in these tweets. For NER, we consider

#### Relevance 2

Label: 1

#### Passage 3

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> NLP toolkits typically have the following capabilities: tokenization, part-of-speech (PoS) tagging, chunking, named entity recognition and sentiment analysis. In a study by BIBREF3, it is shown that the well-known NLP toolkits NLTK BIBREF4, Stanford CoreNLP BIBREF5, and TwitterNLP BIBREF6 have tokenization, PoS tagging and NER modules in their pipelines. There are two main approaches for NER: (1) rule-based and (2) statistical or machine learning based. The most ubiquitous algorithms for sequence tagging use Hidden Markov Models BIBREF7, Maximum Entropy Markov Models BIBREF7, BIBREF8, or Conditional Random Fields BIBREF9. Recent works BIBREF10, BIBREF11 have used recurrent neural networks with attention modules for NER.
> 
> Sentiment detection tools like SentiStrength BIBREF12 and TensiStrength BIBREF13 are rule-based tools, relying on various dictionaries of emoticons, slangs, idioms, and ironic phrases, and set of rules that can detect the sentiment of a sentence overall or a targeted sentiment. Given a list of keywords, TensiStrength (similar to SentiStrength) reports the sentiment towards selected entities in a sentence, based on five levels of relaxation and five levels of stress.
> 
> Among commercial NLP toolkits (e.g., BIBREF14, BIBREF15, BIBREF16), we selected BIBREF17 and BIBREF18 for our experiments, which, to the best of our knowledge, are the only publicly accessible commercial APIs for the task of entity-level sentiment analysis that is agnostic to the text domain. We also report results of TensiStrength BIBREF13, TwitterNLP BIBREF6, BIBREF19, CogComp-NLP BIBREF20, and Stanford NLP NER BIBREF21.

#### Relevance 3

Label: 0

#### Passage 4

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> Partial support of this work by the Hariri Institute for Computing and Computational Science & Engineering at Boston University (to L.G.) and a Google Faculty Research Award (to M.B. and L.G.) is gratefully acknowledged. Additionally, we would like to thank Daniel Khashabi for his help in running the CogComp-NLP Python API and Mike Thelwal for his help with TensiStrength. We are also grateful to the Stanford NLP group for clarifying some of the questions we had with regards to the Stanford NER tool.

#### Relevance 4

Label: 0

#### Passage 5

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> (positive, negative, and neutral), where the classes are mutually exclusive. The CCR, averaged for a set of tweets, is defined to be the number of correctly-predicted sentiments over the number of groundtruth sentiments in these tweets. For NER, we consider that each tweet may reference up to four candidates, i.e., targeted entities. The CCR, averaged for a set of tweets, is the number of correctly predicted entities (candidates) over the number of groundtruth entities (candidates) in this set.

#### Relevance 5

Label: 1

#### Passage 6

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The dataset of 1,000 randomly selected tweets contains more than twice as many tweets about Trump than about the other candidates. In the named-entity recognition experiment, the average CCR of crowdworkers was 98.6%, while the CCR of the automated systems ranged from 77.2% to 96.7%. For four of the automated systems, detecting the entity Trump was more difficult than the other entities (e.g., spaCy 72.7% for the entity Trump vs. above 91% for the other entities). An example of incorrect NER is shown in Figure FIGREF1 top. The difficulties the automated tools had in NER may be explained by the fact that the tools were not trained on tweets, except for TwitterNLP, which was not in active development when the data was created BIBREF1.
> 
> In the sentiment analysis experiments, we found that a tweet may contain multiple sentiments. The groundtruth labels contain 210 positive sentiments, 521 neutral sentiments, and 305 negative sentiments to the candidates. We measured the CCR, across all tweets, to be 31.7% for Rosette Text Analytics, 43.2% for Google Cloud, 44.2% for TensiStrength, and 74.7% for the crowdworkers. This means the difference between the performance of the tools and the crowdworkers is significant – more than 30 percent points.
> 
> Crowdworkers correctly identified 62% of the neutral, 85% of the positive, and 92% of the negative sentiments. Google Cloud correctly identified 88% of the neutral sentiments, but only 3% of the positive, and 19% of the negative sentiments. TensiStrength correctly identified 87.2% of the neutral sentiments, but 10.5% of the positive, and 8.1% of the negative sentiments. Rosette Text Analytics correctly identified 22.7% of neutral sentiments, 38.1% of negative sentiments and 40.9% of positive sentiments. The lowest and highest CCR pertains to tweets about Trump and Sanders for both Google Cloud and TensiStrength, Trump and Clinton for Rosette Text Analytics, and Clinton and Cruz for crowdworkers. An example of incorrect ELS analysis is shown in Figure FIGREF1 bottom.

#### Relevance 6

Label: 1

#### Passage 7

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> Our results show that existing NLP systems cannot accurately perform sentiment analysis of political tweets in the dataset we experimented with. Labeling by humans, even non-expert crowdworkers, yields accuracy results that are well above the results of existing automated NLP systems. In future work we will therefore use a crowdworker-labeled dataset to train a new machine-learning based NLP system for tweet analysis. We will ensure that the training data is balanced among classes. Our plan is to use state-of-the-art deep neural networks and compare their performance for entity-level sentiment analysis of political tweets.

#### Relevance 7

Label: 0

### BM25

None

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0002

Paper: Author Profiling for Hate Speech Detection

> What community-based profiling features are used?

### Common Retrieved Chunks

#### Passage 8

Retrieved by: BM25, Dense, Hybrid RRF

> We conduct a qualitative analysis of system errors and the cases where author profiling leads to the correct classification of previously misclassified examples. Table 3 shows examples of hateful tweets from the dataset that are misclassified by the lr method, but are correctly classified upon the addition of author profiling features, i.e., by the lr + auth method. It is worth noting that some of the wins scored by the latter are on tweets that are part of a larger hateful discourse or contain links to hateful content while not explicitly having textual cues that are indicative of hate speech per se. The addition of author profiling features may then be viewed as a proxy for wider discourse information, thus allowing us to correctly resolve the cases where lexical and semantic features alone are insufficient.
> 
> However, a number of hateful tweets still remain misclassified despite the addition of author profiling features. According to our analysis, many of these tend to contain urls to hateful content, e.g., “@salmonfarmer1: Logic in the world of Islam http://t.co/6nALv2HPc3" and “@juliarforster Yes. http://t.co/ixbt0uc7HN". Since Twitter shortens all urls into a standard format, there is no indication of what they refer to. One way to deal with this limitation could be to additionally maintain a blacklist of links. Another source of system errors is the deliberate obfuscation of words by authors in order to evade detection, e.g., “Kat, a massive c*nt. The biggest ever on #mkr #cuntandandre". Current hate speech detection methods, including ours, do not directly attempt to address this issue. While this is a challenge for bag-of-word based methods such as lr, we hypothesize that neural networks operating at the character level may be helpful in recognizing obfuscated words.
> 
> We further conducted an analysis of the author embeddings generated by node2vec, in order to validate that they capture the relevant aspects of the community graph. We visualized the author embeddings in 2-dimensional space using t-sne BIBREF24 , as shown in Figure 2 . We observe that, as in the community graph, there are a few densely populated regions in the visualization that represent authors in closely knit groups who exhibit similar characteristics. The other regions are largely sparse with

#### Relevance 8

Label: 1

#### Passage 9

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> the ones that do not get tuned lie closely clustered around the oov token, to which unseen words in the test set are mapped.
> 
> Word-sum (ws). As a third baseline, we adopt the “lstm+glove+gbdt" method of Badjatiya et al. Badjatiya:17, which achieves state-of-the-art results on the Twitter dataset we are using. The authors first utilize an lstm to task-tune glove-initialized word embeddings by propagating the error back from an lr layer. They then train a gradient boosted decision tree (gbdt) classifier to classify texts based on the average of the embeddings of constituent words. We make two minor modifications to this method: we use a 2-layer gru instead of the lstm to tune the embeddings, and we train the gbdt classifier on the l $_2$ -normalized sum of the embeddings instead of their average. Although the authors achieved state-of-the-art results on Twitter by initializing embeddings randomly rather than with glove (which is what we do here), we found the opposite when performing a 10-fold stratified cross-validation (cv). A possible explanation of this lies in the authors' decision to not use stratification, which for such a highly imbalanced dataset can lead to unexpected outcomes BIBREF18 . Furthermore, the authors train their lstm on the entire dataset (including the test set) without any early stopping criterion, which leads to over-fitting of the randomly-initialized embeddings.
> 
> Author profile (auth). In order to test whether community-based information of authors is in itself sufficient to correctly classify the content produced by them, we utilize just the author profiles we generated to train a gbdt classifier.
> 
> Char n-grams + author profile (lr + auth). This method builds upon the lr baseline by appending author profile vectors on to the character n-gram count vectors for training the lr classifier.
> 
> Hidden-state + author profile (hs + auth) and Word-sum + author profile (ws + auth). These methods are identical to the char n-grams + author profile method except that here we append the author profiling features on to features derived from the hidden-state and word-sum baselines respectively and feed them to a gbdt classifier.

#### Relevance 9

Label: 0

#### Passage 10

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> helpful indicator. However, Waseem and Hovy focused only on coarse demographic features of the users, disregarding information about their communication with others. But previous research suggests that users who subscribe to particular stereotypes that promote hate speech tend to form communities online. For example, Zook zook mapped the locations of racist tweets in response to President Obama's re-election to show that such tweets were not uniformly distributed across the United States but formed clusters instead. In this paper, we present the first approach to hate speech detection that leverages author profiling information based on properties of the authors' social network and investigate its effectiveness.
> 
> Author profiling has emerged as a powerful tool for NLP applications, leading to substantial performance improvements in several downstream tasks, such as text classification, sentiment analysis and author attribute identification BIBREF8 , BIBREF9 , BIBREF10 . The relevance of information gained from it is best explained by the idea of homophily, i.e., the phenomenon that people, both in real life as well as on the Internet, tend to associate more with those who appear similar. Here, similarity can be defined along various axes, e.g., location, age, language, etc. The strength of author profiling lies in that if we have information about members of a community $c$ defined by some similarity criterion, and we know that the person $p$ belongs to $c$ , we can infer information about $p$ . This concept has a straightforward application to our task: knowing that members of a particular community are prone to creating hateful content, and knowing that the author p is connected to this community, we can leverage information beyond linguistic cues and more accurately predict the use of hateful/non-hateful language from $p$ . The questions that we seek to address here are: are some authors, and the respective communities that they belong to, more hateful than the others? And can such information be effectively utilized to improve the performance of automated hate speech detection methods?
> 
> In this paper, we answer these questions and develop novel methods that take into account community-based profiling features of authors when examining their tweets for hate speech. Experimenting with a dataset of $16k$ tweets, we show that the

#### Relevance 10

Label: 0

#### Passage 11

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We perform 10-fold stratified cross validation (cv), as suggested by Forman and Scholz Forman:10, to evaluate all seven methods described in the previous section. Following previous research BIBREF7 , BIBREF23 , we report the average weighted precision, recall, and f $_1$ scores for all the methods. The average weighted precision is calculated as:
> 
> $$\nonumber \frac{\sum _{i=1}^{10}\; (w_r\cdot \textrm {P}_r^i + w_s\cdot \textrm {P}_s^i + w_n\cdot \textrm {P}_n^i)}{10}$$   (Eq. 16)
> 
> where $\textrm {P}_r^i, \textrm {P}_s^i, \textrm {P}_n^i$ are precision scores on the racism, sexism, and none classes from the $i^{th}$ fold of the cv. The values $w_r$ , $w_s$ , and $w_n$ are the proportions of the racism, sexism, and none classes in the dataset respectively; since we use stratification, these proportions are constant ( $w_r=0.12$ , $w_s=0.19$ , $w_n=0.69$ ) across all folds. Average weighted recall and f $_1$ are calculated in the same manner.
> 
> The results are presented in Table 1 . For all three baseline methods (lr, ws, and hs), the addition of author profiling features significantly improves performance ( $p < 0.05$ under 10-fold cv paired t-test). The lr + auth method yields the highest performance of f $_1$ $=87.57$ , exceeding its respective baseline by nearly 4 points. A similar trend can be observed for the other methods as well. These results point to the importance of community-based information and author profiling in hate speech detection and demonstrate that our approach can further improve the performance of existing state-of-the-art methods.
> 
> In Table 2 , we further compare the performance of the different methods on the racism and sexism classes individually. As in the previous experiments, the scores are averaged over 10 folds of cv. Of particular interest are the scores for the sexism class where the f $_1$ increases by over 10 points upon the addition of author profiling features. Upon analysis, we find that such a substantial increase in performance stems from the fact that many of the 527 unique authors of the sexist tweets are closely connected in the community graph. This allows for their penchant for sexism to be expressed in their respective author profiles.
> 
> The author profiling features on their own (auth) achieve impressive results overall and

#### Relevance 11

Label: 0

#### Passage 12

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> authors of the sexist tweets are closely connected in the community graph. This allows for their penchant for sexism to be expressed in their respective author profiles.
> 
> The author profiling features on their own (auth) achieve impressive results overall and in particular on the sexism class, where their performance is typical of a community-based generalization, i.e., low precision but high recall. For the racism class on the other hand, the performance of auth on its own is quite poor. This contrast can be explained by the fact that tweets in the racism class come from only 5 unique authors who: (i) are isolated in the community graph, or (ii) have also authored several tweets in the sexism class, or (iii) are densely connected to authors from the sexism and none classes which possibly camouflages their racist nature.
> 
> We believe that the gains in performance will be more pronounced as the underlying community graph grows since there will be less solitary authors and more edges worth harnessing information from. Even when the data is skewed and there is an imbalance of hateful vs. non-hateful authors, we do expect our approach to still be able to identify clusters of authors with similar views.

#### Relevance 12

Label: 0

#### Passage 13

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> detection methods?
> 
> In this paper, we answer these questions and develop novel methods that take into account community-based profiling features of authors when examining their tweets for hate speech. Experimenting with a dataset of $16k$ tweets, we show that the addition of such profiling features to the current state-of-the-art methods for hate speech detection significantly enhances their performance. We also release our code (including code that replicates previous work), pre-trained models and the resources we used in the public domain.

#### Relevance 13

Label: 0

#### Passage 14

Retrieved by: Dense, Hybrid RRF

> In this paper, we explored the effectiveness of community-based information about authors for the purpose of identifying hate speech. Working with a dataset of $16k$ tweets annotated for racism and sexism, we first comprehensively replicated three established and currently best-performing hate speech detection methods based on character n-grams and recurrent neural networks as our baselines. We then constructed a graph of all the authors of tweets in our dataset and extracted community-based information in the form of dense low-dimensional embeddings for each of them using node2vec. We showed that the inclusion of author embeddings significantly improves system performance over the baselines and advances the state of the art in this task. Users prone to hate speech do tend to form social groups online, and this stresses the importance of utilizing community-based information for automatic hate speech detection. In the future, we wish to explore the effectiveness of community-based author profiling in other tasks such as stereotype identification and metaphor detection.

#### Relevance 14

Label: 1

### BM25

None

### Dense

#### Passage 15

Retrieved by: Dense

> Author profiling has been leveraged in several ways for a variety of purposes in nlp. For instance, many studies have relied on demographic information of the authors. Amongst these are Hovy et al. hovy2015demographic and Ebrahimi et al. ebrahimi2016personalized who extracted age and gender-related information to achieve superior performance in a text classification task. Pavalanathan and Eisenstein pavalanathan2015confounds, in their work, further showed the relevance of the same information to automatic text-based geo-location. Researching along the same lines, Johannsen et al. johannsen2015cross and Mirkin et al. mirkin2015motivating utilized demographic factors to improve syntactic parsing and machine translation respectively.
> 
> While demographic information has proved to be relevant for a number of tasks, it presents a significant drawback: since this information is not always available for all authors in a social network, it is not particularly reliable. Consequently, of late, a new line of research has focused on creating representations of users in a social network by leveraging the information derived from the connections that they have with other users. In this case, node representations (where nodes represent the authors in the social network) are typically induced using neural architectures. Given the graph representing the social network, such methods create low-dimensional representations for each node, which are optimized to predict the nodes close to it in the network. This approach has the advantage of overcoming the absence of information that the previous approaches face. Among those that implement this idea are Yang et al. yang2016toward, who used representations derived from a social graph to achieve better performance in entity linking tasks, and Chen and Ku chen2016utcnn, who used them for stance classification.
> 
> A considerable amount of literature has also been devoted to sentiment analysis with representations built from demographic factors BIBREF10 , BIBREF12 . Other tasks that have benefited from social representations are sarcasm detection BIBREF13 and political opinion prediction BIBREF14 .

#### Relevance 15

Label: 0

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0003

Paper: WikiRank: Improving Keyphrase Extraction Based on Background Knowledge

> what are the state of the art models?

### Common Retrieved Chunks

#### Passage 16

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Figure shows part of an example document. In this figure, the gold keyphrases are marked with bold, and the keyphrases extracted by the TextRank system are marked with parentheses. We are going to illustrate the errors exist in most of present keyphrase extraction systems using this example. Overgeneration errors occur when a system correctly predicts a candidate as a keyphrase because it contains a word that frequently appears in the associated document, but at the same time erroneously outputs other candidates as keyphrases because they contain the same word BIBREF0 . It is not easy to reject a non-keyphrase containing a word with a high term frequency: many unsupervised systems score a candidate by summing the score of each of its component words, and many supervised systems use unigrams as features to represent a candidate. To be more concrete, consider the news article in Figure . The word Cattle has a significant presence in the document. Consequently, the system not only correctly predict British cattle as a keyphrase, but also erroneously predict cattle industry, cattle feed, and cattle brain as keyphrases, yielding overgeneration errors.
> 
> Redundancy errors occur when a system correctly identifies a candidate as a keyphrase, but at the same time outputs a semantically equivalent candidate (e.g., its alias) as a keyphrase. This type of error can be attributed to the failure of a system to determine that two candidates are semantically equivalent. Nevertheless, some researchers may argue that a system should not be penalized for redundancy errors because the extracted candidates are in fact keyphrases. In our example, bovine spongiform encephalopathy and bse refer to the same concept. If a system predicts both of them as keyphrases, it commits a redundancy error.
> 
> Infrequency errors occur when a system fails to identify a keyphrase owing to its infrequent presence in the associated document. Handling infrequency errors is a challenge because state-of-the-art keyphrase extractors rarely predict candidates that appear only once or twice in a document. In the Mad cow disease example, the keyphrase extractor fails to identify export and scrapie as keyphrases, resulting in infrequency errors.

#### Relevance 16

Label: 1

#### Passage 17

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> As the amount of published material rapidly increases, the problem of managing information becomes more difficult. Keyphrase, as a concise representation of the main idea of the text, facilitates the management, categorization, and retrieval of information. Automatic keyphrase extraction concerns “the automatic selection of important and topical phrases from the body of a document”. Its goal is to extract a set of phrases that are related to the main topics discussed in a given document BIBREF0 .
> 
> Existing methods of keyphrase extraction could be divided into two categories: supervised and unsupervised. While supervised approaches require human labeling, at the same time needs various kinds of training data to get better generalization performance, more and more researchers focus on unsupervised methods.
> 
> Traditional methods of unsupervised keyphrase extraction mostly focus on getting information of document from word frequency and document structure BIBREF0 , however, after years of attempting, the performance seems very hard to be improved any more. Based on this observation, it is reasonable to suspect that the document itself possibly cannot provide enough information for keyphrase extraction task.
> 
> To get good coverage of the main topics of the document, Topical PageRank BIBREF1 started to adopt topical information in automatic keyphrase extraction. The main idea of Topical PageRank is to extract the top topics of the document using LDA, then sum over the scores of a candidate phrase under each topic to be the final score. The main problems with Topical PageRank are: First, The topics are too general. Second, since they are using LDA, they only classify the words to several topics, but don't know what the topics exactly are. However, the topical information we need for keyphrase extraction should be precise. As shown in Figure , the difference between a correct keyphrase sheep disease and an incorrect keyphrase incurable disease could be small, which is hard to be captured by rough topical categorization approach.
> 
> To overcome the limitations of aforementioned approaches, we propose WikiRank, an unsupervised automatic keyphrase extraction approach that links semantic meaning to text
> 
> The key contribution of this paper could be summarized as follows:

#### Relevance 17

Label: 0

#### Passage 18

Retrieved by: BM25, Dense, Hybrid RRF

> This is one of the crucial steps in our paper that connects the plain text with human knowledge, facilitating the understanding of semantics. In this step, we adopt TAGME BIBREF2 to obtain the underlying concepts in documents.
> 
> TAGME is a powerful topic annotator. It identifies meaningful sequences of words in a short text and link them to a pertinent Wikipedia page, as shown in Figure . These links add a new topical dimension to the text that enable us to relate, classify or cluster short texts.
> 
> This step is to filter out unnecessary word tokens from the input document and generate a list of potential keywords using heuristics. As reported in BIBREF3 , most manually assigned keyphrases turn out to be noun groups. We follow BIBREF4 and select candidates lexical unit with the following Penn Treebank tags: NN, NNS, NNP, NNPS, and JJ, which are obtained using the Stanford POS tagger BIBREF5 , and then extract the noun groups whose pattern is zero or more adjectives followed by one or more nouns. The pattern can be represented using regular expressions as follows INLINEFORM0
> 
> where JJ indicates adjectives and various forms of nouns are represented using NN, NNS and NNP .
> 
> We build a semantic graph INLINEFORM0 in which the set of vertices INLINEFORM1 is the union of the concept set INLINEFORM2 and the candidate keyphrase set INLINEFORM3 —i.e., INLINEFORM4 . In the graph, each unique concept INLINEFORM5 or candidate keyphrase INLINEFORM6 for document INLINEFORM7 corresponds to a node. The node corresponds to a concept INLINEFORM8 and the node corresponds to a candidate keyphrase INLINEFORM9 are connected by an edge INLINEFORM10 , if the candidate keyphrase INLINEFORM11 contains concept INLINEFORM12 according to the annotation of TAGME. Part of the semantic graph of the sample document is shown in Figure . Concepts corresponding to are shown in Table .

#### Relevance 18

Label: 0

#### Passage 19

Retrieved by: BM25, Hybrid RRF

> In practice, computing score for all the candidate keyphrases is not always necessary, because some of the candidates are very unlikely to be gold keyphrase that we can remove them from our graph before applying the algorithm to reduce the complexity.
> 
> In this section, we introduce three heuristic pruning steps that significantly reduces the complexity of the optimization problem without reducing much of the accuracy.
> 
> Step 1. Remove the candidate keyphrase INLINEFORM0 from original graph INLINEFORM1 , if it is not connected to any concept.
> 
> The intuition behind this heuristic is straightforward. Since our objective function is constructed over concepts, if a candidate keyphrase INLINEFORM0 doesn't contain any concept, adding it to INLINEFORM1 doesn't bring any improvement to the objective function, so INLINEFORM2 is irrelevant to our optimization process. Pruning INLINEFORM3 would be a wise decision.
> 
> Step 2. Remove the candidate keyphrase INLINEFORM0 from original graph INLINEFORM1 , if it is only connected to one concept that only exists once in the document
> 
> If a candidate keyphrase contains fewer concepts, or the concepts connects to it barely exist in the document, we think this candidate keyphrase contributes less valuable information to the document. In practice, there are numerous INLINEFORM0 pairs in graph INLINEFORM1 that is isolated from the center of the graph. We believe they are irrelevant to the major topic of the document.
> 
> Step 3. For a concept INLINEFORM0 connecting to more than INLINEFORM1 candidate keyphrases, remove any candidate keyphrase INLINEFORM2 which (1)Does not connect to any other concept. AND (2)The ranking is lower than INLINEFORM3 th among all candidate keyphrases connect to INLINEFORM4 .(In practice, INLINEFORM5 is usually 3 or 4.)
> 
> According to equation EQREF10 , if there are already INLINEFORM0 instances of concept INLINEFORM1 in the INLINEFORM2 , adding the INLINEFORM3 th instance of INLINEFORM4 will only contribute INLINEFORM5 to INLINEFORM6 . At the same time, among all the candidate keyphrases connected to concept INLINEFORM7 , our optimization process always chooses the ones that connect to other concepts as well over the ones that do not connect to any other concept. Combining these two logic, a candidate satisfying the constrains of Step 3 is not likely to be picked in the best

#### Relevance 19

Label: 1

#### Passage 20

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The DUC-2001 dataset BIBREF6 , which is a collection of 308 news articles, is annotated by BIBREF7 .
> 
> The Inspec dataset is a collection of 2,000 abstracts from journal papers including the paper title. This is a relatively popular dataset for automatic keyphrase extraction, as it was first used by BIBREF3 and later by Mihalcea and BIBREF8 and BIBREF9 .
> 
> The NUS Keyphrase Corpus BIBREF10 includes 211 scientific conference papers with lengths between 4 to 12 pages. Each paper has one or more sets of keyphrases assigned by its authors and other annotators. The number of candidate keyphrases that can be extracted is potentially large, making this corpus the most challenging of the four.
> 
> Finally, the ICSI Meeting Corpus (Janin et al., 2003), which is annotated by Liu et al. (2009a), includes 161 meeting transcriptions. Unlike the other three datasets, the gold standard keys for the ICSI corpus are mostly unigrams.

#### Relevance 20

Label: 0

#### Passage 22

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The WikiRank algorithm includes three steps: (1) Construct the semantic graph including concepts and candidate keyphrases; (2)(optional) Prune the graph with heuristic to filter out candidates which are likely to be erroneously produced; (3) Generate the best set of keyphrases as output.

#### Relevance 22

Label: 0

### BM25

None

### Dense

#### Passage 21

Retrieved by: Dense

> For comparing with our system, we reimplemented SingleRank and Topical PageRank. Table shows the result of our reimplementation of SingleRank and Topical PageRank, as well as the result of our system. Note that we predict the same number of phrase ( INLINEFORM0 ) for each document while testing all three methods.
> 
> The result shows our result has guaranteed improvement over SingleRank and Topical PageRank on all four corpora.

#### Relevance 21

Label: 1

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 23

Retrieved by: Hybrid RRF followed by BGE reranking

> ones that connect to other concepts as well over the ones that do not connect to any other concept. Combining these two logic, a candidate satisfying the constrains of Step 3 is not likely to be picked in the best keyphrase set INLINEFORM8 , so we can prune it before the optimalization process.

#### Relevance 23

Label: 0

## Question 0004

Paper: Improved English to Russian Translation by Neural Suffix Prediction

> what is the previous work they are comparing to?

### Common Retrieved Chunks

#### Passage 24

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Previous work considered morphological information for both SMT and NMT. BIBREF8 ( BIBREF8 ) proposed an effective way to integrate word-level annotation in SMT, which can be morphological, syntactic, or semantic. Morphological information can be utilized not only on source side, but also the target side. Although these annotation can help to improve the translation procedure, data sparsity still exists. BIBREF9 ( BIBREF9 ) decompose the process of translating a word into two steps. Firstly a stem is produced, then a feature-rich discriminative model selects an appropriate inflection for the stem. Target-side morphological features and source-side context features are utilized in their inflection prediction model.
> 
> BIBREF10 ( BIBREF10 ) use distributed representations for words and soft morphological tags in their neural inflection model, which can effectively reduce lexical sparsity, leading to less morphological ambiguity. This is the first try of modeling inflection through a neural method, integrated in a SMT architecture.
> 
> For NMT, BIBREF11 ( BIBREF11 ) make use of various source side features (such as morphological features, part-of-speech tags, and syntactic dependency labels) to enhance encoding in NMT. This is the first time morphological information is leveraged in NMT architecture. Target-side morphology is not considered in their work. BIBREF12 ( BIBREF12 ) predict a sequence of interleaving morphological tags and lemmas, followed by a morphological generator. They used a external model to synthesize words given tags and lemmas. Our method is the first to explicitly consider the generation of morphological suffixes within a neural translation model. Our work is motivated by a line of work that generates morphology during text generation ( BIBREF13 , BIBREF13 ; BIBREF14 , BIBREF14 ; BIBREF10 , BIBREF10 ).

#### Relevance 24

Label: 1

#### Passage 26

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> predicted. Two types of target side sequences are used during training, namely stem sequence and suffix sequence, which are extracted from the original target side word sequence, as shown in Figure FIGREF1 . Sparsity is relieved since the number of stem types is much smaller than word types, and suffix types can be as small as several hundreds. Another advantage of this structure is that during the prediction of suffix, the previously generated stem sequence can be considered, which can further improve the accuracy of suffix prediction.
> 
> We empirically study this method and compare it with previous work on reducing OOV rates ( BIBREF3 , BIBREF3 ; BIBREF4 , BIBREF4 ). Results show that our method gives significant improvement on the English to Russian translation task on two different domains and two popular NMT architectures. We also verify our method on training data consisting of 50M bilingual sentences, which proves that this method works effectively on large-scale corpora.

#### Relevance 26

Label: 1

#### Passage 29

Retrieved by: Dense, Hybrid RRF

> We use BLEU BIBREF26 as our evaluation metric. The performance of different systems are shown in Table TABREF34 and TABREF35 . On both the news and e-commerce domains, our system performs better than baseline systems.
> 
> On news domain, the average improvement of our method is 1.75 and 0.97 BLEU score when implemented on RNN-based NMT, compared with subword BIBREF3 method and fully character-based BIBREF4 method, respectively. When implemented on Transformer BIBREF15 , average improvement is 1.47 BLEU compared with subword method. On the e-commerce domain, which use 50M sentences as training corpus, the average improvement of our method is 0.68 BLEU compared with the subword method.
> 
> We evaluate stem accuracies and suffix accuracies separately. For stem, we use BLEU as evaluation metric, Table TABREF34 shows stem BLEU of different methods on “News2014” test set, our method can gain significant improvement compared with baselines, since our method can reduce data sparsity better than baselines. Our method can effectively reduce suffix error, Figure FIGREF43 gives some examples both on e-commerce and news domains:
> 
> For the first sample, the suffix of the translation words (tagged by 1 and 2) from two different baseline systems means a reflexive verb, whose direct object is the same as its subject. In other words, a reflexive verb has the same semantic agent and patient. It is an incorrect translation according to the source meaning, because we can infer from the source sentence that the agent is a person and the patient is an object (some goods bought by a customer). In our system, the suffix of the translation word (tagged by 3) is correct. It represents an infinitive verb which may take objects, other complements and modifiers to form a verb phrase.
> 
> In the second sample, the translation word (tagged by 1) is not accurate, its suffix represents a plural form, but the correct form is singular, because the corresponding source word “positive” is singular form. Character-based system can correctly translate source word “stars” into a Russian word with plural form. However, the translation of “positive” (tagged by 2) is still with wrong form. Both the translation of “positive” and “stars” from our system are with the correct forms.
> 
> In the third

#### Relevance 29

Label: 1

#### Passage 30

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> News We select 5.3M sentences from the bilingual training corpus released by WMT2017 shared task on the news translation domain as our training data. We use 3 test set, which are published by WMT2017 news translation task, namely “News2014”, “News2015”, “News2016”.
> 
> E-commerce We collect 50M bilingual sentences as our training corpus:
> 
> 10M sentences are crawled and automatic aligned from some international brand's English and Russian websites.
> 
> 20M are back translated corpus: First we crawled the Russian sentences from websites of certain Russian's Brands. Then translated them to English through a machine translation system trained on limited RU-EN corpus BIBREF24 .
> 
> The last 20M bilingual sentences are crawled from the web, and are not domain specific.
> 
> We typically use the following 3 types of data as test set, which are named title, description and comment, these sentences are all extracted from e-commerce websites. Title are the goods' titles showed on a listing page when some buyers type in some keywords in a searching bar under an e-commerce website. Description refers to the information in a commodities' detail page. Comment include the review or feedback from some buyers. Example sentences are shown in Table TABREF33 . For each kind of test set, we randomly select 1K English sentences and translate it by human.
> 
> Pre-Processing Both the training set and the test set are lowercased, and some entity words appeared in the data are generalized into specific symbols, such as “_date_”, “_time_”, “_number_”. When selecting our training data, we keep the sentences which has length between 1 to 30. We use a bilingual sentence scorer to discard some low-quality bilingual sentences. The scorer is simply trained under algorithm of IBM Model 1 BIBREF25 on a very large bilingual corpus.
> 
> Target Side Word Stemming We use snowball to create stems from words. Because stem created from snowball is always a substring of the original word, we can obtain suffixes by simply applying a string cut operation. By applying snowball to a target side word sequence, we split a target side sentence into a stem sequence and a suffix sequence. The stemming accuracy of snowball is 83.3% on our human labeled test set.
> 
> Applying BPE to Target Side Stem Sequence

#### Relevance 30

Label: 0

#### Passage 31

Retrieved by: Dense, Hybrid RRF

> Our RNN and Transformer baseline systems utilize BPE BIBREF3 to transfer the original word sequence to subword sequence on both the source and the target sides, since the subword method had a stable improvement compared with word based system, especially on morphologically rich languages.
> 
> Besides, we compared our system with a fully character-based baseline system, which is an implementation of BIBREF4 ( BIBREF4 )'s work, and is available on github.
> 
> We limit the source and target vocabularies to the most frequent 30K tokens for both English and Russian. For news domain, about 99.7% tokens are covered by the source side vocabulary, about 97.0% target tokens are covered by the target side vocabulary.

#### Relevance 31

Label: 1

### BM25

#### Passage 25

Retrieved by: BM25

> used in training time.
> 
> Transformer BIBREF15 is a recently proposed model for sequence to sequence tasks. It discards the RNN structure for building the encoder and decoder blocks. Instead, only the attention mechanism is used to calculate the source and target hidden states.
> 
> The encoder is composed of stacked neural layers. In particularly, for the time step INLINEFORM0 in layer INLINEFORM1 , the hidden state INLINEFORM2 is calculated as follows: First, a self-attention sub-layer is employed to encode the context. For this end, the hidden states in the previous layer are projected into a tuple of queries( INLINEFORM3 ), keys( INLINEFORM4 ) and values( INLINEFORM5 ), where INLINEFORM6 in the following function denotes a feed forward layer: DISPLAYFORM0
> 
> Then attention weights are computed as scaled dot product between current query and all keys, normalized with a softmax function. After that, the context vector is represented as weighted sum of the values projected from hidden states in the previous layer. The hidden state in the previous layer and the context vector are then connected by residual connection, followed by a layer normalization function BIBREF21 , to produce a candidate hidden state INLINEFORM0 . Finally, another sub-layer including a feed forward layer, followed by another residual connection and layer normalization, are used to obtain the hidden state INLINEFORM1 : DISPLAYFORM0
> 
> The decoder is also composed of stacked layers. The hidden states are calculated in a similar way, except for the following two differences: First, only those target positions before the current one are used to calculate the target side self-attention. Second, attention is applied in both target-to-target and target-to-source. The target-to-source attention sub-layer is inserted between the target self-attention sub-layer and the feed-forward sub-layer. Different from self-attention, the queries( INLINEFORM0 ) are projected from target hidden states in the previous layer, and the keys( INLINEFORM1 ) and values( INLINEFORM2 ) are projected from the source hidden states in the last layer.
> 
> The rest of the calculation is exactly the same with self-attention. Compared to RNN based sequence to sequence models, transformer allows significantly more parallelization, since all the hidden states in the same layer can be calculated simultaneously, whereas the hidden states in RNN can only be

#### Relevance 25

Label: 0

#### Passage 27

Retrieved by: BM25

> We proposed a simple but effective method to improve English-Russian NMT, for which a morphologically rich language is on the target side. We take a two-step approach in the decoder. At each step, a stem is first generated, then its suffix is generated. We empirically compared our method with two previous methods (namely subword and fully character-based), which can also to some extent address our problem. Our method gives an improvement on two encoder-decoder NMT architectures on two domains. To our knowledge, we are the first to explicitly model suffix for morphologically-rich target translation.

#### Relevance 27

Label: 1

#### Passage 28

Retrieved by: BM25

> Morphology Russian has rich morphology, which includes number (singular or plural), case (nominative, accusative etc.), gender (feminine, masculine or neuter) and tense mood. Figure FIGREF2 shows one example for Russian. A noun word “ball” is always masculine, but the suffix differs when the case and number changes, resulting in 10 different forms. Some other nouns can be feminine or neuter, and their adjectives will agree with them. Both adjectives and verbs have different forms according to their case, tense mood and the form of words they modify. Such morphological changes bring a challenge to machine translation task.
> 
> Stemming A Russian word can be split into two parts, namely the stem and the suffix. Suffix contains morphological information of a Russian word, including gender, number and case etc. In this paper, we use a deterministic rule-based stemmer to obtain stem and suffix for a Russian word. The process of stemming is shown in Figure FIGREF1 .

#### Relevance 28

Label: 0

### Dense

#### Passage 32

Retrieved by: Dense

> word “stars” into a Russian word with plural form. However, the translation of “positive” (tagged by 2) is still with wrong form. Both the translation of “positive” and “stars” from our system are with the correct forms.
> 
> In the third sample, the translation word tagged by 3 represents past tense; However, the translation words tagged by 1 and 2 represent present tense. Our system successfully predicted the tense moods.

#### Relevance 32

Label: 0

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 33

Retrieved by: Hybrid RRF followed by BGE reranking

> Subword based BIBREF3 and character-based ( BIBREF4 , BIBREF4 ; BIBREF5 , BIBREF5 ) NMT are the two directions of adjusting translation granularity, which can be helpful to our problem.
> 
> In BIBREF3 ( BIBREF3 )'s work, commonly appearing words remain unchanged, while others are segmented into several subword units, which are from a fixed set. Both source and target side sentences can be changed into subword sequences. More specifically, some rare words are split into and represent as some more frequent units, base on a data compression technique, namely Byte Pair Encoding (BPE). The vocabulary built on common words and these frequent subword units can successfully improve the coverage of training data. In fact, a fixed size vocabulary can cover all the training data as long as the granularity of subword units is small enough. The main limitation of this method is the absence of morphology boundary. Some subword units may not be a word suffix which can represent a morphological meaning, and the subword units are treated in the same way as complete words. Subword units and complete words are predicted during a same sequence generation procedure. This may lead to two problems:
> 
> The sequence length can increase, especially on a morphologically rich language, which can lead to low NMT performance.
> 
> A subword unit cannot represent a linguistic unit, and suffix is not modeled explicitly.
> 
> BIBREF5 ( BIBREF5 ) proposed a hybrid architecture to deal with the OOV words in source side and any generated unknown tag in the target side. In their system, any OOV words on the source side are encoded at the character level, and if an unknown tag is predicted during decoding, another LSTM will be used to generate a sequence of target-side characters, which will be used as the replacement of the target side unknown word for the translation of a source OOV. However, their model may not work well when the target side is morphologically rich and the source side is not, because their hybrid network on the target side will only be used when an unknown tag is generated, which is always corresponding to a source unknown word. If most of the source side tokens are covered

#### Relevance 33

Label: 1

#### Passage 34

Retrieved by: Hybrid RRF followed by BGE reranking

> source side is not, because their hybrid network on the target side will only be used when an unknown tag is generated, which is always corresponding to a source unknown word. If most of the source side tokens are covered by the source vocabulary, the hybrid network may not have advantage on a morphologically rich target side language.
> 
> In BIBREF4 ( BIBREF4 )'s work, source side and target side sequence are all character-based, which eliminates OOV on the source side, and can generate any target side word theoretically. Character-based NMT may potentially improve the translation accuracy of morphologically rich language on the source side, but the training and decoding latency increase linearly with the sequence length, which is several times to the original word based NMT. Another disadvantage of character-based NMT is that character embedding lost the ability to represent a linguistic unit. Long-distance dependences are more difficult to be modeled in a character-based NMT. BIBREF4 ( BIBREF4 ) use convolutional and pooling layers on the source side to make the source sequence shorter. However, the target side sequence remains much longer than the original word sequence, and suffix boundary of the target side is not specifically considered in their model. This work may more helpful if a morphologically rich language is on the source side, but it is not designed to overcome the problem brought by a morphologically rich target side language.
> 
> There is another way which can effectively reduce target-side OOV. Both BIBREF6 ( BIBREF6 ) and BIBREF7 ( BIBREF7 ) use a large target-side vocabulary. To overcome the problem of GPU memory limitation and increasing computational complexity, instead of the original vocabulary, a selected subset is actually used both during the training and decoding time. Their model can generate any of the words in the large vocabulary, but data sparsity still remains, the low frequent words in the training data is not fully trained.

#### Relevance 34

Label: 1

## Question 0005

Paper: Learning Multi-Sense Word Distributions using Approximate Kullback-Leibler Divergence

> What are the qualitative experiments performed on benchmark datasets?

### Common Retrieved Chunks

#### Passage 35

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We proposed a KL divergence based energy function for learning multi-sense word embedding distributions modelled as Gaussian mixtures. Due to the intractability of the Gaussian mixtures for the KL divergence measure, we use an approximate KL divergence function. We also demonstrated that the proposed GM$\_$KL approaches performed better than other approaches on the benchmark word similarity and entailment datasets.
> 
> tocsectionAppendices

#### Relevance 35

Label: 0

#### Passage 36

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We train our proposed model GM$\_$KL (Gaussian Mixture using KL Divergence) on the Text8 dataset BIBREF14 which is a pre-processed data of $17M$ words from wikipedia. Of which, 71290 unique and frequent words are chosen using the subsampling trick in BIBREF15. We compare GM$\_$KL with the previous approaches w2g BIBREF9 ( single Gaussian model) and w2gm BIBREF10 (mixture of Gaussian model with expected likelihood kernel). For all the models used for experimentation, the embedding size ($D$) was set to 50, number of mixtures to 2, context window length to 10, batch size to 128. The word embeddings were initialized using a uniform distribution in the range of $[-\sqrt{\frac{3}{D}}$, $\sqrt{\frac{3}{D}}]$ such that the expectation of variance is 1 and mean 0 BIBREF16. One could also consider initializing the word embeddings using other contextual representations such as BERT BIBREF17 and ELMo BIBREF18 in the proposed approach. In order to purely analyze the performance of $\emph {GM\_KL}$ over the other models, we have chosen initialization using uniform distribution for experiments. For computational benefits, diagonal covariance is used similar to BIBREF10. Each mixture probability is constrained in the range $[0,1]$, summing to 1 by optimizing over unconstrained scores in the range $(-\infty ,\infty )$ and converting scores to probability using softmax function. The mixture scores are initialized to 0 to ensure fairness among all the components. The threshold for negative sampling was set to $10^{-5}$, as recommended in BIBREF3. Mini-batch gradient descent with Adagrad optimizer BIBREF19 was used with initial learning rate set to $0.05$.
> 
> Table TABREF9 shows the qualitative results of GM$\_$KL. Given a query word and component id, the set of nearest neighbours along with their respective component ids are listed. For eg., the word `plane' in its 0th component captures the `geometry' sense and so are its neighbours, and its 1st component captures `vehicle' sense and so are its corresponding neighbours. Other words such as `rock' captures both the `metal' and `music' senses, `star' captures `celebrity' and `astronomical' senses, and `phone' captures `telephony' and `internet' senses.
> 
> We quantitatively compare the performance of the GM$\_$KL, w2g, and w2gm approaches on the SCWS dataset BIBREF6. The dataset consists of 2003 word pairs of polysemous and homonymous words with

#### Relevance 36

Label: 1

#### Passage 37

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> max margin objective based on the asymmetric KL divergence energy function to capture textual entailment. Multi-sense distributions are advantageous in capturing polysemous nature of words and in reducing the uncertainty per word by distributing it across senses. However, computing KL divergence between mixtures of Gaussians is intractable, and we use a KL divergence approximation based on stricter upper and lower bounds. While capturing textual entailment (asymmetry), we have also not compromised on capturing symmetrical similarity between words (for example, funny and hilarious) which will be elucidated in Section $3.1$. We also show the effectiveness of the proposed approach on the benchmark word similarity and entailment datasets in the experimental section.

#### Relevance 37

Label: 0

#### Passage 38

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> and `astronomical' senses, and `phone' captures `telephony' and `internet' senses.
> 
> We quantitatively compare the performance of the GM$\_$KL, w2g, and w2gm approaches on the SCWS dataset BIBREF6. The dataset consists of 2003 word pairs of polysemous and homonymous words with labels obtained by an average of 10 human scores. The Spearman correlation between the human scores and the model scores are computed. To obtain the model score, the following metrics are used:
> 
> MaxCos: Maximum cosine similarity among all component pairs of words $w$ and $v$:
> 
> AvgCos: Average component-wise cosine similarity between the words $w$ and $v$.
> 
> KL$\_$approx: Formulated as shown in (DISPLAY_FORM8) between the words $w$ and $v$.
> 
> KL$\_$comp: Maximum component-wise negative KL between words $w$ and $v$:
> 
> Table TABREF17 compares the performance of the approaches on the SCWS dataset. It is evident from Table TABREF17 that GM$\_$KL achieves better correlation than existing approaches for various metrics on SCWS dataset.
> 
> Table TABREF18 shows the Spearman correlation values of GM$\_$KL model evaluated on the benchmark word similarity datasets: SL BIBREF20, WS, WS-R, WS-S BIBREF21, MEN BIBREF22, MC BIBREF23, RG BIBREF24, YP BIBREF25, MTurk-287 and MTurk-771 BIBREF26, BIBREF27, and RW BIBREF28. The metric used for comparison is 'AvgCos'. It can be seen that for most of the datasets, GM$\_$KL achieves significantly better correlation score than w2g and w2gm approaches. Other datasets such as MC and RW consist of only a single sense, and hence w2g model performs better and GM$\_$KL achieves next better performance. The YP dataset have multiple senses but does not contain entailed data and hence could not make use of entailment benefits of GM$\_$KL.
> 
> Table TABREF19 shows the evaluation results of GM$\_$KL model on the entailment datasets such as entailment pairs dataset BIBREF29 created from WordNet with both positive and negative labels, a crowdsourced dataset BIBREF30 of 79 semantic relations labelled as entailed or not and annotated distributionally similar nouns dataset BIBREF31. The 'MaxCos' similarity metric is used for evaluation and the best precision and best F1-score is shown, by picking the optimal threshold. Overall, GM$\_$KL performs better than both w2g and w2gm approaches.

#### Relevance 38

Label: 0

#### Passage 40

Retrieved by: Dense, Hybrid RRF

> The model parameters (means, covariances and mixture weights) $\theta $ can be learnt using a variant of max-margin objective BIBREF11.
> 
> Here $E_\theta (\cdot , \cdot )$ represents an energy function which assigns a score to the pair of words, $w$ is a particular word under consideration, $c$ its positive context (same context), and $c^{\prime }$ the negative context. The objective aims to push the margin of the difference between the energy function of a word $w$ to its positive context $c$ higher than its negative context $c$ by a threshold of $m$. Thus, word pairs in the same context gets a higher energy than the word pairs in the dissimilar context. BIBREF10 consider the energy function to be an expected likelihood kernel which is defined as follows.
> 
> This is similar to the cosine similarity metric over vectors and the energy between two words is maximum when they have similar distributions. But, the expected likelihood kernel is a symmetric metric which will not be suitable for capturing ordering among words and hence entailment.

#### Relevance 40

Label: 0

#### Passage 41

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> Language modelling in its inception had one-hot vector encoding of words. However, it captures only alphabetic ordering but not the word semantic similarity. Vector space models helps to learn word representations in a lower dimensional space and also captures semantic similarity. Learning word embedding aids in natural language processing tasks such as question answering and reasoning BIBREF0, stance detection BIBREF1, claim verification BIBREF2.
> 
> Recent models BIBREF3, BIBREF4 work on the basis that words with similar context share semantic similarity. BIBREF4 proposes a neural probabilistic model which models the target word probability conditioned on the previous words using a recurrent neural network. Word2Vec models BIBREF3 such as continuous bag-of-words (CBOW) predict the target word given the context, and skip-gram model works in reverse of predicting the context given the target word. While, GloVe embeddings were based on a Global matrix factorization on local contexts BIBREF5. However, the aforementioned models do not handle words with multiple meanings (polysemies).
> 
> BIBREF6 proposes a neural network approach considering both local and global contexts in learning word embeddings (point estimates). Their multiple prototype model handles polysemous words by providing apriori heuristics about word senses in the dataset. BIBREF7 proposes an alternative to handle polysemous words by a modified skip-gram model and EM algorithm. BIBREF8 presents a non-parametric based alternative to handle polysemies. However, these approaches fail to consider entailment relations among the words. BIBREF9 learn a Gaussian distribution per word using the expected likelihood kernel. However, for polysemous words, this may lead to word distributions with larger variances as it may have to cover various senses.
> 
> BIBREF10 proposes multimodal word distribution approach. It captures polysemy. However, the energy based objective function fails to consider asymmetry and hence entailment. Textual entailment recognition is necessary to capture lexical inference relations such as causality (for example, mosquito $\rightarrow $ malaria), hypernymy (for example, dog $\models $ animal) etc.
> 
> In this paper, we propose to obtain multi-sense word embedding distributions by using a variant of max margin objective based on the asymmetric KL divergence energy function to capture textual entailment. Multi-sense distributions are advantageous in capturing polysemous nature of words and in reducing the uncertainty per word by distributing it across senses. However, computing KL

#### Relevance 41

Label: 0

### BM25

#### Passage 39

Retrieved by: BM25

> As each word is represented by a mixture of Gaussian distributions, KL divergence is a better choice of energy function to capture distance between distributions. Since, KL divergence is minimum when the distributions are similar and maximum when they are dissimilar, energy function is taken as exponentiated negative KL divergence.
> 
> However, computing KL divergence between Gaussian mixtures is intractable and obtaining exact KL value is not possible. One way of approximating the KL is by Monte-Carlo approximation but it requires large number of samples to get a good approximation and is computationally expensive on high dimensional embedding space.
> 
> Alternatively, BIBREF12 presents a KL approximation between Gaussian mixtures where they obtain an upper bound through product of Gaussian approximation method and a lower bound through variational approximation method. In BIBREF13, the authors combine the lower and upper bounds from approximation methods of BIBREF12 to provide a stricter bound on KL between Gaussian mixtures. Lets consider Gaussian mixtures for the words $w$ and $v$ as follows.
> 
> The approximate KL divergence between the Gaussian mixture representations over the words $w$ and $v$ is shown in equation DISPLAY_FORM8. More details on approximation is included in the Supplementary Material.
> 
> where $EL_{ik}(w,w) = \int f_{w,i} (\operatorname{\mathbf {x}}) f_{w,k} (\operatorname{\mathbf {x}}) d\operatorname{\mathbf {x}}$ and $EL_{ij}(w,v) = \int f_{w,i} (\operatorname{\mathbf {x}}) f_{v,k} (\operatorname{\mathbf {x}}) d\operatorname{\mathbf {x}}$. Note that the expected likelihood kernel appears component wise inside the approximate KL divergence derivation.
> 
> One advantage of using KL as energy function is that it enables to capture asymmetry in entailment datasets. For eg., let us consider the words 'chair' with two senses as 'bench' and 'sling', and 'wood' with two senses as 'trees' and 'furniture'. The word chair ($w$) is entailed within wood ($v$), i.e. chair $\models $ wood. Now, minimizing the KL divergence necessitates maximizing $\log {\sum _j p_{v,j} \exp ({-KL(f_{w,i} (\operatorname{\mathbf {x}})||f_{v,j}(\operatorname{\mathbf {x}}))})}$ which in turn minimizes $KL(f_{w,i}(\operatorname{\mathbf {x}})||f_{v,j}(\operatorname{\mathbf {x}}))$. This will result in the support of the $i^{th}$ component of $w$ to be within the $j^{th}$ component of $v$, and holds for all component pairs leading to the entailment of $w$ within $v$. Consequently, we can see that bench $\models $ trees, bench $\models $ furniture, sling $\models $ trees, and sling

#### Relevance 39

Label: 0

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0006

Paper: Enhancing Sentence Relation Modeling with Auxiliary Character-level Embedding

> Which datasets do they evaluate on?

### Common Retrieved Chunks

#### Passage 42

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> representations into bidirectional LSTM, which means forward directional LSTM accept pre-trained word embedding output and backward directional LSTM accept auxiliary character CNN embedding output. The final sentence representation is the concatenation of the two direction. After that, we construct matching features followed by another temporal CNN to learn high-level hidden matching feature representations. Figure FIGREF1 shows the neural network architecture for general sentence relation modeling.
> 
> Our model shows that when trained on small size datasets, combining pre-trained word embeddings with auxiliary character-level embedding can improve the sentence representation. Word embeddings can help capturing general word semantic meanings, whereas char-level embedding can help modeling task specific word meanings. Note that auxiliary character-level embedding based sentence representation do not require the knowledge of words or even syntactic structure of a language. The enhanced sentence representation generated by multi-layer bidirectional LSTM will encapsulate the character and word levels informations. Furthermore, it may enhance matching features that generated by computing similarity measures on sentence pairs. Quantitative evaluations on standard dataset demonstrate the effectiveness and advantages of our method.

#### Relevance 42

Label: 0

#### Passage 43

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> In this paper, we propose a new deep neural network architecture that jointly leverage pre-trained word embedding and character embedding to learn sentence meanings. Our new approach first generates two kinds of word sequence representations as inputs into bidirectional LSTM to learn sentence representation. After that, we construct matching features followed by another temporal CNN to learn high-level hidden matching feature representations. Our model shows that combining pre-trained word embeddings with auxiliary character-level embedding can improve the sentence representation. The enhanced sentence representation generated by multi-layer bidirectional LSTM will encapsulate the character and word levels informations. Furthermore, it may enhance matching features that generated by computing similarity measures on sentence pairs. Experimental results on benchmark datasets demonstrate that our new framework achieved the state-of-the-art performance compared with other deep neural networks based approaches.

#### Relevance 43

Label: 0

#### Passage 45

Retrieved by: BM25, Hybrid RRF

> Existing neural sentence models mainly fall into two groups: convolutional neural networks (CNNs) and recurrent neural networks (RNNs). In regular 1D CNNs BIBREF6 , BIBREF8 , BIBREF19 , a fixed-size window slides over time (successive words in sequence) to extract local features of a sentence; then they pool these features to a vector, usually taking the maximum value in each dimension, for supervised learning. The convolutional unit, when combined with max-pooling, can act as the compositional operator with local selection mechanism as in the recursive autoencoder BIBREF3 . However, semantically related words that are not in one filter can't be captured effectively by this shallow architecture. BIBREF20 built deep convolutional models so that local features can mix at high-level layers. However, deep convolutional models may result in worse performance BIBREF19 .
> 
> On the other hand, RNN can take advantage of the parsing or dependency tree of sentence structure information BIBREF3 , BIBREF21 . BIBREF4 used dependency-tree recursive neural network to map text descriptions to quiz answers. Each node in the tree is represented as a vector; information is propagated recursively along the tree by some elaborate semantic composition. One major drawback of RNNs is the long propagation path of information near leaf nodes. As gradient may vanish when propagated through a deep path, such long dependency buries illuminating information under a complicated neural architecture, leading to the difficulty of training. To address this issue, BIBREF10 proposed a Tree-Structured Long Short-Term Memory Networks. This motivates us to investigate multi-layer bidirectional LSTM that directly models sentence meanings without parsing for RTE task.

#### Relevance 45

Label: 0

#### Passage 47

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We selected two related sentence relation modeling tasks: semantic relatedness task, which measures the degree of semantic relatedness of a sentence pair by assigning a relatedness score ranging from 1 (completely unrelated) to 5 ( very related); and textual entailment task, which determines whether the truth of a text entails the truth of another text called hypothesis. We use standard SICK (Sentences Involving Compositional Knowledge) dataset for evaluation. It consists of about 10,000 English sentence pairs annotated for relatedness in meaning and entailment.

#### Relevance 47

Label: 1

#### Passage 49

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> The task of semantic relatedness prediction tries to measure the degree of semantic relatedness of a sentence pair by assigning a relatedness score ranging from 1 (completely unrelated) to 5 (very related). More formally, given a sentence pair, we wish to predict a real-valued similarity score in a range of INLINEFORM0 , where INLINEFORM1 is an integer. The sequence INLINEFORM2 is the ordinal scale of similarity, where higher scores indicate greater degrees of similarity. We can predict the similarity score INLINEFORM3 by predicting the probability that the learned hidden representation INLINEFORM4 belongs to the ordinal scale. This is done by projecting an input representation onto a set of hyperplanes, each of which corresponds to a class. The distance from the input to a hyperplane reflects the probability that the input will located in corresponding scale.
> 
> Mathematically, the similarity score INLINEFORM0 can be written as: DISPLAYFORM0
> 
> where INLINEFORM0 and the weight matrix INLINEFORM1 and INLINEFORM2 are parameters.
> 
> In order to introduce the task objective function, we define a sparse target distribution INLINEFORM0 that satisfies INLINEFORM1 : DISPLAYFORM0
> 
> where INLINEFORM0 . The objective function then can be defined as the regularized KL-divergence between INLINEFORM1 and INLINEFORM2 : DISPLAYFORM0
> 
> where INLINEFORM0 is the number of training pairs and the superscript INLINEFORM1 indicates the INLINEFORM2 -th sentence pair BIBREF10 .
> 
> Referring to textual entailment recognition task, we want to maximize the likelihood of the correct class. This is equivalent to minimizing the negative log-likelihood (NLL). More specifically, the label INLINEFORM0 given the inputs INLINEFORM1 is predicted by a softmax classifier that takes the hidden state INLINEFORM2 at the node as input: DISPLAYFORM0
> 
> After that, the objective function is the negative log-likelihood of the true class labels INLINEFORM0 : DISPLAYFORM0
> 
> where INLINEFORM0 is the number of training pairs and the superscript INLINEFORM1 indicates the INLINEFORM2 th sentence pair.

#### Relevance 49

Label: 0

#### Passage 50

Retrieved by: Dense, Hybrid RRF

> Table TABREF31 and TABREF32 show the Pearson correlation and accuracy comparison results of semantic relatedness and text entailment tasks. We can see that combining CharCNN with multi-layer bidirectional LSTM yields better performance compared with other traditional machine learning methods such as SVM and MaxEnt approach BIBREF17 , BIBREF0 that served with many handcraft features. Note that our method doesn't need extra handcrafted feature extraction procedure. Also our method doesn't leverage external linguistic resources such as wordnet or parsing which get best results in BIBREF10 . More importantly, both task prediction results close to the state-of-the-art results. It proved that our approaches successfully simultaneously predict heterogeneous tasks. Note that for semantic relatedness task, the latest research BIBREF10 proposed a tree-structure based LSTM, the Pearson correlation score of their system can reach 0.863. Compared with their approach, our method didn't use dependency parsing and can be used to predict tasks contains multiple languages.
> 
> We hope to point out that we implemented the method in BIBREF10 , but the results are not as good as our method. Here we use the results reported in their paper. Based on our experiments, we believe the method in BIBREF10 is very sensitive to the initializations, thus it may not achieve the good performance in different settings. However, our method is pretty stable which may benefit from the joint tasks training.

#### Relevance 50

Label: 0

#### Passage 51

Retrieved by: Dense, Hybrid RRF

> Traditional approaches BIBREF0 , BIBREF1 , BIBREF2 for sentence relation modeling tasks such as paraphrase identification, question answering, recognized textual entailment and semantic textual similarity prediction usually build the supervised model using a variety of hand crafted features. Hundreds of features generated at different linguistic levels are exploited to boost classification. With the success of deep learning, there has been much interest in applying deep neural network based techniques to further improve the prediction performances BIBREF3 , BIBREF4 , BIBREF5 .
> 
> A key component of deep neural network is word embedding which serve as an lookup table to get word representations. From low level NLP tasks such as language modeling, POS tagging, name entity recognition, and semantic role labeling BIBREF6 , BIBREF7 , to high level tasks such as machine translation, information retrieval and semantic analysis BIBREF8 , BIBREF9 , BIBREF10 . Deep word representation learning has demonstrated its importance for these tasks. All the tasks get performance improvement via further learning either word level representations or sentence level representations. On the other hand, some researchers have found character-level convolutional networks BIBREF11 , BIBREF12 are useful in extracting information from raw signals for the task such as language modeling or text classification.
> 
> In this work, we focus on deep neural network based sentence relation modeling tasks. We explore treating each sentence as a kind of raw signal at character level, and applying temporal (one-dimensional) Convolution Neural Network (CNN) BIBREF6 , Highway Multilayer Perceptron (HMLP) and multi-layer bidirectional LSTM (Long Short Term Memory) BIBREF13 to learn sentence representations. We propose a new deep neural network architecture that jointly leverage pre-trained word embedding and character embedding to represent the meaning sentences. More specifically, our new approach first generates two kinds of word sequence representations. One kind of sequence representations are the composition of pre-trained word vectors. The other kind of sequence representation comprise word vectors that generating from character-level convolutional network. We then inject the two sequence representations into bidirectional LSTM, which means forward directional LSTM accept pre-trained word embedding output and backward directional LSTM accept auxiliary character CNN embedding output. The final sentence representation is the concatenation of the two direction. After that, we construct matching

#### Relevance 51

Label: 0

### BM25

#### Passage 44

Retrieved by: BM25

> One shortcoming of conventional RNNs is that they are only able to make use of previous context. In text entailment, the decision is made after the whole sentence pair is digested. Therefore, exploring future context would be better for sequence meaning representation. Bidirectional RNNs architecture BIBREF13 proposed a solution of making prediction based on future words. At each time step INLINEFORM0 , the model maintains two hidden states, one for the left-to-right propagation INLINEFORM1 and the other for the right-to-left propagation INLINEFORM2 . The hidden state of the Bidirectional LSTM is the concatenation of the forward and backward hidden states. The following equations illustrate the main ideas: DISPLAYFORM0
> 
> Deep RNNs can be created by stacking multiple RNN hidden layer on top of each other, with the output sequence of one layer forming the input sequence for the next. Assuming the same hidden layer function is used for all INLINEFORM0 layers in the stack, the hidden vectors INLINEFORM1 are iteratively computed from INLINEFORM2 to INLINEFORM3 and INLINEFORM4 to INLINEFORM5 : DISPLAYFORM0
> 
> Multilayer bidirectional RNNs can be implemented by replacing each hidden vector INLINEFORM0 with the forward and backward vectors INLINEFORM1 and INLINEFORM2 , and ensuring that every hidden layer receives input from both the forward and backward layers at the level below. Furthermore, we can apply LSTM memory cell to hidden layers to construct multilayer bidirectional LSTM.
> 
> Finally, we can concatenate sequence hidden matrix INLINEFORM0 and reversed sequence hidden matrix INLINEFORM1 to form the sentence representation. We refer to INLINEFORM2 is the number of layers, INLINEFORM3 as the memory dimensionality of the LSTM. In the next section, we will use the two matrixs to generate matching feature planes via linear algebra operations.

#### Relevance 44

Label: 0

#### Passage 46

Retrieved by: BM25

> In this experiment, we will compare tree LSTM with sequential LSTM. A limitation of the sequence LSTM architectures is that they only allow for strictly sequential information propagation. However, tree LSTMs allow richer network topologies where each LSTM unit is able to incorporate information from multiple child units. As in standard LSTM units, each Tree-LSTM unit (indexed by INLINEFORM0 ) contains input and output gates INLINEFORM1 and INLINEFORM2 , a memory cell INLINEFORM3 and hidden state INLINEFORM4 . The difference between the standard LSTM unit and tree LSTM units is that gating vectors and memory cell updates are dependent on the states of possibly many child units. Additionally, instead of a single forget gate, the tree LSTM unit contains one forget gate INLINEFORM5 for each child INLINEFORM6 . This allows the tree LSTM unit to selectively incorporate information from each child.
> 
> We use dependency tree child-sum tree LSTM proposed by BIBREF10 as our baseline. Given a tree, let INLINEFORM0 denote the set of children of node INLINEFORM1 . The child-sum tree LSTM transition equations are the following: DISPLAYFORM0
> 
> Table TABREF35 show the comparisons between tree and sequential based methods. We can see that, if we don't deploy CNN, simple Tree LSTM yields better result than traditional LSTM, but worse than Bidirectional LSTM. This is reasonable due to the fact that Bidirectional LSTM can enhance sentence representation by concatenating forward and backward representations. We found that adding CNN layer will decrease the accuracy in this scenario. Because when feeding into CNN, we have to reshape the feature planes otherwise convolution will not work. For example, we set convolution kernel width as 2, the input 2D tensor will have the shape lager than 2. To boost performance with CNN, we need more matching features. We found Multi-layer Bidirectional LSTM can incorporate more features and achieve best performance compared with single-layer Bidirectional LSTM.

#### Relevance 46

Label: 0

### Dense

#### Passage 48

Retrieved by: Dense

> Inspired by BIBREF10 , we apply element-wise merge to first sentence matrix INLINEFORM0 and second sentence matrix INLINEFORM1 . Similar to previous method, we can define two simple matching feature planes (FPs) with below equations: DISPLAYFORM0
> 
> where INLINEFORM0 is the element-wise multiplication. The INLINEFORM1 measure can be interpreted as an element-wise comparison of the signs of the input representations. The INLINEFORM2 measure can be interpreted as the distance between the input representations.
> 
> In addition to the above measures, we also found the following feature plane can improve the performance: DISPLAYFORM0
> 
> In INLINEFORM0 , the INLINEFORM1 means one-dimensional convolution. Join mean concatenate the two representation. The intuition behind INLINEFORM2 is let the one-dimensional convolution preserves the common information between sentence pairs.

#### Relevance 48

Label: 0

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 52

Retrieved by: Hybrid RRF followed by BGE reranking

> Besides pre-trained word vectors, we are also interested in generating word vectors from characters. To achieve that, we leverage deep convolutional neural network(ConvNets). The model accepts a sequence of encoded characters as input. The encoding si done by prescribing an alphabet of size INLINEFORM0 for the input language, and then quantize each character using one-hot encoding. Then, the sequence of characters is transformed to a sequence of such INLINEFORM1 sized vectors with fixed length INLINEFORM2 . Any character exceeding length INLINEFORM3 is ignored, and any characters that are not in the alphabet are quantized as all-zero vectors. The alphabet used in our model consists of 36 characters, including 26 english letters and 10 digits. Below, we will introduce character-level temporal convolution neural network.

#### Relevance 52

Label: 0

## Question 0007

Paper: SAMSum Corpus: A Human-annotated Dialogue Dataset for Abstractive Summarization

> Do authors propose some better metric than ROUGE for measurement of abstractive dialogue summarization?

### Common Retrieved Chunks

#### Passage 53

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> This paper is a step towards abstractive summarization of dialogues by (1) introducing a new dataset, created for this task, (2) comparison with news summarization by the means of automated (ROUGE) and human evaluation.
> 
> Most of the tools and the metrics measuring the quality of text summarization have been developed for a single-speaker document, such as news; as such, they are not necessarily the best choice for conversations with several speakers.
> 
> We test a few general-purpose summarization models. In terms of human evaluation, the results of dialogues summarization are worse than the results of news summarization. This is connected with the fact that the dialogue structure is more complex – information is spread in multiple utterances, discussions, questions, more typos and slang words appear there, posing new challenges for summarization. On the other hand, dialogues are divided into utterances, and for each utterance its author is assigned. We demonstrate in experiments that the models benefit from the introduction of separators, which mark utterances for each person. This suggests that dedicated models having some architectural changes, taking into account the assignation of a person to an utterance in a systematic manner, could improve the quality of dialogue summarization.
> 
> We show that the most popular summarization metric ROUGE does not reflect the quality of a summary. Looking at the ROUGE scores, one concludes that the dialogue summarization models perform better than the ones for news summarization. In fact, this hypothesis is not true – we performed an independent, manual analysis of summaries and we demonstrated that high ROUGE results, obtained for automatically-generated dialogue summaries, correspond with lower evaluation marks given by human annotators. An interesting example of the misleading behavior of the ROUGE metrics is presented in Table TABREF35 for Dialogue 4, where a wrong summary – 'paul and cindy don't like red roses.' – obtained all ROUGE values higher than a correct summary – 'paul asks cindy what color flowers should buy.'. Despite lower ROUGE values, news summaries were scored higher by human evaluators. We conclude that when measuring the quality of model-generated summaries, the ROUGE metrics are more indicative for news than for dialogues, and a new metric should be designed to measure the quality

#### Relevance 53

Label: 1

#### Passage 54

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> ROUGE is a standard way of evaluating the quality of machine generated summaries by comparing them with reference ones. The metric based on n-gram overlapping, however, may not be very informative for abstractive summarization, where paraphrasing is a keypoint in producing high-quality sentences. To quantify this conjecture, we manually evaluated summaries generated by the models for 150 news and 100 dialogues. We asked two linguists to mark the quality of every summary on the scale of $-1$, 0, 1, where $-1$ means that a summarization is poor, extracts irrelevant information or does not make sense at all, 1 – it is understandable and gives a brief overview of the text, and 0 stands for a summarization that extracts only a part of relevant information, or makes some mistakes in the produced summary.
> 
> We noticed a few annotations (7 for news and 4 for dialogues) with opposite marks (i.e. one annotator judgement was $-1$, whereas the second one was 1) and decided to have them annotated once again by another annotator who had to resolve conflicts. For the rest, we calculated the linear weighted Cohen's kappa coefficient BIBREF22 between annotators' scores. For news examples, we obtained agreement on the level of $0.371$ and for dialogues – $0.506$. The annotators' agreement is higher on dialogues than on news, probably because of structures of those data – articles are often long and it is difficult to decide what the key-point of the text is; dialogues, on the contrary, are rather short and focused mainly on one topic.
> 
> For manually evaluated samples, we calculated ROUGE metrics and the mean of two human ratings; the prepared statistics is presented in Table TABREF27. As we can see, models generating dialogue summaries can obtain high ROUGE results, but their outputs are marked as poor by human annotators. Our conclusion is that the ROUGE metric corresponds with the quality of generated summaries for news much better than for dialogues, confirmed by Pearson's correlation between human evaluation and the ROUGE metric, shown in Table TABREF28.

#### Relevance 54

Label: 1

#### Passage 55

Retrieved by: BM25, Hybrid RRF

> The baseline commonly used in the news summarization task is Lead-3 BIBREF4, which takes three leading sentences of the document as the summary. The underlying assumption is that the beginning of the article contains the most significant information. Inspired by the Lead-n model, we propose a few different simple models:
> 
> MIDDLE-n, which takes n utterances from the middle of the dialogue,
> 
> LONGEST-n, treating only n longest utterances in order of length as a summary,
> 
> LONGER-THAN-n, taking only utterances longer than n characters in order of length (if there is no such long utterance in the dialogue, takes the longest one),
> 
> MOST-ACTIVE-PERSON, which treats all utterances of the most active person in the dialogue as a summary.
> 
> Results of the evaluation of the above models are reported in Table TABREF9. There is no obvious baseline for the task of dialogues summarization. We expected rather low results for Lead-3, as the beginnings of the conversations usually contain greetings, not the main part of the discourse. However, it seems that in our dataset greetings are frequently combined with question-asking or information passing (sometimes they are even omitted) and such a baseline works even better than the MIDDLE baseline (taking utterances from the middle of a dialogue). Nevertheless, the best dialogue baseline turns out to be the LONGEST-3 model.

#### Relevance 55

Label: 0

#### Passage 56

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> news summaries were scored higher by human evaluators. We conclude that when measuring the quality of model-generated summaries, the ROUGE metrics are more indicative for news than for dialogues, and a new metric should be designed to measure the quality of abstractive dialogue summaries.

#### Relevance 56

Label: 1

#### Passage 58

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> In our paper we have studied the challenges of abstractive dialogue summarization. We have addressed a major factor that prevents researchers from engaging into this problem: the lack of a proper dataset. To the best of our knowledge, this is the first attempt to create a comprehensive resource of this type which can be used in future research. The next step could be creating an even more challenging dataset with longer dialogues that not only cover one topic, but span over numerous different ones.
> 
> As shown, summarization of dialogues is much more challenging than of news. In order to perform well, it may require designing dedicated tools, but also new, non-standard measures to capture the quality of abstractive dialogue summaries in a relevant way. We hope to tackle these issues in future work.

#### Relevance 58

Label: 1

#### Passage 59

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

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

#### Relevance 59

Label: 0

### BM25

#### Passage 57

Retrieved by: BM25

> The results for the news summarization task are shown in Table TABREF25 and for the dialogue summarization – in Table TABREF26. In both domains, the best models' ROUGE-1 exceeds 39, ROUGE-2 – 17 and ROUGE-L – 36. Note that the strong baseline for news (Lead-3) is outperformed in all three metrics only by one model. In the case of dialogues, all tested models perform better than the baseline (LONGEST-3).
> 
> In general, the Transformer-based architectures benefit from training on the joint dataset: news+dialogues, even though the news and the dialogue documents have very different structures. Interestingly, this does not seem to be the case for the Pointer Generator or Fast Abs RL model.
> 
> The inclusion of a separation token between dialogue utterances is advantageous for most models – presumably because it improves the discourse structure. The improvement is most visible when training is performed on the joint dataset.
> 
> Having compared two variants of the Fast Abs RL model – with original utterances and with enhanced ones (see Section SECREF11), we conclude that enhancing utterances with information about the other interlocutors helps achieve higher ROUGE values.
> 
> The largest improvement of the model performance is observed for LightConv and DynamicConv models when they are complemented with pretrained embeddings from the language model GPT-2, trained on enormous corpora.
> 
> It is also worth noting that some models (Pointer Generator, Fast Abs RL), trained only on the dialogues corpus (which has 16k dialogues), reach similar level (or better) in terms of ROUGE metrics than models trained on the CNN/DM news dataset (which has more than 300k articles). Adding pretrained embeddings and training on the joined dataset helps in achieving significantly higher values of ROUGE for dialogues than the best models achieve on the CNN/DM news dataset.
> 
> According to ROUGE metrics, the best performing model is DynamicConv with GPT-2 embeddings, trained on joined news and dialogue data with an utterance separation token.

#### Relevance 57

Label: 0

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0008

Paper: Towards Supervised and Unsupervised Neural Machine Translation Baselines for Nigerian Pidgin

> What baselines do they propose?

### Common Retrieved Chunks

#### Passage 60

Retrieved by: BM25, Dense, Hybrid RRF

> The following insights can be drawn from the example translations shown in the tables above:
> 
> The unsupervised model performed poorly at some simple translation examples, such as the first translation example.
> 
> For all translation models, the model makes hypothesis that are grammatically and qualitatively correct, but do not exactly match the reference translation, such as the second translation example.
> 
> Surprisingly, the unsupervised model performs better at some relatively simple translation examples than both supervised models. The third example is a typical such case.
> 
> The supervised translation models seem to perform better at longer example translations than the unsupervised example.

#### Relevance 60

Label: 0

#### Passage 61

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Some work has been done on developing neural machine translation baselines for African languages. BIBREF4 implemented a transformer model which significantly outperformed existing statistical machine translation architectures from English to South-African Setswana. Also, BIBREF5 went further, to train neural machine translation models from English to five South African languages using two different architectures - convolutional sequence-to-sequence and transformer. Their results showed that neural machine translation models are very promising for African languages.
> 
> The only known natural language processing work done on any variant of Pidgin English is by BIBREF6. The authors provided the largest known Nigerian Pidgin English corpus and trained the first ever translation models between both languages via unsupervised neural machine translation due to the absence of parallel training data at the time.

#### Relevance 61

Label: 0

#### Passage 62

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Over 500 languages are spoken in Nigeria, but Nigerian Pidgin is the uniting language in the country. Between three and five million people are estimated to use this language as a first language in performing their daily activities. Nigerian Pidgin is also considered a second language to up to 75 million people in Nigeria, accounting for about half of the country's population according to BIBREF0.
> 
> The language is considered an informal lingua franca and offers several benefits to the country. In 2020, 65% of Nigeria's population is estimated to have access to the internet according to BIBREF1. However, over 58.4% of the internet's content is in English language, while Nigerian languages, such as Igbo, Yoruba and Hausa, account for less than 0.1% of internet content according to BIBREF2. For Nigerians to truly harness the advantages the internet offers, it is imperative that English content is able to be translated to Nigerian languages, and vice versa.
> 
> This work is a first attempt towards using contemporary neural machine translation (NMT) techniques to perform machine translation for Nigerian Pidgin, establishing solid baselines that will ease and spur future work. We evaluate the performance of supervised and unsupervised neural machine translation models using word-level and the subword-level tokenization of BIBREF3.

#### Relevance 62

Label: 1

#### Passage 64

Retrieved by: BM25, Hybrid RRF

> All baseline models were trained using the Transformer architecture of BIBREF7. We experiment with both word-level and Byte Pair Encoding (BPE) subword-level tokenization methods for the supervised models. We learned 4000 byte pair encoding tokens, following the findings of BIBREF5. For the unuspervised model, we experiment with only word-level tokenization.

#### Relevance 64

Label: 1

#### Passage 65

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> There is an increasing need to use neural machine translation techniques for African languages. Due to the low-resourced nature of these languages, these techniques can help build useful translation models that could hopefully help with the preservation and discoverability of these languages.
> 
> Future works include establishing qualitative metrics and the use of pre-trained models to bolster these translation models.
> 
> Code, data, trained models and result translations are available here - https://github.com/orevaoghene/pidgin-baseline

#### Relevance 65

Label: 0

### BM25

#### Passage 63

Retrieved by: BM25

> Special thanks to the Masakhane group for catalysing this work.

#### Relevance 63

Label: 0

### Dense

#### Passage 66

Retrieved by: Dense

> When analyzed by L1 speakers, the translation qualities were rated very well. In particular, the unsupervised model makes many translations that did not exactly match the reference translation, but conveyed the same meaning. More analysis and translation examples are in the Appendix.

#### Relevance 66

Label: 0

#### Passage 67

Retrieved by: Dense

> The dataset used for the supervised was obtained from the JW300 large-scale, parallel corpus for Machine Translation (MT) by BIBREF8. The train set contained 20214 sentence pairs, while the validation contained 1000 sentence pairs. Both the supervised and unsupervised models were evaluated on a test set of 2101 sentences preprocessed by the Masakhane group. The model with the highest test BLEU score is selected as the best.

#### Relevance 67

Label: 0

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 68

Retrieved by: Hybrid RRF followed by BGE reranking

> Unsupervised (Word-Level):
> 
> Supervised (Word-Level):
> 
> Supervised (Byte Pair Encoding):

#### Relevance 68

Label: 1

#### Passage 69

Retrieved by: Hybrid RRF followed by BGE reranking

> Unsupervised (Word-Level):
> 
> Supervised (Word-Level):
> 
> Supervised (Byte Pair Encoding):

#### Relevance 69

Label: 1

## Question 0009

Paper: XPersona: Evaluating Multilingual Personalized Chatbot

> Which languages does their newly created dataset contain?

### Common Retrieved Chunks

#### Passage 70

Retrieved by: BM25, Hybrid RRF

> propose competitive baselines in two training settings, namely, cross-lingual and multilingual, and compare them with translation pipeline models. Our baselines leverage pre-trained cross-lingual BIBREF4 and multilingual BIBREF5 models.
> 
> An extensive automatic and human evaluation BIBREF6 of our models shows that a multilingual system is able to outperform strong translation-based models and on par with or even improve the monolingual model. The cross-lingual performance is still lower than other models, which indicates that cross-lingual conversation modeling is very challenging. The main contribution of this paper are summarized as follows:
> 
> We present the first multilingual non-goal-oriented dialogue benchmark for evaluating multilingual generative chatbots.
> 
> We provide both cross-lingual and multilingual baselines and discuss their limitations to inspire future research.
> 
> We show the potential of multilingual systems to understand the mixed language dialogue context and generate coherent responses.

#### Relevance 70

Label: 0

#### Passage 71

Retrieved by: BM25, Dense, Hybrid RRF

> Extensive approaches have been introduced to construct multilingual systems, for example, multilingual semantic role labeling BIBREF28, BIBREF29, multilingual machine translation BIBREF30, multilingual automatic speech recognition BIBREF31, BIBREF32, BIBREF33, BIBREF34, and named entity recognition BIBREF35, BIBREF36. Multilingual deep contextualized model such as Multilingual BERT (M-BERT) BIBREF5 have been commonly used to represent multiple languages and elevate the performance in many NLP applications, such as classification tasks BIBREF37, textual entailment, named entity recognition BIBREF38, and natural language understanding BIBREF39. Multilingual datasets have also been created for a number of NLP tasks, such as named entity recognition or linking BIBREF40, BIBREF41, BIBREF42, BIBREF43, question answering BIBREF44, BIBREF45, semantic role labeling BIBREF46, part-of-speech tagging BIBREF47, dialogue state tracking BIBREF48, and natural language understanding BIBREF49. However, none of these datasets include the multilingual chit-chat task.

#### Relevance 71

Label: 0

#### Passage 73

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> daily colloquial English expressions such as “cool", “I see", and “lol" are usually literally translated. After that, we use a simple string matching to revise the inappropriate translations in the whole training-set and return a revision log, which records all the revised utterances. Then, we assign human annotators to check all the revised utterances and list translation mistakes again. We repeat this process at least twice for each language. Finally, we summarize the statistics of the collected dataset in Table TABREF6.

#### Relevance 73

Label: 0

#### Passage 75

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The proposed XPersona dataset is an extension of the persona-chat dataset BIBREF0, BIBREF1. Specifically, we extend the ConvAI2 BIBREF1 to six languages: Chinese, French, Indonesian, Italian, Korean, and Japanese. Since the test set of ConvAI2 is hidden, we split the original validation set into a new validation set and test sets. Then, we firstly automatically translate the training, validation, and test set using APIs (PapaGo for Korean, Google Translate for other languages). For each language, we hired native speaker annotators with a fluent level of English and asked them to revise the machine-translated dialogues and persona sentences in the validation set and test set according to original English dialogues. The main goal of human annotation is to ensure the resulting conversations are coherent and fluent despite the cultural differences in target languages. Therefore, annotators are not restricted to only translate the English dialogues, and they are allowed to modify the original dialogues to improve the dialogue coherence in the corresponding language while retaining the persona information. The full annotation instructions are reported in Appendix A.
> 
> Compared to collecting new persona sentences and dialogues in each language, human-annotating the dialogues by leveraging translation APIs has multiple advantages. First, it increases the data distribution similarity across languages BIBREF3, which can better examine the system's cross-lingual transferability. Second, revising the machine-translated dialogues based on the original English dialogue improves the data construction efficiency. Third, it leverages the well-constructed English persona conversations as a reference to ensure the dialogue quality without the need for training a new pool of workers to generate new samples BIBREF3.
> 
> On the other hand, human-translating the entire training-set ($\sim $130K utterances) in six languages is expensive. Therefore, we propose an iterative method to improve the quality of the automatically translated training set. We firstly sample 200 dialogues from the training set ($\sim $2600 utterances) in each language, and we assign human annotators to list all frequent translation mistakes in the given dialogues. For example, daily colloquial English expressions such as “cool", “I see", and “lol" are usually literally translated. After that, we use a simple string matching to revise the inappropriate translations in the whole training-set and return a revision log, which records all

#### Relevance 75

Label: 1

#### Passage 77

Retrieved by: Dense, Hybrid RRF

> Another strong baseline we compare with is Poly-encoder BIBREF75, a large-scale pre-trained retrieval model that has shown state-of-the-art performance in the English Persona-chat dataset BIBREF6. We adapt this model to the other languages by using the Google Translate API to translate target languages (e.g., Chinese) query to English as the input to the model, then translate the English response back to the target language. Thus, the response generation flow is: target query $\rightarrow $ English query $\rightarrow $ English response $\rightarrow $ target response. We denote this model as Poly.

#### Relevance 77

Label: 0

### BM25

#### Passage 72

Retrieved by: BM25

> Evaluating open-domain chit-chat models is challenging, especially in multiple languages and at the dialogue-level. Hence, we evaluate our models using both automatic and human evaluation. In both cases, human-annotated dialogues are used, which show the importance of the provided dataset.

#### Relevance 72

Label: 0

#### Passage 74

Retrieved by: BM25

> are categorized as goal-oriented BIBREF7, BIBREF8 and chit-chat BIBREF9, BIBREF10. Interested readers may refer to BIBREF11 for a general overview. In this paper, we focus on the latter, for which, in recent years, several tasks and datasets have been proposed to ground the conversation on knowledge BIBREF12, BIBREF13, BIBREF14, BIBREF15, BIBREF16, BIBREF17, BIBREF18 such as Wiki-Articles, Reddit-Post, and CNN-Article. In this work, we focus on personalized dialogue agents where the dialogues are grounded on persona information.
> 
> BIBREF19 was the first to introduce a persona-grounded dialogue dataset for improving response consistency. Later on, BIBREF0 and BIBREF1 introduced Persona-chat, a multi-turn conversational dataset, where two speakers are paired, and a persona description (4–5 sentences) is randomly assigned to each of them. By conditioning the response generation on the persona descriptions, a chit-chat model is able to produce a more persona-consistent dialogue BIBREF0. Several works have improved on the initial baselines with various methodologies BIBREF20, BIBREF21, BIBREF22, BIBREF23, BIBREF24, BIBREF25, especially using large pre-trained models BIBREF26, BIBREF27.

#### Relevance 74

Label: 0

### Dense

#### Passage 76

Retrieved by: Dense

> transfers knowledge from the source language data to the target languages. In this setting, the model is trained on English (source language) conversational samples, and evaluated on the other 6 languages. Following the methodology proposed by BIBREF4, we align the embedded representations of different languages into the same embedding space by applying cross-lingual pre-training to the encoder-decoder model. The pre-training procedure consists of two stages:
> 
> pre-training the encoder and the decoder independently utilizing masked language modeling, as in BIBREF59;
> 
> jointly pre-training the encoder-decoder by using two objective functions: Cross-Lingual Auto-Encoding (XAE) and Denoising Auto-Encoding (DAE) BIBREF4.
> 
> For instance, DAE adds perturbations to the input sentence and tries to reconstructs the original sentence using the decoder, whereas, XAE uses parallel translation data as the supervision signal to pre-train both the encoder and decoder. As in the multilingual models, the language IDs are fed into the decoder to control the language of generated sentences. Both pre-training stages require both parallel and non-parallel data in the target language.
> 
> After the two stages of pre-training, the model is fine-tuned using just the source language samples (i.e., English) with the same cross-entropy loss as for the multilingual training. However, as suggested in BIBREF4, only the encoder parameters are updated with back-propagation and both the decoder and the word embedding layer remain frozen. This retains the decoders' ability to generate multilingual output while still being able to learn new tasks using only the target language.

#### Relevance 76

Label: 0

#### Passage 78

Retrieved by: Dense

> We report more the mixed-language samples generated by M-CausalBert in Table TABREF61 and TABREF62.

#### Relevance 78

Label: 0

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 79

Retrieved by: Hybrid RRF followed by BGE reranking

> Personalized dialogue agents have been shown efficient in conducting human-like conversation. This progress has been catalyzed thanks to existing conversational dataset such as Persona-chat BIBREF0, BIBREF1. However, the training data are provided in a single language (e.g., English), and thus the resulting systems can perform conversations only in the training language. For wide, commercial dialogue systems are required to handle a large number of languages since the smart home devices market is increasingly international BIBREF2. Therefore, creating multilingual conversational benchmarks is essential, yet challenging since it is costly to perform human annotation of data in all languages.
> 
> A possible solution is to use translation systems before and after the model inference, a two-step translation from any language to English and from English to any language. This comes with three major problems: 1) amplification of translation errors since the current dialogue systems are far from perfect, especially with noisy input; 2) the three-stage pipeline system is significantly slower in terms of inference speed; and 3) high translation costs since the current state-of-the-art models, especially in low resources languages, are only available using costly APIs.
> 
> In this paper, we analyze two possible workarounds to alleviate the aforementioned challenges. The first is to build a cross-lingual transferable system by aligning cross-lingual representations, as in BIBREF3, in which the system is trained on one language and zero-shot to another language. The second is to learn a multilingual system directly from noisy multilingual data (e.g., translated data), thus getting rid of the translation system dependence at inference time.
> 
> To evaluate the aforementioned systems, we propose a dataset called Multilingual Persona-Chat, or XPersona, by extending the Persona-Chat corpora BIBREF1 to six languages: Chinese, French, Indonesian, Italian, Korean, and Japanese. In XPersona, the training sets are automatically translated using translation APIs with several human-in-the-loop passes of mistake correction. In contrast, the validation and test sets are annotated by human experts to facilitate both automatic and human evaluations in multiple languages.
> 
> Furthermore, we propose competitive baselines in two training settings, namely, cross-lingual and multilingual, and compare them with translation pipeline models. Our baselines leverage pre-trained cross-lingual BIBREF4 and multilingual BIBREF5 models.
> 
> An extensive automatic and human evaluation BIBREF6 of our models shows that

#### Relevance 79

Label: 1

#### Passage 80

Retrieved by: Hybrid RRF followed by BGE reranking

> In this paper, we studied both cross-lingual and multilingual approaches in end-to-end personalized dialogue modeling. We presented the XPersona dataset, a multilingual extension of Persona-Chat, for evaluating the multilingual personalized chatbots. We further provided both cross-lingual and multilingual baselines and compared them with the monolingual approach and two-stage translation approach. Extensive automatic evaluation and human evaluation were conducted to examine the models' performance. The experimental results showed that multilingual trained models, with a single model across multiple languages, can outperform the two-stage translation approach and is on par with monolingual models. On the other hand, the current state-of-the-art cross-lingual approach XNLG achieved lower performance than other baselines. In future work, we plan to research a more advanced cross-lingual generation approach and construct a mixed-language conversational benchmark for evaluating multilingual systems.

#### Relevance 80

Label: 0

#### Passage 81

Retrieved by: Hybrid RRF followed by BGE reranking

> Poly-encoder, pretrained on 174 million Reddit data, can accurately retrieve coherent and diverse responses in English. However, in the other six languages, some of the retrieved responses are digressive due to translation error.

#### Relevance 81

Label: 0

## Question 0010

Paper: Data Collection for Interactive Learning through the Dialog

> How was this data collected?

### Common Retrieved Chunks

#### Passage 82

Retrieved by: BM25, Dense, Hybrid RRF

> We collected the dataset with 1900 dialogs and 8533 turns. Topics discussed in dialogs are questions randomly chosen from training examples of Simple questions BIBREF7 dataset. From this dataset we also took the correct answers in form of Freebase entities.
> 
> Our dataset consists of standard data split into training, development and test files. The basic properties of those files are as follows:
> 
> Each file contains complete dialogs enriched by outputs of NLU (see Section "Natural Language Understanding (NLU)" ) that were used during the data collection. On top of that, each dialog is labeled by the correct answer for the question and expert annotation of the user answer hint which tells whether the hint points to the correct answer, incorrect answer, or no answer at all.
> 
> 351 of all collected dialogs contain correct answer provided by users and 702 dialogs have incorrect answer. In the remaining 847 dialogs users did not want to answer the question. The collected dialogs also contain 1828 paraphrases and 1539 explanations for 1870 questions.
> 
> An answer for a question was labeled as correct by annotators only when it was evident to them that the answer points to the same Freebase entity that was present in Simple questions dataset for that particular question. However, a large amount of questions from that dataset is quite general - with many possible answers. Therefore lot of answers from users were labeled as incorrect even though those answers perfectly fit the question. Our annotators identified that 285 of the incorrect answers were answers for such general questions. Example of this situation can be demonstrated by question 'Name an actor' which was correctly answered by 'Brad Pitt is an actor', however, to be consistent with Simple questions annotation, which is 'Kelly Atwood', annotators were forced to mark it as an incorrect answer.

#### Relevance 82

Label: 1

#### Passage 83

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> It is quite challenging to find appropriate entity in the knowledge base even though the user provided the correct answer. Therefore, we propose another metric relevant to our dataset. This metric is the accuracy of entity extraction which measures how many times was extracted a correct answer from answer hints provided by the user in dialogs annotated as correctly answered.

#### Relevance 83

Label: 0

#### Passage 86

Retrieved by: BM25, Dense, Hybrid RRF

> Offline evaluation of interactive dialogs on real data is difficult because different policies can lead to different variants of the dialog. Our solution to this issue is to collect data in a way that allows us to simulate all dialog variants possible according to any policy.
> 
> The dialog variants we are considering for interactive learning differ only in presence of several parts of the dialog. Therefore, we can collect dialogs containing all information used for interactive learning and omit those parts that were not requested by the policy.
> 
> We collected the dataset (see Section "Dataset Collection Process" ) that enables simulation where the policy can decide how much extra information to the question it requests. If the question is clear to the system it can attempt to answer the question without any other information. It can also ask for a broader explanation with a possibility to answer the question afterwards. If the system decides not to answer the question, we can simulate rerouting the question to another user, to try to obtain the answer from them. The principle of simulated user's answer is shown in the Figure 1 .
> 
> Note that the simulated user’s answer can be incorrect because human users naturally made mistakes. We intentionally keep these mistakes in the dataset because real systems must address them as well.

#### Relevance 86

Label: 1

#### Passage 87

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The collection system needs to recognize following dialog acts from user utterances during all phases of the dialog:
> 
> – user does not want to provide requested information,
> 
> – user agrees to provide requested information,
> 
> – user does not know the requested information,
> 
> – user tries chit chat with the system (hello, bye, who are you...),
> 
> – none of the above, interpreted as user is giving information requested by the system.
> 
> Parsing of the dialog acts is made by hand written rules using templates and keyword spotting. The templates and keywords were manually collected from frequent expressions used by CF workers during preparation runs of the dataset collection process (google it, check wikipedia, I would need... $\rightarrow $ Negate).

#### Relevance 87

Label: 1

#### Passage 88

Retrieved by: Dense, Hybrid RRF

> A perfect data collection scenario for our dataset would use real running dialog system providing general information from the knowledge base to real users. This system could then ask for explanations and answers for questions which it is not able to answer.
> 
> However, getting access to systems with real users is usually hard. Therefore, we used the crowdsourcing platform CrowdFlower (CF) for our data collection.
> 
> A CF worker gets a task instructing them to use our chat-like interface to help the system with a question which is randomly selected from training examples of Simple questions BIBREF7 dataset. To complete the task user has to communicate with the system through the three phase dialog discussing question paraphrase (see Section "Interactive Learning Evaluation" ), explanation (see Section "Future Work" ) and answer of the question (see Section "Conclusion" ). To avoid poor English level of dialogs we involved CF workers from English speaking countries only. The collected dialogs has been annotated (see Section "Acknowledgments" ) by expert annotators afterwards.
> 
> The described procedure leads to dialogs like the one shown in the Figure 2 .

#### Relevance 88

Label: 1

### BM25

#### Passage 84

Retrieved by: BM25

> This work was funded by the Ministry of Education, Youth and Sports of the Czech Republic under the grant agreement LK11221 and core research funding, SVV project 260 224, and GAUK grant 1170516 of Charles University in Prague. It used language resources stored and distributed by the LINDAT/CLARIN project of the Ministry of Education, Youth and Sports of the Czech Republic (project LM2015071).

#### Relevance 84

Label: 0

#### Passage 85

Retrieved by: BM25

> In this paper, we presented a novel way how to evaluate different interactive learning approaches for dialog models. The evaluation covers two challenging aspects of interactive learning. First, it scores efficiency of using information gained from users in simulated question answering dialogs. Second, it measures accuracy on answer hints understanding.
> 
> For purposes of evaluation we collected a dataset from conversational dialogs with workers on crowdsourcing platform CrowdFlower. Those dialogs were annotated with expert annotators and published under Creative Commons 4.0 BY-SA license on lindat. We also provide evaluation scripts with the dataset that should ensure comparable evaluation of different interactive learning approaches.

#### Relevance 85

Label: 1

### Dense

#### Passage 89

Retrieved by: Dense

> Our future work will be mainly focused on providing a baseline system for interactive learning which will be evaluated on the dataset. We are also planning improvements for dialog management that is used to gain explanations during the data collection. We believe that with conversation about specific aspects of the discussed question it will be possible to gain even more interesting information from users. The other area of our interest is in possibilities to improve question answering accuracy on test questions of Simple question dataset with the extra information contained in the collected dialogs.

#### Relevance 89

Label: 0

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 90

Retrieved by: Hybrid RRF followed by BGE reranking

> The correct answer for question in each dialog is available from Simple questions dataset. Answers are in form of Freebase entities identified by unique id. For evaluation purposes we need information whether dialog contains the answer which is consistent with the entity from Simple questions, the answer with another entity or whether the dialog does not contain any answer. While the annotation process is quite simple, we did not need crowdsourcing for the process.

#### Relevance 90

Label: 1

#### Passage 91

Retrieved by: Hybrid RRF followed by BGE reranking

> With the valid explanation the dialog turns into the last phase where the user is asked for a correct answer to the original question. The system requires the user to answer with a full sentence. In practical experiments this has shown as a useful decision because it improves system's ability to reveal cheaters. We can simply measure the connection (in terms of common words ) between question and the answer sentence. This allows to reject completely irrelevant answers.

#### Relevance 91

Label: 1

#### Passage 92

Retrieved by: Hybrid RRF followed by BGE reranking

> At beginning of the dialog, the system is requesting the user to paraphrase question that the system does not understand. The main goal of this first phase is to let the user get familiar with the presented question and to get alternative wordings of the posed question.

#### Relevance 92

Label: 1

## Question 0011

Paper: TexTrolls: Identifying Russian Trolls on Twitter from a Textual Perspective

> What unsupervised approach was used to deduce the thematic information?

### Common Retrieved Chunks

#### Passage 93

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> detect them. We aim to answer three research questions: RQ1. Does the thematic information improve the detection performance?, RQ2. Can we detect IRA trolls from only a textual perspective? and RQ3. How IRA campaign utilized the emotions to affect the public opinions?
> 
> The rest of the paper is structured as follows. In the following section, we present an overview on the literature work on IRA trolls. In Section SECREF3, we describe how the used dataset was compiled. Section SECREF4 describes our proposed features for our approach. The experiments, results, and analyses are presented in Section SECREF5. Finally, we draw some conclusions and discuss possible future work on IRA trolls.

#### Relevance 93

Label: 0

#### Passage 94

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Given that the Emotions features boosted the F1$_{macro}$ with the highest value comparing to the other theme-based features, in Figure FIGREF34 we analyze IRA trolls from emotional perspective to answer RQ3. The analysis shows that the themes that were used to attack immigrants (Black People and Islam and War) have the fear emotion in their top two emotions. While on the other hand, a theme like Supporting Trump has a less amount of fear emotion, and the joy emotion among the top emotions.
> 
> Why do the thematic information help? The Flip-Flop behavior. As an example, let's considering the fear and joy emotions in Figure FIGREF34. We can notice that all the themes that used to nudge the division issues have a decreasing dashed line, where others such as Supporting Trump theme has an extremely increasing dashed line. Therefore, we manually analyzed the tweets of some IRA accounts and we found this observation clear, as an example from user $x$:
> 
> Islam and War: (A) @RickMad: Questions are a joke, a Muslim asks how SHE will be protected from Islamaphobia! Gmaffb! How will WE be protected from terrori…
> 
> Supporting Trump: (B) @realDonaldTrump: That was really exciting. Made all of my points. MAKE AMERICA GREAT AGAIN!
> 
> Figure FIGREF35 shows the flipping behaviour for user $x$ by extracting the mean value of the fear and joy emotions. The smaller difference between the fear and joy emotions in the Islam and War theme for this user is due to the ironic way of tweeting for the user (e.g. the beginning of tweet A: "Questions are a joke"). Even though, the fear emotion is still superior to the joy. We notice a similar pattern in some of the regular users, although much more evident among IRA trolls.
> 
> To understand more the NLI features performance, given their high performance comparing to the other features, we extract the top important tokens for each of the NLI feature subsets (see Figure FIGREF37). Some of the obtained results confirmed what was found previously. For instance, the authors in BIBREF19 found that Russians write English tweets with more prepositions comparing to native speakers of other languages (e.g. as, about, because in (c) Stop-words and RP in

#### Relevance 94

Label: 0

#### Passage 95

Retrieved by: BM25, Dense, Hybrid RRF

> In this work, we present a textual approach to detect social media trolls, namely IRA accounts. Due to the anonymity characteristic that social media provide to users, these kinds of suspicious behavioural accounts have started to appear. We built a new machine learning model based on theme-based and profiling features that in cross-validation evaluation achieved a F1$_{macro}$ value of 0.94. We applied a topic modeling algorithm to go behind the superficial textual information of the tweets. Our experiments showed that the extracted themes boosted the performance of the proposed model when coupled with other surface text features. In addition, we proposed NLI features to identify IRA trolls from their writing style, which showed to be very effective. Finally, for a better understanding we analyzed the IRA accounts from emotional and linguistic perspectives.
> 
> Through the manually checking of IRA accounts, we noticed that frequently irony was employed. As a future work, it would be interesting to identify these accounts by integrating an irony detection module.

#### Relevance 95

Label: 1

#### Passage 97

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Table TABREF32 presents the classification results showing the performance of each feature set independently. Generally, we can see that the thematic information improves the performance of the proposed features clearly (RQ1), and with the largest amount in the Emotions features (see $-_{themes}$ and $+_{themes}$ columns). This result emphasizes the importance of the thematic information. Also, we see that the emotions performance increases with the largest amount considering F1$_{macro}$ value; this motivates us to analyze the emotions in IRA tweets (see the following section).
> 
> The result of the NLI feature in the table is interesting; we are able to detect IRA trolls from their writing style with a F1$_{macro}$ value of 0.91. Considering the results in Table TABREF32, we can notice that we are able to detect the IRA trolls effectively using only textual features (RQ2).
> 
> Finally, the baselines results show us that the Network features do not perform well. A previous work BIBREF3 showed that IRA trolls tend to follow a lot of users, and nudging other users to follow them (e.g. by writing "follow me" in their profile description) to fuse their identity (account information) with the regular users. Finally, similar to the Network features, the Tweet2vec baseline performs poorly. This indicates that, although IRA trolls used the hashtag game extensively in their tweets, the Tweet2vec baseline is not able to identify them.

#### Relevance 97

Label: 0

#### Passage 98

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> Previous works BIBREF7 have investigated IRA campaign efforts on Facebook, and they found that IRA pages have posted more than $\sim $80K posts focused on division issues in US. Later on, the work in BIBREF2 has analyzed Facebook advertised posts by IRA and they specified the main themes that these advertisements discussed. Given the results of the previous works, we applied a topic modeling technique on our dataset to extract its main themes. We aim to detect IRA trolls by identifying their suspicious ideological changes across a set of themes.
> 
> Given our dataset, we applied Latent Dirichlet Allocation (LDA) topic modeling algorithm BIBREF8 on the tweets after a prepossessing step where we maintained only nouns and proper nouns. In addition, we removed special characters (except HASH "#" sign for the hashtags) and lowercase the final tweet. To ensure the quality of the themes, we removed the hashtags we used in the collecting process where they may bias the modeling algorithm. We tested multiple number of themes and we chose seven of them. We manually observed the content of these themes to label them. The extracted themes are: Police shootings, Islam and War, Supporting Trump, Black People, Civil Rights, Attacking Hillary, and Crimes. In some themes, like Supporting Trump and Attacking Hillary, we found contradicted opinions, in favor and against the main themes, but we chose the final stance based on the most representative hashtags and words in each of them (see Figure FIGREF11). Also, the themes Police Shooting and Crimes are similar, but we found that some words such as: police, officers, cops, shooting, gun, shot, etc. are the most discriminative between these two themes. In addition, we found that the Crimes theme focuses more on raping crimes against children and women. Our resulted themes are generally consistent with the ones obtained from the Facebook advertised posts in BIBREF2, and this emphasizes that IRA efforts organized in a similar manner in both social media platforms.
> 
> Based on our thematic information, we model the users textual features w.r.t. each of these themes. In other words, we model a set of textual features independently for each of the former themes to capture the emotional, stance, and others

#### Relevance 98

Label: 1

#### Passage 99

Retrieved by: Dense, Hybrid RRF

> Based on our thematic information, we model the users textual features w.r.t. each of these themes. In other words, we model a set of textual features independently for each of the former themes to capture the emotional, stance, and others changes in the users tweets.
> 
> For the theme-based features, we use the following features that we believe that they change based on the themes:
> 
> Emotions: Since the results of the previous works BIBREF2, BIBREF7 showed that IRA efforts engineered to seed discord among individuals in US, we use emotions features to detect their emotional attempts to manipulate the public opinions (e.g. fear spreading behavior). For that, we use the NRC emotions lexicon BIBREF9 that contains $\sim $14K words labeled using the eight Plutchik's emotions.
> 
> Sentiment: We extract the sentiment of the tweets from NRC BIBREF9, positive and negative.
> 
> Bad & Sexual Cues: During the manual analysis of a sample from IRA tweets, we found that some users use bad slang word to mimic the language of a US citizen. Thus, we model the presence of such words using a list of bad and sexual words from BIBREF10.
> 
> Stance Cues: Stance detection has been studied in different contexts to detect the stance of a tweet reply with respect to a main tweet/thread BIBREF11. Using this feature, we aim to detect the stance of the users regarding the different topics we extracted. To model the stance we use a set of stance lexicons employed in previous works BIBREF12, BIBREF13. Concretely, we focus on the following categories: belief, denial, doubt, fake, knowledge, negation, question, and report.
> 
> Bias Cues: We rely on a set of lexicons to capture the bias in text. We model the presence of the words in one of the following cues categories: assertives verbs BIBREF14, bias BIBREF15, factive verbs BIBREF16, implicative verbs BIBREF17, hedges BIBREF18, report verbs BIBREF15. A previous work has used these bias cues to identify bias in suspicious news posts in Twitter BIBREF19.
> 
> LIWC: We use a set of linguistic categories from the LIWC linguistic dictionary BIBREF20. The used categories are: pronoun, anx, cogmech, insight, cause, discrep, tentat, certain, inhib, incl.
> 
> Morality: Cues based on the morality foundation theory BIBREF21 where words

#### Relevance 99

Label: 0

### BM25

#### Passage 96

Retrieved by: BM25

> the obtained results confirmed what was found previously. For instance, the authors in BIBREF19 found that Russians write English tweets with more prepositions comparing to native speakers of other languages (e.g. as, about, because in (c) Stop-words and RP in (a) POS in Figure FIGREF37). Further research must be conducted to investigate in depth the rest of the results.
> 
> Linguistic Analysis. We measure statistically significant differences in the cues markers of Morality, LIWC, Bias and Subjectivity, Stance, and Bad and Sexual words across IRA trolls and regular users. These findings presented in Table TABREF38 allows for a deeper understanding of IRA trolls.
> 
> False Positive Cases. The proposed features showed to be effective in the classification process. We are interested in understanding the causes of misclassifying some of IRA trolls. Therefore, we manually investigated the false positive tweets and we found that there are three main reasons: 1) Some trolls were tweeting in a questioning way by asking about general issues; we examined their tweets but we did not find a clear ideological orientation or a suspicious behaviour in their tweets. 2) Some accounts were sharing traditional social media posts (e.g. "http://t.co/GGpZMvnEAj cat vs trashcan"); the majority of the false positive IRA trolls are categorized under this reason. In addition, these posts were given a false theme name; the tweet in the previous example assigned to Attacking Hillary theme. 3) Lack of content. Some of the misclassified trolls mention only external links without a clear textual content. This kind of trolls needs a second step to investigate the content of the external links. Thus, we tried to read the content of these links but we found that the majority of them referred to deleted tweets. Probably this kind of accounts was used to "raise the voice" of other trolls, as well as, we argue that the three kinds of IRA trolls were used for "likes boosting".

#### Relevance 96

Label: 0

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 100

Retrieved by: Hybrid RRF followed by BGE reranking

> Recent years have seen a large increase in the amount of disinformation and fake news spread on social media. False information was used to spread fear and anger among people, which in turn, provoked crimes in some countries. The US in the recent years experienced many similar cases during the presidential elections, such as the one commonly known as “Pizzagate" . Later on, Twitter declared that they had detected a suspicious campaign originated in Russia by an organization named Internet Research Agency (IRA), and targeted the US to affect the results of the 2016 presidential elections. The desired goals behind these accounts are to spread fake and hateful news to further polarize the public opinion. Such attempts are not limited to Twitter, since Facebook announced in mid-2019 that they detected a similar attempt originating from UAE, Egypt and Saudi Arabia and targeting other countries such as Qatar, Palestine, Lebanon and Jordan. This attempt used Facebook pages, groups, and user accounts with fake identities to spread fake news supporting their ideological agendas. The automatic detection of such attempts is very challenging, since the true identity of these suspicious accounts is hidden by imitating the profiles of real persons from the targeted audience; in addition, sometimes they publish their suspicious idea in a vague way through their tweets' messages.
> 
> A previous work BIBREF0 showed that such suspicious accounts are not bots in a strict sense and they argue that they could be considered as “software-assisted human workers". According to BIBREF1, the online suspicious accounts can be categorized into 3 main types: Robots, Cyborgs, and Human Spammers. We consider IRA accounts as another new emerging type called trolls, which is similar to Cyborgs except that the former focuses on targeting communities instead of individuals.
> 
> In this work, we identify online trolls in Twitter, namely IRA trolls, from a textual perspective. We study the effect of a set of text-based features and we propose a machine learning model to detect them. We aim to answer three research questions: RQ1. Does the thematic information improve the detection performance?, RQ2. Can we detect IRA trolls from only a textual perspective? and RQ3. How IRA campaign utilized the emotions to affect the

#### Relevance 100

Label: 0

## Question 0012

Paper: Character-Level Question Answering with Attention

> What word level and character level model baselines are used?

### Common Retrieved Chunks

#### Passage 101

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Our work is motivated by three major threads of research in machine learning and natural language processing: semantic-parsing for open-domain question answering, character-level language modeling, and encoder-decoder methods.
> 
> Semantic parsing for open-domain question answering, which translates a question into a structured KB query, is a key component in question answering with a KB. While early approaches relied on building high-quality lexicons for domain-specific databases such as GeoQuery BIBREF7 , recent work has focused on building semantic parsing frameworks for general knowledge bases such as Freebase BIBREF1 , BIBREF8 , BIBREF0 , BIBREF9 , BIBREF2 .
> 
> Semantic parsing frameworks for large-scale knowledge bases have to be able to successfully generate queries for the millions of entities and thousands of predicates in the KB, many of which are unseen during training. To address this issue, recent work relies on producing embeddings for predicates and entities in a KB based on their textual descriptions BIBREF8 , BIBREF0 , BIBREF1 , BIBREF10 . A general interaction function can then be used to measure the semantic relevance of these embedded KB entries to the question and determine the most likely KB query.
> 
> Most of these approaches use word-level embeddings to encode entities and predicates, and therefore might suffer from the out-of-vocabulary (OOV) problem when they encounter unseen words during test time. Consequently, they often rely on significant data augmentation from sources such as Paralex BIBREF2 , which contains 18 million question-paraphrase pairs scraped from WikiAnswers, to have sufficient examples for each word they encounter BIBREF11 , BIBREF1 , BIBREF0 .
> 
> As opposed to word-level modeling, character-level modeling can be used to handle the OOV issue. While character-level modeling has not been applied to factoid question answering before, it has been successfully applied to information retrieval, machine translation, sentiment analysis, classification, and named entity recognition BIBREF12 , BIBREF13 , BIBREF6 , BIBREF14 , BIBREF15 , BIBREF16 , BIBREF17 , BIBREF18 , BIBREF19 . Moreover, gflstm demonstrate that gated-feedback LSTMs on top of character-level embeddings can capture long-term dependencies in language modeling.
> 
> Lastly, encoder-decoder networks have been applied to many structured machine learning tasks. First introduced in sutskever2014sequence, in an encoder-decoder network, a source sequence is first encoded with a recurrent neural

#### Relevance 101

Label: 0

#### Passage 103

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> We evaluate the proposed model on the SimpleQuestions dataset BIBREF0 . The dataset consists of 108,442 single-relation questions and their corresponding (topic entity, predicate, answer entity) triples from Freebase. It is split into 75,910 train, 10,845 validation, and 21,687 test questions. Only 10,843 of the 45,335 unique words in entity aliases and 886 out of 1,034 unique predicates in the test set were present in the train set. For the proposed dataset, there are two evaluation settings, called FB2M and FB5M, respectively. The former uses a KB for candidate generation which is a subset of Freebase and contains 2M entities, while the latter uses subset of Freebase with 5M entities.
> 
> In our experiments, the Memory Neural Networks (MemNNs) proposed in babidataset serve as the baselines. For training, in addition to the 76K questions in the training set, the MemNNs use 3K training questions from WebQuestions BIBREF27 , 15M paraphrases from WikiAnswers BIBREF2 , and 11M and 12M automatically generated questions from the KB for the FB2M and FB5M settings, respectively. In contrast, our models are trained only on the 76K questions in the training set.
> 
> For our model, both layers of the LSTM-based question encoder have size 200. The hidden layers of the LSTM-based decoder have size 100, and the CNNs for entity and predicate embeddings have a hidden layer of size 200 and an output layer of size 100. The CNNs for entity and predicate embeddings use a receptive field of size 4, $\lambda =5$ , and $m=100$ . We train the models using RMSProp with a learning rate of $1e^{-4}$ .
> 
> In order to make the input character sequence long enough to fill up the receptive fields of multiple CNN layers, we pad each predicate or entity using three padding symbols $P$ , a special start symbol, and a special end symbol. For instance, $Obama$ would become $S_{start}PPP ObamaPPPS_{end}$ . For consistency, we apply the same padding to the questions.

#### Relevance 103

Label: 1

#### Passage 104

Retrieved by: BM25, Hybrid RRF

> We randomly sampled 50 questions where the best-performing model generated the wrong KB query and categorized the errors. For 46 out of the 50 examples, the model predicted a predicate with a very similar alias to the true predicate, i.e. /music/release/track vs. /music/release/track_list. For 21 out of the 50 examples, the model predicted the wrong entity, e.g., Album vs. Still Here for the question What type of album is still here?. Finally, for 18 of the 50 examples, the model predicted the wrong entity and predicate, i.e. (Play, /freebase/equivalent_topic/equivalent_type) for the question which instrument does amapola cabase play? Training on more data, augmenting the negative sample set with words from the question that are not an entity mention, and having more examples that disambiguate between similar predicates may ameliorate many of these errors.

#### Relevance 104

Label: 0

#### Passage 105

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Following babidataset, we report results on the SimpleQuestions dataset in terms of SQ accuracy, for both FB2M and FB5M settings in Table 1. SQ accuracy is defined as the percentage of questions for which the model generates a correct KB query (i.e., both the topic entity and predicate are correct). Our single character-level model achieves SQ accuracies of 70.9% and 70.3% on the FB2M and FB5M settings, outperforming the previous state-of-art results by 8.2% and 6.4%, respectively. Compared to the character-level model, which only has 1.2M parameters, our word-level model has 19.9M parameters, and only achieves a best SQ accuracy of 53.9%. In addition, in contrast to previous work, the OOV issue is much more severe for our word-level model, since we use no data augmentation to cover entities unseen in the train set.

#### Relevance 105

Label: 1

#### Passage 106

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We carry out ablation studies in Sections 5.2.1 and 5.2.2 through a set of random-sampling experiments. In these experiments, for each question, we randomly sample 200 entities and predicates from the test set as noise samples. We then mix the gold entity and predicate into these negative samples, and evaluate the accuracy of our model in predicting the gold predicate or entity from this mixed set.
> 
> We first explore using word-level models as an alternative to character-level models to construct embeddings for questions, entities and predicates.
> 
> Both word-level and character-level models perform comparably well when predicting the predicate, reaching an accuracy of around 80% (Table 3). However, the word-level model has considerable difficulty generalizing to unseen entities, and is only able to predict 45% of the entities accurately from the mixed set. These results clearly demonstrate that the OOV issue is much more severe for entities than predicates, and the difficulty word-level models have when generalizing to new entities.
> 
> In contrast, character-level models have no such issues, and achieve a 96.6% accuracy in predicting the correct entity on the mixed set. This demonstrates that character-level models encode the semantic representation of entities and can match entity aliases in a KB with their mentions in natural language questions.
> 
> We also study the impact of the depth of neural networks in our model. The results are presented in Table 2. In the ablation experiments we compare the performance of a single-layer LSTM to a two-layer LSTM to encode the question, and a single-layer vs. two-layer CNN to encode the KB entries. We find that a two-layer LSTM boosts joint accuracy by over 6%. The majority of accuracy gains are a result of improved predicate predictions, possibly because entity accuracy is already saturated in this experimental setup.

#### Relevance 106

Label: 1

#### Passage 107

Retrieved by: Dense, Hybrid RRF

> In order to further understand how the model performs question answering, we visualize the attention distribution over question characters in the decoding process. In each sub-figure of Figure 2, the x-axis is the character sequence of the question, and the y-axis is the attention weight distribution $\lbrace \alpha _i\rbrace $ . The blue curve is the attention distribution when generating the entity, and green curve is the attention distribution when generating the predicate.
> 
> Interestingly, as the examples show, the attention distribution typically peaks at empty spaces. This indicates that the character-level model learns that a space defines an ending point of a complete linguistic unit. That is, the hidden state of the LSTM encoder at a space likely summarizes content about the character sequence before that space, and therefore contains important semantic information that the decoder needs to attend to.
> 
> Also, we observe that entity attention distributions are usually less sharp and span longer portions of words, such as john or rutters, than predicate attention distributions (e.g., Figure 2a). For entities, semantic information may accumulate gradually when seeing more and more characters, while for predicates, semantic information will become clear only after seeing the complete word. For example, it may only be clear that characters such as song by refer to a predicate after a space, as opposed to the name of a song such as song bye bye love (Figures 2a, 2b). In contrast, a sequence of characters starts to become a likely entity after seeing an incomplete name such as joh or rutt.
> 
> In addition, a character-level model can identify entities whose English aliases were never seen in training, such as phrenology (Figure 2d). The model apparently learns that words ending with the suffix nology are likely entity mentions, which is interesting because it reads in the input one character at a time.
> 
> Furthermore, as observed in Figure 2d, the attention model is capable of attending disjoint regions of the question and capture the mention of a predicate that is interrupted by entity mentions. We also note that predicate attention often peaks at the padding symbols after the last character of the question, possibly because sentence endings carry extra information that further help

#### Relevance 107

Label: 0

#### Passage 109

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> Single-relation factoid questions are the most common form of questions found in search query logs and community question answering websites BIBREF1 , BIBREF2 . A knowledge-base (KB) such as Freebase, DBpedia, or Wikidata can help answer such questions after users reformulate them as queries. For instance, the question Where was Barack Obama born? can be answered by issuing the following KB query: $
> \lambda (x).place\_of\_birth(Barack\_Obama, x)
> $
> 
> However, automatically mapping a natural language question such as Where was Barack Obama born? to its corresponding KB query remains a challenging task.
> 
> There are three key issues that make learning this mapping non-trivial. First, there are many paraphrases of the same question. Second, many of the KB entries are unseen during training time; however, we still need to correctly predict them at test time. Third, a KB such as Freebase typically contains millions of entities and thousands of predicates, making it difficult for a system to predict these entities at scale BIBREF1 , BIBREF3 , BIBREF0 . In this paper, we address all three of these issues with a character-level encoder-decoder framework that significantly improves performance over state-of-the-art word-level neural models, while also providing a much more compact model that can be learned from less data.
> 
> First, we use a long short-term memory (LSTM) BIBREF4 encoder to embed the question. Second, to make our model robust to unseen KB entries, we extract embeddings for questions, predicates and entities purely from their character-level representations. Character-level modeling has been previously shown to generalize well to new words not seen during training BIBREF5 , BIBREF6 , which makes it ideal for this task. Third, to scale our model to handle the millions of entities and thousands of predicates in the KB, instead of using a large output layer in the decoder to directly predict the entity and predicate, we use a general interaction function between the question embeddings and KB embeddings that measures their semantic relevance to determine the output. The combined use of character-level modeling and a semantic relevance function allows us to successfully produce likelihood scores for the KB entries that are not present in our vocabulary, a challenging task for standard encoder-decoder frameworks.
> 
> Our novel, character-level encoder-decoder

#### Relevance 109

Label: 0

### BM25

#### Passage 102

Retrieved by: BM25

> the mention of a predicate that is interrupted by entity mentions. We also note that predicate attention often peaks at the padding symbols after the last character of the question, possibly because sentence endings carry extra information that further help disambiguate predicate mentions. In certain scenarios, the network may only have sufficient information to build a semantic representation of the predicate after being ensured that it reached the end of a sentence. Finally, certain words in the question help identify both the entity and the predicate. For example, consider the word university in the question What type of educational institution is eastern new mexico university (Figure 2c). Although it is a part of the entity mention, it also helps disambiguate the predicate. However, previous semantic parsing-based QA approaches BIBREF10 , BIBREF1 assume that there is a clear separation between the predicate and entity mentions in the question. In contrast, the proposed model does not need to make this hard categorization, and attends the word university when predicting both the entity and predicate.

#### Relevance 102

Label: 0

### Dense

#### Passage 108

Retrieved by: Dense

> The combined use of character-level modeling and a semantic relevance function allows us to successfully produce likelihood scores for the KB entries that are not present in our vocabulary, a challenging task for standard encoder-decoder frameworks.
> 
> Our novel, character-level encoder-decoder model is compact, requires significantly less data to train than previous work, and is able to generalize well to unseen entities in test time. In particular, without use of ensembles, we achieve 70.9% accuracy in the Freebase2M setting and 70.3% accuracy in the Freebase5M setting on the SimpleQuestions dataset, outperforming the previous state-of-arts of 62.7% and 63.9% BIBREF0 by 8.2% and 6.4% respectively. Moreover, we only use the training questions provided in SimpleQuestions to train our model, which cover about 24% of words in entity aliases on the test set. This demonstrates the robustness of the character-level model to unseen entities. In contrast, data augmentation is usually necessary to provide more coverage for unseen entities and predicates, as done in previous work BIBREF0 , BIBREF1 .

#### Relevance 108

Label: 0

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0013

Paper: Deep Learning the EEG Manifold for Phonological Categorization from Active Thoughts

> How was the spatial aspect of the EEG signal computed?

### Common Retrieved Chunks

#### Passage 110

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Decoding intended speech or motor activity from brain signals is one of the major research areas in Brain Computer Interface (BCI) systems BIBREF0 , BIBREF1 . In particular, speech-related BCI technologies attempt to provide effective vocal communication strategies for controlling external devices through speech commands interpreted from brain signals BIBREF2 . Not only do they provide neuro-prosthetic help for people with speaking disabilities and neuro-muscular disorders like locked-in-syndrome, nasopharyngeal cancer, and amytotropic lateral sclerosis (ALS), but also equip people with a better medium to communicate and express thoughts, thereby improving the quality of rehabilitation and clinical neurology BIBREF3 , BIBREF4 . Such devices also have applications in entertainment, preventive treatments, personal communication, games, etc. Furthermore, BCI technologies can be utilized in silent communication, as in noisy environments, or situations where any sort of audio-visual communication is infeasible.
> 
> Among the various brain activity-monitoring modalities in BCI, electroencephalography (EEG) BIBREF5 , BIBREF6 has demonstrated promising potential to differentiate between various brain activities through measurement of related electric fields. EEG is non-invasive, portable, low cost, and provides satisfactory temporal resolution. This makes EEG suitable to realize BCI systems. EEG data, however, is challenging: these data are high dimensional, have poor SNR, and suffer from low spatial resolution and a multitude of artifacts. For these reasons, it is not particularly obvious how to decode the desired information from raw EEG signals. Although the area of BCI based speech intent recognition has received increasing attention among the research community in the past few years, most research has focused on classification of individual speech categories in terms of discrete vowels, phonemes and words BIBREF7 , BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 , BIBREF13 , BIBREF14 , BIBREF15 . This includes categorization of imagined EEG signal into binary vowel categories like /a/, /u/ and rest BIBREF7 , BIBREF8 , BIBREF9 ; binary syllable classes like /ba/ and /ku/ BIBREF1 , BIBREF10 , BIBREF11 , BIBREF12 ; a handful of control words like 'up', 'down', 'left', 'right' and 'select' BIBREF15 or others like 'water', 'help', 'thanks', 'food', 'stop' BIBREF13 , Chinese characters BIBREF14 , etc. Such works mostly involve traditional signal processing or manual feature handcrafting along with linear classifiers

#### Relevance 110

Label: 0

#### Passage 111

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> control words like 'up', 'down', 'left', 'right' and 'select' BIBREF15 or others like 'water', 'help', 'thanks', 'food', 'stop' BIBREF13 , Chinese characters BIBREF14 , etc. Such works mostly involve traditional signal processing or manual feature handcrafting along with linear classifiers (e.g., SVMs). In our recent work BIBREF16 , we introduced deep learning models for classification of vowels and words that achieved 23.45% improvement of accuracy over the baseline.
> 
> Production of articulatory speech is an extremely complicated process, thereby rendering understanding of the discriminative EEG manifold corresponding to imagined speech highly challenging. As a result, most of the existing approaches failed to achieve satisfactory accuracy on decoding speech tokens from the speech imagery EEG data. Perhaps, for these reasons, very little work has been devoted to relating the brain signals to the underlying articulation. The few exceptions include BIBREF17 , BIBREF18 . In BIBREF17 , Zhao et al. used manually handcrafted features from EEG data, combined with speech audio and facial features to achieve classification of the phonological categories varying based on the articulatory steps. However, the imagined speech classification accuracy based on EEG data alone, as reported in BIBREF17 , BIBREF18 , are not satisfactory in terms of accuracy and reliability. We now turn to describing our proposed models.

#### Relevance 111

Label: 0

#### Passage 112

Retrieved by: BM25, Hybrid RRF

> second set of features are more easily separable than the first one, thereby giving a rationale for our performance.
> 
> Next, we provide performance comparison of the proposed approach with the baseline methods for PHASE-TWO of our study (cross-validation experiment) in Table TABREF15 . Since the model encounters the unseen data of a new subject for testing, and given the high inter-subject variability of the EEG data, a reduction in the accuracy was expected. However, our network still managed to achieve an improvement of 18.91, 9.95, 67.15, 2.83 and 13.70 % over BIBREF17 . Besides, our best model shows more reliability compared to previous works: The standard deviation of our model's classification accuracy across all the tasks is reduced from 22.59% BIBREF17 and 17.52% BIBREF18 to a mere 5.41%.

#### Relevance 112

Label: 0

#### Passage 113

Retrieved by: BM25, Dense, Hybrid RRF

> We performed two sets of experiments with the single-trial EEG data. In PHASE-ONE, our goals was to identify the best architectures and hyperparameters for our networks with a reasonable number of runs. For PHASE-ONE, we randomly shuffled and divided the data (1913 signals from 14 individuals) into train (80%), development (10%) and test sets (10%). In PHASE-TWO, in order to perform a fair comparison with the previous methods reported on the same dataset, we perform a leave-one-subject out cross-validation experiment using the best settings we learn from PHASE-ONE.
> 
> The architectural parameters and hyperparameters listed in Table TABREF6 were selected through an exhaustive grid-search based on the validation set of PHASE-ONE. We conducted a series of empirical studies starting from single hidden-layered networks for each of the blocks and, based on the validation accuracy, we increased the depth of each given network and selected the optimal parametric set from all possible combinations of parameters. For the gradient boosting classification, we fixed the maximum depth at 10, number of estimators at 5000, learning rate at 0.1, regularization coefficient at 0.3, subsample ratio at 0.8, and column-sample/iteration at 0.4. We did not find any notable change of accuracy while varying other hyperparameters while training gradient boost classifier.

#### Relevance 113

Label: 0

#### Passage 114

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> As we found the individually-trained parallel networks (CNN and LSTM) to be useful (see Table TABREF12 ), we suspected the combination of these two networks could provide a more powerful discriminative spatial and temporal representation of the data than each independent network. As such, we concatenate the last fully-connected layer from the CNN with its counterpart in the LSTM to compose a single feature vector based on these two penultimate layers. Ultimately, this forms a joint spatio-temporal encoding of the cross-covariance matrix.
> 
> In order to further reduce the dimensionality of the spatio-temporal encodings and cancel background noise effects BIBREF21 , we train an unsupervised deep autoenoder (DAE) on the fused heterogeneous features produced by the combined CNN and LSTM information. The DAE forms our second level of hierarchy, with 3 encoding and 3 decoding layers, and mean squared error (MSE) as the cost function.

#### Relevance 114

Label: 1

#### Passage 115

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Multichannel EEG data is high dimensional multivariate time series data whose dimensionality depends on the number of electrodes. It is a major hurdle to optimally encode information from these EEG data into lower dimensional space. In fact, our investigation based on a development set (as we explain later) showed that well-known deep neural networks (e.g., fully connected networks such as convolutional neural networks, recurrent neural networks and autoencoders) fail to individually learn such complex feature representations from single-trial EEG data. Besides, we found that instead of using the raw multi-channel high-dimensional EEG requiring large training times and resource requirements, it is advantageous to first reduce its dimensionality by capturing the information transfer among the electrodes. Instead of the conventional approach of selecting a handful of channels as BIBREF17 , BIBREF18 , we address this by computing the channel cross-covariance, resulting in positive, semi-definite matrices encoding the connectivity of the electrodes. We define channel cross-covariance (CCV) between any two electrodes INLINEFORM0 and INLINEFORM1 as: INLINEFORM2 . Next, we reject the channels which have significantly lower cross-covariance than auto-covariance values (where auto-covariance implies CCV on same electrode). We found this measure to be essential as the higher cognitive processes underlying speech planning and synthesis involve frequent information exchange between different parts of the brain. Hence, such matrices often contain more discriminative features and hidden information than mere raw signals. This is essentially different than our previous work BIBREF16 where we extract per-channel 1-D covariance information and feed it to the networks. We present our sample 2-D EEG cross-covariance matrices (of two individuals) in Fig. FIGREF2 .

#### Relevance 115

Label: 1

#### Passage 117

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> Cognitive learning process underlying articulatory speech production involves incorporation of intermediate feedback loops and utilization of past information stored in the form of memory as well as hierarchical combination of several feature extractors. To this end, we develop our mixed neural network architecture composed of three supervised and a single unsupervised learning step, discussed in the next subsections and shown in Fig. FIGREF1 . We formulate the problem of categorizing EEG data based on speech imagery as a non-linear mapping INLINEFORM0 of a multivariate time-series input sequence INLINEFORM1 to fixed output INLINEFORM2 , i.e, mathematically INLINEFORM3 : INLINEFORM4 , where c and t denote the EEG channels and time instants respectively.

#### Relevance 117

Label: 0

### BM25

None

### Dense

#### Passage 116

Retrieved by: Dense

> We follow similar pre-processing steps on raw EEG data as reported in BIBREF17 (ocular artifact removal using blind source separation, bandpass filtering and subtracting mean value from each channel) except that we do not perform Laplacian filtering step since such high-pass filtering may decrease information content from the signals in the selected bandwidth.

#### Relevance 116

Label: 0

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0014

Paper: NRC-Canada at SMM4H Shared Task: Classifying Tweets Mentioning Adverse Drug Reactions and Medication Intake

> what were the evaluation metrics?

### Common Retrieved Chunks

#### Passage 118

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> BIBREF8 , BIBREF9 A variety of features (e.g., word INLINEFORM1 -grams, word embeddings, sentiment, and topic models) as well as extensive medical resources (e.g., UMLS, lexicons of ADRs, drug lists, and lists of known drug-side effect pairs) were explored.
> 
> Task 2: Classification of Tweets for Medication Intake
> 
> Task 2 was formulated as follows: given a tweet, determine if it mentions personal medication intake, possible medication intake, or no intake is mentioned. This was a multi-class classification problem with three classes:
> 
> The official evaluation metric for this task was micro-averaged F-score of the class 1 (intake) and class 2 (possible intake): INLINEFORM0 INLINEFORM1
> 
> Information on how the data was collected and annotated was not available until after the evaluation.
> 
> Two labeled datasets were provided to the participants: a training set containing 8,000 tweets and a development set containing 2,260 tweets. As for Task 1, the training and development sets were distributed through tweet IDs and a download script. Around 95% of the tweets were accessible through download. Again, we removed duplicate and near-duplicate messages. A separate test set of 7,513 tweets was provided without labels at the evaluation period. This set was distributed to the participants, in full, by email. Table TABREF7 shows the number of instances we used for training and testing our model.
> 
> For each task, three submissions were allowed from each participating team.

#### Relevance 118

Label: 1

#### Passage 119

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Below we describe in detail the two tasks we participated in, Task 1 and Task 2.
> 
> Task 1: Classification of Tweets for Adverse Drug Reaction
> 
> Task 1 was formulated as follows: given a tweet, determine whether it mentions an adverse drug reaction. This was a binary classification task:
> 
> The official evaluation metric was the F-score for class 1 (ADR): INLINEFORM0
> 
> The data for this task was created as part of a large project on ADR detection from social media by the DIEGO lab at Arizona State University. The tweets were collected using the generic and brand names of the drugs as well as their phonetic misspellings. Two domain experts under the guidance of a pharmacology expert annotated the tweets for the presence or absence of an ADR mention. The inter-annotator agreement for the two annotators was Cohens Kappa INLINEFORM0 . BIBREF7
> 
> Two labeled datasets were provided to the participants: a training set containing 10,822 tweets and a development set containing 4,845 tweets. These datasets were distributed as lists of tweet IDs, and the participants needed to download the tweets using the provided Python script. However, only about 60–70% of the tweets were accessible at the time of download (May 2017). The training set contained several hundreds of duplicate or near-duplicate messages, which we decided to remove. Near-duplicates were defined as tweets containing mostly the same text but differing in user mentions, punctuation, or other non-essential context. A separate test set of 9,961 tweets was provided without labels at the evaluation period. This set was distributed to the participants, in full, by email. Table TABREF1 shows the number of instances we used for training and testing our model.
> 
> Task 1 was a rerun of the shared task organized in 2016. BIBREF7 The best result obtained in 2016 was INLINEFORM0 . BIBREF8 The participants in the 2016 challenge employed various statistical machine learning techniques, such as Support Vector Machines, Maximum Entropy classifiers, Random Forests, and other ensembles. BIBREF8 , BIBREF9 A variety of features (e.g., word INLINEFORM1 -grams, word embeddings, sentiment, and topic models) as well as extensive medical resources (e.g., UMLS, lexicons of ADRs, drug lists, and lists of known drug-side effect pairs) were explored.
> 
> Task

#### Relevance 119

Label: 1

#### Passage 120

Retrieved by: BM25, Dense, Hybrid RRF

> For each task, our team submitted three sets of predictions. The submissions differed in the sets of features and parameters used to train the classification models (Table TABREF32 ).
> 
> While developing the system for Task 1 we noticed that the results obtained through cross-validation on the training data were almost 13 percentage points higher than the results obtained by the model trained on the full training set and applied on the development set. This drop in performance was mostly due to a drop in precision. This suggests that the datasets had substantial differences in the language use, possibly because they were collected and annotated at separate times. Therefore, we decided to optimize the parameters and features for submission 1 and submission 2 using two different strategies. The models for the three submissions were trained as follows:
> 
> Submission 1: we randomly split the development set into 5 equal folds. We trained a classification model on the combination of four folds and the full training set, and tested the model on the remaining fifth fold of the development set. The procedure was repeated five times, each time testing on a different fold. The feature set and the classification parameters that resulted in the best INLINEFORM0 were used to train the final model.
> 
> Submission 2: the features and parameters were selected based on the performance of the model trained on the full training set and tested on the full development set.
> 
> Submission 3: we used the same features and parameters as in submission 1, except we trained an ensemble of three models, varying the class distribution in the sub-sampling procedure (1:2, 1:3, and 1:4).
> 
> For Task 2, the features and parameters were selected based on the cross-validation results run on the combination of the training and development set. We randomly split the development set into 3 equal folds. We trained a classification model on the combination of two folds and the full training set, and tested the model on the remaining third fold of the development set. The procedure was repeated three times, each time testing on a different fold. The models for the three submissions were trained as follows:
> 
> Submission 1: we used the features and parameters

#### Relevance 120

Label: 0

#### Passage 121

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> voting on the predictions of the three individual classifiers.
> 
> For Task 2 (Classification of tweets for medication intake), the provided datasets were also imbalanced but not as much as for Task 1: the class proportion in all subsets was close to 1:2:3. However, even for this task, we found some of the techniques for reducing class imbalance helpful. In particular, training an SVM classifier with different class weights improved the performance in the cross-validation experiments. These class weights are used to increase the cost of misclassification errors for the corresponding classes. The cost for a class is calculated as the generic cost parameter (parameter C in SVM) multiplied by the class weight. The best performance on the training data was achieved with class weights set to 4 for class 1 (intake), 2 for class 2 (possible intake), and 1 for class 3 (non-intake).
> 
> Preprocessing: The following pre-processing steps were performed. URLs and user mentions were normalized to http://someurl and @username, respectively. Tweets were tokenized with the CMU Twitter NLP tool. BIBREF11

#### Relevance 121

Label: 0

#### Passage 122

Retrieved by: BM25, Dense, Hybrid RRF

> on the remaining third fold of the development set. The procedure was repeated three times, each time testing on a different fold. The models for the three submissions were trained as follows:
> 
> Submission 1: we used the features and parameters that gave the best results during cross-validation.
> 
> Submission 2: we used the same features and parameters as in submission 1, but added features derived from two domain resources: the ADR lexicon and the Pronoun lexicon.
> 
> Submission 3: we used the same features as in submission 1, but changed the SVM C parameter to 0.1.
> 
> For both tasks and all submissions, the final models were trained on the combination of the full training set and full development set, and applied on the test set.

#### Relevance 122

Label: 0

#### Passage 124

Retrieved by: Dense, Hybrid RRF

> ADR Lexicon: a list of 13,699 ADR concepts compiled from COSTART, SIDER, CHV, and drug-related tweets by the DIEGO lab; BIBREF16
> 
> domain word embeddings: dense word representations generated by the DIEGO lab by applying word2vec on one million tweets mentioning medications; BIBREF16
> 
> domain word clusters: word clusters generated by the DIEGO lab using the word2vec tool to perform K-means clustering on the above mentioned domain word embeddings. BIBREF16
> 
> From these resources, the following domain-specific features were generated:
> 
> INLINEFORM0 -grams generalized over domain terms (or domain generalized INLINEFORM1 -grams, for short): INLINEFORM2 -grams where words or phrases representing a medication (from our medication list) or an adverse drug reaction (from the ADR lexicon) are replaced with <MED> INLINEFORM3 and <ADR>, respectively (e.g., <MED> INLINEFORM4 makes me);
> 
> Pronoun Lexicon features: the number of tokens from the Pronoun lexicon matched in the tweet;
> 
> domain word embeddings: the sum of the domain word embeddings for all tokens in the tweet;
> 
> domain word clusters: presence of tokens from the domain word clusters.
> 
> Sentiment Lexicon Features
> 
> We generated features using the sentiment scores provided in the following lexicons: Hu and Liu Lexicon BIBREF17 , Norms of Valence, Arousal, and Dominance BIBREF18 , labMT BIBREF19 , and NRC Emoticon Lexicon BIBREF20 . The first three lexicons were created through manual annotation while the last one, NRC Emoticon Lexicon, was generated automatically from a large collection of tweets with emoticons. The following set of features were calculated separately for each tweet and each lexicon:
> 
> the number of tokens with INLINEFORM0 ;
> 
> the total score = INLINEFORM0 ;
> 
> the maximal score = INLINEFORM0 ;
> 
> the score of the last token in the tweet.
> 
> We experimented with a number of other existing manually created or automatically generated sentiment and emotion lexicons, such as the NRC Emotion Lexicon BIBREF21 and the NRC Hashtag Emotion Lexicon BIBREF22 (http://saifmohammad.com/ WebPages/lexicons.html), but did not observe any improvement in the cross-validation experiments. None of the sentiment lexicon features were effective in the cross-validation experiments on Task 1; therefore, we did not include them in the final feature set for this task.

#### Relevance 124

Label: 0

#### Passage 125

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> embeddings, etc.) results only in slight drop or even increase in the performance (rows b.1–b.4). This indicates that the features in this group capture similar information. Among the domain-specific features, the INLINEFORM1 -grams generalized over domain terms are the most useful. The model trained without these INLINEFORM2 -grams features performs almost one percentage point worse than the model that uses all the features (row c.1). The sentiment lexicon features were not helpful (row d).
> 
> Our strategy of handling class imbalance through class weights did not prove successful on the test set (even though it resulted in increase of one point in F-measure in the cross-validation experiments). The model trained with the default class weights of 1 for all classes performs 0.7 percentage points better than the model trained with the class weights selected in cross-validation (row e).
> 
> The difference in how people can express medication intake vs. how they express that they have not taken a medication can be rather subtle. For example, the expression I need Tylenol indicates that the person has not taken the medication yet (class 3), whereas the expression I need more Tylenol indicates that the person has taken the medication (class 1). In still other instances, the word more might not be the deciding factor in whether a medication was taken or not (e.g., more Tylenol didn't help). A useful avenue of future work is to explore the role function words play in determining the semantics of a sentence, specifically, when they imply medication intake, when they imply the lack of medication intake, and when they are not relevant to determining medication intake.

#### Relevance 125

Label: 1

### BM25

None

### Dense

#### Passage 123

Retrieved by: Dense

> Task 1 (Classification of Tweets for ADR)
> 
> The results for our three official submissions are presented in Table TABREF39 (rows c.1–c.3). The best results in INLINEFORM0 were obtained with submission 1 (row c.1). The results for submission 2 are the lowest, with F-measure being 3.5 percentage points lower than the result for submission 1 (row c.2). The ensemble classifier (submission 3) shows a slightly worse performance than the best result. However, in the post-competition experiments, we found that larger ensembles (with 7–11 classifiers, each trained on a random sub-sample of the majority class to reduce class imbalance to 1:2) outperform our best single-classifier model by over one percentage point with INLINEFORM1 reaching up to INLINEFORM2 (row d). Our best submission is ranked first among the nine teams participated in this task (rows b.1–b.3).
> 
> Table TABREF39 also shows the results for two baseline classifiers. The first baseline is a classifier that assigns class 1 (ADR) to all instances (row a.1). The performance of this baseline is very low ( INLINEFORM0 ) due to the small proportion of class 1 instances in the test set. The second baseline is an SVM classifier trained only on the unigram features (row a.2). Its performance is much higher than the performance of the first baseline, but substantially lower than that of our system. By adding a variety of textual and domain-specific features as well as applying under-sampling, we are able to improve the classification performance by almost ten percentage points in F-measure.
> 
> To investigate the impact of each feature group on the overall performance, we conduct ablation experiments where we repeat the same classification process but remove one feature group at a time. Table TABREF40 shows the results of these ablation experiments for our best system (submission 1). Comparing the two major groups of features, general textual features (row b) and domain-specific features (row c), we observe that they both have a substantial impact on the performance. Removing one of these groups leads to a two percentage points drop in INLINEFORM0 . The general textual features mostly affect recall of the ADR class (row b) while the domain-specific features impact precision (row c). Among the general textual features, the most

#### Relevance 123

Label: 1

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 126

Retrieved by: Hybrid RRF followed by BGE reranking

> The classification model leverages a variety of general textual features as well as sentiment and domain-specific features described below. Many features were inspired by previous work on ADR BIBREF12 , BIBREF8 , BIBREF9 and our work on sentiment analysis (such as the winning system in the SemEval-2013 task on sentiment analysis in Twitter BIBREF13 and best performing stance detection system BIBREF14 ).
> 
> General Textual Features
> 
> The following surface-form features were used:
> 
> INLINEFORM0 -grams: word INLINEFORM1 -grams (contiguous sequences of INLINEFORM2 tokens), non-contiguous word INLINEFORM3 -grams ( INLINEFORM4 -grams with one token replaced by *), character INLINEFORM5 -grams (contiguous sequences of INLINEFORM6 characters), unigram stems obtained with the Porter stemming algorithm;
> 
> General-domain word embeddings:
> 
> dense word representations generated with word2vec on ten million English-language tweets, summed over all tokens in the tweet,
> 
> word embeddings distributed as part of ConceptNet 5.5 BIBREF15 , summed over all tokens in the tweet;
> 
> General-domain word clusters: presence of tokens from the word clusters generated with the Brown clustering algorithm on 56 million English-language tweets; BIBREF11
> 
> Negation: presence of simple negators (e.g., not, never); negation also affects the INLINEFORM0 -gram features—a term INLINEFORM1 becomes INLINEFORM2 if it occurs after a negator and before a punctuation mark;
> 
> Twitter-specific features: the number of tokens with all characters in upper case, the number of hashtags, presence of positive and negative emoticons, whether the last token is a positive or negative emoticon, the number of elongated words (e.g., soooo);
> 
> Punctuation: presence of exclamation and question marks, whether the last token contains an exclamation or question mark.
> 
> Domain-Specific Features
> 
> To generate domain-specific features, we used the following domain resources:
> 
> Medication list: we compiled a medication list by selecting all one-word medication names from RxNorm (e.g, acetaminophen, nicorette, zoloft) since most of the medications mentioned in the training datasets were one-word strings.
> 
> Pronoun Lexicon: we compiled a lexicon of first-person pronouns (e.g., I, ours, we'll), second-person pronouns (e.g., you, yourself), and third-person pronouns (e.g., them, mom's, parents').
> 
> ADR Lexicon: a list of 13,699 ADR concepts compiled from COSTART, SIDER, CHV, and drug-related tweets by the DIEGO lab; BIBREF16
> 
> domain word embeddings: dense word representations generated by the DIEGO lab by applying word2vec on one million tweets mentioning

#### Relevance 126

Label: 0

## Question 0015

Paper: Fixed-Size Ordinally Forgetting Encoding Based Word Sense Disambiguation

> How much lower is the computational cost of the proposed model?

### Common Retrieved Chunks

#### Passage 127

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this paper, we propose a new method for word sense disambiguation problem, which adopts the fixed-size ordinally forgetting encoding (FOFE) to convert variable-length context into almost unique fixed-size representation. A feed forward neural network pseudo language model is trained with FOFE codes of large unlabelled corpus, and used for abstracting the context embeddings of annotated instance to build a k-nearest neighbor classifier for every polyseme. Compared to the high computational cost induced by LSTM model, the fixed-size encoding by FOFE enables the usage of a simple feed forward neural network, which is not only much more efficient but also equivalently promising in numerical performance.

#### Relevance 127

Label: 0

#### Passage 128

Retrieved by: BM25, Hybrid RRF

> an almost unique fixed-size representation, while also retain the positional information for words in the sequence. FOFE has been applied to several NLP problems in the past, such as language model BIBREF5 , named entity recognition BIBREF6 , and word embedding BIBREF7 . The promising results demonstrated by the FOFE approach in these areas inspired us to apply FOFE in solving the WSD problem. In this paper, we will first describe how FOFE is used to encode sequence of any length into a fixed-size representation. Next, we elaborate on how a pseudo language model is trained with the FOFE encoding from unlabelled data for the purpose of context abstraction, and how a classifier for each polyseme is built from context abstractions of its labelled training data. Lastly, we provide the experiment results of our method on several WSD data sets to justify the equivalent performance as the state-of-the-art approach.

#### Relevance 128

Label: 0

#### Passage 129

Retrieved by: BM25, Hybrid RRF

> Words with multiple senses commonly exist in many languages. For example, the word bank can either mean a “financial establishment” or “the land alongside or sloping down to a river or lake”, based on different contexts. Such a word is called a “polyseme”. The task to identify the meaning of a polyseme in its surrounding context is called word sense disambiguation (WSD). Word sense disambiguation is a long-standing problem in natural language processing (NLP), and has broad applications in other NLP problems such as machine translation BIBREF0 . Lexical sample task and all-word task are the two main branches of WSD problem. The former focuses on only a pre-selected set of polysemes whereas the later intends to disambiguate every polyseme in the entire text. Numerous works have been devoted in WSD task, including supervised, unsupervised, semi-supervised and knowledge based learning BIBREF1 . Our work focuses on using supervised learning to solve all-word WSD problem.
> 
> Most supervised approaches focus on extracting features from words in the context. Early approaches mostly depend on hand-crafted features. For example, IMS by BIBREF2 uses POS tags, surrounding words and collections of local words as features. These approaches are later improved by combining with word embedding features BIBREF0 , which better represents the words' semantic information in a real-value space. However, these methods neglect the valuable positional information between the words in the sequence BIBREF3 . The bi-directional Long-Short-Term-Memory (LSTM) approach by BIBREF3 provides one way to leverage the order of words. Recently, BIBREF4 improved the performance by pre-training a LSTM language model with a large unlabelled corpus, and using this model to generate sense vectors for further WSD predictions. However, LSTM significantly increases the computational complexity during the training process.
> 
> The development of the so called “fixed-size ordinally forgetting encoding” (FOFE) has enabled us to consider more efficient method. As firstly proposed in BIBREF5 , FOFE provides a way to encode the entire sequence of words of variable length into an almost unique fixed-size representation, while also retain the positional information for words in the sequence. FOFE has been applied to several NLP problems in the past, such as language model BIBREF5 , named entity recognition BIBREF6 , and word

#### Relevance 129

Label: 0

#### Passage 130

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> A language model is trained with large unlabelled corpus by BIBREF4 in order to overcome the shortage of WSD training data. A language model represents the probability distribution of a given sequence of words, and it is commonly used in predicting the subsequent word given preceding sequence. BIBREF5 proposed a FOFE-based neural network language model by feeding FOFE code of preceding sequence into FFNN. WSD is different from language model in terms of that the sense prediction of a target word depends on its surrounding sequence rather than only preceding sequence. Hence, we build a pseudo language model that uses both preceding and succeeding sequence to accommodate the purpose of WSD tasks.
> 
> The preceding and succeeding sequences are separately converted into FOFE codes. As shown in Figure FIGREF3 , the words preceding the target word are encoded from left to right as the left FOFE code, and the words succeeding the target word are encoded from right to left as the right FOFE code. The forgetting factor that underlies the encoding direction reflects the reducing relevance of a word due to the increasing distance relative to the target word. Furthermore, the FOFE is scalable to higher orders by merging tailing partial FOFE codes. For example, a second order FOFE of sequence INLINEFORM0 can be obtained as INLINEFORM1 . Lastly, the left and right FOFE codes are concatenated into one single fixed-size vector, which can be fed into an FFNN as an input.
> 
> FFNN is constructed in fully-connected layers. Each layer receives values from previous layer as input, and produces values through a function over weighted input values as its output. FFNN increasingly abstracts the features of the data through the layers. As the pseudo language model is trained to predict the target word, the output layer is irrelevant to WSD task and hence can be discarded. However, the remaining layers still have learned the ability to generalize features from word to context during the training process. The values of the held-out layer (the second last layer) are extracted as context embedding, which provides a nice numerical abstraction of the surrounding context of a target word.

#### Relevance 130

Label: 0

#### Passage 131

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> The linguistic distribution hypothesis states that words that occur in close contexts should have similar meaning BIBREF8 . It implies that the particular sense of a polyseme is highly related to its surrounding context. Moreover, human decides the sense of a polyseme by firstly understanding its occurring context. Likewise, our proposed model has two stages, as shown in Figure FIGREF3 : training a FOFE-based pseudo language model that abstracts context as embeddings, and performing WSD classification over context embeddings.

#### Relevance 131

Label: 0

#### Passage 132

Retrieved by: Dense, Hybrid RRF

> Table TABREF6 presents the micro F1 scores from different models. Note that we use a corpus with 0.8 billion words and vocabulary of 100,000 words when training the language model, comparing with BIBREF4 using 100 billion words and vocabulary of 1,000,000 words. The context abstraction using the language model is the most crucial step. The sizes of the training corpus and vocabulary significantly affect the performance of this process, and consequently the final WSD results. However, BIBREF4 did not publish the 100 billion words corpus used for training their LSTM language model.
> 
> Recently, BIBREF9 reimplemented the LSTM-based WSD classifier. The authors trained the language model with a smaller corpus Gigaword BIBREF16 of 2 billion words and vocabulary of 1 million words, and reported the performance. Their published code also enabled us to train an LSTM model with the same data used in training our FOFE model, and compare the performances at the equivalent conditions.
> 
> Additionally, the bottleneck of the LSTM approach is the training speed. The training process of the LSTM model by BIBREF9 took approximately 4.5 months even after applying optimization of trimming sentences, while the training process of our FOFE-based model took around 3 days to produce the claimed results.

#### Relevance 132

Label: 1

#### Passage 133

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> To evaluate the performance of our proposed model, we implemented our model using Tensorflow BIBREF11 and conducted experiments on standard SemEval data that are labelled by senses from WordNet 3.0 BIBREF12 . We built the classifier using SemCor BIBREF13 as training corpus, and evaluated on Senseval2 BIBREF14 , and SemEval-2013 Task 12 BIBREF15 .

#### Relevance 133

Label: 0

#### Passage 135

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> The fact that human languages consist of variable-length sequence of words requires NLP models to be able to consume variable-length data. RNN/LSTM addresses this issue by recurrent connections, but such recurrence consequently increases the computational complexity. On the contrary, feed forward neural network (FFNN) has been widely adopted in many artificial intelligence problems due to its powerful modelling ability and fast computation, but is also limited by its requirement of fixed-size input. FOFE aims at encoding variable-length sequence of words into a fixed-size representation, which subsequently can be fed into an FFNN.
> 
> Given vocabulary INLINEFORM0 of size INLINEFORM1 , each word can be represented by a one-hot vector. FOFE can encode a sequence of words of any length using linear combination, with a forget factor to reflect the positional information. For a sequence of words INLINEFORM2 from V, let INLINEFORM3 denote the one-hot representation for the INLINEFORM4 word, then the FOFE code of S can be recursively obtained using following equation (set INLINEFORM5 ): INLINEFORM6
> 
> where INLINEFORM0 is a constant between 0 and 1, called forgetting factor. For example, assuming A, B, C are three words with one-hot vectors INLINEFORM1 , INLINEFORM2 , INLINEFORM3 respectively. The FOFE encoding from left to right for ABC is [ INLINEFORM4 , INLINEFORM5 ,1] and for ABCBC is [ INLINEFORM6 , INLINEFORM7 , INLINEFORM8 ]. It becomes evident that the FOFE code is in fixed size, which is equal to the size of the one-hot vector, regardless of the length of the sequence INLINEFORM9 .
> 
> The FOFE encoding has the property that the original sequence can be unequivocally recovered from the FOFE encoding. According to BIBREF5 , the uniqueness for the FOFE encoding of a sequence is confirmed by the following two theorems:
> 
> Theorem 1 If the forgetting factor INLINEFORM0 satisfies INLINEFORM1 , FOFE is unique for any sequence of finite length INLINEFORM2 and any countable vocabulary INLINEFORM3 .
> 
> Theorem 2 If the forgetting factor INLINEFORM0 satisfies INLINEFORM1 , FOFE is almost unique for any finite value of INLINEFORM2 and vocabulary INLINEFORM3 , except only a finite set of countable choices of INLINEFORM4 .
> 
> Even for situations described by Theorem SECREF2 where uniqueness is not strictly guaranteed, the probability

#### Relevance 135

Label: 0

### BM25

None

### Dense

#### Passage 134

Retrieved by: Dense

> When training our FOFE-based pseudo language model, we use Google1B BIBREF10 corpus as the training data, which consists of approximately 0.8 billion words. The 100,000 most frequent words in the corpus are chosen as the vocabulary. The dimension of word embedding is chosen to be 512. During the experiment, the best results are produced by the 3rd order pseudo language model. The concatenation of the left and right 3rd order FOFE codes leads to a dimension of 512 * 3 * 2 = 3072 for the FFNN's input layer. Then we append three hidden layers of dimension 4096. Additionally, we choose a constant forgetting factor INLINEFORM0 for the FOFE encoding and INLINEFORM1 for our k-nearest neighbor classifier.

#### Relevance 134

Label: 0

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0016

Paper: Phrase Table as Recommendation Memory for Neural Machine Translation

> which attention based nmt method did they compare with?

### Common Retrieved Chunks

#### Passage 136

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We compare our method with other relevant methods as follows:
> 
> 1) Moses: It is a widely used phrasal SMT system BIBREF22 .
> 
> 2) Baseline: It is the baseline attention-based NMT system BIBREF23 , BIBREF24 .
> 
> 3) Arthur: It is the state-of-the-art method which incorporates discrete translation lexicons into NMT model BIBREF6 . We choose automatically learned lexicons and bias method. We implement the method on the base of the baseline attention-based NMT system. Hyper parameter INLINEFORM0 is 0.001, the same as that reported in their work.

#### Relevance 136

Label: 1

#### Passage 137

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Table 1 reports the detailed translation results for different methods. Comparing the first two rows in Table 1, it is very obvious that the attention-based NMT system Baseline substantially outperforms the phrase-based SMT system Moses on both CH-EN translation and EN-JA translation. The average improvement for CH-EN and EN-JA translation is up to 3.99 BLEU points (32.71 vs. 28.72) and 3.59 BLEU (25.99 vs. 22.40) points, respectively.

#### Relevance 137

Label: 1

#### Passage 138

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this work, we focus on integrating the phrase translation table of SMT into NMT. And there have been several effective works to combine SMT and NMT.
> 
> Using coverage mechanism. BIBREF9 and BIBREF10 improved the over-translation and under-translation problems in NMT inspired by the coverage mechanism in SMT.
> 
> Extending beam search. BIBREF25 extended the beam search method with SMT hypotheses. BIBREF13 improved the beam search by using the SMT lattices.
> 
> Combining SMT features and results. BIBREF12 presented a log-linear model to integrate SMT features (translation model and the language model) into NMT. BIBREF26 and BIBREF27 proposed a supervised attention model for NMT to minimize the alignment disagreement between NMT and SMT. BIBREF11 proposed a method that incorporates the translations of SMT into NMT with an auxiliary classifier and a gating function. BIBREF28 proposed a neural combination model to fuse the NMT translation results and SMT translation results.
> 
> Incorporating translation lexicons. BIBREF6 , BIBREF17 attempted to integrate NMT with the probabilistic translation lexicons. BIBREF16 moved forward further by incorporating a bilingual dictionaries in NMT.
> 
> In above works, integrating the phrase translation table of SMT into NMT has not been fully studied.
> 
> Translating phrase in NMT. The most related works are BIBREF18 and BIBREF19 . Both methods attempted to explore the possibility of translating phrases as a whole in NMT. In their models, NMT can generate a target phrase in phrase memory or a word in vocabulary by using a gate. However, their “phrases” are different from that are used in phrase-based SMT. BIBREF18 's models only support a unique translation for a source phrase. In BIBREF19 's models, the source side of a phrase pair must be a chunk. Different from above two methods, our model can use any phrase pair in the phrase translation table and promising results can be achieved.

#### Relevance 138

Label: 0

#### Passage 140

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> BIBREF19 's models, the source side of a phrase pair must be a chunk. Therefore, it is still a big challenge to incorporate any phrase pair in the phrase table into NMT system to alleviate the unfaithfulness problem.
> 
> In this paper, we propose an effective method to incorporate a phrase table as recommendation memory into the NMT system. To achieve this, we add bonuses to the words in recommendation set to help NMT make better predictions. Generally, our method contains three steps. 1) In order to find out which words are worthy to recommend, we first derive a candidate target phrase set by searching the phrase table according to the input sentence. After that, we construct a recommendation word set at each decoding step by matching between candidate target phrases and previously translated target words by NMT. 2) We then determine the specific bonus value for each recommendable word by using the attention vector produced by NMT and phrase translation probability extracted from phrase table. 3) Finally we integrate the word bonus value into the NMT system to improve the final results.
> 
> In this paper, we make the following contributions:
> 
> 1) We propose a method to incorporate the phrase table as recommendation memory into NMT system. We design a novel approach to find from the phrase table the target words worthy of recommendation, calculate their recommendation scores and use them to promote NMT to make better predictions.
> 
> 2) Our empirical experiments on Chinese-English translation and English-Japanese translation tasks show the efficacy of our methods. For Chinese-English translation, we can obtain an average improvement of 2.23 BLEU points. For English-Japanese translation, the improvement can reach 1.96 BLEU points. We further find that the phrase table is much more beneficial than bilingual lexicons to NMT.

#### Relevance 140

Label: 0

#### Passage 141

Retrieved by: Dense, Hybrid RRF

> A natural question arises that whether it is more beneficial to incorporate a phrase translation table than the translation lexicons. From Table 1, we can conclude that both translation lexicons and phrase translation table can improve NMT system's translation quality. In CH-EN translation, Arthur improves the baseline NMT system with 0.81 BLEU points, while our method improves the baseline NMT system with 2.23 BLEU points. In EN-JA translation, Arthur improves the baseline NMT system with 0.73 BLEU points, while our method improves the baseline NMT system with 1.96 BLEU points. Therefore, it is very obvious that phrase information is more effective than lexicon information when we use them to improve the NMT system.
> 
> Fig. 4 shows an illustrative example. In this example, baseline NMT mistranslates “dianli (electricity) anquan (safe)” into “coal”. Arthur partially fixes this error and it can correctly translate “dianli (electrical)” into “electrical”, but the source word “anquan (safe)” is still missed. Fortunately, this mistake is fixed by our proposed method. The reason behind this is that Arthur uses information from translation lexicons, which makes the system only fix the translation mistake of an individual lexicon (in this example, it is “dianli (electrical)”), while our method uses the information from phrases, which makes the system can not only obtain the correct translation of the individual lexicon but also capture local lexicon reordering and fixed collocation etc.
> 
> Besides the BLEU score, we also conduct a subjective evaluation to validate the benefit of incorporating a phrase table in NMT. The subjective evaluation is conducted on CH-EN translation. As our method tries to solve the problem that NMT system cannot reflect the true meaning of the source sentence, the criterion of the subjective evaluation is the faithfulness of translation results. Specifically, five human evaluators, who are native Chinese and expert in English, are asked to evaluate the translations of 500 source sentences randomly sampled from the test sets without knowing which system a translation is selected from. The score ranges from 0 to 5. For a translation result, the higher its score is, the more faithful it is. Table 2 shows the average results of five subjective evaluations on CH-EN translation. As shown in Table 2，the

#### Relevance 141

Label: 1

### BM25

#### Passage 139

Retrieved by: BM25

> The past several years have witnessed a significant progress in Neural Machine Translation (NMT). Most NMT methods are based on the encoder-decoder architecture BIBREF0 , BIBREF1 , BIBREF2 and can achieve promising translation performance in a variety of language pairs BIBREF3 , BIBREF4 , BIBREF5 .
> 
> However, recent studies BIBREF6 , BIBREF7 show that NMT often generates words that make target sentences fluent, but unfaithful to the source sentences. In contrast, traditional Statistical Machine Translation (SMT) methods tend to rarely make this kind of mistakes. Fig. 1 shows an example that NMT makes mistakes when translating the phrase “jinkou dafu xiahua (the sharp decline in imports)” and the phrase “maoyi shuncha (the trade surplus)”, but SMT can produce correct results when translating these two phrases. BIBREF6 argues that the reason behind this is the use of distributed representations of words in NMT makes systems often generate words that seem natural in the context, but do not reflect the content of the source sentence. Traditional SMT can avoid this problem as it produces the translations based on phrase mappings.
> 
> Therefore, it will be beneficial to combine SMT and NMT to alleviate the previously mentioned problem. Actually, researchers have made some effective attempts to achieve this goal. Earlier studies were based on the SMT framework, and have been deeply discussed in BIBREF8 . Later, the researchers transfers to NMT framework. Specifically, coverage mechanism BIBREF9 , BIBREF10 , SMT features BIBREF11 , BIBREF12 , BIBREF13 , BIBREF14 , BIBREF15 and translation lexicons BIBREF6 , BIBREF16 , BIBREF17 have been fully explored. In contrast, phrase translation table, as the core of SMT, has not been fully studied. Recently, BIBREF18 and BIBREF19 explore the possibility of translating phrases in NMT. However, the “phrase” in their approaches are different from that used in phrase-based SMT. In BIBREF18 's models, the phrase pair must be a one-to-one mapping with a source phrase having a unique target phrase (named entity translation pairs). In BIBREF19 's models, the source side of a phrase pair must be a chunk. Therefore, it is still a big challenge to incorporate any phrase pair in the phrase table into NMT system to alleviate the unfaithfulness problem.
> 
> In this

#### Relevance 139

Label: 0

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 142

Retrieved by: Hybrid RRF followed by BGE reranking

> from. The score ranges from 0 to 5. For a translation result, the higher its score is, the more faithful it is. Table 2 shows the average results of five subjective evaluations on CH-EN translation. As shown in Table 2，the faithfulness of translation results produced by our method is better than Arthur and baseline NMT system.

#### Relevance 142

Label: 1

## Question 0017

Paper: UTCNN: a Deep Learning Model of Stance Classificationon on Social Media Text

> What is the size of the Chinese data?

### Common Retrieved Chunks

#### Passage 143

Retrieved by: BM25, Dense, Hybrid RRF

> We tested the proposed UTCNN on two different datasets: FBFans and CreateDebate. FBFans is a privately-owned, single-topic, Chinese, unbalanced, social media dataset, and CreateDebate is a public, multiple-topic, English, balanced, forum dataset. Results using these two datasets show the applicability and superiority for different topics, languages, data distributions, and platforms.
> 
> The FBFans dataset contains data from anti-nuclear-power Chinese Facebook fan groups from September 2013 to August 2014, including posts and their author and liker IDs. There are a total of 2,496 authors, 505,137 likers, 33,686 commenters, and 505,412 unique users. Two annotators were asked to take into account only the post content to label the stance of the posts in the whole dataset as supportive, neutral, or unsupportive (hereafter denoted as Sup, Neu, and Uns). Sup/Uns posts were those in support of or against anti-reconstruction; Neu posts were those evincing a neutral standpoint on the topic, or were irrelevant. Raw agreement between annotators is 0.91, indicating high agreement. Specifically, Cohen’s Kappa for Neu and not Neu labeling is 0.58 (moderate), and for Sup or Uns labeling is 0.84 (almost perfect). Posts with inconsistent labels were filtered out, and the development and testing sets were randomly selected from what was left. Posts in the development and testing sets involved at least one user who appeared in the training set. The number of posts for each stance is shown on the left-hand side of Table TABREF12 . About twenty percent of the posts were labeled with a stance, and the number of supportive (Sup) posts was much larger than that of the unsupportive (Uns) ones: this is thus highly skewed data, which complicates stance classification. On average, 161.1 users were involved in one post. The maximum was 23,297 and the minimum was one (the author). For comments, on average there were 3 comments per post. The maximum was 1,092 and the minimum was zero.
> 
> To test whether the assumption of this paper – posts attract users who hold the same stance to like them – is reliable, we examine the likes from authors of different stances. Posts in FBFans dataset are used for this analysis. We calculate the like statistics of each distinct author from these 32,595

#### Relevance 143

Label: 1

#### Passage 144

Retrieved by: BM25, Dense, Hybrid RRF

> As shown in Figure FIGREF4 , we use a general CNN BIBREF3 and two semantic transformations for document composition . We are given a document with an engaged user INLINEFORM0 , a topic INLINEFORM1 , and its composite INLINEFORM2 words, each word INLINEFORM3 of which is associated with a word embedding INLINEFORM4 where INLINEFORM5 is the vector dimension. For each word embedding INLINEFORM6 , we apply two dot operations as shown in Equation EQREF6 : DISPLAYFORM0
> 
> where INLINEFORM0 models the user reading preference for certain semantics, and INLINEFORM1 models the topic semantics; INLINEFORM2 and INLINEFORM3 are the dimensions of transformed user and topic embeddings respectively. We use INLINEFORM4 to model semantically what each user prefers to read and/or write, and use INLINEFORM5 to model the semantics of each topic. The dot operation of INLINEFORM6 and INLINEFORM7 transforms the global representation INLINEFORM8 to a user-dependent representation. Likewise, the dot operation of INLINEFORM9 and INLINEFORM10 transforms INLINEFORM11 to a topic-dependent representation.
> 
> After the two dot operations on INLINEFORM0 , we have user-dependent and topic-dependent word vectors INLINEFORM1 and INLINEFORM2 , which are concatenated to form a user- and topic-dependent word vector INLINEFORM3 . Then the transformed word embeddings INLINEFORM4 are used as the CNN input. Here we apply three convolutional layers on the concatenated transformed word embeddings INLINEFORM5 : DISPLAYFORM0
> 
> where INLINEFORM0 is the index of words; INLINEFORM1 is a non-linear activation function (we use INLINEFORM2 ); INLINEFORM5 is the convolutional filter with input length INLINEFORM6 and output length INLINEFORM7 , where INLINEFORM8 is the window size of the convolutional operation; and INLINEFORM9 and INLINEFORM10 are the output and bias of the convolution layer INLINEFORM11 , respectively. In our experiments, the three window sizes INLINEFORM12 in the three convolution layers are one, two, and three, encoding unigram, bigram, and trigram semantics accordingly.
> 
> After the convolutional layer, we add a maximum pooling layer among convolutional outputs to obtain the unigram, bigram, and trigram n-gram representations. This is succeeded by an average pooling layer for an element-wise average of the three maximized convolution outputs.

#### Relevance 144

Label: 0

#### Passage 146

Retrieved by: BM25, Dense, Hybrid RRF

> represent relationships between authors, but UTCNN models do not utilize link information between posts. Though the PSL model has the advantage of being able to jointly label the stances of authors and posts, its performance on posts is lower than the that for the ILP or CRF models. UTCNN significantly outperforms these models on posts and has the potential to predict user stances through the generated user embeddings.
> 
> For the CreateDebate dataset, we also evaluated performance when not using topic embeddings or user embeddings; as replies in this dataset are viewed as posts, the setting without comment embeddings is not available. Table TABREF24 shows the same findings as Table TABREF22 : the 21% improvement in accuracy demonstrates that user information is the most vital. This finding also supports the results in the related work: user constraints are useful and can yield 11.2% improvement in accuracy BIBREF7 . Further considering topic information yields 3.4% improvement, suggesting that knowing the subject of debates provides useful information. In sum, Table TABREF22 together with Table TABREF24 show that UTCNN achieves promising performance regardless of topic, language, data distribution, and platform.

#### Relevance 146

Label: 0

#### Passage 148

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In the UTCNN training process, cross-entropy was used as the loss function and AdaGrad as the optimizer. For FBFans dataset, we learned the 50-dimensional word embeddings on the whole dataset using GloVe BIBREF21 to capture the word semantics; for CreateDebate dataset we used the publicly available English 50-dimensional word embeddings, pre-trained also using GloVe. These word embeddings were fixed in the training process. The learning rate was set to 0.03. All user and topic embeddings were randomly initialized in the range of [-0.1 0.1]. Matrix embeddings for users and topics were sized at 250 ( INLINEFORM0 ); vector embeddings for users and topics were set to length 10.
> 
> We applied the LDA topic model BIBREF22 on the FBFans dataset to determine the latent topics with which to build topic embeddings, as there is only one general known topic: nuclear power plants. We learned 100 latent topics and assigned the top three topics for each post. For the CreateDebate dataset, which itself constitutes four topics, the topic labels for posts were used directly without additionally applying LDA.
> 
> For the FBFans data we report class-based f-scores as well as the macro-average f-score ( INLINEFORM0 ) shown in equation EQREF19 . DISPLAYFORM0
> 
> where INLINEFORM0 and INLINEFORM1 are the average precision and recall of the three class. We adopted the macro-average f-score as the evaluation metric for the overall performance because (1) the experimental dataset is severely imbalanced, which is common for contentious issues; and (2) for stance classification, content in minor-class posts is usually more important for further applications. For the CreateDebate dataset, accuracy was adopted as the evaluation metric to compare the results with related work BIBREF7 , BIBREF9 , BIBREF12 .

#### Relevance 148

Label: 0

#### Passage 149

Retrieved by: Dense, Hybrid RRF

> Table TABREF24 shows the results of UTCNN, baselines as we implemented on the FBFans datset and related work on the CreateDebate dataset. We do not adopt oversampling on these models because the CreateDebate dataset is almost balanced. In previous work, integer linear programming (ILP) or linear-chain conditional random fields (CRFs) were proposed to integrate text features, author, ideology, and user-interaction constraints, where text features are unigram, bigram, and POS-dependencies; the author constraint tends to require that posts from the same author for the same topic hold the same stance; the ideology constraint aims to capture inferences between topics for the same author; the user-interaction constraint models relationships among posts via user interactions such as replies BIBREF7 , BIBREF9 .
> 
> The SVM with n-gram or average word embedding feature performs just similar to the majority. However, with the transformed word embedding, it achieves superior results. It shows that the learned user and topic embeddings really capture the user and topic semantics. This finding is not so obvious in the FBFans dataset and it might be due to the unfavorable data skewness for SVM. As for CNN and RCNN, they perform slightly better than most SVMs as we found in Table TABREF22 for FBFans.
> 
> Compared to the ILP BIBREF7 and CRF BIBREF9 methods, the UTCNN user embeddings encode author and user-interaction constraints, where the ideology constraint is modeled by the topic embeddings and text features are modeled by the CNN. The significant improvement achieved by UTCNN suggests the latent representations are more effective than overt model constraints.
> 
> The PSL model BIBREF12 jointly labels both author and post stance using probabilistic soft logic (PSL) BIBREF23 by considering text features and reply links between authors and posts as in Hasan and Ng's work. Table TABREF24 reports the result of their best AD setting, which represents the full joint stance/disagreement collective model on posts and is hence more relevant to UTCNN. In contrast to their model, the UTCNN user embeddings represent relationships between authors, but UTCNN models do not utilize link information between posts. Though the PSL model has the advantage of being able to jointly label the stances of authors and posts, its performance on posts is lower than

#### Relevance 149

Label: 0

### BM25

#### Passage 145

Retrieved by: BM25

> hold the same stance to like them – is reliable, we examine the likes from authors of different stances. Posts in FBFans dataset are used for this analysis. We calculate the like statistics of each distinct author from these 32,595 posts. As the numbers of authors in the Sup, Neu and Uns stances are largely imbalanced, these numbers are normalized by the number of users of each stance. Table TABREF13 shows the results. Posts with stances (i.e., not neutral) attract users of the same stance. Neutral posts also attract both supportive and neutral users, like what we observe in supportive posts, but just the neutral posts can attract even more neutral likers. These results do suggest that users prefer posts of the same stance, or at least posts of no obvious stance which might cause annoyance when reading, and hence support the user modeling in our approach.
> 
> The CreateDebate dataset was collected from an English online debate forum discussing four topics: abortion (ABO), gay rights (GAY), Obama (OBA), and marijuana (MAR). The posts are annotated as for (F) and against (A). Replies to posts in this dataset are also labeled with stance and hence use the same data format as posts. The labeling results are shown in the right-hand side of Table TABREF12 . We observe that the dataset is more balanced than the FBFans dataset. In addition, there are 977 unique users in the dataset. To compare with Hasan and Ng's work, we conducted five-fold cross-validation and present the annotation results as the average number of all folds BIBREF9 , BIBREF5 .
> 
> The FBFans dataset has more integrated functions than the CreateDebate dataset; thus our model can utilize all linguistic and extra-linguistic features. For the CreateDebate dataset, on the other hand, the like and comment features are not available (as there is a stance label for each reply, replies are evaluated as posts as other previous work) but we still implemented our model using the content, author, and topic information.

#### Relevance 145

Label: 1

#### Passage 147

Retrieved by: BM25

> In Table TABREF22 we show the results of UTCNN and the baselines on the FBFans dataset. Here Majority yields good performance on Neu since FBFans is highly biased to the neutral class. The SVM models perform well on Sup and Neu but perform poorly for Uns, showing that content information in itself is insufficient to predict stance labels, especially for the minor class. With the transformed word embedding feature, SVM can achieve comparable performance as SVM with n-gram feature. However, the much fewer feature dimension of the transformed word embedding makes SVM with word embeddings a more efficient choice for modeling the large scale social media dataset. For the CNN and RCNN models, they perform slightly better than most of the SVM models but still, the content information is insufficient to achieve a good performance on the Uns posts. As to adding comment information to these models, since the commenters do not always hold the same stance as the author, simply adding comments and post contents together merely adds noise to the model.
> 
> Among all UTCNN variations, we find that user information is most important, followed by topic and comment information. UTCNN without user information shows results similar to SVMs — it does well for Sup and Neu but detects no Uns. Its best f-scores on both Sup and Neu among all methods show that with enough training data, content-based models can perform well; at the same time, the lack of user information results in too few clues for minor-class posts to either predict their stance directly or link them to other users and posts for improved performance. The 17.5% improvement when adding user information suggests that user information is especially useful when the dataset is highly imbalanced. All models that consider user information predict the minority class successfully. UCTNN without topic information works well but achieves lower performance than the full UTCNN model. The 4.9% performance gain brought by LDA shows that although it is satisfactory for single topic datasets, adding that latent topics still benefits performance: even when we are discussing the same topic, we use different arguments and supporting evidence. Lastly, we get 4.8% improvement when adding comment information and it achieves

#### Relevance 147

Label: 0

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 150

Retrieved by: Hybrid RRF followed by BGE reranking

> acting as a commenter, though, she interacts with post contents by criticizing past politicians who supported nuclear power or by arguing that the proposed evacuation plan in case of a nuclear accident is ridiculous. Based on this finding, in the final UTCNN setting we train two user matrix embeddings for one user: one for the author/liker role and the other for the commenter role.

#### Relevance 150

Label: 0

#### Passage 151

Retrieved by: Hybrid RRF followed by BGE reranking

> We attempt to learn user and topic representations which encode user interactions and topic influences to further enhance text classification, and we also incorporate comment information. We evaluate this model on a post stance classification task on forum-style social media platforms. The contributions of this paper are as follows: 1. We propose UTCNN, a neural network for text in modern social media channels as well as legacy social media, forums, and message boards — anywhere that reveals users, their tastes, as well as their replies to posts. 2. When classifying social media post stances, we leverage users, including authors and likers. User embeddings can be generated even for users who have never posted anything. 3. We incorporate a topic model to automatically assign topics to each post in a single topic dataset. 4. We show that overall, the proposed method achieves the highest performance in all instances, and that all of the information extracted, whether users, topics, or comments, still has its contributions.

#### Relevance 151

Label: 0

#### Passage 152

Retrieved by: Hybrid RRF followed by BGE reranking

> We have proposed UTCNN, a neural network model that incorporates user, topic, content and comment information for stance classification on social media texts. UTCNN learns user embeddings for all users with minimum active degree, i.e., one post or one like. Topic information obtained from the topic model or the pre-defined labels further improves the UTCNN model. In addition, comment information provides additional clues for stance classification. We have shown that UTCNN achieves promising and balanced results. In the future we plan to explore the effectiveness of the UTCNN user embeddings for author stance classification.

#### Relevance 152

Label: 0

#### Passage 153

Retrieved by: Hybrid RRF followed by BGE reranking

> Research of this paper was partially supported by Ministry of Science and Technology, Taiwan, under the contract MOST 104-2221-E-001-024-MY2.

#### Relevance 153

Label: 0

## Question 0018

Paper: Location, Occupation, and Semantics based Socioeconomic Status Inference on Twitter

> What kind of inference model do they build to estimate socioeconomic status?

### Common Retrieved Chunks

#### Passage 154

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Online social networks have become one of the most disruptive communication platforms, as everyday billions of individuals use them to interact with each other. Their penetration in our everyday lives seems ever-growing and has in turn generated a massive volume of publicly available data open to analysis. The digital footprints left across these multiple media platforms provide us with a unique source to study and understand how the linguistic phenotype of a given user is related to social attributes such as socioeconomic status (SES).
> 
> The quantification and inference of SES of individuals is a long lasting question in the social sciences. It is a rather difficult problem as it may depend on a combination of individual characteristics and environmental variables BIBREF0 . Some of these features can be easier to assess like income, gender, or age whereas others, relying to some degree on self-definition and sometimes entangled with privacy issues, are harder to assign like ethnicity, occupation, education level or home location. Furthermore, individual SES correlates with other individual or network attributes, as users tend to build social links with others of similar SES, a phenomenon known as status homophily BIBREF1 , arguably driving the observed stratification of society BIBREF2 . At the same time, shared social environment, similar education level, and social influence have been shown to jointly lead socioeconomic groups to exhibit stereotypical behavioral patterns, such as shared political opinion BIBREF3 or similar linguistic patterns BIBREF4 . Although these features are entangled and causal relation between them is far from understood, they appear as correlations in the data.
> 
> Datasets recording multiple characteristics of human behaviour are more and more available due to recent developments in data collection technologies and increasingly popular online platforms and personal digital devices. The automatic tracking of online activities, commonly associated with profile data and meta-information; the precise recording of daily activities, interaction dynamics and mobility patterns collected through mobile personal devices; together with the detailed and expert annotated census data all provide new grounds for the inference of individual features or behavioral patterns BIBREF5 . The exploitation of these data sources has already been proven to be fruitful as cutting edge recommendation systems, advanced methods for health record

#### Relevance 154

Label: 0

#### Passage 155

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> epochs. We used this model to classify images of the estimated home location satellite views (cf. Figure FIGREF12 a) and kept those which were identified as residential areas (see Fig. FIGREF12 b, showing the activation of the two first hidden layers of the trained model). This way INLINEFORM5 inferred home locations were discarded.
> 
> Next we aimed to estimate SES from architectural/urban features associated to the home locations. Thus, for each home location we collected two additional satellite views at different resolutions as well as six Street View images, each with a horizontal view of approximately INLINEFORM0 . We randomly selected a sample of INLINEFORM1 locations and involved architects to assign a SES score (from 1 to 9) to a sample set of selected locations based on the satellite and Street View around it (both samples had 333 overlapping locations). For validation, we took users from each annotated SES class and computed the distribution of their incomes inferred from the IRIS census data (see Section SECREF6 ). Violin plots in Fig. FIGREF12 d show that in expert annotated data, as expected, the inferred income values were positively correlated with the annotated SES classes. Labels were then categorized into two socioeconomic classes for comparison purposes. All in all, both annotators assigned the same label to the overlapping locations in INLINEFORM2 of samples.
> 
> To solve the SES inference problem we used the above described three datasets (for a summary see Table TABREF14 ). We defined the inference task as a two-way classification problem by dividing the user set of each dataset into two groups. For the census and occupation datasets the lower and higher SES classes were separated by the average income computed from the whole distribution, while in the case of the expert annotated data we assigned people from the lowest five SES labels to the lower SES class in the two-way task. The relative fractions of people assigned to the two classes are depicted in Fig. FIGREF15 b for each dataset and summarized in Table TABREF14 .

#### Relevance 155

Label: 1

#### Passage 156

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> BIBREF17 . Note, that by applying these consecutive filters we obtained a more representative population as the Gini index, indicating overall socioeconomic inequalities, was INLINEFORM4 before filtering become INLINEFORM5 due to the filtering methods, which is closer to the value reported by the World Bank ( INLINEFORM6 ) BIBREF26 .
> 
> To verify our results, we computed the average weekly distance from each recorded location of a user to his inferred home location defined either as its most frequent location overall or among locations posted outside of work-hours from 9AM to 6PM (see Fig. FIGREF4 a). This circadian pattern displays great similarity to earlier results BIBREF25 with two maxima, roughly corresponding to times at the workplace, and a local minimum at 1PM due to people having lunch at home. We found that this circadian pattern was more consistent with earlier results BIBREF25 when we considered all geolocated tweets (“All" in Fig. FIGREF4 a) rather than only tweets including “home-related" expressions (“Night" in Fig. FIGREF4 a). To further verify the inferred home locations, for a subset of 29,389 users we looked for regular expressions in their tweets that were indicative of being at home BIBREF25 , such as “chez moi", “bruit", “dormir" or “nuit". In Fig. FIGREF4 c we show the temporal distribution of the rate of the word “dormir" at the inferred home locations. This distribution appears with a peak around 10PM, which is very different from the overall distribution of geolocated tweets throughout the day considering any location (see Fig. FIGREF4 b).
> 
> To obtain meaningful linguistic data we pre-processed the incoming tweet streams in several ways. As our central question here deals with language semantics of individuals, re-tweets do not bring any additional information to our study, thus we removed them by default. We also removed any expressions considered to be semantically meaningless like URLs, emoticons, mentions of other users (denoted by the @ symbol) and hashtags (denoted by the # symbol) to simplify later post-processing. In addition, as a last step of textual pre-processing, we downcased and stripped the punctuation from the text of every tweet.

#### Relevance 156

Label: 0

#### Passage 158

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> census data all provide new grounds for the inference of individual features or behavioral patterns BIBREF5 . The exploitation of these data sources has already been proven to be fruitful as cutting edge recommendation systems, advanced methods for health record analysis, or successful prediction tools for social behaviour heavily rely on them BIBREF6 . Nevertheless, despite the available data, some inference tasks, like individual SES prediction, remain an open challenge.
> 
> The precise inference of SES would contribute to overcome several scientific challenges and could potentially have several commercial applications BIBREF7 . Further, robust SES inference would provide unique opportunities to gain deeper insights on socioeconomic inequalities BIBREF8 , social stratification BIBREF2 , and on the driving mechanisms of network evolution, such as status homophily or social segregation.
> 
> In this work, we take a horizontal approach to this problem and explore various ways to infer the SES of a large sample of social media users. We propose different data collection and combination strategies using open, crawlable, or expert annotated socioeconomic data for the prediction task. Specifically, we use an extensive Twitter dataset of 1.3M users located in France, all associated with their tweets and profile information; 32,053 of them having inferred home locations. Individual SES is estimated by relying on three separate datasets, namely socioeconomic census data; crawled profession information and expert annotated Google Street View images of users' home locations. Each of these datasets is then used as ground-truth to infer the SES of Twitter users from profile and semantic features similar to BIBREF9 . We aim to explore and assess how the SES of social media users can be obtained and how much the inference problem depends on annotation and the user's individual and linguistic attributes.
> 
> We provide in Section SECREF2 an overview of the related literature to contextualize the novelty of our work. In Section SECREF3 we provide a detailed description of the data collection and combination methods. In Section SECREF4 we introduce the features extracted to solve the SES inference problem, with results summarized in Section SECREF5 . Finally, in Section SECREF6 and SECREF7 we conclude our paper with a brief discussion of the limitations and perspectives of our methods.

#### Relevance 158

Label: 0

#### Passage 159

Retrieved by: Dense, Hybrid RRF

> In order to assess the degree to which linguistic features can be used for discriminating users by their socioeconomic class, we trained with these feature sets different learning algorithms. Namely, we used the XGBoost algorithm BIBREF43 , an implementation of the gradient-boosted decision trees for this task. Training a decision tree learning algorithm involves the generation of a series of rules, split points or nodes ordered in a tree-like structure enabling the prediction of a target output value based on the values of the input features. More specifically, XGBoost, as an ensemble technique, is trained by sequentially adding a high number of individually weak but complementary classifiers to produce a robust estimator: each new model is built to be maximally correlated with the negative gradient of the loss function associated with the model assembly BIBREF44 . To evaluate the performance of this method we benchmarked it against more standard ensemble learning algorithms such as AdaBoost and Random Forest.
> 
> For each socioeconomic dataset, we trained our models by using 75% of the available data for training and the remaining 25% for testing. During the training phase, the training data undergoes a INLINEFORM0 -fold inner cross-validation, with INLINEFORM1 , where all splits are computed in a stratified manner to get the same ratio of lower to higher SES users. The four first blocks were used for inner training and the remainder for inner testing. This was repeated ten times for each model so that in the end, each model's performance on the validation set was averaged over 50 samples. For each model, the parameters were fine-tuned by training 500 different models over the aforementioned splits. The selected one was that which gave the best performance on average, which was then applied to the held-out test set. This is then repeated through a 5-fold outer cross-validation.
> 
> In terms of prediction score, we followed a standard procedure in the literature BIBREF45 and evaluated the learned models by considering the area under the receiver operating characteristic curve (AUC). This metric can be thought as the probability that a classifier ranks a randomly chosen positive instance higher than a randomly chosen negative one BIBREF44 .
> 
> This procedure was applied to each

#### Relevance 159

Label: 1

#### Passage 160

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> There is a growing effort in the field to combine online behavioral data with census records, and expert annotated information to infer social attributes of users of online services. The predicted attributes range from easily assessable individual characteristics such as age BIBREF10 , or occupation BIBREF9 , BIBREF11 , BIBREF12 , BIBREF13 to more complex psychological and sociological traits like political affiliation BIBREF14 , personality BIBREF15 , or SES BIBREF16 , BIBREF9 .
> 
> Predictive features proposed to infer the desired attributes are also numerous. In case of Twitter, user information can be publicly queried within the limits of the public API BIBREF17 . User characteristics collected in this way, such as profile features, tweeting behavior, social network and linguistic content have been used for prediction, while other inference methods relying on external data sources such as website traffic data BIBREF18 or census data BIBREF19 , BIBREF20 have also proven effective. Nonetheless, only recent works involve user semantics in a broader context related to social networks, spatiotemporal information, and personal attributes BIBREF12 , BIBREF9 , BIBREF11 , BIBREF21 .
> 
> The tradition of relating SES of individuals to their language dates back to the early stages of sociolinguistics where it was first shown that social status reflected through a person's occupation is a determinant factor in the way language is used BIBREF22 . This line of research was recently revisited by Lampos et al. to study the SES inference problem on Twitter. In a series of works BIBREF12 , BIBREF9 , BIBREF11 , BIBREF21 , the authors applied Gaussian Processes to predict user income, occupation and socioeconomic class based on demographic, psycho-linguistic features and a standardized job classification taxonomy which mapped Twitter users to their professional occupations. The high predictive performance has proven this concept with INLINEFORM0 for income prediction, and a precision of INLINEFORM1 for 9-ways SOC classification, and INLINEFORM2 for binary SES classification. Nevertheless, the models developed by the authors are learned by relying on datasets, which were manually labeled through an annotation process crowdsourced through Amazon Mechanical Turk at a high monetary cost. Although the labeled data has been released and provides the base for new extensions BIBREF10 , it has two potential shortfalls

#### Relevance 160

Label: 0

### BM25

#### Passage 157

Retrieved by: BM25

> area under the receiver operating characteristic curve (AUC). This metric can be thought as the probability that a classifier ranks a randomly chosen positive instance higher than a randomly chosen negative one BIBREF44 .
> 
> This procedure was applied to each of our datasets. The obtained results are shown in Fig. FIGREF21 and in Table TABREF22 .
> 
> As a result, we first observed that XGBoost consistently provided top prediction scores when compared to AdaBoost and Random Forest (all performance scores are summarised in Table TABREF20 ). We hence used it for our predictions in the remainder of this study. We found that the LinkedIn data was the best, with INLINEFORM0 , to train a model to predict SES of people based on their semantic features. It provided a INLINEFORM1 increase in performance as compared to the census based inference with INLINEFORM2 , and INLINEFORM3 relative to expert annotated data with INLINEFORM4 . Thus we can conclude that there seem to be a trade-off between scalability and prediction quality, as while the occupation dataset provided the best results, it seems unlikely to be subject to any upscaling due to the high cost of obtaining a clean dataset. Relying on location to estimate SES seems to be more likely to benefit from such an approach, though at the cost of an increased number of mislabelled users in the dataset. Moreover, the annotator's estimation of SES using Street View at each home location seems to be hindered by the large variability of urban features. Note that even though inter-agreement is 76%, the Cohen's kappa score for annotator inter-agreement is low at 0.169. Furthermore, we remark that the expert annotated pipeline was also subject to noise affecting the home location estimations, which potentially contributed to the lowest predictive performance.
> 
> Finally, it should also be noted that following recent work by Aletras and Chamberlain in BIBREF21 , we tested our model by extending the feature set with the node2vec embedding of users computed from the mutual mention graph of Twitter. Nevertheless, in our setting, it did not increase the overall predictive performance of the inference pipeline. We hence didn't include in the feature set for the sake of simplicity.

#### Relevance 157

Label: 1

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0019

Paper: ReviewQA: a relational aspect-based opinion reading dataset

> What kind of questions are present in the dataset?

### Common Retrieved Chunks

#### Passage 161

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We think that evaluating the task of sentiment analysis through the setup of question-answering is a relevant playground for machine reading research. Indeed natural language questions about the different aspects of the targeted venues are typical kind of questions we want to be able to ask to a system. In this context, we introduce a set of reasoning questions types over the relationships between aspects. We propose ReviewQA, a dataset of natural language questions over hotel reviews. These questions are divided into 8 groups, regarding the competency required to be answered. In this section, we describe each task and the process followed to generate this dataset.

#### Relevance 161

Label: 1

#### Passage 162

Retrieved by: BM25, Hybrid RRF

> A large majority of the human knowledge is recorded through text documents. That is why ability for a system to automatically infer information from text without any structured data has become a major challenge. Answering questions about a given document is a relevant proxy task that has been proposed as a way to evaluate the reading ability of a given model. In this configuration, a text document such as a news article, a document from Wikipedia or any type of text is presented to a machine with an associated set of questions. The system is then expected to answer these questions and evaluated by its accuracy on this task. The machine reading framework is very general and we can imagine a large panel of questions that can possibly handle most of the standard natural language processing tasks. For example, the task of named entities recognition can be formulated as a machine reading one where your document is the sentence and the question would be 'What are the named entities mentioned in this sentence?'. These natural language interactions are an important objective for reading systems.
> 
> Recently, many datasets have been proposed to build and evaluate reading models BIBREF0 , BIBREF1 . From cloze style questions BIBREF2 to open questions BIBREF3 , from synthetic data BIBREF4 to human written articles BIBREF5 , many styles of documents and questions have been proposed to challenge reading models. The correct answer to the questions proposed in most of these datasets is a span of text of the source document, which can be restricted to a single word in several cases. It means that the answer should explicitly be present in the source document and that the model should be able to locate it.
> 
> Different models have already shown superhuman performance on several of these datasets and particularly on the SQuAD dataset composed of Wikipedia articles BIBREF6 , BIBREF7 . However, some limits of such models have been highlighted when they encounter perturbations into the input documents BIBREF8 . Indeed almost all of the state of the art models on the SQuAD dataset suffer from a lack of robustness against adversarial examples. Once the model is trained, a meaningless sentence added

#### Relevance 162

Label: 0

#### Passage 163

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> generate only a little set of relational questions. Figure FIGREF15 depicts the repartition of the answers in the generated dataset. A majority of the tasks we introduced, even if they possibly require a high level of understanding of the document and the question, are binary questions. It means that in the generated dataset the answers yes and no tend to be more present than the others. To balance in a better way the distribution of the answers, we chose to affect a higher probability of sampling to the task 5, 6, 7.1, 8. Indeed, these tasks are not binary questions and required an aspect name as the answer. Figure FIGREF17 represents the repartition of question types in our dataset. Finally, figure FIGREF15 shows the repartition of the answers in the dataset.

#### Relevance 163

Label: 1

#### Passage 164

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> Objective: Starting with the original corpus, we aim at building a machine reading task where natural language questions will challenge the model on its understanding of the reviews. Indeed learning relational reasoning competencies over natural language documents is a major challenge of the current reading models. These original raw data allow us to generate relational questions that can possibly require a global understanding of the comment and reasoning skills to be treated. For example, asking a question like What is the best aspect rated in this comment ? is not an easy question that can be answered without a deep understanding of the review. It is necessary to capture all the aspects mentioned in the text, to predict their rating and finally to select the best one. The tasks and the dataset we propose are publicly available at http://www.europe.naverlabs.com/Blog/ReviewQA-A-novel-relational-aspect-based-opinion-dataset-for-machine-reading
> 
> We introduce a list of 8 different competencies that a reading system should master in order to process reviews and text documents in general. These 8 tasks require different competencies and a different level of understanding of the document to be well answered. For instance, detecting if an aspect is mentioned in a review will require less understanding of the review than predicting explicitly the rating of this aspect. Table TABREF10 presents the 8 tasks we have introduced in this dataset with an example of a question that corresponds to each task. We also provide the expected type of the answer (Yes/No question, rating question...). It can be an additional tool to analyze the errors of the readers.

#### Relevance 164

Label: 1

#### Passage 165

Retrieved by: BM25, Dense, Hybrid RRF

> ReviewQA is proposed as a novel dataset regarding the collection of the existing ones. Indeed a large panel of available datasets, that evaluate models on different types of documents, can only be valuable for designing efficient models and learning protocols. In this following part, we describe several of these datasets.
> 
> SQuAD: The Standford Question Answering Dataset (SQuAD) introduced in BIBREF0 is a large dataset of natural questions over the 500 most popular articles of Wikipedia. All the questions have been crowdsourced and answers are spans of text extracted from source documents. This dataset has been very popular these last two years and the performance of the architectures that have been proposed have rapidly increased until several models surpass the human score. Indeed, in the original paper human performance has been measured at 82.304 points for the exact match metric and at the time we are writing this paper four models have already a higher score. In another hand BIBREF8 has shown that these models suffer from a lack of robustness against adversarial examples that are meaningless from a human point of view. This suggests the need for a more challenging dataset that will allow developing strongest reasoning architectures.
> 
> NewsQA: NewsQA BIBREF1 is a dataset very similar to SQuAD. It contains 120.000 human generated questions over 12.000 articles form CNN originally introduced in BIBREF5 . It has been designed to be more challenging than SQuAD with questions that might require to extract multiple spans of text or not be answerable.
> 
> WikiHop and MedHop: These are two recent datasets introduced in BIBREF13 . Unlike SQuAD and NewsQA, important facts are spread out across multiple documents and, in order to answer a question, it is necessary to jump over a set of passages to collect the required information. The relevant passages are not explicitly mentioned in the data so this dataset measures the ability that a model has to navigate across multiple documents. The questions come with a set of candidates which are all present in the text.
> 
> MS Marco: This dataset has been released in BIBREF14 . The documents come from the internet and the questions are real user queries asked through the bing search engine. The

#### Relevance 165

Label: 0

#### Passage 166

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> set of candidates which are all present in the text.
> 
> MS Marco: This dataset has been released in BIBREF14 . The documents come from the internet and the questions are real user queries asked through the bing search engine. The dataset contains around 100.000 queries and each of them comes with a set of approximatively 10 relevant passages. Like in SQuAD, several models are already doing superhuman performances on this dataset.
> 
> Facebook bAbI tasks: This is a set of 20 toy tasks proposed in BIBREF4 and designed to measure text understanding. Each task requires a certain capability to be completed like induction, deduction and more. Documents are synthetic stories, composed of few sentences that describe a set of actions. This dataset was one of the first attempt to introduce a general set of prerequisite capabilities required for the reading task. Although it has been a very challenging framework, beneficial to the emergence of the attention mechanism inside the reading architectures, a Gated end-to-end memory network BIBREF15 now succeed in almost all of the 20 tasks. One of the possible reason is that the data are synthetic data, without noise or ambiguity. We propose a comparable framework with understanding and reasoning tasks based on user-generated comments that are much more realistic and that required language competencies to be understood.
> 
> CLEVR: Beyond textual question-answering, Visual Question-Answering (VQA) has been largely studied during the last couple of years. More recently, the problem of relational reasoning has been introduced through this dataset BIBREF9 . The main original idea was to introduce relational reasoning questions over object shapes and placements. This dataset has already motivated the development of original deep models. To the best of our knowledge, no natural language question-answering corpus has been designed to investigate such capabilities. As we will present in the following of this paper, we think sentiment analysis is particularly suited for this task and we will introduce a novel machine reading corpus with such capability requirements.

#### Relevance 166

Label: 0

### BM25

None

### Dense

#### Passage 167

Retrieved by: Dense

> We sample 100.000 reviews from the original corpus. Figure FIGREF12 presents the distribution of the number of words of the reviews in the dataset. We explicitly favor reviews which contain an important number of words. In average, a review contains 200 words. Indeed these long reviews are most likely to contain challenging relations between different aspects. A short review which deals with only a few aspects is more likely to not be very relevant to the challenge we want to propose in this dataset. Figure FIGREF14 displays the distribution of the ratings per aspects in the 100.000 reviews we based our dataset. We can see that the average values of these ratings tend to be quite high. It could have introduced bias if it was not the case for all the aspects. For example, we do not want that the model learns that in general, the service is rated better than the location and them answer without looking at the document. Since this situation is the same for all the aspects, the relational tasks introduced in this dataset remains extremely relevant.
> 
> Then we randomly select 6 tasks for each review (the same task can be selected multiple times) and randomly select a natural language question that corresponds to this task. The questions are human-generated patterns that we have crowdsourced in order to produce a dataset as rich as possible. To this end, we have generated several patterns that correspond to the capabilities we wanted to express in a given question and we have crowdsourced rephrasing of these patterns.
> 
> The final dataset we propose is composed of more than 500.000 questions about 100.000 reviews. Table TABREF13 shows the repartition of the documents and queries into the train and test set. Each review contains a maximum of 6 questions. Sometimes less when it is not possible to generate all. For example, if only two or three aspects are mentioned in a review, we will be able to generate only a little set of relational questions. Figure FIGREF15 depicts the repartition of the answers in the generated dataset. A majority of the tasks we introduced, even if they possibly require a high level of understanding of the document

#### Relevance 167

Label: 0

#### Passage 168

Retrieved by: Dense

> encounter perturbations into the input documents BIBREF8 . Indeed almost all of the state of the art models on the SQuAD dataset suffer from a lack of robustness against adversarial examples. Once the model is trained, a meaningless sentence added at the end of the text document can completely disturb the reading system. Conversely, these adversarial examples do not seem to fool a human reader who will be capable of answering the questions as well as without this perturbation. One possible explanation of this phenomenon is that computers are good at extracting patterns in the document that match the representation of the question. If multiple spans of the documents look similar to the questions, the reader might not be able to decide which one is relevant. Moreover, Wikipedia articles tend to be written with the same standard writing style, factual, unambiguous. Such writing style tends to favor the pattern matching between the questions and the documents. This format of documents/questions has certainly influenced the design of the comprehension models that have been proposed so far. Most of them are composed of stacked attention layers that match question and document representations.
> 
> Following concepts proposed in the 20 bAbI tasks BIBREF4 or in the visual question-answering dataset CLEVR BIBREF9 , we think that the challenge, limited to the detection of relevant passages in a document, is only the first step in building systems that truly understand text. The second step is the ability of reasoning with the relevant information extracted from a document. To set up this challenge, we propose to leverage on a hotel reviews corpus that requires reasoning skills to answer natural language questions. The reviews we used have been extracted from TripAdvisor and originally proposed in BIBREF10 , BIBREF11 . In the original data, each review comes with a set of rated aspects among the seventh available: Business service, Check in / Front Desk, Cleanliness, Location, Room, Sleep Quality, Value and for all the reviews an Overall rating. In this articles we propose to exploit these data to create a dataset of question-answering that will challenge 8 competencies of the reader.
> 
> Our contributions can be summarized as follow:

#### Relevance 168

Label: 1

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 169

Retrieved by: Hybrid RRF followed by BGE reranking

> Sentiment analysis is one of the historical tasks of Natural Language Processing. It is an important challenge for companies, restaurants, hotels that aim to analyze customer satisfaction regarding products and quality of services. Given a text document, the objective is to predict its overall polarity. Generally, it can be positive, negative or neutral. This analysis gives a quick overview of a general sentiment over a set of documents, but this framework tends to be restrictive. Indeed, one document tends to express multiple opinions of different aspects. For instance, in the sentence: The fish was very good but the service was terrible, there is not a general dominant sentiment, and a finer analysis is needed. The task of aspect-based sentiment analysis aims to predict a polarity of a sentence regarding a given aspect. In the previous example a positive polarity should be associated to the aspect food, and on the contrary, a negative sentiment is expressed regarding the quality of the service.
> 
> The idea of using models originally designed for question-answering, for the sentiment analysis task has been introduced in BIBREF16 , BIBREF17 . In these papers, several adaptations of the end-to-end memory network (MemN2N) BIBREF18 are used to predict the polarity of a review regarding a given aspect. In that configuration, the review is encoded into the memory cells and the controller, usually initialized with a representation of the question, is initialized with a representation of the aspect. The analysis of the attention between the values of the controller and the document has shown interesting results, by highlighting relevant part of a document regarding an aspect.

#### Relevance 169

Label: 0

## Question 0020

Paper: Dice Loss for Data-imbalanced NLP Tasks

> How are weights dynamically adjusted?

### Common Retrieved Chunks

#### Passage 170

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The idea of weighting training examples has a long history. Importance sampling BIBREF17 assigns weights to different samples and changes the data distribution. Boosting algorithms such as AdaBoost BIBREF18 select harder examples to train subsequent classifiers. Similarly, hard example mining BIBREF19 downsamples the majority class and exploits the most difficult examples. Oversampling BIBREF20, BIBREF21 is used to balance the data distribution. Another line of data resampling is to dynamically control the weights of examples as training proceeds. For example, focal loss BIBREF16 used a soft weighting scheme that emphasizes harder examples during training. In self-paced learning BIBREF22, example weights are obtained through optimizing the weighted training loss which encourages learning easier examples first. At each training step, self-paced learning algorithm optimizes model parameters and example weights jointly. Other works BIBREF23, BIBREF24 adjusted the weights of different training examples based on training loss. Besides, recent work BIBREF25, BIBREF26 proposed to learn a separate network to predict sample weights.

#### Relevance 170

Label: 0

#### Passage 171

Retrieved by: BM25, Dense, Hybrid RRF

> The vanilla cross entropy (CE) loss is given by:
> 
> As can be seen from Eq.DISPLAY_FORM8, each $x_i$ contributes equally to the final objective. Two strategies are normally used to address the the case where we wish that not all $x_i$ are treated equal: associating different classes with different weighting factor $\alpha $ or resampling the datasets. For the former, Eq.DISPLAY_FORM8 is adjusted as follows:
> 
> where $\alpha _i\in [0,1]$ may be set by the inverse class frequency or treated as a hyperparameter to set by cross validation. In this work, we use $\lg (\frac{n-n_t}{n_t}+K)$ to calculate the coefficient $\alpha $, where $n_t$ is the number of samples with class $t$ and $n$ is the total number of samples in the training set. $K$ is a hyperparameter to tune. The data resampling strategy constructs a new dataset by sampling training examples from the original dataset based on human-designed criteria, e.g., extract equal training samples from each class. Both strategies are equivalent to changing the data distribution and thus are of the same nature. Empirically, these two methods are not widely used due to the trickiness of selecting $\alpha $ especially for multi-class classification tasks and that inappropriate selection can easily bias towards rare classes BIBREF32.

#### Relevance 171

Label: 0

#### Passage 172

Retrieved by: BM25, Dense, Hybrid RRF

> As mentioned in Section SECREF10, Tversky index (TI) offers the flexibility in controlling the tradeoff between false-negatives and false-positives. In this subsection, we explore the effect of hyperparameters (i.e., $\alpha $ and $\beta $) in TI to test how they manipulate the tradeoff. We conduct experiments on the Chinese OntoNotes4.0 NER dataset and English QuoRef MRC dataset to examine the influence of tradeoff between precision and recall. Experiment results are shown in Table . The highest F1 for Chinese OntoNotes4.0 is 84.67 when $\alpha $ is set to 0.6 while for QuoRef, the highest F1 is 68.44 when $\alpha $ is set to 0.4. In addition, we can observe that the performance varies a lot as $\alpha $ changes in distinct datasets, which shows that the hyperparameters $\alpha ,\beta $ play an important role in the proposed method.

#### Relevance 172

Label: 0

#### Passage 174

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> of the $F_{\beta }$ score, and thus comes with more flexibility. Therefore, We use dice loss or Tversky index to replace CE loss to address the first issue.
> 
> Only using dice loss or Tversky index is not enough since they are unable to address the dominating influence of easy-negative examples. This is intrinsically because dice loss is actually a hard version of the F1 score. Taking the binary classification task as an example, at test time, an example will be classified as negative as long as its probability is smaller than 0.5, but training will push the value to 0 as much as possible. This gap isn't a big issue for balanced datasets, but is extremely detrimental if a big proportion of training examples are easy-negative ones: easy-negative examples can easily dominate training since their probabilities can be pushed to 0 fairly easily. Meanwhile, the model can hardly distinguish between hard-negative examples and positive ones. Inspired by the idea of focal loss BIBREF16 in computer vision, we propose a dynamic weight adjusting strategy, which associates each training example with a weight in proportion to $(1-p)$, and this weight dynamically changes as training proceeds. This strategy helps to deemphasize confident examples during training as their $p$ approaches the value of 1, makes the model attentive to hard-negative examples, and thus alleviates the dominating effect of easy-negative examples.
> 
> Combing both strategies, we observe significant performance boosts on a wide range of data imbalanced NLP tasks. Notably, we are able to achieve SOTA results on CTB5 (97.92, +1.86), CTB6 (96.57, +1.80) and UD1.4 (96.98, +2.19) for the POS task; SOTA results on CoNLL03 (93.33, +0.29), OntoNotes5.0 (92.07, +0.96)), MSRA 96.72(+0.97) and OntoNotes4.0 (84.47,+2.36) for the NER task; along with competitive results on the tasks of machine reading comprehension and paraphrase identification.
> 
> The rest of this paper is organized as follows: related work is presented in Section 2. We describe different training objectives in Section 3. Experimental results are presented in Section 4. We perform ablation studies in Section 5, followed by a brief conclusion in Section 6.

#### Relevance 174

Label: 1

### BM25

#### Passage 173

Retrieved by: BM25

> For illustration purposes, we use the binary classification task to demonstrate how different losses work. The mechanism can be easily extended to multi-class classification.
> 
> Let $\lbrace x_i\rbrace $ denote a set of instances. Each $x_i$ is associated with a golden label vector $y_i = [y_{i0},y_{i1} ]$, where $y_{i1}\in \lbrace 0,1\rbrace $ and $y_{i0}\in \lbrace 0,1\rbrace $ respectively denote the positive and negative classes, and thus $y_i$ can be either $[0,1]$ or $[0,1]$. Let $p_i = [p_{i0},p_{i1} ]$ denote the probability vector, and $p_{i1}$ and $p_{i0}$ respectively denote the probability that a model assigns the positive and negative label to $x_i$.

#### Relevance 173

Label: 0

### Dense

#### Passage 175

Retrieved by: Dense

> Data imbalance is a common issue in a variety of NLP tasks such as tagging and machine reading comprehension. Table TABREF3 gives concrete examples: for the Named Entity Recognition (NER) task BIBREF2, BIBREF3, most tokens are backgrounds with tagging class $O$. Specifically, the number of tokens tagging class $O$ is 5 times as many as those with entity labels for the CoNLL03 dataset and 8 times for the OntoNotes5.0 dataset; Data-imbalanced issue is more severe for MRC tasks BIBREF4, BIBREF5, BIBREF6, BIBREF7, BIBREF8 with the value of negative-positive ratio being 50-200.
> 
> Data imbalance results in the following two issues: (1) the training-test discrepancy: Without balancing the labels, the learning process tends to converge to a point that strongly biases towards class with the majority label. This actually creates a discrepancy between training and test: at training time, each training instance contributes equally to the objective function while at test time, F1 score concerns more about positive examples; (2) the overwhelming effect of easy-negative examples. As pointed out by meng2019dsreg, significantly large number of negative examples also means that the number of easy-negative example is large. The huge number of easy examples tends to overwhelm the training, making the model not sufficiently learned to distinguish between positive examples and hard-negative examples. The cross-entropy objective (CE for short) or maximum likelihood (MLE) objective, which is widely adopted as the training objective for data-imbalanced NLP tasks BIBREF9, BIBREF10, BIBREF11, BIBREF12, BIBREF13, BIBREF14, BIBREF15, handles neither of the issues.
> 
> To handle the first issue, we propose to replace CE or MLE with losses based on the Sørensen–Dice coefficient BIBREF0 or Tversky index BIBREF1. The Sørensen–Dice coefficient, dice loss for short, is the harmonic mean of precision and recall. It attaches equal importance to false positives (FPs) and false negatives (FNs) and is thus more immune to data-imbalanced datasets. Tversky index extends dice loss by using a weight that trades precision and recall, which can be thought as the approximation of the $F_{\beta }$ score, and thus comes with more flexibility. Therefore, We use dice loss or Tversky index to replace CE loss to address the first issue.
> 
> Only using dice loss or Tversky index is not enough since they

#### Relevance 175

Label: 0

### Hybrid RRF

#### Passage 176

Retrieved by: Hybrid RRF

> Consider a simple case where the dataset consists of only one example $x_i$, which is classified as positive as long as $p_{i1}$ is larger than 0.5. The computation of $F1$ score is actually as follows:
> 
> Comparing Eq.DISPLAY_FORM14 with Eq.DISPLAY_FORM22, we can see that Eq.DISPLAY_FORM14 is actually a soft form of $F1$, using a continuous $p$ rather than the binary $\mathbb {I}( p_{i1}>0.5)$. This gap isn't a big issue for balanced datasets, but is extremely detrimental if a big proportion of training examples are easy-negative ones: easy-negative examples can easily dominate training since their probabilities can be pushed to 0 fairly easily. Meanwhile, the model can hardly distinguish between hard-negative examples and positive ones, which has a huge negative effect on the final F1 performance.
> 
> To address this issue, we propose to multiply the soft probability $p$ with a decaying factor $(1-p)$, changing Eq.DISPLAY_FORM22 to the following form:
> 
> One can think $(1-p_{i1})$ as a weight associated with each example, which changes as training proceeds. The intuition of changing $p_{i1}$ to $(1-p_{i1}) p_{i1}$ is to push down the weight of easy examples. For easy examples whose probability are approaching 0 or 1, $(1-p_{i1}) p_{i1}$ makes the model attach significantly less focus to them. Figure FIGREF23 gives gives an explanation from the perspective in derivative: the derivative of $\frac{(1-p)p}{1+(1-p)p}$ with respect to $p$ approaches 0 immediately after $p$ approaches 0, which means the model attends less to examples once they are correctly classified.
> 
> A close look at Eq.DISPLAY_FORM14 reveals that it actually mimics the idea of focal loss (FL for short) BIBREF16 for object detection in vision. Focal loss was proposed for one-stage object detector to handle foreground-background tradeoff encountered during training. It down-weights the loss assigned to well-classified examples by adding a $(1-p)^{\beta }$ factor, leading the final loss to be $(1-p)^{\beta }\log p$.
> 
> In Table TABREF18, we show the losses used in our experiments, which is described in the next section.

#### Relevance 176

Label: 1

### Hybrid RRF followed by BGE reranking

#### Passage 177

Retrieved by: Hybrid RRF followed by BGE reranking

> We evaluate the proposed method on four NLP tasks: part-of-speech tagging, named entity recognition, machine reading comprehension and paraphrase identification. Baselines in our experiments are optimized by using the standard cross-entropy training objective.

#### Relevance 177

Label: 0

#### Passage 178

Retrieved by: Hybrid RRF followed by BGE reranking

> Machine reading comprehension (MRC) BIBREF39, BIBREF40, BIBREF41, BIBREF40, BIBREF42, BIBREF15 has become a central task in natural language understanding. MRC in the SQuAD-style is to predict the answer span in the passage given a question and the passage. In this paper, we choose the SQuAD-style MRC task and report Extract Match (EM) in addition to F1 score on validation set. All hyperparameters are tuned on the development set of each dataset.

#### Relevance 178

Label: 0

#### Passage 179

Retrieved by: Hybrid RRF followed by BGE reranking

> In this paper, we alleviate the severe data imbalance issue in NLP tasks. We propose to use dice loss in replacement of the standard cross-entropy loss, which performs as a soft version of F1 score. Using dice loss can help narrow the gap between training objectives and evaluation metrics. Empirically, we show that the proposed training objective leads to significant performance boost for part-of-speech, named entity recognition, machine reading comprehension and paraphrase identification tasks.

#### Relevance 179

Label: 0
