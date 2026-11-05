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

#### Rank 1: qasper-passage-v1-6ac424154ba16933bc01a910453fbc2c2a8006eb35b2d5c436e8a977f4f717a8

Passage ID: `qasper-passage-v1-6ac424154ba16933bc01a910453fbc2c2a8006eb35b2d5c436e8a977f4f717a8`; retrieval score: 5.875165552753231.

Word count: 200.

```text
Methods for machine translations have been studied for years, and at the same time algorithms to generate word embeddings are becoming more and more accurate. Still, there is a lot of research aiming at unifying word embeddings across multiple languages. In this experience we try a technique for machine translation that relates word embeddings between two different languages. Based on the literature we found that it is possible to infer missing dictionary entries using distributed representations of words and phrases. One way of doing it is to create a linear mapping between the two vector spaces of two different languages. In order to achieve this, we first built two dictionaries of the two different languages. Next, we learned a function that projects the first vector space to the second one. In this way, we are able to translate every word belonging to the first language into the second one. Once we obtain the translated word embedding, we output the most similar word vector as the translation. The word embeddings were learnt using the Skip Gram method proposed by (Mikolov et al., 2013a). An example of how the method would work is reported in figure 1 and figure 2. After creating
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-d133d88f772e0f24df882cbf1f6ac7365e98ddaceb52cf7b799d98b9c1262ea9

Passage ID: `qasper-passage-v1-d133d88f772e0f24df882cbf1f6ac7365e98ddaceb52cf7b799d98b9c1262ea9`; retrieval score: 5.76077576041816.

Word count: 103.

```text
In recent years, various models for learning cross-lingual representations have been proposed. Two main broad categories with some related papers are identified here:

Monolingual mapping: In this approach, models are trained using word embeddings from a monolingual corpora. Then, an objective function is used to minimize a linear mapping that enable them to map unknown words from the source language to the target language.

Pseudo-cross-lingual: In this case we create a pseudo-cross-lingual corpus by mixing contexts of different languages. We then train an off-the-shelf word embedding model on the created corpus. Ideally the cross-lingual contexts allow the learned representations to capture cross-lingual relations.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-135283cf463602542c8fd7b01f944d6eeff6c3738e07f719254dea86a5497c95

Passage ID: `qasper-passage-v1-135283cf463602542c8fd7b01f944d6eeff6c3738e07f719254dea86a5497c95`; retrieval score: 5.547781038931242.

Word count: 131.

```text
It was recently shown that the distributed representations of words capture surprisingly many linguistic regularities, and that there are many types of similarities among words that can be expressed as linear translations (Mikolov et al., 2013c). In the Skip-gram model, the training objective is to learn word vector representations that are good at predicting its context in the same sentence (Mikolov et al., 2013a). The objective function that skip gram tries to minimize is the following:

Where N represents the total number of words in a sentence, P the probability of a word at the position i+j to belong to the sentence, with respect to the word i. Ideally, by using this approach we will be able to provide non-trivial translations that will be related to the context of a word.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-450572557433937cf9781fcb93b1da3dac69dfb89ed0cc7c4a8f67e85b3c8adf

Passage ID: `qasper-passage-v1-450572557433937cf9781fcb93b1da3dac69dfb89ed0cc7c4a8f67e85b3c8adf`; retrieval score: 3.8449272269218557.

Word count: 175.

```text
Since the word embeddings in a single language are based on the cosine similarity, we realized that through the objective function reported in equation 1 we were losing the property of this similarity. As a result we wanted the dot products to be preserved after the mapping. In order to do that we normalized the vectors $x_i$ and $z_i$.The new objective function looks like:

In order to preserve the dot products after the linear mapping we also had to constrain W to be an orthogonal matrix. In order to orthogonalize the matrix, it's required to solve the following optimization problem:

One can show that this problem can be solved by taking the singular value decomposition (SVD) of W and replacing the singular values to ones. This approximation would only work when the dimensions of the source vector and the target vector are the same, which is the set up we are working with. So finally, the method that we tried for this experience uses normalized vectors, and is reduced by using the cosine similarity function.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-7800321f06616e1b2c1e4f42b0073072c5de311860b3a9d720e179d34838b4c4

Passage ID: `qasper-passage-v1-7800321f06616e1b2c1e4f42b0073072c5de311860b3a9d720e179d34838b4c4`; retrieval score: 3.446583760889055.

Word count: 200.

```text
The process for checking the accuracy of the model consisted of first taking a random subset of the corpus that was not used for training. This subset consists of slightly more common words because the more common words should have more accurate word embeddings. Infrequent words (like websites and serial numbers) would not necessarily have accurate word embeddings that were generated through the word2vec model. The English word embedding was multiplied by the transformation matrix to create the predicted translated word embedding. The cosine similarity was then generated with each translated word embedding stored in the corpus. The 20 words with the highest cosine similarity were then outputted. Then the English word was translated through Google Translate and compared to the 20 outputted translated words. It was considered a match if the translated word was found in this list of 20 similar words. The reason why the translated word was not just compared to the most similar embedding was because each word could have multiple semantic meanings or have different synonyms in the other language. After running this accuracy formulation, results for different languages and objective functions are reported in Table TABREF18. In the table you can see the different
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 809.

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

#### Rank 1: qasper-passage-v1-ce205bac883945d0ebfdfe8cf4ae87b97964b42a94b6ea0f0ba704ef651c4497

Passage ID: `qasper-passage-v1-ce205bac883945d0ebfdfe8cf4ae87b97964b42a94b6ea0f0ba704ef651c4497`; retrieval score: 2.7811380341362195.

Word count: 200.

```text
The focus of this section is on recently published datasets and LID research applicable to the South African context. An in depth survey of algorithms, features, datasets, shared tasks and evaluation methods may be found in BIBREF0.

The datasets for the DSL 2015 & DSL 2017 shared tasks BIBREF1 are often used in LID benchmarks and also available on Kaggle . The DSL datasets, like other LID datasets, consists of text sentences labelled by language. The 2017 dataset, for example, contains 14 languages over 6 language groups with 18000 training samples and 1000 testing samples per language.

The recently published JW300 parallel corpus BIBREF2 covers over 300 languages with around 100 thousand parallel sentences per language pair on average. In South Africa, a multilingual corpus of academic texts produced by university students with different mother tongues is being developed BIBREF3. The WiLI-2018 benchmark dataset BIBREF4 for monolingual written natural language identification includes around 1000 paragraphs of 235 languages. A possibly useful link can also be made BIBREF5 between Native Language Identification (NLI) (determining the native language of the author of a text) and Language Variety Identification (LVI) (classification of different varieties of a single language) which opens up more datasets.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-712fd478957e337b2397153bf81a788a465286234e5d46187ebc49b07f582290

Passage ID: `qasper-passage-v1-712fd478957e337b2397153bf81a788a465286234e5d46187ebc49b07f582290`; retrieval score: 1.4307043082648514.

Word count: 200.

```text
The proposed LID algorithm builds on the work in BIBREF8 and BIBREF26. We apply a naive Bayesian classifier with character (2, 4 & 6)-grams, word unigram and word bigram features with a hierarchical lexicon based classifier.

The naive Bayesian classifier is trained to predict the specific language label of a piece of text, but used to first classify text as belonging to either the Nguni family, the Sotho family, English, Afrikaans, Xitsonga or Tshivenda. The scikit-learn multinomial naive Bayes classifier is used for the implementation with an alpha smoothing value of 0.01 and hashed text features.

The lexicon based classifier is then used to predict the specific language within a language group. For the South African languages this is done for the Nguni and Sotho groups. If the lexicon prediction of the specific language has high confidence then its result is used as the final label else the naive Bayesian classifier's specific language prediction is used as the final result. The lexicon is built over all the data and therefore includes the vocabulary from both the training and testing sets.

The lexicon based classifier is designed to trade higher precision for lower recall. The proposed implementation is considered confident if
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-be21bf4fe1a6a567bf5585ffdfc20d0aa4ceebbcc3a9c5d100033d59b9683743

Passage ID: `qasper-passage-v1-be21bf4fe1a6a567bf5585ffdfc20d0aa4ceebbcc3a9c5d100033d59b9683743`; retrieval score: 1.1002163925509785.

Word count: 79.

```text
used followed by a refinement with learning rate of 0.0001. Only one code modification was applied to return the results from a method that previously just printed to screen. The LID algorithm described in BIBREF8 is also available on GitHub.

The stacked classifier is also tested against the results reported for four other algorithms BIBREF16, BIBREF26, BIBREF24, BIBREF15. All the comparisons are done using the NCHLT BIBREF7, DSL 2015 BIBREF19 and DSL 2017 BIBREF1 datasets discussed in Section SECREF2.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-684ec67c41fe30c68836269f63196692d66606b92c145d9bb46802a47a7ca603

Passage ID: `qasper-passage-v1-684ec67c41fe30c68836269f63196692d66606b92c145d9bb46802a47a7ca603`; retrieval score: 1.0857650569726114.

Word count: 200.

```text
The lexicon is built over all the data and therefore includes the vocabulary from both the training and testing sets.

The lexicon based classifier is designed to trade higher precision for lower recall. The proposed implementation is considered confident if the number of words from the winning language is at least one more than the number of words considered to be from the language scored in second place.

The stacked classifier is tested against three public LID implementations BIBREF17, BIBREF23, BIBREF8. The LID implementation described in BIBREF17 is available on GitHub and is trained and tested according to a post on the fasttext blog. Character (5-6)-gram features with 16 dimensional vectors worked the best. The implementation discussed in BIBREF23 is available from https://github.com/tomkocmi/LanideNN. Following the instructions for an OSX pip install of an old r0.8 release of TensorFlow, the LanideNN code could be executed in Python 3.7.4. Settings were left at their defaults and a learning rate of 0.001 was used followed by a refinement with learning rate of 0.0001. Only one code modification was applied to return the results from a method that previously just printed to screen. The LID algorithm described in BIBREF8 is also available on GitHub.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-eb97a1185ed7f952b3743bae27f77f348aab40c0ba94acc3618e98056a673920

Passage ID: `qasper-passage-v1-eb97a1185ed7f952b3743bae27f77f348aab40c0ba94acc3618e98056a673920`; retrieval score: 1.0729678549303405.

Word count: 200.

```text
naive Bayes classifiers BIBREF12, BIBREF8, BIBREF13, BIBREF14, SVMs BIBREF15 and similar models work very well for doing LID. The DSL 2017 paper BIBREF1, for example, gives an overview of the solutions of all of the teams that competed on the shared task and the winning approach BIBREF16 used an SVM with character n-gram, parts of speech tag features and some other engineered features. The winning approach for DSL 2015 used an ensemble naive Bayes classifier. The fasttext classifier BIBREF17 is perhaps one of the best known efficient 'shallow' text classifiers that have been used for LID .

Multiple papers have proposed hierarchical stacked classifiers (including lexicons) that would for example first classify a piece of text by language group and then by exact language BIBREF18, BIBREF19, BIBREF8, BIBREF0. Some work has also been done on classifying surnames between Tshivenda, Xitsonga and Sepedi BIBREF20. Additionally, data augmentation BIBREF21 and adversarial training BIBREF22 approaches are potentially very useful to reduce the requirement for data.

Researchers have investigated deeper LID models like bidirectional recurrent neural networks BIBREF23 or ensembles of recurrent neural networks BIBREF24. The latter is reported to achieve 95.12% in the DSL 2015 shared task. In these models text features can
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 879.

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

#### Rank 1: qasper-passage-v1-c4b9513d1ced5f1d17e25bc9893e044c44aa84f3e2961b4321ee44c4a0f2af18

Passage ID: `qasper-passage-v1-c4b9513d1ced5f1d17e25bc9893e044c44aa84f3e2961b4321ee44c4a0f2af18`; retrieval score: 3.1941250572396163.

Word count: 200.

```text
Entity linking (EL) BIBREF24 , also known as named entity disambiguation or normalization, is the task to determine the identity of entities mentioned in a piece of text with reference to a knowledge base. There are a number of knowledge bases that provide a background repository for entity classification of this type. For this study, we use Wikidata, which can be seen diagrammatically in Figure FIGREF12 . Systems such as DeepType BIBREF25 integrate symbolic information into the reasoning process of a neural network with a type system and show state-of-the-art performances for EL. They do not, however, quote results on Wiki(gold) so a direct comparison is difficult.

While these knowledge bases provide semantically rich and fine-granular classes and relationship types, the task of entity classification often requires associating coarse-grained classes with discovered surface forms of entities. Most existing studies consider NER and entity linking as two separate tasks, whereas we try to combine the two. It has been shown that one can significantly increase the semantic information carried by a NER system when we successfully linking entities from a deep learning method to the related entities from a knowledge base BIBREF26 , BIBREF27 .

Redirection: For the Wikidata linking element,
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-2e159067bab1e48feba29e3c986d79cacffcd23e2eb96d1ec55d5c0355d61869

Passage ID: `qasper-passage-v1-2e159067bab1e48feba29e3c986d79cacffcd23e2eb96d1ec55d5c0355d61869`; retrieval score: 3.125693026541848.

Word count: 160.

```text
The results for each class type are shown in Table TABREF19 , with some specific examples shown in Figure FIGREF18 . For the Wiki(gold) we quote the micro-averaged F-1 scores for the entire top level entity category. The total F-1 score on the OntoNotes dataset is 88%, and the total F-1 cross-validation score on the 112 class Wiki(gold) dataset is 53%. It is worth noting that one could improve Wiki(gold) results by training directly using this dataset. However, the aim is not to tune our model specifically on this class hierarchy. We instead aim to present a framework which can be modified easily to any domain hierarchy and has acceptable out-of-the-box performances to any fine-grained dataset. The results in Table TABREF19 (OntoNotes) only show the main 7 categories in OntoNotes which map to Wiki(gold) for clarity. The other categories (date, time, norp, language, ordinal, cardinal, quantity, percent, money, law) have F-1 scores between 80-90%, with the exception of time (65%)
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.10503:6:0` | full | 0:992 |

#### Rank 3: qasper-passage-v1-cae4ed0af2694ebee740e9b74fc36488c6d082f0739fb2846ee6638294a2d3a3

Passage ID: `qasper-passage-v1-cae4ed0af2694ebee740e9b74fc36488c6d082f0739fb2846ee6638294a2d3a3`; retrieval score: 2.8448011993369073.

Word count: 200.

```text
Named entity recognition (NER) BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 is the process by which we identify text spans which mention named entities, and to classify them into predefined categories such as person, location, organization etc. NER serves as the basis for a variety of natural language processing (NLP) applications such as relation extraction BIBREF4 , machine translation BIBREF5 , question answering BIBREF6 and knowledge base construction BIBREF7 . Although early NER systems have been successful in producing adequate recognition accuracy, they often require significant human effort in carefully designing rules or features.

In recent years, deep learning methods been employed in NER systems, yielding state-of-the-art performance. However, the number of types detected are still not sufficient for certain domain-specific applications. For relation extraction, identifying fine-grained types has been shown to significantly increase the performance of the extractor BIBREF8 , BIBREF9 since this helps in filtering out candidate relation types which do not follow this type constraint. Furthermore, for question answering fine-grained Named Entity Recognition (FgNER) can provide additional information helping to match questions to its potential answers thus improving performance BIBREF10 . For example, Li and Roth BIBREF11 rank questions based on their expected answer types (i.e. will
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-b0f14861bfadc3c94f474a8ccfe7a730b62b4e4d82e97c435d82e95e47e2d4b6

Passage ID: `qasper-passage-v1-b0f14861bfadc3c94f474a8ccfe7a730b62b4e4d82e97c435d82e95e47e2d4b6`; retrieval score: 2.2061769490166867.

Word count: 200.

```text
labels to all mentions of a particular entity in the corpus. For example, “Barack Obama” is a person, politician, lawyer, and author. If a knowledge base has these four matching labels, the distant supervision technique will assign all of them to every mention of “Barack Obama”. Therefore, the training data will also fail to distinguish between mentions of “Barack Obama” in all subsequent utterances.

Ling et al. ling2012fine proposed the first system for FgNER, where they used 112 overlapping labels with a linear classifier perceptron for multi-label classification. Yosef et al. spaniol2012hyena used multiple binary SVM classifiers to assign entities to a set of 505 types. Gillick et al. gillick2014context introduced context dependent FgNER and proposed a set of heuristics for pruning labels that might not be relevant given the local context of the entity. Yogatama et al. yogatama2015embedding proposed an embedding based model where user-defined features and labels were embedded into a low dimensional feature space to facilitate information sharing among labels.

Shimaoka et al. shimaoka2016attentive proposed an attentive neural network model which used long short-term memory (LSTMs) to encode the context of the entity, then used an attention mechanism to allow the model to focus on relevant expressions
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-ffe6687d0551219008b4113f18ad930e6c5f1f3454a35544ad79dab807e07c76

Passage ID: `qasper-passage-v1-ffe6687d0551219008b4113f18ad930e6c5f1f3454a35544ad79dab807e07c76`; retrieval score: 1.8911382286437164.

Word count: 200.

```text
NER involves identifying both entity boundaries and entity types. With “exact-match evaluation”, a named entity is considered correctly recognized only if both the boundaries and type match the ground truth BIBREF8 , BIBREF17 , BIBREF18 . Precision, Recall, and F-1 scores are computed on the number of true positives (TP), false positives (FP), and false negatives (FN). Their formal definitions are as follows:

True Positive (TP): entities that are recognized by NER and match the ground truth.

False Positive (FP): entities that are recognized by NER but do not match the ground truth.

False Negative (FN): entities annotated in the ground which that are not recognized by NER.

Precision measures the ability of a NER system to present only correct entities, and Recall measures the ability of a NER system to recognize all entities in a corpus. DISPLAYFORM0

The F-1 score is the harmonic mean of precision and recall, and the balanced F-1 score is the variant which is most commonly used. This is defined as: DISPLAYFORM0

Since most NER systems involve multiple entity types, it is often required to assess the performance across all entity classes. Two measures are commonly used for this purpose: the macro-averaged F-1 score and
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 960.

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

#### Rank 1: qasper-passage-v1-a29c4f8889e7772d843c82877b4f345fca30acf902010c437eba339a91fce84d

Passage ID: `qasper-passage-v1-a29c4f8889e7772d843c82877b4f345fca30acf902010c437eba339a91fce84d`; retrieval score: 7.61239355077363.

Word count: 200.

```text
To the best of our knowledge, there are only two recent works that specifically study how to combine word and subword-level vector representations.

BIBREF11 propose to use a trainable scalar gating mechanism capable of learning a weighting scheme for combining character-level and word-level representations. They compared their proposed method to manually weighting both levels; using characters only; words only; or their concatenation. They found that in some datasets a specific manual weighting scheme performed better, while in others the learned scalar gate did.

BIBREF12 further expand the gating concept by making the mechanism work at a finer-grained level, learning how to weight each vector's dimensions independently, conditioned on external word-level features such as part-of-speech and named-entity tags. Similarly, they compared their proposed mechanism to using words only, characters only, and a concatenation of both, with and without external features. They found that their vector gate performed better than the other methods in all the reported tasks, and beat the state of the art in two reading comprehension tasks.

Both works showed that the gating mechanisms assigned greater importance to character-level representations in rare words, and to word-level representations in common ones, reaffirming the previous findings that subword structures in general,
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-c922c4624f2234aa7de62915a793ad6d25386fe618b960c57311f155f00934a5

Passage ID: `qasper-passage-v1-c922c4624f2234aa7de62915a793ad6d25386fe618b960c57311f155f00934a5`; retrieval score: 5.8100988984907325.

Word count: 130.

```text
To enable sentence-level classification we need to obtain a sentence representation from the word vectors INLINEFORM0 . We achieved this by using a BiLSTM with max pooling, which was shown to be a good universal sentence encoding mechanism BIBREF13 .

Let INLINEFORM0 , be an input sentence and INLINEFORM1 its matrix representation, where each INLINEFORM2 was obtained by one of the methods described in subsec:methods. INLINEFORM3 is the context-enriched matrix representation of INLINEFORM4 obtained by feeding INLINEFORM5 to a BiLSTM of output dimension INLINEFORM6 . Lastly, INLINEFORM11 is the final sentence representation of INLINEFORM12 obtained by max-pooling INLINEFORM13 along the sequence dimension.

Finally, we initialized the word representations INLINEFORM0 using GloVe embeddings BIBREF14 , and fine-tuned them during training. Refer to app:hyperparams for details on the other hyperparameters we used.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.05584:4:0` | full | 0:250 |

#### Rank 3: qasper-passage-v1-74922125b5546b1b81d39a747549e8b074e219ae610323a1a9db063948406aeb

Passage ID: `qasper-passage-v1-74922125b5546b1b81d39a747549e8b074e219ae610323a1a9db063948406aeb`; retrieval score: 5.356634260297278.

Word count: 200.

```text
The problem of representing sentences as fixed-length vectors has been widely studied.

BIBREF32 suggested a self-adaptive hierarchical model that gradually composes words into intermediate phrase representations, and adaptively selects specific hierarchical levels for specific tasks. BIBREF33 proposed an encoder-decoder model trained by attempting to reconstruct the surrounding sentences of an encoded passage, in a fashion similar to Skip-gram BIBREF34 . BIBREF35 overcame the previous model's need for ordered training sentences by using autoencoders for creating the sentence representations. BIBREF36 implemented a model simpler and faster to train than the previous two, while having competitive performance. Similar to BIBREF33 , BIBREF37 suggested predicting future sentences with a hierarchical CNN-LSTM encoder.

BIBREF13 trained several sentence encoding architectures on a combination of the SNLI and MultiNLI datasets, and showed that a BiLSTM with max-pooling was the best at producing highly transferable sentence representations. More recently, BIBREF18 empirically showed that sentence representations created in a multi-task setting BIBREF38 , performed increasingly better the more tasks they were trained in. BIBREF39 proposed using an autoencoder that relies on multi-head self-attention over the concatenation of the max and mean pooled encoder outputs for producing sentence representations. Finally, BIBREF40 show that modern sentence embedding methods are not
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-52f117ffeccbf8b8195fcd3037363528898503211f13fda41f70e37e456353f5

Passage ID: `qasper-passage-v1-52f117ffeccbf8b8195fcd3037363528898503211f13fda41f70e37e456353f5`; retrieval score: 4.854415293525694.

Word count: 103.

```text
tasks they were trained in. BIBREF39 proposed using an autoencoder that relies on multi-head self-attention over the concatenation of the max and mean pooled encoder outputs for producing sentence representations. Finally, BIBREF40 show that modern sentence embedding methods are not vastly superior to random methods.

The works mentioned so far usually evaluate the quality of the produced sentence representations in sentence-level downstream tasks. Common benchmarks grouping these kind of tasks include SentEval BIBREF23 , and GLUE BIBREF41 . Another trend, however, is to probe sentence representations to understand what linguistic phenomena they encode BIBREF42 , BIBREF43 , BIBREF44 , BIBREF45 , BIBREF46 .
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-2ac17457374ef5df0917944838c8e6ad104038f7ebee00ee9935199d6cb83456

Passage ID: `qasper-passage-v1-2ac17457374ef5df0917944838c8e6ad104038f7ebee00ee9935199d6cb83456`; retrieval score: 4.588531018642148.

Word count: 200.

```text
table:wordlevelresults shows the quality of word representations in terms of the correlation between word similarity scores obtained by the proposed models and word similarity scores defined by humans.

First, we can see that for each task, character only models had significantly worse performance than every other model trained on the same dataset. The most likely explanation for this is that these models are the only ones that need to learn word representations from scratch, since they have no access to the global semantic knowledge encoded by the GloVe embeddings.

Further, bold results show the overall trend that vector gates outperformed the other methods regardless of training dataset. This implies that learning how to combine character and word-level representations at the dimension level produces word vector representations that capture a notion of word similarity and relatedness that is closer to that of humans.

Additionally, results from the MNLI row in general, and underlined results in particular, show that training on MultiNLI produces word representations better at capturing word similarity. This is probably due to MultiNLI data being richer than that of SNLI. Indeed, MultiNLI data was gathered from various sources (novels, reports, letters, and telephone conversations, among others), rather than the
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 833.

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

#### Rank 1: qasper-passage-v1-18e2c5a012133052e35624a9d220270ded695a3a925b2ecf3ed6a04058eb35f4

Passage ID: `qasper-passage-v1-18e2c5a012133052e35624a9d220270ded695a3a925b2ecf3ed6a04058eb35f4`; retrieval score: 6.010968264001631.

Word count: 80.

```text
computed using a one-layer feed-forward network.

During training, the model requires negative samples. For each positive example, (question, ground-truth segment), all the other segments in the same transcript are used as negative samples. Cross entropy is used as an objective function.

Metrics. We used accuracy and MRR (Mean Reciprocal Ranking) as metrics. The accuracy is

We split the ground-truth dataset to train/dev/test into the ratio of 6/2/2. The resulting size is 3,718 (train), 1,238 (dev) and 1,239 qa pairs (test).
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1912.01046:9:5` | full | 0:87 |

#### Rank 2: qasper-passage-v1-b6fc183088222dd814e82d1f484011e07ab4956ea8470d34e11318caa1da2075

Passage ID: `qasper-passage-v1-b6fc183088222dd814e82d1f484011e07ab4956ea8470d34e11318caa1da2075`; retrieval score: 5.397695410945698.

Word count: 200.

```text
We downloaded 76 videos from a tutorial website about an image editing program . Each video is pre-processed to provide the transcripts and the time-stamp information for each sentence in the transcript. We then used Amazon Mechanical Turk to collect the question-answer pairs . One naive way of collecting the data is to prepare a question list and then, for each question, ask the workers to find the relevant parts in the video. However, this approach is not feasible and error-prone because the videos are typically long and finding a relevant part from a long video is difficult. Doing so might also cause us to miss questions which were relevant to the video segment. Instead, we took a reversed approach. First, for each video, we manually identified the sentence spans that can serve as answers. These candidates are of various granularity and may overlap. The segments are also complete in that they encompass the beginning and end of a task. In total, we identified 408 segments from the 76 videos. Second we asked AMT workers to provide question annotations for the videos.

Our AMT experiment consisted of two parts. In the first part, we presented the workers with the video
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-d949947b021dbcb1048a9acd47ef6ffeb6dd552cff54fa98b6f99db6a913e441

Passage ID: `qasper-passage-v1-d949947b021dbcb1048a9acd47ef6ffeb6dd552cff54fa98b6f99db6a913e441`; retrieval score: 5.236060234947983.

Word count: 200.

```text
In total, we identified 408 segments from the 76 videos. Second we asked AMT workers to provide question annotations for the videos.

Our AMT experiment consisted of two parts. In the first part, we presented the workers with the video content of a segment. For each segment, we asked workers to generate questions that can be answered by the presented segment. We did not limit the number of questions a worker can input to a corresponding segment and encouraged them to input a diverse set of questions which the span can answer. Along with the questions, the workers were also required to provide a justification as to why they made their questions. We manually checked this justification to filter out the questions with poor quality by removing those questions which were unrelated to the video. One initial challenge worth mentioning is that at first some workers input questions they had about the video and not questions which the video could answer. This was solved by providing them with an unrelated example. The second part of the question collection framework consisted of a paraphrasing task. In this task we presented workers with the questions generated by the first task and asked
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-dc5fa5366933eae6a5970ef6c14ef63bc78aa8df34aaff73f8dfda0b4d7f58d7

Passage ID: `qasper-passage-v1-dc5fa5366933eae6a5970ef6c14ef63bc78aa8df34aaff73f8dfda0b4d7f58d7`; retrieval score: 5.2316521753610274.

Word count: 200.

```text
Table TABREF12 presents some extracted sample questions from our dataset. The first column corresponds to an AMT generated question, while the second column corresponds to the video ID where the segment can be found. As can be seen in the first two rows, multiple types of questions can be answered within the same video (but different segments). The last two rows display questions which belong to the same segment but correspond to different properties of the same entity, 'crop tool'. Here we observe different types of questions, such as "why", "how", "what", and "where", and can see why the answers may involve multiple steps. Some questions that the worked paraphrased were in the "yes/no" style, however our answer segments then provide an explanation to these questions.

Each answer segment was extracted from an image editing tutorial video that involved multiple steps and procedures to produce a final image, which can partially be seen in FIGREF1. The average number of sentences per video was approximately 52, with the maximum number of sentences contained in a video being 187. The sub-tasks in the tutorial include segments (and thus answers) on editing parts of images, instructions on using certain tools, possible actions that
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-439b95db49d22b044f8c871d0cb956c2a8f2b2af8f13dcaf480197f821e4137c

Passage ID: `qasper-passage-v1-439b95db49d22b044f8c871d0cb956c2a8f2b2af8f13dcaf480197f821e4137c`; retrieval score: 4.641309557083343.

Word count: 115.

```text
inputs are are the question, q, and video transcript, v, encoded by their TF-IDF vectors: BIBREF18:

We then filter the top 10 video transcripts(out of 76) with the minimum cosine distance, and further compute the TF-IDF vectors for their segments, Stop10n, where n = 10. We repeat the process for the corresponding segments:

selecting the segment with the minimal cosine distance distance to the query.

Metrics. To evaluate our pipeline approach we use overall accuracy after filtering and accuracy given that the segment is in the top 10 videos. While the first metric is similar to SECREF17, the second can indicate if initially searching on the video space can be used to improve our selection:
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1912.01046:10:4` | full | 0:294 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 795.

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

#### Rank 1: qasper-passage-v1-f1656375e77dd17d733b859085fad628445a9c4e5bfd76f7760f764ec3eedaa5

Passage ID: `qasper-passage-v1-f1656375e77dd17d733b859085fad628445a9c4e5bfd76f7760f764ec3eedaa5`; retrieval score: 4.504658961972492.

Word count: 200.

```text
This paper has explored how DTW and TED can be extended with word2vec to construct semantic document distance measures: wDTW and wTED. By representing paragraphs with concatenations of word vectors, wDTW and wTED are able to capture the semantics of the words and thus give more accurate distance scores. In order to detect revisions, we have used minimum branching on an appropriately developed network with document distance scores serving as arc weights. We have also assessed the efficiency of the method of retrieving an optimal revision subnetwork by finding the minimum branching.

Furthermore, we have compared wDTW and wTED with several distance measures for revision detection tasks. Our results demonstrate the effectiveness and robustness of wDTW and wTED in the Wikipedia revision dumps and our simulated data sets. In order to reduce the computation time, we have computed document distances at the paragraph level and implemented a boosting learning system using Apache Spark. Although we have demonstrated the superiority of our semantic measures only in the revision detection experiments, wDTW and wTED can also be used as semantic distance measures in many clustering, classification tasks.

Our revision detection system can be enhanced with richer features such as author information and
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-7cace1b126d5733986651acc3a4b3f1b79f08eb2d48c45c0c77fa5588c4d2ce8

Passage ID: `qasper-passage-v1-7cace1b126d5733986651acc3a4b3f1b79f08eb2d48c45c0c77fa5588c4d2ce8`; retrieval score: 4.434628796600351.

Word count: 70.

```text
our semantic measures only in the revision detection experiments, wDTW and wTED can also be used as semantic distance measures in many clustering, classification tasks.

Our revision detection system can be enhanced with richer features such as author information and writing styles, and exact changes in revision pairs. Another interesting aspect we would like to explore in the future is reducing the complexities of calculating the distance between two paragraphs.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-298842d8762bfb93af314053713bc0ed820e14c3c29402bf5bb5856252f00a58

Passage ID: `qasper-passage-v1-298842d8762bfb93af314053713bc0ed820e14c3c29402bf5bb5856252f00a58`; retrieval score: 4.067794017650323.

Word count: 200.

```text
We use precision, recall and F-measure to evaluate the detected revisions. A true positive case is a correctly identified revision. A false positive case is an incorrectly identified revision. A false negative case is a missed revision record.

We illustrate the performances of wDTW, wTED, WMD, VSM, PV-DTW and PV-TED on the Wikipedia revision dumps in Figure FIGREF43 . wDTW and wTED have the highest F-measure scores compared to the rest of four measures, and wDTW also have the highest precision and recall scores. Figure FIGREF49 shows the average evaluation results on the simulated data sets. From left to right, the corpus size increases and the revision chains become longer, thus it becomes more challenging to detect document revisions. Overall, wDTW consistently performs the best. WMD is slightly better than wTED. In particular, when the corpus size increases, the performances of WMD, VSM, PV-DTW and PV-TED drop faster than wDTW and wTED. Because the revision operations were randomly selected in each corpus, it is possible that there are non-monotone points in the series.

wDTW and wTED perform better than WMD especially when the corpus is large, because they use dynamic programming to find the global optimal alignment for documents. In
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1709.01256:12:0` | full | 0:243 |

#### Rank 4: qasper-passage-v1-dd1efdc754728e47bae5459f44290d73b90e89c9ae08fab9310350d745dbfce0

Passage ID: `qasper-passage-v1-dd1efdc754728e47bae5459f44290d73b90e89c9ae08fab9310350d745dbfce0`; retrieval score: 3.8315681412168403.

Word count: 200.

```text
a distance/similarity score. The classic document similarity measure, especially for plagiarism detection, is fingerprinting BIBREF7 , BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 . Fixed-length fingerprints are created using hash functions to represent document features and are then used to measure document similarities. However, the main purpose of fingerprinting is to reduce computation instead of improving accuracy, and it cannot capture word semantics. Another widely used approach is computing the sentence-to-sentence Levenshtein distance and assigning an overall score for every document pair BIBREF13 . Nevertheless, due to the large number of existing documents, as well as the large number of sentences in each document, the Levenshtein distance is not computation-friendly. Although alternatives such as the vector space model (VSM) can largely reduce the computation time, their effectiveness is low. More importantly, none of the above approaches can capture semantic meanings of words, which heavily limits the performances of these approaches. For instance, from a semantic perspective, “I went to the bank" is expected to be similar to “I withdrew some money" rather than “I went hiking." Our document distance measures are inspired by the weaknesses of current document distance/similarity measures and recently proposed models for word representations such
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-19cba8c23f78ff3a7522cae97a0a2ae5b6e5cc56efd0800d7d5cf3166c623915

Passage ID: `qasper-passage-v1-19cba8c23f78ff3a7522cae97a0a2ae5b6e5cc56efd0800d7d5cf3166c623915`; retrieval score: 3.8178924304135506.

Word count: 172.

```text
Our system is a boosting learner that is composed of four modules: weak filter, strong filter, revision network and optimal subnetwork. First of all, we sort all documents by timestamps and pair up documents so that we only compare each document with documents that have been created earlier. In the first module, we calculate the VSM similarity scores for all pairs and eliminate those with scores that are lower than an empirical threshold ( INLINEFORM0 ). This is what we call the weak filter. After that, we apply the strong filter wDTW or wTED on the available pairs and filter out document pairs having distances higher than a threshold INLINEFORM1 . For VSM in Section SECREF32 , we directly filter out document pairs having similarity scores lower than a threshold INLINEFORM2 . The cut-off threshold estimation is explained in Section SECREF30 . The remaining document pairs from the strong filter are then sent to the revision network module. In the end, we output the optimal revision pairs following the minimum branching strategy.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 842.

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

#### Rank 1: qasper-passage-v1-c0b2857b454d753afc33a27d78cc2a07cc40e431057dc752ad639dbd3f6689c8

Passage ID: `qasper-passage-v1-c0b2857b454d753afc33a27d78cc2a07cc40e431057dc752ad639dbd3f6689c8`; retrieval score: 2.788886211149748.

Word count: 52.

```text
be tailored to individual systems. The oos-threshold method is a more general decision rule that can be applied to any model that produces a probability. In our evaluation, the out-of-scope threshold was chosen to be the value which yielded the highest validation score across all intents, treating out-of-scope as its own intent.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-16edfd600126be92d53ab6f5d75ad65f7ca5a83fbf0241bdcd2c3ccc20cab678

Passage ID: `qasper-passage-v1-16edfd600126be92d53ab6f5d75ad65f7ca5a83fbf0241bdcd2c3ccc20cab678`; retrieval score: 2.3430624720572446.

Word count: 118.

```text
For all queries collected, all tokens were down-cased, and all end-of-sentence punctuation was removed. Additionally, all duplicate queries were removed and replaced.

In an effort to reduce bias in the in-scope data, we placed all queries from a given crowd worker in a single split (train, validation, or test). This avoids the potential issue of similar queries from a crowd worker ending up in both the train and test sets, for instance, which would make the train and test distributions unrealistically similar. We note that this is a recommendation from concurrent work by BIBREF3. We also used this procedure for the out-of-scope set, except that we split the data into train/validation/test based on task prompt instead of worker.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-efd6ad9d6f5c1dfe9f63f3ba3ff86e7374765d0600b39fbb0d72b705a3196c39

Passage ID: `qasper-passage-v1-efd6ad9d6f5c1dfe9f63f3ba3ff86e7374765d0600b39fbb0d72b705a3196c39`; retrieval score: 2.251365097817631.

Word count: 151.

```text
Table TABREF14 presents results for all models across the four variations of the dataset. First, BERT is consistently the best approach for in-scope, followed by MLP. Second, out-of-scope query performance is much lower than in-scope across all methods. Training on less data (Small and Imbalanced) yields models that perform slightly worse on in-scope queries. The trend is mostly the opposite when evaluating out-of-scope, where recall increases under the Small and Imbalanced training conditions. Under these two conditions, the size of the in-scope training set was decreased, while the number of out-of-scope training queries remained constant. This indicates that out-of-scope performance can be increased by increasing the relative number of out-of-scope training queries. We do just that in the OOS+ setting—where the models were trained on the full training set as well as 150 additional out-of-scope queries—and see that performance on out-of-scope increases substantially, yet still remains low relative to in-scope accuracy.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-2846a9d58cccf4b5191648e7d92b61342acddeb83f546eab885c5db2b8576f6f

Passage ID: `qasper-passage-v1-2846a9d58cccf4b5191648e7d92b61342acddeb83f546eab885c5db2b8576f6f`; retrieval score: 2.0191135113911196.

Word count: 200.

```text
We use three baseline approaches for the task of predicting whether a query is out-of-scope: (1) oos-train, where we train an additional (i.e. 151st) intent on out-of-scope training data; (2) oos-threshold, where we use a threshold on the classifier's probability estimate; and (3) oos-binary, a two-stage process where we first classify a query as in- or out-of-scope, then classify it into one of the 150 intents if classified as in-scope.

To reduce the severity of the class imbalance between in-scope versus out-of-scope query samples (i.e., 15,000 versus 250 queries for OOS+), we investigate two strategies when using oos-binary: one where we undersample the in-scope data and train using 1,000 in-scope queries sampled evenly across all intents (versus 250 out-of-scope), and another where we augment the 250 OOS+ out-of-scope training queries with 14,750 sentences sampled from Wikipedia.

From a development point of view, the oos-train and oos-binary methods both require careful curation of an out-of-scope training set, and this set can be tailored to individual systems. The oos-threshold method is a more general decision rule that can be applied to any model that produces a probability. In our evaluation, the out-of-scope threshold was chosen to be the value which yielded the
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-482ee0a4173f348e3608715c17df7a12be42c264cbe4b5efef26ad1e70483eaf

Passage ID: `qasper-passage-v1-482ee0a4173f348e3608715c17df7a12be42c264cbe4b5efef26ad1e70483eaf`; retrieval score: 1.130607961204069.

Word count: 200.

```text
system for personal finance. In the first user-system exchange, the system correctly identifies the user's intent as an in-scope balance query. In the second and third exchanges, the user queries with out-of-scope inputs. In the second exchange, the system incorrectly identifies the query as in-scope and yields an unrelated response. In the third exchange, the system correctly classifies the user's query as out-of-scope, and yields a fallback response.

Out-of-scope queries are inevitable for a task-oriented dialog system, as most users will not be fully cognizant of the system's capabilities, which are limited by the fixed number of intent classes. Correctly identifying out-of-scope cases is thus crucial in deployed systems—both to avoid performing the wrong action and also to identify potential future directions for development. However, this problem has seen little attention in analyses and evaluations of intent classification systems.

This paper fills this gap by analyzing intent classification performance with a focus on out-of-scope handling. To do so, we constructed a new dataset with 23,700 queries that are short and unstructured, in the same style made by real users of task-oriented systems. The queries cover 150 intents, plus out-of-scope queries that do not fall within any of the 150 in-scope
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 721.

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

#### Rank 1: qasper-passage-v1-442b5695807a12d4702120cde887a0b9bc45ee2c4387aaa1a8e7da4413e87865

Passage ID: `qasper-passage-v1-442b5695807a12d4702120cde887a0b9bc45ee2c4387aaa1a8e7da4413e87865`; retrieval score: 4.907206669272378.

Word count: 200.

```text
task. In order to do so, we convert an annotated review such as the one in Figure FIGREF1 into the BIO scheme for learning sequence labelling models BIBREF3 . Example (1) shows the review in BIO format. Tokens in the review are tagged depending on whether they are at the beginning (B-target), inside (I-target) or outside (O) of the opinion target expression. Note that the third opinion target in Figure FIGREF1 is implicit.

We learn language independent models which consist of a set of local, shallow features complemented with semantic distributional features based on clusters obtained from a variety of data sources. We show that our approach, despite the lack of hand-engineered, language-specific features, obtains state-of-the-art results in 7 datasets for 6 languages on the ABSA benchmarks BIBREF4 , BIBREF5 , BIBREF6 .

The main contribution of this research note is providing an extension or addendum to previous work on sequence labelling BIBREF7 by reporting additional experimental results as well as further insights on the performance of our model across languages on a different NLP task such as Opinion Target Extraction (OTE). Thus, we empirically demonstrate the validity and strong performance of our approach for six languages in seven different
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-243c9dd9736acbf63109eb399e3b1cfa597c225ca25b99a319ac5313ef64bbc1

Passage ID: `qasper-passage-v1-243c9dd9736acbf63109eb399e3b1cfa597c225ca25b99a319ac5313ef64bbc1`; retrieval score: 3.946356140577918.

Word count: 113.

```text
as further insights on the performance of our model across languages on a different NLP task such as Opinion Target Extraction (OTE). Thus, we empirically demonstrate the validity and strong performance of our approach for six languages in seven different datasets of the restaurant domain. Every experiment and result presented in this note is novel.

In this sense, we show that our approach is not only competitive across languages and domains for Named Entity Recognition, as shown by BIBREF7 , but that it can be straightforwardly adapted to different tasks and domains such as OTE. Furthermore, we release the system and every model trained for public use and to facilitate reproducibility of results.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-048c6dc9e1499de3f386ea52a1cd921ebf8bac8b5de8a6e3c955e1aefa639435

Passage ID: `qasper-passage-v1-048c6dc9e1499de3f386ea52a1cd921ebf8bac8b5de8a6e3c955e1aefa639435`; retrieval score: 3.0452789676244683.

Word count: 200.

```text
We trained our system for 5 other languages on the ABSA 2016 datasets, using the same strategy as for English. We choose the best Clark-Word2vec combination (with and without Brown clusters) via 5-cross validation on the training data. The features are exactly the same as those used for English, the only change is the data on which the clusters are trained. Table TABREF19 reports on the detailed results obtained for each of the languages. In bold we show the best model chosen via 5-fold CV. Moreover, we also show the best models using only one of each of the clustering features.

The first difference with respect to the English results is that the Brown clustering features are, in three out of five settings, detrimental to performance. Second, that combining clustering features is only beneficial for Spanish. Third, the overall results are in general lower than those obtained in the 2016 English data. Finally, the difference between the best results and the results using the Local features is lower than for English, even though the Local results are similar to those obtained with the English datasets (except for Turkish, but this is due to the significantly smaller size of the data,
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-e58bfd9ff8656e8ad09e9641b3011471dc745595634ac1999b626106f6a6255a

Passage ID: `qasper-passage-v1-e58bfd9ff8656e8ad09e9641b3011471dc745595634ac1999b626106f6a6255a`; retrieval score: 2.540449858476144.

Word count: 83.

```text
our system's performance remains competitive thanks to the combination of clustering features. This, together with the lack of linguistic features, facilitates the easy and fast development of systems for new domains or languages. These considerations thus confirm the hypotheses stated in BIBREF7 with respect to the use of clustering features to obtain robust sequence taggers across languages and tasks.

The system and models for every language and dataset are available as part of the ixa-pipe-opinion module for public use and reproducibility of results.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-a4978b5c67c86dd8cd9e7a6629abeb5fa2b7b3cc981a6e1d3ad0fe3ad2be7699

Passage ID: `qasper-passage-v1-a4978b5c67c86dd8cd9e7a6629abeb5fa2b7b3cc981a6e1d3ad0fe3ad2be7699`; retrieval score: 2.4402553587928635.

Word count: 200.

```text
By inspecting our system's output, and both the test and training sets, we found out that there were three main sources of errors: (a) errors caused by ambiguity in the use of certain source forms that may or may not refer to an opinion target; (b) span errors, where the target has only been partially annotated; and (c) unknown targets, which the system was unable to annotate by generalizing on the training data or clusters.

With respect to type (a), it is useful to look at the most common errors for all three languages, namely, `place', `food' and `restaurant', which are also among the top 5 most frequent targets in the gold standard sets. By looking at Examples (1-3) we would say that in all three cases `place' should be annotated as opinion target. However, (2) is a false positive (FP), (3) is a false negative (FN) and (1) is an example from the training set in which `place' is annotated as target. This is the case with many instances of `place' for which there seems to be some inconsistency in the actual annotation of the training and test set examples.

Example (1): Avoid this place!

Example (2): this place
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 796.

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

#### Rank 1: qasper-passage-v1-f85afc71bb706389bc1c0568b41a482b42dcf8e636d5f17437b6b06584187dac

Passage ID: `qasper-passage-v1-f85afc71bb706389bc1c0568b41a482b42dcf8e636d5f17437b6b06584187dac`; retrieval score: 3.607926657075343.

Word count: 200.

```text
learning word embeddings with Word2Vec BIBREF16 , BIBREF17 ). Based on this, we propose an alternative measure of recommendation quality by learning the semantic relationships from both vocabularies and then using it to compare how semantically similar the recommended tags are to the expected review keywords. For this, we first extract the textual content in the form of the description text, title, editor tags and Amazon search terms of e-books from our dataset. We then train a Doc2Vec BIBREF7 model on the content. Then, we use the model to infer the latent representation for both the complete list of recommended tags as well as the list of expected tags from the test set. Finally, we use the cosine similarity measure to calculate how semantically similar these two lists are.

