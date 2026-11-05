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

#### Rank 1: qasper-passage-v1-a27ee7c6b50c2bd01cd40b08cbf51d9099e742ae8c4c35c58122abf5eff23775

Passage ID: `qasper-passage-v1-a27ee7c6b50c2bd01cd40b08cbf51d9099e742ae8c4c35c58122abf5eff23775`; retrieval score: 15.97571911227073.

Word count: 250.

```text
and language modeling together.

Recently, BERT has been successfully used in various natural language processing tasks, such as textual entailment, name entity recognition and machine reading comprehensions. In this paper, we present a novel natural language generation model based on pre-trained language models (we use BERT in this work). As far as we know, this is the first work to extend BERT to the sequence generation task. To address the above issues of previous abstractive methods, in our model, we design a two-stage decoding process to make good use of BERT's context modeling ability. On the first stage, we generate the summary using a left-context-only-decoder. On the second stage, we mask each word of the summary and predict the refined word one-by-one using a refine decoder. To further improve the naturalness of the generated sequence, we cooperate reinforcement objective with the refine decoder.

The main contributions of this work are:

1. We propose a natural language generation model based on BERT, making good use of the pre-trained language model in the encoder and decoder process, and the model can be trained end-to-end without handcrafted features.

2. We design a two-stage decoder process. In this architecture, our model can generate each word of the summary considering both sides' context information.

3. We conduct experiments on the benchmark datasets CNN/Daily Mail and New York Times. Our model achieves a 33.33 average of ROUGE-1, ROUGE-2 and ROUGE-L on the CNN/Daily Mail, which is state-of-the-art. On the New York Times dataset, our model achieves
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1902.09243:0:5` | full | 0:220 |

#### Rank 2: qasper-passage-v1-662365e56d9e1d976cde6a0df4ad7ef3edd1e0bcd5ef768b8996c12f9d53d493

Passage ID: `qasper-passage-v1-662365e56d9e1d976cde6a0df4ad7ef3edd1e0bcd5ef768b8996c12f9d53d493`; retrieval score: 9.073365518806916.

Word count: 192.

```text
removing word-level refine from the Two-Stage model, we observe that without the refine process the average ROUGE score drops by 1.69. The ablation study shows that each module is necessary for our full model, and the improvements are statistically significant on all metrics.

To evaluate the impact of summary length on model performance, we compare the average rouge score improvements of our model with different length of ground-truth summaries. As the above sub-figure of Figure 2 shows, compared to Pointer-Generator with Coverage, on length interval 40-80(occupies about 70% of test set) the improvements of our model are higher than shorter samples, confirms that with better context representations, in longer documents our model can achieve higher performance.

As the below sub-figure of Figure 2 shows, compared to extractive baseline: Lead-3 BIBREF0 , the advantage of our model will fall when golden summary length is greater than 80. This probably because that we truncate the long documents and golden summaries and cannot get full information, it could also because that the training data in these intervals is too few to train an abstractive model, so simple extractive method will not fall too far behind.
```

Evidence coverage: none.

#### Rank 3: qasper-passage-v1-b23cb7032e31abbb6f2979505de4e5d2d1c69f940e93e690907b20053391bcc2

Passage ID: `qasper-passage-v1-b23cb7032e31abbb6f2979505de4e5d2d1c69f940e93e690907b20053391bcc2`; retrieval score: 8.611053527076743.

Word count: 142.

```text
Pre-trained word vectors BIBREF17 , BIBREF18 , BIBREF19 have been widely used in many NLP tasks. More recently, pre-trained language models (ELMo, GPT and BERT), have also achieved great success on several NLP problems such as textual entailment, semantic similarity, reading comprehension, and question answering BIBREF20 , BIBREF21 , BIBREF22 .

Some recent works also focus on leveraging pre-trained language models in summarization. BIBREF23 pretrain a language model and use it as the sentiment analyser when generating reviews of goods. BIBREF24 train a language model on golden summaries, and then use it on the decoder side to incorporate prior knowledge.

In this work, we use BERT(which is a pre-trained language model using large scale unlabeled data) on the encoder and decoder of a seq2seq model, and by designing a two stage decoding structure we build a competitive model for abstractive text summarization.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-6d333f7207252345c24a28365050d48c692cf54f8b07d751ba086cda109161f1

Passage ID: `qasper-passage-v1-6d333f7207252345c24a28365050d48c692cf54f8b07d751ba086cda109161f1`; retrieval score: 8.552920011878218.

Word count: 129.

```text
Table 2 shows experiments on the NYT50 corpus. Since the short summary samples are filtered, NYT50 has average longer summaries than CNN/Daily Mail. So the model needs to catch long-term dependency of the sequences to generate good summaries.

