# Evidence Review

## Question: feafcc1c4026d7f55a2c8ce7850d7e12030b5c22

### Question ID and text

Question ID: `feafcc1c4026d7f55a2c8ce7850d7e12030b5c22`; paper ID: `1902.09243`.

```text
How are the different components of the model trained? Is it trained end-to-end?
```

### Answers

#### Answer: 7eecbe1aed7f283bdd4ca6c207115dbfca91d57d

```text
{"evidence": ["1. We propose a natural language generation model based on BERT, making good use of the pre-trained language model in the encoder and decoder process, and the model can be trained end-to-end without handcrafted features.", "During model training, the objective of our model is sum of the two processes, jointly trained using \"teacher-forcing\" algorithm. During training we feed the ground-truth summary to each decoder and minimize the objective.", "$$L_{model} = \\hat{L}_{dec} + \\hat{L}_{refine}$$ (Eq. 23)", "At test time, each time step we choose the predicted word by $\\hat{y} = argmax_{y^{\\prime }} P(y^{\\prime }|x)$ , use beam search to generate the draft summaries, and use greedy search to generate the refined summaries."], "extractive_spans": ["the objective of our model is sum of the two processes, jointly trained using \"teacher-forcing\" algorithm", "we feed the ground-truth summary to each decoder and minimize the objective", "At test time, each time step we choose the predicted word by $\\hat{y} = argmax_{y^{\\prime }} P(y^{\\prime }|x)$ , use beam search to generate the draft summaries, and use greedy search to generate the refined summaries.", "the model can be trained end-to-end"], "free_form_answer": "", "highlighted_evidence": ["We propose a natural language generation model based on BERT, making good use of the pre-trained language model in the encoder and decoder process, and the model can be trained end-to-end without handcrafted features.", "During model training, the objective of our model is sum of the two processes, jointly trained using \"teacher-forcing\" algorithm. During training we feed the ground-truth summary to each decoder and minimize the objective.\n\n$$L_{model} = \\hat{L}_{dec} + \\hat{L}_{refine}$$ (Eq. 23)\n\nAt test time, each time step we choose the predicted word by $\\hat{y} = argmax_{y^{\\prime }} P(y^{\\prime }|x)$ , use beam search to generate the draft summaries, and use greedy search to generate the refined summaries."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1902.09243:0:5`

```text
1. We propose a natural language generation model based on BERT, making good use of the pre-trained language model in the encoder and decoder process, and the model can be trained end-to-end without handcrafted features.
```

Evidence location: `1902.09243:7:0`

```text
During model training, the objective of our model is sum of the two processes, jointly trained using "teacher-forcing" algorithm. During training we feed the ground-truth summary to each decoder and minimize the objective. 
```

Evidence location: `1902.09243:7:2`

```text
At test time, each time step we choose the predicted word by $\hat{y} = argmax_{y^{\prime }} P(y^{\prime }|x)$ , use beam search to generate the draft summaries, and use greedy search to generate the refined summaries.
```

Limitation: no usable complete text evidence set for this annotation.

Unresolved evidence:

```text
["$$L_{model} = \\hat{L}_{dec} + \\hat{L}_{refine}$$ (Eq. 23)"]
```

#### Answer: f7e4bad697dd285bffe16e2c1157052a3c4baace

```text
{"evidence": ["1. We propose a natural language generation model based on BERT, making good use of the pre-trained language model in the encoder and decoder process, and the model can be trained end-to-end without handcrafted features."], "extractive_spans": ["the model can be trained end-to-end"], "free_form_answer": "", "highlighted_evidence": ["We propose a natural language generation model based on BERT, making good use of the pre-trained language model in the encoder and decoder process, and the model can be trained end-to-end without handcrafted features."], "unanswerable": false, "yes_no": null}
```

Evidence location: `1902.09243:0:5`

