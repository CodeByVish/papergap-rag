# Passage relevance annotation

Annotator: 

Judge whether the passage provides information that helps answer the question, including useful partial evidence. Topic overlap alone is not sufficient. Judge only the supplied question and passage.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Do not change record numbers, questions or passages. Work independently without consulting another annotator or reference answers.

## Record 0701

Paper: Conversational Intent Understanding for Passengers in Autonomous Vehicles

### Question

> What intents does the paper explore?

### Passage

> Understanding passenger intents and extracting relevant slots are important building blocks towards developing a contextual dialogue system responsible for handling certain vehicle-passenger interactions in autonomous vehicles (AV). When the passengers give instructions to AMIE (Automated-vehicle Multimodal In-cabin Experience), the agent should parse such commands properly and trigger the appropriate functionality of the AV system. In our AMIE scenarios, we describe usages and support various natural commands for interacting with the vehicle. We collected a multimodal in-cabin data-set with multi-turn dialogues between the passengers and AMIE using a Wizard-of-Oz scheme. We explored various recent Recurrent Neural Networks (RNN) based techniques and built our own hierarchical models to recognize passenger intents along with relevant slots associated with the action to be performed in AV scenarios. Our experimental results achieved F1-score of 0.91 on utterance-level intent recognition and 0.96 on slot extraction models.

### Relevance

Label: 

## Record 0702

Paper: Conversational Intent Understanding for Passengers in Autonomous Vehicles

### Question

> What intents does the paper explore?

### Passage

> and utterance-level intents (adding <BOU>/<EOU> terms to the start/end of utterances with intent types). For (4) and (5), we experiment with the hierarchical models BIBREF3 , BIBREF4 , BIBREF5 where we extract intent keywords/slots first, and then only feed the predicted keywords/slots as a sequence into (2) and (3), respectively.

### Relevance

Label: 

## Record 0703

Paper: Conversational Intent Understanding for Passengers in Autonomous Vehicles

### Question

> What intents does the paper explore?

### Passage

> Our AV in-cabin data-set includes 30 hours of multimodal data collected from 30 passengers (15 female, 15 male) in 20 rides/sessions. 10 types of passenger intents are identified and annotated as: Set/Change Destination, Set/Change Route (including turn-by-turn instructions), Go Faster, Go Slower, Stop, Park, Pull Over, Drop Off, Open Door, and Other (turn music/radio on/off, open/close window/trunk, change AC/temp, show map, etc.). Relevant slots are identified and annotated as: Location, Position/Direction, Object, Time-Guidance, Person, Gesture/Gaze (this, that, over there, etc.), and None. In addition to utterance-level intent types and their slots, word-level intent keywords are annotated as Intent as well. We obtained 1260 unique utterances having commands to AMIE from our in-cabin data-set. We expanded this data-set via Amazon Mechanical Turk and ended up with 3347 utterances having intents. The annotations for intents and slots are obtained on the transcribed utterances by majority voting of 3 annotators.
> 
> For slot filling and intent keywords extraction tasks, we experimented with seq2seq LSTMs and GRUs, and also Bidirectional LSTM/GRUs. The passenger utterance is fed into a Bi-LSTM network via an embedding layer as a sequence of words, which are transformed into word vectors. We also experimented with GloVe, word2vec, and fastText as pre-trained word embeddings. To prevent overfitting, a dropout layer is used for regularization. Best performing results are obtained with Bi-LSTMs and GloVe embeddings (6B tokens, 400K vocab size, dim 100).
> 
> For utterance-level intent detection, we experimented with mainly 5 models: (1) Hybrid: RNN + Rule-based, (2) Separate: Seq2one Bi-LSTM + Attention, (3) Joint: Seq2seq Bi-LSTM for slots/intent keywords & utterance-level intents, (4) Hierarchical + Separate, (5) Hierarchical + Joint. For (1), we extract intent keywords/slots (Bi-LSTM) and map them into utterance-level intent types (rule-based via term frequencies for each intent). For (2), we feed the whole utterance as input sequence and intent-type as single target. For (3), we experiment with the joint learning models BIBREF0 , BIBREF1 , BIBREF2 where we jointly train word-level intent keywords/slots and utterance-level intents (adding <BOU>/<EOU> terms to the start/end of utterances with intent types). For (4) and (5), we experiment with the hierarchical models BIBREF3 , BIBREF4 , BIBREF5 where we extract intent keywords/slots first, and then only feed the

### Relevance

Label: 

## Record 0704

Paper: Conversational Intent Understanding for Passengers in Autonomous Vehicles

### Question

> What intents does the paper explore?

### Passage

> After exploring various recent Recurrent Neural Networks (RNN) based techniques, we built our own hierarchical joint models to recognize passenger intents along with relevant slots associated with the action to be performed in AV scenarios. Our experimental results outperformed certain competitive baselines and achieved overall F1-scores of 0.91 for utterance-level intent recognition and 0.96 for slot extraction tasks.

### Relevance

Label: 

## Record 0705

Paper: Conversational Intent Understanding for Passengers in Autonomous Vehicles

### Question

> What intents does the paper explore?

### Passage

> The slot extraction and intent keywords extraction results are given in Table TABREF1 and Table TABREF2 , respectively. Table TABREF3 summarizes the results of various approaches we investigated for utterance-level intent understanding. Table TABREF4 shows the intent-wise detection results for our AMIE scenarios with the best performing utterance-level intent recognizer.

### Relevance

Label: 

## Record 0706

Paper: BERT Goes to Law School: Quantifying the Competitive Advantage of Access to Large Legal Corpora in Contract Understanding

### Question

> How big is dataset used for fine-tuning BERT?

### Passage

> Businesses rely on contracts to capture critical obligations with other parties, such as: scope of work, amounts owed, and cancellation policies. Various efforts have gone into automatically extracting and classifying these terms. These efforts have usually been modeled as: classification, entity and relation extraction tasks. In this paper we focus on classification, but in our application we have found that our findings apply equally and sometimes, more profoundly, on other tasks.
> 
> Recently, numerous studies have shown the value of fine-tuning language models such as ELMo BIBREF2 and BERT BIBREF3 to achieve state-of-the-art results BIBREF4 on domain specific tasks BIBREF5, BIBREF6. In this paper we investigate and quantify the impact of utilizing a large domain-specific corpus of legal agreements to improve the accuracy of classification models by fine-tuning BERT. Specifically, we assess: (i) the performance of a simple model that only uses the pre-trained BERT language model, (ii) the impact of further fine tuning BERT, and (iii) how this impact changes as we train on larger corpora.
> 
> Ultimately, our investigations show marginal, but valuable, improvements that increase as we grow the size of the legal corpus used to fine-tine BERT — and allow us to confidently claim that not only is this approach valuable for increasing accuracy, but commercial enterprises seeking to create these models will have an edge if they can amass a corpus of legal documents.

### Relevance

Label: 

## Record 0707

Paper: BERT Goes to Law School: Quantifying the Competitive Advantage of Access to Large Legal Corpora in Contract Understanding

### Question

> How big is dataset used for fine-tuning BERT?

### Passage

> To fine-tune BERT, we used a proprietary corpus that consists of hundreds of thousands of legal agreements. We extracted text from the agreements, tokenized it into sentences, and removed sentences without alphanumeric text. We selected the BERT-Base uncased pre-trained model for fine-tuning. To avoid including repetitive content found at the beginning of each agreement we selected the 31st to 50th sentence of each agreement. We ran unsupervised fine-tuning of BERT using sequence lengths of 128, 256 and 512. The loss function over epochs is shown in Figure FIGREF3.

### Relevance

Label: 

## Record 0708

Paper: BERT Goes to Law School: Quantifying the Competitive Advantage of Access to Large Legal Corpora in Contract Understanding

### Question

> How big is dataset used for fine-tuning BERT?

### Passage

> We use 4 metrics to compare performance across various experiments: Matthews Correlation Coefficient, as well as Precision, Recall and F1 score weighted by class size. In table TABREF10 we show the various results we got from different configurations. It's clear that using pre-trained BERT, we're able to achieve a significant performance lift compared to the base line. It is also clear that fine-tuning BERT on a domain-specific corpus noticeably improves this lift, even when the corpus size is small and we train for a short time.
> 
> In Figure FIGREF3 we also show the different rates of change in train loss across epochs between pre-trained BERT vs fine-tuned Bert. As shown, the model trained on the fine-tuned version learns faster as evident in the faster drop in train loss on the training set (note the logarithmic y-axis).
> 
> It is worth mentioning that our BERT-based architecture is very simplistic for the sake of a fair comparison. In practice, having a deeper neural network on top of BERT that is specialized in the end task yields much more impressive results, and that's the architecture we use in our system. We show the result of using a slightly more advanced architecture with fine-tuned BERT in table TABREF11 to demonstrate what's possible without any sophisticated feature engineering or hyper-parameter tuning.

### Relevance

Label: 

## Record 0709

Paper: BERT Goes to Law School: Quantifying the Competitive Advantage of Access to Large Legal Corpora in Contract Understanding

### Question

> How big is dataset used for fine-tuning BERT?

### Passage

> We conclude that: (i) pre-trained BERT model adds a significant improvement to the classification task in the legal domain, (ii) fine-tuning BERT on a large legal corpus adds marginal but practically valuable improvements in both accuracy and training speed, (iii) fine-tuning both the language model independently and as part of the end task yield the best performance and reduces the need for a more sophisticated architecture and/or features and (iv) a large legal corpus, even an unannotated one, is a very valuable asset and a significant competitive advantage for NLP applications in that domain.

### Relevance

Label: 

## Record 0710

Paper: BERT Goes to Law School: Quantifying the Competitive Advantage of Access to Large Legal Corpora in Contract Understanding

### Question

> How big is dataset used for fine-tuning BERT?

### Passage

> We split our classification dataset into train (80%) and validation (20%) sets. For all architecture variations, we train for a variable number of epochs as long as the validation error is decreasing. We stop training when validation error starts increasing again and then report the final result on a held-out test set. In doing so we try to avoid over-fitting on the training set.

### Relevance

Label: 

## Record 0711

Paper: Improved Document Modelling with a Neural Discourse Parser

### Question

> What datasets are used for this tasks?

### Passage

> BIBREF15 show that discourse analyses produced by an RST parser can improve document-level sentiment analysis. Based on DPLP (Discourse Parsing from Linear Projection) — an RST parser by BIBREF6 — they recursively propagate sentiment scores up to the root via a neural network.
> 
> A similar idea was proposed by BIBREF16, where a recursive neural network is used to learn a discourse-aware representation. Here, DPLP is utilized to obtain discourse structures, and a recursive neural network is applied to the doc2vec BIBREF17 representations for each EDU. The proposed approach is evaluated over sentiment analysis and sarcasm detection tasks, but found to not be competitive with benchmark methods.
> 
> Our work is different in that we use the latent representation (as distinct from the decoded discrete predictions) obtained from a neural RST parser. It is most closely related to the work of BIBREF15 and BIBREF16, but intuitively, our discourse representations contain richer information, and we evaluate over more tasks such as popularity prediction of online petitions.

### Relevance

Label: 

## Record 0712

Paper: Improved Document Modelling with a Neural Discourse Parser

### Question

> What datasets are used for this tasks?

### Passage

> In this paper, we explore incorporating discourse information into two tasks: abstractive summarization and popularity prediction of online petitions. We experiment with both hand-engineered shallow features and latent features extracted from a neural discourse parser, and found that adding them generally benefits both tasks. The caveat, however, is that the best method of incorporation and feature type (shallow or latent) appears to be task-dependent, and so it remains to be seen whether we can find a robust universal approach for incorporating discourse information into NLP tasks.

### Relevance

Label: 

## Record 0713

Paper: Improved Document Modelling with a Neural Discourse Parser

### Question

> What datasets are used for this tasks?

### Passage

> We conduct our summarization experiments using the anonymized CNN/DailyMail corpus BIBREF20. We follow the data preprocessing steps in see2017get to obtain 287K training examples, 13K validation examples, and 11K test examples.
> 
> All of our experiments use the default hyper-parameter configuration of see2017get. Every document and its summary pair are truncated to 400 and 100 tokens respectively (shorter texts are padded accordingly). The model has 256-dimensional hidden states and 128-dimensional word embeddings, and vocabulary is limited to the most frequent 50K tokens. During test inference, we similarly limit the length of the input document to 400 words and the length of the generated summary to 35–100 words for beam search.
> 
> Our experiment has two pointer–generator network baselines: (1) one without the coverage mechanism (“PG”); and (2) one with the coverage mechanism (“PG$+$Cov”; Section SECREF14). For each baseline, we incorporate the latent and shallow discourse features separately in 3 ways (Section SECREF18), giving us 6 additional results.
> 
> We train the models for approximately 240,000-270,000 iterations (13 epochs). When we include the coverage mechanism (second baseline), we train for an additional 3,000–3,500 iterations using the coverage penalty, following see2017get.
> 
> We use ROUGE BIBREF21 as our evaluation metric, which is a standard measure based on overlapping n-grams between the generated summary and the reference summary. We assess unigram (R-1), bigram (R-2), and longest-common-subsequence (R-L) overlap, and present F1, recall and precision scores in Table TABREF17.
> 
> For the first baseline (PG), we see that incorporating discourse features consistently improves recall and F1. This observation is consistent irrespective of how (e.g. M1 or M2) and what (e.g. shallow or latent features) we add. These improvements do come at the expense of precision, with the exception of M2-latent (which produces small improvements in precision). Ultimately however, the latent features are in general a little better, with M2-latent produing the best results based on F1.
> 
> We see similar observations for the second baseline (PG$+$Cov): recall is generally improved at the expense of precision. In terms of F1, the gap between the baseline and our models is a little closer, and M1-latent and M2-latent are the two best performers.

### Relevance

Label: 

## Record 0714

Paper: Improved Document Modelling with a Neural Discourse Parser

### Question

> What datasets are used for this tasks?

### Passage

> Natural language generation and document classification have been widely conducted using neural sequence models based on the encoder–decoder architecture. The underlying technique relies on the production of a context vector as the document representation, to estimate both tokens in natural language generation and labels in classification tasks. By combining recurrent neural networks with attention BIBREF0, the model is able to learn contextualized representations of words at the sentence level. However, higher-level concepts, such as discourse structure beyond the sentence, are hard for an RNN to learn, especially for longer documents. We hypothesize that NLP tasks such as summarization and document classification can be improved through the incorporation of discourse information.
> 
> In this paper, we propose to incorporate latent representations of discourse units into neural training. A discourse parser can provide information about the document structure as well as the relationships between discourse units. In a summarization scenario, for example, this information may help to remove redundant information or discourse disfluencies. In the case of document classification, the structure of the text can provide valuable hints about the document category. For instance, a scientific paper follows a particular discourse narrative pattern, different from a short story. Similarly, we may be able to predict the societal influence of a document such as a petition document, in part, from its discourse structure and coherence.
> 
> Specifically, discourse analysis aims to identify the organization of a text by segmenting sentences into units with relations. One popular representation is Rhetorical Structure Theory (RST) proposed by mann1988rhet, where the document is parsed into a hierarchical tree, where leaf nodes are the segmented units, known as Entity Discourse Units (EDUs), and non-terminal nodes define the relations.
> 
> As an example, in Figure FIGREF1 the two-sentence text has been annotated with discourse structure based on RST, in the form of 4 EDUs connected with discourse labels attr and elab. Arrows in the tree capture the nuclearity of relations, wherein a “satellite” points to its “nucleus”. The Nucleus unit is considered more prominent than the Satellite, indicating that the Satellite is a supporting sentence for the Nucleus. Nuclearity relationships between two EDUs can take the following three forms: Nucleus–Satellite, Satellite–Nucleus, and Nucleus–Nucleus. In this work, we

### Relevance

Label: 

## Record 0715

Paper: Improved Document Modelling with a Neural Discourse Parser

### Question

> What datasets are used for this tasks?

### Passage

> Research has shown that discourse parsing is valuable for summarization. Via the RST tree, the salience of a given text can be determined from the nuclearity structure. In extractive summarization, BIBREF9, BIBREF10, and BIBREF11 suggest introducing penalty scores for each EDU based on the nucleus–satellite structure. In recent work, BIBREF12 utilizes the topic relation to divide documents into sentences with similar topics. Every chunk of sentences is then summarized in extractive fashion, resulting in a concise summary that covers all of the topics discussed in the passage.
> 
> Although the idea of using discourse information in summarization is not new, most work to date has focused on extractive summarization, where our focus is abstractive summarization. BIBREF13 used the parser of BIBREF14 to RST-parse product reviews. By extracting graph-based features, important aspects are identified in the review and included in the summary based on a template-based generation framework. Although the experiment shows that the RST can be beneficial for content selection, the proposed feature is rule-based and highly tailored to review documents. Instead, in this work, we extract a latent representation of the discourse directly from the BIBREF1 parser, and incorporate this into the abstractive summarizer.

### Relevance

Label: 

## Record 0716

Paper: Casting a Wide Net: Robust Extraction of Potentially Idiomatic Expressions

### Question

> What compleentary PIE extraction methods are used to increase reliability further?

### Passage

