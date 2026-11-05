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

#### Rank 1: qasper-passage-v1-697daaf33797b5e00f7859d12952e162f740b8944cbc0ccf26116deeb396aba3

Passage ID: `qasper-passage-v1-697daaf33797b5e00f7859d12952e162f740b8944cbc0ccf26116deeb396aba3`; retrieval score: 6.726270391147626.

Word count: 150.

```text
Methods for machine translations have been studied for years, and at the same time algorithms to generate word embeddings are becoming more and more accurate. Still, there is a lot of research aiming at unifying word embeddings across multiple languages. In this experience we try a technique for machine translation that relates word embeddings between two different languages. Based on the literature we found that it is possible to infer missing dictionary entries using distributed representations of words and phrases. One way of doing it is to create a linear mapping between the two vector spaces of two different languages. In order to achieve this, we first built two dictionaries of the two different languages. Next, we learned a function that projects the first vector space to the second one. In this way, we are able to translate every word belonging to the first language into the second one. Once
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-a1310dca06fe4c2813d6c7f4a2c305fcc84aaa85f9269f133f312cc7a32214a8

Passage ID: `qasper-passage-v1-a1310dca06fe4c2813d6c7f4a2c305fcc84aaa85f9269f133f312cc7a32214a8`; retrieval score: 6.073372539333415.

Word count: 103.

```text
In recent years, various models for learning cross-lingual representations have been proposed. Two main broad categories with some related papers are identified here:

Monolingual mapping: In this approach, models are trained using word embeddings from a monolingual corpora. Then, an objective function is used to minimize a linear mapping that enable them to map unknown words from the source language to the target language.

Pseudo-cross-lingual: In this case we create a pseudo-cross-lingual corpus by mixing contexts of different languages. We then train an off-the-shelf word embedding model on the created corpus. Ideally the cross-lingual contexts allow the learned representations to capture cross-lingual relations.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-3ea9aafcb8197b5a31cc17930079171aa89833dce2f553773fa0711981e35b73

Passage ID: `qasper-passage-v1-3ea9aafcb8197b5a31cc17930079171aa89833dce2f553773fa0711981e35b73`; retrieval score: 5.673576075443647.

Word count: 131.

```text
It was recently shown that the distributed representations of words capture surprisingly many linguistic regularities, and that there are many types of similarities among words that can be expressed as linear translations (Mikolov et al., 2013c). In the Skip-gram model, the training objective is to learn word vector representations that are good at predicting its context in the same sentence (Mikolov et al., 2013a). The objective function that skip gram tries to minimize is the following:

Where N represents the total number of words in a sentence, P the probability of a word at the position i+j to belong to the sentence, with respect to the word i. Ideally, by using this approach we will be able to provide non-trivial translations that will be related to the context of a word.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-01cf5c93eeffecc632320221fdea13376c353bbcdc59d2edcf87420c98d6ee7a

Passage ID: `qasper-passage-v1-01cf5c93eeffecc632320221fdea13376c353bbcdc59d2edcf87420c98d6ee7a`; retrieval score: 4.047008941228972.

Word count: 133.

```text
of the two different languages. Next, we learned a function that projects the first vector space to the second one. In this way, we are able to translate every word belonging to the first language into the second one. Once we obtain the translated word embedding, we output the most similar word vector as the translation. The word embeddings were learnt using the Skip Gram method proposed by (Mikolov et al., 2013a). An example of how the method would work is reported in figure 1 and figure 2. After creating the word embeddings from the two dictionaries, we plotted the numbers in the two graphs using PCA. Figure 3 reports the results after creating a linear mapping between the embeddings from the two languages. You can see how similar words are closer together.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-00b4f27db083847ab0d654b833c3bc5ff5232a9bb870f789b5920a3f54065c95

Passage ID: `qasper-passage-v1-00b4f27db083847ab0d654b833c3bc5ff5232a9bb870f789b5920a3f54065c95`; retrieval score: 4.0266911337177635.

Word count: 150.

```text
Since the word embeddings in a single language are based on the cosine similarity, we realized that through the objective function reported in equation 1 we were losing the property of this similarity. As a result we wanted the dot products to be preserved after the mapping. In order to do that we normalized the vectors $x_i$ and $z_i$.The new objective function looks like:

In order to preserve the dot products after the linear mapping we also had to constrain W to be an orthogonal matrix. In order to orthogonalize the matrix, it's required to solve the following optimization problem:

One can show that this problem can be solved by taking the singular value decomposition (SVD) of W and replacing the singular values to ones. This approximation would only work when the dimensions of the source vector and the target vector are the same, which is the set up we
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 667.

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

#### Rank 1: qasper-passage-v1-1baa0c4623e36fc55dca8f33431216f18c5a9eaa35c599008ad223c85eea7476

Passage ID: `qasper-passage-v1-1baa0c4623e36fc55dca8f33431216f18c5a9eaa35c599008ad223c85eea7476`; retrieval score: 3.365672550687823.

Word count: 150.

```text
The focus of this section is on recently published datasets and LID research applicable to the South African context. An in depth survey of algorithms, features, datasets, shared tasks and evaluation methods may be found in BIBREF0.

The datasets for the DSL 2015 & DSL 2017 shared tasks BIBREF1 are often used in LID benchmarks and also available on Kaggle . The DSL datasets, like other LID datasets, consists of text sentences labelled by language. The 2017 dataset, for example, contains 14 languages over 6 language groups with 18000 training samples and 1000 testing samples per language.

The recently published JW300 parallel corpus BIBREF2 covers over 300 languages with around 100 thousand parallel sentences per language pair on average. In South Africa, a multilingual corpus of academic texts produced by university students with different mother tongues is being developed BIBREF3. The WiLI-2018 benchmark dataset BIBREF4 for monolingual written natural language
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-8817b8d150d68b9eed9b80f8909b1a9fa15a600b3736aaf00c22c02e2bc4af55

Passage ID: `qasper-passage-v1-8817b8d150d68b9eed9b80f8909b1a9fa15a600b3736aaf00c22c02e2bc4af55`; retrieval score: 1.61666293831096.

Word count: 150.

```text
The proposed LID algorithm builds on the work in BIBREF8 and BIBREF26. We apply a naive Bayesian classifier with character (2, 4 & 6)-grams, word unigram and word bigram features with a hierarchical lexicon based classifier.

The naive Bayesian classifier is trained to predict the specific language label of a piece of text, but used to first classify text as belonging to either the Nguni family, the Sotho family, English, Afrikaans, Xitsonga or Tshivenda. The scikit-learn multinomial naive Bayes classifier is used for the implementation with an alpha smoothing value of 0.01 and hashed text features.

The lexicon based classifier is then used to predict the specific language within a language group. For the South African languages this is done for the Nguni and Sotho groups. If the lexicon prediction of the specific language has high confidence then its result is used as the final label else the naive Bayesian
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-8f21329683e745614c45500a64e8704d43002f223ff21489973681e0748d45b4

Passage ID: `qasper-passage-v1-8f21329683e745614c45500a64e8704d43002f223ff21489973681e0748d45b4`; retrieval score: 1.5595184279167627.

Word count: 150.

```text
language group. For the South African languages this is done for the Nguni and Sotho groups. If the lexicon prediction of the specific language has high confidence then its result is used as the final label else the naive Bayesian classifier's specific language prediction is used as the final result. The lexicon is built over all the data and therefore includes the vocabulary from both the training and testing sets.

The lexicon based classifier is designed to trade higher precision for lower recall. The proposed implementation is considered confident if the number of words from the winning language is at least one more than the number of words considered to be from the language scored in second place.

The stacked classifier is tested against three public LID implementations BIBREF17, BIBREF23, BIBREF8. The LID implementation described in BIBREF17 is available on GitHub and is trained and tested according to a post
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-d7384bff9a5ab84459277933cf23d4b38cbfdd0f26a58ae4b11fc53302466a8f

Passage ID: `qasper-passage-v1-d7384bff9a5ab84459277933cf23d4b38cbfdd0f26a58ae4b11fc53302466a8f`; retrieval score: 1.265918464256768.

Word count: 150.

```text
be from the language scored in second place.

The stacked classifier is tested against three public LID implementations BIBREF17, BIBREF23, BIBREF8. The LID implementation described in BIBREF17 is available on GitHub and is trained and tested according to a post on the fasttext blog. Character (5-6)-gram features with 16 dimensional vectors worked the best. The implementation discussed in BIBREF23 is available from https://github.com/tomkocmi/LanideNN. Following the instructions for an OSX pip install of an old r0.8 release of TensorFlow, the LanideNN code could be executed in Python 3.7.4. Settings were left at their defaults and a learning rate of 0.001 was used followed by a refinement with learning rate of 0.0001. Only one code modification was applied to return the results from a method that previously just printed to screen. The LID algorithm described in BIBREF8 is also available on GitHub.

The stacked classifier is also tested against the results reported
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-714a423051fc3a7ac3f05cac00eb404029a33393c02c6a3f02e645695dfc274b

Passage ID: `qasper-passage-v1-714a423051fc3a7ac3f05cac00eb404029a33393c02c6a3f02e645695dfc274b`; retrieval score: 1.2073157896881956.

Word count: 125.

```text
training data is available.

In summary, LID of short texts, informal styles and similar languages remains a difficult problem which is actively being researched. Increased confusion can in general be expected between shorter pieces of text and languages that are more closely related. Shallow methods still seem to work well compared to deeper models for LID. Other remaining research opportunities seem to be data harvesting, building standardised datasets and creating shared tasks for South Africa and Africa. Support for language codes that include more languages seems to be growing and discoverability of research is improving with more survey papers coming out. Paywalls also seem to no longer be a problem; the references used in this paper was either openly published or available as preprint papers.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 725.

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

#### Rank 1: qasper-passage-v1-245c7d8ad276b05da3dbd2f81e7cc14a8c6cf986f0cbf00fa42af22ae98f7822

Passage ID: `qasper-passage-v1-245c7d8ad276b05da3dbd2f81e7cc14a8c6cf986f0cbf00fa42af22ae98f7822`; retrieval score: 4.069079532141482.

Word count: 150.

```text
Entity linking (EL) BIBREF24 , also known as named entity disambiguation or normalization, is the task to determine the identity of entities mentioned in a piece of text with reference to a knowledge base. There are a number of knowledge bases that provide a background repository for entity classification of this type. For this study, we use Wikidata, which can be seen diagrammatically in Figure FIGREF12 . Systems such as DeepType BIBREF25 integrate symbolic information into the reasoning process of a neural network with a type system and show state-of-the-art performances for EL. They do not, however, quote results on Wiki(gold) so a direct comparison is difficult.

While these knowledge bases provide semantically rich and fine-granular classes and relationship types, the task of entity classification often requires associating coarse-grained classes with discovered surface forms of entities. Most existing studies consider NER and entity linking as two separate tasks, whereas we
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-27e5c7a708187bb4da8b72a4b1be148244348f10ecdd227dca72f7d2a4d2bfbf

Passage ID: `qasper-passage-v1-27e5c7a708187bb4da8b72a4b1be148244348f10ecdd227dca72f7d2a4d2bfbf`; retrieval score: 3.6517061483897995.

Word count: 150.

```text
The results for each class type are shown in Table TABREF19 , with some specific examples shown in Figure FIGREF18 . For the Wiki(gold) we quote the micro-averaged F-1 scores for the entire top level entity category. The total F-1 score on the OntoNotes dataset is 88%, and the total F-1 cross-validation score on the 112 class Wiki(gold) dataset is 53%. It is worth noting that one could improve Wiki(gold) results by training directly using this dataset. However, the aim is not to tune our model specifically on this class hierarchy. We instead aim to present a framework which can be modified easily to any domain hierarchy and has acceptable out-of-the-box performances to any fine-grained dataset. The results in Table TABREF19 (OntoNotes) only show the main 7 categories in OntoNotes which map to Wiki(gold) for clarity. The other categories (date, time, norp, language, ordinal, cardinal, quantity, percent, money, law) have
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.10503:6:0` | partial | 0:932 |

#### Rank 3: qasper-passage-v1-cbb6cafd91da3012063b939ee5f22712cedb4b21c6b112fdcfa755786e3d2fb2

Passage ID: `qasper-passage-v1-cbb6cafd91da3012063b939ee5f22712cedb4b21c6b112fdcfa755786e3d2fb2`; retrieval score: 3.280117612002556.

Word count: 150.

```text
corpus. For example, “Barack Obama” is a person, politician, lawyer, and author. If a knowledge base has these four matching labels, the distant supervision technique will assign all of them to every mention of “Barack Obama”. Therefore, the training data will also fail to distinguish between mentions of “Barack Obama” in all subsequent utterances.

Ling et al. ling2012fine proposed the first system for FgNER, where they used 112 overlapping labels with a linear classifier perceptron for multi-label classification. Yosef et al. spaniol2012hyena used multiple binary SVM classifiers to assign entities to a set of 505 types. Gillick et al. gillick2014context introduced context dependent FgNER and proposed a set of heuristics for pruning labels that might not be relevant given the local context of the entity. Yogatama et al. yogatama2015embedding proposed an embedding based model where user-defined features and labels were embedded into a low dimensional feature space to facilitate information
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-9e3093459bed9b4ed4f51929b0a11bf85e67708c283cacece8993a50b4bf1d6b

Passage ID: `qasper-passage-v1-9e3093459bed9b4ed4f51929b0a11bf85e67708c283cacece8993a50b4bf1d6b`; retrieval score: 3.1190630187722057.

Word count: 150.

```text
NER involves identifying both entity boundaries and entity types. With “exact-match evaluation”, a named entity is considered correctly recognized only if both the boundaries and type match the ground truth BIBREF8 , BIBREF17 , BIBREF18 . Precision, Recall, and F-1 scores are computed on the number of true positives (TP), false positives (FP), and false negatives (FN). Their formal definitions are as follows:

True Positive (TP): entities that are recognized by NER and match the ground truth.

False Positive (FP): entities that are recognized by NER but do not match the ground truth.

False Negative (FN): entities annotated in the ground which that are not recognized by NER.

Precision measures the ability of a NER system to present only correct entities, and Recall measures the ability of a NER system to recognize all entities in a corpus. DISPLAYFORM0

The F-1 score is the harmonic mean of precision and recall, and
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-a5e1fc12d3610d4719e4c2adee9b89b17b55acfc6e033f54cedd45783312f2c6

Passage ID: `qasper-passage-v1-a5e1fc12d3610d4719e4c2adee9b89b17b55acfc6e033f54cedd45783312f2c6`; retrieval score: 3.0887827471531275.

Word count: 150.

```text
number of types detected are still not sufficient for certain domain-specific applications. For relation extraction, identifying fine-grained types has been shown to significantly increase the performance of the extractor BIBREF8 , BIBREF9 since this helps in filtering out candidate relation types which do not follow this type constraint. Furthermore, for question answering fine-grained Named Entity Recognition (FgNER) can provide additional information helping to match questions to its potential answers thus improving performance BIBREF10 . For example, Li and Roth BIBREF11 rank questions based on their expected answer types (i.e. will the answer be food, vehicle or disease).

