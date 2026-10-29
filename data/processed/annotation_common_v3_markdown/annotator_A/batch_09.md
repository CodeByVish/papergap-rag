# Passage relevance annotation

Annotator: 

Enter your name or agreed identifier after `Annotator:`.

Judge whether each passage helps answer the question, including useful partial evidence. Topic overlap alone is insufficient.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Preserve all content and record numbers. Work independently; do not exchange labels before submission. Algorithm sources are disclosed.

## Question 0161

Paper: Distinguishing Antonyms and Synonyms in a Pattern-based Neural Network

> What dataset do they use to evaluate their method?

### Common Retrieved Chunks

#### Passage 1482

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In our models, the novel distance feature is successfully integrated along the syntactic path to represent lexico-syntactic patterns. The intuition behind the distance feature exploits properties of trees in graph theory, which show that there exist differences in the degree of relationship between the parent node and the child nodes ( $distance = 1$ ) and in the degree of relationship between the ancestor node and the descendant nodes ( $distance > 1$ ). Hence, we use the distance feature to effectively capture these relationships.
> 
> In order to evaluate the effect of our novel distance feature, we compare the distance feature to the direction feature proposed by Shwartz:16. In their approach, the authors combined lemma, POS, dependency, and direction features for the task of hypernym detection. The direction feature represented the direction of the dependency label between two nodes in a path from X to Y.
> 
> For evaluation, we make use of the same information regarding dataset and patterns as in Section "Overall Results" , and then replace the distance feature by the direction feature. The results are shown in Table 4 . The distance feature enhances the performance of our proposed models more effectively than the direction feature does, across all word classes.

#### Relevance 1482

Label: 

#### Passage 1483

Retrieved by: BM25, Dense, Hybrid RRF

> As a first baseline, we apply the approach by Roth2014, henceforth R&SiW. They used a vector space model to represent pairs of words by a combination of standard lexico-syntactic patterns and discourse markers. In addition to the patterns, the discourse markers added information to express discourse relations, which in turn may indicate the specific semantic relation between the two words in a word pair. For example, contrast relations might indicate antonymy, whereas elaborations may indicate synonymy or hyponymy.
> 
> Michael Roth, the first author of R&SiW, kindly computed the relation classification results of the pattern–discourse model for our test sets. The weights between marker-based and pattern-based models were tuned on the validation sets; other hyperparameters were set exactly as described by the R&SiW method.

#### Relevance 1483

Label: 

#### Passage 1484

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> For training the models, neural networks require a large amount of training data. We use the existing large-scale antonym and synonym pairs previously used by Nguyen:16. Originally, the data pairs were collected from WordNet BIBREF9 and Wordnik.
> 
> In order to induce patterns for the word pairs in the dataset, we identify the sentences in the corpus that contain the word pair. Thereafter, we extract all patterns for the word pair. We filter out all patterns which occur less than five times; and we only take into account word pairs that contain at least five patterns for training, validating and testing. For the proportion of positive and negative pairs, we keep a ratio of 1:1 positive (antonym) to negative (synonym) pairs in the dataset. In order to create the sets of training, testing and validation data, we perform random splitting with 70% train, 25% test, and 5% validation sets. The final dataset contains the number of word pairs according to word classes described in Table 1 . Moreover, Table 2 shows the average number of patterns for each word pair in our dataset.

#### Relevance 1484

Label: 

#### Passage 1485

Retrieved by: BM25, Dense, Hybrid RRF

> Table 3 shows the significant performance of our models in comparison to the baselines. Concerning adjectives, the two proposed models significantly outperform the two baselines: The performance of the baselines is around .72 for $F_1$ , and the corresponding results for the combined AntSynNET model achieve an improvement of $>$ .06. Regarding nouns, the improvement of the new methods is just .02 $F_1$ in comparison to the R&SiW baseline, but we achieve a much better performance in comparison to the SP baseline, an increase of .37 $F_1$ . Regarding verbs, we do not outperform the more advanced R&SiW baseline in terms of the $F_1$ score, but we obtain higher recall scores. In comparison to the SP baseline, our models still show a clear $F_1$ improvement.
> 
> Overall, our proposed models achieve comparatively high recall scores compared to the two baselines. This strengthens our hypothesis that there is a higher possibility for the co-occurrence of antonymous pairs in patterns over synonymous pairs within a sentence. Because, when the proposed models obtain high recall scores, the models are able to retrieve most relevant information (antonymous pairs) corresponding to the patterns. Regarding the low precision in the two proposed models, we sampled randomly 5 pairs in each population: true positive, true negative, false positive, false negative. We then compared the overlap of patterns for the true predictions (true positive pairs and true negative pairs) and the false predictions (false positive pairs and false negative pairs). We found out that there is no overlap between patterns of true predictions; and the number overlap between patterns of false predictions is 2, 2, and 4 patterns for noun, adjective, and verb classes, respectively. This shows that the low precision of our models stems from the patterns which represent both antonymous and synonymous pairs.

#### Relevance 1485

Label: 

#### Passage 1486

Retrieved by: BM25, Hybrid RRF

> The SP method proposed by Schwartz:15 uses symmetric patterns for generating word embeddings. In this work, the authors applied an unsupervised algorithm for the automatic extraction of symmetric patterns from plain text. The symmetric patterns were defined as a sequence of 3-5 tokens consisting of exactly two wildcards and 1-3 words. The patterns were filtered based on their frequencies, such that the resulting pattern set contained 11 patterns. For generating word embeddings, a matrix of co-occurrence counts between patterns and words in the vocabulary was computed, using positive point-wise mutual information. The sparsity problem of vector representations was addressed by smoothing. For antonym representation, the authors relied on two patterns suggested by Lin2003 to construct word embeddings containing an antonym parameter that can be turned on in order to represent antonyms as dissimilar, and that can be turned off to represent antonyms as similar.
> 
> To apply the SP method to our data, we make use of the pre-trained SP embeddings with 500 dimensions. We calculate the cosine similarity of word pairs and then use a Support Vector Machine with Radial Basis Function kernel to classify antonyms and synonyms.

#### Relevance 1486

Label: 

### BM25

None

### Dense

#### Passage 1487

Retrieved by: Dense

> We use the English Wikipedia dump from June 2016 as the corpus resource for our methods and baselines. For parsing the corpus, we rely on spaCy. For the lemma embeddings, we rely on the word embeddings of the dLCE model BIBREF10 which is the state-of-the-art vector representation for distinguishing antonyms from synonyms. We re-implemented this cutting-edge model on Wikipedia with 100 dimensions, and then make use of the dLCE word embeddings for initialization the lemma embeddings. The embeddings of POS tags, dependency labels, distance labels, and out-of-vocabulary lemmas are initialized randomly. The number of dimensions is set to 10 for the embeddings of POS tags, dependency labels and distance labels. We use the validation sets to tune the number of dimensions for these labels. For optimization, we rely on the cross-entropy loss function and Stochastic Gradient Descent with the Adadelta update rule BIBREF11 . For training, we use the Theano framework BIBREF12 . Regularization is applied by a dropout of 0.5 on each of component's embeddings (dropout rate is tuned on the validation set). We train the models with 40 epochs and update all embeddings during training.

#### Relevance 1487

Label: 

#### Passage 1488

Retrieved by: Dense

> To compare AntSynNET with baseline models for pattern-based classification of antonyms and synonyms, we introduce two pattern-based baseline methods: the distributional method (Section "Distributional Baseline" ), and the distributed method (Section "Distributed Baseline" ).

#### Relevance 1488

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1489

Retrieved by: Hybrid RRF followed by BGE reranking

> of this paper is organized as follows: In Section "Related Work" , we present previous work distinguishing antonyms and synonyms. Section "AntSynNET: LSTM-based Antonym-Synonym Distinction" describes our proposed AntSynNET model. We present the induction of the patterns (Section "Baseline Models" ), describe the recurrent neural network with long short-term memory units which is used to encode patterns within a vector representation (Section "Recurrent Neural Network with Long Short-Term Memory Units" ), and describe two models to classify antonyms and synonyms: the pure pattern-based model (Section UID11 ) and the combined model (Section UID13 ). After introducing two baselines in Section "Baseline Models" , we describe our dataset, experimental settings, results of our methods, the effects of the newly proposed distance feature, and the effects of the various types of word embeddings. Section "Conclusion" concludes the paper.

#### Relevance 1489

Label: 

#### Passage 1490

Retrieved by: Hybrid RRF followed by BGE reranking

> We would like to thank Michael Roth for helping us to compute the results of the R&SiW model on our dataset.
> 
> The research was supported by the Ministry of Education and Training of the Socialist Republic of Vietnam (Scholarship 977/QD-BGDDT; Kim-Anh Nguyen), the DFG Collaborative Research Centre SFB 732 (Kim-Anh Nguyen, Ngoc Thang Vu), and the DFG Heisenberg Fellowship SCHU-2580/1 (Sabine Schulte im Walde).

#### Relevance 1490

Label: 

#### Passage 1491

Retrieved by: Hybrid RRF followed by BGE reranking

> A recurrent neural network (RNN) is suitable for modeling sequential data by a vector representation. In our methods, we use a long short-term memory (LSTM) network, a variant of a recurrent neural network to encode patterns, for the following reasons. Given a sequence of words $p=[n_1,n_2,...,n_k]$ as input data, an RNN processes each word $n_t$ at a time, and returns a vector of state $h_k$ for the complete input sequence. For each time step $t$ , the RNN updates an internal memory state $h_t$ which depends on the current input $n_t$ and the previous state $h_{t-1}$ . Yet, if the sequential input is a long-term dependency, an RNN faces the problem of gradient vanishing or exploding, leading to difficulties in training the model.
> 
> LSTM units address these problems. The underlying idea of an LSTM is to use an adaptive gating mechanism to decide on the degree that LSTM units keep the previous state and memorize the extracted features of the current input. More specifically, an LSTM comprises four components: an input gate $i_t$ , a forget gate $f_t$ , an output gate $o_t$ , and a memory cell $c_t$ . The state of an LSTM at each time step $t$ is formalized as follows: $
> \begin{array}{l}
> i_t = \sigma (W_i \cdot x_t + U_i \cdot h_{t-1} + b_i) \\
> f_t = \sigma (W_f \cdot x_t + U_f \cdot h_{t-1} + b_f) \\
> o_t = \sigma (W_o \cdot x_t + U_o \cdot h_{t-1} + b_o) \\
> g_t = \tanh (W_c \cdot x_t + U_c \cdot h_{t-1} + b_c) \\
> c_t = i_t \otimes g_t + f_t \otimes c_{t-1}
> \end{array}
> $
> 
> $W$ refers to a matrix of weights that projects information between two layers; $b$ is a layer-specific vector of bias terms; $\sigma $ denotes the sigmoid function. The output of an LSTM at a time step $t$ is computed as follows: $
> h_t = o_t \otimes \tanh (c_t)
> $
> 
> where $\otimes $ denotes element-wise multiplication. In our methods, we rely on the last state $h_k$ to represent the vector $\vec{v}_p$ of a pattern $p = [\vec{n}_1, \vec{n}_2,...,\vec{n}_k]$ .

#### Relevance 1491

Label: 

## Question 0162

Paper: Text Classification based on Word Subspace with Term-Frequency

> What can word subspace represent?

### Common Retrieved Chunks

#### Passage 1492

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The word subspace formulation presented in Section "Word subspace" is a practical and compact way to represent sets of word vectors, retaining most of the variability of features. However, as seen in the BOW features, the frequency of words is relevant information that can improve the characterization of a text. To incorporate this information into the word subspace modeling, we propose an extension of the word subspace, called the term-frequency (TF) weighted word subspace.
> 
> Like the word subspace, the TF weighted word subspace is mathematically defined as a low-dimensional linear subspace in a word vector space with high dimensionality. However, a weighted version of the PCA BIBREF25 , BIBREF26 is utilized to incorporate the information given by the frequencies of words (term-frequencies). This TF weighted word subspace is equivalent to the word subspace if we consider all occurrences of the words.
> 
> Consider the set of word vectors $\lbrace {x}_c^k\rbrace _{k=1}^{N_c} \in \mathbb {R}^{p}$ , which represents each word in the context $c$ , and the set of weights $\lbrace \omega _i\rbrace _{i=1}^{N_c}$ , which represent the frequencies of the words in the context $c$ .
> 
> We incorporate these frequencies into the subspace calculation by weighting the data matrix ${X}$ as follows:
> 
> $${\widetilde{X}}={X}{\Omega }^{1/2},$$   (Eq. 33)
> 
> where ${X} \in \mathbb {R}^{p \times N_c}$ is a matrix containing the word vectors $\lbrace {x}_c^k\rbrace _{k=1}^{N_c}$ and ${\Omega }$ is a diagonal matrix containing the weights $\lbrace \omega _i\rbrace _{i=1}^{N_c}$ .
> 
> We then perform PCA by solving the SVD of the matrix ${\widetilde{X}}$ :
> 
> $${\widetilde{X}}={AMB}^{\top },$$   (Eq. 34)
> 
> where the columns of the orthogonal matrices ${A}$ and ${B}$ are, respectively, the left-singular vectors and right-singular vectors of the matrix ${\widetilde{X}}$ , and the diagonal matrix ${M}$ contains singular values of ${\widetilde{X}}$ .
> 
> Finally, the orthonormal basis vectors of the $m_c$ -dimensional TF weighted subspace ${W}$ are the column vectors in ${A}$ corresponding to the $m_c$ largest singular values in ${M}$ .
> 
> Text classification with TF weighted word subspace can also be performed under the framework of MSM. In this paper, we will refer to MSM with TF weighted word subspace as TF-MSM.

#### Relevance 1492

Label: 

#### Passage 1494

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> One crucial aspect of the word2vec representation is that arithmetic and distance calculation between two word vectors can be performed, giving information about their semantic relationship. However, rather than looking at pairs of word vectors, we are interested in studying the relationship between sets of vectors as a whole and, therefore, it is desirable to have a text representation based on a set of these word vectors.
> 
> To tackle this problem, we introduce the novel concept of word subspace. It is mathematically defined as a low dimensional linear subspace in a word vector space with high dimensionality. Given that words from texts of the same class belong to the same context, it is possible to model word vectors of each class as word subspaces and efficiently compare them in terms of similarity by using canonical angles between the word subspaces. Through this representation, most of the variability of the class is retained. Consequently, a word subspace can effectively and compactly represent the context of the corresponding text. We achieve this framework through the mutual subspace method (MSM) BIBREF9 .
> 
> The word subspace of each text class is modeled by applying PCA without data centering to the set of word vectors of the class. When modeling the word subspaces, we assume only one occurrence of each word inside the class.
> 
> However, as seen in the BOW approach, the frequency of words inside a text is an informative feature that should be considered. In order to introduce this feature in the word subspace modeling and enhance its performance, we further extend the concept of word subspace to the term-frequency (TF) weighted word subspace.
> 
> In this extension, we consider a set of weights, which encodes the words frequencies, when performing the PCA. Text classification with TF weighted word subspace can also be performed under the framework of MSM. We show the validity of our modeling through experiments on the Reuters database, an established database for natural language processing tasks. We demonstrate the effectiveness of the word subspace formulation and its extension, comparing our methods' performance to various state-of-art methods.
> 
> The main contributions of our work are:
> 
> The remainder of this paper is organized as follows. In Section "Related

#### Relevance 1494

Label: 

#### Passage 1495

Retrieved by: BM25, Dense, Hybrid RRF

> In this experiment, we modeled the word vectors from each class in the Reuters-8 database into a word subspace. The primary goal is to visualize how much of the text data can be represented by a lower dimensional subspace.
> 
> Subspace representations are very efficient in compactly represent data that is close to a normal distribution. This characteristic is due to the application of the PCA, that is optimal to find the direction with the highest variation within the data.
> 
> In PCA, the principal components give the directions of maximum variance, while their corresponding eigenvalues give the variance of the data in each of them. Therefore, by observing the distribution of the eigenvalues computed when performing PCA in the modeling of the subspaces, we can suggest if the data is suitable or not for subspace representation.
> 
> For each class, we normalized the eigenvalues by the largest one of the class. Fig. 2 shows the mean of the eigenvalues and the standard deviation among classes. It is possible to see that the first largest eigenvalues retain larger variance than the smallest ones. In fact, looking at the first 150 largest eigenvalues, we can see that they retain, on average, 86.37% of the data variance. Also, by observing the standard deviation, we can understand that the eigenvalues distribution among classes follows the same pattern, that is, most of the variance is in the first dimensions. This plot indicates that text data represented by vectors generated with word2vec is suitable for subspace representation.

#### Relevance 1495

Label: 

#### Passage 1496

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

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

#### Relevance 1496

Label: 

#### Passage 1497

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this paper, we proposed a new method for text classification, based on the novel concept of word subspace under the MSM framework. We also proposed the term-frequency weighted word subspace which can incorporate the frequency of words directly in the modeling of the subspace by using a weighted version of PCA.
> 
> Most of the conventional text classification methods are based on the bag-of-words features, which are very simple to compute and had been proved to produce positive results. However, bag-of-words are commonly high dimensional models, with a sparse representation, which is computationally heavy to model. Also, bag-of-words fail to convey the semantic meaning of words inside a text. Due to these problems, neural networks started to be applied to generate a vector representation of words. Despite the fact that these representations can encode the semantic meaning of words, conventional methods do not work well when considering word vectors separately.
> 
> In our work, we focused on the word2vec representation, which can embed the semantic structure of words, rendering vector angles as a useful metric to show meaningful similarities between words. Our experiments showed that our word subspace modeling along with the MSM outperforms most of the conventional methods. Ultimately, our TF weighted subspace formulation resulted in significantly higher accuracy when compared to all conventional text classification methods discussed in this work. It is important to note that our method does not consider the order of the words in a text, resulting in a loss of context information. As a future work, we wish to extend our word subspace concept further in mainly two directions. First, we seek to encode word order, which may enrich the representation of context information. Second, we wish to model dynamic context change, enabling analysis of large documents, by having a long-short memory to interpret information using cues from different parts of a text.

#### Relevance 1497

Label: 

### BM25

#### Passage 1493

Retrieved by: BM25

> Given the observation of the eigenvalues distribution of word vectors, we could see that word vectors that belong to the same context, i.e., same class, are suitable for subspace representation. Our analysis showed that half of the word vector space dimensions suffice to represent most of the variability of the data in each class of the Reuters-8 database.
> 
> The results from the text classification experiment showed that subspace-based methods performed better than the text classification methods discussed in this work. Ultimately, our proposed TF weighted word subspace with MSM surpassed all the other methods. word2vec features are reliable tools to represent the semantic meaning of the words and when treated as sets of word vectors, they are capable of representing the content of texts. However, despite the fact that word vectors can be treated separately, conventional methods such as SVM and LSA may not be suitable for text classification using word vectors.
> 
> Among the conventional methods, LSA and SVM achieved about 86% and 89%, respectively, when using bag-of-words features. Interestingly, both methods had better performance when using binary weights. For LSA, we can see that despite the slight differences in the performance, tfidfBOW required approximations with smaller dimensions. SVM had the lowest accuracy rate when using the tfidfBOW features. One possible explanation for this is that TF-IDF weights are useful when rare words and very frequent words exist in the corpus, giving higher weights for rare words and lower weights for common words. Since we removed the stop words, the most frequent words among the training documents were not considered and, therefore, using TF-IDF weights did not improve the results.
> 
> Only MNB with tfBOW performed better than MSM. This result may be because tfBOW features encode the word frequencies, while MSM only considers a single occurrence of words. When incorporating the word frequencies with our TF weighted word subspace, we achieved a higher accuracy of 92.01%, performing better than MNB at a significance level of 95%.

#### Relevance 1493

Label: 

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1498

Retrieved by: Hybrid RRF followed by BGE reranking

> tasks. We demonstrate the effectiveness of the word subspace formulation and its extension, comparing our methods' performance to various state-of-art methods.
> 
> The main contributions of our work are:
> 
> The remainder of this paper is organized as follows. In Section "Related Work" , we describe the main works related to text classification. In Section "Word subspace" , we present the formulation of our proposed word subspace. In Section "Conventional text classification methods" , we explain how text classification with word subspaces is performed under the MSM framework. Then, we present the TF weighted word subspace extension in Section "TF weighted word subspace" . Evaluation experiments and their results are described in Section "Experimental Evaluation" . Further discussion is then presented in Section "Discussion" , and our conclusions are described in Section "Conclusions and Future Work" .

#### Relevance 1498

Label: 

## Question 0163

Paper: Meta-Learning for Low-resource Natural Language Generation in Task-oriented Dialogue Systems

> what other training procedures were explored?

### Common Retrieved Chunks

#### Passage 1499

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We propose a generalized optimization-based meta-learning approach Meta-NLG for the low-resource NLG task. Meta-NLG utilizes Meta NLG tasks and a meta-learning optimization procedure based on MAML. Extensive experiments on a new benchmark dataset (MultiWoz) show that Meta-NLG significantly outperforms other training procedures, indicating that our method adapts fast and well to new low-resource settings. Our work may inspire researchers to use similar optimization techniques for building more robust and scalable NLG components in task-oriented dialog systems.

#### Relevance 1499

Label: 

#### Passage 1501

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> As an essential part of a task-oriented dialogue system BIBREF0 , the task of natural language generation (NLG) is to produce a natural language utterance containing the desired information given a semantic representation consisting of dialogue act types with a set of slot-value pairs. Conventional methods using hand-crafted rules often generates monotonic utterances and it requires substantial amount of human engineering work. Recently, various neural approaches BIBREF1 , BIBREF2 , BIBREF3 have been proposed to generate accurate, natural and diverse utterances. However, these methods are typically developed for particular domains. Moreover, they are often data-intensive to train. The high annotation cost prevents developers to build their own NLG component from scratch. Therefore, it is extremely useful to train a NLG model that can be generalized to other NLG domains or tasks with a reasonable amount of annotated data. This is referred to low-resource NLG task in this paper.
> 
> Recently, some methods have been proposed for low-resource NLG tasks. Apart from the simple data augmentation trick BIBREF4 , specialized model architectures, including conditional variational auto-encoders (CVAEs, BIBREF3 , BIBREF5 , BIBREF6 ) and adversarial domain adaptation critics BIBREF5 , have been proposed to learn domain-invariant representations. Although promising results were reported, we found that datasets used by these methods are simple which tend to enumerate many slots and values in an utterance without much linguistic variations. As a consequence, over-fitting the slots and values in the low-resource target domain could even outperform those versions trained with rich source domain examples BIBREF6 . Fortunately, there is a new large-scale dialog dataset (MultiWoz, BIBREF7 ) that contains a great variety of domains and linguistic patterns that allows us to conduct extensive and meaningful experimental analysis for low-resource NLG tasks.
> 
> In this paper, instead of casting the problem as model-based approaches, we propose a generalized optimization-based meta-learning approach to directly enhance the optimization procedure for the low-resource NLG task. We start by arguing that a recently proposed model-agnostic meta-learning algorithm (MAML, BIBREF8 ) is a nice fit to the low-resource NLG task. Then, we proposed a generalized NLG algorithm called Meta-NLG based on MAML by viewing languages in different domains or dialog act types as separate Meta NLG tasks.

#### Relevance 1501

Label: 

#### Passage 1502

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The goal of low-resource NLG is to fine-tune a pre-trained NLG model on new NLG tasks (e.g., new domains) with a small amount of training examples. BIBREF4 proposed a “data counterfeiting” method to augment the low-resource training data in the new task without modifying the model or training procedure. BIBREF3 proposed a semantically-conditioned variational autoencoder (SCVAE) learn domain-invariant representations feeding to SCLSTM. They shown that it improves SCLSTM in low-resource settings. BIBREF6 adopted the same idea as in BIBREF3 . They used two conditional variational autoencoders to encode the sentence and the DA into two separate latent vectors, which are fed together to the decoder RALSTM BIBREF2 . They later designed two domain adaptation critics with an adversarial training algorithm BIBREF5 to learn an indistinguishable latent representation of the source and the target domain to better generalize to the target domain. Different from these model-based approaches, we directly tackle the optimization issue from a meta-learning perspective.

#### Relevance 1502

Label: 

#### Passage 1504

Retrieved by: Dense, Hybrid RRF

> To learn a INLINEFORM0 that can be easily fine-tuned on new low-resource NLG tasks, the idea of our Meta-NLG algorithm is to repeatedly simulate auxiliary Meta NLG tasks from INLINEFORM1 to mimic the fine-tuning process in Eq.( EQREF9 ). Then, we treat each Meta NLG task as a single meta training sample/episode, and utilize the meta optimization objective in the next section to directly learn from them.
> 
> Therefore, the first step is to construct a set of auxiliary Meta NLG tasks INLINEFORM0 to simulate the low-resource fine-tuning process. We construct a Meta NLG task INLINEFORM1 by:
> 
> DISPLAYFORM0
> 
> INLINEFORM0 and INLINEFORM1 of each INLINEFORM2 are two independent subsets of DA-utterance pairs from high-resource source data INLINEFORM3 . INLINEFORM4 and INLINEFORM5 correspond to meta-train (support) and meta-test (query) sets of a typical meta-learning or few-shot learning setup, and INLINEFORM6 is often referred to as a training episode. This meta setup with both INLINEFORM7 and INLINEFORM8 in one Meta NLG task allows our Meta-NLG algorithm to directly learn from different Meta NLG tasks. The usage of them will be elaborated later. Meta NLG tasks are constructed with two additional principles:
> 
> Task Generalization: To generalize to new NLG tasks, Meta NLG tasks follow the same modality as the target task. For example, if our target task is to adapt to DA-utterance pairs in a new domain, then DA-utterance pairs in each INLINEFORM0 are sampled from the same source domain. We also consider adapting to new DA types in later experiments. In this case, DA-utterance pairs in each INLINEFORM1 have the same DA type. This setting merges the goal of task generalization.
> 
> Low-resource Adaptation: To simulate the process of adapting to a low-resource NLG task, the sizes of both subsets INLINEFORM0 and INLINEFORM1 , especially INLINEFORM2 , are set small. Therefore, when the model is updated on INLINEFORM3 as a part of the later meta-learning steps, it only sees a small amount of samples in that task. This setup embeds the goal of low-resource adaptation.

#### Relevance 1504

Label: 

#### Passage 1505

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Meta-learning or learning-to-learn, which can date back to some early works BIBREF11 , has recently attracted extensive attentions. A fundamental problem is “fast adaptation to new and limited observation data”. In pursuing this problem, there are three categories of meta-learning methods:
> 
> Metric-based: The idea is to learn a metric space and then use it to compare low-resource testing samples to rich training samples. The representative works in this category include Siamese Network BIBREF12 , Matching Network BIBREF13 , Memory-augmented Neural Network (MANN BIBREF14 ), Prototype Net BIBREF15 , and Relation Network BIBREF16 .
> 
> Model-based: The idea is to use an additional meta-learner to learn to update the original learner with a few training examples. BIBREF17 developed a meta-learner based on LSTMs. Hypernetwork BIBREF18 , MetaNet BIBREF19 , and TCML BIBREF20 also learn a separate set of representations for fast model adaptation. BIBREF21 proposed an LSTM-based meta-learner to learn the optimization algorithm (gradients) used to train the original network.
> 
> Optimization-based: The optimization algorithm itself can be designed in a way that favors fast adaption. Model-agnostic meta-learning (MAML, BIBREF8 , BIBREF22 , BIBREF23 ) achieved state-of-the-art performance by directly optimizing the gradient towards a good parameter initialization for easy fine-tuning on low-resource scenarios. It introduces no additional architectures nor parameters. Reptile BIBREF24 is similar to MAML with only first-order gradient. In this paper, we propose a generalized meta optimization method based on MAML to directly solve the intrinsic learning issues of low-resource NLG tasks.