> In order to evaluate the PIE extraction methods developed in this work (Section SECREF6), we exhaustively annotate an evaluation corpus with all instances of a pre-defined set of PIEs. As part of this, we come up with a workable definition of PIEs, and measure the reliability of PIE annotation by inter-annotator agreement.
> 
> Assuming that we have a set of idioms, the main problem of defining what is and what is not a potentially idiomatic expression is caused by variation. In principle, potentially idiomatic expression is an instance of a phrase that, when seen without context, could have either an idiomatic or a literal meaning. This is clearest for the dictionary form of the idiom, as in Example SECREF5. Literal uses generally allow all kinds of variation, but not all of these variations allow a figurative interpretation, e.g. Example SECREF5. However, how much variation an idiom can undergo while retaining its figurative interpretation is different for each expression, and judgements of this might vary from one speaker to the other. An example of this is spill the bean, a variant of spill the beans, in Example SECREF5 judged by BIBREF21 as being highly questionable. However, even here a corpus example can be found containing the same variant used in a figurative sense (Example SECREF5).
> 
> As such, we assume that we cannot know a priori which variants of an expression allow a figurative reading, and are thus a potentially idiomatic expression. Therefore we consider every possible morpho-syntactic variation of an idiom a PIE, regardless of whether it actually allows a figurative reading. We believe the boundaries of this variation can only be determined based on corpus evidence, and even then they are likely variable.
> 
> Note that a similar question is tackled by BIBREF26, when they establish the boundary between a `literal reading of a VMWE' and a `coincidental co-occurrence'. BIBREF26's answer is similar to ours, in that they count something as a literal reading of a VMWE if it `the same or equivalent dependencies hold between [the expression]'s components as in its canonical form'.
> 
> . John kicked the bucket last night.
> 
> . * The bucket, John kicked last night.
> 
> . ?? Azin spilled the bean. (from BIBREF21)

### Relevance

Label: 

## Record 0717

Paper: Casting a Wide Net: Robust Extraction of Potentially Idiomatic Expressions

### Question

> What compleentary PIE extraction methods are used to increase reliability further?

### Passage

> In order to determine which of the methods described previously produces the highest quality extraction of potentially idiomatic expressions, we evaluate them, in various settings, on the corpus described in Section SECREF5.
> 
> For parser-based extraction, systems with and without in-context parsing, ignoring labels, and ignoring directionality are tested. For the three string-based extraction methods, varying numbers of intervening words and case sensitivity are evaluated. Evaluation is done using the development set, consisting of 22 documents and 1112 PIE candidates, and the test set, which consists of 23 documents and 1127 PIE candidates. For each method the best set of parameters and/or options is determined using the development set, after which the best variant by F1-score of each method is evaluated on the test set.
> 
> Since these documents in the corpus are exhaustively annotated for PIEs (see Section SECREF40), we can calculate true and false positives, and false negatives, and thus precision, recall and F1-score. The exact spans are ignored, because the spans annotated in the evaluation corpus are not completely reliable. These were automatically generated during candidate extraction, as described in Section SECREF45. Rather, we count an extraction as a true positive if it finds the correct PIE type in the correct sentence.
> 
> Note that we judge the system with the highest F1-score to be the best-performing system, since it is a clear and objective criterion. However, when using the system in practice, the best performance depends on the goal. When used as a preprocessing step for PIE disambiguation, the system with the highest F1-score is perhaps the most suitable, but as a corpus building tool, one might want to sacrifice some precision for an increase in recall. This helps to get the most comprehensive annotation of PIEs possible, without overloading the annotators with false extractions (i.e. non-PIEs), by maintaining high precision.
> 
> The results for each system on the development set are presented in Tables TABREF70 and TABREF71. Generally, results are in line with expectations: (the best) parse-based methods are better than (the best) string-based methods, and within string-based methods, inflectional matching works best. The same goes for the different settings: case-sensitivity increases precision at the cost of recall, allowing intervening words increases recall at

### Relevance

Label: 

## Record 0718

Paper: Casting a Wide Net: Robust Extraction of Potentially Idiomatic Expressions

### Question

> What compleentary PIE extraction methods are used to increase reliability further?

### Passage

> Since the parser-based method parses PIEs without any context, it often finds an incorrect parse, as for jump ship in Figure FIGREF65. As such, we add an option to the method that aims to increase the number of correct parses by parsing the PIE within context, that is, within a sentence. This can greatly help to disambiguate the parse, as in Figure FIGREF66. If the number of correct parses goes up, the recall of the extraction method should also increase. Naturally, it can also be the case that a PIE is parsed correctly without context, and incorrectly with context. However, we expect the gains to outweigh the losses.
> 
> The challenge here is thus to collect example sentences containing the PIE. Since the whole point of this work is to extract PIEs from raw text, this provides a catch-22-like situation: we need to extract a sentence containing a PIE in order to extract sentences containing a PIE.
> 
> The workaround for this problem is to use the exact string matching method with the dictionary form of the PIE and a very large plain text corpus to gather example sentences. By only considering the exact dictionary form we both simplify the finding of example sentences and the extraction of the PIE's parse from the sentence parse.
> 
> In case multiple example sentences are found, the shortest sentence is selected, since we assume it is easiest to parse. This is also the reason we make use of very large corpora, to increase the likelihood of finding a short, simple sentence. The example sentence extraction method is modified in such a way that sentences where the PIE is used meta-linguistically in quotes, e.g. “the well-known English idiom `to spill the beans' has no equivalents in other languages”, are excluded, since they do not provide a natural context for parsing. When no example sentence can be found in the corpus, we back-off to parsing the PIE without context. After a parse has been found for each PIE (i.e. with or without context), the method proceeds identically to the regular parser-based method.
> 
> We make use of the combination of two large corpora for the extraction of example sentences: the English Wikipedia, and ukWaC

### Relevance

Label: 

## Record 0719

Paper: Casting a Wide Net: Robust Extraction of Potentially Idiomatic Expressions

### Question

> What compleentary PIE extraction methods are used to increase reliability further?

### Passage

> In sum, there is large variation in corpus creation methods, regarding PIE definition, extraction method, annotation schemes, base corpus, and PIE type inventory. Depending on the goal of the corpus, the amount of deviation that is allowed from the PIE's dictionary form to the instances can be very little BIBREF14, to quite a lot BIBREF10. The number of PIE types covered by each corpus is limited, ranging from 17 to 65 types, often limited to one or more syntactic patterns. The extraction of PIE instances is usually done in a semi-automatic manner, by manually defining patterns in a text or parse tree, and doing some manual filtering afterwards. This works well, but an extension to a large number of PIE types (e.g. several hundreds) would also require a large increase in the amount of manual effort involved. Considering the sense annotations done on the PIE corpora, there is significant variation, with BIBREF9 using only three tags, whereas BIBREF10 use six. Outside of PIE-specific corpora there are MWE corpora, which provide a different perspective. A major difference there is that annotation is not restricted to a pre-specified set of expressions, which has not been done for PIEs specifically.

### Relevance

Label: 

## Record 0720

Paper: Casting a Wide Net: Robust Extraction of Potentially Idiomatic Expressions

### Question

> What compleentary PIE extraction methods are used to increase reliability further?

### Passage

> There are two main approaches to idiom extraction. The first approach aims to distinguish idioms from other multiword phrases, where the main purpose is to expand idiom inventories with rare or novel expressions BIBREF21, BIBREF22, BIBREF23, BIBREF24. The second approach aims to extract all occurrences of a known idiomatic expression in a text. In this paper, we focus on the latter approach. We rely on idiom dictionaries to provide a list of PIE types, and build a system that extracts all instances of those PIE types from a corpus. High-quality idiom dictionaries exist for most well-resourced languages, but their reliability and coverage is not known. As such, we quantify the coverage of dictionaries in Section SECREF4.
> 
> There is, to the best of our knowledge, no existing work that focuses on dictionary-based PIE extraction. However, there is closely-related work by BIBREF25, who present a system for the dictionary-based extraction of verb-noun combinations (VNCs) in English and Spanish. In their case, the VNCs can be any kind of multiword expression, which they subdivide into literal expressions, collocations, light verb constructions, metaphoric expressions, and idioms. They extract 173 English VNCs and 150 Spanish VNCs and annotate these with both their lexico-semantic MWE type and the amount of morphosyntactic variation they exhibit. BIBREF25 then compare a word sequence-based method, a chunking-based method, and a parse-based method for VNC extraction. Each method relies on the morpho-syntactic information in order to limit false extractions. Precision is evaluated manually on a sample of the extracted VNCs, and recall is estimated by calculating the overlap between the output of the three methods. Evaluation shows that the methods are highly complementary both in recall, since they extract different VNCs, and in precision, since combining the extractors yields fewer false extractions.
> 
> Whereas BIBREF25 focus on both idiomatic and literal uses of the set of expressions, like in this paper, BIBREF26 tackle only half of that task, namely extracting only literal uses of a given set of VMWEs in Polish. This complicates the task, since it combines extracting all occurrences of the VMWEs and then distinguishing literal from idiomatic uses. Interestingly, they also experiment with models of varying complexity, i.e. just words, part-of-speech tags, and syntactic

### Relevance

Label: 

## Record 0721

Paper: Improving Span-based Question Answering Systems with Coarsely Labeled Data

### Question

> Will these findings be robust through different datasets and different question answering algorithms?

### Passage

> There have been several works addressing the paucity of annotated data for QA. Data noisily annotated with short answer spans has been generated automatically through distant supervision and shown to be useful BIBREF14 . Unlabeled text and data augmentation through machine translation have been used to improve model quality BIBREF17 , BIBREF18 , BIBREF19 . min-seo-hajishirzi:2017:Short used short-answer annotations in SQuAD BIBREF1 to improve paragraph-level question answering for WikiQA BIBREF16 . To the best of our knowledge, there has been no prior work using QA data annotated at the paragraph level to improve models for short question answering.

### Relevance

Label: 

## Record 0722

Paper: Improving Span-based Question Answering Systems with Coarsely Labeled Data

### Question

> Will these findings be robust through different datasets and different question answering algorithms?

### Passage

> We focus on the document-level variant of the SQuAD dataset BIBREF1 , as defined by docqa, where given a question and document, the task is to determine the relevant passage and answer span within the passage $(a_p, a_{\mathit {start}}, a_{\mathit {end}})$ . We define finely annotated subsets $D_{y}$ with two different sizes: 5% and 20% of the original dataset. These are paired with non-overlapping subsets of coarsely annotated data $D_{z}$ with sizes 20% and 70% of the original training set, respectively. Both of these settings represent the regime where coarsely annotated data is available in higher volume, because such data can be obtained faster and at lower cost. For both dataset settings, we derive $D_{y}$ and $D_{z}$ from the SQuAD training set, by allocating whole documents with all their corresponding questions to a given subset. In both settings, we also reserve a finely annotated non-overlapping set $\mbox{Dev}_{y}$ , which is used to select optimal hyperparameters for each method. We report final performance metrics on $\mbox{Test}_{y}$ , which is the unseen SQuAD development set.

### Relevance

Label: 

## Record 0723

Paper: Improving Span-based Question Answering Systems with Coarsely Labeled Data

### Question

> Will these findings be robust through different datasets and different question answering algorithms?

### Passage

> In span-based reading comprehension, a system must be able to extract a plausible text-span answer for a given question from a context document or paragraph BIBREF1 , BIBREF14 , BIBREF15 . Most work has focused on selecting short answers given relevant paragraphs, but datasets and works considering the more realistic task of selection from full documents are starting to appear BIBREF14 .
> 
> Sentence selection or paragraph selection datasets test whether a system can correctly rank texts that are relevant for answering a question higher than texts that do not. Wang2007EMNLP constructed the QASent dataset based on questions from TREC 8-13 QA tracks. WikiQA BIBREF16 associates questions from Bing search query log with all the sentences in the Wikipedia summary paragraph which is then labeled by crowd workers. Most state-of-the-art models for both types of tasks make use of neural network modules to construct and compare representations for a question and the possible answers. We build on a near state-of-the-art baseline model and evaluate on a document-level short question answering task.

### Relevance

Label: 

## Record 0724

Paper: Improving Span-based Question Answering Systems with Coarsely Labeled Data

### Question

> Will these findings be robust through different datasets and different question answering algorithms?

### Passage

> We report results evaluating the impact of using coarsely annotated data in the two dataset conditions in Figure 3 . There are two groups of rows corresponding to the two data sizes: in the smaller setting, only 5% of the original fine-grained data is used, and in the medium setting, 20% of the fine-grained data is used. The first row in each group indicates the performance when using only finely labeled fully supervised data. The column Fine-F1 indicates the performance metric of interest – the test set performance on document-level short answer selection. The next rows indicate the performance of a multi-task and the best latent variable method when using the finely labeled data plus the additional coarsely annotated datasets. The ceiling performance in each group shows the oracle achieved by a model also looking at the gold fine-grained labels for the data that the rest of the models see with only coarse paragraph-level annotation. The column Gain indicates the relative error reduction of each model compared to the supervised-only baseline with respect to the ceiling upper bound. As we can see all models benefit from coarsely labeled data and achieve at least 20% error reduction. The best latent variable method (Posterior Distillation with squared error distance) significantly outperforms the multi-task approach, achieving up to 41% relative gain.
> 
> Figure 4 compares the performance of the three different optimization methods using latent fine-grained answer variables for coarsely annotated data. Here we inlcude an additional last column reporting performance on an easier task where the correct answer paragraph is given at test time, and the model only needs to pick out the short answer within the given paragraph. We include this measurement to observe whether models are improving just by picking out relevant paragraphs or also by selecting the finer-grained short answers within them. Since EM and MML are known to optimize the same function, it is unsurprising that MML and PD with cross-entropy (equivalent to EM) perform similarly. For posterior distillation, we observe substantially better performance with the squared error as the distance function, particularly in the second setting, where there is more coarsely annotated data.
> 
> To gain more insight into the behavior of the different

### Relevance

Label: 

## Record 0725

Paper: Improving Span-based Question Answering Systems with Coarsely Labeled Data

### Question

> Will these findings be robust through different datasets and different question answering algorithms?

### Passage

