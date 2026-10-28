# Passage relevance annotation

Annotator: 

Judge whether the passage provides information that helps answer the question, including useful partial evidence. Topic overlap alone is not sufficient. Judge only the supplied question and passage.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Do not change record numbers, questions or passages. Work independently without consulting another annotator or reference answers.

## Record 0301

Paper: What Does My QA Model Know? Devising Controlled Probes using Expert Knowledge

### Question

> After how many hops does accuracy decrease?

### Passage

> Table TABREF32 shows cluster-level accuracies for the different WordNetQA probes. As with performance across the different inference/distractor categories, these results are mixed. For some probes, such as definitions, our best models appear to be rather robust; e.g., our RoBERTa model has a cluster accuracy of $75\%$, meaning that it can answer all questions perfectly for 75% of the target concepts and that errors are concentrated on a small minority (25%) of concepts. On synonymy and hypernymy, both BERT and RoBERTa appear robust on the majority of concepts, showing that errors are similarly concentrated. In contrast, our best model on hyponymy has an accuracy of 36%, meaning that its errors are spread across many concepts, thus suggesting less robustness.
> 
> Table TABREF30 shows a selection of semantic clusters involving ISA reasoning, as well as the model performance over different answers (shown symbolically) and perturbations. For example, in the the second case, the cluster is based around the concept/synset oppose.v.06 and involves 4 inferences and a total 24 questions (i.e., inferences with perturbations). Our weakest model, ESIM, answers only 5 out of 24 questions correctly, whereas RoBERTa gets 21/24. In the other cases, RoBERTa gets all clusters correct, whereas BERT and ESIM get none of them correct.
> 
> We emphasize that these results only provide a crude look into model consistency and robustness. Recalling again the details in Table TABREF12, probes differ in terms of average size of clusters. Hyponymy, in virtue of having many more questions per cluster, might simply be a much more difficult dataset. In addition, such a strict evaluation does not take into account potential errors inside of clusters, which is an important issue that we discuss in the next section. We leave addressing such issues and coming up with more insightful cluster-based metrics for future work.

### Relevance

Label: 

## Record 0302

Paper: What Does My QA Model Know? Devising Controlled Probes using Expert Knowledge

### Question

> After how many hops does accuracy decrease?

### Passage

> Science models that use non-transformer based encoders, such as the ESIM model with GloVe and ELMO, perform poorly across all probes, in many cases scoring near random chance, showing limits to how well they generalize from science to other tasks even with pre-trained GloVe and ELMO embeddings. In sharp contrast, the transformer models have mixed results, the most striking result being the RoBERTa models on the definitions and synonymy probes (achieving a test accuracy of 77% and 61%, respectively), which outperform several of the task-specific LSTM models trained directly on the probes. At first glance, this suggests that RoBERTa, which generally far outpaces even BERT across most probes, has high competence of definitions and synonyms even without explicit training on our new tasks.
> 
> Given the controlled nature of our probes, we can get a more detailed view of how well the science models are performing across different reasoning and distractor types, as shown in the first column of Figure FIGREF28 for ESIM and RoBERTa. The ESIM science model without training has uniformly poor performance across all categories, whereas the performance of RoBERTa is more varied. Across all datasets and number of hops (i.e., the rows in the heat maps), model performance for RoBERTa is consistently highest among examples with random distractors (i.e., the first column), and lowest in cases involving distractors that are closest in WordNet space (e.g., sister and ISA, or up/down, distractors of distance $k^{\prime }=1$). This is not surprising, given that, in the first case, random distractors are likely to be the easiest category (and the opposite for distractors close in space), but suggests that RoBERTa might only be getting the easiest cases correct.
> 
> Model performance also clearly degrades for hypernymy and hyponymy across all models as the number of hops $k$ increases (see red dashed boxes). For example, problems that involve hyponym reasoning with sister distractors of distance $k^{\prime }=1$ (i.e., the second column) degrades from 47% to 15% when the number of hops $k$ increases from 1 to 4. This general tendency persists even after additional fine-tuning, as we discuss next, and gives evidence that models are limited in their capacity for certain types of multi-hop inferences.
> 
> As discussed by

### Relevance

Label: 

## Record 0303

Paper: What Does My QA Model Know? Devising Controlled Probes using Expert Knowledge

### Question

> After how many hops does accuracy decrease?

### Passage

> The DictionaryQA dataset is created from the GCIDE dictionary, which is a comprehensive open-source English dictionary built largely from the Webster's Revised Unabridged Dictionary BIBREF38. Each entry consists of a word, its part-of-speech, its definition, and an optional example sentence (see Table TABREF14). Overall, 33k entries (out of a total of 155k) contain example sentences/usages. As with the WordNet probes, we focus on this subset so as to contextualize each word being probed. In contrast to WordNet, GCIDE does not have ISA relations or explicit synsets, so we take each unique entry to be a distinct sense. We then use the dictionary entries to create a probe that centers around word-sense disambiguation, as described below.

### Relevance

Label: 

## Record 0304

Paper: What Does My QA Model Know? Devising Controlled Probes using Expert Knowledge

### Question

> After how many hops does accuracy decrease?

### Passage

> An example of how distractors are generated is shown in Figure FIGREF6, which relies on similar principles as above. For each concept $c$, we choose 4 distractor answers that are close in the WordNet semantic space. For example, when constructing hypernymy tests for $c$ from the set hops$(c,\uparrow )$, we build distractors by drawing from $\textsc {hops}(c,\downarrow )$ (and vice versa), as well as from the $\ell $-deep sister family of $c$, defined as follows. The 1-deep sister family is simply $c$'s siblings or sisters, i.e., the other children $\tilde{c} \ne c$ of the parent node $c^{\prime }$ of $c$. For $\ell > 1$, the $\ell $-deep sister family also includes all descendants of each $\tilde{c}$ up to $\ell -1$ levels deep, denoted $\textsc {hops}_{\ell -1}(\tilde{c},\downarrow )$. Formally:
> 
> For definitions and synonyms we build distractors from all of these sets (with a similar restriction on the depth of sister distractors as noted above). In doing this, we can systematically investigate model performance on a wide range of distractor sets.

### Relevance

Label: 

## Record 0305

Paper: What Does My QA Model Know? Devising Controlled Probes using Expert Knowledge

### Question

> After how many hops does accuracy decrease?

### Passage

> to recognize certain types of knowledge captured in our probes—even without additional fine-tuning. Such models can even outperform strong task-specific models trained directly on our probing tasks (e.g., on definitions, our best model achieves 77% test accuracy without specialized training, as opposed to 51% for a task-specific LSTM-based model). We also show that the same models can be effectively re-fine-tuned on small samples (even 100 examples) of probe data, and that high performance on the probes tends to correlate with a smaller drop in the model's performance on the original QA task.
> 
> Our comprehensive assessment reveals several interesting nuances to the overall positive trend. For example, the performance of even the best QA models degrades substantially on our hyponym probes (by 8-15%) when going from 1-hop links to 2-hops. Further, the accuracy of even our best models on the WordNetQA probe drops by 14-44% under our cluster-based analysis, which assesses whether a model knows several facts about each individual concept, rather than just being good at answering isolated questions. State-of-the-art QA models thus have much room to improve even in some fundamental building blocks, namely definitions and taxonomic hierarchies, of more complex forms of reasoning.

### Relevance

Label: 

## Record 0306

Paper: Improving Spoken Language Understanding By Exploiting ASR N-best Hypotheses

### Question

> Which ASR system(s) is used in this work?

### Passage

> The preliminary architecture is shown in Fig. FIGREF4. For a given transcribed utterance, it is firstly encoded with Byte Pair Encoding (BPE) BIBREF14, a compression algorithm splitting words to fundamental subword units (pairs of bytes or BPs) and reducing the embedded vocabulary size. Then we use a BiLSTM BIBREF15 encoder and the output state of the BiLSTM is regarded as a vector representation for this utterance. Finally, a fully connected Feed-forward Neural Network (FNN) followed by a softmax layer, labeled as a multilayer perceptron (MLP) module, is used to perform the domain/intent classification task based on the vector.
> 
> For convenience, we simplify the whole process in Fig.FIGREF4 as a mapping $BM$ (Baseline Mapping) from the input utterance $S$ to an estimated tag's probability $p(\tilde{t})$, where $p(\tilde{t}) \leftarrow BM(S)$. The $Baseline$ is trained on transcription and evaluated on ASR 1st best hypothesis ($S=\text{ASR}\ 1^{st}\ \text{best})$. The $Oracle$ is trained on transcription and evaluated on transcription ($S = \text{Transcription}$). We name it Oracle simply because we assume that hypotheses are noisy versions of transcription.

### Relevance

Label: 

## Record 0307

Paper: Improving Spoken Language Understanding By Exploiting ASR N-best Hypotheses

### Question

> Which ASR system(s) is used in this work?

### Passage

> have observed the success of reranking the $n$-best hypotheses BIBREF1, BIBREF3, BIBREF4, BIBREF5, BIBREF6, BIBREF7, BIBREF8, BIBREF9, BIBREF10 before feeding the best interpretation to the NLU module. These approaches propose the reranking framework by involving morphological, lexical or syntactic features BIBREF8, BIBREF9, BIBREF10, speech recognition features like confidence score BIBREF1, BIBREF4, and other features like number of tokens, rank position BIBREF1. They are effective to select the best from the hypotheses list and reduce the word error rate (WER) BIBREF11 of speech recognition.
> 
> Those reranking models could benefit the first two cases in Table TABREF2 when there is an utterance matching with transcription. However, in other cases like the third row, it is hard to integrate the fragmented information in multiple hypotheses.
> 
> This paper proposes various methods integrating $n$-best hypotheses to tackle the problem. To the best of our knowledge, this is the first study that attempts to collectively exploit the $n$-best speech interpretations in the SLU system. This paper serves as the basis of our $n$-best-hypotheses-based SLU system, focusing on the methods of integration for the hypotheses. Since further improvements of the integration framework require considerable setup and descriptions, where jointly optimized tasks (e.g. transcription reconstruction) trained with multiple ways (multitask BIBREF12, multistage learning BIBREF13) and more features (confidence score, rank position, etc.) are involved, we leave those to a subsequent article.
> 
> This paper is organized as follows. Section SECREF2 introduces the Baseline, Oracle and Direct models. Section SECREF3 describes proposed ways to integrate $n$-best hypotheses during training. The experimental setup and results are described in Section SECREF4. Section SECREF5 contains conclusions and future work.

### Relevance

Label: 

## Record 0308

Paper: Improving Spoken Language Understanding By Exploiting ASR N-best Hypotheses

### Question

> Which ASR system(s) is used in this work?

### Passage

> This paper improves the SLU system robustness to ASR errors by integrating $n$-best hypotheses in different ways, e.g. the aggregation of predictions from hypotheses or the concatenation of hypothesis text or embedding. We can achieve significant classification accuracy improvements over production-quality baselines on domain and intent classifications, 14% to 25% relative gains. The improvement is more significant for a subset of testing data where ASR first best is different from transcription. We also observe that with more hypotheses utilized, the performance can be further improved. In the future, we aim to employ additional features (e.g. confidence scores for hypotheses or tokens) to integrate $n$-bests more efficiently, where we can train a function $f$ to obtain a weight for each hypothesis embedding before pooling. Another direction is using deep learning framework to embed the word lattice BIBREF16 or confusion network BIBREF17, BIBREF18, which can provide a compact representation of multiple hypotheses and more information like times, in the SLU system.

### Relevance

Label: 

## Record 0309

Paper: Improving Spoken Language Understanding By Exploiting ASR N-best Hypotheses

### Question

> Which ASR system(s) is used in this work?

### Passage

