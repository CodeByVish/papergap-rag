# Passage relevance annotation

Annotator: 

Judge whether the passage provides information that helps answer the question, including useful partial evidence. Topic overlap alone is not sufficient. Judge only the supplied question and passage.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Do not change record numbers, questions or passages. Work independently without consulting another annotator or reference answers.

## Record 0001

Paper: Machine Translation with Cross-lingual Word Embeddings

### Question

> Are any experiments performed to try this approach to word embeddings?

### Passage

> In recent years, various models for learning cross-lingual representations have been proposed. Two main broad categories with some related papers are identified here:
> 
> Monolingual mapping: In this approach, models are trained using word embeddings from a monolingual corpora. Then, an objective function is used to minimize a linear mapping that enable them to map unknown words from the source language to the target language.
> 
> Pseudo-cross-lingual: In this case we create a pseudo-cross-lingual corpus by mixing contexts of different languages. We then train an off-the-shelf word embedding model on the created corpus. Ideally the cross-lingual contexts allow the learned representations to capture cross-lingual relations.

### Relevance

Label: 

## Record 0002

Paper: Machine Translation with Cross-lingual Word Embeddings

### Question

> Are any experiments performed to try this approach to word embeddings?

### Passage

> Methods for machine translations have been studied for years, and at the same time algorithms to generate word embeddings are becoming more and more accurate. Still, there is a lot of research aiming at unifying word embeddings across multiple languages. In this experience we try a technique for machine translation that relates word embeddings between two different languages. Based on the literature we found that it is possible to infer missing dictionary entries using distributed representations of words and phrases. One way of doing it is to create a linear mapping between the two vector spaces of two different languages. In order to achieve this, we first built two dictionaries of the two different languages. Next, we learned a function that projects the first vector space to the second one. In this way, we are able to translate every word belonging to the first language into the second one. Once we obtain the translated word embedding, we output the most similar word vector as the translation. The word embeddings were learnt using the Skip Gram method proposed by (Mikolov et al., 2013a). An example of how the method would work is reported in figure 1 and figure 2. After creating the word embeddings from the two dictionaries, we plotted the numbers in the two graphs using PCA. Figure 3 reports the results after creating a linear mapping between the embeddings from the two languages. You can see how similar words are closer together.

### Relevance

Label: 

## Record 0003

Paper: Machine Translation with Cross-lingual Word Embeddings

### Question

> Are any experiments performed to try this approach to word embeddings?

### Passage

> It was recently shown that the distributed representations of words capture surprisingly many linguistic regularities, and that there are many types of similarities among words that can be expressed as linear translations (Mikolov et al., 2013c). In the Skip-gram model, the training objective is to learn word vector representations that are good at predicting its context in the same sentence (Mikolov et al., 2013a). The objective function that skip gram tries to minimize is the following:
> 
> Where N represents the total number of words in a sentence, P the probability of a word at the position i+j to belong to the sentence, with respect to the word i. Ideally, by using this approach we will be able to provide non-trivial translations that will be related to the context of a word.

### Relevance

Label: 

## Record 0004

Paper: Machine Translation with Cross-lingual Word Embeddings

### Question

> Are any experiments performed to try this approach to word embeddings?

### Passage

> This represents the linear function that maps word embeddings from one language to another. Given a word x in one language, and the respective word in the other language z, the following equation reports the objective function we want to minimize:
> 
> Were W represents the final matrix that will contain the values for the mapping.

### Relevance

Label: 

## Record 0005

Paper: Machine Translation with Cross-lingual Word Embeddings

### Question

> Are any experiments performed to try this approach to word embeddings?

### Passage

> In order to minimize the loss function we decided to setup a neural network and reduce the objective by using Stochastic Gradient Descent. Figure 4 represents the architecture of our base model. We repeated the same process both for objective functions expressed in equation DISPLAY_FORM8 and DISPLAY_FORM12. We started by getting an English word from the English corpus and we got the corresponding target word by using Google Translate. If this word was contained in the target corpus, this pair of words was used to train the model; otherwise, it was ignored. We then get the two embeddings and get the result by multiplying the first one by the matrix W and then substracting the second embedding. For this experiment, we used embeddings with a dimension of 100. For this reason W is a matrix of size 100*100.

