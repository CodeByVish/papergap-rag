# Passage relevance annotation

Annotator: 

Enter your name or agreed identifier after `Annotator:`.

Judge whether each passage helps answer the question, including useful partial evidence. Topic overlap alone is insufficient.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Preserve all content and record numbers. Work independently; do not exchange labels before submission. Algorithm sources are disclosed.

## Question 0121

Paper: Neural Summarization by Extracting Sentences and Words

> Do they compare to abstractive summarization methods?

### Common Retrieved Chunks

#### Passage 924

Retrieved by: BM25, Dense, Hybrid

> In this section we formally define the summarization tasks considered in this paper. Given a document $D$ consisting of a sequence of sentences $\lbrace s_1, \cdots , s_m\rbrace $ and a word set $\lbrace w_1, \cdots , w_n\rbrace $ , we are interested in obtaining summaries at two levels of granularity, namely sentences and words.
> 
> Sentence extraction aims to create a summary from $D$ by selecting a subset of $j$ sentences (where $j<m$ ). We do this by scoring each sentence within $D$ and predicting a label $y_L \in {\lbrace 0,1\rbrace }$ indicating whether the sentence should be included in the summary. As we apply supervised training, the objective is to maximize the likelihood of all sentence labels $\mathbf {y}_L=(y_L^1, \cdots , y_L^m)$ given the input document $D$ and model parameters $\theta $ :
> 
> $$\log p(\mathbf {y}_L |D; \theta ) = \sum \limits _{i=1}^{m} \log p(y_L^i |D; \theta )$$   (Eq. 5)
> 
> Although extractive methods yield naturally grammatical summaries and require relatively little linguistic analysis, the selected sentences make for long summaries containing much redundant information. For this reason, we also develop a model based on word extraction which seeks to find a subset of words in $D$ and their optimal ordering so as to form a summary $\mathbf {y}_s = (w^{\prime }_1, \cdots , w^{\prime }_k), w^{\prime }_i \in D$ . Compared to sentence extraction which is a sequence labeling problem, this task occupies the middle ground between full abstractive summarization which can exhibit a wide range of rewrite operations and extractive summarization which exhibits none. We formulate word extraction as a language generation task with an output vocabulary restricted to the original document. In our supervised setting, the training goal is to maximize the likelihood of the generated sentences, which can be further decomposed by enforcing conditional dependencies among their constituent words:
> 
> $$\hspace*{-5.69046pt}\log p(\mathbf {y}_s |D;
> \theta )\hspace*{-2.84544pt}=\hspace*{-2.84544pt}\sum \limits _{i=1}^{k}\hspace*{-2.84544pt}\log p(w^{\prime }_i | D, w^{\prime }_1,\hspace*{-2.84544pt}\cdots \hspace*{-2.84544pt}, w^{\prime }_{i-1}; \theta )$$   (Eq. 7)
> 
> In the following section, we discuss the data elicitation methods which allow us to train neural networks based on the above defined objectives.

#### Relevance 924

Label: 

#### Passage 925

Retrieved by: BM25, Hybrid

> The need to access and digest large amounts of textual data has provided strong impetus to develop automatic summarization systems aiming to create shorter versions of one or more documents, whilst preserving their information content. Much effort in automatic summarization has been devoted to sentence extraction, where a summary is created by identifying and subsequently concatenating the most salient text units in a document.
> 
> Most extractive methods to date identify sentences based on human-engineered features. These include surface features such as sentence position and length BIBREF0 , the words in the title, the presence of proper nouns, content features such as word frequency BIBREF1 , and event features such as action nouns BIBREF2 . Sentences are typically assigned a score indicating the strength of presence of these features. Several methods have been used in order to select the summary sentences ranging from binary classifiers BIBREF3 , to hidden Markov models BIBREF4 , graph-based algorithms BIBREF5 , BIBREF6 , and integer linear programming BIBREF7 .
> 
> In this work we propose a data-driven approach to summarization based on neural networks and continuous sentence features. There has been a surge of interest recently in repurposing sequence transduction neural network architectures for NLP tasks such as machine translation BIBREF8 , question answering BIBREF9 , and sentence compression BIBREF10 . Central to these approaches is an encoder-decoder architecture modeled by recurrent neural networks. The encoder reads the source sequence into a list of continuous-space representations from which the decoder generates the target sequence. An attention mechanism BIBREF11 is often used to locate the region of focus during decoding.
> 
> We develop a general framework for single-document summarization which can be used to extract sentences or words. Our model includes a neural network-based hierarchical document reader or encoder and an attention-based content extractor. The role of the reader is to derive the meaning representation of a document based on its sentences and their constituent words. Our models adopt a variant of neural attention to extract sentences or words. Contrary to previous work where attention is an intermediate step used to blend hidden units of an encoder to a vector propagating additional information to the decoder, our model applies attention directly to select

#### Relevance 925

Label: 

#### Passage 930

Retrieved by: Dense, Hybrid

> Data-driven neural summarization models require a large training corpus of documents with labels indicating which sentences (or words) should be in the summary. Until now such corpora have been limited to hundreds of examples (e.g., the DUC 2002 single document summarization corpus) and thus used mostly for testing BIBREF7 . To overcome the paucity of annotated data for training, we adopt a methodology similar to hermann2015teaching and create two large-scale datasets, one for sentence extraction and another one for word extraction.
> 
> In a nutshell, we retrieved hundreds of thousands of news articles and their corresponding highlights from DailyMail (see Figure 1 for an example). The highlights (created by news editors) are genuinely abstractive summaries and therefore not readily suited to supervised training. To create the training data for sentence extraction, we reverse approximated the gold standard label of each document sentence given the summary based on their semantic correspondence BIBREF7 . Specifically, we designed a rule-based system that determines whether a document sentence matches a highlight and should be labeled with 1 (must be in the summary), and 0 otherwise. The rules take into account the position of the sentence in the document, the unigram and bigram overlap between document sentences and highlights, the number of entities appearing in the highlight and in the document sentence. We adjusted the weights of the rules on 9,000 documents with manual sentence labels created by woodsend2010automatic. The method obtained an accuracy of 85% when evaluated on a held-out set of 216 documents coming from the same dataset and was subsequently used to label 200K documents. Approximately 30% of the sentences in each document were deemed summary-worthy.
> 
> For the creation of the word extraction dataset, we examine the lexical overlap between the highlights and the news article. In cases where all highlight words (after stemming) come from the original document, the document-highlight pair constitutes a valid training example and is added to the word extraction dataset. For out-of-vocabulary (OOV) words, we try to find a semantically equivalent replacement present in the news article. Specifically, we check if a neighbor, represented by pre-trained embeddings, is in the original document and therefore constitutes a valid substitution. If we cannot find any

#### Relevance 930

Label: 

#### Passage 931

Retrieved by: Dense, Hybrid

> attention to extract sentences or words. Contrary to previous work where attention is an intermediate step used to blend hidden units of an encoder to a vector propagating additional information to the decoder, our model applies attention directly to select sentences or words of the input document as the output summary. Similar neural attention architectures have been previously used for geometry reasoning BIBREF12 , under the name Pointer Networks.
> 
> One stumbling block to applying neural network models to extractive summarization is the lack of training data, i.e., documents with sentences (and words) labeled as summary-worthy. Inspired by previous work on summarization BIBREF7 , BIBREF13 and reading comprehension BIBREF9 we retrieve hundreds of thousands of news articles and corresponding highlights from the DailyMail website. Highlights usually appear as bullet points giving a brief overview of the information contained in the article (see Figure 1 for an example). Using a number of transformation and scoring algorithms, we are able to match highlights to document content and construct two large scale training datasets, one for sentence extraction and the other for word extraction. Previous approaches have used small scale training data in the range of a few hundred examples.
> 
> Our work touches on several strands of research within summarization and neural sequence modeling. The idea of creating a summary by extracting words from the source document was pioneered in bankoetal00 who view summarization as a problem analogous to statistical machine translation and generate headlines using statistical models for selecting and ordering the summary words. Our word-based model is similar in spirit, however, it operates over continuous representations, produces multi-sentence output, and jointly selects summary words and organizes them into sentences. A few recent studies BIBREF14 , BIBREF15 perform sentence extraction based on pre-trained sentence embeddings following an unsupervised optimization paradigm. Our work also uses continuous representations to express the meaning of sentences and documents, but importantly employs neural networks more directly to perform the actual summarization task.
> 
> rush2015neural propose a neural attention model for abstractive sentence compression which is trained on pairs of headlines and first sentences in an article. In contrast, our model summarizes documents rather than individual sentences, producing multi-sentential discourse. A major architectural difference is

#### Relevance 931

Label: 

#### Passage 932

Retrieved by: Dense, Hybrid

> propose a neural attention model for abstractive sentence compression which is trained on pairs of headlines and first sentences in an article. In contrast, our model summarizes documents rather than individual sentences, producing multi-sentential discourse. A major architectural difference is that our decoder selects output symbols from the document of interest rather than the entire vocabulary. This effectively helps us sidestep the difficulty of searching for the next output symbol under a large vocabulary, with low-frequency words and named entities whose representations can be challenging to learn. Gu:ea:16 and gulcehre2016pointing propose a similar “copy” mechanism in sentence compression and other tasks; their model can accommodate both generation and extraction by selecting which sub-sequences in the input sequence to copy in the output.
> 
> We evaluate our models both automatically (in terms of Rouge) and by humans on two datasets: the benchmark DUC 2002 document summarization corpus and our own DailyMail news highlights corpus. Experimental results show that our summarizers achieve performance comparable to state-of-the-art systems employing hand-engineered features and sophisticated linguistic constraints.

#### Relevance 932

Label: 

### BM25

#### Passage 926

Retrieved by: BM25

> Table 1 (upper half) summarizes our results on the DUC 2002 test dataset using Rouge. nn-se represents our neural sentence extraction model, nn-we our word extraction model, and nn-abs the neural abstractive baseline. The table also includes results for the lead baseline, the logistic regression classifier (lreg), and three previously published systems (ilp, tgraph, and urank).
> 
> The nn-se outperforms the lead and lreg baselines with a significant margin, while performing slightly better than the ilp model. This is an encouraging result since our model has only access to embedding features obtained from raw text. In comparison, lreg uses a set of manually selected features, while the ilp system takes advantage of syntactic information and extracts summaries subject to well-engineered linguistic constraints, which are not available to our models. Overall, our sentence extraction model achieves performance comparable to the state of the art without sophisticated constraint optimization (ilp, tgraph) or sentence ranking mechanisms (urank). We visualize the sentence weights of the nn-se model in the top half of Figure 4 . As can be seen, the model is able to locate text portions which contribute most to the overall meaning of the document.
> 
> Rouge scores for the word extraction model are less promising. This is somewhat expected given that Rouge is $n$ -gram based and not very well suited to measuring summaries which contain a significant amount of paraphrasing and may deviate from the reference even though they express similar meaning. However, a meaningful comparison can be carried out between nn-we and nn-abs which are similar in spirit. We observe that nn-we consistently outperforms the purely abstractive model. As nn-we generates summaries by picking words from the original document, decoding is easier for this model compared to nn-abs which deals with an open vocabulary. The extraction-based generation approach is more robust for proper nouns and rare words, which pose a serious problem to open vocabulary models. An example of the generated summaries for nn-we is shown at the lower half of Figure 4 .
> 
> Table 1 (lower half) shows system results on the 500 DailyMail news articles (test set). In general, we observe similar trends to DUC 2002, with nn-se performing the best in terms of

#### Relevance 926

Label: 

#### Passage 927

Retrieved by: BM25

> at the lower half of Figure 4 .
> 
> Table 1 (lower half) shows system results on the 500 DailyMail news articles (test set). In general, we observe similar trends to DUC 2002, with nn-se performing the best in terms of all rouge metrics. Note that scores here are generally lower compared to DUC 2002. This is due to the fact that the gold standard summaries (aka highlights) tend to be more laconic and as a result involve a substantial amount of paraphrasing. More experimental results on this dataset are provided in the appendix.
> 
> The results of our human evaluation study are shown in Table 2 . Specifically, we show, proportionally, how often our participants ranked each system 1st, 2nd, and so on. Perhaps unsurprisingly, the human-written descriptions were considered best and ranked 1st 27% of the time, however closely followed by our nn-se model which was ranked 1st 22% of the time. The ilp system was mostly ranked in 2nd place (38% of the time). The rest of the systems occupied lower ranks. We further converted the ranks to ratings on a scale of 1 to 6 (assigning ratings 6 $\dots $ 1 to rank placements 1 $\dots $ 6). This allowed us to perform Analysis of Variance (ANOVA) which revealed a reliable effect of system type. Specifically, post-hoc Tukey tests showed that nn-se and ilp are significantly ( $p < 0.01$ ) better than lead, nn-we, and nn-abs but do not differ significantly from each other or the human goldstandard.

#### Relevance 927

Label: 

#### Passage 928

Retrieved by: BM25

> In the standard neural sequence-to-sequence modeling paradigm BIBREF11 , an attention mechanism is used as an intermediate step to decide which input region to focus on in order to generate the next output. In contrast, our sentence extractor applies attention to directly extract salient sentences after reading them.
> 
> The extractor is another recurrent neural network that labels sentences sequentially, taking into account not only whether they are individually relevant but also mutually redundant. The complete architecture for the document encoder and the sentence extractor is shown in Figure 2 . As can be seen, the next labeling decision is made with both the encoded document and the previously labeled sentences in mind. Given encoder hidden states $(h_1, \cdots , h_m)$ and extractor hidden states $(\bar{h}_1, \cdots , \bar{h}_m)$ at time step $t$ , the decoder attends the $t$ -th sentence by relating its current decoding state to the corresponding encoding state:
> 
> $$\bar{\mathbf {h}}_{t} = \text{LSTM} ( p_{t-1} \mathbf {s}_{t-1}, \mathbf {\bar{h}}_{t-1})$$   (Eq. 20)
> 
> $$p(y_L(t)=1 | D ) = \sigma (\text{MLP} (\mathbf {\bar{h}}_t : \mathbf {h}_t) )$$   (Eq. 21)
> 
> where MLP is a multi-layer neural network with as input the concatenation of $\mathbf {\bar{h}}_t$ and $\mathbf {h}_t$ . $p_{t-1}$ represents the degree to which the extractor believes the previous sentence should be extracted and memorized ( $p_{t-1}$ =1 if the system is certain; 0 otherwise).
> 
> In practice, there is a discrepancy between training and testing such a model. During training we know the true label $p_{t-1}$ of the previous sentence, whereas at test time $p_{t-1}$ is unknown and has to be predicted by the model. The discrepancy can lead to quickly accumulating prediction errors, especially when mistakes are made early in the sequence labeling process. To mitigate this, we adopt a curriculum learning strategy BIBREF21 : at the beginning of training when $p_{t-1}$ cannot be predicted accurately, we set it to the true label of the previous sentence; as training goes on, we gradually shift its value to the predicted label $p(y_L(t-1)=1
> | d )$ .

#### Relevance 928

Label: 

### Dense

#### Passage 929

Retrieved by: Dense

> In this section we present our experimental setup for assessing the performance of our summarization models. We discuss the datasets used for training and evaluation, give implementation details, briefly introduce comparison models, and explain how system output was evaluated.

#### Relevance 929

Label: 

### Hybrid

None

## Question 0122

Paper: The Rapidly Changing Landscape of Conversational Agents

> What are the limitations of the currently used quantitative metrics? e.g. why are they not 'good'?

### Common Retrieved Chunks

#### Passage 933

Retrieved by: BM25, Dense, Hybrid

> Evaluating conversational agents is an open research problem in the field. With the inclusion of emotion component in the modern conversation agents, evaluating such models has become even more complex.The current evaluation methods like perplexity and BLEU score are not good enough and correlate very weakly with human judgments. In the paper by Liu et al, 2016 BIBREF31 , the authors discuss about how not to evaluate the dialogue system. They provide quantitative and qualitative results highlighting specific weaknesses in existing metrics and provide recommendations for the future development of better automatic evaluation metrics for dialogue systems.
> 
> According to them, the metrics (like Kiros et al, 2015 BIBREF32 ) that are based on distributed sentence representations hold the most promise for the future. It is because word-overlap metrics like BLEU simply require too many ground-truth responses to find a significant match for a reasonable response due to the high diversity of dialogue responses. Similarly, the metrics that are embedding-based consist of basic averages of vectors obtained through distributional semantics and so they are also insufficiently complex for modeling sentence-level compositionality in dialogue.
> 
> The metrics that take into account the context can also be considered. Such metrics can come in the form of an evaluation model that is learned from data. This model can be either a discriminative model that attempts to distinguish between model and human responses or a model that uses data collected from the human survey in order to provide human-like scores to proposed responses.

#### Relevance 933

Label: 

#### Passage 934

Retrieved by: BM25, Hybrid

> the next utterance INLINEFORM2 . The next utterance prediction is performed by means of a decoder RNN, which takes the hidden state of the context RNN and produces a probability distribution over the tokens in the next utterance. As seen in figure FIGREF4
> 
> The advantages of using a hierarchical representation are two-fold. First, the context RNN allows the model to represent a form of common ground between speakers, e.g. to represent topics and concepts shared between the speakers using a distributed vector representation. Second, because the number of computational steps between utterances is reduced. This makes the objective function more stable w.r.t. the model parameters, and helps propagate the training signal for first-order optimization methods.
> 
> Models like sequence-to-sequence and the hierarchical approaches have proven to be good baseline models. In the last couple of years there has been a major effort to build on top of these baselines to make conversational agents more robust BIBREF15 BIBREF16 .
> 
> Due to their large parameter space, the estimation of neural conversation models requires considerable amounts of dialogue data. Large online corpora are helpful for this. However several dialogue corpora, most notably those extracted from subtitles, do not include any explicit turn segmentation or speaker identification.The neural conversation model may therefore inadvertently learn responses that remain within the same dialogue turn instead of starting a new turn. Lison et al BIBREF17 overcome these limitations by introduce a weighting model into the neural architecture. The weighting model, which is itself estimated from dialogue data, associates each training example to a numerical weight that reflects its intrinsic quality for dialogue modelling. At training time, these sample weights are included into the empirical loss to be minimized. The purpose of this model is to associate each ⟨context, response⟩ example pair to a numerical weight that reflects the intrinsic “quality” of each example. The instance weights are then included in the empirical loss to minimize when learning the parameters of the neural conversation model. The weights are themselves computed via a neural model learned from dialogue data. Approaches like BIBREF17 are helpful but data to train these neural conversational agents remains scarce especially in academia, we talk more about the scarcity of data

#### Relevance 934

Label: 

#### Passage 935

Retrieved by: BM25, Dense, Hybrid

> that they were able to get a success rate of 79% for the complete dialogues (which was great).
> 
> The previous papers (like the ones which we discussed in the above paragraph) did not attempt to use data-driven techniques for the dialog agents because such data was not available in large amount at that time. But then there was a high increase in the collection of spoken dialog corpora which made it possible to use data-driven techniques to build and use models of task-oriented dialogs and possibly get good results. In the paper by Srinivas et al,2008 BIBREF11 , the authors proposed using data-driven techniques to build task structures for individual dialogs and use the dialog task structures for dialog act classification, task/subtask classification, task/subtask prediction and dialog act prediction.
> 
> For each utterance, they calculated features like n-grams of the words and their POS tags, dialog act and task/subtask label. Then they put those features in the binary MaxEnt classifier. For this, their model was able to achieve an error rate of 25.1% for the dialog act classification which was better than the best performing models at that time. Although, according to the modern standards, the results are not that great but the approach they suggested (of using data to build machine learning models) forms the basis of the techniques that are currently used in this area.

#### Relevance 935

Label: 

#### Passage 938

Retrieved by: Dense, Hybrid

> then executed. The accuracy was not that good and they did not bother to calculate it. Also, due to the integrated nature of conversational interaction in Persona, the necessary knowledge must be provided to each component of the system. Although it had limitations, it provided a very usable linguistic foundation for conversational interaction.
> 
> The researchers thought that if they can create assistant models specific to the corresponding models, they can achieve better accuracy for those applications instead of creating a common unified personal assistant which at that time performed quite poorly. There was a surge in application-specific assistants like in-car intelligent personal assistant (Schillo et al, 1996 BIBREF5 ), spoken-language interface to execute military exercises (Stent et al, 1999 BIBREF6 ), etc. Since it was difficult to develop systems with high domain extensibility, the researchers came up with a distributed architecture for cooperative spoken dialogue agents (Lin et al, 1999 BIBREF7 ).
> 
> Under this architecture, different spoken dialogue agents handling different domains can be developed independently and cooperate with one another to respond to the user’s requests. While a user interface agent can access the correct spoken dialogue agent through a domain switching protocol, and carry over the dialogue state and history so as to keep the knowledge processed persistently and consistently across different domains. Figure FIGREF1 shows the agent society for spoken dialogue for tour information service.
> 
> If we define the false alarm rate by counting the utterances in which unnecessary domain-switching occurred and the detection rate by counting the utterances in which the desired domain-switching were accurately detected, then in this model, high detection rate was achieved at very low false alarm rate. For instance, for around a false alarm rate of 0.2, the model was able to achieve a detection rate of around 0.9 for the case of tag sequence search with language model search scheme.

#### Relevance 938

Label: 

#### Passage 939

Retrieved by: Dense, Hybrid

> tools and entertainment. Dialogue systems can be divided into goal-driven systems, such as technical support services, booking systems, and querying systems. On the other hand we have non-goal-driven systems which are also referred to as chit-chat models. There is no explicit purpose for interacting with these agents other than entertainment. Compared to goal oriented dialog systems where the universe is limited to an application, building open-ended chit-chat models is more challenging. Non-goal oriented agents are a good indication of the state of the art of artificial intelligence according to the Turing test. With no grounding in common sense and no sense of context these agents have to fall back on canned responses and resort to internet searches now. But as we discuss in section SECREF5 , new techniques are emerging to provide this much needed context to these agents.
> 
> The recent successes in the domain of Reinforcement Learning (RL) has also opened new avenues of applications in the conversational agent setting. We explore some of these approaches in section SECREF6
> 
> Another feature that has been traditionally lacking in conversation agents is a personality. O Vinayal et al BIBREF2 hypothesis that not having a consistent personality is one of the main reasons that is stopping us from passing the turing test. Conversational agents also lack emotional consistency in their responses. These features are vital if we want humans to trust conversational agents. In section SECREF7 we discuss state of the art approaches to overcome these problems.
> 
> Despite such huge advancements in the field, the way these models are evaluated is something that needs to be dramatically altered. Currently there exists no perfect quantitative method to compare two conversational agents. The field has to rely on qualitative measures or measures like BLeU and perplexity borrowed from machine translation. In section SECREF8 we discuss this problem in detail.

#### Relevance 939

Label: 

### BM25

#### Passage 936

Retrieved by: BM25

> A lack of a coherent personality in conversational agents that most of these models propose has been identified as one of the primary reasons that these agents have not been able to pass the Turing test BIBREF0 BIBREF2 . Aside from such academic motivations, making conversational agents more like their human interlocutors which posses both a persona and are capable of parsing emotions is of great practical and commercial use. Consequently in the last couple of years different approaches have been tried to achieve this goal.
> 
> Li et al BIBREF29 address the challenge of consistency and how to endow data-driven systems with the coherent “persona” needed to model human-like behavior. They consider a persona to be composite of elements of identity (background facts or user profile), language behavior, and interaction style. They also account for a persona to be adaptive since an agent may need to present different facets to different human interlocutors depending on the interaction. Ultimately these personas are incorporated into the model as embeddings. Adding a persona not only improves the human interaction but also improves BLeU score and perplexity over the baseline sequence to sequence models. The model represents each individual speaker as a vector or embedding, which encodes speaker-specific information (e.g.dialect, register, age, gender, personal information) that influences the content and style of her responses. Most importantly these traits do not need to be explicitly annotated, which would be really tedious and limit the applications of the model. Instead the model manages to cluster users along some of these traits (e.g. age, country of residence) based on the responses alone. The model first encodes message INLINEFORM0 into a vector representation INLINEFORM1 using the source LSTM. Then for each step in the target side, hidden units are obtained by combining the representation produced by the target LSTM at the previous time step, the word representations at the current time step, and the speaker embedding INLINEFORM2 . In this way, speaker information is encoded and injected into the hidden layer at each time step and thus helps predict personalized responses throughout the generation process. The process described here is visualizes in figure FIGREF13 below.
> 
> Building on works like this the Emotional Chatting

#### Relevance 936

Label: 

#### Passage 937

Retrieved by: BM25