> Currently, voice-controlled smart devices are widely used in multiple areas to fulfill various tasks, e.g. playing music, acquiring weather information and booking tickets. The SLU system employs several modules to enable the understanding of the semantics of the input speeches. When there is an incoming speech, the ASR module picks it up and attempts to transcribe the speech. An ASR model could generate multiple interpretations for most speeches, which can be ranked by their associated confidence scores. Among the $n$-best hypotheses, the top-1 hypothesis is usually transformed to the NLU module for downstream tasks such as domain classification, intent classification and named entity recognition (slot tagging). Multi-domain NLU modules are usually designed hierarchically BIBREF0. For one incoming utterance, NLU modules will firstly classify the utterance as one of many possible domains and the further analysis on intent classification and slot tagging will be domain-specific.
> 
> In spite of impressive development on the current SLU pipeline, the interpretation of speech could still contain errors. Sometimes the top-1 recognition hypothesis of ASR module is ungrammatical or implausible and far from the ground-truth transcription BIBREF1, BIBREF2. Among those cases, we find one interpretation exact matching with or more similar to transcription can be included in the remaining hypotheses ($2^{nd}- n^{th}$).
> 
> To illustrate the value of the $2^{nd}- n^{th}$ hypotheses, we count the frequency of exact matching and more similar (smaller edit distance compared to the 1st hypothesis) to transcription for different positions of the $n$-best hypotheses list. Table TABREF1 exhibits the results. For the explored dataset, we only collect the top 5 interpretations for each utterance ($n = 5$). Notably, when the correct recognition exists among the 5 best hypotheses, 50% of the time (sum of the first row's percentages) it occurs among the $2^{nd}-5^{th}$ positions. Moreover, as shown by the second row in Table TABREF1, compared to the top recognition hypothesis, the other hypotheses can sometimes be more similar to the transcription.
> 
> Over the past few years, we have observed the success of reranking the $n$-best hypotheses BIBREF1, BIBREF3, BIBREF4, BIBREF5, BIBREF6, BIBREF7, BIBREF8, BIBREF9, BIBREF10 before feeding the best interpretation to the NLU module. These approaches propose the reranking framework by involving morphological, lexical or syntactic features

### Relevance

Label: 

## Record 0310

Paper: Improving Spoken Language Understanding By Exploiting ASR N-best Hypotheses

### Question

> Which ASR system(s) is used in this work?

### Passage

> To further detect the reason for improvements, we split the test set into two parts based on whether ASR first best agrees with transcription and evaluate separately. Comparing Table TABREF26 and Table TABREF27, obviously the benefits of using multiple hypotheses are mainly gained when ASR 1st best disagrees with the transcription. When ASR 1st best agrees with transcription, the proposed integration models can also keep the performance. Under that condition, we can still improve a little (3.56%) because, by introducing multiple ASR hypotheses, we could have more information and when the transcription/ASR 1st best does not appear in the training set's transcriptions, its $n$-bests list may have similar hypotheses included in the training set's $n$-bests. Then, our integration model trained on $n$-best hypotheses as well has clue to predict. The series of comparisons reveal that our approaches integrating the hypotheses are robust to the ASR errors and whenever the ASR model makes mistakes, we can outperform more significantly.

### Relevance

Label: 

## Record 0311

Paper: IAM at CLEF eHealth 2018: Concept Annotation and Coding in French Death Certificates

### Question

> How long is the dataset?

### Passage

> The present study is part of the Drugs Systematized Assessment in real-liFe Environment (DRUGS-SAFE) research platform that is funded by the French Medicines Agency (Agence Nationale de Sécurité du Médicament et des Produits de Santé, ANSM). This platform aims at providing an integrated system allowing the concomitant monitoring of drug use and safety in France. The funder had no role in the design and conduct of the studies ; collection, management, analysis, and interpretation of the data ; preparation, review, or approval of the manuscript ; and the decision to submit the manuscript for publication. This publication represents the views of the authors and does not necessarily represent the opinion of the French Medicines Agency.
> 
> english

### Relevance

Label: 

## Record 0312

Paper: IAM at CLEF eHealth 2018: Concept Annotation and Coding in French Death Certificates

### Question

> How long is the dataset?

### Passage

> The goal of our algorithm was to recognize one or many dictionary entries in a raw text. An example is given in Figure FIGREF8 . For each raw text entry, the same normalization steps described above were performed first. The raw text was then tokenized. For each token, the algorithm looked for an available dictionary token depending on where it currently was in the tree. For example, the token "cardiaque" was possible after the token "insuffisance" but was not available at the root of the tree.
> 
> For each token, the algorithm used three matching techniques : perfect match, abbreviation match and Levenshtein match. The abbreviation match technique used a dictionary of abbreviations. We manually added nine frequent abbreviations after looking at some examples. The Levenshtein matching technique used the Levenshtein distance. It corresponds to the minimum number of single-character edits (insertions, deletions or substitutions) required to change one token into the other. The Lucene™implementation of the Levenshtein distance was used.
> 
> In Figure FIGREF8 , the algorithm used these three techniques to match the tokens "ins", "cardiaqu", "aigue" to the dictionary term "insuffisance cardiaque aigue" whose ICD-10 code is I509. As the following token "detresse" was not a dictionary entry at this depth, the algorithm saved the previous and longest recognized term and restarted from the root of the tree. At this new level, "detresse" was detected but as no term was associated with this token alone, no ICD-10 code was saved. Finally, only one term was recognized in this example.
> 
> Besides unigrams, bigrams were also indexed in Lucene™to resolve composed words. For example, "meningoencephalite" matched the dictionary entry "meningoencephalite" by a perfect match and "meningo encephalite" thanks to the Levensthein match (one deletion). Therefore, the algorithm entered two different paths in the tree (Figure FIGREF10 ). By combining these different matching methods for each token, the algorithm was able to detect multiple lexical variants. The program was implemented in Java and the source code is on Github.

### Relevance

Label: 

## Record 0313

Paper: IAM at CLEF eHealth 2018: Concept Annotation and Coding in French Death Certificates

### Question

> How long is the dataset?

### Passage

> In the following subsections, we describe the corpora, the terminology used, the steps of pre-processing and the matching algorithm.

### Relevance

Label: 

## Record 0314

Paper: IAM at CLEF eHealth 2018: Concept Annotation and Coding in French Death Certificates

### Question

> How long is the dataset?

### Passage

> We submitted two runs on the CépiDC test set, one used all the terms entered by human coders in the training set only (run 2), the other (run 1) added the 2015 ICD-10 dictionary provided by the task organizers to the set the terms of run 1. We obtained our best precision (0.794) and recall (0.779) with run 2.
> 
> Table TABREF11 shows the performance of our system with median and average scores of all participants in this task.

### Relevance

Label: 

## Record 0315

Paper: IAM at CLEF eHealth 2018: Concept Annotation and Coding in French Death Certificates

### Question

> How long is the dataset?

### Passage

> We constructed two dictionaries based on ICD-10. In practice, we selected all the terms in the "Standard Text" column of the training set to build the first one which was used in the second run. In the first run, we added to this previous set of terms the 2015 ICD-10 dictionary provided by the task organizers. This dictionary contained terms that were not present in the training corpus. When a term was associated with multiple ICD-10 codes in our dictionary, we kept the most frequent one (Table TABREF4 ).
> 
> The first dictionary contained 42439 terms and 3,539 ICD-10 codes (run2) and the second one 148448 terms and 6,392 ICD-10 codes (run1).
> 
> Metadata on death causes were not used (age, gender, location of death).

### Relevance

Label: 

## Record 0316

Paper: Bridging the Gap for Tokenizer-Free Language Models

### Question

> How many characters are accepted as input of the language model?

### Passage

> Language models (LMs) assign a probability distribution over a sequence $x_{0:t}$ by factoring out the joint probability from left to right as follows
> 
> Instead of reading in the tokenized input text, our model reads raw utf-8 bytes. For English text in the ASCII range, this is equivalent to processing characters as individual tokens. Non-ASCII characters (e.g. accented characters, or non-Latin scripts) are typically two or three utf-8 bytes. We use a standard “transformer decoder” (a stack of transformer layers with a causal attention mask) to process the sequence $x_{0:i-1}$ and predict the following byte $x_i$. The model's prediction is an estimate of the probability distribution over all possible 256 byte values. Our input byte embedding matrix has dimensionality 256. Our byte-level transformer model has 40 standard transformer layers with hidden size 1024, filter size 8192, and 16 heads. The model has around 836M parameters, of which only 66K are byte embeddings.

### Relevance

Label: 

## Record 0317

Paper: Bridging the Gap for Tokenizer-Free Language Models

### Question

> How many characters are accepted as input of the language model?

### Passage

> We show that a tokenizer-free language model with sufficient capacity can achieve results that are competitive with word-based LMs. Our model reads raw byte-level input without the use of any text preprocessing. As such, the model has no direct access to word boundary information. Finally, we show that our model's intermediate representations capture word-level semantic similarity and relatedness across layers.

### Relevance

Label: 

## Record 0318

Paper: Bridging the Gap for Tokenizer-Free Language Models

### Question

> How many characters are accepted as input of the language model?

### Passage

> used for their ability to produce pretrained representations that will be fine-tuned for a downstream task BIBREF11, BIBREF12, BIBREF13, BIBREF14. Since word-based LMs use closed vocabulary and sub-word models adopt a segmentation that targets the pretraining corpus, there is little space to adapt the vocabulary or optimize the segmentation to fit the final task data distribution.
> 
> The rest of this paper is organized as follows. In Section SECREF2, we describe our model architecture, which is a vanilla deep transformer byte-level LM. Section SECREF3 describes the lm1b dataset and our evaluation methodology. Section SECREF4 presents our results and how our model compares to the previous work. In Section SECREF5 we analyze the representations learned by the network at different depths using word-similarity benchmarks. For this analysis to be feasible we propose a strategy to extract word representations from a character model.
> 
> To summarize our contributions:
> 
> We develop a competitive tokenizer-free language model on a large scalable dataset.
> 
> We probe the performance of our model's learned intermediate representations on word similarity tasks.

### Relevance

Label: 

## Record 0319

Paper: Bridging the Gap for Tokenizer-Free Language Models

### Question

> How many characters are accepted as input of the language model?

### Passage

> In this section, we test our model's ability to produce meaningful word-level representations. We investigate this by feeding the model single words, and evaluating its intermediate activations on word similarity tasks.
> 
> Since our model is trained to predict each individual character, activations within a word only have partial information about that word. To get a word representation, we append an empty space character at the end of the input word. The activation at the space position from the transformer's feed-forward layer takes all characters into account, given the causal attention. To predict what follows the space, the model must have a good understanding of the preceding word, so this activation can be used as a proxy for a word representation.
> 
> To evaluate our extracted word representations, we use the word similarity tasks described in Swivel BIBREF16. Following their evaluation methodology, we score word pairs using cosine similarity, and then measure the correlation with human ratings using Spearman's $\rho $.
> 
> We do not expect these results to be competitive, given that our model is never trained to represent words. Moreover, the Swivel model is trained on a combination of Wikipedia and the Gigaword5 corpus BIBREF17 which is composed of 3.3 billion lowercased words with discarded punctuation. They discard out-of-vocabulary words for evaluation, while we use all word pairs in the benchmark. Nevertheless, this evaluation is valuable for comparing the relative quality of representation across different layers.
> 
> Figure FIGREF12 shows Spearman's $\rho $ across different layers of the model. We observe two main phases of performance. In the first phrase (layers 1-10), all task metrics improve with depth. In the second phase (layers 11-40), performance either plateaus or degrades slightly with depth. We suspect that the earlier layers learn general-purpose features which are linguistically relevant, while the final layers fine-tune specifically to the task of next character prediction. Interestingly, the Rare Word and SimLex999 datasets do not follow this paradigm. Their performance drops between layers 4-6, but picks up again and improves with depth (layers 6-40). We hypothesize that the model may be storing words at different depths according to their frequency. It would be interesting to investigate to what degree the improved performance of deeper LMs

### Relevance

Label: 

## Record 0320

Paper: Bridging the Gap for Tokenizer-Free Language Models

### Question

> How many characters are accepted as input of the language model?

### Passage

> There has been a recent surge of improvements in language modeling, powered by the introduction of the transformer architecture BIBREF0. These gains stem from the ability of the transformer self-attention mechanism to better model long context (as compared to RNN networks), spanning hundreds of characters BIBREF1 or words BIBREF2, BIBREF3. These approaches consider language modeling as a classification problem with the aim of predicting the next token given a fixed-size preceding context. To support variable-length context, BIBREF4 adds recurrence to a transformer model, improving the state-of-the-art further.
> 
> Current word-based language models (LMs) depend on a series of preprocessing steps that include lowercasing, tokenization, normalization, and out-of-vocabulary handling. This preprocessing stage is language dependent and can add significant complexity to real applications. As such, it is appealing to shift to more general LMs that process raw text at the character level. Processing language at the character level allows us to model morphological variants of a word, assign reasonable likelihood to out-of-vocabulary words, and learn subword-level language abstractions. This open vocabulary modeling is quite important for languages with complex morphology such as Arabic, Turkish, or Finnish BIBREF5, BIBREF6, BIBREF7.
> 
> While character- and word-based LMs have both improved in their performance over time, purely character-based LMs have continued to lag in performance compared to models that leverage a tokenizer. BIBREF1 report inferior performance from character-level modeling on a large scale word-level benchmark, lm1b BIBREF8. Similarly, BIBREF3 observe that a character-level LM is harder to train to competitive performance on their huge WebText corpus, as compared with subword segmentation using byte pair encoding (BPE) BIBREF9, BIBREF10.
> 
> Sub-word tokenization approaches like BPE represent a middle ground for text segmentation. On one hand, they can help with better modeling open vocabulary. On the other hand, they still depend on a tokenizer, adding complexity to the final system. Moreover, the preprocessing stage is not jointly optimized with learning the task objective. This last point is especially relevant given that LMs are increasingly used for their ability to produce pretrained representations that will be fine-tuned for a downstream task BIBREF11, BIBREF12, BIBREF13, BIBREF14. Since word-based LMs use closed vocabulary and sub-word models adopt a segmentation that targets the pretraining corpus, there is little

### Relevance

Label: 

## Record 0321

Paper: From English To Foreign Languages: Transferring Pre-trained Language Models

### Question

> What metrics are used for evaluation?

### Passage

> We create a bilingual LM by plugging foreign language specific parameters to the pre-trained English LM (Figure FIGREF7). The new model has two separate embedding layers and output layers, one for English and one for foreign language. The encoder layer in between is shared. We then fine-tune this model using English and foreign monolingual data. Here, we keep tuning the model on English to ensure that it does not forget what it has learned in English and that we can use the resulting model for zero-shot transfer (§SECREF3). In this step, the encoder parameters are also updated so that in can learn syntactic aspects (i.e., word order, morphological agreement) of the target languages.

### Relevance

Label: 

## Record 0322

Paper: From English To Foreign Languages: Transferring Pre-trained Language Models

### Question

> What metrics are used for evaluation?

### Passage

> All the RAMEN models are built from English and tuned on English for zero-shot cross-lingual tasks. It is reasonable to expect RAMENs do well in those tasks as we have shown in our experiments. But are they also a good feature extractor for supervised tasks? We offer a partial answer to this question by evaluating our model for supervised dependency parsing on UD datasets.
> 
> We used train/dev/test splits provided in UD to train and evaluate our RAMEN-based parser. Table TABREF38 summarizes the results (LAS) of our supervised parser. For a fair comparison, we choose mBERT as the baseline and all the RAMEN models are initialized from aligned fastText vectors. With the same architecture of 12 Transformer layers, RAMEN$_{\textsc {base}}$+BERT performs competitive to mBERT and outshines mBERT by +1.2 points for Vietnamese. The best LAS results are obtained by RAMEN$_{\textsc {large}}$+RoBERTa with 24 Transformer layers. Overall, our results indicate the potential of using contextual representations from RAMEN for supervised tasks.

### Relevance

Label: 

## Record 0323

Paper: From English To Foreign Languages: Transferring Pre-trained Language Models

### Question

> What metrics are used for evaluation?

### Passage

> In all the experiments, we tune RAMEN$_{\textsc {base}}$ for 175,000 updates and RAMEN$_{\textsc {large}}$ for 275,000 updates where the first 25,000 updates are for language specific parameters. The sequence length is set to 256. The mini-batch size are 64 and 24 when tuning language specific parameters using RAMEN$_{\textsc {base}}$ and RAMEN$_{\textsc {large}}$ respectively. For tuning bilingual LMs, we use a mini-batch size of 64 for RAMEN$_{\textsc {base}}$ and 24 for RAMEN$_{\textsc {large}}$ where half of the batch are English sequences and the other half are foreign sequences. This strategy of balancing mini-batch has been used in multilingual neural machine translation BIBREF23, BIBREF24.
> 
> We optimize RAMEN$_{\textsc {base}}$ using Lookahead optimizer BIBREF25 wrapped around Adam with the learning rate of $10^{-4}$, the number of fast weight updates $k=5$, and interpolation parameter $\alpha =0.5$. We choose Lookahead optimizer because it has been shown to be robust to the initial parameters of the based optimizer (Adam). For Adam optimizer, we linearly increase the learning rate from $10^{-7}$ to $10^{-4}$ in the first 4000 updates and then follow an inverse square root decay. All RAMEN$_{\textsc {large}}$ models are optimized with Adam due to memory limit.
> 
> When fine-tuning RAMEN on XNLI and UD, we use a mini-batch size of 32, Adam's learning rate of $10^{-5}$. The number of epochs are set to 4 and 50 for XNLI and UD tasks respectively. All experiments are carried out on a single Tesla V100 16GB GPU. Each RAMEN$_{\textsc {base}}$ model is trained within a day and each RAMEN$_{\textsc {large}}$ is trained within two days.

### Relevance

Label: 

## Record 0324

Paper: From English To Foreign Languages: Transferring Pre-trained Language Models

### Question

> What metrics are used for evaluation?

### Passage

> We build on top of RAMEN a graph-based dependency parser BIBREF27. For the purpose of evaluating the contextual representations learned by our model, we do not use part-of-speech tags. Contextualized representations are directly fed into Deep-Biaffine layers to predict arc and label scores. Table TABREF34 presents the Labeled Attachment Scores (LAS) for zero-shot dependency parsing.
> 
> We first look at the fairest comparison between mBERT and monolingually initialized RAMEN$_{\textsc {base}}$+BERT. The latter outperforms the former on five languages except Arabic. We observe the largest gain of +5.2 LAS for French. Chinese enjoys +3.1 LAS from our approach. With similar architecture (12 or 24 layers) and initialization (using monolingual or parallel data), RAMEN+RoBERTa performs better than RAMEN+BERT for most of the languages. Arabic and Hindi benefit the most from bigger models. For the other four languages, RAMEN$_{\textsc {large}}$ renders a modest improvement over RAMEN$_{\textsc {base}}$.

### Relevance

Label: 

## Record 0325

Paper: From English To Foreign Languages: Transferring Pre-trained Language Models

### Question

> What metrics are used for evaluation?

### Passage

> Pre-trained models BIBREF0, BIBREF1 have received much of attention recently thanks to their impressive results in many down stream NLP tasks. Additionally, multilingual pre-trained models enable many NLP applications for other languages via zero-short cross-lingual transfer. Zero-shot cross-lingual transfer has shown promising results for rapidly building applications for low resource languages. BIBREF2 show the potential of multilingual-BERT BIBREF0 in zero-shot transfer for a large number of languages from different language families on five NLP tasks, namely, natural language inference, document classification, named entity recognition, part-of-speech tagging, and dependency parsing.
> 
> Although multilingual models are an important ingredient for enhancing language technology in many languages, recent research on improving pre-trained models puts much emphasis on English BIBREF3, BIBREF4, BIBREF5. The current state of affairs makes it difficult to translate advancements in pre-training from English to non-English languages. To our best knowledge, there are only three available multilingual pre-trained models to date: (1) the multilingual-BERT (mBERT) that supports 104 languages, (2) cross-lingual language model BIBREF6 that supports 100 languages, and (3) Language Agnostic SEntence Representations BIBREF7 that supports 93 languages. Among the three models, LASER is based on neural machine translation approach and strictly requires parallel data to train.
> 
> Do multilingual models always need to be trained from scratch? Can we transfer linguistic knowledge learned by English pre-trained models to other languages? In this work, we develop a technique to rapidly transfer an existing pre-trained model from English to other languages in an energy efficient way BIBREF8. As the first step, we focus on building a bilingual language model (LM) of English and a target language. Starting from a pre-trained English LM, we learn the target language specific parameters (i.e., word embeddings), while keeping the encoder layers of the pre-trained English LM fixed. We then fine-tune both English and target model to obtain the bilingual LM. We apply our approach to autoencoding language models with masked language model objective and show the advantage of the proposed approach in zero-shot transfer. Our main contributions in this work are:
> 
> We propose a fast adaptation method for obtaining a bilingual BERT$_{\textsc {base}}$ of English and a target language within a day using one Tesla V100 16GB GPU.
> 
> We evaluate our bilingual

### Relevance

Label: 

## Record 0326

Paper: Massively Multilingual Neural Grapheme-to-Phoneme Conversion

### Question

> what datasets did they use?

### Passage

> Finally, we report our models' results on unseen languages in Table TABREF28 . The unseen languages are any that are present in the test corpus but absent from the training data. Deri and Knight did not report results specifically on these languages. Although the NoLangID models sometimes do better on WER 100, even here the LangID models have a slight advantage in WER and PER. This is somewhat surprising because the LangID models have not learned embeddings for the language ID tokens of unseen languages. Perhaps negative associations are also being learned, driving the model towards predicting more common pronunciations for unseen languages.

### Relevance

Label: 

## Record 0327

Paper: Massively Multilingual Neural Grapheme-to-Phoneme Conversion

### Question

> what datasets did they use?

### Passage

> Adding a language ID token always improves results in cases where an embedding has been learned for that token. The power of these embeddings is demonstrated by what happens when one feeds the same input word to the model with different language tokens, as is seen in Table TABREF30 . Impressively, this even works when the source sequence is in the wrong script for the language, as is seen in the entry for Arabic.

### Relevance

Label: 

## Record 0328

Paper: Massively Multilingual Neural Grapheme-to-Phoneme Conversion

### Question

> what datasets did they use?

### Passage

> In contrast to the language embeddings, the phoneme embeddings appear to show many regularities (see Table TABREF33 ). This is a sign that our multilingual model learns similar embeddings for phonemes that are written with the same grapheme in different languages. These phonemes tend to be phonetically similar to each other.
> 
> Perhaps the structure of the phoneme embedding space is what leads to our models' very good performance on WER 100. Even when the model's first predicted pronunciation is not correct, it tends to assign more probability mass to guesses that are more similar to the correct one. Applying some sort of filtering or reranking of the system output might therefore lead to better performance.

### Relevance

Label: 

## Record 0329

Paper: Massively Multilingual Neural Grapheme-to-Phoneme Conversion

### Question

> what datasets did they use?

### Passage

> Our approach is similar in goal to deri2016grapheme's model for adapting high resource g2p models for low resource languages. They trained weighted finite state transducer (wFST) models on a variety of high resource languages, then transferred those models to low resource languages, using a language distance metric to choose which high resource models to use and a phoneme distance metric to map the high resource language's phonemes to the low resource language's phoneme inventory. These distance metrics are computed based on data from Phoible BIBREF4 and URIEL BIBREF5 .
> 
> Other low resource g2p systems have used a strategy of combining multiple models. schlippe2014combining trained several data-driven g2p systems on varying quantities of monolingual data and combined their outputs with a phoneme-level voting scheme. This led to improvements over the best-performing single system for small quantities of data in some languages. jyothilow trained recurrent neural networks for small data sets and found that a version of their system that combined the neural network output with the output of the wFST-based Phonetisaurus system BIBREF1 did better than either system alone.
> 
> A different approach came from kim2012universal, who used supervised learning with an undirected graphical model to induce the grapheme–phoneme mappings for languages written in the Latin alphabet. Given a short text in a language, the model predicts the language's orthographic rules. To create phonemic context features from the short text, the model naïvely maps graphemes to IPA symbols written with the same character, and uses the features of these symbols to learn an approximation of the phonotactic constraints of the language. In their experiments, these phonotactic features proved to be more valuable than geographical and genetic features drawn from WALS BIBREF6 .

### Relevance

Label: 

## Record 0330

Paper: Massively Multilingual Neural Grapheme-to-Phoneme Conversion

### Question

> what datasets did they use?

### Passage

> In recent years, neural networks have emerged as a common way to use data from several languages in a single system. Google's zero-shot neural machine translation system BIBREF7 shares an encoder and decoder across all language pairs. In order to facilitate this multi-way translation, they prepend an artificial token to the beginning of each source sentence at both training and translation time. The token identifies what language the sentence should be translated to. This approach has three benefits: it is far more efficient than building a separate model for each language pair; it allows for translation between languages that share no parallel data; and it improves results on low-resource languages by allowing them to implicitly share parameters with high-resource languages. Our g2p system is inspired by this approach, although it differs in that there is only one target “language”, IPA, and the artificial tokens identify the language of the source instead of the language of the target.
> 
> Other work has also made use of multilingually-trained neural networks. Phoneme-level polyglot language models BIBREF8 train a single model on multiple languages and additionally condition on externally constructed typological data about the language. ostling2017continuous used a similar approach, in which a character-level neural language model is trained on a massively multilingual corpus. A language embedding vector is concatenated to the input at each time step. The language embeddings their system learned correlate closely to the genetic relationships between languages. However, neither of these models was applied to g2p.

### Relevance

Label: 

## Record 0331

Paper: Effective Modeling of Encoder-Decoder Architecture for Joint Entity and Relation Extraction

### Question

> Which one of two proposed approaches performed better in experiments?

### Passage

> The relation tuples extracted by a joint model can be erroneous for multiple reasons such as: (i) extracted entities are wrong; (ii) extracted relations are wrong; (iii) pairings of entities with relations are wrong. To see the effects of the first two reasons, we analyze the performance of HRL and our models on entity generation and relation generation separately. For entity generation, we only consider those entities which are part of some tuple. For relation generation, we only consider the relations of the tuples. We include the performance of our two models and HRL on entity generation and relation generation in Table TABREF20. Our proposed models perform better than HRL on both tasks. Comparing our two models, PtrNetDecoding performs better than WordDecoding on both tasks, although WordDecoding achieves higher F1 scores in tuple extraction. This suggests that PtrNetDecoding makes more errors while pairing the entities with relations. We further analyze the outputs of our models and HRL to determine the errors due to ordering of entities (Order), mismatch of the first entity (Ent1), and mismatch of the second entity (Ent2) in Table TABREF21. WordDecoding generates fewer errors than the other two models in all the categories and thus achieves the highest F1 scores on both datasets.

### Relevance

Label: 

## Record 0332

Paper: Effective Modeling of Encoder-Decoder Architecture for Joint Entity and Relation Extraction

### Question

> Which one of two proposed approaches performed better in experiments?

### Passage

> Extracting relation tuples from sentences is a challenging task due to different length of entities, the presence of multiple tuples, and overlapping of entities among tuples. In this paper, we propose two novel approaches using encoder-decoder architecture to address this task. Experiments on the New York Times (NYT) corpus show that our proposed models achieve significantly improved new state-of-the-art F1 scores. As future work, we would like to explore our proposed models for a document-level tuple extraction task.

### Relevance

Label: 

## Record 0333

Paper: Effective Modeling of Encoder-Decoder Architecture for Joint Entity and Relation Extraction

### Question

> Which one of two proposed approaches performed better in experiments?

### Passage

> overlapping entities. (iii) It should be able to extract exactly two entities of a tuple with their full names. To address these challenges, we propose two novel approaches using encoder-decoder architecture. We first propose a new representation scheme for relation tuples (Table TABREF1) such that it can represent multiple tuples with overlapping entities and different lengths of entities in a simple way. We employ an encoder-decoder model where the decoder extracts one word at a time like machine translation models. At the end of sequence generation, due to the unique representation of the tuples, we can extract the tuples from the sequence of words. Although this model performs quite well, generating one word at a time is somewhat unnatural for this task. Each tuple has exactly two entities and one relation, and each entity appears as a continuous text span in a sentence. The most effective way to identify them is to find their start and end location in the sentence. Each relation tuple can then be represented using five items: start and end location of the two entities and the relation between them (see Table TABREF1). Keeping this in mind, we propose a pointer network-based decoding framework. This decoder consists of two pointer networks which find the start and end location of the two entities in a sentence, and a classification network which identifies the relation between them. At every time step of the decoding, this decoder extracts an entire relation tuple, not just a word. Experiments on the New York Times (NYT) datasets show that our approaches work effectively for this task and achieve state-of-the-art performance. To summarize, the contributions of this paper are as follows:
> 
> (1) We propose a new representation scheme for relation tuples such that an encoder-decoder model, which extracts one word at each time step, can still find multiple tuples with overlapping entities and tuples with multi-token entities from sentences. We also propose a masking-based copy mechanism to extract the entities from the source sentence only.
> 
> (2) We propose a modification in the decoding framework with pointer networks to make the encoder-decoder model more suitable for this task. At every time step, this decoder extracts an entire relation tuple,

### Relevance

Label: 

## Record 0334

Paper: Effective Modeling of Encoder-Decoder Architecture for Joint Entity and Relation Extraction

### Question

> Which one of two proposed approaches performed better in experiments?

### Passage

> Distantly-supervised information extraction systems extract relation tuples with a set of pre-defined relations from text. Traditionally, researchers BIBREF0, BIBREF1, BIBREF2 use pipeline approaches where a named entity recognition (NER) system is used to identify the entities in a sentence and then a classifier is used to find the relation (or no relation) between them. However, due to the complete separation of entity detection and relation classification, these models miss the interaction between multiple relation tuples present in a sentence.
> 
> Recently, several neural network-based models BIBREF3, BIBREF4 were proposed to jointly extract entities and relations from a sentence. These models used a parameter-sharing mechanism to extract the entities and relations in the same network. But they still find the relations after identifying all the entities and do not fully capture the interaction among multiple tuples. BIBREF5 (BIBREF5) proposed a joint extraction model based on neural sequence tagging scheme. But their model could not extract tuples with overlapping entities in a sentence as it could not assign more than one tag to a word. BIBREF6 (BIBREF6) proposed a neural encoder-decoder model for extracting relation tuples with overlapping entities. However, they used a copy mechanism to copy only the last token of the entities, thus this model could not extract the full entity names. Also, their best performing model used a separate decoder to extract each tuple which limited the power of their model. This model was trained with a fixed number of decoders and could not extract tuples beyond that number during inference. Encoder-decoder models are powerful models and they are successful in many NLP tasks such as machine translation, sentence generation from structured data, and open information extraction.
> 
> In this paper, we explore how encoder-decoder models can be used effectively for extracting relation tuples from sentences. There are three major challenges in this task: (i) The model should be able to extract entities and relations together. (ii) It should be able to extract multiple tuples with overlapping entities. (iii) It should be able to extract exactly two entities of a tuple with their full names. To address these challenges, we propose two novel approaches using encoder-decoder architecture. We first propose a new representation scheme for relation

### Relevance

Label: 

## Record 0335

Paper: Effective Modeling of Encoder-Decoder Architecture for Joint Entity and Relation Extraction

### Question

> Which one of two proposed approaches performed better in experiments?

### Passage

> In this task, input to the system is a sequence of words, and output is a set of relation tuples. In our first approach, we represent each tuple as entity1 ; entity2 ; relation. We use `;' as a separator token to separate the tuple components. Multiple tuples are separated using the `$\vert $' token. We have included one example of such representation in Table TABREF1. Multiple relation tuples with overlapping entities and different lengths of entities can be represented in a simple way using these special tokens (; and $\vert $). During inference, after the end of sequence generation, relation tuples can be extracted easily using these special tokens. Due to this uniform representation scheme, where entity tokens, relation tokens, and special tokens are treated similarly, we use a shared vocabulary between the encoder and decoder which includes all of these tokens. The input sentence contains clue words for every relation which can help generate the relation tokens. We use two special tokens so that the model can distinguish between the beginning of a relation tuple and the beginning of a tuple component. To extract the relation tuples from a sentence using the encoder-decoder model, the model has to generate the entity tokens, find relation clue words and map them to the relation tokens, and generate the special tokens at appropriate time. Our experiments show that the encoder-decoder models can achieve this quite effectively.

### Relevance

Label: 

## Record 0336

Paper: Short-Text Classification Using Unsupervised Keyword Expansion

### Question

> What is the language model pre-trained on?

### Passage

> The web has provided researchers with vast amounts of unlabeled text data, and enabled the development of increasingly sophisticated language models which can achieve state of the art performance despite having no task specific training BIBREF0, BIBREF1, BIBREF2. It is desirable to adapt these models for bespoke tasks such as short text classification.
> 
> Short-text is nuanced, difficult to model statistically, and sparse in features, hindering traditional analysis BIBREF3. These difficulties become further compounded when training is limited, as is the case for many practical applications.
> 
> This paper provides a method to expand short-text with additional keywords, generated using a pre-trained language model. The method takes advantage of general language understanding to suggest contextually relevant new words, without necessitating additional domain data. The method can form both derivatives of the input vocabulary, and entirely new words arising from contextualised word interactions and is ideally suited for applications where data volume is limited.
> 
> figureBinary Classification of short headlines into 'WorldPost' or 'Crime' categories, shows improved performance with extended pseudo headlines when the training set is small. Using: Random forest classifier, 1000 test examples, 10-fold cross validation.

### Relevance

Label: 

## Record 0337

Paper: Short-Text Classification Using Unsupervised Keyword Expansion

### Question

> What is the language model pre-trained on?

### Passage

> Words were generated using the BERT pre-trained model developed and trained by Google AI Language BIBREF0. BERT creates contextualized word embedding by passing a list of word tokens through 12 hidden transformer layers and generating encoded word vectors. To generate extended text, an original short-text document was passed to pre-trained BERT. At each transformer layer a new word embedding was formed and saved. BERT's vector decoder was then used to convert hidden word vectors to candidate words, the top three candidate words at each encoder layer were kept.
> 
> Each input word produced 48 candidate words, however many were duplicates. Examples of generated words per layer can be found in table SECREF12 and SECREF12 in the appendix. The generated words were sorted based on frequency, duplicate words from the original input were removed, as were stop-words, punctuation, and incomplete words. The generated words were then appended to the original document to create extended pseudo documents, the extended document was limited to 120 words in order to normalize each feature set. Further analysis can be found in table SECREF12 in the appendix.
> 
> figureThe proposed method uses the BERT pre-trained word embedding model to generate new words which are appended to the orignal text creating extended pseudo documents.

### Relevance

Label: 

## Record 0338

Paper: Short-Text Classification Using Unsupervised Keyword Expansion

### Question

> What is the language model pre-trained on?

### Passage

> Document expansion methods have typically focused on creating new features with the help of custom models. Word co-occurrence models BIBREF4, topic modeling BIBREF5, latent concept expansion BIBREF6, and word embedding clustering BIBREF7, are all examples of document expansion methods that must first be trained using either the original dataset or an external dataset from within the same domain. The expansion models may therefore only be used when there is a sufficiently large training set.
> 
> Transfer learning was developed as a method of reducing the need for training data by adapting models trained mostly from external data BIBREF8. Transfer learning can be an effective method for short-text classification and requires little domain specific training data BIBREF9, BIBREF10, however it demands training a new model for every new classification task and does not offer a general solution to sparse data enrichment.
> 
> Recently, multi-task language models have been developed and trained using ultra-large online datasets without being confined to any narrow applications BIBREF0, BIBREF1, BIBREF2. It is now possible to benefit from the information these models contain by adapting them to the task of text expansion and text classification.
> 
> This paper is a novel approach which combines the advantages of document expansion, transfer learning, and multitask modeling. It expends documents with new and relevant keywords by using the BERT pre-trained learning model, thus taking advantage of transfer learning acquired during BERT's pretraining. It is also unsupervised and requires no task specific training, thus allowing the same model to be applied to many different tasks or domains.

### Relevance

Label: 

## Record 0339

Paper: Short-Text Classification Using Unsupervised Keyword Expansion

### Question

> What is the language model pre-trained on?

### Passage

> Generating new words based solely on ultra small prompts of 10 words or fewer is a major challenge. A short sentence is often characterized by a just a single keyword, and modeling topics from such little data is difficult. Any method of keyword generation that overly relies on the individual words will lack context and fail to add new information, while attempting to freely form new words without any prior domain knowledge is uncertain and leads to misleading suggestions.
> 
> This method attempts to find balance between synonym and free-form word generation, by constraining words to fit the original sentence while still allowing for word-word and word-sentence interactions to create novel outputs.
> 
> The word vectors must move through the transformer layers together and therefore maintain the same token order and semantic meaning, however they also receive new input from the surrounding words at each layer. The result, as can be seen from table SECREF12 and SECREF12 in the appendix, is that the first few transformer layers are mostly synonyms of the input sentence since the word vectors have not been greatly modified. The central transformer layers are relevant and novel, since they are still slightly constrained but also have been greatly influenced by sentence context. And the final transformer layers are mostly non-sensical, since they have been completely altered from their original state and lost their ability to retrieve real words.
> 
> This method is unique since it avoids needing a prior dataset by using the information found within the weights of a general language model. Word embedding models, and BERT in particular, contain vast amounts of information collected through the course of their training. BERT Base for instance, has 110 Million parameters and was trained on both Wikipedea Corpus and BooksCorpus BIBREF0, a combined collection of over 3 Billion words. The full potential of such vastly trained general language models is still unfolding. This paper demonstrates that by carefully prompting and analysing these models, it is possible to extract new information from them, and extend short-text analysis beyond the limitations posed by word count.

### Relevance

Label: 

## Record 0340

Paper: Short-Text Classification Using Unsupervised Keyword Expansion

### Question

> What is the language model pre-trained on?

### Passage

> It is desirable to generate new words which are relevant to the target topics and increase predictive signal, while avoiding words which are irrelevant, add noise, and mislead predictions.
> 
> The strategy, described in section SECREF4, was created to measure word relevance and quantify the unsupervised model performance. It can be seen from fig SECREF4 and SECREF12 in the appendix that the proposed expansion method is effective at generating words which relate to topics of the input sentence, even from very little data. From the context of just a single word, the method can generate 3 new relevant words, and can generate as many as 10 new relevant words from sentences which contain 5 topic related words SECREF12. While the method is susceptible to noise, producing on average 1 word related to each irrelevant topic, the number of correct predictions statistically exceed the noise.
> 
> Furthermore, because the proposed method does not have any prior knowledge of its target topics, it remains completely domain agnostic, and can be applied generally for short text of any topic.

### Relevance

Label: 

## Record 0341

Paper: Represent, Aggregate, and Constrain: A Novel Architecture for Machine Reading from Noisy Sources

### Question

> what are the baselines?

### Passage

> Results are presented in Table TABREF44 . In comparison to previous work, our any configuration of our RAC architecture with sum-based aggregation outperforms the best existing systems by a minimum of 9.8 F INLINEFORM0 . In comparison to the various Mention-CNN systems, it is clear that this improvement is not a result of different features or the use of pre-trained word embeddings, or even the representational power of the CNN-based embeddings. Rather, it is attributable to training end-to-end with aggregation and a cluster-level loss function.
> 
> With respect to aggregation, sum-based methods consistently outperform their max counterparts, indicating that exploiting the redundancy of information in news clusters is beneficial to the task. The topic-based aggregation is statistically significant improvement over standard sum aggregation (p INLINEFORM0 ), and produces the highest performing unconstrained system.
> 
> Date-based aggregation did not yield a statistically significant improvement over sum aggregation. We hypothesize that the method is sound, but accurate datelines could only be extracted for 31 INLINEFORM0 documents. We did not modify the aggregation weights ( INLINEFORM1 ) for the remaining documents, minimizing the effect of this approach.
> 
> The EE-AS Reader has the lowest overall performance, which one can attribute to pooling evidence in a manner that is poorly suited to this problem domain. By placing a softmax over each document's beliefs, what is an advantage in the cloze-style QA setting here becomes a liability: the model is forced to predict a value for every slot, for every each document, even when few are truly mentioned.

### Relevance

Label: 

## Record 0342

Paper: Represent, Aggregate, and Constrain: A Novel Architecture for Machine Reading from Noisy Sources

### Question

> what are the baselines?

### Passage

> For values mentioned repeatedly throughout the news cluster, mention scores must be aggregated to produce a single value-level score. In this section we describe (1) how the right aggregation method can better reflect how the gold labels are applied to the data, (2) how domain knowledge can be incorporated into aggregation, and (3) how aggregation can be used as a dynamic approach to identifying missing information.
> 
> In the traditional view of distant supervision BIBREF9 , if a mention is found in an external knowledge base it is assumed that the mention is an expression of its role in the knowledge base, and it receives the corresponding label. This assumption does not always hold, and the resulting spurious labels are frequently cited as a source of training noise BIBREF10 , BIBREF11 . However, an aggregation over all mention scores provides a more accurate reflection of how distant supervision labels are applied to the data.
> 
> If one were to assign a label to each mention and construct a loss using the mention-level scores ( INLINEFORM0 ) directly, it would recreate the hard labeling of the traditional distant supervision training scenario. Instead, we relax the distant supervision assumption by using a loss on the value-level scores ( INLINEFORM1 ), with aggregation to pool beliefs from one to the other. This explicitly models the way in which cluster-wide labels are applied to mentions, and allows for spuriously labeled mentions to receive lower scores, “explaining away” the cluster's label by assigning a higher score to a mention with a more suitable representation.
> 
> Two natural choices for this aggregation are max and sum. Formally, under max aggregation the value-level scores for a value INLINEFORM0 and slot INLINEFORM1 are computed as: DISPLAYFORM0
> 
> And under sum aggregation: DISPLAYFORM0
> 
> If the most clearly expressed mentions correspond to correct values, max aggregation can be an effective strategy BIBREF10 . If the data set is noisy with numerous spurious mentions, a sum aggregation favoring values which are expressed both clearly and frequently may be the more appropriate choice.
> 
> The aforementioned aggregation methods combine mention-level scores uniformly, but for many domains one may have prior knowledge regarding which mentions should more heavily contribute to the aggregate score.

### Relevance

Label: 

## Record 0343

Paper: Represent, Aggregate, and Constrain: A Novel Architecture for Machine Reading from Noisy Sources

### Question

> what are the baselines?

### Passage

> The Stanford Plane Crash Dataset BIBREF15 is a small data set consisting of 80 plane crash events, each paired with a set of related news articles. Of these events, 40 are reserved for training, and 40 for testing, with the average cluster containing more than 2,000 mentions. Gold labels for each cluster are derived from Wikipedia infoboxes and cover up to 15 slots, of which 8 are used in evaluation (Figure TABREF54 ).
> 
> We follow the same entity normalization procedure as reschke2014, limit the cluster size to the first 200 documents, and further reduce the number of duplicate documents to prevent biases in aggregation. We partition out every fifth document from the training set to be used as development data, primarily for use in an early stopping criterion. We also construct additional clusters from the remaining training documents, and use this to increase the size of the development set.

### Relevance

Label: 

## Record 0344

Paper: Represent, Aggregate, and Constrain: A Novel Architecture for Machine Reading from Noisy Sources

### Question

> what are the baselines?

### Passage

> In all experiments we train using adaptive online gradient updates (Adam, see kingma2014). Model architecture and parameter values were tuned on the development set, and are as follows (chosen values in bold):
> 
> The number of training epochs is determined via early stopping with respect to the model performance on development data. The pre-trained word embeddings are 200-dimensional GLoVe embeddings BIBREF16 .

### Relevance

Label: 

## Record 0345

Paper: Represent, Aggregate, and Constrain: A Novel Architecture for Machine Reading from Noisy Sources

### Question

> what are the baselines?

### Passage

> We evaluate on four categories of architecture:
> 
> reschke2014 proposed several methods for event extraction in this scenario. We compare against three notable examples drawn from this work:
> 
> [leftmargin=*]
> 
> Reschke CRF: a conditional random field model.
> 
> Reschke Noisy-OR: a sequence tagger with a "Noisy-OR" form of aggregation that discourages the model from predicting the same value for multiple slots.
> 
> Reschke Best: a sequence tagger using a cost-sensitive classifier, optimized with SEARN BIBREF17 , a learning-to-search framework.
> 
> Each of these models uses features drawn from dependency trees, local context (unigram/part-of-speech features for up to 5 neighboring words), sentence context (bag-of-word/part-of-speech), words/part-of-speech of words occurring within the value, as well as the entity type of the mention itself.
> 
> The representation and scoring components of our architecture, with an additional slot for predicting a null value. The INLINEFORM0 scores are used when constructing the loss and during decoding. These scores can also be aggregated in a max/sum manner after decoding, but such aggregation is not incorporated during training.
> 
> Representation, scoring, and aggregation components, trained end-to-end with a cluster-level loss. Null values are predicted as described in Sec. UID18 .
> 
> kadlec2016 present AS Reader, a state-of-the-art model for cloze-style QA. Like our architecture, AS Reader aggregates mention-level scores, pooling evidence for each answer candidate. However, in cloze-style QA an entity is often mentioned in complementary contexts throughout the text, but are frequently in similar contexts in news cluster extraction.
> 
> We tailor AS Reader to event extraction to illustrate the importance of choosing an aggregation which reflects how the gold labels are applied to the data. EE-AS Reader is implemented by applying Eq. EQREF9 and Eq. to each document, as opposed to clusters, as documents are analogous to sentences in the cloze-style QA task. We then concatenate the resulting vectors, and apply sum aggregation as before.

### Relevance

Label: 

## Record 0346

Paper: Named Entity Recognition in Twitter using Images and Text

### Question

> Does this model perform better than the state of the art?

### Passage

> train our model.
> 
> where INLINEFORM0 and INLINEFORM1 represent the INLINEFORM2 and INLINEFORM3 position of INLINEFORM4 and INLINEFORM5 , respectively. INLINEFORM6 represents the n-gram of POS tag. INLINEFORM7 and INLINEFORM8 ( INLINEFORM9 ) represent the total objects found by a classifier INLINEFORM10 for a given class INLINEFORM11 ( INLINEFORM12 ) (where N is the total of retrieved images INLINEFORM15 ). INLINEFORM16 and INLINEFORM17 represent the distance between the two higher predictions ( INLINEFORM18 ), i.e. INLINEFORM19 . Finally, INLINEFORM20 represents the sum of all predictions made by all INLINEFORM21 classifiers INLINEFORM22 ( INLINEFORM23 ). - Training (E): the outcomes of D.1 and D.2 ( INLINEFORM26 ) are used as input features to our final classifier. We implemented a simple Decision Tree (non-parametric supervised learning method) algorithm for learning simple decision rules inferred from the data features (since it does not require any assumptions of linearity in the data and also works well with outliers, which are expected to be found more often in a noisy environment, such as the Web of Documents).

### Relevance

Label: 

## Record 0347

Paper: Named Entity Recognition in Twitter using Images and Text

### Question

> Does this model perform better than the state of the art?

### Passage

> In this paper we presented a novel architecture for NER that expands the feature set space based on feature clustering of images and texts, focused on microblogs. Due to their terse nature, such noisy data often lack enough context, which poses a challenge to the correct identification of named entities. To address this issue we have presented and evaluated a novel approach using the Ritter dataset, showing consistent results over state-of-the-art models without using any external resource or encoded rule, achieving an average of 0.59 F1. The results slightly outperformed state-of-the-art models which do not rely on encoded rules (0.49 and 0.54 F1), suggesting the viability of using the produced metadata to also boost existing NER approaches. A further important contribution is the ability to handle single tokens and misspelled words successfully, which is of utmost importance in order to better understand short texts. Finally, the architecture of the approach and its indicators introduce potential to transparently support multilingual data, which is the subject of ongoing investigation.

### Relevance

Label: 

## Record 0348

Paper: Named Entity Recognition in Twitter using Images and Text

### Question

> Does this model perform better than the state of the art?

### Passage

> In order to check the overall performance of the proposed technique, we ran our algorithm without any further rule or apriori knowledge using a gold standard for NER in microblogs (Ritter dataset BIBREF2 ), achieving INLINEFORM0 F1. tab:performance details the performance measures per class. tab:relatedwork presents current state-of-the-art results for the same dataset. The best model achieves INLINEFORM1 F1-measure, but uses encoded rules. Models which are not rule-based, achieve INLINEFORM2 and INLINEFORM3 . We argue that in combination with existing techniques (such as linguistic patterns), we can potentially achieve even better results.
> 
> As an example, the sentence “paris hilton was once the toast of the town” can show the potential of the proposed approach. The token “paris” with a LOC bias (0.6) and “hilton” (global brand of hotels and resorts) with indicators leading to LOC (0.7) or ORG (0.1, less likely though). Furthermore, “town” being correctly biased to LOC (0.7). The algorithm also suggests that the compound “paris hilton” is more likely to be a PER instead (0.7) and updates (correctly) the previous predictions. As a downside in this example, the algorithm misclassified “toast” as LOC. However, in this same example, Stanford NER annotates (mistakenly) only “paris” as LOC. It is worth noting also the ability of the algorithm to take advantage of search engine capabilities. When searching for “miCRs0ft”, the returned values strongly indicate a bias for ORG, as expected ( INLINEFORM0 = 0.2, INLINEFORM1 = 0.8, INLINEFORM2 = 0.0, INLINEFORM3 = 6, INLINEFORM4 = -56, INLINEFORM5 = 0.0, INLINEFORM6 = 0.5, INLINEFORM7 = 0.0, INLINEFORM8 = 5). More local organisations are also recognized correctly, such as “kaufland” (German supermarket), which returns the following metadata: INLINEFORM9 = 0.2, INLINEFORM10 = 0.4, INLINEFORM11 = 0.0, INLINEFORM12 = 2, INLINEFORM13 = -50, INLINEFORM14 = 0.1, INLINEFORM15 = 0.4, INLINEFORM16 = 0.0, INLINEFORM17 = 3.

### Relevance

Label: 

## Record 0349

Paper: Named Entity Recognition in Twitter using Images and Text

### Question

> Does this model perform better than the state of the art?

### Passage

> in tab:tbempirical.
> 
> Training (D.1): we used SIFT (Scale Invariant Feature Transform) features BIBREF12 for extracting image descriptors and BoF (Bag of Features) BIBREF13 , BIBREF14 for clustering the histograms of extracted features. The clustering is possible by constructing a large vocabulary of many visual words and representing each image as a histogram of the frequency words that are in the image. We use k-means BIBREF15 to cluster the set of descriptors to INLINEFORM0 clusters. The resulting clusters are compact and separated by similar characteristics. An empirical analysis shows that some image groups are often related to certain named entities (NE) classes when using search engines, as described in tab:tbempirical. For training purposes, we used the Scene 13 dataset BIBREF16 to train our classifiers for location (LOC), “faces” from Caltech 101 Object Categories BIBREF17 to train our person (PER) and logos from METU dataset BIBREF18 for organisation ORG object detection. These datasets produces the training data for our set of supervised classifiers (1 for ORG, 1 for PER and 10 for LOC). We trained our classifiers using Support Vector Machines BIBREF19 once they generalize reasonably enough for the task.
> 
> Text Analytics (TA): Text Classification - Function Description (D.2): analogously to (D.1), we perform clustering to group texts together that are “distributively” similar. Thus, for each retrieved web page (title and excerpt of its content), we perform the classification based on the main NER classes. We extracted features using a classical sparse vectorizer (Term frequency-Inverse document frequency - TF-IDF. In experiments, we did not find a significant performance gain using HashingVectorizer) - Training (D.2): with this objective in mind, we trained classifiers that rely on a bag-of-words technique. We collected data using DBpedia instances to create our training dataset ( INLINEFORM0 ) and annotated each instance with the respective MUC classes, i.e. PER, ORG and LOC. Listing shows an example of a query to obtain documents of organizations (ORG class). Thereafter, we used this annotated dataset to train our model.
> 
> where INLINEFORM0 and INLINEFORM1 represent the INLINEFORM2 and INLINEFORM3 position of INLINEFORM4 and INLINEFORM5 , respectively. INLINEFORM6 represents the n-gram of POS tag. INLINEFORM7 and INLINEFORM8 ( INLINEFORM9 ) represent the total objects found by a classifier

### Relevance

Label: 

## Record 0350

Paper: Named Entity Recognition in Twitter using Images and Text

### Question

> Does this model perform better than the state of the art?

### Passage

> The main insight underlying this work is that we can produce a NER model which performs similarly to state-of-the-art approaches but without relying on any specific resource or encoded rule. To this aim, we propose a multi-level architecture which intends to produce biased indicators to a certain class (LOC, PER or ORG). These outcomes are then used as input features for our final classifier. We perform clustering on images and texts associated to a given term INLINEFORM0 existing in complete or partial sentences INLINEFORM1 (e.g., “new york” or “einstein”), leveraging the global context obtained from the Web providing valuable insights apart from standard local features and hand-coded information. fig:architecture gives an overview of the proposed architecture.
> 
> In the first step (A), we simply apply POS Tagging and Shallow Parsing to filter out tokens except for those tagged as INLINEFORM0 or INLINEFORM1 and their INLINEFORM2 (local context). Afterwards, we use the search engine (B) to query and cache (C) the top INLINEFORM3 texts and images associated to each term INLINEFORM4 , where INLINEFORM5 is the set resulting of the pre-processing step (A) for each (partial or complete) sentence INLINEFORM6 . This resulting data (composed of excerpts of texts and images from web pages) is used to predict a possible class for a given term. These outcomes are then used in the first two levels (D.1 and D.2) of our approach: the Computer Vision and Text Analytics components, respectively, which we introduce as follows:
> 
> Computer Vision (CV): Detecting Objects: Function Description (D.1): given a set of images INLINEFORM0 , the basic idea behind this component is to detect a specific object (denoted by a class INLINEFORM1 ) in each image. Thus, we query the web for a given term INLINEFORM2 and then extract the features from each image and try to detect a specific object (e.g., logos for ORG) for the top INLINEFORM3 images retrieved as source candidates. The mapping between objects and NER classes is detailed in tab:tbempirical.
> 
> Training (D.1): we used SIFT (Scale Invariant Feature Transform) features BIBREF12 for extracting image descriptors and BoF (Bag of Features) BIBREF13 , BIBREF14 for clustering the histograms of extracted features. The clustering is possible by constructing a large

### Relevance

Label: 

## Record 0351

Paper: The Power of Communities: A Text Classification Model with Automated Labeling Process Using Network Community Detection

### Question

> which had better results, the svm or the random forest model?

### Passage

> In this study, we demonstrated a new approach of training text classification models using the network community detection, and showed how the network community detection can help improve the models by automatically labeling text data and detecting misslabeled or ambiguous data points. As seen in this paper, we were able to yield better results in the accuracy of Support vector machine and Random forest models compared to the same models that were trained on the original human labeled data for the particular text classification problem. Our approach is not only useful in producing better classifiation models, but also in testing the quality of human made text data. One might be able to get even better results using this method by utilizing more sophisticatedly custom designed synonyms and stopwords, using more advanced natural language processing methods such as word-embeddings, utilizing higher n-grams such as trigrams, and using more balanced data sets. In the future, we would like to expand this study further to use the network itself to parse out classifications of unseen sentences without training machine learning models.

### Relevance

Label: 

## Record 0352

Paper: The Power of Communities: A Text Classification Model with Automated Labeling Process Using Network Community Detection

### Question

> which had better results, the svm or the random forest model?

### Passage

> Figure.FIGREF20 shows the accuracy of the four Support vector machine and Random forest models trained on the original human labeled data and on the data labeled by our method. The accuracies are hit ratios that compute the number of correctly classified sentences over the number of all sentences in the test data. For example, if a model classified 85 sentences correctly out of 100 test sentences, then the accuracy is 0.85. In order to accurately compute the Ground truth hit ratio, we used the ground truth messages in the chatbot. The messages are the sentences that are to be shown to the chatbot users in response to the classification for a particular user query as below.
> 
> For example, for a question of "how do I get there by subway?", in the chatbot, there is a designed message of "You can take line M or B to 35th street." to respond to that particular query. Using these output messages in the chatbot, we were able to compute the ground truth accuracy of our classification models by comprehending the input sentences in the test sets, the detected classes from the models and linked messages. In our test, the Support vector machine trained on human labeled data performed 0.9572 while the same model trained on the data labeled by our method resulted 0.9931. Also, the Random forest model trained on human labeled data performed 0.9504 while the same model trained on the data labeled by our method did 0.9759.

### Relevance

Label: 

## Record 0353

Paper: The Power of Communities: A Text Classification Model with Automated Labeling Process Using Network Community Detection

### Question

> which had better results, the svm or the random forest model?

### Passage

> The particular algorithm of network community detection used in this study is Louvain method BIBREF2 which partitions a network into the number of nodes - every node is its own comunity, and from there, clusters the nodes in a way to maximize each cluster's modularity which indicates how strong is the connectivity between the nodes in the community. This means that, based on the cosine similarity scores - the networks edge weights, the algorithm clusters similar sentences together in a same community while the algorithm proceeds maximizing the connectivity strength amongst the nodes in each community. The network constructed with no threshold in place was detected to have 18 distinct communities with three single node communities. Based on the visualized network (see Figure.FIGREF13), it seemed that the network community detection method clustered the sentence network as good as the original data set with human labeled classes although the communities do not look quite distinct. However, based on the fact that it had three single node communities and the number of distinct communities is less than the number of classes in the human labeled data set, we suspected possible problems that would degrade the quality of the community detection for the use of training text classification models.

### Relevance

Label: 

## Record 0354

Paper: The Power of Communities: A Text Classification Model with Automated Labeling Process Using Network Community Detection

### Question

> which had better results, the svm or the random forest model?

### Passage

> Text data is a great source of knowledge for building many useful recommendation systems, search engines as well as conversational intelligence systems. However, it is often found to be a difficult and time consuming task to structure the unstructured text data especially when it comes to labeling the text data for training text classification models. Data labeling, typically done by humans, is prone to make misslabeled data entries, and hard to track whether the data is correctly labeled or not. This human labeling practice indeed impacts on the quality of the trained models in solving classificastion problems.
> 
> Some previous studies attempted to solve this problem by utilizing unsupervised BIBREF3, BIBREF4 and semisupervised BIBREF5 machine learning models. However, those studies used pre-defined keywords list for each category in the document, which provides the models with extra referencial materials to look at when making the classification predictions, or included already labeled data as a part of the entire data set from which the models learn. In case of using clustering algorithms such as K$-$means BIBREF4, since the features selected for each class depend on the frequency of the particular words in the sentences, when there are words that appear in multiple sentences frequently, it is very much possible that those words can be used as features for multiple classes leading the model to render more ambiguity, and to result a poor performance in classifying documents.
> 
> Although there are many studies in text classification problems using machine learning techniques, there has been a limited number of studies conducted in text classifications utilizing networks science. Network science is actively being adopted in studying biological networks, social networks, financial market prediction BIBREF6 and more in many fields of study to mine insights from the collectively inter-connected components by analysing their relationships and structural characteristics. Only a few studies adopted network science theories to study text classifications, and showed preliminary results of the text clustering performed by network analysis specially with network community detection algorithms BIBREF7, BIBREF8. However, those studies did not clearly show the quality of community detection algorithms and other possible usefull features. Network community detection BIBREF9 is graph clustering methods actively used in complex networks analysis From large

### Relevance

Label: 

## Record 0355

Paper: The Power of Communities: A Text Classification Model with Automated Labeling Process Using Network Community Detection

### Question

> which had better results, the svm or the random forest model?

### Passage

> We checked the community detection results with the original human labeled data by comparing the sentences in each community with the sentences in each human labeled class to confirm how well the algorithm worked. We built class maps to facilitate this process (see Figure.FIGREF15) that show mapping between communities in the sentence networks and classes in the original data set. Using the class maps, we found two notable cases where; 1. the sentences from multiple communities are consist of the sentences of one class of the human labeled data, meaning the original class is splitted into multiple communities and 2. the sentences from one community consist of the sentences of multiple classes in human labeled data, meaning multiple classes in the original data are merged into one community. For example, in the earlier case (see blue lines in Figure.FIGREF15) which we call Class-split, the sentences in COMMUNITY_1, COMMUNITY_2, COMMUNITY_5, COMMUNITY_8, COMMUNITY_10, COMMUNITY_14 and COMMUNITY_17 are the same as the sentences in CHAT_AGENT class. Also, in the later case (see red lines in Figure.FIGREF15) which we call Class-merge, the sentences in COMMUNITY_7 are the same as the sentences in GETINFO_PARKING, GETINFO_NEARBY_RESTAURANT, GETINFO_TOUR, GETINFO_EXACT_ADDRESS, STARTOVER, ORDER_EVENTS, GETINFO_JOB, GETINFO, GETINFO_DRESSCODE, GETINFO_LOST_FOUND as well as GETINFO_FREE_PERFORMANCE.
> 
> The Class-split happens when a human labeled class is devided into multiple communities as the sentence network is clustered based on the semantic similarity. This actually can help improve the text classification based systems to work more sophisticatedly as the data set gets more detailed subclasses to design the systems with. Although, it is indeed a helpful phenomena, we would like to minimize the number of subclasses created by the community detection algorithm simply because we want to avoid having too many subclasses that would add more complexity in designing any applications using the community data. On the other hand, the Class-merge happens when multiple human labeled classes are merged into one giant community. This Class-merge phenomena also helps improve the original data set by detecting either misslabeled or ambiguous data entries. We will discuss more details in the following subsection. Nonetheless, we also want to minimize the number of classes merged into the one giant community, because when too many classes are

### Relevance

Label: 

## Record 0356

Paper: Evaluating the Performance of a Speech Recognition based System

### Question

> what bottlenecks were identified?

### Passage

> to go through different number of recognition nodes. For example, to complete the Arrival service it is required to pass through 3 recognition nodes namely (a) selection of a service, (b) selection of a train name and (c) selection of the railway station. While the perplexity (the words that are active) at the service selection node is fixed the perplexity at the station selection node could depend on the selection of the train name at an earlier node. For example, if the selected train stops at 23 stations, then the perplexity at the station selection node will be INLINEFORM2 .
> 
> For confusability analysis at each of the node, we have used the Levenshtein distance BIBREF5 or the edit distance as is well known in computer science literature. We found that the utterances /Sahi/ and /Galat/ have 100% recognition. These words Sahi is represented by the string of phonemes in the lexicon as S AA HH I and the word Galat is represented as the phoneme sequence G L AX tT in the lexicon. We identified the edit distance between these two words Sahi and Galat and used that distance measure as the threshold that is able to differentiate any two words (say INLINEFORM0 ). So if the distance between any two active words at a given recognition node is lower than the threshold INLINEFORM1 , then there is a greater chance that those two active words could get confused (one word could be recognized as the other which is within a distance of INLINEFORM2 ). There are ways in which this possible misrecognition words could be avoided. The easiest way is to make sure that these two words together are not active at a given recognition node.
> 
> Table TABREF6 shows the list of active word at the node 1 when the speech application was initially designed and Table TABREF7 shows the edit distance between all the active words at the node service given in Fig. FIGREF4 . The distance between words Sahi and Galat was found to be INLINEFORM0 which was set at the threshold, namely INLINEFORM1 . This threshold value was used to identify confusing active words. Clearly, as seen in the Table the

### Relevance

Label: 

## Record 0357

Paper: Evaluating the Performance of a Speech Recognition based System

### Question

> what bottlenecks were identified?

### Passage

> In this paper we proposed a methodology to identify words that could lead to confusion at any given node of a speech recognition based system. We used edit distance as the metric to identifying the possible confusion between the active words. We showed that this metric can be used effectively to enhance the performance of a speech solution without actually putting it to people test. There is a significant saving in terms of being able to identify recognition bottlenecks in a menu based speech solution through this analysis because it does not require actual people testing the system. This methodology was adopted to restructuring the set of active words at each node for better speech recognition in an actual menu based speech recognition system that caters to masses.

### Relevance

Label: 

## Record 0358

Paper: Evaluating the Performance of a Speech Recognition based System

### Question

> what bottlenecks were identified?

### Passage

> the system can have several nodes for completion of a transaction. Typical menu based speech solutions strive for a 3 - 5 level nodes to make it usable. In any speech based solution (see Fig. FIGREF3 ) first the spoken utterance is hypothesized into a sequence of phonemes using the acoustic models. Since the phoneme recognition accuracy is low, instead of choosing one phoneme it identifies l-best (typically INLINEFORM0 ) matching phonemes. This phone lattice is then matched with all the expected words (language model) at that node to find the best match. For a node with perplexity INLINEFORM1 the constructed phoneme lattice of the spoken utterance is compared with the phoneme sequence representation of all the INLINEFORM2 words (through the lexicon which is one of he key components of a speech recognition system). The hypothesized phone lattice is declared one of the INLINEFORM3 words depending on the closeness of the phoneme lattice to the phoneme representation of the INLINEFORM4 words.
> 
> We hypothesize that we can identify the performance of a menu based speech system by identifying the possible confusion among all the words that are active at a given node. If active words at a given node are phonetically similar it becomes difficult for the speech recognition system to distinguish them which in turn leads to recognition errors. We used Levenshtein distance BIBREF4 , BIBREF5 a well known measure to analyze and identify the confusion among the active words at a given node. This analysis gives a list of all set of words that have a high degree of confusability among them; this understanding can be then used to (a) restructure the set of active words at that node and/or (b) train the words that can be confused by using a larger corpus of speech data. This allows the speech recognition engine to be equipped to be able to distinguish the confusing words better. Actual use of this analysis was carried out for a speech solution developed for Indian Railway Inquiry System to identify bottlenecks in the system before its actual launch.

### Relevance

Label: 

## Record 0359

Paper: Evaluating the Performance of a Speech Recognition based System

### Question

> what bottlenecks were identified?

### Passage

> time consuming procedure.
> 
> In this paper, we describe a method to evaluate the performance of a speech solution without actual people using the system as is usually done. We then show how this method was adopted to evaluate a speech recognition based solution as a case study. This is the main contribution of the paper. The rest of the paper is organized as follows. The method for evaluation without testing is described in Section SECREF2 . In Section SECREF3 we present a case study and conclude in Section SECREF4 .

### Relevance

Label: 

## Record 0360

Paper: Evaluating the Performance of a Speech Recognition based System

### Question

> what bottlenecks were identified?

### Passage

> FIGREF4 . The distance between words Sahi and Galat was found to be INLINEFORM0 which was set at the threshold, namely INLINEFORM1 . This threshold value was used to identify confusing active words. Clearly, as seen in the Table the distance between word pairs fare, pnr and pnr, prasthan is INLINEFORM2 and INLINEFORM3 respectively, which is very close to the threshold value of INLINEFORM4 . This can cause a high possibility that /fare/ may get recognized as pnr and vice-versa.
> 
> One can derive from the analysis of the active words that fare and pnr can not coexist as active words at the same node. The result of the analysis was to remove the active words fare and pnr at that node.
> 
> When the speech system was actually tested by giving speech samples, 17 out of 20 instances of /pnr/ was was recognized as fare and vice-versa. Similarly 19 out of 20 instances /pnr/ was misrecognized as prasthan and vice versa This confusion is expected as can be seen from the edit distance analysis of the active words in the Table TABREF7 . This modified active word list (removal of fare and pnr) increased the recognition accuracy at the service node (Fig. FIGREF4 ) by as much as 90%.
> 
> A similar analysis was carried out at other recognition nodes and the active word list was suitably modified to avoid possible confusion between active word pair. This analysis and modification of the list of active words at a node resulted in a significant improvement in the transaction completion rate. We will present more experimental results in the final paper.

### Relevance

Label: 

## Record 0361

Paper: Multilingual Twitter Corpus and Baselines for Evaluating Demographic Bias in Hate Speech Recognition

### Question

> Which document classifiers do they experiment with?

### Passage

> We consider four user factors of age, race, gender and geographic location. For location, we inference two granularities, country and US region, but only experiment with the country attribute. While the demographic attributes can be inferred through tweets BIBREF22, BIBREF8, we intentionally exclude the contents from the tweets if they infer these user attributes, in order to make the evaluation of fairness more reliable and independent. If users were grouped based on attributes inferred from their text, then any differences in text classification across those groups could be related to the same text. Instead, we infer attributes from public user profile information (i.e., description, name and photo).

### Relevance

Label: 

## Record 0362

Paper: Multilingual Twitter Corpus and Baselines for Evaluating Demographic Bias in Hate Speech Recognition

### Question

> Which document classifiers do they experiment with?

### Passage

> both word usage and grammar BIBREF13. The rich variations have not been explored under the fairness evaluation due to lack of multilingual corpora. Additionally, while we have hate speech detection datasets in multiple languages BIBREF14, BIBREF15, BIBREF16, BIBREF17, BIBREF18, there is still no integrated multilingual corpora that contain author demographic attributes which can be used to measure group fairness. The lack of author demographic attributes and multilingual datasets limits research for evaluating classifier fairness and developing unbiased classifiers.
> 
> In this study, we combine previously published corpora labeled for Twitter hate speech recognition in English BIBREF14, BIBREF19, BIBREF20, Italian BIBREF15, Polish BIBREF16, Portuguese BIBREF18, and Spanish BIBREF17, and publish this multilingual data augmented with author-level demographic information for four attributes: race, gender, age and country. The demographic factors are inferred from user profiles, which are independent from text documents, the tweets. To our best knowledge, this is the first multilingual hate speech corpus annotated with author attributes aiming for fairness evaluation. We start with presenting collection and inference steps of the datasets. Next, we take an exploratory study on the language variations across demographic groups on the English dataset. We then experiment with four multiple classification models to establish baseline levels of this corpus. Finally, we evaluate the fairness performance of those document classifiers.

### Relevance

Label: 

## Record 0363

Paper: Multilingual Twitter Corpus and Baselines for Evaluating Demographic Bias in Hate Speech Recognition

### Question

> Which document classifiers do they experiment with?

### Passage

> Demographic variations root in documents, especially in social media data BIBREF26, BIBREF25, BIBREF10. Such variations could further impact the performance and fairness of document classifiers. In this study, we experiment four different classification models including logistic regression (LR), recurrent neural network (RNN) BIBREF35, convolutional neural network (CNN) BIBREF36 and Google BERT BIBREF37. We present the baseline results of both performance and fairness evaluations across the multilingual corpus.

### Relevance

Label: 

## Record 0364

Paper: Multilingual Twitter Corpus and Baselines for Evaluating Demographic Bias in Hate Speech Recognition

### Question

> Which document classifiers do they experiment with?

### Passage

> We implement and experiment four baseline classification models. To compare fairly, we keep the feature size up to 15K for each classifier across all five languages. We calculate the weight for each document category by $\frac{N}{N_l}$ BIBREF39, where $N$ is the number of documents in each language and $N_l$ is the number of documents labeled by the category. Particularly, for training BERT model, we append two additional tokens, “[CLS]” and “[SEP]”, at the start and end of each document respectively. For the neural models, we pad each document or drop rest of words up to 40 tokens. We use “unknown” as a replacement for unknown tokens. We initialize CNN and RNN classifiers by pre-trained word embeddings BIBREF40, BIBREF41, BIBREF42, BIBREF43 and train the networks up to 10 epochs.

### Relevance

Label: 

## Record 0365

Paper: Multilingual Twitter Corpus and Baselines for Evaluating Demographic Bias in Hate Speech Recognition

### Question

> Which document classifiers do they experiment with?

### Passage

> Demographic factors can improve the performances of document classifiers BIBREF25, and demographic variations root in language, especially in social media data BIBREF26, BIBREF25. For example, language styles are highly correlated with authors' demographic attributes, such as age, race, gender and location BIBREF27, BIBREF28. Research BIBREF29, BIBREF12, BIBREF30 find that biases and stereotypes exist in word embeddings, which is widely used in document classification tasks. For example, “receptionist” is closer to females while “programmer” is closer to males, and “professor” is closer to Asian Americans while “housekeeper” is closer to Hispanic Americans.
> 
> This motivates us to explore and test if the language variations hold in our particular dataset, how strong the effects are. We conduct the empirical analysis of demographic predictability on the English dataset.

### Relevance

Label: 

## Record 0366

Paper: A Surrogate-based Generic Classifier for Chinese TV Series Reviews

### Question

> Is manual annotation performed?

### Passage

> To prove the generalization of our classifiers, we use two of the TV series as training data and the rest as testing set. We compare them with classifiers trained without the replacement of generic tags like role_i or actor_j. So 3 sets of experiments are performed, and each are trained on top of Bayes, Logistic Regression and SVM. Average accuracies among them are reported as the performance measure for the sake of space limit. The results are shown in Table TABREF42 . “1”, “2” and “3” represent the TV series “The Journey of Flower”, “Nirvana in Fire” and “Good Time” respectively. In each cell, the left value represents accuracy of classifier without replacement of generic tags and winners are bolded.
> 
> From the above table, we can see with substitutions of generic tags in movie reviews, the top 5 classifiers have seen performance increase, which indicates the effectiveness of our method. However for the rest three classifiers, we didn't see an improvement and in some cases the performance seems decreased. This might be due to the fact that in the first five categories, roles' or actors' names are mentioned pretty frequently while the rest classes don't care much about these. But some specific names might be helpful in these categories' classification, so the performance has decreased in some degree.

### Relevance

Label: 

## Record 0367

Paper: A Surrogate-based Generic Classifier for Chinese TV Series Reviews

### Question

> Is manual annotation performed?

### Passage

> Dataset is another important factor influencing the performance of our classifiers. Most of the public available movie review data is in English, like the IMDB dataset collected by Pang/Lee 2004 BIBREF10 . Although it covers all kinds of movies in IMDB website, it only has labels related with the sentiment. Its initial goal was for sentiment analysis. Another intact movie review dataset is SNAP BIBREF11 , which consists of reviews from Amazon but only bearing rating scores. However, what we need is the content or aspect tags that are being discussed in each review. In addition, our review text is in Chinese. Therefore, it is necessary for us to build the review dataset by ourselves and label them into generic categories, which is one of as one of the contributions of this paper.

### Relevance

Label: 

## Record 0368

Paper: A Surrogate-based Generic Classifier for Chinese TV Series Reviews

### Question

> Is manual annotation performed?

### Passage

> What we need is to classify each review into several generic categories that might be attractive to the readers, so classifier selection is also quite important in our problem. Supervised learning takes labeled training pairs and tries to learn an inferred function, which can be used to predict new samples. In this paper, our selection is based on two kinds of learning, i.e., discriminative and generative learning algorithms. And we choose three typical algorithms to compare. Bayes BIBREF7 , which is the representative of generative learning, will output the class with the highest probability that is generated through the bayes' rule. While for the discriminative classifiers like logistic regression BIBREF8 or Support Vector Machine BIBREF9 , final decisions are based on the classifier's output score, which is compared with some threshold to distinguish between different classes.

### Relevance

Label: 

## Record 0369

Paper: A Surrogate-based Generic Classifier for Chinese TV Series Reviews

### Question

> Is manual annotation performed?

### Passage

> Finally, we are going to train classifiers on top of our reduced generic features. As mentioned above, there are two kinds of learning algorithms, i.e., discriminant and generative classifiers. Based on Bayes rule, the optimal classifier is represented as INLINEFORM0
> 
> where INLINEFORM0 is the prior information we know about class INLINEFORM1 .
> 
> So for generative approach like Bayes, it will try to estimate both INLINEFORM0 and INLINEFORM1 . During testing time, we can just apply the above Bayes rule to predict INLINEFORM2 . Why do we call it naive? Remember that we assume that each feature is conditionally independent with each other. So we have DISPLAYFORM0
> 
> where we made the assumption that there are INLINEFORM0 words being used in our input. If features are binary, for each word INLINEFORM1 we may simply estimate the probability by DISPLAYFORM0
> 
> in which, INLINEFORM0 is a smoothing parameter in case there is no training sample for INLINEFORM1 and INLINEFORM2 outputs the number of a set. With all these probabilities computed, we can make decisions by whether DISPLAYFORM0
> 
> On the other hand, discriminant learning algorithms will estimate INLINEFORM0 directly, or learn some “discriminant” function INLINEFORM1 . Then by comparing INLINEFORM2 with some threshold, we can make the final decision. Here we applied two common classifiers logistic regression and support vector machine to classify movie reviews. Logistic regression squeezes the input feature into some interval between 0 and 1 by the sigmoid function, which can be treated as the probability INLINEFORM3 . DISPLAYFORM0
> 
> The Maximum A Posteriori of logistic regression with Gaussian priors on parameter INLINEFORM0 is defined as below INLINEFORM1
> 
> which is a concave function with respect to INLINEFORM0 , so we can use gradient ascent below to optimize the objective function and get the optimal INLINEFORM1 . DISPLAYFORM0
> 
> where INLINEFORM0 is a positive hyper parameter called learning rate. Then we can just use equation ( EQREF24 ) to distinguish between classes.
> 
> While for Support Vector Machine(SVM), its initial goal is to learn a hyperplane, which will maximize the margin between the two classes' boundary hyperplanes. Suppose the hyperplane we want to learn is INLINEFORM0
> 
> Then the soft-margin version of SVM is INLINEFORM0
> 
> where INLINEFORM0 is the slack variable representing

### Relevance

Label: 

## Record 0370

Paper: A Surrogate-based Generic Classifier for Chinese TV Series Reviews

### Question

> Is manual annotation performed?

### Passage

> is to learn a hyperplane, which will maximize the margin between the two classes' boundary hyperplanes. Suppose the hyperplane we want to learn is INLINEFORM0
> 
> Then the soft-margin version of SVM is INLINEFORM0
> 
> where INLINEFORM0 is the slack variable representing the error w.r.t. datapoint INLINEFORM1 . If we represent the inequality constraints by hinge loss function DISPLAYFORM0
> 
> What we want to minimize becomes DISPLAYFORM0
> 
> which can be solved easily with a Quadratic Programming solver. With learned INLINEFORM0 and INLINEFORM1 , decision is made by determining whether DISPLAYFORM0
> 
> Based on these classifiers, we may also apply some kernel trick function on input feature to make originally linearly non-separable data to be separable on mapped space, which can further improve our classifier performance. What we've tried in our experiments are the polynomial and rbf kernels.

### Relevance

Label: 

## Record 0371

Paper: A Multi-Turn Emotionally Engaging Dialog Model

### Question

> What two baseline models are used?

### Passage

> We use two different dialog corpora to train our model—the Cornell Movie Dialogs Corpus BIBREF20 and the DailyDialog dataset BIBREF21.
> 
> Cornell Movie Dialogs Corpus. The dataset contains 83,097 dialogs (220,579 conversational exchanges) extracted from raw movie scripts. In total there are 304,713 utterances.
> 
> DailyDialog. The dataset is developed by crawling raw data from websites used for language learners to learn English dialogs in daily life. It contains 13,118 dialogs in total.
> 
> We summarize some of the basic information regarding the two datasets in Table TABREF25.
> 
> In our experiments, the models are first trained on the Cornell Movie Dialogs Corpus, and then fine-tuned on the DailyDialog dataset. We adopted this training pattern because the Cornell dataset is bigger but noisier, while DailyDialog is smaller but more daily-based. To create a training set and a validation set for each of the two datasets, we take segments of each dialog with number of turns no more than six, to serve as the training/validation examples. Specifically, for each dialog $\mathbf {D}=(\mathbf {x}_1,\mathbf {x}_2,\dots ,\mathbf {x}_M)$, we create $M-1$ context-response pairs, namely $\mathbf {U}_i=(\mathbf {x}_{s_i},\dots ,\mathbf {x}_i)$ and $\mathbf {y}_i=\mathbf {x}_{i+1}$, for $i=1,2,\dots ,M-1$, where $s_i=\max (1,i-4)$. We filter out those pairs that have at least one utterance with length greater than 30. We also reduce the frequency of those pairs whose responses appear too many times (the threshold is set to 10 for Cornell, and 5 for DailyDialog), to prevent them from dominating the learning procedure. See Table TABREF25 for the sizes of the training and validation sets. The test set consists of 100 dialogs with four turns. We give more detailed description of how we create the test set in Section SECREF31.

### Relevance

Label: 

## Record 0372

Paper: A Multi-Turn Emotionally Engaging Dialog Model

### Question

> What two baseline models are used?

### Passage

> We compared our multi-turn emotionally engaging dialog model (denoted as MEED) with two baselines—the vanilla sequence-to-sequence model (denoted as S2S) and HRAN. We chose S2S and HRAN as baselines because we would like to evaluate our model's capability to keep track of the multi-turn context and to produce emotionally more appropriate responses, respectively. In order to adapt S2S to the multi-turn setting, we concatenate all the history utterances in the context into one.
> 
> For all the models, the vocabulary consists of 20,000 most frequent words in the Cornell and DailyDialog datasets, plus three extra tokens: <unk> for words that do not exist in the vocabulary, <go> indicating the begin of an utterance, and <eos> indicating the end of an utterance. Here we summarize the configurations and parameters of our experiments:
> 
> We set the word embedding size to 256. We initialized the word embeddings in the models with word2vec BIBREF22 vectors first trained on Cornell and then fine-tuned on DailyDialog, consistent with the training procedure of the models.
> 
> We set the number of hidden units of each RNN to 256, the word-level attention depth to 256, and utterance-level 128. The output size of the emotion embedding layer is 256.
> 
> We optimized the objective function using the Adam optimizer BIBREF23 with an initial learning rate of 0.001. We stopped training the models when the lowest perplexity on the validation sets was achieved.
> 
> For prediction, we used beam search BIBREF24 with a beam width of 256.

### Relevance

Label: 

## Record 0373

Paper: A Multi-Turn Emotionally Engaging Dialog Model

### Question

> What two baseline models are used?

### Passage

> To develop a test set for human evaluation, we first selected the emotionally colored dialogs with exactly four turns from the DailyDialog dataset. In the dataset each dialog turn is annotated with a corresponding emotional category, including the neutral one. For our purposes we filtered out only those dialogs where more than a half of utterances have non-neutral emotional labels. This gave us 78 emotionally positive dialogs and 14 emotionally negative dialogs. In order to have a balanced test set with equal number of positive and negative dialogs, we recruited two English-speaking students from our university without any relationship to the authors' lab and instructed them to create five negative dialogs with four turns, as if they were interacting with another human, according to each of the following topics: relationships, entertainment, service, work and study, and everyday situations. Thus each person produced 25 dialogs, and in total we obtained 50 emotionally negative daily dialogs in addition to the 14 already available. To form the test set, we randomly selected 50 emotionally positive and 50 emotionally negative dialogs from the two pools of dialogs described above (78 positive dialogs from DailyDialog, 64 negative dialogs from DailyDialog and human-generated).
> 
> For human evaluation of the models, we recruited another four English-speaking students from our university without any relationship to the authors' lab to rate the responses generated by the models. Specifically, we randomly shuffled the 100 dialogs in the test set, then we used the first three utterances of each dialog as the input to the three models being compared and let them generate the responses. According to the context given, the raters were instructed to evaluate the quality of the responses based on three criteria: (1) grammatical correctness—whether or not the response is fluent and free of grammatical mistakes; (2) contextual coherence—whether or not the response is context sensitive to the previous dialog history; (3) emotional appropriateness—whether or not the response conveys the right emotion and feels as if it had been produced by a human. For each criterion, the raters gave scores of either 0, 1 or 2, where 0 means bad, 2 means good, and 1 indicates neutral.

### Relevance

Label: 

## Record 0374

Paper: A Multi-Turn Emotionally Engaging Dialog Model

### Question

> What two baseline models are used?

### Passage

> We present four sample dialogs in Table TABREF36, along with the responses generated by the three models. Dialog 1 and 2 are emotionally positive and dialog 3 and 4 are negative. For the first two examples, we can see that MEED is able to generate more emotional content (like “fun” and “congratulations”) that is appropriate according to the context. For dialog 4, MEED responds in sympathy to the other speaker, which is consistent with the second utterance in the context. On the contrary, HRAN poses a question in reply, contradicting the dialog history.

### Relevance

Label: 

## Record 0375

Paper: A Multi-Turn Emotionally Engaging Dialog Model

### Question

> What two baseline models are used?

### Passage

> Table TABREF34 gives the perplexity scores obtained by the three models on the two validation sets and the test set. As shown in the table, MEED achieves the lowest perplexity score on all three sets. We also conducted t-test on the perplexity obtained, and results show significant improvements (with $p$-value $<0.05$).
> 
> Table TABREF34, TABREF35 and TABREF35 summarize the human evaluation results on the responses' grammatical correctness, contextual coherence, and emotional appropriateness, respectively. In the tables, we give the percentage of votes each model received for the three scores, the average score obtained with improvements over S2S, and the agreement score among the raters. Note that we report Fleiss' $\kappa $ score BIBREF27 for contextual coherence and emotional appropriateness, and Finn's $r$ score BIBREF28 for grammatical correctness. We did not use Fleiss' $\kappa $ score for grammatical correctness. As agreement is extremely high, this can make Fleiss' $\kappa $ very sensitive to prevalence BIBREF29. On the contrary, we did not use Finn's $r$ score for contextual coherence and emotional appropriateness because it is only reasonable when the observed variance is significantly less than the chance variance BIBREF30, which did not apply to these two criteria. As shown in the tables, we got high agreement among the raters for grammatical correctness, and fair agreement among the raters for contextual coherence and emotional appropriateness. For grammatical correctness, all three models achieved high scores, which means all models are capable of generating fluent utterances that make sense. For contextual coherence and emotional appropriateness, MEED achieved higher average scores than S2S and HRAN, which means MEED keeps better track of the context and can generate responses that are emotionally more appropriate and natural. We conducted Friedman test BIBREF31 on the human evaluation results, showing the improvements of MEED are significant (with $p$-value $<0.01$).

### Relevance

Label: 

## Record 0376

Paper: Predicting the Role of Political Trolls in Social Media

### Question

> How large is the dataset?

### Passage

> BERT offers state-of-the-art text embeddings based on the Transformer BIBREF72. We use the pre-trained BERT-large, uncased model, which has 24-layers, 1024-hidden, 16-heads, and 340M parameters, which yields output embeddings with 768 dimensions. Given a tweet, we generate an embedding for it by averaging the representations of the BERT tokens from the penultimate layer of the neural network. To obtain a representation for a user, we average the embeddings of all their tweets. The embeddings extracted from the text capture how similar users are according to their use of language.

### Relevance

Label: 

## Record 0377

Paper: Predicting the Role of Political Trolls in Social Media

### Question

> How large is the dataset?

### Passage

> techniques and link analysis BIBREF37. It has been also shown that sockpuppets differ from ordinary users in their posting behavior, linguistic traits, and social network structure BIBREF4.
> 
> Internet Water Army is a literal translation of the Chinese term wangluo shuijun, which is a metaphor for a large number of people who are well organized to flood the Internet with purposeful comments and articles. Internet water army has been allegedly used in China by the government (also known as 50 Cent Party) as well as by a number of private organizations.
> 
> Astroturfing is an effort to simulate a political grass-roots movement. It has attracted strong interest from political science, and research on it has focused on massive streams of microblogging data BIBREF6.
> 
> Identification of malicious accounts in social media includes detecting spam accounts BIBREF38, BIBREF39, fake accounts BIBREF40, BIBREF41, compromised and phishing accounts BIBREF42. Fake profile detection has also been studied in the context of cyber-bullying BIBREF43. A related problem is that of Web spam detection, which has been addressed as a text classification problem BIBREF44, e.g., using spam keyword spotting BIBREF45, lexical affinity of arbitrary words to spam content BIBREF46, frequency of punctuation and word co-occurrence BIBREF47.
> 
> Trustworthiness of online statements is an emerging topic, given the interest in fake news BIBREF48. It is related to trolls, as they often engage in opinion manipulation and spread rumors BIBREF49. Research topics include predicting the credibility of information in social media BIBREF50, BIBREF51, BIBREF52, BIBREF53 and political debates BIBREF54, BIBREF55, BIBREF56, and stance classification BIBREF57.
> 
> For example, BIBREF58 leverage user reputation, author writing style, and various time-based features, BIBREF59 analyze the interaction of content and social network structure, and BIBREF60 studied how Twitter users judge truthfulness. BIBREF61 study how people handle rumors in social media, and found that users with higher reputation are more trusted, and thus can spread rumors easily. BIBREF62 use temporal patterns to detect rumors and to predict their frequency, and BIBREF61 focus on conversational threads. More recent work has focused on the credibility and the factuality in community forums BIBREF63, BIBREF64, BIBREF65, BIBREF23.

### Relevance

Label: 

## Record 0378

Paper: Predicting the Role of Political Trolls in Social Media

### Question

> How large is the dataset?

### Passage

> We have proposed a novel approach to analyze the behavior patterns of political trolls according to their political leaning (left vs. news feed vs. right) using features from social media, i.e., from Twitter. We experimented with two scenarios: (i) supervised learning, where labels for trolls are provided, and (ii) distant supervision, where such labels are not available, and we rely on more common labels for news outlets cited by the trolls. Technically, we leveraged the community structure and the text of the messages in the online social network of trolls represented as a graph, from which we extracted several types of representations, i.e., embeddings, for the trolls. Our experiments on the “IRA Russian Troll” dataset have shown improvements over the state-of-the-art in the supervised scenario, while providing a compelling case for the distant-supervision scenario, which has not been explored before.
> 
> In future work, we plan to apply our methodology to other political events such as Brexit as well as to other election campaigns around the world, in connection to which large-scale troll campaigns have been revealed. We further plan experiments with other graph embedding methods, and with other social media. Finally, the relationship between media bias and troll's political role that we have highlighted in this paper is extremely interesting. We have shown how to use it to go from the media-space to the user-space and vice-versa, but so far we have just scratched the surface in terms of understanding of the process that generated these data and its possible applications.

### Relevance

Label: 

## Record 0379

Paper: Predicting the Role of Political Trolls in Social Media

### Question

> How large is the dataset?

### Passage

> We build a bipartite, undirected User-to-Hashtag (U2H) graph, where nodes are users and hashtags, and there is an edge $(u,h)$ between a user node $u$ and a hashtag node $h$ if user $u$ uses hashtag $h$ in their tweets. This graph is bipartite as there are no edges connecting two user nodes or two hashtag nodes. We run node2vec BIBREF67 on this graph, and we extract the embeddings for the users (we ignore the hashtag embeddings). We use 128 dimensions for the output embeddings. These embeddings capture how similar troll users are based on their usage of hashtags.

### Relevance

Label: 

## Record 0380

Paper: Predicting the Role of Political Trolls in Social Media

### Question

> How large is the dataset?

### Passage

> We build an undirected User-to-Mentioned-User (U2M) graph, where the nodes are users, and there is an edge $(u,v)$ between two nodes if user $u$ mentions user $v$ in their tweets (i.e., $u$ has authored a tweet that contains “@$v$” ). We run node2vec on this graph and we extract the embeddings for the users. As we are interested only in the troll users, we ignore the embeddings of users who are only mentioned by other trolls. We use 128 dimensions for the output embeddings. The embeddings extracted from this graph capture how similar troll users are according to the targets of their discussions on the social network.

### Relevance

Label: 

## Record 0381

Paper: Modeling Conversation Structure and Temporal Dynamics for Jointly Predicting Rumor Stance and Veracity

### Question

> How do they split the dataset when training and evaluating their models?

### Passage

> To evaluate our proposed method, we conduct experiments on two benchmark datasets.
> 
> The first is SemEval-2017 task 8 BIBREF16 dataset. It includes 325 rumorous conversation threads, and has been split into training, development and test sets. These threads cover ten events, and two events of that only appear in the test set. This dataset is used to evaluate both stance classification and veracity prediction tasks.
> 
> The second is PHEME dataset BIBREF48. It provides 2,402 conversations covering nine events. Following previous work, we conduct leave-one-event-out cross-validation: in each fold, one event's conversations are used for testing, and all the rest events are used for training. The evaluation metric on this dataset is computed after integrating the outputs of all nine folds. Note that only a subset of this dataset has stance labels, and all conversations in this subset are already contained in SemEval-2017 task 8 dataset. Thus, PHEME dataset is used to evaluate veracity prediction task.
> 
> Table TABREF19 shows the statistics of two datasets. Because of the class-imbalanced problem, we use macro-averaged $F_1$ as the evaluation metric for two tasks. We also report accuracy for reference.

### Relevance

Label: 

## Record 0382

Paper: Modeling Conversation Structure and Temporal Dynamics for Jointly Predicting Rumor Stance and Veracity

### Question

> How do they split the dataset when training and evaluating their models?

### Passage

> We vary the value of $\lambda $ in the joint loss $\mathcal {L}$ and train models with various $\lambda $ to show the interrelation between stance and veracity in Figure FIGREF31. As $\lambda $ increases from 0.0 to 1.0, the performance of identifying $false$ and $unverified$ rumors generally gains. Therefore, when the supervision signal of stance classification becomes strong, the learned stance features can produce more accurate clues for predicting rumor veracity.

### Relevance

Label: 

## Record 0383

Paper: Modeling Conversation Structure and Temporal Dynamics for Jointly Predicting Rumor Stance and Veracity

### Question

> How do they split the dataset when training and evaluating their models?

### Passage

> property in conversations to learn tweet representations.
> 
> After determining the stances of people's reactions, another challenge is how we can utilize public stances to predict rumor veracity accurately. We observe that the temporal dynamics of public stances can indicate rumor veracity. Figure FIGREF2 illustrates the stance distributions of tweets discussing $true$ rumors, $false$ rumors, and $unverified$ rumors, respectively. As we can see, $supporting$ stance dominates the inception phase of spreading. However, as time goes by, the proportion of $denying$ tweets towards $false$ rumors increases quite significantly. Meanwhile, the proportion of $querying$ tweets towards $unverified$ rumors also shows an upward trend. Based on this observation, we propose to model the temporal dynamics of stance evolution with a recurrent neural network (RNN), capturing the crucial signals containing in stance features for effective veracity prediction.
> 
> Further, most existing methods tackle stance classification and veracity prediction separately, which is suboptimal and limits the generalization of models. As shown previously, they are two closely related tasks in which stance classification can provide indicative clues to facilitate veracity prediction. Thus, these two tasks can be jointly learned to make better use of their interrelation.
> 
> Based on the above considerations, in this paper, we propose a hierarchical multi-task learning framework for jointly predicting rumor stance and veracity, which achieves deep integration between the preceding task (stance classification) and the subsequent task (veracity prediction). The bottom component of our framework classifies the stances of tweets in a conversation discussing a rumor via aggregation-based structure modeling, and we design a novel graph convolution operation customized for conversation structures. The top component predicts rumor veracity by exploiting the temporal dynamics of stance evolution, taking both content features and stance features learned by the bottom component into account. Two components are jointly trained to utilize the interrelation between the two tasks for learning more powerful feature representations.
> 
> The contributions of this work are as follows.
> 
> $\bullet $ We propose a hierarchical framework to tackle rumor stance classification and veracity prediction jointly, exploiting both structural characteristic and temporal dynamics in rumor spreading process.
> 
> $\bullet $ We design a novel graph convolution operation customized to encode conversation structures for learning stance features. To our knowledge, we are the

### Relevance

Label: 

## Record 0384

Paper: Modeling Conversation Structure and Temporal Dynamics for Jointly Predicting Rumor Stance and Veracity

### Question

> How do they split the dataset when training and evaluating their models?

### Passage

> To show the effect of our customized graph convolution operation (Eq. (DISPLAY_FORM7)) for modeling conversation structures, we further compare it with the original graph convolution (Eq. (DISPLAY_FORM6), named Original-GCN) on stance classification task.
> 
> Specifically, we cluster tweets in the test set according to their depths in the conversation threads (e.g., the cluster “depth = 0” consists of all source tweets in the test set). For BranchLSTM, Original-GCN and Conversational-GCN, we report their macro-averaged $F_1$ on each cluster in Figure FIGREF28.
> 
> We observe that our Conversational-GCN outperforms Original-GCN and BranchLSTM significantly in most levels of depth. BranchLSTM may prefer to “shallow” tweets in a conversation because they often occur in multiple branches (e.g., in Figure FIGREF1, the tweet “2” occurs in two branches and thus it will be modeled twice). The results indicate that Conversational-GCN has advantage to identify stances of “deep” tweets in conversations.

### Relevance

Label: 

## Record 0385

Paper: Modeling Conversation Structure and Temporal Dynamics for Jointly Predicting Rumor Stance and Veracity

### Question

> How do they split the dataset when training and evaluating their models?

### Passage

> To evaluate our framework Hierarchical-PSV, we consider two groups of baselines: single-task and multi-task baselines.
> 
> Single-task Baselines In single-task setting, stance labels are not available. Only veracity labels can be used to supervise the training process.
> 
> $\bullet $ TD-RvNN BIBREF37 models the top-down tree structure using a recursive neural network for veracity classification.
> 
> $\bullet $ Hierarchical GCN-RNN is the single-task variant of our framework: we optimize $\mathcal {L}_{\rm {veracity}}$ (i.e., $\lambda =0$ in Eq. (DISPLAY_FORM16)) during training. Thus, the bottom Conversational-GCN only has indirect supervision (veracity labels) to learn stance features.
> 
> Multi-task Baselines In multi-task setting, both stance labels and veracity labels are available for training.
> 
> $\bullet $ BranchLSTM+NileTMRG BIBREF41 is a pipeline method, combining the winner systems of two subtasks in SemEval-2017 shared task 8. It first trains a BranchLSTM for stance classification, and then uses the predicted stance labels as extra features to train an SVM for veracity prediction BIBREF38.
> 
> $\bullet $ MTL2 (Veracity+Stance) BIBREF41 is a multi-task learning method that adopts BranchLSTM as the shared block across tasks. Then, each task has a task-specific output layer, and two tasks are jointly learned.
> 
> Performance Comparison Table TABREF23 shows the comparisons of different methods. By comparing single-task methods, Hierarchical GCN-RNN performs better than TD-RvNN, which indicates that our hierarchical framework can effectively model conversation structures to learn high-quality tweet representations. The recursive operation in TD-RvNN is performed in a fixed direction and runs over all tweets, thus may not obtain enough useful information. Moreover, the training speed of Hierarchical GCN-RNN is significantly faster than TD-RvNN: in the condition of batch-wise optimization for training one step over a batch containing 32 conversations, our method takes only 0.18 seconds, while TD-RvNN takes 5.02 seconds.
> 
> Comparisons among multi-task methods show that two joint methods outperform the pipeline method (BranchLSTM+NileTMRG), indicating that jointly learning two tasks can improve the generalization through leveraging the interrelation between them. Further, compared with MTL2 which uses a “parallel” architecture to make predictions for two tasks, our Hierarchical-PSV performs better than MTL2. The hierarchical architecture is more effective to tackle the joint predictions of rumor stance and veracity, because it not only possesses the advantage of parameter-sharing but also offers deep integration of

### Relevance

Label: 

## Record 0386

Paper: MCScript: A Novel Dataset for Assessing Machine Comprehension Using Script Knowledge

### Question

> what dataset statistics are provided?

### Passage

> Machine comprehension datasets consist of three main components: texts, questions and answers. In this section, we describe our data collection for these 3 components. We first describe a series of pilot studies that we conducted in order to collect commonsense inference questions (Section SECREF4 ). In Section SECREF5 , we discuss the resulting data collection of questions, texts and answers via crowdsourcing on Amazon Mechanical Turk (henceforth MTurk). Section SECREF17 gives information about some necessary postprocessing steps and the dataset validation. Lastly, Section SECREF19 gives statistics about the final dataset.

### Relevance

Label: 

## Record 0387

Paper: MCScript: A Novel Dataset for Assessing Machine Comprehension Using Script Knowledge

### Question

> what dataset statistics are provided?

### Passage

> As can be seen from the data statistics, our mode of collection leads to a substantial proportion of questions that require inference using commonsense knowledge. Still, the dataset contains a large number of questions in which the answer is explicitly contained or implied by the text: Figure FIGREF22 shows passages from an example text of the dataset together with two such questions. For question Q1, the answer is given literally in the text. Answering question Q2 is not as simple; it can be solved, however, via standard semantic relatedness information (chicken and hotdogs are meat; water, soda and juice are drinks).
> 
> The following cases require commonsense inference to be decided. In all these cases, the answers are not overtly contained nor easily derivable from the respective texts. We do not show the full texts, but only the scenario names for each question.
> 
> Example UID23 refers to a library setting. Script knowledge helps in assessing that usually, paying is not an event when borrowing a book, which answers the question. Similarly, event information helps in answering the questions in Examples UID24 and UID25 . In Example UID26 , knowledge about the typical role of parents in the preparation of a picnic will enable a plausibility decision. Similarly, in Example UID27 , it is commonsense knowledge that showers usually take a few minutes rather than hours.
> 
> There are also cases in which the answer can be inferred from the text, but where commonsense knowledge is still beneficial: The text for example UID28 does not contain the information that breakfast is eaten in the morning, but it could still be inferred from many pointers in the text (e.g. phrases such as I woke up), or from commonsense knowledge.
> 
> These few examples illustrate that our dataset covers questions with a wide spectrum of difficulty, from rather simple questions that can be answered from the text to challenging inference problems.

### Relevance

Label: 

## Record 0388

Paper: MCScript: A Novel Dataset for Assessing Machine Comprehension Using Script Knowledge

### Question

> what dataset statistics are provided?

### Passage

> For all experiments, we admitted only experienced MTurk workers who are based in the US. One HIT consisted of writing one text for the text collection, formulating 15 questions for the question collection, or finding 15 pairs of answers for the answer collection. We paid $0.50 per HIT for the text and question collection, and $0.60 per HIT for the answer collection.
> 
> More than 2,100 texts were paired with 15 questions each, resulting in a total number of approx. 32,000 annotated questions. For 13% of the questions, the workers did not agree on one of the 4 categories with a 3 out of 5 majority, so we did not include these questions in our dataset.
> 
> The distribution of category labels on the remaining 87% is shown in Table TABREF10 . 14,074 (52%) questions could be answered. Out of the answerable questions, 10,160 could be answered from the text directly (text-based) and 3,914 questions required the use of commonsense knowledge (script-based). After removing 135 questions during the validation, the final dataset comprises 13,939 questions, 3,827 of which require commonsense knowledge (i.e. 27.4%). This ratio was manually verified based on a random sample of questions.
> 
> We split the dataset into training (9,731 questions on 1,470 texts), development (1,411 questions on 219 texts), and test set (2,797 questions on 430 texts). Each text appears only in one of the three sets. The complete set of texts for 5 scenarios was held out for the test set. The average text, question, and answer length is 196.0 words, 7.8 words, and 3.6 words, respectively. On average, there are 6.7 questions per text.
> 
> Figure FIGREF21 shows the distribution of question types in the dataset, which we identified using simple heuristics based on the first words of a question: Yes/no questions were identified as questions starting with an auxiliary or modal verb, all other question types were determined based on the question word.
> 
> We found that 29% of all questions are yes/no questions. Questions about details of a situation (such as what/ which and who) form the second most frequent question category. Temporal questions (when and how long/often) form approx. 11% of all questions. We leave a more detailed analysis of question

### Relevance

Label: 

## Record 0389

Paper: MCScript: A Novel Dataset for Assessing Machine Comprehension Using Script Knowledge

### Question

> what dataset statistics are provided?

### Passage

> collection of (1) narrative texts, (2) questions of various types referring to these texts, and (3) pairs of answer candidates for each question. It comprises approx. 2,100 texts and a total of approx. 14,000 questions. Answering a substantial subset of questions requires knowledge beyond the facts mentioned in the text, i.e. it requires inference using commonsense knowledge about everyday activities. An example is given in Figure FIGREF2 . For both questions, the correct choice for an answer requires commonsense knowledge about the activity of planting a tree, which goes beyond what is mentioned in the text. Texts, questions, and answers were obtained through crowdsourcing. In order to ensure high quality, we manually validated and filtered the dataset. Due to our design of the data acquisition process, we ended up with a substantial subset of questions that require commonsense inference (27.4%).

### Relevance

Label: 

## Record 0390

Paper: MCScript: A Novel Dataset for Assessing Machine Comprehension Using Script Knowledge

### Question

> what dataset statistics are provided?

### Passage

> As a starting point for our pilots, we made use of texts from the InScript corpus BIBREF10 , which provides stories centered around everyday situations (see Section SECREF7 ). We conducted three different pilot studies to determine the best way of collecting questions that require inference over commonsense knowledge:
> 
> The most intuitive way of collecting reading comprehension questions is to show texts to workers and let them formulate questions and answers on the texts, which is what we tried internally in a first pilot. Since our focus is to provide an evaluation framework for inference over commonsense knowledge, we manually assessed the number of questions that indeed require common sense knowledge. We found too many questions and answers collected in this manner to be lexically close to the text.
> 
> In a second pilot, we investigated the option to take the questions collected for one text and show them as questions for another text of the same scenario. While this method resulted in a larger number of questions that required inference, we found the majority of questions to not make sense at all when paired with another text. Many questions were specific to a text (and not to a scenario), requiring details that could not be answered from other texts. Since the two previous pilot setups resulted in questions that centered around the texts themselves, we decided for a third pilot to not show workers any specific texts at all. Instead, we asked for questions that centered around a specific script scenario (e.g. eating in a restaurant). We found this mode of collection to result in questions that have the right level of specificity for our purposes: namely, questions that are related to a scenario and that can be answered from different texts (about that scenario), but for which a text does not need to provide the answer explicitly.
> 
> The next section will describe the mode of collection chosen for the final dataset, based on the third pilot, in more detail.

### Relevance

Label: 

## Record 0391

Paper: Application of Pre-training Models in Named Entity Recognition

### Question

> which was the worst performing model?

### Passage

> We conducted experiments on Chinese NER datasets to demonstrate the effectiveness of the pre-training models specified in section III. For the dataset, we used the MSRA-2006 published by Microsoft Research Asia.
> 
> The experiments were conducted on the AI Studio platform launched by the Baidu. This platform has a build-in deep learning framework PaddlePaddle and is equipped with a V100 GPU. The pre-training models mentioned above were downloaded by PaddleHub, which is a pre-training model management toolkit. It is also launched by the Baidu. For hyper-parameter configuration, we adjusted them according to the performance on development sets. In this article, the number of the epoch is 2, the learning rate is 5e-5, and the batch size is 16.
> 
> The BiGRU+CRF model was used as the baseline model. Table I shows that the baseline model has already achieved an F1 value of 90.32. However, using the pre-training models can significantly increase F1 values by 1 to 2 percentage points except for ERNIE-tiny model. Among the pre-training models, the RoBERTa model achieves the highest F1 value of 94.17, while the value of ERNIE-tiny is relatively low, even 4 percentage points lower than the baseline model.

### Relevance

Label: 

## Record 0392

Paper: Application of Pre-training Models in Named Entity Recognition

### Question

> which was the worst performing model?

### Passage

> This section discusses the experimental results in detail. We will analyze the different model structures and pre-training tasks on the effect of the NER task.
> 
> First of all, it is shown that the deeper the layer, the better the performance. All pre-training models have 12 Transformer layers, except ERNIE2.0-tiny. Although Ernie2.0-tiny increases the number of hidden units and improves the pre-training task with continual pre-training, 3 Transformer layers can not extract semantic knowledge well. The F1 value of ERNIE-2.0-tiny is even lower than the baseline model.
> 
> Secondly, for pre-training models with the same model structure, RoBERTa obtained the result of SOTA. BERT and ERNIE retain the sentence pre-training tasks of NSP and DLM respectively, while RoBERTa removes the sentence-level pre-training task because Liu $et$ $al$. BIBREF9 hypothesizes the model can not learn long-range dependencies. The results confirm the above hypothesis. For the NER task, sentence-level pre-training tasks do not improve performance. In contrast, RoBERTa removes the NSP task and improves the performance of entity recognition. As described by Liu $et$ $al$. BIBREF9, the NSP and the MLP are designed to improve the performance on specific downstream tasks, such as the SQuAD 1.1, which requires reasoning about the relationships between pairs of sentences. However, the results show that the NER task does not rely on sentence-level knowledge, and using sentence-level pre-training tasks hurts performance because the pre-training models may not able to learn long-range dependencies.
> 
> Moreover, as mentioned before, RoBERTa could adapt to different masking strategies and acquires richer semantic representations with the dynamic masking strategy. In contrast, BERT and ERNIE use the static masking strategy in every epoch. In addition, the results in this paper show that the F1 value of ERNIE is slightly lower than BERT. We infer that ERNIE may introduce segmentation errors when performing entity-level and phrase-level masking.

### Relevance

Label: 

## Record 0393

Paper: Application of Pre-training Models in Named Entity Recognition

### Question

> which was the worst performing model?

### Passage

> This research was funded by the major special project of Anhui Science and Technology Department (Grant: 18030801133) and Science and Technology Service Network Initiative (Grant: KFJ-STS-ZDTP-079).

### Relevance

Label: 

## Record 0394

Paper: Application of Pre-training Models in Named Entity Recognition

### Question

> which was the worst performing model?

### Passage

> ERNIE is also a pre-training language model. In addition to a basic-level masking strategy, unlike BERT, ERNIE using entity-level and phrase-level masking strategies to obtain the language representations enhanced by knowledge BIBREF8.
> 
> ERNIE has the same model structure as BERT-base, which uses 12 Transformer encoder layers, 768 hidden units and 12 attention heads.
> 
> As mentioned above, ERNIE using three masking strategies: basic-level masking, phrase-level masking, and entity-level masking. the basic-level making is to mask a character and train the model to predict it. Phrase-level and entity-level masking are to mask a phrase or an entity and predict the masking part. In addition, ERNIE also performs the "Dialogue Language Model (DLM)" task to judge whether a multi-turn conversation is real or fake BIBREF8.

### Relevance

Label: 

## Record 0395

Paper: Application of Pre-training Models in Named Entity Recognition

### Question

> which was the worst performing model?

### Passage

> Named entity recognition (NER) is the basic task of the NLP, such as information extraction and data mining. The main goal of the NER is to extract entities (persons, places, organizations and so on) from unstructured documents. Researchers have used rule-based and dictionary-based methods for the NERBIBREF1. Because these methods have poor generalization properties, researchers have proposed machine learning methods, such as Hidden Markov Model (HMM) and Conditional Random Field (CRF)BIBREF2BIBREF10. But machine learning methods require a lot of artificial features and can not avoid costly feature engineering. In recent years, deep learning, which is driven by artificial intelligence and cognitive computing, has been widely used in multiple NLP fields. Huang $et$ $al$. BIBREF3 proposed a model that combine the Bidirectional Long Short-Term Memory (BiLSTM) with the CRF. It can use both forward and backward input features to improve the performance of the NER task. Ma and Hovy BIBREF11 used a combination of the Convolutional Neural Networks (CNN) and the LSTM-CRF to recognize entities. Chiu and Nichols BIBREF12 improved the BiLSTM-CNN model and tested it on the CoNLL-2003 corpus.

### Relevance

Label: 

## Record 0396

Paper: CM-Net: A Novel Collaborative Memory Network for Spoken Language Understanding

### Question

> What is the source of the CAIS dataset?

### Passage

> SNIPS Natural Language Understanding benchmark BIBREF11 is collected in a crowsourced fashion by Snips. The intents of this dataset are more balanced when compared with the ATIS. We split another 700 utterances for validation set following previous works BIBREF7, BIBREF9.

### Relevance

Label: 

## Record 0397

Paper: CM-Net: A Novel Collaborative Memory Network for Spoken Language Understanding

### Question

> What is the source of the CAIS dataset?

### Passage

> exchange among the task-specific features referred from memories, local context representations and global sequential information via the well-designed block, named CM-block, which consists of three computational components:
> 
> Deliberate Attention: Obtaining slot-specific and intent-specific representations from memories in a collaborative manner.
> 
> Local Calculation: Updating local context representations with the guidances of the referred slot and intent representations in the previous Deliberate Attention.
> 
> Global Recurrence: Generating specific (slot and intent) global sequential representations based on local context representations from the previous Local Calculation.
> 
> Above components in each CM-block are conducted consecutively, which are responsible for encoding information from different perspectives. Finally, multiple CM-blocks are stacked together, and construct our CM-Net. We firstly conduct experiments on two popular benchmarks, SNIPS BIBREF11 and ATIS BIBREF12, BIBREF13. Experimental results show that the CM-Net achieves the state-of-the-art results in 3 of 4 criteria (e.g., intent detection accuracy on ATIS) on both benchmarks. Additionally, trials on our self-collected dataset, named CAIS, demonstrate the effectiveness and generalizability of the CM-Net.
> 
> Our main contributions are as follows:
> 
> We propose a novel CM-Net for SLU, which explicitly captures semantic correlations among words, slots and intents in a collaborative manner, and incrementally enriches the specific features, local context representations and global sequential representations through stacked CM-blocks.
> 
> Our CM-Net achieves the state-of-the-art results on two major SLU benchmarks (ATIS and SNIPS) in most of criteria.
> 
> We contribute a new corpus CAIS with manual annotations of slot tags and intent labels to the research community.

### Relevance

Label: 

## Record 0398

Paper: CM-Net: A Novel Collaborative Memory Network for Spoken Language Understanding

### Question

> What is the source of the CAIS dataset?

### Passage

> We propose a novel $\mathbf {C}$ollaborative $\mathbf {M}$emory $\mathbf {N}$etwork (CM-Net) for jointly modeling slot filling and intent detection. The CM-Net is able to explicitly capture the semantic correlations among words, slots and intents in a collaborative manner, and incrementally enrich the information flows with local context and global sequential information. Experiments on two standard benchmarks and our CAIS corpus demonstrate the effectiveness and generalizability of our proposed CM-Net. In addition, we contribute the new corpus (CAIS) to the research community.

### Relevance

Label: 

## Record 0399

Paper: CM-Net: A Novel Collaborative Memory Network for Spoken Language Understanding

### Question

> What is the source of the CAIS dataset?

### Passage

> We conduct experiments on our self-collected CAIS to evaluate the generalizability in different language. We apply two baseline models for comparison, one is the popular BiLSTMs + CRF architecture BIBREF36 for sequence labeling task, and the other one is the more powerful sententce-state LSTM BIBREF21. The results listed in Table TABREF50 demonstrate the generalizability and effectiveness of our CM-Net when handling various domains and different languages.

### Relevance

Label: 

## Record 0400

Paper: CM-Net: A Novel Collaborative Memory Network for Spoken Language Understanding

### Question

> What is the source of the CAIS dataset?

### Passage

> We collect utterances from the $\mathbf {C}$hinese $\mathbf {A}$rtificial $\mathbf {I}$ntelligence $\mathbf {S}$peakers (CAIS), and annotate them with slot tags and intent labels. The training, validation and test sets are split by the distribution of intents, where detailed statistics are provided in the supplementary material. Since the utterances are collected from speaker systems in the real world, intent labels are partial to the PlayMusic option. We adopt the BIOES tagging scheme for slots instead of the BIO2 used in the ATIS, since previous studies have highlighted meaningful improvements with this scheme BIBREF30 in the sequence labeling field.

### Relevance

Label: 