Recommendation diversity. As defined in BIBREF18 , we calculate recommendation diversity as the average dissimilarity of all pairs of tags in the list of recommended tags. Thus, given a distance function INLINEFORM0 that corresponds to the dissimilarity between two tags INLINEFORM1 and INLINEFORM2 in the list of recommended tags, INLINEFORM3 is given as the average dissimilarity of all pairs of tags: DISPLAYFORM0

where INLINEFORM0 is the number of evaluated e-books and
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.04042:6:8` | full | 0:416 |

#### Rank 2: qasper-passage-v1-3f4fe5971c95784af01597c4c7b7237859a687536fa40a55855c0df43c52c61e

Passage ID: `qasper-passage-v1-3f4fe5971c95784af01597c4c7b7237859a687536fa40a55855c0df43c52c61e`; retrieval score: 3.442953196700164.

Word count: 85.

```text
how semantically similar (based on learned Doc2Vec BIBREF7 embeddings) the list of recommended tags is to the list of relevant tags. We use this additional metric to measure not only exact “hits” of our recommendations but also semantic matches.

Our evaluation results show that combining both data sources enhances the quality of tag recommendations for annotating e-books. Furthermore, approaches that solely train on Amazon search terms provide poor performance in terms of accuracy but deliver good results in terms of semantic similarity and recommendation diversity.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-ea49d8e495890374446bf681174e327a3244110a1a26095945660814054575e1

Passage ID: `qasper-passage-v1-ea49d8e495890374446bf681174e327a3244110a1a26095945660814054575e1`; retrieval score: 3.0476562894612624.

Word count: 200.

```text
In this work, we measure (i) recommendation accuracy, (ii) semantic similarity, and (iii) recommendation diversity to evaluate the quality of our approaches from different perspectives.

Recommendation accuracy. We use Normalized Discounted Cumulative Gain (nDCG) BIBREF15 to measure the accuracy of the tag recommendation approaches. The nDCG measure is a standard ranking-dependent metric that not only measures how many tags can be correctly predicted but also takes into account their position in the recommendation list with length of INLINEFORM0 . It is based on the Discounted Cummulative Gain, which is given by: DISPLAYFORM0

where INLINEFORM0 is a function that returns 1 if the recommended tag at position INLINEFORM1 in the recommended list is relevant. We then calculate DCG@ INLINEFORM2 for every evaluated e-book by dividing DCG@ INLINEFORM3 with the ideal DCG value iDCG@ INLINEFORM4 , which is the highest possible DCG value that can be achieved if all the relevant tags would be recommended in the correct order. It is given by the following formula BIBREF15 : DISPLAYFORM0

Semantic similarity. One precondition of standard recommendation accuracy measures is that to generate a “hit”, the recommended tag needs to be an exact syntactical match to the one from the test set. When
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-5f56fe74c4c7093795500afa45abeee798e39d7feaa8b82be8c1f3d33ecdb31c

Passage ID: `qasper-passage-v1-5f56fe74c4c7093795500afa45abeee798e39d7feaa8b82be8c1f3d33ecdb31c`; retrieval score: 3.003857793012619.

Word count: 200.

```text
as well as Amazon search terms to account for the vocabulary of e-book readers.

Concerning the evaluation of tag recommendation systems, most studies focus on measuring the accuracy of tag recommendations (e.g., BIBREF2 ). However, the authors of BIBREF6 suggest also to use beyond-accuracy metrics such as diversity to evaluate the quality of tag recommendations. In our work, we measure recommendation diversity in addition to recommendation accuracy and propose a novel metric termed semantic similarity to validate semantic matches of tag recommendations.

Approach and findings. We exploit editor tags and user-generated search terms as input for tag recommendation approaches. Our evaluation comprises of a rich set of 19 different algorithms to recommend tags for e-books, which we group into (i) popularity-based, (ii) similarity-based (i.e., using content information), and (iii) hybrid approaches. We evaluate our approaches in terms of accuracy, semantic similarity and diversity on the review content of Amazon users, which reflects the readers' vocabulary. With semantic similarity, we measure how semantically similar (based on learned Doc2Vec BIBREF7 embeddings) the list of recommended tags is to the list of relevant tags. We use this additional metric to measure not only exact “hits” of our recommendations but also semantic matches.

Our
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-a2857b4effc0d3c42422962d4d58c8e83d917fdc197875b5ac2612c5d4f644c1

Passage ID: `qasper-passage-v1-a2857b4effc0d3c42422962d4d58c8e83d917fdc197875b5ac2612c5d4f644c1`; retrieval score: 2.3138364218449645.

Word count: 117.

```text
looking at Figure FIGREF16 , we see that, although these approaches do not provide the highest recommendation accuracy, they still result in tag recommendations that are semantically related at a high degree to the expected annotations from the test set. Overall, this suggests that approaches, which provide a poor accuracy performance concerning INLINEFORM4 but provide a good performance regarding semantic similarity could still be helpful for annotating e-books.

Recommendation diversity. Figure FIGREF16 shows the diversity of the tag recommendation approaches. We achieve the highest diversity with the similarity-based approaches, which extract Amazon search terms. Their accuracy is, however, very low. Thus, the combination of the two vocabularies can provide a good trade-off between recommendation accuracy and diversity.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 802.

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

#### Rank 1: qasper-passage-v1-80c3209e389bc991f98f1f41d54f29f5443411e538687fc29f58fe694cf0c90b

Passage ID: `qasper-passage-v1-80c3209e389bc991f98f1f41d54f29f5443411e538687fc29f58fe694cf0c90b`; retrieval score: 5.468310763586937.

Word count: 200.

```text
We compare the proposed approach for translating natural language instructions into a navigation plan against alternative deep-learning models:

[align=left,leftmargin=0em,labelsep=0.4em,font=]

The baseline approach is based on BIBREF20 . It divides the task of interpreting commands for behavioral navigation into two steps: path generation, and path verification. For path generation, this baseline uses a standard sequence-to-sequence model augmented with an attention mechanism, similar to BIBREF23 , BIBREF6 . For path verification, the baseline uses depth-first search to find a route in the graph that matches the sequence of predicted behaviors. If no route matches perfectly, the baseline changes up to three behaviors in the predicted sequence to try to turn it into a valid path.

To test the impact of using the behavioral graphs as an extra input to our translation model, we implemented a version of our approach that only takes natural language instructions as input. In this ablation model, the output of the bidirectional GRU that encodes the input instruction INLINEFORM0 is directly fed to the decoder layer. This model does not have the attention and FC layers described in Sec. SECREF4 , nor uses the masking function in the output layer.

This model is the same as the previous
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-bde4d94b106b92e063a67b7c9c4f3beb89f878e42df1894ec42091b0ed806cd0

Passage ID: `qasper-passage-v1-bde4d94b106b92e063a67b7c9c4f3beb89f878e42df1894ec42091b0ed806cd0`; retrieval score: 5.189908413227222.

Word count: 200.

```text
Table TABREF28 shows the performance of the models considered in our evaluation on both test sets. The next two sections discuss the results in detail.

First, we can observe that the final model “Ours with Mask and Ordered Triplets” outperforms the Baseline and Ablation models on all metrics in previously seen environments. The difference in performance is particularly evident for the Exact Match and Goal Match metrics, with our model increasing accuracy by 35% and 25% in comparison to the Baseline and Ablation models, respectively. These results suggest that providing the behavioral navigation graph to the model and allowing it to process this information as a knowledge base in an end-to-end fashion is beneficial.

We can also observe from Table TABREF28 that the masking function of Eq. ( EQREF12 ) tends to increase performance in the Test-Repeated Set by constraining the output sequence to a valid set of navigation behaviors. For the Ablation model, using the masking function leads to about INLINEFORM0 increase in EM and GM accuracy. For the proposed model (with or without reordering the graph triplets), the increase in accuracy is around INLINEFORM1 . Note that the impact of the masking function is less evident in terms
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1810.00663:10:1` | full | 0:572 |

#### Rank 3: qasper-passage-v1-9b02fc7b1c2185c4c3cb275811f2431466b26eadaf37a8808222a6bb3020d45d

Passage ID: `qasper-passage-v1-9b02fc7b1c2185c4c3cb275811f2431466b26eadaf37a8808222a6bb3020d45d`; retrieval score: 5.08977565677414.

Word count: 200.

```text
This section discusses qualitative results to better understand how the proposed model uses the navigation graph.

We analyze the evolution of the attention weights INLINEFORM0 in Eq. () to assess if the decoder layer of the proposed model is attending to the correct parts of the behavioral graph when making predictions. Fig FIGREF33 (b) shows an example of the resulting attention map for the case of a correct prediction. In the Figure, the attention map is depicted as a scaled and normalized 2D array of color codes. Each column in the array shows the attention distribution INLINEFORM1 used to generate the predicted output at step INLINEFORM2 . Consequently, each row in the array represents a triplet in the corresponding behavioral graph. This graph consists of 72 triplets for Fig FIGREF33 (b).

We observe a locality effect associated to the attention coefficients corresponding to high values (bright areas) in each column of Fig FIGREF33 (b). This suggests that the decoder is paying attention to graph triplets associated to particular neighborhoods of the environment in each prediction step. We include additional attention visualizations in the supplementary Appendix, including cases where the dynamics of the attention distribution are harder to interpret.

All the
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-640e4e9102a58a1a2b13ae4d8178ea2d06e1f00b82d988465c122ba66ce5fb1d

Passage ID: `qasper-passage-v1-640e4e9102a58a1a2b13ae4d8178ea2d06e1f00b82d988465c122ba66ce5fb1d`; retrieval score: 4.7978427221777356.

Word count: 200.

```text
INLINEFORM4 quantifies the affinity between the INLINEFORM5 -th triplet in INLINEFORM6 and the INLINEFORM7 -th word in the corresponding input INLINEFORM8 .

The model then uses each attention distribution INLINEFORM0 to obtain a weighted sum of the encodings of the words in INLINEFORM1 , according to their relevance to the corresponding triplet INLINEFORM2 . This results in L attention vectors INLINEFORM3 , INLINEFORM4 .

The final step in the attention layer concatenates each INLINEFORM0 with INLINEFORM1 to generate the outputs INLINEFORM2 , INLINEFORM3 . Following BIBREF8 , we include the encoded triplet INLINEFORM4 in the output tensor INLINEFORM5 of this layer to prevent early summaries of relevant map information.

FC layer: The model reduces the dimensionality of each individual vector INLINEFORM0 from INLINEFORM1 to INLINEFORM2 with a fully-connected (FC) layer. The resulting L vectors are output to the next layer as columns of a context matrix INLINEFORM3 .

Decoder layer: After the FC layer, the model predicts likelihoods over the sequence of behaviors that correspond to the input instructions with a GRU network. Without loss of generality, consider the INLINEFORM0 -th recurrent cell in the GRU network. This cell takes two inputs: a hidden state vector INLINEFORM1 from the prior
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-a60dc1164afc4c14285202877abb292dd0203c90db57d61fd15a07d7032a2e63

Passage ID: `qasper-passage-v1-a60dc1164afc4c14285202877abb292dd0203c90db57d61fd15a07d7032a2e63`; retrieval score: 4.6354336101436235.

Word count: 200.

```text
mechanism. We use one-way attention because the graph contains information about the whole environment, while the instruction has (potentially incomplete) local information about the route of interest. The use of attention provides our model with a two-step strategy to interpret commands. This resembles the way people find paths on a map: first, relevant parts on the map are selected according to their affinity to each of the words in the input instruction (attention layer); second, the selected parts are connected to assemble a valid path (decoder layer). More formally, let INLINEFORM2 ( INLINEFORM3 ) be the INLINEFORM4 -th row of INLINEFORM5 , and INLINEFORM6 ( INLINEFORM7 ) the INLINEFORM8 -th row of INLINEFORM9 . We use each encoded triplet INLINEFORM10 in INLINEFORM11 to calculate its associated attention distribution INLINEFORM12 over all the atomic instructions INLINEFORM13 : DISPLAYFORM0

where the matrix INLINEFORM0 serves to combine the different sources of information INLINEFORM1 and INLINEFORM2 . Each component INLINEFORM3 of the attention distributions INLINEFORM4 quantifies the affinity between the INLINEFORM5 -th triplet in INLINEFORM6 and the INLINEFORM7 -th word in the corresponding input INLINEFORM8 .

The model then uses each attention distribution INLINEFORM0 to obtain a weighted sum of the encodings of the
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 1000.

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

#### Rank 1: qasper-passage-v1-8ef2a0ca5a2a5798238e496ebf103d5850385a1a3b87740054da2dbe98ad9fee

Passage ID: `qasper-passage-v1-8ef2a0ca5a2a5798238e496ebf103d5850385a1a3b87740054da2dbe98ad9fee`; retrieval score: 8.306361145202823.

Word count: 200.

```text
then randomly sampling the same number of users from the age ranges (11,19] and (19,23]. The average accuracy of this model is 0.63 for depressed users and 0.64 for control class. Table TABREF44 illustrates the performance of gender prediction for each class. The average accuracy is 0.82 on INLINEFORM5 ground-truth dataset.

Prediction with Visual Imagery:

Inspired by BIBREF56 's approach for facial landmark localization, we use their pretrained CNN consisting of convolutional layers, including unshared and fully-connected layers, to predict gender and age from both the profile and shared images. We evaluate the performance for gender and age prediction task on INLINEFORM0 and INLINEFORM1 respectively as shown in Table TABREF42 and Table TABREF44 .

Demographic Prediction Analysis:

We delve deeper into the benefits and drawbacks of each data modality for demographic information prediction. This is crucial as the differences between language cues between age groups above age 35 tend to become smaller (see Figure FIGREF39 -A,B,C) and making the prediction harder for older people BIBREF74 . In this case, the other data modality (e.g., visual content) can play integral role as a complementary source for age inference. For gender prediction (see Table TABREF44 ), on average, the profile image-based predictor
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-1da62828d10983a7c9d0041c599f01954786d9879751ec12ce25163f81f1ba2f

Passage ID: `qasper-passage-v1-1da62828d10983a7c9d0041c599f01954786d9879751ec12ce25163f81f1ba2f`; retrieval score: 7.589707325902419.

Word count: 200.

```text
We now provide an in-depth analysis of visual and textual content of vulnerable users.

Visual Content Analysis: We show that the visual content in images from posts as well as profiles provide valuable psychological cues for understanding a user's depression status. Profile/posted images can surface self-stigmatization BIBREF53 . Additionally, as opposed to typical computer vision framework for object recognition that often relies on thousands of predetermined low-level features, what matters more for assessing user's online behavior is the emotions reflected in facial expressions BIBREF54 , attributes contributing to the computational aesthetics BIBREF55 , and sentimental quotes they may subscribe to (Figure FIGREF15 ) BIBREF8 .

Facial Presence:

For capturing facial presence, we rely on BIBREF56 's approach that uses multilevel convolutional coarse-to-fine network cascade to tackle facial landmark localization. We identify facial presentation, emotion from facial expression, and demographic features from profile/posted images . Table TABREF21 illustrates facial presentation differences in both profile and posted images (media) for depressed and control users in INLINEFORM0 . With control class showing significantly higher in both profile and media (8%, 9% respectively) compared to that for the depressed class. In contrast with age and gender disclosure, vulnerable users are less likely to disclose
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-d5b3ad86264c9a6d846bbc0584ea427ae23faa8b78f7c3478910e79a9bbb6d61

Passage ID: `qasper-passage-v1-d5b3ad86264c9a6d846bbc0584ea427ae23faa8b78f7c3478910e79a9bbb6d61`; retrieval score: 7.277373564262013.

Word count: 169.

```text
harder for older people BIBREF74 . In this case, the other data modality (e.g., visual content) can play integral role as a complementary source for age inference. For gender prediction (see Table TABREF44 ), on average, the profile image-based predictor provides a more accurate prediction for both the depressed and control class (0.92 and 0.90) compared to content-based predictor (0.82). For age prediction (see Table TABREF42 ), textual content-based predictor (on average 0.60) outperforms both of the visual-based predictors (on average profile:0.51, Media:0.53).

However, not every user provides facial identity on his account (see Table TABREF21 ). We studied facial presentation for each age-group to examine any association between age-group, facial presentation and depressive behavior (see Table TABREF43 ). We can see youngsters in both depressed and control class are not likely to present their face on profile image. Less than 3% of vulnerable users between 11-19 years reveal their facial identity. Although content-based gender predictor was not as accurate as image-based one, it is adequate for population-level analysis.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-a121c60c39f74da01395914f9e361333a0a3cf1f0d61b27871c1cb2c9a532222

Passage ID: `qasper-passage-v1-a121c60c39f74da01395914f9e361333a0a3cf1f0d61b27871c1cb2c9a532222`; retrieval score: 5.964411959683169.

Word count: 200.

```text
black bar) shows that the log-odds of prediction is 0.31, that is, the likelihood of this person being a depressed user is 57% (1 / (1 + exp(-0.3))). The figure also sheds light on the impact of each contributing feature. The waterfall charts represent how the probability of being depressed changes with the addition of each feature variable. For instance, the "Analytic thinking" of this user is considered high 48.43 (Median:36.95, Mean: 40.18) and this decreases the chance of this person being classified into the depressed group by the log-odds of -1.41. Depressed users have significantly lower "Analytic thinking" score compared to control class. Moreover, the 40.46 "Clout" score is a low value (Median: 62.22, Mean: 57.17) and it decreases the chance of being classified as depressed. With respect to the visual features, for instance, the mean and the median of 'shared_colorfulness' is 112.03 and 113 respectively. The value of 136.71 would be high; thus, it decreases the chance of being depressed for this specific user by log-odds of -0.54. Moreover, the 'profile_naturalness' of 0.46 is considered high compared to 0.36 as the mean for the depressed class which justifies pull down of the log-odds by INLINEFORM2 . For network
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-4d7131363b16351282160412080f53d352ba284a39a124c8a2bad12fcf1c9f5e

Passage ID: `qasper-passage-v1-4d7131363b16351282160412080f53d352ba284a39a124c8a2bad12fcf1c9f5e`; retrieval score: 5.8763775650516346.

Word count: 200.

```text
We leverage both the visual and textual content for predicting age and gender.

Prediction with Textual Content:

We employ BIBREF73 's weighted lexicon of terms that uses the dataset of 75,394 Facebook users who shared their status, age and gender. The predictive power of this lexica was evaluated on Twitter, blog, and Facebook, showing promising results BIBREF73 . Utilizing these two weighted lexicon of terms, we are predicting the demographic information (age or gender) of INLINEFORM0 (denoted by INLINEFORM1 ) using following equation: INLINEFORM2

where INLINEFORM0 is the lexicon weight of the term, and INLINEFORM1 represents the frequency of the term in the user generated INLINEFORM2 , and INLINEFORM3 measures total word count in INLINEFORM4 . As our data is biased toward young people, we report age prediction performance for each age group separately (Table TABREF42 ). Moreover, to measure the average accuracy of this model, we build a balanced dataset (keeping all the users above 23 -416 users), and then randomly sampling the same number of users from the age ranges (11,19] and (19,23]. The average accuracy of this model is 0.63 for depressed users and 0.64 for control class. Table TABREF44 illustrates the performance of gender prediction for
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 969.

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

#### Rank 1: qasper-passage-v1-88e040351e52744fc99aebdb02f285e91998c30982e21813458bda5eb8fe64c0

Passage ID: `qasper-passage-v1-88e040351e52744fc99aebdb02f285e91998c30982e21813458bda5eb8fe64c0`; retrieval score: 4.573427777696488.

Word count: 177.

```text
E17-1101 showed that given input with author traits like gender, it is possible to retain those traits in Statistical Machine Translation (SMT) models. W17-4727 showed that incorporating morphological analysis in the decoder improves NMT performance for morphologically rich languages. burlot:hal-01618387 presented a new protocol for evaluating the morphological competence of MT systems, indicating that current translation systems only manage to capture some morphological phenomena correctly. Regarding the application of constraints in NMT, N16-1005 presented a method for controlling the politeness level in the generated output. DBLP:journals/corr/FiclerG17aa showed how to guide a neural text generation system towards style and content parameters like the level of professionalism, subjective/objective, sentiment and others. W17-4811 showed that incorporating more context when translating subtitles can improve the coherence of the generated translations. Most closely to our work, vanmassenhove-hardmeier-way:2018:EMNLP also addressed the missing gender information by training proprietary models with a gender-indicating-prefix. We differ from this work by treating the problem in a black-box manner, and by addressing additional information like the number of the speaker and the gender and number of the audience.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-7c59ebe04b83282f905e11e3a87fcb81e70f7be645cf02c38c5b5e38c068c481

Passage ID: `qasper-passage-v1-7c59ebe04b83282f905e11e3a87fcb81e70f7be645cf02c38c5b5e38c068c481`; retrieval score: 3.1608038122345823.

Word count: 102.

```text
Closely related to our work, vanmassenhove-hardmeier-way:2018:EMNLP proposed a method and an English-French test set to evaluate gender-aware translation, based on the Europarl corpus BIBREF7 . We evaluate our method (using Google Translate and the given prefixes) on their test set to see whether it is applicable to another language pair and domain. Table shows the results of our approach vs. their published results and the Google Translate baseline. As may be expected, Google Translate outperforms their system as it is trained on a different corpus and may use more complex machine translation models. Using our method improves the BLEU score even further.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-d20474673be4323fe86eb207420d4b9340d7b2301bf9773c22b231bfdf73560d

Passage ID: `qasper-passage-v1-d20474673be4323fe86eb207420d4b9340d7b2301bf9773c22b231bfdf73560d`; retrieval score: 2.844880402707675.

Word count: 200.

```text
A common way for marking information about gender, number, and case in language is morphology, or the structure of a given word in the language. However, different languages mark such information in different ways – for example, in some languages gender may be marked on the head word of a syntactic dependency relation, while in other languages it is marked on the dependent, on both, or on none of them BIBREF0 . This morphological diversity creates a challenge for machine translation, as there are ambiguous cases where more than one correct translation exists for the same source sentence. For example, while the English sentence “I love language” is ambiguous with respect to the gender of the speaker, Hebrew marks verbs for the gender of their subject and does not allow gender-neutral translation. This allows two possible Hebrew translations – one in a masculine and the other in a feminine form. As a consequence, a sentence-level translator (either human or machine) must commit to the gender of the speaker, adding information that is not present in the source. Without additional context, this choice must be done arbitrarily by relying on language conventions, world knowledge or statistical (stereotypical) knowledge.

Indeed, the English
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-cc2a679ed2915928a400046ad84e17068cbba17014236e4a098d93b15cb90813

Passage ID: `qasper-passage-v1-cc2a679ed2915928a400046ad84e17068cbba17014236e4a098d93b15cb90813`; retrieval score: 2.820357133222313.

Word count: 145.

```text
a black-box NMT system makes the desired morphological decisions according to the given hint, even when no other evidence is available on the source side. While adding those hints results in additional text on the target side, we show that it is simple to remove, leaving only the desired translation.

Our method is appealing as it only requires simple pre-and-post processing of the inputs and outputs, without considering the system internals, or requiring specific annotated data and training procedure as in previous work BIBREF1 . We show that in spite of its simplicity, it is effective in resolving many of the ambiguities and improves the translation quality in up to 2.3 BLEU when given the correct hints, which may be inferred from text metadata or other sources. Finally, we perform a fine-grained syntactic analysis of the translations generated using our method which shows its effectiveness.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-c197b93d02acd1b30bb6a53a1df0faec5f7174e4b7a7c365b0cbe905f6d0aab6

Passage ID: `qasper-passage-v1-c197b93d02acd1b30bb6a53a1df0faec5f7174e4b7a7c365b0cbe905f6d0aab6`; retrieval score: 2.1880082323040684.

Word count: 200.

```text
To demonstrate our method in a black-box setting, we focus our experiments on Google's machine translation system (GMT), accessed through its Cloud API. To test the method on real-world sentences, we consider a monologue from the stand-up comedy show “Sarah Silverman: A Speck of Dust”. The monologue consists of 1,244 English sentences, all by a female speaker conveyed to a plural, gender-neutral audience. Our parallel corpora consists of the 1,244 English sentences from the transcript, and their corresponding Hebrew translations based on the Hebrew subtitles. We translate the monologue one sentence at a time through the Google Cloud API. Eyeballing the results suggest that most of the translations use the incorrect, but default, masculine and singular forms for the speaker and the audience, respectively. We expect that by adding the relevant condition of “female speaking to an audience” we will get better translations, affecting both the gender of the speaker and the number of the audience.

To verify this, we experiment with translating the sentences with the following variations: No Prefix—The baseline translation as returned by the GMT system. “He said:”—Signaling a male speaker. We expect to further skew the system towards masculine forms. “She said:”—Signaling a female speaker and
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1903.03467:3:0` | full | 0:1005 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 824.

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

#### Rank 1: qasper-passage-v1-f9cb0b85457f9a835926e944d20010b3c2bccec7c421ed788b9d9b2c63ddfb4b

Passage ID: `qasper-passage-v1-f9cb0b85457f9a835926e944d20010b3c2bccec7c421ed788b9d9b2c63ddfb4b`; retrieval score: 8.185063373432754.

Word count: 150.

```text
Another major performance concern in distributed computing is network bandwidth. Since the experts are stationary (see above) and the number of gating parameters is small, most of the communication involves sending the inputs and outputs of the experts across the network. To maintain computational efficiency, the ratio of an expert's computation to the size of its input and output must exceed the ratio of computational to network capacity of the computing device. For GPUs, this may be thousands to one. In our experiments, we use experts with one hidden layer containing thousands of RELU-activated units. Since the weight matrices in the expert have sizes INLINEFORM0 _ INLINEFORM1 _ INLINEFORM2 and INLINEFORM3 _ INLINEFORM4 _ INLINEFORM5 , the ratio of computation to input and output is equal to the size of the hidden layer. Conveniently, we can increase computational efficiency simply by using a larger hidden layer, or more hidden layers.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-4d3a411c763e7b25aab41ef16310a64953d875709e4a48562a72a70800896a85

Passage ID: `qasper-passage-v1-4d3a411c763e7b25aab41ef16310a64953d875709e4a48562a72a70800896a85`; retrieval score: 7.965170393888478.

Word count: 159.

```text
If the number of experts is very large, we can reduce the branching factor by using a two-level hierarchical MoE. In a hierarchical MoE, a primary gating network chooses a sparse weighted combination of “experts", each of which is itself a secondary mixture-of-experts with its own gating network. If the hierarchical MoE consists of INLINEFORM0 groups of INLINEFORM1 experts each, we denote the primary gating network by INLINEFORM2 , the secondary gating networks by INLINEFORM3 , and the expert networks by INLINEFORM4 . The output of the MoE is given by: DISPLAYFORM0

Our metrics of expert utilization change to the following: DISPLAYFORM0 DISPLAYFORM1

INLINEFORM0 and INLINEFORM1 deonte the INLINEFORM2 functions for the primary gating network and INLINEFORM3 secondary gating network respectively. INLINEFORM4 denotes the subset of INLINEFORM5 for which INLINEFORM6 .

It would seem simpler to let INLINEFORM0 , but this would not have a gradient with respect to the primary gating network, so we use the formulation above.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-2eb539e4c3732d8b800084fc40300cdf9b531f0d31c0beee7ef62e4c0903bba3

Passage ID: `qasper-passage-v1-2eb539e4c3732d8b800084fc40300cdf9b531f0d31c0beee7ef62e4c0903bba3`; retrieval score: 7.731760961681728.

