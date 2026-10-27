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

#### Rank 1: qasper-passage-v1-3f249c49ed28101cb907c95f3140cf3511d1cc6b2b0f9c76b31611737b2a9300

Passage ID: `qasper-passage-v1-3f249c49ed28101cb907c95f3140cf3511d1cc6b2b0f9c76b31611737b2a9300`; retrieval score: 17.577429567060612.

Word count: 146.

```text
mask each word of the summary and predict the refined word one-by-one using a refine decoder. To further improve the naturalness of the generated sequence, we cooperate reinforcement objective with the refine decoder.

The main contributions of this work are:

1. We propose a natural language generation model based on BERT, making good use of the pre-trained language model in the encoder and decoder process, and the model can be trained end-to-end without handcrafted features.

2. We design a two-stage decoder process. In this architecture, our model can generate each word of the summary considering both sides' context information.

3. We conduct experiments on the benchmark datasets CNN/Daily Mail and New York Times. Our model achieves a 33.33 average of ROUGE-1, ROUGE-2 and ROUGE-L on the CNN/Daily Mail, which is state-of-the-art. On the New York Times dataset, our model achieves about 5.6% relative improvement over ROUGE-1.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1902.09243:0:5` | full | 0:220 |

#### Rank 2: qasper-passage-v1-4064a8790377cd2c90b2088efa419e1e21f7dc98e62583f10dcc5c414c49cbd3

Passage ID: `qasper-passage-v1-4064a8790377cd2c90b2088efa419e1e21f7dc98e62583f10dcc5c414c49cbd3`; retrieval score: 9.048580402981353.

Word count: 200.

```text
two issues in previous abstractive methods: 1) these methods use left-context-only decoder, thus do not have complete context when predicting each word. 2) they do not utilize the pre-trained contextualized language models on the decoder side, so it is more difficult for the decoder to learn summary representations, context interactions and language modeling together.

Recently, BERT has been successfully used in various natural language processing tasks, such as textual entailment, name entity recognition and machine reading comprehensions. In this paper, we present a novel natural language generation model based on pre-trained language models (we use BERT in this work). As far as we know, this is the first work to extend BERT to the sequence generation task. To address the above issues of previous abstractive methods, in our model, we design a two-stage decoding process to make good use of BERT's context modeling ability. On the first stage, we generate the summary using a left-context-only-decoder. On the second stage, we mask each word of the summary and predict the refined word one-by-one using a refine decoder. To further improve the naturalness of the generated sequence, we cooperate reinforcement objective with the refine decoder.

The main contributions of this work are:
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-8d2b5aaa1fb60b2d56a0b70de4cafcb717fb8f249d775fe22c67e140975f5ab1

Passage ID: `qasper-passage-v1-8d2b5aaa1fb60b2d56a0b70de4cafcb717fb8f249d775fe22c67e140975f5ab1`; retrieval score: 8.727756396042215.

Word count: 142.

```text
Pre-trained word vectors BIBREF17 , BIBREF18 , BIBREF19 have been widely used in many NLP tasks. More recently, pre-trained language models (ELMo, GPT and BERT), have also achieved great success on several NLP problems such as textual entailment, semantic similarity, reading comprehension, and question answering BIBREF20 , BIBREF21 , BIBREF22 .

Some recent works also focus on leveraging pre-trained language models in summarization. BIBREF23 pretrain a language model and use it as the sentiment analyser when generating reviews of goods. BIBREF24 train a language model on golden summaries, and then use it on the decoder side to incorporate prior knowledge.

In this work, we use BERT(which is a pre-trained language model using large scale unlabeled data) on the encoder and decoder of a seq2seq model, and by designing a two stage decoding structure we build a competitive model for abstractive text summarization.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-4e1c6b990cc44b7d529ea4f3db32df65f12a721c242b6b6e7ecd2a4c1b9ef4ef

Passage ID: `qasper-passage-v1-4e1c6b990cc44b7d529ea4f3db32df65f12a721c242b6b6e7ecd2a4c1b9ef4ef`; retrieval score: 8.726322199121247.