Typically, FgNER systems use over a hundred labels, arranged in a hierarchical structure. We find that available training data for FgNER typically contain noisy labels, and creating manually annotated training data for FgNER is a time-consuming process. Furthermore, human annotators will have to assign a subset of correct labels from hundreds of possible
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 750.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "4cbb4c87c1ba12f24c101941969835ae60d88c5b": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1904.10503:6:0": [
        [
          932,
          992
        ]
      ]
    }
  },
  "f4eb7f67fb41888ab6b1fa018211c89994b6e8fe": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1904.10503:6:0": [
        [
          932,
          992
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-7e63330b55b4ce5912c06078b32aedccf40c2ca3717ec9303d77b64fc0317312

Passage ID: `qasper-passage-v1-7e63330b55b4ce5912c06078b32aedccf40c2ca3717ec9303d77b64fc0317312`; retrieval score: 7.842641176707737.

Word count: 150.

```text
To the best of our knowledge, there are only two recent works that specifically study how to combine word and subword-level vector representations.

BIBREF11 propose to use a trainable scalar gating mechanism capable of learning a weighting scheme for combining character-level and word-level representations. They compared their proposed method to manually weighting both levels; using characters only; words only; or their concatenation. They found that in some datasets a specific manual weighting scheme performed better, while in others the learned scalar gate did.

BIBREF12 further expand the gating concept by making the mechanism work at a finer-grained level, learning how to weight each vector's dimensions independently, conditioned on external word-level features such as part-of-speech and named-entity tags. Similarly, they compared their proposed mechanism to using words only, characters only, and a concatenation of both, with and without external features. They found that their vector gate performed better than the other
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-d79c41b2148ec4488a913a82e74e7525b0adac9bfbdb492aa265d3eee5b0ad30

Passage ID: `qasper-passage-v1-d79c41b2148ec4488a913a82e74e7525b0adac9bfbdb492aa265d3eee5b0ad30`; retrieval score: 6.091779344541739.

Word count: 130.

```text
To enable sentence-level classification we need to obtain a sentence representation from the word vectors INLINEFORM0 . We achieved this by using a BiLSTM with max pooling, which was shown to be a good universal sentence encoding mechanism BIBREF13 .

Let INLINEFORM0 , be an input sentence and INLINEFORM1 its matrix representation, where each INLINEFORM2 was obtained by one of the methods described in subsec:methods. INLINEFORM3 is the context-enriched matrix representation of INLINEFORM4 obtained by feeding INLINEFORM5 to a BiLSTM of output dimension INLINEFORM6 . Lastly, INLINEFORM11 is the final sentence representation of INLINEFORM12 obtained by max-pooling INLINEFORM13 along the sequence dimension.

Finally, we initialized the word representations INLINEFORM0 using GloVe embeddings BIBREF14 , and fine-tuned them during training. Refer to app:hyperparams for details on the other hyperparameters we used.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.05584:4:0` | full | 0:250 |

#### Rank 3: qasper-passage-v1-cf9f1934276c5a3f83e93ca6e2e777ce5feba95076da5b9f298e9dfbc22b1de7

Passage ID: `qasper-passage-v1-cf9f1934276c5a3f83e93ca6e2e777ce5feba95076da5b9f298e9dfbc22b1de7`; retrieval score: 5.056523641578001.

Word count: 150.

```text
table:wordlevelresults shows the quality of word representations in terms of the correlation between word similarity scores obtained by the proposed models and word similarity scores defined by humans.

First, we can see that for each task, character only models had significantly worse performance than every other model trained on the same dataset. The most likely explanation for this is that these models are the only ones that need to learn word representations from scratch, since they have no access to the global semantic knowledge encoded by the GloVe embeddings.

Further, bold results show the overall trend that vector gates outperformed the other methods regardless of training dataset. This implies that learning how to combine character and word-level representations at the dimension level produces word vector representations that capture a notion of word similarity and relatedness that is closer to that of humans.

Additionally, results from the MNLI row in general,
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-b811434da8918a8d74a52ebcd8e8f6a590a821e18a062d37492bc5ec9e4ba18a

Passage ID: `qasper-passage-v1-b811434da8918a8d74a52ebcd8e8f6a590a821e18a062d37492bc5ec9e4ba18a`; retrieval score: 4.770652036039301.

Word count: 150.

```text
The problem of representing sentences as fixed-length vectors has been widely studied.

BIBREF32 suggested a self-adaptive hierarchical model that gradually composes words into intermediate phrase representations, and adaptively selects specific hierarchical levels for specific tasks. BIBREF33 proposed an encoder-decoder model trained by attempting to reconstruct the surrounding sentences of an encoded passage, in a fashion similar to Skip-gram BIBREF34 . BIBREF35 overcame the previous model's need for ordered training sentences by using autoencoders for creating the sentence representations. BIBREF36 implemented a model simpler and faster to train than the previous two, while having competitive performance. Similar to BIBREF33 , BIBREF37 suggested predicting future sentences with a hierarchical CNN-LSTM encoder.

BIBREF13 trained several sentence encoding architectures on a combination of the SNLI and MultiNLI datasets, and showed that a BiLSTM with max-pooling was the best at producing highly transferable sentence representations. More recently, BIBREF18 empirically showed that sentence representations created in
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-a3dbf2a51649942004b02def1fe6e8dc38cfc3b6d3df83309152ebbfd83f95f2

Passage ID: `qasper-passage-v1-a3dbf2a51649942004b02def1fe6e8dc38cfc3b6d3df83309152ebbfd83f95f2`; retrieval score: 4.694431787657197.

Word count: 128.

```text
sentence representations should have. In response to this, BIBREF13 created SentEval, a sentence representation evaluation benchmark designed for assessing how well sentence representations perform in various downstream tasks BIBREF23 .

Some of the datasets included in SentEval correspond to sentiment classification (CR, MPQA, MR, SST2, and SST5), subjectivity classification (SUBJ), question-type classification (TREC), recognizing textual entailment (SICK E), estimating semantic relatedness (SICK R), and measuring textual semantic similarity (STS16, STSB). The datasets are described by BIBREF13 , and we provide pointers to their original sources in the appendix table:sentence-eval-datasets.

To evaluate these sentence representations SentEval trained a linear model on top of them, and evaluated their performance in the validation sets accompanying each dataset. The only exception was the STS16 task, in which our representations were evaluated directly.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 708.

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

#### Rank 1: qasper-passage-v1-4a8c11b2c97c19d3bdf0f29de68d7070f6a9fdfa00557e6ce4ddaf3dd10a80e4

Passage ID: `qasper-passage-v1-4a8c11b2c97c19d3bdf0f29de68d7070f6a9fdfa00557e6ce4ddaf3dd10a80e4`; retrieval score: 5.807168270800754.

Word count: 130.

```text
The right diagram in Fig. FIGREF15 illustrates the Baseline2 model.

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

#### Rank 2: qasper-passage-v1-617a0c20e0eb8ca7fe97789492bc5dbcee3bc731252a0e94c3b31cb2198d20ab

Passage ID: `qasper-passage-v1-617a0c20e0eb8ca7fe97789492bc5dbcee3bc731252a0e94c3b31cb2198d20ab`; retrieval score: 5.5872038125795624.

Word count: 150.

```text
to the video segment. Instead, we took a reversed approach. First, for each video, we manually identified the sentence spans that can serve as answers. These candidates are of various granularity and may overlap. The segments are also complete in that they encompass the beginning and end of a task. In total, we identified 408 segments from the 76 videos. Second we asked AMT workers to provide question annotations for the videos.

Our AMT experiment consisted of two parts. In the first part, we presented the workers with the video content of a segment. For each segment, we asked workers to generate questions that can be answered by the presented segment. We did not limit the number of questions a worker can input to a corresponding segment and encouraged them to input a diverse set of questions which the span can answer. Along with the questions, the workers were also
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-7d5e9608e9987d896b0a172c36d9092507144b2070d304ae94752e2264905fbf

Passage ID: `qasper-passage-v1-7d5e9608e9987d896b0a172c36d9092507144b2070d304ae94752e2264905fbf`; retrieval score: 5.47640542481439.

Word count: 55.

```text
distance distance to the query.

Metrics. To evaluate our pipeline approach we use overall accuracy after filtering and accuracy given that the segment is in the top 10 videos. While the first metric is similar to SECREF17, the second can indicate if initially searching on the video space can be used to improve our selection:
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1912.01046:10:4` | full | 0:294 |

#### Rank 4: qasper-passage-v1-6591b3073d44620a32ce10aabc0e85a19e92d4a89af94c3d883f213371023642

Passage ID: `qasper-passage-v1-6591b3073d44620a32ce10aabc0e85a19e92d4a89af94c3d883f213371023642`; retrieval score: 5.397707945622137.

Word count: 150.

```text
Table TABREF12 presents some extracted sample questions from our dataset. The first column corresponds to an AMT generated question, while the second column corresponds to the video ID where the segment can be found. As can be seen in the first two rows, multiple types of questions can be answered within the same video (but different segments). The last two rows display questions which belong to the same segment but correspond to different properties of the same entity, 'crop tool'. Here we observe different types of questions, such as "why", "how", "what", and "where", and can see why the answers may involve multiple steps. Some questions that the worked paraphrased were in the "yes/no" style, however our answer segments then provide an explanation to these questions.

Each answer segment was extracted from an image editing tutorial video that involved multiple steps and procedures to produce a final image, which can
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-1fe71d48b8b2825cc5acbed533424ae31f81b14f7d43230a7c97cb4bc9fcd1b1

Passage ID: `qasper-passage-v1-1fe71d48b8b2825cc5acbed533424ae31f81b14f7d43230a7c97cb4bc9fcd1b1`; retrieval score: 5.147689156668605.

Word count: 150.

```text
Video is the fastest growing medium to create and deliver information today. Consequentially, videos have been increasingly used as main data sources in many question answering problems BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, BIBREF2, BIBREF5. These previous studies have mostly focused on factoid questions, each of which can be answered in a few words or phrases generated by understanding multimodal contents in a short video clip.

However, this problem definition of video question answering causes some practical limitations for the following reasons. First, factoid questions are just a small part of what people actually want to ask on video contents. Especially if a short video is given to users, most fragmentary facts within the scope of previous tasks can be easily perceived by themselves even before asking questions. Thus, video question answering is expected to provide answers to more complicated non-factoid questions beyond the simple facts. For example, those questions could
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 635.

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

#### Rank 1: qasper-passage-v1-72b8b0783befca7bdceb8da5d27e8a7bf4d5d3a71a9d879f401e7bad4f42328d

Passage ID: `qasper-passage-v1-72b8b0783befca7bdceb8da5d27e8a7bf4d5d3a71a9d879f401e7bad4f42328d`; retrieval score: 5.205983373343625.

Word count: 150.

```text
provenance is a 1-to-1 problem as it keeps track of detailed updates of one document BIBREF4 , BIBREF5 . Real-world applications include GitHub, version control in Microsoft Word and Wikipedia version trees BIBREF6 . In contrast, our system solves an n-to-n problem on a large scale. Our potential target data sources, such as the entire web or internal corpora in corporations, contain numerous original documents and their revisions. The aim is to find all revision document pairs within a reasonable time.

Document revision detection, plagiarism detection and revision provenance all rely on comparing the content of two documents and assessing a distance/similarity score. The classic document similarity measure, especially for plagiarism detection, is fingerprinting BIBREF7 , BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 . Fixed-length fingerprints are created using hash functions to represent document features and are then used to measure document similarities. However, the main purpose of
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-0133086c13c591cc7539b40444e130cf2cb048d7a7b7031a461dbb768a0e4631

Passage ID: `qasper-passage-v1-0133086c13c591cc7539b40444e130cf2cb048d7a7b7031a461dbb768a0e4631`; retrieval score: 4.585876413861209.

Word count: 120.

```text
the effectiveness and robustness of wDTW and wTED in the Wikipedia revision dumps and our simulated data sets. In order to reduce the computation time, we have computed document distances at the paragraph level and implemented a boosting learning system using Apache Spark. Although we have demonstrated the superiority of our semantic measures only in the revision detection experiments, wDTW and wTED can also be used as semantic distance measures in many clustering, classification tasks.

Our revision detection system can be enhanced with richer features such as author information and writing styles, and exact changes in revision pairs. Another interesting aspect we would like to explore in the future is reducing the complexities of calculating the distance between two paragraphs.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-bfb61d0201d45c31c35e6dddd616de6e6c74508365826a2c3926aea8981d2453

Passage ID: `qasper-passage-v1-bfb61d0201d45c31c35e6dddd616de6e6c74508365826a2c3926aea8981d2453`; retrieval score: 4.506223691353218.

Word count: 150.

```text
We use precision, recall and F-measure to evaluate the detected revisions. A true positive case is a correctly identified revision. A false positive case is an incorrectly identified revision. A false negative case is a missed revision record.

We illustrate the performances of wDTW, wTED, WMD, VSM, PV-DTW and PV-TED on the Wikipedia revision dumps in Figure FIGREF43 . wDTW and wTED have the highest F-measure scores compared to the rest of four measures, and wDTW also have the highest precision and recall scores. Figure FIGREF49 shows the average evaluation results on the simulated data sets. From left to right, the corpus size increases and the revision chains become longer, thus it becomes more challenging to detect document revisions. Overall, wDTW consistently performs the best. WMD is slightly better than wTED. In particular, when the corpus size increases, the performances of WMD, VSM, PV-DTW and PV-TED drop faster than wDTW
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1709.01256:12:0` | full | 0:243 |

#### Rank 4: qasper-passage-v1-7f8fa384019eff05724a1023ca7a25fc7c0fc31cc01ad89c9606adc45bae03f6

Passage ID: `qasper-passage-v1-7f8fa384019eff05724a1023ca7a25fc7c0fc31cc01ad89c9606adc45bae03f6`; retrieval score: 4.441621658214604.

Word count: 150.

```text
plagiarism detection, is fingerprinting BIBREF7 , BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 . Fixed-length fingerprints are created using hash functions to represent document features and are then used to measure document similarities. However, the main purpose of fingerprinting is to reduce computation instead of improving accuracy, and it cannot capture word semantics. Another widely used approach is computing the sentence-to-sentence Levenshtein distance and assigning an overall score for every document pair BIBREF13 . Nevertheless, due to the large number of existing documents, as well as the large number of sentences in each document, the Levenshtein distance is not computation-friendly. Although alternatives such as the vector space model (VSM) can largely reduce the computation time, their effectiveness is low. More importantly, none of the above approaches can capture semantic meanings of words, which heavily limits the performances of these approaches. For instance, from a semantic perspective, “I went
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-6972096ef29b163f84fa6018ac3ce75ee517e91b2b099b37fb1698792a72929e

Passage ID: `qasper-passage-v1-6972096ef29b163f84fa6018ac3ce75ee517e91b2b099b37fb1698792a72929e`; retrieval score: 4.089528842577818.

Word count: 150.

```text
This paper has explored how DTW and TED can be extended with word2vec to construct semantic document distance measures: wDTW and wTED. By representing paragraphs with concatenations of word vectors, wDTW and wTED are able to capture the semantics of the words and thus give more accurate distance scores. In order to detect revisions, we have used minimum branching on an appropriately developed network with document distance scores serving as arc weights. We have also assessed the efficiency of the method of retrieving an optimal revision subnetwork by finding the minimum branching.

Furthermore, we have compared wDTW and wTED with several distance measures for revision detection tasks. Our results demonstrate the effectiveness and robustness of wDTW and wTED in the Wikipedia revision dumps and our simulated data sets. In order to reduce the computation time, we have computed document distances at the paragraph level and implemented a boosting learning system
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 720.

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

#### Rank 1: qasper-passage-v1-5895a200e51b90ff07f77d2a7dd0a9b0ecd973427dcf1826af6be0825069c7d7

Passage ID: `qasper-passage-v1-5895a200e51b90ff07f77d2a7dd0a9b0ecd973427dcf1826af6be0825069c7d7`; retrieval score: 2.9402727626816367.

Word count: 102.

```text
queries sampled evenly across all intents (versus 250 out-of-scope), and another where we augment the 250 OOS+ out-of-scope training queries with 14,750 sentences sampled from Wikipedia.

From a development point of view, the oos-train and oos-binary methods both require careful curation of an out-of-scope training set, and this set can be tailored to individual systems. The oos-threshold method is a more general decision rule that can be applied to any model that produces a probability. In our evaluation, the out-of-scope threshold was chosen to be the value which yielded the highest validation score across all intents, treating out-of-scope as its own intent.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-9c06e591090fcc2e5c5150b73f6f0d846dc8a22b57c9d0bcdafac2820496d314

Passage ID: `qasper-passage-v1-9c06e591090fcc2e5c5150b73f6f0d846dc8a22b57c9d0bcdafac2820496d314`; retrieval score: 2.891924373126757.

Word count: 150.

```text
Table TABREF14 presents results for all models across the four variations of the dataset. First, BERT is consistently the best approach for in-scope, followed by MLP. Second, out-of-scope query performance is much lower than in-scope across all methods. Training on less data (Small and Imbalanced) yields models that perform slightly worse on in-scope queries. The trend is mostly the opposite when evaluating out-of-scope, where recall increases under the Small and Imbalanced training conditions. Under these two conditions, the size of the in-scope training set was decreased, while the number of out-of-scope training queries remained constant. This indicates that out-of-scope performance can be increased by increasing the relative number of out-of-scope training queries. We do just that in the OOS+ setting—where the models were trained on the full training set as well as 150 additional out-of-scope queries—and see that performance on out-of-scope increases substantially, yet still remains low relative to in-scope
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-529de494ab650fc70946cd1b0520d81cab94c38ba1fd2245d1272c05128a4659

Passage ID: `qasper-passage-v1-529de494ab650fc70946cd1b0520d81cab94c38ba1fd2245d1272c05128a4659`; retrieval score: 2.856071990866932.

Word count: 118.

```text
For all queries collected, all tokens were down-cased, and all end-of-sentence punctuation was removed. Additionally, all duplicate queries were removed and replaced.

In an effort to reduce bias in the in-scope data, we placed all queries from a given crowd worker in a single split (train, validation, or test). This avoids the potential issue of similar queries from a crowd worker ending up in both the train and test sets, for instance, which would make the train and test distributions unrealistically similar. We note that this is a recommendation from concurrent work by BIBREF3. We also used this procedure for the out-of-scope set, except that we split the data into train/validation/test based on task prompt instead of worker.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-7e229f552092db37255dafdecb4de11b5f0ffb0c396152ef863a39f95bcc8eb6

Passage ID: `qasper-passage-v1-7e229f552092db37255dafdecb4de11b5f0ffb0c396152ef863a39f95bcc8eb6`; retrieval score: 1.5394559676006638.

Word count: 150.

```text
in-scope queries, representing things a user might say given partial knowledge of the capabilities of a system.

Table TABREF20 compares our dataset with other short-query intent classification datasets. The Snips BIBREF0 dataset and the dataset presented in BIBREF10 are the most similar to the in-scope part of our work, with the same type of conversational agent requests. Like our work, both of these datasets were bootstrapped using crowdsourcing. However, the Snips dataset has only a small number of intents and an enormous number of examples of each. Snips does present a low-data variation, with 70 training queries per intent, in which performance drops slightly. The dataset presented in BIBREF10 has a large number of intent classes, yet also contains a wide range of samples per intent class (ranging from 24 to 5,981 queries per intent, and so is not constrained in all cases).

BIBREF11 created datasets with constrained training data,
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-eddca8cadaba693246cca1f0c38ebe33ba9586553008d0085529efa13f650323

Passage ID: `qasper-passage-v1-eddca8cadaba693246cca1f0c38ebe33ba9586553008d0085529efa13f650323`; retrieval score: 1.4830030114059234.

Word count: 150.

```text
In most other analyses and datasets, the idea of out-of-scope data is not considered, and instead the output classes are intended to cover all possible queries (e.g., TREC BIBREF7). Recent work by BIBREF8 considers a similar problem they call out-of-distribution detection. They use other datasets or classes excluded during training to form the out-of-distribution samples. This means that the out-of-scope samples are from a small set of coherent classes that differ substantially from the in-distribution samples. Similar experiments were conducted for evaluating unknown intent discovery models in BIBREF9. In contrast, our out-of-scope queries cover a broad range of phenomena and are similar in style and often similar in topic to in-scope queries, representing things a user might say given partial knowledge of the capabilities of a system.

Table TABREF20 compares our dataset with other short-query intent classification datasets. The Snips BIBREF0 dataset and the dataset presented in BIBREF10 are the
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

#### Rank 1: qasper-passage-v1-483bd0af3d3c00f92dac53c5c60dd52f2e7924a53213fef8ac989bdda08713e2

Passage ID: `qasper-passage-v1-483bd0af3d3c00f92dac53c5c60dd52f2e7924a53213fef8ac989bdda08713e2`; retrieval score: 4.333681178027103.

Word count: 150.

```text
for 6 languages on the ABSA benchmarks BIBREF4 , BIBREF5 , BIBREF6 .

The main contribution of this research note is providing an extension or addendum to previous work on sequence labelling BIBREF7 by reporting additional experimental results as well as further insights on the performance of our model across languages on a different NLP task such as Opinion Target Extraction (OTE). Thus, we empirically demonstrate the validity and strong performance of our approach for six languages in seven different datasets of the restaurant domain. Every experiment and result presented in this note is novel.

In this sense, we show that our approach is not only competitive across languages and domains for Named Entity Recognition, as shown by BIBREF7 , but that it can be straightforwardly adapted to different tasks and domains such as OTE. Furthermore, we release the system and every model trained for public use and to facilitate
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-565387b29d38c0f77f697a672399b44d257765e2f0924cdbf3b4ad05329fb342

Passage ID: `qasper-passage-v1-565387b29d38c0f77f697a672399b44d257765e2f0924cdbf3b4ad05329fb342`; retrieval score: 3.219984675608964.

Word count: 150.

```text
We trained our system for 5 other languages on the ABSA 2016 datasets, using the same strategy as for English. We choose the best Clark-Word2vec combination (with and without Brown clusters) via 5-cross validation on the training data. The features are exactly the same as those used for English, the only change is the data on which the clusters are trained. Table TABREF19 reports on the detailed results obtained for each of the languages. In bold we show the best model chosen via 5-fold CV. Moreover, we also show the best models using only one of each of the clustering features.

The first difference with respect to the English results is that the Brown clustering features are, in three out of five settings, detrimental to performance. Second, that combining clustering features is only beneficial for Spanish. Third, the overall results are in general lower than those obtained in the 2016
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-07492f48f93291832daaf6e13ecee4e2afa2c7da52cd97829dff35da94f491e4

Passage ID: `qasper-passage-v1-07492f48f93291832daaf6e13ecee4e2afa2c7da52cd97829dff35da94f491e4`; retrieval score: 2.78578845171509.

Word count: 150.

```text
which the system was unable to annotate by generalizing on the training data or clusters.

With respect to type (a), it is useful to look at the most common errors for all three languages, namely, `place', `food' and `restaurant', which are also among the top 5 most frequent targets in the gold standard sets. By looking at Examples (1-3) we would say that in all three cases `place' should be annotated as opinion target. However, (2) is a false positive (FP), (3) is a false negative (FN) and (1) is an example from the training set in which `place' is annotated as target. This is the case with many instances of `place' for which there seems to be some inconsistency in the actual annotation of the training and test set examples.

Example (1): Avoid this place!

Example (2): this place is a keeper!

Example (3): it is great place to
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-d7a4a01f4be8a993a1168fa60d9d9218052cb0119ec6e5e2e537f0bc111fb1b1

Passage ID: `qasper-passage-v1-d7a4a01f4be8a993a1168fa60d9d9218052cb0119ec6e5e2e537f0bc111fb1b1`; retrieval score: 2.6204400265172847.

Word count: 150.

```text
the rest of languages the clusters are induced using the Wikipedia, effectively an out-of-domain corpus. The exception is Turkish, for which a 6 point gain in F1 score is obtained, but we believe that is probably due to the small size of the training data used for training the Local model.

In contrast, Word2vec clusters clearly benefit from larger amounts of data, as illustrated by the best English Word2vec model being the one trained using the Wikipedia, and not the Yelp dataset, which is closer to the application domain. Finally, the Clark algorithm seems to be the most versatile as it consistently outperforms the other two clustering methods in 4 out of the 8 evaluation settings presented.

Summarizing: (i) Brown clusters perform better when leveraged from source data close to the application domain, even if small in size; (ii) Clark clusters are the most robust of the three with respect
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-d1dc0235b020ec1d34a15c962cda5a9618a70c906f4df309bb64ea706fb4cc13

Passage ID: `qasper-passage-v1-d1dc0235b020ec1d34a15c962cda5a9618a70c906f4df309bb64ea706fb4cc13`; retrieval score: 2.606127502284429.

Word count: 150.

```text
“restaurant” in English and for `cuisine' and `restaurant' in French.

Span type (b) errors are typically caused by long opinion targets such as “filet mignon on top of spinach and mashed potatoes” for which our system annotates “filet” and “spinach” as separate targets, or “chicken curry and chicken tikka masala” which is wrongly tagged as one target. These cases are difficult because on the surface they look similar but the first one refers to one dish only, hence one target, whereas the second one refers to two separate dishes for which two different opinion targets should be annotated. Of course, these cases are particularly hurtful because they count as both FP and FN.

Finally, type (c) errors are usually caused by lack of generalization of our system to deal with unknown targets. Example (4-7) contain various mentions to the “Ray's” restaurant, which is in the top 5 errors for the
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 750.

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

#### Rank 1: qasper-passage-v1-00c531a0070fbc8a5e8faa4b8e1d0aad7b2616b803b055226847b5730489f784

Passage ID: `qasper-passage-v1-00c531a0070fbc8a5e8faa4b8e1d0aad7b2616b803b055226847b5730489f784`; retrieval score: 4.026398689423007.

Word count: 133.

```text
to calculate how semantically similar these two lists are.

Recommendation diversity. As defined in BIBREF18 , we calculate recommendation diversity as the average dissimilarity of all pairs of tags in the list of recommended tags. Thus, given a distance function INLINEFORM0 that corresponds to the dissimilarity between two tags INLINEFORM1 and INLINEFORM2 in the list of recommended tags, INLINEFORM3 is given as the average dissimilarity of all pairs of tags: DISPLAYFORM0

where INLINEFORM0 is the number of evaluated e-books and the dissimilarity function is defined as INLINEFORM1 . In our experiments, we use the previously trained Doc2Vec model to extract the latent representation of a specific tag. The similarity of two tags INLINEFORM2 is then calculated with the Cosine similarity measure using the latent vector representations of respective tags INLINEFORM3 and INLINEFORM4 .
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.04042:6:8` | full | 0:416 |

#### Rank 2: qasper-passage-v1-f9cc0892a94823a5ada0c839d3590700fb45219f4a1d79b3f1eed925498c72d2

Passage ID: `qasper-passage-v1-f9cc0892a94823a5ada0c839d3590700fb45219f4a1d79b3f1eed925498c72d2`; retrieval score: 3.5775254042605296.

Word count: 125.

```text
popularity-based, (ii) similarity-based (i.e., using content information), and (iii) hybrid approaches. We evaluate our approaches in terms of accuracy, semantic similarity and diversity on the review content of Amazon users, which reflects the readers' vocabulary. With semantic similarity, we measure how semantically similar (based on learned Doc2Vec BIBREF7 embeddings) the list of recommended tags is to the list of relevant tags. We use this additional metric to measure not only exact “hits” of our recommendations but also semantic matches.

Our evaluation results show that combining both data sources enhances the quality of tag recommendations for annotating e-books. Furthermore, approaches that solely train on Amazon search terms provide poor performance in terms of accuracy but deliver good results in terms of semantic similarity and recommendation diversity.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-3e1198a7f854fd6ea1ae7e7d7a1ff57dc3d21a4575f5a120aad6bbb98483522e

Passage ID: `qasper-passage-v1-3e1198a7f854fd6ea1ae7e7d7a1ff57dc3d21a4575f5a120aad6bbb98483522e`; retrieval score: 3.5418891139489377.

Word count: 150.

```text
In this work, we measure (i) recommendation accuracy, (ii) semantic similarity, and (iii) recommendation diversity to evaluate the quality of our approaches from different perspectives.

Recommendation accuracy. We use Normalized Discounted Cumulative Gain (nDCG) BIBREF15 to measure the accuracy of the tag recommendation approaches. The nDCG measure is a standard ranking-dependent metric that not only measures how many tags can be correctly predicted but also takes into account their position in the recommendation list with length of INLINEFORM0 . It is based on the Discounted Cummulative Gain, which is given by: DISPLAYFORM0

where INLINEFORM0 is a function that returns 1 if the recommended tag at position INLINEFORM1 in the recommended list is relevant. We then calculate DCG@ INLINEFORM2 for every evaluated e-book by dividing DCG@ INLINEFORM3 with the ideal DCG value iDCG@ INLINEFORM4 , which is the highest possible DCG value that can be achieved if all the relevant tags
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-4e50c1d52dd81e88408fd763d0783363b5aaa40ae3b34a46a890b22866383a08

Passage ID: `qasper-passage-v1-4e50c1d52dd81e88408fd763d0783363b5aaa40ae3b34a46a890b22866383a08`; retrieval score: 3.5229838353609093.

Word count: 150.

```text
on this, we propose an alternative measure of recommendation quality by learning the semantic relationships from both vocabularies and then using it to compare how semantically similar the recommended tags are to the expected review keywords. For this, we first extract the textual content in the form of the description text, title, editor tags and Amazon search terms of e-books from our dataset. We then train a Doc2Vec BIBREF7 model on the content. Then, we use the model to infer the latent representation for both the complete list of recommended tags as well as the list of expected tags from the test set. Finally, we use the cosine similarity measure to calculate how semantically similar these two lists are.

Recommendation diversity. As defined in BIBREF18 , we calculate recommendation diversity as the average dissimilarity of all pairs of tags in the list of recommended tags. Thus, given a distance function
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.04042:6:8` | partial | 0:203 |

#### Rank 5: qasper-passage-v1-5d5f439924a7939c549fab26f5069307b7e4896cee9191d98bdb8e2353ad188d

Passage ID: `qasper-passage-v1-5d5f439924a7939c549fab26f5069307b7e4896cee9191d98bdb8e2353ad188d`; retrieval score: 2.6924720929190986.

Word count: 57.

```text
similarity could still be helpful for annotating e-books.

Recommendation diversity. Figure FIGREF16 shows the diversity of the tag recommendation approaches. We achieve the highest diversity with the similarity-based approaches, which extract Amazon search terms. Their accuracy is, however, very low. Thus, the combination of the two vocabularies can provide a good trade-off between recommendation accuracy and diversity.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 615.

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

#### Rank 1: qasper-passage-v1-2eb209864ea98de5717b4a6adfb3ee2542a24c8c85c26f5f150fc3f5c0f74d94

Passage ID: `qasper-passage-v1-2eb209864ea98de5717b4a6adfb3ee2542a24c8c85c26f5f150fc3f5c0f74d94`; retrieval score: 6.095284613165557.

Word count: 150.

```text
We compare the proposed approach for translating natural language instructions into a navigation plan against alternative deep-learning models:

[align=left,leftmargin=0em,labelsep=0.4em,font=]

The baseline approach is based on BIBREF20 . It divides the task of interpreting commands for behavioral navigation into two steps: path generation, and path verification. For path generation, this baseline uses a standard sequence-to-sequence model augmented with an attention mechanism, similar to BIBREF23 , BIBREF6 . For path verification, the baseline uses depth-first search to find a route in the graph that matches the sequence of predicted behaviors. If no route matches perfectly, the baseline changes up to three behaviors in the predicted sequence to try to turn it into a valid path.

To test the impact of using the behavioral graphs as an extra input to our translation model, we implemented a version of our approach that only takes natural language instructions as input. In this ablation model, the
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-c706dceac42b791646c464d43ce259d5ebfa724702f2537a7e1d1b32998b3d15

Passage ID: `qasper-passage-v1-c706dceac42b791646c464d43ce259d5ebfa724702f2537a7e1d1b32998b3d15`; retrieval score: 5.6816722042911305.

Word count: 150.

```text
This section discusses qualitative results to better understand how the proposed model uses the navigation graph.

We analyze the evolution of the attention weights INLINEFORM0 in Eq. () to assess if the decoder layer of the proposed model is attending to the correct parts of the behavioral graph when making predictions. Fig FIGREF33 (b) shows an example of the resulting attention map for the case of a correct prediction. In the Figure, the attention map is depicted as a scaled and normalized 2D array of color codes. Each column in the array shows the attention distribution INLINEFORM1 used to generate the predicted output at step INLINEFORM2 . Consequently, each row in the array represents a triplet in the corresponding behavioral graph. This graph consists of 72 triplets for Fig FIGREF33 (b).

We observe a locality effect associated to the attention coefficients corresponding to high values (bright areas) in each column
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-fffb454e8410b904d6560937a1274a2d90843b7fa08b1f5f90fda09d48c165a6

Passage ID: `qasper-passage-v1-fffb454e8410b904d6560937a1274a2d90843b7fa08b1f5f90fda09d48c165a6`; retrieval score: 5.364262738533953.

Word count: 150.

```text
Table TABREF28 shows the performance of the models considered in our evaluation on both test sets. The next two sections discuss the results in detail.

First, we can observe that the final model “Ours with Mask and Ordered Triplets” outperforms the Baseline and Ablation models on all metrics in previously seen environments. The difference in performance is particularly evident for the Exact Match and Goal Match metrics, with our model increasing accuracy by 35% and 25% in comparison to the Baseline and Ablation models, respectively. These results suggest that providing the behavioral navigation graph to the model and allowing it to process this information as a knowledge base in an end-to-end fashion is beneficial.

We can also observe from Table TABREF28 that the masking function of Eq. ( EQREF12 ) tends to increase performance in the Test-Repeated Set by constraining the output sequence to a valid set of navigation behaviors.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1810.00663:10:1` | full | 0:572 |

#### Rank 4: qasper-passage-v1-0ccb758c92021279b3f003e3fd2863ce7c0bbb7718071df6d8ccac82f2623650

Passage ID: `qasper-passage-v1-0ccb758c92021279b3f003e3fd2863ce7c0bbb7718071df6d8ccac82f2623650`; retrieval score: 4.986724910444006.

Word count: 150.

```text
in INLINEFORM11 to calculate its associated attention distribution INLINEFORM12 over all the atomic instructions INLINEFORM13 : DISPLAYFORM0

where the matrix INLINEFORM0 serves to combine the different sources of information INLINEFORM1 and INLINEFORM2 . Each component INLINEFORM3 of the attention distributions INLINEFORM4 quantifies the affinity between the INLINEFORM5 -th triplet in INLINEFORM6 and the INLINEFORM7 -th word in the corresponding input INLINEFORM8 .

The model then uses each attention distribution INLINEFORM0 to obtain a weighted sum of the encodings of the words in INLINEFORM1 , according to their relevance to the corresponding triplet INLINEFORM2 . This results in L attention vectors INLINEFORM3 , INLINEFORM4 .

The final step in the attention layer concatenates each INLINEFORM0 with INLINEFORM1 to generate the outputs INLINEFORM2 , INLINEFORM3 . Following BIBREF8 , we include the encoded triplet INLINEFORM4 in the output tensor INLINEFORM5 of this layer to prevent early summaries of relevant map information.

FC
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-fd2366dd1866433819af1c277ef7f371a3ba50a567c7bc676c76b19920745361

Passage ID: `qasper-passage-v1-fd2366dd1866433819af1c277ef7f371a3ba50a567c7bc676c76b19920745361`; retrieval score: 4.932325754330978.

Word count: 150.

```text
about the whole environment, while the instruction has (potentially incomplete) local information about the route of interest. The use of attention provides our model with a two-step strategy to interpret commands. This resembles the way people find paths on a map: first, relevant parts on the map are selected according to their affinity to each of the words in the input instruction (attention layer); second, the selected parts are connected to assemble a valid path (decoder layer). More formally, let INLINEFORM2 ( INLINEFORM3 ) be the INLINEFORM4 -th row of INLINEFORM5 , and INLINEFORM6 ( INLINEFORM7 ) the INLINEFORM8 -th row of INLINEFORM9 . We use each encoded triplet INLINEFORM10 in INLINEFORM11 to calculate its associated attention distribution INLINEFORM12 over all the atomic instructions INLINEFORM13 : DISPLAYFORM0

where the matrix INLINEFORM0 serves to combine the different sources of information INLINEFORM1 and INLINEFORM2 . Each component INLINEFORM3 of the attention distributions
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 750.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "a6c1cfab37b756275380368b1d9f8cdb8929f57e": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1810.00663:10:4": [
        [
          0,
          254
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-dc1fe2e449ffe25317cd865831664d7fd9b09469caf7e99a9824a9443bb28a44

Passage ID: `qasper-passage-v1-dc1fe2e449ffe25317cd865831664d7fd9b09469caf7e99a9824a9443bb28a44`; retrieval score: 8.98470263663418.

Word count: 150.

```text
for facial landmark localization, we use their pretrained CNN consisting of convolutional layers, including unshared and fully-connected layers, to predict gender and age from both the profile and shared images. We evaluate the performance for gender and age prediction task on INLINEFORM0 and INLINEFORM1 respectively as shown in Table TABREF42 and Table TABREF44 .

Demographic Prediction Analysis:

We delve deeper into the benefits and drawbacks of each data modality for demographic information prediction. This is crucial as the differences between language cues between age groups above age 35 tend to become smaller (see Figure FIGREF39 -A,B,C) and making the prediction harder for older people BIBREF74 . In this case, the other data modality (e.g., visual content) can play integral role as a complementary source for age inference. For gender prediction (see Table TABREF44 ), on average, the profile image-based predictor provides a more accurate prediction for both the depressed and
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-2f5d0306722c545f928f29cff93ce5b2df17d952c132950db53acd08ef6bfd1f

Passage ID: `qasper-passage-v1-2f5d0306722c545f928f29cff93ce5b2df17d952c132950db53acd08ef6bfd1f`; retrieval score: 8.613088449862296.

Word count: 150.

```text
We now provide an in-depth analysis of visual and textual content of vulnerable users.

Visual Content Analysis: We show that the visual content in images from posts as well as profiles provide valuable psychological cues for understanding a user's depression status. Profile/posted images can surface self-stigmatization BIBREF53 . Additionally, as opposed to typical computer vision framework for object recognition that often relies on thousands of predetermined low-level features, what matters more for assessing user's online behavior is the emotions reflected in facial expressions BIBREF54 , attributes contributing to the computational aesthetics BIBREF55 , and sentimental quotes they may subscribe to (Figure FIGREF15 ) BIBREF8 .

Facial Presence:

For capturing facial presence, we rely on BIBREF56 's approach that uses multilevel convolutional coarse-to-fine network cascade to tackle facial landmark localization. We identify facial presentation, emotion from facial expression, and demographic features from profile/posted images . Table TABREF21 illustrates facial presentation differences
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-e9b8ee2a4570f81f38cd7228f1336a8a20e53fd17d0799347a4d20bce3bfa120

Passage ID: `qasper-passage-v1-e9b8ee2a4570f81f38cd7228f1336a8a20e53fd17d0799347a4d20bce3bfa120`; retrieval score: 7.520332458722571.

Word count: 150.

```text
other data modality (e.g., visual content) can play integral role as a complementary source for age inference. For gender prediction (see Table TABREF44 ), on average, the profile image-based predictor provides a more accurate prediction for both the depressed and control class (0.92 and 0.90) compared to content-based predictor (0.82). For age prediction (see Table TABREF42 ), textual content-based predictor (on average 0.60) outperforms both of the visual-based predictors (on average profile:0.51, Media:0.53).

However, not every user provides facial identity on his account (see Table TABREF21 ). We studied facial presentation for each age-group to examine any association between age-group, facial presentation and depressive behavior (see Table TABREF43 ). We can see youngsters in both depressed and control class are not likely to present their face on profile image. Less than 3% of vulnerable users between 11-19 years reveal their facial identity. Although content-based gender predictor was not as accurate
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-12d49152461f734e971c361d3a212f1721ced7e58854682e53e1545e7d5ac07a

Passage ID: `qasper-passage-v1-12d49152461f734e971c361d3a212f1721ced7e58854682e53e1545e7d5ac07a`; retrieval score: 6.834277774969539.

Word count: 150.

```text
We leverage both the visual and textual content for predicting age and gender.

Prediction with Textual Content:

We employ BIBREF73 's weighted lexicon of terms that uses the dataset of 75,394 Facebook users who shared their status, age and gender. The predictive power of this lexica was evaluated on Twitter, blog, and Facebook, showing promising results BIBREF73 . Utilizing these two weighted lexicon of terms, we are predicting the demographic information (age or gender) of INLINEFORM0 (denoted by INLINEFORM1 ) using following equation: INLINEFORM2

where INLINEFORM0 is the lexicon weight of the term, and INLINEFORM1 represents the frequency of the term in the user generated INLINEFORM2 , and INLINEFORM3 measures total word count in INLINEFORM4 . As our data is biased toward young people, we report age prediction performance for each age group separately (Table TABREF42 ). Moreover, to measure the average accuracy of this model, we build a balanced
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-48b5abf0b305f96c6cb235318f9589034b5e3bd219f2a4456690b2ddcc7d618d

Passage ID: `qasper-passage-v1-48b5abf0b305f96c6cb235318f9589034b5e3bd219f2a4456690b2ddcc7d618d`; retrieval score: 6.738575620662171.

Word count: 150.

```text
total word count in INLINEFORM4 . As our data is biased toward young people, we report age prediction performance for each age group separately (Table TABREF42 ). Moreover, to measure the average accuracy of this model, we build a balanced dataset (keeping all the users above 23 -416 users), and then randomly sampling the same number of users from the age ranges (11,19] and (19,23]. The average accuracy of this model is 0.63 for depressed users and 0.64 for control class. Table TABREF44 illustrates the performance of gender prediction for each class. The average accuracy is 0.82 on INLINEFORM5 ground-truth dataset.

Prediction with Visual Imagery:

Inspired by BIBREF56 's approach for facial landmark localization, we use their pretrained CNN consisting of convolutional layers, including unshared and fully-connected layers, to predict gender and age from both the profile and shared images. We evaluate the performance for gender and age prediction task
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 750.

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

#### Rank 1: qasper-passage-v1-7319427fa15482cac7ce9ef3a1ac527f58110f48be3a589974d720fafc8d7323

Passage ID: `qasper-passage-v1-7319427fa15482cac7ce9ef3a1ac527f58110f48be3a589974d720fafc8d7323`; retrieval score: 4.701295768961641.

Word count: 150.

```text
E17-1101 showed that given input with author traits like gender, it is possible to retain those traits in Statistical Machine Translation (SMT) models. W17-4727 showed that incorporating morphological analysis in the decoder improves NMT performance for morphologically rich languages. burlot:hal-01618387 presented a new protocol for evaluating the morphological competence of MT systems, indicating that current translation systems only manage to capture some morphological phenomena correctly. Regarding the application of constraints in NMT, N16-1005 presented a method for controlling the politeness level in the generated output. DBLP:journals/corr/FiclerG17aa showed how to guide a neural text generation system towards style and content parameters like the level of professionalism, subjective/objective, sentiment and others. W17-4811 showed that incorporating more context when translating subtitles can improve the coherence of the generated translations. Most closely to our work, vanmassenhove-hardmeier-way:2018:EMNLP also addressed the missing gender information by training proprietary models with a gender-indicating-prefix. We differ from this work
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-4000477710ba46ab5b15306e9b00db74d048f5e3adc1e60ff11121434d7d5f8b

Passage ID: `qasper-passage-v1-4000477710ba46ab5b15306e9b00db74d048f5e3adc1e60ff11121434d7d5f8b`; retrieval score: 2.956733539104393.

Word count: 102.

```text
Closely related to our work, vanmassenhove-hardmeier-way:2018:EMNLP proposed a method and an English-French test set to evaluate gender-aware translation, based on the Europarl corpus BIBREF7 . We evaluate our method (using Google Translate and the given prefixes) on their test set to see whether it is applicable to another language pair and domain. Table shows the results of our approach vs. their published results and the Google Translate baseline. As may be expected, Google Translate outperforms their system as it is trained on a different corpus and may use more complex machine translation models. Using our method improves the BLEU score even further.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-1795d90b030e56c1117cda9898a766a91a8f40d6c522f339e792aef5632a3e8d

Passage ID: `qasper-passage-v1-1795d90b030e56c1117cda9898a766a91a8f40d6c522f339e792aef5632a3e8d`; retrieval score: 2.8170764962108614.

Word count: 135.

```text
to the given hint, even when no other evidence is available on the source side. While adding those hints results in additional text on the target side, we show that it is simple to remove, leaving only the desired translation.

Our method is appealing as it only requires simple pre-and-post processing of the inputs and outputs, without considering the system internals, or requiring specific annotated data and training procedure as in previous work BIBREF1 . We show that in spite of its simplicity, it is effective in resolving many of the ambiguities and improves the translation quality in up to 2.3 BLEU when given the correct hints, which may be inferred from text metadata or other sources. Finally, we perform a fine-grained syntactic analysis of the translations generated using our method which shows its effectiveness.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-9a7adb2ad95d131d391eb394eb00a4d3774b49fd2df9458ffad04c4add4c6d79

Passage ID: `qasper-passage-v1-9a7adb2ad95d131d391eb394eb00a4d3774b49fd2df9458ffad04c4add4c6d79`; retrieval score: 2.7877785158598334.

Word count: 150.

```text
A common way for marking information about gender, number, and case in language is morphology, or the structure of a given word in the language. However, different languages mark such information in different ways – for example, in some languages gender may be marked on the head word of a syntactic dependency relation, while in other languages it is marked on the dependent, on both, or on none of them BIBREF0 . This morphological diversity creates a challenge for machine translation, as there are ambiguous cases where more than one correct translation exists for the same source sentence. For example, while the English sentence “I love language” is ambiguous with respect to the gender of the speaker, Hebrew marks verbs for the gender of their subject and does not allow gender-neutral translation. This allows two possible Hebrew translations – one in a masculine and the other in a feminine form.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-9cfbdd0a2fc2dbebe81f80a4a3300cffa4873813b76899875d55492e61544b34

Passage ID: `qasper-passage-v1-9cfbdd0a2fc2dbebe81f80a4a3300cffa4873813b76899875d55492e61544b34`; retrieval score: 2.5077074035820615.

Word count: 150.

```text
respect to the gender of the speaker, Hebrew marks verbs for the gender of their subject and does not allow gender-neutral translation. This allows two possible Hebrew translations – one in a masculine and the other in a feminine form. As a consequence, a sentence-level translator (either human or machine) must commit to the gender of the speaker, adding information that is not present in the source. Without additional context, this choice must be done arbitrarily by relying on language conventions, world knowledge or statistical (stereotypical) knowledge.

Indeed, the English sentence “I work as a doctor” is translated into Hebrew by Google Translate using the masculine verb form oved, indicating a male speaker, while “I work as a nurse” is translated with the feminine form ovedet, indicating a female speaker (verified on March 2019). While this is still an issue, there have been recent efforts to reduce it for specific
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 687.

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

#### Rank 1: qasper-passage-v1-011ef660c1e69a795ea0bff656fd1cf09ebfbffa65de704ac5782949508a4312

Passage ID: `qasper-passage-v1-011ef660c1e69a795ea0bff656fd1cf09ebfbffa65de704ac5782949508a4312`; retrieval score: 8.012082035996807.

Word count: 132.

```text
experts. The mixture of experts is the whole model. BIBREF10 introduce the idea of using multiple MoEs with their own gating networks as parts of a deep model. It is intuitive that the latter approach is more powerful, since complex problems may contain many sub-problems each requiring different experts. They also allude in their conclusion to the potential to introduce sparsity, turning MoEs into a vehicle for computational computation.

Our work builds on this use of MoEs as a general purpose neural network component. While BIBREF10 uses two stacked MoEs allowing for two sets of gating decisions, our convolutional application of the MoE allows for different gating decisions at each position in the text. We also realize sparse gating and demonstrate its use as a practical way to massively increase model capacity.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-4b4dad1b8c9458b9434607200db821033dc115833d3657eb559b06e89949ab32

Passage ID: `qasper-passage-v1-4b4dad1b8c9458b9434607200db821033dc115833d3657eb559b06e89949ab32`; retrieval score: 7.952537326807991.

Word count: 150.

```text
Another major performance concern in distributed computing is network bandwidth. Since the experts are stationary (see above) and the number of gating parameters is small, most of the communication involves sending the inputs and outputs of the experts across the network. To maintain computational efficiency, the ratio of an expert's computation to the size of its input and output must exceed the ratio of computational to network capacity of the computing device. For GPUs, this may be thousands to one. In our experiments, we use experts with one hidden layer containing thousands of RELU-activated units. Since the weight matrices in the expert have sizes INLINEFORM0 _ INLINEFORM1 _ INLINEFORM2 and INLINEFORM3 _ INLINEFORM4 _ INLINEFORM5 , the ratio of computation to input and output is equal to the size of the hidden layer. Conveniently, we can increase computational efficiency simply by using a larger hidden layer, or more hidden layers.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-0013e2d0f97eeab1c92935246f415ecdfb1ff290cdd39074a739765badca11aa

Passage ID: `qasper-passage-v1-0013e2d0f97eeab1c92935246f415ecdfb1ff290cdd39074a739765badca11aa`; retrieval score: 7.783106110314615.

Word count: 150.

```text
We have observed that the gating network tends to converge to a state where it always produces large weights for the same few experts. This imbalance is self-reinforcing, as the favored experts are trained more rapidly and thus are selected even more by the gating network. BIBREF10 describe the same phenomenon, and use a hard constraint at the beginning of training to avoid this local minimum. BIBREF13 include a soft constraint on the batch-wise average of each gate.

We take a soft constraint approach. We define the importance of an expert relative to a batch of training examples to be the batchwise sum of the gate values for that expert. We define an additional loss INLINEFORM0 , which is added to the overall loss function for the model. This loss is equal to the square of the coefficient of variation of the set of importance values, multiplied by a hand-tuned
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-8830ea64ff6c9467e0613a7ec8123d0ce9cc6eca365f8a283de35e16f54f52e6

Passage ID: `qasper-passage-v1-8830ea64ff6c9467e0613a7ec8123d0ce9cc6eca365f8a283de35e16f54f52e6`; retrieval score: 7.777113600738943.

Word count: 150.

```text
We add residual connections around all LSTM and MoE layers to encourage gradient flow BIBREF37 . Similar to GNMT, to effectively deal with rare words, we used sub-word units (also known as “wordpieces") BIBREF42 for inputs and outputs in our system.

We use a shared source and target vocabulary of 32K wordpieces. We also used the same beam search technique as proposed in BIBREF3 .

We train models with different numbers of experts in the MoE layers. In addition to a baseline model with no MoE layers, we train models with flat MoE layers containing 32 experts, and models with hierarchical MoE layers containing 512 and 2048 experts. The flat MoE layers use INLINEFORM0 and the hierarchical MoE models use INLINEFORM1 at each level of the gating network. Thus, each input is processed by exactly 4 experts in each MoE layer. Each expert in the MoE layer is a feed
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-1e2d5f741ec060358b549e9edc6981b7eb08c9c6a279419857fca4c01d662e6b

Passage ID: `qasper-passage-v1-1e2d5f741ec060358b549e9edc6981b7eb08c9c6a279419857fca4c01d662e6b`; retrieval score: 7.414367351567031.

Word count: 150.

```text
where: DISPLAYFORM0

To force each expert to receive the exact same number of examples, we introduce an alternative mask function, INLINEFORM0 , which operates over batches of input vectors. Instead of keeping the top INLINEFORM1 values per example, we keep the top INLINEFORM2 values per expert across the training batch, where INLINEFORM3 , so that each example is sent to an average of INLINEFORM4 experts. DISPLAYFORM0

As our experiments suggest and also observed in BIBREF38 , using a batchwise function during training (such as INLINEFORM0 ) requires modifications to the inference when we may not have a large batch of examples. Our solution to this is to train a vector INLINEFORM1 of per-expert threshold values to approximate the effects of the batchwise mask. We use the following mask at inference time: DISPLAYFORM0

To learn the threshold values, we apply an additional loss at training time which is minimized when the
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 732.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "79c6e303c769cf6b075f42fc27820b4a2f8ee791": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1701.06538:16:1": [
        [
          0,
          968
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-4b6807a6b695e9d9ba7b705e42fcf17f3df7cd57fd5406ea8a0eabf77d8f4a8b

Passage ID: `qasper-passage-v1-4b6807a6b695e9d9ba7b705e42fcf17f3df7cd57fd5406ea8a0eabf77d8f4a8b`; retrieval score: 6.976338479191049.

Word count: 150.

```text
and consequently the final prediction accuracy will be affected. This example demonstrates that the proposed STN works pretty well to help attend to more related opinion words given a particular aspect.

Some predictions of our model and those of LSTM and OURS w/o THA & STN are given in Table TABREF43 . The models incorporating attention-based opinion summary (i.e., OURS and OURS w/o THA & STN) can better determine if the commonly-used nouns are aspect terms or not (e.g. “device” in the first input), since they make decisions based on the global opinion information. Besides, they are able to extract some infrequent or even misspelled aspect terms (e.g. “survice” in the second input) based on the indicative clues provided by opinion words. For the last three cases, having aspects in coordinate structures (i.e. the third and the fourth) or long aspects (i.e. the fifth), our model can give precise predictions
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-60206c6cbc932fcc41be2634e73f90c9a80cdc24e9ce43cd753f2864ae57fa51

Passage ID: `qasper-passage-v1-60206c6cbc932fcc41be2634e73f90c9a80cdc24e9ce43cd753f2864ae57fa51`; retrieval score: 4.9543536061808116.

Word count: 150.

```text
and MIN do not rely on dependency parsing, instead, they employ attention mechanism to distill opinion information to help aspect extraction. Our framework consistently performs better than them. The gains presumably come from two perspectives: (1) In our model, the opinion summary is exploited after performing the selective transformation conditioned on the current aspect features, thus the summary can to some extent avoid the noise due to directly applying conventional attention. (2) Our model can discover some uncommon aspects under the guidance of some commonly-used aspects in coordinate structures by the history attention.

CRF with basic feature template is not strong, therefore, we add CRF-2 as another baseline. As shown in Table TABREF39 , CRF-2 with word embeddings achieves much better results than CRF-1 on all datasets. WDEmb, which is also an enhanced CRF-based method using additional dependency context embeddings, obtains superior performances than CRF-2. Therefore, the above comparison shows
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-499b4a906e0d35f0293191a7cfafc077b4945c734149954250dc47c6979e659c

Passage ID: `qasper-passage-v1-499b4a906e0d35f0293191a7cfafc077b4945c734149954250dc47c6979e659c`; retrieval score: 4.883447510786503.

Word count: 150.

```text
ATE as a sequence labeling problem or a token-level classification problem. Traditional sequence models such as Conditional Random Fields (CRFs) BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 , Long Short-Term Memory Networks (LSTMs) BIBREF6 and classification models such as Support Vector Machine (SVM) BIBREF7 have been applied to tackle the ATE task, and achieved reasonable performance. One drawback of these existing works is that they do not exploit the fact that, according to the task definition, aspect terms should co-occur with opinion-indicating words. Thus, the above methods tend to output false positives on those frequently used aspect terms in non-opinionated sentences, e.g., the word “restaurant” in “the restaurant was packed at first, so we waited for 20 minutes”, which should not be extracted because the sentence does not convey any opinion on it.

There are a few works that consider opinion terms when tackling the ATE task. BIBREF8 proposed Recursive
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-30f36083b53d174883baa020a57b92bd598a3a31b9f28d113fbe951dc2be3cdc

Passage ID: `qasper-passage-v1-30f36083b53d174883baa020a57b92bd598a3a31b9f28d113fbe951dc2be3cdc`; retrieval score: 4.453375503421187.

Word count: 150.

```text
As shown in Table TABREF39 , the proposed framework consistently obtains the best scores on all of the four datasets. Compared with the winning systems of SemEval ABSA, our framework achieves 5.0%, 1.6%, 1.4%, 1.3% absolute gains on INLINEFORM0 , INLINEFORM1 , INLINEFORM2 and INLINEFORM3 respectively.

Our framework can outperform RNCRF, a state-of-the-art model based on dependency parsing, on all datasets. We also notice that RNCRF does not perform well on INLINEFORM0 and INLINEFORM1 (3.7% and 3.9% inferior than ours). We find that INLINEFORM2 and INLINEFORM3 contain many informal reviews, thus RNCRF's performance degradation is probably due to the errors from the dependency parser when processing such informal texts.

CMLA and MIN do not rely on dependency parsing, instead, they employ attention mechanism to distill opinion information to help aspect extraction. Our framework consistently performs better than them. The gains presumably come from two perspectives: (1) In our model, the
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-6529ccc7ef5fd5a12122299120cd743e791f579bc69f3c7393f01b9eb36db361

Passage ID: `qasper-passage-v1-6529ccc7ef5fd5a12122299120cd743e791f579bc69f3c7393f01b9eb36db361`; retrieval score: 4.267025330613357.

Word count: 115.

```text
For more accurate aspect term extraction, we explored two important types of information, namely aspect detection history, and opinion summary. We design two components, i.e. truncated history attention, and selective transformation network. Experimental results show that our model dominates those joint extraction works such as RNCRF and CMLA on the performance of ATE. It suggests that the joint extraction sacrifices the accuracy of aspect prediction, although the ground-truth opinion words were annotated by these authors. Moreover, one should notice that those joint extraction methods do not care about the correspondence between the extracted aspect terms and opinion words. Therefore, the necessity of such joint extraction should be obelized, given the experimental findings in this paper.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 715.

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

#### Rank 1: qasper-passage-v1-d9584636483f32b2c1a171b6dad32578467ced44f7f1d44d318859cf2ca427b4

Passage ID: `qasper-passage-v1-d9584636483f32b2c1a171b6dad32578467ced44f7f1d44d318859cf2ca427b4`; retrieval score: 4.043092266035896.

Word count: 138.

```text
Here we use network and text analysis tools to compare causal attribution networks (Sec. "Comparing causal networks" ). Crucially, nodes in these networks are defined only by their written descriptions, and multiple written descriptions can represent the same conceptual entity. Thus, to understand how causal attribution networks can be combined, we introduce and analyze a method for fusing networks (Sec. "Fusing causal networks" ) that builds off both the network structure and associated text information and explicitly incorporates conceptual equivalencies. Lastly, in Sec. "Inferring the size of the causal attribution network" we use the degree of overlap in these networks as a means to infer the total size of the one underlying causal attribution network being explored by these data collection efforts, allowing us to better understand the size of collective space of cause-effect relationships held by humans.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-32223bb3175497669138f4984c123c69f567669e7b44fbaf328c9c992e17cb85

Passage ID: `qasper-passage-v1-32223bb3175497669138f4984c123c69f567669e7b44fbaf328c9c992e17cb85`; retrieval score: 3.980493549861205.

Word count: 150.

```text
We perform a descriptive analysis of the three datasets, comparing and contrasting their features and properties. We focus on two aspects, the network structure and the text information (the written descriptions associated with each node in the network). Understanding these data at these levels can inform efforts to combine different causal attribution networks (Sec. "Fusing causal networks" ).

Table 1 and Fig. 2 summarize network characteristics for the three causal attribution networks. We focus on standard measures of network structure, measuring the sizes, densities, motif structure, and connectedness of the three networks. Both Wikidata and ConceptNet, the two larger networks, are highly disconnected, amounting to collections of small components with low density. In contrast, IPRnet is smaller but comparatively more dense and connected, with higher average degree, fewer disconnected components, and more clustering (Table 1 ). All three networks are degree dissortative, meaning that high-degree nodes are more likely to
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-306851d9429362a84e1c53c28fcc1ed8bf1b3178902574d2a9f52f48d94526de

Passage ID: `qasper-passage-v1-306851d9429362a84e1c53c28fcc1ed8bf1b3178902574d2a9f52f48d94526de`; retrieval score: 3.9353610349756694.

Word count: 150.

```text
These causal attributions networks are separate efforts to map out the underlying or latent causal attribution network held collectively by humans. It is natural to then ask if these different efforts can be combined in an effective way. Fusing these networks together can provide a single causal attribution network for researchers to study.

At the most basic level, one can fuse these networks together simply by taking their union, defining a single network containing all the unique nodes and edges of the original networks. Unfortunately, nodes in these networks are identified by their sentences, and this graph union assumes that two nodes $i$ and $j$ are equivalent iff $s_i = s_j$ . This is overly restrictive as these sentences serve as descriptions of associated concepts, and we ideally want to combine nodes that represent the same concept even when their written descriptions differ. Indeed, even within a single network it
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-9f3864bed446886f9ec85ba56148d9ba145ce32ace9095e50d1597de23f672a2

Passage ID: `qasper-passage-v1-9f3864bed446886f9ec85ba56148d9ba145ce32ace9095e50d1597de23f672a2`; retrieval score: 3.7929129930833807.

Word count: 150.

```text
The construction of causal attribution networks generates important knowledge networks that may inform causal inference research and even help future AI systems to perform causal reasoning, but these networks are time-consuming and costly to generate, and to date no efforts have been made to combine different networks. Our work not only studies the potential for fusing different networks together, but also infers the overall size of the total causal attribution network being explored.

We used capture-recapture estimators to infer the number of nodes and links in the underlying causal attribution network, given the Wikidata and ConceptNet networks and using NetFUSES and a semantic similarity function to help account for semantically equivalent nodes within and between Wikidata and ConceptNet. The validity of these estimates depends on Wikidata and ConceptNet being independent samples of the underlying network. As with many practical applications of capture-recapture in wildlife ecology and other areas, here we
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-a524de1e04386eafa5ea7d81c44a8690966acf89a72bd8b681949125641abed6

Passage ID: `qasper-passage-v1-a524de1e04386eafa5ea7d81c44a8690966acf89a72bd8b681949125641abed6`; retrieval score: 3.5919588512722975.

Word count: 150.

```text
In this work we compare causal attribution networks derived from three datasets. A causal attribution dataset is a collection of text pairs that reflect cause-effect relationships proposed by humans (for example, “virus causes sickness”). These written statements identify the nodes of the network (see also our graph fusion algorithm for dealing with semantically equivalent statements) while cause-effect relationships form the directed edges (“virus” $\rightarrow $ “sickness”) of the causal attribution network.

We collected causal attribution networks from three sources of data: English Wikidata BIBREF11 , English ConceptNet BIBREF10 , and IPRnet BIBREF12 . Wikidata and ConceptNet, are large knowledge graphs that contain semantic links denoting many types of interactions, one of which is causal attribution, while IPRnet comes from an Amazon Mechanical Turk study in which crowd workers were prompted to provide causal relationships. Wikidata relations were gathered by running four search queries on the Wikidata API (query.wikidata.org). These queries
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1812.06038:0:0` | full | 0:515 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 738.

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

#### Rank 1: qasper-passage-v1-5a610a4f64853b0609e93272900d70cc126e69d8b44511c26b2c86134fa43496

Passage ID: `qasper-passage-v1-5a610a4f64853b0609e93272900d70cc126e69d8b44511c26b2c86134fa43496`; retrieval score: 5.304101609515416.

Word count: 86.

```text
We established strong baselines for two story narrative understanding datasets: CaTeRS and RED. We have shown that neural network-based models can outperform feature-based models with wide margins, and we conducted an ablation study to show that contextualized representation learning can boost performance of NN models. Further research can focus on more systematic study or build stronger NN models over the same datasets used in this work. Exploring possibilities to directly apply temporal relation extraction to enhance performance of story generation systems is another promising research direction.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-7901553c4bdcc4d16cb4f15c2a49e26758e2e6371e75090b90ed8281e5d1f548

Passage ID: `qasper-passage-v1-7901553c4bdcc4d16cb4f15c2a49e26758e2e6371e75090b90ed8281e5d1f548`; retrieval score: 5.234054439272289.

Word count: 126.

```text
The series of TempEval competitions BIBREF21 , BIBREF22 , BIBREF23 have attracted many research interests in predicting event temporal relations. Early attempts by BIBREF24 , BIBREF21 , BIBREF25 , BIBREF26 only use pair-wise classification models. State-of-the-art local methods, such as ClearTK BIBREF27 , UTTime BIBREF28 , and NavyTime BIBREF29 improve on earlier work by feature engineering with linguistic and syntactic rules. As we mention in the Section 2, CAEVO is the current state-of-the-art system for feature-based temporal event relation extraction BIBREF10 . It's widely used as the baseline for evaluating TB-Dense data. We adopt it as our baseline for evaluating CaTeRS and RED datasets. Additionally, several models BramsenDLB2006, ChambersJ2008, DoLuRo12, NingWuRo18, P18-1212 have successfully incorporated global inference to impose global prediction consistency such as temporal transitivity.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.11942:6:0` | full | 0:912 |

#### Rank 3: qasper-passage-v1-09d51b4969f905b2a523412f940a3b9d09a0a904f03477a3318b0472be22f16b

Passage ID: `qasper-passage-v1-09d51b4969f905b2a523412f940a3b9d09a0a904f03477a3318b0472be22f16b`; retrieval score: 4.860728229055078.

Word count: 69.

```text
Table TABREF25 contains the best hyper-parameters and Table TABREF26 contains micro-average F1 scores for both datasets on dev and test sets. We only consider positive pairs, i.e. correct predictions on NONE pairs are excluded for evaluation. In general, the baseline model CAEVO is outperformed by both NN models, and NN model with BERT embedding achieves the greatest performance. We now provide more detailed analysis and discussion for each dataset.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-a75a1fdc241926f8c26d70dde61ed8e8bbe8442403251e8d5e610fa3ad25d470

Passage ID: `qasper-passage-v1-a75a1fdc241926f8c26d70dde61ed8e8bbe8442403251e8d5e610fa3ad25d470`; retrieval score: 3.352808479334385.

Word count: 121.

```text
, the intersection of these two threads seems flimsy. To the best of our knowledge, no event relation extraction results have been reported on CaTeRS and RED.

We apply neural network models that leverage recent advances in contextualized embeddings (BERT BIBREF13 ) to event-event relation extraction tasks for CaTeRS and RED. Our goal in this paper is to increase understanding of how well the state-of-the-art event relation models work for story/narrative comprehension.

In this paper, we report the first results of event temporal relation extraction on two under-explored story comprehension datasets: CaTeRS and RED. We establish strong baselines with neural network models enhanced by recent breakthrough of contextualized embeddings, BERT BIBREF13 . We summarize the contributions of the paper as follows:
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-97e76c34a98990b366ecff45f61829a7bf8b786d6f4ceaec51f727ea645e075d

Passage ID: `qasper-passage-v1-97e76c34a98990b366ecff45f61829a7bf8b786d6f4ceaec51f727ea645e075d`; retrieval score: 3.3314661044106937.

Word count: 150.

```text
standard train, development, test sets, and only focus on the temporal relations.

The common issue of these two datasets is that they are not densely annotated – not every pair of events is annotated with a relation. We provide one way to handle negative (unannotated) pairs in this paper. When constructing negative examples, we take all event pairs that occur within the same or neighboring sentences with no annotations, labeling them as “NONE”. The negative to positive samples ratio is 1.00 and 11.5 for CaTeRS and RED respectively. Note that RED data has much higher negative ratio (as shown in Table TABREF16 ) because it contains longer articles, more complicated sentence structures, and richer entity types than CaTeRS where all stories consist of 5 (mostly short) sentences.

In both the development and test sets, we add all negative pairs as candidates for the relation prediction. During training, the number of
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 552.

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

#### Rank 1: qasper-passage-v1-3dbafd4a0c8c3c38a2e02d9b894b79d68444d3691bb675221d357aa26587171c

Passage ID: `qasper-passage-v1-3dbafd4a0c8c3c38a2e02d9b894b79d68444d3691bb675221d357aa26587171c`; retrieval score: 7.554378874458248.

Word count: 149.

```text
For low resource languages, parallel data may not be available. In this case, we rely only on monolingual data (e.g., Wikipedias). We estimate word translation probabilities from word embeddings of the two languages. Word vectors of these languages can be learned using fastText BIBREF14 and then are aligned into a shared space with English BIBREF15, BIBREF16. Unlike learning contextualized representations, learning word vectors is fast and computationally cheap. Given the aligned vectors $\bar{}_f$ of foreign and $\bar{}_e$ of English, we calculate the word translation matrix $\in ^{|V_f|\times |V_e|}$ as

Here, we use $\mathrm {sparsemax}$ BIBREF17 instead of softmax. Sparsemax is a sparse version of softmax and it puts zero probabilities on most of the word in the English vocabulary except few English words that are similar to a given foreign word. This property is desirable in our approach since it leads to a better initialization of the foreign embeddings.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-01296b2ec139d5ab5ef8131c31611dd38e70f6ba0d1cf578abd8db360f5d4e89

Passage ID: `qasper-passage-v1-01296b2ec139d5ab5ef8131c31611dd38e70f6ba0d1cf578abd8db360f5d4e89`; retrieval score: 7.134740186293591.

Word count: 150.

```text
We evaluate our approach for six target languages: French (fr), Russian (ru), Arabic (ar), Chinese (zh), Hindi (hi), and Vietnamese (vi). These languages belong to four different language families. French, Russian, and Hindi are Indo-European languages, similar to English. Arabic, Chinese, and Vietnamese belong to Afro-Asiatic, Sino-Tibetan, and Austro-Asiatic family respectively. The choice of the six languages also reflects different training conditions depending on the amount of monolingual data. French and Russian, and Arabic can be regarded as high resource languages whereas Hindi has far less data and can be considered as low resource.

For experiments that use parallel data to initialize foreign specific parameters, we use the same datasets in the work of BIBREF6. Specifically, we use United Nations Parallel Corpus BIBREF18 for en-ru, en-ar, en-zh, and en-fr. We collect en-hi parallel data from IIT Bombay corpus BIBREF19 and en-vi data from OpenSubtitles 2018. For experiments that use only
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2002.07306:8:0` | full | 0:649 |

#### Rank 3: qasper-passage-v1-f064d9db4b41613c5c8a78e12d70986f85e83d53bda17edfc8010a2fab849cb5

Passage ID: `qasper-passage-v1-f064d9db4b41613c5c8a78e12d70986f85e83d53bda17edfc8010a2fab849cb5`; retrieval score: 6.363177841892634.

Word count: 150.

```text
Pre-trained models BIBREF0, BIBREF1 have received much of attention recently thanks to their impressive results in many down stream NLP tasks. Additionally, multilingual pre-trained models enable many NLP applications for other languages via zero-short cross-lingual transfer. Zero-shot cross-lingual transfer has shown promising results for rapidly building applications for low resource languages. BIBREF2 show the potential of multilingual-BERT BIBREF0 in zero-shot transfer for a large number of languages from different language families on five NLP tasks, namely, natural language inference, document classification, named entity recognition, part-of-speech tagging, and dependency parsing.

Although multilingual models are an important ingredient for enhancing language technology in many languages, recent research on improving pre-trained models puts much emphasis on English BIBREF3, BIBREF4, BIBREF5. The current state of affairs makes it difficult to translate advancements in pre-training from English to non-English languages. To our best knowledge, there are only three available multilingual pre-trained models to date: (1)
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-5e68a56d44967bdf9c4ca9d499e2b621983b1dadbc99eb9c8c77716b2c3e86a5

Passage ID: `qasper-passage-v1-5e68a56d44967bdf9c4ca9d499e2b621983b1dadbc99eb9c8c77716b2c3e86a5`; retrieval score: 5.999199822837307.

Word count: 150.

```text
Table TABREF32 shows the XNLI test accuracy. For reference, we also include the scores from the previous work, notably the state-of-the-art system XLM BIBREF6. Before discussing the results, we spell out that the fairest comparison in this experiment is the comparison between mBERT and RAMEN$_{\textsc {base}}$+BERT trained with monolingual only.

We first discuss the transfer results from BERT. Initialized from fastText vectors, RAMEN$_{\textsc {base}}$ slightly outperforms mBERT by 1.9 points on average and widen the gap of 3.3 points on Arabic. RAMEN$_{\textsc {base}}$ gains extra 0.8 points on average when initialized from parallel data. With triple number of parameters, RAMEN$_{\textsc {large}}$ offers an additional boost in term of accuracy and initialization with parallel data consistently improves the performance. It has been shown that BERT$_{\textsc {large}}$ significantly outperforms BERT$_{\textsc {base}}$ on 11 English NLP tasks BIBREF0, the strength of BERT$_{\textsc {large}}$ also shows up when adapted to foreign languages.

Transferring from
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-550640a77806216aa43609a4772838b09930f4e08291f3f50250b1f74e206a1b

Passage ID: `qasper-passage-v1-550640a77806216aa43609a4772838b09930f4e08291f3f50250b1f74e206a1b`; retrieval score: 3.80026611451788.

Word count: 150.

```text
We evaluate the performance of RAMEN+RoBERTa$_{\textsc {base}}$ (initialized from monolingual data) at each training steps: initialization of word embeddings (0K update), fine-tuning target embeddings (25K), and fine-tuning the model on both English and target language (at each 25K updates). The results are presented in Figure FIGREF40.

Without fine-tuning, the average accuracy of XLNI is 39.7% for a three-ways classification task, and the average LAS score is 3.6 for dependency parsing. We see the biggest leap in the performance after 50K updates. While semantic similarity task profits significantly at 25K updates of the target embeddings, syntactic task benefits with further fine-tuning the encoder. This is expected since the target languages might exhibit different syntactic structures than English and fine-tuning encoder helps to capture language specific structures. We observe a substantial gain of 19-30 LAS for all languages except French after 50K updates.

Language similarities have more impact on transferring syntax than
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 749.

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

#### Rank 1: qasper-passage-v1-17e22a8d50d110a27537e5ad20761ab604537a41bc4b597b645be9282cc88e00

Passage ID: `qasper-passage-v1-17e22a8d50d110a27537e5ad20761ab604537a41bc4b597b645be9282cc88e00`; retrieval score: 5.719180775943382.

Word count: 94.

```text
imaging is affected by speaker variation, and how severe degradations in performance can be avoided when applying systems to data from previously unseen speakers through the use of speaker adaptation and speaker normalization approaches.

Below, we present the main challenges associated with the automatic processing of ultrasound data, together with a review of speaker-independent models applied to UTI. Following this, we present the experiments that we have performed (Section SECREF2 ), and discuss the results obtained (Section SECREF3 ). Finally we propose some future work and conclude the paper (Sections SECREF4 and SECREF5 ).
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-33c49911c9076513b3d34e24c185edff8d4f33bf405424bc6398998b9a0ba1fa

Passage ID: `qasper-passage-v1-33c49911c9076513b3d34e24c185edff8d4f33bf405424bc6398998b9a0ba1fa`; retrieval score: 5.695936867254469.

Word count: 150.

```text
We use the Ultrax Typically Developing dataset (UXTD) from the publicly available UltraSuite repository BIBREF19 . This dataset contains synchronized acoustic and ultrasound data from 58 typically developing children, aged 5-12 years old (31 female, 27 male). The data was aligned at the phone-level, according to the methods described in BIBREF19 , BIBREF25 . For this work, we discarded the acoustic data and focused only on the B-Mode ultrasound images capturing a midsaggital view of the tongue. The data was recorded using an Ultrasonix SonixRP machine using Articulate Assistant Advanced (AAA) software at INLINEFORM0 121fps with a 135 field of view. A single ultrasound frame consists of 412 echo returns from each of the 63 scan lines (63x412 raw frames). For this work, we only use UXTD type A (semantically unrelated words, such as pack, tap, peak, tea, oak, toe) and type B (non-words designed to elicit the articulation of
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1907.01413:3:0` | partial | 0:934 |

#### Rank 3: qasper-passage-v1-880e5b19cc8b731d352d2100dbcb1413a829cd08b1793239af5d0fe203da639b

Passage ID: `qasper-passage-v1-880e5b19cc8b731d352d2100dbcb1413a829cd08b1793239af5d0fe203da639b`; retrieval score: 5.6195525112551845.

Word count: 150.

```text
images in order to assist SLTs, who currently largely rely on manual processing when using articulatory imaging in speech therapy. One task that could assist SLTs is the automatic classification of tongue shapes from raw ultrasound. This can facilitate the diagnosis and treatment of speech sound disorders, by allowing SLTs to automatically identify incorrect articulations, or by quantifying patient progress in therapy. In addition to being directly useful for speech therapy, the classification of tongue shapes enables further understanding of phonetic variability in ultrasound tongue images. Much of the previous work in this area has focused on speaker-dependent models. In this work we investigate how automatic processing of ultrasound tongue imaging is affected by speaker variation, and how severe degradations in performance can be avoided when applying systems to data from previously unseen speakers through the use of speaker adaptation and speaker normalization approaches.

Below, we present the main challenges
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-5110f79426e270acd8a5fdc298cd5d7d0fa78c6b8148d5477184843b858d7940

Passage ID: `qasper-passage-v1-5110f79426e270acd8a5fdc298cd5d7d0fa78c6b8148d5477184843b858d7940`; retrieval score: 4.137880973026296.

Word count: 71.

```text
2 fully-connected ReLU layers with 512 nodes. The convolutional layers use 16 filters, 8x8 and 4x4 kernels respectively, and rectified units. The fully-connected layers use dropout with a drop probability of 0.2. Because CNN systems take longer to converge, they are optimized over 200 epochs. For all systems, at the end of every epoch, the model is evaluated on the development set, and the best model across all epochs is kept.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-91adb9fd247e1584efb6ac38e974d510071e7e9e43eb7b4797cd544a13a6460b

Passage ID: `qasper-passage-v1-91adb9fd247e1584efb6ac38e974d510071e7e9e43eb7b4797cd544a13a6460b`; retrieval score: 3.913975325680093.

Word count: 109.

```text
In this paper, we have investigated speaker-independent models for the classification of phonetic segments from raw ultrasound data. We have shown that the performance of the models heavily degrades when evaluated on data from unseen speakers. This is a result of the variability in ultrasound images, mostly due to differences across speakers, but also due to shifts in probe placement. Using the mean of all ultrasound frames for a new speaker improves the generalization of the models to unseen data, especially when using convolutional neural networks. We have also shown that adapting a pre-trained speaker-independent system using as few as 50 ultrasound frames can outperform a corresponding speaker-dependent system.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 574.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "2cc03c335d671b820b4f04b30bbdd522332ff8ec": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1907.01413:3:0": [
        [
          934,
          986
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-2248b740217a1135c3cd1bbd31d64766f5a88ace4050144827300c64936500f0

Passage ID: `qasper-passage-v1-2248b740217a1135c3cd1bbd31d64766f5a88ace4050144827300c64936500f0`; retrieval score: 7.67308213330058.

Word count: 90.

```text
In our experiments we aim to answer the following research questions (RQs):

RQ1: How does the number of training iterations in the BERT language model finetuning stage influence the ATSC end-task performance? At what point does performance start to improve, when does it converge?

RQ2: When trained in-domain, what ATSC end-task performance can be reached through fully exploitet finetuning of the BERT language model?

RQ3: When trained cross-domain in the special case of domain adaptation, what ATSC end-task performance can be reached if BERT language model finetuning is fully exploitet?
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-b288bba6ddd004b87a009ce010ba3a4b4b0f21054583dad7bd24cb55145f4d2f

Passage ID: `qasper-passage-v1-b288bba6ddd004b87a009ce010ba3a4b4b0f21054583dad7bd24cb55145f4d2f`; retrieval score: 4.00307416419084.

Word count: 150.

```text
The results of our experiments are shown in fig:acc-dep-lmiterations and tab:results respectively.

To answer RQ1, which is concerned with details on domain-specific language model finetuning, we can see in fig:acc-dep-lmiterations that first of all, language model finetuning has a substantial effect on ATSC end-task performance. Secondly, we see that in the laptops domain the performance starts to increase at about 10 Mio. finetuned sentences. This is an interesting insight as one would expect a relation closer to a logarithmic curve. One reason might be that it takes many steps to train knowledge into the BERT language model due to its vast amount of parameters. The model already converges at around 17 Mio. sentences. More finetuning does not improve performance significantly. In addition, we find that different runs have a high variance, the standard deviation amounts to about $1\%$ in accuracy, which justifies averaging over 9 runs to measure differences in
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-116049912e9dc4bd39c652aba2cbfb662a6300184af56ec24454bc080e41681c

Passage ID: `qasper-passage-v1-116049912e9dc4bd39c652aba2cbfb662a6300184af56ec24454bc080e41681c`; retrieval score: 3.68701840196464.

Word count: 111.

```text
compared to 3 epochs for the restaurants domain, so that the BERT model trains on about 30 million sentences in both cases. This means that 1 sentence can be seen multiple times with a different language model masking.

We also create a mixed corpus to jointly finetune both domains. Here, we sample 1 Mio. restaurant reviews and combine them with the laptop reviews. This results in about 2 Mio. reviews that are finetuned for 15 epochs. The exact statistics for the three finetuning corpora are shown in the top of tab:datasets.

To be able to reproduce our finetuning corpora, we make the code that is used to generate them available online.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-f076a569e7ae1595c5837d85a416137a4bfd89701cec0f769024724c3dcd751a

Passage ID: `qasper-passage-v1-f076a569e7ae1595c5837d85a416137a4bfd89701cec0f769024724c3dcd751a`; retrieval score: 3.645949105757869.

Word count: 99.

```text
make use of left- and right-sided context independently.

BIBREF8 proposed Attention Encoder Networks (AEN), a modification to the transformer architecture. The authors split the Multi-Head Attention (MHA) layers into Intra-MHA and Inter-MHA layers in order to model target words and context differently, which results in a more lightweight model compared to the transformer architecture.

Another recent performance leap was achieved by BIBREF11, who model dependencies between sentiment words explicitly in sentences with more than one aspect-target by using a graph convolutional neural network. They show that their architecture performs particularly well if multiple aspects are present in a sentence.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-2de89121272e88177da80681f5a4c471f5e20dc400b5d33cc773bb85d802e759

Passage ID: `qasper-passage-v1-2de89121272e88177da80681f5a4c471f5e20dc400b5d33cc773bb85d802e759`; retrieval score: 3.348529513611317.

Word count: 109.

```text
BERT and XLNet models on the down-stream task of ATSC we use mixed 16 bit and 32 bit floating point computations, the Adam optimizer, and a learning rate of $3\cdot 10^{-5}$ and a batchsize of 32. We train the model for a total of 7 epochs. The validation accuracy converges after about 3 epochs of training on all datasets, but training loss still improves after that.

It is important to note that all our results reported are the average of 9 runs with different random initializations. This is needed to measure significance of improvements, as the standard deviation in accuray amounts to roughly $1\%$ for all experiments, see fig:acc-dep-lmiterations.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 559.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "46773036407495e12fc0be2224060db32f6d6676": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1908.11860:19:2": [
        [
          0,
          1456
        ]
      ],
      "1908.11860:19:4": [
        [
          0,
          366
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-f7bdfa4dd278fa4c082b4d1273c036308c9b59e0cb6bb1d0429ad9d9ef426784

Passage ID: `qasper-passage-v1-f7bdfa4dd278fa4c082b4d1273c036308c9b59e0cb6bb1d0429ad9d9ef426784`; retrieval score: 6.74083803035016.

Word count: 150.

```text
all of these datasets are tailored towards context-independent embeddings and thus not suitable for evaluating our proposed model. Furthermore, understanding rare words is of negligible importance for most commonly used downstream task datasets. To evaluate our proposed model, we therefore introduce a novel procedure that allows us to automatically turn arbitrary text classification datasets into ones where rare words are guaranteed to be important. This is achieved by replacing classification-relevant frequent words with rare synonyms obtained using semantic resources such as WordNet BIBREF20.

Using this procedure, we extract rare word datasets from three commonly used text (or text pair) classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. On both the WNLaMPro dataset of BIBREF0 and all three so-obtained datasets, our proposed Bertram model outperforms previous work by a large margin.

In summary, our contributions are as follows:

We show that a pretrained BERT instance can be integrated into
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-97224258da7b862963e6116b72ac5e82fa1570a902d6131244964a9a02f15c84

Passage ID: `qasper-passage-v1-97224258da7b862963e6116b72ac5e82fa1570a902d6131244964a9a02f15c84`; retrieval score: 4.639517149147078.

Word count: 150.

```text
for understanding rare words that combines a pretrained BERT language model with Attentive Mimicking BIBREF19. Unlike previous approaches making use of language models BIBREF5, our approach integrates BERT in an end-to-end fashion and directly makes use of its hidden states. By giving Bertram access to both surface form and context information already at its very lowest layer, we allow for a deep connection and exchange of information between both input signals.

For various reasons, assessing the effectiveness of methods like Bertram in a contextualized setting poses a huge difficulty: While most previous work on rare words was evaluated on datasets explicitly focusing on such words BIBREF6, BIBREF3, BIBREF4, BIBREF5, BIBREF10, all of these datasets are tailored towards context-independent embeddings and thus not suitable for evaluating our proposed model. Furthermore, understanding rare words is of negligible importance for most commonly used downstream task datasets. To evaluate our proposed model, we therefore
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-bd6932dce3e239bc6b51886dca939bc19df69ce80071839b50d9a46ebe938be5

Passage ID: `qasper-passage-v1-bd6932dce3e239bc6b51886dca939bc19df69ce80071839b50d9a46ebe938be5`; retrieval score: 4.5494554503106475.

Word count: 121.

```text
both the WNLaMPro dataset of BIBREF0 and all three so-obtained datasets, our proposed Bertram model outperforms previous work by a large margin.

In summary, our contributions are as follows:

We show that a pretrained BERT instance can be integrated into Attentive Mimicking, resulting in much better context representations and a deeper connection of form and context.

We design a procedure that allows us to automatically transform text classification datasets into datasets for which rare words are guaranteed to be important.

We show that Bertram achieves a new state-of-the-art on the WNLaMPro probing task BIBREF0 and beats all baselines on rare word instances of AG's News, MNLI and DBPedia, resulting in an absolute improvement of up to 24% over a BERT baseline.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-4c0cb635d57452de2877e9427a2c37a8e046263d48720b49e19d379ff73a08fd

Passage ID: `qasper-passage-v1-4c0cb635d57452de2877e9427a2c37a8e046263d48720b49e19d379ff73a08fd`; retrieval score: 4.160734783806723.

Word count: 141.

```text
We have introduced Bertram, a novel architecture for relearning high-quality representations of rare words. This is achieved by employing a powerful pretrained language model and deeply connecting surface-form and context information. By replacing important words with rare synonyms, we have created various downstream task datasets focusing on rare words; on all of these datasets, Bertram improves over a BERT model without special handling of rare words, demonstrating the usefulness of our proposed method.

As our analysis has shown that even for the most frequent words considered, using Bertram is still beneficial, future work might further investigate the limits of our proposed method. Furthermore, it would be interesting to explore more complex ways of incorporating surface-form information – e.g., by using a character-level CNN similar to the one of BIBREF27 – to balance out the potency of Bertram's form and context parts.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-03c5953de619d61ed776d6f50e53a38a47325793a2be80b5129b0b16ca672998

Passage ID: `qasper-passage-v1-03c5953de619d61ed776d6f50e53a38a47325793a2be80b5129b0b16ca672998`; retrieval score: 3.9969431124317185.

Word count: 60.

```text
and train Bertram on only the much smaller Westbury Wikipedia Corpus (WWC) BIBREF33; this of course gives BERT a clear advantage over our proposed method. In order to at least partially compensate for this, in our downstream task experiments we gather the set of contexts $\mathcal {C}$ for a given rare word from both the WWC and BooksCorpus during inference.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 622.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "709376b155cf4c245d587fd6177d3ce8b4e23a32": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1910.07181:11:0": [
        [
          0,
          1092
        ]
      ]
    }
  },
  "a7eec1f4a5f97265f08cfd09b1cec20b97c573f6": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1910.07181:11:0": [
        [
          0,
          1092
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-bd6932dce3e239bc6b51886dca939bc19df69ce80071839b50d9a46ebe938be5

Passage ID: `qasper-passage-v1-bd6932dce3e239bc6b51886dca939bc19df69ce80071839b50d9a46ebe938be5`; retrieval score: 6.68835121134878.

Word count: 121.

```text
both the WNLaMPro dataset of BIBREF0 and all three so-obtained datasets, our proposed Bertram model outperforms previous work by a large margin.

In summary, our contributions are as follows:

We show that a pretrained BERT instance can be integrated into Attentive Mimicking, resulting in much better context representations and a deeper connection of form and context.

We design a procedure that allows us to automatically transform text classification datasets into datasets for which rare words are guaranteed to be important.

We show that Bertram achieves a new state-of-the-art on the WNLaMPro probing task BIBREF0 and beats all baselines on rare word instances of AG's News, MNLI and DBPedia, resulting in an absolute improvement of up to 24% over a BERT baseline.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-6dddd2d44e49bb5936c8df2e8d62887bbf8e1de8b025f03c64cf785c91390fd8

Passage ID: `qasper-passage-v1-6dddd2d44e49bb5936c8df2e8d62887bbf8e1de8b025f03c64cf785c91390fd8`; retrieval score: 6.487909684994785.

Word count: 150.

```text
BIBREF15 and WordPiece embeddings BIBREF16, or even character-level CNNs BIBREF17 –, it is unclear whether these models even require special treatment of rare words. However, the listed methods only make use of surface-form information, whereas BIBREF9 found that for covering a wide range of rare words, it is crucial to consider both surface-form and contexts.

Consistently, BIBREF0 recently showed that for BERT BIBREF13, a popular pretrained language model based on a Transformer architecture BIBREF18, performance on a rare word probing task can significantly be improve by relearning representations of rare words using Attentive Mimicking BIBREF19. However, their proposed model is limited in two important respects:

For processing contexts, it uses a simple bag-of-words model, throwing away much of the available information.

It combines form and context only in a shallow fashion, thus preventing both input signals from sharing information in any sophisticated manner.

Importantly, this limitation applies not only to
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-63e17e1bd6a7cbd5efa3bbe3774d56327028509e9d0f51f328b6f6158412f127

Passage ID: `qasper-passage-v1-63e17e1bd6a7cbd5efa3bbe3774d56327028509e9d0f51f328b6f6158412f127`; retrieval score: 5.5228950801734165.

Word count: 150.

```text
We evalute Bertram on the WNLaMPro dataset of BIBREF0. This dataset consists of cloze-style phrases like

and the task is to correctly fill the slot (____) with one of several acceptable target words (e.g., “fruit”, “bush” and “berry”), which requires knowledge of the phrase's keyword (“lingonberry” in the above example). As the goal of this dataset is to probe a language model's ability to understand rare words without any task-specific finetuning, BIBREF0 do not provide a training set. Furthermore, the dataset is partitioned into three subsets; this partition is based on the frequency of the keyword, with keywords occurring less than 10 times in the WWC forming the rare subset, those occurring between 10 and 100 times forming the medium subset, and all remaining words forming the frequent subset. As our focus is on improving representations for rare words, we evaluate our model only on the former two sets.

Results
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1910.07181:10:0` | full | 0:104 |

#### Rank 4: qasper-passage-v1-f7bdfa4dd278fa4c082b4d1273c036308c9b59e0cb6bb1d0429ad9d9ef426784

Passage ID: `qasper-passage-v1-f7bdfa4dd278fa4c082b4d1273c036308c9b59e0cb6bb1d0429ad9d9ef426784`; retrieval score: 4.611625883632815.

Word count: 150.

```text
all of these datasets are tailored towards context-independent embeddings and thus not suitable for evaluating our proposed model. Furthermore, understanding rare words is of negligible importance for most commonly used downstream task datasets. To evaluate our proposed model, we therefore introduce a novel procedure that allows us to automatically turn arbitrary text classification datasets into ones where rare words are guaranteed to be important. This is achieved by replacing classification-relevant frequent words with rare synonyms obtained using semantic resources such as WordNet BIBREF20.

Using this procedure, we extract rare word datasets from three commonly used text (or text pair) classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. On both the WNLaMPro dataset of BIBREF0 and all three so-obtained datasets, our proposed Bertram model outperforms previous work by a large margin.

In summary, our contributions are as follows:

We show that a pretrained BERT instance can be integrated into
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-accdacb804960fc85c12dedf78408eea84a961430a881a5c32dc373d782e110a

Passage ID: `qasper-passage-v1-accdacb804960fc85c12dedf78408eea84a961430a881a5c32dc373d782e110a`; retrieval score: 4.410523571518131.

Word count: 150.

```text
form and context leads to significantly better results than using just one of both input signals for a wide range of tasks. While all aforementioned methods are based on simple bag-of-words models, BIBREF5 recently proposed an architecture based on the context2vec language model BIBREF28. However, in contrast to our work, they (i) do not incorporate surface-form information and (ii) do not directly access the hidden states of the language model, but instead simply use its output distribution.

There are several datasets explicitly focusing on rare words, e.g. the Stanford Rare Word dataset of BIBREF6, the Definitional Nonce dataset of BIBREF3 and the Contextual Rare Word dataset BIBREF4. However, all of these datasets are only suitable for evaluating context-independent word representations.

Our proposed method of generating rare word datasets is loosely related to adversarial example generation methods such as HotFlip BIBREF29, which manipulate the input to change a model's prediction. We
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 721.

Fully covered answer annotations: 0055f1c704b2380b3f9692330601906890b9b49d.

Missing evidence by answer annotation:

```text
{
  "0055f1c704b2380b3f9692330601906890b9b49d": {
    "unresolved_evidence": [],
    "paragraphs": {}
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

#### Rank 1: qasper-passage-v1-c98a5140b4b53d41987c7afcb5d242c453c151aa3821290b59f4ccb73a49cbb7

Passage ID: `qasper-passage-v1-c98a5140b4b53d41987c7afcb5d242c453c151aa3821290b59f4ccb73a49cbb7`; retrieval score: 3.5281979269276076.

Word count: 123.

```text
The primary question we investigate with this model is what kind of input is best for generating accurate and informative citation sentences. Prior works in citation recommendation have made use of abstracts, which perhaps act as sufficient summaries of document content for this task. Additionally, we explore variants of extended context, such as the introduction or first section after the abstract. Since scientific texts are too long to fit into the context window of our generation model, we also investigate a “sampling” approach which samples sentences from throughout the document until the context window is full. In this work, we combine either the abstract or introduction of the source document with each of the abstract, introduction, or sampled sentences from the cited document.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-bb205a5b5bd5ea4e8129046079e04af61e63a027c945be081984ebc1de937718

Passage ID: `qasper-passage-v1-bb205a5b5bd5ea4e8129046079e04af61e63a027c945be081984ebc1de937718`; retrieval score: 3.3368274956707906.

Word count: 65.

```text
samples in each of 100 iterations. This test shows that conditioning on the introduction of the source document improves performance compared to conditioning on the abstract when using the SciGPT2 model. However, we see that IR methods perform better than the best neural models. We do not find enough evidence to reject the null hypothesis regarding what context from the cited document should be used.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2002.00317:7:3` | partial | 86:489 |

#### Rank 3: qasper-passage-v1-13027782e77b76e2b7ce87890df761c94827cd2611af22b0923060f42c6ac15e

Passage ID: `qasper-passage-v1-13027782e77b76e2b7ce87890df761c94827cd2611af22b0923060f42c6ac15e`; retrieval score: 3.0446603413896076.

Word count: 150.

```text
We compare the different baseline systems using BLEU BIBREF12, ROUGE (specifically ROUGE 1, 2, and L; BIBREF13), and the recently introduced BertScore BIBREF14, a similarity metric based on BERT embeddings which has been shown to correlate well with human judgements on other tasks. To adapt the BertScore metric to the scientific text domain, we use SciBERT embeddings.

Table TABREF7 (above the double line) shows the performance of the SciGPT2 model on the test set when provided with the different input context combinations outlined in Section SECREF5. We find that context does make a difference for this category of model, and that models which have access to the intro of the documents outperform those which use abstracts or sampling.

Automatic evaluation of the retrieval-based methods on the test data are shown below the double line in Table TABREF7. This table shows that the retrieval methods perform well on this task. However
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-e8f0c7e54bb4c2669c406e21adff27713ceea4d3e65aa2f4ffd893967228cfe6

Passage ID: `qasper-passage-v1-e8f0c7e54bb4c2669c406e21adff27713ceea4d3e65aa2f4ffd893967228cfe6`; retrieval score: 2.847167305435448.

Word count: 150.

```text
requires a model that can learn phrase meanings from very few exposures, an important but unsolved problem for text generation systems. Possibly more challenging is understanding and expressing the various and nuanced relationships between related scientific works.

In this work, we introduce the task of citation text generation. Leveraging the full texts of English-language scientific articles, we construct a dataset of citation sentences in the computer science domain for training and evaluating citation text generation models. We investigate strong retrieval and neural baseline models against which future work can compare. For use cases where large models can be trained, we extend the successful GPT2 architecture BIBREF6 to the scientific domain with additional pre-training and subsequent fine-tuning on the citation generation task. We experiment with different kinds of document context in the fine-tuning and inference stages. We also explore retrieval-based techniques which may more easily generalize to lower-resource settings. These models
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-aa19bdf43ce15931a49e775b110b6b9b6ac2c2d6dcd42110104cf20d37f4794b

Passage ID: `qasper-passage-v1-aa19bdf43ce15931a49e775b110b6b9b6ac2c2d6dcd42110104cf20d37f4794b`; retrieval score: 2.061036843710907.

Word count: 150.

```text
The fluency and topical relevance of the baseline models show the plausibility of the citation text generation task as well as the utility of including pretrained scientific language models in future models. But based on the kinds of errors we have seen, future work should focus on two complementary goals: ensuring the factual accuracy of the generated text and improved modeling of the cited document. Factual accuracy is difficult to enforce in statistical text generation systems, especially where inference includes sampling procedures. Grounding to knowledge bases could help. For this task, knowledge extracted from candidate generations could be compared with knowledge from the full source and cited documents to prune false or irrelevant statements. Further, modeling input documents as knowledge graphs of their contents may help these algorithms better understand the cited document, resulting in better outputs. However, such a model will have to address the open problem of combining
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 638.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "83bb414e88a59542134862e646f33922ed54f2a1": {
    "unresolved_evidence": [],
    "paragraphs": {
      "2002.00317:7:3": [
        [
          0,
          86
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-2ecbe6e44e9ea50ba73d67b5d6725a4a7d3b3b9fc50498d4e62b0cc85059ef53

Passage ID: `qasper-passage-v1-2ecbe6e44e9ea50ba73d67b5d6725a4a7d3b3b9fc50498d4e62b0cc85059ef53`; retrieval score: 6.999559049092487.

Word count: 150.

```text
The stock price data of Microsoft are labeled suitably for training using a simple program. If the previous day stock price is more than the current day stock price, the current day is marked with a numeric value of 0, else marked with a numeric value of 1. Now, this correlation analysis turns out to be a classification problem. The total positive, negative and neutral emotions in tweets in a 3 day period are calculated successively which are used as features for the classifier model and the output is the labeled next day value of stock 0 or 1.The window size is experimented and best results are achieved when the sentiment values precede 3 days to the stock price. A total of 355 instances, each with 3 attributes are fed to the classifier with a split proportions of 80% train dataset and the remaining dataset for testing. The accuracy of
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-db2e4ee3f8c83c71ff13b67c87bfa0261ba58d8084fb9ce78abc0632b1aa0912

Passage ID: `qasper-passage-v1-db2e4ee3f8c83c71ff13b67c87bfa0261ba58d8084fb9ce78abc0632b1aa0912`; retrieval score: 6.9040139914250975.

Word count: 150.

```text
The above sections discussed the method followed to train the classifier used for sentiment analysis of tweets. The classifier with features as Word2vec representations of human annotated tweets trained on Random Forest algorithm with a split percentage of 90 for training the model and remaining for testing the model showed an accuracy of 70.2%. With N-gram representations, the classifier model with same algorithm and with same dataset showed an accuracy of 70.5%. Though the results are very close, model trained with word2vec representations is picked to classify the nonhuman annotated tweets because of its promising accuracy for large datasets and the sustainability in word meaning. Numerous studies have been conducted on people and they concluded that the rate of human concordance, that is the degree of agreement among humans on the sentiment of a text, is between 70% and 79% BIBREF21 . They have also synthesized that sentiment analyzers above
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-ffa5c09dd77d4b51a5d050b9ba27e7dcc4182d1bc078870bf4d6e06bf1e5eae3

Passage ID: `qasper-passage-v1-ffa5c09dd77d4b51a5d050b9ba27e7dcc4182d1bc078870bf4d6e06bf1e5eae3`; retrieval score: 6.8651735082152.

Word count: 48.

```text
sentiment values precede 3 days to the stock price. A total of 355 instances, each with 3 attributes are fed to the classifier with a split proportions of 80% train dataset and the remaining dataset for testing. The accuracy of the classifier is discussed in the results section.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-5109991c63b88c593adc0180a8c3cd06f5dc4d6612d506d6b252901981a8aede

Passage ID: `qasper-passage-v1-5109991c63b88c593adc0180a8c3cd06f5dc4d6612d506d6b252901981a8aede`; retrieval score: 6.340155263919549.

Word count: 141.

```text
A classifier is presented in the previous sections that is trained with aggregate sentiment values for 3-day period as features and the increase/decrease in stock price represented by 1/0 as the output. Total data is split into two parts, 80 percent to train the model and remaining for testing operations. The classifier results show an accuracy value of 69.01% when trained using Logistic regression algorithm and the accuracy rate varied with the training set. When the model with LibSVM is trained with 90 percent of data, it gave a result of 71.82%. These results give a significant edge to the investors and they show good correlation between stock market movements and the sentiments of public expressed in twitter. This trend shows that with increasing dataset the models are performing well. We would like to incorporate more data in our future work.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-5c5d90b08d48463aad177d9605463409b7e08a4d2df24732be799014ed33a6f2

Passage ID: `qasper-passage-v1-5c5d90b08d48463aad177d9605463409b7e08a4d2df24732be799014ed33a6f2`; retrieval score: 5.313843428876983.

Word count: 125.

```text
In this work, we have considered only twitter data for analyzing people's sentiment which may be biased because not all the people who trade in stocks share their opinions on twitter. Stocktwits BIBREF22 is a financial communication platform designed solely for sharing ideas and insights of investors, entrepreneurs and traders. The current study can be extended by incorporating stocktwits data. In addition to this, data from news can also be included for an exhaustive public opinion collection.

While training the sentiment analyzer, 3,216 tweets are used which is comparatively a less number to train a sentiment analyzer. In future, we look forward to human annotate more than 10,000 tweets and train the classifiers. With increasing size of training datasets, the models tend to perform better.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 614.

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

#### Rank 1: qasper-passage-v1-aa7b4cbf2b9868e0900d04f7698ed8f11c97623db9b0cd903239baee89671dce

Passage ID: `qasper-passage-v1-aa7b4cbf2b9868e0900d04f7698ed8f11c97623db9b0cd903239baee89671dce`; retrieval score: 2.3469442615947456.

Word count: 79.

```text
While image and sound come with a natural high dimensional embedding, the issue of which is the best representation is still an open research problem in the context of natural language and text. It is beyond the scope of this paper to do a thorough overview of word representations, for this we refer the interest reader to the excellent review provided by BIBREF1 . Here, we will just introduce the main representations that are related to the proposed method.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-dbf1b5d1d914ff6a3c9923fed63a8b0791406482398af9e5cb00473602a33857

Passage ID: `qasper-passage-v1-dbf1b5d1d914ff6a3c9923fed63a8b0791406482398af9e5cb00473602a33857`; retrieval score: 2.0656450603657555.

Word count: 101.

```text
In this paper, we presented the network architecture used for the Fortia-FBK submission to the Semeval-2017 Task 5, Subtask 2 challenge, with the goal of predicting positive (bullish) or negative (bearish) attitude towards a target brand from financial news headlines. The proposed system ranked 1st in such challenge.

Our approach is based on 1d convolutions and uses fine-tuning of unsupervised word representations and a rule based sentiment model in its inputs. We showed that the use of pre-computed word representations allows to reduce over-fitting and to achieve significantly better generalization, while some basic pre-processing was needed to further improve the performance.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-eea242876f4d18e35ef5c9b96165a418e4be971a1e508717c15309f1c4bf23b8

Passage ID: `qasper-passage-v1-eea242876f4d18e35ef5c9b96165a418e4be971a1e508717c15309f1c4bf23b8`; retrieval score: 0.789937068176509.

Word count: 150.

```text
Minimal preprocessing was adopted in our approach: we replaced the target company's name with a fixed word <company> and numbers with <number>. The sentences were then tokenized using spaces as separator and keeping punctuation symbols as separate tokens.

The words are represented as fixed length vectors INLINEFORM0 resulting from the concatenation of GloVe pre-trained embeddings and DepecheMood BIBREF19 lexicon representation. Since we cannot directly concatenate token-based embeddings (provided in GloVe) with the lemma#PoS-based representation available in DepecheMood, we proceeded to re-build the latter in token-based form, applying the exact same methodology albeit with two differences: we started from a larger dataset (51.9K news articles instead of 25.3K) and used a frequency cut-off, i.e. keeping only those tokens that appear at least 5 times in the corpus.

These word-level representation are used as the first layer of our network. During training we allow the weights of the representation to be updated.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-ef47e6d173c470baa7a8c6f73123f834dd7ef1af513c2c448f5b332d9677b9e6

Passage ID: `qasper-passage-v1-ef47e6d173c470baa7a8c6f73123f834dd7ef1af513c2c448f5b332d9677b9e6`; retrieval score: 0.6243268130424119.

Word count: 108.

```text
In this section, we report the results obtained by our model according to challenge official evaluation metric, which is based cosine-similarity and described in BIBREF27 . Results are reported for three diverse configurations: (i) the full system; (ii) the system without using word embeddings (i.e. Glove and DepecheMood); and (iii) the system without using pre-processing. In Table TABREF17 we show model's performances on the challenge training data, in a 5-fold cross-validation setting.

Further, the final performances obtained with our approach on the challenge test set are reported in Table TABREF18 . Consistently with the cross-validation performances shown earlier, we observe the beneficial impact of word-representations and basic pre-processing.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-af8daf6940da0c5b9595b8a22166a637a08b1ea0623821dd452471b02f1c98be

Passage ID: `qasper-passage-v1-af8daf6940da0c5b9595b8a22166a637a08b1ea0623821dd452471b02f1c98be`; retrieval score: 0.5419371143149269.

Word count: 146.

```text
raw data, it is thus needed to develop machine learning methods allowing to convert unstructured text into information that can be managed and exploited.

In this paper, we address the sentiment analysis problem applied to financial headlines, where the goal is, for a given news headline and target company, to infer its polarity score i.e. how positive (or negative) the sentence is with respect to the target company. Previous research BIBREF0 has highlighted the association between news items and market fluctiations; hence, in the financial domain, sentiment analysis can be used as a proxy for bullish (i.e. positive, upwards trend) or bearish (i.e. negative, downwards trend) attitude towards a specific financial actor, allowing to identify and monitor in real-time the sentiment associated with e.g. stocks or brands.

Our contribution leverages pre-trained word embeddings (GloVe, trained on wikipedia+gigaword corpus), the DepecheMood affective lexicon, and convolutional neural networks.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1704.00939:0:3` | full | 0:171 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 584.

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

#### Rank 1: qasper-passage-v1-d317a0ae23a36cc325fbefb88eebe2d6d9bbfb604b6ae43fb905d0b2c8f5be5e

Passage ID: `qasper-passage-v1-d317a0ae23a36cc325fbefb88eebe2d6d9bbfb604b6ae43fb905d0b2c8f5be5e`; retrieval score: 7.734490097151916.

Word count: 150.

```text
Neural machine translation (NMT) typically makes use of a recurrent neural network (RNN) -based encoder and decoder, along with an attention mechanism BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 . However, it has been shown that RNNs require some supervision to learn syntax BIBREF4 , BIBREF5 , BIBREF6 . Therefore, explicitly incorporating syntactic information into NMT has the potential to improve performance. This is particularly true for source syntax, which can improve the model's representation of the source language.

Recently, there have been a number of proposals for using linearized representations of parses within standard NMT BIBREF7 , BIBREF8 , BIBREF9 . Linearized parses are advantageous because they can inject syntactic information into the models without significant changes to the architecture. However, using linearized parses in a sequence-to-sequence (seq2seq) framework creates some challenges, particularly when using source parses. First, the parsed sequences are significantly longer than standard sentences, since they
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-881e7004d6a6b2d7f3b163223d6aed38fde2e50ea512451593a307965c440f70

Passage ID: `qasper-passage-v1-881e7004d6a6b2d7f3b163223d6aed38fde2e50ea512451593a307965c440f70`; retrieval score: 6.9153801247784665.

Word count: 150.

```text
The idea of incorporating linearized parses into seq2seq has been adapted to NMT as a means of injecting syntax. aharoni2017towards first did this by parsing the target side of the training data and training the system to generate parsed translations of the source input; this is the inverse of our parse2seq baseline. Similarly, nadejde2017syntax interleaved CCG supertags with words on the target side, finding that this improved translation despite requiring longer sequences.

Most similar to our multi-source model is the parallel RNN model proposed by li2017modeling. Like multi-source, the parallel RNN used two encoders, one for words and the other for syntax. However, they combined these representations at the word level, whereas we combine them on the sentence level. Their mixed RNN model is also similar to our parse2seq baseline, although the mixed RNN decoder attended only to words. As the mixed RNN model outperformed the parallel RNN model, we
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-38471393536e478898a26ab217f86aa95616180c43da39eea58b22db8fc2861b

Passage ID: `qasper-passage-v1-38471393536e478898a26ab217f86aa95616180c43da39eea58b22db8fc2861b`; retrieval score: 6.359026110646875.

Word count: 146.

```text
syntactic information into the models without significant changes to the architecture. However, using linearized parses in a sequence-to-sequence (seq2seq) framework creates some challenges, particularly when using source parses. First, the parsed sequences are significantly longer than standard sentences, since they contain node labels as well as words. Second, these systems often fail when the source sentence is not parsed. This can be a problem for inference, since the external parser may fail on an input sentence at test time. We propose a method for incorporating linearized source parses into NMT that addresses these challenges by taking both the sequential source sentence and its linearized parse simultaneously as input in a multi-source framework. Thus, the model is able to use the syntactic information encoded in the parse while falling back to the sequential sentence when necessary. Our proposed model improves over both standard and parsed NMT baselines.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-67060789181607ed58814a3f3cd14c5d3ce4a74519fde216ce6798a396c9a7fa

Passage ID: `qasper-passage-v1-67060789181607ed58814a3f3cd14c5d3ce4a74519fde216ce6798a396c9a7fa`; retrieval score: 6.010204773107645.

Word count: 131.

```text
We propose a multi-source framework for injecting linearized source parses into NMT. This model consists of two identical RNN encoders with no shared parameters, as well as a standard RNN decoder. For each target sentence, two versions of the source sentence are used: the sequential (standard) version and the linearized parse (lexicalized or unlexicalized). Each of these is encoded simultaneously using the encoders; the encodings are then combined and used as input to the decoder. We combine the source encodings using the hierarchical attention combination proposed by libovicky2017attention. This consists of a separate attention mechanism for each encoder; these are then combined using an additional attention mechanism over the two separate context vectors. This multi-source method is thus able to combine the advantages of both standard RNN-based encodings and syntactic encodings.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-9050a3d82688042ced9e5bdd97ddf6ddbc8efe44847acff3b34a883f5dbb5e1b

Passage ID: `qasper-passage-v1-9050a3d82688042ced9e5bdd97ddf6ddbc8efe44847acff3b34a883f5dbb5e1b`; retrieval score: 5.943463474375428.

Word count: 133.

```text
The parse2seq and multi-source systems require parsed source data at inference time. However, the parser may fail on an input sentence. Therefore, we examine how well these systems do when given only unparsed source sentences at test time.

Table TABREF13 displays the results of these experiments. For the parse2seq baseline, we use only sequential (seq) data as input. For the lexicalized and unlexicalized multi-source systems, two options are considered: seq + seq uses identical sequential data as input to both encoders, while seq + null uses null input for the parsed encoder, where every source sentence is “( )”.

The parse2seq system fails when given only sequential source data. On the other hand, both multi-source systems perform reasonably well without parsed data, although the BLEU scores are worse than multi-source with parsed data.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 710.

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

#### Rank 1: qasper-passage-v1-b701a4e9111b31aa2927b6045367418c848054e49185127a1fb8f8aeacd4f238

Passage ID: `qasper-passage-v1-b701a4e9111b31aa2927b6045367418c848054e49185127a1fb8f8aeacd4f238`; retrieval score: 3.5443407928236064.

Word count: 104.

```text
to handle human generated comments. However, the logistic regression achieves reasonable performance on these tasks, and do not suffer from catastrophic performance on any tasks. Its worst result comes on task 6 and one of the reason is probably that this architecture is not designed to predict a list of answers. On the contrary, the deep projective reader achieves encouraging on this dataset. It outperforms all the other baselines, with very good scores on the first fourth tasks. The question/document and document/document attention layers proposed in BIBREF12 seem once again to produce rich encodings of the inputs which are relevant for our projection layer.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-aef836e13ddb9934048f0b86ab7fd19bd260f418c137bf4a32a5738167c8adf5

Passage ID: `qasper-passage-v1-aef836e13ddb9934048f0b86ab7fd19bd260f418c137bf4a32a5738167c8adf5`; retrieval score: 3.3416105359213955.

Word count: 150.

```text
machine reading framework is very general and we can imagine a large panel of questions that can possibly handle most of the standard natural language processing tasks. For example, the task of named entities recognition can be formulated as a machine reading one where your document is the sentence and the question would be 'What are the named entities mentioned in this sentence?'. These natural language interactions are an important objective for reading systems.

Recently, many datasets have been proposed to build and evaluate reading models BIBREF0 , BIBREF1 . From cloze style questions BIBREF2 to open questions BIBREF3 , from synthetic data BIBREF4 to human written articles BIBREF5 , many styles of documents and questions have been proposed to challenge reading models. The correct answer to the questions proposed in most of these datasets is a span of text of the source document, which can be restricted to a
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-971d0690b7f51b1b92f8badcc020928277ed3db0b2323346e9143f75e636d802

Passage ID: `qasper-passage-v1-971d0690b7f51b1b92f8badcc020928277ed3db0b2323346e9143f75e636d802`; retrieval score: 3.033683368030451.

Word count: 150.

```text
Table TABREF19 displays the performance of the 4 baselines on the ReviewQA's test set. These results are the performance achieved by our own implementation of these 4 models. According to our results, the simple LSTM network and the MemN2N perform very poorly on this dataset. Especially on the most advanced reasoning tasks. Indeed, the task 5 which corresponds to the prediction of the exact rating of an aspect seems to be very challenging for these model. Maybe the tokenization by sentence to create the memory blocks of the MemN2N, which is appropriated in the case of the bAbI tasks, is not a good representation of the documents when it has to handle human generated comments. However, the logistic regression achieves reasonable performance on these tasks, and do not suffer from catastrophic performance on any tasks. Its worst result comes on task 6 and one of the reason is probably that
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-877535c9594098b1729f28c9f06687a78c6d60c9da346811ed7a93e9f2e6fc70

Passage ID: `qasper-passage-v1-877535c9594098b1729f28c9f06687a78c6d60c9da346811ed7a93e9f2e6fc70`; retrieval score: 2.981134344505804.

Word count: 150.

```text
A large majority of the human knowledge is recorded through text documents. That is why ability for a system to automatically infer information from text without any structured data has become a major challenge. Answering questions about a given document is a relevant proxy task that has been proposed as a way to evaluate the reading ability of a given model. In this configuration, a text document such as a news article, a document from Wikipedia or any type of text is presented to a machine with an associated set of questions. The system is then expected to answer these questions and evaluated by its accuracy on this task. The machine reading framework is very general and we can imagine a large panel of questions that can possibly handle most of the standard natural language processing tasks. For example, the task of named entities recognition can be formulated as a
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-b078eef8e2d0e3c8b5cee74a57833fb57321f2f7f7b962eeecf819312b64968b

Passage ID: `qasper-passage-v1-b078eef8e2d0e3c8b5cee74a57833fb57321f2f7f7b962eeecf819312b64968b`; retrieval score: 2.9035355626604007.

Word count: 150.

```text
Objective: Starting with the original corpus, we aim at building a machine reading task where natural language questions will challenge the model on its understanding of the reviews. Indeed learning relational reasoning competencies over natural language documents is a major challenge of the current reading models. These original raw data allow us to generate relational questions that can possibly require a global understanding of the comment and reasoning skills to be treated. For example, asking a question like What is the best aspect rated in this comment ? is not an easy question that can be answered without a deep understanding of the review. It is necessary to capture all the aspects mentioned in the text, to predict their rating and finally to select the best one. The tasks and the dataset we propose are publicly available at http://www.europe.naverlabs.com/Blog/ReviewQA-A-novel-relational-aspect-based-opinion-dataset-for-machine-reading

We introduce a list of 8 different competencies that a reading
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 704.

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

#### Rank 1: qasper-passage-v1-49b0d4418578cf35c5c37667cf7c76089544cd72a02ef07ebd4c258e2327f068

Passage ID: `qasper-passage-v1-49b0d4418578cf35c5c37667cf7c76089544cd72a02ef07ebd4c258e2327f068`; retrieval score: 6.165427800898131.

Word count: 150.

```text
that the proposed method does learn better correspondence. The highlighted words in each example in Table TABREF28 share almost the same previous words. However, in the first one, the baseline considers “UTF8gbsn停” (stop) as the most related words, which is a sign of noisy word relations learned from other training examples, while the proposed method generates “UTF8gbsn进站” (to the platform), which is more related to what a human thinks. It is the same with the second example, where a human selects “UTF8gbsn专家” (expert) and Dual-Train selects “UTF8gbsn工作者” (worker), while the baseline selects “UTF8gbsn钻研” (research) and fails to generate a grammatical sentence later. In the third one, the reference and the baseline use the same word, while Dual-Train chooses a word of the same meaning. It can be concluded that Dual-Train indeed learns better word relations that could generalize to the test set, and good word relations can guide the decoder
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-9fc702d873c41806db6482aa289b838d0082d38b8a399c50ed56c2a425fa37a6

Passage ID: `qasper-passage-v1-9fc702d873c41806db6482aa289b838d0082d38b8a399c50ed56c2a425fa37a6`; retrieval score: 4.900075225188518.

Word count: 150.

```text
We propose a regularization approach for the sequence-to-sequence model on the Chinese social media summarization task. In the proposed approach, we use a cross-entropy based regularization term to make the model neglect the possible unrelated words. We propose two methods for obtaining the soft output word distribution used in the regularization, of which Dual-Train proves to be more effective. Experimental results show that the proposed method can improve the semantic consistency by 4% in terms of human evaluation. As shown by the analysis, the proposed method achieves the improvements by eliminating the less semantically-related word correspondence. The proposed human evaluation method is effective and efficient in judging the semantic consistency, which is absent in previous work but is crucial in the accurate evaluation of the text summarization systems. The proposed metric is simple to conduct and easy to interpret. It also provides an insight on how practicable the existing systems
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-fef88e94b28bddf80ca92e170543125181e9356ba91175b39fd850a4d3290f60

Passage ID: `qasper-passage-v1-fef88e94b28bddf80ca92e170543125181e9356ba91175b39fd850a4d3290f60`; retrieval score: 4.614407440999699.

Word count: 150.

```text
reference only includes the facts in the last sentence of the source content. In short, the generated summary of the proposed method is more consistent with the source content. It also exhibits the necessity of the proposed human evaluation. Because when the generated summary is evaluated against the reference, it may seem redundant or wrong, but it is actually true to the source content. While it is arguable that the generated summary is better than the reference, there is no doubt that the generated summary of the proposed method is better than the baseline. However, the improvement cannot be properly shown by the existing evaluation methods. Furthermore, the examples suggest that the proposed method does learn better correspondence. The highlighted words in each example in Table TABREF28 share almost the same previous words. However, in the first one, the baseline considers “UTF8gbsn停” (stop) as the most related words, which is
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-b084cb588bbdd2ddbb82f4e808bbe31778eb8edd04ac27be3a9b8e96cb83f25e

Passage ID: `qasper-passage-v1-b084cb588bbdd2ddbb82f4e808bbe31778eb8edd04ac27be3a9b8e96cb83f25e`; retrieval score: 4.302293671426676.

Word count: 150.

```text
However, the aforementioned method tries to regularize the output word distribution based on what it has already learned. The relative order of the output words is kept. The self-dependency may not be desirable for regularization. It may be better if more correspondence that is spurious can be identified. In this paper, we further propose to obtain the soft target from a different view of the model, so that different knowledge of the dataset can be used to mitigate the overfitting problem. An additional output layer is introduced to generate the soft target. The two output layers share the same hidden representation but have independent parameters. They could learn different knowledge of the data. We refer to this approach as Dual-Train. For clarity, the original output layer is denoted by INLINEFORM0 and the new output layer INLINEFORM1 . Their outputs are denoted by INLINEFORM2 and INLINEFORM3 , respectively. The output layer
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-960eb1872b36aac53a0646d363ee5240a0796aed1d9fd0dab27f11b93684ad1c

Passage ID: `qasper-passage-v1-960eb1872b36aac53a0646d363ee5240a0796aed1d9fd0dab27f11b93684ad1c`; retrieval score: 4.287013784258811.

Word count: 150.

```text
first one, the baseline system generates a grammatical but unrelated summary, while the proposed method generates a more informative summary. In the second one, the baseline system generates a related but ungrammatical summary, while the proposed method generates a summary related to the source content but different from the reference. We believe the generated summary is actually better than the reference because the focus of the visit is not the event itself but its purpose. In the third one, the baseline system generates a related and grammatical summary, but the facts stated are completely incorrect. The summary generated by the proposed method is more comprehensive than the reference, while the reference only includes the facts in the last sentence of the source content. In short, the generated summary of the proposed method is more consistent with the source content. It also exhibits the necessity of the proposed human evaluation. Because
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 750.

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
          0,
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

#### Rank 1: qasper-passage-v1-9f3fa6e24c8911219159fe2bfe8354f3e30499a19dea24d95bc1139aee9b8c68

Passage ID: `qasper-passage-v1-9f3fa6e24c8911219159fe2bfe8354f3e30499a19dea24d95bc1139aee9b8c68`; retrieval score: 7.037286039933903.

Word count: 150.

```text
ASR, MT and ST respectively, hence, the attention module of ST does not benefit from the pre-training.

To address these issues, we propose a Tandem Connectionist Encoding Network (TCEN), which is able to reuse all subnets in pre-training, keep the roles of subnets consistent, and pre-train the attention module. Concretely, the TCEN consists of three components, a speech encoder, a text encoder, and a target text decoder. Different from the previous work that pre-trains an encoder-decoder based ASR model, we only pre-train an ASR encoder by optimizing the Connectionist Temporal Classification (CTC) BIBREF8 objective function. In this way, the additional decoder of ASR is not required while keeping the ability to read acoustic features into the source language space by the speech encoder. Besides, the text encoder and decoder can be pre-trained on a large MT dataset. After that, we employ common used multi-task learning method to jointly learn ASR,
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-2374dffbb97b5de9866cfc9652903e6fa88e154b360bd3b8c76efdc858c9dd32

Passage ID: `qasper-passage-v1-2374dffbb97b5de9866cfc9652903e6fa88e154b360bd3b8c76efdc858c9dd32`; retrieval score: 6.66501172782019.

Word count: 150.

```text
MT, and ST. This approach, however, causes a huge gap between pre-training and fine-tuning, which are summarized into three folds:

Subnet Waste: The ST system just reuses the ASR encoder and the MT decoder, while discards other pre-trained subnets, such as the MT encoder. Consequently, valuable semantic information captured by the MT encoder cannot be inherited by the final ST system.

Role Mismatch: The speech encoder plays different roles in pre-training and fine-tuning. The encoder is a pure acoustic model in pre-training, while it has to extract semantic and linguistic features additionally in fine-tuning, which significantly increases the learning difficulty.

Non-pre-trained Attention Module: Previous work BIBREF6 trains attention modules for ASR, MT and ST respectively, hence, the attention module of ST does not benefit from the pre-training.

To address these issues, we propose a Tandem Connectionist Encoding Network (TCEN), which is able to reuse all subnets in pre-training, keep the
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-9b0c1398c8015ebc5294c67fd4e4cdcfa6e3786060adda3f03dcc3c77e98189a

Passage ID: `qasper-passage-v1-9b0c1398c8015ebc5294c67fd4e4cdcfa6e3786060adda3f03dcc3c77e98189a`; retrieval score: 6.122958372326266.

Word count: 150.

```text
To leverage large scale ASR and MT data, multi-task learning and pre-training techniques are widely employed to improve the ST system. As shown in Figure FIGREF4, there are three popular multi-task strategies for ST, including 1) one-to-many setting, in which a speech encoder is shared between ASR and ST tasks; 2) many-to-one setting in which a decoder is shared between MT and ST tasks; and 3) many-to-many setting where both the encoder and decoder are shared.

A many-to-many multi-task model contains two encoders as well as two decoders. It can be jointly trained on ASR, MT, and ST tasks. As the attention module is task-specific, three attentions are defined.

Usually, the size of $\mathcal {A}$ and $\mathcal {M}$ is much larger than $\mathcal {S}$. Therefore, the common training practice is to pre-train the model on ASR and MT tasks and then fine-tune it with a multi-task learning manner. However, as
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-bb2dfe4c3998001745570d9812812a1dfdb0d57b3fd2d05318fe640b1cd38830

Passage ID: `qasper-passage-v1-bb2dfe4c3998001745570d9812812a1dfdb0d57b3fd2d05318fe640b1cd38830`; retrieval score: 5.9357824321278.

Word count: 150.

```text
to read acoustic features into the source language space by the speech encoder. Besides, the text encoder and decoder can be pre-trained on a large MT dataset. After that, we employ common used multi-task learning method to jointly learn ASR, MT and ST tasks.

Compared to prior works, the encoder of TCEN is a concatenation of an ASR encoder and an MT encoder and our model does not have an ASR decoder, so the subnet waste issue is solved. Furthermore, the two encoders work at tandem, disentangling acoustic feature extraction and linguistic feature extraction, ensuring the role consistency between pre-training and fine-tuning. Moreover, we reuse the pre-trained MT attention module in ST, so we can leverage the alignment information learned in pre-training.

Since the text encoder consumes word embeddings of plausible texts in MT task but uses speech encoder outputs in ST task, another question is how one guarantees the
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-7ee185118f3fa9a1a46a022347ba2c56dc13feb02fdcb73d37199e23bfa7fc7d

Passage ID: `qasper-passage-v1-7ee185118f3fa9a1a46a022347ba2c56dc13feb02fdcb73d37199e23bfa7fc7d`; retrieval score: 5.542447509952267.

Word count: 150.

```text
Figure FIGREF5 sketches the overall architecture of TCEN, including a speech encoder $enc_s$, a text encoder $enc_t$ and a decoder $dec$ with an attention module $att$. During training, the $enc_s$ acts like an acoustic model which reads the input $\mathbf {x}$ to word or subword representations $\mathbf {h^s}$, then $enc_t$ learns high-level linguistic knowledge into hidden representations $\mathbf {h^t}$. Finally, the $dec$ defines a distribution probability over target words. The advantage of our architecture is that two encoders disentangle acoustic feature extraction and linguistic feature extraction, making sure that valuable knowledge learned from ASR and MT tasks can be effectively leveraged for ST training. Besides, every module in pre-training can be utilized in fine-tuning, alleviating the subnet waste problem.

Follow BIBREF9 inaguma2018speech, we use CNN-BiLSTM architecture to build our model. Specifically, the input features $\mathbf {x}$ are organized as a sequence of feature vectors in length $T_x$. Then, $\mathbf {x}$
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 750.

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

#### Rank 1: qasper-passage-v1-bc0243bd9a928b0e4db572949e1aad7436c435cea9f4305c080de6fe40e68797

Passage ID: `qasper-passage-v1-bc0243bd9a928b0e4db572949e1aad7436c435cea9f4305c080de6fe40e68797`; retrieval score: 9.89999703976908.

Word count: 150.

```text
This paper has used data-driven language mapping to select national dialects of English to be included in a global dialect identification model. The main experiments have focused on a dynamic syntactic feature set, showing that it is possible to predict dialect membership within-domain with only a small loss of performance against lexical models. This work raises two remaining problems:

First, we know that location-specific content (i.e., place names, place references, national events) can be used for geo-location and text-based models of place. To what degree does a lexical approach capture linguistic variation (i.e., “pop" vs. “soda") and to what degree is it capturing non-linguistic information (i.e., “Melbourne" vs. “London")? This is an essential problem for dialect identification models. A purely syntactic model does not perform as well as a lexical model, but it does come with more guarantees.

Second, we have seen that inner-circle varieties have higher feature densities given
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.05527:9:0` | full | 0:389 |

#### Rank 2: qasper-passage-v1-d9feda834b10be30f1a01060802f4710431f6dbcba71f93b97a448daa7d4d6db

Passage ID: `qasper-passage-v1-d9feda834b10be30f1a01060802f4710431f6dbcba71f93b97a448daa7d4d6db`; retrieval score: 7.121169806139993.

Word count: 97.

```text
is restricted to the specific domains or registers that are present in the corpus. To what degree is such a model of variation limited to a specific register? This paper uses both web-crawled corpora and social media corpora to explore the robustness of dialect models across domains (Section 8). Along these same lines, how robust is a model of syntactic variation to the presence of a few highly predictive features? This paper uses unmasking, a method from authorship verification (Koppel, et al., 2007), to evaluate the stability of dialect models over rounds of feature pruning (Section 9).
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-080b785fc2b3a4547f80d4c5b8dc5d9218f5075ba8ae582ee7869264d316af64

Passage ID: `qasper-passage-v1-080b785fc2b3a4547f80d4c5b8dc5d9218f5075ba8ae582ee7869264d316af64`; retrieval score: 5.868367404889602.

Word count: 150.

```text
than on purely linguistic lexical variation (e.g., “jeans" vs. “denim"). How do we differentiate between predictions based on place-names, those based on place-specific content, and those based on dialectal variation? That is a question for future work. For example, is it possible to identify and remove location-specific content terms? Here we focus instead on using syntactic representations that are not subject to such interference.

Within syntactic features, function words perform the worst on both datasets with F1s of 0.65 and 0.55. This is not surprising because function words in English do not represent syntactic structures directly; they are instead markers of the types of structures being used. CxG-1 comes next with F1s of 0.80 and 0.76, a significant improvement over the function-word baseline but not approaching unigrams. Note that the experiments using this same grammar in previous work (Dunn, 2018c) were applied to samples of 2k words each. Finally, CxG-2
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-66fc296f6c842a1c025c1e543f1820bc85545c8ad4713671d6e0e23900fd0f9c

Passage ID: `qasper-passage-v1-66fc296f6c842a1c025c1e543f1820bc85545c8ad4713671d6e0e23900fd0f9c`; retrieval score: 5.6177809372143335.

Word count: 143.

```text
is an essential problem for dialect identification models. A purely syntactic model does not perform as well as a lexical model, but it does come with more guarantees.

Second, we have seen that inner-circle varieties have higher feature densities given the grammars used here. This implies that there are syntactic constructions in varieties like Philippines English that have not been modeled by the grammar induction component. While dialect identification can be used to optimize regional weights for known constructions, how can such missing constructions be adapted? This remains a challenge. While the less proto-typical dialects have higher F1s (i.e., Pakistan English), they also have lower feature densities. This indicates that some of their constructions are missing from the grammar. Nevertheless, this paper has shown that a broader syntactic feature space can be used to model the difference between many national varieties of English.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-fb832240f10a84d3a53dd868ee3e71214e0ff894e38ef38c6b09d7088423a116

Passage ID: `qasper-passage-v1-fb832240f10a84d3a53dd868ee3e71214e0ff894e38ef38c6b09d7088423a116`; retrieval score: 5.497744020230352.

Word count: 150.

```text
vectorizer to avoid a region-specific bias: the vectorizer does not need to be trained or initialized against a specific dataset so there is no chance that one of the varieties will be over-represented in determining which n-grams are included. But this has the side-effect of preventing the inspection of individual features. Vectors for all experiments are available, along with the trained models that depend on these vectors.

As n increases, n-grams tend to represent structural rather than topical information. In this case, performance decreases as n increases. We suggest that this decrease provides an indication that the performance of unigrams is based on location-specific content (e.g., “Chicago" vs. “Singapore") rather than on purely linguistic lexical variation (e.g., “jeans" vs. “denim"). How do we differentiate between predictions based on place-names, those based on place-specific content, and those based on dialectal variation? That is a question for future work. For example, is
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 690.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "a85e7b72967bf239b184ce129eec43a5e8df773f": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1904.05527:6:0": [
        [
          0,
          369
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-6e8653c5c29472f46547d9e4f368a03f54d7dc41dad9efda105af63c9d59b6cd

Passage ID: `qasper-passage-v1-6e8653c5c29472f46547d9e4f368a03f54d7dc41dad9efda105af63c9d59b6cd`; retrieval score: 8.629412359253045.

Word count: 150.

```text
Many machine reading comprehension (MRC) datasets have been released in recent years BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4 to benchmark a system's ability to understand and reason over natural language. Typically, these datasets require an MRC model to read through a document to answer a question about information contained therein.

The supporting document is, more often than not, static and fully observable. This raises concerns, since models may find answers simply through shallow pattern matching; e.g., syntactic similarity between the words in questions and documents. As pointed out by BIBREF5, for questions starting with when, models tend to predict the only date/time answer in the supporting document. Such behavior limits the generality and usefulness of MRC models, and suggests that they do not learn a proper `understanding' of the intended task. In this paper, to address this problem, we shift the focus of MRC data away from `spoon-feeding' models with sufficient
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-301e95ee0c47ebb987a064fe563163ad23473d79b18288ac68981ea6f23cf0fc

Passage ID: `qasper-passage-v1-301e95ee0c47ebb987a064fe563163ad23473d79b18288ac68981ea6f23cf0fc`; retrieval score: 8.10983939610268.

Word count: 150.

```text
generality and usefulness of MRC models, and suggests that they do not learn a proper `understanding' of the intended task. In this paper, to address this problem, we shift the focus of MRC data away from `spoon-feeding' models with sufficient information in fully observable, static documents. Instead, we propose interactive versions of existing MRC tasks, whereby the information needed to answer a question must be gathered sequentially.

The key idea behind our proposed interactive MRC (iMRC) is to restrict the document context that a model observes at one time. Concretely, we split a supporting document into its component sentences and withhold these sentences from the model. Given a question, the model must issue commands to observe sentences in the withheld set; we equip models with actions such as Ctrl+F (search for token) and stop for searching through partially observed documents. A model searches iteratively, conditioning each command on the input
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.10449:0:2` | partial | 0:526 |

#### Rank 3: qasper-passage-v1-fe8754ca9fec49a6d0a9a40e51a3ebf15e211e9d45f69a7ba36615bc87dbb8df

Passage ID: `qasper-passage-v1-fe8754ca9fec49a6d0a9a40e51a3ebf15e211e9d45f69a7ba36615bc87dbb8df`; retrieval score: 5.873774740525582.

Word count: 150.

```text
baseline, we adopted an off-the-shelf, top-performing MRC model and RL method. Either component can be replaced straightforwardly with other methods (e.g., to utilize a large-scale pretrained language model).

Our proposed setup and baseline agent presently use only a single word with the query command. However, a host of other options should be considered in future work. For example, multi-word queries with fuzzy matching are more realistic. It would also be interesting for an agent to generate a vector representation of the query in some latent space. This vector could then be compared with precomputed document representations (e.g., in an open domain QA dataset) to determine what text to observe next, with such behavior tantamount to learning to do IR.

As mentioned, our idea for reformulating existing MRC datasets as partially observable and interactive environments is straightforward and general. Almost all MRC datasets can be used to study interactive, information-seeking behavior
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-3c0d6fb653c776d0edb6ea9397b72908f5b687f2dc454b0e05b7c947969b7f40

Passage ID: `qasper-passage-v1-3c0d6fb653c776d0edb6ea9397b72908f5b687f2dc454b0e05b7c947969b7f40`; retrieval score: 5.612384135518291.

Word count: 96.

```text
to iMRC is work by BIBREF15, in which the authors introduce a collection of synthetic tasks to train and test information-seeking capabilities in neural models. We extend that work by developing a realistic and challenging text-based task.

Broadly speaking, our approach is also linked to the optimal stopping problem in the literature Markov decision processes (MDP) BIBREF16, where at each time-step the agent either continues or stops and accumulates reward. Here, we reformulate conventional QA tasks through the lens of optimal stopping, in hopes of improving over the shallow matching behaviors exhibited by many MRC systems.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-b565ab9573989f6c91cb126980bec94a464159ef18eda5938f4f76bf28320811

Passage ID: `qasper-passage-v1-b565ab9573989f6c91cb126980bec94a464159ef18eda5938f4f76bf28320811`; retrieval score: 5.142749409252214.

Word count: 150.

```text
Skip-reading BIBREF6, BIBREF7, BIBREF8 is an existing setting in which MRC models read partial documents. Concretely, these methods assume that not all tokens in the input sequence are useful, and therefore learn to skip irrelevant tokens based on the current input and their internal memory. Since skipping decisions are discrete, the models are often optimized by the REINFORCE algorithm BIBREF9. For example, the structural-jump-LSTM proposed in BIBREF10 learns to skip and jump over chunks of text. In a similar vein, BIBREF11 designed a QA task where the model reads streaming data unidirectionally, without knowing when the question will be provided. Skip-reading approaches are limited in that they only consider jumping over a few consecutive tokens and the skipping operations are usually unidirectional. Based on the assumption that a single pass of reading may not provide sufficient information, multi-pass reading methods have also been studied BIBREF12, BIBREF13.

Compared to skip-reading and
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 696.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "33b2d26d064251c196238b0c3c455b208680f5fc": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1908.10449:0:2": [
        [
          526,
          778
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-aa8848384bd6bc583477d4533e66cbccbc5413782baf24b75b6f85509d84fb30

Passage ID: `qasper-passage-v1-aa8848384bd6bc583477d4533e66cbccbc5413782baf24b75b6f85509d84fb30`; retrieval score: 5.375244362552678.

Word count: 150.

```text
Seshat was intially developped to study the impact of Huntington's Disease BIBREF17 on speech and language production. One hundred and fifty two interviews between a neuropsychologist and a patient with the Huntington's Disease (HD) were recorded between June 2018 and November 2019. The campaign manager created a campaign with multiple tiers to annotate the turn takings and the speech/non speech boundaries of the utterances of the patient. For both tasks, the annotations did not need to cover completely the audio (sparsity property mentioned above). For the Turn-taking annotations, there are 3 pre-defined tiers, each one with a single class ('Patient', 'Non-Patient', and 'Noise'), which results in possible overlap between these classes. For the Utterance annotations, there is only one pre-defined class ('Utterance').

To this date, a total of 67 files have been fully annotated with the help of Seshat by a cohort of 18 speech pathologist students (see Figure FIGREF33).
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-852b7ed99d78f910d2cdbf2c4249e2355b94be9f83babc932535fd094ffb97e5

Passage ID: `qasper-passage-v1-852b7ed99d78f910d2cdbf2c4249e2355b94be9f83babc932535fd094ffb97e5`; retrieval score: 5.362217705191291.

Word count: 150.

```text
same names. It can also enforce, for certain chosen tiers, a set of valid annotations.

Users with the rights to create Annotation Campaigns and Annotators user accounts, and assign Annotation Tasks to Annotators.

Users who are assigned a set of Annotation Tasks. Their job is to complete the annotation of the audio files with the Praat software.

If the TextGrid file they submit does not comply with their Annotation Task's TextGrid Checking Scheme, Seshat pinpoint their annotation errors with detailed messages. The annotator can re-submit the concerned file to the platform based on these different feedbacks.

Once they they connected to their instance of Seshat, campaign managers can access ongoing annotation campaigns or create new ones. Campaign managers are able to add annotators, assign annotation tasks and track progress. Annotator see a list of assigned tasks. The first step for them is to download the sound file with its corresponding
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-7e2104cbaf0175bc19a149acc2894c5463a10dad6254a0a9013d7e69b1fc3d8b

Passage ID: `qasper-passage-v1-7e2104cbaf0175bc19a149acc2894c5463a10dad6254a0a9013d7e69b1fc3d8b`; retrieval score: 4.809256091187649.

Word count: 150.

```text
The Campaign manager can easily define and monitor annotation campaign. As shown in Figure FIGREF33, the online form enable to choose corpora, pre-define and pre-configure the annotations scheme (tiers and parsers). There are 2 types of tiers already implemented by default: one with no check at all, and one with pre-defined categories. For the latter, these categories are pre-defined when the campaign is created.

Only Campaign managers can access and build new campaigns. If Campaign manager have several campaigns they can easily switch between them via the menu bar or get a full overview with the dashboard (See Figure FIGREF26). The campaign managers can visualise the progress of the assigned tasks at the campaign level or more precisely at the task level. They can retrieve all the intermediate files that have been created for each task. For instance, the campaign manager can examine qualitatively and quantitatively what are the annotation
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-9e342534fdb303af470921421e4e00fa675683b726f1e5da00d12f4d42d086cf

Passage ID: `qasper-passage-v1-9e342534fdb303af470921421e4e00fa675683b726f1e5da00d12f4d42d086cf`; retrieval score: 4.801967393910171.

Word count: 143.

```text
there are more sophisticated systems with various capabilities. Camomille BIBREF11 and the EMU-SDMS system (that can also be used offline) BIBREF12 allow to work with speech data and to distribute the tasks to several annotators. But these systems require expertise in web hosting and technologies to deploy and modify them.

Finally, WebAnno BIBREF13 and GATE Teamware BIBREF14 are the tools that most closely match our main contributions regarding quality control (conformity and consistency checking), annotators' management and flexibility. WebAnno includes consistency checking with the integration of different metrics BIBREF15. However, these tools have only been built for text data. The format and all the custom layers have been designed for Natural Language Processing tasks. Porting WebAnno to support speech data seemed a major engineering challenge. That is why it appeared necessary to develop a new and user-friendly tool addressed to the speech community.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-180d86f845a21a509e84ee6c80e377d0d4e38f73ff3d3ebd70a724f0c8c9d8df

Passage ID: `qasper-passage-v1-180d86f845a21a509e84ee6c80e377d0d4e38f73ff3d3ebd70a724f0c8c9d8df`; retrieval score: 4.540372517448488.

Word count: 150.

```text
to the researchers. This task becomes quickly untraceable as the number of files and annotators grow. In addition, most of these transcription systems do not provide a way to evaluate consistency (intra- and inter-annotator agreement) that would be appropriate for speech data BIBREF8.

Web-based annotations systems. There are several web-based annotation systems for the annotation of audio data. Among them we find light-weight systems, like the VIA software BIBREF9 or Praat on the web BIBREF10 that allow to build simple layers of annotations. However, they do not provide a proper management system for a pool of annotators nor do they integrate annotation checking.

On the other side of the spectrum, there are more sophisticated systems with various capabilities. Camomille BIBREF11 and the EMU-SDMS system (that can also be used offline) BIBREF12 allow to work with speech data and to distribute the tasks to several annotators. But these systems require expertise
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 743.

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

#### Rank 1: qasper-passage-v1-ca21794992d699b0bbdd3d3607a018e60b6cfa424936a144bf8b53d8ddf96b2d

Passage ID: `qasper-passage-v1-ca21794992d699b0bbdd3d3607a018e60b6cfa424936a144bf8b53d8ddf96b2d`; retrieval score: 9.367681876121853.

Word count: 150.

```text
literature has been given to generative Bayesian network models until recently as proposed in BIBREF28 and BIBREF11 . On the other hand, the successful use of discriminative models for belief tracking has recently been reported by BIBREF29 and BIBREF5 and was a major theme in the results of the recent edition of the Dialog State Tracking Challenge. In this paper, a latent decomposition type of approach is proposed in order to address this general problem of dialog system. Our method gives encouraging results in comparison to the state of the art dataset and also does not required complex inference at test time because, as detailed in Section "Spectral decomposition model for state tracking in slot-filling dialogs" , the tracking algorithm hold a linear complexity w.r.t the sum of realization of each considered variables defining the state to track which is what we believe is one of the main advantage of
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-c6832f47e89ba2c722592f9cd42d2857cbc3b8c763c0002c17f8cb48aa929f94

Passage ID: `qasper-passage-v1-c6832f47e89ba2c722592f9cd42d2857cbc3b8c763c0002c17f8cb48aa929f94`; retrieval score: 9.183445299235537.

Word count: 150.

```text
As a comparison to the state of the art methods, Table 1 presents accuracy results of the best Collective Matrix Factorization model, with a latent space dimension of 350, which has been determined by cross-validation on a development set, where the value of each slot is instantiated as the most probable w.r.t the inference procedure presented in Section "Spectral decomposition model for state tracking in slot-filling dialogs" . In our experiments, the variance is estimated using standard dataset reshuffling. The same results are obtained for several state of the art methods of generative and discriminative state tracking on this dataset using the publicly available results as reported in BIBREF22 . More precisely, as provided by the state-of-the-art approaches, the accuracy scores computes $p(s^*_{t+1}|s_t,z_t)$ commonly name the joint goal. Our proposition is compared to the 4 baseline trackers provided by the DSTC organisers. They are the baseline tracker (Baseline), the focus
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1606.05286:9:0` | partial | 0:994 |

#### Rank 3: qasper-passage-v1-08c0e05e38868f3a27c2fb3141a4c821915b216a747b49a1d5d3837f64cb6647

Passage ID: `qasper-passage-v1-08c0e05e38868f3a27c2fb3141a4c821915b216a747b49a1d5d3837f64cb6647`; retrieval score: 8.363695341063659.

Word count: 90.

```text
More precisely, as provided by the state-of-the-art approaches, the accuracy scores computes $p(s^*_{t+1}|s_t,z_t)$ commonly name the joint goal. Our proposition is compared to the 4 baseline trackers provided by the DSTC organisers. They are the baseline tracker (Baseline), the focus tracker (Focus), the HWU tracker (HWU) and the HWU tracker with “original” flag set to (HWU+) respectively. Then a comparison to a maximum entropy (MaxEnt) proposed in BIBREF23 type of discriminative model and finally a deep neural network (DNN) architecture proposed in BIBREF24 as reported also in BIBREF22 is presented.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1606.05286:9:0` | partial | 709:1317 |

#### Rank 4: qasper-passage-v1-4fbdd547d94212738a3f1b0aca597a7bbdf6656f9af87c8442309a4357e56e92

Passage ID: `qasper-passage-v1-4fbdd547d94212738a3f1b0aca597a7bbdf6656f9af87c8442309a4357e56e92`; retrieval score: 7.2987669577204795.

Word count: 69.

```text
for state tracking in slot-filling dialogs" , the tracking algorithm hold a linear complexity w.r.t the sum of realization of each considered variables defining the state to track which is what we believe is one of the main advantage of this method. Secondly collective matrix factorization paradigm also for data fusion and bias by data type of modeling as successfully performed in matrix factorization based recommender systems BIBREF30 .
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-8a1e81b446616f6f203028c2880fabb49673d8b27f0190d0ae416537c9b71f07

Passage ID: `qasper-passage-v1-8a1e81b446616f6f203028c2880fabb49673d8b27f0190d0ae416537c9b71f07`; retrieval score: 6.915725392115841.

Word count: 136.

```text
of possible state variables to those that appeared in NLU results. More recently, BIBREF14 assumes conditional independence between dialog state variables to address scalability issues and uses a conditional random field to track each variable separately. Finally, deep neural models, performing on a sliding window of features extracted from previous user turns, have also been proposed in BIBREF15 . Of the current literature, this family of approaches have proven to be the most efficient for publicly available state tracking datasets. In the next section, we present a decompositional approach of dialog state tracking that aims at reconciling the two main approaches of the state of the art while leveraging on the current advances of low-rank bilinear decomposition models, as recalled in BIBREF16 , that seems particularly adapted to the sparse nature of dialog state tracking tasks.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 595.

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

#### Rank 1: qasper-passage-v1-e78fe1c8d936a873aa39ca78e475c25d02e41422e40a350bb38fd46f7c082157

Passage ID: `qasper-passage-v1-e78fe1c8d936a873aa39ca78e475c25d02e41422e40a350bb38fd46f7c082157`; retrieval score: 10.942379031115623.

Word count: 150.

```text
The explosion of available scientific articles in the Biomedical domain has led to the rise of Biomedical Information Extraction (BioIE). BioIE systems aim to extract information from a wide spectrum of articles including medical literature, biological literature, electronic health records, etc. that can be used by clinicians and researchers in the field. Often the outputs of BioIE systems are used to assist in the creation of databases, or to suggest new paths for research. For example, a ranked list of interacting proteins that are extracted from biomedical literature, but are not present in existing databases, can allow researchers to make informed decisions about which protein/gene to study further. Interactions between drugs are necessary for clinicians who simultaneously administer multiple drugs to their patients. A database of diseases, treatments and tests is beneficial for doctors consulting in complicated medical cases.

The main problems in BioIE are similar to those in Information
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-b4c88ef56207ec7e087b70e28a40f9250b5ee904c711cb423b5122e9aad2932b

Passage ID: `qasper-passage-v1-b4c88ef56207ec7e087b70e28a40f9250b5ee904c711cb423b5122e9aad2932b`; retrieval score: 6.308678884866405.

Word count: 128.

```text
drugs are necessary for clinicians who simultaneously administer multiple drugs to their patients. A database of diseases, treatments and tests is beneficial for doctors consulting in complicated medical cases.

The main problems in BioIE are similar to those in Information Extraction:

This paper discusses, in each section, various methods that have been adopted to solve the listed problems. Each section also highlights the difficulty of Information Extraction tasks in the biomedical domain.

This paper is intended as a primer to Biomedical Information Extraction for current NLP researchers. It aims to highlight the diversity of the various techniques from Information Extraction that have been applied in the Biomedical domain. The state of biomedical text mining is reviewed regularly. For more extensive surveys, consult BIBREF0 , BIBREF1 , BIBREF2 .
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-41fa63833e0f1f6078ff9d762cd6d0c682594021cb9de525e5c7d588b648d4e1

Passage ID: `qasper-passage-v1-41fa63833e0f1f6078ff9d762cd6d0c682594021cb9de525e5c7d588b648d4e1`; retrieval score: 4.5925457686045.

Word count: 150.

```text
Named Entity Recognition (NER) in the Biomedical domain usually includes recognition of entities such as proteins, genes, diseases, treatments, drugs, etc. Fact extraction involves extraction of Named Entities from a corpus, usually given a certain ontology. When compared to NER in the domain of general text, the biomedical domain has some characteristic challenges:

Some of the earliest systems were heavily dependent on hand-crafted features. The method proposed in BIBREF4 for recognition of protein names in text does not require any prepared dictionary. The work gives examples of diversity in protein names and lists multiple rules depending on simple word features as well as POS tags.

BIBREF5 adopt a machine learning approach for NER. Their NER system extracts medical problems, tests and treatments from discharge summaries and progress notes. They use a semi-Conditional Random Field (semi-CRF) BIBREF6 to output labels over all tokens in the sentence. They use a variety of
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1705.05437:1:2` | partial | 1:293 |

#### Rank 4: qasper-passage-v1-69c720678366c39a1a355c22840b81b29295300d52954b00fcca7e8715e24eb1

Passage ID: `qasper-passage-v1-69c720678366c39a1a355c22840b81b29295300d52954b00fcca7e8715e24eb1`; retrieval score: 4.1603381348552.

Word count: 150.

```text
similar to BIBREF24 . They test using manually annotated examples. They note that the F-score achieved are much lesser than that achieved in the general domain in BIBREF24 , and attribute to generally poorer performance of NER tools in the biomedical domain, as well as less training examples. BIBREF25 explore distant supervision methods for protein-protein interaction extraction.

More recently, deep learning methods have been applied to relation extraction in the biomedical domain. One of the main advantages of such methods over traditional feature or kernel based learning methods is that they require minimal feature engineering. In BIBREF26 , skip-gram vectors BIBREF27 are trained over 5.6Gb of unlabelled text. They use these vectors to extract protein-protein interactions by converting them into features for entities, context and the entire sentence. Using an SVM for classification, their method is able to outperform many kernel and feature based methods over a variety of datasets.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-6994347669035604aafaa4a0fd47bf6056afa4bbb172c28b53985b2a1d6a9101

Passage ID: `qasper-passage-v1-6994347669035604aafaa4a0fd47bf6056afa4bbb172c28b53985b2a1d6a9101`; retrieval score: 4.158752518571325.

Word count: 76.

```text
complexity of the task), they use Freebase BIBREF10 , a knowledge base that has some biomedical concepts as well. The lexicon learned using BioNELL is used to train an NER system. The system shows a very high precision, thereby showing that BioNELL learns very few ambiguous terms.

More recently, deep learning techniques have been developed to further enhance the performance of NER systems. BIBREF11 explore recurrent neural networks for the problem of NER in biomedical text.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 654.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "482b34cc6d8ca0cec7ba3e21662c46863c31bd6d": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1705.05437:1:2": [
        [
          293,
          853
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-f6885ab48a4d990f3f8ba803a210a42a24c211dd1df25560304f3df166a264bf

Passage ID: `qasper-passage-v1-f6885ab48a4d990f3f8ba803a210a42a24c211dd1df25560304f3df166a264bf`; retrieval score: 4.856225195948207.

Word count: 150.

```text
gathered from natural sources.

Natural language inference is also a well studied area of research, particularly on the MultiNLI BIBREF21 and SNLI BIBREF22 datasets. Other sources of entailment data include the PASCAL RTE challenges BIBREF23 , BIBREF24 or SciTail BIBREF25 . We note that, although SciTail, RTE-6 and RTE-7 did not use crowd workers to generate candidate statements, they still use sources (multiple choices questions or document summaries) that were written by humans with knowledge of the premise text. Using naturally occurring yes/no questions ensures even greater independence between the questions and premise text, and ties our dataset to a clear end-task. BoolQ also requires detecting entailment in paragraphs instead of sentence pairs.

Transfer learning for entailment has been studied in GLUE BIBREF7 and SentEval BIBREF26 . Unsupervised pre-training in general has recently shown excellent results on many datasets, including entailment data BIBREF9 , BIBREF8 , BIBREF27 .

Converting short-answer
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-f0766040d3c9126c8b1fc64794ca72acf67c153ac83385b28eb14c6c465e2fcd

Passage ID: `qasper-passage-v1-f0766040d3c9126c8b1fc64794ca72acf67c153ac83385b28eb14c6c465e2fcd`; retrieval score: 4.607105609031116.

Word count: 150.

```text
our dataset. Yes/No QA is closely related to many other NLP tasks, including other forms of question answering, entailment, and paraphrasing. Therefore, it is not clear what the best data sources to transfer from are, or if it will be sufficient to just transfer from powerful pre-trained language models such as BERT BIBREF8 or ELMo BIBREF9 . We experiment with state-of-the-art unsupervised approaches, using existing entailment datasets, three methods of leveraging extractive QA data, and using a few other supervised datasets.

We found that transferring from MultiNLI, and the unsupervised pre-training in BERT, gave us the best results. Notably, we found these approaches are surprisingly complementary and can be combined to achieve a large gain in performance. Overall, our best model reaches 80.43% accuracy, compared to 62.31% for the majority baseline and 90% human accuracy. In light of the fact BERT on its own has achieved human-like performance on several
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-c00ad10bfaab37892c9e24b9fa9a4f5381f074fdb016e296665a8b7c0e807e3c

Passage ID: `qasper-passage-v1-c00ad10bfaab37892c9e24b9fa9a4f5381f074fdb016e296665a8b7c0e807e3c`; retrieval score: 4.068617092173559.

Word count: 42.

```text
the best results. We use a batch size of 24, learning rate of 1e-5, and 5 training epochs for BERT and a learning rate of 6.25e-5, batch size of 6, language model loss of 0.5, and 3 training epochs for OpenAI GPT.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-2e069ff20b1d55296414df80ba07f9d5c5bedb9df451a4d0e91c943eb0ad428f

Passage ID: `qasper-passage-v1-2e069ff20b1d55296414df80ba07f9d5c5bedb9df451a4d0e91c943eb0ad428f`; retrieval score: 3.8776859780178556.

Word count: 150.

```text
to write yes/no questions, and who did not know the answer to the question they were asking. Figure contains some examples from our dataset. We find such questions often query for non-factoid information, and that human annotators need to apply a wide range of inferential abilities when answering them. As a result, they can be used to construct highly inferential reading comprehension datasets that have the added benefit of being directly related to the practical end-task of answering user yes/no questions.

Yes/No questions do appear as a subset of some existing datasets BIBREF3 , BIBREF4 , BIBREF5 . However, these datasets are primarily intended to test other aspects of question answering (QA), such as conversational QA or multi-step reasoning, and do not contain naturally occurring questions.

We follow the data collection method used by Natural Questions (NQ) BIBREF6 to gather 16,000 naturally occurring yes/no questions into a dataset we call
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-cfb8d874da3b2e21eae7a9b9fa0ee31547bdd5e878dc8743ac1d49f9278d3212

Passage ID: `qasper-passage-v1-cfb8d874da3b2e21eae7a9b9fa0ee31547bdd5e878dc8743ac1d49f9278d3212`; retrieval score: 3.7321377474586814.

Word count: 150.

```text
these kinds of inferences, previous work in natural language inference (NLI) proposed the task of labeling candidate statements as being entailed or contradicted by a given passage. However, in practice, generating candidate statements that test for complex inferential abilities is challenging. For instance, evidence suggests BIBREF0 , BIBREF1 , BIBREF2 that simply asking human annotators to write candidate statements will result in examples that typically only require surface-level reasoning.

In this paper we propose an alternative: we test models on their ability to answer naturally occurring yes/no questions. That is, questions that were authored by people who were not prompted to write particular kinds of questions, including even being required to write yes/no questions, and who did not know the answer to the question they were asking. Figure contains some examples from our dataset. We find such questions often query for non-factoid information, and that human annotators need to apply
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 642.

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

#### Rank 1: qasper-passage-v1-9899663125fb84a93d8cfdf380d0b3bf83c20d0351f3e13c3a769e42f513abd6

Passage ID: `qasper-passage-v1-9899663125fb84a93d8cfdf380d0b3bf83c20d0351f3e13c3a769e42f513abd6`; retrieval score: 3.2104953216117225.

Word count: 150.

```text
Work on representation learning is concerned with finding an appropriate representation of data in order to perform a machine learning task BIBREF33. In particular, deep learning exploits this concept by its very nature BIBREF2. Work on representation learning include Predictive State Representations (PSR) BIBREF34, BIBREF35, which capture the state as a vector of predictions of future outcomes, and a Heuristic Embedding of Markov Processes (HEMP) BIBREF36, which learns to embed transition probabilities using an energy-based optimization problem.

There has been extensive work attempting to use natural language in RL. Efforts that integrate language in RL develop tools, approaches, and insights that are valuable for improving the generalization and sample efficiency of learning agents. Previous work on language-conditioned RL has considered the use of natural language in the observation and action space. Environments such as Zork and TextWorld BIBREF37 have been the standard benchmarks for testing text-based games. Nevertheless, these environments
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-6e0ba579d350092793f1d92541b9e23c536fc3370c320f82a4c5e278688c16bf

Passage ID: `qasper-passage-v1-6e0ba579d350092793f1d92541b9e23c536fc3370c320f82a4c5e278688c16bf`; retrieval score: 2.748914312955955.

Word count: 150.

```text
There, a large amount of unnecessary objects were spawned in the level, increasing the state's description length to over 250 words, whilst retaining the same amount of useful information. Nevertheless, the NLP representation outperformed the vision and feature based representations, with high robustness to the applied noise.

In order to verify the performance of the natural language representation was not due to extensive discretization of patches, we've conducted experiments increasing the number of horizontal patches - ranging from 3 to 31 patches in the extreme case. Our results, as depicted in fig: patch count, indicate that the amount of discretization of patches did not affect the performance of the NLP agent, remaining a superior representation compared to the rest.

To conclude, our experiments suggest that NLP representations, though they describe the same raw information of the semantic segmentation maps, are more robust to task-nuisances, allow for better transfer, and achieve
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-727f086a3cf0790710a5c8fc696f95efd0dd74767f144600745ddbba6f5dcc63

Passage ID: `qasper-passage-v1-727f086a3cf0790710a5c8fc696f95efd0dd74767f144600745ddbba6f5dcc63`; retrieval score: 2.3104708042586934.

Word count: 92.

```text
agent, remaining a superior representation compared to the rest.

To conclude, our experiments suggest that NLP representations, though they describe the same raw information of the semantic segmentation maps, are more robust to task-nuisances, allow for better transfer, and achieve higher performance in complex tasks, even when their description is long and convoluted. While we've only presented results for DQN agents, we include plots for a PPO agent in the Appendix, showing similar trends and conclusions. We thus deduce that NLP-based semantic state representations are a preferable choice for training VizDoom agents.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-f5830bbac021c70acd5cc470008da496d0a516eb4051d487bfa5ef09f3997a73

Passage ID: `qasper-passage-v1-f5830bbac021c70acd5cc470008da496d0a516eb4051d487bfa5ef09f3997a73`; retrieval score: 1.9027374898025653.

Word count: 150.

```text
shotguns, ammunition and armor. Furthermore, the room is filled with unusable objects, various types of trees, pillars and other decorations. The agent can freely move and turn in any direction, as well as shoot. This scenario combines elements from all of the previous scenarios.

Our agent was implemented using a Convolutional Neural Network as described in Section SECREF4. We converted the parsed state into embedded representations of fixed length. We tested both a DQN and a PPO based agent, and compared the natural language representation to the other representation techniques, namely the raw image, feature vector, and semantic segmentation representations.

In order to effectively compare the performance of the different representation methods, we conducted our experiments under similar conditions for all agents. The same hyper-parameters were used under all tested representations. Moreover, to rule out effects of architectural expressiveness, the number of weights in all neural networks was approximately matched,
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-a4993d1bb15e8f984565e895138dcaff5b551e3919240338eaaf0e2b1c55ceff

Passage ID: `qasper-passage-v1-a4993d1bb15e8f984565e895138dcaff5b551e3919240338eaaf0e2b1c55ceff`; retrieval score: 1.8908204613964064.

Word count: 150.

```text
our main guideline was to keep the "front" patch narrow enough so it can be used as "sights".

our initial experiment was with 3 patches, and later we added 2 more patches classified as "outer left" and "outer right". In our experiments we have tested up to 51 patches, referred to as left or right patch with corresponding numbers.

we used 2 thresholds, which allowed us to classify the distance of an object from the player as "close","mid", and "far. Depending on the task, the value of the threshold can be changed, as well as adding more thresholds.

different states might generate sentence with different size. A maximum sentence length is another parameter that was tested. sentences-length-table presents some data regarding the average word count in some of the game sceanrios.

After the sentence describing the state is generated, it is transformed to an embedding vector. Words that were not
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 692.

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

#### Rank 1: qasper-passage-v1-2bf51ddda24970305a3d7b4cefeec8592f4ad92448c0db66d77209458afef8a4

Passage ID: `qasper-passage-v1-2bf51ddda24970305a3d7b4cefeec8592f4ad92448c0db66d77209458afef8a4`; retrieval score: 7.974047591171098.

Word count: 91.

```text
about the most relevant events, and being able to search, visualize and explore news clusters assists in gathering more insight about a particular story. Since relevant events may be spawned from any part of the world (and from many multilingual sources), it becomes imperative to cluster news across different languages.

In terms of granularity, the type of story clusters we are interested in are the group of articles which, for example : (i) Narrate recent air-strikes in Eastern Ghouta (Syria); (ii) Describe the recent launch of Space X's Falcon Heavy rocket.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-5ead85eec22dbe311c79cceb069e8059dfec6c1d23eefbd162d741de95bcd136

Passage ID: `qasper-passage-v1-5ead85eec22dbe311c79cceb069e8059dfec6c1d23eefbd162d741de95bcd136`; retrieval score: 6.500530116337741.

Word count: 150.

```text
Our system was designed to cluster documents from a (potentially infinite) real-word data stream. The datasets typically used in the literature (TDT, Reuters) have a small number of clusters ( INLINEFORM0 20) with coarse topics (economy, society, etc.), and therefore are not relevant to the use case of media monitoring we treat - as it requires much more fine-grained story clusters about particular events. To evaluate our approach, we adapted a dataset constructed for the different purpose of binary classification of joining cluster pairs. We processed it to become a collection of articles annotated with monolingual and crosslingual cluster labels.

Statistics about this dataset are given in Table TABREF30 . As described further, we tune the hyper-parameter INLINEFORM0 on the development set. As for the hyper-parameters related to the timestamp features, we fixed INLINEFORM1 and tuned INLINEFORM2 on the development set, yielding INLINEFORM3 . To compute IDF scores (which are
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1809.00540:6:1` | partial | 0:331 |

#### Rank 3: qasper-passage-v1-37137f11de7d6e31a908e469d101670ab4b6b11c968becec2dcc692fc7bbbcec

Passage ID: `qasper-passage-v1-37137f11de7d6e31a908e469d101670ab4b6b11c968becec2dcc692fc7bbbcec`; retrieval score: 6.221245312578514.

Word count: 150.

```text
we keep for the function INLINEFORM0 (see § SECREF3 ) are the average of reduced dimensional vectors of the incoming documents as generated by an incremental singular value decomposition (SVD) of a document-term matrix that is updated after each incoming document. However, we discovered that online LSA performs significantly worse than representing the documents the way is described in § SECREF4 . Furthermore, it was also significantly slower than our algorithm due to the time it took to perform singular value decomposition.

Table TABREF35 gives the final monolingual results on the three datasets. For English, we see that the significant improvement we get using our algorithm over the algorithm of aggarwal2006framework is due to an increased recall score. We also note that the trained models surpass the baseline for all languages, and that the timestamp feature (denoted by TS), while not required to beat the baseline, has a very relevant
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-2811b5ef08e08b73939ef0296b28566b61128bbc53afcaf91053b52ed670e630

Passage ID: `qasper-passage-v1-2811b5ef08e08b73939ef0296b28566b61128bbc53afcaf91053b52ed670e630`; retrieval score: 5.4618481074650225.

Word count: 150.

```text
aggarwal2006framework is due to an increased recall score. We also note that the trained models surpass the baseline for all languages, and that the timestamp feature (denoted by TS), while not required to beat the baseline, has a very relevant contribution in all cases. Although the results for both the baseline and our models seem to differ across languages, one can verify a consistent improvement from the latter to the former, suggesting that the score differences should be mostly tied to the different difficulty found across the datasets for each language. The presented scores show that our learning framework generalizes well to different languages and enables high quality clustering results.

To investigate the impact of the timestamp features, we ran an additional experiment using only the same three timestamp features as used in the best model on the English dataset. This experiment yielded scores of INLINEFORM0 , INLINEFORM1 and INLINEFORM2
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-52a6e9634fd26d5b3f85c5d90613a5f7c2af7c98e8427bc54472efee674b32c4

Passage ID: `qasper-passage-v1-52a6e9634fd26d5b3f85c5d90613a5f7c2af7c98e8427bc54472efee674b32c4`; retrieval score: 4.620255689077052.

Word count: 150.

```text
Our similarity metric computes weighted cosine similarity on the different subvectors, both in the case of monolingual clustering and crosslingual clustering. Formally, for the monolingual case, the similarity is given by a function defined as: DISPLAYFORM0

and is computed on the TF-IDF subvectors where INLINEFORM0 is the number of subvectors for the relevant document representation. For the crosslingual case, we discuss below the function INLINEFORM1 , which has a similar structure.

Here, INLINEFORM0 is the INLINEFORM1 th document in the stream and INLINEFORM2 is a monolingual cluster. The function INLINEFORM3 returns the cosine similarity between the document representation of the INLINEFORM4 th document and the centroid for cluster INLINEFORM5 . The vector INLINEFORM6 denotes the weights through which each of the cosine similarity values for each subvectors are weighted, whereas INLINEFORM7 denotes the weights for the timestamp features, as detailed further. Details on learning the weights INLINEFORM8 and INLINEFORM9 are
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 691.

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
      ],
      "1809.00540:6:1": [
        [
          331,
          601
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

#### Rank 1: qasper-passage-v1-e8a7eaf3172a44b7580327e6a1ea9938707c40519f09d60dd112f0dd7e970b42

Passage ID: `qasper-passage-v1-e8a7eaf3172a44b7580327e6a1ea9938707c40519f09d60dd112f0dd7e970b42`; retrieval score: 4.390920113614369.

Word count: 95.

```text
Figure FIGREF1 shows the architecture of the Sequicity framework as described in BIBREF8. In essence, in each turn, the Sequicity model first takes a bspan ($B_1$) and a response ($R_1$) which are determined in the previous step, and the current human question ($U_2$) to generate the current bspan. This bspan is then used together with a knowledge base to generate the corresponding machine answer ($R_2$), as shown in the right part of Figure FIGREF1.

The left part of that figure shows an example dialogue in a mixed-domain setting (which will be explained in Section SECREF3).
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-c12cdd78ef0632fb1de83ae1376b088f8b2d42083c211732a12fdb0c277c60f1

Passage ID: `qasper-passage-v1-c12cdd78ef0632fb1de83ae1376b088f8b2d42083c211732a12fdb0c277c60f1`; retrieval score: 2.9174340747971566.

Word count: 150.

```text
We use the publicly available dataset KVRET BIBREF5 in our experiments. This dataset is created by the Wizard-of-Oz method BIBREF10 on Amazon Mechanical Turk platform. This dataset includes dialogues in 3 domains: calendar, weather, navigation (POI) which is suitable for our mix-domain dialogue experiments. There are 2,425 dialogues for training, 302 for validation and 302 for testing, as shown in the upper half of Table TABREF12.

In this original dataset, each dialogue is of a single domain where all of its turns are on that domain. Each turn is composed of a sentence pair, one sentence is a user utterance, the other sentence is the corresponding machine response. A dialogue is a sequence of turns. To create mix-domain dialogues for our experiments, we make some changes in this dataset as follows:

We keep the dialogues in the calendar domain as they are.

We take a half of dialogues in the
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1909.02265:5:0` | full | 0:434 |

#### Rank 3: qasper-passage-v1-ef457a3431067ab104795a2ec33f07765ed8b08713b58b98226ea195291c6746

Passage ID: `qasper-passage-v1-ef457a3431067ab104795a2ec33f07765ed8b08713b58b98226ea195291c6746`; retrieval score: 2.706384604726405.

Word count: 150.

```text
is a sequence of turns. To create mix-domain dialogues for our experiments, we make some changes in this dataset as follows:

We keep the dialogues in the calendar domain as they are.

We take a half of dialogues in the weather domain and a half of dialogues in the POI domain and mix their turns together, resulting in a dataset of mixed weather-POI dialogues. In this mixed-domain dialogue, there is a turn in the weather domain, followed by a turn in POI domain or vice versa.

We call this dataset the sequential turn dataset. Since the start turn of a dialogue has a special role in triggering the learning systems, we decide to create another and different mixed-domain dataset with the following mixing method:

The first turn and the last turn of each dialogue are kept as in their original.

The internal turns are mixed randomly.

We call this dataset
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-6ec67f1b584da2670ea4061f49e31d84d31929a5c7842f6e2764e3063f8ca28a

Passage ID: `qasper-passage-v1-6ec67f1b584da2670ea4061f49e31d84d31929a5c7842f6e2764e3063f8ca28a`; retrieval score: 2.6664805537296825.

Word count: 136.

```text
answer at the third turn (monday instead of this_week).

The third turn is of domain weather and the fourth turn is switched to domain POI. The bspan value cleveland is retained through cross domain, resulting in an error in the fourth turn, where cleveland is shown instead of home. This example demonstrates a weakness of the system when being trained on a mixed-domain dataset. In the fifth turn, since the system does not recognize the value fastest in the bspan, it generates a random and wrong value moderate traffic. Note that the generated answer of the sixth turn is correct despite of the wrong predicted bspan; however, it is likely that if the dialogue continues, this wrong bspan may result in more answer mistakes. In such situations, multi-domain belief tracker usually performs better at bspan prediction.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-ddb00fd56af1036ece73d539dc24b9c9223a55288c22c4fdaf60ceea618db8a5

Passage ID: `qasper-passage-v1-ddb00fd56af1036ece73d539dc24b9c9223a55288c22c4fdaf60ceea618db8a5`; retrieval score: 2.4974596293913747.

Word count: 150.

```text
he would either switch to a new domain or come back to ask about some other property of the suggested restaurant. This is a realistic scenario which usually happens in practical chatbot applications in our observations. We prefer calling this problem mixed-domain dialogue rather than multiple-domain dialogue.

Second, we study the effect of the mixed-domain setting in the context of multi-domain dialogue approaches to see how they perform in different experimental scenarios.

The main findings of this work include:

A specialized state tracking component in multiple domains still plays an important role and gives better results than a state-of-the-art end-to-end task-oriented dialogue system.

A combination of specialized state tracking system and an end-to-end task-oriented dialogue system is beneficial in mix-domain dialogue systems. Our hybrid system is able to improve the belief tracking accuracy of about 28% of average absolute point on a standard multi-domain dialogue dataset.

These experimental results give
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 681.

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

#### Rank 1: qasper-passage-v1-726fda30af417a53b6c4150c9ab1f35b22724b56ad1321a349402ff92e3af50a

Passage ID: `qasper-passage-v1-726fda30af417a53b6c4150c9ab1f35b22724b56ad1321a349402ff92e3af50a`; retrieval score: 9.788835917302292.

Word count: 150.

```text
The experiments presented here extend and refine a line of research investigating what linguistic knowledge is acquired by neural language models. Previous studies have demonstrated that sequential models trained on a simple regime of optimizing the next word can learn long-distance syntactic dependencies in impressive detail. Our results provide complimentary insights, demonstrating that a range of model architectures trained on a variety of datasets can learn fine-grained information about the interaction of CoordNPs and local syntactic context, but their behavior remains unhumanlike in many key ways. Furthermore, to our best knowledge, this work presents the first psycholinguistic analysis of neural language models trained on French, a high-resource language that has so far been under-investigated in this line of research.

In the simple coordination experiment, we demonstrated that models were able to capture some of the agreement behaviors of humans, although their performance deviated in crucial aspects. Whereas human behavior is
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-67ab8689f52860b7d09eceb832493b635d671b6ebfc12556b1f4559d6848fab5

Passage ID: `qasper-passage-v1-67ab8689f52860b7d09eceb832493b635d671b6ebfc12556b1f4559d6848fab5`; retrieval score: 9.384200071788491.

Word count: 150.

```text
This section further investigates the effects of CoordNP annotation schemes on the behaviors of structurally-supervised models. We test whether an explicit COORD phrasal tag improves model performance. We trained two additional RNNG models on 38,546 sentences from the Penn Treebank annotated with two different schemes: The first, RNNG (PTB-control) was trained with the original Penn Treebank annotation. The second, RNNG (PTB-coord), was trained on the same sentences, but with an extended coordination annotation scheme, meant to employ the scheme employed in the FTB, adapted from BIBREF26. We stripped empty categories from their scheme and only kept the NP-COORD label for constituents inside a coordination structure. Figure FIGREF26 illustrates the detailed annotation differences between two datasets. We tested both models on all the experiments presented in Sections SECREF3-SECREF6 above.

Turning to the results of these six experiments: We see little difference between the two models in the Non-coordination agreement experiment. For
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-5f22a6e1e7d21c59e586d6fae94c4db6eefe50654686b411f577d61a43c76cad

Passage ID: `qasper-passage-v1-5f22a6e1e7d21c59e586d6fae94c4db6eefe50654686b411f577d61a43c76cad`; retrieval score: 8.02155042595129.

Word count: 85.

```text
English language models: one trained on the Billion Word benchmark (referred as `LSTM (1B)') from BIBREF14, and the other trained on English Wikipedia (referred as `LSTM (enWiki)') from BIBREF3. For French, we trained a large LSTM language model (referred as `LSTM (frWaC)') on a random subset (about 4 million sentences, 138 million word tokens) of the frWaC dataset BIBREF15. We set the size of the input embeddings and hidden layers to 400 for the LSTM (frWaC) model since it is trained on a large dataset.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1909.04625:2:1` | partial | 93:602 |

#### Rank 4: qasper-passage-v1-4b54345d3067f7503d23bb3aa76c28acbe9663000fa46e2d8840e354b5a7717a

Passage ID: `qasper-passage-v1-4b54345d3067f7503d23bb3aa76c28acbe9663000fa46e2d8840e354b5a7717a`; retrieval score: 7.01494538710375.

Word count: 150.

```text
annotation differences between two datasets. We tested both models on all the experiments presented in Sections SECREF3-SECREF6 above.

Turning to the results of these six experiments: We see little difference between the two models in the Non-coordination agreement experiment. For the Complex coordination control and Complex coordination critical experiments, both models are largely the same as well. However, in the Simple and-coordination and Simple or-coordination experiments the values for all conditions are shifted upwards for the RNNG PTB-coord model, indicating higher over-all preference for the plural continuation. Furthermore, the range of values is reduced in the RNNG PTB-coord model, compared to the RNNG PTB-control model. These results indicate that adding an explicit COORD phrasal label does not drastically change model performance: Both models still appear to be using a linear combination of number features to drive plural vs. singular expectation. However, the explicit representation has made the interior of the
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-c4c59de61637b4f9ca5e7d9450a7456b18b48fe40f54964fe07910a2a6cb3d56

Passage ID: `qasper-passage-v1-c4c59de61637b4f9ca5e7d9450a7456b18b48fe40f54964fe07910a2a6cb3d56`; retrieval score: 6.952090518959581.

Word count: 150.

```text
and (or is grammatical in all conditions, so it is omitted from this study). Our expectation is that `and' is less surprising in the Vpl_Nsg condition than in the Vsg_Nsg condition, where a CoordNP is not licensed by the grammar in either French or English (as in *What is the pig and the cat eating?). We also expect lower surprisal for and in the Vpl_Nsg condition, where it is obligatory for a grammatical continuation, than in the Vpl_Npl condition, where it is optional.

For French experimental items, the question is embedded into a sentential-complement taking verb, following Example SECREF6, due to the fact that unembedded subject-verb inverted questions sound very formal and might be relatively rare in the training data.

. Je me demande où vont le maire et

I myself ask where go.3PL the.MSG mayor.MSG and

The results for both languages are shown in Figure FIGREF25, with the surprisal
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 685.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "0779f8ebeeb399bdf0300bd70e072d054d56bb77": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1909.04625:2:0": [
        [
          0,
          622
        ]
      ],
      "1909.04625:2:1": [
        [
          0,
          93
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-01fbf42c21c970b8d18a8f71c2b71ff301d542d61bd56a80b25da6fbe8423c8b

Passage ID: `qasper-passage-v1-01fbf42c21c970b8d18a8f71c2b71ff301d542d61bd56a80b25da6fbe8423c8b`; retrieval score: 2.8420959729134885.

Word count: 150.

```text
Future work. For future work, we plan to validate our findings using another dataset, e.g., by recommending tags for scientific articles and books in BibSonomy. With this, we aim to demonstrate the usefulness of the proposed approach in a similar domain and to enhance the reproducibility of our results by using an open dataset.

Moreover, we plan to evaluate our tag recommendation approaches in a study with domain users. Also, we want to improve our similarity-based approaches by integrating novel embedding approaches BIBREF16 , BIBREF17 as we did, for example, with our proposed semantic similarity evaluation metric. Finally, we aim to incorporate explanations for recommended tags so that editors of e-book annotations receive additional support in annotating e-books BIBREF21 . By making the underlying (semantic) reasoning visible to the editor who is in charge of tailoring annotations, we aim to support two goals: (i) allowing readers to discover e-books more
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-01f796eebaf35d16775faa76e90770f280b6998638ec9f00c0785ebf0c99598f

Passage ID: `qasper-passage-v1-01f796eebaf35d16775faa76e90770f280b6998638ec9f00c0785ebf0c99598f`; retrieval score: 2.7442052807627038.

Word count: 150.

```text
We implement three types of tag recommendation approaches, i.e., (i) popularity-based, (ii) similarity-based (i.e., using content information), and (iii) hybrid approaches. Due to the lack of personalized tags (i.e., we do not know which user has assigned a tag), we do not implement other types of algorithms such as collaborative filtering BIBREF8 . In total, we evaluate 19 different algorithms to recommend tags for annotating e-books.

Popularity-based approaches. We recommend the most frequently used tags in the dataset, which is a common strategy for tag recommendations BIBREF9 . That is, a most popular INLINEFORM0 approach for editor tags and a most popular INLINEFORM1 approach for Amazon search terms. For e-books, for which we also have author (= INLINEFORM2 and INLINEFORM3 ) or BISAC (= INLINEFORM4 and INLINEFORM5 ) information, we use these features to further filter the recommended tags, i.e., to only recommend tags that were used to annotate e-books
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-bc1e43acd236f65b876b7f0d9c11baa9e3d9d7699b2e49283d029e52c3b75a7e

Passage ID: `qasper-passage-v1-bc1e43acd236f65b876b7f0d9c11baa9e3d9d7699b2e49283d029e52c3b75a7e`; retrieval score: 2.091759841102955.

Word count: 140.

```text
contexts.

Data used to evaluate recommendations. For evaluation, we use a third set of e-book annotations, namely Amazon review keywords. These review keywords are extracted from the Amazon review texts and are typically provided in the review section of books on Amazon. Our idea is to not favor one or the other data source (i.e., editor tags and Amazon search terms) when evaluating our approaches against expected tags. At the same time, we consider Amazon review keywords to be a good mixture of editor tags and search terms as they describe both the content and the users' opinions on the e-books (i.e., the readers' vocabulary). As shown in Table TABREF3 , we collect Amazon review keywords for 2,896 e-books (publishers: Kiwi, Rowohlt, Fischer, and Droemer), which leads to 33,663 distinct review keywords and on average 30 keyword assignments per e-book.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-6c6c2596ca0d4c1e05482b0716047533e50365d2013f18cbcba99ab38eafbfbc

Passage ID: `qasper-passage-v1-6c6c2596ca0d4c1e05482b0716047533e50365d2013f18cbcba99ab38eafbfbc`; retrieval score: 2.0580338673123304.

Word count: 150.

```text
for which we also have author (= INLINEFORM2 and INLINEFORM3 ) or BISAC (= INLINEFORM4 and INLINEFORM5 ) information, we use these features to further filter the recommended tags, i.e., to only recommend tags that were used to annotate e-books of a specific author or a specific BISAC.

We combine both data sources (i.e., editor tags and Amazon search terms) using a round-robin combination strategy, which ensures an equal weight for both sources. This gives us three additional popularity-based algorithms (= INLINEFORM0 , INLINEFORM1 and INLINEFORM2 ).

Similarity-based approaches. We exploit the textual content of e-books (i.e., description or title) to recommend relevant tags BIBREF10 . For this, we first employ a content-based filtering approach BIBREF11 based on TF-IDF BIBREF12 to find top- INLINEFORM0 similar e-books. For each of the similar e-books, we then either extract the assigned editor tags (= INLINEFORM2 and INLINEFORM3 ) or the Amazon search terms
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-0e871c525673875fb64e79fb5ff9f8fbb2d90b2b5227b80695f910fd47556fe6

Passage ID: `qasper-passage-v1-0e871c525673875fb64e79fb5ff9f8fbb2d90b2b5227b80695f910fd47556fe6`; retrieval score: 2.025378181829589.

Word count: 150.

```text
Amazon to mimic the vocabulary of users in Amazon, who search for e-books. We combine these search terms with tags assigned by editors in a hybrid tag recommendation approach. Thus, our aim is to show that we can improve the performance of tag recommender systems for e-books both concerning recommendation accuracy as well as semantic similarity and tag recommendation diversity.

Related work. In tag recommender systems, mostly content-based algorithms (e.g., BIBREF4 , BIBREF5 ) are used to recommend tags to annotate resources such as e-books. In our work, we incorporate both content features of e-books (i.e., title and description text) as well as Amazon search terms to account for the vocabulary of e-book readers.

Concerning the evaluation of tag recommendation systems, most studies focus on measuring the accuracy of tag recommendations (e.g., BIBREF2 ). However, the authors of BIBREF6 suggest also to use beyond-accuracy metrics such as diversity to evaluate
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 740.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "3f761bb5857701886da42838934df5de71626245": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1908.04042:0:5": [
        [
          0,
          791
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-b66bf940ec1252b22e18032b743b56f6a9b69bd215999889b3eafe90fec810f2

Passage ID: `qasper-passage-v1-b66bf940ec1252b22e18032b743b56f6a9b69bd215999889b3eafe90fec810f2`; retrieval score: 8.919322906566386.

Word count: 150.

```text
holistic regularisation VAE (HR-VAE), which can effectively avoid latent variable collapse. In contrast to existing VAE-RNN models for text modelling which merely impose a standard normal distribution prior on the last hidden state of the RNN encoder, our HR-VAE model imposes regularisation for all hidden states of the RNN encoder. Another advantage of our model is that it is generic and can be applied to any existing VAE-RNN-based architectures.

We evaluate our model against several strong baselines which apply VAE for text modelling BIBREF0, BIBREF7, BIBREF5. We conducted experiments based on two public benchmark datasets, namely, the Penn Treebank dataset BIBREF9 and the end-to-end (E2E) text generation dataset BIBREF10. Experimental results show that our HR-VAE model not only can effectively mitigate the latent variable collapse issue with a stable training process, but also can give better predictive performance than the baselines, as evidenced by both quantitative (e.g., negative log likelihood
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-8d25530d8fef23a262f6fc40f22d581f8da60d41dafd663f78d87fcc1dd1884f

Passage ID: `qasper-passage-v1-8d25530d8fef23a262f6fc40f22d581f8da60d41dafd663f78d87fcc1dd1884f`; retrieval score: 7.261030088619352.

Word count: 72.

```text
We evaluate our model on two public datasets, namely, Penn Treebank (PTB) BIBREF9 and the end-to-end (E2E) text generation corpus BIBREF10, which have been used in a number of previous works for text generation BIBREF0, BIBREF5, BIBREF11, BIBREF12. PTB consists of more than 40,000 sentences from Wall Street Journal articles whereas the E2E dataset contains over 50,000 sentences of restaurant reviews. The statistics of these two datasets are summarised in Table TABREF11.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-0ace6d2fdcd00524304ce8f3b3d20558a9d05c67f43807b40710145a5490cfc8

Passage ID: `qasper-passage-v1-0ace6d2fdcd00524304ce8f3b3d20558a9d05c67f43807b40710145a5490cfc8`; retrieval score: 5.584217400342773.

Word count: 150.

```text
KL loss only depends on the concentration parameter which is fixed during training and testing, and hence results in a constant KL loss. In a more recent work, BIBREF6 avoided latent variable collapse by including skip connections in the generative model, where the skip connections enforce strong links between the latent variables and the likelihood function.

Although the aforementioned works show effectiveness in addressing the latent variable collapse issue to some extent, they either require carefully engineering to balance the weight between the reconstruction loss and KL loss BIBREF0, BIBREF8, or resort to designing more sophisticated model structures BIBREF7, BIBREF5, BIBREF6.

In this paper, we present a simple architecture called holistic regularisation VAE (HR-VAE), which can effectively avoid latent variable collapse. In contrast to existing VAE-RNN models for text modelling which merely impose a standard normal distribution prior on the last hidden state of the RNN encoder, our HR-VAE model
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-bae6cacb309fd0bbb5b7b42e3535b76b8050faa06d7136fa10192ec713f21a52

Passage ID: `qasper-passage-v1-bae6cacb309fd0bbb5b7b42e3535b76b8050faa06d7136fa10192ec713f21a52`; retrieval score: 5.336759280442116.

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

#### Rank 5: qasper-passage-v1-b38b9039adfc4bd0859803e283452e36602cb055c203169db573694e3a4161c1

Passage ID: `qasper-passage-v1-b38b9039adfc4bd0859803e283452e36602cb055c203169db573694e3a4161c1`; retrieval score: 3.833883211516807.

Word count: 150.

```text
latent codes in generative tasks.

Various efforts have been made to alleviate the latent variable collapse issue. BIBREF0 uses KL annealing, where a variable weight is added to the KL term in the cost function at training time. BIBREF7 discovered that there is a trade-off between the contextual capacity of the decoder and effective use of encoding information, and developed a dilated CNN as decoder which can vary the amount of conditioning context. They also introduced a loss clipping strategy in order to make the model more robust. BIBREF5 addressed the problem by replacing the standard normal distribution for the prior with the von Mises-Fisher (vMF) distribution. With vMF, the KL loss only depends on the concentration parameter which is fixed during training and testing, and hence results in a constant KL loss. In a more recent work, BIBREF6 avoided latent variable collapse by including skip connections in the generative
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 604.

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

#### Rank 1: qasper-passage-v1-5c1dbc9e8fd096987e86da30b8193e09b7b79ffa3ac48e06e9c55be66c24b2ca

Passage ID: `qasper-passage-v1-5c1dbc9e8fd096987e86da30b8193e09b7b79ffa3ac48e06e9c55be66c24b2ca`; retrieval score: 9.43831033673766.

Word count: 105.

```text
of raters, the use of linguistic context, and the creation of reference translations. We focus on the data shared by BIBREF3, and empirically test to what extent changes in the evaluation design affect the outcome of the human evaluation. We find that for all three aspects, human translations are judged more favourably, and significantly better than MT, when we make changes that we believe strengthen the evaluation design. Based on our empirical findings, we formulate a set of recommendations for human MT evaluation in general, and assessing human–machine parity in particular. All of our data are made publicly available for external validation and further analysis.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-9aa3b039dce935a7a0124ed5ec5e8b6d7a970de0a46fc88037b6852bd035657f

Passage ID: `qasper-passage-v1-9aa3b039dce935a7a0124ed5ec5e8b6d7a970de0a46fc88037b6852bd035657f`; retrieval score: 8.745406440803368.

Word count: 150.

```text
a source-based direct assessment with non-expert annotators, using data sets and the evaluation protocol of the Conference on Machine Translation (WMT). While the results are intriguing, especially because they are based on best practices in MT evaluation, BIBREF5 warn against taking their results as evidence for human–machine parity, and caution that for well-resourced language pairs, an update of WMT evaluation style will be needed to keep up with the progress in machine translation. We concur that these findings have demonstrated the need to critically re-evaluate the design of human MT evaluation.

Our paper investigates three aspects of human MT evaluation, with a special focus on assessing human–machine parity: the choice of raters, the use of linguistic context, and the creation of reference translations. We focus on the data shared by BIBREF3, and empirically test to what extent changes in the evaluation design affect the outcome of the human evaluation. We
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-4e045cc3eb1de86eff196ecc30b7d229d3f10d17ce17f5c03d522529b8c424ca

Passage ID: `qasper-passage-v1-4e045cc3eb1de86eff196ecc30b7d229d3f10d17ce17f5c03d522529b8c424ca`; retrieval score: 7.613946161625616.

Word count: 150.

```text
We compared professional human Chinese to English translations to the output of a strong MT system. In a human evaluation following best practices, BIBREF3 found no significant difference between the two, concluding that their NMT system had reached parity with professional human translation. Our blind qualitative analysis, however, showed that the machine translation output contained significantly more incorrect words, omissions, mistranslated names, and word order errors.

Our experiments show that recent findings of human–machine parity in language translation are owed to weaknesses in the design of human evaluation campaigns. We empirically tested alternatives to what is currently considered best practice in the field, and found that the choice of raters, the availability of linguistic context, and the creation of reference translations have a strong impact on perceived translation quality. As for the choice of raters, professional translators showed a significant preference for human translation, while non-expert raters did not. In
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-5ff2262bf972bf996bbb47117d7c806b9759d80d934ab2e537a006661ab88bd4

Passage ID: `qasper-passage-v1-5ff2262bf972bf996bbb47117d7c806b9759d80d934ab2e537a006661ab88bd4`; retrieval score: 6.935229998376287.

Word count: 117.

```text
magnitude of the differences, so that it is not possible to determine how much better system A was than system B.

This is one of the reasons why direct assessment has prevailed as an evaluation method more recently. In contrast to relative ranking, the raters are presented with one MT output at a time, to which they assign a score between 0 and 100. To increase homogeneity, each rater's ratings are standardised BIBREF11. Reference translations serve as the basis in the context of WMT, and evaluations are carried out by monolingual raters. To avoid reference bias, the evaluation can be based on source texts instead, which presupposes bilingual raters, but leads to more reliable results overall BIBREF12.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-ddac241a7ae51b96f83391b95ffc5d21f6794d1f4c0f0a66a9f1ae5c0ad03e05

Passage ID: `qasper-passage-v1-ddac241a7ae51b96f83391b95ffc5d21f6794d1f4c0f0a66a9f1ae5c0ad03e05`; retrieval score: 6.513452413311045.

Word count: 72.

```text
Our experiments in Sections SECREF3–SECREF5 show that machine translation quality has not yet reached the level of professional human translation, and that human evaluation methods which are currently considered best practice fail to reveal errors in the output of strong NMT systems. In this section, we recommend a set of evaluation design changes that we believe are needed for assessing human–machine parity, and will strengthen the human evaluation of MT in general.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 594.

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

#### Rank 1: qasper-passage-v1-1316f3106f203d6fc9bd4a5d621b783c9e9447bf5c2896dae319f07810340cd4

Passage ID: `qasper-passage-v1-1316f3106f203d6fc9bd4a5d621b783c9e9447bf5c2896dae319f07810340cd4`; retrieval score: 9.443116729562899.

Word count: 104.

```text
We set up experiments in order to answer the following research questions:

RQ1: Can the comparative evaluator correlate better with human preference in sample-level than previous automated metrics when evaluating open domain NLG models?

RQ2: Can the comparative evaluator correlate better with human preference in model-level, so that our approach can measure the progress on open domain NLG better?

RQ3: As existing approaches fail to correlate well with human preference, whether and to what extent this problem affects the quality of the final NLG model when performing hyperparameter search and early-stopping?

RQ4: If the previous problem exists, can proposed comparative evaluator reduce this problem?
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-12b621f5708a08ac683e39f10691f6967bf0be82ab9215de8d503676012252be

Passage ID: `qasper-passage-v1-12b621f5708a08ac683e39f10691f6967bf0be82ab9215de8d503676012252be`; retrieval score: 2.9832766246603737.

Word count: 150.

```text
Evaluation of NLG models has been a long-standing open problem. While human evaluation may be ideal, it is generally expensive to conduct and does not scale well. Various automated evaluation approaches are proposed to facilitate the development and evaluation of NLG models. We summarize these evaluation approaches below.

Text Overlap Metrics, including BLEU BIBREF5, METEOR BIBREF6 and ROUGE BIBREF7, are the most popular metrics employed in the evaluation of NLG models. They evaluate generated text by comparing the similarity between the generated text and human written references. While this works well in tasks where the diversity of acceptable output is limited, such as machine translation and text summarization, text overlap metrics are shown to have weak or no correlation with human judgments in open domain natural language generation tasks BIBREF8. There are two major drawbacks in these metrics. First, text overlap metrics can not distinguish minor variations in a generated
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2002.05058:1:0` | full | 0:323 |
| `2002.05058:1:1` | partial | 0:669 |

#### Rank 3: qasper-passage-v1-9f78a8685a7317a8ab43969d0abf48a3adb2c1bdb8b24c10665d5a7e272bb464

Passage ID: `qasper-passage-v1-9f78a8685a7317a8ab43969d0abf48a3adb2c1bdb8b24c10665d5a7e272bb464`; retrieval score: 2.876029711956525.

Word count: 94.

```text
in Table 3. We can see that conventional automated metrics perform poorly and result in sub-optimal result when performing hyperparameter search and selecting the best performing checkpoints. Converting evaluation metric from BLEU or perplexity to the proposed comparative evaluator can yield non-neglectable improvements without changing model architecture or training objective. While previous work on NLG evaluation mostly focuses on the evaluation stage and does not explore the influence of imperfect metrics during model training, our experiments demonstrate the existence of this problem and that the proposed method can, to some extent, alleviate this problem.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-211c5d7007b5954fa11824bfb884dd5b252ed3775e01faa3e05852eb5e02a11b

Passage ID: `qasper-passage-v1-211c5d7007b5954fa11824bfb884dd5b252ed3775e01faa3e05852eb5e02a11b`; retrieval score: 2.6364453248674207.

Word count: 64.

```text
skill rating among all models trained with different hyperparameter choices. For early-stopping, as incrementally performing skill rating is computationally expensive, we propose to perform n (e.g. 1000) pairwise comparison between the samples generated by the latest checkpoint and the previous k (e.g. 2) checkpoints and stop training when the wining rate of latest checkpoint keeps being smaller than its losing rate for 5 iterations.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-231342f3ec6639fb3b0c9dbe610f1a2f9e1d4b0feb746ea9d14e7f29d9fedb97

Passage ID: `qasper-passage-v1-231342f3ec6639fb3b0c9dbe610f1a2f9e1d4b0feb746ea9d14e7f29d9fedb97`; retrieval score: 2.3068036707955017.

Word count: 150.

```text
As our objective is to evaluate the evaluators rather than comparing state-of-the-art models, we choose three representative sequence-to-sequence architectures: LSTM BIBREF27 seq2seq, Convolutional seq2seq BIBREF28, and transformer BIBREF1 model. We compare models with different architectures, hyperparameter choices, and early-stopping criteria with different automated metrics, as well as human evaluation.

Regarding the evaluation metric (and criteria for choosing hyperparameter choice and early-stopping), we compare the proposed approach with the discriminative evaluator, BLEU score (average of 2-, 3-, 4-grams), perplexity, and ADEM. When evaluating generated stories, we cut off the story at the nearest sentence for stories longer than 250 words.

The proposed comparative evaluator is employed for choosing hyperparameter by performing skill rating among all models trained with different hyperparameter choices. For early-stopping, as incrementally performing skill rating is computationally expensive, we propose to perform n (e.g. 1000) pairwise comparison between the samples generated by the latest checkpoint and the previous
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 562.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "d449825aa0a1d27531a41dd5ec098834f1fde4a8": {
    "unresolved_evidence": [],
    "paragraphs": {
      "2002.05058:1:1": [
        [
          669,
          897
        ]
      ],
      "2002.05058:1:2": [
        [
          0,
          473
        ]
      ],
      "2002.05058:1:3": [
        [
          0,
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

#### Rank 1: qasper-passage-v1-89448046b9650e597f8ff2d99220960065b703506193f31489def98e4f9a002b

Passage ID: `qasper-passage-v1-89448046b9650e597f8ff2d99220960065b703506193f31489def98e4f9a002b`; retrieval score: 9.489927794609748.

Word count: 138.

```text
This paper presented the UDS-DFKI system submitted to the Similar Language Translation shared task at WMT 2019. We presented the results obtained by our system in translating from Czech to Polish. Our system achieved competitive performance ranking second among ten teams in the competition in terms of BLEU score. The fact that out-of-domain data was provided by the organizers resulted in a challenging but interesting scenario for all participants.

In future work, we would like to investigate how effective is the proposed hypothesis (i.e., word-BPE level information) in similar language translation. Furthermore, we would like to explore the similarity between these two languages (and the other two language pairs in the competition) in more detail by training models that can best capture morphological differences between them. During such competitions, this is not always possible due to time constraints.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-42bd14f9496ecc7224935747b9aaab7817899f05525ab5c58b12823b53ef9057

Passage ID: `qasper-passage-v1-42bd14f9496ecc7224935747b9aaab7817899f05525ab5c58b12823b53ef9057`; retrieval score: 8.495349503266125.

Word count: 147.

```text
the first time at WMT 2019 with the purpose of evaluating the performance of MT systems on three pairs of similar languages from three different language families: Ibero-Romance, Indo-Aryan, and Slavic.

The Similar Language Translation BIBREF2 task provided participants with training, development, and testing data from the following language pairs: Spanish - Portuguese (Romance languages), Czech - Polish (Slavic languages), and Hindi - Nepali (Indo-Aryan languages). Participant could submit system outputs to any of the three language pairs in any direction. The shared task attracted a good number of participants and the performance of all entries was evaluated using popular MT automatic evaluation metrics, namely BLEU BIBREF3 and TER BIBREF4.

In this paper we describe the UDS-DFKI system to the WMT 2019 Similar Language Translation task. The system achieved competitive performance and ranked second among ten entries in Czech to Polish translation in terms of BLEU score.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-eb9171f451145007606044de3f7b29869d760f5868344115d8372aa41282dd61

Passage ID: `qasper-passage-v1-eb9171f451145007606044de3f7b29869d760f5868344115d8372aa41282dd61`; retrieval score: 5.748787262533579.

Word count: 150.

```text
We present the results obtained by our system in Table TABREF8.

Our fine-tuned system on development set provides significant performance improvement over the generic model. We found +12.9 absolute BLEU points improvement over the generic model. Similar improvement is also observed in terms of TER (-16.9 absolute). It is to be noted that our generic model is trained solely on the clean version of training data.

Before submission, we performed punctuation normalization, unicode normalization, and detokenization for the run.

In Table TABREF9 we present the ranking of the competition provided by the shared task organizers. Ten entries were submitted by five teams and are ordered by BLEU score. TER is reported for all submissions which achieved BLEU score greater than 5.0. The type column specifies the type of system, whether it is a Primary (P) or Constrastive (C) entry.

Our system was ranked second in the competition only 0.3 BLEU
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-472fd4d917a66e306aec33e094b59582f2a6025c7ca2bb3ff2d56c0f64b2bebd

Passage ID: `qasper-passage-v1-472fd4d917a66e306aec33e094b59582f2a6025c7ca2bb3ff2d56c0f64b2bebd`; retrieval score: 5.206873336402584.

Word count: 76.

```text
reported for all submissions which achieved BLEU score greater than 5.0. The type column specifies the type of system, whether it is a Primary (P) or Constrastive (C) entry.

Our system was ranked second in the competition only 0.3 BLEU points behind the winning team UPC-TALP. The relative low BLEU and high TER scores obtained by all teams are due to out-of-domain data provided in the competition which made the task equally challenging to all participants.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-996178d2aab49fc4ca3be90309fde92a053d8936019d99ac30a786638c49a3c8

Passage ID: `qasper-passage-v1-996178d2aab49fc4ca3be90309fde92a053d8936019d99ac30a786638c49a3c8`; retrieval score: 4.324414291675323.

Word count: 150.

```text
we use the first 1,000 for validation and the remaining as training data. The released development set (Dev) is used as test data for our experiment. It should be noted noted that, we exclude 1,000 sentences from the General corpus which are scored as top (i.e., more in-domain like) during the data selection process.

We prepare two parallel training sets from the aforementioned training data: (i) transference500K(presented next), collected 500,000 parallel data through data selection method BIBREF11, which are very similar to the in-domain data (for our case the development set), and (ii) transferenceALL, utilizing all the released out-domain data sorted by Equation DISPLAY_FORM2.

The transference500Ktraining set is prepared using in-domain (development set) bilingual cross-entropy difference for data selection as was described in Axelrod:2011. The difference in cross-entropy is computed based on two language models (LM): a domain-specific LM is estimated from the in-domain (containing 2050 sentences) corpus ($lm_{i}$) and
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 661.

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

#### Rank 1: qasper-passage-v1-f52fe1250b591750ed2da78d070ef6f4cd57d98a66452f491fcc242707a4ad14

Passage ID: `qasper-passage-v1-f52fe1250b591750ed2da78d070ef6f4cd57d98a66452f491fcc242707a4ad14`; retrieval score: 5.062880895565758.

Word count: 150.

```text
or re-tweets: Some approaches in rumors detection use the number of replies, likes, and re-tweets to detect rumors BIBREF21. Thus, we extract top $k$ replied, liked or re-tweeted tweets from each account to assess the accounts factuality. We tested different $k$ values between 10 tweets to the max number of tweets from each account. Figure FIGREF24 shows the macro-F1 values for different $k$ values. It seems that $k=500$ for the top replied tweets achieves the highest result. Therefore, we consider this as a baseline.

Experimental Setup. We apply a 5 cross-validation on the account's level. For the FacTweet model, we experiment with 25% of the accounts for validation and parameters selection. We use hyperopt library to select the hyper-parameters on the following values: LSTM layer size (16, 32, 64), dropout ($0.0-0.9$), activation function ($relu$, $selu$, $tanh$), optimizer ($sgd$, $adam$, $rmsprop$) with varying the value of the learning rate (1e-1,..,-5), and
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1910.06592:2:11` | partial | 0:453 |

#### Rank 2: qasper-passage-v1-7524c9251ee1d921eba26222e5b1f6fd1fa005e231a32b7ffa2baca7d6c77723

Passage ID: `qasper-passage-v1-7524c9251ee1d921eba26222e5b1f6fd1fa005e231a32b7ffa2baca7d6c77723`; retrieval score: 4.643426793699488.

Word count: 150.

```text
selection. We use hyperopt library to select the hyper-parameters on the following values: LSTM layer size (16, 32, 64), dropout ($0.0-0.9$), activation function ($relu$, $selu$, $tanh$), optimizer ($sgd$, $adam$, $rmsprop$) with varying the value of the learning rate (1e-1,..,-5), and batch size (4, 8, 16). The validation split is extracted on the class level using stratified sampling: we took a random 25% of the accounts from each class since the dataset is unbalanced. Discarding the classes' size in the splitting process may affect the minority classes (e.g. hoax). For the baselines' classifier, we tested many classifiers and the LR showed the best overall performance.

Results. Table TABREF25 presents the results. We present the results using a chunk size of 20, which was found to be the best size on the held-out data. Figure FIGREF24 shows the results of different chunks sizes. FacTweet performs better than the proposed baselines and obtains
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1910.06592:2:11` | partial | 167:847 |

#### Rank 3: qasper-passage-v1-277c9acce23c09d22403dd387a28f0ed41ddf4f27bd324a295ea3cbf41f3f250

Passage ID: `qasper-passage-v1-277c9acce23c09d22403dd387a28f0ed41ddf4f27bd324a295ea3cbf41f3f250`; retrieval score: 3.621566341926732.

Word count: 150.

```text
We present the results using a chunk size of 20, which was found to be the best size on the held-out data. Figure FIGREF24 shows the results of different chunks sizes. FacTweet performs better than the proposed baselines and obtains the highest macro-F1 value of $0.565$. Our results indicate the importance of taking into account the sequence of the tweets in the accounts' timelines. The sequence of these tweets is better captured by our proposed model sequence-agnostic or non-neural classifiers. Moreover, the results demonstrate that the features at tweet-level do not perform well to detect the Twitter accounts factuality, since they obtain a result near to the majority class ($0.18$). Another finding from our experiments shows that the performance of the Tweet2vec is weak. This demonstrates that tweets' hashtags are not informative to detect non-factual accounts. In Table TABREF25, we present ablation tests so as to quantify the contribution of
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-02ff9b0e2712b4037f5ccd4095fcc47214d79849c00cc20daa6c91689e3cee6e

Passage ID: `qasper-passage-v1-02ff9b0e2712b4037f5ccd4095fcc47214d79849c00cc20daa6c91689e3cee6e`; retrieval score: 3.039844941702779.

Word count: 150.

```text
accounts by considering their tweets in groups (chunks). Our hypothesis is that suspicious accounts have a unique pattern in posting tweet sequences. Since their intention is to mislead, the way they transition from one set of tweets to the next has a hidden signature, biased by their intentions. Therefore, reading these tweets in chunks has the potential to improve the detection of the fake news accounts.

In this work, we investigate the problem of discriminating between factual and non-factual accounts in Twitter. To this end, we collect a large dataset of tweets using a list of propaganda, hoax and clickbait accounts and compare different versions of sequential chunk-based approaches using a variety of feature sets against several baselines. Several approaches have been proposed for news verification, whether in social media (rumors detection) BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, or in news claims BIBREF5, BIBREF6, BIBREF7, BIBREF8. The main orientation in the
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-d02285a65f39996d621ded010c727cdf7bfc72ed93a0234c80879a1c7e38a9d2

Passage ID: `qasper-passage-v1-d02285a65f39996d621ded010c727cdf7bfc72ed93a0234c80879a1c7e38a9d2`; retrieval score: 2.9523757700866096.

Word count: 150.

```text
emotional lexicons. We use the NRC lexicon BIBREF10, which contains $\sim $14K words labeled using the eight Plutchik's emotions BIBREF11. The other lexicon is SentiSense BIBREF12 which is a concept-based affective lexicon that attaches emotional meanings to concepts from the WordNet lexical database. It has $\sim $5.5 words labeled with emotions from a set of 14 emotional categories We use the categories that do not exist in the NRC lexicon.

Sentiment: We extract the sentiment of the tweets by employing EffectWordNet BIBREF13, SenticNet BIBREF14, NRC BIBREF10, and subj_lexicon BIBREF15, where each has the two sentiment classes, positive and negative.

Morality: Features based on morality foundation theory BIBREF16 where words are labeled in one of the following 10 categories (care, harm, fairness, cheating, loyalty, betrayal, authority, subversion, sanctity, and degradation).

Style: We use canonical stylistic features, such as the count of question marks, exclamation marks, consecutive characters and letters, links, hashtags,
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 750.

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

#### Rank 1: qasper-passage-v1-a942076ab8b3d69a1ef83dd597599b2b8b178f961156b960574ad6fcd4981707

Passage ID: `qasper-passage-v1-a942076ab8b3d69a1ef83dd597599b2b8b178f961156b960574ad6fcd4981707`; retrieval score: 5.646420309735023.

Word count: 150.

```text
$\textsc {Zero-stc}$ was first explored by the paradigm “Dataless Classification” BIBREF0. Dataless classification first maps the text and labels into a common space by Explicit Semantic Analysis (ESA) BIBREF4, then picks the label with the highest matching score. Dataless classification emphasizes that the representation of labels takes the equally crucial role as the representation learning of text. Then this idea was further developed in BIBREF5, BIBREF6, BIBREF7, BIBREF8, BIBREF9.

With the prevalence of word embeddings, more and more work adopts pretrained word embeddings to represent the meaning of words, so as to provide the models with the knowledge of labels BIBREF10, BIBREF2, BIBREF11, BIBREF12. DBLPYogatamaDLB17 build generative LSTM to generate text given the embedded labels. DBLPRiosK18 use label embedding to attend the text representation in the developing of a multi-label classifier. But they report R@K, so it is unclear whether the system can really predict unseen labels. DBLPXiaZYCY18 study the
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-09c4a58fe6da8f50d18f543759b0298dd9cc8ae1ed1cf5e40bbeb947c91f79e7

Passage ID: `qasper-passage-v1-09c4a58fe6da8f50d18f543759b0298dd9cc8ae1ed1cf5e40bbeb947c91f79e7`; retrieval score: 5.423378827904504.

Word count: 150.

```text
training pairs for the binary classifier.

We notice “Wikipedia-based” training indeed contributes a lot for the topic detection task; however, its performances on emotion and situation detection problems are far from satisfactory. We believe this is mainly because the Yahoo-based topic categorization task is much closer to the Wikipedia-based topic categorization task; emotion and situation categorizations, however, are relatively further.

Our entailment models, pretrained on MNLI/FEVER/RTE respectively, perform more robust on the three $\textsc {0shot-tc}$ aspects (except for the RTE on emotion). Recall that they are not trained on any text classification data, and never know the domain and the aspects in the test. This clearly shows the great promise of developing textual entailment models for $\textsc {0shot-tc}$. Our ensemble approach further boosts the performances on all three tasks.

An interesting phenomenon, comparing the label-partially-unseen results in Table TABREF30 and the label-fully-unseen results in Table TABREF32, is that the pretrained
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-93373184a00e181ea685bb5c858d3be713533a8fe5673793498b2be496336f96

Passage ID: `qasper-passage-v1-93373184a00e181ea685bb5c858d3be713533a8fe5673793498b2be496336f96`; retrieval score: 5.312465858020972.

Word count: 150.

```text
text given the embedded labels. DBLPRiosK18 use label embedding to attend the text representation in the developing of a multi-label classifier. But they report R@K, so it is unclear whether the system can really predict unseen labels. DBLPXiaZYCY18 study the zero-shot intent detection problem. The learned representations of intents are still the sum of word embeddings. But during testing, the intent space includes only new intents; seen intents are not covered. All of these studies can only meet the definition in Definition-Restrictive, so they do not really generalize to open aspects of $\textsc {0shot-tc}$.

JiangqngGuo enrich the embedding representations by incorporating class descriptions, class hierarchy, and the word-to-label paths in ConceptNet. DBLPMitchellSL18 assume that some natural language explanations about new labels are available. Then those explanations are parsed into formal constraints which are further combined with unlabeled data to yield new label oriented classifiers through posterior regularization. However, those explanatory
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-2a2a714ddcb7a8bb300c71d62756f297b0c7742a2d116d564703577b36f156e3

Passage ID: `qasper-passage-v1-2a2a714ddcb7a8bb300c71d62756f297b0c7742a2d116d564703577b36f156e3`; retrieval score: 4.983267576817442.

Word count: 150.

```text
In Table TABREF24, we listed examples for converting class names into hypotheses. In this work, we only tried to make use of the class names and their definitions in WordNet. Table TABREF33 lists the fine-grained performance of three ways of generating hypotheses: “word”, “definition”, and “combination” (i.e., word&definition).

This table indicates that: i) Definition alone usually does not work well in any of the three tasks, no matter which pretrained entailment model is used; ii) Whether “word” alone or “word&definition” works better depends on the specific task and the pretrained entailment model. For example, the pretrained MNLI model prefers “word&definition” in both “emotion” and “situation” detection tasks. However, the other two entailment models (RTE and FEVER) mostly prefer “word”. iii) Since it is unrealistic to adopt only one entailment model, such as from {RTE, FEVER, MNLI}, for any open $\textsc {0shot-tc}$ problem, an ensemble system should be preferred. However, the
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-153795eb1551cc8087ad626afba8128b6c6276e0295f5e7e2d8c33c778fe2838

Passage ID: `qasper-passage-v1-153795eb1551cc8087ad626afba8128b6c6276e0295f5e7e2d8c33c778fe2838`; retrieval score: 4.151605306713844.

Word count: 120.

```text
detection requires more entailment capability. For example, the text snippet “when my brother was very late in arriving home from work”, its gold emotion “fear” requires some common-knowledge inference, rather than just word semantic matching through Word2Vec and ESA.

The supervised method “Binary-BERT” is indeed strong in learning the seen-label-specific models – this is why it predicts very well for seen classes while performing much worse for unseen classes.

Our entailment models, especially the one pretrained on MNLI, generally get competitive performance with the “Binary-BERT” for seen (slightly worse on “topic” and “emotion” while clearly better on “situation”) and improve the performance regarding unseen by large margins. At this stage, fine-tuning on an MNLI-based pretrained entailment model seems more powerful.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 720.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "29c88f6014c4d1a5f3c403d81164492759efd792": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1909.00161:19:0": [
        [
          0,
          396
        ]
      ],
      "1909.00161:19:1": [
        [
          0,
          313
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-297160b5b81f4559ef77518dfb49fe0cac0aef35bdf73e24b0b6b022c0ce299f

Passage ID: `qasper-passage-v1-297160b5b81f4559ef77518dfb49fe0cac0aef35bdf73e24b0b6b022c0ce299f`; retrieval score: 12.533133761580544.

Word count: 104.

```text
We also run additional CTC experiments with 36 layers Transformer (total parameters $\pm $120 millions). The baseline with 36 layers has the same performance with 24 layers, but by adding the proposed methods, the 36 layer performance improved to give the best results. This shows that our proposed methods can improve even very deep models.

As shown in Table TABREF21, the proposed methods also provide large performance improvements on the curated video set, up to 13% with CTC, and up to 9% with the hybrid model. We also observe moderate gains of between 3.2 and 8% relative on the clean and noisy video sets.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-ed16bb10fd60d746197f07fd4706c45cec772513ab1747ea08c129e033bec762

Passage ID: `qasper-passage-v1-ed16bb10fd60d746197f07fd4706c45cec772513ab1747ea08c129e033bec762`; retrieval score: 9.335232423069161.

Word count: 107.

```text
In this section, we present our proposal for allowing the network to (re)-consider the input features in the light of intermediate processing. We do this by again deploying a self-attention mechanism to combine the information present in the original features with the information available in the activations of an intermediate layer. As described earlier, we calculate the output posteriors and auxiliary loss at the intermediate layer as well. The overall architecture is illustrated in Figure FIGREF6. Here, we have used a 24 layer network, with feature re-presentation after the 12th layer.

In the following subsections, we provide detail on the feature re-presentation mechanism, and iterated loss calculation.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-67ef34efb3ebcc993eb195d36fb655ec59e2525a34f3fa2f3ed6de6efb452db4

Passage ID: `qasper-passage-v1-67ef34efb3ebcc993eb195d36fb655ec59e2525a34f3fa2f3ed6de6efb452db4`; retrieval score: 8.032136684272327.

Word count: 150.

```text
In recent years, Transformer models have become an active research topic in speech processing. The key features of Transformer networks is self-attention, which produces comparable or better performance to LSTMs when used for encoder-decoder based ASR BIBREF23, as well as when trained with CTC BIBREF9. Speech-Transformers BIBREF24 also produce comparable performance to the LSTM-based attention model, but with higher training speed in a single GPU. Abdelrahman et al.BIBREF8 integrates a convolution layer to capture audio context and reduces WER in Librispeech.

The use of an objective function in intermediate layers has been found useful in several previous works such as image classification BIBREF25 and language modeling BIBREF26. In BIBREF27, the authors did pre-training with an RNN-T based model by using a hierarchical CTC criterion with different target units. In this paper, we don't need additional types of target unit, instead we just use same tokenization and targets for both intermediate
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-3c4de299c53ac2128f96fd0717db76b2adc929d68ed9af4de50dc19c3495e1b0

Passage ID: `qasper-passage-v1-3c4de299c53ac2128f96fd0717db76b2adc929d68ed9af4de50dc19c3495e1b0`; retrieval score: 7.42734994790452.

Word count: 97.

```text
In this paper, we have proposed a method for re-processing the input features in light of the information available at an intermediate network layer. We do this in the context of deep transformer networks, via a self-attention mechanism on both features and hidden states representation. To encourage meaningful partial results, we calculate the objective function at intermediate layers of the network as well as the output layer. This improves performance in and of itself, and when combined with feature re-presentation we observe consistent relative improvements of 10 - 20% for Librispeech and 3.2 - 13% for videos.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-9a4439644ef3d134f93f343a564ffffa5d48d1f1fd180774bef914969912ce03

Passage ID: `qasper-passage-v1-9a4439644ef3d134f93f343a564ffffa5d48d1f1fd180774bef914969912ce03`; retrieval score: 6.303152319401476.

Word count: 112.

```text
authors did pre-training with an RNN-T based model by using a hierarchical CTC criterion with different target units. In this paper, we don't need additional types of target unit, instead we just use same tokenization and targets for both intermediate and final losses.

The application of the objective function to intermediate layers is also similar in spirit to the use of KL-divergence in BIBREF28, which estimates output posteriors at an intermediate layer and regularizes them towards the distributions at the final layer. In contrast to this approach, the direct application of the objective function does not require the network to have a good output distribution before the new gradient contribution is meaningful.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 570.

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

#### Rank 1: qasper-passage-v1-c33be72058228d13234d0ffa4c3f2740c8929f092915d14944781f0d72408c4f

Passage ID: `qasper-passage-v1-c33be72058228d13234d0ffa4c3f2740c8929f092915d14944781f0d72408c4f`; retrieval score: 13.046439601624199.

Word count: 150.

```text
data is limited; the size of the recorded corpus usually falls short of the requirements for training a statistical DM. However, even if the size of the corpus is large enough the optimal dialogue strategy is likely not to be contained within it.

A solution is to transform the static corpus into a dynamic tool: a user simulator. The user simulator (US) is trained on a dialogue corpus to learn what responses a real user would provide in a given dialogue context. The US is trained using supervised learning since the aim is for it to learn typical user behaviour. For the DM, however, we want optimal behaviour which is why supervised learning cannot be used. By interacting with the SDS, the trained US can be used to train the DM's policy. The DM's policy is optimised using the feedback given by either the user simulator or a separate evaluator.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-a70fe273dcb3525c33b5ddda17f93f87c0d26034bc3ae4fbfb8cc6680f089ca3

Passage ID: `qasper-passage-v1-a70fe273dcb3525c33b5ddda17f93f87c0d26034bc3ae4fbfb8cc6680f089ca3`; retrieval score: 8.162342283698166.

Word count: 150.

```text
Ideally the DM's policy would be trained by interacting with real users. Although there are models that support on-line learning BIBREF15 , for the majority of RL algorithms, which require a lot of interactions, this is impractical. Furthermore, a set of users needs to be recruited every time a policy is trained. This makes common practices such as hyper-parameter optimization prohibitively expensive. Thus, it is natural to try to learn from a dataset which needs to be recorded only once, but can be used over and over again.

A problem with learning directly from recorded dialogue corpora is that the state space that was visited during the collection of the data is limited; the size of the recorded corpus usually falls short of the requirements for training a statistical DM. However, even if the size of the corpus is large enough the optimal dialogue strategy is likely not to be
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-823ee5335252218a51e2978d0ea7b90c84140aa5e47d2bd11fa21fc6a91ed810

Passage ID: `qasper-passage-v1-823ee5335252218a51e2978d0ea7b90c84140aa5e47d2bd11fa21fc6a91ed810`; retrieval score: 5.367676831138027.

Word count: 150.

```text
A Task-Oriented SDS is typically designed according to a structured ontology, which defines what the system can talk about. In a system recommending restaurants the ontology defines those attributes of a restaurant that the user can choose, called informable slots (e.g. different food types, areas and price ranges), the attributes that the user can request, called requestable slots (e.g. phone number or address) and the restaurants that it has data about. An attribute is referred to as a slot and has a corresponding value. Together these are referred to as a slot-value pair (e.g. area=north).

Using RL the DM is trained to act such that is maximises the cumulative future reward. The process by which the DM chooses its next action is called its policy. A typical approach to defining the reward function for a task-oriented SDS is to apply a small per-turn penalty to encourage short dialogues and to
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-8120de2382f11962f46273bf384d7fb22eac45932325d8a7d736eb39cd375b64

Passage ID: `qasper-passage-v1-8120de2382f11962f46273bf384d7fb22eac45932325d8a7d736eb39cd375b64`; retrieval score: 4.817362289432283.

Word count: 150.

```text
dialogues to be created with each dialogue being faster than a dialogue with a human.

In this paper the Neural User Simulator (NUS) is introduced which outputs natural language and whose behaviour is learned from a corpus. The main component, inspired by BIBREF4 , consists of a feature extractor and a neural network based sequence-to-sequence model BIBREF5 . The sequence-to-sequence model consists of a recurrent neural network (RNN) encoder that encodes the dialogue history and a decoder RNN which outputs natural language. Furthermore, the NUS generates its own goal and possibly changes it during a dialogue. This allows the model to be deployed for training more sophisticated DM policies. To achieve this, a method is proposed that transforms the goal-labels of the used dataset (DSTC2) into labels whose behaviour can be replicated during deployment.

The NUS is trained on dialogues between real users and an SDS in a restaurant recommendation
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1805.06966:0:2` | full | 0:774 |

#### Rank 5: qasper-passage-v1-c9afb7a2c6b6896d8d5dc34c2e8a810227cb282315e197e67dfeb4e102aa657e

Passage ID: `qasper-passage-v1-c9afb7a2c6b6896d8d5dc34c2e8a810227cb282315e197e67dfeb4e102aa657e`; retrieval score: 4.78140598773547.

Word count: 150.

```text
why supervised learning cannot be used. By interacting with the SDS, the trained US can be used to train the DM's policy. The DM's policy is optimised using the feedback given by either the user simulator or a separate evaluator. Any number of dialogues can be generated using the US and dialogue strategies that are not in the recorded corpus can be explored.

Most user-simulators work on the level of user semantics. These usually consist of a user dialogue act (e.g. inform, or request) and a corresponding slot-value pair. The first statistical user simulator BIBREF16 used a simple bi-gram model INLINEFORM0 to predict the next user act INLINEFORM1 given the last system act INLINEFORM2 . It has the advantage of being purely probabilistic and domain-independent. However, it does not take the full dialogue history into account and is not conditioned on a goal, leading to incoherent user behaviour throughout a
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 750.

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

#### Rank 1: qasper-passage-v1-cd5bbdb94cd65b5025d0c2f846b88a3cbcf30d10df4591bcb56b36da3ccdbc81

Passage ID: `qasper-passage-v1-cd5bbdb94cd65b5025d0c2f846b88a3cbcf30d10df4591bcb56b36da3ccdbc81`; retrieval score: 8.004741070857778.

Word count: 119.

```text
The fixed training condition is used to build our speaker recognition system. Only conversational telephone speech data from datasets released through the linguistic data consortium (LDC) have been used, including NIST SRE 2004-2010 and the Switchboard corpora (Switchboard Cellular Parts I and II, Switchboard2 Phase I,II and III) for different steps of system training. A more detailed description of the data used in the system training is presented in Table TABREF1 . We have also included the unlabelled set of 2472 telephone calls from both minor (Cebuano and Mandarin) and major (Tagalog and Cantonese) languages provided by NIST in the system training. We will indicate when and how we used this set in the training in the following sections.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-888556134188fb0479485402a67479ed1a47e1f819e405ed8c7f162111f54303

Passage ID: `qasper-passage-v1-888556134188fb0479485402a67479ed1a47e1f819e405ed8c7f162111f54303`; retrieval score: 5.94036933220002.

Word count: 150.

```text
This section reports on the CPU execution time (single threaded), and the amount of memory used to process a single trial, which includes the time for creating models from the enrolment data and the time needed for processing the test segments. The analysis was performed on an Intel(R) Xeon(R) CPU E5-2670 2.60GHz. The results are shown in Table TABREF27 . We used the time command in Unix to report these results. The user time is the actual CPU time used in executing the process (single thread). The real time is the wall clock time (the elapsed time including time slices used by other processes and the time the process spends blocked). The system time is also the amount of CPU time spent in the kernel within the process. We have also reported the memory allocated for each stage of execution. The most computationally intensive stage is the extraction of i-vectors
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-ef05a0dbf2f8e4d4969c28e6ec5d985839ac1729ce0d6c391de85984cb96e58c

Passage ID: `qasper-passage-v1-ef05a0dbf2f8e4d4969c28e6ec5d985839ac1729ce0d6c391de85984cb96e58c`; retrieval score: 5.515978466271624.

Word count: 120.

```text
blocked). The system time is also the amount of CPU time spent in the kernel within the process. We have also reported the memory allocated for each stage of execution. The most computationally intensive stage is the extraction of i-vectors (both MFCC- and PLP-based i-vectors), which also depends on the duration of the segments. For enrolment, we have reported the time required to extract a model from a segment with a duration of 140 seconds and speech duration of 60 seconds. The time and memory required for front-end processing are negligible compared to the i-vector extraction stage, since they only include matrix operations. The time required for our SAD is also reported which increases linearly with the duration of segment.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-9223adb2b927174dfadff5d05c5c2d6b7e2cc8f663ed1445ea978b3fcbede9ad

Passage ID: `qasper-passage-v1-9223adb2b927174dfadff5d05c5c2d6b7e2cc8f663ed1445ea978b3fcbede9ad`; retrieval score: 5.127258476108774.

Word count: 109.

```text
BIBREF7 , failed to provide even comparable recognition performance to the traditional GMM. Therefore, we concentrated on the cepstral based GMM/i-vector system.

We outline in this paper the Intelligent Voice system, techniques and results obtained on the SRE 2016 development set that will mirror the evaluation condition as well as the timing report. Section SECREF2 describes the data used for the system training. The front-end and back-end processing of the system are presented in Sections SECREF3 and SECREF4 respectively. In Section SECREF5 , we describe experimental evaluation of the system on the SRE 2016 development set. Finally, we present a timing analysis of the system in Section SECREF6 .
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-607cce00d72bc69af92d373bdef50487e6f216c7594168d291d3f74c6253846f

Passage ID: `qasper-passage-v1-607cce00d72bc69af92d373bdef50487e6f216c7594168d291d3f74c6253846f`; retrieval score: 5.086674443964539.

Word count: 126.

```text
effect of using QMF is also investigated in scenario D. Finally in scenario E, we can see the major improvement obtained through the use of the domain adaptation technique explained in Section SECREF16 . For our secondary submission, we incorporated a disjoint portion of the labelled development set (10 out of 20 speakers) in either LN-LDA and in-domain PLDA training. We evaluated the system on almost 6k out of 24k trials from the other portion to avoid any over-fitting, particularly important for the domain adaptation technique. This resulted in a relative improvement of 11% compared to the primary system in terms of the primary metric. However, the results can be misleading, since the recording condition may be the same for all speakers in the development set.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 624.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "c098177da67025e6442b6e3416945868669f695d": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1611.00514:5:0": [
        [
          0,
          835
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-f8ffa965c8df695f877b9516038963bd5b808cfa879e72592293a2a537630b28

Passage ID: `qasper-passage-v1-f8ffa965c8df695f877b9516038963bd5b808cfa879e72592293a2a537630b28`; retrieval score: 7.161283034284927.

Word count: 150.

```text
and K be learned from data Each step in the new iHMM-iFHMM generative process is performed in two phases: (i) the latent feature variables from the iFHMM framework are sampled using the mIBP mechanism; and (ii) the features sampled so far, which become observable during this second phase, are used in an adapted version of the beam sampling algorithm BIBREF183 to infer the clustering components (i.e., latent events).

They report results in terms of recall (R), precision (P), and F-score (F) by employing the mention-based B3 metric BIBREF184 , the entity-based CEAF metric BIBREF185 , and the pairwise F1 (PW) metric. Their experiments for show that both of these models work well when the feature and cluster numbers are treated as free parameters, and the selection of feature values is performed automatically.

BIBREF167 argue that events represent complex phenomena and can therefore co-refer fully, being identical, like other researchers have
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-42ae4d625e5ac69bf01fe748d368eb4f461a99051c668c42e4c316b1f5741407

Passage ID: `qasper-passage-v1-42ae4d625e5ac69bf01fe748d368eb4f461a99051c668c42e4c316b1f5741407`; retrieval score: 7.057040863137848.

Word count: 150.

```text
Many authors in linguistics have delved deeper into the nature of event classes and have tried to come up with features or characteristics that can be used to identify whether something (verb or a clause) belongs to a particular event class or not. These features or characteristics are necessary to describe the structure of events in a theoretical sense. Description of event structure usually refers to the actual words used (lexical features or characteristics) and also the structure of clause or sentence (syntactic features or characteristics). Identification of such features may be described as finding parameters of event types or parameterization of event types.

A lot of the work on parameterization of event types/classes use the classes espoused by Vendler. These include BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 , BIBREF13 , BIBREF14 , BIBREF15 and others. We will only briefly touch upon such work in this paper. Our objective
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-d83b100944336c2c614d0de2e8c9660f8d8c4e090a3e1a45abb3f4e227f5289a

Passage ID: `qasper-passage-v1-d83b100944336c2c614d0de2e8c9660f8d8c4e090a3e1a45abb3f4e227f5289a`; retrieval score: 6.6773671926918015.

Word count: 150.

```text
Mathematical logic is used to represent the semantics of language. In particular, we use logic to represent the meaning of single sentences. Early work on events, e.g., Panini (as discussed by BIBREF21 and BIBREF22 ) stated that language encodes two kinds of information–actions and non-actions. Verbs represent actions and nouns represent non-actions or things.

BIBREF23 proposes that one needs an event variable $e$ to represent events in mathematical logic. This variable $e$ is used to represent relations represented by the event denoted by the verb and other constituents in the sentence, such as modifiers. Davidson claims that logically speaking, events are like things in that they can be represented by a variable and this variable can be modified and quantified. A question that arises is: how many arguments should an event predicate (in logic) take BIBREF2 ? Just like nominal modifiers modify nouns, event modifiers can modify event predicates. An
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-34bfbee0e6417ff33b8d8d4f8b267b832ebf6764d6a4b6639ac9645471c4323d

Passage ID: `qasper-passage-v1-34bfbee0e6417ff33b8d8d4f8b267b832ebf6764d6a4b6639ac9645471c4323d`; retrieval score: 6.395537784511968.

Word count: 150.

```text
time, but lack continuous tenses. Examples: Jon knows the answer and Jon likes Mary.

BIBREF5 adopts the same classification as Vendler and Dowty, but divides achievements into two classes. The first one is still called achievements, but the second one is called semelfactives. In this new scheme, achievements are instantaneous (that is, the beginning of the event is the same as its end) culminating events, but semelfactives are events with no duration that result in no change of state. An example of a semelfactive is: Jon knocked on the door.

Table 1 presents the nomenclatures introduced by various linguists in one place. There are many variations of the schemes given here, although we do not discuss them in this paper.

In the early work on event classification, Aristotle, Vendler and others assume that what needs to be classified is the verb. However, many have concluded that it is impossible to
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-d71cae9fdf2a2e901556b1a80e5f59c5d1911db2826c5a86d8520d41502ad0c1

Passage ID: `qasper-passage-v1-d71cae9fdf2a2e901556b1a80e5f59c5d1911db2826c5a86d8520d41502ad0c1`; retrieval score: 6.264987471758516.

Word count: 150.

```text
event participants, but can work with named entity taggers to link arguments to events.

Evita breaks down the event recognition problem to a number of sub-tasks. Evita preprocesses the input text using the Alembic Workbench POS tagger, lemmatizer to find lexical stems, and chunkier to obtain phrase chunks, verbal, nominal and adjectival, the three that are commonly used as event referring expressions BIBREF142 . For each subtask after pre-processing, it combines linguistic- and statistically-based knowledge. Linguistic knowledge is used in local and limited contexts such as verb phrases and to extract morphological information. Statistical knowledge is used to disambiguate nominal events. The sub-tasks in event recognition in Evita are: determination of event candidates and then the events, identification of grammatical features of events, additional clustering of event chunks for event detection and grammatical feature identification in some situations.

For event identification, Evita looks at the lexical items tagged by the
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 750.

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

#### Rank 1: qasper-passage-v1-7d9f14e5f0557b0bcf731072b5109f103f32ab0c89604b7fb2a9958851a4083b

Passage ID: `qasper-passage-v1-7d9f14e5f0557b0bcf731072b5109f103f32ab0c89604b7fb2a9958851a4083b`; retrieval score: 6.616966212012774.

Word count: 84.

```text
Chatino is a group of languages spoken in Oaxaca, Mexico. Together with the Zapotec language group, the Chatino languages form the Zapotecan branch of the Otomanguean language family. There are three main Chatino languages: Zenzontepec Chatino (ZEN, ISO 639-2 code czn), Tataltepec Chatino (TAT, cta), and Eastern Chatino (ISO 639-2 ctp, cya, ctz, and cly) (E.Cruz 2011 and Campbell 2011). San Juan Quiahije Chatino (SJQ), the language of the focus of this study, belongs to Eastern Chatino, and is used by about 3000 speakers.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-f0feaf328cadb19787ffa62c6fd5d3ae3ebe0fb62ca477801dd35c4753afa53d

Passage ID: `qasper-passage-v1-f0feaf328cadb19787ffa62c6fd5d3ae3ebe0fb62ca477801dd35c4753afa53d`; retrieval score: 5.930114932847964.

Word count: 150.

```text
mixture thereof. As Natural Language Processing (NLP) keeps expanding its frontiers to encompass more and more languages, modeling of the grammatical functions that guide language generation is of utmost importance. It follows, then, that the next crucial step for expanding NLP research on endangered languages is creating benchmarks for standard NLP tasks in such languages.

With this work we take a small first step towards this direction. We present a resource that allows for benchmarking two NLP tasks in San Juan Quiahije Chatino, an endangered language spoken in southern Mexico: morphological analysis and morphological inflection, with a focus on the verb morphology of the language.

We first briefly discuss the Chatino language and the intricacies of its verb morphology (§SECREF2), then describe the resource (§SECREF3), and finally present baseline results on both the morphological analysis and the inflection tasks using state-of-the-art neural models (§SECREF4). We make our resource publicly available
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-13705f5d498968f0abd075ed46bd62c10528a5afa1a790ae09335ac4a9d09445

Passage ID: `qasper-passage-v1-13705f5d498968f0abd075ed46bd62c10528a5afa1a790ae09335ac4a9d09445`; retrieval score: 5.277826780108555.

Word count: 99.

```text
Eastern Chatino languages , including SJQ Chatino, are intensively tonal BIBREF2, BIBREF3. Tones mark both lexical and grammatical distinctions in Eastern Chatino languages.

In SJQ Chatino, there are eleven tones. Three different systems for representing tone distinctions are employed in the literature: the S-H-M-L system of BIBREF2; the numeral system of BIBREF4; and the alphabetic system of BIBREF3. The correspondences among these three systems are given in Table . For present purposes, we will use numeral representations of the second sort. The number 1 represents a high pitch, 4 represents a low pitch, and double digits represent contour tones.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-da9b6e1b0933dead4c7955cba2c604e496ac64a033ebc21af73fd9a81e053dff

Passage ID: `qasper-passage-v1-da9b6e1b0933dead4c7955cba2c604e496ac64a033ebc21af73fd9a81e053dff`; retrieval score: 4.885368387406671.

Word count: 41.

```text
Chatino language and the intricacies of its verb morphology (§SECREF2), then describe the resource (§SECREF3), and finally present baseline results on both the morphological analysis and the inflection tasks using state-of-the-art neural models (§SECREF4). We make our resource publicly available online.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-7c5a0842665fb57b96ce8efc55b1be74028fc55a0c413746d74fd9452de81a05

Passage ID: `qasper-passage-v1-7c5a0842665fb57b96ce8efc55b1be74028fc55a0c413746d74fd9452de81a05`; retrieval score: 4.690361544931845.

Word count: 150.

```text
We provide a hand-curated collection of complete inflection tables for 198 lemmata. The morphological tags follow the guidelines of the UniMorph schema BIBREF6, BIBREF7, in order to allow for the potential of cross-lingual transfer learning, and they are tagged with respect to:

Person: first (1), second (2), and third (3)

Number: singular (SG) ad plural (PL)

Inclusivity (only applicable to first person plural verbs: inclusive (INCL) and exclusive (EXCL)

Aspect/mood: completive (CPL), progressive (PROG), potential (POT), and habitual (HAB).

Two examples of complete inflection tables for the verbs ndyu2 `fell from above' and lyu1 `fall' are shown in Table . Note how the first verb has the same PN triplet for all four aspect/mood categories, while the second paradigm is more representative in that it involves three different triplets (one for the completive, another for the progressive, and another for the habitual/potential). This variety is at the core of why
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 524.

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
      "2004.02083:6:0": [
        [
          0,
          746
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