The first two lines of Table 2 show results of the two baselines introduced by BIBREF15 : these baselines select first n sentences, or select the first k words from the original document. Also we compare performance of our model with two recent models, we see 2.39 ROUGE-1 improvements compared to the ML+RL with intra-attn approach(previous SOTA) carries over to this dataset, which is a large margin. On ROUGE-2, our model also get an improvement of 0.51. The experiment proves that our approach can outperform competitive methods on different data distributions.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-d3d0231845717f3c95088fec32732b897d364071041c9708202533cbab274d31

Passage ID: `qasper-passage-v1-d3d0231845717f3c95088fec32732b897d364071041c9708202533cbab274d31`; retrieval score: 8.542472949944539.

Word count: 250.

```text
Recently, context encoders such as ELMo, GPT, and BERT have been widely used in many NLP tasks. These models are pre-trained on a huge unlabeled corpus and can generate better contextualized token embeddings, thus the approaches built on top of them can achieve better performance.

Since our method is based on BERT, we illustrate the process briefly here. BERT consists of several layers. In each layer there is first a multi-head self-attention sub-layer and then a linear affine sub-layer with the residual connection. In each self-attention sub-layer the attention scores $e_{ij}$ are first calculated as Eq. ( 5 ) () shows, in which $d_e$ is output dimension, and $W^Q, W^K, W^V$ are parameter matrices.

$$&a_{ij} = \cfrac{(h_iW_Q)(h_jW_K)^T}{\sqrt{d_e}}  \\
&e_{ij} = \cfrac{\exp {e_{ij}}}{\sum _{k=1}^N\exp {e_{ik}}} $$   (Eq. 5)

Then the output is calculated as Eq. ( 6 ) shows, which is the weighted sum of previous outputs $h$ added by previous output $h_i$ . The last layer outputs is context encoding of input sequence.

$$o_i = h_i + \sum _{j=1}^{N} e_{ij}(h_j W_V) $$   (Eq. 6)

Despite the wide usage and huge success, there is also a mismatch problem between these pre-trained context encoders and sequence-to-sequence models. The issue is that while using a pre-trained context encoder like GPT or BERT, they model token-level representations by conditioning on both direction context. During pre-training, they are fed with complete sequences. However, with a left-context-only decoder, these pre-trained language models will suffer from incomplete and inconsistent context and thus cannot generate good enough context-aware
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 963.

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

#### Rank 1: qasper-passage-v1-698521bebc24e21a9b0b67b5bc0042d2c3332506729e4d00f6ef1fae2fbcc784

Passage ID: `qasper-passage-v1-698521bebc24e21a9b0b67b5bc0042d2c3332506729e4d00f6ef1fae2fbcc784`; retrieval score: 6.05318529615304.

Word count: 250.

```text
ISIS, published multiple online magazines in different languages including English. The English online magazine of ISIS was named Dabiq and first appeared on the dark web on July 2014 and continued publishing for 15 issues. This publication was followed by Rumiyah which produced 13 English language issues through September 2017. The content of these magazines provides a valuable but underutilized resource for understanding ISIS strategies and how they appeal to recruits, specifically English-speaking audiences. They also provide a way to compare ISIS' approach with other radical groups. Ingram compared Dabiq contents with Inspire (Al Qaeda publication) and suggested that Al Qaeda heavily emphasized identity-choice, while ISIS' messages were more balanced between identity-choice and rational-choice BIBREF7. In another research paper, Wignell et al. BIBREF8 compared Dabiq and Rumiah by examining their style and what both magazine messages emphasized. Despite the volume of research on these magazines, only a few researchers used lexical analysis and mostly relied on experts' opinions. BIBREF9 is one exception to this approach where they used word frequency on 11 issues of Dabiq publications and compared attributes such as anger, anxiety, power, motive, etc.