### Relevance

Label: 

## Record 0006

Paper: Short Text Language Identification for Under Resourced Languages

### Question

> What evaluation metric is used?

### Passage

> The focus of this section is on recently published datasets and LID research applicable to the South African context. An in depth survey of algorithms, features, datasets, shared tasks and evaluation methods may be found in BIBREF0.
> 
> The datasets for the DSL 2015 & DSL 2017 shared tasks BIBREF1 are often used in LID benchmarks and also available on Kaggle . The DSL datasets, like other LID datasets, consists of text sentences labelled by language. The 2017 dataset, for example, contains 14 languages over 6 language groups with 18000 training samples and 1000 testing samples per language.
> 
> The recently published JW300 parallel corpus BIBREF2 covers over 300 languages with around 100 thousand parallel sentences per language pair on average. In South Africa, a multilingual corpus of academic texts produced by university students with different mother tongues is being developed BIBREF3. The WiLI-2018 benchmark dataset BIBREF4 for monolingual written natural language identification includes around 1000 paragraphs of 235 languages. A possibly useful link can also be made BIBREF5 between Native Language Identification (NLI) (determining the native language of the author of a text) and Language Variety Identification (LVI) (classification of different varieties of a single language) which opens up more datasets. The Leipzig Corpora Collection BIBREF6, the Universal Declaration of Human Rights and Tatoeba are also often used sources of data.
> 
> The NCHLT text corpora BIBREF7 is likely a good starting point for a shared LID task dataset for the South African languages BIBREF8. The NCHLT text corpora contains enough data to have 3500 training samples and 600 testing samples of 300+ character sentences per language. Researchers have recently started applying existing algorithms for tasks like neural machine translation in earnest to such South African language datasets BIBREF9.
> 
> Existing NLP datasets, models and services BIBREF10 are available for South African languages. These include an LID algorithm BIBREF11 that uses a character level n-gram language model. Multiple papers have shown that 'shallow' naive Bayes classifiers BIBREF12, BIBREF8, BIBREF13, BIBREF14, SVMs BIBREF15 and similar models work very well for doing LID. The DSL 2017 paper BIBREF1, for example, gives an overview of the solutions of all of the teams that competed on the shared task and the winning

### Relevance

Label: 

## Record 0007

Paper: Short Text Language Identification for Under Resourced Languages

### Question

> What evaluation metric is used?

### Passage

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

### Relevance

Label: 

## Record 0008

Paper: Short Text Language Identification for Under Resourced Languages

### Question

> What evaluation metric is used?

### Passage

> BIBREF13, BIBREF14, SVMs BIBREF15 and similar models work very well for doing LID. The DSL 2017 paper BIBREF1, for example, gives an overview of the solutions of all of the teams that competed on the shared task and the winning approach BIBREF16 used an SVM with character n-gram, parts of speech tag features and some other engineered features. The winning approach for DSL 2015 used an ensemble naive Bayes classifier. The fasttext classifier BIBREF17 is perhaps one of the best known efficient 'shallow' text classifiers that have been used for LID .
> 
> Multiple papers have proposed hierarchical stacked classifiers (including lexicons) that would for example first classify a piece of text by language group and then by exact language BIBREF18, BIBREF19, BIBREF8, BIBREF0. Some work has also been done on classifying surnames between Tshivenda, Xitsonga and Sepedi BIBREF20. Additionally, data augmentation BIBREF21 and adversarial training BIBREF22 approaches are potentially very useful to reduce the requirement for data.
> 
> Researchers have investigated deeper LID models like bidirectional recurrent neural networks BIBREF23 or ensembles of recurrent neural networks BIBREF24. The latter is reported to achieve 95.12% in the DSL 2015 shared task. In these models text features can include character and word n-grams as well as informative character and word-level features learnt BIBREF25 from the training data. The neural methods seem to work well in tasks where more training data is available.
> 
> In summary, LID of short texts, informal styles and similar languages remains a difficult problem which is actively being researched. Increased confusion can in general be expected between shorter pieces of text and languages that are more closely related. Shallow methods still seem to work well compared to deeper models for LID. Other remaining research opportunities seem to be data harvesting, building standardised datasets and creating shared tasks for South Africa and Africa. Support for language codes that include more languages seems to be growing and discoverability of research is improving with more survey papers coming out. Paywalls also seem to no longer be a problem; the references used in this paper was either openly published or available as preprint papers.