> Although these neural models are really powerful, so much so that they power most of the commercially available smart assistants and conversational agents. However these agents lack a sense of context and a grounding in common sense that their human interlocutors possess. This is especially evident when interacting with a commercial conversation agent, when more often that not the agent has to fall back to canned responses or resort to displaying Internet search results in response to an input utterance. One of the main goals of the research community, over the last year or so, has been to overcome this fundamental problem with conversation agents. A lot of different approaches have been proposed ranging from using knowledge graphs BIBREF20 to augment the agent's knowledge to using latest advancements in the field of online learning BIBREF21 . In this section we discuss some of these approaches.
> 
> The first approach we discuss is the Dynamic Knowledge Graph Network (DynoNet) proposed by He et al BIBREF20 , in which the dialogue state is modeled as a knowledge graph with an embedding for each node. To model both structured and open-ended context they model two agents, each with a private list of items with attributes, that must communicate to identify the unique shared item. They structure entities as a knowledge graph; as the dialogue proceeds, new nodes are added and new context is propagated on the graph. An attention-based mechanism over the node embeddings drives generation of new utterances. The model is best explained by the example used in the paper which is as follows: The knowledge graph represents entities and relations in the agent’s private KB, e.g., item-1’s company is google. As the conversation unfolds, utterances are embedded and incorporated into node embeddings of mentioned entities. For instance, in Figure FIGREF6 , “anyone went to columbia” updates the embedding of columbia. Next, each node recursively passes its embedding to neighboring nodes so that related entities (e.g., those in the same row or column) also receive information from the most recent utterance. In this example, jessica and josh both receive new context when columbia is mentioned. Finally, the utterance generator, an LSTM, produces the next utterance by attending to

#### Relevance 937

Label: 

### Dense

#### Passage 940

Retrieved by: Dense

> One of the first main papers that thought of using reinforcement learning for this came in 2005 by English et al BIBREF25 . They used an on-policy Monte Carlo method and the objective function they used was a linear combination of the solution quality (S) and the dialog length (L), taking the form: o(S,I) = INLINEFORM0 - INLINEFORM1 .
> 
> At the end of each dialog the interaction was given a score based on the evaluation function and that score was used to update the dialog policy of both agents (that is, the conversants). The state-action history for each agent was iterated over separately and the score from the recent dialog was averaged in with the expected return from the existing policy. They chose not to include any discounting factor to the dialog score as they progressed back through the dialog history. The decision to equally weight each state-action pair in the dialog history was made because an action’s contribution to the dialog score is not dependent upon its proximity to the end of the task. In order to combat the problem of converging to an effective policy they divided up the agent training process into multiple epochs.
> 
> The average objective function score for the case of learned policies was 44.90. One of the main reasons for the low accuracy (which is also a limitation of this paper) was that there were a number of aspects of dialog that they had not modeled such as non-understandings, misunderstandings, and even parsing sentences into the action specification and generating sentences from the action specification. But the paper set the pavement of the reinforcement learning methods into the area of dialog and personal agents.

#### Relevance 940

Label: 

### Hybrid

None

## Question 0123

Paper: A Question Answering Approach to Emotion Cause Extraction

> what word level sequences features are extracted?

### Common Retrieved Chunks

#### Passage 941

Retrieved by: BM25, Dense, Hybrid

> the emotion word. The question is, will the model really focus on the words which describe the emotion cause? We choose one example to show the attention results in Table 5:
> 
> Ex.2 家人/family 的/'s 坚持/insistence 更/more 让/makes 人/people 感动/touched
> 
> In this example, the cause of the emotion “touched” is “insistence”. We show in Table 5 the distribution of word-level attention weights in different hops of memory network training. We can observe that in the first two hops, the highest attention weights centered on the word “more". However, from the third hop onwards, the highest attention weight moves to the word sub-sequence centred on the word “insistence”. This shows that our model is effective in identifying the most important keyword relating to the emotion cause. Also, better results are obtained using deep memory network trained with at least 3 hops. This is consistent with what we observed in Section UID45 .
> 
> In order to evaluate the quality of keywords extracted by memory networks, we define a new metric on the keyword level of emotion cause extraction. The keyword is defined as the word which obtains the highest attention weight in the identified clause. If the keywords extracted by our algorithm is located within the boundary of annotation, it is treated as correct. Thus, we can obtain the precision, recall, and F-measure by comparing the proposed keywords with the correct keywords by: INLINEFORM0
> 
> Since the reference methods do not focus on the keywords level, we only compare the performance of Memnet and ConvMS-Memnet in Table 6. It can be observed that our proposed ConvMS-Memnet outperforms Memnet by 5.6% in F-measure. It shows that by capturing context features, ConvMS-Memnet is able to identify the word level emotion cause better compare to Memnet.
> 
> In our model, the training epochs are set to 20. In this section, we examine the testing error using a case study. Due to the page length limit, we only choose one example from the corpus. The text below has four clauses:
> 
> Ex.3 45天，对于失去儿子的他们是多么的漫长，宝贝回家了，这个春节是多么幸福。
> 
> Ex.3 45 days, it is long time for the parents who lost their baby. If the baby comes back home, they would become so happy in this Spring Festival.
> 
> In this example,

#### Relevance 941

Label: 

#### Passage 944

Retrieved by: BM25, Hybrid

> The formal definition of emotion cause extraction is given in BIBREF31 . In this task, a given document, which [id=lq]is a passage about an emotion event, contains an emotion word INLINEFORM0 and the cause of the event. The document is manually segmented in the clause level. For each clause INLINEFORM1 consisting of INLINEFORM2 words, the goal [id=lq]is to identify which clause contains the emotion cause. [id=lq]For data representation, we can map each word into a low dimensional embedding space, a.k.a word vector BIBREF32 . All the word vectors are stacked in a word embedding matrix INLINEFORM3 , where INLINEFORM4 is the dimension of word vector and INLINEFORM5 is the vocabulary size.
> 
> For example, the sentence, “I lost my phone yesterday, I feel so sad now.” shown in Figure 1, consists of two clauses. The first clause contains the emotion cause while the second clause [id=lq]expresses the emotion of sadness. [id=lq]Current methods to emotion cause extraction cannot handle complex sentence structures where the expression of an emotion and its cause are not adjacent. We envision that the memory network can [id=lq]better model the relation between [id=lq]a emotion word and [id=lq]its emotion causes in such complex sentence structures. In our approach, we only select the clause with the highest probability to be [id=lq] thean emotion cause in each document.

#### Relevance 944

Label: 

#### Passage 945

Retrieved by: BM25, Dense, Hybrid

> updated [id=lq]respectively in this way by back propagation. The concatenation of three output vectors forms a sequence-level feature which can be used in the training. Such a feature is important especially [id=lq]when the size of annotated training data is small.
> 
> For deep architecture with multiple layer[id=lq]s training, the network is more [id=lq]complex (shown in Figure 5).
> 
> For the first layer, the query is an embedding of the emotion word, INLINEFORM0 .
> 
> In the next layer, there are three input queries since the previous layer has three outputs: INLINEFORM0 , INLINEFORM1 , INLINEFORM2 . So, for the INLINEFORM3 -th layer ( INLINEFORM4 ), we need to re-define the weight function (5) as:
> 
> In the last layer, [id=lq]the concatenation of the three prediction vectors form the final prediction vector to generate the answer.
> 
> For model training, we use stochastic gradient descent and back propagation to optimize the loss function. Word embeddings are learned using a skip-gram model. The size of the word embedding is 20 since the vocabulary size in our dataset is small. The dropout is set to 0.4.

#### Relevance 945

Label: 

#### Passage 946

Retrieved by: Dense, Hybrid

> of 0.5597, outperforming RB+CB. Both SVM and word2vec are word feature based methods and they have similar performance. For word2vec, even though word representations are obtained from the SINA news raw corpus, it still performs worse than SVM trained using n-gram features only. The multi-kernel method BIBREF31 is the best performer among the baselines because it considers context information in a structured way. It models text by its syntactic tree and also considers an emotion lexicon. Their work shows that the structure information is important for the emotion cause extraction task.
> 
> Naively applying the original deep memory network or convolutional network for emotion cause extraction outperforms all the baselines except the convolutional multi-kernel method. However, using our proposed ConvMS-Memnet architecture, we manage to boost the performance by 11.54% in precision, 4.84% in recall and 8.24% in F-measure respectively when compared to Memnet. The improvement is very significant with INLINEFORM0 -value less than 0.01 in INLINEFORM1 -test. The ConvMS-Memnet also outperforms the previous best-performing method, multi-kernel, by 3.01% in F-measure. It shows that by effectively capturing context information, ConvMS-Memnet is able to identify the emotion cause better compared to other methods.

#### Relevance 946

Label: 

#### Passage 947

Retrieved by: Dense, Hybrid

> It is often the case that the meaning of a word is determined by its context, such as the previous word and the following word. [id=lq]Also, negations and emotion transitions are context sensitive. However, the memory network described in Section SECREF3 has only one memory slot with size INLINEFORM0 to represent a clause, where INLINEFORM1 is the dimension of a word embedding and INLINEFORM2 is the length of a clause. It means that when the memory network models a clause, it only considers each word separately.
> 
> In order to capture [id=lq]context information for clauses, we propose a new architecture which contains more memory slot to model the context with a convolutional operation. The basic architecture of Convolutional Multiple-Slot Memory Network (in short: ConvMS-Memnet) is shown in Figure 4.
> 
> Considering the text length is usually short in the dataset used here for emotion cause extraction, we set the size of the convolutional kernel to 3. That is, the weight of word INLINEFORM0 [id=lq]in the INLINEFORM1 -th position considers both the previous word INLINEFORM2 and the following word INLINEFORM3 by a convolutional operation: DISPLAYFORM0
> 
> For the first and the last word in a clause, we use zero padding, INLINEFORM0 , where INLINEFORM1 is the length of a clause. Then, the attention [id=lq]weightsignal for each word position in the clause is [id=lq]now defined as: DISPLAYFORM0
> 
> Note that we obtain the attention for each position rather than each word. It means that the corresponding attention for the INLINEFORM0 -th word in the previous convolutional slot should be INLINEFORM1 . Hence, there are three prediction output vectors, namely, INLINEFORM2 , INLINEFORM3 , INLINEFORM4 : DISPLAYFORM0
> 
> At last, we concatenate the three vectors as INLINEFORM0 for the prediction by a softmax function: DISPLAYFORM0
> 
> Here, the size of INLINEFORM0 is INLINEFORM1 . Since the prediction vector is a concatenation of three outputs. We implement a concatenation operation rather than averaging or other operations because the parameters in different memory slots can be updated [id=lq]respectively in this way by back propagation. The concatenation of three output vectors forms a sequence-level feature which can be used in the training. Such a feature is important especially [id=lq]when the size of annotated training data is small.

#### Relevance 947

Label: 

### BM25

#### Passage 942

Retrieved by: BM25

> We compare with the following baseline methods:
> 
> RB (Rule based method): The rule based method proposed in BIBREF33 .
> 
> CB (Common-sense based method): This is the knowledge based method proposed by BIBREF34 . We use the Chinese Emotion Cognition Lexicon BIBREF35 as the common-sense knowledge base. The lexicon contains more than 5,000 kinds of emotion stimulation and their corresponding reflection words.
> 
> RB+CB+ML (Machine learning method trained from rule-based features and facts from a common-sense knowledge base): This methods was previously proposed for emotion cause classification in BIBREF36 . It takes rules and facts in a knowledge base as features for classifier training. We train a SVM using features extracted from the rules defined in BIBREF33 and the Chinese Emotion Cognition Lexicon BIBREF35 .
> 
> SVM: This is a SVM classifier using the unigram, bigram and trigram features. It is a baseline previously used in BIBREF24 , BIBREF31
> 
> Word2vec: This is a SVM classifier using word representations learned by Word2vec BIBREF32 as features.
> 
> Multi-kernel: This is the state-of-the-art method using the multi-kernel method BIBREF31 to identify the emotion cause. We use the best performance reported in their paper.
> 
> CNN: The convolutional neural network for sentence classification BIBREF5 .
> 
> Memnet: The deep memory network described in Section SECREF3 . Word embeddings are pre-trained by skip-grams. The number of hops is set to 3.
> 
> ConvMS-Memnet: The convolutional multiple-slot deep memory network we proposed in Section SECREF13 . Word embeddings are pre-trained by skip-grams. The number of hops is 3 in our experiments.
> 
> Table 2 shows the evaluation results. The rule based RB gives fairly high precision but with low recall. CB, the common-sense based method, achieves the highest recall. Yet, its precision is the worst. RB+CB, the combination of RB and CB gives higher the F-measure But, the improvement of 1.27% is only marginal compared to RB.
> 
> For machine learning methods, RB+CB+ML uses both rules and common-sense knowledge as features to train a machine learning classifier. It achieves F-measure of 0.5597, outperforming RB+CB. Both SVM and word2vec are word feature based methods and they have similar performance. For word2vec, even though word representations are obtained from the SINA news raw corpus, it still performs worse than SVM trained using

#### Relevance 942

Label: 

#### Passage 943

Retrieved by: BM25

> the top of the network. It is a softmax function on the prediction vector from hop INLINEFORM0 : INLINEFORM1 .
> 
> The illustration of a deep memory network with three layers is shown in Figure 3. Since [id=lq]a memory network models the emotion cause at a fine-grained level, each word has a corresponding weight to measure its importance in this task. Comparing [id=lq]to previous approaches [id=lq]in emotion cause extraction which are [id=lq]mostly based [id=lq]on manually defined rules or linguistic features, [id=lq]a memory network is a more principled way to identify the emotion cause from text. However, the basic [id=lq]memory network model [id=lq]does not capture the sequential information in context which is important in emotion cause extraction.

#### Relevance 943

Label: 

### Dense

#### Passage 948

Retrieved by: Dense

> To gain better insights into our proposed ConvMS-Memnet, we conduct further experiments to understand the impact on performance by using: 1) pre-trained or randomly initialized word embedding; 2) multiple hops; 3) attention visualizations; 4) more training epochs.
> 
> In our ConvMS-Memnet, we use pre-trained word embedding as the input. The embedding maps each word into a lower dimensional real-value vector as its representation. Words sharing similar meanings should have similar representations. It enables our model to deal with synonyms more effectively. The question is, “can we train the network without using pre-trained word embeddings?". We initialize word vectors randomly, and use an embedding matrix to update the word vectors in the training of the network simultaneously. Comparison results are shown in Table 3. It can be observed that pre-trained word embedding gives 2.59% higher F-measure compared to random initialization. This is partly due to the limited size of our training data. Hence using word embedding trained from other much larger corpus gives better results.
> 
> It is widely acknowledged that computational models using deep architecture with multiple layers have better ability to learn data representations with multiple levels of abstractions. In this section, we evaluate the power of multiple hops in this task. We set the number of hops from 1 to 9 with 1 standing for the simplest single layer network shown in Figure 4. The more hops are stacked, the more complicated the model is. Results are shown in Table 4. The single layer network has achieved a competitive performance. With the increasing number of hops, the performance improves. However, when the number of hops is larger than 3, the performance decreases due to overfitting. Since the dataset for this task is small, more parameters will lead to overfitting. As such, we choose 3 hops in our final model since it gives the best performance in our experiments.
> 
> Essentially, memory network aims to measure the weight of each word in the clause with respect to the emotion word. The question is, will the model really focus on the words which describe the emotion cause? We choose one example to show the attention results in Table 5:
> 
> Ex.2 家人/family 的/'s 坚持/insistence 更/more 让/makes 人/people 感动/touched
> 
> In

#### Relevance 948

Label: 

### Hybrid

None

## Question 0124

Paper: When to reply? Context Sensitive Models to Predict Instructor Interventions in MOOC Forums

> What was the previous state of the art for this task?

### Common Retrieved Chunks

#### Passage 949

Retrieved by: BM25, Dense, Hybrid

> The problem of predicting instructor intervention in MOOCs was proposed by BIBREF0 . Later BIBREF7 evaluated baseline models by BIBREF0 over a larger corpus and found the results to vary widely across MOOCs. Since then subsequent works have used similar diverse evaluations on the same prediction problem BIBREF1 , BIBREF8 . BIBREF1 proposed models with discourse features to enable better prediction over unseen MOOCs. BIBREF8 recently showed interventions on Coursera forums to be biased by the position at which a thread appears to an instructor viewing the forum interface and proposed methods for debiased prediction.
> 
> While all works since BIBREF0 address key limitations in this line of research, they have not investigated the role of structure and sequence in the threaded discussion in predicting instructor interventions. BIBREF0 proposed probabilistic graphical models to model structure and sequence. They inferred vocabulary dependent latent post categories to model the thread sequence and infer states that triggered intervention. Their model, however, requires a hyperparameter for the number of latent states. It is likely that their empirically reported setting will not generalise due to their weak evaluation BIBREF7 . In this paper, we propose models to infer the context that triggers instructor intervention that does not require context lengths to be set apriori. All our proposed models generalise over modelling assumptions made by BIBREF0 .
> 
> For the purpose of comparison against a state-of-the-art and competing baselines we choose BIBREF7 since BIBREF0 's system and data are not available for replication.

#### Relevance 949

Label: 

#### Passage 951

Retrieved by: BM25, Dense, Hybrid

> The baseline and the models are evaluated on a corpus of 12 MOOC discussion forums. We train on 80% of the training data and report evaluation results on the held-out 20% of test data. We report INLINEFORM0 scores on the positive class (interventions), in line with prior work. We also argue that recall of the positive class is more important than precision, since it is costlier for instructors to miss intervening on a thread than spending irrelevant time intervening on a less critical threads due to false positives.
> 
> Model hyperpameter settings. All proposed and baseline neural models are trained using Adam optimizer with a learning rate of 0.001. We used cross-entropy as loss function. Importantly we updated the model parameters during training after each instance as in vanilla stochastic gradient descent; this setting was practical since data on most courses had only a few hundred instances enabling convergence within a reasonable training time of a few hours (see Table TABREF15 , column 2). Models were trained for a single epoch as most of our courses with a few hundred thread converged after a single epoch. We used 300-dimensional GloVe vectors and permitted the embeddings to be updated during the model's end-to-end training. The hidden dimension size of both INLINEFORM0 and INLINEFORM1 are set to 128 for all the models.
> 
> Baselines. We compare our models against a neural baseline models, hierarchical LSTM (hLSTM), with the attention ablated but with access to the complete context, and a strong, open-sourced feature-rich baseline BIBREF7 . We choose BIBREF7 over other prior works such as BIBREF0 since we do not have access to the dataset or the system used in their papers for replication. BIBREF7 is a logistic regression classifier with features inclusive of bag-of-words representation of the unigrams and thread length, normalised counts of agreements to previous posts, counts of non-lexical reference items such as URLs, and the Coursera forum type in which a thread appeared. We also report aggregated results from a hLSTM model with access only to the last post as context for comparison. Table TABREF17 compares the performance of these baselines against our proposed methods.

#### Relevance 951

Label: 

#### Passage 952

Retrieved by: BM25, Hybrid

> When they intervene, instructors either pay attention to a specific post or a series of posts, which trigger their reply. However, instructors rarely explicitly indicate to which post(s) their intervention is in relation to. This is the case in our corpus, party due to Coursera's user interface which only allows for single level comments (see Figure FIGREF2 ). Based solely on the binary, thread-level intervention signal, our secondary objective seeks to infer the appropriate context – represented by a sequence of posts – as the basis for the intervention.
> 
> We only consider linear contiguous series of posts starting with the thread's original post to constitute to a context; e.g., INLINEFORM0 . This is a reasonable as MOOC forum posts always reply to the original post or to a subsequent post, which in turn replies to the original post. This is in contrast to forums such as Reddit that have a tree or graph-like structure that require forum structure to be modelled explicitly, such as in BIBREF5 .
> 
> We propose three neural attention BIBREF11 variants based on how an instructor might attend and reply to a context in a thread: the ultimate, penultimate and any post attention models. We review each of these in turn.
> 
> Ultimate Post Attention (UPA) Model. In this model we attend to the context represented by hidden state of the INLINEFORM0 . We use the post prior to the instructor's reply as a query over the contexts INLINEFORM1 to compute attention weights INLINEFORM2 , which are then used to compute the attended context representation INLINEFORM3 (recall again that the intervention text itself is not available for this purpose). This attention formulation makes an equivalence between the final INLINEFORM4 post and the prospective intervention, using Post INLINEFORM5 as the query for finding the appropriate context INLINEFORM6 , inclusive of itself INLINEFORM7 . Said in another way, UPA uses the most recent content in the thread as the attentional query for context.
> 
> For example, if post INLINEFORM0 is the instructor's reply, post INLINEFORM1 will query over the contexts INLINEFORM2 and INLINEFORM3 . The model schematic is shown in Figure FIGREF12 .
> 
> The attended context representations are computed as: DISPLAYFORM0
> 
> The INLINEFORM0 representation is then

#### Relevance 952

Label: 

#### Passage 954

Retrieved by: Dense, Hybrid

