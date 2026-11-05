# Evidence Review

## Question: 30c6d34b878630736f819fd898319ac4e71ee50b

### Question ID and text

Question ID: `30c6d34b878630736f819fd898319ac4e71ee50b`; paper ID: `1912.10167`.

```text
Are any experiments performed to try this approach to word embeddings?
```

### Answers

#### Answer: 287a0cc03da31098bb23b2093eefc83e367ea757

```text
{"evidence": ["In the literature, two main types of datasets are used for machine translation: Word-aligned data and Sentence-aligned data. The first one is basically a dictionary between the two languages, where there is a direct relation between same words in different languages. The second one has the relation between corresponding sentences in the two languages. We decided to start with the sentence aligned corpus, since it was more interesting to infer dependency from contexts among words. For our experiment we decided to use the Europarl dataset, using the data from the WMT11 .The Europarl parallel corpus is extracted from the proceedings of the European Parliament. It includes versions in 21 European languages: Romanic (French, Italian, Spanish, Portuguese, Romanian), Germanic (English, Dutch, German, Danish, Swedish), Slavik (Bulgarian, Czech, Polish, Slovak, Slovene), Finni-Ugric (Finnish, Hungarian, Estonian), Baltic (Latvian, Lithuanian), and Greek. For this experience, we used the English-French parallel corpus, which contains 2,007,723 sentences and the English-Italian corpus, that contains 1,909,115 sentences."], "extractive_spans": [], "free_form_answer": "", "highlighted_evidence": ["For our experiment we decided to use the Europarl dataset, using the data from the WMT11 ."], "unanswerable": false, "yes_no": true}
```

Evidence location: `1912.10167:2:0`

```text
In the literature, two main types of datasets are used for machine translation: Word-aligned data and Sentence-aligned data. The first one is basically a dictionary between the two languages, where there is a direct relation between same words in different languages. The second one has the relation between corresponding sentences in the two languages. We decided to start with the sentence aligned corpus, since it was more interesting to infer dependency from contexts among words. For our experiment we decided to use the Europarl dataset, using the data from the WMT11 .The Europarl parallel corpus is extracted from the proceedings of the European Parliament. It includes versions in 21 European languages: Romanic (French, Italian, Spanish, Portuguese, Romanian), Germanic (English, Dutch, German, Danish, Swedish), Slavik (Bulgarian, Czech, Polish, Slovak, Slovene), Finni-Ugric (Finnish, Hungarian, Estonian), Baltic (Latvian, Lithuanian), and Greek. For this experience, we used the English-French parallel corpus, which contains 2,007,723 sentences and the English-Italian corpus, that contains 1,909,115 sentences.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-333c662b6f95d1df72d84be6e1a77c1e5f076e9192ceee9104c291b6afd71649

Passage ID: `qasper-passage-v1-333c662b6f95d1df72d84be6e1a77c1e5f076e9192ceee9104c291b6afd71649`; retrieval score: 4.6892894331850545.

Word count: 103.

```text
In recent years, various models for learning cross-lingual representations have been proposed. Two main broad categories with some related papers are identified here:

Monolingual mapping: In this approach, models are trained using word embeddings from a monolingual corpora. Then, an objective function is used to minimize a linear mapping that enable them to map unknown words from the source language to the target language.

Pseudo-cross-lingual: In this case we create a pseudo-cross-lingual corpus by mixing contexts of different languages. We then train an off-the-shelf word embedding model on the created corpus. Ideally the cross-lingual contexts allow the learned representations to capture cross-lingual relations.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-941a50f3dbdc4621047c643e6393b5956c6a6dfe013b0f24b052ab065e1401b4

Passage ID: `qasper-passage-v1-941a50f3dbdc4621047c643e6393b5956c6a6dfe013b0f24b052ab065e1401b4`; retrieval score: 4.657799416227245.

Word count: 243.

```text
Methods for machine translations have been studied for years, and at the same time algorithms to generate word embeddings are becoming more and more accurate. Still, there is a lot of research aiming at unifying word embeddings across multiple languages. In this experience we try a technique for machine translation that relates word embeddings between two different languages. Based on the literature we found that it is possible to infer missing dictionary entries using distributed representations of words and phrases. One way of doing it is to create a linear mapping between the two vector spaces of two different languages. In order to achieve this, we first built two dictionaries of the two different languages. Next, we learned a function that projects the first vector space to the second one. In this way, we are able to translate every word belonging to the first language into the second one. Once we obtain the translated word embedding, we output the most similar word vector as the translation. The word embeddings were learnt using the Skip Gram method proposed by (Mikolov et al., 2013a). An example of how the method would work is reported in figure 1 and figure 2. After creating the word embeddings from the two dictionaries, we plotted the numbers in the two graphs using PCA. Figure 3 reports the results after creating a linear mapping between the embeddings from the two languages. You can see how similar words are closer together.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-b67e692ca63be13060e4a8838f81df3b2f2183def14199d6b6d93730dea51f71

Passage ID: `qasper-passage-v1-b67e692ca63be13060e4a8838f81df3b2f2183def14199d6b6d93730dea51f71`; retrieval score: 4.631593745973947.

Word count: 131.

```text
It was recently shown that the distributed representations of words capture surprisingly many linguistic regularities, and that there are many types of similarities among words that can be expressed as linear translations (Mikolov et al., 2013c). In the Skip-gram model, the training objective is to learn word vector representations that are good at predicting its context in the same sentence (Mikolov et al., 2013a). The objective function that skip gram tries to minimize is the following:

Where N represents the total number of words in a sentence, P the probability of a word at the position i+j to belong to the sentence, with respect to the word i. Ideally, by using this approach we will be able to provide non-trivial translations that will be related to the context of a word.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-22f6ec089778b38e18aed6f642300ebbf81d9ca6b3362b17dbfb5a0432435fd1

Passage ID: `qasper-passage-v1-22f6ec089778b38e18aed6f642300ebbf81d9ca6b3362b17dbfb5a0432435fd1`; retrieval score: 3.0042659643648615.

Word count: 55.

```text
This represents the linear function that maps word embeddings from one language to another. Given a word x in one language, and the respective word in the other language z, the following equation reports the objective function we want to minimize:

Were W represents the final matrix that will contain the values for the mapping.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-9b0dd931e88585d051ae57c878f7d2c2e07fdcf53fa70d0a466142d3b5ed181a

Passage ID: `qasper-passage-v1-9b0dd931e88585d051ae57c878f7d2c2e07fdcf53fa70d0a466142d3b5ed181a`; retrieval score: 2.9612255930594737.

Word count: 138.

```text
In order to minimize the loss function we decided to setup a neural network and reduce the objective by using Stochastic Gradient Descent. Figure 4 represents the architecture of our base model. We repeated the same process both for objective functions expressed in equation DISPLAY_FORM8 and DISPLAY_FORM12. We started by getting an English word from the English corpus and we got the corresponding target word by using Google Translate. If this word was contained in the target corpus, this pair of words was used to train the model; otherwise, it was ignored. We then get the two embeddings and get the result by multiplying the first one by the matrix W and then substracting the second embedding. For this experiment, we used embeddings with a dimension of 100. For this reason W is a matrix of size 100*100.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 670.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "287a0cc03da31098bb23b2093eefc83e367ea757": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1912.10167:2:0": [
        [
          0,
          1126
        ]
      ]
    }
  }
}
```

## Question: 0ab3df10f0b7203e859e9b62ffa7d6d79ffbbe50

### Question ID and text

Question ID: `0ab3df10f0b7203e859e9b62ffa7d6d79ffbbe50`; paper ID: `1911.07555`.

```text
What evaluation metric is used?
```

### Answers

#### Answer: 7a75e1c45c5b7e54f8d3bf675b477ea9c5948d5a

```text
{"evidence": ["The average classification accuracy results are summarised in Table TABREF9. The accuracies reported are for classifying a piece of text by its specific language label. Classifying text only by language group or family is a much easier task as reported in BIBREF8."], "extractive_spans": ["average classification accuracy"], "free_form_answer": "", "highlighted_evidence": ["The average classification accuracy results are summarised in Table TABREF9."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1911.07555:3:0`

```text
The average classification accuracy results are summarised in Table TABREF9. The accuracies reported are for classifying a piece of text by its specific language label. Classifying text only by language group or family is a much easier task as reported in BIBREF8.
```

#### Answer: fb9f47f34736e65e1bc8fb3a4b515f02fe2ee9da

```text
{"evidence": ["The average classification accuracy results are summarised in Table TABREF9. The accuracies reported are for classifying a piece of text by its specific language label. Classifying text only by language group or family is a much easier task as reported in BIBREF8.", "The execution performance of some of the LID implementations are shown in Table TABREF10. Results were generated on an early 2015 13-inch Retina MacBook Pro with a 2.9 GHz CPU (Turbo Boosted to 3.4 GHz) and 8GB RAM. The C++ implementation in BIBREF17 is the fastest. The implementation in BIBREF8 makes use of un-hashed feature representations which causes it to be slower than the proposed sklearn implementation. The execution performance of BIBREF23 might improve by a factor of five to ten when executed on a GPU."], "extractive_spans": ["average classification accuracy", "execution performance"], "free_form_answer": "", "highlighted_evidence": ["The average classification accuracy results are summarised in Table TABREF9. The accuracies reported are for classifying a piece of text by its specific language label.", "The execution performance of some of the LID implementations are shown in Table TABREF10."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1911.07555:3:0`

```text
The average classification accuracy results are summarised in Table TABREF9. The accuracies reported are for classifying a piece of text by its specific language label. Classifying text only by language group or family is a much easier task as reported in BIBREF8.
```

Evidence location: `1911.07555:3:4`

```text
The execution performance of some of the LID implementations are shown in Table TABREF10. Results were generated on an early 2015 13-inch Retina MacBook Pro with a 2.9 GHz CPU (Turbo Boosted to 3.4 GHz) and 8GB RAM. The C++ implementation in BIBREF17 is the fastest. The implementation in BIBREF8 makes use of un-hashed feature representations which causes it to be slower than the proposed sklearn implementation. The execution performance of BIBREF23 might improve by a factor of five to ten when executed on a GPU.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-7dcddc58931824f280be5a6f0dbac50c849a410898af50f13135bfe8a9bd2160

Passage ID: `qasper-passage-v1-7dcddc58931824f280be5a6f0dbac50c849a410898af50f13135bfe8a9bd2160`; retrieval score: 1.8487008411245678.

Word count: 400.

```text
The focus of this section is on recently published datasets and LID research applicable to the South African context. An in depth survey of algorithms, features, datasets, shared tasks and evaluation methods may be found in BIBREF0.

The datasets for the DSL 2015 & DSL 2017 shared tasks BIBREF1 are often used in LID benchmarks and also available on Kaggle . The DSL datasets, like other LID datasets, consists of text sentences labelled by language. The 2017 dataset, for example, contains 14 languages over 6 language groups with 18000 training samples and 1000 testing samples per language.

The recently published JW300 parallel corpus BIBREF2 covers over 300 languages with around 100 thousand parallel sentences per language pair on average. In South Africa, a multilingual corpus of academic texts produced by university students with different mother tongues is being developed BIBREF3. The WiLI-2018 benchmark dataset BIBREF4 for monolingual written natural language identification includes around 1000 paragraphs of 235 languages. A possibly useful link can also be made BIBREF5 between Native Language Identification (NLI) (determining the native language of the author of a text) and Language Variety Identification (LVI) (classification of different varieties of a single language) which opens up more datasets. The Leipzig Corpora Collection BIBREF6, the Universal Declaration of Human Rights and Tatoeba are also often used sources of data.

The NCHLT text corpora BIBREF7 is likely a good starting point for a shared LID task dataset for the South African languages BIBREF8. The NCHLT text corpora contains enough data to have 3500 training samples and 600 testing samples of 300+ character sentences per language. Researchers have recently started applying existing algorithms for tasks like neural machine translation in earnest to such South African language datasets BIBREF9.

Existing NLP datasets, models and services BIBREF10 are available for South African languages. These include an LID algorithm BIBREF11 that uses a character level n-gram language model. Multiple papers have shown that 'shallow' naive Bayes classifiers BIBREF12, BIBREF8, BIBREF13, BIBREF14, SVMs BIBREF15 and similar models work very well for doing LID. The DSL 2017 paper BIBREF1, for example, gives an overview of the solutions of all of the teams that competed on the shared task and the winning approach BIBREF16 used an SVM with character n-gram, parts of speech tag features and some other engineered features. The winning approach for DSL 2015 used an ensemble naive Bayes classifier. The fasttext classifier BIBREF17 is
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-d68d861112e52f32ce396472545d9751a4d48da27be537f338f85ffd3783c725

Passage ID: `qasper-passage-v1-d68d861112e52f32ce396472545d9751a4d48da27be537f338f85ffd3783c725`; retrieval score: 0.8218285441218943.

Word count: 399.

```text
The proposed LID algorithm builds on the work in BIBREF8 and BIBREF26. We apply a naive Bayesian classifier with character (2, 4 & 6)-grams, word unigram and word bigram features with a hierarchical lexicon based classifier.

The naive Bayesian classifier is trained to predict the specific language label of a piece of text, but used to first classify text as belonging to either the Nguni family, the Sotho family, English, Afrikaans, Xitsonga or Tshivenda. The scikit-learn multinomial naive Bayes classifier is used for the implementation with an alpha smoothing value of 0.01 and hashed text features.

The lexicon based classifier is then used to predict the specific language within a language group. For the South African languages this is done for the Nguni and Sotho groups. If the lexicon prediction of the specific language has high confidence then its result is used as the final label else the naive Bayesian classifier's specific language prediction is used as the final result. The lexicon is built over all the data and therefore includes the vocabulary from both the training and testing sets.

The lexicon based classifier is designed to trade higher precision for lower recall. The proposed implementation is considered confident if the number of words from the winning language is at least one more than the number of words considered to be from the language scored in second place.

The stacked classifier is tested against three public LID implementations BIBREF17, BIBREF23, BIBREF8. The LID implementation described in BIBREF17 is available on GitHub and is trained and tested according to a post on the fasttext blog. Character (5-6)-gram features with 16 dimensional vectors worked the best. The implementation discussed in BIBREF23 is available from https://github.com/tomkocmi/LanideNN. Following the instructions for an OSX pip install of an old r0.8 release of TensorFlow, the LanideNN code could be executed in Python 3.7.4. Settings were left at their defaults and a learning rate of 0.001 was used followed by a refinement with learning rate of 0.0001. Only one code modification was applied to return the results from a method that previously just printed to screen. The LID algorithm described in BIBREF8 is also available on GitHub.

The stacked classifier is also tested against the results reported for four other algorithms BIBREF16, BIBREF26, BIBREF24, BIBREF15. All the comparisons are done using the NCHLT BIBREF7, DSL 2015 BIBREF19 and DSL 2017 BIBREF1 datasets discussed in Section SECREF2.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-a8a4a6f744e8f31a4ad72dad9f4789c8b4f72b6f7f7b9585693bef452c0fef07

Passage ID: `qasper-passage-v1-a8a4a6f744e8f31a4ad72dad9f4789c8b4f72b6f7f7b9585693bef452c0fef07`; retrieval score: 0.739886453956621.

Word count: 315.

```text
shared task and the winning approach BIBREF16 used an SVM with character n-gram, parts of speech tag features and some other engineered features. The winning approach for DSL 2015 used an ensemble naive Bayes classifier. The fasttext classifier BIBREF17 is perhaps one of the best known efficient 'shallow' text classifiers that have been used for LID .

Multiple papers have proposed hierarchical stacked classifiers (including lexicons) that would for example first classify a piece of text by language group and then by exact language BIBREF18, BIBREF19, BIBREF8, BIBREF0. Some work has also been done on classifying surnames between Tshivenda, Xitsonga and Sepedi BIBREF20. Additionally, data augmentation BIBREF21 and adversarial training BIBREF22 approaches are potentially very useful to reduce the requirement for data.

Researchers have investigated deeper LID models like bidirectional recurrent neural networks BIBREF23 or ensembles of recurrent neural networks BIBREF24. The latter is reported to achieve 95.12% in the DSL 2015 shared task. In these models text features can include character and word n-grams as well as informative character and word-level features learnt BIBREF25 from the training data. The neural methods seem to work well in tasks where more training data is available.

In summary, LID of short texts, informal styles and similar languages remains a difficult problem which is actively being researched. Increased confusion can in general be expected between shorter pieces of text and languages that are more closely related. Shallow methods still seem to work well compared to deeper models for LID. Other remaining research opportunities seem to be data harvesting, building standardised datasets and creating shared tasks for South Africa and Africa. Support for language codes that include more languages seems to be growing and discoverability of research is improving with more survey papers coming out. Paywalls also seem to no longer be a problem; the references used in this paper was either openly published or available as preprint papers.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-ed391b907c243a0bfd3b5be8e8dbf852c1fdac1313e84de5ce0d691c026042c0

Passage ID: `qasper-passage-v1-ed391b907c243a0bfd3b5be8e8dbf852c1fdac1313e84de5ce0d691c026042c0`; retrieval score: 0.6327157436865913.

Word count: 190.

```text
LID of short texts, informal styles and similar languages remains a difficult problem which is actively being researched. The proposed algorithm was evaluated on three existing datasets and compared to the implementations of three public LID implementations as well as to reported results of four other algorithms. It performed well relative to the other methods beating their results. However, the performance is dependent on the support of the lexicon.

We would like to investigate the value of a lexicon in a production system and how to possibly maintain it using self-supervised learning. We are investigating the application of deeper language models some of which have been used in more recent DSL shared tasks. We would also like to investigate data augmentation strategies to reduce the amount of training data that is required.

Further research opportunities include data harvesting, building standardised datasets and shared tasks for South Africa as well as the rest of Africa. In general, the support for language codes that include more languages seems to be growing, discoverability of research is improving and paywalls seem to no longer be a big problem in getting access to published research.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-8f199b5e9b7da0bba42daa7e4037ce0ca8a8ae9578d951ba81362af56b14d301

Passage ID: `qasper-passage-v1-8f199b5e9b7da0bba42daa7e4037ce0ca8a8ae9578d951ba81362af56b14d301`; retrieval score: 0.5962916226170116.

Word count: 311.

```text
Accurate language identification (LID) is the first step in many natural language processing and machine comprehension pipelines. If the language of a piece of text is known then the appropriate downstream models like parts of speech taggers and language models can be applied as required.

LID is further also an important step in harvesting scarce language resources. Harvested data can be used to bootstrap more accurate LID models and in doing so continually improve the quality of the harvested data. Availability of data is still one of the big roadblocks for applying data driven approaches like supervised machine learning in developing countries.

Having 11 official languages of South Africa has lead to initiatives (discussed in the next section) that have had positive effect on the availability of language resources for research. However, many of the South African languages are still under resourced from the point of view of building data driven models for machine comprehension and process automation.

Table TABREF2 shows the percentages of first language speakers for each of the official languages of South Africa. These are four conjunctively written Nguni languages (zul, xho, nbl, ssw), Afrikaans (afr) and English (eng), three disjunctively written Sotho languages (nso, sot, tsn), as well as tshiVenda (ven) and Xitsonga (tso). The Nguni languages are similar to each other and harder to distinguish. The same is true of the Sotho languages.

This paper presents a hierarchical naive Bayesian and lexicon based classifier for LID of short pieces of text of 15-20 characters long. The algorithm is evaluated against recent approaches using existing test sets from previous works on South African languages as well as the Discriminating between Similar Languages (DSL) 2015 and 2017 shared tasks.

Section SECREF2 reviews existing works on the topic and summarises the remaining research problems. Section SECREF3 of the paper discusses the proposed algorithm and Section SECREF4 presents comparative results.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1615.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "7a75e1c45c5b7e54f8d3bf675b477ea9c5948d5a": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1911.07555:3:0": [
        [
          0,
          264
        ]
      ]
    }
  },
  "fb9f47f34736e65e1bc8fb3a4b515f02fe2ee9da": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1911.07555:3:0": [
        [
          0,
          264
        ]
      ],
      "1911.07555:3:4": [
        [
          0,
          517
        ]
      ]
    }
  }
}
```

## Question: 729694a9fe1e05d329b7a4078a596fe606bc5a95

### Question ID and text

Question ID: `729694a9fe1e05d329b7a4078a596fe606bc5a95`; paper ID: `1904.10503`.

```text
What results do they achieve using their proposed approach?
```

### Answers

#### Answer: 4cbb4c87c1ba12f24c101941969835ae60d88c5b

```text
{"evidence": ["The results for each class type are shown in Table TABREF19 , with some specific examples shown in Figure FIGREF18 . For the Wiki(gold) we quote the micro-averaged F-1 scores for the entire top level entity category. The total F-1 score on the OntoNotes dataset is 88%, and the total F-1 cross-validation score on the 112 class Wiki(gold) dataset is 53%. It is worth noting that one could improve Wiki(gold) results by training directly using this dataset. However, the aim is not to tune our model specifically on this class hierarchy. We instead aim to present a framework which can be modified easily to any domain hierarchy and has acceptable out-of-the-box performances to any fine-grained dataset. The results in Table TABREF19 (OntoNotes) only show the main 7 categories in OntoNotes which map to Wiki(gold) for clarity. The other categories (date, time, norp, language, ordinal, cardinal, quantity, percent, money, law) have F-1 scores between 80-90%, with the exception of time (65%)"], "extractive_spans": [], "free_form_answer": "F-1 score on the OntoNotes is 88%, and it is 53% on Wiki (gold).", "highlighted_evidence": ["The total F-1 score on the OntoNotes dataset is 88%, and the total F-1 cross-validation score on the 112 class Wiki(gold) dataset is 53%. "], "unanswerable": false, "yes_no": null}
```

Evidence location: `1904.10503:6:0`

```text
The results for each class type are shown in Table TABREF19 , with some specific examples shown in Figure FIGREF18 . For the Wiki(gold) we quote the micro-averaged F-1 scores for the entire top level entity category. The total F-1 score on the OntoNotes dataset is 88%, and the total F-1 cross-validation score on the 112 class Wiki(gold) dataset is 53%. It is worth noting that one could improve Wiki(gold) results by training directly using this dataset. However, the aim is not to tune our model specifically on this class hierarchy. We instead aim to present a framework which can be modified easily to any domain hierarchy and has acceptable out-of-the-box performances to any fine-grained dataset. The results in Table TABREF19 (OntoNotes) only show the main 7 categories in OntoNotes which map to Wiki(gold) for clarity. The other categories (date, time, norp, language, ordinal, cardinal, quantity, percent, money, law) have F-1 scores between 80-90%, with the exception of time (65%)
```

#### Answer: f4eb7f67fb41888ab6b1fa018211c89994b6e8fe

```text
{"evidence": ["The results for each class type are shown in Table TABREF19 , with some specific examples shown in Figure FIGREF18 . For the Wiki(gold) we quote the micro-averaged F-1 scores for the entire top level entity category. The total F-1 score on the OntoNotes dataset is 88%, and the total F-1 cross-validation score on the 112 class Wiki(gold) dataset is 53%. It is worth noting that one could improve Wiki(gold) results by training directly using this dataset. However, the aim is not to tune our model specifically on this class hierarchy. We instead aim to present a framework which can be modified easily to any domain hierarchy and has acceptable out-of-the-box performances to any fine-grained dataset. The results in Table TABREF19 (OntoNotes) only show the main 7 categories in OntoNotes which map to Wiki(gold) for clarity. The other categories (date, time, norp, language, ordinal, cardinal, quantity, percent, money, law) have F-1 scores between 80-90%, with the exception of time (65%)"], "extractive_spans": [" total F-1 score on the OntoNotes dataset is 88%", "total F-1 cross-validation score on the 112 class Wiki(gold) dataset is 53%"], "free_form_answer": "", "highlighted_evidence": ["The total F-1 score on the OntoNotes dataset is 88%, and the total F-1 cross-validation score on the 112 class Wiki(gold) dataset is 53%."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1904.10503:6:0`

```text
The results for each class type are shown in Table TABREF19 , with some specific examples shown in Figure FIGREF18 . For the Wiki(gold) we quote the micro-averaged F-1 scores for the entire top level entity category. The total F-1 score on the OntoNotes dataset is 88%, and the total F-1 cross-validation score on the 112 class Wiki(gold) dataset is 53%. It is worth noting that one could improve Wiki(gold) results by training directly using this dataset. However, the aim is not to tune our model specifically on this class hierarchy. We instead aim to present a framework which can be modified easily to any domain hierarchy and has acceptable out-of-the-box performances to any fine-grained dataset. The results in Table TABREF19 (OntoNotes) only show the main 7 categories in OntoNotes which map to Wiki(gold) for clarity. The other categories (date, time, norp, language, ordinal, cardinal, quantity, percent, money, law) have F-1 scores between 80-90%, with the exception of time (65%)
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-3df43c0a9464820e5c03e48b35ac3eaf19c3ba41243f5d188338740af330fa85

Passage ID: `qasper-passage-v1-3df43c0a9464820e5c03e48b35ac3eaf19c3ba41243f5d188338740af330fa85`; retrieval score: 2.608056865315901.

Word count: 160.

```text
The results for each class type are shown in Table TABREF19 , with some specific examples shown in Figure FIGREF18 . For the Wiki(gold) we quote the micro-averaged F-1 scores for the entire top level entity category. The total F-1 score on the OntoNotes dataset is 88%, and the total F-1 cross-validation score on the 112 class Wiki(gold) dataset is 53%. It is worth noting that one could improve Wiki(gold) results by training directly using this dataset. However, the aim is not to tune our model specifically on this class hierarchy. We instead aim to present a framework which can be modified easily to any domain hierarchy and has acceptable out-of-the-box performances to any fine-grained dataset. The results in Table TABREF19 (OntoNotes) only show the main 7 categories in OntoNotes which map to Wiki(gold) for clarity. The other categories (date, time, norp, language, ordinal, cardinal, quantity, percent, money, law) have F-1 scores between 80-90%, with the exception of time (65%)
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.10503:6:0` | full | 0:992 |

#### Rank 2: qasper-passage-v1-52a6debb73319fb3f3bdf844569c36a52fe5ce13a7a6009449a00da68ab10d52

Passage ID: `qasper-passage-v1-52a6debb73319fb3f3bdf844569c36a52fe5ce13a7a6009449a00da68ab10d52`; retrieval score: 2.0752326915328436.

Word count: 400.

```text
Entity linking (EL) BIBREF24 , also known as named entity disambiguation or normalization, is the task to determine the identity of entities mentioned in a piece of text with reference to a knowledge base. There are a number of knowledge bases that provide a background repository for entity classification of this type. For this study, we use Wikidata, which can be seen diagrammatically in Figure FIGREF12 . Systems such as DeepType BIBREF25 integrate symbolic information into the reasoning process of a neural network with a type system and show state-of-the-art performances for EL. They do not, however, quote results on Wiki(gold) so a direct comparison is difficult.

While these knowledge bases provide semantically rich and fine-granular classes and relationship types, the task of entity classification often requires associating coarse-grained classes with discovered surface forms of entities. Most existing studies consider NER and entity linking as two separate tasks, whereas we try to combine the two. It has been shown that one can significantly increase the semantic information carried by a NER system when we successfully linking entities from a deep learning method to the related entities from a knowledge base BIBREF26 , BIBREF27 .

Redirection: For the Wikidata linking element, we recognize that the lookup will be constrained by the most common lookup name for each entity. Consider the utterance (referring to the NBA basketball player) from Figure FIGREF12 “Michael Jeffrey Jordan in San Jose” as an example. The lookup for this entity in Wikidata is “Michael Jordan” and consequently will not be picked up if we were to use an exact string match. A simple method to circumvent such a problem is the usage of a redirection list. Such a list is provided on an entity by entity basis in the “Also known as” section in Wikidata. Using this redirection list, when we do not find an exact string match improves the recall of our model by 5-10%. Moreover, with the example of Michael Jordan (person), using our current framework, we will always refer to the retired basketball player (Q41421). We will never, for instance, pick up Michael Jordan (Q27069141) the American football cornerback. Or in fact any other Michael Jordan, famous or otherwise. One possible method to overcome this is to add a disambiguation layer, which seeks to use context from earlier parts of the text. This is, however, work for future improvement and we only consider the
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-36170684349dfff72c22959fc115de2c207d37bf9018db380b698f4e2ff2e739

Passage ID: `qasper-passage-v1-36170684349dfff72c22959fc115de2c207d37bf9018db380b698f4e2ff2e739`; retrieval score: 1.6598492967469949.

Word count: 400.

```text
Named entity recognition (NER) BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 is the process by which we identify text spans which mention named entities, and to classify them into predefined categories such as person, location, organization etc. NER serves as the basis for a variety of natural language processing (NLP) applications such as relation extraction BIBREF4 , machine translation BIBREF5 , question answering BIBREF6 and knowledge base construction BIBREF7 . Although early NER systems have been successful in producing adequate recognition accuracy, they often require significant human effort in carefully designing rules or features.

In recent years, deep learning methods been employed in NER systems, yielding state-of-the-art performance. However, the number of types detected are still not sufficient for certain domain-specific applications. For relation extraction, identifying fine-grained types has been shown to significantly increase the performance of the extractor BIBREF8 , BIBREF9 since this helps in filtering out candidate relation types which do not follow this type constraint. Furthermore, for question answering fine-grained Named Entity Recognition (FgNER) can provide additional information helping to match questions to its potential answers thus improving performance BIBREF10 . For example, Li and Roth BIBREF11 rank questions based on their expected answer types (i.e. will the answer be food, vehicle or disease).

Typically, FgNER systems use over a hundred labels, arranged in a hierarchical structure. We find that available training data for FgNER typically contain noisy labels, and creating manually annotated training data for FgNER is a time-consuming process. Furthermore, human annotators will have to assign a subset of correct labels from hundreds of possible labels making this a somewhat arduous task. Currently, FgNER systems use distant supervision BIBREF12 to automatically generate training data. Distant supervision is a technique which maps each entity in the corpus to knowledge bases such as Freebase BIBREF13 , DBpedia BIBREF14 , YAGO BIBREF15 and helps with the generation of labeled data. This method will assign the same set of labels to all mentions of a particular entity in the corpus. For example, “Barack Obama” is a person, politician, lawyer, and author. If a knowledge base has these four matching labels, the distant supervision technique will assign all of them to every mention of “Barack Obama”. Therefore, the training data will also fail to distinguish between mentions of “Barack Obama” in all subsequent utterances.

Ling et al. ling2012fine proposed the first system for FgNER, where they used 112 overlapping labels
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-741d566e93b6190957baf7779ad53727ffbf7ea5b56f23fecfb471c1c0a2f93d

Passage ID: `qasper-passage-v1-741d566e93b6190957baf7779ad53727ffbf7ea5b56f23fecfb471c1c0a2f93d`; retrieval score: 1.4715526983934124.

Word count: 271.

```text
NER involves identifying both entity boundaries and entity types. With “exact-match evaluation”, a named entity is considered correctly recognized only if both the boundaries and type match the ground truth BIBREF8 , BIBREF17 , BIBREF18 . Precision, Recall, and F-1 scores are computed on the number of true positives (TP), false positives (FP), and false negatives (FN). Their formal definitions are as follows:

True Positive (TP): entities that are recognized by NER and match the ground truth.

False Positive (FP): entities that are recognized by NER but do not match the ground truth.

False Negative (FN): entities annotated in the ground which that are not recognized by NER.

Precision measures the ability of a NER system to present only correct entities, and Recall measures the ability of a NER system to recognize all entities in a corpus. DISPLAYFORM0

The F-1 score is the harmonic mean of precision and recall, and the balanced F-1 score is the variant which is most commonly used. This is defined as: DISPLAYFORM0

Since most NER systems involve multiple entity types, it is often required to assess the performance across all entity classes. Two measures are commonly used for this purpose: the macro-averaged F-1 score and the micro-averaged F-1 score. The macro-averaged F-1 score computes the F-1 score independently for each entity type, then takes the average (hence treating all entity types equally). The micro-averaged F-1 score aggregates the contributions of entities from all classes to compute the average (treating all entities equally). We use the micro-averaged F-1 in our study since this accounts for label imbalances in the evaluation data and therefore a more meaningful statistic.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-7e1745b82627f8da7f0c648db547c9618f158eed43f7734643d6a8a8101349b5

Passage ID: `qasper-passage-v1-7e1745b82627f8da7f0c648db547c9618f158eed43f7734643d6a8a8101349b5`; retrieval score: 0.8604191484079297.

Word count: 162.

```text
We evaluate our model on two publicly available datasets. The statistics for both are shown in Table TABREF3 . The details of these datasets are as follows:

OntoNotes: OntoNotes 5.0 BIBREF16 includes texts from five different text genres: broadcast conversation (200k), broadcast news (200k), magazine (120k), newswire (625k), and web data (300k). This dataset is annotated with 18 categories.

Wiki(gold): The training data consists of Wikipedia sentences and was automatically generated using a distant supervision method, mapping hyperlinks in Wikipedia articles to Freebase, which we do not use in this study. The test data, mainly consisting of sentences from news reports, was manually annotated as described in BIBREF8 . The class hierarchy is shown in Figure FIGREF2 . This dataset is annotated with 7 main categories (bold text in Figure FIGREF2 ), which maps directly to OntoNotes. The miscellaneous category in Figure FIGREF2 does not have direct mappings, so future work may include redefining these categories so the mappings are more meaningful.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1393.

Fully covered answer annotations: 4cbb4c87c1ba12f24c101941969835ae60d88c5b, f4eb7f67fb41888ab6b1fa018211c89994b6e8fe.

Missing evidence by answer annotation:

```text
{
  "4cbb4c87c1ba12f24c101941969835ae60d88c5b": {
    "unresolved_evidence": [],
    "paragraphs": {}
  },
  "f4eb7f67fb41888ab6b1fa018211c89994b6e8fe": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: 65ad17f614b7345f0077424c04c94971c831585b

### Question ID and text

Question ID: `65ad17f614b7345f0077424c04c94971c831585b`; paper ID: `1904.05584`.

```text
Which model architecture do they use to obtain representations?
```

### Answers

#### Answer: ba4bf35bc0b271ac2b86145e2af2f4c6909a14eb

```text
{"evidence": ["To enable sentence-level classification we need to obtain a sentence representation from the word vectors INLINEFORM0 . We achieved this by using a BiLSTM with max pooling, which was shown to be a good universal sentence encoding mechanism BIBREF13 ."], "extractive_spans": ["BiLSTM with max pooling"], "free_form_answer": "", "highlighted_evidence": ["To enable sentence-level classification we need to obtain a sentence representation from the word vectors INLINEFORM0 . We achieved this by using a BiLSTM with max pooling, which was shown to be a good universal sentence encoding mechanism BIBREF13 ."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1904.05584:4:0`

```text
To enable sentence-level classification we need to obtain a sentence representation from the word vectors INLINEFORM0 . We achieved this by using a BiLSTM with max pooling, which was shown to be a good universal sentence encoding mechanism BIBREF13 .
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-60e48bdde3f630296defd75a9e85db71fb882e5824c0babd09d084f73dbe8ba2

Passage ID: `qasper-passage-v1-60e48bdde3f630296defd75a9e85db71fb882e5824c0babd09d084f73dbe8ba2`; retrieval score: 6.976837906881087.

Word count: 210.

```text
To the best of our knowledge, there are only two recent works that specifically study how to combine word and subword-level vector representations.

BIBREF11 propose to use a trainable scalar gating mechanism capable of learning a weighting scheme for combining character-level and word-level representations. They compared their proposed method to manually weighting both levels; using characters only; words only; or their concatenation. They found that in some datasets a specific manual weighting scheme performed better, while in others the learned scalar gate did.

BIBREF12 further expand the gating concept by making the mechanism work at a finer-grained level, learning how to weight each vector's dimensions independently, conditioned on external word-level features such as part-of-speech and named-entity tags. Similarly, they compared their proposed mechanism to using words only, characters only, and a concatenation of both, with and without external features. They found that their vector gate performed better than the other methods in all the reported tasks, and beat the state of the art in two reading comprehension tasks.

Both works showed that the gating mechanisms assigned greater importance to character-level representations in rare words, and to word-level representations in common ones, reaffirming the previous findings that subword structures in general, and characters in particular, are beneficial for modeling uncommon words.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-a2ceaff5a9adf753e846fe3da6ecab9f24dbde70d7e92ff9ae2b0b1cb15f87ff

Passage ID: `qasper-passage-v1-a2ceaff5a9adf753e846fe3da6ecab9f24dbde70d7e92ff9ae2b0b1cb15f87ff`; retrieval score: 5.654154720909253.

Word count: 263.

```text
The problem of representing sentences as fixed-length vectors has been widely studied.

BIBREF32 suggested a self-adaptive hierarchical model that gradually composes words into intermediate phrase representations, and adaptively selects specific hierarchical levels for specific tasks. BIBREF33 proposed an encoder-decoder model trained by attempting to reconstruct the surrounding sentences of an encoded passage, in a fashion similar to Skip-gram BIBREF34 . BIBREF35 overcame the previous model's need for ordered training sentences by using autoencoders for creating the sentence representations. BIBREF36 implemented a model simpler and faster to train than the previous two, while having competitive performance. Similar to BIBREF33 , BIBREF37 suggested predicting future sentences with a hierarchical CNN-LSTM encoder.

BIBREF13 trained several sentence encoding architectures on a combination of the SNLI and MultiNLI datasets, and showed that a BiLSTM with max-pooling was the best at producing highly transferable sentence representations. More recently, BIBREF18 empirically showed that sentence representations created in a multi-task setting BIBREF38 , performed increasingly better the more tasks they were trained in. BIBREF39 proposed using an autoencoder that relies on multi-head self-attention over the concatenation of the max and mean pooled encoder outputs for producing sentence representations. Finally, BIBREF40 show that modern sentence embedding methods are not vastly superior to random methods.

The works mentioned so far usually evaluate the quality of the produced sentence representations in sentence-level downstream tasks. Common benchmarks grouping these kind of tasks include SentEval BIBREF23 , and GLUE BIBREF41 . Another trend, however, is to probe sentence representations to understand what linguistic phenomena they encode BIBREF42 , BIBREF43 , BIBREF44 , BIBREF45 , BIBREF46 .
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-05a4f5377d00db8d1f0016c97007e3033ae41d02d63a1f1a233881af2c92c545

Passage ID: `qasper-passage-v1-05a4f5377d00db8d1f0016c97007e3033ae41d02d63a1f1a233881af2c92c545`; retrieval score: 5.094262837069308.

Word count: 130.

```text
To enable sentence-level classification we need to obtain a sentence representation from the word vectors INLINEFORM0 . We achieved this by using a BiLSTM with max pooling, which was shown to be a good universal sentence encoding mechanism BIBREF13 .

Let INLINEFORM0 , be an input sentence and INLINEFORM1 its matrix representation, where each INLINEFORM2 was obtained by one of the methods described in subsec:methods. INLINEFORM3 is the context-enriched matrix representation of INLINEFORM4 obtained by feeding INLINEFORM5 to a BiLSTM of output dimension INLINEFORM6 . Lastly, INLINEFORM11 is the final sentence representation of INLINEFORM12 obtained by max-pooling INLINEFORM13 along the sequence dimension.

Finally, we initialized the word representations INLINEFORM0 using GloVe embeddings BIBREF14 , and fine-tuned them during training. Refer to app:hyperparams for details on the other hyperparameters we used.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.05584:4:0` | full | 0:250 |

#### Rank 4: qasper-passage-v1-9a355703fa74783b49929ffa09c10704df67fa4a45f230e54f1191e31700e0b8

Passage ID: `qasper-passage-v1-9a355703fa74783b49929ffa09c10704df67fa4a45f230e54f1191e31700e0b8`; retrieval score: 4.44349466321595.

Word count: 378.

```text
Incorporating sub-word structures like substrings, morphemes and characters to the creation of word representations significantly increases their quality as reflected both by intrinsic metrics and performance in a wide range of downstream tasks BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 .

The reason for this improvement is related to sub-word structures containing information that is usually ignored by standard word-level models. Indeed, when representing words as vectors extracted from a lookup table, semantically related words resulting from inflectional processes such as surf, surfing, and surfed, are treated as being independent from one another. Further, word-level embeddings do not account for derivational processes resulting in syntactically-similar words with different meanings such as break, breakable, and unbreakable. This causes derived words, which are usually less frequent, to have lower-quality (or no) vector representations.

Previous works have successfully combined character-level and word-level word representations, obtaining overall better results than using only word-level representations. For example BIBREF1 achieved state-of-the-art results in a machine translation task by representing unknown words as a composition of their characters. BIBREF4 created word representations by adding the vector representations of the words' surface forms and their morphemes ( INLINEFORM0 ), obtaining significant improvements on intrinsic evaluation tasks, word similarity and machine translation. BIBREF5 concatenated character-level and word-level representations for creating word representations, and then used them as input to their models for obtaining state-of-the-art results in Named Entity Recognition on several languages.

What these works have in common is that the models they describe first learn how to represent subword information, at character BIBREF1 , morpheme BIBREF4 , or substring BIBREF0 levels, and then combine these learned representations at the word level. The incorporation of information at a finer-grained hierarchy results in higher-quality modeling of rare words, morphological processes, and semantics BIBREF6 .

There is no consensus, however, on which combination method works better in which case, or how the choice of a combination method affects downstream performance, either measured intrinsically at the word level, or extrinsically at the sentence level.

In this paper we aim to provide some intuitions about how the choice of mechanism for combining character-level with word-level representations influences the quality of the final word representations, and the subsequent effect these have in the performance of downstream tasks. Our contributions are as follows:
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-a5c075f743ea1fdbcfb540f990d25c8c01d9e3cd6f5592e6074b00ef10361ac6

Passage ID: `qasper-passage-v1-a5c075f743ea1fdbcfb540f990d25c8c01d9e3cd6f5592e6074b00ef10361ac6`; retrieval score: 4.1905254165528145.

Word count: 400.

```text
table:wordlevelresults shows the quality of word representations in terms of the correlation between word similarity scores obtained by the proposed models and word similarity scores defined by humans.

First, we can see that for each task, character only models had significantly worse performance than every other model trained on the same dataset. The most likely explanation for this is that these models are the only ones that need to learn word representations from scratch, since they have no access to the global semantic knowledge encoded by the GloVe embeddings.

Further, bold results show the overall trend that vector gates outperformed the other methods regardless of training dataset. This implies that learning how to combine character and word-level representations at the dimension level produces word vector representations that capture a notion of word similarity and relatedness that is closer to that of humans.

Additionally, results from the MNLI row in general, and underlined results in particular, show that training on MultiNLI produces word representations better at capturing word similarity. This is probably due to MultiNLI data being richer than that of SNLI. Indeed, MultiNLI data was gathered from various sources (novels, reports, letters, and telephone conversations, among others), rather than the single image captions dataset from which SNLI was created.

Exceptions to the previous rule are models evaluated in MEN and RW. The former case can be explained by the MEN dataset containing only words that appear as image labels in the ESP-Game and MIRFLICKR-1M image datasets BIBREF24 , and therefore having data that is more closely distributed to SNLI than to MultiNLI.

More notably, in the RareWords dataset BIBREF25 , the word only, concat, and scalar gate methods performed equally, despite having been trained in different datasets ( INLINEFORM0 ), and the char only method performed significantly worse when trained in MultiNLI. The vector gate, however, performed significantly better than its counterpart trained in SNLI. These facts provide evidence that this method is capable of capturing linguistic phenomena that the other methods are unable to model.

table:word-similarity-dataset lists the word-similarity datasets and their corresponding reference. As mentioned in subsec:datasets, all the word-similarity datasets contain pairs of words annotated with similarity or relatedness scores, although this difference is not always explicit. Below we provide some details for each.

MEN contains 3000 annotated word pairs with integer scores ranging from 0 to 50. Words correspond to image labels appearing in the ESP-Game
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1381.

Fully covered answer annotations: ba4bf35bc0b271ac2b86145e2af2f4c6909a14eb.

Missing evidence by answer annotation:

```text
{
  "ba4bf35bc0b271ac2b86145e2af2f4c6909a14eb": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: 5bcc12680cf2eda2dd13ab763c42314a26f2d993

### Question ID and text

Question ID: `5bcc12680cf2eda2dd13ab763c42314a26f2d993`; paper ID: `1912.01046`.

```text
What evaluation metrics were used in the experiment?
```

### Answers

#### Answer: f466691953c65dd6bef779e24b5b85bb75615e7b

```text
{"evidence": ["Metrics. We use tolerance accuracy BIBREF16, which measures how far away the predicted span is from the gold standard span, as a metric. The rationale behind the metric is that, in practice, it suffices to recommend a rough span which contains the answer – a difference of a few seconds would not matter much to the user.", "Metrics. We used accuracy and MRR (Mean Reciprocal Ranking) as metrics. The accuracy is", "Metrics. To evaluate our pipeline approach we use overall accuracy after filtering and accuracy given that the segment is in the top 10 videos. While the first metric is similar to SECREF17, the second can indicate if initially searching on the video space can be used to improve our selection:"], "extractive_spans": [], "free_form_answer": "For sentence-level prediction they used tolerance accuracy, for segment retrieval accuracy and MRR and for the pipeline approach they used overall accuracy", "highlighted_evidence": ["Metrics. We use tolerance accuracy BIBREF16, which measures how far away the predicted span is from the gold standard span, as a metric. The rationale behind the metric is that, in practice, it suffices to recommend a rough span which contains the answer – a difference of a few seconds would not matter much to the user.", "Metrics. We used accuracy and MRR (Mean Reciprocal Ranking) as metrics. ", "Metrics. To evaluate our pipeline approach we use overall accuracy after filtering and accuracy given that the segment is in the top 10 videos. "], "unanswerable": false, "yes_no": null}
```

Evidence location: `1912.01046:8:5`

```text
Metrics. We use tolerance accuracy BIBREF16, which measures how far away the predicted span is from the gold standard span, as a metric. The rationale behind the metric is that, in practice, it suffices to recommend a rough span which contains the answer – a difference of a few seconds would not matter much to the user.
```

Evidence location: `1912.01046:9:5`

```text
Metrics. We used accuracy and MRR (Mean Reciprocal Ranking) as metrics. The accuracy is
```

Evidence location: `1912.01046:10:4`

```text
Metrics. To evaluate our pipeline approach we use overall accuracy after filtering and accuracy given that the segment is in the top 10 videos. While the first metric is similar to SECREF17, the second can indicate if initially searching on the video space can be used to improve our selection:
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-e1d40c1ac39796f32e8a36255fcb3aa210e3d96991801250ef55e3aac4a1dcaf

Passage ID: `qasper-passage-v1-e1d40c1ac39796f32e8a36255fcb3aa210e3d96991801250ef55e3aac4a1dcaf`; retrieval score: 4.38369294964641.

Word count: 236.

```text
Table TABREF12 presents some extracted sample questions from our dataset. The first column corresponds to an AMT generated question, while the second column corresponds to the video ID where the segment can be found. As can be seen in the first two rows, multiple types of questions can be answered within the same video (but different segments). The last two rows display questions which belong to the same segment but correspond to different properties of the same entity, 'crop tool'. Here we observe different types of questions, such as "why", "how", "what", and "where", and can see why the answers may involve multiple steps. Some questions that the worked paraphrased were in the "yes/no" style, however our answer segments then provide an explanation to these questions.

Each answer segment was extracted from an image editing tutorial video that involved multiple steps and procedures to produce a final image, which can partially be seen in FIGREF1. The average number of sentences per video was approximately 52, with the maximum number of sentences contained in a video being 187. The sub-tasks in the tutorial include segments (and thus answers) on editing parts of images, instructions on using certain tools, possible actions that can be performed on an image, and identifying the locations of tools and features, with the shortest and longest segment having a span of 1 and 37 sentences respectively, demonstrating the heterogeneity of the answer spans.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-bdf69cfaaec47ca9106b979a6aad1fda43b25a09cab50b8829992b9646296268

Passage ID: `qasper-passage-v1-bdf69cfaaec47ca9106b979a6aad1fda43b25a09cab50b8829992b9646296268`; retrieval score: 4.277876807884159.

Word count: 95.

```text
video and a question, as illustrated in Figure FIGREF1.

The remainder of this paper is structured as follows. Section SECREF3 introduces TutorialVQA dataset as a case study of our proposed problem. The dataset includes about 6,000 triples, comprised of videos, questions, and answer spans manually collected from screencast tutorial videos with spoken narratives for a photo-editing software. Section SECREF4 presents the baseline models and their experiment details on the sentence-level prediction and video segment retrieval tasks on our dataset. Then, we discuss the experimental results in Section SECREF5 and conclude the paper in Section SECREF6.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-6e2a689a4abe33581b53eabb16d40a929ec89e2f52a0f5ee69fef565761dc3b5

Passage ID: `qasper-passage-v1-6e2a689a4abe33581b53eabb16d40a929ec89e2f52a0f5ee69fef565761dc3b5`; retrieval score: 4.26390731463689.

Word count: 400.

```text
We downloaded 76 videos from a tutorial website about an image editing program . Each video is pre-processed to provide the transcripts and the time-stamp information for each sentence in the transcript. We then used Amazon Mechanical Turk to collect the question-answer pairs . One naive way of collecting the data is to prepare a question list and then, for each question, ask the workers to find the relevant parts in the video. However, this approach is not feasible and error-prone because the videos are typically long and finding a relevant part from a long video is difficult. Doing so might also cause us to miss questions which were relevant to the video segment. Instead, we took a reversed approach. First, for each video, we manually identified the sentence spans that can serve as answers. These candidates are of various granularity and may overlap. The segments are also complete in that they encompass the beginning and end of a task. In total, we identified 408 segments from the 76 videos. Second we asked AMT workers to provide question annotations for the videos.

Our AMT experiment consisted of two parts. In the first part, we presented the workers with the video content of a segment. For each segment, we asked workers to generate questions that can be answered by the presented segment. We did not limit the number of questions a worker can input to a corresponding segment and encouraged them to input a diverse set of questions which the span can answer. Along with the questions, the workers were also required to provide a justification as to why they made their questions. We manually checked this justification to filter out the questions with poor quality by removing those questions which were unrelated to the video. One initial challenge worth mentioning is that at first some workers input questions they had about the video and not questions which the video could answer. This was solved by providing them with an unrelated example. The second part of the question collection framework consisted of a paraphrasing task. In this task we presented workers with the questions generated by the first task and asked them to write the questions differently while keeping the semantics the same. In this way, we expanded our question dataset. After filtering out the questions with low quality, we collected a total of 6,195 questions.

It is important to note
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-928a06784be730f6926120530b5f60b758a0e626038be022405308883adb29c9

Passage ID: `qasper-passage-v1-928a06784be730f6926120530b5f60b758a0e626038be022405308883adb29c9`; retrieval score: 3.764195951229903.

Word count: 240.

```text
We also considered a simpler task by casting our problem as a retrieval task. Specifically, in addition to a plain transcript, we also provided the model with the segmentation information which was created during the data collection phrase (See Section. SECREF3). Note that each segments corresponds to a candidate answer. Then, the task is to pick the best segment for given a query. This task is easier than Baseline1's task in that the segmentation information is provided to the model. Unlike Baseline1, however, it is unable to return an answer span at various granularities. Baseline2 is based on the attentive LSTM BIBREF17, which has been developed for the InsuranceQA task. The right diagram in Fig. FIGREF15 illustrates the Baseline2 model.

Model. The two inputs, $s$ and $q$ represent the segment text and a question. The model first encodes the two inputs.

$h^s$ is then re-weighted using attention weights.

where $\odot $ denotes the element-wise multiplication operation. The final score is computed using a one-layer feed-forward network.

During training, the model requires negative samples. For each positive example, (question, ground-truth segment), all the other segments in the same transcript are used as negative samples. Cross entropy is used as an objective function.

Metrics. We used accuracy and MRR (Mean Reciprocal Ranking) as metrics. The accuracy is

We split the ground-truth dataset to train/dev/test into the ratio of 6/2/2. The resulting size is 3,718 (train), 1,238 (dev) and 1,239 qa pairs (test).
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1912.01046:9:5` | full | 0:87 |

#### Rank 5: qasper-passage-v1-92adef2e12e9e50435651884021f51ee1faa077b0eb8415ab7c1cb545738cc8e

Passage ID: `qasper-passage-v1-92adef2e12e9e50435651884021f51ee1faa077b0eb8415ab7c1cb545738cc8e`; retrieval score: 3.241007459168168.

Word count: 400.

```text
Video is the fastest growing medium to create and deliver information today. Consequentially, videos have been increasingly used as main data sources in many question answering problems BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, BIBREF2, BIBREF5. These previous studies have mostly focused on factoid questions, each of which can be answered in a few words or phrases generated by understanding multimodal contents in a short video clip.

However, this problem definition of video question answering causes some practical limitations for the following reasons. First, factoid questions are just a small part of what people actually want to ask on video contents. Especially if a short video is given to users, most fragmentary facts within the scope of previous tasks can be easily perceived by themselves even before asking questions. Thus, video question answering is expected to provide answers to more complicated non-factoid questions beyond the simple facts. For example, those questions could be the ones asking about a how procedure as shown in Fig. FIGREF5, and the answers should contain all necessary steps to complete the task.

Accordingly, the answer format needs to also be improved towards more flexible ways than multiple choice BIBREF1, BIBREF2 or fill-in-the-blank questions BIBREF3, BIBREF4. Although open-ended video question answering BIBREF0, BIBREF2, BIBREF5 has been explored, it still aims to generate just a short word or phrase-level answer, which is not enough to cover various granularities of non-factoid question answering.

The other issue is that most videos with sufficient amount of information, which are likely to be asked, have much longer lengths than the video clips in the existing datasets. Therefore, the most relevant part of a whole video needs to be determined prior to each answer generation in practice. However, this localization task has been out of scope for previous studies.

In this work, we propose a new question answering problem for non-factoid questions on instructional videos. According to the nature of the media created for educational purposes, we assume that many answers already exist within the given video contents. Under this assumption, we formulate the problem as a localization task to specify the span of a video segment as the direct answer to a given video and a question, as illustrated in Figure FIGREF1.

The remainder of this paper is structured as follows. Section SECREF3 introduces TutorialVQA dataset as a case study of our proposed problem. The dataset includes about 6,000 triples, comprised of videos,
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 1371.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "f466691953c65dd6bef779e24b5b85bb75615e7b": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1912.01046:8:5": [
        [
          0,
          321
        ]
      ],
      "1912.01046:10:4": [
        [
          0,
          294
        ]
      ]
    }
  }
}
```

## Question: 3bfb8c12f151dada259fbd511358914c4b4e1b0e

### Question ID and text

Question ID: `3bfb8c12f151dada259fbd511358914c4b4e1b0e`; paper ID: `1709.01256`.

```text
What metrics are used to evaluation revision detection?
```

### Answers

#### Answer: 8b0add840d20bf740a040223502d86b77dee5181

```text
{"evidence": ["We use precision, recall and F-measure to evaluate the detected revisions. A true positive case is a correctly identified revision. A false positive case is an incorrectly identified revision. A false negative case is a missed revision record."], "extractive_spans": ["precision", "recall", "F-measure"], "free_form_answer": "", "highlighted_evidence": ["We use precision, recall and F-measure to evaluate the detected revisions."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1709.01256:12:0`

```text
We use precision, recall and F-measure to evaluate the detected revisions. A true positive case is a correctly identified revision. A false positive case is an incorrectly identified revision. A false negative case is a missed revision record.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-f249fec30255f59d5678cada6d0e7653614ec8c483a271b4f9c71580bb5b6bcb

Passage ID: `qasper-passage-v1-f249fec30255f59d5678cada6d0e7653614ec8c483a271b4f9c71580bb5b6bcb`; retrieval score: 4.9157707465989295.

Word count: 400.

```text
It is a common habit for people to keep several versions of documents, which creates duplicate data. A scholarly article is normally revised several times before being published. An academic paper may be listed on personal websites, digital conference libraries, Google Scholar, etc. In major corporations, a document typically goes through several revisions involving multiple editors and authors. Users would benefit from visualizing the entire history of a document. It is worthwhile to develop a system that is able to intelligently identify, manage and represent revisions. Given a collection of text documents, our study identifies revision relationships in a completely unsupervised way. For each document in a corpus we only use its content and the last modified timestamp. We assume that a document can be revised by many users, but that the documents are not merged together. We consider collaborative editing as revising documents one by one.

The two research problems that are most relevant to document revision detection are plagiarism detection and revision provenance. In a plagiarism detection system, every incoming document is compared with all registered non-plagiarized documents BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 . The system returns true if an original copy is found in the database; otherwise, the system returns false and adds the document to the database. Thus, it is a 1-to-n problem. Revision provenance is a 1-to-1 problem as it keeps track of detailed updates of one document BIBREF4 , BIBREF5 . Real-world applications include GitHub, version control in Microsoft Word and Wikipedia version trees BIBREF6 . In contrast, our system solves an n-to-n problem on a large scale. Our potential target data sources, such as the entire web or internal corpora in corporations, contain numerous original documents and their revisions. The aim is to find all revision document pairs within a reasonable time.

Document revision detection, plagiarism detection and revision provenance all rely on comparing the content of two documents and assessing a distance/similarity score. The classic document similarity measure, especially for plagiarism detection, is fingerprinting BIBREF7 , BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 . Fixed-length fingerprints are created using hash functions to represent document features and are then used to measure document similarities. However, the main purpose of fingerprinting is to reduce computation instead of improving accuracy, and it cannot capture word semantics. Another widely used approach is computing the sentence-to-sentence Levenshtein distance and assigning an overall score
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-316bd88d3d39f6260c778a96ee0d085f74a845c0d8cb8f887944ae610db77906

Passage ID: `qasper-passage-v1-316bd88d3d39f6260c778a96ee0d085f74a845c0d8cb8f887944ae610db77906`; retrieval score: 4.607913482638998.

Word count: 230.

```text
This paper has explored how DTW and TED can be extended with word2vec to construct semantic document distance measures: wDTW and wTED. By representing paragraphs with concatenations of word vectors, wDTW and wTED are able to capture the semantics of the words and thus give more accurate distance scores. In order to detect revisions, we have used minimum branching on an appropriately developed network with document distance scores serving as arc weights. We have also assessed the efficiency of the method of retrieving an optimal revision subnetwork by finding the minimum branching.

Furthermore, we have compared wDTW and wTED with several distance measures for revision detection tasks. Our results demonstrate the effectiveness and robustness of wDTW and wTED in the Wikipedia revision dumps and our simulated data sets. In order to reduce the computation time, we have computed document distances at the paragraph level and implemented a boosting learning system using Apache Spark. Although we have demonstrated the superiority of our semantic measures only in the revision detection experiments, wDTW and wTED can also be used as semantic distance measures in many clustering, classification tasks.

Our revision detection system can be enhanced with richer features such as author information and writing styles, and exact changes in revision pairs. Another interesting aspect we would like to explore in the future is reducing the complexities of calculating the distance between two paragraphs.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-06744bcb33419d06fd3176d9dd5041c8cb5ab3699e4f4469d2b6a1b4603b7659

Passage ID: `qasper-passage-v1-06744bcb33419d06fd3176d9dd5041c8cb5ab3699e4f4469d2b6a1b4603b7659`; retrieval score: 4.329418513075589.

Word count: 172.

```text
Our system is a boosting learner that is composed of four modules: weak filter, strong filter, revision network and optimal subnetwork. First of all, we sort all documents by timestamps and pair up documents so that we only compare each document with documents that have been created earlier. In the first module, we calculate the VSM similarity scores for all pairs and eliminate those with scores that are lower than an empirical threshold ( INLINEFORM0 ). This is what we call the weak filter. After that, we apply the strong filter wDTW or wTED on the available pairs and filter out document pairs having distances higher than a threshold INLINEFORM1 . For VSM in Section SECREF32 , we directly filter out document pairs having similarity scores lower than a threshold INLINEFORM2 . The cut-off threshold estimation is explained in Section SECREF30 . The remaining document pairs from the strong filter are then sent to the revision network module. In the end, we output the optimal revision pairs following the minimum branching strategy.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-1342ff3744af3d7bb57c5ce0b91492fcc498733d450a2984a711714608ea719e

Passage ID: `qasper-passage-v1-1342ff3744af3d7bb57c5ce0b91492fcc498733d450a2984a711714608ea719e`; retrieval score: 3.409611571086779.

Word count: 155.

```text
represent words, concatenate the word vectors to represent documents and combine word2vec with DTW or TED. Meanwhile, in order to guarantee reasonable computation time in large data sets, we calculate document distances at the paragraph level with Apache Spark. A distance score is computed by feeding paragraph representations to DTW or TED. Our code and data are publicly available.

The primary contributions of this work are as follows.

The rest of this paper is organized in five parts. In Section 2, we clarify related terms and explain the methodology for document revision detection. In Section 3, we provide a brief background on existing document similarity measures and present our wDTW and wTED algorithms as well as the overall process flow. In Section 4, we demonstrate our revision detection results on Wikipedia revision dumps and six simulated data sets. Finally, in Section 5, we summarize some concluding remarks and discuss avenues for future work and improvements.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-345cf79a2a433a2c34311cfe2456b9bbc7d80d5bc7c7b58c4a2d22802cb44b62

Passage ID: `qasper-passage-v1-345cf79a2a433a2c34311cfe2456b9bbc7d80d5bc7c7b58c4a2d22802cb44b62`; retrieval score: 3.300482351006038.

Word count: 382.

```text
We use precision, recall and F-measure to evaluate the detected revisions. A true positive case is a correctly identified revision. A false positive case is an incorrectly identified revision. A false negative case is a missed revision record.

We illustrate the performances of wDTW, wTED, WMD, VSM, PV-DTW and PV-TED on the Wikipedia revision dumps in Figure FIGREF43 . wDTW and wTED have the highest F-measure scores compared to the rest of four measures, and wDTW also have the highest precision and recall scores. Figure FIGREF49 shows the average evaluation results on the simulated data sets. From left to right, the corpus size increases and the revision chains become longer, thus it becomes more challenging to detect document revisions. Overall, wDTW consistently performs the best. WMD is slightly better than wTED. In particular, when the corpus size increases, the performances of WMD, VSM, PV-DTW and PV-TED drop faster than wDTW and wTED. Because the revision operations were randomly selected in each corpus, it is possible that there are non-monotone points in the series.

wDTW and wTED perform better than WMD especially when the corpus is large, because they use dynamic programming to find the global optimal alignment for documents. In contrast, WMD relies on a greedy algorithm that sums up the minimal cost for every word. wDTW and wTED perform better than PV-DTW and PV-TED, which indicates that our DistPara distance in Algorithm SECREF20 is more accurate than the Euclidian distance between paragraph vectors trained by PV.

We show in Table TABREF53 the average running time of the six distance/similarity measures. In all the experiments, VSM is the fastest, wTED is faster than wDTW, and WMD is the slowest. Running WMD is extremely expensive because WMD needs to solve an INLINEFORM0 sequential transshipment problem for every two documents where INLINEFORM1 is the average number of words in a document. In contrast, by splitting this heavy computation into several smaller problems (finding the distance between any two paragraphs), which can be run in parallel, wDTW and wTED scale much better.

Combining Figure FIGREF43 , Figure FIGREF49 and Table TABREF53 we conclude that wDTW yields the most accurate results using marginally more time than VSM, PV-TED and PV-DTW, but much less running time than WMD. wTED returns satisfactory results using shorter time than wDTW.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1709.01256:12:0` | full | 0:243 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1339.

Fully covered answer annotations: 8b0add840d20bf740a040223502d86b77dee5181.

Missing evidence by answer annotation:

```text
{
  "8b0add840d20bf740a040223502d86b77dee5181": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: 2c7e94a65f5f532aa31d3e538dcab0468a43b264

### Question ID and text

Question ID: `2c7e94a65f5f532aa31d3e538dcab0468a43b264`; paper ID: `1909.02027`.

```text
How was the dataset annotated?
```

### Answers

#### Answer: 8ae507d5fd72264c5e26b804f802e7fe35a3acb3

```text
{"evidence": ["We defined the intents with guidance from queries collected using a scoping crowdsourcing task, which prompted crowd workers to provide questions and commands related to topic domains in the manner they would interact with an artificially intelligent assistant. We manually grouped data generated by scoping tasks into intents. To collect additional data for each intent, we used the rephrase and scenario crowdsourcing tasks proposed by BIBREF2. For each intent, there are 100 training queries, which is representative of what a team with a limited budget could gather while developing a task-driven dialog system. Along with the 100 training queries, there are 20 validation and 30 testing queries per intent."], "extractive_spans": [], "free_form_answer": "intents are annotated manually with guidance from queries collected using a scoping crowdsourcing task", "highlighted_evidence": ["We defined the intents with guidance from queries collected using a scoping crowdsourcing task, which prompted crowd workers to provide questions and commands related to topic domains in the manner they would interact with an artificially intelligent assistant. We manually grouped data generated by scoping tasks into intents. "], "unanswerable": false, "yes_no": null}
```

Evidence location: `1909.02027:2:0`

```text
We defined the intents with guidance from queries collected using a scoping crowdsourcing task, which prompted crowd workers to provide questions and commands related to topic domains in the manner they would interact with an artificially intelligent assistant. We manually grouped data generated by scoping tasks into intents. To collect additional data for each intent, we used the rephrase and scenario crowdsourcing tasks proposed by BIBREF2. For each intent, there are 100 training queries, which is representative of what a team with a limited budget could gather while developing a task-driven dialog system. Along with the 100 training queries, there are 20 validation and 30 testing queries per intent.
```

#### Answer: ec4e8ed6bad6662d60e71d3c72c741cd3c33e6a9

```text
{"evidence": ["We defined the intents with guidance from queries collected using a scoping crowdsourcing task, which prompted crowd workers to provide questions and commands related to topic domains in the manner they would interact with an artificially intelligent assistant. We manually grouped data generated by scoping tasks into intents. To collect additional data for each intent, we used the rephrase and scenario crowdsourcing tasks proposed by BIBREF2. For each intent, there are 100 training queries, which is representative of what a team with a limited budget could gather while developing a task-driven dialog system. Along with the 100 training queries, there are 20 validation and 30 testing queries per intent."], "extractive_spans": ["manually "], "free_form_answer": "", "highlighted_evidence": [" We manually grouped data generated by scoping tasks into intents. "], "unanswerable": false, "yes_no": null}
```

Evidence location: `1909.02027:2:0`

```text
We defined the intents with guidance from queries collected using a scoping crowdsourcing task, which prompted crowd workers to provide questions and commands related to topic domains in the manner they would interact with an artificially intelligent assistant. We manually grouped data generated by scoping tasks into intents. To collect additional data for each intent, we used the rephrase and scenario crowdsourcing tasks proposed by BIBREF2. For each intent, there are 100 training queries, which is representative of what a team with a limited budget could gather while developing a task-driven dialog system. Along with the 100 training queries, there are 20 validation and 30 testing queries per intent.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-32689ec30ea40317d2a6f0601b4031133282687ab127e7471b18aff233278e37

Passage ID: `qasper-passage-v1-32689ec30ea40317d2a6f0601b4031133282687ab127e7471b18aff233278e37`; retrieval score: 2.835519558447419.

Word count: 151.

```text
Table TABREF14 presents results for all models across the four variations of the dataset. First, BERT is consistently the best approach for in-scope, followed by MLP. Second, out-of-scope query performance is much lower than in-scope across all methods. Training on less data (Small and Imbalanced) yields models that perform slightly worse on in-scope queries. The trend is mostly the opposite when evaluating out-of-scope, where recall increases under the Small and Imbalanced training conditions. Under these two conditions, the size of the in-scope training set was decreased, while the number of out-of-scope training queries remained constant. This indicates that out-of-scope performance can be increased by increasing the relative number of out-of-scope training queries. We do just that in the OOS+ setting—where the models were trained on the full training set as well as 150 additional out-of-scope queries—and see that performance on out-of-scope increases substantially, yet still remains low relative to in-scope accuracy.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-103c25ae66fbd18cc333f3a967e58ab671ad7a1ce084d3ad049ca4153909c93e

Passage ID: `qasper-passage-v1-103c25ae66fbd18cc333f3a967e58ab671ad7a1ce084d3ad049ca4153909c93e`; retrieval score: 2.5020425128569395.

Word count: 118.

```text
For all queries collected, all tokens were down-cased, and all end-of-sentence punctuation was removed. Additionally, all duplicate queries were removed and replaced.

In an effort to reduce bias in the in-scope data, we placed all queries from a given crowd worker in a single split (train, validation, or test). This avoids the potential issue of similar queries from a crowd worker ending up in both the train and test sets, for instance, which would make the train and test distributions unrealistically similar. We note that this is a recommendation from concurrent work by BIBREF3. We also used this procedure for the out-of-scope set, except that we split the data into train/validation/test based on task prompt instead of worker.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-afda18293eb85d4bb7e27f006707de563360350cf146f875b654eb6f0413d56c

Passage ID: `qasper-passage-v1-afda18293eb85d4bb7e27f006707de563360350cf146f875b654eb6f0413d56c`; retrieval score: 2.096972518371153.

Word count: 212.

```text
We use three baseline approaches for the task of predicting whether a query is out-of-scope: (1) oos-train, where we train an additional (i.e. 151st) intent on out-of-scope training data; (2) oos-threshold, where we use a threshold on the classifier's probability estimate; and (3) oos-binary, a two-stage process where we first classify a query as in- or out-of-scope, then classify it into one of the 150 intents if classified as in-scope.

To reduce the severity of the class imbalance between in-scope versus out-of-scope query samples (i.e., 15,000 versus 250 queries for OOS+), we investigate two strategies when using oos-binary: one where we undersample the in-scope data and train using 1,000 in-scope queries sampled evenly across all intents (versus 250 out-of-scope), and another where we augment the 250 OOS+ out-of-scope training queries with 14,750 sentences sampled from Wikipedia.

From a development point of view, the oos-train and oos-binary methods both require careful curation of an out-of-scope training set, and this set can be tailored to individual systems. The oos-threshold method is a more general decision rule that can be applied to any model that produces a probability. In our evaluation, the out-of-scope threshold was chosen to be the value which yielded the highest validation score across all intents, treating out-of-scope as its own intent.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-7a734cdc9af677388991ba1b5a7ba42fd3685fff81c0b753f59b6e917a123686

Passage ID: `qasper-passage-v1-7a734cdc9af677388991ba1b5a7ba42fd3685fff81c0b753f59b6e917a123686`; retrieval score: 1.7986751005870167.

Word count: 38.

```text
We introduce a new crowdsourced dataset of 23,700 queries, including 22,500 in-scope queries covering 150 intents, which can be grouped into 10 general domains. The dataset also includes 1,200 out-of-scope queries. Table TABREF2 shows examples of the data.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-02cb2744c931dfb5d523002484761b4d471d11546bf28b8028cf4f6594978315

Passage ID: `qasper-passage-v1-02cb2744c931dfb5d523002484761b4d471d11546bf28b8028cf4f6594978315`; retrieval score: 1.7365772173606304.

Word count: 400.

```text
In most other analyses and datasets, the idea of out-of-scope data is not considered, and instead the output classes are intended to cover all possible queries (e.g., TREC BIBREF7). Recent work by BIBREF8 considers a similar problem they call out-of-distribution detection. They use other datasets or classes excluded during training to form the out-of-distribution samples. This means that the out-of-scope samples are from a small set of coherent classes that differ substantially from the in-distribution samples. Similar experiments were conducted for evaluating unknown intent discovery models in BIBREF9. In contrast, our out-of-scope queries cover a broad range of phenomena and are similar in style and often similar in topic to in-scope queries, representing things a user might say given partial knowledge of the capabilities of a system.

Table TABREF20 compares our dataset with other short-query intent classification datasets. The Snips BIBREF0 dataset and the dataset presented in BIBREF10 are the most similar to the in-scope part of our work, with the same type of conversational agent requests. Like our work, both of these datasets were bootstrapped using crowdsourcing. However, the Snips dataset has only a small number of intents and an enormous number of examples of each. Snips does present a low-data variation, with 70 training queries per intent, in which performance drops slightly. The dataset presented in BIBREF10 has a large number of intent classes, yet also contains a wide range of samples per intent class (ranging from 24 to 5,981 queries per intent, and so is not constrained in all cases).

BIBREF11 created datasets with constrained training data, but with very few intents, presenting a very different type of challenge. We also include the TREC query classification datasets BIBREF7, which have a large set of labels, but they describe the desired response type (e.g., distance, city, abbreviation) rather than the action intents we consider. Moreover, TREC contains only questions and no commands. Crucially, none of the other datasets summarized in Table TABREF20 offer a feasible way to evaluate out-of-scope performance.

The Dialog State Tracking Challenge (DSTC) datasets are another related resource. Specifically, DSTC 1 BIBREF12, DSTC 2 BIBREF13, and DSTC 3 BIBREF14 contain “chatbot style" queries, but the datasets are focused on state tracking. Moreover, most if not all queries in these datasets are in-scope. In contrast, the focus of our analysis is on both in- and out-of-scope queries that challenge a virtual assistant to determine whether it
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 919.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "8ae507d5fd72264c5e26b804f802e7fe35a3acb3": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1909.02027:2:0": [
        [
          0,
          711
        ]
      ]
    }
  },
  "ec4e8ed6bad6662d60e71d3c72c741cd3c33e6a9": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1909.02027:2:0": [
        [
          0,
          711
        ]
      ]
    }
  }
}
```

## Question: e755fb599690d0d0c12ddb851ac731a0a7965797

### Question ID and text

Question ID: `e755fb599690d0d0c12ddb851ac731a0a7965797`; paper ID: `1901.09755`.

```text
Which six languages are experimented with?
```

### Answers

#### Answer: 91ea275060a44b2fa896afa9991282a4390606b4

```text
{"evidence": ["In this section we report on the experiments performed using the system and data described above. First we will present the English results for the three ABSA editions as well as a comparison with previous work. After that we will do the same for 5 additional languages included in the ABSA 2016 edition: Dutch, French, Russian, Spanish and Turkish. The local and clustering features, as described in Section SECREF11 , are the same for every language and evaluation setting. The only change is the clustering lexicons used for the different languages. As stated in section SECREF11 , the best cluster combination is chosen via 5-fold cross validation (CV) on the training data. We first try every permutation with the Clark and Word2vec clusters. Once the best combination is obtained, we then try with the Brown clusters obtaining thus the final model for each language and dataset."], "extractive_spans": ["Dutch", "French", "Russian", "Spanish ", "Turkish", "English "], "free_form_answer": "", "highlighted_evidence": ["In this section we report on the experiments performed using the system and data described above. First we will present the English results for the three ABSA editions as well as a comparison with previous work. After that we will do the same for 5 additional languages included in the ABSA 2016 edition: Dutch, French, Russian, Spanish and Turkish. The local and clustering features, as described in Section SECREF11 , are the same for every language and evaluation setting. The only change is the clustering lexicons used for the different languages. As stated in section SECREF11 , the best cluster combination is chosen via 5-fold cross validation (CV) on the training data. We first try every permutation with the Clark and Word2vec clusters. Once the best combination is obtained, we then try with the Brown clusters obtaining thus the final model for each language and dataset."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1901.09755:7:0`

```text
In this section we report on the experiments performed using the system and data described above. First we will present the English results for the three ABSA editions as well as a comparison with previous work. After that we will do the same for 5 additional languages included in the ABSA 2016 edition: Dutch, French, Russian, Spanish and Turkish. The local and clustering features, as described in Section SECREF11 , are the same for every language and evaluation setting. The only change is the clustering lexicons used for the different languages. As stated in section SECREF11 , the best cluster combination is chosen via 5-fold cross validation (CV) on the training data. We first try every permutation with the Clark and Word2vec clusters. Once the best combination is obtained, we then try with the Brown clusters obtaining thus the final model for each language and dataset.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-796c833c4f5848ca26ab3aa41d2f50a3ada1cfa8b2b3c61d0a43549e61cfa937

Passage ID: `qasper-passage-v1-796c833c4f5848ca26ab3aa41d2f50a3ada1cfa8b2b3c61d0a43549e61cfa937`; retrieval score: 5.043889660372256.

Word count: 233.

```text
review are tagged depending on whether they are at the beginning (B-target), inside (I-target) or outside (O) of the opinion target expression. Note that the third opinion target in Figure FIGREF1 is implicit.

We learn language independent models which consist of a set of local, shallow features complemented with semantic distributional features based on clusters obtained from a variety of data sources. We show that our approach, despite the lack of hand-engineered, language-specific features, obtains state-of-the-art results in 7 datasets for 6 languages on the ABSA benchmarks BIBREF4 , BIBREF5 , BIBREF6 .

The main contribution of this research note is providing an extension or addendum to previous work on sequence labelling BIBREF7 by reporting additional experimental results as well as further insights on the performance of our model across languages on a different NLP task such as Opinion Target Extraction (OTE). Thus, we empirically demonstrate the validity and strong performance of our approach for six languages in seven different datasets of the restaurant domain. Every experiment and result presented in this note is novel.

In this sense, we show that our approach is not only competitive across languages and domains for Named Entity Recognition, as shown by BIBREF7 , but that it can be straightforwardly adapted to different tasks and domains such as OTE. Furthermore, we release the system and every model trained for public use and to facilitate reproducibility of results.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-763bbb76e254c54d8489c0b34c158eb85fed7a1b3241c639680307219c7c30f6

Passage ID: `qasper-passage-v1-763bbb76e254c54d8489c0b34c158eb85fed7a1b3241c639680307219c7c30f6`; retrieval score: 2.7755494937093435.

Word count: 378.

```text
We trained our system for 5 other languages on the ABSA 2016 datasets, using the same strategy as for English. We choose the best Clark-Word2vec combination (with and without Brown clusters) via 5-cross validation on the training data. The features are exactly the same as those used for English, the only change is the data on which the clusters are trained. Table TABREF19 reports on the detailed results obtained for each of the languages. In bold we show the best model chosen via 5-fold CV. Moreover, we also show the best models using only one of each of the clustering features.

The first difference with respect to the English results is that the Brown clustering features are, in three out of five settings, detrimental to performance. Second, that combining clustering features is only beneficial for Spanish. Third, the overall results are in general lower than those obtained in the 2016 English data. Finally, the difference between the best results and the results using the Local features is lower than for English, even though the Local results are similar to those obtained with the English datasets (except for Turkish, but this is due to the significantly smaller size of the data, as shown in Table TABREF7 ).

We believe that all these four issues are caused, at least partially, by the lack of domain-specific clustering features used for the multilingual experiments. In other words, while for the English experiments we leveraged the Yelp dataset to train the clustering algorithms, in the multilingual setting we first tried with already available clusters induced from the Wikipedia. Thus, it is to be expected that the gains obtained by clustering features obtained from domain-specific data such as Yelp would be superior to those achieved by the clusters trained on out-of-domain data.

In spite of this, Table TABREF20 shows that our system outperforms the best previous approaches across the five languages. In some cases, such as Turkish and Russian, the best previous scores were the baselines provided by the ABSA organizers, but for Dutch, French and Spanish our system is significantly better than current state-of-the-art. In particular, and despite using the same system for every language, we improve over GTI's submission, which implemented a CRF system with linguistic features specific to Spanish BIBREF28 .
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-fe34835b958a064bb39dc8bab81b9c858e4ded32e851740475dea4a9469403fa

Passage ID: `qasper-passage-v1-fe34835b958a064bb39dc8bab81b9c858e4ded32e851740475dea4a9469403fa`; retrieval score: 2.512304416370324.

Word count: 61.

```text
of text is positive, negative, or neutral with respect to an aspect and a given target (which in Stance Detection is called “author's favorability” towards a given target). However, in Stance Detection the text may express opinion or sentiment about some other target, not mentioned in the given text, and the targets are predefined, whereas in ABSA the targets are open-ended.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-05b3c8f7a00498ef15feb9f4802f37373f3081269c49dfdc01b6e08021f3981f

Passage ID: `qasper-passage-v1-05b3c8f7a00498ef15feb9f4802f37373f3081269c49dfdc01b6e08021f3981f`; retrieval score: 2.468431234946939.

Word count: 400.

```text
We will now discuss the shortcomings and most common errors performed by our system for the OTE task. By looking at the overall results in terms of precision and recall, it is possible to see the following patterns: With respect to the Local models, precision is consistently better than recall or, in other words, the coverage of the Local models is quite low. Tables TABREF16 and TABREF19 show that adding clustering features to the Local models allows to improve the recall for every evaluation setting, although with different outcomes. Overall, precision suffers, except for French. Furthermore, in three cases (English 2014, 2016 and Russian) precision is lower than recall, whereas the remaining 5 evaluations show that, despite large improvements in F1 score, most errors in our system are caused by false negatives, as it can be seen in Table TABREF23 .

Table TABREF25 displays the top 5 most common false positives and false negative errors for English, Spanish and French. By inspecting our system's output, and both the test and training sets, we found out that there were three main sources of errors: (a) errors caused by ambiguity in the use of certain source forms that may or may not refer to an opinion target; (b) span errors, where the target has only been partially annotated; and (c) unknown targets, which the system was unable to annotate by generalizing on the training data or clusters.

With respect to type (a), it is useful to look at the most common errors for all three languages, namely, `place', `food' and `restaurant', which are also among the top 5 most frequent targets in the gold standard sets. By looking at Examples (1-3) we would say that in all three cases `place' should be annotated as opinion target. However, (2) is a false positive (FP), (3) is a false negative (FN) and (1) is an example from the training set in which `place' is annotated as target. This is the case with many instances of `place' for which there seems to be some inconsistency in the actual annotation of the training and test set examples.

Example (1): Avoid this place!

Example (2): this place is a keeper!

Example (3): it is great place to watch sporting events.

For other frequent type (a) errors, ambiguity is the main problem. Thus, in Spanish the use of `comida' and `restaurante' is highly ambiguous and causes many FPs
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-384ad8f6cf8805aa780e4795a1135c6453c236988d9ea5d4d65d34f526703ada

Passage ID: `qasper-passage-v1-384ad8f6cf8805aa780e4795a1135c6453c236988d9ea5d4d65d34f526703ada`; retrieval score: 2.282318778314308.

Word count: 400.

```text
Considering the simplicity of our approach, we obtain best results for 6 languages and 7 different settings in the Opinion Target Extraction (OTE) benchmark for the restaurant domain using the ABSA 2014-2016 datasets.

These results are obtained without linguistic or manually-engineered features, relying on injecting external knowledge from the combination of clustering features to obtain a robust system across languages, outperforming other more complex and language-specific systems. Furthermore, the feature set used is the same for every setting, reducing human intervention to a minimum and establishing a clear methodology for a fast and easy creation of competitive OTE multilingual taggers.

The results also confirm the behaviour of these clustering algorithms to provide features for sequence labelling tasks such as OTE and Named Entity Recognition (NER), as previously discussed in BIBREF7 . Thus, in every evaluation setting the best results using Brown clusters as features were obtained when data close to the application domain and text genre, even if relatively small, was used to train the Brown algorithm. This can be clearly seen if we compare the English with the multilingual results. For English, the models including Brown clusters improve the Local features over 3-5 points in F1 score, whereas for Spanish, Dutch and Russian, they worsen performance. The reason is that for English the Yelp dataset is used whereas for the rest of languages the clusters are induced using the Wikipedia, effectively an out-of-domain corpus. The exception is Turkish, for which a 6 point gain in F1 score is obtained, but we believe that is probably due to the small size of the training data used for training the Local model.

In contrast, Word2vec clusters clearly benefit from larger amounts of data, as illustrated by the best English Word2vec model being the one trained using the Wikipedia, and not the Yelp dataset, which is closer to the application domain. Finally, the Clark algorithm seems to be the most versatile as it consistently outperforms the other two clustering methods in 4 out of the 8 evaluation settings presented.

Summarizing: (i) Brown clusters perform better when leveraged from source data close to the application domain, even if small in size; (ii) Clark clusters are the most robust of the three with respect to the size and domain of the data used; and (iii) for Word2vec size is the crucial factor. The larger the source data the better the performance. Thus, instead of
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1472.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "91ea275060a44b2fa896afa9991282a4390606b4": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1901.09755:7:0": [
        [
          0,
          884
        ]
      ]
    }
  }
}
```

## Question: 249c805ee6f2ebe4dbc972126b3d82fb09fa3556

### Question ID and text

Question ID: `249c805ee6f2ebe4dbc972126b3d82fb09fa3556`; paper ID: `1908.04042`.

```text
how is diversity measured?
```

### Answers

#### Answer: d2cfcf7026276f37987b7046f0254de03b31794a

```text
{"evidence": ["Recommendation diversity. As defined in BIBREF18 , we calculate recommendation diversity as the average dissimilarity of all pairs of tags in the list of recommended tags. Thus, given a distance function INLINEFORM0 that corresponds to the dissimilarity between two tags INLINEFORM1 and INLINEFORM2 in the list of recommended tags, INLINEFORM3 is given as the average dissimilarity of all pairs of tags: DISPLAYFORM0"], "extractive_spans": ["average dissimilarity of all pairs of tags in the list of recommended tags"], "free_form_answer": "", "highlighted_evidence": ["Recommendation diversity. As defined in BIBREF18 , we calculate recommendation diversity as the average dissimilarity of all pairs of tags in the list of recommended tags."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1908.04042:6:8`

```text
Recommendation diversity. As defined in BIBREF18 , we calculate recommendation diversity as the average dissimilarity of all pairs of tags in the list of recommended tags. Thus, given a distance function INLINEFORM0 that corresponds to the dissimilarity between two tags INLINEFORM1 and INLINEFORM2 in the list of recommended tags, INLINEFORM3 is given as the average dissimilarity of all pairs of tags: DISPLAYFORM0 
```

#### Answer: efcf2d9d61895fe92fc32957b54c1eaf84c3b9e1

```text
{"evidence": ["Recommendation diversity. As defined in BIBREF18 , we calculate recommendation diversity as the average dissimilarity of all pairs of tags in the list of recommended tags. Thus, given a distance function INLINEFORM0 that corresponds to the dissimilarity between two tags INLINEFORM1 and INLINEFORM2 in the list of recommended tags, INLINEFORM3 is given as the average dissimilarity of all pairs of tags: DISPLAYFORM0"], "extractive_spans": [" the average dissimilarity of all pairs of tags in the list of recommended tags"], "free_form_answer": "", "highlighted_evidence": ["As defined in BIBREF18 , we calculate recommendation diversity as the average dissimilarity of all pairs of tags in the list of recommended tags. "], "unanswerable": false, "yes_no": null}
```

Evidence location: `1908.04042:6:8`

```text
Recommendation diversity. As defined in BIBREF18 , we calculate recommendation diversity as the average dissimilarity of all pairs of tags in the list of recommended tags. Thus, given a distance function INLINEFORM0 that corresponds to the dissimilarity between two tags INLINEFORM1 and INLINEFORM2 in the list of recommended tags, INLINEFORM3 is given as the average dissimilarity of all pairs of tags: DISPLAYFORM0 
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-42df1276f2a3079ee57163a2ec4b8bea81ec08d6c62dbce81c72b75ae58e3536

Passage ID: `qasper-passage-v1-42df1276f2a3079ee57163a2ec4b8bea81ec08d6c62dbce81c72b75ae58e3536`; retrieval score: 2.6815124935336367.

Word count: 213.

```text
are to the expected review keywords. For this, we first extract the textual content in the form of the description text, title, editor tags and Amazon search terms of e-books from our dataset. We then train a Doc2Vec BIBREF7 model on the content. Then, we use the model to infer the latent representation for both the complete list of recommended tags as well as the list of expected tags from the test set. Finally, we use the cosine similarity measure to calculate how semantically similar these two lists are.

Recommendation diversity. As defined in BIBREF18 , we calculate recommendation diversity as the average dissimilarity of all pairs of tags in the list of recommended tags. Thus, given a distance function INLINEFORM0 that corresponds to the dissimilarity between two tags INLINEFORM1 and INLINEFORM2 in the list of recommended tags, INLINEFORM3 is given as the average dissimilarity of all pairs of tags: DISPLAYFORM0

where INLINEFORM0 is the number of evaluated e-books and the dissimilarity function is defined as INLINEFORM1 . In our experiments, we use the previously trained Doc2Vec model to extract the latent representation of a specific tag. The similarity of two tags INLINEFORM2 is then calculated with the Cosine similarity measure using the latent vector representations of respective tags INLINEFORM3 and INLINEFORM4 .
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.04042:6:8` | full | 0:416 |

#### Rank 2: qasper-passage-v1-83a824835c3aaba8cc9e0d776d691e3ca8d1dcc6538f2768ac16724d870be970

Passage ID: `qasper-passage-v1-83a824835c3aaba8cc9e0d776d691e3ca8d1dcc6538f2768ac16724d870be970`; retrieval score: 2.6159957186352605.

Word count: 400.

```text
In this work, we measure (i) recommendation accuracy, (ii) semantic similarity, and (iii) recommendation diversity to evaluate the quality of our approaches from different perspectives.

Recommendation accuracy. We use Normalized Discounted Cumulative Gain (nDCG) BIBREF15 to measure the accuracy of the tag recommendation approaches. The nDCG measure is a standard ranking-dependent metric that not only measures how many tags can be correctly predicted but also takes into account their position in the recommendation list with length of INLINEFORM0 . It is based on the Discounted Cummulative Gain, which is given by: DISPLAYFORM0

where INLINEFORM0 is a function that returns 1 if the recommended tag at position INLINEFORM1 in the recommended list is relevant. We then calculate DCG@ INLINEFORM2 for every evaluated e-book by dividing DCG@ INLINEFORM3 with the ideal DCG value iDCG@ INLINEFORM4 , which is the highest possible DCG value that can be achieved if all the relevant tags would be recommended in the correct order. It is given by the following formula BIBREF15 : DISPLAYFORM0

Semantic similarity. One precondition of standard recommendation accuracy measures is that to generate a “hit”, the recommended tag needs to be an exact syntactical match to the one from the test set. When tags are recommended from one data source and compared to tags from another source, this can be problematic. For example, if we recommend the tag “victim” but expect the tag “prey”, we would mark this as a mismatch, therefore being a bad recommendation. But if we know that the corresponding e-book is a crime novel, the recommended tag would be (semantically) descriptive to reflect the book's content. Hence, in this paper, we propose to additionally measure the semantic similarity between recommended tags and tags from the test set (i.e., the Amazon review keywords).

Over the last four years, there have been several notable publications in the area of applying deep learning to uncover semantic relationships between textual content (e.g., by learning word embeddings with Word2Vec BIBREF16 , BIBREF17 ). Based on this, we propose an alternative measure of recommendation quality by learning the semantic relationships from both vocabularies and then using it to compare how semantically similar the recommended tags are to the expected review keywords. For this, we first extract the textual content in the form of the description text, title, editor tags and Amazon search terms of e-books from our dataset. We then train a Doc2Vec BIBREF7 model
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-8087fb76156a747c26afe036220c2f4354241a396007f53056793aeba4f94a31

Passage ID: `qasper-passage-v1-8087fb76156a747c26afe036220c2f4354241a396007f53056793aeba4f94a31`; retrieval score: 2.481642312974187.

Word count: 205.

```text
also to use beyond-accuracy metrics such as diversity to evaluate the quality of tag recommendations. In our work, we measure recommendation diversity in addition to recommendation accuracy and propose a novel metric termed semantic similarity to validate semantic matches of tag recommendations.

Approach and findings. We exploit editor tags and user-generated search terms as input for tag recommendation approaches. Our evaluation comprises of a rich set of 19 different algorithms to recommend tags for e-books, which we group into (i) popularity-based, (ii) similarity-based (i.e., using content information), and (iii) hybrid approaches. We evaluate our approaches in terms of accuracy, semantic similarity and diversity on the review content of Amazon users, which reflects the readers' vocabulary. With semantic similarity, we measure how semantically similar (based on learned Doc2Vec BIBREF7 embeddings) the list of recommended tags is to the list of relevant tags. We use this additional metric to measure not only exact “hits” of our recommendations but also semantic matches.

Our evaluation results show that combining both data sources enhances the quality of tag recommendations for annotating e-books. Furthermore, approaches that solely train on Amazon search terms provide poor performance in terms of accuracy but deliver good results in terms of semantic similarity and recommendation diversity.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-021509bb7a06e0a42204499f136baaba1344b6df2263c4dfb566e569ac9a64a0

Passage ID: `qasper-passage-v1-021509bb7a06e0a42204499f136baaba1344b6df2263c4dfb566e569ac9a64a0`; retrieval score: 1.1950405302440852.

Word count: 400.

```text
When people shop for books online in e-book stores such as, e.g., the Amazon Kindle store, they enter search terms with the goal to find e-books that meet their preferences. Such e-books have a variety of metadata such as, e.g., title, author or keywords, which can be used to retrieve e-books that are relevant to the query. As a consequence, from the perspective of e-book publishers and editors, annotating e-books with tags that best describe the content and which meet the vocabulary of users (e.g., when searching and reviewing e-books) is an essential task BIBREF0 .

Problem and aim of this work. Annotating e-books with suitable tags is, however, a complex task as users' vocabulary may differ from the one of editors. Such a vocabulary mismatch yet hinders effective organization and retrieval BIBREF1 of e-books. For example, while editors mostly annotate e-books with descriptive tags that reflect the book's content, Amazon users often search for parts of the book title. In the data we use for the present study (see Section SECREF2 ), we find that around 30% of the Amazon search terms contain parts of e-book titles.

In this paper, we present our work to support editors in the e-book annotation process with tag recommendations BIBREF2 , BIBREF3 . Our idea is to exploit user-generated search query terms in Amazon to mimic the vocabulary of users in Amazon, who search for e-books. We combine these search terms with tags assigned by editors in a hybrid tag recommendation approach. Thus, our aim is to show that we can improve the performance of tag recommender systems for e-books both concerning recommendation accuracy as well as semantic similarity and tag recommendation diversity.

Related work. In tag recommender systems, mostly content-based algorithms (e.g., BIBREF4 , BIBREF5 ) are used to recommend tags to annotate resources such as e-books. In our work, we incorporate both content features of e-books (i.e., title and description text) as well as Amazon search terms to account for the vocabulary of e-book readers.

Concerning the evaluation of tag recommendation systems, most studies focus on measuring the accuracy of tag recommendations (e.g., BIBREF2 ). However, the authors of BIBREF6 suggest also to use beyond-accuracy metrics such as diversity to evaluate the quality of tag recommendations. In our work, we measure recommendation diversity in addition to recommendation accuracy and propose a novel metric termed semantic similarity to validate semantic matches of
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-9d449db79411f53f0213a674a06e69f82e7813e61e48176e262cea2341756e8f

Passage ID: `qasper-passage-v1-9d449db79411f53f0213a674a06e69f82e7813e61e48176e262cea2341756e8f`; retrieval score: 1.0559757233818894.

Word count: 277.

```text
Figure FIGREF16 illustrates the results of the experiments, which measure the recommendation impact beyond-accuracy.

Semantic similarity. Figure FIGREF16 illustrates the results of our proposed semantic similarity measure. To compare our proposed measure to standard accuracy measures such as INLINEFORM0 , we use Kendall's Tau rank correlation BIBREF19 as suggested by BIBREF20 for automatic evaluation of information-ordering tasks. From that, we rank our recommendation approaches according to both accuracy and semantic similarity and calculate the relation between both rankings. This results in INLINEFORM1 with a p-value < INLINEFORM2 , which suggests a high correlation between the semantic similarity and the standard accuracy measure.

Therefore, the semantic similarity measure helps us interpret the recommendation quality. For instance, we achieve the lowest INLINEFORM0 values with the similarity-based approaches that recommend Amazon search terms (i.e., INLINEFORM1 and INLINEFORM2 ). When comparing these results with others from Figure FIGREF11 , a conclusion could be quickly drawn that the recommended tags are merely unusable. However, by looking at Figure FIGREF16 , we see that, although these approaches do not provide the highest recommendation accuracy, they still result in tag recommendations that are semantically related at a high degree to the expected annotations from the test set. Overall, this suggests that approaches, which provide a poor accuracy performance concerning INLINEFORM4 but provide a good performance regarding semantic similarity could still be helpful for annotating e-books.

Recommendation diversity. Figure FIGREF16 shows the diversity of the tag recommendation approaches. We achieve the highest diversity with the similarity-based approaches, which extract Amazon search terms. Their accuracy is, however, very low. Thus, the combination of the two vocabularies can provide a good trade-off between recommendation accuracy and diversity.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1495.

Fully covered answer annotations: d2cfcf7026276f37987b7046f0254de03b31794a, efcf2d9d61895fe92fc32957b54c1eaf84c3b9e1.

Missing evidence by answer annotation:

```text
{
  "d2cfcf7026276f37987b7046f0254de03b31794a": {
    "unresolved_evidence": [],
    "paragraphs": {}
  },
  "efcf2d9d61895fe92fc32957b54c1eaf84c3b9e1": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: fbd47705262bfa0a2ba1440a2589152def64cbbd

### Question ID and text

Question ID: `fbd47705262bfa0a2ba1440a2589152def64cbbd`; paper ID: `1810.00663`.

```text
By how much did their model outperform the baseline?
```

### Answers

#### Answer: a6c1cfab37b756275380368b1d9f8cdb8929f57e

```text
{"evidence": ["First, we can observe that the final model “Ours with Mask and Ordered Triplets” outperforms the Baseline and Ablation models on all metrics in previously seen environments. The difference in performance is particularly evident for the Exact Match and Goal Match metrics, with our model increasing accuracy by 35% and 25% in comparison to the Baseline and Ablation models, respectively. These results suggest that providing the behavioral navigation graph to the model and allowing it to process this information as a knowledge base in an end-to-end fashion is beneficial.", "Lastly, it is worth noting that our proposed model (last row of Table TABREF28 ) outperforms all other models in previously seen environments. In particular, we obtain over INLINEFORM0 increase in EM and GM between our model and the next best two models."], "extractive_spans": ["increasing accuracy by 35% and 25% in comparison to the Baseline and Ablation models, respectively", "over INLINEFORM0 increase in EM and GM between our model and the next best two models"], "free_form_answer": "", "highlighted_evidence": ["First, we can observe that the final model “Ours with Mask and Ordered Triplets” outperforms the Baseline and Ablation models on all metrics in previously seen environments. The difference in performance is particularly evident for the Exact Match and Goal Match metrics, with our model increasing accuracy by 35% and 25% in comparison to the Baseline and Ablation models, respectively. These results suggest that providing the behavioral navigation graph to the model and allowing it to process this information as a knowledge base in an end-to-end fashion is beneficial.", "Lastly, it is worth noting that our proposed model (last row of Table TABREF28 ) outperforms all other models in previously seen environments. In particular, we obtain over INLINEFORM0 increase in EM and GM between our model and the next best two models."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1810.00663:10:1`

```text
First, we can observe that the final model “Ours with Mask and Ordered Triplets” outperforms the Baseline and Ablation models on all metrics in previously seen environments. The difference in performance is particularly evident for the Exact Match and Goal Match metrics, with our model increasing accuracy by 35% and 25% in comparison to the Baseline and Ablation models, respectively. These results suggest that providing the behavioral navigation graph to the model and allowing it to process this information as a knowledge base in an end-to-end fashion is beneficial.
```

Evidence location: `1810.00663:10:4`

```text
Lastly, it is worth noting that our proposed model (last row of Table TABREF28 ) outperforms all other models in previously seen environments. In particular, we obtain over INLINEFORM0 increase in EM and GM between our model and the next best two models.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-0906407de0d6d3587a5e4e428313c36f85e1189ecc7dbf4adddb485a03910b17

Passage ID: `qasper-passage-v1-0906407de0d6d3587a5e4e428313c36f85e1189ecc7dbf4adddb485a03910b17`; retrieval score: 4.995899565077083.

Word count: 400.

```text
commands. This resembles the way people find paths on a map: first, relevant parts on the map are selected according to their affinity to each of the words in the input instruction (attention layer); second, the selected parts are connected to assemble a valid path (decoder layer). More formally, let INLINEFORM2 ( INLINEFORM3 ) be the INLINEFORM4 -th row of INLINEFORM5 , and INLINEFORM6 ( INLINEFORM7 ) the INLINEFORM8 -th row of INLINEFORM9 . We use each encoded triplet INLINEFORM10 in INLINEFORM11 to calculate its associated attention distribution INLINEFORM12 over all the atomic instructions INLINEFORM13 : DISPLAYFORM0

where the matrix INLINEFORM0 serves to combine the different sources of information INLINEFORM1 and INLINEFORM2 . Each component INLINEFORM3 of the attention distributions INLINEFORM4 quantifies the affinity between the INLINEFORM5 -th triplet in INLINEFORM6 and the INLINEFORM7 -th word in the corresponding input INLINEFORM8 .

The model then uses each attention distribution INLINEFORM0 to obtain a weighted sum of the encodings of the words in INLINEFORM1 , according to their relevance to the corresponding triplet INLINEFORM2 . This results in L attention vectors INLINEFORM3 , INLINEFORM4 .

The final step in the attention layer concatenates each INLINEFORM0 with INLINEFORM1 to generate the outputs INLINEFORM2 , INLINEFORM3 . Following BIBREF8 , we include the encoded triplet INLINEFORM4 in the output tensor INLINEFORM5 of this layer to prevent early summaries of relevant map information.

FC layer: The model reduces the dimensionality of each individual vector INLINEFORM0 from INLINEFORM1 to INLINEFORM2 with a fully-connected (FC) layer. The resulting L vectors are output to the next layer as columns of a context matrix INLINEFORM3 .

Decoder layer: After the FC layer, the model predicts likelihoods over the sequence of behaviors that correspond to the input instructions with a GRU network. Without loss of generality, consider the INLINEFORM0 -th recurrent cell in the GRU network. This cell takes two inputs: a hidden state vector INLINEFORM1 from the prior cell, and a one-hot embedding of the previous behavior INLINEFORM2 that was predicted by the model. Based on these inputs, the GRU cell outputs a new hidden state INLINEFORM3 to compute likelihoods for the next behavior. These likelihoods are estimated by combining the output state INLINEFORM4 with relevant information from the context INLINEFORM5 : DISPLAYFORM0

where INLINEFORM0 , INLINEFORM1 , and INLINEFORM2 are trainable parameters. The attention vector INLINEFORM3 in Eq. () quantifies the affinity of INLINEFORM4 with respect to
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-08ecf14ba9dfa21d46efdfe72098d359d2a3a287a24e5bdc4282f61e20eaf6ef

Passage ID: `qasper-passage-v1-08ecf14ba9dfa21d46efdfe72098d359d2a3a287a24e5bdc4282f61e20eaf6ef`; retrieval score: 4.462779908631743.

Word count: 211.

```text
We compare the proposed approach for translating natural language instructions into a navigation plan against alternative deep-learning models:

[align=left,leftmargin=0em,labelsep=0.4em,font=]

The baseline approach is based on BIBREF20 . It divides the task of interpreting commands for behavioral navigation into two steps: path generation, and path verification. For path generation, this baseline uses a standard sequence-to-sequence model augmented with an attention mechanism, similar to BIBREF23 , BIBREF6 . For path verification, the baseline uses depth-first search to find a route in the graph that matches the sequence of predicted behaviors. If no route matches perfectly, the baseline changes up to three behaviors in the predicted sequence to try to turn it into a valid path.

To test the impact of using the behavioral graphs as an extra input to our translation model, we implemented a version of our approach that only takes natural language instructions as input. In this ablation model, the output of the bidirectional GRU that encodes the input instruction INLINEFORM0 is directly fed to the decoder layer. This model does not have the attention and FC layers described in Sec. SECREF4 , nor uses the masking function in the output layer.

This model is the same as the previous Ablation model, but with the masking function in the output layer.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-b726444849ea025d8e03a2c72eb03810a63583e2de8eab4085e8be0bd0c49305

Passage ID: `qasper-passage-v1-b726444849ea025d8e03a2c72eb03810a63583e2de8eab4085e8be0bd0c49305`; retrieval score: 4.441482851713305.

Word count: 397.

```text
This section discusses qualitative results to better understand how the proposed model uses the navigation graph.

We analyze the evolution of the attention weights INLINEFORM0 in Eq. () to assess if the decoder layer of the proposed model is attending to the correct parts of the behavioral graph when making predictions. Fig FIGREF33 (b) shows an example of the resulting attention map for the case of a correct prediction. In the Figure, the attention map is depicted as a scaled and normalized 2D array of color codes. Each column in the array shows the attention distribution INLINEFORM1 used to generate the predicted output at step INLINEFORM2 . Consequently, each row in the array represents a triplet in the corresponding behavioral graph. This graph consists of 72 triplets for Fig FIGREF33 (b).

We observe a locality effect associated to the attention coefficients corresponding to high values (bright areas) in each column of Fig FIGREF33 (b). This suggests that the decoder is paying attention to graph triplets associated to particular neighborhoods of the environment in each prediction step. We include additional attention visualizations in the supplementary Appendix, including cases where the dynamics of the attention distribution are harder to interpret.

All the routes in our dataset are the shortest paths from a start location to a given destination. Thus, we collected a few additional natural language instructions to check if our model was able to follow navigation instructions describing sub-optimal paths. One such example is shown in Fig. FIGREF37 , where the blue route (shortest path) and the red route (alternative path) are described by:

[leftmargin=*, labelsep=0.2em, itemsep=0em]

“Go out the office and make a left. Turn right at the corner and go down the hall. Make a right at the next corner and enter the kitchen in front of table.”

“Exit the room 0 and turn right, go to the end of the corridor and turn left, go straight to the end of the corridor and turn left again. After passing bookshelf on your left and table on your right, Enter the kitchen on your right.”

For both routes, the proposed model was able to predict the correct sequence of navigation behaviors. This result suggests that the model is indeed using the input instructions and is not just approximating shortest paths in the behavioral graph. Other examples on the prediction of sub-obtimal paths are described in the Appendix.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-1c8062ffce9c07d7f6b6cf14d37d98013bf639045fe583bf29fb8a2fa843416d

Passage ID: `qasper-passage-v1-1c8062ffce9c07d7f6b6cf14d37d98013bf639045fe583bf29fb8a2fa843416d`; retrieval score: 4.240718951147089.

Word count: 400.

```text
Table TABREF28 shows the performance of the models considered in our evaluation on both test sets. The next two sections discuss the results in detail.

First, we can observe that the final model “Ours with Mask and Ordered Triplets” outperforms the Baseline and Ablation models on all metrics in previously seen environments. The difference in performance is particularly evident for the Exact Match and Goal Match metrics, with our model increasing accuracy by 35% and 25% in comparison to the Baseline and Ablation models, respectively. These results suggest that providing the behavioral navigation graph to the model and allowing it to process this information as a knowledge base in an end-to-end fashion is beneficial.

We can also observe from Table TABREF28 that the masking function of Eq. ( EQREF12 ) tends to increase performance in the Test-Repeated Set by constraining the output sequence to a valid set of navigation behaviors. For the Ablation model, using the masking function leads to about INLINEFORM0 increase in EM and GM accuracy. For the proposed model (with or without reordering the graph triplets), the increase in accuracy is around INLINEFORM1 . Note that the impact of the masking function is less evident in terms of the F1 score because this metric considers if a predicted behavior exists in the ground truth navigation plan, irrespective of its specific position in the output sequence.

The results in the last four rows of Table TABREF28 suggest that ordering the graph triplets can facilitate predicting correct navigation plans in previously seen environments. Providing the triplets that surround the starting location of the robot first to the model leads to a boost of INLINEFORM0 in EM and GM performance. The rearrangement of the graph triplets also helps to reduce ED and increase F1.

Lastly, it is worth noting that our proposed model (last row of Table TABREF28 ) outperforms all other models in previously seen environments. In particular, we obtain over INLINEFORM0 increase in EM and GM between our model and the next best two models.

The previous section evaluated model performance on new instructions (and corresponding navigation plans) for environments that were previously seen at training time. Here, we examine whether the trained models succeed on environments that are completely new.

The evaluation on the Test-New Set helps understand the generalization capabilities of the models under consideration. This experiment is more challenging than the one in the previous
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1810.00663:10:1` | full | 0:572 |
| `1810.00663:10:4` | full | 0:254 |

#### Rank 5: qasper-passage-v1-ba9d5e74f01911ffee320a2019a1ac9512f85e41a41871b76b45099afcb6d735

Passage ID: `qasper-passage-v1-ba9d5e74f01911ffee320a2019a1ac9512f85e41a41871b76b45099afcb6d735`; retrieval score: 4.077713019713112.

Word count: 400.

```text
We leverage recent advances in deep learning to translate natural language instructions to a sequence of navigation behaviors in an end-to-end fashion. Our proposed model builds on the sequence-to-sequence translation model of BIBREF23 , which computes a soft-alignment between a source sequence (natural language instructions in our case) and the corresponding target sequence (navigation behaviors).

As one of our main contributions, we augment the neural machine translation approach of BIBREF23 to take as input not only natural language instructions, but also the corresponding behavioral navigation graph INLINEFORM0 of the environment where navigation should take place. Specifically, at each step, the graph INLINEFORM1 operates as a knowledge base that the model can access to obtain information about path connectivity, facilitating the grounding of navigation commands.

Figure FIGREF8 shows the structure of the proposed model for interpreting navigation instructions. The model consists of six layers:

Embed layer: The model first encodes each word and symbol in the input sequences INLINEFORM0 and INLINEFORM1 into fixed-length representations. The instructions INLINEFORM2 are embedded into a 100-dimensional pre-trained GloVe vector BIBREF24 . Each of the triplet components, INLINEFORM3 , INLINEFORM4 , and INLINEFORM5 of the graph INLINEFORM6 , are one-hot encoded into vectors of dimensionality INLINEFORM7 , where INLINEFORM8 and INLINEFORM9 are the number of nodes and edges in INLINEFORM10 , respectively.

Encoder layer: The model then uses two bidirectional Gated Recurrent Units (GRUs) BIBREF25 to independently process the information from INLINEFORM0 and INLINEFORM1 , and incorporate contextual cues from the surrounding embeddings in each sequence. The outputs of the encoder layer are the matrix INLINEFORM2 for the navigational commands and the matrix INLINEFORM3 for the behavioral graph, where INLINEFORM4 is the hidden size of each GRU, INLINEFORM5 is the number of words in the instruction INLINEFORM6 , and INLINEFORM7 is the number of triplets in the graph INLINEFORM8 .

Attention layer: Matrices INLINEFORM0 and INLINEFORM1 generated by the encoder layer are combined using an attention mechanism. We use one-way attention because the graph contains information about the whole environment, while the instruction has (potentially incomplete) local information about the route of interest. The use of attention provides our model with a two-step strategy to interpret commands. This resembles the way people find paths on a map: first, relevant parts on the map are selected according to their affinity to each of the words in the input instruction (attention layer); second, the selected parts are connected
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1808.

Fully covered answer annotations: a6c1cfab37b756275380368b1d9f8cdb8929f57e.

Missing evidence by answer annotation:

```text
{
  "a6c1cfab37b756275380368b1d9f8cdb8929f57e": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: b27f7993b1fe7804c5660d1a33655e424cea8d10

### Question ID and text

Question ID: `b27f7993b1fe7804c5660d1a33655e424cea8d10`; paper ID: `1902.06843`.

```text
What is the source of the visual data? 
```

### Answers

#### Answer: 06fbe4ab4db9860966cc6a49627d3554a01ee590

```text
{"evidence": ["The recent advancements in deep neural networks, specifically for image analysis task, can lead to determining demographic features such as age and gender BIBREF13 . We show that by determining and integrating heterogeneous set of features from different modalities – aesthetic features from posted images (colorfulness, hue variance, sharpness, brightness, blurriness, naturalness), choice of profile picture (for gender, age, and facial expression), the screen name, the language features from both textual content and profile's description (n-gram, emotion, sentiment), and finally sociability from ego-network, and user engagement – we can reliably detect likely depressed individuals in a data set of 8,770 human-annotated Twitter users."], "extractive_spans": [], "free_form_answer": "Profile pictures from the Twitter users' profiles.", "highlighted_evidence": ["We show that by determining and integrating heterogeneous set of features from different modalities – aesthetic features from posted images (colorfulness, hue variance, sharpness, brightness, blurriness, naturalness), choice of profile picture (for gender, age, and facial expression), the screen name, the language features from both textual content and profile's description (n-gram, emotion, sentiment), and finally sociability from ego-network, and user engagement – we can reliably detect likely depressed individuals in a data set of 8,770 human-annotated Twitter users."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1902.06843:1:5`

```text
The recent advancements in deep neural networks, specifically for image analysis task, can lead to determining demographic features such as age and gender BIBREF13 . We show that by determining and integrating heterogeneous set of features from different modalities – aesthetic features from posted images (colorfulness, hue variance, sharpness, brightness, blurriness, naturalness), choice of profile picture (for gender, age, and facial expression), the screen name, the language features from both textual content and profile's description (n-gram, emotion, sentiment), and finally sociability from ego-network, and user engagement – we can reliably detect likely depressed individuals in a data set of 8,770 human-annotated Twitter users.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-ca2af40a6a0c77a5182bb8bfe29e6963d8b018aef560da573011b5df8fa5743a

Passage ID: `qasper-passage-v1-ca2af40a6a0c77a5182bb8bfe29e6963d8b018aef560da573011b5df8fa5743a`; retrieval score: 7.343434239963459.

Word count: 400.

```text
We leverage both the visual and textual content for predicting age and gender.

Prediction with Textual Content:

We employ BIBREF73 's weighted lexicon of terms that uses the dataset of 75,394 Facebook users who shared their status, age and gender. The predictive power of this lexica was evaluated on Twitter, blog, and Facebook, showing promising results BIBREF73 . Utilizing these two weighted lexicon of terms, we are predicting the demographic information (age or gender) of INLINEFORM0 (denoted by INLINEFORM1 ) using following equation: INLINEFORM2

where INLINEFORM0 is the lexicon weight of the term, and INLINEFORM1 represents the frequency of the term in the user generated INLINEFORM2 , and INLINEFORM3 measures total word count in INLINEFORM4 . As our data is biased toward young people, we report age prediction performance for each age group separately (Table TABREF42 ). Moreover, to measure the average accuracy of this model, we build a balanced dataset (keeping all the users above 23 -416 users), and then randomly sampling the same number of users from the age ranges (11,19] and (19,23]. The average accuracy of this model is 0.63 for depressed users and 0.64 for control class. Table TABREF44 illustrates the performance of gender prediction for each class. The average accuracy is 0.82 on INLINEFORM5 ground-truth dataset.

Prediction with Visual Imagery:

Inspired by BIBREF56 's approach for facial landmark localization, we use their pretrained CNN consisting of convolutional layers, including unshared and fully-connected layers, to predict gender and age from both the profile and shared images. We evaluate the performance for gender and age prediction task on INLINEFORM0 and INLINEFORM1 respectively as shown in Table TABREF42 and Table TABREF44 .

Demographic Prediction Analysis:

We delve deeper into the benefits and drawbacks of each data modality for demographic information prediction. This is crucial as the differences between language cues between age groups above age 35 tend to become smaller (see Figure FIGREF39 -A,B,C) and making the prediction harder for older people BIBREF74 . In this case, the other data modality (e.g., visual content) can play integral role as a complementary source for age inference. For gender prediction (see Table TABREF44 ), on average, the profile image-based predictor provides a more accurate prediction for both the depressed and control class (0.92 and 0.90) compared to content-based predictor (0.82). For age prediction (see Table TABREF42 ), textual content-based predictor (on average 0.60) outperforms both of the visual-based predictors (on
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-806041d232790bec8b73b261c4950aebe69dec694480aece144c7d3f05a53158

Passage ID: `qasper-passage-v1-806041d232790bec8b73b261c4950aebe69dec694480aece144c7d3f05a53158`; retrieval score: 6.056120562811685.

Word count: 400.

```text
We now provide an in-depth analysis of visual and textual content of vulnerable users.

Visual Content Analysis: We show that the visual content in images from posts as well as profiles provide valuable psychological cues for understanding a user's depression status. Profile/posted images can surface self-stigmatization BIBREF53 . Additionally, as opposed to typical computer vision framework for object recognition that often relies on thousands of predetermined low-level features, what matters more for assessing user's online behavior is the emotions reflected in facial expressions BIBREF54 , attributes contributing to the computational aesthetics BIBREF55 , and sentimental quotes they may subscribe to (Figure FIGREF15 ) BIBREF8 .

Facial Presence:

For capturing facial presence, we rely on BIBREF56 's approach that uses multilevel convolutional coarse-to-fine network cascade to tackle facial landmark localization. We identify facial presentation, emotion from facial expression, and demographic features from profile/posted images . Table TABREF21 illustrates facial presentation differences in both profile and posted images (media) for depressed and control users in INLINEFORM0 . With control class showing significantly higher in both profile and media (8%, 9% respectively) compared to that for the depressed class. In contrast with age and gender disclosure, vulnerable users are less likely to disclose their facial identity, possibly due to lack of confidence or fear of stigma.

Facial Expression:

Following BIBREF8 's approach, we adopt Ekman's model of six emotions: anger, disgust, fear, joy, sadness and surprise, and use the Face++ API to automatically capture them from the shared images. Positive emotions are joy and surprise, and negative emotions are anger, disgust, fear, and sadness. In general, for each user u in INLINEFORM0 , we process profile/shared images for both the depressed and the control groups with at least one face from the shared images (Table TABREF23 ). For the photos that contain multiple faces, we measure the average emotion.

Figure FIGREF27 illustrates the inter-correlation of these features. Additionally, we observe that emotions gleaned from facial expressions correlated with emotional signals captured from textual content utilizing LIWC. This indicates visual imagery can be harnessed as a complementary channel for measuring online emotional signals.

General Image Features:

The importance of interpretable computational aesthetic features for studying users' online behavior has been highlighted by several efforts BIBREF55 , BIBREF8 , BIBREF57 . Color, as a pillar of the human vision system, has a strong association with conceptual ideas like emotion BIBREF58 , BIBREF59 . We measured
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-6443e1d405739830050e4c800afcafd36dc0ba1693dfcbde068582556eccf679

Passage ID: `qasper-passage-v1-6443e1d405739830050e4c800afcafd36dc0ba1693dfcbde068582556eccf679`; retrieval score: 4.628028584278453.

Word count: 400.

```text
We use the above findings for predicting depressive behavior. Our model exploits early fusion BIBREF32 technique in feature space and requires modeling each user INLINEFORM0 in INLINEFORM1 as vector concatenation of individual modality features. As opposed to computationally expensive late fusion scheme where each modality requires a separate supervised modeling, this model reduces the learning effort and shows promising results BIBREF75 . To develop a generalizable model that avoids overfitting, we perform feature selection using statistical tests and all relevant ensemble learning models. It adds randomness to the data by creating shuffled copies of all features (shadow feature), and then trains Random Forest classifier on the extended data. Iteratively, it checks whether the actual feature has a higher Z-score than its shadow feature (See Algorithm SECREF6 and Figure FIGREF45 ) BIBREF76 .

Main each Feature INLINEFORM0 INLINEFORM1

RndForrest( INLINEFORM0 ) Calculate Imp INLINEFORM1 INLINEFORM2 Generate next hypothesis , INLINEFORM3 Once all hypothesis generated Perform Statistical Test INLINEFORM4 //Binomial Distribution INLINEFORM5 Feature is important Feature is important

Ensemble Feature Selection

Next, we adopt an ensemble learning method that integrates the predictive power of multiple learners with two main advantages; its interpretability with respect to the contributions of each feature and its high predictive power. For prediction we have INLINEFORM0 where INLINEFORM1 is a weak learner and INLINEFORM2 denotes the final prediction.

In particular, we optimize the loss function: INLINEFORM0 where INLINEFORM1 incorporates INLINEFORM2 and INLINEFORM3 regularization. In each iteration, the new INLINEFORM4 is obtained by fitting weak learner to the negative gradient of loss function. Particularly, by estimating the loss function with Taylor expansion : INLINEFORM5 where its first expression is constant, the second and the third expressions are first ( INLINEFORM6 ) and second order derivatives ( INLINEFORM7 ) of the loss. INLINEFORM8

For exploring the weak learners, assume INLINEFORM0 has k leaf nodes, INLINEFORM1 be subset of users from INLINEFORM2 belongs to the node INLINEFORM3 , and INLINEFORM4 denotes the prediction for node INLINEFORM5 . Then, for each user INLINEFORM6 belonging to INLINEFORM7 , INLINEFORM8 and INLINEFORM9 INLINEFORM10

Next, for each leaf node INLINEFORM0 , deriving w.r.t INLINEFORM1 : INLINEFORM2

and by substituting weights: INLINEFORM0

which represents the loss for fixed weak learners with INLINEFORM0 nodes. The trees are built sequentially such that each subsequent tree aims to reduce the errors of its predecessor tree. Although, the weak learners have high bias, the ensemble model produces a strong learner
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-5298ec4b7b6fb7cfe81680b99868549c796956becc234a846715717826408ca6

Passage ID: `qasper-passage-v1-5298ec4b7b6fb7cfe81680b99868549c796956becc234a846715717826408ca6`; retrieval score: 4.462267605253722.

Word count: 384.

```text
for fixed weak learners with INLINEFORM0 nodes. The trees are built sequentially such that each subsequent tree aims to reduce the errors of its predecessor tree. Although, the weak learners have high bias, the ensemble model produces a strong learner that effectively integrate the weak learners by reducing bias and variance (the ultimate goal of supervised models) BIBREF77 . Table TABREF48 illustrates our multimodal framework outperform the baselines for identifying depressed users in terms of average specificity, sensitivity, F-Measure, and accuracy in 10-fold cross-validation setting on INLINEFORM1 dataset. Figure FIGREF47 shows how the likelihood of being classified into the depressed class varies with each feature addition to the model for a sample user in the dataset. The prediction bar (the black bar) shows that the log-odds of prediction is 0.31, that is, the likelihood of this person being a depressed user is 57% (1 / (1 + exp(-0.3))). The figure also sheds light on the impact of each contributing feature. The waterfall charts represent how the probability of being depressed changes with the addition of each feature variable. For instance, the "Analytic thinking" of this user is considered high 48.43 (Median:36.95, Mean: 40.18) and this decreases the chance of this person being classified into the depressed group by the log-odds of -1.41. Depressed users have significantly lower "Analytic thinking" score compared to control class. Moreover, the 40.46 "Clout" score is a low value (Median: 62.22, Mean: 57.17) and it decreases the chance of being classified as depressed. With respect to the visual features, for instance, the mean and the median of 'shared_colorfulness' is 112.03 and 113 respectively. The value of 136.71 would be high; thus, it decreases the chance of being depressed for this specific user by log-odds of -0.54. Moreover, the 'profile_naturalness' of 0.46 is considered high compared to 0.36 as the mean for the depressed class which justifies pull down of the log-odds by INLINEFORM2 . For network features, for instance, 'two_hop_neighborhood' for depressed users (Mean : 84) are less than that of control users (Mean: 154), and is reflected in pulling down the log-odds by -0.27.

Baselines:

To test the efficacy of our multi-modal framework for detecting depressed users, we compare it against existing content, content-network, and image-based models (based on the aforementioned general image feature, facial presence, and facial expressions.)
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-2844df83aa5cd341937c54314255fcc8099ab135fbb5ba4fbb6d401bd154136f

Passage ID: `qasper-passage-v1-2844df83aa5cd341937c54314255fcc8099ab135fbb5ba4fbb6d401bd154136f`; retrieval score: 4.4233278403365235.

Word count: 400.

```text
). Overall, vulnerable younger users are not logical thinkers based on their relative analytical score and cognitive processing ability.

Authenticity:

Authenticity measures the degree of honesty. Authenticity is often assessed by measuring present tense verbs, 1st person singular pronouns (I, me, my), and by examining the linguistic manifestations of false stories BIBREF70 . Liars use fewer self-references and fewer complex words. Psychologists often see a child's first successfull lie as a mental growth. There is a decreasing trend of the Authenticity with aging (see Figure FIGREF39 -B.) Authenticity for depressed youngsters is strikingly higher than their control peers. It decreases with age (Figure FIGREF39 -B.)

Clout:

People with high clout speak more confidently and with certainty, employing more social words with fewer negations (e.g., no, not) and swear words. In general, midlife is relatively stable w.r.t. relationships and work. A recent study shows that age 60 to be best for self-esteem BIBREF71 as people take on managerial roles at work and maintain a satisfying relationship with their spouse. We see the same pattern in our data (see Figure FIGREF39 -C and Table TABREF40 ). Unsurprisingly, lack of confidence (the 6th PHQ-9 symptom) is a distinguishable characteristic of vulnerable users, leading to their lower clout scores, especially among depressed users before middle age (34 years old).

Self-references:

First person singular words are often seen as indicating interpersonal involvement and their high usage is associated with negative affective states implying nervousness and depression BIBREF66 . Consistent with prior studies, frequency of first person singular for depressed people is significantly higher compared to that of control class. Similarly to BIBREF66 , youngsters tend to use more first-person (e.g. I) and second person singular (e.g. you) pronouns (Figure FIGREF39 -G).

Informal Language Markers; Swear, Netspeak:

Several studies highlighted the use of profanity by young adults has significantly increased over the last decade BIBREF72 . We observed the same pattern in both the depressed and the control classes (Table TABREF40 ), although it's rate is higher for depressed users BIBREF1 . Psychologists have also shown that swearing can indicate that an individual is not a fragmented member of a society. Depressed youngsters, showing higher rate of interpersonal involvement and relationships, have a higher rate of cursing (Figure FIGREF39 -E). Also, Netspeak lexicon measures the frequency of terms such as lol and thx.

Sexual, Body:

Sexual lexicon contains terms like "horny", "love" and "incest", and body
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1984.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "06fbe4ab4db9860966cc6a49627d3554a01ee590": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1902.06843:1:5": [
        [
          0,
          742
        ]
      ]
    }
  }
}
```

## Question: 0d6d5b6c00551dd0d2519f117ea81d1e9e8785ec

### Question ID and text

Question ID: `0d6d5b6c00551dd0d2519f117ea81d1e9e8785ec`; paper ID: `1903.03467`.

```text
Which neural machine translation system is used?
```

### Answers

#### Answer: 7a7f39d12b1d910bc0ae826f3ee2a957141aecf3

```text
{"evidence": ["To demonstrate our method in a black-box setting, we focus our experiments on Google's machine translation system (GMT), accessed through its Cloud API. To test the method on real-world sentences, we consider a monologue from the stand-up comedy show “Sarah Silverman: A Speck of Dust”. The monologue consists of 1,244 English sentences, all by a female speaker conveyed to a plural, gender-neutral audience. Our parallel corpora consists of the 1,244 English sentences from the transcript, and their corresponding Hebrew translations based on the Hebrew subtitles. We translate the monologue one sentence at a time through the Google Cloud API. Eyeballing the results suggest that most of the translations use the incorrect, but default, masculine and singular forms for the speaker and the audience, respectively. We expect that by adding the relevant condition of “female speaking to an audience” we will get better translations, affecting both the gender of the speaker and the number of the audience."], "extractive_spans": ["Google's machine translation system (GMT)"], "free_form_answer": "", "highlighted_evidence": ["To demonstrate our method in a black-box setting, we focus our experiments on Google's machine translation system (GMT), accessed through its Cloud API."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1903.03467:3:0`

```text
To demonstrate our method in a black-box setting, we focus our experiments on Google's machine translation system (GMT), accessed through its Cloud API. To test the method on real-world sentences, we consider a monologue from the stand-up comedy show “Sarah Silverman: A Speck of Dust”. The monologue consists of 1,244 English sentences, all by a female speaker conveyed to a plural, gender-neutral audience. Our parallel corpora consists of the 1,244 English sentences from the transcript, and their corresponding Hebrew translations based on the Hebrew subtitles. We translate the monologue one sentence at a time through the Google Cloud API. Eyeballing the results suggest that most of the translations use the incorrect, but default, masculine and singular forms for the speaker and the audience, respectively. We expect that by adding the relevant condition of “female speaking to an audience” we will get better translations, affecting both the gender of the speaker and the number of the audience.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-95625525737236834b150b845c7ca0439fe010706116b7d57ec5ec3b4fa10c0a

Passage ID: `qasper-passage-v1-95625525737236834b150b845c7ca0439fe010706116b7d57ec5ec3b4fa10c0a`; retrieval score: 4.126861005711247.

Word count: 177.

```text
E17-1101 showed that given input with author traits like gender, it is possible to retain those traits in Statistical Machine Translation (SMT) models. W17-4727 showed that incorporating morphological analysis in the decoder improves NMT performance for morphologically rich languages. burlot:hal-01618387 presented a new protocol for evaluating the morphological competence of MT systems, indicating that current translation systems only manage to capture some morphological phenomena correctly. Regarding the application of constraints in NMT, N16-1005 presented a method for controlling the politeness level in the generated output. DBLP:journals/corr/FiclerG17aa showed how to guide a neural text generation system towards style and content parameters like the level of professionalism, subjective/objective, sentiment and others. W17-4811 showed that incorporating more context when translating subtitles can improve the coherence of the generated translations. Most closely to our work, vanmassenhove-hardmeier-way:2018:EMNLP also addressed the missing gender information by training proprietary models with a gender-indicating-prefix. We differ from this work by treating the problem in a black-box manner, and by addressing additional information like the number of the speaker and the gender and number of the audience.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-b87ed84d86b47a6c608053bcbb8d5410b4c0ec5b070a7053a7dc77e35f9dbaa0

Passage ID: `qasper-passage-v1-b87ed84d86b47a6c608053bcbb8d5410b4c0ec5b070a7053a7dc77e35f9dbaa0`; retrieval score: 2.7710577626068056.

Word count: 400.

```text
A common way for marking information about gender, number, and case in language is morphology, or the structure of a given word in the language. However, different languages mark such information in different ways – for example, in some languages gender may be marked on the head word of a syntactic dependency relation, while in other languages it is marked on the dependent, on both, or on none of them BIBREF0 . This morphological diversity creates a challenge for machine translation, as there are ambiguous cases where more than one correct translation exists for the same source sentence. For example, while the English sentence “I love language” is ambiguous with respect to the gender of the speaker, Hebrew marks verbs for the gender of their subject and does not allow gender-neutral translation. This allows two possible Hebrew translations – one in a masculine and the other in a feminine form. As a consequence, a sentence-level translator (either human or machine) must commit to the gender of the speaker, adding information that is not present in the source. Without additional context, this choice must be done arbitrarily by relying on language conventions, world knowledge or statistical (stereotypical) knowledge.

Indeed, the English sentence “I work as a doctor” is translated into Hebrew by Google Translate using the masculine verb form oved, indicating a male speaker, while “I work as a nurse” is translated with the feminine form ovedet, indicating a female speaker (verified on March 2019). While this is still an issue, there have been recent efforts to reduce it for specific language pairs.

We present a simple black-box method to influence the interpretation chosen by an NMT system in these ambiguous cases. More concretely, we construct pre-defined textual hints about the gender and number of the speaker and the audience (the interlocutors), which we concatenate to a given input sentence that we would like to translate accordingly. We then show that a black-box NMT system makes the desired morphological decisions according to the given hint, even when no other evidence is available on the source side. While adding those hints results in additional text on the target side, we show that it is simple to remove, leaving only the desired translation.

Our method is appealing as it only requires simple pre-and-post processing of the inputs and outputs, without considering the system internals, or requiring specific annotated data and training procedure as
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-051d84ea637d2ee6a23ef54041881a38e03881421599aea409ec219dc6fac714

Passage ID: `qasper-passage-v1-051d84ea637d2ee6a23ef54041881a38e03881421599aea409ec219dc6fac714`; retrieval score: 2.585457908552495.

Word count: 102.

```text
Closely related to our work, vanmassenhove-hardmeier-way:2018:EMNLP proposed a method and an English-French test set to evaluate gender-aware translation, based on the Europarl corpus BIBREF7 . We evaluate our method (using Google Translate and the given prefixes) on their test set to see whether it is applicable to another language pair and domain. Table shows the results of our approach vs. their published results and the Google Translate baseline. As may be expected, Google Translate outperforms their system as it is trained on a different corpus and may use more complex machine translation models. Using our method improves the BLEU score even further.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-61a0ff4236bb06e08d7aaa8250373f35df86b24a7edfacd98b249281add45f3b

Passage ID: `qasper-passage-v1-61a0ff4236bb06e08d7aaa8250373f35df86b24a7edfacd98b249281add45f3b`; retrieval score: 2.3648547191030946.

Word count: 105.

```text
it is simple to remove, leaving only the desired translation.

Our method is appealing as it only requires simple pre-and-post processing of the inputs and outputs, without considering the system internals, or requiring specific annotated data and training procedure as in previous work BIBREF1 . We show that in spite of its simplicity, it is effective in resolving many of the ambiguities and improves the translation quality in up to 2.3 BLEU when given the correct hints, which may be inferred from text metadata or other sources. Finally, we perform a fine-grained syntactic analysis of the translations generated using our method which shows its effectiveness.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-2c64fcf4f2964ffeb2c36a35ee7887f13745e8f8970d5d32cd6bcef290363507

Passage ID: `qasper-passage-v1-2c64fcf4f2964ffeb2c36a35ee7887f13745e8f8970d5d32cd6bcef290363507`; retrieval score: 1.8136748729596595.

Word count: 353.

```text
Our goal is to supply an NMT system with knowledge regarding the speaker and interlocutor of first-person sentences, in order to produce the desired target-side morphology when the information is not available in the source sentence. The approach we take in the current work is that of black-box injection, in which we attempt to inject knowledge to the input in order to influence the output of a trained NMT system, without having access to its internals or its training procedure as proposed by vanmassenhove-hardmeier-way:2018:EMNLP.

We are motivated by recent work by BIBREF4 who showed that NMT systems learn to track coreference chains when presented with sufficient discourse context. We conjecture that there are enough sentence-internal pronominal coreference chains appearing in the training data of large-scale NMT systems, such that state-of-the-art NMT systems can and do track sentence-internal coreference. We devise a wrapper method to make use of this coreference tracking ability by introducing artificial antecedents that unambiguously convey the desired gender and number properties of the speaker and audience.

More concretely, a sentence such as “I love you” is ambiguous with respect to the gender of the speaker and the gender and number of the audience. However, sentences such as “I love you, she told him” are unambiguous given the coreference groups {I, she} and {you, him} which determine I to be feminine singular and you to be masculine singular. We can thus inject the desired information by prefixing a sentence with short generic sentence fragment such as “She told him:” or “She told them that”, relying on the NMT system's coreference tracking abilities to trigger the correctly marked translation, and then remove the redundant translated prefix from the generated target sentence. We observed that using a parataxis construction (i.e. “she said to him:”) almost exclusively results in target-side parataxis as well (in 99.8% of our examples), making it easy to identify and strip the translated version from the target side. Moreover, because the parataxis construction is grammatically isolated from the rest of the sentence, it can be stripped without requiring additional changes or modification to the rest of the sentence, ensuring grammaticality.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1137.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "7a7f39d12b1d910bc0ae826f3ee2a957141aecf3": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1903.03467:3:0": [
        [
          0,
          1005
        ]
      ]
    }
  }
}
```

## Question: 0cd90e5b79ea426ada0203177c28812a7fc86be5

### Question ID and text

Question ID: `0cd90e5b79ea426ada0203177c28812a7fc86be5`; paper ID: `1701.06538`.

```text
How is the correct number of experts to use decided?
```

### Answers

#### Answer: 79c6e303c769cf6b075f42fc27820b4a2f8ee791

```text
{"evidence": ["Each expert in the MoE layer is a feed forward network with one ReLU-activated hidden layer of size 1024 and an output layer of size 512. Thus, each expert contains INLINEFORM0 parameters. The output of the MoE layer is passed through a sigmoid function before dropout. We varied the number of experts between models, using ordinary MoE layers with 4, 32 and 256 experts and hierarchical MoE layers with 256, 1024 and 4096 experts. We call the resulting models MoE-4, MoE-32, MoE-256, MoE-256-h, MoE-1024-h and MoE-4096-h. For the hierarchical MoE layers, the first level branching factor was 16, corresponding to the number of GPUs in our cluster. We use Noisy-Top-K Gating (see Section UID14 ) with INLINEFORM1 for the ordinary MoE layers and INLINEFORM2 at each level of the hierarchical MoE layers. Thus, each example is processed by exactly 4 experts for a total of 4M ops/timestep. The two LSTM layers contribute 2M ops/timestep each for the desired total of 8M."], "extractive_spans": ["varied the number of experts between models"], "free_form_answer": "", "highlighted_evidence": ["We varied the number of experts between models, using ordinary MoE layers with 4, 32 and 256 experts and hierarchical MoE layers with 256, 1024 and 4096 experts."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1701.06538:16:1`

```text
Each expert in the MoE layer is a feed forward network with one ReLU-activated hidden layer of size 1024 and an output layer of size 512. Thus, each expert contains INLINEFORM0 parameters. The output of the MoE layer is passed through a sigmoid function before dropout. We varied the number of experts between models, using ordinary MoE layers with 4, 32 and 256 experts and hierarchical MoE layers with 256, 1024 and 4096 experts. We call the resulting models MoE-4, MoE-32, MoE-256, MoE-256-h, MoE-1024-h and MoE-4096-h. For the hierarchical MoE layers, the first level branching factor was 16, corresponding to the number of GPUs in our cluster. We use Noisy-Top-K Gating (see Section UID14 ) with INLINEFORM1 for the ordinary MoE layers and INLINEFORM2 at each level of the hierarchical MoE layers. Thus, each example is processed by exactly 4 experts for a total of 4M ops/timestep. The two LSTM layers contribute 2M ops/timestep each for the desired total of 8M.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-a801dfb6e1cc5b828832919fb41447201614ae1067b47b4b1e7bde1c09559f69

Passage ID: `qasper-passage-v1-a801dfb6e1cc5b828832919fb41447201614ae1067b47b4b1e7bde1c09559f69`; retrieval score: 6.645599730105681.

Word count: 150.

```text
Another major performance concern in distributed computing is network bandwidth. Since the experts are stationary (see above) and the number of gating parameters is small, most of the communication involves sending the inputs and outputs of the experts across the network. To maintain computational efficiency, the ratio of an expert's computation to the size of its input and output must exceed the ratio of computational to network capacity of the computing device. For GPUs, this may be thousands to one. In our experiments, we use experts with one hidden layer containing thousands of RELU-activated units. Since the weight matrices in the expert have sizes INLINEFORM0 _ INLINEFORM1 _ INLINEFORM2 and INLINEFORM3 _ INLINEFORM4 _ INLINEFORM5 , the ratio of computation to input and output is equal to the size of the hidden layer. Conveniently, we can increase computational efficiency simply by using a larger hidden layer, or more hidden layers.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-023091d4cb9fc99be63d75b4547eab0bd61f3787bb90a9cd096f1826830ae0af

Passage ID: `qasper-passage-v1-023091d4cb9fc99be63d75b4547eab0bd61f3787bb90a9cd096f1826830ae0af`; retrieval score: 6.558914749712592.

Word count: 400.

```text
On modern CPUs and GPUs, large batch sizes are necessary for computational efficiency, so as to amortize the overhead of parameter loads and updates. If the gating network chooses INLINEFORM0 out of INLINEFORM1 experts for each example, then for a batch of INLINEFORM2 examples, each expert receives a much smaller batch of approximately INLINEFORM3 examples. This causes a naive MoE implementation to become very inefficient as the number of experts increases. The solution to this shrinking batch problem is to make the original batch size as large as possible. However, batch size tends to be limited by the memory necessary to store activations between the forwards and backwards passes. We propose the following techniques for increasing the batch size:

In a conventional distributed training setting, multiple copies of the model on different devices asynchronously process distinct batches of data, and parameters are synchronized through a set of parameter servers. In our technique, these different batches run synchronously so that they can be combined for the MoE layer. We distribute the standard layers of the model and the gating network according to conventional data-parallel schemes, but keep only one shared copy of each expert. Each expert in the MoE layer receives a combined batch consisting of the relevant examples from all of the data-parallel input batches. The same set of devices function as data-parallel replicas (for the standard layers and the gating networks) and as model-parallel shards (each hosting a subset of the experts). If the model is distributed over INLINEFORM0 devices, and each device processes a batch of size INLINEFORM1 , each expert receives a batch of approximately INLINEFORM2 examples. Thus, we achieve a factor of INLINEFORM3 improvement in expert batch size.

In the case of a hierarchical MoE (Section SECREF60 ), the primary gating network employs data parallelism, and the secondary MoEs employ model parallelism. Each secondary MoE resides on one device.

This technique allows us to increase the number of experts (and hence the number of parameters) by proportionally increasing the number of devices in the training cluster. The total batch size increases, keeping the batch size per expert constant. The memory and bandwidth requirements per device also remain constant, as do the step times, as does the amount of time necessary to process a number of training examples equal to the number of parameters in the model. It is our goal to train a trillion-parameter model on
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-7607f9de78c42ca530889bd68485c460d790109ee88a8531933044405759b641

Passage ID: `qasper-passage-v1-7607f9de78c42ca530889bd68485c460d790109ee88a8531933044405759b641`; retrieval score: 6.510132986825794.

Word count: 159.

```text
If the number of experts is very large, we can reduce the branching factor by using a two-level hierarchical MoE. In a hierarchical MoE, a primary gating network chooses a sparse weighted combination of “experts", each of which is itself a secondary mixture-of-experts with its own gating network. If the hierarchical MoE consists of INLINEFORM0 groups of INLINEFORM1 experts each, we denote the primary gating network by INLINEFORM2 , the secondary gating networks by INLINEFORM3 , and the expert networks by INLINEFORM4 . The output of the MoE is given by: DISPLAYFORM0

Our metrics of expert utilization change to the following: DISPLAYFORM0 DISPLAYFORM1

INLINEFORM0 and INLINEFORM1 deonte the INLINEFORM2 functions for the primary gating network and INLINEFORM3 secondary gating network respectively. INLINEFORM4 denotes the subset of INLINEFORM5 for which INLINEFORM6 .

It would seem simpler to let INLINEFORM0 , but this would not have a gradient with respect to the primary gating network, so we use the formulation above.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-fa017936492ce203403f7cdc4816d08d45efff5eebea438544842f285c3989bc

Passage ID: `qasper-passage-v1-fa017936492ce203403f7cdc4816d08d45efff5eebea438544842f285c3989bc`; retrieval score: 6.499960158417993.

Word count: 400.

```text
Our model consists of five layers: a word embedding layer, a recurrent Long Short-Term Memory (LSTM) layer BIBREF15 , BIBREF29 , a MoE layer, a second LSTM layer, and a softmax layer. The dimensionality of the embedding layer, the number of units in each LSTM layer, and the input and output dimensionality of the MoE layer are all equal to 512. For every layer other than the softmax, we apply drouput BIBREF43 to the layer output, dropping each activation with probability INLINEFORM0 , otherwise dividing by INLINEFORM1 . After dropout, the output of the previous layer is added to the layer output. This residual connection encourages gradient flow BIBREF37 .

Each expert in the MoE layer is a feed forward network with one ReLU-activated hidden layer of size 1024 and an output layer of size 512. Thus, each expert contains INLINEFORM0 parameters. The output of the MoE layer is passed through a sigmoid function before dropout. We varied the number of experts between models, using ordinary MoE layers with 4, 32 and 256 experts and hierarchical MoE layers with 256, 1024 and 4096 experts. We call the resulting models MoE-4, MoE-32, MoE-256, MoE-256-h, MoE-1024-h and MoE-4096-h. For the hierarchical MoE layers, the first level branching factor was 16, corresponding to the number of GPUs in our cluster. We use Noisy-Top-K Gating (see Section UID14 ) with INLINEFORM1 for the ordinary MoE layers and INLINEFORM2 at each level of the hierarchical MoE layers. Thus, each example is processed by exactly 4 experts for a total of 4M ops/timestep. The two LSTM layers contribute 2M ops/timestep each for the desired total of 8M.

The MoE-4 model does not employ sparsity, since all 4 experts are always used. In addition, we trained four more computationally-matched baseline models with no sparsity:

MoE-1-Wide: The MoE layer consists of a single "expert" containing one ReLU-activated hidden layer of size 4096.

MoE-1-Deep: The MoE layer consists of a single "expert" containing four ReLU-activated hidden layers, each with size 1024.

4xLSTM-512: We replace the MoE layer with two additional 512-unit LSTM layers.

LSTM-2048-512: The model contains one 2048-unit LSTM layer (and no MoE). The output of the LSTM is projected down to 512 dimensions BIBREF41 . The next timestep of the LSTM receives the projected output. This is identical to one of the models published in BIBREF2 . We re-ran it to account for differences in training regimen,
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1701.06538:16:1` | full | 0:968 |

#### Rank 5: qasper-passage-v1-da7cd8858d71da4edd9805851f3908b284166a9cedf85a17b270c66027bc5709

Passage ID: `qasper-passage-v1-da7cd8858d71da4edd9805851f3908b284166a9cedf85a17b270c66027bc5709`; retrieval score: 6.498080843708186.

Word count: 300.

```text
The Mixture-of-Experts (MoE) layer consists of a set of INLINEFORM0 “expert networks" INLINEFORM1 , and a “gating network" INLINEFORM2 whose output is a sparse INLINEFORM3 -dimensional vector. Figure FIGREF8 shows an overview of the MoE module. The experts are themselves neural networks, each with their own parameters. Although in principle we only require that the experts accept the same sized inputs and produce the same-sized outputs, in our initial investigations in this paper, we restrict ourselves to the case where the models are feed-forward networks with identical architectures, but with separate parameters.

Let us denote by INLINEFORM0 and INLINEFORM1 the output of the gating network and the output of the INLINEFORM2 -th expert network for a given input INLINEFORM3 . The output INLINEFORM4 of the MoE module can be written as follows: DISPLAYFORM0

We save computation based on the sparsity of the output of INLINEFORM0 . Wherever INLINEFORM1 , we need not compute INLINEFORM2 . In our experiments, we have up to thousands of experts, but only need to evaluate a handful of them for every example. If the number of experts is very large, we can reduce the branching factor by using a two-level hierarchical MoE. In a hierarchical MoE, a primary gating network chooses a sparse weighted combination of “experts", each of which is itself a secondary mixture-of-experts with its own gating network. In the following we focus on ordinary MoEs. We provide more details on hierarchical MoEs in Appendix SECREF60 .

Our implementation is related to other models of conditional computation. A MoE whose experts are simple weight matrices is similar to the parameterized weight matrix proposed in BIBREF12 . A MoE whose experts have one hidden layer is similar to the block-wise dropout described in BIBREF13 , where the dropped-out layer is sandwiched between fully-activated layers.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1409.

Fully covered answer annotations: 79c6e303c769cf6b075f42fc27820b4a2f8ee791.

Missing evidence by answer annotation:

```text
{
  "79c6e303c769cf6b075f42fc27820b4a2f8ee791": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: 282aa4e160abfa7569de7d99b8d45cabee486ba4

### Question ID and text

Question ID: `282aa4e160abfa7569de7d99b8d45cabee486ba4`; paper ID: `1805.00760`.

```text
How do they determine the opinion summary?
```

### Answers

#### Answer: b3596aa57239b4bc334f9d6dbd92d867f46924fa

```text
{"evidence": ["As shown in Figure FIGREF3 , our model contains two key components, namely Truncated History-Attention (THA) and Selective Transformation Network (STN), for capturing aspect detection history and opinion summary respectively. THA and STN are built on two LSTMs that generate the initial word representations for the primary ATE task and the auxiliary opinion detection task respectively. THA is designed to integrate the information of aspect detection history into the current aspect feature to generate a new history-aware aspect representation. STN first calculates a new opinion representation conditioned on the current aspect candidate. Then, we employ a bi-linear attention network to calculate the opinion summary as the weighted sum of the new opinion representations, according to their associations with the current aspect representation. Finally, the history-aware aspect representation and the opinion summary are concatenated as features for aspect prediction of the current time step."], "extractive_spans": ["the weighted sum of the new opinion representations, according to their associations with the current aspect representation"], "free_form_answer": "", "highlighted_evidence": ["As shown in Figure FIGREF3 , our model contains two key components, namely Truncated History-Attention (THA) and Selective Transformation Network (STN), for capturing aspect detection history and opinion summary respectively. THA and STN are built on two LSTMs that generate the initial word representations for the primary ATE task and the auxiliary opinion detection task respectively. THA is designed to integrate the information of aspect detection history into the current aspect feature to generate a new history-aware aspect representation. STN first calculates a new opinion representation conditioned on the current aspect candidate. Then, we employ a bi-linear attention network to calculate the opinion summary as the weighted sum of the new opinion representations, according to their associations with the current aspect representation. Finally, the history-aware aspect representation and the opinion summary are concatenated as features for aspect prediction of the current time step."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1805.00760:2:0`

```text
As shown in Figure FIGREF3 , our model contains two key components, namely Truncated History-Attention (THA) and Selective Transformation Network (STN), for capturing aspect detection history and opinion summary respectively. THA and STN are built on two LSTMs that generate the initial word representations for the primary ATE task and the auxiliary opinion detection task respectively. THA is designed to integrate the information of aspect detection history into the current aspect feature to generate a new history-aware aspect representation. STN first calculates a new opinion representation conditioned on the current aspect candidate. Then, we employ a bi-linear attention network to calculate the opinion summary as the weighted sum of the new opinion representations, according to their associations with the current aspect representation. Finally, the history-aware aspect representation and the opinion summary are concatenated as features for aspect prediction of the current time step.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-3f27f6f59586d6129264a634c8918a48e174a84acfb3a9faf9903060b28203b4

Passage ID: `qasper-passage-v1-3f27f6f59586d6129264a634c8918a48e174a84acfb3a9faf9903060b28203b4`; retrieval score: 5.627250932782438.

Word count: 277.

```text
In Figure FIGREF41 , we visualize the opinion attention scores of the words in two example sentences with the candidate aspects “maitre-D” and “bathroom”. The scores in Figures FIGREF41 and FIGREF41 show that our full model captures the related opinion words very accurately with significantly larger scores, i.e. “incredibly”, “unwelcoming” and “arrogant” for “maitre-D”, and “unfriendly” and “filthy” for “bathroom”. “OURS w/o STN” directly applies attention over the opinion hidden states INLINEFORM0 's, similar to what CMLA does. As shown in Figure FIGREF41 , it captures some unrelated opinion words (e.g. “fine”) and even some non-opinionated words. As a result, it brings in some noise into the global opinion summary, and consequently the final prediction accuracy will be affected. This example demonstrates that the proposed STN works pretty well to help attend to more related opinion words given a particular aspect.

Some predictions of our model and those of LSTM and OURS w/o THA & STN are given in Table TABREF43 . The models incorporating attention-based opinion summary (i.e., OURS and OURS w/o THA & STN) can better determine if the commonly-used nouns are aspect terms or not (e.g. “device” in the first input), since they make decisions based on the global opinion information. Besides, they are able to extract some infrequent or even misspelled aspect terms (e.g. “survice” in the second input) based on the indicative clues provided by opinion words. For the last three cases, having aspects in coordinate structures (i.e. the third and the fourth) or long aspects (i.e. the fifth), our model can give precise predictions owing to the previous detection clues captured by THA. Without using these clues, the baseline models fail.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-6a835e032796b72f14bf3299909d2c272ec69fbfa826b143e672339ee4aa9872

Passage ID: `qasper-passage-v1-6a835e032796b72f14bf3299909d2c272ec69fbfa826b143e672339ee4aa9872`; retrieval score: 3.762888584352805.

Word count: 276.

```text
As shown in Table TABREF39 , the proposed framework consistently obtains the best scores on all of the four datasets. Compared with the winning systems of SemEval ABSA, our framework achieves 5.0%, 1.6%, 1.4%, 1.3% absolute gains on INLINEFORM0 , INLINEFORM1 , INLINEFORM2 and INLINEFORM3 respectively.

Our framework can outperform RNCRF, a state-of-the-art model based on dependency parsing, on all datasets. We also notice that RNCRF does not perform well on INLINEFORM0 and INLINEFORM1 (3.7% and 3.9% inferior than ours). We find that INLINEFORM2 and INLINEFORM3 contain many informal reviews, thus RNCRF's performance degradation is probably due to the errors from the dependency parser when processing such informal texts.

CMLA and MIN do not rely on dependency parsing, instead, they employ attention mechanism to distill opinion information to help aspect extraction. Our framework consistently performs better than them. The gains presumably come from two perspectives: (1) In our model, the opinion summary is exploited after performing the selective transformation conditioned on the current aspect features, thus the summary can to some extent avoid the noise due to directly applying conventional attention. (2) Our model can discover some uncommon aspects under the guidance of some commonly-used aspects in coordinate structures by the history attention.

CRF with basic feature template is not strong, therefore, we add CRF-2 as another baseline. As shown in Table TABREF39 , CRF-2 with word embeddings achieves much better results than CRF-1 on all datasets. WDEmb, which is also an enhanced CRF-based method using additional dependency context embeddings, obtains superior performances than CRF-2. Therefore, the above comparison shows that word embeddings are useful and the embeddings incorporating structure information can further improve the performance.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-f837ffddc1702c03e8f55a78f50333ff111b8bd2c2006a994ef398832507936d

Passage ID: `qasper-passage-v1-f837ffddc1702c03e8f55a78f50333ff111b8bd2c2006a994ef398832507936d`; retrieval score: 3.687404528464708.

Word count: 115.

```text
For more accurate aspect term extraction, we explored two important types of information, namely aspect detection history, and opinion summary. We design two components, i.e. truncated history attention, and selective transformation network. Experimental results show that our model dominates those joint extraction works such as RNCRF and CMLA on the performance of ATE. It suggests that the joint extraction sacrifices the accuracy of aspect prediction, although the ground-truth opinion words were annotated by these authors. Moreover, one should notice that those joint extraction methods do not care about the correspondence between the extracted aspect terms and opinion words. Therefore, the necessity of such joint extraction should be obelized, given the experimental findings in this paper.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-73205bba58e846ad270eb77290290eeefbdde57e11fcef0fc45c20d29427e982

Passage ID: `qasper-passage-v1-73205bba58e846ad270eb77290290eeefbdde57e11fcef0fc45c20d29427e982`; retrieval score: 3.406433513754894.

Word count: 232.

```text
(STN) (the STN block in Figure FIGREF3 ), and insert it before attending to global opinion features so that more important features with respect to a given aspect candidate will be highlighted. Specifically, STN first calculates a new opinion representation INLINEFORM0 given the current aspect feature INLINEFORM1 as follows: DISPLAYFORM0

where INLINEFORM0 and INLINEFORM1 are parameters for history-aware aspect representations and opinion representations respectively. They map INLINEFORM2 and INLINEFORM3 to the same subspace. Here the aspect feature INLINEFORM4 acts as a “filter” to keep more important opinion features. Equation EQREF14 also introduces a residual block to obtain a better opinion representation INLINEFORM5 , which is conditioned on the current aspect feature INLINEFORM6 .

For distilling the global opinion summary, we introduce a bi-linear term to calculate the association score between INLINEFORM0 and each INLINEFORM1 : DISPLAYFORM0

where INLINEFORM0 and INLINEFORM1 are parameters of the Bi-Linear Attention layer. The improved opinion summary INLINEFORM2 at the time INLINEFORM3 is obtained via the weighted sum of the opinion representations: DISPLAYFORM0

Finally, we concatenate the opinion summary INLINEFORM0 and the history-aware aspect representation INLINEFORM1 and feed it into the top-most fully-connected (FC) layer for aspect prediction: DISPLAYFORM0 DISPLAYFORM1

Note that our framework actually performs a multi-task learning, i.e. predicting both aspects and opinions. We regard the initial token-level representations INLINEFORM0 as the features for opinion prediction: DISPLAYFORM0

INLINEFORM0 and INLINEFORM1 are parameters of the FC layers.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-70c406458b1022fd541586b6b9f17f4621aa4cb98d106313c8ea151ebaccac81

Passage ID: `qasper-passage-v1-70c406458b1022fd541586b6b9f17f4621aa4cb98d106313c8ea151ebaccac81`; retrieval score: 3.2478276552743415.

Word count: 400.

```text
Aspect-Based Sentiment Analysis (ABSA) involves detecting opinion targets and locating opinion indicators in sentences in product review texts BIBREF0 . The first sub-task, called Aspect Term Extraction (ATE), is to identify the phrases targeted by opinion indicators in review sentences. For example, in the sentence “I love the operating system and preloaded software”, the words “operating system” and “preloaded software” should be extracted as aspect terms, and the sentiment on them is conveyed by the opinion word “love”. According to the task definition, for a term/phrase being regarded as an aspect, it should co-occur with some “opinion words” that indicate a sentiment polarity on it BIBREF1 .

Many researchers formulated ATE as a sequence labeling problem or a token-level classification problem. Traditional sequence models such as Conditional Random Fields (CRFs) BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 , Long Short-Term Memory Networks (LSTMs) BIBREF6 and classification models such as Support Vector Machine (SVM) BIBREF7 have been applied to tackle the ATE task, and achieved reasonable performance. One drawback of these existing works is that they do not exploit the fact that, according to the task definition, aspect terms should co-occur with opinion-indicating words. Thus, the above methods tend to output false positives on those frequently used aspect terms in non-opinionated sentences, e.g., the word “restaurant” in “the restaurant was packed at first, so we waited for 20 minutes”, which should not be extracted because the sentence does not convey any opinion on it.

There are a few works that consider opinion terms when tackling the ATE task. BIBREF8 proposed Recursive Neural Conditional Random Fields (RNCRF) to explicitly extract aspects and opinions in a single framework. Aspect-opinion relation is modeled via joint extraction and dependency-based representation learning. One assumption of RNCRF is that dependency parsing will capture the relation between aspect terms and opinion words in the same sentence so that the joint extraction can benefit. Such assumption is usually valid for simple sentences, but rather fragile for some complicated structures, such as clauses and parenthesis. Moreover, RNCRF suffers from errors of dependency parsing because its network construction hinges on the dependency tree of inputs. CMLA BIBREF9 models aspect-opinion relation without using syntactic information. Instead, it enables the two tasks to share information via attention mechanism. For example, it exploits the global opinion information by directly computing the association score between the aspect prototype and individual opinion hidden representations and then
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1300.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "b3596aa57239b4bc334f9d6dbd92d867f46924fa": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1805.00760:2:0": [
        [
          0,
          999
        ]
      ]
    }
  }
}
```

## Question: 593e307d9a9d7361eba49484099c7a8147d3dade

### Question ID and text

Question ID: `593e307d9a9d7361eba49484099c7a8147d3dade`; paper ID: `1812.06038`.

```text
What are causal attribution networks?
```

### Answers

#### Answer: 9a696b810674778566b40332d9c70845193d44d3

```text
{"evidence": ["In this work we compare causal attribution networks derived from three datasets. A causal attribution dataset is a collection of text pairs that reflect cause-effect relationships proposed by humans (for example, “virus causes sickness”). These written statements identify the nodes of the network (see also our graph fusion algorithm for dealing with semantically equivalent statements) while cause-effect relationships form the directed edges (“virus” $\\rightarrow $ “sickness”) of the causal attribution network."], "extractive_spans": [], "free_form_answer": "networks where nodes represent causes and effects, and directed edges represent cause-effect relationships proposed by humans", "highlighted_evidence": ["A causal attribution dataset is a collection of text pairs that reflect cause-effect relationships proposed by humans (for example, “virus causes sickness”). These written statements identify the nodes of the network (see also our graph fusion algorithm for dealing with semantically equivalent statements) while cause-effect relationships form the directed edges (“virus” $\\rightarrow $ “sickness”) of the causal attribution network."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1812.06038:0:0`

```text
In this work we compare causal attribution networks derived from three datasets. A causal attribution dataset is a collection of text pairs that reflect cause-effect relationships proposed by humans (for example, “virus causes sickness”). These written statements identify the nodes of the network (see also our graph fusion algorithm for dealing with semantically equivalent statements) while cause-effect relationships form the directed edges (“virus” $\rightarrow $ “sickness”) of the causal attribution network.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-5c63cd28051892d19aa490b5212528d17db4537b0e5582722a0325fd01d1a82b

Passage ID: `qasper-passage-v1-5c63cd28051892d19aa490b5212528d17db4537b0e5582722a0325fd01d1a82b`; retrieval score: 3.5829913412171415.

Word count: 138.

```text
Here we use network and text analysis tools to compare causal attribution networks (Sec. "Comparing causal networks" ). Crucially, nodes in these networks are defined only by their written descriptions, and multiple written descriptions can represent the same conceptual entity. Thus, to understand how causal attribution networks can be combined, we introduce and analyze a method for fusing networks (Sec. "Fusing causal networks" ) that builds off both the network structure and associated text information and explicitly incorporates conceptual equivalencies. Lastly, in Sec. "Inferring the size of the causal attribution network" we use the degree of overlap in these networks as a means to infer the total size of the one underlying causal attribution network being explored by these data collection efforts, allowing us to better understand the size of collective space of cause-effect relationships held by humans.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-8b76eea8a3013b9976a3cab95b371a0dafdfffbb6491d4af54dfa8090d6bfd3a

Passage ID: `qasper-passage-v1-8b76eea8a3013b9976a3cab95b371a0dafdfffbb6491d4af54dfa8090d6bfd3a`; retrieval score: 3.337439529460091.

Word count: 256.

```text
In this work we compare causal attribution networks derived from three datasets. A causal attribution dataset is a collection of text pairs that reflect cause-effect relationships proposed by humans (for example, “virus causes sickness”). These written statements identify the nodes of the network (see also our graph fusion algorithm for dealing with semantically equivalent statements) while cause-effect relationships form the directed edges (“virus” $\rightarrow $ “sickness”) of the causal attribution network.

We collected causal attribution networks from three sources of data: English Wikidata BIBREF11 , English ConceptNet BIBREF10 , and IPRnet BIBREF12 . Wikidata and ConceptNet, are large knowledge graphs that contain semantic links denoting many types of interactions, one of which is causal attribution, while IPRnet comes from an Amazon Mechanical Turk study in which crowd workers were prompted to provide causal relationships. Wikidata relations were gathered by running four search queries on the Wikidata API (query.wikidata.org). These queries searched for relations with the properties: "has immediate cause", "has effect", "has cause", or "immediate cause of". The first and third searches reverse the order of the cause and effect which we reversed back. We discarded any Wikidata relations where the cause or effect were blank, as well as one ambiguous relation where the cause was "NaN". ConceptNet attributions were gathered by searching the English ConceptNet version 5.6.0 assertions for “/r/Causes/” relations. Lastly, IPRnet was developed in BIBREF12 which we use directly.

The three networks together contain $23\,239$ causal links and $19\,096$ unique terms, of which there are $4\,265$ and $14\,831$ unique causes and effects, respectively.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1812.06038:0:0` | full | 0:515 |

#### Rank 3: qasper-passage-v1-ba45c197b76f861c09f3bbb5d48496d42e6f8bd07ac28bb79ae72dec527b3912

Passage ID: `qasper-passage-v1-ba45c197b76f861c09f3bbb5d48496d42e6f8bd07ac28bb79ae72dec527b3912`; retrieval score: 3.188876611247084.

Word count: 271.

```text
The construction of causal attribution networks generates important knowledge networks that may inform causal inference research and even help future AI systems to perform causal reasoning, but these networks are time-consuming and costly to generate, and to date no efforts have been made to combine different networks. Our work not only studies the potential for fusing different networks together, but also infers the overall size of the total causal attribution network being explored.

We used capture-recapture estimators to infer the number of nodes and links in the underlying causal attribution network, given the Wikidata and ConceptNet networks and using NetFUSES and a semantic similarity function to help account for semantically equivalent nodes within and between Wikidata and ConceptNet. The validity of these estimates depends on Wikidata and ConceptNet being independent samples of the underlying network. As with many practical applications of capture-recapture in wildlife ecology and other areas, here we must question how well this independence assumption holds. The best way to sharpen these estimates is to introduce a new causal attribution survey specifically designed to capture either nodes or links independently (it is unlikely that a single survey protocol can sample independently both nodes and links), and then perform this same survey multiple times.

NetFUSES is a simple approach to graph fusion, in this case building off advances made in semantic representations of natural language, although any similarity function can be used to identify semantically equivalent nodes as appropriate. We anticipate that more accurate and more computationally efficient methods for graph fusion can be developed, but even the current method may be useful in a number of other problem domains.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-b6131f07870d3393b1c8f5e6b96f65b1c000a9e3a541a96fe831e3adabd2f775

Passage ID: `qasper-passage-v1-b6131f07870d3393b1c8f5e6b96f65b1c000a9e3a541a96fe831e3adabd2f775`; retrieval score: 3.128080666206086.

Word count: 400.

```text
We perform a descriptive analysis of the three datasets, comparing and contrasting their features and properties. We focus on two aspects, the network structure and the text information (the written descriptions associated with each node in the network). Understanding these data at these levels can inform efforts to combine different causal attribution networks (Sec. "Fusing causal networks" ).

Table 1 and Fig. 2 summarize network characteristics for the three causal attribution networks. We focus on standard measures of network structure, measuring the sizes, densities, motif structure, and connectedness of the three networks. Both Wikidata and ConceptNet, the two larger networks, are highly disconnected, amounting to collections of small components with low density. In contrast, IPRnet is smaller but comparatively more dense and connected, with higher average degree, fewer disconnected components, and more clustering (Table 1 ). All three networks are degree dissortative, meaning that high-degree nodes are more likely to connect to low-degree nodes. For connectedness and path lengths, we consider both directed and undirected versions of the network allowing us to measure strong and weak connectivity, respectively. All three networks are well connected when ignoring link directionality, but few directed paths exist between disparate nodes in Wikidata and ConceptNet, as shown by the large number of strong connected components and small size of the strong giant components for those networks.

To examine motifs, we focus on feedback loops and feedforward loops, both of which play important roles in causal relationships BIBREF32 , BIBREF33 . The sparse Wikidata network has neither loops, while ConceptNet has 87 feedforward loops and 1 feedback loop (Table 1 ). In contrast, IPRnet has far more loops, 986 feedback and 3541 feedforward loops.

Complementing the statistics shown in Table 1 , Fig. 2 shows the degree distributions ( 2 A), distributions of component sizes ( 2 B), and distributions of two centrality measures ( 2 C). All three networks display a skewed or heavy-tailed degree distribution. We again see that Wikidata and ConceptNet appear similar to one another while IPRnet is quite different, especially in terms of centrality. One difference between ConceptNet and Wikidata visible in 2 A is a mode of nodes with degree $\sim 30$ within ConceptNet that is not present in Wikidata.

Understanding the network structure of each dataset only accounts for part of the information. Each node $i$ in these networks is associated with a sentence $s_i$ , a written word
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-39f29514be1d41320be3f592b07e54db188648bd9331c00365aef62adfdd76d9

Passage ID: `qasper-passage-v1-39f29514be1d41320be3f592b07e54db188648bd9331c00365aef62adfdd76d9`; retrieval score: 3.09615547804777.

Word count: 400.

```text
These causal attributions networks are separate efforts to map out the underlying or latent causal attribution network held collectively by humans. It is natural to then ask if these different efforts can be combined in an effective way. Fusing these networks together can provide a single causal attribution network for researchers to study.

At the most basic level, one can fuse these networks together simply by taking their union, defining a single network containing all the unique nodes and edges of the original networks. Unfortunately, nodes in these networks are identified by their sentences, and this graph union assumes that two nodes $i$ and $j$ are equivalent iff $s_i = s_j$ . This is overly restrictive as these sentences serve as descriptions of associated concepts, and we ideally want to combine nodes that represent the same concept even when their written descriptions differ. Indeed, even within a single network it can be necessary to identify and combine nodes in this way. We identify this problem as graph fusion. Graph fusion is a type of record linkage problem and is closely related to graph alignment and (inexact) graph matching BIBREF27 , but unlike those problems, graph fusion assumes the need to identify node equivalencies both within and between the networks being fused.

We introduce a fusion algorithm, NetFUSES (Network FUsion with SEmantic Similarity) that allows us to combine networks using a measure of similarity between nodes (Sec. "Data and Methods" ). Crucially, NetFUSES can handle networks where nodes may need to be combined even within a single network. Here we compare nodes by focusing on the corresponding sentences $s_i$ and $s_j$ of the nodes $i$ and $j$ , respectively, in two networks. We use recent advances in computational linguistics to define a semantic similarity $S(s_i,s_j)$ between $s_i$ and $s_j$ and consider $i$ and $j$ as equivalent when $S(s_i,s_j) \ge t$ for some semantic threshold $s_j$0 . See Sec. "Data and Methods" for details.

To apply NetFUSES with our semantic similarity function (Sec. "Data and Methods" ) requires determining a single parameter, the similarity threshold $t$ . One can identify a value of $t$ using an independent analysis of text, but we argue for a simple indicator of its value given the networks: growth in the number of self-loops as $t$ is varied. If two nodes $i$ and $j$ that are connected before fusion are combined into a single node $u$ by
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1465.

Fully covered answer annotations: 9a696b810674778566b40332d9c70845193d44d3.

Missing evidence by answer annotation:

```text
{
  "9a696b810674778566b40332d9c70845193d44d3": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: 601e58a3d2c03a0b4cd627c81c6228a714e43903

### Question ID and text

Question ID: `601e58a3d2c03a0b4cd627c81c6228a714e43903`; paper ID: `1904.11942`.

```text
What type of baseline are established for the two datasets?
```

### Answers

#### Answer: b51e9beb914a8bd0af00931fd7c0e2384a68dcfa

```text
{"evidence": ["The series of TempEval competitions BIBREF21 , BIBREF22 , BIBREF23 have attracted many research interests in predicting event temporal relations. Early attempts by BIBREF24 , BIBREF21 , BIBREF25 , BIBREF26 only use pair-wise classification models. State-of-the-art local methods, such as ClearTK BIBREF27 , UTTime BIBREF28 , and NavyTime BIBREF29 improve on earlier work by feature engineering with linguistic and syntactic rules. As we mention in the Section 2, CAEVO is the current state-of-the-art system for feature-based temporal event relation extraction BIBREF10 . It's widely used as the baseline for evaluating TB-Dense data. We adopt it as our baseline for evaluating CaTeRS and RED datasets. Additionally, several models BramsenDLB2006, ChambersJ2008, DoLuRo12, NingWuRo18, P18-1212 have successfully incorporated global inference to impose global prediction consistency such as temporal transitivity."], "extractive_spans": ["CAEVO"], "free_form_answer": "", "highlighted_evidence": ["As we mention in the Section 2, CAEVO is the current state-of-the-art system for feature-based temporal event relation extraction BIBREF10 . It's widely used as the baseline for evaluating TB-Dense data. We adopt it as our baseline for evaluating CaTeRS and RED datasets."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1904.11942:6:0`

```text
The series of TempEval competitions BIBREF21 , BIBREF22 , BIBREF23 have attracted many research interests in predicting event temporal relations. Early attempts by BIBREF24 , BIBREF21 , BIBREF25 , BIBREF26 only use pair-wise classification models. State-of-the-art local methods, such as ClearTK BIBREF27 , UTTime BIBREF28 , and NavyTime BIBREF29 improve on earlier work by feature engineering with linguistic and syntactic rules. As we mention in the Section 2, CAEVO is the current state-of-the-art system for feature-based temporal event relation extraction BIBREF10 . It's widely used as the baseline for evaluating TB-Dense data. We adopt it as our baseline for evaluating CaTeRS and RED datasets. Additionally, several models BramsenDLB2006, ChambersJ2008, DoLuRo12, NingWuRo18, P18-1212 have successfully incorporated global inference to impose global prediction consistency such as temporal transitivity.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-1f4d16ba72aea6f3403eb9bbaea9c965ca0f8f0863956a01c20b45f9297416bf

Passage ID: `qasper-passage-v1-1f4d16ba72aea6f3403eb9bbaea9c965ca0f8f0863956a01c20b45f9297416bf`; retrieval score: 5.755505463170137.

Word count: 86.

```text
We established strong baselines for two story narrative understanding datasets: CaTeRS and RED. We have shown that neural network-based models can outperform feature-based models with wide margins, and we conducted an ablation study to show that contextualized representation learning can boost performance of NN models. Further research can focus on more systematic study or build stronger NN models over the same datasets used in this work. Exploring possibilities to directly apply temporal relation extraction to enhance performance of story generation systems is another promising research direction.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-d2179ce62b2a74b3c389953153d1d4531aaa1f5e23743a0dfc92dc5e2e9888fe

Passage ID: `qasper-passage-v1-d2179ce62b2a74b3c389953153d1d4531aaa1f5e23743a0dfc92dc5e2e9888fe`; retrieval score: 4.59129002129174.

Word count: 126.

```text
The series of TempEval competitions BIBREF21 , BIBREF22 , BIBREF23 have attracted many research interests in predicting event temporal relations. Early attempts by BIBREF24 , BIBREF21 , BIBREF25 , BIBREF26 only use pair-wise classification models. State-of-the-art local methods, such as ClearTK BIBREF27 , UTTime BIBREF28 , and NavyTime BIBREF29 improve on earlier work by feature engineering with linguistic and syntactic rules. As we mention in the Section 2, CAEVO is the current state-of-the-art system for feature-based temporal event relation extraction BIBREF10 . It's widely used as the baseline for evaluating TB-Dense data. We adopt it as our baseline for evaluating CaTeRS and RED datasets. Additionally, several models BramsenDLB2006, ChambersJ2008, DoLuRo12, NingWuRo18, P18-1212 have successfully incorporated global inference to impose global prediction consistency such as temporal transitivity.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.11942:6:0` | full | 0:912 |

#### Rank 3: qasper-passage-v1-b5b3ed816f85afc3a48b80d3a7eb493ffac82dc4fd7900b51e6ac61c89f1f5d0

Passage ID: `qasper-passage-v1-b5b3ed816f85afc3a48b80d3a7eb493ffac82dc4fd7900b51e6ac61c89f1f5d0`; retrieval score: 4.288529673012455.

Word count: 69.

```text
Table TABREF25 contains the best hyper-parameters and Table TABREF26 contains micro-average F1 scores for both datasets on dev and test sets. We only consider positive pairs, i.e. correct predictions on NONE pairs are excluded for evaluation. In general, the baseline model CAEVO is outperformed by both NN models, and NN model with BERT embedding achieves the greatest performance. We now provide more detailed analysis and discussion for each dataset.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-6756a64385e6a766f14cd34df68f52b739aab05e09bfe2c379a72dbecef8325b

Passage ID: `qasper-passage-v1-6756a64385e6a766f14cd34df68f52b739aab05e09bfe2c379a72dbecef8325b`; retrieval score: 3.6764729731468333.

Word count: 341.

```text
Event temporal relation understanding is a major component of story/narrative comprehension. It is an important natural language understanding (NLU) task with broad applications to downstream tasks such as story understanding BIBREF0 , BIBREF1 , BIBREF2 , question answering BIBREF3 , BIBREF4 , and text summarization BIBREF5 , BIBREF6 .

The goal of event temporal relation extraction is to build a directed graph where nodes correspond to events, and edges reflect temporal relations between the events. Figure FIGREF1 illustrates an example of such a graph for the text shown above. Different types of edges specify different temporal relations: the event assassination is before slaughtered, slaughtered is included in rampage, and the relation between rampage and war is vague.

Modeling event temporal relations is crucial for story/narrative understanding and storytelling, because a story is typically composed of a sequence of events BIBREF7 . Several story corpora are thus annotated with various event-event relations to understand commonsense event knowledge. CaTeRS BIBREF8 is created by annotating 320 five-sentence stories sampled from ROCStories BIBREF7 dataset. RED BIBREF9 contains annotations of rich relations between event pairs for storyline understanding, including co-reference and partial co-reference relations, temporal; causal, and sub-event relations.

Despite multiple productive research threads on temporal and causal relation modeling among events BIBREF10 , BIBREF11 , BIBREF12 and event relation annotation for story understanding BIBREF8 , the intersection of these two threads seems flimsy. To the best of our knowledge, no event relation extraction results have been reported on CaTeRS and RED.

We apply neural network models that leverage recent advances in contextualized embeddings (BERT BIBREF13 ) to event-event relation extraction tasks for CaTeRS and RED. Our goal in this paper is to increase understanding of how well the state-of-the-art event relation models work for story/narrative comprehension.

In this paper, we report the first results of event temporal relation extraction on two under-explored story comprehension datasets: CaTeRS and RED. We establish strong baselines with neural network models enhanced by recent breakthrough of contextualized embeddings, BERT BIBREF13 . We summarize the contributions of the paper as follows:
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-82160e367adde4aad0a7b6b4d3e2d44050a784537de173919f33ab7b60c9d39d

Passage ID: `qasper-passage-v1-82160e367adde4aad0a7b6b4d3e2d44050a784537de173919f33ab7b60c9d39d`; retrieval score: 3.403044242646128.

Word count: 400.

```text
is created by annotating 1600 sentences of 320 five-sentence stories sampled from ROCStories BIBREF7 dataset. CaTeRS contains both temporal and causal relations in an effort to understand and predict commonsense relations between events.

As demonstrated in Table TABREF16 , we split all stories into 220 training and 80 test. We do not construct the development set because the dataset is small. Note that some relations have compounded labels such as “CAUSE_BEFORE”, “ENABLE_BEFORE”, etc. We only take the temporal portion of the annotations.

annotates a wide range of relations of event pairs including their coreference and partial coreference relations, and temporal, causal and subevent relationships. We split data according to the standard train, development, test sets, and only focus on the temporal relations.

The common issue of these two datasets is that they are not densely annotated – not every pair of events is annotated with a relation. We provide one way to handle negative (unannotated) pairs in this paper. When constructing negative examples, we take all event pairs that occur within the same or neighboring sentences with no annotations, labeling them as “NONE”. The negative to positive samples ratio is 1.00 and 11.5 for CaTeRS and RED respectively. Note that RED data has much higher negative ratio (as shown in Table TABREF16 ) because it contains longer articles, more complicated sentence structures, and richer entity types than CaTeRS where all stories consist of 5 (mostly short) sentences.

In both the development and test sets, we add all negative pairs as candidates for the relation prediction. During training, the number of negative pairs we add is based on a hyper-parameter that we tune to control the negative-to-positive sample ratio.

To justify our decision of selecting negative pairs within the same or neighboring sentences, we show the distribution of distances across positive sentence pairs in Table TABREF18 . Although CaTeRS data has pair distance more evenly distributed than RED, we observe that the vast majority (85.87% and 93.99% respectively) of positive pairs have sentence distance less than or equal to one.

To handle negative pairs that are more than two sentences away, we automatically predict all out-of-window pairs as “NONE”. This means that some positive pairs will be automatically labeled as negative pairs. Since the percentage of out-of-window positive pairs is small, we believe the impact on performance is small. We can investigate expanding the prediction window in future research, but the
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1022.

Fully covered answer annotations: b51e9beb914a8bd0af00931fd7c0e2384a68dcfa.

Missing evidence by answer annotation:

```text
{
  "b51e9beb914a8bd0af00931fd7c0e2384a68dcfa": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: d571e0b0f402a3d36fb30d70cdcd2911df883bc7

### Question ID and text

Question ID: `d571e0b0f402a3d36fb30d70cdcd2911df883bc7`; paper ID: `2002.07306`.

```text
Is the system tested on low-resource languages?
```

### Answers

#### Answer: a3d3604691f4c6bb83b436a2db8b4ad2124a3ac2

```text
{"evidence": ["We evaluate our approach for six target languages: French (fr), Russian (ru), Arabic (ar), Chinese (zh), Hindi (hi), and Vietnamese (vi). These languages belong to four different language families. French, Russian, and Hindi are Indo-European languages, similar to English. Arabic, Chinese, and Vietnamese belong to Afro-Asiatic, Sino-Tibetan, and Austro-Asiatic family respectively. The choice of the six languages also reflects different training conditions depending on the amount of monolingual data. French and Russian, and Arabic can be regarded as high resource languages whereas Hindi has far less data and can be considered as low resource."], "extractive_spans": [], "free_form_answer": "", "highlighted_evidence": ["French and Russian, and Arabic can be regarded as high resource languages whereas Hindi has far less data and can be considered as low resource."], "unanswerable": false, "yes_no": true}
```

Evidence location: `2002.07306:8:0`

```text
We evaluate our approach for six target languages: French (fr), Russian (ru), Arabic (ar), Chinese (zh), Hindi (hi), and Vietnamese (vi). These languages belong to four different language families. French, Russian, and Hindi are Indo-European languages, similar to English. Arabic, Chinese, and Vietnamese belong to Afro-Asiatic, Sino-Tibetan, and Austro-Asiatic family respectively. The choice of the six languages also reflects different training conditions depending on the amount of monolingual data. French and Russian, and Arabic can be regarded as high resource languages whereas Hindi has far less data and can be considered as low resource.
```

#### Answer: e8eac861373de62f92bb8ccec47bd9efce254fa9

```text
{"evidence": ["We evaluate our approach for six target languages: French (fr), Russian (ru), Arabic (ar), Chinese (zh), Hindi (hi), and Vietnamese (vi). These languages belong to four different language families. French, Russian, and Hindi are Indo-European languages, similar to English. Arabic, Chinese, and Vietnamese belong to Afro-Asiatic, Sino-Tibetan, and Austro-Asiatic family respectively. The choice of the six languages also reflects different training conditions depending on the amount of monolingual data. French and Russian, and Arabic can be regarded as high resource languages whereas Hindi has far less data and can be considered as low resource."], "extractive_spans": [], "free_form_answer": "", "highlighted_evidence": ["The choice of the six languages also reflects different training conditions depending on the amount of monolingual data. French and Russian, and Arabic can be regarded as high resource languages whereas Hindi has far less data and can be considered as low resource."], "unanswerable": false, "yes_no": true}
```

Evidence location: `2002.07306:8:0`

```text
We evaluate our approach for six target languages: French (fr), Russian (ru), Arabic (ar), Chinese (zh), Hindi (hi), and Vietnamese (vi). These languages belong to four different language families. French, Russian, and Hindi are Indo-European languages, similar to English. Arabic, Chinese, and Vietnamese belong to Afro-Asiatic, Sino-Tibetan, and Austro-Asiatic family respectively. The choice of the six languages also reflects different training conditions depending on the amount of monolingual data. French and Russian, and Arabic can be regarded as high resource languages whereas Hindi has far less data and can be considered as low resource.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-313a518ea39d552dc9d51f266dfd8ecb61d5665259eb96bdfb7098a6a2334d7b

Passage ID: `qasper-passage-v1-313a518ea39d552dc9d51f266dfd8ecb61d5665259eb96bdfb7098a6a2334d7b`; retrieval score: 6.818082484207452.

Word count: 149.

```text
For low resource languages, parallel data may not be available. In this case, we rely only on monolingual data (e.g., Wikipedias). We estimate word translation probabilities from word embeddings of the two languages. Word vectors of these languages can be learned using fastText BIBREF14 and then are aligned into a shared space with English BIBREF15, BIBREF16. Unlike learning contextualized representations, learning word vectors is fast and computationally cheap. Given the aligned vectors $\bar{}_f$ of foreign and $\bar{}_e$ of English, we calculate the word translation matrix $\in ^{|V_f|\times |V_e|}$ as

Here, we use $\mathrm {sparsemax}$ BIBREF17 instead of softmax. Sparsemax is a sparse version of softmax and it puts zero probabilities on most of the word in the English vocabulary except few English words that are similar to a given foreign word. This property is desirable in our approach since it leads to a better initialization of the foreign embeddings.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-3b187bf08412ad1888a43904b848052b86d8b66f0e52dc7c3857727bf34274e6

Passage ID: `qasper-passage-v1-3b187bf08412ad1888a43904b848052b86d8b66f0e52dc7c3857727bf34274e6`; retrieval score: 5.241584735226791.

Word count: 358.

```text
We evaluate our approach for six target languages: French (fr), Russian (ru), Arabic (ar), Chinese (zh), Hindi (hi), and Vietnamese (vi). These languages belong to four different language families. French, Russian, and Hindi are Indo-European languages, similar to English. Arabic, Chinese, and Vietnamese belong to Afro-Asiatic, Sino-Tibetan, and Austro-Asiatic family respectively. The choice of the six languages also reflects different training conditions depending on the amount of monolingual data. French and Russian, and Arabic can be regarded as high resource languages whereas Hindi has far less data and can be considered as low resource.

For experiments that use parallel data to initialize foreign specific parameters, we use the same datasets in the work of BIBREF6. Specifically, we use United Nations Parallel Corpus BIBREF18 for en-ru, en-ar, en-zh, and en-fr. We collect en-hi parallel data from IIT Bombay corpus BIBREF19 and en-vi data from OpenSubtitles 2018. For experiments that use only monolingual data to initialize foreign parameters, instead of training word-vectors from the scratch, we use the pre-trained word vectors from fastText BIBREF14 to estimate word translation probabilities (Eq. DISPLAY_FORM13). We align these vectors into a common space using orthogonal Procrustes BIBREF20, BIBREF15, BIBREF16. We only use identical words between the two languages as the supervised signal. We use WikiExtractor to extract extract raw sentences from Wikipedias as monolingual data for fine-tuning target embeddings and bilingual LMs (§SECREF15). We do not lowercase or remove accents in our data preprocessing pipeline.

We tokenize English using the provided tokenizer from pre-trained models. For target languages, we use fastBPE to learn 30,000 BPE codes and 50,000 codes when transferring from BERT and RoBERTa respectively. We truncate the BPE vocabulary of foreign languages to match the size of the English vocabulary in the source models. Precisely, the size of foreign vocabulary is set to 32,000 when transferring from BERT and 50,000 when transferring from RoBERTa.

We use XNLI dataset BIBREF9 for classification task and Universal Dependencies v2.4 BIBREF21 for parsing task. Since a language might have more than one treebank in Universal Dependencies, we use the following treebanks: en_ewt (English), fr_gsd (French), ru_syntagrus (Russian) ar_padt (Arabic), vi_vtb (Vietnamese), hi_hdtb (Hindi), and zh_gsd (Chinese).
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2002.07306:8:0` | full | 0:649 |

#### Rank 3: qasper-passage-v1-9c637df64fa92999e8da466468cb40dc15f58c0df864e204ef546d12cfa0029c

Passage ID: `qasper-passage-v1-9c637df64fa92999e8da466468cb40dc15f58c0df864e204ef546d12cfa0029c`; retrieval score: 5.016188649460958.

Word count: 400.

```text
Pre-trained models BIBREF0, BIBREF1 have received much of attention recently thanks to their impressive results in many down stream NLP tasks. Additionally, multilingual pre-trained models enable many NLP applications for other languages via zero-short cross-lingual transfer. Zero-shot cross-lingual transfer has shown promising results for rapidly building applications for low resource languages. BIBREF2 show the potential of multilingual-BERT BIBREF0 in zero-shot transfer for a large number of languages from different language families on five NLP tasks, namely, natural language inference, document classification, named entity recognition, part-of-speech tagging, and dependency parsing.

Although multilingual models are an important ingredient for enhancing language technology in many languages, recent research on improving pre-trained models puts much emphasis on English BIBREF3, BIBREF4, BIBREF5. The current state of affairs makes it difficult to translate advancements in pre-training from English to non-English languages. To our best knowledge, there are only three available multilingual pre-trained models to date: (1) the multilingual-BERT (mBERT) that supports 104 languages, (2) cross-lingual language model BIBREF6 that supports 100 languages, and (3) Language Agnostic SEntence Representations BIBREF7 that supports 93 languages. Among the three models, LASER is based on neural machine translation approach and strictly requires parallel data to train.

Do multilingual models always need to be trained from scratch? Can we transfer linguistic knowledge learned by English pre-trained models to other languages? In this work, we develop a technique to rapidly transfer an existing pre-trained model from English to other languages in an energy efficient way BIBREF8. As the first step, we focus on building a bilingual language model (LM) of English and a target language. Starting from a pre-trained English LM, we learn the target language specific parameters (i.e., word embeddings), while keeping the encoder layers of the pre-trained English LM fixed. We then fine-tune both English and target model to obtain the bilingual LM. We apply our approach to autoencoding language models with masked language model objective and show the advantage of the proposed approach in zero-shot transfer. Our main contributions in this work are:

We propose a fast adaptation method for obtaining a bilingual BERT$_{\textsc {base}}$ of English and a target language within a day using one Tesla V100 16GB GPU.

We evaluate our bilingual LMs for six languages on two zero-shot cross-lingual transfer tasks, namely natural language inference BIBREF9 and universal dependency parsing. We show that our models offer competitive performance or even better that mBERT.

We illustrate that
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-bd10cf219a37b8e65602e760b19955a44564aff916348c58d5b4ee9a93e8dafc

Passage ID: `qasper-passage-v1-bd10cf219a37b8e65602e760b19955a44564aff916348c58d5b4ee9a93e8dafc`; retrieval score: 4.789541197718535.

Word count: 289.

```text
Table TABREF32 shows the XNLI test accuracy. For reference, we also include the scores from the previous work, notably the state-of-the-art system XLM BIBREF6. Before discussing the results, we spell out that the fairest comparison in this experiment is the comparison between mBERT and RAMEN$_{\textsc {base}}$+BERT trained with monolingual only.

We first discuss the transfer results from BERT. Initialized from fastText vectors, RAMEN$_{\textsc {base}}$ slightly outperforms mBERT by 1.9 points on average and widen the gap of 3.3 points on Arabic. RAMEN$_{\textsc {base}}$ gains extra 0.8 points on average when initialized from parallel data. With triple number of parameters, RAMEN$_{\textsc {large}}$ offers an additional boost in term of accuracy and initialization with parallel data consistently improves the performance. It has been shown that BERT$_{\textsc {large}}$ significantly outperforms BERT$_{\textsc {base}}$ on 11 English NLP tasks BIBREF0, the strength of BERT$_{\textsc {large}}$ also shows up when adapted to foreign languages.

Transferring from RoBERTa leads to better zero-shot accuracies. With the same initializing condition, RAMEN$_{\textsc {base}}$+RoBERTa outperforms RAMEN$_{\textsc {base}}$+BERT on average by 2.9 and 2.3 points when initializing from monolingual and parallel data respectively. This result show that with similar number of parameters, our approach benefits from a better English pre-trained model. When transferring from RoBERTa$_{\textsc {large}}$, we obtain state-of-the-art results for five languages.

Currently, RAMEN only uses parallel data to initialize foreign embeddings. RAMEN can also exploit parallel data through translation objective proposed in XLM. We believe that by utilizing parallel data during the fine-tuning of RAMEN would bring additional benefits for zero-shot tasks. We leave this exploration to future work. In summary, starting from BERT$_{\textsc {base}}$, our approach obtains competitive bilingual LMs with mBERT for zero-shot XNLI. Our approach shows the accuracy gains when adapting from a better pre-trained model.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-aab5f8dc182f0093cfabec9dd66e93bdf0bb7874a89fa742639ef5f566120633

Passage ID: `qasper-passage-v1-aab5f8dc182f0093cfabec9dd66e93bdf0bb7874a89fa742639ef5f566120633`; retrieval score: 3.6132547173385015.

Word count: 206.

```text
We evaluate the performance of RAMEN+RoBERTa$_{\textsc {base}}$ (initialized from monolingual data) at each training steps: initialization of word embeddings (0K update), fine-tuning target embeddings (25K), and fine-tuning the model on both English and target language (at each 25K updates). The results are presented in Figure FIGREF40.

Without fine-tuning, the average accuracy of XLNI is 39.7% for a three-ways classification task, and the average LAS score is 3.6 for dependency parsing. We see the biggest leap in the performance after 50K updates. While semantic similarity task profits significantly at 25K updates of the target embeddings, syntactic task benefits with further fine-tuning the encoder. This is expected since the target languages might exhibit different syntactic structures than English and fine-tuning encoder helps to capture language specific structures. We observe a substantial gain of 19-30 LAS for all languages except French after 50K updates.

Language similarities have more impact on transferring syntax than semantics. Without tuning the English encoder, French enjoys 50.3 LAS for being closely related to English, whereas Arabic and Hindi, SOV languages, modestly reach 4.2 and 6.4 points using the SVO encoder. Although Chinese has SVO order, it is often seen as head-final while English is strong head-initial. Perhaps, this explains the poor performance for Chinese.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1402.

Fully covered answer annotations: a3d3604691f4c6bb83b436a2db8b4ad2124a3ac2, e8eac861373de62f92bb8ccec47bd9efce254fa9.

Missing evidence by answer annotation:

```text
{
  "a3d3604691f4c6bb83b436a2db8b4ad2124a3ac2": {
    "unresolved_evidence": [],
    "paragraphs": {}
  },
  "e8eac861373de62f92bb8ccec47bd9efce254fa9": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: fffbd6cafef96eeeee2f9fa5d8ab2b325ec528e6

### Question ID and text

Question ID: `fffbd6cafef96eeeee2f9fa5d8ab2b325ec528e6`; paper ID: `1907.01413`.

```text
How many speakers do they have in the dataset?
```

### Answers

#### Answer: 2cc03c335d671b820b4f04b30bbdd522332ff8ec

```text
{"evidence": ["We use the Ultrax Typically Developing dataset (UXTD) from the publicly available UltraSuite repository BIBREF19 . This dataset contains synchronized acoustic and ultrasound data from 58 typically developing children, aged 5-12 years old (31 female, 27 male). The data was aligned at the phone-level, according to the methods described in BIBREF19 , BIBREF25 . For this work, we discarded the acoustic data and focused only on the B-Mode ultrasound images capturing a midsaggital view of the tongue. The data was recorded using an Ultrasonix SonixRP machine using Articulate Assistant Advanced (AAA) software at INLINEFORM0 121fps with a 135 field of view. A single ultrasound frame consists of 412 echo returns from each of the 63 scan lines (63x412 raw frames). For this work, we only use UXTD type A (semantically unrelated words, such as pack, tap, peak, tea, oak, toe) and type B (non-words designed to elicit the articulation of target phones, such as apa, eepee, opo) utterances."], "extractive_spans": ["58"], "free_form_answer": "", "highlighted_evidence": ["We use the Ultrax Typically Developing dataset (UXTD) from the publicly available UltraSuite repository BIBREF19 . This dataset contains synchronized acoustic and ultrasound data from 58 typically developing children, aged 5-12 years old (31 female, 27 male). "], "unanswerable": false, "yes_no": null}
```

Evidence location: `1907.01413:3:0`

```text
We use the Ultrax Typically Developing dataset (UXTD) from the publicly available UltraSuite repository BIBREF19 . This dataset contains synchronized acoustic and ultrasound data from 58 typically developing children, aged 5-12 years old (31 female, 27 male). The data was aligned at the phone-level, according to the methods described in BIBREF19 , BIBREF25 . For this work, we discarded the acoustic data and focused only on the B-Mode ultrasound images capturing a midsaggital view of the tongue. The data was recorded using an Ultrasonix SonixRP machine using Articulate Assistant Advanced (AAA) software at INLINEFORM0 121fps with a 135 field of view. A single ultrasound frame consists of 412 echo returns from each of the 63 scan lines (63x412 raw frames). For this work, we only use UXTD type A (semantically unrelated words, such as pack, tap, peak, tea, oak, toe) and type B (non-words designed to elicit the articulation of target phones, such as apa, eepee, opo) utterances.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-ee1a6db6e3af4f64f660bfbea7fa2a394f677a09cf26e4fd500efd752e62e615

Passage ID: `qasper-passage-v1-ee1a6db6e3af4f64f660bfbea7fa2a394f677a09cf26e4fd500efd752e62e615`; retrieval score: 5.18707575169328.

Word count: 400.

```text
Ultrasound tongue imaging (UTI) uses standard medical ultrasound to visualize the tongue surface during speech production. It provides a non-invasive, clinically safe, and increasingly inexpensive method to visualize the vocal tract. Articulatory visual biofeedback of the speech production process, using UTI, can be valuable for speech therapy BIBREF0 , BIBREF1 , BIBREF2 or language learning BIBREF3 , BIBREF4 . Ultrasound visual biofeedback combines auditory information with visual information of the tongue position, allowing users, for example, to correct inaccurate articulations in real-time during therapy or learning. In the context of speech therapy, automatic processing of ultrasound images was used for tongue contour extraction BIBREF5 and the animation of a tongue model BIBREF6 . More broadly, speech recognition and synthesis from articulatory signals BIBREF7 captured using UTI can be used with silent speech interfaces in order to help restore spoken communication for users with speech or motor impairments, or to allow silent spoken communication in situations where audible speech is undesirable BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 . Similarly, ultrasound images of the tongue have been used for direct estimation of acoustic parameters for speech synthesis BIBREF13 , BIBREF14 , BIBREF15 .

Speech and language therapists (SLTs) have found UTI to be very useful in speech therapy. In this work we explore the automatic processing of ultrasound tongue images in order to assist SLTs, who currently largely rely on manual processing when using articulatory imaging in speech therapy. One task that could assist SLTs is the automatic classification of tongue shapes from raw ultrasound. This can facilitate the diagnosis and treatment of speech sound disorders, by allowing SLTs to automatically identify incorrect articulations, or by quantifying patient progress in therapy. In addition to being directly useful for speech therapy, the classification of tongue shapes enables further understanding of phonetic variability in ultrasound tongue images. Much of the previous work in this area has focused on speaker-dependent models. In this work we investigate how automatic processing of ultrasound tongue imaging is affected by speaker variation, and how severe degradations in performance can be avoided when applying systems to data from previously unseen speakers through the use of speaker adaptation and speaker normalization approaches.

Below, we present the main challenges associated with the automatic processing of ultrasound data, together with a review of speaker-independent models applied to UTI. Following this, we present the experiments that we have performed (Section SECREF2
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-23720d8a90f3fe36de2c4b732da4ec05d5a37bcac9bfac714afe1828bd3874e6

Passage ID: `qasper-passage-v1-23720d8a90f3fe36de2c4b732da4ec05d5a37bcac9bfac714afe1828bd3874e6`; retrieval score: 4.7855780638853.

Word count: 158.

```text
We use the Ultrax Typically Developing dataset (UXTD) from the publicly available UltraSuite repository BIBREF19 . This dataset contains synchronized acoustic and ultrasound data from 58 typically developing children, aged 5-12 years old (31 female, 27 male). The data was aligned at the phone-level, according to the methods described in BIBREF19 , BIBREF25 . For this work, we discarded the acoustic data and focused only on the B-Mode ultrasound images capturing a midsaggital view of the tongue. The data was recorded using an Ultrasonix SonixRP machine using Articulate Assistant Advanced (AAA) software at INLINEFORM0 121fps with a 135 field of view. A single ultrasound frame consists of 412 echo returns from each of the 63 scan lines (63x412 raw frames). For this work, we only use UXTD type A (semantically unrelated words, such as pack, tap, peak, tea, oak, toe) and type B (non-words designed to elicit the articulation of target phones, such as apa, eepee, opo) utterances.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1907.01413:3:0` | full | 0:986 |

#### Rank 3: qasper-passage-v1-2f81878208acda92726c0dbbb4e6be627014c1e2070a05f265292f955d5d0fca

Passage ID: `qasper-passage-v1-2f81878208acda92726c0dbbb4e6be627014c1e2070a05f265292f955d5d0fca`; retrieval score: 3.8360669638190963.

Word count: 291.

```text
For each system, we normalize the training data to zero mean and unit variance. Due to the high dimensionality of the data (63x412 samples per frame), we have opted to investigate two preprocessing techniques: principal components analysis (PCA, often called eigentongues in this context) and a 2-dimensional discrete cosine transform (DCT). In this paper, Raw input denotes the mean-variance normalized raw ultrasound frame. PCA applies principal components analysis to the normalized training data and preserves the top 1000 components. DCT applies the 2D DCT to the normalized raw ultrasound frame and the upper left 40x40 submatrix (1600 coefficients) is flattened and used as input.

The first type of classifier we evaluate in this work are feedforward neural networks (DNNs) consisting of 3 hidden layers, each with 512 rectified linear units (ReLUs) with a softmax activation function. The networks are optimized for 40 epochs with a mini-batch of 32 samples using stochastic gradient descent. Based on preliminary experiments on the validation set, hyperparameters such learning rate, decay rate, and L2 weight vary depending on the input format (Raw, PCA, or DCT). Generally, Raw inputs work better with smaller learning rates and heavier regularization to prevent overfitting to the high-dimensional data. As a second classifier to evaluate, we use convolutional neural networks (CNNs) with 2 convolutional and max pooling layers, followed by 2 fully-connected ReLU layers with 512 nodes. The convolutional layers use 16 filters, 8x8 and 4x4 kernels respectively, and rectified units. The fully-connected layers use dropout with a drop probability of 0.2. Because CNN systems take longer to converge, they are optimized over 200 epochs. For all systems, at the end of every epoch, the model is evaluated on the development set, and the best model across all epochs is kept.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-6704ce0eb6c000f6fb91d4a756bc08cd9ff46a9589e4a67993a9e63f710a7005

Passage ID: `qasper-passage-v1-6704ce0eb6c000f6fb91d4a756bc08cd9ff46a9589e4a67993a9e63f710a7005`; retrieval score: 3.2565526964535847.

Word count: 109.

```text
In this paper, we have investigated speaker-independent models for the classification of phonetic segments from raw ultrasound data. We have shown that the performance of the models heavily degrades when evaluated on data from unseen speakers. This is a result of the variability in ultrasound images, mostly due to differences across speakers, but also due to shifts in probe placement. Using the mean of all ultrasound frames for a new speaker improves the generalization of the models to unseen data, especially when using convolutional neural networks. We have also shown that adapting a pre-trained speaker-independent system using as few as 50 ultrasound frames can outperform a corresponding speaker-dependent system.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-bdcd249d5dde7b9d727985f2384d02029d4ef9899a098f4514a7f06264cf76eb

Passage ID: `qasper-passage-v1-bdcd249d5dde7b9d727985f2384d02029d4ef9899a098f4514a7f06264cf76eb`; retrieval score: 2.797705986073097.

Word count: 132.

```text
most speakers clustered around the identity line (bottom left subplot). Figure FIGREF12 also illustrates the variability across speakers for each of the training scenarios. The classification task is easier for some speakers than others. In an attempt to understand this variability, we can look at correlation between accuracy scores and various speaker details. For the CNN systems, we have found some correlation (Pearson's product-moment correlation) between accuracy and age for the dependent ( INLINEFORM0 ), multi-speaker ( INLINEFORM1 ), and adapted ( INLINEFORM2 ) systems. A very small correlation ( INLINEFORM3 ) was found for the independent system. Similarly, some correlation was found between accuracy and sampling score ( INLINEFORM4 ) for the dependent system, but not for the remaining scenarios. No correlation was found between accuracy and gender (point biserial correlation).
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1090.

Fully covered answer annotations: 2cc03c335d671b820b4f04b30bbdd522332ff8ec.

Missing evidence by answer annotation:

```text
{
  "2cc03c335d671b820b4f04b30bbdd522332ff8ec": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: 0b92fb692feb35d4b4bf4665f7754d283d6ad5f3

### Question ID and text

Question ID: `0b92fb692feb35d4b4bf4665f7754d283d6ad5f3`; paper ID: `1908.11860`.

```text
What are the performance results?
```

### Answers

#### Answer: 46773036407495e12fc0be2224060db32f6d6676

```text
{"evidence": ["To answer RQ2, which is concerned with in-domain ATSC performance, we see in tab:results that for the in-domain training case, our models BERT-ADA Lapt and BERT-ADA Rest achieve performance close to state-of-the-art on the laptops dataset and new state-of-the-art on the restaurants dataset with accuracies of $79.19\\%$ and $87.14\\%$, respectively. On the restaurants dataset, this corresponds to an absolute improvement of $2.2\\%$ compared to the previous state-of-the-art method BERT-PT. Language model finetuning produces a larger improvement on the restaurants dataset. We think that one reason for that might be that the restaurants domain is underrepresented in the pre-training corpora of BERTBASE. Generally, we find that language model finetuning helps even if the finetuning domain does not match the evaluation domain. We think the reason for this might be that the BERT-base model is pre-trained more on knowledge-based corpora like Wikipedia than on text containing opinions. Another finding is that BERT-ADA Joint performs better on the laptops dataset than BERT-ADA Rest, although the unique amount of laptop reviews are the same in laptops- and joint-corpora. We think that confusion can be created when mixing the domains, but this needs to be investigated further. We also find that the XLNet-base baseline performs generally stronger than BERT-base and even outperforms BERT-ADA Lapt with an accuracy of $79.89\\%$ on the laptops dataset.", "In general, the ATSC task generalizes well cross-domain, with about 2-$3\\%$ drop in accuracy compared to in-domain training. We think the reason for this might be that syntactical relationships between the aspect-target and the phrase expressing sentiment polarity as well as knowing the sentiment-polarity itself are sufficient to solve the ATSC task in many cases."], "extractive_spans": ["results that for the in-domain training case, our models BERT-ADA Lapt and BERT-ADA Rest achieve performance close to state-of-the-art on the laptops dataset", "new state-of-the-art on the restaurants dataset with accuracies of $79.19\\%$ and $87.14\\%$, respectively."], "free_form_answer": "", "highlighted_evidence": ["To answer RQ2, which is concerned with in-domain ATSC performance, we see in tab:results that for the in-domain training case, our models BERT-ADA Lapt and BERT-ADA Rest achieve performance close to state-of-the-art on the laptops dataset and new state-of-the-art on the restaurants dataset with accuracies of $79.19\\%$ and $87.14\\%$, respectively.", "In general, the ATSC task generalizes well cross-domain, with about 2-$3\\%$ drop in accuracy compared to in-domain training."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1908.11860:19:2`

```text
To answer RQ2, which is concerned with in-domain ATSC performance, we see in tab:results that for the in-domain training case, our models BERT-ADA Lapt and BERT-ADA Rest achieve performance close to state-of-the-art on the laptops dataset and new state-of-the-art on the restaurants dataset with accuracies of $79.19\%$ and $87.14\%$, respectively. On the restaurants dataset, this corresponds to an absolute improvement of $2.2\%$ compared to the previous state-of-the-art method BERT-PT. Language model finetuning produces a larger improvement on the restaurants dataset. We think that one reason for that might be that the restaurants domain is underrepresented in the pre-training corpora of BERTBASE. Generally, we find that language model finetuning helps even if the finetuning domain does not match the evaluation domain. We think the reason for this might be that the BERT-base model is pre-trained more on knowledge-based corpora like Wikipedia than on text containing opinions. Another finding is that BERT-ADA Joint performs better on the laptops dataset than BERT-ADA Rest, although the unique amount of laptop reviews are the same in laptops- and joint-corpora. We think that confusion can be created when mixing the domains, but this needs to be investigated further. We also find that the XLNet-base baseline performs generally stronger than BERT-base and even outperforms BERT-ADA Lapt with an accuracy of $79.89\%$ on the laptops dataset.
```

Evidence location: `1908.11860:19:4`

```text
In general, the ATSC task generalizes well cross-domain, with about 2-$3\%$ drop in accuracy compared to in-domain training. We think the reason for this might be that syntactical relationships between the aspect-target and the phrase expressing sentiment polarity as well as knowing the sentiment-polarity itself are sufficient to solve the ATSC task in many cases.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-f8f396d7ded3fae45ec91ea77a1d9971732ddc9b72275701b97d48cadb0f7d33

Passage ID: `qasper-passage-v1-f8f396d7ded3fae45ec91ea77a1d9971732ddc9b72275701b97d48cadb0f7d33`; retrieval score: 7.331640619067499.

Word count: 90.

```text
In our experiments we aim to answer the following research questions (RQs):

RQ1: How does the number of training iterations in the BERT language model finetuning stage influence the ATSC end-task performance? At what point does performance start to improve, when does it converge?

RQ2: When trained in-domain, what ATSC end-task performance can be reached through fully exploitet finetuning of the BERT language model?

RQ3: When trained cross-domain in the special case of domain adaptation, what ATSC end-task performance can be reached if BERT language model finetuning is fully exploitet?
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-fa03cc74846bdbf6f7d3d7147d69ac844221a518bfbe6cd436c64998bc0ca70d

Passage ID: `qasper-passage-v1-fa03cc74846bdbf6f7d3d7147d69ac844221a518bfbe6cd436c64998bc0ca70d`; retrieval score: 3.701345501167208.

Word count: 400.

```text
The results of our experiments are shown in fig:acc-dep-lmiterations and tab:results respectively.

To answer RQ1, which is concerned with details on domain-specific language model finetuning, we can see in fig:acc-dep-lmiterations that first of all, language model finetuning has a substantial effect on ATSC end-task performance. Secondly, we see that in the laptops domain the performance starts to increase at about 10 Mio. finetuned sentences. This is an interesting insight as one would expect a relation closer to a logarithmic curve. One reason might be that it takes many steps to train knowledge into the BERT language model due to its vast amount of parameters. The model already converges at around 17 Mio. sentences. More finetuning does not improve performance significantly. In addition, we find that different runs have a high variance, the standard deviation amounts to about $1\%$ in accuracy, which justifies averaging over 9 runs to measure differences in model performance reliably.

To answer RQ2, which is concerned with in-domain ATSC performance, we see in tab:results that for the in-domain training case, our models BERT-ADA Lapt and BERT-ADA Rest achieve performance close to state-of-the-art on the laptops dataset and new state-of-the-art on the restaurants dataset with accuracies of $79.19\%$ and $87.14\%$, respectively. On the restaurants dataset, this corresponds to an absolute improvement of $2.2\%$ compared to the previous state-of-the-art method BERT-PT. Language model finetuning produces a larger improvement on the restaurants dataset. We think that one reason for that might be that the restaurants domain is underrepresented in the pre-training corpora of BERTBASE. Generally, we find that language model finetuning helps even if the finetuning domain does not match the evaluation domain. We think the reason for this might be that the BERT-base model is pre-trained more on knowledge-based corpora like Wikipedia than on text containing opinions. Another finding is that BERT-ADA Joint performs better on the laptops dataset than BERT-ADA Rest, although the unique amount of laptop reviews are the same in laptops- and joint-corpora. We think that confusion can be created when mixing the domains, but this needs to be investigated further. We also find that the XLNet-base baseline performs generally stronger than BERT-base and even outperforms BERT-ADA Lapt with an accuracy of $79.89\%$ on the laptops dataset.

To answer RQ3, which is concerned with domain adaptation, we can see in the grayed out cells in tab:results, which correspond to the cross-domain adaption case where the BERT
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.11860:19:2` | full | 0:1456 |

#### Rank 3: qasper-passage-v1-03cb5aaa998dd4710c2f58aa5589500a647574b995e19bfb9d6aa422e37e79f8

Passage ID: `qasper-passage-v1-03cb5aaa998dd4710c2f58aa5589500a647574b995e19bfb9d6aa422e37e79f8`; retrieval score: 3.3016426039216236.

Word count: 209.

```text
The datasets typically used for Aspect-Target Sentiment Classification are the SemEval 2014 Task 4 datasets BIBREF1 for the restaurants and laptops domain. Unfortunately, both datasets only have a small number of training examples. One common approach to compensate for insufficient training examples is to invent neural architectures that better model ATSC. For example, in the past a big leap in classification performance was achieved with the use of the Memory Network architecture BIBREF3, which uses memory to remember context words and explicitly models attention over both the target word and context. It was found that making full use of context words improves their model compared to previous models BIBREF2 that make use of left- and right-sided context independently.

BIBREF8 proposed Attention Encoder Networks (AEN), a modification to the transformer architecture. The authors split the Multi-Head Attention (MHA) layers into Intra-MHA and Inter-MHA layers in order to model target words and context differently, which results in a more lightweight model compared to the transformer architecture.

Another recent performance leap was achieved by BIBREF11, who model dependencies between sentiment words explicitly in sentences with more than one aspect-target by using a graph convolutional neural network. They show that their architecture performs particularly well if multiple aspects are present in a sentence.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-e9c1d820f6f01c72b5420bdb13952ac0011279d669ac0ef680395b2b06dad3da

Passage ID: `qasper-passage-v1-e9c1d820f6f01c72b5420bdb13952ac0011279d669ac0ef680395b2b06dad3da`; retrieval score: 3.2480841882634754.

Word count: 233.

```text
BERT-ADA Lapt with an accuracy of $79.89\%$ on the laptops dataset.

To answer RQ3, which is concerned with domain adaptation, we can see in the grayed out cells in tab:results, which correspond to the cross-domain adaption case where the BERT language model is trained on the target domain, that domain adaptation works well with $2.2\%$ absolute accuracy improvement on the laptops test set and even $3.6\%$ accuracy improvement on the restaurants test set compared to BERT-base.

In general, the ATSC task generalizes well cross-domain, with about 2-$3\%$ drop in accuracy compared to in-domain training. We think the reason for this might be that syntactical relationships between the aspect-target and the phrase expressing sentiment polarity as well as knowing the sentiment-polarity itself are sufficient to solve the ATSC task in many cases.

For the joint-training case, we find that combining both training datasets improves performance on both test sets. This result is intuitive, as more training data leads to better performance if the domains do not confuse each other. Interesting for the joint-training case is that the BERT-ADA Joint model performs especially strong when measured by the Macro-F1 metric. A reason for this might be that the SemEval 2014 datasets are imbalanced due to dominance of positive label. It seems like through finetuning the language model on both domains the model learns to classify the neutral class much better, especially in the laptops domain.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.11860:19:2` | partial | 1389:1456 |
| `1908.11860:19:4` | full | 0:366 |

#### Rank 5: qasper-passage-v1-52bceb13211dbf619854a0fe06d89c21b953d2fdd82d7b5922054b2752dd03b8

Passage ID: `qasper-passage-v1-52bceb13211dbf619854a0fe06d89c21b953d2fdd82d7b5922054b2752dd03b8`; retrieval score: 2.8603666813646504.

Word count: 123.

```text
We extend the work by Xu et al. by further investigating the behavior of finetuning the BERT language model in relation to ATSC performance. In particular, our contributions are:

The analysis of the influence of the amount of training-steps used for BERT language model finetuning on the Aspect-Target Sentiment Classification performance.

The findings on how to exploit BERT language model finetuning enables us to achieve new state-of-the-art performance on the SemEval 2014 restaurants dataset.

The analysis of cross-domain adaptation between the laptops and restaurants domain. Adaptation is tested by finetuning the BERT language model self-supervised on the target-domain and then supervised training on the ATSC task in the source-domain. In addition, the performance of training on the combination of both datasets is measured.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1055.

Fully covered answer annotations: 46773036407495e12fc0be2224060db32f6d6676.

Missing evidence by answer annotation:

```text
{
  "46773036407495e12fc0be2224060db32f6d6676": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: ef081d78be17ef2af792e7e919d15a235b8d7275

### Question ID and text

Question ID: `ef081d78be17ef2af792e7e919d15a235b8d7275`; paper ID: `1910.07181`.

```text
What are three downstream task datasets?
```

### Answers

#### Answer: 709376b155cf4c245d587fd6177d3ce8b4e23a32

```text
{"evidence": ["To measure the effect of adding Bertram to BERT on downstream tasks, we apply the procedure described in Section SECREF4 to a commonly used textual entailment dataset as well as two text classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. For all three datasets, we use BERT$_\\text{base}$ as a baseline model and create the substitution dictionary $S$ using the synonym relation of WordNet BIBREF20 and the pattern library BIBREF34 to make sure that all synonyms have consistent parts of speech. As an additional source of word substitutions, we make use of the misspellings dataset of BIBREF25, which is based on query logs of a search engine. To prevent misspellings from dominating the resulting dataset, we only assign misspelling-based substitutes to randomly selected 10% of the words contained in each sentence. Motivated by the results on WNLaMPro-medium, we consider every word that occurs less than 100 times in the WWC and our BooksCorpus replica combined as being rare. Some examples of entries in the resulting datasets can be seen in Table TABREF35."], "extractive_spans": ["MNLI BIBREF21", "AG's News BIBREF22", "DBPedia BIBREF23"], "free_form_answer": "", "highlighted_evidence": ["To measure the effect of adding Bertram to BERT on downstream tasks, we apply the procedure described in Section SECREF4 to a commonly used textual entailment dataset as well as two text classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. "], "unanswerable": false, "yes_no": null}
```

Evidence location: `1910.07181:11:0`

```text
To measure the effect of adding Bertram to BERT on downstream tasks, we apply the procedure described in Section SECREF4 to a commonly used textual entailment dataset as well as two text classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. For all three datasets, we use BERT$_\text{base}$ as a baseline model and create the substitution dictionary $S$ using the synonym relation of WordNet BIBREF20 and the pattern library BIBREF34 to make sure that all synonyms have consistent parts of speech. As an additional source of word substitutions, we make use of the misspellings dataset of BIBREF25, which is based on query logs of a search engine. To prevent misspellings from dominating the resulting dataset, we only assign misspelling-based substitutes to randomly selected 10% of the words contained in each sentence. Motivated by the results on WNLaMPro-medium, we consider every word that occurs less than 100 times in the WWC and our BooksCorpus replica combined as being rare. Some examples of entries in the resulting datasets can be seen in Table TABREF35.
```

#### Answer: a7eec1f4a5f97265f08cfd09b1cec20b97c573f6

```text
{"evidence": ["To measure the effect of adding Bertram to BERT on downstream tasks, we apply the procedure described in Section SECREF4 to a commonly used textual entailment dataset as well as two text classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. For all three datasets, we use BERT$_\\text{base}$ as a baseline model and create the substitution dictionary $S$ using the synonym relation of WordNet BIBREF20 and the pattern library BIBREF34 to make sure that all synonyms have consistent parts of speech. As an additional source of word substitutions, we make use of the misspellings dataset of BIBREF25, which is based on query logs of a search engine. To prevent misspellings from dominating the resulting dataset, we only assign misspelling-based substitutes to randomly selected 10% of the words contained in each sentence. Motivated by the results on WNLaMPro-medium, we consider every word that occurs less than 100 times in the WWC and our BooksCorpus replica combined as being rare. Some examples of entries in the resulting datasets can be seen in Table TABREF35."], "extractive_spans": ["MNLI", "AG's News", "DBPedia"], "free_form_answer": "", "highlighted_evidence": ["To measure the effect of adding Bertram to BERT on downstream tasks, we apply the procedure described in Section SECREF4 to a commonly used textual entailment dataset as well as two text classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1910.07181:11:0`

```text
To measure the effect of adding Bertram to BERT on downstream tasks, we apply the procedure described in Section SECREF4 to a commonly used textual entailment dataset as well as two text classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. For all three datasets, we use BERT$_\text{base}$ as a baseline model and create the substitution dictionary $S$ using the synonym relation of WordNet BIBREF20 and the pattern library BIBREF34 to make sure that all synonyms have consistent parts of speech. As an additional source of word substitutions, we make use of the misspellings dataset of BIBREF25, which is based on query logs of a search engine. To prevent misspellings from dominating the resulting dataset, we only assign misspelling-based substitutes to randomly selected 10% of the words contained in each sentence. Motivated by the results on WNLaMPro-medium, we consider every word that occurs less than 100 times in the WWC and our BooksCorpus replica combined as being rare. Some examples of entries in the resulting datasets can be seen in Table TABREF35.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-2306d3657f9d6dcaf202401855a9bcbf364f4d6723d8349f969f9b6d15cb3c2b

Passage ID: `qasper-passage-v1-2306d3657f9d6dcaf202401855a9bcbf364f4d6723d8349f969f9b6d15cb3c2b`; retrieval score: 3.3338681605187808.

Word count: 311.

```text
end-to-end fashion and directly makes use of its hidden states. By giving Bertram access to both surface form and context information already at its very lowest layer, we allow for a deep connection and exchange of information between both input signals.

For various reasons, assessing the effectiveness of methods like Bertram in a contextualized setting poses a huge difficulty: While most previous work on rare words was evaluated on datasets explicitly focusing on such words BIBREF6, BIBREF3, BIBREF4, BIBREF5, BIBREF10, all of these datasets are tailored towards context-independent embeddings and thus not suitable for evaluating our proposed model. Furthermore, understanding rare words is of negligible importance for most commonly used downstream task datasets. To evaluate our proposed model, we therefore introduce a novel procedure that allows us to automatically turn arbitrary text classification datasets into ones where rare words are guaranteed to be important. This is achieved by replacing classification-relevant frequent words with rare synonyms obtained using semantic resources such as WordNet BIBREF20.

Using this procedure, we extract rare word datasets from three commonly used text (or text pair) classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. On both the WNLaMPro dataset of BIBREF0 and all three so-obtained datasets, our proposed Bertram model outperforms previous work by a large margin.

In summary, our contributions are as follows:

We show that a pretrained BERT instance can be integrated into Attentive Mimicking, resulting in much better context representations and a deeper connection of form and context.

We design a procedure that allows us to automatically transform text classification datasets into datasets for which rare words are guaranteed to be important.

We show that Bertram achieves a new state-of-the-art on the WNLaMPro probing task BIBREF0 and beats all baselines on rare word instances of AG's News, MNLI and DBPedia, resulting in an absolute improvement of up to 24% over a BERT baseline.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-6f7713c5dd1642d1edf247945b34a9525029a93fe35024a55f14cd444cef8271

Passage ID: `qasper-passage-v1-6f7713c5dd1642d1edf247945b34a9525029a93fe35024a55f14cd444cef8271`; retrieval score: 2.7863307136373296.

Word count: 141.

```text
We have introduced Bertram, a novel architecture for relearning high-quality representations of rare words. This is achieved by employing a powerful pretrained language model and deeply connecting surface-form and context information. By replacing important words with rare synonyms, we have created various downstream task datasets focusing on rare words; on all of these datasets, Bertram improves over a BERT model without special handling of rare words, demonstrating the usefulness of our proposed method.

As our analysis has shown that even for the most frequent words considered, using Bertram is still beneficial, future work might further investigate the limits of our proposed method. Furthermore, it would be interesting to explore more complex ways of incorporating surface-form information – e.g., by using a character-level CNN similar to the one of BIBREF27 – to balance out the potency of Bertram's form and context parts.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-77f93bb70a0b62863b5f883ad2a9e560745c843cd547b1435f8704de4d9a02f6

Passage ID: `qasper-passage-v1-77f93bb70a0b62863b5f883ad2a9e560745c843cd547b1435f8704de4d9a02f6`; retrieval score: 2.394522021932808.

Word count: 400.

```text
To measure the effect of adding Bertram to BERT on downstream tasks, we apply the procedure described in Section SECREF4 to a commonly used textual entailment dataset as well as two text classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. For all three datasets, we use BERT$_\text{base}$ as a baseline model and create the substitution dictionary $S$ using the synonym relation of WordNet BIBREF20 and the pattern library BIBREF34 to make sure that all synonyms have consistent parts of speech. As an additional source of word substitutions, we make use of the misspellings dataset of BIBREF25, which is based on query logs of a search engine. To prevent misspellings from dominating the resulting dataset, we only assign misspelling-based substitutes to randomly selected 10% of the words contained in each sentence. Motivated by the results on WNLaMPro-medium, we consider every word that occurs less than 100 times in the WWC and our BooksCorpus replica combined as being rare. Some examples of entries in the resulting datasets can be seen in Table TABREF35.

Just like for WNLaMPro, our default way of injecting Bertram embeddings into the baseline model is to replace the sequence of uncontextualized WordPiece tokens for a given rare word with its Bertram-based embedding. That is, given a sequence of uncontextualized token embeddings $\mathbf {e} = e_1, \ldots , e_n$ where $e_{i}, \ldots , e_{i+j}$ with $1 \le i \le i+j \le n$ is the sequence of WordPiece embeddings for a single rare word $w$, we replace $\mathbf {e}$ with

By default, the set of contexts $\mathcal {C}$ required for this replacement is obtained by collecting all sentences from the WWC and BooksCorpus in which $w$ occurs. As our model architecture allows us to easily include new contexts without requiring any additional training, we also try a variant where we add in-domain contexts by giving the model access to the texts found in the test set.

In addition to the procedure described above, we also try a variant where instead of replacing the original WordPiece embeddings for a given rare word, we merely add the Bertram-based embedding, separating both representations using a single slash:

As it performs best on the rare and medium subsets of WNLaMPro combined, we use only the add-gated variant of Bertram for all datasets. Results can be seen in Table TABREF37, where for each task, we report the accuracy on the entire dataset as
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1910.07181:11:0` | full | 0:1092 |

#### Rank 4: qasper-passage-v1-4c9f1c64bc25729f23de634d47ad4aebbf40d86754fa5124908e992736aa245e

Passage ID: `qasper-passage-v1-4c9f1c64bc25729f23de634d47ad4aebbf40d86754fa5124908e992736aa245e`; retrieval score: 1.8122495709969306.

Word count: 275.

```text
on the rare and medium subsets of WNLaMPro combined, we use only the add-gated variant of Bertram for all datasets. Results can be seen in Table TABREF37, where for each task, we report the accuracy on the entire dataset as well as scores obtained considering only instances where at least one word was replaced by a misspelling or a WordNet synonym, respectively. Consistent with results on WNLaMPro, combining BERT with Bertram outperforms both a standalone BERT model and one combined with Attentive Mimicking across all tasks. While keeping the original BERT embeddings in addition to Bertram's representation brings no benefit, adding in-domain data clearly helps for two out of three datasets. This makes sense as for rare words, every single additional context can be crucial for gaining a deeper understanding.

To further understand for which words using Bertram is helpful, in Figure FIGREF39 we look at the accuracy of BERT both with and without Bertram on all three tasks as a function of word frequency. That is, we compute the accuracy scores for both models when considering only entries $(\mathbf {x}_{w_{i_1} = \hat{w}_{i_1}, \ldots , w_{i_k} = \hat{w}_{i_k} }, y)$ where each substituted word $\hat{w}_{i_j}$ occurs less than $c_\text{max}$ times in WWC and BooksCorpus, for various values of $c_\text{max}$. As one would expect, $c_\text{max}$ is positively correlated with the accuracies of both models, showing that the rarer a word is, the harder it is to understand. Perhaps more interestingly, for all three datasets the gap between Bertram and BERT remains more or less constant regardless of $c_\text{max}$. This indicates that using Bertram might also be useful for even more frequent words than the ones considered.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-a923bcc42872f430decfc29734aba0a6592f910bd9814e7c19d60fb90e746b27

Passage ID: `qasper-passage-v1-a923bcc42872f430decfc29734aba0a6592f910bd9814e7c19d60fb90e746b27`; retrieval score: 1.7143957878720606.

Word count: 170.

```text
For our evaluation of Bertram, we largely follow the experimental setup of BIBREF0. Our implementation of Bertram is based on PyTorch BIBREF30 and the Transformers library of BIBREF31. Throughout all of our experiments, we use BERT$_\text{base}$ as the underlying language model for Bertram. To obtain embeddings for frequent multi-token words during training, we use one-token approximation BIBREF0. Somewhat surprisingly, we found in preliminary experiments that excluding BERT's parameters from the finetuning procedure outlined in Section SECREF17 improves performance while speeding up training; we thus exclude them in the third step of our training procedure.

While BERT was trained on BooksCorpus BIBREF32 and a large Wikipedia dump, we follow previous work and train Bertram on only the much smaller Westbury Wikipedia Corpus (WWC) BIBREF33; this of course gives BERT a clear advantage over our proposed method. In order to at least partially compensate for this, in our downstream task experiments we gather the set of contexts $\mathcal {C}$ for a given rare word from both the WWC and BooksCorpus during inference.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1297.

Fully covered answer annotations: 709376b155cf4c245d587fd6177d3ce8b4e23a32, a7eec1f4a5f97265f08cfd09b1cec20b97c573f6.

Missing evidence by answer annotation:

```text
{
  "709376b155cf4c245d587fd6177d3ce8b4e23a32": {
    "unresolved_evidence": [],
    "paragraphs": {}
  },
  "a7eec1f4a5f97265f08cfd09b1cec20b97c573f6": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: 537b2d7799124d633892a1ef1a485b3b071b303d

### Question ID and text

Question ID: `537b2d7799124d633892a1ef1a485b3b071b303d`; paper ID: `1910.07181`.

```text
What is dataset for word probing task?
```

### Answers

#### Answer: 0055f1c704b2380b3f9692330601906890b9b49d

```text
{"evidence": ["We evalute Bertram on the WNLaMPro dataset of BIBREF0. This dataset consists of cloze-style phrases like"], "extractive_spans": ["WNLaMPro dataset"], "free_form_answer": "", "highlighted_evidence": ["We evalute Bertram on the WNLaMPro dataset of BIBREF0."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1910.07181:10:0`

```text
We evalute Bertram on the WNLaMPro dataset of BIBREF0. This dataset consists of cloze-style phrases like
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-2306d3657f9d6dcaf202401855a9bcbf364f4d6723d8349f969f9b6d15cb3c2b

Passage ID: `qasper-passage-v1-2306d3657f9d6dcaf202401855a9bcbf364f4d6723d8349f969f9b6d15cb3c2b`; retrieval score: 4.307277817507901.

Word count: 311.

```text
end-to-end fashion and directly makes use of its hidden states. By giving Bertram access to both surface form and context information already at its very lowest layer, we allow for a deep connection and exchange of information between both input signals.

For various reasons, assessing the effectiveness of methods like Bertram in a contextualized setting poses a huge difficulty: While most previous work on rare words was evaluated on datasets explicitly focusing on such words BIBREF6, BIBREF3, BIBREF4, BIBREF5, BIBREF10, all of these datasets are tailored towards context-independent embeddings and thus not suitable for evaluating our proposed model. Furthermore, understanding rare words is of negligible importance for most commonly used downstream task datasets. To evaluate our proposed model, we therefore introduce a novel procedure that allows us to automatically turn arbitrary text classification datasets into ones where rare words are guaranteed to be important. This is achieved by replacing classification-relevant frequent words with rare synonyms obtained using semantic resources such as WordNet BIBREF20.

Using this procedure, we extract rare word datasets from three commonly used text (or text pair) classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. On both the WNLaMPro dataset of BIBREF0 and all three so-obtained datasets, our proposed Bertram model outperforms previous work by a large margin.

In summary, our contributions are as follows:

We show that a pretrained BERT instance can be integrated into Attentive Mimicking, resulting in much better context representations and a deeper connection of form and context.

We design a procedure that allows us to automatically transform text classification datasets into datasets for which rare words are guaranteed to be important.

We show that Bertram achieves a new state-of-the-art on the WNLaMPro probing task BIBREF0 and beats all baselines on rare word instances of AG's News, MNLI and DBPedia, resulting in an absolute improvement of up to 24% over a BERT baseline.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-21ae161bd20334b405c76f348ad275e69ec6c977cce2a642d46a2d536e043fd3

Passage ID: `qasper-passage-v1-21ae161bd20334b405c76f348ad275e69ec6c977cce2a642d46a2d536e043fd3`; retrieval score: 4.116746579676923.

Word count: 400.

```text
As traditional word embedding algorithms BIBREF1 are known to struggle with rare words, several techniques for improving their representations have been proposed over the last few years. These approaches exploit either the contexts in which rare words occur BIBREF2, BIBREF3, BIBREF4, BIBREF5, their surface-form BIBREF6, BIBREF7, BIBREF8, or both BIBREF9, BIBREF10. However, all of these approaches are designed for and evaluated on uncontextualized word embeddings.

With the recent shift towards contextualized representations obtained from pretrained deep language models BIBREF11, BIBREF12, BIBREF13, BIBREF14, the question naturally arises whether these approaches are facing the same problem. As all of them already handle rare words implicitly – using methods such as byte-pair encoding BIBREF15 and WordPiece embeddings BIBREF16, or even character-level CNNs BIBREF17 –, it is unclear whether these models even require special treatment of rare words. However, the listed methods only make use of surface-form information, whereas BIBREF9 found that for covering a wide range of rare words, it is crucial to consider both surface-form and contexts.

Consistently, BIBREF0 recently showed that for BERT BIBREF13, a popular pretrained language model based on a Transformer architecture BIBREF18, performance on a rare word probing task can significantly be improve by relearning representations of rare words using Attentive Mimicking BIBREF19. However, their proposed model is limited in two important respects:

For processing contexts, it uses a simple bag-of-words model, throwing away much of the available information.

It combines form and context only in a shallow fashion, thus preventing both input signals from sharing information in any sophisticated manner.

Importantly, this limitation applies not only to their model, but to all previous work on obtaining representations for rare words by leveraging form and context. While using bag-of-words models is a reasonable choice for uncontextualized embeddings, which are often themselves based on such models BIBREF1, BIBREF7, it stands to reason that they are suboptimal for contextualized embeddings based on position-aware deep neural architectures.

To overcome these limitations, we introduce Bertram (BERT for Attentive Mimicking), a novel architecture for understanding rare words that combines a pretrained BERT language model with Attentive Mimicking BIBREF19. Unlike previous approaches making use of language models BIBREF5, our approach integrates BERT in an end-to-end fashion and directly makes use of its hidden states. By giving Bertram access to both surface form and context information already at its very lowest layer, we allow for a deep connection and exchange of information between both input
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-4c9f1c64bc25729f23de634d47ad4aebbf40d86754fa5124908e992736aa245e

Passage ID: `qasper-passage-v1-4c9f1c64bc25729f23de634d47ad4aebbf40d86754fa5124908e992736aa245e`; retrieval score: 3.047869834505952.

Word count: 275.

```text
on the rare and medium subsets of WNLaMPro combined, we use only the add-gated variant of Bertram for all datasets. Results can be seen in Table TABREF37, where for each task, we report the accuracy on the entire dataset as well as scores obtained considering only instances where at least one word was replaced by a misspelling or a WordNet synonym, respectively. Consistent with results on WNLaMPro, combining BERT with Bertram outperforms both a standalone BERT model and one combined with Attentive Mimicking across all tasks. While keeping the original BERT embeddings in addition to Bertram's representation brings no benefit, adding in-domain data clearly helps for two out of three datasets. This makes sense as for rare words, every single additional context can be crucial for gaining a deeper understanding.

To further understand for which words using Bertram is helpful, in Figure FIGREF39 we look at the accuracy of BERT both with and without Bertram on all three tasks as a function of word frequency. That is, we compute the accuracy scores for both models when considering only entries $(\mathbf {x}_{w_{i_1} = \hat{w}_{i_1}, \ldots , w_{i_k} = \hat{w}_{i_k} }, y)$ where each substituted word $\hat{w}_{i_j}$ occurs less than $c_\text{max}$ times in WWC and BooksCorpus, for various values of $c_\text{max}$. As one would expect, $c_\text{max}$ is positively correlated with the accuracies of both models, showing that the rarer a word is, the harder it is to understand. Perhaps more interestingly, for all three datasets the gap between Bertram and BERT remains more or less constant regardless of $c_\text{max}$. This indicates that using Bertram might also be useful for even more frequent words than the ones considered.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-77f93bb70a0b62863b5f883ad2a9e560745c843cd547b1435f8704de4d9a02f6

Passage ID: `qasper-passage-v1-77f93bb70a0b62863b5f883ad2a9e560745c843cd547b1435f8704de4d9a02f6`; retrieval score: 2.9317133181214388.

Word count: 400.

```text
To measure the effect of adding Bertram to BERT on downstream tasks, we apply the procedure described in Section SECREF4 to a commonly used textual entailment dataset as well as two text classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. For all three datasets, we use BERT$_\text{base}$ as a baseline model and create the substitution dictionary $S$ using the synonym relation of WordNet BIBREF20 and the pattern library BIBREF34 to make sure that all synonyms have consistent parts of speech. As an additional source of word substitutions, we make use of the misspellings dataset of BIBREF25, which is based on query logs of a search engine. To prevent misspellings from dominating the resulting dataset, we only assign misspelling-based substitutes to randomly selected 10% of the words contained in each sentence. Motivated by the results on WNLaMPro-medium, we consider every word that occurs less than 100 times in the WWC and our BooksCorpus replica combined as being rare. Some examples of entries in the resulting datasets can be seen in Table TABREF35.

Just like for WNLaMPro, our default way of injecting Bertram embeddings into the baseline model is to replace the sequence of uncontextualized WordPiece tokens for a given rare word with its Bertram-based embedding. That is, given a sequence of uncontextualized token embeddings $\mathbf {e} = e_1, \ldots , e_n$ where $e_{i}, \ldots , e_{i+j}$ with $1 \le i \le i+j \le n$ is the sequence of WordPiece embeddings for a single rare word $w$, we replace $\mathbf {e}$ with

By default, the set of contexts $\mathcal {C}$ required for this replacement is obtained by collecting all sentences from the WWC and BooksCorpus in which $w$ occurs. As our model architecture allows us to easily include new contexts without requiring any additional training, we also try a variant where we add in-domain contexts by giving the model access to the texts found in the test set.

In addition to the procedure described above, we also try a variant where instead of replacing the original WordPiece embeddings for a given rare word, we merely add the Bertram-based embedding, separating both representations using a single slash:

As it performs best on the rare and medium subsets of WNLaMPro combined, we use only the add-gated variant of Bertram for all datasets. Results can be seen in Table TABREF37, where for each task, we report the accuracy on the entire dataset as
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-05216621e58b05472b77b05cf51c33254d08b72acb92cbf01f7b5b7d380547cb

Passage ID: `qasper-passage-v1-05216621e58b05472b77b05cf51c33254d08b72acb92cbf01f7b5b7d380547cb`; retrieval score: 2.5428074139210812.

Word count: 282.

```text
Incorporating surface-form information (e.g., morphemes, characters or character $n$-grams) is a commonly used technique for improving word representations. For context-independent word embeddings, this information can either be injected into a given embedding space BIBREF6, BIBREF8, or a model can directly be given access to it during training BIBREF7, BIBREF24, BIBREF25. In the area of contextualized representations, many architectures employ subword segmentation methods BIBREF12, BIBREF13, BIBREF26, BIBREF14, whereas others use convolutional neural networks to directly access character-level information BIBREF27, BIBREF11, BIBREF17.

Complementary to surface form, another useful source of information for understanding rare words are the contexts in which they occur BIBREF2, BIBREF3, BIBREF4. As recently shown by BIBREF19, BIBREF9, combining form and context leads to significantly better results than using just one of both input signals for a wide range of tasks. While all aforementioned methods are based on simple bag-of-words models, BIBREF5 recently proposed an architecture based on the context2vec language model BIBREF28. However, in contrast to our work, they (i) do not incorporate surface-form information and (ii) do not directly access the hidden states of the language model, but instead simply use its output distribution.

There are several datasets explicitly focusing on rare words, e.g. the Stanford Rare Word dataset of BIBREF6, the Definitional Nonce dataset of BIBREF3 and the Contextual Rare Word dataset BIBREF4. However, all of these datasets are only suitable for evaluating context-independent word representations.

Our proposed method of generating rare word datasets is loosely related to adversarial example generation methods such as HotFlip BIBREF29, which manipulate the input to change a model's prediction. We use a similar mechanism to determine which words in a given sentence are most important and replace these words with rare synonyms.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1668.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "0055f1c704b2380b3f9692330601906890b9b49d": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1910.07181:10:0": [
        [
          0,
          104
        ]
      ]
    }
  }
}
```

## Question: e74ba39c35af53d3960be5a6c86eddd62cef859f

### Question ID and text

Question ID: `e74ba39c35af53d3960be5a6c86eddd62cef859f`; paper ID: `2002.00317`.

```text
Which baseline performs best?
```

### Answers

#### Answer: 83bb414e88a59542134862e646f33922ed54f2a1

```text
{"evidence": ["Statistical significance is assessed for select results using bootstrapping with 1000 samples in each of 100 iterations. This test shows that conditioning on the introduction of the source document improves performance compared to conditioning on the abstract when using the SciGPT2 model. However, we see that IR methods perform better than the best neural models. We do not find enough evidence to reject the null hypothesis regarding what context from the cited document should be used."], "extractive_spans": ["IR methods perform better than the best neural models"], "free_form_answer": "", "highlighted_evidence": ["However, we see that IR methods perform better than the best neural models. We do not find enough evidence to reject the null hypothesis regarding what context from the cited document should be used."], "unanswerable": false, "yes_no": null}
```

Evidence location: `2002.00317:7:3`

```text
Statistical significance is assessed for select results using bootstrapping with 1000 samples in each of 100 iterations. This test shows that conditioning on the introduction of the source document improves performance compared to conditioning on the abstract when using the SciGPT2 model. However, we see that IR methods perform better than the best neural models. We do not find enough evidence to reject the null hypothesis regarding what context from the cited document should be used.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-b0196b26649b861436b012dcfe5fce671d68eacbb0150d3c66bcfe11845cd23e

Passage ID: `qasper-passage-v1-b0196b26649b861436b012dcfe5fce671d68eacbb0150d3c66bcfe11845cd23e`; retrieval score: 3.6372610980333206.

Word count: 285.

```text
We compare the different baseline systems using BLEU BIBREF12, ROUGE (specifically ROUGE 1, 2, and L; BIBREF13), and the recently introduced BertScore BIBREF14, a similarity metric based on BERT embeddings which has been shown to correlate well with human judgements on other tasks. To adapt the BertScore metric to the scientific text domain, we use SciBERT embeddings.

Table TABREF7 (above the double line) shows the performance of the SciGPT2 model on the test set when provided with the different input context combinations outlined in Section SECREF5. We find that context does make a difference for this category of model, and that models which have access to the intro of the documents outperform those which use abstracts or sampling.

Automatic evaluation of the retrieval-based methods on the test data are shown below the double line in Table TABREF7. This table shows that the retrieval methods perform well on this task. However we will show the limitations of these automatic metrics in Section SECREF14. We also observe that tuning the $\alpha $ and $\beta $ parameters on the validation set results in overfitting for this method. Outputs are largely unchanged by this tuning; fewer than 400 test datapoints differ from the untuned outputs. A larger validation split may alleviate this problem.

Statistical significance is assessed for select results using bootstrapping with 1000 samples in each of 100 iterations. This test shows that conditioning on the introduction of the source document improves performance compared to conditioning on the abstract when using the SciGPT2 model. However, we see that IR methods perform better than the best neural models. We do not find enough evidence to reject the null hypothesis regarding what context from the cited document should be used.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2002.00317:7:3` | full | 0:489 |

#### Rank 2: qasper-passage-v1-a274e233fb8bb525774d51731247428ecccc5bfb307d76a20ec28a7d0727c0a0

Passage ID: `qasper-passage-v1-a274e233fb8bb525774d51731247428ecccc5bfb307d76a20ec28a7d0727c0a0`; retrieval score: 3.1145351693449275.

Word count: 123.

```text
The primary question we investigate with this model is what kind of input is best for generating accurate and informative citation sentences. Prior works in citation recommendation have made use of abstracts, which perhaps act as sufficient summaries of document content for this task. Additionally, we explore variants of extended context, such as the introduction or first section after the abstract. Since scientific texts are too long to fit into the context window of our generation model, we also investigate a “sampling” approach which samples sentences from throughout the document until the context window is full. In this work, we combine either the abstract or introduction of the source document with each of the abstract, introduction, or sampled sentences from the cited document.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-7f100e9dcc03b30e6bf71f4ecfb1a531f8e1d7f3eaf581fabd385b8a3aa11104

Passage ID: `qasper-passage-v1-7f100e9dcc03b30e6bf71f4ecfb1a531f8e1d7f3eaf581fabd385b8a3aa11104`; retrieval score: 2.504242980915986.

Word count: 158.

```text
and nuanced relationships between related scientific works.

In this work, we introduce the task of citation text generation. Leveraging the full texts of English-language scientific articles, we construct a dataset of citation sentences in the computer science domain for training and evaluating citation text generation models. We investigate strong retrieval and neural baseline models against which future work can compare. For use cases where large models can be trained, we extend the successful GPT2 architecture BIBREF6 to the scientific domain with additional pre-training and subsequent fine-tuning on the citation generation task. We experiment with different kinds of document context in the fine-tuning and inference stages. We also explore retrieval-based techniques which may more easily generalize to lower-resource settings. These models retrieve citation sentences from training documents which are most similar to test inputs. Our evaluations show that these techniques often produce plausible citation sentences, but indicate clear directions for improvement. Code and artifacts are provided for future research.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-aa8ed3b1eaa88a4f0414d3a44af2e0a92296c28eb62cccbd1ae861149a67702f

Passage ID: `qasper-passage-v1-aa8ed3b1eaa88a4f0414d3a44af2e0a92296c28eb62cccbd1ae861149a67702f`; retrieval score: 1.6681753880745698.

Word count: 157.

```text
The fluency and topical relevance of the baseline models show the plausibility of the citation text generation task as well as the utility of including pretrained scientific language models in future models. But based on the kinds of errors we have seen, future work should focus on two complementary goals: ensuring the factual accuracy of the generated text and improved modeling of the cited document. Factual accuracy is difficult to enforce in statistical text generation systems, especially where inference includes sampling procedures. Grounding to knowledge bases could help. For this task, knowledge extracted from candidate generations could be compared with knowledge from the full source and cited documents to prune false or irrelevant statements. Further, modeling input documents as knowledge graphs of their contents may help these algorithms better understand the cited document, resulting in better outputs. However, such a model will have to address the open problem of combining pretrained language models with graph encoding techniques.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-077c7b3650800602e247800963dbacdfce7ed09c7d6933c8d21bc356d420af85

Passage ID: `qasper-passage-v1-077c7b3650800602e247800963dbacdfce7ed09c7d6933c8d21bc356d420af85`; retrieval score: 0.8426029469042182.

Word count: 178.

```text
GPT2-based models have demonstrated an ability to capture long distance dependencies over hundreds of tokens, which we hypothesize will allow them to synthesize information in both the source and cited documents. But citation text generation models must also handle the challenging technical vocabulary of the scientific domain.

Prior work has shown that pretraining on in-domain data improves the performance of large language models on domain-specific tasks BIBREF11. Inspired by this, we experiment with additional pretraining of GPT2 in the science domain. This model, SciGPT2, is trained for an additional 3 epochs over the full text of the documents in our corpus using a language modeling objective. We note that both SciGPT2 and the SciBERT language models used here have been exposed to citing sentences from the test and validation sets as in-line citations during their pre-training phases, which may improve their performance versus models without this exposure. Such exposure is typical when using pretrained language models, as text from test data cannot be guaranteed to be absent from the large task-independent corpora upon which these models are trained.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 901.

Fully covered answer annotations: 83bb414e88a59542134862e646f33922ed54f2a1.

Missing evidence by answer annotation:

```text
{
  "83bb414e88a59542134862e646f33922ed54f2a1": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: b1ce129678e37070e69f01332f1a8587e18e06b0

### Question ID and text

Question ID: `b1ce129678e37070e69f01332f1a8587e18e06b0`; paper ID: `1610.09225`.

```text
What dataset is used to train the model?
```

### Answers

#### Answer: d03bc79638cb60b59ac4b7c9714e11b6ed56e136

```text
{"evidence": ["A total of 2,50,000 tweets over a period of August 31st, 2015 to August 25th,2016 on Microsoft are extracted from twitter API BIBREF15 . Twitter4J is a java application which helps us to extract tweets from twitter. The tweets were collected using Twitter API and filtered using keywords like $ MSFT, # Microsoft, #Windows etc. Not only the opinion of public about the company's stock but also the opinions about products and services offered by the company would have a significant impact and are worth studying. Based on this principle, the keywords used for filtering are devised with extensive care and tweets are extracted in such a way that they represent the exact emotions of public about Microsoft over a period of time. The news on twitter about Microsoft and tweets regarding the product releases were also included. Stock opening and closing prices of Microsoft from August 31st, 2015 to August 25th, 2016 are obtained from Yahoo! Finance BIBREF16 ."], "extractive_spans": ["2,50,000 tweets", "Stock opening and closing prices of Microsoft from August 31st, 2015 to August 25th, 2016"], "free_form_answer": "", "highlighted_evidence": ["A total of 2,50,000 tweets over a period of August 31st, 2015 to August 25th,2016 on Microsoft are extracted from twitter API BIBREF15 .", "The news on twitter about Microsoft and tweets regarding the product releases were also included. Stock opening and closing prices of Microsoft from August 31st, 2015 to August 25th, 2016 are obtained from Yahoo! Finance BIBREF16 ."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1610.09225:2:0`

```text
A total of 2,50,000 tweets over a period of August 31st, 2015 to August 25th,2016 on Microsoft are extracted from twitter API BIBREF15 . Twitter4J is a java application which helps us to extract tweets from twitter. The tweets were collected using Twitter API and filtered using keywords like $ MSFT, # Microsoft, #Windows etc. Not only the opinion of public about the company's stock but also the opinions about products and services offered by the company would have a significant impact and are worth studying. Based on this principle, the keywords used for filtering are devised with extensive care and tweets are extracted in such a way that they represent the exact emotions of public about Microsoft over a period of time. The news on twitter about Microsoft and tweets regarding the product releases were also included. Stock opening and closing prices of Microsoft from August 31st, 2015 to August 25th, 2016 are obtained from Yahoo! Finance BIBREF16 .
```

#### Answer: e7e7b0b7a2ecb7db738187755f4f71de067d1dd8

```text
{"evidence": ["A total of 2,50,000 tweets over a period of August 31st, 2015 to August 25th,2016 on Microsoft are extracted from twitter API BIBREF15 . Twitter4J is a java application which helps us to extract tweets from twitter. The tweets were collected using Twitter API and filtered using keywords like $ MSFT, # Microsoft, #Windows etc. Not only the opinion of public about the company's stock but also the opinions about products and services offered by the company would have a significant impact and are worth studying. Based on this principle, the keywords used for filtering are devised with extensive care and tweets are extracted in such a way that they represent the exact emotions of public about Microsoft over a period of time. The news on twitter about Microsoft and tweets regarding the product releases were also included. Stock opening and closing prices of Microsoft from August 31st, 2015 to August 25th, 2016 are obtained from Yahoo! Finance BIBREF16 ."], "extractive_spans": [], "free_form_answer": "Collected tweets and opening and closing stock prices of Microsoft.", "highlighted_evidence": ["A total of 2,50,000 tweets over a period of August 31st, 2015 to August 25th,2016 on Microsoft are extracted from twitter API BIBREF15 .", "Stock opening and closing prices of Microsoft from August 31st, 2015 to August 25th, 2016 are obtained from Yahoo! Finance BIBREF16 ."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1610.09225:2:0`

```text
A total of 2,50,000 tweets over a period of August 31st, 2015 to August 25th,2016 on Microsoft are extracted from twitter API BIBREF15 . Twitter4J is a java application which helps us to extract tweets from twitter. The tweets were collected using Twitter API and filtered using keywords like $ MSFT, # Microsoft, #Windows etc. Not only the opinion of public about the company's stock but also the opinions about products and services offered by the company would have a significant impact and are worth studying. Based on this principle, the keywords used for filtering are devised with extensive care and tweets are extracted in such a way that they represent the exact emotions of public about Microsoft over a period of time. The news on twitter about Microsoft and tweets regarding the product releases were also included. Stock opening and closing prices of Microsoft from August 31st, 2015 to August 25th, 2016 are obtained from Yahoo! Finance BIBREF16 .
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-ff9abbf1843cc31674d4688a644b2ee21030b39d8a7eb815f59f6c1105fcc64d

Passage ID: `qasper-passage-v1-ff9abbf1843cc31674d4688a644b2ee21030b39d8a7eb815f59f6c1105fcc64d`; retrieval score: 5.567229565449405.

Word count: 158.

```text
The stock price data of Microsoft are labeled suitably for training using a simple program. If the previous day stock price is more than the current day stock price, the current day is marked with a numeric value of 0, else marked with a numeric value of 1. Now, this correlation analysis turns out to be a classification problem. The total positive, negative and neutral emotions in tweets in a 3 day period are calculated successively which are used as features for the classifier model and the output is the labeled next day value of stock 0 or 1.The window size is experimented and best results are achieved when the sentiment values precede 3 days to the stock price. A total of 355 instances, each with 3 attributes are fed to the classifier with a split proportions of 80% train dataset and the remaining dataset for testing. The accuracy of the classifier is discussed in the results section.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-e1e91bb90e624d207d7a50d232abaf3e354c2d824b66242bac4dea2ee135e7a5

Passage ID: `qasper-passage-v1-e1e91bb90e624d207d7a50d232abaf3e354c2d824b66242bac4dea2ee135e7a5`; retrieval score: 5.2352423353006134.

Word count: 141.

```text
A classifier is presented in the previous sections that is trained with aggregate sentiment values for 3-day period as features and the increase/decrease in stock price represented by 1/0 as the output. Total data is split into two parts, 80 percent to train the model and remaining for testing operations. The classifier results show an accuracy value of 69.01% when trained using Logistic regression algorithm and the accuracy rate varied with the training set. When the model with LibSVM is trained with 90 percent of data, it gave a result of 71.82%. These results give a significant edge to the investors and they show good correlation between stock market movements and the sentiments of public expressed in twitter. This trend shows that with increasing dataset the models are performing well. We would like to incorporate more data in our future work.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-1095c53900acc2dd9fe389798d15298a47c790788abbaebdb7b5fe28876e96bc

Passage ID: `qasper-passage-v1-1095c53900acc2dd9fe389798d15298a47c790788abbaebdb7b5fe28876e96bc`; retrieval score: 4.74999196052175.

Word count: 218.

```text
The above sections discussed the method followed to train the classifier used for sentiment analysis of tweets. The classifier with features as Word2vec representations of human annotated tweets trained on Random Forest algorithm with a split percentage of 90 for training the model and remaining for testing the model showed an accuracy of 70.2%. With N-gram representations, the classifier model with same algorithm and with same dataset showed an accuracy of 70.5%. Though the results are very close, model trained with word2vec representations is picked to classify the nonhuman annotated tweets because of its promising accuracy for large datasets and the sustainability in word meaning. Numerous studies have been conducted on people and they concluded that the rate of human concordance, that is the degree of agreement among humans on the sentiment of a text, is between 70% and 79% BIBREF21 . They have also synthesized that sentiment analyzers above 70% are very accurate in most of the cases. Provided this information, the results we obtained from the sentiment classification can be observed as very good figures while predicting the sentiments in short texts, tweets, less than 140 characters in length. Table-2 depicts the results of sentiment classification including accuracy, precision, F-measure and recall when trained with different machine learning algorithms. ROC curves are plotted for detailed analysis.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-9ebc6cd0e8f276cdfd258a969aee0349d2ce750448c023f3652ada2a841e7873

Passage ID: `qasper-passage-v1-9ebc6cd0e8f276cdfd258a969aee0349d2ce750448c023f3652ada2a841e7873`; retrieval score: 4.095916148793189.

Word count: 125.

```text
In this work, we have considered only twitter data for analyzing people's sentiment which may be biased because not all the people who trade in stocks share their opinions on twitter. Stocktwits BIBREF22 is a financial communication platform designed solely for sharing ideas and insights of investors, entrepreneurs and traders. The current study can be extended by incorporating stocktwits data. In addition to this, data from news can also be included for an exhaustive public opinion collection.

While training the sentiment analyzer, 3,216 tweets are used which is comparatively a less number to train a sentiment analyzer. In future, we look forward to human annotate more than 10,000 tweets and train the classifiers. With increasing size of training datasets, the models tend to perform better.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-86e50a3d614e26e9dba8c952efbd21b9c01d6f42801b6da920b79a9f5c133e1e

Passage ID: `qasper-passage-v1-86e50a3d614e26e9dba8c952efbd21b9c01d6f42801b6da920b79a9f5c133e1e`; retrieval score: 3.4162504132736764.

Word count: 266.

```text
The most well-known publication in this area is by Bollen BIBREF10 . They investigated whether the collective mood states of public (Happy, calm, Anxiety) derived from twitter feeds are correlated to the value of the Dow Jones Industrial Index. They used a Fuzzy neural network for their prediction. Their results show that public mood states in twitter are strongly correlated with Dow Jones Industrial Index. Chen and Lazer BIBREF11 derived investment strategies by observing and classifying the twitter feeds. Bing et al. BIBREF12 studied the tweets and concluded the predictability of stock prices based on the type of industry like Finance, IT etc. Zhang BIBREF13 found out a high negative correlation between mood states like hope, fear and worry in tweets with the Dow Jones Average Index. Recently, Brian et al. BIBREF14 investigated the correlation of sentiments of public with stock increase and decreases using Pearson correlation coefficient for stocks. In this paper, we took a novel approach of predicting rise and fall in stock prices based on the sentiments extracted from twitter to find the correlation. The core contribution of our work is the development of a sentiment analyzer which works better than the one in Brian's work and a novel approach to find the correlation. Sentiment analyzer is used to classify the sentiments in tweets extracted.The human annotated dataset in our work is also exhaustive. We have shown that a strong correlation exists between twitter sentiments and the next day stock prices in the results section. We did so by considering the tweets and stock opening and closing prices of Microsoft over a year.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 908.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "d03bc79638cb60b59ac4b7c9714e11b6ed56e136": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1610.09225:2:0": [
        [
          0,
          961
        ]
      ]
    }
  },
  "e7e7b0b7a2ecb7db738187755f4f71de067d1dd8": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1610.09225:2:0": [
        [
          0,
          961
        ]
      ]
    }
  }
}
```

## Question: 5a2f7e27efdedf3c43498ff0c32f808d406c42ec

### Question ID and text

Question ID: `5a2f7e27efdedf3c43498ff0c32f808d406c42ec`; paper ID: `1704.00939`.

```text
What embeddings do they use?
```

### Answers

#### Answer: 527a86257787c039331092a3217b16a2f0847649

```text
{"evidence": ["Our contribution leverages pre-trained word embeddings (GloVe, trained on wikipedia+gigaword corpus), the DepecheMood affective lexicon, and convolutional neural networks."], "extractive_spans": ["GloVe"], "free_form_answer": "", "highlighted_evidence": ["Our contribution leverages pre-trained word embeddings (GloVe, trained on wikipedia+gigaword corpus), the DepecheMood affective lexicon, and convolutional neural networks."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1704.00939:0:3`

```text
Our contribution leverages pre-trained word embeddings (GloVe, trained on wikipedia+gigaword corpus), the DepecheMood affective lexicon, and convolutional neural networks.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-c55a30f3c461e80f4ee47537b21596e170e735d2e17aee4fef46f8d2bc2addc1

Passage ID: `qasper-passage-v1-c55a30f3c461e80f4ee47537b21596e170e735d2e17aee4fef46f8d2bc2addc1`; retrieval score: 2.0340778828157355.

Word count: 79.

```text
While image and sound come with a natural high dimensional embedding, the issue of which is the best representation is still an open research problem in the context of natural language and text. It is beyond the scope of this paper to do a thorough overview of word representations, for this we refer the interest reader to the excellent review provided by BIBREF1 . Here, we will just introduce the main representations that are related to the proposed method.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-37624ec9b767a81a8c2560fa38d8ee73c56cd7798def818fc3196ed0175c89fc

Passage ID: `qasper-passage-v1-37624ec9b767a81a8c2560fa38d8ee73c56cd7798def818fc3196ed0175c89fc`; retrieval score: 1.8269804272218573.

Word count: 101.

```text
In this paper, we presented the network architecture used for the Fortia-FBK submission to the Semeval-2017 Task 5, Subtask 2 challenge, with the goal of predicting positive (bullish) or negative (bearish) attitude towards a target brand from financial news headlines. The proposed system ranked 1st in such challenge.

Our approach is based on 1d convolutions and uses fine-tuning of unsupervised word representations and a rule based sentiment model in its inputs. We showed that the use of pre-computed word representations allows to reduce over-fitting and to achieve significantly better generalization, while some basic pre-processing was needed to further improve the performance.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-0f410e5017e9b0f17270921e7d3ce93a6d60e1a5ffa571023601f3639185291f

Passage ID: `qasper-passage-v1-0f410e5017e9b0f17270921e7d3ce93a6d60e1a5ffa571023601f3639185291f`; retrieval score: 0.0.

Word count: 81.

```text
The data consists of a set of financial news headlines, crawled from several online outlets such as Yahoo Finance, where each sentence contains one or more company names/brands.

Each tuple (headline, company) is annotated with a sentiment score ranging from -1 (very negative, bearish) to 1 (very positive, bullish). The training/test sets provided contain 1142 and 491 annotated sentences, respectively.

A sample instance is reported below:

Headline: “Morrisons book second consecutive quarter of sales growth”

Company name: “Morrisons”

Sentiment score: 0.43
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-260014c6d6b23af0996ec210e854fa91ec10007cb01126e956c9a9185c260c91

Passage ID: `qasper-passage-v1-260014c6d6b23af0996ec210e854fa91ec10007cb01126e956c9a9185c260c91`; retrieval score: 0.0.

Word count: 194.

```text
Minimal preprocessing was adopted in our approach: we replaced the target company's name with a fixed word <company> and numbers with <number>. The sentences were then tokenized using spaces as separator and keeping punctuation symbols as separate tokens.

The words are represented as fixed length vectors INLINEFORM0 resulting from the concatenation of GloVe pre-trained embeddings and DepecheMood BIBREF19 lexicon representation. Since we cannot directly concatenate token-based embeddings (provided in GloVe) with the lemma#PoS-based representation available in DepecheMood, we proceeded to re-build the latter in token-based form, applying the exact same methodology albeit with two differences: we started from a larger dataset (51.9K news articles instead of 25.3K) and used a frequency cut-off, i.e. keeping only those tokens that appear at least 5 times in the corpus.

These word-level representation are used as the first layer of our network. During training we allow the weights of the representation to be updated. We further add the VADER score for the sentence under analysis. The complete sentence representation is presented in Algorithm UID8 .

InputInput OutputOutput The sentence embedding INLINEFORM0 INLINEFORM1

INLINEFORM0 in INLINEFORM1 INLINEFORM2 = [GloVe( INLINEFORM3 , INLINEFORM4 ), DepecheMood( INLINEFORM5 )] INLINEFORM6 Sentence representation
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-4c85813c29128760f760dc41e5d3cecc6e57363755992ad865b56767fd148e62

Passage ID: `qasper-passage-v1-4c85813c29128760f760dc41e5d3cecc6e57363755992ad865b56767fd148e62`; retrieval score: 0.0.

Word count: 256.

```text
Real time information is key for decision making in highly technical domains such as finance. The explosive growth of financial technology industry (Fintech) continued in 2016, partially due to the current interest in the market for Artificial Intelligence-based technologies.

Opinion-rich texts such as micro-blogging and news can have an important impact in the financial sector (e.g. raise or fall in stock value) or in the overall economy (e.g. the Greek public debt crisis). In such a context, having granular access to the opinions of an important part of the population is of key importance to any public and private actor in the field. In order to take advantage of this raw data, it is thus needed to develop machine learning methods allowing to convert unstructured text into information that can be managed and exploited.

In this paper, we address the sentiment analysis problem applied to financial headlines, where the goal is, for a given news headline and target company, to infer its polarity score i.e. how positive (or negative) the sentence is with respect to the target company. Previous research BIBREF0 has highlighted the association between news items and market fluctiations; hence, in the financial domain, sentiment analysis can be used as a proxy for bullish (i.e. positive, upwards trend) or bearish (i.e. negative, downwards trend) attitude towards a specific financial actor, allowing to identify and monitor in real-time the sentiment associated with e.g. stocks or brands.

Our contribution leverages pre-trained word embeddings (GloVe, trained on wikipedia+gigaword corpus), the DepecheMood affective lexicon, and convolutional neural networks.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1704.00939:0:3` | full | 0:171 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 711.

Fully covered answer annotations: 527a86257787c039331092a3217b16a2f0847649.

Missing evidence by answer annotation:

```text
{
  "527a86257787c039331092a3217b16a2f0847649": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: bc1e3f67d607bfc7c4c56d6b9763d3ae7f56ad5b

### Question ID and text

Question ID: `bc1e3f67d607bfc7c4c56d6b9763d3ae7f56ad5b`; paper ID: `1808.10267`.

```text
Whas is the performance drop of their model when there is no parsed input?
```

### Answers

#### Answer: db1d61e4762e120ceaef3e7e4dcc7837d94b151f

```text
{"evidence": ["The proposed models are compared against two baselines. The first, referred to here as seq2seq, is the standard RNN-based neural machine translation system with attention BIBREF0 . This baseline does not use the parsed data.", "The multi-source systems improve strongly over both baselines, with improvements of up to 1.5 BLEU over the seq2seq baseline and up to 1.1 BLEU over the parse2seq baseline. In addition, the lexicalized multi-source systems yields slightly higher BLEU scores than the unlexicalized multi-source systems; this is surprising because the lexicalized systems have significantly longer sequences than the unlexicalized ones. Finally, it is interesting to compare the seq2seq and parse2seq baselines. Parse2seq outperforms seq2seq by only a small amount compared to multi-source; thus, while adding syntax to NMT can be helpful, some ways of doing so are more effective than others."], "extractive_spans": [" improvements of up to 1.5 BLEU over the seq2seq baseline"], "free_form_answer": "", "highlighted_evidence": [" The first, referred to here as seq2seq, is the standard RNN-based neural machine translation system with attention BIBREF0 . This baseline does not use the parsed data.", "The multi-source systems improve strongly over both baselines, with improvements of up to 1.5 BLEU over the seq2seq baseline and up to 1.1 BLEU over the parse2seq baseline."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1808.10267:10:0`

```text
The proposed models are compared against two baselines. The first, referred to here as seq2seq, is the standard RNN-based neural machine translation system with attention BIBREF0 . This baseline does not use the parsed data.
```

Evidence location: `1808.10267:11:1`

```text
The multi-source systems improve strongly over both baselines, with improvements of up to 1.5 BLEU over the seq2seq baseline and up to 1.1 BLEU over the parse2seq baseline. In addition, the lexicalized multi-source systems yields slightly higher BLEU scores than the unlexicalized multi-source systems; this is surprising because the lexicalized systems have significantly longer sequences than the unlexicalized ones. Finally, it is interesting to compare the seq2seq and parse2seq baselines. Parse2seq outperforms seq2seq by only a small amount compared to multi-source; thus, while adding syntax to NMT can be helpful, some ways of doing so are more effective than others.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-6a4c9092d4c885591823dc7b12014230c6a87c19be6f9e8e2fce67d271a13f48

Passage ID: `qasper-passage-v1-6a4c9092d4c885591823dc7b12014230c6a87c19be6f9e8e2fce67d271a13f48`; retrieval score: 7.746276125939242.

Word count: 256.

```text
Neural machine translation (NMT) typically makes use of a recurrent neural network (RNN) -based encoder and decoder, along with an attention mechanism BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 . However, it has been shown that RNNs require some supervision to learn syntax BIBREF4 , BIBREF5 , BIBREF6 . Therefore, explicitly incorporating syntactic information into NMT has the potential to improve performance. This is particularly true for source syntax, which can improve the model's representation of the source language.

Recently, there have been a number of proposals for using linearized representations of parses within standard NMT BIBREF7 , BIBREF8 , BIBREF9 . Linearized parses are advantageous because they can inject syntactic information into the models without significant changes to the architecture. However, using linearized parses in a sequence-to-sequence (seq2seq) framework creates some challenges, particularly when using source parses. First, the parsed sequences are significantly longer than standard sentences, since they contain node labels as well as words. Second, these systems often fail when the source sentence is not parsed. This can be a problem for inference, since the external parser may fail on an input sentence at test time. We propose a method for incorporating linearized source parses into NMT that addresses these challenges by taking both the sequential source sentence and its linearized parse simultaneously as input in a multi-source framework. Thus, the model is able to use the syntactic information encoded in the parse while falling back to the sequential sentence when necessary. Our proposed model improves over both standard and parsed NMT baselines.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-ebdd7708a148d0b3d10ab3e03346227af985bba28d47b51d023150ab6b341882

Passage ID: `qasper-passage-v1-ebdd7708a148d0b3d10ab3e03346227af985bba28d47b51d023150ab6b341882`; retrieval score: 5.608001473660271.

Word count: 180.

```text
The idea of incorporating linearized parses into seq2seq has been adapted to NMT as a means of injecting syntax. aharoni2017towards first did this by parsing the target side of the training data and training the system to generate parsed translations of the source input; this is the inverse of our parse2seq baseline. Similarly, nadejde2017syntax interleaved CCG supertags with words on the target side, finding that this improved translation despite requiring longer sequences.

Most similar to our multi-source model is the parallel RNN model proposed by li2017modeling. Like multi-source, the parallel RNN used two encoders, one for words and the other for syntax. However, they combined these representations at the word level, whereas we combine them on the sentence level. Their mixed RNN model is also similar to our parse2seq baseline, although the mixed RNN decoder attended only to words. As the mixed RNN model outperformed the parallel RNN model, we do not attempt to compare our model to parallel RNN. These models are similar to ours in that they incorporate linearized parses into NMT; here, we utilize a multi-source framework.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-7a2835d79843a22aef383763ccbcbc6834c64281cc15c279bf370013620fbb11

Passage ID: `qasper-passage-v1-7a2835d79843a22aef383763ccbcbc6834c64281cc15c279bf370013620fbb11`; retrieval score: 5.368467394325866.

Word count: 133.

```text
The parse2seq and multi-source systems require parsed source data at inference time. However, the parser may fail on an input sentence. Therefore, we examine how well these systems do when given only unparsed source sentences at test time.

Table TABREF13 displays the results of these experiments. For the parse2seq baseline, we use only sequential (seq) data as input. For the lexicalized and unlexicalized multi-source systems, two options are considered: seq + seq uses identical sequential data as input to both encoders, while seq + null uses null input for the parsed encoder, where every source sentence is “( )”.

The parse2seq system fails when given only sequential source data. On the other hand, both multi-source systems perform reasonably well without parsed data, although the BLEU scores are worse than multi-source with parsed data.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-6be337fd570c7ca273ae014f2d1894f7ce2b06af63b298d12ee48dff769ef2d8

Passage ID: `qasper-passage-v1-6be337fd570c7ca273ae014f2d1894f7ce2b06af63b298d12ee48dff769ef2d8`; retrieval score: 4.9918241310067994.

Word count: 131.

```text
We propose a multi-source framework for injecting linearized source parses into NMT. This model consists of two identical RNN encoders with no shared parameters, as well as a standard RNN decoder. For each target sentence, two versions of the source sentence are used: the sequential (standard) version and the linearized parse (lexicalized or unlexicalized). Each of these is encoded simultaneously using the encoders; the encodings are then combined and used as input to the decoder. We combine the source encodings using the hierarchical attention combination proposed by libovicky2017attention. This consists of a separate attention mechanism for each encoder; these are then combined using an additional attention mechanism over the two separate context vectors. This multi-source method is thus able to combine the advantages of both standard RNN-based encodings and syntactic encodings.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-64b82aabfc1ed87ee0db0a118d7a94f4bdd8020209c02f34d6b70af0f2ab4d2a

Passage ID: `qasper-passage-v1-64b82aabfc1ed87ee0db0a118d7a94f4bdd8020209c02f34d6b70af0f2ab4d2a`; retrieval score: 4.88909620980859.

Word count: 122.

```text
In this paper, we presented a multi-source method for effectively incorporating linearized parses of the source data into neural machine translation. This method, in which the parsed and sequential versions of the sentence were both taken as input during training and inference, resulted in gains of up to 1.5 BLEU on EN INLINEFORM0 DE translation. In addition, unlike parse2seq, the multi-source model translated reasonably well even when the source sentence was not parsed.

In the future, we will explore adding back-translated BIBREF18 or copied BIBREF19 target data to our multi-source system. The multi-source model does not require all training data to be parsed; thus, monolingual data can be used even if the parser is unreliable for the synthetic or copied source sentences.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 822.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "db1d61e4762e120ceaef3e7e4dcc7837d94b151f": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1808.10267:10:0": [
        [
          0,
          224
        ]
      ],
      "1808.10267:11:1": [
        [
          0,
          675
        ]
      ]
    }
  }
}
```

## Question: fb5fb11e7d01b9f9efe3db3417b8faf4f8d6931f

### Question ID and text

Question ID: `fb5fb11e7d01b9f9efe3db3417b8faf4f8d6931f`; paper ID: `1810.12196`.

```text
What baselines are presented?
```

### Answers

#### Answer: 4fb5aca8f96a5927f7fdecdde38bf3e7aedfff9c

```text
{"evidence": ["Logistic regression: To produce the representation of the input, we concatenate the Bag-Of-Words representation of the document with the Bag-Of-Words representation of the question. It produces an array of size INLINEFORM0 where INLINEFORM1 is the vocabulary size. Then we use a logistic regression to select the most probable answer among the INLINEFORM2 possibilities.", "LSTM: We start with a concatenation of the sequence of indexes of the document with the sequence of indexes of the question. Them we feed an LSTM network with this vector and use the final state as the representation of the input. Finally, we apply a logistic regression over this representation to produce the final decision.", "End-to-end memory networks: This architecture is based on two different memory cells (input and output) that contain a representation of the document. A controller, initialized with the encoding of the question, is used to calculate an attention between this controller and the representation of the document in the input memory. This attention is them used to re-weight the representation of the document in the output memory. This response from the output memory is them utilized to update the controller. After that, either a matrix is used to project this representation into the answer space either the controller is used to go through an over hop of memory. This architecture allows the model to sequentially look into the initial document seeking for important information regarding the current state of its controller. This model achieves very good performances on the 20 bAbI tasks dataset.", "Deep projective reader: This is a model of our own design, largely inspired by the efficient R-net reader BIBREF12 . The overall architecture is composed of 4 stacked layers: an encoding layer, a question/document attention, a self-attention layer and a projection layer. The following paragraphs briefly describe the overall utility of each of these layers."], "extractive_spans": ["Logistic regression", "LSTM", "End-to-end memory networks", "Deep projective reader"], "free_form_answer": "", "highlighted_evidence": ["Logistic regression: To produce the representation of the input, we concatenate the Bag-Of-Words representation of the document with the Bag-Of-Words representation of the question.", "LSTM: We start with a concatenation of the sequence of indexes of the document with the sequence of indexes of the question. Them we feed an LSTM network with this vector and use the final state as the representation of the input. Finally, we apply a logistic regression over this representation to produce the final decision.", "End-to-end memory networks: This architecture is based on two different memory cells (input and output) that contain a representation of the document.", "Deep projective reader: This is a model of our own design, largely inspired by the efficient R-net reader BIBREF12 ."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1810.12196:8:1`

```text
Logistic regression: To produce the representation of the input, we concatenate the Bag-Of-Words representation of the document with the Bag-Of-Words representation of the question. It produces an array of size INLINEFORM0 where INLINEFORM1 is the vocabulary size. Then we use a logistic regression to select the most probable answer among the INLINEFORM2 possibilities.
```

Evidence location: `1810.12196:8:2`

```text
LSTM: We start with a concatenation of the sequence of indexes of the document with the sequence of indexes of the question. Them we feed an LSTM network with this vector and use the final state as the representation of the input. Finally, we apply a logistic regression over this representation to produce the final decision.
```

Evidence location: `1810.12196:8:3`

```text
End-to-end memory networks: This architecture is based on two different memory cells (input and output) that contain a representation of the document. A controller, initialized with the encoding of the question, is used to calculate an attention between this controller and the representation of the document in the input memory. This attention is them used to re-weight the representation of the document in the output memory. This response from the output memory is them utilized to update the controller. After that, either a matrix is used to project this representation into the answer space either the controller is used to go through an over hop of memory. This architecture allows the model to sequentially look into the initial document seeking for important information regarding the current state of its controller. This model achieves very good performances on the 20 bAbI tasks dataset.
```

Evidence location: `1810.12196:8:4`

```text
Deep projective reader: This is a model of our own design, largely inspired by the efficient R-net reader BIBREF12 . The overall architecture is composed of 4 stacked layers: an encoding layer, a question/document attention, a self-attention layer and a projection layer. The following paragraphs briefly describe the overall utility of each of these layers.
```

#### Answer: 8febaed24c8afa73ee27ab866d7f74785e0fd426

```text
{"evidence": ["In this section, we present the performance of four different models on our dataset: a logistic regression and three neural models. The first one is a basic LSTM BIBREF20 , the second a MemN2N BIBREF18 and the third one is a model of our own design. This fourth model reuses the encoding layers of the R-net BIBREF12 and we modify the final layers with a projection layer that will be able to select the answer among the set of candidates instead of pointing the answerer directly into the source document.", "Logistic regression: To produce the representation of the input, we concatenate the Bag-Of-Words representation of the document with the Bag-Of-Words representation of the question. It produces an array of size INLINEFORM0 where INLINEFORM1 is the vocabulary size. Then we use a logistic regression to select the most probable answer among the INLINEFORM2 possibilities.", "LSTM: We start with a concatenation of the sequence of indexes of the document with the sequence of indexes of the question. Them we feed an LSTM network with this vector and use the final state as the representation of the input. Finally, we apply a logistic regression over this representation to produce the final decision.", "End-to-end memory networks: This architecture is based on two different memory cells (input and output) that contain a representation of the document. A controller, initialized with the encoding of the question, is used to calculate an attention between this controller and the representation of the document in the input memory. This attention is them used to re-weight the representation of the document in the output memory. This response from the output memory is them utilized to update the controller. After that, either a matrix is used to project this representation into the answer space either the controller is used to go through an over hop of memory. This architecture allows the model to sequentially look into the initial document seeking for important information regarding the current state of its controller. This model achieves very good performances on the 20 bAbI tasks dataset.", "Deep projective reader: This is a model of our own design, largely inspired by the efficient R-net reader BIBREF12 . The overall architecture is composed of 4 stacked layers: an encoding layer, a question/document attention, a self-attention layer and a projection layer. The following paragraphs briefly describe the overall utility of each of these layers."], "extractive_spans": ["Logistic regression", "LSTM", "End-to-end memory networks", "Deep projective reader"], "free_form_answer": "", "highlighted_evidence": ["In this section, we present the performance of four different models on our dataset: a logistic regression and three neural models. ", "Logistic regression: To produce the representation of the input, we concatenate the Bag-Of-Words representation of the document with the Bag-Of-Words representation of the question. ", "LSTM: We start with a concatenation of the sequence of indexes of the document with the sequence of indexes of the question. Them we feed an LSTM network with this vector and use the final state as the representation of the input. Finally, we apply a logistic regression over this representation to produce the final decision.\n\n", "End-to-end memory networks: This architecture is based on two different memory cells (input and output) that contain a representation of the document. ", "Deep projective reader: This is a model of our own design, largely inspired by the efficient R-net reader BIBREF12 ."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1810.12196:8:0`

```text
In this section, we present the performance of four different models on our dataset: a logistic regression and three neural models. The first one is a basic LSTM BIBREF20 , the second a MemN2N BIBREF18 and the third one is a model of our own design. This fourth model reuses the encoding layers of the R-net BIBREF12 and we modify the final layers with a projection layer that will be able to select the answer among the set of candidates instead of pointing the answerer directly into the source document.
```

Evidence location: `1810.12196:8:1`

```text
Logistic regression: To produce the representation of the input, we concatenate the Bag-Of-Words representation of the document with the Bag-Of-Words representation of the question. It produces an array of size INLINEFORM0 where INLINEFORM1 is the vocabulary size. Then we use a logistic regression to select the most probable answer among the INLINEFORM2 possibilities.
```

Evidence location: `1810.12196:8:2`

```text
LSTM: We start with a concatenation of the sequence of indexes of the document with the sequence of indexes of the question. Them we feed an LSTM network with this vector and use the final state as the representation of the input. Finally, we apply a logistic regression over this representation to produce the final decision.
```

Evidence location: `1810.12196:8:3`

```text
End-to-end memory networks: This architecture is based on two different memory cells (input and output) that contain a representation of the document. A controller, initialized with the encoding of the question, is used to calculate an attention between this controller and the representation of the document in the input memory. This attention is them used to re-weight the representation of the document in the output memory. This response from the output memory is them utilized to update the controller. After that, either a matrix is used to project this representation into the answer space either the controller is used to go through an over hop of memory. This architecture allows the model to sequentially look into the initial document seeking for important information regarding the current state of its controller. This model achieves very good performances on the 20 bAbI tasks dataset.
```

Evidence location: `1810.12196:8:4`

```text
Deep projective reader: This is a model of our own design, largely inspired by the efficient R-net reader BIBREF12 . The overall architecture is composed of 4 stacked layers: an encoding layer, a question/document attention, a self-attention layer and a projection layer. The following paragraphs briefly describe the overall utility of each of these layers.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-30910693f9cc88382e88e5ae309f88dcb0ac85d0d7b4eb8f3b8aeb72cb05fcfc

Passage ID: `qasper-passage-v1-30910693f9cc88382e88e5ae309f88dcb0ac85d0d7b4eb8f3b8aeb72cb05fcfc`; retrieval score: 4.169970037087711.

Word count: 214.

```text
Table TABREF19 displays the performance of the 4 baselines on the ReviewQA's test set. These results are the performance achieved by our own implementation of these 4 models. According to our results, the simple LSTM network and the MemN2N perform very poorly on this dataset. Especially on the most advanced reasoning tasks. Indeed, the task 5 which corresponds to the prediction of the exact rating of an aspect seems to be very challenging for these model. Maybe the tokenization by sentence to create the memory blocks of the MemN2N, which is appropriated in the case of the bAbI tasks, is not a good representation of the documents when it has to handle human generated comments. However, the logistic regression achieves reasonable performance on these tasks, and do not suffer from catastrophic performance on any tasks. Its worst result comes on task 6 and one of the reason is probably that this architecture is not designed to predict a list of answers. On the contrary, the deep projective reader achieves encouraging on this dataset. It outperforms all the other baselines, with very good scores on the first fourth tasks. The question/document and document/document attention layers proposed in BIBREF12 seem once again to produce rich encodings of the inputs which are relevant for our projection layer.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-7a2db520e59fa507522851ad67ef48785c33ea2e497884cf987bf63855628e73

Passage ID: `qasper-passage-v1-7a2db520e59fa507522851ad67ef48785c33ea2e497884cf987bf63855628e73`; retrieval score: 3.7641829272931124.

Word count: 400.

```text
A large majority of the human knowledge is recorded through text documents. That is why ability for a system to automatically infer information from text without any structured data has become a major challenge. Answering questions about a given document is a relevant proxy task that has been proposed as a way to evaluate the reading ability of a given model. In this configuration, a text document such as a news article, a document from Wikipedia or any type of text is presented to a machine with an associated set of questions. The system is then expected to answer these questions and evaluated by its accuracy on this task. The machine reading framework is very general and we can imagine a large panel of questions that can possibly handle most of the standard natural language processing tasks. For example, the task of named entities recognition can be formulated as a machine reading one where your document is the sentence and the question would be 'What are the named entities mentioned in this sentence?'. These natural language interactions are an important objective for reading systems.

Recently, many datasets have been proposed to build and evaluate reading models BIBREF0 , BIBREF1 . From cloze style questions BIBREF2 to open questions BIBREF3 , from synthetic data BIBREF4 to human written articles BIBREF5 , many styles of documents and questions have been proposed to challenge reading models. The correct answer to the questions proposed in most of these datasets is a span of text of the source document, which can be restricted to a single word in several cases. It means that the answer should explicitly be present in the source document and that the model should be able to locate it.

Different models have already shown superhuman performance on several of these datasets and particularly on the SQuAD dataset composed of Wikipedia articles BIBREF6 , BIBREF7 . However, some limits of such models have been highlighted when they encounter perturbations into the input documents BIBREF8 . Indeed almost all of the state of the art models on the SQuAD dataset suffer from a lack of robustness against adversarial examples. Once the model is trained, a meaningless sentence added at the end of the text document can completely disturb the reading system. Conversely, these adversarial examples do not seem to fool a human reader who will be capable of answering the questions as well
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-e2f2ed6d9989aaac1e03fcf3c12492e2c7f10c1578f7bebd6430fae16c71f378

Passage ID: `qasper-passage-v1-e2f2ed6d9989aaac1e03fcf3c12492e2c7f10c1578f7bebd6430fae16c71f378`; retrieval score: 2.118463522045778.

Word count: 257.

```text
Objective: Starting with the original corpus, we aim at building a machine reading task where natural language questions will challenge the model on its understanding of the reviews. Indeed learning relational reasoning competencies over natural language documents is a major challenge of the current reading models. These original raw data allow us to generate relational questions that can possibly require a global understanding of the comment and reasoning skills to be treated. For example, asking a question like What is the best aspect rated in this comment ? is not an easy question that can be answered without a deep understanding of the review. It is necessary to capture all the aspects mentioned in the text, to predict their rating and finally to select the best one. The tasks and the dataset we propose are publicly available at http://www.europe.naverlabs.com/Blog/ReviewQA-A-novel-relational-aspect-based-opinion-dataset-for-machine-reading

We introduce a list of 8 different competencies that a reading system should master in order to process reviews and text documents in general. These 8 tasks require different competencies and a different level of understanding of the document to be well answered. For instance, detecting if an aspect is mentioned in a review will require less understanding of the review than predicting explicitly the rating of this aspect. Table TABREF10 presents the 8 tasks we have introduced in this dataset with an example of a question that corresponds to each task. We also provide the expected type of the answer (Yes/No question, rating question...). It can be an additional tool to analyze the errors of the readers.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-2d49e930000ec27b1211b8f0e866649ecdda6fd68f50632be54fd64357a40474

Passage ID: `qasper-passage-v1-2d49e930000ec27b1211b8f0e866649ecdda6fd68f50632be54fd64357a40474`; retrieval score: 0.9023970700776408.

Word count: 400.

```text
ReviewQA is proposed as a novel dataset regarding the collection of the existing ones. Indeed a large panel of available datasets, that evaluate models on different types of documents, can only be valuable for designing efficient models and learning protocols. In this following part, we describe several of these datasets.

SQuAD: The Standford Question Answering Dataset (SQuAD) introduced in BIBREF0 is a large dataset of natural questions over the 500 most popular articles of Wikipedia. All the questions have been crowdsourced and answers are spans of text extracted from source documents. This dataset has been very popular these last two years and the performance of the architectures that have been proposed have rapidly increased until several models surpass the human score. Indeed, in the original paper human performance has been measured at 82.304 points for the exact match metric and at the time we are writing this paper four models have already a higher score. In another hand BIBREF8 has shown that these models suffer from a lack of robustness against adversarial examples that are meaningless from a human point of view. This suggests the need for a more challenging dataset that will allow developing strongest reasoning architectures.

NewsQA: NewsQA BIBREF1 is a dataset very similar to SQuAD. It contains 120.000 human generated questions over 12.000 articles form CNN originally introduced in BIBREF5 . It has been designed to be more challenging than SQuAD with questions that might require to extract multiple spans of text or not be answerable.

WikiHop and MedHop: These are two recent datasets introduced in BIBREF13 . Unlike SQuAD and NewsQA, important facts are spread out across multiple documents and, in order to answer a question, it is necessary to jump over a set of passages to collect the required information. The relevant passages are not explicitly mentioned in the data so this dataset measures the ability that a model has to navigate across multiple documents. The questions come with a set of candidates which are all present in the text.

MS Marco: This dataset has been released in BIBREF14 . The documents come from the internet and the questions are real user queries asked through the bing search engine. The dataset contains around 100.000 queries and each of them comes with a set of approximatively 10 relevant passages. Like in SQuAD, several models are already doing superhuman performances on this dataset.

Facebook bAbI tasks: This
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-f330aac133c11d3cc52e579a8df341ecf5a24128b66446d474d5ebce89ca4689

Passage ID: `qasper-passage-v1-f330aac133c11d3cc52e579a8df341ecf5a24128b66446d474d5ebce89ca4689`; retrieval score: 0.7977222713641668.

Word count: 96.

```text
of understanding of the document and the question, are binary questions. It means that in the generated dataset the answers yes and no tend to be more present than the others. To balance in a better way the distribution of the answers, we chose to affect a higher probability of sampling to the task 5, 6, 7.1, 8. Indeed, these tasks are not binary questions and required an aspect name as the answer. Figure FIGREF17 represents the repartition of question types in our dataset. Finally, figure FIGREF15 shows the repartition of the answers in the dataset.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1367.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "4fb5aca8f96a5927f7fdecdde38bf3e7aedfff9c": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1810.12196:8:1": [
        [
          0,
          370
        ]
      ],
      "1810.12196:8:2": [
        [
          0,
          326
        ]
      ],
      "1810.12196:8:3": [
        [
          0,
          899
        ]
      ],
      "1810.12196:8:4": [
        [
          0,
          358
        ]
      ]
    }
  },
  "8febaed24c8afa73ee27ab866d7f74785e0fd426": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1810.12196:8:0": [
        [
          0,
          506
        ]
      ],
      "1810.12196:8:1": [
        [
          0,
          370
        ]
      ],
      "1810.12196:8:2": [
        [
          0,
          326
        ]
      ],
      "1810.12196:8:3": [
        [
          0,
          899
        ]
      ],
      "1810.12196:8:4": [
        [
          0,
          358
        ]
      ]
    }
  }
}
```

## Question: 73bb8b7d7e98ccb88bb19ecd2215d91dd212f50d

### Question ID and text

Question ID: `73bb8b7d7e98ccb88bb19ecd2215d91dd212f50d`; paper ID: `1805.04033`.

```text
What human evaluation method is proposed?
```

### Answers

#### Answer: d76d0cd894e1434896b72b8211bf1fa0e2db7703

```text
{"evidence": ["More detailed explanation is introduced in Section SECREF2 . Another problem for abstractive text summarization is that the system summary cannot be easily evaluated automatically. ROUGE BIBREF9 is widely used for summarization evaluation. However, as ROUGE is designed for extractive text summarization, it cannot deal with summary paraphrasing in abstractive text summarization. Besides, as ROUGE is based on the reference, it requires high-quality reference summary for a reasonable evaluation, which is also lacking in the existing dataset for Chinese social media text summarization. We argue that for proper evaluation of text generation task, human evaluation cannot be avoided. We propose a simple and practical human evaluation for evaluating text summarization, where the summary is evaluated against the source content instead of the reference. It handles both of the problems of paraphrasing and lack of high-quality reference. The contributions of this work are summarized as follows:", "For text summarization, a common automatic evaluation method is ROUGE BIBREF9 . The generated summary is evaluated against the reference summary, based on unigram recall (ROUGE-1), bigram recall (ROUGE-2), and recall of longest common subsequence (ROUGE-L). To facilitate comparison with the existing systems, we adopt ROUGE as the automatic evaluation method. The ROUGE is calculated on the character level, following the previous work BIBREF1 . However, for abstractive text summarization, the ROUGE is sub-optimal, and cannot assess the semantic consistency between the summary and the source content, especially when there is only one reference for a piece of text. The reason is that the same content may be expressed in different ways with different focuses. Simple word match cannot recognize the paraphrasing. It is the case for all of the existing large-scale datasets. Besides, as aforementioned, ROUGE is calculated on the character level in Chinese text summarization, making the metrics favor the models on the character level in practice. In Chinese, a word is the smallest semantic element that can be uttered in isolation, not a character. In the extreme case, the generated text could be completely intelligible, but the characters could still match. In theory, calculating ROUGE metrics on the word level could alleviate the problem. However, word segmentation is also a non-trivial task for Chinese. There are many kinds of segmentation rules, which will produce different ROUGE scores. We argue that it is not acceptable to introduce additional systematic bias in automatic evaluations, and automatic evaluation for semantically related tasks can only serve as a reference. To avoid the deficiencies, we propose a simple human evaluation method to assess the semantic consistency. Each summary candidate is evaluated against the text rather than the reference. If the candidate is irrelevant or incorrect to the text, or the candidate is not understandable, the candidate is labeled bad. Otherwise, the candidate is labeled good. Then, we can get an accuracy of the good summaries. The proposed evaluation is very simple and straight-forward. It focuses on the relevance between the summary and the text. The semantic consistency should be the major consideration when putting the text summarization methods into practice, but the current automatic methods cannot judge properly. For detailed guidelines in human evaluation, please refer to Appendix SECREF6 . In the human evaluation, the text-summary pairs are dispatched to two human annotators who are native speakers of Chinese. As in our setting the summary is evaluated against the reference, the number of the pairs needs to be manually evaluated is four times the number of the pairs in the test set, because we need to compare four systems in total. To decrease the workload and get a hint about the annotation quality at the same time, we adopt the following procedure. We first randomly select 100 pairs in the validation set for the two human annotators to evaluate. Each pair is annotated twice, and the inter-annotator agreement is checked. We find that under the protocol, the inter-annotator agreement is quite high. In the evaluation of the test set, a pair is only annotated once to accelerate evaluation. To further maintain consistency, summaries of the same source content will not be distributed to different annotators."], "extractive_spans": [], "free_form_answer": "comparing the summary with the text instead of the reference and labeling the candidate bad if it is incorrect or irrelevant", "highlighted_evidence": ["We propose a simple and practical human evaluation for evaluating text summarization, where the summary is evaluated against the source content instead of the reference. It handles both of the problems of paraphrasing and lack of high-quality reference. ", "To avoid the deficiencies, we propose a simple human evaluation method to assess the semantic consistency. Each summary candidate is evaluated against the text rather than the reference. If the candidate is irrelevant or incorrect to the text, or the candidate is not understandable, the candidate is labeled bad. Otherwise, the candidate is labeled good. Then, we can get an accuracy of the good summaries. The proposed evaluation is very simple and straight-forward. It focuses on the relevance between the summary and the text. The semantic consistency should be the major consideration when putting the text summarization methods into practice, but the current automatic methods cannot judge properly. For detailed guidelines in human evaluation, please refer to Appendix SECREF6 . "], "unanswerable": false, "yes_no": null}
```

Evidence location: `1805.04033:0:3`

```text
More detailed explanation is introduced in Section SECREF2 . Another problem for abstractive text summarization is that the system summary cannot be easily evaluated automatically. ROUGE BIBREF9 is widely used for summarization evaluation. However, as ROUGE is designed for extractive text summarization, it cannot deal with summary paraphrasing in abstractive text summarization. Besides, as ROUGE is based on the reference, it requires high-quality reference summary for a reasonable evaluation, which is also lacking in the existing dataset for Chinese social media text summarization. We argue that for proper evaluation of text generation task, human evaluation cannot be avoided. We propose a simple and practical human evaluation for evaluating text summarization, where the summary is evaluated against the source content instead of the reference. It handles both of the problems of paraphrasing and lack of high-quality reference. The contributions of this work are summarized as follows:
```

Evidence location: `1805.04033:7:0`

```text
For text summarization, a common automatic evaluation method is ROUGE BIBREF9 . The generated summary is evaluated against the reference summary, based on unigram recall (ROUGE-1), bigram recall (ROUGE-2), and recall of longest common subsequence (ROUGE-L). To facilitate comparison with the existing systems, we adopt ROUGE as the automatic evaluation method. The ROUGE is calculated on the character level, following the previous work BIBREF1 . However, for abstractive text summarization, the ROUGE is sub-optimal, and cannot assess the semantic consistency between the summary and the source content, especially when there is only one reference for a piece of text. The reason is that the same content may be expressed in different ways with different focuses. Simple word match cannot recognize the paraphrasing. It is the case for all of the existing large-scale datasets. Besides, as aforementioned, ROUGE is calculated on the character level in Chinese text summarization, making the metrics favor the models on the character level in practice. In Chinese, a word is the smallest semantic element that can be uttered in isolation, not a character. In the extreme case, the generated text could be completely intelligible, but the characters could still match. In theory, calculating ROUGE metrics on the word level could alleviate the problem. However, word segmentation is also a non-trivial task for Chinese. There are many kinds of segmentation rules, which will produce different ROUGE scores. We argue that it is not acceptable to introduce additional systematic bias in automatic evaluations, and automatic evaluation for semantically related tasks can only serve as a reference. To avoid the deficiencies, we propose a simple human evaluation method to assess the semantic consistency. Each summary candidate is evaluated against the text rather than the reference. If the candidate is irrelevant or incorrect to the text, or the candidate is not understandable, the candidate is labeled bad. Otherwise, the candidate is labeled good. Then, we can get an accuracy of the good summaries. The proposed evaluation is very simple and straight-forward. It focuses on the relevance between the summary and the text. The semantic consistency should be the major consideration when putting the text summarization methods into practice, but the current automatic methods cannot judge properly. For detailed guidelines in human evaluation, please refer to Appendix SECREF6 . In the human evaluation, the text-summary pairs are dispatched to two human annotators who are native speakers of Chinese. As in our setting the summary is evaluated against the reference, the number of the pairs needs to be manually evaluated is four times the number of the pairs in the test set, because we need to compare four systems in total. To decrease the workload and get a hint about the annotation quality at the same time, we adopt the following procedure. We first randomly select 100 pairs in the validation set for the two human annotators to evaluate. Each pair is annotated twice, and the inter-annotator agreement is checked. We find that under the protocol, the inter-annotator agreement is quite high. In the evaluation of the test set, a pair is only annotated once to accelerate evaluation. To further maintain consistency, summaries of the same source content will not be distributed to different annotators.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-2a962141477f2ed2650e55f0c913b44cec4e9c3a5e8227d91529af4f88b101a8

Passage ID: `qasper-passage-v1-2a962141477f2ed2650e55f0c913b44cec4e9c3a5e8227d91529af4f88b101a8`; retrieval score: 3.774920645964191.

Word count: 400.

```text
To examine the effect of the proposed method and reveal how the proposed method improves the consistency, we compare the output of the baseline with Dual-Train, based on both the output text and the output label distribution. We also conduct error analysis to discover room for improvements.

To gain a better understanding of the results, we analyze the summaries generated by the baseline model and our proposed model. Some of the summaries are listed in Table TABREF28 . As shown in the table, the summaries generated by the proposed method are much better than the baseline, and we believe they are more precise and informative than the references. In the first one, the baseline system generates a grammatical but unrelated summary, while the proposed method generates a more informative summary. In the second one, the baseline system generates a related but ungrammatical summary, while the proposed method generates a summary related to the source content but different from the reference. We believe the generated summary is actually better than the reference because the focus of the visit is not the event itself but its purpose. In the third one, the baseline system generates a related and grammatical summary, but the facts stated are completely incorrect. The summary generated by the proposed method is more comprehensive than the reference, while the reference only includes the facts in the last sentence of the source content. In short, the generated summary of the proposed method is more consistent with the source content. It also exhibits the necessity of the proposed human evaluation. Because when the generated summary is evaluated against the reference, it may seem redundant or wrong, but it is actually true to the source content. While it is arguable that the generated summary is better than the reference, there is no doubt that the generated summary of the proposed method is better than the baseline. However, the improvement cannot be properly shown by the existing evaluation methods. Furthermore, the examples suggest that the proposed method does learn better correspondence. The highlighted words in each example in Table TABREF28 share almost the same previous words. However, in the first one, the baseline considers “UTF8gbsn停” (stop) as the most related words, which is a sign of noisy word relations learned from other training examples, while the proposed method generates “UTF8gbsn进站” (to the platform), which is more related to what a human thinks. It
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-38ca1bc4e6070fbd8acc54a18479b9af7dcad11d5534962f924a3a3e212c042e

Passage ID: `qasper-passage-v1-38ca1bc4e6070fbd8acc54a18479b9af7dcad11d5534962f924a3a3e212c042e`; retrieval score: 2.9241138754795024.

Word count: 335.

```text
However, the aforementioned method tries to regularize the output word distribution based on what it has already learned. The relative order of the output words is kept. The self-dependency may not be desirable for regularization. It may be better if more correspondence that is spurious can be identified. In this paper, we further propose to obtain the soft target from a different view of the model, so that different knowledge of the dataset can be used to mitigate the overfitting problem. An additional output layer is introduced to generate the soft target. The two output layers share the same hidden representation but have independent parameters. They could learn different knowledge of the data. We refer to this approach as Dual-Train. For clarity, the original output layer is denoted by INLINEFORM0 and the new output layer INLINEFORM1 . Their outputs are denoted by INLINEFORM2 and INLINEFORM3 , respectively. The output layer INLINEFORM4 acts as the original output layer. We apply soft training using the output from INLINEFORM5 to this output layer to increase its ability of generalization. Suppose the correct label is INLINEFORM6 . The target of the output INLINEFORM7 includes both the one-hot distribution and the distribution generated from INLINEFORM8 : DISPLAYFORM0

The new output layer INLINEFORM0 is trained normally using the originally hard target. This output layer is not used in the prediction, and its only purpose is to generate the soft target to facilitate the soft training of INLINEFORM1 . Suppose the correct label is INLINEFORM2 . The target of the output INLINEFORM3 includes only the one-hot distribution: DISPLAYFORM0

Because of the random initialization of the parameters in the output layers, INLINEFORM0 and INLINEFORM1 could learn different things. The diversified knowledge is helpful when dealing with the spurious correspondence in the data. It can also be seen as an online kind of ensemble methods. Several different instances of the same model are softly aggregated into one to make classification. The right part of Figure FIGREF6 shows the architecture of the proposed Dual-Train method.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-9c21a7ff7a85f9a7440948c8750dab0df92b9e6426b381c225b8df187c31f1ac

Passage ID: `qasper-passage-v1-9c21a7ff7a85f9a7440948c8750dab0df92b9e6426b381c225b8df187c31f1ac`; retrieval score: 2.880799896322124.

Word count: 400.

```text
considers “UTF8gbsn停” (stop) as the most related words, which is a sign of noisy word relations learned from other training examples, while the proposed method generates “UTF8gbsn进站” (to the platform), which is more related to what a human thinks. It is the same with the second example, where a human selects “UTF8gbsn专家” (expert) and Dual-Train selects “UTF8gbsn工作者” (worker), while the baseline selects “UTF8gbsn钻研” (research) and fails to generate a grammatical sentence later. In the third one, the reference and the baseline use the same word, while Dual-Train chooses a word of the same meaning. It can be concluded that Dual-Train indeed learns better word relations that could generalize to the test set, and good word relations can guide the decoder to generate semantically consistent summaries.

To show why the generated text of the proposed method is more related to the source content, we further analyze the label distribution, i.e., the word distribution, generated by the (first) output layer, from which the output word is selected. To illustrate the relationship, we calculate a representation for each word based on the label distributions. Each representation is associated with a specific label (word), denoted by INLINEFORM0 , and each dimension INLINEFORM1 shows how likely the label indexed by INLINEFORM2 will be generated instead of the label INLINEFORM3 . To get such representation, we run the model on the training set and get the output vectors in the decoder, which are then averaged with respect to their corresponding labels to form a representation. We can obtain the most related words of a word by simply selecting the highest values from its representation. Table TABREF30 lists some of the labels and the top 4 labels that are most likely to replace each of the labels. It is a hint about the correspondence learned by the model. From the results, it can be observed that Dual-Train learns the better semantic relevance of a word compared to the baseline because the spurious word correspondence is alleviated by regularization. For example, the possible substitutes of the word “UTF8gbsn多长时间” (how long) considered by Dual-Train include “UTF8gbsn多少” (how many), “UTF8gbsn多久” (how long) and “UTF8gbsn时间” (time). However, the relatedness is learned poorly in the baseline, as there is “UTF8gbsn知道” (know), a number, and two particles in the possible substitutes considered by the baseline. Another representative example is the word “UTF8gbsn图像” (image), where the baseline also includes two particles in its most
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-2a000f351fd1497b625284f23dbc7999c45b1e466be6107a12d99c1e984b8c68

Passage ID: `qasper-passage-v1-2a000f351fd1497b625284f23dbc7999c45b1e466be6107a12d99c1e984b8c68`; retrieval score: 2.671651434884039.

Word count: 155.

```text
We propose a regularization approach for the sequence-to-sequence model on the Chinese social media summarization task. In the proposed approach, we use a cross-entropy based regularization term to make the model neglect the possible unrelated words. We propose two methods for obtaining the soft output word distribution used in the regularization, of which Dual-Train proves to be more effective. Experimental results show that the proposed method can improve the semantic consistency by 4% in terms of human evaluation. As shown by the analysis, the proposed method achieves the improvements by eliminating the less semantically-related word correspondence. The proposed human evaluation method is effective and efficient in judging the semantic consistency, which is absent in previous work but is crucial in the accurate evaluation of the text summarization systems. The proposed metric is simple to conduct and easy to interpret. It also provides an insight on how practicable the existing systems are in the real-world scenario.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-725e4285d5c6bf4911a4da80ce1b74b42e3ec31d3c3a47849b6fb3b37ee8f634

Passage ID: `qasper-passage-v1-725e4285d5c6bf4911a4da80ce1b74b42e3ec31d3c3a47849b6fb3b37ee8f634`; retrieval score: 2.611549888788584.

Word count: 400.

```text
For text summarization, a common automatic evaluation method is ROUGE BIBREF9 . The generated summary is evaluated against the reference summary, based on unigram recall (ROUGE-1), bigram recall (ROUGE-2), and recall of longest common subsequence (ROUGE-L). To facilitate comparison with the existing systems, we adopt ROUGE as the automatic evaluation method. The ROUGE is calculated on the character level, following the previous work BIBREF1 . However, for abstractive text summarization, the ROUGE is sub-optimal, and cannot assess the semantic consistency between the summary and the source content, especially when there is only one reference for a piece of text. The reason is that the same content may be expressed in different ways with different focuses. Simple word match cannot recognize the paraphrasing. It is the case for all of the existing large-scale datasets. Besides, as aforementioned, ROUGE is calculated on the character level in Chinese text summarization, making the metrics favor the models on the character level in practice. In Chinese, a word is the smallest semantic element that can be uttered in isolation, not a character. In the extreme case, the generated text could be completely intelligible, but the characters could still match. In theory, calculating ROUGE metrics on the word level could alleviate the problem. However, word segmentation is also a non-trivial task for Chinese. There are many kinds of segmentation rules, which will produce different ROUGE scores. We argue that it is not acceptable to introduce additional systematic bias in automatic evaluations, and automatic evaluation for semantically related tasks can only serve as a reference. To avoid the deficiencies, we propose a simple human evaluation method to assess the semantic consistency. Each summary candidate is evaluated against the text rather than the reference. If the candidate is irrelevant or incorrect to the text, or the candidate is not understandable, the candidate is labeled bad. Otherwise, the candidate is labeled good. Then, we can get an accuracy of the good summaries. The proposed evaluation is very simple and straight-forward. It focuses on the relevance between the summary and the text. The semantic consistency should be the major consideration when putting the text summarization methods into practice, but the current automatic methods cannot judge properly. For detailed guidelines in human evaluation, please refer to Appendix SECREF6 . In the human evaluation, the text-summary pairs are dispatched to two human annotators who are native speakers of Chinese. As in our
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1805.04033:7:0` | partial | 0:2612 |

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1690.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "d76d0cd894e1434896b72b8211bf1fa0e2db7703": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1805.04033:0:3": [
        [
          0,
          997
        ]
      ],
      "1805.04033:7:0": [
        [
          2612,
          3412
        ]
      ]
    }
  }
}
```

## Question: 022c365a14fdec406c7a945a1a18e7e79df37f08

### Question ID and text

Question ID: `022c365a14fdec406c7a945a1a18e7e79df37f08`; paper ID: `1909.07575`.

```text
What is the attention module pretrained on?
```

### Answers

#### Answer: b48cc0398f600f20489314a52f50ede783cc5581

```text
{"evidence": ["To sufficiently utilize the large dataset $\\mathcal {A}$ and $\\mathcal {M}$, the model is pre-trained on CTC-based ASR task and MT task in the pre-training stage."], "extractive_spans": ["the model is pre-trained on CTC-based ASR task and MT task in the pre-training stage."], "free_form_answer": "", "highlighted_evidence": ["o sufficiently utilize the large dataset $\\mathcal {A}$ and $\\mathcal {M}$, the model is pre-trained on CTC-based ASR task and MT task in the pre-training stage."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1909.07575:6:0`

```text
To sufficiently utilize the large dataset $\mathcal {A}$ and $\mathcal {M}$, the model is pre-trained on CTC-based ASR task and MT task in the pre-training stage.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-fbfbb0fc24a5a0ebc7d47a68738bd106fde7674bdb8b826b0cd4e09221a867ea

Passage ID: `qasper-passage-v1-fbfbb0fc24a5a0ebc7d47a68738bd106fde7674bdb8b826b0cd4e09221a867ea`; retrieval score: 5.625884774480025.

Word count: 170.

```text
To leverage large scale ASR and MT data, multi-task learning and pre-training techniques are widely employed to improve the ST system. As shown in Figure FIGREF4, there are three popular multi-task strategies for ST, including 1) one-to-many setting, in which a speech encoder is shared between ASR and ST tasks; 2) many-to-one setting in which a decoder is shared between MT and ST tasks; and 3) many-to-many setting where both the encoder and decoder are shared.

A many-to-many multi-task model contains two encoders as well as two decoders. It can be jointly trained on ASR, MT, and ST tasks. As the attention module is task-specific, three attentions are defined.

Usually, the size of $\mathcal {A}$ and $\mathcal {M}$ is much larger than $\mathcal {S}$. Therefore, the common training practice is to pre-train the model on ASR and MT tasks and then fine-tune it with a multi-task learning manner. However, as aforementioned, this method suffers from subnet waste, role mismatch and non-pre-trained attention issues, which severely limits the end-to-end ST performance.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-a888eeae99323acc46803d1bbedc8cdaec568b8352694eb0b40b519ac28a7f44

Passage ID: `qasper-passage-v1-a888eeae99323acc46803d1bbedc8cdaec568b8352694eb0b40b519ac28a7f44`; retrieval score: 5.396738407250305.

Word count: 400.

```text
is able to reuse all subnets in pre-training, keep the roles of subnets consistent, and pre-train the attention module. Concretely, the TCEN consists of three components, a speech encoder, a text encoder, and a target text decoder. Different from the previous work that pre-trains an encoder-decoder based ASR model, we only pre-train an ASR encoder by optimizing the Connectionist Temporal Classification (CTC) BIBREF8 objective function. In this way, the additional decoder of ASR is not required while keeping the ability to read acoustic features into the source language space by the speech encoder. Besides, the text encoder and decoder can be pre-trained on a large MT dataset. After that, we employ common used multi-task learning method to jointly learn ASR, MT and ST tasks.

Compared to prior works, the encoder of TCEN is a concatenation of an ASR encoder and an MT encoder and our model does not have an ASR decoder, so the subnet waste issue is solved. Furthermore, the two encoders work at tandem, disentangling acoustic feature extraction and linguistic feature extraction, ensuring the role consistency between pre-training and fine-tuning. Moreover, we reuse the pre-trained MT attention module in ST, so we can leverage the alignment information learned in pre-training.

Since the text encoder consumes word embeddings of plausible texts in MT task but uses speech encoder outputs in ST task, another question is how one guarantees the speech encoder outputs are consistent with the word embeddings. We further modify our model to achieve semantic consistency and length consistency. Specifically, (1) the projection matrix at the CTC classification layer for ASR is shared with the word embedding matrix, ensuring that they are mapped to the same latent space, and (2) the length of the speech encoder output is proportional to the length of the input frame, so it is much longer than a natural sentence. To bridge the length gap, source sentences in MT are lengthened by adding word repetitions and blank tokens to mimic the CTC output sequences.

We conduct comprehensive experiments on the IWSLT18 speech translation benchmark BIBREF1, demonstrating the effectiveness of each component. Our model is significantly better than previous methods by 3.6 and 2.2 BLEU scores for the subword-level decoding and character-level decoding strategies, respectively.

Our contributions are three-folds: 1) we shed light on why previous ST models cannot sufficiently utilize the knowledge learned from the pre-training process; 2) we propose a new ST
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-858072d5dc34f0f78100a1a6b53a115e7a323c8a308c73ec0cf9eb9222c23c79

Passage ID: `qasper-passage-v1-858072d5dc34f0f78100a1a6b53a115e7a323c8a308c73ec0cf9eb9222c23c79`; retrieval score: 5.179781462649837.

Word count: 400.

```text
Speech-to-Text translation (ST) is essential for a wide range of scenarios: for example in emergency calls, where agents have to respond emergent requests in a foreign language BIBREF0; or in online courses, where audiences and speakers use different languages BIBREF1. To tackle this problem, existing approaches can be categorized into cascaded method BIBREF2, BIBREF3, where a machine translation (MT) model translates outputs of an automatic speech recognition (ASR) system into target language, and end-to-end method BIBREF4, BIBREF5, where a single model learns acoustic frames to target word sequence mappings in one step towards the final objective of interest. Although the cascaded model remains the dominant approach due to its better performance, the end-to-end method becomes more and more popular because it has lower latency by avoiding inferences with two models and rectifies the error propagation in theory.

Since it is hard to obtain a large-scale ST dataset, multi-task learning BIBREF5, BIBREF6 and pre-training techniques BIBREF7 have been applied to end-to-end ST model to leverage large-scale datasets of ASR and MT. A common practice is to pre-train two encoder-decoder models for ASR and MT respectively, and then initialize the ST model with the encoder of the ASR model and the decoder of the MT model. Subsequently, the ST model is optimized with the multi-task learning by weighing the losses of ASR, MT, and ST. This approach, however, causes a huge gap between pre-training and fine-tuning, which are summarized into three folds:

Subnet Waste: The ST system just reuses the ASR encoder and the MT decoder, while discards other pre-trained subnets, such as the MT encoder. Consequently, valuable semantic information captured by the MT encoder cannot be inherited by the final ST system.

Role Mismatch: The speech encoder plays different roles in pre-training and fine-tuning. The encoder is a pure acoustic model in pre-training, while it has to extract semantic and linguistic features additionally in fine-tuning, which significantly increases the learning difficulty.

Non-pre-trained Attention Module: Previous work BIBREF6 trains attention modules for ASR, MT and ST respectively, hence, the attention module of ST does not benefit from the pre-training.

To address these issues, we propose a Tandem Connectionist Encoding Network (TCEN), which is able to reuse all subnets in pre-training, keep the roles of subnets consistent, and pre-train the attention module. Concretely, the TCEN consists of three components, a speech encoder, a text encoder, and a target text decoder. Different from the
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-a629e2314b1618b74f8d49a42fd5b4c984494a25a2f3781dd14eb93961485aca

Passage ID: `qasper-passage-v1-a629e2314b1618b74f8d49a42fd5b4c984494a25a2f3781dd14eb93961485aca`; retrieval score: 4.612364911372831.

Word count: 400.

```text
Figure FIGREF5 sketches the overall architecture of TCEN, including a speech encoder $enc_s$, a text encoder $enc_t$ and a decoder $dec$ with an attention module $att$. During training, the $enc_s$ acts like an acoustic model which reads the input $\mathbf {x}$ to word or subword representations $\mathbf {h^s}$, then $enc_t$ learns high-level linguistic knowledge into hidden representations $\mathbf {h^t}$. Finally, the $dec$ defines a distribution probability over target words. The advantage of our architecture is that two encoders disentangle acoustic feature extraction and linguistic feature extraction, making sure that valuable knowledge learned from ASR and MT tasks can be effectively leveraged for ST training. Besides, every module in pre-training can be utilized in fine-tuning, alleviating the subnet waste problem.

Follow BIBREF9 inaguma2018speech, we use CNN-BiLSTM architecture to build our model. Specifically, the input features $\mathbf {x}$ are organized as a sequence of feature vectors in length $T_x$. Then, $\mathbf {x}$ is passed into a stack of two convolutional layers followed by max-pooling:

where $\mathbf {v}^{(l-1)}$ is feature maps in last layer and $\mathbf {W}^{(l)}$ is the filter. The max-pooling layers downsample the sequence in length by a total factor of four. The down-sampled feature sequence is further fed into a stack of five bidirectional $d$-dimensional LSTM layers:

where $[;]$ denotes the vector concatenation. The final output representation from the speech encoder is denoted as $\mathbf {h^s}=(h^s_1, \cdots , h^s_{\frac{T_x}{4}})$, where $h_i^s \in \mathbb {R}^d$.

The text encoder $enc_t$ consists of two bidirectional LSTM layers. In ST task, $enc_t$ accepts speech encoder output $\mathbf {h}^s$ as input. While in MT, $enc_t$ consumes the word embedding representation $\mathbf {e^s}$ derived from $\mathbf {y^s}$, where each element $e^s_i$ is computed by choosing the $y_i^s$-th vector from the source embedding matrix $W_{E^s}$. The goal of $enc_t$ is to extract high-level linguistic features like syntactic features or semantic features from lower level subword representations $\mathbf {h}^s$ or $\mathbf {e}^s$. Since $\mathbf {h}^s$ and $\mathbf {e}^s$ belong to different latent space and have different lengths, there remain semantic and length inconsistency problems. We will provide our solutions in Section SECREF21. The output sequence of $enc_t$ is denoted as $\mathbf {h}^t$.

The decoder is defined as two unidirectional LSTM layers with an additive attention $att$. It predicts target sequence $\mathbf {y^{t}}$ by estimating conditional probability $P(\mathbf {y^{t}}|\mathbf {x})$:

Here, $z_k$ is the the hidden state of the deocder RNN at $k$ step and $c_k$ is a time-dependent
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-0ea90dc9a1884aa95d3c707c859e8d1b08b7597d681cdef2c45d621900bd8121

Passage ID: `qasper-passage-v1-0ea90dc9a1884aa95d3c707c859e8d1b08b7597d681cdef2c45d621900bd8121`; retrieval score: 4.2047216682868145.

Word count: 52.

```text
In this section, we first introduce the architecture of TCEN, which consists of two encoders connected in tandem, and one decoder with an attention module. Then we give the pre-training and fine-tuning strategy for TCEN. Finally, we propose our solutions for semantic and length inconsistency problems, which are caused by multi-task learning.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1422.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "b48cc0398f600f20489314a52f50ede783cc5581": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1909.07575:6:0": [
        [
          0,
          162
        ]
      ]
    }
  }
}
```

## Question: 43d8057ff0d3f0c745a7164aed7ed146674630e0

### Question ID and text

Question ID: `43d8057ff0d3f0c745a7164aed7ed146674630e0`; paper ID: `1904.05527`.

```text
What do the models that they compare predict?
```

### Answers

#### Answer: a85e7b72967bf239b184ce129eec43a5e8df773f

```text
{"evidence": ["The main set of experiments uses a Linear Support Vector Machine (Joachims, 1998) to classify dialects using CxG features. Parameters are tuned using the development data. Given the general robust performance of SVMs in the literature relative to other similar classifiers on variation tasks (c.f., Dunn, et al., 2016), we forego a systematic evaluation of classifiers.", "This paper has used data-driven language mapping to select national dialects of English to be included in a global dialect identification model. The main experiments have focused on a dynamic syntactic feature set, showing that it is possible to predict dialect membership within-domain with only a small loss of performance against lexical models. This work raises two remaining problems:"], "extractive_spans": ["national dialects of English"], "free_form_answer": "", "highlighted_evidence": ["The main set of experiments uses a Linear Support Vector Machine (Joachims, 1998) to classify dialects using CxG features.", "This paper has used data-driven language mapping to select national dialects of English to be included in a global dialect identification model. "], "unanswerable": false, "yes_no": null}
```

Evidence location: `1904.05527:6:0`

```text
The main set of experiments uses a Linear Support Vector Machine (Joachims, 1998) to classify dialects using CxG features. Parameters are tuned using the development data. Given the general robust performance of SVMs in the literature relative to other similar classifiers on variation tasks (c.f., Dunn, et al., 2016), we forego a systematic evaluation of classifiers.
```

Evidence location: `1904.05527:9:0`

```text
This paper has used data-driven language mapping to select national dialects of English to be included in a global dialect identification model. The main experiments have focused on a dynamic syntactic feature set, showing that it is possible to predict dialect membership within-domain with only a small loss of performance against lexical models. This work raises two remaining problems:
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-9cb7c34863d496924d85b84cb2a4875ff7e65f8064e90edec7285728b11fe1d3

Passage ID: `qasper-passage-v1-9cb7c34863d496924d85b84cb2a4875ff7e65f8064e90edec7285728b11fe1d3`; retrieval score: 8.061351940760824.

Word count: 253.

```text
This paper has used data-driven language mapping to select national dialects of English to be included in a global dialect identification model. The main experiments have focused on a dynamic syntactic feature set, showing that it is possible to predict dialect membership within-domain with only a small loss of performance against lexical models. This work raises two remaining problems:

First, we know that location-specific content (i.e., place names, place references, national events) can be used for geo-location and text-based models of place. To what degree does a lexical approach capture linguistic variation (i.e., “pop" vs. “soda") and to what degree is it capturing non-linguistic information (i.e., “Melbourne" vs. “London")? This is an essential problem for dialect identification models. A purely syntactic model does not perform as well as a lexical model, but it does come with more guarantees.

Second, we have seen that inner-circle varieties have higher feature densities given the grammars used here. This implies that there are syntactic constructions in varieties like Philippines English that have not been modeled by the grammar induction component. While dialect identification can be used to optimize regional weights for known constructions, how can such missing constructions be adapted? This remains a challenge. While the less proto-typical dialects have higher F1s (i.e., Pakistan English), they also have lower feature densities. This indicates that some of their constructions are missing from the grammar. Nevertheless, this paper has shown that a broader syntactic feature space can be used to model the difference between many national varieties of English.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.05527:9:0` | full | 0:389 |

#### Rank 2: qasper-passage-v1-8fae756798b1d8b89038c6d7eb382ebb67682a81c908cbbf7539f65008e6303d

Passage ID: `qasper-passage-v1-8fae756798b1d8b89038c6d7eb382ebb67682a81c908cbbf7539f65008e6303d`; retrieval score: 6.660955053394345.

Word count: 400.

```text
This paper combines grammar induction (Dunn, 2018a, 2018b, 2019) and text classification (Joachims, 1998) to model syntactic variation across national varieties of English. This classification-based approach is situated within the task of dialect identification (Section 2) and evaluated against other baselines for the task (Sections 7 and 8). But the focus is modelling syntactic variation on a global-scale using corpus data. On the one hand, the problem is to use a model of syntactic preferences to predict an author's dialect membership (Dunn, 2018c). On the other hand, the problem is to take a spatially-generic grammar of English that is itself learned from raw text (c.f., Zeman, et al., 2017; Zeman, et al., 2018) and adapt that grammar using dialect identification as an optimization task: which constructions are more likely to occur in a specific regional variety?

Because we want a complete global-scale model, we first have to ask: how many national varieties of English are there? This question, considered in Sections 3 and 4, is essential for determining the inventory of regional varieties that need to be included in the dialect identification task. This paper uses data-driven language mapping to find out where English is consistently used, given web data and Twitter data, in order to avoid the arbitrary selection of dialect areas. This is important for ensuring that each construction in the grammar receives the best regional weighting.

What syntactic features are needed to represent variation in English? As discussed in Section 6, this paper uses grammar induction on a large background corpus to provide a replicable and dynamic feature space in order to avoid arbitrary limitations (e.g., lists of function words). The other side of this problem is to optimize grammar induction for regional dialects by using an identification task to learn regional weights for each part of the grammar: how much does a single generic grammar of English vary across dialects? To what degree does it represent a single dominant dialect?

Finally, a corpus-based approach to variation is restricted to the specific domains or registers that are present in the corpus. To what degree is such a model of variation limited to a specific register? This paper uses both web-crawled corpora and social media corpora to explore the robustness of dialect models across domains (Section 8). Along these same lines, how robust is a model of syntactic variation to the presence of a few highly predictive features?
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-42e4116cc140c0c3fb195bca00d0fbe176b6e44f0f1caea0a421e86e77baf3fc

Passage ID: `qasper-passage-v1-42e4116cc140c0c3fb195bca00d0fbe176b6e44f0f1caea0a421e86e77baf3fc`; retrieval score: 4.223843644456281.

Word count: 400.

```text
The main set of experiments uses a Linear Support Vector Machine (Joachims, 1998) to classify dialects using CxG features. Parameters are tuned using the development data. Given the general robust performance of SVMs in the literature relative to other similar classifiers on variation tasks (c.f., Dunn, et al., 2016), we forego a systematic evaluation of classifiers.

We start, in Table 5, with an evaluation of baselines by feature type and dataset. We have two general types of features: purely syntactic representations (CxG-1, CxG-2, Function words) and potentially topic-based features (unigrams, bigrams, trigrams). The highest performing feature on both datasets is simple lexical unigrams, at 30k dimensions. We use a hashing vectorizer to avoid a region-specific bias: the vectorizer does not need to be trained or initialized against a specific dataset so there is no chance that one of the varieties will be over-represented in determining which n-grams are included. But this has the side-effect of preventing the inspection of individual features. Vectors for all experiments are available, along with the trained models that depend on these vectors.

As n increases, n-grams tend to represent structural rather than topical information. In this case, performance decreases as n increases. We suggest that this decrease provides an indication that the performance of unigrams is based on location-specific content (e.g., “Chicago" vs. “Singapore") rather than on purely linguistic lexical variation (e.g., “jeans" vs. “denim"). How do we differentiate between predictions based on place-names, those based on place-specific content, and those based on dialectal variation? That is a question for future work. For example, is it possible to identify and remove location-specific content terms? Here we focus instead on using syntactic representations that are not subject to such interference.

Within syntactic features, function words perform the worst on both datasets with F1s of 0.65 and 0.55. This is not surprising because function words in English do not represent syntactic structures directly; they are instead markers of the types of structures being used. CxG-1 comes next with F1s of 0.80 and 0.76, a significant improvement over the function-word baseline but not approaching unigrams. Note that the experiments using this same grammar in previous work (Dunn, 2018c) were applied to samples of 2k words each. Finally, CxG-2 performs the best, with F1s of 0.96 and 0.92, falling behind unigrams but rivaling bigrams and surpassing trigrams. Because of this, the more detailed experiments below focus only on the
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.05527:6:0` | full | 0:369 |

#### Rank 4: qasper-passage-v1-75b5ab98308382704344232f30b3e3f65cfaea60b30e1255c381c0b7eb3fbec3

Passage ID: `qasper-passage-v1-75b5ab98308382704344232f30b3e3f65cfaea60b30e1255c381c0b7eb3fbec3`; retrieval score: 3.5727991957881695.

Word count: 303.

```text
false negatives (the umbrella-grammar is missing constructions that are important to a regional dialect). For dialect identification as a task, only missing constructions will reduce prediction performance.

How well do CxG-1 and CxG-2 represent the corpora from each regional variety? While prediction accuracies are the ultimate evaluation, we can also look at the average frequency across all constructions for each national dialect. Because the samples are fixed in length, we would expect the same frequencies across all dialects. On the other hand, false positive constructions (which are contained in the umbrella-grammar but do not occur frequently in a national dialect) will reduce the overall feature density for that dialect. Because the classification results do not directly evaluate false positive constructions, we investigate this in Table 4 using the average feature density: the total average frequency per sample, representing how many syntactic constructions from the umbrella-grammar are present in each regional dialect. This is adjusted to show differences from the average for each grammar (i.e., CxG-1 and CxG-2 are each calculated independently).

First, CxG-1 has a smaller range of feature densities, with the lowest variety (Portugal English) being only 10.41% different from the highest variety (UK English). This range is much higher for CxG-2, with a 36.01% difference between the lowest variety (Philippines English) and the highest variety (Irish English). One potential explanation for the difference is that CxG-2 is a better fit for the inner-circle dominated training data. This is a question for future work. For now, both grammars pattern together in a general sense: the highest feature density is found in UK English and varieties more similar to UK English (Ireland, Australia). The lowest density is found in under-represented varieties such as Portugal English or Philippines English. Any grammar-adaptation based on dialect identification will struggle to add unknown constructions from these varieties.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-1526e46c7ec7d12e888a017b9f2d6fd6a72e3f0d1e86037508bce188d5b1d664

Passage ID: `qasper-passage-v1-1526e46c7ec7d12e888a017b9f2d6fd6a72e3f0d1e86037508bce188d5b1d664`; retrieval score: 3.1778671747165474.

Word count: 400.

```text
The goal of this paper is to model syntactic variation across all major or robust varieties of English. But how do we know which varieties should be included? Rather than select some set of varieties based on convenience, we take a data-driven approach by collecting global web-crawled data and social media data to determine where English is used. This approach is biased towards developed countries with access to digital technologies. As shown in Table 1, however, enough global language data is available from both sources to determine where national varieties of English exist.

Data comes from two sources of digital texts: web pages from the Common Crawl and social media from Twitter. Both types of data have been used previously to study dialectal and spatial variation in language. More commonly, geo-referenced Twitter data has been taken to represent language-use in specific places (e.g., Eisenstein, et al., 2010; Roller, et al., 2012; Kondor, et al., 2013; Mocanu, et al., 2013; Eisenstein, et al., 2014; Graham, et al., 2014; Donoso & Sanchez, 2017); regional variation in Twitter usage was also the subject of a shared task at PAN-17 (Rangel, et al., 2017). Web-crawled data has also been curated and prepared for the purpose of studying spatial variation (Goldhahn, et al., 2012; Davies & Fuchs, 2015), including the use of country-level domains for geo-referencing (Cook & Brinton, 2017). This paper builds on such previous work by systematically collecting geo-referenced data from both sources on a global scale. The full web corpus is available for download.

For the Common Crawl data (abbreviated as CC), language samples are geo-located using country-specific top-level domains. The assumption is that a language sample from a web-site under the .ca domain originated from Canada (c.f., Cook & Brinton, 2017). This approach to regionalization does not assume that whoever produced that language sample was born in Canada or represents a traditional Canadian dialect group; rather, the assumption is only that the sample represents someone in Canada who is producing language data. Some countries are not available because their top-level domains are used for other purposes (i.e., .ai, .fm, .io, .ly, .ag, .tv). Domains that do not contain geographic information are also removed from consideration (e.g., .com sites). The Common Crawl dataset covers 2014 through the end of 2017, totalling 81.5 billion web pages. As shown in Table 1, after processing this produces a corpus of 16.65 billion words.

The basic
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1756.

Fully covered answer annotations: a85e7b72967bf239b184ce129eec43a5e8df773f.

Missing evidence by answer annotation:

```text
{
  "a85e7b72967bf239b184ce129eec43a5e8df773f": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: b2fab9ffbcf1d6ec6d18a05aeb6e3ab9a4dbf2ae

### Question ID and text

Question ID: `b2fab9ffbcf1d6ec6d18a05aeb6e3ab9a4dbf2ae`; paper ID: `1908.10449`.

```text
How do they train models in this setup?
```

### Answers

#### Answer: 33b2d26d064251c196238b0c3c455b208680f5fc

```text
{"evidence": ["The key idea behind our proposed interactive MRC (iMRC) is to restrict the document context that a model observes at one time. Concretely, we split a supporting document into its component sentences and withhold these sentences from the model. Given a question, the model must issue commands to observe sentences in the withheld set; we equip models with actions such as Ctrl+F (search for token) and stop for searching through partially observed documents. A model searches iteratively, conditioning each command on the input question and the sentences it has observed previously. Thus, our task requires models to `feed themselves' rather than spoon-feeding them with information. This casts MRC as a sequential decision-making problem amenable to reinforcement learning (RL)."], "extractive_spans": ["Thus, our task requires models to `feed themselves' rather than spoon-feeding them with information. This casts MRC as a sequential decision-making problem amenable to reinforcement learning (RL)."], "free_form_answer": "", "highlighted_evidence": ["The key idea behind our proposed interactive MRC (iMRC) is to restrict the document context that a model observes at one time. Concretely, we split a supporting document into its component sentences and withhold these sentences from the model. Given a question, the model must issue commands to observe sentences in the withheld set; we equip models with actions such as Ctrl+F (search for token) and stop for searching through partially observed documents. A model searches iteratively, conditioning each command on the input question and the sentences it has observed previously. Thus, our task requires models to `feed themselves' rather than spoon-feeding them with information. This casts MRC as a sequential decision-making problem amenable to reinforcement learning (RL)."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1908.10449:0:2`

```text
The key idea behind our proposed interactive MRC (iMRC) is to restrict the document context that a model observes at one time. Concretely, we split a supporting document into its component sentences and withhold these sentences from the model. Given a question, the model must issue commands to observe sentences in the withheld set; we equip models with actions such as Ctrl+F (search for token) and stop for searching through partially observed documents. A model searches iteratively, conditioning each command on the input question and the sentences it has observed previously. Thus, our task requires models to `feed themselves' rather than spoon-feeding them with information. This casts MRC as a sequential decision-making problem amenable to reinforcement learning (RL).
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-0686797a069dca4b956e4d70f0906ed25fafc6086e28ed832c6fc1be32085d1e

Passage ID: `qasper-passage-v1-0686797a069dca4b956e4d70f0906ed25fafc6086e28ed832c6fc1be32085d1e`; retrieval score: 7.887610100808342.

Word count: 400.

```text
Many machine reading comprehension (MRC) datasets have been released in recent years BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4 to benchmark a system's ability to understand and reason over natural language. Typically, these datasets require an MRC model to read through a document to answer a question about information contained therein.

The supporting document is, more often than not, static and fully observable. This raises concerns, since models may find answers simply through shallow pattern matching; e.g., syntactic similarity between the words in questions and documents. As pointed out by BIBREF5, for questions starting with when, models tend to predict the only date/time answer in the supporting document. Such behavior limits the generality and usefulness of MRC models, and suggests that they do not learn a proper `understanding' of the intended task. In this paper, to address this problem, we shift the focus of MRC data away from `spoon-feeding' models with sufficient information in fully observable, static documents. Instead, we propose interactive versions of existing MRC tasks, whereby the information needed to answer a question must be gathered sequentially.

The key idea behind our proposed interactive MRC (iMRC) is to restrict the document context that a model observes at one time. Concretely, we split a supporting document into its component sentences and withhold these sentences from the model. Given a question, the model must issue commands to observe sentences in the withheld set; we equip models with actions such as Ctrl+F (search for token) and stop for searching through partially observed documents. A model searches iteratively, conditioning each command on the input question and the sentences it has observed previously. Thus, our task requires models to `feed themselves' rather than spoon-feeding them with information. This casts MRC as a sequential decision-making problem amenable to reinforcement learning (RL).

As an initial case study, we repurpose two well known, related corpora with different difficulty levels for our interactive MRC task: SQuAD and NewsQA. Table TABREF2 shows some examples of a model performing interactive MRC on these datasets. Naturally, our reframing makes the MRC problem harder; however, we believe the added demands of iMRC more closely match web-level QA and may lead to deeper comprehension of documents' content.

The main contributions of this work are as follows:

We describe a method to make MRC datasets interactive and formulate the new task as an RL problem.

We develop a baseline agent that combines a top performing
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.10449:0:2` | full | 0:778 |

#### Rank 2: qasper-passage-v1-e876e0a87e568831301d53ce697bf01c2e9cd1c38b3cadf13cd03e35a7bd6560

Passage ID: `qasper-passage-v1-e876e0a87e568831301d53ce697bf01c2e9cd1c38b3cadf13cd03e35a7bd6560`; retrieval score: 6.792043220149556.

Word count: 400.

```text
Skip-reading BIBREF6, BIBREF7, BIBREF8 is an existing setting in which MRC models read partial documents. Concretely, these methods assume that not all tokens in the input sequence are useful, and therefore learn to skip irrelevant tokens based on the current input and their internal memory. Since skipping decisions are discrete, the models are often optimized by the REINFORCE algorithm BIBREF9. For example, the structural-jump-LSTM proposed in BIBREF10 learns to skip and jump over chunks of text. In a similar vein, BIBREF11 designed a QA task where the model reads streaming data unidirectionally, without knowing when the question will be provided. Skip-reading approaches are limited in that they only consider jumping over a few consecutive tokens and the skipping operations are usually unidirectional. Based on the assumption that a single pass of reading may not provide sufficient information, multi-pass reading methods have also been studied BIBREF12, BIBREF13.

Compared to skip-reading and multi-turn reading, our work enables an agent to jump through a document in a more dynamic manner, in some sense combining aspects of skip-reading and re-reading. For example, it can jump forward, backward, or to an arbitrary position, depending on the query. This also distinguishes the model we develop in this work from ReasoNet BIBREF13, where an agent decides when to stop unidirectional reading.

Recently, BIBREF14 propose DocQN, which is a DQN-based agent that leverages the (tree) structure of documents and navigates across sentences and paragraphs. The proposed method has been shown to outperform vanilla DQN and IR baselines on TriviaQA dataset. The main differences between our work and DocQA include: iMRC does not depend on extra meta information of documents (e.g., title, paragraph title) for building document trees as in DocQN; our proposed environment is partially-observable, and thus an agent is required to explore and memorize the environment via interaction; the action space in our setting (especially for the Ctrl+F command as defined in later section) is arguably larger than the tree sampling action space in DocQN.

Closely related to iMRC is work by BIBREF15, in which the authors introduce a collection of synthetic tasks to train and test information-seeking capabilities in neural models. We extend that work by developing a realistic and challenging text-based task.

Broadly speaking, our approach is also linked to the optimal stopping problem in the literature Markov decision processes (MDP) BIBREF16, where at each time-step the agent either continues or stops and accumulates reward.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-79ade64e7a952a5a69e1b20f62ff22aa31cebe97f8400a47c97d9d27313be843

Passage ID: `qasper-passage-v1-79ade64e7a952a5a69e1b20f62ff22aa31cebe97f8400a47c97d9d27313be843`; retrieval score: 5.633905590004382.

Word count: 279.

```text
In this work, we propose and explore the direction of converting MRC datasets into interactive environments. We believe interactive, information-seeking behavior is desirable for neural MRC systems when knowledge sources are partially observable and/or too large to encode in their entirety — for instance, when searching for information on the internet, where knowledge is by design easily accessible to humans through interaction.

Despite being restricted, our proposed task presents major challenges to existing techniques. iMRC lies at the intersection of NLP and RL, which is arguably less studied in existing literature. We hope to encourage researchers from both NLP and RL communities to work toward solving this task.

For our baseline, we adopted an off-the-shelf, top-performing MRC model and RL method. Either component can be replaced straightforwardly with other methods (e.g., to utilize a large-scale pretrained language model).

Our proposed setup and baseline agent presently use only a single word with the query command. However, a host of other options should be considered in future work. For example, multi-word queries with fuzzy matching are more realistic. It would also be interesting for an agent to generate a vector representation of the query in some latent space. This vector could then be compared with precomputed document representations (e.g., in an open domain QA dataset) to determine what text to observe next, with such behavior tantamount to learning to do IR.

As mentioned, our idea for reformulating existing MRC datasets as partially observable and interactive environments is straightforward and general. Almost all MRC datasets can be used to study interactive, information-seeking behavior through similar modifications. We hypothesize that such behavior can, in turn, help in solving real-world MRC problems involving search.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-b30c5ef544d319fd217df519316e7e3b244f30e7c3af797749f4b90661c5ebf2

Passage ID: `qasper-passage-v1-b30c5ef544d319fd217df519316e7e3b244f30e7c3af797749f4b90661c5ebf2`; retrieval score: 4.946730433859333.

Word count: 121.

```text
iMRC games are interactive environments. We use an RL training algorithm to train the interactive information-gathering behavior of QA-DQN. We adopt the Rainbow algorithm proposed by BIBREF23, which integrates several extensions to the original Deep Q-Learning algorithm BIBREF24. Rainbox exhibits state-of-the-art performance on several RL benchmark tasks (e.g., Atari games).

During game playing, we use a mini-batch of size 10 and push all transitions (observation string, question string, generated command, reward) into a replay buffer of size 500,000. We do not compute losses directly using these transitions. After every 5 game steps, we randomly sample a mini-batch of 64 transitions from the replay buffer, compute loss, and update the network.

Detailed hyper-parameter settings for action generation are shown in Table TABREF38.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-2721f630686ff86bb8070f3fe125bd6683f2cfd9fb2ede11b9b0720971a66480

Passage ID: `qasper-passage-v1-2721f630686ff86bb8070f3fe125bd6683f2cfd9fb2ede11b9b0720971a66480`; retrieval score: 4.520172171667078.

Word count: 122.

```text
Similarly, we use another replay buffer to store question answering transitions (observation string when interaction stops, question string, ground-truth answer).

Because both iSQuAD and iNewsQA are converted from datasets that provide ground-truth answer positions, we can leverage this information and train the question answerer with supervised learning. Specifically, we only push question answering transitions when the ground-truth answer is in the observation string. For each transition, we convert the ground-truth answer head- and tail-positions from the SQuAD and NewsQA datasets to positions in the current observation string. After every 5 game steps, we randomly sample a mini-batch of 64 transitions from the replay buffer and train the question answerer using the Negative Log-Likelihood (NLL) loss. We use a dropout rate of 0.1.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1322.

Fully covered answer annotations: 33b2d26d064251c196238b0c3c455b208680f5fc.

Missing evidence by answer annotation:

```text
{
  "33b2d26d064251c196238b0c3c455b208680f5fc": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: 90f80a94fabaab72833256572db1d449c2779beb

### Question ID and text

Question ID: `90f80a94fabaab72833256572db1d449c2779beb`; paper ID: `2003.01472`.

```text
Did they experiment with the tool?
```

### Answers

#### Answer: 26563c5b8f73a45997be3b0b69f71f754b366e51

```text
{"evidence": ["We present two use cases on which Seshat was developped: clinical interviews, and daylong child-centered recordings."], "extractive_spans": [], "free_form_answer": "", "highlighted_evidence": ["We present two use cases on which Seshat was developped: clinical interviews, and daylong child-centered recordings."], "unanswerable": false, "yes_no": true}
```

Evidence location: `2003.01472:12:0`

```text
We present two use cases on which Seshat was developped: clinical interviews, and daylong child-centered recordings.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-366752200fd95c3cf87920868b1f2d4df1a420f1d58466be410b50d4f0563908

Passage ID: `qasper-passage-v1-366752200fd95c3cf87920868b1f2d4df1a420f1d58466be410b50d4f0563908`; retrieval score: 4.7854629257738655.

Word count: 363.

```text
Self-hosted annotation systems. There are many standalone solutions for the transcription of speech data that are already used by researchers: Transcriber BIBREF3, Wavesurfer BIBREF4, Praat BIBREF5, ELAN BIBREF6, XTrans BIBREF7. These systems allow the playback of sound data and the construction of different layers of annotations with various specifications, with some advanced capabilities (such as annotations with hierarchical or no relationship between layers, number of audio channels, video support). Yet, these solutions lack a management system: each researcher must track the files assigned to annotators and build a pipeline to parse (and eventually check) the output annotation files. Moreover, checking can only be done once the annotations have been submitted to the researchers. This task becomes quickly untraceable as the number of files and annotators grow. In addition, most of these transcription systems do not provide a way to evaluate consistency (intra- and inter-annotator agreement) that would be appropriate for speech data BIBREF8.

Web-based annotations systems. There are several web-based annotation systems for the annotation of audio data. Among them we find light-weight systems, like the VIA software BIBREF9 or Praat on the web BIBREF10 that allow to build simple layers of annotations. However, they do not provide a proper management system for a pool of annotators nor do they integrate annotation checking.

On the other side of the spectrum, there are more sophisticated systems with various capabilities. Camomille BIBREF11 and the EMU-SDMS system (that can also be used offline) BIBREF12 allow to work with speech data and to distribute the tasks to several annotators. But these systems require expertise in web hosting and technologies to deploy and modify them.

Finally, WebAnno BIBREF13 and GATE Teamware BIBREF14 are the tools that most closely match our main contributions regarding quality control (conformity and consistency checking), annotators' management and flexibility. WebAnno includes consistency checking with the integration of different metrics BIBREF15. However, these tools have only been built for text data. The format and all the custom layers have been designed for Natural Language Processing tasks. Porting WebAnno to support speech data seemed a major engineering challenge. That is why it appeared necessary to develop a new and user-friendly tool addressed to the speech community.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-757efabdff6c088501ee376f68054a3caf93c90cc6132fd218546442a950d453

Passage ID: `qasper-passage-v1-757efabdff6c088501ee376f68054a3caf93c90cc6132fd218546442a950d453`; retrieval score: 4.291364903127755.

Word count: 271.

```text
Seshat was intially developped to study the impact of Huntington's Disease BIBREF17 on speech and language production. One hundred and fifty two interviews between a neuropsychologist and a patient with the Huntington's Disease (HD) were recorded between June 2018 and November 2019. The campaign manager created a campaign with multiple tiers to annotate the turn takings and the speech/non speech boundaries of the utterances of the patient. For both tasks, the annotations did not need to cover completely the audio (sparsity property mentioned above). For the Turn-taking annotations, there are 3 pre-defined tiers, each one with a single class ('Patient', 'Non-Patient', and 'Noise'), which results in possible overlap between these classes. For the Utterance annotations, there is only one pre-defined class ('Utterance').

To this date, a total of 67 files have been fully annotated with the help of Seshat by a cohort of 18 speech pathologist students (see Figure FIGREF33). Among these, 16 have been done by 2 different annotators independently with the Double-annotator task. The results are summarised in Table TABREF34.

Even though there are more categories for Turn-Takings than Utterance (gut2004measuring reported that the more categories the more the task is difficult in speech annotations), the mean $\gamma $ for the Turn-Takings $\gamma = 0.64$ is slightly higher than the one for Utterance $\gamma = 0.61$. And the range of values for the Turn-Takings is smaller than the Utterance. Indeed, the speech pathologists reported the difficulty to annotate the boundary of utterances in spontaneous speech, with several ambiguous cases due to pauses. These results will help us to redefine the protocol and be more precise on the given instructions.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-81caa8be7e94a8031c3d468400be57bef713bbcf084dd31667493fd51d019e44

Passage ID: `qasper-passage-v1-81caa8be7e94a8031c3d468400be57bef713bbcf084dd31667493fd51d019e44`; retrieval score: 3.893759509286208.

Word count: 160.

```text
The Campaign manager can easily define and monitor annotation campaign. As shown in Figure FIGREF33, the online form enable to choose corpora, pre-define and pre-configure the annotations scheme (tiers and parsers). There are 2 types of tiers already implemented by default: one with no check at all, and one with pre-defined categories. For the latter, these categories are pre-defined when the campaign is created.

Only Campaign managers can access and build new campaigns. If Campaign manager have several campaigns they can easily switch between them via the menu bar or get a full overview with the dashboard (See Figure FIGREF26). The campaign managers can visualise the progress of the assigned tasks at the campaign level or more precisely at the task level. They can retrieve all the intermediate files that have been created for each task. For instance, the campaign manager can examine qualitatively and quantitatively what are the annotation differences before the merge phases of the double annotator task.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-88f54a49dec3da81cd6074b8a944612284ffc69371a618713356951591ad531f

Passage ID: `qasper-passage-v1-88f54a49dec3da81cd6074b8a944612284ffc69371a618713356951591ad531f`; retrieval score: 3.6749088951782696.

Word count: 400.

```text
Seshat is a user-friendly web-based interface whose objective is to smoothly manage large campaigns of audio data annotation, see Figure FIGREF8. Below, we describe the several terms used in Seshat's workflow:

[font=, leftmargin=1cm, style=nextline]

A set of audio/speech files that a Campaign Manager wants to annotate. It is indicated either by a folder containing sound files, or by a CSV summarizing a set of files. We support the same formats as Praat so far: WAV, Flac and MP3.

An object that enables the Campaign Manager to assign Annotation Tasks to the Annotators. It references a Corpus, and allows the Manager to track the annotation's tasks progress and completion in real time. At its creation, a Textgrid Checking Scheme can also be defined for that campaign.

It is contained in an Annotation Campaign, it references an audio file from the campaign's designated Audio Corpus, and assigned to Annotators. It can either be a Single Annotator Task (assigned to one Annotator) or a Double Annotator Task (assigned to two annotators, who will annotatote the assigned task in parallel).

A set of rules defining the TextGrid files' structure and content of the annotations. It is set at the beginning of the Annotation Campaign's creation, and is used to enforce that all TextGrids from the campaign contain the same amount of Tiers, with the same names. It can also enforce, for certain chosen tiers, a set of valid annotations.

Users with the rights to create Annotation Campaigns and Annotators user accounts, and assign Annotation Tasks to Annotators.

Users who are assigned a set of Annotation Tasks. Their job is to complete the annotation of the audio files with the Praat software.

If the TextGrid file they submit does not comply with their Annotation Task's TextGrid Checking Scheme, Seshat pinpoint their annotation errors with detailed messages. The annotator can re-submit the concerned file to the platform based on these different feedbacks.

Once they they connected to their instance of Seshat, campaign managers can access ongoing annotation campaigns or create new ones. Campaign managers are able to add annotators, assign annotation tasks and track progress. Annotator see a list of assigned tasks. The first step for them is to download the sound file with its corresponding auto-generated template TextGrid. In the current implementation, the annotation work has to be done locally with Praat. An upcoming version will use of web tools like Praat on the web
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-391a5b1bc2e85edb2228c74ff19c3a20c9c8208db1f079344b43813ba22d8832

Passage ID: `qasper-passage-v1-391a5b1bc2e85edb2228c74ff19c3a20c9c8208db1f079344b43813ba22d8832`; retrieval score: 3.3760648133172473.

Word count: 138.

```text
Seshat is a new tool for the management of audio annotation efforts. Seshat enables users to define their own campaign of annotations. Based on this configuration, Seshat automatically enforces the format of the annotations returned by the annotators. Besides, we also add the capability to finely tailor the parsing of the annotations. Finally, Seshat provides automatic routines to compute the inter-rate agreements that are specifically designed for audio annotations. Seshat lays some foundations for more advanced features, either for the interface or the annotation capabilities. In future work, we plan to implement an automatic task assignments and an integration of a diarization processing step to reduce human effort. Another planned feature is to add possibility for the campaign manager to design more complex annotation workflows such as, for instance, dependencies between tiers or more intermediate steps of annotations.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1332.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "26563c5b8f73a45997be3b0b69f71f754b366e51": {
    "unresolved_evidence": [],
    "paragraphs": {
      "2003.01472:12:0": [
        [
          0,
          116
        ]
      ]
    }
  }
}
```

## Question: 73abb173a3cc973ab229511cf53b426865a2738b

### Question ID and text

Question ID: `73abb173a3cc973ab229511cf53b426865a2738b`; paper ID: `1606.05286`.

```text
What state-of-the-art models are compared against?
```

### Answers

#### Answer: 0f1c509049f53c831e6715cbbe308ae4340e1b37

```text
{"evidence": ["As a comparison to the state of the art methods, Table 1 presents accuracy results of the best Collective Matrix Factorization model, with a latent space dimension of 350, which has been determined by cross-validation on a development set, where the value of each slot is instantiated as the most probable w.r.t the inference procedure presented in Section \"Spectral decomposition model for state tracking in slot-filling dialogs\" . In our experiments, the variance is estimated using standard dataset reshuffling. The same results are obtained for several state of the art methods of generative and discriminative state tracking on this dataset using the publicly available results as reported in BIBREF22 . More precisely, as provided by the state-of-the-art approaches, the accuracy scores computes $p(s^*_{t+1}|s_t,z_t)$ commonly name the joint goal. Our proposition is compared to the 4 baseline trackers provided by the DSTC organisers. They are the baseline tracker (Baseline), the focus tracker (Focus), the HWU tracker (HWU) and the HWU tracker with “original” flag set to (HWU+) respectively. Then a comparison to a maximum entropy (MaxEnt) proposed in BIBREF23 type of discriminative model and finally a deep neural network (DNN) architecture proposed in BIBREF24 as reported also in BIBREF22 is presented."], "extractive_spans": ["a deep neural network (DNN) architecture proposed in BIBREF24 ", "maximum entropy (MaxEnt) proposed in BIBREF23 type of discriminative model"], "free_form_answer": "", "highlighted_evidence": ["Then a comparison to a maximum entropy (MaxEnt) proposed in BIBREF23 type of discriminative model and finally a deep neural network (DNN) architecture proposed in BIBREF24 as reported also in BIBREF22 is presented.\n\n"], "unanswerable": false, "yes_no": null}
```

Evidence location: `1606.05286:9:0`

```text
As a comparison to the state of the art methods, Table 1 presents accuracy results of the best Collective Matrix Factorization model, with a latent space dimension of 350, which has been determined by cross-validation on a development set, where the value of each slot is instantiated as the most probable w.r.t the inference procedure presented in Section "Spectral decomposition model for state tracking in slot-filling dialogs" . In our experiments, the variance is estimated using standard dataset reshuffling. The same results are obtained for several state of the art methods of generative and discriminative state tracking on this dataset using the publicly available results as reported in BIBREF22 . More precisely, as provided by the state-of-the-art approaches, the accuracy scores computes $p(s^*_{t+1}|s_t,z_t)$ commonly name the joint goal. Our proposition is compared to the 4 baseline trackers provided by the DSTC organisers. They are the baseline tracker (Baseline), the focus tracker (Focus), the HWU tracker (HWU) and the HWU tracker with “original” flag set to (HWU+) respectively. Then a comparison to a maximum entropy (MaxEnt) proposed in BIBREF23 type of discriminative model and finally a deep neural network (DNN) architecture proposed in BIBREF24 as reported also in BIBREF22 is presented.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-b1863d7364126dc2e93ee86e3e3f76be3828822f4e561c624cc83a6721aff7f9

Passage ID: `qasper-passage-v1-b1863d7364126dc2e93ee86e3e3f76be3828822f4e561c624cc83a6721aff7f9`; retrieval score: 6.2814094792647905.

Word count: 200.

```text
As a comparison to the state of the art methods, Table 1 presents accuracy results of the best Collective Matrix Factorization model, with a latent space dimension of 350, which has been determined by cross-validation on a development set, where the value of each slot is instantiated as the most probable w.r.t the inference procedure presented in Section "Spectral decomposition model for state tracking in slot-filling dialogs" . In our experiments, the variance is estimated using standard dataset reshuffling. The same results are obtained for several state of the art methods of generative and discriminative state tracking on this dataset using the publicly available results as reported in BIBREF22 . More precisely, as provided by the state-of-the-art approaches, the accuracy scores computes $p(s^*_{t+1}|s_t,z_t)$ commonly name the joint goal. Our proposition is compared to the 4 baseline trackers provided by the DSTC organisers. They are the baseline tracker (Baseline), the focus tracker (Focus), the HWU tracker (HWU) and the HWU tracker with “original” flag set to (HWU+) respectively. Then a comparison to a maximum entropy (MaxEnt) proposed in BIBREF23 type of discriminative model and finally a deep neural network (DNN) architecture proposed in BIBREF24 as reported also in BIBREF22 is presented.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1606.05286:9:0` | full | 0:1317 |

#### Rank 2: qasper-passage-v1-dc0bf0325c72697dd1fd610bf6e86c108f3df5cd7ade680981eb9dc3b1baa213

Passage ID: `qasper-passage-v1-dc0bf0325c72697dd1fd610bf6e86c108f3df5cd7ade680981eb9dc3b1baa213`; retrieval score: 6.006567949091831.

Word count: 289.

```text
As depicted in Section "Generative Dialog State Tracking" , the litterature of the domain can mainly decomposed into three family of approaches, rule-based, generative and discriminative. In previous works on this topics, BIBREF25 formally used particle filters to perform inference in a Bayesian network modeling of the dialog state, BIBREF26 presented a generative tracker and showed how to train an observation model from transcribed data, BIBREF27 grouped indistinguishable dialog states into partitions and consequently performed dialog state tracking on these partitions instead of the individual states, BIBREF11 used a dynamic Bayesian network to represent the dialog model in an approximate form. So, most attention in the dialog state belief tracking literature has been given to generative Bayesian network models until recently as proposed in BIBREF28 and BIBREF11 . On the other hand, the successful use of discriminative models for belief tracking has recently been reported by BIBREF29 and BIBREF5 and was a major theme in the results of the recent edition of the Dialog State Tracking Challenge. In this paper, a latent decomposition type of approach is proposed in order to address this general problem of dialog system. Our method gives encouraging results in comparison to the state of the art dataset and also does not required complex inference at test time because, as detailed in Section "Spectral decomposition model for state tracking in slot-filling dialogs" , the tracking algorithm hold a linear complexity w.r.t the sum of realization of each considered variables defining the state to track which is what we believe is one of the main advantage of this method. Secondly collective matrix factorization paradigm also for data fusion and bias by data type of modeling as successfully performed in matrix factorization based recommender systems BIBREF30 .
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-88047735e141808dc6d6405a63730ecebdfd126ecce5892c9f160ef708c262ba

Passage ID: `qasper-passage-v1-88047735e141808dc6d6405a63730ecebdfd126ecce5892c9f160ef708c262ba`; retrieval score: 4.3955714523046945.

Word count: 400.

```text
most likely result from an NLU module as described in BIBREF1 . However, these rule-based systems are prone to frequent errors as the most likely result is not always the correct one. Moreover, these systems often force the human customer to respond using simple keywords and to explicitly confirm everything they say, creating an experience that diverges considerably from the natural conversational interaction one might hope to achieve as recalled in BIBREF2 . More recent methods employ statistical approaches to estimate the posterior distribution over the dialog states allowing them to represent the uncertainty of the results of the NLU module. Statistical dialog state trackers are commonly categorized into one of two approaches according to how the posterior probability distribution over the state calculation is defined. In the first type, the generative approach uses a generative model of the dialog dynamic that describes how the sequence of utterances are generated by using the hidden dialog state and using Bayes' rule to calculate the posterior distribution of the state. It has been a popular approach for statistical dialog state tracking, since it naturally fits into the Partially Observable Markov Decision Process (POMDP) models as described in BIBREF3 , which is an integrated model for dialog state tracking and dialog strategy optimization. Using this generic formalism of sequential decision processes, the task of dialog state tracking is to calculate the posterior distribution over an hidden state given an history of observations. In the second type, the discriminative approach models the posterior distribution directly through a closed algebraic formulation as a loss minimization problem. Statistical dialog systems, in maintaining a distribution over multiple hypotheses of the true dialog state, are able to behave robustly even in the face of noisy conditions and ambiguity. In this paper, a statistical type of approach of state tracking is proposed by leveraging the recent progress of spectral decomposition methods formalized as bilinear algebraic decomposition and associated inference procedures. The proposed model estimates each state transition with respect to a set of observations and is able to compute the state transition through an inference procedure with a linear complexity with respect to the number of variables and observations.

Roadmap: This paper is structured as follows, Section "Generative Dialog State Tracking" formally defines transactional dialogs and describes the associated problem of statistical dialog state tracking with both the generative and discriminative approaches. Section "Spectral decomposition model for state tracking
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-7a5c0ccf02c262249bdcdca0bbfa24b7d555c6948741a78ae6d83be1d0d5a73a

Passage ID: `qasper-passage-v1-7a5c0ccf02c262249bdcdca0bbfa24b7d555c6948741a78ae6d83be1d0d5a73a`; retrieval score: 4.140166113632246.

Word count: 378.

```text
In this section, the proposed model is presented and the learning and prediction procedures are detailed. The general idea consists in the decomposition of a matrix $M$ , composed of a set of turn's transition as rows and sparse encoding of the corresponding feature variables as columns. More precisely, a row of $M$ is composed with the concatenation of the sparse representation of (1) $s_{t}$ , a state at time $t$ (2) $s_{t+1}$ , a state at time $t+1$ (3) $z_t$ , a set of feature representating the observation. In the considered context, the bag of words composing the current turn is chosen as the observation. The parameter learning procedure is formalized as a matrix decomposition task solved through Alternating Least Square Ridge regression. The ridge regression task allows for an asymmetric penalization of the targeted variables of the state tracking task to perform. Figure 3 illustrates the collective matrix factorization task that constitutes the learning procedure of the state tracking model. The model introduces the component of the decomposed matrix to the form of latent variables $\lbrace A, B, C\rbrace $ , also called embeddings. In the next section, the learning procedure from dialog state transition data and the proper tracking algorithm are described. In other terms, each row of the matrix corresponds to the concatenation of a "one-hot" representation of a state description at time $t$ and a dialog turn at time $t$ and each column of the overall matrix $M$0 corresponds to a consider feature respectively of the state and dialog turn. Such type of modelization of the state tracking problem presents several advantages. First, the model is particularly flexible, the definition of the state and observation spaces are independent of the learning and prediction models and can be adapted to the context of tracking. Second, a bias by data can be applied in order to condition the transition model w.r.t separated matrices to decompose jointly as often proposed in multi-task learning as described in BIBREF17 and collective matrix factorization as detailed in BIBREF18 . Finally, the decomposition method is fast and parallelizable because it mainly leverages on core methods of linear algebra. From our knowledge, this proposition is the first attend to formalize and solve the state tracking task using a matrix decomposition approach.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-76d35dba841269aaa86a3e9b3aa32023f1351b77c32b1767c5fb993e11b1f7c8

Passage ID: `qasper-passage-v1-76d35dba841269aaa86a3e9b3aa32023f1351b77c32b1767c5fb993e11b1f7c8`; retrieval score: 3.7657441108030354.

Word count: 400.

```text
The field of autonomous dialog systems is rapidly growing with the spread of smart mobile devices but it still faces many challenges to become the primary user interface for natural interaction through conversations. Indeed, when dialogs are conducted in noisy environments or when utterances themselves are noisy, correctly recognizing and understanding user utterances presents a real challenge. In the context of call-centers, efficient automation has the potential to boost productivity through increasing the probability of a call's success while reducing the overall cost of handling the call. One of the core components of a state-of-the-art dialog system is a dialog state tracker. Its purpose is to monitor the progress of a dialog and provide a compact representation of past user inputs and system outputs represented as a dialog state. The dialog state encapsulates the information needed to successfully finish the dialog, such as users' goals or requests. Indeed, the term “dialog state” loosely denotes an encapsulation of user needs at any point in a dialog. Obviously, the precise definition of the state depends on the associated dialog task. An effective dialog system must include a tracking mechanism which is able to accurately accumulate evidence over the sequence of turns of a dialog, and it must adjust the dialog state according to its observations. In that sense, it is an essential componant of a dialog systems. However, actual user utterances and corresponding intentions are not directly observable due to errors from Automatic Speech Recognition (ASR) and Natural Language Understanding (NLU), making it difficult to infer the true dialog state at any time of a dialog. A common method of modeling a dialog state is through the use of a slot-filling schema, as reviewed in BIBREF0 . In slot-filling, the state is composed of a predefined set of variables with a predefined domain of expression for each of them. The goal of the dialog system is to efficiently instantiate each of these variables thereby performing an associated task and satisfying the corresponding intent of the user.

Various approaches have been proposed to define dialog state trackers. The traditional methods used in most commercial implementations use hand-crafted rules that typically rely on the most likely result from an NLU module as described in BIBREF1 . However, these rule-based systems are prone to frequent errors as the most likely result is not always the correct one. Moreover, these systems often force the human customer
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1667.

Fully covered answer annotations: 0f1c509049f53c831e6715cbbe308ae4340e1b37.

Missing evidence by answer annotation:

```text
{
  "0f1c509049f53c831e6715cbbe308ae4340e1b37": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: 42084c41343e5a6ae58a22e5bfc5ce987b5173de

### Question ID and text

Question ID: `42084c41343e5a6ae58a22e5bfc5ce987b5173de`; paper ID: `1705.05437`.

```text
Does the paper explore extraction from electronic health records?
```

### Answers

#### Answer: 482b34cc6d8ca0cec7ba3e21662c46863c31bd6d

```text
{"evidence": ["BIBREF5 adopt a machine learning approach for NER. Their NER system extracts medical problems, tests and treatments from discharge summaries and progress notes. They use a semi-Conditional Random Field (semi-CRF) BIBREF6 to output labels over all tokens in the sentence. They use a variety of token, context and sentence level features. They also use some concept mapping features using existing annotation tools, as well as Brown clustering to form 128 clusters over the unlabelled data. The dataset used is the i2b2 2010 challenge dataset. Their system achieves an F-Score of 0.85. BIBREF7 is an incremental paper on NER taggers. It uses 3 types of word-representation techniques (Brown clustering, distributional clustering, word vectors) to improve performance of the NER Conditional Random Field tagger, and achieves marginal F-Score improvements."], "extractive_spans": [], "free_form_answer": "", "highlighted_evidence": ["BIBREF5 adopt a machine learning approach for NER. Their NER system extracts medical problems, tests and treatments from discharge summaries and progress notes.", "The dataset used is the i2b2 2010 challenge dataset. "], "unanswerable": false, "yes_no": true}
```

Evidence location: `1705.05437:1:2`

```text
 BIBREF5 adopt a machine learning approach for NER. Their NER system extracts medical problems, tests and treatments from discharge summaries and progress notes. They use a semi-Conditional Random Field (semi-CRF) BIBREF6 to output labels over all tokens in the sentence. They use a variety of token, context and sentence level features. They also use some concept mapping features using existing annotation tools, as well as Brown clustering to form 128 clusters over the unlabelled data. The dataset used is the i2b2 2010 challenge dataset. Their system achieves an F-Score of 0.85. BIBREF7 is an incremental paper on NER taggers. It uses 3 types of word-representation techniques (Brown clustering, distributional clustering, word vectors) to improve performance of the NER Conditional Random Field tagger, and achieves marginal F-Score improvements.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-ac7ca8e373f817e11ae04af5035ba5710e9d7aa51c76eb94bd19ba4e1d1a6372

Passage ID: `qasper-passage-v1-ac7ca8e373f817e11ae04af5035ba5710e9d7aa51c76eb94bd19ba4e1d1a6372`; retrieval score: 10.63818910604348.

Word count: 238.

```text
The explosion of available scientific articles in the Biomedical domain has led to the rise of Biomedical Information Extraction (BioIE). BioIE systems aim to extract information from a wide spectrum of articles including medical literature, biological literature, electronic health records, etc. that can be used by clinicians and researchers in the field. Often the outputs of BioIE systems are used to assist in the creation of databases, or to suggest new paths for research. For example, a ranked list of interacting proteins that are extracted from biomedical literature, but are not present in existing databases, can allow researchers to make informed decisions about which protein/gene to study further. Interactions between drugs are necessary for clinicians who simultaneously administer multiple drugs to their patients. A database of diseases, treatments and tests is beneficial for doctors consulting in complicated medical cases.

The main problems in BioIE are similar to those in Information Extraction:

This paper discusses, in each section, various methods that have been adopted to solve the listed problems. Each section also highlights the difficulty of Information Extraction tasks in the biomedical domain.

This paper is intended as a primer to Biomedical Information Extraction for current NLP researchers. It aims to highlight the diversity of the various techniques from Information Extraction that have been applied in the Biomedical domain. The state of biomedical text mining is reviewed regularly. For more extensive surveys, consult BIBREF0 , BIBREF1 , BIBREF2 .
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-f80cbafadf148da36848f61bb6d6de04f3aea3e4a1569401f4213403d0f57a91

Passage ID: `qasper-passage-v1-f80cbafadf148da36848f61bb6d6de04f3aea3e4a1569401f4213403d0f57a91`; retrieval score: 4.639326189917749.

Word count: 400.

```text
Named Entity Recognition (NER) in the Biomedical domain usually includes recognition of entities such as proteins, genes, diseases, treatments, drugs, etc. Fact extraction involves extraction of Named Entities from a corpus, usually given a certain ontology. When compared to NER in the domain of general text, the biomedical domain has some characteristic challenges:

Some of the earliest systems were heavily dependent on hand-crafted features. The method proposed in BIBREF4 for recognition of protein names in text does not require any prepared dictionary. The work gives examples of diversity in protein names and lists multiple rules depending on simple word features as well as POS tags.

BIBREF5 adopt a machine learning approach for NER. Their NER system extracts medical problems, tests and treatments from discharge summaries and progress notes. They use a semi-Conditional Random Field (semi-CRF) BIBREF6 to output labels over all tokens in the sentence. They use a variety of token, context and sentence level features. They also use some concept mapping features using existing annotation tools, as well as Brown clustering to form 128 clusters over the unlabelled data. The dataset used is the i2b2 2010 challenge dataset. Their system achieves an F-Score of 0.85. BIBREF7 is an incremental paper on NER taggers. It uses 3 types of word-representation techniques (Brown clustering, distributional clustering, word vectors) to improve performance of the NER Conditional Random Field tagger, and achieves marginal F-Score improvements.

BIBREF8 propose a boostrapping mechanism to bootstrap biomedical ontologies using NELL BIBREF9 , which uses a coupled semi-supervised bootstrapping approach to extract facts from text, given an ontology and a small number of “seed” examples for each category. This interesting approach (called BioNELL) uses an ontology of over 100 categories. In contrast to NELL, BioNELL does not contain any relations in the ontology. BioNELL is motivated by the fact that a lot of scientific literature available online is highly reliable due to peer-review. The authors note that the algorithm used by NELL to bootstrap fails in BioNELL due to ambiguities in biomedical literature, and heavy semantic drift. One of the causes for this is that often common words such as “white”, “dad”, “arm” are used as names of genes- this can easily result in semantic drift in one iteration of the bootstrapping. In order to mitigate this, they use Pointwise Mutual Information scores for corpus level statistics, which attributes a small score to common words. In addition, in
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1705.05437:1:2` | full | 1:853 |

#### Rank 3: qasper-passage-v1-a35fc4f85d939233a87409bd73e3a2608f6af5e2ff85cbcbe07c151169c28401

Passage ID: `qasper-passage-v1-a35fc4f85d939233a87409bd73e3a2608f6af5e2ff85cbcbe07c151169c28401`; retrieval score: 3.081504190771842.

Word count: 400.

```text
use lexical (bag of words, contextual) features as well as syntactic (dependency parse features). They make the “at-least one” assumption, i.e. at least one of the sentences extracted for a given entity-pair contains the relation in database. They model it as a multi-instance learning problem and adopt a graphical model similar to BIBREF24 . They test using manually annotated examples. They note that the F-score achieved are much lesser than that achieved in the general domain in BIBREF24 , and attribute to generally poorer performance of NER tools in the biomedical domain, as well as less training examples. BIBREF25 explore distant supervision methods for protein-protein interaction extraction.

More recently, deep learning methods have been applied to relation extraction in the biomedical domain. One of the main advantages of such methods over traditional feature or kernel based learning methods is that they require minimal feature engineering. In BIBREF26 , skip-gram vectors BIBREF27 are trained over 5.6Gb of unlabelled text. They use these vectors to extract protein-protein interactions by converting them into features for entities, context and the entire sentence. Using an SVM for classification, their method is able to outperform many kernel and feature based methods over a variety of datasets.

BIBREF28 follow a similar method by using word vectors trained on PubMed articles. They use it for the task of relation extraction from clinical text for entities that include problem, treatment and medical test. For a given sentence, given labelled entities, they predict the type of relation exhibited (or None) by the entity pair. These types include “treatment caused medical problem”, “test conducted to investigate medical problem”, “medical problem indicates medical problems”, etc. They use a Convolutional Neural Network (CNN) followed by feedforward neural network architecture for prediction. In addition to pre-trained word vectors as features, for each token they also add features for POS tags, distance from both the entities in the sentence, as well BIO tags for the entities. Their model performs better than a feature based SVM baseline that they train themselves.

The BioNLP'16 Shared Tasks has also introduced some Relation Extraction tasks, in particular the BB3-event subtask that involves predicting whether a “lives-in” relation holds for a Bacteria in a location. Some of the top performing models for this task are deep learning models. BIBREF29 train word embeddings with six billions words of scientific texts from PubMed. They then consider the shortest dependency path between the
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-8969a4016bd5487818865841a307d6f7f50ad1f8458acb1b9f1d52d1c88c4b2d

Passage ID: `qasper-passage-v1-8969a4016bd5487818865841a307d6f7f50ad1f8458acb1b9f1d52d1c88c4b2d`; retrieval score: 2.9486209108106944.

Word count: 400.

```text
Event Extraction in the Biomedical domain is a task that has gained more importance recently. Event Extraction goes beyond Relation Extraction. In Biomedical Event Extraction, events generally refer to a change in the state of biological molecules such as proteins and DNA. Generally, it includes detection of targeted event types such as gene expression, regulation, localisation and transcription. Each event type in addition can have multiple arguments that need to be detected. An additional layer of complexity comes from the fact that events can also be arguments of other events, giving rise to a nested structure. This helps to capture the underlying biology better BIBREF1 . Detecting the event type often involves recognising and classifying trigger words. Often, these words are verbs such as “activates”, “inhibits”, “phosphorylation” that may indicate a single, or sometimes multiple event types. In this section, we will discuss some of the successful models for Event Extraction in some detail.

Event Extraction gained a lot of interest with the availability of an annotated corpus with the BioNLP'09 Shared Task on Event Extraction BIBREF34 . The task involves prediction of trigger words over nine event types such as expression, transcription, catabolism, binding, etc. given only annotation of named entities (proteins, genes, etc.). For each event, its class, trigger expression and arguments need to be extracted. Since the events can be arguments to other events, the final output in general is a graph representation with events and named entities as nodes, and edges that correspond to event arguments. BIBREF33 present a pipeline based method that is heavily dependent on dependency parsing. Their pipeline approach consists of three steps: trigger detection, argument detection and semantic post-processing. While the first two components are learning based systems, the last component is a rule based system. For the BioNLP'09 corpus, only 5% of the events span multiple sentences. Hence the approach does not get affected severely by considering only single sentences. It is important to note that trigger words cannot simply be reduced to a dictionary lookup. This is because a specific word may belong to multiple classes, or may not always be a trigger word for an event. For example, “activate” is found to not be a trigger word in over 70% of the cases. A multi-class SVM is trained for trigger detection on each token, using a large feature set consisting of semantic and syntactic features. It is interesting to
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-fbbf85882f6ed57f57cab0f6391b81446e771626c100d333869bd4911ab3aa5a

Passage ID: `qasper-passage-v1-fbbf85882f6ed57f57cab0f6391b81446e771626c100d333869bd4911ab3aa5a`; retrieval score: 2.5016263036055624.

Word count: 156.

```text
genes- this can easily result in semantic drift in one iteration of the bootstrapping. In order to mitigate this, they use Pointwise Mutual Information scores for corpus level statistics, which attributes a small score to common words. In addition, in contrast to NELL, BioNELL only uses high instances as seeds in the next iteration, but adds low ranking instances to the knowledge base. Since evaluation is not possible using Mechanical Turk or a small number of experts (due to the complexity of the task), they use Freebase BIBREF10 , a knowledge base that has some biomedical concepts as well. The lexicon learned using BioNELL is used to train an NER system. The system shows a very high precision, thereby showing that BioNELL learns very few ambiguous terms.

More recently, deep learning techniques have been developed to further enhance the performance of NER systems. BIBREF11 explore recurrent neural networks for the problem of NER in biomedical text.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1594.

Fully covered answer annotations: 482b34cc6d8ca0cec7ba3e21662c46863c31bd6d.

Missing evidence by answer annotation:

```text
{
  "482b34cc6d8ca0cec7ba3e21662c46863c31bd6d": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: 5871d258f66b00fb716065086f757ef745645bfe

### Question ID and text

Question ID: `5871d258f66b00fb716065086f757ef745645bfe`; paper ID: `1905.10044`.

```text
did they use other pretrained language models besides bert?
```

### Answers

#### Answer: 5e90675cae548d25dc1b0665ced21ff19a8da6e4

```text
{"evidence": ["Our Recurrent +ELMo model uses the language model from BIBREF9 to provide contextualized embeddings to the baseline model outlined above, as recommended by the authors.", "Our OpenAI GPT model fine-tunes the 12 layer 768 dimensional uni-directional transformer from BIBREF27 , which has been pre-trained as a language model on the Books corpus BIBREF36 ."], "extractive_spans": [], "free_form_answer": "", "highlighted_evidence": ["Our Recurrent +ELMo model uses the language model from BIBREF9 to provide contextualized embeddings to the baseline model outlined above, as recommended by the authors.\n\nOur OpenAI GPT model fine-tunes the 12 layer 768 dimensional uni-directional transformer from BIBREF27 , which has been pre-trained as a language model on the Books corpus BIBREF36 ."], "unanswerable": false, "yes_no": true}
```

Evidence location: `1905.10044:11:2`

```text
Our Recurrent +ELMo model uses the language model from BIBREF9 to provide contextualized embeddings to the baseline model outlined above, as recommended by the authors.
```

Evidence location: `1905.10044:11:3`

```text
Our OpenAI GPT model fine-tunes the 12 layer 768 dimensional uni-directional transformer from BIBREF27 , which has been pre-trained as a language model on the Books corpus BIBREF36 .
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-c3650d90f4820e127f267789c9d09384f10c465908df835aaa22291be092af2e

Passage ID: `qasper-passage-v1-c3650d90f4820e127f267789c9d09384f10c465908df835aaa22291be092af2e`; retrieval score: 3.6979365666612845.

Word count: 400.

```text
Yes/No questions make up a subset of the reading comprehension datasets CoQA BIBREF3 , QuAC BIBREF4 , and HotPotQA BIBREF5 , and are present in the ShARC BIBREF10 dataset. These datasets were built to challenge models to understand conversational QA (for CoQA, ShARC and QuAC) or multi-step reasoning (for HotPotQA), which complicates our goal of using yes/no questions to test inferential abilities. Of the four, QuAC is the only one where the question authors were not allowed to view the text being used to answer their questions, making it the best candidate to contain naturally occurring questions. However, QuAC still heavily prompts users, including limiting their questions to be about pre-selected Wikipedia articles, and is highly class imbalanced with 80% “yes" answers.

The MS Marco dataset BIBREF11 , which contains questions with free-form text answers, also includes some yes/no questions. We experiment with heuristically identifying them in Section SECREF4 , but this process can be noisy and the quality of the resulting annotations is unknown. We also found the resulting dataset is class imbalanced, with 80% “yes" answers.

Yes/No QA has been used in other contexts, such as the templated bAbI stories BIBREF12 or some Visual QA datasets BIBREF13 , BIBREF14 . We focus on answering yes/no questions using natural language text.

Question answering for reading comprehension in general has seen a great deal of recent work BIBREF15 , BIBREF16 , and there have been many recent attempts to construct QA datasets that require advanced reasoning abilities BIBREF5 , BIBREF17 , BIBREF18 , BIBREF19 , BIBREF20 . However, these attempts typically involve engineering data to be more difficult by, for example, explicitly prompting users to write multi-step questions BIBREF5 , BIBREF18 , or filtering out easy questions BIBREF19 . This risks resulting in models that do not have obvious end-use applications since they are optimized to perform in an artificial setting. In this paper, we show that yes/no questions have the benefit of being very challenging even when they are gathered from natural sources.

Natural language inference is also a well studied area of research, particularly on the MultiNLI BIBREF21 and SNLI BIBREF22 datasets. Other sources of entailment data include the PASCAL RTE challenges BIBREF23 , BIBREF24 or SciTail BIBREF25 . We note that, although SciTail, RTE-6 and RTE-7 did not use crowd workers to generate candidate statements, they still use sources (multiple choices questions or document summaries) that were
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-115fb6a1eea0c991187ac5a9b7f93d9e750d7e25914b4306aa6e24be0a468d0e

Passage ID: `qasper-passage-v1-115fb6a1eea0c991187ac5a9b7f93d9e750d7e25914b4306aa6e24be0a468d0e`; retrieval score: 3.50241142539586.

Word count: 400.

```text
Understanding what facts can be inferred to be true or false from text is an essential part of natural language understanding. In many cases, these inferences can go well beyond what is immediately stated in the text. For example, a simple sentence like “Hanna Huyskova won the gold medal for Belarus in freestyle skiing." implies that (1) Belarus is a country, (2) Hanna Huyskova is an athlete, (3) Belarus won at least one Olympic event, (4) the USA did not win the freestyle skiing event, and so on. Work completed while interning at Google. Also affiliated with Columbia University, work done at Google.

To test a model's ability to make these kinds of inferences, previous work in natural language inference (NLI) proposed the task of labeling candidate statements as being entailed or contradicted by a given passage. However, in practice, generating candidate statements that test for complex inferential abilities is challenging. For instance, evidence suggests BIBREF0 , BIBREF1 , BIBREF2 that simply asking human annotators to write candidate statements will result in examples that typically only require surface-level reasoning.

In this paper we propose an alternative: we test models on their ability to answer naturally occurring yes/no questions. That is, questions that were authored by people who were not prompted to write particular kinds of questions, including even being required to write yes/no questions, and who did not know the answer to the question they were asking. Figure contains some examples from our dataset. We find such questions often query for non-factoid information, and that human annotators need to apply a wide range of inferential abilities when answering them. As a result, they can be used to construct highly inferential reading comprehension datasets that have the added benefit of being directly related to the practical end-task of answering user yes/no questions.

Yes/No questions do appear as a subset of some existing datasets BIBREF3 , BIBREF4 , BIBREF5 . However, these datasets are primarily intended to test other aspects of question answering (QA), such as conversational QA or multi-step reasoning, and do not contain naturally occurring questions.

We follow the data collection method used by Natural Questions (NQ) BIBREF6 to gather 16,000 naturally occurring yes/no questions into a dataset we call BoolQ (for Boolean Questions). Each question is paired with a paragraph from Wikipedia that an independent annotator has marked as containing the answer. The task is then to take a
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-a581a115500f25c31fdf6e5720557afb94b1dcb828c8c45399bd5c8fcd13a0e6

Passage ID: `qasper-passage-v1-a581a115500f25c31fdf6e5720557afb94b1dcb828c8c45399bd5c8fcd13a0e6`; retrieval score: 3.3233801590682495.

Word count: 400.

```text
Why do natural yes/no questions require inference so often? We hypothesize that there are several factors. First, we notice factoid questions that ask about simple properties of entities, such as “Was Obama born in 1962?", are rare. We suspect this is because people will almost always prefer to phrase such questions as short-answer questions (e.g., “When was Obama born?"). Thus, there is a natural filtering effect where people tend to use yes/no questions exactly when they want more complex kinds of information.

Second, both the passages and questions rarely include negation. As a result, detecting a “no" answer typically requires understanding that a positive assertion in the text excludes, or makes unlikely, a positive assertion in the question. This requires reasoning that goes beyond paraphrasing (see the “Other-Inference" or “Implicit" examples).

We also think it was important that annotators only had to answer questions, rather than generate them. For example, imagine trying to construct questions that fall into the categories of “Missing Mention" or “Implicit". While possible, it would require a great deal of thought and creativity. On the other hand, detecting when a yes/no question can be answered using these strategies seems much easier and more intuitive. Thus, having annotators answer pre-existing questions opens the door to building datasets that contain more inference and have higher quality labels.

A surprising result from our work is that the datasets that more closely resemble the format of BoolQ, meaning they contain questions and multi-sentence passages, such as SQuAD 2.0, RACE, or Y/N MS Marco, were not very useful for transfer. The entailment datasets were stronger despite consisting of sentence pairs. This suggests that adapting from sentence-pair input to question/passage input was not a large obstacle to achieving transfer. Preliminary work found attempting to convert the yes/no questions in BoolQ into declarative statements did not improve transfer from MultiNLI, which supports this hypothesis.

The success of MultiNLI might also be surprising given recent concerns about the generalization abilities of models trained on it BIBREF37 , particularly related to “annotation artifacts" caused by using crowd workers to write the hypothesis statements BIBREF0 . We have shown that, despite these weaknesses, it can still be an important starting point for models being used on natural data.

We hypothesize that a key advantage of MultiNLI is that it contains examples of contradictions. The other sources of transfer we consider, including the next-sentence-selection objective in BERT,
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-846fce24263fe4e99296cb301a9de26b9c43e419999749f354c13607182a44f2

Passage ID: `qasper-passage-v1-846fce24263fe4e99296cb301a9de26b9c43e419999749f354c13607182a44f2`; retrieval score: 2.9442748578365956.

Word count: 269.

```text
the PASCAL RTE challenges BIBREF23 , BIBREF24 or SciTail BIBREF25 . We note that, although SciTail, RTE-6 and RTE-7 did not use crowd workers to generate candidate statements, they still use sources (multiple choices questions or document summaries) that were written by humans with knowledge of the premise text. Using naturally occurring yes/no questions ensures even greater independence between the questions and premise text, and ties our dataset to a clear end-task. BoolQ also requires detecting entailment in paragraphs instead of sentence pairs.

Transfer learning for entailment has been studied in GLUE BIBREF7 and SentEval BIBREF26 . Unsupervised pre-training in general has recently shown excellent results on many datasets, including entailment data BIBREF9 , BIBREF8 , BIBREF27 .

Converting short-answer or multiple choice questions into entailment examples, as we do when experimenting with transfer learning, has been proposed in several prior works BIBREF28 , BIBREF29 , BIBREF25 . In this paper we found some evidence suggesting that these approaches are less effective than using crowd-sourced entailment examples when it comes to transferring to natural yes/no questions.

Contemporaneously with our work, BIBREF30 showed that pre-training on supervised tasks could be beneficial even when using pre-trained language models, especially for a textual entailment task. Our work confirms these results for yes/no question answering.

This work builds upon the Natural Questions (NQ) BIBREF6 , which contains some natural yes/no questions. However, there are too few (about 1% of the corpus) to make yes/no QA a very important aspect of that task. In this paper, we gather a large number of additional yes/no questions in order to construct a dedicated yes/no QA dataset.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-8965651711f0effebbbb2ead83ba91dada82704b5db2db2f2bd38eda6cdbb10f

Passage ID: `qasper-passage-v1-8965651711f0effebbbb2ead83ba91dada82704b5db2db2f2bd38eda6cdbb10f`; retrieval score: 2.706161973047835.

Word count: 250.

```text
16,000 naturally occurring yes/no questions into a dataset we call BoolQ (for Boolean Questions). Each question is paired with a paragraph from Wikipedia that an independent annotator has marked as containing the answer. The task is then to take a question and passage as input, and to return “yes" or “no" as output. Figure contains some examples, and Appendix SECREF17 contains additional randomly selected examples.

Following recent work BIBREF7 , we focus on using transfer learning to establish baselines for our dataset. Yes/No QA is closely related to many other NLP tasks, including other forms of question answering, entailment, and paraphrasing. Therefore, it is not clear what the best data sources to transfer from are, or if it will be sufficient to just transfer from powerful pre-trained language models such as BERT BIBREF8 or ELMo BIBREF9 . We experiment with state-of-the-art unsupervised approaches, using existing entailment datasets, three methods of leveraging extractive QA data, and using a few other supervised datasets.

We found that transferring from MultiNLI, and the unsupervised pre-training in BERT, gave us the best results. Notably, we found these approaches are surprisingly complementary and can be combined to achieve a large gain in performance. Overall, our best model reaches 80.43% accuracy, compared to 62.31% for the majority baseline and 90% human accuracy. In light of the fact BERT on its own has achieved human-like performance on several NLP tasks, this demonstrates the high degree of difficulty of our dataset. We present our data and code at https://goo.gl/boolq.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1719.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "5e90675cae548d25dc1b0665ced21ff19a8da6e4": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1905.10044:11:2": [
        [
          0,
          168
        ]
      ],
      "1905.10044:11:3": [
        [
          0,
          182
        ]
      ]
    }
  }
}
```

## Question: 8e857e44e4233193c7b2d538e520d37be3ae1552

### Question ID and text

Question ID: `8e857e44e4233193c7b2d538e520d37be3ae1552`; paper ID: `1910.02789`.

```text
What experiments authors perform?
```

### Answers

#### Answer: fc219faad4cbdc4a0d17a5c4e30b187b5b08fd05

```text
{"evidence": ["We tested the natural language representation against the visual-based and feature representations on several tasks, with varying difficulty. In these tasks, the agent could navigate, shoot, and collect items such as weapons and medipacks. Often, enemies of different types attacked the agent, and a positive reward was given when an enemy was killed. Occasionally, the agent also suffered from health degeneration. The tasks included a basic scenario, a health gathering scenario, a scenario in which the agent must take cover from fireballs, a scenario in which the agent must defend itself from charging enemies, and a super scenario, where a mixture of the above scenarios was designed to challenge the agent."], "extractive_spans": ["a basic scenario, a health gathering scenario, a scenario in which the agent must take cover from fireballs, a scenario in which the agent must defend itself from charging enemies, and a super scenario, where a mixture of the above scenarios"], "free_form_answer": "", "highlighted_evidence": ["We tested the natural language representation against the visual-based and feature representations on several tasks, with varying difficulty.", "The tasks included a basic scenario, a health gathering scenario, a scenario in which the agent must take cover from fireballs, a scenario in which the agent must defend itself from charging enemies, and a super scenario, where a mixture of the above scenarios was designed to challenge the agent."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1910.02789:5:0`

```text
We tested the natural language representation against the visual-based and feature representations on several tasks, with varying difficulty. In these tasks, the agent could navigate, shoot, and collect items such as weapons and medipacks. Often, enemies of different types attacked the agent, and a positive reward was given when an enemy was killed. Occasionally, the agent also suffered from health degeneration. The tasks included a basic scenario, a health gathering scenario, a scenario in which the agent must take cover from fireballs, a scenario in which the agent must defend itself from charging enemies, and a super scenario, where a mixture of the above scenarios was designed to challenge the agent.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-d0e7e4c53967fc8379d53b4035627d20d69710740e24a668743d9776ccab64ce

Passage ID: `qasper-passage-v1-d0e7e4c53967fc8379d53b4035627d20d69710740e24a668743d9776ccab64ce`; retrieval score: 2.5147077402358673.

Word count: 142.

```text
due to extensive discretization of patches, we've conducted experiments increasing the number of horizontal patches - ranging from 3 to 31 patches in the extreme case. Our results, as depicted in fig: patch count, indicate that the amount of discretization of patches did not affect the performance of the NLP agent, remaining a superior representation compared to the rest.

To conclude, our experiments suggest that NLP representations, though they describe the same raw information of the semantic segmentation maps, are more robust to task-nuisances, allow for better transfer, and achieve higher performance in complex tasks, even when their description is long and convoluted. While we've only presented results for DQN agents, we include plots for a PPO agent in the Appendix, showing similar trends and conclusions. We thus deduce that NLP-based semantic state representations are a preferable choice for training VizDoom agents.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-7e00511121557c0aec0e001a6b97e0a694b0fc2fa3538b81f8ef181e987c6569

Passage ID: `qasper-passage-v1-7e00511121557c0aec0e001a6b97e0a694b0fc2fa3538b81f8ef181e987c6569`; retrieval score: 2.0218889586195816.

Word count: 400.

```text
Work on representation learning is concerned with finding an appropriate representation of data in order to perform a machine learning task BIBREF33. In particular, deep learning exploits this concept by its very nature BIBREF2. Work on representation learning include Predictive State Representations (PSR) BIBREF34, BIBREF35, which capture the state as a vector of predictions of future outcomes, and a Heuristic Embedding of Markov Processes (HEMP) BIBREF36, which learns to embed transition probabilities using an energy-based optimization problem.

There has been extensive work attempting to use natural language in RL. Efforts that integrate language in RL develop tools, approaches, and insights that are valuable for improving the generalization and sample efficiency of learning agents. Previous work on language-conditioned RL has considered the use of natural language in the observation and action space. Environments such as Zork and TextWorld BIBREF37 have been the standard benchmarks for testing text-based games. Nevertheless, these environments do not search for semantic state representations, in which an RL algorithm can be better evaluated and controlled.

BIBREF38 use high-level semantic abstractions of documents in a representation to facilitate relational learning using Inductive Logic Programming and a generative language model. BIBREF39 use high-level guidance expressed in text to enrich a stochastic agent, playing against the built-in AI of Civilization II. They train an agent with the Monte-Carlo search framework in order to jointly learn to identify text that is relevant to a given game state as well as game strategies based only on environment feedback. BIBREF40 utilize natural language in a model-based approach to describe the dynamics and rewards of an environment, showing these can facilitate transfer between different domains.

More recently, the structure and compositionality of natural language has been used for representing policies in hierarchical RL. In a paper by BIBREF41, instructions given in natural language were used in order to break down complex problems into high-level plans and lower-level actions. Their suggested framework leverages the structure inherent to natural language, allowing for transfer to unfamiliar tasks and situations. This use of semantic structure has also been leveraged by BIBREF42, where abstract actions (not necessarily words) were recognized as symbols of a natural and expressive language, improving performance and transfer of RL agents.

Outside the context of RL, previous work has also shown that high-quality linguistic representations can assist in cross-modal transfer, such as using semantic relationships between labels for zero-shot transfer in image classification BIBREF43, BIBREF44.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-4aaae3eef668980fc83830f2cbc382db851368bc6c2abd4c89bdc94c24182774

Passage ID: `qasper-passage-v1-4aaae3eef668980fc83830f2cbc382db851368bc6c2abd4c89bdc94c24182774`; retrieval score: 1.8501192843789849.

Word count: 400.

```text
as well as shoot. This scenario combines elements from all of the previous scenarios.

Our agent was implemented using a Convolutional Neural Network as described in Section SECREF4. We converted the parsed state into embedded representations of fixed length. We tested both a DQN and a PPO based agent, and compared the natural language representation to the other representation techniques, namely the raw image, feature vector, and semantic segmentation representations.

In order to effectively compare the performance of the different representation methods, we conducted our experiments under similar conditions for all agents. The same hyper-parameters were used under all tested representations. Moreover, to rule out effects of architectural expressiveness, the number of weights in all neural networks was approximately matched, regardless of the input type. Finally, we ensured the “super" scenario was positively biased toward image-based representations. This was done by adding a large amount items to the game level, thereby filling the state with nuisances (these tests are denoted by `nuisance' in the scenario name). This was especially evident in the NLP representations, as sentences became extensively longer (average of over 250 words). This is contrary to image-based representations, which did not change in dimension.

Results of the DQN-based agent are presented in fig: scenario comparison. Each plot depicts the average reward (across 5 seeds) of all representations methods. It can be seen that the NLP representation outperforms the other methods. This is contrary to the fact that it contains the same information as the semantic segmentation maps. More interestingly, comparing the vision-based and feature-based representations render inconsistent conclusions with respect to their relative performance. NLP representations remain robust to changes in the environment as well as task-nuisances in the state. As depicted in fig: nuisance scenarios, inflating the state space with task-nuisances impairs the performance of all representations. There, a large amount of unnecessary objects were spawned in the level, increasing the state's description length to over 250 words, whilst retaining the same amount of useful information. Nevertheless, the NLP representation outperformed the vision and feature based representations, with high robustness to the applied noise.

In order to verify the performance of the natural language representation was not due to extensive discretization of patches, we've conducted experiments increasing the number of horizontal patches - ranging from 3 to 31 patches in the extreme case. Our results, as depicted in fig: patch count, indicate that the amount of discretization
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-f825df83a8e407c4c135d67c55fefa8ab867d9984a44bae705baa60fad80d392

Passage ID: `qasper-passage-v1-f825df83a8e407c4c135d67c55fefa8ab867d9984a44bae705baa60fad80d392`; retrieval score: 1.3658809468635145.

Word count: 332.

```text
To convert each frame to a natural language representation state, the list of available labels is iterated, and a string is built accordingly. The main idea of our implementation is to divide the screen into multiple vertical patches, count the amount of different objects inside by their types, and parse it as a sentence. The decision as to whether an object is close or far can be determined by calculating the distance from it to the player, and using two threshold levels. Object descriptions can be concise or detailed, as needed. We experimented with the following mechanics:

the screen can be divided between patches equally, or by determined ratios. Here, our main guideline was to keep the "front" patch narrow enough so it can be used as "sights".

our initial experiment was with 3 patches, and later we added 2 more patches classified as "outer left" and "outer right". In our experiments we have tested up to 51 patches, referred to as left or right patch with corresponding numbers.

we used 2 thresholds, which allowed us to classify the distance of an object from the player as "close","mid", and "far. Depending on the task, the value of the threshold can be changed, as well as adding more thresholds.

different states might generate sentence with different size. A maximum sentence length is another parameter that was tested. sentences-length-table presents some data regarding the average word count in some of the game sceanrios.

After the sentence describing the state is generated, it is transformed to an embedding vector. Words that were not found in the vocabulary were replaced with an “OOV" vector. All words were then concatenated to a NxDx1 matrix, representing the state. We experimented with both Word2Vec and GloVe pretrained embedding vectors. Eventually, we used the latter, as it consumes less memory and speeds up the training process. The length of the state sentence is one of the hyperparameters of the agents; shorter sentences are zero padded, where longer ones are trimmed.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-0f371cb4c6c7076e8c6fd984f46974528ac63256df6c23e02ad48f9c625b6a22

Passage ID: `qasper-passage-v1-0f371cb4c6c7076e8c6fd984f46974528ac63256df6c23e02ad48f9c625b6a22`; retrieval score: 0.0.

Word count: 89.

```text
is a car two meters in front of you a pedestrian on the sidewalk to your right and a car inbound in the negative lane which is far away.”. Language also allows us to efficiently compress information. As an example, the segmentation map in the bottom image of fig: semantic segmentation example can be compactly described by “There are 13 pedestrians crossing the road in front of you”. In the next section we will demonstrate the benefits of using natural-language-based semantic state representation in a first person shooter enviornment.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1363.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "fc219faad4cbdc4a0d17a5c4e30b187b5b08fd05": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1910.02789:5:0": [
        [
          0,
          713
        ]
      ]
    }
  }
}
```

## Question: 2c78993524ca62bf1f525b60f2220a374d0e3535

### Question ID and text

Question ID: `2c78993524ca62bf1f525b60f2220a374d0e3535`; paper ID: `1809.00540`.

```text
What are the sources of the datasets?
```

### Answers

#### Answer: 8dd741d5006030f9048077e2b61e619815a5607d

```text
{"evidence": ["More recently, crosslingual linking of clusters has been discussed by rupnik2016news in the context of linking existing clusters from the Event Registry BIBREF7 in a batch fashion, and by steinberger2016mediagist who also present a batch clustering linking system. However, these are not “truly” online crosslingual clustering systems since they only decide on the linking of already-built monolingual clusters. In particular, rupnik2016news compute distances of document pairs across clusters using nearest neighbors, which might not scale well in an online setting. As detailed before, we adapted the cluster-linking dataset from rupnik2016news to evaluate our online crosslingual clustering approach. Preliminary work makes use of deep learning techniques BIBREF8 , BIBREF9 to cluster documents while learning their representations, but not in an online or multilingual fashion, and with a very small number of cluster labels (4, in the case of the text benchmark)."], "extractive_spans": ["rupnik2016news"], "free_form_answer": "", "highlighted_evidence": ["As detailed before, we adapted the cluster-linking dataset from rupnik2016news to evaluate our online crosslingual clustering approach."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1809.00540:9:1`

```text
More recently, crosslingual linking of clusters has been discussed by rupnik2016news in the context of linking existing clusters from the Event Registry BIBREF7 in a batch fashion, and by steinberger2016mediagist who also present a batch clustering linking system. However, these are not “truly” online crosslingual clustering systems since they only decide on the linking of already-built monolingual clusters. In particular, rupnik2016news compute distances of document pairs across clusters using nearest neighbors, which might not scale well in an online setting. As detailed before, we adapted the cluster-linking dataset from rupnik2016news to evaluate our online crosslingual clustering approach. Preliminary work makes use of deep learning techniques BIBREF8 , BIBREF9 to cluster documents while learning their representations, but not in an online or multilingual fashion, and with a very small number of cluster labels (4, in the case of the text benchmark).
```

#### Answer: d511a0afda9bc3644330b11fa95751a82542f6ef

```text
{"evidence": ["More recently, crosslingual linking of clusters has been discussed by rupnik2016news in the context of linking existing clusters from the Event Registry BIBREF7 in a batch fashion, and by steinberger2016mediagist who also present a batch clustering linking system. However, these are not “truly” online crosslingual clustering systems since they only decide on the linking of already-built monolingual clusters. In particular, rupnik2016news compute distances of document pairs across clusters using nearest neighbors, which might not scale well in an online setting. As detailed before, we adapted the cluster-linking dataset from rupnik2016news to evaluate our online crosslingual clustering approach. Preliminary work makes use of deep learning techniques BIBREF8 , BIBREF9 to cluster documents while learning their representations, but not in an online or multilingual fashion, and with a very small number of cluster labels (4, in the case of the text benchmark).", "Statistics about this dataset are given in Table TABREF30 . As described further, we tune the hyper-parameter INLINEFORM0 on the development set. As for the hyper-parameters related to the timestamp features, we fixed INLINEFORM1 and tuned INLINEFORM2 on the development set, yielding INLINEFORM3 . To compute IDF scores (which are global numbers computed across a corpus), we used a different and much larger dataset that we collected from Deutsche Welle's news website (http://www.dw.com/). The dataset consists of 77,268, 118,045 and 134,243 documents for Spanish, English and German, respectively."], "extractive_spans": ["rupnik2016news", "Deutsche Welle's news website"], "free_form_answer": "", "highlighted_evidence": ["As detailed before, we adapted the cluster-linking dataset from rupnik2016news to evaluate our online crosslingual clustering approach.", "To compute IDF scores (which are global numbers computed across a corpus), we used a different and much larger dataset that we collected from Deutsche Welle's news website (http://www.dw.com/). "], "unanswerable": false, "yes_no": null}
```

Evidence location: `1809.00540:9:1`

```text
More recently, crosslingual linking of clusters has been discussed by rupnik2016news in the context of linking existing clusters from the Event Registry BIBREF7 in a batch fashion, and by steinberger2016mediagist who also present a batch clustering linking system. However, these are not “truly” online crosslingual clustering systems since they only decide on the linking of already-built monolingual clusters. In particular, rupnik2016news compute distances of document pairs across clusters using nearest neighbors, which might not scale well in an online setting. As detailed before, we adapted the cluster-linking dataset from rupnik2016news to evaluate our online crosslingual clustering approach. Preliminary work makes use of deep learning techniques BIBREF8 , BIBREF9 to cluster documents while learning their representations, but not in an online or multilingual fashion, and with a very small number of cluster labels (4, in the case of the text benchmark).
```

Evidence location: `1809.00540:6:1`

```text
Statistics about this dataset are given in Table TABREF30 . As described further, we tune the hyper-parameter INLINEFORM0 on the development set. As for the hyper-parameters related to the timestamp features, we fixed INLINEFORM1 and tuned INLINEFORM2 on the development set, yielding INLINEFORM3 . To compute IDF scores (which are global numbers computed across a corpus), we used a different and much larger dataset that we collected from Deutsche Welle's news website (http://www.dw.com/). The dataset consists of 77,268, 118,045 and 134,243 documents for Spanish, English and German, respectively.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-7357a4f2aa3aca58de8f6878c8a5561b76ba76c2afb901402cce0baf16c96abd

Passage ID: `qasper-passage-v1-7357a4f2aa3aca58de8f6878c8a5561b76ba76c2afb901402cce0baf16c96abd`; retrieval score: 5.3915551539351405.

Word count: 400.

```text
In our first set of experiments, we report results on monolingual clustering for each language separately. Monolingual clustering of a stream of documents is an important problem that has been inspected by others, such as by ahmed2011unified and by aggarwal2006framework. We compare our results to our own implementation of the online micro-clustering routine presented by aggarwal2006framework, which shall be referred to as CluStream. We note that CluStream of aggarwal2006framework has been a widely used state-of-the-art system in media monitoring companies as well as academia, and serves as a strong baseline to this day.

In our preliminary experiments, we also evaluated an online latent semantic analysis method, in which the centroids we keep for the function INLINEFORM0 (see § SECREF3 ) are the average of reduced dimensional vectors of the incoming documents as generated by an incremental singular value decomposition (SVD) of a document-term matrix that is updated after each incoming document. However, we discovered that online LSA performs significantly worse than representing the documents the way is described in § SECREF4 . Furthermore, it was also significantly slower than our algorithm due to the time it took to perform singular value decomposition.

Table TABREF35 gives the final monolingual results on the three datasets. For English, we see that the significant improvement we get using our algorithm over the algorithm of aggarwal2006framework is due to an increased recall score. We also note that the trained models surpass the baseline for all languages, and that the timestamp feature (denoted by TS), while not required to beat the baseline, has a very relevant contribution in all cases. Although the results for both the baseline and our models seem to differ across languages, one can verify a consistent improvement from the latter to the former, suggesting that the score differences should be mostly tied to the different difficulty found across the datasets for each language. The presented scores show that our learning framework generalizes well to different languages and enables high quality clustering results.

To investigate the impact of the timestamp features, we ran an additional experiment using only the same three timestamp features as used in the best model on the English dataset. This experiment yielded scores of INLINEFORM0 , INLINEFORM1 and INLINEFORM2 , which lead us to conclude that while these features are not competitive when used alone (hence temporal information by itself is not sufficient to predict the clusters), they contribute
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-971b3c21e78046ddfbc4a95da4c083e1dfe184de572355c02ece0d376874c86a

Passage ID: `qasper-passage-v1-971b3c21e78046ddfbc4a95da4c083e1dfe184de572355c02ece0d376874c86a`; retrieval score: 5.280296259767303.

Word count: 311.

```text
Following developing news stories is imperative to making real-time decisions on important political and public safety matters. Given the abundance of media providers and languages, this endeavor is an extremely difficult task. As such, there is a strong demand for automatic clustering of news streams, so that they can be organized into stories or themes for further processing. Performing this task in an online and efficient manner is a challenging problem, not only for newswire, but also for scientific articles, online reviews, forum posts, blogs, and microblogs.

A key challenge in handling document streams is that the story clusters must be generated on the fly in an online fashion: this requires handling documents one-by-one as they appear in the document stream. In this paper, we provide a treatment to the problem of online document clustering, i.e. the task of clustering a stream of documents into themes. For example, for news articles, we would want to cluster them into related news stories.

To this end, we introduce a system which aggregates news articles into fine-grained story clusters across different languages in a completely online and scalable fashion from a continuous stream. Our clustering approach is part of a larger media monitoring project to solve the problem of monitoring massive text and TV/Radio streams (speech-to-text). In particular, media monitors write intelligence reports about the most relevant events, and being able to search, visualize and explore news clusters assists in gathering more insight about a particular story. Since relevant events may be spawned from any part of the world (and from many multilingual sources), it becomes imperative to cluster news across different languages.

In terms of granularity, the type of story clusters we are interested in are the group of articles which, for example : (i) Narrate recent air-strikes in Eastern Ghouta (Syria); (ii) Describe the recent launch of Space X's Falcon Heavy rocket.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-70c7d1d155fbabadcf79a4775a06fc34601c48ebdf4348182392c63930566f8e

Passage ID: `qasper-passage-v1-70c7d1d155fbabadcf79a4775a06fc34601c48ebdf4348182392c63930566f8e`; retrieval score: 5.219946504173341.

Word count: 268.

```text
Our system was designed to cluster documents from a (potentially infinite) real-word data stream. The datasets typically used in the literature (TDT, Reuters) have a small number of clusters ( INLINEFORM0 20) with coarse topics (economy, society, etc.), and therefore are not relevant to the use case of media monitoring we treat - as it requires much more fine-grained story clusters about particular events. To evaluate our approach, we adapted a dataset constructed for the different purpose of binary classification of joining cluster pairs. We processed it to become a collection of articles annotated with monolingual and crosslingual cluster labels.

Statistics about this dataset are given in Table TABREF30 . As described further, we tune the hyper-parameter INLINEFORM0 on the development set. As for the hyper-parameters related to the timestamp features, we fixed INLINEFORM1 and tuned INLINEFORM2 on the development set, yielding INLINEFORM3 . To compute IDF scores (which are global numbers computed across a corpus), we used a different and much larger dataset that we collected from Deutsche Welle's news website (http://www.dw.com/). The dataset consists of 77,268, 118,045 and 134,243 documents for Spanish, English and German, respectively.

The conclusions from our experiments are: (a) the weighting of the similarity metric features using SVM significantly outperforms unsupervised baselines such as CluStream (Table TABREF35 ); (b) the SVM approach significantly helps to learn when to create a new cluster, compared to simple grid search for the optimal INLINEFORM0 (Table TABREF39 ); (c) separating the feature space into one for monolingual clusters in the form of keywords and the other for crosslingual clusters based on crosslingual embeddings significantly helps performance.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1809.00540:6:1` | full | 0:601 |

#### Rank 4: qasper-passage-v1-1f60d2af628cdeb1c537403d6102a859a0f157e8cf9b48c4d6fcda7b61525a09

Passage ID: `qasper-passage-v1-1f60d2af628cdeb1c537403d6102a859a0f157e8cf9b48c4d6fcda7b61525a09`; retrieval score: 3.676883920657993.

Word count: 400.

```text
Our similarity metric computes weighted cosine similarity on the different subvectors, both in the case of monolingual clustering and crosslingual clustering. Formally, for the monolingual case, the similarity is given by a function defined as: DISPLAYFORM0

and is computed on the TF-IDF subvectors where INLINEFORM0 is the number of subvectors for the relevant document representation. For the crosslingual case, we discuss below the function INLINEFORM1 , which has a similar structure.

Here, INLINEFORM0 is the INLINEFORM1 th document in the stream and INLINEFORM2 is a monolingual cluster. The function INLINEFORM3 returns the cosine similarity between the document representation of the INLINEFORM4 th document and the centroid for cluster INLINEFORM5 . The vector INLINEFORM6 denotes the weights through which each of the cosine similarity values for each subvectors are weighted, whereas INLINEFORM7 denotes the weights for the timestamp features, as detailed further. Details on learning the weights INLINEFORM8 and INLINEFORM9 are discussed in § SECREF26 .

The function INLINEFORM0 that maps a pair of document and cluster to INLINEFORM1 is defined as follows. Let DISPLAYFORM0

for a given INLINEFORM0 and INLINEFORM1 . For each document INLINEFORM2 and cluster INLINEFORM3 , we generate the following three-dimensional vector INLINEFORM4 :

INLINEFORM0 where INLINEFORM1 is the timestamp for document INLINEFORM2 and INLINEFORM3 is the timestamp for the newest document in cluster INLINEFORM4 .

INLINEFORM0 where INLINEFORM1 is the average timestamp for all documents in cluster INLINEFORM2 .

INLINEFORM0 where INLINEFORM1 is the timestamp for the oldest document in cluster INLINEFORM2 .

These three timestamp features model the time aspect of the online stream of news data and help disambiguate clustering decisions, since time is a valuable indicator that a news story has changed, even if a cluster representation has a reasonable match in the textual features with the incoming document. The same way a news story becomes popular and fades over time BIBREF2 , we model the probability of a document belonging to a cluster (in terms of timestamp difference) with a probability distribution.

For the case of crosslingual clustering, we introduce INLINEFORM0 , which has a similar definition to INLINEFORM1 , only instead of passing document/cluster similarity feature vectors, we pass cluster/cluster similarities, across all language pairs. Furthermore, the features are the crosslingual embedding vectors of the sections title, body and both combined (similarly to the monolingual case) and the timestamp features. For denoting the cluster timestamp, we use the average timestamps of
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-3ab360792e6e36f3667fd7feba203b69249707b253d7afff267c975b76b7ac7e

Passage ID: `qasper-passage-v1-3ab360792e6e36f3667fd7feba203b69249707b253d7afff267c975b76b7ac7e`; retrieval score: 3.666501475203341.

Word count: 240.

```text
In § SECREF19 we introduced INLINEFORM0 and INLINEFORM1 as the weight vectors for the several document representation features. We experiment with both setting these weights to just 1 ( INLINEFORM2 and INLINEFORM3 ) and also learning these weights using support vector machines (SVMs). To generate the SVM training data, we simulate the execution of the algorithm on a training data partition (which we do not get evaluated on) and in which the gold standard labels are given. We run the algorithm using only the first subvector INLINEFORM4 , which is the TF-IDF vector with the words of the document in the body and title. For each incoming document, we create a collection of positive examples, for the document and the clusters which share at least one document in the gold labeling. We then generate 20 negative examples for the document from the 20 best-matching clusters which are not correct. To find out the best-matching clusters, we rank them according to their similarity to the input document using only the first subvector INLINEFORM5 .

Using this scheme we generate a collection of ranking examples (one for each document in the dataset, with the ranking of the best cluster matches), which are then trained using the SVMRank algorithm BIBREF3 . We run 5-fold cross-validation on this data to select the best model, and train both a separate model for each language according to INLINEFORM0 and a crosslingual model according to INLINEFORM1 .
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 1619.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "8dd741d5006030f9048077e2b61e619815a5607d": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1809.00540:9:1": [
        [
          0,
          968
        ]
      ]
    }
  },
  "d511a0afda9bc3644330b11fa95751a82542f6ef": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1809.00540:9:1": [
        [
          0,
          968
        ]
      ]
    }
  }
}
```

## Question: 27c1c678d3862c7676320ca493537b03a9f0c77a

### Question ID and text

Question ID: `27c1c678d3862c7676320ca493537b03a9f0c77a`; paper ID: `1909.02265`.

```text
What multi-domain dataset is used?
```

### Answers

#### Answer: 80b456e9541dcdfb561a6a0f4e806a685bee97dd

```text
{"evidence": ["We use the publicly available dataset KVRET BIBREF5 in our experiments. This dataset is created by the Wizard-of-Oz method BIBREF10 on Amazon Mechanical Turk platform. This dataset includes dialogues in 3 domains: calendar, weather, navigation (POI) which is suitable for our mix-domain dialogue experiments. There are 2,425 dialogues for training, 302 for validation and 302 for testing, as shown in the upper half of Table TABREF12."], "extractive_spans": ["KVRET"], "free_form_answer": "", "highlighted_evidence": ["We use the publicly available dataset KVRET BIBREF5 in our experiments.", "This dataset includes dialogues in 3 domains: calendar, weather, navigation (POI) which is suitable for our mix-domain dialogue experiments. "], "unanswerable": false, "yes_no": null}
```

Evidence location: `1909.02265:5:0`

```text
We use the publicly available dataset KVRET BIBREF5 in our experiments. This dataset is created by the Wizard-of-Oz method BIBREF10 on Amazon Mechanical Turk platform. This dataset includes dialogues in 3 domains: calendar, weather, navigation (POI) which is suitable for our mix-domain dialogue experiments. There are 2,425 dialogues for training, 302 for validation and 302 for testing, as shown in the upper half of Table TABREF12.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-58ae05e005ff96acab594ea7c61f81fd73249d1bd49cf621b340d5de9c716194

Passage ID: `qasper-passage-v1-58ae05e005ff96acab594ea7c61f81fd73249d1bd49cf621b340d5de9c716194`; retrieval score: 3.9777014736069.

Word count: 95.

```text
Figure FIGREF1 shows the architecture of the Sequicity framework as described in BIBREF8. In essence, in each turn, the Sequicity model first takes a bspan ($B_1$) and a response ($R_1$) which are determined in the previous step, and the current human question ($U_2$) to generate the current bspan. This bspan is then used together with a knowledge base to generate the corresponding machine answer ($R_2$), as shown in the right part of Figure FIGREF1.

The left part of that figure shows an example dialogue in a mixed-domain setting (which will be explained in Section SECREF3).
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-6b88056f47de6a51239a7643911c597024583517a3883804854e0cbcdd93a5cf

Passage ID: `qasper-passage-v1-6b88056f47de6a51239a7643911c597024583517a3883804854e0cbcdd93a5cf`; retrieval score: 2.9265851304171977.

Word count: 280.

```text
We use the publicly available dataset KVRET BIBREF5 in our experiments. This dataset is created by the Wizard-of-Oz method BIBREF10 on Amazon Mechanical Turk platform. This dataset includes dialogues in 3 domains: calendar, weather, navigation (POI) which is suitable for our mix-domain dialogue experiments. There are 2,425 dialogues for training, 302 for validation and 302 for testing, as shown in the upper half of Table TABREF12.

In this original dataset, each dialogue is of a single domain where all of its turns are on that domain. Each turn is composed of a sentence pair, one sentence is a user utterance, the other sentence is the corresponding machine response. A dialogue is a sequence of turns. To create mix-domain dialogues for our experiments, we make some changes in this dataset as follows:

We keep the dialogues in the calendar domain as they are.

We take a half of dialogues in the weather domain and a half of dialogues in the POI domain and mix their turns together, resulting in a dataset of mixed weather-POI dialogues. In this mixed-domain dialogue, there is a turn in the weather domain, followed by a turn in POI domain or vice versa.

We call this dataset the sequential turn dataset. Since the start turn of a dialogue has a special role in triggering the learning systems, we decide to create another and different mixed-domain dataset with the following mixing method:

The first turn and the last turn of each dialogue are kept as in their original.

The internal turns are mixed randomly.

We call this dataset the random turn dataset. Some statistics of these mixed-domain datasets are shown in the lower half of the Table TABREF12.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1909.02265:5:0` | full | 0:434 |

#### Rank 3: qasper-passage-v1-02caee53e7488505ff9361f25345f97224382de7476e090fce1802370d3aa6ef

Passage ID: `qasper-passage-v1-02caee53e7488505ff9361f25345f97224382de7476e090fce1802370d3aa6ef`; retrieval score: 2.6460237274938314.

Word count: 272.

```text
answer. That is, the domains are mixed between turns. For example, in the first turn, the user requests some information of a restaurant; then in the second turn, he switches to the a different domain, for example, he asks about the weather at a specific location. In a next turn, he would either switch to a new domain or come back to ask about some other property of the suggested restaurant. This is a realistic scenario which usually happens in practical chatbot applications in our observations. We prefer calling this problem mixed-domain dialogue rather than multiple-domain dialogue.

Second, we study the effect of the mixed-domain setting in the context of multi-domain dialogue approaches to see how they perform in different experimental scenarios.

The main findings of this work include:

A specialized state tracking component in multiple domains still plays an important role and gives better results than a state-of-the-art end-to-end task-oriented dialogue system.

A combination of specialized state tracking system and an end-to-end task-oriented dialogue system is beneficial in mix-domain dialogue systems. Our hybrid system is able to improve the belief tracking accuracy of about 28% of average absolute point on a standard multi-domain dialogue dataset.

These experimental results give some useful insights on data preparation and acquisition in the development of the chatbot platform FPT.AI, which is currently deployed for many practical chatbot applications.

The remainder of this paper is structured as follows. First, Section SECREF2 discusses briefly the two methods in building dialogue systems that our method relies on. Next, Section SECREF3 presents experimental settings and results. Finally, Section SECREF4 concludes the paper and gives some directions for future work.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-474579230a80c1acc777353b317417c89acc2d83606cb40876ff7ba391a3e3d9

Passage ID: `qasper-passage-v1-474579230a80c1acc777353b317417c89acc2d83606cb40876ff7ba391a3e3d9`; retrieval score: 2.6057607192670575.

Word count: 118.

```text
For the task-oriented Sequicity model, we keep the best parameter settings as reported in the original framework, on the same KVRET dataset BIBREF8. In particular, the hidden size of GRU unit is set to 50; the learning rate of Adam optimizer is 0.003. In addition to the original GRU unit, we also re-run this framework with simple RNN unit to compare the performance of different recurrent network types. The Sequicity tool is freely available for download.

For the multi-domain belief tracker model, we set the hidden size of LSTM units to 50 as in the original model; word embedding size is 300 and number of training epochs is 100. The corresponding tool is also freely available for download.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-0689f160ae1d8a75d42594b2c754a92641c61745d5d4a01979fbcb2bebdb49a8

Passage ID: `qasper-passage-v1-0689f160ae1d8a75d42594b2c754a92641c61745d5d4a01979fbcb2bebdb49a8`; retrieval score: 2.5589684982514003.

Word count: 246.

```text
In this subsection, we present an example of erroneous mixed dialogue with multple turns. Table TABREF23 shows a dialogue in the test set where wrong generated responses of the Sequicity system are marked in bold font.

In the first turn, the system predicts incorrectly the bspan, thus generates wrong slot values (heavy traffic and Pizza Hut). The word Pizza Hut is an arbitrary value selected by the system when it cannot capture the correct value home in the bspan. In the second turn, the machine is not able to capture the value this_week. This failure does not manifest immediately at this turn but it is accumulated to make a wrong answer at the third turn (monday instead of this_week).

The third turn is of domain weather and the fourth turn is switched to domain POI. The bspan value cleveland is retained through cross domain, resulting in an error in the fourth turn, where cleveland is shown instead of home. This example demonstrates a weakness of the system when being trained on a mixed-domain dataset. In the fifth turn, since the system does not recognize the value fastest in the bspan, it generates a random and wrong value moderate traffic. Note that the generated answer of the sixth turn is correct despite of the wrong predicted bspan; however, it is likely that if the dialogue continues, this wrong bspan may result in more answer mistakes. In such situations, multi-domain belief tracker usually performs better at bspan prediction.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1011.

Fully covered answer annotations: 80b456e9541dcdfb561a6a0f4e806a685bee97dd.

Missing evidence by answer annotation:

```text
{
  "80b456e9541dcdfb561a6a0f4e806a685bee97dd": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: a1e07c7563ad038ee2a7de5093ea08efdd6077d4

### Question ID and text

Question ID: `a1e07c7563ad038ee2a7de5093ea08efdd6077d4`; paper ID: `1909.04625`.

```text
What is the size of the datasets employed?
```

### Answers

#### Answer: 0779f8ebeeb399bdf0300bd70e072d054d56bb77

```text
{"evidence": ["are trained to output the probability distribution of the upcoming word given a context, without explicitly representing the structure of the context BIBREF9, BIBREF10. We trained two two-layer recurrent neural language models with long short-term memory architecture BIBREF11 on a relatively small corpus. The first model, referred as `LSTM (PTB)' in the following sections, was trained on the sentences from Penn Treebank BIBREF12. The second model, referred as `LSTM (FTB)', was trained on the sentences from French Treebank BIBREF13. We set the size of input word embedding and LSTM hidden layer of both models as 256.", "We also compare LSTM language models trained on large corpora. We incorporate two pretrained English language models: one trained on the Billion Word benchmark (referred as `LSTM (1B)') from BIBREF14, and the other trained on English Wikipedia (referred as `LSTM (enWiki)') from BIBREF3. For French, we trained a large LSTM language model (referred as `LSTM (frWaC)') on a random subset (about 4 million sentences, 138 million word tokens) of the frWaC dataset BIBREF15. We set the size of the input embeddings and hidden layers to 400 for the LSTM (frWaC) model since it is trained on a large dataset."], "extractive_spans": ["(about 4 million sentences, 138 million word tokens)", "one trained on the Billion Word benchmark"], "free_form_answer": "", "highlighted_evidence": ["The first model, referred as `LSTM (PTB)' in the following sections, was trained on the sentences from Penn Treebank BIBREF12. The second model, referred as `LSTM (FTB)', was trained on the sentences from French Treebank BIBREF13.", "We incorporate two pretrained English language models: one trained on the Billion Word benchmark (referred as `LSTM (1B)') from BIBREF14, and the other trained on English Wikipedia (referred as `LSTM (enWiki)') from BIBREF3. For French, we trained a large LSTM language model (referred as `LSTM (frWaC)') on a random subset (about 4 million sentences, 138 million word tokens) of the frWaC dataset BIBREF15."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1909.04625:2:0`

```text
are trained to output the probability distribution of the upcoming word given a context, without explicitly representing the structure of the context BIBREF9, BIBREF10. We trained two two-layer recurrent neural language models with long short-term memory architecture BIBREF11 on a relatively small corpus. The first model, referred as `LSTM (PTB)' in the following sections, was trained on the sentences from Penn Treebank BIBREF12. The second model, referred as `LSTM (FTB)', was trained on the sentences from French Treebank BIBREF13. We set the size of input word embedding and LSTM hidden layer of both models as 256.
```

Evidence location: `1909.04625:2:1`

```text
We also compare LSTM language models trained on large corpora. We incorporate two pretrained English language models: one trained on the Billion Word benchmark (referred as `LSTM (1B)') from BIBREF14, and the other trained on English Wikipedia (referred as `LSTM (enWiki)') from BIBREF3. For French, we trained a large LSTM language model (referred as `LSTM (frWaC)') on a random subset (about 4 million sentences, 138 million word tokens) of the frWaC dataset BIBREF15. We set the size of the input embeddings and hidden layers to 400 for the LSTM (frWaC) model since it is trained on a large dataset.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-ee7a8bbca3c6178d551d7584b28dc01785f94654ca51d55ba57e36a8c4d591f8

Passage ID: `qasper-passage-v1-ee7a8bbca3c6178d551d7584b28dc01785f94654ca51d55ba57e36a8c4d591f8`; retrieval score: 7.750520632450346.

Word count: 195.

```text
are trained to output the probability distribution of the upcoming word given a context, without explicitly representing the structure of the context BIBREF9, BIBREF10. We trained two two-layer recurrent neural language models with long short-term memory architecture BIBREF11 on a relatively small corpus. The first model, referred as `LSTM (PTB)' in the following sections, was trained on the sentences from Penn Treebank BIBREF12. The second model, referred as `LSTM (FTB)', was trained on the sentences from French Treebank BIBREF13. We set the size of input word embedding and LSTM hidden layer of both models as 256.

We also compare LSTM language models trained on large corpora. We incorporate two pretrained English language models: one trained on the Billion Word benchmark (referred as `LSTM (1B)') from BIBREF14, and the other trained on English Wikipedia (referred as `LSTM (enWiki)') from BIBREF3. For French, we trained a large LSTM language model (referred as `LSTM (frWaC)') on a random subset (about 4 million sentences, 138 million word tokens) of the frWaC dataset BIBREF15. We set the size of the input embeddings and hidden layers to 400 for the LSTM (frWaC) model since it is trained on a large dataset.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1909.04625:2:0` | full | 0:622 |
| `1909.04625:2:1` | full | 0:602 |

#### Rank 2: qasper-passage-v1-ac35f55ed05e5f3c2e31e6bb44cb0667d124093e56e5a7967a120e48d317c654

Passage ID: `qasper-passage-v1-ac35f55ed05e5f3c2e31e6bb44cb0667d124093e56e5a7967a120e48d317c654`; retrieval score: 7.710358705388177.

Word count: 303.

```text
This section further investigates the effects of CoordNP annotation schemes on the behaviors of structurally-supervised models. We test whether an explicit COORD phrasal tag improves model performance. We trained two additional RNNG models on 38,546 sentences from the Penn Treebank annotated with two different schemes: The first, RNNG (PTB-control) was trained with the original Penn Treebank annotation. The second, RNNG (PTB-coord), was trained on the same sentences, but with an extended coordination annotation scheme, meant to employ the scheme employed in the FTB, adapted from BIBREF26. We stripped empty categories from their scheme and only kept the NP-COORD label for constituents inside a coordination structure. Figure FIGREF26 illustrates the detailed annotation differences between two datasets. We tested both models on all the experiments presented in Sections SECREF3-SECREF6 above.

Turning to the results of these six experiments: We see little difference between the two models in the Non-coordination agreement experiment. For the Complex coordination control and Complex coordination critical experiments, both models are largely the same as well. However, in the Simple and-coordination and Simple or-coordination experiments the values for all conditions are shifted upwards for the RNNG PTB-coord model, indicating higher over-all preference for the plural continuation. Furthermore, the range of values is reduced in the RNNG PTB-coord model, compared to the RNNG PTB-control model. These results indicate that adding an explicit COORD phrasal label does not drastically change model performance: Both models still appear to be using a linear combination of number features to drive plural vs. singular expectation. However, the explicit representation has made the interior of the coordination phrase more opaque to the model (each feature matters less) and has slightly shifted model preference towards plural continuations. In this sense, the PTB-coord model may have learned a generalization about CoordNPs, but this generalization remains unlike the ones learned by humans.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-12c0f4f4ba4901eab3ce94d6a39bc217576dc7b4628519e697a861e1bcc335a0

Passage ID: `qasper-passage-v1-12c0f4f4ba4901eab3ce94d6a39bc217576dc7b4628519e697a861e1bcc335a0`; retrieval score: 7.263995565468791.

Word count: 358.

```text
The experiments presented here extend and refine a line of research investigating what linguistic knowledge is acquired by neural language models. Previous studies have demonstrated that sequential models trained on a simple regime of optimizing the next word can learn long-distance syntactic dependencies in impressive detail. Our results provide complimentary insights, demonstrating that a range of model architectures trained on a variety of datasets can learn fine-grained information about the interaction of CoordNPs and local syntactic context, but their behavior remains unhumanlike in many key ways. Furthermore, to our best knowledge, this work presents the first psycholinguistic analysis of neural language models trained on French, a high-resource language that has so far been under-investigated in this line of research.

In the simple coordination experiment, we demonstrated that models were able to capture some of the agreement behaviors of humans, although their performance deviated in crucial aspects. Whereas human behavior is best modeled as a `percolation' process, the neural models appear to be using a linear combination of NP constituent number to drive CoordNP/verb number agreement, with the second noun weighted more heavily than the first. In these experiments, supervision afforded by the RNNG and ActionLSTM models did not translate into more robust or humanlike learning outcomes. The complex coordination experiments provided evidence that the neural models tested were not using a simple `bag of features' strategy, but were sensitive to syntactic context. All models tested were able to interpret material that had similar surface form in ways that corresponded to two different tree-structural descriptions, based on local context. The inverted coordination experiment provided a contrasting example, in which models were unable to modulate expectations based on subtleties in the syntactic environment.

Across all our experiments, the French models performed consistently better on subject/verb number agreement than on subject/predicate gender agreement. Although there are likely more examples of subject/verb number agreement in the French training data, gender agreement is syntactically mandated and widespread in French. It remains an open question why all but one of the models tested were unable to leverage the numerous examples of gender agreement seen in various contexts during training to drive correct subject/predicate expectations.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-c56b5959bcbcfae924256aa970b9e1db5c6599e87eb4911edbe18e4ef545101d

Passage ID: `qasper-passage-v1-c56b5959bcbcfae924256aa970b9e1db5c6599e87eb4911edbe18e4ef545101d`; retrieval score: 5.395448903992004.

Word count: 350.

```text
In addition to using phrase-level features to drive expectation about downstream lexical items, human processors can do the inverse—use lexical features to drive expectations about upcoming syntactic chunks. In this experiment, we assess whether neural models use number features hosted on a verb to modulate their expectations for upcoming CoordNPs.

To assess whether neural language models learn inverted coordination rules, we adapted items from Section SECREF13 in both English (37 items) and French (24 items), following the paradigm in Table TABREF24. The first part of the phrase contains either a plural or singular verb and a plural or singular noun. In this case, we sample the surprisal for the continuations and (or is grammatical in all conditions, so it is omitted from this study). Our expectation is that `and' is less surprising in the Vpl_Nsg condition than in the Vsg_Nsg condition, where a CoordNP is not licensed by the grammar in either French or English (as in *What is the pig and the cat eating?). We also expect lower surprisal for and in the Vpl_Nsg condition, where it is obligatory for a grammatical continuation, than in the Vpl_Npl condition, where it is optional.

For French experimental items, the question is embedded into a sentential-complement taking verb, following Example SECREF6, due to the fact that unembedded subject-verb inverted questions sound very formal and might be relatively rare in the training data.

. Je me demande où vont le maire et

I myself ask where go.3PL the.MSG mayor.MSG and

The results for both languages are shown in Figure FIGREF25, with the surprisal at the coordinator on the y-axis and the various conditions on the x-axis. No model in either language shows a signficant difference in surprisal between the Vpl_Nsg and Vpl_Npl conditions or between the Vpl_Nsg and Vsg_Nsg conditions. The LSTM (1B) shows significant difference between the Vpl_Nsg and Vpl_Npl conditions, but in the opposite direction than expected, with the coordinator less surprising in the latter condition. These results indicate that the models are unable to use the fine-grained context sensitivity to drive expectations for CoordNPs, at least in the inversion setting.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-a00127b62e861e61d0e1f4ccd7ebab367e48f4b5778ff1604539f077b20e453c

Passage ID: `qasper-passage-v1-a00127b62e861e61d0e1f4ccd7ebab367e48f4b5778ff1604539f077b20e453c`; retrieval score: 4.299865419009034.

Word count: 264.

```text
To determine whether state-of-the-art neural architectures are capable of learning humanlike CoordNP/verb agreement properties, we adopt the psycholinguistics paradigm for model assessment. In this paradigm the models are tested using hand-crafted sentences designed to test underlying network knowledge. The assumption here is that if a model implicitly learns humanlike linguistic knowledge during training, its expectations for upcoming words should qualitatively match human expectations in novel contexts. For example, BIBREF1 and BIBREF6 assessed how well neural models had learned the subject/verb number agreement by feeding them with the prefix The keys to the cabinet .... If the models predicted the grammatical continuation are over the ungrammatical continuation is, they can be said to have learned the number agreement insofar as the number of the head noun and not the number of the distractor noun, cabinet, drives expectations about the number of the matrix verb.

If models are able to robustly modulate their expectations based on the internal components of the CoordNP, this will provide evidence that the networks are building up a context-sensitive phrase-level representation. We quantify model expectations as surprisal values. Surprisal is the negative log-conditional probability $S(x_i) = -\log _2 p(x_i|x_1 \dots x_{i-1})$ of a sentence's $i^{th}$ word $x_i$ given the previous words. Surprisal tells us how strongly $x_i$ is expected in context and is known to correlate with human processing difficulty BIBREF7, BIBREF0, BIBREF8. In the CoordNP/Verb agreement studies presented here, cases where the proceeding context sets high expectation for a number-inflected verb form $w_i$, (e.g. singular `is') we would expect $S(w_i)$ to be lower than its number-mismatched counterpart (e.g. plural `are').
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1470.

Fully covered answer annotations: 0779f8ebeeb399bdf0300bd70e072d054d56bb77.

Missing evidence by answer annotation:

```text
{
  "0779f8ebeeb399bdf0300bd70e072d054d56bb77": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: 29c014baf99fb9f40b5171aab3e2c7f12a748f79

### Question ID and text

Question ID: `29c014baf99fb9f40b5171aab3e2c7f12a748f79`; paper ID: `1908.04042`.

```text
what algorithms did they use?
```

### Answers

#### Answer: 3f761bb5857701886da42838934df5de71626245

```text
{"evidence": ["Approach and findings. We exploit editor tags and user-generated search terms as input for tag recommendation approaches. Our evaluation comprises of a rich set of 19 different algorithms to recommend tags for e-books, which we group into (i) popularity-based, (ii) similarity-based (i.e., using content information), and (iii) hybrid approaches. We evaluate our approaches in terms of accuracy, semantic similarity and diversity on the review content of Amazon users, which reflects the readers' vocabulary. With semantic similarity, we measure how semantically similar (based on learned Doc2Vec BIBREF7 embeddings) the list of recommended tags is to the list of relevant tags. We use this additional metric to measure not only exact “hits” of our recommendations but also semantic matches."], "extractive_spans": ["popularity-based", "similarity-based", "hybrid"], "free_form_answer": "", "highlighted_evidence": ["Our evaluation comprises of a rich set of 19 different algorithms to recommend tags for e-books, which we group into (i) popularity-based, (ii) similarity-based (i.e., using content information), and (iii) hybrid approaches."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1908.04042:0:5`

```text
Approach and findings. We exploit editor tags and user-generated search terms as input for tag recommendation approaches. Our evaluation comprises of a rich set of 19 different algorithms to recommend tags for e-books, which we group into (i) popularity-based, (ii) similarity-based (i.e., using content information), and (iii) hybrid approaches. We evaluate our approaches in terms of accuracy, semantic similarity and diversity on the review content of Amazon users, which reflects the readers' vocabulary. With semantic similarity, we measure how semantically similar (based on learned Doc2Vec BIBREF7 embeddings) the list of recommended tags is to the list of relevant tags. We use this additional metric to measure not only exact “hits” of our recommendations but also semantic matches.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-b505631b217ad59a4406fc1efb9581ee5687ca394e36373ad6cef770bba56a46

Passage ID: `qasper-passage-v1-b505631b217ad59a4406fc1efb9581ee5687ca394e36373ad6cef770bba56a46`; retrieval score: 2.216815842086861.

Word count: 389.

```text
In this paper, we present our work to support editors in the e-book annotation process. Specifically, we aim to provide tag recommendations that incorporate both the vocabulary of the editors and e-book readers. Therefore, we train various configurations of tag recommender approaches on editors' tags and Amazon search terms and evaluate them on a dataset containing Amazon review keywords. We find that combining both data sources enhances the quality of tag recommendations for annotating e-books. Furthermore, while approaches that train only on Amazon search terms provide poor performance concerning recommendation accuracy, we show that they still offer helpful annotations concerning recommendation diversity as well as our novel semantic similarity metric.

Future work. For future work, we plan to validate our findings using another dataset, e.g., by recommending tags for scientific articles and books in BibSonomy. With this, we aim to demonstrate the usefulness of the proposed approach in a similar domain and to enhance the reproducibility of our results by using an open dataset.

Moreover, we plan to evaluate our tag recommendation approaches in a study with domain users. Also, we want to improve our similarity-based approaches by integrating novel embedding approaches BIBREF16 , BIBREF17 as we did, for example, with our proposed semantic similarity evaluation metric. Finally, we aim to incorporate explanations for recommended tags so that editors of e-book annotations receive additional support in annotating e-books BIBREF21 . By making the underlying (semantic) reasoning visible to the editor who is in charge of tailoring annotations, we aim to support two goals: (i) allowing readers to discover e-books more efficiently, and (ii) enabling publishers to leverage semi-automatic categorization processes for e-books. In turn, providing explanations fosters control over which vocabulary to choose when tagging e-books for different application contexts.

Acknowledgments. The authors would like to thank Peter Langs, Jan-Philipp Wolf and Alyona Schraa from HGV GmbH for providing the e-book annotation data. This work was funded by the Know-Center GmbH (FFG COMET Program), the FFG Data Market Austria project and the AI4EU project (EU grant 825619). The Know-Center GmbH is funded within the Austrian COMET Program - Competence Centers for Excellent Technologies - under the auspices of the Austrian Ministry of Transport, Innovation and Technology, the Austrian Ministry of Economics and Labor and by the State of Styria. COMET is managed by the Austrian Research Promotion Agency (FFG).
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-ee508ee95fe943bbd79a1c65c034a71b255ef6db1c4bead69e56f48caefe7cdd

Passage ID: `qasper-passage-v1-ee508ee95fe943bbd79a1c65c034a71b255ef6db1c4bead69e56f48caefe7cdd`; retrieval score: 1.9919575171150536.

Word count: 400.

```text
We implement three types of tag recommendation approaches, i.e., (i) popularity-based, (ii) similarity-based (i.e., using content information), and (iii) hybrid approaches. Due to the lack of personalized tags (i.e., we do not know which user has assigned a tag), we do not implement other types of algorithms such as collaborative filtering BIBREF8 . In total, we evaluate 19 different algorithms to recommend tags for annotating e-books.

Popularity-based approaches. We recommend the most frequently used tags in the dataset, which is a common strategy for tag recommendations BIBREF9 . That is, a most popular INLINEFORM0 approach for editor tags and a most popular INLINEFORM1 approach for Amazon search terms. For e-books, for which we also have author (= INLINEFORM2 and INLINEFORM3 ) or BISAC (= INLINEFORM4 and INLINEFORM5 ) information, we use these features to further filter the recommended tags, i.e., to only recommend tags that were used to annotate e-books of a specific author or a specific BISAC.

We combine both data sources (i.e., editor tags and Amazon search terms) using a round-robin combination strategy, which ensures an equal weight for both sources. This gives us three additional popularity-based algorithms (= INLINEFORM0 , INLINEFORM1 and INLINEFORM2 ).

Similarity-based approaches. We exploit the textual content of e-books (i.e., description or title) to recommend relevant tags BIBREF10 . For this, we first employ a content-based filtering approach BIBREF11 based on TF-IDF BIBREF12 to find top- INLINEFORM0 similar e-books. For each of the similar e-books, we then either extract the assigned editor tags (= INLINEFORM2 and INLINEFORM3 ) or the Amazon search terms (= INLINEFORM4 and INLINEFORM5 ). To combine the tags of the top- INLINEFORM6 similar e-books, we use the cross-source algorithm BIBREF13 , which favors tags that were used to annotate more than one similar e-book (i.e., tags that come from multiple recommendation sources). The final tag relevancy is calculated as: DISPLAYFORM0

where INLINEFORM0 denotes the number of distinct e-books, which yielded the recommendation of tag INLINEFORM1 , to favor tags that come from multiple sources and INLINEFORM2 is the similarity score of the corresponding e-book. We again use a round-robin strategy to combine both data sources (= INLINEFORM3 and INLINEFORM4 ).

Hybrid approaches. We use the previously mentioned cross-source algorithm BIBREF13 to construct four hybrid recommendation approaches. In this case, tags are favored that are recommended by more than one algorithm.

Hence, to create a popularity-based hybrid (= INLINEFORM0 ),
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-021509bb7a06e0a42204499f136baaba1344b6df2263c4dfb566e569ac9a64a0

Passage ID: `qasper-passage-v1-021509bb7a06e0a42204499f136baaba1344b6df2263c4dfb566e569ac9a64a0`; retrieval score: 1.656284576286279.

Word count: 400.

```text
When people shop for books online in e-book stores such as, e.g., the Amazon Kindle store, they enter search terms with the goal to find e-books that meet their preferences. Such e-books have a variety of metadata such as, e.g., title, author or keywords, which can be used to retrieve e-books that are relevant to the query. As a consequence, from the perspective of e-book publishers and editors, annotating e-books with tags that best describe the content and which meet the vocabulary of users (e.g., when searching and reviewing e-books) is an essential task BIBREF0 .

Problem and aim of this work. Annotating e-books with suitable tags is, however, a complex task as users' vocabulary may differ from the one of editors. Such a vocabulary mismatch yet hinders effective organization and retrieval BIBREF1 of e-books. For example, while editors mostly annotate e-books with descriptive tags that reflect the book's content, Amazon users often search for parts of the book title. In the data we use for the present study (see Section SECREF2 ), we find that around 30% of the Amazon search terms contain parts of e-book titles.

In this paper, we present our work to support editors in the e-book annotation process with tag recommendations BIBREF2 , BIBREF3 . Our idea is to exploit user-generated search query terms in Amazon to mimic the vocabulary of users in Amazon, who search for e-books. We combine these search terms with tags assigned by editors in a hybrid tag recommendation approach. Thus, our aim is to show that we can improve the performance of tag recommender systems for e-books both concerning recommendation accuracy as well as semantic similarity and tag recommendation diversity.

Related work. In tag recommender systems, mostly content-based algorithms (e.g., BIBREF4 , BIBREF5 ) are used to recommend tags to annotate resources such as e-books. In our work, we incorporate both content features of e-books (i.e., title and description text) as well as Amazon search terms to account for the vocabulary of e-book readers.

Concerning the evaluation of tag recommendation systems, most studies focus on measuring the accuracy of tag recommendations (e.g., BIBREF2 ). However, the authors of BIBREF6 suggest also to use beyond-accuracy metrics such as diversity to evaluate the quality of tag recommendations. In our work, we measure recommendation diversity in addition to recommendation accuracy and propose a novel metric termed semantic similarity to validate semantic matches of
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-8087fb76156a747c26afe036220c2f4354241a396007f53056793aeba4f94a31

Passage ID: `qasper-passage-v1-8087fb76156a747c26afe036220c2f4354241a396007f53056793aeba4f94a31`; retrieval score: 1.609562894346328.

Word count: 205.

```text
also to use beyond-accuracy metrics such as diversity to evaluate the quality of tag recommendations. In our work, we measure recommendation diversity in addition to recommendation accuracy and propose a novel metric termed semantic similarity to validate semantic matches of tag recommendations.

Approach and findings. We exploit editor tags and user-generated search terms as input for tag recommendation approaches. Our evaluation comprises of a rich set of 19 different algorithms to recommend tags for e-books, which we group into (i) popularity-based, (ii) similarity-based (i.e., using content information), and (iii) hybrid approaches. We evaluate our approaches in terms of accuracy, semantic similarity and diversity on the review content of Amazon users, which reflects the readers' vocabulary. With semantic similarity, we measure how semantically similar (based on learned Doc2Vec BIBREF7 embeddings) the list of recommended tags is to the list of relevant tags. We use this additional metric to measure not only exact “hits” of our recommendations but also semantic matches.

Our evaluation results show that combining both data sources enhances the quality of tag recommendations for annotating e-books. Furthermore, approaches that solely train on Amazon search terms provide poor performance in terms of accuracy but deliver good results in terms of semantic similarity and recommendation diversity.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.04042:0:5` | full | 0:791 |

#### Rank 5: qasper-passage-v1-9668f8f50c8c90fc6a932ddd093255d64e0b91075513c565cacf5639bb50b6f0

Passage ID: `qasper-passage-v1-9668f8f50c8c90fc6a932ddd093255d64e0b91075513c565cacf5639bb50b6f0`; retrieval score: 1.0176612350211613.

Word count: 400.

```text
Figure FIGREF11 shows the results of the accuracy experiment for the (i) popularity-based, (ii) similarity-based, and (iii) hybrid tag recommendation approaches.

Popularity-based approaches. In Figure FIGREF11 , we see that popularity-based approaches based on editor tags tend to perform better than if trained on Amazon search terms. If we take into account contextual information like BISAC or author, we can further improve accuracy in terms of INLINEFORM0 . That is, we find that using popular tags from e-books of a specific author leads to the best accuracy of the popularity-based approaches. This suggests that editors and readers do seem to reuse tags for e-books of same authors. If we use both editor tags and Amazon search terms, we can further increase accuracy, especially for higher values of INLINEFORM1 like in the case of INLINEFORM2 . This is, however, not the case for INLINEFORM3 as the accuracy of the integrated INLINEFORM4 approach is low. The reason for this is the limited amount of e-books from within the Amazon search query logs that have BISAC information (i.e., only INLINEFORM5 ).

Similarity-based approaches. We further improve accuracy if we first find similar e-books and then extract their top- INLINEFORM0 tags in a cross-source manner as described in Section SECREF4 .

As shown in Figure FIGREF11 , using the description text to find similar e-books results in more accurate tag recommendations than using the title (i.e., INLINEFORM0 for INLINEFORM1 ). This is somehow expected as the description text consists of a bigger corpus of words (i.e., multiple sentences) than the title. Concerning the collected Amazon search query logs, extracting and then recommending tags from this source results in a much lower accuracy performance. Thus, these results also suggest to investigate beyond-accuracy metrics as done in Section SECREF17 .

Hybrid approaches. Figure FIGREF11 shows the accuracy results of the four hybrid approaches. By combining the best three popularity-based approaches, we outperform all of the initially evaluated popularity algorithms (i.e., INLINEFORM0 for INLINEFORM1 ). On the contrary, the combination of the two best performing similarity-based approaches INLINEFORM2 and INLINEFORM3 does not yield better accuracy. The negative impact of using a lower-performing approach such as INLINEFORM4 within a hybrid combination can also be observed in INLINEFORM5 for lower values of INLINEFORM6 . Overall, this confirms our initial intuition that combining the best performing popularity-based approach with the best similarity-based approach should result in the highest accuracy (i.e.,
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1794.

Fully covered answer annotations: 3f761bb5857701886da42838934df5de71626245.

Missing evidence by answer annotation:

```text
{
  "3f761bb5857701886da42838934df5de71626245": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: 983c2fe7bdbf471bb8b15db858fd2cbec86b96a5

### Question ID and text

Question ID: `983c2fe7bdbf471bb8b15db858fd2cbec86b96a5`; paper ID: `1911.05343`.

```text
Do they compare against state of the art text generation?
```

### Answers

#### Answer: f5f47a4742b4d1e26a66f1811bd153d545fe13ba

```text
{"evidence": ["We compare our HR-VAE model with three strong baselines using VAE for text modelling:", "VAE-LSTM-base: A variational autoencoder model which uses LSTM for both encoder and decoder. KL annealing is used to tackled the latent variable collapse issue BIBREF0;", "VAE-CNN: A variational autoencoder model with a LSTM encoder and a dilated CNN decoder BIBREF7;", "vMF-VAE: A variational autoencoder model using LSTM for both encoder and decoder where the prior distribution is the von Mises-Fisher (vMF) distribution rather than a Gaussian distribution BIBREF5."], "extractive_spans": [], "free_form_answer": "", "highlighted_evidence": ["We compare our HR-VAE model with three strong baselines using VAE for text modelling:\n\nVAE-LSTM-base: A variational autoencoder model which uses LSTM for both encoder and decoder. KL annealing is used to tackled the latent variable collapse issue BIBREF0;\n\nVAE-CNN: A variational autoencoder model with a LSTM encoder and a dilated CNN decoder BIBREF7;\n\nvMF-VAE: A variational autoencoder model using LSTM for both encoder and decoder where the prior distribution is the von Mises-Fisher (vMF) distribution rather than a Gaussian distribution BIBREF5."], "unanswerable": false, "yes_no": true}
```

Evidence location: `1911.05343:5:0`

```text
We compare our HR-VAE model with three strong baselines using VAE for text modelling:
```

Evidence location: `1911.05343:5:1`

```text
VAE-LSTM-base: A variational autoencoder model which uses LSTM for both encoder and decoder. KL annealing is used to tackled the latent variable collapse issue BIBREF0;
```

Evidence location: `1911.05343:5:2`

```text
VAE-CNN: A variational autoencoder model with a LSTM encoder and a dilated CNN decoder BIBREF7;
```

Evidence location: `1911.05343:5:3`

```text
vMF-VAE: A variational autoencoder model using LSTM for both encoder and decoder where the prior distribution is the von Mises-Fisher (vMF) distribution rather than a Gaussian distribution BIBREF5.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-aa93b4f372abba20035dc2d66e74cafd16cab9cc856a8bcdc1e1491bf45ca8f0

Passage ID: `qasper-passage-v1-aa93b4f372abba20035dc2d66e74cafd16cab9cc856a8bcdc1e1491bf45ca8f0`; retrieval score: 6.722109726967938.

Word count: 133.

```text
last hidden state of the RNN encoder, our HR-VAE model imposes regularisation for all hidden states of the RNN encoder. Another advantage of our model is that it is generic and can be applied to any existing VAE-RNN-based architectures.

We evaluate our model against several strong baselines which apply VAE for text modelling BIBREF0, BIBREF7, BIBREF5. We conducted experiments based on two public benchmark datasets, namely, the Penn Treebank dataset BIBREF9 and the end-to-end (E2E) text generation dataset BIBREF10. Experimental results show that our HR-VAE model not only can effectively mitigate the latent variable collapse issue with a stable training process, but also can give better predictive performance than the baselines, as evidenced by both quantitative (e.g., negative log likelihood and perplexity) and qualitative evaluation. The code for our model is available online.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-13b0277e2fcece492ea2fdcaa5e09242cf82913005542c132c74bfaa14fd6944

Passage ID: `qasper-passage-v1-13b0277e2fcece492ea2fdcaa5e09242cf82913005542c132c74bfaa14fd6944`; retrieval score: 4.787564739351398.

Word count: 72.

```text
We evaluate our model on two public datasets, namely, Penn Treebank (PTB) BIBREF9 and the end-to-end (E2E) text generation corpus BIBREF10, which have been used in a number of previous works for text generation BIBREF0, BIBREF5, BIBREF11, BIBREF12. PTB consists of more than 40,000 sentences from Wall Street Journal articles whereas the E2E dataset contains over 50,000 sentences of restaurant reviews. The statistics of these two datasets are summarised in Table TABREF11.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-ff5b0cdd25d129f150e846b129e63d5d35099e4a76b496b712037a262f802df4

Passage ID: `qasper-passage-v1-ff5b0cdd25d129f150e846b129e63d5d35099e4a76b496b712037a262f802df4`; retrieval score: 4.69559356335734.

Word count: 400.

```text
Variational Autoencoder (VAE) BIBREF1 is a powerful method for learning representations of high-dimensional data. However, recent attempts of applying VAEs to text modelling are still far less successful compared to its application to image and speech BIBREF2, BIBREF3, BIBREF4. When applying VAEs for text modelling, recurrent neural networks (RNNs) are commonly used as the architecture for both encoder and decoder BIBREF0, BIBREF5, BIBREF6. While such a VAE-RNN based architecture allows encoding and generating sentences (in the decoding phase) with variable-length effectively, it is also vulnerable to an issue known as latent variable collapse (or KL loss vanishing), where the posterior collapses to the prior and the model will ignore the latent codes in generative tasks.

Various efforts have been made to alleviate the latent variable collapse issue. BIBREF0 uses KL annealing, where a variable weight is added to the KL term in the cost function at training time. BIBREF7 discovered that there is a trade-off between the contextual capacity of the decoder and effective use of encoding information, and developed a dilated CNN as decoder which can vary the amount of conditioning context. They also introduced a loss clipping strategy in order to make the model more robust. BIBREF5 addressed the problem by replacing the standard normal distribution for the prior with the von Mises-Fisher (vMF) distribution. With vMF, the KL loss only depends on the concentration parameter which is fixed during training and testing, and hence results in a constant KL loss. In a more recent work, BIBREF6 avoided latent variable collapse by including skip connections in the generative model, where the skip connections enforce strong links between the latent variables and the likelihood function.

Although the aforementioned works show effectiveness in addressing the latent variable collapse issue to some extent, they either require carefully engineering to balance the weight between the reconstruction loss and KL loss BIBREF0, BIBREF8, or resort to designing more sophisticated model structures BIBREF7, BIBREF5, BIBREF6.

In this paper, we present a simple architecture called holistic regularisation VAE (HR-VAE), which can effectively avoid latent variable collapse. In contrast to existing VAE-RNN models for text modelling which merely impose a standard normal distribution prior on the last hidden state of the RNN encoder, our HR-VAE model imposes regularisation for all hidden states of the RNN encoder. Another advantage of our model is that it is generic and can be applied to any existing VAE-RNN-based architectures.

We
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-cf23265d16dc43797ced4fccda1ea26f03e27e499ed3552e66076ff7980128be

Passage ID: `qasper-passage-v1-cf23265d16dc43797ced4fccda1ea26f03e27e499ed3552e66076ff7980128be`; retrieval score: 4.0349361875335505.

Word count: 82.

```text
We compare our HR-VAE model with three strong baselines using VAE for text modelling:

VAE-LSTM-base: A variational autoencoder model which uses LSTM for both encoder and decoder. KL annealing is used to tackled the latent variable collapse issue BIBREF0;

VAE-CNN: A variational autoencoder model with a LSTM encoder and a dilated CNN decoder BIBREF7;

vMF-VAE: A variational autoencoder model using LSTM for both encoder and decoder where the prior distribution is the von Mises-Fisher (vMF) distribution rather than a Gaussian distribution BIBREF5.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1911.05343:5:0` | full | 0:85 |
| `1911.05343:5:1` | full | 0:168 |
| `1911.05343:5:2` | full | 0:95 |
| `1911.05343:5:3` | full | 0:197 |

#### Rank 5: qasper-passage-v1-1e5f06100b272a33e78f42d64f80ac04461ee653b09e8f92ef60ad5e840e2c4c

Passage ID: `qasper-passage-v1-1e5f06100b272a33e78f42d64f80ac04461ee653b09e8f92ef60ad5e840e2c4c`; retrieval score: 2.2837983193255353.

Word count: 368.

```text
In this section, we discuss the technical details of the proposed holistic regularisation VAE (HR-VAE) model, a general architecture which can effectively mitigate the KL vanishing phenomenon.

Our model design is motivated by one noticeable defect shared by the VAE-RNN based models in previous works BIBREF0, BIBREF7, BIBREF5, BIBREF6. That is, all these models, as shown in Figure FIGREF2, only impose a standard normal distribution prior on the last hidden state of the RNN encoder, which potentially leads to learning a suboptimal representation of the latent variable and results in model vulnerable to KL loss vanishing. Our hypothesis is that to learn a good representation of data and a good generative model, it is crucial to impose the standard normal prior on all the hidden states of the RNN-based encoder (see Figure FIGREF2), which allows a better regularisation of the model learning process.

We implement the HR-VAE model using a two-layer LSTM for both the encoder and decoder. However, one should note that our architecture can be readily applied to other types of RNN such as GRU. For each time stamp $t$ (see Figure FIGREF2), we concatenate the hidden state $\mathbf {h}_t$ and the cell state $\mathbf {c}_t$ of the encoder. The concatenation (i.e., $[\mathbf {h}_t;\mathbf {c}_t]$) is then fed into two linear transformation layers for estimating $\mu _t$ and $\sigma ^2_t$, which are parameters of a normal distribution corresponding to the concatenation of $\mathbf {h}_t$ and $\mathbf {c}_t$. Let $Q_{\phi _t}(\mathbf {z}_t | \mathbf {x})=\mathcal {N}(\mathbf {z}_t|\mu _t,\sigma ^2_t)$, we wish $Q_{\phi _t}(\mathbf {z}_t | \mathbf {x})$ to be close to a prior $P(\mathbf {z}_t)$, which is a standard Gaussian. Finally, the KL divergence between these two multivariate Gaussian distributions (i.e., $Q_{\phi _t}$ and $P(\mathbf {z}_t)$) will contribute to the overall KL loss of the ELBO. By taking the average of the KL loss at each time stamp $t$, the resulting ELBO takes the following form

As can be seen in Eq. DISPLAY_FORM10, our solution to the KL collapse issue does not require any engineering for balancing the weight between the reconstruction term and KL loss as commonly the case in existing works BIBREF0, BIBREF8. The weight between these two terms of our model is simply $1:1$.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1055.

Fully covered answer annotations: f5f47a4742b4d1e26a66f1811bd153d545fe13ba.

Missing evidence by answer annotation:

```text
{
  "f5f47a4742b4d1e26a66f1811bd153d545fe13ba": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: 9299fe72f19c1974564ea60278e03a423eb335dc

### Question ID and text

Question ID: `9299fe72f19c1974564ea60278e03a423eb335dc`; paper ID: `2004.01694`.

```text
What was the weakness in Hassan et al's evaluation design?
```

### Answers

#### Answer: 77a93df6767ecde02e609c91ecef4f61735297e4

```text
{"evidence": ["The human evaluation of MT output in research scenarios is typically conducted by crowd workers in order to minimise costs. BIBREF13 shows that aggregated assessments of bilingual crowd workers are very similar to those of MT developers, and BIBREF14, based on experiments with data from WMT 2012, similarly conclude that with proper quality control, MT systems can be evaluated by crowd workers. BIBREF3 also use bilingual crowd workers, but the studies supporting the use of crowdsourcing for MT evaluation were performed with older MT systems, and their findings may not carry over to the evaluation of contemporary higher-quality neural machine translation (NMT) systems. In addition, the MT developers to which crowd workers were compared are usually not professional translators. We hypothesise that expert translators will provide more nuanced ratings than non-experts, and that their ratings will show a higher difference between MT outputs and human translations.", "MT has been evaluated almost exclusively at the sentence level, owing to the fact that most MT systems do not yet take context across sentence boundaries into account. However, when machine translations are compared to those of professional translators, the omission of linguistic context—e. g., by random ordering of the sentences to be evaluated—does not do justice to humans who, in contrast to most MT systems, can and do take inter-sentential context into account BIBREF15, BIBREF16. We hypothesise that an evaluation of sentences in isolation, as applied by BIBREF3, precludes raters from detecting translation errors that become apparent only when inter-sentential context is available, and that they will judge MT quality less favourably when evaluating full documents.", "The human reference translations with which machine translations are compared within the scope of a human–machine parity assessment play an important role. BIBREF3 used all source texts of the WMT 2017 Chinese–English test set for their experiments, of which only half were originally written in Chinese; the other half were translated from English into Chinese. Since translated texts are usually simpler than their original counterparts BIBREF17, they should be easier to translate for MT systems. Moreover, different human translations of the same source text sometimes show considerable differences in quality, and a comparison with an MT system only makes sense if the human reference translations are of high quality. BIBREF3, for example, had the WMT source texts re-translated as they were not convinced of the quality of the human translations in the test set. At WMT 2018, the organisers themselves noted that the manual evaluation included several reports of ill-formed reference translations BIBREF5. We hypothesise that the quality of the human translations has a significant effect on findings of human–machine parity, which would indicate that it is necessary to ensure that human translations used to assess parity claims need to be carefully vetted for their quality."], "extractive_spans": [], "free_form_answer": "MT developers to which crowd workers were compared are usually not professional translators, evaluation of sentences in isolation prevents raters from detecting translation errors, used not originally written Chinese test set\n", "highlighted_evidence": [" BIBREF3 also use bilingual crowd workers, but the studies supporting the use of crowdsourcing for MT evaluation were performed with older MT systems, and their findings may not carry over to the evaluation of contemporary higher-quality neural machine translation (NMT) systems. In addition, the MT developers to which crowd workers were compared are usually not professional translators. ", "We hypothesise that an evaluation of sentences in isolation, as applied by BIBREF3, precludes raters from detecting translation errors that become apparent only when inter-sentential context is available, and that they will judge MT quality less favourably when evaluating full documents.", "BIBREF3 used all source texts of the WMT 2017 Chinese–English test set for their experiments, of which only half were originally written in Chinese; "], "unanswerable": false, "yes_no": null}
```

Evidence location: `2004.01694:4:0`

```text
The human evaluation of MT output in research scenarios is typically conducted by crowd workers in order to minimise costs. BIBREF13 shows that aggregated assessments of bilingual crowd workers are very similar to those of MT developers, and BIBREF14, based on experiments with data from WMT 2012, similarly conclude that with proper quality control, MT systems can be evaluated by crowd workers. BIBREF3 also use bilingual crowd workers, but the studies supporting the use of crowdsourcing for MT evaluation were performed with older MT systems, and their findings may not carry over to the evaluation of contemporary higher-quality neural machine translation (NMT) systems. In addition, the MT developers to which crowd workers were compared are usually not professional translators. We hypothesise that expert translators will provide more nuanced ratings than non-experts, and that their ratings will show a higher difference between MT outputs and human translations.
```

Evidence location: `2004.01694:5:0`

```text
MT has been evaluated almost exclusively at the sentence level, owing to the fact that most MT systems do not yet take context across sentence boundaries into account. However, when machine translations are compared to those of professional translators, the omission of linguistic context—e. g., by random ordering of the sentences to be evaluated—does not do justice to humans who, in contrast to most MT systems, can and do take inter-sentential context into account BIBREF15, BIBREF16. We hypothesise that an evaluation of sentences in isolation, as applied by BIBREF3, precludes raters from detecting translation errors that become apparent only when inter-sentential context is available, and that they will judge MT quality less favourably when evaluating full documents.
```

Evidence location: `2004.01694:6:0`

```text
The human reference translations with which machine translations are compared within the scope of a human–machine parity assessment play an important role. BIBREF3 used all source texts of the WMT 2017 Chinese–English test set for their experiments, of which only half were originally written in Chinese; the other half were translated from English into Chinese. Since translated texts are usually simpler than their original counterparts BIBREF17, they should be easier to translate for MT systems. Moreover, different human translations of the same source text sometimes show considerable differences in quality, and a comparison with an MT system only makes sense if the human reference translations are of high quality. BIBREF3, for example, had the WMT source texts re-translated as they were not convinced of the quality of the human translations in the test set. At WMT 2018, the organisers themselves noted that the manual evaluation included several reports of ill-formed reference translations BIBREF5. We hypothesise that the quality of the human translations has a significant effect on findings of human–machine parity, which would indicate that it is necessary to ensure that human translations used to assess parity claims need to be carefully vetted for their quality.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-91b03d82de9974d20346f8c054417d609a466b21df449c99db6ac78dcbc744d1

Passage ID: `qasper-passage-v1-91b03d82de9974d20346f8c054417d609a466b21df449c99db6ac78dcbc744d1`; retrieval score: 8.091596019444466.

Word count: 325.

```text
Machine translation (MT) has made astounding progress in recent years thanks to improvements in neural modelling BIBREF0, BIBREF1, BIBREF2, and the resulting increase in translation quality is creating new challenges for MT evaluation. Human evaluation remains the gold standard, but there are many design decisions that potentially affect the validity of such a human evaluation.

This paper is a response to two recent human evaluation studies in which some neural machine translation systems reportedly performed at (or above) the level of human translators for news translation from Chinese to English BIBREF3 and English to Czech BIBREF4, BIBREF5.

Both evaluations were based on current best practices in the field: they used a source-based direct assessment with non-expert annotators, using data sets and the evaluation protocol of the Conference on Machine Translation (WMT). While the results are intriguing, especially because they are based on best practices in MT evaluation, BIBREF5 warn against taking their results as evidence for human–machine parity, and caution that for well-resourced language pairs, an update of WMT evaluation style will be needed to keep up with the progress in machine translation. We concur that these findings have demonstrated the need to critically re-evaluate the design of human MT evaluation.

Our paper investigates three aspects of human MT evaluation, with a special focus on assessing human–machine parity: the choice of raters, the use of linguistic context, and the creation of reference translations. We focus on the data shared by BIBREF3, and empirically test to what extent changes in the evaluation design affect the outcome of the human evaluation. We find that for all three aspects, human translations are judged more favourably, and significantly better than MT, when we make changes that we believe strengthen the evaluation design. Based on our empirical findings, we formulate a set of recommendations for human MT evaluation in general, and assessing human–machine parity in particular. All of our data are made publicly available for external validation and further analysis.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-4196e00027e06d20733fe2b31c9ba008c125a1949ced8ecf231ca7e0e4affbee

Passage ID: `qasper-passage-v1-4196e00027e06d20733fe2b31c9ba008c125a1949ced8ecf231ca7e0e4affbee`; retrieval score: 6.798185657381628.

Word count: 361.

```text
We compared professional human Chinese to English translations to the output of a strong MT system. In a human evaluation following best practices, BIBREF3 found no significant difference between the two, concluding that their NMT system had reached parity with professional human translation. Our blind qualitative analysis, however, showed that the machine translation output contained significantly more incorrect words, omissions, mistranslated names, and word order errors.

Our experiments show that recent findings of human–machine parity in language translation are owed to weaknesses in the design of human evaluation campaigns. We empirically tested alternatives to what is currently considered best practice in the field, and found that the choice of raters, the availability of linguistic context, and the creation of reference translations have a strong impact on perceived translation quality. As for the choice of raters, professional translators showed a significant preference for human translation, while non-expert raters did not. In terms of linguistic context, raters found human translation significantly more accurate than machine translation when evaluating full documents, but not when evaluating single sentences out of context. They also found human translation significantly more fluent than machine translation, both when evaluating full documents and single sentences. Moreover, we showed that aggressive editing of human reference translations for target language fluency can decrease adequacy to the point that they become indistinguishable from machine translation, and that raters found human translations significantly better than machine translations of original source texts, but not of source texts that were translations themselves.

Our results strongly suggest that in order to reveal errors in the output of strong MT systems, the design of MT quality assessments with human raters should be revisited. To that end, we have offered a set of recommendations, supported by empirical data, which we believe are needed for assessing human–machine parity, and will strengthen the human evaluation of MT in general. Our recommendations have the aim of increasing the validity of MT evaluation, but we are aware of the high cost of having MT evaluation done by professional translators, and on the level of full documents. We welcome future research into alternative evaluation protocols that can demonstrate their validity at a lower cost.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-6108ce6d2acd8564eceb31e12f60fabf78abde701ebf9c60d20aa12b0a451472

Passage ID: `qasper-passage-v1-6108ce6d2acd8564eceb31e12f60fabf78abde701ebf9c60d20aa12b0a451472`; retrieval score: 6.55280296730282.

Word count: 337.

```text
The evaluation of MT quality has been the subject of controversial discussions in research and the language services industry for decades due to its high economic importance. While automatic evaluation methods are particularly important in system development, there is consensus that a reliable evaluation should—despite high costs—be carried out by humans.

Various methods have been proposed for the human evaluation of MT quality BIBREF8. What they have in common is that the MT output to be rated is paired with a translation hint: the source text or a reference translation. The MT output is then either adapted or scored with reference to the translation hint by human post-editors or raters, respectively.

As part of the large-scale evaluation campaign at WMT, two primary evaluation methods have been used in recent years: relative ranking and direct assessment BIBREF9. In the case of relative ranking, raters are presented with outputs from two or more systems, which they are asked to evaluate relative to each other (e.g., to determine system A is better than system B). Ties (e.g., system A is as good or as bad as system B) are typically allowed. Compared to absolute scores on Likert scales, data obtained through relative ranking show better inter- and intra-annotator agreement BIBREF10. However, they do not allow conclusions to be drawn about the order of magnitude of the differences, so that it is not possible to determine how much better system A was than system B.

This is one of the reasons why direct assessment has prevailed as an evaluation method more recently. In contrast to relative ranking, the raters are presented with one MT output at a time, to which they assign a score between 0 and 100. To increase homogeneity, each rater's ratings are standardised BIBREF11. Reference translations serve as the basis in the context of WMT, and evaluations are carried out by monolingual raters. To avoid reference bias, the evaluation can be based on source texts instead, which presupposes bilingual raters, but leads to more reliable results overall BIBREF12.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-48bad418fb4f7b83beee731c35424c2af290f3c86fada5c38a0e4564a3f18e20

Passage ID: `qasper-passage-v1-48bad418fb4f7b83beee731c35424c2af290f3c86fada5c38a0e4564a3f18e20`; retrieval score: 6.321783327512337.

Word count: 72.

```text
Our experiments in Sections SECREF3–SECREF5 show that machine translation quality has not yet reached the level of professional human translation, and that human evaluation methods which are currently considered best practice fail to reveal errors in the output of strong NMT systems. In this section, we recommend a set of evaluation design changes that we believe are needed for assessing human–machine parity, and will strengthen the human evaluation of MT in general.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-42c1d076f8a035d534d19bb76e00c3b59ddfa0cc9cc07347f9355512fc70dea1

Passage ID: `qasper-passage-v1-42c1d076f8a035d534d19bb76e00c3b59ddfa0cc9cc07347f9355512fc70dea1`; retrieval score: 5.14320824023634.

Word count: 130.

```text
We use English translations of the Chinese source texts in the WMT 2017 English–Chinese test set BIBREF18 for all experiments presented in this article:

[labelwidth=1cm, leftmargin=1.25cm]

The professional human translations in the dataset of BIBREF3.[1]

Professional human translations that we ordered from a different translation vendor, which included a post-hoc native English check. We produced these only for the documents that were originally Chinese, as discussed in more detail in Section SECREF35.

The machine translations produced by BIBREF3's BIBREF3 best system (Combo-6),[1] for which the authors found parity with H$_A$.

The machine translations produced by Google's production system (Google Translate) in October 2017, as contained in BIBREF3's BIBREF3 dataset.[1]

Statistical significance is denoted by * ($p\le .05$), ** ($p\le .01$), and *** ($p\le .001$) throughout this article, unless otherwise stated.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1225.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "77a93df6767ecde02e609c91ecef4f61735297e4": {
    "unresolved_evidence": [],
    "paragraphs": {
      "2004.01694:4:0": [
        [
          0,
          972
        ]
      ],
      "2004.01694:5:0": [
        [
          0,
          777
        ]
      ],
      "2004.01694:6:0": [
        [
          0,
          1284
        ]
      ]
    }
  }
}
```

## Question: 6dc9960f046ec6bd280a721724458f66d5a9a585

### Question ID and text

Question ID: `6dc9960f046ec6bd280a721724458f66d5a9a585`; paper ID: `2002.05058`.

```text
What previous automated evalution approaches authors mention?
```

### Answers

#### Answer: d449825aa0a1d27531a41dd5ec098834f1fde4a8

```text
{"evidence": ["Evaluation of NLG models has been a long-standing open problem. While human evaluation may be ideal, it is generally expensive to conduct and does not scale well. Various automated evaluation approaches are proposed to facilitate the development and evaluation of NLG models. We summarize these evaluation approaches below.", "Text Overlap Metrics, including BLEU BIBREF5, METEOR BIBREF6 and ROUGE BIBREF7, are the most popular metrics employed in the evaluation of NLG models. They evaluate generated text by comparing the similarity between the generated text and human written references. While this works well in tasks where the diversity of acceptable output is limited, such as machine translation and text summarization, text overlap metrics are shown to have weak or no correlation with human judgments in open domain natural language generation tasks BIBREF8. There are two major drawbacks in these metrics. First, text overlap metrics can not distinguish minor variations in a generated text which may make the sentence not equally grammatically correct or semantically meaningful. Second, there may exist multiple equally good outputs for the given input and comparing against one gold reference can be erroneous.", "Perplexity is commonly used to evaluate the quality of a language model. It measures how well a probability distribution predicts a sample and captures the degree of uncertainty in the model. It is used to evaluate models in open-domain NLG tasks such as story generation BIBREF2 and open domain dialogue systems. However, “how likely a sentence is generated by a given model” may not be comparable across different models and does not indicate the quality of the sentence.", "Parameterized Metrics learn a parameterized model to evaluate generated text. Adversarial evaluation models BIBREF11, BIBREF12 assigns a score based on how easy it is to distinguish the dialogue model responses from human responses. However, training such a discriminator can be difficult as the binary classification task can be easily over-fitted and leads to poor generalizability BIBREF11. Moreover, the information we get from the discriminator accuracy is limited as we can not compare the quality of two generated sentences when they both succeed or fail in fooling the discriminator. Recent study shows that the discriminator accuracy does not correlate well with human preference BIBREF13. Automated Dialogue Evaluation Model (ADEM) BIBREF14 is another parameterized metric proposed for dialogue system evaluation. It learns to score a generated dialogue response based on the context and the human written reference. However, it requires human-annotated scores for generated sentences. It is generally hard to design appropriate questions for crowdsourcing these scores, which makes the annotation very expensive to get and the inter-annotator agreement score is only moderate BIBREF14. As a result, the training data is limited and noisy, which makes the scoring task even harder. It can be problematic when comparing models with similar quality. In addition, this model is designed only for evaluating dialogue response generation models. More recently, embedding similarity based metrics such as HUSE BIBREF15 and BERTScore BIBREF16. These metrics alleviate the first problem of text overlap metrics by modeling semantic similarity better. However, they can not address the response diversity problem and thus are only suitable for machine translation and text summarization."], "extractive_spans": ["Text Overlap Metrics, including BLEU", "Perplexity", "Parameterized Metrics"], "free_form_answer": "", "highlighted_evidence": ["Various automated evaluation approaches are proposed to facilitate the development and evaluation of NLG models. We summarize these evaluation approaches below.", "Text Overlap Metrics, including BLEU BIBREF5, METEOR BIBREF6 and ROUGE BIBREF7, are the most popular metrics employed in the evaluation of NLG models.", "Perplexity is commonly used to evaluate the quality of a language model.", "Parameterized Metrics learn a parameterized model to evaluate generated text."], "unanswerable": false, "yes_no": null}
```

Evidence location: `2002.05058:1:0`

```text
Evaluation of NLG models has been a long-standing open problem. While human evaluation may be ideal, it is generally expensive to conduct and does not scale well. Various automated evaluation approaches are proposed to facilitate the development and evaluation of NLG models. We summarize these evaluation approaches below.
```

Evidence location: `2002.05058:1:1`

```text
Text Overlap Metrics, including BLEU BIBREF5, METEOR BIBREF6 and ROUGE BIBREF7, are the most popular metrics employed in the evaluation of NLG models. They evaluate generated text by comparing the similarity between the generated text and human written references. While this works well in tasks where the diversity of acceptable output is limited, such as machine translation and text summarization, text overlap metrics are shown to have weak or no correlation with human judgments in open domain natural language generation tasks BIBREF8. There are two major drawbacks in these metrics. First, text overlap metrics can not distinguish minor variations in a generated text which may make the sentence not equally grammatically correct or semantically meaningful. Second, there may exist multiple equally good outputs for the given input and comparing against one gold reference can be erroneous.
```

Evidence location: `2002.05058:1:2`

```text
Perplexity is commonly used to evaluate the quality of a language model. It measures how well a probability distribution predicts a sample and captures the degree of uncertainty in the model. It is used to evaluate models in open-domain NLG tasks such as story generation BIBREF2 and open domain dialogue systems. However, “how likely a sentence is generated by a given model” may not be comparable across different models and does not indicate the quality of the sentence.
```

Evidence location: `2002.05058:1:3`

```text
Parameterized Metrics learn a parameterized model to evaluate generated text. Adversarial evaluation models BIBREF11, BIBREF12 assigns a score based on how easy it is to distinguish the dialogue model responses from human responses. However, training such a discriminator can be difficult as the binary classification task can be easily over-fitted and leads to poor generalizability BIBREF11. Moreover, the information we get from the discriminator accuracy is limited as we can not compare the quality of two generated sentences when they both succeed or fail in fooling the discriminator. Recent study shows that the discriminator accuracy does not correlate well with human preference BIBREF13. Automated Dialogue Evaluation Model (ADEM) BIBREF14 is another parameterized metric proposed for dialogue system evaluation. It learns to score a generated dialogue response based on the context and the human written reference. However, it requires human-annotated scores for generated sentences. It is generally hard to design appropriate questions for crowdsourcing these scores, which makes the annotation very expensive to get and the inter-annotator agreement score is only moderate BIBREF14. As a result, the training data is limited and noisy, which makes the scoring task even harder. It can be problematic when comparing models with similar quality. In addition, this model is designed only for evaluating dialogue response generation models. More recently, embedding similarity based metrics such as HUSE BIBREF15 and BERTScore BIBREF16. These metrics alleviate the first problem of text overlap metrics by modeling semantic similarity better. However, they can not address the response diversity problem and thus are only suitable for machine translation and text summarization.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-85f7ff824c10dec1c5b12458f94a3fac856f44c47ab4e6f004270c9c80160f6e

Passage ID: `qasper-passage-v1-85f7ff824c10dec1c5b12458f94a3fac856f44c47ab4e6f004270c9c80160f6e`; retrieval score: 7.71726524505249.

Word count: 104.

```text
We set up experiments in order to answer the following research questions:

RQ1: Can the comparative evaluator correlate better with human preference in sample-level than previous automated metrics when evaluating open domain NLG models?

RQ2: Can the comparative evaluator correlate better with human preference in model-level, so that our approach can measure the progress on open domain NLG better?

RQ3: As existing approaches fail to correlate well with human preference, whether and to what extent this problem affects the quality of the final NLG model when performing hyperparameter search and early-stopping?

RQ4: If the previous problem exists, can proposed comparative evaluator reduce this problem?
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-760194c922bb97343f67ba7574e3f9b0c18f344f8903d141b44cf8243f0762e5

Passage ID: `qasper-passage-v1-760194c922bb97343f67ba7574e3f9b0c18f344f8903d141b44cf8243f0762e5`; retrieval score: 2.088583488212354.

Word count: 174.

```text
As our objective is to evaluate the evaluators rather than comparing state-of-the-art models, we choose three representative sequence-to-sequence architectures: LSTM BIBREF27 seq2seq, Convolutional seq2seq BIBREF28, and transformer BIBREF1 model. We compare models with different architectures, hyperparameter choices, and early-stopping criteria with different automated metrics, as well as human evaluation.

Regarding the evaluation metric (and criteria for choosing hyperparameter choice and early-stopping), we compare the proposed approach with the discriminative evaluator, BLEU score (average of 2-, 3-, 4-grams), perplexity, and ADEM. When evaluating generated stories, we cut off the story at the nearest sentence for stories longer than 250 words.

The proposed comparative evaluator is employed for choosing hyperparameter by performing skill rating among all models trained with different hyperparameter choices. For early-stopping, as incrementally performing skill rating is computationally expensive, we propose to perform n (e.g. 1000) pairwise comparison between the samples generated by the latest checkpoint and the previous k (e.g. 2) checkpoints and stop training when the wining rate of latest checkpoint keeps being smaller than its losing rate for 5 iterations.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-3524732778f0174ad33d6795c842730be5690abfc15876db7d3363eb11719edc

Passage ID: `qasper-passage-v1-3524732778f0174ad33d6795c842730be5690abfc15876db7d3363eb11719edc`; retrieval score: 1.9868688566668966.

Word count: 204.

```text
We further investigate the impact of imperfect metrics on training NLG models. As described in the human evaluation procedure, we perform 10 runs to test the reliability of each metric when used to perform hyperparameter tuning and early-stopping respectively. In each run, we select the best hyperparameter combination or early-stopping checkpoint based on each of the five compared metrics. Human evaluation is then employed to identify the best choice. We evaluate the performance of each metric by how many times (out of 10) they succeeded in selecting the best hyperparameter combination or early-stopping checkpoint (out of 4) and the average human-annotated score for their selected models.

The results are shown in Table 3. We can see that conventional automated metrics perform poorly and result in sub-optimal result when performing hyperparameter search and selecting the best performing checkpoints. Converting evaluation metric from BLEU or perplexity to the proposed comparative evaluator can yield non-neglectable improvements without changing model architecture or training objective. While previous work on NLG evaluation mostly focuses on the evaluation stage and does not explore the influence of imperfect metrics during model training, our experiments demonstrate the existence of this problem and that the proposed method can, to some extent, alleviate this problem.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-2a2a8b93957b87cf091794da2ddeb3d992fce6a024fbaa9844fac69662779482

Passage ID: `qasper-passage-v1-2a2a8b93957b87cf091794da2ddeb3d992fce6a024fbaa9844fac69662779482`; retrieval score: 1.618627282709527.

Word count: 400.

```text
Evaluation of NLG models has been a long-standing open problem. While human evaluation may be ideal, it is generally expensive to conduct and does not scale well. Various automated evaluation approaches are proposed to facilitate the development and evaluation of NLG models. We summarize these evaluation approaches below.

Text Overlap Metrics, including BLEU BIBREF5, METEOR BIBREF6 and ROUGE BIBREF7, are the most popular metrics employed in the evaluation of NLG models. They evaluate generated text by comparing the similarity between the generated text and human written references. While this works well in tasks where the diversity of acceptable output is limited, such as machine translation and text summarization, text overlap metrics are shown to have weak or no correlation with human judgments in open domain natural language generation tasks BIBREF8. There are two major drawbacks in these metrics. First, text overlap metrics can not distinguish minor variations in a generated text which may make the sentence not equally grammatically correct or semantically meaningful. Second, there may exist multiple equally good outputs for the given input and comparing against one gold reference can be erroneous.

Perplexity is commonly used to evaluate the quality of a language model. It measures how well a probability distribution predicts a sample and captures the degree of uncertainty in the model. It is used to evaluate models in open-domain NLG tasks such as story generation BIBREF2 and open domain dialogue systems. However, “how likely a sentence is generated by a given model” may not be comparable across different models and does not indicate the quality of the sentence.

Parameterized Metrics learn a parameterized model to evaluate generated text. Adversarial evaluation models BIBREF11, BIBREF12 assigns a score based on how easy it is to distinguish the dialogue model responses from human responses. However, training such a discriminator can be difficult as the binary classification task can be easily over-fitted and leads to poor generalizability BIBREF11. Moreover, the information we get from the discriminator accuracy is limited as we can not compare the quality of two generated sentences when they both succeed or fail in fooling the discriminator. Recent study shows that the discriminator accuracy does not correlate well with human preference BIBREF13. Automated Dialogue Evaluation Model (ADEM) BIBREF14 is another parameterized metric proposed for dialogue system evaluation. It learns to score a generated dialogue response based on the context and the human written reference. However, it requires
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2002.05058:1:0` | full | 0:323 |
| `2002.05058:1:1` | full | 0:897 |
| `2002.05058:1:2` | full | 0:473 |
| `2002.05058:1:3` | partial | 0:947 |

#### Rank 5: qasper-passage-v1-338fe95982adc47c069ddc61142b81ba04ff110b44b89889531c36d8e31f03ed

Passage ID: `qasper-passage-v1-338fe95982adc47c069ddc61142b81ba04ff110b44b89889531c36d8e31f03ed`; retrieval score: 1.5585519312896845.

Word count: 168.

```text
As for model-level evaluation, we employ the average score of the evaluated 100 samples as each model's score and calculate their correlation with human scores. For comparative evaluator, we propose three different approaches to get an absolute score for each sample: 1) we calculate the average reference-based score (method 1 for sample-level comparison) of each sample as model-level score, 2) we calculate the average skill rating of each sample obtained in the experiments of RQ1 as model-level score, 2) we use the proposed skill rating system to get a model-level skill rating for each compared model.

Results are shown in Table 2. We can see that the proposed comparative evaluator with skill rating significantly outperforms all compared baselines, including comparative evaluator with averaged sample-level scores. This demonstrates the effectiveness of the skill rating system for performing model-level comparison with pairwise sample-level evaluation. In addition, the poor correlation between conventional evaluation metrics including BLEU and perplexity demonstrates the necessity of better automated evaluation metrics in open domain NLG evaluation.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 1050.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "d449825aa0a1d27531a41dd5ec098834f1fde4a8": {
    "unresolved_evidence": [],
    "paragraphs": {
      "2002.05058:1:3": [
        [
          947,
          1788
        ]
      ]
    }
  }
}
```

## Question: 12391aab31c899bac0ecd7238c111cb73723a6b7

### Question ID and text

Question ID: `12391aab31c899bac0ecd7238c111cb73723a6b7`; paper ID: `1908.06138`.

```text
Which algorithm is used in the UDS-DFKI system?
```

### Answers

#### Answer: 528d88233ee6b4e23d10e8d614eaebfe86d3839b

```text
{"evidence": ["Our transference model extends the original transformer model to multi-encoder based transformer architecture. The transformer architecture BIBREF12 is built solely upon such attention mechanisms completely replacing recurrence and convolutions. The transformer uses positional encoding to encode the input and output sequences, and computes both self- and cross-attention through so-called multi-head attentions, which are facilitated by parallelization. We use multi-head attention to jointly attend to information at different positions from different representation subspaces."], "extractive_spans": ["Our transference model extends the original transformer model to multi-encoder based transformer architecture. The transformer architecture BIBREF12 is built solely upon such attention mechanisms completely replacing recurrence and convolutions. "], "free_form_answer": "", "highlighted_evidence": ["Our transference model extends the original transformer model to multi-encoder based transformer architecture. The transformer architecture BIBREF12 is built solely upon such attention mechanisms completely replacing recurrence and convolutions. The transformer uses positional encoding to encode the input and output sequences, and computes both self- and cross-attention through so-called multi-head attentions, which are facilitated by parallelization. We use multi-head attention to jointly attend to information at different positions from different representation subspaces."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1908.06138:4:0`

```text
Our transference model extends the original transformer model to multi-encoder based transformer architecture. The transformer architecture BIBREF12 is built solely upon such attention mechanisms completely replacing recurrence and convolutions. The transformer uses positional encoding to encode the input and output sequences, and computes both self- and cross-attention through so-called multi-head attentions, which are facilitated by parallelization. We use multi-head attention to jointly attend to information at different positions from different representation subspaces.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-df3270ef0a7eab59017f59515655495e3f217423ca9d4cd545bad5245533a19e

Passage ID: `qasper-passage-v1-df3270ef0a7eab59017f59515655495e3f217423ca9d4cd545bad5245533a19e`; retrieval score: 7.646831583471749.

Word count: 138.

```text
This paper presented the UDS-DFKI system submitted to the Similar Language Translation shared task at WMT 2019. We presented the results obtained by our system in translating from Czech to Polish. Our system achieved competitive performance ranking second among ten teams in the competition in terms of BLEU score. The fact that out-of-domain data was provided by the organizers resulted in a challenging but interesting scenario for all participants.

In future work, we would like to investigate how effective is the proposed hypothesis (i.e., word-BPE level information) in similar language translation. Furthermore, we would like to explore the similarity between these two languages (and the other two language pairs in the competition) in more detail by training models that can best capture morphological differences between them. During such competitions, this is not always possible due to time constraints.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-5714ae558e5f887476a9172610960bcfe114b051e90cfa847efab83e7cadcdb4

Passage ID: `qasper-passage-v1-5714ae558e5f887476a9172610960bcfe114b051e90cfa847efab83e7cadcdb4`; retrieval score: 7.057699740258325.

Word count: 257.

```text
The shared tasks organized annually at WMT provide important benchmarks used in the MT community. Most of these shared tasks include English data, which contributes to make English the most resource-rich language in MT and NLP. In the most popular WMT shared task for example, the News task, MT systems have been trained to translate texts from and to English BIBREF0, BIBREF1.

This year, we have observed a shift on the dominant role that English on the WMT shared tasks. The News task featured for the first time two language pairs which did not include English: German-Czech and French-German. In addition to that, the Similar Language Translation was organized for the first time at WMT 2019 with the purpose of evaluating the performance of MT systems on three pairs of similar languages from three different language families: Ibero-Romance, Indo-Aryan, and Slavic.

The Similar Language Translation BIBREF2 task provided participants with training, development, and testing data from the following language pairs: Spanish - Portuguese (Romance languages), Czech - Polish (Slavic languages), and Hindi - Nepali (Indo-Aryan languages). Participant could submit system outputs to any of the three language pairs in any direction. The shared task attracted a good number of participants and the performance of all entries was evaluated using popular MT automatic evaluation metrics, namely BLEU BIBREF3 and TER BIBREF4.

In this paper we describe the UDS-DFKI system to the WMT 2019 Similar Language Translation task. The system achieved competitive performance and ranked second among ten entries in Czech to Polish translation in terms of BLEU score.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-e9bb96e3c0c1258b0795b80f0918468a53dbf4952899b979266a85504d0d7ebe

Passage ID: `qasper-passage-v1-e9bb96e3c0c1258b0795b80f0918468a53dbf4952899b979266a85504d0d7ebe`; retrieval score: 5.034420912333242.

Word count: 186.

```text
We present the results obtained by our system in Table TABREF8.

Our fine-tuned system on development set provides significant performance improvement over the generic model. We found +12.9 absolute BLEU points improvement over the generic model. Similar improvement is also observed in terms of TER (-16.9 absolute). It is to be noted that our generic model is trained solely on the clean version of training data.

Before submission, we performed punctuation normalization, unicode normalization, and detokenization for the run.

In Table TABREF9 we present the ranking of the competition provided by the shared task organizers. Ten entries were submitted by five teams and are ordered by BLEU score. TER is reported for all submissions which achieved BLEU score greater than 5.0. The type column specifies the type of system, whether it is a Primary (P) or Constrastive (C) entry.

Our system was ranked second in the competition only 0.3 BLEU points behind the winning team UPC-TALP. The relative low BLEU and high TER scores obtained by all teams are due to out-of-domain data provided in the competition which made the task equally challenging to all participants.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-a05d098ed5aa23a548077a844bea34e3b406ab09e35e6f975e87fea9987a0326

Passage ID: `qasper-passage-v1-a05d098ed5aa23a548077a844bea34e3b406ab09e35e6f975e87fea9987a0326`; retrieval score: 3.724235643860103.

Word count: 309.

```text
The out-domain data is noisy for our purposes, so we apply methods for cleaning. We performed the following two steps: (i) we use the cleaning process described in Pal:2015:WMT, and (ii) we execute the Moses BIBREF10 corpus cleaning scripts with minimum and maximum number of tokens set to 1 and 100, respectively. After cleaning, we perform punctuation normalization, and then we use the Moses tokenizer to tokenize the out-domain corpus with `no-escape' option. Finally, we apply true-casing.

The cleaned version of the released data, i.e., the General corpus containing 1,394,319 sentences, is sorted based on the score in Equation DISPLAY_FORM2. Thereafter, We split the entire data (1,394,319) into two sets; we use the first 1,000 for validation and the remaining as training data. The released development set (Dev) is used as test data for our experiment. It should be noted noted that, we exclude 1,000 sentences from the General corpus which are scored as top (i.e., more in-domain like) during the data selection process.

We prepare two parallel training sets from the aforementioned training data: (i) transference500K(presented next), collected 500,000 parallel data through data selection method BIBREF11, which are very similar to the in-domain data (for our case the development set), and (ii) transferenceALL, utilizing all the released out-domain data sorted by Equation DISPLAY_FORM2.

The transference500Ktraining set is prepared using in-domain (development set) bilingual cross-entropy difference for data selection as was described in Axelrod:2011. The difference in cross-entropy is computed based on two language models (LM): a domain-specific LM is estimated from the in-domain (containing 2050 sentences) corpus ($lm_{i}$) and the out-domain LM ($lm_{o}$) is estimated from the eScape corpus. We rank the eScape corpus by assigning a score to each of the individual sentences which is the sum of the three cross-entropy ($H$) differences. For a $j^{th}$ sentence pair ${src}_j$–${trg}_j$, the score is calculated based on Equation DISPLAY_FORM2.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-4aa98cfa6ee9e3fd5421416da932f9c9fbb73ab5831784d1b7e3a5f58e5a3665

Passage ID: `qasper-passage-v1-4aa98cfa6ee9e3fd5421416da932f9c9fbb73ab5831784d1b7e3a5f58e5a3665`; retrieval score: 3.6558048845526936.

Word count: 210.

```text
For transferenceALL, we initially train on the complete out-of-domain dataset (General). The General data is sorted based on their in-domain similarities as described in Equation DISPLAY_FORM2.

transferenceALLmodels are then fine-tuned towards the 500K (in-domain-like) data. Finally, we perform checkpoint averaging using the 8 best checkpoints. We report the results on the provided development set, which we use as a test set before the submission. Additionally we also report the official test set result.

To handle out-of-vocabulary words and to reduce the vocabulary size, instead of considering words, we consider subword units BIBREF13 by using byte-pair encoding (BPE). In the preprocessing step, instead of learning an explicit mapping between BPEs in the Czech (CS) and Polish (PL), we define BPE tokens by jointly processing all parallel data. Thus, CS and PL derive a single BPE vocabulary. Since CS and PL belong to the similar language, they naturally share a good fraction of BPE tokens, which reduces the vocabulary size.

We pass word level information on the first encoder and the BPE information to the second one. On the decoder side of the transference model we pass only BPE text.

We evaluate our approach with development data which is used as test case before submission. We use BLEU BIBREF3 and TER BIBREF4.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1100.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "528d88233ee6b4e23d10e8d614eaebfe86d3839b": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1908.06138:4:0": [
        [
          0,
          580
        ]
      ]
    }
  }
}
```

## Question: c00ce1e3be14610fb4e1f0614005911bb5ff0302

### Question ID and text

Question ID: `c00ce1e3be14610fb4e1f0614005911bb5ff0302`; paper ID: `1910.06592`.

```text
What activation function do they use in their model?
```

### Answers

#### Answer: 354142e7e6076bf3fc14e3da127f61ab12fc1b7c

```text
{"evidence": ["Experimental Setup. We apply a 5 cross-validation on the account's level. For the FacTweet model, we experiment with 25% of the accounts for validation and parameters selection. We use hyperopt library to select the hyper-parameters on the following values: LSTM layer size (16, 32, 64), dropout ($0.0-0.9$), activation function ($relu$, $selu$, $tanh$), optimizer ($sgd$, $adam$, $rmsprop$) with varying the value of the learning rate (1e-1,..,-5), and batch size (4, 8, 16). The validation split is extracted on the class level using stratified sampling: we took a random 25% of the accounts from each class since the dataset is unbalanced. Discarding the classes' size in the splitting process may affect the minority classes (e.g. hoax). For the baselines' classifier, we tested many classifiers and the LR showed the best overall performance."], "extractive_spans": ["relu", "selu", "tanh"], "free_form_answer": "", "highlighted_evidence": [" We use hyperopt library to select the hyper-parameters on the following values: LSTM layer size (16, 32, 64), dropout ($0.0-0.9$), activation function ($relu$, $selu$, $tanh$), optimizer ($sgd$, $adam$, $rmsprop$) with varying the value of the learning rate (1e-1,..,-5), and batch size (4, 8, 16)"], "unanswerable": false, "yes_no": null}
```

Evidence location: `1910.06592:2:11`

```text
Experimental Setup. We apply a 5 cross-validation on the account's level. For the FacTweet model, we experiment with 25% of the accounts for validation and parameters selection. We use hyperopt library to select the hyper-parameters on the following values: LSTM layer size (16, 32, 64), dropout ($0.0-0.9$), activation function ($relu$, $selu$, $tanh$), optimizer ($sgd$, $adam$, $rmsprop$) with varying the value of the learning rate (1e-1,..,-5), and batch size (4, 8, 16). The validation split is extracted on the class level using stratified sampling: we took a random 25% of the accounts from each class since the dataset is unbalanced. Discarding the classes' size in the splitting process may affect the minority classes (e.g. hoax). For the baselines' classifier, we tested many classifiers and the LR showed the best overall performance.
```

#### Answer: b6df7caf1df11da06f2a9339595a572829796e81

```text
{"evidence": ["Experimental Setup. We apply a 5 cross-validation on the account's level. For the FacTweet model, we experiment with 25% of the accounts for validation and parameters selection. We use hyperopt library to select the hyper-parameters on the following values: LSTM layer size (16, 32, 64), dropout ($0.0-0.9$), activation function ($relu$, $selu$, $tanh$), optimizer ($sgd$, $adam$, $rmsprop$) with varying the value of the learning rate (1e-1,..,-5), and batch size (4, 8, 16). The validation split is extracted on the class level using stratified sampling: we took a random 25% of the accounts from each class since the dataset is unbalanced. Discarding the classes' size in the splitting process may affect the minority classes (e.g. hoax). For the baselines' classifier, we tested many classifiers and the LR showed the best overall performance."], "extractive_spans": [], "free_form_answer": "Activation function is hyperparameter. Possible values: relu, selu, tanh.", "highlighted_evidence": ["We use hyperopt library to select the hyper-parameters on the following values: LSTM layer size (16, 32, 64), dropout ($0.0-0.9$), activation function ($relu$, $selu$, $tanh$), optimizer ($sgd$, $adam$, $rmsprop$) with varying the value of the learning rate (1e-1,..,-5), and batch size (4, 8, 16)."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1910.06592:2:11`

```text
Experimental Setup. We apply a 5 cross-validation on the account's level. For the FacTweet model, we experiment with 25% of the accounts for validation and parameters selection. We use hyperopt library to select the hyper-parameters on the following values: LSTM layer size (16, 32, 64), dropout ($0.0-0.9$), activation function ($relu$, $selu$, $tanh$), optimizer ($sgd$, $adam$, $rmsprop$) with varying the value of the learning rate (1e-1,..,-5), and batch size (4, 8, 16). The validation split is extracted on the class level using stratified sampling: we took a random 25% of the accounts from each class since the dataset is unbalanced. Discarding the classes' size in the splitting process may affect the minority classes (e.g. hoax). For the baselines' classifier, we tested many classifiers and the LR showed the best overall performance.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-7cda5e42d7a94a93a9df001c156c41af9199a5ef21f9f1e84ce0fccb18c6c4b1

Passage ID: `qasper-passage-v1-7cda5e42d7a94a93a9df001c156c41af9199a5ef21f9f1e84ce0fccb18c6c4b1`; retrieval score: 4.357253818256996.

Word count: 400.

```text
each account to assess the accounts factuality. We tested different $k$ values between 10 tweets to the max number of tweets from each account. Figure FIGREF24 shows the macro-F1 values for different $k$ values. It seems that $k=500$ for the top replied tweets achieves the highest result. Therefore, we consider this as a baseline.

Experimental Setup. We apply a 5 cross-validation on the account's level. For the FacTweet model, we experiment with 25% of the accounts for validation and parameters selection. We use hyperopt library to select the hyper-parameters on the following values: LSTM layer size (16, 32, 64), dropout ($0.0-0.9$), activation function ($relu$, $selu$, $tanh$), optimizer ($sgd$, $adam$, $rmsprop$) with varying the value of the learning rate (1e-1,..,-5), and batch size (4, 8, 16). The validation split is extracted on the class level using stratified sampling: we took a random 25% of the accounts from each class since the dataset is unbalanced. Discarding the classes' size in the splitting process may affect the minority classes (e.g. hoax). For the baselines' classifier, we tested many classifiers and the LR showed the best overall performance.

Results. Table TABREF25 presents the results. We present the results using a chunk size of 20, which was found to be the best size on the held-out data. Figure FIGREF24 shows the results of different chunks sizes. FacTweet performs better than the proposed baselines and obtains the highest macro-F1 value of $0.565$. Our results indicate the importance of taking into account the sequence of the tweets in the accounts' timelines. The sequence of these tweets is better captured by our proposed model sequence-agnostic or non-neural classifiers. Moreover, the results demonstrate that the features at tweet-level do not perform well to detect the Twitter accounts factuality, since they obtain a result near to the majority class ($0.18$). Another finding from our experiments shows that the performance of the Tweet2vec is weak. This demonstrates that tweets' hashtags are not informative to detect non-factual accounts. In Table TABREF25, we present ablation tests so as to quantify the contribution of subset of features. The results indicate that most performance gains come from words embeddings, style, and morality features. Other features (emotion and sentiment) show lower importance: nevertheless, they still improve the overall system performance (on average 0.35% Macro-F$_1$ improvement). These performance figures suggest that non-factual accounts use semantic and stylistic hidden signatures mostly while tweeting news, so as to be
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1910.06592:2:11` | full | 0:847 |

#### Rank 2: qasper-passage-v1-e9d5024476d46303eed307ffbeb185d51dc637facf384ed600e1a01587fb6f18

Passage ID: `qasper-passage-v1-e9d5024476d46303eed307ffbeb185d51dc637facf384ed600e1a01587fb6f18`; retrieval score: 1.5592938976494133.

Word count: 283.

```text
affective lexicon that attaches emotional meanings to concepts from the WordNet lexical database. It has $\sim $5.5 words labeled with emotions from a set of 14 emotional categories We use the categories that do not exist in the NRC lexicon.

Sentiment: We extract the sentiment of the tweets by employing EffectWordNet BIBREF13, SenticNet BIBREF14, NRC BIBREF10, and subj_lexicon BIBREF15, where each has the two sentiment classes, positive and negative.

Morality: Features based on morality foundation theory BIBREF16 where words are labeled in one of the following 10 categories (care, harm, fairness, cheating, loyalty, betrayal, authority, subversion, sanctity, and degradation).

Style: We use canonical stylistic features, such as the count of question marks, exclamation marks, consecutive characters and letters, links, hashtags, users' mentions. In addition, we extract the uppercase ratio and the tweet length.

Words embeddings: We extract words embeddings of the words of the tweet using $Glove\-840B-300d$ BIBREF17 pretrained model. The tweet final representation is obtained by averaging its words embeddings.

Model. To account for chunk sequences we make use of a de facto standard approach and opt for a recurrent neural model using long short-term memory (LSTM) BIBREF18. In our model, the sequence consists of a sequence of tweets belonging to one chunk (Figure FIGREF11). The LSTM learns the hidden state $h\textsubscript {t}$ by capturing the previous timesteps (past tweets). The produced hidden state $h\textsubscript {t}$ at each time step is passed to the attention layer which computes a `context' vector $c\textsubscript {t}$ as the weighted mean of the state sequence $h$ by:

Where $T$ is the total number of timesteps in the input sequence and $\alpha \textsubscript {tj}$ is a weight computed at each time step $j$ for each state hj.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-d2c8e14ad5a3d59ac0ea33869c11cec7c68c248bfa3d06e2f5501d2b489c3a53

Passage ID: `qasper-passage-v1-d2c8e14ad5a3d59ac0ea33869c11cec7c68c248bfa3d06e2f5501d2b489c3a53`; retrieval score: 1.3907574406022987.

Word count: 400.

```text
Data. We build a dataset of Twitter accounts based on two lists annotated in previous works. For the non-factual accounts, we rely on a list of 180 Twitter accounts from BIBREF1. This list was created based on public resources where suspicious Twitter accounts were annotated with the main fake news types (clickbait, propaganda, satire, and hoax). We discard the satire labeled accounts since their intention is not to mislead or deceive. On the other hand, for the factual accounts, we use a list with another 32 Twitter accounts from BIBREF19 that are considered trustworthy by independent third parties. We discard some accounts that publish news in languages other than English (e.g., Russian or Arabic). Moreover, to ensure the quality of the data, we remove the duplicate, media-based, and link-only tweets. For each account, we collect the maximum amount of tweets allowed by Twitter API. Table TABREF13 presents statistics on our dataset.

Baselines. We compare our approach (FacTweet) to the following set of baselines:

[leftmargin=4mm]

LR + Bag-of-words: We aggregate the tweets of a feed and we use a bag-of-words representation with a logistic regression (LR) classifier.

Tweet2vec: We use the Bidirectional Gated recurrent neural network model proposed in BIBREF20. We keep the default parameters that were provided with the implementation. To represent the tweets, we use the decoded embedding produced by the model. With this baseline we aim at assessing if the tweets' hashtags may help detecting the non-factual accounts.

LR + All Features (tweet-level): We extract all our features from each tweet and feed them into a LR classifier. Here, we do not aggregate over tweets and thus view each tweet independently.

LR + All Features (chunk-level): We concatenate the features' vectors of the tweets in a chunk and feed them into a LR classifier.

FacTweet (tweet-level): Similar to the FacTweet approach, but at tweet-level; the sequential flow of the tweets is not utilized. We aim at investigating the importance of the sequential flow of tweets.

Top-$k$ replies, likes, or re-tweets: Some approaches in rumors detection use the number of replies, likes, and re-tweets to detect rumors BIBREF21. Thus, we extract top $k$ replied, liked or re-tweeted tweets from each account to assess the accounts factuality. We tested different $k$ values between 10 tweets to the max number of tweets from each account. Figure FIGREF24 shows the macro-F1 values for different $k$ values. It seems that $k=500$ for the
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-4c95cb6ccf54b99c903194d065be1a1813acc09e3ce57d72d0aa59ed812f515a

Passage ID: `qasper-passage-v1-4c95cb6ccf54b99c903194d065be1a1813acc09e3ce57d72d0aa59ed812f515a`; retrieval score: 1.2613727707784916.

Word count: 400.

```text
Given a news Twitter account, we read its tweets from the account's timeline. Then we sort the tweets by the posting date in ascending way and we split them into $N$ chunks. Each chunk consists of a sorted sequence of tweets labeled by the label of its corresponding account. We extract a set of features from each chunk and we feed them into a recurrent neural network to model the sequential flow of the chunks' tweets. We use an attention layer with dropout to attend over the most important tweets in each chunk. Finally, the representation is fed into a softmax layer to produce a probability distribution over the account types and thus predict the factuality of the accounts. Since we have many chunks for each account, the label for an account is obtained by taking the majority class of the account's chunks.

Input Representation. Let $t$ be a Twitter account that contains $m$ tweets. These tweets are sorted by date and split into a sequence of chunks $ck = \langle ck_1, \ldots , ck_n \rangle $, where each $ck_i$ contains $s$ tweets. Each tweet in $ck_i$ is represented by a vector $v \in {\rm I\!R}^d$ , where $v$ is the concatenation of a set of features' vectors, that is $v = \langle f_1, \ldots , f_n \rangle $. Each feature vector $f_i$ is built by counting the presence of tweet's words in a set of lexical lists. The final representation of the tweet is built by averaging the single word vectors.

Features. We argue that different kinds of features like the sentiment of the text, morality, and other text-based features are critical to detect the nonfactual Twitter accounts by utilizing their occurrence during reporting the news in an account's timeline. We employ a rich set of features borrowed from previous works in fake news, bias, and rumors detection BIBREF0, BIBREF1, BIBREF8, BIBREF9.

[leftmargin=4mm]

Emotion: We build an emotions vector using word occurrences of 15 emotion types from two available emotional lexicons. We use the NRC lexicon BIBREF10, which contains $\sim $14K words labeled using the eight Plutchik's emotions BIBREF11. The other lexicon is SentiSense BIBREF12 which is a concept-based affective lexicon that attaches emotional meanings to concepts from the WordNet lexical database. It has $\sim $5.5 words labeled with emotions from a set of 14 emotional categories We use the categories that do not exist in the NRC lexicon.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-20ed55a0512bf47549632758c1fbae25cf3c8144cfb777463620a6e49c3492d3

Passage ID: `qasper-passage-v1-20ed55a0512bf47549632758c1fbae25cf3c8144cfb777463620a6e49c3492d3`; retrieval score: 1.1364445779501708.

Word count: 132.

```text
In this paper, we proposed a model that utilizes chunked timelines of tweets and a recurrent neural model in order to infer the factuality of a Twitter news account. Our experimental results indicate the importance of analyzing tweet stream into chunks, as well as the benefits of heterogeneous knowledge source (i.e., lexica as well as text) in order to capture factuality. In future work, we would like to extend this line of research with further in-depth analysis to understand the flow change of the used features in the accounts' streams. Moreover, we would like to take our approach one step further incorporating explicit temporal information, e.g., using timestamps. Crucially, we are also interested in developing a multilingual version of our approach, for instance by leveraging the now ubiquitous cross-lingual embeddings BIBREF22, BIBREF23.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1615.

Fully covered answer annotations: 354142e7e6076bf3fc14e3da127f61ab12fc1b7c, b6df7caf1df11da06f2a9339595a572829796e81.

Missing evidence by answer annotation:

```text
{
  "354142e7e6076bf3fc14e3da127f61ab12fc1b7c": {
    "unresolved_evidence": [],
    "paragraphs": {}
  },
  "b6df7caf1df11da06f2a9339595a572829796e81": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: e1f5531ed04d0aae1dfcb0559f1512a43134c43a

### Question ID and text

Question ID: `e1f5531ed04d0aae1dfcb0559f1512a43134c43a`; paper ID: `1909.00161`.

```text
Do they use pretrained models?
```

### Answers

#### Answer: 29c88f6014c4d1a5f3c403d81164492759efd792

```text
{"evidence": ["In this work, we make use of the widely-recognized state of the art entailment technique – BERT BIBREF18, and train it on three mainstream entailment datasets: MNLI BIBREF19, GLUE RTE BIBREF20, BIBREF21 and FEVER BIBREF22, respectively. We convert all datasets into binary case: “entailment” vs. “non-entailment”, by changing the label “neutral” (if exist in some datasets) into “non-entailment”.", "For our label-fully-unseen setup, we directly apply this pretrained entailment model on the test sets of all $\\textsc {0shot-tc}$ aspects. For label-partially-unseen setup in which we intentionally provide annotated data, we first pretrain BERT on the MNLI/FEVER/RTE, then fine-tune on the provided training data."], "extractive_spans": [], "free_form_answer": "", "highlighted_evidence": ["In this work, we make use of the widely-recognized state of the art entailment technique – BERT BIBREF18, and train it on three mainstream entailment datasets: MNLI BIBREF19, GLUE RTE BIBREF20, BIBREF21 and FEVER BIBREF22, respectively. We convert all datasets into binary case: “entailment” vs. “non-entailment”, by changing the label “neutral” (if exist in some datasets) into “non-entailment”.\n\nFor our label-fully-unseen setup, we directly apply this pretrained entailment model on the test sets of all $\\textsc {0shot-tc}$ aspects. For label-partially-unseen setup in which we intentionally provide annotated data, we first pretrain BERT on the MNLI/FEVER/RTE, then fine-tune on the provided training data."], "unanswerable": false, "yes_no": true}
```

Evidence location: `1909.00161:19:0`

```text
In this work, we make use of the widely-recognized state of the art entailment technique – BERT BIBREF18, and train it on three mainstream entailment datasets: MNLI BIBREF19, GLUE RTE BIBREF20, BIBREF21 and FEVER BIBREF22, respectively. We convert all datasets into binary case: “entailment” vs. “non-entailment”, by changing the label “neutral” (if exist in some datasets) into “non-entailment”.
```

Evidence location: `1909.00161:19:1`

```text
For our label-fully-unseen setup, we directly apply this pretrained entailment model on the test sets of all $\textsc {0shot-tc}$ aspects. For label-partially-unseen setup in which we intentionally provide annotated data, we first pretrain BERT on the MNLI/FEVER/RTE, then fine-tune on the provided training data.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-d19e218637da7ded83475266e956311a52cd35740c561ef320d3357df12d8f93

Passage ID: `qasper-passage-v1-d19e218637da7ded83475266e956311a52cd35740c561ef320d3357df12d8f93`; retrieval score: 6.274959513714795.

Word count: 365.

```text
$\textsc {Zero-stc}$ was first explored by the paradigm “Dataless Classification” BIBREF0. Dataless classification first maps the text and labels into a common space by Explicit Semantic Analysis (ESA) BIBREF4, then picks the label with the highest matching score. Dataless classification emphasizes that the representation of labels takes the equally crucial role as the representation learning of text. Then this idea was further developed in BIBREF5, BIBREF6, BIBREF7, BIBREF8, BIBREF9.

With the prevalence of word embeddings, more and more work adopts pretrained word embeddings to represent the meaning of words, so as to provide the models with the knowledge of labels BIBREF10, BIBREF2, BIBREF11, BIBREF12. DBLPYogatamaDLB17 build generative LSTM to generate text given the embedded labels. DBLPRiosK18 use label embedding to attend the text representation in the developing of a multi-label classifier. But they report R@K, so it is unclear whether the system can really predict unseen labels. DBLPXiaZYCY18 study the zero-shot intent detection problem. The learned representations of intents are still the sum of word embeddings. But during testing, the intent space includes only new intents; seen intents are not covered. All of these studies can only meet the definition in Definition-Restrictive, so they do not really generalize to open aspects of $\textsc {0shot-tc}$.

JiangqngGuo enrich the embedding representations by incorporating class descriptions, class hierarchy, and the word-to-label paths in ConceptNet. DBLPMitchellSL18 assume that some natural language explanations about new labels are available. Then those explanations are parsed into formal constraints which are further combined with unlabeled data to yield new label oriented classifiers through posterior regularization. However, those explanatory statements about new labels are collected from crowd-sourcing. This limits its application in real world $\textsc {0shot-tc}$ scenarios.

There are a few works that study a specific zero-shot problem by indirect supervision from other problems. DBLPLevySCZ17 and obamuyide2018zero study zero-shot relation extraction by converting it into a machine comprehension and textual entailment problem respectively. Then, a supervised system pretrained on an existing machine comprehension dataset or textual entailment dataset is used to do inference. Our work studies the $\textsc {0shot-tc}$ by formulating a broader vision: datasets of multiple apsects and evaluations.

Other zero-shot problems studied in NLP involve entity typing BIBREF13, sequence labeling BIBREF14, etc.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-3176abd446f1bbb5cca8e517afebd736244b5818e8ec86caa4ecc5cbd8ddaea7

Passage ID: `qasper-passage-v1-3176abd446f1bbb5cca8e517afebd736244b5818e8ec86caa4ecc5cbd8ddaea7`; retrieval score: 4.65369750177656.

Word count: 334.

```text
In Table TABREF24, we listed examples for converting class names into hypotheses. In this work, we only tried to make use of the class names and their definitions in WordNet. Table TABREF33 lists the fine-grained performance of three ways of generating hypotheses: “word”, “definition”, and “combination” (i.e., word&definition).

This table indicates that: i) Definition alone usually does not work well in any of the three tasks, no matter which pretrained entailment model is used; ii) Whether “word” alone or “word&definition” works better depends on the specific task and the pretrained entailment model. For example, the pretrained MNLI model prefers “word&definition” in both “emotion” and “situation” detection tasks. However, the other two entailment models (RTE and FEVER) mostly prefer “word”. iii) Since it is unrealistic to adopt only one entailment model, such as from {RTE, FEVER, MNLI}, for any open $\textsc {0shot-tc}$ problem, an ensemble system should be preferred. However, the concrete implementation of the ensemble system also influences the strengths of different hypothesis generation approaches. In this work, our ensemble method reaches the top performance when combining the “word” and “definition”. More ensemble systems and hypothesis generation paradigms need to be studied in the future.

To better understand the impact of generated hypotheses, we dive into the performance of each labels, taking “situation detection” as an example. Figure FIGREF47 illustrates the separate F1 scores for each situation class, predicted by the ensemble model for label-fully-unseen setup. This enables us to check in detail how easily the constructed hypotheses can be understood by the entailment model. Unfortunately, some classes are still challenging, such as “evacuation”, “infrastructure”, and “regime change”. This should be attributed to their over-abstract meaning. Some classes were well recognized, such as “water”, “shelter”, and “food”. One reason is that these labels mostly are common words – systems can more easily match them to the text; the other reason is that they are situation classes with higher frequencies (refer to Table TABREF22) – this is reasonable based on our common knowledge about disasters.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-ecc5b9c3dc0961a5ba4cb13286ae4d1aae2e78dcf88063612d591d4ea962d46e

Passage ID: `qasper-passage-v1-ecc5b9c3dc0961a5ba4cb13286ae4d1aae2e78dcf88063612d591d4ea962d46e`; retrieval score: 4.426216999936189.

Word count: 356.

```text
Regarding this label-fully-unseen evaluation, apart from our entailment models and three unsupervised baselines “Majority”, “Word2Vec” and “ESA”, we also report the following baseline:

Wikipedia-based: We train a binary classifier based on BERT on a dataset collected from Wikipedia. Wikipedia is a corpus of general purpose, without targeting any specific $\textsc {0shot-tc}$ task. Collecting categorized articles from Wikipedia is popular way of creating training data for text categorization, such as BIBREF13. More specifically, we collected 100K articles along with their categories in the bottom of each article. For each article, apart from its attached positive categories, we randomly sample three negative categories. Then each article and its positive/negative categories act as training pairs for the binary classifier.

We notice “Wikipedia-based” training indeed contributes a lot for the topic detection task; however, its performances on emotion and situation detection problems are far from satisfactory. We believe this is mainly because the Yahoo-based topic categorization task is much closer to the Wikipedia-based topic categorization task; emotion and situation categorizations, however, are relatively further.

Our entailment models, pretrained on MNLI/FEVER/RTE respectively, perform more robust on the three $\textsc {0shot-tc}$ aspects (except for the RTE on emotion). Recall that they are not trained on any text classification data, and never know the domain and the aspects in the test. This clearly shows the great promise of developing textual entailment models for $\textsc {0shot-tc}$. Our ensemble approach further boosts the performances on all three tasks.

An interesting phenomenon, comparing the label-partially-unseen results in Table TABREF30 and the label-fully-unseen results in Table TABREF32, is that the pretrained entailment models work in this order for label-fully-unseen case: RTE $>$ FEVER $>$MNLI; on the contrary, if we fine-tune them on the label-partially-unseen case, the MNLI-based model performs best. This could be due to a possibility that, on one hand, the constructed situation entailment dataset is closer to the RTE dataset than to the MNLI dataset, so an RTE-based model can generalize well to situation data, but, on the other hand, it could also be more likely to over-fit the training set of “situation” during fine-tuning. A deeper exploration of this is left as future work.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-3ae9ec9c04cfb6bc836046541b250426d69bc92e54a047386b7d35ef5f43aa08

Passage ID: `qasper-passage-v1-3ae9ec9c04cfb6bc836046541b250426d69bc92e54a047386b7d35ef5f43aa08`; retrieval score: 3.4944194629142973.

Word count: 230.

```text
The results of label-partially-unseen are listed in Table TABREF30. “ESA” performs slightly worse than “Word2Vec” in topic detection, mainly because the label names, i.e., topics such as “sports”, are closer than some keywords such as “basketball” in Word2Vec space. However, “ESA” is clearly better than “Word2Vec” in situation detection; this should be mainly due to the fact that the label names (e.g., “shelter”, “evaculation”, etc.) can hardly find close words in the text by Word2Vec embeddings. Quite the contrary, “ESA” is easier to make a class such as “shelter” closer to some keywords like “earthquake”. Unfortunately, both Word2Vec and ESA work poorly for emotion detection problem. We suspect that emotion detection requires more entailment capability. For example, the text snippet “when my brother was very late in arriving home from work”, its gold emotion “fear” requires some common-knowledge inference, rather than just word semantic matching through Word2Vec and ESA.

The supervised method “Binary-BERT” is indeed strong in learning the seen-label-specific models – this is why it predicts very well for seen classes while performing much worse for unseen classes.

Our entailment models, especially the one pretrained on MNLI, generally get competitive performance with the “Binary-BERT” for seen (slightly worse on “topic” and “emotion” while clearly better on “situation”) and improve the performance regarding unseen by large margins. At this stage, fine-tuning on an MNLI-based pretrained entailment model seems more powerful.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-2d36386e6ddeef659792b525984231ffc9ae9412a0ab4b13c2648798d81efac2

Passage ID: `qasper-passage-v1-2d36386e6ddeef659792b525984231ffc9ae9412a0ab4b13c2648798d81efac2`; retrieval score: 3.052865997378742.

Word count: 102.

```text
In this work, we make use of the widely-recognized state of the art entailment technique – BERT BIBREF18, and train it on three mainstream entailment datasets: MNLI BIBREF19, GLUE RTE BIBREF20, BIBREF21 and FEVER BIBREF22, respectively. We convert all datasets into binary case: “entailment” vs. “non-entailment”, by changing the label “neutral” (if exist in some datasets) into “non-entailment”.

For our label-fully-unseen setup, we directly apply this pretrained entailment model on the test sets of all $\textsc {0shot-tc}$ aspects. For label-partially-unseen setup in which we intentionally provide annotated data, we first pretrain BERT on the MNLI/FEVER/RTE, then fine-tune on the provided training data.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1909.00161:19:0` | full | 0:396 |
| `1909.00161:19:1` | full | 0:313 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1387.

Fully covered answer annotations: 29c88f6014c4d1a5f3c403d81164492759efd792.

Missing evidence by answer annotation:

```text
{
  "29c88f6014c4d1a5f3c403d81164492759efd792": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: 35915166ab2fd3d39c0297c427d4ac00e8083066

### Question ID and text

Question ID: `35915166ab2fd3d39c0297c427d4ac00e8083066`; paper ID: `1910.10324`.

```text
Do they just sum up all the loses the calculate to end up with one single loss?
```

### Answers

#### Answer: c84e6b5dd4cad675549fefc0b9eb2da817cb56b7

```text
{"evidence": ["We have found it beneficial to apply the loss function at several intermediate layers of the network. Suppose there are $M$ total layers, and define a subset of these layers at which to apply the loss function: $K = \\lbrace k_1, k_2, ..., k_L\\rbrace \\subseteq \\lbrace 1,..,M-1\\rbrace $. The total objective function is then defined as", "where $Z_{k_l}$ is the $k_l$-th Transformer layer activations, $Y$ is the ground-truth transcription for CTC and context dependent states for hybrid ASR, and $Loss(P, Y)$ can be defined as CTC objective BIBREF11 or cross entropy for hybrid ASR. The coefficient $\\lambda $ scales the auxiliary loss and we set $\\lambda = 0.3$ based on our preliminary experiments. We illustrate the auxiliary prediction and loss in Figure FIGREF6."], "extractive_spans": [], "free_form_answer": "", "highlighted_evidence": ["Suppose there are $M$ total layers, and define a subset of these layers at which to apply the loss function: $K = \\lbrace k_1, k_2, ..., k_L\\rbrace \\subseteq \\lbrace 1,..,M-1\\rbrace $. The total objective function is then defined as\n\nwhere $Z_{k_l}$ is the $k_l$-th Transformer layer activations, $Y$ is the ground-truth transcription for CTC and context dependent states for hybrid ASR, and $Loss(P, Y)$ can be defined as CTC objective BIBREF11 or cross entropy for hybrid ASR. T"], "unanswerable": false, "yes_no": false}
```

Evidence location: `1910.10324:4:0`

```text
We have found it beneficial to apply the loss function at several intermediate layers of the network. Suppose there are $M$ total layers, and define a subset of these layers at which to apply the loss function: $K = \lbrace k_1, k_2, ..., k_L\rbrace \subseteq \lbrace 1,..,M-1\rbrace $. The total objective function is then defined as
```

Evidence location: `1910.10324:4:1`

```text
where $Z_{k_l}$ is the $k_l$-th Transformer layer activations, $Y$ is the ground-truth transcription for CTC and context dependent states for hybrid ASR, and $Loss(P, Y)$ can be defined as CTC objective BIBREF11 or cross entropy for hybrid ASR. The coefficient $\lambda $ scales the auxiliary loss and we set $\lambda = 0.3$ based on our preliminary experiments. We illustrate the auxiliary prediction and loss in Figure FIGREF6.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-86baaf8c15694903fb83612ff488b8688e728ff34b608bac13e0515077a621b9

Passage ID: `qasper-passage-v1-86baaf8c15694903fb83612ff488b8688e728ff34b608bac13e0515077a621b9`; retrieval score: 9.057573303275532.

Word count: 214.

```text
Table TABREF19 presents CTC based results for the Librispeech dataset, without data augmentation. Our baseline is a 24 layer Transformer network trained with CTC. For the proposed method, we varied the number and placement of iterated loss and the feature re-presentation. The next three results show the effect of using CTC multiple times. We see 12 and 8% relative improvements for test-clean and test-other. Adding feature re-presentation gives a further boost, with net 20 and 18% relative improvements over the baseline.

Table TABREF20 shows results for Librispeech with SpecAugment. We test both CTC and CE/hybrid systems. There are consistent gains first from iterated loss, and then from multiple feature presentation. We also run additional CTC experiments with 36 layers Transformer (total parameters $\pm $120 millions). The baseline with 36 layers has the same performance with 24 layers, but by adding the proposed methods, the 36 layer performance improved to give the best results. This shows that our proposed methods can improve even very deep models.

As shown in Table TABREF21, the proposed methods also provide large performance improvements on the curated video set, up to 13% with CTC, and up to 9% with the hybrid model. We also observe moderate gains of between 3.2 and 8% relative on the clean and noisy video sets.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-10f060e3f39c6ffbb19c103711d42f624feb63d6cc3c968c0fbe5d84022f747f

Passage ID: `qasper-passage-v1-10f060e3f39c6ffbb19c103711d42f624feb63d6cc3c968c0fbe5d84022f747f`; retrieval score: 7.209324960820691.

Word count: 222.

```text
In recent years, Transformer models have become an active research topic in speech processing. The key features of Transformer networks is self-attention, which produces comparable or better performance to LSTMs when used for encoder-decoder based ASR BIBREF23, as well as when trained with CTC BIBREF9. Speech-Transformers BIBREF24 also produce comparable performance to the LSTM-based attention model, but with higher training speed in a single GPU. Abdelrahman et al.BIBREF8 integrates a convolution layer to capture audio context and reduces WER in Librispeech.

The use of an objective function in intermediate layers has been found useful in several previous works such as image classification BIBREF25 and language modeling BIBREF26. In BIBREF27, the authors did pre-training with an RNN-T based model by using a hierarchical CTC criterion with different target units. In this paper, we don't need additional types of target unit, instead we just use same tokenization and targets for both intermediate and final losses.

The application of the objective function to intermediate layers is also similar in spirit to the use of KL-divergence in BIBREF28, which estimates output posteriors at an intermediate layer and regularizes them towards the distributions at the final layer. In contrast to this approach, the direct application of the objective function does not require the network to have a good output distribution before the new gradient contribution is meaningful.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-c393822da4df4abdaafd2fc7d2835c8c3b5d3373b01d99735e4c76e4c8e5af6c

Passage ID: `qasper-passage-v1-c393822da4df4abdaafd2fc7d2835c8c3b5d3373b01d99735e4c76e4c8e5af6c`; retrieval score: 6.288162482214055.

Word count: 107.

```text
In this section, we present our proposal for allowing the network to (re)-consider the input features in the light of intermediate processing. We do this by again deploying a self-attention mechanism to combine the information present in the original features with the information available in the activations of an intermediate layer. As described earlier, we calculate the output posteriors and auxiliary loss at the intermediate layer as well. The overall architecture is illustrated in Figure FIGREF6. Here, we have used a 24 layer network, with feature re-presentation after the 12th layer.

In the following subsections, we provide detail on the feature re-presentation mechanism, and iterated loss calculation.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-d899f862e03a0a26396ee68d0fb8bf91da0ee0116f725651a50c6dff70c6393b

Passage ID: `qasper-passage-v1-d899f862e03a0a26396ee68d0fb8bf91da0ee0116f725651a50c6dff70c6393b`; retrieval score: 5.976067553834099.

Word count: 97.

```text
In this paper, we have proposed a method for re-processing the input features in light of the information available at an intermediate network layer. We do this in the context of deep transformer networks, via a self-attention mechanism on both features and hidden states representation. To encourage meaningful partial results, we calculate the objective function at intermediate layers of the network as well as the output layer. This improves performance in and of itself, and when combined with feature re-presentation we observe consistent relative improvements of 10 - 20% for Librispeech and 3.2 - 13% for videos.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-023b035b546817e0d918abc5d7bab8d81e8a4d70450a27bff3cbdca694bdfeff

Passage ID: `qasper-passage-v1-023b035b546817e0d918abc5d7bab8d81e8a4d70450a27bff3cbdca694bdfeff`; retrieval score: 3.984177365505434.

Word count: 400.

```text
In this paper, we propose the processing of features not only in the input layer of a deep network, but in the intermediate layers as well. We are motivated by a desire to enable a neural network acoustic model to adaptively process the features depending on partial hypotheses and noise conditions. Many previous methods for adaptation have operated by linearly transforming either input features or intermediate layers in a two pass process where the transform is learned to maximize the likelihood of some adaptation data BIBREF0, BIBREF1, BIBREF2. Other methods have involved characterizing the input via factor analysis or i-vectors BIBREF3, BIBREF4. Here, we suggest an alternative approach in which adaptation can be achieved by re-presenting the feature stream at an intermediate layer of the network that is constructed to be correlated with the ultimate graphemic or phonetic output of the system.

We present this work in the context of Transformer networks BIBREF5. Transformers have become a popular deep learning architecture for modeling sequential datasets, showing improvements in many tasks such as machine translation BIBREF5, language modeling BIBREF6 and autoregressive image generation BIBREF7. In the speech recognition field, Transformers have been proposed to replace recurrent neural network (RNN) architectures such as LSTMs and GRUs BIBREF8. A recent survey of Transformers in many speech related applications may be found in BIBREF9. Compared to RNNs, Transformers have several advantages, specifically an ability to aggregate information across all the time-steps by using a self-attention mechanism. Unlike RNNs, the hidden representations do not need to be computed sequentially across time, thus enabling significant efficiency improvements via parallelization.

In the context of Transformer module, secondary feature analysis is enabled through an additional mid-network transformer module that has access both to previous-layer activations and the raw features. To implement this model, we apply the objective function several times at the intermediate layers, to encourage the development of phonetically relevant hypotheses. Interestingly, we find that the iterated use of an auxiliary loss in the intermediate layers significantly improves performance by itself, as well as enabling the secondary feature analysis.

This paper makes two main contributions:

We present improvements in the basic training process of deep transformer networks, specifically the iterated use of CTC or CE in intermediate layers, and

We show that an intermediate-layer attention model with access to both previous-layer activations and raw feature inputs can significantly improve performance.

We evaluate our proposed model on Librispeech
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1040.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "c84e6b5dd4cad675549fefc0b9eb2da817cb56b7": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1910.10324:4:0": [
        [
          0,
          334
        ]
      ],
      "1910.10324:4:1": [
        [
          0,
          429
        ]
      ]
    }
  }
}
```

## Question: a15bc19674d48cd9919ad1cf152bf49c88f4417d

### Question ID and text

Question ID: `a15bc19674d48cd9919ad1cf152bf49c88f4417d`; paper ID: `1805.06966`.

```text
what corpus is used to learn behavior?
```

### Answers

#### Answer: c1ed3e2a6e21d189790e8b23f0edc5422b51ec52

```text
{"evidence": ["In this paper the Neural User Simulator (NUS) is introduced which outputs natural language and whose behaviour is learned from a corpus. The main component, inspired by BIBREF4 , consists of a feature extractor and a neural network based sequence-to-sequence model BIBREF5 . The sequence-to-sequence model consists of a recurrent neural network (RNN) encoder that encodes the dialogue history and a decoder RNN which outputs natural language. Furthermore, the NUS generates its own goal and possibly changes it during a dialogue. This allows the model to be deployed for training more sophisticated DM policies. To achieve this, a method is proposed that transforms the goal-labels of the used dataset (DSTC2) into labels whose behaviour can be replicated during deployment."], "extractive_spans": ["DSTC2"], "free_form_answer": "", "highlighted_evidence": ["To achieve this, a method is proposed that transforms the goal-labels of the used dataset (DSTC2) into labels whose behaviour can be replicated during deployment."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1805.06966:0:2`

```text
In this paper the Neural User Simulator (NUS) is introduced which outputs natural language and whose behaviour is learned from a corpus. The main component, inspired by BIBREF4 , consists of a feature extractor and a neural network based sequence-to-sequence model BIBREF5 . The sequence-to-sequence model consists of a recurrent neural network (RNN) encoder that encodes the dialogue history and a decoder RNN which outputs natural language. Furthermore, the NUS generates its own goal and possibly changes it during a dialogue. This allows the model to be deployed for training more sophisticated DM policies. To achieve this, a method is proposed that transforms the goal-labels of the used dataset (DSTC2) into labels whose behaviour can be replicated during deployment.
```

#### Answer: e89a4ff03c55b1be6dd8bff517f6f3f9822e4235

```text
{"evidence": ["The manual transcriptions of the DSTC2 training set (not the ASR output) were used to train the sequence-to-sequence model. Since the transcriptions were done manually they contained spelling errors. These were manually corrected to ensure proper delexicalization. Some dialogues were discarded due to transcriptions errors being too large. After cleaning the dataset the training set consisted of 1609 dialogues with a total of 11638 dialogue turns. The validation set had 505 dialogues with 3896 dialogue turns. The maximum sequence length of the delexicalized turns was 22, including the end of sentence character. The maximum dialogue length was 30 turns."], "extractive_spans": ["The manual transcriptions of the DSTC2 training set "], "free_form_answer": "", "highlighted_evidence": ["The manual transcriptions of the DSTC2 training set (not the ASR output) were used to train the sequence-to-sequence model. "], "unanswerable": false, "yes_no": null}
```

Evidence location: `1805.06966:7:2`

```text
The manual transcriptions of the DSTC2 training set (not the ASR output) were used to train the sequence-to-sequence model. Since the transcriptions were done manually they contained spelling errors. These were manually corrected to ensure proper delexicalization. Some dialogues were discarded due to transcriptions errors being too large. After cleaning the dataset the training set consisted of 1609 dialogues with a total of 11638 dialogue turns. The validation set had 505 dialogues with 3896 dialogue turns. The maximum sequence length of the delexicalized turns was 22, including the end of sentence character. The maximum dialogue length was 30 turns.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-ec497ad5eecfaa2cf6bc1ac2eeb419d1a9ab7c800492b46ad7376076fa3e6be9

Passage ID: `qasper-passage-v1-ec497ad5eecfaa2cf6bc1ac2eeb419d1a9ab7c800492b46ad7376076fa3e6be9`; retrieval score: 10.340410977445263.

Word count: 400.

```text
Ideally the DM's policy would be trained by interacting with real users. Although there are models that support on-line learning BIBREF15 , for the majority of RL algorithms, which require a lot of interactions, this is impractical. Furthermore, a set of users needs to be recruited every time a policy is trained. This makes common practices such as hyper-parameter optimization prohibitively expensive. Thus, it is natural to try to learn from a dataset which needs to be recorded only once, but can be used over and over again.

A problem with learning directly from recorded dialogue corpora is that the state space that was visited during the collection of the data is limited; the size of the recorded corpus usually falls short of the requirements for training a statistical DM. However, even if the size of the corpus is large enough the optimal dialogue strategy is likely not to be contained within it.

A solution is to transform the static corpus into a dynamic tool: a user simulator. The user simulator (US) is trained on a dialogue corpus to learn what responses a real user would provide in a given dialogue context. The US is trained using supervised learning since the aim is for it to learn typical user behaviour. For the DM, however, we want optimal behaviour which is why supervised learning cannot be used. By interacting with the SDS, the trained US can be used to train the DM's policy. The DM's policy is optimised using the feedback given by either the user simulator or a separate evaluator. Any number of dialogues can be generated using the US and dialogue strategies that are not in the recorded corpus can be explored.

Most user-simulators work on the level of user semantics. These usually consist of a user dialogue act (e.g. inform, or request) and a corresponding slot-value pair. The first statistical user simulator BIBREF16 used a simple bi-gram model INLINEFORM0 to predict the next user act INLINEFORM1 given the last system act INLINEFORM2 . It has the advantage of being purely probabilistic and domain-independent. However, it does not take the full dialogue history into account and is not conditioned on a goal, leading to incoherent user behaviour throughout a dialogue. BIBREF17 , BIBREF18 attempted to overcome goal inconsistency by proposing a graph-based model. However, developing the graph structure requires extensive domain-specific knowledge. BIBREF19 combined features from Sheffler and Young's
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-f286edd1779462d9da62fbc1a5c26fdd62785c2d84ba768394eb0e4096837dc3

Passage ID: `qasper-passage-v1-f286edd1779462d9da62fbc1a5c26fdd62785c2d84ba768394eb0e4096837dc3`; retrieval score: 4.561403697395281.

Word count: 162.

```text
A Task-Oriented SDS is typically designed according to a structured ontology, which defines what the system can talk about. In a system recommending restaurants the ontology defines those attributes of a restaurant that the user can choose, called informable slots (e.g. different food types, areas and price ranges), the attributes that the user can request, called requestable slots (e.g. phone number or address) and the restaurants that it has data about. An attribute is referred to as a slot and has a corresponding value. Together these are referred to as a slot-value pair (e.g. area=north).

Using RL the DM is trained to act such that is maximises the cumulative future reward. The process by which the DM chooses its next action is called its policy. A typical approach to defining the reward function for a task-oriented SDS is to apply a small per-turn penalty to encourage short dialogues and to give a large positive reward at the end of each successful interaction.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-91c74578c2edeb54235249bda03b79d5fe30e86d53accd4ce1130e1e2d8134b7

Passage ID: `qasper-passage-v1-91c74578c2edeb54235249bda03b79d5fe30e86d53accd4ce1130e1e2d8134b7`; retrieval score: 4.132114743569586.

Word count: 400.

```text
Spoken Dialogue Systems (SDS) allow human-computer interaction using natural speech. Task-oriented dialogue systems, the focus of this work, help users achieve goals such as finding restaurants or booking flights BIBREF0 .

Teaching a system how to respond appropriately in a task-oriented setting is non-trivial. In state-of-the-art systems this dialogue management task is often formulated as a reinforcement learning (RL) problem BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 . In this framework, the system learns by a trial and error process governed by a reward function. User Simulators can be used to train the policy of a dialogue manager (DM) without real user interactions. Furthermore, they allow an unlimited number of dialogues to be created with each dialogue being faster than a dialogue with a human.

In this paper the Neural User Simulator (NUS) is introduced which outputs natural language and whose behaviour is learned from a corpus. The main component, inspired by BIBREF4 , consists of a feature extractor and a neural network based sequence-to-sequence model BIBREF5 . The sequence-to-sequence model consists of a recurrent neural network (RNN) encoder that encodes the dialogue history and a decoder RNN which outputs natural language. Furthermore, the NUS generates its own goal and possibly changes it during a dialogue. This allows the model to be deployed for training more sophisticated DM policies. To achieve this, a method is proposed that transforms the goal-labels of the used dataset (DSTC2) into labels whose behaviour can be replicated during deployment.

The NUS is trained on dialogues between real users and an SDS in a restaurant recommendation domain. Compared to much of the related work on user simulation, we use the trained NUS to train the policy of a reinforcement learning based SDS. In order to evaluate the NUS, an Agenda-Based User-Simulator (ABUS) BIBREF6 is used to train another policy. The two policies are compared against each other by using cross-model evaluation BIBREF7 . This means to train on one model and to test on the other. Furthermore, both trained policies are tested on real users. On both evaluation tasks the NUS outperforms the ABUS, which is currently one of the most popular off-line training tools for reinforcement learning based Spoken Dialogue Systems BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 , BIBREF13 , BIBREF14 .

The remainder of this paper is organised as follows. Section 2 briefly describes task-oriented dialogue. Section 3 describes the motivation
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1805.06966:0:2` | full | 0:774 |

#### Rank 4: qasper-passage-v1-dee9f839fb40096ef2fe0fdd350761de8d2384abef69b09aab0615876c95902f

Passage ID: `qasper-passage-v1-dee9f839fb40096ef2fe0fdd350761de8d2384abef69b09aab0615876c95902f`; retrieval score: 3.6819247132076036.

Word count: 119.

```text
We introduced the Neural User Simulator (NUS), which uses the system's response in its semantic form as input and gives a natural language response. It thus needs less labelling of the training data than User Simulators that generate a response in semantic form. It was shown that the NUS learns realistic user behaviour from a corpus of recorded dialogues such that it can be used to optimise the policy of the dialogue manager of a spoken dialogue system. The NUS was compared to the Agenda-Based User Simulator by evaluating policies trained with these user simulators. The trained policies were compared both by testing them with simulated users and also with real users. The NUS excelled on both evaluation tasks.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-52d54da483cbba4a55f45da493c67f58dc330887af264811d35fa5857989e3fb

Passage ID: `qasper-passage-v1-52d54da483cbba4a55f45da493c67f58dc330887af264811d35fa5857989e3fb`; retrieval score: 3.6501533324870037.

Word count: 289.

```text
Table TABREF18 shows the results of the cross-model evaluation after 4000 training dialogues. The policies trained with the NUS achieved an average success rate (SR) of 94.0% and of 96.6% when tested on the ABUS and the NUS, respectively. By comparison, the policies trained with the ABUS achieved average SRs of 99.5% and 45.5% respectively. Thus, training with the NUS leads to policies that can perform well on both USs, which is not the case for training with the ABUS. Furthermore, the best SRs when tested on the ABUS are similar at 99.9% (ABUS) and 99.8% (NUS). When tested on the NUS the best SRs were 71.5% (ABUS) and 98.0% (NUS). This shows that the behaviour of the Neural User Simulator is realistic and diverse enough to train policies that can also perform very well on the Agenda-Based User Simulator.

Of the five policies, for each US, the policy performing best on the NUS was not the best performing policy on the ABUS. This could indicate that the policy “overfits” to a particular user simulator. Overfitting usually manifests itself in worse results as the model is trained for longer. Five policies trained on each US for only 1000 dialogues were also evaluated, the results of which can be seen in Table TABREF19 . After training for 1000 dialogues, the average SR of the policies trained on the NUS when tested on the ABUS was 97.3% in comparison to 94.0% after 4000 dialogues. This behaviour was observed for all five seeds, which indicates that the policy indeed overfits to the NUS. For the policies trained with the ABUS this was not observed. This could indicate that the policy can learn to exploit some of the shortcomings of the trained NUS.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1370.

Fully covered answer annotations: c1ed3e2a6e21d189790e8b23f0edc5422b51ec52.

Missing evidence by answer annotation:

```text
{
  "c1ed3e2a6e21d189790e8b23f0edc5422b51ec52": {
    "unresolved_evidence": [],
    "paragraphs": {}
  },
  "e89a4ff03c55b1be6dd8bff517f6f3f9822e4235": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1805.06966:7:2": [
        [
          0,
          659
        ]
      ]
    }
  }
}
```

## Question: 21a96b328b43a568f9ba74cbc6d4689dbc4a3d7b

### Question ID and text

Question ID: `21a96b328b43a568f9ba74cbc6d4689dbc4a3d7b`; paper ID: `1611.00514`.

```text
Do they single out a validation set from the fixed SRE training set?
```

### Answers

#### Answer: c098177da67025e6442b6e3416945868669f695d

```text
{"evidence": ["Since the introduction of i-vectors in BIBREF0 , the speaker recognition community has seen a significant increase in recognition performance. i-Vectors are low-dimensional representations of Baum-Welch statistics obtained with respect to a GMM, referred to as universal background model (UBM), in a single subspace which includes all characteristics of speaker and inter-session variability, named total variability matrix BIBREF0 . We trained on each acoustic feature a full covariance, gender-independent UBM model with 2048 Gaussians followed by a 600-dimensional i-vector extractor to establish our MFCC- and PLP-based i-vector systems. The unlabeled set of development data was used in the training of both the UBM and the i-vector extractor. The open-source Kaldi software has been used for all these processing steps BIBREF12 ."], "extractive_spans": [], "free_form_answer": "", "highlighted_evidence": [" The unlabeled set of development data was used in the training of both the UBM and the i-vector extractor."], "unanswerable": false, "yes_no": false}
```

Evidence location: `1611.00514:5:0`

```text
Since the introduction of i-vectors in BIBREF0 , the speaker recognition community has seen a significant increase in recognition performance. i-Vectors are low-dimensional representations of Baum-Welch statistics obtained with respect to a GMM, referred to as universal background model (UBM), in a single subspace which includes all characteristics of speaker and inter-session variability, named total variability matrix BIBREF0 . We trained on each acoustic feature a full covariance, gender-independent UBM model with 2048 Gaussians followed by a 600-dimensional i-vector extractor to establish our MFCC- and PLP-based i-vector systems. The unlabeled set of development data was used in the training of both the UBM and the i-vector extractor. The open-source Kaldi software has been used for all these processing steps BIBREF12 .
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-bf33b8c17c1aaa31fcebc82a15b8d7807c4b6c4a4a1c8b67ee52397bb7311404

Passage ID: `qasper-passage-v1-bf33b8c17c1aaa31fcebc82a15b8d7807c4b6c4a4a1c8b67ee52397bb7311404`; retrieval score: 9.07067284633237.

Word count: 119.

```text
The fixed training condition is used to build our speaker recognition system. Only conversational telephone speech data from datasets released through the linguistic data consortium (LDC) have been used, including NIST SRE 2004-2010 and the Switchboard corpora (Switchboard Cellular Parts I and II, Switchboard2 Phase I,II and III) for different steps of system training. A more detailed description of the data used in the system training is presented in Table TABREF1 . We have also included the unlabelled set of 2472 telephone calls from both minor (Cebuano and Mandarin) and major (Tagalog and Cantonese) languages provided by NIST in the system training. We will indicate when and how we used this set in the training in the following sections.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-3b750f9690a3843d769392d09fc652258316e8a48bd54afd36b1bb52198a71ae

Passage ID: `qasper-passage-v1-3b750f9690a3843d769392d09fc652258316e8a48bd54afd36b1bb52198a71ae`; retrieval score: 7.250260244403019.

Word count: 230.

```text
This section reports on the CPU execution time (single threaded), and the amount of memory used to process a single trial, which includes the time for creating models from the enrolment data and the time needed for processing the test segments. The analysis was performed on an Intel(R) Xeon(R) CPU E5-2670 2.60GHz. The results are shown in Table TABREF27 . We used the time command in Unix to report these results. The user time is the actual CPU time used in executing the process (single thread). The real time is the wall clock time (the elapsed time including time slices used by other processes and the time the process spends blocked). The system time is also the amount of CPU time spent in the kernel within the process. We have also reported the memory allocated for each stage of execution. The most computationally intensive stage is the extraction of i-vectors (both MFCC- and PLP-based i-vectors), which also depends on the duration of the segments. For enrolment, we have reported the time required to extract a model from a segment with a duration of 140 seconds and speech duration of 60 seconds. The time and memory required for front-end processing are negligible compared to the i-vector extraction stage, since they only include matrix operations. The time required for our SAD is also reported which increases linearly with the duration of segment.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-870a7e721401ac2da7400f558b0afe235492ec6f91a5484283d7debf977064d9

Passage ID: `qasper-passage-v1-870a7e721401ac2da7400f558b0afe235492ec6f91a5484283d7debf977064d9`; retrieval score: 5.998247161561475.

Word count: 208.

```text
Since the introduction of i-vectors in BIBREF0 , the speaker recognition community has seen a significant increase in recognition performance. i-Vectors are low-dimensional representations of Baum-Welch statistics obtained with respect to a GMM, referred to as universal background model (UBM), in a single subspace which includes all characteristics of speaker and inter-session variability, named total variability matrix BIBREF0 . We trained on each acoustic feature a full covariance, gender-independent UBM model with 2048 Gaussians followed by a 600-dimensional i-vector extractor to establish our MFCC- and PLP-based i-vector systems. The unlabeled set of development data was used in the training of both the UBM and the i-vector extractor. The open-source Kaldi software has been used for all these processing steps BIBREF12 .

It has been shown that successive acoustic observation vectors tend to be highly correlated. This may be problematic for maximum a posteriori (MAP) estimation of i-vectors. To investigating this issue, scaling the zero and first order Baum-Welch statistics before presenting them to the i-vector extractor has been proposed. It turns out that a scale factor of 0.33 gives a slight edge, resulting in a better decision cost function BIBREF13 . This scaling factor has been performed in training the i-vector extractor as well as in the testing.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1611.00514:5:0` | full | 0:835 |

#### Rank 4: qasper-passage-v1-437d74f192aae206a7d39e3858235fad0955fdf4c387b519d7367c627f972f9d

Passage ID: `qasper-passage-v1-437d74f192aae206a7d39e3858235fad0955fdf4c387b519d7367c627f972f9d`; retrieval score: 5.776473824118878.

Word count: 329.

```text
Compared to previous years, the 2016 NIST speaker recognition evaluation (SRE) marked a major shift from English towards Austronesian and Chinese languages. The task like previous years is to perform speaker detection with the focus on telephone speech data recorded over a variety of handset types. The main challenges introduced in this evaluation are duration and language variability. The potential variation of languages addressed in this evaluation, recording environment, and variability of test segments duration influenced the design of our system. Our goal was to utilize recent advances in language normalization, domain adaptation, speech activity detection and session compensation techniques to mitigate the adverse bias introduced in this year's evaluation.

Over recent years, the i-vector representation of speech segments has been widely used by state-of-the-art speaker recognition systems BIBREF0 . The speaker recognition technology based on i-vectors currently dominates the research field due to its performance, low computational cost and the compatibility of i-vectors with machine learning techniques. This dominance is reflected by the recent NIST i-vector machine learning challenge BIBREF1 which was designed to find the most promising algorithmic approaches to speaker recognition specifically on the basis of i-vectors BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 . The outstanding ability of DNN for frame alignment which has achieved remarkable performance in text-independent speaker recognition for English data BIBREF6 , BIBREF7 , failed to provide even comparable recognition performance to the traditional GMM. Therefore, we concentrated on the cepstral based GMM/i-vector system.

We outline in this paper the Intelligent Voice system, techniques and results obtained on the SRE 2016 development set that will mirror the evaluation condition as well as the timing report. Section SECREF2 describes the data used for the system training. The front-end and back-end processing of the system are presented in Sections SECREF3 and SECREF4 respectively. In Section SECREF5 , we describe experimental evaluation of the system on the SRE 2016 development set. Finally, we present a timing analysis of the system in Section SECREF6 .
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-9c85dcc531e419ebe7896da5b45133725e9bd125c2d615d5721080cc41f82b81

Passage ID: `qasper-passage-v1-9c85dcc531e419ebe7896da5b45133725e9bd125c2d615d5721080cc41f82b81`; retrieval score: 5.41053993968467.

Word count: 275.

```text
Probabilistic Linear Discriminant Analysis (PLDA) provides a powerful mechanism to distinguish between-speaker variability, separating sources which characterizes speaker information, from all other sources of undesired variability that characterize distortions. Since i-vectors are assumed to be generated by some generative model, we can break it down into statistically independent speaker- and session-components with Gaussian distributions BIBREF18 , BIBREF19 . Although it has been shown that their distribution follow Student’s INLINEFORM0 rather than Gaussian BIBREF19 distributions, length normalizing the entire set of i-vectors as a pre-processing step can approximately Gaussianize their distributions BIBREF18 and as a result improve the performance of Gaussian PLDA to that of heavy-tailed PLDA BIBREF19 . A standard Gaussian PLDA assumes that an i-vector INLINEFORM1 , is modelled according to DISPLAYFORM0

where, INLINEFORM0 is the mean of i-vectors, the columns of matrix INLINEFORM1 contains the basis for the between-speaker subspace, the latent identity variable INLINEFORM2 denotes the speaker factor that represents the identity of the speaker and the residual INLINEFORM3 which is normally distributed with zero mean and full covariance matrix INLINEFORM4 , represents within-speaker variability.

For each acoustic feature we have trained two PLDA models. The first out-domain PLDA ( INLINEFORM0 , INLINEFORM1 ) is trained using the training set presented in Table TABREF1 , and the second in-domain PLDA ( INLINEFORM2 , INLINEFORM3 ) was trained using the unlabelled development set. Our efforts to cluster the development set (e.g using the out-domain PLDA) was not very successful as it sounds that almost all of them are uttered by different speakers. Therefore, each i-vector was considered to be uttered by one speaker. We also set the number of speaker factors to 200.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1161.

Fully covered answer annotations: c098177da67025e6442b6e3416945868669f695d.

Missing evidence by answer annotation:

```text
{
  "c098177da67025e6442b6e3416945868669f695d": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: eac042734f76e787cb98ba3d0c13a916a49bdfb3

### Question ID and text

Question ID: `eac042734f76e787cb98ba3d0c13a916a49bdfb3`; paper ID: `1601.04012`.

```text
Which datasets are used in this work?
```

### Answers

#### Answer: d7488554bc89783a43fe78b62c5890a9fc7b8d4a

```text
{"evidence": ["There have been several workshops on biomedical natural language processing. We focus on the BioNLP Shared Tasks in recent years that had competitions on event extraction. There have been three BioNLP Shared Task competitions so far: 2009, 2011, and 2013. The BioNLP 2009 Shared Task BIBREF195 was based on the GENIA corpus BIBREF196 which contains PubMed abstracts of articles on transcription factors in human blood cells. There was a second BioNLP Shared Task competition organized in 2011 to measure the advances in approaches and associated results BIBREF197 . The third BioNLP ST was held in 2013. We discuss some notable systems from BioNLP ST 2011 and 2013."], "extractive_spans": ["GENIA corpus"], "free_form_answer": "", "highlighted_evidence": ["The BioNLP 2009 Shared Task BIBREF195 was based on the GENIA corpus BIBREF196 which contains PubMed abstracts of articles on transcription factors in human blood cells."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1601.04012:21:1`

```text
There have been several workshops on biomedical natural language processing. We focus on the BioNLP Shared Tasks in recent years that had competitions on event extraction. There have been three BioNLP Shared Task competitions so far: 2009, 2011, and 2013. The BioNLP 2009 Shared Task BIBREF195 was based on the GENIA corpus BIBREF196 which contains PubMed abstracts of articles on transcription factors in human blood cells. There was a second BioNLP Shared Task competition organized in 2011 to measure the advances in approaches and associated results BIBREF197 . The third BioNLP ST was held in 2013. We discuss some notable systems from BioNLP ST 2011 and 2013.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-e74aa7129ce31ee679170c907266a19bf0651d1d7c91616055962b4430c34e99

Passage ID: `qasper-passage-v1-e74aa7129ce31ee679170c907266a19bf0651d1d7c91616055962b4430c34e99`; retrieval score: 6.896057248576551.

Word count: 400.

```text
TimeML is a rich specification language for event and temporal expressions in natural language text. In the TimeML BIBREF119 , BIBREF120 annotation scheme, an event is a general term for situations that happen or occur. Events can be punctual or momentary, or last for a period of time. Events in TimeML format may also include predicates describing states or circumstances in which something holds true. Only those states that participate in an opposition structure, as discussed in Subsection UID42 , are annotated. In general, an event can be expressed in terms of verbs, nominalizations, adjectives, predicative clauses, or prepositional phrases. TimeML allows an event, annotated with the EVENT tag, to be one of seven types: occurrence, state, report, i-action, i-state, aspectual and perception. The first five are special cases. The last two, Occurrence and State are used for general cases that do not fall in the special ones.

Reporting: A reporting event describes an action declaring something, narrating an event, informing about a situation, and so on. Some verbs which express this kind of event are say, report, tell, explain, and state. An example sentence with the verb say is Punongbayan said that the 4,795-foot-high volcano was spewing gases up to 1,800 degrees.

I-Action: I stands for intensional. According to the TimeML annotation guidelines, an i-action is a dynamic event that takes an event-denoting argument, which must be explicitly present in the text. Examples of verbs that are used to express i-actions include attempt, try, promise and offer. An example sentence with the verb try is Companies such as Microsoft or a combined worldcom MCI are trying to monopolize Internet access.

I-State: I-State stands for intensional state. Like an I-Action, an I-State event takes an argument that expresses an event. Unlike an I-Action, the I-State class is used for events which are states. An example sentence that uses the verb believe is We believe that his words cannot distract the world from the facts of Iraqi aggression. Other verbs used to express i-states include intend, want, and think.

Aspectual: An aspectual predicate takes an event as an argument, and points to a part of the temporal structure of the event. Such a part may be the beginning, the middle or the end of an event. Verbs such as begin, finish and continue are such aspectual predicates. An example sentence with the verb begin is All non-essential personnel should begin evacuating
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-5269c6eeeae9f432b6b0521f055d30cd2e73dbdf6995e39c7b3bd8e4203ca3a3

Passage ID: `qasper-passage-v1-5269c6eeeae9f432b6b0521f055d30cd2e73dbdf6995e39c7b3bd8e4203ca3a3`; retrieval score: 6.893983553027447.

Word count: 400.

```text
event triggers or event phrases or just events) are extracted using supervised learning. BIBREF228 annotated 1,000 tweets with event phrases, following guidelines for annotation of EVENT tags in Timebank BIBREF119 . The system recognizes event triggers as a sequence labeling task using Conditional Random Fields BIBREF147 . It uses a contextual dictionary, orthographic features, features based on the Twitter-tuned POS tagger, and dictionaries of event terms gathered from WordNet BIBREF121 . Once a large number of events have been extracted by this CRF learner, TwiCal categorizes these events into types using an unsupervised approach based on latent variable models, inspired by work on modeling selectional preferences BIBREF230 , BIBREF231 , BIBREF232 , BIBREF233 and unsupervised information extraction BIBREF234 , BIBREF225 , BIBREF235 . This automatic discovery of event types is similar to topic modeling, where one automatically identifies the extant topics in a corpus of text documents. The automatically discovered types (topics) are quickly inspected by a human effort to filter out incoherent ones, and the rest are annotated with informative labels. Examples of event types discovered along with top event phrases and top entities are given in Table 12 . The resulting set of types are applied to categorize millions of extracted events without the use of any manually annotated examples. For inference, the system uses collapsed Gibbs sampling BIBREF236 and prediction is performed using a streaming approach to inference BIBREF237 . To resolve temporal expressions, TwiCal uses TempEx BIBREF238 , which takes as input a reference date, some text and POS tags, and marks temporal expressions with unambiguous calendar references. Finally, the system measures the strength of association between each named entity and date based on the number of tweets they co-occur in, in order to determine if the event is significant. Examples of events extracted by TwiCal are given in Table 13 . Each event is a 4-tuple including a named entity, event phrase, calendar date and event type.

The TwiCal system describe above used topic modeling using latent variables as one of the several computational components; it is used to capture events captured using supervised learning into types or topics. BIBREF239 point out some drawbacks of using such an approach. The main problem is that frequently the result generated by Latent Dirichlet Analysis (LDA) is difficult to interpret because it simply gives a list of words associate with the topic. For example, when BIBREF239 attempt to
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-3c7dc6ae61906777add5cadf750377d76dea65b73d09b6f576e73777069ccf25

Passage ID: `qasper-passage-v1-3c7dc6ae61906777add5cadf750377d76dea65b73d09b6f576e73777069ccf25`; retrieval score: 6.731586492426265.

Word count: 400.

```text
Many authors in linguistics have delved deeper into the nature of event classes and have tried to come up with features or characteristics that can be used to identify whether something (verb or a clause) belongs to a particular event class or not. These features or characteristics are necessary to describe the structure of events in a theoretical sense. Description of event structure usually refers to the actual words used (lexical features or characteristics) and also the structure of clause or sentence (syntactic features or characteristics). Identification of such features may be described as finding parameters of event types or parameterization of event types.

A lot of the work on parameterization of event types/classes use the classes espoused by Vendler. These include BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 , BIBREF13 , BIBREF14 , BIBREF15 and others. We will only briefly touch upon such work in this paper. Our objective is to impress upon the reader that identification of features of event classes is considered an important task by linguists.

For example, BIBREF9 describes Vendler's classes with two binary features or parameters: continuousness: whether an event has duration, and boundedness: whether an event has a (natural) terminal point or endpoint. Using these two features, the four Vendler classes can be parameterized as follows.

: -bounded, -continuous

: -bounded, +continuous

: +bounded, -continuous

: +bounded, +continuous

BIBREF12 , BIBREF13 introduce the notion of countability while discussing event classes. This is similar to the mass-count opposition in nouns. Terminating events can be counted, but non-terminating processes cannot. Hoeksema introduces two binary features: count and duration to obtain Vendler's classes as seen below. The feature duration refers to whether the event takes place over time.

: -count, -duration

: -count, +duration

: +count, -duration

: +count, +duration

BIBREF11 refines Vendler's classes by adding a class much like Smith's semelfactives BIBREF5 . He suggests that, in addition to states, there are four event types: culmination, culminated process, point, and process. He uses two binary features or parameters: consequence identifying termination or culmination, and atomic or non-atomic (which Moens called extended). Atomic is also called momentous or pointed. Moen's classification is given below, along with the features and examples.

: +consequence, +atomic (examples: recognize, win the race)

: +consequence, -atomic (examples: build a house)

: -consequence, +atomic (example: hiccup, tap, wink)

: -consequence, -atomic (example: run, swim, play the piano)

: (examples: understand, love, resemble)
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-87bd64f95f18ec7f8c30d1df21858249c7e67dc363581d5b9ea3e09609c567aa

Passage ID: `qasper-passage-v1-87bd64f95f18ec7f8c30d1df21858249c7e67dc363581d5b9ea3e09609c567aa`; retrieval score: 6.444876039497951.

Word count: 400.

```text
contest, generalized in three ways: text types, event types, and subject domains. The 2011 event-related tasks were arranged in four tracks: GENIA task (GE) BIBREF197 , Epigenetics and Post-translational Modifications (EPI) BIBREF198 , Infectious Diseases (ID) BIBREF199 , and the Bacteria Track BIBREF200 , BIBREF201 .

Of the four event-related shared tasks in BioNLP 2011, the first three were related to event extraction. The Genia task was focused on the domain of transcription factors in human blood cell. Trascription is a complex but just the first step in the process in which the instructions contained in the DNA in the nucleus of a cell are used to produce proteins that control most life processes. Transcription factors are proteins that control the transcription process. The EPI task was focused on events related to epigenetics, dealing with protein and DNA modifications, with 14 new event types, including major protein modification types and their reverse reactions. Epigenesis refers to the development of a plant or animal from a seed, spore or egg, through a sequence of steps in which cells differentiate and organs form. The EPI task was designed toward pathway extraction and curation of domain databases BIBREF202 , BIBREF203 . A biological pathway refers to a sequence of actions among molecules in a cell that leads to a certain product or a change in the cell. The ID task was focused on extraction of events relevant to biomolecular mechanisms of infectious diseases from full length publications. Tasks other than ID focused on abstracts only.

In this paper, we discuss the systems and approaches for only the 2011 GE Task. This is because several of the winning systems for the GE Task did well in the other two relevant tasks as well. The Genia Task is described in Table 7 . The table shows for each event type, the primary and secondary arguments to be extracted. For example, a phosphorylation event is primarily extracted with the protein to be phosphorylated, which is the addition of a phosphate group to a protein or other organic molecule. As secondary information, the specific site to be phosphorylated may be extracted. From a computational viewpoint, the event types represent different levels of complexity. When only primary arguments are considered, the first five event types in Table 7 are classified as simple events, requiring only unary arguments. The binding and regulation types are more complex. Binding requires the
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-ab419ea84dd807906935fcd5bc7acfb640a5e934d468731c00c6aeef919d98ec

Passage ID: `qasper-passage-v1-ab419ea84dd807906935fcd5bc7acfb640a5e934d468731c00c6aeef919d98ec`; retrieval score: 6.436471043380034.

Word count: 357.

```text
signal auto-correlations. The remaining words are then clustered to form events with a modularity-based graph partitioning technique, which uses a scalable eigenvalue algorithm. It detects events by grouping sets of words with similar patterns of burst. To cluster, similarities between words need to be computed. It does so by using cross correlation, which is a common measure of similarity between two signals BIBREF244 . Cross correlation is a pairwise operation. Cross correlation values among a number of signals can be represented in terms of a correlation matrix $\mathcal {M}$ , which happens to be a symmetric sparse matrix of adjacent similarities. With this graph setup, event detection can be formulated as a graph partitioning problem, i.e., to cut the graph into subgraphs. Each subgraph corresponds to an event, which contains a set of words with high cross correlation, and also that the cross correlation between words in different subgraphs are low. The quality of such partitioning is measures using a metric called modularity BIBREF245 , BIBREF246 . The modularity of a graph is defined as the sum of weights of all the edges that fall within subgraphs (after partitioning) subtracted by the expected edge weight sum if the edges were placed at random. The main computation task in this component is finding the largest eigenvalue and corresponding eigenvector, of the sparse symmetric modularity matrix. This is solved using power iteration, which is able to scale up with the increase in the number of words in the tweets BIBREF247 . EDCoW requires each individual event to contain at least two words. To differentiate big events from trivial ones, EDCoW quantifies the events' significance, which depends on two factors, the number of words and cross-correlation among the words related to the event. To make EDCoW work with TwiCal to see if it improves performance, the topic detection module will have to be replaced. EDCoW associates fewer words to topics because it filters words away before associating with a topic. Table 15 gives a few event words obtained by EDCoW and the corresponding event description. Please note that the event description was created by the authors and not the system.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1957.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "d7488554bc89783a43fe78b62c5890a9fc7b8d4a": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1601.04012:21:1": [
        [
          0,
          665
        ]
      ]
    }
  }
}
```

## Question: 79cfd1b82c72d18e2279792c66a042c0e9dfa6b7

### Question ID and text

Question ID: `79cfd1b82c72d18e2279792c66a042c0e9dfa6b7`; paper ID: `2004.02083`.

```text
What are the architectures used for the three tasks?
```

### Answers

#### Answer: 4d88a72e4cfb4a6f1b643127dadc9d86e1c212ac

```text
{"evidence": ["Morphological inflection has been thoroughly studied in monolingual high resource settings, especially through the recent SIGMORPHON challenges BIBREF8, BIBREF9, BIBREF10, with the latest iteration focusing more on low-resource settings, utilizing cross-lingual transfer BIBREF11. We use the guidelines of the state-of-the-art approach of BIBREF12 that achieved the highest inflection accuracy in the latest SIGMORPHON 2019 morphological inflection shared task. Our models are implemented in DyNet BIBREF13.", "Morphological analysis is the task of creating a morphosyntactic description for a given word. It can be framed in a context-agnostic manner (as in our case) or within a given context, as for instance for the SIGMORPHON 2019 second shared task BIBREF11. We trained an encoder-decoder model that receives the form as character-level input, encodes it with a BiLSTM encoder, and then an attention enhanced decoder BIBREF14 outputs the corresponding sequence of morphological tags, implemented in DyNet. The baseline results are shown in Table . The exact-match accuracy of 67% is lower than the average accuracy that context-aware systems can achieve, and it highlights the challenge that the complexity of the tonal system of SJQ Chatino can pose.", "Lemmatization is the task of retrieving the underlying lemma from which an inflected form was derived. Although in some languages the lemma is distinct from all forms, in SJQ Chatino the lemma is defined as the completive third-person singular form. As a computational task, lemmatization entails producing the lemma given an inflected form (and possibly, given a set of morphological tags describing the input form). Popular approaches tackle it as a character-level edit sequence generation task BIBREF15, or as a character-level sequence-to-sequence task BIBREF16. For our baseline lemmatization systems we follow the latter approach. We trained a character level encoder-decoder model, similar to the above-mentioned inflection system, implemented in DyNet."], "extractive_spans": ["DyNet"], "free_form_answer": "", "highlighted_evidence": ["We use the guidelines of the state-of-the-art approach of BIBREF12 that achieved the highest inflection accuracy in the latest SIGMORPHON 2019 morphological inflection shared task. Our models are implemented in DyNet BIBREF13.", "We trained an encoder-decoder model that receives the form as character-level input, encodes it with a BiLSTM encoder, and then an attention enhanced decoder BIBREF14 outputs the corresponding sequence of morphological tags, implemented in DyNet.", "We trained a character level encoder-decoder model, similar to the above-mentioned inflection system, implemented in DyNet."], "unanswerable": false, "yes_no": null}
```

Evidence location: `2004.02083:5:1`

```text
Morphological inflection has been thoroughly studied in monolingual high resource settings, especially through the recent SIGMORPHON challenges BIBREF8, BIBREF9, BIBREF10, with the latest iteration focusing more on low-resource settings, utilizing cross-lingual transfer BIBREF11. We use the guidelines of the state-of-the-art approach of BIBREF12 that achieved the highest inflection accuracy in the latest SIGMORPHON 2019 morphological inflection shared task. Our models are implemented in DyNet BIBREF13.
```

Evidence location: `2004.02083:6:0`

```text
Morphological analysis is the task of creating a morphosyntactic description for a given word. It can be framed in a context-agnostic manner (as in our case) or within a given context, as for instance for the SIGMORPHON 2019 second shared task BIBREF11. We trained an encoder-decoder model that receives the form as character-level input, encodes it with a BiLSTM encoder, and then an attention enhanced decoder BIBREF14 outputs the corresponding sequence of morphological tags, implemented in DyNet. The baseline results are shown in Table . The exact-match accuracy of 67% is lower than the average accuracy that context-aware systems can achieve, and it highlights the challenge that the complexity of the tonal system of SJQ Chatino can pose.
```

Evidence location: `2004.02083:7:0`

```text
Lemmatization is the task of retrieving the underlying lemma from which an inflected form was derived. Although in some languages the lemma is distinct from all forms, in SJQ Chatino the lemma is defined as the completive third-person singular form. As a computational task, lemmatization entails producing the lemma given an inflected form (and possibly, given a set of morphological tags describing the input form). Popular approaches tackle it as a character-level edit sequence generation task BIBREF15, or as a character-level sequence-to-sequence task BIBREF16. For our baseline lemmatization systems we follow the latter approach. We trained a character level encoder-decoder model, similar to the above-mentioned inflection system, implemented in DyNet.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-67b6876242ccc6f5e7b4c6942e78b0a8936e93722c36cd838b24d69db0a77cf3

Passage ID: `qasper-passage-v1-67b6876242ccc6f5e7b4c6942e78b0a8936e93722c36cd838b24d69db0a77cf3`; retrieval score: 5.393315723237432.

Word count: 371.

```text
The recent years have seen unprecedented forward steps for Natural Language Processing (NLP) over almost every NLP subtask, relying on the advent of large data collections that can be leveraged to train deep neural networks. However, this progress has solely been observed in languages with significant data resources, while low-resource languages are left behind.

The situation for endangered languages is usually even worse, as the focus of the scientific community mostly relies in language documentation. The typical endangered language documentation process typically includes the creation of language resources in the form of word lists, audio and video recordings, notes, or grammar fragments, with the created resources then stored into large online linguistics archives. This process is often hindered by the so-called Transcription Bottleneck, but recent advances BIBREF0, BIBREF1 provide promising directions towards a solution for this issue.

However, language documentation and linguistic description, although extremely important itself, does not meaningfully contribute to language conservation, which aims to ensure that the language stays in use. We believe that a major avenue towards continual language use is by further creating language technologies for endangered languages, essentially elevating them to the same level as high-resource, economically or politically stronger languages.

The majority of the world's languages are categorized as synthetic, meaning that they have rich morphology, be it fusional, agglutinative, polysynthetic, or a mixture thereof. As Natural Language Processing (NLP) keeps expanding its frontiers to encompass more and more languages, modeling of the grammatical functions that guide language generation is of utmost importance. It follows, then, that the next crucial step for expanding NLP research on endangered languages is creating benchmarks for standard NLP tasks in such languages.

With this work we take a small first step towards this direction. We present a resource that allows for benchmarking two NLP tasks in San Juan Quiahije Chatino, an endangered language spoken in southern Mexico: morphological analysis and morphological inflection, with a focus on the verb morphology of the language.

We first briefly discuss the Chatino language and the intricacies of its verb morphology (§SECREF2), then describe the resource (§SECREF3), and finally present baseline results on both the morphological analysis and the inflection tasks using state-of-the-art neural models (§SECREF4). We make our resource publicly available online.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-481e457b7316c2b58e8e36ca7085a6fa4218d57c21e114a7bec871c09c2b34f6

Passage ID: `qasper-passage-v1-481e457b7316c2b58e8e36ca7085a6fa4218d57c21e114a7bec871c09c2b34f6`; retrieval score: 5.390928746848506.

Word count: 84.

```text
Chatino is a group of languages spoken in Oaxaca, Mexico. Together with the Zapotec language group, the Chatino languages form the Zapotecan branch of the Otomanguean language family. There are three main Chatino languages: Zenzontepec Chatino (ZEN, ISO 639-2 code czn), Tataltepec Chatino (TAT, cta), and Eastern Chatino (ISO 639-2 ctp, cya, ctz, and cly) (E.Cruz 2011 and Campbell 2011). San Juan Quiahije Chatino (SJQ), the language of the focus of this study, belongs to Eastern Chatino, and is used by about 3000 speakers.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-e178dff810fee3fac5f23a8c2add3104cd474738d5b967e1b84c8ca7d50ef97b

Passage ID: `qasper-passage-v1-e178dff810fee3fac5f23a8c2add3104cd474738d5b967e1b84c8ca7d50ef97b`; retrieval score: 4.0171888875592625.

Word count: 99.

```text
Eastern Chatino languages , including SJQ Chatino, are intensively tonal BIBREF2, BIBREF3. Tones mark both lexical and grammatical distinctions in Eastern Chatino languages.

In SJQ Chatino, there are eleven tones. Three different systems for representing tone distinctions are employed in the literature: the S-H-M-L system of BIBREF2; the numeral system of BIBREF4; and the alphabetic system of BIBREF3. The correspondences among these three systems are given in Table . For present purposes, we will use numeral representations of the second sort. The number 1 represents a high pitch, 4 represents a low pitch, and double digits represent contour tones.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-f242c5b422135f17a90f006c655fc0b850adceb56e44715d622c64cbb1e53cda

Passage ID: `qasper-passage-v1-f242c5b422135f17a90f006c655fc0b850adceb56e44715d622c64cbb1e53cda`; retrieval score: 3.607478836451757.

Word count: 244.

```text
We provide a hand-curated collection of complete inflection tables for 198 lemmata. The morphological tags follow the guidelines of the UniMorph schema BIBREF6, BIBREF7, in order to allow for the potential of cross-lingual transfer learning, and they are tagged with respect to:

Person: first (1), second (2), and third (3)

Number: singular (SG) ad plural (PL)

Inclusivity (only applicable to first person plural verbs: inclusive (INCL) and exclusive (EXCL)

Aspect/mood: completive (CPL), progressive (PROG), potential (POT), and habitual (HAB).

Two examples of complete inflection tables for the verbs ndyu2 `fell from above' and lyu1 `fall' are shown in Table . Note how the first verb has the same PN triplet for all four aspect/mood categories, while the second paradigm is more representative in that it involves three different triplets (one for the completive, another for the progressive, and another for the habitual/potential). This variety is at the core of why the SJQ verb morphology is particularly interesting, and a challenging testcase for modern NLP systems.

In total, we end up with 4716 groupings (triplets) of a lemma, a tag-set, and a form; we split these groupings randomly into a training set (3774 groupings), a development set (471 groupings), and test set (471 groupings). Basic statistics of the corpus are outlined in Table 1 . Compared to all the other languages from the Unimorph project, this puts SJQ Chatino in the low- to mid-resource category, but nonetheless it is more than enough for benchmarking purposes.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-d8aa7bce006d9bc5bbe7604166f174f660a21f71d69ce9137b45689d20b8f1a5

Passage ID: `qasper-passage-v1-d8aa7bce006d9bc5bbe7604166f174f660a21f71d69ce9137b45689d20b8f1a5`; retrieval score: 2.9448456967775973.

Word count: 118.

```text
Morphological analysis is the task of creating a morphosyntactic description for a given word. It can be framed in a context-agnostic manner (as in our case) or within a given context, as for instance for the SIGMORPHON 2019 second shared task BIBREF11. We trained an encoder-decoder model that receives the form as character-level input, encodes it with a BiLSTM encoder, and then an attention enhanced decoder BIBREF14 outputs the corresponding sequence of morphological tags, implemented in DyNet. The baseline results are shown in Table . The exact-match accuracy of 67% is lower than the average accuracy that context-aware systems can achieve, and it highlights the challenge that the complexity of the tonal system of SJQ Chatino can pose.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2004.02083:6:0` | full | 0:746 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 916.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "4d88a72e4cfb4a6f1b643127dadc9d86e1c212ac": {
    "unresolved_evidence": [],
    "paragraphs": {
      "2004.02083:5:1": [
        [
          0,
          507
        ]
      ],
      "2004.02083:7:0": [
        [
          0,
          761
        ]
      ]
    }
  }
}
```