> perform similarly. For posterior distillation, we observe substantially better performance with the squared error as the distance function, particularly in the second setting, where there is more coarsely annotated data.
> 
> To gain more insight into the behavior of the different methods using coarsely annotated data, we measured properties of the predictive distributions $P(y|x,\theta )$ for the three methods on the dataset used with coarse labels in training $D_{70coarse}$ . The results are shown in Figure 5 . For models MTL, MML, PD( $xent$ ), and PD( $err^2$ ), trained on finely labeled $D_{20fine}$ and coarsely labeled $D_{70coarse}$ , we study the predictive distributions $P(y|x,\theta ^M)$ for the four model types $M$ . We measure the properties of these distributions on the dataset $D_{70fine}$ , which is the finely labeled version of the same (question, document)-pairs $D_{70}$ as $D_{70coarse}$0 . Note that none of the models see the fine-grained short answer labels for $D_{70coarse}$1 in training since they only observe paragraph-level relevance annotations. Nevertheless, the models can assign a probability distribution over fine-grained labels in the documents, and we can measure the peakiness (entropy) of this distribution, as well as see how it compares to the gold hidden label distribution.
> 
> The first column in the table reports the entropies of the predictive distributions for the four trained models (using the fine task model for the multi-task method MTL). We can see that multi-task method MTL and PD( $xent$ ) (which is equivalent to generalized EM) have lowest entropy, and are most confident about their short answer predictions. MML marginalizes over possible fine answers, resulting in flatter predictive distributions which spread mass among multiple plausible answer positions. The best-performing method PD( $err^2$ ) is somewhere in between and maintains more uncertainty. The next two columns in the Table look at the cross-entropy ( $xent$ ) and squared error ( $err^2$ ) distances of the predictive distributions with respect to the gold one. The gold label distribution has mass of one on a single point indicating the correct fine answer positions. Note that none of the models have seen this gold distribution during training and have thus not been trained to minimize these distances (the PD latent variable

### Relevance

Label: 

## Record 0726

Paper: Enhancing Pre-trained Chinese Character Representation with Word-aligned Attention

### Question

> What pre-trained models did they compare to?

### Passage

> In this paper, we propose an effective architecture Word-aligned Attention to incorporate word segmentation information into character-based pre-trained language models, which is adopted to a variety of downstream NLP tasks as an extend layer in fine-tuned process. And we also employ more segmenters into via proposed Multi-source Word-aligned Attention for reducing segmentation error. The experimental results show the effectiveness of our method. Comparing to BERT, ERNIE and BERT-wwm, our model obtains substantial improvements on various NLP benchmarks. Although we mainly focused on Chinese PLM in this paper, our model would take advantage the capabilities of Word-aligned Attention for word-piece in English NLP task. We are also considering applying this model into pre-training language model for various Language Model task in different grain to capture multi-level language features.

### Relevance

Label: 

## Record 0727

Paper: Enhancing Pre-trained Chinese Character Representation with Word-aligned Attention

### Question

> What pre-trained models did they compare to?

### Passage

> To test the applicability of the proposed MWA attention, we choose three publicly available Chinese pre-trained models as the basic encoder: BERT, ERNIE, and BERT-wwm. In order to make a fair comparison, we keep the same hyper-parameters (such maximum length, warm-up steps, initial learning rate, etc) as suggested in BERT-wwm BIBREF13 for both baselines and our method on each dataset. We run the same experiment for five times and report the average score to ensure the reliability of results. For detailed hyper-parameter settings, please see Appendix. Besides, three popular CWS tools thulac BIBREF14, ictclas BIBREF15 and hanlp BIBREF16 are employed to segment the Chinese sentences into words.
> 
> We carried out experiments on four Chinese NLP tasks, including Emotion Classification (EC), Named Entity Recognition (NER), Sentence Pair Matching (SPM) and Natural Language Inference (NLI). The detail of those tasks and the corresponding datasets are introduced in Appendix.

### Relevance

Label: 

## Record 0728

Paper: Enhancing Pre-trained Chinese Character Representation with Word-aligned Attention

### Question

> What pre-trained models did they compare to?

### Passage

> Pre-trained language Models (PLM) such as ELMo BIBREF0, BERT BIBREF1, ERNIE BIBREF2 and XLNet BIBREF3 have been proven to capture rich language information from text and then benefit many NLP applications by simple fine-tuning, including sentiment classification, natural language inference, named entity recognition and so on.
> 
> Generally, most of PLMs focus on using attention mechanism BIBREF4 to represent the natural language, such as word-level attention for English and character-level attention for Chinese. Unlike English, in Chinese, words are not separated by explicit delimiters, which means that character is the smallest linguistic unit. However, in most cases, the semantic of single Chinese character is ambiguous. UTF8gbsn For example, in Table 1, using the attention over word 西山 is more intuitive than over the two individual characters 西 and 山. Moreover, previous work has shown that considering the word segmentation information can lead to better language understanding and accordingly benefits various Chines NLP tasks BIBREF5, BIBREF6, BIBREF7.
> 
> All these factors motivate us to expand the character-level attention mechanism in Chinese PLM to represent attention over words . To this end, there are two main challenges. (1) How to seamlessly integrate word segmentation information into character-level attention module of PLM is an important problem. (2) Gold-standard segmentation is rarely available in the downstream tasks, and how to effectively reduce the cascading noise caused by automatic segmentation tools BIBREF8 is another challenge.
> 
> In this paper, we propose a new architecture, named Multi-source Word Alignd Attention (MWA), to solve the above issues. (1) Psycholinguistic experiments BIBREF9, BIBREF10 have shown that readers are likely to pay approximate attention to each character in one Chinese word. Drawing inspiration from such finding, we introduce a novel word-aligned attention, which could aggregate attention weight of characters in one word into a unified value with the mixed pooling strategy BIBREF11. (2) For reducing segmentation error, we further extend our word-aligned attention with multi-source segmentation produced by various segmenters, and deploy a fusion function to pull together their disparate output. In this way, we can implicitly reduce the error caused by automatic annotation.
> 
> Extensive experiments are conducted on various Chinese NLP datasets including named entity recognition, sentiment classification, sentence pair matching, natural language inference, etc. The

### Relevance

Label: 

## Record 0729

Paper: Enhancing Pre-trained Chinese Character Representation with Word-aligned Attention

### Question

> What pre-trained models did they compare to?

### Passage

> The primary goal of this work is to inject the word segmentation knowledge into character-level Chinese PLM and enhance original models. Given the strong performance of recent deep transformers trained on language modeling, we adopt BERT and its updated variants (ERNIE, BERT-wwm) as the basic encoder for our work, and the outputs $\mathbf {H}$ from the last layer of encoder are treated as the enriched contextual representations.

### Relevance

Label: 

## Record 0730

Paper: Enhancing Pre-trained Chinese Character Representation with Word-aligned Attention

### Question

> What pre-trained models did they compare to?

### Passage

> Table TABREF14 shows the experiment measuring improvements from the MWA attention on test sets of four datasets. Generally, our method consistently outperforms all baselines on all of four tasks, which clearly indicates the advantage of introducing word segmentation information into the encoding of character sequences. Moreover, the Wilcoxon’s test shows that significant difference ($p< 0.01$) exits between our model with baseline models.
> 
> In detail, On the EC task, we observe 1.46% absolute improvement in F1 score over ERINE. SPM and NLI tasks can also gain benefits from our enhanced representation, achieving an absolute F1 increase of 0.68% and 0.55% over original models averagely. For the NER task, our method improves the performance of BERT by 1.54%, and obtains 1.23% improvement averagely over all baselines. We attribute such significant gain in NER to the particularity of this task. Intuitively, Chinese NER is correlated with word segmentation, and named entity boundaries are also word boundaries. Thus the potential boundary information presented by the additional segmentation input can provide a better guidance to label each character, which is consistent with the conclusion in BIBREF6, BIBREF7.

### Relevance

Label: 

## Record 0731

Paper: SUM-QE: a BERT-based Summary Quality Estimation Model

### Question

> What dataset do they use?

### Passage

> This baseline is the ROUGE version that performs best on each dataset, among the versions considered by BIBREF13. Although ROUGE focuses on surface similarities between peer and reference summaries, we would expect properties like grammaticality, referential clarity and coherence to be captured to some extent by ROUGE versions based on long $n$-grams or longest common subsequences.

### Relevance

Label: 

## Record 0732

Paper: SUM-QE: a BERT-based Summary Quality Estimation Model

### Question

> What dataset do they use?

### Passage

> We use datasets from the NIST DUC-05, DUC-06 and DUC-07 shared tasks BIBREF7, BIBREF19, BIBREF20. Given a question and a cluster of newswire documents, the contestants were asked to generate a 250-word summary answering the question. DUC-05 contains 1,600 summaries (50 questions x 32 systems); in DUC-06, 1,750 summaries are included (50 questions x 35 systems); and DUC-07 has 1,440 summaries (45 questions x 32 systems).
> 
> The submitted summaries were manually evaluated in terms of content preservation using the Pyramid score, and according to five linguistic quality criteria ($\mathcal {Q}1, \dots , \mathcal {Q}5$), described in Figure FIGREF2, that do not involve comparison with a model summary. Annotators assigned scores on a five-point scale, with 1 and 5 indicating that the summary is bad or good with respect to a specific $\mathcal {Q}$. The overall score for a contestant with respect to a specific $\mathcal {Q}$ is the average of the manual scores assigned to the summaries generated by the contestant. Note that the DUC-04 shared task involved seven $\mathcal {Q}$s, but some of them were found to be highly overlapping and were grouped into five in subsequent years BIBREF20. We address these five criteria and use DUC data from 2005 onwards in our experiments.

### Relevance

Label: 

## Record 0733

Paper: SUM-QE: a BERT-based Summary Quality Estimation Model

### Question

> What dataset do they use?

### Passage

> Summarization evaluation metrics like Pyramid BIBREF5 and ROUGE BIBREF3, BIBREF2 are recall-oriented; they basically measure the content from a model (reference) summary that is preserved in peer (system generated) summaries. Pyramid requires substantial human effort, even in its more recent versions that involve the use of word embeddings BIBREF8 and a lightweight crowdsourcing scheme BIBREF9. ROUGE is the most commonly used evaluation metric BIBREF10, BIBREF11, BIBREF12. Inspired by BLEU BIBREF4, it relies on common $n$-grams or subsequences between peer and model summaries. Many ROUGE versions are available, but it remains hard to decide which one to use BIBREF13. Being recall-based, ROUGE correlates well with Pyramid but poorly with linguistic qualities of summaries. BIBREF14 proposed a regression model for measuring summary quality without references. The scores of their model correlate well with Pyramid and Responsiveness, but text quality is only addressed indirectly.
> 
> Quality Estimation is well established in MT BIBREF15, BIBREF0, BIBREF1, BIBREF16, BIBREF17. QE methods provide a quality indicator for translation output at run-time without relying on human references, typically needed by MT evaluation metrics BIBREF4, BIBREF18. QE models for MT make use of large post-edited datasets, and apply machine learning methods to predict post-editing effort scores and quality (good/bad) labels.
> 
> We apply QE to summarization, focusing on linguistic qualities that reflect the readability and fluency of the generated texts. Since no post-edited datasets – like the ones used in MT – are available for summarization, we use instead the ratings assigned by human annotators with respect to a set of linguistic quality criteria. Our proposed models achieve high correlation with human judgments, showing that it is possible to estimate summary quality without human references.

### Relevance

Label: 

## Record 0734

Paper: SUM-QE: a BERT-based Summary Quality Estimation Model

### Question

> What dataset do they use?

### Passage

> We propose a novel Quality Estimation model for summarization which does not require human references to estimate the quality of automatically produced summaries. Sum-QE successfully predicts qualitative aspects of summaries that recall-oriented evaluation metrics fail to approximate. Leveraging powerful BERT representations, it achieves high correlations with human scores for most linguistic qualities rated, on three different datasets. Future work involves extending the Sum-QE model to capture content-related aspects, either in combination with existing evaluation metrics (like Pyramid and ROUGE) or, preferably, by identifying important information in the original text and modelling its preservation in the proposed summaries. This would preserve Sum-QE's independence from human references, a property of central importance in real-life usage scenarios and system development settings.
> 
> The datasets used in our experiments come from the NIST DUC shared tasks which comprise newswire articles. We believe that Sum-QE could be easily applied to other domains. A small amount of annotated data would be needed for fine-tuning – especially in domains with specialized vocabulary (e.g., biomedical) – but the model could also be used out of the box. A concrete estimation of performance in this setting will be part of future work. Also, the model could serve to estimate linguistic qualities other than the ones in the DUC dataset with mininum effort.
> 
> Finally, Sum-QE could serve to assess the quality of other types of texts, not only summaries. It could thus be applied to other text generation tasks, such as natural language generation and sentence compression.

### Relevance

Label: 

## Record 0735

Paper: SUM-QE: a BERT-based Summary Quality Estimation Model

### Question

> What dataset do they use?

### Passage

> The third version of Sum-QE is similar to BERT-FT-M-1, but we now use five different linear (affine) regressors, one per quality score:
> 
> Although BERT-FT-M-5 is mathematically equivalent to BERT-FT-M-1, in practice these two versions of Sum-QE produce different results because of implementation details related to how the losses of the regressors (five or one) are combined.

### Relevance

Label: 

## Record 0736

Paper: Using Monolingual Data in Neural Machine Translation: a Systematic Study

### Question

> what language pairs are explored?

### Passage

> As a follow up of previous discussions, we analyze the effect of BT on the internals of the network. Arguably, using a copy of the target sentence instead of a natural source should not be helpful for the encoder, but is it also the case with a strong BT? What are the effects on the attention model?

### Relevance

Label: 

## Record 0737

Paper: Using Monolingual Data in Neural Machine Translation: a Systematic Study

### Question

> what language pairs are explored?

### Passage

> We observe that the copy setup has only a small impact on the English-French system, for which the baseline is already strong. This is less true for English-German where simple copies yield a significant improvement. Performance drops for both language pairs in the copy-dummies setup.
> 
> We achieve our best gains with the copy-marked setup, which is the best way to use a copy of the target (although the performance on the out-of-domain tests is at most the same as the baseline). Such gains may look surprising, since the NMT model does not need to learn to translate but only to copy the source. This is indeed what happens: to confirm this, we built a fake test set having identical source and target side (in French). The average cross-entropy for this test set is 0.33, very close to 0, to be compared with an average cost of 58.52 when we process an actual source (in English). This means that the model has learned to copy words from source to target with no difficulty, even for sentences not seen in training. A follow-up question is whether training a copying task instead of a translation task limits the improvement: would the NMT learn better if the task was harder? To measure this, we introduce noise in the target sentences copied onto the source, following the procedure of BIBREF26 : it deletes random words and performs a small random permutation of the remaining words. Results (+ Source noise) show no difference for the French in-domain test sets, but bring the out-of-domain score to the level of the baseline. Finally, we observe a significant improvement on German in-domain test sets, compared to the baseline (about +1.5 BLEU). This last setup is even almost as good as the backtrans-nmt condition (see § SECREF8 ) for German. This shows that learning to reorder and predict missing words can more effectively serve our purposes than simply learning to copy.

### Relevance

Label: 

## Record 0738

Paper: Using Monolingual Data in Neural Machine Translation: a Systematic Study

### Question

> what language pairs are explored?

### Passage

> We are mostly interested with the following training scenario: a large out-of-domain parallel corpus, and limited monolingual in-domain data. We focus here on the Europarl domain, for which we have ample data in several languages, and use as in-domain training data the Europarl corpus BIBREF5 for two translation directions: English INLINEFORM0 German and English INLINEFORM1 French. As we study the benefits of monolingual data, most of our experiments only use the target side of this corpus. The rationale for choosing this domain is to (i) to perform large scale comparisons of synthetic and natural parallel corpora; (ii) to study the effect of BT in a well-defined domain-adaptation scenario. For both language pairs, we use the Europarl tests from 2007 and 2008 for evaluation purposes, keeping test 2006 for development. When measuring out-of-domain performance, we will use the WMT newstest 2014.

### Relevance

Label: 

## Record 0739

Paper: Using Monolingual Data in Neural Machine Translation: a Systematic Study

### Question

> what language pairs are explored?

### Passage

> Results are in Table TABREF32 , assuming the same fine-tuning procedure as above. On top of the copy-marked setup, our GANs do not provide any improvement in both language pairs, with the exception of a small improvement for English-French on the out-of-domain test, which we understand as a sign that the model is more robust to domain variations, just like when adding pseudo-source noise. When combined with noise, the French model yields the best performance we could obtain with stupid BT on the in-domain tests, at least in terms of BLEU and BEER. On the News domain, we remain close to the baseline level, with slight improvements in German.
> 
> A first observation is that this method brings stupid BT models closer to conventional BT, at a greatly reduced computational cost. While French still remains 0.4 to 1.0 BLEU below very good backtranslation, both approaches are in the same ballpark for German - may be because BTs are better for the former system than for the latter.
> 
> Finally note that the GAN architecture has two differences with basic copy-marked: (a) a distinct encoder for real and pseudo-sentence; (b) a different training regime for these encoders. To sort out the effects of (a) and (b), we reproduce the GAN setup with BT sentences, instead of copies. Using a separate encoder for the pseudo-source in the backtrans-nmt setup can be detrimental to performance (see Table TABREF32 ): translation degrades in French for all metrics. Adding GANs on top of the pseudo-encoder was not able to make up for the degradation observed in French, but allowed the German system to slightly outperform backtrans-nmt. Even though this setup is unrealistic and overly costly, it shows that GANs are actually helping even good systems.

### Relevance

Label: 

## Record 0740

Paper: Using Monolingual Data in Neural Machine Translation: a Systematic Study

### Question

> what language pairs are explored?

### Passage

> BT requires the availability of an MT system in the reverse translation direction. We consider here three MT systems of increasing quality:
> 
> backtrans-bad: this is a very poor SMT system trained using only 50k parallel sentences from the out-of-domain data, and no additional monolingual data. For this system as for the next one, we use Moses BIBREF17 out-of-the-box, computing alignments with Fastalign BIBREF18 , with a minimal pre-processing (basic tokenization). This setting provides us with a pessimistic estimate of what we could get in low-resource conditions.
> 
> backtrans-good: these are much larger SMT systems, which use the same parallel data as the baseline NMTs (see § SECREF4 ) and all the English monolingual data available for the WMT 2017 shared tasks, totalling approximately 174M sentences. These systems are strong, yet relatively cheap to build.
> 
> backtrans-nmt: these are the best NMT systems we could train, using settings that replicate the forward translation NMTs.
> 
> Note that we do not use any in-domain (Europarl) data to train these systems. Their performance is reported in Table TABREF7 , where we observe a 12 BLEU points gap between the worst and best systems (for both languages).
> 
> As noted eg. in BIBREF19 , BIBREF20 , artificial parallel data obtained through forward-translation (FT) can also prove advantageous and we also consider a FT system (fwdtrans-nmt): in this case the target side of the corpus is artificial and is generated using the baseline NMT applied to a natural source.
> 
> Our results (see Table TABREF6 ) replicate the findings of BIBREF2 : large gains can be obtained from BT (nearly INLINEFORM0 BLEU in French and German); better artificial data yields better translation systems. Interestingly, our best Moses system is almost as good as the NMT and an order of magnitude faster to train. Improvements obtained with the bad system are much smaller; contrary to the better MTs, this system is even detrimental for the out-of-domain test.
> 
> Gains with forward translation are significant, as in BIBREF21 , albeit about half as good as with BT, and result in small improvements for the in-domain and for the out-of-domain tests. Experiments combining forward and backward translation (backfwdtrans-nmt), each using a half of the available artificial data, do not

### Relevance

Label: 

## Record 0741

Paper: A multimodal deep learning approach for named entity recognition from social media

### Question

> Which social media platform is explored?

### Passage

> tasks such as named entity recognition and disambiguation BIBREF5 while some methods only use the textual data BIBREF6.
> 
> The provided extra information is closely related to the textual data. As a clear example, figure FIGREF1 shows a tweet containing an image. The combination of these multimodal data in order to achieve better performance in NLP related tasks is a promising alternative explored recently.
> 
> An NLP task such as named entity recognition in social media is a most challenging task because users tend to invent, mistype and epitomize words. Sometimes these words correspond to named entities which makes the recognition task even more difficult BIBREF7. In some cases, the context that carries the entity (surrounding words and related image) is more descriptive than the entity word presentation BIBREF8.
> 
> To find a solution to the issues at hand, and keeping multimodal data in mind, recognition of named entities from social media has become a research interest which utilizes image compared to NER task in a conventional text. Researchers in this field have tried to propose multimodal architectures based on deep neural networks with multimodal input that are capable of combining text and image BIBREF9, BIBREF8, BIBREF10.
> 
> In this paper we draw a better solution in terms of performance by proposing a new novel method called CWI (Character-Word-Image model). We used multimodal deep neural network to overcome the NER task in micro-blogging social media.
> 
> The rest of the paper is organized as follows: section SECREF2 provides an insight view of previous methods; section SECREF3 describes the method we propose; section SECREF4 shows experimental evaluation and test results; finally, section SECREF5 concludes the whole article.

### Relevance

Label: 

## Record 0742

Paper: A multimodal deep learning approach for named entity recognition from social media

### Question

> Which social media platform is explored?

### Passage

> A common social media delivery system such as Twitter supports various media types like video, image and text. This media allows users to share their short posts called Tweets. Users are able to share their tweets with other users that are usually following the source user. Hovewer there are rules to protect the privacy of users from unauthorized access to their timeline BIBREF0. The very nature of user interactions in Twitter micro-blogging social media is oriented towards their daily life, first witness news-reporting and engaging in various events (sports, political stands etc.). According to studies, news in twitter is propagated and reported faster than conventional news media BIBREF1. Thus, extracting first hand news and entities occurring in this fast and versatile online media gives valuable information. However, abridged and noisy content of Tweets makes it even more difficult and challenging for tasks such as named entity recognition and information retrieval BIBREF2.
> 
> The task of tracking and recovering information from social media posts is a concise definition of information retrieval in social media BIBREF3, BIBREF4. However many challenges are blocking useful solutions to this issue, namely, the noisy nature of user generated content and the perplexity of words used in short posts. Sometimes different entities are called exactly the same, for example "Micheal Jordan" refers to a basketball player and also a computer scientist in the field of artificial intelligence. The only thing that divides both of these is the context in which entity appeared. If the context refers to something related to AI, the reader can conclude "Micheal Jordan" is the scientist, and if the context is refers to sports and basketball then he is the basketball player. The task of distinguishing between different named entities that appear to have the same textual appearance is called named entity disambiguation. There is more useful data on the subject rather than on plain text. For example images and visual data are more descriptive than just text for tasks such as named entity recognition and disambiguation BIBREF5 while some methods only use the textual data BIBREF6.
> 
> The provided extra information is closely related to the textual data. As a clear example, figure FIGREF1 shows a tweet containing an

### Relevance

Label: 

## Record 0743

Paper: A multimodal deep learning approach for named entity recognition from social media

### Question

> Which social media platform is explored?

### Passage

> An LSTM unit has been used to output the final image features. These combined embeddings from the most probable items in image are the key to have extra information from a social media post.
> 
> where $IW$ is image-word vector, $x$ is output of InceptionV3 and $i$ is the image. $x$ is in domain of [0,1] and $\sum \limits _{\forall k\in x}k=1$ holds true, while $\sum \limits _{\forall k\in IW}k\le 1$.
> 
> Multimodal Fusion in our work is presented as concatenation of three feature sets extracted from words, characters and images. Unlike previous methods, our original work does not include an attention layer to remove noisy features. Instead, we stacked LSTM units from word and image feature extractors to have better results. The last layer presented at the top right side of figure FIGREF11 shows this part. In our second proposed method, we have used attention layer applied to this triplet. Our proposed attention mechanism is able to detect on which modality to increase or decrease focus. Equations DISPLAY_FORM17, and show attention mechanism related to second proposed model.
> 
> Conditional Random Field is the last layer in our setup which forms the final output. The same implementation explained in eq. DISPLAY_FORM5 is used for our method.

### Relevance

Label: 

## Record 0744

Paper: A multimodal deep learning approach for named entity recognition from social media

### Question

> Which social media platform is explored?

### Passage

> information from the whole sentence rather than only tokens and for that reason, it is also considered to be a sequence tagging problem. Another analogous problem to this issue is part of speech tagging and some methods are capable of doing both. However, in cases where noise is present and input sequence has linguistic typos, many methods fail to overcome the problem. As an example, consider a sequence of tokens where a new token invented by social media users gets trended. This trending new word is misspelled and is used in a sequence along with other tokens in which the whole sequence does not follow known linguistic grammar. For this special case, classical methods and those which use engineered features do not perform well.
> 
> Using the sequence $s$ itself or adding more information to it divides two approaches to overcome this problem: unimodal and multimodal.
> 
> Although many approaches for NER have been proposed and reviewing them is not in the scope of this article, we focus on foremost analogues classical and deep learning approaches for named entity recognition in two subsections. In subsection SECREF4 unimodal approaches for named entity recognition are presented while in subsection SECREF7 emerging multimodal solutions are described.

### Relevance

Label: 

## Record 0745

Paper: A multimodal deep learning approach for named entity recognition from social media

### Question

> Which social media platform is explored?

### Passage

> The recognition of named entities from only textual data (unimodal learning approach) is a well studied and explored research criteria. For a prominent example of this category, the Stanford NER is a widely used baseline for many applications BIBREF18. The incorporation of non-local information in information extraction is proposed by the authors using of Gibbs sampling. The conditional random field (CRF) approach used in this article, creates a chain of cliques, where each clique represents the probabilistic relationship between two adjacent states. Also, Viterbi algorithm has been used to infer the most likely state in the CRF output sequence. Equation DISPLAY_FORM5 shows the proposed CRF method.
> 
> where $\phi $ is the potential function.
> 
> CRF finds the most probable likelihood by modeling the input sequence of tokens $s$ as a normalized product of feature functions. In a simpler explanation, CRF outputs the most probable tags that follow each other. For example it is more likely to have an I-PER, O or any other that that starts with B- after B-PER rather than encountering tags that start with I-.
> 
> T-NER is another approach that is specifically aimed to answer NER task in twitter BIBREF19. A set of algorithms in their original work have been published to answer tasks such as POS (part of speech tagging), named entity segmentation and NER. Labeled LDA has been used by the authors in order to outperform baseline in BIBREF20 for NER task. Their approach strongly relies on dictionary, contextual and orthographic features.
> 
> Deep learning techniques use distributed word or character representation rather than raw one-hot vectors. Most of this research in NLP field use pretrained word embeddings such as Word2Vec BIBREF21, GloVe BIBREF22 or fastText BIBREF23. These low dimensional real valued dense vectors have proved to provide better representation for words compared to one-hot vector or other space vector models.
> 
> The combination of word embedding along with bidirectional long-short term memory (LSTM) neural networks are examined in BIBREF24. The authors also propose to add a CRF layer at the end of their neural network architecture in order to preserve output tag relativity. Utilization of recurrent neural networks (RNN) provides better sequential modeling over data. However, only using sequential information does not

### Relevance

Label: 

## Record 0746

Paper: Revealing the Dark Secrets of BERT

### Question

> In which certain heads was attention disabled in experiments?

### Passage

> Our experiments suggest that certain heads have a detrimental effect on the overall performance of BERT, and this trend holds for all the chosen tasks. Unexpectedly, disabling some heads leads not to a drop in accuracy, as one would expect, but to an increase in performance. This is effect is different across tasks and datasets. While disabling some heads improves the results, disabling the others hurts the results. However, it is important to note that across all tasks and datasets, disabling some heads leads to an increase in performance. The gain from disabling a single head is different for different tasks, ranging from the minimum absolute gain of 0.1% for STS-B, to the maximum of 1.2% for MRPC (see fig:disableheadsall). In fact, for some tasks, such as MRPC and RTE, disabling a random head gives, on average, an increase in performance. Furthermore, disabling a whole layer, that is, all 12 heads in a given layer, also improves the results. fig:disablelayers shows the resulting model performance on the target GLUE tasks when different layers are disabled. Notably, disabling the first layer in the RTE task gives a significant boost, resulting in an absolute performance gain of 3.2%. However, effects of this operation vary across tasks, and for QNLI and MNLI, it produces a performance drop of up to -0.2%.

### Relevance

Label: 

## Record 0747

Paper: Revealing the Dark Secrets of BERT

### Question

> In which certain heads was attention disabled in experiments?

### Passage

> The heatmap of averaged attention scores over all collected examples (fig:framenetresults) suggests that 2 out of 144 heads tend to attend to the parts of the sentence that FrameNet annotators identified as core elements of the same frame. fig:framenetresults shows an example of this attention pattern for these two heads. Both show high attention weight for “he” while processing “agitated” in the sentence “He was becoming agitated" (the frame “Emotion_directed”).

### Relevance

Label: 

## Record 0748

Paper: Revealing the Dark Secrets of BERT

### Question

> In which certain heads was attention disabled in experiments?

### Passage

> In this experiment, our goal was to understand whether different syntactic and semantic relations are captured by self-attention patterns. While a large number of such relations could be investigated, we chose to examine semantic role relations defined in frame semantics, since they can be viewed as being at the intersection of syntax and semantics. Specifically, we focused on whether BERT captures FrameNet's relations between frame-evoking lexical units (predicates) and core frame elements BIBREF19, and whether the links between them produce higher attention weights in certain specific heads. We used pre-trained BERT in these experiments.
> 
> The data for this experiment comes from FrameNet BIBREF19, a database that contains frame annotations for example sentences for different lexical units. Frame elements correspond to semantic roles for a given frame, for example, “buyer", “seller", and “goods” for the “Commercial_transaction" frame evoked by the words “sell” and “spend” or “topic” and “text” for the “Scrutiny” semantic frame evoked by the verb “address”. fig:framenet shows an example of such annotation.
> 
> We extracted sample sentences for every lexical unit in the database and identified the corresponding core frame elements. Annotated elements in FrameNet may be rather long, so we considered only the sentences with frame elements of 3 tokens or less. Since each sentences is annotated only for one frame, semantic links from other frames can exist between unmarked elements. We therefore filter out all the sentences longer than 12 tokens, since shorter sentences are less likely to evoke multiple frames.
> 
> To establish whether BERT attention captures semantic relations that do not simply correspond to the previous/following token, we exclude sentences where the linked objects are less than two tokens apart. This leaves us with 473 annotated sentences.
> 
> For each of these sentences, we obtain pre-trained BERT's attention weights for each of the 144 heads. For every head, we return the maximum absolute attention weight among those token pairs that correspond to the annotated semantic link contained within a given sentence. We then average the derived scores over all the collected examples. This strategy allows us to identify the heads that prioritize the features correlated with frame-semantic relations within a sentence.

### Relevance

Label: 

## Record 0749

Paper: Revealing the Dark Secrets of BERT

### Question

> In which certain heads was attention disabled in experiments?

### Passage

> In this experiment, we investigate whether fine-tuning BERT for a given task creates self-attention patterns which emphasize specific linguistic features. In this case, certain kinds of tokens may get high attention weights from all the other tokens in the sentence, producing vertical stripes on the corresponding attention maps (fig:atttypes).
> 
> We tested this hypothesis by checking whether there are vertical stripe patterns corresponding to certain linguistically interpretable features, and to what extent such features are relevant for solving a given task. In particular, we investigated attention to nouns, verbs, pronouns, subjects, objects, and negation words, and special BERT tokens across the tasks.
> 
> For every head, we compute the sum of self-attention weights assigned to the token of interest from each input token. Since the weights depend on the number of tokens in the input sequence, this sum is normalized by sequence length. This allows us to aggregate the weights for this feature across different examples. If there are multiple tokens of the same type (e.g. several nouns or negations), we take the maximum value. We disregard input sentences that do not contain a given feature.
> 
> For each investigated feature, we calculate this aggregated attention score for each head in every layer and build a map in order to detect the heads potentially responsible for this feature. We then compare the obtained maps to the ones derived using the pre-trained BERT model. This comparison enables us to determine if a particular feature is important for a specific task and whether it contributes to some tasks more than to others.

### Relevance

Label: 

## Record 0750

Paper: Revealing the Dark Secrets of BERT

### Question

> In which certain heads was attention disabled in experiments?

### Passage

> Since there does seem to be a certain degree of specialization for different heads, we investigated the effects of disabling different heads in BERT and the resulting effects on task performance. Since BERT relies heavily on the learned attention weights, we define disabling a head as modifying the attention values of a head to be constant $a = \frac{1}{L}$ for every token in the input sentence, where $L$ is the length of the sentence. Thus, every token receives the same attention, effectively disabling the learned attention patterns while maintaining the information flow of the original model. Note that by using this framework, we can disable an arbitrary number of heads, ranging from a single head per model to the whole layer or multiple layers.

### Relevance

Label: 

## Record 0751

Paper: Multimodal Differential Network for Visual Question Generation

### Question

> How do the authors define a differential network?

### Passage

> engaging question for an image. BIBREF35 proposed a method for continuously generating questions from an image and subsequently answering those questions. The works closely related to ours are that of BIBREF5 and BIBREF36 . In the former work, the authors used an encoder-decoder based framework whereas in the latter work, the authors extend it by using a variational autoencoder based sequential routine to obtain natural questions by performing sampling of the latent variable.

### Relevance

Label: 

## Record 0752

Paper: Multimodal Differential Network for Visual Question Generation

### Question

> How do the authors define a differential network?

### Passage

> To understand the progress towards multimedia vision and language understanding, a visual Turing test was proposed by BIBREF0 that was aimed at visual question answering BIBREF1 . Visual Dialog BIBREF2 is a natural extension for VQA. Current dialog systems as evaluated in BIBREF3 show that when trained between bots, AI-AI dialog systems show improvement, but that does not translate to actual improvement for Human-AI dialog. This is because, the questions generated by bots are not natural (human-like) and therefore does not translate to improved human dialog. Therefore it is imperative that improvement in the quality of questions will enable dialog agents to perform well in human interactions. Further, BIBREF4 show that unanswered questions can be used for improving VQA, Image captioning and Object Classification.
> 
> An interesting line of work in this respect is the work of BIBREF5 . Here the authors have proposed the challenging task of generating natural questions for an image. One aspect that is central to a question is the context that is relevant to generate it. However, this context changes for every image. As can be seen in Figure FIGREF1 , an image with a person on a skateboard would result in questions related to the event. Whereas for a little girl, the questions could be related to age rather than the action. How can one have widely varying context provided for generating questions? To solve this problem, we use the context obtained by considering exemplars, specifically we use the difference between relevant and irrelevant exemplars. We consider different contexts in the form of Location, Caption, and Part of Speech tags.
> 
> The human annotated questions are (b) for the first image and (a) for the second image.
> 
> Our method implicitly uses a differential context obtained through supporting and contrasting exemplars to obtain a differentiable embedding. This embedding is used by a question decoder to decode the appropriate question. As discussed further, we observe this implicit differential context to perform better than an explicit keyword based context. The difference between the two approaches is illustrated in Figure FIGREF2 . This also allows for better optimization as we can backpropagate through the whole network. We provide detailed empirical evidence to support our hypothesis.

### Relevance

Label: 

## Record 0753

Paper: Multimodal Differential Network for Visual Question Generation

### Question

> How do the authors define a differential network?

### Passage

> using standard practice followed in the literature BIBREF38 . This method selects the argmax sentence. Also, we evaluated our method by sampling from the probability distributions and provide the results for our proposed MDN-Joint method for VQG dataset as follows: How are exemplars improving Embedding In Multimodel differential network, we use exemplars and train them using a triplet loss. It is known that using a triplet network, we can learn a representation that accentuates how the image is closer to a supporting exemplar as against the opposing exemplar BIBREF42 , BIBREF41 . The Joint embedding is obtained between the image and language representations. Therefore the improved representation helps in obtaining an improved context vector. Further we show that this also results in improving VQG. Are exemplars required? We had similar concerns and validated this point by using random exemplars for the nearest neighbor for MDN. (k=R in table TABREF35 ) In this case the method is similar to the baseline. This suggests that with random exemplar, the model learns to ignore the cue. Are captions necessary for our method? This is not actually necessary. In our method, we have used an existing image captioning method BIBREF13 to generate captions for images that did not have them. For VQG dataset, captions were available and we have used that, but, for VQA dataset captions were not available and we have generated captions while training. We provide detailed evidence with respect to caption-question pairs to ensure that we are generating novel questions. While the caption generates scene description, our proposed method generates semantically meaningful and novel questions. Examples for Figure 1 of main paper: First Image:- Caption- A young man skateboarding around little cones. Our Question- Is this a skateboard competition? Second Image:- Caption- A small child is standing on a pair of skis. Our Question:- How old is that little girl? Intuition behind Triplet Network: The intuition behind use of triplet networks is clear through this paper BIBREF41 that first advocated its use. The main idea is that when we learn distance functions that are “close” for similar and “far” from dissimilar representations, it is not clear that close and far are with respect to what measure.

### Relevance

Label: 

## Record 0754

Paper: Multimodal Differential Network for Visual Question Generation

### Question

> How do the authors define a differential network?

### Passage

> words i.e 3 nouns, 3 verbs and 3 Wh-words, the Concatenation model performs the best. In this table the conv model is using 1D convolution to combine the tags and the joint model combine all the tags. Analysis of Context: Exemplars In Multimodel Differential Network and Differential Image Network, we use exemplar images(target, supporting and opposing image) to obtain the differential context. We have performed the experiment based on the single exemplar(K=1), which is one supporting and one opposing image along with target image, based on two exemplar(K=2), i.e. two supporting and two opposing image along with single target image. similarly we have performed experiment for K=3 and K=4 as shown in table- TABREF35 . Mixture Module: Other Variations Hadamard method uses element-wise multiplication whereas Addition method uses element-wise addition in place of the concatenation operator of the Joint method. The Hadamard method finds a correlation between image feature and caption feature vector while the Addition method learns a resultant vector. In the attention method, the output INLINEFORM35 is the weighted average of attention probability vector INLINEFORM36 and convolutional features INLINEFORM37 . The attention probability vector weights the contribution of each convolutional feature based on the caption vector. This attention method is similar to work stack attention method BIBREF54 . The attention mechanism is given by: DISPLAYFORM0 where INLINEFORM38 is the 14x14x512-dimensional convolution feature map from the fifth convolution layer of VGG-19 Net of image INLINEFORM39 and INLINEFORM40 is the caption context vector. The attention probability vector INLINEFORM41 is a 196-dimensional vector. INLINEFORM42 are the weights and INLINEFORM43 is the bias for different layers. We evaluate the different approaches and provide results for the same. Here INLINEFORM44 represents element-wise addition. Evaluation Metrics Our task is similar to encoder -decoder framework of machine translation. we have used same evaluation metric is used in machine translation. BLEU BIBREF46 is the first metric to find the correlation between generated question with ground truth question. BLEU score is used to measure the precision value, i.e That is how much words in the predicted question is appeared in reference question. BLEU-n score measures the n-gram precision for counting co-occurrence on reference sentences. we have evaluated BLEU score from n is

### Relevance

Label: 

## Record 0755

Paper: Multimodal Differential Network for Visual Question Generation

### Question

> How do the authors define a differential network?

### Passage

> a function INLINEFORM28 where INLINEFORM29 are the weights of the CNN. This is illustrated in figure FIGREF43 . Tag net The tag net consists of two parts Context Extractor & Tag Embedding Net. This is illustrated in figure FIGREF45 . Extract Context: The first step is to extract the caption of the image using NeuralTalk2 BIBREF53 model. We find the part-of-speech(POS) tag present in the caption. POS taggers have been developed for two well known corpuses, the Brown Corpus and the Penn Treebanks. For our work, we are using the Brown Corpus tags. The tags are clustered into three category namely Noun tag, Verb tag and Question tags (What, Where, ...). Noun tag consists of all the noun & pronouns present in the caption sentence and similarly, verb tag consists of verb & adverbs present in the caption sentence. The question tags consists of the 7-well know question words i.e., why, how, what, when, where, who and which. Each tag token is represented as a one-hot vector of the dimension of vocabulary size. For generalization, we have considered 5 tokens from each category of the Tags. Tag Embedding Net: The embedding network consists of word embedding followed by temporal convolutions neural network followed by max-pooling network. In the first step, sparse high dimensional one-hot vector is transformed to dense low dimension vector using word embedding. After this, we apply temporal convolution on the word embedding vector. The uni-gram, bi-gram and tri-gram feature are computed by applying convolution filter of size 1, 2 and 3 respectability. Finally, we applied max-pooling on this to get a vector representation of the tags as shown figure FIGREF45 . We concatenated all the tag words followed by fully connected layer to get feature dimension of 512. We also explored joint networks based on concatenation of all the tags, on element-wise addition and element-wise multiplication of the tag vectors. However, we observed that convolution over max pooling and joint concatenation gives better performance based on CIDer score. INLINEFORM30 Where, T_CNN is Temporally Convolution Neural Network applied on word embedding vector with kernel size three. Place net Visual object and scene recognition plays a crucial role in the image. Here, places in

### Relevance

Label: 

## Record 0756

Paper: A Novel Approach for Effective Learning in Low Resourced Scenarios

### Question

> Which models/frameworks do they compare to?

### Passage

> Deep neural networks (DNNs), in particular convolutional and recurrent neural networks, with huge architectures have been proven successful in wide range of tasks including audio processing such as speech to text [1 - 4], emotion recognition [5 - 8], speech/non-speech (e.g., of non-speech include noise, music, etc.,) classification [9 - 12], etc.
> 
> Training these deep architectures require large amount of annotated data, as a result, they cannot be used in low data resource scenarios which is common in speech-based applications [13 - 15]. Apart from collecting large data corpus, annotating the data is also very difficult, and requires manual supervision and efforts. Especially, annotation of speech for tasks like emotion recognition also suffer from lack of agreement among the annotators [16]. Hence, there is a need to build reliable systems that can work in low resource scenario.
> 
> In this work, we propose a novel approach to address the task of classification in low data resource scenarios. Our approach involves simultaneously considering more than one sample (in this work, two samples are considered) to train the classifier. We call this approach as simultaneous two sample learning (s2sL). The proposed approach is also applicable to low resource data suffering with data imbalance. The contributions of this paper are:

### Relevance

Label: 

## Record 0757

Paper: A Novel Approach for Effective Learning in Low Resourced Scenarios

### Question

> Which models/frameworks do they compare to?

### Passage

> MLP, the most commonly used feed forward neural network, is considered as the base classifier to validate our proposed s2s framework. Generally, MLPs are trained using the data format given by eq. INLINEFORM0 . But to train the MLP on our s2s based data representation (as in eq. INLINEFORM1 ), the following modifications are made to the MLP architecture (refer to Figure FIGREF4 ).
> 
> We have INLINEFORM0 units (instead of INLINEFORM1 units) in the input layer to accept the two samples i.e., INLINEFORM2 and INLINEFORM3 , simultaneously.
> 
> The structure of the hidden layer in this approach is similar to that of a regular MLP. The number of hidden layers and hidden units can be varied depending upon the complexity of the problem. The number of units in the hidden layer is selected empirically by varying the number of hidden units from 2 to twice the length of the input layer (i.e., 2 to INLINEFORM0 ) and the unit at which the highest performance is obtained are selected. In this paper, we considered only a single hidden layer. Rectified linear units (ReLU) are used for hidden layer.
> 
> The output layer will consist of units equal to twice the considered number of classes in the classification task i.e, the output layer will have four units for two-class classification task. The sigmoid activation function (not softmax) is used on the output layer units. Unlike regular MLP, we use sigmoid activation units in the output layer, with binary cross-entropy as the cost function, because the output labels in the proposed s2s based data representation will have more than one unit active at a time (not one-hot encoded output) and this condition cannot be handled using softmax function.
> 
> As can be seen from Figure FIGREF4 , the output layer in our proposed method has outputs INLINEFORM0 and INLINEFORM1 which corresponds to the outputs associated with the input feature vectors INLINEFORM2 and INLINEFORM3 , respectively. For a two-class classification problem, there will be four units in the output layer and the possible output labels are INLINEFORM4 , INLINEFORM5 , INLINEFORM6 , INLINEFORM7 corresponding to the class labels INLINEFORM8 and INLINEFORM9 , respectively. This architecture is referred to as s2s-MLP. In s2sL,

### Relevance

Label: 

## Record 0758

Paper: A Novel Approach for Effective Learning in Low Resourced Scenarios

### Question

> Which models/frameworks do they compare to?

### Passage

> Generally, the feature vector corresponding to the test sample is provided as input to the trained MLP in the testing phase and the class label is decided based on the obtained output.
> 
> However, in s2sL method, the feature vector corresponding to the test sample should also be converted to the s2s data representation format to test the trained s2s-MLP. We propose a testing approach, where the given test sample is combined with a set of preselected reference samples, whose class label is known a priori, to generate multiple instances of the same test sample as follows. DISPLAYFORM0
> 
> where INLINEFORM0 , INLINEFORM1 refer to the INLINEFORM2 -dimensional feature vector corresponding to the test sample and the INLINEFORM3 reference sample, respectively. INLINEFORM4 refers to the considered number of reference samples. These reference samples can be selected from any of the two classes.
> 
> For testing the s2s-MLP (as shown in Figure FIGREF4 ), each test sample INLINEFORM0 (same as ' INLINEFORM1 ' in (3)) is combined with all the INLINEFORM2 reference samples ( INLINEFORM3 ) to form INLINEFORM4 different instances of the same test sample INLINEFORM5 . The corresponding outputs ( INLINEFORM6 ) obtained from s2s-MLP for the INLINEFORM7 generated instances of INLINEFORM8 are combined by voting-based decision approach to obtain the final decision INLINEFORM9 . The class label that gets maximum votes is considered as the predicted output label.

### Relevance

Label: 

## Record 0759

Paper: A Novel Approach for Effective Learning in Low Resourced Scenarios

### Question

> Which models/frameworks do they compare to?

### Passage

> Consider a two-class classification task with INLINEFORM0 denoting the set of class labels, and let INLINEFORM1 and INLINEFORM2 be the number of samples corresponding to INLINEFORM3 and INLINEFORM4 , respectively. In general, to train a classifier, the samples in the train set are provided as input-output pairs as follows. DISPLAYFORM0
> 
> where INLINEFORM0 refers to the INLINEFORM1 -dimensional feature vector representing the INLINEFORM2 sample corresponding to INLINEFORM3 class label, and INLINEFORM4 , refers to output label of INLINEFORM5 class. In the proposed data representation format, called simultaneous two sample (s2s) representation, we will simultaneously consider two samples as follows. DISPLAYFORM0
> 
> where INLINEFORM0 , INLINEFORM1 are the INLINEFORM2 -dimensional feature vectors representing the INLINEFORM3 sample in INLINEFORM4 class and INLINEFORM5 sample in the INLINEFORM6 class, respectively; and INLINEFORM7 , INLINEFORM8 refers to the output labels of INLINEFORM9 and INLINEFORM10 class, respectively.
> 
> Hence, in s2s data representation, we will have an input feature vector of length INLINEFORM0 i.e., INLINEFORM1 , and output class labels as either INLINEFORM2 or INLINEFORM3 . Each sample can be combined with all the samples (i.e., with ( INLINEFORM4 ) samples) in the dataset. Therefore, by representing the data in the s2s format, the number of samples in the train set increases to INLINEFORM5 from INLINEFORM6 samples. We hypothesize that the s2s format is expected to help the network not only to learn the characteristics of the two classes separately, but also the difference and similarity in characteristics of the two classes.

### Relevance

Label: 

## Record 0760

Paper: A Novel Approach for Effective Learning in Low Resourced Scenarios

### Question

> Which models/frameworks do they compare to?

### Passage

> In this paper, we introduced a novel s2s framework to effectively learn the class discriminative characteristics, even from low data resources. In this framework, more than one sample (here, two samples) are simultaneously considered to train the classifier. Further, this framework allows to generate multiple instances of the same test sample, by considering preselected reference samples, to achieve a more profound decision making. We illustrated the significance of our approach by providing the experimental results for two different tasks namely, speech/music discrimination and emotion classification. Further, we showed that the s2s framework can also handle the low resourced data imbalance problem.

### Relevance

Label: 

## Record 0761

Paper: Unfolding and Shrinking Neural Machine Translation Ensembles

### Question

> What dataset is used?

### Passage

> The individual NMT systems we use as source for constructing the unfolded networks are trained using AdaDelta BIBREF21 on the Blocks/Theano implementation BIBREF22 , BIBREF23 of the standard attention-based NMT model BIBREF19 with: 1000 dimensional GRU layers BIBREF18 in both the decoder and bidrectional encoder; a single maxout output layer BIBREF24 ; and 620 dimensional embedding layers. We follow Sennrich et al. nmt-bpe and use subword units based on byte pair encoding rather than words as modelling units. Our SGNMT decoder BIBREF25 with a beam size of 12 is used in all experiments. Our primary corpus is the Japanese-English (Ja-En) ASPEC data set BIBREF26 . We select a subset of 500K sentence pairs to train our models as suggested by Neubig et al. sys-neubig-wat15. We report cased BLEU scores calculated with Moses' multi-bleu.pl to be strictly comparable to the evaluation done in the Workshop of Asian Translation (WAT). We also apply our method to the WMT data set for English-German (En-De), using the news-test2014 as a development set, and keeping news-test2015 and news-test2016 as test sets. En-De BLEU scores are computed using mteval-v13a.pl as in the WMT evaluation. We set the vocabulary sizes to 30K for Ja-En and 50K for En-De. We also report the size factor for each model which is the total number of model parameters (sum of all weight matrix sizes) divided by the number of parameters in the original NMT network (86M for Ja-En and 120M for En-De). We choose a widely used, simple ensembling method (prediction averaging) as our baseline. We feel that the prevalence of this method makes it a reasonable baseline for our experiments.

### Relevance

Label: 

## Record 0762

Paper: Unfolding and Shrinking Neural Machine Translation Ensembles

### Question

> What dataset is used?

### Passage

> After constructing the weight matrices of the unfolded network we reduce the size of it by iteratively shrinking layer sizes. In this section we denote the incoming weight matrix of the layer to shrink as INLINEFORM0 and the outgoing weight matrix as INLINEFORM1 . Our procedure is inspired by the method of Srinivas and Babu sparsify-datafree. They propose a criterion for removing neurons in inner layers of the network based on two intuitions. First, similarly to Hebb's learning rule, they detect redundancy by the principle neurons which fire together, wire together. If the incoming weight vectors INLINEFORM2 and INLINEFORM3 are exactly the same for two neurons INLINEFORM4 and INLINEFORM5 , we can remove the neuron INLINEFORM6 and add its outgoing connections to neuron INLINEFORM7 ( INLINEFORM8 ) without changing the output. This holds since the activity in neuron INLINEFORM14 will always be equal to the activity in neuron INLINEFORM15 . In practice, Srinivas and Babu use a distance measure based on the difference of the incoming weight vectors to search for similar neurons as exact matches are very rare.
> 
> The second intuition of the criterion used by Srinivas and Babu sparsify-datafree is that neurons with small outgoing weights contribute very little overall. Therefore, they search for a pair of neurons INLINEFORM0 according the following term and remove the INLINEFORM1 -th neuron. DISPLAYFORM0
> 
> Neuron INLINEFORM0 is selected for removal if (1) there is another neuron INLINEFORM1 which has a very similar set of incoming weights and if (2) INLINEFORM2 has a small outgoing weight vector. Their criterion is data-free since it does not require any training data. For further details we refer to Srinivas and Babu sparsify-datafree.

### Relevance

Label: 

## Record 0763

Paper: Unfolding and Shrinking Neural Machine Translation Ensembles

### Question

> What dataset is used?

### Passage

> The first concept of our approach is called unfolding. Unfolding is an alternative to ensembling of multiple neural networks with the same topology. Rather than averaging their predictions, unfolding constructs a single large neural net out of the individual models which has the same number of input and output neurons but larger inner layers. Our main motivation for unfolding is to obtain a single network with ensemble level performance which can be shrunk with the techniques in Sec. SECREF3 .
> 
> Suppose we ensemble two single layer feedforward neural nets as shown in Fig. FIGREF1 . Normally, ensembling is implemented by performing an isolated forward pass through the first network (Fig. SECREF2 ), another isolated forward pass through the second network (Fig. SECREF3 ), and averaging the activities in the output layers of both networks. This can be simulated by merging both networks into a single large network as shown in Fig. SECREF4 . The first neurons in the hidden layer of the combined network correspond to the hidden layer in the first single network, and the others to the hidden layer of the second network. A single pass through the combined network yields the same output as the ensemble if the output layer is linear (up to a factor 2). The weight matrices in the unfolded network can be constructed by stacking the corresponding weight matrices (either horizontally or vertically) in network 1 and 2. This kind of aggregation of multiple networks with the same topology is not only possible for single-layer feedforward architectures but also for complex networks consisting of multiple GRU layers and attention.
> 
> For a formal description of unfolding we address layers with indices INLINEFORM0 . The special layer 0 has a single neuron for modelling bias vectors. Layer 1 holds the input neurons and layer INLINEFORM1 is the output layer. We denote the size of a layer in the individual models as INLINEFORM2 . When combining INLINEFORM3 networks, the layer size INLINEFORM4 in the unfolded network is increased by factor INLINEFORM5 if INLINEFORM6 is an inner layer, and equal to INLINEFORM7 if INLINEFORM8 is the input or output layer. We denote the weight matrix between two layers INLINEFORM9 in the INLINEFORM10

### Relevance

Label: 

## Record 0764

Paper: Unfolding and Shrinking Neural Machine Translation Ensembles

### Question

> What dataset is used?

### Passage

> Data-free and data-bound shrinking can be interpreted as setting the expected difference between network outputs before and after a removal operation to zero under different assumptions.
> 
> For simplicity, we focus our probabilistic treatment of shrinking on single layer feedforward networks. Such a network maps an input INLINEFORM0 to an output INLINEFORM1 . The INLINEFORM2 -th output INLINEFORM3 is computed according the following equation DISPLAYFORM0
> 
> where INLINEFORM0 is the incoming weight vector of the INLINEFORM1 -th hidden neuron (denoted as INLINEFORM2 in the main paper) and INLINEFORM3 the outgoing weight matrix of the INLINEFORM4 -dimensional hidden layer. We now remove the INLINEFORM5 -th neuron in the hidden layer and modify the outgoing weights to compensate for the removal: DISPLAYFORM0
> 
> where INLINEFORM0 is the output after the removal operation and INLINEFORM1 are the modified outgoing weights. Our goal is to choose INLINEFORM2 such that the expected error introduced by removing neuron INLINEFORM3 is zero: DISPLAYFORM0

### Relevance

Label: 

## Record 0765

Paper: Unfolding and Shrinking Neural Machine Translation Ensembles

### Question

> What dataset is used?

### Passage

> INLINEFORM4 in the unfolded network is increased by factor INLINEFORM5 if INLINEFORM6 is an inner layer, and equal to INLINEFORM7 if INLINEFORM8 is the input or output layer. We denote the weight matrix between two layers INLINEFORM9 in the INLINEFORM10 -th individual model ( INLINEFORM11 ) as INLINEFORM12 , and the corresponding weight matrix in the unfolded network as INLINEFORM13 . We explicitly allow INLINEFORM14 and INLINEFORM15 to be non-consecutive or reversed to be able to model recurrent networks. We use the zero-matrix if layers INLINEFORM16 and INLINEFORM17 are not connected. The construction of the unfolded weight matrix INLINEFORM18 from the individual matrices INLINEFORM19 depends on whether the connected layers are inner layers or not. The complete formula is listed in Fig. FIGREF5 .
> 
> Unfolded NMT networks approximate but do not exactly match the output of the ensemble due to two reasons. First, the unfolded network synchronizes the attentions of the individual models. Each decoding step in the unfolded network computes a single attention weight vector. In contrast, ensemble decoding would compute one attention weight vector for each of the INLINEFORM0 input models. A second difference is that the ensemble decoder first applies the softmax at the output layer, and then averages the prediction probabilities. The unfolded network averages the neuron activities (i.e. the logits) first, and then applies the softmax function. Interestingly, as shown in Sec. SECREF4 , these differences do not have any impact on the BLEU score but yield potential speed advantages of unfolding since the computationally expensive softmax layer is only applied once.

### Relevance

Label: 

## Record 0766

Paper: Generating Personalized Recipes from Historical User Preferences

### Question

> What are the baseline models?

### Passage

> For training and evaluation, we provide our model with the first 3-5 ingredients listed in each recipe. We decode recipe text via top-$k$ sampling BIBREF7, finding $k=3$ to produce satisfactory results. We use a hidden size $d_h=256$ for both the encoder and decoder. Embedding dimensions for vocabulary, ingredient, recipe, techniques, and caloric level are 300, 10, 50, 50, and 5 (respectively). For prior recipe attention, we set $k=20$, the 80th %-ile for the number of user interactions. We use the Adam optimizer BIBREF28 with a learning rate of $10^{-3}$, annealed with a decay rate of 0.9 BIBREF29. We also use teacher-forcing BIBREF30 in all training epochs.
> 
> In this work, we investigate how leveraging historical user preferences can improve generation quality over strong baselines in our setting. We compare our personalized models against two baselines. The first is a name-based Nearest-Neighbor model (NN). We initially adapted the Neural Checklist Model of BIBREF0 as a baseline; however, we ultimately use a simple Encoder-Decoder baseline with ingredient attention (Enc-Dec), which provides comparable performance and lower complexity. All personalized models outperform baseline in BPE perplexity (tab:metricsontest) with Prior Name performing the best. While our models exhibit comparable performance to baseline in BLEU-1/4 and ROUGE-L, we generate more diverse (Distinct-1/2: percentage of distinct unigrams and bigrams) and acceptable recipes. BLEU and ROUGE are not the most appropriate metrics for generation quality. A `correct' recipe can be written in many ways with the same main entities (ingredients). As BLEU-1/4 capture structural information via n-gram matching, they are not correlated with subjective recipe quality. This mirrors observations from BIBREF31, BIBREF8.
> 
> We observe that personalized models make more diverse recipes than baseline. They thus perform better in BLEU-1 with more key entities (ingredient mentions) present, but worse in BLEU-4, as these recipes are written in a personalized way and deviate from gold on the phrasal level. Similarly, the `Prior Name' model generates more unigram-diverse recipes than other personalized models and obtains a correspondingly lower BLEU-1 score.
> 
> Qualitative Analysis: We present sample outputs for a cocktail recipe in tab:samplerecipes, and additional recipes in the appendix. Generation quality progressively improves from generic baseline output to a blended cocktail produced by our best performing model. Models

### Relevance

Label: 

## Record 0767

Paper: Generating Personalized Recipes from Historical User Preferences

### Question

> What are the baseline models?

### Passage

> to the difference between the former and latter. A higher score indicates better step ordering (with a maximum score of 2). tab:coherencemetrics shows that our personalized models achieve average recipe-level coherence scores of 1.78-1.82, surpassing the baseline at 1.77.
> 
> Recipe Step Entailment: Local coherence is also crucial to a user following a recipe: it is crucial that subsequent steps are logically consistent with prior ones. We model local coherence as an entailment task: predicting the likelihood that a recipe step follows the preceding. We sample several consecutive (positive) and non-consecutive (negative) pairs of steps from each recipe. We train a BERT BIBREF34 model to predict the entailment score of a pair of steps separated by a [SEP] token, using the final representation of the [CLS] token. The step entailment score is computed as the average of scores for each set of consecutive steps in each recipe, averaged over every generated recipe for a model, as shown in tab:coherencemetrics.
> 
> Human Evaluation: We presented 310 pairs of recipes for pairwise comparison BIBREF8 (details in appendix) between baseline and each personalized model, with results shown in tab:metricsontest. On average, human evaluators preferred personalized model outputs to baseline 63% of the time, confirming that personalized attention improves the semantic plausibility of generated recipes. We also performed a small-scale human coherence survey over 90 recipes, in which 60% of users found recipes generated by personalized models to be more coherent and preferable to those generated by baseline models.

### Relevance

Label: 

## Record 0768

Paper: Generating Personalized Recipes from Historical User Preferences

### Question

> What are the baseline models?

### Passage

> lower BLEU-1 score.
> 
> Qualitative Analysis: We present sample outputs for a cocktail recipe in tab:samplerecipes, and additional recipes in the appendix. Generation quality progressively improves from generic baseline output to a blended cocktail produced by our best performing model. Models attending over prior recipes explicitly reference ingredients. The Prior Name model further suggests the addition of lemon and mint, which are reasonably associated with previously consumed recipes like coconut mousse and pork skewers.
> 
> Personalization: To measure personalization, we evaluate how closely the generated text corresponds to a particular user profile. We compute the likelihood of generated recipes using identical input specifications but conditioned on ten different user profiles—one `gold' user who consumed the original recipe, and nine randomly generated user profiles. Following BIBREF8, we expect the highest likelihood for the recipe conditioned on the gold user. We measure user matching accuracy (UMA)—the proportion where the gold user is ranked highest—and Mean Reciprocal Rank (MRR) BIBREF32 of the gold user. All personalized models beat baselines in both metrics, showing our models personalize generated recipes to the given user profiles. The Prior Name model achieves the best UMA and MRR by a large margin, revealing that prior recipe names are strong signals for personalization. Moreover, the addition of attention mechanisms to capture these signals improves language modeling performance over a strong non-personalized baseline.
> 
> Recipe Level Coherence: A plausible recipe should possess a coherent step order, and we evaluate this via a metric for recipe-level coherence. We use the neural scoring model from BIBREF33 to measure recipe-level coherence for each generated recipe. Each recipe step is encoded by BERT BIBREF34. Our scoring model is a GRU network that learns the overall recipe step ordering structure by minimizing the cosine similarity of recipe step hidden representations presented in the correct and reverse orders. Once pretrained, our scorer calculates the similarity of a generated recipe to the forward and backwards ordering of its corresponding gold label, giving a score equal to the difference between the former and latter. A higher score indicates better step ordering (with a maximum score of 2). tab:coherencemetrics shows that our personalized models achieve average recipe-level coherence scores of 1.78-1.82, surpassing the baseline at 1.77.
> 
> Recipe

### Relevance

Label: 

## Record 0769

Paper: Generating Personalized Recipes from Historical User Preferences

### Question

> What are the baseline models?

### Passage

> We prepared a set of 15 pairwise comparisons per evaluation session, and collected 930 pairwise evaluations (310 per personalized model) over 62 sessions. For each pair, users were given a partial recipe specification (name and 3-5 key ingredients), as well as two generated recipes labeled `A' and `B'. One recipe is generated from our baseline encoder-decoder model and one recipe is generated by one of our three personalized models (Prior Tech, Prior Name, Prior Recipe). The order of recipe presentation (A/B) is randomly selected for each question. A screenshot of the user evaluation interface is given in fig:exeval. We ask the user to indicate which recipe they find more coherent, and which recipe best accomplishes the goal indicated by the recipe name. A screenshot of this survey interface is given in fig:exeval2.

### Relevance

Label: 

## Record 0770

Paper: Generating Personalized Recipes from Historical User Preferences

### Question

> What are the baseline models?

### Passage

> In the kitchen, we increasingly rely on instructions from cooking websites: recipes. A cook with a predilection for Asian cuisine may wish to prepare chicken curry, but may not know all necessary ingredients apart from a few basics. These users with limited knowledge cannot rely on existing recipe generation approaches that focus on creating coherent recipes given all ingredients and a recipe name BIBREF0. Such models do not address issues of personal preference (e.g. culinary tastes, garnish choices) and incomplete recipe details. We propose to approach both problems via personalized generation of plausible, user-specific recipes using user preferences extracted from previously consumed recipes.
> 
> Our work combines two important tasks from natural language processing and recommender systems: data-to-text generation BIBREF1 and personalized recommendation BIBREF2. Our model takes as user input the name of a specific dish, a few key ingredients, and a calorie level. We pass these loose input specifications to an encoder-decoder framework and attend on user profiles—learned latent representations of recipes previously consumed by a user—to generate a recipe personalized to the user's tastes. We fuse these `user-aware' representations with decoder output in an attention fusion layer to jointly determine text generation. Quantitative (perplexity, user-ranking) and qualitative analysis on user-aware model outputs confirm that personalization indeed assists in generating plausible recipes from incomplete ingredients.
> 
> While personalized text generation has seen success in conveying user writing styles in the product review BIBREF3, BIBREF4 and dialogue BIBREF5 spaces, we are the first to consider it for the problem of recipe generation, where output quality is heavily dependent on the content of the instructions—such as ingredients and cooking techniques.
> 
> To summarize, our main contributions are as follows:
> 
> We explore a new task of generating plausible and personalized recipes from incomplete input specifications by leveraging historical user preferences;
> 
> We release a new dataset of 180K+ recipes and 700K+ user reviews for this task;
> 
> We introduce new evaluation strategies for generation quality in instructional texts, centering on quantitative measures of coherence. We also show qualitatively and quantitatively that personalized models generate high-quality and specific recipes that align with historical user preferences.

### Relevance

Label: 

## Record 0771

Paper: Automatic Target Recovery for Hindi-English Code Mixed Puns

### Question

> What are the categories of code-mixed puns?

### Passage

> We focus on the task of automatically disambiguating or recovering Hindi-English code mixed puns. For this purpose, it is first necessary to understand what these puns are.

### Relevance

Label: 

## Record 0772

Paper: Automatic Target Recovery for Hindi-English Code Mixed Puns

### Question

> What are the categories of code-mixed puns?

### Passage

> For the purposes of this research, we only consider puns where the ambiguity or the wordplay lies in the code-switching i.e, the pun word and its target are from different languages. For example the pun "Rivers can't hear because woh behri hoti hai." is a sentence with the pun being behri (meaning deaf) and its target being beh rahi (meaning flowing). Here, while the sentence is code-mixed, the pun word and the target both belong to the same language. We do not consider such puns for the present study.
> 
> We analyze the structure of code-mixed puns with the pun word and its target belonging to different languages and propose two broad categories to classify them in - puns where the code-mixing is intra-sentential and the other where it is intra-word. Both these categories are explained below, while we evaluate only on the former category.
> 
> Intra-sentential code-mixing is where code-switching occurs within a sentence. Here, the language varies at the word level. Also, each word of the sentence belongs to one or the other language. Table 1 gives examples of puns belonging to this category.
> 
> In this category, code mixing is present within a word. New words are formed using Portmanteau or Blending where two or more syllables/phonemes from different languages are blended together to form a single word, resulting in a word which is phonetically similar to the target word. Table 2 illustrates examples of intra-word code-mixed puns.

### Relevance

Label: 

## Record 0773

Paper: Automatic Target Recovery for Hindi-English Code Mixed Puns

### Question

> What are the categories of code-mixed puns?

### Passage

> Most puns we hear or use in everyday conversations are rarely recorded. One of the most common resources to find recorded puns are advertisements, for example the highly creative and frequently released Amul advertisements in India BIBREF1 . Most of these are contextually integrated BIBREF0 with an image. While such puns may lose their humour out of context, it is still possible to recover their targets, so using these does not affect our task in any way
> 
> To create a dataset to test our model on, we collected 518 advertisements released by Amul in the years 2014, 2015, 2017 and 2018, from their official web page. Of these, 333 were puns, including 121 code-mixed puns as defined in Section 3.1. We extracted the text of these 121 code-mixed puns and asked 3 people to disambiguate them, given just the advertisement text. All three annotators were university students in 22-23 years age group, native Hindi speakers with bilingual fluency in English. The annotators were asked to identify the location of the pun in each of the advertisements and write down the target of the pun. Any disagreements between annotators were resolved by mutual discussion.
> 
> In a few cases where puns were identified to have multiple targets, we kept all such possibilities in our dataset. A few puns were identified to be non-recoverable because of the lack of contextual knowledge, while a few puns had multiple pun locations. We removed both these types from our dataset, which left us with 110 puns.
> 
> Finally, we divided these 110 annotated puns into the two categories as defined in Section 3.1 thereby getting 51 advertisements categorized as intra-sentential code-mixed puns, and the rest as intra-word code-mixed puns. We use the former as our test data.

### Relevance

Label: 

## Record 0774

Paper: Automatic Target Recovery for Hindi-English Code Mixed Puns

### Question

> What are the categories of code-mixed puns?

### Passage

> Humour is one of the most complex and intriguing phenomenon of the human language. It exists in various forms, across space and time, in literature and culture, and is a valued part of human interactions. Puns are one of the simplest and most common forms of humour in the English language. They are also one of the most widespread forms of spontaneous humour BIBREF0 and have found their place in casual conversations, literature, online comments, tweets and advertisements BIBREF1 , BIBREF2 . Puns are a hugely versatile and commonly used literary device and it is essential to include them in any comprehensive approach to computational humour.
> 
> In this paper, we consider Hindi-English code-mixed puns and aim to automatically recover their targets. The target of a pun is its phonologically similar counterpart, the relationship to which and whose resolution (recovery) in the mind of the listener/hearer induces humour. For example, in the pun “The life of a patient of hypertension is always at steak." the word “steak" is the pun with target “stake".
> 
> With India being a diverse linguistic region, there is an ever increasing usage of code-mixed Hindi-English language (along with various others) because bilingualism and even multilingualism are quite common. Consequently, we have also seen an increase in the usage of code-mixed language in online forums, advertisements etc. Code-mixed humour, especially puns have become increasingly popular because being able to use the same punning techniques but with two languages in play has opened up numerous avenues for new and interesting wordplays. With the increasing popularity and acceptance for the usage of code-mixed language, it has become important that computers are also able to process it and even decipher complex phenomena like humour. Traditional Word Sense Disambiguation (WSD) based methods cannot be used in target recovery of code-mixed puns, because they are no longer about multiple senses of a single word but about two words from two different languages. Code-switching comes with no markers, and the punning word may not even be a word in either of the languages being used. Sometimes words from the two languages can be combined to form a word which only a bilingual speaker would understand. Hence, this task on

### Relevance

Label: 

## Record 0775

Paper: Automatic Target Recovery for Hindi-English Code Mixed Puns

### Question

> What are the categories of code-mixed puns?

### Passage

> To conclude, in this paper, we present a first-ever work on target recovery code-mixed puns. We study various puns where the word-play is a result of code-switching, and classify them into 2 categories - puns with intra-sentential code mixing and those with intra-word code mixing. We then propose a methodology to recover the targets for puns belonging to the former category, using only monolingual language data. We test our proposed approach on a small manually annotated dataset, and we see that our system was able to successfully recover 67% of the puns from the set.
> 
> In the future, we want to perform a more comprehensive evaluation of this approach on a larger, more diverse set of puns. We want to improve and extend our approach to be able to recover intra-word code-mixed puns along with the intra-sentential ones that it handles right now. After that, the system should be extended to be able to recover all kinds of puns in code-mixed language, regardless of whether the pun itself is monolingual or code-mixed.

### Relevance

Label: 

## Record 0776

Paper: Open-Vocabulary Semantic Parsing with both Distributional Statistics and Formal Knowledge

### Question

> How big is their dataset?

### Passage

> Much recent work on semantic parsing has been evaluated using the WebQuestions dataset BIBREF3 . This dataset is not suitable for evaluating our model because it was filtered to only questions that are mappable to Freebase queries. In contrast, our focus is on language that is not directly mappable to Freebase. We thus use the dataset introduced by Krishnamurthy and Mitchell krishnamurthy-2015-semparse-open-vocabulary, which consists of the ClueWeb09 web corpus along with Google's FACC entity linking of that corpus to Freebase BIBREF9 . For training data, 3 million webpages from this corpus were processed with a CCG parser to produce logical forms BIBREF10 . This produced 2.1m predicate instances involving 142k entity pairs and 184k entities. After removing infrequently-seen predicates (seen fewer than 6 times), there were 25k categories and 4.2k relations.
> 
> We also used the test set created by Krishnamurthy and Mitchell, which contains 220 queries generated in the same fashion as the training data from a separate section of ClueWeb. However, as they did not release a development set with their data, we used this set as a development set. For a final evaluation, we generated another, similar test set from a different held out section of ClueWeb, in the same fashion as done by Krishnamurthy and Mitchell. This final test set contains 307 queries.

### Relevance

Label: 

## Record 0777

Paper: Open-Vocabulary Semantic Parsing with both Distributional Statistics and Formal Knowledge

### Question

> How big is their dataset?

### Passage

> We compare three models in our experiments: (1) the distributional model of Krishnamurthy and Mitchell, described in Section "Subgraph feature extraction" , which is the current state-of-the-art method for open vocabulary semantic parsing; (2) a formal model (new to this work), where the distributional parameters $\theta $ and $\phi $ in Section "Combined predicate models" are fixed at zero; and (3) the combined model described in Section "Combined predicate models" (also new to this work). In each of these models, we used vectors of size 300 for all embeddings. Except where noted, all experiments use our modified logical forms (Section "Evaluation" ) and our entity proposal mechanism (Section "Related work" ). We do not compare against any traditional semantic parsers, as more than half of the questions in our dataset are not answerable by Freebase queries, and so are out of scope for those parsers BIBREF5 .

### Relevance

Label: 

## Record 0778

Paper: Open-Vocabulary Semantic Parsing with both Distributional Statistics and Formal Knowledge

### Question

> How big is their dataset?

### Passage

> In this section, we briefly describe the current state-of-the-art model for open vocabulary semantic parsing, introduced by Krishnamurthy and Mitchell krishnamurthy-2015-semparse-open-vocabulary. Instead of mapping text to Freebase queries, as done by a traditional semantic parser, their method parses text to a surface logical form with predicates derived directly from the words in the text (see Figure 1 ). Next, a distribution over denotations for each predicate is learned using a matrix factorization approach similar to that of Riedel et al. riedel-2013-mf-universal-schema. This distribution is concisely represented using a probabilistic database, which also enables efficient probabilistic execution of logical form queries.
> 
> The matrix factorization has two sets of parameters: each category or relation has a learned $k$ -dimensional embedding $\theta $ , and each entity or entity pair has a learned $k$ -dimensional embedding $\phi $ . The probability assigned to a category instance $c(e)$ or relation instance $r(e_1, e_2)$ is given by: $ p(c(e)) &= \sigma ( \theta _c^T \phi _e ) \\ p(r(e_1, e_2)) &= \sigma (
> \theta _r^T \phi _{(e_1, e_2)} ) $
> 
> The probability of a predicate instance is the sigmoided inner product of the corresponding predicate and entity embeddings. Predicates with nearby embeddings will have similar distributions over the entities in their denotation. The parameters $\theta $ and $\phi $ are learned using a query ranking objective that optimizes them to rank entities observed in the denotation of a logical form above unobserved entities. Given the trained predicate and entity parameters, the system is capable of efficiently computing the marginal probability that an entity is an element of a logical form's denotation using approximate inference algorithms for probabilistic databases.
> 
> The model presented in this section is purely distributional, with predicate and entity models that draw only on co-occurrence information found in a corpus. In the following sections, we show how to augment this model with information contained in large, curated KBs such as Freebase.

### Relevance

Label: 

## Record 0779

Paper: Open-Vocabulary Semantic Parsing with both Distributional Statistics and Formal Knowledge

### Question

> How big is their dataset?

### Passage

> Semantic parsing is the task of mapping a phrase in natural language onto a formal query in some fixed schema, which can then be executed against a knowledge base (KB) BIBREF0 , BIBREF1 . For example, the phrase “Who is the president of the United States?” might be mapped onto the query $\lambda (x).$ $\textsc {/government/president\_of}$ ( $x$ , $\textsc {USA}$ ), which, when executed against Freebase BIBREF2 , returns $\textsc {Barack Obama}$ . By mapping phrases to executable statements, semantic parsers can leverage large, curated sources of knowledge to answer questions BIBREF3 .
> 
> This benefit comes with an inherent limitation, however—semantic parsers can only produce executable statements within their manually-produced schema. There is no query against Freebase that can answer questions like “Who are the Democratic front-runners in the US election?”, as Freebase does not encode information about front-runners. Semantic parsers trained for Freebase fail on these kinds of questions.
> 
> To overcome this limitation, recent work has proposed methods for open vocabulary semantic parsing, which replace a formal KB with a probabilistic database learned from a text corpus. In these methods, language is mapped onto queries with predicates derived directly from the text itself BIBREF4 , BIBREF5 . For instance, the question above might be mapped to $\lambda (x).$ $\textit {president\_of}$ ( $x$ , $\textsc {USA}$ ). This query is not executable against any KB, however, and so open vocabulary semantic parsers must learn execution models for the predicates found in the text. They do this with a distributional approach similar to word embedding methods, giving them broad coverage, but lacking access to the large, curated KBs available to traditional semantic parsers.
> 
> Prior work in semantic parsing, then, has either had direct access to the information in a knowledge base, or broad coverage over all of natural language using the information in a large corpus, but not both.
> 
> In this work, we show how to combine these two approaches by incorporating KB information into open vocabulary semantic parsing models. Our key insight is that formal KB queries can be converted into features that can be added to the learned execution models of open vocabulary semantic parsers. This conversion allows open vocabulary models to use

### Relevance

Label: 

## Record 0780

Paper: Open-Vocabulary Semantic Parsing with both Distributional Statistics and Formal Knowledge

### Question

> How big is their dataset?

### Passage

> Here we present our approach to incorporating KB information into open vocabulary semantic parsers. Having described how we use SFE to generate features corresponding to statements in a formal schema, adding these features to the models described in Section "Subgraph feature extraction" is straightforward.
> 
> We saw in Section "Subgraph feature extraction" that open vocabulary semantic parsers learn distributional vectors for each category, relation, entity and entity pair. We augment these vectors with the feature vectors described in Section "Converting Freebase queries to features" . Each category and relation receives a weight $\omega $ for each selected Freebase query, and each entity and entity pair has an associated feature vector $\psi $ . The truth probability of a category instance $c(e)$ or relation instance $r(e_1, e_2)$ is thus given by: $
> p(c(e)) &= \sigma ( \theta _c^T \phi _e + \omega _c^T \psi _c(e)) \\
> p(r(e_1, e_2)) &= \sigma ( \theta _r^T \phi _{(e_1, e_2)} + \omega _r^T \psi _r(e_1, e_2) )
> $
> 
> In these equations, $\theta $ and $\phi $ are learned predicate and entity embeddings, as described in Section "Subgraph feature extraction" . The second term in the sum represents our new features and their learned weights. $\psi _c(e)$ and $\psi _r(e_1, e_2)$ are SFE feature vectors for each entity and entity pair; a different set of features is chosen for each predicate $c$ and $r$ , as described in Section "Making full use of KB information" . $\omega _c$ and $\omega _r$ are learned weights for these features.
> 
> In our model, there are now three sets of parameters to be learned: (1) $\theta $ , low-dimensional distributional vectors trained for each predicate; (2) $\phi $ , low-dimensional distributional vectors trained for each entity and entity pair; and (3) $\omega $ , weights associated with the selected formal SFE features for each predicate. All of these parameters are optimized jointly, using the same method described in Section "Subgraph feature extraction" .
> 
> Note here that each SFE feature corresponds to a query over the formal schema, defining a set of entities (or entity pairs). The associated feature weight measures the likelihood that an entity in this set is also in the denotation of the surface

### Relevance

Label: 

## Record 0781

Paper: Prose for a Painting

### Question

> What limitations do the authors demnostrate of their model?

### Passage

> Since we do not have an end-to-end dataset, the generated English poem may not work well with Shakespeare style transfer as shown in Figure FIGREF12 for "Starry Night" with a low average content score. This happens when the style transfer dataset does not have similar words in the training set of sentences. A solution would be to expand the style transfer dataset, for a better representation of the poem data.

### Relevance

Label: 

## Record 0782

Paper: Prose for a Painting

### Question

> What limitations do the authors demnostrate of their model?

### Passage

> We use a total three datasets: two datasets for generating an English poem from an image, and Shakespeare plays and their English translations for text style transfer.
> 
> We train a model for generating poems from images based on two datasets BIBREF1. The first dataset consists of image and poem pairs, namely a multi-modal poem dataset (MultiM-Poem), and the second dataset is a large poem corpus, namely a uni-modal poem dataset (UniM-Poem). The image and poem pairs are extended by adding the nearest three neighbor poems from the poem corpus without redundancy, and an extended image and poem pair dataset is constructed and denoted as MultiM-Poem(Ex)BIBREF1.
> 
> We use a collection of line-by-line modern paraphrases for 16 of Shakespeare’s plays BIBREF2, for training a style transfer network from English poems to Shakespearean prose. We use 18,395 sentences from the training data split. We keep 1,218 sentences in the validation data set and 1,462 sentences in our test set.

### Relevance

Label: 

## Record 0783

Paper: Prose for a Painting

### Question

> What limitations do the authors demnostrate of their model?

### Passage

> We perform a qualitative analysis of the Shakespearean prose generated for the input paintings. We conducted a survey, in which we presented famous paintings including those shown in Figures FIGREF1 and FIGREF10 and the corresponding Shakespearean prose generated by the model, and asked 32 students to rate them on the basis of content, creativity and similarity to Shakespearean style on a Likert scale of 1-5. Figure FIGREF12 shows the result of our human evaluation.
> 
> The average content score across the paintings is 3.7 which demonstrates that the prose generated is relevant to the painting. The average creativity score is 3.9 which demonstrates that the model captures more than basic objects in the painting successfully using poetic clues in the scene. The average style score is 3.9 which demonstrates that the prose generated is perceived to be in the style of Shakespeare.
> 
> We also perform a quantitative analysis of style transfer by generating BLEU scores for the model output using the style transfer dataset. The variation of the BLEU scores with the source sentence lengths is shown in Figure FIGREF11. As expected, the BLEU scores decrease with increase in source sentence lengths.

### Relevance

Label: 

## Record 0784

Paper: Prose for a Painting

### Question

> What limitations do the authors demnostrate of their model?

### Passage

> We use a sequence-to-sequence model which consists of a single layer unidrectional LSTM encoder and a single layer LSTM decoder and pre-trained retrofitted word embeddings shared between source and target sentences. We experimented with two different types of attention: global attention BIBREF9, in which the model makes use of the output from the encoder and decoder for the current time step only, and Bahdanau attention BIBREF10, where computing attention requires the output of the decoder from the prior time step. We found that global attention performs better in practice for our task of text style transfer.

### Relevance

Label: 

## Record 0785

Paper: Prose for a Painting

### Question

> What limitations do the authors demnostrate of their model?

### Passage

> For generating a poem from images we use an existing actor-critic architecture BIBREF1. This involves 3 parallel CNNs: an object CNN, sentiment CNN, and scene CNN, for feature extraction. These features are combined with a skip-thought model which provides poetic clues, which are then fed into a sequence-to-sequence model trained by policy gradient with 2 discriminator networks for rewards. This as a whole forms a pipeline that takes in an image and outputs a poem as shown on the top left of Figure FIGREF4. A CNN-RNN generative model acts as an agent. The parameters of this agent define a policy whose execution determines which word is selected as an action. When the agent selects all words in a poem, it receives a reward. Two discriminative networks, shown on the top right of Figure FIGREF4, are defined to serve as rewards concerning whether the generated poem properly describes the input image and whether the generated poem is poetic. The goal of the poem generation model is to generate a sequence of words as a poem for an image to maximize the expected return.

### Relevance

Label: 

## Record 0786

Paper: Medication Regimen Extraction From Clinical Conversations

### Question

> What is the baseline?

### Passage

> We consider QA PGNet and Multi-decoder QA PGNet with lookup table embedding as baseline models and improve on the baselines with other variations described below.
> 
> Apart from learning-based baselines, we also create two naive baselines, one each for the Dosage and Frequency extraction tasks. For Dosage extraction, the baseline we consider is `Nearest Number', where we take the number nearest to the Medication Name as the prediction, and `none' if no number is mentioned or if the Medication Name is not detected in the input. For Frequency extraction, the baseline we consider is `Random Top-3' where we predict a random Frequency tag, from top-3 most frequent ones from our dataset - {`none', `daily', `twice a day'}.
> 
> Embedding: We developed different variations of our models with a simple lookup table embeddings learned from scratch and using high-performance contextual embeddings, which are ELMo BIBREF11, BERT BIBREF16 and ClinicalBERT BIBREF13 (trained and provided by the authors). Refer to Table TABREF5 for the performance comparisons.
> 
> We derive embeddings from ELMo by learning a linear combination of its last three layer's hidden states (task-specific fine-tuning BIBREF11). Similarly, for BERT-based embeddings, we take a linear combination of the hidden states from its last four layers, as this combination performs best without increasing the size of the embeddings BIBREF16. Since BERT and ClinicalBERT use word-piece vocabulary and computes sub-word embeddings, we compute word-level embedding by averaging the corresponding sub-word tokens. ELMo and BERT embeddings both have 1024 dimensions, ClinicalBERT have 768 as it is based on BERT base model, and the lookup table have 128 – higher dimension models leads to overfitting.
> 
> Pertaining Encoder: We trained the PGNet as a summarization task using the clinical summaries and used the trained model to initialize the encoders (and the embeddings) of the corresponding QA models. We use a vocab size of 4073 words, derived from the training dataset with a frequency threshold of 30 for the task. We trained the models using Adagrad optimizer with a learning rate of 0.015, normal gradient clipping set at 2 and trained for around 150000 iterations (stopped using validation dataset). On the summarization task PGNet obtained ROUGE-1 F1 scores of 41.42 with ELMo and 39.15 with BERT embeddings.

### Relevance

Label: 

## Record 0787

Paper: Medication Regimen Extraction From Clinical Conversations

### Question

> What is the baseline?

### Passage

> We frame the Medication Regimen extraction problem as a Question Answering (QA) task, which forms the basis for our first approach. It can also be considered as a specific inference or relation extract task, since we extract specific information about an entity (Medication Name), hence our second approach is at the intersection of Question Answering (QA) and Information Extraction (IE) domains. Both the approaches involve using a contiguous segment of the transcript and the Medication Name as input, to find/infer the medication's Dosage and Frequency. When testing the approaches mimicking real-world conditions, we extract Medication Name from the transcript separately using ontology, refer to SECREF19.
> 
> In the first approach, we frame the MR task as a QA task and generate questions using the template: “What is the $ <$dosage/frequency$>$ for $<$Medication Name$>$". Here, we use an abstractive QA model based on pointer-generator networks BIBREF9 augmented with coattention encoder BIBREF10 (QA-PGNet).
> 
> In the second approach, we frame the problem as a conditioned IE task, where the information extracted depends on an entity (Medication Name). Here, we use a multi-decoder pointer-generator network augmented with coattention encoder (Multi-decoder QA-PGNet). Instead of using templates to generate questions and using a single decoder to extract different types of information as in the QA approach (which might lead to performance degradation), here we consider separate decoders for extracting specific types of information about an entity $E$ (Medication Name).

### Relevance

Label: 

## Record 0788

Paper: Medication Regimen Extraction From Clinical Conversations

### Question

> What is the baseline?

### Passage

> To appear in Proceedings of International Workshop on Health Intelligence (W3PHIAI) of the 34th AAAI Conference on Artificial Intelligence, 2020.
> 
> Physician burnout is a growing concern, estimated to be experienced by at least 35% of physicians in the developing world and 50% in the United States BIBREF0. BIBREF1 found that for every hour physicians provide direct clinical facetime to patients, nearly two additional hours are spent on EHR (Electronic Health Records) and administrative or desk work. As per the study conducted by Massachusetts General Physicians Organization (MPGO) BIBREF2 and as reported by BIBREF3, the average time spent on administrative tasks increased from 23.7% in 2014 to 27.9% in 2017. Both the surveys found that time spent on administrative tasks was positively associated with higher likelihood of burnout. Top reasons under administrative burden include working on the ambulatory EHR, handling medication reconciliation (sometimes done by aids), medication renewals, and medical billing and coding. The majority of these reasons revolve around documentation of information exchanged between doctors and patients during the clinical encounters. Automatically extracting such clinical information BIBREF4, BIBREF5 can not only help alleviate the documentation burden on the physician, but also allow them to dedicate more time directly with patients.
> 
> Among all the clinical information extraction tasks, Medication Regimen (Medication, dosage, and frequency) extraction is particularly interesting due to its ability to help doctors with medication orders cum renewals, medication reconciliation, potentially verifying the reconciliations for errors, and, other medication-centered EHR documentation tasks. In addition, the same information when provided to patients can help them with better recall of doctor instructions which might aid in compliance with the care plan. This is particularly important given that patients forget or wrongly recollect 40-80% BIBREF6 of what is discussed in the clinic, and accessing EHR data has its own challenges.
> 
> Spontaneous clinical conversations happening between a doctor and a patient, have several distinguishing characteristics from a normal monologue or prepared speech: it involves multiple speakers with overlapping dialogues, covers a variety of speech patterns, and the vocabulary can range from colloquial to complex domain-specific language. With recent advancements in Conversational Speech Recognition BIBREF7 rendering the systems less prone to errors, the subsequent challenge of understanding and extracting

### Relevance

Label: 

## Record 0789

Paper: Medication Regimen Extraction From Clinical Conversations

### Question

> What is the baseline?

### Passage

> the effects of training data size on our models.
> 
> On the MR extraction task, ELMo with encoder multi-decoder architecture and BERT with encoder-decoder with encoders pretrained on the summarization task perform the best. The best-performing models improve our baseline's dosage and frequency extractions ROUGE-1 F1 scores from 54.28 and 37.13 to 89.57 and 45.94, respectively.
> 
> Using our models, we present the first fully automated system to extract MR tags from spontaneous doctor-patient conversations. We evaluate the system (using our best performing models) on the transcripts generated from Automatic Speech Recognition (ASR) APIs offered by Google and IBM. In Google ASR's transcripts, our best model obtained ROUGE-1 F1 of 71.75 for Dosage extraction (which in this specific case equals to the percentage of times dosage is correct, refer Metrics Section for more details) and 40.13 for Frequency extraction tasks. On qualitative evaluation, we find that for 73.58% of the medications the model can find the correct frequency. These results demonstrate that the research on NLP can be used effectively in a real clinical setting to benefit both doctors and patients

### Relevance

Label: 

## Record 0790

Paper: Medication Regimen Extraction From Clinical Conversations

### Question

> What is the baseline?

### Passage

> dialogues, covers a variety of speech patterns, and the vocabulary can range from colloquial to complex domain-specific language. With recent advancements in Conversational Speech Recognition BIBREF7 rendering the systems less prone to errors, the subsequent challenge of understanding and extracting relevant information from the conversations is receiving increasing research focus BIBREF4, BIBREF8.
> 
> In this paper, we focus on local information extraction in transcribed clinical conversations. Specifically, we extract dosage (e.g. 5mg) and frequency (e.g. once a day) for the medications (e.g. aspirin) from these transcripts, collectively referred to as Medication Regimen (MR) extraction. The information extraction is local as we extract the information from a segment of the transcript and not the entire transcript since doing the latter is difficult owing to the long meandering nature of the conversations often with multiple medication regimens and care plans being discussed.
> 
> The challenges associated with the Medication Regimen (MR) extraction task include understanding the spontaneous dialog with clinical vocabulary and understanding the relationship between different entities as the discussion can contain multiple medications and dosages (e.g. doctor revising a dosage or reviewing all the current medications).
> 
> We frame this problem as a Question Answering (QA) task by generating questions using templates. We base the QA model on pointer-generator networks BIBREF9 augmented with Co-Attentions BIBREF10. In addition, we develop models combining QA and Information Extraction frameworks using multi-decoder (one each for dosage and frequency) architecture.
> 
> Lack of availability of a large volume of data is a typical challenge in healthcare. A conversation corpus by itself is a rare commodity in the healthcare data space because of the cost and difficulty in handing (because of data privacy concerns). Moreover, transcribing and labeling the conversations is a costly process as it requires domain-specific medical annotation expertise. To address data shortage and improve the model performance, we investigate different high-performance contextual embeddings (ELMO BIBREF11, BERT BIBREF12 and ClinicalBERT BIBREF13), and pretrain the models on a clinical summarization task. We further investigate the effects of training data size on our models.
> 
> On the MR extraction task, ELMo with encoder multi-decoder architecture and BERT with encoder-decoder with encoders pretrained on the summarization task perform the best. The best-performing models improve our baseline's dosage

### Relevance

Label: 

## Record 0791

Paper: Predictive Embeddings for Hate Speech Detection on Twitter

### Question

> how much was the parameter difference between their model and previous methods?

### Passage

> The approach we have developed establishes a new state of the art for classifying hate speech, outperforming previous results by as much as 12 F1 points. Table TABREF10 illustrates the robustness of our method, which often outperform previous results, measured by weighted F1.
> 
> Using the Approximate Randomization (AR) Test BIBREF14 , we perform significance testing using a 75/25 train and test split
> 
> to compare against BIBREF3 and BIBREF4 , whose models we re-implemented. We found 0.001 significance compared to both methods. We also include in-depth precision and recall results for all three datasets in the supplement.
> 
> Our results indicate better performance than several more complex approaches, including BIBREF4 's best model (which used word and part-of-speech ngrams, sentiment, readability, text, and Twitter specific features), BIBREF6 (which used two fold classification and a hybrid of word and character CNNs, using approximately twice the parameters we use excluding the word embeddings) and even recent work by BIBREF8 , (whose best model relies on GRUs, metadata including popularity, network reciprocity, and subscribed lists).
> 
> On the SR dataset, we outperform BIBREF8 's text based model by 3 F1 points, while just falling short of the Text + Metadata Interleaved Training model. While we appreciate the potential added value of metadata, we believe a tweet-only classifier has merits because retrieving features from the social graph is not always tractable in production settings. Excluding the embedding weights, our model requires 100k parameters , while BIBREF8 requires 250k parameters.

### Relevance

Label: 

## Record 0792

Paper: Predictive Embeddings for Hate Speech Detection on Twitter

### Question

> how much was the parameter difference between their model and previous methods?

### Passage

> We tokenize the data using Spacy BIBREF10 . We use 300 Dimensional Glove Common Crawl Embeddings (840B Token) BIBREF11 and fine tune them for the task. We experimented extensively with pre-processing variants and our results showed better performance without lemmatization and lower-casing (see supplement for details). We pad each input to 50 words. We train using RMSprop with a learning rate of .001 and a batch size of 512. We add dropout with a drop rate of 0.1 in the final layer to reduce overfitting BIBREF12 , batch size, and input length empirically through random hyperparameter search.
> 
> All of our results are produced from 10-fold cross validation to allow comparison with previous results. We trained a logistic regression baseline model (line 1 in Table TABREF10 ) using character ngrams and word unigrams using TF*IDF weighting BIBREF13 , to provide a baseline since HAR has no reported results. For the SR and HATE datasets, the authors reported their trained best logistic regression model's results on their respective datasets.
> 
> SR: Sexist/Racist BIBREF3 , HATE: Hate BIBREF4 HAR: Harassment BIBREF9

### Relevance

Label: 

## Record 0793

Paper: Predictive Embeddings for Hate Speech Detection on Twitter

### Question

> how much was the parameter difference between their model and previous methods?

### Passage

> Since our method was a simple word embedding based model, we explored the learned embedding space to analyze results. For this analysis, we only use the max pooling part of our architecture to help analyze the learned embedding space because it encourages salient words to increase their values to be selected. We projected the original pre-trained embeddings to the learned space using the time distributed MLP. We summed the embedding dimensions for each word and sorted by the sum in descending order to find the 1000 most salient word embeddings from our vocabulary. We then ran PCA BIBREF16 to reduce the dimensionality of the projected embeddings from 300 dimensions to 75 dimensions. This captured about 60% of the variance. Finally, we ran K means clustering for INLINEFORM0 clusters to organize the most salient embeddings in the projected space.
> 
> The learned clusters from the SR vocabulary were very illuminating (see Table TABREF14 ); they gave insights to how hate speech surfaced in the datasets. One clear grouping we found is the misogynistic and pornographic group, which contained words like breasts, blonds, and skank. Two other clusters had references to geopolitical and religious issues in the Middle East and disparaging and resentful epithets that could be seen as having an intellectual tone. This hints towards the subtle pedagogic forms of hate speech that surface. We ran silhouette analysis BIBREF17 on the learned clusters to find that the clusters from the learned representations had a 35% higher silhouette coefficient using the projected embeddings compared to the clusters created from the original pre-trained embeddings. This reinforces the claim that our training process pushed hate-speech related words together, and words from other clusters further away, thus, structuring the embedding space effectively for detecting hate speech.

### Relevance

Label: 

## Record 0794

Paper: Predictive Embeddings for Hate Speech Detection on Twitter

### Question

> how much was the parameter difference between their model and previous methods?

### Passage

> In this paper, we use three data sets from the literature to train and evaluate our own classifier. Although all address the category of hateful speech, they used different strategies of labeling the collected data. Table TABREF5 shows the characteristics of the datasets.
> 
> Data collected by BIBREF3 , which we term the Sexist/Racist (SR) data set, was collected using an initial Twitter search followed by analysis and filtering by the authors and their team who identified 17 common phrases, hashtags, and users that were indicative of abusive speech. BIBREF4 collected the HATE dataset by searching for tweets using a lexicon provided by Hatebase.org. The final data set we used, which we call HAR, was collected by BIBREF9 ; we removed all retweets reducing the dataset to 20,000 tweets. Tweets were labeled as “Harrassing” or “Non-Harrassing”; hate speech was not explicitly labeled, but treated as an unlabeled subset of the broader “Harrassing” category BIBREF9 .

### Relevance

Label: 

## Record 0795

Paper: Predictive Embeddings for Hate Speech Detection on Twitter

### Question

> how much was the parameter difference between their model and previous methods?

### Passage

> False negatives
> 
> Many of the false negatives we see are specific references to characters in the TV show “My Kitchen Rules”, rather than something about women in general. Such examples may be innocuous in isolation but could potentially be sexist or racist in context. While this may be a limitation of considering only the content of the tweet, it could also be a mislabel.
> 
> Debra are now my most hated team on #mkr after least night's ep. Snakes in the grass those two.
> 
> Along these lines, we also see correct predictions of innocuous speech, but find data mislabeled as hate speech:
> 
> @LoveAndLonging ...how is that example "sexism"?
> 
> @amberhasalamb ...in what way?
> 
> Another case our classifier misses is problematic speech within a hashtag:
> 
> :D @nkrause11 Dudes who go to culinary school: #why #findawife #notsexist :)
> 
> This limitation could be potentially improved through the use of character convolutions or subword tokenization.
> 
> False Positives
> 
> In certain cases, our model seems to be learning user names instead of semantic content:
> 
> RT @GrantLeeStone: @MT8_9 I don't even know what that is, or where it's from. Was that supposed to be funny? It wasn't.
> 
> Since the bulk of our model's weights are in the embedding and embedding-transformation matrices, we cluster the SR vocabulary using these transformed embeddings to clarify our intuitions about the model ( TABREF14 ). We elaborate on our clustering approach in the supplement. We see that the model learned general semantic groupings of words associated with hate speech as well as specific idiosyncrasies related to the dataset itself (e.g. katieandnikki)

### Relevance

Label: 

## Record 0796

Paper: Automatic Detection of Cyberbullying in Social Media Text

### Question

> What are their baselines?

### Passage

> As mentioned earlier, although research on cyberbullying detection is more limited than social studies on the phenomenon, some important advances have been made in recent years. In what follows, we present a brief overview of the most important natural language processing approaches to cyberbullying detection.
> 
> Although some studies have investigated the effectiveness of rule-based modelling BIBREF31 , the dominant approach to cyberbullying detection involves machine learning. Most machine learning approaches are based on supervised BIBREF32 , BIBREF33 , BIBREF34 or semi-supervised learning BIBREF35 . The former involves the construction of a classifier based on labeled training data, whereas semi-supervised approaches rely on classifiers that are built from a training corpus containing a small set of labeled and a large set of unlabelled instances (a method that is often used to handle data sparsity). As cyberbullying detection essentially involves the distinction between bullying and non-bullying posts, the problem is generally approached as a binary classification task where the positive class is represented by instances containing (textual) cyberbullying, while the negative class includes instances containing non-cyberbullying or `innocent' text.
> 
> A key challenge in cyberbullying research is the availability of suitable data, which is necessary to develop models that characterise cyberbullying. In recent years, only a few datasets have become publicly available for this particular task, such as the training sets provided in the context of the CAW 2.0 workshop and more recently, the Twitter Bullying Traces dataset BIBREF36 . As a result, several studies have worked with the former or have constructed their own corpus from social media websites that are prone to bullying content, such as YouTube BIBREF32 , BIBREF33 , Formspring BIBREF33 , and ASKfm BIBREF37 (the latter two are social networking sites where users can send each other questions or respond to them). Despite the bottleneck of data availability, existing approaches to cyberbullying detection have shown its potential, and the relevance of automatic text analysis techniques to ensure child safety online has been recognised BIBREF38 , BIBREF39 .
> 
> Among the first studies on cyberbullying detection are BIBREF34 , BIBREF31 , BIBREF33 , who explored the predictive power of INLINEFORM0 -grams (with and without tf-idf weighting), part-of-speech information (e.g. first and second pronouns), and sentiment

### Relevance

Label: 

## Record 0797

Paper: Automatic Detection of Cyberbullying in Social Media Text

### Question

> What are their baselines?

### Passage

> characteristics of the Web: once defamatory or confidential information about a person is made public through the Internet, it is hard, if not impossible, to remove.
> 
> Finally, while arguing that repetition is a criterion to distinguish cyberbullying from single acts of aggression, BIBREF23 himself states that such a single aggressive action can be considered bullying under certain circumstances, although it is not entirely clear what these circumstances involve. Accordingly, BIBREF27 claim that repetition in cyberbullying is problematic to operationalise, as it is unclear what the consequences are of a single derogatory message on a public page. A single act of aggression or humiliation may result in continued distress and humiliation for the victim if it is shared or liked by multiple perpetrators or read by a large audience. BIBREF29 compare this with a `snowball effect': one post may be repeated or distributed by other people so that it becomes out of the control of the initial bully and has larger effects than was originally intended.
> 
> Given these arguments, a number of less `strict' definitions of cyberbullying were postulated by among others BIBREF6 , BIBREF5 , BIBREF1 , where a power imbalance and repetition are not deemed necessary conditions for cyberbullying.
> 
> The above paragraphs demonstrate that defining cyberbullying is far from trivial, and varying prevalence rates (cf. Section SECREF1 ) confirm that a univocal definition of the phenomenon is still lacking in the literature BIBREF1 . Based on existing conceptualisations, we define cyberbullying as content that is published online by an individual and that is aggressive or hurtful against a victim. Based on this definition, an annotation scheme was developed (see BIBREF30 ) to signal textual characteristics of cyberbullying, including posts from bullies, as well as reactions by victims and bystanders.

### Relevance

Label: 

## Record 0798

Paper: Automatic Detection of Cyberbullying in Social Media Text

### Question

> What are their baselines?

### Passage

> Cyberbullying has been a widely covered research topic recently and studies have shed light on direct and indirect types of cyberbullying, implicit and explicit forms, verbal and non-verbal cyberbullying, and so on. This is important from a sociolinguistic point of view, but knowing what cyberbullying involves is also crucial to build models for automatic cyberbullying detection. In the following paragraphs, we present our data annotation guidelines BIBREF30 and focus on different types and roles related to the phenomenon.

### Relevance

Label: 

## Record 0799

Paper: Automatic Detection of Cyberbullying in Social Media Text

### Question

> What are their baselines?

### Passage

> and subjectivity lexicons prove to be strong features for this task. In effect, adding character INLINEFORM2 -grams always improved classification performance for both languages. They likely provide robustness to lexical variation in social media text, as compared to word INLINEFORM3 -grams. While subjectivity lexicons appear to be discriminative features, term lists perform badly on their own as well as in combinations for both languages. This shows once again (cf. profanity baseline) that cyberbullying detection requires more sophisticated information sources than profanity lists. Topic models seem to do badly for both languages on their own, but in combination, they improve Dutch performance consistently. A possible explanation for their varying performance in both languages would be that the topic models trained on the Dutch background corpus are of better quality than the English ones. In effect, a random selection of background corpus texts reveals that the English scrape contains more noisy data (i.e., low word-count posts and non-English posts) than the Dutch data.
> 
> A shallow qualitative analysis of the classification output provided insight into some of the classification mistakes.
> 
> Table TABREF52 gives an overview of the error rates per cyberbullying category of the best performing and baseline systems. This could give an indication of which types of bullying the current system has trouble classifying. All categories are always considered positive for cyberbullying (i.e., the error rate equals the false negative rate), except for Sexual and Insult which can also be negative (in case of harmless sexual talk and `socially acceptable' insulting language like `hi bitches, in for a movie?' the corresponding category was indicated, but the post itself was not annotated as cyberbullying) and Not cyberbullying, which is always negative. Error rates often being lowest for the profanity baseline confirms that it performs particularly well in terms of recall (at the expense of precision, see Table TABREF47 ) When looking at the best system for both languages, we see that Defense is the hardest category to correctly classify. This should not be a surprise as the category comprises defensive posts from bystanders and victims, which contain less aggressive language than cyberbullying attacks and are often shorter in length than the latter. Assertive defensive posts (i.e., a subcategory

### Relevance

Label: 

## Record 0800

Paper: Automatic Detection of Cyberbullying in Social Media Text

### Question

> What are their baselines?

### Passage

> In this section, we present the results of our experiments on the automatic detection of cyberbullying-related posts in an English (EN) and Dutch (NL) corpus of ASKfm posts. Ten-fold cross-validation was performed in exhaustive grid-search over different feature type and hyperparameter combinations (see Section SECREF4 ). The unoptimised word INLINEFORM0 -gram-based classifier and keyword-matching system serve as baselines for comparison. Precision, Recall and F INLINEFORM1 performance metrics were calculated on the positive class (i.e., `binary averaging'). We also report Area Under the ROC curve (AUC) scores, a performance metric that is more robust to data imbalance than precision, recall and micro-averaged F-score BIBREF74 .
> 
> Table TABREF45 gives us an indication of which feature type combinations score best and hence contribute most to this task. A total of 31 feature type combinations, each with 28 different hyperparameter sets have been tested. Table TABREF45 shows the results for the three best scoring systems by included feature types with optimised hyperparameters. The maximum attained F INLINEFORM0 -score in cross-validation is 64.26% for English and 61.20% for Dutch and shows that the classifier benefits from a variety of feature types. The results on the holdout test set show that the trained systems generalise well on unseen data, indicating little under- or overfitting. The simple keyword-matching baseline system has the lowest performance for both languages even though it obtains high recall for English, suggesting that profane language characterises many cyberbullying-related posts. Feature group and hyperparameter optimisation provides a considerable performance increase over the unoptimised word INLINEFORM1 -gram baseline system. The top-scoring systems for each language do not differ a lot in performance, except the best system for Dutch, which trades recall for precision when compared to the runner-ups.
> 
> Table TABREF47 presents the scores of the (hyperparameter-optimised) single feature type systems, to gain insight into the performance of these feature types when used individually. Analysis of the combined and single feature type sets reveals that word INLINEFORM0 -grams, character INLINEFORM1 -grams, and subjectivity lexicons prove to be strong features for this task. In effect, adding character INLINEFORM2 -grams always improved classification performance for both languages. They likely provide robustness to lexical variation in social media text, as compared to word INLINEFORM3

### Relevance

Label: 
