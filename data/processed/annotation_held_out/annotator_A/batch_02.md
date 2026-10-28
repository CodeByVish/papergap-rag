# Passage relevance annotation

Annotator: 

Judge whether the passage provides information that helps answer the question, including useful partial evidence. Topic overlap alone is not sufficient. Judge only the supplied question and passage.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Do not change record numbers, questions or passages. Work independently without consulting another annotator or reference answers.

## Record 0101

Paper: Towards Supervised and Unsupervised Neural Machine Translation Baselines for Nigerian Pidgin

### Question

> What baselines do they propose?

### Passage

> The following insights can be drawn from the example translations shown in the tables above:
> 
> The unsupervised model performed poorly at some simple translation examples, such as the first translation example.
> 
> For all translation models, the model makes hypothesis that are grammatically and qualitatively correct, but do not exactly match the reference translation, such as the second translation example.
> 
> Surprisingly, the unsupervised model performs better at some relatively simple translation examples than both supervised models. The third example is a typical such case.
> 
> The supervised translation models seem to perform better at longer example translations than the unsupervised example.

### Relevance

Label: 

## Record 0102

Paper: Towards Supervised and Unsupervised Neural Machine Translation Baselines for Nigerian Pidgin

### Question

> What baselines do they propose?

### Passage

> Some work has been done on developing neural machine translation baselines for African languages. BIBREF4 implemented a transformer model which significantly outperformed existing statistical machine translation architectures from English to South-African Setswana. Also, BIBREF5 went further, to train neural machine translation models from English to five South African languages using two different architectures - convolutional sequence-to-sequence and transformer. Their results showed that neural machine translation models are very promising for African languages.
> 
> The only known natural language processing work done on any variant of Pidgin English is by BIBREF6. The authors provided the largest known Nigerian Pidgin English corpus and trained the first ever translation models between both languages via unsupervised neural machine translation due to the absence of parallel training data at the time.

### Relevance

Label: 

## Record 0103

Paper: Towards Supervised and Unsupervised Neural Machine Translation Baselines for Nigerian Pidgin

### Question

> What baselines do they propose?

### Passage

> Over 500 languages are spoken in Nigeria, but Nigerian Pidgin is the uniting language in the country. Between three and five million people are estimated to use this language as a first language in performing their daily activities. Nigerian Pidgin is also considered a second language to up to 75 million people in Nigeria, accounting for about half of the country's population according to BIBREF0.
> 
> The language is considered an informal lingua franca and offers several benefits to the country. In 2020, 65% of Nigeria's population is estimated to have access to the internet according to BIBREF1. However, over 58.4% of the internet's content is in English language, while Nigerian languages, such as Igbo, Yoruba and Hausa, account for less than 0.1% of internet content according to BIBREF2. For Nigerians to truly harness the advantages the internet offers, it is imperative that English content is able to be translated to Nigerian languages, and vice versa.
> 
> This work is a first attempt towards using contemporary neural machine translation (NMT) techniques to perform machine translation for Nigerian Pidgin, establishing solid baselines that will ease and spur future work. We evaluate the performance of supervised and unsupervised neural machine translation models using word-level and the subword-level tokenization of BIBREF3.

### Relevance

Label: 

## Record 0104

Paper: Towards Supervised and Unsupervised Neural Machine Translation Baselines for Nigerian Pidgin

### Question

> What baselines do they propose?

### Passage

> Special thanks to the Masakhane group for catalysing this work.

### Relevance

Label: 

## Record 0105

Paper: Towards Supervised and Unsupervised Neural Machine Translation Baselines for Nigerian Pidgin

### Question

> What baselines do they propose?

### Passage

> All baseline models were trained using the Transformer architecture of BIBREF7. We experiment with both word-level and Byte Pair Encoding (BPE) subword-level tokenization methods for the supervised models. We learned 4000 byte pair encoding tokens, following the findings of BIBREF5. For the unuspervised model, we experiment with only word-level tokenization.

### Relevance

Label: 

## Record 0106

Paper: Legal Question Answering using Ranking SVM and Deep Convolutional Neural Network

### Question

> What contribute to improve the accuracy on legal question answering task?

### Passage

> This work investigates Ranking SVM model and CNN for building a legal question answering system for Japan Civil Code. Experimental results show that feature selection affects significantly to the performance of SVM-Rank, in which a set of features consisting of (LSI, Manhattan, Jaccard) gives promising results for information retrieval task. For question answering task, the CNN model is sensitive to initial values of parameters and exerts higher accuracy when adding auxiliary features.
> 
> In our current work, we have not yet fully explored the characteristics of legal texts in order to utilize these features for building legal QA system. Properties such as references between articles or structured relations in legal sentences should be investigated more deeply. In addition, there should be more evaluation of SVM-Rank and other L2R methods to observe how they perform on this legal data using the same feature set. These are left as our future work.

### Relevance

Label: 

## Record 0107

Paper: Legal Question Answering using Ranking SVM and Deep Convolutional Neural Network

### Question

> What contribute to improve the accuracy on legal question answering task?

### Passage

> Legal text, along with other natural language text data, e.g. scientific literature, news articles or social media, has seen an exponential growth on the Internet and in specialized systems. Unlike other textual data, legal texts contain strict logical connections of law-specific words, phrases, issues, concepts and factors between sentences or various articles. Those are for helping people to make a correct argumentation and avoid ambiguity when using them in a particular case. Unfortunately, this also makes information retrieval and question answering on legal domain become more complicated than others.
> 
> There are two primary approaches to information retrieval (IR) in the legal domain BIBREF0 : manual knowledge engineering (KE) and natural language processing (NLP). In the KE approach, an effort is put into translating the way legal experts remember and classify cases into data structures and algorithms, which will be used for information retrieval. Although this approach often yields a good result, it is hard to be applied in practice because of time and financial cost when building the knowledge base. In contrast, NLP-based IR systems are more practical as they are designed to quickly process terabytes of data by utilizing NLP techniques. However, several challenges are presented when designing such system. For example, factors and concepts in legal language are applied in a different way from common usage BIBREF1 . Hence, in order to effectively answer a legal question, it must compare the semantic connections between the question and sentences in relevant articles found in advance BIBREF2 .
> 
> Given a legal question, retrieving relevant legal articles and deciding whether the content of a relevant article can be used to answer the question are two vital steps in building a legal question answering system. Kim et al. BIBREF2 exploited Ranking SVM with a set of features for legal IR and Convolutional Neural Network (CNN) BIBREF3 combining with linguistic features for question answering (QA) task. However, generating linguistic features is a non-trivial task in the legal domain. Carvalho et al. BIBREF1 utilized n-gram features to rank articles by using an extension of TF-IDF. For QA task, the authors adopted AdaBoost BIBREF4 with a set of similarity features between a query and an article pair BIBREF5 to classify

### Relevance

Label: 

## Record 0108

Paper: Legal Question Answering using Ranking SVM and Deep Convolutional Neural Network

### Question

> What contribute to improve the accuracy on legal question answering task?

### Passage

> In this stage, we illustrate our framework on COLIEE 2016 data. The framework was trained on XML files, from H18 to H23 and tested on XML file H24. Given a legal question, the framework first retrieves top five relevant articles and then transfers the question and relevant articles to CNN classifier. The running of framework was evaluated with 3 scenarios:
> 
> No voting: taking only a top relevant article to use for predicting an answer for that question.
> 
> Voting without ratio: each of results, which is generated by applying our Textual entailment model to each article, gives one vote to the answer which it belongs to. The final result is the answer with more votes.
> 
> Voting with ratio: similar to Voting without ratio. However, each of results gives one vote corresponding to article's relevant score. The final result is the answer with higher voting score.
> 
> Table 9 shows results with different scenarios. The result of No voting approach is influenced by IR task's performance, so the accuracy is not as high as using voting. The relevant score disparity between the first and second relevant article is large, which causes a worse result of Voting with ratio compared to Voting without ratio.

### Relevance

Label: 

## Record 0109

Paper: Legal Question Answering using Ranking SVM and Deep Convolutional Neural Network

### Question

> What contribute to improve the accuracy on legal question answering task?

### Passage

> Legal Question Answering is a form of textual entailment problem BIBREF14 , which can be viewed as a binary classification task. To capture the relation between a question and an article, a set of features can be used. In the COLLIE 2015, Kim BIBREF3 efficiently applied Convolution Neural Network (CNN) for the legal QA task. However, the small dataset is a limit of deep learning models. Therefores, we provided additional features to the CNN model.
> 
> The idea behind the QA is that we use CNN BIBREF2 with additional features. This is because: (i) CNN is capable to capture local relationship between neighboring words, which helps CNN to achieve excellent performance in NLP problems BIBREF15 , BIBREF2 , BIBREF16 , BIBREF17 and (ii) we can integrate our knowledge in legal domain in the form of statistical features, e.g. TF-IDF and LSI.
> 
> In Figure 2 , the input features $v_1,v_2,...,v_{400}$ are constructed and fed to the network as follows :
> 
> $v_1,v_3,v_5,...,v_{399}$ : a word embedding vector of the question sentence
> 
> $v_2,v_4,...,v_{400}$ : a word embedding vector of the most relevant article sentence
> 
> A sentence represented by a set of words was converted to a word embedding vector $v_1^{200}$ by using bag-of-words model (BOW) BIBREF18 . BOW model generates a vector representation for a sentence by taking a summation over embedding of words in the sentence. The vector is then normalized by the length of the sentence:
> 
> $$s= \frac{1}{n}\sum _{i= 1}^{n}s_{i}$$   (Eq. 22)
> 
> where: $s$ is a $d$ -dimensional vector of a sentence, $s_{i}$ is a $d$ -dimensional vector of $i^{th}$ word in the sentence, $n$ is the length of sentence. A word embedding model ( $d=200$ ) was trained by using Word2Vec BIBREF19 on the data of Japanese law corpus BIBREF1 . The corpus contains all Civil law articles of Japan's constitution with 13.5 million words from 642 cleaned and tokenized articles.
> 
> A filter was denoted as a weight vector $w$ with length $h$ ; $w$ will have $h$ parameters to be estimated. For each input vector $S \in \mathbb {R}^{d} $ , the feature map vector $O \in \mathbb {R}^{d-h+1}$ of the convolution operator with a filter $w$ was obtained by applying repeatedly $w$ to sub-vectors

### Relevance

Label: 

## Record 0110

Paper: Legal Question Answering using Ranking SVM and Deep Convolutional Neural Network

### Question

> What contribute to improve the accuracy on legal question answering task?

### Passage

> In order to build a legal IR, traditional models such as TF-IDF, BM25 or PL2F can be used to generate basic features for matching documents with a query. Nevertheless, to improve not only the accuracy but also the robustness of ranking function, it is essential to take into account a combination of fundamental features and other potential features. Hence, the idea is to build a L2R model, which incorporates various features to generate an optimal ranking function.
> 
> Among different L2R methods, Ranking SVM (SVM-Rank) BIBREF9 , a state-of-the-art pairwise ranking method and also a strong method for IR BIBREF10 , BIBREF11 , was used. Our model is an extended version of Kim's model BIBREF2 with two new aspects. Firstly, there is a big distinction between our features and Kim's features. While Kim used three types of features: lexical words, dependency pairs, and TF-IDF score; we conducted a series of experiments to discover a set of best features among six features as shown in Table 2 . Secondly, our model is applied to individual paragraphs as described in section "Data Observation" instead of the whole articles as in Kim's work.
> 
> Given n training queries $\lbrace q_i\rbrace _{i=1}^{n}$ , their associated document pairs $(x_u^{(i)},x_v^{(i)})$ and the corresponding ground truth label $y_{u,v}^{(i)}$ , SVM Rank optimizes the objective function shown in Equation ( 13 ) subject to constraints ( 14 ), and ( 15 ):
> 
> $$min \quad \frac{1}{2}\Vert w\Vert ^2 + \lambda \sum _{i=1}^{n}\sum _{u,v:y_{u,v}^{(i)}} \xi _{u,v}^{(i)}$$   (Eq. 13)
> 
> $$s.t. \quad w^T(x_u^{(i)} - x_v^{(i)}) \ge 1 - \xi _{u,v}^{(i)} \quad \text{if} \quad y_{u,v}^{(i)}=1$$   (Eq. 14)
> 
> where: $f(x)=w^Tx$ is a linear scoring function, $(x_u,x_v)$ is a pairwise and $\xi _{u,v}^{(i)}$ is the loss. The document pairwise in our model is a pair of a query and an article.
> 
> Based on the corpus constructed from all of the single-paragraph articles (see Section "Data Observation" ), three basic models were built: TF-IDF, LSI and Latent Dirichlet Allocation (LDA) BIBREF12 . Note that, LSI and LDA model transform articles and queries from their TF-IDF-weighted space into a latent space of a lower dimension. For COLIEE 2016 corpora, the dimension of both LSI and LDA is 300 instead of over 2,100 of TF-IDF

### Relevance

Label: 

## Record 0111

Paper: $\rho$-hot Lexicon Embedding-based Two-level LSTM for Sentiment Analysis

### Question

> What are the other models they compare to?

### Passage