Word count: 140.

```text
up to thousands of experts, but only need to evaluate a handful of them for every example. If the number of experts is very large, we can reduce the branching factor by using a two-level hierarchical MoE. In a hierarchical MoE, a primary gating network chooses a sparse weighted combination of “experts", each of which is itself a secondary mixture-of-experts with its own gating network. In the following we focus on ordinary MoEs. We provide more details on hierarchical MoEs in Appendix SECREF60 .

Our implementation is related to other models of conditional computation. A MoE whose experts are simple weight matrices is similar to the parameterized weight matrix proposed in BIBREF12 . A MoE whose experts have one hidden layer is similar to the block-wise dropout described in BIBREF13 , where the dropped-out layer is sandwiched between fully-activated layers.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-4c023175c22660861e8b6c7964a72cea689b4508dca4dc81dd9d7bd00baf87f8

Passage ID: `qasper-passage-v1-4c023175c22660861e8b6c7964a72cea689b4508dca4dc81dd9d7bd00baf87f8`; retrieval score: 7.357792915338354.

Word count: 200.

```text
As discussed in section SECREF4 , for load-balancing purposes, we want to define an additional loss function to encourage experts to receive roughly equal numbers of training examples. Unfortunately, the number of examples received by an expert is a discrete quantity, so it can not be used in back-propagation. Instead, we define a smooth estimator INLINEFORM0 of the number of examples assigned to each expert for a batch INLINEFORM1 of inputs. The smoothness allows us to back-propagate gradients through the estimator. This is the purpose of the noise term in the gating function. We define INLINEFORM2 as the probability that INLINEFORM3 is nonzero, given a new random choice of noise on element INLINEFORM4 , but keeping the already-sampled choices of noise on the other elements. To compute INLINEFORM5 , we note that the INLINEFORM6 is nonzero if and only if INLINEFORM7 is greater than the INLINEFORM8 -greatest element of INLINEFORM9 excluding itself. The probability works out to be: DISPLAYFORM0

Where INLINEFORM0 means the kth highest component of INLINEFORM1 , excluding component INLINEFORM2 . Simplifying, we get: DISPLAYFORM0

Where INLINEFORM0 is the CDF of the standard normal distribution. DISPLAYFORM0

We can now define the load loss to be the square of
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-edcdcdc9f56bf68f4dc684133bbd5992fb9769e9f4bd0c58340631e4df30fc7f

Passage ID: `qasper-passage-v1-edcdcdc9f56bf68f4dc684133bbd5992fb9769e9f4bd0c58340631e4df30fc7f`; retrieval score: 7.2834773457673645.

Word count: 173.

```text
Our approach to conditional computation is to introduce a new type of general purpose neural network component: a Sparsely-Gated Mixture-of-Experts Layer (MoE). The MoE consists of a number of experts, each a simple feed-forward neural network, and a trainable gating network which selects a sparse combination of the experts to process each input (see Figure FIGREF8 ). All parts of the network are trained jointly by back-propagation.

While the introduced technique is generic, in this paper we focus on language modeling and machine translation tasks, which are known to benefit from very large models. In particular, we apply a MoE convolutionally between stacked LSTM layers BIBREF15 , as in Figure FIGREF8 . The MoE is called once for each position in the text, selecting a potentially different combination of experts at each position. The different experts tend to become highly specialized based on syntax and semantics (see Appendix SECREF84 Table TABREF92 ). On both language modeling and machine translation benchmarks, we improve on best published results at a fraction of the computational cost.
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

#### Rank 1: qasper-passage-v1-95785d43f39a15294c1e1d25eb5101d5585fd87254213666ab3aa5ad314cf0c5

Passage ID: `qasper-passage-v1-95785d43f39a15294c1e1d25eb5101d5585fd87254213666ab3aa5ad314cf0c5`; retrieval score: 6.825401360662422.

Word count: 117.

```text
TABREF43 . The models incorporating attention-based opinion summary (i.e., OURS and OURS w/o THA & STN) can better determine if the commonly-used nouns are aspect terms or not (e.g. “device” in the first input), since they make decisions based on the global opinion information. Besides, they are able to extract some infrequent or even misspelled aspect terms (e.g. “survice” in the second input) based on the indicative clues provided by opinion words. For the last three cases, having aspects in coordinate structures (i.e. the third and the fourth) or long aspects (i.e. the fifth), our model can give precise predictions owing to the previous detection clues captured by THA. Without using these clues, the baseline models fail.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-bc4ec4dcc9d44e3b8ad3dd3a3fc89b13953170c524d4e7bd3ef564779cedda14

Passage ID: `qasper-passage-v1-bc4ec4dcc9d44e3b8ad3dd3a3fc89b13953170c524d4e7bd3ef564779cedda14`; retrieval score: 5.830255213988551.

Word count: 200.

```text
In Figure FIGREF41 , we visualize the opinion attention scores of the words in two example sentences with the candidate aspects “maitre-D” and “bathroom”. The scores in Figures FIGREF41 and FIGREF41 show that our full model captures the related opinion words very accurately with significantly larger scores, i.e. “incredibly”, “unwelcoming” and “arrogant” for “maitre-D”, and “unfriendly” and “filthy” for “bathroom”. “OURS w/o STN” directly applies attention over the opinion hidden states INLINEFORM0 's, similar to what CMLA does. As shown in Figure FIGREF41 , it captures some unrelated opinion words (e.g. “fine”) and even some non-opinionated words. As a result, it brings in some noise into the global opinion summary, and consequently the final prediction accuracy will be affected. This example demonstrates that the proposed STN works pretty well to help attend to more related opinion words given a particular aspect.

Some predictions of our model and those of LSTM and OURS w/o THA & STN are given in Table TABREF43 . The models incorporating attention-based opinion summary (i.e., OURS and OURS w/o THA & STN) can better determine if the commonly-used nouns are aspect terms or not (e.g. “device” in the first input), since they make decisions based on
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-4033450e17842414c6f584f6da610a2e9bf903c349c8d142aace9e54d51e262e

Passage ID: `qasper-passage-v1-4033450e17842414c6f584f6da610a2e9bf903c349c8d142aace9e54d51e262e`; retrieval score: 4.662645885939768.

Word count: 200.

```text
As shown in Table TABREF39 , the proposed framework consistently obtains the best scores on all of the four datasets. Compared with the winning systems of SemEval ABSA, our framework achieves 5.0%, 1.6%, 1.4%, 1.3% absolute gains on INLINEFORM0 , INLINEFORM1 , INLINEFORM2 and INLINEFORM3 respectively.

Our framework can outperform RNCRF, a state-of-the-art model based on dependency parsing, on all datasets. We also notice that RNCRF does not perform well on INLINEFORM0 and INLINEFORM1 (3.7% and 3.9% inferior than ours). We find that INLINEFORM2 and INLINEFORM3 contain many informal reviews, thus RNCRF's performance degradation is probably due to the errors from the dependency parser when processing such informal texts.

CMLA and MIN do not rely on dependency parsing, instead, they employ attention mechanism to distill opinion information to help aspect extraction. Our framework consistently performs better than them. The gains presumably come from two perspectives: (1) In our model, the opinion summary is exploited after performing the selective transformation conditioned on the current aspect features, thus the summary can to some extent avoid the noise due to directly applying conventional attention. (2) Our model can discover some uncommon aspects under the guidance of some commonly-used aspects in coordinate structures by
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-e8f6b5b45ef674266a8c5ec85483255049e375a807f5559a3fbf4cab845ddcd9

Passage ID: `qasper-passage-v1-e8f6b5b45ef674266a8c5ec85483255049e375a807f5559a3fbf4cab845ddcd9`; retrieval score: 4.3096803044957115.

Word count: 115.

```text
For more accurate aspect term extraction, we explored two important types of information, namely aspect detection history, and opinion summary. We design two components, i.e. truncated history attention, and selective transformation network. Experimental results show that our model dominates those joint extraction works such as RNCRF and CMLA on the performance of ATE. It suggests that the joint extraction sacrifices the accuracy of aspect prediction, although the ground-truth opinion words were annotated by these authors. Moreover, one should notice that those joint extraction methods do not care about the correspondence between the extracted aspect terms and opinion words. Therefore, the necessity of such joint extraction should be obelized, given the experimental findings in this paper.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-0fc85fd46e778739649aac59ca54afc754f93b7870ec2f0fe186d56c3964f0b6

Passage ID: `qasper-passage-v1-0fc85fd46e778739649aac59ca54afc754f93b7870ec2f0fe186d56c3964f0b6`; retrieval score: 4.30177426449772.

Word count: 200.

```text
Aspect-Based Sentiment Analysis (ABSA) involves detecting opinion targets and locating opinion indicators in sentences in product review texts BIBREF0 . The first sub-task, called Aspect Term Extraction (ATE), is to identify the phrases targeted by opinion indicators in review sentences. For example, in the sentence “I love the operating system and preloaded software”, the words “operating system” and “preloaded software” should be extracted as aspect terms, and the sentiment on them is conveyed by the opinion word “love”. According to the task definition, for a term/phrase being regarded as an aspect, it should co-occur with some “opinion words” that indicate a sentiment polarity on it BIBREF1 .

Many researchers formulated ATE as a sequence labeling problem or a token-level classification problem. Traditional sequence models such as Conditional Random Fields (CRFs) BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 , Long Short-Term Memory Networks (LSTMs) BIBREF6 and classification models such as Support Vector Machine (SVM) BIBREF7 have been applied to tackle the ATE task, and achieved reasonable performance. One drawback of these existing works is that they do not exploit the fact that, according to the task definition, aspect terms should co-occur with opinion-indicating words. Thus, the above methods tend to output
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 832.

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

#### Rank 1: qasper-passage-v1-2a7e11053aa3180d7faa223af31245608bd9d55158fa28b3da6be1c561e0cbab

Passage ID: `qasper-passage-v1-2a7e11053aa3180d7faa223af31245608bd9d55158fa28b3da6be1c561e0cbab`; retrieval score: 3.3404284186523827.

Word count: 138.

```text
Here we use network and text analysis tools to compare causal attribution networks (Sec. "Comparing causal networks" ). Crucially, nodes in these networks are defined only by their written descriptions, and multiple written descriptions can represent the same conceptual entity. Thus, to understand how causal attribution networks can be combined, we introduce and analyze a method for fusing networks (Sec. "Fusing causal networks" ) that builds off both the network structure and associated text information and explicitly incorporates conceptual equivalencies. Lastly, in Sec. "Inferring the size of the causal attribution network" we use the degree of overlap in these networks as a means to infer the total size of the one underlying causal attribution network being explored by these data collection efforts, allowing us to better understand the size of collective space of cause-effect relationships held by humans.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-3cb8b18ae13cb7548b5006d5f1bdb9fc19c1665c93deaf52195c9c2f4414abee

Passage ID: `qasper-passage-v1-3cb8b18ae13cb7548b5006d5f1bdb9fc19c1665c93deaf52195c9c2f4414abee`; retrieval score: 3.3332491435051033.

Word count: 200.

```text
We perform a descriptive analysis of the three datasets, comparing and contrasting their features and properties. We focus on two aspects, the network structure and the text information (the written descriptions associated with each node in the network). Understanding these data at these levels can inform efforts to combine different causal attribution networks (Sec. "Fusing causal networks" ).

Table 1 and Fig. 2 summarize network characteristics for the three causal attribution networks. We focus on standard measures of network structure, measuring the sizes, densities, motif structure, and connectedness of the three networks. Both Wikidata and ConceptNet, the two larger networks, are highly disconnected, amounting to collections of small components with low density. In contrast, IPRnet is smaller but comparatively more dense and connected, with higher average degree, fewer disconnected components, and more clustering (Table 1 ). All three networks are degree dissortative, meaning that high-degree nodes are more likely to connect to low-degree nodes. For connectedness and path lengths, we consider both directed and undirected versions of the network allowing us to measure strong and weak connectivity, respectively. All three networks are well connected when ignoring link directionality, but few directed paths exist between disparate nodes in Wikidata and ConceptNet,
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-9a4ec799055a64ae42123d0fe8c4e96252ee8fde9d1c8d21b5722e8da3332040

Passage ID: `qasper-passage-v1-9a4ec799055a64ae42123d0fe8c4e96252ee8fde9d1c8d21b5722e8da3332040`; retrieval score: 3.170956728698331.

Word count: 200.

```text
These causal attributions networks are separate efforts to map out the underlying or latent causal attribution network held collectively by humans. It is natural to then ask if these different efforts can be combined in an effective way. Fusing these networks together can provide a single causal attribution network for researchers to study.

At the most basic level, one can fuse these networks together simply by taking their union, defining a single network containing all the unique nodes and edges of the original networks. Unfortunately, nodes in these networks are identified by their sentences, and this graph union assumes that two nodes $i$ and $j$ are equivalent iff $s_i = s_j$ . This is overly restrictive as these sentences serve as descriptions of associated concepts, and we ideally want to combine nodes that represent the same concept even when their written descriptions differ. Indeed, even within a single network it can be necessary to identify and combine nodes in this way. We identify this problem as graph fusion. Graph fusion is a type of record linkage problem and is closely related to graph alignment and (inexact) graph matching BIBREF27 , but unlike those problems, graph fusion assumes the need to
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-80876635fd1995a7d35e8b76f5644d8a8b715bb662b5d578b671e49bd585bc3e

Passage ID: `qasper-passage-v1-80876635fd1995a7d35e8b76f5644d8a8b715bb662b5d578b671e49bd585bc3e`; retrieval score: 3.059337895580387.

Word count: 200.

```text
The construction of causal attribution networks generates important knowledge networks that may inform causal inference research and even help future AI systems to perform causal reasoning, but these networks are time-consuming and costly to generate, and to date no efforts have been made to combine different networks. Our work not only studies the potential for fusing different networks together, but also infers the overall size of the total causal attribution network being explored.

We used capture-recapture estimators to infer the number of nodes and links in the underlying causal attribution network, given the Wikidata and ConceptNet networks and using NetFUSES and a semantic similarity function to help account for semantically equivalent nodes within and between Wikidata and ConceptNet. The validity of these estimates depends on Wikidata and ConceptNet being independent samples of the underlying network. As with many practical applications of capture-recapture in wildlife ecology and other areas, here we must question how well this independence assumption holds. The best way to sharpen these estimates is to introduce a new causal attribution survey specifically designed to capture either nodes or links independently (it is unlikely that a single survey protocol can sample independently both nodes and links), and then perform
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-1d945388f2cefa9a2b2d0048355767ec7e853a4cbae533a7fd3fc80def44dd5d

Passage ID: `qasper-passage-v1-1d945388f2cefa9a2b2d0048355767ec7e853a4cbae533a7fd3fc80def44dd5d`; retrieval score: 2.929170172074344.

Word count: 200.

```text
in the written descriptions of two nodes means the nodes are different. Yet, written descriptions can easily represent the same conceptual entity in a variety of ways, leading to equivalent nodes that do not have equal written descriptions. Therefore we repeated the above estimation procedure using Wikidata and ConceptNet networks after applying NetFUSES (Sec. "Fusing causal networks" ). NetFUSES incorporates natural language information directly into the semantic similarity, allowing us to incorporate, to some extent, natural language information into our node comparison.

Applying the fusion analysis of Sec. "Fusing causal networks" and combining equivalent nodes within the fused Wikidata and ConceptNet, networks, then determining whether fused nodes contain nodes from both original networks to compute the overlap in the two networks, we obtain a new estimate of the underlying causal attribution network size of $\hat{N} = 293\,819.0 \pm 39\,727.3$ . This estimate is smaller than our previous, stricter estimate, as expected due to the fusion procedure, but within the previous estimate's margin of error. Again, comparing this estimate to the size of the union of the fused Wikidata and ConceptNet networks implies that the experiments have explored approximately 5.77% $\pm $ 0.781% of the underlying or latent causal attribution network.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 938.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "9a696b810674778566b40332d9c70845193d44d3": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1812.06038:0:0": [
        [
          0,
          515
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-0688674355ac652df300c69903b9ac741f6a75d6365bc150cf066df6c95e99fc

Passage ID: `qasper-passage-v1-0688674355ac652df300c69903b9ac741f6a75d6365bc150cf066df6c95e99fc`; retrieval score: 5.303692319898355.

Word count: 86.

```text
We established strong baselines for two story narrative understanding datasets: CaTeRS and RED. We have shown that neural network-based models can outperform feature-based models with wide margins, and we conducted an ablation study to show that contextualized representation learning can boost performance of NN models. Further research can focus on more systematic study or build stronger NN models over the same datasets used in this work. Exploring possibilities to directly apply temporal relation extraction to enhance performance of story generation systems is another promising research direction.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-f9695094c0fd093b7b436ba8c2dc56daa69932db55fa0793557d15ddbe91ebf0

Passage ID: `qasper-passage-v1-f9695094c0fd093b7b436ba8c2dc56daa69932db55fa0793557d15ddbe91ebf0`; retrieval score: 4.856882147583593.

Word count: 126.

```text
The series of TempEval competitions BIBREF21 , BIBREF22 , BIBREF23 have attracted many research interests in predicting event temporal relations. Early attempts by BIBREF24 , BIBREF21 , BIBREF25 , BIBREF26 only use pair-wise classification models. State-of-the-art local methods, such as ClearTK BIBREF27 , UTTime BIBREF28 , and NavyTime BIBREF29 improve on earlier work by feature engineering with linguistic and syntactic rules. As we mention in the Section 2, CAEVO is the current state-of-the-art system for feature-based temporal event relation extraction BIBREF10 . It's widely used as the baseline for evaluating TB-Dense data. We adopt it as our baseline for evaluating CaTeRS and RED datasets. Additionally, several models BramsenDLB2006, ChambersJ2008, DoLuRo12, NingWuRo18, P18-1212 have successfully incorporated global inference to impose global prediction consistency such as temporal transitivity.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.11942:6:0` | full | 0:912 |

#### Rank 3: qasper-passage-v1-cfb69bcade0fa6bf97095c20002fc77e5d95404fdb34c05171ed55dc6bc62076

Passage ID: `qasper-passage-v1-cfb69bcade0fa6bf97095c20002fc77e5d95404fdb34c05171ed55dc6bc62076`; retrieval score: 4.489406580660744.

Word count: 69.

```text
Table TABREF25 contains the best hyper-parameters and Table TABREF26 contains micro-average F1 scores for both datasets on dev and test sets. We only consider positive pairs, i.e. correct predictions on NONE pairs are excluded for evaluation. In general, the baseline model CAEVO is outperformed by both NN models, and NN model with BERT embedding achieves the greatest performance. We now provide more detailed analysis and discussion for each dataset.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-58f6928898cb162c36e2bb25c606d72424e6ca91360e5fa8096ce77510b7530d

Passage ID: `qasper-passage-v1-58f6928898cb162c36e2bb25c606d72424e6ca91360e5fa8096ce77510b7530d`; retrieval score: 3.323551162059889.

Word count: 181.

```text
by annotating 320 five-sentence stories sampled from ROCStories BIBREF7 dataset. RED BIBREF9 contains annotations of rich relations between event pairs for storyline understanding, including co-reference and partial co-reference relations, temporal; causal, and sub-event relations.

Despite multiple productive research threads on temporal and causal relation modeling among events BIBREF10 , BIBREF11 , BIBREF12 and event relation annotation for story understanding BIBREF8 , the intersection of these two threads seems flimsy. To the best of our knowledge, no event relation extraction results have been reported on CaTeRS and RED.

We apply neural network models that leverage recent advances in contextualized embeddings (BERT BIBREF13 ) to event-event relation extraction tasks for CaTeRS and RED. Our goal in this paper is to increase understanding of how well the state-of-the-art event relation models work for story/narrative comprehension.

In this paper, we report the first results of event temporal relation extraction on two under-explored story comprehension datasets: CaTeRS and RED. We establish strong baselines with neural network models enhanced by recent breakthrough of contextualized embeddings, BERT BIBREF13 . We summarize the contributions of the paper as follows:
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-2230767bf9344b49e1a41b8724d698df63157336d52dc5c8c766632d3d1fd271

Passage ID: `qasper-passage-v1-2230767bf9344b49e1a41b8724d698df63157336d52dc5c8c766632d3d1fd271`; retrieval score: 3.0015612026732548.

Word count: 200.

```text
is created by annotating 1600 sentences of 320 five-sentence stories sampled from ROCStories BIBREF7 dataset. CaTeRS contains both temporal and causal relations in an effort to understand and predict commonsense relations between events.

As demonstrated in Table TABREF16 , we split all stories into 220 training and 80 test. We do not construct the development set because the dataset is small. Note that some relations have compounded labels such as “CAUSE_BEFORE”, “ENABLE_BEFORE”, etc. We only take the temporal portion of the annotations.

annotates a wide range of relations of event pairs including their coreference and partial coreference relations, and temporal, causal and subevent relationships. We split data according to the standard train, development, test sets, and only focus on the temporal relations.

The common issue of these two datasets is that they are not densely annotated – not every pair of events is annotated with a relation. We provide one way to handle negative (unannotated) pairs in this paper. When constructing negative examples, we take all event pairs that occur within the same or neighboring sentences with no annotations, labeling them as “NONE”. The negative to positive samples ratio is 1.00 and 11.5 for CaTeRS and RED respectively. Note that
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 662.

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

#### Rank 1: qasper-passage-v1-ffa829c6f7bbf6594e4c38c8518896e80711feb61c8284d1c971efcaeba1462d

Passage ID: `qasper-passage-v1-ffa829c6f7bbf6594e4c38c8518896e80711feb61c8284d1c971efcaeba1462d`; retrieval score: 7.271753397099097.

Word count: 149.

```text
For low resource languages, parallel data may not be available. In this case, we rely only on monolingual data (e.g., Wikipedias). We estimate word translation probabilities from word embeddings of the two languages. Word vectors of these languages can be learned using fastText BIBREF14 and then are aligned into a shared space with English BIBREF15, BIBREF16. Unlike learning contextualized representations, learning word vectors is fast and computationally cheap. Given the aligned vectors $\bar{}_f$ of foreign and $\bar{}_e$ of English, we calculate the word translation matrix $\in ^{|V_f|\times |V_e|}$ as

Here, we use $\mathrm {sparsemax}$ BIBREF17 instead of softmax. Sparsemax is a sparse version of softmax and it puts zero probabilities on most of the word in the English vocabulary except few English words that are similar to a given foreign word. This property is desirable in our approach since it leads to a better initialization of the foreign embeddings.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-92730e124c19a6bc327b5eac965798c7986224c30cd12d84a7f7cb7cad15e2ca

Passage ID: `qasper-passage-v1-92730e124c19a6bc327b5eac965798c7986224c30cd12d84a7f7cb7cad15e2ca`; retrieval score: 6.38876201619256.

Word count: 200.

```text
Pre-trained models BIBREF0, BIBREF1 have received much of attention recently thanks to their impressive results in many down stream NLP tasks. Additionally, multilingual pre-trained models enable many NLP applications for other languages via zero-short cross-lingual transfer. Zero-shot cross-lingual transfer has shown promising results for rapidly building applications for low resource languages. BIBREF2 show the potential of multilingual-BERT BIBREF0 in zero-shot transfer for a large number of languages from different language families on five NLP tasks, namely, natural language inference, document classification, named entity recognition, part-of-speech tagging, and dependency parsing.

Although multilingual models are an important ingredient for enhancing language technology in many languages, recent research on improving pre-trained models puts much emphasis on English BIBREF3, BIBREF4, BIBREF5. The current state of affairs makes it difficult to translate advancements in pre-training from English to non-English languages. To our best knowledge, there are only three available multilingual pre-trained models to date: (1) the multilingual-BERT (mBERT) that supports 104 languages, (2) cross-lingual language model BIBREF6 that supports 100 languages, and (3) Language Agnostic SEntence Representations BIBREF7 that supports 93 languages. Among the three models, LASER is based on neural machine translation approach and strictly requires parallel data to train.

Do multilingual models always
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-df7345c10a45b98fa7ec14709ee5831cfc705cc8b315876eba4e90a46728030b

Passage ID: `qasper-passage-v1-df7345c10a45b98fa7ec14709ee5831cfc705cc8b315876eba4e90a46728030b`; retrieval score: 6.248516294398148.

Word count: 200.

```text
We evaluate our approach for six target languages: French (fr), Russian (ru), Arabic (ar), Chinese (zh), Hindi (hi), and Vietnamese (vi). These languages belong to four different language families. French, Russian, and Hindi are Indo-European languages, similar to English. Arabic, Chinese, and Vietnamese belong to Afro-Asiatic, Sino-Tibetan, and Austro-Asiatic family respectively. The choice of the six languages also reflects different training conditions depending on the amount of monolingual data. French and Russian, and Arabic can be regarded as high resource languages whereas Hindi has far less data and can be considered as low resource.

For experiments that use parallel data to initialize foreign specific parameters, we use the same datasets in the work of BIBREF6. Specifically, we use United Nations Parallel Corpus BIBREF18 for en-ru, en-ar, en-zh, and en-fr. We collect en-hi parallel data from IIT Bombay corpus BIBREF19 and en-vi data from OpenSubtitles 2018. For experiments that use only monolingual data to initialize foreign parameters, instead of training word-vectors from the scratch, we use the pre-trained word vectors from fastText BIBREF14 to estimate word translation probabilities (Eq. DISPLAY_FORM13). We align these vectors into a common space using orthogonal Procrustes BIBREF20, BIBREF15, BIBREF16. We only use identical words between the
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2002.07306:8:0` | full | 0:649 |

#### Rank 4: qasper-passage-v1-ebe2bdf7752cefb50e609d0c858b61ce1b44fd937a5b7331b965a8ed58db33de

Passage ID: `qasper-passage-v1-ebe2bdf7752cefb50e609d0c858b61ce1b44fd937a5b7331b965a8ed58db33de`; retrieval score: 5.343732329663534.

Word count: 200.

```text
Table TABREF32 shows the XNLI test accuracy. For reference, we also include the scores from the previous work, notably the state-of-the-art system XLM BIBREF6. Before discussing the results, we spell out that the fairest comparison in this experiment is the comparison between mBERT and RAMEN$_{\textsc {base}}$+BERT trained with monolingual only.

We first discuss the transfer results from BERT. Initialized from fastText vectors, RAMEN$_{\textsc {base}}$ slightly outperforms mBERT by 1.9 points on average and widen the gap of 3.3 points on Arabic. RAMEN$_{\textsc {base}}$ gains extra 0.8 points on average when initialized from parallel data. With triple number of parameters, RAMEN$_{\textsc {large}}$ offers an additional boost in term of accuracy and initialization with parallel data consistently improves the performance. It has been shown that BERT$_{\textsc {large}}$ significantly outperforms BERT$_{\textsc {base}}$ on 11 English NLP tasks BIBREF0, the strength of BERT$_{\textsc {large}}$ also shows up when adapted to foreign languages.

Transferring from RoBERTa leads to better zero-shot accuracies. With the same initializing condition, RAMEN$_{\textsc {base}}$+RoBERTa outperforms RAMEN$_{\textsc {base}}$+BERT on average by 2.9 and 2.3 points when initializing from monolingual and parallel data respectively. This result show that with similar number of parameters, our approach benefits from a better English pre-trained model. When
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-17f124b6bf70233b2da068d6fa8471d71c4b974a3ce857f6ed7cfb43ff834ed7

Passage ID: `qasper-passage-v1-17f124b6bf70233b2da068d6fa8471d71c4b974a3ce857f6ed7cfb43ff834ed7`; retrieval score: 3.7587830333388146.

Word count: 200.

```text
We evaluate the performance of RAMEN+RoBERTa$_{\textsc {base}}$ (initialized from monolingual data) at each training steps: initialization of word embeddings (0K update), fine-tuning target embeddings (25K), and fine-tuning the model on both English and target language (at each 25K updates). The results are presented in Figure FIGREF40.

Without fine-tuning, the average accuracy of XLNI is 39.7% for a three-ways classification task, and the average LAS score is 3.6 for dependency parsing. We see the biggest leap in the performance after 50K updates. While semantic similarity task profits significantly at 25K updates of the target embeddings, syntactic task benefits with further fine-tuning the encoder. This is expected since the target languages might exhibit different syntactic structures than English and fine-tuning encoder helps to capture language specific structures. We observe a substantial gain of 19-30 LAS for all languages except French after 50K updates.

Language similarities have more impact on transferring syntax than semantics. Without tuning the English encoder, French enjoys 50.3 LAS for being closely related to English, whereas Arabic and Hindi, SOV languages, modestly reach 4.2 and 6.4 points using the SVO encoder. Although Chinese has SVO order, it is often seen as head-final while English is strong head-initial. Perhaps, this
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 949.

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

#### Rank 1: qasper-passage-v1-5340ceb024a5c089a7b801dcf630a94ac9d23ebb98d8d0949f093fc4e3162679

Passage ID: `qasper-passage-v1-5340ceb024a5c089a7b801dcf630a94ac9d23ebb98d8d0949f093fc4e3162679`; retrieval score: 5.57439081161227.

Word count: 104.

```text
this work we investigate how automatic processing of ultrasound tongue imaging is affected by speaker variation, and how severe degradations in performance can be avoided when applying systems to data from previously unseen speakers through the use of speaker adaptation and speaker normalization approaches.

Below, we present the main challenges associated with the automatic processing of ultrasound data, together with a review of speaker-independent models applied to UTI. Following this, we present the experiments that we have performed (Section SECREF2 ), and discuss the results obtained (Section SECREF3 ). Finally we propose some future work and conclude the paper (Sections SECREF4 and SECREF5 ).
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-0c30f7fd8890e0dc23a6845e0a7df2f2c359115e1941099dbb20323406eee1a8

Passage ID: `qasper-passage-v1-0c30f7fd8890e0dc23a6845e0a7df2f2c359115e1941099dbb20323406eee1a8`; retrieval score: 5.331423453534349.

Word count: 200.

```text
BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 . Similarly, ultrasound images of the tongue have been used for direct estimation of acoustic parameters for speech synthesis BIBREF13 , BIBREF14 , BIBREF15 .

Speech and language therapists (SLTs) have found UTI to be very useful in speech therapy. In this work we explore the automatic processing of ultrasound tongue images in order to assist SLTs, who currently largely rely on manual processing when using articulatory imaging in speech therapy. One task that could assist SLTs is the automatic classification of tongue shapes from raw ultrasound. This can facilitate the diagnosis and treatment of speech sound disorders, by allowing SLTs to automatically identify incorrect articulations, or by quantifying patient progress in therapy. In addition to being directly useful for speech therapy, the classification of tongue shapes enables further understanding of phonetic variability in ultrasound tongue images. Much of the previous work in this area has focused on speaker-dependent models. In this work we investigate how automatic processing of ultrasound tongue imaging is affected by speaker variation, and how severe degradations in performance can be avoided when applying systems to data from previously unseen speakers through the use of speaker adaptation
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-e80727dc6d6c71456c112efef7f06a579e6d051fa3282bb089c1bd13aa2e60c0

Passage ID: `qasper-passage-v1-e80727dc6d6c71456c112efef7f06a579e6d051fa3282bb089c1bd13aa2e60c0`; retrieval score: 5.260628152036508.

Word count: 158.

```text
We use the Ultrax Typically Developing dataset (UXTD) from the publicly available UltraSuite repository BIBREF19 . This dataset contains synchronized acoustic and ultrasound data from 58 typically developing children, aged 5-12 years old (31 female, 27 male). The data was aligned at the phone-level, according to the methods described in BIBREF19 , BIBREF25 . For this work, we discarded the acoustic data and focused only on the B-Mode ultrasound images capturing a midsaggital view of the tongue. The data was recorded using an Ultrasonix SonixRP machine using Articulate Assistant Advanced (AAA) software at INLINEFORM0 121fps with a 135 field of view. A single ultrasound frame consists of 412 echo returns from each of the 63 scan lines (63x412 raw frames). For this work, we only use UXTD type A (semantically unrelated words, such as pack, tap, peak, tea, oak, toe) and type B (non-words designed to elicit the articulation of target phones, such as apa, eepee, opo) utterances.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1907.01413:3:0` | full | 0:986 |

#### Rank 4: qasper-passage-v1-985381ad812ab7b2a5e97ac530832cdd31fca0cd32012256c97a174c653f6ca6

Passage ID: `qasper-passage-v1-985381ad812ab7b2a5e97ac530832cdd31fca0cd32012256c97a174c653f6ca6`; retrieval score: 3.8257466971223284.

Word count: 131.

```text
set, hyperparameters such learning rate, decay rate, and L2 weight vary depending on the input format (Raw, PCA, or DCT). Generally, Raw inputs work better with smaller learning rates and heavier regularization to prevent overfitting to the high-dimensional data. As a second classifier to evaluate, we use convolutional neural networks (CNNs) with 2 convolutional and max pooling layers, followed by 2 fully-connected ReLU layers with 512 nodes. The convolutional layers use 16 filters, 8x8 and 4x4 kernels respectively, and rectified units. The fully-connected layers use dropout with a drop probability of 0.2. Because CNN systems take longer to converge, they are optimized over 200 epochs. For all systems, at the end of every epoch, the model is evaluated on the development set, and the best model across all epochs is kept.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-6dad23eeb5e7d3a3f341ab3fb3b087e9d33164dfe99cb36e8e562a9b2ca6f615

Passage ID: `qasper-passage-v1-6dad23eeb5e7d3a3f341ab3fb3b087e9d33164dfe99cb36e8e562a9b2ca6f615`; retrieval score: 2.964605771039002.

Word count: 109.

```text
In this paper, we have investigated speaker-independent models for the classification of phonetic segments from raw ultrasound data. We have shown that the performance of the models heavily degrades when evaluated on data from unseen speakers. This is a result of the variability in ultrasound images, mostly due to differences across speakers, but also due to shifts in probe placement. Using the mean of all ultrasound frames for a new speaker improves the generalization of the models to unseen data, especially when using convolutional neural networks. We have also shown that adapting a pre-trained speaker-independent system using as few as 50 ultrasound frames can outperform a corresponding speaker-dependent system.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 702.

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

#### Rank 1: qasper-passage-v1-d813ffa8f8bdc47be7d8ad512ad1df3198b67cc846eb2e4fdd335597a0a418e6

Passage ID: `qasper-passage-v1-d813ffa8f8bdc47be7d8ad512ad1df3198b67cc846eb2e4fdd335597a0a418e6`; retrieval score: 7.989457307403386.

Word count: 90.

```text
In our experiments we aim to answer the following research questions (RQs):

RQ1: How does the number of training iterations in the BERT language model finetuning stage influence the ATSC end-task performance? At what point does performance start to improve, when does it converge?

RQ2: When trained in-domain, what ATSC end-task performance can be reached through fully exploitet finetuning of the BERT language model?

RQ3: When trained cross-domain in the special case of domain adaptation, what ATSC end-task performance can be reached if BERT language model finetuning is fully exploitet?
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-f599dc2b4c88f425186f5dca4b2747f5003daac38b36060daa506e567addde1a

Passage ID: `qasper-passage-v1-f599dc2b4c88f425186f5dca4b2747f5003daac38b36060daa506e567addde1a`; retrieval score: 4.197836214441568.

Word count: 200.

```text
The results of our experiments are shown in fig:acc-dep-lmiterations and tab:results respectively.

To answer RQ1, which is concerned with details on domain-specific language model finetuning, we can see in fig:acc-dep-lmiterations that first of all, language model finetuning has a substantial effect on ATSC end-task performance. Secondly, we see that in the laptops domain the performance starts to increase at about 10 Mio. finetuned sentences. This is an interesting insight as one would expect a relation closer to a logarithmic curve. One reason might be that it takes many steps to train knowledge into the BERT language model due to its vast amount of parameters. The model already converges at around 17 Mio. sentences. More finetuning does not improve performance significantly. In addition, we find that different runs have a high variance, the standard deviation amounts to about $1\%$ in accuracy, which justifies averaging over 9 runs to measure differences in model performance reliably.

To answer RQ2, which is concerned with in-domain ATSC performance, we see in tab:results that for the in-domain training case, our models BERT-ADA Lapt and BERT-ADA Rest achieve performance close to state-of-the-art on the laptops dataset and new state-of-the-art on the restaurants dataset with accuracies of $79.19\%$
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.11860:19:2` | partial | 0:319 |

#### Rank 3: qasper-passage-v1-a6a60bf06782d34b000b9ee118d325ff7e81decf5176df95337d6dad3bf91c0e

Passage ID: `qasper-passage-v1-a6a60bf06782d34b000b9ee118d325ff7e81decf5176df95337d6dad3bf91c0e`; retrieval score: 3.5391162633699675.

Word count: 200.

