# Readability Review

## Source sample: 1

### Source text

Paper: 1605.04655; section: 12; paragraphs: [3]; character span: 0:389 (within sampled paragraph).

Original section context:

```text
We have established a general Hypothesis Evaluation task with three datasets of various properties, and shown that neural models can exhibit strong performance (with less hand-crafting effort than non-neural classifiers). We propose an evidence weighing model that is never harmful and improves performance on some tasks. We also demonstrate that simple models can outperform or closely match performance of complex architectures; all the models we consider are task-independent and were successfully used in different contexts than Hypothesis Evaluation BIBREF6 . Our results empirically show that a basic RNN text comprehension model well trained on a large dataset (even if the task is unrelated and vocabulary characteristics are very different) outperforms or matches more complex architectures trained only on the dataset of the task at hand.

Finally, on the MCTest dataset, our best proposed model is better or statistically indistinguishable from the best neural model reported so far BIBREF17 , even though it has a simpler architecture and only a naive attention mechanism.

We would like to draw several recommendations for future research from our findings: (A) encourage usage of basic neural architectures as evaluation baselines; (B) suggest that future research includes models pretrained on large data as baselines; (C) validate complex architectures on tasks with large datasets if they cannot beat baselines on small datasets; and (D) for randomized machine comprehension models (e.g. neural networks with random weight initialization, batch shuffling or probabilistic dropout), report expected test set performance based on multiple independent training runs.

As a general advice for solving complex tasks with small datasets, besides the point (B) above our analysis suggests convolutional networks as the best models regarding the tendency to overfit, unless semantic composionality plays a crucial role in the task; in this scenario, simple averaging-based models are a great start as well. Preinitializing a model also helps against overfitting.

We release our implementation of the Argus task, evidence integration models and processing of all the evaluated datasets as open source.

We believe the next step towards machine comprehension NLP models (based on deep learning but capable of dealing with real-world, large-vocabulary data) will involve research into a better way to deal with entities without available embeddings. When distinguishing specific entities, simple word-level attention mechanisms will not do. A promising approach could extend the flexibility of the final sentence representation, moving from attention mechanism to a memory mechanism by allowing the network to remember a set of “facts” derived from each sentence; related work has been done for example on end-to-end differentiable shift-reduce parsers with LSTM as stack cells BIBREF28 .
```

### Chunks (ID and text)

Passage ID: `qasper-passage-v1-d8b6513e84927404f6990557ffde62af918ac4a7754b4b872bbc5a6136dd3089`

```text
We have established a general Hypothesis Evaluation task with three datasets of various properties, and shown that neural models can exhibit strong performance (with less hand-crafting effort than non-neural classifiers). We propose an evidence weighing model that is never harmful and improves performance on some tasks. We also demonstrate that simple models can outperform or closely match performance of complex architectures; all the models we consider are task-independent and were successfully used in different contexts than Hypothesis Evaluation BIBREF6 . Our results empirically show that a basic RNN text comprehension model well trained on a large dataset (even if the task is unrelated and vocabulary characteristics are very different) outperforms or matches more complex architectures trained only on the dataset of the task at hand.

Finally, on the MCTest dataset, our best proposed model is better or statistically indistinguishable from the best neural model reported so far BIBREF17 , even though it has a simpler architecture and only a naive attention mechanism.

We would like to draw several recommendations for future research from our findings: (A) encourage usage of basic neural architectures as evaluation baselines; (B) suggest that future research includes models pretrained on large data as baselines; (C) validate complex architectures on tasks with large datasets if they cannot beat baselines on small datasets; and (D) for randomized machine comprehension models (e.g. neural networks with random weight initialization, batch shuffling or probabilistic dropout), report expected test set performance based on multiple independent training runs.

As a general advice for
```

Passage ID: `qasper-passage-v1-45e83c12b6e7975080cccfc2a30fae23169fd9d638a28b6b26ad0f66979aab2f`

```text
beat baselines on small datasets; and (D) for randomized machine comprehension models (e.g. neural networks with random weight initialization, batch shuffling or probabilistic dropout), report expected test set performance based on multiple independent training runs.

As a general advice for solving complex tasks with small datasets, besides the point (B) above our analysis suggests convolutional networks as the best models regarding the tendency to overfit, unless semantic composionality plays a crucial role in the task; in this scenario, simple averaging-based models are a great start as well. Preinitializing a model also helps against overfitting.

We release our implementation of the Argus task, evidence integration models and processing of all the evaluated datasets as open source.

We believe the next step towards machine comprehension NLP models (based on deep learning but capable of dealing with real-world, large-vocabulary data) will involve research into a better way to deal with entities without available embeddings. When distinguishing specific entities, simple word-level attention mechanisms will not do. A promising approach could extend the flexibility of the final sentence representation, moving from attention mechanism to a memory mechanism by allowing the network to remember a set of “facts” derived from each sentence; related work has been done for example on end-to-end differentiable shift-reduce parsers with LSTM as stack cells BIBREF28 .
```