#### Relevance 1505

Label: 

### BM25

#### Passage 1500

Retrieved by: BM25

> To better evaluate the quality of the generated utterances, we performed manual evaluation.
> 
> Metrics: Given a DA and a reference utterance in a low-resource target domain with adaptation size 500, two responses generated by Meta-NLG and MTL-NLG were presented to three human annotators to score each of them in terms of informativeness and naturalness (rating out of 3), and also indicate their pairwise preferences (Win-Tie-Lose) on Meta-NLG against MTL-NLG. Informativeness is defined as whether the generated utterance captures all the information, including multiple slots and probably multiple DA types, specified in the DA. Naturalness measures whether the utterance is plausibly generated by a human.
> 
> Annotation Statistics: Cases with identical utterances generated by two models were filtered out. We obtained in total 600 annotations on each individual metric for each target domain. We calculated the Fleiss’ kappa BIBREF27 to measure inter-rater consistency. The overall Fleiss’ kappa values for informativeness and naturalness are 0.475 and 0.562, indicating “Moderate Agreement”, and 0.637 for pairwise preferences, indicating “Substantial Agreement”.
> 
> Results: Scores of informativeness and naturalness are presented in Table TABREF36 . Meta-NLG outscores MTL-NLG in terms of both metrics on all four domains. Overall, Meta-NLG received significantly (two-tailed t-test, INLINEFORM0 ) higher scores than MTL-NLG. Results for pairwise preferences are summarized in Table TABREF37 . Even though there are certain amount of cases where the utterances generated by different models are nearly the same (Tie) to annotators, Meta-NLG is overall significantly preferred over MTL-NLG (two-tailed t-test, INLINEFORM1 ) across different target domains.

#### Relevance 1500

Label: 

#### Passage 1503

Retrieved by: BM25

> In this section, we tested when a NLG model is adapted to two types (near and far) of low-resource language domains. Experiment follows a leave-one-out setup by leaving one target domain for low-resource adaptation, while using the remainder domains as high-resource source training data. A target domain is a near-domain if it contains no domain-specific DA type but only domain-specific slots compared to the remainder domains. In contrast, a target domain containing both domain-specific DA types and slots is considered as a far-domain. Adapting to near-domains requires to capture unseen slots, while adapting to far-domains requires to learn new slots as well as new language patterns. Adaptation size is the number of DA-utterance pairs in the target domain used to fine-tune the NLG model. To test different low-resource degrees, we considered different adaptation sizes (1,000, 500, 200) in subsequent experiments.
> 
> Near-domain Adaptation: Figure FIGREF25 and Table TABREF26 show that “Attraction”, “Hotel”, “Restaurant”, and “Taxi”, are four near-domains compared to remainder domains. Only results for “Attraction” and “Hotel” are included due to page limit. The other two domains are also simpler with only one domain-specific slot. Several observations can be noted from results in Table TABREF27 . First, Using only source or target domain samples does not produce competitive performance. Using only source domain samples (Zero-NLG) performs the worst. It obtains very low BLEU-4 scores, indicating that the sentences generated do not match the linguistic patterns in the target domain. Using only low-resource target domain samples (Scratch-NLG) performs slightly better, yet still much worse than MTL-NLG and Meta-NLG. Second, Meta-NLG shows a very strong performance for this near-domain adaptation setting. It consistently outperforms MTL-NLG and other methods with very remarkable margins in different metrics and adaptation sizes. More importantly, it even works better than Supervised-NLG which is trained on high-resource samples in the target domain. Third, Meta-NLG is particularly strong in performance when the adaptation size is small. As the adaptation size decreases from 1,000 to 200, the performance of Scratch-NLG and MTL-NLG drops quickly, while Meta-NLG performs stably well. Both BLEU-4 and ERR even increase in “Hotel” domain when the adaptation size decreases from 500 to 200.
> 
> Far-domain Adaptation: In this experiment, we tested the

#### Relevance 1503

Label: 

### Dense

#### Passage 1506

Retrieved by: Dense

> We utilized the well-recognized semantically conditioned LSTM (SCLSTM BIBREF1 ) as the base model INLINEFORM0 . We used the default setting of hyperparameters (n_layer = 1, hidden_size = 100, dropout = 0.25, clip = 0.5, beam_width = 5). We implemented Meta-NLG based on the PyTorch SCLSTM implementation from BIBREF7 . As Meta-NLG is model-agnostic, it is applicable to many other NLG models.
> 
> We included different model settings as baseline:
> 
> Scratch-NLG: Train INLINEFORM0 with only low-resource target task data, ignoring all high-resource source task data.
> 
> MTL-NLG: Train INLINEFORM0 using a multi-task learning paradigm with source task data, then fine-tune on the low-resource target task.
> 
> Zero-NLG: Train INLINEFORM0 using multi-task learning (MTL) with source task data, then directly test on a target task without a fine-tuning step. This corresponds to a zero-shot learning scenario.
> 
> Supervised-NLG: Train INLINEFORM0 using MTL with full access to high-resource data from both source and target tasks. Its performance serves an upper bound using multi-task learning without the low-resource restriction.
> 
> Meta-NLG(proposed): Use Algorithm 1 to train INLINEFORM0 on source task data, then fine-tune on the low-resource target task.
> 
> For Meta-NLG, we set batch size to 5, and INLINEFORM0 and INLINEFORM1 . A single inner gradient update is used per meta update with Adam BIBREF25 . The size of a Meta NLG task is set to 400 with 200 samples assigned to INLINEFORM2 and INLINEFORM3 because the minimum amount of target low-resource samples is 200 in our later experiments. During fine-tuning on a low-resource target task, early-stop is conducted on a small validation set with size 200. The model is then evaluated on other DA-utterance pairs in the target task.
> 
> As in earlier NLG researches, we use the BLEU-4 score BIBREF26 and the slot error rate (ERR) as evaluation metrics. ERR is computed by the ratio of the sum of the number of missing and redundant slots in a generated utterance divided by the total number of slots in the DA. We randomly sampled target low-resource task five times for each experiment and reported the average score.

#### Relevance 1506

Label: 

#### Passage 1507

Retrieved by: Dense

> With the Meta NLG tasks defined above, we formulate the meta-learning objective of Meta-NLG as below: DISPLAYFORM0 DISPLAYFORM1
> 
> The optimization for each Meta NLG task INLINEFORM0 is computed on INLINEFORM1 referring to INLINEFORM2 . Firstly, the model parameter INLINEFORM3 to be optimized is updated on INLINEFORM4 by Eq.( EQREF14 ). This step mimics the process when INLINEFORM5 is adapted to a new low-resource NLG task INLINEFORM6 with low-resource observations INLINEFORM7 . We need to note that Eq.( EQREF14 ) is an intermediate step, and it only provides an adapted parameter ( INLINEFORM8 ) to our base model INLINEFORM9 to be optimized in each iteration. Afterwards, the base model parameterized by the updated parameter ( INLINEFORM10 ) is optimized on INLINEFORM11 using the meta objective in Eq.( EQREF13 ). This meta-learning optimization objective directly optimizes the model towards generalizing to new low-resource NLG tasks by simulating the process repeatedly with Meta NLG tasks in Eq.( EQREF13 ).
> 
> The optimization of Eq.( EQREF13 ) can be derived in Eq.( EQREF15 ). It involves a standard first-order gradient INLINEFORM0 as well as a gradient through another gradient INLINEFORM1 . Previous study BIBREF8 shows that the second term can be approximated for computation efficiency with marginal performance drop. In our case, we still use the exact optimization in Eq.( EQREF15 ) as we do not encounter any computation difficulties even on the largest NLG dataset so far. The second-order gradient is computed by a Hessian matrix INLINEFORM2 .
> 
> DISPLAYFORM0
> 
> DISPLAYFORM0
> 
> To better understand the meta objective, we include a standard multi-task learning (MTL) objective in Eq.( EQREF17 ). MTL learns through individual DA-utterance pairs from different high-resource NLG tasks INLINEFORM0 , and it does not explicitly learn to adapt to new low-resource NLG tasks. Figure FIGREF16 visually illustrates the differences with three high-resource source tasks INLINEFORM1 with optimal parameters INLINEFORM2 for each task. INLINEFORM3 is learned from individual DA-utterance pairs in INLINEFORM4 , while Meta-NLG repeatedly constructs auxiliary Meta NLG tasks INLINEFORM5 from INLINEFORM6 and directly learns INLINEFORM7 from them. As a result, INLINEFORM8 is closer to INLINEFORM9 and INLINEFORM10 (the optimal parameters of some new low-resource tasks, e.g, INLINEFORM11 and INLINEFORM12 ) than INLINEFORM13 . As we will

#### Relevance 1507

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1508

Retrieved by: Hybrid RRF followed by BGE reranking

> NLG tasks INLINEFORM5 from INLINEFORM6 and directly learns INLINEFORM7 from them. As a result, INLINEFORM8 is closer to INLINEFORM9 and INLINEFORM10 (the optimal parameters of some new low-resource tasks, e.g, INLINEFORM11 and INLINEFORM12 ) than INLINEFORM13 . As we will see soon later, our meta optimization scheme results in a substantial gain in the final performance.
> 
> Algorithm 1 illustrates the process to learn INLINEFORM0 from INLINEFORM1 . We note that batches are at the level of Meta NLG tasks, not DA-utterances pairs. Fine-tuning Meta-NLG on a new low-resource NLG task with annotated DA-utterance pairs INLINEFORM2 uses the same algorithm parameterized by ( INLINEFORM3 ).
> 
> [1]
> 
> INLINEFORM0 INLINEFORM1
> 
> Initialize INLINEFORM0
> 
> INLINEFORM0 not converge
> 
> Simulate a batch of Meta NLG tasks INLINEFORM0 INLINEFORM1
> 
> Compute INLINEFORM0 in Eq.( EQREF14 )
> 
> Meta update INLINEFORM0 in Eq.( EQREF15 )
> 
> Return INLINEFORM0
> 
> Meta-NLG( INLINEFORM0 )

#### Relevance 1508

Label: 

## Question 0164

Paper: #SarcasmDetection is soooo general! Towards a Domain-Independent Approach for Detecting Sarcasm

> what domains are explored?

### Common Retrieved Chunks