### Relevance

Label: 

## Record 0009

Paper: Short Text Language Identification for Under Resourced Languages

### Question

> What evaluation metric is used?

### Passage

> LID of short texts, informal styles and similar languages remains a difficult problem which is actively being researched. The proposed algorithm was evaluated on three existing datasets and compared to the implementations of three public LID implementations as well as to reported results of four other algorithms. It performed well relative to the other methods beating their results. However, the performance is dependent on the support of the lexicon.
> 
> We would like to investigate the value of a lexicon in a production system and how to possibly maintain it using self-supervised learning. We are investigating the application of deeper language models some of which have been used in more recent DSL shared tasks. We would also like to investigate data augmentation strategies to reduce the amount of training data that is required.
> 
> Further research opportunities include data harvesting, building standardised datasets and shared tasks for South Africa as well as the rest of Africa. In general, the support for language codes that include more languages seems to be growing, discoverability of research is improving and paywalls seem to no longer be a big problem in getting access to published research.

### Relevance

Label: 

## Record 0010

Paper: Short Text Language Identification for Under Resourced Languages

### Question

> What evaluation metric is used?

### Passage

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

### Relevance

Label: 

## Record 0011

Paper: Fine-Grained Named Entity Recognition using ELMo and Wikidata

### Question

> What results do they achieve using their proposed approach?

### Passage

> The results for each class type are shown in Table TABREF19 , with some specific examples shown in Figure FIGREF18 . For the Wiki(gold) we quote the micro-averaged F-1 scores for the entire top level entity category. The total F-1 score on the OntoNotes dataset is 88%, and the total F-1 cross-validation score on the 112 class Wiki(gold) dataset is 53%. It is worth noting that one could improve Wiki(gold) results by training directly using this dataset. However, the aim is not to tune our model specifically on this class hierarchy. We instead aim to present a framework which can be modified easily to any domain hierarchy and has acceptable out-of-the-box performances to any fine-grained dataset. The results in Table TABREF19 (OntoNotes) only show the main 7 categories in OntoNotes which map to Wiki(gold) for clarity. The other categories (date, time, norp, language, ordinal, cardinal, quantity, percent, money, law) have F-1 scores between 80-90%, with the exception of time (65%)

### Relevance

Label: 

## Record 0012

Paper: Fine-Grained Named Entity Recognition using ELMo and Wikidata

### Question

> What results do they achieve using their proposed approach?

### Passage

> Entity linking (EL) BIBREF24 , also known as named entity disambiguation or normalization, is the task to determine the identity of entities mentioned in a piece of text with reference to a knowledge base. There are a number of knowledge bases that provide a background repository for entity classification of this type. For this study, we use Wikidata, which can be seen diagrammatically in Figure FIGREF12 . Systems such as DeepType BIBREF25 integrate symbolic information into the reasoning process of a neural network with a type system and show state-of-the-art performances for EL. They do not, however, quote results on Wiki(gold) so a direct comparison is difficult.
> 
> While these knowledge bases provide semantically rich and fine-granular classes and relationship types, the task of entity classification often requires associating coarse-grained classes with discovered surface forms of entities. Most existing studies consider NER and entity linking as two separate tasks, whereas we try to combine the two. It has been shown that one can significantly increase the semantic information carried by a NER system when we successfully linking entities from a deep learning method to the related entities from a knowledge base BIBREF26 , BIBREF27 .
> 
> Redirection: For the Wikidata linking element, we recognize that the lookup will be constrained by the most common lookup name for each entity. Consider the utterance (referring to the NBA basketball player) from Figure FIGREF12 “Michael Jeffrey Jordan in San Jose” as an example. The lookup for this entity in Wikidata is “Michael Jordan” and consequently will not be picked up if we were to use an exact string match. A simple method to circumvent such a problem is the usage of a redirection list. Such a list is provided on an entity by entity basis in the “Also known as” section in Wikidata. Using this redirection list, when we do not find an exact string match improves the recall of our model by 5-10%. Moreover, with the example of Michael Jordan (person), using our current framework, we will always refer to the retired basketball player (Q41421). We will never, for instance, pick up Michael Jordan (Q27069141) the American football cornerback. Or in fact any other Michael Jordan, famous or otherwise.