```text
are the same in laptops- and joint-corpora. We think that confusion can be created when mixing the domains, but this needs to be investigated further. We also find that the XLNet-base baseline performs generally stronger than BERT-base and even outperforms BERT-ADA Lapt with an accuracy of $79.89\%$ on the laptops dataset.

To answer RQ3, which is concerned with domain adaptation, we can see in the grayed out cells in tab:results, which correspond to the cross-domain adaption case where the BERT language model is trained on the target domain, that domain adaptation works well with $2.2\%$ absolute accuracy improvement on the laptops test set and even $3.6\%$ accuracy improvement on the restaurants test set compared to BERT-base.

In general, the ATSC task generalizes well cross-domain, with about 2-$3\%$ drop in accuracy compared to in-domain training. We think the reason for this might be that syntactical relationships between the aspect-target and the phrase expressing sentiment polarity as well as knowing the sentiment-polarity itself are sufficient to solve the ATSC task in many cases.

For the joint-training case, we find that combining both training datasets improves performance on both test sets. This result is intuitive, as more training data leads to better performance
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.11860:19:2` | partial | 1132:1456 |
| `1908.11860:19:4` | full | 0:366 |

#### Rank 4: qasper-passage-v1-c5eeab892eceae4bb14b9ecd5aba808b1f6abc6f7a1397ea47e8fe886bbca909

Passage ID: `qasper-passage-v1-c5eeab892eceae4bb14b9ecd5aba808b1f6abc6f7a1397ea47e8fe886bbca909`; retrieval score: 3.272977417293434.

Word count: 200.

```text
The datasets typically used for Aspect-Target Sentiment Classification are the SemEval 2014 Task 4 datasets BIBREF1 for the restaurants and laptops domain. Unfortunately, both datasets only have a small number of training examples. One common approach to compensate for insufficient training examples is to invent neural architectures that better model ATSC. For example, in the past a big leap in classification performance was achieved with the use of the Memory Network architecture BIBREF3, which uses memory to remember context words and explicitly models attention over both the target word and context. It was found that making full use of context words improves their model compared to previous models BIBREF2 that make use of left- and right-sided context independently.

BIBREF8 proposed Attention Encoder Networks (AEN), a modification to the transformer architecture. The authors split the Multi-Head Attention (MHA) layers into Intra-MHA and Inter-MHA layers in order to model target words and context differently, which results in a more lightweight model compared to the transformer architecture.

Another recent performance leap was achieved by BIBREF11, who model dependencies between sentiment words explicitly in sentences with more than one aspect-target by using a graph convolutional neural network. They show that their architecture performs particularly
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-e7eaba3a32775b9a8aed7d5c3fd54ef4d298bfdd71440d43f7ca4ace6a2c387e

Passage ID: `qasper-passage-v1-e7eaba3a32775b9a8aed7d5c3fd54ef4d298bfdd71440d43f7ca4ace6a2c387e`; retrieval score: 3.2605217540458513.

Word count: 200.

```text
in-domain ATSC performance, we see in tab:results that for the in-domain training case, our models BERT-ADA Lapt and BERT-ADA Rest achieve performance close to state-of-the-art on the laptops dataset and new state-of-the-art on the restaurants dataset with accuracies of $79.19\%$ and $87.14\%$, respectively. On the restaurants dataset, this corresponds to an absolute improvement of $2.2\%$ compared to the previous state-of-the-art method BERT-PT. Language model finetuning produces a larger improvement on the restaurants dataset. We think that one reason for that might be that the restaurants domain is underrepresented in the pre-training corpora of BERTBASE. Generally, we find that language model finetuning helps even if the finetuning domain does not match the evaluation domain. We think the reason for this might be that the BERT-base model is pre-trained more on knowledge-based corpora like Wikipedia than on text containing opinions. Another finding is that BERT-ADA Joint performs better on the laptops dataset than BERT-ADA Rest, although the unique amount of laptop reviews are the same in laptops- and joint-corpora. We think that confusion can be created when mixing the domains, but this needs to be investigated further. We also find that the XLNet-base baseline performs generally stronger than BERT-base and even outperforms
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.11860:19:2` | partial | 39:1388 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 890.

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

#### Rank 1: qasper-passage-v1-11bc26f734e2179609853bd34a1369839c7dbffb28459f8bf6168cef42515f48

Passage ID: `qasper-passage-v1-11bc26f734e2179609853bd34a1369839c7dbffb28459f8bf6168cef42515f48`; retrieval score: 3.853835232105258.

Word count: 141.

```text
We have introduced Bertram, a novel architecture for relearning high-quality representations of rare words. This is achieved by employing a powerful pretrained language model and deeply connecting surface-form and context information. By replacing important words with rare synonyms, we have created various downstream task datasets focusing on rare words; on all of these datasets, Bertram improves over a BERT model without special handling of rare words, demonstrating the usefulness of our proposed method.

As our analysis has shown that even for the most frequent words considered, using Bertram is still beneficial, future work might further investigate the limits of our proposed method. Furthermore, it would be interesting to explore more complex ways of incorporating surface-form information – e.g., by using a character-level CNN similar to the one of BIBREF27 – to balance out the potency of Bertram's form and context parts.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-9cad096cc009a01b31bf742870544562a62237c470db6853c6ad446c5acda779

Passage ID: `qasper-passage-v1-9cad096cc009a01b31bf742870544562a62237c470db6853c6ad446c5acda779`; retrieval score: 3.691160431044295.

Word count: 200.

```text
we introduce Bertram (BERT for Attentive Mimicking), a novel architecture for understanding rare words that combines a pretrained BERT language model with Attentive Mimicking BIBREF19. Unlike previous approaches making use of language models BIBREF5, our approach integrates BERT in an end-to-end fashion and directly makes use of its hidden states. By giving Bertram access to both surface form and context information already at its very lowest layer, we allow for a deep connection and exchange of information between both input signals.

For various reasons, assessing the effectiveness of methods like Bertram in a contextualized setting poses a huge difficulty: While most previous work on rare words was evaluated on datasets explicitly focusing on such words BIBREF6, BIBREF3, BIBREF4, BIBREF5, BIBREF10, all of these datasets are tailored towards context-independent embeddings and thus not suitable for evaluating our proposed model. Furthermore, understanding rare words is of negligible importance for most commonly used downstream task datasets. To evaluate our proposed model, we therefore introduce a novel procedure that allows us to automatically turn arbitrary text classification datasets into ones where rare words are guaranteed to be important. This is achieved by replacing classification-relevant frequent words with rare synonyms obtained using semantic resources such
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-3231c3833dac065387b1249b445613e0bc300bb05adc01c650460d7231af4af5

Passage ID: `qasper-passage-v1-3231c3833dac065387b1249b445613e0bc300bb05adc01c650460d7231af4af5`; retrieval score: 3.495012919928321.

Word count: 191.

```text
introduce a novel procedure that allows us to automatically turn arbitrary text classification datasets into ones where rare words are guaranteed to be important. This is achieved by replacing classification-relevant frequent words with rare synonyms obtained using semantic resources such as WordNet BIBREF20.

Using this procedure, we extract rare word datasets from three commonly used text (or text pair) classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. On both the WNLaMPro dataset of BIBREF0 and all three so-obtained datasets, our proposed Bertram model outperforms previous work by a large margin.

In summary, our contributions are as follows:

We show that a pretrained BERT instance can be integrated into Attentive Mimicking, resulting in much better context representations and a deeper connection of form and context.

We design a procedure that allows us to automatically transform text classification datasets into datasets for which rare words are guaranteed to be important.

We show that Bertram achieves a new state-of-the-art on the WNLaMPro probing task BIBREF0 and beats all baselines on rare word instances of AG's News, MNLI and DBPedia, resulting in an absolute improvement of up to 24% over a BERT baseline.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-e5976dc77c5ac9d0d28c3ef0ddb7a2afdf75e4f5407cad6dd98e29a0a105a303

Passage ID: `qasper-passage-v1-e5976dc77c5ac9d0d28c3ef0ddb7a2afdf75e4f5407cad6dd98e29a0a105a303`; retrieval score: 3.488158386425669.

Word count: 200.

```text
To measure the effect of adding Bertram to BERT on downstream tasks, we apply the procedure described in Section SECREF4 to a commonly used textual entailment dataset as well as two text classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. For all three datasets, we use BERT$_\text{base}$ as a baseline model and create the substitution dictionary $S$ using the synonym relation of WordNet BIBREF20 and the pattern library BIBREF34 to make sure that all synonyms have consistent parts of speech. As an additional source of word substitutions, we make use of the misspellings dataset of BIBREF25, which is based on query logs of a search engine. To prevent misspellings from dominating the resulting dataset, we only assign misspelling-based substitutes to randomly selected 10% of the words contained in each sentence. Motivated by the results on WNLaMPro-medium, we consider every word that occurs less than 100 times in the WWC and our BooksCorpus replica combined as being rare. Some examples of entries in the resulting datasets can be seen in Table TABREF35.

Just like for WNLaMPro, our default way of injecting Bertram embeddings into the baseline model is to replace the sequence of uncontextualized WordPiece tokens for a given
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1910.07181:11:0` | full | 0:1092 |

#### Rank 5: qasper-passage-v1-8d519c7f03f61766432cfb2e2aff0e8935c405b48acff5f4668a25c165c3260e

Passage ID: `qasper-passage-v1-8d519c7f03f61766432cfb2e2aff0e8935c405b48acff5f4668a25c165c3260e`; retrieval score: 2.988646416603272.

Word count: 200.

```text
to the procedure described above, we also try a variant where instead of replacing the original WordPiece embeddings for a given rare word, we merely add the Bertram-based embedding, separating both representations using a single slash:

As it performs best on the rare and medium subsets of WNLaMPro combined, we use only the add-gated variant of Bertram for all datasets. Results can be seen in Table TABREF37, where for each task, we report the accuracy on the entire dataset as well as scores obtained considering only instances where at least one word was replaced by a misspelling or a WordNet synonym, respectively. Consistent with results on WNLaMPro, combining BERT with Bertram outperforms both a standalone BERT model and one combined with Attentive Mimicking across all tasks. While keeping the original BERT embeddings in addition to Bertram's representation brings no benefit, adding in-domain data clearly helps for two out of three datasets. This makes sense as for rare words, every single additional context can be crucial for gaining a deeper understanding.

To further understand for which words using Bertram is helpful, in Figure FIGREF39 we look at the accuracy of BERT both with and without Bertram on all three tasks as
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 932.

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

#### Rank 1: qasper-passage-v1-3231c3833dac065387b1249b445613e0bc300bb05adc01c650460d7231af4af5

Passage ID: `qasper-passage-v1-3231c3833dac065387b1249b445613e0bc300bb05adc01c650460d7231af4af5`; retrieval score: 5.72116305918037.

Word count: 191.

```text
introduce a novel procedure that allows us to automatically turn arbitrary text classification datasets into ones where rare words are guaranteed to be important. This is achieved by replacing classification-relevant frequent words with rare synonyms obtained using semantic resources such as WordNet BIBREF20.

Using this procedure, we extract rare word datasets from three commonly used text (or text pair) classification datasets: MNLI BIBREF21, AG's News BIBREF22 and DBPedia BIBREF23. On both the WNLaMPro dataset of BIBREF0 and all three so-obtained datasets, our proposed Bertram model outperforms previous work by a large margin.

In summary, our contributions are as follows:

We show that a pretrained BERT instance can be integrated into Attentive Mimicking, resulting in much better context representations and a deeper connection of form and context.

We design a procedure that allows us to automatically transform text classification datasets into datasets for which rare words are guaranteed to be important.

We show that Bertram achieves a new state-of-the-art on the WNLaMPro probing task BIBREF0 and beats all baselines on rare word instances of AG's News, MNLI and DBPedia, resulting in an absolute improvement of up to 24% over a BERT baseline.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-712a2982f92da8f69b3f330635e29030cb95c1b93f71c8f48051f3cbf1e1a249

Passage ID: `qasper-passage-v1-712a2982f92da8f69b3f330635e29030cb95c1b93f71c8f48051f3cbf1e1a249`; retrieval score: 5.462512710298585.

Word count: 200.

```text
As traditional word embedding algorithms BIBREF1 are known to struggle with rare words, several techniques for improving their representations have been proposed over the last few years. These approaches exploit either the contexts in which rare words occur BIBREF2, BIBREF3, BIBREF4, BIBREF5, their surface-form BIBREF6, BIBREF7, BIBREF8, or both BIBREF9, BIBREF10. However, all of these approaches are designed for and evaluated on uncontextualized word embeddings.

With the recent shift towards contextualized representations obtained from pretrained deep language models BIBREF11, BIBREF12, BIBREF13, BIBREF14, the question naturally arises whether these approaches are facing the same problem. As all of them already handle rare words implicitly – using methods such as byte-pair encoding BIBREF15 and WordPiece embeddings BIBREF16, or even character-level CNNs BIBREF17 –, it is unclear whether these models even require special treatment of rare words. However, the listed methods only make use of surface-form information, whereas BIBREF9 found that for covering a wide range of rare words, it is crucial to consider both surface-form and contexts.

Consistently, BIBREF0 recently showed that for BERT BIBREF13, a popular pretrained language model based on a Transformer architecture BIBREF18, performance on a rare word probing task can significantly be improve by relearning representations of rare
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-65f64659d54d6d782f1a1cb87f7b377f836479f52c35b889ba817803df563d87

Passage ID: `qasper-passage-v1-65f64659d54d6d782f1a1cb87f7b377f836479f52c35b889ba817803df563d87`; retrieval score: 5.215910323700135.

Word count: 200.

```text
We evalute Bertram on the WNLaMPro dataset of BIBREF0. This dataset consists of cloze-style phrases like

and the task is to correctly fill the slot (____) with one of several acceptable target words (e.g., “fruit”, “bush” and “berry”), which requires knowledge of the phrase's keyword (“lingonberry” in the above example). As the goal of this dataset is to probe a language model's ability to understand rare words without any task-specific finetuning, BIBREF0 do not provide a training set. Furthermore, the dataset is partitioned into three subsets; this partition is based on the frequency of the keyword, with keywords occurring less than 10 times in the WWC forming the rare subset, those occurring between 10 and 100 times forming the medium subset, and all remaining words forming the frequent subset. As our focus is on improving representations for rare words, we evaluate our model only on the former two sets.

Results on WNLaMPro rare and medium are shown in Table TABREF34, where the mean reciprocal rank (MRR) is reported for BERT, Attentive Mimicking and Bertram. As can be seen, supplementing BERT with any of the proposed relearning methods results in noticeable improvements for the rare subset, with add clearly outperforming replace.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1910.07181:10:0` | full | 0:104 |

#### Rank 4: qasper-passage-v1-ac987997971c5fc066c1853580c75cc08dd585d7910b0920be0dfdee94a6e6d3

Passage ID: `qasper-passage-v1-ac987997971c5fc066c1853580c75cc08dd585d7910b0920be0dfdee94a6e6d3`; retrieval score: 5.198110383454053.

Word count: 200.

```text
consider both surface-form and contexts.

Consistently, BIBREF0 recently showed that for BERT BIBREF13, a popular pretrained language model based on a Transformer architecture BIBREF18, performance on a rare word probing task can significantly be improve by relearning representations of rare words using Attentive Mimicking BIBREF19. However, their proposed model is limited in two important respects:

For processing contexts, it uses a simple bag-of-words model, throwing away much of the available information.

It combines form and context only in a shallow fashion, thus preventing both input signals from sharing information in any sophisticated manner.

Importantly, this limitation applies not only to their model, but to all previous work on obtaining representations for rare words by leveraging form and context. While using bag-of-words models is a reasonable choice for uncontextualized embeddings, which are often themselves based on such models BIBREF1, BIBREF7, it stands to reason that they are suboptimal for contextualized embeddings based on position-aware deep neural architectures.

To overcome these limitations, we introduce Bertram (BERT for Attentive Mimicking), a novel architecture for understanding rare words that combines a pretrained BERT language model with Attentive Mimicking BIBREF19. Unlike previous approaches making use of language models BIBREF5, our approach integrates BERT in an
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-4571dfde1538b00b5b5b826869a0e0344faab3c764208d954e53beb50c80cb94

Passage ID: `qasper-passage-v1-4571dfde1538b00b5b5b826869a0e0344faab3c764208d954e53beb50c80cb94`; retrieval score: 4.368349704173636.

Word count: 122.

```text
they (i) do not incorporate surface-form information and (ii) do not directly access the hidden states of the language model, but instead simply use its output distribution.

There are several datasets explicitly focusing on rare words, e.g. the Stanford Rare Word dataset of BIBREF6, the Definitional Nonce dataset of BIBREF3 and the Contextual Rare Word dataset BIBREF4. However, all of these datasets are only suitable for evaluating context-independent word representations.

Our proposed method of generating rare word datasets is loosely related to adversarial example generation methods such as HotFlip BIBREF29, which manipulate the input to change a model's prediction. We use a similar mechanism to determine which words in a given sentence are most important and replace these words with rare synonyms.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 913.

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

#### Rank 1: qasper-passage-v1-561b469d2ac02098ab079ba56b4c2ca8aab6563b0ec52b92501a53630944a287

Passage ID: `qasper-passage-v1-561b469d2ac02098ab079ba56b4c2ca8aab6563b0ec52b92501a53630944a287`; retrieval score: 3.40093871709988.

Word count: 123.

```text
The primary question we investigate with this model is what kind of input is best for generating accurate and informative citation sentences. Prior works in citation recommendation have made use of abstracts, which perhaps act as sufficient summaries of document content for this task. Additionally, we explore variants of extended context, such as the introduction or first section after the abstract. Since scientific texts are too long to fit into the context window of our generation model, we also investigate a “sampling” approach which samples sentences from throughout the document until the context window is full. In this work, we combine either the abstract or introduction of the source document with each of the abstract, introduction, or sampled sentences from the cited document.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-bc56e1c95f4e40cc2d69994c91cf5e14fe732d57ed817bdce4fcf0e394f8520c

Passage ID: `qasper-passage-v1-bc56e1c95f4e40cc2d69994c91cf5e14fe732d57ed817bdce4fcf0e394f8520c`; retrieval score: 2.583695280765658.

Word count: 200.

```text
We compare the different baseline systems using BLEU BIBREF12, ROUGE (specifically ROUGE 1, 2, and L; BIBREF13), and the recently introduced BertScore BIBREF14, a similarity metric based on BERT embeddings which has been shown to correlate well with human judgements on other tasks. To adapt the BertScore metric to the scientific text domain, we use SciBERT embeddings.

Table TABREF7 (above the double line) shows the performance of the SciGPT2 model on the test set when provided with the different input context combinations outlined in Section SECREF5. We find that context does make a difference for this category of model, and that models which have access to the intro of the documents outperform those which use abstracts or sampling.

Automatic evaluation of the retrieval-based methods on the test data are shown below the double line in Table TABREF7. This table shows that the retrieval methods perform well on this task. However we will show the limitations of these automatic metrics in Section SECREF14. We also observe that tuning the $\alpha $ and $\beta $ parameters on the validation set results in overfitting for this method. Outputs are largely unchanged by this tuning; fewer than 400 test datapoints differ from the untuned
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-faff409a7222498191210693b1c4dfe5b877a2f1ede71eebf764c23e3a5fcde2

Passage ID: `qasper-passage-v1-faff409a7222498191210693b1c4dfe5b877a2f1ede71eebf764c23e3a5fcde2`; retrieval score: 2.5550815929816744.

Word count: 198.

```text
specific cited document and not elsewhere in the corpus. This requires a model that can learn phrase meanings from very few exposures, an important but unsolved problem for text generation systems. Possibly more challenging is understanding and expressing the various and nuanced relationships between related scientific works.

In this work, we introduce the task of citation text generation. Leveraging the full texts of English-language scientific articles, we construct a dataset of citation sentences in the computer science domain for training and evaluating citation text generation models. We investigate strong retrieval and neural baseline models against which future work can compare. For use cases where large models can be trained, we extend the successful GPT2 architecture BIBREF6 to the scientific domain with additional pre-training and subsequent fine-tuning on the citation generation task. We experiment with different kinds of document context in the fine-tuning and inference stages. We also explore retrieval-based techniques which may more easily generalize to lower-resource settings. These models retrieve citation sentences from training documents which are most similar to test inputs. Our evaluations show that these techniques often produce plausible citation sentences, but indicate clear directions for improvement. Code and artifacts are provided for future research.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-99d670015e63fa0894063ecd5854f25c84ad49a47ffc1245e0f0ff030815bc79

Passage ID: `qasper-passage-v1-99d670015e63fa0894063ecd5854f25c84ad49a47ffc1245e0f0ff030815bc79`; retrieval score: 2.5338189722819657.

Word count: 125.

```text
Section SECREF14. We also observe that tuning the $\alpha $ and $\beta $ parameters on the validation set results in overfitting for this method. Outputs are largely unchanged by this tuning; fewer than 400 test datapoints differ from the untuned outputs. A larger validation split may alleviate this problem.

Statistical significance is assessed for select results using bootstrapping with 1000 samples in each of 100 iterations. This test shows that conditioning on the introduction of the source document improves performance compared to conditioning on the abstract when using the SciGPT2 model. However, we see that IR methods perform better than the best neural models. We do not find enough evidence to reject the null hypothesis regarding what context from the cited document should be used.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2002.00317:7:3` | full | 0:489 |

#### Rank 5: qasper-passage-v1-7f85ad193f5e2f6c39cde51b81085e5d7170de22bc004d7f2eacd5ce1c3924fe

Passage ID: `qasper-passage-v1-7f85ad193f5e2f6c39cde51b81085e5d7170de22bc004d7f2eacd5ce1c3924fe`; retrieval score: 1.9117269519020972.

Word count: 157.

```text
The fluency and topical relevance of the baseline models show the plausibility of the citation text generation task as well as the utility of including pretrained scientific language models in future models. But based on the kinds of errors we have seen, future work should focus on two complementary goals: ensuring the factual accuracy of the generated text and improved modeling of the cited document. Factual accuracy is difficult to enforce in statistical text generation systems, especially where inference includes sampling procedures. Grounding to knowledge bases could help. For this task, knowledge extracted from candidate generations could be compared with knowledge from the full source and cited documents to prune false or irrelevant statements. Further, modeling input documents as knowledge graphs of their contents may help these algorithms better understand the cited document, resulting in better outputs. However, such a model will have to address the open problem of combining pretrained language models with graph encoding techniques.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 803.

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

#### Rank 1: qasper-passage-v1-ff1539166bcfe1f5bcb410744b9bc2caf42f332f465e109da6eebff6506e42cd

Passage ID: `qasper-passage-v1-ff1539166bcfe1f5bcb410744b9bc2caf42f332f465e109da6eebff6506e42cd`; retrieval score: 6.930584420694174.

Word count: 158.

```text
The stock price data of Microsoft are labeled suitably for training using a simple program. If the previous day stock price is more than the current day stock price, the current day is marked with a numeric value of 0, else marked with a numeric value of 1. Now, this correlation analysis turns out to be a classification problem. The total positive, negative and neutral emotions in tweets in a 3 day period are calculated successively which are used as features for the classifier model and the output is the labeled next day value of stock 0 or 1.The window size is experimented and best results are achieved when the sentiment values precede 3 days to the stock price. A total of 355 instances, each with 3 attributes are fed to the classifier with a split proportions of 80% train dataset and the remaining dataset for testing. The accuracy of the classifier is discussed in the results section.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-dd74dddec56f3187f27281c0815d649db09b9e4249c6f31fa301ffc11a3bf5c7

Passage ID: `qasper-passage-v1-dd74dddec56f3187f27281c0815d649db09b9e4249c6f31fa301ffc11a3bf5c7`; retrieval score: 6.451836968378243.

Word count: 141.

```text
A classifier is presented in the previous sections that is trained with aggregate sentiment values for 3-day period as features and the increase/decrease in stock price represented by 1/0 as the output. Total data is split into two parts, 80 percent to train the model and remaining for testing operations. The classifier results show an accuracy value of 69.01% when trained using Logistic regression algorithm and the accuracy rate varied with the training set. When the model with LibSVM is trained with 90 percent of data, it gave a result of 71.82%. These results give a significant edge to the investors and they show good correlation between stock market movements and the sentiments of public expressed in twitter. This trend shows that with increasing dataset the models are performing well. We would like to incorporate more data in our future work.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-a68b2aefa92f57cb7acff81f03bf9424630e9b5bbaf43e2686d3929d09ae80f6

Passage ID: `qasper-passage-v1-a68b2aefa92f57cb7acff81f03bf9424630e9b5bbaf43e2686d3929d09ae80f6`; retrieval score: 6.095443761302011.

Word count: 200.

```text
The above sections discussed the method followed to train the classifier used for sentiment analysis of tweets. The classifier with features as Word2vec representations of human annotated tweets trained on Random Forest algorithm with a split percentage of 90 for training the model and remaining for testing the model showed an accuracy of 70.2%. With N-gram representations, the classifier model with same algorithm and with same dataset showed an accuracy of 70.5%. Though the results are very close, model trained with word2vec representations is picked to classify the nonhuman annotated tweets because of its promising accuracy for large datasets and the sustainability in word meaning. Numerous studies have been conducted on people and they concluded that the rate of human concordance, that is the degree of agreement among humans on the sentiment of a text, is between 70% and 79% BIBREF21 . They have also synthesized that sentiment analyzers above 70% are very accurate in most of the cases. Provided this information, the results we obtained from the sentiment classification can be observed as very good figures while predicting the sentiments in short texts, tweets, less than 140 characters in length. Table-2 depicts the results of sentiment classification including accuracy,
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-050b4ed45093f189705bdce098d44ee759aac508f53f19d54dd7fba008377f9c

Passage ID: `qasper-passage-v1-050b4ed45093f189705bdce098d44ee759aac508f53f19d54dd7fba008377f9c`; retrieval score: 4.978159859728936.

Word count: 125.

```text
In this work, we have considered only twitter data for analyzing people's sentiment which may be biased because not all the people who trade in stocks share their opinions on twitter. Stocktwits BIBREF22 is a financial communication platform designed solely for sharing ideas and insights of investors, entrepreneurs and traders. The current study can be extended by incorporating stocktwits data. In addition to this, data from news can also be included for an exhaustive public opinion collection.

While training the sentiment analyzer, 3,216 tweets are used which is comparatively a less number to train a sentiment analyzer. In future, we look forward to human annotate more than 10,000 tweets and train the classifiers. With increasing size of training datasets, the models tend to perform better.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-3bf6d6a8458e3b46035156e279df90bf275dcb2a362d936526c47ebfd6a999de

Passage ID: `qasper-passage-v1-3bf6d6a8458e3b46035156e279df90bf275dcb2a362d936526c47ebfd6a999de`; retrieval score: 4.790213558783997.

Word count: 106.

```text
rise and fall in stock prices based on the sentiments extracted from twitter to find the correlation. The core contribution of our work is the development of a sentiment analyzer which works better than the one in Brian's work and a novel approach to find the correlation. Sentiment analyzer is used to classify the sentiments in tweets extracted.The human annotated dataset in our work is also exhaustive. We have shown that a strong correlation exists between twitter sentiments and the next day stock prices in the results section. We did so by considering the tweets and stock opening and closing prices of Microsoft over a year.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 730.

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

#### Rank 1: qasper-passage-v1-259d03763925b430f6ac0144286f4ca70393e137e63db9a4905ed91ef861c954

Passage ID: `qasper-passage-v1-259d03763925b430f6ac0144286f4ca70393e137e63db9a4905ed91ef861c954`; retrieval score: 2.2193380839148125.

Word count: 79.

```text
While image and sound come with a natural high dimensional embedding, the issue of which is the best representation is still an open research problem in the context of natural language and text. It is beyond the scope of this paper to do a thorough overview of word representations, for this we refer the interest reader to the excellent review provided by BIBREF1 . Here, we will just introduce the main representations that are related to the proposed method.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-b00c7cace135632c06b04b51d5de0ffd579579d93af6159b080cb7cbf796f7e9

Passage ID: `qasper-passage-v1-b00c7cace135632c06b04b51d5de0ffd579579d93af6159b080cb7cbf796f7e9`; retrieval score: 1.9711176348653756.

Word count: 101.

```text
In this paper, we presented the network architecture used for the Fortia-FBK submission to the Semeval-2017 Task 5, Subtask 2 challenge, with the goal of predicting positive (bullish) or negative (bearish) attitude towards a target brand from financial news headlines. The proposed system ranked 1st in such challenge.

Our approach is based on 1d convolutions and uses fine-tuning of unsupervised word representations and a rule based sentiment model in its inputs. We showed that the use of pre-computed word representations allows to reduce over-fitting and to achieve significantly better generalization, while some basic pre-processing was needed to further improve the performance.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-ca8f0c8dc09b09c4fc614b3d8ca31fb7a66d63d23b8a95504bbaea22f942546d

Passage ID: `qasper-passage-v1-ca8f0c8dc09b09c4fc614b3d8ca31fb7a66d63d23b8a95504bbaea22f942546d`; retrieval score: 0.43883256013422584.

Word count: 194.

```text
Minimal preprocessing was adopted in our approach: we replaced the target company's name with a fixed word <company> and numbers with <number>. The sentences were then tokenized using spaces as separator and keeping punctuation symbols as separate tokens.

The words are represented as fixed length vectors INLINEFORM0 resulting from the concatenation of GloVe pre-trained embeddings and DepecheMood BIBREF19 lexicon representation. Since we cannot directly concatenate token-based embeddings (provided in GloVe) with the lemma#PoS-based representation available in DepecheMood, we proceeded to re-build the latter in token-based form, applying the exact same methodology albeit with two differences: we started from a larger dataset (51.9K news articles instead of 25.3K) and used a frequency cut-off, i.e. keeping only those tokens that appear at least 5 times in the corpus.

These word-level representation are used as the first layer of our network. During training we allow the weights of the representation to be updated. We further add the VADER score for the sentence under analysis. The complete sentence representation is presented in Algorithm UID8 .

InputInput OutputOutput The sentence embedding INLINEFORM0 INLINEFORM1

INLINEFORM0 in INLINEFORM1 INLINEFORM2 = [GloVe( INLINEFORM3 , INLINEFORM4 ), DepecheMood( INLINEFORM5 )] INLINEFORM6 Sentence representation
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-00d71462d2b8cf025fc141489090e791514135b644d2b1c526436443abf330ed

Passage ID: `qasper-passage-v1-00d71462d2b8cf025fc141489090e791514135b644d2b1c526436443abf330ed`; retrieval score: 0.39883798401475035.

Word count: 96.

```text
infer its polarity score i.e. how positive (or negative) the sentence is with respect to the target company. Previous research BIBREF0 has highlighted the association between news items and market fluctiations; hence, in the financial domain, sentiment analysis can be used as a proxy for bullish (i.e. positive, upwards trend) or bearish (i.e. negative, downwards trend) attitude towards a specific financial actor, allowing to identify and monitor in real-time the sentiment associated with e.g. stocks or brands.

Our contribution leverages pre-trained word embeddings (GloVe, trained on wikipedia+gigaword corpus), the DepecheMood affective lexicon, and convolutional neural networks.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1704.00939:0:3` | full | 0:171 |

#### Rank 5: qasper-passage-v1-d0aa3c79d16aa0209291030ef034b53c6cad75215cd5893f261613db4139e76c

Passage ID: `qasper-passage-v1-d0aa3c79d16aa0209291030ef034b53c6cad75215cd5893f261613db4139e76c`; retrieval score: 0.38093205523457363.

Word count: 108.

```text
In this section, we report the results obtained by our model according to challenge official evaluation metric, which is based cosine-similarity and described in BIBREF27 . Results are reported for three diverse configurations: (i) the full system; (ii) the system without using word embeddings (i.e. Glove and DepecheMood); and (iii) the system without using pre-processing. In Table TABREF17 we show model's performances on the challenge training data, in a 5-fold cross-validation setting.

Further, the final performances obtained with our approach on the challenge test set are reported in Table TABREF18 . Consistently with the cross-validation performances shown earlier, we observe the beneficial impact of word-representations and basic pre-processing.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 578.

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

#### Rank 1: qasper-passage-v1-3f37ba617c6c93186050542d631fa84ce37645eea79d7e659a39dc4cbf031453

Passage ID: `qasper-passage-v1-3f37ba617c6c93186050542d631fa84ce37645eea79d7e659a39dc4cbf031453`; retrieval score: 7.773193540981777.

Word count: 200.

```text
Neural machine translation (NMT) typically makes use of a recurrent neural network (RNN) -based encoder and decoder, along with an attention mechanism BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 . However, it has been shown that RNNs require some supervision to learn syntax BIBREF4 , BIBREF5 , BIBREF6 . Therefore, explicitly incorporating syntactic information into NMT has the potential to improve performance. This is particularly true for source syntax, which can improve the model's representation of the source language.

Recently, there have been a number of proposals for using linearized representations of parses within standard NMT BIBREF7 , BIBREF8 , BIBREF9 . Linearized parses are advantageous because they can inject syntactic information into the models without significant changes to the architecture. However, using linearized parses in a sequence-to-sequence (seq2seq) framework creates some challenges, particularly when using source parses. First, the parsed sequences are significantly longer than standard sentences, since they contain node labels as well as words. Second, these systems often fail when the source sentence is not parsed. This can be a problem for inference, since the external parser may fail on an input sentence at test time. We propose a method for incorporating linearized source parses into NMT
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-6e3f2d04f5ac372012e199739b8cd5aa292ef44edaab7432a24fb47a34afb578

Passage ID: `qasper-passage-v1-6e3f2d04f5ac372012e199739b8cd5aa292ef44edaab7432a24fb47a34afb578`; retrieval score: 6.412017579166906.

Word count: 180.

```text
The idea of incorporating linearized parses into seq2seq has been adapted to NMT as a means of injecting syntax. aharoni2017towards first did this by parsing the target side of the training data and training the system to generate parsed translations of the source input; this is the inverse of our parse2seq baseline. Similarly, nadejde2017syntax interleaved CCG supertags with words on the target side, finding that this improved translation despite requiring longer sequences.

Most similar to our multi-source model is the parallel RNN model proposed by li2017modeling. Like multi-source, the parallel RNN used two encoders, one for words and the other for syntax. However, they combined these representations at the word level, whereas we combine them on the sentence level. Their mixed RNN model is also similar to our parse2seq baseline, although the mixed RNN decoder attended only to words. As the mixed RNN model outperformed the parallel RNN model, we do not attempt to compare our model to parallel RNN. These models are similar to ours in that they incorporate linearized parses into NMT; here, we utilize a multi-source framework.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-c52bdbf3c24272bb010977359653d7210ab40996ca69f82d650df2e6da45c0a1

Passage ID: `qasper-passage-v1-c52bdbf3c24272bb010977359653d7210ab40996ca69f82d650df2e6da45c0a1`; retrieval score: 5.603915586918501.

Word count: 96.

```text
often fail when the source sentence is not parsed. This can be a problem for inference, since the external parser may fail on an input sentence at test time. We propose a method for incorporating linearized source parses into NMT that addresses these challenges by taking both the sequential source sentence and its linearized parse simultaneously as input in a multi-source framework. Thus, the model is able to use the syntactic information encoded in the parse while falling back to the sequential sentence when necessary. Our proposed model improves over both standard and parsed NMT baselines.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-9bf142d01766dc439a9d931592a07c1b3293db8af15d721b40fc88324f70f02c

Passage ID: `qasper-passage-v1-9bf142d01766dc439a9d931592a07c1b3293db8af15d721b40fc88324f70f02c`; retrieval score: 5.384470934138515.

Word count: 131.

```text
We propose a multi-source framework for injecting linearized source parses into NMT. This model consists of two identical RNN encoders with no shared parameters, as well as a standard RNN decoder. For each target sentence, two versions of the source sentence are used: the sequential (standard) version and the linearized parse (lexicalized or unlexicalized). Each of these is encoded simultaneously using the encoders; the encodings are then combined and used as input to the decoder. We combine the source encodings using the hierarchical attention combination proposed by libovicky2017attention. This consists of a separate attention mechanism for each encoder; these are then combined using an additional attention mechanism over the two separate context vectors. This multi-source method is thus able to combine the advantages of both standard RNN-based encodings and syntactic encodings.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-daa5dce8d92b0bdef3a0e4b5292f0d77f15056b238519421d8d0287c6d411e00

Passage ID: `qasper-passage-v1-daa5dce8d92b0bdef3a0e4b5292f0d77f15056b238519421d8d0287c6d411e00`; retrieval score: 5.184847812491391.

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

#### Rank 1: qasper-passage-v1-90fc4910fa68d29db79a8a96168cb07f40062e70e94979c76f71f668a2d891fb

Passage ID: `qasper-passage-v1-90fc4910fa68d29db79a8a96168cb07f40062e70e94979c76f71f668a2d891fb`; retrieval score: 5.127611321004302.

Word count: 200.

