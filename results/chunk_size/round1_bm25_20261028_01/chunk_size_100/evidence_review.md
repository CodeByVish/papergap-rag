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

#### Rank 1: qasper-passage-v1-cd71bf9363ba5866957761212ba3107c3e32e19e6153bd5a547c599fad67ec1d

Passage ID: `qasper-passage-v1-cd71bf9363ba5866957761212ba3107c3e32e19e6153bd5a547c599fad67ec1d`; retrieval score: 7.049766114748859.

Word count: 100.

```text
Methods for machine translations have been studied for years, and at the same time algorithms to generate word embeddings are becoming more and more accurate. Still, there is a lot of research aiming at unifying word embeddings across multiple languages. In this experience we try a technique for machine translation that relates word embeddings between two different languages. Based on the literature we found that it is possible to infer missing dictionary entries using distributed representations of words and phrases. One way of doing it is to create a linear mapping between the two vector spaces of two different languages.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-790648a0390f223b6ab5b1e6be860763958a10dc53648b19e95802c077fc8b78

Passage ID: `qasper-passage-v1-790648a0390f223b6ab5b1e6be860763958a10dc53648b19e95802c077fc8b78`; retrieval score: 6.522251820183467.

Word count: 71.

```text
(Mikolov et al., 2013a). The objective function that skip gram tries to minimize is the following:

Where N represents the total number of words in a sentence, P the probability of a word at the position i+j to belong to the sentence, with respect to the word i. Ideally, by using this approach we will be able to provide non-trivial translations that will be related to the context of a word.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-2046a116b1778264a3bdd65d5359bd8d743106d3f14d2acc2c6a6ce678899fbd

Passage ID: `qasper-passage-v1-2046a116b1778264a3bdd65d5359bd8d743106d3f14d2acc2c6a6ce678899fbd`; retrieval score: 6.202831637348374.

Word count: 100.

```text
In recent years, various models for learning cross-lingual representations have been proposed. Two main broad categories with some related papers are identified here:

Monolingual mapping: In this approach, models are trained using word embeddings from a monolingual corpora. Then, an objective function is used to minimize a linear mapping that enable them to map unknown words from the source language to the target language.

Pseudo-cross-lingual: In this case we create a pseudo-cross-lingual corpus by mixing contexts of different languages. We then train an off-the-shelf word embedding model on the created corpus. Ideally the cross-lingual contexts allow the learned representations to
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-4c0457ea269df606d0964614f92eab289cc6b04ae7f71d2f76f6fadc8eda5b7a

Passage ID: `qasper-passage-v1-4c0457ea269df606d0964614f92eab289cc6b04ae7f71d2f76f6fadc8eda5b7a`; retrieval score: 4.369896301389908.

Word count: 55.

```text
This represents the linear function that maps word embeddings from one language to another. Given a word x in one language, and the respective word in the other language z, the following equation reports the objective function we want to minimize:

Were W represents the final matrix that will contain the values for the mapping.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-9ed95b6d625191eb54bdc4d6e200e563617eba5968f391d3733efab08d81eb53

Passage ID: `qasper-passage-v1-9ed95b6d625191eb54bdc4d6e200e563617eba5968f391d3733efab08d81eb53`; retrieval score: 4.326032653827899.

Word count: 100.

```text
that projects the first vector space to the second one. In this way, we are able to translate every word belonging to the first language into the second one. Once we obtain the translated word embedding, we output the most similar word vector as the translation. The word embeddings were learnt using the Skip Gram method proposed by (Mikolov et al., 2013a). An example of how the method would work is reported in figure 1 and figure 2. After creating the word embeddings from the two dictionaries, we plotted the numbers in the two graphs using PCA. Figure 3 reports
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 426.

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

#### Rank 1: qasper-passage-v1-e611ec0f6f36000250ad808a8e4c986649f52bc83e5bd00ac6551b477e4efd95

Passage ID: `qasper-passage-v1-e611ec0f6f36000250ad808a8e4c986649f52bc83e5bd00ac6551b477e4efd95`; retrieval score: 3.550189458379045.

Word count: 100.

```text
The focus of this section is on recently published datasets and LID research applicable to the South African context. An in depth survey of algorithms, features, datasets, shared tasks and evaluation methods may be found in BIBREF0.

The datasets for the DSL 2015 & DSL 2017 shared tasks BIBREF1 are often used in LID benchmarks and also available on Kaggle . The DSL datasets, like other LID datasets, consists of text sentences labelled by language. The 2017 dataset, for example, contains 14 languages over 6 language groups with 18000 training samples and 1000 testing samples per language.

The recently published
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-2a467dc3cc4b7a18c79e47af727bd73f08c2898dc6061d92c3723a9886fd82f7

Passage ID: `qasper-passage-v1-2a467dc3cc4b7a18c79e47af727bd73f08c2898dc6061d92c3723a9886fd82f7`; retrieval score: 1.152894701385712.

Word count: 100.

```text
for the Nguni and Sotho groups. If the lexicon prediction of the specific language has high confidence then its result is used as the final label else the naive Bayesian classifier's specific language prediction is used as the final result. The lexicon is built over all the data and therefore includes the vocabulary from both the training and testing sets.

The lexicon based classifier is designed to trade higher precision for lower recall. The proposed implementation is considered confident if the number of words from the winning language is at least one more than the number of words considered to
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-1ba1db55ad411ee03499d5ee3ba134e97e782427c8d1aec1dcd6cce011a93685

Passage ID: `qasper-passage-v1-1ba1db55ad411ee03499d5ee3ba134e97e782427c8d1aec1dcd6cce011a93685`; retrieval score: 1.1336756094247633.

Word count: 100.

```text
belonging to either the Nguni family, the Sotho family, English, Afrikaans, Xitsonga or Tshivenda. The scikit-learn multinomial naive Bayes classifier is used for the implementation with an alpha smoothing value of 0.01 and hashed text features.

The lexicon based classifier is then used to predict the specific language within a language group. For the South African languages this is done for the Nguni and Sotho groups. If the lexicon prediction of the specific language has high confidence then its result is used as the final label else the naive Bayesian classifier's specific language prediction is used as the final result.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-40b69473d7057282f0e511cbea051268492ce208980dc436b837e62ae9ad3897

Passage ID: `qasper-passage-v1-40b69473d7057282f0e511cbea051268492ce208980dc436b837e62ae9ad3897`; retrieval score: 1.088558804703261.

Word count: 100.

```text
The lexicon based classifier is designed to trade higher precision for lower recall. The proposed implementation is considered confident if the number of words from the winning language is at least one more than the number of words considered to be from the language scored in second place.

The stacked classifier is tested against three public LID implementations BIBREF17, BIBREF23, BIBREF8. The LID implementation described in BIBREF17 is available on GitHub and is trained and tested according to a post on the fasttext blog. Character (5-6)-gram features with 16 dimensional vectors worked the best. The implementation discussed in BIBREF23 is
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-63636ded134d640d866b99049c05d2f38d0cc8023e62c029d11f07d99a9092fb

Passage ID: `qasper-passage-v1-63636ded134d640d866b99049c05d2f38d0cc8023e62c029d11f07d99a9092fb`; retrieval score: 1.0290667943898375.

Word count: 100.

```text
Accurate language identification (LID) is the first step in many natural language processing and machine comprehension pipelines. If the language of a piece of text is known then the appropriate downstream models like parts of speech taggers and language models can be applied as required.

LID is further also an important step in harvesting scarce language resources. Harvested data can be used to bootstrap more accurate LID models and in doing so continually improve the quality of the harvested data. Availability of data is still one of the big roadblocks for applying data driven approaches like supervised machine learning in
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 500.

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

#### Rank 1: qasper-passage-v1-a63f2bd371c233a20b5ea0de09ce2b92e31bf50f421a8ca52ab9d5071522cb54

Passage ID: `qasper-passage-v1-a63f2bd371c233a20b5ea0de09ce2b92e31bf50f421a8ca52ab9d5071522cb54`; retrieval score: 4.172900625636694.

Word count: 100.

```text
Entity linking (EL) BIBREF24 , also known as named entity disambiguation or normalization, is the task to determine the identity of entities mentioned in a piece of text with reference to a knowledge base. There are a number of knowledge bases that provide a background repository for entity classification of this type. For this study, we use Wikidata, which can be seen diagrammatically in Figure FIGREF12 . Systems such as DeepType BIBREF25 integrate symbolic information into the reasoning process of a neural network with a type system and show state-of-the-art performances for EL. They do not, however, quote results on
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-290c44e6f583e37593fc3c3c43aa6a6f8645340b40fab1600288f68babfdd295

Passage ID: `qasper-passage-v1-290c44e6f583e37593fc3c3c43aa6a6f8645340b40fab1600288f68babfdd295`; retrieval score: 4.097791543920305.

Word count: 100.

```text
be seen diagrammatically in Figure FIGREF12 . Systems such as DeepType BIBREF25 integrate symbolic information into the reasoning process of a neural network with a type system and show state-of-the-art performances for EL. They do not, however, quote results on Wiki(gold) so a direct comparison is difficult.

While these knowledge bases provide semantically rich and fine-granular classes and relationship types, the task of entity classification often requires associating coarse-grained classes with discovered surface forms of entities. Most existing studies consider NER and entity linking as two separate tasks, whereas we try to combine the two. It has been shown that
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-e738f43cb9426b117a1867b8a72dd5980a965751d300a4913605c195eac03fe8

Passage ID: `qasper-passage-v1-e738f43cb9426b117a1867b8a72dd5980a965751d300a4913605c195eac03fe8`; retrieval score: 3.7470793173529158.

Word count: 100.

```text
The results for each class type are shown in Table TABREF19 , with some specific examples shown in Figure FIGREF18 . For the Wiki(gold) we quote the micro-averaged F-1 scores for the entire top level entity category. The total F-1 score on the OntoNotes dataset is 88%, and the total F-1 cross-validation score on the 112 class Wiki(gold) dataset is 53%. It is worth noting that one could improve Wiki(gold) results by training directly using this dataset. However, the aim is not to tune our model specifically on this class hierarchy. We instead aim to present a framework which can
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.10503:6:0` | partial | 0:584 |

#### Rank 4: qasper-passage-v1-5a9e4f13268bc24746057f61c25c8574b68f923089a8bfd156b4effa072b4f58

Passage ID: `qasper-passage-v1-5a9e4f13268bc24746057f61c25c8574b68f923089a8bfd156b4effa072b4f58`; retrieval score: 3.720468192742829.

Word count: 100.

```text
53%. It is worth noting that one could improve Wiki(gold) results by training directly using this dataset. However, the aim is not to tune our model specifically on this class hierarchy. We instead aim to present a framework which can be modified easily to any domain hierarchy and has acceptable out-of-the-box performances to any fine-grained dataset. The results in Table TABREF19 (OntoNotes) only show the main 7 categories in OntoNotes which map to Wiki(gold) for clarity. The other categories (date, time, norp, language, ordinal, cardinal, quantity, percent, money, law) have F-1 scores between 80-90%, with the exception of time (65%)
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.10503:6:0` | partial | 350:992 |

#### Rank 5: qasper-passage-v1-3f72547afd0b1afb37b8b41ef6ae97ec3d3fd237806b914a2fbc488169be8fe2

Passage ID: `qasper-passage-v1-3f72547afd0b1afb37b8b41ef6ae97ec3d3fd237806b914a2fbc488169be8fe2`; retrieval score: 3.1391421145336094.

Word count: 100.

```text
NER involves identifying both entity boundaries and entity types. With “exact-match evaluation”, a named entity is considered correctly recognized only if both the boundaries and type match the ground truth BIBREF8 , BIBREF17 , BIBREF18 . Precision, Recall, and F-1 scores are computed on the number of true positives (TP), false positives (FP), and false negatives (FN). Their formal definitions are as follows:

True Positive (TP): entities that are recognized by NER and match the ground truth.

False Positive (FP): entities that are recognized by NER but do not match the ground truth.

False Negative (FN): entities annotated in the
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 500.

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

#### Rank 1: qasper-passage-v1-d52cbda0078311a775c72b8d98f04548e565103e5574a7bf55ec06da43fd675b

Passage ID: `qasper-passage-v1-d52cbda0078311a775c72b8d98f04548e565103e5574a7bf55ec06da43fd675b`; retrieval score: 8.532480610174629.

Word count: 100.

```text
To the best of our knowledge, there are only two recent works that specifically study how to combine word and subword-level vector representations.

BIBREF11 propose to use a trainable scalar gating mechanism capable of learning a weighting scheme for combining character-level and word-level representations. They compared their proposed method to manually weighting both levels; using characters only; words only; or their concatenation. They found that in some datasets a specific manual weighting scheme performed better, while in others the learned scalar gate did.

BIBREF12 further expand the gating concept by making the mechanism work at a finer-grained level, learning how
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-63efa53216e970e89d27ff9f2bba593177c4ca3820346651209d362512fb3f28

Passage ID: `qasper-passage-v1-63efa53216e970e89d27ff9f2bba593177c4ca3820346651209d362512fb3f28`; retrieval score: 6.167221446045291.

Word count: 100.

```text
To enable sentence-level classification we need to obtain a sentence representation from the word vectors INLINEFORM0 . We achieved this by using a BiLSTM with max pooling, which was shown to be a good universal sentence encoding mechanism BIBREF13 .

Let INLINEFORM0 , be an input sentence and INLINEFORM1 its matrix representation, where each INLINEFORM2 was obtained by one of the methods described in subsec:methods. INLINEFORM3 is the context-enriched matrix representation of INLINEFORM4 obtained by feeding INLINEFORM5 to a BiLSTM of output dimension INLINEFORM6 . Lastly, INLINEFORM11 is the final sentence representation of INLINEFORM12 obtained by max-pooling INLINEFORM13 along the
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.05584:4:0` | full | 0:250 |

#### Rank 3: qasper-passage-v1-8f3e658d3a994861fd37e6a0042a7074cc6352d08e28c66290e6312b248c866c

Passage ID: `qasper-passage-v1-8f3e658d3a994861fd37e6a0042a7074cc6352d08e28c66290e6312b248c866c`; retrieval score: 5.867621866184213.

Word count: 48.

```text
pointers to their original sources in the appendix table:sentence-eval-datasets.

To evaluate these sentence representations SentEval trained a linear model on top of them, and evaluated their performance in the validation sets accompanying each dataset. The only exception was the STS16 task, in which our representations were evaluated directly.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-f050023cd917b5b2281a5bc03f24fb66ff9402cfa82d0e7c7f82188d29b434f1

Passage ID: `qasper-passage-v1-f050023cd917b5b2281a5bc03f24fb66ff9402cfa82d0e7c7f82188d29b434f1`; retrieval score: 5.324301407945567.

Word count: 100.

```text
table:wordlevelresults shows the quality of word representations in terms of the correlation between word similarity scores obtained by the proposed models and word similarity scores defined by humans.

First, we can see that for each task, character only models had significantly worse performance than every other model trained on the same dataset. The most likely explanation for this is that these models are the only ones that need to learn word representations from scratch, since they have no access to the global semantic knowledge encoded by the GloVe embeddings.

Further, bold results show the overall trend that vector gates outperformed
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-9d4e5cde082fc4e7d2f432b0168fc378cc01d72aa356f5ee3d6970b64c4fb60a

Passage ID: `qasper-passage-v1-9d4e5cde082fc4e7d2f432b0168fc378cc01d72aa356f5ee3d6970b64c4fb60a`; retrieval score: 5.200269835170708.

Word count: 100.

```text
that the models they describe first learn how to represent subword information, at character BIBREF1 , morpheme BIBREF4 , or substring BIBREF0 levels, and then combine these learned representations at the word level. The incorporation of information at a finer-grained hierarchy results in higher-quality modeling of rare words, morphological processes, and semantics BIBREF6 .

There is no consensus, however, on which combination method works better in which case, or how the choice of a combination method affects downstream performance, either measured intrinsically at the word level, or extrinsically at the sentence level.

In this paper we aim to provide some
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 448.

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

#### Rank 1: qasper-passage-v1-0ba02c34d201ab3c497476f637ec9b2fc61429b98ea55580942ad42f12928e39

Passage ID: `qasper-passage-v1-0ba02c34d201ab3c497476f637ec9b2fc61429b98ea55580942ad42f12928e39`; retrieval score: 8.429697086910052.

Word count: 60.

```text
all the other segments in the same transcript are used as negative samples. Cross entropy is used as an objective function.

Metrics. We used accuracy and MRR (Mean Reciprocal Ranking) as metrics. The accuracy is

We split the ground-truth dataset to train/dev/test into the ratio of 6/2/2. The resulting size is 3,718 (train), 1,238 (dev) and 1,239 qa pairs (test).
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1912.01046:9:5` | full | 0:87 |

#### Rank 2: qasper-passage-v1-9e4837de42b9973bb5b34b83bc6129adfb4fb8ddc30dbbb7cbbc3d85226457e6

Passage ID: `qasper-passage-v1-9e4837de42b9973bb5b34b83bc6129adfb4fb8ddc30dbbb7cbbc3d85226457e6`; retrieval score: 7.6454146096366955.

Word count: 100.

```text
Model. The two inputs, $s$ and $q$ represent the segment text and a question. The model first encodes the two inputs.

$h^s$ is then re-weighted using attention weights.

where $\odot $ denotes the element-wise multiplication operation. The final score is computed using a one-layer feed-forward network.

During training, the model requires negative samples. For each positive example, (question, ground-truth segment), all the other segments in the same transcript are used as negative samples. Cross entropy is used as an objective function.

Metrics. We used accuracy and MRR (Mean Reciprocal Ranking) as metrics. The accuracy is

We split the ground-truth dataset
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1912.01046:9:5` | full | 0:87 |

#### Rank 3: qasper-passage-v1-63cba9c2d8e43c8a08106d4a6ab0b8e90fe3b617acf4dc874a071793a0949cc0

Passage ID: `qasper-passage-v1-63cba9c2d8e43c8a08106d4a6ab0b8e90fe3b617acf4dc874a071793a0949cc0`; retrieval score: 6.299651332328595.

Word count: 100.

```text
the videos.

Our AMT experiment consisted of two parts. In the first part, we presented the workers with the video content of a segment. For each segment, we asked workers to generate questions that can be answered by the presented segment. We did not limit the number of questions a worker can input to a corresponding segment and encouraged them to input a diverse set of questions which the span can answer. Along with the questions, the workers were also required to provide a justification as to why they made their questions. We manually checked this justification to filter out
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-3e0c2899944fdfd236761e53715772eacfd5c444ecfa628e5db389c61f08e533

Passage ID: `qasper-passage-v1-3e0c2899944fdfd236761e53715772eacfd5c444ecfa628e5db389c61f08e533`; retrieval score: 6.210215479082347.

Word count: 100.

```text
rows display questions which belong to the same segment but correspond to different properties of the same entity, 'crop tool'. Here we observe different types of questions, such as "why", "how", "what", and "where", and can see why the answers may involve multiple steps. Some questions that the worked paraphrased were in the "yes/no" style, however our answer segments then provide an explanation to these questions.

Each answer segment was extracted from an image editing tutorial video that involved multiple steps and procedures to produce a final image, which can partially be seen in FIGREF1. The average number of sentences
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-3eabe0fb3b5959a65510a2877d5721de7a02c57fe49fd2ad5ce5ada2f6ca4510

Passage ID: `qasper-passage-v1-3eabe0fb3b5959a65510a2877d5721de7a02c57fe49fd2ad5ce5ada2f6ca4510`; retrieval score: 5.953754083214869.

Word count: 95.

```text
top 10 video transcripts(out of 76) with the minimum cosine distance, and further compute the TF-IDF vectors for their segments, Stop10n, where n = 10. We repeat the process for the corresponding segments:

selecting the segment with the minimal cosine distance distance to the query.

Metrics. To evaluate our pipeline approach we use overall accuracy after filtering and accuracy given that the segment is in the top 10 videos. While the first metric is similar to SECREF17, the second can indicate if initially searching on the video space can be used to improve our selection:
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1912.01046:10:4` | full | 0:294 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 455.

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

#### Rank 1: qasper-passage-v1-d669ea925c37d9ea4da78122ac0872f1254c246512de7c93a5a61f49017bdce6

Passage ID: `qasper-passage-v1-d669ea925c37d9ea4da78122ac0872f1254c246512de7c93a5a61f49017bdce6`; retrieval score: 7.063612166132197.

Word count: 100.

```text
time.

Document revision detection, plagiarism detection and revision provenance all rely on comparing the content of two documents and assessing a distance/similarity score. The classic document similarity measure, especially for plagiarism detection, is fingerprinting BIBREF7 , BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 . Fixed-length fingerprints are created using hash functions to represent document features and are then used to measure document similarities. However, the main purpose of fingerprinting is to reduce computation instead of improving accuracy, and it cannot capture word semantics. Another widely used approach is computing the sentence-to-sentence Levenshtein distance and assigning an overall score
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-ede020cf47b7b3d4c3ca7a3746314eda622146a5a5ead2c98034607c64be3df1

Passage ID: `qasper-passage-v1-ede020cf47b7b3d4c3ca7a3746314eda622146a5a5ead2c98034607c64be3df1`; retrieval score: 5.076218862757633.

Word count: 100.

```text
that a document can be revised by many users, but that the documents are not merged together. We consider collaborative editing as revising documents one by one.

The two research problems that are most relevant to document revision detection are plagiarism detection and revision provenance. In a plagiarism detection system, every incoming document is compared with all registered non-plagiarized documents BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 . The system returns true if an original copy is found in the database; otherwise, the system returns false and adds the document to the database. Thus, it is a 1-to-n problem. Revision
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-da5c5656d43fe4756a6e73f25760c01d221f383452d2f789cb382aa7900a6d98

Passage ID: `qasper-passage-v1-da5c5656d43fe4756a6e73f25760c01d221f383452d2f789cb382aa7900a6d98`; retrieval score: 4.988274615235826.

Word count: 100.

```text
pairs and eliminate those with scores that are lower than an empirical threshold ( INLINEFORM0 ). This is what we call the weak filter. After that, we apply the strong filter wDTW or wTED on the available pairs and filter out document pairs having distances higher than a threshold INLINEFORM1 . For VSM in Section SECREF32 , we directly filter out document pairs having similarity scores lower than a threshold INLINEFORM2 . The cut-off threshold estimation is explained in Section SECREF30 . The remaining document pairs from the strong filter are then sent to the revision network module. In the
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-cc8867b034c483f270107bb2310b68659139b195b0db405db9ac19fa5cd5e516

Passage ID: `qasper-passage-v1-cc8867b034c483f270107bb2310b68659139b195b0db405db9ac19fa5cd5e516`; retrieval score: 4.822807186841661.

Word count: 100.

```text
Wikipedia revision dumps and our simulated data sets. In order to reduce the computation time, we have computed document distances at the paragraph level and implemented a boosting learning system using Apache Spark. Although we have demonstrated the superiority of our semantic measures only in the revision detection experiments, wDTW and wTED can also be used as semantic distance measures in many clustering, classification tasks.

Our revision detection system can be enhanced with richer features such as author information and writing styles, and exact changes in revision pairs. Another interesting aspect we would like to explore in the future is
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-7d89d0be5af83d59e23a0f8fa4c16468d06c8353d5d620049a019e82c74fb89f

Passage ID: `qasper-passage-v1-7d89d0be5af83d59e23a0f8fa4c16468d06c8353d5d620049a019e82c74fb89f`; retrieval score: 4.469348422510779.

Word count: 100.

```text
We use precision, recall and F-measure to evaluate the detected revisions. A true positive case is a correctly identified revision. A false positive case is an incorrectly identified revision. A false negative case is a missed revision record.

We illustrate the performances of wDTW, wTED, WMD, VSM, PV-DTW and PV-TED on the Wikipedia revision dumps in Figure FIGREF43 . wDTW and wTED have the highest F-measure scores compared to the rest of four measures, and wDTW also have the highest precision and recall scores. Figure FIGREF49 shows the average evaluation results on the simulated data sets. From left to right,
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1709.01256:12:0` | full | 0:243 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 500.

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

#### Rank 1: qasper-passage-v1-d5c5f5aa5610cf47f123cd2c451a98268674785e4c889f6da788bc7dc81be2d2

Passage ID: `qasper-passage-v1-d5c5f5aa5610cf47f123cd2c451a98268674785e4c889f6da788bc7dc81be2d2`; retrieval score: 3.461889615121081.

Word count: 100.

```text
Table TABREF14 presents results for all models across the four variations of the dataset. First, BERT is consistently the best approach for in-scope, followed by MLP. Second, out-of-scope query performance is much lower than in-scope across all methods. Training on less data (Small and Imbalanced) yields models that perform slightly worse on in-scope queries. The trend is mostly the opposite when evaluating out-of-scope, where recall increases under the Small and Imbalanced training conditions. Under these two conditions, the size of the in-scope training set was decreased, while the number of out-of-scope training queries remained constant. This indicates that out-of-scope performance
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-a4f0d29fbd8cff8ed1ed565cca5662661d25fe32e70a80dcc4a4671bc46d621a

Passage ID: `qasper-passage-v1-a4f0d29fbd8cff8ed1ed565cca5662661d25fe32e70a80dcc4a4671bc46d621a`; retrieval score: 3.0568108903483733.

Word count: 91.