> The key innovation of our work is to decompose the intervention prediction problem into a two-stage model that first explicitly tries to discover the proper context to which a potential intervention could be replying to, and then, predict the intervention status. This model implicitly assesses the importance (or urgency) of the existing thread's context to decide whether an intervention is necessary. For example in Figure SECREF1 , prior to the instructor's intervention, the ultimate post (Post #6) by Student 2 already acknowledged the OP's gratitude for his answer. In this regard, the instructor may have decided to use this point to summarize the entire thread to consolidate all the pertinent positions. Here, we might assume that the instructor's reply takes the entire thread (Posts #1–6) as the context for her reply.
> 
> This subproblem of inferring the context scope is where our innovation centers on. To be clear, in order to make the prediction that a instruction intervention is now necessary on a thread, the instructor's reply is not yet available — the model predicts whether a reply is necessary — so in the example, only Posts #1–6 are available in the problem setting. To infer the context, we have to decide which subsequence of posts are the most plausible motivation for an intervention.
> 
> Recent work in deep neural modeling has used an attention mechanism as a focusing query to highlight specific items within the input history that significantly influence the current decision point. Our work employs this mechanism – but with a twist: due to the fact that the actual instructor intervention is not (yet) available at the decision timing, we cannot use any actual intervention to decide the context. To employ attention, we must then employ a surrogate text as the query to train our prediction model. Our model variants model assess the suitability of such surrogate texts for the attention mechanism basis.
> 
> Congruent with the representation of the input forums, in all our proposed models, we encode the discussion thread hierarchically. We first build representations for each post by passing pre-trained word vector representations from GloVe BIBREF9 for each word through an LSTM BIBREF10 , INLINEFORM0 . We use the last layer output

#### Relevance 954

Label: 

#### Passage 955

Retrieved by: Dense, Hybrid

> show an example from smac-1 in Figure FIGREF22 with nine posts which was predicted correctly as intervened by APA but not by other models. Threads shows students confused over a missing figure in a homework. The instructor finally shows up, though late, to resolve the confusion.
> 
> RQ3. Do models trained with different context lengths perform better than when trained on a single context length?
> 
> We find that context length has a regularising effect on the model's performance at test time. This is not surprising since models trained with threads of single context length will not generalise to infer different context lengths. Row 4 of Table TABREF17 shows a steep performance drop in training by classifier with all threads truncated to a context of just one post, INLINEFORM0 , the post immediately preceding the intervened post. We also conducted an experiment with a multi-objective loss function with an additive cross-entropy term where each term computes loss from a model with context limited to a length of 3. We chose 3 since intervened threads in all the courses had a median length between 3 and 4. We achieved an INLINEFORM1 of 0.45 with a precision of 0.47 and recall of 0.43. This achieves a performance comparable to that of the BIBREF7 with context length set to only to 3. This approach of using infinitely many loss terms for each context length from 1 through the maximum thread length in a course is naive and not practical. We only use this model to show the importance of training the model with loss from threads of different lengths to prevent models overfitting to threads of specific context lengths.

#### Relevance 955

Label: 

### BM25

#### Passage 950

Retrieved by: BM25

> Massive Open Online Courses (MOOCs) have strived to bridge the social gap in higher education by bringing quality education from reputed universities to students at large. Such massive scaling through online classrooms, however, disrupt co-located, synchronous two-way communication between the students and the instructor.
> 
> MOOC platforms provide discussion forums for students to talk to their classmates about the lectures, homeworks, quizzes and provide a venue to socialise. Instructors (defined here as the course instructors, their teaching assistants and the MOOC platform's technical staff) monitor the discussion forum to post (reply to their message) in discussion threads among students. We refer to this posting as intervention, following prior work BIBREF0 . However, due to large student enrolment, the student–instructor ratio in MOOCs is very high Therefore, instructors are not able to monitor and participate in all student discussions. To address this problem, a number of works have proposed systems e.g., BIBREF0 , BIBREF1 to aid instructors to selectively intervene on student discussions where they are needed the most.
> 
> In this paper, we improve the state-of-the-art for instructor intervention in MOOC forums. We propose the first neural models for this prediction problem. We show that modelling the thread structure and the sequence of posts explicitly improves performance. Instructors in different MOOCs from different subject areas intervene differently. For example, on a Science, Technology, Engineering and Mathematics (STEM) MOOC, instructors may often intervene early as possible to resolve misunderstanding of the subject material and prevent confusion. However, in a Humanities MOOC, instructors allow for the students to explore open-ended discussions and debate among themselves. Such instructors may prefer to intervene later in the discussion to encourage further discussion or resolve conflicts among students. We therefore propose attention models to infer the latent context, i.e., the series of posts that trigger an intervention. Earlier studies on MOOC forum intervention either model the entire context or require the context size to be specified explicitly.

#### Relevance 950

Label: 

#### Passage 953

Retrieved by: BM25

> if post INLINEFORM0 is the instructor's reply, post INLINEFORM1 will query over the contexts INLINEFORM2 and INLINEFORM3 . The model schematic is shown in Figure FIGREF12 .
> 
> The attended context representations are computed as: DISPLAYFORM0
> 
> The INLINEFORM0 representation is then passed through a fully connected softmax layer to yield the binary prediction.
> 
> Penultimate Post Attention (PPA) Model. While the UPA model uses the most recent text and makes the ultimate post itself available as potential context, our the ultimate post may be better modeled as having any of its prior posts as potential context. Penultimate Post Attention (PPA) variant does this. The schematic and the equations for the PPA model are obtained by summing over contexts INLINEFORM0 in Equation EQREF10 and Figure FIGREF12 . While we could properly model such a context inference decision with any post INLINEFORM1 and prospective contexts INLINEFORM2 (where INLINEFORM3 is a random post), it makes sense to use the penultimate post, as we can make the most information available to the model for the context inference.
> 
> The attended context representations are computed as: DISPLAYFORM0
> 
> Any Post Attention (APA) Model. APA further relaxes both UPA and PPA, allowing APA to generalize and hypothesize that the prospective instructor intervention is based on the context that any previous post INLINEFORM0 replied to. In this model, each post INLINEFORM1 is set as a query to attend to its previous context INLINEFORM2 . For example, INLINEFORM3 will attend to INLINEFORM4 . Different from standard attention mechanisms, APA attention weights INLINEFORM5 are obtained by normalising interaction matrix over the different queries.
> 
> In APA, the attention context INLINEFORM0 is computed via: DISPLAYFORM0

#### Relevance 953

Label: 

### Dense

#### Passage 956

Retrieved by: Dense

> We evaluate our proposed models over a corpus of 12 MOOC iterations (offerings) on Coursera.org In partnership with Coursera and in line with its Terms of Service, we obtained the data for use in our academic research. Following prior work BIBREF7 we evaluate over a diverse dataset to represent MOOCs of varying sizes, instructor styles, instructor team sizes and number of threads intervened. We only include threads from sub-forums on Lecture, Homework, Quiz and Exam. We also normalise and label sub-forums with other non-standard names (e.g., Assignments instead of Homework) into of the four said sub-forums. Threads on general discussion, meet and greet and other custom sub-forums for social chitchat are omitted as our focus is to aid instructors on intervening on discussion on the subject matter. We also exclude announcement threads and other threads started by instructors since they are not interventions. We preprocess each thread by replacing URLs, equations and other mathematical formulae and references to timestamps in lecture videos by tokens INLINEFORM0 URL INLINEFORM1 , INLINEFORM2 MATH INLINEFORM3 , INLINEFORM4 TIMEREF INLINEFORM5 respectively. We also truncate intervened threads to only include posts before the first instructor post since the instructor's and subsequent posts will bias the prediction due to the instructor's post.

#### Relevance 956

Label: 

### Hybrid

None

## Question 0125

Paper: Spoken Conversational Search for General Knowledge

> What metrics are used for evaluation?

### Common Retrieved Chunks

#### Passage 957

Retrieved by: BM25, Hybrid

> On the one hand, the system is able to answer complex out-of-context questions such as “What are the capitals of the countries of the Iberian Peninsula?", by correctly answering the list of capitals: “Andorra la Vella, Gibraltar, Lisbon, Madrid".
> 
> On the other hand, consider the dialogue presented in Figure FIGREF23, in which the user asks several related questions about Michael Jackson. First she asks “Who is Michael Jackson?” and the system correctly answers “Michael Jackson is an American author, composer, singer and dancer”, note that this is the generated long answer.
> 
> The subsequent questions are related to the names of his family members. In order to correctly answer these questions, the resolution of coreferences is neccesary to solve the possessive pronouns, which in French agree in gender and number with the noun they introduce. In this specific example, while in English “his” is used in all the cases, in French it changes to: son père (father), sa mère (mother), ses frères (brothers). This example also illustrates resolution of elliptical questions in the context, by solving the question “and his mother's" as “What is the name of his mother".

#### Relevance 957

Label: 

#### Passage 958

Retrieved by: BM25, Dense, Hybrid

> The evaluation of the individual components of the proposed system was performed outside the scope of this work. We evaluated out-of-context questions, as well as the coreference resolution module.
> 
> Performance on out-of-context questions was evaluated on Bench'It, a dataset containing 150 open ended questions about general knowledge in French (Figure FIGREF20). The system reached a macro precision, recall and F-1 of $64.14\%$, $64.33\%$ and $63.46\%$ respectively.
> 
> We also evaluated the coreference resolution model on the test-set of CALOR (Table TABREF11), obtaining an average precision, recall and F-1 of 65.59%, 48.86% and 55.77% respectively. The same model reached a average F-1 of 68.8% for English BIBREF6. Comparable measurements are not available for French. F-1 scores for French are believed to be lower because of the lower amount of annotated data.

#### Relevance 958

Label: 

#### Passage 959

Retrieved by: BM25, Hybrid

> The Context Manager component is able to solve coreferences by using an adaptation of the end-to-end model presented in BIBREF6, that we trained for French by using fasttext multilingual character embeddings BIBREF7. The data used to train the coreference resolution model is a subset of the corpus CALOR BIBREF8 (Table TABREF11), which has been manually annotated with coreferences. This corpus contains coreference chains of named entities, nouns and pronouns (such as “the president” – “JFK” – “he” – “his”).
> 
> The dependency tree and semantic frames provided by the linguistic module are used to solve ellipsis by taking into account the syntactic and semantic structure of the previous question. Once the question has been resolved, it calls the QA systems and passes their results to the generation module.

#### Relevance 959

Label: 

#### Passage 962

Retrieved by: Dense, Hybrid

> The Search QA system uses an internal knowledge base, which finely indexes data using Elasticsearch. It is powered by Wikidata and enriched by Wikipedia, especially to calculate a Page-Rank BIBREF10 on each entity. This QA system first determines the potential named entities in the question (i.e. subjects, predicates, and types of subjects). Second, it constructs a correlation matrix by looking for the triplets in Wikidata that link these entities. This matrix is filtered according the coverage of the question and the relevance of each entity in order to find the best answer.

#### Relevance 962

Label: 

#### Passage 964

Retrieved by: Dense, Hybrid

> Two complementary question answering components were integrated into the system: the Reasoning QA and Search QA. Each of these QA systems computes a confidence score for every answer by using icsiboost BIBREF9, an Adaboost-based classifier trained on a corpus of around 21 000 questions. The Context Manager takes into account these scores to pick the higher-confidence of the two answers.
> 
> Besides the QA components, there are two other components that are able to provide complementary information about the Wikidata's entities under discussion: Documentary and Entity Sheet.

#### Relevance 964

Label: 

### BM25

#### Passage 960

Retrieved by: BM25

> The Reasoning QA system first parses the question by using a Prolog definite clause grammar (DCG), extended with word-embeddings to support variability in the vocabulary. Then it explores a graph containing logical patterns that are used to produce requests in SPARQL that agree with the question.

#### Relevance 960

Label: 

#### Passage 961

Retrieved by: BM25

> Conversational question answering is an open research problem. It studies the integration of question answering (QA) systems in a dialogue system(DS). Not long ago, each of these research subjects were studied separately; only very recently has studying the intersection between them gained increasing interest BIBREF0, BIBREF1.
> 
> We present a spoken conversational question answering system that is able to answer questions about general knowledge in French by calling two distinct QA systems. It solves coreference and ellipsis by modelling context. Furthermore, it is extensible, thus other components such as neural approaches for question-answering can be easily integrated. It is also possible to collect a dialogue corpus from its iterations.
> 
> In contrast to most conversational systems which support only speech, two input and output modalities are supported speech and text. Thus it is possible to let the user check the answers by either asking relevant Wikipedia excerpts or by navigating through the retrieved name entities or by exploring the answer details of the QA components: the confidence score as well as the set of explored triplets. Therefore, the user has the final word to consider the answer as correct or incorrect and to provide a reward, which can be used in the future for training reinforcement learning algorithms.

#### Relevance 961

Label: 

### Dense

#### Passage 963

Retrieved by: Dense

> The documentary component is able to extract pertinent excerpts of Wikipedia. It uses an internal documentary base, which indexes Wikipedia's paragraphs by incorporating the Wikidata entity's IDs into elasticsearch indexes. Thus, it is possible to find paragraphs (ranked by elasticsearch) illustrating the answer to the given question by taking into account the entities detected in the question and in the answer.

#### Relevance 963

Label: 

#### Passage 965

Retrieved by: Dense

> The high-level architecture of the proposed system consists of a speech-processing front-end, an understanding component, a context manager, a generation component, and a synthesis component. The context manager provides contextualised mediation between the dialogue components and several question answering back-ends, which rely on data provided by WikidataFOOTREF1. Interaction with a human user is achieved through a graphical user interface (GUI). Figure 1 depicts the components together with their interactions.
> 
> In the remainder of this section, we explain the components of our system.

#### Relevance 965

Label: 

### Hybrid

None

## Question 0126

Paper: Knowledge Based Machine Reading Comprehension

> Where is a question generation model used?

### Common Retrieved Chunks

#### Passage 967

Retrieved by: BM25, Dense, Hybrid

> Our question generation model takes the path between an “anchor” and the candidate answer, and outputs a question. We adopt the sequence to sequence architecture as our basic question generation model due to its effectiveness in natural language generation tasks. The hierarchical encoder and the hierarchical attention mechanism are introduced to take into account the structure of the input facts. Facts from external KBs are conventionally integrated into the model using the same way as described in the matching model.
> 
> As illustrated in Figure 3 , the question generation model contains an encoder and a decoder. We use a hierarchical encoder consisting of two layers to model the meaning of each element (subject, predicate or object) and the relationship between them. Since each element might contain multiple words, we use RNN as the word layer encoder to get the representation of each element. We define the fact level sequence as a path starting from the anchor and ending at the candidate answer. Another RNN is used as the fact level encoder. The last hidden state at the fact layer is fed to the decoder.
> 
> We develop a hierarchical attention mechanism in the decoder, which first makes soft alignment over the hidden states at the fact layer, the output of which is further used to attend to hidden states at the word level. Specifically, given the decoder hidden state $h^{dec}_{t-1}$ , we use a fact-level attention model $Att_{fct}$ to calculate the contextual vector, which is further combined with the current hidden state $h^{dec}_{t}$ , resulting in $c_{fct}$ . The contextual vector is calculated through weighted averaging over hidden vectors at the fact level, which is given as follows, where $\odot $ is dot product, $h^{fld}_j$ is the $j$ -th hidden state at the fact layer from the encoder, and $l_f$ is the number of hidden states at the fact level.
> 
> $$c_{fct} &= GRU(h^{dec}_{t}, \sum _{j=1}^{{l_f}} \alpha _{tj}h^{fct}_j) \\
> \alpha _{tj} &= \frac{ exp(h^{dec}_{t-1} \odot h^{fct}_j)}{\sum _{k=1}^{{l_f}}exp(h^{dec}_{t-1} \odot h^{fct}_k)}$$   (Eq. 19)
> 
> Similarly, we feed $c_{fct}$ to the word-level attention function $Att_{wrd}$ and calculate over hidden vectors at the word-level. The output $c_{wrd}$ will be concatenated with $h^{dec}_{t}$ to predict the next word.
> 
> Since many entity names of

#### Relevance 967

Label: 

#### Passage 968

Retrieved by: BM25, Dense, Hybrid

> In our experiments, we tune model parameters on the development set and report results on the test set. We design experiments from both ranking-based direction and question generation-based direction. The evaluation metric is precision @1 BIBREF17 , which indicates whether the top ranked result is the correct answer. We further report BLEU score BIBREF27 for the question generation approach.
> 
> We also adapt BiDAF BIBREF10 , a top-performing reading comprehension model on the SQuAD dataset BIBREF0 as a strong baseline. As BiDAF output a span from the input document as the answer to the given question, we adapt it to KBMRC as a ranking model similarly as the approach used in previous research BIBREF28 . We use BiDAF to select an answer span from a corresponding document based on a given question and select the candidate answer that has maximum overlap with the answer span as the final answer.

#### Relevance 968

Label: 

#### Passage 969

Retrieved by: BM25, Dense, Hybrid

> Our framework consists of a question answering model and a question generation model.
> 
> We implement two question answering models, which directly measure the semantic similarity between questions and candidate answers in the semantic space. First, to make the model's prediction more explainable, we implement a path based QA model PCNet. In this model, to get candidate answers from the triplets based document for a given question. We first retrieve the an “anchor” point $arg1_i$ or $arg2_i$ in the document fact $f_i$ . These anchors are selected based on edit distance between the words in the questions and the arguments. Then we regard all arguments in the 1-hops and 2-hops fact of the anchors as answers. However, the coverage of the candidate answers can be 100% in the model. We then implement a second end-to-end neural model KVMenNet which covers all the answers but with less interpretability. Both models generate a score $f_{qa}(q, a)$ of each candidate answer.
> 
> We then implement a generation-based model. The motivation to design this model is that we want to associate natural language phrases with knowledge based representation. It takes semantics of a candidate answer as the input and generates a question $\hat{q}$ . Then a paraphrasing model gives a score $f_{qg}(q,\hat{q})$ , which is computed between the generated question $\hat{q}$ and the original question $q$ , as the ranking score.
> 
> We get the final scores $S(q,a)$ used for ranking as follows.
> 
> $$S(q,a) = \lambda f_{qa}(q, a) + (1-\lambda ) f_{qg}(q,\hat{q})$$   (Eq. 7)
> 
> Moreover, we incorporate side information from external KBs into the three models. The details of how we use external KBs to enhance the representation of elements in the document KB will be described in section Incorporating External Knowledge.

#### Relevance 969

Label: 

#### Passage 970

Retrieved by: BM25, Hybrid

> The paraphrasing model is used to measure the semantic relevance between the original question and the question generated from the QG model. We use bidirectional RNN with gated recurrent unit to represent two questions, and compose them with element-wise multiplication. The results are followed by a $softmax$ layer, whose output length is 2. The model is trained by minimizing the cross-entropy error, in which the supervision is provided in the training data.
> 
> We collect two datasets to train the paraphrasing model. The first dataset is from Quora dataset, which is built for detecting whether or not a pair of questions are semantically equivalent. 345,989 positive question pairs and 255,027 negative pairs are included in the first dataset. The second dataset includes web queries from query logs, which are obtained by clustering the web queries that click the same web page. In this way we obtain 6,118,023 positive query pairs. We implement a heuristic rule to get 6,118,023 negative instances for the query dataset. For each pair of query text, we clamp the first query and retrieve a query that is mostly similar to the second query. To improve the efficiency of this process, we randomly sample 10,000 queries and define the “similarity” as the number of co-occurred words between two questions. During training, we initialize the values of word embeddings with $300d$ Glove vectors, which is learned on Wikipedia texts. We use a held-out data consisting of 20K query pairs to check the performance of the paraphrasing model. The accuracy of the paraphrasing model on the held-out dataset is 87.36%.

#### Relevance 970

Label: 

#### Passage 971

Retrieved by: Dense, Hybrid

> In this section, we present the generation model which generates a question based on the semantics of a candidate answer. Afterward, we introduce how our paraphrasing model, which measures the semantic relevance between the generated question and the original question, is pretrained.

#### Relevance 971

Label: 

### BM25

#### Passage 966

Retrieved by: BM25

> Despite the interpretability of PCNet, the coverage of anchor detection limits the upper bound of the approach. We implement a more powerful method based on the key-value memory network BIBREF19 , KVMemNet for short, which has proven powerful in KB-based question answering.
> 
> The KVMenNet could be viewed as a “soft” matching approach, which includes a parameterized memory consisting of key-value pairs. Intuitively, keys are used for matching with the question, and values are used for matching to the candidate answer. Given a KB fact ( $subj, pred, obj$ ), We consider both directions and add two key-value pairs in the memory, namely ( $key = subj +pred, value=obj$ ) and ( $key =obj + pred, value=subj$ ). The vectors of arguments/predicates are calculated the same way as described in PCNet. The concatenation of two vectors is used as the key vector $v_{key}$ .
> 
> Each memory item is assigned a relevance probability by comparing the question to each key.
> 
> $$\alpha _{key_i} = {softmax}(v_q \cdot v_{key_i})$$   (Eq. 12)
> 
> Afterwards, vectors in memory ( $v_{value}$ ) are weighted summed according to their addressing probabilities, and the vector $v_o$ is returned.
> 
> $$v_o = \sum _i \alpha _{key_i}v_{value_i}$$   (Eq. 13)
> 
> In PCNet, reasoning over two facts is achieved by incorporating 2-hop paths, while in KVMemNet this is achieved by repeating the memory access process twice. After receiving the result $v_o$ , we update the query with $q_2 = R(v_q + v_o)$ , where $R$ is model parameter. Finally, after a fixed number $n$ hops ( $n=2$ in this work), the resulting vector is used to measure the relevance to candidate answers via the dot product.

#### Relevance 966

Label: 

### Dense

#### Passage 972

Retrieved by: Dense

> Table 4 shows the results of different question generation models. Our approach is abbreviated as QGNet, which stands for the use of a paraphrasing model plus our question generation model. We can see that QGNet performs better than Seq2Seq in terms of BLEU score because many important words of low frequency from the input are replicated to the target sequence. However, the improvement is not significant for the QA task. We also incorporate each of the four KBs into QGNet, and observe slight improvements on NELL and Reverb. Despite the overall accuracy of QGNet being lower than PCNet and KVMemNet, combining outcomes with them could generates 1.5% and 0.8% absolute gains, respectively.
> 
> We show examples generated by our QG model in Figure 5 , in which the paths of two candidate answers are regarded as the input to the QG model. We can see that the original question is closer to the first generated result than the second one. Accordingly, the first candidate ($ 61,300) would be assigned with a larger probability as the answer.

#### Relevance 972

Label: 

### Hybrid

None

## Question 0127

Paper: Improving Fine-grained Entity Typing with Entity Linking

> How do they obtain the entity linking results in their model?

### Common Retrieved Chunks

#### Passage 973

Retrieved by: BM25, Hybrid

> In this paper, we use a simple EL algorithm that directly links the mention to the entity with the greatest commonness score. Commonness BIBREF17, BIBREF18 is calculated base on the anchor links in Wikipedia. It estimates the probability of an entity given only the mention string. In our FET approach, the commonness score is also used as the confidence on the linking result (i.e., the $\mathbf {g}$ used in the prediction part of Subsection SECREF5). Within a same document, we also use the same heuristic used in BIBREF19 to find coreferences of generic mentions of persons (e.g., “Matt”) to more specific mentions (e.g., “Matt Damon”).
> 
> We also tried other more advanced EL methods in our experiments. However, they do not improve the final performance of our model. Experimental results of using the EL system proposed in BIBREF19 is provided in Section SECREF4.

#### Relevance 973

Label: 

#### Passage 974

Retrieved by: BM25, Hybrid

> Given a piece of text and the span of an entity mention in this text, fine-grained entity typing (FET) is the task of assigning fine-grained type labels to the mention BIBREF0. The assigned labels should be context dependent BIBREF1. For example, in the sentence “Trump threatens to pull US out of World Trade Organization,” the mention “Trump” should be labeled as /person and /person/politician, although Donald Trump also had other occupations such as businessman, TV personality, etc.
> 
> This task is challenging because it usually uses a relatively large tag set, and some mentions may require the understanding of the context to be correctly labeled. Moreover, since manual annotation is very labor-intensive, existing approaches have to rely on distant supervision to train models BIBREF0, BIBREF2.
> 
> Thus, the use of extra information to help with the classification process becomes very important. In this paper, we improve FET with entity linking (EL). EL is helpful for a model to make typing decisions because if a mention is correctly linked to its target entity, we can directly obtain the type information about this entity in the knowledge base (KB). For example, in the sentence “There were some great discussions on a variety of issues facing Federal Way,” the mention “Federal Way” may be incorrectly labeled as a company by some FET models. Such a mistake can be avoided after linking it to the city Federal Way, Washington. For cases that require the understanding of the context, using entity linking results is also beneficial. In the aforementioned example where “Trump” is the mention, obtaining all the types of Donald Trump in the knowledge base (e.g., politician, businessman, TV personality, etc.) is still informative for inferring the correct type (i.e., politician) that fits the context, since they narrows the possible labels down.
> 
> However, the information obtained through EL should not be fully trusted since it is not always accurate. Even when a mention is correctly linked to an entity, the type information of this entity in the KB may be incomplete or outdated. Thus, in this paper, we propose a deep neural fine-grained entity typing model that flexibly predicts labels based on the context, the mention string, and the type information

#### Relevance 974

Label: 

#### Passage 975

Retrieved by: BM25, Dense, Hybrid

> Following existing studies, we also generate training data by using the anchor links in Wikipedia. Each anchor link can be used as a mention. These mentions are labeled by mapping the Freebase types of the target entries to the tag set $T$ BIBREF0.
> 
> Since the KB type representations we use in our FET model are also obtained through mapping Freebase types, they will perfectly match the automatically generated labels for the mentions that are correctly linked (i.e., when the entity returned by the EL algorithm and the target entry of the anchor link are the same). For example, in Figure FIGREF4, suppose the example sentence is a training sample obtained from Wikipedia, where “Donald Trump” is an anchor link points to the Wikipedia page of Donald Trump. After mapping the Freebase types of Donald Trump to the target tag set, this sample will be weakly annotated as /person/politician, /person/tv_personality, and /person/business, which is exactly the same as the type information (the “Types From KB” in Figure FIGREF4) obtained through EL. Thus, during training, when the EL system links the mention to the correct entity, the model only needs to output the types in the KB type representation. This may cause the trained model to overfit the weakly labeled training data. For most types of entities such as locations and organizations, it is fine since they usually have the same types in different contexts. But it is problematic for person mentions, as their types can be context dependent.
> 
> To address this problem, during training, if a mention is linked to a person entity by our entity linking algorithm, we add a random fine-grained person type label that does not belong to this entity while generating the KB type representation. For example, if the mention is linked to a person with types /person/actor and /person/author, a random label /person/politician may be added. This will force the model to still infer the type labels from the context even when the mention is correctly linked, since the KB type representation no longer perfectly match the weak labels.
> 
> To make it more flexible, we also propose to use a variant of the hinge loss used by BIBREF16 to train our

#### Relevance 975

Label: 

#### Passage 978

Retrieved by: Dense, Hybrid

> Apart from the three representations, we also obtain the score returned by our entity linking algorithm, which indicates its confidence on the linking result. We denote it as a one dimensional vector $\mathbf {g}$. Then, we get $\mathbf {f}=\mathbf {f}_c\oplus \mathbf {f}_s\oplus \mathbf {f}_e\oplus \mathbf {g}$, where $\oplus $ means concatenation. $\mathbf {f}$ is then fed into an MLP that contains three dense layers to obtain $\mathbf {u}_m$, out final representation for the current mention sample $m$. Let $t_1,t_2,...,t_k$ be all the types in $T$, where $k=|T|$. We embed them into the same space as $\mathbf {u}_m$ by assigning each of them a dense vector BIBREF15. These vectors are denoted as $\mathbf {t}_1,...,\mathbf {t}_k$. Then the score of the mention $m$ having the type $t_i\in T$ is calculated as the dot product of $\mathbf {u}_m$ and $\mathbf {t}_i$:
> 
> We predict $t_i$ as a type of $m$ if $s(m,t_i)>0$.

#### Relevance 978

Label: 

#### Passage 979

Retrieved by: Dense, Hybrid

> information of this entity in the KB may be incomplete or outdated. Thus, in this paper, we propose a deep neural fine-grained entity typing model that flexibly predicts labels based on the context, the mention string, and the type information from KB obtained with EL.
> 
> Using EL also introduces a new problem for the training process. Currently, a widely used approach to create FET training samples is to use the anchor links in Wikipedia BIBREF0, BIBREF3. Each anchor link is regarded as a mention, and is weakly labeled with all the types of its referred entity (the Wikipedia page the anchor link points to) in KB. Our approach, when links the mention correctly, also uses all the types of the referred entity in KB as extra information. This may cause the trained model to overfit the weakly labeled data. We design a variant of the hinge loss and introduce noise during training to address this problem.
> 
> We conduct experiments on two commonly used FET datasets. Experimental results show that introducing information obtained through entity linking and having a deep neural model both helps to improve FET performance. Our model achieves more than 5% absolute strict accuracy improvement over the state of the art on both datasets.
> 
> Our contributions are summarized as follows:
> 
> We propose a deep neural fine-grained entity typing model that utilizes type information from KB obtained through entity linking.
> 
> We address the problem that our model may overfit the weakly labeled data by using a variant of the hinge-loss and introducing noise during training.
> 
> We demonstrate the effectiveness of our approach with experimental results on commonly used FET datasets.
> 
> Our code is available at https://github.com/HKUST-KnowComp/IFETEL.

#### Relevance 979

Label: 

### BM25

#### Passage 976

Retrieved by: BM25

> To obtain the KB type representation, we run an EL algorithm for the current mention. If the EL algorithm returns an entity, we retrieve the types of of this entity from the KB. We use Freebase as our KB. Since the types in Freebase is different from $T$, the target type set, they are mapped to the types in $T$ with rules similar to those used in BIBREF14. Afterwards, we perform one hot encoding on these types to get the KB Type Representation $\mathbf {f}_e$. If the EL algorithm returns NIL (i.e., the mention cannot be linked to an entity), we simply one hot encode the empty type set.

#### Relevance 976

Label: 

#### Passage 977

Retrieved by: BM25

> To obtain the context representation, we first use a special token $w_m$ to represent the mention (the token “[Mention]” in Figure FIGREF4). Then, the word sequence of the sentence becomes $w_1,...,w_{p_l-1},w_m,w_{p_l+1},...,w_n$. Their corresponding word embeddings are fed into two layers of BiLSTMs. Let $\mathbf {h}_m^1$ and $\mathbf {h}_m^2$ be the output of the first and the second layer of BiLSTMs for $w_m$, respectively. We use $\mathbf {f}_c=\mathbf {h}_m^1+\mathbf {h}_m^2$ as the context representation vector.

#### Relevance 977

Label: 

### Dense

#### Passage 980

Retrieved by: Dense

> The experimental results are listed in Table TABREF16. As we can see, our approach performs much better than existing approaches on both datasets.
> 
> The benefit of using entity linking in our approach can be verified by comparing Ours (Full) and Ours (NoEL). The performance on both datasets decreases if the entity linking part is removed. Especially on FIGER (GOLD), the strict accuracy drops from 75.5 to 69.8. Using entity linking improves less on BBN. We think this is because of three reasons: 1) BBN has a much smaller tag set than FIGER (GOLD); 2) BBN does not allow a mention to be annotated with multiple type paths (e.g., labeling a mention with both /building and /location is not allowed), thus the task is easier; 3) By making the model deep, the performance on BBN is already improved a lot, which makes further improvement harder.
> 
> The improvement of our full approach over Ours (DirectTrain) on FIGER (GOLD) indicates that the techniques we use to avoid overfitting the weakly labeled data are also effective.
> 
> Ours (LocAttEL), which uses a more advanced EL system, does not achieve better performance than Ours (Full), which uses our own EL approach. After manually checking the results of the two EL approaches and the predictions of our model on FIGER (GOLD), we think this is mainly because: 1) Our model also uses the context while making predictions. Sometimes, if it “thinks” that the type information provided by EL is incorrect, it may not use it. 2) The performances of different EL approaches also depends on the dataset and the types of entities used for evaluation. We find that on FIGER (GOLD), the approach in BIBREF19 is better at distinguishing locations and sports teams, but it may also make some mistakes that our simple EL method does not. For example, it may incorrectly link “March,” the month, to an entity whose Wikipedia description fits the context better. 3) For some mentions, although the EL system links it to an incorrect entity, the type of this entity is the same with the correct entity.

