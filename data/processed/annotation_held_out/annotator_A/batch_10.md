# Passage relevance annotation

Annotator: 

Judge whether the passage provides information that helps answer the question, including useful partial evidence. Topic overlap alone is not sufficient. Judge only the supplied question and passage.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Do not change record numbers, questions or passages. Work independently without consulting another annotator or reference answers.

## Record 0901

Paper: Plain English Summarization of Contracts

### Question

> How big is the dataset?

### Passage

> this area, we have collected 446 sets of contract sections and corresponding reference summaries which can be used as a test set for such a task. We have compiled these sets from two websites dedicated to explaining complicated legal documents in plain English.
> 
> Rather than attempt to summarize an entire document, these sources summarize each document at the section level. In this way, the reader can reference the more detailed text if need be. The summaries in this dataset are reviewed for quality by the first author, who has 3 years of professional contract drafting experience.
> 
> The dataset we propose contains 446 sets of parallel text. We show the level of abstraction through the number of novel words in the reference summaries, which is significantly higher than the abstractive single-document summaries created for the shared tasks of the Document Understanding Conference (DUC) in 2002 BIBREF11 , a standard dataset used for single document news summarization. Additionally, we utilize several common readability metrics to show that there is an average of a 6 year reading level difference between the original documents and the reference summaries in our legal dataset.
> 
> In initial experimentation using this dataset, we employ popular unsupervised extractive summarization models such as TextRank BIBREF12 and Greedy KL BIBREF13 , as well as lead baselines. We show that such methods do not perform well on this dataset when compared to the same methods on DUC 2002. These results highlight the fact that this is a very challenging task. As there is not currently a dataset in this domain large enough for supervised methods, we suggest the use of methods developed for simplification and/or style transfer.
> 
> In this paper, we begin by discussing how this task relates to the current state of text summarization and similar tasks in Section SECREF2 . We then introduce the novel dataset and provide details on the level of abstraction, compression, and readability in Section SECREF3 . Next, we provide results and analysis on the performance of extractive summarization baselines on our data in Section SECREF5 . Finally, we discuss the potential for unsupervised systems in this genre in Section SECREF6 .

### Relevance

Label: 

## Record 0902

Paper: Plain English Summarization of Contracts

### Question

> How big is the dataset?

### Passage

> In this paper, we propose the task of summarizing legal documents in plain English and present an initial evaluation dataset for this task. We gather our dataset from online sources dedicated to explaining sections of contracts in plain English and manually verify the quality of the summaries. We show that our dataset is highly abstractive and that the summaries are much simpler to read. This task is challenging, as popular unsupervised extractive summarization methods do not perform well on this dataset and, as discussed in section SECREF6 , current methods that address the change in register are mostly supervised as well. We call for the development of resources for unsupervised simplification and style transfer in this domain.

### Relevance

Label: 

## Record 0903

Paper: Plain English Summarization of Contracts

### Question

> How big is the dataset?

### Passage

> To understand the level of abstraction of the proposed dataset, we first calculate the number of n-grams that appear only in the reference summaries and not in the original texts they summarize BIBREF14 , BIBREF27 . As shown in Figure FIGREF14 , 41.4% of words in the reference summaries did not appear in the original text. Additionally, 78.5%, 88.4%, and 92.3% of 2-, 3-, and 4-grams in the reference summaries did not appear in the original text. When compared to a standard abstractive news dataset also shown in the graph (DUC 2002), the legal dataset is significantly more abstractive.
> 
> Furthermore, as shown in Figure FIGREF15 , the dataset is very compressive, with a mean compression rate of 0.31 (std 0.23). The original texts have a mean of 3.6 (std 3.8) sentences per document and a mean of 105.6 (std 147.8) words per document. The reference summaries have a mean of 1.2 (std 0.6) sentences per document, and a mean of 17.2 (std 11.8) words per document.

### Relevance

Label: 

## Record 0904

Paper: Plain English Summarization of Contracts

### Question

> How big is the dataset?

### Passage

> Given a document, the goal of single document summarization is to produce a shortened summary of the document that captures its main semantic content BIBREF5 . Existing research extends over several genres, including news BIBREF11 , BIBREF14 , BIBREF15 , scientific writing BIBREF16 , BIBREF17 , BIBREF18 , legal case reports BIBREF8 , etc. A critical factor in successful summarization research is the availability of a dataset with parallel document/human-summary pairs for system evaluation. However, no such publicly available resource for summarization of contracts exists to date. We present the first dataset in this genre. Note that unlike other genres where human summaries paired with original documents can be found at scale, e.g., the CNN/DailyMail dataset BIBREF14 , resources of this kind are yet to be curated/created for contracts. As traditional supervised summarization systems require these types of large datasets, the resources released here are intended for evaluation, rather than training. Additionally, as a first step, we restrict our initial experiments to unsupervised baselines which do not require training on large datasets.
> 
> The dataset we present summarizes contracts in plain English. While there is no precise definition of plain English, the general philosophy is to make a text readily accessible for as many English speakers as possible. BIBREF19 , BIBREF20 . Guidelines for plain English often suggest a preference for words with Saxon etymologies rather than a Latin/Romance etymologies, the use of short words, sentences, and paragraphs, etc. BIBREF20 , BIBREF21 . In this respect, the proposed task involves some level of text simplification, as we will discuss in Section SECREF16 . However, existing resources for text simplification target literacy/reading levels BIBREF22 or learners of English as a second language BIBREF23 . Additionally, these models are trained using Wikipedia or news articles, which are quite different from legal documents. These systems are trained without access to sentence-aligned parallel corpora; they only require semantically similar texts BIBREF24 , BIBREF25 , BIBREF26 . To the best of our knowledge, however, there is no existing dataset to facilitate the transfer of legal language to plain English.

### Relevance

Label: 

## Record 0905

Paper: Plain English Summarization of Contracts

### Question

> How big is the dataset?

### Passage

> Our preliminary experiments and analysis show that summarizing legal contracts in plain English is challenging, and point to the potential usefulness of a simplification or style transfer system in the summarization pipeline. Yet this is challenging. First, there may be a substantial domain gap between legal documents and texts that existing simplification systems are trained on (e.g., Wikipedia, news). Second, popular supervised approaches such as treating sentence simplification as monolingual machine translation BIBREF35 , BIBREF23 , BIBREF36 , BIBREF37 , BIBREF38 would be difficult to apply due to the lack of sentence-aligned parallel corpora. Possible directions include unsupervised lexical simplification utilizing distributed representations of words BIBREF39 , BIBREF40 , unsupervised sentence simplification using rich semantic structure BIBREF41 , or unsupervised style transfer techniques BIBREF24 , BIBREF25 , BIBREF26 . However, there is not currently a dataset in this domain large enough for unsupervised methods, nor corpora unaligned but comparable in semantics across legal and plain English, which we see as a call for future research.

### Relevance

Label: 

## Record 0906

Paper: What we write about when we write about causality: Features of causal statements across large-scale social discourse

### Question

> What is the source of the "control" corpus?

### Passage

> The difference in mean sentiment score was significant (t-test: $p < 0.01$ ).
> 
> Second, we moved from the mean score to the distribution of sentiment across all (scored) unigrams in the causal and control corpora (Fig. 3 B). The causal corpus contained a large group of negative sentiment unigrams, with labMT scores in the approximate range $-3 < s < -1/2$ ; the control corpus had significantly fewer unigrams in this score range.
> 
> Third, in Fig. 3 C we used POS tags to categorize scored unigrams into nouns, verbs, and adjectives. Studying the distributions for each, we found that nouns explain much of the overall difference observed in Fig. 3 B, with verbs showing a similar but smaller difference between the two corpora. Adjectives showed little difference. The distributions in Fig. 3 C account for 87.8% of scored text in the causal corpus and 77.2% of the control corpus. The difference in sentiment between corpora was significant for all distributions (t-test: $p < 0.01$ ).
> 
> Fourth, to further confirm that the causal documents tend toward negative sentiment, we applied a separate, independent sentiment analysis using the Stanford NLP sentiment toolkit BIBREF38 to classify the sentiment of individual documents not unigrams (see Methods). Instead of a numeric sentiment score, this classifier assigns documents to one of five categories ranging from very negative to very positive. The classifier showed that the causal corpus contains more negative and very negative documents than the control corpus, while the control corpus contains more neutral, positive, and very positive documents (Fig. 3 D).
> 
> We have found language (Figs. 1 and 2 ) and sentiment (Fig. 3 ) differences between causal statements made on social media compared with other social media statements. But what is being discussed? What are the topical foci of causal statements? To study this, for our last analysis we applied topic models to the causal statements. Topic modeling finds groups of related terms (unigrams) by considering similarities between how those terms co-occur across a set of documents.
> 
> We used the popular topic modeling method Latent Dirichlet Allocation (LDA) BIBREF39 . We ranked unigrams by how strongly associated they were with the topic. Inspecting these unigrams we found that

### Relevance

Label: 

## Record 0907

Paper: What we write about when we write about causality: Features of causal statements across large-scale social discourse

### Question

> What is the source of the "control" corpus?

### Passage

> Lastly, we applied topic modeling to the causal corpus to determine what are the topical foci most discussed in causal statements. Topics were built from the causal corpus using Latent Dirichlet Allocation (LDA) BIBREF39 . Under LDA each document is modeled as a bag-of-words or unordered collection of unigrams. Topics are considered as mixtures of unigrams by estimating conditional distributions over unigrams: $P(w|T)$ , the probability of unigram $w$ given topic $T$ and documents are considered as mixtures of topics via $P(T|d)$ , the probability of topic $T$ given document $d$ . These distributions are then found via statistical inference given the observed distributions of unigrams across documents. The total number of topics is a parameter chosen by the practitioner. For this study we used the MALLET v2.0.8RC3 topic modeling toolkit BIBREF40 for model inference. By inspecting the most probable unigrams per topic (according to $P(w|T)$ ), we found 10 topics provided meaningful and distinct topics.

### Relevance

Label: 

## Record 0908

Paper: What we write about when we write about causality: Features of causal statements across large-scale social discourse

### Question

> What is the source of the "control" corpus?

### Passage

> to attribute causes and effects. Another finding is the role of a valence bias: the volume and intensity of causal reasoning may increase due to negative feedback or negative events BIBREF27 .
> 
> Despite these long lines of research, causal attributions made via social media or online social networks have not been well studied. The goal of this paper is to explore the language and topics of causal statements in a large corpus of social media taken from Twitter. We hypothesize that language and sentiment biases play a significant role in these statements, and that tools from natural language processing and computational linguistics can be used to study them. We do not attempt to study the factual correctness of these statements or offer any degree of verification, nor do we exhaustively identify and extract all causal statements from these data. Instead, here we focus on statements that are with high certainty causal statements, with the goal to better understand key characteristics about causal statements that differ from everyday online communication.
> 
> The rest of this paper is organized as follows: In Sec. "Materials and Methods" we discuss our materials and methods, including the dataset we studied, how we preprocessed that data and extracted a `causal' corpus and a corresponding `control' corpus, and the details of the statistical and language analysis tools we studied these corpora with. In Sec. "Results" we present results using these tools to compare the causal statements to control statements. We conclude with a discussion in Sec. "Discussion" .

### Relevance

Label: 

## Record 0909

Paper: What we write about when we write about causality: Features of causal statements across large-scale social discourse

### Question

> What is the source of the "control" corpus?

### Passage

> Documents were further studied by annotating their unigrams with Parts-of-Speech (POS) and Named Entities (NE) tags. POS tagging was done using NLTK v3.1 BIBREF29 which implements an averaged perceptron classifier BIBREF32 trained on the Brown Corpus BIBREF33 . (POS tagging is affected by punctuation; we show in the Appendix that our results are relatively robust to the removal of punctuation.) POS tags denote the nouns, verbs, and other grammatical constructs present in a document. Named Entity Recognition (NER) was performed using the 4-class, distributional similarity tagger provided as part of the Stanford CoreNLP v3.6.0 toolkit BIBREF34 . NER aims to identify and classify proper words in a text. The NE classifications considered were: Organization, Location, Person, and Misc. The Stanford NER tagger uses a conditional random field model BIBREF35 trained on diverse sets of manually-tagged English-language data (CoNLL-2003) BIBREF34 . Conditional random fields allow dependencies between words so that `New York' and `New York Times', for example, are classified separately as a location and organization, respectively. These taggers are commonly used and often provide reasonably accurate results, but there is always potential ambiguity in written text and improving upon these methods remains an active area of research.
> 
> Unigrams, POS, and NEs were compared between the cause and control corpora using odds ratios (ORs):
> 
> $$\operatorname{OR}(x) = \frac{p_C(x)/ (1-p_C(x))}{p_N(x) / (1-p_N(x))},$$   (Eq. 1)
> 
> where $p_C(x)$ and $p_N(x)$ are the probabilities that a unigram, POS, or NE $x$ occurs in the causal and control corpus, respectively. These probabilities were computed for each corpus separately as $p(x) = f(x) / \sum _{x^{\prime } \in V} f(x^{\prime })$ , where $f(x)$ is the total number of occurrences of $x$ in the corpus and $V$ is the relevant set of unigrams, POS, or NEs. Confidence intervals for the ORs were computed using Wald's methodology BIBREF36 .
> 
> As there are many unique unigrams in the text, when computing unigram ORs we focused on the most meaningful unigrams within each corpus by using the following filtering criteria: we considered only the $\operatorname{OR}$ s of the 1500 most frequent unigrams in that corpus that also have a term-frequency-inverse-document-frequency (tf-idf) score above the 90th percentile for that corpus BIBREF37 . The tf-idf was computed as

### Relevance

Label: 

## Record 0910

Paper: What we write about when we write about causality: Features of causal statements across large-scale social discourse

### Question

> What is the source of the "control" corpus?

### Passage

> We have collected approximately 1M causal statements made on Twitter over the course of 2013, and for a control we gathered the same number of statements selected at random but controlling for time of year (see Methods). We applied Parts-of-Speech (POS) and Named Entity (NE) taggers to all these texts. Some post-processed and tagged example documents, both causal and control, are shown in Fig. 1 A. We also applied sentiment analysis methods to these documents (Methods) and we have highlighted very positive and very negative words throughout Fig. 1 .
> 
> In Fig. 1 B we present odds ratios for how frequently unigrams (words), POS, or NE appear in causal documents relative to control documents. The three unigrams most strongly skewed towards causal documents were `stress', `problems', and `trouble', while the three most skewed towards control documents were `photo', `ready', and `cute'. While these are only a small number of the unigrams present, this does imply a negative sentiment bias among causal statements (we return to this point shortly).
> 
> Figure 1 B also presents odds ratios for POS tags, to help us measure the differences in grammatical structure between causal and control documents (see also the Appendix for the effects of punctuation and casing on these odds ratios). The causal corpus showed greater odds for plural nouns (Penn Treebank tag: NNS), plural proper nouns (NNPS), Wh-determiners/pronouns (WDT, WP$) such as `whichever',`whatever', `whose', or `whosever', and predeterminers (PDT) such as `all' or `both'. Predeterminers quantify noun phrases such as `all' in `after all the events that caused you tears', showing that many causal statements, despite the potential brevity of social media, can encompass or delineate classes of agents and/or patients. On the other hand, the causal corpus has lower odds than the control corpus for list items (LS), proper singular nouns (NNP), and interjections (UH).
> 
> Lastly, Fig. 1 B contains odds ratios for NE tags, allowing us to quantify the types of proper nouns that are more or less likely to appear in causal statements. Of the four tags, only the “Person” tag is less likely in the causal corpus than the control. (This matches the odds ratio for the proper singular noun discussed above.) Perhaps surprisingly,

### Relevance

Label: 

## Record 0911

Paper: Towards Scalable Multi-domain Conversational Agents: The Schema-Guided Dialogue Dataset

### Question

> How did they gather the data?

### Passage

> We use a single model, shared among all services and domains, to make these predictions. We first encode all the intents, slots and slot values for categorical slots present in the schema into an embedded representation. Since different schemas can have differing numbers of intents or slots, predictions are made over dynamic sets of schema elements by conditioning them on the corresponding schema embeddings. This is in contrast to existing models which make predictions over a static schema and are hence unable to share knowledge across domains and services. They are also not robust to changes in schema and require the model to be retrained with new annotated data upon addition of a new intent, slot, or in some cases, a slot value to a service.

### Relevance

Label: 

## Record 0912

Paper: Towards Scalable Multi-domain Conversational Agents: The Schema-Guided Dialogue Dataset

### Question

> How did they gather the data?

### Passage

> Virtual assistants aim to support a large number of services available on the web. One possible approach is to define a large unified schema for the assistant, to which different service providers can integrate with. However, it is difficult to come up with a common schema covering all use cases. Having a common schema also complicates integration of tail services with limited developer support. We propose the schema-guided approach as an alternative to allow easy integration of new services and APIs.
> 
> Under our proposed approach, each service provides a schema listing the supported slots and intents along with their natural language descriptions (Figure FIGREF7 shows an example). These descriptions are used to obtain a semantic representation of these schema elements. The assistant employs a single unified model containing no domain or service specific parameters to make predictions conditioned on these schema elements. For example, Figure FIGREF14 shows how dialogue state representation for the same dialogue can vary for two different services. Here, the departure and arrival cities are captured by analogously functioning but differently named slots in both schemas. Furthermore, values for the number_stops and direct_only slots highlight idiosyncrasies between services interpreting the same concept.
> 
> There are many advantages to this approach. First, using a single model facilitates representation and transfer of common knowledge across related services. Second, since the model utilizes semantic representation of schema elements as input, it can interface with unseen services or APIs on which it has not been trained. Third, it is robust to changes like addition of new intents or slots to the service.

### Relevance

Label: 

## Record 0913

Paper: Towards Scalable Multi-domain Conversational Agents: The Schema-Guided Dialogue Dataset

### Question

> How did they gather the data?

### Passage