This paper seeks to establish how ISIS specifically tailored propaganda targeting western women, who became a particular target for the organization as the “caliphate” expanded. Although the number of recruits is unknown, in 2015 it was estimated that around 10 percent of all western recruits were female BIBREF10. Some researchers have attempted to understand how ISIS propaganda targets women. Kneip, for example, analyzed women's
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1912.03804:1:2` | partial | 252:1526 |

#### Rank 2: qasper-passage-v1-e060e03b4cd27f33ffe55978ecfb29b1028ea16e9b3832345e9f63dc268d4888

Passage ID: `qasper-passage-v1-e060e03b4cd27f33ffe55978ecfb29b1028ea16e9b3832345e9f63dc268d4888`; retrieval score: 5.576874452568402.

Word count: 250.

```text
scholars have identified the distinctiveness of this population when it comes to nearly all facets of terrorism.

ISIS used different types of media to propagate its messages, such as videos, images, texts, and even music. Twitter was particularly effective and the Arabic Twitter app allowed ISIS to tweet extensively without triggering spam-detection mechanisms the platform uses BIBREF0. Scholars followed the resulting trove of data and this became the preeminent way in which they assess ISIS messages. For example, in BIBREF5 they use both lexical analysis of tweets as well as social network analysis to examine ISIS support or opposition on Twitter. Other researchers used data mining techniques to detect pro-ISIS user divergence behavior at various points in time BIBREF6. By looking at these works, the impact of using text mining and lexical analysis to address important questions becomes obvious. Proper usage of these tools allows the research community to analyze big chunks of unstructured data. This approach, however, became less productive as the social media networks began cracking down and ISIS recruiters moved off of them.

With their ability to operate freely on social media now curtailed, ISIS recruiters and propagandists increased their attentiveness to another longstanding tool–English language online magazines targeting western audiences. Al Hayat, the media wing of ISIS, published multiple online magazines in different languages including English. The English online magazine of ISIS was named Dabiq and first appeared on the dark web on July 2014 and continued publishing for 15 issues. This publication was followed by
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1912.03804:1:2` | partial | 0:508 |

#### Rank 3: qasper-passage-v1-43f4f6274f0c40fb5b64111512d633f2e058364997eacfc5c2bdb91be7bff8a1

Passage ID: `qasper-passage-v1-43f4f6274f0c40fb5b64111512d633f2e058364997eacfc5c2bdb91be7bff8a1`; retrieval score: 4.698136994202313.

Word count: 154.

```text
this type of problem is to use an approach called Depechemood.

Depechemood is a lexicon-based emotion detection method gathered from crowd-annotated news BIBREF24. Drawing on approximately 23.5K documents with average of 500 words per document from rappler.com, researchers asked subjects to report their emotions after reading each article. They then multiplied the document-emotion matrix and word-document matrix to derive emotion-word matrix for these words. Due to limitations of their experiment setup, the emotion categories that they present does not exactly match the emotions from the Plutchik wheel categories. However, they still provide a good sense of the general feeling of an individual after reading an article. The emotion categories of Depechemood are: AFRAID, AMUSED, ANGRY, ANNOYED, DON'T CARE, HAPPY, INSPIRED, SAD. Depechemood simply creates dictionaries of words where each word has scores between 0 and 1 for all of these 8 emotion categories. We present our finding using this approach in the result section.
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-8ec1c23d982d379b52e5946a4ae484c1e372d987eeb57e1ffad6ef44c196d734

Passage ID: `qasper-passage-v1-8ec1c23d982d379b52e5946a4ae484c1e372d987eeb57e1ffad6ef44c196d734`; retrieval score: 4.367171060573711.

Word count: 250.

```text
Since its rise in 2013, the Islamic State of Iraq and Syria (ISIS) has utilized the Internet to spread its ideology, radicalize individuals, and recruit them to their cause. In comparison to other Islamic extremist groups, ISIS' use of technology was more sophisticated, voluminous, and targeted. For example, during ISIS' advance toward Mosul, ISIS related accounts tweeted some 40,000 tweets in one day BIBREF0.However, this heavy engagement forced social media platforms to institute policies to prevent unchecked dissemination of terrorist propaganda to their users, forcing ISIS to adapt to other means to reach their target audience.

One such approach was the publication of online magazines in different languages including English. Although discontinued now, these online resources provided a window into ISIS ideology, recruitment, and how they wanted the world to perceive them. For example, after predominantly recruiting men, ISIS began to also include articles in their magazines that specifically addressed women. ISIS encouraged women to join the group by either traveling to the caliphate or by carrying out domestic attacks on behalf of ISIS in their respective countries. This tactical change concerned both practitioners and researchers in the counterterrorism community. New advancements in data science can shed light on exactly how the targeting of women in extremist propaganda works and whether it differs significantly from mainstream religious rhetoric.

We utilize natural language processing methods to answer three questions:

What are the main topics in women-related articles in ISIS' online magazines?

What similarities and/or differences do these topics have with non-violent,
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-89219e00d5494ffab4ccf2ee8cd3b5800d5fce1f0650a29118a2f5e286b03703

Passage ID: `qasper-passage-v1-89219e00d5494ffab4ccf2ee8cd3b5800d5fce1f0650a29118a2f5e286b03703`; retrieval score: 4.315976529509299.

Word count: 209.

```text
whether it differs significantly from mainstream religious rhetoric.