```text
A large majority of the human knowledge is recorded through text documents. That is why ability for a system to automatically infer information from text without any structured data has become a major challenge. Answering questions about a given document is a relevant proxy task that has been proposed as a way to evaluate the reading ability of a given model. In this configuration, a text document such as a news article, a document from Wikipedia or any type of text is presented to a machine with an associated set of questions. The system is then expected to answer these questions and evaluated by its accuracy on this task. The machine reading framework is very general and we can imagine a large panel of questions that can possibly handle most of the standard natural language processing tasks. For example, the task of named entities recognition can be formulated as a machine reading one where your document is the sentence and the question would be 'What are the named entities mentioned in this sentence?'. These natural language interactions are an important objective for reading systems.

Recently, many datasets have been proposed to build and evaluate reading models BIBREF0 , BIBREF1 .
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-b69682efcd01667999d46a3291c1f28a81a3f3d604d77785bda46c198a021dcc

Passage ID: `qasper-passage-v1-b69682efcd01667999d46a3291c1f28a81a3f3d604d77785bda46c198a021dcc`; retrieval score: 4.110948132177202.

Word count: 54.

```text
answers. On the contrary, the deep projective reader achieves encouraging on this dataset. It outperforms all the other baselines, with very good scores on the first fourth tasks. The question/document and document/document attention layers proposed in BIBREF12 seem once again to produce rich encodings of the inputs which are relevant for our projection layer.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-c711fa146275650b4aee9bb1b187d5d16e5f2c6091bc0db830fdaf8c61c0735b

Passage ID: `qasper-passage-v1-c711fa146275650b4aee9bb1b187d5d16e5f2c6091bc0db830fdaf8c61c0735b`; retrieval score: 3.58210231104928.

Word count: 200.

```text
Table TABREF19 displays the performance of the 4 baselines on the ReviewQA's test set. These results are the performance achieved by our own implementation of these 4 models. According to our results, the simple LSTM network and the MemN2N perform very poorly on this dataset. Especially on the most advanced reasoning tasks. Indeed, the task 5 which corresponds to the prediction of the exact rating of an aspect seems to be very challenging for these model. Maybe the tokenization by sentence to create the memory blocks of the MemN2N, which is appropriated in the case of the bAbI tasks, is not a good representation of the documents when it has to handle human generated comments. However, the logistic regression achieves reasonable performance on these tasks, and do not suffer from catastrophic performance on any tasks. Its worst result comes on task 6 and one of the reason is probably that this architecture is not designed to predict a list of answers. On the contrary, the deep projective reader achieves encouraging on this dataset. It outperforms all the other baselines, with very good scores on the first fourth tasks. The question/document and document/document attention layers proposed in BIBREF12 seem once again
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-f44cc9eb04d94fd180aec17b63b0741ae5fe8ad4314a3dad698105a347da37ed

Passage ID: `qasper-passage-v1-f44cc9eb04d94fd180aec17b63b0741ae5fe8ad4314a3dad698105a347da37ed`; retrieval score: 2.5470349106313797.

Word count: 200.

```text
the question would be 'What are the named entities mentioned in this sentence?'. These natural language interactions are an important objective for reading systems.

Recently, many datasets have been proposed to build and evaluate reading models BIBREF0 , BIBREF1 . From cloze style questions BIBREF2 to open questions BIBREF3 , from synthetic data BIBREF4 to human written articles BIBREF5 , many styles of documents and questions have been proposed to challenge reading models. The correct answer to the questions proposed in most of these datasets is a span of text of the source document, which can be restricted to a single word in several cases. It means that the answer should explicitly be present in the source document and that the model should be able to locate it.

Different models have already shown superhuman performance on several of these datasets and particularly on the SQuAD dataset composed of Wikipedia articles BIBREF6 , BIBREF7 . However, some limits of such models have been highlighted when they encounter perturbations into the input documents BIBREF8 . Indeed almost all of the state of the art models on the SQuAD dataset suffer from a lack of robustness against adversarial examples. Once the model is
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-1f6b3b3eff32c40c0e5e8a99b27137966dde01283da29bdb77ac3cb9919464cb

Passage ID: `qasper-passage-v1-1f6b3b3eff32c40c0e5e8a99b27137966dde01283da29bdb77ac3cb9919464cb`; retrieval score: 2.186486127516074.

Word count: 200.

```text
Objective: Starting with the original corpus, we aim at building a machine reading task where natural language questions will challenge the model on its understanding of the reviews. Indeed learning relational reasoning competencies over natural language documents is a major challenge of the current reading models. These original raw data allow us to generate relational questions that can possibly require a global understanding of the comment and reasoning skills to be treated. For example, asking a question like What is the best aspect rated in this comment ? is not an easy question that can be answered without a deep understanding of the review. It is necessary to capture all the aspects mentioned in the text, to predict their rating and finally to select the best one. The tasks and the dataset we propose are publicly available at http://www.europe.naverlabs.com/Blog/ReviewQA-A-novel-relational-aspect-based-opinion-dataset-for-machine-reading

We introduce a list of 8 different competencies that a reading system should master in order to process reviews and text documents in general. These 8 tasks require different competencies and a different level of understanding of the document to be well answered. For instance, detecting if an aspect is mentioned in a review will require less understanding of the review
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 854.

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

#### Rank 1: qasper-passage-v1-eaab379c868a230e2e76b9a31a34d3567f4a6eabc5e5c9680bf25959a643e892

Passage ID: `qasper-passage-v1-eaab379c868a230e2e76b9a31a34d3567f4a6eabc5e5c9680bf25959a643e892`; retrieval score: 4.675618558828398.

Word count: 200.

```text
shown by the existing evaluation methods. Furthermore, the examples suggest that the proposed method does learn better correspondence. The highlighted words in each example in Table TABREF28 share almost the same previous words. However, in the first one, the baseline considers “UTF8gbsn停” (stop) as the most related words, which is a sign of noisy word relations learned from other training examples, while the proposed method generates “UTF8gbsn进站” (to the platform), which is more related to what a human thinks. It is the same with the second example, where a human selects “UTF8gbsn专家” (expert) and Dual-Train selects “UTF8gbsn工作者” (worker), while the baseline selects “UTF8gbsn钻研” (research) and fails to generate a grammatical sentence later. In the third one, the reference and the baseline use the same word, while Dual-Train chooses a word of the same meaning. It can be concluded that Dual-Train indeed learns better word relations that could generalize to the test set, and good word relations can guide the decoder to generate semantically consistent summaries.

To show why the generated text of the proposed method is more related to the source content, we further analyze the label distribution, i.e., the word distribution, generated by the (first) output layer, from which
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-194ebd0810098c051b1b0646f19ef6166024f00d94cbd39297304ef1f30f3e8b

Passage ID: `qasper-passage-v1-194ebd0810098c051b1b0646f19ef6166024f00d94cbd39297304ef1f30f3e8b`; retrieval score: 3.5845741126298627.

Word count: 200.

```text
However, the aforementioned method tries to regularize the output word distribution based on what it has already learned. The relative order of the output words is kept. The self-dependency may not be desirable for regularization. It may be better if more correspondence that is spurious can be identified. In this paper, we further propose to obtain the soft target from a different view of the model, so that different knowledge of the dataset can be used to mitigate the overfitting problem. An additional output layer is introduced to generate the soft target. The two output layers share the same hidden representation but have independent parameters. They could learn different knowledge of the data. We refer to this approach as Dual-Train. For clarity, the original output layer is denoted by INLINEFORM0 and the new output layer INLINEFORM1 . Their outputs are denoted by INLINEFORM2 and INLINEFORM3 , respectively. The output layer INLINEFORM4 acts as the original output layer. We apply soft training using the output from INLINEFORM5 to this output layer to increase its ability of generalization. Suppose the correct label is INLINEFORM6 . The target of the output INLINEFORM7 includes both the one-hot distribution and the distribution generated from INLINEFORM8
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-47d1169692fdcde983a5e3542bc421a0b13781e45a92b969cfd77fc734b7ab98

Passage ID: `qasper-passage-v1-47d1169692fdcde983a5e3542bc421a0b13781e45a92b969cfd77fc734b7ab98`; retrieval score: 2.7828184866753922.

Word count: 155.

```text
We propose a regularization approach for the sequence-to-sequence model on the Chinese social media summarization task. In the proposed approach, we use a cross-entropy based regularization term to make the model neglect the possible unrelated words. We propose two methods for obtaining the soft output word distribution used in the regularization, of which Dual-Train proves to be more effective. Experimental results show that the proposed method can improve the semantic consistency by 4% in terms of human evaluation. As shown by the analysis, the proposed method achieves the improvements by eliminating the less semantically-related word correspondence. The proposed human evaluation method is effective and efficient in judging the semantic consistency, which is absent in previous work but is crucial in the accurate evaluation of the text summarization systems. The proposed metric is simple to conduct and easy to interpret. It also provides an insight on how practicable the existing systems are in the real-world scenario.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-f98e5d50b048087e57fd3df8919220cf01e216f622f768f8a63e48accd7456b7

Passage ID: `qasper-passage-v1-f98e5d50b048087e57fd3df8919220cf01e216f622f768f8a63e48accd7456b7`; retrieval score: 2.7755504185018367.

Word count: 200.

```text
the good summaries. The proposed evaluation is very simple and straight-forward. It focuses on the relevance between the summary and the text. The semantic consistency should be the major consideration when putting the text summarization methods into practice, but the current automatic methods cannot judge properly. For detailed guidelines in human evaluation, please refer to Appendix SECREF6 . In the human evaluation, the text-summary pairs are dispatched to two human annotators who are native speakers of Chinese. As in our setting the summary is evaluated against the reference, the number of the pairs needs to be manually evaluated is four times the number of the pairs in the test set, because we need to compare four systems in total. To decrease the workload and get a hint about the annotation quality at the same time, we adopt the following procedure. We first randomly select 100 pairs in the validation set for the two human annotators to evaluate. Each pair is annotated twice, and the inter-annotator agreement is checked. We find that under the protocol, the inter-annotator agreement is quite high. In the evaluation of the test set, a pair is only annotated once to accelerate evaluation. To further maintain consistency,
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1805.04033:7:0` | partial | 2082:3326 |

#### Rank 5: qasper-passage-v1-8fb470884aa9994b4aec6ac808ce61d52202fac82af8948017a92b4ba1173339

Passage ID: `qasper-passage-v1-8fb470884aa9994b4aec6ac808ce61d52202fac82af8948017a92b4ba1173339`; retrieval score: 2.6412728220599115.

Word count: 124.

```text
be easily evaluated automatically. ROUGE BIBREF9 is widely used for summarization evaluation. However, as ROUGE is designed for extractive text summarization, it cannot deal with summary paraphrasing in abstractive text summarization. Besides, as ROUGE is based on the reference, it requires high-quality reference summary for a reasonable evaluation, which is also lacking in the existing dataset for Chinese social media text summarization. We argue that for proper evaluation of text generation task, human evaluation cannot be avoided. We propose a simple and practical human evaluation for evaluating text summarization, where the summary is evaluated against the source content instead of the reference. It handles both of the problems of paraphrasing and lack of high-quality reference. The contributions of this work are summarized as follows:
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1805.04033:0:3` | partial | 146:997 |

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 879.

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
          146
        ]
      ],
      "1805.04033:7:0": [
        [
          0,
          2082
        ],
        [
          3326,
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

#### Rank 1: qasper-passage-v1-2168c6e6531d2e6850e1c7196d95aa7c30439b4e609aa973b3fd3862b15614d7

Passage ID: `qasper-passage-v1-2168c6e6531d2e6850e1c7196d95aa7c30439b4e609aa973b3fd3862b15614d7`; retrieval score: 7.338028597563338.

Word count: 200.

```text
Non-pre-trained Attention Module: Previous work BIBREF6 trains attention modules for ASR, MT and ST respectively, hence, the attention module of ST does not benefit from the pre-training.

To address these issues, we propose a Tandem Connectionist Encoding Network (TCEN), which is able to reuse all subnets in pre-training, keep the roles of subnets consistent, and pre-train the attention module. Concretely, the TCEN consists of three components, a speech encoder, a text encoder, and a target text decoder. Different from the previous work that pre-trains an encoder-decoder based ASR model, we only pre-train an ASR encoder by optimizing the Connectionist Temporal Classification (CTC) BIBREF8 objective function. In this way, the additional decoder of ASR is not required while keeping the ability to read acoustic features into the source language space by the speech encoder. Besides, the text encoder and decoder can be pre-trained on a large MT dataset. After that, we employ common used multi-task learning method to jointly learn ASR, MT and ST tasks.

Compared to prior works, the encoder of TCEN is a concatenation of an ASR encoder and an MT encoder and our model does not have an ASR decoder, so the subnet waste issue is solved. Furthermore,
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-84c839d4675e5bbac5850714eda3ba329a92439366866c812d53927261ee0604

Passage ID: `qasper-passage-v1-84c839d4675e5bbac5850714eda3ba329a92439366866c812d53927261ee0604`; retrieval score: 6.235107138834423.

Word count: 170.

```text
To leverage large scale ASR and MT data, multi-task learning and pre-training techniques are widely employed to improve the ST system. As shown in Figure FIGREF4, there are three popular multi-task strategies for ST, including 1) one-to-many setting, in which a speech encoder is shared between ASR and ST tasks; 2) many-to-one setting in which a decoder is shared between MT and ST tasks; and 3) many-to-many setting where both the encoder and decoder are shared.

A many-to-many multi-task model contains two encoders as well as two decoders. It can be jointly trained on ASR, MT, and ST tasks. As the attention module is task-specific, three attentions are defined.

Usually, the size of $\mathcal {A}$ and $\mathcal {M}$ is much larger than $\mathcal {S}$. Therefore, the common training practice is to pre-train the model on ASR and MT tasks and then fine-tune it with a multi-task learning manner. However, as aforementioned, this method suffers from subnet waste, role mismatch and non-pre-trained attention issues, which severely limits the end-to-end ST performance.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-c31c48f6ec17ef62cb985655435fee9f1f7d3bdb0d189ff26d5e1adcdb1163cc

Passage ID: `qasper-passage-v1-c31c48f6ec17ef62cb985655435fee9f1f7d3bdb0d189ff26d5e1adcdb1163cc`; retrieval score: 6.135553780760821.

Word count: 200.

```text
ST model to leverage large-scale datasets of ASR and MT. A common practice is to pre-train two encoder-decoder models for ASR and MT respectively, and then initialize the ST model with the encoder of the ASR model and the decoder of the MT model. Subsequently, the ST model is optimized with the multi-task learning by weighing the losses of ASR, MT, and ST. This approach, however, causes a huge gap between pre-training and fine-tuning, which are summarized into three folds:

Subnet Waste: The ST system just reuses the ASR encoder and the MT decoder, while discards other pre-trained subnets, such as the MT encoder. Consequently, valuable semantic information captured by the MT encoder cannot be inherited by the final ST system.

Role Mismatch: The speech encoder plays different roles in pre-training and fine-tuning. The encoder is a pure acoustic model in pre-training, while it has to extract semantic and linguistic features additionally in fine-tuning, which significantly increases the learning difficulty.

Non-pre-trained Attention Module: Previous work BIBREF6 trains attention modules for ASR, MT and ST respectively, hence, the attention module of ST does not benefit from the pre-training.

To address these issues, we propose a Tandem Connectionist Encoding Network (TCEN), which
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-4fa580206bd6b856273c8a0049772b5c06026bd91f1542ccd0def33cc77ecf36

Passage ID: `qasper-passage-v1-4fa580206bd6b856273c8a0049772b5c06026bd91f1542ccd0def33cc77ecf36`; retrieval score: 5.453122857325736.

Word count: 200.

```text
Figure FIGREF5 sketches the overall architecture of TCEN, including a speech encoder $enc_s$, a text encoder $enc_t$ and a decoder $dec$ with an attention module $att$. During training, the $enc_s$ acts like an acoustic model which reads the input $\mathbf {x}$ to word or subword representations $\mathbf {h^s}$, then $enc_t$ learns high-level linguistic knowledge into hidden representations $\mathbf {h^t}$. Finally, the $dec$ defines a distribution probability over target words. The advantage of our architecture is that two encoders disentangle acoustic feature extraction and linguistic feature extraction, making sure that valuable knowledge learned from ASR and MT tasks can be effectively leveraged for ST training. Besides, every module in pre-training can be utilized in fine-tuning, alleviating the subnet waste problem.

Follow BIBREF9 inaguma2018speech, we use CNN-BiLSTM architecture to build our model. Specifically, the input features $\mathbf {x}$ are organized as a sequence of feature vectors in length $T_x$. Then, $\mathbf {x}$ is passed into a stack of two convolutional layers followed by max-pooling:

where $\mathbf {v}^{(l-1)}$ is feature maps in last layer and $\mathbf {W}^{(l)}$ is the filter. The max-pooling layers downsample the sequence in length by a total factor of four. The down-sampled feature sequence is further fed into a
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-e2414dd1b4ce5fac6d1238a88611769f7409f4dd62f68fbaf3eb03a93073e724

Passage ID: `qasper-passage-v1-e2414dd1b4ce5fac6d1238a88611769f7409f4dd62f68fbaf3eb03a93073e724`; retrieval score: 5.007876507989364.

Word count: 200.

```text
MT and ST tasks.

Compared to prior works, the encoder of TCEN is a concatenation of an ASR encoder and an MT encoder and our model does not have an ASR decoder, so the subnet waste issue is solved. Furthermore, the two encoders work at tandem, disentangling acoustic feature extraction and linguistic feature extraction, ensuring the role consistency between pre-training and fine-tuning. Moreover, we reuse the pre-trained MT attention module in ST, so we can leverage the alignment information learned in pre-training.

Since the text encoder consumes word embeddings of plausible texts in MT task but uses speech encoder outputs in ST task, another question is how one guarantees the speech encoder outputs are consistent with the word embeddings. We further modify our model to achieve semantic consistency and length consistency. Specifically, (1) the projection matrix at the CTC classification layer for ASR is shared with the word embedding matrix, ensuring that they are mapped to the same latent space, and (2) the length of the speech encoder output is proportional to the length of the input frame, so it is much longer than a natural sentence. To bridge the length gap, source sentences in MT are lengthened by adding
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 970.

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

#### Rank 1: qasper-passage-v1-c54eb4f2203159700e34140e87a58660e43ac00a8ddb7e381b0339673b26d99f

Passage ID: `qasper-passage-v1-c54eb4f2203159700e34140e87a58660e43ac00a8ddb7e381b0339673b26d99f`; retrieval score: 9.090224891689052.

Word count: 200.

```text
This paper has used data-driven language mapping to select national dialects of English to be included in a global dialect identification model. The main experiments have focused on a dynamic syntactic feature set, showing that it is possible to predict dialect membership within-domain with only a small loss of performance against lexical models. This work raises two remaining problems:

First, we know that location-specific content (i.e., place names, place references, national events) can be used for geo-location and text-based models of place. To what degree does a lexical approach capture linguistic variation (i.e., “pop" vs. “soda") and to what degree is it capturing non-linguistic information (i.e., “Melbourne" vs. “London")? This is an essential problem for dialect identification models. A purely syntactic model does not perform as well as a lexical model, but it does come with more guarantees.

Second, we have seen that inner-circle varieties have higher feature densities given the grammars used here. This implies that there are syntactic constructions in varieties like Philippines English that have not been modeled by the grammar induction component. While dialect identification can be used to optimize regional weights for known constructions, how can such missing constructions be adapted? This remains a challenge.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1904.05527:9:0` | full | 0:389 |

#### Rank 2: qasper-passage-v1-0791da4f0b38148184547372d093bc0d00ad8a7606808df5d6ccf5ba44865618

Passage ID: `qasper-passage-v1-0791da4f0b38148184547372d093bc0d00ad8a7606808df5d6ccf5ba44865618`; retrieval score: 6.433950756568748.

Word count: 200.

```text
features. Vectors for all experiments are available, along with the trained models that depend on these vectors.

As n increases, n-grams tend to represent structural rather than topical information. In this case, performance decreases as n increases. We suggest that this decrease provides an indication that the performance of unigrams is based on location-specific content (e.g., “Chicago" vs. “Singapore") rather than on purely linguistic lexical variation (e.g., “jeans" vs. “denim"). How do we differentiate between predictions based on place-names, those based on place-specific content, and those based on dialectal variation? That is a question for future work. For example, is it possible to identify and remove location-specific content terms? Here we focus instead on using syntactic representations that are not subject to such interference.

Within syntactic features, function words perform the worst on both datasets with F1s of 0.65 and 0.55. This is not surprising because function words in English do not represent syntactic structures directly; they are instead markers of the types of structures being used. CxG-1 comes next with F1s of 0.80 and 0.76, a significant improvement over the function-word baseline but not approaching unigrams. Note that the experiments using this same grammar in previous work (Dunn, 2018c)
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-7a609302f4f375dfe4f3168f3689274f833ada89bde7d9bfae383467ab2becfe

Passage ID: `qasper-passage-v1-7a609302f4f375dfe4f3168f3689274f833ada89bde7d9bfae383467ab2becfe`; retrieval score: 6.403417205226895.

Word count: 107.

```text
a single dominant dialect?

Finally, a corpus-based approach to variation is restricted to the specific domains or registers that are present in the corpus. To what degree is such a model of variation limited to a specific register? This paper uses both web-crawled corpora and social media corpora to explore the robustness of dialect models across domains (Section 8). Along these same lines, how robust is a model of syntactic variation to the presence of a few highly predictive features? This paper uses unmasking, a method from authorship verification (Koppel, et al., 2007), to evaluate the stability of dialect models over rounds of feature pruning (Section 9).
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-2da6fb27f4410843c2c2cd519928fcef993fc7f6feaa4ac691f8a7ed44260d2a

Passage ID: `qasper-passage-v1-2da6fb27f4410843c2c2cd519928fcef993fc7f6feaa4ac691f8a7ed44260d2a`; retrieval score: 5.555443994187057.

Word count: 200.

```text
Sections 3 and 4, is essential for determining the inventory of regional varieties that need to be included in the dialect identification task. This paper uses data-driven language mapping to find out where English is consistently used, given web data and Twitter data, in order to avoid the arbitrary selection of dialect areas. This is important for ensuring that each construction in the grammar receives the best regional weighting.

What syntactic features are needed to represent variation in English? As discussed in Section 6, this paper uses grammar induction on a large background corpus to provide a replicable and dynamic feature space in order to avoid arbitrary limitations (e.g., lists of function words). The other side of this problem is to optimize grammar induction for regional dialects by using an identification task to learn regional weights for each part of the grammar: how much does a single generic grammar of English vary across dialects? To what degree does it represent a single dominant dialect?

Finally, a corpus-based approach to variation is restricted to the specific domains or registers that are present in the corpus. To what degree is such a model of variation limited to a specific register? This paper
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-ccd23a5b26dfda9c31794eaa714f19cc9e61f43f91277f6a592fdda5aaeaceba

Passage ID: `qasper-passage-v1-ccd23a5b26dfda9c31794eaa714f19cc9e61f43f91277f6a592fdda5aaeaceba`; retrieval score: 4.868601075557692.

Word count: 200.

```text
at the end. This creates, in effect, one large umbrella-grammar that potentially over-represents a regional dialect. From the perspective of the grammar, we can think of false positives (the umbrella-grammar contains constructions that a regional dialect does not use) and false negatives (the umbrella-grammar is missing constructions that are important to a regional dialect). For dialect identification as a task, only missing constructions will reduce prediction performance.

How well do CxG-1 and CxG-2 represent the corpora from each regional variety? While prediction accuracies are the ultimate evaluation, we can also look at the average frequency across all constructions for each national dialect. Because the samples are fixed in length, we would expect the same frequencies across all dialects. On the other hand, false positive constructions (which are contained in the umbrella-grammar but do not occur frequently in a national dialect) will reduce the overall feature density for that dialect. Because the classification results do not directly evaluate false positive constructions, we investigate this in Table 4 using the average feature density: the total average frequency per sample, representing how many syntactic constructions from the umbrella-grammar are present in each regional dialect. This is adjusted to show differences from the average
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 907.

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

#### Rank 1: qasper-passage-v1-21a91023719c690722b7257e66a10b0645944902f3ca65df6cd412af9a326b53

Passage ID: `qasper-passage-v1-21a91023719c690722b7257e66a10b0645944902f3ca65df6cd412af9a326b53`; retrieval score: 8.349886459787035.

Word count: 200.

```text
Many machine reading comprehension (MRC) datasets have been released in recent years BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4 to benchmark a system's ability to understand and reason over natural language. Typically, these datasets require an MRC model to read through a document to answer a question about information contained therein.

The supporting document is, more often than not, static and fully observable. This raises concerns, since models may find answers simply through shallow pattern matching; e.g., syntactic similarity between the words in questions and documents. As pointed out by BIBREF5, for questions starting with when, models tend to predict the only date/time answer in the supporting document. Such behavior limits the generality and usefulness of MRC models, and suggests that they do not learn a proper `understanding' of the intended task. In this paper, to address this problem, we shift the focus of MRC data away from `spoon-feeding' models with sufficient information in fully observable, static documents. Instead, we propose interactive versions of existing MRC tasks, whereby the information needed to answer a question must be gathered sequentially.

The key idea behind our proposed interactive MRC (iMRC) is to restrict the document context that a model observes at one time. Concretely,
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1908.10449:0:2` | partial | 0:138 |

#### Rank 2: qasper-passage-v1-8c0895c1986b97a964c5b9486055f3729a8bd5b93b481781b2fd3349a68ecf7e

Passage ID: `qasper-passage-v1-8c0895c1986b97a964c5b9486055f3729a8bd5b93b481781b2fd3349a68ecf7e`; retrieval score: 5.459706332582527.

Word count: 200.

```text
Skip-reading BIBREF6, BIBREF7, BIBREF8 is an existing setting in which MRC models read partial documents. Concretely, these methods assume that not all tokens in the input sequence are useful, and therefore learn to skip irrelevant tokens based on the current input and their internal memory. Since skipping decisions are discrete, the models are often optimized by the REINFORCE algorithm BIBREF9. For example, the structural-jump-LSTM proposed in BIBREF10 learns to skip and jump over chunks of text. In a similar vein, BIBREF11 designed a QA task where the model reads streaming data unidirectionally, without knowing when the question will be provided. Skip-reading approaches are limited in that they only consider jumping over a few consecutive tokens and the skipping operations are usually unidirectional. Based on the assumption that a single pass of reading may not provide sufficient information, multi-pass reading methods have also been studied BIBREF12, BIBREF13.

Compared to skip-reading and multi-turn reading, our work enables an agent to jump through a document in a more dynamic manner, in some sense combining aspects of skip-reading and re-reading. For example, it can jump forward, backward, or to an arbitrary position, depending on the query. This also distinguishes the model we develop in
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-723b985ab1489b1a25a025d2fe0b256b1eca83ee3f218600383aab28696a1433

Passage ID: `qasper-passage-v1-723b985ab1489b1a25a025d2fe0b256b1eca83ee3f218600383aab28696a1433`; retrieval score: 5.293844670399025.

Word count: 106.

```text
than the tree sampling action space in DocQN.

Closely related to iMRC is work by BIBREF15, in which the authors introduce a collection of synthetic tasks to train and test information-seeking capabilities in neural models. We extend that work by developing a realistic and challenging text-based task.

Broadly speaking, our approach is also linked to the optimal stopping problem in the literature Markov decision processes (MDP) BIBREF16, where at each time-step the agent either continues or stops and accumulates reward. Here, we reformulate conventional QA tasks through the lens of optimal stopping, in hopes of improving over the shallow matching behaviors exhibited by many MRC systems.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-541974ef08f339c533a29660ad124078c2baad99020e2455a7acfb38dd16c554

Passage ID: `qasper-passage-v1-541974ef08f339c533a29660ad124078c2baad99020e2455a7acfb38dd16c554`; retrieval score: 5.067761326266076.

Word count: 200.

```text
a document in a more dynamic manner, in some sense combining aspects of skip-reading and re-reading. For example, it can jump forward, backward, or to an arbitrary position, depending on the query. This also distinguishes the model we develop in this work from ReasoNet BIBREF13, where an agent decides when to stop unidirectional reading.

Recently, BIBREF14 propose DocQN, which is a DQN-based agent that leverages the (tree) structure of documents and navigates across sentences and paragraphs. The proposed method has been shown to outperform vanilla DQN and IR baselines on TriviaQA dataset. The main differences between our work and DocQA include: iMRC does not depend on extra meta information of documents (e.g., title, paragraph title) for building document trees as in DocQN; our proposed environment is partially-observable, and thus an agent is required to explore and memorize the environment via interaction; the action space in our setting (especially for the Ctrl+F command as defined in later section) is arguably larger than the tree sampling action space in DocQN.

Closely related to iMRC is work by BIBREF15, in which the authors introduce a collection of synthetic tasks to train and test information-seeking capabilities in neural models. We extend that work by
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-a141fcc19f85bb5bed7da4dc3ac21761dd92e403d38130d07f84cc342991003c

Passage ID: `qasper-passage-v1-a141fcc19f85bb5bed7da4dc3ac21761dd92e403d38130d07f84cc342991003c`; retrieval score: 4.92995898430162.

Word count: 121.

```text
iMRC games are interactive environments. We use an RL training algorithm to train the interactive information-gathering behavior of QA-DQN. We adopt the Rainbow algorithm proposed by BIBREF23, which integrates several extensions to the original Deep Q-Learning algorithm BIBREF24. Rainbox exhibits state-of-the-art performance on several RL benchmark tasks (e.g., Atari games).

During game playing, we use a mini-batch of size 10 and push all transitions (observation string, question string, generated command, reward) into a replay buffer of size 500,000. We do not compute losses directly using these transitions. After every 5 game steps, we randomly sample a mini-batch of 64 transitions from the replay buffer, compute loss, and update the network.

Detailed hyper-parameter settings for action generation are shown in Table TABREF38.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 827.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "33b2d26d064251c196238b0c3c455b208680f5fc": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1908.10449:0:2": [
        [
          138,
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

#### Rank 1: qasper-passage-v1-1c06891d218475cca26d761e6219b60ace7d16bbdc2035863d5c7ea9fd59463a

Passage ID: `qasper-passage-v1-1c06891d218475cca26d761e6219b60ace7d16bbdc2035863d5c7ea9fd59463a`; retrieval score: 5.694874440398552.

Word count: 200.

```text
annotation systems for the annotation of audio data. Among them we find light-weight systems, like the VIA software BIBREF9 or Praat on the web BIBREF10 that allow to build simple layers of annotations. However, they do not provide a proper management system for a pool of annotators nor do they integrate annotation checking.

On the other side of the spectrum, there are more sophisticated systems with various capabilities. Camomille BIBREF11 and the EMU-SDMS system (that can also be used offline) BIBREF12 allow to work with speech data and to distribute the tasks to several annotators. But these systems require expertise in web hosting and technologies to deploy and modify them.

Finally, WebAnno BIBREF13 and GATE Teamware BIBREF14 are the tools that most closely match our main contributions regarding quality control (conformity and consistency checking), annotators' management and flexibility. WebAnno includes consistency checking with the integration of different metrics BIBREF15. However, these tools have only been built for text data. The format and all the custom layers have been designed for Natural Language Processing tasks. Porting WebAnno to support speech data seemed a major engineering challenge. That is why it appeared necessary to develop a new and user-friendly tool addressed to
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-23158601a3bd6d59025b464453b6f0c6c5de2db46d985ff5b207f03848b0d703

Passage ID: `qasper-passage-v1-23158601a3bd6d59025b464453b6f0c6c5de2db46d985ff5b207f03848b0d703`; retrieval score: 4.885792135360335.

Word count: 200.

```text
Seshat was intially developped to study the impact of Huntington's Disease BIBREF17 on speech and language production. One hundred and fifty two interviews between a neuropsychologist and a patient with the Huntington's Disease (HD) were recorded between June 2018 and November 2019. The campaign manager created a campaign with multiple tiers to annotate the turn takings and the speech/non speech boundaries of the utterances of the patient. For both tasks, the annotations did not need to cover completely the audio (sparsity property mentioned above). For the Turn-taking annotations, there are 3 pre-defined tiers, each one with a single class ('Patient', 'Non-Patient', and 'Noise'), which results in possible overlap between these classes. For the Utterance annotations, there is only one pre-defined class ('Utterance').

To this date, a total of 67 files have been fully annotated with the help of Seshat by a cohort of 18 speech pathologist students (see Figure FIGREF33). Among these, 16 have been done by 2 different annotators independently with the Double-annotator task. The results are summarised in Table TABREF34.

Even though there are more categories for Turn-Takings than Utterance (gut2004measuring reported that the more categories the more the task is difficult in speech annotations), the mean $\gamma
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-75445759d682e9dafcffcad2c0c615fea0219f01936202b9dbf07b5251f31503

Passage ID: `qasper-passage-v1-75445759d682e9dafcffcad2c0c615fea0219f01936202b9dbf07b5251f31503`; retrieval score: 4.606048270682542.

Word count: 200.

```text
a Double Annotator Task (assigned to two annotators, who will annotatote the assigned task in parallel).

A set of rules defining the TextGrid files' structure and content of the annotations. It is set at the beginning of the Annotation Campaign's creation, and is used to enforce that all TextGrids from the campaign contain the same amount of Tiers, with the same names. It can also enforce, for certain chosen tiers, a set of valid annotations.

Users with the rights to create Annotation Campaigns and Annotators user accounts, and assign Annotation Tasks to Annotators.

Users who are assigned a set of Annotation Tasks. Their job is to complete the annotation of the audio files with the Praat software.

If the TextGrid file they submit does not comply with their Annotation Task's TextGrid Checking Scheme, Seshat pinpoint their annotation errors with detailed messages. The annotator can re-submit the concerned file to the platform based on these different feedbacks.

Once they they connected to their instance of Seshat, campaign managers can access ongoing annotation campaigns or create new ones. Campaign managers are able to add annotators, assign annotation tasks and track progress. Annotator see a list of assigned tasks. The first step for
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-6e6989338e13554afee2784e0088668def837f50e5bf101adbdfb7abfe15a8ae

Passage ID: `qasper-passage-v1-6e6989338e13554afee2784e0088668def837f50e5bf101adbdfb7abfe15a8ae`; retrieval score: 4.3131966870251555.

Word count: 160.

```text
The Campaign manager can easily define and monitor annotation campaign. As shown in Figure FIGREF33, the online form enable to choose corpora, pre-define and pre-configure the annotations scheme (tiers and parsers). There are 2 types of tiers already implemented by default: one with no check at all, and one with pre-defined categories. For the latter, these categories are pre-defined when the campaign is created.

Only Campaign managers can access and build new campaigns. If Campaign manager have several campaigns they can easily switch between them via the menu bar or get a full overview with the dashboard (See Figure FIGREF26). The campaign managers can visualise the progress of the assigned tasks at the campaign level or more precisely at the task level. They can retrieve all the intermediate files that have been created for each task. For instance, the campaign manager can examine qualitatively and quantitatively what are the annotation differences before the merge phases of the double annotator task.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-b9933e1b075d5a5320878cc1fd69ec265f3ca0669cd01e5006a55036fbab06ec

Passage ID: `qasper-passage-v1-b9933e1b075d5a5320878cc1fd69ec265f3ca0669cd01e5006a55036fbab06ec`; retrieval score: 3.967675308910258.

Word count: 43.

```text
format and all the custom layers have been designed for Natural Language Processing tasks. Porting WebAnno to support speech data seemed a major engineering challenge. That is why it appeared necessary to develop a new and user-friendly tool addressed to the speech community.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 803.

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

#### Rank 1: qasper-passage-v1-969fc9b28636c3e6776c7c5f08f43832c0933a2901d30dae974b7d88e4b90046

Passage ID: `qasper-passage-v1-969fc9b28636c3e6776c7c5f08f43832c0933a2901d30dae974b7d88e4b90046`; retrieval score: 8.105506788540701.

Word count: 129.