### Relevance

Label: 

## Record 0013

Paper: Fine-Grained Named Entity Recognition using ELMo and Wikidata

### Question

> What results do they achieve using their proposed approach?

### Passage

> Named entity recognition (NER) BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 is the process by which we identify text spans which mention named entities, and to classify them into predefined categories such as person, location, organization etc. NER serves as the basis for a variety of natural language processing (NLP) applications such as relation extraction BIBREF4 , machine translation BIBREF5 , question answering BIBREF6 and knowledge base construction BIBREF7 . Although early NER systems have been successful in producing adequate recognition accuracy, they often require significant human effort in carefully designing rules or features.
> 
> In recent years, deep learning methods been employed in NER systems, yielding state-of-the-art performance. However, the number of types detected are still not sufficient for certain domain-specific applications. For relation extraction, identifying fine-grained types has been shown to significantly increase the performance of the extractor BIBREF8 , BIBREF9 since this helps in filtering out candidate relation types which do not follow this type constraint. Furthermore, for question answering fine-grained Named Entity Recognition (FgNER) can provide additional information helping to match questions to its potential answers thus improving performance BIBREF10 . For example, Li and Roth BIBREF11 rank questions based on their expected answer types (i.e. will the answer be food, vehicle or disease).
> 
> Typically, FgNER systems use over a hundred labels, arranged in a hierarchical structure. We find that available training data for FgNER typically contain noisy labels, and creating manually annotated training data for FgNER is a time-consuming process. Furthermore, human annotators will have to assign a subset of correct labels from hundreds of possible labels making this a somewhat arduous task. Currently, FgNER systems use distant supervision BIBREF12 to automatically generate training data. Distant supervision is a technique which maps each entity in the corpus to knowledge bases such as Freebase BIBREF13 , DBpedia BIBREF14 , YAGO BIBREF15 and helps with the generation of labeled data. This method will assign the same set of labels to all mentions of a particular entity in the corpus. For example, “Barack Obama” is a person, politician, lawyer, and author. If a knowledge base has these four matching labels, the distant supervision technique will assign all of them to every mention of “Barack

### Relevance

Label: 

## Record 0014

Paper: Fine-Grained Named Entity Recognition using ELMo and Wikidata

### Question

> What results do they achieve using their proposed approach?

### Passage

> NER involves identifying both entity boundaries and entity types. With “exact-match evaluation”, a named entity is considered correctly recognized only if both the boundaries and type match the ground truth BIBREF8 , BIBREF17 , BIBREF18 . Precision, Recall, and F-1 scores are computed on the number of true positives (TP), false positives (FP), and false negatives (FN). Their formal definitions are as follows:
> 
> True Positive (TP): entities that are recognized by NER and match the ground truth.
> 
> False Positive (FP): entities that are recognized by NER but do not match the ground truth.
> 
> False Negative (FN): entities annotated in the ground which that are not recognized by NER.
> 
> Precision measures the ability of a NER system to present only correct entities, and Recall measures the ability of a NER system to recognize all entities in a corpus. DISPLAYFORM0
> 
> The F-1 score is the harmonic mean of precision and recall, and the balanced F-1 score is the variant which is most commonly used. This is defined as: DISPLAYFORM0
> 
> Since most NER systems involve multiple entity types, it is often required to assess the performance across all entity classes. Two measures are commonly used for this purpose: the macro-averaged F-1 score and the micro-averaged F-1 score. The macro-averaged F-1 score computes the F-1 score independently for each entity type, then takes the average (hence treating all entity types equally). The micro-averaged F-1 score aggregates the contributions of entities from all classes to compute the average (treating all entities equally). We use the micro-averaged F-1 in our study since this accounts for label imbalances in the evaluation data and therefore a more meaningful statistic.

### Relevance

Label: 

## Record 0015

Paper: Fine-Grained Named Entity Recognition using ELMo and Wikidata

### Question

> What results do they achieve using their proposed approach?

### Passage