> The dialogue paraphrasing framework converts the outlines generated by the simulator into a natural conversation. Figure FIGREF11a shows a snippet of the dialogue outline generated by the simulator, containing a sequence of user and system actions. The slot values present in these actions are in a canonical form because they obtained directly from the service. However, users may refer to these values in various different ways during the conversation, e.g., “los angeles" may be referred to as “LA" or “LAX". To introduce these natural variations in the slot values, we replace different slot values with a randomly selected variation (kept consistent across user turns in a dialogue) as shown in Figure FIGREF11b.
> 
> Next we define a set of action templates for converting each action into a utterance. A few examples of such templates are shown below. These templates are used to convert each action into a natural language utterance, and the resulting utterances for the different actions in a turn are concatenated together as shown in Figure FIGREF11c. The dialogue transformed by these steps is then sent to the crowd workers. One crowd worker is tasked with paraphrasing all utterances of a dialogue to ensure naturalness and coherence.
> 
> In our paraphrasing task, the crowd workers are instructed to exactly repeat the slot values in their paraphrases. This not only helps us verify the correctness of the paraphrases, but also lets us automatically obtain slot spans in the generated utterances by string search. This automatic slot span generation greatly reduced the annotation effort required, with little impact on dialogue naturalness, thus allowing us to collect more data with the same resources. Furthermore, it is important to note that this entire procedure preserves all other annotations obtained from the simulator including the dialogue state. Hence, no further annotation is needed.

### Relevance

Label: 

## Record 0914

Paper: Towards Scalable Multi-domain Conversational Agents: The Schema-Guided Dialogue Dataset

### Question

> How did they gather the data?

### Passage

> Models in the schema-guided setting can condition on the pertinent services' schemas using descriptions of intents and slots. These models, however, also need access to representations for potentially unseen inputs from new services. Recent pretrained models like ELMo BIBREF23 and BERT BIBREF4 can help, since they are trained on very large corpora. Building upon these, we present our zero-shot schema-guided dialogue state tracking model.

### Relevance

Label: 

## Record 0915

Paper: Towards Scalable Multi-domain Conversational Agents: The Schema-Guided Dialogue Dataset

### Question

> How did they gather the data?

### Passage

> Virtual assistants help users accomplish tasks including but not limited to finding flights, booking restaurants and, more recently, navigating user interfaces, by providing a natural language interface to services and APIs on the web. The recent popularity of conversational interfaces and the advent of frameworks like Actions on Google and Alexa Skills, which allow developers to easily add support for new services, has resulted in a major increase in the number of application domains and individual services that assistants need to support, following the pattern of smartphone applications.
> 
> Consequently, recent work has focused on scalable dialogue systems that can handle tasks across multiple application domains. Data-driven deep learning based approaches for multi-domain modeling have shown promise, both for end-to-end and modular systems involving dialogue state tracking and policy learning. This line of work has been facilitated by the release of multi-domain dialogue corpora such as MultiWOZ BIBREF0, M2M BIBREF1 and FRAMES BIBREF2.
> 
> However, existing datasets for multi-domain task-oriented dialogue do not sufficiently capture a number of challenges that arise with scaling virtual assistants in production. These assistants need to support a large BIBREF3, constantly increasing number of services over a large number of domains. In comparison, existing public datasets cover few domains. Furthermore, they define a single static API per domain, whereas multiple services with overlapping functionality, but heterogeneous interfaces, exist in the real world.
> 
> To highlight these challenges, we introduce the Schema-Guided Dialogue (SGD) dataset, which is, to the best of our knowledge, the largest public task-oriented dialogue corpus. It exceeds existing corpora in scale, with over 16000 dialogues in the training set spanning 26 services belonging to 16 domains (more details in Table TABREF2). Further, to adequately test the models' ability to generalize in zero-shot settings, the evaluation sets contain unseen services and domains. The dataset is designed to serve as an effective testbed for intent prediction, slot filling, state tracking and language generation, among other tasks in large-scale virtual assistants.
> 
> We also propose the schema-guided paradigm for task-oriented dialogue, advocating building a single unified dialogue model for all services and APIs. Using a service's schema as input, the model would make predictions over this dynamic set of intents and slots present in

### Relevance

Label: 

## Record 0916

Paper: Impact of Coreference Resolution on Slot Filling

### Question

> What is the task of slot filling?

### Passage

> The main idea of slot filling is to extend a knowledge base by extracting pre-defined relations between (named) entities from text data. Systems are provided with a large collection of text documents and a query file including entities and the relations to find in the text. As output, they have to provide the second argument for each relation. For entity “Apple” and relation “org:founded_by”, for example, the systems need to extract “Steve Jobs”, “Steve Wozniak” and “Ronald Wayne” along with text passages for justification.
> 
> This task combines several NLP challenges like information retrieval, information extraction, relation classification and knowledge inference. Until 2014, the slot filling shared task included 41 relations (25 for persons and 16 for organizations) BIBREF3 . Since 2015, these relations have been extended to all possible inverse relations which introduced a new query entity type (geo-political entity) and augmented the set of relations to 64 (27 for persons, 20 for organizations and 17 for geo-political entities) BIBREF6 . Table 1 provides exemplary relations for the different entity types.
> 
> The input for a slot filling system is an xml query containing the name and type of the entity, an exemplary occurence of the entity in the document collection and the slot to be filled. The expected output of the system contains, i.a., a provenance for the slot filler in the document collection, the slot filler itself, the type of the filler ( $\in {PER, ORG, GPE, STRING}$ ), its offsets in the document collection, as well as a confidence value of the system.
> 
> The document collection from which the slot fillers should be extracted is quite large: until 2014, it consisted of about 2.1 million documents, in 2015 the number was reduced to about 50,000 documents. The documents comprise newswire, web and discussion forum texts. Therefore, the slot filling task is more than relation extraction for pre-defined relations: It also includes challenges like information retrieval and coping with different genres.
> 
> Most slot filling systems are a pipeline of different components, such as query expansion, information retrieval, candidate extraction, candidate classification and postprocessing. Figure 1 depicts a typical system. We performed a detailed analysis of the errors of these components and found that one

### Relevance

Label: 

## Record 0917

Paper: Impact of Coreference Resolution on Slot Filling

### Question

> What is the task of slot filling?

### Passage

> As motivated above, coreference information is a very important resource for participants of the slot filling task or related knowledge base population tasks on the same documents. Since we found that the coreference resolution component is one of the bottlenecks which considerably slows down our slot filling pipeline, we have pre-processed the TAC source corpus by tagging its documents using Stanford CoreNLP BIBREF10 . We call this resource of coreference chains KBPchains and share it (in the form of document-offset spans) on our website. Although CoreNLP is publicly available, KBPchains will save researchers much time and resources (cf., analysisRecall who mentioned the need for efficient coreference resolution when processing the large slot filling corpora). Table 2 lists statistics about the extracted coreference chains and their mentions. In addition to the minimum, maximum, average and median numbers of chains per document, mentions per chain and words per mention, we also report the number of mentions which are pronouns, the number of singletons (chains consisting of only one mention) and the number of chains with only identical mentions.

### Relevance

Label: 

## Record 0918

Paper: Impact of Coreference Resolution on Slot Filling

### Question

> What is the task of slot filling?

### Passage

> The slot filling task has been organized since 2009. The top ranked systems of the last years achieved F1 scores of 37.28 (2013) BIBREF4 , 36.77 (2014) BIBREF5 and 31.48 (2015). In 2015, the task has been merged with the Cold Start track of the same conference. This led to several changes in the number of relations, the evaluation documents and the outputs expected from the systems BIBREF6 .
> 
> Previous studies and error analyses have shown that coreference resolution is an important component to increase the recall of slot filling systems BIBREF7 , BIBREF8 , BIBREF9 . analysis2012 identified coreference failures as the second most frequent error source of slot filling systems (after inference failures). In most cases, nominal anaphors were not resolved correctly. analysisRecall investigated possible causes of recall loss in a slot filling system. They described that coreference resolution provided higher recall but might be inefficient since it requires a lot of time and resources. Moreover, they argued that the overall results of a slot filling system might be better without coreference resolution since it can have a negative impact on precision. In contrast, our experiments in this study show that the increased number of true positives when using coreference resolution has a much higher impact on the final results. For coping with the problem of time-consuming coreference resolution, we prepared and publish KBPchains, a coreference resource for slot filling.

### Relevance

Label: 

## Record 0919

Paper: Impact of Coreference Resolution on Slot Filling

### Question

> What is the task of slot filling?

### Passage

> In this work, we analyzed the impact of coreference resolution on the NLP task slot filling. We showed that coreference information improves the slot filling system performance and outlined the most important challenges we have discovered in an analysis of coreference resolution errors. Since the TAC source corpus is very large, we will publish KBPchains, a resource containing the coreference chains which we have extracted automatically.

### Relevance

Label: 

## Record 0920

Paper: Impact of Coreference Resolution on Slot Filling

### Question

> What is the task of slot filling?

### Passage

> In our study, we have identified two main reasons why coreference resolution can improve slot filling performance. The first reason is that both arguments of a relation can be pronouns referring to the entity or filler in question. Consider the relation “per:parents” and the sentence “Bill is the father of Jane.” Both entities “Bill” and “Jane” might have been mentioned in sentences before and could now be replaced by pronouns: “He is the father of Jane”, “Bill is her father” or “He is her father”. If a slot filling system only extracts sentences with appearances of the full name of a person, it might miss many relevant sentences which can reduce the recall of the whole system drastically. As analysisRecall pointed out, the recall losses cannot be recovered by subsequent pipeline modules.
> 
> The second reason is that coreference resolution can provide slot fillers “for free”: If a phrase like “The Hawaii-born” is coreferent to the entity in question, it not only provides an additional sentence with information about the entity but also directly the location of birth (without the need of classification). Similar phrases can provide the age, a title or the religion of a person or the location of headquarters of an organization.

### Relevance

Label: 

## Record 0921

Paper: RelNet: End-to-End Modeling of Entities & Relations

### Question

> How is knowledge stored in the memory?

### Passage

> Reasoning about entities and their relations is an important problem for achieving general artificial intelligence. Often such problems are formulated as reasoning over graph-structured representation of knowledge. Knowledge graphs, for example, consist of entities and relations between them BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 . Representation learning BIBREF4 , BIBREF5 , BIBREF6 , BIBREF7 and reasoning BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 with such structured representations is an important and active area of research.
> 
> Most previous work on knowledge representation and reasoning relies on a pipeline of natural language processing systems, often consisting of named entity extraction BIBREF12 , entity resolution and coreference BIBREF13 , relationship extraction BIBREF4 , and knowledge graph inference BIBREF14 . While this cascaded approach of using NLP systems can be effective at reasoning with knowledge bases at scale, it also leads to a problem of compounding of the error from each component sub-system. The importance of each of these sub-component on a particular downstream application is also not clear.
> 
> For the task of question-answering, we instead make an attempt at an end-to-end approach which directly models the entities and relations in the text as memory slots. While incorporating existing knowledge (from curated knowledge bases) for the purpose of question-answering BIBREF11 , BIBREF8 , BIBREF15 is an important area of research, we consider the simpler setting where all the information is contained within the text itself – which is the approach taken by many recent memory based neural network models BIBREF16 , BIBREF17 , BIBREF18 , BIBREF19 .
> 
> Recently, BIBREF17 proposed a dynamic memory based neural network for implicitly modeling the state of entities present in the text for question answering. However, this model lacks any module for relational reasoning. In response, we propose RelNet, which extends memory-augmented neural networks with a relational memory to reason about relationships between multiple entities present within the text. Our end-to-end method reads text, and writes to both memory slots and edges between them. Intuitively, the memory slots correspond to entities and the edges correspond to relationships between entities, each represented as a vector. The only supervision signal for our method comes from answering questions on the text.
> 
> We demonstrate the utility of

### Relevance

Label: 

## Record 0922

Paper: RelNet: End-to-End Modeling of Entities & Relations

### Question

> How is knowledge stored in the memory?

### Passage

> There is a long line of work in textual question-answering systems BIBREF21 , BIBREF22 . Recent successful approaches use memory based neural networks for question answering, for example BIBREF23 , BIBREF18 , BIBREF24 , BIBREF19 , BIBREF17 . Our model is also a memory network based model and is also related to the neural turing machine BIBREF25 . As described previously, the model is closely related to the Recurrent Entity Networks model BIBREF17 which describes an end-to-end approach to model entities in text but does not directly model relations. Other approaches to question answering use external knowledge, for instance external knowledge bases BIBREF26 , BIBREF11 , BIBREF27 , BIBREF28 , BIBREF9 or external text like Wikipedia BIBREF29 , BIBREF30 .
> 
> Very recently, and in parallel to this work, a method for relational reasoning called relation networks BIBREF31 was proposed. They demonstrated that simple neural network modules are not as effective at relational reasoning and their proposed module is similar to our model. However, relation network is not a memory-based model and there is no mechanism to read and write relevant information for each pair. Moreover, while their approach scales as the square of the number of sentences, our approach scales as the square of the number of memory slots used per QA pair. The output module in our model can be seen as a type of relation network.
> 
> Representation learning and reasoning over graph structured data is also relevant to this work. Graph based neural network models BIBREF32 , BIBREF33 , BIBREF34 have been proposed which take graph data as an input. The relational memory however does not rely on a specified graph structure and such models can potentially be used for multi-hop reasoning over the relational memory. BIBREF35 proposed a method for learning a graphical representation of the text data for question answering, however the model requires explicit supervision for the graph at every step whereas RelNet does not require explicit supervision for the graph.

### Relevance

Label: 

## Record 0923

Paper: RelNet: End-to-End Modeling of Entities & Relations

### Question

> How is knowledge stored in the memory?

### Passage

> We describe the RelNet model in this section. Figure 1 provides a high-level view of the model. The model is sequential in nature, consisting of the following steps: read text, process it into a dynamic relational memory and then attention conditioned on the question generates the answer. We model the dynamic memory in a fashion similar to Recurrent Entity Networks BIBREF17 and then equip it with an additional relational memory.
> 
> There are three main components to the model: 1) input encoder 2) dynamic memory, and 3) output module. We will describe these three modules in details. The input encoder and output module implementations are similar to the Entity Network BIBREF17 and main novelty lies in the dynamic memory. We describe the operations executed by the network for a single example consisting of a document with $T$ sentences, where each sentence consists of a sequence of words represented with $K$ -dimensional word embeddings $\lbrace e_1, \ldots , e_N\rbrace $ , a question on the document represented as another sequence of words and an answer to the question.

### Relevance

Label: 

## Record 0924

Paper: RelNet: End-to-End Modeling of Entities & Relations

### Question

> How is knowledge stored in the memory?

### Passage

> We evaluate the model's performance on the bAbI tasks BIBREF18 , a collection of 20 question answering tasks which have become a benchmark for evaluating memory-augmented neural networks. We compare the performance with the Recurrent Entity Networks model (EntNet) BIBREF17 . Performance is measured in terms of mean percentage error on the tasks.
> 
> Training Details: We used Adam and did a grid search for the learning rate in {0.01, 0.005, 0.001} and choose a fixed learning rate of 0.005 based on performance on the validation set, and clip the gradient norm at 2. We keep all other details similar to BIBREF17 for a fair comparison. embedding dimensions were fixed to be 100, models were trained for a maximum of 250 epochs with mini-batches size of 32 for all tasks except 3 for which the batch size was 16. The document sizes were limited to most recent 70 sentences for all tasks, except for task 3 for which it was limited to 130. The RelNet models were run for 5 times with random seed on each task and the model with best validation performance was chosen as the final model. The baseline EntNet model was run for 10 times for each task BIBREF17 .
> 
> The results are shown in Table 1 . The RelNet model achieves a mean error of 0.285% across tasks which is better than the results of the EntNet model BIBREF17 . The RelNet model is able to achieve 0% test error on 11 of the tasks, whereas the EntNet model achieves 0% error on 7 of the tasks.

### Relevance

Label: 

## Record 0925

Paper: RelNet: End-to-End Modeling of Entities & Relations

### Question

> How is knowledge stored in the memory?

### Passage

> them. Intuitively, the memory slots correspond to entities and the edges correspond to relationships between entities, each represented as a vector. The only supervision signal for our method comes from answering questions on the text.
> 
> We demonstrate the utility of the model through experiments on the bAbI tasks BIBREF18 and find that the model achieves smaller mean error across the tasks than the best previously published result BIBREF17 in the 10k examples regime and achieves 0% error on 11 of the 20 tasks.

### Relevance

Label: 

## Record 0926

Paper: Gated Convolutional Neural Networks for Domain Adaptation

### Question

> Does the fact that GCNs can perform well on this tell us that the task is simpler than previously thought?

### Passage

> We find that gated architectures vastly outperform non gated CNN model. The effectiveness of gated architectures rely on the idea of training a gate with sole purpose of identifying a weightage. In the task of sentiment analysis this weightage corresponds to what weights will lead to a decrement in final loss or in other words, most accurate prediction of sentiment. In doing so, the gate architecture learns which words or n-grams contribute to the sentiment the most, these words or n-grams often co-relate with domain independent words. On the other hand the gate gives less weightage to n-grams which are largely either specific to domain or function word chunks which contribute negligible to the overall sentiment. This is what makes gated architectures effective at Domain Adaptation.
> 
> In Figure 3 , we have illustrated the visualization of convolution outputs(kernel size = 3) from the sigmoid gate in GLU across domains. As the kernel size is 3, each row in the output corresponds to a trigram from input sentence. This heat map visualizes values of all 100 filters and their average for every input trigram. These examples demonstrate what the convolution gate learns. Trigrams with domain independent but heavy polarity like “_ _ good” and “_ costly would” have higher weightage. Meanwhile, Trigrams with domain specific terms like “quality functional case” and “sell entire kitchen” get some of the least weights. In Figure 3 (b) example, the trigram “would have to” just consists of function words, hence gets the least weight. While “sell entire kitchen” gets more weight comparatively. This might be because while function words are merely grammatical units which contribute minimal to overall sentiment, domain specific terms like “sell” may contain sentiment level knowledge only relevant within the domain. In such a case it is possible that the filters effectively propagate sentiment level knowledge from domain specific terms as well.
> 
> We see that gated architectures almost always outperform recurrent, attention and linear models BoW, TFIDF, PV. This is largely because while training and testing on same domains, these models especially recurrent and attention based may perform better. However, for Domain Adaptation, as they lack gated structure which is trained in parallel to learn importance, their