```text
edition of the Dialog State Tracking Challenge. In this paper, a latent decomposition type of approach is proposed in order to address this general problem of dialog system. Our method gives encouraging results in comparison to the state of the art dataset and also does not required complex inference at test time because, as detailed in Section "Spectral decomposition model for state tracking in slot-filling dialogs" , the tracking algorithm hold a linear complexity w.r.t the sum of realization of each considered variables defining the state to track which is what we believe is one of the main advantage of this method. Secondly collective matrix factorization paradigm also for data fusion and bias by data type of modeling as successfully performed in matrix factorization based recommender systems BIBREF30 .
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-5191029e6b136ce54dde0e0a95cd48cd9549769e6f971ab9c2994b327b6a82d0

Passage ID: `qasper-passage-v1-5191029e6b136ce54dde0e0a95cd48cd9549769e6f971ab9c2994b327b6a82d0`; retrieval score: 7.882151040161366.

Word count: 200.

```text
As a comparison to the state of the art methods, Table 1 presents accuracy results of the best Collective Matrix Factorization model, with a latent space dimension of 350, which has been determined by cross-validation on a development set, where the value of each slot is instantiated as the most probable w.r.t the inference procedure presented in Section "Spectral decomposition model for state tracking in slot-filling dialogs" . In our experiments, the variance is estimated using standard dataset reshuffling. The same results are obtained for several state of the art methods of generative and discriminative state tracking on this dataset using the publicly available results as reported in BIBREF22 . More precisely, as provided by the state-of-the-art approaches, the accuracy scores computes $p(s^*_{t+1}|s_t,z_t)$ commonly name the joint goal. Our proposition is compared to the 4 baseline trackers provided by the DSTC organisers. They are the baseline tracker (Baseline), the focus tracker (Focus), the HWU tracker (HWU) and the HWU tracker with “original” flag set to (HWU+) respectively. Then a comparison to a maximum entropy (MaxEnt) proposed in BIBREF23 type of discriminative model and finally a deep neural network (DNN) architecture proposed in BIBREF24 as reported also in BIBREF22 is presented.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1606.05286:9:0` | full | 0:1317 |

#### Rank 3: qasper-passage-v1-5f839491cd44d6a471c34caafcbcb0b9ca869a2c68df44be530bfb370876998d

Passage ID: `qasper-passage-v1-5f839491cd44d6a471c34caafcbcb0b9ca869a2c68df44be530bfb370876998d`; retrieval score: 6.69652752991169.

Word count: 58.

```text
In a first section, the dialog domain used for the evaluation of our dialog tracker is described and the different probability models used for the domain. In a second section, we present a first set of experimental results obtained through the proposed approach and its comparison to several reported results of approaches of the state of the art.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-3be7390140741f538dac98924ea7974367273820261151ef9aa56c57d0db661c

Passage ID: `qasper-passage-v1-3be7390140741f538dac98924ea7974367273820261151ef9aa56c57d0db661c`; retrieval score: 6.532480366320117.

Word count: 196.

```text
out for all possible state realizations in order to obtain the normalizing constant $\eta $ . This is not feasible for real dialog domains, which can have a large number of variables and possible variable instantiations. So, it is vital to the discriminative approach to reduce the size of the state space. For example, BIBREF13 proposes to restrict the set of possible state variables to those that appeared in NLU results. More recently, BIBREF14 assumes conditional independence between dialog state variables to address scalability issues and uses a conditional random field to track each variable separately. Finally, deep neural models, performing on a sliding window of features extracted from previous user turns, have also been proposed in BIBREF15 . Of the current literature, this family of approaches have proven to be the most efficient for publicly available state tracking datasets. In the next section, we present a decompositional approach of dialog state tracking that aims at reconciling the two main approaches of the state of the art while leveraging on the current advances of low-rank bilinear decomposition models, as recalled in BIBREF16 , that seems particularly adapted to the sparse nature of dialog state tracking tasks.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-208bcbfe618f33b176a292e96f882f0ea35239bd4755b8215baf48d0cc1764b8

Passage ID: `qasper-passage-v1-208bcbfe618f33b176a292e96f882f0ea35239bd4755b8215baf48d0cc1764b8`; retrieval score: 6.058343645911704.

Word count: 170.

```text
robustly even in the face of noisy conditions and ambiguity. In this paper, a statistical type of approach of state tracking is proposed by leveraging the recent progress of spectral decomposition methods formalized as bilinear algebraic decomposition and associated inference procedures. The proposed model estimates each state transition with respect to a set of observations and is able to compute the state transition through an inference procedure with a linear complexity with respect to the number of variables and observations.

Roadmap: This paper is structured as follows, Section "Generative Dialog State Tracking" formally defines transactional dialogs and describes the associated problem of statistical dialog state tracking with both the generative and discriminative approaches. Section "Spectral decomposition model for state tracking in slot-filling dialogs" depicts the proposed decompositional model for coupled and temporal hidden variable models and the associated inference procedure based on Collective Matrix Factorization (CMF). Finally, Section "Experimental settings and Evaluation" illustrates the approach with experimental results obtained using a state of the art benchmark for dialog state tracking.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 753.

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

#### Rank 1: qasper-passage-v1-ee00e5a0180ceb11f4f1c1a43868a032c29a9603ac39904cc162aef69bb05af2

Passage ID: `qasper-passage-v1-ee00e5a0180ceb11f4f1c1a43868a032c29a9603ac39904cc162aef69bb05af2`; retrieval score: 12.180317789534435.

Word count: 200.

```text
The explosion of available scientific articles in the Biomedical domain has led to the rise of Biomedical Information Extraction (BioIE). BioIE systems aim to extract information from a wide spectrum of articles including medical literature, biological literature, electronic health records, etc. that can be used by clinicians and researchers in the field. Often the outputs of BioIE systems are used to assist in the creation of databases, or to suggest new paths for research. For example, a ranked list of interacting proteins that are extracted from biomedical literature, but are not present in existing databases, can allow researchers to make informed decisions about which protein/gene to study further. Interactions between drugs are necessary for clinicians who simultaneously administer multiple drugs to their patients. A database of diseases, treatments and tests is beneficial for doctors consulting in complicated medical cases.

The main problems in BioIE are similar to those in Information Extraction:

This paper discusses, in each section, various methods that have been adopted to solve the listed problems. Each section also highlights the difficulty of Information Extraction tasks in the biomedical domain.

This paper is intended as a primer to Biomedical Information Extraction for current NLP researchers. It aims to
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-cdfb8862b420dbc35f139c54d58157a3ebe3cb97711ab779c42292cc295907cc

Passage ID: `qasper-passage-v1-cdfb8862b420dbc35f139c54d58157a3ebe3cb97711ab779c42292cc295907cc`; retrieval score: 4.869085339301215.

Word count: 78.

```text
have been adopted to solve the listed problems. Each section also highlights the difficulty of Information Extraction tasks in the biomedical domain.

This paper is intended as a primer to Biomedical Information Extraction for current NLP researchers. It aims to highlight the diversity of the various techniques from Information Extraction that have been applied in the Biomedical domain. The state of biomedical text mining is reviewed regularly. For more extensive surveys, consult BIBREF0 , BIBREF1 , BIBREF2 .
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-982fea0c1165080a782efe6b8d53215f13a1ec1e68447352a83ca32f5f066105

Passage ID: `qasper-passage-v1-982fea0c1165080a782efe6b8d53215f13a1ec1e68447352a83ca32f5f066105`; retrieval score: 4.53742618103248.

Word count: 200.

```text
concept mapping features using existing annotation tools, as well as Brown clustering to form 128 clusters over the unlabelled data. The dataset used is the i2b2 2010 challenge dataset. Their system achieves an F-Score of 0.85. BIBREF7 is an incremental paper on NER taggers. It uses 3 types of word-representation techniques (Brown clustering, distributional clustering, word vectors) to improve performance of the NER Conditional Random Field tagger, and achieves marginal F-Score improvements.

BIBREF8 propose a boostrapping mechanism to bootstrap biomedical ontologies using NELL BIBREF9 , which uses a coupled semi-supervised bootstrapping approach to extract facts from text, given an ontology and a small number of “seed” examples for each category. This interesting approach (called BioNELL) uses an ontology of over 100 categories. In contrast to NELL, BioNELL does not contain any relations in the ontology. BioNELL is motivated by the fact that a lot of scientific literature available online is highly reliable due to peer-review. The authors note that the algorithm used by NELL to bootstrap fails in BioNELL due to ambiguities in biomedical literature, and heavy semantic drift. One of the causes for this is that often common words such as “white”, “dad”, “arm” are used as names of
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1705.05437:1:2` | partial | 357:853 |

#### Rank 4: qasper-passage-v1-b98d7db7c8243e8bca82e452e354064b3a5c9b455ddfd1a2745f31f40548bea5

Passage ID: `qasper-passage-v1-b98d7db7c8243e8bca82e452e354064b3a5c9b455ddfd1a2745f31f40548bea5`; retrieval score: 3.892762191879945.

Word count: 200.

```text
Named Entity Recognition (NER) in the Biomedical domain usually includes recognition of entities such as proteins, genes, diseases, treatments, drugs, etc. Fact extraction involves extraction of Named Entities from a corpus, usually given a certain ontology. When compared to NER in the domain of general text, the biomedical domain has some characteristic challenges:

Some of the earliest systems were heavily dependent on hand-crafted features. The method proposed in BIBREF4 for recognition of protein names in text does not require any prepared dictionary. The work gives examples of diversity in protein names and lists multiple rules depending on simple word features as well as POS tags.

BIBREF5 adopt a machine learning approach for NER. Their NER system extracts medical problems, tests and treatments from discharge summaries and progress notes. They use a semi-Conditional Random Field (semi-CRF) BIBREF6 to output labels over all tokens in the sentence. They use a variety of token, context and sentence level features. They also use some concept mapping features using existing annotation tools, as well as Brown clustering to form 128 clusters over the unlabelled data. The dataset used is the i2b2 2010 challenge dataset. Their system achieves an F-Score of 0.85. BIBREF7 is an incremental
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1705.05437:1:2` | partial | 1:610 |

#### Rank 5: qasper-passage-v1-3d546ace1050ccea556d4c881f6a1a1a800f80c6b1c982efe8a583ed00b352c2

Passage ID: `qasper-passage-v1-3d546ace1050ccea556d4c881f6a1a1a800f80c6b1c982efe8a583ed00b352c2`; retrieval score: 3.803929118635743.

Word count: 200.

```text
features. An SVM classifier is then trained on the feature vectors, with a positive label if the drug pair interacts, and negative otherwise. Their method beats other systems on the DDI-2013 dataset. Some other feature-based approaches are described in BIBREF21 , BIBREF22 .

Distant supervision methods have also been applied to relation extraction over biomedical corpora. In BIBREF23 , 10,000 neuroscience articles are distantly supervised using information from UMLS Semantic Network to classify brain-gene relations into geneExpression and otherRelation. They use lexical (bag of words, contextual) features as well as syntactic (dependency parse features). They make the “at-least one” assumption, i.e. at least one of the sentences extracted for a given entity-pair contains the relation in database. They model it as a multi-instance learning problem and adopt a graphical model similar to BIBREF24 . They test using manually annotated examples. They note that the F-score achieved are much lesser than that achieved in the general domain in BIBREF24 , and attribute to generally poorer performance of NER tools in the biomedical domain, as well as less training examples. BIBREF25 explore distant supervision methods for protein-protein interaction extraction.

More recently, deep learning methods have been applied to relation extraction in the
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 878.

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

#### Rank 1: qasper-passage-v1-f927e70723e7d5f1bc814483e0d70108b501bc83449974cbb183bb5cde30d91f

Passage ID: `qasper-passage-v1-f927e70723e7d5f1bc814483e0d70108b501bc83449974cbb183bb5cde30d91f`; retrieval score: 4.7103646927847445.

Word count: 200.

```text
the benefit of being very challenging even when they are gathered from natural sources.

Natural language inference is also a well studied area of research, particularly on the MultiNLI BIBREF21 and SNLI BIBREF22 datasets. Other sources of entailment data include the PASCAL RTE challenges BIBREF23 , BIBREF24 or SciTail BIBREF25 . We note that, although SciTail, RTE-6 and RTE-7 did not use crowd workers to generate candidate statements, they still use sources (multiple choices questions or document summaries) that were written by humans with knowledge of the premise text. Using naturally occurring yes/no questions ensures even greater independence between the questions and premise text, and ties our dataset to a clear end-task. BoolQ also requires detecting entailment in paragraphs instead of sentence pairs.

Transfer learning for entailment has been studied in GLUE BIBREF7 and SentEval BIBREF26 . Unsupervised pre-training in general has recently shown excellent results on many datasets, including entailment data BIBREF9 , BIBREF8 , BIBREF27 .

Converting short-answer or multiple choice questions into entailment examples, as we do when experimenting with transfer learning, has been proposed in several prior works BIBREF28 , BIBREF29 , BIBREF25 . In this paper we found some evidence suggesting that these approaches are
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-3fb922d9fddb7aa395cfa4102b41dce3acbe82e1e3df873a27a5ae51936421a3

Passage ID: `qasper-passage-v1-3fb922d9fddb7aa395cfa4102b41dce3acbe82e1e3df873a27a5ae51936421a3`; retrieval score: 4.184800061280734.

Word count: 130.

```text
sufficient to just transfer from powerful pre-trained language models such as BERT BIBREF8 or ELMo BIBREF9 . We experiment with state-of-the-art unsupervised approaches, using existing entailment datasets, three methods of leveraging extractive QA data, and using a few other supervised datasets.

We found that transferring from MultiNLI, and the unsupervised pre-training in BERT, gave us the best results. Notably, we found these approaches are surprisingly complementary and can be combined to achieve a large gain in performance. Overall, our best model reaches 80.43% accuracy, compared to 62.31% for the majority baseline and 90% human accuracy. In light of the fact BERT on its own has achieved human-like performance on several NLP tasks, this demonstrates the high degree of difficulty of our dataset. We present our data and code at https://goo.gl/boolq.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-13f4c41584c35b2a70edc664c0746bdade0ac29fa72b29efbde78b1b94b453b1

Passage ID: `qasper-passage-v1-13f4c41584c35b2a70edc664c0746bdade0ac29fa72b29efbde78b1b94b453b1`; retrieval score: 4.02818803797692.

Word count: 102.

```text
Books corpus BIBREF36 .

Our BERTL model fine-tunes the 24 layer 1024 dimensional transformer from BIBREF8 , which has been trained on next-sentence-selection and masked language modelling on the Book Corpus and Wikipedia.

We fine-tune the BERTL and the OpenAI GPT models using the optimizers recommended by the authors, but found it important to tune the optimization parameters to achieve the best results. We use a batch size of 24, learning rate of 1e-5, and 5 training epochs for BERT and a learning rate of 6.25e-5, batch size of 6, language model loss of 0.5, and 3 training epochs for OpenAI GPT.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1905.10044:11:3` | partial | 159:182 |

#### Rank 4: qasper-passage-v1-3c28b8d62fb4ac81eca9a97829f4a096ccf9740b0b24ea884e778488330e4ba1

Passage ID: `qasper-passage-v1-3c28b8d62fb4ac81eca9a97829f4a096ccf9740b0b24ea884e778488330e4ba1`; retrieval score: 3.997141406021207.

Word count: 200.

```text
that simply asking human annotators to write candidate statements will result in examples that typically only require surface-level reasoning.

In this paper we propose an alternative: we test models on their ability to answer naturally occurring yes/no questions. That is, questions that were authored by people who were not prompted to write particular kinds of questions, including even being required to write yes/no questions, and who did not know the answer to the question they were asking. Figure contains some examples from our dataset. We find such questions often query for non-factoid information, and that human annotators need to apply a wide range of inferential abilities when answering them. As a result, they can be used to construct highly inferential reading comprehension datasets that have the added benefit of being directly related to the practical end-task of answering user yes/no questions.

Yes/No questions do appear as a subset of some existing datasets BIBREF3 , BIBREF4 , BIBREF5 . However, these datasets are primarily intended to test other aspects of question answering (QA), such as conversational QA or multi-step reasoning, and do not contain naturally occurring questions.

We follow the data collection method used by Natural Questions (NQ) BIBREF6 to gather
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-b1f8ad5a198a33930f12934d330ec8794c758e737caea23453efac20fac1f3ef

Passage ID: `qasper-passage-v1-b1f8ad5a198a33930f12934d330ec8794c758e737caea23453efac20fac1f3ef`; retrieval score: 3.9933740592732625.

Word count: 200.

```text
the resulting annotations is unknown. We also found the resulting dataset is class imbalanced, with 80% “yes" answers.

Yes/No QA has been used in other contexts, such as the templated bAbI stories BIBREF12 or some Visual QA datasets BIBREF13 , BIBREF14 . We focus on answering yes/no questions using natural language text.

Question answering for reading comprehension in general has seen a great deal of recent work BIBREF15 , BIBREF16 , and there have been many recent attempts to construct QA datasets that require advanced reasoning abilities BIBREF5 , BIBREF17 , BIBREF18 , BIBREF19 , BIBREF20 . However, these attempts typically involve engineering data to be more difficult by, for example, explicitly prompting users to write multi-step questions BIBREF5 , BIBREF18 , or filtering out easy questions BIBREF19 . This risks resulting in models that do not have obvious end-use applications since they are optimized to perform in an artificial setting. In this paper, we show that yes/no questions have the benefit of being very challenging even when they are gathered from natural sources.

Natural language inference is also a well studied area of research, particularly on the MultiNLI BIBREF21 and SNLI BIBREF22 datasets. Other sources of entailment data include
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 832.

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
          159
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

#### Rank 1: qasper-passage-v1-d92e44d3685d27953c348d7d078621d809976a2af0df4f48945eaee76f5c3eaf

Passage ID: `qasper-passage-v1-d92e44d3685d27953c348d7d078621d809976a2af0df4f48945eaee76f5c3eaf`; retrieval score: 2.9125361610174028.

Word count: 200.

```text
the state. As depicted in fig: nuisance scenarios, inflating the state space with task-nuisances impairs the performance of all representations. There, a large amount of unnecessary objects were spawned in the level, increasing the state's description length to over 250 words, whilst retaining the same amount of useful information. Nevertheless, the NLP representation outperformed the vision and feature based representations, with high robustness to the applied noise.

In order to verify the performance of the natural language representation was not due to extensive discretization of patches, we've conducted experiments increasing the number of horizontal patches - ranging from 3 to 31 patches in the extreme case. Our results, as depicted in fig: patch count, indicate that the amount of discretization of patches did not affect the performance of the NLP agent, remaining a superior representation compared to the rest.

To conclude, our experiments suggest that NLP representations, though they describe the same raw information of the semantic segmentation maps, are more robust to task-nuisances, allow for better transfer, and achieve higher performance in complex tasks, even when their description is long and convoluted. While we've only presented results for DQN agents, we include plots for a PPO agent in the
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-8e8c909a357601e2197ef3cd417d4a50536e4553bfc22b625066010c7f5a1d98

Passage ID: `qasper-passage-v1-8e8c909a357601e2197ef3cd417d4a50536e4553bfc22b625066010c7f5a1d98`; retrieval score: 2.8236704779686765.

Word count: 200.

```text
Work on representation learning is concerned with finding an appropriate representation of data in order to perform a machine learning task BIBREF33. In particular, deep learning exploits this concept by its very nature BIBREF2. Work on representation learning include Predictive State Representations (PSR) BIBREF34, BIBREF35, which capture the state as a vector of predictions of future outcomes, and a Heuristic Embedding of Markov Processes (HEMP) BIBREF36, which learns to embed transition probabilities using an energy-based optimization problem.

There has been extensive work attempting to use natural language in RL. Efforts that integrate language in RL develop tools, approaches, and insights that are valuable for improving the generalization and sample efficiency of learning agents. Previous work on language-conditioned RL has considered the use of natural language in the observation and action space. Environments such as Zork and TextWorld BIBREF37 have been the standard benchmarks for testing text-based games. Nevertheless, these environments do not search for semantic state representations, in which an RL algorithm can be better evaluated and controlled.

BIBREF38 use high-level semantic abstractions of documents in a representation to facilitate relational learning using Inductive Logic Programming and a generative language model. BIBREF39 use high-level guidance expressed in text to enrich
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-b17f125b8e4c0935e7555ff1e6812e67bddb2051d4c0b1741e9e6befdde8b829

Passage ID: `qasper-passage-v1-b17f125b8e4c0935e7555ff1e6812e67bddb2051d4c0b1741e9e6befdde8b829`; retrieval score: 2.006900317236124.

Word count: 200.

```text
To convert each frame to a natural language representation state, the list of available labels is iterated, and a string is built accordingly. The main idea of our implementation is to divide the screen into multiple vertical patches, count the amount of different objects inside by their types, and parse it as a sentence. The decision as to whether an object is close or far can be determined by calculating the distance from it to the player, and using two threshold levels. Object descriptions can be concise or detailed, as needed. We experimented with the following mechanics:

the screen can be divided between patches equally, or by determined ratios. Here, our main guideline was to keep the "front" patch narrow enough so it can be used as "sights".

our initial experiment was with 3 patches, and later we added 2 more patches classified as "outer left" and "outer right". In our experiments we have tested up to 51 patches, referred to as left or right patch with corresponding numbers.

we used 2 thresholds, which allowed us to classify the distance of an object from the player as "close","mid", and "far. Depending on the task, the value of the threshold can
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-93af31de1d5e80079e862fac3d7d8e5d97832624b74d61678b8420f0f8a09b80

Passage ID: `qasper-passage-v1-93af31de1d5e80079e862fac3d7d8e5d97832624b74d61678b8420f0f8a09b80`; retrieval score: 2.0020182279879593.

Word count: 200.

```text
the agent can pick up and use, such as medipacks, shotguns, ammunition and armor. Furthermore, the room is filled with unusable objects, various types of trees, pillars and other decorations. The agent can freely move and turn in any direction, as well as shoot. This scenario combines elements from all of the previous scenarios.

Our agent was implemented using a Convolutional Neural Network as described in Section SECREF4. We converted the parsed state into embedded representations of fixed length. We tested both a DQN and a PPO based agent, and compared the natural language representation to the other representation techniques, namely the raw image, feature vector, and semantic segmentation representations.

In order to effectively compare the performance of the different representation methods, we conducted our experiments under similar conditions for all agents. The same hyper-parameters were used under all tested representations. Moreover, to rule out effects of architectural expressiveness, the number of weights in all neural networks was approximately matched, regardless of the input type. Finally, we ensured the “super" scenario was positively biased toward image-based representations. This was done by adding a large amount items to the game level, thereby filling the state with nuisances (these tests are denoted
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-030fa6ac5bbd8ff34b85ffb0c7804ad6af664891216980e7ad7500ba1c6ef5a7

Passage ID: `qasper-passage-v1-030fa6ac5bbd8ff34b85ffb0c7804ad6af664891216980e7ad7500ba1c6ef5a7`; retrieval score: 0.0.

Word count: 200.

```text
We tested the natural language representation against the visual-based and feature representations on several tasks, with varying difficulty. In these tasks, the agent could navigate, shoot, and collect items such as weapons and medipacks. Often, enemies of different types attacked the agent, and a positive reward was given when an enemy was killed. Occasionally, the agent also suffered from health degeneration. The tasks included a basic scenario, a health gathering scenario, a scenario in which the agent must take cover from fireballs, a scenario in which the agent must defend itself from charging enemies, and a super scenario, where a mixture of the above scenarios was designed to challenge the agent.