Word count: 97.

```text
of input sequence.

$$o_i = h_i + \sum _{j=1}^{N} e_{ij}(h_j W_V) $$   (Eq. 6)

Despite the wide usage and huge success, there is also a mismatch problem between these pre-trained context encoders and sequence-to-sequence models. The issue is that while using a pre-trained context encoder like GPT or BERT, they model token-level representations by conditioning on both direction context. During pre-training, they are fed with complete sequences. However, with a left-context-only decoder, these pre-trained language models will suffer from incomplete and inconsistent context and thus cannot generate good enough context-aware word representations, especially during the inference process.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-c6e17340f8b75f0c6a203986a805e37015c8926f62870056c5e4863d76cc0d05

Passage ID: `qasper-passage-v1-c6e17340f8b75f0c6a203986a805e37015c8926f62870056c5e4863d76cc0d05`; retrieval score: 8.626318952686773.

Word count: 200.

```text
+ RL: Full model with refine process cooperated with RL objective.

First, we compare the Two-Stage+RL model with Two-Stage ablation, we observe that the full model outperforms by 0.30 on average ROUGE, suggesting that the reinforcement objective helps the model effectively. Then we analyze the effect of refine process by removing word-level refine from the Two-Stage model, we observe that without the refine process the average ROUGE score drops by 1.69. The ablation study shows that each module is necessary for our full model, and the improvements are statistically significant on all metrics.

To evaluate the impact of summary length on model performance, we compare the average rouge score improvements of our model with different length of ground-truth summaries. As the above sub-figure of Figure 2 shows, compared to Pointer-Generator with Coverage, on length interval 40-80(occupies about 70% of test set) the improvements of our model are higher than shorter samples, confirms that with better context representations, in longer documents our model can achieve higher performance.

As the below sub-figure of Figure 2 shows, compared to extractive baseline: Lead-3 BIBREF0 , the advantage of our model will fall when golden summary length is greater than 80. This probably because that
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 785.

Fully covered answer annotations: f7e4bad697dd285bffe16e2c1157052a3c4baace.

Missing evidence by answer annotation:

```text
{
  "7eecbe1aed7f283bdd4ca6c207115dbfca91d57d": {
    "unresolved_evidence": [
      "$$L_{model} = \\hat{L}_{dec} + \\hat{L}_{refine}$$ (Eq. 23)"
    ],
    "paragraphs": {
      "1902.09243:7:0": [
        [
          0,
          223
        ]
      ],
      "1902.09243:7:2": [
        [
          0,
          218
        ]
      ]
    }
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

#### Rank 1: qasper-passage-v1-002788a17368f34a888f35e93e3aff7f5c1001cdcdb68b21b0227762435dd44c

Passage ID: `qasper-passage-v1-002788a17368f34a888f35e93e3aff7f5c1001cdcdb68b21b0227762435dd44c`; retrieval score: 6.284025327465458.

Word count: 200.

```text
user divergence behavior at various points in time BIBREF6. By looking at these works, the impact of using text mining and lexical analysis to address important questions becomes obvious. Proper usage of these tools allows the research community to analyze big chunks of unstructured data. This approach, however, became less productive as the social media networks began cracking down and ISIS recruiters moved off of them.