```text
1. We propose a natural language generation model based on BERT, making good use of the pre-trained language model in the encoder and decoder process, and the model can be trained end-to-end without handcrafted features.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-f08fefef04b0cf3aa30673d28ecbb5ceffe310ddf8108f337109a5289fcdbce3

Passage ID: `qasper-passage-v1-f08fefef04b0cf3aa30673d28ecbb5ceffe310ddf8108f337109a5289fcdbce3`; retrieval score: 19.0866486138257.

Word count: 136.

```text
word one-by-one using a refine decoder. To further improve the naturalness of the generated sequence, we cooperate reinforcement objective with the refine decoder.

The main contributions of this work are:

1. We propose a natural language generation model based on BERT, making good use of the pre-trained language model in the encoder and decoder process, and the model can be trained end-to-end without handcrafted features.

2. We design a two-stage decoder process. In this architecture, our model can generate each word of the summary considering both sides' context information.

3. We conduct experiments on the benchmark datasets CNN/Daily Mail and New York Times. Our model achieves a 33.33 average of ROUGE-1, ROUGE-2 and ROUGE-L on the CNN/Daily Mail, which is state-of-the-art. On the New York Times dataset, our model achieves about 5.6% relative improvement over ROUGE-1.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1902.09243:0:5` | full | 0:220 |

#### Rank 2: qasper-passage-v1-58fdfc30738c40174fb885716afd87de96b4c858159cdedefc920b19e9f4c304

Passage ID: `qasper-passage-v1-58fdfc30738c40174fb885716afd87de96b4c858159cdedefc920b19e9f4c304`; retrieval score: 10.006410036154566.

Word count: 142.

```text
Pre-trained word vectors BIBREF17 , BIBREF18 , BIBREF19 have been widely used in many NLP tasks. More recently, pre-trained language models (ELMo, GPT and BERT), have also achieved great success on several NLP problems such as textual entailment, semantic similarity, reading comprehension, and question answering BIBREF20 , BIBREF21 , BIBREF22 .

Some recent works also focus on leveraging pre-trained language models in summarization. BIBREF23 pretrain a language model and use it as the sentiment analyser when generating reviews of goods. BIBREF24 train a language model on golden summaries, and then use it on the decoder side to incorporate prior knowledge.

In this work, we use BERT(which is a pre-trained language model using large scale unlabeled data) on the encoder and decoder of a seq2seq model, and by designing a two stage decoding structure we build a competitive model for abstractive text summarization.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-305877c23096f54fabf65c852c57d85268c0369eae056993867bdd8723cbd998

Passage ID: `qasper-passage-v1-305877c23096f54fabf65c852c57d85268c0369eae056993867bdd8723cbd998`; retrieval score: 9.956138109501765.

Word count: 147.

```text
W^V$ are parameter matrices.

$$&a_{ij} = \cfrac{(h_iW_Q)(h_jW_K)^T}{\sqrt{d_e}}  \\
&e_{ij} = \cfrac{\exp {e_{ij}}}{\sum _{k=1}^N\exp {e_{ik}}} $$   (Eq. 5)

Then the output is calculated as Eq. ( 6 ) shows, which is the weighted sum of previous outputs $h$ added by previous output $h_i$ . The last layer outputs is context encoding of input sequence.

$$o_i = h_i + \sum _{j=1}^{N} e_{ij}(h_j W_V) $$   (Eq. 6)

Despite the wide usage and huge success, there is also a mismatch problem between these pre-trained context encoders and sequence-to-sequence models. The issue is that while using a pre-trained context encoder like GPT or BERT, they model token-level representations by conditioning on both direction context. During pre-training, they are fed with complete sequences. However, with a left-context-only decoder, these pre-trained language models will suffer from incomplete and inconsistent context and thus cannot generate good enough context-aware word representations, especially during the inference process.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-8b9ae461a6884555ab1b23362dc3db4d4418c31312a12cd6baa81617ebfbc2c0

Passage ID: `qasper-passage-v1-8b9ae461a6884555ab1b23362dc3db4d4418c31312a12cd6baa81617ebfbc2c0`; retrieval score: 9.744836088680854.

Word count: 150.

```text
without the refine process the average ROUGE score drops by 1.69. The ablation study shows that each module is necessary for our full model, and the improvements are statistically significant on all metrics.

