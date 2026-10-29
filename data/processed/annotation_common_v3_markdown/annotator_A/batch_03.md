# Passage relevance annotation

Annotator: 

Enter your name or agreed identifier after `Annotator:`.

Judge whether each passage helps answer the question, including useful partial evidence. Topic overlap alone is insufficient.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Preserve all content and record numbers. Work independently; do not exchange labels before submission. Algorithm sources are disclosed.

## Question 0041

Paper: One Single Deep Bidirectional LSTM Network for Word Sense Disambiguation of Text Data

> Do they use pretrained word embeddings?

### Common Retrieved Chunks

#### Passage 365

Retrieved by: BM25, Dense, Hybrid RRF

> From the results of Table TABREF19 , we notice our single WSD network, despite eliminating the problem of having a large number of WSD classifiers, still falls short when is compared with the state-of-the-art WSD algorithms. Based on our intuition and supported by some of our preliminary experiments, this deficiency stems from an important factor in our BLSTM network. Since no sense embedding is made publicly available for use, the sense embeddings are initialized randomly; yet, word embeddings are initialized by pre-trained GloVe vectors in order to benefit from the semantic and syntactic properties of the context words conveyed by these embeddings. That is to say, the separate spaces that the sense embeddings and the (context) word embeddings come from enforces some delay for the alignment of these spaces which in turn demands more training data. Furthermore, this early misalignment does not allow the BLSTM fully take advantage of larger context sizes which can be helpful. Our first attempt to deal with such problem was to pre-train the sense embeddings by some techniques - such as taking the average of the GloVe embeddings of the (informative) definition content words of senses, or taking the average of the GloVe embeddings of the (informative) context words in their training samples - did not give us a better result than our random initialization. Our preliminary experiments though in which we replaced all GloVe embeddings in the network with sense embeddings (using a method proposed by Chen et al. BIBREF11 ), showed considerable improvements in the results of some ambiguous words. That means both senses and context words (while they can be ambiguous by themselves) come from one vector space. In other words, the context would also be represented by the possible senses that its words can take. This idea not only can help to improve the results of the current model, it can also avoid the need for a large amount of training data since senses can be seen in both places, center and context, to be trained.

#### Relevance 365

Label: 