> a particular entity in the corpus. For example, “Barack Obama” is a person, politician, lawyer, and author. If a knowledge base has these four matching labels, the distant supervision technique will assign all of them to every mention of “Barack Obama”. Therefore, the training data will also fail to distinguish between mentions of “Barack Obama” in all subsequent utterances.
> 
> Ling et al. ling2012fine proposed the first system for FgNER, where they used 112 overlapping labels with a linear classifier perceptron for multi-label classification. Yosef et al. spaniol2012hyena used multiple binary SVM classifiers to assign entities to a set of 505 types. Gillick et al. gillick2014context introduced context dependent FgNER and proposed a set of heuristics for pruning labels that might not be relevant given the local context of the entity. Yogatama et al. yogatama2015embedding proposed an embedding based model where user-defined features and labels were embedded into a low dimensional feature space to facilitate information sharing among labels.
> 
> Shimaoka et al. shimaoka2016attentive proposed an attentive neural network model which used long short-term memory (LSTMs) to encode the context of the entity, then used an attention mechanism to allow the model to focus on relevant expressions in the entity mention's context. To learn entity representations, we propose a scheme which is potentially more generalizable.

### Relevance

Label: 

## Record 0016

Paper: Gating Mechanisms for Combining Character and Word-level Word Representations: An Empirical Study

### Question

> Which model architecture do they use to obtain representations?

### Passage

> To the best of our knowledge, there are only two recent works that specifically study how to combine word and subword-level vector representations.
> 
> BIBREF11 propose to use a trainable scalar gating mechanism capable of learning a weighting scheme for combining character-level and word-level representations. They compared their proposed method to manually weighting both levels; using characters only; words only; or their concatenation. They found that in some datasets a specific manual weighting scheme performed better, while in others the learned scalar gate did.
> 
> BIBREF12 further expand the gating concept by making the mechanism work at a finer-grained level, learning how to weight each vector's dimensions independently, conditioned on external word-level features such as part-of-speech and named-entity tags. Similarly, they compared their proposed mechanism to using words only, characters only, and a concatenation of both, with and without external features. They found that their vector gate performed better than the other methods in all the reported tasks, and beat the state of the art in two reading comprehension tasks.
> 
> Both works showed that the gating mechanisms assigned greater importance to character-level representations in rare words, and to word-level representations in common ones, reaffirming the previous findings that subword structures in general, and characters in particular, are beneficial for modeling uncommon words.

### Relevance

Label: 

## Record 0017

Paper: Gating Mechanisms for Combining Character and Word-level Word Representations: An Empirical Study

### Question

> Which model architecture do they use to obtain representations?

### Passage

> The problem of representing sentences as fixed-length vectors has been widely studied.
> 
> BIBREF32 suggested a self-adaptive hierarchical model that gradually composes words into intermediate phrase representations, and adaptively selects specific hierarchical levels for specific tasks. BIBREF33 proposed an encoder-decoder model trained by attempting to reconstruct the surrounding sentences of an encoded passage, in a fashion similar to Skip-gram BIBREF34 . BIBREF35 overcame the previous model's need for ordered training sentences by using autoencoders for creating the sentence representations. BIBREF36 implemented a model simpler and faster to train than the previous two, while having competitive performance. Similar to BIBREF33 , BIBREF37 suggested predicting future sentences with a hierarchical CNN-LSTM encoder.
> 
> BIBREF13 trained several sentence encoding architectures on a combination of the SNLI and MultiNLI datasets, and showed that a BiLSTM with max-pooling was the best at producing highly transferable sentence representations. More recently, BIBREF18 empirically showed that sentence representations created in a multi-task setting BIBREF38 , performed increasingly better the more tasks they were trained in. BIBREF39 proposed using an autoencoder that relies on multi-head self-attention over the concatenation of the max and mean pooled encoder outputs for producing sentence representations. Finally, BIBREF40 show that modern sentence embedding methods are not vastly superior to random methods.
> 
> The works mentioned so far usually evaluate the quality of the produced sentence representations in sentence-level downstream tasks. Common benchmarks grouping these kind of tasks include SentEval BIBREF23 , and GLUE BIBREF41 . Another trend, however, is to probe sentence representations to understand what linguistic phenomena they encode BIBREF42 , BIBREF43 , BIBREF44 , BIBREF45 , BIBREF46 .