To evaluate the impact of summary length on model performance, we compare the average rouge score improvements of our model with different length of ground-truth summaries. As the above sub-figure of Figure 2 shows, compared to Pointer-Generator with Coverage, on length interval 40-80(occupies about 70% of test set) the improvements of our model are higher than shorter samples, confirms that with better context representations, in longer documents our model can achieve higher performance.

As the below sub-figure of Figure 2 shows, compared to extractive baseline: Lead-3 BIBREF0 , the advantage of our model will fall when golden summary length is greater than 80. This probably because that we truncate the long documents and golden summaries and cannot
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-c063bc4cf4f2e5a19e342dde0be577a92de419a7e3c6c54f9f7d155360e71167

Passage ID: `qasper-passage-v1-c063bc4cf4f2e5a19e342dde0be577a92de419a7e3c6c54f9f7d155360e71167`; retrieval score: 9.428142501719272.

Word count: 76.

```text
During model training, the objective of our model is sum of the two processes, jointly trained using "teacher-forcing" algorithm. During training we feed the ground-truth summary to each decoder and minimize the objective.

$$L_{model} = \hat{L}_{dec} + \hat{L}_{refine}$$   (Eq. 23)

At test time, each time step we choose the predicted word by $\hat{y} = argmax_{y^{\prime }} P(y^{\prime }|x)$ , use beam search to generate the draft summaries, and use greedy search to generate the refined summaries.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1902.09243:7:0` | full | 0:222 |
| `1902.09243:7:2` | full | 0:218 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 651.

Fully covered answer annotations: f7e4bad697dd285bffe16e2c1157052a3c4baace.

Missing evidence by answer annotation:

```text
{
  "7eecbe1aed7f283bdd4ca6c207115dbfca91d57d": {
    "unresolved_evidence": [
      "$$L_{model} = \\hat{L}_{dec} + \\hat{L}_{refine}$$ (Eq. 23)"
    ],
    "paragraphs": {}
  },
  "f7e4bad697dd285bffe16e2c1157052a3c4baace": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: 2ccc26e11df4eb26fcccdd1f446dc749aff5d572

### Question ID and text

Question ID: `2ccc26e11df4eb26fcccdd1f446dc749aff5d572`; paper ID: `1912.03804`.

```text
Do they report results only on English data?
```

### Answers

#### Answer: 3a93821ea58a02da7e9de8da480c74f443d0e908

```text
{"evidence": ["With their ability to operate freely on social media now curtailed, ISIS recruiters and propagandists increased their attentiveness to another longstanding tool–English language online magazines targeting western audiences. Al Hayat, the media wing of ISIS, published multiple online magazines in different languages including English. The English online magazine of ISIS was named Dabiq and first appeared on the dark web on July 2014 and continued publishing for 15 issues. This publication was followed by Rumiyah which produced 13 English language issues through September 2017. The content of these magazines provides a valuable but underutilized resource for understanding ISIS strategies and how they appeal to recruits, specifically English-speaking audiences. They also provide a way to compare ISIS' approach with other radical groups. Ingram compared Dabiq contents with Inspire (Al Qaeda publication) and suggested that Al Qaeda heavily emphasized identity-choice, while ISIS' messages were more balanced between identity-choice and rational-choice BIBREF7. In another research paper, Wignell et al. BIBREF8 compared Dabiq and Rumiah by examining their style and what both magazine messages emphasized. Despite the volume of research on these magazines, only a few researchers used lexical analysis and mostly relied on experts' opinions. BIBREF9 is one exception to this approach where they used word frequency on 11 issues of Dabiq publications and compared attributes such as anger, anxiety, power, motive, etc.", "Finding useful collections of texts where ISIS targets women is a challenging task. Most of the available material are not reflecting ISIS' official point of view or they do not talk specifically about women. However, ISIS' online magazines are valuable resources for understanding how the organization attempts to appeal to western audiences, particularly women. Looking through both Dabiq and Rumiyah, many issues of the magazines contain articles specifically addressing women, usually with “ to our sisters ” incorporated into the title. Seven out of fifteen Dabiq issues and all thirteen issues of Rumiyah contain articles targeting women, clearly suggesting an increase in attention to women over time."], "extractive_spans": [], "free_form_answer": "", "highlighted_evidence": ["The English online magazine of ISIS was named Dabiq and first appeared on the dark web on July 2014 and continued publishing for 15 issues. This publication was followed by Rumiyah which produced 13 English language issues through September 2017.", "Looking through both Dabiq and Rumiyah, many issues of the magazines contain articles specifically addressing women, usually with “ to our sisters ” incorporated into the title."], "unanswerable": false, "yes_no": true}
```

Evidence location: `1912.03804:1:2`

```text
With their ability to operate freely on social media now curtailed, ISIS recruiters and propagandists increased their attentiveness to another longstanding tool–English language online magazines targeting western audiences. Al Hayat, the media wing of ISIS, published multiple online magazines in different languages including English. The English online magazine of ISIS was named Dabiq and first appeared on the dark web on July 2014 and continued publishing for 15 issues. This publication was followed by Rumiyah which produced 13 English language issues through September 2017. The content of these magazines provides a valuable but underutilized resource for understanding ISIS strategies and how they appeal to recruits, specifically English-speaking audiences. They also provide a way to compare ISIS' approach with other radical groups. Ingram compared Dabiq contents with Inspire (Al Qaeda publication) and suggested that Al Qaeda heavily emphasized identity-choice, while ISIS' messages were more balanced between identity-choice and rational-choice BIBREF7. In another research paper, Wignell et al. BIBREF8 compared Dabiq and Rumiah by examining their style and what both magazine messages emphasized. Despite the volume of research on these magazines, only a few researchers used lexical analysis and mostly relied on experts' opinions. BIBREF9 is one exception to this approach where they used word frequency on 11 issues of Dabiq publications and compared attributes such as anger, anxiety, power, motive, etc.
```

Evidence location: `1912.03804:2:0`

```text
Finding useful collections of texts where ISIS targets women is a challenging task. Most of the available material are not reflecting ISIS' official point of view or they do not talk specifically about women. However, ISIS' online magazines are valuable resources for understanding how the organization attempts to appeal to western audiences, particularly women. Looking through both Dabiq and Rumiyah, many issues of the magazines contain articles specifically addressing women, usually with “ to our sisters ” incorporated into the title. Seven out of fifteen Dabiq issues and all thirteen issues of Rumiyah contain articles targeting women, clearly suggesting an increase in attention to women over time.
```

#### Answer: 61b98560b9a7f63f0b2538f9f7238375ca446378

```text
{"evidence": [], "extractive_spans": [], "free_form_answer": "", "highlighted_evidence": [], "unanswerable": false, "yes_no": true}
```

Limitation: no usable complete text evidence set for this annotation.

### Retrieved chunks

#### Rank 1: qasper-passage-v1-2dfacbf30876e0fb6aacedcd31d4d7074d8a2a3aa77287415d90d46e8aa4c925

Passage ID: `qasper-passage-v1-2dfacbf30876e0fb6aacedcd31d4d7074d8a2a3aa77287415d90d46e8aa4c925`; retrieval score: 6.686163307104533.

Word count: 150.

```text
first appeared on the dark web on July 2014 and continued publishing for 15 issues. This publication was followed by Rumiyah which produced 13 English language issues through September 2017. The content of these magazines provides a valuable but underutilized resource for understanding ISIS strategies and how they appeal to recruits, specifically English-speaking audiences. They also provide a way to compare ISIS' approach with other radical groups. Ingram compared Dabiq contents with Inspire (Al Qaeda publication) and suggested that Al Qaeda heavily emphasized identity-choice, while ISIS' messages were more balanced between identity-choice and rational-choice BIBREF7. In another research paper, Wignell et al. BIBREF8 compared Dabiq and Rumiah by examining their style and what both magazine messages emphasized. Despite the volume of research on these magazines, only a few researchers used lexical analysis and mostly relied on experts' opinions. BIBREF9 is one exception to this approach where they used word frequency
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1912.03804:1:2` | partial | 392:1423 |

#### Rank 2: qasper-passage-v1-ef75d4d1d77696b70c1411f3d976cfa1b5502078cc1e50f2051f43bc443c5b10

Passage ID: `qasper-passage-v1-ef75d4d1d77696b70c1411f3d976cfa1b5502078cc1e50f2051f43bc443c5b10`; retrieval score: 5.788652211773767.

Word count: 150.

```text
looking at these works, the impact of using text mining and lexical analysis to address important questions becomes obvious. Proper usage of these tools allows the research community to analyze big chunks of unstructured data. This approach, however, became less productive as the social media networks began cracking down and ISIS recruiters moved off of them.