> of such sentences BIBREF26 . Sentiments expressed in a conditional sentence can be difficult to determine due to the semantic condition. The sentiment polarities of interrogative sentences are also difficult to classify according to our empirical study.
> 
> Five types of words, namely, positive (Pos), negative (Neg), privative (Pri), suppositive (Sup), and interrogative (Int), are represented by the proposed encoding method. The rest words, which do not belong to any of the above five types, are named “others (Oth)" instead of “neutral" because some words, such as “the", are unrelated to “sentiment". The value of INLINEFORM0 in Eq. (6) is set as 10. The encoded vectors are as follows. INLINEFORM1
> 
> In the proposed INLINEFORM0 -hot embedding, the parameter INLINEFORM1 can be learned during training. The representation of the third clause (“but the rest is not so bad") of S1 in Subsection 3.1 is taken as an illustrative example. The new embedding of each word in this clause is as follows. DISPLAYFORM0
> 
> Certain types (e.g., positive, negative, and privative) of words should play more important roles than other words do in texts; therefore, their embeddings are also used in the attention layer. A new LSTM based on our lexicon embedding is proposed, as shown in Fig. 5. The attention layer and final dense vector of the network in Fig. 3(a) are calculated as follows. DISPLAYFORM0
> 
> where INLINEFORM0 is the attention weight for the INLINEFORM1 -th input, lt is the lexicon embedding for key lexical words for the INLINEFORM2 -th input, and INLINEFORM3 is the final dense vector. Eq. (2) is used in the first-level LSTM.
> 
> POS is usually used as a key cue in sentiment analysis BIBREF27 . To this end, we use additional lexicon embedding. The new lexicon embedding includes several major types of POS, namely, interrogative, exclamatory, and others. This new lexicon embedding is also applied to the attention layer. The motivation lies in that certain types of POS should play important roles in sentiment.
> 
> The proposed INLINEFORM0 -hot embedding is still applied to POS types in this study. According to our initial case studies, eight POS types are considered. They are noun, adjective, verb, pronoun, adverb, preposition, accessory, and others. The eight POS types

### Relevance

Label: 

## Record 0112

Paper: $\rho$-hot Lexicon Embedding-based Two-level LSTM for Sentiment Analysis

### Question

> What are the other models they compare to?

### Passage

> The proposed lexicon embedding is based on INLINEFORM0 -hot encoding. Therefore, INLINEFORM1 -hot encoding is first described.
> 
> For categorical data, one-hot encoding is the most widely used encoding strategy when different categories are independent. For example, if one-hot encoding is used to represent three categories, namely, positive, neutral, and negative, the encoding vectors for the three categories are INLINEFORM0 , INLINEFORM1 , and INLINEFORM2 , respectively.
> 
> In this work, many lexical cues are categorical data, and different categories are independent. These lexical cues can directly be represented by one-hot encoding. The encoded vectors for lexical cues are then concatenated with other vectors, such as character/word embedding. However, one-hot encoding presents two main limitations when the encoded vector is concatenated with other vectors.
> 
> The value difference between the elements of one-hot encoded vectors and those of other encoded vectors (e.g., word embedding vectors) may be large. Fig. 4 shows the histogram of the values of the elements of the word embedding vectors. The magnitude of most elements are smaller than 1.
> 
> The lengths of one-hot encoded vectors are usually shorter than those of other encoded vectors. Consequently, the proportion of one-hot encoded part is small in the concatenated vectors.
> 
> The above two limitations affect the final sentiment analysis performance. To this end, we propose a new encoding strategy. DISPLAYFORM0
> 
> where INLINEFORM0 is the INLINEFORM1 -hot encoded vector, INLINEFORM2 is the proportion parameter, INLINEFORM3 is the one-hot encoded vector, and INLINEFORM4 is an INLINEFORM5 -dimensional vector. If INLINEFORM6 and INLINEFORM7 are equal to 1, then INLINEFORM8 -hot encoding is reduced to one-hot encoding. The parameter INLINEFORM9 is applied to increase the length of the final encoded vector.
> 
> Most lexicon-based sentiment methods rely on four types of words, namely, positive, negative, neutral, and privative. These words are useful cues for predicting the sentiment labels of input texts. The incorporation of these words should also be useful. A previous study has shown that a typical document comprises approximately 8% of such sentences BIBREF26 . Sentiments expressed in a conditional sentence can be difficult to determine due to the semantic condition. The sentiment polarities of interrogative sentences are also difficult to classify according to our empirical study.
> 
> Five types of

### Relevance

Label: 

## Record 0113

Paper: $\rho$-hot Lexicon Embedding-based Two-level LSTM for Sentiment Analysis

### Question

> What are the other models they compare to?

### Passage

> lowest accuracies on all the three data sets. Considering that the performances of (traditional) CNN, Lex-rule, and BOW are relatively poor, they are not applied in the remaining parts.
> 
> In this experimental comparison, the proposed two-level LSTM is evaluated, whereas lexicon embedding is not used in the entire network. The primary goal is to test whether the introduced two-stage labeling and the two-level network structure are useful for sentiment analysis.
> 
> The raw and clause data listed in Table 1 are used to perform the two-level LSTM. Tl-LSTM denotes the two-level LSTM. “R+C" refer to the mixed data of raw and clause data. The test data are still the 1000 samples used in section 4.3.1 for each corpus. Table 4 shows the classification accuracies. To ensure that the results differ from those in Table 3, we explicitly add “R+C" after each algorithm in Table 4. In the last line of Table 4, the base results for each corpus in Table 3 are also listed.
> 
> On all the three data corpora, the proposed two-level network (without lexicon embedding) with character embedding, Tl-LSTM-C, outperforms all the other involved algorithms. On the travel and the mobile corpora, TI-LSTM-W outperforms Bi-LSTM-W. The results in Table 4 indicate that the performances of Tl-LSTM on the mixed training and test data (R+C) are better than those of Bi-LSTM. This comparison indicates that the proposed two-level LSTM is effective.
> 
> In addition, for the involved algorithms, most results achieved on “R+C" are better than the best results only achieved on `R'listed in Table 3. This comparison suggests that the introduced two-stage labeling is useful.
> 
> The results also show that in the two-level LSTM, character embedding is more effective than word embedding.
> 
> In this experimental run, lexicon embedding is used in the proposed two-level LSTM or INLINEFORM0 Tl-LSTM. Table 5 shows the results. The optimal parameter INLINEFORM1 is about 11.
> 
> The performances of TI-LSTM with lexicon embedding (i.e., INLINEFORM0 Tl-LSTM) are consistently better than those of TI-LSTM without lexicon embedding (i.e., Tl-LSTM) listed in Table 5. The improved accuracies of INLINEFORM1 TI-LSTM over Tl-LSTM on the three data corpora are explicitly listed in Table 6.
> 
> The experimental evaluation discussed in Subsection 4.3 verifies the effectiveness

### Relevance

Label: 

## Record 0114

Paper: $\rho$-hot Lexicon Embedding-based Two-level LSTM for Sentiment Analysis

### Question

> What are the other models they compare to?

### Passage

> crucial for learning systems. Nevertheless, texts with mixed sentiments are difficult for humans to label in text sentiment classification. In this study, a new labeling strategy is introduced to partition texts into those with pure and mixed sentiment orientations. These two categories of texts are labeled using different processes. A two-level network is accordingly proposed to utilize the two labeled data in our two-stage labeling strategy. Lexical cues (e.g., polar words, POS, conjunction words) are particularly useful in sentiment analysis. These lexical cues are used in our two-level network, and a new encoding strategy, that is, INLINEFORM0 -hot encoding, is introduced. INLINEFORM1 -hot encoding is motivated by one-hot encoding. However, the former alleviates the drawbacks of the latter. Three Chinese sentiment text data corpora are compiled to verify the effectiveness of the proposed methodology. Our proposed method achieves the highest accuracies on these three data corpora.
> 
> The proposed two-level network and lexicon embedding can also be applied to other types of deep neural networks. In our future work, we will extend our main idea into several networks and text mining applications.
> 
> The authors wish to thank Zefeng Han, Qing Yin, Lei Yang, Xiaonan Wang, Nan Chen, Rujing Yao, Lihong Guo, Pinglong Zhao for the labeling of the experimental data.

### Relevance

Label: 

## Record 0115

Paper: $\rho$-hot Lexicon Embedding-based Two-level LSTM for Sentiment Analysis

### Question

> What are the other models they compare to?

### Passage

> network and each part of the lexicon embedding.
> 
> We compile three Chinese text corpora from online data for three domains, namely, “hotel", “mobile phone (mobile)", and “travel". All texts are about user reviews. Each text sample collected is first partitioned into clauses according to Chinese tokens. Three clause sets are subsequently obtained from the three text corpora.
> 
> The labels “+1", “0.5", and “0" correspond to the three sentiment classes “positive", “neutral", and “negative", respectively. The text data are labeled according to our two-stage labeling strategy.
> 
> In the first stage, only one user is invited to label each clause sample as the sentiment orientations for clauses (or sub-sentences) are easy to label.
> 
> In the second stage, five users are invited to label each text sample in the three raw data sets. The average score of the five users on each sample is calculated. Samples with average scores located in [0.6, 1] are labeled as “positive". Samples with average scores located in [0, 0.4] are labeled as “negative". Others are labeled as “neutral". The details of the labeling results are shown in Table 1.
> 
> All the training and test data and the labels are available online.
> 
> In our experiments, the five types of key lexical words introduced in Subsection 3.3.2 are manually constructed. The details of the five types of words are listed in Table 2. The conjunction words are also manually constructed. The number of conjunction words used in the experiments is 169.
> 
> In each experimental run, the training set is compiled on the basis of the training data listed in Table 1. The compiling rule is specified before each experimental run. The test data are fixed to facilitate experimental duplication and comparison by other researchers.
> 
> In our experiments, three competing algorithms, namely, BOW, CNN, and (conventional) LSTM, are used.
> 
> For BOW, term frequency-inverse document frequency is utilized to construct features. Ridge regression BIBREF29 is used as a classifier. For CNN, a three-channel CNN is used. For LSTM, one-layer and two-layer bi-LSTM with attention are adopted, and the results of the network with superior performance are presented. CNN and LSTM are performed on TensorFlow, and default parameter settings are followed.
> 
> The key parameters are searched as

### Relevance

Label: 

## Record 0116

Paper: Investigating Linguistic Pattern Ordering in Hierarchical Natural Language Generation

### Question

> What evaluation metrics are used?

### Passage

> The E2E NLG challenge dataset BIBREF21 is utilized in our experiments, which is a crowd-sourced dataset of 50k instances in the restaurant domain. Our models are trained on the official training set and verified on the official testing set. As shown in Figure FIGREF2 , the inputs are semantic frames containing specific slots and corresponding values, and the outputs are the associated natural language utterances with the given semantics. For example, a semantic frame with the slot-value pairs “name[Bibimbap House], food[English], priceRange[moderate], area [riverside], near [Clare Hall]” corresponds to the target sentence “Bibimbap House is a moderately priced restaurant who's main cuisine is English food. You will find this local gem near Clare Hall in the Riverside area.”.
> 
> The data preprocessing includes trimming punctuation marks, lemmatization, and turning all words into lowercase. To prepare the labels of each layer within the hierarchical structure of the proposed method, we utilize spaCy toolkit to perform POS tagging for the target word sequences. Some properties such as names of restaurants are delexicalized (for example, replaced with a symbol “RESTAURANT_NAME”) to avoid data sparsity. In our experiments, we perform six different generating linguistic orders, in which each hierarchy is constructed based on different permutations of the POS tag sets: (1) nouns, proper nouns, and pronouns (2) verbs (3) adjectives and adverbs (4) others.
> 
> The probability of activating inter-layer and inner-layer teacher forcing is set to 0.5, the probability of teacher forcing is attenuated every epoch, and the decaying ratio is 0.9. The models are trained for 20 training epochs without early stop; when curriculum learning is applied, only the first layer is trained during first five epochs, the second decoder layer starts to be trained at the sixth epoch, and so on. To evaluate the quality of the generated sequences regarding both precision and recall, the evaluation metrics include BLEU and ROUGE (1, 2, L) scores with multiple references BIBREF22 .

### Relevance

Label: 

## Record 0117

Paper: Investigating Linguistic Pattern Ordering in Hierarchical Natural Language Generation

### Question

> What evaluation metrics are used?

### Passage

> In order to model the relationship between layers in a generating hierarchy, we further design attention mechanisms for the hierarchical decoder. The proposed attention mechanisms are content-based, which means the weights are determined based on hidden states of neural models: DISPLAYFORM0
> 
> where INLINEFORM0 is the hidden state at the current step, INLINEFORM1 are the hidden states from the previous decoder layer, and INLINEFORM2 is a learned weight matrix. At each decoding step, attention values INLINEFORM3 are calculated by these methods and then used to compute the weighted sum as a context vector, which is then concatenated to decoder inputs as additional information.

### Relevance

Label: 

## Record 0118

Paper: Investigating Linguistic Pattern Ordering in Hierarchical Natural Language Generation

### Question

> What evaluation metrics are used?

### Passage

> In the experiments, we borrow the idea of hierarchical decoding proposed by the previous work BIBREF8 and investigate various extensions of generating hierarchies. To examine the effectiveness of hierarchical decoders, we control our model size to be smaller than the baseline's. Specifically, the decoder in the baseline seq2seq model has hidden layers of size 400, while our models with hierarchical decoders have four decoding layers of size 100 for fair comparison.
> 
> Table TABREF13 compares the performance between a baseline and proposed models with different generating linguistic orders. For all generating hierarchies with different orders, simply replacing the decoder by a hierarchical decoder achieves significant improvement in every evaluation metrics; for example, the topmost generating hierarchy in Table TABREF13 has 49.25% improvement in BLEU, 30.03% in ROUGE-1, 96.48% in ROUGE-2, and 25.99% in ROUGE-L respectively. In other words, separating the generation process into several phases is proven to be a promising method. Performing curriculum learning strategy offers a considerable improvement, take the topmost generating hierarchy in Table TABREF13 for example, this method yields a 102.07% improvement in BLEU, 48.26% in ROUGE-1, 144.8% in ROUGE-2, and 39.18% in ROUGE-L. Despite that applying repeat-input mechanism alone does not offer benefit, combining these two strategies together further achieves the best performance. Note that these methods do not require any additional parameters.
> 
> Unfortunately, even some of the attentional hierarchical decoders achieve the best results in the generating hierarchies (Table TABREF18 ). Mostly, the additional attention mechanisms are not capable of bringing benefit for model performance. The reason may be that the decoding process is designed for gradually importing words in the specific set of linguistic patterns to the output sequence, each decoder layer is responsible of copying the output tokens from the previous layer and insert new words into the sequence precisely. Because of this nature, a decoder needs explicit information of the structure of a sentence rather than implicit high-level latent information. For instance, when a decoder is trying to insert some Verb words into the output sequence, knowing the position of subject and object would be very helpful.
> 
> The above results show that among these six different generating hierarchy, the generating order: (1) verbs INLINEFORM0 (2) nouns, proper

### Relevance

Label: 

## Record 0119

Paper: Investigating Linguistic Pattern Ordering in Hierarchical Natural Language Generation

### Question

> What evaluation metrics are used?

### Passage

> to insert some Verb words into the output sequence, knowing the position of subject and object would be very helpful.
> 
> The above results show that among these six different generating hierarchy, the generating order: (1) verbs INLINEFORM0 (2) nouns, proper nouns, and pronouns INLINEFORM1 (3) adjectives and adverbs INLINEFORM2 (4) the other POS tags yields the worst performance. Table TABREF23 shows that the gap of average length of target sequences between the first and the second decoder layer is the largest among all the hierarchies; in average, the second decoder needs to insert up to 8 words into the sequence based on 3.62 words from the first decoder layer in this generation process, which is absolutely difficult. The essence of the hierarchical design is to separate the job of the decoder into several phases; if the job of each phase is balanced, it is intuitive that it is more suitable for applying curriculum learning and improve the model performance.
> 
> The model performance is also related to linguistic structures of sentences: the fifth and the sixth generating hierarchies in Table TABREF13 have very similar trends, where the length of target sentences of each decoder layer is almost identical as shown in Table TABREF23 . However, the model performance differs a lot. An adverb word could be used to modify anything but nouns and pronouns, which means that the number of adverbs used for modifying verbs would be a factor to determine the generating order as well. In our cases, almost all adverbs in the dataset are used to describe adjectives, indicating that generating verbs before inserting adverbs to sequences may not provide enough useful information; instead, it would possibly obstruct the model learning. We can also find that in all experiments, inserting adverbs before verbs would be better.
> 
> In summary, the concept of the hierarchical decoder is simple and useful, separating a difficult job to many phases is demonstrated to be a promising direction and not limited to a specific generating hierarchy. Furthermore, the generating linguistic orders should be determined based on the dataset, and the important factors include the distribution over length of subsequences and the linguistic nature of the dataset for designing a proper

### Relevance

Label: 

## Record 0120

Paper: Investigating Linguistic Pattern Ordering in Hierarchical Natural Language Generation

### Question

> What evaluation metrics are used?

### Passage

> The objective of the proposed model is to optimize the conditional probability INLINEFORM0 , so that the difference between the predicted distribution and the target distribution, INLINEFORM1 , can be minimized: DISPLAYFORM0
> 
> where INLINEFORM0 is the number of samples and the labels INLINEFORM1 are the word labels. Each decoder in the hierarchical NLG is trained based on curriculum learning with the objective.

### Relevance

Label: 

## Record 0121

Paper: Towards Multimodal Emotion Recognition in German Speech Events in Cars using Transfer Learning

### Question

> What is the baseline method for the task?

### Passage

> A common approach to encode emotions for facial expressions is the facial action coding system FACS BIBREF9, BIBREF10, BIBREF11. As the reliability and reproducability of findings with this method have been critically discussed BIBREF12, the trend has increasingly shifted to perform the recognition directly on images and videos, especially with deep learning. For instance, jung2015joint developed a model which considers temporal geometry features and temporal appearance features from image sequences. kim2016hierarchical propose an ensemble of convolutional neural networks which outperforms isolated networks.
> 
> In the automotive domain, FACS is still popular. Ma2017 use support vector machines to distinguish happy, bothered, confused, and concentrated based on data from a natural driving environment. They found that bothered and confused are difficult to distinguish, while happy and concentrated are well identified. Aiming to reduce computational cost, Tews2011 apply a simple feature extraction using four dots in the face defining three facial areas. They analyze the variance of the three facial areas for the recognition of happy, anger and neutral. Ihme2018 aim at detecting frustration in a simulator environment. They induce the emotion with specific scenarios and a demanding secondary task and are able to associate specific face movements according to FACS. Paschero2012 use OpenCV (https://opencv.org/) to detect the eyes and the mouth region and track facial movements. They simulate different lightning conditions and apply a multilayer perceptron for the classification task of Ekman's set of fundamental emotions.
> 
> Overall, we found that studies using facial features usually focus on continuous driver monitoring, often in driver-only scenarios. In contrast, our work investigates the potential of emotion recognition during speech interactions.

### Relevance

Label: 

## Record 0122

Paper: Towards Multimodal Emotion Recognition in German Speech Events in Cars using Transfer Learning

### Question

> What is the baseline method for the task?

### Passage

> the speech modality is increasingly being used in cars due to its potential to limit distraction. It has been shown that adapting the in-car speech interaction system according to the drivers' emotional state can help to enhance security, performance as well as the overall driving experience BIBREF6, BIBREF7.
> 
> With this paper, we investigate how each of the three considered modalitites, namely facial expressions, utterances of a driver as an audio signal, and transcribed text contributes to the task of emotion recognition in in-car speech interactions. We focus on the five emotions of joy, insecurity, annoyance, relaxation, and boredom since terms corresponding to so-called fundamental emotions like fear have been shown to be associated to too strong emotional states than being appropriate for the in-car context BIBREF8. Our first contribution is the description of the experimental setup for our data collection. Aiming to provoke specific emotions with situations which can occur in real-world driving scenarios and to induce speech interactions, the study was conducted in a driving simulator. Based on the collected data, we provide baseline predictions with off-the-shelf tools for face and speech emotion recognition and compare them to a neural network-based approach for emotion recognition from text. Our second contribution is the introduction of transfer learning to adapt models trained on established out-of-domain corpora to our use case. We work on German language, therefore the transfer consists of a domain and a language transfer.

### Relevance

Label: 

## Record 0123

Paper: Towards Multimodal Emotion Recognition in German Speech Events in Cars using Transfer Learning

### Question

> What is the baseline method for the task?

### Passage

> Table TABREF16 shows the confusion matrices for facial and audio emotion recognition on our complete AMMER data set and Table TABREF17 shows the results per class for each method, including facial and audio data and micro and macro averages. The classification from facial expressions yields a macro-averaged $\text{F}_1$ score of 33 % across the three emotions joy, insecurity, and annoyance (P=0.31, R=0.35). While the classification results for joy are promising (R=43 %, P=57 %), the distinction of insecurity and annoyance from the other classes appears to be more challenging.
> 
> Regarding the audio signal, we observe a macro $\text{F}_1$ score of 29 % (P=42 %, R=22 %). There is a bias towards negative emotions, which results in a small number of detected joy predictions (R=4 %). Insecurity and annoyance are frequently confused.

### Relevance

Label: 

## Record 0124

Paper: Towards Multimodal Emotion Recognition in German Speech Events in Cars using Transfer Learning

### Question

> What is the baseline method for the task?

### Passage

> We first set a baseline by validating our models on established corpora. We train the baseline model on 60 % of each data set listed in Table TABREF12 and evaluate that model with 40 % of the data from the same domain (results shown in the column “In-Domain” in Table TABREF19). Excluding AMMER, we achieve an average micro $\text{F}_1$ of 68 %, with best results of F$_1$=73 % on TEC. The model trained on our AMMER corpus achieves an F1 score of 57%. This is most probably due to the small size of this data set and the class bias towards joy, which makes up more than half of the data set. These results are mostly in line with Bostan2018.

### Relevance

Label: 

## Record 0125

Paper: Towards Multimodal Emotion Recognition in German Speech Events in Cars using Transfer Learning

### Question

> What is the baseline method for the task?

### Passage

> We described the creation of the multimodal AMMER data with emotional speech interactions between a driver and both a virtual agent and a co-driver. We analyzed the modalities of facial expressions, acoustics, and transcribed utterances regarding their potential for emotion recognition during in-car speech interactions. We applied off-the-shelf emotion recognition tools for facial expressions and acoustics. For transcribed text, we developed a neural network-based classifier with transfer learning exploiting existing annotated corpora. We find that analyzing transcribed utterances is most promising for classification of the three emotional states of joy, annoyance and insecurity.
> 
> Our results for facial expressions indicate that there is potential for the classification of joy, however, the states of annoyance and insecurity are not well recognized. Future work needs to investigate more sophisticated approaches to map frame predictions to sequence predictions. Furthermore, movements of the mouth region during speech interactions might negatively influence the classification from facial expressions. Therefore, the question remains how facial expressions can best contribute to multimodal detection in speech interactions.
> 
> Regarding the classification from the acoustic signal, the application of off-the-shelf classifiers without further adjustments seems to be challenging. We find a strong bias towards negative emotional states for our experimental setting. For instance, the personalization of the recognition algorithm (e. g., mean and standard deviation normalization) could help to adapt the classification for specific speakers and thus to reduce this bias. Further, the acoustic environment in the vehicle interior has special properties and the recognition software might need further adaptations.
> 
> Our transfer learning-based text classifier shows considerably better results. This is a substantial result in its own, as only one previous method for transfer learning in emotion recognition has been proposed, in which a sentiment/emotion specific source for labels in pre-training has been used, to the best of our knowledge BIBREF29. Other applications of transfer learning from general language models include BIBREF41, BIBREF42. Our approach is substantially different, not being trained on a huge amount of noisy data, but on smaller out-of-domain sets of higher quality. This result suggests that emotion classification systems which work across domains can be developed with reasonable effort.
> 
> For a productive application of emotion detection in the context of speech events we

### Relevance

Label: 

## Record 0126

Paper: Dataset and Neural Recurrent Sequence Labeling Model for Open-Domain Factoid Question Answering

### Question

> What was the inter-annotator agreement?

### Passage

> The three-layer evidence LSTMs processes evidence INLINEFORM0 INLINEFORM1 to produce “features” for the CRF layer.
> 
> The first LSTM layer takes evidence INLINEFORM0 , question representation INLINEFORM1 and optional features as input. We find the following two simple common word indicator features are effective:
> 
> Question-Evidence common word feature (q-e.comm): for each word in the evidence, the feature has value 1 when the word also occurs in the question, otherwise 0. The intuition is that words occurring in questions tend not to be part of the answers for factoid questions.
> 
> Evidence-Evidence common word feature (e-e.comm): for each word in the evidence, the feature has value 1 when the word occurs in another evidence, otherwise 0. The intuition is that words shared by two or more evidences are more likely to be part of the answers.
> 
> Although counterintuitive, we found non-binary e-e.comm feature values does not work well. Because the more evidences we considered, the more words tend to get non-zero feature values, and the less discriminative the feature is.
> 
> The second LSTM layer stacks on top of the first LSTM layer, but processes its output in a reverse order. The third LSTM layer stacks upon the first and second LSTM layers with cross layer links, and its output serves as features for CRF layer.
> 
> Formally, the computations are defined as follows DISPLAYFORM0
> 
> where INLINEFORM0 and INLINEFORM1 are one-hot feature vectors, INLINEFORM2 and INLINEFORM3 are embeddings for the features, and INLINEFORM4 and INLINEFORM5 are the feature embedding dimensions. Note that we use the same word embedding matrix INLINEFORM6 as in question LSTM.

### Relevance

Label: 

## Record 0127

Paper: Dataset and Neural Recurrent Sequence Labeling Model for Open-Domain Factoid Question Answering

### Question

> What was the inter-annotator agreement?

### Passage

> As stated in Section SECREF34 , the word embedding INLINEFORM0 is initialized with LM embedding and kept fixed in training. We evaluate different initialization and optimization methods in this section. The evaluation results are shown in Table TABREF40 . The second row shows the results when the embedding is optimized jointly during training. The performance drops significantly. Detailed analysis reveals that the trainable embedding enlarge trainable parameter number and the model gets over fitting easily. The model acts like a context independent entity tagger to some extend, which is not desired. For example, the model will try to find any location name in the evidence when the word “在哪 (where)” occurs in the question. In contrary, pre-trained fixed embedding forces the model to pay more attention to the latent syntactic regularities. And it also carries basic priors such as “梨 (pear)” is fruit and “李世石 (Lee Sedol)” is a person, thus the model will generalize better to test data with fixed embedding. The third row shows the result when the embedding is randomly initialized and jointly optimized. The performance drops significantly further, suggesting that pre-trained embedding indeed carries meaningful priors.

### Relevance

Label: 

## Record 0128

Paper: Dataset and Neural Recurrent Sequence Labeling Model for Open-Domain Factoid Question Answering

### Question

> What was the inter-annotator agreement?

### Passage

> Figure FIGREF4 shows the structure of our model. The model consists of three components: (1) question LSTM for computing question representation; (2) evidence LSTMs for evidence analysis; and (3) a CRF layer for sequence labeling. The question LSTM in a form of a single layer LSTM equipped with a single time attention takes the question as input and generates the question representation INLINEFORM0 . The three-layer evidence LSTMs takes the evidence, question representation INLINEFORM1 and optional features as input and produces “features” for the CRF layer. The CRF layer takes the “features” as input and produces the label sequence. The details will be given in the following sections.

### Relevance

Label: 

## Record 0129

Paper: Dataset and Neural Recurrent Sequence Labeling Model for Open-Domain Factoid Question Answering

### Question

> What was the inter-annotator agreement?

### Passage

> As shown in Table TABREF41 , both the q-e.comm and e-e.comm features are effective, and the q-e.comm feature contributes more to the overall performance. The reason is that the interaction between question and evidence is limited and q-e.comm feature with value 1, i.e. the corresponding word also occurs in the question, is a strong indication that the word may not be part of the answer.

### Relevance

Label: 

## Record 0130

Paper: Dataset and Neural Recurrent Sequence Labeling Model for Open-Domain Factoid Question Answering

### Question

> What was the inter-annotator agreement?

### Passage

> If not specified, the following hyper-parameters will be used in the reset of this section: LSTM layer width INLINEFORM0 (Section SECREF7 ), word embedding dimension INLINEFORM1 (Section SECREF9 ), feature embedding dimension INLINEFORM2 (Section SECREF9 ). The word embeddings are initialized with pre-trained embeddings using a 5-gram neural language model BIBREF25 and is fixed during training.
> 
> We will show that injecting noise data is important for improving performance on retrieved evidence setting in Section SECREF37 . In the following experiments, 20% of the training evidences will be negative ones randomly selected on the fly, of which 25% are annotated negative evidences and 75% are retrieved trivial negative evidences (Section SECREF5 ). The percentages are determined empirically. Intuitively, we provide the noise data to teach the model learning to recognize unreliable evidence.
> 
> For each evidence, we will randomly sample another evidence from the rest evidences of the question and compare them to compute the e-e.comm feature (Section SECREF14 ). We will develop more powerful models to process multiple evidences in a more principle way in the future.
> 
> As the answer for each question in our WebQA dataset only involves one entity (Section SECREF5 ), we distinguish label Os before and after the first B in the label sequence explicitly to discourage our model to produce multiple answers for a question. For example, the golden labels for the example evidence in Figure FIGREF3 will became “Einstein/O1 married/O1 his/O1 first/O1 wife/O1 Mileva/B Marić/I in/O2 1903/O2”, where we use “O1” and “O2” to denote label Os before and after the first B . “Fuzzy matching” is also used for computing golden standard labels for training set.
> 
> For each setting, we will run three trials with different random seeds and report the average performance in the following sections.

### Relevance

Label: 

## Record 0131

Paper: Attentional Encoder Network for Targeted Sentiment Classification

### Question

> Do they use multi-attention heads?

### Passage

> The research approach of the targeted sentiment classification task including traditional machine learning methods and neural networks methods.
> 
> Traditional machine learning methods, including rule-based methods BIBREF9 and statistic-based methods BIBREF10 , mainly focus on extracting a set of features like sentiment lexicons features and bag-of-words features to train a sentiment classifier BIBREF11 . The performance of these methods highly depends on the effectiveness of the feature engineering works, which are labor intensive.
> 
> In recent years, neural network methods are getting more and more attention as they do not need handcrafted features and can encode sentences with low-dimensional word vectors where rich semantic information stained. In order to incorporate target words into a model, Tang et al. tang2016effective propose TD-LSTM to extend LSTM by using two single-directional LSTM to model the left context and right context of the target word respectively. Tang et al. tang2016aspect design MemNet which consists of a multi-hop attention mechanism with an external memory to capture the importance of each context word concerning the given target. Multiple attention is paid to the memory represented by word embeddings to build higher semantic information. Wang et al. wang2016attention propose ATAE-LSTM which concatenates target embeddings with word representations and let targets participate in computing attention weights. Chen et al. chen2017recurrent propose RAM which adopts multiple-attention mechanism on the memory built with bidirectional LSTM and nonlinearly combines the attention results with gated recurrent units (GRUs). Ma et al. ma2017interactive propose IAN which learns the representations of the target and context with two attention networks interactively.

### Relevance

Label: 

## Record 0132

Paper: Attentional Encoder Network for Targeted Sentiment Classification

### Question

> Do they use multi-attention heads?

### Passage

> The attentional encoder layer is a parallelizable and interactive alternative of LSTM and is applied to compute the hidden states of the input embeddings. This layer consists of two submodules: the Multi-Head Attention (MHA) and the Point-wise Convolution Transformation (PCT).
> 
> Multi-Head Attention (MHA) is the attention that can perform multiple attention function in parallel. Different from Transformer BIBREF13 , we use Intra-MHA for introspective context words modeling and Inter-MHA for context-perceptive target words modeling, which is more lightweight and target is modeled according to a given context.
> 
> An attention function maps a key sequence INLINEFORM0 and a query sequence INLINEFORM1 to an output sequence INLINEFORM2 : DISPLAYFORM0
> 
> where INLINEFORM0 denotes the alignment function which learns the semantic relevance between INLINEFORM1 and INLINEFORM2 : DISPLAYFORM0
> 
> where INLINEFORM0 are learnable weights.
> 
> MHA can learn n_head different scores in parallel child spaces and is very powerful for alignments. The INLINEFORM0 outputs are concatenated and projected to the specified hidden dimension INLINEFORM1 , namely, DISPLAYFORM0
> 
> where “ INLINEFORM0 ” denotes vector concatenation, INLINEFORM1 , INLINEFORM2 is the output of the INLINEFORM3 -th head attention and INLINEFORM4 .
> 
> Intra-MHA, or multi-head self-attention, is a special situation for typical attention mechanism that INLINEFORM0 . Given a context embedding INLINEFORM1 , we can get the introspective context representation INLINEFORM2 by: DISPLAYFORM0
> 
> The learned context representation INLINEFORM0 is aware of long-term dependencies.
> 
> Inter-MHA is the generally used form of attention mechanism that INLINEFORM0 is different from INLINEFORM1 . Given a context embedding INLINEFORM2 and a target embedding INLINEFORM3 , we can get the context-perceptive target representation INLINEFORM4 by: DISPLAYFORM0
> 
> After this interactive procedure, each given target word INLINEFORM0 will have a composed representation selected from context embeddings INLINEFORM1 . Then we get the context-perceptive target words modeling INLINEFORM2 .
> 
> A Point-wise Convolution T ransformation (PCT) can transform contextual information gathered by the MHA. Point-wise means that the kernel sizes are 1 and the same transformation is applied to every single token belonging to the input. Formally, given a input sequence INLINEFORM0 , PCT is defined as: DISPLAYFORM0
> 
> where INLINEFORM0 stands for the ELU activation, INLINEFORM1 is the convolution operator, INLINEFORM2 and INLINEFORM3 are the learnable weights of the two convolutional kernels, INLINEFORM4 and

### Relevance

Label: 

## Record 0133

Paper: Attentional Encoder Network for Targeted Sentiment Classification

### Question

> Do they use multi-attention heads?

### Passage

> After we obtain the introspective context representation INLINEFORM0 and the context-perceptive target representation INLINEFORM1 , we employ another MHA to obtain the target-specific context representation INLINEFORM2 by: DISPLAYFORM0
> 
> The multi-head attention function here also has its independent parameters.

### Relevance

Label: 

## Record 0134

Paper: Attentional Encoder Network for Targeted Sentiment Classification

### Question

> Do they use multi-attention heads?

### Passage

> Targeted sentiment classification is a fine-grained sentiment analysis task, which aims at determining the sentiment polarities (e.g., negative, neutral, or positive) of a sentence over “opinion targets” that explicitly appear in the sentence. For example, given a sentence “I hated their service, but their food was great”, the sentiment polarities for the target “service” and “food” are negative and positive respectively. A target is usually an entity or an entity aspect.
> 
> In recent years, neural network models are designed to automatically learn useful low-dimensional representations from targets and contexts and obtain promising results BIBREF0 , BIBREF1 . However, these neural network models are still in infancy to deal with the fine-grained targeted sentiment classification task.
> 
> Attention mechanism, which has been successfully used in machine translation BIBREF2 , is incorporated to enforce the model to pay more attention to context words with closer semantic relations with the target. There are already some studies use attention to generate target-specific sentence representations BIBREF3 , BIBREF4 , BIBREF5 or to transform sentence representations according to target words BIBREF6 . However, these studies depend on complex recurrent neural networks (RNNs) as sequence encoder to compute hidden semantics of texts.
> 
> The first problem with previous works is that the modeling of text relies on RNNs. RNNs, such as LSTM, are very expressive, but they are hard to parallelize and backpropagation through time (BPTT) requires large amounts of memory and computation. Moreover, essentially every training algorithm of RNN is the truncated BPTT, which affects the model's ability to capture dependencies over longer time scales BIBREF7 . Although LSTM can alleviate the vanishing gradient problem to a certain extent and thus maintain long distance information, this usually requires a large amount of training data. Another problem that previous studies ignore is the label unreliability issue, since neutral sentiment is a fuzzy sentimental state and brings difficulty for model learning. As far as we know, we are the first to raise the label unreliability issue in the targeted sentiment classification task.
> 
> This paper propose an attention based model to solve the problems above. Specifically, our model eschews recurrence and employs attention as a competitive alternative to draw the introspective and interactive semantics between target

### Relevance

Label: 

## Record 0135

Paper: Attentional Encoder Network for Targeted Sentiment Classification

### Question

> Do they use multi-attention heads?

### Passage

> In order to comprehensively evaluate and analysis the performance of AEN-GloVe, we list 7 baseline models and design 4 ablations of AEN-GloVe. We also design a basic BERT-based model to evaluate the performance of AEN-BERT.
> 
> Non-RNN based baselines:
> 
> INLINEFORM0 Feature-based SVM BIBREF18 is a traditional support vector machine based model with extensive feature engineering.
> 
> INLINEFORM0 Rec-NN BIBREF0 firstly uses rules to transform the dependency tree and put the opinion target at the root, and then learns the sentence representation toward target via semantic composition using Recursive NNs.
> 
> INLINEFORM0 MemNet BIBREF19 uses multi-hops of attention layers on the context word embeddings for sentence representation to explicitly captures the importance of each context word.
> 
> RNN based baselines:
> 
> INLINEFORM0 TD-LSTM BIBREF1 extends LSTM by using two LSTM networks to model the left context with target and the right context with target respectively. The left and right target-dependent representations are concatenated for predicting the sentiment polarity of the target.
> 
> INLINEFORM0 ATAE-LSTM BIBREF3 strengthens the effect of target embeddings, which appends the target embeddings with each word embeddings and use LSTM with attention to get the final representation for classification.
> 
> INLINEFORM0 IAN BIBREF4 learns the representations of the target and context with two LSTMs and attentions interactively, which generates the representations for targets and contexts with respect to each other.
> 
> INLINEFORM0 RAM BIBREF5 strengthens MemNet by representing memory with bidirectional LSTM and using a gated recurrent unit network to combine the multiple attention outputs for sentence representation.
> 
> AEN-GloVe ablations:
> 
> INLINEFORM0 AEN-GloVe w/o PCT ablates PCT module.
> 
> INLINEFORM0 AEN-GloVe w/o MHA ablates MHA module.
> 
> INLINEFORM0 AEN-GloVe w/o LSR ablates label smoothing regularization.
> 
> INLINEFORM0 AEN-GloVe-BiLSTM replaces the attentional encoder layer with two bidirectional LSTM.
> 
> Basic BERT-based model:
> 
> INLINEFORM0 BERT-SPC feeds sequence “[CLS] + context + [SEP] + target + [SEP]” into the basic BERT model for sentence pair classification task.

### Relevance

Label: 

## Record 0136

Paper: Named Entity Recognition for Nepali Language

### Question

> Which machine learning models do they explore?

### Passage

> Named Entity Recognition (NER) is a foremost NLP task to label each atomic elements of a sentence into specific categories like "PERSON", "LOCATION", "ORGANIZATION" and othersBIBREF0. There has been an extensive NER research on English, German, Dutch and Spanish language BIBREF1, BIBREF2, BIBREF3, BIBREF4, BIBREF5, and notable research on low resource South Asian languages like HindiBIBREF6, IndonesianBIBREF7 and other Indian languages (Kannada, Malayalam, Tamil and Telugu)BIBREF8. However, there has been no study on developing neural NER for Nepali language. In this paper, we propose a neural based Nepali NER using latest state-of-the-art architecture based on grapheme-level which doesn't require any hand-crafted features and no data pre-processing.
> 
> Recent neural architecture like BIBREF1 is used to relax the need to hand-craft the features and need to use part-of-speech tag to determine the category of the entity. However, this architecture have been studied for languages like English, and German and not been applied to languages like Nepali which is a low resource language i.e limited data set to train the model. Traditional methods like Hidden Markov Model (HMM) with rule based approachesBIBREF9,BIBREF10, and Support Vector Machine (SVM) with manual feature-engineeringBIBREF11 have been applied but they perform poor compared to neural. However, there has been no research in Nepali NER using neural network. Therefore, we created the named entity annotated dataset partly with the help of Dataturk to train a neural model. The texts used for this dataset are collected from various daily news sources from Nepal around the year 2015-2016.
> 
> Following are our contributions:
> 
> We present a novel Named Entity Recognizer (NER) for Nepali language. To best of our knowledge we are the first to propose neural based Nepali NER.
> 
> As there are not good quality dataset to train NER we release a dataset to support future research
> 
> We perform empirical evaluation of our model with state-of-the-art models with relative improvement of upto 10%
> 
> In this paper, we present works similar to ours in Section SECREF2. We describe our approach and dataset statistics in Section SECREF3 and SECREF4, followed by our experiments, evaluation and discussion in Section SECREF5, SECREF6, and SECREF7. We conclude with our observations in Section SECREF8.
> 
> To facilitate further research our code and dataset will

### Relevance

Label: 

## Record 0137

Paper: Named Entity Recognition for Nepali Language

### Question

> Which machine learning models do they explore?

### Passage

> There has been a handful of research on Nepali NER task based on approaches like Support Vector Machine and gazetteer listBIBREF11 and Hidden Markov Model and gazetteer listBIBREF9,BIBREF10.
> 
> BIBREF11 uses SVM along with features like first word, word length, digit features and gazetteer (person, organization, location, middle name, verb, designation and others). It uses one vs rest classification model to classify each word into different entity classes. However, it does not the take context word into account while training the model. Similarly, BIBREF9 and BIBREF10 uses Hidden Markov Model with n-gram technique for extracting POS-tags. POS-tags with common noun, proper noun or combination of both are combined together, then uses gazetteer list as look-up table to identify the named entities.
> 
> Researchers have shown that the neural networks like CNNBIBREF12, RNNBIBREF13, LSTMBIBREF14, GRUBIBREF15 can capture the semantic knowledge of language better with the help of pre-trained embbeddings like word2vecBIBREF16, gloveBIBREF17 or fasttextBIBREF18.
> 
> Similar approaches has been applied to many South Asian languages like HindiBIBREF6, IndonesianBIBREF7, BengaliBIBREF19 and In this paper, we present the neural network architecture for NER task in Nepali language, which doesn't require any manual feature engineering nor any data pre-processing during training. First we are comparing BiLSTMBIBREF14, BiLSTM+CNNBIBREF20, BiLSTM+CRFBIBREF1, BiLSTM+CNN+CRFBIBREF2 models with CNN modelBIBREF0 and Stanford CRF modelBIBREF21. Secondly, we show the comparison between models trained on general word embeddings, word embedding + character-level embedding, word embedding + part-of-speech(POS) one-hot encoding and word embedding + grapheme clustered or sub-word embeddingBIBREF22. The experiments were performed on the dataset that we created and on the dataset received from ILPRL lab. Our extensive study shows that augmenting word embedding with character or grapheme-level representation and POS one-hot encoding vector yields better results compared to using general word embedding alone.

### Relevance

Label: 

## Record 0138

Paper: Named Entity Recognition for Nepali Language

### Question

> Which machine learning models do they explore?

### Passage

> We ran our experiment looking for the best hyper-parameters by changing learning rate from (0,1, 0.01, 0.001, 0.0001), weight decay from [$10^{-1}$, $10^{-2}$, $10^{-3}$, $10^{-4}$, $10^{-5}$, $10^{-6}$, $10^{-7}$], batch size from [1, 2, 4, 8, 16, 32, 64, 128], hidden size from [8, 16, 32, 64, 128, 256, 512 1024]. Table TABREF30 shows all other hyper-parameter used in our experiment for both of the dataset.

### Relevance

Label: 

## Record 0139

Paper: Named Entity Recognition for Nepali Language

### Question

> Which machine learning models do they explore?

### Passage

> In this section, we present the details regarding evaluation and comparison of our models with other baselines.
> 
> Table TABREF25 shows the study of various embeddings and comparison among each other in OurNepali dataset. Here, raw dataset represents such dataset where post-positions are not lemmatized. We can observe that pre-trained embeddings significantly improves the score compared to randomly initialized embedding. We can deduce that Skip Gram models perform better compared CBOW models for word2vec and fasttext. Here, fastText_Pretrained represents the embedding readily available in fastText website, while other embeddings are trained on the Nepali National Corpus as mentioned in sub-section SECREF11. From this table TABREF25, we can clearly observe that model using fastText_Skip Gram embeddings outperforms all other models.
> 
> Table TABREF35 shows the model architecture comparison between all the models experimented. The features used for Stanford CRF classifier are words, letter n-grams of upto length 6, previous word and next word. This model is trained till the current function value is less than $1\mathrm {e}{-2}$. The hyper-parameters of neural network experiments are set as shown in table TABREF30. Since, word embedding of character-level and grapheme-level is random, their scores are near.
> 
> All models are evaluated using CoNLL-2003 evaluation scriptBIBREF25 to calculate entity-wise precision, recall and f1 score.

### Relevance

Label: 

## Record 0140

Paper: Named Entity Recognition for Nepali Language

### Question

> Which machine learning models do they explore?

### Passage

> In this paper, we proposed a novel NER for Nepali language and achieved relative improvement of upto 10% and studies different factors effecting the performance of the NER for Nepali language.
> 
> We also present a neural architecture BiLSTM+CNN(grapheme-level) which turns out to be performing on par with BiLSTM+CNN(character-level) under the same configuration. We believe this will not only help Nepali language but also other languages falling under the umbrellas of Devanagari languages. Our model BiLSTM+CNN(grapheme-level) and BiLSTM+CNN(G)+POS outperforms all other model experimented in OurNepali and ILPRL dataset respectively.
> 
> Since this is the first named entity recognition research in Nepal language using neural network, there are many rooms for improvement. We believe initializing the grapheme-level embedding with fasttext embeddings might help boosting the performance, rather than randomly initializing it. In future, we plan to apply other latest techniques like BERT, ELMo and FLAIR to study its effect on low-resource language like Nepali. We also plan to improve the model using cross-lingual or multi-lingual parameter sharing techniques by jointly training with other Devanagari languages like Hindi and Bengali.
> 
> Finally, we would like to contribute our dataset to Nepali NLP community to move forward the research going on in language understanding domain. We believe there should be special committee to create and maintain such dataset for Nepali NLP and organize various competitions which would elevate the NLP research in Nepal.
> 
> Some of the future works are listed below:
> 
> Proper initialization of grapheme level embedding from fasttext embeddings.
> 
> Apply robust POS-tagger for Nepali dataset
> 
> Lemmatize the OurNepali dataset with robust and efficient lemmatizer
> 
> Improve Nepali language score with cross-lingual learning techniques
> 
> Create more dataset using Wikipedia/Wikidata framework

### Relevance

Label: 

## Record 0141

Paper: Remedying BiLSTM-CNN Deficiency in Modeling Cross-Context for NER.

### Question

> What are the baseline models?

### Passage

> that patterns forming an XOR cannot be modeled by Baseline-BiLSTM-CNN used in all previous work. Cross-BiLSTM-CNN and Att-BiLSTM-CNN are shown to have additive and multiplicative cross-structures respectively to deal with the problem. Section SECREF4 evaluates the approaches on two challenging NER datasets spanning a wide range of domains with complex, noisy, and emerging entities. The cross-structures bring consistent improvements over the prevalently used Baseline-BiLSTM-CNN without additional gazetteers, POS taggers, language-modeling, or multi-task supervision. The improved core module surpasses comparable previous models on OntoNotes 5.0 and WNUT 2017 by 1.4% and 4.6% respectively. Experiments reveal that emerging, complex, confusing, and multi-token entity mentions benefitted much from the cross-structures, and the in-depth entity-chunking analysis finds that the prevalently used Baseline-BiLSTM-CNN is flawed for real-world NER.

### Relevance

Label: 

## Record 0142

Paper: Remedying BiLSTM-CNN Deficiency in Modeling Cross-Context for NER.

### Question

> What are the baseline models?

### Passage

> Named Entity Recognition (NER) is a core task for information extraction. Originally a structured prediction task, NER has since been formulated as a task of sequential token labeling. BiLSTM-CNN uses a CNN to encode each word and then uses bi-directional LSTMs to encode past and future context respectively at each time step. With state-of-the-art empirical results, most regard it as a robust core module for sequence-labeling NER BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4.
> 
> However, each direction of BiLSTM only sees and encodes half of a sequence at each time step. For each token, the forward LSTM only encodes past context; the backward LSTM only encodes future context. For computing sentence representations for tasks such as sentence classification and machine translation, this is not a problem, as only the rightmost hidden state of the forward LSTM and only the leftmost hidden state of the backward LSTM are used, and each of the endpoint hidden states sees and encodes the whole sentence. For computing sentence representations for sequence-labeling tasks such as NER, however, this becomes a limitation, as each token uses its own midpoint hidden states, which do not model the patterns that happen to cross past and future at this specific time step.
> 
> This paper explores two types of cross-structures to help cope with the problem: Cross-BiLSTM-CNN and Att-BiLSTM-CNN. Previous studies have tried to stack multiple LSTMs for sequence-labeling NER BIBREF1. As they follow the trend of stacking forward and backward LSTMs independently, the Baseline-BiLSTM-CNN is only able to learn higher-level representations of past or future per se. Instead, Cross-BiLSTM-CNN, which interleaves every layer of the two directions, models cross-context in an additive manner by learning higher-level representations of the whole context of each token. On the other hand, Att-BiLSTM-CNN models cross-context in a multiplicative manner by capturing the interaction between past and future with a dot-product self-attentive mechanism BIBREF5, BIBREF6.
> 
> Section SECREF3 formulates the three Baseline, Cross, and Att-BiLSTM-CNN models. The section gives a concrete proof that patterns forming an XOR cannot be modeled by Baseline-BiLSTM-CNN used in all previous work. Cross-BiLSTM-CNN and Att-BiLSTM-CNN are shown to have additive and multiplicative cross-structures respectively to deal with the problem. Section SECREF4 evaluates the approaches on two challenging

### Relevance

Label: 

## Record 0143

Paper: Remedying BiLSTM-CNN Deficiency in Modeling Cross-Context for NER.

### Question

> What are the baseline models?

### Passage

> Entity-chunking is a subtask of NER concerned with locating entity mentions and their boundaries without disambiguating their types. For sequence-labeling models, this means correct O, S, B, I, E tagging for each token. In addition to showing that cross-structures achieved superior performance on multi-token entity mentions (Section SECREF18), an ablation study focused on the chunking tags was performed to better understand how it was achieved.
> 
> Table TABREF22 shows the entity-chunking ablation results on OntoNotes 5.0 development set. Both Att and Baseline models were taken without re-training for this subtask. The $HC^{all}$ column lists the performance of Att-BiLSTM-CNN on each chunking tag. Other columns list the performance compared to $HC^{all}$. Columns $H$ to $C^5$ are when the full model is deprived of all other information in testing time by forcefully zeroing all vectors except the one specified by the column header. The figures shown in the table are per-token recalls for each chunking tag, which tells if a part of the model is responsible for signaling the whole model to predict that tag. Colors mark relatively high and low values of interest.
> 
> Firstly, Att appeared to designate the task of scoring I to the attention mechanism: When context vectors $C^{all}$ were left alone, the recall for I tokens only dropped a little (-3.80); When token hidden states $H$ were left alone, the recall for I tokens seriously degraded (-28.18). When $H$ and $C^{all}$ work together, the full Att model was then better at predicting multi-token entity mentions than Baseline.
> 
> Then, breaking context vectors to each attention head reveals that they have worked in cooperation: $C^2$, $C^3$ focused more on scoring E (-36.45, -39.19) than I (-60.56, -50.19), while $C^4$ focused more on scoring B (-12.21) than I (-57.19). It was when information from all these heads were combined was Att able to better identify a token as being Inside a multi-token mention than Baseline.
> 
> Finally, the quantitative ablation analysis of chunking tags in this Section and the qualitative case-study attention visualizations in Section SECREF18 explains each other: $C^2$ and especially $C^3$ tended to focus on looking for immediate preceding mention tokens (the diagonal shifted left in Figure FIGREF24, FIGREF24), enabling them to signal for End and

### Relevance

Label: 

## Record 0144

Paper: Remedying BiLSTM-CNN Deficiency in Modeling Cross-Context for NER.

### Question

> What are the baseline models?

### Passage

> Motivated by the limitation of the conventional Baseline-BiLSTM-CNN for sequence labeling, this paper proposes the use of Cross-BiLSTM-CNN by changing the deep structure in Section SECREF2 to
> 
> As the forward and backward hidden states are interleaved between stacked LSTM layers, Cross-BiLSTM-CNN models cross-context patterns by computing representations of the whole sequence in a feed-forward, additive manner.
> 
> Specifically, for the XOR cases introduced in Section SECREF3, although phrase 1 and phrase 3 still have the same past context for "and" and hence the first layer $\overrightarrow{LSTM}_1$ can only extract the same low-level hidden features $\overrightarrow{H}^1_2$, the second layer $\overrightarrow{LSTM}_2$ considers the whole context $\overrightarrow{H}^1||\overleftarrow{H}^3$ and thus have the ability to extract different high-level hidden features $\overrightarrow{H}^2_2$ for the two phrases.
> 
> As the higher-level LSTMs of Cross-BiLSTM-CNN have interleaved input from forward and backward hidden states down below, their weight parameters double the size of the first-level LSTMs. Nevertheless, the cross formulation provides the modeling capacity absent in previous studies with how many more LSTM layers.

### Relevance

Label: 

## Record 0145

Paper: Remedying BiLSTM-CNN Deficiency in Modeling Cross-Context for NER.

### Question

> What are the baseline models?

### Passage

> Another way to capture the interaction between past and future context per time step is to add a token-level self-attentive mechanism on top of the same BiLSTM formulation introduced in Section SECREF2. Given the hidden features $H$ of a whole sequence, the model projects each hidden state to different subspaces, depending on whether it is used as the query vector to consult other hidden states for each word token, the key vector to compute its dot-similarities with incoming queries, or the value vector to be weighted and actually convey information to the querying token. As different aspects of a task can call for different attention, multiple attention heads running in parallel are used BIBREF19.
> 
> Formally, let $m$ be the number of attention heads and $d_c$ be the subspace dimension. For each head $i\in \lbrace 1..m\rbrace $, the attention weight matrix and context matrix are computed by
> 
> where $W^{qi},W^{ki},W^{vi}\in R^{d_h\times d_c}$ are trainable projection matrices and $\sigma $ performs softmax along the second dimension. Each row of the resulting $\alpha ^1,\alpha ^2,\ldots ,\alpha ^m\in R^{n\times n}$ contains the attention weights of a token to its context, and each row of $C^1,C^2,\ldots ,C^m\in R^{n\times d_c}$ is its context vector.
> 
> For Att-BiLSTM-CNN, the hidden vector and context vectors of each token are considered together for classification:
> 
> where $C^i_t$ is the $t$-th row of $C^i$, and $W_c\in R^{(d_h+md_c)\times d_p}$ is a trainable weight matrix. In all the experiments, $m=5$ and $d_c=\frac{d_h}{5}$, so $W_c\in R^{2d_h\times d_p}$.
> 
> While the BiLSTM formulation stays the same as Baseline-BiLSTM-CNN, the computation of attention weights $\alpha ^i$ and context features $C^i$ models the cross interaction between past and future. To see this, the computation of attention scores can be rewritten as follows.
> 
> With the un-shifted covariance matrix of the projected $\overrightarrow{H}\ ||\ \overleftarrow{H}$, Att-BiLSTM-CNN correlates past and future context for each token in a dot-product, multiplicative manner.
> 
> One advantage of the multi-head self-attentive mechanism is that it only needs to be computed once per sequence, and the matrix computations are highly parallelizable, resulting in little computation time overhead. Moreover, in Section SECREF4, the attention weights provide a better understanding of how the model learns to tackle sequence-labeling NER.

### Relevance

Label: 

## Record 0146

Paper: MIT-QCRI Arabic Dialect Identification System for the 2017 Multi-Genre Broadcast Challenge

### Question

> Which are the four Arabic dialects?

### Passage

> Phoneme feature extraction consists of extracting the phone sequence, and phone duration statistics using four different speech recognizers: Czech, Hungarian, and Russian using narrowband model, and English using a broadband model BIBREF27 . We evaluated the four systems using a Support Vector Machine (SVM). The hyper-parameters for the SVM are distance from the hyperplane (C is 0.01), and penalty l2. We used the training data for training the SVM and the development data for testing. Table TABREF13 shows the results for the four phoneme recognizers. The Hungarian phoneme recognition obtained the best results, so we used it for the final system combination.

### Relevance

Label: 

## Record 0147

Paper: MIT-QCRI Arabic Dialect Identification System for the 2017 Multi-Genre Broadcast Challenge

### Question

> Which are the four Arabic dialects?

### Passage

> Word sequences are extracted using a state-of-the-art Arabic speech-to-text transcription system built as part of the MGB-2 BIBREF28 . The system is a combination of a Time Delayed Neural Network (TDNN), a Long Short-Term Memory Recurrent Neural Network (LSTM) and Bidirectional LSTM acoustic models, followed by 4-gram and Recurrent Neural Network (RNN) language model rescoring. Our system uses a grapheme lexicon during both training and decoding. The acoustic models are trained on 1,200 hours of Arabic broadcast speech. We also perform data augmentation (speed and volume perturbation) which gives us three times the original training data. For more details see the system description paper BIBREF4 . We kept the <UNK> from the ASR system, which indicates out-of-vocabulary (OOV) words, we replaced it with special symbol. Space was inserted between all characters including the word boundaries. An SVM classifier was trained similarly to the one used for the phoneme ASR systems, and we achieved 52% accuracy, 51.2% precision and 51.8% recall. The confusion matrix is different between the phoneme classifier and the character classifier systems, which motivates us to use both of them in the final system combination.

### Relevance

Label: 

## Record 0148

Paper: MIT-QCRI Arabic Dialect Identification System for the 2017 Multi-Genre Broadcast Challenge

### Question

> Which are the four Arabic dialects?

### Passage

> One of the challenges of processing real-world spoken content, such as media broadcasts, is the potential presence of different dialects of a language in the material. Dialect identification can be a useful capability to identify which dialect is being spoken during a recording. Dialect identification can be regarded as a special case of language recognition, requiring an ability to discriminate between different members within the same language family, as opposed to across language families (i.e., for language recognition). The dominant approach, based on i-vector extraction, has proven to be very effective for both language and speaker recognition BIBREF0 . Recently, phonetically aware deep neural models have also been found to be effective in combination with i-vectors BIBREF1 , BIBREF2 , BIBREF3 . Phonetically aware models could be beneficial for dialect identification, since they provide a mechanism to focus attention on small phonetic differences between dialects with predominantly common phonetic inventories.
> 
> Since 2015, the Arabic Multi-Genre Broadcast (MGB) Challenge tasks have provided a valuable resource for researchers interested in processing multi-dialectal Arabic speech. For the ASRU 2017 MGB-3 Challenge, there were two possible tasks. The first task was aimed at developing an automatic speech recognition system for Arabic dialectal speech based on a multi-genre broadcast audio dataset. The second task was aimed at developing an Arabic Dialect Identification (ADI) capability for five major Arabic dialects. This paper reports our experimentation efforts for the ADI task.
> 
> While the MGB-3 Arabic ASR task included seven different genres from the broadcast domain, the ADI task focused solely on broadcast news. Participants were provided high-quality Aljazeera news broadcasts as well as transcriptions generated by a multi-dialect ASR system created from the MGB-2 dataset BIBREF4 . The biggest difference from previous MGB challenges is that only a relatively small development set of in-domain data is provided for adaptation to the test set (i.e., the training data is mismatched with the test data). For the ADI baseline, participants were also provided with i-vector features from the audio dataset, and lexical features from the transcripts. Evaluation software was shared with all participants using baseline features available via Github.
> 
> The evaluation scenario for the MGB-3 ADI task can be viewed as channel and domain

### Relevance

Label: 

## Record 0149

Paper: MIT-QCRI Arabic Dialect Identification System for the 2017 Multi-Genre Broadcast Challenge

### Question

> Which are the four Arabic dialects?

### Passage

> To further distinguish speech from different Arabic dialects, while making speech from the same dialect more similar, we adopted a Siamese neural network architecture BIBREF24 based on an i-vector feature space. The Siamese neural network has two parallel convolutional networks, INLINEFORM0 , that share the same set of weights, INLINEFORM1 , as shown in Figure FIGREF5 (a). Let INLINEFORM2 and INLINEFORM3 be a pair of i-vectors for which we wish to compute a distance. Let INLINEFORM4 be the label for the pair, where INLINEFORM5 = 1 if the i-vectors INLINEFORM6 and INLINEFORM7 belong to same dialect, and INLINEFORM8 otherwise. To optimize the network, we use a Euclidean distance loss function between the label and the cosine distance, INLINEFORM9 , where INLINEFORM10
> 
> For training, i-vector pairs and their corresponding labels can be processed by combinations of i-vectors from the training dataset. The trained convolutional network INLINEFORM0 transforms an i-vector INLINEFORM1 to a low-dimensional subspace that is more robust for distinguishing dialects. A detailed illustration of the convolutional network INLINEFORM2 is shown in Figure FIGREF5 (b). The final transformed i-vector, INLINEFORM3 , is a 200-dimensional vector. No nonlinear activation function was used on the fully connected layer. A cosine distance is used for scoring.

### Relevance

Label: 

## Record 0150

Paper: MIT-QCRI Arabic Dialect Identification System for the 2017 Multi-Genre Broadcast Challenge

### Question

> Which are the four Arabic dialects?

### Passage

> For the MGB-3 ADI task, the challenge organizers provided 13,825 utterances (53.6 hours) for the training (TRN) set, 1,524 utterances (10 hours) for a development (DEV) set, and 1,492 utterances (10.1 hours) for a test (TST) set. Each dataset consisted of five Arabic dialects: Egyptian (EGY), Levantine (LEV), Gulf (GLF), North African (NOR), and Modern Standard Arabic (MSA). Detailed statistics of the ADI dataset can be found in BIBREF23 . Table TABREF3 shows some facts about the evaluation conditions and data properties. Note that the development set is relatively small compared to the training set. However, it is matched with the test set channel domain. Thus, the development set provides valuable information to adapt or compensate the channel (recording) domain mismatch between the train and test sets.

### Relevance

Label: 

## Record 0151

Paper: Satirical News Detection with Semantic Feature Extraction and Game-theoretic Rough Sets

### Question

> What features do they extract?

### Passage

> We repeat the game with the new thresholds until a balanced solution is reached. We first analyzes the pure strategy equilibrium of the game and then check if the stopping criteria are satisfied.
> 
> Game equilibrium. The game solution of pure strategy Nash equilibrium is used to determine possible game outcomes in GTRS. The strategy profile $(s_{i},t_{j})$ is a pure strategy Nash equilibrium, if
> 
> This means that none of players would like to change his strategy or they would loss benefit if deriving from this strategy profile, provided this player has the knowledge of other player's strategy.
> 
> Repetition of games. Assuming that we formulate a game, in which the initial thresholds are $(\alpha , \beta )$, and the equilibrium analysis shows that the thresholds corresponding to the equilibrium are $(\alpha ^{*}, \beta ^{*})$. If the thresholds $(\alpha ^{*}, \beta ^{*})$ do not satisfy the stopping criterion, we will update the initial thresholds in the subsequent games. The initial thresholds of the new game will be set as $(\alpha ^{*}, \beta ^{*})$. If the thresholds $(\alpha ^{*}, \beta ^{*})$ satisfy the stopping criterion, we may stop the repetition of games.
> 
> Stopping criterion. We define the stopping criteria so that the iterations of games can stop at a proper time. In this research, we set the stopping criterion as within the range of thresholds, the increase of one player's payoff is less than the decrease of the other player's payoff.

### Relevance

Label: 

## Record 0152

Paper: Satirical News Detection with Semantic Feature Extraction and Game-theoretic Rough Sets

### Question

> What features do they extract?

### Passage

> Satirical news detection is an important yet challenging NLP task. Many feature based models have been proposed. Burfoot et al. extracted features of headline, profanity, and slang using word relations given by statistical metrics and lexical database BIBREF1. Rubin et al. proposed a SVM based model with five features (absurdity, humor, grammar, negative affect, and punctuation) for fake news document detection BIBREF2. Yang et al. presented linguistic features such as psycholinguistic feature based on dictionary and writing stylistic feature from part-of-speech tags distribution frequency BIBREF17. Shu et al. gave a survey in which a set of feature extraction methods is introduced for fake news on social media BIBREF3. Conroy et al. also uses social network behavior to detect fake news BIBREF18. For satirical sentence classification, Davidov et al. extract patterns using word frequency and punctuation features for tweet sentences and amazon comments BIBREF19. The detection of a certain type of sarcasm which contracts positive sentiment with a negative situation by analyzing the sentence pattern with a bootstrapped learning was also discussed BIBREF20. Although word level statistical features are widely used, with advanced word representations and state-of-the-art part-of-speech tagging and named entity recognition model, we observe that semantic features are more important than word level statistical features to model performance. Thus, we decompose the syntactic tree and use word vectors to more precisely capture the semantic inconsistencies in different structural parts of a satirical news tweet.
> 
> Recently, with the success of deep learning in NLP, many researchers attempted to detect fake news with end-to-end neural nets based approaches. Ruchansky et al. proposed a hybrid deep neural model which processes both text and user information BIBREF5, while Wang et al. proposed a neural network model that takes both text and image data BIBREF6 for detection. Sarkar et al. presented a neural network with attention to both capture sentence level and document level satire BIBREF4. Some research analyzed sarcasm from non-news text. Ghosh and Veale BIBREF21 used both the linguistic context and the psychological context information with a bi-directional LSTM to detect sarcasm in users' tweets. They also published a feedback-based dataset by collecting the responses from the tweets authors for future analysis. While all these works detect

### Relevance

Label: 

## Record 0153

Paper: Satirical News Detection with Semantic Feature Extraction and Game-theoretic Rough Sets

### Question

> What features do they extract?

### Passage

> In this section, we will describe the composition and preprocessing of our dataset and introduce our model in detail. We create our dataset by collecting legitimate and satirical news tweets from different news source accounts. Our model aims to detect whether the content of a news tweet is satirical or legitimate. We first extract the semantic features based on inconsistencies in different structural parts of the tweet sentences, and then use these features to train game-theoretic rough set decision model.

### Relevance

Label: 

## Record 0154

Paper: Satirical News Detection with Semantic Feature Extraction and Game-theoretic Rough Sets

### Question

> What features do they extract?

### Passage

> In this paper, we propose a satirical news detection approach based on extracted semantic features and game-theoretic rough sets. In our mode, the semantic features extraction captures the inconsistency in the different structural parts of the sentences and the GTRS classifier can process the incomplete information based on repetitive learning and the acceptance and rejection thresholds. The experimental results on our created satirical and legitimate news tweets dataset show that our model significantly outperforms Pawlak rough set model and SVM. In particular, we demonstrate our model's ability to interpret satirical news detection from a semantic and information trade-off perspective. Other interesting extensions of our paper may be to use rough set models to extract the linguistic features at document level.

### Relevance

Label: 

## Record 0155

Paper: Satirical News Detection with Semantic Feature Extraction and Game-theoretic Rough Sets

### Question

> What features do they extract?

### Passage

> Even though many satirical news tweets are made based on real persons or events, most of them lack specific entities. Rather, because the news is fabricated, news writers use the words such as “man",“woman",“local man", “area woman",“local family" as subject. However, the inconsistency between named entities and noun phrases often exists in a news satire if a named entity is included. For example, the named entity “Andrew Yang" and the noun phrases “time vortex" show great inconsistency than “President Trump", "Senate Republicans", and “White House" do in the legitimate news “President Trump invites Senate Republicans to the White House to talk about the funding bill." We define such inconsistency as a categorical feature that:
> 
> $S_{N\! E\! R\! N}$ is the cosine similarity of named entities and noun phrases of a certain sentence and $\bar{S}_{N\! E\! R\! N}$ is the mean value of $S_{N\! E\! R\! N}$ in corpus.

### Relevance

Label: 

## Record 0156

Paper: Analysis of Wikipedia-based Corpora for Question Answering

### Question

> How many question types do they find in the datasets analyzed?

### Passage

> This section describes another selection-based QA task, called answer retrieval, that finds the answer context from a larger dataset, the entire Wikipedia. SQuAD provides no mapping of the answer contexts to Wikipedia, whereas WikiQA and SelQA provide mappings; however, their data do not come from the same version of Wikipedia. We propose an automatic way of mapping the answer contexts from all corpora to the same version of Wikipeda so they can be coherently used for answer retrieval.
> 
> Each paragraph in Wikipedia is first indexed by Lucene using {1,2,3}-grams, where the paragraphs are separated by WikiExtractor and segmented by NLP4J (28.7M+ paragraphs are indexed). Each answer sentence from the corpora in Table TABREF3 is then queried to Lucene, and the top-5 ranked paragraphs are retrieved. The cosine similarity between each sentence in these paragraphs and the answer sentence is measured for INLINEFORM0 -grams, say INLINEFORM1 . A weight is assigned to each INLINEFORM2 -gram score, say INLINEFORM3 , and the weighted sum is measured: INLINEFORM4 . The fixed weights of INLINEFORM5 are used for our experiments, which can be improved.
> 
> If there exists a sentence whose INLINEFORM0 , the paragraph consisting of that sentence is considered the silver-standard answer passage. Table TABREF3 shows how robust these silver-standard passages are based on human judgement ( INLINEFORM1 ) and how many passages are collected ( INLINEFORM2 ) for INLINEFORM3 , where the human judgement is performed on 50 random samples for each case. For answer retrieval, a dataset is created by INLINEFORM4 , which gives INLINEFORM5 accuracy and INLINEFORM6 coverage, respectively. Finally, each question is queried to Lucene and the top- INLINEFORM7 paragraphs are retrieved from the entire Wikipedia. If the answer sentence exists within those retrieved paragraphs according to the silver-standard, it is considered correct.
> 
> Finding a paragraph that includes the answer context out of the entire Wikipedia is an extremely difficult task (128.7M). The last row of Table TABREF3 shows results from answer retrieval. Given INLINEFORM0 , SelQA and SQuAD show about 34% and 35% accuracy, which are reasonable. However, WikiQA shows a significantly lower accuracy of 12.47%; this is because the questions in WikiQA is about twice shorter than the questions in the other

### Relevance

Label: 

## Record 0157

Paper: Analysis of Wikipedia-based Corpora for Question Answering

### Question

> How many question types do they find in the datasets analyzed?

### Passage

> Question answering (QA) has been a blooming research field for the last decade. Selection-based QA implies a family of tasks that find answer contexts from large data given questions in natural language. Three tasks have been proposed for selection-based QA. Given a document, answer extraction BIBREF0 , BIBREF1 finds answer phrases whereas answer selection BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 and answer triggering BIBREF6 , BIBREF7 find answer sentences instead, although the presence of the answer context is not assumed within the provided document for answer triggering but it is for the other two tasks. Recently, various QA tasks that are not selection-based have been proposed BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 ; however, selection-based QA remains still important because of its practical value to real applications (e.g., IBM Watson, MIT Start).
> 
> Several datasets have been released for selection-based QA. wang:07a created the QASent dataset consisting of 277 questions, which has been widely used for benchmarking the answer selection task. feng:15a presented InsuranceQA comprising 16K+ questions on insurance contexts. yang:15a introduced WikiQA for answer selection and triggering. jurczyk:16 created SelQA for large real-scale answer triggering. rajpurkar2016squad presented SQuAD for answer extraction and selection as well as for reading comprehension. Finally, morales-EtAl:2016:EMNLP2016 provided InfoboxQA for answer selection.
> 
> These corpora make it possible to evaluate the robustness of statistical question answering learning. Although all of these corpora target on selection-based QA, they are designed for different purposes such that it is important to understand the nature of these corpora so a better use of them can be made. In this paper, we make both intrinsic and extrinsic analyses of four latest corpora based on Wikipedia, WikiQA, SelQA, SQuAD, and InfoboxQA. We first give a thorough intrinsic analysis regarding contextual similarities, question types, and answer categories (Section SECREF2 ). We then map questions in all corpora to the current version of English Wikipedia and benchmark another selection-based QA task, answer retrieval (Section SECREF3 ). Finally, we present an extrinsic analysis through a set of experiments cross-testing these corpora using a convolutional neural network architecture (Section SECREF4 ).

### Relevance

Label: 

## Record 0158

Paper: Analysis of Wikipedia-based Corpora for Question Answering

### Question

> How many question types do they find in the datasets analyzed?

### Passage

> All corpora provide datasets/splits for answer selection, whereas only (WikiQA, SQuAD) and (WikiQA, SelQA) provide datasets for answer extraction and answer triggering, respectively. SQuAD is much larger in size although questions in this corpus are often paraphrased multiple times. On the contrary, SQuAD's average candidates per question ( INLINEFORM0 ) is the smallest because SQuAD extracts answer candidates from paragraphs whereas the others extract them from sections or infoboxes that consist of bigger contexts. Although InfoboxQA is larger than WikiQA or SelQA, the number of token types ( INLINEFORM1 ) in InfoboxQA is smaller than those two, due to the repetitive nature of infoboxes.
> 
> All corpora show similar average answer candidate lengths ( INLINEFORM0 ), except for InfoboxQA where each line in the infobox is considered a candidate. SelQA and SQuAD show similar average question lengths ( INLINEFORM1 ) because of the similarity between their annotation schemes. It is not surprising that WikiQA's average question length is the smallest, considering their questions are taken from search queries. InfoboxQA's average question length is relatively small, due to the restricted information that can be asked from the infoboxes. InfoboxQA and WikiQA show the least question-answer word overlaps over questions and answers ( INLINEFORM2 and INLINEFORM3 in Table TABREF2 ), respectively. In terms of the F1-score for overlapping words ( INLINEFORM4 ), SQuAD gives the least portion of overlaps between question-answer pairs although WikiQA comes very close.
> 
> Fig. FIGREF4 shows the distributions of seven question types grouped deterministically from the lexicons. Although these corpora have been independently developed, a general trend is found, where the what question type dominates, followed by how and who, followed by when and where, and so on.
> 
> Fig. FIGREF6 shows the distributions of answer categories automatically classified by our Convolutional Neural Network model trained on the data distributed by li:02a. Interestingly, each corpus focuses on different categories, Numeric for WikiQA and SelQA, Entity for SQuAD, and Person for InfoboxQA, which gives enough diversities for statistical learning to build robust models.

### Relevance

Label: 

## Record 0159

Paper: Analysis of Wikipedia-based Corpora for Question Answering

### Question

> How many question types do they find in the datasets analyzed?

### Passage

> The results of INLINEFORM0 from the answer retrieval task in Section SECREF13 are used to create the datasets for answer triggering, where about 65% of the questions are not expected to find their answer contexts from the provided paragraphs for SelQA and SQuAD and 87.5% are not expected for WikiQA. Answer triggering is evaluated by the F1 scores as presented in Table TABREF11 , where three corpora are cross validated. The results on WikiQA are pretty low as expected from the poor accuracy on the answer retrieval task. Training on SelQA gives the best models for both WikiQA and SelQA. Training on SQuAD gives the best model for SQuAD although the model trained on SelQA is comparable. Since the answer triggering datasets are about 5 times larger than the answer selection datasets, it is computationally too expensive to combine all data for training. We plan to find a strong machine to perform this experiment in near future.

### Relevance

Label: 

## Record 0160

Paper: Analysis of Wikipedia-based Corpora for Question Answering

### Question

> How many question types do they find in the datasets analyzed?

### Passage

> Four publicly available corpora are selected for our analysis. These corpora are based on Wikipedia, so more comparable than the others, and have already been used for the evaluation of several QA systems.
> 
> WikiQA BIBREF6 comprises questions selected from the Bing search queries, where user click data give the questions and their corresponding Wikipedia articles. The abstracts of these articles are then extracted to create answer candidates. The assumption is made that if many queries lead to the same article, it must contain the answer context; however, this assumption fails for some occasions, which makes this dataset more challenging. Since the existence of answer contexts is not guaranteed in this task, it is called answer triggering instead of answer selection.
> 
> SelQA BIBREF7 is a product of five annotation tasks through crowdsourcing. It consists of about 8K questions where a half of the questions are paraphrased from the other half, aiming to reduce contextual similarities between questions and answers. Each question is associated with a section in Wikipedia where the answer context is guaranteed, and also with five sections selected from the entire Wikipedia where the selection is made by the Lucene search engine. This second dataset does not assume the existence of the answer context, so can be used for the evaluation of answer triggering.
> 
> SQuAD BIBREF12 presents 107K+ crowdsourced questions on 536 Wikipedia articles, where the answer contexts are guaranteed to exist within the provided paragraph. It contains annotation of answer phrases as well as the pointers to the sentences including the answer phrases; thus, it can be used for both answer extraction and selection. This corpus also provides human accuracy on those questions, setting up a reasonable upper bound for machines. To avoid overfitting, the evaluation set is not publicly available although system outputs can be evaluated by their provided script.
> 
> InfoboxQA BIBREF13 gives 15K+ questions based on the infoboxes from 150 articles in Wikipedia. Each question is crowdsourced and associated with an infobox, where each line of the infobox is considered an answer candidate. This corpus emphasizes the gravity of infoboxes, which summary arguably the most commonly asked information about those articles. Although the nature of this corpus is different from the

### Relevance

Label: 

## Record 0161

Paper: Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks

### Question

> What transfer learning tasks are evaluated?

### Passage

> SentEval BIBREF6 is a popular toolkit to evaluate the quality of sentence embeddings. Sentence embeddings are used as features for a logistic regression classifier. The logistic regression classifier is trained on various tasks in a 10-fold cross-validation setup and the prediction accuracy is computed for the test-fold.
> 
> The purpose of SBERT sentence embeddings are not to be used for transfer learning for other tasks. Here, we think fine-tuning BERT as described by devlin2018bert for new tasks is the more suitable method, as it updates all layers of the BERT network. However, SentEval can still give an impression on the quality of our sentence embeddings for various tasks.
> 
> We compare the SBERT sentence embeddings to other sentence embeddings methods on the following seven SentEval transfer tasks:
> 
> MR: Sentiment prediction for movie reviews snippets on a five start scale BIBREF25.
> 
> CR: Sentiment prediction of customer product reviews BIBREF26.
> 
> SUBJ: Subjectivity prediction of sentences from movie reviews and plot summaries BIBREF27.
> 
> MPQA: Phrase level opinion polarity classification from newswire BIBREF28.
> 
> SST: Stanford Sentiment Treebank with binary labels BIBREF29.
> 
> TREC: Fine grained question-type classification from TREC BIBREF30.
> 
> MRPC: Microsoft Research Paraphrase Corpus from parallel news sources BIBREF31.
> 
> The results can be found in Table TABREF15. SBERT is able to achieve the best performance in 5 out of 7 tasks. The average performance increases by about 2 percentage points compared to InferSent as well as the Universal Sentence Encoder. Even though transfer learning is not the purpose of SBERT, it outperforms other state-of-the-art sentence embeddings methods on this task.
> 
> It appears that the sentence embeddings from SBERT capture well sentiment information: We observe large improvements for all sentiment tasks (MR, CR, and SST) from SentEval in comparison to InferSent and Universal Sentence Encoder.
> 
> The only dataset where SBERT is significantly worse than Universal Sentence Encoder is the TREC dataset. Universal Sentence Encoder was pre-trained on question-answering data, which appears to be beneficial for the question-type classification task of the TREC dataset.
> 
> Average BERT embeddings or using the CLS-token output from a BERT network achieved bad results for various STS tasks (Table TABREF6), worse than average GloVe embeddings. However, for SentEval, average BERT embeddings and the BERT CLS-token output achieves decent

### Relevance

Label: 

## Record 0162

Paper: Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks

### Question

> What transfer learning tasks are evaluated?

### Passage

> dataset.
> 
> Average BERT embeddings or using the CLS-token output from a BERT network achieved bad results for various STS tasks (Table TABREF6), worse than average GloVe embeddings. However, for SentEval, average BERT embeddings and the BERT CLS-token output achieves decent results (Table TABREF15), outperforming average GloVe embeddings. The reason for this are the different setups. For the STS tasks, we used cosine-similarity to estimate the similarities between sentence embeddings. Cosine-similarity treats all dimensions equally. In contrast, SentEval fits a logistic regression classifier to the sentence embeddings. This allows that certain dimensions can have higher or lower impact on the classification result.
> 
> We conclude that average BERT embeddings / CLS-token output from BERT return sentence embeddings that are infeasible to be used with cosine-similarity or with Manhatten / Euclidean distance. For transfer learning, they yield slightly worse results than InferSent or Universal Sentence Encoder. However, using the described fine-tuning setup with a siamese network structure on NLI datasets yields sentence embeddings that achieve a new state-of-the-art for the SentEval toolkit.

### Relevance

Label: 

## Record 0163

Paper: Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks

### Question

> What transfer learning tasks are evaluated?

### Passage

> We showed that BERT out-of-the-box maps sentences to a vector space that is rather unsuitable to be used with common similarity measures like cosine-similarity. The performance for seven STS tasks was below the performance of average GloVe embeddings.
> 
> To overcome this shortcoming, we presented Sentence-BERT (SBERT). SBERT fine-tunes BERT in a siamese / triplet network architecture. We evaluated the quality on various common benchmarks, where it could achieve a significant improvement over state-of-the-art sentence embeddings methods. Replacing BERT with RoBERTa did not yield a significant improvement in our experiments.
> 
> SBERT is computationally efficient. On a GPU, it is about 9% faster than InferSent and about 55% faster than Universal Sentence Encoder. SBERT can be used for tasks which are computationally not feasible to be modeled with BERT. For example, clustering of 10,000 sentences with hierarchical clustering requires with BERT about 65 hours, as around 50 Million sentence combinations must be computed. With SBERT, we were able to reduce the effort to about 5 seconds.

### Relevance

Label: 

## Record 0164

Paper: Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks

### Question

> What transfer learning tasks are evaluated?

### Passage

> We have demonstrated strong empirical results for the quality of SBERT sentence embeddings. In this section, we perform an ablation study of different aspects of SBERT in order to get a better understanding of their relative importance.
> 
> We evaluated different pooling strategies (MEAN, MAX, and CLS). For the classification objective function, we evaluate different concatenation methods. For each possible configuration, we train SBERT with 10 different random seeds and average the performances.
> 
> The objective function (classification vs. regression) depends on the annotated dataset. For the classification objective function, we train SBERT-base on the SNLI and the Multi-NLI dataset. For the regression objective function, we train on the training set of the STS benchmark dataset. Performances are measured on the development split of the STS benchmark dataset. Results are shown in Table TABREF23.
> 
> When trained with the classification objective function on NLI data, the pooling strategy has a rather minor impact. The impact of the concatenation mode is much larger. InferSent BIBREF4 and Universal Sentence Encoder BIBREF5 both use $(u, v, |u-v|, u*v)$ as input for a softmax classifier. However, in our architecture, adding the element-wise $u*v$ decreased the performance.
> 
> The most important component is the element-wise difference $|u-v|$. Note, that the concatenation mode is only relevant for training the softmax classifier. At inference, when predicting similarities for the STS benchmark dataset, only the sentence embeddings $u$ and $v$ are used in combination with cosine-similarity. The element-wise difference measures the distance between the dimensions of the two sentence embeddings, ensuring that similar pairs are closer and dissimilar pairs are further apart.
> 
> When trained with the regression objective function, we observe that the pooling strategy has a large impact. There, the MAX strategy perform significantly worse than MEAN or CLS-token strategy. This is in contrast to BIBREF4, who found it beneficial for the BiLSTM-layer of InferSent to use MAX instead of MEAN pooling.

### Relevance

Label: 

## Record 0165

Paper: Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks

### Question

> What transfer learning tasks are evaluated?

### Passage

> We first introduce BERT, then, we discuss state-of-the-art sentence embedding methods.
> 
> BERT BIBREF0 is a pre-trained transformer network BIBREF9, which set for various NLP tasks new state-of-the-art results, including question answering, sentence classification, and sentence-pair regression. The input for BERT for sentence-pair regression consists of the two sentences, separated by a special [SEP] token. Multi-head attention over 12 (base-model) or 24 layers (large-model) is applied and the output is passed to a simple regression function to derive the final label. Using this setup, BERT set a new state-of-the-art performance on the Semantic Textual Semilarity (STS) benchmark BIBREF10. RoBERTa BIBREF1 showed, that the performance of BERT can further improved by small adaptations to the pre-training process. We also tested XLNet BIBREF11, but it led in general to worse results than BERT.
> 
> A large disadvantage of the BERT network structure is that no independent sentence embeddings are computed, which makes it difficult to derive sentence embeddings from BERT. To bypass this limitations, researchers passed single sentences through BERT and then derive a fixed sized vector by either averaging the outputs (similar to average word embeddings) or by using the output of the special CLS token (for example: bertsentenceembeddings1,bertsentenceembeddings2,bertsentenceembeddings3). These two options are also provided by the popular bert-as-a-service-repository. Up to our knowledge, there is so far no evaluation if these methods lead to useful sentence embeddings.
> 
> Sentence embeddings are a well studied area with dozens of proposed methods. Skip-Thought BIBREF12 trains an encoder-decoder architecture to predict the surrounding sentences. InferSent BIBREF4 uses labeled data of the Stanford Natural Language Inference dataset BIBREF13 and the Multi-Genre NLI dataset BIBREF14 to train a siamese BiLSTM network with max-pooling over the output. Conneau et al. showed, that InferSent consistently outperforms unsupervised methods like SkipThought. Universal Sentence Encoder BIBREF5 trains a transformer network and augments unsupervised learning with training on SNLI. hill-etal-2016-learning showed, that the task on which sentence embeddings are trained significantly impacts their quality. Previous work BIBREF4, BIBREF5 found that the SNLI datasets are suitable for training sentence embeddings. yang-2018-learning presented a method to train on conversations from Reddit using siamese DAN and siamese transformer networks, which yielded good results on the STS benchmark dataset.
> 
> polyencoders addresses the run-time

### Relevance

Label: 

## Record 0166

Paper: Queens are Powerful too: Mitigating Gender Bias in Dialogue Generation

### Question

> How does counterfactual data augmentation aim to tackle bias?

### Passage

> We explore both data augmentation and algorithmic methods to mitigate bias in generative Transformer dialogue models. We describe first our modeling setting and then the three proposed techniques for mitigating bias. Using (i) counterfactual data augmentation BIBREF25 to swap gendered words and (ii) additional data collection with crowdworkers, we create a gender-balanced dataset. Further, (iii) we describe a controllable generation method which moderates the male and female gendered words it produces.

### Relevance

Label: 

## Record 0167

Paper: Queens are Powerful too: Mitigating Gender Bias in Dialogue Generation

### Question

> How does counterfactual data augmentation aim to tackle bias?

### Passage

> We analyze gender bias in dialogue and propose a general purpose method for understanding and mitigating bias in character personas and their associated dialogues. We present techniques using data augmentation and controllable generation to reduce gender bias in neural language generation for dialogue. We use the dataset LIGHT as a testbed for this work. By integrating these methods together, our models provide control over how gendered dialogue is and decrease the offensiveness of the generated utterances. Overall, our proposed methodology reduces the effect of bias while maintaining dialogue engagingness.

### Relevance

Label: 

## Record 0168

Paper: Queens are Powerful too: Mitigating Gender Bias in Dialogue Generation

### Question

> How does counterfactual data augmentation aim to tackle bias?

### Passage

> We train generative Transformer models using each of these methods – Counterfactual Data Augmentation that augments with swaps of gendered words (CDA, §SECREF19), adding new dialogues (Positive-Bias Data Collection, §SECREF20), and controllable generation to control the quantity of gendered words (CT, §SECREF24) – and finally combine all of these methods together (ALL).

### Relevance

Label: 

## Record 0169

Paper: Queens are Powerful too: Mitigating Gender Bias in Dialogue Generation

### Question

> How does counterfactual data augmentation aim to tackle bias?

### Passage

> After analyzing the bias in LIGHT personas, we go on to analyze the bias in dialogues created from those personas and how to quantify it.

### Relevance

Label: 

## Record 0170

Paper: Queens are Powerful too: Mitigating Gender Bias in Dialogue Generation

### Question

> How does counterfactual data augmentation aim to tackle bias?

### Passage

> of male and female genders, although there are many characters that are gender neutral (like “trees") or for which the gender could not be determined. We did not find any explicitly identified non-binary characters. We note that this is a bias in and of itself, and should be addressed in future work. We show that training on gender biased data leads existing generative dialogue models to amplify gender bias further. To offset this, we collect additional in-domain personas and dialogues to balance gender and increase the diversity of personas in the dataset. Next, we combine this approach with Counterfactual Data Augmentation and methods for controllable text generation to mitigate the bias in dialogue generation. Our proposed techniques create models that produce engaging responses with less gender bias.

### Relevance

Label: 

## Record 0171

Paper: To What Extent are Name Variants Used as Named Entities in Turkish Tweets?

### Question

> How many tweets are in the dataset?

### Passage

> Although NER is an NLP topic that has been studied for a long time, currently, the target genre of the related studies has shifted from well-formed texts such as news articles to microblog texts like tweets BIBREF6. Following this scheme (mostly) on English content, NER research on other languages like Turkish has also started to target at tweets BIBREF5, BIBREF2. A named entity-annotated dataset consisting of Turkish tweets is described in BIBREF5 and the results of NER experiments on Turkish tweets are presented in BIBREF2. Interested readers are referred to BIBREF7 which presents a survey of named entity recognition on Turkish, including related work on tweets.
> 
> In this study, we analyze the basic named entities (of type PERSON, LOCATION, and ORGANIZATION, henceforth, PLOs) in the annotated dataset compiled in BIBREF5, with respect to their being well-formed canonical names or name variants. The dataset includes a total of 1.322 named entity annotations, however, 980 of them are PLOs (457 PERSON, 282 LOCATION, and 241 ORGANIZATION names) and are the main focus of this paper. These 980 PLOs were annotated within a total of 670 tweets.
> 
> We have extracted these PLO annotations from the dataset and further annotated them as belonging to one of the following eight name variant categories that we propose. We should note that a particular name can belong to several categories and therefore, there may be multiple category labels assigned to it. However, the number of category labels does not exceed two in our case, i.e., each name is annotated with either one or two labels in the resulting dataset.
> 
> WELL-FORMED: This category comprises those names which are written in their open and canonical form without any distortions, conforming to the capitalization and other writing rules of Turkish. In Turkish, each of the tokens of names are written with their initial letters capitalized. However, those names written all in uppercase are also considered within this category as they cannot be considered as writing errors.
> 
> ABBREVIATION: This category represents those names which are provided as abbreviations. This usually applies to named entities of ORGANIZATION type. But, these abbreviations can include writing errors due capitalization or characters with diacritics, as will be explained below. Hence,

### Relevance

Label: 

## Record 0172

Paper: To What Extent are Name Variants Used as Named Entities in Turkish Tweets?

### Question

> How many tweets are in the dataset?

### Passage

> We have annotated the PLOs in the tweet dataset (already-annotated for named entities as described in BIBREF5) with the name variant category labels of WELL-FORMED, ABBREVIATION, CAPITALIZATION, DIACRITICS, HASHTAG-LIKE, CONTRACTED, HYPOCORISM, and ERROR, as described in the previous subsection. Although there are 980 PLOs in the dataset, since 44 names have two name variant category labels, the total number of name variant annotations is 1,024.
> 
> The percentages of the category labels in the final annotation file are provided as a bar graph in Figure FIGREF9. As indicated in the figure, about 60% of all named entities are well-formed and hence about 40% of them are not in their canonical open form or do not conform to the capitalization/writing errors regarding named entities in Turkish.
> 
> The most common issue is the lack of proper capitalization of names in tweets, revealed with a percentage of 22.56% names annotated with the CAPITALIZATION label. For instance, people write istanbul instead of the correct form İstanbul and ankara instead of Ankara in their tweets.
> 
> The number of names having issues about characters with diacritics is 45, and similarly there are 45 abbreviations (of mostly organization names) in the dataset. As examples of names having issues with diacritics, people use Kutahya istead of the correct form Kütahya, and similarly Besiktas instead of Beşiktaş. Abbreviations in the dataset include national corporations like TRT and SGK, and international organizations like UEFA.
> 
> Instances of the categories of HASHTAG-LIKE and CONTRACTED are observed in 38 and 35 names, respectively. A sample name variant marked with HASHTAG-LIKE is SabriSarıoğlu where this person name should have been written as Sabri Sarıoğlu. A contracted name instance in the dataset is Diyanet which is an organization name with the correct open form of Diyanet İşleri Başkanlığı.
> 
> The instances of HYPOCORISM and ERROR are comparatively low, where 10 instances of hyprocorism and 11 instances of other errors are seen in the dataset. An instance of the former category is Nazlış which is a hypocoristic use of the female person name Nazlı. An instance of the ERROR category is the use of FENEBAHÇE instead of the correct sports club name FENERBAHÇE.
> 
> Overall, this finer-granularity analysis of named entities as name variants

### Relevance

Label: 

## Record 0173

Paper: To What Extent are Name Variants Used as Named Entities in Turkish Tweets?

### Question

> How many tweets are in the dataset?

### Passage

> which amounts to a total of 980 annotations in 670 tweets in Turkish. We further annotate these 980 names with respect to a name variant categorization that we propose and try to present a rough estimate of the extent at which different named entity variants are used as named entities in Turkish tweets. The resulting annotations of named entities as different name variants are also made publicly available for research purposes. We believe that both the analysis described in the paper and the publicly-shared annotations (i.e., a tweet dataset annotated for name variants) will help improve research on NER, name disambiguation, and name linking on Turkish social media posts.
> 
> The rest of the paper is organized as follows: In Section 2, an analysis of the named entities in the publicly-available Turkish tweet dataset with respect to their being name variants or not is presented together with the descriptions of name variant categories. In Section 3, details and samples of the related finer-grained annotations of named entities are described and Section 4 concludes the paper with a summary of main points.

### Relevance

Label: 

## Record 0174

Paper: To What Extent are Name Variants Used as Named Entities in Turkish Tweets?

### Question

> How many tweets are in the dataset?

### Passage

> This paper focuses on named entity variants in Turkish tweets and presents the related analysis results on a common named-entity annotated tweet dataset in Turkish. The named entities of type person, location, and organization names are further categorized into eight proprietary name variant classes and the resulting annotations are made publicly available. The results indicate that about 40% of the considered names deviate from their standard canonical forms in these tweets and the categorizations for these cases can be used by researchers to devise solutions for related NLP problems. These problems include named entity recognition, name disambiguation and linking, and more recently, stance detection.

### Relevance

Label: 

## Record 0175

Paper: To What Extent are Name Variants Used as Named Entities in Turkish Tweets?

### Question

> How many tweets are in the dataset?

### Passage

> Automatic extraction and classification of named entities in natural language texts (i.e., named entity recognition (NER)) is a significant topic of natural language processing (NLP), both as a stand-alone research problem and as a subproblem to facilitate solutions of other related NLP problems. NER has been studied for a long time and in different domains, and there are several survey papers on NER including BIBREF0.
> 
> Conducting NLP research (such as NER) on microblog texts like tweets poses further challenges, due to the particular nature of this text genre. Contractions, writing/grammatical errors, and deliberate distortions of words are common in this informal text genre which is produced with character limitations and published without a formal review process before publication. There are several studies that propose tweet normalization schemes BIBREF1 to alleviate the negative effects of such language use in microblogs, for the other NLP tasks to be performed on the normalized microblogs thereafter. Yet, particularly regarding Turkish content, a related study on NER on Turkish tweets BIBREF2 claims that normalization before the actual NER procedure on tweets may not guarantee improved NER performance.
> 
> Identification of name variants is an important research issue that can help facilitate tasks including named entity linking BIBREF3 and NER, among others. Name variants can appear due to several reasons including the use of abbreviations, contracted forms, nicknames, hypocorism, and capitalization/writing errors BIBREF3. The identification and disambiguation of name variants have been studied in studies such as BIBREF4 and BIBREF3, where resource-based and/or algorithmic solutions are proposed.
> 
> In this paper, we consider name variants from the perspective of a NER application and analyze an existing named entity-annotated tweet dataset in Turkish described in BIBREF5, in order to further annotate the included named entities with respect to a proprietary name variant categorization. The original dataset includes named annotations for eight types: PERSON, LOCATION, ORGANIZATION, DATE, TIME, MONEY, PERCENT, and MISC BIBREF5. However, in this study, we target only at the first three categories which amounts to a total of 980 annotations in 670 tweets in Turkish. We further annotate these 980 names with respect to a name variant categorization that we propose and try to present a rough estimate of the extent at

### Relevance

Label: 

## Record 0176

Paper: Unsupervised Terminological Ontology Learning based on Hierarchical Topic Modeling

### Question

> How do they obtain syntax from raw documents in hrLDA?

### Passage

> The main problem we address in this section is generating terminological ontologies in an unsupervised fashion. The fundamental concept of hrLDA is as follows. When people construct a document, they start with selecting several topics. Then, they choose some noun phrases as subjects for each topic. Next, for each subject they come up with relation triplets to describe this subject or its relationships with other subjects. Finally, they connect the subject phrases and relation triplets to sentences via reasonable grammar. The main topic is normally described with the most important relation triplets. Sentences in one paragraph, especially adjacent sentences, are likely to express the same topic.
> 
> We begin by describing the process of reconstructing LDA. Subsequently, we explain relation extraction from heterogeneous documents. Next, we propose an improved topic partition method over CRP. Finally, we demonstrate how to build topic hierarchies that bind with extracted relation triplets.

### Relevance

Label: 

## Record 0177

Paper: Unsupervised Terminological Ontology Learning based on Hierarchical Topic Modeling

### Question

> How do they obtain syntax from raw documents in hrLDA?

### Passage

> In this paper, we have proposed a completely unsupervised model, hrLDA, for terminological ontology learning. hrLDA is a domain-independent and self-learning model, which means it is very promising for learning ontologies in new domains and thus can save significant time and effort in ontology acquisition.
> 
> We have compared hrLDA with popular topic models to interpret how our algorithm learns meaningful hierarchies. By taking syntax and document structures into consideration, hrLDA is able to extract more descriptive topics. In addition, hrLDA eliminates the restrictions on the fixed topic tree depth and the limited number of topic paths. Furthermore, ACRP allows hrLDA to create more reasonable topics and to converge faster in Gibbs sampling.
> 
> We have also compared hrLDA to several unsupervised ontology learning models and shown that hrLDA can learn applicable terminological ontologies from real world data. Although hrLDA cannot be applied directly in formal reasoning, it is efficient for building knowledge bases for information retrieval and simple question answering. Also, hrLDA is sensitive to the quality of extracted relation triplets. In order to give optimal answers, hrLDA should be embedded in more complex probabilistic modules to identify true facts from extracted ontology rules. Finally, one issue we have not addressed in our current study is capturing pre-knowledge. Although a direct solution would be adding the missing information to the data set, a more advanced approach would be to train topic embeddings to extract hidden semantics.

### Relevance

Label: 

## Record 0178

Paper: Unsupervised Terminological Ontology Learning based on Hierarchical Topic Modeling

### Question

> How do they obtain syntax from raw documents in hrLDA?

### Passage

> topics being on different topic levels. Despite the fact that the single path was changed to multiple paths in some extensions of hLDA - the nested Chinese restaurant franchise processes BIBREF22 and the nested hierarchical Dirichlet Processes BIBREF23 , - this topic path drawing strategy puts words from different domains into one topic when input data are mixed with topics from multiple domains. This means that if a corpus contains documents in four different domains, hLDA is likely to include words from the four domains in every topic (see Figure FIGREF55 ). In light of the various inadequacies discussed above, we propose a relation-based model, hrLDA. hrLDA incorporates semantic topic modeling with relation extraction to integrate syntax and has the capacity to provide comprehensive hierarchies even in corpora containing mixed topics.

### Relevance

Label: 

## Record 0179

Paper: Unsupervised Terminological Ontology Learning based on Hierarchical Topic Modeling

### Question

> How do they obtain syntax from raw documents in hrLDA?

### Passage

> learning. However, these models are deficient in that they still need human supervision to decide the number of topics, and to pick meaningful topic labels usually from a list of unigrams. Among models not using unigrams, LDA-based Global Similarity Hierarchy Learning (LDA+GSHL) BIBREF13 only extracts a subset of relations: “broader" and “related" relations. In addition, the topic hierarchies of KB-LDA BIBREF17 rely on hypernym-hyponym pairs capturing only a subset of hierarchies.
> 
> Considering the shortcomings of the existing methods, the main objectives of applying topic modeling to ontology learning are threefold.
> 
> To achieve the first objective, we extract noun phrases and then propose a sampling method to estimate the number of topics. For the second objective, we use language parsing and relation extraction to learn relations for the noun phrases. Regarding the third objective, we adapt and improve the hierarchical latent Dirichlet allocation (hLDA) model BIBREF19 , BIBREF20 . hLDA is not ideal for ontology learning because it builds topics from unigrams (which are not descriptive enough to serve as entities in ontologies) and the topics may contain words from multiple domains when input data have documents from many domains (see Section SECREF2 and Figure FIGREF55 ). Our model, hrLDA, overcomes these deficiencies. In particular, hrLDA represents topics with noun phrases, uses syntax and document structures such as paragraph indentations and item lists, assigns multiple topic paths for every document, and allows topic trees to grow vertically and horizontally.
> 
> The primary contributions of this work can be specified as follows.
> 
> The rest of this paper is organized into five parts. In Section 2, we provide a brief background of hLDA. In Section 3, we present our hrLDA model and the ontology generation method. In Section 4, we demonstrate empirical results regarding topic hierarchies and generated terminological ontologies. Finally, in Section 5, we present some concluding remarks and discuss avenues for future work and improvements.

### Relevance

Label: 

## Record 0180

Paper: Unsupervised Terminological Ontology Learning based on Hierarchical Topic Modeling

### Question

> How do they obtain syntax from raw documents in hrLDA?

### Passage

> become rapidly high. Figure FIGREF52 highlights the perplexity values of the three models with confidence intervals in the final state. As shown in the two types of experiments, hrLDA has the lowest average perplexities and smallest confidence intervals, followed by phrase_hLDA, and then hLDA.
> 
> Our interpretation is that hLDA and phrase_hLDA tend to assign terms to the largest topic and thus do not guarantee that each topic path contains terms with similar meaning.
> 
> Robustness
> 
> Figure FIGREF55 shows exhaustive hierarchical topic trees extracted from a small text sample with topics from four domains: INLINEFORM0 , INLINEFORM1 INLINEFORM2 , INLINEFORM3 , and INLINEFORM4 . hLDA tends to mix words from different domains into one topic. For instance, words on the first level of the topic tree come from all four domains. This is because the topic path drawing method in existing hLDA-based models takes words in the most important topic of every document and labels them as the main topic of the corpus. In contrast, hrLDA is able to create four big branches for the four domains from the root. Hence, it generates clean topic hierarchies from the corpus.

### Relevance

Label: 

## Record 0181

Paper: Unsupervised Identification of Study Descriptors in Toxicology Research: An Experimental Study

### Question

> What is their binary classifier?

### Passage

> The goal of this experiment was to explore empirically whether our approach truly identifies mentions of the minimum criteria in text. As we did not have any fine-grained annotations that could be used to directly evaluate whether our model identifies the correct sequences, we have used a different methodology. We have utilized the existing 0/1 labels which were available in the database (these were discussed in Section SECREF2 ) to train one binary classifier for each MC. The task of each of the classifiers is to determine whether a publication met the given criteria or not. We have then compared a baseline classifier trained on all full text with three other models:
> 
> The only difference between the four models is which sentences from each document are passed to the classifier for training and testing. The intuition is that a classifier utilizing the correct sentences should outperform both other models.
> 
> To avoid selecting the same sentences across the three models we removed documents which contained less than INLINEFORM0 sentences (Table TABREF17 , row Number of documents shows how many documents satisfied this condition). In all of the experiments presented in this section, the publication full text was tokenized, lower-cased, stemmed, and stop words were removed. All models used a Bernoulli Naïve Bayes classifier (scikit-learn implementation which used a uniform class prior) trained on binary occurrence matrices created using 1-3-grams extracted from the publications, with n-grams appearing in only one document removed. The complete results obtained from leave-one-out cross validation are shown in Table TABREF17 . In all cases we report classification accuracy. In the case of the random-k sentences model the accuracy was averaged over 10 runs of the model.
> 
> We compare the results to two baselines: (1) a baseline obtained by classifying all documents as belonging to the majority class (baseline 1 in Table TABREF17 ) and (2) a baseline obtained using the same setup (features and classification algorithm) as in the case of the top-/random-/bottom-k sentences models but which utilized all full text instead of selected sentences extracted from the text only (baseline 2 in Table TABREF17 ).

### Relevance

Label: 

## Record 0182

Paper: Unsupervised Identification of Study Descriptors in Toxicology Research: An Experimental Study

### Question

> What is their binary classifier?

### Passage

> In this paper we presented a method for unsupervised identification of text segments relevant to specific sought after information being extracted from scientific documents. Our method is entirely unsupervised and only requires the current document itself and the input descriptions instead of corpus linked to this document. The method utilizes short descriptions of the information being extracted from the documents and the ability of word embeddings to capture word context. Consequently, it is domain independent and can potentially be applied to another set of documents and criteria with minimal effort. We have used the method on a corpus of toxicology documents and a set of guideline protocol criteria needed to be extracted from the documents. We have shown the identified text segments are very accurate. Furthermore, a binary classifier trained to identify publications that met the criteria performed better when trained on the candidate sentences than when trained on sentences randomly picked from the text, supporting our intuition that our method is able to accurately identify relevant text segments from full text documents.
> 
> There are a number of things we plan on investigating next. In our initial experiment we have utilized criteria descriptions which were not designed to be used by our model. One possible improvement of our method could be replacing the current descriptions with example sentences taken from the documents containing the sought after information. We also plan on testing our method on an annotated dataset, for example using existing annotated PICO element datasets BIBREF24 .

### Relevance

Label: 

## Record 0183

Paper: Unsupervised Identification of Study Descriptors in Toxicology Research: An Experimental Study

### Question

> What is their binary classifier?

### Passage

> In this section we present studies most similar to our work. We focus on unsupervised methods for information extraction from biomedical texts.
> 
> Many methods for biomedical data annotation and extraction exist which utilize labeled data and supervised learning approaches ( BIBREF12 and BIBREF6 provided a good overview of a number of these methods); however, unsupervised approaches in this area are much scarcer. One such approach has been introduced by BIBREF13 , who have proposed a model for unsupervised Named Entity Recognition. Similar to our approach, their model is based on calculating the similarity between vector representations of candidate phrases and existing entities. However, their vector representations are created using a combination of TF-IDF weights and word context information, and their method relies on a terminology. More recently, BIBREF14 have utilized Word2Vec and Doc2Vec embeddings for unsupervised sentiment classification in medical discharge summaries.
> 
> A number of previous studies have focused on unsupervised extraction of relations such as protein-protein interactions (PPI) from biomedical texts. For example, BIBREF15 have utilized several techniques, namely kernel-based pattern clustering and dependency parsing, to extract PPI from biomedical texts. BIBREF16 have introduced a system for unsupervised extraction of entities and relations between these entities from clinical texts written in Italian, which utilized a thesaurus for extraction of entities and clustering methods for relation extraction. BIBREF17 also used clinical texts and proposed a generative model for unsupervised relation extraction. Another approach focusing on relation extraction has been proposed by BIBREF18 . Their approach is based on constructing a graph which is used to construct domain-independent patterns for extracting protein-protein interactions.
> 
> A similar but distinct approach to unsupervised extraction is distant supervision. Similarly as unsupervised extraction methods, distant supervision methods don't require any labeled data, but make use of weakly labeled data, such as data extracted from a knowledge base. Distant supervision has been applied to relation extraction BIBREF19 , extraction of gene interactions BIBREF20 , PPI extraction BIBREF21 , BIBREF22 , and identification of PICO elements BIBREF23 . The advantage of our approach compared to the distantly supervised methods is that it does not require any underlying knowledge base or a similar source of data.

### Relevance

Label: 

## Record 0184

Paper: Unsupervised Identification of Study Descriptors in Toxicology Research: An Experimental Study

### Question

> What is their binary classifier?

### Passage

> work has largely focused on identifying specific pieces of information such as biomedical events BIBREF6 or PICO elements BIBREF0 . However, depending on the domain and the end goal of the extraction, these may be insufficient to comprehensively describe a given study.
> 
> Therefore, in this paper we focus on unsupervised methods for identifying text segments (such as sentences or fixed length sequences of words) relevant to the information being extracted. We develop a model that can be used to identify text segments from text documents without labeled data and that only requires the current document itself, rather than an entire training corpus linked to the target document. More specifically, we utilize representation learning methods BIBREF7 , where words or phrases are embedded into the same vector space. This allows us to compute semantic relatedness among text fragments, in particular sentences or text segments in a given document and a short description of the type of information being extracted from the document, by using similarity measures in the feature space. The model has the potential to speed up identification of relevant segments in text and therefore to expedite annotation of domain specific information without reliance on costly labeled data.
> 
> We have developed and tested our approach on a reference database of rodent uterotropic bioassays BIBREF1 which are labeled according to their adherence to test guidelines set forth in BIBREF3 . Each study in the database is assigned a label determining whether or not it met each of six main criteria defined by the guidelines; however, the database does not contain sentence-level annotations or any information about where the criteria was mentioned in each publication. Due to the lack of fine-grained annotations, supervised learning methods cannot be easily applied to aid annotating new publications or to annotate related but distinct types of studies. This database therefore presents an ideal use-case for unsupervised approaches.
> 
> While our approach doesn't require any labeled data to work, we use the labels available in the dataset to evaluate the approach. We train a binary classification model for identifying publications which satisfied given criteria and show the model performs better when trained on relevant sentences identified by our method than when trained on

### Relevance

Label: 

## Record 0185

Paper: Unsupervised Identification of Study Descriptors in Toxicology Research: An Experimental Study

### Question

> What is their binary classifier?

### Passage

> (Raleigh, NC, USA) on offspring postnatal day (pnd) 16.
> 
> This validation study followed OECD TG 440, with six female weanling rats (postnatal day 21) per dose group and six treatment groups.
> 
> These three sentences were extracted from the abstract and the full text of a single document (document 20981862, the abstract of which is shown in Figures FIGREF2 and FIGREF11 - FIGREF21 ). These three sentences were retrieved as the most similar to MC 1, with similarity scores of 70.61, 65.31, and 63.69, respectively. The third sentence contains the “answer” to MC 1 (underlined). However, it can be seen the top two sentences also discuss the animals used in the study (more specifically, the sentences discuss the animals' housing and their origin).

### Relevance

Label: 

## Record 0186

Paper: Autocompletion interfaces make crowd workers slower, but their use promotes response diversity

### Question

> What crowdsourcing platform was used?

### Passage

> Crowdsourcing applications vary from basic, self-contained tasks such as image recognition or labeling BIBREF0 all the way to open-ended and creative endeavors such as collaborative writing, creative question proposal, or more general ideation BIBREF1 . Yet scaling the crowd to very large sets of creative tasks may require prohibitive numbers of workers. Scalability is one of the key challenges in crowdsourcing: how to best apply the valuable but limited resources provided by crowd workers and how to help workers be as efficient as possible.
> 
> Efficiency gains can be achieved either collectively at the level of the entire crowd or by helping individual workers. At the crowd level, efficiency can be gained by assigning tasks to workers in the best order BIBREF2 , by filtering out poor tasks or workers, or by best incentivizing workers BIBREF3 . At the individual worker level, efficiency gains can come from helping workers craft more accurate responses and complete tasks in less time.
> 
> One way to make workers individually more efficient is to computationally augment their task interface with useful information. For example, an autocompletion user interface (AUI) BIBREF4 , such as used on Google's main search page, may speed up workers as they answer questions or propose ideas. However, support for the benefits of AUIs is mixed and existing research has not considered short, repetitive inputs such as those required by many large-scale crowdsourcing problems. More generally, it is not yet clear what are the best approaches or general strategies to achieve efficiency gains for creative crowdsourcing tasks.
> 
> In this work, we conducted a randomized trial of the benefits of allowing workers to answer a text-based question with the help of an autocompletion user interface. Workers interacted with a web form that recorded how quickly they entered text into the response field and how quickly they submitted their responses after typing is completed. After the experiment concluded, we measured response diversity using textual analyses and response quality using a followup crowdsourcing task with an independent population of workers. Our results indicate that the AUI treatment did not affect quality, and did not help workers perform more quickly or achieve greater response consensus. Instead, workers with the AUI were significantly

### Relevance

Label: 

## Record 0187

Paper: Autocompletion interfaces make crowd workers slower, but their use promotes response diversity

### Question

> What crowdsourcing platform was used?

### Passage

> We have showed via a randomized control trial that an autocompletion user interface (AUI) is not helpful in making workers more efficient. Further, the AUI led to a more lexically and semantically diverse set of text responses to a given task than if the AUI was not present. The AUI also had no noticeable impact, positive or negative, on response quality, as independently measured by other workers.
> 
> A challenge with text-focused crowdsourcing is aggregation of natural language responses. Unlike binary labeling tasks, for example, normalizing text data can be challenging. Should casing be removed? Should words be stemmed? What to do with punctuation? Should typos be fixed? One of our goals when testing the effects of the AUI was to see if it helps with this normalization task, so that crowdsourcers can spend less time aggregating responses. We found that the AUI would likely not help with this in the sense that the sets of responses became more diverse, not less. Yet, this may in fact be desirable—if a crowdsourcer wants as much diverse information from workers as possible, then showing them dynamic AUI suggestions may provide a cognitive priming mechanism to inspire workers to consider responses which otherwise would not have occurred to them.
> 
> One potential explanation for the increased submission delay among AUI workers is an excessive number of options presented by the AUI. The goal of an AUI is to present the best options at the top of the drop down menu (Fig. FIGREF2 B). Then a worker can quickly start typing and choose the best option with a single keystroke or mouse click. However, if the best option appears farther down the menu, then the worker must commit more time to scan and process the AUI suggestions. Our AUI always presented six suggestions, with another six available by scrolling, and our experiment did not vary these numbers. Yet the size of the AUI and where options land may play significant roles in submission delay, especially if significant numbers of selections come from AUI positions far from the input area.
> 
> We aimed to explore position effects, but due to some technical issues we did not record the positions in the AUI that

### Relevance

Label: 

## Record 0188

Paper: Autocompletion interfaces make crowd workers slower, but their use promotes response diversity

### Question

> What crowdsourcing platform was used?

### Passage

> An important goal of crowdsourcing research is achieving efficient scalability of the crowd to very large sets of tasks. Efficiency in crowdsourcing manifests both in receiving more effective information per worker and in making individual workers faster and/or more accurate. The former problem is a significant area of interest BIBREF5 , BIBREF6 , BIBREF7 while less work has been put towards the latter.
> 
> One approach to helping workers be faster at individual tasks is the application of usability studies. BIBREF8 ( BIBREF8 ) famously showed how crowd workers can perform user studies, although this work was focused on using workers as usability testers for other platforms, not on studying crowdsourcing interfaces. More recent usability studies on the efficiency and accuracy of workers include: BIBREF9 ( BIBREF9 ), who consider the task completion times of macrotasks and microtasks and find workers given smaller microtasks were slower but achieve higher quality than those given larger macrotasks; BIBREF10 ( BIBREF10 ), who study how the sequence of tasks given to workers and interruptions between tasks may slow workers down; and BIBREF11 ( BIBREF11 ), who study completion times for relevance judgment tasks, and find that imposed time limits can improve relevance quality, but do not focus on ways to speed up workers. These studies do not test the effects of the task interface, however, as we do here.
> 
> The usability feature we study here is an autocompletion user interface (AUI). AUIs are broadly familiar to online workers at this point, thanks in particular to their prominence on Google's main search bar (evolving out of the original Google Instant implementation). However, literature on the benefits of AUIs (and related word prediction and completion interfaces) in terms of improving efficiency is decidedly mixed.
> 
> It is generally assumed that AUIs make users faster by saving keystrokes BIBREF12 . However, there is considerable debate about whether or not such gains are countered by increased cognitive load induced by processing the given autocompletions BIBREF13 . BIBREF14 ( BIBREF14 ) showed that typists can enter text more quickly with word completion and prediction interfaces than without. However, this study focused on a different input modality (an onscreen keyboard) and, more importantly, on a text

### Relevance

Label: 

## Record 0189

Paper: Autocompletion interfaces make crowd workers slower, but their use promotes response diversity

### Question

> What crowdsourcing platform was used?

### Passage

> in submission delay, especially if significant numbers of selections come from AUI positions far from the input area.
> 
> We aimed to explore position effects, but due to some technical issues we did not record the positions in the AUI that workers chose. However, our Javascript instrumentation logged worker keystrokes as they typed so we can approximately reconstruct the AUI position of the worker's ultimate response. To do this, we first identified the logged text inputed by the worker before it was replaced by the AUI selection, then used this text to replicate the database query underlying the AUI, and lastly determined where the worker's final response appeared in the query results. This procedure is only an approximation because our instrumentation would occasionally fail to log some keystrokes and because a worker could potentially type out the entire response even if it also appeared in the AUI (which the worker may not have even noticed). Nevertheless, most AUI workers submitted responses that appeared in the AUI (Fig. FIGREF24 A) and, of those responses, most owere found in the first few (reconstructed) positions near the top of the AUI (Fig. FIGREF24 B). Specifically, we found that 59.3% of responses were found in the first two reconstructed positions, and 91.2% were in the first six. With the caveats of this analysis in mind, which we hope to address in future experiments, these results provide some evidence that the AUI responses were meaningful and that the AUI workers were delayed by the AUI even though most chosen responses came from the top area of the AUI which is most quickly accessible to the worker.
> 
> Beyond AUI position effects and the number of options shown in the AUI, there are many aspects of the interplay between workers and the AUI to be further explored. We limited workers to performing no more than ten tasks, but will an AUI eventually lead to efficiency gains beyond that level of experience? It is also an open question if an AUI will lead to efficiency gains when applying more advanced autocompletion and ranking algorithms than the one we used. Given that workers were slower with the AUI primarily due to a delay after they

### Relevance

Label: 

## Record 0190

Paper: Autocompletion interfaces make crowd workers slower, but their use promotes response diversity

### Question

> What crowdsourcing platform was used?

### Passage

> , BIBREF19 . Vector operations within this space such as addition and subtraction are capable of representing meaning and interrelationships between words BIBREF19 . For example, the vector INLINEFORM0 is very close to the vector INLINEFORM1 , indicating that these vectors capture analogy relations. Here we used 300-dimension word vectors trained on a 100B-word corpus taken from Google News (word2vec). For each question we computed the average similarity between words in the responses to that question—a lower similarity implies more semantically diverse answers. Specifically, for a given question INLINEFORM2 , we concatenated all responses to that question into a single document INLINEFORM3 , and averaged the vector similarities INLINEFORM4 of all pairs of words INLINEFORM5 in INLINEFORM6 , where INLINEFORM7 is the word vector corresponding to word INLINEFORM8 : DISPLAYFORM0
> 
> where INLINEFORM0 if INLINEFORM1 and zero otherwise. We also excluded from EQREF21 any word pairs where one or both words were not present in the pre-trained word vectors (approximately 13% of word pairs). For similarity INLINEFORM2 we chose the standard cosine similarity between two vectors. As with response density, we found that most questions had lower word vector similarity INLINEFORM3 (and are thus collectively more semantically diverse) when considering AUI responses as the document INLINEFORM4 than when INLINEFORM5 came from the Control workers (Fig. FIGREF19 C). The difference was significant (Wilcoxon signed rank test paired on questions: INLINEFORM6 , INLINEFORM7 , INLINEFORM8 ).
> 
> Taken together, we conclude from these three analyses that the AUI increased the diversity of the responses workers gave.

### Relevance

Label: 

## Record 0191

Paper: Learning Representations of Emotional Speech with Deep Convolutional Generative Adversarial Networks

### Question

> What are the tasks in the multitask learning setup?

### Passage

> The investigated multitask model is based upon the DCGAN architecture described in Section SECREF2 and is implemented in TensorFlow. For emotion classification a fully connected layer is attached to the final convolutional layer of the DCGAN's discriminator. The output of this layer is then fed to two separate fully connected layers, one of which outputs a valence label and the other of which outputs an activation label. This setup is shown visually in Figure FIGREF4 . Through this setup, the model is able to take advantage of unlabeled data during training by feeding it through the DCGAN layers in the model, and is also able to take advantage of multitask learning and train the valence and activation outputs simultaneously.
> 
> In particular, the model is trained by iteratively running the generator, discriminator, valence classifier, and activation classifier, and back-propagating the error for each component through the network. The loss functions for the generator and discriminator are unaltered, and remain as shown in Section SECREF2 . Both the valence classifier and activation classifier use cross entropy loss as in Equation EQREF2 .
> 
> Since the valence and activation classifiers share layers with the discriminator the model learns features and convolutional filters that are effective for the tasks of valence classification, activation classification, and discriminating between real and generated samples.

### Relevance

Label: 

## Record 0192

Paper: Learning Representations of Emotional Speech with Deep Convolutional Generative Adversarial Networks

### Question

> What are the tasks in the multitask learning setup?

### Passage

> The proposed model builds upon previous results in the field of emotion recognition, and leverages prior work in representation learning.
> 
> Multitask learning has been effective in some prior experiments on emotion detection. In particular, Xia and Liu proposed a multitask model for emotion recognition which, like the investigated model, has activation and valence as targets BIBREF13 . Their work uses a Deep Belief Network (DBN) architecture to classify the emotion of audio input, with valence and activation as secondary tasks. Their experiments indicate that the use of multitask learning produces improved unweighted accuracy on the emotion classification task. Like Xia and Liu, the proposed model uses multitask learning with valence and activation as targets. Unlike them, however, we are primarily interested not in emotion classification, but in valence classification as a primary task. Thus, our multitask model has valence as a primary target and activation as a secondary target. Also, while our experiments use the IEMOCAP database like Xia and Liu do, our method of speaker split differs from theirs. Xia and Liu use a leave-one-speaker-out cross validation scheme with separate train and test sets that have no speaker overlap. This method lacks a distinct validation set; instead, they validate and test on the same set. Our experimental setup, on the other hand, splits the data into distinct train, validation, and test sets, still with no speaker overlap. This is described in greater detail in Section SECREF5 .
> 
> The unsupervised learning part of the investigated model builds upon an architecture known as the deep convolutional generative adversarial network, or DCGAN. DCGAN consists of two components, known as the generator and discriminator, which are trained against each other in a minimax setup. The generator learns to map samples from a random distribution to output matrices of some pre-specified form. The discriminator takes an input which is either a generator output or a “real” sample from a dataset. The discriminator learns to classify the input as either generated or real BIBREF9 .
> 
> For training, the discriminator uses a cross entropy loss function based on how many inputs were correctly classified as real and how many were correctly classified as generated. The cross entropy loss between true labels

### Relevance

Label: 

## Record 0193

Paper: Learning Representations of Emotional Speech with Deep Convolutional Generative Adversarial Networks

### Question

> What are the tasks in the multitask learning setup?

### Passage

> shown to be the most challenging emotional dimension for acoustic analyses in a number of studies BIBREF10 , BIBREF11 . Apart from solely targeting valence classification, we further investigate the principle of multitask learning. In multitask learning, a set of related tasks are learned (e.g., emotional activation), along with a primary task (e.g., emotional valence); both tasks share parts of the network topology and are hence jointly trained, as depicted in Figure FIGREF4 . It is expected that data for the secondary task models information, which would also be discriminative in learning the primary task. In fact, this approach has been shown to improve generalizability across corpora BIBREF12 .
> 
> The remainder of this paper is organized as follows: First we introduce the DCGAN model and discuss prior work, in Section SECREF2 . Then we describe our specific multitask DCGAN model in Section SECREF3 , introduce the datasets in Section SECREF4 , and describe our experimental design in Section SECREF5 . Finally, we report our results in Section SECREF6 and discuss our findings in Section SECREF7 .

### Relevance

Label: 

## Record 0194

Paper: Learning Representations of Emotional Speech with Deep Convolutional Generative Adversarial Networks

### Question

> What are the tasks in the multitask learning setup?

### Passage

> We investigated the use of unsupervised and multitask learning to improve the performance of an emotional valence classifier. Overall, we found that unsupervised learning yields considerable improvements in classification accuracy for the emotional valence recognition task. The best performing model achieves 43.88% in the 5-class case and 49.80% in the 3-class case with a significant Pearson correlation between continuous target label and prediction of INLINEFORM0 ( INLINEFORM1 ). There is no indication that multitask learning provides any advantage.
> 
> The results for multitask learning are somewhat surprising. It may be that the valence and activation classification tasks are not sufficiently related for multitask learning to yield improvements in accuracy. Alternatively, a different neural network architecture may be needed for multitask learning to work. Further, the alternating update strategy employed in the present work might not have been the optimal strategy for training. The iterative swapping of target tasks valence/activation might have created instabilities in the weight updates of the backpropagation algorithm. There may yet be other explanations; further investigation may be warranted.
> 
> Lastly, it is important to note that this model's performance is only approaching state-of-the-art, which employs potentially better suited sequential classifiers such as Long Short-term Memory (LSTM) networks BIBREF17 . However, basic LSTM are not suited to learn from entirely unsupervised data, which we leveraged for the proposed DCGAN models. For future work, we hope to adapt the technique of using unlabeled data to sequential models, including LSTM. We expect that combining our work here with the advantages of sequential models may result in further performance gains which may be more competitive with today's leading models and potentially outperform them. For the purposes of this investigation, the key takeaway is that the use of unsupervised learning yields clear performance gains on the emotional valence classification task, and that this represents a technique that may be adapted to other models to achieve even higher classification accuracies.

### Relevance

Label: 

## Record 0195

Paper: Learning Representations of Emotional Speech with Deep Convolutional Generative Adversarial Networks

### Question

> What are the tasks in the multitask learning setup?

### Passage

> measure) between predicted and actual labels.
> 
> Some pre-processing was needed to obtain accurate measures. In particular, in cases where human annotators were perfectly split on what the correct label for a particular sample should be, both possibilities should be accepted as correct predictions. For instance, if the correct label is 4.5 (vector form INLINEFORM0 ), a correct prediction could be either 4 or 5 (i.e. the maximum index in the output vector should either be 4 or 5).
> 
> The above measures are for a 5-point labeling scale, which is how the IEMOCAP data is originally labeled. However, prior experiments have evaluated performance on valence classification on a 3-point scale BIBREF16 . The authors provide an example of this, with valence levels 1 and 2 being pooled into a single “negative” category, valence level 3 remaining untouched as the “neutral” category, and valence levels 4 and 5 being pooled into a single “positive” category. Thus, to allow for comparison with our models, we also report results on such a 3-point scale. We construct these results by taking the results for 5 class comparison and pooling them as just described.

### Relevance

Label: 

## Record 0196

Paper: Impact of Batch Size on Stopping Active Learning for Text Classification

### Question

> What is active learning?

### Passage

> Active learning has the potential to significantly reduce annotation costs. Two important considerations in the active learning process are when to stop the iterative process of asking for more labeled data and how large of a batch size to use when asking for additional labels during each iteration. We found that stopping methods degrade in performance when larger batch sizes are used. The degradation in performance is larger than the amount that can be explained due to the degradation in learning efficiency that results from using larger batch sizes. An important parameter used by stopping methods is what window size of earlier iterations to consider in making the stopping decision. Our results indicate that making the window size smaller helps to mitigate the degradation in stopping method performance that occurs with larger batch sizes.

### Relevance

Label: 

## Record 0197

Paper: Impact of Batch Size on Stopping Active Learning for Text Classification

### Question

> What is active learning?

### Passage

> The use of active learning has received a lot of interest for reducing annotation costs for text classification BIBREF0 , BIBREF1 , BIBREF2 .
> 
> Active learning sharply increases the performance of iteratively trained machine learning models by selectively determining which unlabeled samples should be annotated. The number of samples that are selected for annotation at each iteration of active learning is called the batch size.
> 
> An important aspect of the active learning process is when to stop the active learning process. Stopping methods enable the potential benefits of active learning to be achieved in practice. Without stopping methods, the active learning process would continue until all annotations have been labeled, defeating the purpose of using active learning. Accordingly, there has been a lot of interest in the development of active learning stopping methods BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 , BIBREF6 .
> 
> Another important aspect of the active learning process is what batch size to use. Previous work has shown that using smaller batch sizes leads to greater learning efficiency BIBREF2 , BIBREF7 . There is a tension between using smaller batch sizes to optimize learning efficiency and using larger batch sizes to optimize development speed and ease of annotation. We analyze how batch size affects a leading stopping method and how stopping method parameters can be changed to optimize performance depending on the batch size.
> 
> We evaluate the effect batch size has on active learning stopping methods for text classification. We use the publicly available 20Newsgroups dataset in our experiments.
> 
> For our base learner, we use the implementation of a Support Vector Machine from the scikit-learn Python library. For our sampling algorithm, we use the closest-to-hyperplane algorithm BIBREF2 , which has been shown in recent work to compare favorably with other sampling algorithms BIBREF8 . We use a binary bag of words representation and only consider words that show up in the dataset more than three times. We use a stop word list to remove common English words.
> 
> For analyzing the impact of batch size on stopping methods, we use a method that will stop at the first training iteration that is within a specified percentage of the maximum achievable performance. We denote

### Relevance

Label: 

## Record 0198

Paper: Impact of Batch Size on Stopping Active Learning for Text Classification

### Question

> What is active learning?

### Passage

> Looking at Table~ SECREF4 , one can see that Oracle-99 needs more annotations with larger batch percents to reach approximately the same F-Measure as with smaller batch percents.
> 
> These results are consistent with past findings that learning efficiency is decreased with larger batch sizes BIBREF2 , BIBREF7 . However, an open question is whether changing the parameters associated with actual stopping methods can make them experience less degradation in performance when larger batch sizes are used. In particular, an important parameter of stopping methods is the window size of previous iterations to consider. The next subsection shows how decreasing the window size parameter can help to reduce the degradation in performance that stopping methods experience with larger batch sizes.

### Relevance

Label: 

## Record 0199

Paper: Impact of Batch Size on Stopping Active Learning for Text Classification

### Question

> What is active learning?

### Passage

> We set INLINEFORM0 to be the window size that the user has defined. Kappa is an agreement metric between two models. Therefore, BV2009 needs INLINEFORM1 models to be generated before it begins to check if the average is above the threshold. This does not necessarily mean it stops after INLINEFORM2 models have been generated. Rather, it represents the first point in the active learning process at which BV2009 even has a chance to stop.
> 
> When using larger batch percents, fewer models are generated than when using smaller batch percents. This gives any stopping method less points to test whether or not to stop. We also note that kappa agreement scores are generally low between the first few models trained. This, combined with fewer points to stop at, causes BV2009 to stop somewhat sub-optimally when using very large batch percents. Usage of very large batch sizes, such as 10% of the data, is not common so sub-optimal performance of stopping methods in those situations is not a major problem.

### Relevance

Label: 

## Record 0200

Paper: Impact of Batch Size on Stopping Active Learning for Text Classification

### Question

> What is active learning?

### Passage

> We denote the stopping method published in BIBREF4 as BV2009. This stopping method will stop the active learning process if the mean of the three previous kappa agreement values between consecutive models is above a threshold. For larger batch percents, note that BV2009 stops later than the optimal Oracle Method point.
> 
> We ran BV2009 with smaller window sizes for each of our different batch sizes. Our results are summarized for a window size of one in the row ``BV2009 (Window Size = 1)'' in Table~ SECREF4 . When using a window size of one, BV2009 is able to stop with a smaller number of annotations than when using a window size of three. This is done without losing much F-Measure. The next subsection provides an explanation as to why smaller window sizes are more effective than larger window sizes when larger batch sizes are used.

### Relevance

Label: 