### Relevance

Label: 

## Record 0018

Paper: Gating Mechanisms for Combining Character and Word-level Word Representations: An Empirical Study

### Question

> Which model architecture do they use to obtain representations?

### Passage

> To enable sentence-level classification we need to obtain a sentence representation from the word vectors INLINEFORM0 . We achieved this by using a BiLSTM with max pooling, which was shown to be a good universal sentence encoding mechanism BIBREF13 .
> 
> Let INLINEFORM0 , be an input sentence and INLINEFORM1 its matrix representation, where each INLINEFORM2 was obtained by one of the methods described in subsec:methods. INLINEFORM3 is the context-enriched matrix representation of INLINEFORM4 obtained by feeding INLINEFORM5 to a BiLSTM of output dimension INLINEFORM6 . Lastly, INLINEFORM11 is the final sentence representation of INLINEFORM12 obtained by max-pooling INLINEFORM13 along the sequence dimension.
> 
> Finally, we initialized the word representations INLINEFORM0 using GloVe embeddings BIBREF14 , and fine-tuned them during training. Refer to app:hyperparams for details on the other hyperparameters we used.

### Relevance

Label: 

## Record 0019

Paper: Gating Mechanisms for Combining Character and Word-level Word Representations: An Empirical Study

### Question

> Which model architecture do they use to obtain representations?

### Passage

> Incorporating sub-word structures like substrings, morphemes and characters to the creation of word representations significantly increases their quality as reflected both by intrinsic metrics and performance in a wide range of downstream tasks BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 .
> 
> The reason for this improvement is related to sub-word structures containing information that is usually ignored by standard word-level models. Indeed, when representing words as vectors extracted from a lookup table, semantically related words resulting from inflectional processes such as surf, surfing, and surfed, are treated as being independent from one another. Further, word-level embeddings do not account for derivational processes resulting in syntactically-similar words with different meanings such as break, breakable, and unbreakable. This causes derived words, which are usually less frequent, to have lower-quality (or no) vector representations.
> 
> Previous works have successfully combined character-level and word-level word representations, obtaining overall better results than using only word-level representations. For example BIBREF1 achieved state-of-the-art results in a machine translation task by representing unknown words as a composition of their characters. BIBREF4 created word representations by adding the vector representations of the words' surface forms and their morphemes ( INLINEFORM0 ), obtaining significant improvements on intrinsic evaluation tasks, word similarity and machine translation. BIBREF5 concatenated character-level and word-level representations for creating word representations, and then used them as input to their models for obtaining state-of-the-art results in Named Entity Recognition on several languages.
> 
> What these works have in common is that the models they describe first learn how to represent subword information, at character BIBREF1 , morpheme BIBREF4 , or substring BIBREF0 levels, and then combine these learned representations at the word level. The incorporation of information at a finer-grained hierarchy results in higher-quality modeling of rare words, morphological processes, and semantics BIBREF6 .
> 
> There is no consensus, however, on which combination method works better in which case, or how the choice of a combination method affects downstream performance, either measured intrinsically at the word level, or extrinsically at the sentence level.
> 
> In this paper we aim to provide some intuitions about how the choice of mechanism for combining character-level with word-level representations influences the quality of the final word representations, and the subsequent effect

### Relevance

Label: 

## Record 0020

Paper: Gating Mechanisms for Combining Character and Word-level Word Representations: An Empirical Study

### Question

> Which model architecture do they use to obtain representations?

### Passage