With their ability to operate freely on social media now curtailed, ISIS recruiters and propagandists increased their attentiveness to another longstanding tool–English language online magazines targeting western audiences. Al Hayat, the media wing of ISIS, published multiple online magazines in different languages including English. The English online magazine of ISIS was named Dabiq and first appeared on the dark web on July 2014 and continued publishing for 15 issues. This publication was followed by Rumiyah which produced 13 English language issues through September 2017. The content of these magazines provides a valuable but underutilized
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1912.03804:1:2` | partial | 0:651 |

#### Rank 3: qasper-passage-v1-5a4a457d3eede39f9f013632a682795d5a8948ef9ea0c876b9630aa2a7f25030

Passage ID: `qasper-passage-v1-5a4a457d3eede39f9f013632a682795d5a8948ef9ea0c876b9630aa2a7f25030`; retrieval score: 4.468556553009455.

Word count: 150.

```text
Although discontinued now, these online resources provided a window into ISIS ideology, recruitment, and how they wanted the world to perceive them. For example, after predominantly recruiting men, ISIS began to also include articles in their magazines that specifically addressed women. ISIS encouraged women to join the group by either traveling to the caliphate or by carrying out domestic attacks on behalf of ISIS in their respective countries. This tactical change concerned both practitioners and researchers in the counterterrorism community. New advancements in data science can shed light on exactly how the targeting of women in extremist propaganda works and whether it differs significantly from mainstream religious rhetoric.

We utilize natural language processing methods to answer three questions:

What are the main topics in women-related articles in ISIS' online magazines?

What similarities and/or differences do these topics have with non-violent, non-Islamic religious material addressed specifically to women?

What kind of
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-71547367f1d631d0e2c8cc6c120d5849cf1b6a67f844d722714d229d7c53187b

Passage ID: `qasper-passage-v1-71547367f1d631d0e2c8cc6c120d5849cf1b6a67f844d722714d229d7c53187b`; retrieval score: 4.318085998228249.

Word count: 150.

```text
After pre-processing the text, both corpora were analyzed for word frequencies. These word frequencies have been normalized by the number of words in each corpus. Figure FIGREF17 shows the most common words in each of these corpora.

A comparison of common words suggests that those related to marital relationships ( husband, wife, etc.) appear in both corpora, but the religious theme of ISIS material appears to be stronger. A stronger comparison can be made using topic modeling techniques to discover main topics of these documents. Although we used LDA, our results by using NMF outperform LDA topics, due to the nature of these corpora. Also, fewer numbers of ISIS documents might contribute to the comparatively worse performance. Therefore, we present only NMF results. Based on their coherence, we selected 10 topics for analyzing within both corporas. Table TABREF18 and Table TABREF19 show the most important words in each topic with
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-33267b32b888acf34167651390811e18259a8effa64e43e0e26974f5efd86a76

Passage ID: `qasper-passage-v1-33267b32b888acf34167651390811e18259a8effa64e43e0e26974f5efd86a76`; retrieval score: 4.304075344900628.

Word count: 144.

```text
Depechemood.

Depechemood is a lexicon-based emotion detection method gathered from crowd-annotated news BIBREF24. Drawing on approximately 23.5K documents with average of 500 words per document from rappler.com, researchers asked subjects to report their emotions after reading each article. They then multiplied the document-emotion matrix and word-document matrix to derive emotion-word matrix for these words. Due to limitations of their experiment setup, the emotion categories that they present does not exactly match the emotions from the Plutchik wheel categories. However, they still provide a good sense of the general feeling of an individual after reading an article. The emotion categories of Depechemood are: AFRAID, AMUSED, ANGRY, ANNOYED, DON'T CARE, HAPPY, INSPIRED, SAD. Depechemood simply creates dictionaries of words where each word has scores between 0 and 1 for all of these 8 emotion categories. We present our finding using this approach in the result section.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: false