```text
when evaluating out-of-scope, where recall increases under the Small and Imbalanced training conditions. Under these two conditions, the size of the in-scope training set was decreased, while the number of out-of-scope training queries remained constant. This indicates that out-of-scope performance can be increased by increasing the relative number of out-of-scope training queries. We do just that in the OOS+ setting—where the models were trained on the full training set as well as 150 additional out-of-scope queries—and see that performance on out-of-scope increases substantially, yet still remains low relative to in-scope accuracy.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-7b2fe0afe6ab885d6ab879213308b6308d0717e68c073bdfd6560f441102f018

Passage ID: `qasper-passage-v1-7b2fe0afe6ab885d6ab879213308b6308d0717e68c073bdfd6560f441102f018`; retrieval score: 3.018859730994846.

Word count: 92.

```text
another where we augment the 250 OOS+ out-of-scope training queries with 14,750 sentences sampled from Wikipedia.

From a development point of view, the oos-train and oos-binary methods both require careful curation of an out-of-scope training set, and this set can be tailored to individual systems. The oos-threshold method is a more general decision rule that can be applied to any model that produces a probability. In our evaluation, the out-of-scope threshold was chosen to be the value which yielded the highest validation score across all intents, treating out-of-scope as its own intent.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-1077bb0201cbc5d2e9a95a4a3f200eac46d6ebac112bc07c9e573e1042b944d1

Passage ID: `qasper-passage-v1-1077bb0201cbc5d2e9a95a4a3f200eac46d6ebac112bc07c9e573e1042b944d1`; retrieval score: 2.9035924328689156.

Word count: 100.

```text
For all queries collected, all tokens were down-cased, and all end-of-sentence punctuation was removed. Additionally, all duplicate queries were removed and replaced.

In an effort to reduce bias in the in-scope data, we placed all queries from a given crowd worker in a single split (train, validation, or test). This avoids the potential issue of similar queries from a crowd worker ending up in both the train and test sets, for instance, which would make the train and test distributions unrealistically similar. We note that this is a recommendation from concurrent work by BIBREF3. We also used this procedure for
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-fb30537295a2d1b46677500c7c8df97110ecf8d3b39ddbc7a3c55cc17eb57f49

Passage ID: `qasper-passage-v1-fb30537295a2d1b46677500c7c8df97110ecf8d3b39ddbc7a3c55cc17eb57f49`; retrieval score: 2.1452335935524034.

Word count: 100.

```text
knowledge of the capabilities of a system.

Table TABREF20 compares our dataset with other short-query intent classification datasets. The Snips BIBREF0 dataset and the dataset presented in BIBREF10 are the most similar to the in-scope part of our work, with the same type of conversational agent requests. Like our work, both of these datasets were bootstrapped using crowdsourcing. However, the Snips dataset has only a small number of intents and an enormous number of examples of each. Snips does present a low-data variation, with 70 training queries per intent, in which performance drops slightly. The dataset presented in BIBREF10 has
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 483.

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

#### Rank 1: qasper-passage-v1-e9a714eed36a662c70bd7d950878d87c83251cd31973f6cb6702d88fb0302301

Passage ID: `qasper-passage-v1-e9a714eed36a662c70bd7d950878d87c83251cd31973f6cb6702d88fb0302301`; retrieval score: 5.083391987351941.

Word count: 100.

```text
as further insights on the performance of our model across languages on a different NLP task such as Opinion Target Extraction (OTE). Thus, we empirically demonstrate the validity and strong performance of our approach for six languages in seven different datasets of the restaurant domain. Every experiment and result presented in this note is novel.

In this sense, we show that our approach is not only competitive across languages and domains for Named Entity Recognition, as shown by BIBREF7 , but that it can be straightforwardly adapted to different tasks and domains such as OTE. Furthermore, we release the system
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-abca7d83bec6af082abb91745264d29a8b31af4f0ba2e3c25f6ea96c917ee218

Passage ID: `qasper-passage-v1-abca7d83bec6af082abb91745264d29a8b31af4f0ba2e3c25f6ea96c917ee218`; retrieval score: 5.02294485298715.

Word count: 100.

```text
data sources. We show that our approach, despite the lack of hand-engineered, language-specific features, obtains state-of-the-art results in 7 datasets for 6 languages on the ABSA benchmarks BIBREF4 , BIBREF5 , BIBREF6 .

The main contribution of this research note is providing an extension or addendum to previous work on sequence labelling BIBREF7 by reporting additional experimental results as well as further insights on the performance of our model across languages on a different NLP task such as Opinion Target Extraction (OTE). Thus, we empirically demonstrate the validity and strong performance of our approach for six languages in seven different
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-c6ed11b78b53481226476576731119ae6b5fe7e5658d9894865dfea1e086c7eb

Passage ID: `qasper-passage-v1-c6ed11b78b53481226476576731119ae6b5fe7e5658d9894865dfea1e086c7eb`; retrieval score: 3.106509104712995.

Word count: 100.

```text
it is useful to look at the most common errors for all three languages, namely, `place', `food' and `restaurant', which are also among the top 5 most frequent targets in the gold standard sets. By looking at Examples (1-3) we would say that in all three cases `place' should be annotated as opinion target. However, (2) is a false positive (FP), (3) is a false negative (FN) and (1) is an example from the training set in which `place' is annotated as target. This is the case with many instances of `place' for which there seems to be some inconsistency
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-651b3ba0810967e94bb5ecffd56c802e497efd53cd1afdd06d123b23de5cd91c

Passage ID: `qasper-passage-v1-651b3ba0810967e94bb5ecffd56c802e497efd53cd1afdd06d123b23de5cd91c`; retrieval score: 2.9750874168821593.

Word count: 100.

```text
We trained our system for 5 other languages on the ABSA 2016 datasets, using the same strategy as for English. We choose the best Clark-Word2vec combination (with and without Brown clusters) via 5-cross validation on the training data. The features are exactly the same as those used for English, the only change is the data on which the clusters are trained. Table TABREF19 reports on the detailed results obtained for each of the languages. In bold we show the best model chosen via 5-fold CV. Moreover, we also show the best models using only one of each of the clustering
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-0e5b4c145148ed99d2533a596068b4b65b56242dc2cd86bb878dbc94564c57dc

Passage ID: `qasper-passage-v1-0e5b4c145148ed99d2533a596068b4b65b56242dc2cd86bb878dbc94564c57dc`; retrieval score: 2.911318895086762.

Word count: 100.

```text
sources of errors: (a) errors caused by ambiguity in the use of certain source forms that may or may not refer to an opinion target; (b) span errors, where the target has only been partially annotated; and (c) unknown targets, which the system was unable to annotate by generalizing on the training data or clusters.

With respect to type (a), it is useful to look at the most common errors for all three languages, namely, `place', `food' and `restaurant', which are also among the top 5 most frequent targets in the gold standard sets. By looking at Examples (1-3) we
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 500.

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

#### Rank 1: qasper-passage-v1-f85e20cc773194b847566459fa96db21963dd85e74f7a10294d93ec317bbe8ed

Passage ID: `qasper-passage-v1-f85e20cc773194b847566459fa96db21963dd85e74f7a10294d93ec317bbe8ed`; retrieval score: 4.720823213266234.

Word count: 100.

```text
tags as well as the list of expected tags from the test set. Finally, we use the cosine similarity measure to calculate how semantically similar these two lists are.

Recommendation diversity. As defined in BIBREF18 , we calculate recommendation diversity as the average dissimilarity of all pairs of tags in the list of recommended tags. Thus, given a distance function INLINEFORM0 that corresponds to the dissimilarity between two tags INLINEFORM1 and INLINEFORM2 in the list of recommended tags, INLINEFORM3 is given as the average dissimilarity of all pairs of tags: DISPLAYFORM0

where INLINEFORM0 is the number of evaluated e-books and
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.04042:6:8` | full | 0:416 |

#### Rank 2: qasper-passage-v1-0ffb86ddecd3a88c0ee97a22425824bab3e00dabafbf44f867d16e4a1262c114

Passage ID: `qasper-passage-v1-0ffb86ddecd3a88c0ee97a22425824bab3e00dabafbf44f867d16e4a1262c114`; retrieval score: 4.4193044585264065.

Word count: 100.

```text
In this work, we measure (i) recommendation accuracy, (ii) semantic similarity, and (iii) recommendation diversity to evaluate the quality of our approaches from different perspectives.

Recommendation accuracy. We use Normalized Discounted Cumulative Gain (nDCG) BIBREF15 to measure the accuracy of the tag recommendation approaches. The nDCG measure is a standard ranking-dependent metric that not only measures how many tags can be correctly predicted but also takes into account their position in the recommendation list with length of INLINEFORM0 . It is based on the Discounted Cummulative Gain, which is given by: DISPLAYFORM0

where INLINEFORM0 is a function that returns 1
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-c69ed02b1ac8fa07b56e7b27044a072c9f321648fecfe9920b48a361056714af

Passage ID: `qasper-passage-v1-c69ed02b1ac8fa07b56e7b27044a072c9f321648fecfe9920b48a361056714af`; retrieval score: 4.147314608889094.

Word count: 85.

```text
how semantically similar (based on learned Doc2Vec BIBREF7 embeddings) the list of recommended tags is to the list of relevant tags. We use this additional metric to measure not only exact “hits” of our recommendations but also semantic matches.

Our evaluation results show that combining both data sources enhances the quality of tag recommendations for annotating e-books. Furthermore, approaches that solely train on Amazon search terms provide poor performance in terms of accuracy but deliver good results in terms of semantic similarity and recommendation diversity.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-f556672986a184323fafea0d3a593addd51c5fe85319959b3c379543ae1d21ef

Passage ID: `qasper-passage-v1-f556672986a184323fafea0d3a593addd51c5fe85319959b3c379543ae1d21ef`; retrieval score: 3.810068136956738.

Word count: 100.

```text
evaluation comprises of a rich set of 19 different algorithms to recommend tags for e-books, which we group into (i) popularity-based, (ii) similarity-based (i.e., using content information), and (iii) hybrid approaches. We evaluate our approaches in terms of accuracy, semantic similarity and diversity on the review content of Amazon users, which reflects the readers' vocabulary. With semantic similarity, we measure how semantically similar (based on learned Doc2Vec BIBREF7 embeddings) the list of recommended tags is to the list of relevant tags. We use this additional metric to measure not only exact “hits” of our recommendations but also semantic matches.

Our
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-cca7dee5ba79aca1cecb731026a369f982867b77bba7a75612e63997757a0533

Passage ID: `qasper-passage-v1-cca7dee5ba79aca1cecb731026a369f982867b77bba7a75612e63997757a0533`; retrieval score: 3.795306022252006.

Word count: 100.

```text
are to the expected review keywords. For this, we first extract the textual content in the form of the description text, title, editor tags and Amazon search terms of e-books from our dataset. We then train a Doc2Vec BIBREF7 model on the content. Then, we use the model to infer the latent representation for both the complete list of recommended tags as well as the list of expected tags from the test set. Finally, we use the cosine similarity measure to calculate how semantically similar these two lists are.

Recommendation diversity. As defined in BIBREF18 , we calculate recommendation diversity
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.04042:6:8` | partial | 0:88 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 485.

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

#### Rank 1: qasper-passage-v1-65f95961129f47c25b78720bcb89c8e3246bb2c560395339fe02ee53d84c3692

Passage ID: `qasper-passage-v1-65f95961129f47c25b78720bcb89c8e3246bb2c560395339fe02ee53d84c3692`; retrieval score: 6.640449090163637.

Word count: 100.

```text
This section discusses qualitative results to better understand how the proposed model uses the navigation graph.

We analyze the evolution of the attention weights INLINEFORM0 in Eq. () to assess if the decoder layer of the proposed model is attending to the correct parts of the behavioral graph when making predictions. Fig FIGREF33 (b) shows an example of the resulting attention map for the case of a correct prediction. In the Figure, the attention map is depicted as a scaled and normalized 2D array of color codes. Each column in the array shows the attention distribution INLINEFORM1 used to generate
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-976701b6b66d6e3b153e61aee54091883d80b1b48e78d6e46b5a0b6477d9de07

Passage ID: `qasper-passage-v1-976701b6b66d6e3b153e61aee54091883d80b1b48e78d6e46b5a0b6477d9de07`; retrieval score: 6.608821248675907.

Word count: 100.

```text
Table TABREF28 shows the performance of the models considered in our evaluation on both test sets. The next two sections discuss the results in detail.

First, we can observe that the final model “Ours with Mask and Ordered Triplets” outperforms the Baseline and Ablation models on all metrics in previously seen environments. The difference in performance is particularly evident for the Exact Match and Goal Match metrics, with our model increasing accuracy by 35% and 25% in comparison to the Baseline and Ablation models, respectively. These results suggest that providing the behavioral navigation graph to the model and allowing it
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1810.00663:10:1` | partial | 0:484 |

#### Rank 3: qasper-passage-v1-9dddd60c267f33b2fea5f287347c311c71e9e1e99a575a3a4e57bae3956bcf45

Passage ID: `qasper-passage-v1-9dddd60c267f33b2fea5f287347c311c71e9e1e99a575a3a4e57bae3956bcf45`; retrieval score: 6.250067530439379.

Word count: 100.

```text
We compare the proposed approach for translating natural language instructions into a navigation plan against alternative deep-learning models:

[align=left,leftmargin=0em,labelsep=0.4em,font=]

The baseline approach is based on BIBREF20 . It divides the task of interpreting commands for behavioral navigation into two steps: path generation, and path verification. For path generation, this baseline uses a standard sequence-to-sequence model augmented with an attention mechanism, similar to BIBREF23 , BIBREF6 . For path verification, the baseline uses depth-first search to find a route in the graph that matches the sequence of predicted behaviors. If no route matches perfectly, the baseline changes up to three behaviors
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-451ea3fd68ee801d292c592f71204fecd32a9e18c073ef79607c117082a95610

Passage ID: `qasper-passage-v1-451ea3fd68ee801d292c592f71204fecd32a9e18c073ef79607c117082a95610`; retrieval score: 5.916274469011899.

Word count: 100.

```text
the graph INLINEFORM8 .

Attention layer: Matrices INLINEFORM0 and INLINEFORM1 generated by the encoder layer are combined using an attention mechanism. We use one-way attention because the graph contains information about the whole environment, while the instruction has (potentially incomplete) local information about the route of interest. The use of attention provides our model with a two-step strategy to interpret commands. This resembles the way people find paths on a map: first, relevant parts on the map are selected according to their affinity to each of the words in the input instruction (attention layer); second, the selected parts are connected
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-720504fc423c4cb62a28a2053193adcb979bbb04471a9ee39a6bf58b822be805

Passage ID: `qasper-passage-v1-720504fc423c4cb62a28a2053193adcb979bbb04471a9ee39a6bf58b822be805`; retrieval score: 5.899132910435576.

Word count: 100.

```text
similar to BIBREF23 , BIBREF6 . For path verification, the baseline uses depth-first search to find a route in the graph that matches the sequence of predicted behaviors. If no route matches perfectly, the baseline changes up to three behaviors in the predicted sequence to try to turn it into a valid path.

To test the impact of using the behavioral graphs as an extra input to our translation model, we implemented a version of our approach that only takes natural language instructions as input. In this ablation model, the output of the bidirectional GRU that encodes the input instruction
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 500.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "a6c1cfab37b756275380368b1d9f8cdb8929f57e": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1810.00663:10:1": [
        [
          484,
          572
        ]
      ],
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

#### Rank 1: qasper-passage-v1-42a0e46b448f6fccfaa9d33b034113b7da3a66025bff6b7f5e868a556f8b28a5

Passage ID: `qasper-passage-v1-42a0e46b448f6fccfaa9d33b034113b7da3a66025bff6b7f5e868a556f8b28a5`; retrieval score: 10.397241771769714.

Word count: 100.

```text
language cues between age groups above age 35 tend to become smaller (see Figure FIGREF39 -A,B,C) and making the prediction harder for older people BIBREF74 . In this case, the other data modality (e.g., visual content) can play integral role as a complementary source for age inference. For gender prediction (see Table TABREF44 ), on average, the profile image-based predictor provides a more accurate prediction for both the depressed and control class (0.92 and 0.90) compared to content-based predictor (0.82). For age prediction (see Table TABREF42 ), textual content-based predictor (on average 0.60) outperforms both of the visual-based predictors (on
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-95de0c3818dcf5dfc30c6837c70d1868c3f6151dd862b4a8ffe7133718e3d7c3

Passage ID: `qasper-passage-v1-95de0c3818dcf5dfc30c6837c70d1868c3f6151dd862b4a8ffe7133718e3d7c3`; retrieval score: 10.028485552845817.

Word count: 100.

```text
We now provide an in-depth analysis of visual and textual content of vulnerable users.

Visual Content Analysis: We show that the visual content in images from posts as well as profiles provide valuable psychological cues for understanding a user's depression status. Profile/posted images can surface self-stigmatization BIBREF53 . Additionally, as opposed to typical computer vision framework for object recognition that often relies on thousands of predetermined low-level features, what matters more for assessing user's online behavior is the emotions reflected in facial expressions BIBREF54 , attributes contributing to the computational aesthetics BIBREF55 , and sentimental quotes they may subscribe to
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-4bc793780134006880da65a7fb0733f4bee280a7b52bfecb2424be5d1407cf6c

Passage ID: `qasper-passage-v1-4bc793780134006880da65a7fb0733f4bee280a7b52bfecb2424be5d1407cf6c`; retrieval score: 7.642478017483253.

Word count: 100.

```text
gender and age from both the profile and shared images. We evaluate the performance for gender and age prediction task on INLINEFORM0 and INLINEFORM1 respectively as shown in Table TABREF42 and Table TABREF44 .

Demographic Prediction Analysis:

We delve deeper into the benefits and drawbacks of each data modality for demographic information prediction. This is crucial as the differences between language cues between age groups above age 35 tend to become smaller (see Figure FIGREF39 -A,B,C) and making the prediction harder for older people BIBREF74 . In this case, the other data modality (e.g., visual content) can play integral role
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-ce8d61367240c1b3e049d41ef25c363bf8da54fa821c40ef6e635ae6b3771785

Passage ID: `qasper-passage-v1-ce8d61367240c1b3e049d41ef25c363bf8da54fa821c40ef6e635ae6b3771785`; retrieval score: 7.448986442522971.

Word count: 100.

```text
the "Analytic thinking" of this user is considered high 48.43 (Median:36.95, Mean: 40.18) and this decreases the chance of this person being classified into the depressed group by the log-odds of -1.41. Depressed users have significantly lower "Analytic thinking" score compared to control class. Moreover, the 40.46 "Clout" score is a low value (Median: 62.22, Mean: 57.17) and it decreases the chance of being classified as depressed. With respect to the visual features, for instance, the mean and the median of 'shared_colorfulness' is 112.03 and 113 respectively. The value of 136.71 would be high; thus, it decreases the chance of
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-01b96432a5378e65824f570d269ecb61f5f3680bb232f37172ccd7316f53c45b

Passage ID: `qasper-passage-v1-01b96432a5378e65824f570d269ecb61f5f3680bb232f37172ccd7316f53c45b`; retrieval score: 7.333352995823438.

Word count: 100.

```text
the chance of being classified as depressed. With respect to the visual features, for instance, the mean and the median of 'shared_colorfulness' is 112.03 and 113 respectively. The value of 136.71 would be high; thus, it decreases the chance of being depressed for this specific user by log-odds of -0.54. Moreover, the 'profile_naturalness' of 0.46 is considered high compared to 0.36 as the mean for the depressed class which justifies pull down of the log-odds by INLINEFORM2 . For network features, for instance, 'two_hop_neighborhood' for depressed users (Mean : 84) are less than that of control users (Mean: 154), and
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 500.

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

#### Rank 1: qasper-passage-v1-73905bd6b0976d10bed88e667e26f4a2aecb23701b3fb6df4e24b4cfc135d2dd

Passage ID: `qasper-passage-v1-73905bd6b0976d10bed88e667e26f4a2aecb23701b3fb6df4e24b4cfc135d2dd`; retrieval score: 5.891759623116437.

Word count: 100.

```text
E17-1101 showed that given input with author traits like gender, it is possible to retain those traits in Statistical Machine Translation (SMT) models. W17-4727 showed that incorporating morphological analysis in the decoder improves NMT performance for morphologically rich languages. burlot:hal-01618387 presented a new protocol for evaluating the morphological competence of MT systems, indicating that current translation systems only manage to capture some morphological phenomena correctly. Regarding the application of constraints in NMT, N16-1005 presented a method for controlling the politeness level in the generated output. DBLP:journals/corr/FiclerG17aa showed how to guide a neural text generation system towards style and content parameters
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-3974a968f2400751ea0cc5e30615c693df2ad08934dd05feaf2886ed2e60921b

Passage ID: `qasper-passage-v1-3974a968f2400751ea0cc5e30615c693df2ad08934dd05feaf2886ed2e60921b`; retrieval score: 4.384852416524233.

Word count: 42.

```text
their published results and the Google Translate baseline. As may be expected, Google Translate outperforms their system as it is trained on a different corpus and may use more complex machine translation models. Using our method improves the BLEU score even further.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-619b5dcd4e217e0ed4339af2d94100684af782c3e831779eb95068d2d6becf09

Passage ID: `qasper-passage-v1-619b5dcd4e217e0ed4339af2d94100684af782c3e831779eb95068d2d6becf09`; retrieval score: 3.6564986119692198.

Word count: 100.

```text
on the dependent, on both, or on none of them BIBREF0 . This morphological diversity creates a challenge for machine translation, as there are ambiguous cases where more than one correct translation exists for the same source sentence. For example, while the English sentence “I love language” is ambiguous with respect to the gender of the speaker, Hebrew marks verbs for the gender of their subject and does not allow gender-neutral translation. This allows two possible Hebrew translations – one in a masculine and the other in a feminine form. As a consequence, a sentence-level translator (either human or machine)
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-6b49b7273767b579e4d04bc8ee68e61c983350d185023893a00e621c4f07d241

Passage ID: `qasper-passage-v1-6b49b7273767b579e4d04bc8ee68e61c983350d185023893a00e621c4f07d241`; retrieval score: 3.6367758809786848.

Word count: 100.

```text
Closely related to our work, vanmassenhove-hardmeier-way:2018:EMNLP proposed a method and an English-French test set to evaluate gender-aware translation, based on the Europarl corpus BIBREF7 . We evaluate our method (using Google Translate and the given prefixes) on their test set to see whether it is applicable to another language pair and domain. Table shows the results of our approach vs. their published results and the Google Translate baseline. As may be expected, Google Translate outperforms their system as it is trained on a different corpus and may use more complex machine translation models. Using our method improves the BLEU score
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-e28305572ee2ca44e2c2ae663e30bb68bc7d5e6074eb901eed13882f85c29172

Passage ID: `qasper-passage-v1-e28305572ee2ca44e2c2ae663e30bb68bc7d5e6074eb901eed13882f85c29172`; retrieval score: 3.5268273138612845.

Word count: 100.

```text
interlocutors), which we concatenate to a given input sentence that we would like to translate accordingly. We then show that a black-box NMT system makes the desired morphological decisions according to the given hint, even when no other evidence is available on the source side. While adding those hints results in additional text on the target side, we show that it is simple to remove, leaving only the desired translation.

Our method is appealing as it only requires simple pre-and-post processing of the inputs and outputs, without considering the system internals, or requiring specific annotated data and training procedure as
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 442.

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

#### Rank 1: qasper-passage-v1-a665a881d46421203dabddcf3c9c3a444df68273826af95d719bdd948f429f8e

Passage ID: `qasper-passage-v1-a665a881d46421203dabddcf3c9c3a444df68273826af95d719bdd948f429f8e`; retrieval score: 8.126504040526505.

Word count: 100.

```text
Another major performance concern in distributed computing is network bandwidth. Since the experts are stationary (see above) and the number of gating parameters is small, most of the communication involves sending the inputs and outputs of the experts across the network. To maintain computational efficiency, the ratio of an expert's computation to the size of its input and output must exceed the ratio of computational to network capacity of the computing device. For GPUs, this may be thousands to one. In our experiments, we use experts with one hidden layer containing thousands of RELU-activated units. Since the weight matrices in
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-ef66a0ff9d9fcf75d26f2cbdd6268698bd09588ab3cadf4baf21c787a4a89b10

Passage ID: `qasper-passage-v1-ef66a0ff9d9fcf75d26f2cbdd6268698bd09588ab3cadf4baf21c787a4a89b10`; retrieval score: 7.7178654695076085.

Word count: 100.

```text
sent across the network, the number of (example, parameter) interactions is limited by network bandwidth instead of computational capacity.

Depending on the scheme, loss terms may be necessary to achieve the desired level of sparsity per-chunk and/or per example. BIBREF13 use three such terms. These issues can affect both model quality and load-balancing.

Model capacity is most critical for very large data sets. The existing literature on conditional computation deals with relatively small image recognition data sets consisting of up to 600,000 images. It is hard to imagine that the labels of these images provide a sufficient signal to adequately
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-d0520155eb87ab63c81c37e9e599584fe5131bded60012f1d85459c012988dda

Passage ID: `qasper-passage-v1-d0520155eb87ab63c81c37e9e599584fe5131bded60012f1d85459c012988dda`; retrieval score: 7.344696677912808.

Word count: 100.