#### Relevance 980

Label: 

#### Passage 981

Retrieved by: Dense

> We compare with the following existing approaches: AFET BIBREF3, AAA BIBREF16, NFETC BIBREF9, and CLSC BIBREF21.
> 
> We use Ours (Full) to represent our full model, and also compare with five variants of our own approach: Ours (DirectTrain) is trained without adding random person types while obtaining the KB type representation, and $\lambda _P$ is set to 1; Ours (NoEL) does not use entity linking, i.e., the KB type representation and the entity linking confidence score are removed, and the model is trained in DirectTrain style; Ours (NonDeep) uses one BiLSTM layer and replaces the MLP with a dense layer; Ours (NonDeep NoEL) is the NoEL version of Ours (NonDeep); Ours (LocAttEL) uses the entity linking approach proposed in BIBREF19 instead of our own commonness based approach. Ours (Full), Ours (DirectTrain), and Ours (NonDeep) all use our own commonness based entity linking approach.

#### Relevance 981

Label: 

### Hybrid

None

## Question 0128

Paper: Learning Scripts as Hidden Markov Models

> Which baselines do they use?

### Common Retrieved Chunks

#### Passage 982

Retrieved by: BM25, Dense, Hybrid

> average narrative length across domains is 3.8 with standard deviation of 1.7. This implies that only a frcation of the event types are present in any given narrative. There is a high degree of omission of events and many different ways of accomplishing each task. Hence, the prediction task is reasonably difficult, as evidenced by the simple baselines. Neither the frequency of events nor simple temporal structure is enough to accurately fill in the gaps which indicates that most sophisticated modeling such as SEM-HMM is needed.
> 
> The average accuracy across the 84 domains for each method is found in Table 1. On average our method significantly out-performed all the baselines, with the average improvement in accuracy across OMICS tasks between SEM-HMM and each baseline being statistically significant at a .01 level across all pairs and on sizes of INLINEFORM0 and INLINEFORM1 using one-sided paired t-tests. For INLINEFORM2 improvement was not statistically greater than zero. We see that the results improve with batch size INLINEFORM3 until INLINEFORM4 for SEM-HMM and BMM+EM, but they decrease with batch size for BMM without EM. Both of the methods which use EM depend on statistics to be robust and hence need a larger INLINEFORM5 value to be accurate. However for BMM, a smaller INLINEFORM6 size means it reconciles a couple of documents with the current model in each iteration which ultimately helps guide the structure search. The accuracy for “SEM-HMM Approx.” is close to the exact version at each batch level, while only taking half the time on average.

#### Relevance 982

Label: 

#### Passage 985

Retrieved by: BM25, Dense, Hybrid

> We now describe how we score the structures produced by our algorithm to select the best structure. We employ a Bayesian scoring function, which is the posterior probability of the model given the data, denoted INLINEFORM0 . The score is decomposed via Bayes Rule (i.e., INLINEFORM1 ), and the denominator is omitted since it is invariant with regards to the model.
> 
> Since each observation sequence is independent of the others, the data likelihood INLINEFORM0 is calculated using the Forward-Backward algorithm and Equation EQREF7 in Section SECREF4 . Because the initial model fully enumerates the data, any merge can only reduce the data likelihood. Hence, the model prior INLINEFORM1 must be designed to encourage generalization via state merges and edge deletions (described in Section SECREF10 ). We employed a prior with three components: the first two components are syntactic and penalize the number of states INLINEFORM2 and the number of non-zero transitions INLINEFORM3 respectively. The third component penalizes the number of frequently-observed semantic constraint violations INLINEFORM4 . In particular, the prior probabilty of the model INLINEFORM5 . The INLINEFORM6 parameters assign weights to each component in the prior.
> 
> The semantic constraints are learned from the event sequences for use in the model prior. The constraints take the simple form “ INLINEFORM0 never follows INLINEFORM1 .” They are learned by generating all possible such rules using pairwise permutations of event types, and evaluating them on the training data. In particular, the number of times each rule is violated is counted and a INLINEFORM2 -test is performed to determine if the violation rate is lower than a predetermined error rate. Those rules that pass the hypothesis test with a threshold of INLINEFORM3 are included. When evaluating a model, these contraints are considered violated if the model could generate a sequence of observations that violates the constraint.
> 
> Also, in addition to incrementally computing the transition and observation counts, INLINEFORM0 and INLINEFORM1 , the likelihood, INLINEFORM2 can be incrementally updated with structure changes as well. Note that the likelihood can be expressed as INLINEFORM3 when the state transitions are observed. Since the state transitions are not actually observed, we approximate the above expression by replacing the observed counts with expected

#### Relevance 985

Label: 

#### Passage 986

Retrieved by: BM25, Dense, Hybrid

> We now present our experimental results on SEM-HMM and SEM-HMM-Approx. The evaluation task is to predict missing events from an observed sequence of events. For comparison, four baselines were also evaluated. The “Frequency” baseline predicts the most frequent event in the training set that is not found in the observed test sequence. The “Conditional” baseline predicts the next event based on what most frequently follows the prior event. A third baseline, referred to as “BMM,” is a version of our algorithm that does not use EM for parameter estimation and instead only incrementally updates the parameters starting from the raw document counts. Further, it learns a standard HMM, that is, with no INLINEFORM0 transitions. This is very similar to the Bayesian Model Merging approach for HMMs BIBREF9 . The fourth baseline is the same as above, but uses our EM algorithm for parameter estimation without INLINEFORM1 transitions. It is referred to as “BMM + EM.”
> 
> The Open Minds Indoor Common Sense (OMICS) corpus was developed by the Honda Research Institute and is based upon the Open Mind Common Sense project BIBREF17 . It describes 175 common household tasks with each task having 14 to 122 narratives describing, in short sentences, the necessary steps to complete it. Each narrative consists of temporally ordered, simple sentences from a single author that describe a plan to accomplish a task. Examples from the “Answer the Doorbell” task can be found in Table 2. The OMICS corpus has 9044 individual narratives and its short and relatively consistent language lends itself to relatively easy event extraction.
> 
> The 84 domains with at least 50 narratives and 3 event types were used for evaluation. For each domain, forty percent of the narratives were withheld for testing, each with one randomly-chosen event omitted. The model was evaluated on the proportion of correctly predicted events given the remaining sequence. On average each domain has 21.7 event types with a standard deviation of 4.6. Further, the average narrative length across domains is 3.8 with standard deviation of 1.7. This implies that only a frcation of the event types are present in any given narrative. There is a high degree of omission of events and many different

#### Relevance 986

Label: 

#### Passage 988

Retrieved by: Dense, Hybrid

> We would like to thank Nate Chambers, Frank Ferraro, and Ben Van Durme for their helpful comments, criticism, and feedback. Also we would like to thank the SCALE 2013 workshop. This work was supported by the DARPA and AFRL under contract No. FA8750-13-2-0033. Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the DARPA, the AFRL, or the US government.

#### Relevance 988

Label: 

### BM25

#### Passage 983

Retrieved by: BM25

> He came back after ten minutes.” The standard inference algorithms, such as the Forward-Backward algorithm, are able to answer questions about the hidden states given the observed sentences, for example, “What did John do in Starbucks?”
> 
> There are two complications that need to be dealt with to adapt HMMs to model narrative scripts. First, both the set of states, i.e., event types, and the set of observations are not pre-specified but are to be learned from data. We assume that the set of possible observations and the set of event types to be bounded but unknown. We employ the clustering algorithm proposed in BIBREF4 to reduce the natural language sentences, i.e., event descriptions, to a small set of observations and states based on their Wordnet similarity.
> 
> The second complication of narrative texts is that many events may be omitted either in the narration or by the event extraction process. More importantly, there is no indication of a time lapse or a gap in the story, so the standard forward-backward algorithm does not apply. To account for this, we allow the states to skip generating observations with some probability. This kind of HMMs, with insertions and gaps, have been considered previously in speech processing BIBREF7 and in computational biology BIBREF8 . We refine these models by allowing state-dependent missingness, without introducing additional “insert states” or “delete states” as in BIBREF8 . In this paper, we restrict our attention to the so-called “Left-to-Right HMMs” which have acyclic graphical structure with possible self-loops, as they support more efficient inference algorithms than general HMMs and suffice to model most of the natural scripts. We consider the problem of learning the structure and parameters of scripts in the form of HMMs from sequences of natural language sentences. Our solution to script learning is a novel bottom-up method for structure learning, called SEM-HMM, which is inspired by Bayesian Model Merging (BMM) BIBREF9 and Structural Expectation Maximization (SEM) BIBREF10 . It starts with a fully enumerated HMM representation of the event sequences and incrementally merges states and deletes edges to improve the posterior probability of the structure and the parameters given the data. We compare our approach to several informed baselines on

#### Relevance 983

Label: 

#### Passage 984

Retrieved by: BM25

> Scripts were developed as a means of representing stereotypical event sequences and interactions in narratives. The benefits of scripts for encoding common sense knowledge, filling in gaps in a story, resolving ambiguous references, and answering comprehension questions have been amply demonstrated in the early work in natural language understanding BIBREF0 . The earliest attempts to learn scripts were based on explanation-based learning, which can be characterized as example-guided deduction from first principles BIBREF1 , BIBREF2 . While this approach is successful in generalizing from a small number of examples, it requires a strong domain theory, which limits its applicability.
> 
> More recently, some new graph-based algorithms for inducing script-like structures from text have emerged. “Narrative Chains” is a narrative model similar to Scripts BIBREF3 . Each Narrative Chain is a directed graph indicating the most frequent temporal relationship between the events in the chain. Narrative Chains are learned by a novel application of pairwise mutual information and temporal relation learning. Another graph learning approach employs Multiple Sequence Alignment in conjunction with a semantic similarity function to cluster sequences of event descriptions into a directed graph BIBREF4 . More recently still, graphical models have been proposed for representing script-like knowledge, but these lack the temporal component that is central to this paper and to the early script work. These models instead focus on learning bags of related events BIBREF5 , BIBREF6 .
> 
> While the above approches demonstrate the learnability of script-like knowledge, they do not offer a probabilistic framework to reason robustly under uncertainty taking into account the temporal order of events. In this paper we present the first formal representation of scripts as Hidden Markov Models (HMMs), which support robust inference and effective learning algorithms. The states of the HMM correspond to event types in scripts, such as entering a restaurant or opening a door. Observations correspond to natural language sentences that describe the event instances that occur in the story, e.g., “John went to Starbucks. He came back after ten minutes.” The standard inference algorithms, such as the Forward-Backward algorithm, are able to answer questions about the hidden states given the observed sentences, for example, “What did John do in Starbucks?”
> 
> There are two complications

#### Relevance 984

Label: 

### Dense

#### Passage 987

Retrieved by: Dense

> sequence, INLINEFORM0 , INLINEFORM1 , INLINEFORM2 , and INLINEFORM3 all have an implicit index INLINEFORM4 which denotes the observation sequence and has been omitted in the above equations. We will make it explicit below and calculate the expected counts of state visits, state transitions, and state transition observation triples. DISPLAYFORM0
> 
> Equation EQREF8 counts the total expected number of visits of each state in the data. Also, Equation estimates the expected number of transitions between each state pair. Finally, Equation computes the expected number of observations and state-transitions including null transitions. This concludes the E-step of the EM procedure.
> 
> The M-step of the EM procedure consists of Maximum Aposteriori (MAP) estimation of the transition and observation distributions is done assuming an uninformative Dirichlet prior. This amounts to adding a pseudocount of 1 to each of the next states and observation symbols. The observation distributions for the initial and final states INLINEFORM0 and INLINEFORM1 are fixed to be the Kronecker delta distributions at their true values. DISPLAYFORM0
> 
> The E-step and the M-step are repeated until convergence of the parameter estimates.

#### Relevance 987

Label: 

### Hybrid

#### Passage 989

Retrieved by: Hybrid

> setting, we do not know INLINEFORM1 —the true number of state transitions—as some of the observations are missing. Hence, we define INLINEFORM2 as the conditional probability of observing INLINEFORM3 in the remaining INLINEFORM4 steps given that the current state is INLINEFORM5 . This allows us to increment INLINEFORM6 starting from 0 as recursion proceeds, rather than decrementing it from INLINEFORM7 .
> 
> DISPLAYFORM0
> 
> Equation EQREF7 calculates the probability of the observation sequence INLINEFORM0 , which is computed by marginalizing INLINEFORM1 over time INLINEFORM2 and state INLINEFORM3 and setting the second index INLINEFORM4 to the length of the observation sequence INLINEFORM5 . The quantity INLINEFORM6 serves as the normalizing factor for the last three equations. DISPLAYFORM0
> 
> Equation , the joint distribution of the state and observation index INLINEFORM0 at time INLINEFORM1 is computed by convolution, i.e., multiplying the INLINEFORM2 and INLINEFORM3 that correspond to the same time step and the same state and marginalizing out the length of the state-sequence INLINEFORM4 . Convolution is necessary, as the length of the state-sequence INLINEFORM5 is a random variable equal to the sum of the corresponding time indices of INLINEFORM6 and INLINEFORM7 .
> 
> Equation computes the joint probability of a state-transition associated with a null observation by first multiplying the state transition probability by the null observation probability given the state transition and the appropriate INLINEFORM0 and INLINEFORM1 values. It then marginalizes out the observation index INLINEFORM2 . Again we need to compute a convolution with respect to INLINEFORM3 to take into account the variation over the total number of state transitions. Equation calculates the same probability for a non-null observation INLINEFORM4 . This equation is similar to Equation with two differences. First, we ensure that the observation is consistent with INLINEFORM5 by multiplying the product with the indicator function INLINEFORM6 which is 1 if INLINEFORM7 and 0 otherwise. Second, we advance the observation index INLINEFORM8 in the INLINEFORM9 function.
> 
> Since the equations above are applied to each individual observation sequence, INLINEFORM0 , INLINEFORM1 , INLINEFORM2 , and INLINEFORM3 all have an implicit index INLINEFORM4 which denotes the observation sequence and has been omitted in the above equations. We will make it explicit below and calculate the expected counts of

#### Relevance 989

Label: 

## Question 0129

Paper: DuTongChuan: Context-aware Translation Model for Simultaneous Interpreting

> Which datasets do they evaluate on?

### Common Retrieved Chunks

#### Passage 990

Retrieved by: BM25, Dense, Hybrid

> We use a subset of the data available for NIST OpenMT08 task . The parallel training corpus contains approximate 2 million sentence pairs. We choose NIST 2006 (NIST06) dataset as our development set, and the NIST 2002 (NIST02), 2003 (NIST03), 2004 (NIST04) 2005 (NIST05), and 2008 (NIST08) datasets as our test sets. We will use this dataset to evaluate the performance of our partial decoding and context-aware decoding strategy from the perspective of translation quality and latency.
> 
> Recently, we release Baidu Speech Translation Corpus (BSTC) for open research . This dataset covers speeches in a wide range of domains, including IT, economy, culture, biology, arts, etc. We transcribe the talks carefully, and have professional translators to produce the English translations. This procedure is extremely difficult due to the large number of domain-specific terminologies, speech redundancies and speakers' accents. We expect that this dataset will help the researchers to develop robust NMT models on the speech translation. In summary, there are many features that distinguish this dataset to the previously related resources:
> 
> Speech irregularities are kept in transcription while omitted in translation (eg. filler words like “嗯, 呃, 啊”, and unconscious repetitions like “这个这个呢”), which can be used to evaluate the robustness of the NMT model dealing with spoken language.
> 
> Each talk's transcription is translated into English by a single translator, and then segmented into bilingual sentence pairs according to the sentence boundaries in the English translations. Therefore, every sentence is translated based on the understanding of the entire talk and is translated faithfully and coherently in global sense.
> 
> We use the streaming multi-layer truncated attention model (SMLTA) trained on the large-scale speech corpus (more than 10,000 hours) and fine-tuned on a number of talk related corpora (more than 1,000 hours), to generate the 5-best automatic recognized text for each acoustic speech.
> 
> The test dataset includes interpretations produced by simultaneous interpreters with professional experience. This dataset contributes an essential resource for the comparison between translation and interpretation.
> 
> We randomly extract several talks from the dataset, and divide them into the development and test set. In Table TABREF34 , we summarize the statistics of our dataset. The average number of utterances per talk is 152.6 in the

#### Relevance 990

Label: 

#### Passage 993

Retrieved by: BM25, Hybrid

> criteria are designed for evaluating written translation and have a special emphasis on adequacy and faithfulness. But in simultaneous interpreting, human interpreters routinely omit less-important information to overcome their limitations in working memory. As the last column in Table 6 shows, human interpreters' oral translations have more omissions than machine's and receive lower acceptability. The evaluation results do not mean that machines have exceeded human interpreters in simultaneous interpreting. Instead, it means we need machine translation criteria that suit simultaneous interpreting. We also find that the BSTC dataset is extremely difficult as the best human interpreter obtains a lower Acceptability 73.04%. Although the NMT model obtains impressive translation quality, we do not compare the latency of machine translation and human interpreting in this paper, and leave it to the future work.
> 
> To better understand the contribution of our model on generating coherent translation, we select one representative running example for analysis. As the red text in Figure FIGREF73 demonstrates that machine translation model generates coherent translation “its own grid” for the sub-sentence “这个网络”, and “corresponds actually to” for the subsequence “...对应的,就是每个...”. Compared to the human interpretation, our model presents comparable translation quality. In details, our model treats segments as IUs, and generates translation for each IU consecutively. While the human interpreter splits the entire source text into two sub-sentences, and produces the translation respectively.
> 
> In the final deployment, we train DuTongChuan on the large-scale training corpus. We also utilize techniques to enhance the robustness of the translation model, such as normalization of the speech irregularities, dealing with abnormal ASR errors, and content censorship, etc (see Appendix). We successfully deploy DuTongChuan in the Baidu Create 2019 (Baidu AI Developer Conference) .
> 
> As shown in Table TABREF74 , it is clear that DuTongChuan achieves promising acceptability on both translation tasks (85.71% for Chinese-English, and 86.36 % for English-Chinese). We also elaborately analyze the error types in the final translations, and we find that apart from errors occurring in translation and ASR, a majority of errors come from IU boundary detection, which account for nearly a half of errors. In the future, we should concentrate on improving the translation quality by enhancing the robustness of our IU boundary

#### Relevance 993

Label: 

#### Passage 995

Retrieved by: Dense, Hybrid

> interpretation.
> 
> We randomly extract several talks from the dataset, and divide them into the development and test set. In Table TABREF34 , we summarize the statistics of our dataset. The average number of utterances per talk is 152.6 in the training set, 59.75 in the dev set, and 162.5 in the test set.
> 
> We firstly run the standard Transformer model on the NIST dataset. Then we evaluate the quality of the pre-trained model on our proposed speech translation dataset, and propose effective methods to improve the performance of the baseline. In that the testing data in this dataset contains ASR errors and speech irregularities, it can be used to evaluate the robustness of novel methods.
> 
> In the final deployment, we train our model using a corpus containing approximately 200 million bilingual pairs both in Chinese-English and English-Chinese translation tasks.

#### Relevance 995

Label: 

#### Passage 996

Retrieved by: Dense, Hybrid

> of all models.
> 
> In all settings, the best system in context-aware model beats the wait-15 model.
> 
> Pre-trained models are not sensitive to errors from Auto IU, while fine-tuned models are.
> 
> Another interesting work is to compare machine translation with human interpretation. We request three simultaneous interpreters (S, A and B) with years of interpreting experience ranging from three to seven years, to interpret the talks in BSTC testing dataset, in a mock conference setting .
> 
> We concatenate the translation of each talk into one big sentence, and then evaluate it by BLEU score. From Table TABREF69 , we find that machine translation beats the human interpreters significantly. Moreover, the length of interpretations are relatively short, and results in a high length penalty provided by the evaluation script. The result is unsurprising, because human interpreters often deliberately skip non-primary information to keep a reasonable ear-voice span, which may bring a loss of adequacy and yet a shorter lag time, whereas the machine translation model translates the content adequately. We also use human interpreting results as references. As Table TABREF69 indicates, our model achieves a higher BLEU score, 28.08.
> 
> Furthermore, we ask human translators to evaluate the quality between interpreting and machine translation. To evaluate the performance of our final system, we select one Chinese talk as well as one English talk consisting of about 110 sentences, and have human translators to assess the translation from multiple aspects: adequacy, fluency and correctness. The detailed measurements are:
> 
> Bad: Typically, the mark Bad indicates that the translation is incorrect and unacceptable.
> 
> OK: If a translation is comprehensible and adequate, but with minor errors such as incorrect function words and less fluent phrases, then it will be marked as OK.
> 
> Good: A translation will be marked as Good if it contains no obvious errors.
> 
> As shown in Table TABREF70 , the performance of our model is comparable to the interpreting. It is worth mentioning that both automatic and human evaluation criteria are designed for evaluating written translation and have a special emphasis on adequacy and faithfulness. But in simultaneous interpreting, human interpreters routinely omit less-important information to overcome their limitations in working memory. As the last column in Table 6

#### Relevance 996

Label: 

#### Passage 998

Retrieved by: Dense, Hybrid

> the traditional language model based methods, a 5-gram language model trained by KenLM toolkit , and an in-house implemented RNN based model. Both of two contrastive models are trained on approximate 2 million monolingual Chinese sentences. As shown in Table TABREF60 , it is clear that our model beats the previous work with an absolute improvement of more than 15 points in term of F-score (62.79 INLINEFORM0 78.26) and no obvious burden in latency (average latency). This observation indicates that with bidirectional context, the model can learn better representation to help the downstream tasks. In the next experiments, we will evaluate models given testing data with IU boundaries detected by our detector.
> 
> To our knowledge, almost all of the previous related work on simultaneous translation evaluate their models upon the clean testing data without ASR errors and with explicit sentence boundaries annotated by human translators. Certainly, testing data with real ASR errors and without explicit sentence boundaries is beneficial to evaluate the robustness of translation models. To this end, we perform experiments on our proposed BSTC dataset.
> 
> The testing data in BSTC corpus consists of six talks. We firstly employ our ASR model to recognize the acoustic waves into Chinese text, which will be further segmented into small pieces of sub-sentences by our IU detector. To evaluate the contribution of our proposed BSTC dataset, we firstly train all models on the NIST dataset, and then check whether the performance can be further improved by fine-tuning them on the BSTC dataset.
> 
> From the results shown in Table TABREF64 , we conclude the following observations:
> 
> Due to the relatively lower CER in ASR errors (10.32 %), the distinction between the clean input and the noisy input results in a BLEU score difference smaller than 2 points (15.85 vs. 14.60 for pre-train, and 21.98 vs. 19.91 for fine-tune).
> 
> Despite the small size of the training data in BSTC, fine-tuning on this data is essential to improve the performance of all models.
> 
> In all settings, the best system in context-aware model beats the wait-15 model.
> 
> Pre-trained models are not sensitive to errors from Auto IU, while fine-tuned models are.
> 
> Another interesting work is to compare machine translation with human