Complete evidence rate@5: false

Total retrieved words: 744.

Fully covered answer annotations: none.

Missing evidence by answer annotation:

```text
{
  "3a93821ea58a02da7e9de8da480c74f443d0e908": {
    "unresolved_evidence": [],
    "paragraphs": {
      "1912.03804:1:2": [
        [
          1423,
          1526
        ]
      ],
      "1912.03804:2:0": [
        [
          0,
          708
        ]
      ]
    }
  },
  "61b98560b9a7f63f0b2538f9f7238375ca446378": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```

## Question: 09f0dce416a1e40cc6a24a8b42a802747d2c9363

### Question ID and text

Question ID: `09f0dce416a1e40cc6a24a8b42a802747d2c9363`; paper ID: `1810.04528`.

```text
Which word embeddings are analysed?
```

### Answers

#### Answer: 8b5278bfc35cf0a1b43ceb3418c2c5d20f213a31

```text
{"evidence": ["In BIBREF14 , several word embedding models trained in a large Portuguese corpus are evaluated. Within the Word2Vec model, two training strategies were used. In the first, namely Skip-Gram, the model is given the word and attempts to predict its neighboring words. The second, Continuous Bag-of-Words (CBOW), the model is given the sequence of words without the middle one and attempts to predict this omitted word. The latter was chosen for application in the present proposal."], "extractive_spans": ["Continuous Bag-of-Words (CBOW)"], "free_form_answer": "", "highlighted_evidence": ["The second, Continuous Bag-of-Words (CBOW), the model is given the sequence of words without the middle one and attempts to predict this omitted word. "], "unanswerable": false, "yes_no": null}
```

Evidence location: `1810.04528:2:1`

```text
In BIBREF14 , several word embedding models trained in a large Portuguese corpus are evaluated. Within the Word2Vec model, two training strategies were used. In the first, namely Skip-Gram, the model is given the word and attempts to predict its neighboring words. The second, Continuous Bag-of-Words (CBOW), the model is given the sequence of words without the middle one and attempts to predict this omitted word. The latter was chosen for application in the present proposal.
```

### Retrieved chunks

#### Rank 1: qasper-passage-v1-f63461da7737d7bcec4fcf3c16217f21caee42e2debb86aa27d87303f01102ec

Passage ID: `qasper-passage-v1-f63461da7737d7bcec4fcf3c16217f21caee42e2debb86aa27d87303f01102ec`; retrieval score: 3.597200797062566.

Word count: 150.

```text
There is a wide range of techniques that provide interesting results in the context of ML algorithms geared to the classification of data without discrimination; these techniques range from the pre-processing of data BIBREF4 to the use of bias removal techniques BIBREF5 in fact. Approaches linked to the data pre-processing step usually consist of methods based on improving the quality of the dataset after which the usual classification tools can be used to train a classifier. So, it starts from a baseline already stipulated by the execution of itself. On the other side of the spectrum, there are Unsupervised and semi-supervised learning techniques, that are attractive because they do not imply the cost of corpus annotation BIBREF6 , BIBREF7 , BIBREF8 , BIBREF9 .

The bias reduction is studied as a way to reduce discrimination through classification through different approaches BIBREF10 BIBREF11 . In BIBREF12 the authors propose to specify,
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-9b0b8e10d9040a80329020bb37cdac5ed8bd2486970ac3b2ee9d491e66ba6035

Passage ID: `qasper-passage-v1-9b0b8e10d9040a80329020bb37cdac5ed8bd2486970ac3b2ee9d491e66ba6035`; retrieval score: 1.3653105491086759.

Word count: 150.

```text
In BIBREF13 , the quality of the representation of words through vectors in several models is discussed. According to the authors, the ability to train high-quality models using simplified architectures is useful in models composed of predictive methods that try to predict neighboring words with one or more context words, such as Word2Vec. Word embeddings have been used to provide meaningful representations for words in an efficient way.