With their ability to operate freely on social media now curtailed, ISIS recruiters and propagandists increased their attentiveness to another longstanding tool–English language online magazines targeting western audiences. Al Hayat, the media wing of ISIS, published multiple online magazines in different languages including English. The English online magazine of ISIS was named Dabiq and first appeared on the dark web on July 2014 and continued publishing for 15 issues. This publication was followed by Rumiyah which produced 13 English language issues through September 2017. The content of these magazines provides a valuable but underutilized resource for understanding ISIS strategies and how they appeal to recruits, specifically English-speaking audiences. They also provide a way to compare ISIS' approach with other radical groups. Ingram compared Dabiq contents with Inspire (Al Qaeda publication) and suggested that Al
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1912.03804:1:2` | partial | 0:934 |

#### Rank 2: qasper-passage-v1-5ca8220ad01fa12518a0a8bfed46f9d450119c8d4260a3df3f09ccdda4c78b0e

Passage ID: `qasper-passage-v1-5ca8220ad01fa12518a0a8bfed46f9d450119c8d4260a3df3f09ccdda4c78b0e`; retrieval score: 5.575947055512034.

Word count: 200.

```text
resource for understanding ISIS strategies and how they appeal to recruits, specifically English-speaking audiences. They also provide a way to compare ISIS' approach with other radical groups. Ingram compared Dabiq contents with Inspire (Al Qaeda publication) and suggested that Al Qaeda heavily emphasized identity-choice, while ISIS' messages were more balanced between identity-choice and rational-choice BIBREF7. In another research paper, Wignell et al. BIBREF8 compared Dabiq and Rumiah by examining their style and what both magazine messages emphasized. Despite the volume of research on these magazines, only a few researchers used lexical analysis and mostly relied on experts' opinions. BIBREF9 is one exception to this approach where they used word frequency on 11 issues of Dabiq publications and compared attributes such as anger, anxiety, power, motive, etc.

This paper seeks to establish how ISIS specifically tailored propaganda targeting western women, who became a particular target for the organization as the “caliphate” expanded. Although the number of recruits is unknown, in 2015 it was estimated that around 10 percent of all western recruits were female BIBREF10. Some researchers have attempted to understand how ISIS propaganda targets women. Kneip, for example, analyzed women's desire to join as a form of emancipation BIBREF11. We
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1912.03804:1:2` | partial | 652:1526 |

#### Rank 3: qasper-passage-v1-0cc6f2cad014e37c04138fc8fb8c334b51e17f585001017a7b80b2ff5c56f175

Passage ID: `qasper-passage-v1-0cc6f2cad014e37c04138fc8fb8c334b51e17f585001017a7b80b2ff5c56f175`; retrieval score: 4.4251987271098.

Word count: 200.

```text
in the text, but in the case of propaganda we are more interested in emotions that are elicited in the reader of such materials. The closest analogy to this problem can be found in research that seek to model feelings of people after reading a news article. One solution for this type of problem is to use an approach called Depechemood.

Depechemood is a lexicon-based emotion detection method gathered from crowd-annotated news BIBREF24. Drawing on approximately 23.5K documents with average of 500 words per document from rappler.com, researchers asked subjects to report their emotions after reading each article. They then multiplied the document-emotion matrix and word-document matrix to derive emotion-word matrix for these words. Due to limitations of their experiment setup, the emotion categories that they present does not exactly match the emotions from the Plutchik wheel categories. However, they still provide a good sense of the general feeling of an individual after reading an article. The emotion categories of Depechemood are: AFRAID, AMUSED, ANGRY, ANNOYED, DON'T CARE, HAPPY, INSPIRED, SAD. Depechemood simply creates dictionaries of words where each word has scores between 0 and 1 for all of these 8 emotion categories. We present our finding using this approach
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-2c2fc21eb6f486d51a7a7738ba386c297ff378e66b9cac7df00fbc61fa92c169

Passage ID: `qasper-passage-v1-2c2fc21eb6f486d51a7a7738ba386c297ff378e66b9cac7df00fbc61fa92c169`; retrieval score: 4.180681664977439.

Word count: 200.