```text
. The amount of noise per component is controlled by a second trainable weight matrix INLINEFORM1 . DISPLAYFORM0 DISPLAYFORM1

We train the gating network by simple back-propagation, along with the rest of the model. If we choose INLINEFORM0 , the gate values for the top k experts have nonzero derivatives with respect to the weights of the gating network. This type of occasionally-sensitive behavior is described in BIBREF9 with respect to noisy rectifiers. Gradients also back-propagate through the gating network to its inputs. Our method differs here from BIBREF13 who use boolean gates and a REINFORCE-style approach to train the
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-71f29b1e747fb32e24d038820ada84303529d19c56fda5aeda6751e8a3d207df

Passage ID: `qasper-passage-v1-71f29b1e747fb32e24d038820ada84303529d19c56fda5aeda6751e8a3d207df`; retrieval score: 7.312960590890994.

Word count: 89.

```text
and also observed in BIBREF38 , using a batchwise function during training (such as INLINEFORM0 ) requires modifications to the inference when we may not have a large batch of examples. Our solution to this is to train a vector INLINEFORM1 of per-expert threshold values to approximate the effects of the batchwise mask. We use the following mask at inference time: DISPLAYFORM0

To learn the threshold values, we apply an additional loss at training time which is minimized when the batchwise mask and the threshold mask are identical. DISPLAYFORM0
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-41496a9638f406ccdb16f1e20568d0b1678cff6644f3a77975c92b16f28c3659

Passage ID: `qasper-passage-v1-41496a9638f406ccdb16f1e20568d0b1678cff6644f3a77975c92b16f28c3659`; retrieval score: 7.191140647810738.

Word count: 90.

```text
exceed the ratio of computational to network capacity of the computing device. For GPUs, this may be thousands to one. In our experiments, we use experts with one hidden layer containing thousands of RELU-activated units. Since the weight matrices in the expert have sizes INLINEFORM0 _ INLINEFORM1 _ INLINEFORM2 and INLINEFORM3 _ INLINEFORM4 _ INLINEFORM5 , the ratio of computation to input and output is equal to the size of the hidden layer. Conveniently, we can increase computational efficiency simply by using a larger hidden layer, or more hidden layers.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 479.

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

#### Rank 1: qasper-passage-v1-f4441011747d688dfa43272dab85ce2fd4517719d1ff0d7ff25137983f7a123d

Passage ID: `qasper-passage-v1-f4441011747d688dfa43272dab85ce2fd4517719d1ff0d7ff25137983f7a123d`; retrieval score: 8.860433715083937.

Word count: 100.

```text
example demonstrates that the proposed STN works pretty well to help attend to more related opinion words given a particular aspect.