> table:wordlevelresults shows the quality of word representations in terms of the correlation between word similarity scores obtained by the proposed models and word similarity scores defined by humans.
> 
> First, we can see that for each task, character only models had significantly worse performance than every other model trained on the same dataset. The most likely explanation for this is that these models are the only ones that need to learn word representations from scratch, since they have no access to the global semantic knowledge encoded by the GloVe embeddings.
> 
> Further, bold results show the overall trend that vector gates outperformed the other methods regardless of training dataset. This implies that learning how to combine character and word-level representations at the dimension level produces word vector representations that capture a notion of word similarity and relatedness that is closer to that of humans.
> 
> Additionally, results from the MNLI row in general, and underlined results in particular, show that training on MultiNLI produces word representations better at capturing word similarity. This is probably due to MultiNLI data being richer than that of SNLI. Indeed, MultiNLI data was gathered from various sources (novels, reports, letters, and telephone conversations, among others), rather than the single image captions dataset from which SNLI was created.
> 
> Exceptions to the previous rule are models evaluated in MEN and RW. The former case can be explained by the MEN dataset containing only words that appear as image labels in the ESP-Game and MIRFLICKR-1M image datasets BIBREF24 , and therefore having data that is more closely distributed to SNLI than to MultiNLI.
> 
> More notably, in the RareWords dataset BIBREF25 , the word only, concat, and scalar gate methods performed equally, despite having been trained in different datasets ( INLINEFORM0 ), and the char only method performed significantly worse when trained in MultiNLI. The vector gate, however, performed significantly better than its counterpart trained in SNLI. These facts provide evidence that this method is capable of capturing linguistic phenomena that the other methods are unable to model.
> 
> table:word-similarity-dataset lists the word-similarity datasets and their corresponding reference. As mentioned in subsec:datasets, all the word-similarity datasets contain pairs of words annotated with similarity or relatedness scores, although this

### Relevance

Label: 

## Record 0021

Paper: TutorialVQA: Question Answering Dataset for Tutorial Videos

### Question

> What evaluation metrics were used in the experiment?

### Passage

> We downloaded 76 videos from a tutorial website about an image editing program . Each video is pre-processed to provide the transcripts and the time-stamp information for each sentence in the transcript. We then used Amazon Mechanical Turk to collect the question-answer pairs . One naive way of collecting the data is to prepare a question list and then, for each question, ask the workers to find the relevant parts in the video. However, this approach is not feasible and error-prone because the videos are typically long and finding a relevant part from a long video is difficult. Doing so might also cause us to miss questions which were relevant to the video segment. Instead, we took a reversed approach. First, for each video, we manually identified the sentence spans that can serve as answers. These candidates are of various granularity and may overlap. The segments are also complete in that they encompass the beginning and end of a task. In total, we identified 408 segments from the 76 videos. Second we asked AMT workers to provide question annotations for the videos.
> 
> Our AMT experiment consisted of two parts. In the first part, we presented the workers with the video content of a segment. For each segment, we asked workers to generate questions that can be answered by the presented segment. We did not limit the number of questions a worker can input to a corresponding segment and encouraged them to input a diverse set of questions which the span can answer. Along with the questions, the workers were also required to provide a justification as to why they made their questions. We manually checked this justification to filter out the questions with poor quality by removing those questions which were unrelated to the video. One initial challenge worth mentioning is that at first some workers input questions they had about the video and not questions which the video could answer. This was solved by providing them with an unrelated example. The second part of the question collection framework consisted of a paraphrasing task. In this task we presented workers with the questions generated by the first task and asked them to write the questions

### Relevance

Label: 

## Record 0022

Paper: TutorialVQA: Question Answering Dataset for Tutorial Videos

### Question

> What evaluation metrics were used in the experiment?

### Passage

> Table TABREF12 presents some extracted sample questions from our dataset. The first column corresponds to an AMT generated question, while the second column corresponds to the video ID where the segment can be found. As can be seen in the first two rows, multiple types of questions can be answered within the same video (but different segments). The last two rows display questions which belong to the same segment but correspond to different properties of the same entity, 'crop tool'. Here we observe different types of questions, such as "why", "how", "what", and "where", and can see why the answers may involve multiple steps. Some questions that the worked paraphrased were in the "yes/no" style, however our answer segments then provide an explanation to these questions.
> 
> Each answer segment was extracted from an image editing tutorial video that involved multiple steps and procedures to produce a final image, which can partially be seen in FIGREF1. The average number of sentences per video was approximately 52, with the maximum number of sentences contained in a video being 187. The sub-tasks in the tutorial include segments (and thus answers) on editing parts of images, instructions on using certain tools, possible actions that can be performed on an image, and identifying the locations of tools and features, with the shortest and longest segment having a span of 1 and 37 sentences respectively, demonstrating the heterogeneity of the answer spans.

### Relevance

Label: 

## Record 0023

Paper: TutorialVQA: Question Answering Dataset for Tutorial Videos

### Question