```text
After pre-processing the text, both corpora were analyzed for word frequencies. These word frequencies have been normalized by the number of words in each corpus. Figure FIGREF17 shows the most common words in each of these corpora.

A comparison of common words suggests that those related to marital relationships ( husband, wife, etc.) appear in both corpora, but the religious theme of ISIS material appears to be stronger. A stronger comparison can be made using topic modeling techniques to discover main topics of these documents. Although we used LDA, our results by using NMF outperform LDA topics, due to the nature of these corpora. Also, fewer numbers of ISIS documents might contribute to the comparatively worse performance. Therefore, we present only NMF results. Based on their coherence, we selected 10 topics for analyzing within both corporas. Table TABREF18 and Table TABREF19 show the most important words in each topic with a general label that we assigned to the topic manually. Based on the NMF output, ISIS articles that address women include topics mainly about Islam, women's role in early Islam, hijrah (moving to another land), spousal relations, marriage, and motherhood.

The topics generated from the Catholic women forum are clearly
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-0c08e1b59999df19afb20286c646681a29c82b53c0f43601c1963a4c37189172

Passage ID: `qasper-passage-v1-0c08e1b59999df19afb20286c646681a29c82b53c0f43601c1963a4c37189172`; retrieval score: 4.069900145428864.

Word count: 200.

```text
traveling to the caliphate or by carrying out domestic attacks on behalf of ISIS in their respective countries. This tactical change concerned both practitioners and researchers in the counterterrorism community. New advancements in data science can shed light on exactly how the targeting of women in extremist propaganda works and whether it differs significantly from mainstream religious rhetoric.

We utilize natural language processing methods to answer three questions:

What are the main topics in women-related articles in ISIS' online magazines?

What similarities and/or differences do these topics have with non-violent, non-Islamic religious material addressed specifically to women?

What kind of emotions do these articles evoke in their readers and are there similarities in the emotions evoked from both ISIS and non-violent religious materials?