### Relevance

Label: 

## Record 0927

Paper: Gated Convolutional Neural Networks for Domain Adaptation

### Question

> Does the fact that GCNs can perform well on this tell us that the task is simpler than previously thought?

### Passage

> Given a source domain $D_{S}$ represented as $D_{S}$ = { $(x_{s_{1}},y_{s_{1}})$ , $(x_{s_{2}},y_{s_{2}})$ .... $(x_{s_{n}},y_{s_{n}})$ } where $x_{s_{i}} \in \mathbb {R}$ represents the vector of $i^{th}$ source text and $y_{s_{i}}$ represents the corresponding source domain label. Let $T_{S}$ represent the task in source domain. Given a target domain $D_{T}$ represented as $D_{S}$0 = { $D_{S}$1 , $D_{S}$2 .... $D_{S}$3 }, where $D_{S}$4 represents the vector of $D_{S}$5 target text and $D_{S}$6 represents corresponding target domain label. Let $D_{S}$7 represent the task in target domain. Domain Adaptation (DA) is defined by the target predictive function $D_{S}$8 calculated using the knowledge of $D_{S}$9 and $(x_{s_{1}},y_{s_{1}})$0 where $(x_{s_{1}},y_{s_{1}})$1 but $(x_{s_{1}},y_{s_{1}})$2 . It is imperative to note that the domains are different but only a single task. In this paper, the task is sentiment classification.

### Relevance

Label: 

## Record 0928

Paper: Gated Convolutional Neural Networks for Domain Adaptation

### Question

> Does the fact that GCNs can perform well on this tell us that the task is simpler than previously thought?

### Passage

> The proposed model architecture is shown in the Figure 1 . Recurrent Neural Networks like LSTM, GRU update their weights at every timestep sequentially and hence lack parallelization over inputs in training. In case of attention based models, the attention layer has to wait for outputs from all timesteps. Hence, these models fail to take the advantage of parallelism either. Since, proposed model is based on convolution layers and gated mechanism, it can be parallelized efficiently. The convolution layers learn higher level representations for the source domain. The gated mechanism learn the domain agnostic representations. They together control the information that has to flow through further fully connected output layer after max pooling.
> 
> Let $I$ denote the input sentence represented as $I$ = { $w_{1}$ $w_{2}$ $w_{3}$ ... $w_{N}$ } where $w_{i}$ represents the $i_{th}$ word in $I$ and $N$ is the maximum sentence length considered. Let $I$0 be the vocabulary size for each dataset and $I$1 denote the word embedding matrix where each $I$2 is a $I$3 dimensional vector. Input sentences whose length is less than $I$4 are padded with 0s to reach maximum sentence length. Words absent in the pretrained word embeddings are initialized to 0s. Therefore each input sentence $I$5 is converted to $I$6 dimensional vector. Convolution operation is applied on $I$7 with kernel $I$8 . The convolution operation is one-dimensional, applied with a fixed window size across words. We consider kernel size of 3,4 and 5. The weight initialization of these kernels is done using glorot uniform BIBREF23 . Each kernel is a feature detector which extracts patterns from n-grams. After convolution we obtain a new feature map $I$9 = [ $w_{1}$0 ] for each kernel $w_{1}$1 .
> 
> $$C_{i} = f(P_{i:i+h} \ast W_{a} + b_{a})$$   (Eq. 5)
> 
> where $f$ represents the activation function in convolution layer. The gated mechanism is applied on each convolution layer. Each gated layer learns to filter domain agnostic representations for every time step $i$ .
> 
> $$S_{i} = g(P_{i:i+h} \ast W_{s} + b_{s})$$   (Eq. 6)
> 
> where $g$ is the activation function used in gated convolution layer. The outputs from convolution layer and gated convolution layer are element wise multiplied to compute a new feature representation $G_{i}$
> 
> $$G_{i}

### Relevance

Label: 

## Record 0929

Paper: Gated Convolutional Neural Networks for Domain Adaptation

### Question

> Does the fact that GCNs can perform well on this tell us that the task is simpler than previously thought?

### Passage

> All the models are experimented with approximately matching number of parameters for a solid comparison using a Tesla K80 GPU.
> 
> Input Each word in the input sentence is converted to a 300 dimensional vector using GloVe pretrained vectors BIBREF28 . A maximum sentence length 100 is considered for all the datasets. Sentences with length less than 100 are padded with 0s.
> 
> Architecture details: The model is implemented using keras. We considered 100 convolution filters for each of the kernels of sizes 3,4 and 5. To get the same sentence length after convolution operation zero padding is done on the input.
> 
> Training Each sentence or paragraph is converted to lower case. Stopword removal is not done. A vocabulary size of 20000 is considered for all the datasets. We apply a dropout layer BIBREF29 with a probability of 0.5, on the embedding layer and probability 0.2, on the dense layer that connects the output layer. Adadelta BIBREF30 is used as the optimizer for training with gradient descent updates. Batch-size of 16 is taken for MDD and 50 for ARD. The model is trained for 50 epochs. We employ an early stopping mechanism based on validation loss for a patience of 10 epochs. The models are trained on source domain and tested on unseen target domain in all experiments.

### Relevance

Label: 

## Record 0930

Paper: Gated Convolutional Neural Networks for Domain Adaptation

### Question

> Does the fact that GCNs can perform well on this tell us that the task is simpler than previously thought?

### Passage

> PV. This is largely because while training and testing on same domains, these models especially recurrent and attention based may perform better. However, for Domain Adaptation, as they lack gated structure which is trained in parallel to learn importance, their performance on target domain is poor as compared to gated architectures. As gated architectures are based on convolutions, they exploit parallelization to give significant boost in time complexity as compared to other models. This is depicted in Table 1 .
> 
> While the gated architectures outperform other baselines, within them as well we make observations. Gated Linear Unit (GLU) performs the best often over other gated architectures. In case of GTU, outputs from Sigmoid and Tanh are multiplied together, this may result in small gradients, and hence resulting in the vanishing gradient problem. However, this will not be the in the case of GLU, as the activation is linear. In case of GTRU, outputs from Tanh and ReLU are multiplied. In ReLU, because of absence of negative activations, corresponding Tanh outputs will be completely ignored, resulting in loss of some domain independent knowledge.

### Relevance

Label: 

## Record 0931

Paper: Filling Gender&Number Gaps in Neural Machine Translation with Black-box Context Injection

### Question

> What type of syntactic analysis is performed?

### Passage

> The BLEU score is an indication of how close the automated translation is to the reference translation, but does not tell us what exactly changed concerning the gender and number properties we attempt to control. We perform a finer-grained analysis focusing on the relation between the injected speaker and audience information, and the morphological realizations of the corresponding elements. We parse the translations and the references using a Hebrew dependency parser. In addition to the parse structure, the parser also performs morphological analysis and tagging of the individual tokens. We then perform the following analysis.
> 
> Speaker's Gender Effects: We search for first-person singular pronouns with subject case (ani, unmarked for gender, corresponding to the English I), and consider the gender of its governing verb (or adjectives in copular constructions such as `I am nice'). The possible genders are `masculine', `feminine' and `both', where the latter indicates a case where the none-diacriticized written form admits both a masculine and a feminine reading. We expect the gender to match the ones requested in the prefix.
> 
> Interlocutors' Gender and Number Effects: We search for second-person pronouns and consider their gender and number. For pronouns in subject position, we also consider the gender and number of their governing verbs (or adjectives in copular constructions). For a singular audience, we expect the gender and number to match the requested ones. For a plural audience, we expect the masculine-plural forms.
> 
> Results: Speaker. Figure FIGREF3 shows the result for controlling the morphological properties of the speaker ({he, she, I} said). It shows the proportion of gender-inflected verbs for the various conditions and the reference. We see that the baseline system severely under-predicts the feminine form of verbs as compared to the reference. The “He said” conditions further decreases the number of feminine verbs, while the “I said” conditions bring it back to the baseline level. Finally, the “She said” prefixes substantially increase the number of feminine-marked verbs, bringing the proportion much closer to that of the reference (though still under-predicting some of the feminine cases).
> 
> Results: Audience. The chart in Figure FIGREF3 shows the results for controlling the number of the audience (...to them vs nothing). It shows the proportion of singular

### Relevance

Label: 

## Record 0932

Paper: Filling Gender&Number Gaps in Neural Machine Translation with Black-box Context Injection

### Question

> What type of syntactic analysis is performed?

### Passage

> the desired morphological decisions according to the given hint, even when no other evidence is available on the source side. While adding those hints results in additional text on the target side, we show that it is simple to remove, leaving only the desired translation.
> 
> Our method is appealing as it only requires simple pre-and-post processing of the inputs and outputs, without considering the system internals, or requiring specific annotated data and training procedure as in previous work BIBREF1 . We show that in spite of its simplicity, it is effective in resolving many of the ambiguities and improves the translation quality in up to 2.3 BLEU when given the correct hints, which may be inferred from text metadata or other sources. Finally, we perform a fine-grained syntactic analysis of the translations generated using our method which shows its effectiveness.

### Relevance

Label: 

## Record 0933

Paper: Filling Gender&Number Gaps in Neural Machine Translation with Black-box Context Injection

### Question

> What type of syntactic analysis is performed?

### Passage

> We highlight the problem of translating between languages with different morphological systems, in which the target translation must contain gender and number information that is not available in the source. We propose a method for injecting such information into a pre-trained NMT model in a black-box setting. We demonstrate the effectiveness of this method by showing an improvement of 2.3 BLEU in an English-to-Hebrew translation setting where the speaker and audience gender can be inferred. We also perform a fine-grained syntactic analysis that shows how our method enables to control the morphological realization of first and second-person pronouns, together with verbs and adjectives related to them. In future work we would like to explore automatic generation of the injected context, or the use of cross-sentence context to infer the injected information.

### Relevance

Label: 

## Record 0934

Paper: Filling Gender&Number Gaps in Neural Machine Translation with Black-box Context Injection

### Question

> What type of syntactic analysis is performed?

### Passage

> Different languages use different morphological features marking different properties on different elements. For example, English marks for number, case, aspect, tense, person, and degree of comparison. However, English does not mark gender on nouns and verbs. Even when a certain property is marked, languages differ in the form and location of the marking BIBREF0 . For example, marking can occur on the head of a syntactic dependency construction, on its argument, on both (requiring agreement), or on none of them. Translation systems must generate correct target-language morphology as part of the translation process. This requires knowledge of both the source-side and target-side morphology. Current state-of-the-art translation systems do capture many aspects of natural language, including morphology, when a relevant context is available BIBREF2 , BIBREF3 , but resort to “guessing” based on the training-data statistics when it is not. Complications arise when different languages convey different kinds of information in their morphological systems. In such cases, a translation system may be required to remove information available in the source sentence, or to add information not available in it, where the latter can be especially tricky.

### Relevance

Label: 

## Record 0935

Paper: Filling Gender&Number Gaps in Neural Machine Translation with Black-box Context Injection

### Question

> What type of syntactic analysis is performed?

### Passage

> A common way for marking information about gender, number, and case in language is morphology, or the structure of a given word in the language. However, different languages mark such information in different ways – for example, in some languages gender may be marked on the head word of a syntactic dependency relation, while in other languages it is marked on the dependent, on both, or on none of them BIBREF0 . This morphological diversity creates a challenge for machine translation, as there are ambiguous cases where more than one correct translation exists for the same source sentence. For example, while the English sentence “I love language” is ambiguous with respect to the gender of the speaker, Hebrew marks verbs for the gender of their subject and does not allow gender-neutral translation. This allows two possible Hebrew translations – one in a masculine and the other in a feminine form. As a consequence, a sentence-level translator (either human or machine) must commit to the gender of the speaker, adding information that is not present in the source. Without additional context, this choice must be done arbitrarily by relying on language conventions, world knowledge or statistical (stereotypical) knowledge.
> 
> Indeed, the English sentence “I work as a doctor” is translated into Hebrew by Google Translate using the masculine verb form oved, indicating a male speaker, while “I work as a nurse” is translated with the feminine form ovedet, indicating a female speaker (verified on March 2019). While this is still an issue, there have been recent efforts to reduce it for specific language pairs.
> 
> We present a simple black-box method to influence the interpretation chosen by an NMT system in these ambiguous cases. More concretely, we construct pre-defined textual hints about the gender and number of the speaker and the audience (the interlocutors), which we concatenate to a given input sentence that we would like to translate accordingly. We then show that a black-box NMT system makes the desired morphological decisions according to the given hint, even when no other evidence is available on the source side. While adding those hints results in additional text on the target side, we show that it is simple to remove,

### Relevance

Label: 

## Record 0936

Paper: HireNet: a Hierarchical Attention Model for the Automatic Analysis of Asynchronous Video Job Interviews

### Question

> Is there any ethical consideration in the research?

### Passage

> To the best of our knowledge, only one corpus of interviews with real open positions has been collected and is subject to automatic analysis BIBREF3 . This corpus consists of face-to-face job interviews for a marketing short assignment whose candidates are mainly students. There are video corpora of face-to-face mock interviews that include two corpora built at the Massachusetts Institute of Technology BIBREF4 , BIBREF5 , and a corpus of students in services related to hospitality BIBREF6 . Many corpora of simulated asynchronous video interviews have also been built: a corpus of employees BIBREF7 , a corpus of students from Bangalore University BIBREF8 and a corpus collected through the use of crowdsourcing tools BIBREF2 . Some researchers are also interested in online video resumes and have constituted a corpus of video CVs from YouTube BIBREF9 . A first impressions challenge dataset was also supplemented by hirability annotation BIBREF10 . Some corpora are annotated by experts or students in psychology BIBREF7 , BIBREF2 , BIBREF3 , BIBREF11 . Other corpora have used crowdsourcing platforms or naive observers BIBREF8 for annotation. Table TABREF2 contains a summary of the corpora of job interviews used in previous works.

### Relevance

Label: 

## Record 0937

Paper: HireNet: a Hierarchical Attention Model for the Automatic Analysis of Asynchronous Video Job Interviews

### Question

> Is there any ethical consideration in the research?

### Passage