#### Relevance 998

Label: 

### BM25

#### Passage 991

Retrieved by: BM25

> We thank Ying Chen for improving the written of this paper. We thank Yutao Qu for developing partial modules of DuTongChuan. We thank colleagues in Baidu for their efforts on construction of the BSTC. They are Zhi Li, Ying Chen, Xuesi Song, Na Chen, Qingfei Li, Xin Hua, Can Jin, Lin Su, Lin Gao, Yang Luo, Xing Wan, Qiaoqiao She, Jingxuan Zhao, Can Jin, Wei Jin, Xiao Yang, Shuo Liu, Yang Zhang, Jing Ma, Junjin Zhao, Yan Xie, Minyang Zhang, Niandong Du, etc.
> 
> We also thank tndao.com and zaojiu.com for contributing their speech corpora.

#### Relevance 991

Label: 

#### Passage 992

Retrieved by: BM25

> The existing research on speech translation can be divided into two types: the End-to-End model BIBREF24 , BIBREF25 , BIBREF26 , BIBREF27 , BIBREF28 and the cascaded model. The former approach directly translates the acoustic speech in one language, into text in another language without generating the intermediate transcription for the source language. Depending on the complexity of the translation task as well as the scarce training data, previous literatures explore effective techniques to boost the performance. For example pre-training BIBREF29 , multi-task learning BIBREF24 , BIBREF27 , attention-passing, BIBREF30 , and knowledge distillation BIBREF28 etc.,. However, the cascaded model remains the dominant approach and presents superior performance practically, since the ASR and NMT model can be optimized separately training on the large-scale corpus.
> 
> Many studies have proposed to synthesize realistic ASR errors, and augment them with translation training data, to enhance the robustness of the NMT model towards ASR errors BIBREF2 , BIBREF3 , BIBREF4 . However, most of these approaches depend on simple heuristic rules and only evaluate on artificially noisy test set, which do not always reflect the real noises distribution on training and inference BIBREF5 , BIBREF6 , BIBREF7 .
> 
> Beyond the research on translation models, there are many research on the other relevant problems, such as sentence boundary detection for realtime speech translation BIBREF31 , BIBREF18 , BIBREF32 , BIBREF33 , BIBREF34 , low-latency simultaneous interpreting BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 , BIBREF35 , BIBREF36 , automatic punctuation annotation for speech transcription BIBREF37 , BIBREF38 , and discussion about human and machine in simultaneous interpreting BIBREF39 .
> 
> Focus on the simultaneous translation task, there are some work referring to the construction of the simultaneous interpreting corpus BIBREF40 , BIBREF41 , BIBREF42 . Particularly, BIBREF42 deliver a collection of a simultaneous translation corpus for comparative analysis on Japanese-English and English-Japanese speech translation. This work analyze the difference between the translation and the interpretations, using the interpretations from human simultaneous interpreters.
> 
> For better generation of coherent translations, gong2011cache propose a memory based approach to capture contextual information to make the statistical translation model generate discourse coherent translations. kuang2017cache,tu2018learning,P18-1118 extend similar memory based approach to the NMT framework. wang2017exploiting

#### Relevance 992

Label: 

#### Passage 994

Retrieved by: BM25

> Traditional NMT models are usually trained on bilingual corpora containing only complete sentences. However in our context-aware translation model, information units usually are sub-sentences. Intuitively, the discrepancy between the training and the decoding will lead to a problematic translation, if we use the conventional NMT model to translate such information units. On the other hand, conventional NMT models rarely do anticipation. Whereas in simultaneous interpreting, human interpreters often have to anticipate the up-coming input and render a constituent at the same time or even before it is uttered by the speaker.
> 
> In our previous work BIBREF0 , training a wait-k policy slightly differs from the traditional method. When predicting the first target token, we mask the source content behind the INLINEFORM0 token, in order to make the model learn to anticipate. The prediction of other tokens can also be obtained by moving the mask-window token-by-token from position INLINEFORM1 to the end of the line. According to our practical experiments, this training strategy do help the model anticipate correctly most of the time.
> 
> Following our previous work, we propose the partial decoding model, a tailored NMT model for translating the IUs that appear at the beginning of each sentence. As depicted in Figure FIGREF17 , in the training stage, we mask the second sub-sentence both in the source and target side. While translating the first sub-sentence, the model learns to anticipate the content after the comma, and produces a temporary translation that can be further completed with more source context. Clearly, this method relies on the associated sub-sentence pairs in the training data (black text in Figure FIGREF17 ). In this paper, we propose an automatic method to acquire such sub-sentence pairs.
> 
> Definition 3 Given a source sentence INLINEFORM0 with INLINEFORM1 tokens, a target sentence INLINEFORM2 with INLINEFORM3 tokens, and a word alignment set INLINEFORM4 where each alignment INLINEFORM5 is a tuple indicating a word alignment existed between the source token INLINEFORM6 and target token INLINEFORM7 , a sub-sentence pair INLINEFORM8 holds if satisfying the following conditions: DISPLAYFORM0
> 
> To acquire the word alignment, we run the open source toolkit fast_align , and use a variety of standard symmetrization heuristics to generate the alignment matrix. In the

#### Relevance 994

Label: 

### Dense

#### Passage 997

Retrieved by: Dense

> For example, for a sentence “她说我错了，那个叫什么什么呃妖姬。”, there are some representative training samples:

#### Relevance 997

Label: 

### Hybrid

None

## Question 0130

Paper: Universal Dependencies for Learner English

> How long is the dataset?

### Common Retrieved Chunks

#### Passage 999

Retrieved by: BM25, Hybrid

> on learner language BIBREF8 , syntax based grammatical error correction BIBREF9 , BIBREF10 , and many other fundamental challenges in NLP. In this work, we take the first step in this direction by benchmarking tagging and parsing accuracy on our dataset under different training regimes, and obtaining several estimates for the impact of grammatical errors on these tasks.
> 
> To summarize, this paper presents three contributions. First, we introduce the first large scale syntactic treebank for ESL, manually annotated with POS tags and universal dependencies. Second, we describe a linguistically motivated annotation scheme for ungrammatical learner English and provide empirical support for its consistency via inter-annotator agreement analysis. Third, we benchmark a state of the art parser on our dataset and estimate the influence of grammatical errors on the accuracy of automatic POS tagging and dependency parsing.
> 
> The remainder of this paper is structured as follows. We start by presenting an overview of the treebank in section SECREF2 . In sections SECREF3 and SECREF4 we provide background information on the annotation project, and review the main annotation stages leading to the current form of the dataset. The ESL annotation guidelines are summarized in section SECREF5 . Inter-annotator agreement analysis is presented in section SECREF6 , followed by parsing experiments in section SECREF7 . Finally, we review related work in section SECREF8 and present the conclusion in section SECREF9 .

#### Relevance 999

Label: 

#### Passage 1001

Retrieved by: BM25, Dense, Hybrid

> We utilize our two step review process to estimate agreement rates between annotators. We measure agreement as the fraction of annotation tokens approved by the editor. Table TABREF15 presents the agreement between annotators and reviewers, as well as the agreement between reviewers and the judges. Agreement measurements are provided for both the original the corrected versions of the dataset.
> 
> Overall, the results indicate a high agreement rate in the two editing tasks. Importantly, the gap between the agreement on the original and corrected sentences is small. Note that this result is obtained despite the introduction of several ESL annotation guidelines in the course of the annotation process, which inevitably increased the number of edits related to grammatical errors. We interpret this outcome as evidence for the effectiveness of the ESL annotation scheme in supporting consistent annotations of learner language.

#### Relevance 1001

Label: 

#### Passage 1002

Retrieved by: BM25, Dense, Hybrid

> The TLE currently contains 5,124 sentences (97,681 tokens) with POS tag and dependency annotations in the English Universal Dependencies (UD) formalism BIBREF2 , BIBREF3 . The sentences were obtained from the FCE corpus BIBREF1 , a collection of upper intermediate English learner essays, containing error annotations with 75 error categories BIBREF7 . Sentence level segmentation was performed using an adaptation of the NLTK sentence tokenizer. Under-segmented sentences were split further manually. Word level tokenization was generated using the Stanford PTB word tokenizer.
> 
> The treebank represents learners with 10 different native language backgrounds: Chinese, French, German, Italian, Japanese, Korean, Portuguese, Spanish, Russian and Turkish. For every native language, we randomly sampled 500 automatically segmented sentences, under the constraint that selected sentences have to contain at least one grammatical error that is not punctuation or spelling.
> 
> The TLE annotations are provided in two versions. The first version is the original sentence authored by the learner, containing grammatical errors. The second, corrected sentence version, is a grammatical variant of the original sentence, generated by correcting all the grammatical errors in the sentence according to the manual error annotation provided in the FCE dataset. The resulting corrected sentences constitute a parallel corpus of standard English. Table TABREF4 presents basic statistics of both versions of the annotated sentences.
> 
> To avoid potential annotation biases, the annotations of the treebank were created manually from scratch, without utilizing any automatic annotation tools. To further assure annotation quality, each annotated sentence was reviewed by two additional annotators. To the best of our knowledge, TLE is the first large scale English treebank constructed in a completely manual fashion.

#### Relevance 1002

Label: 

#### Passage 1003

Retrieved by: BM25, Dense, Hybrid

> data. For example, in Foster foster2007treebanks and Foster et al. foster2008 parsing experiments are carried out on synthetic learner-like data, that was created by automatic insertion of grammatical errors to well formed English text. In Cahill et al. cahill2014 a treebank of secondary level native students texts was used to approximate learner text in order to evaluate a parser that utilizes unlabeled learner data.
> 
> Syntactic annotations for ESL were previously developed by Nagata et al. nagata2011, who annotate an English learner corpus with POS tags and shallow syntactic parses. Our work departs from shallow syntax to full syntactic analysis, and provides annotations on a significantly larger scale. Furthermore, differently from this annotation effort, our treebank covers a wide range of learner native languages. An additional syntactic dataset for ESL, currently not available publicly, are 1,000 sentences from the EFCamDat dataset BIBREF8 , annotated with Stanford dependencies BIBREF19 . This dataset was used to measure the impact of grammatical errors on parsing by comparing performance on sentences with grammatical errors to error free sentences. The TLE enables a more direct way of estimating the magnitude of this performance gap by comparing performance on the same sentences in their original and error corrected versions. Our comparison suggests that the effect of grammatical errors on parsing is smaller that the one reported in this study.

#### Relevance 1003

Label: 

#### Passage 1005

Retrieved by: Dense, Hybrid

> The treebank was annotated by six students, five undergraduates and one graduate. Among the undergraduates, three are linguistics majors and two are engineering majors with a linguistic minor. The graduate student is a linguist specializing in syntax. An additional graduate student in NLP participated in the final debugging of the dataset.
> 
> Prior to annotating the treebank sentences, the annotators were trained for about 8 weeks. During the training, the annotators attended tutorials on dependency grammars, and learned the English UD guidelines, the Penn Treebank POS guidelines BIBREF11 , the grammatical error annotation scheme of the FCE BIBREF7 , as well as the ESL guidelines described in section SECREF5 and in the annotation manual.
> 
> Furthermore, the annotators completed six annotation exercises, in which they were required to annotate POS tags and dependencies for practice sentences from scratch. The exercises were done individually, and were followed by group meetings in which annotation disagreements were discussed and resolved. Each of the first three exercises consisted of 20 sentences from the UD gold standard for English, the English Web Treebank (EWT) BIBREF12 . The remaining three exercises contained 20-30 ESL sentences from the FCE. Many of the ESL guidelines were introduced or refined based on the disagreements in the ESL practice exercises and the subsequent group discussions. Several additional guidelines were introduced in the course of the annotation process.
> 
> During the training period, the annotators also learned to use a search tool that enables formulating queries over word and POS tag sequences as regular expressions and obtaining their annotation statistics in the EWT. After experimenting with both textual and graphical interfaces for performing the annotations, we converged on a simple text based format described in section SECREF6 , where the annotations were filled in using a spreadsheet or a text editor, and tested with a script for detecting annotation typos. The annotators continued to meet and discuss annotation issues on a weekly basis throughout the entire duration of the project.

#### Relevance 1005

Label: 

### BM25

#### Passage 1000

Retrieved by: BM25

> The majority of the English text available worldwide is generated by non-native speakers BIBREF0 . Such texts introduce a variety of challenges, most notably grammatical errors, and are of paramount importance for the scientific study of language acquisition as well as for NLP. Despite the ubiquity of non-native English, there is currently no publicly available syntactic treebank for English as a Second Language (ESL).
> 
> To address this shortcoming, we present the Treebank of Learner English (TLE), a first of its kind resource for non-native English, containing 5,124 sentences manually annotated with POS tags and dependency trees. The TLE sentences are drawn from the FCE dataset BIBREF1 , and authored by English learners from 10 different native language backgrounds. The treebank uses the Universal Dependencies (UD) formalism BIBREF2 , BIBREF3 , which provides a unified annotation framework across different languages and is geared towards multilingual NLP BIBREF4 . This characteristic allows our treebank to support computational analysis of ESL using not only English based but also multilingual approaches which seek to relate ESL phenomena to native language syntax.
> 
> While the annotation inventory and guidelines are defined by the English UD formalism, we build on previous work in learner language analysis BIBREF5 , BIBREF6 to formulate an additional set of annotation conventions aiming at a uniform treatment of ungrammatical learner language. Our annotation scheme uses a two-layer analysis, whereby a distinct syntactic annotation is provided for the original and the corrected version of each sentence. This approach is enabled by a pre-existing error annotation of the FCE BIBREF7 which is used to generate an error corrected variant of the dataset. Our inter-annotator agreement results provide evidence for the ability of the annotation scheme to support consistent annotation of ungrammatical structures.
> 
> Finally, a corpus that is annotated with both grammatical errors and syntactic dependencies paves the way for empirical investigation of the relation between grammaticality and syntax. Understanding this relation is vital for improving tagging and parsing performance on learner language BIBREF8 , syntax based grammatical error correction BIBREF9 , BIBREF10 , and many other fundamental challenges in NLP. In this work, we take the first step in this direction by benchmarking tagging and parsing accuracy on our

#### Relevance 1000

Label: 

### Dense

#### Passage 1004

Retrieved by: Dense

> After applying the resolutions produced by the judges, we queried the corpus with debugging tests for specific linguistics constructions. This additional testing phase further reduced the number of annotation errors and inconsistencies in the treebank. Including the training period, the treebank creation lasted over a year, with an aggregate of more than 2,000 annotation hours.

#### Relevance 1004

Label: 

### Hybrid

None

## Question 0131

Paper: Causal Explanation Analysis on Social Media

> What types of social media did they consider?

### Common Retrieved Chunks

#### Passage 1006

Retrieved by: BM25, Hybrid

> Identifying causal explanations in documents can be viewed as discourse relation parsing. The Penn Discourse Treebank (PDTB) BIBREF7 has a `Cause' and `Pragmatic Cause' discourse type under a general `Contingency' class and Rhetorical Structure Theory (RST) BIBREF8 has a `Relations of Cause'. In most cases, the development of discourse parsers has taken place in-domain, where researchers have used the existing annotations of discourse arguments in newswire text (e.g. Wall Street Journal) from the discourse treebank and focused on exploring different features and optimizing various types of models for predicting relations BIBREF9 , BIBREF10 , BIBREF11 . In order to further develop automated systems, researchers have proposed end-to-end discourse relation parsers, building models which are trained and evaluated on the annotated PDTB and RST Discourse Treebank (RST DT). These corpora consist of documents from Wall Street Journal (WSJ) which are much more well-organized and grammatical than social media texts BIBREF12 , BIBREF13 , BIBREF14 , BIBREF15 .
> 
> Only a few works have attempted to parse discourse relations for out-of-domain problems such as text categorizations on social media texts; Ji and Bhatia used models which are pretrained with RST DT for building discourse structures from movie reviews, and Son adapted the PDTB discourse relation parsing approach for capturing counterfactual conditionals from tweets BIBREF4 , BIBREF3 , BIBREF16 . These works had substantial differences to what propose in this paper. First, Ji and Bhatia used a pretrained model (not fully optimal for some parts of the given task) in their pipeline; Ji's model performed worse than the baseline on the categorization of legislative bills, which is thought to be due to legislative discourse structures differing from those of the training set (WSJ corpus). Bhatia also used a pretrained model finding that utilizing discourse relation features did not boost accuracy BIBREF4 , BIBREF3 . Both Bhatia and Son used manual schemes which may limit the coverage of certain types of positive samples– Bhatia used a hand-crafted schema for weighting discourse structures for the neural network model and Son manually developed seven surface forms of counterfactual thinking for the rule-based system BIBREF4 , BIBREF16 . We use social-media-specific features from pretrained models which are directly trained on tweets and we

#### Relevance 1006

Label: 

#### Passage 1007

Retrieved by: BM25, Hybrid

> In order to classify whether a message contains causal relation, we compared off-the-shelf PDTB parsers, linear SVM, RBF SVM, Random forest and LSTM classifiers. The off-the-shelf parsers achieved the lowest accuracies ( BIBREF12 and BIBREF13 in Table 3 ). This result can be expected since 1) these models were trained with news articles and 2) they are trained for all possible discourse relations in addition to causal relations (e.g., contrast, condition, etc). Among our suggested models, SVM and random forest classifier performed better than LSTM and, in the general trend, the more complex the models were, the worse they performed. This suggests that the models with more direct and simpler learning methods with features might classify the causality messages better than the ones more optimized for capturing distributional information or non-linear relationships of features.
> 
> Table 4 shows the results of a feature ablation test to see how each feature contributes to causality classification performance of the linear SVM classifier. POS tags caused the largest drop in F1. We suspect POS tags played a unique role because discourse connectives can have various surface forms (e.g., because, cuz, bcuz, etc) but still the same POS tag `P'. Also POS tags can capture the occurrences of modal verbs, a feature previously found to be very useful for detecting similar discourse relations BIBREF9 . N-gram features caused 0.022 F1 drop while sentiment tags did not affect the model when removed. Unlike the previous work where First-Last, First3 and Word pairs tended to gain a large F1 increase for multiclass discourse relation prediction, in our case, they did not affect the prediction performance compared to other feature types such as POS tags or N-grams.

#### Relevance 1007

Label: 

#### Passage 1008

Retrieved by: BM25, Hybrid

> Explanations of happenings in one's life, causal explanations, are an important topic of study in social, psychological, economic, and behavioral sciences. For example, psychologists have analyzed people's causal explanatory style BIBREF0 and found strong negative relationships with depression, passivity, and hostility, as well as positive relationships with life satisfaction, quality of life, and length of life BIBREF1 , BIBREF2 , BIBREF0 .
> 
> To help understand the significance of causal explanations, consider how they are applied to measuring optimism (and its converse, pessimism) BIBREF0 . For example, in “My parser failed because I always have bugs.”, the emphasized text span is considered a causal explanation which indicates pessimistic personality – a negative event where the author believes the cause is pervasive. However, in “My parser failed because I barely worked on the code.”, the explanation would be considered a signal of optimistic personality – a negative event for which the cause is believed to be short-lived.
> 
> Language-based models which can detect causal explanations from everyday social media language can be used for more than automating optimism detection. Language-based assessments would enable other large-scale downstream tasks: tracking prevailing causal beliefs (e.g., about climate change or autism), better extracting process knowledge from non-fiction (e.g., gravity causes objects to move toward one another), or detecting attribution of blame or praise in product or service reviews (“I loved this restaurant because the fish was cooked to perfection”).
> 
> In this paper, we introduce causal explanation analysis and its subtasks of detecting the presence of causality (causality prediction) and identifying explanatory phrases (causal explanation identification). There are many challenges to achieving these task. First, the ungrammatical texts in social media incur poor syntactic parsing results which drastically affect the performance of discourse relation parsing pipelines . Many causal relations are implicit and do not contain any discourse markers (e.g., `because'). Further, Explicit causal relations are also more difficult in social media due to the abundance of abbreviations and variations of discourse connectives (e.g., `cuz' and `bcuz').
> 
> Prevailing approaches for social media analyses, utilizing traditional linear models or bag of words models (e.g., SVM trained with n-gram, part-of-speech (POS) tags, or lexicon-based features) alone do not seem appropriate for this task since they

#### Relevance 1008

Label: 

#### Passage 1011

Retrieved by: Dense, Hybrid

> We developed a pipeline for causal explanation analysis over social media text, including both causality prediction and causal explanation identification. We examined a variety of model types and RNN architectures for each part of the pipeline, finding an SVM best for causality prediction and a hierarchy of BiLSTMs for causal explanation identification, suggesting the later task relies more heavily on sequential information. In fact, we found replacing either layer of the hierarchical LSTM architecture (the word-level or the DA-level) with a an equivalent “bag of features” approach resulted in reduced accuracy. Results of our whole pipeline of causal explanation analysis were found quite strong, achieving an $F1=0.868$ at identifying discourse arguments that are causal explanations.
> 
> Finally, we demonstrated use of our models in applications, finding associations between demographics and rate of mentioning causal explanations, as well as showing differences in the top words predictive of negative ratings in Yelp reviews. Utilization of discourse structure in social media analysis has been a largely untapped area of exploration, perhaps due to its perceived difficulty. We hope the strong results of causal explanation identification here leads to the integration of more syntax and deeper semantics into social media analyses and ultimately enables new applications beyond the current state of the art.

#### Relevance 1011

Label: 

#### Passage 1012

Retrieved by: Dense, Hybrid