We utilize natural language processing methods to answer three questions:

What are the main topics in women-related articles in ISIS' online magazines?

What similarities and/or differences do these topics have with non-violent, non-Islamic religious material addressed specifically to women?

What kind of emotions do these articles evoke in their readers and are there similarities in the emotions evoked from both ISIS and non-violent religious materials?

As these questions suggest, to understand what, if anything, makes extremist appeals distinctive, we need a point of comparison in terms of the outreach efforts to women from a mainstream, non-violent religious group. For this purpose, we rely on an online Catholic women's forum. Comparison between Catholic material and the content of ISIS' online magazines allows for novel insight into the distinctiveness of extremist rhetoric when targeted towards the female population. To accomplish this task, we employ topic modeling and an unsupervised emotion detection method.

The rest of the paper is organized as follows: in Section SECREF2, we review related works on ISIS propaganda and applications of natural language methods. Section SECREF3 describes data collection and pre-processing. Section SECREF4 describes in detail the approach. Section SECREF5 reports the results, and finally, Section SECREF6 presents the conclusion.
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: false

Total retrieved words: 1113.

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

#### Rank 1: qasper-passage-v1-d362867d9466755f9ac1e392230cbf03c3d473e3b9f3df17467c4370d3b60978

Passage ID: `qasper-passage-v1-d362867d9466755f9ac1e392230cbf03c3d473e3b9f3df17467c4370d3b60978`; retrieval score: 2.556259335830172.

Word count: 250.

```text
There is a wide range of techniques that provide interesting results in the context of ML algorithms geared to the classification of data without discrimination; these techniques range from the pre-processing of data BIBREF4 to the use of bias removal techniques BIBREF5 in fact. Approaches linked to the data pre-processing step usually consist of methods based on improving the quality of the dataset after which the usual classification tools can be used to train a classifier. So, it starts from a baseline already stipulated by the execution of itself. On the other side of the spectrum, there are Unsupervised and semi-supervised learning techniques, that are attractive because they do not imply the cost of corpus annotation BIBREF6 , BIBREF7 , BIBREF8 , BIBREF9 .

The bias reduction is studied as a way to reduce discrimination through classification through different approaches BIBREF10 BIBREF11 . In BIBREF12 the authors propose to specify, implement, and evaluate the “fairness-aware" ML interface called themis-ml. In this interface, the main idea is to pick up a data set from a modified dataset. Themis-ml implements two methods for training fairness-aware models. The tool relies on two methods to make agnostic model type predictions: Reject Option Classification and Discrimination-Aware Ensemble Classification, these procedures being used to post-process predictions in a way that reduces potentially discriminatory predictions. According to the authors, it is possible to perceive the potential use of the method as a means of reducing bias in the use of ML algorithms.

In BIBREF3 , the authors
```

Evidence coverage: none.

#### Rank 2: qasper-passage-v1-9484bf9101d06174b12dd745ef5afca21820300f760c45bfe29ec0ffc94b4940

Passage ID: `qasper-passage-v1-9484bf9101d06174b12dd745ef5afca21820300f760c45bfe29ec0ffc94b4940`; retrieval score: 1.8309608165525586.

Word count: 216.

```text
In BIBREF13 , the quality of the representation of words through vectors in several models is discussed. According to the authors, the ability to train high-quality models using simplified architectures is useful in models composed of predictive methods that try to predict neighboring words with one or more context words, such as Word2Vec. Word embeddings have been used to provide meaningful representations for words in an efficient way.

In BIBREF14 , several word embedding models trained in a large Portuguese corpus are evaluated. Within the Word2Vec model, two training strategies were used. In the first, namely Skip-Gram, the model is given the word and attempts to predict its neighboring words. The second, Continuous Bag-of-Words (CBOW), the model is given the sequence of words without the middle one and attempts to predict this omitted word. The latter was chosen for application in the present proposal.

The authors of BIBREF14 claim to have collected a large corpus from several sources to obtain a multi-genre corpus representative of the Portuguese language. Hence, it comprehensively covers different expressions of the language, making it possible to analyze gender bias and stereotype in Portuguese word embeddings. The dataset used was tokenized and normalized by the authors to reduce the corpus vocabulary size, under the premise that vocabulary reduction provides more representative vectors.
```

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `1810.04528:2:1` | full | 0:478 |