### Evaluation results

| Passage ID | Result | Reason |
| --- | --- | --- |
| `qasper-passage-v1-d8b6513e84927404f6990557ffde62af918ac4a7754b4b872bbc5a6136dd3089` | pending | |
| `qasper-passage-v1-45e83c12b6e7975080cccfc2a30fae23169fd9d638a28b6b26ad0f66979aab2f` | pending | |

## Source sample: 2

### Source text

Paper: 1805.12032; section: 0; paragraphs: [1]; character span: 0:309 (within sampled paragraph).

Original section context:

```text
As the reliance on social media as a source of news increases and the reliability of sources is increasingly debated, it is important to understand how users react to various sources of news. Most studies that investigate misinformation spread in social media focus on individual events and the role of the network structure in the spread BIBREF0 , BIBREF1 , BIBREF2 or detection of false information BIBREF3 . These studies have found that the size and shape of misinformation cascades within a social network depends heavily on the initial reactions of the users. Other work has focused on the language of misinformation in social media BIBREF4 , BIBREF5 , BIBREF6 , BIBREF7 , BIBREF8 , BIBREF9 to detect types of deceptive news.

As an alternative to studying newsworthy events one at a time BIBREF10 , the current work applies linguistically-infused models to predict user reactions to deceptive and trusted news sources. Our analysis reveals differences in reaction types and speed across two social media platforms — Twitter and Reddit.

The first metric we report is the reaction type. Recent studies have found that 59% of bitly-URLs on Twitter are shared without ever being read BIBREF11 , and 73% of Reddit posts were voted on without reading the linked article BIBREF12 . Instead, users tend to rely on the commentary added to retweets or the comments section of Reddit-posts for information on the content and its credibility. Faced with this reality, we ask: what kind of reactions do users find when they browse sources of varying credibility? Discourse acts, or speech acts, can be used to identify the use of language within a conversation, e.g., agreement, question, or answer. Recent work by Zhang et al. zhang2017characterizing classified Reddit comments by their primary discourse act (e.g., question, agreement, humor), and further analyzed patterns from these discussions.

The second metric we report is reaction speed. A study by Jin et al. jin2013epidemiological found that trusted news stories spread faster than misinformation or rumor; Zeng et al. zeng2016rumors found that tweets which deny rumors had shorter delays than tweets of support. Our second goal is to determine if these trends are maintained for various types of news sources on Twitter and Reddit.

Hence, the contributions of this work are two-fold: (1) we develop a linguistically-infused neural network model to classify reactions in social media posts, and (2) we apply our model to label 10.8M Twitter posts and 6.2M Reddit comments in order to evaluate the speed and type of user reactions to various news sources.
```

### Chunks (ID and text)

Passage ID: `qasper-passage-v1-13f9f4fb269d25edfb97401f43a36a57cc70756d5691c9ad3905c68988187501`

```text
As the reliance on social media as a source of news increases and the reliability of sources is increasingly debated, it is important to understand how users react to various sources of news. Most studies that investigate misinformation spread in social media focus on individual events and the role of the network structure in the spread BIBREF0 , BIBREF1 , BIBREF2 or detection of false information BIBREF3 . These studies have found that the size and shape of misinformation cascades within a social network depends heavily on the initial reactions of the users. Other work has focused on the language of misinformation in social media BIBREF4 , BIBREF5 , BIBREF6 , BIBREF7 , BIBREF8 , BIBREF9 to detect types of deceptive news.

As an alternative to studying newsworthy events one at a time BIBREF10 , the current work applies linguistically-infused models to predict user reactions to deceptive and trusted news sources. Our analysis reveals differences in reaction types and speed across two social media platforms — Twitter and Reddit.

The first metric we report is the reaction type. Recent studies have found that 59% of bitly-URLs on Twitter are shared without ever being read BIBREF11 , and 73% of Reddit posts were voted on without reading the linked article BIBREF12 . Instead, users tend to rely on the commentary added to retweets or the comments section of Reddit-posts for information on the content and its credibility. Faced with this reality, we ask: what kind of reactions do users find when
```

### Evaluation results

| Passage ID | Result | Reason |
| --- | --- | --- |
| `qasper-passage-v1-13f9f4fb269d25edfb97401f43a36a57cc70756d5691c9ad3905c68988187501` | pending | |
