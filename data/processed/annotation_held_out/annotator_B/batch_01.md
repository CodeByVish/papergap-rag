# Passage relevance annotation

Annotator: 

Judge whether the passage provides information that helps answer the question, including useful partial evidence. Topic overlap alone is not sufficient. Judge only the supplied question and passage.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Do not change record numbers, questions or passages. Work independently without consulting another annotator or reference answers.

## Record 0001

Paper: Extreme Language Model Compression with Optimal Subwords and Shared Projections

### Question

> Why are prior knowledge distillation techniques models are ineffective in producing student models with vocabularies different from the original teacher models?  

### Passage

> We follow the general knowledge distillation paradigm of training a small student model from a large teacher model. Our teacher model is a 12-layer uncased BERTBASE, trained with 30522 WordPiece tokens and 768-dimensional embeddings and hidden states. We denote the teacher model parameters by $\theta _{t}$. Our student model consists of an equal number of transformer layers with parameters denoted by $\theta _{s}$, but with a smaller vocabulary as well as embedding/hidden dimensions, illustrated in Figure FIGREF4. Using the same WordPiece algorithm and training corpus as BERT, we obtain a vocabulary of 4928 WordPieces, which we use for the student model.
> 
> WordPiece tokens BIBREF14 are sub-word units obtained by applying a greedy segmentation algorithm to the training corpus: a desired number (say, $D$) of WordPieces are chosen such that the segmented corpus is minimal in the number of WordPieces used. A cursory look at both vocabularies reveals that $93.9\%$ of the WordPieces in the student vocabulary also exist in the teacher vocabulary, suggesting room for a reduction in the WordPiece vocabulary size from 30K tokens.
> 
> Since we seek to train a general-purpose student language model, we elect to reuse the teacher model's original training objective to optimize the student model, i.e., masked language modeling and next sentence prediction, before any fine-tuning. In the former task, words in context are randomly masked, and the language model needs to predict those words given the masked context. In the latter task, given a pair of sentences, the language model predicts whether the pair is consistent.
> 
> However, since the student vocabulary is not a complete subset of the teacher vocabulary, the two vocabularies may tokenize the same words differently. As a result, the outputs of the teacher and student model for the masked language modeling task may not align. Even with the high overlap between the two vocabularies, the need to train the student embedding from scratch, and the change in embedding dimension precludes existing knowledge distillation techniques, which rely on the alignment of both models' output spaces. As a result, we explore two alternative approaches that enable implicit transfer of knowledge to the student model, which we describe below.

### Relevance

Label: 

## Record 0002

Paper: Extreme Language Model Compression with Optimal Subwords and Shared Projections

### Question

> Why are prior knowledge distillation techniques models are ineffective in producing student models with vocabularies different from the original teacher models?  

### Passage

> Shared projections and model performance: We see that for downstream task performance, dual training still consistently improves upon the direct fine-tuning approach for virtually all experiments. The effect of shared variable projection, however, is less pronounced, with consistent improvements visible only for MRPC and for the 48-dimensional models i.e. the smallest dataset and models respectively in our experiments. This aligns with our intuition for variable projection as a more direct way to provide a training signal from the teacher model internals, which can assume more importance for a low-data or small-model scenario. However, for larger models and more data, the linear projection of parameters may be reducing the degrees of freedom available to the model, since linear projection is a fairly simple function to align the teacher and student parameter spaces.
> 
> A related comparison of interest is between up-projection and down-projection of the model variables: we note up-projection does visibly better on the language modeling task and slightly better on the downstream tasks. The parameters of a well-trained teacher model represent a high-quality local minimum in the teacher space, which may be easier to search for during up-projection.
> 
> Vocabulary size tradeoffs: Issues with input vocabulary size are peculiar to problems in natural language processing: they do not always apply to other areas such as computer vision, where a small fixed number of symbols can encode most inputs. There has been some work on reducing input vocabulary sizes for NLP, but typically not targeting model compression. One concern with reducing the vocabularies of NLP models is it pushes the average tokenized sequence lengths up, making model training harder. In this work, however, we consider classification tasks on shorter texts, which are not as affected by input sequence lengths as, say, tasks such as machine translation are. Furthermore, many real-world applications revolve around short text inputs, which is why a better trade-off between vocabulary size and sequence lengths may be worthwhile for such applications.
> 
> Order of distillation and fine-tuning: Most of the existing work on distilling language models such as BERT and reporting results on downstream tasks, including some of the baselines in this work, first fine-tune a teacher model on the downstream tasks, and then distill

### Relevance

Label: 

## Record 0003

Paper: Extreme Language Model Compression with Optimal Subwords and Shared Projections

### Question

> Why are prior knowledge distillation techniques models are ineffective in producing student models with vocabularies different from the original teacher models?  

### Passage

> Table TABREF20 contains masked word prediction accuracy figures for the different models and the NoKD baseline. We observe that dual training significantly improves over the baseline for all model dimensions, and that both shared projection losses added to dual training further improve the word prediction accuracy. It is interesting to note that for all model dimensions, SharedProjUp projecting into the teacher space outperforms SharedProjDown, significantly so for dimension 48. Expectedly, there is a noticeable performance drop going from 192 to 96 to 48-dimensional hidden state models. Note that because of the differing teacher and student model vocabularies, masked word prediction accuracy for the teacher BERTBASE model is not directly comparable with the student models.
> 
> Table TABREF21 shows results on the downstream language understanding tasks, as well as model sizes, for our approaches, the BERTBASE teacher model, and the PKD and NoKD baselines. We note that models trained with our proposed approaches perform strongly and consistently improve upon the identically parametrized NoKD baselines, indicating that the dual training and shared projection techniques are effective, without incurring significant losses against the BERTBASE teacher model. Comparing with the PKD baseline, our 192-dimensional models, achieving a higher compression rate than either of the PKD models, perform better than the 3-layer PKD baseline and are competitive with the larger 6-layer baseline on task accuracy while being nearly 5 times as small.
> 
> Another observation we make is that the performance drop from 192-dimensional to 96-dimensional models is minimal (less than 2% for most tasks). For the MRPC task, in fact, the 96-dimensional model trained with dual training achieves an accuracy of 80.5%, which is higher than even the PKD 6-layer baseline with nearly 12 times as many parameters. Finally, our highly-compressed 48-dimensional models also perform respectably: the best 48-dimensional models are in a similar performance bracket as the 3-layer PKD model, a model 25 times larger by memory footprint.

### Relevance

Label: 

## Record 0004

Paper: Extreme Language Model Compression with Optimal Subwords and Shared Projections

### Question

> Why are prior knowledge distillation techniques models are ineffective in producing student models with vocabularies different from the original teacher models?  

### Passage

> Recently, contextual-aware language models such as ELMo BIBREF0, GPT BIBREF1, BERT BIBREF2 and XLNet BIBREF3 have shown to greatly outperform traditional word embedding models including Word2Vec BIBREF4 and GloVe BIBREF5 in a variety of NLP tasks. These pre-trained language models, when fine-tuned on downstream language understanding tasks such as sentiment classification BIBREF6, natural language inference BIBREF7 and reading comprehension BIBREF8, BIBREF9, have achieved state-of-the-art performance. However, the large number of parameters in these models, often above hundreds of millions, makes it impossible to host them on resource-constrained tasks such as doing real-time inference on mobile and edge devices.
> 
> Besides utilizing model quantization techniques BIBREF10, BIBREF11 which aim to reduce the floating-point accuracy of the parameters, significant recent research has focused on knowledge distillation BIBREF12, BIBREF13 techniques. Here, the goal is to train a small-footprint student model by borrowing knowledge, such as through a soft predicted label distribution, from a larger pre-trained teacher model.
> 
> However, a significant bottleneck that has been overlooked by previous efforts is the input vocabulary size and its corresponding word embedding matrix, often accounting for a significant proportion of all model parameters. For instance, the embedding table of the BERTBASE model, comprising over 30K WordPiece tokens BIBREF14, accounts for over $21\%$ of the model size. While there has been existing work on reducing NLP model vocabulary sizes BIBREF15, distillation techniques cannot utilize these, since they require the student and teacher models to share the same vocabulary and output space. This profoundly limits their potential to further reduce model sizes.
> 
> We present two novel ideas to improve the effectiveness of knowledge distillation, in particular for BERT, with the focus on bringing down model sizes to as much as a few mega-bytes. Our model is among the first to propose to use a significantly smaller vocabulary for the student model learned during distillation. In addition, instead of distilling solely on the teacher model's final-layer outputs, our model leverages layer-wise teacher model parameters to directly optimize the parameters of the corresponding layers in the student model. Specifically, our contributions are:
> 
> [leftmargin=*]
> 
> Dual Training: Our teacher and student models have different vocabularies and incompatible tokenizations for the same sequence. To address this during distillation, we feed

### Relevance

Label: 

## Record 0005

Paper: Extreme Language Model Compression with Optimal Subwords and Shared Projections

### Question

> Why are prior knowledge distillation techniques models are ineffective in producing student models with vocabularies different from the original teacher models?  

### Passage

> For explicit evaluation of the generalized language perspective of the distilled student language models, we use the Reddit dataset BIBREF40 to measure word mask prediction accuracy of the student models, since the language used on Reddit is different from that in the training corpora. The dataset is preprocessed similarly to the training corpora, except we do not need to tokenize it using the teacher vocabulary, since we only run and evaluate the student models.
> 
> For implicit evaluation on downstream language understanding tasks, we fine-tune and evaluate the distilled student models on three tasks from the GLUE benchmark BIBREF41:
> 
> [leftmargin=*,topsep=0pt]
> 
> Stanford Sentiment Treebank (SST-2) BIBREF6, a two-way sentence sentiment classification task with 67K training instances,
> 
> Microsoft Research Paraphrase Corpus (MRPC) BIBREF42, a two-way sentence pair classification task to identify paraphrases, with 3.7K training instances, and
> 
> Multi-Genre Natural Language Inference (MNLI) BIBREF7, a three-way sentence pair classification task with 393K training instances, to identify premise-hypothesis relations. There are separate development and test sets for genre-matched and genre-mismatched premise-hypothesis pairs; we tune our models solely on the genre-matched development set.
> 
> For all downstream task evaluations, we fine-tune for 10 epochs using LAMB with a learning rate of 0.0002 and batch size of 32. Since our language models are trained with a maximum sequence length of 128 tokens, we do not evaluate on reading comprehension datasets such as SQuAD BIBREF8 or RACE BIBREF9, which require models supporting longer sequences.

### Relevance

Label: 

## Record 0006

Paper: An Annotated Corpus of Emerging Anglicisms in Spanish Newspaper Headlines

### Question

> Does the paper mention other works proposing methods to detect anglicisms in Spanish?

### Passage

> In this paper we have presented a new corpus of 21,570 newspaper headlines written in European Spanish. The corpus is annotated with emergent anglicisms and, up to our very best knowledge, is the first corpus of this type to be released publicly. We have presented the annotation scope, tagset and guidelines, and we have introduced a CRF baseline model for anglicism extraction trained with the described corpus. The results obtained show that the the corpus and baseline model are appropriate for automatic anglicism extraction.

### Relevance

Label: 

## Record 0007

Paper: An Annotated Corpus of Emerging Anglicisms in Spanish Newspaper Headlines

### Question

> Does the paper mention other works proposing methods to detect anglicisms in Spanish?

### Passage

> The study of English influence in the Spanish language has been a hot topic in Hispanic linguistics for decades, particularly concerning lexical borrowing or anglicisms BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, BIBREF5, BIBREF6.
> 
> Lexical borrowing is a phenomenon that affects all languages and constitutes a productive mechanism for word-formation, especially in the press. chesleypaulapredicting2010 estimated that a reader of French newspapers encountered a new lexical borrowing for every 1,000 words. In Chilean newspapers, lexical borrowings account for approximately 30% of neologisms, 80% of those corresponding to English loanwords BIBREF7.
> 
> Detecting lexical borrowings is relevant both for lexicographic purposes and for NLP downstream tasks BIBREF8, BIBREF9. However, strategies to track and register lexical borrowings have traditionally relied on manual review of corpora.
> 
> In this paper we present: (1) a corpus of newspaper headlines in European Spanish annotated with emerging anglicisms and (2) a CRF baseline model for anglicism automatic extraction in Spanish newswire.

### Relevance

Label: 

## Record 0008

Paper: An Annotated Corpus of Emerging Anglicisms in Spanish Newspaper Headlines

### Question

> Does the paper mention other works proposing methods to detect anglicisms in Spanish?

### Passage

> the newspaper, and therefore included borrowings from other languages such as Catalan, Basque or French. When running the model without the OTHER tag on the supplemental test set, these non-English borrowings were labeled as anglicisms by the model (after all, their spelling does not resemble Spanish spelling), damaging the precision score. When the OTHER tag was included, these non-English borrowings got correctly labeled as OTHER, improving the precision score. This proves that, although the OTHER tag might be irrelevant or even damaging when testing on the development or test set, it can be useful when testing on more naturalistic data, such as the one in the supplemental test set.
> 
> Concerning errors, two types of errors were recurrent among all sets: long titles of songs, films or series written in English were a source of false positives, as the model tended to mistake some of the uncapitalized words in the title for anglicisms (for example, it darker in “`You want it darker', la oscura y brillante despedida de Leonard Cohen"). On the other hand, anglicisms that appear on the first position of the sentence (and were, therefore, capitalized) were consistently ignored (as the model probably assumed they were named entities) and produced a high number of false negatives (for example, vamping in “Vamping: la recurrente leyenda urbana de la luz azul `asesina'").
> 
> The results on Table TABREF28 cannot, however, be compared to the ones reported by previous work: the metric that we report is span F-measure, as the evaluation was done on span level (instead of token level) and credit was only given to full matches. Secondly, there was no Spanish tag assigned to non-borrowings, that means that no credit was given if a Spanish token was identified as such.

### Relevance

Label: 

## Record 0009

Paper: An Annotated Corpus of Emerging Anglicisms in Spanish Newspaper Headlines

### Question

> Does the paper mention other works proposing methods to detect anglicisms in Spanish?

### Passage

> Corpus-based studies of English borrowings in Spanish media have traditionally relied on manual evaluation of either previously compiled general corpora such as CREA BIBREF10, BIBREF11, BIBREF12, BIBREF13, either new tailor-made corpora designed to analyze specific genres, varieties or phenomena BIBREF14, BIBREF15, BIBREF16, BIBREF17, BIBREF18, BIBREF19, BIBREF20.
> 
> In terms of automatic detection of anglicisms, previous approaches in different languages have mostly depended on resource lookup (lexicon or corpus frequencies), character n-grams and pattern matching. alex-2008-comparing combined lexicon lookup and a search engine module that used the web as a corpus to detect English inclusions in a corpus of German texts and compared her results with a maxent Markov model. furiassi2007retrieval explored corpora lookup and character n-grams to extract false anglicisms from a corpus of Italian newspapers. andersen2012semi used dictionary lookup, regular expressions and lexicon-derived frequencies of character n-grams to detect anglicism candidates in the Norwegian Newspaper Corpus (NNC) BIBREF21, while losnegaard2012data explored a Machine Learning approach to anglicism detection in Norwegian by using TiMBL (Tilburg Memory-Based Learner, an implementation of a k-nearest neighbor classifier) with character trigrams as features. garley-hockenmaier-2012-beefmoves trained a maxent classifier with character n-gram and morphological features to identify anglicisms in German online communities. In Spanish, serigos2017using extracted anglicisms from a corpus of Argentinian newspapers by combining dictionary lookup (aided by TreeTagger and the NLTK lemmatizer) with automatic filtering of capitalized words and manual inspection. In serigos2017applying, a character n-gram module was added to estimate the probabilities of a word being English or Spanish. moreno2018configuracion used different pattern-matching filters and lexicon lookup to extract anglicism cadidates from a corpus of tweets in US Spanish.
> 
> Work within the code-switching community has also dealt with language identification on multilingual corpora. Due to the nature of code-switching, these models have primarily focused on oral copora and social media datasets BIBREF22, BIBREF23, BIBREF24. In the last shared task of language identification in code-switched data BIBREF23, approaches to English-Spanish included CRFs models BIBREF25, BIBREF26, BIBREF27, BIBREF28, logistic regression BIBREF29 and LSTMs models BIBREF30, BIBREF31.
> 
> The scope and nature of lexical borrowing is, however, somewhat different to that of code-switching. In fact, applying code-switching models to lexical borrowing detection has previously proved to be unsuccessful, as they tend to

### Relevance

Label: 

## Record 0010

Paper: An Annotated Corpus of Emerging Anglicisms in Spanish Newspaper Headlines

### Question

> Does the paper mention other works proposing methods to detect anglicisms in Spanish?

### Passage

> In addition to the usual train/development/test split we have just presented, a supplemental test set of 5,017 headlines was collected. The headlines included in this additional test set also belong to eldiario.es. These headlines were retrieved daily through RSS during February 2020 and included all sections from the newspaper. The headlines in the supplemental corpus therefore do not overlap in time with the main corpus and include more sections. The number of headlines, tokens and anglicisms in the supplemental test set can be found in Table TABREF6.
> 
> The motivation behind this supplemental test set is to assess the model performance on more naturalistic data, as the headlines in the supplemental corpus (1) belong to the future of the main corpus and (2) come from a less borrowing-dense sample. This supplemental test set better mimics the real scenario that an actual anglicism extractor would face and can be used to assess how well the model generalizes to detect anglicisms in any section of the daily news, which is ultimately the aim of this project.

### Relevance

Label: 

## Record 0011

Paper: Argumentation Mining in User-Generated Web Discourse

### Question

> What argument components do the ML methods aim to identify?

### Passage

> distribution of the premise types with examples for each topic from the annotated corpus. As can be seen in the first row, arguments in prayer in schools contain majority (73%) of unverifiable premises. Closer examination reveals that their content vary from general vague propositions to obvious fallacies, such as a hasty generalization, straw men, or slippery slope. As Nieminen.Mustonen.2014 found out, fallacies are very common in argumentation about religion-related issues. On the other side of the spectrum, arguments about redshirting rely mostly on anecdotal evidence (61% of verifiable experiential propositions). We will discuss the phenomena of narratives in argumentation in more detail later in section UID98 . All the topics except private vs. public schools exhibit similar amount of verifiable non-experiential premises (9%–22%), usually referring to expert studies or facts. However, this type of premises has usually the lowest frequency.
> 
> Manually analyzing argumentative discourse and reconstructing (annotating) the underlying argument structure and its components is difficult. As [p. 267]Reed2006 point out, “the analysis of arguments is often hard, not only for students, but for experts too.” According to [p. 81]Harrell.2011b, argumentation is a skill and “even for simple arguments, untrained college students can identify the conclusion but without prompting are poor at both identifying the premises and how the premises support the conclusion.” [p. 81]Harrell.2011 further claims that “a wide literature supports the contention that the particular skills of understanding, evaluating, and producing arguments are generally poor in the population of people who have not had specific training and that specific training is what improves these skills.” Some studies, for example, show that students perform significantly better on reasoning tasks when they have learned to identify premises and conclusions BIBREF95 or have learned some standard argumentation norms BIBREF96 .
> 
> One particular extra challenge in analyzing argumentation in Web user-generated discourse is that the authors produce their texts probably without any existing argumentation theory or model in mind. We assume that argumentation or persuasion is inherent when users discuss controversial topics, but the true reasons why people participate in on-line communities and what drives their behavior is another research question BIBREF97 , BIBREF98 , BIBREF99 , BIBREF100 . When the analyzed texts have a clear intention

### Relevance

Label: 

## Record 0012

Paper: Argumentation Mining in User-Generated Web Discourse

### Question

> What argument components do the ML methods aim to identify?

### Passage

> for me.] [premise: I really haven't met any homeschoolers who turned out quite right, including myself.] I apologize if what I'm saying offends any of you - that's not my intention, [rebuttal: I know that there are many homeschooled children who do just fine,] but [refutation: that hasn't been my experience.]
> 
> To the best of our knowledge, these context-dependent dialogical properties of argument components using Toulmin's model have not been solved in the literature on argumentation theory and we suggest that these observations should be taken into account in the future research in monological argumentation.
> 
> Appeal to emotion, sarcasm, irony, or jokes are common in argumentation in user-generated Web content. We also observed documents in our data that were purely sarcastic (the pathos dimension), therefore logical analysis of the argument (the logos dimension) would make no sense. However, given the structure of such documents, some claims or premises might be also identified. Such an argument is a typical example of fallacious argumentation, which intentionally pretends to present a valid argument, but its persuasion is conveyed purely for example by appealing to emotions of the reader BIBREF88 .
> 
> We present some statistics of the annotated data that are important from the argumentation research perspective. Regardless of the register, 48% of claims are implicit. This means that the authors assume that their standpoint towards the discussed controversy can be inferred by the reader and give only reasons for that standpoint. Also, explicit claims are mainly written just once, only in 3% of the documents the claim was rephrased and occurred multiple times.
> 
> In 6% of the documents, the reasons for an implicit claim are given only in the pathos dimension, making the argument purely persuasive without logical argumentation.
> 
> The “myside bias”, defined as a bias against information supporting another side of an argument BIBREF89 , BIBREF90 , can be observed by the presence of rebuttals to the author's claim or by formulating arguments for both sides when the overall stance is neutral. While 85% of the documents do not consider any opposing side, only 8% documents present a rebuttal, which is then attacked by refutation in 4% of the documents. Multiple rebuttals and refutations were found in