More specifically, in the basic scenario, a single monster is spawned in front of the agent. The purpose of this scenario is to teach the agent to aim at the enemy and shoot at it. In the health gathering scenario, the floor of the room is covered in toxin, causing the agent to gradually lose health. Medipacks are spawned randomly in the room and the agent's objective is to keep itself alive by collecting them. In the take cover scenario, multiple fireball shooting monsters are spawned in front of
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1910.02789:5:0` | full | 0:713 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1000.

Fully covered answer annotations: fc219faad4cbdc4a0d17a5c4e30b187b5b08fd05.

Missing evidence by answer annotation:

```text
{
  "fc219faad4cbdc4a0d17a5c4e30b187b5b08fd05": {
    "unresolved_evidence": [],
    "paragraphs": {}
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

#### Rank 1: qasper-passage-v1-ec2ca4227b75033730cd9c92b45ba67178367beebbcce8f0060ea41e5e33bfd9

Passage ID: `qasper-passage-v1-ec2ca4227b75033730cd9c92b45ba67178367beebbcce8f0060ea41e5e33bfd9`; retrieval score: 6.747241538532782.

Word count: 151.

```text
stories.

To this end, we introduce a system which aggregates news articles into fine-grained story clusters across different languages in a completely online and scalable fashion from a continuous stream. Our clustering approach is part of a larger media monitoring project to solve the problem of monitoring massive text and TV/Radio streams (speech-to-text). In particular, media monitors write intelligence reports about the most relevant events, and being able to search, visualize and explore news clusters assists in gathering more insight about a particular story. Since relevant events may be spawned from any part of the world (and from many multilingual sources), it becomes imperative to cluster news across different languages.

In terms of granularity, the type of story clusters we are interested in are the group of articles which, for example : (i) Narrate recent air-strikes in Eastern Ghouta (Syria); (ii) Describe the recent launch of Space X's Falcon Heavy rocket.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-a07086022cf92af091436eb8237d3b314291900b5367656fd745316d1a4c959a

Passage ID: `qasper-passage-v1-a07086022cf92af091436eb8237d3b314291900b5367656fd745316d1a4c959a`; retrieval score: 6.228058717728661.

Word count: 200.

```text
Our system was designed to cluster documents from a (potentially infinite) real-word data stream. The datasets typically used in the literature (TDT, Reuters) have a small number of clusters ( INLINEFORM0 20) with coarse topics (economy, society, etc.), and therefore are not relevant to the use case of media monitoring we treat - as it requires much more fine-grained story clusters about particular events. To evaluate our approach, we adapted a dataset constructed for the different purpose of binary classification of joining cluster pairs. We processed it to become a collection of articles annotated with monolingual and crosslingual cluster labels.

Statistics about this dataset are given in Table TABREF30 . As described further, we tune the hyper-parameter INLINEFORM0 on the development set. As for the hyper-parameters related to the timestamp features, we fixed INLINEFORM1 and tuned INLINEFORM2 on the development set, yielding INLINEFORM3 . To compute IDF scores (which are global numbers computed across a corpus), we used a different and much larger dataset that we collected from Deutsche Welle's news website (http://www.dw.com/). The dataset consists of 77,268, 118,045 and 134,243 documents for Spanish, English and German, respectively.

The conclusions from our experiments are: (a) the weighting of the similarity
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1809.00540:6:1` | full | 0:601 |

#### Rank 3: qasper-passage-v1-8094d0e6f76c1f23582b4c336997ad9816309af29839c81266187591d9c035d1

Passage ID: `qasper-passage-v1-8094d0e6f76c1f23582b4c336997ad9816309af29839c81266187591d9c035d1`; retrieval score: 6.07495495686363.

Word count: 200.

```text
than representing the documents the way is described in § SECREF4 . Furthermore, it was also significantly slower than our algorithm due to the time it took to perform singular value decomposition.

Table TABREF35 gives the final monolingual results on the three datasets. For English, we see that the significant improvement we get using our algorithm over the algorithm of aggarwal2006framework is due to an increased recall score. We also note that the trained models surpass the baseline for all languages, and that the timestamp feature (denoted by TS), while not required to beat the baseline, has a very relevant contribution in all cases. Although the results for both the baseline and our models seem to differ across languages, one can verify a consistent improvement from the latter to the former, suggesting that the score differences should be mostly tied to the different difficulty found across the datasets for each language. The presented scores show that our learning framework generalizes well to different languages and enables high quality clustering results.

To investigate the impact of the timestamp features, we ran an additional experiment using only the same three timestamp features as used in the best model on the English dataset.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-4dd068e52d1252e002a8729bd9ec0f15baefe4b6e2c1670a2a8eccd6a9c94bba

Passage ID: `qasper-passage-v1-4dd068e52d1252e002a8729bd9ec0f15baefe4b6e2c1670a2a8eccd6a9c94bba`; retrieval score: 4.343434150659756.

Word count: 200.

```text
In § SECREF19 we introduced INLINEFORM0 and INLINEFORM1 as the weight vectors for the several document representation features. We experiment with both setting these weights to just 1 ( INLINEFORM2 and INLINEFORM3 ) and also learning these weights using support vector machines (SVMs). To generate the SVM training data, we simulate the execution of the algorithm on a training data partition (which we do not get evaluated on) and in which the gold standard labels are given. We run the algorithm using only the first subvector INLINEFORM4 , which is the TF-IDF vector with the words of the document in the body and title. For each incoming document, we create a collection of positive examples, for the document and the clusters which share at least one document in the gold labeling. We then generate 20 negative examples for the document from the 20 best-matching clusters which are not correct. To find out the best-matching clusters, we rank them according to their similarity to the input document using only the first subvector INLINEFORM5 .

Using this scheme we generate a collection of ranking examples (one for each document in the dataset, with the ranking of the best cluster matches), which are
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-51c7dcd9e084096d5a9c288d35397aea12becedbf111d3f40172be33c7413fde

Passage ID: `qasper-passage-v1-51c7dcd9e084096d5a9c288d35397aea12becedbf111d3f40172be33c7413fde`; retrieval score: 4.226208653091501.

Word count: 200.

```text
Our similarity metric computes weighted cosine similarity on the different subvectors, both in the case of monolingual clustering and crosslingual clustering. Formally, for the monolingual case, the similarity is given by a function defined as: DISPLAYFORM0

and is computed on the TF-IDF subvectors where INLINEFORM0 is the number of subvectors for the relevant document representation. For the crosslingual case, we discuss below the function INLINEFORM1 , which has a similar structure.

Here, INLINEFORM0 is the INLINEFORM1 th document in the stream and INLINEFORM2 is a monolingual cluster. The function INLINEFORM3 returns the cosine similarity between the document representation of the INLINEFORM4 th document and the centroid for cluster INLINEFORM5 . The vector INLINEFORM6 denotes the weights through which each of the cosine similarity values for each subvectors are weighted, whereas INLINEFORM7 denotes the weights for the timestamp features, as detailed further. Details on learning the weights INLINEFORM8 and INLINEFORM9 are discussed in § SECREF26 .

The function INLINEFORM0 that maps a pair of document and cluster to INLINEFORM1 is defined as follows. Let DISPLAYFORM0

for a given INLINEFORM0 and INLINEFORM1 . For each document INLINEFORM2 and cluster INLINEFORM3 , we generate the following three-dimensional vector INLINEFORM4 :

INLINEFORM0 where INLINEFORM1
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 951.

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

#### Rank 1: qasper-passage-v1-637deb3dfa745dd28b32395ed680ab396daf61ba71487097574a6b7b09901013

Passage ID: `qasper-passage-v1-637deb3dfa745dd28b32395ed680ab396daf61ba71487097574a6b7b09901013`; retrieval score: 4.257519742036263.

Word count: 95.

```text
Figure FIGREF1 shows the architecture of the Sequicity framework as described in BIBREF8. In essence, in each turn, the Sequicity model first takes a bspan ($B_1$) and a response ($R_1$) which are determined in the previous step, and the current human question ($U_2$) to generate the current bspan. This bspan is then used together with a knowledge base to generate the corresponding machine answer ($R_2$), as shown in the right part of Figure FIGREF1.

The left part of that figure shows an example dialogue in a mixed-domain setting (which will be explained in Section SECREF3).
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-3ca9885861dac248f04317c572ba008da45f57eb99e0273be878c23cb7b7b240

Passage ID: `qasper-passage-v1-3ca9885861dac248f04317c572ba008da45f57eb99e0273be878c23cb7b7b240`; retrieval score: 2.670034602999894.

Word count: 200.

```text
This method has been shown not only to scale well to multi-domain dialogues, but also outperform existing state-of-the-art models in single-domain tracking tasks.

The problem that we are interested in this work is task-oriented dialogue in mixed-domain settings. This is different from the multi-domain dialogue problem above in several aspects, as follows:

First, we investigate the phenomenon of alternating between different dialogue domains in subsequent dialogue turns, where each turn is defined as a pair of user question and machine answer. That is, the domains are mixed between turns. For example, in the first turn, the user requests some information of a restaurant; then in the second turn, he switches to the a different domain, for example, he asks about the weather at a specific location. In a next turn, he would either switch to a new domain or come back to ask about some other property of the suggested restaurant. This is a realistic scenario which usually happens in practical chatbot applications in our observations. We prefer calling this problem mixed-domain dialogue rather than multiple-domain dialogue.

Second, we study the effect of the mixed-domain setting in the context of multi-domain dialogue approaches to see how they perform in different
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-12c955a28222b08873f3fc41f07df293ffae775df2a773bd665c2684b2d01cc6

Passage ID: `qasper-passage-v1-12c955a28222b08873f3fc41f07df293ffae775df2a773bd665c2684b2d01cc6`; retrieval score: 2.563985416937529.

Word count: 192.

```text
practical chatbot applications in our observations. We prefer calling this problem mixed-domain dialogue rather than multiple-domain dialogue.

Second, we study the effect of the mixed-domain setting in the context of multi-domain dialogue approaches to see how they perform in different experimental scenarios.

The main findings of this work include:

A specialized state tracking component in multiple domains still plays an important role and gives better results than a state-of-the-art end-to-end task-oriented dialogue system.

A combination of specialized state tracking system and an end-to-end task-oriented dialogue system is beneficial in mix-domain dialogue systems. Our hybrid system is able to improve the belief tracking accuracy of about 28% of average absolute point on a standard multi-domain dialogue dataset.

These experimental results give some useful insights on data preparation and acquisition in the development of the chatbot platform FPT.AI, which is currently deployed for many practical chatbot applications.

The remainder of this paper is structured as follows. First, Section SECREF2 discusses briefly the two methods in building dialogue systems that our method relies on. Next, Section SECREF3 presents experimental settings and results. Finally, Section SECREF4 concludes the paper and gives some directions for future work.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-187012a7f1522e2927224f26fc4deb8fd75825fa4e040fc9c6a80c6e4c7666d8

Passage ID: `qasper-passage-v1-187012a7f1522e2927224f26fc4deb8fd75825fa4e040fc9c6a80c6e4c7666d8`; retrieval score: 2.5319232271426775.

Word count: 173.

```text
GRU unit is also better than the RNN unit on response generation in terms of BLEU scores.

We also see that the task-oriented dialogue system has difficulty running on mixed-domain dataset; it achieves only about 75.62% of Success F1 in comparison to about 81.1% (as reported in the Sequicity paper, not shown in our table). Appendix SECREF5 shows some example dialogues generated automatically by our implemented system.

In the second series of experiments, we evaluate the belief tracking components of two systems, the specialized multi-domain belief tracker and the Sequicity bspan component. As shown in the lower half of the Table TABREF21, Sequicity capability of belief tracking is much worse than that of the multi-domain belief tracker. The slot accuracy gap between the tools is about 21.6%, the value accuracy gap is about 34.4%; that is a large average gap of 28% of accuracy. This result suggests a future work on combining a specialized belief tracking module with an end-to-end task-oriented dialogue system to improve further the performance of the overall dialogue system.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-78b505b845a9c64cca68d59de911905dcd796b4367230303a0cb380fc93e9d68

Passage ID: `qasper-passage-v1-78b505b845a9c64cca68d59de911905dcd796b4367230303a0cb380fc93e9d68`; retrieval score: 2.4753365328755197.

Word count: 86.

```text
example demonstrates a weakness of the system when being trained on a mixed-domain dataset. In the fifth turn, since the system does not recognize the value fastest in the bspan, it generates a random and wrong value moderate traffic. Note that the generated answer of the sixth turn is correct despite of the wrong predicted bspan; however, it is likely that if the dialogue continues, this wrong bspan may result in more answer mistakes. In such situations, multi-domain belief tracker usually performs better at bspan prediction.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 746.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "80b456e9541dcdfb561a6a0f4e806a685bee97dd": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1909.02265:5:0": [
        [
          0,
          434
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-aa6a2f4f682aa2ad1f0d5f70f95974ecc7e64a6b5daa0d78fda7c713a2a7077e

Passage ID: `qasper-passage-v1-aa6a2f4f682aa2ad1f0d5f70f95974ecc7e64a6b5daa0d78fda7c713a2a7077e`; retrieval score: 9.148136751608241.

Word count: 200.

```text
The experiments presented here extend and refine a line of research investigating what linguistic knowledge is acquired by neural language models. Previous studies have demonstrated that sequential models trained on a simple regime of optimizing the next word can learn long-distance syntactic dependencies in impressive detail. Our results provide complimentary insights, demonstrating that a range of model architectures trained on a variety of datasets can learn fine-grained information about the interaction of CoordNPs and local syntactic context, but their behavior remains unhumanlike in many key ways. Furthermore, to our best knowledge, this work presents the first psycholinguistic analysis of neural language models trained on French, a high-resource language that has so far been under-investigated in this line of research.

In the simple coordination experiment, we demonstrated that models were able to capture some of the agreement behaviors of humans, although their performance deviated in crucial aspects. Whereas human behavior is best modeled as a `percolation' process, the neural models appear to be using a linear combination of NP constituent number to drive CoordNP/verb number agreement, with the second noun weighted more heavily than the first. In these experiments, supervision afforded by the RNNG and ActionLSTM models did not translate into
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-6dd32f45797c819024685631e40f9dcf210987e5977ab9d1cb82c9cc255904a1

Passage ID: `qasper-passage-v1-6dd32f45797c819024685631e40f9dcf210987e5977ab9d1cb82c9cc255904a1`; retrieval score: 8.64751454947638.

Word count: 200.

```text
This section further investigates the effects of CoordNP annotation schemes on the behaviors of structurally-supervised models. We test whether an explicit COORD phrasal tag improves model performance. We trained two additional RNNG models on 38,546 sentences from the Penn Treebank annotated with two different schemes: The first, RNNG (PTB-control) was trained with the original Penn Treebank annotation. The second, RNNG (PTB-coord), was trained on the same sentences, but with an extended coordination annotation scheme, meant to employ the scheme employed in the FTB, adapted from BIBREF26. We stripped empty categories from their scheme and only kept the NP-COORD label for constituents inside a coordination structure. Figure FIGREF26 illustrates the detailed annotation differences between two datasets. We tested both models on all the experiments presented in Sections SECREF3-SECREF6 above.

Turning to the results of these six experiments: We see little difference between the two models in the Non-coordination agreement experiment. For the Complex coordination control and Complex coordination critical experiments, both models are largely the same as well. However, in the Simple and-coordination and Simple or-coordination experiments the values for all conditions are shifted upwards for the RNNG PTB-coord model, indicating higher over-all preference for the plural continuation. Furthermore, the range
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-82d51a52eea712fce506ecacc4f5c7fc805127e690934ba5f8cc2ced7a12e229

Passage ID: `qasper-passage-v1-82d51a52eea712fce506ecacc4f5c7fc805127e690934ba5f8cc2ced7a12e229`; retrieval score: 8.543097856729224.

Word count: 195.

```text
are trained to output the probability distribution of the upcoming word given a context, without explicitly representing the structure of the context BIBREF9, BIBREF10. We trained two two-layer recurrent neural language models with long short-term memory architecture BIBREF11 on a relatively small corpus. The first model, referred as `LSTM (PTB)' in the following sections, was trained on the sentences from Penn Treebank BIBREF12. The second model, referred as `LSTM (FTB)', was trained on the sentences from French Treebank BIBREF13. We set the size of input word embedding and LSTM hidden layer of both models as 256.

We also compare LSTM language models trained on large corpora. We incorporate two pretrained English language models: one trained on the Billion Word benchmark (referred as `LSTM (1B)') from BIBREF14, and the other trained on English Wikipedia (referred as `LSTM (enWiki)') from BIBREF3. For French, we trained a large LSTM language model (referred as `LSTM (frWaC)') on a random subset (about 4 million sentences, 138 million word tokens) of the frWaC dataset BIBREF15. We set the size of the input embeddings and hidden layers to 400 for the LSTM (frWaC) model since it is trained on a large dataset.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1909.04625:2:0` | full | 0:622 |
| `1909.04625:2:1` | full | 0:602 |

#### Rank 4: qasper-passage-v1-99f787c209cf776effe0debb65b8b46ac76b8c18de6100094af8c819b249648f

Passage ID: `qasper-passage-v1-99f787c209cf776effe0debb65b8b46ac76b8c18de6100094af8c819b249648f`; retrieval score: 6.756651618013193.

Word count: 200.

```text
In addition to using phrase-level features to drive expectation about downstream lexical items, human processors can do the inverse—use lexical features to drive expectations about upcoming syntactic chunks. In this experiment, we assess whether neural models use number features hosted on a verb to modulate their expectations for upcoming CoordNPs.

To assess whether neural language models learn inverted coordination rules, we adapted items from Section SECREF13 in both English (37 items) and French (24 items), following the paradigm in Table TABREF24. The first part of the phrase contains either a plural or singular verb and a plural or singular noun. In this case, we sample the surprisal for the continuations and (or is grammatical in all conditions, so it is omitted from this study). Our expectation is that `and' is less surprising in the Vpl_Nsg condition than in the Vsg_Nsg condition, where a CoordNP is not licensed by the grammar in either French or English (as in *What is the pig and the cat eating?). We also expect lower surprisal for and in the Vpl_Nsg condition, where it is obligatory for a grammatical continuation, than in the Vpl_Npl condition, where it is optional.

For French experimental items, the question is
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-f0f084f4c9487cb34c37157704cff7f14143966612e26545ac0cd53f523ad87a

Passage ID: `qasper-passage-v1-f0f084f4c9487cb34c37157704cff7f14143966612e26545ac0cd53f523ad87a`; retrieval score: 4.906052094044958.

Word count: 200.

```text
To determine whether state-of-the-art neural architectures are capable of learning humanlike CoordNP/verb agreement properties, we adopt the psycholinguistics paradigm for model assessment. In this paradigm the models are tested using hand-crafted sentences designed to test underlying network knowledge. The assumption here is that if a model implicitly learns humanlike linguistic knowledge during training, its expectations for upcoming words should qualitatively match human expectations in novel contexts. For example, BIBREF1 and BIBREF6 assessed how well neural models had learned the subject/verb number agreement by feeding them with the prefix The keys to the cabinet .... If the models predicted the grammatical continuation are over the ungrammatical continuation is, they can be said to have learned the number agreement insofar as the number of the head noun and not the number of the distractor noun, cabinet, drives expectations about the number of the matrix verb.

If models are able to robustly modulate their expectations based on the internal components of the CoordNP, this will provide evidence that the networks are building up a context-sensitive phrase-level representation. We quantify model expectations as surprisal values. Surprisal is the negative log-conditional probability $S(x_i) = -\log _2 p(x_i|x_1 \dots x_{i-1})$ of a sentence's $i^{th}$ word $x_i$
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 995.

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

#### Rank 1: qasper-passage-v1-fbeec7718824e7aaba8c8025bc90475304b72ead8233ee8a719698d8009f95f3

Passage ID: `qasper-passage-v1-fbeec7718824e7aaba8c8025bc90475304b72ead8233ee8a719698d8009f95f3`; retrieval score: 2.9463504297736924.

Word count: 200.

```text
In this paper, we present our work to support editors in the e-book annotation process. Specifically, we aim to provide tag recommendations that incorporate both the vocabulary of the editors and e-book readers. Therefore, we train various configurations of tag recommender approaches on editors' tags and Amazon search terms and evaluate them on a dataset containing Amazon review keywords. We find that combining both data sources enhances the quality of tag recommendations for annotating e-books. Furthermore, while approaches that train only on Amazon search terms provide poor performance concerning recommendation accuracy, we show that they still offer helpful annotations concerning recommendation diversity as well as our novel semantic similarity metric.

Future work. For future work, we plan to validate our findings using another dataset, e.g., by recommending tags for scientific articles and books in BibSonomy. With this, we aim to demonstrate the usefulness of the proposed approach in a similar domain and to enhance the reproducibility of our results by using an open dataset.

Moreover, we plan to evaluate our tag recommendation approaches in a study with domain users. Also, we want to improve our similarity-based approaches by integrating novel embedding approaches BIBREF16 , BIBREF17 as we did, for example,
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-23909dd0647293520d2916a1d95efb3de95a44ac75de1e6671efb8e58dc7aaf5

Passage ID: `qasper-passage-v1-23909dd0647293520d2916a1d95efb3de95a44ac75de1e6671efb8e58dc7aaf5`; retrieval score: 2.3986129498128825.

Word count: 124.

```text
evaluated popularity algorithms (i.e., INLINEFORM0 for INLINEFORM1 ). On the contrary, the combination of the two best performing similarity-based approaches INLINEFORM2 and INLINEFORM3 does not yield better accuracy. The negative impact of using a lower-performing approach such as INLINEFORM4 within a hybrid combination can also be observed in INLINEFORM5 for lower values of INLINEFORM6 . Overall, this confirms our initial intuition that combining the best performing popularity-based approach with the best similarity-based approach should result in the highest accuracy (i.e., INLINEFORM7 for INLINEFORM8 ). Moreover, our goal, namely to exploit editor tags in combination with search terms used by readers to increase the metadata quality of e-books, is shown to be best supported by applying hybrid approaches as they provide the best prediction results.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-fa9956fe46fa251c1051d4f32adb1c02e6f53c2de766bcbe2220da625cdb0720

Passage ID: `qasper-passage-v1-fa9956fe46fa251c1051d4f32adb1c02e6f53c2de766bcbe2220da625cdb0720`; retrieval score: 2.161437319819812.

Word count: 200.

```text
We implement three types of tag recommendation approaches, i.e., (i) popularity-based, (ii) similarity-based (i.e., using content information), and (iii) hybrid approaches. Due to the lack of personalized tags (i.e., we do not know which user has assigned a tag), we do not implement other types of algorithms such as collaborative filtering BIBREF8 . In total, we evaluate 19 different algorithms to recommend tags for annotating e-books.

Popularity-based approaches. We recommend the most frequently used tags in the dataset, which is a common strategy for tag recommendations BIBREF9 . That is, a most popular INLINEFORM0 approach for editor tags and a most popular INLINEFORM1 approach for Amazon search terms. For e-books, for which we also have author (= INLINEFORM2 and INLINEFORM3 ) or BISAC (= INLINEFORM4 and INLINEFORM5 ) information, we use these features to further filter the recommended tags, i.e., to only recommend tags that were used to annotate e-books of a specific author or a specific BISAC.

We combine both data sources (i.e., editor tags and Amazon search terms) using a round-robin combination strategy, which ensures an equal weight for both sources. This gives us three additional popularity-based algorithms (= INLINEFORM0 , INLINEFORM1 and INLINEFORM2 ).

Similarity-based approaches. We
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-d47b842dd0a7e97b4fbe5012f4a81a878fd3e388f78882c1af65d83068697d74

Passage ID: `qasper-passage-v1-d47b842dd0a7e97b4fbe5012f4a81a878fd3e388f78882c1af65d83068697d74`; retrieval score: 1.9621702896218371.

Word count: 200.

```text
using an open dataset.

Moreover, we plan to evaluate our tag recommendation approaches in a study with domain users. Also, we want to improve our similarity-based approaches by integrating novel embedding approaches BIBREF16 , BIBREF17 as we did, for example, with our proposed semantic similarity evaluation metric. Finally, we aim to incorporate explanations for recommended tags so that editors of e-book annotations receive additional support in annotating e-books BIBREF21 . By making the underlying (semantic) reasoning visible to the editor who is in charge of tailoring annotations, we aim to support two goals: (i) allowing readers to discover e-books more efficiently, and (ii) enabling publishers to leverage semi-automatic categorization processes for e-books. In turn, providing explanations fosters control over which vocabulary to choose when tagging e-books for different application contexts.

Acknowledgments. The authors would like to thank Peter Langs, Jan-Philipp Wolf and Alyona Schraa from HGV GmbH for providing the e-book annotation data. This work was funded by the Know-Center GmbH (FFG COMET Program), the FFG Data Market Austria project and the AI4EU project (EU grant 825619). The Know-Center GmbH is funded within the Austrian COMET Program - Competence Centers for Excellent Technologies - under the auspices of the Austrian
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-291801af92706f858d4aed92908034aa04088ad817918bbe76c487cdcf8190d3

Passage ID: `qasper-passage-v1-291801af92706f858d4aed92908034aa04088ad817918bbe76c487cdcf8190d3`; retrieval score: 1.6425410979444153.

Word count: 200.

```text
both data sources (i.e., editor tags and Amazon search terms) using a round-robin combination strategy, which ensures an equal weight for both sources. This gives us three additional popularity-based algorithms (= INLINEFORM0 , INLINEFORM1 and INLINEFORM2 ).

Similarity-based approaches. We exploit the textual content of e-books (i.e., description or title) to recommend relevant tags BIBREF10 . For this, we first employ a content-based filtering approach BIBREF11 based on TF-IDF BIBREF12 to find top- INLINEFORM0 similar e-books. For each of the similar e-books, we then either extract the assigned editor tags (= INLINEFORM2 and INLINEFORM3 ) or the Amazon search terms (= INLINEFORM4 and INLINEFORM5 ). To combine the tags of the top- INLINEFORM6 similar e-books, we use the cross-source algorithm BIBREF13 , which favors tags that were used to annotate more than one similar e-book (i.e., tags that come from multiple recommendation sources). The final tag relevancy is calculated as: DISPLAYFORM0

where INLINEFORM0 denotes the number of distinct e-books, which yielded the recommendation of tag INLINEFORM1 , to favor tags that come from multiple sources and INLINEFORM2 is the similarity score of the corresponding e-book. We again use a round-robin strategy to combine both data sources (= INLINEFORM3 and INLINEFORM4
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 924.

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

#### Rank 1: qasper-passage-v1-fe27899e2b6ca3e32ebcb62019e0639a58b6fd93cd4c3354e0c6711193ba4092

Passage ID: `qasper-passage-v1-fe27899e2b6ca3e32ebcb62019e0639a58b6fd93cd4c3354e0c6711193ba4092`; retrieval score: 7.81050291958746.

Word count: 173.

```text
BIBREF6.

In this paper, we present a simple architecture called holistic regularisation VAE (HR-VAE), which can effectively avoid latent variable collapse. In contrast to existing VAE-RNN models for text modelling which merely impose a standard normal distribution prior on the last hidden state of the RNN encoder, our HR-VAE model imposes regularisation for all hidden states of the RNN encoder. Another advantage of our model is that it is generic and can be applied to any existing VAE-RNN-based architectures.

We evaluate our model against several strong baselines which apply VAE for text modelling BIBREF0, BIBREF7, BIBREF5. We conducted experiments based on two public benchmark datasets, namely, the Penn Treebank dataset BIBREF9 and the end-to-end (E2E) text generation dataset BIBREF10. Experimental results show that our HR-VAE model not only can effectively mitigate the latent variable collapse issue with a stable training process, but also can give better predictive performance than the baselines, as evidenced by both quantitative (e.g., negative log likelihood and perplexity) and qualitative evaluation. The code for our model is available online.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-65d2defcb333cff37001949a1611a5892ff5075c884960ae2fc53b32a76f81b1

Passage ID: `qasper-passage-v1-65d2defcb333cff37001949a1611a5892ff5075c884960ae2fc53b32a76f81b1`; retrieval score: 6.256936822630532.

Word count: 72.

```text
We evaluate our model on two public datasets, namely, Penn Treebank (PTB) BIBREF9 and the end-to-end (E2E) text generation corpus BIBREF10, which have been used in a number of previous works for text generation BIBREF0, BIBREF5, BIBREF11, BIBREF12. PTB consists of more than 40,000 sentences from Wall Street Journal articles whereas the E2E dataset contains over 50,000 sentences of restaurant reviews. The statistics of these two datasets are summarised in Table TABREF11.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-99969c14292233ca9b6f089e81d9a70d371e7448d2c0934ddb7f2c8196ffc2f6

Passage ID: `qasper-passage-v1-99969c14292233ca9b6f089e81d9a70d371e7448d2c0934ddb7f2c8196ffc2f6`; retrieval score: 4.799514933315386.

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

#### Rank 4: qasper-passage-v1-08b742d77908579a5f2329074941c11b8e62ebe9b9177e83ef539b6238253e7c

Passage ID: `qasper-passage-v1-08b742d77908579a5f2329074941c11b8e62ebe9b9177e83ef539b6238253e7c`; retrieval score: 4.649739195162287.

Word count: 200.

```text
the decoder and effective use of encoding information, and developed a dilated CNN as decoder which can vary the amount of conditioning context. They also introduced a loss clipping strategy in order to make the model more robust. BIBREF5 addressed the problem by replacing the standard normal distribution for the prior with the von Mises-Fisher (vMF) distribution. With vMF, the KL loss only depends on the concentration parameter which is fixed during training and testing, and hence results in a constant KL loss. In a more recent work, BIBREF6 avoided latent variable collapse by including skip connections in the generative model, where the skip connections enforce strong links between the latent variables and the likelihood function.

Although the aforementioned works show effectiveness in addressing the latent variable collapse issue to some extent, they either require carefully engineering to balance the weight between the reconstruction loss and KL loss BIBREF0, BIBREF8, or resort to designing more sophisticated model structures BIBREF7, BIBREF5, BIBREF6.

In this paper, we present a simple architecture called holistic regularisation VAE (HR-VAE), which can effectively avoid latent variable collapse. In contrast to existing VAE-RNN models for text modelling which merely impose a standard normal distribution prior on the
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-0ca3d9ee262ca22030557b722f9ed199169d1bc53a48d3721baaf8b92164aa0b

Passage ID: `qasper-passage-v1-0ca3d9ee262ca22030557b722f9ed199169d1bc53a48d3721baaf8b92164aa0b`; retrieval score: 4.421017797467073.

Word count: 200.

```text
Variational Autoencoder (VAE) BIBREF1 is a powerful method for learning representations of high-dimensional data. However, recent attempts of applying VAEs to text modelling are still far less successful compared to its application to image and speech BIBREF2, BIBREF3, BIBREF4. When applying VAEs for text modelling, recurrent neural networks (RNNs) are commonly used as the architecture for both encoder and decoder BIBREF0, BIBREF5, BIBREF6. While such a VAE-RNN based architecture allows encoding and generating sentences (in the decoding phase) with variable-length effectively, it is also vulnerable to an issue known as latent variable collapse (or KL loss vanishing), where the posterior collapses to the prior and the model will ignore the latent codes in generative tasks.

Various efforts have been made to alleviate the latent variable collapse issue. BIBREF0 uses KL annealing, where a variable weight is added to the KL term in the cost function at training time. BIBREF7 discovered that there is a trade-off between the contextual capacity of the decoder and effective use of encoding information, and developed a dilated CNN as decoder which can vary the amount of conditioning context. They also introduced a loss clipping strategy in order to make the model more robust. BIBREF5 addressed
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 727.

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

#### Rank 1: qasper-passage-v1-1cd67417b2a55d353ab37568f089f248278365ddd0c6ac35fbcd8b1938cb6189

Passage ID: `qasper-passage-v1-1cd67417b2a55d353ab37568f089f248278365ddd0c6ac35fbcd8b1938cb6189`; retrieval score: 9.066840761061465.

Word count: 165.

```text
that for well-resourced language pairs, an update of WMT evaluation style will be needed to keep up with the progress in machine translation. We concur that these findings have demonstrated the need to critically re-evaluate the design of human MT evaluation.

Our paper investigates three aspects of human MT evaluation, with a special focus on assessing human–machine parity: the choice of raters, the use of linguistic context, and the creation of reference translations. We focus on the data shared by BIBREF3, and empirically test to what extent changes in the evaluation design affect the outcome of the human evaluation. We find that for all three aspects, human translations are judged more favourably, and significantly better than MT, when we make changes that we believe strengthen the evaluation design. Based on our empirical findings, we formulate a set of recommendations for human MT evaluation in general, and assessing human–machine parity in particular. All of our data are made publicly available for external validation and further analysis.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-af166dcb6f7bb3ed63cd475b7a29db84170402e4ea7c20cb1394e0b2078bd458

Passage ID: `qasper-passage-v1-af166dcb6f7bb3ed63cd475b7a29db84170402e4ea7c20cb1394e0b2078bd458`; retrieval score: 6.945438440172928.

Word count: 200.

```text
We compared professional human Chinese to English translations to the output of a strong MT system. In a human evaluation following best practices, BIBREF3 found no significant difference between the two, concluding that their NMT system had reached parity with professional human translation. Our blind qualitative analysis, however, showed that the machine translation output contained significantly more incorrect words, omissions, mistranslated names, and word order errors.

Our experiments show that recent findings of human–machine parity in language translation are owed to weaknesses in the design of human evaluation campaigns. We empirically tested alternatives to what is currently considered best practice in the field, and found that the choice of raters, the availability of linguistic context, and the creation of reference translations have a strong impact on perceived translation quality. As for the choice of raters, professional translators showed a significant preference for human translation, while non-expert raters did not. In terms of linguistic context, raters found human translation significantly more accurate than machine translation when evaluating full documents, but not when evaluating single sentences out of context. They also found human translation significantly more fluent than machine translation, both when evaluating full documents and single sentences. Moreover, we showed that
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-08939091c8304d5460e9be3483bf80eee961c12505613c9ce422e5a0778494b1

Passage ID: `qasper-passage-v1-08939091c8304d5460e9be3483bf80eee961c12505613c9ce422e5a0778494b1`; retrieval score: 6.46014234436058.

Word count: 200.

```text
Machine translation (MT) has made astounding progress in recent years thanks to improvements in neural modelling BIBREF0, BIBREF1, BIBREF2, and the resulting increase in translation quality is creating new challenges for MT evaluation. Human evaluation remains the gold standard, but there are many design decisions that potentially affect the validity of such a human evaluation.

This paper is a response to two recent human evaluation studies in which some neural machine translation systems reportedly performed at (or above) the level of human translators for news translation from Chinese to English BIBREF3 and English to Czech BIBREF4, BIBREF5.

Both evaluations were based on current best practices in the field: they used a source-based direct assessment with non-expert annotators, using data sets and the evaluation protocol of the Conference on Machine Translation (WMT). While the results are intriguing, especially because they are based on best practices in MT evaluation, BIBREF5 warn against taking their results as evidence for human–machine parity, and caution that for well-resourced language pairs, an update of WMT evaluation style will be needed to keep up with the progress in machine translation. We concur that these findings have demonstrated the need to critically re-evaluate the design of human MT
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-15b4a3706e60bbda3ed86158e3b6557affe8dc5206972bdf37e21312725caa81

Passage ID: `qasper-passage-v1-15b4a3706e60bbda3ed86158e3b6557affe8dc5206972bdf37e21312725caa81`; retrieval score: 6.345431162102873.

Word count: 72.

```text
Our experiments in Sections SECREF3–SECREF5 show that machine translation quality has not yet reached the level of professional human translation, and that human evaluation methods which are currently considered best practice fail to reveal errors in the output of strong NMT systems. In this section, we recommend a set of evaluation design changes that we believe are needed for assessing human–machine parity, and will strengthen the human evaluation of MT in general.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-1c112cb94aef2dbf7d21d717ef0d4f7eb755a013eef3520a9bfd43e8d8fe5f0f

Passage ID: `qasper-passage-v1-1c112cb94aef2dbf7d21d717ef0d4f7eb755a013eef3520a9bfd43e8d8fe5f0f`; retrieval score: 6.048141968496566.

Word count: 200.

```text
a stronger preference for human translation in terms of fluency (compare Tables TABREF30 and TABREF21). In a direct comparison of the two human translations (Table TABREF30), we also find that H$_A$ is considered significantly more adequate than H$_B$, while there is no significant difference in fluency.

To achieve a finer-grained understanding of what errors the evaluated translations exhibit, we perform a categorisation of 150 randomly sampled sentences based on the classification used by BIBREF3. We expand the classification with a Context category, which we use to mark errors that are only apparent in larger context (e. g., regarding poor register choice, or coreference errors), and which do not clearly fit into one of the other categories. BIBREF3 perform this classification only for the machine-translated outputs, and thus the natural question of whether the mistakes that humans and computers make are qualitatively different is left unanswered. Our analysis was performed by one of the co-authors who is a bi-lingual native Chinese/English speaker. Sentences were shown in the context of the document, to make it easier to determine whether the translations were correct based on the context. The analysis was performed on one machine translation (MT$_1$) and two human translation outputs (H$_A$,
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 837.

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

#### Rank 1: qasper-passage-v1-546bb7d116068c808ce17f53bcc202e33f0937a5b96be477ac80b5c0690e9032

Passage ID: `qasper-passage-v1-546bb7d116068c808ce17f53bcc202e33f0937a5b96be477ac80b5c0690e9032`; retrieval score: 8.402819725257132.

Word count: 104.

```text
We set up experiments in order to answer the following research questions:

RQ1: Can the comparative evaluator correlate better with human preference in sample-level than previous automated metrics when evaluating open domain NLG models?

RQ2: Can the comparative evaluator correlate better with human preference in model-level, so that our approach can measure the progress on open domain NLG better?

RQ3: As existing approaches fail to correlate well with human preference, whether and to what extent this problem affects the quality of the final NLG model when performing hyperparameter search and early-stopping?

RQ4: If the previous problem exists, can proposed comparative evaluator reduce this problem?
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-ecfcf5e8bc47cf6c31892490bc023fe154e1899adc276e4d098201145c8f50ed

Passage ID: `qasper-passage-v1-ecfcf5e8bc47cf6c31892490bc023fe154e1899adc276e4d098201145c8f50ed`; retrieval score: 2.5569222405550147.

Word count: 44.

```text
While previous work on NLG evaluation mostly focuses on the evaluation stage and does not explore the influence of imperfect metrics during model training, our experiments demonstrate the existence of this problem and that the proposed method can, to some extent, alleviate this problem.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-21ecac6c5ab8b541a537f32f9103d6ecb064e5b1615aca6c46015228a53cb9a9

Passage ID: `qasper-passage-v1-21ecac6c5ab8b541a537f32f9103d6ecb064e5b1615aca6c46015228a53cb9a9`; retrieval score: 2.237108376792628.

Word count: 61.

```text
accurate than several baseline approaches.

We conduct experiments on both story generation task and open domain dialogue response generation task. Experimental results show that our approach correlates better with human evaluation on both datasets. Moreover, we show that using automated metrics such as BLEU to perform hyperparameter tuning and early-stopping results in sub-optimal model and our approach helps alleviate this problem.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-085a01a5e6eee2dd8f528caf6f6a27b62278cff3b8aebdc1b08dc1f3f7506f77

Passage ID: `qasper-passage-v1-085a01a5e6eee2dd8f528caf6f6a27b62278cff3b8aebdc1b08dc1f3f7506f77`; retrieval score: 2.037155119370468.

Word count: 200.

```text
Evaluation of NLG models has been a long-standing open problem. While human evaluation may be ideal, it is generally expensive to conduct and does not scale well. Various automated evaluation approaches are proposed to facilitate the development and evaluation of NLG models. We summarize these evaluation approaches below.

Text Overlap Metrics, including BLEU BIBREF5, METEOR BIBREF6 and ROUGE BIBREF7, are the most popular metrics employed in the evaluation of NLG models. They evaluate generated text by comparing the similarity between the generated text and human written references. While this works well in tasks where the diversity of acceptable output is limited, such as machine translation and text summarization, text overlap metrics are shown to have weak or no correlation with human judgments in open domain natural language generation tasks BIBREF8. There are two major drawbacks in these metrics. First, text overlap metrics can not distinguish minor variations in a generated text which may make the sentence not equally grammatically correct or semantically meaningful. Second, there may exist multiple equally good outputs for the given input and comparing against one gold reference can be erroneous.

Perplexity is commonly used to evaluate the quality of a language model. It measures how well
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `2002.05058:1:0` | full | 0:323 |
| `2002.05058:1:1` | full | 0:897 |
| `2002.05058:1:2` | partial | 0:93 |

#### Rank 5: qasper-passage-v1-6927fa72e9a2798d2bd7d813152854712016eff926a9aad2909c9fea0c02a6c7

Passage ID: `qasper-passage-v1-6927fa72e9a2798d2bd7d813152854712016eff926a9aad2909c9fea0c02a6c7`; retrieval score: 1.8899693243811977.

Word count: 174.

```text
As our objective is to evaluate the evaluators rather than comparing state-of-the-art models, we choose three representative sequence-to-sequence architectures: LSTM BIBREF27 seq2seq, Convolutional seq2seq BIBREF28, and transformer BIBREF1 model. We compare models with different architectures, hyperparameter choices, and early-stopping criteria with different automated metrics, as well as human evaluation.

Regarding the evaluation metric (and criteria for choosing hyperparameter choice and early-stopping), we compare the proposed approach with the discriminative evaluator, BLEU score (average of 2-, 3-, 4-grams), perplexity, and ADEM. When evaluating generated stories, we cut off the story at the nearest sentence for stories longer than 250 words.

The proposed comparative evaluator is employed for choosing hyperparameter by performing skill rating among all models trained with different hyperparameter choices. For early-stopping, as incrementally performing skill rating is computationally expensive, we propose to perform n (e.g. 1000) pairwise comparison between the samples generated by the latest checkpoint and the previous k (e.g. 2) checkpoints and stop training when the wining rate of latest checkpoint keeps being smaller than its losing rate for 5 iterations.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 583.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "d449825aa0a1d27531a41dd5ec098834f1fde4a8": {
    "unresolved_evidence": [],
    "paragraphs": {
      "2002.05058:1:2": [
        [
          93,
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

#### Rank 1: qasper-passage-v1-7d5396befedfeba2fe7c467cef1e2ab8f5b163618edfe709984b198686bfe7a1

Passage ID: `qasper-passage-v1-7d5396befedfeba2fe7c467cef1e2ab8f5b163618edfe709984b198686bfe7a1`; retrieval score: 8.712989340886283.

Word count: 138.

```text
This paper presented the UDS-DFKI system submitted to the Similar Language Translation shared task at WMT 2019. We presented the results obtained by our system in translating from Czech to Polish. Our system achieved competitive performance ranking second among ten teams in the competition in terms of BLEU score. The fact that out-of-domain data was provided by the organizers resulted in a challenging but interesting scenario for all participants.

In future work, we would like to investigate how effective is the proposed hypothesis (i.e., word-BPE level information) in similar language translation. Furthermore, we would like to explore the similarity between these two languages (and the other two language pairs in the competition) in more detail by training models that can best capture morphological differences between them. During such competitions, this is not always possible due to time constraints.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-0df3c30399ff56b6d9b47e5e9cebb9c07cb7e5a393086c2bb8bdb8d6e8625024

Passage ID: `qasper-passage-v1-0df3c30399ff56b6d9b47e5e9cebb9c07cb7e5a393086c2bb8bdb8d6e8625024`; retrieval score: 8.692609320326865.

Word count: 97.

```text
Spanish - Portuguese (Romance languages), Czech - Polish (Slavic languages), and Hindi - Nepali (Indo-Aryan languages). Participant could submit system outputs to any of the three language pairs in any direction. The shared task attracted a good number of participants and the performance of all entries was evaluated using popular MT automatic evaluation metrics, namely BLEU BIBREF3 and TER BIBREF4.

In this paper we describe the UDS-DFKI system to the WMT 2019 Similar Language Translation task. The system achieved competitive performance and ranked second among ten entries in Czech to Polish translation in terms of BLEU score.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-de649e3a23a0ea2d5147b2475afb54ea4a02e590c5b620b8af5330ff78a8e549

Passage ID: `qasper-passage-v1-de649e3a23a0ea2d5147b2475afb54ea4a02e590c5b620b8af5330ff78a8e549`; retrieval score: 5.6094211989127505.

Word count: 186.

```text
We present the results obtained by our system in Table TABREF8.

Our fine-tuned system on development set provides significant performance improvement over the generic model. We found +12.9 absolute BLEU points improvement over the generic model. Similar improvement is also observed in terms of TER (-16.9 absolute). It is to be noted that our generic model is trained solely on the clean version of training data.

Before submission, we performed punctuation normalization, unicode normalization, and detokenization for the run.

In Table TABREF9 we present the ranking of the competition provided by the shared task organizers. Ten entries were submitted by five teams and are ordered by BLEU score. TER is reported for all submissions which achieved BLEU score greater than 5.0. The type column specifies the type of system, whether it is a Primary (P) or Constrastive (C) entry.

Our system was ranked second in the competition only 0.3 BLEU points behind the winning team UPC-TALP. The relative low BLEU and high TER scores obtained by all teams are due to out-of-domain data provided in the competition which made the task equally challenging to all participants.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-905011d0167b1f301e4d2d4833ccb39133bea96f4b4d9f84025494d3099baa34

Passage ID: `qasper-passage-v1-905011d0167b1f301e4d2d4833ccb39133bea96f4b4d9f84025494d3099baa34`; retrieval score: 4.462070261044194.

Word count: 200.

```text
The shared tasks organized annually at WMT provide important benchmarks used in the MT community. Most of these shared tasks include English data, which contributes to make English the most resource-rich language in MT and NLP. In the most popular WMT shared task for example, the News task, MT systems have been trained to translate texts from and to English BIBREF0, BIBREF1.

This year, we have observed a shift on the dominant role that English on the WMT shared tasks. The News task featured for the first time two language pairs which did not include English: German-Czech and French-German. In addition to that, the Similar Language Translation was organized for the first time at WMT 2019 with the purpose of evaluating the performance of MT systems on three pairs of similar languages from three different language families: Ibero-Romance, Indo-Aryan, and Slavic.

The Similar Language Translation BIBREF2 task provided participants with training, development, and testing data from the following language pairs: Spanish - Portuguese (Romance languages), Czech - Polish (Slavic languages), and Hindi - Nepali (Indo-Aryan languages). Participant could submit system outputs to any of the three language pairs in any direction. The shared task attracted a good number of participants
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-9b2b32884aa8c01267241a4f3a4e81c4bb0b8da9ce70d795a845b0c6bdcd7030

Passage ID: `qasper-passage-v1-9b2b32884aa8c01267241a4f3a4e81c4bb0b8da9ce70d795a845b0c6bdcd7030`; retrieval score: 4.189480375459732.

Word count: 200.

```text
For transferenceALL, we initially train on the complete out-of-domain dataset (General). The General data is sorted based on their in-domain similarities as described in Equation DISPLAY_FORM2.

transferenceALLmodels are then fine-tuned towards the 500K (in-domain-like) data. Finally, we perform checkpoint averaging using the 8 best checkpoints. We report the results on the provided development set, which we use as a test set before the submission. Additionally we also report the official test set result.

To handle out-of-vocabulary words and to reduce the vocabulary size, instead of considering words, we consider subword units BIBREF13 by using byte-pair encoding (BPE). In the preprocessing step, instead of learning an explicit mapping between BPEs in the Czech (CS) and Polish (PL), we define BPE tokens by jointly processing all parallel data. Thus, CS and PL derive a single BPE vocabulary. Since CS and PL belong to the similar language, they naturally share a good fraction of BPE tokens, which reduces the vocabulary size.

We pass word level information on the first encoder and the BPE information to the second one. On the decoder side of the transference model we pass only BPE text.

We evaluate our approach with development data which is used as test
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 821.

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

#### Rank 1: qasper-passage-v1-259c3d80d46f8f72cc121070bdaaf9cc1a16048904ac0f40060bfc88b8101966

Passage ID: `qasper-passage-v1-259c3d80d46f8f72cc121070bdaaf9cc1a16048904ac0f40060bfc88b8101966`; retrieval score: 5.497815364181023.

Word count: 200.

```text
importance of the sequential flow of tweets.

Top-$k$ replies, likes, or re-tweets: Some approaches in rumors detection use the number of replies, likes, and re-tweets to detect rumors BIBREF21. Thus, we extract top $k$ replied, liked or re-tweeted tweets from each account to assess the accounts factuality. We tested different $k$ values between 10 tweets to the max number of tweets from each account. Figure FIGREF24 shows the macro-F1 values for different $k$ values. It seems that $k=500$ for the top replied tweets achieves the highest result. Therefore, we consider this as a baseline.

Experimental Setup. We apply a 5 cross-validation on the account's level. For the FacTweet model, we experiment with 25% of the accounts for validation and parameters selection. We use hyperopt library to select the hyper-parameters on the following values: LSTM layer size (16, 32, 64), dropout ($0.0-0.9$), activation function ($relu$, $selu$, $tanh$), optimizer ($sgd$, $adam$, $rmsprop$) with varying the value of the learning rate (1e-1,..,-5), and batch size (4, 8, 16). The validation split is extracted on the class level using stratified sampling: we took a random 25% of the accounts from each class since the dataset is unbalanced. Discarding the classes' size in the splitting
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1910.06592:2:11` | partial | 0:688 |

#### Rank 2: qasper-passage-v1-f0a99d0c6ad16ae4083208d9b39b19697b012bbd76c66a4a5a497e978bebeb1c

Passage ID: `qasper-passage-v1-f0a99d0c6ad16ae4083208d9b39b19697b012bbd76c66a4a5a497e978bebeb1c`; retrieval score: 3.04862536958534.

Word count: 200.

```text
batch size (4, 8, 16). The validation split is extracted on the class level using stratified sampling: we took a random 25% of the accounts from each class since the dataset is unbalanced. Discarding the classes' size in the splitting process may affect the minority classes (e.g. hoax). For the baselines' classifier, we tested many classifiers and the LR showed the best overall performance.

Results. Table TABREF25 presents the results. We present the results using a chunk size of 20, which was found to be the best size on the held-out data. Figure FIGREF24 shows the results of different chunks sizes. FacTweet performs better than the proposed baselines and obtains the highest macro-F1 value of $0.565$. Our results indicate the importance of taking into account the sequence of the tweets in the accounts' timelines. The sequence of these tweets is better captured by our proposed model sequence-agnostic or non-neural classifiers. Moreover, the results demonstrate that the features at tweet-level do not perform well to detect the Twitter accounts factuality, since they obtain a result near to the majority class ($0.18$). Another finding from our experiments shows that the performance of the Tweet2vec is weak. This demonstrates that tweets' hashtags are
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1910.06592:2:11` | partial | 454:847 |

#### Rank 3: qasper-passage-v1-1d86ed766ccc37f7e1a1ebb861441a2ba59d804a40a19bbf4d4bdd0e48df162a

Passage ID: `qasper-passage-v1-1d86ed766ccc37f7e1a1ebb861441a2ba59d804a40a19bbf4d4bdd0e48df162a`; retrieval score: 2.9447115531069197.

Word count: 200.

```text
set of baselines:

[leftmargin=4mm]

LR + Bag-of-words: We aggregate the tweets of a feed and we use a bag-of-words representation with a logistic regression (LR) classifier.

Tweet2vec: We use the Bidirectional Gated recurrent neural network model proposed in BIBREF20. We keep the default parameters that were provided with the implementation. To represent the tweets, we use the decoded embedding produced by the model. With this baseline we aim at assessing if the tweets' hashtags may help detecting the non-factual accounts.

LR + All Features (tweet-level): We extract all our features from each tweet and feed them into a LR classifier. Here, we do not aggregate over tweets and thus view each tweet independently.

LR + All Features (chunk-level): We concatenate the features' vectors of the tweets in a chunk and feed them into a LR classifier.

FacTweet (tweet-level): Similar to the FacTweet approach, but at tweet-level; the sequential flow of the tweets is not utilized. We aim at investigating the importance of the sequential flow of tweets.

Top-$k$ replies, likes, or re-tweets: Some approaches in rumors detection use the number of replies, likes, and re-tweets to detect rumors BIBREF21. Thus, we extract top $k$ replied, liked or re-tweeted tweets from
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-3224c9b3dc04575feadb2f685c1a870fd069351274886af79ae982fc1cc415b0

Passage ID: `qasper-passage-v1-3224c9b3dc04575feadb2f685c1a870fd069351274886af79ae982fc1cc415b0`; retrieval score: 2.7440046420127957.

Word count: 200.

```text
using word occurrences of 15 emotion types from two available emotional lexicons. We use the NRC lexicon BIBREF10, which contains $\sim $14K words labeled using the eight Plutchik's emotions BIBREF11. The other lexicon is SentiSense BIBREF12 which is a concept-based affective lexicon that attaches emotional meanings to concepts from the WordNet lexical database. It has $\sim $5.5 words labeled with emotions from a set of 14 emotional categories We use the categories that do not exist in the NRC lexicon.

Sentiment: We extract the sentiment of the tweets by employing EffectWordNet BIBREF13, SenticNet BIBREF14, NRC BIBREF10, and subj_lexicon BIBREF15, where each has the two sentiment classes, positive and negative.

Morality: Features based on morality foundation theory BIBREF16 where words are labeled in one of the following 10 categories (care, harm, fairness, cheating, loyalty, betrayal, authority, subversion, sanctity, and degradation).

Style: We use canonical stylistic features, such as the count of question marks, exclamation marks, consecutive characters and letters, links, hashtags, users' mentions. In addition, we extract the uppercase ratio and the tweet length.

Words embeddings: We extract words embeddings of the words of the tweet using $Glove\-840B-300d$ BIBREF17 pretrained model. The tweet final representation is obtained by averaging its words
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-8cbc3dcdf3e84a729060372b72b4185ac783c3d0d66eb0ee7ea3819f046f6748

Passage ID: `qasper-passage-v1-8cbc3dcdf3e84a729060372b72b4185ac783c3d0d66eb0ee7ea3819f046f6748`; retrieval score: 2.608530725120015.

Word count: 200.

```text
high volume of available tweets Consequently, a first step in this direction, e.g., as a pre-filtering step, can be viewed as the task of detecting fake news at the account level.

The main obstacle for detecting suspicious Twitter accounts is due to the behavior of mixing some real news with the misleading ones. Consequently, we investigate ways to detect suspicious accounts by considering their tweets in groups (chunks). Our hypothesis is that suspicious accounts have a unique pattern in posting tweet sequences. Since their intention is to mislead, the way they transition from one set of tweets to the next has a hidden signature, biased by their intentions. Therefore, reading these tweets in chunks has the potential to improve the detection of the fake news accounts.

In this work, we investigate the problem of discriminating between factual and non-factual accounts in Twitter. To this end, we collect a large dataset of tweets using a list of propaganda, hoax and clickbait accounts and compare different versions of sequential chunk-based approaches using a variety of feature sets against several baselines. Several approaches have been proposed for news verification, whether in social media (rumors detection) BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, or in news
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 1000.

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

#### Rank 1: qasper-passage-v1-9f6493cff7a95d2d90278fe30fc0948374a2b143480b8912e3cc909855450b4f

Passage ID: `qasper-passage-v1-9f6493cff7a95d2d90278fe30fc0948374a2b143480b8912e3cc909855450b4f`; retrieval score: 6.152149187477263.

Word count: 200.

```text
$\textsc {Zero-stc}$ was first explored by the paradigm “Dataless Classification” BIBREF0. Dataless classification first maps the text and labels into a common space by Explicit Semantic Analysis (ESA) BIBREF4, then picks the label with the highest matching score. Dataless classification emphasizes that the representation of labels takes the equally crucial role as the representation learning of text. Then this idea was further developed in BIBREF5, BIBREF6, BIBREF7, BIBREF8, BIBREF9.

With the prevalence of word embeddings, more and more work adopts pretrained word embeddings to represent the meaning of words, so as to provide the models with the knowledge of labels BIBREF10, BIBREF2, BIBREF11, BIBREF12. DBLPYogatamaDLB17 build generative LSTM to generate text given the embedded labels. DBLPRiosK18 use label embedding to attend the text representation in the developing of a multi-label classifier. But they report R@K, so it is unclear whether the system can really predict unseen labels. DBLPXiaZYCY18 study the zero-shot intent detection problem. The learned representations of intents are still the sum of word embeddings. But during testing, the intent space includes only new intents; seen intents are not covered. All of these studies can only meet the definition in Definition-Restrictive, so they do not really generalize to open
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-81a32d63b8156c79f3e29fda6fcfe70e02c9beda0121c8405a3e46dae626b9f4

Passage ID: `qasper-passage-v1-81a32d63b8156c79f3e29fda6fcfe70e02c9beda0121c8405a3e46dae626b9f4`; retrieval score: 4.567514730703426.

Word count: 196.

```text
categorization task; emotion and situation categorizations, however, are relatively further.

Our entailment models, pretrained on MNLI/FEVER/RTE respectively, perform more robust on the three $\textsc {0shot-tc}$ aspects (except for the RTE on emotion). Recall that they are not trained on any text classification data, and never know the domain and the aspects in the test. This clearly shows the great promise of developing textual entailment models for $\textsc {0shot-tc}$. Our ensemble approach further boosts the performances on all three tasks.

An interesting phenomenon, comparing the label-partially-unseen results in Table TABREF30 and the label-fully-unseen results in Table TABREF32, is that the pretrained entailment models work in this order for label-fully-unseen case: RTE $>$ FEVER $>$MNLI; on the contrary, if we fine-tune them on the label-partially-unseen case, the MNLI-based model performs best. This could be due to a possibility that, on one hand, the constructed situation entailment dataset is closer to the RTE dataset than to the MNLI dataset, so an RTE-based model can generalize well to situation data, but, on the other hand, it could also be more likely to over-fit the training set of “situation” during fine-tuning. A deeper exploration of this is left as future work.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-14e11b9d71fe990eb5c7f7d855b3fe9b3bb7e86809a6ff3f99a0bba885e21278

Passage ID: `qasper-passage-v1-14e11b9d71fe990eb5c7f7d855b3fe9b3bb7e86809a6ff3f99a0bba885e21278`; retrieval score: 4.281410317135272.

Word count: 70.

```text
models – this is why it predicts very well for seen classes while performing much worse for unseen classes.

Our entailment models, especially the one pretrained on MNLI, generally get competitive performance with the “Binary-BERT” for seen (slightly worse on “topic” and “emotion” while clearly better on “situation”) and improve the performance regarding unseen by large margins. At this stage, fine-tuning on an MNLI-based pretrained entailment model seems more powerful.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-70f772b6f4790c3281ef79c340673786496d702a7ac4ee28d0ccc2b34342f6f1

Passage ID: `qasper-passage-v1-70f772b6f4790c3281ef79c340673786496d702a7ac4ee28d0ccc2b34342f6f1`; retrieval score: 4.024501683410941.

Word count: 200.

```text
In Table TABREF24, we listed examples for converting class names into hypotheses. In this work, we only tried to make use of the class names and their definitions in WordNet. Table TABREF33 lists the fine-grained performance of three ways of generating hypotheses: “word”, “definition”, and “combination” (i.e., word&definition).

This table indicates that: i) Definition alone usually does not work well in any of the three tasks, no matter which pretrained entailment model is used; ii) Whether “word” alone or “word&definition” works better depends on the specific task and the pretrained entailment model. For example, the pretrained MNLI model prefers “word&definition” in both “emotion” and “situation” detection tasks. However, the other two entailment models (RTE and FEVER) mostly prefer “word”. iii) Since it is unrealistic to adopt only one entailment model, such as from {RTE, FEVER, MNLI}, for any open $\textsc {0shot-tc}$ problem, an ensemble system should be preferred. However, the concrete implementation of the ensemble system also influences the strengths of different hypothesis generation approaches. In this work, our ensemble method reaches the top performance when combining the “word” and “definition”. More ensemble systems and hypothesis generation paradigms need to be studied in the future.

To better understand the impact
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-eb450a9d7c992b989b7e83f3db1e03e707792d8cdc715b8a687d197522a6f521

Passage ID: `qasper-passage-v1-eb450a9d7c992b989b7e83f3db1e03e707792d8cdc715b8a687d197522a6f521`; retrieval score: 3.747960609357157.

Word count: 200.

```text
still the sum of word embeddings. But during testing, the intent space includes only new intents; seen intents are not covered. All of these studies can only meet the definition in Definition-Restrictive, so they do not really generalize to open aspects of $\textsc {0shot-tc}$.

JiangqngGuo enrich the embedding representations by incorporating class descriptions, class hierarchy, and the word-to-label paths in ConceptNet. DBLPMitchellSL18 assume that some natural language explanations about new labels are available. Then those explanations are parsed into formal constraints which are further combined with unlabeled data to yield new label oriented classifiers through posterior regularization. However, those explanatory statements about new labels are collected from crowd-sourcing. This limits its application in real world $\textsc {0shot-tc}$ scenarios.

There are a few works that study a specific zero-shot problem by indirect supervision from other problems. DBLPLevySCZ17 and obamuyide2018zero study zero-shot relation extraction by converting it into a machine comprehension and textual entailment problem respectively. Then, a supervised system pretrained on an existing machine comprehension dataset or textual entailment dataset is used to do inference. Our work studies the $\textsc {0shot-tc}$ by formulating a broader vision: datasets of multiple apsects and evaluations.

Other zero-shot problems studied in NLP involve entity typing
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 866.

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

#### Rank 1: qasper-passage-v1-837f66d55fbc06dd51c0eedc5887a19ec5f9c215a0958d202bac22840ab23cd4

Passage ID: `qasper-passage-v1-837f66d55fbc06dd51c0eedc5887a19ec5f9c215a0958d202bac22840ab23cd4`; retrieval score: 10.536939244028954.

Word count: 54.

```text
improve even very deep models.

As shown in Table TABREF21, the proposed methods also provide large performance improvements on the curated video set, up to 13% with CTC, and up to 9% with the hybrid model. We also observe moderate gains of between 3.2 and 8% relative on the clean and noisy video sets.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-20f7b0d9dec0535ff4bc9fad6cd4468b87a740af4f01e6dbfe7ef235aa131a39

Passage ID: `qasper-passage-v1-20f7b0d9dec0535ff4bc9fad6cd4468b87a740af4f01e6dbfe7ef235aa131a39`; retrieval score: 9.006577574799767.

Word count: 200.

```text
Table TABREF19 presents CTC based results for the Librispeech dataset, without data augmentation. Our baseline is a 24 layer Transformer network trained with CTC. For the proposed method, we varied the number and placement of iterated loss and the feature re-presentation. The next three results show the effect of using CTC multiple times. We see 12 and 8% relative improvements for test-clean and test-other. Adding feature re-presentation gives a further boost, with net 20 and 18% relative improvements over the baseline.

Table TABREF20 shows results for Librispeech with SpecAugment. We test both CTC and CE/hybrid systems. There are consistent gains first from iterated loss, and then from multiple feature presentation. We also run additional CTC experiments with 36 layers Transformer (total parameters $\pm $120 millions). The baseline with 36 layers has the same performance with 24 layers, but by adding the proposed methods, the 36 layer performance improved to give the best results. This shows that our proposed methods can improve even very deep models.

As shown in Table TABREF21, the proposed methods also provide large performance improvements on the curated video set, up to 13% with CTC, and up to 9% with the hybrid model. We also observe moderate
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-8427bf7714f1d881056b6141a2a96ece9f4a86daf6778299b98a4203cf3d5946

Passage ID: `qasper-passage-v1-8427bf7714f1d881056b6141a2a96ece9f4a86daf6778299b98a4203cf3d5946`; retrieval score: 7.994299975287412.

Word count: 200.

```text
In recent years, Transformer models have become an active research topic in speech processing. The key features of Transformer networks is self-attention, which produces comparable or better performance to LSTMs when used for encoder-decoder based ASR BIBREF23, as well as when trained with CTC BIBREF9. Speech-Transformers BIBREF24 also produce comparable performance to the LSTM-based attention model, but with higher training speed in a single GPU. Abdelrahman et al.BIBREF8 integrates a convolution layer to capture audio context and reduces WER in Librispeech.

The use of an objective function in intermediate layers has been found useful in several previous works such as image classification BIBREF25 and language modeling BIBREF26. In BIBREF27, the authors did pre-training with an RNN-T based model by using a hierarchical CTC criterion with different target units. In this paper, we don't need additional types of target unit, instead we just use same tokenization and targets for both intermediate and final losses.

The application of the objective function to intermediate layers is also similar in spirit to the use of KL-divergence in BIBREF28, which estimates output posteriors at an intermediate layer and regularizes them towards the distributions at the final layer. In contrast to this approach, the direct application
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-202e263d4c8117bc6d6005f65b5f0ebbe05b00a9bbd9321375df5c0c29d49b55

Passage ID: `qasper-passage-v1-202e263d4c8117bc6d6005f65b5f0ebbe05b00a9bbd9321375df5c0c29d49b55`; retrieval score: 7.90806441106053.

Word count: 107.

```text
In this section, we present our proposal for allowing the network to (re)-consider the input features in the light of intermediate processing. We do this by again deploying a self-attention mechanism to combine the information present in the original features with the information available in the activations of an intermediate layer. As described earlier, we calculate the output posteriors and auxiliary loss at the intermediate layer as well. The overall architecture is illustrated in Figure FIGREF6. Here, we have used a 24 layer network, with feature re-presentation after the 12th layer.

In the following subsections, we provide detail on the feature re-presentation mechanism, and iterated loss calculation.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-50b3994bc40dc663f487f94e62005f415ccab703446ea0db36f1bb8cdbb68458

Passage ID: `qasper-passage-v1-50b3994bc40dc663f487f94e62005f415ccab703446ea0db36f1bb8cdbb68458`; retrieval score: 7.205702110515386.

Word count: 97.

```text
In this paper, we have proposed a method for re-processing the input features in light of the information available at an intermediate network layer. We do this in the context of deep transformer networks, via a self-attention mechanism on both features and hidden states representation. To encourage meaningful partial results, we calculate the objective function at intermediate layers of the network as well as the output layer. This improves performance in and of itself, and when combined with feature re-presentation we observe consistent relative improvements of 10 - 20% for Librispeech and 3.2 - 13% for videos.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 658.

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

#### Rank 1: qasper-passage-v1-e0a61fd8df903066bc552a8c0e7a9b6f846c738af0384504142a8a5c0f516a60

Passage ID: `qasper-passage-v1-e0a61fd8df903066bc552a8c0e7a9b6f846c738af0384504142a8a5c0f516a60`; retrieval score: 11.08514029839559.

Word count: 200.

```text
Ideally the DM's policy would be trained by interacting with real users. Although there are models that support on-line learning BIBREF15 , for the majority of RL algorithms, which require a lot of interactions, this is impractical. Furthermore, a set of users needs to be recruited every time a policy is trained. This makes common practices such as hyper-parameter optimization prohibitively expensive. Thus, it is natural to try to learn from a dataset which needs to be recorded only once, but can be used over and over again.

A problem with learning directly from recorded dialogue corpora is that the state space that was visited during the collection of the data is limited; the size of the recorded corpus usually falls short of the requirements for training a statistical DM. However, even if the size of the corpus is large enough the optimal dialogue strategy is likely not to be contained within it.

A solution is to transform the static corpus into a dynamic tool: a user simulator. The user simulator (US) is trained on a dialogue corpus to learn what responses a real user would provide in a given dialogue context. The US is trained using supervised learning since
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-a45ca4ea7d93e805e98141698358a63dccbd81856157ae159b45b9476bd68089

Passage ID: `qasper-passage-v1-a45ca4ea7d93e805e98141698358a63dccbd81856157ae159b45b9476bd68089`; retrieval score: 10.86994562310367.

Word count: 200.

```text
corpus into a dynamic tool: a user simulator. The user simulator (US) is trained on a dialogue corpus to learn what responses a real user would provide in a given dialogue context. The US is trained using supervised learning since the aim is for it to learn typical user behaviour. For the DM, however, we want optimal behaviour which is why supervised learning cannot be used. By interacting with the SDS, the trained US can be used to train the DM's policy. The DM's policy is optimised using the feedback given by either the user simulator or a separate evaluator. Any number of dialogues can be generated using the US and dialogue strategies that are not in the recorded corpus can be explored.

Most user-simulators work on the level of user semantics. These usually consist of a user dialogue act (e.g. inform, or request) and a corresponding slot-value pair. The first statistical user simulator BIBREF16 used a simple bi-gram model INLINEFORM0 to predict the next user act INLINEFORM1 given the last system act INLINEFORM2 . It has the advantage of being purely probabilistic and domain-independent. However, it does not take the full dialogue history into account and is not conditioned
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-ea45c40a0f64fd8459c1d6ca97ac51d29b2069c86e0ca979cf5360b62f963190

Passage ID: `qasper-passage-v1-ea45c40a0f64fd8459c1d6ca97ac51d29b2069c86e0ca979cf5360b62f963190`; retrieval score: 4.593360777154306.

Word count: 162.

```text
A Task-Oriented SDS is typically designed according to a structured ontology, which defines what the system can talk about. In a system recommending restaurants the ontology defines those attributes of a restaurant that the user can choose, called informable slots (e.g. different food types, areas and price ranges), the attributes that the user can request, called requestable slots (e.g. phone number or address) and the restaurants that it has data about. An attribute is referred to as a slot and has a corresponding value. Together these are referred to as a slot-value pair (e.g. area=north).

Using RL the DM is trained to act such that is maximises the cumulative future reward. The process by which the DM chooses its next action is called its policy. A typical approach to defining the reward function for a task-oriented SDS is to apply a small per-turn penalty to encourage short dialogues and to give a large positive reward at the end of each successful interaction.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-d776c6851488be6f0736b4b3b24b678db2f759d4e5dccbb86fd166369b25d4fe

Passage ID: `qasper-passage-v1-d776c6851488be6f0736b4b3b24b678db2f759d4e5dccbb86fd166369b25d4fe`; retrieval score: 4.418083787190343.

Word count: 200.

```text
Spoken Dialogue Systems (SDS) allow human-computer interaction using natural speech. Task-oriented dialogue systems, the focus of this work, help users achieve goals such as finding restaurants or booking flights BIBREF0 .

Teaching a system how to respond appropriately in a task-oriented setting is non-trivial. In state-of-the-art systems this dialogue management task is often formulated as a reinforcement learning (RL) problem BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 . In this framework, the system learns by a trial and error process governed by a reward function. User Simulators can be used to train the policy of a dialogue manager (DM) without real user interactions. Furthermore, they allow an unlimited number of dialogues to be created with each dialogue being faster than a dialogue with a human.

In this paper the Neural User Simulator (NUS) is introduced which outputs natural language and whose behaviour is learned from a corpus. The main component, inspired by BIBREF4 , consists of a feature extractor and a neural network based sequence-to-sequence model BIBREF5 . The sequence-to-sequence model consists of a recurrent neural network (RNN) encoder that encodes the dialogue history and a decoder RNN which outputs natural language. Furthermore, the NUS generates its own goal and
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1805.06966:0:2` | partial | 0:490 |

#### Rank 5: qasper-passage-v1-8b0999802a4aebff4eae354dec41a371ecf73e5e08e01f66f821fa8aeb220370

Passage ID: `qasper-passage-v1-8b0999802a4aebff4eae354dec41a371ecf73e5e08e01f66f821fa8aeb220370`; retrieval score: 4.205164850099022.

Word count: 129.

```text
on the ABUS. This could indicate that the policy “overfits” to a particular user simulator. Overfitting usually manifests itself in worse results as the model is trained for longer. Five policies trained on each US for only 1000 dialogues were also evaluated, the results of which can be seen in Table TABREF19 . After training for 1000 dialogues, the average SR of the policies trained on the NUS when tested on the ABUS was 97.3% in comparison to 94.0% after 4000 dialogues. This behaviour was observed for all five seeds, which indicates that the policy indeed overfits to the NUS. For the policies trained with the ABUS this was not observed. This could indicate that the policy can learn to exploit some of the shortcomings of the trained NUS.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 891.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "c1ed3e2a6e21d189790e8b23f0edc5422b51ec52": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1805.06966:0:2": [
        [
          490,
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

#### Rank 1: qasper-passage-v1-9b0c08f4620d9f68e1d05f86d1521039159ff504153924954f135a89d413a3f6

Passage ID: `qasper-passage-v1-9b0c08f4620d9f68e1d05f86d1521039159ff504153924954f135a89d413a3f6`; retrieval score: 7.863545314067128.

Word count: 119.

```text
The fixed training condition is used to build our speaker recognition system. Only conversational telephone speech data from datasets released through the linguistic data consortium (LDC) have been used, including NIST SRE 2004-2010 and the Switchboard corpora (Switchboard Cellular Parts I and II, Switchboard2 Phase I,II and III) for different steps of system training. A more detailed description of the data used in the system training is presented in Table TABREF1 . We have also included the unlabelled set of 2472 telephone calls from both minor (Cebuano and Mandarin) and major (Tagalog and Cantonese) languages provided by NIST in the system training. We will indicate when and how we used this set in the training in the following sections.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-46a5127dc97b6b70a04361a96e696292b955548bfd8ed3e7c9265ac35bccac67

Passage ID: `qasper-passage-v1-46a5127dc97b6b70a04361a96e696292b955548bfd8ed3e7c9265ac35bccac67`; retrieval score: 5.9822305501258235.

Word count: 70.

```text
duration of the segments. For enrolment, we have reported the time required to extract a model from a segment with a duration of 140 seconds and speech duration of 60 seconds. The time and memory required for front-end processing are negligible compared to the i-vector extraction stage, since they only include matrix operations. The time required for our SAD is also reported which increases linearly with the duration of segment.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-11be6c535379010ffc3a771e3d6f826a0f4976db64b4b0df43e18f7c367cf8cd

Passage ID: `qasper-passage-v1-11be6c535379010ffc3a771e3d6f826a0f4976db64b4b0df43e18f7c367cf8cd`; retrieval score: 5.684584622887012.

Word count: 200.

```text
This section reports on the CPU execution time (single threaded), and the amount of memory used to process a single trial, which includes the time for creating models from the enrolment data and the time needed for processing the test segments. The analysis was performed on an Intel(R) Xeon(R) CPU E5-2670 2.60GHz. The results are shown in Table TABREF27 . We used the time command in Unix to report these results. The user time is the actual CPU time used in executing the process (single thread). The real time is the wall clock time (the elapsed time including time slices used by other processes and the time the process spends blocked). The system time is also the amount of CPU time spent in the kernel within the process. We have also reported the memory allocated for each stage of execution. The most computationally intensive stage is the extraction of i-vectors (both MFCC- and PLP-based i-vectors), which also depends on the duration of the segments. For enrolment, we have reported the time required to extract a model from a segment with a duration of 140 seconds and speech duration of 60 seconds. The time and memory required for front-end processing are
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-78aa0c147299100029a77f5732e4c645fa58e5523af0357d1ae7394ee05c00b6

Passage ID: `qasper-passage-v1-78aa0c147299100029a77f5732e4c645fa58e5523af0357d1ae7394ee05c00b6`; retrieval score: 5.503190946601262.

Word count: 200.

```text
Since the introduction of i-vectors in BIBREF0 , the speaker recognition community has seen a significant increase in recognition performance. i-Vectors are low-dimensional representations of Baum-Welch statistics obtained with respect to a GMM, referred to as universal background model (UBM), in a single subspace which includes all characteristics of speaker and inter-session variability, named total variability matrix BIBREF0 . We trained on each acoustic feature a full covariance, gender-independent UBM model with 2048 Gaussians followed by a 600-dimensional i-vector extractor to establish our MFCC- and PLP-based i-vector systems. The unlabeled set of development data was used in the training of both the UBM and the i-vector extractor. The open-source Kaldi software has been used for all these processing steps BIBREF12 .

It has been shown that successive acoustic observation vectors tend to be highly correlated. This may be problematic for maximum a posteriori (MAP) estimation of i-vectors. To investigating this issue, scaling the zero and first order Baum-Welch statistics before presenting them to the i-vector extractor has been proposed. It turns out that a scale factor of 0.33 gives a slight edge, resulting in a better decision cost function BIBREF13 . This scaling factor has been performed in training the
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1611.00514:5:0` | full | 0:835 |

#### Rank 5: qasper-passage-v1-2a399d6e806efa2d6cf8f211d223f05b75fac322cdd9d1db4466409c4f2e198c

Passage ID: `qasper-passage-v1-2a399d6e806efa2d6cf8f211d223f05b75fac322cdd9d1db4466409c4f2e198c`; retrieval score: 4.652062819318145.

Word count: 169.

```text
is reflected by the recent NIST i-vector machine learning challenge BIBREF1 which was designed to find the most promising algorithmic approaches to speaker recognition specifically on the basis of i-vectors BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 . The outstanding ability of DNN for frame alignment which has achieved remarkable performance in text-independent speaker recognition for English data BIBREF6 , BIBREF7 , failed to provide even comparable recognition performance to the traditional GMM. Therefore, we concentrated on the cepstral based GMM/i-vector system.

We outline in this paper the Intelligent Voice system, techniques and results obtained on the SRE 2016 development set that will mirror the evaluation condition as well as the timing report. Section SECREF2 describes the data used for the system training. The front-end and back-end processing of the system are presented in Sections SECREF3 and SECREF4 respectively. In Section SECREF5 , we describe experimental evaluation of the system on the SRE 2016 development set. Finally, we present a timing analysis of the system in Section SECREF6 .
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 758.

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

#### Rank 1: qasper-passage-v1-c2bdb002930424e65ae7948c623833e964ec4ff1b18d21803ec41061a3b76290

Passage ID: `qasper-passage-v1-c2bdb002930424e65ae7948c623833e964ec4ff1b18d21803ec41061a3b76290`; retrieval score: 6.013413815629019.

Word count: 200.

```text
the latent feature variables from the iFHMM framework are sampled using the mIBP mechanism; and (ii) the features sampled so far, which become observable during this second phase, are used in an adapted version of the beam sampling algorithm BIBREF183 to infer the clustering components (i.e., latent events).

They report results in terms of recall (R), precision (P), and F-score (F) by employing the mention-based B3 metric BIBREF184 , the entity-based CEAF metric BIBREF185 , and the pairwise F1 (PW) metric. Their experiments for show that both of these models work well when the feature and cluster numbers are treated as free parameters, and the selection of feature values is performed automatically.

BIBREF167 argue that events represent complex phenomena and can therefore co-refer fully, being identical, like other researchers have discussed, or co-refer partially, being quasi-identical or only partially identical. Two event mentions fully co-refer if their activity, event or state representation is identical in terms of all features used (e.g., agent, location or time). Two event mentions are quasi-identical if they partially co-refer, i.e., most features are the same, but there may be additional details to one or the other.

When two events fully co-refer, Hovy et al. state
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-8f1c2d420acffe2c167e70da00e380f3dd5af765aa9930c5da6dd4544108670f

Passage ID: `qasper-passage-v1-8f1c2d420acffe2c167e70da00e380f3dd5af765aa9930c5da6dd4544108670f`; retrieval score: 5.7068759953680415.

Word count: 200.

```text
Many authors in linguistics have delved deeper into the nature of event classes and have tried to come up with features or characteristics that can be used to identify whether something (verb or a clause) belongs to a particular event class or not. These features or characteristics are necessary to describe the structure of events in a theoretical sense. Description of event structure usually refers to the actual words used (lexical features or characteristics) and also the structure of clause or sentence (syntactic features or characteristics). Identification of such features may be described as finding parameters of event types or parameterization of event types.

A lot of the work on parameterization of event types/classes use the classes espoused by Vendler. These include BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 , BIBREF13 , BIBREF14 , BIBREF15 and others. We will only briefly touch upon such work in this paper. Our objective is to impress upon the reader that identification of features of event classes is considered an important task by linguists.

For example, BIBREF9 describes Vendler's classes with two binary features or parameters: continuousness: whether an event has duration, and boundedness: whether an event has a (natural) terminal point or endpoint.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-b3be49a509a0538f20e53800eaaf120da12fb6080a4086e89a6c1cdf071b879d

Passage ID: `qasper-passage-v1-b3be49a509a0538f20e53800eaaf120da12fb6080a4086e89a6c1cdf071b879d`; retrieval score: 5.632498803399064.

Word count: 200.

```text
be a unique tool within the TimeML framework in that it is very general, being not based on any pre-established list of event patterns and being domain-independent. Evita can also identify, based on linguistic cues, grammatical information associated with event referring expressions, such as tense, aspect, polarity and modality, as stated in the TimeML specification. Evita does not directly identify event participants, but can work with named entity taggers to link arguments to events.

Evita breaks down the event recognition problem to a number of sub-tasks. Evita preprocesses the input text using the Alembic Workbench POS tagger, lemmatizer to find lexical stems, and chunkier to obtain phrase chunks, verbal, nominal and adjectival, the three that are commonly used as event referring expressions BIBREF142 . For each subtask after pre-processing, it combines linguistic- and statistically-based knowledge. Linguistic knowledge is used in local and limited contexts such as verb phrases and to extract morphological information. Statistical knowledge is used to disambiguate nominal events. The sub-tasks in event recognition in Evita are: determination of event candidates and then the events, identification of grammatical features of events, additional clustering of event chunks for event detection and grammatical feature identification in some situations.

For event
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-3308b67448445faccd7fb7e604183b503bd856c9fcd2ba6ad96f956d1e4b5a13

Passage ID: `qasper-passage-v1-3308b67448445faccd7fb7e604183b503bd856c9fcd2ba6ad96f956d1e4b5a13`; retrieval score: 5.626595572640904.

Word count: 200.

```text
Mathematical logic is used to represent the semantics of language. In particular, we use logic to represent the meaning of single sentences. Early work on events, e.g., Panini (as discussed by BIBREF21 and BIBREF22 ) stated that language encodes two kinds of information–actions and non-actions. Verbs represent actions and nouns represent non-actions or things.

BIBREF23 proposes that one needs an event variable $e$ to represent events in mathematical logic. This variable $e$ is used to represent relations represented by the event denoted by the verb and other constituents in the sentence, such as modifiers. Davidson claims that logically speaking, events are like things in that they can be represented by a variable and this variable can be modified and quantified. A question that arises is: how many arguments should an event predicate (in logic) take BIBREF2 ? Just like nominal modifiers modify nouns, event modifiers can modify event predicates. An event predicate can take any number of modifiers just like noun (nominal) modifiers. Examples of event modifiers are: time, place, manner and instrument. Davidson proposed that an event predicate may take one or more required arguments (is this true?) and any number of adjuncts or optional modifiers. Consider the following
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-32bfa9108a99ae06c34d04e3cc1e7435a079fadf1fd48a49bfecccd0252023ad

Passage ID: `qasper-passage-v1-32bfa9108a99ae06c34d04e3cc1e7435a079fadf1fd48a49bfecccd0252023ad`; retrieval score: 5.446026355454158.

Word count: 40.

```text
Different models of events have been used in computational linguistics work geared toward information extraction.

We discuss TimeML events next followed by events. We discuss biomedical event extraction in Section , and extraction of events from Twitter in Section .
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 840.

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

#### Rank 1: qasper-passage-v1-a3549821c13e2ae0cfdebf31e012478846b43c6ab0ba5e34285b9b360abdc160

Passage ID: `qasper-passage-v1-a3549821c13e2ae0cfdebf31e012478846b43c6ab0ba5e34285b9b360abdc160`; retrieval score: 6.667767640360605.

Word count: 84.

```text
Chatino is a group of languages spoken in Oaxaca, Mexico. Together with the Zapotec language group, the Chatino languages form the Zapotecan branch of the Otomanguean language family. There are three main Chatino languages: Zenzontepec Chatino (ZEN, ISO 639-2 code czn), Tataltepec Chatino (TAT, cta), and Eastern Chatino (ISO 639-2 ctp, cya, ctz, and cly) (E.Cruz 2011 and Campbell 2011). San Juan Quiahije Chatino (SJQ), the language of the focus of this study, belongs to Eastern Chatino, and is used by about 3000 speakers.
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-124a2e1e2141cca70b529cb1ce04a7a140d30ae2c2c09f84c8f7878281dd9b50

Passage ID: `qasper-passage-v1-124a2e1e2141cca70b529cb1ce04a7a140d30ae2c2c09f84c8f7878281dd9b50`; retrieval score: 5.866894857293612.

Word count: 200.

```text
language stays in use. We believe that a major avenue towards continual language use is by further creating language technologies for endangered languages, essentially elevating them to the same level as high-resource, economically or politically stronger languages.

The majority of the world's languages are categorized as synthetic, meaning that they have rich morphology, be it fusional, agglutinative, polysynthetic, or a mixture thereof. As Natural Language Processing (NLP) keeps expanding its frontiers to encompass more and more languages, modeling of the grammatical functions that guide language generation is of utmost importance. It follows, then, that the next crucial step for expanding NLP research on endangered languages is creating benchmarks for standard NLP tasks in such languages.

With this work we take a small first step towards this direction. We present a resource that allows for benchmarking two NLP tasks in San Juan Quiahije Chatino, an endangered language spoken in southern Mexico: morphological analysis and morphological inflection, with a focus on the verb morphology of the language.

We first briefly discuss the Chatino language and the intricacies of its verb morphology (§SECREF2), then describe the resource (§SECREF3), and finally present baseline results on both the morphological analysis and the inflection tasks using
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-8a869ab4e7118b18884597ddaadb763b7203863e4b4f8a0241439938634de9e6

Passage ID: `qasper-passage-v1-8a869ab4e7118b18884597ddaadb763b7203863e4b4f8a0241439938634de9e6`; retrieval score: 5.3990173642891435.

Word count: 99.

```text
Eastern Chatino languages , including SJQ Chatino, are intensively tonal BIBREF2, BIBREF3. Tones mark both lexical and grammatical distinctions in Eastern Chatino languages.

In SJQ Chatino, there are eleven tones. Three different systems for representing tone distinctions are employed in the literature: the S-H-M-L system of BIBREF2; the numeral system of BIBREF4; and the alphabetic system of BIBREF3. The correspondences among these three systems are given in Table . For present purposes, we will use numeral representations of the second sort. The number 1 represents a high pitch, 4 represents a low pitch, and double digits represent contour tones.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-ddaeba14504692874c3422aaa855a42b0b520e9788d3fcead7d0d233f662ec50

Passage ID: `qasper-passage-v1-ddaeba14504692874c3422aaa855a42b0b520e9788d3fcead7d0d233f662ec50`; retrieval score: 4.6187027491811.

Word count: 51.

```text
verb morphology of the language.

We first briefly discuss the Chatino language and the intricacies of its verb morphology (§SECREF2), then describe the resource (§SECREF3), and finally present baseline results on both the morphological analysis and the inflection tasks using state-of-the-art neural models (§SECREF4). We make our resource publicly available online.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-32112b3ae271380267513c0621dfefc25d7bc32bfd4b43c670e9f39cb6cb072e

Passage ID: `qasper-passage-v1-32112b3ae271380267513c0621dfefc25d7bc32bfd4b43c670e9f39cb6cb072e`; retrieval score: 4.4601778684423525.

Word count: 200.

```text
We provide a hand-curated collection of complete inflection tables for 198 lemmata. The morphological tags follow the guidelines of the UniMorph schema BIBREF6, BIBREF7, in order to allow for the potential of cross-lingual transfer learning, and they are tagged with respect to:

Person: first (1), second (2), and third (3)

Number: singular (SG) ad plural (PL)

Inclusivity (only applicable to first person plural verbs: inclusive (INCL) and exclusive (EXCL)

Aspect/mood: completive (CPL), progressive (PROG), potential (POT), and habitual (HAB).

Two examples of complete inflection tables for the verbs ndyu2 `fell from above' and lyu1 `fall' are shown in Table . Note how the first verb has the same PN triplet for all four aspect/mood categories, while the second paradigm is more representative in that it involves three different triplets (one for the completive, another for the progressive, and another for the habitual/potential). This variety is at the core of why the SJQ verb morphology is particularly interesting, and a challenging testcase for modern NLP systems.

In total, we end up with 4716 groupings (triplets) of a lemma, a tag-set, and a form; we split these groupings randomly into a training set (3774 groupings), a development set (471 groupings), and test
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 634.

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