As these questions suggest, to understand what, if anything, makes extremist appeals distinctive, we need a point of comparison in terms of the outreach efforts to women from a mainstream, non-violent religious group. For this purpose, we rely on an online Catholic women's forum. Comparison between Catholic material and the content of ISIS' online magazines allows for novel insight into the distinctiveness of extremist rhetoric when targeted towards the female population. To accomplish this task, we employ
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
  "3a93821ea58a02da7e9de8da480c74f443d0e908": {
    "unresolved_evidence": [],
    "paragraphs": {
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

#### Rank 1: qasper-passage-v1-dd3509bb8d024c764cdf6370623f5e2c483e5d2de1775e53fed98eaf4e92ad14

Passage ID: `qasper-passage-v1-dd3509bb8d024c764cdf6370623f5e2c483e5d2de1775e53fed98eaf4e92ad14`; retrieval score: 2.493509599930867.

Word count: 200.

```text
There is a wide range of techniques that provide interesting results in the context of ML algorithms geared to the classification of data without discrimination; these techniques range from the pre-processing of data BIBREF4 to the use of bias removal techniques BIBREF5 in fact. Approaches linked to the data pre-processing step usually consist of methods based on improving the quality of the dataset after which the usual classification tools can be used to train a classifier. So, it starts from a baseline already stipulated by the execution of itself. On the other side of the spectrum, there are Unsupervised and semi-supervised learning techniques, that are attractive because they do not imply the cost of corpus annotation BIBREF6 , BIBREF7 , BIBREF8 , BIBREF9 .

The bias reduction is studied as a way to reduce discrimination through classification through different approaches BIBREF10 BIBREF11 . In BIBREF12 the authors propose to specify, implement, and evaluate the “fairness-aware" ML interface called themis-ml. In this interface, the main idea is to pick up a data set from a modified dataset. Themis-ml implements two methods for training fairness-aware models. The tool relies on two methods to make agnostic model type predictions: Reject Option Classification and
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-8603c0788c7d1bcc0bb8f9f8ff74d5d7201fba803840b8ba7dd59a9a507ec69d

Passage ID: `qasper-passage-v1-8603c0788c7d1bcc0bb8f9f8ff74d5d7201fba803840b8ba7dd59a9a507ec69d`; retrieval score: 1.6435571609255475.

Word count: 200.

```text
In BIBREF13 , the quality of the representation of words through vectors in several models is discussed. According to the authors, the ability to train high-quality models using simplified architectures is useful in models composed of predictive methods that try to predict neighboring words with one or more context words, such as Word2Vec. Word embeddings have been used to provide meaningful representations for words in an efficient way.

In BIBREF14 , several word embedding models trained in a large Portuguese corpus are evaluated. Within the Word2Vec model, two training strategies were used. In the first, namely Skip-Gram, the model is given the word and attempts to predict its neighboring words. The second, Continuous Bag-of-Words (CBOW), the model is given the sequence of words without the middle one and attempts to predict this omitted word. The latter was chosen for application in the present proposal.

The authors of BIBREF14 claim to have collected a large corpus from several sources to obtain a multi-genre corpus representative of the Portuguese language. Hence, it comprehensively covers different expressions of the language, making it possible to analyze gender bias and stereotype in Portuguese word embeddings. The dataset used was tokenized and normalized by the authors
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1810.04528:2:1` | full | 0:478 |

#### Rank 3: qasper-passage-v1-f3a16c9bf56412933a0b7bc8e8df96a37ccec340a391f56f9470df38ac61533e

Passage ID: `qasper-passage-v1-f3a16c9bf56412933a0b7bc8e8df96a37ccec340a391f56f9470df38ac61533e`; retrieval score: 1.2860613785763109.

Word count: 160.

```text
Thus, all the results are analyzed by comparing the accuracies.

Using the word2vec model available in a public repository BIBREF14 , the proposal involves the analysis of the most similar analogies generated before and after the application of the BIBREF3 . The work is focused on the analysis of gender bias associated with professions in word embeddings. So therefore into the evaluation of the accuracy of the associations generated, aiming at achieving results as good as possible without prejudicing the evaluation metrics.

Algorithm SECREF4 describes the method performed during the evaluation of the gender bias presence. In this method we try to evaluate the accuracy of the analogies generated through the model, that is, to verify the cases of association matching generated between the words.

[!htb] Model Evaluation [1]

w2v_evaluate INLINEFORM0 open_model( INLINEFORM1 ) count = 0 INLINEFORM2 in INLINEFORM3 read list of tuples x = model.most_similar(positive=[`ela', male], negative=[`ele'])

x = female count += 1 accuracy = count/size(profession_pairs) return accuracy
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-3a7dde394bde798f235e0b91d4a9e27c3e72a95aa8f250d19eed9d9d72a33f93

Passage ID: `qasper-passage-v1-3a7dde394bde798f235e0b91d4a9e27c3e72a95aa8f250d19eed9d9d72a33f93`; retrieval score: 1.0423378019547613.

Word count: 56.

```text
a multi-genre corpus representative of the Portuguese language. Hence, it comprehensively covers different expressions of the language, making it possible to analyze gender bias and stereotype in Portuguese word embeddings. The dataset used was tokenized and normalized by the authors to reduce the corpus vocabulary size, under the premise that vocabulary reduction provides more representative vectors.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-ceb95467c47064c7d17a4b20662a2fe9b653b4ee7303ff94124dd2963da6806e

Passage ID: `qasper-passage-v1-ceb95467c47064c7d17a4b20662a2fe9b653b4ee7303ff94124dd2963da6806e`; retrieval score: 1.02831694893434.

Word count: 200.

```text
Some linguists point out that the female gender is, in Portuguese, a particularization of the masculine. In this way the only gender mark is the feminine, the others being considered without gender (including names considered masculine). In BIBREF15 the gender representation in Portuguese is associated with a set of phenomena, not only from a linguistic perspective but also from a socio-cultural perspective. Since most of the termination of words (e.g., advogada and advogado) are used to indicate to whom the expression refers, stereotypes can be explained through communication. This implies the presence of biases when dealing with terms such as those referring to professions.

Figure FIGREF1 illustrates the approach proposed in this work. First, using a list of professions relating the identification of female and male who perform it as a parameter, we evaluate the accuracy of similarity generated by the embeddings. Then, getting the biased results, we apply the De-bias algorithm BIBREF3 aiming to reduce sexist analogies previous generated. Thus, all the results are analyzed by comparing the accuracies.

Using the word2vec model available in a public repository BIBREF14 , the proposal involves the analysis of the most similar analogies generated before and after the application of the BIBREF3
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 816.

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
