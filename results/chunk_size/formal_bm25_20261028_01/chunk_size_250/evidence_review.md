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

#### Rank 1: qasper-passage-v1-ef90349b013851f1257559db8ed9bfaadb1dc4119a128562fe107a5721bf8513

Passage ID: `qasper-passage-v1-ef90349b013851f1257559db8ed9bfaadb1dc4119a128562fe107a5721bf8513`; retrieval score: 5.11122167046978.

Word count: 103.

```text
In recent years, various models for learning cross-lingual representations have been proposed. Two main broad categories with some related papers are identified here:

Monolingual mapping: In this approach, models are trained using word embeddings from a monolingual corpora. Then, an objective function is used to minimize a linear mapping that enable them to map unknown words from the source language to the target language.

Pseudo-cross-lingual: In this case we create a pseudo-cross-lingual corpus by mixing contexts of different languages. We then train an off-the-shelf word embedding model on the created corpus. Ideally the cross-lingual contexts allow the learned representations to capture cross-lingual relations.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-8b777ac115230157596949bc810229caa076577842725cf6daf02c6eb4f42839

Passage ID: `qasper-passage-v1-8b777ac115230157596949bc810229caa076577842725cf6daf02c6eb4f42839`; retrieval score: 5.108952376767218.

Word count: 243.

```text
Methods for machine translations have been studied for years, and at the same time algorithms to generate word embeddings are becoming more and more accurate. Still, there is a lot of research aiming at unifying word embeddings across multiple languages. In this experience we try a technique for machine translation that relates word embeddings between two different languages. Based on the literature we found that it is possible to infer missing dictionary entries using distributed representations of words and phrases. One way of doing it is to create a linear mapping between the two vector spaces of two different languages. In order to achieve this, we first built two dictionaries of the two different languages. Next, we learned a function that projects the first vector space to the second one. In this way, we are able to translate every word belonging to the first language into the second one. Once we obtain the translated word embedding, we output the most similar word vector as the translation. The word embeddings were learnt using the Skip Gram method proposed by (Mikolov et al., 2013a). An example of how the method would work is reported in figure 1 and figure 2. After creating the word embeddings from the two dictionaries, we plotted the numbers in the two graphs using PCA. Figure 3 reports the results after creating a linear mapping between the embeddings from the two languages. You can see how similar words are closer together.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-99bba4547e0684e34c5f79d63ee20a66627c9b0acaff95b7abf4e8af37fd43a6

Passage ID: `qasper-passage-v1-99bba4547e0684e34c5f79d63ee20a66627c9b0acaff95b7abf4e8af37fd43a6`; retrieval score: 4.911134746766101.

Word count: 131.

```text
It was recently shown that the distributed representations of words capture surprisingly many linguistic regularities, and that there are many types of similarities among words that can be expressed as linear translations (Mikolov et al., 2013c). In the Skip-gram model, the training objective is to learn word vector representations that are good at predicting its context in the same sentence (Mikolov et al., 2013a). The objective function that skip gram tries to minimize is the following:

Where N represents the total number of words in a sentence, P the probability of a word at the position i+j to belong to the sentence, with respect to the word i. Ideally, by using this approach we will be able to provide non-trivial translations that will be related to the context of a word.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-ee8dd3d40dbdb29c7f97fb73b174570af6af4702175e75cedda475ef11d7b919

Passage ID: `qasper-passage-v1-ee8dd3d40dbdb29c7f97fb73b174570af6af4702175e75cedda475ef11d7b919`; retrieval score: 3.2613921676067528.

Word count: 175.

```text
Since the word embeddings in a single language are based on the cosine similarity, we realized that through the objective function reported in equation 1 we were losing the property of this similarity. As a result we wanted the dot products to be preserved after the mapping. In order to do that we normalized the vectors $x_i$ and $z_i$.The new objective function looks like:

In order to preserve the dot products after the linear mapping we also had to constrain W to be an orthogonal matrix. In order to orthogonalize the matrix, it's required to solve the following optimization problem:

One can show that this problem can be solved by taking the singular value decomposition (SVD) of W and replacing the singular values to ones. This approximation would only work when the dimensions of the source vector and the target vector are the same, which is the set up we are working with. So finally, the method that we tried for this experience uses normalized vectors, and is reduced by using the cosine similarity function.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-50459e4dc56794bc3dd3f330614d8606f3c93875cad5c1ce30825c695502ce35

Passage ID: `qasper-passage-v1-50459e4dc56794bc3dd3f330614d8606f3c93875cad5c1ce30825c695502ce35`; retrieval score: 3.2399003030253533.

Word count: 55.

```text
This represents the linear function that maps word embeddings from one language to another. Given a word x in one language, and the respective word in the other language z, the following equation reports the objective function we want to minimize:

Were W represents the final matrix that will contain the values for the mapping.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 707.

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

#### Rank 1: qasper-passage-v1-c9e36392a9c73ebb2c154667c244dc8eca0fcd97d8ebf2e8a2e4c66e1749e698

Passage ID: `qasper-passage-v1-c9e36392a9c73ebb2c154667c244dc8eca0fcd97d8ebf2e8a2e4c66e1749e698`; retrieval score: 2.703869596441051.

Word count: 250.

```text
The focus of this section is on recently published datasets and LID research applicable to the South African context. An in depth survey of algorithms, features, datasets, shared tasks and evaluation methods may be found in BIBREF0.

The datasets for the DSL 2015 & DSL 2017 shared tasks BIBREF1 are often used in LID benchmarks and also available on Kaggle . The DSL datasets, like other LID datasets, consists of text sentences labelled by language. The 2017 dataset, for example, contains 14 languages over 6 language groups with 18000 training samples and 1000 testing samples per language.

The recently published JW300 parallel corpus BIBREF2 covers over 300 languages with around 100 thousand parallel sentences per language pair on average. In South Africa, a multilingual corpus of academic texts produced by university students with different mother tongues is being developed BIBREF3. The WiLI-2018 benchmark dataset BIBREF4 for monolingual written natural language identification includes around 1000 paragraphs of 235 languages. A possibly useful link can also be made BIBREF5 between Native Language Identification (NLI) (determining the native language of the author of a text) and Language Variety Identification (LVI) (classification of different varieties of a single language) which opens up more datasets. The Leipzig Corpora Collection BIBREF6, the Universal Declaration of Human Rights and Tatoeba are also often used sources of data.

The NCHLT text corpora BIBREF7 is likely a good starting point for a shared LID task dataset for the South African languages BIBREF8. The NCHLT text corpora contains enough data
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-c50e832bd51c0af64318cfc604c7a85e1820533415942c03b32831363c8544f1

Passage ID: `qasper-passage-v1-c50e832bd51c0af64318cfc604c7a85e1820533415942c03b32831363c8544f1`; retrieval score: 1.37168806012201.

Word count: 250.

```text
The proposed LID algorithm builds on the work in BIBREF8 and BIBREF26. We apply a naive Bayesian classifier with character (2, 4 & 6)-grams, word unigram and word bigram features with a hierarchical lexicon based classifier.

The naive Bayesian classifier is trained to predict the specific language label of a piece of text, but used to first classify text as belonging to either the Nguni family, the Sotho family, English, Afrikaans, Xitsonga or Tshivenda. The scikit-learn multinomial naive Bayes classifier is used for the implementation with an alpha smoothing value of 0.01 and hashed text features.

The lexicon based classifier is then used to predict the specific language within a language group. For the South African languages this is done for the Nguni and Sotho groups. If the lexicon prediction of the specific language has high confidence then its result is used as the final label else the naive Bayesian classifier's specific language prediction is used as the final result. The lexicon is built over all the data and therefore includes the vocabulary from both the training and testing sets.

The lexicon based classifier is designed to trade higher precision for lower recall. The proposed implementation is considered confident if the number of words from the winning language is at least one more than the number of words considered to be from the language scored in second place.

The stacked classifier is tested against three public LID implementations BIBREF17, BIBREF23, BIBREF8. The LID implementation described in BIBREF17 is available on
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-295a4985415648219807e0360def89be85ff4ef4e69ca0b1f0ea62e6b4247c15

Passage ID: `qasper-passage-v1-295a4985415648219807e0360def89be85ff4ef4e69ca0b1f0ea62e6b4247c15`; retrieval score: 1.0495760590087981.

Word count: 45.

```text
codes that include more languages seems to be growing and discoverability of research is improving with more survey papers coming out. Paywalls also seem to no longer be a problem; the references used in this paper was either openly published or available as preprint papers.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-29b41e3b7015b82719c18bdfac7682f1eae58b54bb989dfdfdb122c0dff61158

Passage ID: `qasper-passage-v1-29b41e3b7015b82719c18bdfac7682f1eae58b54bb989dfdfdb122c0dff61158`; retrieval score: 1.0363845805447551.

Word count: 250.

```text
Rights and Tatoeba are also often used sources of data.

The NCHLT text corpora BIBREF7 is likely a good starting point for a shared LID task dataset for the South African languages BIBREF8. The NCHLT text corpora contains enough data to have 3500 training samples and 600 testing samples of 300+ character sentences per language. Researchers have recently started applying existing algorithms for tasks like neural machine translation in earnest to such South African language datasets BIBREF9.

Existing NLP datasets, models and services BIBREF10 are available for South African languages. These include an LID algorithm BIBREF11 that uses a character level n-gram language model. Multiple papers have shown that 'shallow' naive Bayes classifiers BIBREF12, BIBREF8, BIBREF13, BIBREF14, SVMs BIBREF15 and similar models work very well for doing LID. The DSL 2017 paper BIBREF1, for example, gives an overview of the solutions of all of the teams that competed on the shared task and the winning approach BIBREF16 used an SVM with character n-gram, parts of speech tag features and some other engineered features. The winning approach for DSL 2015 used an ensemble naive Bayes classifier. The fasttext classifier BIBREF17 is perhaps one of the best known efficient 'shallow' text classifiers that have been used for LID .

Multiple papers have proposed hierarchical stacked classifiers (including lexicons) that would for example first classify a piece of text by language group and then by exact language BIBREF18, BIBREF19, BIBREF8, BIBREF0. Some work has also been done on classifying surnames between Tshivenda, Xitsonga
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-7b0ad0472ea7b88ce47a22ee66a51a78278a6eee1071fbf827f3256ca46dc555

Passage ID: `qasper-passage-v1-7b0ad0472ea7b88ce47a22ee66a51a78278a6eee1071fbf827f3256ca46dc555`; retrieval score: 1.0218014365926034.

Word count: 189.

```text
least one more than the number of words considered to be from the language scored in second place.

The stacked classifier is tested against three public LID implementations BIBREF17, BIBREF23, BIBREF8. The LID implementation described in BIBREF17 is available on GitHub and is trained and tested according to a post on the fasttext blog. Character (5-6)-gram features with 16 dimensional vectors worked the best. The implementation discussed in BIBREF23 is available from https://github.com/tomkocmi/LanideNN. Following the instructions for an OSX pip install of an old r0.8 release of TensorFlow, the LanideNN code could be executed in Python 3.7.4. Settings were left at their defaults and a learning rate of 0.001 was used followed by a refinement with learning rate of 0.0001. Only one code modification was applied to return the results from a method that previously just printed to screen. The LID algorithm described in BIBREF8 is also available on GitHub.

The stacked classifier is also tested against the results reported for four other algorithms BIBREF16, BIBREF26, BIBREF24, BIBREF15. All the comparisons are done using the NCHLT BIBREF7, DSL 2015 BIBREF19 and DSL 2017 BIBREF1 datasets discussed in Section SECREF2.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 984.

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

#### Rank 1: qasper-passage-v1-2fce7c78634f8a686f605f2b4b637ff358b4b4b7017ee558f68e249858773861

Passage ID: `qasper-passage-v1-2fce7c78634f8a686f605f2b4b637ff358b4b4b7017ee558f68e249858773861`; retrieval score: 2.994575771344636.

Word count: 160.

```text
The results for each class type are shown in Table TABREF19 , with some specific examples shown in Figure FIGREF18 . For the Wiki(gold) we quote the micro-averaged F-1 scores for the entire top level entity category. The total F-1 score on the OntoNotes dataset is 88%, and the total F-1 cross-validation score on the 112 class Wiki(gold) dataset is 53%. It is worth noting that one could improve Wiki(gold) results by training directly using this dataset. However, the aim is not to tune our model specifically on this class hierarchy. We instead aim to present a framework which can be modified easily to any domain hierarchy and has acceptable out-of-the-box performances to any fine-grained dataset. The results in Table TABREF19 (OntoNotes) only show the main 7 categories in OntoNotes which map to Wiki(gold) for clarity. The other categories (date, time, norp, language, ordinal, cardinal, quantity, percent, money, law) have F-1 scores between 80-90%, with the exception of time (65%)
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.10503:6:0` | full | 0:992 |

#### Rank 2: qasper-passage-v1-04823e4b85ed2a8ed968f796b8487184972c31964ca95abbc6265fbaf236966b

Passage ID: `qasper-passage-v1-04823e4b85ed2a8ed968f796b8487184972c31964ca95abbc6265fbaf236966b`; retrieval score: 2.5784665479317637.

Word count: 250.

```text
Named entity recognition (NER) BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 is the process by which we identify text spans which mention named entities, and to classify them into predefined categories such as person, location, organization etc. NER serves as the basis for a variety of natural language processing (NLP) applications such as relation extraction BIBREF4 , machine translation BIBREF5 , question answering BIBREF6 and knowledge base construction BIBREF7 . Although early NER systems have been successful in producing adequate recognition accuracy, they often require significant human effort in carefully designing rules or features.

In recent years, deep learning methods been employed in NER systems, yielding state-of-the-art performance. However, the number of types detected are still not sufficient for certain domain-specific applications. For relation extraction, identifying fine-grained types has been shown to significantly increase the performance of the extractor BIBREF8 , BIBREF9 since this helps in filtering out candidate relation types which do not follow this type constraint. Furthermore, for question answering fine-grained Named Entity Recognition (FgNER) can provide additional information helping to match questions to its potential answers thus improving performance BIBREF10 . For example, Li and Roth BIBREF11 rank questions based on their expected answer types (i.e. will the answer be food, vehicle or disease).

Typically, FgNER systems use over a hundred labels, arranged in a hierarchical structure. We find that available training data for FgNER typically contain noisy labels, and creating manually annotated training data for FgNER is a time-consuming process. Furthermore, human annotators will have to
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-fc16d7043b9f3111d1ceaedc1267b9cdbed56feb869c29a6d3716c326ff844ca

Passage ID: `qasper-passage-v1-fc16d7043b9f3111d1ceaedc1267b9cdbed56feb869c29a6d3716c326ff844ca`; retrieval score: 2.5676250627968016.

Word count: 250.

```text
Entity linking (EL) BIBREF24 , also known as named entity disambiguation or normalization, is the task to determine the identity of entities mentioned in a piece of text with reference to a knowledge base. There are a number of knowledge bases that provide a background repository for entity classification of this type. For this study, we use Wikidata, which can be seen diagrammatically in Figure FIGREF12 . Systems such as DeepType BIBREF25 integrate symbolic information into the reasoning process of a neural network with a type system and show state-of-the-art performances for EL. They do not, however, quote results on Wiki(gold) so a direct comparison is difficult.

While these knowledge bases provide semantically rich and fine-granular classes and relationship types, the task of entity classification often requires associating coarse-grained classes with discovered surface forms of entities. Most existing studies consider NER and entity linking as two separate tasks, whereas we try to combine the two. It has been shown that one can significantly increase the semantic information carried by a NER system when we successfully linking entities from a deep learning method to the related entities from a knowledge base BIBREF26 , BIBREF27 .

Redirection: For the Wikidata linking element, we recognize that the lookup will be constrained by the most common lookup name for each entity. Consider the utterance (referring to the NBA basketball player) from Figure FIGREF12 “Michael Jeffrey Jordan in San Jose” as an example. The lookup for this entity in Wikidata is “Michael Jordan” and consequently
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-8bfa5307f138c3f29c0cd08c455946c34638591994e1ba8b15a03053065272b0

Passage ID: `qasper-passage-v1-8bfa5307f138c3f29c0cd08c455946c34638591994e1ba8b15a03053065272b0`; retrieval score: 1.8127481564015493.

Word count: 250.

```text
NER involves identifying both entity boundaries and entity types. With “exact-match evaluation”, a named entity is considered correctly recognized only if both the boundaries and type match the ground truth BIBREF8 , BIBREF17 , BIBREF18 . Precision, Recall, and F-1 scores are computed on the number of true positives (TP), false positives (FP), and false negatives (FN). Their formal definitions are as follows:

True Positive (TP): entities that are recognized by NER and match the ground truth.

False Positive (FP): entities that are recognized by NER but do not match the ground truth.

False Negative (FN): entities annotated in the ground which that are not recognized by NER.

Precision measures the ability of a NER system to present only correct entities, and Recall measures the ability of a NER system to recognize all entities in a corpus. DISPLAYFORM0

The F-1 score is the harmonic mean of precision and recall, and the balanced F-1 score is the variant which is most commonly used. This is defined as: DISPLAYFORM0

Since most NER systems involve multiple entity types, it is often required to assess the performance across all entity classes. Two measures are commonly used for this purpose: the macro-averaged F-1 score and the micro-averaged F-1 score. The macro-averaged F-1 score computes the F-1 score independently for each entity type, then takes the average (hence treating all entity types equally). The micro-averaged F-1 score aggregates the contributions of entities from all classes to compute the average (treating all entities equally). We use the
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-7a4e143cc445f4ba8f4509ca002527ccb4b959666c28482f8ce9c0e4b71a37d1

Passage ID: `qasper-passage-v1-7a4e143cc445f4ba8f4509ca002527ccb4b959666c28482f8ce9c0e4b71a37d1`; retrieval score: 1.5619701514490332.

Word count: 250.

```text
use over a hundred labels, arranged in a hierarchical structure. We find that available training data for FgNER typically contain noisy labels, and creating manually annotated training data for FgNER is a time-consuming process. Furthermore, human annotators will have to assign a subset of correct labels from hundreds of possible labels making this a somewhat arduous task. Currently, FgNER systems use distant supervision BIBREF12 to automatically generate training data. Distant supervision is a technique which maps each entity in the corpus to knowledge bases such as Freebase BIBREF13 , DBpedia BIBREF14 , YAGO BIBREF15 and helps with the generation of labeled data. This method will assign the same set of labels to all mentions of a particular entity in the corpus. For example, “Barack Obama” is a person, politician, lawyer, and author. If a knowledge base has these four matching labels, the distant supervision technique will assign all of them to every mention of “Barack Obama”. Therefore, the training data will also fail to distinguish between mentions of “Barack Obama” in all subsequent utterances.

Ling et al. ling2012fine proposed the first system for FgNER, where they used 112 overlapping labels with a linear classifier perceptron for multi-label classification. Yosef et al. spaniol2012hyena used multiple binary SVM classifiers to assign entities to a set of 505 types. Gillick et al. gillick2014context introduced context dependent FgNER and proposed a set of heuristics for pruning labels that might not be relevant given the local context of the entity. Yogatama et al. yogatama2015embedding proposed
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1160.

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

#### Rank 1: qasper-passage-v1-40d1f24923c533f4a9c4c2cf85f836574d901b48875f4be1a3a90c4c161181b0

Passage ID: `qasper-passage-v1-40d1f24923c533f4a9c4c2cf85f836574d901b48875f4be1a3a90c4c161181b0`; retrieval score: 6.742099426312027.

Word count: 210.

```text
To the best of our knowledge, there are only two recent works that specifically study how to combine word and subword-level vector representations.

BIBREF11 propose to use a trainable scalar gating mechanism capable of learning a weighting scheme for combining character-level and word-level representations. They compared their proposed method to manually weighting both levels; using characters only; words only; or their concatenation. They found that in some datasets a specific manual weighting scheme performed better, while in others the learned scalar gate did.

BIBREF12 further expand the gating concept by making the mechanism work at a finer-grained level, learning how to weight each vector's dimensions independently, conditioned on external word-level features such as part-of-speech and named-entity tags. Similarly, they compared their proposed mechanism to using words only, characters only, and a concatenation of both, with and without external features. They found that their vector gate performed better than the other methods in all the reported tasks, and beat the state of the art in two reading comprehension tasks.

Both works showed that the gating mechanisms assigned greater importance to character-level representations in rare words, and to word-level representations in common ones, reaffirming the previous findings that subword structures in general, and characters in particular, are beneficial for modeling uncommon words.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-f832d66ef5267abd0169851d7d259d6fe151b4ebbc5dec696ff98e1f96f58d7d

Passage ID: `qasper-passage-v1-f832d66ef5267abd0169851d7d259d6fe151b4ebbc5dec696ff98e1f96f58d7d`; retrieval score: 5.55893476903343.

Word count: 130.

```text
To enable sentence-level classification we need to obtain a sentence representation from the word vectors INLINEFORM0 . We achieved this by using a BiLSTM with max pooling, which was shown to be a good universal sentence encoding mechanism BIBREF13 .

Let INLINEFORM0 , be an input sentence and INLINEFORM1 its matrix representation, where each INLINEFORM2 was obtained by one of the methods described in subsec:methods. INLINEFORM3 is the context-enriched matrix representation of INLINEFORM4 obtained by feeding INLINEFORM5 to a BiLSTM of output dimension INLINEFORM6 . Lastly, INLINEFORM11 is the final sentence representation of INLINEFORM12 obtained by max-pooling INLINEFORM13 along the sequence dimension.

Finally, we initialized the word representations INLINEFORM0 using GloVe embeddings BIBREF14 , and fine-tuned them during training. Refer to app:hyperparams for details on the other hyperparameters we used.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.05584:4:0` | full | 0:250 |

#### Rank 3: qasper-passage-v1-a5ff31c7076cc936c6ef8675c4d66f3a076ca30b2f63d78b92b714303930e64e

Passage ID: `qasper-passage-v1-a5ff31c7076cc936c6ef8675c4d66f3a076ca30b2f63d78b92b714303930e64e`; retrieval score: 4.844981974224655.

Word count: 250.

```text
Incorporating sub-word structures like substrings, morphemes and characters to the creation of word representations significantly increases their quality as reflected both by intrinsic metrics and performance in a wide range of downstream tasks BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 .

The reason for this improvement is related to sub-word structures containing information that is usually ignored by standard word-level models. Indeed, when representing words as vectors extracted from a lookup table, semantically related words resulting from inflectional processes such as surf, surfing, and surfed, are treated as being independent from one another. Further, word-level embeddings do not account for derivational processes resulting in syntactically-similar words with different meanings such as break, breakable, and unbreakable. This causes derived words, which are usually less frequent, to have lower-quality (or no) vector representations.

Previous works have successfully combined character-level and word-level word representations, obtaining overall better results than using only word-level representations. For example BIBREF1 achieved state-of-the-art results in a machine translation task by representing unknown words as a composition of their characters. BIBREF4 created word representations by adding the vector representations of the words' surface forms and their morphemes ( INLINEFORM0 ), obtaining significant improvements on intrinsic evaluation tasks, word similarity and machine translation. BIBREF5 concatenated character-level and word-level representations for creating word representations, and then used them as input to their models for obtaining state-of-the-art results in Named Entity Recognition on several languages.

What these works have in common is that the models they describe first learn how to represent
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-cfc2d8a52c3c6c21755f5dbe5ca3c7b93a3e2f80333cc80eac74bd49bdb835dc

Passage ID: `qasper-passage-v1-cfc2d8a52c3c6c21755f5dbe5ca3c7b93a3e2f80333cc80eac74bd49bdb835dc`; retrieval score: 4.8093708912475694.

Word count: 250.

```text
The problem of representing sentences as fixed-length vectors has been widely studied.

BIBREF32 suggested a self-adaptive hierarchical model that gradually composes words into intermediate phrase representations, and adaptively selects specific hierarchical levels for specific tasks. BIBREF33 proposed an encoder-decoder model trained by attempting to reconstruct the surrounding sentences of an encoded passage, in a fashion similar to Skip-gram BIBREF34 . BIBREF35 overcame the previous model's need for ordered training sentences by using autoencoders for creating the sentence representations. BIBREF36 implemented a model simpler and faster to train than the previous two, while having competitive performance. Similar to BIBREF33 , BIBREF37 suggested predicting future sentences with a hierarchical CNN-LSTM encoder.

BIBREF13 trained several sentence encoding architectures on a combination of the SNLI and MultiNLI datasets, and showed that a BiLSTM with max-pooling was the best at producing highly transferable sentence representations. More recently, BIBREF18 empirically showed that sentence representations created in a multi-task setting BIBREF38 , performed increasingly better the more tasks they were trained in. BIBREF39 proposed using an autoencoder that relies on multi-head self-attention over the concatenation of the max and mean pooled encoder outputs for producing sentence representations. Finally, BIBREF40 show that modern sentence embedding methods are not vastly superior to random methods.

The works mentioned so far usually evaluate the quality of the produced sentence representations in sentence-level downstream tasks. Common benchmarks grouping these kind of tasks include SentEval BIBREF23 , and GLUE BIBREF41 . Another trend, however, is to probe sentence representations to understand what linguistic
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-5c9fb8de285a2d47c5fe2c419258e5bb19baf9496eb1cd43eabd12a37b008cc4

Passage ID: `qasper-passage-v1-5c9fb8de285a2d47c5fe2c419258e5bb19baf9496eb1cd43eabd12a37b008cc4`; retrieval score: 4.280104832223368.

Word count: 250.

```text
table:wordlevelresults shows the quality of word representations in terms of the correlation between word similarity scores obtained by the proposed models and word similarity scores defined by humans.

First, we can see that for each task, character only models had significantly worse performance than every other model trained on the same dataset. The most likely explanation for this is that these models are the only ones that need to learn word representations from scratch, since they have no access to the global semantic knowledge encoded by the GloVe embeddings.

Further, bold results show the overall trend that vector gates outperformed the other methods regardless of training dataset. This implies that learning how to combine character and word-level representations at the dimension level produces word vector representations that capture a notion of word similarity and relatedness that is closer to that of humans.

Additionally, results from the MNLI row in general, and underlined results in particular, show that training on MultiNLI produces word representations better at capturing word similarity. This is probably due to MultiNLI data being richer than that of SNLI. Indeed, MultiNLI data was gathered from various sources (novels, reports, letters, and telephone conversations, among others), rather than the single image captions dataset from which SNLI was created.

Exceptions to the previous rule are models evaluated in MEN and RW. The former case can be explained by the MEN dataset containing only words that appear as image labels in the ESP-Game and MIRFLICKR-1M image datasets BIBREF24 , and therefore
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1090.

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

#### Rank 1: qasper-passage-v1-397e875b7909d7e5cf6e93dd7f26c91478df4175d9ad33b97938b4e37f2c9b2d

Passage ID: `qasper-passage-v1-397e875b7909d7e5cf6e93dd7f26c91478df4175d9ad33b97938b4e37f2c9b2d`; retrieval score: 4.847019410973598.

Word count: 250.

```text
We downloaded 76 videos from a tutorial website about an image editing program . Each video is pre-processed to provide the transcripts and the time-stamp information for each sentence in the transcript. We then used Amazon Mechanical Turk to collect the question-answer pairs . One naive way of collecting the data is to prepare a question list and then, for each question, ask the workers to find the relevant parts in the video. However, this approach is not feasible and error-prone because the videos are typically long and finding a relevant part from a long video is difficult. Doing so might also cause us to miss questions which were relevant to the video segment. Instead, we took a reversed approach. First, for each video, we manually identified the sentence spans that can serve as answers. These candidates are of various granularity and may overlap. The segments are also complete in that they encompass the beginning and end of a task. In total, we identified 408 segments from the 76 videos. Second we asked AMT workers to provide question annotations for the videos.

Our AMT experiment consisted of two parts. In the first part, we presented the workers with the video content of a segment. For each segment, we asked workers to generate questions that can be answered by the presented segment. We did not limit the number of questions a worker can input to a corresponding segment and encouraged them to input a diverse set of questions which the span
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-d81d61463e623496a5f417f6bffd11e14b4152bbc282499746d85ee34da0a3ca

Passage ID: `qasper-passage-v1-d81d61463e623496a5f417f6bffd11e14b4152bbc282499746d85ee34da0a3ca`; retrieval score: 4.601556600841127.

Word count: 236.

```text
Table TABREF12 presents some extracted sample questions from our dataset. The first column corresponds to an AMT generated question, while the second column corresponds to the video ID where the segment can be found. As can be seen in the first two rows, multiple types of questions can be answered within the same video (but different segments). The last two rows display questions which belong to the same segment but correspond to different properties of the same entity, 'crop tool'. Here we observe different types of questions, such as "why", "how", "what", and "where", and can see why the answers may involve multiple steps. Some questions that the worked paraphrased were in the "yes/no" style, however our answer segments then provide an explanation to these questions.

Each answer segment was extracted from an image editing tutorial video that involved multiple steps and procedures to produce a final image, which can partially be seen in FIGREF1. The average number of sentences per video was approximately 52, with the maximum number of sentences contained in a video being 187. The sub-tasks in the tutorial include segments (and thus answers) on editing parts of images, instructions on using certain tools, possible actions that can be performed on an image, and identifying the locations of tools and features, with the shortest and longest segment having a span of 1 and 37 sentences respectively, demonstrating the heterogeneity of the answer spans.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-52b253980b6d7bb88518c75fb3771478c2f1966cb7fe6165b981a87ba1cb0751

Passage ID: `qasper-passage-v1-52b253980b6d7bb88518c75fb3771478c2f1966cb7fe6165b981a87ba1cb0751`; retrieval score: 4.032811025311288.

Word count: 250.

```text
Video is the fastest growing medium to create and deliver information today. Consequentially, videos have been increasingly used as main data sources in many question answering problems BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, BIBREF2, BIBREF5. These previous studies have mostly focused on factoid questions, each of which can be answered in a few words or phrases generated by understanding multimodal contents in a short video clip.

However, this problem definition of video question answering causes some practical limitations for the following reasons. First, factoid questions are just a small part of what people actually want to ask on video contents. Especially if a short video is given to users, most fragmentary facts within the scope of previous tasks can be easily perceived by themselves even before asking questions. Thus, video question answering is expected to provide answers to more complicated non-factoid questions beyond the simple facts. For example, those questions could be the ones asking about a how procedure as shown in Fig. FIGREF5, and the answers should contain all necessary steps to complete the task.

Accordingly, the answer format needs to also be improved towards more flexible ways than multiple choice BIBREF1, BIBREF2 or fill-in-the-blank questions BIBREF3, BIBREF4. Although open-ended video question answering BIBREF0, BIBREF2, BIBREF5 has been explored, it still aims to generate just a short word or phrase-level answer, which is not enough to cover various granularities of non-factoid question answering.

The other issue is that most videos with sufficient amount of information, which are likely to be
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-3704ffb1505dc378910c490e329b16ef5bc6b331198c8eb6676d09d562676253

Passage ID: `qasper-passage-v1-3704ffb1505dc378910c490e329b16ef5bc6b331198c8eb6676d09d562676253`; retrieval score: 3.972005493806823.

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

#### Rank 5: qasper-passage-v1-dcf3a775059b0e50e1495c25ed114a51500ef1fe6fb3236a349f465471e14aff

Passage ID: `qasper-passage-v1-dcf3a775059b0e50e1495c25ed114a51500ef1fe6fb3236a349f465471e14aff`; retrieval score: 3.92443413127537.

Word count: 65.

```text
the corresponding segments:

selecting the segment with the minimal cosine distance distance to the query.

Metrics. To evaluate our pipeline approach we use overall accuracy after filtering and accuracy given that the segment is in the top 10 videos. While the first metric is similar to SECREF17, the second can indicate if initially searching on the video space can be used to improve our selection:
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1912.01046:10:4` | full | 0:294 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 1041.

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

#### Rank 1: qasper-passage-v1-5bcd3538966d084245dacd4aa1eab04bde0d976b1efcbee8c093627b528cb0ee

Passage ID: `qasper-passage-v1-5bcd3538966d084245dacd4aa1eab04bde0d976b1efcbee8c093627b528cb0ee`; retrieval score: 5.554306831978875.

Word count: 250.

```text
to the database. Thus, it is a 1-to-n problem. Revision provenance is a 1-to-1 problem as it keeps track of detailed updates of one document BIBREF4 , BIBREF5 . Real-world applications include GitHub, version control in Microsoft Word and Wikipedia version trees BIBREF6 . In contrast, our system solves an n-to-n problem on a large scale. Our potential target data sources, such as the entire web or internal corpora in corporations, contain numerous original documents and their revisions. The aim is to find all revision document pairs within a reasonable time.

Document revision detection, plagiarism detection and revision provenance all rely on comparing the content of two documents and assessing a distance/similarity score. The classic document similarity measure, especially for plagiarism detection, is fingerprinting BIBREF7 , BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 . Fixed-length fingerprints are created using hash functions to represent document features and are then used to measure document similarities. However, the main purpose of fingerprinting is to reduce computation instead of improving accuracy, and it cannot capture word semantics. Another widely used approach is computing the sentence-to-sentence Levenshtein distance and assigning an overall score for every document pair BIBREF13 . Nevertheless, due to the large number of existing documents, as well as the large number of sentences in each document, the Levenshtein distance is not computation-friendly. Although alternatives such as the vector space model (VSM) can largely reduce the computation time, their effectiveness is low. More importantly, none of the above approaches can capture
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-f6f0f42c97e8b38623392e0ce450c07e0594019a7c43dd958aa0b74177380e31

Passage ID: `qasper-passage-v1-f6f0f42c97e8b38623392e0ce450c07e0594019a7c43dd958aa0b74177380e31`; retrieval score: 5.362469690086533.

Word count: 230.

```text
This paper has explored how DTW and TED can be extended with word2vec to construct semantic document distance measures: wDTW and wTED. By representing paragraphs with concatenations of word vectors, wDTW and wTED are able to capture the semantics of the words and thus give more accurate distance scores. In order to detect revisions, we have used minimum branching on an appropriately developed network with document distance scores serving as arc weights. We have also assessed the efficiency of the method of retrieving an optimal revision subnetwork by finding the minimum branching.

Furthermore, we have compared wDTW and wTED with several distance measures for revision detection tasks. Our results demonstrate the effectiveness and robustness of wDTW and wTED in the Wikipedia revision dumps and our simulated data sets. In order to reduce the computation time, we have computed document distances at the paragraph level and implemented a boosting learning system using Apache Spark. Although we have demonstrated the superiority of our semantic measures only in the revision detection experiments, wDTW and wTED can also be used as semantic distance measures in many clustering, classification tasks.

Our revision detection system can be enhanced with richer features such as author information and writing styles, and exact changes in revision pairs. Another interesting aspect we would like to explore in the future is reducing the complexities of calculating the distance between two paragraphs.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-2d6c849f472b96b536ead6837875252963ae5770ab2ebd0b4665251e873514f5

Passage ID: `qasper-passage-v1-2d6c849f472b96b536ead6837875252963ae5770ab2ebd0b4665251e873514f5`; retrieval score: 4.6293914306124355.

Word count: 172.

```text
Our system is a boosting learner that is composed of four modules: weak filter, strong filter, revision network and optimal subnetwork. First of all, we sort all documents by timestamps and pair up documents so that we only compare each document with documents that have been created earlier. In the first module, we calculate the VSM similarity scores for all pairs and eliminate those with scores that are lower than an empirical threshold ( INLINEFORM0 ). This is what we call the weak filter. After that, we apply the strong filter wDTW or wTED on the available pairs and filter out document pairs having distances higher than a threshold INLINEFORM1 . For VSM in Section SECREF32 , we directly filter out document pairs having similarity scores lower than a threshold INLINEFORM2 . The cut-off threshold estimation is explained in Section SECREF30 . The remaining document pairs from the strong filter are then sent to the revision network module. In the end, we output the optimal revision pairs following the minimum branching strategy.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-24fcbd2156e670c43c8d70e2693291f8a2b4a54cd46cd056f7db0db2ed9f7c97

Passage ID: `qasper-passage-v1-24fcbd2156e670c43c8d70e2693291f8a2b4a54cd46cd056f7db0db2ed9f7c97`; retrieval score: 4.194534693214248.

Word count: 250.

```text
We use precision, recall and F-measure to evaluate the detected revisions. A true positive case is a correctly identified revision. A false positive case is an incorrectly identified revision. A false negative case is a missed revision record.

We illustrate the performances of wDTW, wTED, WMD, VSM, PV-DTW and PV-TED on the Wikipedia revision dumps in Figure FIGREF43 . wDTW and wTED have the highest F-measure scores compared to the rest of four measures, and wDTW also have the highest precision and recall scores. Figure FIGREF49 shows the average evaluation results on the simulated data sets. From left to right, the corpus size increases and the revision chains become longer, thus it becomes more challenging to detect document revisions. Overall, wDTW consistently performs the best. WMD is slightly better than wTED. In particular, when the corpus size increases, the performances of WMD, VSM, PV-DTW and PV-TED drop faster than wDTW and wTED. Because the revision operations were randomly selected in each corpus, it is possible that there are non-monotone points in the series.

wDTW and wTED perform better than WMD especially when the corpus is large, because they use dynamic programming to find the global optimal alignment for documents. In contrast, WMD relies on a greedy algorithm that sums up the minimal cost for every word. wDTW and wTED perform better than PV-DTW and PV-TED, which indicates that our DistPara distance in Algorithm SECREF20 is more accurate than the Euclidian distance between paragraph vectors trained by PV.

We show in
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1709.01256:12:0` | full | 0:243 |

#### Rank 5: qasper-passage-v1-14da190c18ec7ba8e3a9f015539c219488ed94882eabd1628804daba235a0aac

Passage ID: `qasper-passage-v1-14da190c18ec7ba8e3a9f015539c219488ed94882eabd1628804daba235a0aac`; retrieval score: 3.9782506824778228.

Word count: 250.

```text
It is a common habit for people to keep several versions of documents, which creates duplicate data. A scholarly article is normally revised several times before being published. An academic paper may be listed on personal websites, digital conference libraries, Google Scholar, etc. In major corporations, a document typically goes through several revisions involving multiple editors and authors. Users would benefit from visualizing the entire history of a document. It is worthwhile to develop a system that is able to intelligently identify, manage and represent revisions. Given a collection of text documents, our study identifies revision relationships in a completely unsupervised way. For each document in a corpus we only use its content and the last modified timestamp. We assume that a document can be revised by many users, but that the documents are not merged together. We consider collaborative editing as revising documents one by one.

The two research problems that are most relevant to document revision detection are plagiarism detection and revision provenance. In a plagiarism detection system, every incoming document is compared with all registered non-plagiarized documents BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 . The system returns true if an original copy is found in the database; otherwise, the system returns false and adds the document to the database. Thus, it is a 1-to-n problem. Revision provenance is a 1-to-1 problem as it keeps track of detailed updates of one document BIBREF4 , BIBREF5 . Real-world applications include GitHub, version control in Microsoft Word and Wikipedia
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1152.

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

#### Rank 1: qasper-passage-v1-e73636c22c123aeb1c6b1fa328a433a68236c31194fbee74b377df5afc72cb54

Passage ID: `qasper-passage-v1-e73636c22c123aeb1c6b1fa328a433a68236c31194fbee74b377df5afc72cb54`; retrieval score: 2.8788236845807678.

Word count: 151.

```text
Table TABREF14 presents results for all models across the four variations of the dataset. First, BERT is consistently the best approach for in-scope, followed by MLP. Second, out-of-scope query performance is much lower than in-scope across all methods. Training on less data (Small and Imbalanced) yields models that perform slightly worse on in-scope queries. The trend is mostly the opposite when evaluating out-of-scope, where recall increases under the Small and Imbalanced training conditions. Under these two conditions, the size of the in-scope training set was decreased, while the number of out-of-scope training queries remained constant. This indicates that out-of-scope performance can be increased by increasing the relative number of out-of-scope training queries. We do just that in the OOS+ setting—where the models were trained on the full training set as well as 150 additional out-of-scope queries—and see that performance on out-of-scope increases substantially, yet still remains low relative to in-scope accuracy.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-9e09304cf9a66ad18656a9fa870e624a4029a25839fa41da466fa7a9a5556e09

Passage ID: `qasper-passage-v1-9e09304cf9a66ad18656a9fa870e624a4029a25839fa41da466fa7a9a5556e09`; retrieval score: 2.555432210634751.

Word count: 118.

```text
For all queries collected, all tokens were down-cased, and all end-of-sentence punctuation was removed. Additionally, all duplicate queries were removed and replaced.

In an effort to reduce bias in the in-scope data, we placed all queries from a given crowd worker in a single split (train, validation, or test). This avoids the potential issue of similar queries from a crowd worker ending up in both the train and test sets, for instance, which would make the train and test distributions unrealistically similar. We note that this is a recommendation from concurrent work by BIBREF3. We also used this procedure for the out-of-scope set, except that we split the data into train/validation/test based on task prompt instead of worker.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-8830385d1676f71dbc6943fbb124b68a4368a09f48d3ab7c0547cf18d1de46f3

Passage ID: `qasper-passage-v1-8830385d1676f71dbc6943fbb124b68a4368a09f48d3ab7c0547cf18d1de46f3`; retrieval score: 2.1304071173952446.

Word count: 212.

```text
We use three baseline approaches for the task of predicting whether a query is out-of-scope: (1) oos-train, where we train an additional (i.e. 151st) intent on out-of-scope training data; (2) oos-threshold, where we use a threshold on the classifier's probability estimate; and (3) oos-binary, a two-stage process where we first classify a query as in- or out-of-scope, then classify it into one of the 150 intents if classified as in-scope.

To reduce the severity of the class imbalance between in-scope versus out-of-scope query samples (i.e., 15,000 versus 250 queries for OOS+), we investigate two strategies when using oos-binary: one where we undersample the in-scope data and train using 1,000 in-scope queries sampled evenly across all intents (versus 250 out-of-scope), and another where we augment the 250 OOS+ out-of-scope training queries with 14,750 sentences sampled from Wikipedia.

From a development point of view, the oos-train and oos-binary methods both require careful curation of an out-of-scope training set, and this set can be tailored to individual systems. The oos-threshold method is a more general decision rule that can be applied to any model that produces a probability. In our evaluation, the out-of-scope threshold was chosen to be the value which yielded the highest validation score across all intents, treating out-of-scope as its own intent.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-f0f66146047535d54d2953f5fe716f3c6f9c5f8dec0c77d97d9c9e22003aab56

Passage ID: `qasper-passage-v1-f0f66146047535d54d2953f5fe716f3c6f9c5f8dec0c77d97d9c9e22003aab56`; retrieval score: 1.8575066468457728.

Word count: 250.

```text
In most other analyses and datasets, the idea of out-of-scope data is not considered, and instead the output classes are intended to cover all possible queries (e.g., TREC BIBREF7). Recent work by BIBREF8 considers a similar problem they call out-of-distribution detection. They use other datasets or classes excluded during training to form the out-of-distribution samples. This means that the out-of-scope samples are from a small set of coherent classes that differ substantially from the in-distribution samples. Similar experiments were conducted for evaluating unknown intent discovery models in BIBREF9. In contrast, our out-of-scope queries cover a broad range of phenomena and are similar in style and often similar in topic to in-scope queries, representing things a user might say given partial knowledge of the capabilities of a system.

Table TABREF20 compares our dataset with other short-query intent classification datasets. The Snips BIBREF0 dataset and the dataset presented in BIBREF10 are the most similar to the in-scope part of our work, with the same type of conversational agent requests. Like our work, both of these datasets were bootstrapped using crowdsourcing. However, the Snips dataset has only a small number of intents and an enormous number of examples of each. Snips does present a low-data variation, with 70 training queries per intent, in which performance drops slightly. The dataset presented in BIBREF10 has a large number of intent classes, yet also contains a wide range of samples per intent class (ranging from 24 to 5,981 queries per intent, and so is not constrained
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-639dcc67d09fed5854db74590826750a9b2e9768a7a215846c90672be9fba3c4

Passage ID: `qasper-passage-v1-639dcc67d09fed5854db74590826750a9b2e9768a7a215846c90672be9fba3c4`; retrieval score: 1.813960604777695.

Word count: 38.

```text
We introduce a new crowdsourced dataset of 23,700 queries, including 22,500 in-scope queries covering 150 intents, which can be grouped into 10 general domains. The dataset also includes 1,200 out-of-scope queries. Table TABREF2 shows examples of the data.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 769.

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

#### Rank 1: qasper-passage-v1-7569f2ad224ea8d03a6d9880d434e6046daf244b0db82c3f495b686bd53fc1b6

Passage ID: `qasper-passage-v1-7569f2ad224ea8d03a6d9880d434e6046daf244b0db82c3f495b686bd53fc1b6`; retrieval score: 3.728237148791819.

Word count: 173.

```text
data sources. We show that our approach, despite the lack of hand-engineered, language-specific features, obtains state-of-the-art results in 7 datasets for 6 languages on the ABSA benchmarks BIBREF4 , BIBREF5 , BIBREF6 .

The main contribution of this research note is providing an extension or addendum to previous work on sequence labelling BIBREF7 by reporting additional experimental results as well as further insights on the performance of our model across languages on a different NLP task such as Opinion Target Extraction (OTE). Thus, we empirically demonstrate the validity and strong performance of our approach for six languages in seven different datasets of the restaurant domain. Every experiment and result presented in this note is novel.

In this sense, we show that our approach is not only competitive across languages and domains for Named Entity Recognition, as shown by BIBREF7 , but that it can be straightforwardly adapted to different tasks and domains such as OTE. Furthermore, we release the system and every model trained for public use and to facilitate reproducibility of results.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-99cb9c60babb329091bf541895c26fdf3ff5815e54a9cbc70310023b520f14e2

Passage ID: `qasper-passage-v1-99cb9c60babb329091bf541895c26fdf3ff5815e54a9cbc70310023b520f14e2`; retrieval score: 2.3707595171790903.

Word count: 250.

```text
We trained our system for 5 other languages on the ABSA 2016 datasets, using the same strategy as for English. We choose the best Clark-Word2vec combination (with and without Brown clusters) via 5-cross validation on the training data. The features are exactly the same as those used for English, the only change is the data on which the clusters are trained. Table TABREF19 reports on the detailed results obtained for each of the languages. In bold we show the best model chosen via 5-fold CV. Moreover, we also show the best models using only one of each of the clustering features.

The first difference with respect to the English results is that the Brown clustering features are, in three out of five settings, detrimental to performance. Second, that combining clustering features is only beneficial for Spanish. Third, the overall results are in general lower than those obtained in the 2016 English data. Finally, the difference between the best results and the results using the Local features is lower than for English, even though the Local results are similar to those obtained with the English datasets (except for Turkish, but this is due to the significantly smaller size of the data, as shown in Table TABREF7 ).

We believe that all these four issues are caused, at least partially, by the lack of domain-specific clustering features used for the multilingual experiments. In other words, while for the English experiments we leveraged the Yelp dataset to train the clustering algorithms, in the
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-d4cf5a67070747b491a2d9b15e46cb999fe817a245b1500e938e28af12539a9d

Passage ID: `qasper-passage-v1-d4cf5a67070747b491a2d9b15e46cb999fe817a245b1500e938e28af12539a9d`; retrieval score: 2.106413233207855.

Word count: 146.

```text
In this section we report on the experiments performed using the system and data described above. First we will present the English results for the three ABSA editions as well as a comparison with previous work. After that we will do the same for 5 additional languages included in the ABSA 2016 edition: Dutch, French, Russian, Spanish and Turkish. The local and clustering features, as described in Section SECREF11 , are the same for every language and evaluation setting. The only change is the clustering lexicons used for the different languages. As stated in section SECREF11 , the best cluster combination is chosen via 5-fold cross validation (CV) on the training data. We first try every permutation with the Clark and Word2vec clusters. Once the best combination is obtained, we then try with the Brown clusters obtaining thus the final model for each language and dataset.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1901.09755:7:0` | full | 0:884 |

#### Rank 4: qasper-passage-v1-68f702aa072aa57901d5bbd6b183d6f6aa21bb26f6ee817d5bf23dd9db4c2b2d

Passage ID: `qasper-passage-v1-68f702aa072aa57901d5bbd6b183d6f6aa21bb26f6ee817d5bf23dd9db4c2b2d`; retrieval score: 2.076246950517511.

Word count: 243.

```text
In this research note we provide additional empirical experimentation to BIBREF7 , reporting best results for Opinion Target Extraction for 6 languages and 7 datasets using the same set of simple, shallow and language independent features. Furthermore, the results provide some interesting insights with respect to the use of clusters to inject external knowledge via semi-supervised features.

First, Brown clusters are particularly beneficial when trained on domain-related data. This seems to be the case in the multilingual setting, where the Brown clusters (trained on out-of-domain Wikipedia data) worsen the system's performance for every language except for Turkish.

Second, the results also show that Clark and Word2vec improve results in general, even if induced on out-of-domain data. Thirdly, for best performance it is convenient to combine clusters obtained from diverse data sources, both from in- and out-of-domain corpora.

Finally, the results indicate that, even when the amount of training data is small, such as in the 2015 and 2016 English benchmarks, our system's performance remains competitive thanks to the combination of clustering features. This, together with the lack of linguistic features, facilitates the easy and fast development of systems for new domains or languages. These considerations thus confirm the hypotheses stated in BIBREF7 with respect to the use of clustering features to obtain robust sequence taggers across languages and tasks.

The system and models for every language and dataset are available as part of the ixa-pipe-opinion module for public use and reproducibility of results.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-ac32cc832f80728a4881be99cc74549cc0b3fd1a45f4751ba2704a1655c76738

Passage ID: `qasper-passage-v1-ac32cc832f80728a4881be99cc74549cc0b3fd1a45f4751ba2704a1655c76738`; retrieval score: 1.9183111449154882.

Word count: 250.

```text
that for English the Yelp dataset is used whereas for the rest of languages the clusters are induced using the Wikipedia, effectively an out-of-domain corpus. The exception is Turkish, for which a 6 point gain in F1 score is obtained, but we believe that is probably due to the small size of the training data used for training the Local model.

In contrast, Word2vec clusters clearly benefit from larger amounts of data, as illustrated by the best English Word2vec model being the one trained using the Wikipedia, and not the Yelp dataset, which is closer to the application domain. Finally, the Clark algorithm seems to be the most versatile as it consistently outperforms the other two clustering methods in 4 out of the 8 evaluation settings presented.

Summarizing: (i) Brown clusters perform better when leveraged from source data close to the application domain, even if small in size; (ii) Clark clusters are the most robust of the three with respect to the size and domain of the data used; and (iii) for Word2vec size is the crucial factor. The larger the source data the better the performance. Thus, instead of choosing over one clustering type or the other, our system provides a method to effectively combining them, depending on the data sources available, to obtain robust and language independent sequence labelling systems.

Finally, results show that our models are particularly competitive when the amount of training data available is small, allowing us to compete with more complex systems including also
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1062.

Fully covered answer annotations: 91ea275060a44b2fa896afa9991282a4390606b4.

Missing evidence by answer annotation:

```text
{
  "91ea275060a44b2fa896afa9991282a4390606b4": {
    "unresolved_evidence": [],
    "paragraphs": {}
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

#### Rank 1: qasper-passage-v1-2863d4869f3d085398d227b67d847efa093afc059f74686d75602b13fd106fac

Passage ID: `qasper-passage-v1-2863d4869f3d085398d227b67d847efa093afc059f74686d75602b13fd106fac`; retrieval score: 3.0873946751683476.

Word count: 153.

```text
tags as well as the list of expected tags from the test set. Finally, we use the cosine similarity measure to calculate how semantically similar these two lists are.

Recommendation diversity. As defined in BIBREF18 , we calculate recommendation diversity as the average dissimilarity of all pairs of tags in the list of recommended tags. Thus, given a distance function INLINEFORM0 that corresponds to the dissimilarity between two tags INLINEFORM1 and INLINEFORM2 in the list of recommended tags, INLINEFORM3 is given as the average dissimilarity of all pairs of tags: DISPLAYFORM0

where INLINEFORM0 is the number of evaluated e-books and the dissimilarity function is defined as INLINEFORM1 . In our experiments, we use the previously trained Doc2Vec model to extract the latent representation of a specific tag. The similarity of two tags INLINEFORM2 is then calculated with the Cosine similarity measure using the latent vector representations of respective tags INLINEFORM3 and INLINEFORM4 .
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.04042:6:8` | full | 0:416 |

#### Rank 2: qasper-passage-v1-51eb368cd5b54b1c08673477e550af751c109b3ff59ccee4e97ff1f7525f31fb

Passage ID: `qasper-passage-v1-51eb368cd5b54b1c08673477e550af751c109b3ff59ccee4e97ff1f7525f31fb`; retrieval score: 2.721810783739113.

Word count: 250.

```text
tags from another source, this can be problematic. For example, if we recommend the tag “victim” but expect the tag “prey”, we would mark this as a mismatch, therefore being a bad recommendation. But if we know that the corresponding e-book is a crime novel, the recommended tag would be (semantically) descriptive to reflect the book's content. Hence, in this paper, we propose to additionally measure the semantic similarity between recommended tags and tags from the test set (i.e., the Amazon review keywords).

Over the last four years, there have been several notable publications in the area of applying deep learning to uncover semantic relationships between textual content (e.g., by learning word embeddings with Word2Vec BIBREF16 , BIBREF17 ). Based on this, we propose an alternative measure of recommendation quality by learning the semantic relationships from both vocabularies and then using it to compare how semantically similar the recommended tags are to the expected review keywords. For this, we first extract the textual content in the form of the description text, title, editor tags and Amazon search terms of e-books from our dataset. We then train a Doc2Vec BIBREF7 model on the content. Then, we use the model to infer the latent representation for both the complete list of recommended tags as well as the list of expected tags from the test set. Finally, we use the cosine similarity measure to calculate how semantically similar these two lists are.

Recommendation diversity. As defined in BIBREF18 , we calculate recommendation diversity
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.04042:6:8` | partial | 0:88 |

#### Rank 3: qasper-passage-v1-cfb3492f4139b9befa7aa23ae287a0ed4a0e29053200a0041cc73f81b50f8b08

Passage ID: `qasper-passage-v1-cfb3492f4139b9befa7aa23ae287a0ed4a0e29053200a0041cc73f81b50f8b08`; retrieval score: 2.6988214821899104.

Word count: 145.

```text
evaluation comprises of a rich set of 19 different algorithms to recommend tags for e-books, which we group into (i) popularity-based, (ii) similarity-based (i.e., using content information), and (iii) hybrid approaches. We evaluate our approaches in terms of accuracy, semantic similarity and diversity on the review content of Amazon users, which reflects the readers' vocabulary. With semantic similarity, we measure how semantically similar (based on learned Doc2Vec BIBREF7 embeddings) the list of recommended tags is to the list of relevant tags. We use this additional metric to measure not only exact “hits” of our recommendations but also semantic matches.

Our evaluation results show that combining both data sources enhances the quality of tag recommendations for annotating e-books. Furthermore, approaches that solely train on Amazon search terms provide poor performance in terms of accuracy but deliver good results in terms of semantic similarity and recommendation diversity.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-ce908c73d3401a557e591d6b9f6a1b7d2ef7c5c966ddac89b6b4cbfca08e913a

Passage ID: `qasper-passage-v1-ce908c73d3401a557e591d6b9f6a1b7d2ef7c5c966ddac89b6b4cbfca08e913a`; retrieval score: 2.5448871545315503.

Word count: 250.

```text
In this work, we measure (i) recommendation accuracy, (ii) semantic similarity, and (iii) recommendation diversity to evaluate the quality of our approaches from different perspectives.

Recommendation accuracy. We use Normalized Discounted Cumulative Gain (nDCG) BIBREF15 to measure the accuracy of the tag recommendation approaches. The nDCG measure is a standard ranking-dependent metric that not only measures how many tags can be correctly predicted but also takes into account their position in the recommendation list with length of INLINEFORM0 . It is based on the Discounted Cummulative Gain, which is given by: DISPLAYFORM0

where INLINEFORM0 is a function that returns 1 if the recommended tag at position INLINEFORM1 in the recommended list is relevant. We then calculate DCG@ INLINEFORM2 for every evaluated e-book by dividing DCG@ INLINEFORM3 with the ideal DCG value iDCG@ INLINEFORM4 , which is the highest possible DCG value that can be achieved if all the relevant tags would be recommended in the correct order. It is given by the following formula BIBREF15 : DISPLAYFORM0

Semantic similarity. One precondition of standard recommendation accuracy measures is that to generate a “hit”, the recommended tag needs to be an exact syntactical match to the one from the test set. When tags are recommended from one data source and compared to tags from another source, this can be problematic. For example, if we recommend the tag “victim” but expect the tag “prey”, we would mark this as a mismatch, therefore being a bad recommendation. But if we know that the corresponding
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-93cdde8d00e34aba6f880cebc704a0b4bffb2dc4048b34c8ac7631349dcb8ee8

Passage ID: `qasper-passage-v1-93cdde8d00e34aba6f880cebc704a0b4bffb2dc4048b34c8ac7631349dcb8ee8`; retrieval score: 1.6409599307606855.

Word count: 67.

```text
performance concerning INLINEFORM4 but provide a good performance regarding semantic similarity could still be helpful for annotating e-books.

Recommendation diversity. Figure FIGREF16 shows the diversity of the tag recommendation approaches. We achieve the highest diversity with the similarity-based approaches, which extract Amazon search terms. Their accuracy is, however, very low. Thus, the combination of the two vocabularies can provide a good trade-off between recommendation accuracy and diversity.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 865.

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

#### Rank 1: qasper-passage-v1-6eafc84dddd245b365d9897de051c788f118cba707184ecdd07a7ada6e29afcf

Passage ID: `qasper-passage-v1-6eafc84dddd245b365d9897de051c788f118cba707184ecdd07a7ada6e29afcf`; retrieval score: 5.418266343738948.

Word count: 211.

```text
We compare the proposed approach for translating natural language instructions into a navigation plan against alternative deep-learning models:

[align=left,leftmargin=0em,labelsep=0.4em,font=]

The baseline approach is based on BIBREF20 . It divides the task of interpreting commands for behavioral navigation into two steps: path generation, and path verification. For path generation, this baseline uses a standard sequence-to-sequence model augmented with an attention mechanism, similar to BIBREF23 , BIBREF6 . For path verification, the baseline uses depth-first search to find a route in the graph that matches the sequence of predicted behaviors. If no route matches perfectly, the baseline changes up to three behaviors in the predicted sequence to try to turn it into a valid path.

To test the impact of using the behavioral graphs as an extra input to our translation model, we implemented a version of our approach that only takes natural language instructions as input. In this ablation model, the output of the bidirectional GRU that encodes the input instruction INLINEFORM0 is directly fed to the decoder layer. This model does not have the attention and FC layers described in Sec. SECREF4 , nor uses the masking function in the output layer.

This model is the same as the previous Ablation model, but with the masking function in the output layer.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-810587f146423338f0f6eeb0595f6362dcf68b94eb756a2e93e45da4d5f6db9d

Passage ID: `qasper-passage-v1-810587f146423338f0f6eeb0595f6362dcf68b94eb756a2e93e45da4d5f6db9d`; retrieval score: 4.767391796752594.

Word count: 250.

```text
This section discusses qualitative results to better understand how the proposed model uses the navigation graph.

We analyze the evolution of the attention weights INLINEFORM0 in Eq. () to assess if the decoder layer of the proposed model is attending to the correct parts of the behavioral graph when making predictions. Fig FIGREF33 (b) shows an example of the resulting attention map for the case of a correct prediction. In the Figure, the attention map is depicted as a scaled and normalized 2D array of color codes. Each column in the array shows the attention distribution INLINEFORM1 used to generate the predicted output at step INLINEFORM2 . Consequently, each row in the array represents a triplet in the corresponding behavioral graph. This graph consists of 72 triplets for Fig FIGREF33 (b).

We observe a locality effect associated to the attention coefficients corresponding to high values (bright areas) in each column of Fig FIGREF33 (b). This suggests that the decoder is paying attention to graph triplets associated to particular neighborhoods of the environment in each prediction step. We include additional attention visualizations in the supplementary Appendix, including cases where the dynamics of the attention distribution are harder to interpret.

All the routes in our dataset are the shortest paths from a start location to a given destination. Thus, we collected a few additional natural language instructions to check if our model was able to follow navigation instructions describing sub-optimal paths. One such example is shown in Fig. FIGREF37 , where the
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-046e0b5ca45eb99c8cbbaf4151aa9e7054c91fd81b32519276248430318293f5

Passage ID: `qasper-passage-v1-046e0b5ca45eb99c8cbbaf4151aa9e7054c91fd81b32519276248430318293f5`; retrieval score: 4.563571474707191.

Word count: 250.

```text
Table TABREF28 shows the performance of the models considered in our evaluation on both test sets. The next two sections discuss the results in detail.

First, we can observe that the final model “Ours with Mask and Ordered Triplets” outperforms the Baseline and Ablation models on all metrics in previously seen environments. The difference in performance is particularly evident for the Exact Match and Goal Match metrics, with our model increasing accuracy by 35% and 25% in comparison to the Baseline and Ablation models, respectively. These results suggest that providing the behavioral navigation graph to the model and allowing it to process this information as a knowledge base in an end-to-end fashion is beneficial.

We can also observe from Table TABREF28 that the masking function of Eq. ( EQREF12 ) tends to increase performance in the Test-Repeated Set by constraining the output sequence to a valid set of navigation behaviors. For the Ablation model, using the masking function leads to about INLINEFORM0 increase in EM and GM accuracy. For the proposed model (with or without reordering the graph triplets), the increase in accuracy is around INLINEFORM1 . Note that the impact of the masking function is less evident in terms of the F1 score because this metric considers if a predicted behavior exists in the ground truth navigation plan, irrespective of its specific position in the output sequence.

The results in the last four rows of Table TABREF28 suggest that ordering the graph triplets can facilitate predicting correct navigation plans
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1810.00663:10:1` | full | 0:572 |

#### Rank 4: qasper-passage-v1-947d55e01e23414dd5fa66cf21da3ab2555f25ecbf2293282e4a7d18128b3f38

Passage ID: `qasper-passage-v1-947d55e01e23414dd5fa66cf21da3ab2555f25ecbf2293282e4a7d18128b3f38`; retrieval score: 4.360058284060429.

Word count: 250.

```text
INLINEFORM5 , and INLINEFORM6 ( INLINEFORM7 ) the INLINEFORM8 -th row of INLINEFORM9 . We use each encoded triplet INLINEFORM10 in INLINEFORM11 to calculate its associated attention distribution INLINEFORM12 over all the atomic instructions INLINEFORM13 : DISPLAYFORM0

where the matrix INLINEFORM0 serves to combine the different sources of information INLINEFORM1 and INLINEFORM2 . Each component INLINEFORM3 of the attention distributions INLINEFORM4 quantifies the affinity between the INLINEFORM5 -th triplet in INLINEFORM6 and the INLINEFORM7 -th word in the corresponding input INLINEFORM8 .

The model then uses each attention distribution INLINEFORM0 to obtain a weighted sum of the encodings of the words in INLINEFORM1 , according to their relevance to the corresponding triplet INLINEFORM2 . This results in L attention vectors INLINEFORM3 , INLINEFORM4 .

The final step in the attention layer concatenates each INLINEFORM0 with INLINEFORM1 to generate the outputs INLINEFORM2 , INLINEFORM3 . Following BIBREF8 , we include the encoded triplet INLINEFORM4 in the output tensor INLINEFORM5 of this layer to prevent early summaries of relevant map information.

FC layer: The model reduces the dimensionality of each individual vector INLINEFORM0 from INLINEFORM1 to INLINEFORM2 with a fully-connected (FC) layer. The resulting L vectors are output to the next layer as columns of a context matrix INLINEFORM3 .

Decoder layer: After the FC layer, the model predicts likelihoods over the sequence of behaviors that correspond to the input instructions with a GRU network. Without loss of generality, consider the INLINEFORM0 -th recurrent cell in the GRU network. This cell takes
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-499ec982bcbc232b2a500ec4e5b03178ed14c463616333e86550d23c8b2b5046

Passage ID: `qasper-passage-v1-499ec982bcbc232b2a500ec4e5b03178ed14c463616333e86550d23c8b2b5046`; retrieval score: 4.193739542823035.

Word count: 250.

```text
and edges in INLINEFORM10 , respectively.

Encoder layer: The model then uses two bidirectional Gated Recurrent Units (GRUs) BIBREF25 to independently process the information from INLINEFORM0 and INLINEFORM1 , and incorporate contextual cues from the surrounding embeddings in each sequence. The outputs of the encoder layer are the matrix INLINEFORM2 for the navigational commands and the matrix INLINEFORM3 for the behavioral graph, where INLINEFORM4 is the hidden size of each GRU, INLINEFORM5 is the number of words in the instruction INLINEFORM6 , and INLINEFORM7 is the number of triplets in the graph INLINEFORM8 .

Attention layer: Matrices INLINEFORM0 and INLINEFORM1 generated by the encoder layer are combined using an attention mechanism. We use one-way attention because the graph contains information about the whole environment, while the instruction has (potentially incomplete) local information about the route of interest. The use of attention provides our model with a two-step strategy to interpret commands. This resembles the way people find paths on a map: first, relevant parts on the map are selected according to their affinity to each of the words in the input instruction (attention layer); second, the selected parts are connected to assemble a valid path (decoder layer). More formally, let INLINEFORM2 ( INLINEFORM3 ) be the INLINEFORM4 -th row of INLINEFORM5 , and INLINEFORM6 ( INLINEFORM7 ) the INLINEFORM8 -th row of INLINEFORM9 . We use each encoded triplet INLINEFORM10 in INLINEFORM11 to calculate its associated attention distribution INLINEFORM12 over all the atomic instructions INLINEFORM13 : DISPLAYFORM0

where the matrix
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 1211.

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

#### Rank 1: qasper-passage-v1-c6adfeda9f3c6048e0801edaa468b32c7b13df23140cf557a8cf02ebdd8118eb

Passage ID: `qasper-passage-v1-c6adfeda9f3c6048e0801edaa468b32c7b13df23140cf557a8cf02ebdd8118eb`; retrieval score: 7.67772289921951.

Word count: 250.

```text
dataset.

Prediction with Visual Imagery:

Inspired by BIBREF56 's approach for facial landmark localization, we use their pretrained CNN consisting of convolutional layers, including unshared and fully-connected layers, to predict gender and age from both the profile and shared images. We evaluate the performance for gender and age prediction task on INLINEFORM0 and INLINEFORM1 respectively as shown in Table TABREF42 and Table TABREF44 .

Demographic Prediction Analysis:

We delve deeper into the benefits and drawbacks of each data modality for demographic information prediction. This is crucial as the differences between language cues between age groups above age 35 tend to become smaller (see Figure FIGREF39 -A,B,C) and making the prediction harder for older people BIBREF74 . In this case, the other data modality (e.g., visual content) can play integral role as a complementary source for age inference. For gender prediction (see Table TABREF44 ), on average, the profile image-based predictor provides a more accurate prediction for both the depressed and control class (0.92 and 0.90) compared to content-based predictor (0.82). For age prediction (see Table TABREF42 ), textual content-based predictor (on average 0.60) outperforms both of the visual-based predictors (on average profile:0.51, Media:0.53).

However, not every user provides facial identity on his account (see Table TABREF21 ). We studied facial presentation for each age-group to examine any association between age-group, facial presentation and depressive behavior (see Table TABREF43 ). We can see youngsters in both depressed and control class are not likely to present their face on profile image. Less
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-fd65197da1dd8a7e0cb1b2a8258cc0cb5b9f8c45134a7d09692de8e3158de020

Passage ID: `qasper-passage-v1-fd65197da1dd8a7e0cb1b2a8258cc0cb5b9f8c45134a7d09692de8e3158de020`; retrieval score: 7.584761399622599.

Word count: 250.

```text
We now provide an in-depth analysis of visual and textual content of vulnerable users.

Visual Content Analysis: We show that the visual content in images from posts as well as profiles provide valuable psychological cues for understanding a user's depression status. Profile/posted images can surface self-stigmatization BIBREF53 . Additionally, as opposed to typical computer vision framework for object recognition that often relies on thousands of predetermined low-level features, what matters more for assessing user's online behavior is the emotions reflected in facial expressions BIBREF54 , attributes contributing to the computational aesthetics BIBREF55 , and sentimental quotes they may subscribe to (Figure FIGREF15 ) BIBREF8 .

Facial Presence:

For capturing facial presence, we rely on BIBREF56 's approach that uses multilevel convolutional coarse-to-fine network cascade to tackle facial landmark localization. We identify facial presentation, emotion from facial expression, and demographic features from profile/posted images . Table TABREF21 illustrates facial presentation differences in both profile and posted images (media) for depressed and control users in INLINEFORM0 . With control class showing significantly higher in both profile and media (8%, 9% respectively) compared to that for the depressed class. In contrast with age and gender disclosure, vulnerable users are less likely to disclose their facial identity, possibly due to lack of confidence or fear of stigma.

Facial Expression:

Following BIBREF8 's approach, we adopt Ekman's model of six emotions: anger, disgust, fear, joy, sadness and surprise, and use the Face++ API to automatically capture them from the shared images. Positive emotions are joy
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-86bcfa8f05a6563271ad22419b39f49f915c11de8bebf072022f3e55add73f6b

Passage ID: `qasper-passage-v1-86bcfa8f05a6563271ad22419b39f49f915c11de8bebf072022f3e55add73f6b`; retrieval score: 5.872970455951516.

Word count: 250.

```text
We leverage both the visual and textual content for predicting age and gender.

Prediction with Textual Content:

We employ BIBREF73 's weighted lexicon of terms that uses the dataset of 75,394 Facebook users who shared their status, age and gender. The predictive power of this lexica was evaluated on Twitter, blog, and Facebook, showing promising results BIBREF73 . Utilizing these two weighted lexicon of terms, we are predicting the demographic information (age or gender) of INLINEFORM0 (denoted by INLINEFORM1 ) using following equation: INLINEFORM2

where INLINEFORM0 is the lexicon weight of the term, and INLINEFORM1 represents the frequency of the term in the user generated INLINEFORM2 , and INLINEFORM3 measures total word count in INLINEFORM4 . As our data is biased toward young people, we report age prediction performance for each age group separately (Table TABREF42 ). Moreover, to measure the average accuracy of this model, we build a balanced dataset (keeping all the users above 23 -416 users), and then randomly sampling the same number of users from the age ranges (11,19] and (19,23]. The average accuracy of this model is 0.63 for depressed users and 0.64 for control class. Table TABREF44 illustrates the performance of gender prediction for each class. The average accuracy is 0.82 on INLINEFORM5 ground-truth dataset.

Prediction with Visual Imagery:

Inspired by BIBREF56 's approach for facial landmark localization, we use their pretrained CNN consisting of convolutional layers, including unshared and fully-connected layers, to predict gender and age from both the profile and shared images.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-7a7412cf1eeb6301b7b2b1a6d2ee6b55df302972399c66bf1f64540a8b904cad

Passage ID: `qasper-passage-v1-7a7412cf1eeb6301b7b2b1a6d2ee6b55df302972399c66bf1f64540a8b904cad`; retrieval score: 5.706886373794651.

Word count: 250.

```text
TABREF48 illustrates our multimodal framework outperform the baselines for identifying depressed users in terms of average specificity, sensitivity, F-Measure, and accuracy in 10-fold cross-validation setting on INLINEFORM1 dataset. Figure FIGREF47 shows how the likelihood of being classified into the depressed class varies with each feature addition to the model for a sample user in the dataset. The prediction bar (the black bar) shows that the log-odds of prediction is 0.31, that is, the likelihood of this person being a depressed user is 57% (1 / (1 + exp(-0.3))). The figure also sheds light on the impact of each contributing feature. The waterfall charts represent how the probability of being depressed changes with the addition of each feature variable. For instance, the "Analytic thinking" of this user is considered high 48.43 (Median:36.95, Mean: 40.18) and this decreases the chance of this person being classified into the depressed group by the log-odds of -1.41. Depressed users have significantly lower "Analytic thinking" score compared to control class. Moreover, the 40.46 "Clout" score is a low value (Median: 62.22, Mean: 57.17) and it decreases the chance of being classified as depressed. With respect to the visual features, for instance, the mean and the median of 'shared_colorfulness' is 112.03 and 113 respectively. The value of 136.71 would be high; thus, it decreases the chance of being depressed for this specific user by log-odds of -0.54. Moreover, the 'profile_naturalness' of 0.46 is considered high compared to 0.36 as the mean for the depressed class which justifies
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-73f83210a2ca2a738296366f640af63351d70b7558763d881672109805c8ab7b

Passage ID: `qasper-passage-v1-73f83210a2ca2a738296366f640af63351d70b7558763d881672109805c8ab7b`; retrieval score: 5.31391393973782.

Word count: 250.

```text
a few attempts BIBREF3 , BIBREF4 , BIBREF5 , BIBREF6 , these investigations have seldom studied extraction of emotional state from visual content of images in posted/profile images. Visual content can express users' emotions more vividly, and psychologists noted that imagery is an effective medium for communicating difficult emotions.

According to eMarketer, photos accounted for 75% of content posted on Facebook worldwide and they are the most engaging type of content on Facebook (87%). Indeed, "a picture is worth a thousand words" and now "photos are worth a million likes." Similarly, on Twitter, the tweets with image links get twice as much attention as those without , and video-linked tweets drive up engagement . The ease and naturalness of expression through visual imagery can serve to glean depression-indicators in vulnerable individuals who often seek social support through social media BIBREF7 . Further, as psychologist Carl Rogers highlights, we often pursue and promote our Ideal-Self . In this regard, the choice of profile image can be a proxy for the online persona BIBREF8 , providing a window into an individual's mental health status. For instance, choosing emaciated legs of girls covered with several cuts as profile image portrays negative self-view BIBREF9 .

Inferring demographic information like gender and age can be crucial for stratifying our understanding of population-level epidemiology of mental health disorders. Relying on electronic health records data, previous studies explored gender differences in depressive behavior from different angles including prevalence, age at onset, comorbidities, as well as biological and
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1250.

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

#### Rank 1: qasper-passage-v1-5751b5f6c74dae61eda5c9f18208ccc68136d46b46dbbf2f07ac7c44e18ded32

Passage ID: `qasper-passage-v1-5751b5f6c74dae61eda5c9f18208ccc68136d46b46dbbf2f07ac7c44e18ded32`; retrieval score: 4.502201455198708.

Word count: 177.

```text
E17-1101 showed that given input with author traits like gender, it is possible to retain those traits in Statistical Machine Translation (SMT) models. W17-4727 showed that incorporating morphological analysis in the decoder improves NMT performance for morphologically rich languages. burlot:hal-01618387 presented a new protocol for evaluating the morphological competence of MT systems, indicating that current translation systems only manage to capture some morphological phenomena correctly. Regarding the application of constraints in NMT, N16-1005 presented a method for controlling the politeness level in the generated output. DBLP:journals/corr/FiclerG17aa showed how to guide a neural text generation system towards style and content parameters like the level of professionalism, subjective/objective, sentiment and others. W17-4811 showed that incorporating more context when translating subtitles can improve the coherence of the generated translations. Most closely to our work, vanmassenhove-hardmeier-way:2018:EMNLP also addressed the missing gender information by training proprietary models with a gender-indicating-prefix. We differ from this work by treating the problem in a black-box manner, and by addressing additional information like the number of the speaker and the gender and number of the audience.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-8c677ea0ba9187d006c76ab347fe88c38f0a538ce7798d03c3ac01fe25a97d30

Passage ID: `qasper-passage-v1-8c677ea0ba9187d006c76ab347fe88c38f0a538ce7798d03c3ac01fe25a97d30`; retrieval score: 3.058999884801701.

Word count: 102.

```text
Closely related to our work, vanmassenhove-hardmeier-way:2018:EMNLP proposed a method and an English-French test set to evaluate gender-aware translation, based on the Europarl corpus BIBREF7 . We evaluate our method (using Google Translate and the given prefixes) on their test set to see whether it is applicable to another language pair and domain. Table shows the results of our approach vs. their published results and the Google Translate baseline. As may be expected, Google Translate outperforms their system as it is trained on a different corpus and may use more complex machine translation models. Using our method improves the BLEU score even further.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-87e5e3083fcece0f508b82ce865d6c8250c449d1ab062016894062802431b948

Passage ID: `qasper-passage-v1-87e5e3083fcece0f508b82ce865d6c8250c449d1ab062016894062802431b948`; retrieval score: 2.6679658127628727.

Word count: 250.

```text
A common way for marking information about gender, number, and case in language is morphology, or the structure of a given word in the language. However, different languages mark such information in different ways – for example, in some languages gender may be marked on the head word of a syntactic dependency relation, while in other languages it is marked on the dependent, on both, or on none of them BIBREF0 . This morphological diversity creates a challenge for machine translation, as there are ambiguous cases where more than one correct translation exists for the same source sentence. For example, while the English sentence “I love language” is ambiguous with respect to the gender of the speaker, Hebrew marks verbs for the gender of their subject and does not allow gender-neutral translation. This allows two possible Hebrew translations – one in a masculine and the other in a feminine form. As a consequence, a sentence-level translator (either human or machine) must commit to the gender of the speaker, adding information that is not present in the source. Without additional context, this choice must be done arbitrarily by relying on language conventions, world knowledge or statistical (stereotypical) knowledge.

Indeed, the English sentence “I work as a doctor” is translated into Hebrew by Google Translate using the masculine verb form oved, indicating a male speaker, while “I work as a nurse” is translated with the feminine form ovedet, indicating a female speaker (verified on March 2019). While this is still an issue,
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-848c13b70f61370ccd33c230c820a9ad465727ded3f63c4899595e0d5b3ed1b3

Passage ID: `qasper-passage-v1-848c13b70f61370ccd33c230c820a9ad465727ded3f63c4899595e0d5b3ed1b3`; retrieval score: 2.4474190440224213.

Word count: 250.

```text
by Google Translate using the masculine verb form oved, indicating a male speaker, while “I work as a nurse” is translated with the feminine form ovedet, indicating a female speaker (verified on March 2019). While this is still an issue, there have been recent efforts to reduce it for specific language pairs.

We present a simple black-box method to influence the interpretation chosen by an NMT system in these ambiguous cases. More concretely, we construct pre-defined textual hints about the gender and number of the speaker and the audience (the interlocutors), which we concatenate to a given input sentence that we would like to translate accordingly. We then show that a black-box NMT system makes the desired morphological decisions according to the given hint, even when no other evidence is available on the source side. While adding those hints results in additional text on the target side, we show that it is simple to remove, leaving only the desired translation.

Our method is appealing as it only requires simple pre-and-post processing of the inputs and outputs, without considering the system internals, or requiring specific annotated data and training procedure as in previous work BIBREF1 . We show that in spite of its simplicity, it is effective in resolving many of the ambiguities and improves the translation quality in up to 2.3 BLEU when given the correct hints, which may be inferred from text metadata or other sources. Finally, we perform a fine-grained syntactic analysis of the translations generated using our
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-b0ab62019f37e966900b0402e54039ccb8db20cb6f72f9225be2f45dfc8b6d0f

Passage ID: `qasper-passage-v1-b0ab62019f37e966900b0402e54039ccb8db20cb6f72f9225be2f45dfc8b6d0f`; retrieval score: 2.0332692499433094.

Word count: 250.

```text
To demonstrate our method in a black-box setting, we focus our experiments on Google's machine translation system (GMT), accessed through its Cloud API. To test the method on real-world sentences, we consider a monologue from the stand-up comedy show “Sarah Silverman: A Speck of Dust”. The monologue consists of 1,244 English sentences, all by a female speaker conveyed to a plural, gender-neutral audience. Our parallel corpora consists of the 1,244 English sentences from the transcript, and their corresponding Hebrew translations based on the Hebrew subtitles. We translate the monologue one sentence at a time through the Google Cloud API. Eyeballing the results suggest that most of the translations use the incorrect, but default, masculine and singular forms for the speaker and the audience, respectively. We expect that by adding the relevant condition of “female speaking to an audience” we will get better translations, affecting both the gender of the speaker and the number of the audience.

To verify this, we experiment with translating the sentences with the following variations: No Prefix—The baseline translation as returned by the GMT system. “He said:”—Signaling a male speaker. We expect to further skew the system towards masculine forms. “She said:”—Signaling a female speaker and unknown audience. As this matches the actual speaker's gender, we expect an improvement in translation of first-person pronouns and verbs with first-person pronouns as subjects. “I said to them:”—Signaling an unknown speaker and plural audience. “He said to them:”—Masculine speaker and plural audience. “She said to them:”—Female speaker and plural
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1903.03467:3:0` | full | 0:1005 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1029.

Fully covered answer annotations: 7a7f39d12b1d910bc0ae826f3ee2a957141aecf3.

Missing evidence by answer annotation:

```text
{
  "7a7f39d12b1d910bc0ae826f3ee2a957141aecf3": {
    "unresolved_evidence": [],
    "paragraphs": {}
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

#### Rank 1: qasper-passage-v1-2ebaa45c3982e55315ce6c8800d59a1e5d1c085ddba830d6f316c342013b478a

Passage ID: `qasper-passage-v1-2ebaa45c3982e55315ce6c8800d59a1e5d1c085ddba830d6f316c342013b478a`; retrieval score: 7.2855192157550785.

Word count: 150.

```text
Another major performance concern in distributed computing is network bandwidth. Since the experts are stationary (see above) and the number of gating parameters is small, most of the communication involves sending the inputs and outputs of the experts across the network. To maintain computational efficiency, the ratio of an expert's computation to the size of its input and output must exceed the ratio of computational to network capacity of the computing device. For GPUs, this may be thousands to one. In our experiments, we use experts with one hidden layer containing thousands of RELU-activated units. Since the weight matrices in the expert have sizes INLINEFORM0 _ INLINEFORM1 _ INLINEFORM2 and INLINEFORM3 _ INLINEFORM4 _ INLINEFORM5 , the ratio of computation to input and output is equal to the size of the hidden layer. Conveniently, we can increase computational efficiency simply by using a larger hidden layer, or more hidden layers.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-d85caaf5e801b709911e1475f7feda38ccf18a57ee5e8393ae9f0779be70f543

Passage ID: `qasper-passage-v1-d85caaf5e801b709911e1475f7feda38ccf18a57ee5e8393ae9f0779be70f543`; retrieval score: 7.112376472400289.

Word count: 159.

```text
If the number of experts is very large, we can reduce the branching factor by using a two-level hierarchical MoE. In a hierarchical MoE, a primary gating network chooses a sparse weighted combination of “experts", each of which is itself a secondary mixture-of-experts with its own gating network. If the hierarchical MoE consists of INLINEFORM0 groups of INLINEFORM1 experts each, we denote the primary gating network by INLINEFORM2 , the secondary gating networks by INLINEFORM3 , and the expert networks by INLINEFORM4 . The output of the MoE is given by: DISPLAYFORM0

Our metrics of expert utilization change to the following: DISPLAYFORM0 DISPLAYFORM1

INLINEFORM0 and INLINEFORM1 deonte the INLINEFORM2 functions for the primary gating network and INLINEFORM3 secondary gating network respectively. INLINEFORM4 denotes the subset of INLINEFORM5 for which INLINEFORM6 .

It would seem simpler to let INLINEFORM0 , but this would not have a gradient with respect to the primary gating network, so we use the formulation above.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-e195037f066945ca237bf3631bca833325ba1711a8d923adcfe67d3050f76dfd

Passage ID: `qasper-passage-v1-e195037f066945ca237bf3631bca833325ba1711a8d923adcfe67d3050f76dfd`; retrieval score: 7.055583043694238.

Word count: 250.

```text
Our model consists of five layers: a word embedding layer, a recurrent Long Short-Term Memory (LSTM) layer BIBREF15 , BIBREF29 , a MoE layer, a second LSTM layer, and a softmax layer. The dimensionality of the embedding layer, the number of units in each LSTM layer, and the input and output dimensionality of the MoE layer are all equal to 512. For every layer other than the softmax, we apply drouput BIBREF43 to the layer output, dropping each activation with probability INLINEFORM0 , otherwise dividing by INLINEFORM1 . After dropout, the output of the previous layer is added to the layer output. This residual connection encourages gradient flow BIBREF37 .

Each expert in the MoE layer is a feed forward network with one ReLU-activated hidden layer of size 1024 and an output layer of size 512. Thus, each expert contains INLINEFORM0 parameters. The output of the MoE layer is passed through a sigmoid function before dropout. We varied the number of experts between models, using ordinary MoE layers with 4, 32 and 256 experts and hierarchical MoE layers with 256, 1024 and 4096 experts. We call the resulting models MoE-4, MoE-32, MoE-256, MoE-256-h, MoE-1024-h and MoE-4096-h. For the hierarchical MoE layers, the first level branching factor was 16, corresponding to the number of GPUs in our cluster. We use Noisy-Top-K Gating (see Section UID14 ) with INLINEFORM1 for the ordinary MoE layers and INLINEFORM2 at each level of the hierarchical MoE layers. Thus, each example is processed by exactly 4
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1701.06538:16:1` | partial | 0:847 |

#### Rank 4: qasper-passage-v1-ad38423141ff6a42e4e5da416d2b30abeea9177a5342b61cc85ce303d8ead904

Passage ID: `qasper-passage-v1-ad38423141ff6a42e4e5da416d2b30abeea9177a5342b61cc85ce303d8ead904`; retrieval score: 6.950752802929891.

Word count: 250.

```text
of the data-parallel input batches. The same set of devices function as data-parallel replicas (for the standard layers and the gating networks) and as model-parallel shards (each hosting a subset of the experts). If the model is distributed over INLINEFORM0 devices, and each device processes a batch of size INLINEFORM1 , each expert receives a batch of approximately INLINEFORM2 examples. Thus, we achieve a factor of INLINEFORM3 improvement in expert batch size.

In the case of a hierarchical MoE (Section SECREF60 ), the primary gating network employs data parallelism, and the secondary MoEs employ model parallelism. Each secondary MoE resides on one device.

This technique allows us to increase the number of experts (and hence the number of parameters) by proportionally increasing the number of devices in the training cluster. The total batch size increases, keeping the batch size per expert constant. The memory and bandwidth requirements per device also remain constant, as do the step times, as does the amount of time necessary to process a number of training examples equal to the number of parameters in the model. It is our goal to train a trillion-parameter model on a trillion-word corpus. We have not scaled our systems this far as of the writing of this paper, but it should be possible by adding more hardware.

In our language models, we apply the same MoE to each time step of the previous layer. If we wait for the previous layer to finish, we can apply the MoE to all
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-a17df2e259f5db8d39b20a26bf95f897738be68648ad11490fb54e24774b58d2

Passage ID: `qasper-passage-v1-a17df2e259f5db8d39b20a26bf95f897738be68648ad11490fb54e24774b58d2`; retrieval score: 6.922709203343276.

Word count: 173.

```text
Our approach to conditional computation is to introduce a new type of general purpose neural network component: a Sparsely-Gated Mixture-of-Experts Layer (MoE). The MoE consists of a number of experts, each a simple feed-forward neural network, and a trainable gating network which selects a sparse combination of the experts to process each input (see Figure FIGREF8 ). All parts of the network are trained jointly by back-propagation.

While the introduced technique is generic, in this paper we focus on language modeling and machine translation tasks, which are known to benefit from very large models. In particular, we apply a MoE convolutionally between stacked LSTM layers BIBREF15 , as in Figure FIGREF8 . The MoE is called once for each position in the text, selecting a potentially different combination of experts at each position. The different experts tend to become highly specialized based on syntax and semantics (see Appendix SECREF84 Table TABREF92 ). On both language modeling and machine translation benchmarks, we improve on best published results at a fraction of the computational cost.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 982.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "79c6e303c769cf6b075f42fc27820b4a2f8ee791": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1701.06538:16:1": [
        [
          847,
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

#### Rank 1: qasper-passage-v1-77a5da56e158b539a333caf261130719373b308ece8b177677e18414c6d9173a

Passage ID: `qasper-passage-v1-77a5da56e158b539a333caf261130719373b308ece8b177677e18414c6d9173a`; retrieval score: 6.622294076360174.

Word count: 250.

```text
In Figure FIGREF41 , we visualize the opinion attention scores of the words in two example sentences with the candidate aspects “maitre-D” and “bathroom”. The scores in Figures FIGREF41 and FIGREF41 show that our full model captures the related opinion words very accurately with significantly larger scores, i.e. “incredibly”, “unwelcoming” and “arrogant” for “maitre-D”, and “unfriendly” and “filthy” for “bathroom”. “OURS w/o STN” directly applies attention over the opinion hidden states INLINEFORM0 's, similar to what CMLA does. As shown in Figure FIGREF41 , it captures some unrelated opinion words (e.g. “fine”) and even some non-opinionated words. As a result, it brings in some noise into the global opinion summary, and consequently the final prediction accuracy will be affected. This example demonstrates that the proposed STN works pretty well to help attend to more related opinion words given a particular aspect.

Some predictions of our model and those of LSTM and OURS w/o THA & STN are given in Table TABREF43 . The models incorporating attention-based opinion summary (i.e., OURS and OURS w/o THA & STN) can better determine if the commonly-used nouns are aspect terms or not (e.g. “device” in the first input), since they make decisions based on the global opinion information. Besides, they are able to extract some infrequent or even misspelled aspect terms (e.g. “survice” in the second input) based on the indicative clues provided by opinion words. For the last three cases, having aspects in coordinate structures (i.e. the third and the fourth) or long
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-94fd3d274444cd0cca1222b94a10400f99664d8ad308e96b4a8ee4a705dde127

Passage ID: `qasper-passage-v1-94fd3d274444cd0cca1222b94a10400f99664d8ad308e96b4a8ee4a705dde127`; retrieval score: 4.636323825731864.

Word count: 250.

```text
As shown in Table TABREF39 , the proposed framework consistently obtains the best scores on all of the four datasets. Compared with the winning systems of SemEval ABSA, our framework achieves 5.0%, 1.6%, 1.4%, 1.3% absolute gains on INLINEFORM0 , INLINEFORM1 , INLINEFORM2 and INLINEFORM3 respectively.

Our framework can outperform RNCRF, a state-of-the-art model based on dependency parsing, on all datasets. We also notice that RNCRF does not perform well on INLINEFORM0 and INLINEFORM1 (3.7% and 3.9% inferior than ours). We find that INLINEFORM2 and INLINEFORM3 contain many informal reviews, thus RNCRF's performance degradation is probably due to the errors from the dependency parser when processing such informal texts.

CMLA and MIN do not rely on dependency parsing, instead, they employ attention mechanism to distill opinion information to help aspect extraction. Our framework consistently performs better than them. The gains presumably come from two perspectives: (1) In our model, the opinion summary is exploited after performing the selective transformation conditioned on the current aspect features, thus the summary can to some extent avoid the noise due to directly applying conventional attention. (2) Our model can discover some uncommon aspects under the guidance of some commonly-used aspects in coordinate structures by the history attention.

CRF with basic feature template is not strong, therefore, we add CRF-2 as another baseline. As shown in Table TABREF39 , CRF-2 with word embeddings achieves much better results than CRF-1 on all datasets. WDEmb, which is also an enhanced CRF-based method using additional dependency context embeddings,
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-a951580b65045fd54a062f7dbf6a1e36922e8986ccd2bda356f03a1cd0028dc1

Passage ID: `qasper-passage-v1-a951580b65045fd54a062f7dbf6a1e36922e8986ccd2bda356f03a1cd0028dc1`; retrieval score: 4.411228311123465.

Word count: 115.

```text
For more accurate aspect term extraction, we explored two important types of information, namely aspect detection history, and opinion summary. We design two components, i.e. truncated history attention, and selective transformation network. Experimental results show that our model dominates those joint extraction works such as RNCRF and CMLA on the performance of ATE. It suggests that the joint extraction sacrifices the accuracy of aspect prediction, although the ground-truth opinion words were annotated by these authors. Moreover, one should notice that those joint extraction methods do not care about the correspondence between the extracted aspect terms and opinion words. Therefore, the necessity of such joint extraction should be obelized, given the experimental findings in this paper.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-fc180ea9815ad36060f2ebfd9064929011963efcc1abd419a41ad317236a5b5e

Passage ID: `qasper-passage-v1-fc180ea9815ad36060f2ebfd9064929011963efcc1abd419a41ad317236a5b5e`; retrieval score: 4.394015813422085.

Word count: 250.

```text
Aspect-Based Sentiment Analysis (ABSA) involves detecting opinion targets and locating opinion indicators in sentences in product review texts BIBREF0 . The first sub-task, called Aspect Term Extraction (ATE), is to identify the phrases targeted by opinion indicators in review sentences. For example, in the sentence “I love the operating system and preloaded software”, the words “operating system” and “preloaded software” should be extracted as aspect terms, and the sentiment on them is conveyed by the opinion word “love”. According to the task definition, for a term/phrase being regarded as an aspect, it should co-occur with some “opinion words” that indicate a sentiment polarity on it BIBREF1 .

Many researchers formulated ATE as a sequence labeling problem or a token-level classification problem. Traditional sequence models such as Conditional Random Fields (CRFs) BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 , Long Short-Term Memory Networks (LSTMs) BIBREF6 and classification models such as Support Vector Machine (SVM) BIBREF7 have been applied to tackle the ATE task, and achieved reasonable performance. One drawback of these existing works is that they do not exploit the fact that, according to the task definition, aspect terms should co-occur with opinion-indicating words. Thus, the above methods tend to output false positives on those frequently used aspect terms in non-opinionated sentences, e.g., the word “restaurant” in “the restaurant was packed at first, so we waited for 20 minutes”, which should not be extracted because the sentence does not convey any opinion on it.

There are a few works that consider
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-46a1f8213d24b3f63759637e886a65bcb25a781538cec68cb2e14b209a722154

Passage ID: `qasper-passage-v1-46a1f8213d24b3f63759637e886a65bcb25a781538cec68cb2e14b209a722154`; retrieval score: 3.9268345932537994.

Word count: 250.

```text
given the appearance of the strongly related opinion “fresh”. However, CMLA employs conventional attention and does not have a mechanism to suppress the noise caused by other terms such as “rolls”. Dependency parsing seems to be a good solution for finding the most related opinion and indeed it was utilized in BIBREF8 , but the parser is prone to generating mistakes when processing the informal online reviews, as discussed in BIBREF17 .

To make use of opinion information and suppress the possible noise, we propose a novel Selective Transformation Network (STN) (the STN block in Figure FIGREF3 ), and insert it before attending to global opinion features so that more important features with respect to a given aspect candidate will be highlighted. Specifically, STN first calculates a new opinion representation INLINEFORM0 given the current aspect feature INLINEFORM1 as follows: DISPLAYFORM0

where INLINEFORM0 and INLINEFORM1 are parameters for history-aware aspect representations and opinion representations respectively. They map INLINEFORM2 and INLINEFORM3 to the same subspace. Here the aspect feature INLINEFORM4 acts as a “filter” to keep more important opinion features. Equation EQREF14 also introduces a residual block to obtain a better opinion representation INLINEFORM5 , which is conditioned on the current aspect feature INLINEFORM6 .

For distilling the global opinion summary, we introduce a bi-linear term to calculate the association score between INLINEFORM0 and each INLINEFORM1 : DISPLAYFORM0

where INLINEFORM0 and INLINEFORM1 are parameters of the Bi-Linear Attention layer. The improved opinion summary INLINEFORM2 at the time INLINEFORM3 is obtained via the
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1115.

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

#### Rank 1: qasper-passage-v1-9c189a265760e09dfa0e10761c149c377412476715d22f1a05cf430035e65910

Passage ID: `qasper-passage-v1-9c189a265760e09dfa0e10761c149c377412476715d22f1a05cf430035e65910`; retrieval score: 3.1202450168643496.

Word count: 250.

```text
We perform a descriptive analysis of the three datasets, comparing and contrasting their features and properties. We focus on two aspects, the network structure and the text information (the written descriptions associated with each node in the network). Understanding these data at these levels can inform efforts to combine different causal attribution networks (Sec. "Fusing causal networks" ).

Table 1 and Fig. 2 summarize network characteristics for the three causal attribution networks. We focus on standard measures of network structure, measuring the sizes, densities, motif structure, and connectedness of the three networks. Both Wikidata and ConceptNet, the two larger networks, are highly disconnected, amounting to collections of small components with low density. In contrast, IPRnet is smaller but comparatively more dense and connected, with higher average degree, fewer disconnected components, and more clustering (Table 1 ). All three networks are degree dissortative, meaning that high-degree nodes are more likely to connect to low-degree nodes. For connectedness and path lengths, we consider both directed and undirected versions of the network allowing us to measure strong and weak connectivity, respectively. All three networks are well connected when ignoring link directionality, but few directed paths exist between disparate nodes in Wikidata and ConceptNet, as shown by the large number of strong connected components and small size of the strong giant components for those networks.

To examine motifs, we focus on feedback loops and feedforward loops, both of which play important roles in causal relationships BIBREF32 , BIBREF33 . The sparse Wikidata network has
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-58244663101003d2faa51036e222c03edc8db2a7e81eb808320bfe4de2d0fa4b

Passage ID: `qasper-passage-v1-58244663101003d2faa51036e222c03edc8db2a7e81eb808320bfe4de2d0fa4b`; retrieval score: 3.108334655220781.

Word count: 138.

```text
Here we use network and text analysis tools to compare causal attribution networks (Sec. "Comparing causal networks" ). Crucially, nodes in these networks are defined only by their written descriptions, and multiple written descriptions can represent the same conceptual entity. Thus, to understand how causal attribution networks can be combined, we introduce and analyze a method for fusing networks (Sec. "Fusing causal networks" ) that builds off both the network structure and associated text information and explicitly incorporates conceptual equivalencies. Lastly, in Sec. "Inferring the size of the causal attribution network" we use the degree of overlap in these networks as a means to infer the total size of the one underlying causal attribution network being explored by these data collection efforts, allowing us to better understand the size of collective space of cause-effect relationships held by humans.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-d69778ceba0ebf8c6e520b056a1aadc3951ab1fcd80c867af51c8c51e1c2a499

Passage ID: `qasper-passage-v1-d69778ceba0ebf8c6e520b056a1aadc3951ab1fcd80c867af51c8c51e1c2a499`; retrieval score: 2.952088836749115.

Word count: 250.

```text
These causal attributions networks are separate efforts to map out the underlying or latent causal attribution network held collectively by humans. It is natural to then ask if these different efforts can be combined in an effective way. Fusing these networks together can provide a single causal attribution network for researchers to study.

At the most basic level, one can fuse these networks together simply by taking their union, defining a single network containing all the unique nodes and edges of the original networks. Unfortunately, nodes in these networks are identified by their sentences, and this graph union assumes that two nodes $i$ and $j$ are equivalent iff $s_i = s_j$ . This is overly restrictive as these sentences serve as descriptions of associated concepts, and we ideally want to combine nodes that represent the same concept even when their written descriptions differ. Indeed, even within a single network it can be necessary to identify and combine nodes in this way. We identify this problem as graph fusion. Graph fusion is a type of record linkage problem and is closely related to graph alignment and (inexact) graph matching BIBREF27 , but unlike those problems, graph fusion assumes the need to identify node equivalencies both within and between the networks being fused.

We introduce a fusion algorithm, NetFUSES (Network FUsion with SEmantic Similarity) that allows us to combine networks using a measure of similarity between nodes (Sec. "Data and Methods" ). Crucially, NetFUSES can handle networks where nodes may need to
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-6129a8aaf7b30d794c65c3cb77b574b22e0d9b00d8a748746895f17597ba6e1f

Passage ID: `qasper-passage-v1-6129a8aaf7b30d794c65c3cb77b574b22e0d9b00d8a748746895f17597ba6e1f`; retrieval score: 2.8024690901939295.

Word count: 250.

```text
In this work we compare causal attribution networks derived from three datasets. A causal attribution dataset is a collection of text pairs that reflect cause-effect relationships proposed by humans (for example, “virus causes sickness”). These written statements identify the nodes of the network (see also our graph fusion algorithm for dealing with semantically equivalent statements) while cause-effect relationships form the directed edges (“virus” $\rightarrow $ “sickness”) of the causal attribution network.

We collected causal attribution networks from three sources of data: English Wikidata BIBREF11 , English ConceptNet BIBREF10 , and IPRnet BIBREF12 . Wikidata and ConceptNet, are large knowledge graphs that contain semantic links denoting many types of interactions, one of which is causal attribution, while IPRnet comes from an Amazon Mechanical Turk study in which crowd workers were prompted to provide causal relationships. Wikidata relations were gathered by running four search queries on the Wikidata API (query.wikidata.org). These queries searched for relations with the properties: "has immediate cause", "has effect", "has cause", or "immediate cause of". The first and third searches reverse the order of the cause and effect which we reversed back. We discarded any Wikidata relations where the cause or effect were blank, as well as one ambiguous relation where the cause was "NaN". ConceptNet attributions were gathered by searching the English ConceptNet version 5.6.0 assertions for “/r/Causes/” relations. Lastly, IPRnet was developed in BIBREF12 which we use directly.

The three networks together contain $23\,239$ causal links and $19\,096$ unique terms, of which there are $4\,265$ and
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1812.06038:0:0` | full | 0:515 |

#### Rank 5: qasper-passage-v1-925ef1d576d112dfa92291f33b676ed8d5882dd13e4e215d7a16999d6ec80e33

Passage ID: `qasper-passage-v1-925ef1d576d112dfa92291f33b676ed8d5882dd13e4e215d7a16999d6ec80e33`; retrieval score: 2.730712457750056.

Word count: 250.

```text
The construction of causal attribution networks generates important knowledge networks that may inform causal inference research and even help future AI systems to perform causal reasoning, but these networks are time-consuming and costly to generate, and to date no efforts have been made to combine different networks. Our work not only studies the potential for fusing different networks together, but also infers the overall size of the total causal attribution network being explored.

We used capture-recapture estimators to infer the number of nodes and links in the underlying causal attribution network, given the Wikidata and ConceptNet networks and using NetFUSES and a semantic similarity function to help account for semantically equivalent nodes within and between Wikidata and ConceptNet. The validity of these estimates depends on Wikidata and ConceptNet being independent samples of the underlying network. As with many practical applications of capture-recapture in wildlife ecology and other areas, here we must question how well this independence assumption holds. The best way to sharpen these estimates is to introduce a new causal attribution survey specifically designed to capture either nodes or links independently (it is unlikely that a single survey protocol can sample independently both nodes and links), and then perform this same survey multiple times.

NetFUSES is a simple approach to graph fusion, in this case building off advances made in semantic representations of natural language, although any similarity function can be used to identify semantically equivalent nodes as appropriate. We anticipate that more accurate and more computationally efficient methods
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1138.

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

#### Rank 1: qasper-passage-v1-18790e6e4f151c9f52e717da3cad55fb2f314482a4e70002eff141931d7debde

Passage ID: `qasper-passage-v1-18790e6e4f151c9f52e717da3cad55fb2f314482a4e70002eff141931d7debde`; retrieval score: 4.918359881520997.

Word count: 86.

```text
We established strong baselines for two story narrative understanding datasets: CaTeRS and RED. We have shown that neural network-based models can outperform feature-based models with wide margins, and we conducted an ablation study to show that contextualized representation learning can boost performance of NN models. Further research can focus on more systematic study or build stronger NN models over the same datasets used in this work. Exploring possibilities to directly apply temporal relation extraction to enhance performance of story generation systems is another promising research direction.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-2263d72697fb7a5e7d19fc277225aa9b054816f85f55a75a8d25e8fd5dd8730f

Passage ID: `qasper-passage-v1-2263d72697fb7a5e7d19fc277225aa9b054816f85f55a75a8d25e8fd5dd8730f`; retrieval score: 4.613718820138195.

Word count: 126.

```text
The series of TempEval competitions BIBREF21 , BIBREF22 , BIBREF23 have attracted many research interests in predicting event temporal relations. Early attempts by BIBREF24 , BIBREF21 , BIBREF25 , BIBREF26 only use pair-wise classification models. State-of-the-art local methods, such as ClearTK BIBREF27 , UTTime BIBREF28 , and NavyTime BIBREF29 improve on earlier work by feature engineering with linguistic and syntactic rules. As we mention in the Section 2, CAEVO is the current state-of-the-art system for feature-based temporal event relation extraction BIBREF10 . It's widely used as the baseline for evaluating TB-Dense data. We adopt it as our baseline for evaluating CaTeRS and RED datasets. Additionally, several models BramsenDLB2006, ChambersJ2008, DoLuRo12, NingWuRo18, P18-1212 have successfully incorporated global inference to impose global prediction consistency such as temporal transitivity.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.11942:6:0` | full | 0:912 |

#### Rank 3: qasper-passage-v1-4f9ae4f83628a2f8fb987916c530ec37adbd2f95876e93ecdab87f062613d81e

Passage ID: `qasper-passage-v1-4f9ae4f83628a2f8fb987916c530ec37adbd2f95876e93ecdab87f062613d81e`; retrieval score: 4.225739334809775.

Word count: 69.

```text
Table TABREF25 contains the best hyper-parameters and Table TABREF26 contains micro-average F1 scores for both datasets on dev and test sets. We only consider positive pairs, i.e. correct predictions on NONE pairs are excluded for evaluation. In general, the baseline model CAEVO is outperformed by both NN models, and NN model with BERT embedding achieves the greatest performance. We now provide more detailed analysis and discussion for each dataset.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-06f433f2141d72e3bf5f69183dac012be15511022e3de63db1a7cce12865726e

Passage ID: `qasper-passage-v1-06f433f2141d72e3bf5f69183dac012be15511022e3de63db1a7cce12865726e`; retrieval score: 3.207522139691232.

Word count: 131.

```text
, BIBREF12 and event relation annotation for story understanding BIBREF8 , the intersection of these two threads seems flimsy. To the best of our knowledge, no event relation extraction results have been reported on CaTeRS and RED.

We apply neural network models that leverage recent advances in contextualized embeddings (BERT BIBREF13 ) to event-event relation extraction tasks for CaTeRS and RED. Our goal in this paper is to increase understanding of how well the state-of-the-art event relation models work for story/narrative comprehension.

In this paper, we report the first results of event temporal relation extraction on two under-explored story comprehension datasets: CaTeRS and RED. We establish strong baselines with neural network models enhanced by recent breakthrough of contextualized embeddings, BERT BIBREF13 . We summarize the contributions of the paper as follows:
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-bdd3d4764423825e93ac94f5592f90745491082f82047b7895c5d79ff7527432

Passage ID: `qasper-passage-v1-bdd3d4764423825e93ac94f5592f90745491082f82047b7895c5d79ff7527432`; retrieval score: 2.8958497507792584.

Word count: 204.

```text
Table TABREF16 ) because it contains longer articles, more complicated sentence structures, and richer entity types than CaTeRS where all stories consist of 5 (mostly short) sentences.

In both the development and test sets, we add all negative pairs as candidates for the relation prediction. During training, the number of negative pairs we add is based on a hyper-parameter that we tune to control the negative-to-positive sample ratio.

To justify our decision of selecting negative pairs within the same or neighboring sentences, we show the distribution of distances across positive sentence pairs in Table TABREF18 . Although CaTeRS data has pair distance more evenly distributed than RED, we observe that the vast majority (85.87% and 93.99% respectively) of positive pairs have sentence distance less than or equal to one.

To handle negative pairs that are more than two sentences away, we automatically predict all out-of-window pairs as “NONE”. This means that some positive pairs will be automatically labeled as negative pairs. Since the percentage of out-of-window positive pairs is small, we believe the impact on performance is small. We can investigate expanding the prediction window in future research, but the trade-off is that we will get more negative pairs that are hard to predict.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 616.

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

#### Rank 1: qasper-passage-v1-7a747578dc919919cb19cc085428fb1f88af9b649db6243362a590047c70922e

Passage ID: `qasper-passage-v1-7a747578dc919919cb19cc085428fb1f88af9b649db6243362a590047c70922e`; retrieval score: 7.160753145403044.

Word count: 149.

```text
For low resource languages, parallel data may not be available. In this case, we rely only on monolingual data (e.g., Wikipedias). We estimate word translation probabilities from word embeddings of the two languages. Word vectors of these languages can be learned using fastText BIBREF14 and then are aligned into a shared space with English BIBREF15, BIBREF16. Unlike learning contextualized representations, learning word vectors is fast and computationally cheap. Given the aligned vectors $\bar{}_f$ of foreign and $\bar{}_e$ of English, we calculate the word translation matrix $\in ^{|V_f|\times |V_e|}$ as

Here, we use $\mathrm {sparsemax}$ BIBREF17 instead of softmax. Sparsemax is a sparse version of softmax and it puts zero probabilities on most of the word in the English vocabulary except few English words that are similar to a given foreign word. This property is desirable in our approach since it leads to a better initialization of the foreign embeddings.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-d8eab3c905b27a206ecb65e8f2cb7272005f6b167e7817c5c1bc70423d094906

Passage ID: `qasper-passage-v1-d8eab3c905b27a206ecb65e8f2cb7272005f6b167e7817c5c1bc70423d094906`; retrieval score: 5.896080612719393.

Word count: 250.

```text
Pre-trained models BIBREF0, BIBREF1 have received much of attention recently thanks to their impressive results in many down stream NLP tasks. Additionally, multilingual pre-trained models enable many NLP applications for other languages via zero-short cross-lingual transfer. Zero-shot cross-lingual transfer has shown promising results for rapidly building applications for low resource languages. BIBREF2 show the potential of multilingual-BERT BIBREF0 in zero-shot transfer for a large number of languages from different language families on five NLP tasks, namely, natural language inference, document classification, named entity recognition, part-of-speech tagging, and dependency parsing.

Although multilingual models are an important ingredient for enhancing language technology in many languages, recent research on improving pre-trained models puts much emphasis on English BIBREF3, BIBREF4, BIBREF5. The current state of affairs makes it difficult to translate advancements in pre-training from English to non-English languages. To our best knowledge, there are only three available multilingual pre-trained models to date: (1) the multilingual-BERT (mBERT) that supports 104 languages, (2) cross-lingual language model BIBREF6 that supports 100 languages, and (3) Language Agnostic SEntence Representations BIBREF7 that supports 93 languages. Among the three models, LASER is based on neural machine translation approach and strictly requires parallel data to train.

Do multilingual models always need to be trained from scratch? Can we transfer linguistic knowledge learned by English pre-trained models to other languages? In this work, we develop a technique to rapidly transfer an existing pre-trained model from English to other languages in an energy efficient way BIBREF8. As the first step, we focus
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-996e09b89d6b134dd8c159492bd24c138d6bac76ff6ed4c176e2d750a30ac1f2

Passage ID: `qasper-passage-v1-996e09b89d6b134dd8c159492bd24c138d6bac76ff6ed4c176e2d750a30ac1f2`; retrieval score: 5.736215883532804.

Word count: 250.

```text
We evaluate our approach for six target languages: French (fr), Russian (ru), Arabic (ar), Chinese (zh), Hindi (hi), and Vietnamese (vi). These languages belong to four different language families. French, Russian, and Hindi are Indo-European languages, similar to English. Arabic, Chinese, and Vietnamese belong to Afro-Asiatic, Sino-Tibetan, and Austro-Asiatic family respectively. The choice of the six languages also reflects different training conditions depending on the amount of monolingual data. French and Russian, and Arabic can be regarded as high resource languages whereas Hindi has far less data and can be considered as low resource.

For experiments that use parallel data to initialize foreign specific parameters, we use the same datasets in the work of BIBREF6. Specifically, we use United Nations Parallel Corpus BIBREF18 for en-ru, en-ar, en-zh, and en-fr. We collect en-hi parallel data from IIT Bombay corpus BIBREF19 and en-vi data from OpenSubtitles 2018. For experiments that use only monolingual data to initialize foreign parameters, instead of training word-vectors from the scratch, we use the pre-trained word vectors from fastText BIBREF14 to estimate word translation probabilities (Eq. DISPLAY_FORM13). We align these vectors into a common space using orthogonal Procrustes BIBREF20, BIBREF15, BIBREF16. We only use identical words between the two languages as the supervised signal. We use WikiExtractor to extract extract raw sentences from Wikipedias as monolingual data for fine-tuning target embeddings and bilingual LMs (§SECREF15). We do not lowercase or remove accents in our data preprocessing pipeline.

We tokenize English using the provided tokenizer from pre-trained models. For
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2002.07306:8:0` | full | 0:649 |

#### Rank 4: qasper-passage-v1-20d4cd84b1d98e309f040f9113a0e40f6f309a296e62463192866bae3036c24e

Passage ID: `qasper-passage-v1-20d4cd84b1d98e309f040f9113a0e40f6f309a296e62463192866bae3036c24e`; retrieval score: 5.120971059310558.

Word count: 250.

```text
Table TABREF32 shows the XNLI test accuracy. For reference, we also include the scores from the previous work, notably the state-of-the-art system XLM BIBREF6. Before discussing the results, we spell out that the fairest comparison in this experiment is the comparison between mBERT and RAMEN$_{\textsc {base}}$+BERT trained with monolingual only.

We first discuss the transfer results from BERT. Initialized from fastText vectors, RAMEN$_{\textsc {base}}$ slightly outperforms mBERT by 1.9 points on average and widen the gap of 3.3 points on Arabic. RAMEN$_{\textsc {base}}$ gains extra 0.8 points on average when initialized from parallel data. With triple number of parameters, RAMEN$_{\textsc {large}}$ offers an additional boost in term of accuracy and initialization with parallel data consistently improves the performance. It has been shown that BERT$_{\textsc {large}}$ significantly outperforms BERT$_{\textsc {base}}$ on 11 English NLP tasks BIBREF0, the strength of BERT$_{\textsc {large}}$ also shows up when adapted to foreign languages.

Transferring from RoBERTa leads to better zero-shot accuracies. With the same initializing condition, RAMEN$_{\textsc {base}}$+RoBERTa outperforms RAMEN$_{\textsc {base}}$+BERT on average by 2.9 and 2.3 points when initializing from monolingual and parallel data respectively. This result show that with similar number of parameters, our approach benefits from a better English pre-trained model. When transferring from RoBERTa$_{\textsc {large}}$, we obtain state-of-the-art results for five languages.

Currently, RAMEN only uses parallel data to initialize foreign embeddings. RAMEN can also exploit parallel data through translation objective proposed in XLM. We believe that by utilizing parallel data during the fine-tuning of RAMEN would bring additional benefits for
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-33737649f85647463466a2a0fa4f117faabbcdad0ea5d5d3db4cfe5bc4dace7f

Passage ID: `qasper-passage-v1-33737649f85647463466a2a0fa4f117faabbcdad0ea5d5d3db4cfe5bc4dace7f`; retrieval score: 3.724718996613369.

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

Total retrieved words: 1105.

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

#### Rank 1: qasper-passage-v1-e88266a75483c714a045b9345c5d7190a2dcc0dba140d8a24ee1b49b0cc40c42

Passage ID: `qasper-passage-v1-e88266a75483c714a045b9345c5d7190a2dcc0dba140d8a24ee1b49b0cc40c42`; retrieval score: 5.8323488321988055.

Word count: 214.

```text
this work we explore the automatic processing of ultrasound tongue images in order to assist SLTs, who currently largely rely on manual processing when using articulatory imaging in speech therapy. One task that could assist SLTs is the automatic classification of tongue shapes from raw ultrasound. This can facilitate the diagnosis and treatment of speech sound disorders, by allowing SLTs to automatically identify incorrect articulations, or by quantifying patient progress in therapy. In addition to being directly useful for speech therapy, the classification of tongue shapes enables further understanding of phonetic variability in ultrasound tongue images. Much of the previous work in this area has focused on speaker-dependent models. In this work we investigate how automatic processing of ultrasound tongue imaging is affected by speaker variation, and how severe degradations in performance can be avoided when applying systems to data from previously unseen speakers through the use of speaker adaptation and speaker normalization approaches.

Below, we present the main challenges associated with the automatic processing of ultrasound data, together with a review of speaker-independent models applied to UTI. Following this, we present the experiments that we have performed (Section SECREF2 ), and discuss the results obtained (Section SECREF3 ). Finally we propose some future work and conclude the paper (Sections SECREF4 and SECREF5 ).
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-9af4fb6cacf59cc492b87fcdd07a3b2ffde873fcd2c86eeb6a5d261150220a8e

Passage ID: `qasper-passage-v1-9af4fb6cacf59cc492b87fcdd07a3b2ffde873fcd2c86eeb6a5d261150220a8e`; retrieval score: 5.149973418806592.

Word count: 158.

```text
We use the Ultrax Typically Developing dataset (UXTD) from the publicly available UltraSuite repository BIBREF19 . This dataset contains synchronized acoustic and ultrasound data from 58 typically developing children, aged 5-12 years old (31 female, 27 male). The data was aligned at the phone-level, according to the methods described in BIBREF19 , BIBREF25 . For this work, we discarded the acoustic data and focused only on the B-Mode ultrasound images capturing a midsaggital view of the tongue. The data was recorded using an Ultrasonix SonixRP machine using Articulate Assistant Advanced (AAA) software at INLINEFORM0 121fps with a 135 field of view. A single ultrasound frame consists of 412 echo returns from each of the 63 scan lines (63x412 raw frames). For this work, we only use UXTD type A (semantically unrelated words, such as pack, tap, peak, tea, oak, toe) and type B (non-words designed to elicit the articulation of target phones, such as apa, eepee, opo) utterances.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1907.01413:3:0` | full | 0:986 |

#### Rank 3: qasper-passage-v1-a3c3cbcbcec80526b4d0d0bb27b0bb09b31fc5890a51456faf0fe8a226cef705

Passage ID: `qasper-passage-v1-a3c3cbcbcec80526b4d0d0bb27b0bb09b31fc5890a51456faf0fe8a226cef705`; retrieval score: 4.210429513460842.

Word count: 81.

```text
(CNNs) with 2 convolutional and max pooling layers, followed by 2 fully-connected ReLU layers with 512 nodes. The convolutional layers use 16 filters, 8x8 and 4x4 kernels respectively, and rectified units. The fully-connected layers use dropout with a drop probability of 0.2. Because CNN systems take longer to converge, they are optimized over 200 epochs. For all systems, at the end of every epoch, the model is evaluated on the development set, and the best model across all epochs is kept.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-5934cd4d5dc29cd268efca378c957d85454238f6edda8c82cf807f0705317016

Passage ID: `qasper-passage-v1-5934cd4d5dc29cd268efca378c957d85454238f6edda8c82cf807f0705317016`; retrieval score: 2.9241973700469726.

Word count: 250.

```text
of the size of the adaptation data when finetuning a pre-trained speaker-independent system. As expected, the more data is available, the better that system performs. It is observed that, for the CNN system, with roughly 50 samples, the model outperforms a similar speaker-dependent system with roughly three times more examples.

Speaker means improve results across all scenarios. It is particularly useful for speaker-independent systems. The ability to generalize to unseen speakers is clear in the CNN system. Using the mean as a second channel in the convolutional network has the advantage of relating each pixel to its corresponding speaker mean value, allowing the model to better generalize to unseen speakers.

Figure FIGREF12 shows pair-wise scatterplots for the CNN system. Training scenarios are compared in terms of the effect on individual speakers. It is observed, for example, that the performance of a speaker-adapted system is similar to a multi-speaker system, with most speakers clustered around the identity line (bottom left subplot). Figure FIGREF12 also illustrates the variability across speakers for each of the training scenarios. The classification task is easier for some speakers than others. In an attempt to understand this variability, we can look at correlation between accuracy scores and various speaker details. For the CNN systems, we have found some correlation (Pearson's product-moment correlation) between accuracy and age for the dependent ( INLINEFORM0 ), multi-speaker ( INLINEFORM1 ), and adapted ( INLINEFORM2 ) systems. A very small correlation ( INLINEFORM3 ) was found for the independent system. Similarly, some
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-07651a54ec6c9bbb6c5c7815412b9127e77c285d38ec39023823703211c35073

Passage ID: `qasper-passage-v1-07651a54ec6c9bbb6c5c7815412b9127e77c285d38ec39023823703211c35073`; retrieval score: 2.9191594440180006.

Word count: 109.

```text
In this paper, we have investigated speaker-independent models for the classification of phonetic segments from raw ultrasound data. We have shown that the performance of the models heavily degrades when evaluated on data from unseen speakers. This is a result of the variability in ultrasound images, mostly due to differences across speakers, but also due to shifts in probe placement. Using the mean of all ultrasound frames for a new speaker improves the generalization of the models to unseen data, especially when using convolutional neural networks. We have also shown that adapting a pre-trained speaker-independent system using as few as 50 ultrasound frames can outperform a corresponding speaker-dependent system.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 812.

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

#### Rank 1: qasper-passage-v1-05ab94f591006560bdc25db3f5cf336d386ec1ec21080d9efac30b2da4733345

Passage ID: `qasper-passage-v1-05ab94f591006560bdc25db3f5cf336d386ec1ec21080d9efac30b2da4733345`; retrieval score: 6.864863313097233.

Word count: 90.

```text
In our experiments we aim to answer the following research questions (RQs):

RQ1: How does the number of training iterations in the BERT language model finetuning stage influence the ATSC end-task performance? At what point does performance start to improve, when does it converge?

RQ2: When trained in-domain, what ATSC end-task performance can be reached through fully exploitet finetuning of the BERT language model?

RQ3: When trained cross-domain in the special case of domain adaptation, what ATSC end-task performance can be reached if BERT language model finetuning is fully exploitet?
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-f6c757adf6cab8c30e275cc73d4e746da4995d5efec0bf1d34a99f25fe4a014e

Passage ID: `qasper-passage-v1-f6c757adf6cab8c30e275cc73d4e746da4995d5efec0bf1d34a99f25fe4a014e`; retrieval score: 3.396289852540484.

Word count: 250.

```text
The results of our experiments are shown in fig:acc-dep-lmiterations and tab:results respectively.

To answer RQ1, which is concerned with details on domain-specific language model finetuning, we can see in fig:acc-dep-lmiterations that first of all, language model finetuning has a substantial effect on ATSC end-task performance. Secondly, we see that in the laptops domain the performance starts to increase at about 10 Mio. finetuned sentences. This is an interesting insight as one would expect a relation closer to a logarithmic curve. One reason might be that it takes many steps to train knowledge into the BERT language model due to its vast amount of parameters. The model already converges at around 17 Mio. sentences. More finetuning does not improve performance significantly. In addition, we find that different runs have a high variance, the standard deviation amounts to about $1\%$ in accuracy, which justifies averaging over 9 runs to measure differences in model performance reliably.

To answer RQ2, which is concerned with in-domain ATSC performance, we see in tab:results that for the in-domain training case, our models BERT-ADA Lapt and BERT-ADA Rest achieve performance close to state-of-the-art on the laptops dataset and new state-of-the-art on the restaurants dataset with accuracies of $79.19\%$ and $87.14\%$, respectively. On the restaurants dataset, this corresponds to an absolute improvement of $2.2\%$ compared to the previous state-of-the-art method BERT-PT. Language model finetuning produces a larger improvement on the restaurants dataset. We think that one reason for that might be that the restaurants domain is underrepresented in the
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.11860:19:2` | partial | 0:671 |

#### Rank 3: qasper-passage-v1-5f70bd83929c4ccf19588f0b8f38afd9bc9c545b7c44ea6b7a38e10af24173ef

Passage ID: `qasper-passage-v1-5f70bd83929c4ccf19588f0b8f38afd9bc9c545b7c44ea6b7a38e10af24173ef`; retrieval score: 3.296336369422385.

Word count: 121.

```text
epochs, 30 epochs in the case of the laptops domain compared to 3 epochs for the restaurants domain, so that the BERT model trains on about 30 million sentences in both cases. This means that 1 sentence can be seen multiple times with a different language model masking.

We also create a mixed corpus to jointly finetune both domains. Here, we sample 1 Mio. restaurant reviews and combine them with the laptop reviews. This results in about 2 Mio. reviews that are finetuned for 15 epochs. The exact statistics for the three finetuning corpora are shown in the top of tab:datasets.

To be able to reproduce our finetuning corpora, we make the code that is used to generate them available online.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-4cc3ff96c4d69a9797bb7f05566a58777f42dda82a13f10458344c7d6d3525ea

Passage ID: `qasper-passage-v1-4cc3ff96c4d69a9797bb7f05566a58777f42dda82a13f10458344c7d6d3525ea`; retrieval score: 3.0869279991339136.

Word count: 250.

```text
We compare in-domain results to current state of the art methods, which we will now describe briefly.

SDGCN-BERT BIBREF11 explicitly models sentiment dependencies for sentences with multiple aspects with a graph convolutional network. This method is current state-of-the-art on the SemEval 2014 laptops dataset.

AEN-BERT BIBREF8 is an attentional encoder network. When used on top of BERT embeddings this method performs especially well on the laptops dataset.

BERT-SPC BIBREF8 is BERT used in sentence-pair classification mode. This is exactly the same method as our BERT-base baseline and therefore, we can cross-check the authors results.

BERT-PT BIBREF9 uses multi-task fine-tuning prior to downstream classification, where the BERT language model is finetuned jointly with a question answering task. It performs state-of-the-art on the restaurants dataset prior to this paper.

To our knowledge, cross- and joint-domain training on the SemEval 2014 Task 4 datasets has not been analyzed so far. Thus, we compare our method to two very strong baselines: BERT and XLNet.

BERT-base BIBREF7 is using the pre-trained BERTBASE embeddings directly on the down-stream task without any domain specific language model finetuning.

XLNet-base BIBREF19 is a method also based on general language model pre-training similar to BERT. Instead of randomly masking tokens for pre-training like in BERT a more general permutation objective is used, where all possible variants of masking are fully exploitet.

Our models are BERT models whose language model has been finetuned on different domain corpora.

BERT-ADA Lapt is the BERT language model finetuned on the laptops domain corpus.

BERT-ADA
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-2325f89a3b815ffa6943d00cab27eecb8aa855d80aa212ffb15c7556198bd467

Passage ID: `qasper-passage-v1-2325f89a3b815ffa6943d00cab27eecb8aa855d80aa212ffb15c7556198bd467`; retrieval score: 3.0195029991294753.

Word count: 209.

```text
The datasets typically used for Aspect-Target Sentiment Classification are the SemEval 2014 Task 4 datasets BIBREF1 for the restaurants and laptops domain. Unfortunately, both datasets only have a small number of training examples. One common approach to compensate for insufficient training examples is to invent neural architectures that better model ATSC. For example, in the past a big leap in classification performance was achieved with the use of the Memory Network architecture BIBREF3, which uses memory to remember context words and explicitly models attention over both the target word and context. It was found that making full use of context words improves their model compared to previous models BIBREF2 that make use of left- and right-sided context independently.

BIBREF8 proposed Attention Encoder Networks (AEN), a modification to the transformer architecture. The authors split the Multi-Head Attention (MHA) layers into Intra-MHA and Inter-MHA layers in order to model target words and context differently, which results in a more lightweight model compared to the transformer architecture.

Another recent performance leap was achieved by BIBREF11, who model dependencies between sentiment words explicitly in sentences with more than one aspect-target by using a graph convolutional neural network. They show that their architecture performs particularly well if multiple aspects are present in a sentence.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 920.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "46773036407495e12fc0be2224060db32f6d6676": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1908.11860:19:2": [
        [
          671,
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

#### Rank 1: qasper-passage-v1-65a9d8cdb353296dbe32f01bf5def2e068a01a22bf1fe98a96d8f13aa0019e0e

Passage ID: `qasper-passage-v1-65a9d8cdb353296dbe32f01bf5def2e068a01a22bf1fe98a96d8f13aa0019e0e`; retrieval score: 5.035755770367537.

Word count: 250.

```text
most previous work on rare words was evaluated on datasets explicitly focusing on such words BIBREF6, BIBREF3, BIBREF4, BIBREF5, BIBREF10, all of these datasets are tailored towards context-independent embeddings and thus not suitable for evaluating our proposed model. Furthermore, understanding rare words is of negligible importance for most commonly used downstream task datasets. To evaluate our proposed model, we therefore introduce a novel procedure that allows us to automatically turn arbitrary text classification datasets into ones where rare words are guaranteed to be important. This is achieved by replacing classification-relevant frequent words with rare synonyms obtained using semantic resources such as WordNet BIBREF20.

Using this procedure, we extract rare word datasets from three commonly used text (or text pair) classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. On both the WNLaMPro dataset of BIBREF0 and all three so-obtained datasets, our proposed Bertram model outperforms previous work by a large margin.

In summary, our contributions are as follows:

We show that a pretrained BERT instance can be integrated into Attentive Mimicking, resulting in much better context representations and a deeper connection of form and context.

We design a procedure that allows us to automatically transform text classification datasets into datasets for which rare words are guaranteed to be important.

We show that Bertram achieves a new state-of-the-art on the WNLaMPro probing task BIBREF0 and beats all baselines on rare word instances of AG's News, MNLI and DBPedia, resulting in an absolute improvement of up to 24% over a BERT
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-ec6035ca5ae00ef28249068adb2a174ab304922d4eb0bc58bb755d7703de7d30

Passage ID: `qasper-passage-v1-ec6035ca5ae00ef28249068adb2a174ab304922d4eb0bc58bb755d7703de7d30`; retrieval score: 3.6897177046205134.

Word count: 141.

```text
We have introduced Bertram, a novel architecture for relearning high-quality representations of rare words. This is achieved by employing a powerful pretrained language model and deeply connecting surface-form and context information. By replacing important words with rare synonyms, we have created various downstream task datasets focusing on rare words; on all of these datasets, Bertram improves over a BERT model without special handling of rare words, demonstrating the usefulness of our proposed method.

As our analysis has shown that even for the most frequent words considered, using Bertram is still beneficial, future work might further investigate the limits of our proposed method. Furthermore, it would be interesting to explore more complex ways of incorporating surface-form information – e.g., by using a character-level CNN similar to the one of BIBREF27 – to balance out the potency of Bertram's form and context parts.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-6264220bb0b8c589f34f9a4806a8999c303354621f83f2ac06d8cc00da84a569

Passage ID: `qasper-passage-v1-6264220bb0b8c589f34f9a4806a8999c303354621f83f2ac06d8cc00da84a569`; retrieval score: 3.0501579998403763.

Word count: 250.

```text
To measure the effect of adding Bertram to BERT on downstream tasks, we apply the procedure described in Section SECREF4 to a commonly used textual entailment dataset as well as two text classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. For all three datasets, we use BERT$_\text{base}$ as a baseline model and create the substitution dictionary $S$ using the synonym relation of WordNet BIBREF20 and the pattern library BIBREF34 to make sure that all synonyms have consistent parts of speech. As an additional source of word substitutions, we make use of the misspellings dataset of BIBREF25, which is based on query logs of a search engine. To prevent misspellings from dominating the resulting dataset, we only assign misspelling-based substitutes to randomly selected 10% of the words contained in each sentence. Motivated by the results on WNLaMPro-medium, we consider every word that occurs less than 100 times in the WWC and our BooksCorpus replica combined as being rare. Some examples of entries in the resulting datasets can be seen in Table TABREF35.

Just like for WNLaMPro, our default way of injecting Bertram embeddings into the baseline model is to replace the sequence of uncontextualized WordPiece tokens for a given rare word with its Bertram-based embedding. That is, given a sequence of uncontextualized token embeddings $\mathbf {e} = e_1, \ldots , e_n$ where $e_{i}, \ldots , e_{i+j}$ with $1 \le i \le i+j \le n$ is the sequence of WordPiece embeddings for a single rare word $w$, we replace $\mathbf
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1910.07181:11:0` | full | 0:1092 |

#### Rank 4: qasper-passage-v1-57e33c335b05101c7c92486b7d4a1f22f40536759a12bba0cd658c29b31b1ff2

Passage ID: `qasper-passage-v1-57e33c335b05101c7c92486b7d4a1f22f40536759a12bba0cd658c29b31b1ff2`; retrieval score: 2.615699779962121.

Word count: 170.

```text
For our evaluation of Bertram, we largely follow the experimental setup of BIBREF0. Our implementation of Bertram is based on PyTorch BIBREF30 and the Transformers library of BIBREF31. Throughout all of our experiments, we use BERT$_\text{base}$ as the underlying language model for Bertram. To obtain embeddings for frequent multi-token words during training, we use one-token approximation BIBREF0. Somewhat surprisingly, we found in preliminary experiments that excluding BERT's parameters from the finetuning procedure outlined in Section SECREF17 improves performance while speeding up training; we thus exclude them in the third step of our training procedure.

While BERT was trained on BooksCorpus BIBREF32 and a large Wikipedia dump, we follow previous work and train Bertram on only the much smaller Westbury Wikipedia Corpus (WWC) BIBREF33; this of course gives BERT a clear advantage over our proposed method. In order to at least partially compensate for this, in our downstream task experiments we gather the set of contexts $\mathcal {C}$ for a given rare word from both the WWC and BooksCorpus during inference.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-7fdadf770fd8969893e5992fe728b2c3ce8d7ceb1a9cab51e4d2034232b7219e

Passage ID: `qasper-passage-v1-7fdadf770fd8969893e5992fe728b2c3ce8d7ceb1a9cab51e4d2034232b7219e`; retrieval score: 2.196185668500839.

Word count: 215.

```text
synonym, respectively. Consistent with results on WNLaMPro, combining BERT with Bertram outperforms both a standalone BERT model and one combined with Attentive Mimicking across all tasks. While keeping the original BERT embeddings in addition to Bertram's representation brings no benefit, adding in-domain data clearly helps for two out of three datasets. This makes sense as for rare words, every single additional context can be crucial for gaining a deeper understanding.

To further understand for which words using Bertram is helpful, in Figure FIGREF39 we look at the accuracy of BERT both with and without Bertram on all three tasks as a function of word frequency. That is, we compute the accuracy scores for both models when considering only entries $(\mathbf {x}_{w_{i_1} = \hat{w}_{i_1}, \ldots , w_{i_k} = \hat{w}_{i_k} }, y)$ where each substituted word $\hat{w}_{i_j}$ occurs less than $c_\text{max}$ times in WWC and BooksCorpus, for various values of $c_\text{max}$. As one would expect, $c_\text{max}$ is positively correlated with the accuracies of both models, showing that the rarer a word is, the harder it is to understand. Perhaps more interestingly, for all three datasets the gap between Bertram and BERT remains more or less constant regardless of $c_\text{max}$. This indicates that using Bertram might also be useful for even more frequent words than the ones considered.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1026.

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

#### Rank 1: qasper-passage-v1-65a9d8cdb353296dbe32f01bf5def2e068a01a22bf1fe98a96d8f13aa0019e0e

Passage ID: `qasper-passage-v1-65a9d8cdb353296dbe32f01bf5def2e068a01a22bf1fe98a96d8f13aa0019e0e`; retrieval score: 5.693761380060521.

Word count: 250.

```text
most previous work on rare words was evaluated on datasets explicitly focusing on such words BIBREF6, BIBREF3, BIBREF4, BIBREF5, BIBREF10, all of these datasets are tailored towards context-independent embeddings and thus not suitable for evaluating our proposed model. Furthermore, understanding rare words is of negligible importance for most commonly used downstream task datasets. To evaluate our proposed model, we therefore introduce a novel procedure that allows us to automatically turn arbitrary text classification datasets into ones where rare words are guaranteed to be important. This is achieved by replacing classification-relevant frequent words with rare synonyms obtained using semantic resources such as WordNet BIBREF20.

Using this procedure, we extract rare word datasets from three commonly used text (or text pair) classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. On both the WNLaMPro dataset of BIBREF0 and all three so-obtained datasets, our proposed Bertram model outperforms previous work by a large margin.

In summary, our contributions are as follows:

We show that a pretrained BERT instance can be integrated into Attentive Mimicking, resulting in much better context representations and a deeper connection of form and context.

We design a procedure that allows us to automatically transform text classification datasets into datasets for which rare words are guaranteed to be important.

We show that Bertram achieves a new state-of-the-art on the WNLaMPro probing task BIBREF0 and beats all baselines on rare word instances of AG's News, MNLI and DBPedia, resulting in an absolute improvement of up to 24% over a BERT
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-8354da125773185e453ffffb962b4acfdffab3d1478e1af6002b74dc499df1a8

Passage ID: `qasper-passage-v1-8354da125773185e453ffffb962b4acfdffab3d1478e1af6002b74dc499df1a8`; retrieval score: 5.102913467057298.

Word count: 250.

```text
As traditional word embedding algorithms BIBREF1 are known to struggle with rare words, several techniques for improving their representations have been proposed over the last few years. These approaches exploit either the contexts in which rare words occur BIBREF2, BIBREF3, BIBREF4, BIBREF5, their surface-form BIBREF6, BIBREF7, BIBREF8, or both BIBREF9, BIBREF10. However, all of these approaches are designed for and evaluated on uncontextualized word embeddings.

With the recent shift towards contextualized representations obtained from pretrained deep language models BIBREF11, BIBREF12, BIBREF13, BIBREF14, the question naturally arises whether these approaches are facing the same problem. As all of them already handle rare words implicitly – using methods such as byte-pair encoding BIBREF15 and WordPiece embeddings BIBREF16, or even character-level CNNs BIBREF17 –, it is unclear whether these models even require special treatment of rare words. However, the listed methods only make use of surface-form information, whereas BIBREF9 found that for covering a wide range of rare words, it is crucial to consider both surface-form and contexts.

Consistently, BIBREF0 recently showed that for BERT BIBREF13, a popular pretrained language model based on a Transformer architecture BIBREF18, performance on a rare word probing task can significantly be improve by relearning representations of rare words using Attentive Mimicking BIBREF19. However, their proposed model is limited in two important respects:

For processing contexts, it uses a simple bag-of-words model, throwing away much of the available information.

It combines form and context only in a shallow fashion, thus preventing both input signals from sharing information in
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-bd7c6e1c20df2f28116ac5e2440591a30813c29a32416c88ea2a220cf7cc0f2f

Passage ID: `qasper-passage-v1-bd7c6e1c20df2f28116ac5e2440591a30813c29a32416c88ea2a220cf7cc0f2f`; retrieval score: 5.064183007203183.

Word count: 41.

```text
We show that Bertram achieves a new state-of-the-art on the WNLaMPro probing task BIBREF0 and beats all baselines on rare word instances of AG's News, MNLI and DBPedia, resulting in an absolute improvement of up to 24% over a BERT baseline.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-e5bd889edea80e62afa8a3fc0381b16ede81cfa67c7c9b27050fe93f4630fc72

Passage ID: `qasper-passage-v1-e5bd889edea80e62afa8a3fc0381b16ede81cfa67c7c9b27050fe93f4630fc72`; retrieval score: 4.407695647257327.

Word count: 250.

```text
We evalute Bertram on the WNLaMPro dataset of BIBREF0. This dataset consists of cloze-style phrases like

and the task is to correctly fill the slot (____) with one of several acceptable target words (e.g., “fruit”, “bush” and “berry”), which requires knowledge of the phrase's keyword (“lingonberry” in the above example). As the goal of this dataset is to probe a language model's ability to understand rare words without any task-specific finetuning, BIBREF0 do not provide a training set. Furthermore, the dataset is partitioned into three subsets; this partition is based on the frequency of the keyword, with keywords occurring less than 10 times in the WWC forming the rare subset, those occurring between 10 and 100 times forming the medium subset, and all remaining words forming the frequent subset. As our focus is on improving representations for rare words, we evaluate our model only on the former two sets.

Results on WNLaMPro rare and medium are shown in Table TABREF34, where the mean reciprocal rank (MRR) is reported for BERT, Attentive Mimicking and Bertram. As can be seen, supplementing BERT with any of the proposed relearning methods results in noticeable improvements for the rare subset, with add clearly outperforming replace. Moreover, the add and add-gated variants of Bertram perform surprisingly well for more frequent words, improving the score for WNLaMPro-medium by 50% compared to BERT$_\text{base}$ and 31% compared to Attentive Mimicking. This makes sense considering that compared to Attentive Mimicking, the key enhancement of Bertram lies in improving context representations
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1910.07181:10:0` | full | 0:104 |

#### Rank 5: qasper-passage-v1-f7cce81c4bc2129e34120976e174813ec9ea0ed7098be4c2014975e809eba930

Passage ID: `qasper-passage-v1-f7cce81c4bc2129e34120976e174813ec9ea0ed7098be4c2014975e809eba930`; retrieval score: 3.9549614651328975.

Word count: 250.

```text
sequence of uncontextualized token embeddings $\mathbf {e} = e_1, \ldots , e_n$ where $e_{i}, \ldots , e_{i+j}$ with $1 \le i \le i+j \le n$ is the sequence of WordPiece embeddings for a single rare word $w$, we replace $\mathbf {e}$ with

By default, the set of contexts $\mathcal {C}$ required for this replacement is obtained by collecting all sentences from the WWC and BooksCorpus in which $w$ occurs. As our model architecture allows us to easily include new contexts without requiring any additional training, we also try a variant where we add in-domain contexts by giving the model access to the texts found in the test set.

In addition to the procedure described above, we also try a variant where instead of replacing the original WordPiece embeddings for a given rare word, we merely add the Bertram-based embedding, separating both representations using a single slash:

As it performs best on the rare and medium subsets of WNLaMPro combined, we use only the add-gated variant of Bertram for all datasets. Results can be seen in Table TABREF37, where for each task, we report the accuracy on the entire dataset as well as scores obtained considering only instances where at least one word was replaced by a misspelling or a WordNet synonym, respectively. Consistent with results on WNLaMPro, combining BERT with Bertram outperforms both a standalone BERT model and one combined with Attentive Mimicking across all tasks. While keeping the original BERT embeddings in addition to Bertram's representation brings no benefit,
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1041.

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

#### Rank 1: qasper-passage-v1-4ef91995283e76fb24711ff13e6840cb3c97c6cc3d38b12e7f6be8032df9cd5e

Passage ID: `qasper-passage-v1-4ef91995283e76fb24711ff13e6840cb3c97c6cc3d38b12e7f6be8032df9cd5e`; retrieval score: 3.270832366661941.

Word count: 123.

```text
The primary question we investigate with this model is what kind of input is best for generating accurate and informative citation sentences. Prior works in citation recommendation have made use of abstracts, which perhaps act as sufficient summaries of document content for this task. Additionally, we explore variants of extended context, such as the introduction or first section after the abstract. Since scientific texts are too long to fit into the context window of our generation model, we also investigate a “sampling” approach which samples sentences from throughout the document until the context window is full. In this work, we combine either the abstract or introduction of the source document with each of the abstract, introduction, or sampled sentences from the cited document.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-94a4d367b0dd48b37fc61c0f847a6e38f160c01bbd737a75a1f5ee8c84eb6d5e

Passage ID: `qasper-passage-v1-94a4d367b0dd48b37fc61c0f847a6e38f160c01bbd737a75a1f5ee8c84eb6d5e`; retrieval score: 2.8378076964108874.

Word count: 75.

```text
significance is assessed for select results using bootstrapping with 1000 samples in each of 100 iterations. This test shows that conditioning on the introduction of the source document improves performance compared to conditioning on the abstract when using the SciGPT2 model. However, we see that IR methods perform better than the best neural models. We do not find enough evidence to reject the null hypothesis regarding what context from the cited document should be used.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2002.00317:7:3` | partial | 12:489 |

#### Rank 3: qasper-passage-v1-4539996f52c840dc396165ca38a2b96c670b510a810be2ef7693beb7a33c9e94

Passage ID: `qasper-passage-v1-4539996f52c840dc396165ca38a2b96c670b510a810be2ef7693beb7a33c9e94`; retrieval score: 2.2464568352082144.

Word count: 250.

```text
We compare the different baseline systems using BLEU BIBREF12, ROUGE (specifically ROUGE 1, 2, and L; BIBREF13), and the recently introduced BertScore BIBREF14, a similarity metric based on BERT embeddings which has been shown to correlate well with human judgements on other tasks. To adapt the BertScore metric to the scientific text domain, we use SciBERT embeddings.

Table TABREF7 (above the double line) shows the performance of the SciGPT2 model on the test set when provided with the different input context combinations outlined in Section SECREF5. We find that context does make a difference for this category of model, and that models which have access to the intro of the documents outperform those which use abstracts or sampling.

Automatic evaluation of the retrieval-based methods on the test data are shown below the double line in Table TABREF7. This table shows that the retrieval methods perform well on this task. However we will show the limitations of these automatic metrics in Section SECREF14. We also observe that tuning the $\alpha $ and $\beta $ parameters on the validation set results in overfitting for this method. Outputs are largely unchanged by this tuning; fewer than 400 test datapoints differ from the untuned outputs. A larger validation split may alleviate this problem.

Statistical significance is assessed for select results using bootstrapping with 1000 samples in each of 100 iterations. This test shows that conditioning on the introduction of the source document improves performance compared to conditioning on the abstract when using the SciGPT2
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2002.00317:7:3` | partial | 0:282 |

#### Rank 4: qasper-passage-v1-ce8a60c4646bbcdeafaf2a1f780a7009cebb564b521cdbbd0ebc206a5cf0b2b7

Passage ID: `qasper-passage-v1-ce8a60c4646bbcdeafaf2a1f780a7009cebb564b521cdbbd0ebc206a5cf0b2b7`; retrieval score: 1.8659126004166269.

Word count: 250.

```text
be incorporated into writing assistance systems to help less experienced or non-native writers better articulate the connection between their work and prior art. Additionally, users of citation recommendation systems can benefit from natural language explanations of recommendation system choices.

Beyond the immediate utility of citation text generation systems, the task offers significant challenges for language understanding and generation research. A major challenge is how to represent the information in one or more scientific texts. These documents are longer than those in most other domains typically studied in NLP, and make use of a long-tailed, open-domain technical vocabulary. Often an important phrase in the citing sentence output occurs only in a specific cited document and not elsewhere in the corpus. This requires a model that can learn phrase meanings from very few exposures, an important but unsolved problem for text generation systems. Possibly more challenging is understanding and expressing the various and nuanced relationships between related scientific works.

In this work, we introduce the task of citation text generation. Leveraging the full texts of English-language scientific articles, we construct a dataset of citation sentences in the computer science domain for training and evaluating citation text generation models. We investigate strong retrieval and neural baseline models against which future work can compare. For use cases where large models can be trained, we extend the successful GPT2 architecture BIBREF6 to the scientific domain with additional pre-training and subsequent fine-tuning on the citation generation task. We experiment with different kinds of document context in
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-d801a29c312f408857a901779e23cd9540529b16e916f1efecbc7247a87c2715

Passage ID: `qasper-passage-v1-d801a29c312f408857a901779e23cd9540529b16e916f1efecbc7247a87c2715`; retrieval score: 1.8065340924425752.

Word count: 157.

```text
The fluency and topical relevance of the baseline models show the plausibility of the citation text generation task as well as the utility of including pretrained scientific language models in future models. But based on the kinds of errors we have seen, future work should focus on two complementary goals: ensuring the factual accuracy of the generated text and improved modeling of the cited document. Factual accuracy is difficult to enforce in statistical text generation systems, especially where inference includes sampling procedures. Grounding to knowledge bases could help. For this task, knowledge extracted from candidate generations could be compared with knowledge from the full source and cited documents to prune false or irrelevant statements. Further, modeling input documents as knowledge graphs of their contents may help these algorithms better understand the cited document, resulting in better outputs. However, such a model will have to address the open problem of combining pretrained language models with graph encoding techniques.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 855.

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

#### Rank 1: qasper-passage-v1-13925fcd34cebfb0d26b44b84133ad6d25c1329c2a304625d3486b8b72297fce

Passage ID: `qasper-passage-v1-13925fcd34cebfb0d26b44b84133ad6d25c1329c2a304625d3486b8b72297fce`; retrieval score: 5.892966999591861.

Word count: 158.

```text
The stock price data of Microsoft are labeled suitably for training using a simple program. If the previous day stock price is more than the current day stock price, the current day is marked with a numeric value of 0, else marked with a numeric value of 1. Now, this correlation analysis turns out to be a classification problem. The total positive, negative and neutral emotions in tweets in a 3 day period are calculated successively which are used as features for the classifier model and the output is the labeled next day value of stock 0 or 1.The window size is experimented and best results are achieved when the sentiment values precede 3 days to the stock price. A total of 355 instances, each with 3 attributes are fed to the classifier with a split proportions of 80% train dataset and the remaining dataset for testing. The accuracy of the classifier is discussed in the results section.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-2b90b411fbb28f93b099de7d1f795cb3227dcd2d68ff97c40fec258740712556

Passage ID: `qasper-passage-v1-2b90b411fbb28f93b099de7d1f795cb3227dcd2d68ff97c40fec258740712556`; retrieval score: 5.527753410747798.

Word count: 141.

```text
A classifier is presented in the previous sections that is trained with aggregate sentiment values for 3-day period as features and the increase/decrease in stock price represented by 1/0 as the output. Total data is split into two parts, 80 percent to train the model and remaining for testing operations. The classifier results show an accuracy value of 69.01% when trained using Logistic regression algorithm and the accuracy rate varied with the training set. When the model with LibSVM is trained with 90 percent of data, it gave a result of 71.82%. These results give a significant edge to the investors and they show good correlation between stock market movements and the sentiments of public expressed in twitter. This trend shows that with increasing dataset the models are performing well. We would like to incorporate more data in our future work.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-d37f5d20aab50004ace2bca5ef9e68bfe6ee03189df188f169f778f2f303c89c

Passage ID: `qasper-passage-v1-d37f5d20aab50004ace2bca5ef9e68bfe6ee03189df188f169f778f2f303c89c`; retrieval score: 5.033746645676681.

Word count: 218.

```text
The above sections discussed the method followed to train the classifier used for sentiment analysis of tweets. The classifier with features as Word2vec representations of human annotated tweets trained on Random Forest algorithm with a split percentage of 90 for training the model and remaining for testing the model showed an accuracy of 70.2%. With N-gram representations, the classifier model with same algorithm and with same dataset showed an accuracy of 70.5%. Though the results are very close, model trained with word2vec representations is picked to classify the nonhuman annotated tweets because of its promising accuracy for large datasets and the sustainability in word meaning. Numerous studies have been conducted on people and they concluded that the rate of human concordance, that is the degree of agreement among humans on the sentiment of a text, is between 70% and 79% BIBREF21 . They have also synthesized that sentiment analyzers above 70% are very accurate in most of the cases. Provided this information, the results we obtained from the sentiment classification can be observed as very good figures while predicting the sentiments in short texts, tweets, less than 140 characters in length. Table-2 depicts the results of sentiment classification including accuracy, precision, F-measure and recall when trained with different machine learning algorithms. ROC curves are plotted for detailed analysis.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-79f760a091e7a478924f986c0cd13947eef19a93b973e3e7bf8997fed39b9230

Passage ID: `qasper-passage-v1-79f760a091e7a478924f986c0cd13947eef19a93b973e3e7bf8997fed39b9230`; retrieval score: 4.620967680520635.

Word count: 125.

```text
In this work, we have considered only twitter data for analyzing people's sentiment which may be biased because not all the people who trade in stocks share their opinions on twitter. Stocktwits BIBREF22 is a financial communication platform designed solely for sharing ideas and insights of investors, entrepreneurs and traders. The current study can be extended by incorporating stocktwits data. In addition to this, data from news can also be included for an exhaustive public opinion collection.

While training the sentiment analyzer, 3,216 tweets are used which is comparatively a less number to train a sentiment analyzer. In future, we look forward to human annotate more than 10,000 tweets and train the classifiers. With increasing size of training datasets, the models tend to perform better.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-040eb452cf830a5bb86cbca5c1e3e466d7705cb2851995a7108a44804f70cb52

Passage ID: `qasper-passage-v1-040eb452cf830a5bb86cbca5c1e3e466d7705cb2851995a7108a44804f70cb52`; retrieval score: 3.97343307279261.

Word count: 56.

```text
used to classify the sentiments in tweets extracted.The human annotated dataset in our work is also exhaustive. We have shown that a strong correlation exists between twitter sentiments and the next day stock prices in the results section. We did so by considering the tweets and stock opening and closing prices of Microsoft over a year.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 698.

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

#### Rank 1: qasper-passage-v1-5670842feec68361f496de650712a4158af4843c72ba0262f28440215ec68da1

Passage ID: `qasper-passage-v1-5670842feec68361f496de650712a4158af4843c72ba0262f28440215ec68da1`; retrieval score: 2.219941055168461.

Word count: 79.

```text
While image and sound come with a natural high dimensional embedding, the issue of which is the best representation is still an open research problem in the context of natural language and text. It is beyond the scope of this paper to do a thorough overview of word representations, for this we refer the interest reader to the excellent review provided by BIBREF1 . Here, we will just introduce the main representations that are related to the proposed method.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-065c05be2a98231bef04b69b98c3cdc2704a60f97e3a8b4b987705e92a70d1ea

Passage ID: `qasper-passage-v1-065c05be2a98231bef04b69b98c3cdc2704a60f97e3a8b4b987705e92a70d1ea`; retrieval score: 1.9717701486712798.

Word count: 101.

```text
In this paper, we presented the network architecture used for the Fortia-FBK submission to the Semeval-2017 Task 5, Subtask 2 challenge, with the goal of predicting positive (bullish) or negative (bearish) attitude towards a target brand from financial news headlines. The proposed system ranked 1st in such challenge.

Our approach is based on 1d convolutions and uses fine-tuning of unsupervised word representations and a rule based sentiment model in its inputs. We showed that the use of pre-computed word representations allows to reduce over-fitting and to achieve significantly better generalization, while some basic pre-processing was needed to further improve the performance.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-0c9e52dc60bc424714216c940f2b9857d2fe246179e002366de061cf75378724

Passage ID: `qasper-passage-v1-0c9e52dc60bc424714216c940f2b9857d2fe246179e002366de061cf75378724`; retrieval score: 0.0.

Word count: 250.

```text
Real time information is key for decision making in highly technical domains such as finance. The explosive growth of financial technology industry (Fintech) continued in 2016, partially due to the current interest in the market for Artificial Intelligence-based technologies.

Opinion-rich texts such as micro-blogging and news can have an important impact in the financial sector (e.g. raise or fall in stock value) or in the overall economy (e.g. the Greek public debt crisis). In such a context, having granular access to the opinions of an important part of the population is of key importance to any public and private actor in the field. In order to take advantage of this raw data, it is thus needed to develop machine learning methods allowing to convert unstructured text into information that can be managed and exploited.

In this paper, we address the sentiment analysis problem applied to financial headlines, where the goal is, for a given news headline and target company, to infer its polarity score i.e. how positive (or negative) the sentence is with respect to the target company. Previous research BIBREF0 has highlighted the association between news items and market fluctiations; hence, in the financial domain, sentiment analysis can be used as a proxy for bullish (i.e. positive, upwards trend) or bearish (i.e. negative, downwards trend) attitude towards a specific financial actor, allowing to identify and monitor in real-time the sentiment associated with e.g. stocks or brands.

Our contribution leverages pre-trained word embeddings (GloVe, trained on wikipedia+gigaword corpus), the DepecheMood
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1704.00939:0:3` | partial | 0:117 |

#### Rank 4: qasper-passage-v1-23c45f74911c2874de24ca13979ae7daee9b262609ad9732631d8e2ac7df712a

Passage ID: `qasper-passage-v1-23c45f74911c2874de24ca13979ae7daee9b262609ad9732631d8e2ac7df712a`; retrieval score: 0.0.

Word count: 13.

```text
In Figure FIGREF5 , we can see the overall architecture of our model.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-38dbf69fad557a0a1e53cf7a3b3502c0bff165b84c191e3a5b1d3fbe82a55a7a

Passage ID: `qasper-passage-v1-38dbf69fad557a0a1e53cf7a3b3502c0bff165b84c191e3a5b1d3fbe82a55a7a`; retrieval score: 0.0.

Word count: 250.

```text
A 1D convolutional layer with filters of multiple sizes {2, 3, 4} is applied to the sequence of word embeddings. The filters are used to learn useful translation-invariant representations of the sequential input data. A global max-pooling is then applied across the sequence for each filter output.

We apply the concatenation layer to the output of the global max-pooling and the output of VADER.

The activation function used between layers is ReLU BIBREF24 except for the out layer where tanh is used to map the output into [-1, 1] range.

Dropout BIBREF25 was used to avoid over-fitting to the training data: it prevents the co-adaptation of the neurones and it also provides an inexpensive way to average an exponential number of networks. In addition, we averaged the output of multiple networks with the same architecture but trained independently with different random seeds in order to reduce noise.

The loss function used is the cosine distance between the predicted scores and the gold standard for each batch. Even though stochastic optimization methods like Adam BIBREF26 are usually applied to loss functions that are written as a sum of per-sample loss, which is not the case for the cosine, it converges to an acceptable solution. The loss can be written as : DISPLAYFORM0

where INLINEFORM0 and INLINEFORM1 are the predicted and true sentiment scores for batch INLINEFORM2 , respectively.

The algorithm for training/testing our model is reported in Algorithm UID15 .

InputInput OutputOutput ParameterParameters A set of trained models INLINEFORM0 , and
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 693.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "527a86257787c039331092a3217b16a2f0847649": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1704.00939:0:3": [
        [
          117,
          171
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-ec7830e388274acb3a4f220932a04bae2db288f7980bf54768ecd6d3143ceaf1

Passage ID: `qasper-passage-v1-ec7830e388274acb3a4f220932a04bae2db288f7980bf54768ecd6d3143ceaf1`; retrieval score: 7.911761347234814.

Word count: 250.

```text
Neural machine translation (NMT) typically makes use of a recurrent neural network (RNN) -based encoder and decoder, along with an attention mechanism BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 . However, it has been shown that RNNs require some supervision to learn syntax BIBREF4 , BIBREF5 , BIBREF6 . Therefore, explicitly incorporating syntactic information into NMT has the potential to improve performance. This is particularly true for source syntax, which can improve the model's representation of the source language.

Recently, there have been a number of proposals for using linearized representations of parses within standard NMT BIBREF7 , BIBREF8 , BIBREF9 . Linearized parses are advantageous because they can inject syntactic information into the models without significant changes to the architecture. However, using linearized parses in a sequence-to-sequence (seq2seq) framework creates some challenges, particularly when using source parses. First, the parsed sequences are significantly longer than standard sentences, since they contain node labels as well as words. Second, these systems often fail when the source sentence is not parsed. This can be a problem for inference, since the external parser may fail on an input sentence at test time. We propose a method for incorporating linearized source parses into NMT that addresses these challenges by taking both the sequential source sentence and its linearized parse simultaneously as input in a multi-source framework. Thus, the model is able to use the syntactic information encoded in the parse while falling back to the sequential sentence when necessary. Our proposed model improves over
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-416a3dd3b57e81868620f3c42f039a1a2108991c1319c4a49f4f3b61a5d7f8d1

Passage ID: `qasper-passage-v1-416a3dd3b57e81868620f3c42f039a1a2108991c1319c4a49f4f3b61a5d7f8d1`; retrieval score: 6.426640708637178.

Word count: 180.

```text
The idea of incorporating linearized parses into seq2seq has been adapted to NMT as a means of injecting syntax. aharoni2017towards first did this by parsing the target side of the training data and training the system to generate parsed translations of the source input; this is the inverse of our parse2seq baseline. Similarly, nadejde2017syntax interleaved CCG supertags with words on the target side, finding that this improved translation despite requiring longer sequences.

Most similar to our multi-source model is the parallel RNN model proposed by li2017modeling. Like multi-source, the parallel RNN used two encoders, one for words and the other for syntax. However, they combined these representations at the word level, whereas we combine them on the sentence level. Their mixed RNN model is also similar to our parse2seq baseline, although the mixed RNN decoder attended only to words. As the mixed RNN model outperformed the parallel RNN model, we do not attempt to compare our model to parallel RNN. These models are similar to ours in that they incorporate linearized parses into NMT; here, we utilize a multi-source framework.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-131da1e82710038761b7ed4af02f6061bc91cc1caae75b316c674cb9fdcc7715

Passage ID: `qasper-passage-v1-131da1e82710038761b7ed4af02f6061bc91cc1caae75b316c674cb9fdcc7715`; retrieval score: 5.396281103103659.

Word count: 131.

```text
We propose a multi-source framework for injecting linearized source parses into NMT. This model consists of two identical RNN encoders with no shared parameters, as well as a standard RNN decoder. For each target sentence, two versions of the source sentence are used: the sequential (standard) version and the linearized parse (lexicalized or unlexicalized). Each of these is encoded simultaneously using the encoders; the encodings are then combined and used as input to the decoder. We combine the source encodings using the hierarchical attention combination proposed by libovicky2017attention. This consists of a separate attention mechanism for each encoder; these are then combined using an additional attention mechanism over the two separate context vectors. This multi-source method is thus able to combine the advantages of both standard RNN-based encodings and syntactic encodings.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-4dee579f799a2ead2e6875596aa740794e15f0dbf5d49c48f92baa50b40c9c20

Passage ID: `qasper-passage-v1-4dee579f799a2ead2e6875596aa740794e15f0dbf5d49c48f92baa50b40c9c20`; retrieval score: 5.341922901350823.

Word count: 46.

```text
sentence and its linearized parse simultaneously as input in a multi-source framework. Thus, the model is able to use the syntactic information encoded in the parse while falling back to the sequential sentence when necessary. Our proposed model improves over both standard and parsed NMT baselines.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-34dfc145bd762d17a5dafc3e2e83418df1f856e1c75ff845a3f414fa6c5bae82

Passage ID: `qasper-passage-v1-34dfc145bd762d17a5dafc3e2e83418df1f856e1c75ff845a3f414fa6c5bae82`; retrieval score: 5.198024210847481.

Word count: 122.

```text
In this paper, we presented a multi-source method for effectively incorporating linearized parses of the source data into neural machine translation. This method, in which the parsed and sequential versions of the sentence were both taken as input during training and inference, resulted in gains of up to 1.5 BLEU on EN INLINEFORM0 DE translation. In addition, unlike parse2seq, the multi-source model translated reasonably well even when the source sentence was not parsed.

In the future, we will explore adding back-translated BIBREF18 or copied BIBREF19 target data to our multi-source system. The multi-source model does not require all training data to be parsed; thus, monolingual data can be used even if the parser is unreliable for the synthetic or copied source sentences.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 729.

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

#### Rank 1: qasper-passage-v1-7e2a33fc3c12a6962485439fa5fae600e891badec426f73382614db24cd08ab0

Passage ID: `qasper-passage-v1-7e2a33fc3c12a6962485439fa5fae600e891badec426f73382614db24cd08ab0`; retrieval score: 4.883199147442138.

Word count: 250.

```text
A large majority of the human knowledge is recorded through text documents. That is why ability for a system to automatically infer information from text without any structured data has become a major challenge. Answering questions about a given document is a relevant proxy task that has been proposed as a way to evaluate the reading ability of a given model. In this configuration, a text document such as a news article, a document from Wikipedia or any type of text is presented to a machine with an associated set of questions. The system is then expected to answer these questions and evaluated by its accuracy on this task. The machine reading framework is very general and we can imagine a large panel of questions that can possibly handle most of the standard natural language processing tasks. For example, the task of named entities recognition can be formulated as a machine reading one where your document is the sentence and the question would be 'What are the named entities mentioned in this sentence?'. These natural language interactions are an important objective for reading systems.

Recently, many datasets have been proposed to build and evaluate reading models BIBREF0 , BIBREF1 . From cloze style questions BIBREF2 to open questions BIBREF3 , from synthetic data BIBREF4 to human written articles BIBREF5 , many styles of documents and questions have been proposed to challenge reading models. The correct answer to the questions proposed in most of these datasets is a span of text
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-685ce6646fca40c9d90fe6dbfac9c9bc2f2e5573b857ecbd829f59efbfe4c015

Passage ID: `qasper-passage-v1-685ce6646fca40c9d90fe6dbfac9c9bc2f2e5573b857ecbd829f59efbfe4c015`; retrieval score: 4.356185108725625.

Word count: 214.

```text
Table TABREF19 displays the performance of the 4 baselines on the ReviewQA's test set. These results are the performance achieved by our own implementation of these 4 models. According to our results, the simple LSTM network and the MemN2N perform very poorly on this dataset. Especially on the most advanced reasoning tasks. Indeed, the task 5 which corresponds to the prediction of the exact rating of an aspect seems to be very challenging for these model. Maybe the tokenization by sentence to create the memory blocks of the MemN2N, which is appropriated in the case of the bAbI tasks, is not a good representation of the documents when it has to handle human generated comments. However, the logistic regression achieves reasonable performance on these tasks, and do not suffer from catastrophic performance on any tasks. Its worst result comes on task 6 and one of the reason is probably that this architecture is not designed to predict a list of answers. On the contrary, the deep projective reader achieves encouraging on this dataset. It outperforms all the other baselines, with very good scores on the first fourth tasks. The question/document and document/document attention layers proposed in BIBREF12 seem once again to produce rich encodings of the inputs which are relevant for our projection layer.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-ec4f82654003d61b456d867b33eea67742b2e5eb34c16e629726852cccdef601

Passage ID: `qasper-passage-v1-ec4f82654003d61b456d867b33eea67742b2e5eb34c16e629726852cccdef601`; retrieval score: 2.2222154291657157.

Word count: 250.

```text
Objective: Starting with the original corpus, we aim at building a machine reading task where natural language questions will challenge the model on its understanding of the reviews. Indeed learning relational reasoning competencies over natural language documents is a major challenge of the current reading models. These original raw data allow us to generate relational questions that can possibly require a global understanding of the comment and reasoning skills to be treated. For example, asking a question like What is the best aspect rated in this comment ? is not an easy question that can be answered without a deep understanding of the review. It is necessary to capture all the aspects mentioned in the text, to predict their rating and finally to select the best one. The tasks and the dataset we propose are publicly available at http://www.europe.naverlabs.com/Blog/ReviewQA-A-novel-relational-aspect-based-opinion-dataset-for-machine-reading

We introduce a list of 8 different competencies that a reading system should master in order to process reviews and text documents in general. These 8 tasks require different competencies and a different level of understanding of the document to be well answered. For instance, detecting if an aspect is mentioned in a review will require less understanding of the review than predicting explicitly the rating of this aspect. Table TABREF10 presents the 8 tasks we have introduced in this dataset with an example of a question that corresponds to each task. We also provide the expected type of the answer (Yes/No question, rating question...). It can be an additional tool
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-d0a647e53c65a10d516b72c35c48f77ebc4b3994e2a8bdc90b69fcc5227c3714

Passage ID: `qasper-passage-v1-d0a647e53c65a10d516b72c35c48f77ebc4b3994e2a8bdc90b69fcc5227c3714`; retrieval score: 1.023256642560168.

Word count: 250.

```text
120.000 human generated questions over 12.000 articles form CNN originally introduced in BIBREF5 . It has been designed to be more challenging than SQuAD with questions that might require to extract multiple spans of text or not be answerable.

WikiHop and MedHop: These are two recent datasets introduced in BIBREF13 . Unlike SQuAD and NewsQA, important facts are spread out across multiple documents and, in order to answer a question, it is necessary to jump over a set of passages to collect the required information. The relevant passages are not explicitly mentioned in the data so this dataset measures the ability that a model has to navigate across multiple documents. The questions come with a set of candidates which are all present in the text.

MS Marco: This dataset has been released in BIBREF14 . The documents come from the internet and the questions are real user queries asked through the bing search engine. The dataset contains around 100.000 queries and each of them comes with a set of approximatively 10 relevant passages. Like in SQuAD, several models are already doing superhuman performances on this dataset.

Facebook bAbI tasks: This is a set of 20 toy tasks proposed in BIBREF4 and designed to measure text understanding. Each task requires a certain capability to be completed like induction, deduction and more. Documents are synthetic stories, composed of few sentences that describe a set of actions. This dataset was one of the first attempt to introduce a general set of prerequisite capabilities
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-e6c4b40920bd10d03fe9b9472883b78dacfac36847dc5e4436c487f45addb244

Passage ID: `qasper-passage-v1-e6c4b40920bd10d03fe9b9472883b78dacfac36847dc5e4436c487f45addb244`; retrieval score: 0.8815993174076701.

Word count: 246.

```text
The questions are human-generated patterns that we have crowdsourced in order to produce a dataset as rich as possible. To this end, we have generated several patterns that correspond to the capabilities we wanted to express in a given question and we have crowdsourced rephrasing of these patterns.

The final dataset we propose is composed of more than 500.000 questions about 100.000 reviews. Table TABREF13 shows the repartition of the documents and queries into the train and test set. Each review contains a maximum of 6 questions. Sometimes less when it is not possible to generate all. For example, if only two or three aspects are mentioned in a review, we will be able to generate only a little set of relational questions. Figure FIGREF15 depicts the repartition of the answers in the generated dataset. A majority of the tasks we introduced, even if they possibly require a high level of understanding of the document and the question, are binary questions. It means that in the generated dataset the answers yes and no tend to be more present than the others. To balance in a better way the distribution of the answers, we chose to affect a higher probability of sampling to the task 5, 6, 7.1, 8. Indeed, these tasks are not binary questions and required an aspect name as the answer. Figure FIGREF17 represents the repartition of question types in our dataset. Finally, figure FIGREF15 shows the repartition of the answers in the dataset.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1210.

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

#### Rank 1: qasper-passage-v1-39f8ecfc29401e9276cd777181af9fa6dbbeef3340815fb3796a0d4e78d9ab2f

Passage ID: `qasper-passage-v1-39f8ecfc29401e9276cd777181af9fa6dbbeef3340815fb3796a0d4e78d9ab2f`; retrieval score: 5.1645798487835295.

Word count: 250.

```text
proposed method is more comprehensive than the reference, while the reference only includes the facts in the last sentence of the source content. In short, the generated summary of the proposed method is more consistent with the source content. It also exhibits the necessity of the proposed human evaluation. Because when the generated summary is evaluated against the reference, it may seem redundant or wrong, but it is actually true to the source content. While it is arguable that the generated summary is better than the reference, there is no doubt that the generated summary of the proposed method is better than the baseline. However, the improvement cannot be properly shown by the existing evaluation methods. Furthermore, the examples suggest that the proposed method does learn better correspondence. The highlighted words in each example in Table TABREF28 share almost the same previous words. However, in the first one, the baseline considers “UTF8gbsn停” (stop) as the most related words, which is a sign of noisy word relations learned from other training examples, while the proposed method generates “UTF8gbsn进站” (to the platform), which is more related to what a human thinks. It is the same with the second example, where a human selects “UTF8gbsn专家” (expert) and Dual-Train selects “UTF8gbsn工作者” (worker), while the baseline selects “UTF8gbsn钻研” (research) and fails to generate a grammatical sentence later. In the third one, the reference and the baseline use the same word, while Dual-Train chooses a word of the same meaning. It can be concluded that Dual-Train
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-bb3704de151262e78606f0cbe68c724a285621aa7d07ecfcbc29affddc3697e0

Passage ID: `qasper-passage-v1-bb3704de151262e78606f0cbe68c724a285621aa7d07ecfcbc29affddc3697e0`; retrieval score: 3.3313046621945586.

Word count: 250.

```text
is also a non-trivial task for Chinese. There are many kinds of segmentation rules, which will produce different ROUGE scores. We argue that it is not acceptable to introduce additional systematic bias in automatic evaluations, and automatic evaluation for semantically related tasks can only serve as a reference. To avoid the deficiencies, we propose a simple human evaluation method to assess the semantic consistency. Each summary candidate is evaluated against the text rather than the reference. If the candidate is irrelevant or incorrect to the text, or the candidate is not understandable, the candidate is labeled bad. Otherwise, the candidate is labeled good. Then, we can get an accuracy of the good summaries. The proposed evaluation is very simple and straight-forward. It focuses on the relevance between the summary and the text. The semantic consistency should be the major consideration when putting the text summarization methods into practice, but the current automatic methods cannot judge properly. For detailed guidelines in human evaluation, please refer to Appendix SECREF6 . In the human evaluation, the text-summary pairs are dispatched to two human annotators who are native speakers of Chinese. As in our setting the summary is evaluated against the reference, the number of the pairs needs to be manually evaluated is four times the number of the pairs in the test set, because we need to compare four systems in total. To decrease the workload and get a hint about the annotation quality at the same time, we adopt the following procedure.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1805.04033:7:0` | partial | 1379:2949 |

#### Rank 3: qasper-passage-v1-73bd6be5d78081733ede18645a0384513ac5cc26516616d8393a5ccd4f91fc2c

Passage ID: `qasper-passage-v1-73bd6be5d78081733ede18645a0384513ac5cc26516616d8393a5ccd4f91fc2c`; retrieval score: 3.2831975946081027.

Word count: 250.

```text
However, the aforementioned method tries to regularize the output word distribution based on what it has already learned. The relative order of the output words is kept. The self-dependency may not be desirable for regularization. It may be better if more correspondence that is spurious can be identified. In this paper, we further propose to obtain the soft target from a different view of the model, so that different knowledge of the dataset can be used to mitigate the overfitting problem. An additional output layer is introduced to generate the soft target. The two output layers share the same hidden representation but have independent parameters. They could learn different knowledge of the data. We refer to this approach as Dual-Train. For clarity, the original output layer is denoted by INLINEFORM0 and the new output layer INLINEFORM1 . Their outputs are denoted by INLINEFORM2 and INLINEFORM3 , respectively. The output layer INLINEFORM4 acts as the original output layer. We apply soft training using the output from INLINEFORM5 to this output layer to increase its ability of generalization. Suppose the correct label is INLINEFORM6 . The target of the output INLINEFORM7 includes both the one-hot distribution and the distribution generated from INLINEFORM8 : DISPLAYFORM0

The new output layer INLINEFORM0 is trained normally using the originally hard target. This output layer is not used in the prediction, and its only purpose is to generate the soft target to facilitate the soft training of INLINEFORM1 . Suppose the correct label is INLINEFORM2 . The
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-c42200f40f3186e110e038ee2f0247390344f175600613ab43bf59305d9ee0e4

Passage ID: `qasper-passage-v1-c42200f40f3186e110e038ee2f0247390344f175600613ab43bf59305d9ee0e4`; retrieval score: 3.1880894743225983.

Word count: 155.

```text
We propose a regularization approach for the sequence-to-sequence model on the Chinese social media summarization task. In the proposed approach, we use a cross-entropy based regularization term to make the model neglect the possible unrelated words. We propose two methods for obtaining the soft output word distribution used in the regularization, of which Dual-Train proves to be more effective. Experimental results show that the proposed method can improve the semantic consistency by 4% in terms of human evaluation. As shown by the analysis, the proposed method achieves the improvements by eliminating the less semantically-related word correspondence. The proposed human evaluation method is effective and efficient in judging the semantic consistency, which is absent in previous work but is crucial in the accurate evaluation of the text summarization systems. The proposed metric is simple to conduct and easy to interpret. It also provides an insight on how practicable the existing systems are in the real-world scenario.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-7e1168a857a0efce6a4f57c24f704fe44b6eb4aaddb345da58be8c5d7a8d55be

Passage ID: `qasper-passage-v1-7e1168a857a0efce6a4f57c24f704fe44b6eb4aaddb345da58be8c5d7a8d55be`; retrieval score: 3.09406315136063.

Word count: 184.

```text
robust correspondence of the source content and the output words can be learned, and potentially, the output summary will be more semantically consistent. To obtain the softened output word distribution, we propose two methods based on the sequence-to-sequence model.

More detailed explanation is introduced in Section SECREF2 . Another problem for abstractive text summarization is that the system summary cannot be easily evaluated automatically. ROUGE BIBREF9 is widely used for summarization evaluation. However, as ROUGE is designed for extractive text summarization, it cannot deal with summary paraphrasing in abstractive text summarization. Besides, as ROUGE is based on the reference, it requires high-quality reference summary for a reasonable evaluation, which is also lacking in the existing dataset for Chinese social media text summarization. We argue that for proper evaluation of text generation task, human evaluation cannot be avoided. We propose a simple and practical human evaluation for evaluating text summarization, where the summary is evaluated against the source content instead of the reference. It handles both of the problems of paraphrasing and lack of high-quality reference. The contributions of this work are summarized as follows:
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1805.04033:0:3` | full | 0:997 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 1089.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "d76d0cd894e1434896b72b8211bf1fa0e2db7703": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1805.04033:7:0": [
        [
          0,
          1379
        ],
        [
          2949,
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

#### Rank 1: qasper-passage-v1-5beebbad9081ca1cee655efb7e0016aadc27509d96a0e75e5599d49a39e1df17

Passage ID: `qasper-passage-v1-5beebbad9081ca1cee655efb7e0016aadc27509d96a0e75e5599d49a39e1df17`; retrieval score: 6.29193615323763.

Word count: 250.

```text
with the multi-task learning by weighing the losses of ASR, MT, and ST. This approach, however, causes a huge gap between pre-training and fine-tuning, which are summarized into three folds:

Subnet Waste: The ST system just reuses the ASR encoder and the MT decoder, while discards other pre-trained subnets, such as the MT encoder. Consequently, valuable semantic information captured by the MT encoder cannot be inherited by the final ST system.

Role Mismatch: The speech encoder plays different roles in pre-training and fine-tuning. The encoder is a pure acoustic model in pre-training, while it has to extract semantic and linguistic features additionally in fine-tuning, which significantly increases the learning difficulty.

Non-pre-trained Attention Module: Previous work BIBREF6 trains attention modules for ASR, MT and ST respectively, hence, the attention module of ST does not benefit from the pre-training.

To address these issues, we propose a Tandem Connectionist Encoding Network (TCEN), which is able to reuse all subnets in pre-training, keep the roles of subnets consistent, and pre-train the attention module. Concretely, the TCEN consists of three components, a speech encoder, a text encoder, and a target text decoder. Different from the previous work that pre-trains an encoder-decoder based ASR model, we only pre-train an ASR encoder by optimizing the Connectionist Temporal Classification (CTC) BIBREF8 objective function. In this way, the additional decoder of ASR is not required while keeping the ability to read acoustic features into the source language space by the speech encoder. Besides, the text encoder and decoder can
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-4267cd2fd862fdef37817ed3ce519c6472829fe3d478a0eeab253a0d1f3b1bfe

Passage ID: `qasper-passage-v1-4267cd2fd862fdef37817ed3ce519c6472829fe3d478a0eeab253a0d1f3b1bfe`; retrieval score: 6.166815889204184.

Word count: 170.

```text
To leverage large scale ASR and MT data, multi-task learning and pre-training techniques are widely employed to improve the ST system. As shown in Figure FIGREF4, there are three popular multi-task strategies for ST, including 1) one-to-many setting, in which a speech encoder is shared between ASR and ST tasks; 2) many-to-one setting in which a decoder is shared between MT and ST tasks; and 3) many-to-many setting where both the encoder and decoder are shared.

A many-to-many multi-task model contains two encoders as well as two decoders. It can be jointly trained on ASR, MT, and ST tasks. As the attention module is task-specific, three attentions are defined.

Usually, the size of $\mathcal {A}$ and $\mathcal {M}$ is much larger than $\mathcal {S}$. Therefore, the common training practice is to pre-train the model on ASR and MT tasks and then fine-tune it with a multi-task learning manner. However, as aforementioned, this method suffers from subnet waste, role mismatch and non-pre-trained attention issues, which severely limits the end-to-end ST performance.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-4f0295fe80154ab9982375188427fd2ff13841822d30f5a614947e7c7f54099f

Passage ID: `qasper-passage-v1-4f0295fe80154ab9982375188427fd2ff13841822d30f5a614947e7c7f54099f`; retrieval score: 5.1921429036236235.

Word count: 250.

```text
Classification (CTC) BIBREF8 objective function. In this way, the additional decoder of ASR is not required while keeping the ability to read acoustic features into the source language space by the speech encoder. Besides, the text encoder and decoder can be pre-trained on a large MT dataset. After that, we employ common used multi-task learning method to jointly learn ASR, MT and ST tasks.

Compared to prior works, the encoder of TCEN is a concatenation of an ASR encoder and an MT encoder and our model does not have an ASR decoder, so the subnet waste issue is solved. Furthermore, the two encoders work at tandem, disentangling acoustic feature extraction and linguistic feature extraction, ensuring the role consistency between pre-training and fine-tuning. Moreover, we reuse the pre-trained MT attention module in ST, so we can leverage the alignment information learned in pre-training.

Since the text encoder consumes word embeddings of plausible texts in MT task but uses speech encoder outputs in ST task, another question is how one guarantees the speech encoder outputs are consistent with the word embeddings. We further modify our model to achieve semantic consistency and length consistency. Specifically, (1) the projection matrix at the CTC classification layer for ASR is shared with the word embedding matrix, ensuring that they are mapped to the same latent space, and (2) the length of the speech encoder output is proportional to the length of the input frame, so it is much longer than a natural sentence. To bridge the
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-76a3c72aeae006f2e116eabb47181232f4fd0706bff28c787f048fed6f543295

Passage ID: `qasper-passage-v1-76a3c72aeae006f2e116eabb47181232f4fd0706bff28c787f048fed6f543295`; retrieval score: 5.142893401147992.

Word count: 250.

```text
Figure FIGREF5 sketches the overall architecture of TCEN, including a speech encoder $enc_s$, a text encoder $enc_t$ and a decoder $dec$ with an attention module $att$. During training, the $enc_s$ acts like an acoustic model which reads the input $\mathbf {x}$ to word or subword representations $\mathbf {h^s}$, then $enc_t$ learns high-level linguistic knowledge into hidden representations $\mathbf {h^t}$. Finally, the $dec$ defines a distribution probability over target words. The advantage of our architecture is that two encoders disentangle acoustic feature extraction and linguistic feature extraction, making sure that valuable knowledge learned from ASR and MT tasks can be effectively leveraged for ST training. Besides, every module in pre-training can be utilized in fine-tuning, alleviating the subnet waste problem.

Follow BIBREF9 inaguma2018speech, we use CNN-BiLSTM architecture to build our model. Specifically, the input features $\mathbf {x}$ are organized as a sequence of feature vectors in length $T_x$. Then, $\mathbf {x}$ is passed into a stack of two convolutional layers followed by max-pooling:

where $\mathbf {v}^{(l-1)}$ is feature maps in last layer and $\mathbf {W}^{(l)}$ is the filter. The max-pooling layers downsample the sequence in length by a total factor of four. The down-sampled feature sequence is further fed into a stack of five bidirectional $d$-dimensional LSTM layers:

where $[;]$ denotes the vector concatenation. The final output representation from the speech encoder is denoted as $\mathbf {h^s}=(h^s_1, \cdots , h^s_{\frac{T_x}{4}})$, where $h_i^s \in \mathbb {R}^d$.

The text encoder $enc_t$ consists of two bidirectional LSTM layers. In ST task, $enc_t$ accepts speech
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-82a52d7fa554611d79aa37965b70f8b745a6e15f6d1c2f5d36b7bf2d72fa8583

Passage ID: `qasper-passage-v1-82a52d7fa554611d79aa37965b70f8b745a6e15f6d1c2f5d36b7bf2d72fa8583`; retrieval score: 4.865770202934754.

Word count: 52.

```text
In this section, we first introduce the architecture of TCEN, which consists of two encoders connected in tandem, and one decoder with an attention module. Then we give the pre-training and fine-tuning strategy for TCEN. Finally, we propose our solutions for semantic and length inconsistency problems, which are caused by multi-task learning.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 972.

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

#### Rank 1: qasper-passage-v1-a4cba1cd8f9d0b60f9611655b0b376277a14a6387a5752b0ed61b82482961767

Passage ID: `qasper-passage-v1-a4cba1cd8f9d0b60f9611655b0b376277a14a6387a5752b0ed61b82482961767`; retrieval score: 9.05307813479897.

Word count: 250.

```text
This paper has used data-driven language mapping to select national dialects of English to be included in a global dialect identification model. The main experiments have focused on a dynamic syntactic feature set, showing that it is possible to predict dialect membership within-domain with only a small loss of performance against lexical models. This work raises two remaining problems:

First, we know that location-specific content (i.e., place names, place references, national events) can be used for geo-location and text-based models of place. To what degree does a lexical approach capture linguistic variation (i.e., “pop" vs. “soda") and to what degree is it capturing non-linguistic information (i.e., “Melbourne" vs. “London")? This is an essential problem for dialect identification models. A purely syntactic model does not perform as well as a lexical model, but it does come with more guarantees.

Second, we have seen that inner-circle varieties have higher feature densities given the grammars used here. This implies that there are syntactic constructions in varieties like Philippines English that have not been modeled by the grammar induction component. While dialect identification can be used to optimize regional weights for known constructions, how can such missing constructions be adapted? This remains a challenge. While the less proto-typical dialects have higher F1s (i.e., Pakistan English), they also have lower feature densities. This indicates that some of their constructions are missing from the grammar. Nevertheless, this paper has shown that a broader syntactic feature space can be used to model the difference between many national
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.05527:9:0` | full | 0:389 |

#### Rank 2: qasper-passage-v1-c879b2f59587c8426e621922b468ece774decfca54dc9076b3a07dbdbb64bca5

Passage ID: `qasper-passage-v1-c879b2f59587c8426e621922b468ece774decfca54dc9076b3a07dbdbb64bca5`; retrieval score: 6.553883463633127.

Word count: 217.

```text
of dialect areas. This is important for ensuring that each construction in the grammar receives the best regional weighting.

What syntactic features are needed to represent variation in English? As discussed in Section 6, this paper uses grammar induction on a large background corpus to provide a replicable and dynamic feature space in order to avoid arbitrary limitations (e.g., lists of function words). The other side of this problem is to optimize grammar induction for regional dialects by using an identification task to learn regional weights for each part of the grammar: how much does a single generic grammar of English vary across dialects? To what degree does it represent a single dominant dialect?

Finally, a corpus-based approach to variation is restricted to the specific domains or registers that are present in the corpus. To what degree is such a model of variation limited to a specific register? This paper uses both web-crawled corpora and social media corpora to explore the robustness of dialect models across domains (Section 8). Along these same lines, how robust is a model of syntactic variation to the presence of a few highly predictive features? This paper uses unmasking, a method from authorship verification (Koppel, et al., 2007), to evaluate the stability of dialect models over rounds of feature pruning (Section 9).
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-8acd276a145dcf1c4ed4014863ac27b3731e07dff47d3260e694e50545e9bff9

Passage ID: `qasper-passage-v1-8acd276a145dcf1c4ed4014863ac27b3731e07dff47d3260e694e50545e9bff9`; retrieval score: 5.891922390290686.

Word count: 250.

```text
This paper combines grammar induction (Dunn, 2018a, 2018b, 2019) and text classification (Joachims, 1998) to model syntactic variation across national varieties of English. This classification-based approach is situated within the task of dialect identification (Section 2) and evaluated against other baselines for the task (Sections 7 and 8). But the focus is modelling syntactic variation on a global-scale using corpus data. On the one hand, the problem is to use a model of syntactic preferences to predict an author's dialect membership (Dunn, 2018c). On the other hand, the problem is to take a spatially-generic grammar of English that is itself learned from raw text (c.f., Zeman, et al., 2017; Zeman, et al., 2018) and adapt that grammar using dialect identification as an optimization task: which constructions are more likely to occur in a specific regional variety?

Because we want a complete global-scale model, we first have to ask: how many national varieties of English are there? This question, considered in Sections 3 and 4, is essential for determining the inventory of regional varieties that need to be included in the dialect identification task. This paper uses data-driven language mapping to find out where English is consistently used, given web data and Twitter data, in order to avoid the arbitrary selection of dialect areas. This is important for ensuring that each construction in the grammar receives the best regional weighting.

What syntactic features are needed to represent variation in English? As discussed in Section 6, this paper uses grammar induction on
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-87b3aad216bdcc1c891fa7ec37a6e1dd89d027f5f823202a2235fcc4e313e107

Passage ID: `qasper-passage-v1-87b3aad216bdcc1c891fa7ec37a6e1dd89d027f5f823202a2235fcc4e313e107`; retrieval score: 4.113050034647275.

Word count: 250.

```text
is based on location-specific content (e.g., “Chicago" vs. “Singapore") rather than on purely linguistic lexical variation (e.g., “jeans" vs. “denim"). How do we differentiate between predictions based on place-names, those based on place-specific content, and those based on dialectal variation? That is a question for future work. For example, is it possible to identify and remove location-specific content terms? Here we focus instead on using syntactic representations that are not subject to such interference.

Within syntactic features, function words perform the worst on both datasets with F1s of 0.65 and 0.55. This is not surprising because function words in English do not represent syntactic structures directly; they are instead markers of the types of structures being used. CxG-1 comes next with F1s of 0.80 and 0.76, a significant improvement over the function-word baseline but not approaching unigrams. Note that the experiments using this same grammar in previous work (Dunn, 2018c) were applied to samples of 2k words each. Finally, CxG-2 performs the best, with F1s of 0.96 and 0.92, falling behind unigrams but rivaling bigrams and surpassing trigrams. Because of this, the more detailed experiments below focus only on the CxG-2 grammar.

A closer look at both datasets by region for CxG-2 is given in Table 6. The two datasets (web-crawled and social media) present some interesting divergences. For example, Australian English is among the better performing varieties on the CC dataset (F1 = 0.97) but among the worst performing varieties on Twitter (F1 = 0.83). This is the case
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-f8b21e37d1a22e36686f888e670c1cbd6d5904bc51fa33a10e9dbda804c82e4c

Passage ID: `qasper-passage-v1-f8b21e37d1a22e36686f888e670c1cbd6d5904bc51fa33a10e9dbda804c82e4c`; retrieval score: 4.080604091084091.

Word count: 250.

```text
The main set of experiments uses a Linear Support Vector Machine (Joachims, 1998) to classify dialects using CxG features. Parameters are tuned using the development data. Given the general robust performance of SVMs in the literature relative to other similar classifiers on variation tasks (c.f., Dunn, et al., 2016), we forego a systematic evaluation of classifiers.

We start, in Table 5, with an evaluation of baselines by feature type and dataset. We have two general types of features: purely syntactic representations (CxG-1, CxG-2, Function words) and potentially topic-based features (unigrams, bigrams, trigrams). The highest performing feature on both datasets is simple lexical unigrams, at 30k dimensions. We use a hashing vectorizer to avoid a region-specific bias: the vectorizer does not need to be trained or initialized against a specific dataset so there is no chance that one of the varieties will be over-represented in determining which n-grams are included. But this has the side-effect of preventing the inspection of individual features. Vectors for all experiments are available, along with the trained models that depend on these vectors.

As n increases, n-grams tend to represent structural rather than topical information. In this case, performance decreases as n increases. We suggest that this decrease provides an indication that the performance of unigrams is based on location-specific content (e.g., “Chicago" vs. “Singapore") rather than on purely linguistic lexical variation (e.g., “jeans" vs. “denim"). How do we differentiate between predictions based on place-names, those based on place-specific content, and those based on dialectal variation?
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.05527:6:0` | full | 0:369 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1217.

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

#### Rank 1: qasper-passage-v1-96b3c7744e3f4c74dc029660516cefcfcf3021af1851ede82b1e50821562a11a

Passage ID: `qasper-passage-v1-96b3c7744e3f4c74dc029660516cefcfcf3021af1851ede82b1e50821562a11a`; retrieval score: 7.770032073403617.

Word count: 250.

```text
Many machine reading comprehension (MRC) datasets have been released in recent years BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4 to benchmark a system's ability to understand and reason over natural language. Typically, these datasets require an MRC model to read through a document to answer a question about information contained therein.

The supporting document is, more often than not, static and fully observable. This raises concerns, since models may find answers simply through shallow pattern matching; e.g., syntactic similarity between the words in questions and documents. As pointed out by BIBREF5, for questions starting with when, models tend to predict the only date/time answer in the supporting document. Such behavior limits the generality and usefulness of MRC models, and suggests that they do not learn a proper `understanding' of the intended task. In this paper, to address this problem, we shift the focus of MRC data away from `spoon-feeding' models with sufficient information in fully observable, static documents. Instead, we propose interactive versions of existing MRC tasks, whereby the information needed to answer a question must be gathered sequentially.

The key idea behind our proposed interactive MRC (iMRC) is to restrict the document context that a model observes at one time. Concretely, we split a supporting document into its component sentences and withhold these sentences from the model. Given a question, the model must issue commands to observe sentences in the withheld set; we equip models with actions such as Ctrl+F (search for token) and stop for searching through partially observed documents.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.10449:0:2` | partial | 0:457 |

#### Rank 2: qasper-passage-v1-f8ec3d6d72dd1df203822d3b59fb01c3fab2de22d78cde18cd3355efa0fedbc4

Passage ID: `qasper-passage-v1-f8ec3d6d72dd1df203822d3b59fb01c3fab2de22d78cde18cd3355efa0fedbc4`; retrieval score: 5.664995355688099.

Word count: 250.

```text
In this work, we propose and explore the direction of converting MRC datasets into interactive environments. We believe interactive, information-seeking behavior is desirable for neural MRC systems when knowledge sources are partially observable and/or too large to encode in their entirety — for instance, when searching for information on the internet, where knowledge is by design easily accessible to humans through interaction.

Despite being restricted, our proposed task presents major challenges to existing techniques. iMRC lies at the intersection of NLP and RL, which is arguably less studied in existing literature. We hope to encourage researchers from both NLP and RL communities to work toward solving this task.

For our baseline, we adopted an off-the-shelf, top-performing MRC model and RL method. Either component can be replaced straightforwardly with other methods (e.g., to utilize a large-scale pretrained language model).

Our proposed setup and baseline agent presently use only a single word with the query command. However, a host of other options should be considered in future work. For example, multi-word queries with fuzzy matching are more realistic. It would also be interesting for an agent to generate a vector representation of the query in some latent space. This vector could then be compared with precomputed document representations (e.g., in an open domain QA dataset) to determine what text to observe next, with such behavior tantamount to learning to do IR.

As mentioned, our idea for reformulating existing MRC datasets as partially observable and interactive environments is straightforward and general. Almost all
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-44f687ebd47e39a6915d0ba26f9331af14df4686f1e5523ddacd51e1ac6ab5da

Passage ID: `qasper-passage-v1-44f687ebd47e39a6915d0ba26f9331af14df4686f1e5523ddacd51e1ac6ab5da`; retrieval score: 5.330055920222712.

Word count: 250.

```text
Skip-reading BIBREF6, BIBREF7, BIBREF8 is an existing setting in which MRC models read partial documents. Concretely, these methods assume that not all tokens in the input sequence are useful, and therefore learn to skip irrelevant tokens based on the current input and their internal memory. Since skipping decisions are discrete, the models are often optimized by the REINFORCE algorithm BIBREF9. For example, the structural-jump-LSTM proposed in BIBREF10 learns to skip and jump over chunks of text. In a similar vein, BIBREF11 designed a QA task where the model reads streaming data unidirectionally, without knowing when the question will be provided. Skip-reading approaches are limited in that they only consider jumping over a few consecutive tokens and the skipping operations are usually unidirectional. Based on the assumption that a single pass of reading may not provide sufficient information, multi-pass reading methods have also been studied BIBREF12, BIBREF13.

Compared to skip-reading and multi-turn reading, our work enables an agent to jump through a document in a more dynamic manner, in some sense combining aspects of skip-reading and re-reading. For example, it can jump forward, backward, or to an arbitrary position, depending on the query. This also distinguishes the model we develop in this work from ReasoNet BIBREF13, where an agent decides when to stop unidirectional reading.

Recently, BIBREF14 propose DocQN, which is a DQN-based agent that leverages the (tree) structure of documents and navigates across sentences and paragraphs. The proposed method has been shown to outperform vanilla DQN and IR baselines on
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-b08de4297d641dc640126469fac0102e0c6d8db8d1ca5ad3f4bacf9146c032a5

Passage ID: `qasper-passage-v1-b08de4297d641dc640126469fac0102e0c6d8db8d1ca5ad3f4bacf9146c032a5`; retrieval score: 4.761775490551747.

Word count: 121.

```text
iMRC games are interactive environments. We use an RL training algorithm to train the interactive information-gathering behavior of QA-DQN. We adopt the Rainbow algorithm proposed by BIBREF23, which integrates several extensions to the original Deep Q-Learning algorithm BIBREF24. Rainbox exhibits state-of-the-art performance on several RL benchmark tasks (e.g., Atari games).

During game playing, we use a mini-batch of size 10 and push all transitions (observation string, question string, generated command, reward) into a replay buffer of size 500,000. We do not compute losses directly using these transitions. After every 5 game steps, we randomly sample a mini-batch of 64 transitions from the replay buffer, compute loss, and update the network.

Detailed hyper-parameter settings for action generation are shown in Table TABREF38.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-681a20351fa901f5028a4f8ce389ad1b6a8f060d4b5500fdc9b04f5520d67576

Passage ID: `qasper-passage-v1-681a20351fa901f5028a4f8ce389ad1b6a8f060d4b5500fdc9b04f5520d67576`; retrieval score: 4.655060861219983.

Word count: 122.

```text
Similarly, we use another replay buffer to store question answering transitions (observation string when interaction stops, question string, ground-truth answer).

Because both iSQuAD and iNewsQA are converted from datasets that provide ground-truth answer positions, we can leverage this information and train the question answerer with supervised learning. Specifically, we only push question answering transitions when the ground-truth answer is in the observation string. For each transition, we convert the ground-truth answer head- and tail-positions from the SQuAD and NewsQA datasets to positions in the current observation string. After every 5 game steps, we randomly sample a mini-batch of 64 transitions from the replay buffer and train the question answerer using the Negative Log-Likelihood (NLL) loss. We use a dropout rate of 0.1.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 993.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "33b2d26d064251c196238b0c3c455b208680f5fc": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1908.10449:0:2": [
        [
          457,
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

#### Rank 1: qasper-passage-v1-329098f70f83ee7523d777d3f69aab1aec568a334bf9b69772efb779fd32363f

Passage ID: `qasper-passage-v1-329098f70f83ee7523d777d3f69aab1aec568a334bf9b69772efb779fd32363f`; retrieval score: 4.65262967282035.

Word count: 250.

```text
the campaign contain the same amount of Tiers, with the same names. It can also enforce, for certain chosen tiers, a set of valid annotations.

Users with the rights to create Annotation Campaigns and Annotators user accounts, and assign Annotation Tasks to Annotators.

Users who are assigned a set of Annotation Tasks. Their job is to complete the annotation of the audio files with the Praat software.

If the TextGrid file they submit does not comply with their Annotation Task's TextGrid Checking Scheme, Seshat pinpoint their annotation errors with detailed messages. The annotator can re-submit the concerned file to the platform based on these different feedbacks.

Once they they connected to their instance of Seshat, campaign managers can access ongoing annotation campaigns or create new ones. Campaign managers are able to add annotators, assign annotation tasks and track progress. Annotator see a list of assigned tasks. The first step for them is to download the sound file with its corresponding auto-generated template TextGrid. In the current implementation, the annotation work has to be done locally with Praat. An upcoming version will use of web tools like Praat on the web BIBREF10. Once the task is completed, the TextGrid file is to be uploaded to Seshat via the web interface. We used the TextGrid format because of the wide acceptance of the Praat software in the speech science community (e.g., language acquisition research, clinical linguistics, phonetics and phonology).

The Textgrid Checking Scheme that encompasses rules on the tier's naming, file structure,
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-f7ff7d31a5998ebd8061ce75ed163f95e67b5ff6bd6a77ec528334a5c4b5685b

Passage ID: `qasper-passage-v1-f7ff7d31a5998ebd8061ce75ed163f95e67b5ff6bd6a77ec528334a5c4b5685b`; retrieval score: 4.566574861434601.

Word count: 250.

```text
Seshat was intially developped to study the impact of Huntington's Disease BIBREF17 on speech and language production. One hundred and fifty two interviews between a neuropsychologist and a patient with the Huntington's Disease (HD) were recorded between June 2018 and November 2019. The campaign manager created a campaign with multiple tiers to annotate the turn takings and the speech/non speech boundaries of the utterances of the patient. For both tasks, the annotations did not need to cover completely the audio (sparsity property mentioned above). For the Turn-taking annotations, there are 3 pre-defined tiers, each one with a single class ('Patient', 'Non-Patient', and 'Noise'), which results in possible overlap between these classes. For the Utterance annotations, there is only one pre-defined class ('Utterance').

To this date, a total of 67 files have been fully annotated with the help of Seshat by a cohort of 18 speech pathologist students (see Figure FIGREF33). Among these, 16 have been done by 2 different annotators independently with the Double-annotator task. The results are summarised in Table TABREF34.

Even though there are more categories for Turn-Takings than Utterance (gut2004measuring reported that the more categories the more the task is difficult in speech annotations), the mean $\gamma $ for the Turn-Takings $\gamma = 0.64$ is slightly higher than the one for Utterance $\gamma = 0.61$. And the range of values for the Turn-Takings is smaller than the Utterance. Indeed, the speech pathologists reported the difficulty to annotate the boundary of utterances in spontaneous speech, with several ambiguous
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-5e7f082cb2205d42fe85b997a27868c66193d6ab3e93c8b15ee18893c32ea56a

Passage ID: `qasper-passage-v1-5e7f082cb2205d42fe85b997a27868c66193d6ab3e93c8b15ee18893c32ea56a`; retrieval score: 4.468090661656275.

Word count: 153.

```text
integrate annotation checking.

On the other side of the spectrum, there are more sophisticated systems with various capabilities. Camomille BIBREF11 and the EMU-SDMS system (that can also be used offline) BIBREF12 allow to work with speech data and to distribute the tasks to several annotators. But these systems require expertise in web hosting and technologies to deploy and modify them.

Finally, WebAnno BIBREF13 and GATE Teamware BIBREF14 are the tools that most closely match our main contributions regarding quality control (conformity and consistency checking), annotators' management and flexibility. WebAnno includes consistency checking with the integration of different metrics BIBREF15. However, these tools have only been built for text data. The format and all the custom layers have been designed for Natural Language Processing tasks. Porting WebAnno to support speech data seemed a major engineering challenge. That is why it appeared necessary to develop a new and user-friendly tool addressed to the speech community.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-ba7c9ac561b3eaf35ec7b1c60c6adfad7f3360c63749a547ce67b1c125c0e1eb

Passage ID: `qasper-passage-v1-ba7c9ac561b3eaf35ec7b1c60c6adfad7f3360c63749a547ce67b1c125c0e1eb`; retrieval score: 4.450593883888409.

Word count: 160.

```text
The Campaign manager can easily define and monitor annotation campaign. As shown in Figure FIGREF33, the online form enable to choose corpora, pre-define and pre-configure the annotations scheme (tiers and parsers). There are 2 types of tiers already implemented by default: one with no check at all, and one with pre-defined categories. For the latter, these categories are pre-defined when the campaign is created.

Only Campaign managers can access and build new campaigns. If Campaign manager have several campaigns they can easily switch between them via the menu bar or get a full overview with the dashboard (See Figure FIGREF26). The campaign managers can visualise the progress of the assigned tasks at the campaign level or more precisely at the task level. They can retrieve all the intermediate files that have been created for each task. For instance, the campaign manager can examine qualitatively and quantitatively what are the annotation differences before the merge phases of the double annotator task.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-70015e9ba309ab5d2ee18f0f9ce5fd6087b1c6bb43ac002e39455ceca074ba97

Passage ID: `qasper-passage-v1-70015e9ba309ab5d2ee18f0f9ce5fd6087b1c6bb43ac002e39455ceca074ba97`; retrieval score: 4.095470969153171.

Word count: 250.

```text
Self-hosted annotation systems. There are many standalone solutions for the transcription of speech data that are already used by researchers: Transcriber BIBREF3, Wavesurfer BIBREF4, Praat BIBREF5, ELAN BIBREF6, XTrans BIBREF7. These systems allow the playback of sound data and the construction of different layers of annotations with various specifications, with some advanced capabilities (such as annotations with hierarchical or no relationship between layers, number of audio channels, video support). Yet, these solutions lack a management system: each researcher must track the files assigned to annotators and build a pipeline to parse (and eventually check) the output annotation files. Moreover, checking can only be done once the annotations have been submitted to the researchers. This task becomes quickly untraceable as the number of files and annotators grow. In addition, most of these transcription systems do not provide a way to evaluate consistency (intra- and inter-annotator agreement) that would be appropriate for speech data BIBREF8.

Web-based annotations systems. There are several web-based annotation systems for the annotation of audio data. Among them we find light-weight systems, like the VIA software BIBREF9 or Praat on the web BIBREF10 that allow to build simple layers of annotations. However, they do not provide a proper management system for a pool of annotators nor do they integrate annotation checking.

On the other side of the spectrum, there are more sophisticated systems with various capabilities. Camomille BIBREF11 and the EMU-SDMS system (that can also be used offline) BIBREF12 allow to work with speech data and to distribute
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1063.

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

#### Rank 1: qasper-passage-v1-b00eaf120903c407420244d999188991d03c9c56bc9d24fde71506978dcc05c8

Passage ID: `qasper-passage-v1-b00eaf120903c407420244d999188991d03c9c56bc9d24fde71506978dcc05c8`; retrieval score: 7.98596728830965.

Word count: 200.

```text
As a comparison to the state of the art methods, Table 1 presents accuracy results of the best Collective Matrix Factorization model, with a latent space dimension of 350, which has been determined by cross-validation on a development set, where the value of each slot is instantiated as the most probable w.r.t the inference procedure presented in Section "Spectral decomposition model for state tracking in slot-filling dialogs" . In our experiments, the variance is estimated using standard dataset reshuffling. The same results are obtained for several state of the art methods of generative and discriminative state tracking on this dataset using the publicly available results as reported in BIBREF22 . More precisely, as provided by the state-of-the-art approaches, the accuracy scores computes $p(s^*_{t+1}|s_t,z_t)$ commonly name the joint goal. Our proposition is compared to the 4 baseline trackers provided by the DSTC organisers. They are the baseline tracker (Baseline), the focus tracker (Focus), the HWU tracker (HWU) and the HWU tracker with “original” flag set to (HWU+) respectively. Then a comparison to a maximum entropy (MaxEnt) proposed in BIBREF23 type of discriminative model and finally a deep neural network (DNN) architecture proposed in BIBREF24 as reported also in BIBREF22 is presented.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1606.05286:9:0` | full | 0:1317 |

#### Rank 2: qasper-passage-v1-3eeb2ad53c3999a212685f8f2725dacfa81be6f4676e8449e83b3a2f03dfbe8d

Passage ID: `qasper-passage-v1-3eeb2ad53c3999a212685f8f2725dacfa81be6f4676e8449e83b3a2f03dfbe8d`; retrieval score: 7.015140352485469.

Word count: 79.

```text
test time because, as detailed in Section "Spectral decomposition model for state tracking in slot-filling dialogs" , the tracking algorithm hold a linear complexity w.r.t the sum of realization of each considered variables defining the state to track which is what we believe is one of the main advantage of this method. Secondly collective matrix factorization paradigm also for data fusion and bias by data type of modeling as successfully performed in matrix factorization based recommender systems BIBREF30 .
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-45f33a8e9fc983ba4d6d51fb326e852d1929b8771f1ddb4acf546b2405775167

Passage ID: `qasper-passage-v1-45f33a8e9fc983ba4d6d51fb326e852d1929b8771f1ddb4acf546b2405775167`; retrieval score: 5.929063295570586.

Word count: 146.

```text
state space. For example, BIBREF13 proposes to restrict the set of possible state variables to those that appeared in NLU results. More recently, BIBREF14 assumes conditional independence between dialog state variables to address scalability issues and uses a conditional random field to track each variable separately. Finally, deep neural models, performing on a sliding window of features extracted from previous user turns, have also been proposed in BIBREF15 . Of the current literature, this family of approaches have proven to be the most efficient for publicly available state tracking datasets. In the next section, we present a decompositional approach of dialog state tracking that aims at reconciling the two main approaches of the state of the art while leveraging on the current advances of low-rank bilinear decomposition models, as recalled in BIBREF16 , that seems particularly adapted to the sparse nature of dialog state tracking tasks.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-d5fbab3f1821e920bd478c861be8e982f673eb389bb4862f1428e886c8458fc6

Passage ID: `qasper-passage-v1-d5fbab3f1821e920bd478c861be8e982f673eb389bb4862f1428e886c8458fc6`; retrieval score: 5.898649691482162.

Word count: 180.

```text
hypotheses of the true dialog state, are able to behave robustly even in the face of noisy conditions and ambiguity. In this paper, a statistical type of approach of state tracking is proposed by leveraging the recent progress of spectral decomposition methods formalized as bilinear algebraic decomposition and associated inference procedures. The proposed model estimates each state transition with respect to a set of observations and is able to compute the state transition through an inference procedure with a linear complexity with respect to the number of variables and observations.

Roadmap: This paper is structured as follows, Section "Generative Dialog State Tracking" formally defines transactional dialogs and describes the associated problem of statistical dialog state tracking with both the generative and discriminative approaches. Section "Spectral decomposition model for state tracking in slot-filling dialogs" depicts the proposed decompositional model for coupled and temporal hidden variable models and the associated inference procedure based on Collective Matrix Factorization (CMF). Finally, Section "Experimental settings and Evaluation" illustrates the approach with experimental results obtained using a state of the art benchmark for dialog state tracking.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-be8968fa5a5a8085df5cfe3c7ae846ac314fe9b61a86a6c101cce092f3b093b7

Passage ID: `qasper-passage-v1-be8968fa5a5a8085df5cfe3c7ae846ac314fe9b61a86a6c101cce092f3b093b7`; retrieval score: 5.819277891229447.

Word count: 250.

```text
natural conversational interaction one might hope to achieve as recalled in BIBREF2 . More recent methods employ statistical approaches to estimate the posterior distribution over the dialog states allowing them to represent the uncertainty of the results of the NLU module. Statistical dialog state trackers are commonly categorized into one of two approaches according to how the posterior probability distribution over the state calculation is defined. In the first type, the generative approach uses a generative model of the dialog dynamic that describes how the sequence of utterances are generated by using the hidden dialog state and using Bayes' rule to calculate the posterior distribution of the state. It has been a popular approach for statistical dialog state tracking, since it naturally fits into the Partially Observable Markov Decision Process (POMDP) models as described in BIBREF3 , which is an integrated model for dialog state tracking and dialog strategy optimization. Using this generic formalism of sequential decision processes, the task of dialog state tracking is to calculate the posterior distribution over an hidden state given an history of observations. In the second type, the discriminative approach models the posterior distribution directly through a closed algebraic formulation as a loss minimization problem. Statistical dialog systems, in maintaining a distribution over multiple hypotheses of the true dialog state, are able to behave robustly even in the face of noisy conditions and ambiguity. In this paper, a statistical type of approach of state tracking is proposed by leveraging the recent progress of spectral
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 855.

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

#### Rank 1: qasper-passage-v1-8ebf298ccb06865b696110b9f16801672289142dffd5e0afc0f9f2bbcf0cfeaa

Passage ID: `qasper-passage-v1-8ebf298ccb06865b696110b9f16801672289142dffd5e0afc0f9f2bbcf0cfeaa`; retrieval score: 11.581299694198602.

Word count: 238.

```text
The explosion of available scientific articles in the Biomedical domain has led to the rise of Biomedical Information Extraction (BioIE). BioIE systems aim to extract information from a wide spectrum of articles including medical literature, biological literature, electronic health records, etc. that can be used by clinicians and researchers in the field. Often the outputs of BioIE systems are used to assist in the creation of databases, or to suggest new paths for research. For example, a ranked list of interacting proteins that are extracted from biomedical literature, but are not present in existing databases, can allow researchers to make informed decisions about which protein/gene to study further. Interactions between drugs are necessary for clinicians who simultaneously administer multiple drugs to their patients. A database of diseases, treatments and tests is beneficial for doctors consulting in complicated medical cases.

The main problems in BioIE are similar to those in Information Extraction:

This paper discusses, in each section, various methods that have been adopted to solve the listed problems. Each section also highlights the difficulty of Information Extraction tasks in the biomedical domain.

This paper is intended as a primer to Biomedical Information Extraction for current NLP researchers. It aims to highlight the diversity of the various techniques from Information Extraction that have been applied in the Biomedical domain. The state of biomedical text mining is reviewed regularly. For more extensive surveys, consult BIBREF0 , BIBREF1 , BIBREF2 .
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-2a24bd2a43357273b329c3ef36088e9bbc99a1cd282d145068ff0bc3df3aefc3

Passage ID: `qasper-passage-v1-2a24bd2a43357273b329c3ef36088e9bbc99a1cd282d145068ff0bc3df3aefc3`; retrieval score: 4.890548513353164.

Word count: 250.

```text
Named Entity Recognition (NER) in the Biomedical domain usually includes recognition of entities such as proteins, genes, diseases, treatments, drugs, etc. Fact extraction involves extraction of Named Entities from a corpus, usually given a certain ontology. When compared to NER in the domain of general text, the biomedical domain has some characteristic challenges:

Some of the earliest systems were heavily dependent on hand-crafted features. The method proposed in BIBREF4 for recognition of protein names in text does not require any prepared dictionary. The work gives examples of diversity in protein names and lists multiple rules depending on simple word features as well as POS tags.

BIBREF5 adopt a machine learning approach for NER. Their NER system extracts medical problems, tests and treatments from discharge summaries and progress notes. They use a semi-Conditional Random Field (semi-CRF) BIBREF6 to output labels over all tokens in the sentence. They use a variety of token, context and sentence level features. They also use some concept mapping features using existing annotation tools, as well as Brown clustering to form 128 clusters over the unlabelled data. The dataset used is the i2b2 2010 challenge dataset. Their system achieves an F-Score of 0.85. BIBREF7 is an incremental paper on NER taggers. It uses 3 types of word-representation techniques (Brown clustering, distributional clustering, word vectors) to improve performance of the NER Conditional Random Field tagger, and achieves marginal F-Score improvements.

BIBREF8 propose a boostrapping mechanism to bootstrap biomedical ontologies using NELL BIBREF9 , which uses a coupled semi-supervised
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1705.05437:1:2` | full | 1:853 |

#### Rank 3: qasper-passage-v1-d4179669a9557b4b5d9c180744e2709997d18e9f1237994ca414b431856889ed

Passage ID: `qasper-passage-v1-d4179669a9557b4b5d9c180744e2709997d18e9f1237994ca414b431856889ed`; retrieval score: 3.6015586151371206.

Word count: 250.

```text
to a hand-crafted list of trigger words to define their features. An SVM classifier is then trained on the feature vectors, with a positive label if the drug pair interacts, and negative otherwise. Their method beats other systems on the DDI-2013 dataset. Some other feature-based approaches are described in BIBREF21 , BIBREF22 .

Distant supervision methods have also been applied to relation extraction over biomedical corpora. In BIBREF23 , 10,000 neuroscience articles are distantly supervised using information from UMLS Semantic Network to classify brain-gene relations into geneExpression and otherRelation. They use lexical (bag of words, contextual) features as well as syntactic (dependency parse features). They make the “at-least one” assumption, i.e. at least one of the sentences extracted for a given entity-pair contains the relation in database. They model it as a multi-instance learning problem and adopt a graphical model similar to BIBREF24 . They test using manually annotated examples. They note that the F-score achieved are much lesser than that achieved in the general domain in BIBREF24 , and attribute to generally poorer performance of NER tools in the biomedical domain, as well as less training examples. BIBREF25 explore distant supervision methods for protein-protein interaction extraction.

More recently, deep learning methods have been applied to relation extraction in the biomedical domain. One of the main advantages of such methods over traditional feature or kernel based learning methods is that they require minimal feature engineering. In BIBREF26 , skip-gram vectors BIBREF27 are trained over 5.6Gb of unlabelled text. They use
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-a72df547ecc5f844e917fc89e2c11048367a0c4f9eb935a3160f409d5e327f5a

Passage ID: `qasper-passage-v1-a72df547ecc5f844e917fc89e2c11048367a0c4f9eb935a3160f409d5e327f5a`; retrieval score: 3.232511757995221.

Word count: 96.

```text
the knowledge base. Since evaluation is not possible using Mechanical Turk or a small number of experts (due to the complexity of the task), they use Freebase BIBREF10 , a knowledge base that has some biomedical concepts as well. The lexicon learned using BioNELL is used to train an NER system. The system shows a very high precision, thereby showing that BioNELL learns very few ambiguous terms.

More recently, deep learning techniques have been developed to further enhance the performance of NER systems. BIBREF11 explore recurrent neural networks for the problem of NER in biomedical text.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-1847c919953c3ac365a3e0deb2859aa6652581ba5410ac73b3074ee2e49f4e99

Passage ID: `qasper-passage-v1-1847c919953c3ac365a3e0deb2859aa6652581ba5410ac73b3074ee2e49f4e99`; retrieval score: 2.7280977449915267.

Word count: 250.

```text
trigger expression and arguments need to be extracted. Since the events can be arguments to other events, the final output in general is a graph representation with events and named entities as nodes, and edges that correspond to event arguments. BIBREF33 present a pipeline based method that is heavily dependent on dependency parsing. Their pipeline approach consists of three steps: trigger detection, argument detection and semantic post-processing. While the first two components are learning based systems, the last component is a rule based system. For the BioNLP'09 corpus, only 5% of the events span multiple sentences. Hence the approach does not get affected severely by considering only single sentences. It is important to note that trigger words cannot simply be reduced to a dictionary lookup. This is because a specific word may belong to multiple classes, or may not always be a trigger word for an event. For example, “activate” is found to not be a trigger word in over 70% of the cases. A multi-class SVM is trained for trigger detection on each token, using a large feature set consisting of semantic and syntactic features. It is interesting to note that the hyperparameters of this classifier are optimised based on the performance of the entire end-to-end system.

For the second component to detect arguments, labels for edges between entities must be predicted. For the BioNLP'09 Shared Task, each directed edge from one event node to another event node, or from an event node to a named entity node are
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1084.

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

#### Rank 1: qasper-passage-v1-0f40cd613fb439f9899e45ae54b5b379f4148342d82b25e1b5803f63a23716a2

Passage ID: `qasper-passage-v1-0f40cd613fb439f9899e45ae54b5b379f4148342d82b25e1b5803f63a23716a2`; retrieval score: 5.2878115243140265.

Word count: 250.

```text
language text.

Question answering for reading comprehension in general has seen a great deal of recent work BIBREF15 , BIBREF16 , and there have been many recent attempts to construct QA datasets that require advanced reasoning abilities BIBREF5 , BIBREF17 , BIBREF18 , BIBREF19 , BIBREF20 . However, these attempts typically involve engineering data to be more difficult by, for example, explicitly prompting users to write multi-step questions BIBREF5 , BIBREF18 , or filtering out easy questions BIBREF19 . This risks resulting in models that do not have obvious end-use applications since they are optimized to perform in an artificial setting. In this paper, we show that yes/no questions have the benefit of being very challenging even when they are gathered from natural sources.

Natural language inference is also a well studied area of research, particularly on the MultiNLI BIBREF21 and SNLI BIBREF22 datasets. Other sources of entailment data include the PASCAL RTE challenges BIBREF23 , BIBREF24 or SciTail BIBREF25 . We note that, although SciTail, RTE-6 and RTE-7 did not use crowd workers to generate candidate statements, they still use sources (multiple choices questions or document summaries) that were written by humans with knowledge of the premise text. Using naturally occurring yes/no questions ensures even greater independence between the questions and premise text, and ties our dataset to a clear end-task. BoolQ also requires detecting entailment in paragraphs instead of sentence pairs.

Transfer learning for entailment has been studied in GLUE BIBREF7 and SentEval BIBREF26 . Unsupervised pre-training in
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-6022642bed0237060067d59030daf08232669e04c8d23a83e5eccbeb3c0b28d5

Passage ID: `qasper-passage-v1-6022642bed0237060067d59030daf08232669e04c8d23a83e5eccbeb3c0b28d5`; retrieval score: 4.396388389956526.

Word count: 250.

```text
Understanding what facts can be inferred to be true or false from text is an essential part of natural language understanding. In many cases, these inferences can go well beyond what is immediately stated in the text. For example, a simple sentence like “Hanna Huyskova won the gold medal for Belarus in freestyle skiing." implies that (1) Belarus is a country, (2) Hanna Huyskova is an athlete, (3) Belarus won at least one Olympic event, (4) the USA did not win the freestyle skiing event, and so on. Work completed while interning at Google. Also affiliated with Columbia University, work done at Google.

To test a model's ability to make these kinds of inferences, previous work in natural language inference (NLI) proposed the task of labeling candidate statements as being entailed or contradicted by a given passage. However, in practice, generating candidate statements that test for complex inferential abilities is challenging. For instance, evidence suggests BIBREF0 , BIBREF1 , BIBREF2 that simply asking human annotators to write candidate statements will result in examples that typically only require surface-level reasoning.

In this paper we propose an alternative: we test models on their ability to answer naturally occurring yes/no questions. That is, questions that were authored by people who were not prompted to write particular kinds of questions, including even being required to write yes/no questions, and who did not know the answer to the question they were asking. Figure contains some examples from our dataset. We find such questions often query
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-7c8e5c33b09323c986ef4a775b163f830679f56483fea7457608e6d6fece49b6

Passage ID: `qasper-passage-v1-7c8e5c33b09323c986ef4a775b163f830679f56483fea7457608e6d6fece49b6`; retrieval score: 4.274010854135292.

Word count: 250.

```text
that contain more inference and have higher quality labels.

A surprising result from our work is that the datasets that more closely resemble the format of BoolQ, meaning they contain questions and multi-sentence passages, such as SQuAD 2.0, RACE, or Y/N MS Marco, were not very useful for transfer. The entailment datasets were stronger despite consisting of sentence pairs. This suggests that adapting from sentence-pair input to question/passage input was not a large obstacle to achieving transfer. Preliminary work found attempting to convert the yes/no questions in BoolQ into declarative statements did not improve transfer from MultiNLI, which supports this hypothesis.

The success of MultiNLI might also be surprising given recent concerns about the generalization abilities of models trained on it BIBREF37 , particularly related to “annotation artifacts" caused by using crowd workers to write the hypothesis statements BIBREF0 . We have shown that, despite these weaknesses, it can still be an important starting point for models being used on natural data.

We hypothesize that a key advantage of MultiNLI is that it contains examples of contradictions. The other sources of transfer we consider, including the next-sentence-selection objective in BERT, are closer to providing examples of entailed text vs. neutral/unrelated text. Indeed, we found that our two step transfer procedure only reaches 78.43% dev set accuracy if we remove the contradiction class from MultiNLI, regressing its performance close to the level of BERTL when just using unsupervised pre-training.

Note that it is possible to pre-train a model on several of
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-4d014e592a03588fe55bcc93136405bb997b61e7082b6435b0ce1c6db5c0ab6a

Passage ID: `qasper-passage-v1-4d014e592a03588fe55bcc93136405bb997b61e7082b6435b0ce1c6db5c0ab6a`; retrieval score: 3.967073228526385.

Word count: 190.

```text
contains additional randomly selected examples.

Following recent work BIBREF7 , we focus on using transfer learning to establish baselines for our dataset. Yes/No QA is closely related to many other NLP tasks, including other forms of question answering, entailment, and paraphrasing. Therefore, it is not clear what the best data sources to transfer from are, or if it will be sufficient to just transfer from powerful pre-trained language models such as BERT BIBREF8 or ELMo BIBREF9 . We experiment with state-of-the-art unsupervised approaches, using existing entailment datasets, three methods of leveraging extractive QA data, and using a few other supervised datasets.

We found that transferring from MultiNLI, and the unsupervised pre-training in BERT, gave us the best results. Notably, we found these approaches are surprisingly complementary and can be combined to achieve a large gain in performance. Overall, our best model reaches 80.43% accuracy, compared to 62.31% for the majority baseline and 90% human accuracy. In light of the fact BERT on its own has achieved human-like performance on several NLP tasks, this demonstrates the high degree of difficulty of our dataset. We present our data and code at https://goo.gl/boolq.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-6b5db14a255300def9529b7ac9c3545210297ac2ea1889fa0f09420f41c61298

Passage ID: `qasper-passage-v1-6b5db14a255300def9529b7ac9c3545210297ac2ea1889fa0f09420f41c61298`; retrieval score: 3.4379218184911533.

Word count: 83.

```text
or “no", and then pair the corresponding questions with snippets marked as being related to the question. We call this task Y/N MS Marco; in total we gather 38k examples, 80% of which are “yes” answers.

Unsupervised: It is well known that unsupervised pre-training using language-modeling objectives BIBREF9 , BIBREF8 , BIBREF27 , can improve performance on many tasks. We experiment with these methods by using the pre-trained models from ELMo, BERT, and OpenAI's Generative Pre-trained Transformer (OpenAI GPT) (see Section SECREF11 ).
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1023.

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

#### Rank 1: qasper-passage-v1-42d419d31863b47fbece2b5e32de79583543c3b6eba51447ee16257c26cf03bb

Passage ID: `qasper-passage-v1-42d419d31863b47fbece2b5e32de79583543c3b6eba51447ee16257c26cf03bb`; retrieval score: 2.5530159981041347.

Word count: 250.

```text
Work on representation learning is concerned with finding an appropriate representation of data in order to perform a machine learning task BIBREF33. In particular, deep learning exploits this concept by its very nature BIBREF2. Work on representation learning include Predictive State Representations (PSR) BIBREF34, BIBREF35, which capture the state as a vector of predictions of future outcomes, and a Heuristic Embedding of Markov Processes (HEMP) BIBREF36, which learns to embed transition probabilities using an energy-based optimization problem.

There has been extensive work attempting to use natural language in RL. Efforts that integrate language in RL develop tools, approaches, and insights that are valuable for improving the generalization and sample efficiency of learning agents. Previous work on language-conditioned RL has considered the use of natural language in the observation and action space. Environments such as Zork and TextWorld BIBREF37 have been the standard benchmarks for testing text-based games. Nevertheless, these environments do not search for semantic state representations, in which an RL algorithm can be better evaluated and controlled.

BIBREF38 use high-level semantic abstractions of documents in a representation to facilitate relational learning using Inductive Logic Programming and a generative language model. BIBREF39 use high-level guidance expressed in text to enrich a stochastic agent, playing against the built-in AI of Civilization II. They train an agent with the Monte-Carlo search framework in order to jointly learn to identify text that is relevant to a given game state as well as game strategies based only on environment feedback. BIBREF40 utilize natural language
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-1dd1bc853a38ecc71cf19ba3a5007a064947fb3a997d96683cf9566322f8ac11

Passage ID: `qasper-passage-v1-1dd1bc853a38ecc71cf19ba3a5007a064947fb3a997d96683cf9566322f8ac11`; retrieval score: 2.151483603207673.

Word count: 232.

```text
to changes in the environment as well as task-nuisances in the state. As depicted in fig: nuisance scenarios, inflating the state space with task-nuisances impairs the performance of all representations. There, a large amount of unnecessary objects were spawned in the level, increasing the state's description length to over 250 words, whilst retaining the same amount of useful information. Nevertheless, the NLP representation outperformed the vision and feature based representations, with high robustness to the applied noise.

In order to verify the performance of the natural language representation was not due to extensive discretization of patches, we've conducted experiments increasing the number of horizontal patches - ranging from 3 to 31 patches in the extreme case. Our results, as depicted in fig: patch count, indicate that the amount of discretization of patches did not affect the performance of the NLP agent, remaining a superior representation compared to the rest.

To conclude, our experiments suggest that NLP representations, though they describe the same raw information of the semantic segmentation maps, are more robust to task-nuisances, allow for better transfer, and achieve higher performance in complex tasks, even when their description is long and convoluted. While we've only presented results for DQN agents, we include plots for a PPO agent in the Appendix, showing similar trends and conclusions. We thus deduce that NLP-based semantic state representations are a preferable choice for training VizDoom agents.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-f0e63dc0919ddfcc744c15a0f9630380bfbb1a31841df333e6ff7386ba9f95a4

Passage ID: `qasper-passage-v1-f0e63dc0919ddfcc744c15a0f9630380bfbb1a31841df333e6ff7386ba9f95a4`; retrieval score: 1.4462783128420011.

Word count: 250.

```text
alive as long as possible, dodging inbound fireballs. The difficulty of the task increases over time, as additional monsters are spawned. In the defend the center scenario, melee attacking monsters are randomly spawned in the room, and charge towards the agent. As opposed to other scenarios, the agent is incapable of moving, aside from turning left and right and shooting. In the defend the line scenario, both melee and fireball shooting monsters are spawned near the opposing wall. The agent can only step right, left or shoot. Finally, in the “super" scenario both melee and fireball shooting monsters are repeatably spawned all over the room. the room contains various items the agent can pick up and use, such as medipacks, shotguns, ammunition and armor. Furthermore, the room is filled with unusable objects, various types of trees, pillars and other decorations. The agent can freely move and turn in any direction, as well as shoot. This scenario combines elements from all of the previous scenarios.

Our agent was implemented using a Convolutional Neural Network as described in Section SECREF4. We converted the parsed state into embedded representations of fixed length. We tested both a DQN and a PPO based agent, and compared the natural language representation to the other representation techniques, namely the raw image, feature vector, and semantic segmentation representations.

In order to effectively compare the performance of the different representation methods, we conducted our experiments under similar conditions for all agents. The same hyper-parameters were used under all tested
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-2ca96d945aff7df387625da70b240407f1a2e2b413bc69c6471ba85875bb475c

Passage ID: `qasper-passage-v1-2ca96d945aff7df387625da70b240407f1a2e2b413bc69c6471ba85875bb475c`; retrieval score: 1.4406375529049342.

Word count: 250.

```text
To convert each frame to a natural language representation state, the list of available labels is iterated, and a string is built accordingly. The main idea of our implementation is to divide the screen into multiple vertical patches, count the amount of different objects inside by their types, and parse it as a sentence. The decision as to whether an object is close or far can be determined by calculating the distance from it to the player, and using two threshold levels. Object descriptions can be concise or detailed, as needed. We experimented with the following mechanics:

the screen can be divided between patches equally, or by determined ratios. Here, our main guideline was to keep the "front" patch narrow enough so it can be used as "sights".

our initial experiment was with 3 patches, and later we added 2 more patches classified as "outer left" and "outer right". In our experiments we have tested up to 51 patches, referred to as left or right patch with corresponding numbers.

we used 2 thresholds, which allowed us to classify the distance of an object from the player as "close","mid", and "far. Depending on the task, the value of the threshold can be changed, as well as adding more thresholds.

different states might generate sentence with different size. A maximum sentence length is another parameter that was tested. sentences-length-table presents some data regarding the average word count in some of the game sceanrios.

After the sentence describing the state is generated, it
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-a05c58ebaebb607e07f3cdd87f812448b7867dfa365dbde3ae7db7f7d8dcc240

Passage ID: `qasper-passage-v1-a05c58ebaebb607e07f3cdd87f812448b7867dfa365dbde3ae7db7f7d8dcc240`; retrieval score: 1.4267262945188013.

Word count: 250.

```text
namely the raw image, feature vector, and semantic segmentation representations.

In order to effectively compare the performance of the different representation methods, we conducted our experiments under similar conditions for all agents. The same hyper-parameters were used under all tested representations. Moreover, to rule out effects of architectural expressiveness, the number of weights in all neural networks was approximately matched, regardless of the input type. Finally, we ensured the “super" scenario was positively biased toward image-based representations. This was done by adding a large amount items to the game level, thereby filling the state with nuisances (these tests are denoted by `nuisance' in the scenario name). This was especially evident in the NLP representations, as sentences became extensively longer (average of over 250 words). This is contrary to image-based representations, which did not change in dimension.

Results of the DQN-based agent are presented in fig: scenario comparison. Each plot depicts the average reward (across 5 seeds) of all representations methods. It can be seen that the NLP representation outperforms the other methods. This is contrary to the fact that it contains the same information as the semantic segmentation maps. More interestingly, comparing the vision-based and feature-based representations render inconsistent conclusions with respect to their relative performance. NLP representations remain robust to changes in the environment as well as task-nuisances in the state. As depicted in fig: nuisance scenarios, inflating the state space with task-nuisances impairs the performance of all representations. There, a large amount of unnecessary objects were spawned in
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1232.

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

#### Rank 1: qasper-passage-v1-7eeeb66ce633fe022dd3ebba3b703ec4a33f8b4fa9c7279786728656b552d38c

Passage ID: `qasper-passage-v1-7eeeb66ce633fe022dd3ebba3b703ec4a33f8b4fa9c7279786728656b552d38c`; retrieval score: 7.069618373013254.

Word count: 101.

```text
TV/Radio streams (speech-to-text). In particular, media monitors write intelligence reports about the most relevant events, and being able to search, visualize and explore news clusters assists in gathering more insight about a particular story. Since relevant events may be spawned from any part of the world (and from many multilingual sources), it becomes imperative to cluster news across different languages.

In terms of granularity, the type of story clusters we are interested in are the group of articles which, for example : (i) Narrate recent air-strikes in Eastern Ghouta (Syria); (ii) Describe the recent launch of Space X's Falcon Heavy rocket.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-dc820d802410e3394a60ffaf13b3da593480cf2c316dc0563211556b0b2f7ae8

Passage ID: `qasper-passage-v1-dc820d802410e3394a60ffaf13b3da593480cf2c316dc0563211556b0b2f7ae8`; retrieval score: 5.385156830196754.

Word count: 250.

```text
Our system was designed to cluster documents from a (potentially infinite) real-word data stream. The datasets typically used in the literature (TDT, Reuters) have a small number of clusters ( INLINEFORM0 20) with coarse topics (economy, society, etc.), and therefore are not relevant to the use case of media monitoring we treat - as it requires much more fine-grained story clusters about particular events. To evaluate our approach, we adapted a dataset constructed for the different purpose of binary classification of joining cluster pairs. We processed it to become a collection of articles annotated with monolingual and crosslingual cluster labels.

Statistics about this dataset are given in Table TABREF30 . As described further, we tune the hyper-parameter INLINEFORM0 on the development set. As for the hyper-parameters related to the timestamp features, we fixed INLINEFORM1 and tuned INLINEFORM2 on the development set, yielding INLINEFORM3 . To compute IDF scores (which are global numbers computed across a corpus), we used a different and much larger dataset that we collected from Deutsche Welle's news website (http://www.dw.com/). The dataset consists of 77,268, 118,045 and 134,243 documents for Spanish, English and German, respectively.

The conclusions from our experiments are: (a) the weighting of the similarity metric features using SVM significantly outperforms unsupervised baselines such as CluStream (Table TABREF35 ); (b) the SVM approach significantly helps to learn when to create a new cluster, compared to simple grid search for the optimal INLINEFORM0 (Table TABREF39 ); (c) separating the feature space into one for monolingual clusters
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1809.00540:6:1` | full | 0:601 |

#### Rank 3: qasper-passage-v1-e98e76fbe47365ebfacb0230704c45458fae013f2b1401bc0c8671e3efed09ee

Passage ID: `qasper-passage-v1-e98e76fbe47365ebfacb0230704c45458fae013f2b1401bc0c8671e3efed09ee`; retrieval score: 5.055172319832549.

Word count: 250.

```text
In our first set of experiments, we report results on monolingual clustering for each language separately. Monolingual clustering of a stream of documents is an important problem that has been inspected by others, such as by ahmed2011unified and by aggarwal2006framework. We compare our results to our own implementation of the online micro-clustering routine presented by aggarwal2006framework, which shall be referred to as CluStream. We note that CluStream of aggarwal2006framework has been a widely used state-of-the-art system in media monitoring companies as well as academia, and serves as a strong baseline to this day.

In our preliminary experiments, we also evaluated an online latent semantic analysis method, in which the centroids we keep for the function INLINEFORM0 (see § SECREF3 ) are the average of reduced dimensional vectors of the incoming documents as generated by an incremental singular value decomposition (SVD) of a document-term matrix that is updated after each incoming document. However, we discovered that online LSA performs significantly worse than representing the documents the way is described in § SECREF4 . Furthermore, it was also significantly slower than our algorithm due to the time it took to perform singular value decomposition.

Table TABREF35 gives the final monolingual results on the three datasets. For English, we see that the significant improvement we get using our algorithm over the algorithm of aggarwal2006framework is due to an increased recall score. We also note that the trained models surpass the baseline for all languages, and that the timestamp feature (denoted by TS), while
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-f77c472eb33b5e4cc2fb302868c1b874c1272ed16275d07f82dd93a9b618f2e0

Passage ID: `qasper-passage-v1-f77c472eb33b5e4cc2fb302868c1b874c1272ed16275d07f82dd93a9b618f2e0`; retrieval score: 5.031132963034448.

Word count: 250.

```text
improvement we get using our algorithm over the algorithm of aggarwal2006framework is due to an increased recall score. We also note that the trained models surpass the baseline for all languages, and that the timestamp feature (denoted by TS), while not required to beat the baseline, has a very relevant contribution in all cases. Although the results for both the baseline and our models seem to differ across languages, one can verify a consistent improvement from the latter to the former, suggesting that the score differences should be mostly tied to the different difficulty found across the datasets for each language. The presented scores show that our learning framework generalizes well to different languages and enables high quality clustering results.

To investigate the impact of the timestamp features, we ran an additional experiment using only the same three timestamp features as used in the best model on the English dataset. This experiment yielded scores of INLINEFORM0 , INLINEFORM1 and INLINEFORM2 , which lead us to conclude that while these features are not competitive when used alone (hence temporal information by itself is not sufficient to predict the clusters), they contribute significantly to recall with the final feature ensemble.

We note that as described in § SECREF3 , the optimization of the INLINEFORM0 parameter is part of the development process. The parameter INLINEFORM1 is a similarity threshold used to decide when an incoming document should merge to the best cluster or create a new one. We tune INLINEFORM2 on the development
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-8fe9ce642b75bcd938ff879c19c2d7afbbddfd8562f8d97673ae436d71761c1b

Passage ID: `qasper-passage-v1-8fe9ce642b75bcd938ff879c19c2d7afbbddfd8562f8d97673ae436d71761c1b`; retrieval score: 4.0325907549482.

Word count: 240.

```text
In § SECREF19 we introduced INLINEFORM0 and INLINEFORM1 as the weight vectors for the several document representation features. We experiment with both setting these weights to just 1 ( INLINEFORM2 and INLINEFORM3 ) and also learning these weights using support vector machines (SVMs). To generate the SVM training data, we simulate the execution of the algorithm on a training data partition (which we do not get evaluated on) and in which the gold standard labels are given. We run the algorithm using only the first subvector INLINEFORM4 , which is the TF-IDF vector with the words of the document in the body and title. For each incoming document, we create a collection of positive examples, for the document and the clusters which share at least one document in the gold labeling. We then generate 20 negative examples for the document from the 20 best-matching clusters which are not correct. To find out the best-matching clusters, we rank them according to their similarity to the input document using only the first subvector INLINEFORM5 .

Using this scheme we generate a collection of ranking examples (one for each document in the dataset, with the ranking of the best cluster matches), which are then trained using the SVMRank algorithm BIBREF3 . We run 5-fold cross-validation on this data to select the best model, and train both a separate model for each language according to INLINEFORM0 and a crosslingual model according to INLINEFORM1 .
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 1091.

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

#### Rank 1: qasper-passage-v1-7049c72a9f9d2c0548794ca384c671797de34462b51287b4ab1e316a7e61f1cc

Passage ID: `qasper-passage-v1-7049c72a9f9d2c0548794ca384c671797de34462b51287b4ab1e316a7e61f1cc`; retrieval score: 4.193273747806815.

Word count: 95.

```text
Figure FIGREF1 shows the architecture of the Sequicity framework as described in BIBREF8. In essence, in each turn, the Sequicity model first takes a bspan ($B_1$) and a response ($R_1$) which are determined in the previous step, and the current human question ($U_2$) to generate the current bspan. This bspan is then used together with a knowledge base to generate the corresponding machine answer ($R_2$), as shown in the right part of Figure FIGREF1.

The left part of that figure shows an example dialogue in a mixed-domain setting (which will be explained in Section SECREF3).
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-5545aa0a56c066788393f54163f266f6897ceb8a303ef6d2650361fcc0880e0c

Passage ID: `qasper-passage-v1-5545aa0a56c066788393f54163f266f6897ceb8a303ef6d2650361fcc0880e0c`; retrieval score: 2.7966425299794664.

Word count: 250.

```text
We use the publicly available dataset KVRET BIBREF5 in our experiments. This dataset is created by the Wizard-of-Oz method BIBREF10 on Amazon Mechanical Turk platform. This dataset includes dialogues in 3 domains: calendar, weather, navigation (POI) which is suitable for our mix-domain dialogue experiments. There are 2,425 dialogues for training, 302 for validation and 302 for testing, as shown in the upper half of Table TABREF12.

In this original dataset, each dialogue is of a single domain where all of its turns are on that domain. Each turn is composed of a sentence pair, one sentence is a user utterance, the other sentence is the corresponding machine response. A dialogue is a sequence of turns. To create mix-domain dialogues for our experiments, we make some changes in this dataset as follows:

We keep the dialogues in the calendar domain as they are.

We take a half of dialogues in the weather domain and a half of dialogues in the POI domain and mix their turns together, resulting in a dataset of mixed weather-POI dialogues. In this mixed-domain dialogue, there is a turn in the weather domain, followed by a turn in POI domain or vice versa.

We call this dataset the sequential turn dataset. Since the start turn of a dialogue has a special role in triggering the learning systems, we decide to create another and different mixed-domain dataset with the following mixing method:

The first turn and the last turn of each dialogue are kept as in their original.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1909.02265:5:0` | full | 0:434 |

#### Rank 3: qasper-passage-v1-c852416df2044435ee404ff57d86781c7ce43612e0cce6fbf661b766c309ff83

Passage ID: `qasper-passage-v1-c852416df2044435ee404ff57d86781c7ce43612e0cce6fbf661b766c309ff83`; retrieval score: 2.5659448574996184.

Word count: 250.

```text
kept unmixed, the match rates are better than those of the mixed training data. It is interesting to note that the GRU unit is much more sensitive with mixed data than the simple RNN unit with the corresponding absolute point drop of about 10%, compared to about 3.5%. However, the entity match rate is less important than the Success F1 score, where the GRU unit outperforms RNN in both sequential turn and random turn by a large margin. It is logical that if the test data are mixed but the training data are unmixed, we get lower scores than when both the training data and test data are mixed. The GRU unit is also better than the RNN unit on response generation in terms of BLEU scores.

We also see that the task-oriented dialogue system has difficulty running on mixed-domain dataset; it achieves only about 75.62% of Success F1 in comparison to about 81.1% (as reported in the Sequicity paper, not shown in our table). Appendix SECREF5 shows some example dialogues generated automatically by our implemented system.

In the second series of experiments, we evaluate the belief tracking components of two systems, the specialized multi-domain belief tracker and the Sequicity bspan component. As shown in the lower half of the Table TABREF21, Sequicity capability of belief tracking is much worse than that of the multi-domain belief tracker. The slot accuracy gap between the tools is about 21.6%, the value accuracy gap is about 34.4%; that is a large average gap
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-5d8612c12314c41cf8e82fc2afba4d1b54cbd144a1461853acef35a440dbc20b

Passage ID: `qasper-passage-v1-5d8612c12314c41cf8e82fc2afba4d1b54cbd144a1461853acef35a440dbc20b`; retrieval score: 2.5492139668880816.

Word count: 118.

```text
For the task-oriented Sequicity model, we keep the best parameter settings as reported in the original framework, on the same KVRET dataset BIBREF8. In particular, the hidden size of GRU unit is set to 50; the learning rate of Adam optimizer is 0.003. In addition to the original GRU unit, we also re-run this framework with simple RNN unit to compare the performance of different recurrent network types. The Sequicity tool is freely available for download.

For the multi-domain belief tracker model, we set the hidden size of LSTM units to 50 as in the original model; word embedding size is 300 and number of training epochs is 100. The corresponding tool is also freely available for download.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-cdd3f4b696627e8258ea08cdecaad398233fa0452d2208a23278431d67cf1785

Passage ID: `qasper-passage-v1-cdd3f4b696627e8258ea08cdecaad398233fa0452d2208a23278431d67cf1785`; retrieval score: 2.542081492870057.

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

Total retrieved words: 959.

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

#### Rank 1: qasper-passage-v1-58590acf1a779c951863da4b6f8ed39b7cacb06792efde5c67f7962dca085883

Passage ID: `qasper-passage-v1-58590acf1a779c951863da4b6f8ed39b7cacb06792efde5c67f7962dca085883`; retrieval score: 8.549983083348373.

Word count: 250.

```text
This section further investigates the effects of CoordNP annotation schemes on the behaviors of structurally-supervised models. We test whether an explicit COORD phrasal tag improves model performance. We trained two additional RNNG models on 38,546 sentences from the Penn Treebank annotated with two different schemes: The first, RNNG (PTB-control) was trained with the original Penn Treebank annotation. The second, RNNG (PTB-coord), was trained on the same sentences, but with an extended coordination annotation scheme, meant to employ the scheme employed in the FTB, adapted from BIBREF26. We stripped empty categories from their scheme and only kept the NP-COORD label for constituents inside a coordination structure. Figure FIGREF26 illustrates the detailed annotation differences between two datasets. We tested both models on all the experiments presented in Sections SECREF3-SECREF6 above.

Turning to the results of these six experiments: We see little difference between the two models in the Non-coordination agreement experiment. For the Complex coordination control and Complex coordination critical experiments, both models are largely the same as well. However, in the Simple and-coordination and Simple or-coordination experiments the values for all conditions are shifted upwards for the RNNG PTB-coord model, indicating higher over-all preference for the plural continuation. Furthermore, the range of values is reduced in the RNNG PTB-coord model, compared to the RNNG PTB-control model. These results indicate that adding an explicit COORD phrasal label does not drastically change model performance: Both models still appear to be using a linear combination of number features to drive plural vs. singular expectation.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-1d11f38bf0ee61e4fe1d21a5a5741bfd00e6fd4baaa139f61ceeb6367e6b1598

Passage ID: `qasper-passage-v1-1d11f38bf0ee61e4fe1d21a5a5741bfd00e6fd4baaa139f61ceeb6367e6b1598`; retrieval score: 8.428923906855438.

Word count: 250.

```text
The experiments presented here extend and refine a line of research investigating what linguistic knowledge is acquired by neural language models. Previous studies have demonstrated that sequential models trained on a simple regime of optimizing the next word can learn long-distance syntactic dependencies in impressive detail. Our results provide complimentary insights, demonstrating that a range of model architectures trained on a variety of datasets can learn fine-grained information about the interaction of CoordNPs and local syntactic context, but their behavior remains unhumanlike in many key ways. Furthermore, to our best knowledge, this work presents the first psycholinguistic analysis of neural language models trained on French, a high-resource language that has so far been under-investigated in this line of research.

In the simple coordination experiment, we demonstrated that models were able to capture some of the agreement behaviors of humans, although their performance deviated in crucial aspects. Whereas human behavior is best modeled as a `percolation' process, the neural models appear to be using a linear combination of NP constituent number to drive CoordNP/verb number agreement, with the second noun weighted more heavily than the first. In these experiments, supervision afforded by the RNNG and ActionLSTM models did not translate into more robust or humanlike learning outcomes. The complex coordination experiments provided evidence that the neural models tested were not using a simple `bag of features' strategy, but were sensitive to syntactic context. All models tested were able to interpret material that had similar surface form in ways that corresponded to
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-13b6ed99bcf5c17392fbb51f22217e9e4008d0678070ccecf507f0a752619a1d

Passage ID: `qasper-passage-v1-13b6ed99bcf5c17392fbb51f22217e9e4008d0678070ccecf507f0a752619a1d`; retrieval score: 8.368625441534531.

Word count: 195.

```text
are trained to output the probability distribution of the upcoming word given a context, without explicitly representing the structure of the context BIBREF9, BIBREF10. We trained two two-layer recurrent neural language models with long short-term memory architecture BIBREF11 on a relatively small corpus. The first model, referred as `LSTM (PTB)' in the following sections, was trained on the sentences from Penn Treebank BIBREF12. The second model, referred as `LSTM (FTB)', was trained on the sentences from French Treebank BIBREF13. We set the size of input word embedding and LSTM hidden layer of both models as 256.

We also compare LSTM language models trained on large corpora. We incorporate two pretrained English language models: one trained on the Billion Word benchmark (referred as `LSTM (1B)') from BIBREF14, and the other trained on English Wikipedia (referred as `LSTM (enWiki)') from BIBREF3. For French, we trained a large LSTM language model (referred as `LSTM (frWaC)') on a random subset (about 4 million sentences, 138 million word tokens) of the frWaC dataset BIBREF15. We set the size of the input embeddings and hidden layers to 400 for the LSTM (frWaC) model since it is trained on a large dataset.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1909.04625:2:0` | full | 0:622 |
| `1909.04625:2:1` | full | 0:602 |

#### Rank 4: qasper-passage-v1-94549b04c416ff96faf8de7ec296520d3077fe5dcef7052baa85150a798b08b3

Passage ID: `qasper-passage-v1-94549b04c416ff96faf8de7ec296520d3077fe5dcef7052baa85150a798b08b3`; retrieval score: 6.2596466990153.

Word count: 250.

```text
In addition to using phrase-level features to drive expectation about downstream lexical items, human processors can do the inverse—use lexical features to drive expectations about upcoming syntactic chunks. In this experiment, we assess whether neural models use number features hosted on a verb to modulate their expectations for upcoming CoordNPs.

To assess whether neural language models learn inverted coordination rules, we adapted items from Section SECREF13 in both English (37 items) and French (24 items), following the paradigm in Table TABREF24. The first part of the phrase contains either a plural or singular verb and a plural or singular noun. In this case, we sample the surprisal for the continuations and (or is grammatical in all conditions, so it is omitted from this study). Our expectation is that `and' is less surprising in the Vpl_Nsg condition than in the Vsg_Nsg condition, where a CoordNP is not licensed by the grammar in either French or English (as in *What is the pig and the cat eating?). We also expect lower surprisal for and in the Vpl_Nsg condition, where it is obligatory for a grammatical continuation, than in the Vpl_Npl condition, where it is optional.

For French experimental items, the question is embedded into a sentential-complement taking verb, following Example SECREF6, due to the fact that unembedded subject-verb inverted questions sound very formal and might be relatively rare in the training data.

. Je me demande où vont le maire et

I myself ask where go.3PL the.MSG mayor.MSG and

The results for
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-508d66a78a121e8a9ecd0adc71be553089e6e375ceea5beca8d57b6df0cd1143

Passage ID: `qasper-passage-v1-508d66a78a121e8a9ecd0adc71be553089e6e375ceea5beca8d57b6df0cd1143`; retrieval score: 4.851593493906278.

Word count: 250.

```text
To determine whether state-of-the-art neural architectures are capable of learning humanlike CoordNP/verb agreement properties, we adopt the psycholinguistics paradigm for model assessment. In this paradigm the models are tested using hand-crafted sentences designed to test underlying network knowledge. The assumption here is that if a model implicitly learns humanlike linguistic knowledge during training, its expectations for upcoming words should qualitatively match human expectations in novel contexts. For example, BIBREF1 and BIBREF6 assessed how well neural models had learned the subject/verb number agreement by feeding them with the prefix The keys to the cabinet .... If the models predicted the grammatical continuation are over the ungrammatical continuation is, they can be said to have learned the number agreement insofar as the number of the head noun and not the number of the distractor noun, cabinet, drives expectations about the number of the matrix verb.

If models are able to robustly modulate their expectations based on the internal components of the CoordNP, this will provide evidence that the networks are building up a context-sensitive phrase-level representation. We quantify model expectations as surprisal values. Surprisal is the negative log-conditional probability $S(x_i) = -\log _2 p(x_i|x_1 \dots x_{i-1})$ of a sentence's $i^{th}$ word $x_i$ given the previous words. Surprisal tells us how strongly $x_i$ is expected in context and is known to correlate with human processing difficulty BIBREF7, BIBREF0, BIBREF8. In the CoordNP/Verb agreement studies presented here, cases where the proceeding context sets high expectation for a number-inflected verb form $w_i$, (e.g. singular `is')
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1195.

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

#### Rank 1: qasper-passage-v1-16922aac64eaaa30b41da094551ed3c251d29057b4d306eea078d54246b0e6ca

Passage ID: `qasper-passage-v1-16922aac64eaaa30b41da094551ed3c251d29057b4d306eea078d54246b0e6ca`; retrieval score: 3.1263300988287575.

Word count: 250.

```text
In this paper, we present our work to support editors in the e-book annotation process. Specifically, we aim to provide tag recommendations that incorporate both the vocabulary of the editors and e-book readers. Therefore, we train various configurations of tag recommender approaches on editors' tags and Amazon search terms and evaluate them on a dataset containing Amazon review keywords. We find that combining both data sources enhances the quality of tag recommendations for annotating e-books. Furthermore, while approaches that train only on Amazon search terms provide poor performance concerning recommendation accuracy, we show that they still offer helpful annotations concerning recommendation diversity as well as our novel semantic similarity metric.

Future work. For future work, we plan to validate our findings using another dataset, e.g., by recommending tags for scientific articles and books in BibSonomy. With this, we aim to demonstrate the usefulness of the proposed approach in a similar domain and to enhance the reproducibility of our results by using an open dataset.

Moreover, we plan to evaluate our tag recommendation approaches in a study with domain users. Also, we want to improve our similarity-based approaches by integrating novel embedding approaches BIBREF16 , BIBREF17 as we did, for example, with our proposed semantic similarity evaluation metric. Finally, we aim to incorporate explanations for recommended tags so that editors of e-book annotations receive additional support in annotating e-books BIBREF21 . By making the underlying (semantic) reasoning visible to the editor who is in charge of tailoring annotations, we aim to
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-b04ebc8181736866472f3d956797fa76719b01b365f12103eab7f2bfce42bab9

Passage ID: `qasper-passage-v1-b04ebc8181736866472f3d956797fa76719b01b365f12103eab7f2bfce42bab9`; retrieval score: 2.4474279934520515.

Word count: 250.

```text
We implement three types of tag recommendation approaches, i.e., (i) popularity-based, (ii) similarity-based (i.e., using content information), and (iii) hybrid approaches. Due to the lack of personalized tags (i.e., we do not know which user has assigned a tag), we do not implement other types of algorithms such as collaborative filtering BIBREF8 . In total, we evaluate 19 different algorithms to recommend tags for annotating e-books.

Popularity-based approaches. We recommend the most frequently used tags in the dataset, which is a common strategy for tag recommendations BIBREF9 . That is, a most popular INLINEFORM0 approach for editor tags and a most popular INLINEFORM1 approach for Amazon search terms. For e-books, for which we also have author (= INLINEFORM2 and INLINEFORM3 ) or BISAC (= INLINEFORM4 and INLINEFORM5 ) information, we use these features to further filter the recommended tags, i.e., to only recommend tags that were used to annotate e-books of a specific author or a specific BISAC.

We combine both data sources (i.e., editor tags and Amazon search terms) using a round-robin combination strategy, which ensures an equal weight for both sources. This gives us three additional popularity-based algorithms (= INLINEFORM0 , INLINEFORM1 and INLINEFORM2 ).

Similarity-based approaches. We exploit the textual content of e-books (i.e., description or title) to recommend relevant tags BIBREF10 . For this, we first employ a content-based filtering approach BIBREF11 based on TF-IDF BIBREF12 to find top- INLINEFORM0 similar e-books. For each of the similar e-books, we then either extract the assigned editor tags
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-785ad65b33fc83e0adee538d4183e9cc8f88e967eb7f056eaada5b7c175f5d04

Passage ID: `qasper-passage-v1-785ad65b33fc83e0adee538d4183e9cc8f88e967eb7f056eaada5b7c175f5d04`; retrieval score: 2.1357020984649635.

Word count: 234.

```text
Figure FIGREF11 , using the description text to find similar e-books results in more accurate tag recommendations than using the title (i.e., INLINEFORM0 for INLINEFORM1 ). This is somehow expected as the description text consists of a bigger corpus of words (i.e., multiple sentences) than the title. Concerning the collected Amazon search query logs, extracting and then recommending tags from this source results in a much lower accuracy performance. Thus, these results also suggest to investigate beyond-accuracy metrics as done in Section SECREF17 .

Hybrid approaches. Figure FIGREF11 shows the accuracy results of the four hybrid approaches. By combining the best three popularity-based approaches, we outperform all of the initially evaluated popularity algorithms (i.e., INLINEFORM0 for INLINEFORM1 ). On the contrary, the combination of the two best performing similarity-based approaches INLINEFORM2 and INLINEFORM3 does not yield better accuracy. The negative impact of using a lower-performing approach such as INLINEFORM4 within a hybrid combination can also be observed in INLINEFORM5 for lower values of INLINEFORM6 . Overall, this confirms our initial intuition that combining the best performing popularity-based approach with the best similarity-based approach should result in the highest accuracy (i.e., INLINEFORM7 for INLINEFORM8 ). Moreover, our goal, namely to exploit editor tags in combination with search terms used by readers to increase the metadata quality of e-books, is shown to be best supported by applying hybrid approaches as they provide the best prediction results.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-5454615923fade31464287b7abaddf5ea3467383e829dc64d904d65bde623b6a

Passage ID: `qasper-passage-v1-5454615923fade31464287b7abaddf5ea3467383e829dc64d904d65bde623b6a`; retrieval score: 2.097410252842861.

Word count: 250.

```text
Our idea is to exploit user-generated search query terms in Amazon to mimic the vocabulary of users in Amazon, who search for e-books. We combine these search terms with tags assigned by editors in a hybrid tag recommendation approach. Thus, our aim is to show that we can improve the performance of tag recommender systems for e-books both concerning recommendation accuracy as well as semantic similarity and tag recommendation diversity.

Related work. In tag recommender systems, mostly content-based algorithms (e.g., BIBREF4 , BIBREF5 ) are used to recommend tags to annotate resources such as e-books. In our work, we incorporate both content features of e-books (i.e., title and description text) as well as Amazon search terms to account for the vocabulary of e-book readers.

Concerning the evaluation of tag recommendation systems, most studies focus on measuring the accuracy of tag recommendations (e.g., BIBREF2 ). However, the authors of BIBREF6 suggest also to use beyond-accuracy metrics such as diversity to evaluate the quality of tag recommendations. In our work, we measure recommendation diversity in addition to recommendation accuracy and propose a novel metric termed semantic similarity to validate semantic matches of tag recommendations.

Approach and findings. We exploit editor tags and user-generated search terms as input for tag recommendation approaches. Our evaluation comprises of a rich set of 19 different algorithms to recommend tags for e-books, which we group into (i) popularity-based, (ii) similarity-based (i.e., using content information), and (iii) hybrid approaches. We evaluate our approaches in terms of accuracy, semantic
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.04042:0:5` | partial | 0:404 |

#### Rank 5: qasper-passage-v1-cfb3492f4139b9befa7aa23ae287a0ed4a0e29053200a0041cc73f81b50f8b08

Passage ID: `qasper-passage-v1-cfb3492f4139b9befa7aa23ae287a0ed4a0e29053200a0041cc73f81b50f8b08`; retrieval score: 2.0006264332864747.

Word count: 145.

```text
evaluation comprises of a rich set of 19 different algorithms to recommend tags for e-books, which we group into (i) popularity-based, (ii) similarity-based (i.e., using content information), and (iii) hybrid approaches. We evaluate our approaches in terms of accuracy, semantic similarity and diversity on the review content of Amazon users, which reflects the readers' vocabulary. With semantic similarity, we measure how semantically similar (based on learned Doc2Vec BIBREF7 embeddings) the list of recommended tags is to the list of relevant tags. We use this additional metric to measure not only exact “hits” of our recommendations but also semantic matches.

Our evaluation results show that combining both data sources enhances the quality of tag recommendations for annotating e-books. Furthermore, approaches that solely train on Amazon search terms provide poor performance in terms of accuracy but deliver good results in terms of semantic similarity and recommendation diversity.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.04042:0:5` | partial | 126:791 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1129.

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

#### Rank 1: qasper-passage-v1-f0b0c4d78f5ae305c042f7686473eac6e2ce0e15cdf4b6221c2b1c41c8f88a5b

Passage ID: `qasper-passage-v1-f0b0c4d78f5ae305c042f7686473eac6e2ce0e15cdf4b6221c2b1c41c8f88a5b`; retrieval score: 7.711567638876417.

Word count: 250.

```text
prior with the von Mises-Fisher (vMF) distribution. With vMF, the KL loss only depends on the concentration parameter which is fixed during training and testing, and hence results in a constant KL loss. In a more recent work, BIBREF6 avoided latent variable collapse by including skip connections in the generative model, where the skip connections enforce strong links between the latent variables and the likelihood function.

Although the aforementioned works show effectiveness in addressing the latent variable collapse issue to some extent, they either require carefully engineering to balance the weight between the reconstruction loss and KL loss BIBREF0, BIBREF8, or resort to designing more sophisticated model structures BIBREF7, BIBREF5, BIBREF6.

In this paper, we present a simple architecture called holistic regularisation VAE (HR-VAE), which can effectively avoid latent variable collapse. In contrast to existing VAE-RNN models for text modelling which merely impose a standard normal distribution prior on the last hidden state of the RNN encoder, our HR-VAE model imposes regularisation for all hidden states of the RNN encoder. Another advantage of our model is that it is generic and can be applied to any existing VAE-RNN-based architectures.

We evaluate our model against several strong baselines which apply VAE for text modelling BIBREF0, BIBREF7, BIBREF5. We conducted experiments based on two public benchmark datasets, namely, the Penn Treebank dataset BIBREF9 and the end-to-end (E2E) text generation dataset BIBREF10. Experimental results show that our HR-VAE model not only can effectively mitigate the latent variable collapse issue with a stable training
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-db40baad55c54ae14fb5fe1cc936ca0969ac4d000e5e9b0924c6bfac6c66e075

Passage ID: `qasper-passage-v1-db40baad55c54ae14fb5fe1cc936ca0969ac4d000e5e9b0924c6bfac6c66e075`; retrieval score: 5.004399363172016.

Word count: 72.

```text
We evaluate our model on two public datasets, namely, Penn Treebank (PTB) BIBREF9 and the end-to-end (E2E) text generation corpus BIBREF10, which have been used in a number of previous works for text generation BIBREF0, BIBREF5, BIBREF11, BIBREF12. PTB consists of more than 40,000 sentences from Wall Street Journal articles whereas the E2E dataset contains over 50,000 sentences of restaurant reviews. The statistics of these two datasets are summarised in Table TABREF11.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-11350ae2caee96a5d963c16c81346db7eefca747cb76b2d0b5283b96e7182be4

Passage ID: `qasper-passage-v1-11350ae2caee96a5d963c16c81346db7eefca747cb76b2d0b5283b96e7182be4`; retrieval score: 4.501352712999187.

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

#### Rank 4: qasper-passage-v1-e1f588f04d0f75e6f51ddb0713732c3a06c93ac0ec90d9e34da087a45f7c5f68

Passage ID: `qasper-passage-v1-e1f588f04d0f75e6f51ddb0713732c3a06c93ac0ec90d9e34da087a45f7c5f68`; retrieval score: 3.8485550182168358.

Word count: 250.

```text
Variational Autoencoder (VAE) BIBREF1 is a powerful method for learning representations of high-dimensional data. However, recent attempts of applying VAEs to text modelling are still far less successful compared to its application to image and speech BIBREF2, BIBREF3, BIBREF4. When applying VAEs for text modelling, recurrent neural networks (RNNs) are commonly used as the architecture for both encoder and decoder BIBREF0, BIBREF5, BIBREF6. While such a VAE-RNN based architecture allows encoding and generating sentences (in the decoding phase) with variable-length effectively, it is also vulnerable to an issue known as latent variable collapse (or KL loss vanishing), where the posterior collapses to the prior and the model will ignore the latent codes in generative tasks.

Various efforts have been made to alleviate the latent variable collapse issue. BIBREF0 uses KL annealing, where a variable weight is added to the KL term in the cost function at training time. BIBREF7 discovered that there is a trade-off between the contextual capacity of the decoder and effective use of encoding information, and developed a dilated CNN as decoder which can vary the amount of conditioning context. They also introduced a loss clipping strategy in order to make the model more robust. BIBREF5 addressed the problem by replacing the standard normal distribution for the prior with the von Mises-Fisher (vMF) distribution. With vMF, the KL loss only depends on the concentration parameter which is fixed during training and testing, and hence results in a constant KL loss. In a more recent work, BIBREF6 avoided
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-cfd9b709df0936e2c3a0e348c03905f641b49fbb26a766e2a795a7e494a53674

Passage ID: `qasper-passage-v1-cfd9b709df0936e2c3a0e348c03905f641b49fbb26a766e2a795a7e494a53674`; retrieval score: 3.64594438990588.

Word count: 250.

```text
In this section, we discuss the technical details of the proposed holistic regularisation VAE (HR-VAE) model, a general architecture which can effectively mitigate the KL vanishing phenomenon.

Our model design is motivated by one noticeable defect shared by the VAE-RNN based models in previous works BIBREF0, BIBREF7, BIBREF5, BIBREF6. That is, all these models, as shown in Figure FIGREF2, only impose a standard normal distribution prior on the last hidden state of the RNN encoder, which potentially leads to learning a suboptimal representation of the latent variable and results in model vulnerable to KL loss vanishing. Our hypothesis is that to learn a good representation of data and a good generative model, it is crucial to impose the standard normal prior on all the hidden states of the RNN-based encoder (see Figure FIGREF2), which allows a better regularisation of the model learning process.

We implement the HR-VAE model using a two-layer LSTM for both the encoder and decoder. However, one should note that our architecture can be readily applied to other types of RNN such as GRU. For each time stamp $t$ (see Figure FIGREF2), we concatenate the hidden state $\mathbf {h}_t$ and the cell state $\mathbf {c}_t$ of the encoder. The concatenation (i.e., $[\mathbf {h}_t;\mathbf {c}_t]$) is then fed into two linear transformation layers for estimating $\mu _t$ and $\sigma ^2_t$, which are parameters of a normal distribution corresponding to the concatenation of $\mathbf {h}_t$ and $\mathbf {c}_t$. Let $Q_{\phi _t}(\mathbf {z}_t | \mathbf {x})=\mathcal {N}(\mathbf {z}_t|\mu _t,\sigma ^2_t)$,
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 904.

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

#### Rank 1: qasper-passage-v1-0d76e3f25cff04bce53e424b453c2afd932c7235faa265a385b4f81539f02914

Passage ID: `qasper-passage-v1-0d76e3f25cff04bce53e424b453c2afd932c7235faa265a385b4f81539f02914`; retrieval score: 8.620399870966164.

Word count: 115.

```text
with a special focus on assessing human–machine parity: the choice of raters, the use of linguistic context, and the creation of reference translations. We focus on the data shared by BIBREF3, and empirically test to what extent changes in the evaluation design affect the outcome of the human evaluation. We find that for all three aspects, human translations are judged more favourably, and significantly better than MT, when we make changes that we believe strengthen the evaluation design. Based on our empirical findings, we formulate a set of recommendations for human MT evaluation in general, and assessing human–machine parity in particular. All of our data are made publicly available for external validation and further analysis.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-185d7eb81eafc2b46f77840f8fae547c09de30322412e82f8635383b6ef9777c

Passage ID: `qasper-passage-v1-185d7eb81eafc2b46f77840f8fae547c09de30322412e82f8635383b6ef9777c`; retrieval score: 7.545080153380738.

Word count: 250.

```text
Machine translation (MT) has made astounding progress in recent years thanks to improvements in neural modelling BIBREF0, BIBREF1, BIBREF2, and the resulting increase in translation quality is creating new challenges for MT evaluation. Human evaluation remains the gold standard, but there are many design decisions that potentially affect the validity of such a human evaluation.

This paper is a response to two recent human evaluation studies in which some neural machine translation systems reportedly performed at (or above) the level of human translators for news translation from Chinese to English BIBREF3 and English to Czech BIBREF4, BIBREF5.

Both evaluations were based on current best practices in the field: they used a source-based direct assessment with non-expert annotators, using data sets and the evaluation protocol of the Conference on Machine Translation (WMT). While the results are intriguing, especially because they are based on best practices in MT evaluation, BIBREF5 warn against taking their results as evidence for human–machine parity, and caution that for well-resourced language pairs, an update of WMT evaluation style will be needed to keep up with the progress in machine translation. We concur that these findings have demonstrated the need to critically re-evaluate the design of human MT evaluation.

Our paper investigates three aspects of human MT evaluation, with a special focus on assessing human–machine parity: the choice of raters, the use of linguistic context, and the creation of reference translations. We focus on the data shared by BIBREF3, and empirically test to what extent changes in the
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-d522b1b0108be57e67d77e4cc48013b48380cc8d8ef53591093bf37870e87fb6

Passage ID: `qasper-passage-v1-d522b1b0108be57e67d77e4cc48013b48380cc8d8ef53591093bf37870e87fb6`; retrieval score: 6.300356298825496.

Word count: 127.

```text
not allow conclusions to be drawn about the order of magnitude of the differences, so that it is not possible to determine how much better system A was than system B.

This is one of the reasons why direct assessment has prevailed as an evaluation method more recently. In contrast to relative ranking, the raters are presented with one MT output at a time, to which they assign a score between 0 and 100. To increase homogeneity, each rater's ratings are standardised BIBREF11. Reference translations serve as the basis in the context of WMT, and evaluations are carried out by monolingual raters. To avoid reference bias, the evaluation can be based on source texts instead, which presupposes bilingual raters, but leads to more reliable results overall BIBREF12.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-d9912276e03e19b68feda70869dfab3bc93a7720681ee9fa49d0efb9da78849d

Passage ID: `qasper-passage-v1-d9912276e03e19b68feda70869dfab3bc93a7720681ee9fa49d0efb9da78849d`; retrieval score: 6.141087684328523.

Word count: 72.

```text
Our experiments in Sections SECREF3–SECREF5 show that machine translation quality has not yet reached the level of professional human translation, and that human evaluation methods which are currently considered best practice fail to reveal errors in the output of strong NMT systems. In this section, we recommend a set of evaluation design changes that we believe are needed for assessing human–machine parity, and will strengthen the human evaluation of MT in general.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-752b4c806584dbec207f800091d7e79a85706ae51035029e712a5d7a397bf48b

Passage ID: `qasper-passage-v1-752b4c806584dbec207f800091d7e79a85706ae51035029e712a5d7a397bf48b`; retrieval score: 6.100138247527472.

Word count: 250.

```text
We compared professional human Chinese to English translations to the output of a strong MT system. In a human evaluation following best practices, BIBREF3 found no significant difference between the two, concluding that their NMT system had reached parity with professional human translation. Our blind qualitative analysis, however, showed that the machine translation output contained significantly more incorrect words, omissions, mistranslated names, and word order errors.

Our experiments show that recent findings of human–machine parity in language translation are owed to weaknesses in the design of human evaluation campaigns. We empirically tested alternatives to what is currently considered best practice in the field, and found that the choice of raters, the availability of linguistic context, and the creation of reference translations have a strong impact on perceived translation quality. As for the choice of raters, professional translators showed a significant preference for human translation, while non-expert raters did not. In terms of linguistic context, raters found human translation significantly more accurate than machine translation when evaluating full documents, but not when evaluating single sentences out of context. They also found human translation significantly more fluent than machine translation, both when evaluating full documents and single sentences. Moreover, we showed that aggressive editing of human reference translations for target language fluency can decrease adequacy to the point that they become indistinguishable from machine translation, and that raters found human translations significantly better than machine translations of original source texts, but not of source texts that were translations themselves.

Our results strongly
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 814.

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

#### Rank 1: qasper-passage-v1-9a0b1445751347b85f02465d400572cc59e0bfe3d662ed32cc1011da5b94ecdf

Passage ID: `qasper-passage-v1-9a0b1445751347b85f02465d400572cc59e0bfe3d662ed32cc1011da5b94ecdf`; retrieval score: 8.189608834164744.

Word count: 104.

```text
We set up experiments in order to answer the following research questions:

RQ1: Can the comparative evaluator correlate better with human preference in sample-level than previous automated metrics when evaluating open domain NLG models?

RQ2: Can the comparative evaluator correlate better with human preference in model-level, so that our approach can measure the progress on open domain NLG better?

RQ3: As existing approaches fail to correlate well with human preference, whether and to what extent this problem affects the quality of the final NLG model when performing hyperparameter search and early-stopping?

RQ4: If the previous problem exists, can proposed comparative evaluator reduce this problem?
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-60a170c52b8885055be4246e4964e2b2588a93d964311bc3204813f1851c4b06

Passage ID: `qasper-passage-v1-60a170c52b8885055be4246e4964e2b2588a93d964311bc3204813f1851c4b06`; retrieval score: 1.9075055783241963.

Word count: 174.

```text
As our objective is to evaluate the evaluators rather than comparing state-of-the-art models, we choose three representative sequence-to-sequence architectures: LSTM BIBREF27 seq2seq, Convolutional seq2seq BIBREF28, and transformer BIBREF1 model. We compare models with different architectures, hyperparameter choices, and early-stopping criteria with different automated metrics, as well as human evaluation.

Regarding the evaluation metric (and criteria for choosing hyperparameter choice and early-stopping), we compare the proposed approach with the discriminative evaluator, BLEU score (average of 2-, 3-, 4-grams), perplexity, and ADEM. When evaluating generated stories, we cut off the story at the nearest sentence for stories longer than 250 words.

The proposed comparative evaluator is employed for choosing hyperparameter by performing skill rating among all models trained with different hyperparameter choices. For early-stopping, as incrementally performing skill rating is computationally expensive, we propose to perform n (e.g. 1000) pairwise comparison between the samples generated by the latest checkpoint and the previous k (e.g. 2) checkpoints and stop training when the wining rate of latest checkpoint keeps being smaller than its losing rate for 5 iterations.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-b617c0907b75b0879543786d0e5f10346f73e3617be137697d0bf048b8bce22c

Passage ID: `qasper-passage-v1-b617c0907b75b0879543786d0e5f10346f73e3617be137697d0bf048b8bce22c`; retrieval score: 1.7985043368009808.

Word count: 204.

```text
We further investigate the impact of imperfect metrics on training NLG models. As described in the human evaluation procedure, we perform 10 runs to test the reliability of each metric when used to perform hyperparameter tuning and early-stopping respectively. In each run, we select the best hyperparameter combination or early-stopping checkpoint based on each of the five compared metrics. Human evaluation is then employed to identify the best choice. We evaluate the performance of each metric by how many times (out of 10) they succeeded in selecting the best hyperparameter combination or early-stopping checkpoint (out of 4) and the average human-annotated score for their selected models.

The results are shown in Table 3. We can see that conventional automated metrics perform poorly and result in sub-optimal result when performing hyperparameter search and selecting the best performing checkpoints. Converting evaluation metric from BLEU or perplexity to the proposed comparative evaluator can yield non-neglectable improvements without changing model architecture or training objective. While previous work on NLG evaluation mostly focuses on the evaluation stage and does not explore the influence of imperfect metrics during model training, our experiments demonstrate the existence of this problem and that the proposed method can, to some extent, alleviate this problem.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-bdf8b87527cabfba2e025be2b0b9428bc4b2e2cb68e0e664725be754467c905a

Passage ID: `qasper-passage-v1-bdf8b87527cabfba2e025be2b0b9428bc4b2e2cb68e0e664725be754467c905a`; retrieval score: 1.7499421188598074.

Word count: 71.

```text
comparison model. The skill rating system is more efficient and accurate than several baseline approaches.

We conduct experiments on both story generation task and open domain dialogue response generation task. Experimental results show that our approach correlates better with human evaluation on both datasets. Moreover, we show that using automated metrics such as BLEU to perform hyperparameter tuning and early-stopping results in sub-optimal model and our approach helps alleviate this problem.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-940793365b7f6228adbef8fab71b1c7b00d2643a29125d1d9a7bdb7e0b6248ab

Passage ID: `qasper-passage-v1-940793365b7f6228adbef8fab71b1c7b00d2643a29125d1d9a7bdb7e0b6248ab`; retrieval score: 1.5764028645448978.

Word count: 250.

```text
Evaluation of NLG models has been a long-standing open problem. While human evaluation may be ideal, it is generally expensive to conduct and does not scale well. Various automated evaluation approaches are proposed to facilitate the development and evaluation of NLG models. We summarize these evaluation approaches below.

Text Overlap Metrics, including BLEU BIBREF5, METEOR BIBREF6 and ROUGE BIBREF7, are the most popular metrics employed in the evaluation of NLG models. They evaluate generated text by comparing the similarity between the generated text and human written references. While this works well in tasks where the diversity of acceptable output is limited, such as machine translation and text summarization, text overlap metrics are shown to have weak or no correlation with human judgments in open domain natural language generation tasks BIBREF8. There are two major drawbacks in these metrics. First, text overlap metrics can not distinguish minor variations in a generated text which may make the sentence not equally grammatically correct or semantically meaningful. Second, there may exist multiple equally good outputs for the given input and comparing against one gold reference can be erroneous.

Perplexity is commonly used to evaluate the quality of a language model. It measures how well a probability distribution predicts a sample and captures the degree of uncertainty in the model. It is used to evaluate models in open-domain NLG tasks such as story generation BIBREF2 and open domain dialogue systems. However, “how likely a sentence is generated by a given model” may not be comparable
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2002.05058:1:0` | full | 0:323 |
| `2002.05058:1:1` | full | 0:897 |
| `2002.05058:1:2` | partial | 0:398 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 803.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "d449825aa0a1d27531a41dd5ec098834f1fde4a8": {
    "unresolved_evidence": [],
    "paragraphs": {
      "2002.05058:1:2": [
        [
          398,
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

#### Rank 1: qasper-passage-v1-f2b44b6c6c72ea00288b13ffac1b444bb68854b5090e4037afda0851337c3b7f

Passage ID: `qasper-passage-v1-f2b44b6c6c72ea00288b13ffac1b444bb68854b5090e4037afda0851337c3b7f`; retrieval score: 7.784158590989809.

Word count: 47.

```text
MT automatic evaluation metrics, namely BLEU BIBREF3 and TER BIBREF4.

In this paper we describe the UDS-DFKI system to the WMT 2019 Similar Language Translation task. The system achieved competitive performance and ranked second among ten entries in Czech to Polish translation in terms of BLEU score.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-bd111aa3b3c4b224d8a1a2db7aa94741c3af8c054b6464b6fa9d7beb888f7503

Passage ID: `qasper-passage-v1-bd111aa3b3c4b224d8a1a2db7aa94741c3af8c054b6464b6fa9d7beb888f7503`; retrieval score: 7.410408205706436.

Word count: 138.

```text
This paper presented the UDS-DFKI system submitted to the Similar Language Translation shared task at WMT 2019. We presented the results obtained by our system in translating from Czech to Polish. Our system achieved competitive performance ranking second among ten teams in the competition in terms of BLEU score. The fact that out-of-domain data was provided by the organizers resulted in a challenging but interesting scenario for all participants.

In future work, we would like to investigate how effective is the proposed hypothesis (i.e., word-BPE level information) in similar language translation. Furthermore, we would like to explore the similarity between these two languages (and the other two language pairs in the competition) in more detail by training models that can best capture morphological differences between them. During such competitions, this is not always possible due to time constraints.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-14abb1045789420f34e207c765ef706762aac3ba838ed100355209508ba6465c

Passage ID: `qasper-passage-v1-14abb1045789420f34e207c765ef706762aac3ba838ed100355209508ba6465c`; retrieval score: 7.068886816423645.

Word count: 250.

```text
The shared tasks organized annually at WMT provide important benchmarks used in the MT community. Most of these shared tasks include English data, which contributes to make English the most resource-rich language in MT and NLP. In the most popular WMT shared task for example, the News task, MT systems have been trained to translate texts from and to English BIBREF0, BIBREF1.

This year, we have observed a shift on the dominant role that English on the WMT shared tasks. The News task featured for the first time two language pairs which did not include English: German-Czech and French-German. In addition to that, the Similar Language Translation was organized for the first time at WMT 2019 with the purpose of evaluating the performance of MT systems on three pairs of similar languages from three different language families: Ibero-Romance, Indo-Aryan, and Slavic.

The Similar Language Translation BIBREF2 task provided participants with training, development, and testing data from the following language pairs: Spanish - Portuguese (Romance languages), Czech - Polish (Slavic languages), and Hindi - Nepali (Indo-Aryan languages). Participant could submit system outputs to any of the three language pairs in any direction. The shared task attracted a good number of participants and the performance of all entries was evaluated using popular MT automatic evaluation metrics, namely BLEU BIBREF3 and TER BIBREF4.

In this paper we describe the UDS-DFKI system to the WMT 2019 Similar Language Translation task. The system achieved competitive performance and ranked second among ten entries in Czech to
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-fae09679617e1f6f670d43ddbd63d6b660a52587be3e86816aca91ddd221cac3

Passage ID: `qasper-passage-v1-fae09679617e1f6f670d43ddbd63d6b660a52587be3e86816aca91ddd221cac3`; retrieval score: 5.284724870629875.

Word count: 186.

```text
We present the results obtained by our system in Table TABREF8.

Our fine-tuned system on development set provides significant performance improvement over the generic model. We found +12.9 absolute BLEU points improvement over the generic model. Similar improvement is also observed in terms of TER (-16.9 absolute). It is to be noted that our generic model is trained solely on the clean version of training data.

Before submission, we performed punctuation normalization, unicode normalization, and detokenization for the run.

In Table TABREF9 we present the ranking of the competition provided by the shared task organizers. Ten entries were submitted by five teams and are ordered by BLEU score. TER is reported for all submissions which achieved BLEU score greater than 5.0. The type column specifies the type of system, whether it is a Primary (P) or Constrastive (C) entry.

Our system was ranked second in the competition only 0.3 BLEU points behind the winning team UPC-TALP. The relative low BLEU and high TER scores obtained by all teams are due to out-of-domain data provided in the competition which made the task equally challenging to all participants.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-cacf7dd28a1d3233c228eca2774418567c9285cdfccab928c6c23d30d2f9f1db

Passage ID: `qasper-passage-v1-cacf7dd28a1d3233c228eca2774418567c9285cdfccab928c6c23d30d2f9f1db`; retrieval score: 4.197722726736459.

Word count: 250.

```text
The out-domain data is noisy for our purposes, so we apply methods for cleaning. We performed the following two steps: (i) we use the cleaning process described in Pal:2015:WMT, and (ii) we execute the Moses BIBREF10 corpus cleaning scripts with minimum and maximum number of tokens set to 1 and 100, respectively. After cleaning, we perform punctuation normalization, and then we use the Moses tokenizer to tokenize the out-domain corpus with `no-escape' option. Finally, we apply true-casing.

The cleaned version of the released data, i.e., the General corpus containing 1,394,319 sentences, is sorted based on the score in Equation DISPLAY_FORM2. Thereafter, We split the entire data (1,394,319) into two sets; we use the first 1,000 for validation and the remaining as training data. The released development set (Dev) is used as test data for our experiment. It should be noted noted that, we exclude 1,000 sentences from the General corpus which are scored as top (i.e., more in-domain like) during the data selection process.

We prepare two parallel training sets from the aforementioned training data: (i) transference500K(presented next), collected 500,000 parallel data through data selection method BIBREF11, which are very similar to the in-domain data (for our case the development set), and (ii) transferenceALL, utilizing all the released out-domain data sorted by Equation DISPLAY_FORM2.

The transference500Ktraining set is prepared using in-domain (development set) bilingual cross-entropy difference for data selection as was described in Axelrod:2011. The difference in cross-entropy is computed based on two language models (LM): a domain-specific LM is
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 871.

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

#### Rank 1: qasper-passage-v1-c63f4caeef84e396944b6750f4d79a6931e759191945b5450f6072e93abf90fb

Passage ID: `qasper-passage-v1-c63f4caeef84e396944b6750f4d79a6931e759191945b5450f6072e93abf90fb`; retrieval score: 6.112531062068877.

Word count: 250.

```text
cross-validation on the account's level. For the FacTweet model, we experiment with 25% of the accounts for validation and parameters selection. We use hyperopt library to select the hyper-parameters on the following values: LSTM layer size (16, 32, 64), dropout ($0.0-0.9$), activation function ($relu$, $selu$, $tanh$), optimizer ($sgd$, $adam$, $rmsprop$) with varying the value of the learning rate (1e-1,..,-5), and batch size (4, 8, 16). The validation split is extracted on the class level using stratified sampling: we took a random 25% of the accounts from each class since the dataset is unbalanced. Discarding the classes' size in the splitting process may affect the minority classes (e.g. hoax). For the baselines' classifier, we tested many classifiers and the LR showed the best overall performance.

Results. Table TABREF25 presents the results. We present the results using a chunk size of 20, which was found to be the best size on the held-out data. Figure FIGREF24 shows the results of different chunks sizes. FacTweet performs better than the proposed baselines and obtains the highest macro-F1 value of $0.565$. Our results indicate the importance of taking into account the sequence of the tweets in the accounts' timelines. The sequence of these tweets is better captured by our proposed model sequence-agnostic or non-neural classifiers. Moreover, the results demonstrate that the features at tweet-level do not perform well to detect the Twitter accounts factuality, since they obtain a result near to the majority class ($0.18$). Another finding from our experiments shows that the performance of
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1910.06592:2:11` | partial | 33:847 |

#### Rank 2: qasper-passage-v1-c880b2d723bf59071c8f2e2b2c9c6ab395c98586f9c05eeff7be0d957f70fcc6

Passage ID: `qasper-passage-v1-c880b2d723bf59071c8f2e2b2c9c6ab395c98586f9c05eeff7be0d957f70fcc6`; retrieval score: 2.681363815464733.

Word count: 173.

```text
Moreover, the results demonstrate that the features at tweet-level do not perform well to detect the Twitter accounts factuality, since they obtain a result near to the majority class ($0.18$). Another finding from our experiments shows that the performance of the Tweet2vec is weak. This demonstrates that tweets' hashtags are not informative to detect non-factual accounts. In Table TABREF25, we present ablation tests so as to quantify the contribution of subset of features. The results indicate that most performance gains come from words embeddings, style, and morality features. Other features (emotion and sentiment) show lower importance: nevertheless, they still improve the overall system performance (on average 0.35% Macro-F$_1$ improvement). These performance figures suggest that non-factual accounts use semantic and stylistic hidden signatures mostly while tweeting news, so as to be able to mislead the readers and behave as reputable (i.e., factual) sources. We leave a more fine-grained, diachronic analysis of semantic and stylistic features – how semantic and stylistic signature evolve across time and change across the accounts' timelines – for future work.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-f41419b100105ac9bc90857721d90278f029e83fb7e7322261ba3ff2ba9a7536

Passage ID: `qasper-passage-v1-f41419b100105ac9bc90857721d90278f029e83fb7e7322261ba3ff2ba9a7536`; retrieval score: 2.0063770211877583.

Word count: 250.

```text
To represent the tweets, we use the decoded embedding produced by the model. With this baseline we aim at assessing if the tweets' hashtags may help detecting the non-factual accounts.

LR + All Features (tweet-level): We extract all our features from each tweet and feed them into a LR classifier. Here, we do not aggregate over tweets and thus view each tweet independently.

LR + All Features (chunk-level): We concatenate the features' vectors of the tweets in a chunk and feed them into a LR classifier.

FacTweet (tweet-level): Similar to the FacTweet approach, but at tweet-level; the sequential flow of the tweets is not utilized. We aim at investigating the importance of the sequential flow of tweets.

Top-$k$ replies, likes, or re-tweets: Some approaches in rumors detection use the number of replies, likes, and re-tweets to detect rumors BIBREF21. Thus, we extract top $k$ replied, liked or re-tweeted tweets from each account to assess the accounts factuality. We tested different $k$ values between 10 tweets to the max number of tweets from each account. Figure FIGREF24 shows the macro-F1 values for different $k$ values. It seems that $k=500$ for the top replied tweets achieves the highest result. Therefore, we consider this as a baseline.

Experimental Setup. We apply a 5 cross-validation on the account's level. For the FacTweet model, we experiment with 25% of the accounts for validation and parameters selection. We use hyperopt library to select the hyper-parameters on the following values: LSTM layer size (16, 32, 64), dropout
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1910.06592:2:11` | partial | 0:295 |

#### Rank 4: qasper-passage-v1-1f5365012edf3926879c735f739998473e5e2bb29fba86c631da6226035f78af

Passage ID: `qasper-passage-v1-1f5365012edf3926879c735f739998473e5e2bb29fba86c631da6226035f78af`; retrieval score: 1.878604365704211.

Word count: 250.

```text
the misleading ones. Consequently, we investigate ways to detect suspicious accounts by considering their tweets in groups (chunks). Our hypothesis is that suspicious accounts have a unique pattern in posting tweet sequences. Since their intention is to mislead, the way they transition from one set of tweets to the next has a hidden signature, biased by their intentions. Therefore, reading these tweets in chunks has the potential to improve the detection of the fake news accounts.

In this work, we investigate the problem of discriminating between factual and non-factual accounts in Twitter. To this end, we collect a large dataset of tweets using a list of propaganda, hoax and clickbait accounts and compare different versions of sequential chunk-based approaches using a variety of feature sets against several baselines. Several approaches have been proposed for news verification, whether in social media (rumors detection) BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, or in news claims BIBREF5, BIBREF6, BIBREF7, BIBREF8. The main orientation in the previous works is to verify the textual claims/tweets but not their sources. To the best of our knowledge, this is the first work aiming to detect factuality at the account level, and especially from a textual perspective. Our contributions are:

[leftmargin=4mm]

We propose an approach to detect non-factual Twitter accounts by treating post streams as a sequence of tweets' chunks. We test several semantic and dictionary-based features together with a neural sequential approach, and apply an ablation test to investigate their contribution.

We benchmark our approach against other approaches that
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-d2e46064a62f389b125e5d675f96fa636d23c8945b853633e106a6d893a8dc41

Passage ID: `qasper-passage-v1-d2e46064a62f389b125e5d675f96fa636d23c8945b853633e106a6d893a8dc41`; retrieval score: 1.8422535106044573.

Word count: 250.

```text
Data. We build a dataset of Twitter accounts based on two lists annotated in previous works. For the non-factual accounts, we rely on a list of 180 Twitter accounts from BIBREF1. This list was created based on public resources where suspicious Twitter accounts were annotated with the main fake news types (clickbait, propaganda, satire, and hoax). We discard the satire labeled accounts since their intention is not to mislead or deceive. On the other hand, for the factual accounts, we use a list with another 32 Twitter accounts from BIBREF19 that are considered trustworthy by independent third parties. We discard some accounts that publish news in languages other than English (e.g., Russian or Arabic). Moreover, to ensure the quality of the data, we remove the duplicate, media-based, and link-only tweets. For each account, we collect the maximum amount of tweets allowed by Twitter API. Table TABREF13 presents statistics on our dataset.

Baselines. We compare our approach (FacTweet) to the following set of baselines:

[leftmargin=4mm]

LR + Bag-of-words: We aggregate the tweets of a feed and we use a bag-of-words representation with a logistic regression (LR) classifier.

Tweet2vec: We use the Bidirectional Gated recurrent neural network model proposed in BIBREF20. We keep the default parameters that were provided with the implementation. To represent the tweets, we use the decoded embedding produced by the model. With this baseline we aim at assessing if the tweets' hashtags may help detecting the non-factual accounts.

LR + All Features (tweet-level): We extract all our features
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1173.

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

#### Rank 1: qasper-passage-v1-6a33f9dfebae50d99f25fe03397beb325254da22ca428e49fc6218f8d555850e

Passage ID: `qasper-passage-v1-6a33f9dfebae50d99f25fe03397beb325254da22ca428e49fc6218f8d555850e`; retrieval score: 6.114326656090714.

Word count: 250.

```text
$\textsc {Zero-stc}$ was first explored by the paradigm “Dataless Classification” BIBREF0. Dataless classification first maps the text and labels into a common space by Explicit Semantic Analysis (ESA) BIBREF4, then picks the label with the highest matching score. Dataless classification emphasizes that the representation of labels takes the equally crucial role as the representation learning of text. Then this idea was further developed in BIBREF5, BIBREF6, BIBREF7, BIBREF8, BIBREF9.

With the prevalence of word embeddings, more and more work adopts pretrained word embeddings to represent the meaning of words, so as to provide the models with the knowledge of labels BIBREF10, BIBREF2, BIBREF11, BIBREF12. DBLPYogatamaDLB17 build generative LSTM to generate text given the embedded labels. DBLPRiosK18 use label embedding to attend the text representation in the developing of a multi-label classifier. But they report R@K, so it is unclear whether the system can really predict unseen labels. DBLPXiaZYCY18 study the zero-shot intent detection problem. The learned representations of intents are still the sum of word embeddings. But during testing, the intent space includes only new intents; seen intents are not covered. All of these studies can only meet the definition in Definition-Restrictive, so they do not really generalize to open aspects of $\textsc {0shot-tc}$.

JiangqngGuo enrich the embedding representations by incorporating class descriptions, class hierarchy, and the word-to-label paths in ConceptNet. DBLPMitchellSL18 assume that some natural language explanations about new labels are available. Then those explanations are parsed into formal constraints which are further combined with unlabeled data to yield
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-4eb0254991c90faf19751aa385fd8f4f7d7fb454d614712506bad678b98aa7e2

Passage ID: `qasper-passage-v1-4eb0254991c90faf19751aa385fd8f4f7d7fb454d614712506bad678b98aa7e2`; retrieval score: 4.0807596559865855.

Word count: 250.

```text
Regarding this label-fully-unseen evaluation, apart from our entailment models and three unsupervised baselines “Majority”, “Word2Vec” and “ESA”, we also report the following baseline:

Wikipedia-based: We train a binary classifier based on BERT on a dataset collected from Wikipedia. Wikipedia is a corpus of general purpose, without targeting any specific $\textsc {0shot-tc}$ task. Collecting categorized articles from Wikipedia is popular way of creating training data for text categorization, such as BIBREF13. More specifically, we collected 100K articles along with their categories in the bottom of each article. For each article, apart from its attached positive categories, we randomly sample three negative categories. Then each article and its positive/negative categories act as training pairs for the binary classifier.

We notice “Wikipedia-based” training indeed contributes a lot for the topic detection task; however, its performances on emotion and situation detection problems are far from satisfactory. We believe this is mainly because the Yahoo-based topic categorization task is much closer to the Wikipedia-based topic categorization task; emotion and situation categorizations, however, are relatively further.

Our entailment models, pretrained on MNLI/FEVER/RTE respectively, perform more robust on the three $\textsc {0shot-tc}$ aspects (except for the RTE on emotion). Recall that they are not trained on any text classification data, and never know the domain and the aspects in the test. This clearly shows the great promise of developing textual entailment models for $\textsc {0shot-tc}$. Our ensemble approach further boosts the performances on all three tasks.

An interesting phenomenon, comparing the label-partially-unseen results in Table TABREF30 and
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-65983def2a52825341b2df28411cf266fbc954edb8b3fa720d0eef291df2dbf6

Passage ID: `qasper-passage-v1-65983def2a52825341b2df28411cf266fbc954edb8b3fa720d0eef291df2dbf6`; retrieval score: 3.69389690041561.

Word count: 250.

```text
In Table TABREF24, we listed examples for converting class names into hypotheses. In this work, we only tried to make use of the class names and their definitions in WordNet. Table TABREF33 lists the fine-grained performance of three ways of generating hypotheses: “word”, “definition”, and “combination” (i.e., word&definition).

This table indicates that: i) Definition alone usually does not work well in any of the three tasks, no matter which pretrained entailment model is used; ii) Whether “word” alone or “word&definition” works better depends on the specific task and the pretrained entailment model. For example, the pretrained MNLI model prefers “word&definition” in both “emotion” and “situation” detection tasks. However, the other two entailment models (RTE and FEVER) mostly prefer “word”. iii) Since it is unrealistic to adopt only one entailment model, such as from {RTE, FEVER, MNLI}, for any open $\textsc {0shot-tc}$ problem, an ensemble system should be preferred. However, the concrete implementation of the ensemble system also influences the strengths of different hypothesis generation approaches. In this work, our ensemble method reaches the top performance when combining the “word” and “definition”. More ensemble systems and hypothesis generation paradigms need to be studied in the future.

To better understand the impact of generated hypotheses, we dive into the performance of each labels, taking “situation detection” as an example. Figure FIGREF47 illustrates the separate F1 scores for each situation class, predicted by the ensemble model for label-fully-unseen setup. This enables us to check in detail how easily the constructed hypotheses can be
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-35b03eea978a6558a087f7b4d7ff83d083c1e797686a00cd40f074ef3566a767

Passage ID: `qasper-passage-v1-35b03eea978a6558a087f7b4d7ff83d083c1e797686a00cd40f074ef3566a767`; retrieval score: 3.0582401786206797.

Word count: 146.

```text
aspects in the test. This clearly shows the great promise of developing textual entailment models for $\textsc {0shot-tc}$. Our ensemble approach further boosts the performances on all three tasks.

An interesting phenomenon, comparing the label-partially-unseen results in Table TABREF30 and the label-fully-unseen results in Table TABREF32, is that the pretrained entailment models work in this order for label-fully-unseen case: RTE $>$ FEVER $>$MNLI; on the contrary, if we fine-tune them on the label-partially-unseen case, the MNLI-based model performs best. This could be due to a possibility that, on one hand, the constructed situation entailment dataset is closer to the RTE dataset than to the MNLI dataset, so an RTE-based model can generalize well to situation data, but, on the other hand, it could also be more likely to over-fit the training set of “situation” during fine-tuning. A deeper exploration of this is left as future work.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-5739e68ccaab20238eaf45fa190cb48454510156f49188bfe99499a61bd870f7

Passage ID: `qasper-passage-v1-5739e68ccaab20238eaf45fa190cb48454510156f49188bfe99499a61bd870f7`; retrieval score: 3.033624123699149.

Word count: 230.

```text
The results of label-partially-unseen are listed in Table TABREF30. “ESA” performs slightly worse than “Word2Vec” in topic detection, mainly because the label names, i.e., topics such as “sports”, are closer than some keywords such as “basketball” in Word2Vec space. However, “ESA” is clearly better than “Word2Vec” in situation detection; this should be mainly due to the fact that the label names (e.g., “shelter”, “evaculation”, etc.) can hardly find close words in the text by Word2Vec embeddings. Quite the contrary, “ESA” is easier to make a class such as “shelter” closer to some keywords like “earthquake”. Unfortunately, both Word2Vec and ESA work poorly for emotion detection problem. We suspect that emotion detection requires more entailment capability. For example, the text snippet “when my brother was very late in arriving home from work”, its gold emotion “fear” requires some common-knowledge inference, rather than just word semantic matching through Word2Vec and ESA.

The supervised method “Binary-BERT” is indeed strong in learning the seen-label-specific models – this is why it predicts very well for seen classes while performing much worse for unseen classes.

Our entailment models, especially the one pretrained on MNLI, generally get competitive performance with the “Binary-BERT” for seen (slightly worse on “topic” and “emotion” while clearly better on “situation”) and improve the performance regarding unseen by large margins. At this stage, fine-tuning on an MNLI-based pretrained entailment model seems more powerful.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1126.

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

#### Rank 1: qasper-passage-v1-a15257942ca7bfb6e3abf01bce724ba22e620f450d95a2a54e39b2ced81e11bc

Passage ID: `qasper-passage-v1-a15257942ca7bfb6e3abf01bce724ba22e620f450d95a2a54e39b2ced81e11bc`; retrieval score: 9.811460760264659.

Word count: 214.

```text
Table TABREF19 presents CTC based results for the Librispeech dataset, without data augmentation. Our baseline is a 24 layer Transformer network trained with CTC. For the proposed method, we varied the number and placement of iterated loss and the feature re-presentation. The next three results show the effect of using CTC multiple times. We see 12 and 8% relative improvements for test-clean and test-other. Adding feature re-presentation gives a further boost, with net 20 and 18% relative improvements over the baseline.

Table TABREF20 shows results for Librispeech with SpecAugment. We test both CTC and CE/hybrid systems. There are consistent gains first from iterated loss, and then from multiple feature presentation. We also run additional CTC experiments with 36 layers Transformer (total parameters $\pm $120 millions). The baseline with 36 layers has the same performance with 24 layers, but by adding the proposed methods, the 36 layer performance improved to give the best results. This shows that our proposed methods can improve even very deep models.

As shown in Table TABREF21, the proposed methods also provide large performance improvements on the curated video set, up to 13% with CTC, and up to 9% with the hybrid model. We also observe moderate gains of between 3.2 and 8% relative on the clean and noisy video sets.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-51ad10f815d5b6de4b20dcd334dd2eef96a5c59965c3a8a38b704a03f4876604

Passage ID: `qasper-passage-v1-51ad10f815d5b6de4b20dcd334dd2eef96a5c59965c3a8a38b704a03f4876604`; retrieval score: 7.460349515721701.

Word count: 222.

```text
In recent years, Transformer models have become an active research topic in speech processing. The key features of Transformer networks is self-attention, which produces comparable or better performance to LSTMs when used for encoder-decoder based ASR BIBREF23, as well as when trained with CTC BIBREF9. Speech-Transformers BIBREF24 also produce comparable performance to the LSTM-based attention model, but with higher training speed in a single GPU. Abdelrahman et al.BIBREF8 integrates a convolution layer to capture audio context and reduces WER in Librispeech.

The use of an objective function in intermediate layers has been found useful in several previous works such as image classification BIBREF25 and language modeling BIBREF26. In BIBREF27, the authors did pre-training with an RNN-T based model by using a hierarchical CTC criterion with different target units. In this paper, we don't need additional types of target unit, instead we just use same tokenization and targets for both intermediate and final losses.

The application of the objective function to intermediate layers is also similar in spirit to the use of KL-divergence in BIBREF28, which estimates output posteriors at an intermediate layer and regularizes them towards the distributions at the final layer. In contrast to this approach, the direct application of the objective function does not require the network to have a good output distribution before the new gradient contribution is meaningful.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-2837a0a69ccdcd093c2a2584b9913e8291570f176c9b3651645695192269b9c8

Passage ID: `qasper-passage-v1-2837a0a69ccdcd093c2a2584b9913e8291570f176c9b3651645695192269b9c8`; retrieval score: 6.830732357137342.

Word count: 107.

```text
In this section, we present our proposal for allowing the network to (re)-consider the input features in the light of intermediate processing. We do this by again deploying a self-attention mechanism to combine the information present in the original features with the information available in the activations of an intermediate layer. As described earlier, we calculate the output posteriors and auxiliary loss at the intermediate layer as well. The overall architecture is illustrated in Figure FIGREF6. Here, we have used a 24 layer network, with feature re-presentation after the 12th layer.

In the following subsections, we provide detail on the feature re-presentation mechanism, and iterated loss calculation.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-56eefe94e6b775241b19412cb1eb54b5d1877ff88da247f8d4d263953da9f99f

Passage ID: `qasper-passage-v1-56eefe94e6b775241b19412cb1eb54b5d1877ff88da247f8d4d263953da9f99f`; retrieval score: 6.0424425038895695.

Word count: 97.

```text
In this paper, we have proposed a method for re-processing the input features in light of the information available at an intermediate network layer. We do this in the context of deep transformer networks, via a self-attention mechanism on both features and hidden states representation. To encourage meaningful partial results, we calculate the objective function at intermediate layers of the network as well as the output layer. This improves performance in and of itself, and when combined with feature re-presentation we observe consistent relative improvements of 10 - 20% for Librispeech and 3.2 - 13% for videos.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-7e918b42959d7e586f6b0b34485d17529bf6008b1d85d1885b8f97c5fa4c5731

Passage ID: `qasper-passage-v1-7e918b42959d7e586f6b0b34485d17529bf6008b1d85d1885b8f97c5fa4c5731`; retrieval score: 4.415484398771776.

Word count: 212.

```text
in many speech related applications may be found in BIBREF9. Compared to RNNs, Transformers have several advantages, specifically an ability to aggregate information across all the time-steps by using a self-attention mechanism. Unlike RNNs, the hidden representations do not need to be computed sequentially across time, thus enabling significant efficiency improvements via parallelization.

In the context of Transformer module, secondary feature analysis is enabled through an additional mid-network transformer module that has access both to previous-layer activations and the raw features. To implement this model, we apply the objective function several times at the intermediate layers, to encourage the development of phonetically relevant hypotheses. Interestingly, we find that the iterated use of an auxiliary loss in the intermediate layers significantly improves performance by itself, as well as enabling the secondary feature analysis.

This paper makes two main contributions:

We present improvements in the basic training process of deep transformer networks, specifically the iterated use of CTC or CE in intermediate layers, and

We show that an intermediate-layer attention model with access to both previous-layer activations and raw feature inputs can significantly improve performance.

We evaluate our proposed model on Librispeech and a large-scale video dataset. From our experimental results, we observe 10-20% relative improvement on Librispeech and 3.2-11% on the video dataset.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 852.

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

#### Rank 1: qasper-passage-v1-93cd513b7c06785bc5dcdf33bc8d00389d98e9f47b08243aded04ab71823ebeb

Passage ID: `qasper-passage-v1-93cd513b7c06785bc5dcdf33bc8d00389d98e9f47b08243aded04ab71823ebeb`; retrieval score: 11.950951180977734.

Word count: 250.

```text
Ideally the DM's policy would be trained by interacting with real users. Although there are models that support on-line learning BIBREF15 , for the majority of RL algorithms, which require a lot of interactions, this is impractical. Furthermore, a set of users needs to be recruited every time a policy is trained. This makes common practices such as hyper-parameter optimization prohibitively expensive. Thus, it is natural to try to learn from a dataset which needs to be recorded only once, but can be used over and over again.

A problem with learning directly from recorded dialogue corpora is that the state space that was visited during the collection of the data is limited; the size of the recorded corpus usually falls short of the requirements for training a statistical DM. However, even if the size of the corpus is large enough the optimal dialogue strategy is likely not to be contained within it.

A solution is to transform the static corpus into a dynamic tool: a user simulator. The user simulator (US) is trained on a dialogue corpus to learn what responses a real user would provide in a given dialogue context. The US is trained using supervised learning since the aim is for it to learn typical user behaviour. For the DM, however, we want optimal behaviour which is why supervised learning cannot be used. By interacting with the SDS, the trained US can be used to train the DM's policy. The DM's policy is optimised using the feedback
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-8cef6a4613071e1c335ce93532110865f6ef09ecb67e6bdd9bc8d0ca8e31ceaf

Passage ID: `qasper-passage-v1-8cef6a4613071e1c335ce93532110865f6ef09ecb67e6bdd9bc8d0ca8e31ceaf`; retrieval score: 4.900015191764757.

Word count: 162.

```text
A Task-Oriented SDS is typically designed according to a structured ontology, which defines what the system can talk about. In a system recommending restaurants the ontology defines those attributes of a restaurant that the user can choose, called informable slots (e.g. different food types, areas and price ranges), the attributes that the user can request, called requestable slots (e.g. phone number or address) and the restaurants that it has data about. An attribute is referred to as a slot and has a corresponding value. Together these are referred to as a slot-value pair (e.g. area=north).

Using RL the DM is trained to act such that is maximises the cumulative future reward. The process by which the DM chooses its next action is called its policy. A typical approach to defining the reward function for a task-oriented SDS is to apply a small per-turn penalty to encourage short dialogues and to give a large positive reward at the end of each successful interaction.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-254f6e36c30f23271d127eb3a7d74c5c748421c164bece49f99a10f8d5ae3f83

Passage ID: `qasper-passage-v1-254f6e36c30f23271d127eb3a7d74c5c748421c164bece49f99a10f8d5ae3f83`; retrieval score: 4.592743219045223.

Word count: 250.

```text
For the DM, however, we want optimal behaviour which is why supervised learning cannot be used. By interacting with the SDS, the trained US can be used to train the DM's policy. The DM's policy is optimised using the feedback given by either the user simulator or a separate evaluator. Any number of dialogues can be generated using the US and dialogue strategies that are not in the recorded corpus can be explored.

Most user-simulators work on the level of user semantics. These usually consist of a user dialogue act (e.g. inform, or request) and a corresponding slot-value pair. The first statistical user simulator BIBREF16 used a simple bi-gram model INLINEFORM0 to predict the next user act INLINEFORM1 given the last system act INLINEFORM2 . It has the advantage of being purely probabilistic and domain-independent. However, it does not take the full dialogue history into account and is not conditioned on a goal, leading to incoherent user behaviour throughout a dialogue. BIBREF17 , BIBREF18 attempted to overcome goal inconsistency by proposing a graph-based model. However, developing the graph structure requires extensive domain-specific knowledge. BIBREF19 combined features from Sheffler and Young's work with Eckert's Model, by conditioning a set of probabilities on an explicit representation of the user goal and memory. A Markov Model is also used by BIBREF20 . It uses a large feature vector to describe the user's current state, which helps to compensate for the Markov assumption. However, the model is not conditioned on any goal. Therefore, it
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-186f792e2c004e9e5963b5a88f5470b0984e40ac0b9fb9fb60ed25534d9c78c5

Passage ID: `qasper-passage-v1-186f792e2c004e9e5963b5a88f5470b0984e40ac0b9fb9fb60ed25534d9c78c5`; retrieval score: 4.466419389560938.

Word count: 250.

```text
Spoken Dialogue Systems (SDS) allow human-computer interaction using natural speech. Task-oriented dialogue systems, the focus of this work, help users achieve goals such as finding restaurants or booking flights BIBREF0 .

Teaching a system how to respond appropriately in a task-oriented setting is non-trivial. In state-of-the-art systems this dialogue management task is often formulated as a reinforcement learning (RL) problem BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 . In this framework, the system learns by a trial and error process governed by a reward function. User Simulators can be used to train the policy of a dialogue manager (DM) without real user interactions. Furthermore, they allow an unlimited number of dialogues to be created with each dialogue being faster than a dialogue with a human.

In this paper the Neural User Simulator (NUS) is introduced which outputs natural language and whose behaviour is learned from a corpus. The main component, inspired by BIBREF4 , consists of a feature extractor and a neural network based sequence-to-sequence model BIBREF5 . The sequence-to-sequence model consists of a recurrent neural network (RNN) encoder that encodes the dialogue history and a decoder RNN which outputs natural language. Furthermore, the NUS generates its own goal and possibly changes it during a dialogue. This allows the model to be deployed for training more sophisticated DM policies. To achieve this, a method is proposed that transforms the goal-labels of the used dataset (DSTC2) into labels whose behaviour can be replicated during deployment.

The NUS is trained on dialogues
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1805.06966:0:2` | full | 0:774 |

#### Rank 5: qasper-passage-v1-f4dee1babba8cf668e3cc6dab45accb2877efc592728d5910231e815690669e9

Passage ID: `qasper-passage-v1-f4dee1babba8cf668e3cc6dab45accb2877efc592728d5910231e815690669e9`; retrieval score: 4.330405819089753.

Word count: 79.

```text
Table TABREF19 . After training for 1000 dialogues, the average SR of the policies trained on the NUS when tested on the ABUS was 97.3% in comparison to 94.0% after 4000 dialogues. This behaviour was observed for all five seeds, which indicates that the policy indeed overfits to the NUS. For the policies trained with the ABUS this was not observed. This could indicate that the policy can learn to exploit some of the shortcomings of the trained NUS.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 991.

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

#### Rank 1: qasper-passage-v1-09bd2d0933c493ceafbec18facb59ce4e7b3041a38c1c2d56d3800dc7ac4135f

Passage ID: `qasper-passage-v1-09bd2d0933c493ceafbec18facb59ce4e7b3041a38c1c2d56d3800dc7ac4135f`; retrieval score: 9.17127131936913.

Word count: 119.

```text
The fixed training condition is used to build our speaker recognition system. Only conversational telephone speech data from datasets released through the linguistic data consortium (LDC) have been used, including NIST SRE 2004-2010 and the Switchboard corpora (Switchboard Cellular Parts I and II, Switchboard2 Phase I,II and III) for different steps of system training. A more detailed description of the data used in the system training is presented in Table TABREF1 . We have also included the unlabelled set of 2472 telephone calls from both minor (Cebuano and Mandarin) and major (Tagalog and Cantonese) languages provided by NIST in the system training. We will indicate when and how we used this set in the training in the following sections.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-9be3b3822a7bee2d07e73061637754ab743a611111d540b748df8b00ab469698

Passage ID: `qasper-passage-v1-9be3b3822a7bee2d07e73061637754ab743a611111d540b748df8b00ab469698`; retrieval score: 7.470383065430825.

Word count: 230.

```text
This section reports on the CPU execution time (single threaded), and the amount of memory used to process a single trial, which includes the time for creating models from the enrolment data and the time needed for processing the test segments. The analysis was performed on an Intel(R) Xeon(R) CPU E5-2670 2.60GHz. The results are shown in Table TABREF27 . We used the time command in Unix to report these results. The user time is the actual CPU time used in executing the process (single thread). The real time is the wall clock time (the elapsed time including time slices used by other processes and the time the process spends blocked). The system time is also the amount of CPU time spent in the kernel within the process. We have also reported the memory allocated for each stage of execution. The most computationally intensive stage is the extraction of i-vectors (both MFCC- and PLP-based i-vectors), which also depends on the duration of the segments. For enrolment, we have reported the time required to extract a model from a segment with a duration of 140 seconds and speech duration of 60 seconds. The time and memory required for front-end processing are negligible compared to the i-vector extraction stage, since they only include matrix operations. The time required for our SAD is also reported which increases linearly with the duration of segment.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-95cae1ca50503fdba75930571c0a7e48c24860293fc98a2790392306d5370694

Passage ID: `qasper-passage-v1-95cae1ca50503fdba75930571c0a7e48c24860293fc98a2790392306d5370694`; retrieval score: 6.479054878800225.

Word count: 119.

```text
performance in text-independent speaker recognition for English data BIBREF6 , BIBREF7 , failed to provide even comparable recognition performance to the traditional GMM. Therefore, we concentrated on the cepstral based GMM/i-vector system.

We outline in this paper the Intelligent Voice system, techniques and results obtained on the SRE 2016 development set that will mirror the evaluation condition as well as the timing report. Section SECREF2 describes the data used for the system training. The front-end and back-end processing of the system are presented in Sections SECREF3 and SECREF4 respectively. In Section SECREF5 , we describe experimental evaluation of the system on the SRE 2016 development set. Finally, we present a timing analysis of the system in Section SECREF6 .
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-5ca3deb23f82a8c84e3c0e9e6f61dbd2b8e5b84ce86ee2b54e89c11f80057d14

Passage ID: `qasper-passage-v1-5ca3deb23f82a8c84e3c0e9e6f61dbd2b8e5b84ce86ee2b54e89c11f80057d14`; retrieval score: 6.230128464322917.

Word count: 208.

```text
Since the introduction of i-vectors in BIBREF0 , the speaker recognition community has seen a significant increase in recognition performance. i-Vectors are low-dimensional representations of Baum-Welch statistics obtained with respect to a GMM, referred to as universal background model (UBM), in a single subspace which includes all characteristics of speaker and inter-session variability, named total variability matrix BIBREF0 . We trained on each acoustic feature a full covariance, gender-independent UBM model with 2048 Gaussians followed by a 600-dimensional i-vector extractor to establish our MFCC- and PLP-based i-vector systems. The unlabeled set of development data was used in the training of both the UBM and the i-vector extractor. The open-source Kaldi software has been used for all these processing steps BIBREF12 .

It has been shown that successive acoustic observation vectors tend to be highly correlated. This may be problematic for maximum a posteriori (MAP) estimation of i-vectors. To investigating this issue, scaling the zero and first order Baum-Welch statistics before presenting them to the i-vector extractor has been proposed. It turns out that a scale factor of 0.33 gives a slight edge, resulting in a better decision cost function BIBREF13 . This scaling factor has been performed in training the i-vector extractor as well as in the testing.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1611.00514:5:0` | full | 0:835 |

#### Rank 5: qasper-passage-v1-50aee7f3278f045e68c20476d9a0a66108348cbefc832d43218137b73f6054da

Passage ID: `qasper-passage-v1-50aee7f3278f045e68c20476d9a0a66108348cbefc832d43218137b73f6054da`; retrieval score: 5.846973409349171.

Word count: 136.

```text
fusion, however, PLP seems not to be adversely affected. The effect of using QMF is also investigated in scenario D. Finally in scenario E, we can see the major improvement obtained through the use of the domain adaptation technique explained in Section SECREF16 . For our secondary submission, we incorporated a disjoint portion of the labelled development set (10 out of 20 speakers) in either LN-LDA and in-domain PLDA training. We evaluated the system on almost 6k out of 24k trials from the other portion to avoid any over-fitting, particularly important for the domain adaptation technique. This resulted in a relative improvement of 11% compared to the primary system in terms of the primary metric. However, the results can be misleading, since the recording condition may be the same for all speakers in the development set.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 812.

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

#### Rank 1: qasper-passage-v1-d0c0d7dfa900f2c5fe6a64569ac6cf3e47aeef7b600ef378d4322de9ea9d0f9a

Passage ID: `qasper-passage-v1-d0c0d7dfa900f2c5fe6a64569ac6cf3e47aeef7b600ef378d4322de9ea9d0f9a`; retrieval score: 5.34557455674409.

Word count: 250.

```text
nonparametric extension of the hidden Markov model (HMM) BIBREF182 that allows performing inference on an infinite number of states. To further increase the representational power for modeling discrete time series data, they develop a nonparametric extension that combines the best of the two models, and lets the two parameters M and K be learned from data Each step in the new iHMM-iFHMM generative process is performed in two phases: (i) the latent feature variables from the iFHMM framework are sampled using the mIBP mechanism; and (ii) the features sampled so far, which become observable during this second phase, are used in an adapted version of the beam sampling algorithm BIBREF183 to infer the clustering components (i.e., latent events).

They report results in terms of recall (R), precision (P), and F-score (F) by employing the mention-based B3 metric BIBREF184 , the entity-based CEAF metric BIBREF185 , and the pairwise F1 (PW) metric. Their experiments for show that both of these models work well when the feature and cluster numbers are treated as free parameters, and the selection of feature values is performed automatically.

BIBREF167 argue that events represent complex phenomena and can therefore co-refer fully, being identical, like other researchers have discussed, or co-refer partially, being quasi-identical or only partially identical. Two event mentions fully co-refer if their activity, event or state representation is identical in terms of all features used (e.g., agent, location or time). Two event mentions are quasi-identical if they partially co-refer, i.e., most features are the same,
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-9918dc3a7ff991a7ab68befdac4291416236d116edcaf5b9ba0a91459468bdd6

Passage ID: `qasper-passage-v1-9918dc3a7ff991a7ab68befdac4291416236d116edcaf5b9ba0a91459468bdd6`; retrieval score: 5.122263278350643.

Word count: 250.

```text
With the explosive expansion of the Internet during the past twenty years, the volume of socially generated text has skyrocketed. Socially generated text includes blogs and microblogs. For example, Twitter, started in 2006, has become a social phenomenon. It allows individuals with accounts to post short messages that are up to 140 characters long. Currently, more than 340 million tweets are sent out every day. While a majority of posts are conversational or not particularly meaningful, about 3.6% of the posts concern topics of mainstream news. Twitter has been credited with providing the most current news about many important events before traditional media, such as the attacks in Mumbai in November 2008. Twitter also played a prominent role in the unfolding of the troubles in Iran in 2009 subsequent to a disputed election, and the so-called Twitter Revolutions in Tunisia and Egypt in 2010-11.

Most early work on event extraction of information from documents found on the Internet has focussed on news articles BIBREF225 , BIBREF226 , BIBREF227 . However, as noted earlier, social networking sites such as Twitter and Facebook have become important complimentary sources of such information. Individual tweets, like SMS messages, are usually short and self-contained and therefore are not composed of complex discourse structures as is the case with texts containing narratives. However, extracting structured representation of events from short or informal texts is also challenging because most tweets are about mundane things, without any news value and of interest only to the immediate social network.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-98787cb4fdc2caaa61949fdc342f6b7ef63350d14d3bbf81fb180a5a395e09f0

Passage ID: `qasper-passage-v1-98787cb4fdc2caaa61949fdc342f6b7ef63350d14d3bbf81fb180a5a395e09f0`; retrieval score: 5.068342766134567.

Word count: 250.

```text
Many authors in linguistics have delved deeper into the nature of event classes and have tried to come up with features or characteristics that can be used to identify whether something (verb or a clause) belongs to a particular event class or not. These features or characteristics are necessary to describe the structure of events in a theoretical sense. Description of event structure usually refers to the actual words used (lexical features or characteristics) and also the structure of clause or sentence (syntactic features or characteristics). Identification of such features may be described as finding parameters of event types or parameterization of event types.

A lot of the work on parameterization of event types/classes use the classes espoused by Vendler. These include BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 , BIBREF13 , BIBREF14 , BIBREF15 and others. We will only briefly touch upon such work in this paper. Our objective is to impress upon the reader that identification of features of event classes is considered an important task by linguists.

For example, BIBREF9 describes Vendler's classes with two binary features or parameters: continuousness: whether an event has duration, and boundedness: whether an event has a (natural) terminal point or endpoint. Using these two features, the four Vendler classes can be parameterized as follows.

: -bounded, -continuous

: -bounded, +continuous

: +bounded, -continuous

: +bounded, +continuous

BIBREF12 , BIBREF13 introduce the notion of countability while discussing event classes. This is similar to the mass-count opposition in nouns. Terminating events can be
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-3406da865e90d4ad15900f2b87043c16eedf3c17e649f751f39c652216e4e114

Passage ID: `qasper-passage-v1-3406da865e90d4ad15900f2b87043c16eedf3c17e649f751f39c652216e4e114`; retrieval score: 5.065750839024368.

Word count: 250.

```text
stated in the TimeML specification. Evita does not directly identify event participants, but can work with named entity taggers to link arguments to events.

Evita breaks down the event recognition problem to a number of sub-tasks. Evita preprocesses the input text using the Alembic Workbench POS tagger, lemmatizer to find lexical stems, and chunkier to obtain phrase chunks, verbal, nominal and adjectival, the three that are commonly used as event referring expressions BIBREF142 . For each subtask after pre-processing, it combines linguistic- and statistically-based knowledge. Linguistic knowledge is used in local and limited contexts such as verb phrases and to extract morphological information. Statistical knowledge is used to disambiguate nominal events. The sub-tasks in event recognition in Evita are: determination of event candidates and then the events, identification of grammatical features of events, additional clustering of event chunks for event detection and grammatical feature identification in some situations.

For event identification, Evita looks at the lexical items tagged by the preprocessing step. It uses different strategies for identifying events in the three categories: verbs, nouns and adjectives. For identifying events in a verbal chunk, Evita performs lexical look-up and limited contextual parsing in order to exclude weak stative predicates such as be and generics such as verbs with bare plural subjects. Identifying events expressed by nouns involves a phase of lexical look-up and disambiguation using WordNet, and by mapping events SemCor and TimeBank 1.2 to WordNet synsets. Evita consults 25 subtrees from WordNet where all the synsets denote events. One
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-9cd6d3c32292040224f348aaffae25a8893fb5e806d71b4d2a033f5a3f9d400a

Passage ID: `qasper-passage-v1-9cd6d3c32292040224f348aaffae25a8893fb5e806d71b4d2a033f5a3f9d400a`; retrieval score: 5.034724190185791.

Word count: 250.

```text
tagger, and dictionaries of event terms gathered from WordNet BIBREF121 . Once a large number of events have been extracted by this CRF learner, TwiCal categorizes these events into types using an unsupervised approach based on latent variable models, inspired by work on modeling selectional preferences BIBREF230 , BIBREF231 , BIBREF232 , BIBREF233 and unsupervised information extraction BIBREF234 , BIBREF225 , BIBREF235 . This automatic discovery of event types is similar to topic modeling, where one automatically identifies the extant topics in a corpus of text documents. The automatically discovered types (topics) are quickly inspected by a human effort to filter out incoherent ones, and the rest are annotated with informative labels. Examples of event types discovered along with top event phrases and top entities are given in Table 12 . The resulting set of types are applied to categorize millions of extracted events without the use of any manually annotated examples. For inference, the system uses collapsed Gibbs sampling BIBREF236 and prediction is performed using a streaming approach to inference BIBREF237 . To resolve temporal expressions, TwiCal uses TempEx BIBREF238 , which takes as input a reference date, some text and POS tags, and marks temporal expressions with unambiguous calendar references. Finally, the system measures the strength of association between each named entity and date based on the number of tweets they co-occur in, in order to determine if the event is significant. Examples of events extracted by TwiCal are given in Table 13 . Each event is a
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 1250.

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

#### Rank 1: qasper-passage-v1-33e8ddcf6d50de9070aaa477d4789dfa2fcc659f58f1c558fcd0829ace63a204

Passage ID: `qasper-passage-v1-33e8ddcf6d50de9070aaa477d4789dfa2fcc659f58f1c558fcd0829ace63a204`; retrieval score: 5.8639108357612315.

Word count: 161.

```text
have rich morphology, be it fusional, agglutinative, polysynthetic, or a mixture thereof. As Natural Language Processing (NLP) keeps expanding its frontiers to encompass more and more languages, modeling of the grammatical functions that guide language generation is of utmost importance. It follows, then, that the next crucial step for expanding NLP research on endangered languages is creating benchmarks for standard NLP tasks in such languages.

With this work we take a small first step towards this direction. We present a resource that allows for benchmarking two NLP tasks in San Juan Quiahije Chatino, an endangered language spoken in southern Mexico: morphological analysis and morphological inflection, with a focus on the verb morphology of the language.

We first briefly discuss the Chatino language and the intricacies of its verb morphology (§SECREF2), then describe the resource (§SECREF3), and finally present baseline results on both the morphological analysis and the inflection tasks using state-of-the-art neural models (§SECREF4). We make our resource publicly available online.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-051eb62a88e3da69ea725e6dfdbe7e34d0711eb4aa2242899e3725f1826f65fa

Passage ID: `qasper-passage-v1-051eb62a88e3da69ea725e6dfdbe7e34d0711eb4aa2242899e3725f1826f65fa`; retrieval score: 5.673556598713484.

Word count: 84.

```text
Chatino is a group of languages spoken in Oaxaca, Mexico. Together with the Zapotec language group, the Chatino languages form the Zapotecan branch of the Otomanguean language family. There are three main Chatino languages: Zenzontepec Chatino (ZEN, ISO 639-2 code czn), Tataltepec Chatino (TAT, cta), and Eastern Chatino (ISO 639-2 ctp, cya, ctz, and cly) (E.Cruz 2011 and Campbell 2011). San Juan Quiahije Chatino (SJQ), the language of the focus of this study, belongs to Eastern Chatino, and is used by about 3000 speakers.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-3f07f7931cd82ee0c07089d3b7822af983f639ff9d0ea39c5ab49ee7f2236add

Passage ID: `qasper-passage-v1-3f07f7931cd82ee0c07089d3b7822af983f639ff9d0ea39c5ab49ee7f2236add`; retrieval score: 4.312642512327558.

Word count: 99.

```text
Eastern Chatino languages , including SJQ Chatino, are intensively tonal BIBREF2, BIBREF3. Tones mark both lexical and grammatical distinctions in Eastern Chatino languages.

In SJQ Chatino, there are eleven tones. Three different systems for representing tone distinctions are employed in the literature: the S-H-M-L system of BIBREF2; the numeral system of BIBREF4; and the alphabetic system of BIBREF3. The correspondences among these three systems are given in Table . For present purposes, we will use numeral representations of the second sort. The number 1 represents a high pitch, 4 represents a low pitch, and double digits represent contour tones.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-094f41c6fc095964636a38db57f269c1f5706f6b45fa544b52e04808a11691d2

Passage ID: `qasper-passage-v1-094f41c6fc095964636a38db57f269c1f5706f6b45fa544b52e04808a11691d2`; retrieval score: 3.791615848882489.

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

#### Rank 5: qasper-passage-v1-39437f40f3061e86353627d369088e63d8db0cc8008c2869c7b04896b58d2cb5

Passage ID: `qasper-passage-v1-39437f40f3061e86353627d369088e63d8db0cc8008c2869c7b04896b58d2cb5`; retrieval score: 3.122930849162232.

Word count: 219.

```text
SJQ Chatino verb inflection distinguishes four aspect/mood categories: completive (`I did'), progressive (`I am doing'), habitual (`I habitually do') and potential (`I might do'). In each of these categories, verbs inflect for three persons (first, second, third) and two numbers (singular, plural) and distinguish inclusive and exclusive categories of the first person plural (`we including you' vs `we excluding you'). Verbs can be classified into dozens of different conjugation classes. Each conjugation class involves its own tone pattern; each tone pattern is based on a series of three person/number (PN) triplets. A PN triplet [X, Y, Z] consists of three tones: tone X is employed in the third person singular as well as in all plural forms; tone Y is employed in the second person singular, and tone Z, in the third person singular. Thus, a verb's membership in a particular conjugation class entails the assignment of one tone triplet to completive forms, another to progressive forms, and a third to habitual and potential forms. The paradigm of the verb lyu1 `fall' in Table illustrates: the conjugation class to which this verb belongs entails the assignment of the triplet [1, 42, 20] to the completive, [1, 42, 32] to the progressive, and [20, 42, 32] to the habitual and potential. Verbs in other conjugation classes exhibit other triplet series.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 807.

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