Some predictions of our model and those of LSTM and OURS w/o THA & STN are given in Table TABREF43 . The models incorporating attention-based opinion summary (i.e., OURS and OURS w/o THA & STN) can better determine if the commonly-used nouns are aspect terms or not (e.g. “device” in the first input), since they make decisions based on the global opinion information. Besides, they are able to extract some infrequent or even misspelled aspect terms (e.g. “survice” in
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-1dd4dcb50edd2a5ab590af2d5dee9eaa0dfeacdeb244f4e158f801a36068a350

Passage ID: `qasper-passage-v1-1dd4dcb50edd2a5ab590af2d5dee9eaa0dfeacdeb244f4e158f801a36068a350`; retrieval score: 6.460337120780436.

Word count: 100.

```text
datasets. We also notice that RNCRF does not perform well on INLINEFORM0 and INLINEFORM1 (3.7% and 3.9% inferior than ours). We find that INLINEFORM2 and INLINEFORM3 contain many informal reviews, thus RNCRF's performance degradation is probably due to the errors from the dependency parser when processing such informal texts.

CMLA and MIN do not rely on dependency parsing, instead, they employ attention mechanism to distill opinion information to help aspect extraction. Our framework consistently performs better than them. The gains presumably come from two perspectives: (1) In our model, the opinion summary is exploited after performing the selective transformation conditioned
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-8eeab113afeadab3fbe1d433432b2d4086d8df7ea987fd24c336d76df5a158ff

Passage ID: `qasper-passage-v1-8eeab113afeadab3fbe1d433432b2d4086d8df7ea987fd24c336d76df5a158ff`; retrieval score: 5.799224185690088.

Word count: 100.

```text
problem. Traditional sequence models such as Conditional Random Fields (CRFs) BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 , Long Short-Term Memory Networks (LSTMs) BIBREF6 and classification models such as Support Vector Machine (SVM) BIBREF7 have been applied to tackle the ATE task, and achieved reasonable performance. One drawback of these existing works is that they do not exploit the fact that, according to the task definition, aspect terms should co-occur with opinion-indicating words. Thus, the above methods tend to output false positives on those frequently used aspect terms in non-opinionated sentences, e.g., the word “restaurant” in “the restaurant was packed
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-28881b850ccee0c2d2eb2b2925aa223480dab9e1534ff868cf3f36f33f549aea

Passage ID: `qasper-passage-v1-28881b850ccee0c2d2eb2b2925aa223480dab9e1534ff868cf3f36f33f549aea`; retrieval score: 5.20647279228797.

Word count: 100.

```text
and opinion representations respectively. They map INLINEFORM2 and INLINEFORM3 to the same subspace. Here the aspect feature INLINEFORM4 acts as a “filter” to keep more important opinion features. Equation EQREF14 also introduces a residual block to obtain a better opinion representation INLINEFORM5 , which is conditioned on the current aspect feature INLINEFORM6 .

For distilling the global opinion summary, we introduce a bi-linear term to calculate the association score between INLINEFORM0 and each INLINEFORM1 : DISPLAYFORM0

where INLINEFORM0 and INLINEFORM1 are parameters of the Bi-Linear Attention layer. The improved opinion summary INLINEFORM2 at the time INLINEFORM3 is obtained via the
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-88968d7e15b011aad7ed233b8ed60ecf413230d2c7c987509ce7422ed5709b65

Passage ID: `qasper-passage-v1-88968d7e15b011aad7ed233b8ed60ecf413230d2c7c987509ce7422ed5709b65`; retrieval score: 5.155235486380657.

Word count: 55.

```text
the accuracy of aspect prediction, although the ground-truth opinion words were annotated by these authors. Moreover, one should notice that those joint extraction methods do not care about the correspondence between the extracted aspect terms and opinion words. Therefore, the necessity of such joint extraction should be obelized, given the experimental findings in this paper.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 455.

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

#### Rank 1: qasper-passage-v1-e42ffdc865170c86863135ab01227cd37d6667a960fcabb9b87e74ea57f1f3c3

Passage ID: `qasper-passage-v1-e42ffdc865170c86863135ab01227cd37d6667a960fcabb9b87e74ea57f1f3c3`; retrieval score: 3.9948758486673146.

Word count: 100.

```text
Here we use network and text analysis tools to compare causal attribution networks (Sec. "Comparing causal networks" ). Crucially, nodes in these networks are defined only by their written descriptions, and multiple written descriptions can represent the same conceptual entity. Thus, to understand how causal attribution networks can be combined, we introduce and analyze a method for fusing networks (Sec. "Fusing causal networks" ) that builds off both the network structure and associated text information and explicitly incorporates conceptual equivalencies. Lastly, in Sec. "Inferring the size of the causal attribution network" we use the degree of overlap in these networks
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-ebcf8e5ddc1154bb54d225a59921e2953f4bd0a5831d1d345611470d67826348

Passage ID: `qasper-passage-v1-ebcf8e5ddc1154bb54d225a59921e2953f4bd0a5831d1d345611470d67826348`; retrieval score: 3.916105979885896.

Word count: 100.

```text
The construction of causal attribution networks generates important knowledge networks that may inform causal inference research and even help future AI systems to perform causal reasoning, but these networks are time-consuming and costly to generate, and to date no efforts have been made to combine different networks. Our work not only studies the potential for fusing different networks together, but also infers the overall size of the total causal attribution network being explored.

We used capture-recapture estimators to infer the number of nodes and links in the underlying causal attribution network, given the Wikidata and ConceptNet networks and using NetFUSES
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-efb05614dda7682b5d2c05516c7414562ad3d4a7f82635dca33125277e214413

Passage ID: `qasper-passage-v1-efb05614dda7682b5d2c05516c7414562ad3d4a7f82635dca33125277e214413`; retrieval score: 3.762400045770697.

Word count: 100.

```text
These causal attributions networks are separate efforts to map out the underlying or latent causal attribution network held collectively by humans. It is natural to then ask if these different efforts can be combined in an effective way. Fusing these networks together can provide a single causal attribution network for researchers to study.

At the most basic level, one can fuse these networks together simply by taking their union, defining a single network containing all the unique nodes and edges of the original networks. Unfortunately, nodes in these networks are identified by their sentences, and this graph union assumes that
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-288d36fc09aaee7c9496bdce8348e8d246dce6ff09c97c2150070fe1a3158873

Passage ID: `qasper-passage-v1-288d36fc09aaee7c9496bdce8348e8d246dce6ff09c97c2150070fe1a3158873`; retrieval score: 3.599594182210132.

Word count: 100.

```text
In this work we compare causal attribution networks derived from three datasets. A causal attribution dataset is a collection of text pairs that reflect cause-effect relationships proposed by humans (for example, “virus causes sickness”). These written statements identify the nodes of the network (see also our graph fusion algorithm for dealing with semantically equivalent statements) while cause-effect relationships form the directed edges (“virus” $\rightarrow $ “sickness”) of the causal attribution network.

We collected causal attribution networks from three sources of data: English Wikidata BIBREF11 , English ConceptNet BIBREF10 , and IPRnet BIBREF12 . Wikidata and ConceptNet, are large knowledge graphs
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1812.06038:0:0` | full | 0:515 |

#### Rank 5: qasper-passage-v1-683bf861c56e43b9ce838e23a1b31e4c77e000cd45fa7542b1fcf115d3ac9712

Passage ID: `qasper-passage-v1-683bf861c56e43b9ce838e23a1b31e4c77e000cd45fa7542b1fcf115d3ac9712`; retrieval score: 3.188420266971553.

Word count: 100.

```text
We perform a descriptive analysis of the three datasets, comparing and contrasting their features and properties. We focus on two aspects, the network structure and the text information (the written descriptions associated with each node in the network). Understanding these data at these levels can inform efforts to combine different causal attribution networks (Sec. "Fusing causal networks" ).

Table 1 and Fig. 2 summarize network characteristics for the three causal attribution networks. We focus on standard measures of network structure, measuring the sizes, densities, motif structure, and connectedness of the three networks. Both Wikidata and ConceptNet, the two larger networks,
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 500.

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

#### Rank 1: qasper-passage-v1-fdb62659f19a2d03f251482260b1dc590506a8e2e17bf0373206cde41e3b09b0

Passage ID: `qasper-passage-v1-fdb62659f19a2d03f251482260b1dc590506a8e2e17bf0373206cde41e3b09b0`; retrieval score: 6.745189662245311.

Word count: 86.

```text
We established strong baselines for two story narrative understanding datasets: CaTeRS and RED. We have shown that neural network-based models can outperform feature-based models with wide margins, and we conducted an ablation study to show that contextualized representation learning can boost performance of NN models. Further research can focus on more systematic study or build stronger NN models over the same datasets used in this work. Exploring possibilities to directly apply temporal relation extraction to enhance performance of story generation systems is another promising research direction.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-79760b3c86adbb313fa96d26b5d9026247356dd5cf9551dd84d58a83f2b6c4a0

Passage ID: `qasper-passage-v1-79760b3c86adbb313fa96d26b5d9026247356dd5cf9551dd84d58a83f2b6c4a0`; retrieval score: 6.292450398000178.

Word count: 66.

```text
rules. As we mention in the Section 2, CAEVO is the current state-of-the-art system for feature-based temporal event relation extraction BIBREF10 . It's widely used as the baseline for evaluating TB-Dense data. We adopt it as our baseline for evaluating CaTeRS and RED datasets. Additionally, several models BramsenDLB2006, ChambersJ2008, DoLuRo12, NingWuRo18, P18-1212 have successfully incorporated global inference to impose global prediction consistency such as temporal transitivity.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.11942:6:0` | partial | 424:912 |

#### Rank 3: qasper-passage-v1-30c2200d41532327fb50957a319a735cb9ff8ca62e8e8bafe86a67aafa70cb12

Passage ID: `qasper-passage-v1-30c2200d41532327fb50957a319a735cb9ff8ca62e8e8bafe86a67aafa70cb12`; retrieval score: 5.3822996332597155.

Word count: 100.

```text
The series of TempEval competitions BIBREF21 , BIBREF22 , BIBREF23 have attracted many research interests in predicting event temporal relations. Early attempts by BIBREF24 , BIBREF21 , BIBREF25 , BIBREF26 only use pair-wise classification models. State-of-the-art local methods, such as ClearTK BIBREF27 , UTTime BIBREF28 , and NavyTime BIBREF29 improve on earlier work by feature engineering with linguistic and syntactic rules. As we mention in the Section 2, CAEVO is the current state-of-the-art system for feature-based temporal event relation extraction BIBREF10 . It's widely used as the baseline for evaluating TB-Dense data. We adopt it as our baseline for evaluating
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.11942:6:0` | partial | 0:677 |

#### Rank 4: qasper-passage-v1-75378adc1f8159b5ef35d4f0a554b12f2e436ae08dba5b616cbaccdc2bd047f8

Passage ID: `qasper-passage-v1-75378adc1f8159b5ef35d4f0a554b12f2e436ae08dba5b616cbaccdc2bd047f8`; retrieval score: 4.808944619790568.

Word count: 69.

```text
Table TABREF25 contains the best hyper-parameters and Table TABREF26 contains micro-average F1 scores for both datasets on dev and test sets. We only consider positive pairs, i.e. correct predictions on NONE pairs are excluded for evaluation. In general, the baseline model CAEVO is outperformed by both NN models, and NN model with BERT embedding achieves the greatest performance. We now provide more detailed analysis and discussion for each dataset.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-9b6cfd861c2997cdf8070855d521af8d56d7b589ecd5c37993f87222a3765fd9

Passage ID: `qasper-passage-v1-9b6cfd861c2997cdf8070855d521af8d56d7b589ecd5c37993f87222a3765fd9`; retrieval score: 4.353422012358295.

Word count: 100.

```text
have been reported on CaTeRS and RED.

We apply neural network models that leverage recent advances in contextualized embeddings (BERT BIBREF13 ) to event-event relation extraction tasks for CaTeRS and RED. Our goal in this paper is to increase understanding of how well the state-of-the-art event relation models work for story/narrative comprehension.

In this paper, we report the first results of event temporal relation extraction on two under-explored story comprehension datasets: CaTeRS and RED. We establish strong baselines with neural network models enhanced by recent breakthrough of contextualized embeddings, BERT BIBREF13 . We summarize the contributions of the paper as
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 421.

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

#### Rank 1: qasper-passage-v1-f3d45f27145c5a3bc45b4376655b1fd86f3fdbb6339c4ed9df1d78ab6430b673

Passage ID: `qasper-passage-v1-f3d45f27145c5a3bc45b4376655b1fd86f3fdbb6339c4ed9df1d78ab6430b673`; retrieval score: 7.15282071415086.

Word count: 100.

```text
We evaluate our approach for six target languages: French (fr), Russian (ru), Arabic (ar), Chinese (zh), Hindi (hi), and Vietnamese (vi). These languages belong to four different language families. French, Russian, and Hindi are Indo-European languages, similar to English. Arabic, Chinese, and Vietnamese belong to Afro-Asiatic, Sino-Tibetan, and Austro-Asiatic family respectively. The choice of the six languages also reflects different training conditions depending on the amount of monolingual data. French and Russian, and Arabic can be regarded as high resource languages whereas Hindi has far less data and can be considered as low resource.

For experiments that use parallel data
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2002.07306:8:0` | full | 0:649 |

#### Rank 2: qasper-passage-v1-d0f54154523c9c5ca615abafdbda433c4d00eddd6784e14f78773ca79f297305

Passage ID: `qasper-passage-v1-d0f54154523c9c5ca615abafdbda433c4d00eddd6784e14f78773ca79f297305`; retrieval score: 6.901408713041676.

Word count: 100.

```text
training conditions depending on the amount of monolingual data. French and Russian, and Arabic can be regarded as high resource languages whereas Hindi has far less data and can be considered as low resource.

For experiments that use parallel data to initialize foreign specific parameters, we use the same datasets in the work of BIBREF6. Specifically, we use United Nations Parallel Corpus BIBREF18 for en-ru, en-ar, en-zh, and en-fr. We collect en-hi parallel data from IIT Bombay corpus BIBREF19 and en-vi data from OpenSubtitles 2018. For experiments that use only monolingual data to initialize foreign parameters, instead of training word-vectors
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2002.07306:8:0` | partial | 440:649 |

#### Rank 3: qasper-passage-v1-9e222adc696c03fc0fc932228fd1ae0be506e568f8eed50fafb97f378cb254f3

Passage ID: `qasper-passage-v1-9e222adc696c03fc0fc932228fd1ae0be506e568f8eed50fafb97f378cb254f3`; retrieval score: 6.305526638976049.

Word count: 100.

```text
For low resource languages, parallel data may not be available. In this case, we rely only on monolingual data (e.g., Wikipedias). We estimate word translation probabilities from word embeddings of the two languages. Word vectors of these languages can be learned using fastText BIBREF14 and then are aligned into a shared space with English BIBREF15, BIBREF16. Unlike learning contextualized representations, learning word vectors is fast and computationally cheap. Given the aligned vectors $\bar{}_f$ of foreign and $\bar{}_e$ of English, we calculate the word translation matrix $\in ^{|V_f|\times |V_e|}$ as

Here, we use $\mathrm {sparsemax}$ BIBREF17 instead of softmax. Sparsemax is
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-0ce173cb54d76e7269957c1ed256e721cdc47b8cd57ae0d4d55f1ad6ef2847bd

Passage ID: `qasper-passage-v1-0ce173cb54d76e7269957c1ed256e721cdc47b8cd57ae0d4d55f1ad6ef2847bd`; retrieval score: 5.810103620521632.

Word count: 100.

```text
Table TABREF32 shows the XNLI test accuracy. For reference, we also include the scores from the previous work, notably the state-of-the-art system XLM BIBREF6. Before discussing the results, we spell out that the fairest comparison in this experiment is the comparison between mBERT and RAMEN$_{\textsc {base}}$+BERT trained with monolingual only.

We first discuss the transfer results from BERT. Initialized from fastText vectors, RAMEN$_{\textsc {base}}$ slightly outperforms mBERT by 1.9 points on average and widen the gap of 3.3 points on Arabic. RAMEN$_{\textsc {base}}$ gains extra 0.8 points on average when initialized from parallel data. With triple number of parameters, RAMEN$_{\textsc
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-7f2ea21ce55ef8120b57d948bbf1053eeb24b920914331f3b5b6c344b687002d

Passage ID: `qasper-passage-v1-7f2ea21ce55ef8120b57d948bbf1053eeb24b920914331f3b5b6c344b687002d`; retrieval score: 5.641872727550876.

Word count: 100.

```text
Pre-trained models BIBREF0, BIBREF1 have received much of attention recently thanks to their impressive results in many down stream NLP tasks. Additionally, multilingual pre-trained models enable many NLP applications for other languages via zero-short cross-lingual transfer. Zero-shot cross-lingual transfer has shown promising results for rapidly building applications for low resource languages. BIBREF2 show the potential of multilingual-BERT BIBREF0 in zero-shot transfer for a large number of languages from different language families on five NLP tasks, namely, natural language inference, document classification, named entity recognition, part-of-speech tagging, and dependency parsing.

Although multilingual models are an important ingredient for enhancing language technology
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 500.

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

#### Rank 1: qasper-passage-v1-7f6b57283ac6bfb75c4d31ecb3faee40c094ed041996b11856f31fae27c113af

Passage ID: `qasper-passage-v1-7f6b57283ac6bfb75c4d31ecb3faee40c094ed041996b11856f31fae27c113af`; retrieval score: 7.933369954610745.

Word count: 100.

```text
phonetic variability in ultrasound tongue images. Much of the previous work in this area has focused on speaker-dependent models. In this work we investigate how automatic processing of ultrasound tongue imaging is affected by speaker variation, and how severe degradations in performance can be avoided when applying systems to data from previously unseen speakers through the use of speaker adaptation and speaker normalization approaches.

Below, we present the main challenges associated with the automatic processing of ultrasound data, together with a review of speaker-independent models applied to UTI. Following this, we present the experiments that we have performed (Section SECREF2
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-fce370022af6ae66b661cfbc69d467482d6ddb97a803a8425207bbeba71d39b2

Passage ID: `qasper-passage-v1-fce370022af6ae66b661cfbc69d467482d6ddb97a803a8425207bbeba71d39b2`; retrieval score: 6.7945146825964065.

Word count: 100.

```text
We use the Ultrax Typically Developing dataset (UXTD) from the publicly available UltraSuite repository BIBREF19 . This dataset contains synchronized acoustic and ultrasound data from 58 typically developing children, aged 5-12 years old (31 female, 27 male). The data was aligned at the phone-level, according to the methods described in BIBREF19 , BIBREF25 . For this work, we discarded the acoustic data and focused only on the B-Mode ultrasound images capturing a midsaggital view of the tongue. The data was recorded using an Ultrasonix SonixRP machine using Articulate Assistant Advanced (AAA) software at INLINEFORM0 121fps with a 135 field of
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1907.01413:3:0` | partial | 0:650 |

#### Rank 3: qasper-passage-v1-b37a864a5e96c82ba14be7f344d4b8090c1bb9db516f754abce51e21ae5e9a78

Passage ID: `qasper-passage-v1-b37a864a5e96c82ba14be7f344d4b8090c1bb9db516f754abce51e21ae5e9a78`; retrieval score: 6.423466228397993.

Word count: 100.

```text
One task that could assist SLTs is the automatic classification of tongue shapes from raw ultrasound. This can facilitate the diagnosis and treatment of speech sound disorders, by allowing SLTs to automatically identify incorrect articulations, or by quantifying patient progress in therapy. In addition to being directly useful for speech therapy, the classification of tongue shapes enables further understanding of phonetic variability in ultrasound tongue images. Much of the previous work in this area has focused on speaker-dependent models. In this work we investigate how automatic processing of ultrasound tongue imaging is affected by speaker variation, and how severe degradations
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-2c780f89e3d7d1153c638d416199897c2366520bf751568b5898ad5434f34a9f

Passage ID: `qasper-passage-v1-2c780f89e3d7d1153c638d416199897c2366520bf751568b5898ad5434f34a9f`; retrieval score: 4.928725858912982.

Word count: 51.

```text
units. The fully-connected layers use dropout with a drop probability of 0.2. Because CNN systems take longer to converge, they are optimized over 200 epochs. For all systems, at the end of every epoch, the model is evaluated on the development set, and the best model across all epochs is kept.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-4f90a13f5060327d19621318157b1c020b7317509e6b7ecc5e97143b052155f6

Passage ID: `qasper-passage-v1-4f90a13f5060327d19621318157b1c020b7317509e6b7ecc5e97143b052155f6`; retrieval score: 4.883178942387899.

Word count: 100.

```text
In this paper, we have investigated speaker-independent models for the classification of phonetic segments from raw ultrasound data. We have shown that the performance of the models heavily degrades when evaluated on data from unseen speakers. This is a result of the variability in ultrasound images, mostly due to differences across speakers, but also due to shifts in probe placement. Using the mean of all ultrasound frames for a new speaker improves the generalization of the models to unseen data, especially when using convolutional neural networks. We have also shown that adapting a pre-trained speaker-independent system using as few as
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 451.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "2cc03c335d671b820b4f04b30bbdd522332ff8ec": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1907.01413:3:0": [
        [
          650,
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

#### Rank 1: qasper-passage-v1-6fffc08f7afe8654173d620980640b4f60d564490be3fa04ac36576499df9aa4

Passage ID: `qasper-passage-v1-6fffc08f7afe8654173d620980640b4f60d564490be3fa04ac36576499df9aa4`; retrieval score: 8.287319110324619.

Word count: 90.

```text
In our experiments we aim to answer the following research questions (RQs):

RQ1: How does the number of training iterations in the BERT language model finetuning stage influence the ATSC end-task performance? At what point does performance start to improve, when does it converge?

RQ2: When trained in-domain, what ATSC end-task performance can be reached through fully exploitet finetuning of the BERT language model?

RQ3: When trained cross-domain in the special case of domain adaptation, what ATSC end-task performance can be reached if BERT language model finetuning is fully exploitet?
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-72b7c9942caa13ea5f8bf38793afe9e29b649a2c6267edd8902e0ef417f2be0b

Passage ID: `qasper-passage-v1-72b7c9942caa13ea5f8bf38793afe9e29b649a2c6267edd8902e0ef417f2be0b`; retrieval score: 3.995362307141965.

Word count: 100.

```text
The results of our experiments are shown in fig:acc-dep-lmiterations and tab:results respectively.

To answer RQ1, which is concerned with details on domain-specific language model finetuning, we can see in fig:acc-dep-lmiterations that first of all, language model finetuning has a substantial effect on ATSC end-task performance. Secondly, we see that in the laptops domain the performance starts to increase at about 10 Mio. finetuned sentences. This is an interesting insight as one would expect a relation closer to a logarithmic curve. One reason might be that it takes many steps to train knowledge into the BERT language model due to its
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-ea2bc7ea38813ebe67c9e326332603fba4de74bc46faa09f43e3c33e09c749d5

Passage ID: `qasper-passage-v1-ea2bc7ea38813ebe67c9e326332603fba4de74bc46faa09f43e3c33e09c749d5`; retrieval score: 3.432424071564719.

Word count: 100.

```text
In addition, we find that different runs have a high variance, the standard deviation amounts to about $1\%$ in accuracy, which justifies averaging over 9 runs to measure differences in model performance reliably.

To answer RQ2, which is concerned with in-domain ATSC performance, we see in tab:results that for the in-domain training case, our models BERT-ADA Lapt and BERT-ADA Rest achieve performance close to state-of-the-art on the laptops dataset and new state-of-the-art on the restaurants dataset with accuracies of $79.19\%$ and $87.14\%$, respectively. On the restaurants dataset, this corresponds to an absolute improvement of $2.2\%$ compared to the previous state-of-the-art
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.11860:19:2` | partial | 0:473 |

#### Rank 4: qasper-passage-v1-9f3de949f8e29ad30c1ec6189a5034a16ffc2547ecdfdcab438b5022f85c1068

Passage ID: `qasper-passage-v1-9f3de949f8e29ad30c1ec6189a5034a16ffc2547ecdfdcab438b5022f85c1068`; retrieval score: 3.427622034409409.

Word count: 58.

```text
could probably bring significant performance improvements. Another interesting direction for future work would be to investigate cross-domain behavior for an additional domain like hotels, which is more similar to the restaurants domain. Here, it could be interesting to find out if the shared nature of these domain would results in more confusion or if they would behave synergetically.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-5f166610351e443dc830cdc238f28f56841ac7794b4e9f98689d5023a34b384b

Passage ID: `qasper-passage-v1-5f166610351e443dc830cdc238f28f56841ac7794b4e9f98689d5023a34b384b`; retrieval score: 3.420290800350354.

Word count: 100.

```text
We compare in-domain results to current state of the art methods, which we will now describe briefly.

SDGCN-BERT BIBREF11 explicitly models sentiment dependencies for sentences with multiple aspects with a graph convolutional network. This method is current state-of-the-art on the SemEval 2014 laptops dataset.

AEN-BERT BIBREF8 is an attentional encoder network. When used on top of BERT embeddings this method performs especially well on the laptops dataset.

BERT-SPC BIBREF8 is BERT used in sentence-pair classification mode. This is exactly the same method as our BERT-base baseline and therefore, we can cross-check the authors results.

BERT-PT BIBREF9 uses multi-task fine-tuning prior
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 448.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "46773036407495e12fc0be2224060db32f6d6676": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1908.11860:19:2": [
        [
          473,
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

#### Rank 1: qasper-passage-v1-8bb871c9f0428f744c076fac41b8f924f354c366cddd485d1e73616e11e5718e

Passage ID: `qasper-passage-v1-8bb871c9f0428f744c076fac41b8f924f354c366cddd485d1e73616e11e5718e`; retrieval score: 6.954947848599677.

Word count: 100.

```text
most previous work on rare words was evaluated on datasets explicitly focusing on such words BIBREF6, BIBREF3, BIBREF4, BIBREF5, BIBREF10, all of these datasets are tailored towards context-independent embeddings and thus not suitable for evaluating our proposed model. Furthermore, understanding rare words is of negligible importance for most commonly used downstream task datasets. To evaluate our proposed model, we therefore introduce a novel procedure that allows us to automatically turn arbitrary text classification datasets into ones where rare words are guaranteed to be important. This is achieved by replacing classification-relevant frequent words with rare synonyms obtained using semantic resources such
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-264aa409af98d3772e715cb8576ec9a2ea98574ba6d601f3819d0442bc9b9a34

Passage ID: `qasper-passage-v1-264aa409af98d3772e715cb8576ec9a2ea98574ba6d601f3819d0442bc9b9a34`; retrieval score: 5.753153578140544.

Word count: 100.

```text
We have introduced Bertram, a novel architecture for relearning high-quality representations of rare words. This is achieved by employing a powerful pretrained language model and deeply connecting surface-form and context information. By replacing important words with rare synonyms, we have created various downstream task datasets focusing on rare words; on all of these datasets, Bertram improves over a BERT model without special handling of rare words, demonstrating the usefulness of our proposed method.

As our analysis has shown that even for the most frequent words considered, using Bertram is still beneficial, future work might further investigate the limits of our
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-e384dfab3219994c3efe1b574c80529a024a56374ef345b4bc74c69b4b2872f8

Passage ID: `qasper-passage-v1-e384dfab3219994c3efe1b574c80529a024a56374ef345b4bc74c69b4b2872f8`; retrieval score: 5.5160972123587015.

Word count: 100.

```text
To measure the effect of adding Bertram to BERT on downstream tasks, we apply the procedure described in Section SECREF4 to a commonly used textual entailment dataset as well as two text classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. For all three datasets, we use BERT$_\text{base}$ as a baseline model and create the substitution dictionary $S$ using the synonym relation of WordNet BIBREF20 and the pattern library BIBREF34 to make sure that all synonyms have consistent parts of speech. As an additional source of word substitutions, we make use of the misspellings dataset of BIBREF25, which is
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1910.07181:11:0` | partial | 0:633 |

#### Rank 4: qasper-passage-v1-a04c6551e776c100fa603912c1e9a867c6256baa66a91c3c729569e7a6413bc3

Passage ID: `qasper-passage-v1-a04c6551e776c100fa603912c1e9a867c6256baa66a91c3c729569e7a6413bc3`; retrieval score: 5.299991945438489.

Word count: 50.

```text
Corpus (WWC) BIBREF33; this of course gives BERT a clear advantage over our proposed method. In order to at least partially compensate for this, in our downstream task experiments we gather the set of contexts $\mathcal {C}$ for a given rare word from both the WWC and BooksCorpus during inference.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-cd89e725d684862a61751efb3b0eadf0000bbd7ebc60d77fff412f9d6e1d80c1

Passage ID: `qasper-passage-v1-cd89e725d684862a61751efb3b0eadf0000bbd7ebc60d77fff412f9d6e1d80c1`; retrieval score: 4.9276408806114675.

Word count: 100.

```text
introduce a novel procedure that allows us to automatically turn arbitrary text classification datasets into ones where rare words are guaranteed to be important. This is achieved by replacing classification-relevant frequent words with rare synonyms obtained using semantic resources such as WordNet BIBREF20.

Using this procedure, we extract rare word datasets from three commonly used text (or text pair) classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. On both the WNLaMPro dataset of BIBREF0 and all three so-obtained datasets, our proposed Bertram model outperforms previous work by a large margin.

In summary, our contributions are as follows:

We
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 450.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "709376b155cf4c245d587fd6177d3ce8b4e23a32": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1910.07181:11:0": [
        [
          633,
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
          633,
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

#### Rank 1: qasper-passage-v1-952b19029ec1f74e81f1129f8c4504c7f5cbc0cbe1da092ecb5e83187681b20b

Passage ID: `qasper-passage-v1-952b19029ec1f74e81f1129f8c4504c7f5cbc0cbe1da092ecb5e83187681b20b`; retrieval score: 7.030296039893324.

Word count: 100.

```text
–, it is unclear whether these models even require special treatment of rare words. However, the listed methods only make use of surface-form information, whereas BIBREF9 found that for covering a wide range of rare words, it is crucial to consider both surface-form and contexts.

Consistently, BIBREF0 recently showed that for BERT BIBREF13, a popular pretrained language model based on a Transformer architecture BIBREF18, performance on a rare word probing task can significantly be improve by relearning representations of rare words using Attentive Mimicking BIBREF19. However, their proposed model is limited in two important respects:

For processing contexts, it uses
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-69004497639e711cf274dde214eb187fb19bfccf415f79cef6f12af9aa2c392f

Passage ID: `qasper-passage-v1-69004497639e711cf274dde214eb187fb19bfccf415f79cef6f12af9aa2c392f`; retrieval score: 6.342789978105629.

Word count: 100.

```text
a Transformer architecture BIBREF18, performance on a rare word probing task can significantly be improve by relearning representations of rare words using Attentive Mimicking BIBREF19. However, their proposed model is limited in two important respects:

For processing contexts, it uses a simple bag-of-words model, throwing away much of the available information.

It combines form and context only in a shallow fashion, thus preventing both input signals from sharing information in any sophisticated manner.

Importantly, this limitation applies not only to their model, but to all previous work on obtaining representations for rare words by leveraging form and context. While using
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-63f515e86a7d135a0fb8d507e5d80c28fd476cebd7ae28525967a8aeb1d94550

Passage ID: `qasper-passage-v1-63f515e86a7d135a0fb8d507e5d80c28fd476cebd7ae28525967a8aeb1d94550`; retrieval score: 6.052258904306952.

Word count: 100.

```text
We evalute Bertram on the WNLaMPro dataset of BIBREF0. This dataset consists of cloze-style phrases like

and the task is to correctly fill the slot (____) with one of several acceptable target words (e.g., “fruit”, “bush” and “berry”), which requires knowledge of the phrase's keyword (“lingonberry” in the above example). As the goal of this dataset is to probe a language model's ability to understand rare words without any task-specific finetuning, BIBREF0 do not provide a training set. Furthermore, the dataset is partitioned into three subsets; this partition is based on the frequency of the keyword, with keywords occurring less
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1910.07181:10:0` | full | 0:104 |

#### Rank 4: qasper-passage-v1-470dfc71056d59e99563999931ecc1d3b37d1bda3944b54f4e5765e80437b0d7

Passage ID: `qasper-passage-v1-470dfc71056d59e99563999931ecc1d3b37d1bda3944b54f4e5765e80437b0d7`; retrieval score: 6.044886044537675.

Word count: 71.

```text
deeper connection of form and context.

We design a procedure that allows us to automatically transform text classification datasets into datasets for which rare words are guaranteed to be important.

We show that Bertram achieves a new state-of-the-art on the WNLaMPro probing task BIBREF0 and beats all baselines on rare word instances of AG's News, MNLI and DBPedia, resulting in an absolute improvement of up to 24% over a BERT baseline.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-f04dc1005cbb748d6260a7b2fa702956843c62a88f0fd43e96bc1409f75691a7

Passage ID: `qasper-passage-v1-f04dc1005cbb748d6260a7b2fa702956843c62a88f0fd43e96bc1409f75691a7`; retrieval score: 4.8846922559643.

Word count: 100.

```text
language model's ability to understand rare words without any task-specific finetuning, BIBREF0 do not provide a training set. Furthermore, the dataset is partitioned into three subsets; this partition is based on the frequency of the keyword, with keywords occurring less than 10 times in the WWC forming the rare subset, those occurring between 10 and 100 times forming the medium subset, and all remaining words forming the frequent subset. As our focus is on improving representations for rare words, we evaluate our model only on the former two sets.

Results on WNLaMPro rare and medium are shown in Table TABREF34,
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 471.

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

#### Rank 1: qasper-passage-v1-57121e3eab48e69320db13fdfaafae20de522d108dd63f3ea346bff4430a8b5c

Passage ID: `qasper-passage-v1-57121e3eab48e69320db13fdfaafae20de522d108dd63f3ea346bff4430a8b5c`; retrieval score: 3.5905299891528215.

Word count: 45.

```text
compared to conditioning on the abstract when using the SciGPT2 model. However, we see that IR methods perform better than the best neural models. We do not find enough evidence to reject the null hypothesis regarding what context from the cited document should be used.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2002.00317:7:3` | partial | 219:489 |

#### Rank 2: qasper-passage-v1-43af1a457a4a55d2f773ba8e9e96e87a36684171603412e13d4c90573f6a744e

Passage ID: `qasper-passage-v1-43af1a457a4a55d2f773ba8e9e96e87a36684171603412e13d4c90573f6a744e`; retrieval score: 2.9457119479482374.

Word count: 100.

```text
The primary question we investigate with this model is what kind of input is best for generating accurate and informative citation sentences. Prior works in citation recommendation have made use of abstracts, which perhaps act as sufficient summaries of document content for this task. Additionally, we explore variants of extended context, such as the introduction or first section after the abstract. Since scientific texts are too long to fit into the context window of our generation model, we also investigate a “sampling” approach which samples sentences from throughout the document until the context window is full. In this work, we
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-8ec1f53c5f169c390a2367e8e6c4cbc0f9d7ff3899acefcfdf6db2db14535a8b

Passage ID: `qasper-passage-v1-8ec1f53c5f169c390a2367e8e6c4cbc0f9d7ff3899acefcfdf6db2db14535a8b`; retrieval score: 2.8584773029166826.

Word count: 100.

```text
We compare the different baseline systems using BLEU BIBREF12, ROUGE (specifically ROUGE 1, 2, and L; BIBREF13), and the recently introduced BertScore BIBREF14, a similarity metric based on BERT embeddings which has been shown to correlate well with human judgements on other tasks. To adapt the BertScore metric to the scientific text domain, we use SciBERT embeddings.

Table TABREF7 (above the double line) shows the performance of the SciGPT2 model on the test set when provided with the different input context combinations outlined in Section SECREF5. We find that context does make a difference for this category of model, and
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-3fc9d6dd07e59b9572a270e02b827d8903b4ea5ae1e390ca48c013af4c1f491a

Passage ID: `qasper-passage-v1-3fc9d6dd07e59b9572a270e02b827d8903b4ea5ae1e390ca48c013af4c1f491a`; retrieval score: 2.8187127481751166.

Word count: 100.

```text
and nuanced relationships between related scientific works.

In this work, we introduce the task of citation text generation. Leveraging the full texts of English-language scientific articles, we construct a dataset of citation sentences in the computer science domain for training and evaluating citation text generation models. We investigate strong retrieval and neural baseline models against which future work can compare. For use cases where large models can be trained, we extend the successful GPT2 architecture BIBREF6 to the scientific domain with additional pre-training and subsequent fine-tuning on the citation generation task. We experiment with different kinds of document context in
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-24c6a418c2ccac9a291772a2425ed80900ea55d0fde1eea270580544ba44ba17

Passage ID: `qasper-passage-v1-24c6a418c2ccac9a291772a2425ed80900ea55d0fde1eea270580544ba44ba17`; retrieval score: 2.6618944560413005.

Word count: 100.

```text
overfitting for this method. Outputs are largely unchanged by this tuning; fewer than 400 test datapoints differ from the untuned outputs. A larger validation split may alleviate this problem.

Statistical significance is assessed for select results using bootstrapping with 1000 samples in each of 100 iterations. This test shows that conditioning on the introduction of the source document improves performance compared to conditioning on the abstract when using the SciGPT2 model. However, we see that IR methods perform better than the best neural models. We do not find enough evidence to reject the null hypothesis regarding what context from the
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2002.00317:7:3` | partial | 0:458 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 445.

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

#### Rank 1: qasper-passage-v1-b525d8655d88d5fce31953be6d2eec596ce1e55112919fb829bd16ccb8d063cd

Passage ID: `qasper-passage-v1-b525d8655d88d5fce31953be6d2eec596ce1e55112919fb829bd16ccb8d063cd`; retrieval score: 9.234891103079951.

Word count: 98.

```text
total positive, negative and neutral emotions in tweets in a 3 day period are calculated successively which are used as features for the classifier model and the output is the labeled next day value of stock 0 or 1.The window size is experimented and best results are achieved when the sentiment values precede 3 days to the stock price. A total of 355 instances, each with 3 attributes are fed to the classifier with a split proportions of 80% train dataset and the remaining dataset for testing. The accuracy of the classifier is discussed in the results section.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-f2a9585e714da557c2ce6c8eb42c9c66e91008e73c075e76a7840aaa172985c7

Passage ID: `qasper-passage-v1-f2a9585e714da557c2ce6c8eb42c9c66e91008e73c075e76a7840aaa172985c7`; retrieval score: 8.71880768454266.

Word count: 100.

```text
The above sections discussed the method followed to train the classifier used for sentiment analysis of tweets. The classifier with features as Word2vec representations of human annotated tweets trained on Random Forest algorithm with a split percentage of 90 for training the model and remaining for testing the model showed an accuracy of 70.2%. With N-gram representations, the classifier model with same algorithm and with same dataset showed an accuracy of 70.5%. Though the results are very close, model trained with word2vec representations is picked to classify the nonhuman annotated tweets because of its promising accuracy for large datasets and
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-014a17b5726de3640f90d4e1c1216d964dff86b496adbb06d7f4b78fa9f93ac6

Passage ID: `qasper-passage-v1-014a17b5726de3640f90d4e1c1216d964dff86b496adbb06d7f4b78fa9f93ac6`; retrieval score: 6.67956740464864.

Word count: 65.

```text
In addition to this, data from news can also be included for an exhaustive public opinion collection.

While training the sentiment analyzer, 3,216 tweets are used which is comparatively a less number to train a sentiment analyzer. In future, we look forward to human annotate more than 10,000 tweets and train the classifiers. With increasing size of training datasets, the models tend to perform better.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-5c94101ae9a68b0cb8d8c523391ca6052b36e85f31ae9f1e9a65897d81917c21

Passage ID: `qasper-passage-v1-5c94101ae9a68b0cb8d8c523391ca6052b36e85f31ae9f1e9a65897d81917c21`; retrieval score: 6.417865658137329.

Word count: 100.

```text
A classifier is presented in the previous sections that is trained with aggregate sentiment values for 3-day period as features and the increase/decrease in stock price represented by 1/0 as the output. Total data is split into two parts, 80 percent to train the model and remaining for testing operations. The classifier results show an accuracy value of 69.01% when trained using Logistic regression algorithm and the accuracy rate varied with the training set. When the model with LibSVM is trained with 90 percent of data, it gave a result of 71.82%. These results give a significant edge to the
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-170056109830af8cda9fa1b51ba645949b77ff0bf9e5d084d96623234479c77e

Passage ID: `qasper-passage-v1-170056109830af8cda9fa1b51ba645949b77ff0bf9e5d084d96623234479c77e`; retrieval score: 5.868929917796063.

Word count: 81.

```text
trained using Logistic regression algorithm and the accuracy rate varied with the training set. When the model with LibSVM is trained with 90 percent of data, it gave a result of 71.82%. These results give a significant edge to the investors and they show good correlation between stock market movements and the sentiments of public expressed in twitter. This trend shows that with increasing dataset the models are performing well. We would like to incorporate more data in our future work.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 444.

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

#### Rank 1: qasper-passage-v1-d720b80f8296a152d5d2fcd4da139bde9bdc00993d8c56749160e455176c73e7

Passage ID: `qasper-passage-v1-d720b80f8296a152d5d2fcd4da139bde9bdc00993d8c56749160e455176c73e7`; retrieval score: 2.6117589528476777.

Word count: 79.

```text
While image and sound come with a natural high dimensional embedding, the issue of which is the best representation is still an open research problem in the context of natural language and text. It is beyond the scope of this paper to do a thorough overview of word representations, for this we refer the interest reader to the excellent review provided by BIBREF1 . Here, we will just introduce the main representations that are related to the proposed method.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-15d6eb7874f9385e11969792cc0a4f06af50d02a5ddbb587804cf77ce303de78

Passage ID: `qasper-passage-v1-15d6eb7874f9385e11969792cc0a4f06af50d02a5ddbb587804cf77ce303de78`; retrieval score: 2.4872131459523565.

Word count: 41.

```text
word representations and a rule based sentiment model in its inputs. We showed that the use of pre-computed word representations allows to reduce over-fitting and to achieve significantly better generalization, while some basic pre-processing was needed to further improve the performance.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-61f11bbcc2f62dc09c3e5b71bf0c933649c14af7598c627c605eed47d5c22f58

Passage ID: `qasper-passage-v1-61f11bbcc2f62dc09c3e5b71bf0c933649c14af7598c627c605eed47d5c22f58`; retrieval score: 1.7534039411829985.

Word count: 100.

```text
In this paper, we presented the network architecture used for the Fortia-FBK submission to the Semeval-2017 Task 5, Subtask 2 challenge, with the goal of predicting positive (bullish) or negative (bearish) attitude towards a target brand from financial news headlines. The proposed system ranked 1st in such challenge.

Our approach is based on 1d convolutions and uses fine-tuning of unsupervised word representations and a rule based sentiment model in its inputs. We showed that the use of pre-computed word representations allows to reduce over-fitting and to achieve significantly better generalization, while some basic pre-processing was needed to further improve the
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-97ab8d7a69ebec45ec6f75adf5688cba2f4812eea560e15b6d50eda2ea5e338a

Passage ID: `qasper-passage-v1-97ab8d7a69ebec45ec6f75adf5688cba2f4812eea560e15b6d50eda2ea5e338a`; retrieval score: 1.2796767109034526.

Word count: 100.

```text
Minimal preprocessing was adopted in our approach: we replaced the target company's name with a fixed word <company> and numbers with <number>. The sentences were then tokenized using spaces as separator and keeping punctuation symbols as separate tokens.

The words are represented as fixed length vectors INLINEFORM0 resulting from the concatenation of GloVe pre-trained embeddings and DepecheMood BIBREF19 lexicon representation. Since we cannot directly concatenate token-based embeddings (provided in GloVe) with the lemma#PoS-based representation available in DepecheMood, we proceeded to re-build the latter in token-based form, applying the exact same methodology albeit with two differences: we started from a larger
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-8fc24a40f8b0b3f62bbc4fac837494508205671996bf0c9f0a59b5ce5756f54e

Passage ID: `qasper-passage-v1-8fc24a40f8b0b3f62bbc4fac837494508205671996bf0c9f0a59b5ce5756f54e`; retrieval score: 0.9861201357717568.

Word count: 76.

```text
BIBREF0 has highlighted the association between news items and market fluctiations; hence, in the financial domain, sentiment analysis can be used as a proxy for bullish (i.e. positive, upwards trend) or bearish (i.e. negative, downwards trend) attitude towards a specific financial actor, allowing to identify and monitor in real-time the sentiment associated with e.g. stocks or brands.

Our contribution leverages pre-trained word embeddings (GloVe, trained on wikipedia+gigaword corpus), the DepecheMood affective lexicon, and convolutional neural networks.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1704.00939:0:3` | full | 0:171 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 396.

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

#### Rank 1: qasper-passage-v1-1113e438a7ab69aa1fd1815fe938b31f70058dce71c18bb514a4f9a74ac197c5

Passage ID: `qasper-passage-v1-1113e438a7ab69aa1fd1815fe938b31f70058dce71c18bb514a4f9a74ac197c5`; retrieval score: 7.951876841340748.

Word count: 100.

```text
improve performance. This is particularly true for source syntax, which can improve the model's representation of the source language.

Recently, there have been a number of proposals for using linearized representations of parses within standard NMT BIBREF7 , BIBREF8 , BIBREF9 . Linearized parses are advantageous because they can inject syntactic information into the models without significant changes to the architecture. However, using linearized parses in a sequence-to-sequence (seq2seq) framework creates some challenges, particularly when using source parses. First, the parsed sequences are significantly longer than standard sentences, since they contain node labels as well as words. Second, these systems
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-2646c110fbf871c7260e354a23794922065e8f692b6d5d27d28e1155224d6480

Passage ID: `qasper-passage-v1-2646c110fbf871c7260e354a23794922065e8f692b6d5d27d28e1155224d6480`; retrieval score: 6.8635392722450765.

Word count: 100.

```text
Neural machine translation (NMT) typically makes use of a recurrent neural network (RNN) -based encoder and decoder, along with an attention mechanism BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 . However, it has been shown that RNNs require some supervision to learn syntax BIBREF4 , BIBREF5 , BIBREF6 . Therefore, explicitly incorporating syntactic information into NMT has the potential to improve performance. This is particularly true for source syntax, which can improve the model's representation of the source language.

Recently, there have been a number of proposals for using linearized representations of parses within standard NMT BIBREF7 , BIBREF8 ,
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-ad8090fb00935068e7741e56f44c117ce2bf56a93238d230cc0989bbd03aa1bd

Passage ID: `qasper-passage-v1-ad8090fb00935068e7741e56f44c117ce2bf56a93238d230cc0989bbd03aa1bd`; retrieval score: 6.272445957880405.

Word count: 100.

```text
We propose a multi-source framework for injecting linearized source parses into NMT. This model consists of two identical RNN encoders with no shared parameters, as well as a standard RNN decoder. For each target sentence, two versions of the source sentence are used: the sequential (standard) version and the linearized parse (lexicalized or unlexicalized). Each of these is encoded simultaneously using the encoders; the encodings are then combined and used as input to the decoder. We combine the source encodings using the hierarchical attention combination proposed by libovicky2017attention. This consists of a separate attention mechanism for each encoder; these are
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-625cb4cd3c301aeea7e04c03965941ce5a6f946b71adbf36be2916c7cdfffa8a

Passage ID: `qasper-passage-v1-625cb4cd3c301aeea7e04c03965941ce5a6f946b71adbf36be2916c7cdfffa8a`; retrieval score: 5.802952802162222.

Word count: 100.

```text
the target side, finding that this improved translation despite requiring longer sequences.

Most similar to our multi-source model is the parallel RNN model proposed by li2017modeling. Like multi-source, the parallel RNN used two encoders, one for words and the other for syntax. However, they combined these representations at the word level, whereas we combine them on the sentence level. Their mixed RNN model is also similar to our parse2seq baseline, although the mixed RNN decoder attended only to words. As the mixed RNN model outperformed the parallel RNN model, we do not attempt to compare our model to parallel RNN.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-95a765a5641903fad1aeb1e9b1afd0ee8356fae1938327272f2c89cb2dad1da2

Passage ID: `qasper-passage-v1-95a765a5641903fad1aeb1e9b1afd0ee8356fae1938327272f2c89cb2dad1da2`; retrieval score: 5.33009496968303.

Word count: 100.

```text
The parse2seq and multi-source systems require parsed source data at inference time. However, the parser may fail on an input sentence. Therefore, we examine how well these systems do when given only unparsed source sentences at test time.

Table TABREF13 displays the results of these experiments. For the parse2seq baseline, we use only sequential (seq) data as input. For the lexicalized and unlexicalized multi-source systems, two options are considered: seq + seq uses identical sequential data as input to both encoders, while seq + null uses null input for the parsed encoder, where every source sentence is “( )”.

The
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 500.

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

#### Rank 1: qasper-passage-v1-016b55fac7ada05997343f38e8c9cab77d890a698074dca28340e6cdf63c490c

Passage ID: `qasper-passage-v1-016b55fac7ada05997343f38e8c9cab77d890a698074dca28340e6cdf63c490c`; retrieval score: 3.241963138737861.

Word count: 94.

```text
reasonable performance on these tasks, and do not suffer from catastrophic performance on any tasks. Its worst result comes on task 6 and one of the reason is probably that this architecture is not designed to predict a list of answers. On the contrary, the deep projective reader achieves encouraging on this dataset. It outperforms all the other baselines, with very good scores on the first fourth tasks. The question/document and document/document attention layers proposed in BIBREF12 seem once again to produce rich encodings of the inputs which are relevant for our projection layer.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-2597abc79e5a214ad68f11b961f801ae4a4aac6f5c973c763644c52f649a9c49

Passage ID: `qasper-passage-v1-2597abc79e5a214ad68f11b961f801ae4a4aac6f5c973c763644c52f649a9c49`; retrieval score: 3.167052880856117.

Word count: 100.

```text
Table TABREF19 displays the performance of the 4 baselines on the ReviewQA's test set. These results are the performance achieved by our own implementation of these 4 models. According to our results, the simple LSTM network and the MemN2N perform very poorly on this dataset. Especially on the most advanced reasoning tasks. Indeed, the task 5 which corresponds to the prediction of the exact rating of an aspect seems to be very challenging for these model. Maybe the tokenization by sentence to create the memory blocks of the MemN2N, which is appropriated in the case of the bAbI tasks, is
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-1f27803e10dba847390b2f94f69acb2a1f051e10c5a4ec6b8d62ad28882f5634

Passage ID: `qasper-passage-v1-1f27803e10dba847390b2f94f69acb2a1f051e10c5a4ec6b8d62ad28882f5634`; retrieval score: 3.087420487128232.

Word count: 100.

```text
model. In this configuration, a text document such as a news article, a document from Wikipedia or any type of text is presented to a machine with an associated set of questions. The system is then expected to answer these questions and evaluated by its accuracy on this task. The machine reading framework is very general and we can imagine a large panel of questions that can possibly handle most of the standard natural language processing tasks. For example, the task of named entities recognition can be formulated as a machine reading one where your document is the sentence and
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-4d2aa07debe8b7c619d6d1b50a96997590c6790ca890b64778a943e32576c3c7

Passage ID: `qasper-passage-v1-4d2aa07debe8b7c619d6d1b50a96997590c6790ca890b64778a943e32576c3c7`; retrieval score: 3.087420487128232.

Word count: 100.

```text
A large majority of the human knowledge is recorded through text documents. That is why ability for a system to automatically infer information from text without any structured data has become a major challenge. Answering questions about a given document is a relevant proxy task that has been proposed as a way to evaluate the reading ability of a given model. In this configuration, a text document such as a news article, a document from Wikipedia or any type of text is presented to a machine with an associated set of questions. The system is then expected to answer these
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-43e140d2428f6d3a973e5789270daeb09c6175b7f69273894d46d6504e88f7a8

Passage ID: `qasper-passage-v1-43e140d2428f6d3a973e5789270daeb09c6175b7f69273894d46d6504e88f7a8`; retrieval score: 2.932690531553895.

Word count: 100.

```text
a large panel of questions that can possibly handle most of the standard natural language processing tasks. For example, the task of named entities recognition can be formulated as a machine reading one where your document is the sentence and the question would be 'What are the named entities mentioned in this sentence?'. These natural language interactions are an important objective for reading systems.

Recently, many datasets have been proposed to build and evaluate reading models BIBREF0 , BIBREF1 . From cloze style questions BIBREF2 to open questions BIBREF3 , from synthetic data BIBREF4 to human written articles BIBREF5 ,
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 494.

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

#### Rank 1: qasper-passage-v1-42ce36a57e3b16705deab34c77660a254546513ac5d2a94314533baf80ed705a

Passage ID: `qasper-passage-v1-42ce36a57e3b16705deab34c77660a254546513ac5d2a94314533baf80ed705a`; retrieval score: 8.432421828384589.

Word count: 100.

```text
doubt that the generated summary of the proposed method is better than the baseline. However, the improvement cannot be properly shown by the existing evaluation methods. Furthermore, the examples suggest that the proposed method does learn better correspondence. The highlighted words in each example in Table TABREF28 share almost the same previous words. However, in the first one, the baseline considers “UTF8gbsn停” (stop) as the most related words, which is a sign of noisy word relations learned from other training examples, while the proposed method generates “UTF8gbsn进站” (to the platform), which is more related to what a human thinks. It
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-0f9ba710c62c621d226d41df52fa9a7a166ecd068eaa9399f0f545beddc42eec

Passage ID: `qasper-passage-v1-0f9ba710c62c621d226d41df52fa9a7a166ecd068eaa9399f0f545beddc42eec`; retrieval score: 7.06050599321406.

Word count: 100.

```text
considers “UTF8gbsn停” (stop) as the most related words, which is a sign of noisy word relations learned from other training examples, while the proposed method generates “UTF8gbsn进站” (to the platform), which is more related to what a human thinks. It is the same with the second example, where a human selects “UTF8gbsn专家” (expert) and Dual-Train selects “UTF8gbsn工作者” (worker), while the baseline selects “UTF8gbsn钻研” (research) and fails to generate a grammatical sentence later. In the third one, the reference and the baseline use the same word, while Dual-Train chooses a word of the same meaning. It can be concluded that Dual-Train
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-a17fb23c9f95097c39ee3403b949fd350a93bc4ce91b0c54d2930e3d88edc5eb

Passage ID: `qasper-passage-v1-a17fb23c9f95097c39ee3403b949fd350a93bc4ce91b0c54d2930e3d88edc5eb`; retrieval score: 6.886415774797777.

Word count: 95.

```text
results show that the proposed method can improve the semantic consistency by 4% in terms of human evaluation. As shown by the analysis, the proposed method achieves the improvements by eliminating the less semantically-related word correspondence. The proposed human evaluation method is effective and efficient in judging the semantic consistency, which is absent in previous work but is crucial in the accurate evaluation of the text summarization systems. The proposed metric is simple to conduct and easy to interpret. It also provides an insight on how practicable the existing systems are in the real-world scenario.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-4cec7dde818a0de1fa028d585c919e7b805565da533aaf7ee1a031699b2211fb

Passage ID: `qasper-passage-v1-4cec7dde818a0de1fa028d585c919e7b805565da533aaf7ee1a031699b2211fb`; retrieval score: 6.266422997892029.

Word count: 100.

```text
proposed method is more consistent with the source content. It also exhibits the necessity of the proposed human evaluation. Because when the generated summary is evaluated against the reference, it may seem redundant or wrong, but it is actually true to the source content. While it is arguable that the generated summary is better than the reference, there is no doubt that the generated summary of the proposed method is better than the baseline. However, the improvement cannot be properly shown by the existing evaluation methods. Furthermore, the examples suggest that the proposed method does learn better correspondence. The highlighted
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-0d26e0fb4382190e48421d46d1002002d7efab2d9d47f032840550e07dd35955

Passage ID: `qasper-passage-v1-0d26e0fb4382190e48421d46d1002002d7efab2d9d47f032840550e07dd35955`; retrieval score: 5.5159005439296855.

Word count: 100.

```text
systematic bias in automatic evaluations, and automatic evaluation for semantically related tasks can only serve as a reference. To avoid the deficiencies, we propose a simple human evaluation method to assess the semantic consistency. Each summary candidate is evaluated against the text rather than the reference. If the candidate is irrelevant or incorrect to the text, or the candidate is not understandable, the candidate is labeled bad. Otherwise, the candidate is labeled good. Then, we can get an accuracy of the good summaries. The proposed evaluation is very simple and straight-forward. It focuses on the relevance between the summary and
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1805.04033:7:0` | partial | 1565:2214 |

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 495.

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
          1565
        ],
        [
          2214,
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

#### Rank 1: qasper-passage-v1-bcabaf57662dc9b663a295976c5943548b7f3f7d4de337cb6a2879c2e6902fad

Passage ID: `qasper-passage-v1-bcabaf57662dc9b663a295976c5943548b7f3f7d4de337cb6a2879c2e6902fad`; retrieval score: 8.178482608291588.

Word count: 100.

```text
in pre-training, while it has to extract semantic and linguistic features additionally in fine-tuning, which significantly increases the learning difficulty.

Non-pre-trained Attention Module: Previous work BIBREF6 trains attention modules for ASR, MT and ST respectively, hence, the attention module of ST does not benefit from the pre-training.

To address these issues, we propose a Tandem Connectionist Encoding Network (TCEN), which is able to reuse all subnets in pre-training, keep the roles of subnets consistent, and pre-train the attention module. Concretely, the TCEN consists of three components, a speech encoder, a text encoder, and a target text decoder. Different from the
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-f000a75e8792e39e79507f0334392552b6a3600b74c739975459573100cadadc

Passage ID: `qasper-passage-v1-f000a75e8792e39e79507f0334392552b6a3600b74c739975459573100cadadc`; retrieval score: 7.561633063776997.

Word count: 100.

```text
Subnet Waste: The ST system just reuses the ASR encoder and the MT decoder, while discards other pre-trained subnets, such as the MT encoder. Consequently, valuable semantic information captured by the MT encoder cannot be inherited by the final ST system.

Role Mismatch: The speech encoder plays different roles in pre-training and fine-tuning. The encoder is a pure acoustic model in pre-training, while it has to extract semantic and linguistic features additionally in fine-tuning, which significantly increases the learning difficulty.

Non-pre-trained Attention Module: Previous work BIBREF6 trains attention modules for ASR, MT and ST respectively, hence, the attention module of
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-b79be9065c9ea54224705c18986665b67ff5ec6e4898788f90adcfbd4cdfeb94

Passage ID: `qasper-passage-v1-b79be9065c9ea54224705c18986665b67ff5ec6e4898788f90adcfbd4cdfeb94`; retrieval score: 6.228100766010522.

Word count: 100.

```text
MT and ST tasks; and 3) many-to-many setting where both the encoder and decoder are shared.

A many-to-many multi-task model contains two encoders as well as two decoders. It can be jointly trained on ASR, MT, and ST tasks. As the attention module is task-specific, three attentions are defined.

Usually, the size of $\mathcal {A}$ and $\mathcal {M}$ is much larger than $\mathcal {S}$. Therefore, the common training practice is to pre-train the model on ASR and MT tasks and then fine-tune it with a multi-task learning manner. However, as aforementioned, this method suffers from subnet waste, role mismatch and
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-d22bc534b9178cead454e932d9c755872eb84845040c415504d3ca3e6f612e18

Passage ID: `qasper-passage-v1-d22bc534b9178cead454e932d9c755872eb84845040c415504d3ca3e6f612e18`; retrieval score: 6.083647394927256.

Word count: 100.

```text
and fine-tuning. Moreover, we reuse the pre-trained MT attention module in ST, so we can leverage the alignment information learned in pre-training.

Since the text encoder consumes word embeddings of plausible texts in MT task but uses speech encoder outputs in ST task, another question is how one guarantees the speech encoder outputs are consistent with the word embeddings. We further modify our model to achieve semantic consistency and length consistency. Specifically, (1) the projection matrix at the CTC classification layer for ASR is shared with the word embedding matrix, ensuring that they are mapped to the same latent space,
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-b7b1d65fc1707301c6e1226607ec0c8d89d68f8874bbed3d74062a9d073024e7

Passage ID: `qasper-passage-v1-b7b1d65fc1707301c6e1226607ec0c8d89d68f8874bbed3d74062a9d073024e7`; retrieval score: 6.067412621378134.

Word count: 100.

```text
is able to reuse all subnets in pre-training, keep the roles of subnets consistent, and pre-train the attention module. Concretely, the TCEN consists of three components, a speech encoder, a text encoder, and a target text decoder. Different from the previous work that pre-trains an encoder-decoder based ASR model, we only pre-train an ASR encoder by optimizing the Connectionist Temporal Classification (CTC) BIBREF8 objective function. In this way, the additional decoder of ASR is not required while keeping the ability to read acoustic features into the source language space by the speech encoder. Besides, the text encoder and decoder can
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 500.

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

#### Rank 1: qasper-passage-v1-593a996e9328b6cce2f19636b9e3cc6db01ccb87deae614d2206fe6759b96a9c

Passage ID: `qasper-passage-v1-593a996e9328b6cce2f19636b9e3cc6db01ccb87deae614d2206fe6759b96a9c`; retrieval score: 11.048757905720365.

Word count: 100.

```text
This paper has used data-driven language mapping to select national dialects of English to be included in a global dialect identification model. The main experiments have focused on a dynamic syntactic feature set, showing that it is possible to predict dialect membership within-domain with only a small loss of performance against lexical models. This work raises two remaining problems:

First, we know that location-specific content (i.e., place names, place references, national events) can be used for geo-location and text-based models of place. To what degree does a lexical approach capture linguistic variation (i.e., “pop" vs. “soda") and to what degree
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.05527:9:0` | full | 0:389 |

#### Rank 2: qasper-passage-v1-780a0bd02dc92b093c8b718c91c140f2d0142b907d2a2efe25d406c0b9583021

Passage ID: `qasper-passage-v1-780a0bd02dc92b093c8b718c91c140f2d0142b907d2a2efe25d406c0b9583021`; retrieval score: 8.251397894464567.

Word count: 100.

```text
we know that location-specific content (i.e., place names, place references, national events) can be used for geo-location and text-based models of place. To what degree does a lexical approach capture linguistic variation (i.e., “pop" vs. “soda") and to what degree is it capturing non-linguistic information (i.e., “Melbourne" vs. “London")? This is an essential problem for dialect identification models. A purely syntactic model does not perform as well as a lexical model, but it does come with more guarantees.

Second, we have seen that inner-circle varieties have higher feature densities given the grammars used here. This implies that there are syntactic
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-b1d7ce44643cd723de86eb201724ca9ab09b901395673d199d46cda8b7212d2b

Passage ID: `qasper-passage-v1-b1d7ce44643cd723de86eb201724ca9ab09b901395673d199d46cda8b7212d2b`; retrieval score: 7.757689061716553.

Word count: 100.

```text
the grammar: how much does a single generic grammar of English vary across dialects? To what degree does it represent a single dominant dialect?

Finally, a corpus-based approach to variation is restricted to the specific domains or registers that are present in the corpus. To what degree is such a model of variation limited to a specific register? This paper uses both web-crawled corpora and social media corpora to explore the robustness of dialect models across domains (Section 8). Along these same lines, how robust is a model of syntactic variation to the presence of a few highly predictive features?
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-0b7329fe6f4e57869f4805aa8c0ca5c69fe4ecb88eeca5471232f1874109fe44

Passage ID: `qasper-passage-v1-0b7329fe6f4e57869f4805aa8c0ca5c69fe4ecb88eeca5471232f1874109fe44`; retrieval score: 6.102228564185568.

Word count: 100.

```text
0.55. This is not surprising because function words in English do not represent syntactic structures directly; they are instead markers of the types of structures being used. CxG-1 comes next with F1s of 0.80 and 0.76, a significant improvement over the function-word baseline but not approaching unigrams. Note that the experiments using this same grammar in previous work (Dunn, 2018c) were applied to samples of 2k words each. Finally, CxG-2 performs the best, with F1s of 0.96 and 0.92, falling behind unigrams but rivaling bigrams and surpassing trigrams. Because of this, the more detailed experiments below focus only on the
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-6f0c8c469c891f8e222511c99842177798124184c79991500deb3f4d7586c90c

Passage ID: `qasper-passage-v1-6f0c8c469c891f8e222511c99842177798124184c79991500deb3f4d7586c90c`; retrieval score: 6.008448465195343.

Word count: 100.

```text
based on place-specific content, and those based on dialectal variation? That is a question for future work. For example, is it possible to identify and remove location-specific content terms? Here we focus instead on using syntactic representations that are not subject to such interference.

Within syntactic features, function words perform the worst on both datasets with F1s of 0.65 and 0.55. This is not surprising because function words in English do not represent syntactic structures directly; they are instead markers of the types of structures being used. CxG-1 comes next with F1s of 0.80 and 0.76, a significant improvement over
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 500.

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

#### Rank 1: qasper-passage-v1-e8ab9f6342d0bdc645eaaf7a241b6a960a543459bc3faec1b217cf32006ac2e3

Passage ID: `qasper-passage-v1-e8ab9f6342d0bdc645eaaf7a241b6a960a543459bc3faec1b217cf32006ac2e3`; retrieval score: 10.78273050205771.

Word count: 100.

```text
observable. This raises concerns, since models may find answers simply through shallow pattern matching; e.g., syntactic similarity between the words in questions and documents. As pointed out by BIBREF5, for questions starting with when, models tend to predict the only date/time answer in the supporting document. Such behavior limits the generality and usefulness of MRC models, and suggests that they do not learn a proper `understanding' of the intended task. In this paper, to address this problem, we shift the focus of MRC data away from `spoon-feeding' models with sufficient information in fully observable, static documents. Instead, we propose interactive
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-ad24afe5b1e6cbdeb943420309cb3d312b2fd6126652739fab1318745ca4e0a5

Passage ID: `qasper-passage-v1-ad24afe5b1e6cbdeb943420309cb3d312b2fd6126652739fab1318745ca4e0a5`; retrieval score: 6.461675877587847.

Word count: 100.

```text
do not learn a proper `understanding' of the intended task. In this paper, to address this problem, we shift the focus of MRC data away from `spoon-feeding' models with sufficient information in fully observable, static documents. Instead, we propose interactive versions of existing MRC tasks, whereby the information needed to answer a question must be gathered sequentially.

The key idea behind our proposed interactive MRC (iMRC) is to restrict the document context that a model observes at one time. Concretely, we split a supporting document into its component sentences and withhold these sentences from the model. Given a question, the
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.10449:0:2` | partial | 0:265 |

#### Rank 3: qasper-passage-v1-6e431f701208e0272af25409cee5725c48da778331d6e8dc00b6bca8251e3a61

Passage ID: `qasper-passage-v1-6e431f701208e0272af25409cee5725c48da778331d6e8dc00b6bca8251e3a61`; retrieval score: 5.998508933309142.

Word count: 100.

```text
interaction; the action space in our setting (especially for the Ctrl+F command as defined in later section) is arguably larger than the tree sampling action space in DocQN.

Closely related to iMRC is work by BIBREF15, in which the authors introduce a collection of synthetic tasks to train and test information-seeking capabilities in neural models. We extend that work by developing a realistic and challenging text-based task.

Broadly speaking, our approach is also linked to the optimal stopping problem in the literature Markov decision processes (MDP) BIBREF16, where at each time-step the agent either continues or stops and accumulates reward.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-67e6e71e2642501bd6a4c5d8716ceb48acffd691cde461a6cec4c9ef8d2c8780

Passage ID: `qasper-passage-v1-67e6e71e2642501bd6a4c5d8716ceb48acffd691cde461a6cec4c9ef8d2c8780`; retrieval score: 5.035562974450368.

Word count: 100.

```text
method. Either component can be replaced straightforwardly with other methods (e.g., to utilize a large-scale pretrained language model).

Our proposed setup and baseline agent presently use only a single word with the query command. However, a host of other options should be considered in future work. For example, multi-word queries with fuzzy matching are more realistic. It would also be interesting for an agent to generate a vector representation of the query in some latent space. This vector could then be compared with precomputed document representations (e.g., in an open domain QA dataset) to determine what text to observe next,
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-538f03ac870e71a547d10aed21489b78b8091cb63deca9c207cc4a7006c744bb

Passage ID: `qasper-passage-v1-538f03ac870e71a547d10aed21489b78b8091cb63deca9c207cc4a7006c744bb`; retrieval score: 4.86251643885928.

Word count: 57.

```text
and they have much less variance across different settings. This supports our hypothesis that information seeking play an important role in solving iMRC tasks, whereas question answering given necessary information is relatively straightforward. This also suggests that an interactive agent that can better navigate to important sentences is very likely to achieve better performance on iMRC tasks.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 457.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "33b2d26d064251c196238b0c3c455b208680f5fc": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1908.10449:0:2": [
        [
          265,
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

#### Rank 1: qasper-passage-v1-43f6e0853805df54c6eb9e335814bb1025c31141988a94368d35af956a3f6fd7

Passage ID: `qasper-passage-v1-43f6e0853805df54c6eb9e335814bb1025c31141988a94368d35af956a3f6fd7`; retrieval score: 5.900095324363107.

Word count: 63.

```text
consistency checking with the integration of different metrics BIBREF15. However, these tools have only been built for text data. The format and all the custom layers have been designed for Natural Language Processing tasks. Porting WebAnno to support speech data seemed a major engineering challenge. That is why it appeared necessary to develop a new and user-friendly tool addressed to the speech community.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-a3f20b6851f3b42f8feaaf2d8ff94c34791791eb15fdacae1bab14a4d8814374

Passage ID: `qasper-passage-v1-a3f20b6851f3b42f8feaaf2d8ff94c34791791eb15fdacae1bab14a4d8814374`; retrieval score: 5.709685307421583.

Word count: 100.

```text
Seshat was intially developped to study the impact of Huntington's Disease BIBREF17 on speech and language production. One hundred and fifty two interviews between a neuropsychologist and a patient with the Huntington's Disease (HD) were recorded between June 2018 and November 2019. The campaign manager created a campaign with multiple tiers to annotate the turn takings and the speech/non speech boundaries of the utterances of the patient. For both tasks, the annotations did not need to cover completely the audio (sparsity property mentioned above). For the Turn-taking annotations, there are 3 pre-defined tiers, each one with a single class ('Patient',
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-2fbba32f0e36578e0204e79dac4dc538c2ffb3c6d1c44f804af5062e6fec3506

Passage ID: `qasper-passage-v1-2fbba32f0e36578e0204e79dac4dc538c2ffb3c6d1c44f804af5062e6fec3506`; retrieval score: 5.573860525494567.

Word count: 100.

```text
create Annotation Campaigns and Annotators user accounts, and assign Annotation Tasks to Annotators.

Users who are assigned a set of Annotation Tasks. Their job is to complete the annotation of the audio files with the Praat software.

If the TextGrid file they submit does not comply with their Annotation Task's TextGrid Checking Scheme, Seshat pinpoint their annotation errors with detailed messages. The annotator can re-submit the concerned file to the platform based on these different feedbacks.

Once they they connected to their instance of Seshat, campaign managers can access ongoing annotation campaigns or create new ones. Campaign managers are able
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-268ab8254e25ef5962b98aa60068702059f6d37cfc71dc3be2d953a9ebb59978

Passage ID: `qasper-passage-v1-268ab8254e25ef5962b98aa60068702059f6d37cfc71dc3be2d953a9ebb59978`; retrieval score: 5.457677561162567.

Word count: 100.

```text
boundaries of the utterances of the patient. For both tasks, the annotations did not need to cover completely the audio (sparsity property mentioned above). For the Turn-taking annotations, there are 3 pre-defined tiers, each one with a single class ('Patient', 'Non-Patient', and 'Noise'), which results in possible overlap between these classes. For the Utterance annotations, there is only one pre-defined class ('Utterance').

To this date, a total of 67 files have been fully annotated with the help of Seshat by a cohort of 18 speech pathologist students (see Figure FIGREF33). Among these, 16 have been done by 2 different annotators
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-1e6bfaf5ada727c0c5aec2a573d57aaff8834b8775d9068bce3892ea11c24005

Passage ID: `qasper-passage-v1-1e6bfaf5ada727c0c5aec2a573d57aaff8834b8775d9068bce3892ea11c24005`; retrieval score: 5.0044213759054434.

Word count: 100.

```text
messages. The annotator can re-submit the concerned file to the platform based on these different feedbacks.

Once they they connected to their instance of Seshat, campaign managers can access ongoing annotation campaigns or create new ones. Campaign managers are able to add annotators, assign annotation tasks and track progress. Annotator see a list of assigned tasks. The first step for them is to download the sound file with its corresponding auto-generated template TextGrid. In the current implementation, the annotation work has to be done locally with Praat. An upcoming version will use of web tools like Praat on the web
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 463.

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

#### Rank 1: qasper-passage-v1-3c48bb5331cb971837164426f3c630e25fcf856c487fecf91694b4d6b7ca7b98

Passage ID: `qasper-passage-v1-3c48bb5331cb971837164426f3c630e25fcf856c487fecf91694b4d6b7ca7b98`; retrieval score: 9.868590751018433.

Word count: 100.

```text
model for state tracking in slot-filling dialogs" . In our experiments, the variance is estimated using standard dataset reshuffling. The same results are obtained for several state of the art methods of generative and discriminative state tracking on this dataset using the publicly available results as reported in BIBREF22 . More precisely, as provided by the state-of-the-art approaches, the accuracy scores computes $p(s^*_{t+1}|s_t,z_t)$ commonly name the joint goal. Our proposition is compared to the 4 baseline trackers provided by the DSTC organisers. They are the baseline tracker (Baseline), the focus tracker (Focus), the HWU tracker (HWU) and the HWU tracker
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1606.05286:9:0` | partial | 381:1053 |

#### Rank 2: qasper-passage-v1-511244885ebff0f549df5d5d0857f2df37948ab5eef71f133ca9976a912fd221

Passage ID: `qasper-passage-v1-511244885ebff0f549df5d5d0857f2df37948ab5eef71f133ca9976a912fd221`; retrieval score: 8.969580674827933.

Word count: 100.

```text
to address this general problem of dialog system. Our method gives encouraging results in comparison to the state of the art dataset and also does not required complex inference at test time because, as detailed in Section "Spectral decomposition model for state tracking in slot-filling dialogs" , the tracking algorithm hold a linear complexity w.r.t the sum of realization of each considered variables defining the state to track which is what we believe is one of the main advantage of this method. Secondly collective matrix factorization paradigm also for data fusion and bias by data type of modeling as successfully
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-22171bd4c39b75e152313c5bb12bdc12dc1eaf1a7484dbaa12200b1dcbf33585

Passage ID: `qasper-passage-v1-22171bd4c39b75e152313c5bb12bdc12dc1eaf1a7484dbaa12200b1dcbf33585`; retrieval score: 8.46905366354157.

Word count: 56.

```text
In the next section, we present a decompositional approach of dialog state tracking that aims at reconciling the two main approaches of the state of the art while leveraging on the current advances of low-rank bilinear decomposition models, as recalled in BIBREF16 , that seems particularly adapted to the sparse nature of dialog state tracking tasks.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-c51ab31ebd08516eb6c08e6fbec6342706a848cf87529f0194484ee2e2a72de5

Passage ID: `qasper-passage-v1-c51ab31ebd08516eb6c08e6fbec6342706a848cf87529f0194484ee2e2a72de5`; retrieval score: 8.161326171543532.

Word count: 100.

```text
variables to address scalability issues and uses a conditional random field to track each variable separately. Finally, deep neural models, performing on a sliding window of features extracted from previous user turns, have also been proposed in BIBREF15 . Of the current literature, this family of approaches have proven to be the most efficient for publicly available state tracking datasets. In the next section, we present a decompositional approach of dialog state tracking that aims at reconciling the two main approaches of the state of the art while leveraging on the current advances of low-rank bilinear decomposition models, as recalled
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-de6974f110d39e683f92fa8184aac12fdfb89fc30f1928f58989267bfc68e9b7

Passage ID: `qasper-passage-v1-de6974f110d39e683f92fa8184aac12fdfb89fc30f1928f58989267bfc68e9b7`; retrieval score: 7.9957920670297336.

Word count: 49.

```text
each considered variables defining the state to track which is what we believe is one of the main advantage of this method. Secondly collective matrix factorization paradigm also for data fusion and bias by data type of modeling as successfully performed in matrix factorization based recommender systems BIBREF30 .
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 405.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "0f1c509049f53c831e6715cbbe308ae4340e1b37": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1606.05286:9:0": [
        [
          0,
          381
        ],
        [
          1053,
          1317
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-03b92f83687b5357a172491f73621511c902d2527290033580e27ba707babc8a

Passage ID: `qasper-passage-v1-03b92f83687b5357a172491f73621511c902d2527290033580e27ba707babc8a`; retrieval score: 13.270228756611436.

Word count: 100.

```text
The explosion of available scientific articles in the Biomedical domain has led to the rise of Biomedical Information Extraction (BioIE). BioIE systems aim to extract information from a wide spectrum of articles including medical literature, biological literature, electronic health records, etc. that can be used by clinicians and researchers in the field. Often the outputs of BioIE systems are used to assist in the creation of databases, or to suggest new paths for research. For example, a ranked list of interacting proteins that are extracted from biomedical literature, but are not present in existing databases, can allow researchers to make
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-48b615abdbdfcb43c1fd7b687ec0d804aa0e207f169758dbaccb9bbcf306721b

Passage ID: `qasper-passage-v1-48b615abdbdfcb43c1fd7b687ec0d804aa0e207f169758dbaccb9bbcf306721b`; retrieval score: 6.1908689916129385.

Word count: 100.

```text
to their patients. A database of diseases, treatments and tests is beneficial for doctors consulting in complicated medical cases.

The main problems in BioIE are similar to those in Information Extraction:

This paper discusses, in each section, various methods that have been adopted to solve the listed problems. Each section also highlights the difficulty of Information Extraction tasks in the biomedical domain.

This paper is intended as a primer to Biomedical Information Extraction for current NLP researchers. It aims to highlight the diversity of the various techniques from Information Extraction that have been applied in the Biomedical domain. The state
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-c5696d48eaf3a6e87a9e6d70b44d24e3d6bb51ad83e5e2c059bcf59416e92b32

Passage ID: `qasper-passage-v1-c5696d48eaf3a6e87a9e6d70b44d24e3d6bb51ad83e5e2c059bcf59416e92b32`; retrieval score: 5.829811989751453.

Word count: 58.

```text
biomedical domain.

This paper is intended as a primer to Biomedical Information Extraction for current NLP researchers. It aims to highlight the diversity of the various techniques from Information Extraction that have been applied in the Biomedical domain. The state of biomedical text mining is reviewed regularly. For more extensive surveys, consult BIBREF0 , BIBREF1 , BIBREF2 .
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-a8b5194e5233bd68d5b233bcc8bef2f1819442c0629bf78e1af23a364d224664

Passage ID: `qasper-passage-v1-a8b5194e5233bd68d5b233bcc8bef2f1819442c0629bf78e1af23a364d224664`; retrieval score: 4.953113431306774.

Word count: 100.

```text
Named Entity Recognition (NER) in the Biomedical domain usually includes recognition of entities such as proteins, genes, diseases, treatments, drugs, etc. Fact extraction involves extraction of Named Entities from a corpus, usually given a certain ontology. When compared to NER in the domain of general text, the biomedical domain has some characteristic challenges:

Some of the earliest systems were heavily dependent on hand-crafted features. The method proposed in BIBREF4 for recognition of protein names in text does not require any prepared dictionary. The work gives examples of diversity in protein names and lists multiple rules depending on simple word features
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-2a0163332457f76d7b31ab113e22e9a0257ecc4e23c22c4d0d8ab43530b958cb

Passage ID: `qasper-passage-v1-2a0163332457f76d7b31ab113e22e9a0257ecc4e23c22c4d0d8ab43530b958cb`; retrieval score: 4.728894008314902.

Word count: 100.

```text
They note that the F-score achieved are much lesser than that achieved in the general domain in BIBREF24 , and attribute to generally poorer performance of NER tools in the biomedical domain, as well as less training examples. BIBREF25 explore distant supervision methods for protein-protein interaction extraction.

More recently, deep learning methods have been applied to relation extraction in the biomedical domain. One of the main advantages of such methods over traditional feature or kernel based learning methods is that they require minimal feature engineering. In BIBREF26 , skip-gram vectors BIBREF27 are trained over 5.6Gb of unlabelled text. They use
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 458.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "482b34cc6d8ca0cec7ba3e21662c46863c31bd6d": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1705.05437:1:2": [
        [
          0,
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

#### Rank 1: qasper-passage-v1-90e6b98d083dea913b2ea53d167fc37d21d3558dd1b34fc6c7c55a892b3337c4

Passage ID: `qasper-passage-v1-90e6b98d083dea913b2ea53d167fc37d21d3558dd1b34fc6c7c55a892b3337c4`; retrieval score: 8.044939115350738.

Word count: 100.

```text
applications since they are optimized to perform in an artificial setting. In this paper, we show that yes/no questions have the benefit of being very challenging even when they are gathered from natural sources.

Natural language inference is also a well studied area of research, particularly on the MultiNLI BIBREF21 and SNLI BIBREF22 datasets. Other sources of entailment data include the PASCAL RTE challenges BIBREF23 , BIBREF24 or SciTail BIBREF25 . We note that, although SciTail, RTE-6 and RTE-7 did not use crowd workers to generate candidate statements, they still use sources (multiple choices questions or document summaries) that were
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-59fa357807a320aa42b4cd156d6915e447a1fd376feac07caacaa67b9870dd2b

Passage ID: `qasper-passage-v1-59fa357807a320aa42b4cd156d6915e447a1fd376feac07caacaa67b9870dd2b`; retrieval score: 5.46431076566005.

Word count: 100.

```text
statements did not improve transfer from MultiNLI, which supports this hypothesis.

The success of MultiNLI might also be surprising given recent concerns about the generalization abilities of models trained on it BIBREF37 , particularly related to “annotation artifacts" caused by using crowd workers to write the hypothesis statements BIBREF0 . We have shown that, despite these weaknesses, it can still be an important starting point for models being used on natural data.

We hypothesize that a key advantage of MultiNLI is that it contains examples of contradictions. The other sources of transfer we consider, including the next-sentence-selection objective in BERT,
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-7217576fd4221bce82e6bcc906e57592e3047b43f37d6ce6d452be30e0c1d137

Passage ID: `qasper-passage-v1-7217576fd4221bce82e6bcc906e57592e3047b43f37d6ce6d452be30e0c1d137`; retrieval score: 5.218674251314765.

Word count: 82.

```text
trained on next-sentence-selection and masked language modelling on the Book Corpus and Wikipedia.

We fine-tune the BERTL and the OpenAI GPT models using the optimizers recommended by the authors, but found it important to tune the optimization parameters to achieve the best results. We use a batch size of 24, learning rate of 1e-5, and 5 training epochs for BERT and a learning rate of 6.25e-5, batch size of 6, language model loss of 0.5, and 3 training epochs for OpenAI GPT.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-e6dff3a4599d3b82cbf3c85f2211cfb57172d2e3396084dcb77f4025608b1363

Passage ID: `qasper-passage-v1-e6dff3a4599d3b82cbf3c85f2211cfb57172d2e3396084dcb77f4025608b1363`; retrieval score: 5.063264517403124.

Word count: 100.

```text
sufficient to just transfer from powerful pre-trained language models such as BERT BIBREF8 or ELMo BIBREF9 . We experiment with state-of-the-art unsupervised approaches, using existing entailment datasets, three methods of leveraging extractive QA data, and using a few other supervised datasets.

We found that transferring from MultiNLI, and the unsupervised pre-training in BERT, gave us the best results. Notably, we found these approaches are surprisingly complementary and can be combined to achieve a large gain in performance. Overall, our best model reaches 80.43% accuracy, compared to 62.31% for the majority baseline and 90% human accuracy. In light of the fact
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-c37646d9dac02c0724b47758eaf36caec4f68eae97a3a2968d8228d5deb9b1f8

Passage ID: `qasper-passage-v1-c37646d9dac02c0724b47758eaf36caec4f68eae97a3a2968d8228d5deb9b1f8`; retrieval score: 5.058852285374399.

Word count: 100.

```text
QA datasets that require advanced reasoning abilities BIBREF5 , BIBREF17 , BIBREF18 , BIBREF19 , BIBREF20 . However, these attempts typically involve engineering data to be more difficult by, for example, explicitly prompting users to write multi-step questions BIBREF5 , BIBREF18 , or filtering out easy questions BIBREF19 . This risks resulting in models that do not have obvious end-use applications since they are optimized to perform in an artificial setting. In this paper, we show that yes/no questions have the benefit of being very challenging even when they are gathered from natural sources.

Natural language inference is also a
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 482.

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

#### Rank 1: qasper-passage-v1-0b24cdf7f62e9705e4e825d7bebca03132ffec0a8cb3ca57a31af1d83fe564b4

Passage ID: `qasper-passage-v1-0b24cdf7f62e9705e4e825d7bebca03132ffec0a8cb3ca57a31af1d83fe564b4`; retrieval score: 3.853465481228186.

Word count: 100.

```text
Work on representation learning is concerned with finding an appropriate representation of data in order to perform a machine learning task BIBREF33. In particular, deep learning exploits this concept by its very nature BIBREF2. Work on representation learning include Predictive State Representations (PSR) BIBREF34, BIBREF35, which capture the state as a vector of predictions of future outcomes, and a Heuristic Embedding of Markov Processes (HEMP) BIBREF36, which learns to embed transition probabilities using an energy-based optimization problem.

There has been extensive work attempting to use natural language in RL. Efforts that integrate language in RL develop tools, approaches, and insights
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-690ed4daeadb546de4911465bc0a788886f8842194f9ed8d1f08034a9cfcaffe

Passage ID: `qasper-passage-v1-690ed4daeadb546de4911465bc0a788886f8842194f9ed8d1f08034a9cfcaffe`; retrieval score: 3.129809634543883.

Word count: 100.

```text
due to extensive discretization of patches, we've conducted experiments increasing the number of horizontal patches - ranging from 3 to 31 patches in the extreme case. Our results, as depicted in fig: patch count, indicate that the amount of discretization of patches did not affect the performance of the NLP agent, remaining a superior representation compared to the rest.

To conclude, our experiments suggest that NLP representations, though they describe the same raw information of the semantic segmentation maps, are more robust to task-nuisances, allow for better transfer, and achieve higher performance in complex tasks, even when their description is
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-50448ca751d3e51882e2357a785d15dc8d8b7d0958dc088b59bc86ddc17adbad

Passage ID: `qasper-passage-v1-50448ca751d3e51882e2357a785d15dc8d8b7d0958dc088b59bc86ddc17adbad`; retrieval score: 2.3530156899564805.

Word count: 82.

```text
conclude, our experiments suggest that NLP representations, though they describe the same raw information of the semantic segmentation maps, are more robust to task-nuisances, allow for better transfer, and achieve higher performance in complex tasks, even when their description is long and convoluted. While we've only presented results for DQN agents, we include plots for a PPO agent in the Appendix, showing similar trends and conclusions. We thus deduce that NLP-based semantic state representations are a preferable choice for training VizDoom agents.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-e8a967b8b4887ea163254f03fc9614e8fed0844f0e3562e12703ac1f05005e6c

Passage ID: `qasper-passage-v1-e8a967b8b4887ea163254f03fc9614e8fed0844f0e3562e12703ac1f05005e6c`; retrieval score: 2.19248010247082.

Word count: 100.

```text
object is close or far can be determined by calculating the distance from it to the player, and using two threshold levels. Object descriptions can be concise or detailed, as needed. We experimented with the following mechanics:

the screen can be divided between patches equally, or by determined ratios. Here, our main guideline was to keep the "front" patch narrow enough so it can be used as "sights".

our initial experiment was with 3 patches, and later we added 2 more patches classified as "outer left" and "outer right". In our experiments we have tested up to 51 patches, referred
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-15189b11e07f7709c6622a1db10d0a17a799ff2f041b186c6fafb66928e6c3a7

Passage ID: `qasper-passage-v1-15189b11e07f7709c6622a1db10d0a17a799ff2f041b186c6fafb66928e6c3a7`; retrieval score: 2.18255305612545.

Word count: 100.

```text
as well as shoot. This scenario combines elements from all of the previous scenarios.

Our agent was implemented using a Convolutional Neural Network as described in Section SECREF4. We converted the parsed state into embedded representations of fixed length. We tested both a DQN and a PPO based agent, and compared the natural language representation to the other representation techniques, namely the raw image, feature vector, and semantic segmentation representations.

In order to effectively compare the performance of the different representation methods, we conducted our experiments under similar conditions for all agents. The same hyper-parameters were used under all tested
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 482.

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

#### Rank 1: qasper-passage-v1-57c16ca089d3641c559616655990611c095110b461d85b212cb6a134123c9839

Passage ID: `qasper-passage-v1-57c16ca089d3641c559616655990611c095110b461d85b212cb6a134123c9839`; retrieval score: 8.295659194352979.

Word count: 71.

```text
about a particular story. Since relevant events may be spawned from any part of the world (and from many multilingual sources), it becomes imperative to cluster news across different languages.

In terms of granularity, the type of story clusters we are interested in are the group of articles which, for example : (i) Narrate recent air-strikes in Eastern Ghouta (Syria); (ii) Describe the recent launch of Space X's Falcon Heavy rocket.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-d20a1e1e2f7eb356c4681b739f3c54e0ffa2fdf6e1654b31090f01f4c71f02aa

Passage ID: `qasper-passage-v1-d20a1e1e2f7eb356c4681b739f3c54e0ffa2fdf6e1654b31090f01f4c71f02aa`; retrieval score: 6.825228390089871.

Word count: 100.

```text
are the average of reduced dimensional vectors of the incoming documents as generated by an incremental singular value decomposition (SVD) of a document-term matrix that is updated after each incoming document. However, we discovered that online LSA performs significantly worse than representing the documents the way is described in § SECREF4 . Furthermore, it was also significantly slower than our algorithm due to the time it took to perform singular value decomposition.

Table TABREF35 gives the final monolingual results on the three datasets. For English, we see that the significant improvement we get using our algorithm over the algorithm of
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-c4fffe3fda1be74970806cdea61d5cf8b7d053633b010de017e75004fbfcb225

Passage ID: `qasper-passage-v1-c4fffe3fda1be74970806cdea61d5cf8b7d053633b010de017e75004fbfcb225`; retrieval score: 6.575713052389066.

Word count: 100.

```text
to the different difficulty found across the datasets for each language. The presented scores show that our learning framework generalizes well to different languages and enables high quality clustering results.

To investigate the impact of the timestamp features, we ran an additional experiment using only the same three timestamp features as used in the best model on the English dataset. This experiment yielded scores of INLINEFORM0 , INLINEFORM1 and INLINEFORM2 , which lead us to conclude that while these features are not competitive when used alone (hence temporal information by itself is not sufficient to predict the clusters), they contribute
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-7d334e0906b259332e5833f865dc2276bcc014cfc1e9a18b7e833eae1caa7cab

Passage ID: `qasper-passage-v1-7d334e0906b259332e5833f865dc2276bcc014cfc1e9a18b7e833eae1caa7cab`; retrieval score: 6.52424247379945.

Word count: 100.

```text
a completely online and scalable fashion from a continuous stream. Our clustering approach is part of a larger media monitoring project to solve the problem of monitoring massive text and TV/Radio streams (speech-to-text). In particular, media monitors write intelligence reports about the most relevant events, and being able to search, visualize and explore news clusters assists in gathering more insight about a particular story. Since relevant events may be spawned from any part of the world (and from many multilingual sources), it becomes imperative to cluster news across different languages.

In terms of granularity, the type of story clusters we
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-7fb9bc51179a10b149f06bf7f3199d9590e96c044832470658799230cd2897dc

Passage ID: `qasper-passage-v1-7fb9bc51179a10b149f06bf7f3199d9590e96c044832470658799230cd2897dc`; retrieval score: 6.422253505937922.

Word count: 100.

```text
Our system was designed to cluster documents from a (potentially infinite) real-word data stream. The datasets typically used in the literature (TDT, Reuters) have a small number of clusters ( INLINEFORM0 20) with coarse topics (economy, society, etc.), and therefore are not relevant to the use case of media monitoring we treat - as it requires much more fine-grained story clusters about particular events. To evaluate our approach, we adapted a dataset constructed for the different purpose of binary classification of joining cluster pairs. We processed it to become a collection of articles annotated with monolingual and crosslingual cluster labels.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 471.

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
          0,
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

#### Rank 1: qasper-passage-v1-1b145458e719c64e8a3baad11cf81c9a5a76900628f1f9a43bf517a37aef6f10

Passage ID: `qasper-passage-v1-1b145458e719c64e8a3baad11cf81c9a5a76900628f1f9a43bf517a37aef6f10`; retrieval score: 4.5231225078770185.

Word count: 95.

```text
Figure FIGREF1 shows the architecture of the Sequicity framework as described in BIBREF8. In essence, in each turn, the Sequicity model first takes a bspan ($B_1$) and a response ($R_1$) which are determined in the previous step, and the current human question ($U_2$) to generate the current bspan. This bspan is then used together with a knowledge base to generate the corresponding machine answer ($R_2$), as shown in the right part of Figure FIGREF1.

The left part of that figure shows an example dialogue in a mixed-domain setting (which will be explained in Section SECREF3).
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-cbc8b245bc3524bbfd27bf52270f8f729e22648556bc9a5cfa27d14766a31389

Passage ID: `qasper-passage-v1-cbc8b245bc3524bbfd27bf52270f8f729e22648556bc9a5cfa27d14766a31389`; retrieval score: 3.9805598635255173.

Word count: 100.

```text
We use the publicly available dataset KVRET BIBREF5 in our experiments. This dataset is created by the Wizard-of-Oz method BIBREF10 on Amazon Mechanical Turk platform. This dataset includes dialogues in 3 domains: calendar, weather, navigation (POI) which is suitable for our mix-domain dialogue experiments. There are 2,425 dialogues for training, 302 for validation and 302 for testing, as shown in the upper half of Table TABREF12.

In this original dataset, each dialogue is of a single domain where all of its turns are on that domain. Each turn is composed of a sentence pair, one sentence is a user utterance,
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1909.02265:5:0` | full | 0:434 |

#### Rank 3: qasper-passage-v1-4baa0f4538e2bb87375fb933ea088a3d233f57819aaca16fc111d1bac32fb6e9

Passage ID: `qasper-passage-v1-4baa0f4538e2bb87375fb933ea088a3d233f57819aaca16fc111d1bac32fb6e9`; retrieval score: 3.771111268609098.

Word count: 100.

```text
the upper half of Table TABREF12.

In this original dataset, each dialogue is of a single domain where all of its turns are on that domain. Each turn is composed of a sentence pair, one sentence is a user utterance, the other sentence is the corresponding machine response. A dialogue is a sequence of turns. To create mix-domain dialogues for our experiments, we make some changes in this dataset as follows:

We keep the dialogues in the calendar domain as they are.

We take a half of dialogues in the weather domain and a half of dialogues in the POI
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1909.02265:5:0` | partial | 401:434 |

#### Rank 4: qasper-passage-v1-895c8291c322252723f38229cda176b6c3025aec47d3dc8f7c19ae398b635c58

Passage ID: `qasper-passage-v1-895c8291c322252723f38229cda176b6c3025aec47d3dc8f7c19ae398b635c58`; retrieval score: 3.6307835354231806.

Word count: 100.

```text
our experiments, we make some changes in this dataset as follows:

We keep the dialogues in the calendar domain as they are.

We take a half of dialogues in the weather domain and a half of dialogues in the POI domain and mix their turns together, resulting in a dataset of mixed weather-POI dialogues. In this mixed-domain dialogue, there is a turn in the weather domain, followed by a turn in POI domain or vice versa.

We call this dataset the sequential turn dataset. Since the start turn of a dialogue has a special role in triggering the learning systems,
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-925f2adf059fd3f10d0611ad2526a448746d850d1f4f3a5a32c39f35f3336435

Passage ID: `qasper-passage-v1-925f2adf059fd3f10d0611ad2526a448746d850d1f4f3a5a32c39f35f3336435`; retrieval score: 3.3225492957689156.

Word count: 100.

```text
third turn is of domain weather and the fourth turn is switched to domain POI. The bspan value cleveland is retained through cross domain, resulting in an error in the fourth turn, where cleveland is shown instead of home. This example demonstrates a weakness of the system when being trained on a mixed-domain dataset. In the fifth turn, since the system does not recognize the value fastest in the bspan, it generates a random and wrong value moderate traffic. Note that the generated answer of the sixth turn is correct despite of the wrong predicted bspan; however, it is likely
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 495.

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

#### Rank 1: qasper-passage-v1-e4131fa5db0fc00f7125cc08696c023aeabe930dbf5e492c653e6e48247b199a

Passage ID: `qasper-passage-v1-e4131fa5db0fc00f7125cc08696c023aeabe930dbf5e492c653e6e48247b199a`; retrieval score: 10.775823434998914.

Word count: 100.

```text
The experiments presented here extend and refine a line of research investigating what linguistic knowledge is acquired by neural language models. Previous studies have demonstrated that sequential models trained on a simple regime of optimizing the next word can learn long-distance syntactic dependencies in impressive detail. Our results provide complimentary insights, demonstrating that a range of model architectures trained on a variety of datasets can learn fine-grained information about the interaction of CoordNPs and local syntactic context, but their behavior remains unhumanlike in many key ways. Furthermore, to our best knowledge, this work presents the first psycholinguistic analysis of neural
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-bafd9b0a0ae0a484710bdd96aab8c8563d14349d0e7fa4fdc48c10eb1465df7f

Passage ID: `qasper-passage-v1-bafd9b0a0ae0a484710bdd96aab8c8563d14349d0e7fa4fdc48c10eb1465df7f`; retrieval score: 10.105038337075598.

Word count: 100.

```text
(PTB-coord), was trained on the same sentences, but with an extended coordination annotation scheme, meant to employ the scheme employed in the FTB, adapted from BIBREF26. We stripped empty categories from their scheme and only kept the NP-COORD label for constituents inside a coordination structure. Figure FIGREF26 illustrates the detailed annotation differences between two datasets. We tested both models on all the experiments presented in Sections SECREF3-SECREF6 above.

Turning to the results of these six experiments: We see little difference between the two models in the Non-coordination agreement experiment. For the Complex coordination control and Complex coordination critical experiments, both
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-8291f1428c0dfaefd7ef21e277cfeded244ca71f782e1595ec60e732a0da3fbf

Passage ID: `qasper-passage-v1-8291f1428c0dfaefd7ef21e277cfeded244ca71f782e1595ec60e732a0da3fbf`; retrieval score: 8.414114385148881.

Word count: 100.

```text
we adapted items from Section SECREF13 in both English (37 items) and French (24 items), following the paradigm in Table TABREF24. The first part of the phrase contains either a plural or singular verb and a plural or singular noun. In this case, we sample the surprisal for the continuations and (or is grammatical in all conditions, so it is omitted from this study). Our expectation is that `and' is less surprising in the Vpl_Nsg condition than in the Vsg_Nsg condition, where a CoordNP is not licensed by the grammar in either French or English (as in *What is the
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-a7a19f7e3f2de438129c5abc17636191b836b7be2c205ac0f4e7fd5e629634fc

Passage ID: `qasper-passage-v1-a7a19f7e3f2de438129c5abc17636191b836b7be2c205ac0f4e7fd5e629634fc`; retrieval score: 8.349652205000284.

Word count: 75.

```text
(referred as `LSTM (1B)') from BIBREF14, and the other trained on English Wikipedia (referred as `LSTM (enWiki)') from BIBREF3. For French, we trained a large LSTM language model (referred as `LSTM (frWaC)') on a random subset (about 4 million sentences, 138 million word tokens) of the frWaC dataset BIBREF15. We set the size of the input embeddings and hidden layers to 400 for the LSTM (frWaC) model since it is trained on a large dataset.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1909.04625:2:1` | partial | 160:602 |

#### Rank 5: qasper-passage-v1-6140f59c5a67ec3f6372f8a48a7e3789551d85c025529daa27461c296ce051c4

Passage ID: `qasper-passage-v1-6140f59c5a67ec3f6372f8a48a7e3789551d85c025529daa27461c296ce051c4`; retrieval score: 7.997278402143699.

Word count: 100.

```text
a variety of datasets can learn fine-grained information about the interaction of CoordNPs and local syntactic context, but their behavior remains unhumanlike in many key ways. Furthermore, to our best knowledge, this work presents the first psycholinguistic analysis of neural language models trained on French, a high-resource language that has so far been under-investigated in this line of research.

In the simple coordination experiment, we demonstrated that models were able to capture some of the agreement behaviors of humans, although their performance deviated in crucial aspects. Whereas human behavior is best modeled as a `percolation' process, the neural models appear
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 475.

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
          160
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

#### Rank 1: qasper-passage-v1-36d0037d9c8cf5b0987f5fb999b3045e2f896ea9a01b426f7a321165855ba17f

Passage ID: `qasper-passage-v1-36d0037d9c8cf5b0987f5fb999b3045e2f896ea9a01b426f7a321165855ba17f`; retrieval score: 2.956278329567856.

Word count: 100.

```text
findings using another dataset, e.g., by recommending tags for scientific articles and books in BibSonomy. With this, we aim to demonstrate the usefulness of the proposed approach in a similar domain and to enhance the reproducibility of our results by using an open dataset.

Moreover, we plan to evaluate our tag recommendation approaches in a study with domain users. Also, we want to improve our similarity-based approaches by integrating novel embedding approaches BIBREF16 , BIBREF17 as we did, for example, with our proposed semantic similarity evaluation metric. Finally, we aim to incorporate explanations for recommended tags so that editors of
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-98f8498d94261a9133c3b35df22fc1674dd948109f666f695979d5bd901bc25b

Passage ID: `qasper-passage-v1-98f8498d94261a9133c3b35df22fc1674dd948109f666f695979d5bd901bc25b`; retrieval score: 2.9162124664444447.

Word count: 100.

```text
we want to improve our similarity-based approaches by integrating novel embedding approaches BIBREF16 , BIBREF17 as we did, for example, with our proposed semantic similarity evaluation metric. Finally, we aim to incorporate explanations for recommended tags so that editors of e-book annotations receive additional support in annotating e-books BIBREF21 . By making the underlying (semantic) reasoning visible to the editor who is in charge of tailoring annotations, we aim to support two goals: (i) allowing readers to discover e-books more efficiently, and (ii) enabling publishers to leverage semi-automatic categorization processes for e-books. In turn, providing explanations fosters control over which
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-a83d67699bbb513103e1bac3e4c2033f503f258e43a00c0f5ea75aea58099e37

Passage ID: `qasper-passage-v1-a83d67699bbb513103e1bac3e4c2033f503f258e43a00c0f5ea75aea58099e37`; retrieval score: 2.326685921611753.

Word count: 100.

```text
We implement three types of tag recommendation approaches, i.e., (i) popularity-based, (ii) similarity-based (i.e., using content information), and (iii) hybrid approaches. Due to the lack of personalized tags (i.e., we do not know which user has assigned a tag), we do not implement other types of algorithms such as collaborative filtering BIBREF8 . In total, we evaluate 19 different algorithms to recommend tags for annotating e-books.

Popularity-based approaches. We recommend the most frequently used tags in the dataset, which is a common strategy for tag recommendations BIBREF9 . That is, a most popular INLINEFORM0 approach for editor tags and a
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-62f7cbaa5b39ee799279f7e8491e8401e16fa7adc04425081648627017173865

Passage ID: `qasper-passage-v1-62f7cbaa5b39ee799279f7e8491e8401e16fa7adc04425081648627017173865`; retrieval score: 2.1349055797038012.

Word count: 60.

```text
good mixture of editor tags and search terms as they describe both the content and the users' opinions on the e-books (i.e., the readers' vocabulary). As shown in Table TABREF3 , we collect Amazon review keywords for 2,896 e-books (publishers: Kiwi, Rowohlt, Fischer, and Droemer), which leads to 33,663 distinct review keywords and on average 30 keyword assignments per e-book.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-36662e809d84420b01f0e291455c4b248bfcebb71258f45dcefb0c53caed8d94

Passage ID: `qasper-passage-v1-36662e809d84420b01f0e291455c4b248bfcebb71258f45dcefb0c53caed8d94`; retrieval score: 1.968172459181904.

Word count: 100.

```text
) or BISAC (= INLINEFORM4 and INLINEFORM5 ) information, we use these features to further filter the recommended tags, i.e., to only recommend tags that were used to annotate e-books of a specific author or a specific BISAC.

We combine both data sources (i.e., editor tags and Amazon search terms) using a round-robin combination strategy, which ensures an equal weight for both sources. This gives us three additional popularity-based algorithms (= INLINEFORM0 , INLINEFORM1 and INLINEFORM2 ).

Similarity-based approaches. We exploit the textual content of e-books (i.e., description or title) to recommend relevant tags BIBREF10 . For this, we first
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 460.

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

#### Rank 1: qasper-passage-v1-7e3bee31a0e4db9733149defda2a80d1124694a470f43a4255e91cf4db3958fd

Passage ID: `qasper-passage-v1-7e3bee31a0e4db9733149defda2a80d1124694a470f43a4255e91cf4db3958fd`; retrieval score: 10.406802323980505.

Word count: 100.

```text
last hidden state of the RNN encoder, our HR-VAE model imposes regularisation for all hidden states of the RNN encoder. Another advantage of our model is that it is generic and can be applied to any existing VAE-RNN-based architectures.

We evaluate our model against several strong baselines which apply VAE for text modelling BIBREF0, BIBREF7, BIBREF5. We conducted experiments based on two public benchmark datasets, namely, the Penn Treebank dataset BIBREF9 and the end-to-end (E2E) text generation dataset BIBREF10. Experimental results show that our HR-VAE model not only can effectively mitigate the latent variable collapse issue with a stable training
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-fc3c6575b1d6d459adfa1596cf52575b3b7f1188b12880de8b25ca119e05c59f

Passage ID: `qasper-passage-v1-fc3c6575b1d6d459adfa1596cf52575b3b7f1188b12880de8b25ca119e05c59f`; retrieval score: 7.73985704195737.

Word count: 72.

```text
We evaluate our model on two public datasets, namely, Penn Treebank (PTB) BIBREF9 and the end-to-end (E2E) text generation corpus BIBREF10, which have been used in a number of previous works for text generation BIBREF0, BIBREF5, BIBREF11, BIBREF12. PTB consists of more than 40,000 sentences from Wall Street Journal articles whereas the E2E dataset contains over 50,000 sentences of restaurant reviews. The statistics of these two datasets are summarised in Table TABREF11.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-8e2a9a53a8a08234c852e2578f2005096edd7d3a3f47e5c7d92910c6081ab9c2

Passage ID: `qasper-passage-v1-8e2a9a53a8a08234c852e2578f2005096edd7d3a3f47e5c7d92910c6081ab9c2`; retrieval score: 5.762263436047012.

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

#### Rank 4: qasper-passage-v1-dd57c93e8d6b0b2081595dcfa4827e078427b9541aa9b00703427f65311b5059

Passage ID: `qasper-passage-v1-dd57c93e8d6b0b2081595dcfa4827e078427b9541aa9b00703427f65311b5059`; retrieval score: 5.193340305627523.

Word count: 73.

```text
on two public benchmark datasets, namely, the Penn Treebank dataset BIBREF9 and the end-to-end (E2E) text generation dataset BIBREF10. Experimental results show that our HR-VAE model not only can effectively mitigate the latent variable collapse issue with a stable training process, but also can give better predictive performance than the baselines, as evidenced by both quantitative (e.g., negative log likelihood and perplexity) and qualitative evaluation. The code for our model is available online.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-31cc44488e846e5d2a3e34033a5baf725568d8a46017bd458693921cdca6a914

Passage ID: `qasper-passage-v1-31cc44488e846e5d2a3e34033a5baf725568d8a46017bd458693921cdca6a914`; retrieval score: 4.635303942558562.

Word count: 100.

```text
weight between the reconstruction loss and KL loss BIBREF0, BIBREF8, or resort to designing more sophisticated model structures BIBREF7, BIBREF5, BIBREF6.

In this paper, we present a simple architecture called holistic regularisation VAE (HR-VAE), which can effectively avoid latent variable collapse. In contrast to existing VAE-RNN models for text modelling which merely impose a standard normal distribution prior on the last hidden state of the RNN encoder, our HR-VAE model imposes regularisation for all hidden states of the RNN encoder. Another advantage of our model is that it is generic and can be applied to any existing VAE-RNN-based architectures.

We
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 427.

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

#### Rank 1: qasper-passage-v1-62c252761fcfbd4f8dc915dc6b21d5173f5b9e472e5f64752a93b9d5ab67516b

Passage ID: `qasper-passage-v1-62c252761fcfbd4f8dc915dc6b21d5173f5b9e472e5f64752a93b9d5ab67516b`; retrieval score: 8.238589884505675.

Word count: 85.

```text
BIBREF3, and empirically test to what extent changes in the evaluation design affect the outcome of the human evaluation. We find that for all three aspects, human translations are judged more favourably, and significantly better than MT, when we make changes that we believe strengthen the evaluation design. Based on our empirical findings, we formulate a set of recommendations for human MT evaluation in general, and assessing human–machine parity in particular. All of our data are made publicly available for external validation and further analysis.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-eb74ab266d13c20efba9571203d285709e4090266c1c933ba349f629428ea844

Passage ID: `qasper-passage-v1-eb74ab266d13c20efba9571203d285709e4090266c1c933ba349f629428ea844`; retrieval score: 7.873121715758126.

Word count: 100.

```text
in machine translation. We concur that these findings have demonstrated the need to critically re-evaluate the design of human MT evaluation.

Our paper investigates three aspects of human MT evaluation, with a special focus on assessing human–machine parity: the choice of raters, the use of linguistic context, and the creation of reference translations. We focus on the data shared by BIBREF3, and empirically test to what extent changes in the evaluation design affect the outcome of the human evaluation. We find that for all three aspects, human translations are judged more favourably, and significantly better than MT, when we make
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-7dc2814bfc46fd876d18e2f644fda8ccf3d1b3868d087fe9d4319b6c5e7b040c

Passage ID: `qasper-passage-v1-7dc2814bfc46fd876d18e2f644fda8ccf3d1b3868d087fe9d4319b6c5e7b040c`; retrieval score: 7.172462272301228.

Word count: 100.

```text
mistranslated names, and word order errors.

Our experiments show that recent findings of human–machine parity in language translation are owed to weaknesses in the design of human evaluation campaigns. We empirically tested alternatives to what is currently considered best practice in the field, and found that the choice of raters, the availability of linguistic context, and the creation of reference translations have a strong impact on perceived translation quality. As for the choice of raters, professional translators showed a significant preference for human translation, while non-expert raters did not. In terms of linguistic context, raters found human translation significantly more
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-9c8e78e950db05299c3c405a9391f4d7d4121450f63d9ff5d4b42dacddf76eaa

Passage ID: `qasper-passage-v1-9c8e78e950db05299c3c405a9391f4d7d4121450f63d9ff5d4b42dacddf76eaa`; retrieval score: 6.926556593739589.

Word count: 100.

```text
We compared professional human Chinese to English translations to the output of a strong MT system. In a human evaluation following best practices, BIBREF3 found no significant difference between the two, concluding that their NMT system had reached parity with professional human translation. Our blind qualitative analysis, however, showed that the machine translation output contained significantly more incorrect words, omissions, mistranslated names, and word order errors.

Our experiments show that recent findings of human–machine parity in language translation are owed to weaknesses in the design of human evaluation campaigns. We empirically tested alternatives to what is currently considered best practice
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-29801015cfdbaf30811faea6e2d68861b9c11b1a523144c8a3d361043e9177fb

Passage ID: `qasper-passage-v1-29801015cfdbaf30811faea6e2d68861b9c11b1a523144c8a3d361043e9177fb`; retrieval score: 6.778876585619156.

Word count: 70.

```text
that were originally Chinese, as discussed in more detail in Section SECREF35.

The machine translations produced by BIBREF3's BIBREF3 best system (Combo-6),[1] for which the authors found parity with H$_A$.

The machine translations produced by Google's production system (Google Translate) in October 2017, as contained in BIBREF3's BIBREF3 dataset.[1]

Statistical significance is denoted by * ($p\le .05$), ** ($p\le .01$), and *** ($p\le .001$) throughout this article, unless otherwise stated.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 455.

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

#### Rank 1: qasper-passage-v1-2632d33635c370bc85983a5bf69b4235fedfdb5c10345e98f1ea8796756e5675

Passage ID: `qasper-passage-v1-2632d33635c370bc85983a5bf69b4235fedfdb5c10345e98f1ea8796756e5675`; retrieval score: 10.50477297382438.

Word count: 44.

```text
As existing approaches fail to correlate well with human preference, whether and to what extent this problem affects the quality of the final NLG model when performing hyperparameter search and early-stopping?

RQ4: If the previous problem exists, can proposed comparative evaluator reduce this problem?
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-149899d23e06cf55ce9f4c97fce1f15e0c4cf42d673cf13d2d321f474f1ad245

Passage ID: `qasper-passage-v1-149899d23e06cf55ce9f4c97fce1f15e0c4cf42d673cf13d2d321f474f1ad245`; retrieval score: 9.81236810737079.

Word count: 100.

```text
We set up experiments in order to answer the following research questions:

RQ1: Can the comparative evaluator correlate better with human preference in sample-level than previous automated metrics when evaluating open domain NLG models?

RQ2: Can the comparative evaluator correlate better with human preference in model-level, so that our approach can measure the progress on open domain NLG better?

RQ3: As existing approaches fail to correlate well with human preference, whether and to what extent this problem affects the quality of the final NLG model when performing hyperparameter search and early-stopping?

RQ4: If the previous problem exists, can proposed comparative
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-6a024dfa959875c178feffd80025345d04eacb0752306418816b069eab8b7421

Passage ID: `qasper-passage-v1-6a024dfa959875c178feffd80025345d04eacb0752306418816b069eab8b7421`; retrieval score: 4.036304024175584.

Word count: 100.

```text
Evaluation of NLG models has been a long-standing open problem. While human evaluation may be ideal, it is generally expensive to conduct and does not scale well. Various automated evaluation approaches are proposed to facilitate the development and evaluation of NLG models. We summarize these evaluation approaches below.

Text Overlap Metrics, including BLEU BIBREF5, METEOR BIBREF6 and ROUGE BIBREF7, are the most popular metrics employed in the evaluation of NLG models. They evaluate generated text by comparing the similarity between the generated text and human written references. While this works well in tasks where the diversity of acceptable output is
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2002.05058:1:0` | full | 0:323 |
| `2002.05058:1:1` | partial | 0:339 |

#### Rank 4: qasper-passage-v1-d54c475fc7a13d61d26f434583b259db408fd61906152c87084c9a8b7ed4fd13

Passage ID: `qasper-passage-v1-d54c475fc7a13d61d26f434583b259db408fd61906152c87084c9a8b7ed4fd13`; retrieval score: 3.124864019707892.

Word count: 100.

```text
To test the correlation of different automated metrics with respect to human preference, we employ different metrics to score the collected 2000 samples and calculate their Pearson and Spearman correlation with human scores. For comparative evaluator, as the evaluation is performed pairwisely and no absolute score is available, we use two different approaches to get an absolute score for each sample: 1) we sample 50 common references from machine-generated samples for each task and compare each sample with all references by the comparative evaluator. A sample gets 3 points when beats a reference, 1 point when draws with the reference,
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-83185d5cc5c5d0e6cc32ee6f3cea7be5ebb9d527538aeb5fc13fdcfdca1accc6

Passage ID: `qasper-passage-v1-83185d5cc5c5d0e6cc32ee6f3cea7be5ebb9d527538aeb5fc13fdcfdca1accc6`; retrieval score: 3.0825532978017716.

Word count: 100.

```text
of overfitting the reference in the test set.

We propose to use the skill rating system to perform model-level evaluation based on the sample-level evaluation information provided by our pairwise comparison model. The skill rating system is more efficient and accurate than several baseline approaches.

We conduct experiments on both story generation task and open domain dialogue response generation task. Experimental results show that our approach correlates better with human evaluation on both datasets. Moreover, we show that using automated metrics such as BLEU to perform hyperparameter tuning and early-stopping results in sub-optimal model and our approach helps alleviate this
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 444.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "d449825aa0a1d27531a41dd5ec098834f1fde4a8": {
    "unresolved_evidence": [],
    "paragraphs": {
      "2002.05058:1:1": [
        [
          339,
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

#### Rank 1: qasper-passage-v1-b325081d8e9185a74078e65a7f61732f399201e3928d4ed109da9f9341681e4c

Passage ID: `qasper-passage-v1-b325081d8e9185a74078e65a7f61732f399201e3928d4ed109da9f9341681e4c`; retrieval score: 10.776662933286254.

Word count: 100.

```text
This paper presented the UDS-DFKI system submitted to the Similar Language Translation shared task at WMT 2019. We presented the results obtained by our system in translating from Czech to Polish. Our system achieved competitive performance ranking second among ten teams in the competition in terms of BLEU score. The fact that out-of-domain data was provided by the organizers resulted in a challenging but interesting scenario for all participants.

In future work, we would like to investigate how effective is the proposed hypothesis (i.e., word-BPE level information) in similar language translation. Furthermore, we would like to explore the similarity between
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-460083b5ecaf9188f7cebdc929f3d61b0886ad95e27da6721cbbe5041930a034

Passage ID: `qasper-passage-v1-460083b5ecaf9188f7cebdc929f3d61b0886ad95e27da6721cbbe5041930a034`; retrieval score: 10.644607210259805.

Word count: 77.

```text
outputs to any of the three language pairs in any direction. The shared task attracted a good number of participants and the performance of all entries was evaluated using popular MT automatic evaluation metrics, namely BLEU BIBREF3 and TER BIBREF4.

In this paper we describe the UDS-DFKI system to the WMT 2019 Similar Language Translation task. The system achieved competitive performance and ranked second among ten entries in Czech to Polish translation in terms of BLEU score.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-5fa37e6add57a14bceedfcfad407cc5a13640bd6a1b4b8192440b55c70f2fd1e

Passage ID: `qasper-passage-v1-5fa37e6add57a14bceedfcfad407cc5a13640bd6a1b4b8192440b55c70f2fd1e`; retrieval score: 5.653815911921978.

Word count: 66.

```text
5.0. The type column specifies the type of system, whether it is a Primary (P) or Constrastive (C) entry.

Our system was ranked second in the competition only 0.3 BLEU points behind the winning team UPC-TALP. The relative low BLEU and high TER scores obtained by all teams are due to out-of-domain data provided in the competition which made the task equally challenging to all participants.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-cd19d3532ce835ad366b3f45e815e4ee165d20280344236f3fa4bddf6953bd61

Passage ID: `qasper-passage-v1-cd19d3532ce835ad366b3f45e815e4ee165d20280344236f3fa4bddf6953bd61`; retrieval score: 5.5528744853344065.

Word count: 100.

```text
We present the results obtained by our system in Table TABREF8.

Our fine-tuned system on development set provides significant performance improvement over the generic model. We found +12.9 absolute BLEU points improvement over the generic model. Similar improvement is also observed in terms of TER (-16.9 absolute). It is to be noted that our generic model is trained solely on the clean version of training data.

Before submission, we performed punctuation normalization, unicode normalization, and detokenization for the run.

In Table TABREF9 we present the ranking of the competition provided by the shared task organizers. Ten entries were submitted by
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-f7e8424532f4451d8feb5a732be7a02c53f85dba341258b992cf9e435a1c4af4

Passage ID: `qasper-passage-v1-f7e8424532f4451d8feb5a732be7a02c53f85dba341258b992cf9e435a1c4af4`; retrieval score: 5.447864624664771.

Word count: 100.

```text
the clean version of training data.

Before submission, we performed punctuation normalization, unicode normalization, and detokenization for the run.

In Table TABREF9 we present the ranking of the competition provided by the shared task organizers. Ten entries were submitted by five teams and are ordered by BLEU score. TER is reported for all submissions which achieved BLEU score greater than 5.0. The type column specifies the type of system, whether it is a Primary (P) or Constrastive (C) entry.

Our system was ranked second in the competition only 0.3 BLEU points behind the winning team UPC-TALP. The relative low BLEU
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 443.

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

#### Rank 1: qasper-passage-v1-8ab624feaab37d8109c29aceedd0cf1769c8b479c0a1ae67b01a3a5c87696ca1

Passage ID: `qasper-passage-v1-8ab624feaab37d8109c29aceedd0cf1769c8b479c0a1ae67b01a3a5c87696ca1`; retrieval score: 7.0846446640256815.

Word count: 100.

```text
cross-validation on the account's level. For the FacTweet model, we experiment with 25% of the accounts for validation and parameters selection. We use hyperopt library to select the hyper-parameters on the following values: LSTM layer size (16, 32, 64), dropout ($0.0-0.9$), activation function ($relu$, $selu$, $tanh$), optimizer ($sgd$, $adam$, $rmsprop$) with varying the value of the learning rate (1e-1,..,-5), and batch size (4, 8, 16). The validation split is extracted on the class level using stratified sampling: we took a random 25% of the accounts from each class since the dataset is unbalanced. Discarding the classes' size in the splitting
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1910.06592:2:11` | partial | 33:688 |

#### Rank 2: qasper-passage-v1-c0bbd8d3205b8c43ea1f0b47ef0e3ec215e67858e4947f8ad16750ca9f08fa67

Passage ID: `qasper-passage-v1-c0bbd8d3205b8c43ea1f0b47ef0e3ec215e67858e4947f8ad16750ca9f08fa67`; retrieval score: 4.46155992647077.

Word count: 100.

```text
importance of taking into account the sequence of the tweets in the accounts' timelines. The sequence of these tweets is better captured by our proposed model sequence-agnostic or non-neural classifiers. Moreover, the results demonstrate that the features at tweet-level do not perform well to detect the Twitter accounts factuality, since they obtain a result near to the majority class ($0.18$). Another finding from our experiments shows that the performance of the Tweet2vec is weak. This demonstrates that tweets' hashtags are not informative to detect non-factual accounts. In Table TABREF25, we present ablation tests so as to quantify the contribution of
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-40d2c1f8b8a34bd414917dded4d10f43ffe92c5d6decb7a1c63d3fe7acca0289

Passage ID: `qasper-passage-v1-40d2c1f8b8a34bd414917dded4d10f43ffe92c5d6decb7a1c63d3fe7acca0289`; retrieval score: 4.284296295448519.

Word count: 100.

```text
as the task of detecting fake news at the account level.

The main obstacle for detecting suspicious Twitter accounts is due to the behavior of mixing some real news with the misleading ones. Consequently, we investigate ways to detect suspicious accounts by considering their tweets in groups (chunks). Our hypothesis is that suspicious accounts have a unique pattern in posting tweet sequences. Since their intention is to mislead, the way they transition from one set of tweets to the next has a hidden signature, biased by their intentions. Therefore, reading these tweets in chunks has the potential to improve the
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-4cbfed6ea8891e24686f922ce892f183119e1bc9c7f50b93eca090ff6aa1411f

Passage ID: `qasper-passage-v1-4cbfed6ea8891e24686f922ce892f183119e1bc9c7f50b93eca090ff6aa1411f`; retrieval score: 4.0196829603189626.

Word count: 100.

```text
tweet sequences. Since their intention is to mislead, the way they transition from one set of tweets to the next has a hidden signature, biased by their intentions. Therefore, reading these tweets in chunks has the potential to improve the detection of the fake news accounts.

In this work, we investigate the problem of discriminating between factual and non-factual accounts in Twitter. To this end, we collect a large dataset of tweets using a list of propaganda, hoax and clickbait accounts and compare different versions of sequential chunk-based approaches using a variety of feature sets against several baselines. Several approaches
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-ef8e7af1f309b7384dbb4a9204166744ccc2db0f25d1f1ddf066ded5da1c99b2

Passage ID: `qasper-passage-v1-ef8e7af1f309b7384dbb4a9204166744ccc2db0f25d1f1ddf066ded5da1c99b2`; retrieval score: 2.876445516779701.

Word count: 100.

```text
with a logistic regression (LR) classifier.

Tweet2vec: We use the Bidirectional Gated recurrent neural network model proposed in BIBREF20. We keep the default parameters that were provided with the implementation. To represent the tweets, we use the decoded embedding produced by the model. With this baseline we aim at assessing if the tweets' hashtags may help detecting the non-factual accounts.

LR + All Features (tweet-level): We extract all our features from each tweet and feed them into a LR classifier. Here, we do not aggregate over tweets and thus view each tweet independently.

LR + All Features (chunk-level): We concatenate
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 500.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "354142e7e6076bf3fc14e3da127f61ab12fc1b7c": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1910.06592:2:11": [
        [
          0,
          33
        ],
        [
          688,
          847
        ]
      ]
    }
  },
  "b6df7caf1df11da06f2a9339595a572829796e81": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1910.06592:2:11": [
        [
          0,
          33
        ],
        [
          688,
          847
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-927a732aafa07d898cc34e88a5d3ec197939954be4c5a514c3e60c7e2e362182

Passage ID: `qasper-passage-v1-927a732aafa07d898cc34e88a5d3ec197939954be4c5a514c3e60c7e2e362182`; retrieval score: 6.535173566775893.

Word count: 100.

```text
was further developed in BIBREF5, BIBREF6, BIBREF7, BIBREF8, BIBREF9.

With the prevalence of word embeddings, more and more work adopts pretrained word embeddings to represent the meaning of words, so as to provide the models with the knowledge of labels BIBREF10, BIBREF2, BIBREF11, BIBREF12. DBLPYogatamaDLB17 build generative LSTM to generate text given the embedded labels. DBLPRiosK18 use label embedding to attend the text representation in the developing of a multi-label classifier. But they report R@K, so it is unclear whether the system can really predict unseen labels. DBLPXiaZYCY18 study the zero-shot intent detection problem. The learned representations of intents are
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-27d638f34987f4cc876eda78b0cc526f806ef822657e7f6845eaa2f81dd8e170

Passage ID: `qasper-passage-v1-27d638f34987f4cc876eda78b0cc526f806ef822657e7f6845eaa2f81dd8e170`; retrieval score: 5.345138162527002.

Word count: 100.

```text
on the three $\textsc {0shot-tc}$ aspects (except for the RTE on emotion). Recall that they are not trained on any text classification data, and never know the domain and the aspects in the test. This clearly shows the great promise of developing textual entailment models for $\textsc {0shot-tc}$. Our ensemble approach further boosts the performances on all three tasks.

An interesting phenomenon, comparing the label-partially-unseen results in Table TABREF30 and the label-fully-unseen results in Table TABREF32, is that the pretrained entailment models work in this order for label-fully-unseen case: RTE $>$ FEVER $>$MNLI; on the contrary, if we fine-tune them
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-60709f1ebe16c5e397e0890ce697b01a5e49f76c164ceec769fec656a547276d

Passage ID: `qasper-passage-v1-60709f1ebe16c5e397e0890ce697b01a5e49f76c164ceec769fec656a547276d`; retrieval score: 4.703226814508026.

Word count: 100.

```text
indeed contributes a lot for the topic detection task; however, its performances on emotion and situation detection problems are far from satisfactory. We believe this is mainly because the Yahoo-based topic categorization task is much closer to the Wikipedia-based topic categorization task; emotion and situation categorizations, however, are relatively further.

Our entailment models, pretrained on MNLI/FEVER/RTE respectively, perform more robust on the three $\textsc {0shot-tc}$ aspects (except for the RTE on emotion). Recall that they are not trained on any text classification data, and never know the domain and the aspects in the test. This clearly shows the great promise
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-b21f5491726ec461c3362c73bc0a141715f321822ce0c9507c48c19c3f5a4dd3

Passage ID: `qasper-passage-v1-b21f5491726ec461c3362c73bc0a141715f321822ce0c9507c48c19c3f5a4dd3`; retrieval score: 4.512425979473482.

Word count: 100.

```text
attend the text representation in the developing of a multi-label classifier. But they report R@K, so it is unclear whether the system can really predict unseen labels. DBLPXiaZYCY18 study the zero-shot intent detection problem. The learned representations of intents are still the sum of word embeddings. But during testing, the intent space includes only new intents; seen intents are not covered. All of these studies can only meet the definition in Definition-Restrictive, so they do not really generalize to open aspects of $\textsc {0shot-tc}$.

JiangqngGuo enrich the embedding representations by incorporating class descriptions, class hierarchy, and the word-to-label paths in
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-60b5db2dcc8da24137211f5fd38abbbc23605c4ab1ae57d56fab50fed3e907a5

Passage ID: `qasper-passage-v1-60b5db2dcc8da24137211f5fd38abbbc23605c4ab1ae57d56fab50fed3e907a5`; retrieval score: 4.268642486145126.

Word count: 50.

```text
entailment models, especially the one pretrained on MNLI, generally get competitive performance with the “Binary-BERT” for seen (slightly worse on “topic” and “emotion” while clearly better on “situation”) and improve the performance regarding unseen by large margins. At this stage, fine-tuning on an MNLI-based pretrained entailment model seems more powerful.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 450.

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

#### Rank 1: qasper-passage-v1-c051adf277bbbbf83f0700a71ba19c9c4fccf606932c0a97c8b68bf2820230dc

Passage ID: `qasper-passage-v1-c051adf277bbbbf83f0700a71ba19c9c4fccf606932c0a97c8b68bf2820230dc`; retrieval score: 13.987771598158037.

Word count: 94.

```text
(total parameters $\pm $120 millions). The baseline with 36 layers has the same performance with 24 layers, but by adding the proposed methods, the 36 layer performance improved to give the best results. This shows that our proposed methods can improve even very deep models.

As shown in Table TABREF21, the proposed methods also provide large performance improvements on the curated video set, up to 13% with CTC, and up to 9% with the hybrid model. We also observe moderate gains of between 3.2 and 8% relative on the clean and noisy video sets.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-d4a5660911cbfaa5ae4653750506d2beeb737887f4765f01d896acf52077fa14

Passage ID: `qasper-passage-v1-d4a5660911cbfaa5ae4653750506d2beeb737887f4765f01d896acf52077fa14`; retrieval score: 9.968052792818566.

Word count: 100.

```text
In this section, we present our proposal for allowing the network to (re)-consider the input features in the light of intermediate processing. We do this by again deploying a self-attention mechanism to combine the information present in the original features with the information available in the activations of an intermediate layer. As described earlier, we calculate the output posteriors and auxiliary loss at the intermediate layer as well. The overall architecture is illustrated in Figure FIGREF6. Here, we have used a 24 layer network, with feature re-presentation after the 12th layer.

In the following subsections, we provide detail on the
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-25a2586c94bf1314871a268812dc145f35724934cab290afc8adea01a81b0aaa

Passage ID: `qasper-passage-v1-25a2586c94bf1314871a268812dc145f35724934cab290afc8adea01a81b0aaa`; retrieval score: 9.057141443426897.

Word count: 100.

```text
speed in a single GPU. Abdelrahman et al.BIBREF8 integrates a convolution layer to capture audio context and reduces WER in Librispeech.

The use of an objective function in intermediate layers has been found useful in several previous works such as image classification BIBREF25 and language modeling BIBREF26. In BIBREF27, the authors did pre-training with an RNN-T based model by using a hierarchical CTC criterion with different target units. In this paper, we don't need additional types of target unit, instead we just use same tokenization and targets for both intermediate and final losses.

The application of the objective function to
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-b6ea0eb2326d9925580a75262d61db60d94fd0aff1a10ddcf57d09cd85e23bad

Passage ID: `qasper-passage-v1-b6ea0eb2326d9925580a75262d61db60d94fd0aff1a10ddcf57d09cd85e23bad`; retrieval score: 8.293737267712352.

Word count: 97.

```text
In this paper, we have proposed a method for re-processing the input features in light of the information available at an intermediate network layer. We do this in the context of deep transformer networks, via a self-attention mechanism on both features and hidden states representation. To encourage meaningful partial results, we calculate the objective function at intermediate layers of the network as well as the output layer. This improves performance in and of itself, and when combined with feature re-presentation we observe consistent relative improvements of 10 - 20% for Librispeech and 3.2 - 13% for videos.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-fd82057497cc7417a40b142fa8bc29301e5093ddddcd630ce051d0fa686b89ac

Passage ID: `qasper-passage-v1-fd82057497cc7417a40b142fa8bc29301e5093ddddcd630ce051d0fa686b89ac`; retrieval score: 6.90209051073445.

Word count: 100.

```text
a hierarchical CTC criterion with different target units. In this paper, we don't need additional types of target unit, instead we just use same tokenization and targets for both intermediate and final losses.

The application of the objective function to intermediate layers is also similar in spirit to the use of KL-divergence in BIBREF28, which estimates output posteriors at an intermediate layer and regularizes them towards the distributions at the final layer. In contrast to this approach, the direct application of the objective function does not require the network to have a good output distribution before the new gradient contribution
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 491.

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

#### Rank 1: qasper-passage-v1-ab43e5daaabbfb529c04a0cc03733508f8f46eb4cdf01b1702d05dc20dc83699

Passage ID: `qasper-passage-v1-ab43e5daaabbfb529c04a0cc03733508f8f46eb4cdf01b1702d05dc20dc83699`; retrieval score: 13.009871191885592.

Word count: 100.

```text
falls short of the requirements for training a statistical DM. However, even if the size of the corpus is large enough the optimal dialogue strategy is likely not to be contained within it.

A solution is to transform the static corpus into a dynamic tool: a user simulator. The user simulator (US) is trained on a dialogue corpus to learn what responses a real user would provide in a given dialogue context. The US is trained using supervised learning since the aim is for it to learn typical user behaviour. For the DM, however, we want optimal behaviour which is
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-b7f5cdde3af29fcfab93e9288e654729f4c7ff509df7eb080a2610453ff69a6f

Passage ID: `qasper-passage-v1-b7f5cdde3af29fcfab93e9288e654729f4c7ff509df7eb080a2610453ff69a6f`; retrieval score: 9.954731951992523.

Word count: 100.

```text
what responses a real user would provide in a given dialogue context. The US is trained using supervised learning since the aim is for it to learn typical user behaviour. For the DM, however, we want optimal behaviour which is why supervised learning cannot be used. By interacting with the SDS, the trained US can be used to train the DM's policy. The DM's policy is optimised using the feedback given by either the user simulator or a separate evaluator. Any number of dialogues can be generated using the US and dialogue strategies that are not in the recorded corpus
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-cea5fe23d200fb7bb898bfe3e9337120818bf5b1a476184c1ce73bc7a968a1f9

Passage ID: `qasper-passage-v1-cea5fe23d200fb7bb898bfe3e9337120818bf5b1a476184c1ce73bc7a968a1f9`; retrieval score: 8.50581252158699.

Word count: 100.

```text
prohibitively expensive. Thus, it is natural to try to learn from a dataset which needs to be recorded only once, but can be used over and over again.

A problem with learning directly from recorded dialogue corpora is that the state space that was visited during the collection of the data is limited; the size of the recorded corpus usually falls short of the requirements for training a statistical DM. However, even if the size of the corpus is large enough the optimal dialogue strategy is likely not to be contained within it.

A solution is to transform the static
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-5e6b9c3213eaa12a120691f387365cb76500f9032471b71c501765d889c0c3c0

Passage ID: `qasper-passage-v1-5e6b9c3213eaa12a120691f387365cb76500f9032471b71c501765d889c0c3c0`; retrieval score: 5.395691520952768.

Word count: 100.

```text
A Task-Oriented SDS is typically designed according to a structured ontology, which defines what the system can talk about. In a system recommending restaurants the ontology defines those attributes of a restaurant that the user can choose, called informable slots (e.g. different food types, areas and price ranges), the attributes that the user can request, called requestable slots (e.g. phone number or address) and the restaurants that it has data about. An attribute is referred to as a slot and has a corresponding value. Together these are referred to as a slot-value pair (e.g. area=north).

Using RL the DM is
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-783dd0169a81f0582b3d869a8c7115bc36636481f1c590ffb76fe49282b42938

Passage ID: `qasper-passage-v1-783dd0169a81f0582b3d869a8c7115bc36636481f1c590ffb76fe49282b42938`; retrieval score: 5.092518227507048.

Word count: 100.

```text
Ideally the DM's policy would be trained by interacting with real users. Although there are models that support on-line learning BIBREF15 , for the majority of RL algorithms, which require a lot of interactions, this is impractical. Furthermore, a set of users needs to be recruited every time a policy is trained. This makes common practices such as hyper-parameter optimization prohibitively expensive. Thus, it is natural to try to learn from a dataset which needs to be recorded only once, but can be used over and over again.

A problem with learning directly from recorded dialogue corpora is that the
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 500.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "c1ed3e2a6e21d189790e8b23f0edc5422b51ec52": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1805.06966:0:2": [
        [
          0,
          774
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-78034ebc16b327c632eb34612ca6baaff2065af41a72d75108dc1d82f9f2fbf9

Passage ID: `qasper-passage-v1-78034ebc16b327c632eb34612ca6baaff2065af41a72d75108dc1d82f9f2fbf9`; retrieval score: 10.206418878137448.

Word count: 100.

```text
The fixed training condition is used to build our speaker recognition system. Only conversational telephone speech data from datasets released through the linguistic data consortium (LDC) have been used, including NIST SRE 2004-2010 and the Switchboard corpora (Switchboard Cellular Parts I and II, Switchboard2 Phase I,II and III) for different steps of system training. A more detailed description of the data used in the system training is presented in Table TABREF1 . We have also included the unlabelled set of 2472 telephone calls from both minor (Cebuano and Mandarin) and major (Tagalog and Cantonese) languages provided by NIST in the
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-8ba73cd8ab8d144e11ae02d3ac86db0c3a49a1fa214876d19eb6f65f69526257

Passage ID: `qasper-passage-v1-8ba73cd8ab8d144e11ae02d3ac86db0c3a49a1fa214876d19eb6f65f69526257`; retrieval score: 6.96256231628513.

Word count: 100.

```text
This section reports on the CPU execution time (single threaded), and the amount of memory used to process a single trial, which includes the time for creating models from the enrolment data and the time needed for processing the test segments. The analysis was performed on an Intel(R) Xeon(R) CPU E5-2670 2.60GHz. The results are shown in Table TABREF27 . We used the time command in Unix to report these results. The user time is the actual CPU time used in executing the process (single thread). The real time is the wall clock time (the elapsed time including time slices
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-b51b96d31fae697e984c7a9b210022bf8112a2b0f9fe869f74d7d4603f5550ad

Passage ID: `qasper-passage-v1-b51b96d31fae697e984c7a9b210022bf8112a2b0f9fe869f74d7d4603f5550ad`; retrieval score: 6.841755529572859.

Word count: 100.

```text
obtained through the use of the domain adaptation technique explained in Section SECREF16 . For our secondary submission, we incorporated a disjoint portion of the labelled development set (10 out of 20 speakers) in either LN-LDA and in-domain PLDA training. We evaluated the system on almost 6k out of 24k trials from the other portion to avoid any over-fitting, particularly important for the domain adaptation technique. This resulted in a relative improvement of 11% compared to the primary system in terms of the primary metric. However, the results can be misleading, since the recording condition may be the same for
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-e4e47b3bbef91385cab2e59c2a1ac5f10b66fc3d92ec19b64477a1b7887386c4

Passage ID: `qasper-passage-v1-e4e47b3bbef91385cab2e59c2a1ac5f10b66fc3d92ec19b64477a1b7887386c4`; retrieval score: 6.837571163886912.

Word count: 89.

```text
GMM/i-vector system.

We outline in this paper the Intelligent Voice system, techniques and results obtained on the SRE 2016 development set that will mirror the evaluation condition as well as the timing report. Section SECREF2 describes the data used for the system training. The front-end and back-end processing of the system are presented in Sections SECREF3 and SECREF4 respectively. In Section SECREF5 , we describe experimental evaluation of the system on the SRE 2016 development set. Finally, we present a timing analysis of the system in Section SECREF6 .
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-ff53c66ad636ecb8db32fc04a4720325c5fb42a25b9c57fb0178c843a03cbb2f

Passage ID: `qasper-passage-v1-ff53c66ad636ecb8db32fc04a4720325c5fb42a25b9c57fb0178c843a03cbb2f`; retrieval score: 5.959283872101986.

Word count: 100.

```text
time spent in the kernel within the process. We have also reported the memory allocated for each stage of execution. The most computationally intensive stage is the extraction of i-vectors (both MFCC- and PLP-based i-vectors), which also depends on the duration of the segments. For enrolment, we have reported the time required to extract a model from a segment with a duration of 140 seconds and speech duration of 60 seconds. The time and memory required for front-end processing are negligible compared to the i-vector extraction stage, since they only include matrix operations. The time required for our SAD is
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 489.

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

#### Rank 1: qasper-passage-v1-a0e86828bbe4c30f5c945c00f70ce527147b0a17242a0c121d50b293162686c7

Passage ID: `qasper-passage-v1-a0e86828bbe4c30f5c945c00f70ce527147b0a17242a0c121d50b293162686c7`; retrieval score: 8.411170625612034.

Word count: 100.

```text
far, which become observable during this second phase, are used in an adapted version of the beam sampling algorithm BIBREF183 to infer the clustering components (i.e., latent events).

They report results in terms of recall (R), precision (P), and F-score (F) by employing the mention-based B3 metric BIBREF184 , the entity-based CEAF metric BIBREF185 , and the pairwise F1 (PW) metric. Their experiments for show that both of these models work well when the feature and cluster numbers are treated as free parameters, and the selection of feature values is performed automatically.

BIBREF167 argue that events represent complex phenomena and
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-538fb2193ec6c916f94d985b5c81be24109447fb3ab6bbd19ab18d8669763e87

Passage ID: `qasper-passage-v1-538fb2193ec6c916f94d985b5c81be24109447fb3ab6bbd19ab18d8669763e87`; retrieval score: 7.728941078511017.

Word count: 100.

```text
is called semelfactives. In this new scheme, achievements are instantaneous (that is, the beginning of the event is the same as its end) culminating events, but semelfactives are events with no duration that result in no change of state. An example of a semelfactive is: Jon knocked on the door.

Table 1 presents the nomenclatures introduced by various linguists in one place. There are many variations of the schemes given here, although we do not discuss them in this paper.

In the early work on event classification, Aristotle, Vendler and others assume that what needs to be classified is the
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-4812e279f019ee621bbad2108e0dcba1133c24dba82daea8660671cfc9167fde

Passage ID: `qasper-passage-v1-4812e279f019ee621bbad2108e0dcba1133c24dba82daea8660671cfc9167fde`; retrieval score: 7.018582269128171.

Word count: 40.

```text
Different models of events have been used in computational linguistics work geared toward information extraction.

We discuss TimeML events next followed by events. We discuss biomedical event extraction in Section , and extraction of events from Twitter in Section .
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-0ecaaf350b1eb20b6c0b7c5710a9e8f63775984182bffaac46d1e1e5a2e13550

Passage ID: `qasper-passage-v1-0ecaaf350b1eb20b6c0b7c5710a9e8f63775984182bffaac46d1e1e5a2e13550`; retrieval score: 6.980359412160941.

Word count: 100.

```text
more than 6,000 of which are fully annotated, in nearly 800 hierarchically-related semantic frames, exemplified in more than 170,000 annotated sentences. See the FrameNet website for the latest statistics. FrameNet has been used as a semantic role labeling, used in applications such as information extraction, machine translation, event recognition, sentiment analysis, etc., like the other publicly available lexical resources.

An example of a frame is Attack. This frame has several frame elements. The core frame elements are assailant and victim. There are a large number of non-core frame elements. These include Circumstances, Containing_event, Direction, Duration, Explanation, Frequency, Manner, Means, Place,
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-3854dd728b6489b91764c3578b5af2592e88251d56e16ccb3fdded2bcf00c682

Passage ID: `qasper-passage-v1-3854dd728b6489b91764c3578b5af2592e88251d56e16ccb3fdded2bcf00c682`; retrieval score: 6.943188505200176.

Word count: 100.

```text
event mentions. The second model overcomes some of the limitations of the first model, and uses the infinite factorial hidden Markov model BIBREF175 coupled to the infinite hidden Markov model BIBREF176 in order to consider a potentially infinite number of features associated with observable objects which are event mentions here, perform an automatic selection of the most salient features, and capture the structural dependencies of observable objects or event mentions at the discourse level. Furthermore, both models can work with a potentially infinite number of categorical outcomes or events in this case.

Two event mentions corefer if they have the
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 440.

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

#### Rank 1: qasper-passage-v1-ddfb836330e24f7bf190126433da98110857182b839222c41ef3eeca794f8893

Passage ID: `qasper-passage-v1-ddfb836330e24f7bf190126433da98110857182b839222c41ef3eeca794f8893`; retrieval score: 7.172970154512866.

Word count: 84.

```text
Chatino is a group of languages spoken in Oaxaca, Mexico. Together with the Zapotec language group, the Chatino languages form the Zapotecan branch of the Otomanguean language family. There are three main Chatino languages: Zenzontepec Chatino (ZEN, ISO 639-2 code czn), Tataltepec Chatino (TAT, cta), and Eastern Chatino (ISO 639-2 ctp, cya, ctz, and cly) (E.Cruz 2011 and Campbell 2011). San Juan Quiahije Chatino (SJQ), the language of the focus of this study, belongs to Eastern Chatino, and is used by about 3000 speakers.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-9b730c4e1f6c7aa89f4a5fffba2f27e475ef18bb9b2ac777cf15a55d12b4b816

Passage ID: `qasper-passage-v1-9b730c4e1f6c7aa89f4a5fffba2f27e475ef18bb9b2ac777cf15a55d12b4b816`; retrieval score: 5.88543999901669.

Word count: 99.

```text
Eastern Chatino languages , including SJQ Chatino, are intensively tonal BIBREF2, BIBREF3. Tones mark both lexical and grammatical distinctions in Eastern Chatino languages.

In SJQ Chatino, there are eleven tones. Three different systems for representing tone distinctions are employed in the literature: the S-H-M-L system of BIBREF2; the numeral system of BIBREF4; and the alphabetic system of BIBREF3. The correspondences among these three systems are given in Table . For present purposes, we will use numeral representations of the second sort. The number 1 represents a high pitch, 4 represents a low pitch, and double digits represent contour tones.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-989deb687dc66ba0f0a08bcecd97dfaa2fa799681730d22a2a5a9ff513373f05

Passage ID: `qasper-passage-v1-989deb687dc66ba0f0a08bcecd97dfaa2fa799681730d22a2a5a9ff513373f05`; retrieval score: 5.8767376017512305.

Word count: 100.

```text
grammatical functions that guide language generation is of utmost importance. It follows, then, that the next crucial step for expanding NLP research on endangered languages is creating benchmarks for standard NLP tasks in such languages.

With this work we take a small first step towards this direction. We present a resource that allows for benchmarking two NLP tasks in San Juan Quiahije Chatino, an endangered language spoken in southern Mexico: morphological analysis and morphological inflection, with a focus on the verb morphology of the language.

We first briefly discuss the Chatino language and the intricacies of its verb morphology (§SECREF2),
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-7d5dc0f32be618b98330687bb2ebc87657fa2042af1048b0f0318ba7a78bd651

Passage ID: `qasper-passage-v1-7d5dc0f32be618b98330687bb2ebc87657fa2042af1048b0f0318ba7a78bd651`; retrieval score: 5.544935203680244.

Word count: 100.

```text
for endangered languages, essentially elevating them to the same level as high-resource, economically or politically stronger languages.

The majority of the world's languages are categorized as synthetic, meaning that they have rich morphology, be it fusional, agglutinative, polysynthetic, or a mixture thereof. As Natural Language Processing (NLP) keeps expanding its frontiers to encompass more and more languages, modeling of the grammatical functions that guide language generation is of utmost importance. It follows, then, that the next crucial step for expanding NLP research on endangered languages is creating benchmarks for standard NLP tasks in such languages.

With this work we take
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-a9d5b034d094b981f9ceef2db39bcb18cc78f9abdf87805473d4ecf2612d1053

Passage ID: `qasper-passage-v1-a9d5b034d094b981f9ceef2db39bcb18cc78f9abdf87805473d4ecf2612d1053`; retrieval score: 5.245549537470066.

Word count: 100.

```text
first person plural verbs: inclusive (INCL) and exclusive (EXCL)

Aspect/mood: completive (CPL), progressive (PROG), potential (POT), and habitual (HAB).

Two examples of complete inflection tables for the verbs ndyu2 `fell from above' and lyu1 `fall' are shown in Table . Note how the first verb has the same PN triplet for all four aspect/mood categories, while the second paradigm is more representative in that it involves three different triplets (one for the completive, another for the progressive, and another for the habitual/potential). This variety is at the core of why the SJQ verb morphology is particularly interesting, and a challenging
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 483.

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