### Relevance

Label: 

## Record 0013

Paper: Argumentation Mining in User-Generated Web Discourse

### Question

> What argument components do the ML methods aim to identify?

### Passage

> various approaches to argument analysis and persuasion studies presented in this section, we would like to stress some novel aspects of the current article. First, we aim at adapting a model of argument based on research by argumentation scholars, both theoretical and empirical. We pose several pragmatical constraints, such as register independence (generalization over several registers). Second, our emphasis is put on reliable annotations and sufficient data size (about 90k tokens). Third, we deal with fairly unrestricted Web-based sources, so additional steps of distinguishing whether the texts are argumentative are required. Argumentation mining has been a rapidly evolving field with several major venues in 2015. We encourage readers to consult an upcoming survey article by Lippi.Torroni.2016 or the proceedings of the 2nd Argumentation Mining workshop BIBREF50 to keep up with recent developments. However, to the best of our knowledge, the main findings of this article have not yet been made obsolete by any related work.

### Relevance

Label: 

## Record 0014

Paper: Argumentation Mining in User-Generated Web Discourse

### Question

> What argument components do the ML methods aim to identify?

### Passage

> We create a new corpus which is, to the best of our knowledge, the largest corpus that has been annotated within the argumentation mining field to date. We choose several target domains from educational controversies, such as homeschooling, single-sex education, or mainstreaming. A novel aspect of the corpus is its coverage of different registers of user-generated Web content, such as comments to articles, discussion forum posts, blog posts, as well as professional newswire articles.
> 
> Since the data come from a variety of sources and no assumptions about its actual content with respect to argumentation can be drawn, we conduct two extensive annotation studies. In the first study, we tackle the problem of relatively high “noise” in the retrieved data. In particular, not all of the documents are related to the given topics in a way that makes them candidates for further deep analysis of argumentation (this study results into 990 annotated documents). In the second study, we discuss the selection of an appropriate argumentation model based on evidence in argumentation research and propose a model that is suitable for analyzing micro-level argumention in user-generated Web content. Using this model, we annotate 340 documents (approx. 90,000 tokens), reaching a substantial inter-annotator agreement. We provide a hand-analysis of all the phenomena typical to argumentation that are prevalent in our data. These findings may also serve as empirical evidence to issues that are on the spot of current argumentation research.
> 
> From the computational perspective, we experiment on the annotated data using various machine learning methods in order to extract argument structure from documents. We propose several novel feature sets and identify configurations that run best in in-domain and cross-domain scenarios. To foster research in the community, we provide the annotated data as well as all the experimental software under free license.
> 
> The rest of the article is structured as follows. First, we provide an essential background in argumentation theory in section SECREF2 . Section SECREF3 surveys related work in several areas. Then we introduce the dataset and two annotation studies in section SECREF4 . Section SECREF5 presents our experimental work and discusses the results and errors and section SECREF6 concludes this article.

### Relevance

Label: 

## Record 0015

Paper: Argumentation Mining in User-Generated Web Discourse

### Question

> What argument components do the ML methods aim to identify?

### Passage

> In the following experiment, we focus on automatic identification of arguments in the discourse. Our approach is based on supervised and semi-supervised machine learning methods on the gold data Toulmin dataset introduced in section SECREF51 .
> 
> An argument consists of different components (such as premises, backing, etc.) which are implicitly linked to the claim. In principle one document can contain multiple independent arguments. However, only 4% of the documents in our dataset contain arguments for both sides of the issue. Thus we simplify the task and assume there is only one argument per document.
> 
> Given the low inter-annotator agreement on the pathos dimension (Table TABREF77 ), we focus solely on recognizing the logical dimension of argument. The pathos dimension of argument remains an open problem for a proper modeling as well as its later recognition.
> 
> Since the smallest annotation unit is a token and the argument components do not overlap, we approach identification of argument components as a sequence labeling problem. We use the BIO encoding, so each token belongs to one of the following 11 classes: O (not a part of any argument component), Backing-B, Backing-I, Claim-B, Claim-I, Premise-B, Premise-I, Rebuttal-B, Rebuttal-I, Refutation-B, Refutation-I. This is the minimal encoding that is able to distinguish two adjacent argument components of the same type. In our data, 48% of all adjacent argument components of the same type are direct neighbors (there are no "O" tokens in between).
> 
> We report Macro- INLINEFORM0 score and INLINEFORM1 scores for each of the 11 classes as the main evaluation metric. This evaluation is performed on the token level, and for each token the predicted label must exactly match the gold data label (classification of tokens into 11 classes).
> 
> As instances for the sequence labeling model, we chose sentences rather than tokens. During our initial experiments, we observed that building a sequence labeling model for recognizing argument components as sequences of tokens is too fine-grained, as a single token does not convey enough information that could be encoded as features for a machine learner. However, as discussed in section UID73 , the annotations were performed on data pre-segmented to sentences and annotating tokens was necessary only when the sentence segmentation was

### Relevance

Label: 

## Record 0016

Paper: End-to-End Trainable Non-Collaborative Dialog System

### Question

> What are the baselines outperformed by this work?

### Passage

> This work was supported by DARPA ASED Program HR001117S0050. The U.S. Government is authorized to reproduce and distribute reprints for governmental purposes not withstanding any copyright notation therein. The views and conclusions contained herein are those of the authors and should not be interpreted as necessarily representing the official policies, either expressed or implied, of DARPA or the U.S. Government.

### Relevance

Label: 

## Record 0017

Paper: End-to-End Trainable Non-Collaborative Dialog System

### Question

> What are the baselines outperformed by this work?

### Passage

> The interest in non-collaborative tasks has been increasing and there have already been several related datasets. For instance, BIBREF1 wang2019persuasion collected conversations where one participant persuades another to donate to a charity. BIBREF2 he2018decoupling collected negotiation dialogs where buyers and sellers bargain for items for sale on Craigslist. There are many other non-collaborative tasks, such as the turn-taking game BIBREF6, the multi-party game BIBREF7 and item splitting negotiation BIBREF8. Similar to the AntiScam dataset proposed in this paper, these datasets contain off-task content and can be used to train non-collaborative dialog systems. However, since they are not specifically collected and designed for non-collaborative tasks, it might be difficult to disentangle the on-task and off-task contents and measure the performance. Therefore, we propose the AntiScam dataset, which is designed to interleave the on-task and off-task contents in the conversation, and can serve as a benchmark dataset for similar non-collaborative tasks.
> 
> To better understand user utterances and separate on-task and off-task content within a conversation, previous work has designed hierarchical annotation schemes for specific domains. BIBREF9 hardy2002multi followed the DAMSL schemeBIBREF10 and annotated a multilingual human-computer dialog corpus with a hierarchical dialog act annotation scheme. BIBREF11 gupta2018semantic used a hierarchical annotation scheme for semantic parsing. Inspired by these studies, our idea is to annotate the intent and semantic slot separately in non-collaborative tasks. We propose a hierarchical intent annotation scheme that can be adopted by all non-collaborative tasks. With this annotation scheme, MISSA is able to quickly build an end-to-end trainable dialog system for any non-collaborative task.
> 
> Traditional task-oriented dialog systems BIBREF12 are usually composed of multiple independent modules, for example, natural language understanding, dialog state tracking BIBREF13, BIBREF14, dialog policy manager BIBREF15, and natural language generation BIBREF16. Conversational intent is adopted to capture the meaning of task content in these dialog systems BIBREF2, BIBREF17. In comparison to this work, we use a hierarchical intent scheme that includes off-task and on-task intents to capture utterance meaning. We also train the model in a multi-task fashion to predict decoupled intents and semantic slots. The major defect of a separately trained pipeline is the laborious dialog state design and annotation. In order to mitigate this problem, recent work has

### Relevance

Label: 

## Record 0018

Paper: End-to-End Trainable Non-Collaborative Dialog System

### Question

> What are the baselines outperformed by this work?

### Passage

> Automatic metrics only validate the system’s performance on a single dimension at a time. The ultimate holistic evaluation should be conducted by having the trained system interact with human users. Therefore we also conduct human evaluations for the dialog system built on AntiScam. We test our models and baselines with 15 college-student volunteers. Each of them is asked to pretend to be an attacker and interact with all the models for at least three times to avoid randomness. We in total collect 225 number of dialogs. Each time, volunteers are required to use similar sentences and strategies to interact with all five models and score each model based on the metrics listed below at the end of the current round. Each model receives a total of 45 human ratings, and the average score is reported as the final human-evaluation score. In total, we design five different metrics to assess the models' conversational ability whilst interacting with humans. The results are shown in Table TABREF19.
> 
> Fluency Fluency is used to explore different models' language generation quality.
> 
> Coherence Different from single sentence's fluency, coherence focuses more on the logical consistency between sentences in each turn.
> 
> Engagement In the anti-scam scenario, one of our missions is to keep engaging with the attackers to waste their time. So we directly ask volunteers (attackers) to what extend they would like to continue chatting with the system.
> 
> Dialog length (Length) Engagement is a subjective metric. Anti-scam system's goal is to engage user in the conversation longer in order to limit their harm to other potential victims. So we count the dialog length as another metric to evaluate system performance.
> 
> Task Success Score (TaskSuc) The other goal of the anti-scam system is to elicit attacker's personal information. We count the average type of information (name, address and phone number) that the system obtained from attackers as the task success score.

### Relevance

Label: 

## Record 0019

Paper: End-to-End Trainable Non-Collaborative Dialog System

### Question

> What are the baselines outperformed by this work?

### Passage

> also train the model in a multi-task fashion to predict decoupled intents and semantic slots. The major defect of a separately trained pipeline is the laborious dialog state design and annotation. In order to mitigate this problem, recent work has explored replacing independent modules with end-to-end neural networks BIBREF18, BIBREF19, BIBREF20. Our model also follows this end-to-end fashion.
> 
> Over the last few years, we have witnessed a huge growth in non-task-oriented dialog systems BIBREF21, BIBREF22. Social chatbots such as Gunrock BIBREF23 were able to maintain a conversation for around ten minutes in an open domain. Recent improvements build on top of the transformer and pre-trained language models BIBREF24, BIBREF25, BIBREF26, obtained state-of-the-art results on the Persona-Chat dataset BIBREF0. Pre-trained language models are proposed to build task-oriented dialog systems to drive the progress on leveraging large amounts of available unannotated data. BIBREF27. Similarly, our approach is also built on top of the TransferTransfo framework BIBREF0. BIBREF27 budzianowski2019hello focused on collaborative tasks BIBREF28. We target non-collaborative tasks instead.
> 
> Another line of work interleaves on-task and off-task content by building a hybrid dialog system that combines a task-oriented model and a non-task-oriented model BIBREF4, BIBREF29. In these studies, task-oriented systems and non-task-oriented systems are designed separately and both systems generate candidate responses. A selector is then designed to choose an appropriate output from the candidate responses BIBREF4 and a connector to combine two response candidates BIBREF30, BIBREF31. Compared with these works, MISSA is end-to-end trainable and thus easier to train and update.

### Relevance

Label: 

## Record 0020

Paper: End-to-End Trainable Non-Collaborative Dialog System

### Question

> What are the baselines outperformed by this work?

### Passage

> The TransferTransfo framework was proposed to build open domain dialog systems. BIBREF0 wolf2019transfertransfo fine-tuned the generative pre-training model (GPT) BIBREF32 with the PERSONA-CHAT dataset BIBREF33 in a multi-task fashion, where the language model objective is combined with a next-utterance classification task. The language model's objective is to maximize the following likelihood for a given sequence of tokens, $X = \lbrace x_1,\dots ,x_n\rbrace $:
> 
> The authors also trained a classifier to distinguish the correct next-utterance appended to the input human utterances from a set of randomly selected utterance distractors. In addition, they introduced dialog state embeddings to indicate speaker role in the model. The model significantly outperformed previous baselines over both automatic evaluations and human evaluations in social conversations. Since the TransferTransfo framework performs well in open domain, we adapt it for non-collaborative settings. We keep all the embeddings in the framework and train the language model and next-utterance classification task in a multi-task fashion following TransferTransfo.
> 
> We make two major changes: (1) To address the problem that TransferTransfo is originally designed for an open domain without explicit intents and regulations, we add two intent classifiers and two semantic slot classifiers to classify the intents and semantic slots for both human utterances and system responses as an effort to incorporate the proposed hierarchical intent and semantic slot annotation for non-collaborative tasks. (2) In dialog systems, multiple generated responses can be coherent under the current context. Generating diverse responses has proven to be an enduring challenge. To increase response diversity, we sample multiple generated responses and choose an appropriate one according to a set of pre-defined rules.

### Relevance

Label: 

## Record 0021

Paper: Abstractive Dialog Summarization with Semantic Scaffolds

### Question

> How does new evaluation metric considers critical informative entities?

### Passage

> We adapt a dialog generation dataset, MultiWOZ to an abstractive dialog summarization dataset. We propose SPNet, an end-to-end model that incorporates the speaker role, semantic slot and dialog domain as the semantic scaffolds to improve abstractive summary quality. We also propose an automatic evaluation metric CIC that considers semantic slot relevance to serve as a complementary metric to ROUGE. SPNet outperforms baseline methods in both automatic and human evaluation metrics. It suggests that involving semantic scaffolds efficiently improves abstractive summarization quality in the dialog scene.
> 
> Moreover, we can easily extend SPNet to other summarization tasks. We plan to apply semantic slot scaffold to news summarization. Specifically, we can annotate the critical entities such as person names or location names to ensure that they are captured correctly in the generated summary. We also plan to collect a human-human dialog dataset with more diverse human-written summaries.

### Relevance

Label: 

## Record 0022

Paper: Abstractive Dialog Summarization with Semantic Scaffolds

### Question

> How does new evaluation metric considers critical informative entities?

### Passage