> (e.g., `cuz' and `bcuz').
> 
> Prevailing approaches for social media analyses, utilizing traditional linear models or bag of words models (e.g., SVM trained with n-gram, part-of-speech (POS) tags, or lexicon-based features) alone do not seem appropriate for this task since they simply cannot segment the text into meaningful discourse units or discourse arguments such as clauses or sentences rather than random consecutive token sequences or specific word tokens. Even when the discourse units are clear, parsers may still fail to accurately identify discourse relations since the content of social media is quite different than that of newswire which is typically used for discourse parsing.
> 
> In order to overcome these difficulties of discourse relation parsing in social media, we simplify and minimize the use of syntactic parsing results and capture relations between discourse arguments, and investigate the use of a recursive neural network model (RNN). Recent work has shown that RNNs are effective for utilizing discourse structures for their downstream tasks BIBREF3 , BIBREF4 , BIBREF5 , BIBREF6 , but they have yet to be directly used for discourse relation prediction in social media. We evaluated our model by comparing it to off-the-shelf end-to-end discourse relation parsers and traditional models. We found that the SVM and random forest classifiers work better than the LSTM classifier for the causality detection, while the LSTM classifier outperforms other models for identifying causal explanation.
> 
> The contributions of this work include: (1) the proposal of models for both (a) causality prediction and (b) causal explanation identification, (2) the extensive evaluation of a variety of models from social media classification models and discourse relation parsers to RNN-based application models, demonstrating that feature-based models work best for causality prediction while RNNs are superior for the more difficult task of causal explanation identification, (3) performance analysis on architectural differences of the pipeline and the classifier structures, (4) exploration of the applications of causal explanation to downstream tasks, and (5) release of a novel, anonymized causality Facebook dataset along with our causality prediction and causal explanation identification models.

#### Relevance 1012

Label: 

### BM25

#### Passage 1009

Retrieved by: BM25

> Here, we explore the use of causal explanation analysis for downstream tasks. First we look at the relationship between use of causal explanation and one's demographics: age and gender. Then, we consider their use in sentiment analysis for extracting the causes of polarity ratings. Research involving human subjects was approved by the University of Pennsylvania Institutional Review Board.

#### Relevance 1009

Label: 

#### Passage 1010

Retrieved by: BM25

> In this task, the model identifies causal explanations given the discourse arguments of the causality message. We explored over the same models as those we used for causality (sans the output layer), and found the almost opposite trend of performances (see Table 5 ). The Linear SVM obtained lowest F1 while the LSTM model made the best identification performance. As opposed to the simple binary classification of the causality messages, in order to detect causal explanation, it is more beneficial to consider the relation across discourse arguments of the whole message and implicit distributional representation due to the implicit causal relations between two distant arguments.

#### Relevance 1010

Label: 

### Dense

#### Passage 1013

Retrieved by: Dense

> We build two types of models. First, we develop feature-based models which utilize features of the successful models in social media analysis and causal relation discourse parsing. Then, we build a recursive neural network model which uses distributed representation of discourse arguments as this approach can even capture latent properties of causal relations which may exist between distant discourse arguments. We specifically selected bidirectional LSTM since the model with the discourse distributional structure built in this form outperformed the traditional models in similar NLP downstream tasks BIBREF3 .
> 
> As the first step of our pipeline, we use Tweebo parser BIBREF20 to extract syntactic features from messages. Then, we demarcate sentences using punctuation (`,') tag and periods. Among those sentences, we find discourse connectives defined in PDTB annotation along with a Tweet POS tag for conjunction words which can also be a discourse marker. In order to decide whether these connectives are really discourse connectives (e.g., I went home, but he stayed) as opposed to simple connections of two words (I like apple and banana) we see if verb phrases exist before and after the connective by using dependency parsing results. Although discourse connective disambiguation is a complicated task which can be much improved by syntactic features BIBREF21 , we try to minimize effects of syntactic parsing and simplify it since it is highly error-prone in social media. Finally, according to visual inspection, emojis (`E' tag) are crucial for discourse relation in social media so we take them as separate discourse arguments (e.g.,in “My test result... :(” the sad feeling is caused by the test result, but it cannot be captured by plain word tokens).
> 
> We trained a linear SVM, an rbf SVM, and a random forest with N-gram, charater N-gram, and tweet POS tags, sentiment tags, average word lengths and word counts from each message as they have a pivotal role in the models for many NLP downstream tasks in social media BIBREF19 , BIBREF18 . In addition to these features, we also extracted First-Last, First3 features and Word Pairs from every adjacent pair of discourse arguments since these features were most helpful for causal relation prediction BIBREF9 . First-Last, First3 features are first and

#### Relevance 1013

Label: 

#### Passage 1014

Retrieved by: Dense

> We created our own causal explanation dataset by collecting 3,268 random Facebook status update messages. Three well-trained annotators manually labeled whether or not each message contains the causal explanation and obtained 1,598 causality messages with substantial agreement ( $\kappa =0.61$ ). We used the majority vote for our gold standard. Then, on each causality message, annotators identified which text spans are causal explanations.
> 
> For each task, we used 80% of the dataset for training our model and 10% for tuning the hyperparameters of our models. Finally, we evaluated all of our models on the remaining 10% (Table 1 and Table 2 ). For causal explanation detection task, we extracted discourse arguments using our parser and selected discourse arguments which most cover the annotated causal explanation text span as our gold standard.

#### Relevance 1014

Label: 

#### Passage 1015

Retrieved by: Dense

> discourse structures for the neural network model and Son manually developed seven surface forms of counterfactual thinking for the rule-based system BIBREF4 , BIBREF16 . We use social-media-specific features from pretrained models which are directly trained on tweets and we avoid any hand-crafted rules except for those included in the existing discourse argument extraction techniques.
> 
> The automated systems for discourse relation parsing involve multiple subtasks from segmenting the whole text into discourse arguments to classifying discourse relations between the arguments. Past research has found that different types of models and features yield varying performance for each subtask. Some have optimized models for discourse relation classification (i.e. given a document indicating if the relation existing) without discourse argument parsing using models such as Naive-Bayes or SVMs, achieve relatively stronger accuracies but a simpler task than that associated with discourse arguments BIBREF10 , BIBREF11 , BIBREF9 . Researchers who, instead, tried to build the end-to-end parsing pipelines considered a wider range of approaches including sequence models and RNNs BIBREF12 , BIBREF15 , BIBREF14 , BIBREF17 . Particularly, when they tried to utilize the discourse structures for out-domain applications, they used RNN-based models and found that those models are advantageous for their downstream tasks BIBREF4 , BIBREF3 .
> 
> In our case, for identifying causal explanations from social media using discourse structure, we build an RNN-based model for its structural effectiveness in this task (see details in section UID13 ). However, we also note that simpler models such as SVMs and logistic regression obtained the state-of-the-art performances for text categorization tasks in social media BIBREF18 , BIBREF19 , so we build relatively simple models with different properties for each stage of the full pipeline of our parser.

#### Relevance 1015

Label: 

### Hybrid

None

## Question 0132

Paper: QuaRTz: An Open-Domain Dataset of Qualitative Relationship Questions

> How many general qualitative statements are in dataset?

### Common Retrieved Chunks

#### Passage 1016

Retrieved by: BM25, Dense, Hybrid

> Despite rapid progress in general question-answering (QA), e.g., BIBREF1, and formal models for qualitative reasoning (QR), e.g., BIBREF2, BIBREF3, there has been little work on reasoning with textual qualitative knowledge, and no dataset available in this area. Although many datasets include a few qualitative questions, e.g., BIBREF4, BIBREF5, the only one directly probing QR is QuaRel BIBREF0. However, although QuaRel contains 2700 qualitative questions, its underlying qualitative knowledge was specified formally, using a small, fixed ontology of 19 properties. As a result, systems trained on QuaRel are limited to only questions about those properties. Likewise, although the QR community has performed some work on extracting qualitative models from text, e.g., BIBREF6, BIBREF7, and interpreting questions about identifying qualitative processes, e.g., BIBREF8, there is no dataset available for the NLP community to study textual qualitative reasoning. QuaRTz addresses this need.

#### Relevance 1016

Label: 

#### Passage 1017

Retrieved by: BM25, Dense, Hybrid

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

#### Relevance 1017

Label: 

#### Passage 1018

Retrieved by: BM25, Dense, Hybrid

> Understanding and applying textual qualitative knowledge is an important skill for question-answering, but has received limited attention, in part due the lack of a broad-coverage dataset to study the task. QuaRTz aims to fill this gap by providing the first open-domain dataset of qualitative relationship questions, along with the requisite qualitative knowledge and a rich set of annotations. Specifically, QuaRTz removes the requirement, present in all previous qualitative reasoning work, that a fixed set of qualitative relationships be formally pre-specified. Instead, QuaRTz tests the ability of a system to find and apply an arbitrary relationship on the fly to answer a question, including when simple reasoning (arguments, polarities) is required.
> 
> As the QuaRTz task involves using a general corpus $K$ of textual qualitative knowledge, a high-performing system would be close to a fully general system where $K$ was much larger (e.g., the Web or a filtered subset), encompassing many more qualitative relationships, and able to answer arbitrary questions of this kind. Scaling further would thus require more sophisticated retrieval over a larger corpus, and (sometimes) chaining across influences, when a direct connection was not described in the corpus. QuaRTz thus provides a dataset towards this end, allowing controlled experiments while still covering a substantial number of textual relations in an open setting. QuaRTz is available at http://data.allenai.org/quartz/.

#### Relevance 1018

Label: 

#### Passage 1019

Retrieved by: BM25, Dense, Hybrid

> Understanding and applying qualitative knowledge is a fundamental facet of intelligence. For example, we may read that exercise improves health, and thus decide to spend more time at the gym; or that larger cars cause more pollution, and thus decide to buy a smaller car to be environmentally sensitive. These skills require understanding the underlying qualitative relationships, and being able to apply them in specific contexts.
> 
> To promote research in this direction, we present the first open-domain dataset of qualitative relationship questions, called QuaRTz (“Qualitative Relationship Test set”). Unlike earlier work in qualitative reasoning, e.g., BIBREF0, the dataset is not restricted to a small, fixed set of relationships. Each question $Q_i$ (2-way multiple choice) is grounded in a particular situation, and is paired with a sentence $K_i$ expressing the general qualitative knowledge needed to answer it. $Q_i$ and $K_i$ are also annotated with the properties being compared (Figure FIGREF1). The property annotations serve as supervision for a potential semantic parsing based approach. The overall task is to answer the $Q_i$ given the corpus $K = \lbrace K_i\rbrace $.
> 
> We test several state-of-the-art (BERT-based) models and find that they are still substantially (20%) below human performance. Our contributions are thus (1) the dataset, containing 3864 richly annotated questions plus a background corpus of 400 qualitative knowledge sentences; and (2) an analysis of the dataset, performance of BERT-based models, and a catalog of the challenges it poses, pointing the way towards solutions.

#### Relevance 1019

Label: 

#### Passage 1020

Retrieved by: BM25, Dense, Hybrid

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

#### Relevance 1020

Label: 

### BM25

None

### Dense

None

### Hybrid

None

## Question 0133

Paper: Comparative Studies of Detecting Abusive Language on Twitter

> What additional features and context are proposed?

### Common Retrieved Chunks

#### Passage 1021

Retrieved by: BM25, Dense, Hybrid

> While manually analyzing the raw dataset, we noticed that looking at the tweet one has replied to or has quoted, provides significant contextual information. We call these, “context tweets". As humans can better understand a tweet with the reference of its context, our assumption is that computers also benefit from taking context tweets into account in detecting abusive language.
> 
> As shown in the examples below, (2) is labeled abusive due to the use of vulgar language. However, the intention of the user can be better understood with its context tweet (1).
> 
> (1) I hate when I'm sitting in front of the bus and somebody with a wheelchair get on.
> 
> INLINEFORM0 (2) I hate it when I'm trying to board a bus and there's already an as**ole on it.
> 
> Similarly, context tweet (3) is important in understanding the abusive tweet (4), especially in identifying the target of the malice.
> 
> (3) Survivors of #Syria Gas Attack Recount `a Cruel Scene'.
> 
> INLINEFORM0 (4) Who the HELL is “LIKE" ING this post? Sick people....
> 
> Huang et al. huang2016modeling used several attributes of context tweets for sentiment analysis in order to improve the baseline LSTM model. However, their approach was limited because the meta-information they focused on—author information, conversation type, use of the same hashtags or emojis—are all highly dependent on data.
> 
> In order to avoid data dependency, text sequences of context tweets are directly used as an additional feature of neural network models. We use the same baseline model to convert context tweets to vectors, then concatenate these vectors with outputs of their corresponding labeled tweets. More specifically, we concatenate max-pooled layers of context and labeled tweets for the CNN baseline model. As for RNN, the last hidden states of context and labeled tweets are concatenated.

#### Relevance 1021

Label: 

#### Passage 1022

Retrieved by: BM25, Dense, Hybrid

> While character-level features are known to improve the accuracy of neural network models BIBREF16 , they reduce classification accuracy for Hate and Abusive Speech on Twitter. We conclude this is because of the lack of labeled data as well as the significant imbalance among the different labels. Unlike neural network models, character-level features in traditional machine learning classifiers have positive results because we have trained the models only with the most significant character elements using TF-IDF values.
> 
> Variants of neural network models also suffer from data insufficiency. However, these models show positive performances on “spam" (14%) and “hateful" (4%) tweets—the lower distributed labels. The highest F1 score for “spam" is from the RNN-LTC model (0.551), and the highest for “hateful" is CNN with context tweets (0.309). Since each variant model excels in different metrics, we expect to see additional improvements with the use of ensemble models of these variants in future works.
> 
> In this paper, we report the baseline accuracy of different learning models as well as their variants on the recently introduced dataset, Hate and Abusive Speech on Twitter. Experimental results show that bidirectional GRU networks with LTC provide the most accurate results in detecting abusive language. Additionally, we present the possibility of using ensemble models of variant models and features for further improvements.

#### Relevance 1022

Label: 

#### Passage 1023

Retrieved by: BM25, Hybrid

> As shown in Table , neural network models are more accurate than feature engineering based models (i.e. NB, SVM, etc.) except for the LR model—the best LR model has the same F1 score as the best CNN model.
> 
> Among traditional machine learning models, the most accurate in classifying abusive language is the LR model followed by ensemble models such as GBT and RF. Character-level representations improve F1 scores of SVM and RF classifiers, but they have no positive effect on other models.
> 
> For neural network models, RNN with LTC modules have the highest accuracy score, but there are no significant improvements from its baseline model and its attention-added model. Similarly, HybridCNN does not improve the baseline CNN model. For both CNN and RNN models, character-level features significantly decrease the accuracy of classification.
> 
> The use of context tweets generally have little effect on baseline models, however they noticeably improve the scores of several metrics. For instance, CNN with context tweets score the highest recall and F1 for “hateful" labels, and RNN models with context tweets have the highest recall for “abusive" tweets.

#### Relevance 1023

Label: 

#### Passage 1026

Retrieved by: Dense, Hybrid

> This section illustrates our implementations on traditional machine learning classifiers and neural network based models in detail. Furthermore, we describe additional features and variant models investigated.

#### Relevance 1026

Label: 

#### Passage 1027

Retrieved by: Dense, Hybrid

> Along with traditional machine learning approaches, we investigate neural network based models to evaluate their efficacy within a larger dataset. In particular, we explore Convolutional Neural Networks (CNN), Recurrent Neural Networks (RNN), and their variant models. A pre-trained GloVe BIBREF17 representation is used for word-level features.
> 
> CNN: We adopt Kim's kim2014convolutional implementation as the baseline. The word-level CNN models have 3 convolutional filters of different sizes [1,2,3] with ReLU activation, and a max-pooling layer. For the character-level CNN, we use 6 convolutional filters of various sizes [3,4,5,6,7,8], then add max-pooling layers followed by 1 fully-connected layer with a dimension of 1024.
> 
> Park and Fung park2017one proposed a HybridCNN model which outperformed both word-level and character-level CNNs in abusive language detection. In order to evaluate the HybridCNN for this dataset, we concatenate the output of max-pooled layers from word-level and character-level CNN, and feed this vector to a fully-connected layer in order to predict the output.
> 
> All three CNN models (word-level, character-level, and hybrid) use cross entropy with softmax as their loss function and Adam BIBREF18 as the optimizer.
> 
> RNN: We use bidirectional RNN BIBREF19 as the baseline, implementing a GRU BIBREF20 cell for each recurrent unit. From extensive parameter-search experiments, we chose 1 encoding layer with 50 dimensional hidden states and an input dropout probability of 0.3. The RNN models use cross entropy with sigmoid as their loss function and Adam as the optimizer.
> 
> For a possible improvement, we apply a self-matching attention mechanism on RNN baseline models BIBREF21 so that they may better understand the data by retrieving text sequences twice. We also investigate a recently introduced method, Latent Topic Clustering (LTC) BIBREF22 . The LTC method extracts latent topic information from the hidden states of RNN, and uses it for additional information in classifying the text data.

#### Relevance 1027

Label: 

### BM25

#### Passage 1024

Retrieved by: BM25

> In the data preprocessing steps, user IDs, URLs, and frequently used emojis are replaced as special tokens. Since hashtags tend to have a high correlation with the content of the tweet BIBREF23 , we use a segmentation library BIBREF24 for hashtags to extract more information.
> 
> For character-level representations, we apply the method Zhang et al. zhang2015character proposed. Tweets are transformed into one-hot encoded vectors using 70 character dimensions—26 lower-cased alphabets, 10 digits, and 34 special characters including whitespace.

#### Relevance 1024

Label: 

#### Passage 1025

Retrieved by: BM25

> The research community introduced various approaches on abusive language detection. Razavi et al. razavi2010offensive applied Naïve Bayes, and Warner and Hirschberg warner2012detecting used Support Vector Machine (SVM), both with word-level features to classify offensive language. Xiang et al. xiang2012detecting generated topic distributions with Latent Dirichlet Allocation BIBREF12 , also using word-level features in order to classify offensive tweets.
> 
> More recently, distributed word representations and neural network models have been widely applied for abusive language detection. Djuric et al. djuric2015hate used the Continuous Bag Of Words model with paragraph2vec algorithm BIBREF13 to more accurately detect hate speech than that of the plain Bag Of Words models. Badjatiya et al. badjatiya2017deep implemented Gradient Boosted Decision Trees classifiers using word representations trained by deep learning models. Other researchers have investigated character-level representations and their effectiveness compared to word-level representations BIBREF14 , BIBREF15 .
> 
> As traditional machine learning methods have relied on feature engineering, (i.e. n-grams, POS tags, user information) BIBREF1 , researchers have proposed neural-based models with the advent of larger datasets. Convolutional Neural Networks and Recurrent Neural Networks have been applied to detect abusive language, and they have outperformed traditional machine learning classifiers such as Logistic Regression and SVM BIBREF15 , BIBREF16 . However, there are no studies investigating the efficiency of neural models with large-scale datasets over 100K.

#### Relevance 1025

Label: 

### Dense

#### Passage 1028

Retrieved by: Dense

> We implement five feature engineering based machine learning classifiers that are most often used for abusive language detection. In data preprocessing, text sequences are converted into Bag Of Words (BOW) representations, and normalized with Term Frequency-Inverse Document Frequency (TF-IDF) values. We experiment with word-level features using n-grams ranging from 1 to 3, and character-level features from 3 to 8-grams. Each classifier is implemented with the following specifications:
> 
> Naïve Bayes (NB): Multinomial NB with additive smoothing constant 1
> 
> Logistic Regression (LR): Linear LR with L2 regularization constant 1 and limited-memory BFGS optimization
> 
> Support Vector Machine (SVM): Linear SVM with L2 regularization constant 1 and logistic loss function
> 
> Random Forests (RF): Averaging probabilistic predictions of 10 randomized decision trees
> 
> Gradient Boosted Trees (GBT): Tree boosting with learning rate 1 and logistic loss function

#### Relevance 1028

Label: 

### Hybrid

None

## Question 0134

Paper: Mitigating Annotation Artifacts in Natural Language Inference Datasets to Improve Cross-dataset Generalization Ability

> How does the proposed training framework mitigate the bias pattern?

### Common Retrieved Chunks

#### Passage 1030

Retrieved by: BM25, Dense, Hybrid

> In this paper, we take a close look at the annotation artifacts in NLI datasets. We find that the bias pattern could be predictive or misleading in cross-dataset testing. Furthermore, we propose a debiasing framework and experiments demonstrate that it can effectively mitigate the impacts of the bias pattern and improve the cross-dataset generalization ability of models. However, it remains an open problem that how we should treat the annotation artifacts. We cannot assert whether the bias pattern should not exist at all or it is actually some kind of nature. We hope that our findings will encourage more explorations on reliable evaluation protocols for NLI models.

#### Relevance 1030

Label: 

#### Passage 1031

Retrieved by: BM25, Dense, Hybrid

> Essentially speaking, the problem of the bias pattern is that the artifacts in hypotheses are distributed differently among labels, so balancing them across labels may be a good solution to alleviate the impacts BIBREF2.
> 
> Based on the idea proposed by BIBREF12, we demonstrate that we can make artifacts in biased datasets balanced across different classes by assigning specific weights for every sample. We refer the distribution of the acquired weighted dataset as artifact-balanced distribution. We consider a supervised NLI task, which is to predict the relationship label $y$ given a sentence pair $x$, and we denote the hypothesis in $x$ as $h$. Without loss of generality, we assume that the prior probability of different labels is equal, and then we have the following theorem.
> 
> Theorem 1 For any classifier $f=f(x, h)$, and for any loss function $\Delta (f(x, h), y)$, if we use $w = \frac{1}{P(y|h)}$ as weight for every sample during training, it's equivalent to training with the artifact-balanced distribution.
> 
> Detailed assumptions and the proof of the theorem is presented in Appendix SECREF6. With the theorem, we can simply use cross predictions to estimate $P(y|h)$ in origin datasets and use them as sample weights during training. The step-by-step procedure for artifact-balanced learning is presented in Algorithm 1.
> 
> However, it is difficult to precisely estimate the probability $P(y|h)$. A minor error might lead to a significant difference to the weight, especially when the probability is close to zero. Thus, in practice, we use $w = \frac{1}{(1-\epsilon )P(y|h) + \epsilon }$ as sample weights during training in order to improve the robustness. We can find that as $\epsilon $ increases, the weights tend to be uniform, indicating that the debiasing effect decreases as the smooth term grows. Moreover, in order to keep the prior probability $P(Y)$ unchanged, we normalize the sum of weights of the three labels to the same.

#### Relevance 1031

Label: 

#### Passage 1032

Retrieved by: BM25, Dense, Hybrid

> Natural language inference (NLI) is a widely-studied problem in natural language processing. It aims at comparing a pair of sentences (i.e. a premise and a hypothesis), and inferring the relationship between them (i.e., entailment, neutral and contradiction). Large-scaled datasets like SNLI BIBREF0 and MultiNLI BIBREF1 have been created by crowd-sourcing and fertilized NLI research substantially.
> 
> However, several works BIBREF2, BIBREF3, BIBREF4 have pointed out that crowd-sourcing workers have brought a bias pattern named annotation artifacts in these NLI datasets. Such artifacts in hypotheses can reveal the labels and make it possible to predict the labels solely by looking at the hypotheses. For example, models trained on SNLI with only the hypotheses can achieve an accuracy of 67.0%, despite the always predicting the majority-class baseline is only 34.3% BIBREF2.
> 
> Classifiers trained on NLI datasets are supposed to make predictions by understanding the semantic relationships between given sentence pairs. However, it is shown that models are unintentionally utilizing the annotation artifacts BIBREF4, BIBREF2. If the evaluation is conducted under a similar distribution as the training data, e.g., with the given testing set, models will enjoy additional advantages, making the evaluation results over-estimated. On the other hand, if the bias pattern cannot be generalized to the real-world, it may introduce noise to models, thus hurting the generalization ability.
> 
> In this paper, we use cross-dataset testing to better assess models' generalization ability. We investigate the impacts of annotation artifacts in cross-dataset testing. Furthermore, we propose an easy-adopting debiasing training framework, which doesn't require any additional data or annotations, and apply it to the high-performing Densely Interactive Inference Network BIBREF5. Experiments show that our method can effectively mitigate the bias pattern and improve the cross-dataset generalization ability of models. To the best of our knowledge, our work is the first attempt to alleviate the annotation artifacts without any extra resources.

#### Relevance 1032

Label: 

#### Passage 1033

Retrieved by: BM25, Dense, Hybrid

> Frequently-used NLI datasets such as SNLI and MultiNLI are created by crowd-sourcing BIBREF0, BIBREF1, during which they present workers a premise and ask them to produce three hypotheses corresponding to labels. As BIBREF2 pointed out, workers may adopt some specific annotation strategies and heuristics when authoring hypotheses to save efforts, which produces certain patterns called annotation artifacts in the data. Models' trained on such datasets are heavily affected by the bias pattern BIBREF2.
> 
> BIBREF4 further investigate models' robustness to the bias pattern using swapping operations. BIBREF6 demonstrate that the annotation artifacts widely exist among NLI datasets. They show that hypothesis-only-model, which refers to models trained and predict only with hypotheses, outperforms always predicting the majority-class in six of ten NLI datasets.
> 
> The emergence of the pattern can be due to selection bias BIBREF7, BIBREF8, BIBREF9 in the datasets preparing procedure. Several works BIBREF10, BIBREF11 investigate the bias problem in relation inference datasest. BIBREF12 investigate the selection bias embodied in the comparing relationships in six natural language sentence matching datasets and propose a debiasing training and evaluation framework.

#### Relevance 1033

Label: 

#### Passage 1034

Retrieved by: Dense, Hybrid

> Debiasing may improve models' generalization ability from two aspects: (1) Mitigate the misleading effect of annotation artifacts. (2) Improve models' semantic learning ability.
> 
> When the annotation artifacts of the training set cannot be generalized to the testing set, which should be more common in the real-world, predicting by artifacts may hurt models' performance. Centering on the results of JOCI, in which the bias pattern of MultiNLI is misleading, we find that Norm trained with MultiNLI outperforms baseline after debiasing with all smooth values tested.
> 
> Furthermore, debiasing can reduce models' dependence on the bias pattern during training, thus force models to better learn semantic information to make predictions. Norm trained with SNLI exceed baseline in JOCI with smooth terms $0.01$ and $0.1$. With larger smooth terms, Norm trained with both SNLI and MultiNLI exceeds baseline in SICK. Given the fact that JOCI is almost neutral to artifacts in SNLI, and the bias pattern of both SNLI and MultiNLI are even predictive in SICK, we owe these promotions to that our method improves models' semantic learning ability.
> 
> As to other testing sets like SNLI, MMatch and MMismatch, we notice that the performance of Norm always decreases compared with the baseline. As mentioned before, both SNLI and MultiNLI are prepared by Huamn Elicited, and their artifacts can be generalized across each other. We owe the drop to that the detrimental effect of mitigating the predictable bias pattern exceeds the beneficial effect of the improvement of semantic learning ability.

#### Relevance 1034

Label: 

### BM25

#### Passage 1029

Retrieved by: BM25

> In this section, we present the experimental results for cross-dataset testing of artifacts and artifact-balanced learning. We show that cross-dataset testing is less affected by annotation artifacts, while there are still some influences more or less in different datasets. We also demonstrate that our proposed framework can mitigate the bias and improve the generalization ability of models.

#### Relevance 1029

Label: 

### Dense

None

### Hybrid

None

## Question 0135

Paper: Feature Studies to Inform the Classification of Depressive Symptoms from Twitter Data for Population Health

> Do they evaluate only on English datasets?

### Common Retrieved Chunks

#### Passage 1036

Retrieved by: BM25, Dense, Hybrid

> Feature elimination strategies are often taken 1) to remove irrelevant or noisy features, 2) to improve classifier performance, and 3) to reduce training and run times. We conducted an experiment to determine whether we could maintain or improve classifier performances by applying the following three-tiered feature elimination approach:
> 
> Reduction We reduced the dataset encoded for each class by eliminating features that occur less than twice in the full dataset.
> 
> Selection We iteratively applied Chi-Square feature selection on the reduced dataset, selecting the top percentile of highest ranked features in increments of 5 percent to train and test the support vector model using a linear kernel and 5-fold, stratified cross-validation.
> 
> Rank We cumulatively plotted the average F1-score performances of each incrementally added percentile of top ranked features. We report the percentile and count of features resulting in the first occurrence of the highest average F1-score for each class.
> 
> All experiments were programmed using scikit-learn 0.18.
> 
> The initial matrices of almost 17,000 features were reduced by eliminating features that only occurred once in the full dataset, resulting in 5,761 features. We applied Chi-Square feature selection and plotted the top-ranked subset of features for each percentile (at 5 percent intervals cumulatively added) and evaluated their predictive contribution using the support vector machine with linear kernel and stratified, 5-fold cross validation.
> 
> In Figure 2, we observed optimal F1-score performance using the following top feature counts: no evidence of depression: F1: 87 (15th percentile, 864 features), evidence of depression: F1: 59 (30th percentile, 1,728 features), depressive symptoms: F1: 55 (15th percentile, 864 features), depressed mood: F1: 39 (55th percentile, 3,168 features), disturbed sleep: F1: 46 (10th percentile, 576 features), and fatigue or loss of energy: F1: 72 (5th percentile, 288 features) (Figure 1). We note F1-score improvements for depressed mood from F1: 13 at the 1st percentile to F1: 33 at the 20th percentile.
> 
> We observed peak F1-score performances at low percentiles for fatigue or loss of energy (5th percentile), disturbed sleep (10th percentile) as well as depressive symptoms and no evidence of depression (both 15th percentile) suggesting fewer features are needed to reach optimal performance. In contrast, peak F1-score performances occurred at moderate percentiles for evidence of depression (30th

#### Relevance 1036

Label: 

#### Passage 1037

Retrieved by: BM25, Dense, Hybrid

> Specifically, we conducted a feature ablation study to assess the informativeness of each feature group and a feature elimination study to determine the optimal feature sets for classifying Twitter tweets. We leveraged an existing, annotated Twitter dataset that was constructed based on a hierarchical model of depression-related symptoms BIBREF12 , BIBREF13 . The dataset contains 9,473 annotations for 9,300 tweets. Each tweet is annotated as no evidence of depression (e.g., “Citizens fear an economic depression") or evidence of depression (e.g., “depressed over disappointment"). If a tweet is annotated evidence of depression, then it is further annotated with one or more depressive symptoms, for example, depressed mood (e.g., “feeling down in the dumps"), disturbed sleep (e.g., “another restless night"), or fatigue or loss of energy (e.g., “the fatigue is unbearable") BIBREF10 . For each class, every annotation (9,473 tweets) is binarized as the positive class e.g., depressed mood=1 or negative class e.g., not depressed mood=0.

#### Relevance 1037

Label: 

#### Passage 1038

Retrieved by: BM25, Hybrid

> Furthermore, this dataset was encoded with 7 feature groups with associated feature values binarized (i.e., present=1 or absent=0) to represent potentially informative features for classifying depression-related classes. We describe the feature groups by type, subtype, and provide one or more examples of words representing the feature subtype from a tweet:
> 
> lexical features, unigrams, e.g., “depressed”;
> 
> syntactic features, parts of speech, e.g., “cried” encoded as V for verb;
> 
> emotion features, emoticons, e.g., :( encoded as SAD;
> 
> demographic features, age and gender e.g., “this semester” encoded as an indicator of 19-22 years of age and “my girlfriend” encoded as an indicator of male gender, respectively;
> 
> sentiment features, polarity and subjectivity terms with strengths, e.g., “terrible” encoded as strongly negative and strongly subjective;
> 
> personality traits, neuroticism e.g., “pissed off” implies neuroticism;
> 
> LIWC Features, indicators of an individual's thoughts, feelings, personality, and motivations, e.g., “feeling” suggestions perception, feeling, insight, and cognitive mechanisms experienced by the Twitter user.
> 
> A more detailed description of leveraged features and their values, including LIWC categories, can be found in BIBREF10 .
> 
> Based on our prior initial experiments using these feature groups BIBREF10 , we learned that support vector machines perform with the highest F1-score compared to other supervised approaches. For this study, we aim to build upon this work by conducting two experiments: 1) to assess the contribution of each feature group and 2) to determine the optimal percentile of top ranked features for classifying Twitter tweets in the depression schema hierarchy.

#### Relevance 1038

Label: 

#### Passage 1039

Retrieved by: BM25, Dense, Hybrid

> Feature ablation studies are conducted to assess the informativeness of a feature group by quantifying the change in predictive power when comparing the performance of a classifier trained with the all feature groups versus the performance without a particular feature group. We conducted a feature ablation study by holding out (sans) each feature group and training and testing the support vector model using a linear kernel and 5-fold, stratified cross-validation. We report the average F1-score from our baseline approach (all feature groups) and report the point difference (+ or -) in F1-score performance observed by ablating each feature set.
> 
> By ablating each feature group from the full dataset, we observed the following count of features - sans lexical: 185, sans syntactic: 16,935, sans emotion: 16,954, sans demographics: 16,946, sans sentiment: 16,950, sans personality: 16,946, and sans LIWC: 16,832. In Figure 1, compared to the baseline performance, significant drops in F1-scores resulted from sans lexical for depressed mood (-35 points), disturbed sleep (-43 points), and depressive symptoms (-45 points). Less extensive drops also occurred for evidence of depression (-14 points) and fatigue or loss of energy (-3 points). In contrast, a 3 point gain in F1-score was observed for no evidence of depression. We also observed notable drops in F1-scores for disturbed sleep by ablating demographics (-7 points), emotion (-5 points), and sentiment (-5 points) features. These F1-score drops were accompanied by drops in both recall and precision. We found equal or higher F1-scores by removing non-lexical feature groups for no evidence of depression (0-1 points), evidence of depression (0-1 points), and depressive symptoms (2 points).
> 
> Unsurprisingly, lexical features (unigrams) were the largest contributor to feature counts in the dataset. We observed that lexical features are also critical for identifying depressive symptoms, specifically for depressed mood and for disturbed sleep. For the classes higher in the hierarchy - no evidence of depression, evidence of depression, and depressive symptoms - the classifier produced consistent F1-scores, even slightly above the baseline for depressive symptoms and minor fluctuations of change in recall and precision when removing other feature groups suggesting that the contribution of non-lexical features to classification performance was limited. However, notable changes in F1-score were observed for

#### Relevance 1039

Label: 

#### Passage 1041

Retrieved by: Dense, Hybrid

> From our annotated dataset of Twitter tweets (n=9,300 tweets), we conducted two feature studies to better understand the predictive power of several feature groups for classifying whether or not a tweet contains no evidence of depression (n=6,829 tweets) or evidence of depression (n=2,644 tweets). If there was evidence of depression, we determined whether the tweet contained one or more depressive symptoms (n=1,656 tweets) and further classified the symptom subtype of depressed mood (n=1,010 tweets), disturbed sleep (n=98 tweets), or fatigue or loss of energy (n=427 tweets) using support vector machines. From our prior work BIBREF10 and in Figure 1, we report the performance for prediction models built by training a support vector machine using 5-fold, stratified cross-validation with all feature groups as a baseline for each class. We observed high performance for no evidence of depression and fatigue or loss of energy and moderate performance for all remaining classes.

#### Relevance 1041

Label: 

### BM25

#### Passage 1035

Retrieved by: BM25

> Research reported in this publication was supported by the National Library of Medicine of the [United States] National Institutes of Health under award numbers K99LM011393 and R00LM011393. This study was granted an exemption from review by the University of Utah Institutional Review Board (IRB 00076188). Note that in order to protect tweeter anonymity, we have not reproduced tweets verbatim. Example tweets shown were generated by the researchers as exemplars only. Finally, we would like to thank the anonymous reviewers of this paper for their valuable comments.

#### Relevance 1035

Label: 

### Dense

#### Passage 1040

Retrieved by: Dense

> above the baseline for depressive symptoms and minor fluctuations of change in recall and precision when removing other feature groups suggesting that the contribution of non-lexical features to classification performance was limited. However, notable changes in F1-score were observed for the classes lower in the hierarchy including disturbed sleep and fatigue or loss of energy. For instance, changes in F1-scores driven by both recall and precision were observed for disturbed sleep by ablating demographics, emotion, and sentiment features, suggesting that age or gender (“mid-semester exams have me restless”), polarity and subjective terms (“lack of sleep is killing me”), and emoticons (“wide awake :(”) could be important for both identifying and correctly classifying a subset of these tweets.

#### Relevance 1040

Label: 

### Hybrid

None

## Question 0136

Paper: A survey of cross-lingual features for zero-shot cross-lingual semantic parsing

> How big is the Parallel Meaning Bank?

### Common Retrieved Chunks

#### Passage 1042

Retrieved by: BM25, Dense, Hybrid

> Semantic parsing is a task of transducing natural language to meaning representations, which in turn can be expressed through many different semantic formalisms including lambda calculus BIBREF1, DCS BIBREF2, Discourse Representation Theory (DRT) BIBREF3, AMR BIBREF4 and so on. This availability of annotated data in English has translated into the development of a plethora of models, including encoder-decoders BIBREF5, BIBREF6 as well as tree or graph-structured decoders BIBREF5, BIBREF7, BIBREF0, BIBREF8.
> 
> Whereas the majority of semantic banks focus on English, recent effort has focussed on building multilingual representations, e.g. PMB BIBREF9, MRS BIBREF10 and FrameNetBIBREF11. However, manually annotating meaning representations in a new language is a painstaking process which explains why there are only a few datasets available for different formalisms in languages other than English. As a consequence, whereas the field has made great advances for English, little work has been done in other languages.
> 
> We ask: can we learn a semantic parser for English and test it where in another where annotations are not available? What would that require?
> 
> To answer this question, previous work have leveraged machine translation techniques to map the semantics from a language to another BIBREF12. However, these methods require parallel corpora to extract automatic alignments which are often noisy or not available at all.
> 
> In this paper we explore parameter-shared models instead, where a model is trained on English using language independent features and tested in a target language.
> 
> To show how this approach performs, we focus on the Parallel Meaning Bank BIBREF13 – a multilingual semantic bank, where sentences in English, German, Italian and Dutch have been annotated with their meaning representations. The annotations in the PMB are based on Discourse Representation Theory BIBREF3, a popular theory of meaning representation designed to account for intra and inter-sentential phenomena, like temporal expressions and anaphora. Figure 1 shows an example DRT for the sentence `I sat down and opened my laptop' in its canonical `box' representation. A DRS is a nested structure with the top part containing the discourse references and the bottom with unary and binary predicates, as well as semantic constants (e.g. `speaker'). DRS can be linked to each other via logic operator (e.g. $\lnot $, $\rightarrow

#### Relevance 1042

Label: 

#### Passage 1043

Retrieved by: BM25, Dense, Hybrid

> Previous work have explored two main methods for cross-lingual semantic parsing. One method requires parallel corpora to extract alignments between source and target languages using machine translation BIBREF11, BIBREF22, BIBREF23 The other method is to use parameter-shared models in the target language and the source language by leveraging language-independent features such as multilingual word embeddings, Universal POS tags and UD BIBREF24, BIBREF25, BIBREF26, BIBREF27. For semantic parsing, encoder-decoder models have achieved great success. Amongst these, tree or graph-structured decoders have recently shown to be state-of-the-art BIBREF5, BIBREF7, BIBREF0, BIBREF28, BIBREF8.

#### Relevance 1043

Label: 

#### Passage 1044

Retrieved by: BM25, Hybrid

> a nested structure with the top part containing the discourse references and the bottom with unary and binary predicates, as well as semantic constants (e.g. `speaker'). DRS can be linked to each other via logic operator (e.g. $\lnot $, $\rightarrow $, $\diamond $) or, as in this case, discourse relations (e.g. CONTINUATION, RESULT, ELABORATION, etc.).
> 
> To test our approach we leverage the DRT parser of liu2018discourse, an encoder-decoder architecture where the meaning representation is reconstructed in three stages, coarse-to-fine, by first building the DRS skeleton (i.e. the `box' structures) and then fill each DRS with predicates and variables. Whereas the original parser utilizes a sequential Bi-LSTM encoder with monolingual lexical features, we experiment with language-independent features in the form of cross-lingual word-embeddings, universal PoS tags and universal dependencies. In particular, we also make use of tree encoders to assess whether modelling syntax can be beneficial in cross-lingual settings, as shown for other semantic tasks (e.g. negation scope detection BIBREF14).
> 
> Results show that language-independent features are a valid alternative to projection methods for cross-lingual semantic parsing. We show that adding dependency relation as features is beneficial, even when they are the only feature used during encoding. However, we also show that modeling the dependency structure directly via tree encoders does not outperform a sequential BiLSTM architecture for the three languages we have experimented with.

#### Relevance 1044

Label: 

#### Passage 1046

Retrieved by: BM25, Dense, Hybrid

> We use the PMB v.2.1.0 for the experiments. The dataset consists of 4405 English sentences, 1173 German sentences, 633 Italian sentences and 583 Dutch sentences. We divide the English sentences into 3072 training sentences, 663 development and 670 testing sentences. We consider all the sentences in other languages as test set.
> 
> In order to be used as input to the parser, liu2018discourse first convert the DRS into tree-based representations, which are subsequently linearized into PTB-style bracketed sequences. This transformation is lossless in that re-entrancies are duplicated to fit in the tree structure. We use the same conversion in this work; for further detail we refer the reader to the original paper.
> 
> Finally, it is worth noting that lexical predicates in PMB are in English, even for non-English languages. Since this is not compatible with our copy mechanism, we revert predicates to their original language by substituting them with the lemmas of the tokens they are aligned to (since gold alignment information is included in the PMB).

#### Relevance 1046

Label: 

#### Passage 1047

Retrieved by: Dense, Hybrid

> We use Counter BIBREF20 to evaluate the performance of our models. Counter looks for the best alignment between the predicted and gold DRS and computes precision, recall and F1. For further details about Counter, the reader is referred to van2018evaluating. It is worth reminding that unlike other work on the PMB BIBREF21, BIBREF0 does not deal with presupposition. In the PMB, presupposed variables are extracted from a main box and included in a separate one. In our work, we revert this process so to ignore presupposed boxes. Similarly, we also do not deal with sense tags which we aim to include in future work.

#### Relevance 1047

Label: 

### BM25

#### Passage 1045

Retrieved by: BM25

> BiLSTM. We use BIBREF0's Bi-LSTM as baseline. However, whereas the original model represents each token in the input sentence as the concatenation of word ($e_{w_i}$) and lemma embeddings, we discard the latter and add a POS tag embedding ($e_{p_i}$) and dependency relation embedding ($e_{d_i}$) feature. These embeddings are concatenated to represent the input token. The final encoder representation is obtained by concatenating both final forward and backward hidden states.
> 
> TreeLSTM. To model the dependency structure directly, we use a child-sum tree-LSTM BIBREF15, where each word in the input sentence corresponds to a node in the dependency tree. In particular, summing across children is advantageous for cross-lingual tasks since languages might display different word orders. Computation follows Equation (1).
> 
> Po/treeLSTM. Completely discarding word order might hurt performance for related languages, where a soft notion of positioning can help. To this end, we add a positional embeddings $P_i$ BIBREF16 that helps the child-sum tree-LSTM discriminating between the left and right child of a parent node. This is computed following Equation (2) where $i$ is the position of the word, $j$ is the $jth$ dimension in total $d$ dimensions.
> 
> Bi/treeLSTM. Finally, similarly to chen2017improved, we combine tree-LSTM and Bi-LSTM, where a tree-LSTM come is initialized using the last layer of a Bi-LSTM, which encodes order information. Computation is shown in Equation (3).

#### Relevance 1045

Label: 

### Dense

#### Passage 1048

Retrieved by: Dense

> In this section, we describe the modifications to the coarse-to-fine encoder-decoder architecture of BIBREF0; for more detail, we refer the reader to the original paper.

#### Relevance 1048

Label: 

### Hybrid

None

## Question 0137

Paper: autoNLP: NLP Feature Recommendations for Text Analytics Applications

> What are meta elements of language for specifying NLP features?

### Common Retrieved Chunks

#### Passage 1049

Retrieved by: BM25, Dense, Hybrid

> Figure FIGREF4 specifies the meta elements of the nlpFSpL which are used by the FExSys while interpreting other features.
> 
> Analysis Unit (AU) specifies level at which features have to be extracted. At Corpus level, features are extracted for all the text documents together. At Document level, features are extracted for each document in corpus separately. At Para (paragraph) level Features are extracted for multiple sentences constituting paragraphs together. At Sentence level features to be extracted for each sentence. Figure FIGREF6 depicts classes of features considered in nlpFSpL and their association with different AUs.
> 
> Syntactic Unit (SU) specifies unit of linguistic features. It could be a `Word' or a `Phrase', or a `N-gram' or a sequence of words matching specific lexico-syntactic pattern captured as `POS tag pattern' (e.g., Hearst pattern BIBREF15) or a sequence of words matching specific regular expression `Regex' or a combination of these. Option Regex is used for special types of terms, e.g., Dates, Numbers, etc. LOGICAL is a Boolean logical operator including AND, OR and NOT (in conjunction with other operator). For example, Phrase AND POS Regex would specify inclusion of a `Phrase' as SU when its constituents also satisfy 'regex' of `POS tags'. Similarly, POS Regex OR NOT(Regex) specifies inclusion of sequence of words as SU if it satisfies `POS tag Pattern' but does not match pattern specified by character `Regex'. Note that SU can be a feature in itself for document and corpus level analysis.
> 
> Normalize Morphosyntactic Variants: If YES, variants of words including stems, lemmas, and fuzzy matches will be identified before analyzing input text for feature exaction and would be treated equivalent.

#### Relevance 1049

Label: 

#### Passage 1050

Retrieved by: BM25, Dense, Hybrid

> Figure FIGREF1 depicts typical design life cycle of a (traditional) ML based solution for the TA applications, which involves steps to manually define relevant features and implement code components to extract those feature from input text corpus during training, validation, testing and actual usage of the application. In traditional ML based solutions, feature interactions also need to be explicitly specified, though this step is largely automated when using deep neural network based solutions BIBREF9.
> 
> As the process of defining features is manual, prior experience and expertize of the designer affects which features to extract and how to extract these features from input text. Current practice lacks standardization and automation in feature definition process, provides partial automation in extraction process, and does not enable automated reuse of features across related application.
> 
> Next, let us consider scenarios when features are specified as elements of a language. Let us refer to this language as NLP Feature Specification Language (nlpFSpL) such that a program in nlpFSpL would specify which features should be used by the underlying ML based solution to achieve goals of the target application. Given a corpus of unstructured natural language text data and a specifications in the nlpFSpL, an interpreter can be implemented as feature extraction system (FExSys) to automatically generate feature matrix which can be directly used by underlying ML technique.
> 
> In contrast to the life-cycle view in the Figure FIGREF1, this would result into refined solution life cycle of ML based TA applications as depicted in the Figure FIGREF2.

#### Relevance 1050

Label: 

#### Passage 1051

Retrieved by: BM25, Dense, Hybrid

> feature engineering. We start with an outline of a language for expressing NLP features abstracting over the feature extraction process, which often implicitly captures intent of the NLP data scientist to extract specific features from given input text. We next discuss a method to enable automated reuse of features across semantically related applications when a corpus of feature specifications for related applications is available. Proposed language and system would help achieving reduction in manual effort towards design and extraction of features, would ensure standardization in feature specification process, and could enable effective reuse of features across similar and/or related applications.

#### Relevance 1051

Label: 

#### Passage 1052

Retrieved by: BM25, Dense, Hybrid

> For an ever increasing spectrum of applications (e.g., medical text analysis, opinion mining, sentiment analysis, social media text analysis, customer intelligence, fraud analytics etc.) mining and analysis of unstructured natural language text data is necessary BIBREF0, BIBREF1, BIBREF2.
> 
> One of key challenge while designing such text analytics (TA) applications is to identify right set of features. For example, for text classification problem, different sets of features have been considered in different works (spanning a history of more than twenty years) including `bag of words', `bag of phrases', `bag of n-grams', `WordNet based word generalizations', and `word embeddings' BIBREF3, BIBREF4, BIBREF5, BIBREF6, BIBREF7. Even for recent end-to-end designs using deep neural networks, specification of core features remains manually driven BIBREF8, BIBREF9. During feature engineering, often data scientists manually determine which features to use based upon their experience and expertise with respect to the underlying application domain as well as state-of-the-art tools and techniques. Different tools (e.g., NLTK BIBREF10, Mallet BIBREF11, Stanford CoreNLP BIBREF12, Apache OpenNLP BIBREF13, Apache Lucene BIBREF14, etc.) available to a NLP data scientist for TA application design and development often differ in terms of support towards extraction of features, level of granularity at which feature extraction process is to be specified; and these tools often use different programing vocabularies to specify semantically equivalent features.
> 
> Currently, there is no generic method or approach, which can be applied during TA application's design process to define and extract features for any arbitrary application in an automated or semi-automated manner. Even there is no single way to express wide range of NLP features, resulting into increased efforts during feature engineering which has to start new for each data scientist and automated reuse of features across semantically similar or related applications designed by different data scientists is difficult. This also hinders foundational studies on NLP feature engineering including why certain features are more critical than others.
> 
> In this paper, we aim to present an approach towards automating NLP feature engineering. We start with an outline of a language for expressing NLP features abstracting over the feature extraction process, which often implicitly captures intent of the NLP data scientist to extract specific features from given input text. We next

#### Relevance 1052

Label: 

#### Passage 1054

Retrieved by: Dense, Hybrid

> In this paper, we have presented high level overview of a feature specification language for ML based TA applications and an approach to enable reuse of feature specifications across semantically related applications. Currently, there is no generic method or approach, which can be applied during TA applications' design process to define and extract features for any arbitrary application in an automated or semi-automated manner primarily because there is no standard way to specify wide range of features which can be extracted and used. We considered different classes of features including linguistic, semantic, and statistical for various levels of analysis including words, phrases, sentences, paragraphs, documents, and corpus. As a next step, we presented an approach for building a recommendation system for enabling automated reuse of features for new application scenarios which improves its underlying similarity model based upon user feedback.
> 
> To take this work forward, it is essential to have it integrated to a ML platform, which is being used by large user base for building TA applications so that to be able to populate a repository of statistically significant number of TA applications with details as specified in Section SECREF5 and thereafter refine the proposed approach so that eventually it rightly enables reuse of features across related applications.

#### Relevance 1054

Label: 

### BM25

#### Passage 1053

Retrieved by: BM25

> Figure FIGREF23 depicts overall process flow for enabling automated feature recommendations.
> 
> For a new text analytics application requiring feature engineering, it starts with estimating its semantic proximity (from the perspective of a NLP data scientist) with existing applications with known features. Based upon these proximity estimates as well as expected relevance of features for existing applications, system would recommend features for the new application in a ranked order. Furthermore, if user's selections are not aligned with system's recommendations, system gradually adapts its recommendation so that eventually it can achieve alignment with user preferences.
> 
> Towards that let us start with characterizing text analytics applications. A TA application's details should include following fields:
> 
> Text based description of an TA application (or problem). For example, “identify medical procedures being referenced in a discharge summary” or “what are the input and output entities mentioned in a software requirements specification”.
> 
> Analysis unit at which features are to be specified and training annotations are available, and ML model is designed to give outcomes. Options include word, phrase, sentence, paragraph, or document.
> 
> Specifies technical classification of the underlying ML challenge with respect to a well-defined ontology. E.g., Classification (with details), Clustering, etc.
> 
> Specifies how performance of the ML model is to be measured - again should be specified as per some well defined ontology.
> 
> Knowledge base of text analytics applications contains details for text analytics applications in above specified format. Each application is further assumed to be associated with a set of Features (or feature types) specified in nlpFSpL together with their relevance scores against a performance metric. Relevance score of a feature is a measure of the extent to which this feature contributes to achieve overall performance of ML model while solving the underlying application. Relevance score may be estimated using any of the known feature selection metrics BIBREF25.
> 
> To specify knowledge base formally, let us assume that there are $m$ different applications and $k$ unique feature specifications across these applications applying same performance metric. Let us denote these as follows: $APPS=\lbrace App_1,\ldots , App_m\rbrace $ and ${\mathit {\Theta }}_F$ = $\left\lbrace F_1,F_2,\dots ,F_k\right\rbrace $ respectively. Knowledge base is then represented as a feature co-occurrence matrix $PF_{m\times k}$ such that $PF[i,j]

#### Relevance 1053

Label: 

### Dense

None

### Hybrid

None

## Question 0138

Paper: TENER: Adapting Transformer Encoder for Named Entity Recognition

> How do they incorporate direction and relative distance in attention?

### Common Retrieved Chunks

#### Passage 1055

Retrieved by: BM25, Dense, Hybrid

> using the equations below:
> 
> where $t$ is index of the target token, $j$ is the index of the context token, $Q_t, K_j$ is the query vector and key vector of token $t, j$ respectively, $W_q, W_v \in \mathbb {R}^{d \times d_k}$. To get $H_{d_k}\in \mathbb {R}^{l \times d_k}$, we first split $H$ into $d/d_k$ partitions in the second dimension, then for each head we use one partition. $\mathbf {u} \in \mathbb {R}^{d_k}$, $\mathbf {v} \in \mathbb {R}^{d_k}$ are learnable parameters, $R_{t-j}$ is the relative positional encoding, and $R_{t-j} \in \mathbb {R}^{d_k}$, $i$ in Eq.() is in the range $[0, \frac{d_k}{2}]$. $Q_t^TK_j$ in Eq.() is the attention score between two tokens; $Q_t^TR_{t-j}$ is the $t$th token's bias on certain relative distance; $u^TK_j$ is the bias on the $j$th token; $v^TR_{t-j}$ is the bias term for certain distance and direction.
> 
> Based on Eq.(), we have
> 
> because $\sin (-x)=-\sin (x), \cos (x)=\cos (-x)$. This means for an offset $t$, the forward and backward relative positional encoding are the same with respect to the $\cos (c_it)$ terms, but is the opposite with respect to the $\sin (c_it)$ terms. Therefore, by using $R_{t-j}$, the attention score can distinguish different directions and distances.
> 
> The above improvement is based on the work BIBREF17, BIBREF19. Since the size of NER datasets is usually small, we avoid direct multiplication of two learnable parameters, because they can be represented by one learnable parameter. Therefore we do not use $W_k$ in Eq.(DISPLAY_FORM22). The multi-head version is the same as Eq.(DISPLAY_FORM8), but we discard $W_o$ since it is directly multiplied by $W_1$ in Eq.(DISPLAY_FORM9).

#### Relevance 1055

Label: 

#### Passage 1056

Retrieved by: BM25, Dense, Hybrid

> directionality. In addition, this property will lose when used in the vanilla Transformer. However, both the direction and distance information are important in the NER task. For example in Fig FIGREF3, words after “in" are more likely to be a location or time than words before it, and words before “Inc." are mostly likely to be of the entity type “ORG". Besides, an entity is a continuous span of words. Therefore, the awareness of distance might help the word better recognizes its neighbor. To endow the Transformer with the ability of direction- and distance-awareness, we adopt the relative positional encoding BIBREF17, BIBREF18, BIBREF19. instead of the absolute position encoding. We propose a revised relative positional encoding that uses fewer parameters and performs better.
> 
> The second is an empirical finding. The attention distribution of the vanilla Transformer is scaled and smooth. But for NER, a sparse attention is suitable since not all words are necessary to be attended. Given a current word, a few contextual words are enough to judge its label. The smooth attention could include some noisy information. Therefore, we abandon the scale factor of dot-production attention and use an un-scaled and sharp attention.
> 
> With the above improvements, we can greatly boost the performance of Transformer encoder for NER.
> 
> Other than only using Transformer to model the word-level context, we also tried to apply it as a character encoder to model word representation with character-level information. The previous work has proved that character encoder is necessary to capture the character-level features and alleviate the out-of-vocabulary (OOV) problem BIBREF6, BIBREF5, BIBREF7, BIBREF20. In NER, CNN is commonly used as the character encoder. However, we argue that CNN is also not perfect for representing character-level information, because the receptive field of CNN is limited, and the kernel size of the CNN character encoder is usually 3, which means it cannot correctly recognize 2-gram or 4-gram patterns. Although we can deliberately design different kernels, CNN still cannot solve patterns with discontinuous characters, such as “un..ily” in “unhappily" and “unnecessarily". Instead, the Transformer-based character encoder shall not only fully make use of the concurrence power of GPUs, but also have the potentiality to recognize different n-grams and even

#### Relevance 1056

Label: 

#### Passage 1057

Retrieved by: BM25, Dense, Hybrid

> Transformer was introduced by BIBREF13, which was mainly based on self-attention. It achieved great success in various NLP tasks. Since the self-attention mechanism used in the Transformer is unaware of positions, to avoid this shortage, position embeddings were used BIBREF13, BIBREF15. Instead of using the sinusoidal position embedding BIBREF13 and learned absolute position embedding, BIBREF17 argued that the distance between two tokens should be considered when calculating their attention score. BIBREF18 reduced the computation complexity of relative positional encoding from $O(l^2d)$ to $O(ld)$, where $l$ is the length of sequences and $d$ is the hidden size. BIBREF19 derived a new form of relative positional encodings, so that the relative relation could be better considered.

#### Relevance 1057

Label: 

#### Passage 1058

Retrieved by: BM25, Hybrid

> In this paper, we propose TENER, a model adopting Transformer Encoder with specific customizations for the NER task. Transformer Encoder has a powerful ability to capture the long-range context. In order to make the Transformer more suitable to the NER task, we introduce the direction-aware, distance-aware and un-scaled attention. Experiments in two English NER tasks and four Chinese NER tasks show that the performance can be massively increased. Under the same pre-trained embeddings and external knowledge, our proposed modification outperforms previous models in the six datasets. Meanwhile, we also found the adapted Transformer is suitable for being used as the English character encoder, because it has the potentiality to extract intricate patterns from characters. Experiments in two English NER datasets show that the adapted Transformer character encoder performs better than BiLSTM and CNN character encoders.

#### Relevance 1058

Label: 

#### Passage 1059

Retrieved by: BM25, Dense, Hybrid

> Inspired by the success of BiLSTM in NER tasks, we consider what properties the Transformer lacks compared to BiLSTM-based models. One observation is that BiLSTM can discriminatively collect the context information of a token from its left and right sides. But it is not easy for the Transformer to distinguish which side the context information comes from.
> 
> Although the dot product between two sinusoidal position embeddings is able to reflect their distance, it lacks directionality and this property will be broken by the vanilla Transformer attention. To illustrate this, we first prove two properties of the sinusoidal position embeddings.
> 
> Property 1 For an offset $k$ and a position $t$, $PE_{t+k}^TPE_{t}$ only depends on $k$, which means the dot product of two sinusoidal position embeddings can reflect the distance between two tokens.
> 
> Based on the definitions of Eq.(DISPLAY_FORM11) and Eq.(), the position embedding of $t$-th token is PEt = [ c (c0t)
> 
> (c0t)
> 
> $\vdots $
> 
> (cd2-1t)
> 
> (cd2-1t)
> 
> ], where $d$ is the dimension of the position embedding, $c_i$ is a constant decided by $i$, and its value is $1/10000^{2i/d}$.
> 
> Therefore,
> 
> where Eq.(DISPLAY_FORM17) to Eq.() is based on the equation $\cos (x-y) = \sin (x)\sin (y) + \cos (x)\cos (y)$.
> 
> Property 2 For an offset $k$ and a position $t$, $PE_{t}^TPE_{t-k}=PE_{t}^TPE_{t+k}$, which means the sinusoidal position embeddings is unware of directionality.
> 
> Let $j=t-k$, according to property 1, we have
> 
> The relation between $d$, $k$ and $PE_t^TPE_{t+k}$ is displayed in Fig FIGREF18. The sinusoidal position embeddings are distance-aware but lacks directionality.
> 
> However, the property of distance-awareness also disappears when $PE_t$ is projected into the query and key space of self-attention. Since in vanilla Transformer the calculation between $PE_t$ and $PE_{t+k}$ is actually $PE_t^TW_q^TW_kPE_{t+k}$, where $W_q, W_k$ are parameters in Eq.(DISPLAY_FORM7). Mathematically, it can be viewed as $PE_t^TWPE_{t+k}$ with only one parameter $W$. The relation between $PE_t^TPE_{t+k}$ and $PE_t^TWPE_{t+k}$ is depicted in Fig FIGREF19.
> 
> Therefore, to improve the Transformer with direction- and distance-aware characteristic, we calculate the attention scores using the equations below:
> 
> where $t$ is index of the target token, $j$ is the index of the context token, $Q_t, K_j$ is the query vector and key vector of token $t, j$ respectively, $W_q, W_v \in \mathbb {R}^{d \times

#### Relevance 1059

Label: 

### BM25

None

### Dense

#### Passage 1060

Retrieved by: Dense

> The self-attention is not aware of the positions of different tokens, making it unable to capture the sequential characteristic of languages. In order to solve this problem, BIBREF13 suggested to use position embeddings generated by sinusoids of varying frequency. The $t$th token's position embedding can be represented by the following equations
> 
> where $i$ is in the range of $[0, \frac{d}{2}]$, $d$ is the input dimension. This sinusoid based position embedding makes Transformer have an ability to model the position of a token and the distance of each two tokens. For any fixed offset $k$, $PE_{t+k}$ can be represented by a linear transformation of $PE_{t}$ BIBREF13.

#### Relevance 1060

Label: 

### Hybrid

None

## Question 0139

Paper: Predicting Audience's Laughter Using Convolutional Neural Network

> How are the positive instances annotated? e.g. by annotators, or by laughter from the audience?

### Common Retrieved Chunks

#### Passage 1061

Retrieved by: BM25, Dense, Hybrid

> TED Talks are recordings from TED conferences and other special TED programs. In the present study, we focused on the transcripts of the talks. Most transcripts of the talks contain the markup `(Laughter)', which represents where audiences laughed aloud during the talks. This special markup was used to determine utterance labels.
> 
> We collected INLINEFORM0 TED Talk transcripts. An example transcription is given in Figure FIGREF4 . The collected transcripts were split into sentences using the Stanford CoreNLP tool BIBREF11 . In this study, sentences containing or immediately followed by `(Laughter)' were used as `Laughter' sentences, as shown in Figure FIGREF4 ; all other sentences were defined as `No-Laughter' sentences. Following BIBREF1 and BIBREF3 , we selected the same numbers ( INLINEFORM1 ) of `Laughter' and `No-Laughter' sentences. To minimize possible topic shifts between positive and negative instances, for each positive instance, we picked one negative instance nearby (the context window was 7 sentences in this study). For example, in Figure FIGREF4 , a negative instance (corresponding to `sent-2') was selected from the nearby sentences ranging from `sent-7' to `sent+7'.

#### Relevance 1061

Label: 

#### Passage 1062

Retrieved by: BM25, Dense, Hybrid

> For the purpose of monitoring how well speakers can use humor during their presentations, we have created a corpus from TED talks. Compared to the existing (albeit limited) corpora for humor recognition research, ours has the following advantages: (a) it was collected from authentic talks, rather than from TV shows performed by professional actors based on scripts; (b) it contains about 100 times more speakers compared to the limited number of actors in existing corpora. We compared two types of leading text-based humor recognition methods: a conventional classifier (e.g., Random Forest) based on human-engineered features vs. an end-to-end CNN method, which relies on its inherent representation learning. We found that the CNN method has better performance. More importantly, the representation learning of the CNN method makes it very efficient when facing new data sets.
> 
> Stemming from the present study, we envision that more research is worth pursuing: (a) for presentations, cues from other modalities such as audio or video will be included, similar to Bertero2016LREC; (b) context information from multiple utterances will be modeled by using sequential modeling methods.

#### Relevance 1062

Label: 

#### Passage 1063

Retrieved by: BM25, Dense, Hybrid

> The ability to make effective presentations has been found to be linked with success at school and in the workplace. Humor plays an important role in successful public speaking, e.g., helping to reduce public speaking anxiety often regarded as the most prevalent type of social phobia, generating shared amusement to boost persuasive power, and serving as a means to attract attention and reduce tension BIBREF0 .
> 
> Automatically simulating an audience's reactions to humor will not only be useful for presentation training, but also improve conversational systems by giving machines more empathetic power. The present study reports our efforts in recognizing utterances that cause laughter in presentations. These include building a corpus from TED talks and using Convolutional Neural Networks (CNNs) in the recognition.
> 
> The remainder of the paper is organized as follows: Section SECREF2 briefly reviews the previous related research; Section SECREF3 describes the corpus we collected from TED talks; Section SECREF4 describes the text classification methods; Section SECREF5 reports on our experiments; finally, Section SECREF6 discusses the findings of our study and plans for future work.

#### Relevance 1063

Label: 

#### Passage 1064

Retrieved by: BM25, Dense, Hybrid

> Humor recognition refers to the task of deciding whether a sentence/spoken-utterance expresses a certain degree of humor. In most of the previous studies BIBREF1 , BIBREF2 , BIBREF3 , humor recognition was modeled as a binary classification task. In the seminal work BIBREF1 , a corpus of INLINEFORM0 “one-liners" was created using daily joke websites to collect humorous instances while using formal writing resources (e.g., news titles) to obtain non-humorous instances. Three humor-specific stylistic features, including alliteration, antonymy, and adult slang were utilized together with content-based features to build classifiers. In a recent work BIBREF3 , a new corpus was constructed from the Pun of the Day website. BIBREF3 explained and computed latent semantic structure features based on the following four aspects: (a) Incongruity, (b) Ambiguity, (c) Interpersonal Effect, and (d) Phonetic Style. In addition, Word2Vec BIBREF4 distributed representations were utilized in the model building.
> 
> Beyond lexical cues from text inputs, other research has also utilized speakers' acoustic cues BIBREF2 , BIBREF5 . These studies have typically used audio tracks from TV shows and their corresponding captions in order to categorize characters' speaking turns as humorous or non-humorous. Utterances prior to canned laughter that was manually inserted into the shows were treated as humorous, while other utterances were treated as negative cases.
> 
> Convolutional Neural Networks (CNNs) have recently been successfully used in several text categorization tasks (e.g., review rating, sentiment recognition, and question type recognition). Kim2014,Johnson2015,Zhang2015 suggested that using a simple CNN setup, which entails one layer of convolution on top of word embedding vectors, achieves excellent results on multiple tasks. Deep learning recently has been applied to computational humor research BIBREF5 , BIBREF6 . In Bertero2016LREC, CNN was found to be the best model that uses both acoustic and lexical cues for humor recognition. By using Long Short Time Memory (LSTM) cells BIBREF7 , Bertero2016NAACL showed that Recurrent Neural Networks (RNNs) perform better on modeling sequential information than Conditional Random Fields (CRFs) BIBREF8 .
> 
> From the brief review, it is clear that corpora used in humor research so far are limited to one-line puns or jokes and conversations from TV comedy shows. There is a great need for an open corpus that can support

#### Relevance 1064

Label: 

#### Passage 1066

Retrieved by: Dense, Hybrid

> From the brief review, it is clear that corpora used in humor research so far are limited to one-line puns or jokes and conversations from TV comedy shows. There is a great need for an open corpus that can support investigating humor in presentations. CNN-based text categorization methods have been applied to humor recognition (e.g., in BIBREF5 ) but with limitations: (a) a rigorous comparison with the state-of-the-art conventional method examined in yang-EtAl:2015:EMNLP2 is missing; (b) CNN's performance in the previous research is not quite clear; and (c) some important techniques that can improve CNN performance (e.g., using varied-sized filters and dropout regularization BIBREF10 ) were not applied. Therefore, the present study is meant to address these limitations.

#### Relevance 1066

Label: 

### BM25

#### Passage 1065

Retrieved by: BM25

> Our CNN-based text classification's setup follows Kim2014. Figure FIGREF17 depicts the model's details. From the left side's input texts to the right side's prediction labels, different shapes of tensors flow through the entire network for solving the classification task in an end-to-end mode.
> 
> Firstly, tokenized text strings were converted to a INLINEFORM0 tensor with shape INLINEFORM1 , where INLINEFORM2 represents sentences' maximum length while INLINEFORM3 represents the word-embedding dimension. In this study, we utilized the Word2Vec BIBREF4 embedding vectors ( INLINEFORM4 ) that were trained on 100 billion words of Google News. Next, the embedding matrix was fed into a INLINEFORM5 convolution network with multiple filters. To cover varied reception fields, we used filters of sizes of INLINEFORM6 , INLINEFORM7 , and INLINEFORM8 . For each filter size, INLINEFORM9 filters were utilized. Then, max pooling, which stands for finding the largest value from a vector, was applied to each feature map (total INLINEFORM10 feature maps) output by the INLINEFORM11 convolution. Finally, maximum values from all of INLINEFORM12 filters were formed as a flattened vector to go through a fully connected (FC) layer to predict two possible labels (Laughter vs. No-Laughter). Note that for INLINEFORM13 convolution and FC layer's input, we applied `dropout' BIBREF10 regularization, which entails randomly setting a proportion of network weights to be zero during model training, to overcome over-fitting. By using cross-entropy as the learning metric, the whole sequential network (all weights and bias) could be optimized by using any SGD optimization, e.g., Adam BIBREF13 , Adadelta BIBREF14 , and so on.

#### Relevance 1065

Label: 

### Dense

None

### Hybrid

None

## Question 0140

Paper: "Wait, I'm Still Talking!"Predicting the Dialogue Interaction Behavior Using Imagine-Then-Arbitrate Model

> What is the source of their datasets?

### Common Retrieved Chunks

#### Passage 1067

Retrieved by: BM25, Dense, Hybrid

> As the proposed approach mainly concentrates on the interaction of human-computer, we select and modify two very different style datasets to test the performance of our method. One is a task-oriented dialogue dataset MultiWoz 2.0 and the other is a chitchat dataset DailyDialogue . Both datasets are collected from human-to-human conversations. We evaluate and compare the results with the baseline methods in multiple dimensions. Table TABREF28 shows the statistics of datasets.
> 
> MultiWOZ 2.0 BIBREF18. MultiDomain Wizard-of-Oz dataset (MultiWOZ) is a fully-labeled collection of human-human written conversations. Compared with previous task-oriented dialogue datasets, e.g. DSTC 2 BIBREF19 and KVR BIBREF20, it is a much larger multi-turn conversational corpus and across serveral domains and topics: It is at least one order of magnitude larger than all previous annotated task-oriented corpora, with dialogues spanning across several domains and topics.
> 
> DailyDialogue BIBREF21. DailyDialogue is a high-quality multi-turn dialogue dataset, which contains conversations about daily life. In this dataset, humans often first respond to previous context and then propose their own questions and suggestions. In this way, people show their attention others’ words and are willing to continue the conversation. Compare to the task-oriented dialogue datasets, the speaker's behavior will be more unpredictable and complex for the arbitrator.

#### Relevance 1067

Label: 

#### Passage 1068

Retrieved by: BM25, Hybrid

> In Table TABREF29, we show different imaginators' generation abilities and their performances on the same TextCNN based arbitrator. Firstly, we gathered the results of agent and user imaginators' generation based on LSTM, LSTM-attention and LSTM-attention with GLOVE pretrained word embedding. According to the evaluation metric BLEU, the latter two models achieve higher but similar results. Secondly, when fixed the arbitrator on the TextCNNs model, the latter two also get the similar results on accuracy and significantly outperform the others including the TextCNNs baseline.
> 
> The performances on different arbitrators with the same LSTM-attention imaginators are shown in Table TABREF30. From those results, we can directly compared with the corresponding baseline models. The imaginators with BERT based arbitrator make the best results in both datasets while all ITA models beat the baseline models.
> 
> We also present an example of how our model runs in Table TABREF37. Imaginators predict the agent and user's utterance according to the dialogue history(shown in model prediction), and then arbitrator selects the user imaginator's prediction that is more suitable with the dialogue history. It is worth noting that the arbitrator generates a high-quality sentence again if only considering the generation effect. However, referring to the dialogue history, it is not a good choice since its semantic is repeated in the last turn by the agent.

#### Relevance 1068

Label: 

#### Passage 1069

Retrieved by: BM25, Hybrid

> From Table TABREF30, we can see that not only our BERT based model get the best results in both datasets, the other two models also significantly beat the corresponding baselines. Even the TextCNNs based model can beat all baselines in both datasets.
> 
> Table TABREF29 figures out experiment results on MultiWOZ dataset. The LSTM based agent imaginator get the BLEU score at 11.77 on agent samples, in which the ground truth is agents' utterances, and 0.80 on user samples. Meanwhile, the user imaginator get the BLEU score at 0.3 on agent samples and 8.87 on user target samples. Similar results are shown in other imaginators' expermients. Although these comparisons seem unfair to some extends since we do not have the agent and user's real utterances at the same time and under the same dialogue history, these results show that the imaginators did learn the speaking style of agent and user respectively. So the suitable imaginator's generation will be more similar to the ground truth, such an example shown in Table TABREF37, which means this response more semantically suitable given the dialogue history.
> 
> If we fix the agent and user imaginators' model, as we take the LSTM-attention model, the arbitrators achieve different performances on different models, shown in Table TABREF30. As expected, ITA models beat their base models by nearly 2 $\sim $ 3% and ITA-BERT model beats all other ITA models.
> 
> So from the all results, we can conclude that imaginators will significantly help the arbitrator in predicting the dialogue interaction behavior using the future possible agent and user responses’ semantic information.

#### Relevance 1069

Label: 

#### Passage 1071

Retrieved by: BM25, Dense, Hybrid

> most important feature:
> 
> , and thus we get the final feature map of the input sequence.
> 
> We apply same CNNs to get the feature maps of $X$, $R_{agent}$ and $R_{user}$:
> 
> where function TextCNNs() follows as equations from DISPLAY_FORM20 to DISPLAY_FORM23. Then we will have two possible dialogue paths, $X$ with $R_{agent}$ and $X$ with $R_{user}$, representations $D_{agent}$ and $D_{user}$:
> 
> And then, the arbitrator will calculate the probability of the two possible dialogue paths:
> 
> Through learnt parameters $W_{4}$ and $b_{4}$, we will get a two-dimensional probability distribution $P$, in which the most reasonable response has the max probability. This also indicates whether the agent should wait or not.
> 
> And the total loss function of the whole attribution module will be negative log likelihood of the probability of choosing the correct action:
> 
> where $N$ is the number of samples and $Y_{i}$ is the ground truth label of i-th sample.
> 
> The arbitrator module based on Bi-GRU and BERT is implemented similar to TextCNNs.

#### Relevance 1071

Label: 

#### Passage 1072

Retrieved by: Dense, Hybrid

> Because the task we concentrate on is different from traditional ones, to make the datasets fit our problems and real life, we modify the datasets with the following steps:
> 
> Drop Slots and Values For task-oriented dialogue, slot labels are important for navigating the system to complete a specific task. However, those labels and accurate values from ontology files will not benefit our task essentially. So we replace all specific values with a slot placeholder in preprocessing step.
> 
> Split Utterances Existing datasets concentrate on the dialogue content, combining multiple sentences into one utterance each turn when gathering the data. In this step, we randomly split the combined utterance into multiple utterances according to the punctuation. And we set a determined probability to decide if the preprocessing program should split a certain sentence.
> 
> Add Turn Tag We add turn tags, subturn tags and role tags to each split and original sentences to (1) label the speaker role and dialogue turns (2) tag the ground truth for training and testing the supervised baselines and our model.
> 
> Finally, we have the modified datasets which imitate the real life human chatting behaviors as shown in Figure FIGREF1. Our datasets and code will be released to public for further researches in both academic and industry.

#### Relevance 1072

Label: 

### BM25

#### Passage 1070

Retrieved by: BM25

> We first address an interaction problem, whether the dialogue model should wait for the end of the utterance or reply directly in order to simulate user's real life conversation behavior, and propose a novel Imagine-then-Arbitrate (ITA) neural dialogue model to deal with it. Our model introduces the imagined future possible semantic information for prediction. We modified two popular dialogue datasets to fit in the real situation. It is reasonable that additional information is helpful for arbitrator, despite its fantasy.

#### Relevance 1070

Label: 

### Dense

#### Passage 1073

Retrieved by: Dense

> To compare with dataset baselines in multiple dimensions and test the model's performance, we use the overall Bilingual Evaluation Understudy (BLEU) BIBREF22 to evaluate the imaginators' generation performance. As for arbitrator, we use accuracy score of the classification to evaluate. Accuracy in our experiments is the correct ratio in all samples.

#### Relevance 1073

Label: 

#### Passage 1074

Retrieved by: Dense

> Though end-to-end methods play a more and more important role in dialogue system, the text classification modules BIBREF8, BIBREF9 remains very useful in many problems like emotion recognition BIBREF10, gender recognition BIBREF11, verbal intelligence, etc. There have been several widely used text classification methods proposed, e.g. Recurrent Neural Networks (RNNs) and CNNs. Typically RNN is trained to recognize patterns across time, while CNN learns to recognize patterns across space. BIBREF12 proposed TextCNNs trained on top of pre-trained word vectors for sentence-level classification tasks, and achieved excellent results on multiple benchmarks.
> 
> Besides RNNs and CNNs, BIBREF13 proposed a new network architecture called Transformer, based solely on attention mechanism and obtained promising performance on many NLP tasks. To make the best use of unlabeled data, BIBREF14 introduced a new language representation model called BERT based on transformer and obtained state-of-the-art results.

#### Relevance 1074

Label: 

### Hybrid

None