In BIBREF14 , several word embedding models trained in a large Portuguese corpus are evaluated. Within the Word2Vec model, two training strategies were used. In the first, namely Skip-Gram, the model is given the word and attempts to predict its neighboring words. The second, Continuous Bag-of-Words (CBOW), the model is given the sequence of words without the middle one and attempts to predict this omitted word. The latter was chosen for application in the present proposal.

The authors of BIBREF14 claim to
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1810.04528:2:1` | full | 0:478 |

#### Rank 3: qasper-passage-v1-241083aa2564d0c4205ffb0bfff57232d57c34aed69e79714e08ced58251acf5

Passage ID: `qasper-passage-v1-241083aa2564d0c4205ffb0bfff57232d57c34aed69e79714e08ced58251acf5`; retrieval score: 1.180954656788545.

Word count: 150.

```text
in this work. First, using a list of professions relating the identification of female and male who perform it as a parameter, we evaluate the accuracy of similarity generated by the embeddings. Then, getting the biased results, we apply the De-bias algorithm BIBREF3 aiming to reduce sexist analogies previous generated. Thus, all the results are analyzed by comparing the accuracies.

Using the word2vec model available in a public repository BIBREF14 , the proposal involves the analysis of the most similar analogies generated before and after the application of the BIBREF3 . The work is focused on the analysis of gender bias associated with professions in word embeddings. So therefore into the evaluation of the accuracy of the associations generated, aiming at achieving results as good as possible without prejudicing the evaluation metrics.

Algorithm SECREF4 describes the method performed during the evaluation of the gender bias presence. In this method we
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-24fdc51ad7ff10419652f52fe9e09710a825c63b984f6b1f815535c2445098bc

Passage ID: `qasper-passage-v1-24fdc51ad7ff10419652f52fe9e09710a825c63b984f6b1f815535c2445098bc`; retrieval score: 0.9498003560444677.

Word count: 150.

```text
Some linguists point out that the female gender is, in Portuguese, a particularization of the masculine. In this way the only gender mark is the feminine, the others being considered without gender (including names considered masculine). In BIBREF15 the gender representation in Portuguese is associated with a set of phenomena, not only from a linguistic perspective but also from a socio-cultural perspective. Since most of the termination of words (e.g., advogada and advogado) are used to indicate to whom the expression refers, stereotypes can be explained through communication. This implies the presence of biases when dealing with terms such as those referring to professions.

Figure FIGREF1 illustrates the approach proposed in this work. First, using a list of professions relating the identification of female and male who perform it as a parameter, we evaluate the accuracy of similarity generated by the embeddings. Then, getting the biased results, we apply the
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-a4c5a10a811de552faab646bbdaef89e8fb902596b95d2e04c86e4ead9d8ae47

Passage ID: `qasper-passage-v1-a4c5a10a811de552faab646bbdaef89e8fb902596b95d2e04c86e4ead9d8ae47`; retrieval score: 0.3562901769498883.

Word count: 106.

```text
The second, Continuous Bag-of-Words (CBOW), the model is given the sequence of words without the middle one and attempts to predict this omitted word. The latter was chosen for application in the present proposal.

The authors of BIBREF14 claim to have collected a large corpus from several sources to obtain a multi-genre corpus representative of the Portuguese language. Hence, it comprehensively covers different expressions of the language, making it possible to analyze gender bias and stereotype in Portuguese word embeddings. The dataset used was tokenized and normalized by the authors to reduce the corpus vocabulary size, under the premise that vocabulary reduction provides more representative vectors.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1810.04528:2:1` | partial | 265:478 |

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 706.

Fully covered answer annotations: 8b5278bfc35cf0a1b43ceb3418c2c5d20f213a31.

Missing evidence by answer annotation:

```text
{
  "8b5278bfc35cf0a1b43ceb3418c2c5d20f213a31": {
    "unresolved_evidence": [],
    "paragraphs": {}
  }
}
```