#### Passage 1509

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Twitter is a micro-blogging service that allows users to post short “tweets” to share content or describe their feelings or opinions in 140 characters or less. For researchers, it boasts a low cost of annotation and plentiful supply of data (users often self-label their tweets using the “#” symbol—many explicitly label their sarcastic tweets using the hashtag “#sarcasm”). A variety of approaches have been taken toward automatically detecting sarcasm on Twitter, including explicitly using the information present in a tweet's hashtag(s); Maynard and Greenwood maynard2014cares learned which hashtags characteristically corresponded with sarcastic tweets, and used the presence of those indicators to predict other sarcastic tweets, with high success. BIBREF2 liebrecht2013perfect detected sarcasm in Dutch tweets using unigram, bigram, and trigram features.
> 
> BIBREF3 Rajadesingan:2015:SDT:2684822.2685316 detected sarcastic tweets based on features adapted from behavioral models of sarcasm usage, drawing extensively from individual users' Twitter histories and relying heavily on situational context and user characteristics. The system also employed lexical features and grammatical correctness as a means of modelling different aspects of the user's behavior.
> 
> Other researchers have had success identifying sarcasm by a tweet's use of positive sentiment to describe a negative situation BIBREF4 , employing contextual BIBREF5 or pragmatic BIBREF6 features, and observing the writing style and emotional scenario of a tweet BIBREF7 . An underlying theme among these methods is that the features are generally designed specifically for use with tweets. A major challenge in developing a more general approach for sarcasm detection lies in developing features that are present across many domains, yet still specific enough to reliably capture the differences between sarcastic and non-sarcastic text.
> 
> Finally, some researchers have recently explored approaches that rely on word embeddings and/or carefully tailored neural networks, rather than on task-specific feature design BIBREF8 , BIBREF9 , BIBREF10 . Since neural networks offer little transparency, it is uncertain whether the features learned in these approaches would be easily transferable across text domains for this task (prior research on other tasks suggests that the features computed by deep neural networks grow increasingly specific to the training dataset—and in turn, to the training domain—with each layer BIBREF11 ). Although an interesting question, the focus herein is on uncovering the specific

#### Relevance 1509

Label: 

#### Passage 1510

Retrieved by: BM25, Hybrid RRF

> Three feature sets were developed (one general, and two targeted toward Twitter and Amazon, respectively). Resources used to develop the features are described in Table TABREF9 . Five classifiers (Naïve Bayes, J48, Bagging, DecisionTable, and SVM), all from the Weka library, were tested using five-fold cross-validation on the training sets, and the highest-scoring (Naïve Bayes) was selected for use on the test set.
> 
> The Twitter- (T) and Amazon-specific (A) features are shown in Table TABREF11 . Domain-specific features were still computed for instances from the other domain unless it was impossible to compute those features in that domain (i.e., Amazon Star Rating for Twitter instances), in which case they were left empty. Twitter-specific features are based on the work of BIBREF15 maynard2014cares and BIBREF4 RiloffSarcasm. Maynard and Greenwood detect sarcastic tweets by checking for the presence of learned hashtags that correspond with sarcastic tweets, as well as sarcasm-indicator phrases and emoticons. We construct binary features based on their work, and on Riloff et al.'s work RiloffSarcasm, which determined whether or not a tweet was sarcastic by checking for positive sentiment phrases contrasting with negative situations (both of which were learned from other sarcastic tweets). We also add a feature indicating the presence of laughter terms. Amazon-based features are primarily borrowed from BIBREF12 's buschmeier-cimiano-klinger:2014:W14-26 earlier work on the Amazon dataset. [4]Individual binary features for each of the sarcasm hashtags (5 features) and laughter tokens (9 features) were also included.
> 
> We model some of our general features after those from BIBREF4 RiloffSarcasm, under the premise that the underlying principle that sarcasm often associates positive expressions with negative situations holds true across domains. Since positive sentiment phrases and negative situations learned from tweets are unlikely to generalize to different domains, we instead use three sentiment lexicons to build features that capture positive and negative sentiment rather than checking for specific learned phrases. Likewise, rather than bootstrapping specific negative situations from Twitter, we calculate the pointwise mutual information (PMI) between the most positive or negative word in the instance and the n-grams that immediately proceed it to create a more general version of the feature. Other general features developed for this work rely on syntactic characteristics, or are

#### Relevance 1510

Label: 

#### Passage 1511

Retrieved by: BM25, Hybrid RRF

> When testing on Amazon reviews, the worst-performing case was that in which the classifier was trained only on Twitter data (it did not manage to outperform either baseline). This underscores the inherent variations in the data across the two domains; despite the fact that many of the features were deliberately designed to be generalizable and robust to domain-specific idiosyncrasies, the different trends across domains still confused the classifier.
> 
> However, combining all of that same Twitter data with a much smaller amount of Amazon data (3998 Twitter training instances relative to 1003 Amazon training instances) and applying EasyAdapt to the combined dataset performed quite well ( INLINEFORM0 =0.780). The classifier was able to take advantage of a wealth of additional Twitter samples that had led to terrible performance on their own ( INLINEFORM1 =0.276). Thus, the high performance demonstrated when the EasyAdapt algorithm is applied to the training data from the two domains is particularly impressive. It shows that more data is indeed better data—provided that the proper features are selected and the classifier is properly guided in handling it.
> 
> Overall, the system cut the error rate from .256 to .220, representing a 14% relative reduction in error over prior best results on the Amazon dataset. Our results testing on Twitter are not directly comparable to others, since prior work's datasets could not be released; however, our results ( INLINEFORM0 =0.583) are in line with those reported previously ( BIBREF4 RiloffSarcasm: INLINEFORM1 =0.51; BIBREF13 davidov-tsur-rappoport:2010:CONLL: INLINEFORM2 =0.545). Additionally, our Twitter data did not contain many indicators shown to be discriminative in the past (leading our general features to be better predictors of sarcasm even when training/testing entirely within the domain), and our focus in developing features was on general performance rather than performance on Twitter specifically.
> 
> Both datasets were somewhat noisy. Many full-length reviews that were marked as “sarcastic” were only partially so, and included other sentences that were not sarcastic at all. This may have been particularly problematic when strong polarity was present in those sentences. An example of this is shown in Figure FIGREF20 , where the highlighted portion of the review indicates the sarcastic segment submitted by the annotator, and awesome, the most

#### Relevance 1511

Label: 

#### Passage 1512

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Sarcasm, a creative device used to communicate an intended meaning that is actually the opposite of its literal meaning, is notoriously difficult to convey and interpret through text, in part because doing so relies heavily upon shared contextual understandings that can be marked more easily by altered prosody (e.g., emphasis upon certain words) or non-verbal signals (e.g., rolling one's eyes). It is a complex process even for humans, and in fact an inability to detect sarcasm has been linked with a number of neurocognitive disorders, including dementia BIBREF0 . It is similarly a challenging open task in natural language processing, and has direct implications to a number of other critical application areas, such as sentiment analysis.
> 
> Most research on automatic sarcasm detection to date has focused on the Twitter domain, which boasts an ample source of publicly-available data, some of which is already self-labeled by users for the presence of sarcasm (e.g., with #sarcasm). However, Twitter is highly informal, space-restricted, and subject to frequent topic fluctuations from one post to the next due to the ebb and flow of current events—in short, it is not broadly representative of most text domains. Thus, sarcasm detectors trained using features designed for maximum Twitter performance are not necessarily transferable to other domains. Despite this, it is desirable to develop approaches that can harness the more generalizable information present in the abundance of Twitter data.
> 
> In this work, we develop a set of domain-independent features for sarcasm detection and show that the features generally perform well across text domains. Further, we validate that domain adaptation can be applied to sarcasm detection to leverage patterns in out-of-domain training data, even when results from training only on that source domain data are extremely bad (far below baseline results), to improve over training on only the target data or over training on the simply combined dataset. Finally, we make a new dataset of sarcastic and non-sarcastic tweets available online as a resource to other researchers.

#### Relevance 1512

Label: 

#### Passage 1514

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> domain-general approach. [6]Part-of-speech is considered in MPQA; Amazon and Twitter data was tagged using Stanford CoreNLP BIBREF20 and the Twitter POS-tagger BIBREF21 , respectively.
> 
> Finally, we include the best results reported by BIBREF12 buschmeier-cimiano-klinger:2014:W14-26 on the same Amazon dataset. For a more direct comparison between our work and theirs, we also report the results from using all of our features under the same classification conditions as theirs (10-fold cross-validation using scikit-learn's Logistic Regression, tuning with an F1 objective). We refer to the latter case as Our Results, Same Classifier as Prior Best.

#### Relevance 1514

Label: 

#### Passage 1515

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> This work develops a set of domain-independent features and demonstrates their usefulness for general sarcasm detection. Moreover, it shows that by applying a domain adaptation step to the extracted features, even a surplus of “bad” training data can be used to improve the performance of the classifier on target domain data, reducing error by 14% relative to prior work. The Twitter corpus described in this paper is publicly available for research purposes,[2] and represents a substantial contribution to multiple NLP sub-communities. This shared corpus of tweets annotated for sarcasm will hasten the advancement of further research. In the future, we plan to extend our approach to detect sarcasm in a completely novel domain, literature, eventually integrating the work into an application to support reading comprehension.

#### Relevance 1515

Label: 

#### Passage 1517

Retrieved by: Dense, Hybrid RRF

> Research on automatic sarcasm detection in other domains has been limited, but recently a publicly-available corpus of sarcastic and non-sarcastic Amazon product reviews was released by Filatova FILATOVA12.661 to facilitate research. BIBREF12 buschmeier-cimiano-klinger:2014:W14-26 test many feature combinations on this dataset, including those based on metadata (e.g., Amazon star rating), sentiment, grammar, the presence of interjections (e.g., “wow”) or laughter (e.g., through onomatopoeia or acronyms such as “lol”), the presence of emoticons, and bag-of-words features. Their highest F1 (0.744) is achieved using all of these with a logistic regression classifier; however, using only the star rating, they still achieve an F1 of 0.717. This highlights the need for high-performing, general features for sarcasm detection; metadata features are highly domain-specific, and even bag-of-words trends may be unique to certain domains (“trump” was one of the most common unigrams in our own Twitter training set, but only occurred once across all Amazon product reviews).
> 
> Prior to the release of Filatova's dataset, BIBREF13 davidov-tsur-rappoport:2010:CONLL developed a semi-supervised approach to classify tweets or Amazon reviews as sarcastic or non-sarcastic by clustering samples based on grammatical features and the full or partial presence of automatically-extracted text patterns. They evaluated their work on a sample of the classified instances annotated by anonymous users on Amazon Mechanical Turk. They tested several different seed sets with their approach, one of which contained a mixture of positive Amazon reviews, positive #sarcasm-tagged tweets, and a manually-selected sample of negative tweets. Although they did not report test results on Amazon reviews using this seed set, they did report test results on #sarcasm-tagged tweets, achieving an F-measure of 0.545. Their work is the closest to ours, because it attempts to harness training samples from both the Twitter and Amazon review domains.

#### Relevance 1517

Label: 

### BM25

#### Passage 1513

Retrieved by: BM25

> been particularly problematic when strong polarity was present in those sentences. An example of this is shown in Figure FIGREF20 , where the highlighted portion of the review indicates the sarcastic segment submitted by the annotator, and awesome, the most polar word in the entire review (circled), is outside that highlighted sentence.
> 
> Since tweets are self-labeled, users' own varying definitions of sarcasm lead to some extreme idiosyncrasies in the kinds of tweets labeled as sarcastic. Sarcastic tweets were also often dependent upon outside context. Some examples include (#sarcasm tags were removed in the actual dataset): “My daughter's 5th grade play went over as professional, flawless, and well rehearsed as a Trump speech. #sarcasm,” “#MilanAlessandria Mario Balotelli scored the fifth goal in the 5-0 win. He should play for the #Azzurri at #EURO2016. #sarcasm,” and “Good morning #sarcasm.”
> 
> Finally, some past research has found that it is more difficult to discriminate between sarcastic and non-sarcastic texts when the non-sarcastic texts contain sentiment BIBREF6 , BIBREF8 . Since our non-sarcastic tweets are emotionally-charged, our classifier may have exhibited lower performance than it would have with only neutral non-sarcastic tweets. Since distinguishing between literal and sarcastic sentiment is useful for real-world applications of sarcasm detection, we consider the presence of sentiment in our dataset to be a worthwhile challenge.
> 
> Regarding the general features developed for this work, the polarity- and subjectivity-based features performed well, while performance using only PMI features was lower. PMI scores in particular may have been negatively impacted by common Twitter characteristics, such as the trend to join keywords together in hashtags, and the use of acronyms that are unconventional in other domains. These issues could be addressed to some extent in the future via word segmentation tools, spell-checkers, and acronym expansion.

#### Relevance 1513

Label: 

### Dense

#### Passage 1516

Retrieved by: Dense

> The features used for each train/test scenario are shown in the first column of Table TABREF18 . Twitter Features refers to all features listed in Table TABREF11 preceded by the parenthetical (T), and Amazon Features to all features preceded by (A). General: Other Polarity includes the positive and negative percentages, average polarities, overall polarities, and largest polarity gap features from Table TABREF14 . General: Subjectivity includes the % strongly subjective positive words, % weakly subjective positive words, and their negative counterparts. We also include two baselines: the All Sarcasm case assumes that every instance is sarcastic, and the Random case randomly assigns each instance as sarcastic or non-sarcastic.
> 
> Results are reported for models trained only on Twitter, only on Amazon, on both training sets, and on both training sets when Daumé's daumeiii:2007:ACLMain EasyAdapt technique is applied, employing Twitter as the algorithm's source domain and Amazon as its target domain. EasyAdapt works by modifying the feature space so that it contains three mappings of the original features: a general (source + target) version, a source-only version, and a target-only version. More specifically, assuming an input feature set INLINEFORM0 for some INLINEFORM1 , where INLINEFORM2 is the number of features in the set, EasyAdapt transforms INLINEFORM3 to the augmented set, INLINEFORM4 . The mappings INLINEFORM5 for the source and target domain data, respectively, are defined as INLINEFORM6 and INLINEFORM7 , where INLINEFORM8 is the zero vector. Refer to Daumé daumeiii:2007:ACLMain for an in-depth discussion of this technique.
> 
> Each model was tested on the Amazon test data (the model trained only on Twitter was also tested on the Twitter test set). Amazon reviews were selected as the target domain since the Twitter dataset was much larger than the Amazon dataset; this scenario is more consistent with the typically stated goal of domain adaptation (a large labeled out-of-domain source dataset and a small amount of labeled data in the target domain), and most clearly highlights the need for a domain-general approach. [6]Part-of-speech is considered in MPQA; Amazon and Twitter data was tagged using Stanford CoreNLP BIBREF20 and the Twitter POS-tagger BIBREF21 , respectively.
> 
> Finally, we include the best results reported by BIBREF12 buschmeier-cimiano-klinger:2014:W14-26 on the same Amazon dataset. For

#### Relevance 1516

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1518

Retrieved by: Hybrid RRF followed by BGE reranking

> Data was taken from two domains: Twitter, and Amazon product reviews. The Amazon reviews were from the publicly available sarcasm corpus developed by Filatova FILATOVA12.661. To build our Twitter dataset, tweets containing exactly one of the trailing hashtags “#sarcasm,” “#happiness,” “#sadness,” “#anger,” “#surprise,” “#fear,” and “#disgust” were downloaded regularly during February and March 2016. Tweets containing the latter six hashtags, corresponding to Ekman's six basic emotions BIBREF14 , were labeled as non-sarcastic. Those hashtags were chosen because their associated tweets were expected to still express opinions, similarly to sarcastic tweets, but in a non-sarcastic way. Tweets containing #sarcasm were labeled as sarcastic; annotating tweets with the #sarcasm hashtag as such is consistent with the vast majority of prior work in the Twitter domain BIBREF6 , BIBREF2 , BIBREF15 , BIBREF3 , BIBREF5 , BIBREF8 , BIBREF10 .
> 
> The downloaded tweets were filtered to remove retweets, “@replies,” and tweets containing links. Retweets were removed to avoid having duplicate copies of identical tweets in the dataset, @replies were removed in case the hashtag referred to content in the tweet to which it replied rather than content in the tweet itself, and tweets with links were likewise removed in case the hashtag referred to content in the link rather than in the tweet itself. Requiring that the specified hashtag trailed the rest of the tweet (it could only be followed by other hashtags) was done based on the observation that when sarcastic or emotional hashtags occur in the main tweet body, the tweet generally discusses sarcasm or the specified emotion, rather than actually expressing sarcasm or the specified emotion. Finally, requiring that only one of the specified hashtags trailed the tweet eliminated cases of ambiguity between sarcastic and non-sarcastic tweets. All trailing “#sarcasm” or emotion hashtags were removed from the data before training and testing, and both datasets were randomly divided into training (80%) and testing (20%) sets. Further details are shown in Table TABREF6 .

#### Relevance 1518

Label: 

## Question 0165

Paper: Neural Machine Translation for Low Resource Languages using Bilingual Lexicon Induced from Comparable Corpora

> Do they evaluate their parallel sentence generation?

### Common Retrieved Chunks

#### Passage 1519

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The binary classifier described in the next section, assigns a translation probability score to a given sentence pair, after learning from examples of translations and negative examples of non-translation pairs. For, this we make a simplistic assumption that the parallel sentence pairs found in the bootstrap dataset are unique combinations, which fail being translations of each other, when we randomly pick a sentence from both the sets. Thus, there might be cases of false negatives due to the reliance on unsupervised random sampling for generation of negative labels.
> 
> Therefore at the beginning of every epoch, we randomly sample INLINEFORM0 negative sentences of the target language for every source sentence. From a few experiments and also from the literature, we converged on INLINEFORM1 to be performing the best, given our compute constraints.

#### Relevance 1519

Label: 

#### Passage 1520

Retrieved by: BM25, Hybrid RRF

> We evaluated the quality of the extracted parallel sentence pairs, by performing machine translation experiments on the augmented parallel corpus.
> 
> As the dataset for training the machine translation systems, we used high precision sentences extracted with greedy decoding, by ranking the sentence-pairs on their translation probabilities. Phrase-Based SMT systems were trained using Moses BIBREF14 . We used the grow-diag-final-and heuristic for extracting phrases, lexicalised reordering and Batch MIRA BIBREF15 for tuning (the default parameters on Moses). We trained 5-gram language models with Kneser-Ney smoothing using KenLM BIBREF16 . With these parameters, we trained SMT systems for en–ta and en–hi language pairs, with and without the use of extracted parallel sentence pairs.
> 
> For training neural machine translation models, we used the TensorFlow BIBREF17 implementation of OpenNMT BIBREF18 with attention-based transformer architecture BIBREF19 . The BLEU scores for the NMT models were higher than for SMT models, for both en–ta and en–hi pairs, as can be seen in Table TABREF23 .

#### Relevance 1520

Label: 

#### Passage 1521

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> maximum entropy classifier. The difference in the BLEU scores between out of domain and domain-specific translation is proved clearly using the word embeddings from characteristic vocabulary extracted using the extracted additional bitexts.
> 
> BIBREF2 ( BIBREF2 ) extract parallel sentences without the use of a classifier. Target language candidate sentences are found using the translation of source side comparable corpora. Sentence tail removal is used to strip the tail parts of sentence pairs which differ only at the end. This, along with the use of parallel sentences enhanced the BLEU score and helped to determine if the translated source sentence and candidate target sentence are parallel by measuring the word and translation error rate. This method succeeds in eliminating the need for domain specific text by using the target side as a source of candidate sentences. However, this approach is not feasible if there isn't a good source side translation system to begin with, like in our case.
> 
> Yet another approach which uses an existing translation system to extract parallel sentences from comparable documents was proposed by BIBREF3 ( BIBREF3 ). They describe a framework for machine translation using multilingual Wikipedia articles. The parallel corpus is assembled iteratively, by using a statistical machine translation system trained on a preliminary sentence-aligned corpus, to score sentence-level en–jp BLEU scores. After filtering out the unaligned pairs based on the MT evaluation metric, the SMT is retrained on the filtered pairs.

#### Relevance 1521

Label: 

#### Passage 1523

Retrieved by: BM25, Dense, Hybrid RRF

> Both neural and statistical machine translation approaches are highly reliant on the availability of large amounts of data and are known to perform poorly in low resource settings. Recent crowd-sourcing efforts and workshops on machine translation have resulted in small amounts of parallel texts for building viable machine translation systems for low-resource pairs BIBREF0 . But, they have been shown to suffer from low accuracy (incorrect translation) and low coverage (high out-of-vocabulary rates), due to insufficient training data. In this project, we try to address the high OOV rates in low-resource machine translation systems by leveraging the increasing amount of multilingual content available on the Internet for enriching the bilingual lexicon.
> 
> Comparable corpora such as Wikipedia, are collections of topic-aligned but non-sentence-aligned multilingual documents which are rich resources for extracting parallel sentences from. For example, Figure FIGREF1 shows that there are equivalent sentences on the page about Donald Trump in Tamil and English, and the phrase alignment for an example sentence is shown in Table TABREF4 .
> 
> Table TABREF2 shows that there are at least tens of thousands of bilingual articles on Wikipedia which could potentially have at least as many parallel sentences that could be mined to address the scarcity of parallel sentences as indicated in column 2 which shows the number of sentence-pairs in the largest available bilingual corpora for xx-en. As shown by BIBREF1 ( BIBREF1 ), the illustrated data sparsity can be addressed by extending the scarce parallel sentence-pairs with those automatically extracted from Wikipedia and thereby improving the performance of statistical machine translation systems.
> 
> In this paper, we will propose a neural approach to parallel sentence extraction and compare the BLEU scores of machine translation systems with and without the use of the extracted sentence pairs to justify the effectiveness of this method. Compared to previous approaches which require specialized meta-data from document structure or significant amount of hand-engineered features, the neural model for extracting parallel sentences is learned end-to-end using only a small bootstrap set of parallel sentence pairs.

#### Relevance 1523

Label: 

#### Passage 1524

Retrieved by: Dense, Hybrid RRF

> The parallel sentence extraction system needs a sentence aligned corpus which has been curated. These sentences were used as the ground truth pairs when we trained the model to classify parallel sentence pair from non-parallel pairs.

#### Relevance 1524

Label: 

#### Passage 1525

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> In this paper, we evaluated the benefits of using a neural network procedure to extract parallel sentences. Unlike traditional translation systems which make use of multi-step classification procedures, this method requires just a parallel corpus to extract parallel sentence pairs using a Siamese BiRNN encoder using GRU as the activation function.
> 
> This method is extremely beneficial for translating language pairs with very little parallel corpora. These parallel sentences facilitate significant improvement in machine translation quality when compared to a generic system as has been shown in our results.
> 
> The experiments are shown for English-Tamil and English-Hindi language pairs. Our model achieved a marked percentage increase in the BLEU score for both en–ta and en–hi language pairs. We demonstrated a percentage increase in BLEU scores of 11.03% and 14.7% for en–ta and en–hi pairs respectively, due to the use of parallel-sentence pairs extracted from comparable corpora using the neural architecture.
> 
> As a follow-up to this work, we would be comparing our framework against other sentence alignment methods described in BIBREF20 , BIBREF21 , BIBREF22 and BIBREF23 . It has also been interesting to note that the 2018 edition of the Workshop on Machine Translation (WMT) has released a new shared task called Parallel Corpus Filtering where participants develop methods to filter a given noisy parallel corpus (crawled from the web), to a smaller size of high quality sentence pairs. This would be the perfect avenue to test the efficacy of our neural network based approach of extracting parallel sentences from unaligned corpora.

#### Relevance 1525

Label: 

#### Passage 1526

Retrieved by: Dense, Hybrid RRF

> We experimented with two language pairs: English – Hindi (en–hi) and English – Tamil (en–ta). The parallel sentence extraction systems for both en–ta and en–hi were trained using the architecture described in SECREF7 on the following bootstrap set of parallel corpora:
> 
> An English-Tamil parallel corpus BIBREF11 containing a total of INLINEFORM0 sentence pairs, composed of INLINEFORM1 English Tokens and INLINEFORM2 Tamil Tokens.
> 
> An English-Hindi parallel corpus BIBREF12 containing a total of INLINEFORM0 sentence pairs, from which a set of INLINEFORM1 sentence pairs were picked randomly.
> 
> Subsequently, we extracted parallel sentences using the trained model, and parallel articles collected from Wikipedia. There were INLINEFORM0 bilingual English-Tamil and INLINEFORM1 English-Hindi titles on the Wikimedia dumps collected in December 2017.

#### Relevance 1526

Label: 

### BM25

#### Passage 1522

Retrieved by: BM25

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

#### Relevance 1522

Label: 

### Dense

#### Passage 1527

Retrieved by: Dense

> For the evaluation of the performance of our sentence extraction models, we looked at a few sentences manually, and have done a qualitative analysis, as there was no gold standard evaluation set for sentences extracted from Wikipedia. In Table TABREF13 , we can see the qualitative accuracy for some parallel sentences extracted from Tamil. The sentences extracted from Tamil, have been translated to English using Google Translate, so as to facilitate a comparison with the sentences extracted from English.
> 
> For the statistical machine translation and neural machine translation evaluation we use the BLEU score BIBREF13 as an evaluation metric, computed using the multi-bleu script from Moses BIBREF14 .

#### Relevance 1527

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1528

Retrieved by: Hybrid RRF followed by BGE reranking

> A lot of work has been done on the problem of automatic sentence alignment from comparable corpora, but a majority of them BIBREF2 , BIBREF1 , BIBREF3 use a pre-existing translation system as a precursor to ranking the candidate sentence pairs, which the low resource language pairs are not at the luxury of having; or use statistical machine learning approaches, where a Maximum Entropy classifier is used that relies on surface level features such as word overlap in order to obtain parallel sentence pairs BIBREF4 . However, the deep neural network model used in our paper is probably the first of its kind, which does not need any feature engineering and also does not need a pre-existing translation system.
> 
> BIBREF4 ( BIBREF4 ) proposed a parallel sentence extraction system which used comparable corpora from newspaper articles to extract the parallel sentence pairs. In this procedure, a maximum entropy classifier is designed for all sentence pairs possible from the Cartesian product of a pair of documents and passed through a sentence-length ratio filter in order to obtain candidate sentence pairs. SMT systems were trained on the extracted sentence pairs using the additional features from the comparable corpora like distortion and position of current and previously aligned sentences. This resulted in a state of the art approach with respect to the translation performance of low resource languages.
> 
> Similar to our proposed approach, BIBREF5 ( BIBREF5 ) showed how using parallel documents from Wikipedia for domain specific alignment would improve translation quality of SMT systems on in-domain data. In this method, similarity between all pairs of cross-language sentences with different text similarity measures are estimated. The issue of domain definition is overcome by the use of IR techniques which use the characteristic vocabulary of the domain to query a Lucene search engine over the entire corpus. The candidate sentences are defined based on word overlap and the decision whether a sentence pair is parallel or not using the maximum entropy classifier. The difference in the BLEU scores between out of domain and domain-specific translation is proved clearly using the word embeddings from characteristic vocabulary extracted using the extracted additional bitexts.
> 
> BIBREF2 ( BIBREF2 ) extract parallel sentences without

#### Relevance 1528

Label: 

#### Passage 1529

Retrieved by: Hybrid RRF followed by BGE reranking

> In this section, we will describe the entire pipeline, depicted in Figure FIGREF5 , which is involved in training a parallel sentence extraction system, and also to infer and decode high-precision nearly-parallel sentence-pairs from bilingual article pages collected from Wikipedia.

#### Relevance 1529

Label: 

## Question 0166

Paper: Character-Level Models versus Morphology in Semantic Role Labeling

> What morphological typologies are considered?

### Common Retrieved Chunks

#### Passage 1530

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> capabilities. Furthermore, their behaviour across languages from different families; and their limitations and strengths such as handling of long-range dependencies, reaction to model complexity or performance on out-of-domain data are unknown. Analyzing such issues is a key to fully understanding the character-level models.
> 
> To achieve this, we perform a case study on semantic role labeling (SRL), a sentence-level semantic analysis task that aims to identify predicate-argument structures and assign meaningful labels to them as follows:
> 
> $[$ Villagers $]$ comers came $[$ to town $]$ end point
> 
> We use a simple method based on bidirectional LSTMs to train three types of base semantic role labelers that employ (1) words (2) characters and character sequences and (3) gold morphological analysis. The gold morphology serves as the upper bound for us to compare and analyze the performances of character-level models on languages of varying morphological typologies. We carry out an exhaustive error analysis for each language type and analyze the strengths and limitations of character-level models compared to morphology. In regard to the diversity hypothesis which states that diversity of systems in ensembles lead to further improvement, we combine character and morphology-level models and measure the performance of the ensemble to better understand how similar they are.
> 
> We experiment with several languages with varying degrees of morphological richness and typology: Turkish, Finnish, Czech, German, Spanish, Catalan and English. Our experiments and analysis reveal insights such as:

#### Relevance 1530

Label: 

#### Passage 1531

Retrieved by: BM25, Hybrid RRF

> Throughout this paper, our aim was to gain insights on how models perform on different languages rather than scoring the highest F1. For this reason, we used a model that can be considered small when compared to recent neural SRL models and avoided parameter search. However, we wonder how the models behave when given a larger network. To answer this question, we trained char3 and oracle models with more layers for two fusional languages (Spanish, Catalan), and two agglutinative languages (Finnish, Turkish). The results given in Table 6 clearly shows that model complexity provides relatively more benefit to morphological models. This indicates that morphological signals help to extract more complex linguistic features that have semantic clues.

#### Relevance 1531

Label: 

#### Passage 1535

Retrieved by: Dense, Hybrid RRF

> We use three types of units: (1) words (2) characters and character sequences and (3) outputs of morphological analysis. Words serve as a lower bound; while morphology is used as an upper bound for comparison. Table 1 shows sample outputs of various $\rho $ functions.
> 
> Here, char function simply splits the token into its characters. Similar to n-gram language models, char3 slides a character window of width $n=3$ over the token. Finally, gold morphological features are used as outputs of morph-language. Throughout this paper, we use morph and oracle interchangably, i.e., morphology-level models (MLM) have access to gold tags unless otherwise is stated. For all languages, morph outputs the lemma of the token followed by language specific morphological tags. As an exception, it outputs additional information for some languages, such as parts-of-speech tags for Turkish. Word segmenters such as Morfessor and Byte Pair Encoding (BPE) are other commonly used subword units. Due to low scores obtained from our preliminary experiments and unsatisfactory results from previous studies BIBREF13 , we excluded these units.

#### Relevance 1535

Label: 

#### Passage 1536

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Our main results on test and development sets for models that use words, characters (char), character trigrams (char3) and morphological analyses (morph) are given in Table 3 . We calculate improvement over word (IOW) for each subword model and improvement over the best character model (IOC) for the morph. IOW and IOC values are calculated on the test set.
> 
> The biggest improvement over the word baseline is achieved by the models that have access to morphology for all languages (except for English) as expected. Character trigrams consistently outperformed characters by a small margin. Same pattern is observed on the results of the development set. IOW has the values between 0% to 38% while IOC values range between 2%-10% dependending on the properties of the language and the dataset. We analyze the results separately for agglutinative and fusional languages and reveal the links between certain linguistic phenomena and the IOC, IOW values.

#### Relevance 1536

Label: 

#### Passage 1537

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Encoding of words is perhaps the most important step towards a successful end-to-end natural language processing application. Although word embeddings have been shown to provide benefit to such models, they commonly treat words as the smallest meaning bearing unit and assume that each word type has its own vector representation. This assumption has two major shortcomings especially for languages with rich morphology: (1) inability to handle unseen or out-of-vocabulary (OOV) word-forms (2) inability to exploit the regularities among word parts. The limitations of word embeddings are particularly pronounced in sentence-level semantic tasks, especially in languages where word parts play a crucial role. Consider the Turkish sentences “Köy+lü-ler (villagers) şehr+e (to town) geldi (came)” and “Sendika+lı-lar (union members) meclis+e (to council) geldi (came)”. Here the stems köy (village) and sendika (union) function similarly in semantic terms with respect to the verb come (as the origin of the agents of the verb), where şehir (town) and meclis (council) both function as the end point. These semantic similarities are determined by the common word parts shown in bold. However ortographic similarity does not always correspond to semantic similarity. For instance the ortographically similar words knight and night have large semantic differences. Therefore, for a successful semantic application, the model should be able to capture both the regularities, i.e, morphological tags and the irregularities, i.e, lemmas of the word.
> 
> Morphological analysis already provides the aforementioned information about the words. However access to useful morphological features may be problematic due to software licensing issues, lack of robust morphological analyzers and high ambiguity among analyses. Character-level models (CLM), being a cheaper and accessible alternative to morphology, have been reported as performing competitively on various NLP tasks BIBREF0 , BIBREF1 , BIBREF2 . However the extent to which these tasks depend on morphology is small; and their relation to semantics is weak. Hence, little is known on their true ability to reveal the underlying morphological structure of a word and their semantic capabilities. Furthermore, their behaviour across languages from different families; and their limitations and strengths such as handling of long-range dependencies, reaction to model complexity or performance on out-of-domain data are unknown. Analyzing such issues is a key to fully understanding

#### Relevance 1537

Label: 

### BM25

#### Passage 1532

Retrieved by: BM25

> We analyzed how char3 and oracle models perform with respect to the training data size. For that purpose, we trained them on chunks of increasing size and evaluate on the provided test split. We used units of 2000 sentences for German and Czech; and 400 for Turkish. Results are shown in Fig. 4 . Apparently as the data size increases, the performances of both models logarithmically increase - with a varying speed. To speak in statistical terms, we fit a logarithmic curve to the observed F1 scores (shown with transparent lines) and check the x coefficients, where x refers to the number of sentences. This coefficient can be considered as an approximation to the speed of growth with data size. We observe that the coefficient is higher for char3 than oracle for all languages. It can be interpreted as: in the presence of more training data, char3 may surpass the oracle; i.e., char3 relies on data more than the oracle.

#### Relevance 1532

Label: 

#### Passage 1533

Retrieved by: BM25

> To fit the requirements of the SRL task and of our model, we performed the following:
> 
> Multiword expressions (MWE) are represented as a single token, (e.g., Confederación_Francesa_del_Trabajo), that causes notably long character sequences which are hard to handle by LSTMs. For the sake of memory efficiency and performance, we used an abbreviation (e.g., CFdT) for each MWE during training and testing.
> 
> Original dataset defines its own format of semantic annotation, such as 17:PBArgM_mod $\mid $ 19:PBArgM_mod meaning the node is an argument of $17_{th}$ and $19_{th}$ tokens with ArgM-mod (temporary modifier) semantic role. They have been converted into CoNLL-09 tabular format, where each predicate's arguments are given in a specific column.
> 
> Words are splitted from derivational boundaries in the original dataset, where each inflectional group is represented as a separate token. We first merge boundaries of the same word, i.e, tokens of the word, then we use our own $\rho $ function to split words into subwords.
> 
> We lowercase all tokens beforehand and place special start and end of the token characters. For all experiments, we initialized weight parameters orthogonally and used one layer bi-LSTMs both for subword composition and argument labeling with hidden size of 200. Subword embedding size is chosen as 200. We used gradient clipping and early stopping to prevent overfitting. Stochastic gradient descent is used as the optimizer. The initial learning rate is set to 1 and reduced by half if scores on development set do not improve after 3 epochs. We use the provided splits and evaluate the results with the official evaluation script provided by CoNLL-09 shared task. In this work (and in most of the recent SRL works), only the scores for argument labeling are reported, which may cause confusions for the readers while comparing with older SRL studies. Most of the early SRL work report combined scores (argument labeling with predicate sense disambiguation (PSD)). However, PSD is considered a simpler task with higher F1 scores . Therefore, we believe omitting PSD helps us gain more useful insights on character level models.

#### Relevance 1533

Label: 

#### Passage 1534

Retrieved by: BM25

> Although models with access to gold morphological tags achieve better F1 scores than character models, they can be less useful a in real-life scenario since they require gold tags at test time. To predict the performance of morphology-level models in such a scenario, we train the same models with the same parameters with predicted morphological features. Predicted tags were only available for German, Spanish, Catalan and Czech. Our results given in Fig. 5 , show that (except for Czech), predicted morphological tags are not as useful as characters alone.

#### Relevance 1534

Label: 

### Dense

#### Passage 1538

Retrieved by: Dense

> One way to infer similarity is to measure diversity. Consider a set of baseline models that are not diverse, i.e., making similar errors with similar inputs. In such a case, combination of these models would not be able to overcome the biases of the learners, hence the combination would not achieve a better result. In order to test if character and morphological models are similar, we combine them and measure the performance of the ensemble. Suppose that a prediction $p_{i}$ is generated for each token by a model $m_i$ , $i \in n$ , then the final prediction is calculated from these predictions by:
> 
> $$p_{final} = f(p_0, p_1,..,p_n|\phi )$$   (Eq. 36)
> 
> where $f$ is the combining function with parameter $\phi $ . The simplest global approach is averaging (AVG), where $f$ is simply the mean function and $p_i$ s are the log probabilities. Mean function combines model outputs linearly, therefore ignores the nonlinear relation between base models/units. In order to exploit nonlinear connections, we learn the parameters $\phi $ of $f$ via a simple linear layer followed by sigmoid activation. In other words, we train a new model that learns how to best combine the predictions from subword models. This ensemble technique is generally referred to as stacking or stacked generalization (SG).
> 
> Although not guaranteed, diverse models can be achieved by altering the input representation, the learning algorithm, training data or the hyperparameters. To ensure that the only factor contributing to the diversity of the learners is the input representation, all parameters, training data and model settings are left unchanged.
> 
> Our results are given in Table 4 . IOB shows the improvement over the best of the baseline models in the ensemble. Averaging and stacking methods gave similar results, meaning that there is no immediate nonlinear relations between units. We observe two language clusters: (1) Czech and agglutinative languages (2) Spanish, Catalan, German and English. The common property of that separate clusters are (1) high OOV% and (2) relatively low OOV%. Amongst the first set, we observe that the improvement gained by character-morphology ensembles is higher (shown with green) than ensembles between characters and character trigrams (shown with red), whereas the opposite is true for

#### Relevance 1538

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1539

Retrieved by: Hybrid RRF followed by BGE reranking

> OOV% and (2) relatively low OOV%. Amongst the first set, we observe that the improvement gained by character-morphology ensembles is higher (shown with green) than ensembles between characters and character trigrams (shown with red), whereas the opposite is true for the second set of languages. It can be interpreted as character level models being more similar to the morphology level models for the first cluster, i.e., languages with high OOV%, and characters and morphology being more diverse for the second cluster.

#### Relevance 1539

Label: 

#### Passage 1540

Retrieved by: Hybrid RRF followed by BGE reranking

> We use the datasets distributed by LDC for Catalan (CAT), Spanish (SPA), German (DEU), Czech (CZE) and English (ENG) BIBREF17 , BIBREF18 ; and datasets made available by BIBREF19 , BIBREF20 for Finnish (FIN) and Turkish (TUR) respectively . Datasets are provided with syntactic dependency annotations and semantic roles of verbal predicates. In addition, English supplies nominal predicates annotated with semantic roles and does not provide any morphological feature.
> 
> Statistics for the training split for all languages are given in Table 2 . Here, #pred is number of predicates, and #role refers to number distinct semantic roles that occur more than 10 times. More detailed statistics about the datasets can be found in BIBREF27 , BIBREF19 , BIBREF20 .

#### Relevance 1540

Label: 

## Question 0167

Paper: A Generalized Recurrent Neural Architecture for Text Classification with Multi-Task Learning

> What recurrent neural networks are explored?

### Common Retrieved Chunks

#### Passage 1541

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> There are a large body of literatures related to multi-task learning with neural networks in NLP BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 .
> 
> BIBREF8 belongs to Type-I and utilizes shared lookup tables for common features, followed by task-specific neural layers for several traditional NLP tasks such as part-of-speech tagging and semantic parsing. They use a fix-size window to solve the problem of variable-length texts, which can be better handled by recurrent neural networks.
> 
> BIBREF9 , BIBREF10 , BIBREF11 all belong to Type-II where samples from different tasks are learned sequentially. BIBREF9 applies bag-of-word representation and information of word orders are lost. BIBREF10 introduces an external memory for information sharing with a reading/writing mechanism for communicating, and BIBREF11 proposes three different models for multi-task learning with recurrent neural networks. However, models of these two papers only involve pair-wise interactions, which can be regarded as specific implementations of Coupling Layer and Fusion Layer in our model.
> 
> Different from the above models, our model focuses on Type-III and utilize recurrent neural networks to comprehensively capture various interactions among tasks, both direct and indirect, local and global. Three or more tasks are learned simultaneously and samples from different tasks are trained in parallel benefitting from each other, thus obtaining better sentence representations.

#### Relevance 1541

Label: 

#### Passage 1542

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Recently neural network based models have obtained substantial interests in many natural language processing tasks for their capabilities to represent variable-length text sequences as fix-length vectors, for example, Neural Bag-of-Words (NBOW), Recurrent Neural Networks (RNN), Recursive Neural Networks (RecNN) and Convolutional Neural Network (CNN). Most of them first map sequences of words, n-grams or other semantic units into embedding representations with a pre-trained lookup table, then fuse these vectors with different architectures of neural networks, and finally utilize a softmax layer to predict categorical distribution for specific classification tasks. For recurrent neural network, input vectors are absorbed one by one in a recurrent way, which makes RNN particularly suitable for natural language processing tasks.

#### Relevance 1542

Label: 

#### Passage 1543

Retrieved by: BM25, Dense, Hybrid RRF

> We apply the optimal hyperparameter settings and compare our model against the following state-of-the-art models:
> 
> NBOW Neural Bag-of-Words that simply sums up embedding vectors of all words.
> 
> PV Paragraph Vectors followed by logistic regression BIBREF21 .
> 
> MT-RNN Multi-Task learning with Recurrent Neural Networks by a shared-layer architecture BIBREF11 .
> 
> MT-CNN Multi-Task learning with Convolutional Neural Networks BIBREF8 where lookup tables are partially shared.
> 
> MT-DNN Multi-Task learning with Deep Neural Networks BIBREF9 that utilizes bag-of-word representations and a hidden shared layer.
> 
> GRNN Gated Recursive Neural Network for sentence modeling BIBREF1 .
> 
> As Table TABREF48 shows, our model obtains competitive or better performances on all tasks except for the QC dataset, as it contains poor correlations with other tasks. MT-RNN slightly outperforms our model on SST, as sentences from this dataset are much shorter than those from IMDB and MDSD, and another possible reason may be that our model are more complex and requires larger data for training. Our model proposes the designs of various interactions including coupling, local and global fusion, which can be further implemented by other state-of-the-art models and produce better performances.

#### Relevance 1543

Label: 

#### Passage 1544

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> Neural network based models have been widely exploited with the prosperities of Deep Learning BIBREF0 and achieved inspiring performances on many NLP tasks, such as text classification BIBREF1 , BIBREF2 , semantic matching BIBREF3 , BIBREF4 and machine translation BIBREF5 . These models are robust at feature engineering and can represent words, sentences and documents as fix-length vectors, which contain rich semantic information and are ideal for subsequent NLP tasks.
> 
> One formidable constraint of deep neural networks (DNN) is their strong reliance on large amounts of annotated corpus due to substantial parameters to train. A DNN trained on limited data is prone to overfitting and incapable to generalize well. However, constructions of large-scale high-quality labeled datasets are extremely labor-intensive. To solve the problem, these models usually employ a pre-trained lookup table, also known as Word Embedding BIBREF6 , to map words into vectors with semantic implications. However, this method just introduces extra knowledge and does not directly optimize the targeted task. The problem of insufficient annotated resources is not solved either.
> 
> Multi-task learning leverages potential correlations among related tasks to extract common features, increase corpus size implicitly and yield classification improvements. Inspired by BIBREF7 , there are a large literature dedicated for multi-task learning with neural network based models BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 . These models basically share some lower layers to capture common features and further feed them to subsequent task-specific layers, which can be classified into three types:
> 
> In this paper, we propose a generalized multi-task learning architecture with four types of recurrent neural layers for text classification. The architecture focuses on Type-III, which involves more complicated interactions but has not been researched yet. All the related tasks are jointly integrated into a single system and samples from different tasks are trained in parallel. In our model, every two tasks can directly interact with each other and selectively absorb useful information, or communicate indirectly via a shared intermediate layer. We also design a global memory storage to share common features and collect interactions among all tasks.
> 
> We conduct extensive experiments on five benchmark datasets for text classification. Compared to learning separately, jointly learning multiple relative tasks in our model demonstrate

#### Relevance 1544

Label: 

#### Passage 1545

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> A recurrent neural network maintains a internal hidden state vector INLINEFORM0 that is recurrently updated by a transition function INLINEFORM1 . At each time step INLINEFORM2 , the hidden state INLINEFORM3 is updated according to the current input vector INLINEFORM4 and the previous hidden state INLINEFORM5 . DISPLAYFORM0
> 
> where INLINEFORM0 is usually a composition of an element-wise nonlinearity with an affine transformation of both INLINEFORM1 and INLINEFORM2 .
> 
> In this way, recurrent neural networks can comprehend a sequence of arbitrary length into a fix-length vector and feed it to a softmax layer for text classification or other NLP tasks. However, gradient vector of INLINEFORM0 can grow or decay exponentially over long sequences during training, also known as the gradient exploding or vanishing problems, which makes it difficult to learn long-term dependencies and correlations for RNNs.
> 
> BIBREF12 proposed Long Short-Term Memory Network (LSTM) to tackle the above problems. Apart from the internal hidden state INLINEFORM0 , LSTM also maintains a internal hidden memory cell and three gating mechanisms. While there are numerous variants of the standard LSTM, here we follow the implementation of BIBREF13 . At each time step INLINEFORM1 , states of the LSTM can be fully represented by five vectors in INLINEFORM2 , an input gate INLINEFORM3 , a forget gate INLINEFORM4 , an output gate INLINEFORM5 , the hidden state INLINEFORM6 and the memory cell INLINEFORM7 , which adhere to the following transition functions. DISPLAYFORM0
> 
> where INLINEFORM0 is the current input, INLINEFORM1 denotes logistic sigmoid function and INLINEFORM2 denotes element-wise multiplication. By selectively controlling portions of the memory cell INLINEFORM3 to update, erase and forget at each time step, LSTM can better comprehend long-term dependencies with respect to labels of the whole sequences.

#### Relevance 1545

Label: 

#### Passage 1546

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this paper, we propose a multi-task learning architecture for text classification with four types of recurrent neural layers. The architecture is structurally flexible and can be regarded as a generalized case of many previous works with deliberate designs. We explore three different scenarios of multi-task learning and our model can improve performances of most tasks with additional related information from others in all scenarios.
> 
> In future work, we would like to investigate further implementations of couplings and fusions, and conclude more multi-task learning perspectives.

#### Relevance 1546

Label: 

### BM25

None

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0168

Paper: Socioeconomic Dependencies of Linguistic Patterns in Twitter: A Multivariate Analysis

> How do they combine the socioeconomic maps with Twitter data? 

### Common Retrieved Chunks

#### Passage 1547

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Data collected from Twitter provides a large variety of information about several users including their tweets, which disclose their interests, vocabulary, and linguistic patterns; their direct mentions from which their social interactions can be inferred; and the sequence of their locations, which can be used to infer their representative location. However, no information is directly available regarding their socioeconomic status, which can be pivotal to understand the dynamics and structure of their personal linguistic patterns.
> 
> To overcome this limitation we combined our Twitter data with the socioeconomic maps of INSEE by assigning each geolocated Twitter user to a patch closest to their estimated home location (within 1 km). This way we obtained for all $110,369$ geolocated users their dynamical linguistic data, their egocentric social network as well as a set of SES indicators.
> 
> Such a dataset associating language with socioeconomic status and social network throughout the French metropolitan territory is unique to our knowledge and provides unrivaled opportunities to verify sociolinguistic patterns observed over a long period on a small-scale, but never established in such a large population.
> 
> To verify whether the geolocated Twitter users yet provide a representative sample of the whole population we compared the distribution and correlations of the their SES indicators to the population measures. Results are shown in Fig. 1 b diagonal (red distributions) and lower diagonal panels (in blue) with correlation coefficients and $p$ -values summarized in Table. 1 . Even if we observed some discrepancy between the corresponding distributions and somewhat weaker correlations between the SES indicators, we found the same significant correlation trends (with the exception of the pair density / income) as the ones seen when studying the whole population, assuring us that each indicator correctly reflected the SES of individuals.

#### Relevance 1547

Label: 

#### Passage 1548

Retrieved by: BM25, Dense, Hybrid RRF

> For decades, sociolinguistic studies have repeatedly shown that speakers vary the way they talk depending on several factors. These studies have usually been limited to the analysis of small scale datasets, often obtained by surveying a set of individuals, or by direct observation after placing them in a controlled experimental setting. In spite of the volume of data collected generally, these studies have consistently shown the link between linguistic variation and social factors BIBREF10 , BIBREF11 .
> 
> Recently, the advent of social media and publicly available communication platforms has opened up a new gate to access individual information at a massive scale. Among all available social platforms, Twitter has been regarded as the choice by default, namely thanks to the intrinsic nature of communications taking place through it and the existence of data providers that are able to supply researchers with the volume of data they require. Work previously done on demographic variation is now relying increasingly on corpora from this social media platform as evidenced by the myriad of results showing that this resource reflects not only morpholexical variation of spoken language but also geographical BIBREF12 , BIBREF13 .
> 
> Although the value of this kind of platform for linguistic analysis has been more than proven, the question remains on how previous sociolinguistic results scale up to the sheer amount of data within reach and how can the latter enrich the former. To do so, numerous studies have focused on enhancing the data emanating from Twitter itself. Indeed, one of the core limitations of Twitter is the lack of reliable sociodemographic information about the sampled users as usually data fields such as user-entered profile locations, gender or age differ from reality. This in turn implies that user-generated profile content cannot be used as a useful proxy for the sociodemographic information BIBREF14 .
> 
> Many studies have overcome this limitation by taking advantage of the geolocation feature allowing Twitter users to include in their posts the location from which they were tweeted. Based on this metadata, studies have been able to assign home location to geolocated users with varying degrees of accuracy BIBREF15 . Subsequent work has also been devoted to assigning to each user some indicator

#### Relevance 1548

Label: 

#### Passage 1550

Retrieved by: BM25, Dense, Hybrid RRF

> One of the main achievements of our study was the construction of a combined dataset for the analysis of sociolinguistic variables as a function of socioeconomic status, geographic location, time, and the social network. As follows, we introduce the two aforementioned independent datasets and how they were combined. We also present a brief cross-correlation analysis to ground the validity of our combined dataset for the rest of the study. In what follows, it should also be noted that regression analysis was performed via linear regression as implemented in the Scikit Learn Toolkit while data preprocessing and network study were performed using respectively pandas BIBREF23 and NetworkX BIBREF24 Python libraries.

#### Relevance 1550

Label: 

#### Passage 1551

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The overall goal of our study was to explore the dependencies of linguistic variables on the socioeconomic status, location, time varying activity, and social network of users. To do so we constructed a combined dataset from a large Twitter data corpus, including geotagged posts and proxy social interactions of millions of users, as well as a detailed socioeconomic map describing average socioeconomic indicators with a high spatial resolution in France. The combination of these datasets provided us with a large set of Twitter users all assigned to their Twitter timeline over three years, their location, three individual socioeconomic indicators, and a set of meaningful social ties. Three linguistic variables extracted from individual Twitter timelines were then studied as a function of the former, namely, the rate of standard negation, the rate of plural agreement and the size of vocabulary set.
> 
> Via a detailed multidimensional correlation study we concluded that (a) socioeconomic indicators and linguistic variables are significantly correlated. i.e. people with higher socioeconomic status are more prone to use more standard variants of language and a larger vocabulary set, while people on the other end of the socioeconomic spectrum tend to use more non-standard terms and, on average, a smaller vocabulary set; (b) Spatial position was also found to be a key feature of standard language use as, overall, people from the North tended to use more non-standard terms and a smaller vocabulary set compared to people from the South; a more fine-grained analysis reveals that the spatial variability of language is determined to a greater extent locally by the socioeconomic status; (c) In terms of temporal activity, standard language was more likely to be used during the daytime while non-standard variants were predominant during the night. We explained this temporal variability by the turnover of population with different socioeconomic status active during night and day; Finally (d) we showed that the social network and status homophily mattered in terms of linguistic similarity between peers, as connected users with the same socioeconomic status appeared to be the most similar, while disconnected people were found to be the most dissimilar in terms of their individual use of the aforementioned linguistic markers.
> 
> Despite these findings, one has

#### Relevance 1551

Label: 

#### Passage 1552

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> from which they were tweeted. Based on this metadata, studies have been able to assign home location to geolocated users with varying degrees of accuracy BIBREF15 . Subsequent work has also been devoted to assigning to each user some indicator that might characterize their socioeconomic status based on their estimated home location. These indicators are generally extracted from other datasets used to complete the Twitter one, namely census data BIBREF16 , BIBREF12 , BIBREF17 or real estate online services as Zillow.com BIBREF18 . Other approaches have also relied on sources of socioeconomic information such as the UK Standard Occupation Classification (SOC) hierarchy, to assign socioeconomic status to users with occupation mentions BIBREF19 . Despite the relative success of these methods, their common limitation is to provide observations and predictions based on a carefully hand-picked small set of users, letting alone the problem of socioeconomic status inference on larger and more heterogeneous populations. Our work stands out from this well-established line of research by expanding the definition of socioeconomic status to include several demographic features as well as by pinpointing potential home location to individual users with an unprecedented accuracy. Identifying socioeconomic status and the network effects of homophily BIBREF20 is an open question BIBREF21 . However, recent results already showed that status homophily, i.e. the tendency of people of similar socioeconomic status are better connected among themselves, induce structural correlations which are pivotal to understand the stratified structure of society BIBREF22 . While we verify the presence of status homophily in the Twitter social network, we detect further sociolinguistic correlations between language, location, socioeconomic status, and time, which may inform novel methods to infer socioeconomic status for a broader set of people using common information available on Twitter.

#### Relevance 1552

Label: 

### BM25

#### Passage 1549

Retrieved by: BM25

> been described in many languages: variable pronunciation of -ing as [in] instead of [iŋ] in English (playing pronounced playin'); optional realization of the first part of the French negation (je (ne) fume pas, "I do not smoke"); optional realization of the plural ending of verb in Brazilian Portuguese (eles disse(ram), "they said"). For decades, sociolinguistic studies have showed that hearing certain variants triggers social stereotypes BIBREF5 . The so-called standard variants (e.g. [iŋ], realization of negative ne and plural -ram) are associated with social prestige, high education, professional ambition and effectiveness. They are more often produced in more formal situation. Non-standard variants are linked to social skills, solidarity and loyalty towards the local group, and they are produced more frequently in less formal situation.
> 
> It is therefore reasonable to say that the sociolinguistic task can benefit from the rapid development of computational social science BIBREF6 : the similarity of the online communication and face-to-face interaction BIBREF7 ensures the validity of the comparison with previous works. In this context, the nascent field of computational sociolinguistics found the digital counterparts of the sociolinguistic patterns already observed in spoken interaction. However a closer collaboration between computer scientists and sociolinguists is needed to meet the challenges facing the field BIBREF8 :
> 
> The present work meets most of these challenges. It constructs the largest dataset of French tweets enriched with census sociodemographic information existent to date to the best of our knowledge. From this dataset, we observed variation of two grammatical cues and an index of vocabulary size in users located in France. We study how the linguistic cues correlated with three features reflective of the socioeconomic status of the users, their most representative location and their daily periods of activity on Twitter. We also observed whether connected people are more linguistically alike than disconnected ones. Multivariate analysis shows strong correlations between linguistic cues and socioeconomic status as well as a broad spatial pattern never observed before, with more standard language variants and lexical diversity in the southern part of the country. Moreover, we found an unexpected daily cyclic evolution of the frequency of standard variants. Further analysis revealed that the observed cycle arose from the ever changing average economic

#### Relevance 1549

Label: 

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1553

Retrieved by: Hybrid RRF followed by BGE reranking

> The socioeconomic status of a person is arguably correlated with education level, income, habitual location, or even with ethnicity and political orientation and may strongly determine to some extent patterns of individual language usage. Such dependencies have been theoretically proposed before BIBREF11 , but have rarely been inspected at this scale yet. The use of our previously described datasets enabled us to do so via the measuring of correlations between the inferred SES indicators of Twitter users and the use of the previously described linguistic markers.
> 
> To compute and visualize these correlations we defined linear bins (in numbers varying from 20 to 50) for the socioeconomic indicators and computed the average of the given linguistic variables for people falling within the given bin. These binned values (shown as symbols in Fig. 2 ) were used to compute linear regression curves and the corresponding confidence intervals (see Fig. 2 ). An additional transformation was applied to the SES indicator describing population density, which was broadly distributed (as discussed in Section "INSEE dataset: socioeconomic features" and Fig. 1 b), thus, for the regression process, the logarithm of its values were considered. To quantify pairwise correlations we computed the $R^2$ coefficient of determination values in each case.
> 
> In Fig. 2 we show the correlation plots of all nine pairs of SES indicators and linguistic variables together with the linear regression curves, the corresponding $R^2$ values and the 95 percentile confidence intervals (note that all values are also in Table 2 ). These results show that correlations between socioeconomic indicators and linguistic variables actually exist. Furthermore, these correlation trends suggest that people with lower SES may use more non-standard expressions (higher rates of incorrect negation and plural forms) have a smaller vocabulary set size than people with higher SES. Note that, although the observed variation of linguistic variables were limited, all the correlations were statistically significant ( $p<10^{-2}$ ) with considerably high $R^2$ values ranging from $0.19$ (between $\overline{L}_{\mathrm {cn}}\sim S_\mathrm {inc}$ ) to $0.76$ (between $\overline{L}_{\mathrm {cp}}\sim S_\mathrm {den}$ ). For the rates of standard negation and plural terms the population density appeared to be the most determinant indicator with $R^2=0.74$ (and $0.76$ respectively), while for the vocabulary

#### Relevance 1553

Label: 

#### Passage 1554

Retrieved by: Hybrid RRF followed by BGE reranking

> each user, we extracted the sequence of all declared locations from their geolocated tweets. Using this set of locations we selected the most frequent to be the representative one, and we took it as a proxy for the user's home location. Further we limited our users to ones located throughout the French territory thus not considering others tweeting from places outside the country. This selection method provided us with $110,369$ geolocated users who are either detected as French speakers or assigned to be such by Twitter and all associated to specific 'home' GPS coordinates in France. To verify the spatial distribution of the selected population, we further assessed the correlations between the true population distributions (obtained from census data BIBREF28 ) at different administrative level and the geolocated user distribution aggregated correspondingly. More precisely, we computed the $R^2$ coefficient of variation between the inferred and official population distributions (a) at the level of 22 regions. Correlations at this level induced a high coefficient of $R^2\simeq 0.89$ ( $p<10^{-2}$ ); (b) At the arrondissement level with 322 administrative units and coefficient $R^2\simeq 0.87$ ( $p<10^{-2}$ ); and (c) at the canton level with 4055 units with a coefficient $R\simeq 0.16$ ( $p<10^{-2}$ ). Note that the relatively small coefficient at this level is due to the interplay of the sparsity of the inferred data and the fine grained spatial resolution of cantons. All in all, we can conclude that our sample is highly representative in terms of spatial population distribution, which at the same time validate our selection method despite the potential inherent biases induced by the method taking the most frequented GPS coordinates as the user's home location.

#### Relevance 1554

Label: 

## Question 0169

Paper: Understanding the Radical Mind: Identifying Signals to Detect Extremist Content on Twitter

> What languages feature in the dataset?

### Common Retrieved Chunks

#### Passage 1555

Retrieved by: BM25, Hybrid RRF

> In this paper, we identified different signals that can be utilized to detect evidence of online radicalization. We derived linguistic and psychological properties from propaganda published by ISIS for recruitment purposes. We utilize these properties to detect pro-ISIS tweets that are influenced by their ideology. Unlike previous efforts, these properties do not only focus on lexical keyword analysis of the messages, but also add a contextual and psychological dimension. We validated our approach in different experiments and the results show that this method is robust across multiple datasets. This system can aid law enforcement and OSN companies to better address such threats and help solve a challenging real-world problem. In future work, we aim to investigate if the model is resilient to different evasion techniques that users may adopt. We will also expand the analysis to other languages.

#### Relevance 1555

Label: 

#### Passage 1556

Retrieved by: BM25, Dense, Hybrid RRF

> We remove those from the dataset and only keep users that are still active on Twitter. This dataset is labelled as counterpoise data.
> 
> We performed a series of preprocessing steps to clean the complete dataset and prepare it for feature extraction. These steps are: (1) We remove any duplicates and re-tweets from the dataset in order to reduce noise. (2) We remove tweets that have been authored by verified users accounts, as they are typically accounts associated with known public figures. (3) All stop words (e.g., and, or, the) and punctuation marks are removed from the text of the tweet. (4) If the tweet text contains a URL, we record the existence of the URL in a new attribute, hasURL, and then remove it from the tweet text. (5) If the tweet text contains emojis (e.g., :-), :), :P), we record the existence of the emoji in a new attribute, hasEmj, and then remove it from the tweet text. (6) If the tweet text contains any words with all capital characters, we record its existence in a new attribute, allCaps, and then normalize the text to lower-case and filter out any non-alphabetic characters. (7) We tokenize the cleansed tweet text into words, then we perform lemmatization, the process of reducing inflected words to their roots (lemma), and store the result in a vector.

#### Relevance 1556

Label: 

#### Passage 1557

Retrieved by: BM25, Hybrid RRF

> We acquired a publicly available dataset of tweets posted by known pro-ISIS Twitter accounts that was published during the 2015 Paris attacks by Kaggle data science community. The dataset consists of around INLINEFORM0 tweets posted by more than 100 users. These tweets were labelled as being pro-ISIS by looking at specific indicators, such as a set of keywords used (in the user's name, description, tweet text), their network of follower/following of other known radical accounts, and sharing of images of the ISIS flag or some radical leaders. To validate that these accounts are indeed malicious, we checked the current status of the users' accounts in the dataset and found that most of them had been suspended by Twitter. This suggests that they did, in fact, possess a malicious behaviour that opposes the Twitter platform terms of use which caused them to be suspended. We filter out any tweets posted by existing active users and label this dataset as known-bad.
> 
> To model the normal behaviour, we collected a random sample of tweets from ten-trending topics in Twitter using the Twitter streaming API. These topics were related to news events and on-going social events (e.g., sports, music). We filter out any topics and keywords that may be connected to extremist views. This second dataset consists of around INLINEFORM0 tweets published by around INLINEFORM1 users. A random sample of 200 tweets was manually verified to ascertain it did not contain radical views. We label this dataset as our random-good data.
> 
> A third dataset is used which was acquired from Kaggle community. This dataset is created to be a counterpoise to the pro-ISIS dataset (our known-bad) as it consists of tweets talking about topics concerning ISIS without being radical. It contains INLINEFORM0 tweets from around INLINEFORM1 users collected on two separate days. We verify that this dataset is indeed non radical by checking the status of users in Twitter and found that a subset ( INLINEFORM2 users) was suspended. We remove those from the dataset and only keep users that are still active on Twitter. This dataset is labelled as counterpoise data.
> 
> We performed a series of preprocessing steps to clean the complete dataset and prepare it for feature

#### Relevance 1557

Label: 

#### Passage 1558

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Feature engineering is the process of exploring large spaces of heterogeneous features with the aim of discovering meaningful features that may aid in modeling the problem at hand. We explore three categories of information to identify relevant features to detect radical content. Some features are user-based while others are message-based. The three categories are: 1) Radical language (Textual features INLINEFORM0 ); 2) Psychological signals (Psychological features INLINEFORM1 ); and 3) Behavioural features ( INLINEFORM2 ). In the following, we detail each of these categories.
> 
> In order to understand how radical messages are constructed and used, as mentioned earlier, we analyze content of ISIS propaganda material published in Dabiq magazine. Dabiq is an online magazine published by ISIS terrorist groups with the purpose of recruiting people and promoting their propaganda and ideology. Using this data source, we investigate what topics, textual properties, and linguistic cues exist in these magazines. Our intuition is that utilising these linguistic cues from the extremist propaganda would allow us to detect supporters of ISIS group who are influenced by their propaganda.
> 
> We use two methods to extract the radical language from the propaganda corpus. First we calculate tf-idf scores for each gram in the propaganda corpus. We use uni-grams, bi-grams, and tri-grams to capture phrases and context in which words are being used. We then select the top scoring grams to be used as features for the language model. N-grams and words frequency have been used in the literature to classify similar problems, such as hate-speech and extremist text and have proven successful BIBREF16 . The second method we use is word embeddings to capture semantic meanings. Research in NLP has compared the effectiveness of word embedding methods for encoding semantic meaning and found that semantic relationships between words are best captured by word vectors within word embedding models BIBREF17 . Therefore, we train word2vec model on our propaganda corpus to build the lexical semantic aspects of the text using vector space models. We learn word embeddings using skip-gram word2vec model implemented in the gensim package with vector size of 100 and window size of 5. This word embedding model is used to obtain the vector representation for each word. We

#### Relevance 1558

Label: 

#### Passage 1559

Retrieved by: BM25, Dense, Hybrid RRF

> Exp 1: The classification results using the known-bad and random-good datasets are reported in Table TABREF16 . The table shows the average accuracy, precision, recall and f-measure scores obtained from each feature category ( INLINEFORM0 , INLINEFORM1 , INLINEFORM2 ) and their combination ( INLINEFORM3 ). We also compared the two textual models, and find that results obtained from using word embedding outperforms the use of n-grams tf-idf scores. This confirms that contextual information is important in detecting radicalization activities. Furthermore, our model performed best using the INLINEFORM4 features across all metrics. This means that the model is able to distinguish between both radical and non-radical with high confidence using only INLINEFORM5 .
> 
> Exp2: In this experiment, we tested the performance of our classifier in distinguishing between radical and normal tweets that discusses ISIS-related topics. Although this task is more challenging given the similarity of the topic discussed in the two classes, we find that the model still achieves high performance. Table TABREF17 shows the different metrics obtained from each feature category. The INLINEFORM0 feature group obtains 80% accuracy, and 91%, 100% for INLINEFORM1 and INLINEFORM2 feature groups, respectively. The results are consistent with the ones obtained from the first experiment with the features from INLINEFORM3 group contributing to the high accuracy of the model. The area under the Receiver Operator Characteristic (ROC) curve, which measures accuracy based on TP, and FP rates, is shown in Fig. FIGREF18 for each classification model.

#### Relevance 1559

Label: 

#### Passage 1561

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> space models. We learn word embeddings using skip-gram word2vec model implemented in the gensim package with vector size of 100 and window size of 5. This word embedding model is used to obtain the vector representation for each word. We aggregate the vectors for each word in the tweet, and concatenate the maximum and average for each word vector dimension, such that any given tweet is represented in 200 dimension sized vector. This approach of aggregating vectors was used successfully in previous research BIBREF18 . Moreover, since ISIS supporters typically advocate for violent behaviour and tend to use offensive curse words, we use dictionaries of violent words and curse words to record the ratio of such words in the tweet. We also count the frequency of words with all capital letters as they are traditionally used to convey yelling behaviour.
> 
> Research in fields such as linguistics, social science, and psychology suggest that the use of language and the word choices we make in our daily communication, can act as a powerful signal to detect our emotional and psychological states BIBREF8 . Several psychological properties are unintentionally transmitted when we communicate. Additionally, literature from the fields of terrorism and psychology suggests that terrorists may differ from non-terrorists in their psychological profiles BIBREF19 . A number of studies looked at the motivating factors surrounding terrorism, radicalization, and recruitment tactics, and found that terrorist groups tend to target vulnerable individuals who have feelings of desperation and displaced aggression. In particular research into the recruiting tactics of ISIS groups, it was found that they focus on harnessing the individual's need for significance. They seek out vulnerable people and provide them with constant attention BIBREF20 . Similarly, these groups create a dichotomy and promote the mentality of dividing the world into “us” versus “them” BIBREF21 . Inspired by previous research, we extract psychological properties from the radical corpus in order to understand the personality, emotions, and the different psychological properties conveyed in these articles.
> 
> We utilise LIWC dictionaries to assign a score to a set of psychological, personality, and emotional categories. Mainly, we look at the following properties: (1) Summary variables: Analytically thinking which reflects formal, logical, and hierarchical thinking

#### Relevance 1561

Label: 

### BM25

None

### Dense

#### Passage 1560

Retrieved by: Dense

> As illustrated in Fig. FIGREF1 , our approach consists of two main phases: Phase 1:Radical Properties Extraction, where articles from Dabiq extremist magazines are input into this step to perform two parallel tasks. In the first task, we build a language model using (i) Term-Frequency Inverse-Document-Frequency (TF-IDF) scores of uni-, bi-, and tri-grams, and (ii) Word embeddings generated from a word2vec model BIBREF15 . The output of this task is a radical corpus of top k-grams, and a word embedding model giving a vector representation for each word in the corpus. The second task seeks to create a psychological profile based on the language used in the extremist propaganda articles, consisting of a set of emotional and topical categories using LIWC dictionary-based tool. Phase 2: Tweet classification involves the use of the models generated from Phase 1 to engineer features related to radical activities. We identify three groups of features and then train a binary classifier to detect radical tweets.

#### Relevance 1560

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1562

Retrieved by: Hybrid RRF followed by BGE reranking

> conveyed in these articles.
> 
> We utilise LIWC dictionaries to assign a score to a set of psychological, personality, and emotional categories. Mainly, we look at the following properties: (1) Summary variables: Analytically thinking which reflects formal, logical, and hierarchical thinking (high value), versus informal, personal, and narrative thinking (low value). Clout which reflects high expertise and confidence levels (high value), versus tentative, humble, and anxious levels (low value). Tone which reflects positive emotions (high value) versus more negative emotions such as anxiety, sadness, or anger (low value). Authentic which reflects whether the text is conveying honesty and disclosing (high value) versus more guarded, and distanced (low value). (2) Big five: Measures the five psychological properties (OCEAN), namely Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. (3) Emotional Analysis: Measures the positive emotions conveyed in the text, and the negative emotions (including anger, sadness, anxiety). (4) Personal Drives: Focuses on five personal drives, namely power, reward, risk, achievement, and affiliation. (5) Personal Pronouns: Counts the number of 1st, 2nd, and 3rd personal pronouns used. For each Twitter user, we calculate their psychological profiles across these categories. Additionally, using Minkowski distance measure, we calculate the distance between each of these profiles and the average values of the psychological properties created from the ISIS magazines.
> 
> This category consists of measuring behavioural features to capture different properties related to the user and their behaviour. This includes how active the user is (frequency of tweets posted) and the followers/following ratio. Additionally, we use features to capture users' interactions with others through using hashtags, and engagement in discussions using mention action. To capture this, we construct the mention interaction graph ( INLINEFORM0 ) from our dataset, such that INLINEFORM1 = INLINEFORM2 , where INLINEFORM3 represents the user nodes and INLINEFORM4 represents the set of edges. The graph INLINEFORM5 is a directed graph, where an edge INLINEFORM6 exists between two user nodes INLINEFORM7 and INLINEFORM8 , if user INLINEFORM9 mentions user INLINEFORM10 . After constructing the graph, we measure the degree of influence each user has over their network using different centrality measures, such as degree centrality, betweenness centrality, and HITS-Hub. Such properties have been adopted in the research literature to study properties of

#### Relevance 1562

Label: 

#### Passage 1563

Retrieved by: Hybrid RRF followed by BGE reranking

> In recent years, there has been an increase in online accounts advocating and supporting terrorist groups such as ISIS BIBREF5 . This phenomenon has attracted researchers to study their online existence, and research ways to automatically detect these accounts and limit their spread. Ashcroft et al. BIBREF6 make an attempt to automatically detect Jihadist messages on Twitter. They adopt a machine-learning method to classify tweets as ISIS supporters or not. In the article, the authors focus on English tweets that contain a reference to a set of predefined English hashtags related to ISIS. Three different classes of features are used, including stylometric features, temporal features and sentiment features. However, one of the main limitations of their approach is that it is highly dependent on the data. Rowe and Saif BIBREF7 focused on studying Europe-based Twitter accounts in order to understand what happens before, during, and after they exhibit pro-ISIS behaviour. They define such behaviour as sharing of pro-ISIS content and/or using pro-ISIS terms. To achieve this, they use a term-based approach such that a user is considered to exhibit a radicalization behaviour if he/she uses more pro-ISIS terms than anti-ISIS terms. While such an approach seems effective in distinguishing radicalised users, it is unable to properly deal with lexical ambiguity (i.e., polysemy). Furthermore, in BIBREF11 the authors focused on detecting Twitter users who are involved with “Media Mujahideen”, a Jihadist group who distribute propaganda content online. They used a machine learning approach using a combination of data-dependent and data-independent features. Similar to BIBREF7 they used textual features as well as temporal features to classify tweets and accounts. The experiment was based on a limited set of Twitter accounts, which makes it difficult to generalize the results for a more complex and realistic scenario.
> 
> Radicalization literature also looked at psychological factors involved with adopting such behaviour. Torok BIBREF12 used a grounded theory approach to develop an explanatory model for the radicalization process utilizing concepts of psychiatric power. Their findings show that the process typically starts with the social isolation of individuals. This isolation seems to be self-imposed as individuals tend to spend a long time engaging with radical content. This leads to the concept of homophily,

#### Relevance 1563

Label: 

#### Passage 1564

Retrieved by: Hybrid RRF followed by BGE reranking

> we find that a number of existing studies incorporate methods to identify distinguishing properties that can aid in automatic detection of these users BIBREF6 , BIBREF7 . However, many of them depend on performing a keyword-based textual analysis which, if used alone, may have several shortcomings, such as producing a large number of false positives and having a high dependency on the data being studied. In addition, it can be evaded using automated tools to adjust the writing style.
> 
> Another angle for analyzing written text is by looking at the psychological properties that can be inferred regarding their authors. This is typically called psycholinguistics, where one examines how the use of the language can be indicative of different psychological states. Examples of such psychological properties include introversion, extroversion, sensitivity, and emotions. One of the tools that automates the process of extracting psychological meaning from text is the Linguistic Inquiry and Word Count (LIWC) BIBREF8 tool. This approach has been used in the literature to study the behaviour of different groups and to predict their psychological states, such as predicting depression BIBREF9 . More recently, it has also been applied to uncover different psychological properties of extremist groups and understand their intentions behind the recruitment campaigns BIBREF10 .
> 
> Building on the findings of previous research efforts, this paper aims to study the effects of using new textual and psycholinguistic signals to detect extremist content online. These signals are developed based on insights gathered from analyzing propaganda material published by known extremist groups. In this study, we focus mainly on the ISIS group as they are one of the leading terrorist groups that utilise social media to share their propaganda and recruit individuals. We analyze the propaganda material they publish in their online English magazine called Dabiq, and use data-mining techniques to computationally uncover contextual text and psychological properties associated with these groups. From our analysis of these texts, we are able to extract a set of signals that provide some insight into the mindset of the radical group. This allows us to create a general radical profile that we apply as a signal to detect pro-ISIS supporters on Twitter. Our results show that these identified signals

#### Relevance 1564

Label: 

## Question 0170

Paper: Creative GANs for generating poems, lyrics, and metaphors

> What objective function is used in the GAN?

### Common Retrieved Chunks

#### Passage 1565

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Language models can be optimized to recognize syntax and semantics with great accuracy BIBREF0. However, the output generated can be repetitive and generic leading to monotonous or uninteresting responses (e.g “I don't know”) regardless of the input BIBREF1. While application of attention BIBREF2, BIBREF3 and advanced decoding mechanisms like beam search and variation sampling BIBREF4 have shown improvements, it does not solve the underlying problem. In creative text generation, the objective is not strongly bound to the ground truth—instead the objective is to generate diverse, unique or original samples. We attempt to do this through a discriminator which can give feedback to the generative model through a cost function that encourages sampling of creative tokens. The contributions of this paper are in the usage of a GAN framework to generate creative pieces of writing. Our experiments suggest that generative text models, while very good at encapsulating semantic, syntactic and domain information, perform better with external feedback from a discriminator for fine-tuning objectiveless decoding tasks like that of creative text. We show this by evaluating our model on three very different creative datasets containing poetry, metaphors and lyrics.
> 
> Previous work on handling the shortcomings of MLE include length-normalizing sentence probability BIBREF5, future cost estimation BIBREF6, diversity-boosting objective function BIBREF7, BIBREF1 or penalizing repeating tokens BIBREF8. When it comes to poetry generation using generative text models, Zhang and Lapata BIBREF9, Yi et al. BIBREF10 and Wang et al. BIBREF11 use language modeling to generate Chinese poems. However, none of these methods provide feedback on the quality of the generated sample and hence, do not address the qualitative objective required for creative decoding. For the task of text generation, MaskGAN BIBREF12 uses a Reinforcement Learning signal from the discriminator, FMD-GAN BIBREF13 uses an optimal transport mechanism as an objective function. GumbelGAN BIBREF14 uses Gumbel-Softmax distribution that replaces the non-differentiable sample from a categorical distribution with a differentiable sample to propagate stronger gradients. Li et al. BIBREF1 use a discriminator for a diversity promoting objective. Yu et al. BIBREF15 use SeqGAN to generate poetry and comment on the performance of SeqGAN over MLE in human evaluations, encouraging our study of GANs for creative text generation. However, these studies do

#### Relevance 1565

Label: 

#### Passage 1566

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> a corpus of 14950 metaphor sentences retrieved from a metaphor database website and (3) a corpus of 1500 song lyrics ranging across genres. The mix of linguistic styles within this corpus offers the potential for interesting variation during the generation phase. We use the same pre-processing as in earlier work BIBREF19, BIBREF23. We reserve 10% of our data for test set and another 10% for our validation set.
> 
> We first pre-train our generator on the Gutenberg dataset BIBREF24 for 20 epochs and then fine-tune BIBREF19 them to our target datasets with a language modeling objective. The discriminator's encoder is initialized to the same weights as our fine-tuned language model. Once we have our fine-tuned encoders for each target dataset, we train in an adversarial manner. The discriminator objective here is to score the quality of the creative text. The discriminator is trained for 3 iterations for every iteration of the generator, a practice seen in previous work BIBREF25. Creative-GAN relies on using the reward from the discriminator BIBREF12, BIBREF15 for backpropagation. We follow a similar training procedure for GumbelGAN. Outputs are generated through sampling over a multinomial distribution for all methods, instead of $argmax$ on the log-likelihood probabilities, as sampling has shown to produce better output quality BIBREF4. Please refer to Supplementary Section Table TABREF6 for training parameters of each dataset and Table TABREF5 for hyperparameters of each encoder. We pick these values after experimentation with our validation set. Training and output generation code can be found online.

#### Relevance 1566

Label: 

#### Passage 1567

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Using GANs, we can train generative models in a two-player game setting between a discriminator and a generator, where the discriminator (a binary classifier) learns to distinguish between real and fake data samples and the generator tries to fool the discriminator by generating authentic and high quality output BIBREF16. GANs have shown to be successful in image generation tasks BIBREF17 and recently, some progress has been observed in text generation BIBREF13, BIBREF12, BIBREF15. Our generator is a language model trained using backpropagation through time BIBREF18. During the pre-training phase we optimize for MLE and during the GAN training phase, we optimize on the creativity reward from the discriminator. The discriminator's encoder has the same architecture as the generator encoder module with the addition of a pooled decoder layer. The decoder contains 3 $[Dense Batch Normalization,ReLU]$ blocks and an addtional $Sigmoid$ layer. The discriminator decoder takes the hidden state at the last time step of a sequence concatenated with both the max-pooled and mean-pooled representation of the hidden states BIBREF19 and outputs a number in the range $[0,1]$. The difficulty of using GANs in text generation comes from the discrete nature of text, making the model non-differentiable hence, we update parameters for the generator model with policy gradients as described in Yu BIBREF15.
> 
> We utilize AWD-LSTM BIBREF20 and TransformerXL BIBREF21 based language models. For model hyperparameters please to refer to Supplementary Section Table TABREF5. We use Adam optimizer BIBREF22 with $\beta 1= 0.7$ and $\beta 2= 0.8$ similar to BIBREF19 and use a batch size of 50. Other practices for LM training were the same as BIBREF21 and BIBREF20 for Transformer-XL and AWD-LSTM respectively. We refer to our proposed GAN as Creative-GAN and compare it to a baseline (a language model equivalent to our pre-trained generator) and a GumbelGAN model BIBREF14 across all proposed datasets. We use three creative English datasets with distinct linguistic characteristics: (1) A corpus of 740 classical and contemporary English poems, (2) a corpus of 14950 metaphor sentences retrieved from a metaphor database website and (3) a corpus of 1500 song lyrics ranging across genres. The mix of linguistic styles within this corpus offers the potential for interesting variation during the generation

#### Relevance 1567

Label: 

#### Passage 1568

Retrieved by: BM25, Dense, Hybrid RRF

> In this section, we report our results on computational metrics, hyperparameters and training configurations for our models. Table TABREF4 shows the results of the perplexity score evaluation of the evaluated models, Table TABREF5 shows hyperparameters for each encoding method and Table TABREF6 shows our training parameters. In Table TABREF6, the values for Gutenberg dataset in columns, GumbelGAN and Creative-GAN are empty as we only pretrain our LMs with the Gutenberg dataset

#### Relevance 1568

Label: 

#### Passage 1569

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> Evaluating creative generation tasks is both critical and complex BIBREF26. Along the lines of previous research on evaluating text generation tasks BIBREF26, we report the perplexity scores of our test set on the evaluated models in the Supplementary Section, Table TABREF4 Our model shows improvements over baseline and GumbelGAN. Common computational methods like BLEU BIBREF27 and perplexity are at best a heuristic and not strong indicators of good performance in text generation models BIBREF28. Particularly, since these scores use target sequences as a reference, it has the same pitfalls as relying on MLE. The advantages in this approach lie in the discriminator's ability to influence the generator to explore other possibilities. Sample outputs for our model can be found on our website .

#### Relevance 1569

Label: 

#### Passage 1570

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> discriminator for a diversity promoting objective. Yu et al. BIBREF15 use SeqGAN to generate poetry and comment on the performance of SeqGAN over MLE in human evaluations, encouraging our study of GANs for creative text generation. However, these studies do not focus solely on creative text.

#### Relevance 1570

Label: 

### BM25

None

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0171

Paper: UIT-ViIC: A Dataset for the First Evaluation on Vietnamese Image Captioning

> What are the other two Vietnamese datasets?

### Common Retrieved Chunks

#### Passage 1571

Retrieved by: BM25, Hybrid RRF

> information is mainly included in captions. The MS-COCO threshold for sentence’s length is 8, and we raise the number to 10 for our dataset. One reason for this change is that an object in image is usually expressed in many Vietnamese words. For example, a “baseball player” in English can be translated into “vận động viên bóng chày” or “cầu thủ bóng chày”, which already accounted for a significant length of the Vietnamese sentence. In addition, captions must be single sentences with continuous tense as we expect our model’s output to capture what we are seeing in the image in a consise way.
> 
> On the other hand, proper name for places, streets, etc must not be mentioned in this dataset in order to avoid confusions and incorrect identification names with the same scenery for output. Besides, annotators’ personal opinion must be excluded for more meaningful captions. Vietnamese words for several English ones such as tennis, pizza, TV, etc are not existed, so annotators could use such familiar words in describing captions. For some images, the subjects are ambiguous and not descriptive which would be difficult for annotators to describe in words. That’s the reason why annotators can describe images from more than one perspective.

#### Relevance 1571

Label: 

#### Passage 1572

Retrieved by: BM25, Dense, Hybrid RRF

> In this paper, we constructed a Vietnamese dataset with images from MS-COCO, relating to the category within sportball, consisting of 3,850 images with 19,250 manually-written Vietnamese captions. Next, we conducted several experiments on two popular existed Image Captioning models to evaluate their efficiency when learning two Vietnamese datasets. The results are then compared with the original MS-COCO English categorized with sportball category.
> 
> Overall, we can see that English set only out-performed Vietnamese ones in BLEU-1 metric, rather, the Vietnamese sets performing well basing on BLEU-2 to BLEU-4, especially CIDEr scores. On the other hand, when UIT-ViIC is compared with the dataset having captions translated by Google, the evaluation results and the output examples suggest that Google Translation service is able to perform acceptablly even though most translated captions are not perfectly natural and linguistically friendly. As a results, we proved that manually written captions for Vietnamese dataset is currently prefered.
> 
> For future improvements, extending the UIT-ViIC's cateogry into all types of sport to verify how the dataset's size and category affect the Image Captioning models' performance is considered as our highest priority. Moreover, the human resources for dataset construction will be expanded. Second, we will continue to finetune our experiments to find out proper parameters for models, especially with encoding and decoding architectures, for better learning performance with Vietnamese dataset, especially when the categories are limited.

#### Relevance 1572

Label: 

#### Passage 1574

Retrieved by: BM25, Dense, Hybrid RRF

> We conduct our experiments and do comparisons through three datasets with the same size and images of sportball category: Two Vietnamese datasets generated by two methods (translated by Google Translation service and annotated by human) and the original MS-COCO English dataset. The three sets are distributed into three subsets: 2,695 images for the training set, 924 images for validation set and 231 images for test set.

#### Relevance 1574

Label: 

#### Passage 1575

Retrieved by: BM25, Dense, Hybrid RRF

> We summarize in Table TABREF8 an incomplete list of published Image Captioning datasets, in English and in other languages. Several image caption datasets for English have been constructed, the representative examples are Flickr3k BIBREF5, BIBREF6; Flickr 30k BIBREF7 – an extending of Flickr3k and Microsoft COCO (Microsoft Common in Objects in Context) BIBREF8.
> 
> Besides, several image datasets with non-English captions have been developed. Depending on their applications, the target languages of these datasets vary, including German and French for image retrieval, Japanese for cross-lingual document retrieval BIBREF9 and image captioning BIBREF10, BIBREF3, Chinese for image tagging, captioning and retrieval BIBREF4. Each of these datasets is built on top of an existing English dataset, with MS-COCO as the most popular choice.
> 
> Our dataset UIT-ViIC is constructed using images from Microsoft COCO (MS-COCO). MS-COCO dataset includes more than 150,000 images, divided into three distributions: train, vailidate, test. For each image, five captions are provided independently by Amazon’s Mechanical Turk. MS-COCO is the most popular dataset for Image Captioning thanks to the MS-COCO challenge (2015) and it has a powerful evaluation server for candidates.
> 
> Regarding to the Vietnamese language processing, there are quite a number of research works on other tasks such as parsing, part-of-speech, named entity recognition, sentiment analysis, question answering. However, to the extent of our knowledge, there are no research publications on image captioning for Vietnamese. Therefore, we decide to build a new corpus of Vietnamese image captioning for Image Captioning research community and evaluate the state-of-the-art models on our corpus. In particular, we validate and compare the results by BLEU BIBREF11, ROUGE BIBREF12 and CIDEr BIBREF13 metrics between Neural Image Captioning (NIC) model BIBREF14, Image Captioning model from the Pytorch-tutorial BIBREF15 by Yunjey on our corpus as the pioneering results.

#### Relevance 1575

Label: 

#### Passage 1576

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> This section demonstrates how we constructed our new Vietnamese dataset. The dataset consists of 3,850 images relating to sports played with balls from 2017 edition of Microsoft COCO. Similar to most Image Captioning datasets, we provide five Vietnamese captions for each image, summing up to 19,250 captions in total.

#### Relevance 1576

Label: 

#### Passage 1577

Retrieved by: Dense, Hybrid RRF

> After finishing constructing UIT-ViIC dataset, we have a look in statistical analysis on our corpus in this section. UIT-ViIC covers 3,850 images described by 19,250 Vietnamese captions. Sticking strictly to our annotation guidelines, the majority of our captions are at the length of 10-15 tokens. We are using the term “tokens” here as a Vietnamese word can consist of one, two or even three tokens. Therefore, to apply Vietnamese properly to Image Captioning, we present a tokenization tool - PyVI BIBREF17, which is specialized for Vietnamese language tokenization, at words level. The sentence length using token-level tokenizer and word-level tokenizer are compared and illustrated in Fig. FIGREF23, we can see there are variances there. So that, we can suggest that the tokenizer performs well enough, and we can expect our Image Captioning models to perform better with Vietnamese sentences that are tokenized, as most models perform more efficiently with captions having fewer words.
> 
> Table TABREF24 summarizes top three most occuring words for each part-of-speech. Our dataset vocabulary size is 1,472 word classes, including 723 nouns, 567 verbs, and 182 adjectives. It is no surprise that as our dataset is about sports with balls, the noun “bóng” (meaning “ball") occurs most, followed by “sân” and "cầu thủ" (“pitch” and “athlete” respectively). We also found that the frequency of word “tennis” stands out among other adjectives, which specifies that the set covers the majority of tennis sport, followed by “bóng chày” (meaning “baseball”). Therefore, we expect our model to generate the best results for tennis images.

#### Relevance 1577

Label: 

### BM25

#### Passage 1573

Retrieved by: BM25

> The two following tables, Table TABREF36 and Table TABREF36, summarize experimental results of Pytorch-tutorial, NIC - Show and Tell models. The two models are trained with three mentioned datasets, which are English-sportball, GT-sportball, UIT-ViIC. After training, 924 images from validation subset for each dataset are used to validate the our models.
> 
> As can be seen in Table TABREF36, with model from Pytorch tutorial, MS-COCO English captions categorized with sportball yields better results than the two Vietnamese datasets. However, as number of consecutive words considered (BLEU gram) increase, UIT-ViIC’s BLEU scores start to pass that of English sportball and their gaps keep growing. The ROUGE-L and CIDEr-D scores for UIT-ViIC model prove the same thing, and interestingly, we can observe that the CIDEr-D score for the UIT-ViIC model surpasses English-sportball counterpart.
> 
> The same conclusion can be said from Table TABREF36. Show and Tell model’s results show that MS-COCO sportball English captions only gives better result at BLEU-1. From BLEU-3 to BLEU-4, both GT-sportball and UIT-ViIC yield superior scores to English-sportball. Besides, when limiting MS-COCO English dataset to sportball category only, the results are higher (0.689, 0.501, 0.355, 0.252) than when the model is trained on MS-COCO with all images, which scored only 0.629, 0.436, 0.290, 0.193 (results without tuning in 2018) from BLEU-1 to BLEU-4 respectively.
> 
> When we compare between two Vietnamese datasets, UIT-ViIC models perform better than sportball dataset translated automatically, GT-sportball. The gaps between the two results sets are more trivial in NIC model, and the numbers get smaller as the BLEU’s n-gram increase.
> 
> In Fig. FIGREF37, two images inputted into the models generate two Vietnamese captions that are able to describe accurately the sport game, which is soccer. The two models can also differentiate if there is more than one person in the images. However, when comparing GT-sportball outputs with UIT-ViIC ones in both images, UIT-ViIC yield captions that sound more naturally, considering Vietnamese language. Furthermore, UIT-ViIC demonstrates the specific action of the sport more accurately than GT-sportball. For example, in the below image of Fig. FIGREF37, UIT-ViIC tells the exact action (the man is preparing to throw the ball), whereas GT-sportball is mistaken (the man swing the bat). The confusion of GT-sportball

#### Relevance 1573

Label: 

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1578

Retrieved by: Hybrid RRF followed by BGE reranking

> Generating descriptions for multimedia contents such as images and videos, so called Image Captioning, is helpful for e-commerce companies or news agencies. For instance, in e-commerce field, people will no longer need to put much effort into understanding and describing products' images on their websites because image contents can be recognized and descriptions are automatically generated. Inspired by Horus BIBREF0 , Image Captioning system can also be integrated into a wearable device, which is able to capture surrounding images and generate descriptions as sound in real time to guide people with visually impaired.
> 
> Image Captioning has attracted attentions from researchers in recent years BIBREF1, BIBREF2, BIBREF3, and there has been promising attempts dealing with language barrier in this task by extending existed dataset captions into different languages BIBREF3, BIBREF4.
> 
> In this study, generating image captions in Vietnamese language is put into consideration. One straightforward approach for this task is to translate English captions into Vietnamese by human or by using machine translation tool, Google translation. With the method of translating directly from English to Vietnamese, we found that the descriptions are sometimes confusing and unnatural to native people. Moreover, image understandings are cultural dependent, as in Western, people usually have different ways to grasp images and different vocabulary choices for describing contexts. For instance, in Fig. FIGREF2, one MS-COCO English caption introduce about "a baseball player in motion of pitching", which makes sense and capture accurately the main activity in the image. Though it sounds sensible in English, the sentence becomes less meaningful when we try to translate it into Vietnamese. One attempt of translating the sentence is performed by Google Translation, and the result is not as expected.
> 
> Therefore, we come up with the approach of constructing a Vietnamese Image Captioning dataset with descriptions written manually by human. Composed by Vietnamese people, the sentences would be more natural and friendlier to Vietnamese users. The main resources we used from MS-COCO for our dataset are images. Besides, we consider having our dataset focus on sportball category due to several reasons:
> 
> By concentrating on a specific domain we are more likely to improve performance of the Image Captioning models. We expect our dataset can be used

#### Relevance 1578

Label: 

#### Passage 1579

Retrieved by: Hybrid RRF followed by BGE reranking

> We do comparisons with three sportball datasets, as follows:
> 
> Original English (English-sportball): The original MS-COCO English dataset with 3,850 sportball images. This dataset is first evaluated in order to have base results for following comparisons.
> 
> Google-translated Vietnamese (GT-sportball): The translated MS-COCO English dataset into Vietnamese using Google Translation API, categorized into sportball.
> 
> Manually-annotated Vietnamese (UIT-ViIC): The Vietnamese dataset built with manually written captions for images from MS-COCO, categorized into sportball.

#### Relevance 1579

Label: 

#### Passage 1580

Retrieved by: Hybrid RRF followed by BGE reranking

> images. Besides, we consider having our dataset focus on sportball category due to several reasons:
> 
> By concentrating on a specific domain we are more likely to improve performance of the Image Captioning models. We expect our dataset can be used to confirm or reject this hypothesis.
> 
> Sportball Image Captioning can be used in certain sport applications, such as supportting journalists describing great amount of images for their articles.
> 
> Our primary contributions of this paper are as follows:
> 
> Firstly, we introduce UIT-ViIC, the first Vietnamese dataset extending MS-COCO with manually written captions for Image Captioning. UIT-ViIC is published for research purposes.
> 
> Secondly, we introduce our annotation tool for dataset construction, which is also published to help annotators conveniently create captions.
> 
> Finally, we conduct experiments to evaluate state-of-the-art models (evaluated on English dataset) on UIT-ViIC dataset, then we analyze the performance results to have insights into our corpus.
> 
> The structure of the paper is organized as follows. Related documents and studies are presented in Section SECREF2. UIT-ViIC dataset creation is described in Section SECREF3. Section SECREF4 describes the methods we implement. The experimental results and analysis are presented in Section SECREF5. Conclusion and future work are deduced in Section SECREF6.

#### Relevance 1580

Label: 

#### Passage 1581

Retrieved by: Hybrid RRF followed by BGE reranking

> In this section, we describes procedures of building our sportball Vietnamese dataset, called UIT-ViIC.
> 
> Our human resources for dataset construction involve five writers, whose ages are from 22-25. Being native Vietnamese residents, they are fluent in Vietnamese. All five UIT-ViIC creators first research and are trained about sports knowledge as well as the specialized vocabulary before starting to work.
> 
> During annotation process, there are inconsistencies and disagreements between human's understandings and the way they see images. According to Micah Hodosh et al BIBREF5, most images’ captions on Internet nowadays tend to introduce information that cannot be obtained from the image itself, such as people name, location name, time, etc. Therefore, to successfully compose meaningful descriptive captions we expect, their should be strict guidelines.
> 
> Inspired from MS-COCO annotation rules BIBREF16, we first sketched UIT-ViIC's guidelines for our captions:
> 
> Each caption must contain at least ten Vietnamese words.
> 
> Only describe visible activities and objects included in image.
> 
> Exclude name of places, streets (Chinatown, New York, etc.) and number (apartment numbers, specific time on TV, etc.)
> 
> Familiar English words such as laptop, TV, tennis, etc. are allowed.
> 
> Each caption must be a single sentence with continuous tense.
> 
> Personal opinion and emotion must be excluded while annotating.
> 
> Annotators can describe the activities and objects from different perspectives.
> 
> Visible “thing” objects are the only one to be described.
> 
> Ambiguous “stuff” objects which do not have obvious “border” are ignored.
> 
> In case of 10 to 15 objects which are in the same category or species, annotators do not need to include them in the caption.
> 
> In comparison with MS-COCO BIBREF16 data collection guidelines in terms of annotation, UIT-ViIC’s guidelines has similar rules (1, 2, 8, 9, 10) . We extend from MS-COCO’s guidelines with five new rules to our own and have modifications in the original ones.
> 
> In both datasets, we would like to control sentence length and focus on describing important subjects only in order to make sure that essential information is mainly included in captions. The MS-COCO threshold for sentence’s length is 8, and we raise the number to 10 for our dataset. One reason for this change is that an object in image is usually expressed in many

#### Relevance 1581

Label: 

## Question 0172

Paper: Assessing BERT's Syntactic Abilities

> Were any of these tasks evaluated in any previous work?

### Common Retrieved Chunks

#### Passage 1582

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The recently introduced BERT model BIBREF0 exhibits strong performance on several language understanding benchmarks. To what extent does it capture syntax-sensitive structures?
> 
> Recent work examines the extent to which RNN-based models capture syntax-sensitive phenomena that are traditionally taken as evidence for the existence in hierarchical structure. In particular, in BIBREF1 we assess the ability of LSTMs to learn subject-verb agreement patterns in English, and evaluate on naturally occurring wikipedia sentences. BIBREF2 also consider subject-verb agreement, but in a “colorless green ideas” setting in which content words in naturally occurring sentences are replaced with random words with the same part-of-speech and inflection, thus ensuring a focus on syntax rather than on selectional-preferences based cues. BIBREF3 consider a wider range of syntactic phenomena (subject-verb agreement, reflexive anaphora, negative polarity items) using manually constructed stimuli, allowing for greater coverage and control than in the naturally occurring setting.
> 
> The BERT model is based on the “Transformer” architecture BIBREF4 , which—in contrast to RNNs—relies purely on attention mechanisms, and does not have an explicit notion of word order beyond marking each word with its absolute-position embedding. This reliance on attention may lead one to expect decreased performance on syntax-sensitive tasks compared to RNN (LSTM) models that do model word order directly, and explicitly track states across the sentence. Indeed, BIBREF5 finds that transformer-based models perform worse than LSTM models on the BIBREF1 agreement prediction dataset. In contrast, BIBREF6 find that self-attention performs on par with LSTM for syntax sensitive dependencies in the context of machine-translation, and performance on syntactic tasks is correlated with the number of attention heads in multi-head attention.
> 
> I adapt the evaluation protocol and stimuli of BIBREF1 , BIBREF2 and BIBREF3 to the bidirectional setting required by BERT, and evaluate the pre-trained BERT models (both the Large and the Base models). Surprisingly (at least to me), the out-of-the-box models (without any task-specific fine-tuning) perform very well on all the syntactic tasks.

#### Relevance 1582

Label: 

#### Passage 1583

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Tables 1 , 2 and 3 show the results. All cases exhibit high scores—in the vast majority of the cases substantially higher than reported in previous work. As discussed above, the results are not directly comparable to previous work: the BERT models are trained on different (and larger) data, are allowed to access the suffix of the sentence in addition to its prefix, and are evaluated on somewhat different data due to discarding OOV items. Still, taken together, the high performance numbers indicate that the purely attention-based BERT models are likely capable of capturing the same kind of syntactic regularities that LSTM-based models are capable of capturing, at least as well as the LSTM models and probably better.
> 
> Another noticeable and interesting trend is that larger is not necessarily better: the BERT-Base model outperforms the BERT-Large model on many of the syntactic conditions.

#### Relevance 1583

Label: 

#### Passage 1584

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> construction, in which strong agreement hints can be found also on the object following the verb. This is not an issue in the manually constructed BIBREF3 stimuli due to the patterns they chose.
> 
> Finally, I discard stimuli in which the focus verb or its plural/singular inflection does not appear as a single word in the BERT word-piece-based vocabulary (and hence cannot be predicted by the model). This include discarding BIBREF3 stimuli involving the words swims or admires, resulting in 23,368 discarded pairs (out of 152,300). I similarly discard 680 sentences from BIBREF1 where the focus verb or its inflection were one of 108 out-of-vocabulary tokens, and 28 sentence-pairs (8 tokens) from BIBREF2 .
> 
> The BERT results are not directly comparable to the numbers reported in previous work. Beyond the differences due to bidirectionality and the discarded stimuli, the BERT models are also trained on a different and larger corpus (covering both wikipedia and books).
> 
> Code is available at https://github.com/yoavg/bert-syntax.

#### Relevance 1584

Label: 

#### Passage 1585

Retrieved by: BM25, Dense, Hybrid RRF

> In contrast to these works, the BERT model is bi-directional: it is trained to predict the identity of masked words based on both the prefix and suffix surrounding these words. I adapt the uni-directional setup by feeding into BERT the complete sentence, while masking out the single focus verb. I then ask BERT for its word predictions for the masked position, and compare the score assigned to the original correct verb to the score assigned to the incorrect one.
> 
> For example, for the sentence:
> 
> a 2002 systemic review of herbal products found that several herbs , including peppermint and caraway , have anti-dyspeptic effects for non-ulcer dyspepsia with “ encouraging safety profiles ” . (from BIBREF1 )
> 
> I feed into BERT:
> 
> [CLS] a 2002 systemic review of herbal products found that several herbs , including peppermint and caraway , [MASK] anti-dyspeptic effects for non-ulcer dyspepsia with “ encouraging safety profiles ” . and look for the score assigned to the words have and has at the masked position.
> 
> Similarly, for the pair
> 
> the game that the guard hates is bad .
> 
> the game that the guard hates are bad .
> 
> (from BIBREF3 ), I feed into BERT:
> 
> [CLS] the game that the guard hates [MASK] bad .
> 
> and compare the scores predicted for is and are.
> 
> This differs from BIBREF1 and BIBREF2 by considering the entire sentence (excluding the verb) and not just its prefix leading to the verb, and differs from BIBREF3 by conditioning the focus verb on bidirectional context.
> 
> I use the PyTorch implementation of BERT, with the pre-trained models supplied by Google. I experiment with the bert-large-uncased and bert-base-uncased models.
> 
> The bi-directional setup precludes using using the NPI stimuli of BIBREF3 , in which the minimal pair differs in two words position, which I discard from the evaluation. I also discard the agreement cases involving the verbs is or are in BIBREF1 and in BIBREF2 , because some of them are copular construction, in which strong agreement hints can be found also on the object following the verb. This is not an issue in the manually constructed BIBREF3 stimuli due to the patterns they chose.
> 
> Finally, I discard stimuli in which the

#### Relevance 1585

Label: 

#### Passage 1587

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> All three previous work use uni-directional language-model-like models.
> 
> BIBREF1 start with existing sentences from wikipedia that contain a present-tense verb. They feed each sentence word by word into an LSTM, stop right before the focus verb, and ask the model to predict a binary plural/singular decision (supervised setup) or compare the probability assigned by a pre-trained language model (LM) to the plural vs singular forms of the verb (LM setup). The evaluation is then performed on sentences with “agreement attractors” in which at there is at least one noun between the verb and its subject, and all of the nouns between the verb and subject are of the opposite number from the subject.
> 
> BIBREF2 also start with existing sentences. However, in order to control for the possibillity of the model learning to rely on “semantic” selectional-preferences cues rather than syntactic ones, they replace each content word with random words from the same part-of-speech and inflection. This results in “coloreless green ideas” nonce sentences. The evaluation is then performed similarly to the LM setup of BIBREF1 : the sentence is fed into a pre-traiend LSTM LM up to the focus verb, and the model is considered correct if the probability assigned to the correct inflection of the original verb form given the prefix is larger than that assigned to the incorrect inflection.
> 
> BIBREF3 focus on manually constructed and controlled stimuli, that also emphasizes linguistic structure over selectional preferences. They construct minimal pairs of grammatical and ungrammatical sentences, feed each one in its entirety into a pre-trained LSTM-LM, and compare the perplexity assigned by the model to the grammatical and ungrammatical sentences. The model is “correct” if it assigns the grammatical sentence a higher probability than to the ungrammatical one. Since the minimal pairs for most phenomena differ only in a single word (the focus verb), this scoring is very similar to the one used in the two previous works. However, it does consider the continuation of the sentence after the focus verb, and also allows for assessing phenomena that require change into two or more words (like negative polarity items).

#### Relevance 1587

Label: 

#### Passage 1588

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> I use the stimuli provided by BIBREF1 , BIBREF2 , BIBREF3 , but change the experimental protocol to adapt it to the bidirectional nature of the BERT model. This requires discarding some of the stimuli, as described below. Thus, the numbers are not strictly comparable to those reported in previous work.

#### Relevance 1588

Label: 

### BM25

#### Passage 1586

Retrieved by: BM25

> The BERT models perform remarkably well on all the syntactic test cases. I expected the attention-based mechanism to fail on these (compared to the LSTM-based models), and am surprised by these results. The BIBREF2 and BIBREF3 conditions rule out the possibility of overly relying on selectional preference cues or memorizing the wikipedia training data, and suggest real syntactic generalization is taking place. Exploring the extent to which deep purely-attention-based architectures such as BERT are capable of capturing hierarchy-sensitive and syntactic dependencies—as well as the mechanisms by which this is achieved—is a fascinating area for future research.

#### Relevance 1586

Label: 

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0173

Paper: Reducing Gender Bias in Neural Machine Translation as a Domain Adaptation Problem

> What metrics are used to measure bias reduction?

### Common Retrieved Chunks

#### Passage 1589

Retrieved by: BM25, Dense, Hybrid RRF

> translation, are as undesirable as large positive values.
> 
> We note that $\Delta S$ can be significantly skewed by very biased systems. A model that generates male forms for almost all test sentences, stereotypical roles or not, will have an extremely low $\Delta S$, since its pro- and anti-stereotypical class accuracy will both be about 50%. Consequently we also report:
> 
> M:F – ratio of hypotheses with male predictions to those with female predictions.
> 
> Ideally this should be close to 1.0, since the WinoMT challenge set is gender-balanced. While M:F correlates strongly with $\Delta G$, we consider M:F easier to interpret, particularly since very high or low M:F reduce the relevance of $\Delta S$.
> 
> Finally, we wish to reduce gender bias without reducing translation performance. We report BLEU BIBREF22 on separate, general test sets for each language pair. WinoMT is designed to work without target language references, and so it is not possible to measure translation performance on this set by measures such as BLEU.

#### Relevance 1589

Label: 

#### Passage 1590

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> As language processing tools become more prevalent concern has grown over their susceptibility to social biases and their potential to propagate bias BIBREF1, BIBREF2. Natural language training data inevitably reflects biases present in our society. For example, gender bias manifests itself in training data which features more examples of men than of women. Tools trained on such data will then exhibit or even amplify the biases BIBREF3.
> 
> Gender bias is a particularly important problem for Neural Machine Translation (NMT) into gender-inflected languages. An over-prevalence of some gendered forms in the training data leads to translations with identifiable errors BIBREF0. Translations are better for sentences involving men and for sentences containing stereotypical gender roles. For example, mentions of male doctors are more reliably translated than those of male nurses BIBREF2, BIBREF4.
> 
> Recent approaches to the bias problem in NLP have involved training from scratch on artificially gender-balanced versions of the original dataset BIBREF5, BIBREF6 or with de-biased embeddings BIBREF7, BIBREF8. While these approaches may be effective, training from scratch is inefficient and gender-balancing embeddings or large parallel datasets are challenging problems BIBREF9.
> 
> Instead we propose treating gender debiasing as a domain adaptation problem, since NMT models can very quickly adapt to a new domain BIBREF10. To the best of our knowledge this work is the first to attempt NMT bias reduction by fine-tuning, rather than retraining. We consider three aspects of this adaptation problem: creating less biased adaptation data, parameter adaptation using this data, and inference with the debiased models produced by adaptation.
> 
> Regarding data, we suggest that a small, trusted gender-balanced set could allow more efficient and effective gender debiasing than a larger, noisier set. To explore this we create a tiny, handcrafted profession-based dataset for transfer learning. For contrast, we also consider fine-tuning on a counterfactual subset of the full dataset and propose a straightforward scheme for artificially gender-balancing parallel text for NMT.
> 
> We find that during domain adaptation improvement on the gender-debiased domain comes at the expense of translation quality due to catastrophic forgetting BIBREF11. We can balance improvement and forgetting with a regularised training procedure, Elastic Weight Consolidation (EWC), or in inference by a two-step lattice rescoring procedure.
> 
> We experiment with three

#### Relevance 1590

Label: 

#### Passage 1591

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> WinoMT BIBREF0 is a recently proposed challenge set for gender bias in NMT. Moreover it is the only significant challenge set we are aware of to evaluate translation gender bias comparably across several language pairs. It permits automatic bias evaluation for translation from English to eight target languages with grammatical gender. The source side of WinoMT is 3888 concatenated sentences from Winogender BIBREF19 and WinoBias BIBREF5. These are coreference resolution datasets in which each sentence contains a primary entity which is co-referent with a pronoun – the doctor in the first example above and the developer in the second – and a secondary entity – the nurse and the cleaner respectively.
> 
> WinoMT evaluation extracts the grammatical gender of the primary entity from each translation hypothesis by automatic word alignment followed by morphological analysis. WinoMT then compares the translated primary entity with the gold gender, with the objective being a correctly gendered translation. The authors emphasise the following metrics over the challenge set:
> 
> Accuracy – percentage of hypotheses with the correctly gendered primary entity.
> 
> $\mathbf {\Delta G}$ – difference in $F_1$ score between the set of sentences with masculine entities and the set with feminine entities.
> 
> $\mathbf {\Delta S}$ – difference in accuracy between the set of sentences with pro-stereotypical (`pro') entities and those with anti-stereotypical (`anti') entities, as determined by BIBREF5 using US labour statistics. For example, the `pro' set contains male doctors and female nurses, while `anti' contains female doctors and male nurses.
> 
> Our main objective is increasing accuracy. We also report on $\Delta G$ and $\Delta S$ for ease of comparison to previous work. Ideally the absolute values of $\Delta G$ and $\Delta S$ should be close to 0. A high positive $\Delta G$ indicates that a model translates male entities better, while a high positive $\Delta S$ indicates that a model stereotypes male and female entities. Large negative values for $\Delta G$ and $\Delta S$, indicating a bias towards female or anti-stereotypical translation, are as undesirable as large positive values.
> 
> We note that $\Delta S$ can be significantly skewed by very biased systems. A model that generates male forms for almost all test sentences, stereotypical roles or not, will have an extremely

#### Relevance 1591

Label: 

#### Passage 1592

Retrieved by: BM25, Dense, Hybrid RRF

> Finally, in Table TABREF41, we apply the gender inflection transducer to the commercial system translations listed in Table TABREF36. We find rescoring these lattices with our strongest debiasing model (line 5 of Table TABREF40) substantially improves WinoMT accuracy for all systems and language pairs.
> 
> One interesting observation is that WinoMT accuracy after rescoring tends to fall in a fairly narrow range for each language relative to the performance range of the baseline systems. For example, a 25.5% range in baseline en-de accuracy becomes a 3.6% range after rescoring. This suggests that our rescoring approach is not limited as much by the bias level of the baseline system as by the gender-inflection transducer and the models used in rescoring. Indeed, we emphasise that the large improvements reported in Table TABREF41 do not require any knowledge of the commercial systems or the data they were trained on; we use only the translation hypotheses they produce and our own rescoring model and transducer.

#### Relevance 1592

Label: 

#### Passage 1594

Retrieved by: Dense, Hybrid RRF

> comes at the expense of translation quality due to catastrophic forgetting BIBREF11. We can balance improvement and forgetting with a regularised training procedure, Elastic Weight Consolidation (EWC), or in inference by a two-step lattice rescoring procedure.
> 
> We experiment with three language pairs, assessing the impact of debiasing on general domain BLEU and on the WinoMT challenge set BIBREF0. We find that continued training on the handcrafted set gives far stronger and more consistent improvements in gender-debiasing with orders of magnitude less training time, although as expected general translation performance as measured by BLEU decreases.
> 
> We further show that regularised adaptation with EWC can reduce bias while limiting degradation in general translation quality. We also present a lattice rescoring procedure in which initial hypotheses produced by the biased baseline system are transduced to create gender-inflected search spaces which can be rescored by the adapted model. We believe this approach, rescoring with models targeted to remove bias, is novel in NMT. The rescoring procedure improves WinoMT accuracy by up to 30% with no decrease in BLEU on the general test set.
> 
> Recent recommendations for ethics in Artificial Intelligence have suggested that social biases or imbalances in a dataset be addressed prior to model training BIBREF12. This recommendation presupposes that the source of bias in a dataset is both obvious and easily adjusted. We show that debiasing a full NMT dataset is difficult, and suggest alternative efficient and effective approaches for debiasing a model after it is trained. This avoids the need to identify and remove all possible biases prior to training, and has the added benefit of preserving privacy, since no access to the original data or knowledge of its contents is required. As evidence, in section SECREF43, we show this scheme can be applied to remove gender bias in the output of ‘black box‘ online commercial MT systems.

#### Relevance 1594

Label: 

#### Passage 1595

Retrieved by: Dense, Hybrid RRF

> In Table TABREF36 we compare our three baselines to commercial systems on WinoMT, using results quoted directly from BIBREF0. Our baselines achieve comparable accuracy, masculine/feminine bias score $\Delta G$ and pro/anti stereotypical bias score $\Delta S$ to four commercial translation systems, outscoring at least one system for each metric on each language pair.
> 
> The $\Delta S$ for our en-es baseline is surprisingly small. Investigation shows this model predicts male and female entities in a ratio of over 6:1. Since almost all entities are translated as male, pro- and anti-stereotypical class accuracy are both about 50%, making $\Delta S$ very small. This highlights the importance of considering $\Delta S$ in the context of $\Delta G$ and M:F prediction ratio.

#### Relevance 1595

Label: 

### BM25

#### Passage 1593

Retrieved by: BM25

> Results for fine-tuning on the handcrafted set are given in lines 3-6 of Table TABREF40. These experiments take place in minutes on a single GPU, compared to several hours when fine-tuning on the counterfactual sets and far longer if training from scratch.
> 
> Fine-tuning on the handcrafted sets gives a much faster BLEU drop than fine-tuning on counterfactual sets. This is unsurprising since the handcrafted sets are domains of new sentences with consistent sentence length and structure. By contrast the counterfactual sets are less repetitive and close to subsets of the original training data, slowing forgetting. We believe the degradation here is limited only by the ease of fitting the small handcrafted sets.
> 
> Line 4 of Table TABREF40 adapts to the handcrafted set, stopping when validation BLEU degrades by 5% on each language pair. This gives a WinoMT accuracy up to 19 points above the baseline, far more improvement than the best counterfactual result. Difference in gender score $\Delta G$ improves by at least a factor of 4. Stereotyping score $\Delta S$ also improves far more than for counterfactual fine-tuning. Unlike the Table TABREF37 results, the improvement is consistent across all WinoMT metrics and all language pairs.
> 
> The model adapted to no-overlap handcrafted data (line 3) gives a similar drop in BLEU to the model in line 4. This model also gives stronger and more consistent WinoMT improvements over the baseline compared to the balanced counterfactual set, despite the implausibly strict scenario of no English profession vocabulary in common with the challenge set. This demonstrates that the adapted model does not simply memorise vocabulary.
> 
> The drop in BLEU and improvement on WinoMT can be explored by varying the training procedure. The model of line 5 simply adapts to handcrafted data for more iterations with no regularisation, to approximate loss convergence on the handcrafted set. This leads to a severe drop in BLEU, but even higher WinoMT scores.
> 
> In line 6 we regularise adaptation with EWC. There is a trade-off between general translation performance and WinoMT accuracy. With EWC regularization tuned to balance validation BLEU and WinoMT accuracy, the decrease is limited to about 0.5 BLEU on each language pair. Adapting to convergence, as in line 5,

#### Relevance 1593

Label: 

### Dense

#### Passage 1596

Retrieved by: Dense

> Regularized training is a well-established approach for minimizing catastrophic forgetting during domain adaptation of machine translation BIBREF24. One effective form is Elastic Weight Consolidation (EWC) BIBREF25 which in NMT has been shown to maintain or even improve original domain performance BIBREF26, BIBREF27. In EWC a regularization term is added to the original loss function $L$ when training the debiased model (DB):
> 
> $\theta ^{B}_{j}$ are the converged parameters of the original biased model, and $\theta ^{DB}_j$ are the current debiased model parameters. $F_j=\mathbb {E} \big [ \nabla ^2 L(\theta ^{B}_j)\big ] $, a Fisher information estimate over samples from the biased data under the biased model. We apply EWC when performance on the original validation set drops, selecting hyperparameter $\lambda $ via validation set BLEU.

#### Relevance 1596

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1597

Retrieved by: Hybrid RRF followed by BGE reranking

> For contrast, we fine-tune on an approximated counterfactual dataset. Counterfactual data augmentation is an intuitive solution to bias from data over-representation BIBREF23. It involves identifying the subset of sentences containing bias – in this case gendered terms – and, for each one, adding an equivalent sentence with the bias reversed – in this case a gender-swapped version.
> 
> While counterfactual data augmentation is relatively simple for sentences in English, the process for inflected languages is challenging, involving identifying and updating words that are co-referent with all gendered entities in a sentence. Gender-swapping MT training data additionally requires that the same entities are swapped in the corresponding parallel sentence. A robust scheme for gender-swapping multiple entities in inflected language sentences directly, together with corresponding parallel text, is beyond the scope of this paper. Instead we suggest a rough but straightforward approach for counterfactual data augmentation for NMT which to the best of our knowledge is the first application to parallel sentences.
> 
> We first perform simple gender-swapping on the subset of the English source sentences with gendered terms. We use the approach described in BIBREF5 which swaps a fixed list of gendered stopwords (e.g. man / woman, he / she).. We then greedily forward-translate the gender-swapped English sentences with a baseline NMT model trained on the the full source and target text, producing gender-swapped target language sentences.
> 
> This lets us compare four related sets for gender debiasing adaptation, as illustrated in Figure FIGREF11:
> 
> Original: a subset of parallel sentences from the original training data where the source sentence contains gendered stopwords.
> 
> Forward-translated (FTrans) original: the source side of the original set with forward-translated target sentences.
> 
> Forward-translated (FTrans) swapped: the original source sentences are gender-swapped, then forward-translated to produce gender-swapped target sentences.
> 
> Balanced: the concatenation of the original and FTrans swapped parallel datasets. This is twice the size of the other counterfactual sets.
> 
> Comparing performance in adaptation of FTrans swapped and FTrans original lets us distinguish between the effects of gender-swapping and of obtaining target sentences from forward-translation.

#### Relevance 1597

Label: 

#### Passage 1598

Retrieved by: Hybrid RRF followed by BGE reranking

> Our hypothesis is that the absence of gender bias can be treated as a small domain for the purposes of NMT model adaptation. In this case a well-formed small dataset may give better results than attempts at debiasing the entire original dataset.
> 
> We therefore construct a tiny, trivial set of gender-balanced English sentences which we can easily translate into each target language. The sentences follow the template:
> 
> The $[$PROFESSION$]$ finished $[$his$|$her$]$ work.
> 
> We refer to this as the handcrafted set. Each profession is from the list collected by BIBREF4 from US labour statistics. We simplify this list by removing field-specific adjectives. For example, we have a single profession `engineer', as opposed to specifying industrial engineer, locomotive engineer, etc. In total we select 194 professions, giving just 388 sentences in a gender-balanced set.
> 
> With manually translated masculine and feminine templates, we simply translate the masculine and feminine forms of each listed profession for each target language. In practice this translation is via an MT first-pass for speed, followed by manual checking, but given available lexicons this could be further automated. We note that the handcrafted sets contain no examples of coreference resolution and very little variety in terms of grammatical gender. A set of more complex sentences targeted at the coreference task might further improve WinoMT scores, but would be more difficult to produce for new languages.
> 
> We wish to distinguish between a model which improves gender translation, and one which improves its WinoMT scores simply by learning the vocabulary for previously unseen or uncommon professions. We therefore create a handcrafted no-overlap set, removing source sentences with professions occurring in WinoMT to leave 216 sentences. We increase this set back to 388 examples with balanced adjective-based sentences in the same pattern, e.g. The tall $[$man$|$woman$]$ finished $[$his$|$her$]$ work.

#### Relevance 1598

Label: 

#### Passage 1599

Retrieved by: Hybrid RRF followed by BGE reranking

> For all models we use a Transformer model BIBREF35 with the `base' parameter settings given in Tensor2Tensor BIBREF36. We train baselines to validation set BLEU convergence on one GPU, delaying gradient updates by factor 4 to simulate 4 GPUs BIBREF37. During fine-tuning training is continued without learning rate resetting. Normal and lattice-constrained decoding is via SGNMT with beam size 4. BLEU scores are calculated for cased, detokenized output using SacreBLEU BIBREF38

#### Relevance 1599

Label: 

## Question 0174

Paper: Evaluating the Cross-Lingual Effectiveness of Massively Multilingual Neural Machine Translation

> What are the five downstream tasks?

### Common Retrieved Chunks

#### Passage 1600

Retrieved by: BM25, Hybrid RRF

> More recent work has shown that CWRs obtained using unsupervised generative pre-training techniques such as language modeling or cloze task BIBREF26 have led to state-of-the-art results beyond what was achieved with traditional word type representations on many monolingual NLP tasks BIBREF27, BIBREF1, BIBREF28, BIBREF29 such as sentence classification, sequence tagging, and question answering. Subsequently, these contextual methods have been extended to produce multilingual representations by training a single model on text from multiple languages which have proven to be very effective for cross lingual transfer BIBREF18, BIBREF30, BIBREF31. BIBREF19 show that adding a translation language modeling (TLM) objective to mBERT's MLM objective utilizes both monolingual and parallel data to further improve the cross-lingual effectiveness.

#### Relevance 1600

Label: 

#### Passage 1601

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> In this section, we describe our massively multilingual NMT system. Similar to BERT, our transfer learning setup has two distinct steps: pre-training and fine-tuning. During pre-training, the NMT model is trained on large amounts of parallel data to perform translation. During fine-tuning, we initialize our downstream model with the pre-trained parameters from the encoder of the NMT system, and then all of the parameters are fine-tuned using labeled data from the downstream tasks.

#### Relevance 1601

Label: 

#### Passage 1602

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Fine-tuning involves taking the encoder of our mNMT model, named Massively Multilingual Translation Encoder (MMTE), and adapting it to the downstream task. For tasks which involve single input, the text is directly fed into the encoder. For tasks such as entailment which involve input pairs, we concatenate the two inputs using a separator token and pass this through the encoder. For each downstream task, the inputs and outputs are passed through the encoder and we fine-tune all the parameters end-to-end. The encoder encodes the input through the stack of Transformer layers and produces representations for each token at the output. For sequence tagging tasks, these token level representations are individually fed into a task-specific output layer. For classification or entailment tasks, we apply max-pooling on the token level representations and feed this into the task-specific output layer.
> 
> It should be noted that fine-tuning is relatively inexpensive and fast. All of the results can be obtained within a few thousand gradient steps. The individual task-specific modeling details are described in detail in section SECREF3. It is also important to note that while the encoder, the attention mechanism, and the decoder of the model are trained in the pre-training phase, only the encoder is used during fine-tuning.

#### Relevance 1602

Label: 

#### Passage 1603

Retrieved by: BM25, Hybrid RRF

> In this setting, instead of fine-tuning the entire network of mBERT or MMTE, we only fine-tune the task-specific network which only has a small percentage of the total number of parameters. The rest of the model parameters are frozen. We perform this experiment on POS tagging task by fine-tuning a single layer feed-forward neural network stacked on top of mBERT and MMTE. We report the results in Table TABREF31. While the scores of the feature-based approach are significantly lower than those obtained via full fine-tuning (TABREF27), we see that MMTE still outperforms mBERT on both in-language and zero-shot settings by an even bigger margin. This is particularly interesting as the feature-based approach has its own advantages: 1) it is applicable to downstream tasks which require significant task-specific parameters on top of a transformer encoder, 2) it is computationally cheaper to train and tune the downstream model, and 3) it is compact and scalable since we only need a small number of task-specific parameters.

#### Relevance 1603

Label: 

#### Passage 1604

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this section we provide the list of languages codes used throughout this paper and the statistics of the datasets used for the downstream tasks.

#### Relevance 1604

Label: 

#### Passage 1605

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> As stated earlier, we use MMTE to perform downstream cross-lingual transfer on 5 NLP tasks. These include 3 classification tasks: NLI (XNLI dataset), document classification (MLDoc dataset) and intent classification, and 2 sequence tagging tasks: POS tagging and NER. We detail all of the experiments in this section.

#### Relevance 1605

Label: 

#### Passage 1607

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> English has an abundance of labeled data that can be used for various Natural Language Processing (NLP) tasks, such as part-of-speech tagging (POS), named entity recognition (NER), and natural language inference (NLI). This richness of labeled data manifests itself as a boost in accuracy in the current era of data-hungry deep learning algorithms. However, the same is not true for many other languages where task specific data is scarce and expensive to acquire. This motivates the need for cross-lingual transfer learning – the ability to leverage the knowledge from task specific data available in one or more languages to solve that task in languages with little or no task-specific data.
> 
> Recent progress in NMT has enabled one to train multilingual systems that support translation from multiple source languages into multiple target languages within a single model BIBREF2, BIBREF3, BIBREF0. Such multilingual NMT (mNMT) systems often demonstrate large improvements in translation quality on low resource languages. This positive transfer originates from the model's ability to learn representations which are transferable across languages. Previous work has shown that these representations can then be used for cross-lingual transfer in other downstream NLP tasks - albeit on only a pair of language pairs BIBREF4, or by limiting the decoder to use a pooled vector representation of the entire sentence from the encoder BIBREF5.
> 
> In this paper we scale up the number of translation directions used in the NMT model to include 102 languages to and from English. Unlike BIBREF5, we do not apply any restricting operations such as pooling while training mNMT which allows us to obtain token level representations making it possible to transfer them to sequence tagging tasks as well. We find that mNMT models trained using plain translation losses can out of the box emerge as competitive alternatives to other methods at the forefront of cross-lingual transfer learning BIBREF1, BIBREF5
> 
> Our contributions in this paper are threefold:
> 
> We use representations from a Massively Multilingual Translation Encoder (MMTE) that can handle 103 languages to achieve cross-lingual transfer on 5 classification and sequence tagging tasks spanning more than 50 languages.
> 
> We compare MMTE to mBERT in different cross-lingual transfer scenarios including zero-shot, few-shot, fine-tuning, and feature extraction scenarios.

#### Relevance 1607

Label: 

### BM25

None

### Dense

#### Passage 1606

Retrieved by: Dense

> BIBREF7 recently presented a dataset for multilingual task oriented dialog. This dataset contains 57k annotated utterances in English (43k), Spanish (8.6k), and Thai (5k) with 12 different intents across the domains weather, alarm, and reminder. The evaluation metric used is classification accuracy. We use this data for both in-language training and zero-shot transfer. The task-specific network and the optimizer used is the same as the one used for the above two tasks. The learning rate schedule is (0.1,100k). Results are reported in Table TABREF25. MMTE outperforms both mBERT and previous SOTA in both in-language and zero-shot setting on all 3 languages and establishes a new SOTA for this dataset.

#### Relevance 1606

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

None

## Question 0175

Paper: Improving Neural Text Simplification Model with Simplified Corpora

> what evaluation metrics did they use?

### Common Retrieved Chunks

#### Passage 1608

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We evaluate the performance of text simplification using neural machine translation on available parallel sentences and additional simplified sentences.
> 
> Dataset. We use two simplification datasets (WikiSmall and WikiLarge). WikiSmall consists of ordinary and simplified sentences from the ordinary and simple English Wikipedias, which has been used as benchmark for evaluating text simplification BIBREF17 , BIBREF18 , BIBREF8 . The training set has 89,042 sentence pairs, and the test set has 100 pairs. WikiLarge is also from Wikipedia corpus whose training set contains 296,402 sentence pairs BIBREF19 , BIBREF20 . WikiLarge includes 8 (reference) simplifications for 2,359 sentences split into 2,000 for development and 359 for testing.
> 
> Metrics. Three metrics in text simplification are chosen in this paper. BLEU BIBREF5 is one traditional machine translation metric to assess the degree to which translated simplifications differed from reference simplifications. FKGL measures the readability of the output BIBREF23 . A small FKGL represents simpler output. SARI is a recent text-simplification metric by comparing the output against the source and reference simplifications BIBREF20 .
> 
> We evaluate the output of all systems using human evaluation. The metric is denoted as Simplicity BIBREF8 . The three non-native fluent English speakers are shown reference sentences and output sentences. They are asked whether the output sentence is much simpler (+2), somewhat simpler (+1), equally (0), somewhat more difficult (-1), and much more difficult (-2) than the reference sentence.
> 
> Methods. We use OpenNMT BIBREF24 as the implementation of the NMT system for all experiments BIBREF5 . We generally follow the default settings and training procedure described by Klein et al.(2017). We replace out-of-vocabulary words with a special UNK symbol. At prediction time, we replace UNK words with the highest probability score from the attention layer. OpenNMT system used on parallel data is the baseline system. To obtain a synthetic parallel training set, we back-translate a random sample of 100K sentences from the collected simplified corpora. OpenNMT used on parallel data and synthetic data is our model. The benchmarks are run on a Intel(R) Core(TM) i7-5930K CPU@3.50GHz, 32GB Mem, trained on 1 GPU GeForce GTX 1080 (Pascal) with CUDA v. 8.0.
> 
> We choose three statistical text simplification systems. PBMT-R is a phrase-based method with a

#### Relevance 1608

Label: 

#### Passage 1609

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> adding simplified training data with synthetic ordinary sentences. Compared with statistical machine translation models (PBMT-R, Hybrid, SBMT-SARI), our method (NMT+synthetic) still have better results, but slightly worse FKGL and SARI. Similar to the results in WikiLarge, the results of our human evaluation using Simplicity outperforms the other models. In conclusion, Our method produces better results comparing with the baselines, which demonstrates the effectiveness of adding simplified training data.

#### Relevance 1609

Label: 

#### Passage 1610

Retrieved by: BM25, Hybrid RRF, Hybrid RRF followed by BGE reranking

> our model. The benchmarks are run on a Intel(R) Core(TM) i7-5930K CPU@3.50GHz, 32GB Mem, trained on 1 GPU GeForce GTX 1080 (Pascal) with CUDA v. 8.0.
> 
> We choose three statistical text simplification systems. PBMT-R is a phrase-based method with a reranking post-processing step BIBREF18 . Hybrid performs sentence splitting and deletion operations based on discourse representation structures, and then simplifies sentences with PBMT-R BIBREF25 . SBMT-SARI BIBREF19 is syntax-based translation model using PPDB paraphrase database BIBREF26 and modifies tuning function (using SARI). We choose two neural text simplification systems. NMT is a basic attention-based encoder-decoder model which uses OpenNMT framework to train with two LSTM layers, hidden states of size 500 and 500 hidden units, SGD optimizer, and a dropout rate of 0.3 BIBREF8 . Dress is an encoder-decoder model coupled with a deep reinforcement learning framework, and the parameters are chosen according to the original paper BIBREF20 . For the experiments with synthetic parallel data, we back-translate a random sample of 60 000 sentences from the collected simplified sentences into ordinary sentences. Our model is trained on synthetic data and the available parallel data, denoted as NMT+synthetic.
> 
> Results. Table 1 shows the results of all models on WikiLarge dataset. We can see that our method (NMT+synthetic) can obtain higher BLEU, lower FKGL and high SARI compared with other models, except Dress on FKGL and SBMT-SARI on SARI. It verified that including synthetic data during training is very effective, and yields an improvement over our baseline NMF by 2.11 BLEU, 1.7 FKGL and 1.07 SARI. We also substantially outperform Dress, who previously reported SOTA result. The results of our human evaluation using Simplicity are also presented in Table 1. NMT on synthetic data is significantly better than PBMT-R, Dress, and SBMT-SARI on Simplicity. It indicates that our method with simplified data is effective at creating simpler output.
> 
> Results on WikiSmall dataset are shown in Table 2. We see substantial improvements (6.37 BLEU) than NMT from adding simplified training data with synthetic ordinary sentences. Compared with statistical machine translation models (PBMT-R, Hybrid, SBMT-SARI), our method (NMT+synthetic) still have better results, but slightly worse FKGL and SARI. Similar to the results in WikiLarge, the results of our

#### Relevance 1610

Label: 

#### Passage 1612

Retrieved by: BM25, Hybrid RRF followed by BGE reranking

> for text simplification task, and achieved good results BIBREF8 , BIBREF4 , BIBREF20 . The main limitation of the aforementioned NMT models for text simplification depended on the parallel ordinary-simplified sentence pairs. Because ordinary-simplified sentence pairs are expensive and time-consuming to build, the available largest data is EW-SEW that only have 296,402 sentence pairs. The dataset is insufficiency for NMT model if we want to NMT model can obtain the best parameters. Considering simplified data plays an important role in boosting fluency for phrase-based text simplification, and we investigate the use of simplified data for text simplification. We are the first to show that we can effectively adapt neural translation models for text simplifiation with simplified corpora.

#### Relevance 1612

Label: 

#### Passage 1613

Retrieved by: Dense, Hybrid RRF

> We collected a simplified dataset from Simple English Wikipedia that are freely available, which has been previously used for many text simplification methods BIBREF0 , BIBREF10 , BIBREF3 . The simple English Wikipedia is pretty easy to understand than normal English Wikipedia. We downloaded all articles from Simple English Wikipedia. For these articles, we removed stubs, navigation pages and any article that consisted of a single sentence. We then split them into sentences with the Stanford CorNLP BIBREF21 , and deleted these sentences whose number of words are smaller than 10 or large than 40. After removing repeated sentences, we chose 600K sentences as the simplified data with 11.6M words, and the size of vocabulary is 82K.

#### Relevance 1613

Label: 

#### Passage 1614

Retrieved by: Dense, Hybrid RRF

> In this paper, we propose one simple method to use simplified corpora during training of NMT systems, with no changes to the network architecture. In the experiments on two datasets, we achieve substantial gains in all tasks, and new SOTA results, via back-translation of simplified sentences into the ordinary sentences, and treating this synthetic data as additional training data. Because we do not change the neural network architecture to integrate simplified corpora, our method can be easily applied to other Neural Text Simplification (NTS) systems. We expect that the effectiveness of our method not only varies with the quality of the NTS system used for back-translation, but also depends on the amount of available parallel and simplified corpora. In the paper, we have only utilized data from Wikipedia for simplified sentences. In the future, many other text sources are available and the impact of not only size, but also of domain should be investigated.

#### Relevance 1614

Label: 

### BM25

#### Passage 1611

Retrieved by: BM25

> We train an auxiliary system using NMT model from the simplified sentence to the ordinary sentence, which is first trained on the available parallel data. For leveraging simplified sentences to improve the quality of NMT model for text simplification, we propose to adapt the back-translation approach proposed by Sennrich et al. BIBREF11 to our scenario. More concretely, Given one sentence in simplified sentences, we use the simplified-ordinary system in translate mode with greedy decoding to translate it to the ordinary sentences, which is denoted as back-translation. This way, we obtain a synthetic parallel simplified-ordinary sentences. Both the synthetic sentences and the available parallel data are used as training data for the original NMT system.

#### Relevance 1611

Label: 

### Dense

#### Passage 1615

Retrieved by: Dense

> models can be typically improved when trained on more data. Therefore, we expect simplified corpora to be especially helpful for NMT models.
> 
> In contrast to previous work, which uses the existing NMT models, we explore strategy to include simplified training corpora in the training process without changing the neural network architecture. We first propose to pair simplified training sentences with synthetic ordinary sentences during training, and treat this synthetic data as additional training data. We obtain synthetic ordinary sentences through back-translation, i.e. an automatic translation of the simplified sentence into the ordinary sentence BIBREF11 . Then, we mix the synthetic data into the original (simplified-ordinary) data to train NMT model. Experimental results on two publicly available datasets show that we can improve the text simplification quality of NMT models by mixing simplified sentences into the training set over NMT model only using the original training data.

#### Relevance 1615

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1616

Retrieved by: Hybrid RRF followed by BGE reranking

> Text simplification aims to reduce the lexical and structural complexity of a text, while still retaining the semantic meaning, which can help children, non-native speakers, and people with cognitive disabilities, to understand text better. One of the methods of automatic text simplification can be generally divided into three categories: lexical simplification (LS) BIBREF0 , BIBREF1 , rule-based BIBREF2 , and machine translation (MT) BIBREF3 , BIBREF4 . LS is mainly used to simplify text by substituting infrequent and difficult words with frequent and easier words. However, there are several challenges for the LS approach: a great number of transformation rules are required for reasonable coverage and should be applied based on the specific context; third, the syntax and semantic meaning of the sentence is hard to retain. Rule-based approaches use hand-crafted rules for lexical and syntactic simplification, for example, substituting difficult words in a predefined vocabulary. However, such approaches need a lot of human-involvement to manually define these rules, and it is impossible to give all possible simplification rules. MT-based approach has attracted great attention in the last several years, which addresses text simplification as a monolingual machine translation problem translating from 'ordinary' and 'simplified' sentences.
> 
> In recent years, neural Machine Translation (NMT) is a newly-proposed deep learning approach and achieves very impressive results BIBREF5 , BIBREF6 , BIBREF7 . Unlike the traditional phrased-based machine translation system which operates on small components separately, NMT system is being trained end-to-end, without the need to have external decoders, language models or phrase tables. Therefore, the existing architectures in NMT are used for text simplification BIBREF8 , BIBREF4 . However, most recent work using NMT is limited to the training data that are scarce and expensive to build. Language models trained on simplified corpora have played a central role in statistical text simplification BIBREF9 , BIBREF10 . One main reason is the amount of available simplified corpora typically far exceeds the amount of parallel data. The performance of models can be typically improved when trained on more data. Therefore, we expect simplified corpora to be especially helpful for NMT models.
> 
> In contrast to previous work, which uses the existing NMT models, we explore strategy to include simplified training

#### Relevance 1616

Label: 

## Question 0176

Paper: Transcribing Lyrics From Commercial Song Audio: The First Step Towards Singing Content Processing

> How many songs were collected?

### Common Retrieved Chunks

#### Passage 1617

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> To make our work easier and compatible to more available singing content, we collected 130 music-removed (or vocal-only) English songs from www.youtube.com so as to consider only the vocal line.The music-removing processes are conducted by the video owners, containing the original vocal recordings by the singers and vocal elements for remix purpose.
> 
> After initial test by speech recognition system trained with LibriSpeech BIBREF20 , we dropped 20 songs, with WERs exceeding 95%. The remaining 110 pieces of music-removed version of commercial English popular songs were produced by 15 male singers, 28 female singers and 19 groups. The term group means by more than one person. No any further preprocessing was performed on the data, so the data preserves many characteristics of the vocal extracted from commercial polyphonic music, such as harmony, scat, and silent parts. Some pieces also contain overlapping verses and residual background music, and some frequency components may be truncated. Below this database is called vocal data here.
> 
> These songs were manually segmented into fragments with duration ranging from 10 to 35 sec primarily at the end of the verses. Then we randomly divided the vocal data by the singer and split it into training and testing sets. We got a total of 640 fragments in the training set and 97 fragments in the testing set. The singers in the two sets do not overlap. The details of the vocal data are listed in Table. TABREF3 .
> 
> Because music genre may affect the singing style and the audio, for example, hiphop has some rap parts, and rock has some shouting vocal, we obtained five frequently observed genre labels of the vocal data from wikipedia BIBREF21 : pop, electronic, rock, hiphop, and R&B/soul. The details are also listed in Table. TABREF3 . Note that a song may belong to multiple genres.
> 
> To train initial models for speech for adaptation to singing voice, we used 100 hrs of English clean speech data of LibriSpeech.

#### Relevance 1617

Label: 

#### Passage 1618

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In addition to the data set from LibriSpeech (803M words, 40M sentences), we collected 574k pieces of lyrics text (totally 129.8M words) from lyrics.wikia.com, a lyric website, and the lyrics were normalized by removing punctuation marks and unnecessary words (like ’[CHORUS]’). Also, those lyrics for songs within our vocal data were removed from the data set.

#### Relevance 1618

Label: 

#### Passage 1619

Retrieved by: BM25, Hybrid RRF

> in singing voice.
> 
> Applying ASR technologies to singing voice has been studied for long. However, not too much work has been reported, probably because the recognition accuracy remained to be relatively low compared to the experiences for speech. But such low accuracy is actually natural considering the various difficulties caused by the significant differences between singing voice and speech. An extra major problem is probably the lack of singing voice database, which pushed the researchers to collect their own closed datasets BIBREF12 , BIBREF15 , BIBREF17 , which made it difficult to compare results from different works.
> 
> Having the language model learned from a data set of lyrics is definitely helpful BIBREF15 , BIBREF17 . Hosoya et al. BIBREF16 achieved this with finite state automaton. Sasou et al. BIBREF12 actually prepared a language model for each song. In order to cope with the acoustic characteristics of singing voice, Sasou et al. BIBREF12 , BIBREF14 proposed AR-HMM to take care of the high-pitched sounds and prolonged vowels, while recently Kawai et al. BIBREF15 handled the prolonged vowels by extending the vowel parts in the lexicon, both achieving good improvement. Adaptation from models trained with speech was attractive, and various approaches were compared by Mesaros el al. BIBREF18 .
> 
> In this paper, we wish our work can be compatible to more available singing content, therefore in the initial effort we collected about five hours of music-removed version of English songs directly from commercial singing content on YouTube. The descriptive term "music-removed" implies the background music have been removed somehow. Because many very impressive works were based on Japanese songs BIBREF12 , BIBREF13 , BIBREF14 , BIBREF15 , BIBREF16 , the comparison is difficult. We analyzed various approaches with HMM, deep learning with data augmentation, and acoustic adaptation on fragment, song, singer, and genre levels, primarily based on fMLLR BIBREF19 . We also trained the language model with a corpus of lyrics, and modify the pronunciation lexicon and increase the transition probability of HMM for prolonged vowels. Initial results are reported.

#### Relevance 1619

Label: 

#### Passage 1621

Retrieved by: BM25, Dense, Hybrid RRF

> The exploding multimedia content over the Internet, has created a new world of spoken content processing, for example the retrieval BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 , BIBREF4 , browsing BIBREF5 , summarization BIBREF0 , BIBREF5 , BIBREF6 , BIBREF7 , and comprehension BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 of spoken content. On the other hand, we may realize there still exists a huge part of multimedia content not yet taken care of, i.e., the singing content or those with audio including songs. Songs are human voice carrying plenty of semantic information just as speech. It will be highly desired if the huge quantities of singing content can be similarly retrieved, browsed, summarized or comprehended by machine based on the lyrics just as speech. For example, it is highly desired if song retrieval can be achieved based on the lyrics in addition.
> 
> Singing voice can be considered as a special type of speech with highly flexible and artistically designed prosody: the rhythm as artistically designed duration, pause and energy patterns, the melody as artistically designed pitch contours with much wider range, the lyrics as artistically authored sentences to be uttered by the singer. So transcribing lyrics from song audio is an extended version of automatic speech recognition (ASR) taking into account these differences.
> 
> On the other hand, singing voice and speech differ widely in both acoustic and linguistic characteristics. Singing signals are often accompanied with some extra music and harmony, which are noisy for recognition. The highly flexible pitch contours with much wider range BIBREF12 , BIBREF13 , the significantly changing phone durations in songs, including the prolonged vowels BIBREF14 , BIBREF15 over smoothly varying pitch contours, create much more problems not existing in speech. The falsetto in singing voice may be an extra type of human voice not present in normal speech. Regarding linguistic characteristics BIBREF16 , BIBREF17 , word repetition and meaningless words (e.g.oh) frequently appear in the artistically authored lyrics in singing voice.
> 
> Applying ASR technologies to singing voice has been studied for long. However, not too much work has been reported, probably because the recognition accuracy remained to be relatively low compared to the experiences for speech. But such

#### Relevance 1621

Label: 

#### Passage 1622

Retrieved by: Dense, Hybrid RRF

> In this paper we report some initial results of transcribing lyrics from commercial song audio using different sets of acoustic models, adaptation approaches, language models and lexicons. Techniques for special characteristics of song audio were considered. The achieved WER was relatively high compared to experiences in speech recognition. However, considering the much more difficult problems in song audio and the wide difference between speech and singing voice, the results here may serve as good references for future work to be continued.

#### Relevance 1622

Label: 

#### Passage 1623

Retrieved by: Dense, Hybrid RRF followed by BGE reranking

> In Fig. FIGREF5 Model E includes different models obtained with fMLLR over different levels, Models E-1,2,3,4. But in Table. TABREF14 only Model E-4 is listed. Complete results for Models E-1,2,3,4 are listed in Table. TABREF19 , all for Lyrics Language Model with extended lexicon. Row (4) here is for Model E-4, or fMLLR over fragment level, exactly row (7) of Table. TABREF14 . Rows (1)(2)(3) are the same as row (5) here, except over levels of genre, singer and song. We see fragment level is the best, probably because fragment(10-35 sec long) is the smallest unit and the acoustic characteristic of signals within a fragment is almost uniform (same genre, same singer and the same song).

#### Relevance 1623

Label: 

### BM25

#### Passage 1620

Retrieved by: BM25

> Consider the many errors caused by the frequently appearing prolonged vowels in song audio, we considered two approaches below.
> 
> The previously proposed approach BIBREF15 was adopted here as shown by the example in Fig. FIGREF10 (a). For the word “apple”, each vowel within the word ( but not the consonants) can be either repeated or not, so for a word with INLINEFORM0 vowels, INLINEFORM1 pronunciations become possible. In the experiments below, we only did it for words with INLINEFORM2 .
> 
> This is also shown in Fig. FIGREF10 . Assume an vowel HMM have INLINEFORM0 states (including an end state). Let the original self-looped probability of state INLINEFORM1 is denoted INLINEFORM2 and the probability of transition to the next state is INLINEFORM3 . We increased the self-looped transition probabilities by replacing INLINEFORM4 by INLINEFORM5 . This was also done for vowel HMMs only but not for consonants.

#### Relevance 1620

Label: 

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1624

Retrieved by: Hybrid RRF followed by BGE reranking

> We analyzed the perplexity and out-of-vocabulary(OOV) rate of the two language models (trained with LibriSpeech and Lyrics respectively) tested on the transcriptions of the testing set of vocal data. Both models are 3-gram, pruned with SRILM with the same threshold. LM trained with lyrics was found to have a significantly lower perplexity(123.92 vs 502.06) and a much lower OOV rate (0.55% vs 1.56%).
> 
> Fig. FIGREF12 depicts the histogram for pitch distribution for speech and different genders of vocal. We can see the pitch values of vocal are significantly higher with a much wider range, and female singers produce slightly higher pitch values than male singers and groups.

#### Relevance 1624

Label: 

#### Passage 1625

Retrieved by: Hybrid RRF followed by BGE reranking

> From the data, we found errors frequently occurred under some specific circumstances, such as high-pitched voice, widely varying phone duration, overlapping verses (multiple people sing simultaneously), and residual background music.
> 
> Figure FIGREF15 shows a sample recognition results obtained with Model E-4 as in row(7) of Table. TABREF14 , showing the error caused by high-pitched voice and overlapping verses. At first, the model successfully decoded the words, "what doesn't kill you makes", but afterward the pitch went high and a lower pitch harmony was added, the recognition results then went totally wrong.

#### Relevance 1625

Label: 

## Question 0177

Paper: Hotel2vec: Learning Attribute-Aware Hotel Embeddings with Self-Supervision

> what dataset was used for training?

### Common Retrieved Chunks

#### Passage 1626

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> The learned hotel embeddings can be used for recommending similar hotels in various situations. In this section, we show examples of how these embeddings are helpful with real examples of hotels from our dataset.

#### Relevance 1626

Label: 

#### Passage 1627

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Our dataset contains more than 40M user click sessions, which includes more than 1.1 million unique hotels. A click session is defined as a span of clicks performed by a user with no gap of more than 7 days. We randomly split the sessions into training, validation, and test with a ratio of 8:1:1.
> 
> We use a system with 64GB RAM, 8 CPU cores, and a Tesla V100 GPU. We use Python 3 as the programming language and the Tensorflow BIBREF21 library for the neural network architecture and gradient calculations. is sufficient for prevention of overfitting.
> 
> We tune the hyperparameters for all models, including the baseline session-only model, on the validation set. We search for a learning rate from $\lbrace 0.01, 0.1, 0.5, 1.0, 2.5\rbrace $ and embedding dimensions from $\lbrace 32, 128\rbrace $. To train the model weights, we use stochastic gradient descent (SGD) with exponential decay since it performs better than other optimizers in our case, and a batch size of 4096.
> 
> For our implementation of the session-only model, a learning rate of 0.5 and embedding dimension of 32 worked best. Throughout the remainder of the paper, we refer to this model as the session-32 model. For our enriched model (hotel2vec), a learning rate of 0.05 worked best; for the dimensionality of the embedding vectors, we found that letting $V_c, V_e \in {R}^{32}$, $V_a \in {R}^{15}$ and $V_g \in {R}^{5}$ worked best. We refer to this model as the enriched-32 model.

#### Relevance 1627

Label: 

#### Passage 1628

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this section, we present several experiments to evaluate the performance of the trained hotel2vec embeddings. Before diving into the details of the experiments, we first describe the dataset and model parameters.

#### Relevance 1628

Label: 

#### Passage 1631

Retrieved by: Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In this section, we first look at the learning curves for both the session-32 and enriched-32 models. Then, we analyse the effect of $N$ (number of negative samples), $lr$ (learning rate), and the optimization algorithm on the performance of our model.
> 
> Figure FIGREF35 shows the overall training progress of both the session-32 and enriched-32 models with their respective best hyperparameters. As shown in Figure FIGREF35, our model achieves similar performance with fewer data.
> 
> An interesting phenomenon is the effect of increasing the number of negative samples on training time and accuracy. Although it takes more time to create a large number of negative samples, as Figure FIGREF36 shows, using more negative samples results in faster training times.
> 
> We show empirical experiments with various optimization algorithms and learning rates, summarized in Figure FIGREF37. Surprisingly, we see that SGD with exponential learning rate decay outperforms most optimizers with sophisticated learning rate adaptations. We believe this is due to large variance and overfitting in the early stages of training. These issues have been observed in other tasks such as BIBREF22, BIBREF23, BIBREF24, suggesting the need to use tricks such as warm-up heuristics when using momentum-based optimization algorithms to learn embeddings on large, diverse datasets such as ours.

#### Relevance 1631

Label: 

#### Passage 1632

Retrieved by: Dense, Hybrid RRF

> Here we analyze how well the model learns embeddings for hotels with little to no presence in the training data. To demonstrate the effectiveness of our model, we compare the enriched model's hits@k with the session-only model's hits@k, for 14K target hotels that were absent during training. Table TABREF33 shows results in the filtered scenario. As we can see, the proposed enriched embedding significantly outperforms the session based embeddings for cold-start hotels.
> 
> In addition, we use a simple heuristic for cold-start imputation and compare the results with the enriched model for cold-start hotels. To impute vectors for cold-start hotels, we borrow the idea in BIBREF2 and use price, star rating, geodesic distance, type of the property (e.g., hotel, vacation rental, etc.) size in terms of number of rooms, and the geographic market information. For each imputed property, we collect the most similar properties in the same market based on the above features, considering only those properties that fall within a radius of 5km of the target hotel. Results are in Table TABREF33. The heuristic imputation technique improves the Session-32 model's performance on cold-start hotels, but it remains well below that of the enriched model.

#### Relevance 1632

Label: 

### BM25

#### Passage 1629

Retrieved by: BM25

> A common scenario is finding similar hotels to a target hotel in other destinations. For example, when the user searches for a specific hotel name (e.g., Hotel Beacon, NY) we would like to be able to recommend a few similar hotels. The learned embeddings can be used to find top-k most similar hotels to a given one. Given a target hotel $h$, we compute the cosine similarity of every other hotel with $h$ and pick the most similar hotels. Rigid evaluation of this system requires A/B testing; here we show a few examples comparing our enriched embeddings and the session-only embeddings in Figure FIGREF29 to provide some intuition for the behavior of the two models.

#### Relevance 1629

Label: 

#### Passage 1630

Retrieved by: BM25

> Recommendation is an inherently challenging task that requires learning user interests and behaviour. There has been a significant body of research on advancing it using various frameworks BIBREF3, BIBREF4, BIBREF5, BIBREF6, BIBREF7. Learning a semantic representation/embedding of the items being recommended is a critical piece of most of these frameworks.
> 
> Deep learning models have been widely used for learning embeddings BIBREF8, BIBREF9, BIBREF10. One prominent use case is learning product embeddings for e-commerce. In BIBREF1, BIBREF11, the authors develop an approach based on the skip-gram model BIBREF0, frequently used in natural language processing. They leverage users' purchase histories obtained from their e-mail receipts to learn a dense representation of products. Each user's complete purchase history is represented as a sequence, which is treated as a sentence in which the items are considered words.
> 
> In more recent work BIBREF2, the authors use the skip-gram framework to learn embeddings for vacation rental properties. They extend the ideas in BIBREF1 to take into account a user's click stream data during a session. A key contribution of their method is the modification of the skip-gram model to always include the booked hotels in the context of each target token, so that special attention is paid to bookings. They also improve negative sampling by sampling from the same market, which leads to better within-market listing similarities. Nevertheless, their model relies exclusively on large amounts of historical user engagement data, which is a major drawback when such data are sparse.
> 
> In another relevant work, BIBREF12, authors propose a framework for YouTube video recommendation which fuses multiple features (e.g., video watches, search tokens, geo embeddings) into a unified representation via a neural architecture. They then use these embeddings for candidate generation and ranking. The main limitation of this work is that the individual embeddings are learned separately, and then combined via a neural network to perform classification.
> 
> Similar to our work on hotel2vec, there are also some works which attempt to include explicit item attributes (e.g., size, artist, model, color) within the sequence prediction framework using various strategies. In BIBREF13, the item metadata is injected into the model as side information to regularize the item embeddings. In their approach, they only use

#### Relevance 1630

Label: 

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1633

Retrieved by: Hybrid RRF followed by BGE reranking

> Figure FIGREF7 illustrates the proposed architecture for an enriched, hotel2vec model. As we can see, each aspect of the hotel is embedded separately, and these representations are later concatenated and further compressed before being used for context prediction.
> 
> Formally, a click session is defined as a sequence of hotels (items) $\lbrace h_1, h_2, \cdots , h_n\rbrace $ clicked on by a user during a defined window of time or visit. We denote the click, amenity, geographic, and enriched embedding vectors with $\mathbf {V}_c$, $\mathbf {V}_a$, $\mathbf {V}_g$, and $\mathbf {V}_e$ respectively. These are defined as follows:
> 
> where $I_c$ is the one-hot encoding of hotels in the click session, and $I_g$ is a continuous vector with geographical coordinates of the hotel. Amenity features can be categorical or numerical with possible missing values. Thus, $I_a$ is partitioned per feature, where for numerical features we simply use an element of $I_a$ assigned with the value of that feature, and for categorical features with $m$ categories, we assign $m$ elements of $I_a$ and set the corresponding category to 1 and the others to 0. If the feature is missing, we set everything to 0. $\operatornamewithlimits{ReLU}$ is the rectified linear unit activation function BIBREF17 and $f(x; \mathbf {W})$ is a normalized projection layer parameterized with trainable weights $\mathbf {W}$, i.e., $f(x; \mathbf {W}) = \operatornamewithlimits{ReLU}(\frac{x \mathbf {W}}{\hphantom{{}_2}\Vert x \mathbf {W} \Vert _{\scriptstyle {2}}})$.
> 
> We train our model using negative sampling based on optimizing the noise contrastive estimation (NCE) loss BIBREF18. More formally, given $h_t$ as the target, we estimate the probability of $h_c$ being a context hotel to be
> 
> where $\mathbf {W}_{c,:}$ is the $c^{\text{th}}$ row of $W_{\scriptstyle _{NCE}}$. We find parameters of the model by maximizing the probabilities of correct predictions. We train the model using backpropagation and minimizing the following loss function:
> 
> where $\mathbf {V}_{e_{\scriptstyle {t}}}$ is the enriched embedding of $h_t$, $\mathbf {W}_{i,:}$ is $i^{\text{th}}$ row of $W_{\scriptstyle _{NCE}}$ matrix, $\mathcal {N}_c = \lbrace h_i| 1 \le i \le N, h_i \sim P_n(h_c)\rbrace $ is the set of negative examples, and $P_n(h_c)$ is the distribution which we use to pick the negative samples. We train our model by maximizing equation DISPLAY_FORM10 using batch stochastic gradient descent.

#### Relevance 1633

Label: 

## Question 0178

Paper: Prose for a Painting

> What models are used for painting embedding and what for language style transfer?

### Common Retrieved Chunks

#### Passage 1634

Retrieved by: BM25, Dense, Hybrid RRF

> Neural networks have been successfully used to describe images with text using sequence-to-sequence models BIBREF0. However, the results are simple and dry captions which are one or two phrases long. Humans looking at a painting see more than just objects. Paintings stimulate sentiments, metaphors and stories as well. Therefore, our goal is to have a neural network describe the painting artistically in a style of choice. As a proof of concept, we present a model which generates Shakespearean prose for a given painting as shown in Figure FIGREF1. Accomplishing this task is difficult with traditional sequence to sequence models since there does not exist a large collection of Shakespearean prose which describes paintings: Shakespeare's works describes a single painting shown in Figure FIGREF3. Fortunately we have a dataset of modern English poems which describe images BIBREF1 and line-by-line modern paraphrases of Shakespeare's plays BIBREF2. Our solution is therefore to combine two separately trained models to synthesize Shakespearean prose for a given painting.

#### Relevance 1634

Label: 

#### Passage 1635

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> In conclusion, combining two pipelines with an intermediate representation works well in practice. We observe that a CNN-RNN based image-to-poem net combined with a seq2seq model with parallel text corpus for text style transfer synthesizes Shakespeare-style prose for a given painting. For the seq2seq model used, we observe that it performs better in practice using global attention as compared with local attention. We make our models and code publicly available BIBREF12. In future work we would like to experiment with GANs in the absence of non-parallel datasets, so that we can use varied styles for text style transfer. We would also like to experiment with cross aligned auto-encoders, which form a latent content representation, to efficiently separate style and content.

#### Relevance 1635

Label: 

#### Passage 1636

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> A general end-to-end approach to sequence learning BIBREF3 makes minimal assumptions on the sequence structure. This model is widely used in tasks such as machine translation, text summarization, conversational modeling, and image captioning. A generative model using a deep recurrent architecture BIBREF0 has also beeen used for generating phrases describing an image. The task of synthesizing multiple lines of poetry for a given image BIBREF1 is accomplished by extracting poetic clues from images. Given the context image, the network associates image attributes with poetic descriptions using a convolutional neural net. The poem is generated using a recurrent neural net which is trained using multi-adversarial training via policy gradient.
> 
> Transforming text from modern English to Shakespearean English using text "style transfer" is challenging. An end to end approach using a sequence-to-sequence model over a parallel text corpus BIBREF2 has been proposed based on machine translation. In the absence of a parallel text corpus, generative adversarial networks (GANs) have been used, which simultaneously train two models: a generative model which captures the data distribution, and a discriminative model which evaluates the performance of the generator. Using a target domain language model as a discriminator has also been employed BIBREF4, providing richer and more stable token-level feedback during the learning process. A key challenge in both image and text style transfer is separating content from style BIBREF5, BIBREF6, BIBREF7. Cross-aligned auto-encoder models have focused on style transfer using non-parallel text BIBREF7. Recently, a fine grained model for text style transfer has been proposed BIBREF8 which controls several factors of variation in textual data by using back-translation. This allows control over multiple attributes, such as gender and sentiment, and fine-grained control over the trade-off between content and style.

#### Relevance 1636

Label: 

#### Passage 1637

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We perform a qualitative analysis of the Shakespearean prose generated for the input paintings. We conducted a survey, in which we presented famous paintings including those shown in Figures FIGREF1 and FIGREF10 and the corresponding Shakespearean prose generated by the model, and asked 32 students to rate them on the basis of content, creativity and similarity to Shakespearean style on a Likert scale of 1-5. Figure FIGREF12 shows the result of our human evaluation.
> 
> The average content score across the paintings is 3.7 which demonstrates that the prose generated is relevant to the painting. The average creativity score is 3.9 which demonstrates that the model captures more than basic objects in the painting successfully using poetic clues in the scene. The average style score is 3.9 which demonstrates that the prose generated is perceived to be in the style of Shakespeare.
> 
> We also perform a quantitative analysis of style transfer by generating BLEU scores for the model output using the style transfer dataset. The variation of the BLEU scores with the source sentence lengths is shown in Figure FIGREF11. As expected, the BLEU scores decrease with increase in source sentence lengths.

#### Relevance 1637

Label: 

#### Passage 1638

Retrieved by: BM25, Hybrid RRF

> We use a total three datasets: two datasets for generating an English poem from an image, and Shakespeare plays and their English translations for text style transfer.
> 
> We train a model for generating poems from images based on two datasets BIBREF1. The first dataset consists of image and poem pairs, namely a multi-modal poem dataset (MultiM-Poem), and the second dataset is a large poem corpus, namely a uni-modal poem dataset (UniM-Poem). The image and poem pairs are extended by adding the nearest three neighbor poems from the poem corpus without redundancy, and an extended image and poem pair dataset is constructed and denoted as MultiM-Poem(Ex)BIBREF1.
> 
> We use a collection of line-by-line modern paraphrases for 16 of Shakespeare’s plays BIBREF2, for training a style transfer network from English poems to Shakespearean prose. We use 18,395 sentences from the training data split. We keep 1,218 sentences in the validation data set and 1,462 sentences in our test set.

#### Relevance 1638

Label: 

### BM25

None

### Dense

#### Passage 1639

Retrieved by: Dense

> Since we do not have an end-to-end dataset, the generated English poem may not work well with Shakespeare style transfer as shown in Figure FIGREF12 for "Starry Night" with a low average content score. This happens when the style transfer dataset does not have similar words in the training set of sentences. A solution would be to expand the style transfer dataset, for a better representation of the poem data.

#### Relevance 1639

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1640

Retrieved by: Hybrid RRF followed by BGE reranking

> We use a sequence-to-sequence model which consists of a single layer unidrectional LSTM encoder and a single layer LSTM decoder and pre-trained retrofitted word embeddings shared between source and target sentences. We experimented with two different types of attention: global attention BIBREF9, in which the model makes use of the output from the encoder and decoder for the current time step only, and Bahdanau attention BIBREF10, where computing attention requires the output of the decoder from the prior time step. We found that global attention performs better in practice for our task of text style transfer.

#### Relevance 1640

Label: 

#### Passage 1641

Retrieved by: Hybrid RRF followed by BGE reranking

> For Shakespearizing modern English texts, we experimented with various types of sequence to sequence models. Since the size of the parallel translation data available is small, we leverage a dictionary providing a mapping between Shakespearean words and modern English words to retrofit pre-trained word embeddings. Incorporating this extra information improves the translation task. The large number of shared word types between the source and target sentences indicates that sharing the representation between them is beneficial.

#### Relevance 1641

Label: 

## Question 0179

Paper: Do Sentence Interactions Matter? Leveraging Sentence Level Representations for Fake News Classification

> What are the neural baselines mentioned?

### Common Retrieved Chunks

#### Passage 1642

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> We use SLN: Satirical and Legitimate News Database BIBREF2, RPN: Random Political News Dataset BIBREF10 and LUN: Labeled Unreliable News Dataset BIBREF0 for our experiments. Table TABREF4 shows the statistics. Since all of the previous methods on the aforementioned datasets are non-neural, we implement the following neural baselines,
> 
> CNN: In this model, we apply a 1-d CNN (Convolutional Neural Network) layer BIBREF11 with filter size 3 over the word embeddings of the sentences within a document. This is followed by a max-pooling layer to get a single document vector which is passed to a fully connected projection layer to get the logits over output classes.
> 
> LSTM: In this model, we encode the document using a LSTM (Long Short-Term Memory) layer BIBREF12. We use the hidden state at the last time step as the document vector which is passed to a fully connected projection layer to get the logits over output classes.
> 
> BERT: In this model, we extract the sentence vector (representation corresponding to [CLS] token) using BERT (Bidirectional Encoder Representations from Transformers) BIBREF4 for each sentence in the document. We then apply a LSTM layer on the sentence embeddings, followed by a projection layer to make the prediction for each document.

#### Relevance 1642

Label: 

#### Passage 1643

Retrieved by: BM25, Dense, Hybrid RRF

> We use a randomly initialized embedding matrix with 100 dimensions. We use a single layer LSTM to encode the sentences prior to the graph neural networks. All the hidden dimensions used in our networks are set to 100. The node embedding dimension is 32. For GCN and GAT, we set $\sigma $ as LeakyRelU with slope 0.2. We train the models for a maximum of 10 epochs and use Adam optimizer with learning rate 0.001. For all the models, we use max-pool for pooling, which is followed by a fully connected projection layer with output nodes equal to the number of classes for classification.

#### Relevance 1643

Label: 

#### Passage 1644

Retrieved by: BM25, Hybrid RRF

> Satire, according to BIBREF5, is complicated because it occupies more than one place in the framework for humor, proposed by BIBREF6: it clearly has an aggressive and social function, and often expresses an intellectual aspect as well. BIBREF2 defines news satire as a genre of satire that mimics the format and style of journalistic reporting. Datasets created for the task of identifying satirical news articles from the trusted ones are often constructed by collecting documents from different online sources BIBREF2. BIBREF7 hypothesized that this encourages the models to learn characteristics for different publication sources rather than characteristics of satire. In this work, we show that our proposed model generalizes to articles from unseen publication sources.
> 
> BIBREF0 extends BIBREF2's work by offering a quantitative study of linguistic differences found in articles of different types of fake news such as hoax, propaganda and satire. They also proposed predictive models for graded deception across multiple domains. BIBREF0 found that neural methods didn't perform well for this task and proposed to use a Max-Entropy classifier. We show that our proposed neural network based on graph convolutional layers can outperform this model. Recent works by BIBREF8, BIBREF9 show that sophisticated neural models can be used for satirical news detection. To the best of our knowledge, none of the previous works represent individual documents as graphs where the nodes represent the sentences for performing classification using a graph neural network.

#### Relevance 1644

Label: 

#### Passage 1645

Retrieved by: BM25, Hybrid RRF

> The graph convolutional network BIBREF14 is a spectral convolutional operation denoted by $f(Z^l, E|W^l)$,
> 
> Here, $Z^l$ is the output feature corresponding to the nodes after $l^{th}$ convolution. $W^l$ is the parameter associated with the $l^{th}$ layer. We set $Z^0 = S$. Based on the above operation, we can define arbitrarily deep networks. For our experiments, we just use a single layer unless stated otherwise. By default, the adjacency matrix ($E$) is fully connected i.e. all the elements are 1 except the diagonal elements which are all set to 0. We set $E$ based on semantic similarity model in our GCN + SS model. For the GCN + Attn model, we just add a self attention layer BIBREF15 after the GCN layer and before the pooling layer.

#### Relevance 1645

Label: 

#### Passage 1646

Retrieved by: BM25, Dense, Hybrid RRF

> BIBREF16 introduced graph attention networks to address various shortcomings of GCNs. Most importantly, they enable nodes to attend over their neighborhoods’ features without depending on the graph structure upfront. The key idea is to compute the hidden representations of each node in the graph, by attending over its neighbors, following a self-attention BIBREF15 strategy. By default, there is one attention head in the GAT model. For our GAT + 2 Attn Heads model, we use two attention heads and concatenate the node embeddings obtained from different heads before passing it to the pooling layer. For a fully connected graph, the GAT model allows every node to attend on every other node and learn the edge weights. Thus, initializing the edge weights using the SS model is useless as they are being learned. Mathematical details are provided in the Supplementary Material.

#### Relevance 1646

Label: 

### BM25

None

### Dense

#### Passage 1647

Retrieved by: Dense

> We conduct experiments across various settings and datasets. We report macro-averaged scores in all the settings.
> 
> 2-way classification b/w satire and trusted articles: We use the satirical and trusted news articles from LUN-train for training, and from LUN-test as the development set. We evaluate our model on the entire SLN dataset. This is done to emulate a real-world scenario where we want to see the performance of our classifier on an out of domain dataset. We don't use SLN for training purposes because it just contains 360 examples which is too little for training our model and we want to have an unseen test set. The best performing model on SLN is used to evaluate the performance on RPN.
> 
> 4-way classification b/w satire, propaganda, hoax and trusted articles: We split the LUN-train into a 80:20 split to create our training and development set. We use the LUN-test as our out of domain test set.

#### Relevance 1647

Label: 

#### Passage 1648

Retrieved by: Dense

> Table TABREF20 shows the quantitative results for the two way classification between satirical and trusted news articles. Our proposed GAT method with 2 attention heads outperforms SoTA. The semantic similarity model does not seem to have much impact on the GCN model, and considering the computing cost, we don't experiment with it for the 4-way classification scenario. Given that we use SLN as an out of domain test set (just one overlapping source, no overlap in articles), whereas the SoTA paper BIBREF2 reports a 10-fold cross validation number on SLN. We believe that our results are quite strong, the GAT + 2 Attn Heads model achieves an accuracy of 87% on the entire RPN dataset when used as an out-of-domain test set. The SoTA paper BIBREF10 on RPN reports a 5-fold cross validation accuracy of 91%. These results indicate the generalizability of our proposed model across datasets. We also present results of four way classification in Table TABREF21. All of our proposed methods outperform SoTA on both the in-domain and out of domain test set.
> 
> To further understand the working of our proposed model, we closely inspect the attention maps generated by the GAT model for satirical and trusted news articles for the SLN dataset. From Figure FIGREF16, we can see that the attention map generated for the trusted news article only focuses on two specific sentence whereas the attention weights are much more distributed in case of a satirical article. Interestingly enough the highlighted sentences in case of the trusted news article were the starting sentence of two different paragraphs in the article indicating the presence of similar sentence clusters within a document. This opens a new avenue for understanding the differences between different kind of text articles for future research.

#### Relevance 1648

Label: 

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1649

Retrieved by: Hybrid RRF followed by BGE reranking

> Each document in the corpus is represented as a graph. The nodes of the graph represent the sentences of a document while the edges represent the semantic similarity between a pair of sentences. Representing a document as a fully connected graph allows the model to directly capture the interaction of each sentence with every other sentence in the document. Formally,
> 
> We initialize the edge scores using BERT BIBREF4 finetuned on the semantic textual similarity task for computing the semantic similarity (SS) between two sentences. Refer to the Supplementary Material for more details regarding the SS model. Note that this representation drops the sentence order information but is better able to capture the interaction between far off sentences within a document.

#### Relevance 1649

Label: 

#### Passage 1650

Retrieved by: Hybrid RRF followed by BGE reranking

> This paper introduces a novel way of encoding articles for fake news classification. The intuition behind representing documents as a graph is motivated by the fact that sentences interact differently with each other across different kinds of article. Recurrent networks are unable to maintain long term dependencies in large documents, whereas a fully connected graph captures the interaction between sentences at unit distance. The quantitative result shows the effectiveness of our proposed model and the qualitative results validate our hypothesis about difference in sentence interaction across different articles. Further, we show that our proposed model generalizes to unseen datasets.

#### Relevance 1650

Label: 

#### Passage 1651

Retrieved by: Hybrid RRF followed by BGE reranking

> The supplementary material is available along with the code which provides mathematical details of the GAT model and few additional qualitative results.

#### Relevance 1651

Label: 

#### Passage 1652

Retrieved by: Hybrid RRF followed by BGE reranking

> In today's day and age of social media, there are ample opportunities for fake news production, dissemination and consumption. BIBREF0 break down fake news into three categories, hoax, propaganda and satire. A hoax article typically tries to convince the reader about a cooked-up story while propaganda ones usually mislead the reader into believing a false political or social agenda. BIBREF1 defines a satirical article as the one which deliberately exposes real-world individuals, organisations and events to ridicule.
> 
> Previous works BIBREF2, BIBREF0 rely on various linguistic and hand-crafted semantic features for differentiating between news articles. However, none of them try to model the interaction of sentences within the document. We observed a pattern in the way sentences cluster in different kind of news articles. Specifically, satirical articles had a more coherent story and thus all the sentences in the document seemed similar to each other. On the other hand, the trusted news articles were also coherent but the similarity between sentences from different parts of the document was not that strong, as depicted in Figure FIGREF1. We believe that the reason for such kind of behaviour is the presence of factual jumps across sections in a trusted document.
> 
> In this work, we propose a graph neural network-based model to classify news articles while capturing the interaction of sentences across the document. We present a series of experiments on News Corpus with Varying Reliability dataset BIBREF0 and Satirical Legitimate News dataset BIBREF2. Our results demonstrate that the proposed model achieves state-of-the-art performance on these datasets and provides interesting insights. Experiments performed in out-of-domain settings establish the generalizability of our proposed method.

#### Relevance 1652

Label: 

## Question 0180

Paper: FacTweet: Profiling Fake News Twitter Accounts

> Based on this paper, what is the more predictive set of features to detect fake news?

### Common Retrieved Chunks

#### Passage 1653

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> they obtain a result near to the majority class ($0.18$). Another finding from our experiments shows that the performance of the Tweet2vec is weak. This demonstrates that tweets' hashtags are not informative to detect non-factual accounts. In Table TABREF25, we present ablation tests so as to quantify the contribution of subset of features. The results indicate that most performance gains come from words embeddings, style, and morality features. Other features (emotion and sentiment) show lower importance: nevertheless, they still improve the overall system performance (on average 0.35% Macro-F$_1$ improvement). These performance figures suggest that non-factual accounts use semantic and stylistic hidden signatures mostly while tweeting news, so as to be able to mislead the readers and behave as reputable (i.e., factual) sources. We leave a more fine-grained, diachronic analysis of semantic and stylistic features – how semantic and stylistic signature evolve across time and change across the accounts' timelines – for future work.

#### Relevance 1653

Label: 

#### Passage 1654

Retrieved by: BM25, Dense, Hybrid RRF

> In this paper, we proposed a model that utilizes chunked timelines of tweets and a recurrent neural model in order to infer the factuality of a Twitter news account. Our experimental results indicate the importance of analyzing tweet stream into chunks, as well as the benefits of heterogeneous knowledge source (i.e., lexica as well as text) in order to capture factuality. In future work, we would like to extend this line of research with further in-depth analysis to understand the flow change of the used features in the accounts' streams. Moreover, we would like to take our approach one step further incorporating explicit temporal information, e.g., using timestamps. Crucially, we are also interested in developing a multilingual version of our approach, for instance by leveraging the now ubiquitous cross-lingual embeddings BIBREF22, BIBREF23.

#### Relevance 1654

Label: 

#### Passage 1655

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Social media platforms have made the spreading of fake news easier, faster as well as able to reach a wider audience. Social media offer another feature which is the anonymity for the authors, and this opens the door to many suspicious individuals or organizations to utilize these platforms. Recently, there has been an increased number of spreading fake news and rumors over the web and social media BIBREF0. Fake news in social media vary considering the intention to mislead. Some of these news are spread with the intention to be ironic or to deliver the news in an ironic way (satirical news). Others, such as propaganda, hoaxes, and clickbaits, are spread to mislead the audience or to manipulate their opinions. In the case of Twitter, suspicious news annotations should be done on a tweet rather than an account level, since some accounts mix fake with real news. However, these annotations are extremely costly and time consuming – i.e., due to high volume of available tweets Consequently, a first step in this direction, e.g., as a pre-filtering step, can be viewed as the task of detecting fake news at the account level.
> 
> The main obstacle for detecting suspicious Twitter accounts is due to the behavior of mixing some real news with the misleading ones. Consequently, we investigate ways to detect suspicious accounts by considering their tweets in groups (chunks). Our hypothesis is that suspicious accounts have a unique pattern in posting tweet sequences. Since their intention is to mislead, the way they transition from one set of tweets to the next has a hidden signature, biased by their intentions. Therefore, reading these tweets in chunks has the potential to improve the detection of the fake news accounts.
> 
> In this work, we investigate the problem of discriminating between factual and non-factual accounts in Twitter. To this end, we collect a large dataset of tweets using a list of propaganda, hoax and clickbait accounts and compare different versions of sequential chunk-based approaches using a variety of feature sets against several baselines. Several approaches have been proposed for news verification, whether in social media (rumors detection) BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, or in news claims BIBREF5, BIBREF6, BIBREF7, BIBREF8.

#### Relevance 1655

Label: 

#### Passage 1656

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> Data. We build a dataset of Twitter accounts based on two lists annotated in previous works. For the non-factual accounts, we rely on a list of 180 Twitter accounts from BIBREF1. This list was created based on public resources where suspicious Twitter accounts were annotated with the main fake news types (clickbait, propaganda, satire, and hoax). We discard the satire labeled accounts since their intention is not to mislead or deceive. On the other hand, for the factual accounts, we use a list with another 32 Twitter accounts from BIBREF19 that are considered trustworthy by independent third parties. We discard some accounts that publish news in languages other than English (e.g., Russian or Arabic). Moreover, to ensure the quality of the data, we remove the duplicate, media-based, and link-only tweets. For each account, we collect the maximum amount of tweets allowed by Twitter API. Table TABREF13 presents statistics on our dataset.
> 
> Baselines. We compare our approach (FacTweet) to the following set of baselines:
> 
> [leftmargin=4mm]
> 
> LR + Bag-of-words: We aggregate the tweets of a feed and we use a bag-of-words representation with a logistic regression (LR) classifier.
> 
> Tweet2vec: We use the Bidirectional Gated recurrent neural network model proposed in BIBREF20. We keep the default parameters that were provided with the implementation. To represent the tweets, we use the decoded embedding produced by the model. With this baseline we aim at assessing if the tweets' hashtags may help detecting the non-factual accounts.
> 
> LR + All Features (tweet-level): We extract all our features from each tweet and feed them into a LR classifier. Here, we do not aggregate over tweets and thus view each tweet independently.
> 
> LR + All Features (chunk-level): We concatenate the features' vectors of the tweets in a chunk and feed them into a LR classifier.
> 
> FacTweet (tweet-level): Similar to the FacTweet approach, but at tweet-level; the sequential flow of the tweets is not utilized. We aim at investigating the importance of the sequential flow of tweets.
> 
> Top-$k$ replies, likes, or re-tweets: Some approaches in rumors detection use the number of replies, likes, and re-tweets to detect rumors BIBREF21. Thus, we extract top $k$ replied, liked or re-tweeted tweets from each account to assess the

#### Relevance 1656

Label: 

#### Passage 1657

Retrieved by: BM25, Dense, Hybrid RRF, Hybrid RRF followed by BGE reranking

> of sequential chunk-based approaches using a variety of feature sets against several baselines. Several approaches have been proposed for news verification, whether in social media (rumors detection) BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, or in news claims BIBREF5, BIBREF6, BIBREF7, BIBREF8. The main orientation in the previous works is to verify the textual claims/tweets but not their sources. To the best of our knowledge, this is the first work aiming to detect factuality at the account level, and especially from a textual perspective. Our contributions are:
> 
> [leftmargin=4mm]
> 
> We propose an approach to detect non-factual Twitter accounts by treating post streams as a sequence of tweets' chunks. We test several semantic and dictionary-based features together with a neural sequential approach, and apply an ablation test to investigate their contribution.
> 
> We benchmark our approach against other approaches that discard the chronological order of the tweets or read the tweets individually. The results show that our approach produces superior results at detecting non-factual accounts.

#### Relevance 1657

Label: 

### BM25

None

### Dense

None

### Hybrid RRF

None

### Hybrid RRF followed by BGE reranking

#### Passage 1658

Retrieved by: Hybrid RRF followed by BGE reranking

> Given a news Twitter account, we read its tweets from the account's timeline. Then we sort the tweets by the posting date in ascending way and we split them into $N$ chunks. Each chunk consists of a sorted sequence of tweets labeled by the label of its corresponding account. We extract a set of features from each chunk and we feed them into a recurrent neural network to model the sequential flow of the chunks' tweets. We use an attention layer with dropout to attend over the most important tweets in each chunk. Finally, the representation is fed into a softmax layer to produce a probability distribution over the account types and thus predict the factuality of the accounts. Since we have many chunks for each account, the label for an account is obtained by taking the majority class of the account's chunks.
> 
> Input Representation. Let $t$ be a Twitter account that contains $m$ tweets. These tweets are sorted by date and split into a sequence of chunks $ck = \langle ck_1, \ldots , ck_n \rangle $, where each $ck_i$ contains $s$ tweets. Each tweet in $ck_i$ is represented by a vector $v \in {\rm I\!R}^d$ , where $v$ is the concatenation of a set of features' vectors, that is $v = \langle f_1, \ldots , f_n \rangle $. Each feature vector $f_i$ is built by counting the presence of tweet's words in a set of lexical lists. The final representation of the tweet is built by averaging the single word vectors.
> 
> Features. We argue that different kinds of features like the sentiment of the text, morality, and other text-based features are critical to detect the nonfactual Twitter accounts by utilizing their occurrence during reporting the news in an account's timeline. We employ a rich set of features borrowed from previous works in fake news, bias, and rumors detection BIBREF0, BIBREF1, BIBREF8, BIBREF9.
> 
> [leftmargin=4mm]
> 
> Emotion: We build an emotions vector using word occurrences of 15 emotion types from two available emotional lexicons. We use the NRC lexicon BIBREF10, which contains $\sim $14K words labeled using the eight Plutchik's emotions BIBREF11. The other lexicon is SentiSense BIBREF12 which is a concept-based affective lexicon that attaches emotional

#### Relevance 1658

Label: 