> Among assessment methods, the job interview remains the most common way to evaluate candidates. The interview can be done via phone, live video, face to face, or more recently asynchronous video interview. For the latter, candidates connect to a platform, and record themselves while answering a set of questions chosen by the recruiter. The platform then allows several recruiters to evaluate the candidate, to discuss among themselves and possibly to invite the candidate to a face-to-face interview. Recruiters choose to use these platforms because it gives them access to a larger pool of candidates, and it speeds up the application processing time. In addition, it allows candidates to do the interview whenever and wherever it suits them the most. However, given a large number of these asynchronous interviews it may quickly become unmanageable for recruiters. The highly structured characteristic of asynchronous video interviews (same questions, same amount of time per candidate) enhances their predictive validity, and reduces inter-recruiter variability BIBREF0 . Moreover, recent advances in Social Signal Processing (SSP) BIBREF1 have enabled automated candidate assessment BIBREF2 , and companies have already started deploying solutions serving that purpose. However, previous studies used corpora of simulated interviews with limited sizes. The work proposed in this paper relies on a corpus that has been built in collaboration with a company and that consists of more than 7000 real job interviews for 475 open positions. The size of this corpus enables the exploration of emerging models such as deep learning models, that are known to be difficult to deploy for Social Computing because of the difficulty to obtain large annotations of social behaviors. Based on those facts, we propose HireNet, a new hierarchical attention neural network for the purpose of automatically classifying candidates into two classes: hirable and not hirable. Our model aims to assist recruiters in the selection process. It does not aim to make any automatic decision about candidate selection. First, this model was built to mirror the sequential and hierarchical structure of an interview assessment: recruiters watch a sequence of questions and answers, which are themselves sequences of words or behavioral signals. Second, the HireNet model integrates the context of the open position (questions during the

### Relevance

Label: 

## Record 0938

Paper: HireNet: a Hierarchical Attention Model for the Automatic Analysis of Asynchronous Video Job Interviews

### Question

> Is there any ethical consideration in the research?

### Passage

> We propose here a new model named HireNet, as in a neural network for hirability prediction. It is inspired by work carried out in neural networks for natural language processing and from the HierNet BIBREF19 , in particular, which aims to model a hierarchy in a document. Following the idea that a document is composed of sentences and words, a job interview could be decomposed, as a sequence of answers to questions, and the answers, as a sequence of low level descriptors describing each answer.
> 
> The model architecture (see Figure FIGREF6 ) is built relying on four hypotheses. The first hypothesis (H1) is the importance of the information provided by the sequentiality of the multimodal cues occurring in the interview. We thus choose to use a sequential model such as a recurrent neural network. The second hypothesis (H2) concerns the importance of the hierarchical structure of an interview: the decision of to hire should be performed at the candidate level, the candidates answering several questions during the interview. We thus choose to introduce different levels of hierarchy in HireNet namely the candidate level, the answer level and the word (or frame) level. The third hypothesis (H3) concerns the existence of salient information or social signals in a candidate's video interview: questions are not equally important and not all the parts of the answers have an equal influence on the recruiter's decision. We thus choose to introduce attention mechanisms in HireNet. The last hypothesis (H4) concerns the importance of contextual information such as questions and job titles. Therefore, HireNet includes vectors that encode this contextual information.

### Relevance

Label: 

## Record 0939

Paper: HireNet: a Hierarchical Attention Model for the Automatic Analysis of Asynchronous Video Job Interviews

### Question

> Is there any ethical consideration in the research?

### Passage

> same amount of previous information for each element of INLINEFORM0 . Using a simple forward encoder could lead to biased attention vectors focusing only on the latest elements of the answers.
> 
> In this study, the local context information corresponds to the questions INLINEFORM0 . In order to encode these sentences, we use a simple forward GRU. DISPLAYFORM0
> 
> And the final representation of a question is the hidden state of the last word in the question INLINEFORM0 (i.e. INLINEFORM1 ).
> 
> In order to obtain a better representation of of the candidate's answer, we aim to detect elements in the sequence which were salient for the classification task. Moreover, we hypothesize that the local context is highly important. Different behavioral signals can occur depending on the question type and it can also influence the way recruiters assess their candidates BIBREF23 . An additive attention mechanism is proposed in order to extract the importance of each moment in the sequence representing the answer. DISPLAYFORM0 DISPLAYFORM1
> 
> where INLINEFORM0 and INLINEFORM1 are weight matrices, INLINEFORM2 and INLINEFORM3 are weight vectors and INLINEFORM4 denotes the transpose of INLINEFORM5 .
> 
> In order to have the maximum amount of information, we concatenate at the second level, the representation of the local context and the answer representation. Moreover, we think that given the way video interviews work, the more questions a candidate answers during the interview, the more he adapts and gets comfortable. In the light of this, we decided to encode question-answer pairs as a sequence. Given INLINEFORM0 , we can use the same representation scheme as that of the low level encoder: DISPLAYFORM0 DISPLAYFORM1
> 
> We will also concatenate forward hidden states and backward hidden states: DISPLAYFORM0
> 
> We encode the job title the same way we encode the questions : DISPLAYFORM0
> 
> As done for the representation of the question, the final representation of the job title is the hidden state of the last word of INLINEFORM0 (i.e. INLINEFORM1 ).
> 
> The importance of a question depends on the context of the interview, and specifically, on the type of job the candidate is applying for. For instance, a junior sales position interview could accord more importance to the social skills, while an interview for a

### Relevance

Label: 

## Record 0940

Paper: HireNet: a Hierarchical Attention Model for the Automatic Analysis of Asynchronous Video Job Interviews

### Question

> Is there any ethical consideration in the research?

### Passage

> We represent a video interview as an object composed of a job title INLINEFORM0 and INLINEFORM1 question-answer pairs INLINEFORM2 . In our model, the job title INLINEFORM3 is composed of a sequence of INLINEFORM4 words INLINEFORM5 where INLINEFORM6 denotes the length of the job title. In a same way, the INLINEFORM7 -th question INLINEFORM8 is a sequence of INLINEFORM9 words INLINEFORM10 where INLINEFORM11 denotes the number of words in the question INLINEFORM12 . INLINEFORM13 denotes the sequence of low level descriptors INLINEFORM14 describing the INLINEFORM15 -th answer. In our study these low level descriptors could be embedded words, features extracted from an audio frame, or features extracted from a video frame. INLINEFORM16 denotes the length of the sequence of low level descriptors of the INLINEFORM17 -th answer.
> 
> We decided to use a Gated Recurrent Unit (GRU) BIBREF22 to encode information from the job title, the questions and the answers. A GRU is able to encode sequences. It uses two mechanisms to solve the vanishing gradient problem, namely the reset gate, controlling how much past information is needed; and the update gate, determining how much past information has to be kept and the amount of new information to add. For formalization, we will denote by INLINEFORM0 the hidden state of GRU at timestep INLINEFORM1 of the encoded sequence.
> 
> This part of the model aims to encode the sequences of low level descriptors. As mentioned before, the sequences can represent a text, an audio stream or a video stream. A bidirectional GRU is used to obtain representations from both directions for each element of the sequence INLINEFORM0 . It contains the forward GRU which reads the sequence from left to right and backward GRU which reads the sequence from right to left: DISPLAYFORM0 DISPLAYFORM1
> 
> In the same way, an encoding for a given low level descriptor INLINEFORM0 is obtained by concatenating forward hidden states and backward hidden states: DISPLAYFORM0
> 
> Encoding sequences in a bidirectional fashion ensures the same amount of previous information for each element of INLINEFORM0 . Using a simple forward encoder could lead to biased attention vectors focusing only on the latest elements of the answers.
> 
> In this study, the local context information corresponds to

### Relevance

Label: 

## Record 0941

Paper: Generating Narrative Text in a Switching Dynamical System

### Question

> What baselines are used?

### Passage

> For the SLDS models, the interpolations are generated via the Gibbs sampling algorithm described earlier. In all experiments for the SLDS models we draw 50 samples (including burn in samples) and output the interpolation that maximizes the probability of the given sentence(s). Since the baselines do not have the means for doing interpolations, we simulate `interpolations' for the baselines; we draw 1000 samples using top k (with k=15) truncated sampling (conditioned on the given initial sentences, if available). We then output the sample that maximizes the probability of the clamped sentences around which we are interpolating the others. We allow the S2S access to the gold sentiment tags. To give a lower bound on the performance of the SLDS model, we do not provide it with gold tags. We instead provide the SLDS model with the semi-noisy tags that are output from $q(S_i | X)$.

### Relevance

Label: 

## Record 0942

Paper: Generating Narrative Text in a Switching Dynamical System

### Question

> What baselines are used?

### Passage

> We automatically evaluate on four different types of interpolations (where different combinations of sentences are removed and the model is forced to regenerate them), We evaluate the generations with the ROUGE BIBREF29 and METEOR BIBREF30 metrics using the true sentences as targets. Table TABREF33 shows the automatic evaluation results from interpolations using our proposed models and baselines. The #Sent(s) column indicates which sentence(s) were removed, and then regenerated by the model. We gave the baselines a slight edge over SLDS because they pick the best out of 1000 samples while SLDS is only out of 50. The SLDS models see their largest gain over the baseline models when at least the first sentence is given as an input. The baseline models do better when the first and second sentence need to be imputed. This is likely due to the fact that having access to the earlier sentences allows a better initialization for the Gibbs sampler. Surprisingly, the semi-supervised variants of the SLDS models achieve higher scores. The reasons for this is discussed below in the Perplexity section.

### Relevance

Label: 

## Record 0943

Paper: Generating Narrative Text in a Switching Dynamical System

### Question

> What baselines are used?

### Passage

> A more fitting model would thus be a Switching Linear Dynamical System BIBREF1, BIBREF2, BIBREF3. In an SLDS, we assume there exists a set of $K$ different sets of dynamics, $\lbrace (A_1, \Sigma _1),...(A_K,\Sigma _K)\rbrace $. At time step $i+1$, one of these sets of dynamics is used. The one used depends on the value of a discrete variable at time step $i+1$ called the switching variable, $S_{i+1} \in \lbrace 1,...K\rbrace $:
> 
> There is a switching variable $S_i$ associated with each time step. The switching variable value itself evolves over time by a prior Markov process, $P(S_{i+1} | S_{i})$. This top level chain of switching variables thus forms our narrative scaffold, indicating what transitions we must go through in the narrative, with the dynamics matrices indicating how they transition.

### Relevance

Label: 

## Record 0944

Paper: Generating Narrative Text in a Switching Dynamical System

### Question

> What baselines are used?

### Passage

> Language Model (LM): We train a two layer recurrent neural language model with GRU cells of hidden size 512.
> 
> Sequence-to-Sequence Attention Model (S2S): We train a two layer neural sequence to sequence model equipped with bi-linear attention function with GRU cells of hidden size 512. Sentiments tags for a narrative (1 for each sentence) are given as input to the model and the corresponding sentences are concatenated together as the output with only one <eos> tag at the end. This model is trained with a 0.1 dropout. This model is comparable to the static model of BIBREF7, and other recent works employing a notion of scaffolding into neural generation (albeit adapted for our setting).
> 
> Linear Dynamical System (LDS): We also train a linear dynamical system as discussed in Section SECREF1 as one of our baselines for fair comparisons. Apart from having just a single transition matrix this model has the same architectural details as SLDS.
> 
> Semi-Supervised SLDS (SLDS-X%): To gauge the usability of semi-supervision, we also train semi-supervised SLDS models with varying amount of labelled sentiment tags unlike the original model which uses 100% tagged data. We refer to these as SLDS-X%, where X is the % labelled data used for training: 1%, 10%, 25%, and 50%.

### Relevance

Label: 

## Record 0945

Paper: Generating Narrative Text in a Switching Dynamical System

### Question

> What baselines are used?

### Passage

> One matter of interest is whether or not the transitions are capturing what they are supposed to capture, appropriate sentiment. Since we used the sentiment tagger Vader for training tags, we again utilize it to evaluate whether using transitions of a certain sentiment actually leads the model to produce outputs with the given sentiment. To perform this evaluation, we give as input to our models (and the S2S baseline) the sentiment tags for a sentence and allow it to generate a sentence conditioned on these sentiment tags. We then tag the generated sentences with Vader and see if the sentiment tags match the originals. We calculate the F1 score across all sentiment tags and report the macro average. In Table TABREF47 we see that having labels is incredibly important for meaningful transitions. There is a large drop in F1 as the amount of labels given to the model is decreased. The SLDS model that is trained with 100% of the labels performs a little better than even S2S, despite not having direct access to the sentiment labels (SLDS only uses the sentiment labels to decide which transition to use while the S2S model uses attention directly on the sentiment labels).

### Relevance

Label: 

## Record 0946

Paper: Classifying movie genres by analyzing text reviews

### Question

> how many movie genres do they explore?

### Passage

> This paper demonstrates that by only looking at text reviews of a movie, there is enough information to predict its genre with an INLINEFORM0 of INLINEFORM1 . This result implies that movie reviews carry latent information about genres. This paper also shows the complexity of doing prediction on multi-label problems, both in implementation and data processing but also when it comes to evaluation. Regular metrics typically work, but they mask the entire picture and the depth of how good a model is.
> 
> Finally this paper provides an explanation of the whole process needed to conduct an experiment like this. The process includes downloading a data set, web scraping for extra information, data preprocessing, model tuning and evaluation of the results.

### Relevance

Label: 

## Record 0947

Paper: Classifying movie genres by analyzing text reviews

### Question

> how many movie genres do they explore?

### Passage

> MLP is a class of feedforward neural network built up by a layered acyclic graph. An MLP consists of at least three layers and non-linear activations. The first layer is called input layer, the second layer is called hidden layer and the third layer is called output layer. The three layers are fully connected which means that every node in the hidden layer is connected to every node in the other layers. MLP is trained using backpropagation, where the weights are updated by calculating the gradient descent with respect to an error function. BIBREF4
> 
> K-nearest Neighbors (KNN) works by evaluating similarities between entities, where INLINEFORM0 stands for how many neighbors are taken into account during the classification. KNN is different from MLP in the sense that it does not require a computationally heavy training step; instead, all of the computation is done at the classification step. There are multiple ways of calculating the similarity, one way is to calculate the Minkowski distance. The Minkowski distance between two points DISPLAYFORM0
> 
> and DISPLAYFORM0
> 
> is defined by DISPLAYFORM0
> 
> where INLINEFORM0 which is equal to the Euclidean distance. BIBREF2

### Relevance

Label: 

## Record 0948

Paper: Classifying movie genres by analyzing text reviews

### Question

> how many movie genres do they explore?

### Passage

> By only reading a single text review of a movie it can be difficult to say what the genre of that movie is, but by using text mining techniques on thousands of movie reviews is it possible to predict the genre?
> 
> This paper explores the possibility of classifying genres of a movie based only on a text review of that movie. This is an interesting problem because to the naked eye it may seem difficult to predict the genre by only looking at a text review. One example of a review can be seen in the following example:
> 
> I liked the film. Some of the action scenes were very interesting, tense and well done. I especially liked the opening scene which had a semi truck in it. A very tense action scene that seemed well done. Some of the transitional scenes were filmed in interesting ways such as time lapse photography, unusual colors, or interesting angles. Also the film is funny is several parts. I also liked how the evil guy was portrayed too. I'd give the film an 8 out of 10.
> 
> http://www.imdb.com/title/tt0211938/reviews
> 
> From the quoted review, one could probably predict the movie falls in the action genre; however, it would be difficult to predict all three of the genres (action, comedy, crime) that International Movie Database (IMDB) lists. With the use of text mining techniques it is feasible to predict multiple genres based on a review.
> 
> There are numerous previous works on classifying the sentiment of reviews, e.g., maas-EtAl:2011:ACL-HLT2011 by BIBREF0 . There are fewer scientific papers available on specifically classifying movie genres based on reviews; therefore, inspiration for this paper comes from papers describing classification of text for other or general contexts. One of those papers is DBLP:journals/corr/cmp-lg-9707002 where BIBREF1 describe how to use a multilayer perceptron (MLP) for genre classification.
> 
> All data, in the form of reviews and genres, used in this paper originates from IMDb.

### Relevance

Label: 

## Record 0949

Paper: Classifying movie genres by analyzing text reviews

### Question

> how many movie genres do they explore?

### Passage

> In this paper the data comes from two sources where the first is a collection of text reviews. Those reviews were downloaded from Large Movie Review Datasets website . Because only 7000 reviews was used in this paper all of them were from the `train` folder and split evenly between positive reviews and negative reviews.
> 
> The genres for the reviews where obtained by iterating through all reviews and doing the following steps:
> 
> Save the text of the review.
> 
> Retrieve IMDb URL to the movie from the Large Movie Review Datasets data.
> 
> Scrape that movie website for all genres and download the genres.
> 
> The distribution of genres was plotted in a histogram to check that the scraped data looked reasonable and can be seen in figure FIGREF27 . All genres with less than 50 reviews corresponding to that genre were removed.
> 
> The number of genres per review can be seen in figure FIGREF28 and it shows that it is most common for a review to have three different genres; furthermore, it shows that no review has more than three genres.
> 
> http://ai.stanford.edu/ amaas/data/sentiment

### Relevance

Label: 

## Record 0950

Paper: Classifying movie genres by analyzing text reviews

### Question

> how many movie genres do they explore?

### Passage

> When evaluating classifiers it is common to use accuracy, precision and recall as well as Hamming loss. Accuracy, precision and recall are defined by the the four terms true positive ( INLINEFORM0 ), true negative ( INLINEFORM1 ), false positive ( INLINEFORM2 ) and false negative ( INLINEFORM3 ) which can be seen in table TABREF16 .
> 
> Accuracy is a measurement of how correct a model's predictions are and is defined as DISPLAYFORM0
> 
> .
> 
> Precision is a ratio of how often positive predictions actually are positve and is defined as DISPLAYFORM0
> 
> .
> 
> Recall is a measurement of how good the model is to find all true positives and is defined as DISPLAYFORM0
> 
> . BIBREF5
> 
> It has been shown that when calculating precision and recall on multi-label classifiers, it can be advantageous to use micro averaged precision and recall BIBREF6 . The formulas for micro averaged precision are expressed as DISPLAYFORM0 DISPLAYFORM1
> 
> where INLINEFORM0 is label index and INLINEFORM1 is number of labels.
> 
> Hamming loss is different in the sense that it is a loss and it is defined as the fraction of wrong labels to the total number of labels. Hamming loss can be a good measurement when it comes to evaluating multi-label classifiers. the hamming loss is expressed as DISPLAYFORM0
> 
> where INLINEFORM0 is number of documents, INLINEFORM1 number of labels, INLINEFORM2 is the target value and INLINEFORM3 is predicted value. BIBREF7
> 
> For evaluation the INLINEFORM0 and INLINEFORM1 was calculated as defined in section SECREF15 for both the MLP model and the KNN model. For precision and recall formulas EQREF20 and EQREF21 were used because of their advantage in multi-label classification. The distribution of predicted genres was also shown in a histogram and compared to the target distribution of genres.
> 
> Furthermore the ratio of reviews that got zero genres predicted was also calculated and can be expressed as DISPLAYFORM0
> 
> where INLINEFORM0 is the number of reviews without any predicted genre and INLINEFORM1 is the total amount of predicted reviews.

### Relevance

Label: 

## Record 0951

Paper: Sequence Labeling Parsing by Learning Across Representations

### Question

> Which dataset do they use?

### Passage

> To learn across representations we cast the problem as multi-task learning. mtl enables learning many tasks jointly, encapsulating them in a single model and leveraging their shared representation BIBREF12 , BIBREF22 . In particular, we will use a hard-sharing architecture: the sentence is first processed by stacked bilstms shared across all tasks, with a task-dependent feed-forward network on the top of it, to compute each task's outputs. In particular, to benefit from a specific parsing abstraction we will be using the concept of auxiliary tasks BIBREF23 , BIBREF24 , BIBREF25 , where tasks are learned together with the main task in the mtl setup even if they are not of actual interest by themselves, as they might help to find out hidden patterns in the data and lead to better generalization of the model. For instance, BIBREF26 have shown that semantic parsing benefits from that approach.
> 
> The input is the same for both types of parsing and the same number of timesteps are required to compute a tree (equal to the length of the sentence), which simplifies the joint modeling. In this work, we focus on parallel data (we train on the same sentences labeled for both constituency and dependency abstractions). In the future, we plan to explore the idea of exploiting joint training over disjoint treebanks BIBREF27 .

### Relevance

Label: 

## Record 0952

Paper: Sequence Labeling Parsing by Learning Across Representations

### Question

> Which dataset do they use?

### Passage

> Table TABREF18 compares single-paradigm models against their double-paradigm mtl versions. On average, mtl models with auxiliary losses achieve the best performance for both parsing abstractions. They gain INLINEFORM0 F1 points on average in comparison with the single model for constituency parsing, and INLINEFORM1 uas and INLINEFORM2 las points for dependency parsing. In comparison to the single-paradigm MTL models, the average gain is smaller: 0.05 f1 points for constituency parsing, and 0.09 uas and 0.21 las points for dependency parsing.
> 
> mtl models that use auxiliary tasks (d-mtl-aux) consistently outperform the single-task models (s-s) in all datasets, both for constituency parsing and for dependency parsing in terms of uas. However, this does not extend to las. This different behavior between uas and las seems to be originated by the fact that 2-task dependency parsing models, which are the basis for the corresponding auxiliary task and mtl models, improve uas but not las with respect to single-task dependency parsing models. The reason might be that the single-task setup excludes unlikely combinations of dependency labels with PoS tags or dependency directions that are not found in the training set, while in the 2-task setup, both components are treated separately, which may be having a negative influence on dependency labeling accuracy.
> 
> In general, one can observe different range of gains of the models across languages. In terms of uas, the differences between single-task and mtl models span between INLINEFORM0 (Basque) and INLINEFORM1 (Hebrew); for las, INLINEFORM2 and INLINEFORM3 (both for Hebrew); and for F1, INLINEFORM4 (Hebrew) and INLINEFORM5 (Korean). Since the sequence labeling encoding used for dependency parsing heavily relies on PoS tags, the result for a given language can be dependent on the degree of the granularity of its PoS tags.
> 
> In addition, Table TABREF19 provides a comparison of the d-mtl-aux models for dependency and constituency parsing against existing models on the PTB test set. Tables TABREF20 and TABREF21 shows the results for various existing models on the SPMRL test sets.
> 
> Table TABREF22 shows the speeds (sentences/second) on a single core of a CPU. The d-mtl setup comes at almost no added computational cost, so the very good speed-accuracy tradeoff already provided by the single-task models is improved.

### Relevance

Label: 

## Record 0953

Paper: Sequence Labeling Parsing by Learning Across Representations

### Question

> Which dataset do they use?

### Passage

> Constituency BIBREF0 and dependency grammars BIBREF1 , BIBREF2 are the two main abstractions for representing the syntactic structure of a given sentence, and each of them has its own particularities BIBREF3 . While in constituency parsing the structure of sentences is abstracted as a phrase-structure tree (see Figure FIGREF6 ), in dependency parsing the tree encodes binary syntactic relations between pairs of words (see Figure FIGREF6 ).
> 
> When it comes to developing natural language processing (nlp) parsers, these two tasks are usually considered as disjoint tasks, and their improvements therefore have been obtained separately BIBREF4 , BIBREF5 , BIBREF6 , BIBREF7 , BIBREF8 , BIBREF9 .
> 
> Despite the potential benefits of learning across representations, there have been few attempts in the literature to do this. klein2003fast considered a factored model that provides separate methods for phrase-structure and lexical dependency trees and combined them to obtain optimal parses. With a similar aim, ren2013combine first compute the n best constituency trees using a probabilistic context-free grammar, convert those into dependency trees using a dependency model, compute a probability score for each of them, and finally rerank the most plausible trees based on both scores. However, these methods are complex and intended for statistical parsers. Instead, we propose a extremely simple framework to learn across constituency and dependency representations.

### Relevance

Label: 

## Record 0954

Paper: Sequence Labeling Parsing by Learning Across Representations

### Question

> Which dataset do they use?

### Passage

> In the following experiments we use two parallel datasets that provide syntactic analyses for both dependency and constituency parsing.
> 
> For the evaluation on English language we use the English Penn Treebank BIBREF40 , transformed into Stanford dependencies BIBREF41 with the predicted PoS tags as in BIBREF32 .
> 
> We also use the spmrl datasets, a collection of parallel dependency and constituency treebanks for morphologically rich languages BIBREF42 . In this case, we use the predicted PoS tags provided by the organizers. We observed some differences between the constituency and dependency predicted input features provided with the corpora. For experiments where dependency parsing is the main task, we use the input from the dependency file, and the converse for constituency, for comparability with other work. d-mtl models were trained twice (one for each input), and dependency and constituent scores are reported on the model trained on the corresponding input.
> 
> We use bracketing F-score from the original evalb and eval_spmrl official scripts to evaluate constituency trees. For dependency parsing, we rely on las and uas scores where punctuation is excluded in order to provide a homogeneous setup for PTB and SPMRL.

### Relevance

Label: 

## Record 0955

Paper: Sequence Labeling Parsing by Learning Across Representations

### Question

> Which dataset do they use?

### Passage

> We test different sequence labeling parsers to determine whether there are any benefits in learning across representations. We compare: (i) a single-task model for constituency parsing and another one for dependency parsing, (ii) a multi-task model for constituency parsing (and another for dependency parsing) where each element of the 3-tuple is predicted as a partial label in a separate subtask instead of as a whole, (iii) different mtl models where the partial labels from a specific parsing abstraction are used as auxiliary tasks for the other one, and (iv) an mtl model that learns to produce both abstractions as main tasks.
> 
> For constituency parsing, we use the single-task model by BIBREF10 . The input is the raw sentence and the output for each token a single label of the form INLINEFORM0 = INLINEFORM1 . For dependency parsing we use the model by BIBREF11 to predict a single dependency label of the form INLINEFORM2 = INLINEFORM3 for each token.
> 
> For constituency parsing, instead of predicting a single label output of the form INLINEFORM0 , we generate three partial and separate labels INLINEFORM1 , INLINEFORM2 and INLINEFORM3 through three task-dependent feed-forward networks on the top of the stacked bilstms. This is similar to BIBREF28 . For dependency parsing, we propose in this work a mtl version too. We observed in preliminary experiments, as shown in Table TABREF14 , that casting the problem as 3-task learning led to worse results. Instead, we cast it as a 2-task learning problem, where the first task consists in predicting the head of a word INLINEFORM4 , i.e. predicting the tuple INLINEFORM5 , and the second task predicts the type of the relation INLINEFORM6 . The loss is here computed as INLINEFORM7 = INLINEFORM8 , where INLINEFORM9 is the partial loss coming from the subtask INLINEFORM10 .
> 
> We predict the partial labels from one of the parsing abstractions as main tasks. The partial labels from the other parsing paradigm are used as auxiliary tasks. The loss is computed as INLINEFORM0 = INLINEFORM1 , where INLINEFORM2 is an auxiliary loss and INLINEFORM3 its specific weighting factor. Figure FIGREF17 shows the architecture used in this and the following multi-paradigm model.
> 
> All tasks are learned

### Relevance

Label: 

## Record 0956

Paper: Extracting clinical concepts from user queries

### Question

> where did they obtain the annotated clinical notes from?

### Passage

> task in 2010 i2b2/VA defines three types of entities: “problem”, “treatment”, and “test”. The CE task in 2013 ShARe/CLEF defines various types of disorder such as “injury or poisoning”, "disease or syndrome”, etc. In addition to tagging, the CE task in 2013 ShARe/CLEF has an encoding component which requires selecting one and only one Concept Unique Identifier (CUI) from Systematized Nomenclature Of Medicine Clinical Terms (SNOMED-CT) for each disorder entity tagged. Our problem, similar to the CE task in 2013 ShARe/CLEF, also contains two sub-problems: tagging mentions of entities of interest (entity tagging), and selecting appropriate terms from a glossary to match the mentions (term matching). However, several major differences exist. First, compared to clinical notes, the user queries are much shorter, less technical, and often less coherent. Second, instead of encoding, we are dealing with term matching where we rank a few best terms that match an entity, instead of selecting only one. This is because the users who type the queries may not have a clear idea about what they are looking for, or could be laymen who know little terminology, it may be more helpful to provide a set of likely results and let the users choose. Third, the types of entities are different. Each medical search engine may have its own types of entities to tag. There is also one minor difference in the tagging scheme between our problem and the CE task in 2013 ShARe/CLEF - We limit our scope to dealing with entities of consecutive words and not disjoint entities . We use only Beginning, Inside, Outside (BIO) tags. Given the differences listed above, we need to customize a framework consisting of an entity tagging and term matching component for our CE problem.

### Relevance

Label: 

## Record 0957

Paper: Extracting clinical concepts from user queries

### Question

> where did they obtain the annotated clinical notes from?

### Passage

> In most real user queries we sampled, the entities were tagged at the correct boundary and the tagging was complete (such as the ones shown in Figure FIGREF24). Only on a few user queries the tagging was controversial. For example, the query “Erythematous blanching round, oval patches on torso, extremities” was tagged as “Erythematous blanching” and “oval patches on torso”. The entity “extremities” was missing. The segmentation was also not correct. A more appropriate tagging would be “Erythematous blanching round, oval patches”, “torso”, and “extremities”. The tagging could be further improved by synthesizing more realistic user queries. Recall that the synthesized user queries were created by randomly combining terminologies from the dermatology glossary, which, while providing data that helped the model learn entity segmentation, did not reflect the co-occurrence information in real user queries. For example, there could be two clinical entities that often co-occur or never co-occur in a user query. But since the synthesized user queries we used combined terms randomly, the co-occurrence information was thus missing.
> 
> The final retrieval results of our framework were not evaluated quantitatively in terms of recall and precision, due the the lack of ground truth. When ground truth becomes available, we will be able to evaluate our framework more thoroughly. Recently, a fine-tuned BERT model in the medical domain called BioBERT BIBREF17 has attracted some attention in the medical NLP domain. We could experiment with BioBERT embeddings in the future. We could also include query expansion technique for term matching. When finding candidate terms for an entity, our first step was still based on string matching. Given that there might be multiple entities that could be matched to the same term, it could be hard to include all these entities in the glossary and hard to match terms to these entities.

### Relevance

Label: 

## Record 0958

Paper: Extracting clinical concepts from user queries

### Question

> where did they obtain the annotated clinical notes from?

### Passage

> FIGREF10), is given by
> 
> where $ELMo(C_i|C)$ and $ELMo(E_j|E)$ are the ELMo embeddings for the word $C_i$ and $E_j$, respectively. The ELMo embeddings have the same dimension for all words when using the same fine-tuned ELMo model. Thus, we can use a distance function (e.g., the cosine distance), denoted $d(\cdot )$ in equation DISPLAY_FORM13, to compute the semantic similarity between words. In step 2, we calculate the candidate-entity relevance score (similarity) using the formula
> 
> where $s_c$ is a score threshold, and $\mathbb {I} \lbrace max(\vec{S_i}) > s_c\rbrace $ is an indicator function that equals 1 if $max(\vec{S_i}) > s_c$ or equals 0 if not. In equation DISPLAY_FORM14 we define a metric that measures “information coverage” of the candidate terms with respect to a tagged entity. If the constituent words of a candidate term are relevant to the constituent words in the tagged entity, then the candidate term offers more information coverage. Intuitively, the more relevant words present in the candidate term, the more relevant the candidate is to the tagged entity. The purpose of the cutoff, $s_c$, is to screen the $(C_i,E_j)$ word pairs that are dissimilar, so that they do not contribute to information coverage. One can adjust the strictness of the entity - terminology matching by adjusting $s_c$. The higher we set $s_c$, the fewer candidate terms will be selected for a tagged entity. A normalization factor, $\frac{1}{m}$, is added to give preference to more concise candidate terms given the same amount of information coverage.
> 
> We need to create an extra stopword list to include words such as “configuration” and “color”, and exclude these words from the word count for a candidate term. This is because the terms associated with the description of color or configuration usually have the word “color” or “configuration” in them. On the other hand, a user query normally does not contain such words. For example, a tagged entity in a user query could be “round yellow patches”, for which the relevant terminologies include “round configuration” and “yellow color”. Since we applied a normalization factor, $\frac{1}{m}$, to the relevance score, the word “color” and “configuration” would lower the relevance score because they do not have a counterpart in the tagged

### Relevance

Label: 

## Record 0959

Paper: Extracting clinical concepts from user queries

### Question

> where did they obtain the annotated clinical notes from?

### Passage

> Despite the greater similarity between our task and the 2013 ShARe/CLEF Task 1, we use the clinical notes from the CE task in 2010 i2b2/VA on account of 1) the data from 2010 i2b2/VA being easier to access and parse, 2) 2013 ShARe/CLEF containing disjoint entities and hence requiring more complicated tagging schemes. The synthesized user queries are generated using the aforementioned dermatology glossary. Tagged sentences are extracted from the clinical notes. Sentences with no clinical entity present are ignored. 22,489 tagged sentences are extracted from the clinical notes. We will refer to these tagged sentences interchangeably as the i2b2 data. The sentences are shuffled and split into train/dev/test set with a ratio of 7:2:1. The synthesized user queries are composed by randomly selecting several clinical terms from the dermatology glossary and then combining them in no particular order. When combining the clinical terms, we attach the BIO tags to their constituent words. The synthesized user queries (13,697 in total) are then split into train/dev/test set with the same ratio. Next, each set in the i2b2 data and the corresponding set in the synthesized query data are combined to form a hybrid train/dev/test set, respectively. This way we ensure that in each hybrid train/dev/test set, the ratio between the i2b2 data and the synthesized query data is the same.
> 
> The reason for combining the two data is their drastic structural difference (See figure FIGREF16 for an example). Previously, when trained on the i2b2 data only, the BiLSTM-CRF model was not able to segment clinical entities at the correct boundary. It would fail to recognize the user query in Figure FIGREF16(a) as four separate entities. On the other hand, if the model was trained solely on the synthesized user queries, we could imagine that it would fail miserably on any queries that resemble the sentence in Figure FIGREF16(b) because the model would have never seen an “O” tag in the training data. Therefore, it is necessary to use the hybrid training data containing both the i2b2 data and the synthesized user queries.
> 
> To make the hybrid training data, we need to unify the tags. Recall that in Section SECREF1 we point out that the tags are

### Relevance

Label: 

## Record 0960

Paper: Extracting clinical concepts from user queries

### Question

> where did they obtain the annotated clinical notes from?

### Passage

> From the hyperparameter tuning we found that the best combination was
> 
> embeddings: “ELMo on pubmed”,
> 
> hidden_size: 256,
> 
> learning_rate: 0.05,
> 
> mini_batch_size: 32.
> 
> With the above hyperparameter setting, the hybrid NER model achieved a F1 score of $0.995$ on synthesized queries and $0.948$ on clinical notes while the i2b2 NER model achieved a F1 score of $0.441$ on synthesized queries and $0.927$ on clinical notes (See Table TABREF23).
> 
> Since there was no ground truth available for the retrieved terms, we randomly picked a few samples to assess its performance. Some example outputs of our complete framework on real user queries are shown in Figure FIGREF24. For example, from the figure we see that the query "child fever double vision dizzy" was correctly tagged with four entities: "child", "fever", "double vision", and "dizzy". A list of terms from our glossary was matched to each entity. In real world application, the lists of terms will be presented to the user as the retrieval results to their queries.

### Relevance

Label: 

## Record 0961

Paper: Short Text Language Identification for Under Resourced Languages

### Question

> What is the approach of previous work?

### Passage

> BIBREF13, BIBREF14, SVMs BIBREF15 and similar models work very well for doing LID. The DSL 2017 paper BIBREF1, for example, gives an overview of the solutions of all of the teams that competed on the shared task and the winning approach BIBREF16 used an SVM with character n-gram, parts of speech tag features and some other engineered features. The winning approach for DSL 2015 used an ensemble naive Bayes classifier. The fasttext classifier BIBREF17 is perhaps one of the best known efficient 'shallow' text classifiers that have been used for LID .
> 
> Multiple papers have proposed hierarchical stacked classifiers (including lexicons) that would for example first classify a piece of text by language group and then by exact language BIBREF18, BIBREF19, BIBREF8, BIBREF0. Some work has also been done on classifying surnames between Tshivenda, Xitsonga and Sepedi BIBREF20. Additionally, data augmentation BIBREF21 and adversarial training BIBREF22 approaches are potentially very useful to reduce the requirement for data.
> 
> Researchers have investigated deeper LID models like bidirectional recurrent neural networks BIBREF23 or ensembles of recurrent neural networks BIBREF24. The latter is reported to achieve 95.12% in the DSL 2015 shared task. In these models text features can include character and word n-grams as well as informative character and word-level features learnt BIBREF25 from the training data. The neural methods seem to work well in tasks where more training data is available.
> 
> In summary, LID of short texts, informal styles and similar languages remains a difficult problem which is actively being researched. Increased confusion can in general be expected between shorter pieces of text and languages that are more closely related. Shallow methods still seem to work well compared to deeper models for LID. Other remaining research opportunities seem to be data harvesting, building standardised datasets and creating shared tasks for South Africa and Africa. Support for language codes that include more languages seems to be growing and discoverability of research is improving with more survey papers coming out. Paywalls also seem to no longer be a problem; the references used in this paper was either openly published or available as preprint papers.

### Relevance

Label: 

## Record 0962

Paper: Short Text Language Identification for Under Resourced Languages

### Question

> What is the approach of previous work?

### Passage

> Accurate language identification (LID) is the first step in many natural language processing and machine comprehension pipelines. If the language of a piece of text is known then the appropriate downstream models like parts of speech taggers and language models can be applied as required.
> 
> LID is further also an important step in harvesting scarce language resources. Harvested data can be used to bootstrap more accurate LID models and in doing so continually improve the quality of the harvested data. Availability of data is still one of the big roadblocks for applying data driven approaches like supervised machine learning in developing countries.
> 
> Having 11 official languages of South Africa has lead to initiatives (discussed in the next section) that have had positive effect on the availability of language resources for research. However, many of the South African languages are still under resourced from the point of view of building data driven models for machine comprehension and process automation.
> 
> Table TABREF2 shows the percentages of first language speakers for each of the official languages of South Africa. These are four conjunctively written Nguni languages (zul, xho, nbl, ssw), Afrikaans (afr) and English (eng), three disjunctively written Sotho languages (nso, sot, tsn), as well as tshiVenda (ven) and Xitsonga (tso). The Nguni languages are similar to each other and harder to distinguish. The same is true of the Sotho languages.
> 
> This paper presents a hierarchical naive Bayesian and lexicon based classifier for LID of short pieces of text of 15-20 characters long. The algorithm is evaluated against recent approaches using existing test sets from previous works on South African languages as well as the Discriminating between Similar Languages (DSL) 2015 and 2017 shared tasks.
> 
> Section SECREF2 reviews existing works on the topic and summarises the remaining research problems. Section SECREF3 of the paper discusses the proposed algorithm and Section SECREF4 presents comparative results.

### Relevance

Label: 

## Record 0963

Paper: Short Text Language Identification for Under Resourced Languages

### Question

> What is the approach of previous work?

### Passage

> The proposed LID algorithm builds on the work in BIBREF8 and BIBREF26. We apply a naive Bayesian classifier with character (2, 4 & 6)-grams, word unigram and word bigram features with a hierarchical lexicon based classifier.
> 
> The naive Bayesian classifier is trained to predict the specific language label of a piece of text, but used to first classify text as belonging to either the Nguni family, the Sotho family, English, Afrikaans, Xitsonga or Tshivenda. The scikit-learn multinomial naive Bayes classifier is used for the implementation with an alpha smoothing value of 0.01 and hashed text features.
> 
> The lexicon based classifier is then used to predict the specific language within a language group. For the South African languages this is done for the Nguni and Sotho groups. If the lexicon prediction of the specific language has high confidence then its result is used as the final label else the naive Bayesian classifier's specific language prediction is used as the final result. The lexicon is built over all the data and therefore includes the vocabulary from both the training and testing sets.
> 
> The lexicon based classifier is designed to trade higher precision for lower recall. The proposed implementation is considered confident if the number of words from the winning language is at least one more than the number of words considered to be from the language scored in second place.
> 
> The stacked classifier is tested against three public LID implementations BIBREF17, BIBREF23, BIBREF8. The LID implementation described in BIBREF17 is available on GitHub and is trained and tested according to a post on the fasttext blog. Character (5-6)-gram features with 16 dimensional vectors worked the best. The implementation discussed in BIBREF23 is available from https://github.com/tomkocmi/LanideNN. Following the instructions for an OSX pip install of an old r0.8 release of TensorFlow, the LanideNN code could be executed in Python 3.7.4. Settings were left at their defaults and a learning rate of 0.001 was used followed by a refinement with learning rate of 0.0001. Only one code modification was applied to return the results from a method that previously just printed to screen. The LID algorithm described in BIBREF8 is also available on GitHub.
> 
> The stacked classifier is also

### Relevance

Label: 

## Record 0964

Paper: Short Text Language Identification for Under Resourced Languages

### Question

> What is the approach of previous work?

### Passage

> The focus of this section is on recently published datasets and LID research applicable to the South African context. An in depth survey of algorithms, features, datasets, shared tasks and evaluation methods may be found in BIBREF0.
> 
> The datasets for the DSL 2015 & DSL 2017 shared tasks BIBREF1 are often used in LID benchmarks and also available on Kaggle . The DSL datasets, like other LID datasets, consists of text sentences labelled by language. The 2017 dataset, for example, contains 14 languages over 6 language groups with 18000 training samples and 1000 testing samples per language.
> 
> The recently published JW300 parallel corpus BIBREF2 covers over 300 languages with around 100 thousand parallel sentences per language pair on average. In South Africa, a multilingual corpus of academic texts produced by university students with different mother tongues is being developed BIBREF3. The WiLI-2018 benchmark dataset BIBREF4 for monolingual written natural language identification includes around 1000 paragraphs of 235 languages. A possibly useful link can also be made BIBREF5 between Native Language Identification (NLI) (determining the native language of the author of a text) and Language Variety Identification (LVI) (classification of different varieties of a single language) which opens up more datasets. The Leipzig Corpora Collection BIBREF6, the Universal Declaration of Human Rights and Tatoeba are also often used sources of data.
> 
> The NCHLT text corpora BIBREF7 is likely a good starting point for a shared LID task dataset for the South African languages BIBREF8. The NCHLT text corpora contains enough data to have 3500 training samples and 600 testing samples of 300+ character sentences per language. Researchers have recently started applying existing algorithms for tasks like neural machine translation in earnest to such South African language datasets BIBREF9.
> 
> Existing NLP datasets, models and services BIBREF10 are available for South African languages. These include an LID algorithm BIBREF11 that uses a character level n-gram language model. Multiple papers have shown that 'shallow' naive Bayes classifiers BIBREF12, BIBREF8, BIBREF13, BIBREF14, SVMs BIBREF15 and similar models work very well for doing LID. The DSL 2017 paper BIBREF1, for example, gives an overview of the solutions of all of the teams that competed on the shared task and the winning

### Relevance

Label: 

## Record 0965

Paper: Short Text Language Identification for Under Resourced Languages

### Question

> What is the approach of previous work?

### Passage

> The average classification accuracy results are summarised in Table TABREF9. The accuracies reported are for classifying a piece of text by its specific language label. Classifying text only by language group or family is a much easier task as reported in BIBREF8.
> 
> Different variations of the proposed classifier were evaluated. A single NB classifier (NB), a stack of two NB classifiers (NB+NB), a stack of a NB classifier and lexicon (NB+Lex) and a lexicon (Lex) by itself. A lexicon with a 50% training token dropout is also listed to show the impact of the lexicon support on the accuracy.
> 
> From the results it seems that the DSL 2017 task might be harder than the DSL 2015 and NCHLT tasks. Also, the results for the implementation discussed in BIBREF23 might seem low, but the results reported in that paper is generated on longer pieces of text so lower scores on the shorter pieces of text derived from the NCHLT corpora is expected.
> 
> The accuracy of the proposed algorithm seems to be dependent on the support of the lexicon. Without a good lexicon a non-stacked naive Bayesian classifier might even perform better.
> 
> The execution performance of some of the LID implementations are shown in Table TABREF10. Results were generated on an early 2015 13-inch Retina MacBook Pro with a 2.9 GHz CPU (Turbo Boosted to 3.4 GHz) and 8GB RAM. The C++ implementation in BIBREF17 is the fastest. The implementation in BIBREF8 makes use of un-hashed feature representations which causes it to be slower than the proposed sklearn implementation. The execution performance of BIBREF23 might improve by a factor of five to ten when executed on a GPU.

### Relevance

Label: 

## Record 0966

Paper: Code-Switching Language Modeling using Syntax-Aware Multi-Task Learning

### Question

> What languages are explored in the work?

### Passage

> The earliest language modeling research on code-switching data was applying linguistic theories on computational modelings such as Inversion Constraints and Functional Head Constraints on Chinese-English code-switching data BIBREF9 , BIBREF10 . BIBREF11 built a bilingual language model which is trained by interpolating two monolingual language models with statistical machine translation (SMT) based text generation to generate artificial code-switching text. BIBREF12 , BIBREF13 introduced a class-based method using RNNLM for computing the posterior probability and added POS tags in the input. BIBREF14 explored the combination of brown word clusters, open class words, and clusters of open class word embeddings as hand-crafted features for improving the factored language model. In addition, BIBREF15 proposed a generative language modeling with explicit phrase structure. A method of tying input and output embedding helped to reduce the number of parameters in language model and improved the perplexity BIBREF16 .
> 
> Learning multiple NLP tasks using multi-task learning have been recently used in many domains BIBREF17 , BIBREF18 , BIBREF19 . They presented a joint many-task model to handle multiple NLP tasks and share parameters with growing depth in a single end-to-end model. A work by BIBREF20 showed the potential of combining POS tagging with Named-Entity Recognition task.

### Relevance

Label: 

## Record 0967

Paper: Code-Switching Language Modeling using Syntax-Aware Multi-Task Learning

### Question

> What languages are explored in the work?

### Passage

> In the model, word lexicons and syntactic features are used as input.
> 
> Word Lexicons: Sentences are encoded as 1-hot vectors and our vocabulary is built from training data.
> 
> Syntactic Features: For each language island, phrase within the same language, we extract POS Tags iteratively using Chinese and English Penn Tree Bank Parser BIBREF21 , BIBREF22 . There are 31 English POS Tags and 34 Chinese POS Tags. Chinese words are distinguishable from English words since they have different encoding. We add language information in the POS tag label to discriminate POS tag between two languages.

### Relevance

Label: 

## Record 0968

Paper: Code-Switching Language Modeling using Syntax-Aware Multi-Task Learning

### Question

> What languages are explored in the work?

### Passage

> Code-switching has received a lot of attention from speech and computational linguistic communities especially on how to automatically recognize text from speech and understand the structure within it. This phenomenon is very common in bilingual and multilingual communities. For decades, linguists studied this phenomenon and found that speakers switch at certain points, not randomly and obeys several constraints which point to the code-switched position in an utterance BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 , BIBREF4 . These hypotheses have been empirically proven by observing that bilinguals tend to code-switch intra-sententially at certain (morpho)-syntactic boundaries BIBREF5 . BIBREF1 defined the well-known theory that constraints the code-switch between a functional head and its complement is given the strong relationship between the two constituents, which corresponds to a hierarchical structure in terms of Part-of-Speech (POS) tags. BIBREF3 introduced Matrix-Language Model Framework for an intra-sentential case where the primary language is called Matrix Language and the second one called Embedded Language BIBREF2 . A language island was then introduced which is a constituent composed entirely of the language morphemes. From the Matrix-Language Frame Model, both matrix language (ML) island and embedded language (EL) islands are well-formed in their grammars and the EL islands are constrained under ML grammar BIBREF6 . BIBREF7 studied determiner–noun switches in Spanish–English bilinguals .
> 
> Code-switching can be classified into two categories: intra-sentential and inter-sentential switches BIBREF0 . Intra-sentential switch defines a shift from one language to another language within an utterance. Inter-sentential switch refers to the change between two languages in a single discourse, where the switching occurs after a sentence in the first language has been completed and the next sentence starts with a new language. The example of the intra-sentential switch is shown in (1), and the inter-sentential switch is shown in (2).
> 
> Language modeling using only word lexicons is not adequate to learn the complexity of code-switching patterns, especially in a low resource setting. Learning at the same time syntactic features such as POS tag and language identifier allows to have a shared grammatical information that constraint the next word prediction. Due to this reason, we propose a multi-task learning framework for code-switching language modeling task which is able to leverage

### Relevance

Label: 

## Record 0969

Paper: Code-Switching Language Modeling using Syntax-Aware Multi-Task Learning

### Question

> What languages are explored in the work?

### Passage

> This work is partially funded by ITS/319/16FP of the Innovation Technology Commission, HKUST 16214415 & 16248016 of Hong Kong Research Grants Council, and RDC 1718050-0 of EMOS.AI.

### Relevance

Label: 

## Record 0970

Paper: Code-Switching Language Modeling using Syntax-Aware Multi-Task Learning

### Question

> What languages are explored in the work?

### Passage

> faFigure FIGREF7 illustrates our multi-task learning extension to recurrent language model. In this multi-task learning setting, the tasks are language modeling and POS tagging. The POS tagging task shares the POS tag vector and the hidden states to LM task, but it does not receive any information from the other loss. Let INLINEFORM0 be the word lexicon in the document and INLINEFORM1 be the POS tag of the corresponding INLINEFORM2 at index INLINEFORM3 . They are mapped into embedding matrices to get their INLINEFORM4 -dimensional vector representations INLINEFORM5 and INLINEFORM6 . The input embedding weights are tied with the output weights. We concatenate INLINEFORM7 and INLINEFORM8 as the input of INLINEFORM9 . The information from the POS tag sequence is shared to the language model through this step. INLINEFORM10 INLINEFORM11
> 
> where INLINEFORM0 denotes the concatenation operator, INLINEFORM1 and INLINEFORM2 are the final hidden states of INLINEFORM3 and INLINEFORM4 respectively. INLINEFORM5 and INLINEFORM6 , the hidden states from both LSTMs are summed before predicting the next word. INLINEFORM7 INLINEFORM8
> 
> The word distribution of the next word INLINEFORM0 is normalized using softmax function. The model uses cross-entropy losses as error functions INLINEFORM1 and INLINEFORM2 for language modeling task and POS tagging task respectively. We optimize the multi-objective losses using the Back Propagation algorithm and we perform a weighted linear sum of the losses for each individual task. INLINEFORM3
> 
> where INLINEFORM0 is the weight of the loss in the training.

### Relevance

Label: 

## Record 0971

Paper: Named Entity Recognition on Twitter for Turkish using Semi-supervised Learning with Word Embeddings

### Question

> What data was used to build the word embeddings?

### Passage

> In the unsupervised stage, we used two types of unlabeled data to obtain Turkish word embeddings. The first one is a Turkish news-web corpus containing 423M words and 491M tokens, namely the BOUN Web Corpus BIBREF9 , BIBREF10 . The second one is composed of 21M Turkish tweets with 241M words and 293M tokens, where we combined 1M tweets from TS TweetS by Sezer-2013 and 20M Turkish Tweets by Bolat and Amasyalı.
> 
> We applied tokenization on both Turkish news-web corpus and Turkish tweets corpus using the publicly available Zemberek tool developed for Turkish. We have also applied lower-casing on both corpora in order to limit the number of unique words. Since our combined tweets corpus is composed of Twitter-specific texts, we applied what we call Twitter processing where we replaced mentions, hashtags, smileys and URLs with certain keywords.

### Relevance

Label: 

## Record 0972

Paper: Named Entity Recognition on Twitter for Turkish using Semi-supervised Learning with Word Embeddings

### Question

> What data was used to build the word embeddings?

### Passage

> Most of our NER models are trained on annotated Turkish news data by Tur-2003 and tested on tweets, due to the limited amount of annotated Turkish tweets.
> 
> In addition to using TwitterDS-1 and TwitterDS-2 as test sets, we detected 291 completely non-Turkish tweets out of 5040 in TwitterDS-1 and filtered them out using the isTurkish tool BIBREF13 to obtain TwitterDS-1_FT. We also used the normalized versions of these data sets. As shown in Table TABREF23 , turning off the capitalization feature is better when text normalization is not applied (bold entries), but the best results are achieved when normalization is applied and the capitalization feature is used (underlined bold entries). To observe the effects of the type of the source text used to learn the word embeddings, we have three models as Web, Twt, and Web+Twt where we used the Turkish web corpus, tweet corpus, and their combination respectively to learn the word embeddings. Including in-domain data from a relatively smaller tweet corpus together with a larger web corpus yields in better Twitter NER performance.
> 
> We examined the effects of word embeddings on the performance of our NER models, and compared them to the improvements achieved by applying normalization on Turkish tweets. The baseline NER model is built by using the features explained in section 3.2, except the capitalization and word embeddings features. Using word embeddings obtained with unsupervised learning from a large corpus of web articles and tweets results in better NER performance than applying a Twitter-specific text normalizer, as shown in Table TABREF26 . This is crucial since Turkish text normalization for unstructured data is a challenging task and requires successful morphological analysis, whereas extracting word embeddings for any language or domain is much easier, yet more effective.

### Relevance

Label: 

## Record 0973

Paper: Named Entity Recognition on Twitter for Turkish using Semi-supervised Learning with Word Embeddings

### Question

> What data was used to build the word embeddings?

### Passage

> the performance drops to F-score of 19.28% when this system is adopted to Twitter data BIBREF4 .
> 
> There are several challenges for NER on tweets, which are also summarized in Kucuk-2014-1, due to the very short text length and informal structure of the language used. Missing proper grammar rules and punctuation, lack of capitalization and apostrophes, usage of hashtags, abbreviations, and slang words are some of those challenges. In Twitter, using contracted forms and metonymic expressions instead of full organization or location names is very common as well. The usage of non-diacritic characters and the limited annotated data bring additional challenges for processing Turkish tweets.
> 
> Due to the dynamic language used in Twitter, heavy feature engineering is not feasible for Twitter NER. Demir-2014 developed a semi-supervised approach for Turkish NER on formal (newswire) text using word embeddings obtained from unlabeled data. They obtained promising results without using any gazetteers and language dependent features. We adopted this approach for informal texts and evaluated it on Turkish tweets, where we achieved the state-of-the-art F-score performance. Our results show that using word embeddings for Twitter NER in Turkish can result in better F-score performance compared to using text normalization as a pre-processing step. In addition, utilizing in-domain word embeddings can be a promising approach for Twitter NER.

### Relevance

Label: 

## Record 0974

Paper: Named Entity Recognition on Twitter for Turkish using Semi-supervised Learning with Word Embeddings

### Question

> What data was used to build the word embeddings?

### Passage

> We designed a number of experimental settings to investigate their effects on Turkish Twitter NER. These settings are as follows: the text type of annotated data used for training, the text type of unlabeled data used to learn the word embeddings, using the capitalization feature or not, and applying text normalization. We evaluated all models on ENAMEX types with the CoNLL metric and reported phrase-level overall F-score performance results. To be more precise, the F-score values presented in Table TABREF23 , Table TABREF26 and Table TABREF27 are micro-averaged over the classes using the strict metric.

### Relevance

Label: 

## Record 0975

Paper: Named Entity Recognition on Twitter for Turkish using Semi-supervised Learning with Word Embeddings

### Question

> What data was used to build the word embeddings?

### Passage

> We adopted a neural networks based semi-supervised approach using word embeddings for the NER task on Turkish tweets. At the first stage, we attained distributed representations of words by employing a fast unsupervised learning method on a large unlabeled corpus. At the second stage, we exploited these word embeddings together with language independent features in order to train our neural network on labeled data. We compared our results on two different Turkish Twitter data sets with the state-of-the-art NER systems proposed for Twitter data in Turkish and showed that our system outperforms the state-of-the-art results on both data sets. Our results also show that using word embeddings from an unlabeled corpus can lead to better performance than applying Twitter-specific text normalization. We discussed the promising benefits of using in-domain data to learn word embeddings at the unsupervised stage as well. Since the only language dependent part of our Turkish Twitter NER system is text normalization, and since even without text normalization it outperforms the previous state-of-the-art results, we believe that our approach can be adapted to other morphologically rich languages. Our Turkish Twitter NER system, namely TTNER, is publicly available.
> 
> We believe that there is still room for improvement for NLP tasks on Turkish social media data. As a future work, we aim to construct a much larger in-domain resource, i.e., unlabeled Turkish tweets corpus, and investigate the full benefits of attaining word embeddings from in-domain data on Twitter NER.

### Relevance

Label: 

## Record 0976

Paper: Crowdsourcing a High-Quality Gold Standard for QA-SRL

### Question

> How much more coverage is in the new dataset?

### Passage

> We introduced a refined crowdsourcing pipeline and a corresponding evaluation methodology for QA-SRL. It enabled us to release a new gold standard for evaluations, notably of much higher coverage of core and implied roles than the previous Dense evaluation dataset. We believe that our annotation methodology and dataset would facilitate future research on natural semantic annotations and QA-SRL parsing.

### Relevance

Label: 

## Record 0977

Paper: Crowdsourcing a High-Quality Gold Standard for QA-SRL

### Question

> How much more coverage is in the new dataset?

### Passage

> Semantic Role Labeling (SRL) provides explicit annotation of predicate-argument relations, which have been found useful in various downstream tasks BIBREF0, BIBREF1, BIBREF2, BIBREF3. Question-Answer driven Semantic Role Labeling (QA-SRL) BIBREF4 is an SRL scheme in which roles are captured by natural language questions, while arguments represent their answers, making the annotations intuitive, semantically rich, and easily attainable by laymen. For example, in Table TABREF4, the question Who cut something captures the traditional “agent” role.
> 
> Previous attempts to annotate QA-SRL initially involved trained annotators BIBREF4 but later resorted to crowdsourcing BIBREF5 to achieve scalability. Naturally, employing crowd workers raises challenges when annotating semantic structures like SRL. As BIBREF5 acknowledged, the main shortage of the large-scale 2018 dataset is the lack of recall, estimated by experts to be in the lower 70s.
> 
> In light of this and other annotation inconsistencies, we propose an improved QA-SRL crowdsourcing protocol for high-quality annotation, allowing for substantially more reliable performance evaluation of QA-SRL parsers. To address worker quality, we systematically screen workers, provide concise yet effective guidelines, and perform a short training procedure, all within a crowd-sourcing platform. To address coverage, we employ two independent workers plus an additional one for consolidation — similar to conventional expert-annotation practices. In addition to yielding 25% more roles, our coverage gain is demonstrated by evaluating against expertly annotated data and comparison with PropBank (Section SECREF4). To foster future research, we release an assessed high-quality gold dataset along with our reproducible protocol and evaluation scheme, and report the performance of the existing parser BIBREF5 as a baseline.

### Relevance

Label: 

## Record 0978

Paper: Crowdsourcing a High-Quality Gold Standard for QA-SRL

### Question

> How much more coverage is in the new dataset?

### Passage

> To illustrate the effectiveness of our new gold-standard, we use its Wikinews development set to evaluate the currently available parser from BIBREF5. For each predicate, the parser classifies every span for being an argument, independently of the other spans. Unlike many other SRL systems, this policy often produces outputs with redundant arguments (see appendix for examples). Results for 1200 predicates are reported in Table TABREF23, demonstrating reasonable performance along with substantial room for improvement, especially with respect to coverage. As expected, the parser's recall against our gold is substantially lower than the 84.2 recall reported in BIBREF5 against Dense, due to the limited recall of Dense relative to our gold set.

### Relevance

Label: 

## Record 0979

Paper: Crowdsourcing a High-Quality Gold Standard for QA-SRL

### Question

> How much more coverage is in the new dataset?

### Passage

> It is illuminating to observe the agreement between QA-SRL and PropBank (CoNLL-2009) annotations BIBREF7. In Table TABREF22, we replicate the experiments in BIBREF4 for both our gold set and theirs, over a sample of 200 sentences from Wall Street Journal (agreement evaluation is automatic and the metric is somewhat similar to our UA). We report macro-averaged (over predicates) precision and recall for all roles, including core and adjuncts, while considering the PropBank data as the reference set. Our recall of the PropBank roles is notably high, reconfirming the coverage obtained by our annotation protocol.
> 
> The measured precision with respect to PropBank is low for adjuncts due to the fact that our annotators were capturing many correct arguments not covered in PropBank. To examine this, we analyzed 100 false positive arguments. Only 32 of those were due to wrong or incomplete QA annotations in our gold, while most others were outside of PropBank's scope, capturing either implied arguments or roles not covered in PropBank. Extrapolating from this manual analysis estimates our true precision (on all roles) to be about 91%, which is consistent with the 88% precision figure in Table TABREF19. Compared with 2015, our QA-SRL gold yielded 1593 annotations, with 989 core and 604 adjuncts, while theirs yielded 1315 annotations, 979 core and 336 adjuncts. Overall, the comparison to PropBank reinforces the quality of our gold dataset and shows its better coverage relative to the 2015 dataset.

### Relevance

Label: 

## Record 0980

Paper: Crowdsourcing a High-Quality Gold Standard for QA-SRL

### Question

> How much more coverage is in the new dataset?

### Passage

> We assess both our gold standard set and the recent Dense set against an integrated expert annotated sample of 100 predicates. To construct the expert set, we blindly merged the Dense set with our worker annotations and manually corrected them. We further corrected the evaluation decisions, accounting for some automatic evaluation mistakes introduced by the span-matching and question paraphrasing criteria. As seen in Table TABREF19, our gold set yields comparable precision with significantly higher recall, which is in line with our 25% higher yield.
> 
> Examining disagreements between our gold and Dense, we observe that our workers successfully produced more roles, both implied and explicit. To a lesser extent, they split more arguments into independent answers, as emphasized by our guidelines, an issue which was left under-specified in the previous annotation guidelines.

### Relevance

Label: 

## Record 0981

Paper: EmotionX-IDEA: Emotion BERT -- an Affectional Model for Conversation

### Question

> what datasets were used?

### Passage

> Since the size of both datasets are not large enough for complex neural-based model training as well as BERT model is only pre-train on formal text datasets, the issues of overfitting and domain bias are important considerations for design the pre-training process.
> 
> To avoid our model overfitting on the training data and increase the understanding of informal text, we adapted BERT and derived two models, namely FriendsBERT and ChatBERT, with different pre-training tasks before the formal training process for Friends and EmotionPush dataset, respectively. The pre-training strategies are described below.
> 
> For pre-training FriendsBERT, we collect the completed scripts of all ten seasons of Friends TV shows from emorynlp which includes 3,107 scenes within 61,309 utterances. All the utterances are followed the preprocessing methods mentions above to compose the corpus for Masked language model pre-training task. The consequent utterances in the same scenes are considered as the consequent sentences to pre-train the Next Sentence Prediction task. In the pre-training process, the training loss is the sum of the mean likelihood of two pre-train tasks.
> 
> For pre-training ChatBERT, we pre-train our model on the Twitter dataset, since the text and writing style on Twitter are close to the chat text where both may involved with many informal words or emoticons as well. The Twitter emotion dataset, 8 basic emotions from emotion wheel BIBREF1, was collected by twitter streaming API with specific emotion-related hashtags, such as #anger, #joy, #cry, #sad and etc. The hashtags in tweets are treated as emotion label for model fine-tuning. The tweets were fine-grined processing followed the rules in BIBREF9, BIBREF4, including duplicate tweets removing, the emotion hashtags must appearing in the last position of a tweet, and etc. The statis of tweets were summarized in Table TABREF17. Each tweet and corresponding emotion label composes an emotion classification dataset for pre-training.

### Relevance

Label: 

## Record 0982

Paper: EmotionX-IDEA: Emotion BERT -- an Affectional Model for Conversation

### Question

> what datasets were used?

### Passage

> The main goal of the present work is to predict the emotion of utterance within the dialogue. Following are four major difficulties we concern about:
> 
> The emotion of the utterances depends not only on the text but also on the interaction happened earlier.
> 
> The source of the two datasets are different. Friends is speech-based dialogues and EmotionPush is chat-based dialogues. It makes datasets possess different characteristics.
> 
> There are only $1,000$ dialogues in both training datasets which are not large enough for the stability of training a complex neural-based model.
> 
> The prediction targets (emotion labels) are highly unbalanced.
> 
> The proposed approach is summarized in Figure FIGREF3, which aims to overcome these challenges. The framework could be separated into three steps and described as follow:

### Relevance

Label: 

## Record 0983

Paper: EmotionX-IDEA: Emotion BERT -- an Affectional Model for Conversation

### Question

> what datasets were used?

### Passage

> EmotionLines BIBREF6 is a dialogue dataset composed of two subsets, Friends and EmotionPush, according to the source of the dialogues. The former comes from the scripts of the Friends TV sitcom. The other is made up of Facebook messenger chats. Each subset includes $1,000$ English dialogues, and each dialogue can be further divided into a few consecutive utterances. All the utterances are annotated by five annotators on a crowd-sourcing platform (Amazon Mechanical Turk), and the labeling work is only based on the textual content. Annotator votes for one of the seven emotions, namely Ekman’s six basic emotions BIBREF1, plus the neutral. If none of the emotion gets more than three votes, the utterance will be marked as “non-neutral”.
> 
> For the datasets, there are properties worth additional mentioning. Although Friends and EmotionPush share the same data format, they are quite different in nature. Friends is a speech-based dataset which is annotated dialogues from the TV sitcom. It means most of the utterances are generated by the a few main characters. The personality of a character often affects the way of speaking, and therefore “who is the speaker" might provide extra clues for emotion prediction. In contrast, EmotionPush does not have this trait due to the anonymous mechanism. In addition, features such as typo, hyperlink, and emoji that only appear in chat-based data will need some domain-specific techniques to process.
> 
> Incidentally, the objective of the challenge is to predict the emotion for each utterance. Just, according to EmotionX 2019 specification, there are only four emotions be selected as our label candidates, which are Joy, Sadness, Anger, and Neutral. These emotions will be considered during performance evaluation. The technical detail will also be introduced and discussed in following Section SECREF13 and Section SECREF26.

### Relevance

Label: 

## Record 0984

Paper: EmotionX-IDEA: Emotion BERT -- an Affectional Model for Conversation

### Question

> what datasets were used?

### Passage

> Given a dialogue $D^{(i)}$ which includes sequence of utterances denoted as $D^{(i)}=(u^{(i)}_{1}, u^{(i)}_{2}, ..., u^{(i)}_{n})$, where $i$ is the index in dataset and $n$ is the number of utterances in the given dialogue. In order to conserve the emotional information of both utterance and conversation, we rearrange each two consecutive utterances $u_{t}, u_{t-1}$ into a single sentence representation $x_{t}$ as
> 
> The corresponding sentence representation corpus $X^{(i)}$ are denoted as $X^{(i)}=(x^{(i)}_{1}, x^{(i)}_{2}, ..., x^{(i)}_{n})$. Note that the first utterance within a conversation does not have its causal utterance (previous sentence), therefore, the causal utterance will be set as [None]. A practical example of sentence representation is shown in Table TABREF11.
> 
> Since the characteristics of two datasets are not identical, we customize different causal utterance modeling strategies to refine the information in text.
> 
> For Friends, there are two specific properties. The first one is that most dialogues are surrounding with the six main characters, including Rachel, Monica, Phoebe, Joey, Chandler, and Ross. The utterance ratio of given by the six roles is up to $83.4\%$. Second, the personal characteristics of the six characters are very clear. Each leading role has its own emotion undulated rule. To make use of these features, we introduce the personality tokenization which help learning the personality of the six characters. Personality tokenization concatenate the speaker and says tokens before the input utterance if the speaker is one of the six characters. The example is shown in Table TABREF12.
> 
> For EmotionPush, the text are informal chats which including like slang, acronym, typo, hyperlink, and emoji. Another characteristic is that the specific name entities are tokenized with random index. (e.g. “organization_80”, “person_01”, and “time_12”). We consider some of these informal text are related to expressing emotion such as repeated typing, purposed capitalization, and emoji (e.g. “:D”, “:(”, and “<3”)). Therefore, we keep most informal expressions but only process hyperlinks, empty utterance, and name entities by unifying the tokens.

### Relevance

Label: 

## Record 0985

Paper: EmotionX-IDEA: Emotion BERT -- an Affectional Model for Conversation

### Question

> what datasets were used?

### Passage

> Since our emotion recognition task is treated as a sequence-level classification task, the model would be fine-tuned on the processed training data. Following the BERT construction, we take the first embedding vector which corresponds to the special token [CLS] from the final hidden state of the Transformer encoder. This vector represents the embedding vector of the corresponding conversation utterances which is denoted as $\mathbf {C} \in \mathbb {R}^{H}$, where $H$ is the embedding size. A dense neural layer is treated as a classification layer which consists of parameters $\mathbf {W} \in \mathbb {R}^{K\times H}$ and $\mathbf {b} \in \mathbb {R}^{K}$, where $K$ is the number of emotion class. The emotion prediction probabilities $\mathbf {P} \in \mathbb {R}^{K}$ are computed by a softmax activation function as
> 
> All the parameters in BERT and the classification layer would be fine-turned together to minimize the Negative Log Likelihood (NLL) loss function, as Equation (DISPLAY_FORM22), based on the ground truth emotion label $c$.
> 
> In order to tackle the problem of highly unbalanced emotion labels, we apply weighted balanced warming on NLL loss function, as Equation (DISPLAY_FORM23), in the first epoch of fine-tuning procedure.
> 
> where $\mathbf {w}$ are the weights of corresponding emotion label $c$ which are computed and normalize by the frequency as
> 
> By adding the weighted balanced warming on NLL loss, the model could learn to predict the minor emotions (e.g. anger and sadness) earlier and make the training process more stable. Since the major evaluation metrics micro F1-score is effect by the number of each label, we only apply the weighted balanced warming in first epoch to optimize the performance.

### Relevance

Label: 

## Record 0986

Paper: A Dictionary-based Approach to Racism Detection in Dutch Social Media

### Question

> how did they ask if a tweet was racist?

### Passage

> Racism is an important issue which is not easily defined, as racist ideas can be expressed in a variety of ways. Furthermore, there is no clear definition of what exactly constitutes a racist utterance; what is racist to one person is highly likely to not be considered racist universally. Additionally, although there exist mechanisms for reporting acts of racism, victims often neglect to do so as they feel that reporting the situation will not solve anything, according to Unia, the Belgian Interfederal Centre for Equal Opportunities. The scope of this issue, however, is currently unknown. Hence, the goal of our system is two-fold: it can be used to shed light on how many racist remarks are not being reported online, and furthermore, the automated detection of racism could provide interesting insights in the linguistic mechanisms used in racist discourse.
> 
> In this study, we try to automatically detect racist language in Dutch social media comments, using a dictionary-based approach. We retrieved and annotated comments from two public social media sites which were likely to attract racist reactions according to Unia. We use a Support Vector Machine to automatically classify comments, using handcrafted dictionaries, which were later expanded using automated techniques, as features.
> 
> We first discuss previous research on our subject and methodology, and discuss the problem of defining racist language (section "Annotation Style" ). Next, we describe our data (section "Datasets and Annotations" ). Finally, after discussing the experimental setup (section "Experimental Setup" ), we present our results (section "Results and Discussion" ).

### Relevance

Label: 

## Record 0987

Paper: A Dictionary-based Approach to Racism Detection in Dutch Social Media

### Question

> how did they ask if a tweet was racist?

### Passage

> We annotated the retrieved comments with three different labels: `racist', `non-racist' and `invalid'.
> 
> The `racist' label describes comments that contain negative utterances or insults about someone's ethnicity, nationality, religion or culture. This definition also includes utterances which equate, for example, an ethnic group to an extremist group, as well as extreme generalizations. The following examples are comments that were classified as racist:
> 
> Het zijn precies de vreemden die de haat of het racisme opwekken bij de autochtonen.
> 
> It is the foreigners that elicit hate and racism from natives.
> 
> Kan je niets aan doen dat je behoort tot het ras dat nog minder verstand en gevoelens heeft in uw hersenen dan het stinkend gat van een VARKEN ! :-p
> 
> You cannot help the fact that you belong to the race that has less intellect and sense in their brains than the smelly behind of a PIG! :-P
> 
> Wil weer eens lukken dat wij met het vuilste krapuul zitten, ik verschiet er zelfs niet van!
> 
> Once again we have to put up with the filthiest scum, it doesn't even surprise me anymore!
> 
> The label `invalid' was used for comments that were written in languages other than Dutch, or that did not contain any textual information, i.e. comments that solely consist of pictures or links. Before classification, we excluded these from both our training and test set.
> 
> The final label, `non-racist', was the default label. If a comment was valid, but could not be considered racist according to our definition, this was the label we used.

### Relevance

Label: 

## Record 0988

Paper: A Dictionary-based Approach to Racism Detection in Dutch Social Media

### Question

> how did they ask if a tweet was racist?

### Passage

> test between dictionary models reveals that none of the models had performance differences that were statistically significant. Similarly, all dictionary models outperformed the unigram baseline with statistical significance, with $p$ $<$ 0.01 for the models based on the cleaned and expanded dictionaries, and $p$ $<$ 0.05 for the models based on the original dictionary.
> 
> To get more insight into why the expanded models were not more successful, we calculated dictionary coverage for every dictionary separately on the test set. If the expanded dictionaries do not have increased coverage, the reason for their similar performance is clear: not enough words have been added to affect the performance in any reasonable way. As Table 7 indicates, the coverage of the expanded dictionaries did increase, which indicates that the automated expansion, or manual deletion for that matter, contrary to expectations, did not add words that were useful for the classification of racist content. To obtain additional evidence for this claim, we looked at the number of comments that contained words from the original, cleaned and expanded dictionaries. The coverage in terms of total comments also increased, as well as the absolute number of racist comments that contained the added terms. Because the coverage in number of comments did not increase the performance of the dictionaries, we hypothesize that the terms that were included in the expanded dictionaries were not distributed clearly enough (over racist and neutral texts) to make a difference in the performance on the classification task.

### Relevance

Label: 

## Record 0989

Paper: A Dictionary-based Approach to Racism Detection in Dutch Social Media

### Question

> how did they ask if a tweet was racist?

### Passage

> utterances that C classified as `racist', but A and B classified as `not racist'.
> 
> The cause of these consistent differences in annotations might be cultural, as C is from the southern part of the Netherlands, whereas A and B are native to the northern part of Belgium. Some terms are simply misannotated by C because they are Flemish vernacular expressions. For example, zwartzak [black sack], from sentence 7, superficially looks like a derogatory term for a person of color, but actually does not carry this meaning, as it is a slang word for someone who collaborated with the German occupying forces in the Second World War. While this could still be classified as being racist, the point is that C only registered this as a slang word based on skin color, and not a cultural or political term. Finally, it is improbable that the cause of these mismatches is annotator training, as A and B did not discuss their annotations during the task. In addition to this, C functioned as a tiebreaker in the first dataset, and thus already had experience with the nature of the training material.

### Relevance

Label: 

## Record 0990

Paper: A Dictionary-based Approach to Racism Detection in Dutch Social Media

### Question

> how did they ask if a tweet was racist?

### Passage

> frequent use of modals and adverbs, which they link to the higher frequency of truth claims in racist utterances BIBREF2 , BIBREF3 . In several studies, pronoun use is reported as an important feature in the detection of racist language. While paolo2015racist reports a high frequency of (especially first person plural) pronouns in racist data, vandijk reports a more general finding: the importance of us and them constructions in racist discourse. He explains that they involve a `semantic move with a positive part about Us and a negative part about Them' BIBREF5 . Using such constructions, one linguistically emphasizes - either deliberately or subconsciously - a divide between groups of people. A strict interpretation implies that even positive utterances about `them' can be perceived as racist, as they can also imply a divide between us and them. In this sense, Van Dijk's definition of racism is subtler, but also broader, than the definition used in our own research: we only count negative utterances and generalizations about groups of people as racist.
> 
> Our dictionary-based approach is inspired by methods used in previous research, like LIWC (Linguistic Inquiry and Word Count) BIBREF6 . LIWC is a dictionary-based computational tool that counts word frequencies for both grammatical categories (e.g. pronouns) and content-related categories (e.g. negative emotion words). As LIWC uses counts per category instead of individual words' frequencies, it allows for broader generalizations on functionally or semantically related words.
> 
> The construction of dictionary categories related to racist discourse (cf. section "Dictionaries" ) is largely based on linguistic properties of racist language reported in earlier work (see above). Additionally, the categories were adjusted to fit the corpus used in the research, which differs from corpora used in other studies. As our corpus is retrieved from social media sites with an anti-Islamic orientation, we added categories to reflect anti-religious sentiment. The relevant features in this study therefore differ from those reported in other studies, as different words are used to insult different groups of people BIBREF3 .
> 
> Finally, some other successful quantitative approaches to racism detection that have been used in earlier studies are a bag of words (BoW) approach as well as the analysis of part-of-speech (PoS) tags BIBREF2

### Relevance

Label: 

## Record 0991

Paper: QuaRTz: An Open-Domain Dataset of Qualitative Relationship Questions

### Question

> How many general qualitative statements are in dataset?

### Passage

> Despite rapid progress in general question-answering (QA), e.g., BIBREF1, and formal models for qualitative reasoning (QR), e.g., BIBREF2, BIBREF3, there has been little work on reasoning with textual qualitative knowledge, and no dataset available in this area. Although many datasets include a few qualitative questions, e.g., BIBREF4, BIBREF5, the only one directly probing QR is QuaRel BIBREF0. However, although QuaRel contains 2700 qualitative questions, its underlying qualitative knowledge was specified formally, using a small, fixed ontology of 19 properties. As a result, systems trained on QuaRel are limited to only questions about those properties. Likewise, although the QR community has performed some work on extracting qualitative models from text, e.g., BIBREF6, BIBREF7, and interpreting questions about identifying qualitative processes, e.g., BIBREF8, there is no dataset available for the NLP community to study textual qualitative reasoning. QuaRTz addresses this need.

### Relevance

Label: 

## Record 0992

Paper: QuaRTz: An Open-Domain Dataset of Qualitative Relationship Questions

### Question

> How many general qualitative statements are in dataset?

### Passage

> QuaRTz was constructed as follows. First, 400 sentences expressing general qualitative relations were manually extracted by the authors from a large corpus using keyword search (“increase”, “faster”, etc.). Examples ($K_i$) are in Table TABREF3.
> 
> Second, crowdworkers were shown a seed sentence $K_i$, and asked to annotate the two properties being compared using the template below, illustrated using $K_2$ from Table TABREF3:
> 
> [vskip=0mm,leftmargin=3mm]
> 
> "The smaller its mass is, the greater its acceleration for a given amount of force."
> 
> They were then asked to author a situated, 2-way multiple-choice (MC) question that tested this relationship, guided by multiple illustrations. Examples of their questions ($Q_i$) are in Table TABREF3.
> 
> Third, a second set of workers was shown an authored question, asked to validate its answer and quality, and asked to annotate how the properties of $K_i$ identified earlier were expressed. To do this, they filled a second template, illustrated for $Q_2$:
> 
> Finally these workers were asked to generate a new question by “flipping” the original so the answer switched. Flipping means inverting comparatives (e.g., “more” $\rightarrow $ “less”), values, and other edits as needed to change the answer, e.g.,
> 
> K: More rain causes damper surfaces.
> 
> Q:More rain causes (A) wetter land (B) drier land
> 
> Q-flipped: Less rain causes (A) wetter land (B)
> 
> drier land
> 
> Flipped questions are created to counteract the tendency of workers to use the same comparison direction (e.g., “more”) in their question as in the seed sentence $K_i$, potentially answerable by simply matching $Q_i$ and $K_i$. Flipped questions are more challenging as they demand more qualitative reasoning (Section SECREF11).
> 
> Questions marked by workers as poor quality were reviewed by the authors and rejected/modified as appropriate. The dataset was then split into train/dev/test partitions such that questions from the same seed $K_i$ were all in the same partition. Statistics are in Table TABREF9.
> 
> To determine if the questions are correct and answerable given the general knowledge, a human baseline was computed. Three annotators independently answered a random sample of 100 questions given the supporting sentence $K_i$ for each. The mean score was 95.0%.

### Relevance

Label: 

## Record 0993

Paper: QuaRTz: An Open-Domain Dataset of Qualitative Relationship Questions

### Question

> How many general qualitative statements are in dataset?

### Passage

> Understanding and applying textual qualitative knowledge is an important skill for question-answering, but has received limited attention, in part due the lack of a broad-coverage dataset to study the task. QuaRTz aims to fill this gap by providing the first open-domain dataset of qualitative relationship questions, along with the requisite qualitative knowledge and a rich set of annotations. Specifically, QuaRTz removes the requirement, present in all previous qualitative reasoning work, that a fixed set of qualitative relationships be formally pre-specified. Instead, QuaRTz tests the ability of a system to find and apply an arbitrary relationship on the fly to answer a question, including when simple reasoning (arguments, polarities) is required.
> 
> As the QuaRTz task involves using a general corpus $K$ of textual qualitative knowledge, a high-performing system would be close to a fully general system where $K$ was much larger (e.g., the Web or a filtered subset), encompassing many more qualitative relationships, and able to answer arbitrary questions of this kind. Scaling further would thus require more sophisticated retrieval over a larger corpus, and (sometimes) chaining across influences, when a direct connection was not described in the corpus. QuaRTz thus provides a dataset towards this end, allowing controlled experiments while still covering a substantial number of textual relations in an open setting. QuaRTz is available at http://data.allenai.org/quartz/.

### Relevance

Label: 

## Record 0994

Paper: QuaRTz: An Open-Domain Dataset of Qualitative Relationship Questions

### Question

> How many general qualitative statements are in dataset?

### Passage

> Understanding and applying qualitative knowledge is a fundamental facet of intelligence. For example, we may read that exercise improves health, and thus decide to spend more time at the gym; or that larger cars cause more pollution, and thus decide to buy a smaller car to be environmentally sensitive. These skills require understanding the underlying qualitative relationships, and being able to apply them in specific contexts.
> 
> To promote research in this direction, we present the first open-domain dataset of qualitative relationship questions, called QuaRTz (“Qualitative Relationship Test set”). Unlike earlier work in qualitative reasoning, e.g., BIBREF0, the dataset is not restricted to a small, fixed set of relationships. Each question $Q_i$ (2-way multiple choice) is grounded in a particular situation, and is paired with a sentence $K_i$ expressing the general qualitative knowledge needed to answer it. $Q_i$ and $K_i$ are also annotated with the properties being compared (Figure FIGREF1). The property annotations serve as supervision for a potential semantic parsing based approach. The overall task is to answer the $Q_i$ given the corpus $K = \lbrace K_i\rbrace $.
> 
> We test several state-of-the-art (BERT-based) models and find that they are still substantially (20%) below human performance. Our contributions are thus (1) the dataset, containing 3864 richly annotated questions plus a background corpus of 400 qualitative knowledge sentences; and (2) an analysis of the dataset, performance of BERT-based models, and a catalog of the challenges it poses, pointing the way towards solutions.

### Relevance

Label: 

## Record 0995

Paper: QuaRTz: An Open-Domain Dataset of Qualitative Relationship Questions

### Question

> How many general qualitative statements are in dataset?

### Passage

> The results are shown in Table TABREF10, and provide insights into both the data and the models:
> 
> 1. The dataset is hard. Our best model, BERT-PFT (IR), scores only 73.7, over 20 points behind human performance (95.0), suggesting there are significant linguistic and semantic challenges to overcome (Section SECREF7).
> 
> 2. A general science-trained QA system has not learned this style of reasoning. BERT-Sci only scores 54.6, just a little above random (50.0).
> 
> 3. Pre-Fine-Tuning is important. Fine-tuning only on QuaRTz does signficantly worse (64.4) than pre-fine-tuning on RACE before fine-tuning on QuaRTz (73.7). Pre-fine-tuning appears to teach BERT something about multiple choice questions in general, helping it more effectively fine-tune on QuaRTz.
> 
> 4. BERT already “knows” some qualitative knowledge. Interestingly, BERT-PFT (no knowledge) scores 68.8, significantly above random, suggesting that BERT already “knows” some kind of qualitative knowledge. To rule out annotation artifacts, we we experimented with balancing the distributions of positive and negative influences, and different train/test splits to ensure no topical overlap between train and test, but the scores remained consistent.
> 
> 5. BERT can apply general qualitative knowledge to QA, but only partially. The model for the full task, BERT-PFT (IR) outperforms the no knowledge version (73.7, vs. 68.8), but still over 20 points below human performance. Even given the ideal knowledge (IR upper bound), it is still substantially behind (at 79.8) human performance. This suggests more sophisticated ways of training and/or reasoning with the knowledge are needed.

### Relevance

Label: 

## Record 0996

Paper: Correcting Length Bias in Neural Machine Translation

### Question

> Why does wider beam search hurt NMT?

### Passage

> In NMT, unlike the word-by-word translation example in the previous section, each output symbol is conditioned on the entire input sequence. Nevertheless, it's still possible to overestimate or underestimate INLINEFORM0 , so the possibility of label bias still exists. We expect that it will be more visible with weaker models, that is, with less training data.
> 
> Moreover, in NMT, the output sequence is of variable length, and generation of the output sequence stops when </s> is generated. In effect, for any prefix ending with </s>, the suffix distribution has zero entropy. This situation parallels example of the previous section closely: if the model overestimates the probability of outputting </s>, it may proceed to ignore the rest of the input and generate a truncated translation.
> 
> Figure FIGREF4 illustrates how this can happen. Although the model can learn not to prefer shorter translations by predicting a low probability for INLINEFORM0 early on, at each time step, the score of INLINEFORM1 puts a limit on the total remaining score a translation can have; in the figure, the empty translation has score INLINEFORM2 , so that no translation can have score lower than INLINEFORM3 . This lays a heavy burden on the model to correctly guess the total score of the whole translation at the outset.
> 
> As in our label-bias example, greedy search would prune the incorrect empty translation. More generally, consider beam search: at time step INLINEFORM0 , only the top INLINEFORM1 partial or complete translations are retained while the rest are pruned. (Implementations of beam search vary in the details, but this variant is simplest for the sake of argument.) Even if a translation ending at time INLINEFORM2 scores higher than a longer translation, as long as it does not fall within the top INLINEFORM3 when compared with partial translations of length INLINEFORM4 (or complete translations of length at most INLINEFORM5 ), it will be pruned and unable to block the longer translation. But if we widen the beam ( INLINEFORM6 ), then translation accuracy will suffer. We call this problem (which is BIBREF0 's sixth challenge) the beam problem. Our claim, hinted at by BIBREF0 , is that the brevity problem and the beam problem are

### Relevance

Label: 

## Record 0997

Paper: Correcting Length Bias in Neural Machine Translation

### Question

> Why does wider beam search hurt NMT?

### Passage

> Although highly successful, neural machine translation (NMT) systems continue to be plagued by a number of problems. We focus on two here: the beam problem and the brevity problem.
> 
> First, machine translation systems rely on heuristics to search through the intractably large space of possible translations. Most commonly, beam search is used during the decoding process. Traditional statistical machine translation systems often rely on large beams to find good translations. However, in neural machine translation, increasing the beam size has been shown to degrade performance. This is the last of the six challenges identified by BIBREF0 .
> 
> The second problem, noted by several authors, is that NMT tends to generate translations that are too short. BIBREF1 and BIBREF0 address this by dividing translation scores by their length, inspired by work on audio chords BIBREF2 . A similar method is also used by Google's production system BIBREF3 . A third simple method used by various authors BIBREF4 , BIBREF5 , BIBREF6 is a tunable reward added for each output word. BIBREF7 and BIBREF8 propose variations of this reward that enable better guarantees during search.
> 
> In this paper, we argue that these two problems are related (as hinted at by BIBREF0 ) and that both stem from label bias, an undesirable property of models that generate sentences word by word instead of all at once.
> 
> The typical solution is to introduce a sentence-level correction to the model. We show that making such a correction almost completely eliminates the beam problem. We compare two commonly-used corrections, length normalization and a word reward, and show that the word reward is slightly better.
> 
> Finally, instead of tuning the word reward using grid search, we introduce a way to learn it using a perceptron-like tuning method. We show that the optimal value is sensitive both to task and beam size, implying that it is important to tune for every model trained. Fortunately, tuning is a quick post-training step.

### Relevance

Label: 

## Record 0998

Paper: Correcting Length Bias in Neural Machine Translation

### Question

> Why does wider beam search hurt NMT?

### Passage

> Without any length correction, the standard model score (higher is better) is: INLINEFORM0
> 
> To our knowledge, there are three methods in common use for adjusting the model to favor longer sentences.
> 
> Length normalization divides the score by INLINEFORM0 BIBREF0 , BIBREF1 , BIBREF2 : INLINEFORM1
> 
> Google's NMT system BIBREF3 relies on a more complicated correction: INLINEFORM0
> 
> Finally, some systems add a constant word reward BIBREF5 : INLINEFORM0
> 
> If INLINEFORM0 , this reduces to the baseline model. The advantage of this simple reward is that it can be computed on partial translations, making it easier to integrate into beam search.

### Relevance

Label: 

## Record 0999

Paper: Correcting Length Bias in Neural Machine Translation

### Question

> Why does wider beam search hurt NMT?

### Passage

> Here, we first show that the beam problem is indeed the brevity problem. We then demonstrate that solving the length problem does solve the beam problem. Tables TABREF10 , TABREF11 , and TABREF12 show the results of our German–English, Russian–English, and French–English systems respectively. Each table looks at the impact on BLEU, METEOR, and the ratio of the lengths of generated sentences compared to the gold lengths BIBREF22 , BIBREF23 . The baseline method is a standard model without any length correction. The reward method is the tuned constant word reward discussed in the previous section. Norm refers to the normalization method, where a hypothesis' score is divided by its length.
> 
> The top sections of Tables TABREF10 , TABREF11 , TABREF12 illustrate the brevity and beam problems in the baseline models. As beam size increases, the BLEU and METEOR scores drop significantly. This is due to the brevity problem, which is illustrated by the length ratio numbers that also drop with increased beam size. For larger beam sizes, the length of the generated output sentences are a fraction of the lengths of the correct translations. For the lower-resource French–English task, the drop is more than 8 BLEU when increasing the beam size from 10 to 150. The issue is even more evident in our Russian-English system where we increase the beam to 1000 and BLEU scores drop by more than 20 points.
> 
> The results of tuning the word reward, INLINEFORM0 , as described in Section SECREF6 , is shown in the second section of Tables TABREF10 , TABREF11 , and TABREF12 . In contrast to our baseline systems, our tuned word reward always fixes the brevity problem (length ratios are approximately 1.0), and generally fixes the beam problem. An optimized word reward score always leads to improvements in METEOR scores over any of the best baselines. Across all language pairs, reward and norm have close METEOR scores, though the reward method wins out slightly. BLEU scores for reward and norm also increase over the baseline in most cases, despite BLEU's inherent bias towards shorter sentences. Most notably, whereas the baseline Russian–English system lost more than 20 BLEU points when the beam was increased to 1000,

### Relevance

Label: 

## Record 1000

Paper: Correcting Length Bias in Neural Machine Translation

### Question

> Why does wider beam search hurt NMT?

### Passage

> To address the brevity problem, many designers of NMT systems add corrections to the model. These corrections are often presented as modifications to the search procedure. But, in our view, the brevity problem is essentially a modeling problem, and these corrections should be seen as modifications to the model (Section SECREF5 ). Furthermore, since the root of the problem is local normalization, our view is that these modifications should be trained as globally-normalized models (Section SECREF6 ).

### Relevance

Label: 