#### Rank 3: qasper-passage-v1-3374b41be583319105e37cd567475c0d1aca7794de6923182993f0b345d5ac18

Passage ID: `qasper-passage-v1-3374b41be583319105e37cd567475c0d1aca7794de6923182993f0b345d5ac18`; retrieval score: 1.7283348051501728.

Word count: 250.

```text
Some linguists point out that the female gender is, in Portuguese, a particularization of the masculine. In this way the only gender mark is the feminine, the others being considered without gender (including names considered masculine). In BIBREF15 the gender representation in Portuguese is associated with a set of phenomena, not only from a linguistic perspective but also from a socio-cultural perspective. Since most of the termination of words (e.g., advogada and advogado) are used to indicate to whom the expression refers, stereotypes can be explained through communication. This implies the presence of biases when dealing with terms such as those referring to professions.

Figure FIGREF1 illustrates the approach proposed in this work. First, using a list of professions relating the identification of female and male who perform it as a parameter, we evaluate the accuracy of similarity generated by the embeddings. Then, getting the biased results, we apply the De-bias algorithm BIBREF3 aiming to reduce sexist analogies previous generated. Thus, all the results are analyzed by comparing the accuracies.

Using the word2vec model available in a public repository BIBREF14 , the proposal involves the analysis of the most similar analogies generated before and after the application of the BIBREF3 . The work is focused on the analysis of gender bias associated with professions in word embeddings. So therefore into the evaluation of the accuracy of the associations generated, aiming at achieving results as good as possible without prejudicing the evaluation metrics.

Algorithm SECREF4 describes the method performed during the
```

Evidence coverage: none.

#### Rank 4: qasper-passage-v1-f9a6f626c93d717fb2be0b1cd87bf5fa7a1154c8e79f1a820798c02d26c7c3fa

Passage ID: `qasper-passage-v1-f9a6f626c93d717fb2be0b1cd87bf5fa7a1154c8e79f1a820798c02d26c7c3fa`; retrieval score: 1.032865335131535.

Word count: 132.

```text
in a way that reduces potentially discriminatory predictions. According to the authors, it is possible to perceive the potential use of the method as a means of reducing bias in the use of ML algorithms.

In BIBREF3 , the authors propose a method to hardly reduce bias in English word embeddings collected from Google News. Using word2vec, they performed a geometric analysis of gender direction of the bias contained in the data. Using this property with the generation of gender-neutral analogies, a methodology was provided for modifying an embedding to remove gender stereotypes. Some metrics were defined to quantify both direct and indirect gender biases in embeddings and to develop algorithms to reduce bias in some embedding. Hence, the authors show that embeddings can be used in applications without amplifying gender bias.
```

Evidence coverage: none.

#### Rank 5: qasper-passage-v1-f8375e20467e5bb181106824edafd7fbd24a405d10306780c038140a94d40a69

Passage ID: `qasper-passage-v1-f8375e20467e5bb181106824edafd7fbd24a405d10306780c038140a94d40a69`; retrieval score: 0.8584058104027673.

Word count: 110.

```text
bias associated with professions in word embeddings. So therefore into the evaluation of the accuracy of the associations generated, aiming at achieving results as good as possible without prejudicing the evaluation metrics.

Algorithm SECREF4 describes the method performed during the evaluation of the gender bias presence. In this method we try to evaluate the accuracy of the analogies generated through the model, that is, to verify the cases of association matching generated between the words.

[!htb] Model Evaluation [1]

w2v_evaluate INLINEFORM0 open_model( INLINEFORM1 ) count = 0 INLINEFORM2 in INLINEFORM3 read list of tuples x = model.most_similar(positive=[`ela', male], negative=[`ele'])

x = female count += 1 accuracy = count/size(profession_pairs) return accuracy
```

Evidence coverage: none.

### Evaluation results

Evidence Hit@5: true

Complete evidence rate@5: true

Total retrieved words: 958.

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