#### Passage 366

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Between-all-models comparisons - When SensEval-3 task was launched 47 submissions (supervised and unsupervised algorithms) were received addressing this task. Afterward, some other papers tried to work on this data and reported their results in separate articles as well. We compare the result of our model with the top-performing and low-performing algorithms (supervised). We show our single model sits among the 5 top-performing algorithms, considering that in other algorithms for each ambiguous word one separate classifier is trained (i.e. in the same number of ambiguous words in a language there have to be classifiers; which means 57 classifiers for this specific task). Table TABREF19 shows the results of the top-performing and low-performing supervised algorithms.
> 
> The first two algorithms represent the state-of-the-art models of supervised WSD when evaluated on SensEval-3. Multi-classifier BLSTM BIBREF15 consists of deep neural networks which make use of pre-trained word embeddings. While the lower layers of these networks are shared, upper layers of each network are responsible to individually classify the ambiguous that word the network is associated with. IMS+adapted CW BIBREF16 is another WSD model that considers deep neural networks and also uses pre-trained word embeddings as inputs. In contrast to Multi-classifier BLSTM, this model relies on features such as POS tags, collocations, and surrounding words to achieve their result. For these two models, softmax constitutes the output layers of all networks. htsa3 BIBREF22 was the winner of the SensEval-3 lexical sample. It is a Naive Bayes system applied mainly to raw words, lemmas, and POS tags with correction of the a-priori frequencies. IRST-Kernels BIBREF23 utilizes kernel methods for pattern abstraction, paradigmatic and syntagmatic information and unsupervised term proximity on British National Corpus (BNC), in SVM classifiers. Likewise, nusels BIBREF24 makes use of SVM classifiers with a combination of knowledge sources (part-of-speech of neighboring words, words in context, local collocations, syntactic relations. The second part of the table lists the low-performing supervised algorithms BIBREF3 . Considering their ranking scores we see that there are unsupervised methods that outperform these supervised algorithms.
> 
> Within-our-model comparisons - Besides several internal experiments to examine the importance of some hyper-parameters to our network, we investigated if the sequential follow of cosine similarities computed between a true sense

#### Relevance 366

Label: 

#### Passage 367

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> embeddings; in this work, GloVe vectors are used.
> 
> On the other hand, the output of the network that is examining sense INLINEFORM0 is DISPLAYFORM0
> 
> where INLINEFORM0 and INLINEFORM1 are the weights and the bias of the classification layer (sigmoid), and INLINEFORM2 is the result of the merge layer (concatenation).
> 
> When we train the network, for an instance with the correct sense and the given context as inputs, INLINEFORM0 is set to be 1.0, and for incorrect senses they are set to be 0.0. During testing, however, among all the senses, the output of the network for a sense that gives the highest value of INLINEFORM1 will be considered as the true sense of the ambiguous term, in other words, the correct sense would be: DISPLAYFORM0
> 
> By applying softmax to the result of estimated classification values, INLINEFORM0 , we can show them as probabilities; this facilitates interpretation of the results.
> 
> Further, the hidden layer INLINEFORM0 is computed as DISPLAYFORM0
> 
> where INLINEFORM0 means rectified linear unit; INLINEFORM1 is the concatenated outputs of the right and left traversing LSTMs of the BLSTM when the last context components are met. INLINEFORM2 and INLINEFORM3 are the weights and bias for the hidden layer.

#### Relevance 367

Label: 

#### Passage 369

Retrieved by: BM25, Dense, Hybrid RRF

> In the past few years, there has been an increasing interest in training neural word embeddings from large unlabeled corpora using neural networks BIBREF9 BIBREF10 . Word embeddings are typically represented as a dense real-valued low dimensional matrix INLINEFORM0 (i.e. a lookup table) of size INLINEFORM1 , where INLINEFORM2 is the predefined embedding dimension and INLINEFORM3 is the vocabulary size. Each column of the matrix is an embedding vector associated with a word in the vocabulary and each row of the matrix represents a latent feature. These vectors can subsequently be used to initialize the input layer of a neural network or some other NLP model. GloVe BIBREF2 is one of the existing unsupervised learning algorithms for obtaining these vector representations of the words in which training is performed on aggregated global word-word co-occurrence statistics from a corpus.
> 
> Besides word embeddings, recently, computation of sense embeddings has gained the attention of numerous studies as well. For example, Chen et al. BIBREF11 adapted neural word embeddings to compute different sense embeddings (of the same word) and showed competitive performance on the SemEval-2007 data BIBREF12 .

#### Relevance 369

Label: 

#### Passage 370

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> there are unsupervised methods that outperform these supervised algorithms.
> 
> Within-our-model comparisons - Besides several internal experiments to examine the importance of some hyper-parameters to our network, we investigated if the sequential follow of cosine similarities computed between a true sense and its preceding and succeeding context words carries a pattern-like information that can be encoded with BLSTM. Table TABREF20 presents the results of these experiments.
> 
> The first row shows the best result of the network that we described above (and depicted in Fig. FIGREF4 ). Each of the other rows shows one change that we applied to the network to see the behavior of the network in terms of F-measure. In the middle part, we are specifically concerned about the importance of the presence of a BLSTM layer in our network. So, we introduced some fundamental changes in the input or in the structure of the network. Generally, it is expected that the cosine similarities of closer words (in the context) to the true sense be larger than the incorrect senses' BIBREF17 ; however, if a series of cosine similarities can be encoded through an LSTM (or BLSTM) network should be experimented. We observe if reverse the sequential follow of information into our Bidirectional LSTM, we shuffle the order of the context words, or even replace our Bidirectional LSTMs with two different fully-connected networks of the same size 50 (the size of the LSTMs outputs), the achieved results were notably less than 72.5%.
> 
> In the third section of the table, we report our changes to the hyper-parameters. Specifically, we see the importance of using GloVe as pre-trained word embeddings, how word dropout improves generalization, and how context size plays an important role in the final classification result (showing one of our experiments).

#### Relevance 370

Label: 

#### Passage 371

Retrieved by: Dense, Hybrid RRF

> Given a document and the position of a target word, our model computes a probability distribution over possible senses related to that word. The architecture of our model, depicted in Fig. FIGREF4 , consist of 6 layers which are a sigmoid layer (at the top), a fully-connected layer, a concatenation layer, a BLSTM layer, a cosine layer, and a sense and word embeddings layer (on the bottom).
> 
> In contrast to other supervised neural WSD networks in which generally a softmax layer - with a cross entropy or hinge loss - is parameterized by the context words and selects the corresponding weight matrix and bias vector for each ambiguous word's senses BIBREF15 BIBREF16 , our network shares parameters over all words' senses. While remaining computationally efficient, this structure aims to encode statistical information across different words enabling the network to select the true sense (or even a proper word) in a blank space within a context.
> 
> Due to the replacement of their softmax layers with a sigmoid layer in our network, we need to impose a modification in the input of the model. For this purpose, not only the contextual features are going to make the input of the network, but also, the sense for which we are interested to find out whether that given context makes sense or not (no pun intended) would be provided to the network. Next, the context words would be transferred to a sequence of word embeddings while the sense would be represented as a sense embedding (the shaded embeddings in Fig. FIGREF4 ). For a set of candidate senses (i.e. INLINEFORM0 ) for an ambiguous term, after computing cosine similarities of each sense embedding with the word embeddings of the context words, we expect the sequence result of similarities between the true sense and the surrounding context communicate a pattern-like information that can be encoded through our BLSTM network; for the incorrect senses this premise does not hold. Several WSD studies already incorporated the idea of sense-context cosine similarities in their models BIBREF17 BIBREF18 .

#### Relevance 371

Label: 

#### Passage 373

Retrieved by: Hybrid RRF, Hybrid RRF followed by BGE reranking

> Word Sense Disambiguation (WSD) is an important problem in Natural Language Processing (NLP), both in its own right and as a stepping stone to other advanced tasks in the NLP pipeline, applications such as machine translation BIBREF0 and question answering BIBREF1 . WSD specifically deals with identifying the correct sense of a word, among a set of given candidate senses for that word, when it is presented in a brief narrative (surrounding text) which is generally referred to as context. Consider the ambiguous word `cold'. In the sentence “He started to give me a cold shoulder after that experiment”, the possible senses for cold can be cold temperature (S1), a cold sensation (S2), common cold (S3), or a negative emotional reaction (S4). Therefore, the ambiguous word cold is specified along with the sense set {S1, S2, S3, S4} and our goal is to identify the correct sense S4 (as the closest meaning) for this specific occurrence of cold after considering - the semantic and the syntactic information of - its context.
> 
> In this effort, we develop our supervised WSD model that leverages a Bidirectional Long Short-Term Memory (BLSTM) network. This network works with neural sense vectors (i.e. sense embeddings), which are learned during model training, and employs neural word vectors (i.e. word embeddings), which are learned through an unsupervised deep learning approach called GloVe (Global Vectors for word representation) BIBREF2 for the context words. By evaluating our one-model-fits-all WSD network over the public gold standard dataset of SensEval-3 BIBREF3 , we demonstrate that the accuracy of our model in terms of F-measure is comparable with the state-of-the-art WSD algorithms'.
> 
> We outline the organization of the rest of the paper as follows. In Section 2, we briefly explore earlier efforts in WSD and discuss recent approaches that incorporate deep neural networks and word embeddings. Our main model that employs BLSTM with the sense and word embeddings is detailed in Section 3. We then present our experiments and results in Section 4 supported by a discussion on how to avoid some drawbacks of the current model in order to achieve higher accuracies and demand less number of training data which is desirable. Finally, in Section 5, we

#### Relevance 373

Label: 

### BM25

#### Passage 368

Retrieved by: BM25

> SensEval-3 data BIBREF3 on which the network is evaluated, consist of separate training and test samples. In order to find hyper-parameters of the network 5% of the training samples were used for the validation in advance. Once the hyper-parameters are selected, the whole network is trained on all training samples prior to testing. As to the loss function employed for the network, even though is it common to use (binary) cross entropy loss function when the last unit is a sigmoidal classification, we observed that mean square error led to better results for the final argmax classification (Eq. ( EQREF9 )) that we used. Regarding parameter optimization, RMSprop BIBREF19 is employed. Also, all weights including embeddings are updated during training.

#### Relevance 368

Label: 

### Dense

#### Passage 372

Retrieved by: Dense

> In contrast to common one-classifier-per-each-word supervised WSD algorithms, we developed our single network of BLSTM that is able to effectively exploit word orders and achieve comparable results with the best-performing supervised algorithms. This single WSD BLSTM network is language and domain independent and can be applied to resource-poor languages (or domains) as well. As an ongoing project, we also provided a direction which can lead us to the improvement of the results of the current network using pre-trained sense embeddings.
> 
> For future work, besides following the discussed direction in order to resolve the inadequacy of the network regarding having two non-overlapping vector spaces of the embeddings, we plan to examine the network on technical domains such as biomedicine as well. In this case, our model will be evaluated on MSH WSD dataset prepared by National Library of Medicine (NLM). Also, construction of sense embeddings using (extended) definitions of senses BIBREF25 BIBREF26 can be tested. Moreover, considering that for many senses we have at least one (lexically) unambiguous word representing that sense, we also aim to experiment with unsupervised (pre-)training of our network which benefits form quarry management by which more training data will be automatically collected from the web.

#### Relevance 372

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 374

Retrieved by: Hybrid RRF followed by BGE reranking

> Dropout BIBREF20 is a regularization technique for neural network models where randomly selected neurons are ignored during training. This means that their contribution to the activation of downstream neurons is temporally removed on the forward pass, and any weight updates are not applied to the neuron on the backward pass. The effect is that the network becomes less sensitive to the specific weights of neurons, resulting in better generalization, and a network that is less likely to overfit the training data. In our network, dropout is applied to the embeddings as well as the outputs of the merge and fully-connected layers.
> 
> Following the dropout logic, dropword BIBREF21 is the word level generalizations of it, but in word dropout the word is set to zero while in dropword it is replaced with a specific tag. The tag is subsequently treated just like one word in the vocabulary. The motivation for doing dropword and word dropout is to decrease the dependency on individual words in the training context. Since by replacing word dropout with dropword we observed no change in the results, only word dropout was applied to the sequence of context words during training.

#### Relevance 374

Label: 

## Question 0042

Paper: Text Classification based on Word Subspace with Term-Frequency

> Which dataset has been used in this work?

### Common Retrieved Chunks

#### Passage 375

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this section we describe the experiments performed to demonstrate the validity of our proposed method and its extension. We used the Reuters-8 dataset without stop words from BIBREF27 aiming at single-label classification, which is a preprocessed format of the Reuters-21578. Words in the texts were considered as they appeared, without performing stemming or typo correction. This database has eight different classes with the number of samples varying from 51 to over 3000 documents, as can be seen in Table 1 .
> 
> To obtain the vector representation of words, we used a freely available word2vec model, trained by BIBREF8 , on approximately 100 billion words, which encodes the vector representation in $\mathbb {R}^{300}$ of over 3 million words from several different languages. Since we decided to focus on English words only, we filtered these vectors to about 800 thousand words, excluding all words with non-roman characters.
> 
> To show the validity of our word subspace representation for text classification and the proposed extension, we divided our experiment section into two parts: The first one aims to verify if sets of word vectors are suitable for subspace representation, and the second one puts our methods in practice in a text classification test, comparing our results with the conventional methods described in Section "Related Work" .

#### Relevance 375

Label: 

#### Passage 376

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Text classification has become an indispensable task due to the rapid growth in the number of texts in digital form available online. It aims to classify different texts, also called documents, into a fixed number of predefined categories, helping to organize data, and making easier for users to find the desired information. Over the past three decades, many methods based on machine learning and statistical models have been applied to perform this task, such as latent semantic analysis (LSA), support vector machines (SVM), and multinomial naive Bayes (MNB).
> 
> The first step in utilizing such methods to categorize textual data is to convert the texts into a vector representation. One of the most popular text representation models is the bag-of-words model BIBREF0 , which represents each document in a collection as a vector in a vector space. Each dimension of the vectors represents a term (e.g., a word, a sequence of words), and its value encodes a weight, which can be how many times the term occurs in the document.
> 
> Despite showing positive results in tasks such as language modeling and classification BIBREF1 , BIBREF2 , BIBREF3 , the BOW representation has limitations: first, feature vectors are commonly very high-dimensional, resulting in sparse document representations, which are hard to model due to space and time complexity. Second, BOW does not consider the proximity of words and their position in the text and consequently cannot encode the words semantic meanings.
> 
> To solve these problems, neural networks have been employed to learn vector representations of words BIBREF4 , BIBREF5 , BIBREF6 , BIBREF7 . In particular, the word2vec representation BIBREF8 has gained attention. Given a training corpus, word2vec can generate a vector for each word in the corpus that encodes its semantic information. These word vectors are distributed in such a way that words from similar contexts are represented by word vectors with high correlation, while words from different contexts are represented by word vectors with low correlation.
> 
> One crucial aspect of the word2vec representation is that arithmetic and distance calculation between two word vectors can be performed, giving information about their semantic relationship. However, rather than looking at pairs of word vectors, we are interested in studying

#### Relevance 376

Label: 

#### Passage 377

Retrieved by: BM25, Dense, Hybrid RRF

> In this experiment, we performed text classification among the classes in the Reuters-8 database. We compared the classification using the word subspace, and its weighted extension, based on MSM (to which we will refer as MSM and TF-MSM, respectively) with the baselines presented in Section "Related Work" : MVB, MNB, LSA, and SVM. Since none of the baseline methods work with vector set classification, we also compared to a simple baseline for comparing sets of vectors, defined as the average of similarities between all vector pair combinations of two given sets. For two matrices ${A}$ and ${B}$ , containing the sets of vectors $\lbrace  {x}^{i}_a \rbrace _{i = 1}^{N_A}$ and $\lbrace  {x}^{i}_b \rbrace _{i = 1}^{N_B}$ , respectively, where $N_A$ and $N_B$ are the number of main words in each set, the similarity is defined as:
> 
> $$Sim_{(A,B)} = \frac{1}{N_A N_B}\sum _{i}^{N_A}\sum _{j}^{N_B}{{x}_a^i}^{\top }{x}_b^j.$$   (Eq. 41)
> 
> We refer to this baseline as similarity average (SA). For this method, we only considered one occurrence of each word in each set.
> 
> Different features were used, depending on the method. Classification with SA, MSM, and TF-MSM was performed using word2vec features, to which we refer as w2v. For MVB, due to its nature, only bag-of-words features with binary weights were used (binBOW). For the same reason, we only used bag-of-words features with term-frequency weights (tfBOW) with MNB. Classification with LSA and SVM is usually performed using bag-of-words features and, therefore, we tested with binBOW, tfBOW, and with the term-frequency inverse document-frequency weight, tfidfBOW. We also tested them using word2vec vectors. In this case, we considered each word vector from all documents in each class to be a single sample.
> 
> To determine the dimensions of the class subspaces and query subspace of MSM and TF-MSM, and the dimension of the approximation performed by LSA, we performed a 10-fold cross validation, wherein each fold, the data were randomly divided into train (60%), validation (20%) and test set (20%).
> 
> The results can be seen in Table 2 . The simplest baseline, SA with w2v, achieved an accuracy rate of 78.73%. This result is important because it shows the validity of the word2vec representation, performing better than more elaborate methods based on BOW,

#### Relevance 377

Label: 

#### Passage 379

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> All methods mentioned above utilize the BOW features to represent a document. Although this representation is simple and powerful, its main problem lies on disregarding the word semantics within a document, where the context and meaning could offer many benefits to the model such as identification of synonyms.
> 
> In our formulation, words are represented as vectors in a real-valued feature vector space $\mathbb {R}^{p}$ , by using word2vec BIBREF8 . Through this representation, it is possible to calculate the distance between two words, where words from similar contexts are represented by vectors close to each other, while words from different contexts are represented as far apart vectors. Also, this representation brings the new concept of arithmetic operations between words, where operations such as addition and subtraction carry meaning (eg., “king”-“man”+“woman”=“queen”) BIBREF20 .
> 
> Consider a set of documents which belong to the same context $D_c = \lbrace d_i\rbrace _{i=1}^{|D_c|}$ . Each document $d_i$ is represented by a set of $N_i$ words, $d_i = \lbrace w_k\rbrace _{k=1}^{N_i}$ . By considering that all words from documents of the same context belong to the same distribution, a set of words $W_c = \lbrace w_k\rbrace _{k=1}^{N_c}$ with the words in the context $c$ is obtained.
> 
> We then translate these words into word vectors using word2vec, resulting in a set of word vectors $X_c = \lbrace {x}^k_c\rbrace _{k=1}^{N_c} \in \mathbb {R}^p$ . This set of word vectors is modeled into a word subspace, which is a compact, scalable and meaningful representation of the whole set. Such a word subspace is generated by applying PCA to the set of word vectors.
> 
> First, we compute an autocorrelation matrix, ${R}_c$ :
> 
> $${R}_c = \frac{1}{N_c}\sum _{i=1}^{N_c}{x}^{i}_c{x}_c^{i^{\top }}.$$   (Eq. 29)
> 
> The orthonormal basis vectors of $m_c$ -dimensional subspace ${Y}_c$ are obtained as the eigenvectors with the $m_c$ largest eigenvalues of the matrix ${R}_c$ . We represent a subspace ${Y}_c$ by the matrix ${Y}_c \in \mathbb {R}^{p \times m_c}$ , which has the corresponding orthonormal basis vectors as its column vectors.

#### Relevance 379

Label: 

#### Passage 382

Retrieved by: Hybrid RRF, Hybrid RRF followed by BGE reranking

> (Eq. 25)
> 
> Despite its extensive application on text classification BIBREF13 , BIBREF14 , BIBREF15 , this method was initially proposed for document indexing and, therefore, does not encode any class information when modeling the low-rank approximation. To perform classification, 1-nearest neighbor is usually performed, placing a query document into the class of the nearest training document.
> 
> The support vector machine (SVM) was first presented in BIBREF16 and performs the separation between samples of two different classes by projecting them onto a higher dimensionality space. It was first applied in text classification by BIBREF17 and have since been successfully applied in many tasks related to natural language processing BIBREF18 , BIBREF19 .
> 
> Consider a training data set $D$ , with $n$ samples
> 
> $$D = \lbrace ({x}_i,c_i)|{x}_i\in \mathbb {R}^p, c_i \in \lbrace -1,1\rbrace  \rbrace _{i=1}^{n},$$   (Eq. 27)
> 
> where $c_i$ represents the class to which ${x}_i$ belongs to. Each ${x}_i$ is a $p$ -dimensional vector. The goal is to find the hyperplane that divides the points from $c_i = 1$ from the points from $c_i = -1$ . This hyperplane can be written as a set of points $x$ satisfying:
> 
> $${w} \cdot {x} - b = 0,$$   (Eq. 28)
> 
> where $\cdot $ denotes the dot product. The vector ${w}$ is perpendicular to the hyperplane. The parameter $\frac{b}{\Vert {w}\Vert }$ determines the offset of the hyperplane from the origin along the normal vector ${w}$ .
> 
> We wish to choose ${w}$ and $b$ , so they maximize the distance between the parallel hyperplanes that are as far apart as possible, while still separating the data.
> 
> If the training data is linearly separable, we can select two hyperplanes in a way that there are no points between them and then try to maximize the distance. In other words, minimize $\Vert {w}\Vert $ subject to $c_i({w}\cdot {x}_u-b) \ge 1, i=\lbrace 1,2,...,n\rbrace $ . If the training data is not linearly separable, the kernel trick can be applied, where every dot product is replaced by a non-linear kernel function.

#### Relevance 382

Label: 

### BM25

#### Passage 378

Retrieved by: BM25

> In this paper, we proposed a new method for text classification, based on the novel concept of word subspace under the MSM framework. We also proposed the term-frequency weighted word subspace which can incorporate the frequency of words directly in the modeling of the subspace by using a weighted version of PCA.
> 
> Most of the conventional text classification methods are based on the bag-of-words features, which are very simple to compute and had been proved to produce positive results. However, bag-of-words are commonly high dimensional models, with a sparse representation, which is computationally heavy to model. Also, bag-of-words fail to convey the semantic meaning of words inside a text. Due to these problems, neural networks started to be applied to generate a vector representation of words. Despite the fact that these representations can encode the semantic meaning of words, conventional methods do not work well when considering word vectors separately.
> 
> In our work, we focused on the word2vec representation, which can embed the semantic structure of words, rendering vector angles as a useful metric to show meaningful similarities between words. Our experiments showed that our word subspace modeling along with the MSM outperforms most of the conventional methods. Ultimately, our TF weighted subspace formulation resulted in significantly higher accuracy when compared to all conventional text classification methods discussed in this work. It is important to note that our method does not consider the order of the words in a text, resulting in a loss of context information. As a future work, we wish to extend our word subspace concept further in mainly two directions. First, we seek to encode word order, which may enrich the representation of context information. Second, we wish to model dynamic context change, enabling analysis of large documents, by having a long-short memory to interpret information using cues from different parts of a text.

#### Relevance 378

Label: 

### Dense

#### Passage 380

Retrieved by: Dense

> In this section, we outline relevant work towards text classification. We start by describing how text data is conventionally represented using the bag-of-words model and then follow to describe the conventional methods utilized in text classification.

#### Relevance 380

Label: 

#### Passage 381

Retrieved by: Dense

> Given the observation of the eigenvalues distribution of word vectors, we could see that word vectors that belong to the same context, i.e., same class, are suitable for subspace representation. Our analysis showed that half of the word vector space dimensions suffice to represent most of the variability of the data in each class of the Reuters-8 database.
> 
> The results from the text classification experiment showed that subspace-based methods performed better than the text classification methods discussed in this work. Ultimately, our proposed TF weighted word subspace with MSM surpassed all the other methods. word2vec features are reliable tools to represent the semantic meaning of the words and when treated as sets of word vectors, they are capable of representing the content of texts. However, despite the fact that word vectors can be treated separately, conventional methods such as SVM and LSA may not be suitable for text classification using word vectors.
> 
> Among the conventional methods, LSA and SVM achieved about 86% and 89%, respectively, when using bag-of-words features. Interestingly, both methods had better performance when using binary weights. For LSA, we can see that despite the slight differences in the performance, tfidfBOW required approximations with smaller dimensions. SVM had the lowest accuracy rate when using the tfidfBOW features. One possible explanation for this is that TF-IDF weights are useful when rare words and very frequent words exist in the corpus, giving higher weights for rare words and lower weights for common words. Since we removed the stop words, the most frequent words among the training documents were not considered and, therefore, using TF-IDF weights did not improve the results.
> 
> Only MNB with tfBOW performed better than MSM. This result may be because tfBOW features encode the word frequencies, while MSM only considers a single occurrence of words. When incorporating the word frequencies with our TF weighted word subspace, we achieved a higher accuracy of 92.01%, performing better than MNB at a significance level of 95%.

#### Relevance 381

Label: 

### Hybrid RRF

#### Passage 383

Retrieved by: Hybrid RRF

> be seen in Table 2 . The simplest baseline, SA with w2v, achieved an accuracy rate of 78.73%. This result is important because it shows the validity of the word2vec representation, performing better than more elaborate methods based on BOW, such as MVB with binBOW.
> 
> LSA with BOW features was almost 10% more accurate than SA, where the best results with binary weights were achieved with an approximation with 130 dimensions, with TF weights were achieved with 50 dimensions, and with TF-IDF weights were achieved with 30 dimensions. SVM with BOW features was about 3% more accurate than LSA, with binary weights leading to a higher accuracy rate.
> 
> It is interesting to note that despite the reasonably high accuracy rates achieved using LSA and SVM with BOW features, they poorly performed when using w2v features.
> 
> Among the baselines, the best method was MNB with tfBOW features, with an accuracy of 91.47%, being the only conventional method to outperform MSM. MSM with w2v had an accuracy rate of 90.62%, with the best results achieved with word subspace dimensions for the training classes ranging from 150 to 181, and for the query ranging from 3 to 217. Incorporating the frequency information in the subspace modeling resulted in higher accuracy, with TF-MSM achieving 92.01%, with dimensions of word subspaces for training classes ranging from 150 to 172, and for the query, ranging from 2 to 109. To confirm that TF-MSM is significantly more accurate than MNB, we performed a t-test to compare their results. It resulted in a p-value of 0.031, which shows that at a 95% significance level, TF-MSM has produced better results.

#### Relevance 383

Label: 

### Hybrid RRF followed by BGE reranking

#### Passage 384

Retrieved by: Hybrid RRF followed by BGE reranking

> document $d_i$ and it represents how many times word $w_k$ occurs in $d_i$ .
> 
> Finally, the posterior $P(w_k|c_j)$ can be obtained by the following equation:
> 
> $$P(w_k|c_j) = \frac{1+|D_j^k|}{|C|+|D|},$$   (Eq. 21)
> 
> where $|D_j^k|$ is the number of documents in class $c_j$ that contain the word $w_k$ .
> 
> In general, MVB tends to perform better than MNB at small vocabulary sizes whereas MNB is more efficient on large vocabularies.
> 
> Despite being robust tools for text classification, both these models depend directly on the bag-of-words features and do not naturally work with representations such as word2vec.
> 
> Latent semantic analysis (LSA), or latent semantic indexing (LSI), was proposed in BIBREF12 , and it extends the vector space model by using singular value decomposition (SVD) to find a set of underlying latent variables which spans the meaning of texts.
> 
> It is built from a term-document matrix, in which each row represents a term, and each column represents a document. This matrix can be built by concatenating the vectors of all documents in a corpus, obtained using the bag-of-words model, that is, $ {X} = [ {v}_1, {v}_2, ..., {v}_{|D|}]$ , where ${v}_i$ is the vector representation obtained using the bag-of-words model.
> 
> In this method, the term-document matrix is decomposed using the singular value decomposition,
> 
> $${X} = {U\Sigma V}^\top ,$$   (Eq. 23)
> 
> where $U$ and $V$ are orthogonal matrices and correspond to the left singular vectors and right singular vectors of $X$ , respectively. $\Sigma $ is a diagonal matrix, and it contains the square roots of the eigenvalues of $X^TX$ and $XX^T$ . LSA finds a low-rank approximation of $X$ by selecting only the $k$ largest singular values and its respective singular vectors,
> 
> $${X}_k = {U}_k{\Sigma }_k {V}_k^{\top }.$$   (Eq. 24)
> 
> To compare two documents, we project both of them into this lower dimension space and calculate the cosine distance between them. The projection ${\hat{d}}$ of document ${d}$ is obtained by the following equation:
> 
> $${\hat{d}} = {\Sigma }_k^{-1} {U}_k^\top {d}.$$   (Eq. 25)
> 
> Despite its extensive application on text classification BIBREF13 , BIBREF14 , BIBREF15 , this method was initially proposed for document indexing and, therefore, does not encode any class information when modeling the low-rank approximation. To perform classification, 1-nearest

#### Relevance 384

Label: 

## Question 0043

Paper: Structured Embedding Models for Grouped Data

> Which words are used differently across ArXiv?

### Common Retrieved Chunks

#### Passage 385

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> market basket data from a large grocery store, grouped by season. On all three data sets, sefe outperforms efe in terms of held-out log-likelihood. Qualitatively, we demonstrate how sefe discovers which words are used most differently across U.S. states and political parties, and show how word usage changes in different ArXiv disciplines.

#### Relevance 385

Label: 

#### Passage 386

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this section, we develop sefe, a model that builds on efe BIBREF10 to capture semantic variations across groups of data. In embedding models, we represent each object (e.g., a word in text, or an item in shopping data) using two sets of vectors, an embedding vector and a context vector. In this paper, we are interested in how the embeddings vary across groups of data, and for each object we want to learn a separate embedding vector for each group. Having a separate embedding for each group allows us to study how the usage of a word like 1.10intelligence varies across categories of the ArXiv, or which words are used most differently by U.S. Senators depending on which state they are from and whether they are Democrats or Republicans.
> 
> The sefe model extends efe to grouped data, by having the embedding vectors be specific for each group, while sharing the context vectors across all groups. We review the efe model in Section SECREF4 . We then formalize the idea of sharing the context vectors in Section SECREF8 , where we present two approaches to build a hierarchical structure over the group-specific embeddings.

#### Relevance 386

Label: 

#### Passage 387

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> vectors for each term in the vocabulary; an embedding vector and a context vector. (We use the language of text for concreteness; as we mentioned, efe extend to other types of data.) The idea is that the conditional probability of each observed word depends on the interaction between the embedding vector and the context vectors of the surrounding words. In sefe, we posit a separate set of embedding vectors for each group but a shared set of context vectors; this ensures that the embedding vectors are in the same space.
> 
> We propose two methods to share statistical strength among the embedding vectors. The first approach is based on hierarchical modeling BIBREF13 , which assumes that the group-specific embedding representations are tied through a global embedding. The second approach is based on amortization BIBREF14 , BIBREF15 , which considers that the individual embeddings are the output of a deterministic function of a global embedding representation. We use stochastic optimization to fit large data sets.
> 
> Our work relates closely to two threads of research in the embedding literature. One is embedding methods that study how language evolves over time BIBREF16 , BIBREF17 , BIBREF18 , BIBREF19 , BIBREF20 , BIBREF21 . Time can be thought of as a type of “group”, though with evolutionary structure that we do not consider. The second thread is multilingual embeddings BIBREF22 , BIBREF23 , BIBREF24 , BIBREF25 ; our approach is different in that most words appear in all groups and we are interested in the variations of the embeddings across those groups.
> 
> Our contributions are thus as follows. We introduce the sefe model, extending efe to grouped data. We present two techniques to share statistical strength among the embedding vectors, one based on hierarchical modeling and one based on amortization. We carry out a thorough experimental study on two text databases, ArXiv papers by section and U.S. Congressional speeches by home state and political party. Using Poisson embeddings, we study market basket data from a large grocery store, grouped by season. On all three data sets, sefe outperforms efe in terms of held-out log-likelihood. Qualitatively, we demonstrate how sefe discovers which words are used most differently across U.S. states and

#### Relevance 387

Label: 

#### Passage 388

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Word embeddings BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 , BIBREF6 are unsupervised learning methods for capturing latent semantic structure in language. Word embedding methods analyze text data to learn distributed representations of the vocabulary that capture its co-occurrence statistics. These representations are useful for reasoning about word usage and meaning BIBREF7 , BIBREF8 . Word embeddings have also been extended to data beyond text BIBREF9 , BIBREF10 , such as items in a grocery store or neurons in the brain. efe is a probabilistic perspective on embeddings that encompasses many existing methods and opens the door to bringing expressive probabilistic modeling BIBREF11 , BIBREF12 to the problem of learning distributed representations.
> 
> We develop sefe, an extension of efe for studying how embeddings can vary across groups of related data. We will study several examples: in U.S. Congressional speeches, word usage can vary across states or party affiliations; in scientific literature, the usage patterns of technical terms can vary across fields; in supermarket shopping data, co-purchase patterns of items can vary across seasons of the year. We will see that sefe discovers a per-group embedding representation of objects. While the naïve approach of fitting an individual embedding model for each group would typically suffer from lack of data—especially in groups for which fewer observations are available—we develop two methods that can share information across groups.
> 
> Figure FIGREF1 illustrates the kind of variation that we can capture. We fit an sefe to ArXiv abstracts grouped into different sections, such as computer science (cs), quantitative finance (q-fin), and nonlinear sciences (nlin). sefe results in a per-section embedding of each term in the vocabulary. Using the fitted embeddings, we illustrate similar words to the word 1.10intelligence. We can see that how 1.10intelligence is used varies by field: in computer science the most similar words include 1.10artificial and 1.10ai; in finance, similar words include 1.10abilities and 1.10consciousness.
> 
> In more detail, embedding methods posit two representation vectors for each term in the vocabulary; an embedding vector and a context vector. (We use the language of text for concreteness; as we mentioned, efe extend to other types of data.) The idea is that the conditional probability of

#### Relevance 388

Label: 

#### Passage 390

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this section, we describe the experimental study. We fit the sefe model on three datasets and compare it against the efe BIBREF10 . Our quantitative results show that sharing the context vectors provides better results, and that amortization and hierarchical structure give further improvements.
> 
> Data. We apply the sefe on three datasets: ArXiv papers, U.S. Senate speeches, and purchases on supermarket grocery shopping data. We describe these datasets below, and we provide a summary of the datasets in Table TABREF17 .
> 
> ArXiv papers: This dataset contains the abstracts of papers published on the ArXiv under the 19 different tags between April 2007 and June 2015. We treat each tag as a group and fit sefe with the goal of uncovering which words have the strongest shift in usage. We split the abstracts into training, validation, and test sets, with proportions of INLINEFORM0 , INLINEFORM1 , and INLINEFORM2 , respectively.
> 
> Senate speeches: This dataset contains U.S. Senate speeches from 1994 to mid 2009. In contrast to the ArXiv collection, it is a transcript of spoken language. We group the data into state of origin of the speaker and his or her party affiliation. Only affiliations with the Republican and Democratic Party are considered. As a result, there are 83 groups (Republicans from Alabama, Democrats from Alabama, Republicans from Arkansas, etc.). Some of the state/party combinations are not available in the data, as some of the 50 states have only had Senators with the same party affiliation. We split the speeches into training ( INLINEFORM0 ), validation ( INLINEFORM1 ), and testing ( INLINEFORM2 ).
> 
> Grocery shopping data: This dataset contains the purchases of INLINEFORM0 customers. The data covers a period of 97 weeks. After removing low-frequency items, the data contains INLINEFORM1 unique items at the 1.10upc (Universal Product Code) level. We split the data into a training, test, and validation sets, with proportions of INLINEFORM2 , INLINEFORM3 , and INLINEFORM4 , respectively. The training data contains INLINEFORM5 shopping trips and INLINEFORM6 purchases in total.
> 
> For the text corpora, we fix the vocabulary to the 15k most frequent terms and remove all words that are not in the vocabulary. Following BIBREF2 , we additionally remove each

#### Relevance 390

Label: 

### BM25

#### Passage 389

Retrieved by: BM25

> Here, we describe the sefe model for grouped data. In text, some examples of grouped data are Congressional speeches grouped into political parties or scientific documents grouped by discipline. Our goal is to learn group-specific embeddings from data partitioned into INLINEFORM0 groups, i.e., each instance INLINEFORM1 is associated with a group INLINEFORM2 . The sefe model extends efe to learn a separate set of embedding vectors for each group.
> 
> To build the sefe model, we impose a particular parameter sharing structure over the set of embedding and context vectors. We posit a structured model in which the context vectors are shared across groups, i.e., INLINEFORM0 (as in the standard efe model), but the embedding vectors are only shared at the group level, i.e., for an observation INLINEFORM1 belonging to group INLINEFORM2 , INLINEFORM3 . Here, INLINEFORM4 denotes the embedding vector corresponding to group INLINEFORM5 . We show a graphical representation of the sefe in Figure FIGREF1 .
> 
> Sharing the context vectors INLINEFORM0 has two advantages. First, the shared structure reduces the number of parameters, while the resulting sefe model is still flexible to capture how differently words are used across different groups, as INLINEFORM1 is allowed to vary. Second, it has the important effect of uniting all embedding parameters in the same space, as the group-specific vectors INLINEFORM4 need to agree with the components of INLINEFORM5 . While one could learn a separate embedding model for each group, as has been done for text grouped into time slices BIBREF16 , BIBREF17 , BIBREF18 , this approach would require ad-hoc postprocessing steps to align the embeddings.
> 
> When there are INLINEFORM0 groups, the sefe model has INLINEFORM1 times as many embedding vectors than the standard embedding model. This may complicate inferences about the group-specific vectors, especially for groups with less data. Additionally, an object INLINEFORM2 may appear with very low frequency in a particular group. Thus, the naïve approach for building the sefe model without additional structure may be detrimental for the quality of the embeddings, especially for small-sized groups. To address this problem, we propose two different methods to tie the individual INLINEFORM3 together, sharing statistical strength among them. The first approach consists in a hierarchical

#### Relevance 389

Label: 

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0044

Paper: Multimodal Named Entity Recognition for Short Social Media Posts

> Do they inspect their model to see if their model learned to associate image parts with words related to entities?

### Common Retrieved Chunks

#### Passage 391

Retrieved by: BM25, Dense, Hybrid RRF

> Table TABREF6 shows the NER performance on the Snap Captions dataset. We report both entity types recognition (PER, LOC, ORG, MISC) and named entity segmentation (named entity or not) results.
> 
> Parameters: We tune the parameters of each model with the following search space (bold indicate the choice for our final model): character embeddings dimension: {25, 50, 100, 150, 200, 300}, word embeddings size: {25, 50, 100, 150, 200, 300}, LSTM hidden states: {25, 50, 100, 150, 200, 300}, and INLINEFORM0 dimension: {25, 50, 100, 150, 200, 300}. We optimize the parameters with Adagrad BIBREF28 with batch size 10, learning rate 0.02, epsilon INLINEFORM1 , and decay 0.0.
> 
> Main Results: When visual context is available (W+C+V), we see that the model performance greatly improves over the textual models (W+C), showing that visual contexts are complimentary to textual information in named entity recognition tasks. In addition, it can be seen that the modality attention module further improves the entity type recognition performance for (W+C+V). This result indicates that the modality attention is able to focus on the most effective modality (visual, words, or characters) adaptive to each sample to maximize information gain. Note that our text-only model (W+C) with the modality attention module also significantly outperform the state-of-the-art baselines BIBREF8 , BIBREF1 , BIBREF0 that use the same textual modalities (W+C), showing the effectiveness of the modality attention module for textual models as well.
> 
> Error Analysis: Table TABREF17 shows example cases where incorporation of visual contexts affects prediction of named entities. For example, the token `curry' in the caption “The curry's " is polysemous and may refer to either a type of food or a famous basketball player `Stephen Curry', and the surrounding textual contexts do not provide enough information to disambiguate it. On the other hand, visual contexts (visual tags: `parade', `urban area', ...) provide similarities to the token's distributional semantics from other training examples (snaps from “NBA Championship Parade Story"), and thus the model successfully predicts the token as a named entity. Similarly, while the text-only model erroneously predicts `Apple' in the caption “Grandma w dat lit Apple Crisp" as an organization (Apple Inc.), the visual contexts (describing objects related to food) help disambiguate the

#### Relevance 391

Label: 

#### Passage 392

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Figure FIGREF2 illustrates the proposed multimodal NER (MNER) model. First, we obtain word embeddings, character embeddings, and visual features (Section SECREF3 ). A Bi-LSTM-CRF model then takes as input a sequence of tokens, each of which comprises a word token, a character sequence, and an image, in their respective representation (Section SECREF4 ). At each decoding step, representations from each modality are combined via the modality attention module to produce an entity label for each token ( SECREF5 ). We formulate each component of the model in the following subsections.
> 
> Notations: Let INLINEFORM0 a sequence of input tokens with length INLINEFORM1 , with a corresponding label sequence INLINEFORM2 indicating named entities (e.g. in standard BIO formats). Each input token is composed of three modalities: INLINEFORM3 for word embeddings, character embeddings, and visual embeddings representations, respectively.

#### Relevance 392

Label: 

#### Passage 393

Retrieved by: BM25, Dense, Hybrid RRF

> predicts the token as a named entity. Similarly, while the text-only model erroneously predicts `Apple' in the caption “Grandma w dat lit Apple Crisp" as an organization (Apple Inc.), the visual contexts (describing objects related to food) help disambiguate the token, making the model predict it correctly as a non-named entity (a fruit). Trending entities (musicians or DJs such as `CID', `Duke Dumont', `Marshmello', etc.) are also recognized correctly with strengthened contexts from visual information (describing concert scenes) despite lack of surrounding textual contexts. A few cases where visual contexts harmed the performance mostly include visual tags that are unrelated to a token or its surrounding textual contexts.
> 
> Visualization of Modality Attention: Figure FIGREF19 visualizes the modality attention module at each decoding step (each column), where amplified modality is represented with darker color, and attenuated modality is represented with lighter color.
> 
> For the image-aided model (W+C+V; upper row in Figure FIGREF19 ), we confirm that the modality attention successfully attenuates irrelevant signals (selfies, etc.) and amplifies relevant modality-based contexts in prediction of a given token. In the example of “disney word essential = coffee" with visual tags selfie, phone, person, the modality attention successfully attenuates distracting visual signals and focuses on textual modalities, consequently making correct predictions. The named entities in the examples of “Beautiful night atop The Space Needle" and “Splash Mountain" are challenging to predict because they are composed of common nouns (space, needle, splash, mountain), and thus they often need additional contexts to correctly predict. In the training data, visual contexts make stronger indicators for these named entities (space needle, splash mountain), and the modality attention module successfully attends more to stronger signals.
> 
> For text-only model (W+C), we observe that performance gains mostly come from the modality attention module better handling tokens unseen during training or unknown tokens from the pre-trained word embeddings matrix. For example, while WaRriOoOrs and Kooler Matic are missing tokens in the word embeddings matrix, it successfully amplifies character-based contexts (capitalized first letters, similarity to known entities `Golden State Warriors') and suppresses word-based contexts (word embeddings for unknown tokens `WaRriOoOrs'), leading to correct predictions. This result is significant because it shows performance of the model, with an almost

#### Relevance 393

Label: 

#### Passage 396

Retrieved by: Dense, Hybrid RRF

> correctly recognizing it as a named entity.
> 
> Second, we also propose a general modality attention module which chooses per decoding step the most informative modality among available ones (in our case, word embeddings, character embeddings, or visual features) to extract context from. For example, the modality attention module lets the decoder attenuate the word-level signals for unknown word tokens (“Marshmellooooo" with trailing `o's) and amplifies character-level features intsead (capitalized first letter, lexical similarity to other known named entity token `Marshmello', etc.), thereby suppressing noise information (“UNK" token embedding) in decoding steps. Note that most of the previous literature in NER or other NLP tasks combine word and character-level information with naive concatenation, which is vulnerable to noisy social media posts. When an auxiliary image is available, the modality attention module determines to amplify this visual context in disambiguating polysemous entities, or to attenuate visual contexts when they are irrelevant to target named entities, selfies, etc. Note that the proposed modality attention module is distinct from how attention is used in other sequence-to-sequence literature (e.g. attending to a specific token within an input sequence). Section SECREF2 provides the detailed literature review.
> 
> Our contributions are three-fold: we propose (1) an LSTM-CNN hybrid multimodal NER network that takes as input both image and text for recognition of a named entity in text input. To the best of our knowledge, our approach is the first work to incorporate visual contexts for named entity recognition tasks. (2) We propose a general modality attention module that selectively chooses modalities to extract primary context from, maximizing information gain and suppressing irrelevant contexts from each modality (we treat words, characters, and images as separate modalities). (3) We show that the proposed approaches outperform the state-of-the-art NER models (both with and without using additional visual contexts) on our new MNER dataset SnapCaptions, a large collection of informal and extremely short social media posts paired with unique images.

#### Relevance 396

Label: 

#### Passage 397

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> Social media with abundant user-generated posts provide a rich platform for understanding events, opinions and preferences of groups and individuals. These insights are primarily hidden in unstructured forms of social media posts, such as in free-form text or images without tags. Named entity recognition (NER), the task of recognizing named entities from free-form text, is thus a critical step for building structural information, allowing for its use in personalized assistance, recommendations, advertisement, etc.
> 
> While many previous approaches BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 on NER have shown success for well-formed text in recognizing named entities via word context resolution (e.g. LSTM with word embeddings) combined with character-level features (e.g. CharLSTM/CNN), several additional challenges remain for recognizing named entities from extremely short and coarse text found in social media posts. For instance, short social media posts often do not provide enough textual contexts to resolve polysemous entities (e.g. “monopoly is da best ", where `monopoly' may refer to a board game (named entity) or a term in economics). In addition, noisy text includes a huge number of unknown tokens due to inconsistent lexical notations and frequent mentions of various newly trending entities (e.g. “xoxo Marshmelloooo ", where `Marshmelloooo' is a mis-spelling of a known entity `Marshmello', a music producer), making word embeddings based neural networks NER models vulnerable.
> 
> To address the challenges above for social media posts, we build upon the state-of-the-art neural architecture for NER with the following two novel approaches (Figure FIGREF1 ). First, we propose to leverage auxiliary modalities for additional context resolution of entities. For example, many popular social media platforms now provide ways to compose a post in multiple modalities - specifically image and text (e.g. Snapchat captions, Twitter posts with image URLs), from which we can obtain additional context for understanding posts. While “monopoly" in the previous example is ambiguous in its textual form, an accompanying snap image of a board game can help disambiguate among polysemous entities, thereby correctly recognizing it as a named entity.
> 
> Second, we also propose a general modality attention module which chooses per decoding step the most informative modality among available ones (in our case, word embeddings, character embeddings, or visual features) to extract

#### Relevance 397

Label: 

#### Passage 398

Retrieved by: Dense, Hybrid RRF

> character-based contexts (capitalized first letters, similarity to known entities `Golden State Warriors') and suppresses word-based contexts (word embeddings for unknown tokens `WaRriOoOrs'), leading to correct predictions. This result is significant because it shows performance of the model, with an almost identical architecture, can still improve without having to scale the word embeddings matrix indefinitely.
> 
> Figure FIGREF19 (b) shows the cases where the modality attention led to incorrect predictions. For example, the model predicts missing tokens HUUUGE and Shampooer incorrectly as named entities by amplifying misleading character-based contexts (capitalized first letters) or visual contexts (concert scenes, associated contexts of which often include named entities in the training dataset).
> 
> Sensitivity to Word Embeddings Vocabulary Size: In order to isolate the effectiveness of the modality attention module on textual models in handling missing tokens, we report the performance with varying word embeddings vocabulary sizes in Table TABREF20 . By increasing the number of missing tokens artificially by randomly removing words from the word embeddings matrix (original vocab size: 400K), we observe that while the overall performance degrades, the modality attention module is able to suppress the peformance degradation. Note also that the performance gap generally gets bigger as we decrease the vocabulary size of the word embeddings matrix. This result is significant in that the modality attention is able to improve the model more robust to missing tokens without having to train an indefinitely large word embeddings matrix for arbitrarily noisy social media text datasets.

#### Relevance 398

Label: 

### BM25

#### Passage 394

Retrieved by: BM25

> Neural models for NER have been recently proposed, producing state-of-the-art performance on standard NER tasks. For example, some of the end-to-end NER systems BIBREF4 , BIBREF2 , BIBREF3 , BIBREF0 , BIBREF1 use a recurrent neural network usually with a CRF BIBREF5 , BIBREF6 for sequence labeling, accompanied with feature extractors for words and characters (CNN, LSTMs, etc.), and achieve the state-of-the-art performance mostly without any use of gazetteers information. Note that most of these work aggregate textual contexts via concatenation of word embeddings and character embeddings. Recently, several work have addressed the NER task specifically on noisy short text segments such as Tweets, etc. BIBREF7 , BIBREF8 . They report performance gains from leveraging external sources of information such as lexical information (POS tags, etc.) and/or from several preprocessing steps (token substitution, etc.). Our model builds upon these state-of-the-art neural models for NER tasks, and improves the model in two critical ways: (1) incorporation of visual contexts to provide auxiliary information for short media posts, and (2) addition of the modality attention module, which better incorporates word embeddings and character embeddings, especially when there are many missing tokens in the given word embedding matrix. Note that we do not explore the use of gazetteers information or other auxiliary information (POS tags, etc.) BIBREF9 as it is not the focus of our study.
> 
> Attention modules are widely applied in several deep learning tasks BIBREF10 , BIBREF11 , BIBREF12 , BIBREF13 . For example, they use an attention module to attend to a subset within a single input (a part/region of an image, a specific token in an input sequence of tokens, etc.) at each decoding step in an encoder-decoder framework for image captioning tasks, etc. BIBREF14 explore various attention mechanisms in NLP tasks, but do not incorporate visual components or investigate the impact of such models on noisy social media data. BIBREF15 propose to use attention for a subset of discrete source samples in transfer learning settings. Our modality attention differs from the previous approaches in that we attenuate or amplifies each modality input as a whole among multiple available modalities, and that we use the attention mechanism essentially to map heterogeneous modalities in a

#### Relevance 394

Label: 

#### Passage 395

Retrieved by: BM25

> The modality attention module learns a unified representation space for multiple available modalities (words, characters, images, etc.), and produces a single vector representation with aggregated knowledge among multiple modalities, based on their weighted importance. We motivate this module from the following observations.
> 
> A majority of the previous literature combine the word and character-level contexts by simply concatenating the word and character embeddings at each decoding step, e.g. INLINEFORM0 in Eq. SECREF4 . However, this naive concatenation of two modalities (word and characters) results in inaccurate decoding, specifically for unknown word token embeddings (an all-zero vector INLINEFORM1 or a random vector INLINEFORM2 is assigned for any unknown token INLINEFORM3 , thus INLINEFORM4 or INLINEFORM5 ). While this concatenation approach does not cause significant errors for well-formatted text, we observe that it induces performance degradation for our social media post datasets which contain a significant number of missing tokens.
> 
> Similarly, naive merging of textual and visual information ( INLINEFORM0 ) yields suboptimal results as each modality is treated equally informative, whereas in our datasets some of the images may contain irrelevant contexts to textual modalities. Hence, ideally there needs a mechanism in which the model can effectively turn the switch on and off the modalities adaptive to each sample.
> 
> To this end, we propose a general modality attention module, which adaptively attenuates or emphasizes each modality as a whole at each decoding step INLINEFORM0 , and produces a soft-attended context vector INLINEFORM1 as an input token for the entity LSTM. [at(w),at(c),at(v)] = (Wm[xt(w); xt(c); xt(v)] + bm )
> 
> t(m) = (at(m))m'{w,c,v}(at(m')) m {w,c,v}
> 
> xt = m{w,c,v} t(m)xt(m)
> 
> where INLINEFORM0 is an attention vector at each decoding step INLINEFORM1 , and INLINEFORM2 is a final context vector at INLINEFORM3 that maximizes information gain for INLINEFORM4 . Note that the optimization of the objective function (Eq. SECREF4 ) with modality attention (Eq. SECREF5 ) requires each modality to have the same dimension ( INLINEFORM5 ), and that the transformation via INLINEFORM6 essentially enforces each modality to be mapped into the same unified subspace, where the weighted average of which encodes discrimitive features for recognition of named entities.
> 
> When visual context is not provided with each token (as in the

#### Relevance 395

Label: 

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 399

Retrieved by: Hybrid RRF followed by BGE reranking

> Similar to the state-of-the-art NER approaches BIBREF0 , BIBREF1 , BIBREF8 , BIBREF4 , BIBREF2 , BIBREF3 , we use both word embeddings and character embeddings.
> 
> Word embeddings are obtained from an unsupervised learning model that learns co-occurrence statistics of words from a large external corpus, yielding word embeddings as distributional semantics BIBREF21 . Specifically, we use pre-trained embeddings from GloVE BIBREF22 .
> 
> Character embeddings are obtained from a Bi-LSTM which takes as input a sequence of characters of each token, similarly to BIBREF0 . An alternative approach for obtaining character embeddings is using a convolutional neural network as in BIBREF1 , but we find that Bi-LSTM representation of characters yields empirically better results in our experiments.
> 
> Visual embeddings: To extract features from an image, we take the final hidden layer representation of a modified version of the convolutional network model called Inception (GoogLeNet) BIBREF23 , BIBREF24 trained on the ImageNet dataset BIBREF25 to classify multiple objects in the scene. Our implementation of the Inception model has deep 22 layers, training of which is made possible via “network in network" principles and several dimension reduction techniques to improve computing resource utilization. The final layer representation encodes discriminative information describing what objects are shown in an image, which provide auxiliary contexts for understanding textual tokens and entities in accompanying captions.
> 
> Incorporating this visual information onto the traditional NER system is an open challenge, and multiple approaches can be considered. For instance, one may provide visual contexts only as an initial input to decoder as in some encoder-decoder image captioning systems BIBREF26 . However, we empirically observe that an NER decoder which takes as input the visual embeddings at every decoding step (Section SECREF4 ), combined with the modality attention module (Section SECREF5 ), yields better results.
> 
> Lastly, we add a transform layer for each feature INLINEFORM0 before it is fed to the NER entity LSTM.

#### Relevance 399

Label: 

#### Passage 400

Retrieved by: Hybrid RRF followed by BGE reranking

> Task: given a caption and a paired image (if used), the goal is to label every token in a caption in BIO scheme (B: beginning, I: inside, O: outside) BIBREF27 . We report the performance of the following state-of-the-art NER models as baselines, as well as several configurations of our proposed approach to examine contributions of each component (W: word, C: char, V: visual).
> 
> Bi-LSTM/CRF (W only): only takes word token embeddings (Stanford GloVE) as input. The rest of the architecture is kept the same.
> 
> Bi-LSTM/CRF + Bi-CharLSTM (C only): only takes a character sequence of each word token as input. (No word embeddings)
> 
> Bi-LSTM/CRF + Bi-CharLSTM (W+C) BIBREF0 : takes as input both word embeddings and character embeddings extracted from a Bi-CharLSTM. Entity LSTM takes concatenated vectors of word and character embeddings as input tokens.
> 
> Bi-LSTM/CRF + CharCNN (W+C) BIBREF1 : uses character embeddings extracted from a CNN instead.
> 
> Bi-LSTM/CRF + CharCNN (W+C) + Multi-task BIBREF8 : trains the model to perform both recognition (into multiple entity types) as well as segmentation (binary) tasks.
> 
> (proposed) Bi-LSTM/CRF + Bi-CharLSTM with modality attention (W+C): uses the modality attention to merge word and character embeddings.
> 
> (proposed) Bi-LSTM/CRF + Bi-CharLSTM + Inception (W+C+V): takes as input visual contexts extracted from InceptionNet as well, concatenated with word and char vectors.
> 
> (proposed) Bi-LSTM/CRF + Bi-CharLSTM + Inception with modality attention (W+C+V): uses the modality attention to merge word, character, and visual embeddings as input to entity LSTM.

#### Relevance 400

Label: 

#### Passage 401

Retrieved by: Hybrid RRF followed by BGE reranking

> We proposed a new multimodal NER (MNER: image + text) task on short social media posts. We demonstrated for the first time an effective MNER system, where visual information is combined with textual information to outperform traditional text-based NER baselines. Our work can be applied to myriads of social media posts or other articles across multiple platforms which often include both text and accompanying images. In addition, we proposed the modality attention module, a new neural mechanism which learns optimal integration of different modes of correlated information. In essence, the modality attention learns to attenuate irrelevant or uninformative modal information while amplifying the primary modality to extract better overall representations. We showed that the modality attention based model outperforms other state-of-the-art baselines when text was the only modality available, by better combining word and character level information.

#### Relevance 401

Label: 

## Question 0045

Paper: Creating a Real-Time, Reproducible Event Dataset

> What language is this dataset in?

### Common Retrieved Chunks

#### Passage 402

Retrieved by: BM25, Dense, Hybrid RRF

> PETRARCH (Python Engine for Text Resolution And Related Coding Hierarchy) is the new generation of event-data coding software that is the successor to the TABARI software. As noted in the previous sections, the major advance of this next generation of event data coding is the incorporation of a “deep parse” that enables more advanced analysis of the syntactic structure of sentences. In PETRARCH's case, this deep parse is provided by the Stanford NLP group's CoreNLP software BIBREF14 . CoreNLP provides information regarding part-of-speech tags for individual words, noun and verb phrase chunking, and syntactic information regarding the relation of noun and verb phrases. Figure 1 provides an example of what information CoreNLP outputs, while Figure 2 provides an example of the input that PETRARCH accepts.
> 
> The main advantage that this deep parse information provides for the current iteration of PETRARCH is improved noun and verb phrase disambiguation. At its heart, PETRARCH is still software to perform a lookup of terms in a set of text dictionaries. Given this, if the terms identified by the program are incorrect then the final event coding will also be incorrect. The list of noun and verb phrases created as output by CoreNLP increases the probability that the terms used to match in the dictionaries are “good.” Thus, in theory, PETRARCH coding should be more accurate due to a more accurate identification of noun phrases, which translates to actor lookups, and verb phrases, which translates to event code lookups. To put it bluntly, PETRARCH operates in much the same manner as TABARI, but offloads the issues of dealing with syntactic and grammatical structures to purpose-built software.
> 
> The downside of the use of deep parse information is the increased computational load required to process the news stories. TABARI is capable of processing upwards of 10,000 sentences per second, whereas CoreNLP can process less than 100 sentences per second and PETRARCH codes around 100 sentences per second. The slowness of CoreNLP is due to the complexity of applying the parsing models to English-language sentences. PETRARCH is slow for a variety of reasons, foremost among them being the use of the Python programming language as opposed to the C++ language TABARI uses. Additionally,

#### Relevance 402

Label: 

#### Passage 403

Retrieved by: BM25, Dense, Hybrid RRF

> Automated coding of political event data, or the record of who-did-what-to-whom within the context of political actions, has existed for roughly two decades. The approach has remained largely the same during this time, with the underlying coding procedures not updating to reflect changes in natural language processing (NLP) technology. These NLP technologies have now advanced to such a level, and with accompanying open-source software implementations, that their inclusion in the event-data coding process comes as an obvious advancement. When combined with changes in how news content is obtained, the ability to store and process large amounts of text, and enhancements based on two decades worth of event-data experience, it becomes clear that political event data is ready for a next generation dataset.
> 
> In this chapter, I provide the technical details for creating such a next-generation dataset. The technical details lead to a pipeline for the production of the Phoenix event dataset. The Phoenix dataset is a daily updated, near-real-time political event dataset. The coding process makes use of open-source NLP software, an abundance of online news content, and other technical advances made possible by open-source software. This enables a dataset that is transparent and replicable, while providing a more accurate coding process than previously possible. Additionally, the dataset's near-real-time nature also enables many applications that were previously impossible with batch-updated datasets, such as monitoring of ongoing events. Thus, this dataset provides a significant improvement over previous event data generation efforts.
> 
> In the following sections I briefly outline the history of computer-generated political event data to this point in history. I then outline what the “next generation” of event data should look like. Following this, I discuss the many facets of creating a real-time political event dataset, mainly from a technological and infrastructure standpoint. Finally, the paper concludes with a brief empirical view of the Phoenix event dataset, which is the output of the previously-discussed technological pipeline.

#### Relevance 403

Label: 

#### Passage 405

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The Phoenix dataset is an attempt to take both the new advances in event data described above, along with decades of knowledge regarding best practices, in order to create a new iteration of event data. The dataset makes use of 450 English-language news sites, which are each scraped every hour for new content. New data is generated on a daily basis, coded according to the CAMEO event ontology, with an average of 2,200 events generated per day. The full dataset examined here contains 254,060 total events spread across 102 days of generated data. Based on publicly available information, the project also makes use of the most up-to-date actor dictionaries of any available machine-coded event dataset.
> 
> The dataset currently contains 27 columns: “EventID”, “Date”, “Year”, “Month”, “Day”, “SourceActorFull”, “SourceActorEntity”, “SourceActorRole”, “SourceActorAttribute”, “TargetActorFull”, “TargetActorEntity”, “TargetActorRole”, “TargetActorAttribute”, “EventCode”, “EventRootCode”, “QuadClass”, “GoldsteinScore”, “Issues”, “ActionLat”, “ActionLong”, “LocationName”, “GeoCountryName”, “GeoStateName”, “SentenceID”, “URLs”, “NewsSources.” While there are columns included for geolocation of events, this feature is not fully implemented due to the difficult nature of accurately geolocating event data.
> 
> The *ActorFull columns include the full actor coding, which is made up of several three-letter CAMEO codes strung together. *ActorEntity breaks out the top-level code, which is usually a country code but can also be “IMG” for international militarized group, “IGO” for inter(national) governmental organizations, or “MNC” for multinational corporations. *ActorRole includes codes like “GOV”, “MED”, “EDU”, “MIL”, and *ActorAttribute includes modifiers, such as “MOS”, “INS”, “ELI” (Muslim, insurgent, and elite).
> 
> EventCode is the full CAMEO code, while EventRootCode is the 20 top-level CAMEO categories. The QuadClass is an updated version of the quad class divisions seen in other event datasets. The changes include the creation of a 0 code for CAMEO category 01 (“Make a Statement”), rather than counting 01 as verbal cooperation, as well as several lower-level codes changing quad classes. Previous quadclass implementations sliced the CAMEO categories in a linear fashion. This new implementation takes into consideration what the CAMEO categories actually suggest in terms of material or verbal conflict/cooperation. In this scheme, 0 is “Neutral,” 1 is “Verbal Cooperation,” 2 is “Material Cooperation,” 3 is “Verbal Conflict,” and 4 is “Material Conflict.” The categories are as follows:
> 
> ￼￼
> 
> The

#### Relevance 405

Label: 

#### Passage 407

Retrieved by: Dense, Hybrid RRF

> One of the defining traits of previous event-data projects is the method through which they were generated. The original datasets such as WEIS and COPDAB were created by human coders who read news stories and coded events. Future datasets such as KEDS and Phil Schrodt's Levant dataset were created using automated coding software, such as KEDS or TABARI, and news stories download from content aggregators such as Lexis Nexis or Factiva. Both pieces of coding software made use of a technique referred to as shallow parsing BIBREF13 . Shallow parsing is best understood in contrast to a deep parsing method. In deep parsing, the entire syntactic structure of a sentence is used and understood. This syntactic structure includes things such as prepositional phrases, direct and indirect objects, and other grammatical structures. A shallow parse, however, focuses solely on, as the name implies, shallow aspects such as the part of speech of the words within the sentence.
> 
> The second major dimension that differentiates event datasets is how news content was acquired. For WEIS and COPDAB this was as simple as subscribing to the New York Times and coding from there. Later datasets, such as those created in conjunction with the Kansas Event Data Project, obtained historical content from aggregators, as mentioned above. This difficulty of this process changed at various points in time, with something like full automation possible at some points while human downloading of stories was required at others. There are often gaps in this historical content since the content aggregators catalog of different news services changes at various points and is often fairly limited. Updating datasets based on this type of content was also fairly labor intensive since new content had to be downloaded, cleaned, and run for every update. While orders of magnitude faster than human coding, this remained an involved process.
> 
> Taken together, these two aspects of event data generation, shallow parsing and content acquisition, form the basis for where the next generation of political event data can improve upon previous efforts. In short, a shift to deep parsing based on relatively recent advances in open-source natural language processing software, combined with realtime acquisition of news content and aggressive strategies for

#### Relevance 407

Label: 

#### Passage 408

Retrieved by: Dense, Hybrid RRF

> This paper has shown that creating a near-real-time event dataset, while using deep parsing methods and advanced natural language processing software, is feasible and produces useful results. The combination of various technological and software advances enables a new generation of political event data that is distinctly different from previous iterations. In addition to the advances in accuracy and coverage, the marginal cost of generating event data is now nearly zero. Even with previous automated coding efforts, human intervention was necessary to gather and format news content. With the addition of real-time web scraping, the entire system has moved much closer to a “set it and forget it” model. The primary interaction needed once the system is running is to periodically check to ensure that relevant content is scraped and that no subtle bugs cause the system to crash.
> 
> While this new generation provides an improvement over previous iterations, there is still much work to be done. The main place for future work is deeper integration with the open-source NLP software. The PETRARCH system currently uses the parse information provided by CoreNLP to distinguish noun and verb phrases. This is actually a fraction of the information provided by CoreNLP. Additional information includes named entity recognition and a semantic dependency parse, which shows how words relate to each other in a more complex way than in the standard parse tree BIBREF21 . Using this information would allow for a more accurate event coding since events could be constructed in a manner that fits better with the natural construction of a sentence. Additionally, using a semantic dependency parse could alleviate issues of constructing arbitrary actor codings since codes would be built based on noun-adjective relationships. When combined with named entity recognition this could prove to be a quite powerful approach.

#### Relevance 408

Label: 

### BM25

#### Passage 404

Retrieved by: BM25

> due to the complexity of applying the parsing models to English-language sentences. PETRARCH is slow for a variety of reasons, foremost among them being the use of the Python programming language as opposed to the C++ language TABARI uses. Additionally, speed issues likely arise from the internal data representation of PETRARCH as opposed to TABARI; with TABARI making use of more efficient lookup algorithms and data structures.
> 
> PETRARCH2 represents a further iteration upon the basic principles seen in PETRARCH, mainly a deep reliance on information from a syntactic parse tree. The exact operational details of PETRARCH2 are beyond the scope of this chapter, with a complete explanation of the algorithm available in BIBREF15 , it should suffice to say that this second version of PETRARCH makes extensive use of the actual structure of the parse tree to determine source-action-target event codings. In other words, PETRARCH still mainly focused on parsing noun and verb phrase chunks without fully integrating syntactic information. In PETRARCH2 the tree structure of sentences is inherent to the coding algorithm. Changing the algorithm to depend more heavily on the tree structure of the sentence allows for a clearer identification of actors and the assignment of role codes to the actors, and a more accurate identification of the who and whom portions of the who-did-what-to-whom equation. The second major change between PETRARCH and PETRARCH2 is the internal category coding logic within PETRARCH2. In short, PETRARCH2 allows for interactions of verbs to create a different category classification than either verb on its own would produce. For PETRARCH, such things would have to be defined explicitly within the dictionaries. In PETRARCH2, however, there is a coding scheme that allows verbs like “intend” and “aid” to interact in order to create a different coding than either verb on its own would create. Additionally, PETRARCH2 brought about a refactoring and speedup of the code base and a reformatting of the underlying verb dictionaries. This reformatting of the dictionaries also included a “cleaning up” of various verb patterns within the dictionaries. This was largely due to changes internal to the coding engine such as the tight coupling to the constituency parse tree and the verb interactions mentioned above.

#### Relevance 404

Label: 

#### Passage 406

Retrieved by: BM25

> are the low-level events described in the previous section, but the “Material Conflict” class is higher than in the broader dataset. This is, of course, as expected given the ongoing conflict within Syria.
> 
> Figures 11 and 12 show the top actor and entity codes for the Syria subset. Various Syrian actors appear most often, with other Middle East countries also accounting for a fairly high portion of events. Also seen within this group of top actors is ISIL and the United States. Additionally, Russia appears high in the rankings of actors within Syria, capturing the recent activity by Russian forces in support of the Assad regime.
> 
> Overall, the Syrian subset of the data suggests that the Phoenix dataset is doing an adequate job of picking up events of interest in a conflict zone. The actor and event distributions follow what one would expect for the Syrian conflict. Additionally, there are no obvious errors in which actors make up the top participants in the subset. This examination provides confidence that the dataset is “working” in terms of face validity.

#### Relevance 406

Label: 

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 409

Retrieved by: Hybrid RRF followed by BGE reranking

> of the Python library Goose. Goose works through a series of heuristic rules to identify which portions of the web page contain content rather than things such as navigation links and advertisements. These heuristics operate on the HTML tags within a page, and the inherent tree-structure of the relationships between these tags. I, with the contributions of others, created an open-source software implementation of this RSS scraping concept which works well for a couple hundred RSS feeds. As the scope and ambition of the event data project grew, however, it became clear that this implementation is less than adequate for the task. Thus, the final scraper product, named atlas, moved to a distributed worker queue model that continuously queries RSS feeds to check for new links and consumes new content as it becomes available. This architecture has enabled the scraping of over 500 RSS feeds in both English and Arabic. This distributed architecture also allows for nearly infinite scalability; workers can move from process on an individual server to process on a cluster of servers.
> 
> This scraped content is stored in a NoSQL database, specifically a MongoDB instance, due to the inherently flexible nature of NoSQL databases. The lack of a predefined schema allows requirements and storage strategies to change and update as the scraping process matures and more knowledge is gained. This is especially important given the ever changing nature of web scraping. Some sites can move from being viable sources of information to no longer being useful or relevant. Sometimes sites update and break the scraping process. A flexible storage format allows for this information to be accommodated as it arises.
> 
> The final additional piece of information necessary for a modern event dataset is the geolocation of the coded events. The geolocation of event data is difficult from both a technological and ontological perspective. First, from an ontological standpoint, deciding which location to pick as the location for an event is often difficult. For example, a sentence such as “Speaking from the Rose Garden, President Obama denounced the Russian actions in Syria” provides several possible locations: the Rose Garden, Syria, and even, possibly, Russia. It is also possible for an event to have

#### Relevance 409

Label: 

#### Passage 410

Retrieved by: Hybrid RRF followed by BGE reranking

> dictionaries also included a “cleaning up” of various verb patterns within the dictionaries. This was largely due to changes internal to the coding engine such as the tight coupling to the constituency parse tree and the verb interactions mentioned above. This change in the event coder software further demonstrates the modular and composable nature of the processing pipeline; the rest of the processing architecture is able to remain the same even with a relatively major shift in the event coding software.
> 
> There are several ways that the scraping of news content from the web can occur. A system can sit on top of an aggregator such as Google News, use a true spidering system that follows links from a seed list, or can pull from a designated list of trusted resources. Each system has its benefits and challenges. The use of an aggregator means that a project is subject to another layer of complexity that is out of the user's control; those making use of Google News have no say over how, and what, content is aggregated. Implementing a full-scale web spider to obtain news content is a labor and maintenance intensive process that calls for a dedicated team of software engineers. This type of undertaking is beyond the scope of the current event data projects. The final option is to use a list of predefined resources, in this case RSS feeds of news websites, and pull content from these resources. For the purposes of the realtime event data discussed herein, I have settled on the final option.
> 
> The conceptual implementation of a web scraper built on top of RSS is relatively simple. Given a defined list of RSS feeds, pull those feeds at a fixed time interval and obtain the links to news stories contained within the feeds. The final step is to then follow the links to the news stories and obtain the news content. The relevant content is obtained through the use of the Python library Goose. Goose works through a series of heuristic rules to identify which portions of the web page contain content rather than things such as navigation links and advertisements. These heuristics operate on the HTML tags within

#### Relevance 410

Label: 

#### Passage 411

Retrieved by: Hybrid RRF followed by BGE reranking

> While the features discussed in the previous section provide a significant change from previous generations of event data, moving the field forward also comes with some unexpected challenges. Issues of processing time, data/software versioning, updating dictionaries, and reconceptualizing how event data is coded come into play when moving the event data research program forward. Each of these issues is a difficult problem when taken alone, when combined the obstacles can seem unsurmountable. Future iterations of event data will need to consider and address each of these issues.
> 
> One of the biggest unforeseen issues when moving from a shallow to a deep parse was the exponential increase in processing time. The TABARI program was extremely fast for two reasons: it is highly optimized C++ code and the shallow parsing markup is a speedy operation. PETRARCH requires a deep parse generated by software such as CoreNLP. CoreNLP takes a large amount of time to complete a deep parse of news stories. This means that the processing load for realtime data updating is more than a single consumer computer can handle. It also means that processing large amounts of historical text takes a significant amount of time.
> 
> Processing realtime data also means that the relevant actors are often changing. For example, during the development process of this event data project the Islamic State of Iraq and the Levant (ISIL) became a major actor in the Middle East. ISIL and its leadership were not encoded in the actor dictionaries used in any event data project. Updates to the dictionaries to include these actors lead to a near doubling of events coded in the relevant countries. This presents a serious issue for the sustainability of realtime coding; dictionary updating is a labor intensive process that lacks much of the appeal to potential funders that other projects have. Automated entity extraction is an area of active research that can help in this situation, but the main step, actually creating new actor codes for the relevant entities, is one that currently still needs a “human in the loop.”
> 
> The constantly changing nature of the constituent parts of the event data coding process (both software and text dictionaries) creates a problem for various

#### Relevance 411

Label: 

#### Passage 412

Retrieved by: Hybrid RRF followed by BGE reranking

> next generation of political event data can improve upon previous efforts. In short, a shift to deep parsing based on relatively recent advances in open-source natural language processing software, combined with realtime acquisition of news content and aggressive strategies for acquiring historical material, provide the motivation for the next generation of political event data. The following section provides greater detail regarding the implementation of these new features.

#### Relevance 412

Label: 

## Question 0046

Paper: Affective Behaviour Analysis of On-line User Interactions: Are On-line Support Groups more Therapeutic than Twitter?

> How large is the Twitter dataset?

### Common Retrieved Chunks

#### Passage 413

Retrieved by: BM25, Dense, Hybrid RRF

> We verify the presence of therapeutic factors in two social media datasets: OSG and Twitter. The first dataset is crawled from an on-line support groups website, and the second dataset consists of a small sample of Twitter conversation threads. Since the former consists of multi-threaded conversations, we apply a pre-processing to extract conversation threads to provide a fair comparison with the Twitter dataset. An example conversation from each data source is presented in Figure FIGREF19.

#### Relevance 413

Label: 

#### Passage 414

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Our data has been developed by crawling and pre-processing an OSG web forum. The forum has a great variety of different groups such as depression, anxiety, stress, relationship, cancer, sexually transmitted diseases, etc. Each conversation starts with one post and can contain multiple comments. Each post or comment is represented by a poster, a timestamp, a list of users it is referencing to, thread id, a comment id and a conversation id. The thread id is the same for comments replying to each other, otherwise it is different. The thread id is increasing with time. Thus, it provides ordering among threads; whereas the timestamp provides ordering in the thread.
> 
> Each conversation can belong to multiple groups. Consequently, the dataset needs to be processed to remove duplicates. The dataset resulting after de-duplication contains 295 thousand conversations, each conversation contains on average 6 comments. In total, there are 1.5 million comments. Since the created dataset is multi-threaded, we need to extract conversation threads, to eliminate paths not relevant to the original post.

#### Relevance 414

Label: 

#### Passage 415

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We have downloaded 1,873 Twitter conversation threads, roughly 14k tweets, from a publicly available resource that were previously pre-processed and have conversation threads extracted. A conversation in the dataset consists of at least 4 tweets. Even though, according to BIBREF23, Twitter is broadly applicable to public health research, our expectation is that it contains less therapeutic conversations in comparison to specialized on-line support forums.

#### Relevance 415

Label: 

#### Passage 416

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> family of origin issues. In this paper, we focus on 3 therapeutic factors: Universality, Altruism and Instillation of Hope (listed below), as we believe that these can be approximated by using established NLP techniques (e.g. Sentiment Analysis, Dialogue Act tagging etc.).
> 
> Universality: the disconfirmation of a user's feelings of uniqueness of their mental health condition.
> 
> Altruism: others offer support, reassurance, suggestions and insight.
> 
> Instillation of Hope: inspiration provided to participants by their peers.
> 
> The selected therapeutic factors are analysed in terms of illocutionary force and attitude. Due to the multi-party and asynchronous nature of on-line social media conversations, prior to the analysis, we extract conversation threads among users – an essential prerequisite for any kind of higher-level dialogue analysis BIBREF10. Afterwards, the illocutionary force is identified using Dialogue Act tagging, whereas the attitude by using Sentiment Analysis. The quantitative analysis is then performed on these processed conversations.
> 
> Ideally, the analysis would require experts to annotate each post and comment on the presence of therapeutic factors. However, due to time and cost demands of this task, it is feasible to analyse only a small fraction of the available data. Compared to previous studies (e.g. BIBREF6) that analysed few tens of conversations and several thousand lines of chat; using the proposed approach – application of Dialogue Acts and Sentiment Analysis – we were able to automatically analyse approximately 300 thousands conversations (roughly 1.5 million comments). The rest of the paper is structured as follows. In Section 2 we introduce related work. Next, in Section 3 we describe the pre-processing pipeline and the methodology to perform thread extraction on asynchronous multi-party conversations. In Section 4 we provide the describe the final dataset used for the analysis, and in Section 5 we present the results of our analysis. Finally, in Section 6 we provide concluding remarks and future research directions.

#### Relevance 416

Label: 

#### Passage 417

Retrieved by: BM25, Hybrid RRF

> The first condition which we test is the sentiment change in conversation threads, comparing the initial and final sentiment scores (i.e. posts' scores) of the original poster. The results of the analysis are presented in Figure FIGREF33. In the figure we can observe that the distribution of the sentiment change in the two datasets is different. While in Twitter the amount of conversations that lead to the increase of sentiment score is roughly equal to the amount of conversations that lead to the decrease of sentiment score; the situation is different for OSG. In OSG, the amount of conversations that lead to the increase of sentiment score is considerably higher.
> 
> Figure FIGREF34 provides a more fine grained analysis, where we additionally analyse the sentiment change in nominal polarity terms – negative and positive. In OSG, the number of users that changed polarity from negative to positive is more than the double of the users that have changed the polarity from positive to negative. In Twitter, on the other hand, the users mostly changed polarity from positive to negative. Results of the analysis suggest that in OSG , sentiment increases and users tend to change polarity from negative to positive, whereas in Twitter sentiment tends to decrease. Verification of this condition alone indicates that the ratio of potentially therapeutic conversations in Twitter is lower.

#### Relevance 417

Label: 

#### Passage 419

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Table TABREF36 presents the distribution of automatically predicted per-sentence Dialogue Acts in the datasets. The most frequent tag is statement in both. In Table TABREF37, on the other hand, we present the distribution of post and comment structures in terms of automatically predicted Dialogue Act tags. The structure is an unordered set of tags in the post or comment. From the table we can observe that the distribution of tag sets is similar between posts and comments. In both cases the most common set is statement only. However, conversations containing only statement, emphasis or question posts and comments predominantly appear in Twitter. Which is expected due to the shorter length of Twitter posts and comments.
> 
> We can also observe that the original posters tend to ask more questions than the commenting posters – 19.83% for posts vs. 11.21% for comments (summed). This suggests that the original posters frequently ask either for suggestion or confirmation of their points of view or their disconfirmation. However, the high presence of personal experiences is supported by the high number of posts containing only statements.
> 
> High number of statement tags in comments suggests that users reply either with supporting or empathic statements or personal experience. However, 6.39% of comments contain accept and reject tags, which mark the degree to which a speaker accepts some previous proposal, plan, opinion, or statement BIBREF20. The described Dialogue Act tags are often used when commenting posters discuss original poster's point of view. For instance, “It's true. I felt the same.” – {Accept, Statement} or “Well no. You're not alone” – {Reject, Statement}. The datasets differ with respect to the distribution of these Dialogue Acts tags, they appear more frequently in OSG.

#### Relevance 419

Label: 

### BM25

None

### Dense

#### Passage 418

Retrieved by: Dense

> For both data sources, Twitter and OSG with extracted threads, posts and comments are tokenized and sentence split. Each sentence is passed through Sentiment Analysis and Dialogue Act tagging. Since a post or a comment can contain multiple sentences, therefore multiple Dialogue Acts, it is represented as as a one-hot encoding, where each position represents a Dialogue Act.
> 
> For Sentiment Analysis we use a lexicon-based sentiment analyser introduced by BIBREF25. For Dialogue Act tagging, on the other hand, we make use of a model trained on NPSChat corpus BIBREF22 following the approach of BIBREF26.

#### Relevance 418

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 420

Retrieved by: Hybrid RRF followed by BGE reranking

> Table TABREF39 presents the distribution of sentiment polarity in post and comment statements (i.e. sentences tagged as statement). For OSG, the predominant sentiment label of statements is positive and it is the highest for both posts and comments. However, the difference between the amounts of positive and negative statements is higher for the replying comments (34.5% vs. 42.5%). For Twitter, on the other hand, the predominant sentiment label of statements is neutral and the polarity distribution between posts and comments is very close. One particular observation is that the ratio of negative statements is higher in OSG for both posts and comments than in Twitter, which supports the idea of sharing negative experiences.
> 
> Further we analyze whether the sentiment of a comment (i.e. the replying user) is affected by the sentiment of the original post (i.e. the user being replied to), which will imply that the users adapt their behaviour with respect to the post's sentiment. For the analysis, we split the datasets into three buckets according to the posts' sentiment score – negative, neutral, or positive, and represent each conversation in terms of percentages of comments (replies) with each sentiment label. The buckets are then compared using t-test for statistically significant differences.
> 
> Table TABREF40 presents the distribution of sentiment labels with respect to the post's sentiment score. The patterns of distribution are similar across the datasets. We can observe that overall, replies tend to have a positive sentiment, which suggests that replying posters tend to have a positive attitude. However, the ratio of positive comments is higher for OSG than for Twitter.
> 
> The results of the Welch's t-test on OSG data reveal that there are statistically significant differences in the distribution of replying comments' sentiment between conversations with positive and negative starting posts. A positive post tends to get significantly more positive replies. Similarly, a negative post tends to get significantly more negative replies (both with $p < 0.01$).
> 
> Table TABREF41 presents the distribution of the sentiment labels of the final text provided by the original poster with respect to the sentiment polarity of the comments. The results indicate that OSG participants are more supportive, as the majority of conversations end in a positive

#### Relevance 420

Label: 

## Question 0047

Paper: Offensive Language Detection: A Comparative Analysis

> What is the Random Kitchen Sink approach?

### Common Retrieved Chunks

#### Passage 421

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this work, we have selected word vectors generated by Google universal encoder model, Fasttext, and DMD based features. The classification using the selected features are performed using machine learning algorithms such as Random Forest (RF), Decision Tree (DT), Naive Bayes (NB), Support vector machine (SVM) linear and RBF kernels, Logistic Regression, and Random kitchen sinks. The evaluation measures used are accuracy (Acc.), precision (Prec), recall, f1-score (F1). Table TABREF21 shows the classification result obtained for classical machine learning algorithms using the Google universal sentence encoder model features. It can be observed that svm linear classifier and Logistic regression has given maximum accuracy of 82.44% and 82.56%.
> 
> Table TABREF22 shows the classification results obtained using the features generated by fasttext model for classical machine learning algorithms. For the fasttext model also, svm linear and logistic regression model have given maximum accuracies of 81.16% respectively.

#### Relevance 421

Label: 

#### Passage 422

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> RKS approach proposed in BIBREF21, BIBREF22, explicitly maps data vectors to a space where linear separation is possible. It has been explored for natural language processing tasks BIBREF23, BIBREF24. The RKS method provides an approximate kernel function via explicit mapping.
> 
> Here, $\phi (.)$ denotes the implicit mapping function (used to compute kernel matrix), $Z(.)$ denotes the explicit mapping function using RKS and ${\Omega _k}$ denotes random variable .
> 
> Figure FIGREF15 show the block diagram of the proposed approach.

#### Relevance 422

Label: 

#### Passage 423

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Offensive language detection is an important task related to social media data analysis. The nature of the content can vary as its provided by different people. The current work uses the data provided in SemEval 2019 shared task A for Offensive language identification. A comparative study is provided by exploring the effectiveness of Google universal sentence encoder, Fasttext based embedding, Dynamic Mode Decomposition based features and RKS based explicit mapping approach. For the experiments, we used the machine learning methods such as SVM linear, Random Forest, Logistic regression, Navie Bayes and Regularized least-square based classification. The measures used for evaluation are accuracy, precision, recall, and f1-score. We observed that RKS approach improved the results. However, as a future work, the proposed approach cane be explored on large datasets.

#### Relevance 423

Label: 

#### Passage 424

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> Word embeddings are ubiquitous for any NLP problem, as algorithms cannot process the plain text or strings in its raw form. Word emeddings are vectors that captures the semantic and contextual information of words. The word embedding used for this work are:
> 
> FastText: The fastText algorithm created by Facebook BIBREF10 assumes every word to be n-grams of character. It helps to give the vector representations for out of vocabuary words. For the current work, fasttext based word embedding is used for generating token vectors of dimension 300 BIBREF11. Each vector corresponding to the tweet is generated by taking the average of token vectors.
> 
> Universal Sentence Encoder: Developed by Google, Universal sentence encoder BIBREF12, BIBREF13 provides embeddings at sentence level. The dimension of the embedding vector is 512, irrespective of the number of tokens in the input tweet. These vectors can capture good semantic information from the sentences. For each tweet, this model generates a 512 length embedding vector and is used as features for further classification.
> 
> DMD and HODMD: DMD is a method initially used in fluid dynamics which captures spatio-temporal features BIBREF14. It has been used in background-foreground separation BIBREF15, load forecasting BIBREF16, saliency detection BIBREF17 etc. For natural language processing, DMD has been first applied for sentiment analysis BIBREF18, BIBREF19. This motivated to explore DMD based feature for the present work.
> 
> Dynamic mode decomposition (DMD) is a much more powerful concept and it assumes the evolution of the function over the rectangular field is effected by the mapping of a constant matrix $A$. $A$ captures the system’s inherent dynamics and the aim of the DMD is to understand using its dominant eignevalues and eigenvectors. Assumption is that this matrix $A$ is of low rank and hence the sequence of vectors $ \mathop {{x_1}}\limits _|^| ,\mathop {{x_2}}\limits _|^| ,\mathop {{x_3}}\limits _|^| ,...\mathop {,{x_k}}\limits _|^| ,...,\mathop {{x_{m + 1}}}\limits _|^| $ finally become a linearly dependent set. That is, vector $ \mathop {{x_{m + 1}}}\limits _|^|$ become linearly dependent on previous vectors. The data matrix X in terms of eigen vectors associated with matrix $A$.
> 
> where, ${\Phi ^\dag }$ is pseudo inverse of ${\Phi }$. $A$ is of rank m and ${\Phi }$ have m

#### Relevance 424

Label: 

#### Passage 425

Retrieved by: BM25, Hybrid RRF

> RKS approach has been used in the articles for NLP tasks [29,30,23]. In this work, we use RKS to imporve the evaluation scores as discussed previously. The RKS approach explicitly maps the embedding vectors to a dimension where the data becomes linearly separable. In that space, regularized least-square based classification (RLSC) is performed. The implementation of the RKS is taken from BIBREF29, BIBREF30. The feature vectors from Google universal sentence encoder and fasttext are explicitly mapped using RKS and the results are tabulated in Table TABREF27 and TABREF28.
> 
> The Table TABREF27 shows the classification report on the proposed RKS method taking word vectors generated by Google universal encoder model as features with dimension 512. For this work, such vector is explicitly mapped to dimensions 100, 200, 500 and 1000 using RKS. The maximum accuracy obtained is 90.58% for higher dimension 1000.
> 
> Table TABREF28 shows the classification report on the proposed RKS method taking word vectors generated by Fasttext model as features. For this model also, features are mapped to dimensions 100, 200, 500 and 1000. For Fasttext model, the proposed method gave a maximum accuracy of 99.53%, which is a bench marking result when compared to the literature. This result shows the discriminating capability of the features chosen, as when mapped to higher dimensions, they become linearly separable. From Table TABREF27 and TABREF28 it can be observed that as the mapping dimension increases, the evaluation score also improves. This shows the effectiveness of the RKS approach to obtain competing score. The capability of the RKS approach cane be explored on large datasets.

#### Relevance 425

Label: 

#### Passage 426

Retrieved by: Dense, Hybrid RRF

> Data pre-processing is a very crucial step which needs to be done before applying any machine learning tasks, because the real time data could be very noisy and unstructured. For the two models used in this work, pre-processing of tweets is done separately:
> 
> Pre-processing for Google model:
> 
> It has become a common culture to use #tags across social media. So we have replaced multiple #tags with a single #tag. Mostly @ symbol id used to mention person or entities in a tweet. So we replace multiple @symbols with a single @-mention. Some tweets may contain the link to a website or some other urls. So we replace all of these with a single keyword URLS.
> 
> Pre-processing for fasttext model:
> 
> For applying fasttext model to get word vectors, we followed a different set of pre-processing steps. First, all the numbers, punctuation marks, urls (http:// or www.) and symbols (emoji, #tags, -mention) were removed from the tweet as it do not contain information related to sentiment. After that, tokenization and lowercasing was applied to the tweets. Tokenization was done using tokenizer from NLTK package BIBREF9. Finally, the stop word are removed. The list is obtained from NLTK package.

#### Relevance 426

Label: 

### BM25

None

### Dense

#### Passage 427

Retrieved by: Dense

> This section describes the result as three different cases. Case 1 & 2 provides baseline approach to compare with the proposed RKS approcah described in case 3. Table TABREF19 gives the results of the top 5 teams of sub-task A. Team with rank 1 achieved a maximum f1-score of 82.9%.

#### Relevance 427

Label: 

#### Passage 428

Retrieved by: Dense

> participation. In Table TABREF19, the list of first 5 participants along with system and f1-score has been shown.
> 
> Offensive language detection is one of the challenging and interesting topic for research. Recent past had multiple shared tasks and research on this topic. One of the initial work on offensive language using supervised classification was done by Yin et al. BIBREF4. They have used Ngram, TFIDF and combination of TFIDF with Sentiment and Contextual as Features. Schmidt and Wiegand BIBREF5 gave a survey on automatic hate speech detection using NLP. The authors surveyed on features like Simple Surface Features, Word Generalization, Linguistic Features, Knowledge-Based Features, Multimodal Information etc. In 2013, a study on detecting cyberbullying in YouTube comments was done by Dadvar et al. BIBREF6. They have used a combination of content-based, cyberbullying-specific and user-based features and showed that detection of cyberbullying can be improved by taking user context into account. Shared task GermEval 2018 organised by Wiegand et al.,BIBREF7 was focused on offensive language detection on German tweets. It had a dataset of over 8,500 annotated tweets and was trained for binary classification of offensive and non-offensive tweets. They obtained an overall maco-F1 score of 76.77%. Another shared task on Aggression Identification in Social Media was organised by Kumar et al., BIBREF8. The task provided a dataset with 15,000 annotated Facebook posts and comments in Hindi and English. They obtained a weighted F-score of 64% for both English and Hindi. The rest of the paper is structured as follows. Section 2 explains about the methodology with formulation. Section 3 discusses on the Proposed approach. Section 4 talks on the Experiments and discussions performed. Finally, conclusion is given in Section 5.

#### Relevance 428

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 429

Retrieved by: Hybrid RRF followed by BGE reranking

> In order to provide a comparison, we explore DMD based features. The Table TABREF24 shows the result obtained for normal DMD and HODMD based feature. The order for HODMD for the present work is 2 & 3. The classification is performed using SVM-linear kernel with control parameter value chosen as 1000 as the suitable one. We tried for other values such as 0.1, 1, 100, 500, and 1000. Figure FIGREF25 shows the control parameter versus accuracy plot which helped to fix the parameter value.

#### Relevance 429

Label: 

## Question 0048

Paper: Neural Machine Translation for Low Resource Languages using Bilingual Lexicon Induced from Comparable Corpora

> What are the BLEU performance improvements they achieve?

### Common Retrieved Chunks

#### Passage 430

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Both neural and statistical machine translation approaches are highly reliant on the availability of large amounts of data and are known to perform poorly in low resource settings. Recent crowd-sourcing efforts and workshops on machine translation have resulted in small amounts of parallel texts for building viable machine translation systems for low-resource pairs BIBREF0 . But, they have been shown to suffer from low accuracy (incorrect translation) and low coverage (high out-of-vocabulary rates), due to insufficient training data. In this project, we try to address the high OOV rates in low-resource machine translation systems by leveraging the increasing amount of multilingual content available on the Internet for enriching the bilingual lexicon.
> 
> Comparable corpora such as Wikipedia, are collections of topic-aligned but non-sentence-aligned multilingual documents which are rich resources for extracting parallel sentences from. For example, Figure FIGREF1 shows that there are equivalent sentences on the page about Donald Trump in Tamil and English, and the phrase alignment for an example sentence is shown in Table TABREF4 .
> 
> Table TABREF2 shows that there are at least tens of thousands of bilingual articles on Wikipedia which could potentially have at least as many parallel sentences that could be mined to address the scarcity of parallel sentences as indicated in column 2 which shows the number of sentence-pairs in the largest available bilingual corpora for xx-en. As shown by BIBREF1 ( BIBREF1 ), the illustrated data sparsity can be addressed by extending the scarce parallel sentence-pairs with those automatically extracted from Wikipedia and thereby improving the performance of statistical machine translation systems.
> 
> In this paper, we will propose a neural approach to parallel sentence extraction and compare the BLEU scores of machine translation systems with and without the use of the extracted sentence pairs to justify the effectiveness of this method. Compared to previous approaches which require specialized meta-data from document structure or significant amount of hand-engineered features, the neural model for extracting parallel sentences is learned end-to-end using only a small bootstrap set of parallel sentence pairs.

#### Relevance 430

Label: 

#### Passage 431

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> maximum entropy classifier. The difference in the BLEU scores between out of domain and domain-specific translation is proved clearly using the word embeddings from characteristic vocabulary extracted using the extracted additional bitexts.
> 
> BIBREF2 ( BIBREF2 ) extract parallel sentences without the use of a classifier. Target language candidate sentences are found using the translation of source side comparable corpora. Sentence tail removal is used to strip the tail parts of sentence pairs which differ only at the end. This, along with the use of parallel sentences enhanced the BLEU score and helped to determine if the translated source sentence and candidate target sentence are parallel by measuring the word and translation error rate. This method succeeds in eliminating the need for domain specific text by using the target side as a source of candidate sentences. However, this approach is not feasible if there isn't a good source side translation system to begin with, like in our case.
> 
> Yet another approach which uses an existing translation system to extract parallel sentences from comparable documents was proposed by BIBREF3 ( BIBREF3 ). They describe a framework for machine translation using multilingual Wikipedia articles. The parallel corpus is assembled iteratively, by using a statistical machine translation system trained on a preliminary sentence-aligned corpus, to score sentence-level en–jp BLEU scores. After filtering out the unaligned pairs based on the MT evaluation metric, the SMT is retrained on the filtered pairs.

#### Relevance 431

Label: 

#### Passage 432

Retrieved by: BM25, Dense, Hybrid RRF

> For the evaluation of the performance of our sentence extraction models, we looked at a few sentences manually, and have done a qualitative analysis, as there was no gold standard evaluation set for sentences extracted from Wikipedia. In Table TABREF13 , we can see the qualitative accuracy for some parallel sentences extracted from Tamil. The sentences extracted from Tamil, have been translated to English using Google Translate, so as to facilitate a comparison with the sentences extracted from English.
> 
> For the statistical machine translation and neural machine translation evaluation we use the BLEU score BIBREF13 as an evaluation metric, computed using the multi-bleu script from Moses BIBREF14 .

#### Relevance 432

Label: 

#### Passage 433

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> A lot of work has been done on the problem of automatic sentence alignment from comparable corpora, but a majority of them BIBREF2 , BIBREF1 , BIBREF3 use a pre-existing translation system as a precursor to ranking the candidate sentence pairs, which the low resource language pairs are not at the luxury of having; or use statistical machine learning approaches, where a Maximum Entropy classifier is used that relies on surface level features such as word overlap in order to obtain parallel sentence pairs BIBREF4 . However, the deep neural network model used in our paper is probably the first of its kind, which does not need any feature engineering and also does not need a pre-existing translation system.
> 
> BIBREF4 ( BIBREF4 ) proposed a parallel sentence extraction system which used comparable corpora from newspaper articles to extract the parallel sentence pairs. In this procedure, a maximum entropy classifier is designed for all sentence pairs possible from the Cartesian product of a pair of documents and passed through a sentence-length ratio filter in order to obtain candidate sentence pairs. SMT systems were trained on the extracted sentence pairs using the additional features from the comparable corpora like distortion and position of current and previously aligned sentences. This resulted in a state of the art approach with respect to the translation performance of low resource languages.
> 
> Similar to our proposed approach, BIBREF5 ( BIBREF5 ) showed how using parallel documents from Wikipedia for domain specific alignment would improve translation quality of SMT systems on in-domain data. In this method, similarity between all pairs of cross-language sentences with different text similarity measures are estimated. The issue of domain definition is overcome by the use of IR techniques which use the characteristic vocabulary of the domain to query a Lucene search engine over the entire corpus. The candidate sentences are defined based on word overlap and the decision whether a sentence pair is parallel or not using the maximum entropy classifier. The difference in the BLEU scores between out of domain and domain-specific translation is proved clearly using the word embeddings from characteristic vocabulary extracted using the extracted additional bitexts.
> 
> BIBREF2 ( BIBREF2 ) extract parallel sentences without

#### Relevance 433

Label: 

#### Passage 434

Retrieved by: BM25, Hybrid RRF

> Here, we describe the neural network architecture as shown in BIBREF6 ( BIBREF6 ), where the network learns to estimate the probability that the sentences in a given sentence pair, are translations of each other, INLINEFORM0 , where INLINEFORM1 is the candidate source sentence in the given pair, and INLINEFORM2 is the candidate target sentence.
> 
> As illustrated in Figure FIGREF5 (d), the architecture uses a siamese network BIBREF7 , consisting of a bidirectional RNN BIBREF8 sentence encoder with recurrent units such as long short-term memory units, or LSTMs BIBREF9 and gated recurrent units, or GRUs BIBREF10 learning a vector representation for the source and target sentences and the probability of any given pair of sentences being translations of each other. For seq2seq architectures, especially in translation, we have found the that the recommended recurrent unit is GRU, and all our experiments use this over LSTM.
> 
> The forward RNN reads the variable-length sentence and updates its recurrent state from the first token until the last one to create a fixed-size continuous vector representation of the sentence. The backward RNN processes the sentence in reverse. In our experiments, we use the concatenation of the last recurrent state in both directions as a final representation INLINEFORM0 DISPLAYFORM0
> 
> where INLINEFORM0 is the gated recurrent unit (GRU). After both source and target sentences have been encoded, we capture their matching information by using their element-wise product and absolute element-wise difference. We estimate the probability that the sentences are translations of each other by feeding the matching vectors into fully connected layers: DISPLAYFORM0
> 
> where INLINEFORM0 is the sigmoid function, INLINEFORM1 , INLINEFORM2 , INLINEFORM3 , INLINEFORM4 and INLINEFORM5 are model parameters. The model is trained by minimizing the cross entropy of our labeled sentence pairs: DISPLAYFORM0
> 
> where INLINEFORM0 is the number of source sentences and INLINEFORM1 is the number of candidate target sentences being considered.
> 
> For prediction, a sentence pair is classified as parallel if the probability score is greater than or equal to a decision threshold INLINEFORM0 that we need to fix. We found that to get high precision sentence pairs, we had to use INLINEFORM1 , and if we were able to sacrifice some precision for recall, a lower

#### Relevance 434

Label: 

#### Passage 436

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this paper, we evaluated the benefits of using a neural network procedure to extract parallel sentences. Unlike traditional translation systems which make use of multi-step classification procedures, this method requires just a parallel corpus to extract parallel sentence pairs using a Siamese BiRNN encoder using GRU as the activation function.
> 
> This method is extremely beneficial for translating language pairs with very little parallel corpora. These parallel sentences facilitate significant improvement in machine translation quality when compared to a generic system as has been shown in our results.
> 
> The experiments are shown for English-Tamil and English-Hindi language pairs. Our model achieved a marked percentage increase in the BLEU score for both en–ta and en–hi language pairs. We demonstrated a percentage increase in BLEU scores of 11.03% and 14.7% for en–ta and en–hi pairs respectively, due to the use of parallel-sentence pairs extracted from comparable corpora using the neural architecture.
> 
> As a follow-up to this work, we would be comparing our framework against other sentence alignment methods described in BIBREF20 , BIBREF21 , BIBREF22 and BIBREF23 . It has also been interesting to note that the 2018 edition of the Workshop on Machine Translation (WMT) has released a new shared task called Parallel Corpus Filtering where participants develop methods to filter a given noisy parallel corpus (crawled from the web), to a smaller size of high quality sentence pairs. This would be the perfect avenue to test the efficacy of our neural network based approach of extracting parallel sentences from unaligned corpora.

#### Relevance 436

Label: 

#### Passage 437

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> We evaluated the quality of the extracted parallel sentence pairs, by performing machine translation experiments on the augmented parallel corpus.
> 
> As the dataset for training the machine translation systems, we used high precision sentences extracted with greedy decoding, by ranking the sentence-pairs on their translation probabilities. Phrase-Based SMT systems were trained using Moses BIBREF14 . We used the grow-diag-final-and heuristic for extracting phrases, lexicalised reordering and Batch MIRA BIBREF15 for tuning (the default parameters on Moses). We trained 5-gram language models with Kneser-Ney smoothing using KenLM BIBREF16 . With these parameters, we trained SMT systems for en–ta and en–hi language pairs, with and without the use of extracted parallel sentence pairs.
> 
> For training neural machine translation models, we used the TensorFlow BIBREF17 implementation of OpenNMT BIBREF18 with attention-based transformer architecture BIBREF19 . The BLEU scores for the NMT models were higher than for SMT models, for both en–ta and en–hi pairs, as can be seen in Table TABREF23 .

#### Relevance 437

Label: 

### BM25

None

### Dense

#### Passage 435

Retrieved by: Dense

> or equal to a decision threshold INLINEFORM0 that we need to fix. We found that to get high precision sentence pairs, we had to use INLINEFORM1 , and if we were able to sacrifice some precision for recall, a lower INLINEFORM2 of 0.80 would work in the favor of reducing OOV rates. DISPLAYFORM0

#### Relevance 435

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0049

Paper: Hint-Based Training for Non-Autoregressive Machine Translation

> Were any datasets other than WMT used to test the model?

### Common Retrieved Chunks

#### Passage 438

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We compare our model with several baselines, including three ART models, the fertility based (FT) NART model BIBREF5, the deterministic iterative refinement based (IR) NART model BIBREF6, and the Latent Transformer BIBREF7 which is not fully non-autoregressive by incorporating an autoregressive sub-module in the NART model architecture.
> 
> The results are shown in the Table TABREF15. Across different datasets, our method achieves significant improvements over previous non-autoregressive models. Specifically, our method outperforms fertility based NART model with 6.54/7.11 BLEU score improvements on WMT En-De and De-En tasks in similar settings and achieves comparable results with state-of-the-art LSTM-based model on WMT En-De task. Furthermore, our model achieves a speedup of 30.2 (output a single sentence) or 17.8 (teacher rescoring) times over the ART counterparts. Note that our speedups significantly outperform all previous works, because of our lighter design of the NART model: without any computationally expensive module trying to improve the expressiveness.
> 
> We also visualize the hidden state cosine similarities and attention distributions for the NART model with hint-based training, as shown in Figure FIGREF4(c) and FIGREF6(c). With hints from hidden states, the hidden states similarities of the NART model decrease in general, and especially for the positions where the original NART model outputs incoherent phrases. The attention distribution of the NART model after hint-based training is more similar to the ART teacher model and less ambiguous comparing to the NART model without hints.
> 
> According to our empirical analysis, the percentage of repetitive words drops from 8.3% to 6.5% by our proposed methods on the IWSLT14 De-En test set, which is a 20%+ reduction. This shows that our proposed method effectively improve the quality of the translation outputs. We also provide several case studies in Appendix.
> 
> Finally, we conduct an ablation study on IWSLT14 De-En task. As shown in Table TABREF18, the hints from word alignments provide an improvement of about 1.6 BLEU points, and the hints from hidden states improve the results by about 0.8 BLEU points. We also test these models on a subsampled set whose source sentence lengths are at least 40. Our model outperforms the baseline model by more than 3 BLEU points (20.63 v.s. 17.48).

#### Relevance 438

Label: 

#### Passage 439

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The evaluation is on two widely used public machine translation datasets: IWSLT14 German-to-English (De-En) BIBREF9, BIBREF1 and WMT14 English-to-German (En-De) dataset BIBREF4, BIBREF10. To compare with previous works, we also reverse WMT14 English-to-German dataset and obtain WMT14 German-to-English dataset.
> 
> We pretrain Transformer BIBREF8 as the teacher model on each dataset, which achieves 33.26/27.30/31.29 in terms of BLEU BIBREF11 in IWSLT14 De-En, WMT14 En-De and De-En test sets. The student model shares the same number of layers in encoder/decoder, size of hidden states/embeddings and number of heads as the teacher models (Figure FIGREF11). Following BIBREF5, BIBREF12, we replace the target sentences by the decoded output of the teacher models.
> 
> Hyperparameters ($\gamma _\mathit {st}, \gamma _\mathit {tr}, \lambda , \mu $) for hint-based learning are determined to make the scales of three loss components similar after initialization. We also employ label smoothing of value $\epsilon _\mathit {ls}=0.1$ BIBREF13 in all experiments. We use Adam optimizer and follow the setting in BIBREF8. Models for WMT14/IWSLT14 tasks are trained on 8/1 NVIDIA M40 GPUs respectively. The model is based on the open-sourced tensor2tensor BIBREF14. More settings can be found in Appendix.

#### Relevance 439

Label: 

#### Passage 440

Retrieved by: BM25, Hybrid RRF

> According to the case study in BIBREF5, the translations of the NART models contain incoherent phrases (e.g. repetitive words) and miss meaningful tokens on the source side, while these patterns do not commonly appear in ART models. After some empirical study, we find two non-obvious facts that lead to this phenomenon.
> 
> First, we visualize the cosine similarities between decoder hidden states of a certain layer in both ART and NART models for sampled cases. Mathematically, for a set of hidden states $r_1, \ldots , r_T$, the pairwise cosine similarity can be derived by $\cos _{ij} = {\left<r_i, r_j\right>}/{(\Vert r_i\Vert \cdot \Vert r_j\Vert )}.$ We then plot the heatmap of the resulting matrix $\cos $. A typical example is shown in Figure FIGREF4, where the cosine similarities in the NART model are larger than those of the ART model, indicating that the hidden states across positions in the NART model are “similar”. Positions with highly-correlated hidden states tend to generate the same word and make the NART model output repetitive tokens, e.g., the yellow area on the top-left of Figure FIGREF4(b), while this does not happen in the ART model (Figure FIGREF4(a)). According to our statistics, 70% of the cosine similarities between hidden states in the ART model are less than 0.25, and 95% are less than 0.5.
> 
> Second, we visualize the encoder-decoder attentions for sampled cases, shown in Figure FIGREF6. Good attentions between the source and target sentences are usually considered to lead to accurate translation while poor ones may cause wrong output tokens BIBREF0. In Figure FIGREF6(b), the attentions of the ART model almost covers all source tokens, while the attentions of the NART model do not cover “farm” but with two “morning”. This directly makes the translation result worse in the NART model. These phenomena inspire us to use the intermediate hidden information in the ART model to guide the learning process of the NART model.

#### Relevance 440

Label: 

#### Passage 441

Retrieved by: BM25, Dense, Hybrid RRF

> In this section, we first describe the observations on the ART and NART models, and then discuss what kinds of information can be used as hints to help the training of the NART model. We follow the network structure in BIBREF8, use a copy of the source sentence as decoder input, remove the attention masks in decoder self-attention layers and add a positional attention layer as suggested in BIBREF5. We provide a visualization of ART and NART models we used in Figure FIGREF11 and a detailed description of the model structure in Appendix.

#### Relevance 441

Label: 

#### Passage 443

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this paper, we proposed to use hints from a well-trained ART model to enhance the training of NART models. Our results on WMT14 En-De and De-En significantly outperform previous NART baselines, with one order of magnitude faster in inference than ART models. In the future, we will focus on designing new architectures and training methods for NART models to achieve comparable accuracy as ART models.

#### Relevance 443

Label: 

### BM25

#### Passage 442

Retrieved by: BM25

> Our study motivates us to leverage the intermediate hidden information from an ART model to improve the NART model. We focus on how to define hints from a well-trained ART teacher model and use it to guide the training process of a NART student model. We study layer-to-layer hints and assume both the teacher and student models have an $M$-layer encoder and an $N$-layer decoder, despite the difference in stacked components.
> 
> Without the loss of generality, we discuss our method on a given paired sentence $(x,y)$. In real experiments, losses are averaged over all training data. For the teacher model, we use $a_{t,l,h}^\mathit {tr}$ as the encoder-to-decoder attention distribution of $h$-th head in the $l$-th decoder layer at position $t$, and use $r_{t,l}^\mathit {tr}$ as the output of the $l$-th decoder layer after feed forward network at position $t$. Correspondingly, $a_{t,l,h}^\mathit {st}$ and $r_{t,l}^\mathit {st}$ are used for the student model. We propose a hint-based training framework that contains two kinds of hints:

#### Relevance 442

Label: 

### Dense

#### Passage 444

Retrieved by: Dense

> those of ART model. Therefore, we design two kinds of hints from the hidden states and attention distributions of the ART model to help the training of the NART model. The experimental results show that our model achieves significant improvement over the NART baseline models and is even comparable to a strong ART baseline in BIBREF4.

#### Relevance 444

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 445

Retrieved by: Hybrid RRF followed by BGE reranking

> During training, $T_y$ does not need to be predicted as the target sentence is given. During testing, we have to predict the length of the target sentence for each source sentence. In many languages, the length of the target sentence can be roughly estimated from the length of the source sentence. We choose a simple method to avoid the computational overhead, which uses input length to determine target sentence length: $T_y = T_x + C$, where $C$ is a constant bias determined by the average length differences between the source and target training sentences. We can also predict the target length ranging from $[(T_x+C)-B, (T_x+C)+B]$, where $B$ is the halfwidth. By doing this, we can obtain multiple translation results with different lengths. Note that we choose this method only to show the effectiveness of our proposed method and a more advanced length estimation method can be used to further improve the performance.
> 
> Once we have multiple translation results, we additionally use our ART teacher model to evaluate each result and select the one that achieves the highest probability. As the evaluation is fully parallelizable (since it is identical to the parallel training of the ART model), this rescoring operation will not hurt the non-autoregressive property of the NART model.

#### Relevance 445

Label: 

#### Passage 446

Retrieved by: Hybrid RRF followed by BGE reranking

> We observe that meaningful words in the source sentence are sometimes untranslated by the NART model, and the corresponding positions often suffer from ambiguous attention distributions. Therefore, we use the word alignment information from the ART model to help the training of the NART model.
> 
> In particular, we minimize KL-divergence between the per-head encoder-to-decoder attention distributions of the teacher and the student to encourage the student to have similar word alignments to the teacher model, i.e.
> 
> Our final training loss $\mathcal {L}$ is a weighted sum of two parts stated above and the negative log-likelihood loss $\mathcal {L}_\mathit {nll}$ defined on bilingual sentence pair $(x, y)$, i.e.
> 
> where $\lambda $ and $\mu $ are hyperparameters controlling the weight of different loss terms.

#### Relevance 446

Label: 

## Question 0050

Paper: GitHub Typo Corpus: A Large-Scale Multilingual Dataset of Misspellings and Grammatical Errors

> How did they identify what language the text was?

### Common Retrieved Chunks

#### Passage 447

Retrieved by: BM25, Dense, Hybrid RRF

> distributions of these computed statistics per category for English. We observed similar trends for other two languages (Chinese and Japanese), except for a slightly larger number of spell edits, mainly due to the non-Latin character conversion errors. We also confirmed that the difference of perplexities between the source and the target for typo edits (i.e., mechanical, spell, and grammatical edits) was statistically significant for all three languages (two-tailed t-test, $p < .01$). This means that these edits, on average, turn the source text into a more fluent text in the target.

#### Relevance 447

Label: 

#### Passage 449

Retrieved by: BM25, Dense, Hybrid RRF

> In this second phase of filtering, we identify all non-typo edits that are not intended to fix mechanical, spelling, or grammatical errors, but to modify the intended meaning between the source and the target.
> 
> In order to investigate the characteristics of such edits empirically, we first extracted 200 edits for each one of the three largest languages in the GitHub Typo Corpus: English (eng), Simplified Chinese (cmn-hans), and Japanese (jpn). We then had fluent speakers of each language go over the list and annotate each edit with the following four edit categories:
> 
> Mechanical ... a mechanical edit fixes errors in punctuation and capitalization.
> 
> Spell ... a spell edit fixes misspellings in words. This also includes conversion errors in non-Latin languages (e.g., Chinese and Japanese).
> 
> Grammatical ... a grammatical edit fixes grammatical errors in the source.
> 
> Semantic ... a semantic edit changes the intended meaning between the source and the target.
> 
> See Figure FIGREF27 for some examples of different edit types on each language. If one edit contains more than one type of changes, the least superficial category is assigned. For example, if there are both spell and grammatical changes in a single edit, the “grammatical” category is assigned to the edit. We note that the first three (mechanical, spell, and grammatical edits, also called typos) are within the scope of the dataset we build, while the last one (semantic edits) is not. Thus, our goal is to identify the last type of edits as accurately as possible in a scalable manner. We will show the statistics of the annotated data in Section 6.
> 
> We note that the distinction between different categories, especially between spell and grammatical, is not always obvious. For example, even if one mistypes a word “what” to “want” resulting in an ungrammatical sentence, we wouldn't consider this as a grammatical edit but as a spell edit. We clarify the difference by focusing on the process where the error is introduced in the first place. Conceptually, if one assumes that the source is generated by introducing errors to the target through a noisy channel model BIBREF18, BIBREF19, a spell edit is something where noise is introduced to some implicit character-generating process, while a

#### Relevance 449

Label: 

#### Passage 451

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Table TABREF41 shows the statistics of the GitHub Typo Corpus, broken down per language. The distribution of languages is heavily skewed towards English, although we observe the dataset includes a diverse set of other languages. There are 15 languages that have 100 or more edits in the dataset.
> 
> In addition to an obvious fact that a large fraction of the code on GitHub is written in English, one reason of the bias towards English may be due to our commit collection process, where we used an English keyword “typo” to harvest eligible commit. Although it is a norm on GitHub (and in software development in general) to write commit messages in English no matter what language you are working in, we may be able to collect a more diverse set of commits if we build models to filter through commit messages written in other languages, which is future work.

#### Relevance 451

Label: 

#### Passage 452

Retrieved by: Dense, Hybrid RRF

> Finally, after annotating a small amount of samples for the three languages, we computed some basic statistics about each edit that may help in classifying typo edits from non-typo ones. Specifically, we computed three statistics:
> 
> Ratio of the target perplexity over the source calculated by a language model
> 
> Normalized edit distance between the source and the target
> 
> Binary variable indicating whether the edit purely consists of changes in numbers
> 
> The rationale behind the third feature is that we observed that purely numerical changes always end up being tagged as semantic edits.
> 
> The perplexity of a text ${\mathbf {x}} = x_1 x_2, ..., x_L$ is defined by:
> 
> where $p(x)$ is determined by a trained language model. We hypothesize that perplexity captures the “fluency” of the input text to some degree, and by taking the ratio between the source and the target, the feature can represent the degree to which the fluency is improved before and after the edit.
> 
> As for the language model, we trained a character level Long Short Term Memory (LSTM) language model developed in BIBREF20 per language, which consists of a trainable embedding layer, three layers of a stacked recurrent neural network, and a softmax classifier. The LSTM hidden state and word embedding sizes are set to be 1000 and 200, respectively. We used 100,000 sentences from the W2C Web Corpus BIBREF21 for training (except for Chinese, where we used 28,000 sentences) and 1,000 sentences for validation for all the languages.
> 
> The normalized edit distance between the source $\mathbf {x} = x_1 x_2, ..., x_{L_x}$ and the target $\mathbf {y} = y_1 y_2, ..., y_{L_y}$ is defined by:
> 
> where $d({\mathbf {x}}, {\mathbf {y}})$ is the (unnormalized) edit distance between ${\mathbf {x}}$ and ${\mathbf {y}}$. This feature can capture the amount of the change made between the source and the target, based on our hypothesis that many typo edits only involve a small amount of changes.
> 
> See Figure FIGREF33 for an overview of the distributions of these computed statistics per category for English. We observed similar trends for other two languages (Chinese and Japanese), except for a slightly larger number of spell edits, mainly due to the non-Latin character conversion errors. We also confirmed

#### Relevance 452

Label: 

#### Passage 453

Retrieved by: Dense, Hybrid RRF

> Due to its nature, repositories on GitHub contain a large amount of code (in programming language) as well as natural language texts. We used NanigoNet, a language detector based on GCNNs (Gated Convolutional Neural Networks) BIBREF17 that supports human languages as well as programming languages. Specifically, we ran the language detector against both the source and the target and discarded all the edits where either is determined as written in a non-human language. We also discarded an edit if the detected language doesn't match between the source and the target. This left us with a total of 203,270 commits and 353,055 edits, which are all included in the final dataset.

#### Relevance 453

Label: 

### BM25

#### Passage 448

Retrieved by: BM25

> First, we define and clarify the terminology that we use throughout this paper. See Figure FIGREF3 for an illustration of the concepts and how they relate to each other.
> 
> Repository ... in git terms, a repository is a database of files whose versions are controlled under git. A single repository may contain multiple files and directories just like a computer file system.
> 
> Commit ... a commit is a collection of one or more changes made to a git repository at a time. Changes in a single commit can span over multiple files and multiple parts of a file.
> 
> Edit ... in this paper, an edit is a pair of lines to which changes are made in a commit (note the special usage here). The line before the change is called the source and the line after is the target. In other words, an edit is a pair of the source and the target. Note that a single edit may contain changes to multiple parts of the source (for example, multiple words that are not contiguous).
> 
> Typo ... finally, in this paper a typo refers to an edit where the target fixes some mechanical, spelling and/or grammatical errors in the source, while preserving the meaning between the two.
> 
> Our goal is to collect typos from GitHub and build a dataset that is high in both quantity and quality.

#### Relevance 448

Label: 

#### Passage 450

Retrieved by: BM25

> As mentioned above, a closely related line of work is the use of Wikipedia edits for various tasks, including GEC. Grundkiewicz:2014 constructed the WikiEd Error Corpus, a dataset consisting of error edits harvested from the Wikipedia edit history and demonstrated that the newly-built resource was effective for improving the performance of GEC systems. Boyd:2018 built a German GEC system leveraging the WikiEd Error Corpus and showed that the use of the Wikipedia edit data led to improved performance. In both cases, the dataset required extensive filtering based on a set of heuristic rules or heavy linguistic analysis.
> 
> Spelling correction is itself an important sub-problem of grammatical error correction (GEC). Many GEC and essay scoring systems BIBREF10, BIBREF11, BIBREF12 assume that spelling errors in the input text are fixed before it is fed to the main model, by pre-processing them using open-source tools such as Enchant and LanguageTool. In many GEC corpora, spelling errors account for approximately 10% of total errors (Table TABREF10), meaning that improving the accuracy of spelling correction can have a non-negligible impact on the performance of GEC.
> 
> Datasets of real-world typos have applications in building models robust to spelling errors BIBREF16. We note that Mizumoto:2017 argue against the necessity of spell checking on learner English, which has little effect on the performance of PoS (part-of-speech) tagging and chunking.

#### Relevance 450

Label: 

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 454

Retrieved by: Hybrid RRF followed by BGE reranking

> Spelling correction BIBREF0, BIBREF1, BIBREF2 and grammatical error correction (GEC) BIBREF3 are two fundamental tasks that have important implications for downstream NLP tasks and for education in general. In recent years, the use of statistical machine translation (SMT) and neural sequence-to-sequence (seq2seq) models has been becoming increasingly popular for solving these tasks. Such modern NLP models are usually data hungry and require a large amount of parallel training data consisting of sentences before and after the correction. However, only relatively small datasets are available for these tasks, compared to other NLP tasks such as machine translation. This is especially the case for spelling correction, for which only a small number of datasets consisting of individual misspelled words are available, including the Birkbeck spelling error corpus and a list of typos collected from Twitter.
> 
> Due to this lack of large-scale datasets, many research studies BIBREF4, BIBREF2, BIBREF5 resort to automatic generation of artificial errors (also called pseudo-errors). Although such methods are efficient and have seen some success, they do not guarantee that generated errors reflect the range and the distribution of true errors made by humans BIBREF6.
> 
> As one way to complement this lack of resources, Wikipedia has been utilized as a rich source of textual edits, including typos BIBREF7, BIBREF8, BIBREF9. However, the edits harvested from Wikipedia are often very noisy and diverse in their types, containing edits from typos to adding and modifying information. To make the matters worse, Wikipedia suffers from vandalism, where articles are edited in a malicious manner, which requires extensive detection and filtering.
> 
> In order to create a high-quality, large-scale dataset of misspelling and grammatical errors (collectively called typos in this paper), we leverage the data from GitHub, the largest platform for hosting and sharing repositories maintained by git, a popular version control system commonly used for software development. Changes made to git repositories (called commits, see Section 3 for the definition) are usually tagged with commit messages, making detection of typos a trivial task. Also, GitHub suffers less from vandalism, since commits in many repositories are code reviewed, a process where every change is manually reviewed by other team members before merged into the repository. This guarantees that the

#### Relevance 454

Label: 

#### Passage 455

Retrieved by: Hybrid RRF followed by BGE reranking

> first place. Conceptually, if one assumes that the source is generated by introducing errors to the target through a noisy channel model BIBREF18, BIBREF19, a spell edit is something where noise is introduced to some implicit character-generating process, while a grammatical edit is the one which corrupts some implicit grammatical process (for example, production rules of a context-free grammar).

#### Relevance 455

Label: 

#### Passage 456

Retrieved by: Hybrid RRF followed by BGE reranking

> In order to provide a more qualitative look into the dataset, we analyzed all the edits in the top three languages and extracted atomic edits. An atomic edit is defined as a sequence of contiguous characters that are inserted, deleted, or substituted between the source and the target. We extracted these atomic edits by aligning the characters between the source and the target by minimizing the edit distance, then by extracting contiguous edits that are insertion, deletion, or substitution.
> 
> As one can see from Figure FIGREF45, simple spelling edits such as inserting “s” and deleting “e” dominate the lists. In fact, many of the frequent atomic edits even in Chinese and Japanese are made against English words (see Figure FIGREF27 for examples—you notice many English words such as “GB-18030” and “Gemfile” in non-English text). You also notice a number of grammatical edits in Chinese (e.g., confusion between the possessive particle de and the adjectival particle de) and Japanese (e.g., omissions of case particles such as wo, no, and ni). This demonstrates that the dataset can serve as a rich source of not only spelling but also naturally-occurring grammatical errors.

#### Relevance 456

Label: 

#### Passage 457

Retrieved by: Hybrid RRF followed by BGE reranking

> of typos a trivial task. Also, GitHub suffers less from vandalism, since commits in many repositories are code reviewed, a process where every change is manually reviewed by other team members before merged into the repository. This guarantees that the edits indeed fix existing spelling and/or grammatical issues.
> 
> This paper describes our process for building the GitHub Typo Corpus, a large-scale, multilingual dataset of misspellings and grammatical errors, along with their corrections. The process for building the dataset can be summarized as follows:
> 
> Extract eligible repositories and typo commits from GitHub based on the meta data of the repository and the commit message
> 
> Filter out edits that are not written in human language
> 
> Identify true typo edits (vs semantic edits) by using learned classifiers on a small annotated dataset
> 
> We demonstrate that a very simple logistic regression model with only three features can classify typos and non-typo edits correctly with $F1 \sim 0.9$. This resulted in a dataset containing more than 350k edits and 64M characters in more than 15 languages. To the best of our knowledge, this is the largest multilingual dataset of misspellings to date. We made the dataset publicly available (https://github.com/mhagiwara/github-typo-corpus) along with the automatically assigned typo labels as well as the source code to extract typos. We also provide the detailed analyses of the dataset, where we demonstrate that the F measure of existing spell checkers merely reaches $\sim 0.5$, arguing that the GitHub Typo Corpus provides a new, rich source of naturally-occurring misspellings and grammatical errors that complement existing datasets.

#### Relevance 457

Label: 

## Question 0051

Paper: Quasi-Recurrent Neural Networks

> What sentiment classification dataset is used?

### Common Retrieved Chunks

#### Passage 458

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We evaluate the QRNN architecture on a popular document-level sentiment classification benchmark, the IMDb movie review dataset BIBREF17 . The dataset consists of a balanced sample of 25,000 positive and 25,000 negative reviews, divided into equal-size train and test sets, with an average document length of 231 words BIBREF18 . We compare only to other results that do not make use of additional unlabeled data (thus excluding e.g., BIBREF19 ).
> 
> Our best performance on a held-out development set was achieved using a four-layer densely-connected QRNN with 256 units per layer and word vectors initialized using 300-dimensional cased GloVe embeddings BIBREF20 . Dropout of 0.3 was applied between layers, and we used INLINEFORM0 regularization of INLINEFORM1 . Optimization was performed on minibatches of 24 examples using RMSprop BIBREF21 with learning rate of INLINEFORM2 , INLINEFORM3 , and INLINEFORM4 .
> 
> Small batch sizes and long sequence lengths provide an ideal situation for demonstrating the QRNN's performance advantages over traditional recurrent architectures. We observed a speedup of 3.2x on IMDb train time per epoch compared to the optimized LSTM implementation provided in NVIDIA's cuDNN library. For specific batch sizes and sequence lengths, a 16x speed gain is possible. Figure FIGREF15 provides extensive speed comparisons.
> 
> In Figure FIGREF12 , we visualize the hidden state vectors INLINEFORM0 of the final QRNN layer on part of an example from the IMDb dataset. Even without any post-processing, changes in the hidden state are visible and interpretable in regards to the input. This is a consequence of the elementwise nature of the recurrent pooling function, which delays direct interaction between different channels of the hidden state until the computation of the next QRNN layer.

#### Relevance 458

Label: 

#### Passage 459

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We evaluate the performance of the QRNN on three different natural language tasks: document-level sentiment classification, language modeling, and character-based neural machine translation. Our QRNN models outperform LSTM-based models of equal hidden size on all three tasks while dramatically improving computation speed. Experiments were implemented in Chainer BIBREF16 .

#### Relevance 459

Label: 

#### Passage 460

Retrieved by: BM25, Dense, Hybrid RRF

> We replicate the language modeling experiment of BIBREF2 and BIBREF13 to benchmark the QRNN architecture for natural language sequence prediction. The experiment uses a standard preprocessed version of the Penn Treebank (PTB) by BIBREF25 .
> 
> We implemented a gated QRNN model with medium hidden size: 2 layers with 640 units in each layer. Both QRNN layers use a convolutional filter width INLINEFORM0 of two timesteps. While the “medium” models used in other work BIBREF2 , BIBREF13 consist of 650 units in each layer, it was more computationally convenient to use a multiple of 32. As the Penn Treebank is a relatively small dataset, preventing overfitting is of considerable importance and a major focus of recent research. It is not obvious in advance which of the many RNN regularization schemes would perform well when applied to the QRNN. Our tests showed encouraging results from zoneout applied to the QRNN's recurrent pooling layer, implemented as described in Section SECREF5 .
> 
> The experimental settings largely followed the “medium” setup of BIBREF2 . Optimization was performed by stochastic gradient descent (SGD) without momentum. The learning rate was set at 1 for six epochs, then decayed by 0.95 for each subsequent epoch, for a total of 72 epochs. We additionally used INLINEFORM0 regularization of INLINEFORM1 and rescaled gradients with norm above 10. Zoneout was applied by performing dropout with ratio 0.1 on the forget gates of the QRNN, without rescaling the output of the dropout function. Batches consist of 20 examples, each 105 timesteps.
> 
> Comparing our results on the gated QRNN with zoneout to the results of LSTMs with both ordinary and variational dropout in Table TABREF14 , we see that the QRNN is highly competitive. The QRNN without zoneout strongly outperforms both our medium LSTM and the medium LSTM of BIBREF2 which do not use recurrent dropout and is even competitive with variational LSTMs. This may be due to the limited computational capacity that the QRNN's pooling layer has relative to the LSTM's recurrent weights, providing structural regularization over the recurrence.
> 
> Without zoneout, early stopping based upon validation loss was required as the QRNN would begin overfitting. By applying a small amount of zoneout ( INLINEFORM0 ), no early

#### Relevance 460

Label: 

#### Passage 461

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> relative to the LSTM's recurrent weights, providing structural regularization over the recurrence.
> 
> Without zoneout, early stopping based upon validation loss was required as the QRNN would begin overfitting. By applying a small amount of zoneout ( INLINEFORM0 ), no early stopping is required and the QRNN achieves competitive levels of perplexity to the variational LSTM of BIBREF13 , which had variational inference based dropout of 0.2 applied recurrently. Their best performing variation also used Monte Carlo (MC) dropout averaging at test time of 1000 different masks, making it computationally more expensive to run.
> 
> When training on the PTB dataset with an NVIDIA K40 GPU, we found that the QRNN is substantially faster than a standard LSTM, even when comparing against the optimized cuDNN LSTM. In Figure FIGREF15 we provide a breakdown of the time taken for Chainer's default LSTM, the cuDNN LSTM, and QRNN to perform a full forward and backward pass on a single batch during training of the RNN LM on PTB. For both LSTM implementations, running time was dominated by the RNN computations, even with the highly optimized cuDNN implementation. For the QRNN implementation, however, the “RNN” layers are no longer the bottleneck. Indeed, there are diminishing returns from further optimization of the QRNN itself as the softmax and optimization overhead take equal or greater time. Note that the softmax, over a vocabulary size of only 10,000 words, is relatively small; for tasks with larger vocabularies, the softmax would likely dominate computation time.
> 
> It is also important to note that the cuDNN library's RNN primitives do not natively support any form of recurrent dropout. That is, running an LSTM that uses a state-of-the-art regularization scheme at cuDNN-like speeds would likely require an entirely custom kernel.

#### Relevance 461

Label: 

#### Passage 462

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Recurrent neural networks (RNNs), including gated variants such as the long short-term memory (LSTM) BIBREF0 have become the standard model architecture for deep learning approaches to sequence modeling tasks. RNNs repeatedly apply a function with trainable parameters to a hidden state. Recurrent layers can also be stacked, increasing network depth, representational power and often accuracy. RNN applications in the natural language domain range from sentence classification BIBREF1 to word- and character-level language modeling BIBREF2 . RNNs are also commonly the basic building block for more complex models for tasks such as machine translation BIBREF3 , BIBREF4 , BIBREF5 or question answering BIBREF6 , BIBREF7 . Unfortunately standard RNNs, including LSTMs, are limited in their capability to handle tasks involving very long sequences, such as document classification or character-level machine translation, as the computation of features or states for different parts of the document cannot occur in parallel.
> 
> Convolutional neural networks (CNNs) BIBREF8 , though more popular on tasks involving image data, have also been applied to sequence encoding tasks BIBREF9 . Such models apply time-invariant filter functions in parallel to windows along the input sequence. CNNs possess several advantages over recurrent models, including increased parallelism and better scaling to long sequences such as those often seen with character-level language data. Convolutional models for sequence processing have been more successful when combined with RNN layers in a hybrid architecture BIBREF10 , because traditional max- and average-pooling approaches to combining convolutional features across timesteps assume time invariance and hence cannot make full use of large-scale sequence order information.
> 
> We present quasi-recurrent neural networks for neural sequence modeling. QRNNs address both drawbacks of standard models: like CNNs, QRNNs allow for parallel computation across both timestep and minibatch dimensions, enabling high throughput and good scaling to long sequences. Like RNNs, QRNNs allow the output to depend on the overall order of elements in the sequence. We describe QRNN variants tailored to several natural language tasks, including document-level sentiment classification, language modeling, and character-level machine translation. These models outperform strong LSTM baselines on all three tasks while dramatically reducing computation time.

#### Relevance 462

Label: 

#### Passage 463

Retrieved by: Dense, Hybrid RRF

> Exploring alternatives to traditional RNNs for sequence tasks is a major area of current research. Quasi-recurrent neural networks are related to several such recently described models, especially the strongly-typed recurrent neural networks (T-RNN) introduced by BIBREF12 . While the motivation and constraints described in that work are different, BIBREF12 's concepts of “learnware” and “firmware” parallel our discussion of convolution-like and pooling-like subcomponents. As the use of a fully connected layer for recurrent connections violates the constraint of “strong typing”, all strongly-typed RNN architectures (including the T-RNN, T-GRU, and T-LSTM) are also quasi-recurrent. However, some QRNN models (including those with attention or skip-connections) are not “strongly typed”. In particular, a T-RNN differs from a QRNN as described in this paper with filter size 1 and f-pooling only in the absence of an activation function on INLINEFORM0 . Similarly, T-GRUs and T-LSTMs differ from QRNNs with filter size 2 and fo- or ifo-pooling respectively in that they lack INLINEFORM1 on INLINEFORM2 and use INLINEFORM3 rather than sigmoid on INLINEFORM4 .
> 
> The QRNN is also related to work in hybrid convolutional–recurrent models. BIBREF31 apply CNNs at the word level to generate INLINEFORM0 -gram features used by an LSTM for text classification. BIBREF32 also tackle text classification by applying convolutions at the character level, with a stride to reduce sequence length, then feeding these features into a bidirectional LSTM. A similar approach was taken by BIBREF10 for character-level machine translation. Their model's encoder uses a convolutional layer followed by max-pooling to reduce sequence length, a four-layer highway network, and a bidirectional GRU. The parallelism of the convolutional, pooling, and highway layers allows training speed comparable to subword-level models without hard-coded text segmentation.
> 
> The QRNN encoder–decoder model shares the favorable parallelism and path-length properties exhibited by the ByteNet BIBREF33 , an architecture for character-level machine translation based on residual convolutions over binary trees. Their model was constructed to achieve three desired properties: parallelism, linear-time computational complexity, and short paths between any pair of words in order to better propagate gradient signals.

#### Relevance 463

Label: 

### BM25

None

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 464

Retrieved by: Hybrid RRF followed by BGE reranking

> We evaluate the sequence-to-sequence QRNN architecture described in SECREF5 on a challenging neural machine translation task, IWSLT German–English spoken-domain translation, applying fully character-level segmentation. This dataset consists of 209,772 sentence pairs of parallel training data from transcribed TED and TEDx presentations, with a mean sentence length of 103 characters for German and 93 for English. We remove training sentences with more than 300 characters in English or German, and use a unified vocabulary of 187 Unicode code points.
> 
> Our best performance on a development set (TED.tst2013) was achieved using a four-layer encoder–decoder QRNN with 320 units per layer, no dropout or INLINEFORM0 regularization, and gradient rescaling to a maximum magnitude of 5. Inputs were supplied to the encoder reversed, while the encoder convolutions were not masked. The first encoder layer used convolutional filter width INLINEFORM1 , while the other encoder layers used INLINEFORM2 . Optimization was performed for 10 epochs on minibatches of 16 examples using Adam BIBREF28 with INLINEFORM3 , INLINEFORM4 , INLINEFORM5 , and INLINEFORM6 . Decoding was performed using beam search with beam width 8 and length normalization INLINEFORM7 . The modified log-probability ranking criterion is provided in the appendix.
> 
> Results using this architecture were compared to an equal-sized four-layer encoder–decoder LSTM with attention, applying dropout of 0.2. We again optimized using Adam; other hyperparameters were equal to their values for the QRNN and the same beam search procedure was applied. Table TABREF17 shows that the QRNN outperformed the character-level LSTM, almost matching the performance of a word-level attentional baseline.

#### Relevance 464

Label: 

## Question 0052

Paper: Human-like machine thinking: Language guided imagination

> How do the authors measure the extent to which LGI has learned the task?

### Common Retrieved Chunks

#### Passage 465

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The first syntaxes that LGI has learned are the ‘move left’ and ‘move right’ random pixels, with the corresponding results shown in Figure 3. After 50000 steps training, LGI could not only reconstruct the input image with high precision but also predict the 'mentally' moved object with specified morphology, correct manipulated direction and position just after the command sentence completed. The predicted text can complete the word ‘move’ given the first letter ‘m’ (till now, LGI has only learned syntaxes of ‘move left or right’). LGI tried to predict the second word ‘right’ with initial letter ‘r’, however, after knowing the command text is ‘l’, it turned to complete the following symbols with ‘eft’. It doesn’t care if the sentence length is 12 or 11, the predicted image and text just came at proper time and position. Even if the command asked to move out of screen, LGI still could reconstruct the partially occluded image with high fidelity.
> 
> Based on the same network, LGI continued to learn syntax ‘this is …’. Just like a parent teaching child numbers by pointing to number instances, Figure 4 demonstrates that, after training of 50000 steps, LGI could classify figures in various morphology with correct identity (accuracy = 72.7%). Note that, the classification process is not performed by softmax operation, but by directly textizing operation (i.e. rounding followed by a symbol mapping operation), which is more biologically plausible than the softmax operation.
> 
> After that, LGI learned the syntax ‘the size is big/small’, followed by ‘the size is not small/big’. Figure 5 illustrates that LGI could correctly categorize whether the digit size was small or big with proper text output. And we witness that, based on the syntax of ‘the size is big/small’ (train steps =1000), the negative adverb ‘not’ in the language text ‘the size is not small/big’ was much easier to be learned (train steps =200, with same hyper-parameters). This is quite similar to the cumulative learning process of the human being.
> 
> And then, LGI rapidly learned three more syntaxes: ‘give me a …’, ‘enlarge/shrink’, and ‘rotate …’, whose results are shown in Figure 6. After training (5000 steps), LGI could generate a correct digit figure given the

#### Relevance 465

Label: 

#### Passage 467

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> of the human being.
> 
> And then, LGI rapidly learned three more syntaxes: ‘give me a …’, ‘enlarge/shrink’, and ‘rotate …’, whose results are shown in Figure 6. After training (5000 steps), LGI could generate a correct digit figure given the language command ‘give me a [number]’ (Figure 6.A). The generated digit instance is somewhat the ‘averaged’ version of all training examples of the same digit identity. In the future, the generative adversarial network (GAN) technique could be included to generate object instances with specific details. However, using more specific language, such as ‘give me a red Arial big 9’ to generate the characterized instance can better resemble the human thinking process than GAN. LGI can also learn to change the size and orientation of an imagined object. Figure 6.B-C illustrates the morphology of the final imagined instance could be kept unchanged after experiencing various manipulations. Some other syntaxes or tasks could be integrated into LGI in a similar way.
> 
> Finally, in Figure 7, we illustrate how LGI performed the human-like language-guided thinking process, with the above-learned syntaxes. (1) LGI first closed its eyes, namely, that no input images were fed into the vision subsystem (all the subsequent input images were generated through the imagination process). (2) LGI said to itself ‘give me a 9’, then the PFC produced the corresponding encoding vector INLINEFORM0 , and finally one digit ‘9’ instance was reconstructed via the imagination network. (3) LGI gave the command ‘rotate 180’, then the imagined digit ‘9’ was rotated upside down. (4) Following the language command ‘this is ’, LGI automatically predicted that the newly imaged object was the digit ‘6’. (5) LGI used ‘enlarge’ command to make the object bigger. (6) Finally, LGI predicted that the size was ‘big’ according to the imagined object morphology. This demonstrates that LGI can understand the verbs and nouns by properly manipulating the imagination, and can form the iterative thinking process via the interaction between vision and language subsystems through the PFC layer. The human thinking process normally would not form a concrete imagination through the full visual loop, but rather a vague and rapid imagination through the short-cut loop by feeding back INLINEFORM1 to AIT directly.

#### Relevance 467

Label: 

#### Passage 470

Retrieved by: Dense, Hybrid RRF

> rule conveyed by language, we can quickly start a game with proper moves using a try-in-imagination strategy without requiring even a single practice. With imagination, people can change the answering contents (or even tell good-will lies) by considering or imagining the consequence of the next few output sentences. Machine equipped with the unique ability of imagination could easily select clever actions for multiple tasks without being trained heavily.
> 
> In the future, many more syntaxes and functionalities can be added to LGI in a similar way, such as math reasoning, intuitive physics prediction and navigation [24, 25, 26]. Insights of human audition processing could be leveraged to convert sound wave into language text as a direct input for LGI [27, 28]. And the mechanisms of human value systems in the striatum [29] may also endow LGI with motivation and emotion. The PFC cortex consists of many sub-regions interacted within the PFC and across the whole brain areas [3, 30], and the implementation of these features might finally enable LGI to possess real machine intelligence.

#### Relevance 470

Label: 

#### Passage 471

Retrieved by: Dense, Hybrid RRF

> In this paper, we first introduced a PFC layer to involve representations from both language and vision subsystems to form a human-like thinking system (the LGI system). The LGI contains three subsystems: the vision, language, and PFC subsystem, which are trained separately. The development, recognition and learning mechanism is discussed in the cocurrent paper [10]. In the language subsystem, we use an LSTM layer to mimic the human IPS to extract the quantity information from language text and proposed a biologically plausible textizer to produce text symbols output, instead of traditional softmax classifier. We propose to train the LGI with the NFP loss function, which endows the capacity to describe the image content in form of symbol text and manipulated images according to language commands. LGI shows its ability to learn eight different syntaxes or tasks in a cumulative learning way, and form the first machine thinking loop with the interaction between imagined pictures and language text.

#### Relevance 471

Label: 

### BM25

#### Passage 466

Retrieved by: BM25

> an example [17], during training, the autoencoder learns the 3D characteristics of a car with a pair of images from two views of the same car together with the viewpoint of the output view. During testing, the autoencoder could predict the desired image from a single image of the car given the expected viewpoint. However, this architecture is task-specific, namely that the network can only make predictions on cars' unseen views. To include multiple tasks, we added an additional PFC layer that can receive task commands conveyed via language stream and object representation via the visual encoder pathway, and output the modulated images according to task commands and the desired text prediction associated with the images. In addition, by transmitting the output image from the decoder to the encoder, an imagination loop is formed, which enables the continual operation of a human-like thinking process involving both language and image.

#### Relevance 466

Label: 

#### Passage 468

Retrieved by: BM25

> Our goal is to build a human-like neural network by removing components unsupported by neuroscience from AI architecture while introducing novel neural mechanisms and algorithms into it. Taking the convolution neural network (CNN) as an example, although it has reached human-level performance in image recognition tasks [6], animal neural systems do not support such kernel scanning operation across retinal neurons, and thus the neuronal responses measured on monkeys do not match that of CNN units [7,8]. Therefore, instead of CNN, we used fully connected (FC) module [9] to build our neural network, which achieved more resemblance to animal neurophysiology in term of the network development, neuronal firing patterns, object recognition mechanism, learning and forgetting mechanisms, as illustrated in our concurrent submission [10]. In addition, the error backpropagation technique is generally used to modify network weights to learn representation and achieve training objectives [11]. However, in neuroscience, it is the activity-dependent molecular events (e.g. the inflow of calcium ion and the switching of glutamate N-methyl-D-aspartate receptor etc.) that modify synaptic connections [12, 13]. Indeed, the real neural feedback connection provides the top-down imagery information [14], which is usually ignored by AI network constructions due to the concept of error backpropagation. What’s more, our concurrent paper [10] demonstrates that the invariance property of visual recognition under the rotation, scaling, and translation of an object is supported by coordinated population coding rather than the max-pooling mechanism [15]. The softmax classification is usually used to compute the probability of each category (or word) in the repository (or vocabulary) before prediction. However, in reality, we never evaluate all fruit categories in mind before saying ‘it is an apple’, let alone the complicated computation of the normalization term in the softmax. In this paper, we demonstrate object classification is directly output by neurons via a simple rounding operation, rather than the neuroscience unsupported softmax classification [16].
> 
> Modern autoencoder techniques could synthesize an unseen view for the desired viewpoint. Using car as an example [17], during training, the autoencoder learns the 3D characteristics of a car with a pair of images from two views of the same car together with the viewpoint of the output view. During testing, the autoencoder could predict

#### Relevance 468

Label: 

#### Passage 469

Retrieved by: BM25

> no neuroscience foundation.
> 
> The PFC subsystem contains a LSTM and a full connected layer. It receives inputs from both language and vision subsystems in a concatenated form of INLINEFORM0 at time t, and gives a prediction output INLINEFORM1 , which is expected to be identical to INLINEFORM2 at time t+1. This has been achieved with a next frame prediction (NFP) loss function as, INLINEFORM3 . So given an input image, the PFC can predict the corresponding text description; while given an input text command the PFC can predict the corresponding manipulated image. This NFP loss function has neuroscience foundation, since the molecular mediated synaptic plasticity always takes place after the completion of an event, when the information of both t and t+1 time points have been acquired and presented by the neural system. The strategy of learning by predicting its own next frame is essentially an unsupervised learning.
> 
> For human brain development, the visual and auditory systems mature in much earlier stages than the PFC [19]. To mimic this process, our PFC subsystem was trained separately after vision and language components had completed their functionalities. We have trained the network to accumulatively learn eight syntaxes, and the related results are shown in the following section. Finally, we demonstrate how the network forms a thinking loop with text language and imagined pictures.

#### Relevance 469

Label: 

### Dense

#### Passage 472

Retrieved by: Dense

> Human thinking is regarded as ‘mental ideas flow guided by language to achieve a goal’. For instance, after seeing heavy rain, you may say internally ‘holding an umbrella could avoid getting wet’, and then you will take an umbrella before leaving. In the process, we know that the visual input of ‘water drop’ is called rain, and can imagine ‘holding an umbrella’ could keep off the rain, and can even experience the feeling of being wet. This continual thinking capacity distinguishes us from the machine, even though the latter can also recognize images, process language, and sense rain-drops. Continual thinking requires the capacity to generate mental imagination guided by language, and extract language representations from a real or imagined scenario.
> 
> Modern natural language processing (NLP) techniques can handle question answering etc. tasks, such as answering that ‘Cao Cao’s nickname is Meng De’ based on the website knowledge [1]. However, the NLP network is just a probability model [2] and does not know whether Cao Cao is a man or cat. Indeed, it even does not understand what is a man. On the other hand, human being learns Cao Cao with his nickname via watching TV. When presented the question ‘what’s Cao Cao’s nickname?’, we can give the correct answer of ‘Meng De’ while imagining the figure of an actor in the brain. In this way, we say the machine network does not understand it, but the human does.
> 
> Human beings possess such thinking capacity due to its cumulative learning capacity accompanying the neural developmental process. Initially, parent points to a real apple and teaches the baby ‘this is an apple’. After gradually assimilating the basic meanings of numerous nouns, children begin to learn some phrases and finally complicated syntaxes. Unlike the cumulative learning, most NLP techniques normally choose to learn by reading and predicting target words. After consuming billions of words in corpus materials [2], the NLP network can predict ‘Trump’ following ‘Donald’, but it is merely a probability machine.
> 
> The human-like thinking system often requires specific neural substrates to support the corresponding functionalities. The most important brain area related to thinking is the prefrontal cortex (PFC), where the working memory takes place, including but

#### Relevance 472

Label: 

### Hybrid RRF

#### Passage 473

Retrieved by: Hybrid RRF

> Language guided imagination is the nature of human thinking and intelligence. Normally, the real-time tasks or goals are conveyed by language, such as ‘to build a Lego car’. To achieve this goal, first, an agent (human being or machine) needs to know what’s car, and then imagine a vague car instance, based on which the agent can plan to later collect wheel, window and chassis blocks for construction. Imagining the vague car is the foundation for decomposing future tasks. We trained the LGI network with a human-like cumulative learning process, from learning the meaning of words, to understanding complicated syntaxes, and finally organizing the thinking process with language. We trained the LGI to associate object name with corresponding instances by ‘this is …’ syntax; and trained the LGI to produce a digit instance, when there comes the sentence ‘give me a [number]’. In contrast, traditional language models could only serve as a word dependency predictor rather than really understand the sentence.
> 
> Language is the most remarkable characteristics distinguishing mankind from animals. Theoretically, all kinds of information such as object properties, tasks and goals, commands and even emotions can be described and conveyed by language [21]. We trained with LGI eight different syntaxes (in other word, eight different tasks), and LGI demonstrates its understanding by correctly interacting with the vision system. After learning ‘this is 9’, it is much easier to learn ‘give me a 9’; after learning the ‘size is big’, it is much easier to learn ‘the size is not small’. Maybe some digested words or syntaxes were represented by certain PFC units, which could be shared with the following sentence learning.
> 
> Imagination is another key component of human thinking. For the game Go [22, 23], the network using a reinforcement learning strategy has to be trained with billions of games in order to acquire a feeling (Q value estimated for each potential action) to move the chess. As human beings, after knowing the rule conveyed by language, we can quickly start a game with proper moves using a try-in-imagination strategy without requiring even a single practice. With imagination, people can change the answering contents (or even tell good-will lies) by considering or imagining

#### Relevance 473

Label: 

### Hybrid RRF followed by BGE reranking

#### Passage 474

Retrieved by: Hybrid RRF followed by BGE reranking

> 19(10), 590-602.
> 
> [15] Boureau, Y. L., Ponce, J. & LeCun, Y. (2010). A theoretical analysis of feature pooling in visual recognition. In Proceedings of the 27th international conference on machine learning (ICML-10) (pp. 111-118).
> 
> [16] LeCun, Y., Bengio, Y. & Hinton, G. (2015). Deep learning. Nature, 521(7553), 436.
> 
> [17] Zhou, T., Brown, M., Snavely, N. & Lowe, D. G. (2017). Unsupervised learning of depth and ego-motion from video. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (pp. 1851-1858).
> 
> [18] Ralph, M. A. L., Jefferies, E., Patterson, K. & Rogers, T. T. (2017). The neural and computational bases of semantic cognition. Nature Reviews Neuroscience, 18(1), 42.
> 
> [19] Petanjek, Z., Judaš, M., Kostović, I. & Uylings, H. B. (2007). Lifespan alterations of basal dendritic trees of pyramidal neurons in the human prefrontal cortex: a layer-specific pattern. Cerebral cortex, 18(4), 915-929.
> 
> [20] Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S. & Bengio, Y. (2014). Generative adversarial nets. In Advances in neural information processing systems (pp. 2672-2680).
> 
> [21] Wittgenstein, L. (2013). Tractatus logico-philosophicus.
> 
> [22] Silver, D., Huang, A., Maddison, C. J., Guez, A., Sifre, L., Van Den Driessche, G., & Dieleman, S. (2016). Mastering the game of Go with deep neural networks and tree search. Nature, 529(7587), 484.
> 
> [23] Silver, D., Schrittwieser, J., Simonyan, K., Antonoglou, I., Huang, A., Guez, A. & Chen, Y. (2017). Mastering the game of go without human knowledge. Nature, 550(7676), 354.
> 
> [24] Saxton, D., Grefenstette, E., Hill, F. & Kohli, P. (2019). Analysing Mathematical Reasoning Abilities of Neural Models. arXiv preprint arXiv:1904.01557.
> 
> [25] Battaglia, P., Pascanu, R., Lai, M. & Rezende, D. J. (2016). Interaction networks for learning about objects, relations and physics. In Advances in neural information processing systems (pp. 4502-4510).
> 
> [26] Banino, A., Barry, C., Uria, B., Blundell, C., Lillicrap, T., Mirowski, P. & Wayne, G. (2018). Vector-based navigation using grid-like representations in artificial agents. Nature, 557(7705), 429.
> 
> [27] Jasmin, K., Lima, C. F. & Scott, S. K. (2019). Understanding rostral–caudal auditory cortex contributions to auditory perception. Nature Reviews Neuroscience, in press.
> 
> [28] Afouras, T., Chung, J. S. & Zisserman, A. (2018). The conversation: Deep audio-visual speech enhancement. arXiv preprint arXiv:1804.04121.
> 
> [29] Husain, M.

#### Relevance 474

Label: 

#### Passage 475

Retrieved by: Hybrid RRF followed by BGE reranking

> is merely a probability machine.
> 
> The human-like thinking system often requires specific neural substrates to support the corresponding functionalities. The most important brain area related to thinking is the prefrontal cortex (PFC), where the working memory takes place, including but not confined to, the maintenance and manipulation of particular information [3]. With the PFC, human beings can analyze and execute various tasks via ‘phonological loop’ and ‘visuospatial scratchpad’ etc. [4,5]. Inspired by the human-like brain organization, we build a ‘PFC’ network to combine language and vision streams to achieve tasks such as language controlled imagination, and imagination based thinking process. Our results show that the LGI network could incrementally learn eight syntaxes rapidly. Based on the LGI, we present the first language guided continual thinking process, which shows considerable promise for the human-like strong machine intelligence.

#### Relevance 475

Label: 

#### Passage 476

Retrieved by: Hybrid RRF followed by BGE reranking

> As is shown in Figure 1, the LGI network contains three main subsystems including the vision, language and PFC subsystems. The vision autoencoder network was trained separately, whose characteristics of development, recognition, learning, and forgetting can be referred to [10]. After training, the autoencoder is separated into two parts: the encoder (or recognition) part ranges from the image entry point to the final encoding layer, which functions as human anterior inferior temporal lobe (AIT) to provide the high-level abstract representation of the input image [18]; the decoder (or imagination) part ranges from the AIT to image prediction point. The activity vectors of the third encoding layer INLINEFORM0 and AIT layer INLINEFORM1 are concatenated with language activity vectors INLINEFORM2 as input signals to the PFC. We expect, after acquiring the language command, the PFC could output a desired visual activation vector INLINEFORM3 , based on which the imagination network could reconstruct the predicted image. Finally, the predicted or imagined image is fed back to the encoder network for the next thinking iteration.
> 
> The language processing component first binarizes the input text symbol-wise into a sequence of binary vectors INLINEFORM0 , where T is the text length. To improve the language command recognition, we added one LSTM layer to extract the quantity information of the text (for example, suppose text = ‘move left 12’, the expected output INLINEFORM1 is 1 dimensional quantity 12 at the last time point). This layer mimics the number processing functionality of human Intra-Parietal Sulcus (IPS), so it is given the name IPS layer. The PFC outputs the desired activation of INLINEFORM2 , which can either be decoded by the ‘texitizer’ into predicted text or serve as INLINEFORM3 for the next iteration of the imagination process. Here, we propose a textizer (a rounding operation, followed by symbol mapping from binary vector, whose detailed discussion can be referred to the Supplementary section A) to classify the predicted symbol instead of softmax operation which has no neuroscience foundation.
> 
> The PFC subsystem contains a LSTM and a full connected layer. It receives inputs from both language and vision subsystems in a concatenated form of INLINEFORM0 at time t, and gives a prediction output INLINEFORM1 , which

#### Relevance 476

Label: 

## Question 0053

Paper: Subword ELMo

> How long is the vocabulary of subwords?

### Common Retrieved Chunks

#### Passage 477

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The overall architecture of our subword-aware language model shows in Figure FIGREF1. It consists of four parts, word segmentation, word-level CNN, highway network and sentence-level RNN.
> 
> Given a sentence $S = \lbrace W_1, W_2, ... , W_n\rbrace $, we first use a segmentation algorithm to divide each word into a sequence of subwords BIBREF13, BIBREF14.
> 
> where $M_i$ is the output of the segmentation algorithm, $x_{i, j}$ is the subword unit and $f$ represents the segmentation algorithm. Then a look-up table is applied to transform the subword sequence into subword embeddings BIBREF15.
> 
> To further augment the word representation from the subwords, we apply a narrow convolution between subword embeddings and several kernels.
> 
> where $Concat$ is the concatenation operation for all the input vectors, $\mathbf {K}_i$ is convolution kernel and $g$ is CNN-MaxPooling operation.
> 
> A highway network BIBREF16 is then applied to the output of CNN. A bidirectional long short-term memory network (Bi-LSTM) BIBREF17 generates the hidden states for the given sentence representation in forward and backward. Finally, the probability of each token is calculated by applying an affine transformation to all the hidden states followed by a $SoftMax$ function. During the training, our objective is to minimize the negative log-likelihood of all training samples.
> 
> To apply our pre-trained language models to other NLP tasks, we combine the input vector and the last layer's hidden state of the Bi-LSTM to represent each word.

#### Relevance 477

Label: 

#### Passage 478

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Recently, pre-trained language representation has shown to be useful for improving many NLP tasks BIBREF0, BIBREF1, BIBREF2, BIBREF3. Embeddings from Language Models (ELMo) BIBREF0 is one of the most outstanding works, which uses a character-aware language model to augment word representation.
> 
> An essential challenge in training word-based language models is how to control vocabulary size for better rare word representation. No matter how large the vocabulary is, rare words are always insufficiently trained. Besides, an extensive vocabulary takes too much time and computational resource for the model to converge. Whereas, if the vocabulary is too small, the out-of-vocabulary (OOV) issue will harm the model performance heavily BIBREF4. To obtain effective word representation, BIBREF4 introduce character-driven word embedding using convolutional neural network (CNN) BIBREF5, following the language model in BIBREF6 for deep contextual representation.
> 
> However, there is potential insufficiency when modeling word from characters which hold little linguistic sense, especially, the morphological source BIBREF7. Only 86 characters(also included some common punctuations) are adopted in English writing, making the input too coarse for embedding learning. As we argue that for better representation from a refined granularity, word is too large and character is too small, it is natural for us to consider subword unit between character and word levels.
> 
> Splitting a word into subwords and using them to augment the word representation may recover the latent syntactic or semantic information BIBREF8. For example, uselessness could be split into the following subwords: $<$use, less, ness$>$. Previous work usually considers linguistic knowledge-based methods to tokenize each word into subwords (namely, morphemes) BIBREF9, BIBREF10, BIBREF11. However, such treatment may encounter three main inconveniences. First, the subwords from linguistic knowledge, typically including the morphological suffix, prefix, and stem, may not be suitable for a targeted NLP task BIBREF12 or mislead the representation of some words, like the meaning of understand cannot be formed by under and stand. Second, linguistic knowledge, including related annotated lexicons or corpora, may not even be available for a specific low-resource language. Due to these limitations, we focus on computationally motivated subword tokenization approaches in this work.
> 
> In this paper, we propose Embedding from Subword-aware Language Models (ESuLMo), which takes subword as input to augment word representation

#### Relevance 478

Label: 

#### Passage 479

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> To segment subwords from a word, we adopt the generalized unsupervised segmentation framework proposed by BIBREF18. The generalized framework can be divided into two collocative parts, goodness measure (score), which evaluates how likely a subword is to be a ‘proper’ one, and a segmentation or decoding algorithm. For the sake of simplicity, we choose frequency as the goodness score and two representative decoding algorithms, byte pair encoding (BPE) BIBREF13 which uses a greedy decoding algorithm and unigram language model (ULM) BIBREF14 which adopts a Viterbi-style decoding algorithm.
> 
> For a group of character sequences, the working procedure of BPE is as follows:
> 
> $\bullet $ All the input sequences are tokenized into a sequence of single-character subwords.
> 
> $\bullet $ Repeatedly, we calculate the frequencies of all bigrams and merge the bigram with the highest one until we get the desired subword vocabulary.
> 
> ULM is proposed based on the assumption that each subword occurs independently. The working procedure of ULM segmentation is as follows.
> 
> $\bullet $ Heuristically make a reasonably large seed vocabulary from the training corpus.
> 
> $\bullet $ Iteratively, the probability of each subword is estimated by the expectation maximization (EM) algorithm and the top $\eta \%$ subwords with the highest probabilities are kept. Note that we always keep the single character in subword vocabulary to avoid out-of-vocabulary.
> 
> For a specific dataset, the BPE algorithm keeps the same segmentation for the same word in different sequences, whereas ULM cannot promise such segmentation. Both segmentation algorithms have their strengths, BIBREF13 show that BPE can fix the OOV issue well, and BIBREF14 proves that ULM is a subword regularization which is helpful in neural machine translation.

#### Relevance 479

Label: 

#### Passage 480

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this section, we examine the pre-trained language models of ESuLMo in terms of PPL. All the models' training and evaluation are done on One Billion Word dataset BIBREF19 . During training, we strictly follow the same hyper-parameter published by ELMo, including the hidden size, embedding size, and the number of LSTM layers. Meanwhile, we train each model on 4 Nvidia P40 GPUs, which takes about three days for each epoch. Table TABREF5 shows that our pre-trained language models can improve the performance of RNN-based language models by a large margin and our subword-aware language models outperform all previous RNN-based language models, including ELMo, in terms of PPL. During the experiment, we find that 500 is the best vocabulary size for both segmentation algorithms, and BPE is better than ULM in our setting.

#### Relevance 480

Label: 

#### Passage 481

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Subword Vocabulary Size Tables TABREF5 and TABREF10 show the performance of ESuLMo drops with the vocabulary size increases . We explain the trend that neural network pipeline especially CNN would fail to capture necessary details of building word embeddings as more subwords are introduced.
> 
> Subword Segmentation Algorithms Tables TABREF5 and TABREF10 show that ESuLMo based on both ULM and BPE segmentation with 500 subwords outperform the original ELMo, and BPE is consistently better than ULM on all evaluations under the same settings. We notice that BPE can give static subword segmentation for the same word in different sentences, while ULM cannot. It suggests that ESuLMo is sensitive to segmentation consistency.
> 
> We also analyze the subword vocabularies from two algorithms and find that the overlapping rates for 500, 1K and 2K sizes are 60.2%, 55.1% and 51.9% respectively. This indicates subword mechanism can stably work in different vocabularies.
> 
> Task Independent vs. Task Specific To discover the necessary training progress, we show the accuracy in SNLI and PPL for language model in Figure FIGREF15. The training curves show that our ESuLMo helps ESIM reach stable accuracy for SNLI while the corresponding PPL of the language model is far away from convergence.
> 
> Word Sense Disambiguation To explore the word sense disambiguation capability of our ESuLMo, we isolate the representation encoded by our ESuLMo and use them to directly make predictions for a fine-grained word sense disambiguation (WSD) task. We choose the dataset and perform this experiment using the same setting as ELMo with only the last layer's representation. Table TABREF16 shows that our model can outperform the original ELMo.

#### Relevance 481

Label: 

### BM25

None

### Dense

#### Passage 482

Retrieved by: Dense

> for a specific low-resource language. Due to these limitations, we focus on computationally motivated subword tokenization approaches in this work.
> 
> In this paper, we propose Embedding from Subword-aware Language Models (ESuLMo), which takes subword as input to augment word representation and release a sizeable pre-trained language model research communities. Evaluations show that the pre-trained language models of ESuLMo outperform all RNN-based language models, including ELMo, in terms of PPL and ESuLMo outperforms state-of-the-art results in three of four downstream NLP tasks.

#### Relevance 482

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0054

Paper: Dialog Context Language Modeling with Recurrent Neural Networks

> How long of dialog history is captured?

### Common Retrieved Chunks

#### Passage 483

Retrieved by: BM25, Dense, Hybrid RRF

> The previously proposed contextual language models, such as DRNNLM and CCDCLM, treat dialog history as a sequence of inputs, without modeling dialog interactions. A dialog turn from one speaker may not only be a direct response to the other speaker's query, but also likely to be a continuation of his own previous statement. Thus, when modeling turn $k$ in a dialog, we propose to connect the last RNN state of turn $k-2$ directly to the starting RNN state of turn $k$ , instead of letting it to propagate through the RNN for turn $k-1$ . The last RNN state of turn $k-1$ serves as the context vector to turn $k$ , which is fed to turn $k$ 's RNN hidden state at each time step together with the word input. The model architecture is as shown in Figure 2 . The context vector $c$ and the initial RNN hidden state for the $k$ th turn $h^{\mathbf {U}_k}_{0}$ are defined as:
> 
> $$c = h^{\mathbf {U}_{k-1}}_{T_{k-1}}, \; h^{\mathbf {U}_k}_{0} = h^{\mathbf {U}_{k-2}}_{T_{k-2}}$$   (Eq. 11)
> 
> where $h^{\mathbf {U}_{k-1}}_{T_{k-1}}$ represents the last RNN hidden state of turn $k-1$ . This model also allows the context signal from previous turns to propagate through the network in fewer steps, which helps to reduce information loss along the propagation. We refer to this model as Interactive Dialog Context Language Model (IDCLM).

#### Relevance 483

Label: 

#### Passage 484

Retrieved by: BM25, Hybrid RRF

> Language model plays an important role in many natural language processing systems, such as in automatic speech recognition BIBREF0 , BIBREF1 and machine translation systems BIBREF2 , BIBREF3 . Recurrent neural network (RNN) based models BIBREF4 , BIBREF5 have recently shown success in language modeling, outperforming conventional n-gram based models. Long short-term memory BIBREF6 , BIBREF7 is a widely used RNN variant for language modeling due to its superior performance in capturing longer term dependencies.
> 
> Conventional RNN based language model uses a hidden state to represent the summary of the preceding words in a sentence without considering context signals. Mikolov et al. proposed a context dependent RNN language model BIBREF8 by connecting a contextual vector to the RNN hidden state. This contextual vector is produced by applying Latent Dirichlet Allocation BIBREF9 on preceding text. Several other contextual language models were later proposed by using bag-of-word BIBREF10 and RNN methods BIBREF11 to learn larger context representation that beyond the target sentence.
> 
> The previously proposed contextual language models treat preceding sentences as a sequence of inputs, and they are suitable for document level context modeling. In dialog modeling, however, dialog interactions between speakers play an important role. Modeling utterances in a dialog as a sequence of inputs might not well capture the pauses, turn-taking, and grounding phenomena BIBREF12 in a dialog. In this work, we propose contextual RNN language models that specially track the interactions between speakers. We expect such models to generate better representations of the dialog context.
> 
> The remainder of the paper is organized as follows. In section 2, we introduce the background on contextual language modeling. In section 3, we describe the proposed dialog context language models. Section 4 discusses the evaluation procedures and results. Section 5 concludes the work.

#### Relevance 484

Label: 

#### Passage 485

Retrieved by: BM25, Hybrid RRF

> The experiment results on language modeling perplexity for models using different dialog turn size are shown in Table 1 . $K$ value indicates the number of turns in the dialog. Perplexity is calculated on the last turn, with preceding turns used as context to the model.
> 
> As can be seen from the results, all RNN based models outperform the n-gram model by large margin. The BoW-Context-RNNLM and DRNNLM beat the Single-Turn-RNNLM consistently. Our implementation of the context dependent CCDCLM performs worse than Single-Turn-RNNLM. This might due to fact that the target turn word prediction depends too much on the previous turn context vector, which connects directly to the hidden state of current turn RNN at each time step. The model performance on training set might not generalize well during inference given the limited size of the training set.
> 
> The proposed IDCLM and ESIDCLM beat the single turn RNNLM consistently under different context turn sizes. ESIDCLM shows the best language modeling performance under dialog turn size of 3 and 5, outperforming IDCLM by a small margin. IDCLM beats all baseline models when using dialog turn size of 5, and produces slightly worse perplexity than DRNNLM when using dialog turn size of 3.
> 
> To analyze the best potential gain that may be achieved by introducing linguistic context, we compare the proposed contextual models to DACLM, the model that uses true dialog act history for dialog context modeling. As shown in Table 1 , the gap between our proposed models and DACLM is not wide. This gives a positive hint that the proposed contextual models may implicitly capture the dialog context state changes.
> 
> For fine-grained analyses of the model performance, we further compute the test set perplexity per POS tag and per dialog act tag. We selected the most frequent POS tags and dialog act tags in SwDA corpus, and report the tag based perplexity relative changes ( $\%$ ) of the proposed models comparing to Single-Turn-RNNLM. A negative number indicates performance gain.
> 
> Table 2 shows the model perplexity per POS tag. All the three context dependent models produce consistent performance gain over the Single-Turn-RNNLM for pronouns, prepositions, and adverbs, with pronouns having the largest perplexity improvement. However,

#### Relevance 485

Label: 

#### Passage 486

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> In this work, we use LSTM cell BIBREF6 as the basic RNN unit for its stronger capability in capturing long-range dependencies in a word sequence comparing to simple RNN. We use pre-trained word vectors BIBREF16 that are trained on Google News dataset to initialize the word embeddings. These word embeddings are fine-tuned during model training. We conduct mini-batch training using Adam optimization method following the suggested parameter setup in BIBREF17 . Maximum norm is set to 5 for gradient clipping . For regularization, we apply dropout ( $p=0.8$ ) on the non-recurrent connections BIBREF18 of LSTM. In addition, we apply $L_2$ regularization ( $\lambda = 10^{-4}$ ) on the weights and biases of the RNN output layer.

#### Relevance 486

Label: 

#### Passage 487

Retrieved by: BM25, Dense, Hybrid RRF

> The propagation of dialog context can be seen as a series of updates of a hidden dialog context state along the growing dialog. IDCLM models this hidden dialog context state changes implicitly in the turn level RNN state. Such dialog context state updates can also be modeled in a separated RNN. As shown in the architecture in Figure 3 , we use an external RNN to model the context changes explicitly. Input to the external state RNN is the vector representation of the previous dialog turns. The external state RNN output serves as the dialog context for next turn:
> 
> $$s_{k-1} = \operatorname{RNN}_{ES}(s_{k-2}, h^{\mathbf {U}_{k-1}}_{T_{k-1}})$$   (Eq. 14)
> 
> where $s_{k-1}$ is the output of the external state RNN after the processing of turn $k-1$ . The context vector $c$ and the initial RNN hidden state for the $k$ th turn $h^{\mathbf {U}_k}_{0}$ are then defined as:
> 
> $$c = s_{k-1}, \; h^{\mathbf {U}_k}_{0} = h^{\mathbf {U}_{k-2}}_{T_{k-2}}$$   (Eq. 15)
> 
> We refer to this model as External State Interactive Dialog Context Language Model (ESIDCLM).
> 
> Comparing to IDCLM, ESIDCLM releases the burden of turn level RNN by using an external RNN to model dialog context state changes. One drawback of ESIDCLM is that there are additional RNN model parameters to be learned during model training, which may make the model more prone to overfitting when training data size is limited.

#### Relevance 487

Label: 

#### Passage 488

Retrieved by: Dense, Hybrid RRF

> In this work, we propose two dialog context language models that with special design to model dialog interactions. Our evaluation results on Switchboard Dialog Act Corpus show that the proposed model outperform conventional RNN language model by 3.3%. The proposed models also illustrate advantageous performance over several competitive contextual language models. Perplexity of the proposed dialog context language models is higher than that of the model using true dialog act tags as context by a small margin. This indicates that the proposed model may implicitly capture the dialog context state for language modeling.

#### Relevance 488

Label: 

#### Passage 489

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> We use the Switchboard Dialog Act Corpus (SwDA) in evaluating our contextual langauge models. The SwDA corpus extends the Switchboard-1 Telephone Speech Corpus with turn and utterance-level dialog act tags. The utterances are also tagged with part-of-speech (POS) tags. We split the data in folder sw00 to sw09 as training set, folder sw10 as test set, and folder sw11 to sw13 as validation set. The training, validation, and test sets contain 98.7K turns (190.0K utterances), 5.7K turns (11.3K utterances), and 11.9K turns (22.2K utterances) respectively. Maximum turn length is set to 160. The vocabulary is defined with the top frequent 10K words.

#### Relevance 489

Label: 

### BM25

None

### Dense

#### Passage 490

Retrieved by: Dense

> The previously proposed contextual language models focus on applying context by encoding preceding text, without considering interactions in dialogs. These models may not be well suited for dialog language modeling, as they are not designed to capture dialog interactions, such as clarifications and confirmations. By making special design in learning dialog interactions, we expect the models to generate better representations of the dialog context, and thus lower perplexity of the target dialog turn or utterance.
> 
> In this section, we first explain the context dependent RNN language model that operates on utterance or turn level. Following that, we describe the two proposed contextual language models that utilize the dialog level context.

#### Relevance 490

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 491

Retrieved by: Hybrid RRF followed by BGE reranking

> Let $\mathbf {D} = (\mathbf {U}_1, \mathbf {U}_2, ..., \mathbf {U}_K)$ be a dialog that has $K$ turns and involves two speakers. Each turn may have one or more utterances. The $k$ th turn $\mathbf {U}_k = (w_1, w_2, ..., w_{T_k})$ is represented as a sequence of $T_k$ words. Conditioning on information of the preceding text in the dialog, probability of the target turn $\mathbf {U}_k$ can be calculated as:
> 
> $$P(\mathbf {U}_k|\mathbf {U}_{<k}) = \prod _{t=1}^{T_k}P(w^{\mathbf {U}_{k}}_{t}|w^{\mathbf {U}_{k}}_{< t}, \mathbf {U}_{<k}) \\$$   (Eq. 6)
> 
> where $\mathbf {U}_{<k}$ denotes all previous turns before $\mathbf {U}_k$ , and $w^{\mathbf {U}_{k}}_{< t}$ denotes all previous words before the $t$ th word in turn $\mathbf {U}_k$ .
> 
> In context dependent RNN language model, the context vector $c$ is connected to the RNN hidden state together with the input word embedding at each time step (Figure 1 ). This is similar to the context dependent RNN language model proposed in BIBREF8 , other than that the context vector is not connected directly to the RNN output layer. With the additional context vector input $c$ , the RNN state $h_t$ is updated as:
> 
> $$h_t = \operatorname{RNN}(h_{t-1}, [w_t, c])$$   (Eq. 8)

#### Relevance 491

Label: 

#### Passage 492

Retrieved by: Hybrid RRF followed by BGE reranking

> A language model assigns a probability to a sequence of words $\mathbf {w}=(w_1, w_2, ..., w_{T})$ following probability distribution. Using the chain rule, the likelihood of the word sequence $\mathbf {w}$ can be factorized as:
> 
> $$P(\mathbf {w}) = P(w_1, w_2, ..., w_{T}) = \prod _{t=1}^{T}P(w_{t}|w_{< t}) \\$$   (Eq. 2)
> 
> At time step $t$ , the system input is the embedding of the word at index $t$ , and the system output is the probability distribution of the word at index $t+1$ . The RNN hidden state $h_t$ encodes the information of the word sequence up till current step:
> 
> $$&h_t = \operatorname{RNN}(h_{t-1}, w_t) \\
> &P(w_{t+1}|w_{< t+1}) = \operatorname{softmax}(W_{o}h_{t} + b_{o})$$   (Eq. 3)
> 
> where $W_{o}$ and $b_{o}$ are the output layer weights and biases.

#### Relevance 492

Label: 

#### Passage 493

Retrieved by: Hybrid RRF followed by BGE reranking

> A number of methods have been proposed to introduce contextual information to the language model. Mikolov and Zweig BIBREF8 proposed a topic-conditioned RNNLM by introducing a contextual real-valued vector to RNN hidden state. The contextual vector was created by performing LDA BIBREF9 on preceding text. Wang and Cho BIBREF10 studied introducing corpus-level discourse information into language modeling. A number of context representation methods were explored, including bag-of-words, sequence of bag-of-words, and sequence of bag-of-words with attention. Lin et al. BIBREF13 proposed using hierarchical RNN for document modeling. Comparing to using bag-of-words and sequence of bag-of-words for document context representation, using hierarchical RNN can better model the order of words in preceding text, at the cost of the increased computational complexity. These contextual language models focused on contextual information at the document level. Tran et al. BIBREF14 further proposed a contextual language model that consider information at inter-document level. They claimed that by utilizing the structural information from a tree-structured document set, language modeling performance was largely improved.

#### Relevance 493

Label: 

## Question 0055

Paper: Topic-Specific Sentiment Analysis Can Help Identify Political Ideology

> Which widely used dataset did the authors use?

### Common Retrieved Chunks

#### Passage 494

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We proposed to exploit topic-specific sentiment analysis for the task of automatic ideology detection from text. We described a simple framework for representing political ideologies and documents as a matrix capturing sentiment distributions over topics and used this representation for classifying documents based on their topic-sentiment signatures. Empirical evaluation over a widely used dataset of US Congressional speeches showed that the proposed approach performs on a par with classifiers using distributional text representations. In addition, the proposed approach offers simplicity and easy interpretability of results making it a promising technique for ideology detection. Our immediate future work will focus on further solidifying our observations by using a larger dataset to learn better TSMs for different ideologies. Further, the framework easily lends itself to be used for detecting ideological leanings of authors, social media users, news websites, magazines, etc. by computing their TSMs and comparing against the TSMs of different ideologies.

#### Relevance 494

Label: 

#### Passage 495

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> often bring the ideological differences to the centre stage, though somewhat indirectly. Heated debates in such forums tend to focus on the choices proposed by the executive that are in sharp conflict with the preference structure of the opposition members. Due to this inherent tendency of parliamentary debates to focus on topics of disagreement, the sentiments exposited in debates hold valuable cues to identify the political orientation of the participants.
> 
> We develop a simple classification model that uses a topic-specific sentiment summarization for republican and democrat speeches separately. Initial results of experiments conducted using a widely used dataset of US Congress debates BIBREF3 are encouraging and show that this simple model compares well with classification models that employ state-of-the-art distributional text representations (Section SECREF4 ).

#### Relevance 495

Label: 

#### Passage 496

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We used the publicly available Convote dataset BIBREF3 for our experiments. The dataset provides transcripts of debates in the House of Representatives of the U.S Congress for the year 2005. Each file in the dataset corresponds to a single, uninterrupted utterance by a speaker in a given debate. We combine all the utterances of a speaker in a given debate in a single file to capture different opinions/view points of the speaker about the debate topic. We call this document the view point document (VPD) representing the speaker's opinion about different aspects of the issue being debated. The dataset also provides political affiliations of all the speakers – Republican (R), Democrat (D), and Independent (I). With there being only six documents for the independent class (four in training, two in test), we excluded them from our evaluation. Table TABREF15 summarizes the statistics about the dataset and distribution of different classes. We obtained 50 topics using LDA from Mallet run over the training dataset. The topic-sentiment matrix was obtained using the Stanford CoreNLP sentiment API BIBREF9 which provides probability distributions over a set of five sentiment polarity classes.

#### Relevance 496

Label: 

#### Passage 497

Retrieved by: BM25, Dense, Hybrid RRF

> In constructing TSMs, we make use of topic-specific sentiment estimations as outlined above. Typical sentiment analysis methods (e.g., NLTK Sentiment Analysis) are designed to determine the overall sentiment for a text segment. Using such sentiment analysis methods in order to determine topic-specific sentiments is not necessarily straightforward. We adopt a simple keyword based approach for the task. For every document-topic pair INLINEFORM0 , we extract the sentences from INLINEFORM1 that contain at least one of the top- INLINEFORM2 keywords associated with the topic INLINEFORM3 . We then collate the sentences in the order in which they appear in INLINEFORM4 and form a mini-document INLINEFORM5 . This document INLINEFORM6 is then passed on to a conventional sentiment analyzer that would then estimate the sentiment polarity as a probability distribution over sentiment polarity classes, which then forms the INLINEFORM7 vector. We use INLINEFORM8 and the RNN based sentiment analyzer BIBREF8 in our method.

#### Relevance 497

Label: 

#### Passage 498

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> In two class scenarios with label such as INLINEFORM0 or INLINEFORM1 as we have in our dataset, TSMs can be flattened into a vector and fed into a logistic regression classifier that learns weights - i.e., co-efficients for each topic + sentiment polarity class combination. These weights can then be used to estimate the label by applying it to the new document's TSM.

#### Relevance 498

Label: 

#### Passage 499

Retrieved by: Dense, Hybrid RRF

> Sentiment analysis has proved to be a useful tool in detecting controversial topics as it can help identify topics that evoke different feelings among people on opposite side of the arguments. Mejova et al. controversy-news2 analyzed language use in controversial news articles and found that a writer may choose to highlight the negative aspects of the opposing view rather than emphasizing the positive aspects of one’s view. Lourentzou et al. controversy-news3 utilize the sentiments expressed in social media comments to identify controversial portions of news articles. Given a news article and its associated comments on social media, the paper links comments with each sentence of the article (by using a sentence as a query and retrieving comments using BM25 score). For all the comments associated with a sentence, a sentiment score is then computed, and sentences with large variations in positive and negative comments are identified as controversial sentences. Choi et al. controversy-news go one step further and identify controversial topics and their sub-topics in news articles.

#### Relevance 499

Label: 

#### Passage 502

Retrieved by: Hybrid RRF, Hybrid RRF followed by BGE reranking

> Political ideology detection has been a relatively new field of research within the NLP community. Most of the previous efforts have focused on capturing the variations in language use in text representing content of different ideologies. Beissmann et al. ideologyPrediction-text employ bag-of-word features for ideology detection in different domains such as speeches in German parliament, party manifestos, and facebook posts. Sim et al. ideological-proportion-speeches use a labeled corpus of political writings to infer lexicons of cues strongly associated with different ideologies. These “ideology lexicons” are then used to analyze political speeches and identify their ideological leanings. Iyyer at al. rnn-ideology recently adopted a recursive neural network architecture to detect ideological bias of single sentences. In addition, topic models have also been used for ideology detection by identifying latent topic distributions across different ideologies BIBREF4 , BIBREF5 . Gerrish and Blei legislativeRollCalls connected text of the legislations to voting patterns of legislators from different parties.

#### Relevance 502

Label: 

### BM25

None

### Dense

#### Passage 500

Retrieved by: Dense

> to worker safety (L3) and energy projects (L2). One counter-intuitive observation is topic related to gun control (L4) that is amongst the least polarizing topics. This anomaly could be attributed to only a few speeches related to this issue in the training set (only 23 out of 1175 speeches mention gun) that prevents a reliable estimate of the probability distributions. We observed similar low occurrences of other lower distance topics too indicating the potential for improvements in computation of topic-specific sentiment representations with more data. In fact, performing the nearest neighbor classification INLINEFORM0 with only top-10 most polarizing topics led to improvements in classification accuracy from INLINEFORM1 to INLINEFORM2 suggesting that with more data, better INLINEFORM3 representations could be learned that are better at discriminating between different ideologies.

#### Relevance 500

Label: 

#### Passage 501

Retrieved by: Dense

> Towards analyzing the significance of the results, we would like to start with drawing attention to the format of the data used in the TSM methods. The document-specific TSM matrices do not contain any information about the topics themselves, but only about the sentiment in the document towards each topic; one may recollect that INLINEFORM0 is a quantification of the strength of the sentiment in INLINEFORM1 towards topic INLINEFORM2 . Thus, in contrast to distributional embeddings such as doc2vec, TSMs contain only the information that directly relates to sentiment towards specific topics that are learnt from across the corpus. The results indicate that TSM methods are able to achieve comparable performance to doc2vec-based methods despite usage of only a small slice of informatiom. This points to the importance of sentiment information in determining the political leanings from text. We believe that leveraging TSMs along with distributional embeddings in a manner that can combine the best of both views would improve the state-of-the-art of political ideology detection.
> 
> Next, we also studied if there are topics that are more polarizing than others and how different topics impact classification performance. We identified polarizing topics, i.e, topics that invoke opposite sentiments across two classes (ideologies) by using the following equation. DISPLAYFORM0
> 
> Here, INLINEFORM0 represent the sentiment vectors for topic INLINEFORM1 for republican and democrat classes. Note that these sentiment vectors are the rows corresponding to topic INLINEFORM2 in TSMs for the two classes, respectively.
> 
> Table TABREF21 lists the top five topics with most distance, i.e., most polarizing topics (top) and five topics with least distance, i.e.,least polarizing topics (bottom) as computed by equation EQREF23 . Note that the topics are represented using the top keywords that they contain according to the probability distribution of the topic. We observe that the most polarizing topics include topics related to healthcare (H3, H4), military programs (H5), and topics related to administration processes (H1 and H2). The least polarizing topics include topics related to worker safety (L3) and energy projects (L2). One counter-intuitive observation is topic related to gun control (L4) that is amongst the least polarizing topics. This anomaly could be attributed to only a few speeches related to this issue in

#### Relevance 501

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0056

Paper: Automatic Judgment Prediction via Legal Reading Comprehension

> what datasets are used in the experiment?

### Common Retrieved Chunks

#### Passage 503

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Since none of the datasets from previous works have been published, we decide to build a new one. We randomly collect INLINEFORM0 cases from China Judgments Online, among which INLINEFORM1 cases are for training, INLINEFORM2 each for validation and testing. Among the original cases, INLINEFORM3 are granted divorce and others not. There are INLINEFORM4 valid pleas in total, with INLINEFORM5 supported and INLINEFORM6 rejected. Note that, if the divorce plea in a case is not granted, the other pleas of this case will not be considered by the judge. Case materials are all natural language sentences, with averagely INLINEFORM7 tokens per fact description and INLINEFORM8 per plea. There are 62 relevant law articles in total, each with INLINEFORM9 tokens averagely. Note that the case documents include special typographical signals, making it easy to extract labeled data with regular expression.
> 
> We apply some rules with legal prior to preprocess the dataset according to previous works BIBREF33 , BIBREF34 , BIBREF35 , which have proved effective in our experiments.
> 
> Name Replacement: All names in case documents are replaced with marks indicating their roles, instead of simply anonymizing them, e.g. <Plantiff>, <Defendant>, <Daughter_x> and so on. Since “all are equal before the law”, names should make no more difference than what role they take.
> 
> Law Article Filtration : Since most accessible divorce proceeding documents do not contain ground-truth fine-grained articles, we use an unsupervised method instead. First, we extract all the articles from the law text with regular expression. Afterwards, we select the most relevant 10 articles according to the fact descriptions as follows. We obtain sentence representation with CBOW BIBREF36 , BIBREF37 weighted by inverse document frequency, and calculate cosine distance between cases and law articles. Word embeddings are pre-trained with Chinese Wikipedia pages. As the final step, we extract top 5 relevant articles for each sample respectively from the main marriage law articles and their interpretations, which are equally important. We manually check the extracted articles for 100 cases to ensure that the extraction quality is fairly good and acceptable.
> 
> The filtration process is automatic and fully unsupervised since the original documents have no ground-truth labels for fine-grained law articles, and coarse-grained law-articles only provide limited

#### Relevance 503

Label: 

#### Passage 504

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> In this paper, we explore the task of predicting judgments of civil cases. Comparing with conventional text classification framework, we propose Legal Reading Comprehension framework to handle multiple and complex textual inputs. Moreover, we present a novel neural model, AutoJudge, to incorporate law articles for judgment prediction. In experiments, we compare our model on divorce proceedings with various state-of-the-art baselines of various frameworks. Experimental results show that our model achieves considerable improvement than all the baselines. Besides, visualization results also demonstrate the effectiveness and interpretability of our proposed model.
> 
> In the future, we can explore the following directions: (1) Limited by the datasets, we can only verify our proposed model on divorce proceedings. A more general and larger dataset will benefit the research on judgment prediction. (2) Judicial decisions in some civil cases are not always binary, but more diverse and flexible ones, e.g. compensation amount. Thus, it is critical for judgment prediction to manage various judgment forms.

#### Relevance 504

Label: 

#### Passage 506

Retrieved by: BM25, Dense, Hybrid RRF

> AutoJudge is characterized by the incorporation of pair-wise attentive reader, law articles, and a CNN output layer, as well as some pre-processing with legal prior. We design ablation tests respectively to evaluate the effectiveness of these modules. When taken off the attention mechanism, AutoJudge degrades into a GRU on which a CNN is stacked. When taken off law articles, the CNN output layer only takes INLINEFORM0 as input. Besides, our model is tested respectively without name-replacement or unsupervised selection of law articles (i.e. passing the whole law text). As mentioned above, we system use law articles extracted with unsupervised method, so we also experiment with ground-truth law articles.
> 
> Results are shown in Table TABREF38 . We can infer that:
> 
> (1) The performance drops significantly after removing the attention layer or excluding the law articles, which is consistent with the comparison between AutoJudge and baselines. The result verifies that both the reading mechanism and incorporation of law articles are important and effective.
> 
> (2) After replacing CNN with an LSTM layer, performance drops as much as INLINEFORM0 in accuracy and INLINEFORM1 in F1 score. The reason may be the redundancy of RNNs. AutoJudge has employed several GRU layers to encode text sequences. Another RNN layer may be useless to capture sequential dependencies, while CNN can catch the local structure in convolution windows.
> 
> (3) Motivated by existing rule-based works, we conduct data pre-processing on cases, including name replacement and law article filtration. If we remove the pre-processing operations, the performance drops considerably. It demonstrates that applying the prior knowledge in legal filed would benefit the understanding of legal cases.
> 
> It's intuitive that the quality of the retrieved law articles would affect the final performance. As is shown in Table TABREF38 , feeding the whole law text without filtration results in worse performance. However, when we train and evaluate our model with ground truth articles, the performance is boosted by nearly INLINEFORM0 in both F1 and Acc. The performance improvement is quite limited compared to that in previous work BIBREF3 for the following reasons: (1) As mentioned above, most case documents only contain coarse-grained articles, and only a small number of them contain fine-grained ones, which has limited information

#### Relevance 506

Label: 

#### Passage 507

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> provide better an environment for children's growth as well as parents' financial condition. Here, different pleas are independent.
> 
> Heterogeneity of Input Triple. Inputs to a judgment prediction system consist of three heterogeneous yet complementary parts, i.e., fact description, plaintiff's plea, and related law articles. Concatenating them together and treating them simply as a sequence of words as in previous works BIBREF2 , BIBREF1 would cause a great loss of information. This is the same in question-answering where the dual inputs, i.e., query and passage, should be modeled separately.
> 
> Despite the introduction of the neural networks that can learn better semantic representations of input text, it remains unsolved to incorporate proper mechanisms to integrate the complementary triple of pleas, fact descriptions, and law articles together.
> 
> Inspired by recent advances in question answering (QA) based reading comprehension (RC) BIBREF5 , BIBREF6 , BIBREF7 , BIBREF8 , we propose the Legal Reading Comprehension (LRC) framework for automatic judgment prediction. LRC incorporates the reading mechanism for better modeling of the complementary inputs above-mentioned, as is done by human judges when referring to legal materials in search of supporting law articles. Reading mechanism, by simulating how human connects and integrates multiple text, has proven an effective module in RC tasks. We argue that applying the reading mechanism in a proper way among the triplets can obtain a better understanding and more informative representation of the original text, and further improve performance . To instantiate the framework, we propose an end-to-end neural network model named AutoJudge.
> 
> For experiments, we train and evaluate our models in the civil law system of mainland China. We collect and construct a large-scale real-world data set of INLINEFORM0 case documents that the Supreme People's Court of People's Republic of China has made publicly available. Fact description, pleas, and results can be extracted easily from these case documents with regular expressions, since the original documents have special typographical characteristics indicating the discourse structure. We also take into account law articles and their corresponding juridical interpretations. We also implement and evaluate previous methods on our dataset, which prove to be strong baselines.
> 
> Our experiment results show significant improvements over previous methods. Further experiments demonstrate that our model also

#### Relevance 507

Label: 

#### Passage 508

Retrieved by: Dense, Hybrid RRF

> For comparison, we adopt and re-implement three kinds of baselines as follows:
> 
> We implement an SVM with lexical features in accordance with previous works BIBREF16 , BIBREF17 , BIBREF1 , BIBREF15 , BIBREF4 and select the best feature set on the development set.
> 
> We implement and fine-tune a series of neural text classifiers, including attention-based method BIBREF3 and other methods we deem important. CNN BIBREF18 and GRU BIBREF27 , BIBREF21 take as input the concatenation of fact description and plea. Similarly, CNN/GRU+law refers to using the concatenation of fact description, plea and law articles as inputs.
> 
> We implement and train some off-the-shelf RC models, including r-net BIBREF5 and AoA BIBREF6 , which are the leading models on SQuAD leaderboard. In our initial experiments, these models take fact description as passage and plea as query. Further, Law articles are added to the fact description as a part of the reading materials, which is a simple way to consider them as well.

#### Relevance 508

Label: 

#### Passage 509

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> account law articles and their corresponding juridical interpretations. We also implement and evaluate previous methods on our dataset, which prove to be strong baselines.
> 
> Our experiment results show significant improvements over previous methods. Further experiments demonstrate that our model also achieves considerable improvement over other off-the-shelf state-of-the-art models under classification and question answering framework respectively. Ablation tests carried out by taking off some components of our model further prove its robustness and effectiveness.
> 
> To sum up, our contributions are as follows:
> 
> (1) We introduce reading mechanism and re-formalize judgment prediction as Legal Reading Comprehension to better model the complementary inputs.
> 
> (2) We construct a real-world dataset for experiments, and plan to publish it for further research.
> 
> (3) Besides baselines from previous works, we also carry out comprehensive experiments comparing different existing deep neural network methods on our dataset. Supported by these experiments, improvements achieved by LRC prove to be robust.

#### Relevance 509

Label: 

#### Passage 511

Retrieved by: Dense, Hybrid RRF

> We visualize the heat maps of attention results. As shown in Fig. FIGREF47 , deeper background color represents larger attention score. The attention score is calculated with Eq. ( EQREF15 ). We take the average of the resulting INLINEFORM0 attention matrix over the time dimension to obtain attention values for each word.
> 
> The visualization demonstrates that the attention mechanism can capture relevant patterns and semantics in accordance with different pleas in different cases.
> 
> As for the failed samples, the most common reason comes from the anonymity issue, which is also shown in Fig. FIGREF47 . As mentioned above, we conduct name replacement. However, some critical elements are also anonymized by the government, due to the privacy issue. These elements are sometimes important to judgment prediction. For example, determination of the key factor long-time separation is relevant to the explicit dates, which are anonymized.

#### Relevance 511

Label: 

### BM25

#### Passage 505

Retrieved by: BM25

> for 100 cases to ensure that the extraction quality is fairly good and acceptable.
> 
> The filtration process is automatic and fully unsupervised since the original documents have no ground-truth labels for fine-grained law articles, and coarse-grained law-articles only provide limited information. We also experiment with the ground-truth articles, but only a small fraction of them has fine-grained ones, and they are usually not available in real-world scenarios.

#### Relevance 505

Label: 

### Dense

#### Passage 510

Retrieved by: Dense

> As illustrated in Fig. FIGREF6 , Text Encoder aims to encode the word sequences of inputs into continuous representation sequences.
> 
> Formally, consider a fact description INLINEFORM0 , a plea INLINEFORM1 , and the relevant law articles INLINEFORM2 , where INLINEFORM3 denotes the INLINEFORM4 -th word in the sequence and INLINEFORM5 are the lengths of word sequences INLINEFORM6 respectively. First, we convert the words to their respective word embeddings to obtain INLINEFORM7 , INLINEFORM8 and INLINEFORM9 , where INLINEFORM10 . Afterwards, we employ bi-directional GRU BIBREF27 , BIBREF28 , BIBREF29 to produce the encoded representation INLINEFORM11 of all words as follows: DISPLAYFORM0
> 
> Note that, we adopt different bi-directional GRUs to encode fact descriptions, pleas, and law articles respectively(denoted as INLINEFORM0 , INLINEFORM1 , and INLINEFORM2 ). With these text encoders, INLINEFORM3 , INLINEFORM4 , and INLINEFORM5 are converting into INLINEFORM6 , INLINEFORM7 , and INLINEFORM8 .

#### Relevance 510

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 512

Retrieved by: Hybrid RRF followed by BGE reranking

> We employ Jieba for Chinese word segmentation and keep the top INLINEFORM0 frequent words. The word embedding size is set to 128 and the other low-frequency words are replaced with the mark <UNK>. The hidden size of GRU is set to 128 for each direction in Bi-GRU. In the pair-wise attentive reader, the hidden state is set to 256 for mGRu. In the CNN layer, filter windows are set to 1, 3, 4, and 5 with each filter containing 200 feature maps. We add a dropout layer BIBREF38 after the CNN layer with a dropout rate of INLINEFORM1 . We use Adam BIBREF32 for training and set learning rate to INLINEFORM2 , INLINEFORM3 to INLINEFORM4 , INLINEFORM5 to INLINEFORM6 , INLINEFORM7 to INLINEFORM8 , batch size to 64. We employ precision, recall, F1 and accuracy for evaluation metrics. We repeat all the experiments for 10 times, and report the average results.

#### Relevance 512

Label: 

## Question 0057

Paper: Sequence-Level Knowledge Distillation

> Which dataset do they train on?

### Common Retrieved Chunks

#### Passage 513

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> sequence. In fact, in experiments we find that with beam of size 1, INLINEFORM2 (on average) accounts for INLINEFORM3 of the distribution for German INLINEFORM4 English, and INLINEFORM5 for Thai INLINEFORM6 English (Table 1: INLINEFORM7 ).
> 
> To summarize, sequence-level knowledge distillation suggests to: (1) train a teacher model, (2) run beam search over the training set with this model, (3) train the student network with cross-entropy on this new dataset. Step (3) is identical to the word-level NLL process except now on the newly-generated data set. This is shown in Figure 1 (center).

#### Relevance 513

Label: 

#### Passage 514

Retrieved by: BM25, Dense, Hybrid RRF

> Next we consider integrating the training data back into the process, such that we train the student model as a mixture of our sequence-level teacher-generated data ( INLINEFORM0 ) with the original training data ( INLINEFORM1 ), INLINEFORM2
> 
> where INLINEFORM0 is the gold target sequence.
> 
> Since the second term is intractable, we could again apply the mode approximation from the previous section, INLINEFORM0
> 
> and train on both observed ( INLINEFORM0 ) and teacher-generated ( INLINEFORM1 ) data. However, this process is non-ideal for two reasons: (1) unlike for standard knowledge distribution, it doubles the size of the training data, and (2) it requires training on both the teacher-generated sequence and the true sequence, conditioned on the same source input. The latter concern is particularly problematic since we observe that INLINEFORM2 and INLINEFORM3 are often quite different.
> 
> As an alternative, we propose a single-sequence approximation that is more attractive in this setting. This approach is inspired by local updating BIBREF12 , a method for discriminative training in statistical machine translation (although to our knowledge not for knowledge distillation). Local updating suggests selecting a training sequence which is close to INLINEFORM0 and has high probability under the teacher model, INLINEFORM1
> 
> where INLINEFORM0 is a function measuring closeness (e.g. Jaccard similarity or BLEU BIBREF13 ). Following local updating, we can approximate this sequence by running beam search and choosing INLINEFORM1
> 
> where INLINEFORM0 is the INLINEFORM1 -best list from beam search. We take INLINEFORM2 to be smoothed sentence-level BLEU BIBREF14 .
> 
> We justify training on INLINEFORM0 from a knowledge distillation perspective with the following generative process: suppose that there is a true target sequence (which we do not observe) that is first generated from the underlying data distribution INLINEFORM1 . And further suppose that the target sequence that we observe ( INLINEFORM2 ) is a noisy version of the unobserved true sequence: i.e. (i) INLINEFORM3 , (ii) INLINEFORM4 , where INLINEFORM5 is, for example, a noise function that independently replaces each element in INLINEFORM6 with a random element in INLINEFORM7 with some small probability. In such a case, ideally the student's distribution should match the mixture distribution, INLINEFORM10
> 
> In this setting, due to the noise assumption, INLINEFORM0 now has

#### Relevance 514

Label: 

#### Passage 515

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> distillation in the context of neural machine translation. We note that NMT differs from previous work which has mainly explored non-recurrent models in the multi-class prediction setting. For NMT, while the model is trained on multi-class prediction at the word-level, it is tasked with predicting complete sequence outputs conditioned on previous decisions. With this difference in mind, we experiment with standard knowledge distillation for NMT and also propose two new versions of the approach that attempt to approximately match the sequence-level (as opposed to word-level) distribution of the teacher network. This sequence-level approximation leads to a simple training procedure wherein the student network is trained on a newly generated dataset that is the result of running beam search with the teacher network.
> 
> We run experiments to compress a large state-of-the-art INLINEFORM0 LSTM model, and find that with sequence-level knowledge distillation we are able to learn a INLINEFORM1 LSTM that roughly matches the performance of the full system. We see similar results compressing a INLINEFORM2 model down to INLINEFORM3 on a smaller data set. Furthermore, we observe that our proposed approach has other benefits, such as not requiring any beam search at test-time. As a result we are able to perform greedy decoding on the INLINEFORM4 model 10 times faster than beam search on the INLINEFORM5 model with comparable performance. Our student models can even be run efficiently on a standard smartphone. Finally, we apply weight pruning on top of the student network to obtain a model that has INLINEFORM6 fewer parameters than the original teacher model. We have released all the code for the models described in this paper.

#### Relevance 515

Label: 

#### Passage 516

Retrieved by: BM25, Hybrid RRF

> Compressing deep learning models is an active area of current research. Pruning methods involve pruning weights or entire neurons/nodes based on some criterion. LeCun1990 prune weights based on an approximation of the Hessian, while Han2016 show that a simple magnitude-based pruning works well. Prior work on removing neurons/nodes include Srinivas2015 and Mariet2016. See2016 were the first to apply pruning to Neural Machine Translation, observing that that different parts of the architecture (input word embeddings, LSTM matrices, etc.) admit different levels of pruning. Knowledge distillation approaches train a smaller student model to mimic a larger teacher model, by minimizing the loss between the teacher/student predictions BIBREF0 , BIBREF10 , BIBREF11 , BIBREF1 . Romero2015 additionally regress on the intermediate hidden layers of the student/teacher network as a pretraining step, while Mou2015 obtain smaller word embeddings from a teacher model via regression. There has also been work on transferring knowledge across different network architectures: Chan2015b show that a deep non-recurrent neural network can learn from an RNN; Geras2016 train a CNN to mimic an LSTM for speech recognition. Kuncoro2016 recently investigated knowledge distillation for structured prediction by having a single parser learn from an ensemble of parsers.
> 
> Other approaches for compression involve low rank factorizations of weight matrices BIBREF20 , BIBREF21 , BIBREF22 , BIBREF23 , sparsity-inducing regularizers BIBREF24 , binarization of weights BIBREF25 , BIBREF26 , and weight sharing BIBREF27 , BIBREF9 . Finally, although we have motivated sequence-level knowledge distillation in the context of training a smaller model, there are other techniques that train on a mixture of the model's predictions and the data, such as local updating BIBREF12 , hope/fear training BIBREF28 , SEARN BIBREF29 , DAgger BIBREF30 , and minimum risk training BIBREF31 , BIBREF32 .

#### Relevance 516

Label: 

#### Passage 519

Retrieved by: Dense, Hybrid RRF

> To test out these approaches, we conduct two sets of NMT experiments: high resource (English INLINEFORM0 German) and low resource (Thai INLINEFORM1 English).
> 
> The English-German data comes from WMT 2014. The training set has 4m sentences and we take newstest2012/newstest2013 as the dev set and newstest2014 as the test set. We keep the top 50k most frequent words, and replace the rest with UNK. The teacher model is a INLINEFORM0 LSTM (as in Luong2015) and we train two student models: INLINEFORM1 and INLINEFORM2 . The Thai-English data comes from IWSLT 2015. There are 90k sentences in the training set and we take 2010/2011/2012 data as the dev set and 2012/2013 as the test set, with a vocabulary size is 25k. Size of the teacher model is INLINEFORM3 (which performed better than INLINEFORM4 , INLINEFORM5 models), and the student model is INLINEFORM6 . Other training details mirror Luong2015.
> 
> We evaluate on tokenized BLEU with INLINEFORM0 , and experiment with the following variations:

#### Relevance 519

Label: 

### BM25

#### Passage 517

Retrieved by: BM25

> In this work we have investigated existing knowledge distillation methods for NMT (which work at the word-level) and introduced two sequence-level variants of knowledge distillation, which provide improvements over standard word-level knowledge distillation.
> 
> We have chosen to focus on translation as this domain has generally required the largest capacity deep learning models, but the sequence-to-sequence framework has been successfully applied to a wide range of tasks including parsing BIBREF33 , summarization BIBREF34 , dialogue BIBREF35 , BIBREF36 , BIBREF37 , NER/POS-tagging BIBREF38 , image captioning BIBREF39 , BIBREF40 , video generation BIBREF41 , and speech recognition BIBREF42 . We anticipate that methods described in this paper can be used to similarly train smaller models in other domains.

#### Relevance 517

Label: 

### Dense

#### Passage 518

Retrieved by: Dense

> Knowledge distillation describes a class of methods for training a smaller student network to perform better by learning from a larger teacher network (in addition to learning from the training data set). We generally assume that the teacher has previously been trained, and that we are estimating parameters for the student. Knowledge distillation suggests training by matching the student's predictions to the teacher's predictions. For classification this usually means matching the probabilities either via INLINEFORM0 on the INLINEFORM1 scale BIBREF10 or by cross-entropy BIBREF11 , BIBREF1 .
> 
> Concretely, assume we are learning a multi-class classifier over a data set of examples of the form INLINEFORM0 with possible classes INLINEFORM1 . The usual training criteria is to minimize NLL for each example from the training data, INLINEFORM2
> 
> where INLINEFORM0 is the indicator function and INLINEFORM1 the distribution from our model (parameterized by INLINEFORM2 ). This objective can be seen as minimizing the cross-entropy between the degenerate data distribution (which has all of its probability mass on one class) and the model distribution INLINEFORM3 .
> 
> In knowledge distillation, we assume access to a learned teacher distribution INLINEFORM0 , possibly trained over the same data set. Instead of minimizing cross-entropy with the observed data, we instead minimize the cross-entropy with the teacher's probability distribution, INLINEFORM1
> 
> where INLINEFORM0 parameterizes the teacher distribution and remains fixed. Note the cross-entropy setup is identical, but the target distribution is no longer a sparse distribution. Training on INLINEFORM5 is attractive since it gives more information about other classes for a given data point (e.g. similarity between classes) and has less variance in gradients BIBREF1 .
> 
> Since this new objective has no direct term for the training data, it is common practice to interpolate between the two losses, INLINEFORM0
> 
> where INLINEFORM0 is mixture parameter combining the one-hot distribution and the teacher distribution.

#### Relevance 518

Label: 

#### Passage 520

Retrieved by: Dense

> Although knowledge distillation enables training faster models, the number of parameters for the student models is still somewhat large (Table 1: Params), due to the word embeddings which dominate most of the parameters. For example, on the INLINEFORM0 English INLINEFORM1 German model the word embeddings account for approximately INLINEFORM2 (50m out of 84m) of the parameters. The size of word embeddings have little impact on run-time as the word embedding layer is a simple lookup table that only affects the first layer of the model.
> 
> We therefore focus next on reducing the memory footprint of the student models further through weight pruning. Weight pruning for NMT was recently investigated by See2016, who found that up to INLINEFORM0 of the parameters in a large NMT model can be pruned with little loss in performance. We take our best English INLINEFORM1 German student model ( INLINEFORM2 Seq-KD INLINEFORM3 Seq-Inter) and prune INLINEFORM4 of the parameters by removing the weights with the lowest absolute values. We then retrain the pruned model on Seq-KD data with a learning rate of INLINEFORM5 and fine-tune towards Seq-Inter data with a learning rate of INLINEFORM6 . As observed by See2016, retraining proved to be crucial. The results are shown in Table 3.
> 
> Our findings suggest that compression benefits achieved through weight pruning and knowledge distillation are orthogonal. Pruning INLINEFORM0 of the weight in the INLINEFORM1 student model results in a model with INLINEFORM2 fewer parameters than the original teacher model with only a decrease of INLINEFORM3 BLEU. While pruning INLINEFORM4 of the weights results in a more appreciable decrease of INLINEFORM5 BLEU, the model is drastically smaller with 8m parameters, which is INLINEFORM6 fewer than the original teacher model.

#### Relevance 520

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 521

Retrieved by: Hybrid RRF followed by BGE reranking

> The large sizes of neural machine translation systems make them an ideal candidate for knowledge distillation approaches. In this section we explore three different ways this technique can be applied to NMT.

#### Relevance 521

Label: 

#### Passage 522

Retrieved by: Hybrid RRF followed by BGE reranking

> Neural machine translation (NMT) BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 is a deep learning-based method for translation that has recently shown promising results as an alternative to statistical approaches. NMT systems directly model the probability of the next word in the target sentence simply by conditioning a recurrent neural network on the source sentence and previously generated target words.
> 
> While both simple and surprisingly accurate, NMT systems typically need to have very high capacity in order to perform well: Sutskever2014 used a 4-layer LSTM with 1000 hidden units per layer (herein INLINEFORM0 ) and Zhou2016 obtained state-of-the-art results on English INLINEFORM1 French with a 16-layer LSTM with 512 units per layer. The sheer size of the models requires cutting-edge hardware for training and makes using the models on standard setups very challenging.
> 
> This issue of excessively large networks has been observed in several other domains, with much focus on fully-connected and convolutional networks for multi-class classification. Researchers have particularly noted that large networks seem to be necessary for training, but learn redundant representations in the process BIBREF6 . Therefore compressing deep models into smaller networks has been an active area of research. As deep learning systems obtain better results on NLP tasks, compression also becomes an important practical issue with applications such as running deep learning models for speech and translation locally on cell phones.
> 
> Existing compression methods generally fall into two categories: (1) pruning and (2) knowledge distillation. Pruning methods BIBREF7 , BIBREF8 , BIBREF9 , zero-out weights or entire neurons based on an importance criterion: LeCun1990 use (a diagonal approximation to) the Hessian to identify weights whose removal minimally impacts the objective function, while Han2016 remove weights based on thresholding their absolute values. Knowledge distillation approaches BIBREF0 , BIBREF10 , BIBREF1 learn a smaller student network to mimic the original teacher network by minimizing the loss (typically INLINEFORM0 or cross-entropy) between the student and teacher output.
> 
> In this work, we investigate knowledge distillation in the context of neural machine translation. We note that NMT differs from previous work which has mainly explored non-recurrent models in the multi-class prediction setting. For NMT, while the model is trained on multi-class prediction at the word-level,

#### Relevance 522

Label: 

#### Passage 523

Retrieved by: Hybrid RRF followed by BGE reranking

> NMT systems are trained directly to minimize word NLL, INLINEFORM0 , at each position. Therefore if we have a teacher model, standard knowledge distillation for multi-class cross-entropy can be applied. We define this distillation for a sentence as, INLINEFORM1
> 
> where INLINEFORM0 is the target vocabulary set. The student can further be trained to optimize the mixture of INLINEFORM1 and INLINEFORM2 . In the context of NMT, we refer to this approach as word-level knowledge distillation and illustrate this in Figure 1 (left).

#### Relevance 523

Label: 

## Question 0058

Paper: Quasi-Recurrent Neural Networks

> What pooling function is used?

### Common Retrieved Chunks

#### Passage 524

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Motivated by several common natural language tasks, and the long history of work on related architectures, we introduce several extensions to the stacked QRNN described above. Notably, many extensions to both recurrent and convolutional models can be applied directly to the QRNN as it combines elements of both model types.
> 
> Regularization An important extension to the stacked QRNN is a robust regularization scheme inspired by recent work in regularizing LSTMs.
> 
> The need for an effective regularization method for LSTMs, and dropout's relative lack of efficacy when applied to recurrent connections, led to the development of recurrent dropout schemes, including variational inference–based dropout BIBREF13 and zoneout BIBREF14 . These schemes extend dropout to the recurrent setting by taking advantage of the repeating structure of recurrent networks, providing more powerful and less destructive regularization.
> 
> Variational inference–based dropout locks the dropout mask used for the recurrent connections across timesteps, so a single RNN pass uses a single stochastic subset of the recurrent weights. Zoneout stochastically chooses a new subset of channels to “zone out” at each timestep; for these channels the network copies states from one timestep to the next without modification.
> 
> As QRNNs lack recurrent weights, the variational inference approach does not apply. Thus we extended zoneout to the QRNN architecture by modifying the pooling function to keep the previous pooling state for a stochastic subset of channels. Conveniently, this is equivalent to stochastically setting a subset of the QRNN's INLINEFORM0 gate channels to 1, or applying dropout on INLINEFORM1 : DISPLAYFORM0
> 
> Thus the pooling function itself need not be modified at all. We note that when using an off-the-shelf dropout layer in this context, it is important to remove automatic rescaling functionality from the implementation if it is present. In many experiments, we also apply ordinary dropout between layers, including between word embeddings and the first QRNN layer.
> 
> Densely-Connected Layers We can also extend the QRNN architecture using techniques introduced for convolutional networks. For sequence classification tasks, we found it helpful to use skip-connections between every QRNN layer, a technique termed “dense convolution” by BIBREF15 . Where traditional feed-forward or convolutional networks have connections only between subsequent layers, a “DenseNet” with INLINEFORM0 layers has feed-forward or

#### Relevance 524

Label: 

#### Passage 525

Retrieved by: BM25, Hybrid RRF

> We replicate the language modeling experiment of BIBREF2 and BIBREF13 to benchmark the QRNN architecture for natural language sequence prediction. The experiment uses a standard preprocessed version of the Penn Treebank (PTB) by BIBREF25 .
> 
> We implemented a gated QRNN model with medium hidden size: 2 layers with 640 units in each layer. Both QRNN layers use a convolutional filter width INLINEFORM0 of two timesteps. While the “medium” models used in other work BIBREF2 , BIBREF13 consist of 650 units in each layer, it was more computationally convenient to use a multiple of 32. As the Penn Treebank is a relatively small dataset, preventing overfitting is of considerable importance and a major focus of recent research. It is not obvious in advance which of the many RNN regularization schemes would perform well when applied to the QRNN. Our tests showed encouraging results from zoneout applied to the QRNN's recurrent pooling layer, implemented as described in Section SECREF5 .
> 
> The experimental settings largely followed the “medium” setup of BIBREF2 . Optimization was performed by stochastic gradient descent (SGD) without momentum. The learning rate was set at 1 for six epochs, then decayed by 0.95 for each subsequent epoch, for a total of 72 epochs. We additionally used INLINEFORM0 regularization of INLINEFORM1 and rescaled gradients with norm above 10. Zoneout was applied by performing dropout with ratio 0.1 on the forget gates of the QRNN, without rescaling the output of the dropout function. Batches consist of 20 examples, each 105 timesteps.
> 
> Comparing our results on the gated QRNN with zoneout to the results of LSTMs with both ordinary and variational dropout in Table TABREF14 , we see that the QRNN is highly competitive. The QRNN without zoneout strongly outperforms both our medium LSTM and the medium LSTM of BIBREF2 which do not use recurrent dropout and is even competitive with variational LSTMs. This may be due to the limited computational capacity that the QRNN's pooling layer has relative to the LSTM's recurrent weights, providing structural regularization over the recurrence.
> 
> Without zoneout, early stopping based upon validation loss was required as the QRNN would begin overfitting. By applying a small amount of zoneout ( INLINEFORM0 ), no early

#### Relevance 525

Label: 

#### Passage 526

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Each layer of a quasi-recurrent neural network consists of two kinds of subcomponents, analogous to convolution and pooling layers in CNNs. The convolutional component, like convolutional layers in CNNs, allows fully parallel computation across both minibatches and spatial dimensions, in this case the sequence dimension. The pooling component, like pooling layers in CNNs, lacks trainable parameters and allows fully parallel computation across minibatch and feature dimensions.
> 
> Given an input sequence INLINEFORM0 of INLINEFORM1 INLINEFORM2 -dimensional vectors INLINEFORM3 , the convolutional subcomponent of a QRNN performs convolutions in the timestep dimension with a bank of INLINEFORM4 filters, producing a sequence INLINEFORM5 of INLINEFORM6 -dimensional candidate vectors INLINEFORM7 . In order to be useful for tasks that include prediction of the next token, the filters must not allow the computation for any given timestep to access information from future timesteps. That is, with filters of width INLINEFORM8 , each INLINEFORM9 depends only on INLINEFORM10 through INLINEFORM11 . This concept, known as a masked convolution BIBREF11 , is implemented by padding the input to the left by the convolution's filter size minus one.
> 
> We apply additional convolutions with separate filter banks to obtain sequences of vectors for the elementwise gates that are needed for the pooling function. While the candidate vectors are passed through a INLINEFORM0 nonlinearity, the gates use an elementwise sigmoid. If the pooling function requires a forget gate INLINEFORM1 and an output gate INLINEFORM2 at each timestep, the full set of computations in the convolutional component is then: DISPLAYFORM0
> 
> where INLINEFORM0 , INLINEFORM1 , and INLINEFORM2 , each in INLINEFORM3 , are the convolutional filter banks and INLINEFORM4 denotes a masked convolution along the timestep dimension. Note that if the filter width is 2, these equations reduce to the LSTM-like DISPLAYFORM0
> 
> Convolution filters of larger width effectively compute higher INLINEFORM0 -gram features at each timestep; thus larger widths are especially important for character-level tasks.
> 
> Suitable functions for the pooling subcomponent can be constructed from the familiar elementwise gates of the traditional LSTM cell. We seek a function controlled by gates that can mix states across timesteps, but which acts independently on each channel of the state vector. The simplest option, which BIBREF12 term “dynamic average

#### Relevance 526

Label: 

#### Passage 528

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> We evaluate the QRNN architecture on a popular document-level sentiment classification benchmark, the IMDb movie review dataset BIBREF17 . The dataset consists of a balanced sample of 25,000 positive and 25,000 negative reviews, divided into equal-size train and test sets, with an average document length of 231 words BIBREF18 . We compare only to other results that do not make use of additional unlabeled data (thus excluding e.g., BIBREF19 ).
> 
> Our best performance on a held-out development set was achieved using a four-layer densely-connected QRNN with 256 units per layer and word vectors initialized using 300-dimensional cased GloVe embeddings BIBREF20 . Dropout of 0.3 was applied between layers, and we used INLINEFORM0 regularization of INLINEFORM1 . Optimization was performed on minibatches of 24 examples using RMSprop BIBREF21 with learning rate of INLINEFORM2 , INLINEFORM3 , and INLINEFORM4 .
> 
> Small batch sizes and long sequence lengths provide an ideal situation for demonstrating the QRNN's performance advantages over traditional recurrent architectures. We observed a speedup of 3.2x on IMDb train time per epoch compared to the optimized LSTM implementation provided in NVIDIA's cuDNN library. For specific batch sizes and sequence lengths, a 16x speed gain is possible. Figure FIGREF15 provides extensive speed comparisons.
> 
> In Figure FIGREF12 , we visualize the hidden state vectors INLINEFORM0 of the final QRNN layer on part of an example from the IMDb dataset. Even without any post-processing, changes in the hidden state are visible and interpretable in regards to the input. This is a consequence of the elementwise nature of the recurrent pooling function, which delays direct interaction between different channels of the hidden state until the computation of the next QRNN layer.

#### Relevance 528

Label: 

#### Passage 529

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> familiar elementwise gates of the traditional LSTM cell. We seek a function controlled by gates that can mix states across timesteps, but which acts independently on each channel of the state vector. The simplest option, which BIBREF12 term “dynamic average pooling”, uses only a forget gate: DISPLAYFORM0
> 
> We term these three options f-pooling, fo-pooling, and ifo-pooling respectively; in each case we initialize INLINEFORM0 or INLINEFORM1 to zero. Although the recurrent parts of these functions must be calculated for each timestep in sequence, their simplicity and parallelism along feature dimensions means that, in practice, evaluating them over even long sequences requires a negligible amount of computation time.
> 
> A single QRNN layer thus performs an input-dependent pooling, followed by a gated linear combination of convolutional features. As with convolutional neural networks, two or more QRNN layers should be stacked to create a model with the capacity to approximate more complex functions.

#### Relevance 529

Label: 

#### Passage 531

Retrieved by: Dense, Hybrid RRF

> The modified log-probability ranking criterion we used in beam search for translation experiments is: DISPLAYFORM0
> 
> where INLINEFORM0 is a length normalization parameter BIBREF34 , INLINEFORM1 is the INLINEFORM2 th output character, and INLINEFORM3 is a “target length” equal to the source sentence length plus five characters. This reduces at INLINEFORM4 to ordinary beam search with probabilities: DISPLAYFORM0
> 
> and at INLINEFORM0 to beam search with probabilities normalized by length (up to the target length): DISPLAYFORM0
> 
> Conveniently, this ranking criterion can be computed at intermediate beam-search timesteps, obviating the need to apply a separate reranking on complete hypotheses.

#### Relevance 531

Label: 

### BM25

#### Passage 527

Retrieved by: BM25

> Exploring alternatives to traditional RNNs for sequence tasks is a major area of current research. Quasi-recurrent neural networks are related to several such recently described models, especially the strongly-typed recurrent neural networks (T-RNN) introduced by BIBREF12 . While the motivation and constraints described in that work are different, BIBREF12 's concepts of “learnware” and “firmware” parallel our discussion of convolution-like and pooling-like subcomponents. As the use of a fully connected layer for recurrent connections violates the constraint of “strong typing”, all strongly-typed RNN architectures (including the T-RNN, T-GRU, and T-LSTM) are also quasi-recurrent. However, some QRNN models (including those with attention or skip-connections) are not “strongly typed”. In particular, a T-RNN differs from a QRNN as described in this paper with filter size 1 and f-pooling only in the absence of an activation function on INLINEFORM0 . Similarly, T-GRUs and T-LSTMs differ from QRNNs with filter size 2 and fo- or ifo-pooling respectively in that they lack INLINEFORM1 on INLINEFORM2 and use INLINEFORM3 rather than sigmoid on INLINEFORM4 .
> 
> The QRNN is also related to work in hybrid convolutional–recurrent models. BIBREF31 apply CNNs at the word level to generate INLINEFORM0 -gram features used by an LSTM for text classification. BIBREF32 also tackle text classification by applying convolutions at the character level, with a stride to reduce sequence length, then feeding these features into a bidirectional LSTM. A similar approach was taken by BIBREF10 for character-level machine translation. Their model's encoder uses a convolutional layer followed by max-pooling to reduce sequence length, a four-layer highway network, and a bidirectional GRU. The parallelism of the convolutional, pooling, and highway layers allows training speed comparable to subword-level models without hard-coded text segmentation.
> 
> The QRNN encoder–decoder model shares the favorable parallelism and path-length properties exhibited by the ByteNet BIBREF33 , an architecture for character-level machine translation based on residual convolutions over binary trees. Their model was constructed to achieve three desired properties: parallelism, linear-time computational complexity, and short paths between any pair of words in order to better propagate gradient signals.

#### Relevance 527

Label: 

### Dense

#### Passage 530

Retrieved by: Dense

> relative to the LSTM's recurrent weights, providing structural regularization over the recurrence.
> 
> Without zoneout, early stopping based upon validation loss was required as the QRNN would begin overfitting. By applying a small amount of zoneout ( INLINEFORM0 ), no early stopping is required and the QRNN achieves competitive levels of perplexity to the variational LSTM of BIBREF13 , which had variational inference based dropout of 0.2 applied recurrently. Their best performing variation also used Monte Carlo (MC) dropout averaging at test time of 1000 different masks, making it computationally more expensive to run.
> 
> When training on the PTB dataset with an NVIDIA K40 GPU, we found that the QRNN is substantially faster than a standard LSTM, even when comparing against the optimized cuDNN LSTM. In Figure FIGREF15 we provide a breakdown of the time taken for Chainer's default LSTM, the cuDNN LSTM, and QRNN to perform a full forward and backward pass on a single batch during training of the RNN LM on PTB. For both LSTM implementations, running time was dominated by the RNN computations, even with the highly optimized cuDNN implementation. For the QRNN implementation, however, the “RNN” layers are no longer the bottleneck. Indeed, there are diminishing returns from further optimization of the QRNN itself as the softmax and optimization overhead take equal or greater time. Note that the softmax, over a vocabulary size of only 10,000 words, is relatively small; for tasks with larger vocabularies, the softmax would likely dominate computation time.
> 
> It is also important to note that the cuDNN library's RNN primitives do not natively support any form of recurrent dropout. That is, running an LSTM that uses a state-of-the-art regularization scheme at cuDNN-like speeds would likely require an entirely custom kernel.

#### Relevance 530

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 532

Retrieved by: Hybrid RRF followed by BGE reranking

> Recurrent neural networks (RNNs), including gated variants such as the long short-term memory (LSTM) BIBREF0 have become the standard model architecture for deep learning approaches to sequence modeling tasks. RNNs repeatedly apply a function with trainable parameters to a hidden state. Recurrent layers can also be stacked, increasing network depth, representational power and often accuracy. RNN applications in the natural language domain range from sentence classification BIBREF1 to word- and character-level language modeling BIBREF2 . RNNs are also commonly the basic building block for more complex models for tasks such as machine translation BIBREF3 , BIBREF4 , BIBREF5 or question answering BIBREF6 , BIBREF7 . Unfortunately standard RNNs, including LSTMs, are limited in their capability to handle tasks involving very long sequences, such as document classification or character-level machine translation, as the computation of features or states for different parts of the document cannot occur in parallel.
> 
> Convolutional neural networks (CNNs) BIBREF8 , though more popular on tasks involving image data, have also been applied to sequence encoding tasks BIBREF9 . Such models apply time-invariant filter functions in parallel to windows along the input sequence. CNNs possess several advantages over recurrent models, including increased parallelism and better scaling to long sequences such as those often seen with character-level language data. Convolutional models for sequence processing have been more successful when combined with RNN layers in a hybrid architecture BIBREF10 , because traditional max- and average-pooling approaches to combining convolutional features across timesteps assume time invariance and hence cannot make full use of large-scale sequence order information.
> 
> We present quasi-recurrent neural networks for neural sequence modeling. QRNNs address both drawbacks of standard models: like CNNs, QRNNs allow for parallel computation across both timestep and minibatch dimensions, enabling high throughput and good scaling to long sequences. Like RNNs, QRNNs allow the output to depend on the overall order of elements in the sequence. We describe QRNN variants tailored to several natural language tasks, including document-level sentiment classification, language modeling, and character-level machine translation. These models outperform strong LSTM baselines on all three tasks while dramatically reducing computation time.

#### Relevance 532

Label: 

## Question 0059

Paper: Clotho: An Audio Captioning Dataset

> What domain do the audio samples fall under?

### Common Retrieved Chunks

#### Passage 533

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> word labels (by AudioSet) and viewed the accompanying videos of the audio samples.
> 
> The perceptual ambiguity of sounds can be hampered by providing contextual information (e.g. word labels) to annotators, making them aware of the actual source and not letting them describe their own perceived information. Using visual stimuli (e.g. video) introduces a bias, since annotators may describe what they see and not what they hear. Also, a single caption per file impedes the learning and evaluation of diverse descriptions of information, and domain-specific data of previous audio captioning datasets have an observed significant impact on the performance of methods BIBREF5. Finally, unique words (i.e. words appearing only once) affect the learning process, as they have an impact on the evaluation process (e.g. if a word is unique, will be either on training or on evaluation). An audio captioning dataset should at least provide some information on unique words contained in its captions.
> 
> In this paper we present the freely available audio captioning dataset Clotho, with 4981 audio samples and 24 905 captions. All audio samples are from Freesound platform BIBREF8, and are of duration from 15 to 30 seconds. Each audio sample has five captions of eight to 20 words length, collected by AMT and a specific protocol for crowdsourcing audio annotations, which ensures diversity and reduced grammatical errors BIBREF0. During annotation no other information but the audio signal was available to the annotators, e.g. video or word tags. The rest of the paper is organized as follows. Section SECREF2 presents the creation of Clotho, i.e. gathering and processing of the audio samples and captions, and the splitting of the data to development, evaluation, and testing splits. Section SECREF3 presents the baseline method used, the process followed for its evaluation using Clotho, and the obtained results. Section SECREF4 concludes the paper.

#### Relevance 533

Label: 

#### Passage 534

Retrieved by: BM25, Hybrid RRF

> In this work we present a novel dataset for audio captioning, named Clotho, that contains 4981 audio samples and five captions for each file (totaling to 24 905 captions). During the creating of Clotho care has been taken in order to promote diversity of captions, eliminate words that appear only once and named entities, and provide data splits that do not hamper the training or evaluation process. Also, there is an example of the usage of Clotho, using a method proposed at the original work of audio captioning. The baseline results indicate that the baseline method started learning the content of the input audio, but more tuning is needed in order to express the content properly. Future work includes the employment of Clotho and development of novel methods for audio captioning.

#### Relevance 534

Label: 

#### Passage 535

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Captioning is the intermodal translation task of describing the human-perceived information in a medium, e.g. images (image captioning) or audio (audio captioning), using free text BIBREF0, BIBREF1, BIBREF2, BIBREF3. In particular, audio captioning was first introduced in BIBREF3, it does not involve speech transcription, and is focusing on identifying the human-perceived information in an general audio signal and expressing it through text, using natural language. This information includes identification of sound events, acoustic scenes, spatiotemporal relationships of sources, foreground versus background discrimination, concepts, and physical properties of objects and environment. For example, given an audio signal, an audio captioning system would be able to generate captions like “a door creaks as it slowly revolves back and forth”.
> 
> The dataset used for training an audio captioning method defines to a great extent what the method can learn BIBREF0, BIBREF4. Diversity in captions allows the method to learn and exploit the perceptual differences on the content (e.g. a thin plastic rattling could be perceived as a fire crackling) BIBREF0. Also, the evaluation of the method becomes more objective and general by having more captions per audio signal BIBREF4.
> 
> Recently, two different datasets for audio captioning were presented, Audio Caption and AudioCaps BIBREF5, BIBREF6. Audio Caption is partially released, and contains 3710 domain-specific (hospital) video clips with their audio tracks, and annotations that were originally obtained in Mandarin Chinese and afterwards translated to English using machine translation BIBREF5. The annotators had access and viewed the videos. The annotations contain description of the speech content (e.g. “The patient inquired about the location of the doctor’s police station”). AudioCaps dataset has 46 000 audio samples from AudioSet BIBREF7, annotated with one caption each using the crowdsourcing platform Amazon Mechanical Turk (AMT) and automated quality and location control of the annotators BIBREF6. Authors of AudioCaps did not use categories of sounds which they claimed that visuals were required for correct recognition, e.g. “inside small room”. Annotators of AudioCaps were provided the word labels (by AudioSet) and viewed the accompanying videos of the audio samples.
> 
> The perceptual ambiguity of sounds can be hampered by providing contextual information (e.g. word labels) to annotators, making them aware of the actual source and not letting

#### Relevance 535

Label: 

#### Passage 537

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We collect the set of audio samples $\mathbb {X}_{\text{init}}=\lbrace \mathbf {x}_{\text{init}}^{i}\rbrace _{i=1}^{N_{\text{init}}}$, with $N_{\text{init}}=12000$ and their corresponding metadata (e.g. tags that indicate their content, and a short textual description), from the online platform Freesound BIBREF8. $\mathbf {x}_{\text{init}}$ was obtained by randomly sampling audio files from Freesound fulfilling the following criteria: lossless file type, audio quality at least 44.1 kHz and 16-bit, duration $10\text{ s}\le d({\mathbf {x}_{\text{init}}^{i}})\le 300$ s (where $d(\mathbf {x})$ is the duration of $\mathbf {x}$), a textual description which first sentence does not have spelling errors according to US and UK English dictionaries (as an indication of the correctness of the metadata, e.g. tags), and not having tags that indicate music, sound effects, or speech. As tags indicating speech files we consider those like “speech”, “speak”, and “woman”. We normalize $\mathbf {x}^{i}_{\text{init}}$ to the range $[-1, 1]$, trim the silence (60 dB below the maximum amplitude) from the beginning and end, and resample to 44.1 kHz. Finally, we keep samples that are longer than 15 s as a result of the processing. This results in $\mathbb {X}^{\prime }_{\text{init}}=\lbrace \mathbf {x}_{\text{init}}^{j}\rbrace _{j=1}^{N^{\prime }_{\text{init}}},\,N^{\prime }_{\text{init}}=9000$.
> 
> For enhancing the diversity of the audio content, we aim to create $\mathbb {X}_{\text{med}}\subset \mathbb {X}^{\prime }_{\text{init}}$ based on the tags of $\mathbb {X}^{\prime }_{\text{init}}$, targeting to the most uniform possible distribution of the tags of the audio samples in $\mathbb {X}_{\text{med}}$. We first create the bag of tags $\mathbb {T}$ by collecting all the tags of sounds in $\mathbb {X}^{\prime }_{\text{init}}$. We omit tags that describe time or recording equipment and process (e.g. “autumn”, “field-recording”). Then, we calculate the normalized frequency of all tags in $\mathbb {T}$ and create $\mathbb {T}_{\text{0.01}}\subset \mathbb {T}$, with tags of a normalized frequency of at least 0.01. We randomly sample $10^6$ sets (with overlap) of $N_{\text{med}}=5000$ files from $\mathbb {X}^{\prime }_{\text{init}}$, and keep the set that has the maximum entropy for $\mathbb {T}_{\text{0.01}}$. This process results in $\mathbb {X}_{\text{med}}=\lbrace \mathbf {x}_{\text{init}}^{z}\rbrace _{z=1}^{N_{\text{med}}}$, having the most uniform tag distribution and, hence, the most diverse content. The resulting distribution of the tags in $\mathbb {T}_{\text{0.01}}$ is illustrated in Figure FIGREF5. The 10 most common tags are: ambient, water, nature, birds, noise, rain, city, wind, metal,

#### Relevance 537

Label: 

#### Passage 539

Retrieved by: Dense, Hybrid RRF

> mechanism, decoder, and the classifier, using 150 epochs, the cross entropy loss, and Adam optimizer BIBREF11 with proposed hyper-parameters. Also, in each batch we pad the captions of the batch to the longest in the same batch, using the end-of-sequence token, and the input audio features to the longest ones, by prepending zeros.
> 
> We assess the performance of the method on evaluation and testing splits, using the machine translation metrics BLEU$n$ (with $n=1,\ldots ,4$), METEOR, CIDEr, and ROUGEL for comparing the output of the method and the reference captions for the input audio sample. In a nutshell, BLEU$n$ measures a modified precision of $n$-grams (e.g. BLEU2 for 2-grams), METEOR measures a harmonic mean-based score of the precision and recall for unigrams, CIDEr measures a weighted cosine similarity of $n$-grams, and ROUGEL is a longest common subsequence-based score.
> 
> In Table TABREF13 are the scores of the employed metrics for the evaluation and testing splits.
> 
> As can be seen from Table TABREF13 and BLEU1, the method has started identifying the content of the audio samples by outputting words that exist in the reference captions. For example, the method outputs “water is running into a container into a”, while the closest reference caption is “water pouring into a container with water in it already”, or “birds are of chirping the chirping and various chirping” while the closest reference is “several different kinds of birds are chirping and singing”. The scores of the rest metrics reveal that the structure of the sentence and order of the words are not correct. These are issues that can be tackled by adopting either a pre-calculated or jointly learnt language model. In any case, the results show that the Clotho dataset can effectively be used for research on audio captioning, posing useful data in tackling the challenging task of audio content description.

#### Relevance 539

Label: 

### BM25

#### Passage 536

Retrieved by: BM25

> The research leading to these results has received funding from the European Research Council under the European Union’s H2020 Framework Programme through ERC Grant Agreement 637422 EVERYSOUND. Part of the computations leading to these results were performed on a TITAN-X GPU donated by NVIDIA to K. Drossos. The authors also wish to acknowledge CSC-IT Center for Science, Finland, for computational resources.

#### Relevance 536

Label: 

### Dense

#### Passage 538

Retrieved by: Dense

> Otherwise, we remove completely the audio sample. This process yields the final set of audio samples and captions, $\mathbb {X}=\lbrace \mathbf {x}^{o}\rbrace _{o=1}^{N}$ and $\mathbb {C}^{\prime }=\lbrace \mathbb {C}^{\prime o}\rbrace _{o=1}^{N}$, respectively, with $\mathbb {C}^{\prime o}=\lbrace c^{\prime o,u}\rbrace _{u=1}^{N_{\text{cp}}}$ and $N=4981$.
> 
> An audio sample should belong to only one split of data (e.g., training, development, testing). This means that if a word appears only at the captions of one $\mathbf {x}^{o}$, then this word will be appearing only at one of the splits. Having a word appearing only in training split leads to sub-optimal learning procedure, because resources are spend to words unused in validation and testing. If a word is not appearing in the training split, then the evaluation procedure suffers by having to evaluate on words not known during training. For that reason, for each $\mathbf {x}^{o}$ we construct the set of words $\mathbb {S}_{a}^{o}$ from $\mathbb {C}^{\prime o}$. Then, we merge all $\mathbb {S}_{a}^{o}$ to the bag $\mathbb {S}_{T}$ and we identify all words that appear only once (i.e. having a frequency of one) in $\mathbb {S}_{T}$. We employ an extra annotator (not from AMT) which has access only to the captions of $\mathbf {x}^{o}$, and has the instructions to change the all words in $\mathbb {S}_{T}$ with frequency of one, with other synonym words in $\mathbb {S}_{T}$ and (if necessary) rephrase the caption. The result is the set of captions $\mathbb {C}=\lbrace \mathbb {C}^{o}\rbrace _{o=1}^{N}$, with words in $\mathbb {S}_{T}$ having a frequency of at least two. Each word will appear in the development set and at least in one of the evaluation or testing splits. This process yields the data of the Clotho dataset, $\mathbb {D}=\lbrace \left<\mathbf {x}^{o}, \mathbb {C}^{o}\right>\rbrace _{o=1}^{N}$.

#### Relevance 538

Label: 

#### Passage 540

Retrieved by: Dense

> In order to provide an example of how to employ Clotho and some initial (baseline) results, we use a previously utilized method for audio captioning BIBREF3 which is based on an encoder-decoder scheme with attention. The method accepts as an input a length-$T$ sequence of 64 log mel-band energies $\mathbf {X}\in \mathbb {R}^{T\times 64}$, which is used as an input to a DNN which outputs a probability distribution of words. The generated caption is constructed from the output of the DNN, as in BIBREF3. We optimize the parameters of the method using the development split of Clotho and we evaluate it using the evaluation and the testing splits, separately.
> 
> We first extract 64 log mel-band energies, using a Hamming window of 46 ms, with 50% overlap. We tokenize the captions of the development split, using a one-hot encoding of the words. Since all the words in in the development split appear in the other two splits as well, there are no unknown tokens/words. We also employ the start- and end-of-sequence tokens ($\left<\text{SOS}\right>$ and $\left<\text{EOS}\right>$ respectively), in order to signify the start and end of a caption.
> 
> The encoder is a series of bi-directional gated recurrent units (bi-GRUs) BIBREF10, similarly to BIBREF3. The output dimensionality for the GRU layers (forward and backward GRUs have same dimensionality) is $\lbrace 256, 256, 256\rbrace $. The output of the encoder is processed by an attention mechanism and its output is given as an input to the decoder. The attention mechanism is a feed-forward neural network (FNN) and the decoder a GRU. Then, the output of the decoder is given as an input to another FNN with a softmax non-linearity, which acts as a classifier and outputs the probability distribution of words for the $i$-th time-step. To optimize the parameters of the employed method, we use five times each audio sample, using its five different captions as targeted outputs each time. We optimize jointly the parameters of the encoder, attention mechanism, decoder, and the classifier, using 150 epochs, the cross entropy loss, and Adam optimizer BIBREF11 with proposed hyper-parameters. Also, in each batch we pad the captions of the batch to the longest in the same batch, using the end-of-sequence

#### Relevance 540

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 541

Retrieved by: Hybrid RRF followed by BGE reranking

> the most uniform tag distribution and, hence, the most diverse content. The resulting distribution of the tags in $\mathbb {T}_{\text{0.01}}$ is illustrated in Figure FIGREF5. The 10 most common tags are: ambient, water, nature, birds, noise, rain, city, wind, metal, and people.
> 
> We target at audio samples $\mathbf {x}$ having a uniform distribution between 15 and 30 s. Thus, we further process $\mathbb {X}_{\text{med}}$, keeping the files with a maximum duration of 30 s and cutting a segment from the rest. We randomly select a set of values for the duration of the segments that will maximize the entropy of the duration of the files, discretizing the durations with a resolution of 0.05 s. In order to not pick segment without activity, we sample the files by taking a window with a selected duration that maximizes the energy of the sample. Finally, we apply a 512-point Hamming window to the beginning and the end of the samples, smoothing the effect of sampling. The above process results to $\mathbb {X}_{\text{sam}}=\lbrace \mathbf {x}_{\text{sam}}^{z}\rbrace _{z=1}^{N_{\text{med}}}$, where the distribution of durations is approximately uniform between 15 and 30 s.

#### Relevance 541

Label: 

#### Passage 542

Retrieved by: Hybrid RRF followed by BGE reranking

> We use AMT and a novel three-step based framework BIBREF0 for crowdsourcing the annotation of $\mathbb {X}_{\text{sam}}$, acquiring the set of captions $\mathbb {C}_{\text{sam}}^{z}=\lbrace c_{\text{sam}}^{z,u}\rbrace _{u=1}^{N_{\text{cp}}}$ for each $\mathbf {x}_{\text{sam}}^{z}$, where $c_{\text{sam}}^{z,u}$ is an eight to 20 words long caption for $\mathbf {x}_{\text{sam}}^{z}$. In a nutshell, each audio sample $\mathbf {x}_{\text{sam}}^{z}$ gets annotated by $N_{\text{cp}}$ different annotators in the first step of the framework. The annotators have access only to $\mathbf {x}_{\text{sam}}^{z}$ and not any other information. In the second step, different annotators are instructed to correct any grammatical errors, typos, and/or rephrase the captions. This process results in $2\times N_{\text{cp}}$ captions per $\mathbf {x}_{\text{sam}}^{z}$. Finally, three (again different) annotators have access to $\mathbf {x}_{\text{sam}}^{z}$ and its $2\times N_{\text{cp}}$ captions, and score each caption in terms of the accuracy of the description and fluency of English, using a scale from 1 to 4 (the higher the better). The captions for each $\mathbf {x}_{\text{sam}}^{z}$ are sorted (first according to accuracy of description and then according to fluency), and two groups are formed: the top $N_{\text{cp}}$ and the bottom $N_{\text{cp}}$ captions. The top $N_{\text{cp}}$ captions are selected as $\mathbb {C}_{\text{sam}}^{z}$. We manually sanitize further $\mathbb {C}_{\text{sam}}^{z}$, e.g. by replacing “it's” with “it is” or “its”, making consistent hyphenation and compound words (e.g. “nonstop”, “non-stop”, and “non stop”), removing words or rephrasing captions pertaining to the content of speech (e.g. “French”, “foreign”), and removing/replacing named entities (e.g. “Windex”).
> 
> Finally, we observe that some captions include transcription of speech. To remove it, we employ extra annotators (not from AMT) which had access only at the captions. We instruct the annotators to remove the transcribed speech and rephrase the caption. If the result is less than eight words, we check the bottom $N_{\text{cp}}$ captions for that audio sample. If they include a caption that has been rated with at least 3 by all the annotators for both accuracy and fluency, and does not contain transcribed speech, we use that caption. Otherwise, we remove completely the audio sample. This process yields the final set of audio samples and captions, $\mathbb {X}=\lbrace \mathbf {x}^{o}\rbrace _{o=1}^{N}$ and $\mathbb {C}^{\prime }=\lbrace \mathbb {C}^{\prime o}\rbrace _{o=1}^{N}$, respectively, with $\mathbb {C}^{\prime o}=\lbrace c^{\prime o,u}\rbrace _{u=1}^{N_{\text{cp}}}$ and

#### Relevance 542

Label: 

## Question 0060

Paper: Automatic Judgment Prediction via Legal Reading Comprehension

> what is the size of the real-world civil case dataset?

### Common Retrieved Chunks

#### Passage 543

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> improvement is quite limited compared to that in previous work BIBREF3 for the following reasons: (1) As mentioned above, most case documents only contain coarse-grained articles, and only a small number of them contain fine-grained ones, which has limited information in themselves. (2) Unlike in criminal cases where the application of an article indicates the corresponding crime, law articles in civil cases work as reference, and can be applied in both the cases of supports and rejects. As law articles cut both ways for the judgment result, this is one of the characteristics that distinguishes civil cases from criminal ones. We also need to remember that, the performance of INLINEFORM1 in accuracy or INLINEFORM2 in F1 score is unattainable in real-world setting for automatic prediction where ground-truth articles are not available.
> 
> In the area of civil cases, the understanding of the case materials and how they interact is a critical factor. The inclusion of law articles is not enough. As is shown in Table TABREF38 , compared to feeding the model with an un-selected set of law articles, taking away the reading mechanism results in greater performance drop. Therefore, the ability to read, understand and select relevant information from the complex multi-sourced case materials is necessary. It's even more important in real world since we don't have access to ground-truth law articles to make predictions.

#### Relevance 543

Label: 

#### Passage 544

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> We employ Jieba for Chinese word segmentation and keep the top INLINEFORM0 frequent words. The word embedding size is set to 128 and the other low-frequency words are replaced with the mark <UNK>. The hidden size of GRU is set to 128 for each direction in Bi-GRU. In the pair-wise attentive reader, the hidden state is set to 256 for mGRu. In the CNN layer, filter windows are set to 1, 3, 4, and 5 with each filter containing 200 feature maps. We add a dropout layer BIBREF38 after the CNN layer with a dropout rate of INLINEFORM1 . We use Adam BIBREF32 for training and set learning rate to INLINEFORM2 , INLINEFORM3 to INLINEFORM4 , INLINEFORM5 to INLINEFORM6 , INLINEFORM7 to INLINEFORM8 , batch size to 64. We employ precision, recall, F1 and accuracy for evaluation metrics. We repeat all the experiments for 10 times, and report the average results.

#### Relevance 544

Label: 

#### Passage 545

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> account law articles and their corresponding juridical interpretations. We also implement and evaluate previous methods on our dataset, which prove to be strong baselines.
> 
> Our experiment results show significant improvements over previous methods. Further experiments demonstrate that our model also achieves considerable improvement over other off-the-shelf state-of-the-art models under classification and question answering framework respectively. Ablation tests carried out by taking off some components of our model further prove its robustness and effectiveness.
> 
> To sum up, our contributions are as follows:
> 
> (1) We introduce reading mechanism and re-formalize judgment prediction as Legal Reading Comprehension to better model the complementary inputs.
> 
> (2) We construct a real-world dataset for experiments, and plan to publish it for further research.
> 
> (3) Besides baselines from previous works, we also carry out comprehensive experiments comparing different existing deep neural network methods on our dataset. Supported by these experiments, improvements achieved by LRC prove to be robust.

#### Relevance 545

Label: 

#### Passage 546

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> provide better an environment for children's growth as well as parents' financial condition. Here, different pleas are independent.
> 
> Heterogeneity of Input Triple. Inputs to a judgment prediction system consist of three heterogeneous yet complementary parts, i.e., fact description, plaintiff's plea, and related law articles. Concatenating them together and treating them simply as a sequence of words as in previous works BIBREF2 , BIBREF1 would cause a great loss of information. This is the same in question-answering where the dual inputs, i.e., query and passage, should be modeled separately.
> 
> Despite the introduction of the neural networks that can learn better semantic representations of input text, it remains unsolved to incorporate proper mechanisms to integrate the complementary triple of pleas, fact descriptions, and law articles together.
> 
> Inspired by recent advances in question answering (QA) based reading comprehension (RC) BIBREF5 , BIBREF6 , BIBREF7 , BIBREF8 , we propose the Legal Reading Comprehension (LRC) framework for automatic judgment prediction. LRC incorporates the reading mechanism for better modeling of the complementary inputs above-mentioned, as is done by human judges when referring to legal materials in search of supporting law articles. Reading mechanism, by simulating how human connects and integrates multiple text, has proven an effective module in RC tasks. We argue that applying the reading mechanism in a proper way among the triplets can obtain a better understanding and more informative representation of the original text, and further improve performance . To instantiate the framework, we propose an end-to-end neural network model named AutoJudge.
> 
> For experiments, we train and evaluate our models in the civil law system of mainland China. We collect and construct a large-scale real-world data set of INLINEFORM0 case documents that the Supreme People's Court of People's Republic of China has made publicly available. Fact description, pleas, and results can be extracted easily from these case documents with regular expressions, since the original documents have special typographical characteristics indicating the discourse structure. We also take into account law articles and their corresponding juridical interpretations. We also implement and evaluate previous methods on our dataset, which prove to be strong baselines.
> 
> Our experiment results show significant improvements over previous methods. Further experiments demonstrate that our model also

#### Relevance 546

Label: 

#### Passage 548

Retrieved by: Dense, Hybrid RRF

> Since none of the datasets from previous works have been published, we decide to build a new one. We randomly collect INLINEFORM0 cases from China Judgments Online, among which INLINEFORM1 cases are for training, INLINEFORM2 each for validation and testing. Among the original cases, INLINEFORM3 are granted divorce and others not. There are INLINEFORM4 valid pleas in total, with INLINEFORM5 supported and INLINEFORM6 rejected. Note that, if the divorce plea in a case is not granted, the other pleas of this case will not be considered by the judge. Case materials are all natural language sentences, with averagely INLINEFORM7 tokens per fact description and INLINEFORM8 per plea. There are 62 relevant law articles in total, each with INLINEFORM9 tokens averagely. Note that the case documents include special typographical signals, making it easy to extract labeled data with regular expression.
> 
> We apply some rules with legal prior to preprocess the dataset according to previous works BIBREF33 , BIBREF34 , BIBREF35 , which have proved effective in our experiments.
> 
> Name Replacement: All names in case documents are replaced with marks indicating their roles, instead of simply anonymizing them, e.g. <Plantiff>, <Defendant>, <Daughter_x> and so on. Since “all are equal before the law”, names should make no more difference than what role they take.
> 
> Law Article Filtration : Since most accessible divorce proceeding documents do not contain ground-truth fine-grained articles, we use an unsupervised method instead. First, we extract all the articles from the law text with regular expression. Afterwards, we select the most relevant 10 articles according to the fact descriptions as follows. We obtain sentence representation with CBOW BIBREF36 , BIBREF37 weighted by inverse document frequency, and calculate cosine distance between cases and law articles. Word embeddings are pre-trained with Chinese Wikipedia pages. As the final step, we extract top 5 relevant articles for each sample respectively from the main marriage law articles and their interpretations, which are equally important. We manually check the extracted articles for 100 cases to ensure that the extraction quality is fairly good and acceptable.
> 
> The filtration process is automatic and fully unsupervised since the original documents have no ground-truth labels for fine-grained law articles, and coarse-grained law-articles only provide limited

#### Relevance 548

Label: 

#### Passage 549

Retrieved by: Dense, Hybrid RRF

> Automatic judgment prediction is to train a machine judge to determine whether a certain plea in a given civil case would be supported or rejected. In countries with civil law system, e.g. mainland China, such process should be done with reference to related law articles and the fact description, as is performed by a human judge. The intuition comes from the fact that under civil law system, law articles act as principles for juridical judgments. Such techniques would have a wide range of promising applications. On the one hand, legal consulting systems could provide better access to high-quality legal resources in a low-cost way to legal outsiders, who suffer from the complicated terminologies. On the other hand, machine judge assistants for professionals would help improve the efficiency of the judicial system. Besides, automated judgment system can help in improving juridical equality and transparency. From another perspective, there are currently 7 times much more civil cases than criminal cases in mainland China, with annual rates of increase of INLINEFORM0 and INLINEFORM1 respectively, making judgment prediction in civil cases a promising application BIBREF0 .
> 
> Previous works BIBREF1 , BIBREF2 , BIBREF3 , BIBREF4 formalize judgment prediction as the text classification task, regarding either charge names or binary judgments, i.e., support or reject, as the target classes. These works focus on the situation where only one result is expected, e.g., the US Supreme Court's decisions BIBREF2 , and the charge name prediction for criminal cases BIBREF3 . Despite these recent efforts and their progress, automatic judgment prediction in civil law system is still confronted with two main challenges:
> 
> One-to-Many Relation between Case and Plea. Every single civil case may contain multiple pleas and the result of each plea is co-determined by related law articles and specific aspects of the involved case. For example, in divorce proceedings, judgment of alienation of mutual affection is the key factor for granting divorce but custody of children depends on which side can provide better an environment for children's growth as well as parents' financial condition. Here, different pleas are independent.
> 
> Heterogeneity of Input Triple. Inputs to a judgment prediction system consist of three heterogeneous yet complementary parts, i.e., fact description, plaintiff's plea,

#### Relevance 549

Label: 

#### Passage 550

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this paper, we explore the task of predicting judgments of civil cases. Comparing with conventional text classification framework, we propose Legal Reading Comprehension framework to handle multiple and complex textual inputs. Moreover, we present a novel neural model, AutoJudge, to incorporate law articles for judgment prediction. In experiments, we compare our model on divorce proceedings with various state-of-the-art baselines of various frameworks. Experimental results show that our model achieves considerable improvement than all the baselines. Besides, visualization results also demonstrate the effectiveness and interpretability of our proposed model.
> 
> In the future, we can explore the following directions: (1) Limited by the datasets, we can only verify our proposed model on divorce proceedings. A more general and larger dataset will benefit the research on judgment prediction. (2) Judicial decisions in some civil cases are not always binary, but more diverse and flexible ones, e.g. compensation amount. Thus, it is critical for judgment prediction to manage various judgment forms.

#### Relevance 550

Label: 

### BM25

#### Passage 547

Retrieved by: BM25

> for 100 cases to ensure that the extraction quality is fairly good and acceptable.
> 
> The filtration process is automatic and fully unsupervised since the original documents have no ground-truth labels for fine-grained law articles, and coarse-grained law-articles only provide limited information. We also experiment with the ground-truth articles, but only a small fraction of them has fine-grained ones, and they are usually not available in real-world scenarios.

#### Relevance 547

Label: 

### Dense

#### Passage 551

Retrieved by: Dense

> To evaluate the proposed LRC framework and the AutoJudge model, we carry out a series of experiments on the divorce proceedings, a typical yet complex field of civil cases. Divorce proceedings often come with several kinds of pleas, e.g. seeking divorce, custody of children, compensation, and maintenance, which focuses on different aspects and thus makes it a challenge for judgment prediction.

#### Relevance 551

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None