> ROUGE BIBREF32 is a standard metric for summarization, designed to measure the surface word alignment between a generated summary and a human written summary. We evaluate our model with ROUGE-1, ROUGE-2 and ROUGE-L. They measure the word-overlap, bigram-overlap, and longest common sequence between the reference summary and the generated summary respectively. We obtain ROUGE scores using the files2rouge package. However, ROUGE is insufficient to measure summarization performance. The following example shows its limitations:
> 
> Reference: You are going to [restaurant_name] at [time].
> 
> Summary: You are going to [restaurant_name] at.
> 
> In this case, the summary has a high ROUGE score, as it has a considerable proportion of word overlap with the reference summary. However, it still has poor relevance and readability, for leaving out one of the most critical information: [time]. ROUGE treats each word equally in computing n-gram overlap while the informativeness actually varies: common words or phrases (e.g. “You are going to") significantly contribute to the ROUGE score and readability, but they are almost irrelevant to essential contents. The semantic slot values (e.g. [restaurant_name], [time]) are more essential compared to other words in the summary. However, ROUGE did not take this into consideration. To address this drawback in ROUGE, we propose a new evaluation metric: Critical Information Completeness (CIC). Formally, CIC is a recall of semantic slot information between a candidate summary and a reference summary. CIC is defined as follows:
> 
> where $V$ stands for a set of delexicalized values in the reference summary, $Count_{match}(v)$ is the number of values co-occurring in the candidate summary and reference summary, and $m$ is the number of values in set $V$. In our experiments, CIC is computed as the arithmetic mean over all the dialog domains to retain the overall performance.
> 
> CIC is a suitable complementary metric to ROUGE because it accounts for the most important information within each dialog domain. CIC can be applied to any summarization task with predefined essential entities. For example, in news summarization the proper nouns are the critical information to retain.

### Relevance

Label: 

## Record 0023

Paper: Abstractive Dialog Summarization with Semantic Scaffolds

### Question

> How does new evaluation metric considers critical informative entities?

### Passage

> We also perform human evaluation to verify if our method's increased performance on automatic evaluation metrics entails better human perceived quality. We randomly select 100 test samples from MultiWOZ test set for evaluation. We recruit 150 crowd workers from Amazon Mechanical Turk. For each sample, we show the conversation, reference summary, as well as summaries generated by Pointer-Generator and SPNet to three different participants. The participants are asked to score each summary on three indicators: relevance, conciseness and readability on a 1 to 5 scale, and rank the summary pair (tie allowed).
> 
> We present human evaluation results in Table TABREF27. In the scoring part, our model outperforms Pointer-Generator in all three evaluation metrics. SPNet scored better than Pointer-Generator on relevance and readability. All generated summaries are relatively concise; therefore, they score very similar in conciseness. Ground truth is still perceived as more relevant and readable than SPNet results. However, ground truth does not get a high absolute score. From the feedback of the evaluators, we found that they think that the ground truth has not covered all the necessary information in the conversation, and the description is not so natural. This motivates us to collect a dialog summarization dataset with high-quality human-written summaries in the future. Results in the ranking evaluation show more differences between different summaries. SPNet outperforms Pointer-Generator with a large margin. Its performance is relatively close to the ground truth summary.

### Relevance

Label: 

## Record 0024

Paper: Abstractive Dialog Summarization with Semantic Scaffolds

### Question

> How does new evaluation metric considers critical informative entities?

### Passage

> Summarization aims to condense a piece of text to a shorter version, retaining the critical information. On dialogs, summarization has various promising applications in the real world. For instance, the automatic doctor-patient interaction summary can save doctors' massive amount of time used for filling medical records. There is also a general demand for summarizing meetings in order to track project progress in the industry. Generally, multi-party conversations with interactive communication are more difficult to summarize than single-speaker documents. Hence, dialog summarization will be a potential field in summarization track.
> 
> There are two types of summarization: extractive and abstractive. Extractive summarization selects sentences or phrases directly from the source text and merges them to a summary, while abstractive summarization attempts to generate novel expressions to condense information. Previous dialog summarization research mostly study extractive summarization BIBREF1, BIBREF2. Extractive methods merge selected important utterances from a dialog to form summary. Because dialogs are highly dependant on their histories, it is difficult to produce coherent discourses with a set of non-consecutive conversation turns. Therefore, extractive summarization is not the best approach to summarize dialogs. However, most modern abstractive methods focus on single-speaker documents rather than dialogs due to the lack of dialog summarization corpora. Popular abstractive summarization dataset like CNN/Daily Mail BIBREF3 is on news documents. AMI meeting corpus BIBREF4 is the common benchmark, but it only has extractive summary.
> 
> In this work, we introduce a dataset for abstractive dialog summarization based on MultiWOZ BIBREF0. Seq2Seq models such as Pointer-Generator BIBREF5 have achieved high-quality summaries of news document. However, directly applying a news summarizer to dialog results in two drawbacks: informative entities such as place name are difficult to capture precisely and contents in different domains are summarized unequally. To address these problems, we propose Scaffold Pointer Network (SPNet). SPNet incorporates three types of semantic scaffolds in dialog: speaker role, semantic slot, and dialog domain. Firstly, SPNet adapts separate encoder to attentional Seq2Seq framework, producing distinct semantic representations for different speaker roles. Then, our method inputs delexicalized utterances for producing delexicalized summary, and fills in slot values to generate complete summary. Finally, we incorporate dialog domain scaffold by jointly optimizing dialog domain classification task along with the summarization

### Relevance

Label: 

## Record 0025

Paper: Abstractive Dialog Summarization with Semantic Scaffolds

### Question

> How does new evaluation metric considers critical informative entities?

### Passage

> Table TABREF25 shows an example summary from all models along with ground truth summary. We observe that Pointer-Generator ignores some essential fragments, such as the restaurant booking information (6 people, Sunday, 18:45). Missing information always belongs to the last several domains (restaurant in this case) in a multi-domain dialog. We also observe that separately encoding two speakers reduces repetition and inconsistency. For instance, Pointer-Generator's summary mentions “free wifi" several times and has conflicting requirements on wifi. This is because dialogs has information redundancy, but single-speaker model ignores such dialog property.
> 
> Our method has limitations. In the example shown in Table TABREF25, our summary does not mention the hotel name (Alexander Bed and Breakfast) and its address (517a Coldham Lane) referred in the source. It occurs because the ground truth summary doe not cover it in the training data. As a supervised method, SPNet is hard to generate a summary containing additional information beyond the ground truth. However, in some cases, SPNet can also correctly summarize the content not covered in the reference summary (see Table TABREF31 in Appendix).
> 
> Furthermore, although our SPNet achieves a much-improved performance, the application of SPNet still needs extra annotations for semantic scaffolds. For a dialog dataset, speaker role scaffold is a natural pattern for modeling. Most multi-domain dialog corpus has the domain annotation. While for texts, for example news, its topic categorization such as sports or entertainment can be used as domain annotation. We find that semantic slot scaffold brings the most significant improvement, but it is seldom explicitly annotated. However, the semantic slot scaffold can be relaxed to any critical entities in the corpus, such as team name in sports news or professional terminology in a technical meeting.

### Relevance

Label: 

## Record 0026

Paper: Episodic Memory in Lifelong Language Learning

### Question

> Do they compare against other models?

### Passage

> In this section, we evaluate our proposed model against several baselines on text classification and question answering tasks.

### Relevance

Label: 

## Record 0027

Paper: Episodic Memory in Lifelong Language Learning

### Question

> Do they compare against other models?

### Passage

> We compare the following models in our experiments:
> 
> Enc-Dec: a standard encoder-decoder model without any episodic memory module.
> 
> A-GEM BIBREF9 : Average Gradient Episodic Memory model that defines constraints on the gradients that are used to update model parameters based on retrieved examples from the memory. In its original formulation, A-GEM requires dataset identifiers and randomly samples examples from previous datasets. We generalize it to the setting without dataset identities by randomly sampling from the episodic memory module at fixed intervals, similar to our method.
> 
> Replay: a model that uses stored examples for sparse experience replay without local adaptation. We perform experience replay by sampling 100 examples from the memory and perform a gradient update after every 10,000 training steps, which gives us a 1% replay rate.
> 
> MbPA BIBREF7 : an episodic memory model that uses stored examples for local adaptation without sparse experience replay. The original MbPA formulation has a trainable key network. Our MbPA baseline uses a fixed key network since MbPA with a trainable key network performs significantly worse.
> 
> MbPA INLINEFORM0 : an episodic memory model with randomly retrieved examples for local adaptation (no key network).
> 
> MbPA++: our episodic memory model described in § SECREF2 .
> 
> MTL: a multitask model trained on all datasets jointly, used as a performance upper bound.

### Relevance

Label: 

## Record 0028

Paper: Episodic Memory in Lifelong Language Learning

### Question

> Do they compare against other models?

### Passage

> We consider a continual (lifelong) learning setup where a model needs to learn from a stream of training examples INLINEFORM0 . We assume that all our training examples in the series come from multiple datasets of the same task (e.g., a text classification task, a question answering task), and each dataset comes one after the other. Since all examples come from the same task, the same model can be used to make predictions on all examples. A crucial difference between our continual learning setup and previous work is that we do not assume that each example comes with a dataset descriptor (e.g., a dataset identity). As a result, the model does not know which dataset an example comes from and when a dataset boundary has been crossed during training. The goal of learning is to find parameters INLINEFORM1 that minimize the negative log probability of training examples under our model: INLINEFORM2
> 
> Our model consists of three main components: (i) an example encoder, (ii) a task decoder, and (iii) an episodic memory module. Figure FIGREF6 shows an illustration of our complete model. We describe each component in detail in the following.

### Relevance

Label: 

## Record 0029

Paper: Episodic Memory in Lifelong Language Learning

### Question

> Do they compare against other models?

### Passage

> The ability to continuously learn and accumulate knowledge throughout a lifetime and reuse it effectively to adapt to a new problem quickly is a hallmark of general intelligence. State-of-the-art machine learning models work well on a single dataset given enough training examples, but they often fail to isolate and reuse previously acquired knowledge when the data distribution shifts (e.g., when presented with a new dataset)—a phenomenon known as catastrophic forgetting BIBREF0 , BIBREF1 .
> 
> The three main approaches to address catastrophic forgetting are based on: (i) augmenting the loss function that is being minimized during training with extra terms (e.g., a regularization term, an optimization constraint) to prevent model parameters learned on a new dataset from significantly deviating from parameters learned on previously seen datasets BIBREF2 , BIBREF3 , BIBREF4 , (ii) adding extra learning phases such as a knowledge distillation phase, an experience replay BIBREF5 , BIBREF6 , and (iii) augmenting the model with an episodic memory module BIBREF7 . Recent methods have shown that these approaches can be combined—e.g., by defining optimization constraints using samples from the episodic memory BIBREF8 , BIBREF9 .
> 
> In language learning, progress in unsupervised pretraining BIBREF10 , BIBREF11 , BIBREF12 has driven advances in many language understanding tasks BIBREF13 , BIBREF14 . However, these models have been shown to require a lot of in-domain training examples, rapidly overfit to particular datasets, and are prone to catastrophic forgetting BIBREF15 , making them unsuitable as a model of general linguistic intelligence.
> 
> In this paper, we investigate the role of episodic memory for learning a model of language in a lifelong setup. We propose to use such a component for sparse experience replay and local adaptation to allow the model to continually learn from examples drawn from different data distributions. In experience replay, we randomly select examples from memory to retrain on. Our model only performs experience replay very sparsely to consolidate newly acquired knowledge with existing knowledge in the memory into the model. We show that a 1% experience replay to learning new examples ratio is sufficient. Such a process bears some similarity to memory consolidation in human learning BIBREF16 . In local adaptation, we follow Memory-based Parameter Adaptation BIBREF7

### Relevance

Label: 

## Record 0030

Paper: Episodic Memory in Lifelong Language Learning

### Question

> Do they compare against other models?

### Passage

> our best model can be improved further by choosing relevant examples for sparse experience replay as well. We leave investigations of such methods to future work.
> 
> Comparing to the performance of the multitask model MTL—which is as an upper bound on achievable performance—we observe that there is still a gap between continual models and the multitask model. MbPA++ has the smallest performance gap. For text classification, MbPA++ outperforms single-dataset models in terms of averaged performance (70.6 vs. 60.7), demonstrating the success of positive transfer. For question answering, MbPA++ still lags behind single dataset models (62.0 vs. 66.0). Note that the collection of single-dataset models have many more parameters since there is a different set of model parameters per dataset. See Appendix SECREF8 for detailed results of multitask and single-dataset models.
> 
> Figure FIGREF34 shows INLINEFORM0 score and accuracy of various models on the test set corresponding to the first dataset seen during training as the models are trained on more datasets. The figure illustrates how well each model retains its previously acquired knowledge as it learns new knowledge. We can see that MbPA++ is consistently better compared to other methods.

### Relevance

Label: 

## Record 0031

Paper: Short-Text Classification Using Unsupervised Keyword Expansion

### Question

> How do they determine similarity between predicted word and topics?

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

## Record 0032

Paper: Short-Text Classification Using Unsupervised Keyword Expansion

### Question

> How do they determine similarity between predicted word and topics?

### Passage

> The Extended pseudo documents improved multiclass performance by 4.6% on average, in the region of 100 to 3000 training examples, as seen in figure SECREF11. The results indicate the effectiveness of the proposed method at suggesting relevant words within a narrow topic domain, even without any previous domain knowledge.
> 
> In each instance it was found that the extended pseudo documents only improved performance on small training sizes. This demonstrates that while the extended pseudo docs are effective at generating artificial data, they also produce a lot of noise. Once the training size exceeds a certain threshold, it becomes no longer necessary to create additional data, and using extended documents simply adds noise to an otherwise well trained model.
> 
> figureBinary Classification of 'Politics' or 'Entertainment' demonstrates that the number of added words can behave like a hyper paremeter and should be tuned based on training size. Tested on 1000 examples with 10-fold cross validation
> 
> figureBinary Classification of 'Politics' vs 'Sports' has less improvement compared to other datasets which indicates that the proposed method, while constructed to be domain agnostic, shows better performance towards certain topics. Tested on 1000 examples with 10-fold cross validation.
> 
> figureAdded Words improve Multiclass Classification between 1.5% and 13% in the range of 150 to 2000 training examples. Tests were conducted using equal size samples of Headlines categorized into 'World-Post', 'Crime', 'Politics', 'Entertainment', 'Sports' or 'Comedy'. A 900 Estimator Random Forest classifier was trained for each each data point, tested using 2000 examples, and averaged using 10-fold cross validation.
> 
> 2

### Relevance

Label: 

## Record 0033

Paper: Short-Text Classification Using Unsupervised Keyword Expansion

### Question

> How do they determine similarity between predicted word and topics?

### Passage

> It is desirable to generate new words which are relevant to the target topics and increase predictive signal, while avoiding words which are irrelevant, add noise, and mislead predictions.
> 
> The strategy, described in section SECREF4, was created to measure word relevance and quantify the unsupervised model performance. It can be seen from fig SECREF4 and SECREF12 in the appendix that the proposed expansion method is effective at generating words which relate to topics of the input sentence, even from very little data. From the context of just a single word, the method can generate 3 new relevant words, and can generate as many as 10 new relevant words from sentences which contain 5 topic related words SECREF12. While the method is susceptible to noise, producing on average 1 word related to each irrelevant topic, the number of correct predictions statistically exceed the noise.
> 
> Furthermore, because the proposed method does not have any prior knowledge of its target topics, it remains completely domain agnostic, and can be applied generally for short text of any topic.

### Relevance

Label: 

## Record 0034

Paper: Short-Text Classification Using Unsupervised Keyword Expansion

### Question

> How do they determine similarity between predicted word and topics?

### Passage

> figureA Topic table, created from the category labels of the complete headline dataset, can be used to measure the relevance of generated words.
> 
> An original headline was analyzed by counting the number of words which related to each topic. The generated words were then analyzed in the same way. The change in word count between input topics and output topics was measured and plotted as seen in figure SECREF12.
> 
> figureBox plot of the number of generated words within a topic as a function of the number of input words within the same topic. Results indicate that additional related words can be generated by increasing the signal of the input prompt. Tested on 7600 examples spanning 23 topics.
> 
> figureInformation regarding the original headlines, and generated words used to create extended pseudo headlines.
> 
> figureTop 3 guesses for each token position at each later of a BERT pretrained embedding model. Given the input sentence '2 peoplpe injured in Indiana school shooting', the full list of generated words can be obtainedfrom the values in the table.
> 
> figureTop 3 guesses for each token position at each later of a BERT pretrained embedding model.

### Relevance

Label: 

## Record 0035

Paper: Short-Text Classification Using Unsupervised Keyword Expansion

### Question

> How do they determine similarity between predicted word and topics?

### Passage

> Words were generated using the BERT pre-trained model developed and trained by Google AI Language BIBREF0. BERT creates contextualized word embedding by passing a list of word tokens through 12 hidden transformer layers and generating encoded word vectors. To generate extended text, an original short-text document was passed to pre-trained BERT. At each transformer layer a new word embedding was formed and saved. BERT's vector decoder was then used to convert hidden word vectors to candidate words, the top three candidate words at each encoder layer were kept.
> 
> Each input word produced 48 candidate words, however many were duplicates. Examples of generated words per layer can be found in table SECREF12 and SECREF12 in the appendix. The generated words were sorted based on frequency, duplicate words from the original input were removed, as were stop-words, punctuation, and incomplete words. The generated words were then appended to the original document to create extended pseudo documents, the extended document was limited to 120 words in order to normalize each feature set. Further analysis can be found in table SECREF12 in the appendix.
> 
> figureThe proposed method uses the BERT pre-trained word embedding model to generate new words which are appended to the orignal text creating extended pseudo documents.

### Relevance

Label: 

## Record 0036

Paper: Explaining Queries over Web Tables to Non-Experts

### Question

> Do they conduct a user study where they show an NL interface with and without their explanation?

### Passage

> model for explaining formal queries over web tables and implement it with our query explanations, (see Figure FIGREF1 ). We enhance an existing NL interface for querying tables BIBREF5 by introducing a novel component featuring our query explanations. Following the parsing of an input NL question, our component explains the candidate queries to users, allowing non-experts to choose the one that best fits their intention. The immediate application is to improve the quality of obtained queries at deployment time over simply choosing the parser's top query (without user feedback). Furthermore, we show how query explanations can be used to obtain user feedback which is used to retrain the Machine Learning system, thereby improving its performance.

### Relevance

Label: 

## Record 0037

Paper: Explaining Queries over Web Tables to Non-Experts

### Question

> Do they conduct a user study where they show an NL interface with and without their explanation?

### Passage

> that for INLINEFORM3 only 5% of the examples contained a correct query, a minor improvement at the cost of doubling user effort. Thus a choice of INLINEFORM4 appears to be reasonable.
> 
> To verify that our query explanations were understandable to non-experts we measured each worker's success. Results in Table TABREF59 show that in 78.4% of the cases, workers had succeeded in identifying the correct query or identifying that no candidate query was correct. The average success rate for all 35 workers being 15.7/20 questions. When comparing our explanation approach (utterances + highlights) to a baseline of no explanations, non-expert users failed to identify correct queries when shown only lambda DCS queries. This demonstrates that utterances and provenance-based highlights serve as effective explanations of formal queries to the layperson. We now show that using them jointly is superior to using only utterances.
> 
> When introducing our two explanation methods, we noted their complementary nature. NL utterances serve as highly detailed phrases describing the query, while highlighting provenance cells allows to quickly single out the correct queries. We put this claim to the test by measuring the impact our novel provenance-based highlights had on the average work-time of users. We measured the work-time of 20 distinct AMT workers, divided into two separate groups, each containing half of the participants. Workers from both groups were presented with 20 questions from WikiTableQuestions. The first group of workers were presented both with highlights and utterances as their query explanations, while the second group had to rely solely on NL utterances. Though both groups achieved identical correctness results, the group employing table highlights performed significantly faster. Results in Table TABREF60 show our provenance-based explanations cut the average and median work-time by 34% and 20% respectively. Since user work-time is valuable, the introduction of visual explanations such as table highlights may lead to significant savings in worker costs.
> 
> We have examined the effect to which our query explanations can help users improve the correctness of a baseline NL interface. Our user study compares the correctness of three scenarios:
> 
> Parser correctness - our baseline is the percentage of examples where the top query returned by the semantic parser was correct.
> 
> User correctness - the

### Relevance

Label: 

## Record 0038

Paper: Explaining Queries over Web Tables to Non-Experts

### Question

> Do they conduct a user study where they show an NL interface with and without their explanation?

### Passage

> Following the definition of our data model we introduce our formal query language, lambda dependency-based compositional semantics (lambda DCS) BIBREF6 , BIBREF0 , which is a language inspired by lambda calculus, that revolves around sets. Lambda DCS was originally designed for building an NL interface over Freebase BIBREF9 .
> 
> Lambda DCS is a highly expressive language, designed to represent complex NL questions involving sorting, aggregation intersection and more. It has been considered a standard language for performing semantic parsing over knowledge bases BIBREF6 , BIBREF0 , BIBREF1 , BIBREF5 . A lambda DCS formula is executed against a target table and returns either a set of values (string, number or date) or a set of table records. We describe here a simplified version of lambda DCS that will be sufficient for understanding the examples presented in this paper. For a full description of lambda DCS, the reader should refer to BIBREF6 . The basic constructs of lambda DCS are as follows:
> 
> Unary: a set of values. The simplest type of unary in a table is a table cell, e.g., Greece, which denotes the set of cells containing the entity 'Greece'.
> 
> Binary: A binary relation describes a relation between sets of objects. The simplest type of a binary relation is a table column INLINEFORM0 , mapping table entities to the records where they appear, e.g., Country.
> 
> Join: For a binary relation INLINEFORM0 and unary relation INLINEFORM1 , INLINEFORM2 operates as a selection and projection. INLINEFORM3 denotes all table records where the value of column Country is Greece.
> 
> Prev: Given records INLINEFORM0 the INLINEFORM1 operator will return the set of preceding table records, INLINEFORM2 .
> 
> Reverse: Given a binary relation INLINEFORM0 from INLINEFORM1 to INLINEFORM2 , there is a reversed binary relation R[ INLINEFORM3 ] from INLINEFORM4 to INLINEFORM5 . E.g., for a column binary relation INLINEFORM6 from table values to their records, R[ INLINEFORM7 ] is a relation from records to values. R[Year].Country.Greece takes all the record indices of Country.Greece and returns the values of column Year in these records. Similarly, R[Prev] denotes a relation from a set of records, to the set of following (reverse of previous) table records.
> 
> Intersection: Intersection of sets. E.g., the

### Relevance

Label: 

## Record 0039

Paper: Explaining Queries over Web Tables to Non-Experts

### Question

> Do they conduct a user study where they show an NL interface with and without their explanation?

### Passage

> We have studied in this paper the problem of explaining complex NL queries to non expert users. We introduced visual query explanations in the form of table highlights, based on a novel cell-based provenance model tested on web tables from hundreds of distinct domains. Table highlights provide immediate visual feedback for identifying correct candidate queries. We combine table highlights with utterance based query explanations, significantly improving their effectiveness. Using our query explanations we enhanced an NL interface for querying tables by providing it with feedback at both deployment and training time. Feedback is procured through query explanations, allowing users with no technical background to query tables with confidence, while simultaneously providing feedback to enhance the interface itself. We implement a human in the loop paradigm, where our users both exploit the underlying Machine Learning algorithm while providing it with further data to train on.
> 
> We have put our methods to the test, having conducted an extensive user study to determine the clarity of our explanations. Experimenting with explanations for hundreds of formal queries, users proved to be successful in interactively choosing correct queries, easily topping the baseline parser correctness. The addition of provenance-based highlights helps boost the efficacy of user feedback, cutting average work-time by a third compared to the utterances baseline.

### Relevance

Label: 

## Record 0040

Paper: Explaining Queries over Web Tables to Non-Experts

### Question

> Do they conduct a user study where they show an NL interface with and without their explanation?

### Passage

> correctness of a baseline NL interface. Our user study compares the correctness of three scenarios:
> 
> Parser correctness - our baseline is the percentage of examples where the top query returned by the semantic parser was correct.
> 
> User correctness - the percentage of examples where the user selected a correct query from the top-7 generated by the parser.
> 
> Hybrid correctness - correctness of queries returned by a combination of the previous two scenarios. The system returns the query marked by the user as correct; if the user marks all queries as incorrect it will return the parser's top candidate.
> 
> Results in Table TABREF64 show the correctness rates of these scenarios. User correctness score is superior to that of the baseline parser by 7.5% (from 37.1% to 44.6%), while the hybrid approach outscores both with a correctness of 48.7% improving the baseline by 11.6%. For the user and hybrid correctness we used a INLINEFORM0 test to measure significance. Random queries and tables included in the experiment are presented in Table TABREF66 . We also include a comparison of the top ranked query of the baseline parser compared to that of the user.
> 
> We define the correctness bound as the percentage of examples where the top-k candidate queries actually contain a correct result. This bound serves as the optimal correctness score that workers can achieve. The 56% correctness-bound of the baseline parser stems from the sheer complexity of the WikiTableQuestions benchmark. Given the training and test tables are disjoint, the parser is tested on relations and entities unobserved during its training. This task of generalizing to unseen domains is an established challenge in semantic parsing BIBREF1 , BIBREF21 . Using the correctness-bound as an upper bound on our results shows the hybrid approach achieves 87% of its full potential. Though there is some room for improvement, it seems reasonable given that our non-expert workers possess no prior experience of their given task.
> 
> We describe the execution times for generating our query explanations in Table TABREF65 . We trained the semantic parser using the SMEPRE toolkit BIBREF0 on a machine with Xeon 2.20GHz CPU and 256GB RAM running Linux Ubuntu 14.04 LTS. We report the average generation times of

### Relevance

Label: 

## Record 0041

Paper: Neural Language Modeling with Visual Features

### Question

> what features were derived from the videos?

### Passage

> Our training data consist of about 64M segments from YouTube videos comprising a total of INLINEFORM0 B tokens BIBREF14 . We tokenize the training data using a vocabulary of 66K wordpieces BIBREF15 . Thus, the input to the model is a sequence of wordpieces. Using wordpieces allows us to address out-of-vocabulary (OOV) word issues that would arise from having a fixed word vocabulary. In practice, a wordpiece RNNLM gives similar performance as a word-level model BIBREF16 . For about INLINEFORM1 of the segments, we were able to obtain visual features at the frame level. The features are 1500-dimensional vectors, extracted from the video frames at 1-second intervals, similar to those used for large scale image classification tasks BIBREF17 , BIBREF18 . For a INLINEFORM2 -second video and INLINEFORM3 wordpieces, each feature is uniformly allocated to INLINEFORM4 wordpieces.
> 
> Our RNNLM models consist of 2 LSTM layers, each containing 2048 units which are linearly projected to 512 units BIBREF19 . The word-piece and video embeddings are of size 512 each. We do not use dropout. During training, the batch size per worker is set to 256, and we perform full length unrolling to a max length of 70. The INLINEFORM0 -norms of the gradients are clipped to a max norm of INLINEFORM1 for the LSTM weights and to 10,000 for all other weights. We train with Synchronous SGD with the Adafactor optimizer BIBREF20 until convergence on a development set, created by randomly selecting INLINEFORM2 of all utterances.

### Relevance

Label: 

## Record 0042

Paper: Neural Language Modeling with Visual Features

### Question

> what features were derived from the videos?

### Passage

> We explore three locations for fusing visual features in an RNNLM (Figure ). Our Early Fusion strategy merges the text and the visual features at the input to the LSTM cells. This embodies the intuition that it is best to do feature combination at the earliest possible stage. The Middle Fusion merges the visual features at the output of the 1st LSTM layer while the Late Fusion strategies merges the two features after the final LSTM layer. The idea behind the Middle and Late fusion is that we would like to minimize changes to the regular RNNLM architecture at the early stages and still be able to benefit from the visual features.

### Relevance

Label: 

## Record 0043

Paper: Neural Language Modeling with Visual Features

### Question

> what features were derived from the videos?

### Passage

> For evaluation we used two datasets, YouCook2 and sth-sth, allowing us to evaluate our models in cases where the visual context is relevant to the modelled language. Note that no data from these datasets are present in the YouTube videos used for training. The perplexity of our models is shown in Table .

### Relevance

Label: 

## Record 0044

Paper: Neural Language Modeling with Visual Features

### Question

> what features were derived from the videos?

### Passage

> INLINEFORM0 Work performed while the author was an intern at Google.
> 
> Language models are vital components of a wide variety of systems for Natural Language Processing (NLP) including Automatic Speech Recognition, Machine Translation, Optical Character Recognition, Spelling Correction, etc. However, most language models are trained and applied in a manner that is oblivious to the environment in which human language operates BIBREF0 . These models are typically trained only on sequences of words, ignoring the physical context in which the symbolic representations are grounded, or ignoring the social context that could inform the semantics of an utterance.
> 
> For incorporating additional modalities, the NLP community has typically used datasets such as MS COCO BIBREF1 and Flickr BIBREF2 for image-based tasks, while several datasets BIBREF3 , BIBREF4 , BIBREF5 , BIBREF6 , BIBREF7 have been curated for video-based tasks. Despite the lack of big datasets, researchers have started investigating language grounding in images BIBREF8 , BIBREF9 , BIBREF10 and to lesser extent in videos BIBREF11 , BIBREF1 . However, language grounding has focused more on obtaining better word and sentence representations or other downstream tasks, and to lesser extent on language modeling.
> 
> In this paper, we examine the problem of incorporating temporal visual context into a recurrent neural language model (RNNLM). Multimodal Neural Language Models were introduced in BIBREF12 , where log-linear LMs BIBREF13 were conditioned to handle both image and text modalities. Notably, this work did not use the recurrent neural model paradigm which has now become the de facto way of implementing neural LMs.
> 
> The closest work to ours is that of BIBREF0 , who report perplexity gains of around 5–6% on three languages on the MS COCO dataset (with an English vocabulary of only 16K words).
> 
> Our work is distinguishable from previous work with respect to three dimensions:

### Relevance

Label: 

## Record 0045

Paper: Neural Language Modeling with Visual Features

### Question

> what features were derived from the videos?

### Passage

> We present a simple strategy to augment a standard recurrent neural network language model with temporal visual features. Through an exploration of candidate architectures, we show that the Middle Fusion of visual and textual features leads to a 20-28% reduction in perplexity relative to a text only baseline. These experiments were performed using datasets of unprecedented scale, with more than 1.2 billion tokens – two orders of magnitude more than any previously published work. Our work is a first step towards creating and deploying large-scale multimodal systems that properly situate themselves into a given context, by taking full advantage of every available signal.

### Relevance

Label: 

## Record 0046

Paper: Analysis of Speeches in Indian Parliamentary Debates

### Question

> What classification models were used?

### Passage

> In this section, we deal with two tasks, task one is the classification of the stances the speakers take and task two is the classification of categories based on purpose. Stance classification differs from sentiment analysis. For instance, the number of speeches that were annotated as for i.e 919 had only 719 labelled as positive and the number of speeches that were annotated as against i.e 282 had only 89 as negatively labelled. So, these statistics clearly indicate the difference between polarity detection and stance classification.
> 
> Text classification is a core task to many applications, like spam detection, sentiment analysis or smart replies. We used fastText and SVM BIBREF16 for preliminary experiments. We have pre-processed the text removing punctuation's and lowering the case. Facebook developers have developed fastText BIBREF17 which is a library for efficient learning of word representations and sentence classification. The reason we have used fastText is because of its promising results in BIBREF18 .
> 
> We divided our training and testing data in the ratio of 8:2 for classification. As mentioned above we used fastText and SVM for both the classification tasks. We report accuracy for each class as it is a multi-label classification problem. The results are shown in Table 7 and Table 8. Also, the parameters used for fastText is described in Table 9.
> 
> We have not used hs (Hierarchical Soft-max) for binary classification, instead used regular softmax as it was giving better results in fastText.
> 
> For SVM, the features were the word vectors trained using word2vec BIBREF19 with dimesion size of 300 whereas for fastText, the features were the word vectors trained using character n-gram embedding. We have achieved considerably good results. We plan to annotate more and check if the accuracy increase any further. The limitation that we feel is the number of annotations being done. We approached the classification problem as one vs rest classification problem. We performed the classification on document level. Later we would like to analyze at sentence level. The least accuracy was for Issue category and the highest is for Blame category. This research will inspire researchers to take on further research on mining appreciation, blaming from text in lines with the ongoing approaches

### Relevance

Label: 

## Record 0047

Paper: Analysis of Speeches in Indian Parliamentary Debates

### Question

> What classification models were used?

### Passage

> We have annotated 1201 speeches with the four categories mentioned above, on the speeches. We also annotated stances of the speakers towards the bill/issue that is being debated on. There are two stances one is for and other is against. The statistics of the annotated data is shown in Table 4.
> 
> Two humanities students were involved in the annotation of the four categories on 1201 speeches. The annotator agreement is shown in Table 5 and is evaluated using two metrics, one is the Kohen's Kappa BIBREF12 and other is the inter annotator agreement which is the percentage of overlapping choices between the annotators.
> 
> The inter annotator agreement for the stance categories were 0.92. The high values of inter annotator scores clearly explain how easy it was to delineate each category. It also signifies that the definition of the category that needed to be annotated, were very clear.

### Relevance

Label: 

## Record 0048

Paper: Analysis of Speeches in Indian Parliamentary Debates

### Question

> What classification models were used?

### Passage

> The creation of the dataset involved 3 steps. The first step was to scrap the pdf files from the Lok Sabha website. Each pdf file is a session. The second step was to convert the pdf files into text files for easy parsing. The challenge here was to convert this unstructured information into a structured format. The third step is to extract relevant data using pattern matching. We developed a software parser for extracting the entities such as date, debate type, member name and speech. We used regex, pattern matching code to find out patterns from the text file. For example to segregate a speaker's name from his speech, we used :
> 
> re.split(":")
> 
> as name of the speaker and his/her speech is separated by a colon. An example pdf can be accessed using this URL . Right now, member name and bill name are needed to be stored manually which we plan to automate too. Sometimes the pattern matching fails due to irregularities in the pdf as those were written by humans though they were negligible. We stored the structured data into a Mongo database as different debate types have different schema. The database consists of the following tables :
> 
> Sessions : all the debates happened on a particular day with date, secretary general name.
> 
> Members : information about the members/speakers of the parliament i.e name and party affiliation.
> 
> Debates : contains the member id and the corresponding speeches, summaries and keywords.
> 
> Bills : the name of the bill.
> 
> Debate Type : the name of the debate type.
> 
> The software parser developed is very generic. As new sessions are being added on the Lok Sabha website, the software parser automatically identifies them, parses it and stores the structured data in the database. The database has been hosted in a online database hosting site, mLab. The mongo shell can be accessed using this command in any linux machine which has mongo installed.
> 
> mongo ds235388.mlab.com:35388/synopsis -u public -p public

### Relevance

Label: 

## Record 0049

Paper: Analysis of Speeches in Indian Parliamentary Debates

### Question

> What classification models were used?

### Passage

> As the world moves towards increasing forms of digitization, the creation of text corpora has become an important activity for NLP and other fields of research. Parliamentary data is a rich corpus of discourse on a wide array of topics. The Lok Sabha website provides access to all kinds of reports, debates, bills related to the proceedings of the house. Similarly, the Rajya Sabha website also contains debates, bills, reports introduced in the house. The Lok Sabha website also contains information about members of the parliament who are elected by the people and debate in the house. Since the data is unstructured , it cannot be computationally analyzed. There is a need to shape the data into a structured format for analysis. This data is important as it can be used to visualize person, party and agenda level semantics in the house.
> 
> The data that we get from parliamentary proceedings has presence of sarcasm, interjections and allegations which makes it difficult to apply standard NLP techniques BIBREF0 . Members of the parliament discuss various important aspects and there is a strong purpose behind every speech. We wanted to analyze this particular aspect. Traditional polar stances (for or against) do not justify for the diplomatic intricacies in the speeches. We created this taxonomy to better understand the semantics i.e the pragmatics of the speeches and to give enriched insights into member's responses in a speech. The study of the speaker's meaning, not focusing on the phonetic or grammatical form of an utterance, but instead on what the speaker's intentions and beliefs are is pragmatics. Pragmatics is a sub-field of linguistics and semiotics that studies the ways in which context contributes to meaning.
> 
> After thorough investigation of many speeches we found that the statements made by members cannot be deemed strictly "for or against" a bill or government. A person maybe appreciating a bill or government's effort in one part of a speech but also asking attention to other contentious issues. Similarly, a person criticizing government for an irresponsible action could be giving some constructive suggestions elsewhere. A political discourse may not always be polar and might have a higher spectrum of meaning. After investigating and highlighting

### Relevance

Label: 

## Record 0050

Paper: Analysis of Speeches in Indian Parliamentary Debates

### Question

> What classification models were used?

### Passage

> In future, we would like to increase the size of the dataset by including sessions of previous years which are not yet digitized. Sessions before 2009 are yet to be digitalised by the Lok Sabha editorial of India. Also we plan to include Rajya Sabha debates into the dataset. We have used fastText for classifying categories. We plan to develop a set of features to increase the accuracy of the classification task as we believe that features like party affiliation will have greater impact and experiment with other machine learning approaches.
> 
> TextRank is used for summarization. We feel that for political debates, summarization should emphasize on arguments made by members unlike TextRank. In the whole debate, a lot of themes are raised by the members. The debate revolves around these themes. So, developing a model for thematic summarization with arguments will capture the complete picture of the entire debate unlike TextRank. We plan to do this as our future work on these debates. A short summary of the important themes discussed with its arguments will benefit journalists, newspaper editors, common people etc.

### Relevance

Label: 

## Record 0051

Paper: Unfolding and Shrinking Neural Machine Translation Ensembles

### Question

> Do they explore other language pairs?

### Passage

> The top systems in recent machine translation evaluation campaigns on various language pairs use ensembles of a number of NMT systems BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 , BIBREF6 . Ensembling BIBREF7 , BIBREF8 of neural networks is a simple yet very effective technique to improve the accuracy of NMT. The decoder makes use of INLINEFORM0 NMT networks which are either trained independently BIBREF9 , BIBREF2 , BIBREF3 , BIBREF4 or share some amount of training iterations BIBREF10 , BIBREF1 , BIBREF5 , BIBREF6 . The ensemble decoder computes predictions from each of the individual models which are then combined using the arithmetic average BIBREF9 or the geometric average BIBREF5 .
> 
> Ensembling consistently outperforms single NMT by a large margin. However, the decoding speed is significantly worse since the decoder needs to apply INLINEFORM0 NMT models rather than only one. Therefore, a recent line of research transfers the idea of knowledge distillation BIBREF11 , BIBREF12 to NMT and trains a smaller network (the student) by minimizing the cross-entropy to the output of the ensemble system (the teacher) BIBREF13 , BIBREF14 . This paper presents an alternative to knowledge distillation as we aim to speed up decoding to be comparable to single NMT while retaining the boost in translation accuracy from the ensemble. In a first step, we describe how to construct a single large neural network which imitates the output of an ensemble of multiple networks with the same topology. We will refer to this process as unfolding. GPU-based decoding with the unfolded network is often much faster than ensemble decoding since more work can be done on the GPU. In a second step, we explore methods to reduce the size of the unfolded network. This idea is justified by the fact that ensembled neural networks are often over-parameterized and have a large degree of redundancy BIBREF15 , BIBREF16 , BIBREF17 . Shrinking the unfolded network leads to a smaller model which consumes less space on the disk and in the memory; a crucial factor on mobile devices. More importantly, the decoding speed on all platforms benefits greatly from the reduced number of neurons. We find that the dimensionality of

### Relevance

Label: 

## Record 0052

Paper: Unfolding and Shrinking Neural Machine Translation Ensembles

### Question

> Do they explore other language pairs?

### Passage

> After constructing the weight matrices of the unfolded network we reduce the size of it by iteratively shrinking layer sizes. In this section we denote the incoming weight matrix of the layer to shrink as INLINEFORM0 and the outgoing weight matrix as INLINEFORM1 . Our procedure is inspired by the method of Srinivas and Babu sparsify-datafree. They propose a criterion for removing neurons in inner layers of the network based on two intuitions. First, similarly to Hebb's learning rule, they detect redundancy by the principle neurons which fire together, wire together. If the incoming weight vectors INLINEFORM2 and INLINEFORM3 are exactly the same for two neurons INLINEFORM4 and INLINEFORM5 , we can remove the neuron INLINEFORM6 and add its outgoing connections to neuron INLINEFORM7 ( INLINEFORM8 ) without changing the output. This holds since the activity in neuron INLINEFORM14 will always be equal to the activity in neuron INLINEFORM15 . In practice, Srinivas and Babu use a distance measure based on the difference of the incoming weight vectors to search for similar neurons as exact matches are very rare.
> 
> The second intuition of the criterion used by Srinivas and Babu sparsify-datafree is that neurons with small outgoing weights contribute very little overall. Therefore, they search for a pair of neurons INLINEFORM0 according the following term and remove the INLINEFORM1 -th neuron. DISPLAYFORM0
> 
> Neuron INLINEFORM0 is selected for removal if (1) there is another neuron INLINEFORM1 which has a very similar set of incoming weights and if (2) INLINEFORM2 has a small outgoing weight vector. Their criterion is data-free since it does not require any training data. For further details we refer to Srinivas and Babu sparsify-datafree.

### Relevance

Label: 

## Record 0053

Paper: Unfolding and Shrinking Neural Machine Translation Ensembles

### Question

> Do they explore other language pairs?

### Passage

> INLINEFORM4 in the unfolded network is increased by factor INLINEFORM5 if INLINEFORM6 is an inner layer, and equal to INLINEFORM7 if INLINEFORM8 is the input or output layer. We denote the weight matrix between two layers INLINEFORM9 in the INLINEFORM10 -th individual model ( INLINEFORM11 ) as INLINEFORM12 , and the corresponding weight matrix in the unfolded network as INLINEFORM13 . We explicitly allow INLINEFORM14 and INLINEFORM15 to be non-consecutive or reversed to be able to model recurrent networks. We use the zero-matrix if layers INLINEFORM16 and INLINEFORM17 are not connected. The construction of the unfolded weight matrix INLINEFORM18 from the individual matrices INLINEFORM19 depends on whether the connected layers are inner layers or not. The complete formula is listed in Fig. FIGREF5 .
> 
> Unfolded NMT networks approximate but do not exactly match the output of the ensemble due to two reasons. First, the unfolded network synchronizes the attentions of the individual models. Each decoding step in the unfolded network computes a single attention weight vector. In contrast, ensemble decoding would compute one attention weight vector for each of the INLINEFORM0 input models. A second difference is that the ensemble decoder first applies the softmax at the output layer, and then averages the prediction probabilities. The unfolded network averages the neuron activities (i.e. the logits) first, and then applies the softmax function. Interestingly, as shown in Sec. SECREF4 , these differences do not have any impact on the BLEU score but yield potential speed advantages of unfolding since the computationally expensive softmax layer is only applied once.

### Relevance

Label: 

## Record 0054

Paper: Unfolding and Shrinking Neural Machine Translation Ensembles

### Question

> Do they explore other language pairs?

### Passage

> Srinivas and Babu sparsify-datafree propose to add the outgoing weights of INLINEFORM0 to the weights of a similar neuron INLINEFORM1 to compensate for the removal of INLINEFORM2 . However, we have found that this approach does not work well on NMT networks. We propose instead to compensate for the removal of a neuron by a linear combination of the remaining neurons in the layer. Data-free shrinking assumes for the sake of deriving the update rule that the neuron activation function is linear. We now ask the following question: How can we compensate as well as possible for the loss of neuron INLINEFORM3 such that the impact on the output of the whole network is minimized? Data-free shrinking represents the incoming weight vector of neuron INLINEFORM4 ( INLINEFORM5 ) as linear combination of the incoming weight vectors of the other neurons. The linear factors can be found by satisfying the following linear system: DISPLAYFORM0
> 
> where INLINEFORM0 is matrix INLINEFORM1 without the INLINEFORM2 -th column. In practice, we use the method of ordinary least squares to find INLINEFORM3 because the system may be overdetermined. The idea is that if we mix the outputs of all neurons in the layer by the INLINEFORM4 -weights, we get the output of the INLINEFORM5 -th neuron. The row vector INLINEFORM6 contains the contributions of the INLINEFORM7 -th neuron to each of the neurons in the next layer. Rather than using these connections, we approximate their effect by adding some weight to the outgoing connections of the other neurons. How much weight depends on INLINEFORM8 and the outgoing weights INLINEFORM9 . The factor INLINEFORM10 which we need to add to the outgoing connection of the INLINEFORM11 -th neuron to compensate for the loss of the INLINEFORM12 -th neuron on the INLINEFORM13 -th neuron in the next layer is: DISPLAYFORM0
> 
> Therefore, the update rule for INLINEFORM0 is: DISPLAYFORM0
> 
> In the remainder we will refer to this method as data-free shrinking. Note that we recover the update rule of Srinivas and Babu sparsify-datafree by setting INLINEFORM0 to the INLINEFORM1 -th unit vector. Also note that the error introduced by our shrinking method is due to the fact that we ignore the non-linearity, and that

### Relevance

Label: 

## Record 0055

Paper: Unfolding and Shrinking Neural Machine Translation Ensembles

### Question

> Do they explore other language pairs?

### Passage

> We have described a generic method for improving the decoding speed and BLEU score of single system NMT. Our approach involves unfolding an ensemble of multiple systems into a single large neural network and shrinking this network by removing redundant neurons. Our best results on Japanese-English either yield a gain of 2.2 BLEU compared to the original single NMT network at about the same decoding speed, or a INLINEFORM0 CPU decoding speed up with only a minor drop in BLEU.
> 
> The current formulation of unfolding works for networks of the same topology as the concatenation of layers is only possible for analogous layers in different networks. Unfolding and shrinking diverse networks could be possible, for example by applying the technique only to the input and output layers or by some other scheme of finding associations between units in different models, but we leave this investigation to future work as models in NMT ensembles in current research usually have the same topology BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 , BIBREF4 , BIBREF6 .

### Relevance

Label: 

## Record 0056

Paper: Offensive Language and Hate Speech Detection for Danish

### Question

> How large was the dataset of Danish comments?

### Passage

> in Europe (GDPR) and the increased concern for online privacy, we applied some necessary pre-processing steps on our dataset to ensure the privacy of the authors of the comments that were used. Personally identifying content (such as the names of individuals, not including celebrity names) was removed. This was handled by replacing each name of an individual (i.e. author or subject) with @USER, as presented in both BIBREF0 and BIBREF2 . All comments containing any sensitive information were removed. We classify sensitive information as any information that can be used to uniquely identify someone by the following characteristics; racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic data, and bio-metric data.
> 
> We base our annotation procedure on the guidelines and schemas presented in BIBREF0 , discussed in detail in section "Classification Structure" . As a warm-up procedure, the first 100 posts were annotated by two annotators (the author and the supervisor) and the results compared. This was used as an opportunity to refine the mutual understanding of the task at hand and to discuss the mismatches in these annotations for each sub-task.
> 
> We used a Jaccard index BIBREF18 to assess the similarity of our annotations. In sub-task A the Jaccard index of these initial 100 posts was 41.9%, 39.1% for sub-task B , and 42.8% for sub-task C. After some analysis of these results and the posts that we disagreed on it became obvious that to a large extent the disagreement was mainly caused by two reasons:
> 
> Guesswork of the context where the post itself was too vague to make a decisive decision on whether it was offensive or not without more context. An example of this is a post such as Skal de hjælpes hjem, næ nej de skal sendes hjem, where one might conclude, given the current political climate, that this is an offensive post targeted at immigrants. The context is, however, lacking so we cannot make a decisive decision. This post should, therefore, be labeled as non-offensive, since the post does not contain any profanity or a clearly stated group.
> 
> Failure to label posts containing some kind of profanity as offensive (typically when the posts themselves were

### Relevance

Label: 

## Record 0057

Paper: Offensive Language and Hate Speech Detection for Danish

### Question

> How large was the dataset of Danish comments?

### Passage

> Offensive language in user-generated content on online platforms and its implications has been gaining attention over the last couple of years. This interest is sparked by the fact that many of the online social media platforms have come under scrutiny on how this type of content should be detected and dealt with. It is, however, far from trivial to deal with this type of language directly due to the gigantic amount of user-generated content created every day. For this reason, automatic methods are required, using natural language processing (NLP) and machine learning techniques.
> 
> Given the fact that the research on offensive language detection has to a large extent been focused on the English language, we set out to explore the design of models that can successfully be used for both English and Danish. To accomplish this, an appropriate dataset must be constructed, annotated with the guidelines described in BIBREF0 . We, furthermore, set out to analyze the linguistic features that prove hard to detect by analyzing the patterns that prove hard to detect.

### Relevance

Label: 

## Record 0058

Paper: Offensive Language and Hate Speech Detection for Danish

### Question

> How large was the dataset of Danish comments?

### Passage

> suitable source of data for our task. This is due to the fact that Twitter has limited usage in Denmark, resulting in low quality data with many classes of interest unrepresented.
> 
> Facebook. We next considered Facebook, and the public page for the Danish media company Ekstra Bladet. We looked at user-generated comments on articles posted by Ekstra Bladet, and initial analysis of these comments showed great promise as they have a high degree of variation. The user behaviour on the page and the language used ranges from neutral language to very aggressive, where some users pour out sexist, racist and generally hateful language. We faced obstacles when collecting data from Facebook, due to the fact that Facebook recently made the decision to shut down all access to public pages through their developer interface. This makes computational data collection approaches impossible. We faced restrictions on scraping public pages with Facebook, and turned to manual collection of randomly selected user-generated comments from Ekstra Bladet's public page, yielding 800 comments of sufficient quality.
> 
> Reddit. Given that language classification tasks in general require substantial amounts of data, our exploration for suitable sources continued and our search next led us to Reddit. We scraped Reddit, collecting the top 500 posts from the Danish sub-reddits r/DANMAG and r/Denmark, as well as the user comments contained within each post.
> 
> We published a survey on Reddit asking Danish speaking users to suggest offensive, sexist, and racist terms for a lexicon. Language and user behaviour varies between platforms, so the goal is to capture platform-specific terms. This gave 113 offensive and hateful terms which were used to find offensive comments. The remainder of comments in the corpus were shuffled and a subset of this corpus was then used to fill the remainder of the final dataset. The resulting dataset contains 3600 user-generated comments, 800 from Ekstra Bladet on Facebook, 1400 from r/DANMAG and 1400 from r/Denmark. In light of the General Data Protection Regulations in Europe (GDPR) and the increased concern for online privacy, we applied some necessary pre-processing steps on our dataset to ensure the privacy of the authors of the comments that were used. Personally identifying content (such as the names of

### Relevance

Label: 

## Record 0059

Paper: Offensive Language and Hate Speech Detection for Danish

### Question

> How large was the dataset of Danish comments?

### Passage

> In Table 1 the distribution of samples by sources in our final dataset is presented. Although a useful tool, using the hate speech lexicon as a filter only resulted in 232 comments. The remaining comments from Reddit were then randomly sampled from the remaining corpus.
> 
> The fully annotated dataset was split into a train and test set, while maintaining the distribution of labels from the original dataset. The training set contains 80% of the samples, and the test set contains 20%. Table 2 presents the distribution of samples by label for both the train and test set. The dataset is skewed, with around 88% of the posts labeled as not offensive (NOT). This is, however, generally the case when it comes to user-generated content on online platforms, and any automatic detection system needs be able to handle the problem of imbalanced data in order to be truly effective.

### Relevance

Label: 

## Record 0060

Paper: Offensive Language and Hate Speech Detection for Danish

### Question

> How large was the dataset of Danish comments?

### Passage

> Offensive content is broken into three sub-tasks to be able to effectively identify both the type and the target of the offensive posts. These three sub-tasks are chosen with the objective of being able to capture different types of offensive language, such as hate speech and cyberbullying (section "Background" ).
> 
> In sub-task A the goal is to classify posts as either offensive or not. Offensive posts include insults and threats as well as any form of untargeted profanity BIBREF17 . Each sample is annotated with one of the following labels:
> 
> In English this could be a post such as #TheNunMovie was just as scary as I thought it would be. Clearly the critics don't think she is terrifyingly creepy. I like how it ties in with #TheConjuring series. In Danish this could be a post such as Kim Larsen var god, men hans død blev alt for hyped.
> 
> . In English this could be a post such as USER is a #pervert himself!. In Danish this could be a post such as Kalle er faggot...
> 
> In sub-task B the goal is to classify the type of offensive language by determining if the offensive language is targeted or not. Targeted offensive language contains insults and threats to an individual, group, or others BIBREF17 . Untargeted posts contain general profanity while not clearly targeting anyone BIBREF17 . Only posts labeled as offensive (OFF) in sub-task A are considered in this task. Each sample is annotated with one of the following labels:
> 
> Targeted Insult (TIN). In English this could be a post such as @USER Please ban this cheating scum. In Danish this could be e.g. Hun skal da selv have 99 år, den smatso.
> 
> Untargeted (UNT). In English this could be a post such as 2 weeks of resp done and I still don't know shit my ass still on vacation mode. In Danish this could e.g. Dumme svin...
> 
> In sub-task C the goal is to classify the target of the offensive language. Only posts labeled as targeted insults (TIN) in sub-task B are considered in this task BIBREF17 . Samples are annotated with one of the following:
> 
> Individual (IND): Posts targeting a named or unnamed person

### Relevance

Label: 

## Record 0061

Paper: Conflict as an Inverse of Attention in Sequence Relationship

### Question

> Which neural architecture do they use as a base for their attention conflict mechanisms?

### Passage

> Bahdanau et al. BIBREF2 introduced attention first in neural machine translation. It used a feed-forward network over addition of encoder and decoder states to compute alignment score. Our work is very similar to this except we use element wise difference instead of addition to build our conflict function. BIBREF3 came up with a scaled dot-product attention in their Transformer model which is fast and memory-efficient. Due to the scaling factor, it didn't have the issue of gradients zeroing out. On the other hand, BIBREF4 has experimented with global and local attention based on the how many hidden states the attention function takes into account. Their experiments have revolved around three attention functions - dot, concat and general. Their findings include that dot product works best for global attention. Our work also belongs to the global attention family as we consider all the hidden states of the sequence.
> 
> Attention has been widely used in pair-classification problems like natural language inference. Wang et al. BIBREF5 introduced BIMPM which matched one sequence with another in four different fashion but one single matching function which they used as cosine. Liu et al. BIBREF6 proposed SAN for language inference which also used dot-product attention between the sequences.
> 
> Summarizing, attention has helped in achieving state-of-the-art results in NLI and QA. Prior work in attention has been mostly in similarity based approaches while our work focuses on non-matching sequences.

### Relevance

Label: 

## Record 0062

Paper: Conflict as an Inverse of Attention in Sequence Relationship

### Question

> Which neural architecture do they use as a base for their attention conflict mechanisms?

### Passage

> Multi-head attention, as introduced in BIBREF3 , computes multiple identical attention mechanism parallelly on multiple linear projections of same inputs. The parameters of each attention and projections are different in each head. Finally, they concatenate all the attentions which is similar to how we concatenate conflict and attention. However, they use dot-product to compute each of the attention.
> 
> Our combined model that contains both attention and conflict can be thought of as a 2-head attention model but both heads are different. Our conflict head explicitly captures difference between the inputs.

### Relevance

Label: 

## Record 0063

Paper: Conflict as an Inverse of Attention in Sequence Relationship

### Question

> Which neural architecture do they use as a base for their attention conflict mechanisms?

### Passage

> We propose a different mechanism that does the opposite of what attention does that is computing how much two sequences repel each other. This works very similar to how attention works but inversely.
> 
> We demonstrate a general model but we also realize that there can be other variants of it which may be worked out to perform better. Our approach consists of using element wise difference between two vectors followed by a linear transformation to produce a scalar weight. The remaining of the process acts similar to how attention works. Mathematically, we can express it as: DISPLAYFORM0
> 
> where INLINEFORM0 INLINEFORM1 INLINEFORM2 is a parameter that we introduce to provide a weight for the pair. The two word representations INLINEFORM3 and INLINEFORM4 are projected to a space where their element wise difference can be used to model their dissimilarity and softmax applied on them can produce high probability to more dissimilar word pairs.
> 
> It is good to note that conflict suffers from the same limitation that attention suffers from. This is when a pair of sentences are highly matching especially with multiple associations. But when the two methods work together, each compensates for the other's shortcomings.

### Relevance

Label: 

## Record 0064

Paper: Conflict as an Inverse of Attention in Sequence Relationship

### Question

> Which neural architecture do they use as a base for their attention conflict mechanisms?

### Passage

> We also show qualitative results where we can observe that our model with attention and conflict combined does better on cases where pairs are non-duplicate and has very small difference. We have observed that the conflict model is very sensitive to even minor differences and compensates in such cases where attention poses high bias towards similarities already there in the sequences.
> 
> Sequence 1: What are the best ways to learn French ?
> 
> Sequence 2: How do I learn french genders ?
> 
> Attention only: 1
> 
> Attention+Conflict: 0
> 
> Ground Truth: 0
> 
> Sequence 1: How do I prevent breast cancer ?
> 
> Sequence 2: Is breast cancer preventable ?
> 
> Attention only: 1
> 
> Attention+Conflict: 0
> 
> Ground Truth: 0
> 
> We provide two examples with predictions from the models with only attention and combination of attention and conflict. Each example is accompanied by the ground truth in our data.

### Relevance

Label: 

## Record 0065

Paper: Conflict as an Inverse of Attention in Sequence Relationship

### Question

> Which neural architecture do they use as a base for their attention conflict mechanisms?

### Passage

> We used two weighted representations of INLINEFORM0 using weights of attention and conflict as computed in Eqn. (4) and (8) respectively. Our final representation of a word representation INLINEFORM1 conditioned on INLINEFORM2 can be expressed as: DISPLAYFORM0
> 
> where A and C denote that they are from attention and conflict models respectively.

### Relevance

Label: 

## Record 0066

Paper: Morphological Word Segmentation on Agglutinative Languages for Neural Machine Translation

### Question

> How is morphology knowledge implemented in the method?

### Passage

> In this paper, we investigate morphological segmentation strategies on the low-resource and morphologically-rich languages of Turkish and Uyghur. Experimental results show that our proposed morphologically motivated word segmentation method is better suitable for NMT. And the BPE-SSS strategy achieves the best machine translation performance, as it can better preserve the syntactic and semantic information of the words with complex morphology as well as reduce the vocabulary size for model training. Moreover, we also estimate how the number of merge operations on the stem units for BPE-SSS strategy effects the translation quality, and we find that an appropriate vocabulary size is more useful for the NMT model.
> 
> In future work, we are planning to incorporate more linguistic and morphology knowledge into the training process of NMT to enhance its capacity of capturing syntactic structure and semantic information on the low-resource and morphologically-rich languages.

### Relevance

Label: 

## Record 0067

Paper: Morphological Word Segmentation on Agglutinative Languages for Neural Machine Translation

### Question

> How is morphology knowledge implemented in the method?

### Passage

> We employ the Transformer model BIBREF13 with self-attention mechanism architecture implemented in Sockeye toolkit BIBREF14. Both the encoder and decoder have 6 layers. We set the number of hidden units to 512, the number of heads for self-attention to 8, the source and target word embedding size to 512, and the number of hidden units in feed-forward layers to 2048. We train the NMT model by using the Adam optimizer BIBREF15 with a batch size of 128 sentences, and we shuffle all the training data at each epoch. The label smoothing is set to 0.1. We report the result of averaging the parameters of the 4 best checkpoints on the validation perplexity. Decoding is performed by beam search with beam size of 5. To effectively evaluate the machine translation quality, we report case-sensitive BLEU score with standard tokenization and character n-gram ChrF3 score .

### Relevance

Label: 

## Record 0068

Paper: Morphological Word Segmentation on Agglutinative Languages for Neural Machine Translation

### Question

> How is morphology knowledge implemented in the method?

### Passage

> Neural machine translation (NMT) has achieved impressive performance on machine translation task in recent years for many language pairs BIBREF0, BIBREF1, BIBREF2. However, in consideration of time cost and space capacity, the NMT model generally employs a limited-size vocabulary that only contains the top-N highest frequency words (commonly in the range of 30K to 80K) BIBREF3, which leads to the Out-of-Vocabulary (OOV) problem following with inaccurate and terrible translation results. Research indicated that sentences with too many unknown words tend to be translated much more poorly than sentences with mainly frequent words. For the low-resource and source-side morphologically-rich machine translation tasks, such as Turkish-English and Uyghur-Chinese, all the above issues are more serious due to the fact that the NMT model cannot effectively identify the complex morpheme structure or capture the linguistic and semantic information with too many rare and unknown words in the training corpus.
> 
> Both the Turkish and Uyghur are agglutinative and highly-inflected languages in which the word is formed by suffixes attaching to a stem BIBREF4. The word consists of smaller morpheme units without any splitter between them and its structure can be denoted as “stem + suffix1 + suffix2 + ... + suffixN”. A stem is attached in the rear by zero to many suffixes that have many inflected and morphological variants depending on case, number, gender, and so on. The complex morpheme structure and relatively free constituent order can produce very large vocabulary because of the derivational morphology, so when translating from the agglutinative languages, many words are unseen at training time. Moreover, due to the semantic context, the same word generally has different segmentation forms in the training corpus.
> 
> For the purpose of incorporating morphology knowledge of agglutinative languages into word segmentation for NMT, we propose a morphological word segmentation method on the source-side of Turkish-English and Uyghur-Chinese machine translation tasks, which segments the complex words into simple and effective morpheme units while reducing the vocabulary size for model training. In this paper, we investigate and compare the following segmentation strategies:
> 
> Stem with combined suffix
> 
> Stem with singular suffix
> 
> Byte Pair Encoding (BPE)
> 
> BPE on stem with combined suffix
> 
> BPE on stem with singular suffix
> 
> The latter two segmentation

### Relevance

Label: 

## Record 0069

Paper: Morphological Word Segmentation on Agglutinative Languages for Neural Machine Translation

### Question

> How is morphology knowledge implemented in the method?

### Passage

> The NMT system is typically trained with a limited vocabulary, which creates bottleneck on translation accuracy and generalization capability. Many word segmentation methods have been proposed to cope with the above problems, which consider the morphological properties of different languages.
> 
> Bradbury and Socher BIBREF16 employed the modified Morfessor to provide morphology knowledge into word segmentation, but they neglected the morphological varieties between subword units, which might result in ambiguous translation results. Sanchez-Cartagena and Toral BIBREF17 proposed a rule-based morphological word segmentation for Finnish, which applies BPE on all the morpheme units uniformly without distinguishing their inner morphological roles. Huck BIBREF18 explored target-side segmentation method for German, which shows that the cascading of suffix splitting and compound splitting with BPE can achieve better translation results. Ataman et al. BIBREF19 presented a linguistically motivated vocabulary reduction approach for Turkish, which optimizes the segmentation complexity with constraint on the vocabulary based on a category-based hidden markov model (HMM). Our work is closely related to their idea while ours are more simple and realizable. Tawfik et al. BIBREF20 confirmed that there is some advantage from using a high accuracy dialectal segmenter jointly with a language independent word segmentation method like BPE. The main difference is that their approach needs sufficient monolingual data additionally to train a segmentation model while ours do not need any external resources, which is very convenient for word segmentation on the low-resource and morphologically-rich agglutinative languages.

### Relevance

Label: 

## Record 0070

Paper: Morphological Word Segmentation on Agglutinative Languages for Neural Machine Translation

### Question

> How is morphology knowledge implemented in the method?

### Passage

> According to Table 6 and Table 7, we can find that both the BPE-SCS and BPE-SSS strategies outperform morpheme segmentation and the strong baseline of pure BPE method. Especially, the BPE-SSS strategy is better and it achieves significant improvement of up to 1.2 BLEU points on Turkish-English machine translation task and 2.5 BLEU points on Uyghur-Chinese machine translation task. Furthermore, we also find that the translation performance of our proposed segmentation strategy on Turkish-English machine translation task is not obvious than Uyghur-Chinese machine translation task, the probable reasons are: the training corpus of Turkish-English consists of talk and news data while most of the talk data are short informal sentences compared with the news data, which cannot provide more language information for the NMT model. Moreover, the test corpus consists of news data, so due to the data domain is different, the improvement of machine translation quality is limited.
> 
> In addition, we estimate how the number of merge operations on the stem units for BPE-SSS strategy effects the machine translation quality. Experimental results are shown in Table 8 and Table 9. We find that the number of 25K for Turkish, 30K and 35K for Uyghur maximizes the translation performance. The probable reason is that these numbers of merge operations are able to generate a more appropriate vocabulary that containing effective morpheme units and moderate subword units, which makes better generalization over the morphologically-rich words.

### Relevance

Label: 

## Record 0071

Paper: Enhancing PIO Element Detection in Medical Text Using Contextualized Embedding

### Question

> what shortcomings of previous datasets are mentioned?

### Passage

> The classification model is built on top of the BERT representation by adding a dense layer corresponding to the multi-label classifier with three output neurons corresponding to PIO labels. In order to insure that independent probabilities are assigned to the labels, as a loss function we have chosen the binary cross entropy with logits (BCEWithLogits) defined by DISPLAYFORM0
> 
> where t and y are the target and output vectors, respectively; n is the number of independent targets (n=3). The outputs are computed by applying the logistic function to the weighted sums of the last hidden layer activations, s, DISPLAYFORM0 DISPLAYFORM1
> 
> For the original BERT model, we have chosen the smallest uncased model, Bert-Base. The model has 12 attention layers and all texts are converted to lowercase by the tokenizer BIBREF9 . The architecture of the model is illustrated in Figure FIGREF7 .
> 
> Using this framework, we trained the model using the two pretrained embedding models described in the previous section. It is worth to mention that the embedding is contextualized during the training phase. For both models, the pretrained embedding layer is frozen during the first epoch (the embedding vectors are not updated). After the first epoch, the embedding layer is unfrozen and the vectors are fine-tuned for the classification task during training. The advantage of this approach is that few parameters need to be learned from scratch BIBREF16 , BIBREF11 , BIBREF9 .

### Relevance

Label: 

## Record 0072

Paper: Enhancing PIO Element Detection in Medical Text Using Contextualized Embedding

### Question

> what shortcomings of previous datasets are mentioned?

### Passage

> Evidence-based medicine (EBM) is of primary importance in the medical field. Its goal is to present statistical analyses of issues of clinical focus based on retrieving and analyzing numerous papers in the medical literature BIBREF0 . The PubMed database is one of the most commonly used databases in EBM BIBREF1 .
> 
> Biomedical papers, describing randomized controlled trials in medical intervention, are published at a high rate every year. The volume of these publications makes it very challenging for physicians to find the best medical intervention for a given patient group and condition BIBREF2 . Computational methods and natural language processing (NLP) could be adopted in order to expedite the process of biomedical evidence synthesis. Specifically, NLP tasks applied to well structured documents and queries can help physicians extract appropriate information to identify the best available evidence in the context of medical treatment.
> 
> Clinical questions are formed using the PIO framework, where clinical issues are broken down into four components: Population/Problem (P), Intervention (I), Comparator (C), and Outcome (O). We will refer to these categories as PIO elements, by using the common practice of merging the C and I categories. In BIBREF3 a literature screening performed in 10 systematic reviews was studied. It was found that using the PIO framework can significantly improve literature screening efficacy. Therefore, efficient extraction of PIO elements is a key feature of many EBM applications and could be thought of as a multi-label sentence classification problem.
> 
> Previous works on PIO element extraction focused on classical NLP methods, such as Naive Bayes (NB), Support Vector Machines (SVM) and Conditional Random Fields (CRF) BIBREF4 , BIBREF5 . These models are shallow and limited in terms of modeling capacity. Furthermore, most of these classifiers are trained to extract PIO elements one by one which is sub-optimal since this approach does not allow the use of shared structure among the individual classifiers.
> 
> Deep neural network models have increased in popularity in the field of NLP. They have pushed the state of the art of text representation and information retrieval. More specifically, these techniques enhanced NLP algorithms through the use of contextualized text embeddings at word, sentence, and paragraph levels BIBREF6 , BIBREF7 , BIBREF8 ,

### Relevance

Label: 

## Record 0073

Paper: Enhancing PIO Element Detection in Medical Text Using Contextualized Embedding

### Question

> what shortcomings of previous datasets are mentioned?

### Passage

> We further applied ensemble methods to enhance the model. This approach consists of combining predictions from base classifiers with features of the input data to increase the accuracy of the model BIBREF17 .
> 
> We investigate an important family of ensemble methods known as boosting, and more specifically a Light Gradient Boosting Machine (LGBM) algorithm, which consists of an implementation of fast gradient boosting on decision trees. In this study, we use a library implemented by Microsoft BIBREF18 . In our model, we learn a linear combination of the prediction given by the base classifiers and the input text features to predict the labels. As features, we consider the average term frequency-inverse document frequency (TF-IDF) score for each instance and the frequency of occurrence of quantitative information elements (QIEF) (e.g. percentage, population, dose of medicine). Finally, the output of the binary cross entropy with logits layer (predicted probabilities for the three classes) and the feature information are fed to the LGBM.
> 
> We train the base classifier using the original training dataset, using INLINEFORM0 of the whole data as training dataset, and use a five-fold cross-validation framework to train the LGBM on the remaining INLINEFORM1 of the data to avoid any information leakage. We train the LGBM on four folds and test on the excluded one and repeat the process for all five folds.
> 
> The results of the LGBM classifier for the different boosting frameworks and the scores from the base classifiers are illustrated in Table TABREF14 . The highest average ROC_AUC score of 0.9998 is obtained in the case of combining the two base learners along with the TF-IDF and QIEF features.

### Relevance

Label: 

## Record 0074

Paper: Enhancing PIO Element Detection in Medical Text Using Contextualized Embedding

### Question

> what shortcomings of previous datasets are mentioned?

### Passage

> In this study, we introduce PICONET, a multi-label dataset consisting of sequences with labels Population/Problem (P), Intervention (I), and Outcome (O). This dataset was created by collecting structured abstracts from PubMed and carefully choosing abstract headings representative of the desired categories. The present approach is an improvement over a similar approach used in BIBREF12 .
> 
> Our aim was to perform automatic labeling while removing as much ambiguity as possible. We performed a search on April 11, 2019 on PubMed for 363,078 structured abstracts with the following filters: Article Types (Clinical Trial), Species (Humans), and Languages (English). Structured abstract sections from PubMed have labels such as introduction, goals, study design, findings, or discussion; however, the majority of these labels are not useful for P, I, and O extraction since most are general (e.g. methods) and do not isolate a specific P, I, O sequence. Therefore, in order to narrow down abstract sections that correspond to the P label, for example, we needed to find a subset of labels such as, but not limited to population, patients, and subjects. We performed a lemmatization of the abstract section labels in order to cluster similar categories such as subject and subjects. Using this approach, we carefully chose candidate labels for each P, I, and O, and manually looked at a small number of samples for each label to determine if text was representative.
> 
> Since our goal was to collect sequences that are uniquely representative of a description of Population, Intervention, and Outcome, we avoided a keyword-based approach such as in BIBREF12 . For example, using a keyword-based approach would yield a sequence labeled population and methods with the label P, but such abstract sections were not purely about the population and contained information about the interventions and study design making them poor candidates for a P label. Thus, we were able to extract portions of abstracts pertaining to P, I, and O categories while minimizing ambiguity and redundancy. Moreover, in the dataset from BIBREF12 , a section labeled as P that contained more than one sentence would be split into multiple P sentences to be included in the dataset. We avoided this approach and kept the full abstract sections.

### Relevance

Label: 

## Record 0075

Paper: Enhancing PIO Element Detection in Medical Text Using Contextualized Embedding

### Question

> what shortcomings of previous datasets are mentioned?

### Passage

> In order to quantify the performance of the classification model, we computed the precision and recall scores. On average, it was found that the model leads to better results when trained using the BioBERT embedding. In addition, the performance of the PIO classifier was measured by averaging the three Area Under Receiver Operating Characteristic Curve (ROC_AUC) scores for P, I, and O. The ROC_AUC score of 0.9951 was obtained by the model using the general BERT embedding. This score was improved to 0.9971 when using the BioBERT model pre-trained on medical context. The results are illustrated in Figure FIGREF9 .

### Relevance

Label: 

## Record 0076

Paper: A system for the 2019 Sentiment, Emotion and Cognitive State Task of DARPAs LORELEI project

### Question

> Did they pre-train on existing sentiment corpora?

### Passage

> Model performance during train is presented in Table 5 . While all the models outperformed the baselines, not all of them did so with a significant margin due to the robustness of the baselines selected. The ones found to be significantly better than the baselines were models IIb (Domain-specific) and IIc (Twitter-only) (permutation test, $n = 10^5$ both $p < 0.05$ ). The difference in precision between model IIb and IIc points out to the former making the wrong predictions for news articles. These errors are most likely in selecting the wrong supporting segment. Moreover, even though models IIa-c only produce negative labels, they still achieve improved performance over the state-of-the-art systems, highlighting the highly skewed nature of the training dataset.
> 
> Table 6 present the official evaluation results for English and Spanish. Some information is missing since at the time of submission only partial score had been made public. As previously mentioned, the pre-trained state-of-the-art models (model I) were directly applied to the evaluation data without any adaptation. These performed reasonably well for the English data. Among the submissions of the SEC Task pilot, our systems outperformed the other competitors for both languages.

### Relevance

Label: 

## Record 0077

Paper: A system for the 2019 Sentiment, Emotion and Cognitive State Task of DARPAs LORELEI project

### Question

> Did they pre-train on existing sentiment corpora?

### Passage

> We now describe the models used for this work. Our models can be broken down into two groups: our first approach explores state-of-the-art models in targeted and untargeted sentiment analysis to evaluate their performance in the context of the SEC task. These models were pre-trained on larger corpora and evaluated directly on the task without any further adaptation. In a second approach we explore a data augmentation technique based on a proposed simplification of the task. In this approach, traditional machine learning classifiers were trained to identify which segments contain sentiment towards a SF regardless of sentiment polarity. For the classifiers, we explored the use of Support Vector Machines and Random Forests. Model performance was estimated through 10-fold cross validation on the train set. Hyper-parameters, such as of regularization, were selected based on the performance on grid-search using an 10-fold inner-cross validation loop. After choosing the parameters, models were re-trained on all the available data.
> 
> We consider some of the most popular baseline models in the literature: (i) minority class baseline (due to the heavily imbalanced dataset), (ii) Support Vector Machines trained on TF-IDF bi-gram language model, (iii) and Support Vector Machines trained on word2vec representations. These models were trained using English documents only.
> 
> Two types of targeted sentiment are evaluated for the task: those expressed towards either a situation frame or those towards an entity. To identify sentiment expressed towards an SF, we use the pretrained model described in BIBREF44 , in which a multiplicative LSTM cell is trained at the character level on a corpus of 82 million Amazon reviews. The model representation is then fed to a logistic regression classifier to predict sentiment. This model (which we will refer to as OpenAI) was chosen since at the time of our system submission it was one of the top three performers on the binary sentiment classification task on the Stanford Sentiment Treebank. In our approach, we first map the text associated with the SF annotation with a segment from the document and pass the full segment to the pretrained OpenAI model identify the sentiment polarity for that segment.
> 
> To identify sentiment targeted towards an entity, we use the recently released Target-Based Sentiment Analysis

### Relevance

Label: 

## Record 0078

Paper: A system for the 2019 Sentiment, Emotion and Cognitive State Task of DARPAs LORELEI project

### Question

> Did they pre-train on existing sentiment corpora?

### Passage

> We extract word unigrams and bigrams. These features were then transformed using term frequencies (TF) and Inverse document-frequency (IDF).
> 
> Word embeddings pretrained on large corpora allow models to efficiently leverage word semantics as well as similarities between words. This can help with vocabulary generalization as models can adapt to words not previously seen in training data. In our feature set we include a 300-dimensional word2vec word representation trained on a large news corpus BIBREF36 . We obtain a representation for each segment by averaging the embedding of each word in the segment. We also experimented with the use of GloVe BIBREF37 , and Sent2Vec BIBREF38 , an extension of word2vec for sentences.
> 
> We use two sources of sentiment features: manually constructed lexica, and pre-trained sentiment embeddings. When available, manually constructed lexica are a useful resource for identifying expressions of sentiment BIBREF21 . We obtained word percentages across 192 lexical categories using Empath BIBREF39 , which extends popular tools such as the Linguistic Inquiry and Word Count (LIWC) BIBREF22 and General Inquirer (GI) BIBREF40 by adding a wider range of lexical categories. These categories include emotion classes such as surprise or disgust.
> 
> Neural networks have been shown to capture specific task related subtleties which can complement the manually constructed sentiment lexica described in the previous subsection. For this work, we learn sentiment representations using a bilateral Long Short-Term Memory model BIBREF41 trained on the Stanford Sentiment Treebank BIBREF42 . This model was selected because it provided a good trade off between simplicity and performance on a fine-grained sentiment task, and has been shown to achieve competitive results to the state-of-the-art BIBREF43 .

### Relevance

Label: 

## Record 0079

Paper: A system for the 2019 Sentiment, Emotion and Cognitive State Task of DARPAs LORELEI project

### Question

> Did they pre-train on existing sentiment corpora?

### Passage

> Given a dataset of text documents and manually annotated situation frames, the task is to automatically detect sentiment polarity relevant to existing frames and identify the source and target for each sentiment instance. The source is defined as a person or a group of people expressing the sentiment, and can be either a PER/ORG/GPE (person, organization or geo political entity) construct in the frame, the author of the text document, or an entity not explicitly expressed in the document. The target toward which the sentiment is expressed, is either the frame or an entity in the document.
> 
> Situation awareness information is encoded into situation frames in the LORELEI program BIBREF35 . Situation Frames (SF) are similar in nature to those used in Natural Language Understanding (NLU) systems: in essence they are data structures that record information corresponding to a single incident at a single location BIBREF15 . A SF frame includes a situation Type taken from a fixed inventory of 11 categories (e.g., medical need, shelter, infrastructure), Location where the situation exists (if a location is mentioned) and additional variables highlighting the Status of the situation (e.g., entities involved in resolution, time and urgency). An example of a SF can be found in table 1 . A list of situation frames and documents serve as input for our sentiment analysis systems.

### Relevance

Label: 

## Record 0080

Paper: A system for the 2019 Sentiment, Emotion and Cognitive State Task of DARPAs LORELEI project

### Question

> Did they pre-train on existing sentiment corpora?

### Passage

> The growing adoption of online technologies has created new opportunities for emergency information propagation BIBREF0 . During crises, affected populations post information about what they are experiencing, what they are witnessing, and relate what they hear from other sources BIBREF1 . This information contributes to the creation and dissemination of situational awareness BIBREF2 , BIBREF3 , BIBREF4 , BIBREF0 , and crisis response agencies such as government departments or public health-care NGOs can make use of these channels to gain insight into the situation as it unfolds BIBREF2 , BIBREF5 . Additionally, these organizations might also post time-sensitive crisis management information to help with resource allocation and provide status reports BIBREF6 . While many of these organizations recognize the value of the information found online—specially during the on-set of a crisis—they are in need of automatic tools that locate actionable and tactical information BIBREF7 , BIBREF0 .
> 
> Opinion mining and sentiment analysis techniques offer a viable way of addressing these needs, with complementary insights to what keyword searches or topic and event extraction might offer BIBREF8 . Studies have shown that sentiment analysis of social media during crises can be useful to support response coordination BIBREF9 or provide information about which audiences might be affected by emerging risk events BIBREF10 . For example, identifying tweets labeled as “fear” might support responders on assessing mental health effects among the affected population BIBREF11 . Given the critical and global nature of the HADR events, tools must process information quickly, from a variety of sources and languages, making it easily accessible to first responders and decision makers for damage assessment and to launch relief efforts accordingly BIBREF12 , BIBREF13 . However, research efforts in these tasks are primarily focused on high resource languages such as English, even though such crises may happen anywhere in the world.
> 
> The LORELEI program provides a framework for developing and testing systems for real-time humanitarian crises response in the context of low-resource languages. The working scenario is as follows: a sudden state of danger requiring immediate action has been identified in a region which communicates in a low resource language. Under strict time constraints, participants are expected to build systems that can: translate

### Relevance

Label: 

## Record 0081

Paper: Elephant in the Room: An Evaluation Framework for Assessing Adversarial Examples in NLP

### Question

> What are the benchmark attacking methods?

### Passage

> We propose an evaluation framework for assessing the quality of adversarial examples in NLP, based on four criteria: (a) attacking performance, (b) textual similarity; (c) fluency; (d) label preservation. Our framework involves both automatic and human evaluation, and we test 5 benchmark methods and a novel auto-encoder approach. We found that the architecture of the target classifier is an important factor when it comes to attacking performance, e.g. CNNs are more vulnerable than LSTMs; dataset features such as length of text, training data size (for target classifiers) and input domains are also influencing factors that affect how difficulty it is to perform adversarial attack; and the predominant dataset (IMDB) used by most studies is comparatively easy for adversarial attack. Lastly, we also observe in our human evaluation that on shorter texts (Yelp) these methods produce adversarial examples that tend not to preserve their semantic content and have low readability. More importantly, these methods also “cheat” by simply flipping the sentiment in the adversarial examples, and this behaviour is evident on both datasets, suggesting they could be ineffective for adversarial training.

### Relevance

Label: 

## Record 0082

Paper: Elephant in the Room: An Evaluation Framework for Assessing Adversarial Examples in NLP

### Question

> What are the benchmark attacking methods?

### Passage

> We experiment with five benchmark attacking methods for texts: FGM, FGVM, DeepFool BIBREF5, HotFlip BIBREF3) and TYC BIBREF4.
> 
> To perturb the discrete inputs, both FGM and FGVM introduce noises in the word embedding space via the fast gradient method BIBREF1 and reconstruct the input by mapping perturbed word embeddings to valid words via nearest neighbour search. Between FGM and FGVM, the former introduce noises that is proportional to the sign of the gradients while the latter introduce perturbations proportional to the gradients directly. The proportion is known as the overshoot value and denoted by $\epsilon $. DeepFool uses the same trick to deal with discrete inputs except that, instead of using the fast gradient method, it uses the DeepFool method introduced in BIBREF8 for image to search for an optimal direction to perturb the word embeddings.
> 
> Unlike the previous methods, HotFlip and TYC rely on performing one or more atomic flip operations to replace words while monitoring the label change given by the target classifier. In HotFlip, the directional derivatives w.r.t. flip operations are calculated and the flip operation that results in the largest increase in loss is selected. TYC is similar to FGM, FGVM and DeepFool in that it also uses nearest neighbour search to map the perturbed embeddings to valid words, but instead of using the perturbed tokens directly, it uses greedy search or beam search to flip original tokens to perturbed ones one at a time in order of their vulnerability.

### Relevance

Label: 

## Record 0083

Paper: Elephant in the Room: An Evaluation Framework for Assessing Adversarial Examples in NLP

### Question

> What are the benchmark attacking methods?

### Passage

> Adversarial examples, a term introduced in BIBREF0, are inputs transformed by small perturbations that machine learning models consistently misclassify. The experiments are conducted in the context of computer vision (CV), and the core idea is encapsulated by an illustrative example: after imperceptible noises are added to a panda image, an image classifier predicts, with high confidence, that it is a gibbon. Interestingly, these adversarial examples can also be used to improve the classifier — either as additional training data BIBREF0 or as a regularisation objective BIBREF1 — thus providing motivation for generating effective adversarial examples.
> 
> The germ of this paper comes from our investigation of adversarial attack methods for natural language processing (NLP) tasks, e.g. sentiment classification, which drives us to quantify what is an “effective” or “good” adversarial example. In the context of images, a good adversarial example is typically defined according two criteria:
> 
> it has successfully fooled the classifier;
> 
> it is visually similar to the original example.
> 
> In NLP, defining a good adversarial example is a little more involving, because while criterion (b) can be measured with a comparable text similarity metric (e.g. BLEU or edit distance), an adversarial example should also:
> 
> be fluent or natural;
> 
> preserve its original label.
> 
> These two additional criteria are generally irrelevant for images, as adding minor perturbations to an image is unlikely to: (1) create an uninterpretable image (where else changing one word in a sentence can render a sentence incoherent), or (2) change how we perceive the image, say from seeing a panda to a gibbon (but a sentence's sentiment can be reversed by simply adding a negative adverb such as not). Without considering criterion (d), generating adversarial examples in NLP would be trivial, as the model can learn to simply replace a positive adjective (amazing) with a negative one (awful) to attack a sentiment classifier.
> 
> To the best of our knowledge, most studies on adversarial example generation in NLP have largely ignored these additional criteria BIBREF2, BIBREF3, BIBREF4, BIBREF5. We believe the lack of a rigorous evaluation framework partially explains why adversarial training for NLP models has not seen the same extent of improvement compared to CV models. As our experiments reveal, examples generated from

### Relevance

Label: 

## Record 0084

Paper: Elephant in the Room: An Evaluation Framework for Assessing Adversarial Examples in NLP

### Question

> What are the benchmark attacking methods?

### Passage

> Automatic metrics provide a proxy to quantify the quality of the adversarial examples. To validate that these metrics work, we conduct a crowdsourcing experiment on Figure-Eight. Recall that the automatic metrics do not assess sentiment preservation (criterion (d)); we evaluate that aspect here.
> 
> We experiment with the 3 best methods (TYC, AutoEncoder and HotFlip) on 2 accuracy thresholds (T0 and T2), using BiLSTM$+$A as the classifier. For each method and threshold, we randomly sample 25 positive-to-negative and 25 negative-to-positive examples. To control for quality, we reserve and annotate 10% of the samples ourselves as control questions. Workers are first presented with 10 control questions as a quiz, and only those who pass the quiz with at least 80% accuracy can continue to work on the task. We display 10 questions per page, where one control question is embedded to continue monitor worker performance. The task is designed such that each control question can only be seen once per worker. We restrict our jobs to workers in United States, United Kingdoms, Australia, and Canada.
> 
> To evaluate the criteria discussed in Section SECREF1: (b) textual similarity, (c) fluency, and (d) sentiment preservation, we ask the annotators three questions:
> 
> Is snippet B a good paraphrase of snippet A?
> 
> $\circledcirc $ Yes $\circledcirc $ Somewhat yes $\circledcirc $ No
> 
> How natural does the text read?
> 
> $\circledcirc $ Very unnatural $\circledcirc $ Somewhat natural $\circledcirc $ Natural
> 
> What is the sentiment of the text?
> 
> $\circledcirc $ Positive $\circledcirc $ Negative $\circledcirc $ Cannot tell
> 
> For question 1, we display both the adversarial input and the original input, while for question 2 and 3 we present only the adversarial example. As an upper-bound, we also run a survey on question 2 and 3 for 50 random original samples.

### Relevance

Label: 

## Record 0085

Paper: Elephant in the Room: An Evaluation Framework for Assessing Adversarial Examples in NLP

### Question

> What are the benchmark attacking methods?

### Passage

> Most existing adversarial attack methods for text inputs are derived from those for image inputs. These methods can be categorised into three types including gradient-based attacks, optimisation-based attacks and model-based attacks.
> 
> Gradient-based attacks are mainly white-box attacks that rely on calculating the gradients of the target classifier with respect to the input representation. This class of attacking methods BIBREF6, BIBREF7, BIBREF6 are mainly derived from the fast gradient sign method (FGSM) BIBREF1, and it has been shown to be effective in attacking CV classifiers. However, these gradient-based methods could not be applied to text directly because perturbed word embeddings do not necessarily map to valid words. Other methods such as DeepFool BIBREF8 that rely on perturbing the word embedding space face similar roadblocks. BIBREF5 propose to use nearest neighbour search to find the closest word to the perturbed embedding.
> 
> Both optimisation-based and model-based attacks treat adversarial attack as an optimisation problem where the constraints are to maximise the loss of target classifiers and to minimise the difference between original and adversarial examples. Between these two, the former uses optimisation algorithms directly; while the latter trains a seperate model to generate adversarial examples and therefore involves a training process. Some of the most effective attacks for images are achieved by optimisation-based methods, such as the L-BFGS attack BIBREF1 and the C&W attack BIBREF9 in white-box attacks and the ZOO method BIBREF10 in black-box attacks. For texts, the white-box attack HotFlip BIBREF3 and black-box attack DeepWordBug BIBREF11 and TextBugger BIBREF12 are proposed in this category.
> 
> In a similar vein, a few model-based attacks have been proposed for images, e.g. BIBREF13 design a generative adversarial network (GAN) to generate the image perturbation from a noise map. The attacking method and target classifier typically form a single large network and the attacking method is trained using the loss from the target classifier. For this reason, it is not very straightforward to use these model-based techniques for text because there is a discontinuity in the network (since words in the adversarial examples are discrete) and so it is not fully differentiable.

### Relevance

Label: 

## Record 0086

Paper: A Joint Model for Multimodal Document Quality Assessment

### Question

> Which languages do they use?

### Passage

> We compare our models against the following five baselines:
> 
> Majority: the model labels all test samples with the majority class of the training data.
> 
> Benchmark: a benchmark method from the literature. In the case of Wikipedia, this is BIBREF5 , who use structural features and readability scores as features to build a random forest classifier; for arXiv, this is BIBREF2 , who use hand-crafted features, such as the number of references and TF-IDF weighted bag-of-words in abstract, to build a classifier based on the best of logistic regression, multi-layer perception, and AdaBoost.
> 
> Doc2Vec: doc2vec BIBREF11 to learn document embeddings with a dimension of 500, and a 4-layer feed-forward classification model on top of this, with 2000, 1000, 500, and 200 dimensions, respectively.
> 
> biLSTM: first derive a sentence representation by averaging across words in a sentence, then feed the sentence representation into a biLSTM and a maxpooling layer over output sequence to learn a document level representation with a dimension of 512, which is used to predict document quality.
> 
> Inception $_{\text{fixed}}$ : the frozen Inception model, where only parameters in the last layer are fine-tuned during training.
> 
> The hyper-parameters of Benchmark, Doc2Vec, and biLSTM are based on the corresponding papers except that: (1) we fine-tune the feed forward layer of Doc2Vec on the development set and train the model 300 epochs on Wikipedia and 50 epochs on arXiv; (2) we do not use hand-crafted features for biLSTM as we want the baselines to be comparable to our models, and the main focus of this paper is not to explore the effects of hand-crafted features (e.g., see BIBREF12 ).

### Relevance

Label: 

## Record 0087

Paper: A Joint Model for Multimodal Document Quality Assessment

### Question

> Which languages do they use?

### Passage

> Table 3 shows the performance of the different models over our two datasets, in the form of the average accuracy on the test set (along with the standard deviation) over 10 runs, with different random initializations.
> 
> On Wikipedia, we observe that the performance of biLSTM, Inception, and Joint is much better than that of all four baselines. Inception achieves 2.9% higher accuracy than biLSTM. The performance of Joint achieves an accuracy of 59.4%, which is 5.3% higher than using textual features alone (biLSTM) and 2.4% higher than using visual features alone (Inception). Based on a one-tailed Wilcoxon signed-rank test, the performance of Joint is statistically significant ( $p<0.05$ ). This shows that the textual and visual features complement each other, achieving state-of-the-art results in combination.
> 
> For arXiv, baseline methods Majority, Benchmark, and Inception $_{\text{fixed}}$ outperform biLSTM over cs.ai, in large part because of the class imbalance in this dataset (90% of papers are rejected). Surprisingly, Inception $_{\text{fixed}}$ is better than Majority and Benchmark over the arXiv cs.lg subset, which verifies the usefulness of visual features, even when only the last layer is fine-tuned. Table 3 also shows that Inception and biLSTM achieve similar performance on arXiv, showing that textual and visual representations are equally discriminative: Inception and biLSTM are indistinguishable over cs.cl; biLSTM achieves 1.8% higher accuracy over cs.lg, while Inception achieves 1.3% higher accuracy over cs.ai. Once again, the Joint model achieves the highest accuracy on cs.ai and cs.cl by combining textual and visual representations (at a level of statistical significance for cs.ai). This, again, confirms that textual and visual features complement each other, and together they achieve state-of-the-art results. On arXiv cs.lg, Joint achieves a 0.6% higher accuracy than Inception by combining visual features and textual features, but biLSTM achieves the highest accuracy. One characteristic of cs.lg documents is that they tend to contain more equations than the other two arXiv datasets, and preliminary analysis suggests that the biLSTM is picking up on a correlation between the volume/style of mathematical presentation and the quality of the document.

### Relevance

Label: 

## Record 0088

Paper: A Joint Model for Multimodal Document Quality Assessment

### Question

> Which languages do they use?

### Passage

> A variety of approaches have been proposed for document quality assessment across different domains: Wikipedia article quality assessment, academic paper rating, content quality assessment in community question answering (cQA), and essay scoring. Among these approaches, some use hand-crafted features while others use neural networks to learn features from documents. For each domain, we first briefly describe feature-based approaches and then review neural network-based approaches. Wikipedia article quality assessment: Quality assessment of Wikipedia articles is a task that assigns a quality class label to a given Wikipedia article, mirroring the quality assessment process that the Wikipedia community carries out manually. Many approaches have been proposed that use features from the article itself, meta-data features (e.g., the editors, and Wikipedia article revision history), or a combination of the two. Article-internal features capture information such as whether an article is properly organized, with supporting evidence, and with appropriate terminology. For example, BIBREF3 use writing styles represented by binarized character trigram features to identify featured articles. BIBREF4 and BIBREF0 explore the number of headings, images, and references in the article. BIBREF5 use nine readability scores, such as the percentage of difficult words in the document, to measure the quality of the article. Meta-data features, which are indirect indicators of article quality, are usually extracted from revision history, and the interaction between editors and articles. For example, one heuristic that has been proposed is that higher-quality articles have more edits BIBREF6 , BIBREF7 . BIBREF8 use the percentage of registered editors and the total number of editors of an article. Article–editor dependencies have also been explored. For example, BIBREF9 use the authority of editors to measure the quality of Wikipedia articles, where the authority of editors is determined by the articles they edit. Deep learning approaches to predicting Wikipedia article quality have also been proposed. For example, BIBREF10 use a version of doc2vec BIBREF11 to represent articles, and feed the document embeddings into a four hidden layer neural network. BIBREF12 first obtain sentence representations by averaging words within a sentence, and then apply a biLSTM BIBREF13 to learn a document-level representation, which is combined with hand-crafted features as side information. BIBREF14 exploit two stacked biLSTMs to learn document representations.
> 
> Academic

### Relevance

Label: 

## Record 0089

Paper: A Joint Model for Multimodal Document Quality Assessment

### Question

> Which languages do they use?

### Passage

> As discussed above, our model has two main components — biLSTM and Inception— which generate textual and visual representations, respectively. For the biLSTM component, the documents are preprocessed as described in BIBREF12 , where an article is divided into sentences and tokenized using NLTK BIBREF38 . Words appearing more than 20 times are retained when building the vocabulary. All other words are replaced by the special UNK token. We use the pre-trained GloVe BIBREF39 50-dimensional word embeddings to represent words. For words not in GloVe, word embeddings are randomly initialized based on sampling from a uniform distribution $U(-1, 1)$ . All word embeddings are updated in the training process. We set the LSTM hidden layer size to 256. The concatenation of the forward and backward LSTMs thus gives us 512 dimensions for the document embedding. A dropout layer is applied at the sentence and document level, respectively, with a probability of 0.5.
> 
> For Inception, we adopt data augmentation techniques in the training with a “nearest” filling mode, a zoom range of 0.1, a width shift range of 0.1, and a height shift range of 0.1. As the original screenshots have the size of 1,000 $\times 2$ ,000 pixels, they are resized to 500 $\times $ 500 to feed into Inception, where the input shape is (500, 500, 3). A dropout layer is applied with a probability of 0.5. Then, a GlobalAveragePooling2D layer is applied, which produces a 2,048 dimensional representation.
> 
> For the Joint model, we get a representation of 2,560 dimensions by concatenating the 512 dimensional representation from the biLSTM with the 2,048 dimensional representation from Inception. The dropout layer is applied to the two components with a probability of 0.5. For biLSTM, we use a mini-batch size of 128 and a learning rate of 0.001. For both Inception and joint model, we use a mini-batch size of 16 and a learning rate of 0.0001. All hyper-parameters were set empirically over the development data, and the models were optimized using the Adam optimizer BIBREF40 .
> 
> In the training phase, the weights in Inception are initialized by parameters pretrained on ImageNet, and the weights in biLSTM are randomly initialized (except for the word embeddings). We train

### Relevance

Label: 

## Record 0090

Paper: A Joint Model for Multimodal Document Quality Assessment

### Question

> Which languages do they use?

### Passage

> first obtain sentence representations by averaging words within a sentence, and then apply a biLSTM BIBREF13 to learn a document-level representation, which is combined with hand-crafted features as side information. BIBREF14 exploit two stacked biLSTMs to learn document representations.
> 
> Academic paper rating: Academic paper rating is a relatively new task in NLP/AI, with the basic formulation being to automatically predict whether to accept or reject a paper. BIBREF2 explore hand-crafted features, such as the length of the title, whether specific words (such as outperform, state-of-the-art, and novel) appear in the abstract, and an embedded representation of the abstract as input to different downstream learners, such as logistic regression, decision tree, and random forest. BIBREF15 exploit a modularized hierarchical convolutional neural network (CNN), where each paper section is treated as a module. For each paper section, they train an attention-based CNN, and an attentive pooling layer is applied to the concatenated representation of each section, which is then fed into a softmax layer.
> 
> Content quality assessment in cQA: Automatic quality assessment in cQA is the task of determining whether an answer is of high quality, selected as the best answer, or ranked higher than other answers. To measure answer content quality in cQA, researchers have exploited various features from different sources, such as the answer content itself, the answerer's profile, interactions among users, and usage of the content. The most common feature used is the answer length BIBREF16 , BIBREF17 , with other features including: syntactic and semantic features, such as readability scores. BIBREF18 ; similarity between the question and the answer at lexical, syntactic, and semantic levels BIBREF18 , BIBREF19 , BIBREF20 ; or user data (e.g., a user's status points or the number of answers written by the user). There have also been approaches using neural networks. For example, BIBREF21 combine CNN-learned representations with hand-crafted features to predict answer quality. BIBREF22 use a 2-dimensional CNN to learn the semantic relevance of an answer to the question, and apply an LSTM to the answer sequence to model thread context. BIBREF23 and BIBREF24 model the problem similarly to machine translation quality estimation, treating answers as competing translation hypotheses and the question as the reference translation, and

### Relevance

Label: 

## Record 0091

Paper: Finding Dominant User Utterances And System Responses in Conversations

### Question

> Do they use the same distance metric for both the SimCluster and K-means algorithm?

### Passage

> To evaluate the clusters we computed the following metrics
> 
> ARI (Adjusted Rand Index): Standard Rand Index is a metric used to check the clustering quality against a given standard set of clusters by comparing the pairwise clustering decisions. It is defined as INLINEFORM0 , where a is the number of true positive pairs, b is the number of true negative pairs, c is the number of false positive pairs and d is the number of false negative pairs. Adjusted rand index corrects the standard rand index for chance and is defined as INLINEFORM1 BIBREF15 .
> 
> We compute ARI score for both the source clusters as well as the target clusters.
> 
> F1 scores: We also report F1 scores for the pairwise clustering decisions. In the above notation we considered the pair-precision as INLINEFORM0 and recall as INLINEFORM1 . The F1 measure is the Harmonic mean given as INLINEFORM2 .
> 
> We used the gaussian index from which an utterance pair was generated as the ground truth label, which served to provide ground truth clusters for computation of the above evaluation metrics. Table TABREF15 shows a comparison of the results on SimCluster versus K-means algorithm. Here our SimCluster algorithm improves the F1-scores from 0.412 and 0.417 in the two domains to 0.442 and 0.441. The ARI scores also improve from 0.176 and 0.180 to 0.203 and 0.204.
> 
> We also performed experiments to see how the performance of SimCluster is affected by the variance in the cluster (controlled by the generative process in Algorithm SECREF11 ). Intuitively we expect SimCluster to obtain an advantage over simple K-means when variance is larger. This is because at larger variance, the data points are more likely to be generated away from the centroid due to which they might be clustered incorrectly with the points from neighbouring cluster. However if the corresponding point from the other domain is generated closer to the centroid, it might help in clustering the given data point correctly. We performed these experiments with points generated from Algorithm SECREF11 at differet values of variance. We generated the points with centroids located on a grid of size INLINEFORM0 in each domain. The value of k was set to 9. The

### Relevance

Label: 

## Record 0092

Paper: Finding Dominant User Utterances And System Responses in Conversations

### Question

> Do they use the same distance metric for both the SimCluster and K-means algorithm?

### Passage

> [] SimCluster [1] SimClusterInput: INLINEFORM0 ,k (No. of cluster) Output: A cluster assignment INLINEFORM1 for INLINEFORM2 s and a cluster assignment INLINEFORM3 for INLINEFORM4 s Initialize a set of centroids INLINEFORM5 , and INLINEFORM6 Perform simple clustering for a few iterations For each i, compute INLINEFORM7 as the index j among 1 to k which minimizes INLINEFORM8 . Similarly , compute INLINEFORM9 as the index j' among 1 to k which minimizes INLINEFORM10 . Update the centroids, INLINEFORM11 and INLINEFORM12 as:- INLINEFORM13
> 
> and INLINEFORM0
> 
> Perform a Hungarian matching between the cluster indices in the two domains with weights
> 
> N(j,j') on edges from index j to index j'. convergence To minimize the above energy term we adopt an approach similar to Lloyd's clustering algorithm Llo82 . We assume that we are given a set of initial seeds for the cluster centroids INLINEFORM0 and INLINEFORM1 . We repeat the following steps iteratively:-
> 
> Minimize the energy with respect to cluster assignment keeping centroids unchanged. As in standard K-means algorithm, this is achieved by updating the cluster assignment, INLINEFORM0 for each index i to be the cluster index j which minimizes INLINEFORM1 . Correspondingly for INLINEFORM2 , we pick the cluster index j' which minimizes INLINEFORM3 .
> 
> Minimize the energy with respect to the centroids keeping cluster assignment unchanged. To achieve this step we need to minimize the energy function with respect to the centroids INLINEFORM0 and INLINEFORM1 . This is achieved by setting INLINEFORM2 for each j and INLINEFORM3 for each j.
> 
> Setting INLINEFORM0 , we obtain INLINEFORM1
> 
> or equivalently INLINEFORM0
> 
> Similarly, setting INLINEFORM0 , we obtain INLINEFORM1
> 
> Finally we update the matching between the clusters. To do so, we need to find a bipartite matching match on the cluster indices so as to maximize INLINEFORM0 . We use Hungarian algorithm BIBREF13 to perform the same i.e. we define a bipartite graph with vertices consisting of cluster indices in the two domains. There is an edge from vertex representing cluster indices j (in domain 1) and j' in domain 2, with weight N(j,j'). We find a maximum weight bipartite matching in this graph.
> 
> Similar to Lloyd's algorithm, each step of the above algorithm decreases the cost function. This

### Relevance

Label: 

## Record 0093

Paper: Finding Dominant User Utterances And System Responses in Conversations

### Question

> Do they use the same distance metric for both the SimCluster and K-means algorithm?

### Passage

> For the clusters so obtained we have computed F1 and ARI measures as before and compared with the K-means approach. We used the partitioning formed by the 8 categories (from which the utterance pairs were selected) as the ground truth clustering.
> 
> Table TABREF20 summarizes the results. We observe that for K-means algorithm, the vectors generated from sequence to sequence model perform better than the vectors generated using paragraph to vector for both the domains. This is expected as the vectors generated from sequence to sequence model encode some adjacency information as well. We further observe that the SimCluster approach performs better than the K-means approach for both the vector representations. It improves the F1-scores for Doc2Vec representation from 0.787 and 0.783 to 0.88 and 0.887 in the two domains. Also the F1-scores on Seq2Seq based representation improve from 0.83 and 0.9 to 0.86 and 0.916 using SimCluster. However the gains are much more in case of Doc2Vec representations than Seq2Seq representations since Doc2Vec did not have any information from the other domain where as some amount of this information is already captured by Seq2Seq representation. Moreover it is the clustering of customer utterances which is likely to see an improvement. This is because agent utterances tends to follow a generic pattern while customer utterances tend to be more varied. Considering agent utterances while generating clusters in the user domain thus tends to be more helpful than the other way round.
> 
> Table TABREF25 shows qualitative results on the same dataset. Column 1 and 2 consists of clusters of utterances in customer domain and agent domain respectively. The utterances with usual font are representative utterances from clusters obtained through K-means clustering. The utterances in bold face indicate the similar utterances which were incorrectly classified in different clusters using K-means but were correctly classified together with the utterances by SimCluster algorithm.

### Relevance

Label: 

## Record 0094

Paper: Finding Dominant User Utterances And System Responses in Conversations

### Question

> Do they use the same distance metric for both the SimCluster and K-means algorithm?

### Passage

> We consider a problem setting where we are given a collection of pairs of consecutive utterances, with vector representations INLINEFORM0 where INLINEFORM1 s are in speaker 1's domain and INLINEFORM2 s are in speaker 2's domain. We need to simultaneously cluster the utterances in their respective domains to minimize the variations within each domain and also ensure that the clusters for both domains are close together.
> 
> We denote the clusters for speaker 1's domain by INLINEFORM0 with their respective means INLINEFORM1 . We denote the clusters assignments for INLINEFORM2 by INLINEFORM3 .
> 
> We denote the clusters for second speaker by INLINEFORM0 with their respective means INLINEFORM1 . We denote the clusters assignments for INLINEFORM2 by INLINEFORM3 . The usual energy function has the terms for distance of points from their corresponding cluster centroids. To be able to ensure that the clusters in each domain are similar, we also consider an alignment between the centroids of the two domains. Since the semantic representations in the two domains are not comparable we consider a notion of induced centroids.
> 
> We define the induced centroids INLINEFORM0 as the arithmetic means of the points INLINEFORM1 s such that INLINEFORM2 's have the same cluster assigned to them. Similarly, we define INLINEFORM3 as the arithmetic means of INLINEFORM4 s such that INLINEFORM5 s have the same cluster assigned to them. More formally, we define these induced centroids as:- INLINEFORM6
> 
> and INLINEFORM0
> 
> The alignment between these clusters given by the function INLINEFORM0 , which is a bijective mapping from the cluster indices in speaker 1's domain to those in speaker 2's domain. Though there can be several choices for this alignment function, we consider this alignment to be a matching which maximizes the sum of number of common indices in the aligned clusters. More formally we define INLINEFORM1
> 
> Then the matching INLINEFORM0 is defined to be the bijective function which maximizes INLINEFORM1 . We consider a term in the cost function corresponding to the sum of distances between the original centroids and the matched induced centroids. Our overall cost function is now given by:- INLINEFORM2
> 
> We explain the above definition via an example. Consider the clusters shown in Figure FIGREF10 . Here

### Relevance

Label: 

## Record 0095

Paper: Finding Dominant User Utterances And System Responses in Conversations

### Question

> Do they use the same distance metric for both the SimCluster and K-means algorithm?

### Passage

> create part of the dialog flow.
> 
> We propose two ways to take adjacency information into account. Firstly we propose a method called SimCluster for jointly or simultaneously clustering user utterances and agent utterances. SimCluster extends the K-means clustering method by incorporating additional penalty terms in the objective function that try to align the clusters together (described in Section SECREF3 ). The algorithm creates initial user utterance clusters as well as agent utterance clusters and then use bi-partite matching to get the best alignment across these clusters. Minimizing the objective function pushes the cluster centroids to move towards the centroids of the aligned clusters. The process implicitly ensures that the similarity of adjacent agent utterances affect the grouping of user utterances and conversely similarity of adjacent user utterances affect the grouping of agent utterances. In our second approach we use the information about neighbouring utterances for creating the vector representation of an utterance. For this we train a sequence to sequence model BIBREF8 to create the vectors (described in Section SECREF5 ).
> 
> Our experiments described in section SECREF5 show that we achieve upto 10% absolute improvement in F1 scores over standard K-means using SimCluster. Also we observe that clustering of customer utterances gains significantly by using the adjacency information of agent utterances whereas the gain in clustering quality of agent utterances is moderate. This is because the agent utterances typically follow similar syntactic constructs whereas customer utterances are more varied. Considering the agent utterances into account while clustering users utterances is thus helpful. The organization of the rest of the paper is as follows. In Section SECREF2 we describe the related work. In Section SECREF3 we describe our problem formulation for clustering and the associated algorithm. Finally in sections SECREF4 and SECREF5 we discuss our experiments on synthetic and real datasets respectively.

### Relevance

Label: 

## Record 0096

Paper: What do character-level models learn about morphology? The case of dependency parsing

### Question

> Do the character-level models perform better than models with access to morphological analyses only?

### Passage

> the 20K most frequent words, replacing less frequent words with an unknown word token. The char-lstm, trigram-lstm, and oracle models use a one-layer bi-LSTM with 200 hidden units to compose subwords. For char-cnn, we use the small model setup of kim2015.
> 
> Table 2 presents test results for every model on every language, establishing three results. First, they support previous findings that character-level models outperform word-based models—indeed, the char-lstm model outperforms the word model on LAS for all languages except Hindi and Urdu for which the results are identical. Second, they establish strong baselines for the character-level models: the char-lstm generally obtains the best parsing accuracy, closely followed by char-cnn. Third, they demonstrate that character-level models rarely match the accuracy of an oracle model with access to explicit morphology. This reinforces a finding of BIBREF9 : character-level models are effective tools, but they do not learn everything about morphology, and they seem to be closer to oracle accuracy in agglutinative rather than in fusional languages.
> 
> In character-level models, orthographically similar words share many parameters, so we would expect these models to produce good representations of OOV words that are morphological variants of training words. Does this effect explain why they are better than word-level models?
> 
> Table 3 shows how the character model improves over the word model for both non-OOV and OOV words. On the agglutinative languages Finnish and Turkish, where the OOV rates are 23% and 24% respectively, we see the highest LAS improvements, and we see especially large improvements in accuracy of OOV words. However, the effects are more mixed in other languages, even with relatively high OOV rates. In particular, languages with rich morphology like Czech, Russian, and (unvocalised) Arabic see more improvement than languages with moderately rich morphology and high OOV rates like Portuguese or Spanish. This pattern suggests that parameter sharing between pairs of observed training words can also improve parsing performance. For example, if “dog” and “dogs” are observed in the training data, they will share activations in their context and on their common prefix.
> 
> Let's turn to our main question: what do character-level models learn about morphology? To answer it, we compare the oracle model to char-lstm, our best

### Relevance

Label: 

## Record 0097

Paper: What do character-level models learn about morphology? The case of dependency parsing

### Question

> Do the character-level models perform better than models with access to morphological analyses only?

### Passage

> results are interesting, since in non-neural parsers, predicted case usually harms accuracy BIBREF19 . However, we note that our taggers use gold POS, which might help. The MTL models achieve similar or slightly better performance than the character-only models, suggesting that supplying case in this way is beneficial. Curiously, the MTL parser is worse than the the pipeline parser, but the MTL case tagger is better than the pipeline case tagger (Table 7 ). This indicates that the MTL model must learn to encode case in the model's representation, but must not learn to effectively use it for parsing. Finally, we observe that augmenting the char-lstm with either gold or predicted case improves the parsing performance for all languages, and indeed closes the performance gap with the full oracle, which has access to all morphological features. This is especially interesting, because it shows using carefully targeted linguistic analyses can improve accuracy as much as wholesale linguistic analysis.
> 
> The previous experiments condition their analysis on the dependent, but dependency is a relationship between dependents and heads. We also want to understand the importance of morphological features to the head. Which morphological features of the head are important to the oracle?
> 
> To see which morphological features the oracle depends on when making predictions, we augmented our model with a gated attention mechanism following kuncoro-EtAl:2017:EACLlong. Our new model attends to the morphological features of candidate head $w_j$ when computing its association with dependent $w_i$ (Eq. 5 ), and morpheme representations are then scaled by their attention weights to produce a final representation.
> 
> Let $f_{i1}, \cdots , f_{ik}$ be the $k$ morphological features of $w_i$ , and denote by $\textbf {f}_{i1}, \cdots , \textbf {f}_{ik}$ their corresponding feature embeddings. As in § "Dependency parsing model" , $\textbf {h}_i$ and $\textbf {h}_j$ are the encodings of $w_i$ and $w_j$ , respectively. The morphological representation $\textbf {m}_j$ of $w_j$ is:
> 
> $$\textbf {m}_j = [\textbf {f}_{j1}, \cdots , \textbf {f}_{jk}]^\top \textbf {k}$$   (Eq. 43)
> 
> where $\textbf {k}$ is a vector of attention weights:
> 
> $$\textbf {k} = \textrm {softmax}([\textbf {f}_{j1}, \cdots , \textbf {f}_{jk}]^\top \textbf {V} \textbf {h}_i )$$   (Eq. 44)
> 
> The intuition is that dependent $w_i$ can choose which morphological features of

### Relevance

Label: 

## Record 0098

Paper: What do character-level models learn about morphology? The case of dependency parsing

### Question

> Do the character-level models perform better than models with access to morphological analyses only?

### Passage

> Modeling language input at the character level BIBREF0 , BIBREF1 is effective for many NLP tasks, and often produces better results than modeling at the word level. For parsing, ballesteros-dyer-smith:2015:EMNLP have shown that character-level input modeling is highly effective on morphologically-rich languages, and the three best systems on the 45 languages of the CoNLL 2017 shared task on universal dependency parsing all use character-level models BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 , showing that they are effective across many typologies.
> 
> The effectiveness of character-level models in morphologically-rich languages has raised a question and indeed debate about explicit modeling of morphology in NLP. BIBREF0 propose that “prior information regarding morphology ... among others, should be incorporated” into character-level models, while BIBREF6 counter that it is “unnecessary to consider these prior information” when modeling characters. Whether we need to explicitly model morphology is a question whose answer has a real cost: as ballesteros-dyer-smith:2015:EMNLP note, morphological annotation is expensive, and this expense could be reinvested elsewhere if the predictive aspects of morphology are learnable from strings.
> 
> Do character-level models learn morphology? We view this as an empirical claim requiring empirical evidence. The claim has been tested implicitly by comparing character-level models to word lookup models BIBREF7 , BIBREF8 . In this paper, we test it explicitly, asking how character-level models compare with an oracle model with access to morphological annotations. This extends experiments showing that character-aware language models in Czech and Russian benefit substantially from oracle morphology BIBREF9 , but here we focus on dependency parsing (§ "Dependency parsing model" )—a task that benefits substantially from morphological knowledge—and we experiment with twelve languages using a variety of techniques to probe our models.
> 
> Our summary finding is that character-level models lag the oracle in nearly all languages (§ "Experiments" ). The difference is small, but suggests that there is value in modeling morphology. When we tease apart the results by part of speech and dependency type, we trace the difference back to the character-level model's inability to disambiguate words even when encoded with arbitrary context (§ "Analysis" ). Specifically, it struggles with case syncretism, in which noun case—and thus syntactic function—is ambiguous. We show that the oracle relies

### Relevance

Label: 

## Record 0099

Paper: What do character-level models learn about morphology? The case of dependency parsing

### Question

> Do the character-level models perform better than models with access to morphological analyses only?

### Passage

> predict them so well. We hypothesized that these cases are more challenging for the character model because these languages feature a high degree of syncretism—functionally distinct words that have the same form—and in particular case syncretism. For example, referring back to examples ( UID28 ) and ( UID28 ), the character model must disambiguate pisˊmo from its context, whereas the oracle can directly disambiguate it from a feature of the word itself.
> 
> To understand this, we first designed an experiment to see whether the char-lstm could successfully disambiguate noun case, using a method similar to BIBREF8 . We train a neural classifier that takes as input a word representation from the trained parser and predicts a morphological feature of that word—for example that its case is nominative (Case=Nom). The classifier is a feedforward neural network with one hidden layer, followed by a ReLU non-linearity. We consider two representations of each word: its embedding ( $\textbf {x}_i$ ; Eq. 2 ) and its encoding ( $\textbf {h}_i$ ; Eq. 3 ). To understand the importance of case, we consider it alongside number and gender features as well as whole feature bundles.
> 
> Table 5 shows the results of morphological feature classification on Czech; we found very similar results in German and Russian (Appendix "Results on morphological tagging" ). The oracle embeddings have almost perfect accuracy—and this is just what we expect, since the representation only needs to preserve information from its input. The char-lstm embeddings perform well on number and gender, but less well on case. This results suggest that the character-level models still struggle to learn case when given only the input text. Comparing the char-lstm with a baseline model which predicts the most frequent feature for each type in the training data, we observe that both of them show similar trends even though character models slightly outperforms the baseline model.
> 
> The classification results from the encoding are particularly interesting: the oracle still performs very well on morphological case, but less well on other features, even though they appear in the input. In the character model, the accuracy in morphological prediction also degrades in the encoding—except for case, where accuracy on case improves by 12%.
> 
> These

### Relevance

Label: 

## Record 0100

Paper: What do character-level models learn about morphology? The case of dependency parsing

### Question

> Do the character-level models perform better than models with access to morphological analyses only?

### Passage

> on morphological case, but less well on other features, even though they appear in the input. In the character model, the accuracy in morphological prediction also degrades in the encoding—except for case, where accuracy on case improves by 12%.
> 
> These results make intuitive sense: representations learn to preserve information from their input that is useful for subsequent predictions. In our parsing model, morphological case is very useful for predicting dependency labels, and since it is present in the oracle's input, it is passed almost completely intact through each representation layer. The character model, which must disambiguate case from context, draws as much additional information as it can from surrounding words through the LSTM encoder. But other features, and particularly whole feature bundles, are presumably less useful for parsing, so neither model preserves them with the same fidelity.
> 
> Our analysis indicates that case is important for parsing, so it is natural to ask: Can we improve the neural model by explicitly modeling case? To answer this question, we ran a set of experiments, considering two ways to augment the char-lstm with case information: multitask learning BIBREF16 and a pipeline model in which we augment the char-lstm model with either predicted or gold case. For example, we use $\langle $ p, i, z, z, a, Nom $\rangle $ to represent pizza with nominative case. For MTL, we follow the setup of BIBREF17 and BIBREF18 . We increase the biLSTMs layers from two to four and use the first two layers to predict morphological case, leaving out the other two layers specific only for parser. For the pipeline model, we train a morphological tagger to predict morphological case (Appendix "Morphological tagger" ). This tagger does not share parameters with the parser.
> 
> Table 6 summarizes the results on Czech, German, and Russian. We find augmenting the char-lstm model with either oracle or predicted case improve its accuracy, although the effect is different across languages. The improvements from predicted case results are interesting, since in non-neural parsers, predicted case usually harms accuracy BIBREF19 . However, we note that our taggers use gold POS, which might help. The MTL models achieve similar or slightly better performance than the character-only models, suggesting

### Relevance

Label: 