> What evaluation metrics were used in the experiment?

### Passage

> many answers already exist within the given video contents. Under this assumption, we formulate the problem as a localization task to specify the span of a video segment as the direct answer to a given video and a question, as illustrated in Figure FIGREF1.
> 
> The remainder of this paper is structured as follows. Section SECREF3 introduces TutorialVQA dataset as a case study of our proposed problem. The dataset includes about 6,000 triples, comprised of videos, questions, and answer spans manually collected from screencast tutorial videos with spoken narratives for a photo-editing software. Section SECREF4 presents the baseline models and their experiment details on the sentence-level prediction and video segment retrieval tasks on our dataset. Then, we discuss the experimental results in Section SECREF5 and conclude the paper in Section SECREF6.

### Relevance

Label: 

## Record 0024

Paper: TutorialVQA: Question Answering Dataset for Tutorial Videos

### Question

> What evaluation metrics were used in the experiment?

### Passage

> We also considered a simpler task by casting our problem as a retrieval task. Specifically, in addition to a plain transcript, we also provided the model with the segmentation information which was created during the data collection phrase (See Section. SECREF3). Note that each segments corresponds to a candidate answer. Then, the task is to pick the best segment for given a query. This task is easier than Baseline1's task in that the segmentation information is provided to the model. Unlike Baseline1, however, it is unable to return an answer span at various granularities. Baseline2 is based on the attentive LSTM BIBREF17, which has been developed for the InsuranceQA task. The right diagram in Fig. FIGREF15 illustrates the Baseline2 model.
> 
> Model. The two inputs, $s$ and $q$ represent the segment text and a question. The model first encodes the two inputs.
> 
> $h^s$ is then re-weighted using attention weights.
> 
> where $\odot $ denotes the element-wise multiplication operation. The final score is computed using a one-layer feed-forward network.
> 
> During training, the model requires negative samples. For each positive example, (question, ground-truth segment), all the other segments in the same transcript are used as negative samples. Cross entropy is used as an objective function.
> 
> Metrics. We used accuracy and MRR (Mean Reciprocal Ranking) as metrics. The accuracy is
> 
> We split the ground-truth dataset to train/dev/test into the ratio of 6/2/2. The resulting size is 3,718 (train), 1,238 (dev) and 1,239 qa pairs (test).

### Relevance

Label: 

## Record 0025

Paper: TutorialVQA: Question Answering Dataset for Tutorial Videos

### Question

> What evaluation metrics were used in the experiment?

### Passage

> Video is the fastest growing medium to create and deliver information today. Consequentially, videos have been increasingly used as main data sources in many question answering problems BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, BIBREF2, BIBREF5. These previous studies have mostly focused on factoid questions, each of which can be answered in a few words or phrases generated by understanding multimodal contents in a short video clip.
> 
> However, this problem definition of video question answering causes some practical limitations for the following reasons. First, factoid questions are just a small part of what people actually want to ask on video contents. Especially if a short video is given to users, most fragmentary facts within the scope of previous tasks can be easily perceived by themselves even before asking questions. Thus, video question answering is expected to provide answers to more complicated non-factoid questions beyond the simple facts. For example, those questions could be the ones asking about a how procedure as shown in Fig. FIGREF5, and the answers should contain all necessary steps to complete the task.
> 
> Accordingly, the answer format needs to also be improved towards more flexible ways than multiple choice BIBREF1, BIBREF2 or fill-in-the-blank questions BIBREF3, BIBREF4. Although open-ended video question answering BIBREF0, BIBREF2, BIBREF5 has been explored, it still aims to generate just a short word or phrase-level answer, which is not enough to cover various granularities of non-factoid question answering.
> 
> The other issue is that most videos with sufficient amount of information, which are likely to be asked, have much longer lengths than the video clips in the existing datasets. Therefore, the most relevant part of a whole video needs to be determined prior to each answer generation in practice. However, this localization task has been out of scope for previous studies.
> 
> In this work, we propose a new question answering problem for non-factoid questions on instructional videos. According to the nature of the media created for educational purposes, we assume that many answers already exist within the given video contents. Under this assumption, we formulate the problem as a localization task to specify the span of a video segment as the direct answer to a given video and a question, as

### Relevance

Label: 
