# Passage relevance annotation

Annotator: 

Enter your name or agreed identifier after `Annotator:`.

Judge whether each passage helps answer the question, including useful partial evidence. Topic overlap alone is insufficient.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Preserve all content and record numbers. Work independently; do not exchange labels before submission. Algorithm sources are disclosed.

## Question 0181

Paper: A Comprehensive Comparison of Machine Learning Based Methods Used in Bengali Question Classification

> what datasets did they use?

### Common Retrieved Chunks

#### Passage 1371

Retrieved by: BM25, Hybrid

> A Bengali QC System was built by Somnath Banerjee and Sivaji Bandyopadhyay BIBREF13 BIBREF19 BIBREF20. They proposed a two-layer taxonomy classification with 9 coarse-grained classes and 69 fine-grained classes. There are other research works BIBREF0 BIBREF21 in Bengali Language. A survey was performed on text QA techniques BIBREF22 where there was an analysis conducted in Bengali Language. Syed Mehedi Hasan Nirob et al achieved 88.62% accuracy by using 380 top frequent words as the feature in their work BIBREF17.

#### Relevance 1371

Label: 

#### Passage 1372

Retrieved by: BM25, Dense, Hybrid

> Researches on question classification, question taxonomies and QA system have been undertaken in recent years. There are two types of approaches for question classification according to Banerjee et al in BIBREF13 - by rules and by machine learning approach. Rule based approaches use some hard coded grammar rules to map the question to an appropriate answer type BIBREF14 BIBREF15. Machine Learning based approaches have been used by Zhang et al and Md. Aminul Islam et al in BIBREF16 and BIBREF0. Many classifiers have been used in machine learning for QC such as Support Vector Machine (SVM) BIBREF16 BIBREF17, Support Vector Machines and Maximum Entropy Model BIBREF18, Naive Bayes (NB), Kernel Naive Bayes (KNB), Decision Tree (DT) and Rule Induction (RI) BIBREF13. In BIBREF0, they claimed to achieve average precision of 0.95562 for coarse class and 0.87646 for finer class using Stochastic Gradient Descent (SGD).

#### Relevance 1372

Label: 

#### Passage 1376

Retrieved by: Dense, Hybrid

> We use two setups (as done in BIBREF0) for our system. In the first setup, we eliminate the stop words from the text using another dataset containing only stop words. At second step, we work without eliminating the stop words from the text which gives better result than the first setup.

#### Relevance 1376

Label: 

#### Passage 1377

Retrieved by: Dense, Hybrid

> RF is an ensemble learning technique. It constructs large number of decision trees during training and then predicts the majority class. We use 500 decision trees in the forest and "entropy" function to measure the quality of a split.

#### Relevance 1377

Label: 

#### Passage 1378

Retrieved by: Dense, Hybrid

> We use different types of classifiers for QA type classification. We separate our methodology into two sections similar to BIBREF0 - one is training section and another is validation section shown in Figure FIGREF5.
> 
> We use 10 fold cross validation where we have 3150 and 350 questions in our training set and validation set respectively. During training, after selecting the possible class labels, the system extracts the features of the questions and creates a model by passing through a classifier algorithm with the extracted features and class labels. During validation, the system extracts the features of the question and passes it into the model created during training and predicts the answer type.

#### Relevance 1378

Label: 

### BM25

#### Passage 1373

Retrieved by: BM25

> SVM gives an optimal hyper-plane and it maximizes the margin between classes. We use Radial Basis Function (RBF) kernel in our system to make decision boundary curve-shaped. For decision function shape, we use the original one-vs-one (ovo) decision function.

#### Relevance 1373

Label: 

#### Passage 1374

Retrieved by: BM25

> MLP contains three layers - an input layer, an output layer and some hidden layers. Input layer receives the signal, the output layer gives a decision or prediction about the input and the computation of the MLP is conducted in the hidden layers. In our system, we use 100 layers. For weight optimization, we use Limited-memory Broyden–Fletcher–Goldfarb–Shanno (LBFGS) optimization algorithm.

#### Relevance 1374

Label: 

#### Passage 1375

Retrieved by: BM25

> Gradient Boosting Classifier produces a prediction model consisting of weak prediction models. Gradient boosting uses decision trees. We use 100 boosting stages in this work.

#### Relevance 1375

Label: 

### Dense

#### Passage 1379

Retrieved by: Dense

> Table II shows the accuracy and F1 score for different classifiers with and without eliminating stop words while extracting features. Figure FIGREF21 shows the average results of different classifiers in a bar chart with and without eliminating stop words from the questions.
> 
> Overall, SGD has shown the best performance on our dataset as it introduces non-linearity and uses back-propagation for updating parameter weights using loss function calculated on training set into classification. K-NN has shown the weakest performance overall, as this algorithm has a bad reputation of not working well in high dimensional data BIBREF28. MLP and SVM have shown similar performance. MLP takes advantage of multiple hidden layers in order to take non-linearly separable samples in a linearly separable condition. SVM accomplishes this same feat by taking the samples to a higher dimensional hyperplane where the samples are linearly separable. Gradient Boosting Classifier (GBC) and Random Forest (RF) both utilize a set of decision trees and achieve similar results (RF performs slightly without eliminating stop words). Naive Bayesian Classifier (NBC) shows performance on per with GBC and RF algorithms. The overall better performance of all the algorithms when provided with stop words show the importance of stop words in Bengali QA classification.
> 
> Figure FIGREF22 shows the predictions of some particular questions by each of the classifiers. The input is a full question and the output is the class of the question.

#### Relevance 1379

Label: 

### Hybrid

None

## Question 0182

Paper: A Focus on Neural Machine Translation for African Languages

> What evaluation metrics did they use?

### Common Retrieved Chunks

#### Passage 1380

Retrieved by: BM25, Dense, Hybrid

> We examine randomly sampled sentences from the test set for each language and translate them using the trained models. In order for readers to understand the accuracy of the translations, we provide back-translations of the generated translation to English. These back-translations were performed by a speaker of the specific target language. More examples of the translations are provided in the Appendix. Additionally, attention visualizations are provided for particular translations. The attention visualizations showed how the Transformer multi-head attention captured certain syntactic rules of the target languages.
> 
> In Table TABREF20 , ConvS2S did not perform the translation successfully. Despite the content being related to the topic of the original sentence, the semantics did not carry. On the other hand, Transformer achieved an accurate translation. Interestingly, the target sentence used an abbreviation, however, both translations did not. This is an example of how lazy target translations in the original dataset would negatively affect the BLEU score, and implore further improvement to the datasets. We plot an attention map to demonstrate the success of Transformer to learn the English-to-Afrikaans sentence structure in Figure FIGREF12 .
> 
> Despite the bad performance of the English-to-isiZulu models, we wanted to understand how they were performing. The translated sentences, given in Table TABREF21 , do not make sense, but all of the words are valid isiZulu words. Interestingly, the ConvS2S translation uses English words in the translation, perhaps due to English data occurring in the isiZulu dataset. The ConvS2S however correctly prefixed the English phrase with the correct prefix “i-". The Transformer translation includes invalid acronyms and mentions “disease" which is not in the source sentence.
> 
> If we examine Table TABREF22 , the ConvS2S model struggled to translate the sentence and had many repeating phrases. Given that the sentence provided is a difficult one to translate, this is not surprising. The Transformer model translated the sentence well, except included the word “boithabišo”, which in this context can be translated to “fun” - a concept that was not present in the original sentence.
> 
> Table TABREF23 shows that the ConvS2S model translated the sentence very successfully. The word “khumo” directly means “wealth” or “riches”. A better synonym would be “letseno”, meaning income or “letlotlo” which

#### Relevance 1380

Label: 

#### Passage 1381

Retrieved by: BM25, Dense, Hybrid

> The BLEU scores for each target language for both the ConvS2S and the Transformer models are reported in Table TABREF7 . For the ConvS2S model, we provide results for sentences tokenised by white spaces (Word), and when tokenised using the optimal number of BPE tokens (Best BPE), as determined in Section SECREF25 . The Transformer model uses the same number of WordPiece tokens as the number of BPE tokens which was deemed optimal during the BPE ablation study done on the ConvS2S model.
> 
> In general, the Transformer model outperformed the ConvS2S model for all of the languages, sometimes achieving 10 BLEU points or more over the ConvS2S models. The results also show that the translations using BPE tokenisation outperformed translations using standard word-based tokenisation. The relative performance of Transformer to ConvS2S models agrees with what has been seen in existing NMT literature BIBREF20 . This is also the case when using BPE tokenisation as compared to standard word-based tokenisation techniques BIBREF21 .
> 
> Overall, we notice that the performance of the NMT techniques on a specific target language is related to both the number of parallel sentences and the morphological typology of the language. In particular, isiZulu, N. Sotho, Setswana, and Xitsonga languages are all agglutinative languages, making them harder to translate, especially with very little data BIBREF22 . Afrikaans is not agglutinative, thus despite having less than half the number of parallel sentences as Xitsonga and Setswana, the Transformer model still achieves reasonable performance. Xitsonga and Setswana are both agglutinative, but have significantly more data, so their models achieve much higher performance than N. Sotho or isiZulu.
> 
> The translation models for isiZulu achieved the worst performance when compared to the others, with the maximum BLEU score of 3.33. We attribute the bad performance to the morphological complexity of the language (as discussed in Section SECREF3 ), the very small size of the dataset as well as the poor quality of the data (as discussed in Section SECREF4 ).

#### Relevance 1381

Label: 

#### Passage 1383

Retrieved by: BM25, Hybrid

> The publicly-available Autshumato parallel corpora are aligned corpora of South African governmental data which were created for use in machine translation systems BIBREF15 . The datasets are available for download at the South African Centre for Digital Language Resources website. The datasets were created as part of the Autshumato project which aims to provide access to data to aid in the development of open-source translation systems in South Africa.
> 
> The Autshumato project provides parallel corpora for English to Afrikaans, isiZulu, N. Sotho, Setswana, and Xitsonga. These parallel corpora were aligned on the sentence level through a combination of automatic and manual alignment techniques.
> 
> The official Autshumato datasets contain many duplicates, therefore to avoid data leakage between training, development and test sets, all duplicate sentences were removed. These clean datasets were then split into 70% for training, 30% for validation, and 3000 parallel sentences set aside for testing. Summary statistics for each dataset are shown in Table TABREF2 , highlighting how small each dataset is.
> 
> Even though the datasets were cleaned for duplicate sentences, further issues exist within the datasets which negatively affects models trained with this data. In particular, the isiZulu dataset is of low quality. Examples of issues found in the isiZulu dataset are explained in Table TABREF3 . The source and target sentences are provided from the dataset, the back translation from the target to the source sentence is given, and the issue pertaining to the translation is explained.

#### Relevance 1383

Label: 

#### Passage 1384

Retrieved by: BM25, Hybrid

> BPE BIBREF21 and its variants, such as SentencePiece BIBREF19 , aid translation of rare words in NMT systems. However, the choice of the number of tokens to generate for any particular language is not made obvious by literature. Popular choices for the number of tokens are between 30,000 and 40,000: BIBREF20 use 37,000 for WMT 2014 English-to-German translation task and 32,000 tokens for the WMT 2014 English-to-French translation task. BIBREF23 used 32,000 SentencePiece tokens across all source and target data. Unfortunately, no motivation for the choice for the number of tokens used when creating sub-words has been provided.
> 
> Initial experimentation suggested that the choice of the number of tokens used when running BPE tokenisation, affected the model's final performance significantly. In order to obtain the best results for the given datasets and models, we performed an ablation study, using subword-nmt BIBREF21 , over the number of tokens required by BPE, for each language, on the ConvS2S model. The results of the ablation study are shown in Figure FIGREF26 .
> 
> As can be seen in Figure FIGREF26 , the models for languages with the smallest datasets (namely isiZulu and N. Sotho) achieve higher BLEU scores when the number of BPE tokens is smaller, and decrease as the number of BPE tokens increases. In contrast, the performance of the models for languages with larger datasets (namely Setswana, Xitsonga, and Afrikaans) improves as the number of BPE tokens increases. There is a decrease in performance at 20 000 BPE tokens for Setswana and Afrikaans, which the authors cannot yet explain and require further investigation. The optimal number of BPE tokens were used for each language, as indicated in Table TABREF7 .

#### Relevance 1384

Label: 

### BM25

#### Passage 1382

Retrieved by: BM25

> The difficulties hindering the progress of machine translation of African languages are discussed below.
> 
> Low availability of resources for African languages hinders the ability for researchers to do machine translation. Institutes such as the South African Centre for Digital Language Resources (SADiLaR) are attempting to change that by providing an open platform for technologies and resources for South African languages BIBREF7 . This, however, only addresses the 11 official languages of South Africa and not the greater problems within Africa.
> 
> Discoverability: The resources for African languages that do exist are hard to find. Often one needs to be associated with a specific academic institution in a specific country to gain access to the language data available for that country. This reduces the ability of countries and institutions to combine their knowledge and datasets to achieve better performance and innovations. Often the existing research itself is hard to discover since they are often published in smaller African conferences or journals, which are not electronically available nor indexed by research tools such as Google Scholar.
> 
> Reproducibility: The data and code of existing research are rarely shared, which means researchers cannot reproduce the results properly. Examples of papers that do not publicly provide their data and code are described in Section SECREF4 .
> 
> Focus: According to BIBREF8 , African society does not see hope for indigenous languages to be accepted as a more primary mode for communication. As a result, there are few efforts to fund and focus on translation of these languages, despite their potential impact.
> 
> Lack of benchmarks: Due to the low discoverability and the lack of research in the field, there are no publicly available benchmarks or leader boards to new compare machine translation techniques to.
> 
> This paper aims to address some of the above problems as follows: We trained models to translate English to Afrikaans, isiZulu, N. Sotho, Setswana and Xitsonga, using modern NMT techniques. We have published the code, datasets and results for the above experiments on GitHub, and in doing so promote reproducibility, ensure discoverability and create a baseline leader board for the five languages, to begin to address the lack of benchmarks.

#### Relevance 1382

Label: 

### Dense

#### Passage 1385

Retrieved by: Dense

> Section SECREF9 describes the quantitative performance of the models by comparing BLEU scores, while a qualitative analysis is performed in Section SECREF10 by analysing translated sentences as well as attention maps. Section SECREF25 provides the results for an ablation study done regarding the effects of BPE.

#### Relevance 1385

Label: 

#### Passage 1386

Retrieved by: Dense

> Additional translation results from ConvS2S and Transformer are given in Table TABREF27 along with their back-translations for Afrikaans, N. Sotho, Setswana, and Xitsonga. We include these additional sentences as we feel that the single sentence provided per language in Section SECREF10 , is not enough demonstrate the capabilities of the models. Given the scarcity of research in this field, researchers might find the additional sentences insightful into understanding the real-world capabilities and potential, even if BLEU scores are low.

#### Relevance 1386

Label: 

#### Passage 1387

Retrieved by: Dense

> The authors would like to thank Reinhard Cromhout, Guy Bosa, Mbongiseni Ncube, Seale Rapolai, and Vongani Maluleke for assisting us with the back-translations, and Jason Webster for Google Translate API assistance. Research supported with Cloud TPUs from Google's TensorFlow Research Cloud (TFRC).

#### Relevance 1387

Label: 

### Hybrid

#### Passage 1388

Retrieved by: Hybrid

> This section details published research for machine translation for the South African languages. The existing research is technically incomparable to results published in this paper, because their datasets (in particular their test sets) are not published. Table TABREF1 shows the BLEU scores provided by the existing work.
> 
> Google Translate BIBREF2 , as of February 2019, provides translations for English, Afrikaans, isiZulu, isiXhosa and Southern Sotho, six of the official South African languages. Google Translate was tested with the Afrikaans and isiZulu test sets used in this paper to determine its performance. However, due to the uncertainty regarding how Google Translate was trained, and which data it was trained on, there is a possibility that the system was trained on the test set used in this study as this test set was created from publicly available governmental data. For this reason, we determined this system is not comparable to this paper's models for isiZulu and Afrikaans.
> 
> BIBREF3 trained Transformer models for English to Setswana on the parallel Autshumato dataset BIBREF15 . Data was not cleaned nor was any additional data used. This is the only study reviewed that released datasets and code. BIBREF4 performed statistical phrase-based translation for English to Setswana translation. This research used linguistically-motivated pre- and post-processing of the corpus in order to improve the translations. The system was trained on the Autshumato dataset and also used an additional monolingual dataset.
> 
> BIBREF5 used statistical machine translation for English to Xitsonga translation. The models were trained on the Autshumato data, as well as a large monolingual corpus. A factored machine translation system was used, making use of a combination of lemmas and part of speech tags.
> 
> BIBREF6 used unsupervised word segmentation with phrase-based statistical machine translation models. These models translate from English to Afrikaans, N. Sotho, Xitsonga and isiZulu. The parallel corpora were created by crawling online sources and official government data and aligning these sentences using the HunAlign software package. Large monolingual datasets were also used.
> 
> BIBREF16 performed word translation for English to isiZulu. The translation system was trained on a combination of Autshumato, Bible, and data obtained from the South African Constitution. All of the isiZulu text was syllabified prior to the training

#### Relevance 1388

Label: 

## Question 0183

Paper: Generating Major Types of Chinese Classical Poetry in a Uniformed Framework

> What is the source of the training/testing data?

### Common Retrieved Chunks

#### Passage 1389

Retrieved by: BM25, Hybrid

> 1.1.1.1em
> 
> Jinyi Hu, Maosong Sun$^{*}$ $*$ Corresponding author
> 
> Department of Computer Science and Technology, Tsinghua University, Beijing, China
> 
> Institute for Artificial Intelligence, Tsinghua University, Beijing, China
> 
> State Key Lab on Intelligent Technology and Systems, Tsinghua University, Beijing, China
> 
> hujy17@mails.tsinghua.edu.cn, sms@tsinghua.edu.cn
> 
> Poetry generation is an interesting research topic in the field of text generation. As one of the most valuable literary and cultural heritages of China, Chinese classical poetry is very familiar and loved by Chinese people from generation to generation. It has many particular characteristics in its language structure, ranging from form, sound to meaning, thus is regarded as an ideal testing task for text generation. In this paper, we propose a GPT-2 based uniformed framework for generating major types of Chinese classical poems. We define a unified format for formulating all types of training samples by integrating detailed form information, then present a simple form-stressed weighting method in GPT-2 to strengthen the control to the form of the generated poems, with special emphasis on those forms with longer body length. Preliminary experimental results show this enhanced model can generate Chinese classical poems of major types with high quality in both form and content, validating the effectiveness of the proposed strategy. The model has been incorporated into Jiuge, the most influential Chinese classical poetry generation system developed by Tsinghua University BIBREF0.

#### Relevance 1389

Label: 

#### Passage 1392

Retrieved by: BM25, Hybrid

> With the development of deep learning, the mainstream of poem generation research has been shifted from traditional statistical models to neural network methods in recent years. Most existing works are based on the Encoder-Decoder architecture BIBREF2. In Chinese classical poetry generation, yan2013poet proposed a model using the Encoder-Decoder architecture and wang2016chinese further used attention-based sequence-to-sequence model.
> 
> The key factor in designing the model architecture is how to treat the generated context so far in the process of generating a poem. The input to the encoder could be as short as a single poetic line or all the previously generated lines (whole history). Theoretically, considering the whole history is more appropriate for keeping the thematic coherence and integrity of the generated poem than considering the short history, at the expense that may hurt the fluency of the generated sentences due to the data sparseness problem possibly caused by the more sophisticated model.
> 
> Thus we have two basic ways to figure out the history. One is to consider the whole history. zhang2014chinese first introduced the neural network method into poetry generation by proposing the so-called incremental Recurrent Neural Network, where every sentence (line) is embedded into a sentence vector by a Convolutional Sentence Model and then all are packed into a history vector. yi2018chinesea presented a working memory mechanism in LSTM, designing three kinds of memory to address the whole history. Another is to select part of history. yi2018chineseb observed that considering the full context may not lead to good performance in LSTM, and proposed salient clue mechanism where only salient characters in partial history are under consideration.
> 
> The Transformer BIBREF3 architecture and other models based on this, including GPT BIBREF4, Bert BIBREF5, show much better results in various NLP tasks. Transformer utilizes the self-attention mechanism in which any pair of tokens in the sequence can attend to each other, making it possible to generate much longer SHI or CI while keeping the coherence throughout the poem.
> 
> liao2019gpt applied GPT to Chinese classical poetry generation. They pre-trained the model on a Chinese news corpus with 235M sentences and then fine-tuning the model on Chinese poem corpus with 250,000 Jueju and Lvshi, 20,000 CIs, 700,000 pairs of couplets.

#### Relevance 1392

Label: 

#### Passage 1395

Retrieved by: Dense, Hybrid

> In the basic model, the loss function for training with respect to the $i$th token in the text is conventionally defined as the cross-entropy:
> 
> where $x[i]$ is the vector of $i$th token, $j$ is over all possible token types.
> 
> To address the form problem, we simply add a weighting factor into the loss function with particular stress on the aforementioned three types of form-related tokens, i.e., the line separation label ‘,’, the stanza separation label ‘$\&$’, and $[EOF]$, as in:
> 
> where $weight[i]$ is set as 1 for any Chinese character, 2 for ‘,’ and ‘$\&$’, and 3 for $[EOF]$.
> 
> This simple method (we thus call it the form-stressed weighting method) enhances the model’s capability to form control quite significantly. Figure 4(b) shows an example that contrasts the case in Figure 4(a).

#### Relevance 1395

Label: 

#### Passage 1396

Retrieved by: Dense, Hybrid

> liao2019gpt applied GPT to Chinese classical poetry generation. They pre-trained the model on a Chinese news corpus with 235M sentences and then fine-tuning the model on Chinese poem corpus with 250,000 Jueju and Lvshi, 20,000 CIs, 700,000 pairs of couplets. A key point is they defined a unified format to formulate different types of training samples, as [form, identifier 1, theme, identifier 2, body], where “body” accommodates the full content of an SHI, CI, or couplet in corresponding “form” with “theme” as its title. Experiments demonstrated GPT-based poem generation gained promising performance, meanwhile still faced some limitations, for instance, only 70% of the generated CIs for the Cipai Shuidiaogetou, a sort of CI with quite long body, are correct in form.
> 
> Regarding this, we think the work of liao2019gpt could be improved in the following three respects. First, there is a large improving room for better fitting the form requirement of CI in the process of generation, especially for those with relatively long body length. Second, their formulation format for training samples can be supplemented, for example, the stanza structure of CI is missing. Third, using contemporary Chinese news corpus to pre-train the model may not be necessary, owing to distinctive differences in both meaning and form between contemporary Chinese and Chinese classical poetry language.
> 
> For the above considerations, we give up the pre-training on the news corpus and add a separation label to indicate the stanza structure of CI. Then we make use of GPT-2 to train the model. Furthermore, we propose a form-stressed weighting method in GPT-2 to strengthen the control in particular to the form of CI.

#### Relevance 1396

Label: 

#### Passage 1397

Retrieved by: Dense, Hybrid

> We present a unified format for formulating all types of training samples of SHI and CI by extending the format given in liao2019gpt. First, we change various punctuations between lines into the comma ‘,’, serving as a uniform separation label between two lines. Second, we utilize three separation labels, $[label_1]$ and $[label_2]$ to separate between form, title, and body of the poem respectively, and $[label_3]$ to separate two stanzas of CI if needed. Third, we enclose $[EOS]$ at the end of the body. Thus, the format for SHI is as follows:
> 
> where n is the number of lines in the poem.
> 
> The format of CI will be enriched with $[label_3]$ if it has two stanzas in the body:
> 
> Here, $[label_1]$, $[label_2]$ and $[label_3]$ are set as ‘$\#$’, ‘$*$’ and ‘$\&$’.
> 
> After pre-processing, all the formatted poem samples will be sent to the poetry generation model for training, as illustrated in Figure 3.

#### Relevance 1397

Label: 

### BM25

#### Passage 1390

Retrieved by: BM25

> We would like to thank Zhipeng Guo, Xiaoyuan Yi, Xinran Gu and anonymous reviewers for their insightful comments. This work is supported by the project Text Analysis and Studies on Chinese Classical Literary Canons with Big Data Technology under grant number 18ZDA238 from the Major Program of the National Social Science Fund of China. Hu is also supported by the Initiative Scientific Research Program and Academic Training Program of the Department of Computer Science and Technology, Tsinghua University.

#### Relevance 1390

Label: 

#### Passage 1391

Retrieved by: BM25

> Chinese poetry is a rich treasure in Chinese traditional culture. For thousands of years, poetry is always considered as the crystallization of human wisdom and erudition by Chinese people and deeply influences the Chinese history from the mental and cultural perspective.
> 
> In general, a Chinese classical poem is a perfect combination of three aspects, i.e., form, sound, and meaning. Firstly, it must strictly obey a particular form which specifies the number of lines (i.e., sentences) in the poem and the number of characters in each line. Secondly, it must strictly obey a particular sound pattern which specifies the sound requirement for each character in every position of the poem. Lastly, it must be meaningful, i.e., with grammatical and semantic well-formedness for each line and, with thematic coherence and integrity throughout the poem. These three points form the universal principles for human poets to create Chinese classical poems.
> 
> Chinese Classical poetry can be classified into two primary categories, SHI and CI. According to the statistical data from CCPC1.0, a Chinese Classical Poetry Corpus consisting of 834,902 poems in total (We believe it is almost a full collection of Chinese Classical poems). 92.87% poems in CCPC1.0 fall into the category of SHI and 7.13% fall into the category of CI. SHI and CI can be further divided into many different types in terms of their forms. We briefly introduce the related background knowledge as follows.

#### Relevance 1391

Label: 

#### Passage 1393

Retrieved by: BM25

> According to our observation, the enhanced model is likely to generate poems with both high quality and diversity. We present two examples generated by the model and give some comments on the meaning of each poem.
> 
> UTF8gbsn七律 · 远望
> 
> UTF8gbsn江上微茫一叶舟，天涯芳草满汀洲
> 
> UTF8gbsn数声渔唱隔船过，几点人家落帆游
> 
> UTF8gbsn春色不从莺语到，夕阳空度客心愁
> 
> UTF8gbsn何时重向长桥饮，同泛溪光共白头
> 
> The example above is a Qiyan Lvshi. The title of this poem means “look far around”. In this poem, the first four lines depict a view seen from the river bank-misty and rolling waters, a drifting boat, lush vanillas, melodies from passing boats and cottages on the bank, creating a tranquil and halcyon atmosphere. However, the poet is still overcome by solitude and nostalgia because of the lonely trip, which is vividly revealed in the second four sentences. The poem adopts a typical semantic structure of Qiyan Lvshi with its first-half delineating a view and then conveying the poet’s feeling in the second-half (the contrast between the view and the feeling is one of the appreciated artistic methods in Chinese classical poems). In addition, for Lvshi, the pairs of $<$the third line, the fourth line$>$ and $<$the fifth line, the sixth line$>$ must satisfy the requirement of Duizhang, a correspondence in both part-of-speech(POS) and word sense between two parallel lines. This point is perfectly reflected in the generated poem, as shown in Table 2.
> 
> UTF8gbsn满江红 · 塞外
> 
> UTF8gbsn风急秋空，天欲暮，黄云飞处。
> 
> UTF8gbsn人不见，沙堤野戍，乱鸦啼苦。
> 
> UTF8gbsn万里胡笳吹雁断，三更羌笛愁如许。
> 
> UTF8gbsn甚关河、征妇泪痕多，无行路。
> 
> UTF8gbsn青狼火，荒烟树。
> 
> UTF8gbsn白露草，残阳度。
> 
> UTF8gbsn但寒山远近，故乡千古。
> 
> UTF8gbsn一角斜晖归梦绕，满江红叶西陵去。
> 
> UTF8gbsn待明年，又到汉家城，重回顾。
> 
> The example above is a CI in the form of Manjianghong and the title means “beyond the Great Wall”. It vividly depicts a typical view of the Northwestern China howling wind, clouds of dust, crying crows and lugubrious sound of flutes. The poem is saturated with nostalgia, solitude and desolate feelings of life, which is not only embodied in the bleak scenery but also overtly revealed in the last three sentences. The combination of visual and audio feelings and of reality and imagination is tactfully employed in the poem and makes it even more impressive and resonating.

#### Relevance 1393

Label: 

### Dense

#### Passage 1394

Retrieved by: Dense

> The preliminary observation on the generated poems suggests that the inclusion of the stanza separation into the unified format of training samples is beneficial in some degree for meeting the form requirement. For instance, we input the same title to the enhanced model and to a model trained under the same condition except without the stanza separation, asking them to generate a number of CIs with Cipai of Busuanzi, a task similar to that in Figure 4. We find that about 20% of CIs generated by the latter suffer from some errors in form, as illustrated in Figure 5, meanwhile all the CIs generated by the former ideally match the expected form.

#### Relevance 1394

Label: 

#### Passage 1398

Retrieved by: Dense

> We leverage the Transformer-based GPT-2, which is often used to train a robust language model, as the basic model of poetry generation. Compared to previous neural network-based language models such as RNN and LSTM, it is reported that GPT-2 exhibits good performance in the quality of generated texts given quite a long history BIBREF6. To weaken the so-called degeneration problem in generation and increase the diversity of generated texts, we use the top-k stochastic sampling strategy BIBREF7 (k is set as 15 in our experiment) to choose the next tokens to generate. In addition, our poetry generation model takes the Chinese character rather than the word as a basic linguistic unit, so word segmentation is not needed.
> 
> With this naive GPT-2 model, we see from the experimental results that the generated poems appear pretty good in both meaning and sound(including rhyme), though if being observed carefully, there still exist some in-depth problems in sentence fluency and thematic coherence of the whole poem which are uneasy to solve. As for form, the model can perform well in generating Jueju and Lvshi of SHI whereas rather poorly in generating various Cipai of CI, with quite high form errors. Figure 4(a) is an example of a generated CI by this model, under Cipai of Busuanzi, where two characters are mistakenly missing which obviously violates the form requirement.

#### Relevance 1398

Label: 

### Hybrid

None

## Question 0184

Paper: Verb Pattern: A Probabilistic Semantic Representation on Verbs

> what evaluation metrics are used?

### Common Retrieved Chunks

#### Passage 1399

Retrieved by: BM25, Dense, Hybrid

> To evaluate the effectiveness of our pattern summarization approach, we report two metrics: (1) ( INLINEFORM0 ) how much of the verb phrases in natural language our solution can find corresponding patterns (2) ( INLINEFORM1 ) how much of the phrases and their corresponding patterns are correctly matched? We compute the two metrics by: DISPLAYFORM0
> 
> ,where INLINEFORM0 is the number of phrases in the test data for which our solution finds corresponding patterns, INLINEFORM1 is the total number of phrases, INLINEFORM2 is the number of phrases whose corresponding patterns are correct. To evaluate INLINEFORM3 , we randomly selected 100 verb phrases from the test data and ask volunteers to label the correctness of their assigned patterns. We regard a phrase-pattern matching is incorrect if it's either too specific or too general (see examples in Fig FIGREF9 ). For comparison, we also tested two baselines for pattern summarization:
> 
> Idiomatic Baseline (IB) We treat each verb phrase as a idiom.
> 
> Conceptualized Baseline (CB) For each phrase, we assign it to a conceptualized pattern. For object INLINEFORM0 , we choose the concept with the highest probability, i.e. INLINEFORM1 , to construct the pattern.
> 
> Verb patterns cover 64.3% and 70% verb phrases in Tweets and News, respectively. Considering the spelling errors or parsing errors in Google N-Gram data, the coverage in general is acceptable. We report the precision of the extracted verb patterns (VP) with the comparisons to baselines in Fig FIGREF53 . The results show that our approach (VP) has a significant priority over the baselines in terms of precision. The result suggests that both conceptualized patterns and idiom patterns are necessary for the semantic representation of verbs.

#### Relevance 1399

Label: 

#### Passage 1400

Retrieved by: BM25, Dense, Hybrid

> We try to answer the question: “what are good verb patterns to summarize a set of verb phrases?” This is hard because in general we have multiple candidate verb patterns. Intuitively, good verb patterns should be aware of the generality and specificity.
> 
> Generality In general, we hope to use fewer patterns to represent the verbs' semantics. Otherwise, the extracted patterns will be trivial. Consider one extreme case where all phrases are considered as idiom phrases. Such idiom patterns obviously make no sense since idioms in general are a minority of the verb phrases.
> 
> Example 2 In Fig FIGREF9 , (eat $ INLINEFORM0 meal) is obviously better than the three patterns (eat $ INLINEFORM1 breakfast + eat $ INLINEFORM2 lunch+ eat $ INLINEFORM3 dinner). The former case provides a more general representation.
> 
> Specificity On the other hand, we expect the generated patterns are specific enough, or the results might be trivial. As shown in Example SECREF11 , we can generate the objects into some high-level concepts such as activity, thing, and item. These conceptualized patterns in general are too vague to characterize a verb's fine-grained semantic.
> 
> Example 3 For phrases in Fig FIGREF9 , eat $ INLINEFORM0 activity is more general than eat $ INLINEFORM1 meal. As a result, some wrong verb phrases such as eat shopping or each fishing can be recognized as a valid instance of phrases for eat. Instead, eat $ INLINEFORM2 meal has good specificity. This is because breakfast, lunch, dinner are three typical instances of meal, and meal has few other instances.
> 
> Contributions Generality and specificity obviously contradict to each other. How to find a good trade-off between them is the main challenge in this paper. We will use minimum description length (MDL) as the basic framework to reconcile the two objectives. More specifically, our contribution in this paper can be summarized as follows:
> 
> We proposed verb patterns, a novel semantic representations of verb. We proposed two types of verb patterns: conceptualized patterns and idiom patterns. The verb pattern is polysemy-aware so that we can use it to distinguish different verb semantics.
> 
> We proposed the principles for verb pattern extraction: generality and specificity. We show that the trade-off between them is

#### Relevance 1400

Label: 

#### Passage 1401

Retrieved by: BM25, Dense, Hybrid

> As suggested in the introduction, we can use verb patterns to improve context-aware conceptualization (i.e. to extract an entity's concept while considering its context). We do this by incorporating the verb patterns into a state-of-the-art entity-based approach BIBREF11 .
> 
> Entity-based approach The approach conceptualizes an entity INLINEFORM0 by fully employing the mentioned entities in the context. Let INLINEFORM1 be entities in the context. We denote the probability that INLINEFORM2 is the concept of INLINEFORM3 given the context INLINEFORM4 as INLINEFORM5 . By assuming all these entities are independent for the given concept, we compute INLINEFORM6 by: DISPLAYFORM0
> 
> Our approach We add the verb in the context as an additional feature to conceptualize INLINEFORM0 when INLINEFORM1 is an object of the verb. From verb patterns, we can derive INLINEFORM2 , which is the probability to observe the conceptualized pattern with concept INLINEFORM3 in all phrases of verb INLINEFORM4 . Thus, the probability of INLINEFORM5 conditioned on INLINEFORM6 given the context INLINEFORM7 as well as verb INLINEFORM8 is INLINEFORM9 . Similar to Eq EQREF54 , we compute it by: DISPLAYFORM0
> 
> Note that if INLINEFORM0 is observed in Google Syntactic N-Grams, which means that we have already learned its pattern, then we can use these verb patterns to do the conceptualization. That is, if INLINEFORM1 is mapped to a conceptualized pattern, we use the pattern's concept as the conceptualization result. If INLINEFORM2 is an idiom pattern, we stop the conceptualization.
> 
> Settings and Results For the two datasets used in the experimental section, we use both approaches to conceptualize objects in all verb phrases. Then, we select the concept with the highest probability as the label of the object. We randomly select 100 phrases for which the two approaches generate different labels. For each difference, we manually label if our result is better than, equal to, or worse than the competitor. Results are shown in Fig FIGREF56 . On both datasets, the precisions are significantly improved after adding verb patterns. This verifies that verb patterns are helpful in semantic understanding tasks.

#### Relevance 1401

Label: 

#### Passage 1402

Retrieved by: BM25, Hybrid

> Verb is crucial in sentence understanding BIBREF0 , BIBREF1 . A major issue of verb understanding is polysemy BIBREF2 , which means that a verb has different semantics or senses when collocating with different objects. In this paper, we only focus on verbs that collocate with objects. As illustrated in Example SECREF1 , most verbs are polysemous. Hence, a good semantic representation of verbs should be aware of their polysemy.
> 
> Example 1 (Verb Polysemy) eat has the following senses:
> 
> Many typical verb representations, including FrameNet BIBREF3 , PropBank BIBREF4 , and VerbNet BIBREF5 , describe verbs' semantic roles (e.g. ingestor and ingestibles for “eat”). However, semantic roles in general are too coarse to differentiate a verb's fine-grained semantics. A verb in different phrases can have different semantics but similar roles. In Example SECREF1 , both “eat”s in “eat breakfast” and “eat apple” have ingestor. But they have different semantics.
> 
> The unawareness of verbs' polysemy makes traditional verb representations unable to fully understand the verb in some applications. In sentence I like eating pitaya, people directly know “pitaya” is probably one kind of food since eating a food is the most fundamental semantic of “eat”. This enables context-aware conceptualization of pitaya to food concept. But by only knowing pitaya's role is the “ingestibles”, traditional representations cannot tell if pitaya is a food or a meal.
> 
> Verb Patterns We argue that verb patterns (available at http://kw.fudan.edu.cn/verb) can be used to represent more fine-grained semantics of a verb. We design verb patterns based on two word collocations principles proposed in corpus linguistics BIBREF6 : idiom principle and open-choice principle. Following the principles, we designed two types of verb patterns.
> 
> According to the above definitions, we use verb patterns to represent the verb's semantics. Phrases assigned to the same pattern have similar semantics, while those assigned to different patterns have different semantics. By verb patterns, we know the “pitaya” in I like eating pitaya is a food by mapping “eat pitaya” to “eat $ INLINEFORM0 food”. On the other hand, idiom patterns specify which phrases should not be conceptualized. We list verb phrases from Example SECREF1 and their verb patterns in Table TABREF7 . And we will show how

#### Relevance 1402

Label: 

#### Passage 1403

Retrieved by: BM25, Hybrid

> Traditional Verb Representations We compare verb patterns with traditional verb representations BIBREF12 . FrameNet BIBREF3 is built upon the idea that the meanings of most words can be best understood by semantic frames BIBREF13 . Semantic frame is a description of a type of event, relation, or entity and the participants in it. And each semantic frame uses frame elements (FEs) to make simple annotations. PropBank BIBREF4 uses manually labeled predicates and arguments of semantic roles, to capture the precise predicate-argument structure. The predicates here are verbs, while arguments are other roles of verb. To make PropBank more formalized, the arguments always consist of agent, patient, instrument, starting point and ending point. VerbNet BIBREF5 classifies verbs according to their syntax patterns based on Levin classes BIBREF14 . All these verb representations focus on different roles of the verb instead of the semantics of verb. While different verb semantics might have similar roles, the existing representations cannot fully characterize the verb's semantics.
> 
> Conceptualization One typical application of our work is context-aware conceptualization, which motivates the survey of the conceptualization. Conceptualization determines the most appropriate concept for an entity.Traditional text retrieval based approaches use NER BIBREF15 for conceptualization. But NER usually has only a few predefined coarse concepts. Wu et al. built a knowledge base with large-scale lexical information to provide richer IsA relations BIBREF7 . Using IsA relations, context-aware conceptualization BIBREF16 performs better. Song et al. BIBREF11 proposed a conceptualization mechanism by Naive Bayes. And Wen et al. BIBREF17 proposed a state-of-the-art model by combining co-occurrence network, IsA network and concept clusters.
> 
> Semantic Composition We represent verb phrases by verb patterns. while semantic composition works aim to represent the meaning of an arbitrary phrase as a vector or a tree. Vector-space model is widely used to represent the semantic of single word. A straightforward approach to characterize the semantic of a phrase thus is averaging the vectors over all the phrase's words BIBREF18 . But this approach certainly ignores the syntactic relation BIBREF19 between words. Socher et al. BIBREF20 represent the syntactic relation by a binary tree, which is fed into a recursive neural network together with the words' vectors. Recently, word2vec BIBREF21 shows its advantage

#### Relevance 1403

Label: 

### BM25

None

### Dense

#### Passage 1404

Retrieved by: Dense

> (which is given by the isA taxonomy), to encode the phrase. We will give more details about the probability computation in the experimental settings.
> 
> Thus, we have DISPLAYFORM0
> 
> Total Length We sum up the code length for all phrases to get the total code length INLINEFORM0 for assignment INLINEFORM1 : DISPLAYFORM0
> 
> Note that here we introduce the parameter INLINEFORM0 to control the relative importance of INLINEFORM1 and INLINEFORM2 . Next, we will explain that INLINEFORM3 actually reflects the trade-off between the generality and the specificity of the patterns.

#### Relevance 1404

Label: 

#### Passage 1405

Retrieved by: Dense

> “eat pitaya” to “eat $ INLINEFORM0 food”. On the other hand, idiom patterns specify which phrases should not be conceptualized. We list verb phrases from Example SECREF1 and their verb patterns in Table TABREF7 . And we will show how context-aware conceptualization benefits from our verb patterns in the application section.
> 
> Thus, our problem is how to generate conceptualized patterns and idiom patterns for verbs. We use two public data sets for this purpose: Google Syntactic N-Grams (http://commondatastorage.googleapis.com/books/syntactic -ngrams/index.html) and Probase BIBREF7 . Google Syntactic N-grams contains millions of verb phrases, which allows us to mine rich patterns for verbs. Probase contains rich concepts for instances, which enables the conceptualization for objects. Thus, our problem is given a verb INLINEFORM0 and a set of its phrases, generating a set of patterns (either conceptualized patterns or idiom patterns) for INLINEFORM1 . However, the pattern generation for verbs is non-trivial. In general, the most critical challenge we face is the trade-off between generality and specificity of the generated patterns, as explained below.

#### Relevance 1405

Label: 

### Hybrid

None

## Question 0185

Paper: Explicit Sentence Compression for Neural Machine Translation

> Which baselines to they compare to?

### Common Retrieved Chunks

#### Passage 1406

Retrieved by: BM25, Dense, Hybrid

> Explicit compression rate (length) control is a common method which has been used in previous sentence compression works. BIBREF18 examined several methods of introducing target output length information, and found that they were effective without negatively impacting summarization quality. BIBREF19 introduced a length marker token that induces the model to target an output of a desired length, coarsely divided into discrete bins. BIBREF17 augmented the decoder with an additional length countdown input which is a single scalar that ticks down to 0 when the generation reached the desired length.
> 
> Different with the length marker or length countdown input, to induce our model to output the compression sequence with desired length, we use beam search during generation to find the sequence $S^{^{\prime }}$ that maximizes a score function $s(S^{^{\prime }}, S)$ given a trained ESC model. The length normalization is introduced to account for the fact that we have to compare hypotheses of different length. Without some form of length-normalization regular $ln$, beam search will favor shorter sequences over longer ones on average since a negative log-probability is added at each step, yielding lower (more negative) scores for longer sentences. Moreover, a coverage penalty $cp$ is also added to favor the sequence that cover the source sentence meaning as much as possible according to the attention weights BIBREF20.
> 
> where $p_{i,j}$ is the attention probability of the $j$-th target word on the $i$-th source word. Parameters $\alpha $ and $\beta $ control the strength of the length normalization and the coverage penalty. Although $\alpha $ can be used to control the compression ratio softly, we use the compression ratio $\gamma $ to control the maximum length of decoding generation by hard requirements. When the decoding length $|S^{^{\prime }}|$ is greater than $\gamma |S|$, the decoding stops.

#### Relevance 1406

Label: 

#### Passage 1407

Retrieved by: BM25, Hybrid

> To let the translation have more focus over the source sentence information, efforts have been initiated on exploiting sentence segmentation, sentence simplification, and sentence compression for machine translation. BIBREF33 presented a approach to integrating the sentence skeleton information into a phrase-based statistic machine translation system. BIBREF34 proposed an approach to modeling syntactically-motivated skeletal structure of source sentence for statistic machine translation. BIBREF35 describe an early approach to skeleton-based translation, which decomposes input sentences into syntactically meaningful chunks. The central part of the sentence is identified and remains unaltered while other parts of the sentence are simplified. This process produces a set of partial, potentially overlapping translations which are recombined to form the final translation. BIBREF36 describe a “divide and translate” approach to dealing with complex input sentences. They parse the input sentences, replace subclauses with placeholders and later substitute them with separately translated clauses. Their method requires training translation models on clause-level aligned parallel data with placeholders in order for the translation model to deal with the placeholders correctly. BIBREF37 experimented with automatically segmenting the source sentence to overcome problems with overly long sentences. BIBREF38 showed that the spaces of original and simplified translations can be effectively combined using translation lattices and compare two decoding approaches to process both inputs at different levels of integration.
> 
> Different from these work, our proposed sentence compression model does not rely on any known linguistics motivated (such as syntax) skeleton simplification, but directly trains a computation motivated sentence compression model to learn to compress sentences and re-paraphrase them directly in seq2seq model. Though with a pure computation source, our sentence compression model can surprisingly generate more grammatically correct and refined sentences, and the words in the compressed sentence do not have to be the same as the original sentence. In the meantime, our sentence compression model can stably give source backbone representation exempt from unstable performance of a syntactic parser which is essential for syntactic skeleton simplification. Our sentence compression model can perform unsupervised training on large-scale data sets, and then use the supervised data for finetune, which is more promising from the results.

#### Relevance 1407

Label: 

#### Passage 1409

Retrieved by: BM25, Dense, Hybrid

> According to the results in Table TABREF34, we chose the semi-supervised ESC model (which performed the best) to generate compressed sentences for the machine translation task. The main results on the WMT14 EN-DE and EN-FR translation tasks are shown in Table TABREF35. In the EN-DE task, we made the following observations:
> 
> 1) The baseline Transformer (base) in this work achieved a performance comparable to the original Transformer (base) BIBREF0. This indicates that it is a strong baseline NMT system.
> 
> 2) All BSFNMT, BTFNMT, and BBFNMT significantly outperformed the baseline Transformer (base/big) and only introduces a very small amount of extra parameters. This indicates that the learned compressed backbone information was beneficial for the Transformer translation system.
> 
> 3) Among the proposed three methods, BTFNMT performed better than BSFNMT. This indicates that the backbone fusion at the target-side is better than at the source-side. In addition, BBFNMT (base/big) outperformed the comparison systems +Localness and +Context-Aware SANs. This indicates that the compression knowledge as an additional context can enhance NMT better.
> 
> 4) BBFNMT (based) is comparable to the +global-deep context, the best comparison system, while BBFNMT (big) slightly outperformed +global-deep context by $0.16$ BLEU scores. In particular, the parameters of BBFNMT (base/big) model, which just increased $12.1/7.9$M over the Transformer (base/big), were only 70% of the +global-deep context model. This denotes that the BBFNMT model is more efficient than the +global-deep context model. In addition, the training speed of the proposed models slightly decreased ($8\%$), compared to the corresponding baselines.
> 
> 5) The proposed BBFNMT (base) slightly outperformed the Transformer (big) which contains much more parameters than BBFNMT (base). This indicates that our improvement is not likely to be due to the increased number of parameters.
> 
> For the EN-FR translation task, the proposed models gave similar improvements over the baseline systems and comparing methods (except that the Transformer (big) performed much more better than Transformer (base)). These results show that our method is robust for improving the translation of other language pairs.

#### Relevance 1409

Label: 

#### Passage 1410

Retrieved by: BM25, Dense, Hybrid

> To evaluate the quality of our sentence compression model, we used the Annotated Gigaword corpus BIBREF21 as the benchmark BIBREF22. The data includes approximately 3.8 M training samples, 400 K validation samples, and 2 K test samples. The byte pair encoding (BPE) algorithm BIBREF23 was adopted for subword segmentation, and the vocabulary size was set at 40 K for our supervised, unsupervised and semi-supervised settings BIBREF24.
> 
> Baseline systems include AllText and F8W BIBREF22, BIBREF25. F8W is simply the first 8 words of the input, and AllText uses the whole text as the compression output. The $F_1$ score of ROUGE-1 (R-1), ROUGE-2 (R-2), and ROUGE-L (R-L) was used to evaluate this task BIBREF26. We use beam search with a beam size of 5, the length length normalization of 0.5, and the coverage penalty of 0.2.
> 
> For the semi-supervised setting, in order to make the results comparable to BIBREF13, we used the same 190M English monolingual unpaired data from WMT News Crawl datasets for pre-training (unsupervised training). We included the other pretraining methods: masked language modeling (MLM, BERT) BIBREF27, denoising auto-encoder (DAE) BIBREF28, and masked sequence to sequence (MASS) BIBREF13 to compare with our unsupervised pretraining method in the semi-supervised setting.

#### Relevance 1410

Label: 

#### Passage 1411

Retrieved by: Dense, Hybrid

> The proposed NMT model was evaluated on the WMT14 English-to-German (EN-DE) and English-to-French (EN-FR) tasks, which are both standard large-scale corpora for NMT evaluation. For the EN-DE translation task, 4.43 M bilingual sentence pairs from the WMT14 dataset were used as training data, including Common Crawl, News Commentary, and Europarl v7. The newstest2013 and newstest2014 datasets were used as the dev set and test set, respectively. For the EN-FR translation task, 36 M bilingual sentence pairs from the WMT14 dataset were were used as training data. Newstest12 and newstest13 were combined for validation and the newstest14 was the test set, following the setting of BIBREF29. The BPE algorithm BIBREF23 was also adopted, and the joint vocabulary size was set at 40 K. For the hyper-parameters of our Transformer (base/large) models, we followed the settings used in BIBREF0's work.
> 
> In addition, we also reported the state-of-the-art results in recent literatures, including modelling local dependencies (Localness) BIBREF30, fusing multiple-layer representations in SANs (Context-Aware) BIBREF31, and fusing all global context representations in SANs (global-deep context) BIBREF32. MultiBLEU was used to evaluate the translation task.

#### Relevance 1411

Label: 

### BM25

#### Passage 1408

Retrieved by: BM25

> Neural machine translation (NMT) is popularly implemented as an encoder-decoder framework BIBREF0, in which the encoder is right in charge of source sentence representation. Typically, the input sentence is implicitly represented as a contextualized source representation through deep learning networks. By further feeding the decoder, the source representation is used to learn dependent time-step context vectors for predicting target translation BIBREF1.
> 
> In state-of-the-art Transformer-based encoder, self-attention mechanisms are good at capturing the general information in a sentence BIBREF2, BIBREF3, BIBREF4. However, it is difficult to distinguish which kind of information lying deeply under the language is really salient for learning source representation. Intuitively, when a person reads a source sentence, he/she often selectively focuses on the basic sentence meaning, and re-reads the entire sentence to understand its meaning completely. Take the English sentence in Table TABREF2 as an example. We manually annotate its basic meaning as a shorter sequence of words than in the original sentence, called backbone information. Obviously, these words with the basic meaning contain more important information for human understanding than the remaining words in the sentence. We argue that such backbone information is also helpful for learning source representation, and is not explicitly considered by the existing NMT system to enrich the source sentence representation.
> 
> In this paper, we propose a novel explicit sentence compression approach to enhance the source representation for NMT. To this end, we first design three sentence compression models to accommodate the needs of various languages and scenarios, including supervised, unsupervised, and semi-supervised ways, to learn a backbone information words sequence (as shown in Table TABREF2) from the source sentence. We then propose three translation models, including backbone source-side fusion based NMT (BSFNMT), backbone target-side fusion (BTFNMT), and both-side fusion based NMT (BBFNMT), to introduce this backbone knowledge into the existing Transformer NMT system for improving translation predictions. Empirical results on the WMT14 English-to-German and English-to-French translation tasks show that the proposed approach significantly improves the translation performance over the strong even state-of-the-art NMT baselines.

#### Relevance 1408

Label: 

### Dense

#### Passage 1412

Retrieved by: Dense

> To evaluate the quality of our sentence compression model, we conducted a horizontal comparison between the proposed sentence compression model and other sentence compression models in different settings. Table TABREF34 shows the comparison results. We observed that the proposed unsupervised ESC model performed substantially better than Fevry and BIBREF17's unsupervised method. The proposed supervised ESC model also substantially outperformed the RNN-based Seq2seq and BIBREF11's baseline method. That is, our supervised model gave +2.0 improvements on R-1, R-2, and R-L scores over the RNN-based Seq2seq. This means that the proposed Transformer-based approaches can generate compressed sentences of high quality.
> 
> We further compared our semi-supervised model with the semi-supervised pretraining methods of MLM BIBREF27, DAE BIBREF28, and MASS BIBREF13. Our unsupervised pretrainining method outperformed the other unsupervised pretrainining ones on the sentence compression task consistently.

#### Relevance 1412

Label: 

### Hybrid

None

## Question 0186

Paper: From English To Foreign Languages: Transferring Pre-trained Language Models

> What datasets are used for evaluation?

### Common Retrieved Chunks

#### Passage 1413

Retrieved by: BM25, Dense, Hybrid

> All the RAMEN models are built from English and tuned on English for zero-shot cross-lingual tasks. It is reasonable to expect RAMENs do well in those tasks as we have shown in our experiments. But are they also a good feature extractor for supervised tasks? We offer a partial answer to this question by evaluating our model for supervised dependency parsing on UD datasets.
> 
> We used train/dev/test splits provided in UD to train and evaluate our RAMEN-based parser. Table TABREF38 summarizes the results (LAS) of our supervised parser. For a fair comparison, we choose mBERT as the baseline and all the RAMEN models are initialized from aligned fastText vectors. With the same architecture of 12 Transformer layers, RAMEN$_{\textsc {base}}$+BERT performs competitive to mBERT and outshines mBERT by +1.2 points for Vietnamese. The best LAS results are obtained by RAMEN$_{\textsc {large}}$+RoBERTa with 24 Transformer layers. Overall, our results indicate the potential of using contextual representations from RAMEN for supervised tasks.

#### Relevance 1413

Label: 

#### Passage 1415

Retrieved by: BM25, Hybrid

> In all the experiments, we tune RAMEN$_{\textsc {base}}$ for 175,000 updates and RAMEN$_{\textsc {large}}$ for 275,000 updates where the first 25,000 updates are for language specific parameters. The sequence length is set to 256. The mini-batch size are 64 and 24 when tuning language specific parameters using RAMEN$_{\textsc {base}}$ and RAMEN$_{\textsc {large}}$ respectively. For tuning bilingual LMs, we use a mini-batch size of 64 for RAMEN$_{\textsc {base}}$ and 24 for RAMEN$_{\textsc {large}}$ where half of the batch are English sequences and the other half are foreign sequences. This strategy of balancing mini-batch has been used in multilingual neural machine translation BIBREF23, BIBREF24.
> 
> We optimize RAMEN$_{\textsc {base}}$ using Lookahead optimizer BIBREF25 wrapped around Adam with the learning rate of $10^{-4}$, the number of fast weight updates $k=5$, and interpolation parameter $\alpha =0.5$. We choose Lookahead optimizer because it has been shown to be robust to the initial parameters of the based optimizer (Adam). For Adam optimizer, we linearly increase the learning rate from $10^{-7}$ to $10^{-4}$ in the first 4000 updates and then follow an inverse square root decay. All RAMEN$_{\textsc {large}}$ models are optimized with Adam due to memory limit.
> 
> When fine-tuning RAMEN on XNLI and UD, we use a mini-batch size of 32, Adam's learning rate of $10^{-5}$. The number of epochs are set to 4 and 50 for XNLI and UD tasks respectively. All experiments are carried out on a single Tesla V100 16GB GPU. Each RAMEN$_{\textsc {base}}$ model is trained within a day and each RAMEN$_{\textsc {large}}$ is trained within two days.

#### Relevance 1415

Label: 

#### Passage 1416

Retrieved by: BM25, Dense, Hybrid

> We evaluate our approach for six target languages: French (fr), Russian (ru), Arabic (ar), Chinese (zh), Hindi (hi), and Vietnamese (vi). These languages belong to four different language families. French, Russian, and Hindi are Indo-European languages, similar to English. Arabic, Chinese, and Vietnamese belong to Afro-Asiatic, Sino-Tibetan, and Austro-Asiatic family respectively. The choice of the six languages also reflects different training conditions depending on the amount of monolingual data. French and Russian, and Arabic can be regarded as high resource languages whereas Hindi has far less data and can be considered as low resource.
> 
> For experiments that use parallel data to initialize foreign specific parameters, we use the same datasets in the work of BIBREF6. Specifically, we use United Nations Parallel Corpus BIBREF18 for en-ru, en-ar, en-zh, and en-fr. We collect en-hi parallel data from IIT Bombay corpus BIBREF19 and en-vi data from OpenSubtitles 2018. For experiments that use only monolingual data to initialize foreign parameters, instead of training word-vectors from the scratch, we use the pre-trained word vectors from fastText BIBREF14 to estimate word translation probabilities (Eq. DISPLAY_FORM13). We align these vectors into a common space using orthogonal Procrustes BIBREF20, BIBREF15, BIBREF16. We only use identical words between the two languages as the supervised signal. We use WikiExtractor to extract extract raw sentences from Wikipedias as monolingual data for fine-tuning target embeddings and bilingual LMs (§SECREF15). We do not lowercase or remove accents in our data preprocessing pipeline.
> 
> We tokenize English using the provided tokenizer from pre-trained models. For target languages, we use fastBPE to learn 30,000 BPE codes and 50,000 codes when transferring from BERT and RoBERTa respectively. We truncate the BPE vocabulary of foreign languages to match the size of the English vocabulary in the source models. Precisely, the size of foreign vocabulary is set to 32,000 when transferring from BERT and 50,000 when transferring from RoBERTa.
> 
> We use XNLI dataset BIBREF9 for classification task and Universal Dependencies v2.4 BIBREF21 for parsing task. Since a language might have more than one treebank in Universal Dependencies, we use the following treebanks: en_ewt (English), fr_gsd (French), ru_syntagrus (Russian) ar_padt (Arabic), vi_vtb (Vietnamese), hi_hdtb (Hindi), and zh_gsd (Chinese).

#### Relevance 1416

Label: 

#### Passage 1417

Retrieved by: BM25, Dense, Hybrid

> We build on top of RAMEN a graph-based dependency parser BIBREF27. For the purpose of evaluating the contextual representations learned by our model, we do not use part-of-speech tags. Contextualized representations are directly fed into Deep-Biaffine layers to predict arc and label scores. Table TABREF34 presents the Labeled Attachment Scores (LAS) for zero-shot dependency parsing.
> 
> We first look at the fairest comparison between mBERT and monolingually initialized RAMEN$_{\textsc {base}}$+BERT. The latter outperforms the former on five languages except Arabic. We observe the largest gain of +5.2 LAS for French. Chinese enjoys +3.1 LAS from our approach. With similar architecture (12 or 24 layers) and initialization (using monolingual or parallel data), RAMEN+RoBERTa performs better than RAMEN+BERT for most of the languages. Arabic and Hindi benefit the most from bigger models. For the other four languages, RAMEN$_{\textsc {large}}$ renders a modest improvement over RAMEN$_{\textsc {base}}$.

#### Relevance 1417

Label: 

#### Passage 1418

Retrieved by: Dense, Hybrid

> We evaluate the performance of RAMEN+RoBERTa$_{\textsc {base}}$ (initialized from monolingual data) at each training steps: initialization of word embeddings (0K update), fine-tuning target embeddings (25K), and fine-tuning the model on both English and target language (at each 25K updates). The results are presented in Figure FIGREF40.
> 
> Without fine-tuning, the average accuracy of XLNI is 39.7% for a three-ways classification task, and the average LAS score is 3.6 for dependency parsing. We see the biggest leap in the performance after 50K updates. While semantic similarity task profits significantly at 25K updates of the target embeddings, syntactic task benefits with further fine-tuning the encoder. This is expected since the target languages might exhibit different syntactic structures than English and fine-tuning encoder helps to capture language specific structures. We observe a substantial gain of 19-30 LAS for all languages except French after 50K updates.
> 
> Language similarities have more impact on transferring syntax than semantics. Without tuning the English encoder, French enjoys 50.3 LAS for being closely related to English, whereas Arabic and Hindi, SOV languages, modestly reach 4.2 and 6.4 points using the SVO encoder. Although Chinese has SVO order, it is often seen as head-final while English is strong head-initial. Perhaps, this explains the poor performance for Chinese.

#### Relevance 1418

Label: 

### BM25

#### Passage 1414

Retrieved by: BM25

> We create a bilingual LM by plugging foreign language specific parameters to the pre-trained English LM (Figure FIGREF7). The new model has two separate embedding layers and output layers, one for English and one for foreign language. The encoder layer in between is shared. We then fine-tune this model using English and foreign monolingual data. Here, we keep tuning the model on English to ensure that it does not forget what it has learned in English and that we can use the resulting model for zero-shot transfer (§SECREF3). In this step, the encoder parameters are also updated so that in can learn syntactic aspects (i.e., word order, morphological agreement) of the target languages.

#### Relevance 1414

Label: 

### Dense

#### Passage 1419

Retrieved by: Dense

> Table TABREF32 shows the XNLI test accuracy. For reference, we also include the scores from the previous work, notably the state-of-the-art system XLM BIBREF6. Before discussing the results, we spell out that the fairest comparison in this experiment is the comparison between mBERT and RAMEN$_{\textsc {base}}$+BERT trained with monolingual only.
> 
> We first discuss the transfer results from BERT. Initialized from fastText vectors, RAMEN$_{\textsc {base}}$ slightly outperforms mBERT by 1.9 points on average and widen the gap of 3.3 points on Arabic. RAMEN$_{\textsc {base}}$ gains extra 0.8 points on average when initialized from parallel data. With triple number of parameters, RAMEN$_{\textsc {large}}$ offers an additional boost in term of accuracy and initialization with parallel data consistently improves the performance. It has been shown that BERT$_{\textsc {large}}$ significantly outperforms BERT$_{\textsc {base}}$ on 11 English NLP tasks BIBREF0, the strength of BERT$_{\textsc {large}}$ also shows up when adapted to foreign languages.
> 
> Transferring from RoBERTa leads to better zero-shot accuracies. With the same initializing condition, RAMEN$_{\textsc {base}}$+RoBERTa outperforms RAMEN$_{\textsc {base}}$+BERT on average by 2.9 and 2.3 points when initializing from monolingual and parallel data respectively. This result show that with similar number of parameters, our approach benefits from a better English pre-trained model. When transferring from RoBERTa$_{\textsc {large}}$, we obtain state-of-the-art results for five languages.
> 
> Currently, RAMEN only uses parallel data to initialize foreign embeddings. RAMEN can also exploit parallel data through translation objective proposed in XLM. We believe that by utilizing parallel data during the fine-tuning of RAMEN would bring additional benefits for zero-shot tasks. We leave this exploration to future work. In summary, starting from BERT$_{\textsc {base}}$, our approach obtains competitive bilingual LMs with mBERT for zero-shot XNLI. Our approach shows the accuracy gains when adapting from a better pre-trained model.

#### Relevance 1419

Label: 

### Hybrid

None

## Question 0187

Paper: Translating Questions into Answers using DBPedia n-triples

> Which movie subtitles dataset did they use?

### Common Retrieved Chunks

#### Passage 1420

Retrieved by: BM25, Dense, Hybrid

> We presented the work on a QA system trained with a sequence-to-sequence neural model with the DBpedia knowledge and movie dialogues. Although the automatic evaluation shows a low overlap of generated answers compared to the gold standard, a manual inspection of the showed promising outcomes from the experiment. Due to the nature of the training dataset, short answers are preferred, since they are more likely to have a lower log-likelihood score than the longer ones. Nevertheless, we observed several correct answers, which shows the availability of storing the entire DBpedia knowledge into neural networks. Our future work will focus on providing longer answers, as well as focusing on answering more complex questions.

#### Relevance 1420

Label: 

#### Passage 1421

Retrieved by: BM25, Dense, Hybrid

> For our QA system we used the DBpedia repository and the Subtitles corpus. Due to the nature of training a sequence-to-sequence neural model, questions and answers need to be aligned. The statistics on the used data are shown in Table TABREF5 .
> 
> In our work, we use the DBpedia BIBREF17 repository (version 2016-04). The DBpedia project aims to extract structured knowledge from the knowledge added to the Wikipedia repository. DBpedia allows users to semantically query relationships and properties of Wikipedia resources, including links to other related datasets.
> 
> For our experiment on training a QA system, we extracted (see Section SECREF4 ) the knowledge stored in Dbpedia Infobox Properties, which with its n-triple structure represents answers to particular questions. From this dataset we extracted more than 21M question-answer entries.
> 
> Since the extracted information form the DBpedia n-triples does not represent a natural language, we added to the extracted n-triples answers with dialogues from the OpenSubtitles dataset BIBREF18 . Since this dataset is stored in an XML structure with time codes, only sentences were extracted, where the first sentence ends with a question mark and the second sentence does not end with a question mark. Additionally, to ensure a better consistency between an question and the answer, the second sentence has to follow the first sentence by less than 20 seconds. From the 14M sentence corpus of question-answer pairs provided by the OpenNMT project, we used 5M dialogue entries to modify the language generation part. Table TABREF10 shows some examples from the OpenSubtitles dataset.

#### Relevance 1421

Label: 

#### Passage 1422

Retrieved by: BM25, Dense, Hybrid

> Recent approaches on building QA systems are dominated by the usage of neural networks. BIBREF2 present an approach for conversational modelling, which uses a sequence-to-sequence neural model. Their model predicts the next sentence given the previous sentences for an IT helpdesk domain, as well as for an open-domain trained on a subtitles dataset. For an open-domain dialogue generation, BIBREF3 propose using adversarial training. Therefore, reinforcement learning is used to train the system that produces sequences that are indistinguishable from human-generated dialogue utterances. For this, they jointly train two systems, a generative model, which produces response sequences and a discriminator to distinguish between the human-generated dialogues and the machine-generated ones. The outputs from the discriminator are then used as rewards for the generative model, guiding the system to generate dialogues that mostly resemble human dialogues. BIBREF4 demonstrate an end-to-end neural network model for generative QA. Their model is built on the encoder-decoder framework for sequence-to-sequence learning, while equipped with the ability to query a knowledge-base, which they demonstrate on the Chinese encyclopedia web site. The authors show that the proposed model is capable of generating natural and right answers by referring to the facts in the knowledge base. Additionally to the previous approaches, BIBREF5 extend the hierarchical recurrent encoder-decoder neural network to the open domain dialogue system and demonstrate that this model is competitive with state-of-the-art neural language models and back-off n-gram models. They illustrate limitations of similar approaches and show how the performance can be improved by bootstrapping the learning from a larger question-answer pair corpus and from pre-trained word embeddings. A heuristic that guides the development of neural baseline systems for the extractive QA task is described in BIBREF6 , which serves as guideline for the development of two neural baseline systems. Their RNN-based system, called FastQA, demonstrates good performance for extractive question answering due to the awareness of question words while processing the context. Additionally they introduce a composition function that goes beyond simple bag-of-words modelling. BIBREF7 demonstrate an approach to non-factoid answer generation with a separate component, which bases on BiLSTM to determine the importance of segments in the input. In contrast to other attention-based models, they determine the importance while assuming

#### Relevance 1422

Label: 

#### Passage 1424

Retrieved by: BM25, Dense, Hybrid

> Recent work on sequence-to-sequence neural networks have shown remarkable progress in many domains such as speech recognition, computer vision and language processing. These neural models can be used to map a sequence to another sequence, which has direct applications in natural language understanding BIBREF0 . One of the major advantages of this framework is that it requires a limited amount of feature engineering while still improving state-of-the-art results. This allows researchers to work on tasks for which domain knowledge may not be available. Question answering (QA) systems can directly benefit from this novel approaches, because it only requires mapping between questions and their answers. Due to the complexity of this mapping, most of the previous research in this domain used a complex pipeline of conventional linguistically-based NLP techniques, such as parsing, part-of-speech tagging and co-reference resolution BIBREF1 .
> 
> In this work, we build an open-domain QA system with sequence-to-sequence neural network models. The system was trained with question-answer pairs on the world knowledge represented in the DBpedia repository. Although building an open-domain system allows us to use an extensive amount of data stored in DBpedia, one of the challenges is to store this large amount of knowledge in the neural network architecture. Although these systems generally involve a smaller learning pipeline, they require a significant amount of training data.
> 
> Figure FIGREF1 illustrates how a sequence-to-sequence neural network can be trained on question-answering pairs. First, an sequence-to-sequence framework reads the source sentence, i.e. question, using an encoder to build a dense vector, a sequence of non-zero values that represents the meaning of a question. A decoder, processes this vector to predict an answer. In this manner, these encoder-decoder models can capture long-range dependencies in languages, e.g., gender agreements or syntax structures.

#### Relevance 1424

Label: 

### BM25

#### Passage 1423

Retrieved by: BM25

> simple bag-of-words modelling. BIBREF7 demonstrate an approach to non-factoid answer generation with a separate component, which bases on BiLSTM to determine the importance of segments in the input. In contrast to other attention-based models, they determine the importance while assuming the independence of questions and candidate answers. BIBREF8 present their Gated-Attention reader for answering cloze-style questions over documents. The reader features a novel multiplicative gating mechanism in combination with a multi-hop architecture, which is based on multiplicative interactions between the query embedding and the intermediate states of a recurrent neural network document reader. This enables the reader to build query-specific representations of tokens in the document for accurate answer selection.
> 
> The work mentioned above employ neural networks, but incorporate only a small amount of question-answering pairs to build their QA systems. Work on QA, which uses the DBpedia knowledge on the other hand, use much more complex linguistically-based NLP techniques to generate an answer for a given question. BIBREF9 propose a general purpose a QA system using Wikipedia data as its knowledge source, which can answer wh-interrogated questions. Their QA system includes tasks of named entity tagging, question classification, information retrieval and answer extraction. BIBREF10 present a QA approach on the DBpedia dataset. With predefined templates and dependency parsing on questions they obtain the entity and property mention from the question. They split the QA process into two steps; first they build an entity-centric index to search the target entity, whereby in the second step they expand the property mention with WordNet and ConceptNet to match the target entity with the searched entity property. Similarly, BIBREF11 present a QA system over Linked Data (DBpedia), which focuses on construct a bridge between the users and the Linked Data. Based on the consisting of subject-property-object (SPO) triples, each natural language question firstly is transformed into a triple-based representation (query triple). Then, the corresponding resources in DBpedia, including class, entity, property, are mapped for the phrases in the query triples. Finally, the optimal SPARQL query is generated as the output result. With this approach, their system can not only deal with the single-relation questions but also complex questions containing multi-relations. Differentially to the approaches mentioned above, we combine

#### Relevance 1423

Label: 

### Dense

#### Passage 1425

Retrieved by: Dense

> In this section, we give an overview of the sequence-to-sequence framework used in this experiment as well as information on the datasets used in our experiment. Furthermore, we give insights into the techniques to evaluate the correctness of the provided answers.

#### Relevance 1425

Label: 

### Hybrid

#### Passage 1426

Retrieved by: Hybrid

> The automatic evaluation of the proposed QA system is based on the correspondence between the generated answer and gold standard. For the automatic evaluation we used the BLEU BIBREF19 , METEOR BIBREF20 and chrF BIBREF21 metrics. BLEU (Bilingual Evaluation Understudy) is calculated for individual generated segments (n-grams) by comparing them with a dataset of of the gold standard. Considering the shortness of the questions, we report besides the four-gram overlap (BLEU) also scores based on the unigram overlap (BLEU-1). Those scores, between 0 and 100 (perfect overlap), are then averaged over the whole evaluation dataset to reach an estimate of the overall quality of the generated answers.
> 
> INLINEFORM0
> 
> METEOR (Metric for Evaluation of Translation with Explicit ORdering) is based on the harmonic mean of precision and recall, whereby recall is weighted higher than precision. Along with exact word (or phrase) matching it has additional features, i.e. stemming, paraphrasing and synonymy matching. In contrast to BLEU, the metric produces good correlation with human judgement at the sentence or segment level. Differently to the BLEU metric, which penalises the hypothesis, if words were generated with a different inflection, chrF3 is a character n-gram metric, which showed very good correlations with human judgements for morphologically rich languages.
> 
> INLINEFORM0
> 
> chrP represents the percentage of n-grams in the generated answer which has a counterpart in the gold standard answer, whereby chrR represents the percentage of character n-grams in the gold standard, which are also present in the predicted answer. INLINEFORM0 is a parameter which assigns INLINEFORM1 times more importance to recall than to precision.

#### Relevance 1426

Label: 

## Question 0188

Paper: Reader-Aware Multi-Document Summarization: An Enhanced Model and The First Dataset

> what is the source of their dataset?

### Common Retrieved Chunks

#### Passage 1427

Retrieved by: BM25, Dense, Hybrid

> The definition of the terminology related to the dataset is given as follows.
> 
> Topic: A topic refers to an event and it is composed of a set of news documents from different sources.
> 
> Document: A news article describing some aspects of the topic. The set of documents in the same topic typically span a period, say a few days.
> 
> Category: Each topic belongs to a category. There are 6 predefined categories: (1) Accidents and Natural Disasters, (2) Attacks (Criminal/Terrorist), (3) New Technology, (4) Health and Safety, (5) Endangered Resources, and (6) Investigations and Trials (Criminal/Legal/Other).
> 
> Aspect: Each category has a set of predefined aspects. Each aspect describes one important element of an event. For example, for the category “Accidents and Natural Disasters”, the aspects are “WHAT”, “WHEN”, “WHERE”, “WHY”, “WHO_AFFECTED”, “DAMAGES”, and “COUNTERMEASURES”.
> 
> Aspect facet: An aspect facet refers to the actual content of a particular aspect for a particular topic. Take the topic “Malaysia Airlines Disappearance” as an example, facets for the aspect “WHAT” include “missing Malaysia Airlines Flight 370”, “two passengers used passports stolen in Thailand from an Austrian and an Italian.” etc. Facets for the aspect “WHEN” are “ Saturday morning”, “about an hour into its flight from Kuala Lumpur”, etc.
> 
> Comment: A piece of text written by a reader conveying his or her altitude, emotion, or any thought on a particular news document.

#### Relevance 1427

Label: 

#### Passage 1428

Retrieved by: BM25, Hybrid

> The goal of multi-document summarization (MDS) is to automatically generate a brief, well-organized summary for a topic which describes an event with a set of documents from different sources. BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 , BIBREF6 . In the typical setting of MDS, the input is a set of news documents about the same topic. The output summary is a piece of short text document containing several sentences, generated only based on the input original documents.
> 
> With the development of social media and mobile equipments, more and more user generated content is available. Figure FIGREF2 is a snapshot of reader comments under the news report “The most important announcements from Google's big developers' conference”. The content of the original news report talks about some new products based on AI techniques. The news report generally conveys an enthusiastic tone. However, while some readers share similar enthusiasms, some others express their worries about new products and technologies and these comments can also reflect their interests which may not be very salient in the original news reports. Unfortunately, existing MDS approaches cannot handle this issue. We investigate this problem known as reader-aware multi-document summarization (RA-MDS). Under the RA-MDS setting, one should jointly consider news documents and reader comments when generating the summaries.
> 
> One challenge of the RA-MDS problem is how to conduct salience estimation by jointly considering the focus of news reports and the reader interests revealed by comments. Meanwhile, the model should be insensitive to the availability of diverse aspects of reader comments. Another challenge is that reader comments are very noisy, not fully grammatical and often expressed in informal expressions. Some previous works explore the effect of comments or social contexts in single document summarization such as blog summarization BIBREF7 , BIBREF8 . However, the problem setting of RA-MDS is more challenging because the considered comments are about an event which is described by multiple documents spanning a time period. Another challenge is that reader comments are very diverse and noisy. Recently, BIBREF9 employed a sparse coding based framework for RA-MDS jointly considering news documents and reader comments via an unsupervised data reconstruction strategy. However, they only used the bag-of-words

#### Relevance 1428

Label: 

#### Passage 1429

Retrieved by: BM25, Dense, Hybrid

> Another challenge is that reader comments are very diverse and noisy. Recently, BIBREF9 employed a sparse coding based framework for RA-MDS jointly considering news documents and reader comments via an unsupervised data reconstruction strategy. However, they only used the bag-of-words method to represent texts, which cannot capture the complex relationship between documents and comments.
> 
> Recently, BIBREF6 proposed a sentence salience estimation framework known as VAESum based on a neural generative model called Variational Auto-Encoders (VAEs) BIBREF10 , BIBREF11 . During our investigation, we find that the Gaussian based VAEs have a strong ability to capture the salience information and filter the noise from texts. Intuitively, if we feed both the news sentences and the comment sentences into the VAEs, commonly existed latent aspect information from both of them will be enhanced and become salient. Inspired by this consideration, to address the sentence salience estimation problem for RA-MDS by jointly considering news documents and reader comments, we extend the VAESum framework by training the news sentence latent model and the comment sentence latent model simultaneously by sharing the neural parameters. After estimating the sentence salience, we employ a phrase based compressive unified optimization framework to generate a final summary.
> 
> There is a lack of high-quality dataset suitable for RA-MDS. Existing datasets from DUC and TAC are not appropriate. Therefore, we introduce a new dataset for RA-MDS. We employed some experts to conduct the tasks of data collection, aspect annotation, and summary writing as well as scrutinizing. To our best knowledge, this is the first dataset for RA-MDS.
> 
> Our contributions are as follows: (1) We investigate the RA-MDS problem and introduce a new dataset for the problem of RA-MDS. To our best knowledge, it is the first dataset for RA-MDS. (2) To tackle the RA-MDS, we extend a VAEs-based MDS framework by jointly considering news documents and reader comments. (3) Experimental results show that reader comments can improve the summarization performance, which also demonstrates the usefulness of the dataset.

#### Relevance 1429

Label: 

#### Passage 1430

Retrieved by: BM25, Dense, Hybrid

> The dataset contains 45 topics from those 6 predefined categories. Some examples of topics are “Malaysia Airlines Disappearance”, “Flappy Bird”, “Bitcoin Mt. Gox”, etc. All the topics and categories are listed in Appendix SECREF7 . Each topic contains 10 news documents and 4 model summaries. The length limit of the model summary is 100 words (slitted by space). On average, each topic contains 215 pieces of comments and 940 comment sentences. Each news document contains an average of 27 sentences, and each sentence contains an average of 25 words. 85% of non-stop model summary terms (entities, unigrams, bigrams) appeared in the news documents, and 51% of that appeared in the reader comments. The dataset contains 19k annotated aspect facets.

#### Relevance 1430

Label: 

### BM25

#### Passage 1431

Retrieved by: BM25

> To evaluate the performance of our dataset and the proposed framework RAVAESum for RA-MDS, we compare our model with the following methods:
> 
> RA-Sparse BIBREF9 : It is a framework to tackle the RA-MDS problem. A sparse-coding-based method is used to calculate the salience of the news sentences by jointly considering news documents and reader comments.
> 
> Lead BIBREF17 : It ranks the news sentences chronologically and extracts the leading sentences one by one until the length limit.
> 
> Centroid BIBREF18 : It summarizes clusters of news articles automatically grouped by a topic detection system, and then it uses information from the centroids of the clusters to select sentences.
> 
> LexRank BIBREF1 and TextRank BIBREF19 : Both methods are graph-based unsupervised framework for sentence salience estimation based on PageRank algorithm.
> 
> Concept BIBREF5 : It generates abstractive summaries using phrase-based optimization framework with concept weight as salience estimation. The concept set contains unigrams, bigrams, and entities. The weighted term-frequency is used as the concept weight.
> 
> We can see that only the method RA-Sparse can handle RA-MDS. All the other methods are only for traditional MDS without comments.

#### Relevance 1431

Label: 

### Dense

#### Passage 1432

Retrieved by: Dense

> In this section, we describe the preparation process of the dataset. Then we provide some properties and statistics.

#### Relevance 1432

Label: 

#### Passage 1433

Retrieved by: Dense

> The properties of our own dataset are depicted in Section SECREF28 . We use ROUGE score as our evaluation metric BIBREF16 with standard options. F-measures of ROUGE-1, ROUGE-2 and ROUGE-SU4 are reported.

#### Relevance 1433

Label: 

### Hybrid

#### Passage 1434

Retrieved by: Hybrid

> The first step is to select topics. The selected topics should be in one of the above categories. We make use of several ways to find topics. The first way is to search the category name using Google News. The second way is to follow the related tags on Twitter. One more useful method is to scan the list of event archives on the Web, such as earthquakes happened in 2017 .
> 
> For some news websites, in addition to provide news articles, they offer a platform to allow readers to enter comments. Regarding the collection of news documents, for a particular topic, one consideration is that reader comments can be easily found. Another consideration is that all the news documents under a topic must be collected from different websites as far as possible. Similar to the methods used in DUC and TAC, we also capture and store the content using XML format.
> 
> Each topic is assigned to 4 experts, who are major in journalism, to conduct the summary writing. The task of summary writing is divided into two phases, namely, aspect facet identification, and summary generation. For the aspect facet identification, the experts read and digested all the news documents and reader comments under the topic. Then for each aspect, the experts extracted the related facets from the news document. The summaries were generated based on the annotated aspect facets. When selecting facets, one consideration is those facets that are popular in both news documents and reader comments have higher priority. Next, the facets that are popular in news documents have the next priority. The generated summary should cover as many aspects as possible, and should be well-organized using complete sentences with a length restriction of 100 words.
> 
> After finishing the summary writing procedure, we employed another expert for scrutinizing the summaries. Each summary is checked from five linguistic quality perspectives: grammaticality, non-redundancy, referential clarity, focus, and coherence. Finally, all the model summaries are stored in XML files.

#### Relevance 1434

Label: 

## Question 0189

Paper: WorldTree: A Corpus of Explanation Graphs for Elementary Science Questions supporting Multi-Hop Inference

> What does it mean for sentences to be "lexically overlapping"?

### Common Retrieved Chunks

#### Passage 1435

Retrieved by: BM25, Dense, Hybrid

> One might hypothesize that questions that require similar inferences to correctly answer may also contain some of the same knowledge in their explanations, with the amount of knowledge overlap dependent upon the similarity of the questions. We plan to explore using this overlap as a method of inference that can generate new explanations by editing, merging, or expanding known explanations from similar, known questions (see Jansen jansen:akbc2017 for an initial study). For this to be possible, an explanation corpus must reach a sufficient size that a large majority of questions have substantial overlap in their explanations.
> 
> Figure 5 shows the proportion of questions in the corpus that have 1 or more, 2 or more, 3 or more, etc., overlapping rows in their explanations with at least one other question in the corpus. Similarly, to ground this, Figure 4 shows a visualization of questions whose explanations have 2 or more overlapping rows. For a given level of overlapping explanation sentences, Figure 5 shows that the proportion of questions with that level of overlap increases logarithmically with the number of questions.
> 
> This has two consequences. First, it allows us to estimate the size of corpus required to train hypothetical inference methods for the science exam domain capable of producing explanations. If a given inference method can work successfully with only minimal overlap (for example, 1 shared table row), then a training corpus of 500 explanations in this domain should be sufficient to answer 80% of questions. If an inference method requires 2 shared rows, the corpus requirements would increase to approximately 2,500 questions to answer 80% of questions. However, if an inference method requires 3 or more rows, this likely would not be possible without a corpus of at least 20,000 questions and explanations – a substantial undertaking. Second, because this relationship is strongly logarithmic, if it transfers to domains outside elementary science, it should be possible to estimate the corpus size requirements for those domains after authoring explanations for only a few hundred questions.

#### Relevance 1435

Label: 

#### Passage 1436

Retrieved by: BM25, Dense, Hybrid

> Explanations for a given question here take the form of a list of sentences, where each sentence is a reference to a specific table row in the table store. To increase their utility for knowledge and inference analyses, we require that each sentence in an explanation be explicitly lexically connected (i.e. share words) with either the question, answer, or other sentences in the explanation. We call this lexically-connected set of sentences an explanation graph.
> 
> In our preliminary analysis, we observed that the sentences in our explanations can take on very different roles, and we hypothesize that differentiating these roles is likely important for inference algorithms. We identified four coarse roles, listed in Table 2 , and described below:
> 
> Central: The central concept(s) that a question is testing, such as changes of state or the coupled relationship between kinetic energy and temperature.
> 
> Grounding: Sentences linking generic or abstract terms in a central sentence with specific instances of those terms in the question or answer. For example, for questions about changes of state, grounding sentences might identify specific instances of liquids (such as water) or gasses (such as water vapor).
> 
> Background: Extra information elaborating on the topic, but that (strictly speaking) isn't required to arrive at the correct inference.
> 
> Lexical glue: Sentences that lexically link two concepts, such as “to add means to increase”, or “heating means adding heat”. This is an artificial category in our corpus, brought about by the need for explanation graphs to be explicitly lexically linked.
> 
> For each sentence in each authored explanation, we provide annotation indicating which of these four roles the sentence serves in that explanation.
> 
> Note that this figure also appears in an earlier workshop submission on identifying explanatory patterns BIBREF19

#### Relevance 1436

Label: 

#### Passage 1439

Retrieved by: BM25, Hybrid

> In terms of question answering, the ability to provide compelling human-readable explanations for answers to questions has been proposed as a complementary metric to assess QA performance alongside the proportion of questions answered correctly. Jansen et al. jansen2017framing developed a QA system for elementary science that answers questions by building and ranking explanation graphs built from aggregating multiple sentences read from free text corpora, including study guides and dictionaries. Because of the difficulty in constructing gold explanations to serve as training data, the explanations built with this system were constructed by modeling explanation quality as a latent variable machine learning problem. First, sentences were decomposed into sentence graphs based on clausal and prepositional boundaries, then assembled into multi-sentence “explanation graphs”. Questions were answered by ranking these candidate explanation graphs, using answer correctness as well as features that capture the connectivity of key-terms in the graphs as a proxy for explanation quality. Jansen at al. jansen2017framing showed that it is possible to learn to generate high quality explanations for 60% of elementary science questions using this method, an increase of 15% over a baseline that retrieved single continuous passages of text as answer justifications. Critically, in their error analysis Jansen et al. found that for questions answered incorrectly by their system, nearly half had successfully generated high-quality explanation graphs and ranked these highly, though they were not ultimately selected. They suggest that the process of building and ranking explanations would be aided by developing more expensive second-pass reranking processes that are able to better recognize the components and structure of high-quality explanations within a short list of candidates.
> 
> Knowledge bases of tables, or “table stores”, have recently been proposed as a semi-structured knowledge formalism for question answering that balances the cost of manually crafting highly-structured knowledge bases with the difficulties in acquiring this knowledge from free text BIBREF14 , BIBREF15 , BIBREF16 . The methods for question answering over tables generally take the form of constructing chains of multiple table rows that lead from terms in the question to terms in the answer, while the tables themselves are generally either collected from the web, automatically generated by extracting relations from free text, or manually constructed.
> 
> At

#### Relevance 1439

Label: 

#### Passage 1442

Retrieved by: Dense, Hybrid

> We began with the following design goals:
> 
> Computable explanations: Explanations should be represented at different levels of structure (explanation, then sentences, then relations within sentences). The knowledge links between explanation sentences should be explicit through lexical overlap, which can be used to form an “explanation graph” that describes how each sentence is linked in an explanation.
> 
> Depth: Sufficient knowledge should be present in explanations such that that the answer could be arrived at with little extra domain or world knowledge – i.e. where possible, explanations should be targeted at the level of knowledge of a 5-year old child, or lower (see below for a more detailed discussion of explanatory depth).
> 
> Reuse: Where possible, knowledge should be re-used across explanations to facilitate automated analysis of knowledge use, and identifying common explanation patterns across questions.

#### Relevance 1442

Label: 

### BM25

#### Passage 1437

Retrieved by: BM25

> chains of multiple table rows that lead from terms in the question to terms in the answer, while the tables themselves are generally either collected from the web, automatically generated by extracting relations from free text, or manually constructed.
> 
> At the collection end of the spectrum, Pasupat and Liang pasupat:2015 extract 2,108 HTML tables from Wikipedia, and propose a method of answering these questions by reasoning over the tables using formal logic. They also introduce the WikiTableQuestions dataset, a set of 22,033 question-answer pairs (such as “Greece held its last Summer Olympics during which year?”) that can be answered using these tables. Demonstrating the ability for collection at scale, Sun et al. sun:2016table extract a total of 104 million tables from Wikipedia and the web, and develop a model that constructs relational chains between table rows using a deep-learning framework. Using their system and table store, Sun et al. demonstrate state-of-the-art performance on several benchmark datasets, including WebQuestions BIBREF17 , a set of popular questions asked from the web designed to be answerable using the large structured knowledge graph Freebase (e.g. “What movies does Morgan Freeman star in?”).
> 
> In terms of automatic generation, though relations are often represented as $<subject, relation, argument>$ triples, Yin et al. yin:2015answering create a large table containing 120M n-tuple relations using OpenIE BIBREF18 , arguing that the extra expressivity afforded by these more detailed relations allows their system to answer more complex questions. Yin et al. use this to successfully reason over the WebQuestions dataset, as well as their own set of questions with more complex prepositional and adverbial constraints.
> 
> Elementary science exams contain a variety of complex and challenging inference problems BIBREF1 , BIBREF2 , with nearly 70% of questions requiring some form of causal, process, or model-based reasoning to solve and produce an explanation for. In spite of these exams being taken by millions of students each year, elementary students tend not to be fast or voluminous readers by adult standards, making this a surprisingly low-resource domain for grade-appropriate study guides and other materials. The questions also tend to require world knowledge expressed in grade-appropriate language (like that bears have fur and that fur keeps animals warm) to

#### Relevance 1437

Label: 

#### Passage 1438

Retrieved by: BM25

> Finally, we examine the growth of the tablestore as it relates to the number of questions in the corpus. Figure 6 shows a monte-carlo simulation of the number of unique tablestore rows required to author explanations for specific corpus sizes. This relationship is strongly correlated (R=0.99) with an exponential proportional decrease. For this elementary science corpus, this asymptotes at approximately 6,000 unique table rows, and 10,000 questions, providing an estimate of the upper-bound of knowledge required in this domain, and the number of unique questions that can be generated within the scope of the elementary science curriculum.
> 
> The caveat to this estimate is that it estimates the knowledge required for elementary science exams as they currently exist, with the natural level of variation introduced by the test designers. Questions are naturally grounded in examples, such as “Which part of an oak tree is responsible for undertaking photosynthesis?” (Answer: the leaves). While the corpus often contains a number of variations of a given question that test the same curriculum topic and have similar explanations, many more variations on these questions are possible that ground the question in different examples, like orchids, peach trees, or other plants. As such, while we believe that these estimates likely cover the core knowledge of the domain, many times that knowledge would be required to make the explanation tablestore robust to small variations in the presentation of those existing exam questions, or to novel unseen questions.

#### Relevance 1438

Label: 

### Dense

#### Passage 1440

Retrieved by: Dense

> to shared lexical overlap, incomplete word-sense disambiguation, or other noisy signals (e.g. erroneously aggregating a sentence about Apple computers to an inference when working to determine whether apples are a kind of fruit). In a generating a corpus of natural-language explanations for 432 elementary science questions, Jansen et al. jansen2016:COLING found that the average question requires aggregating 4 separate pieces of knowledge to explainably answer, with some questions requiring much longer explanations.
> 
> Though few QA solvers explicitly report the aggregation limits of their algorithms, Fried et al. fried2015higher, Khabashi et al. Khashabi:2016TableILP and Jansen et al. jansen2017framing appear to show limits or substantial decreases in performance after aggregating two pieces of knowledge. To the best of our knowledge, of systems that use information aggregation, only Jansen et al. jansen2017framing explicitly rate the explanatory performance of the justifications from their model, with good explanations generated for only 60% of correctly answered questions. Taken together, all of this suggests that performance on information aggregation and explainable question answering is still far from human performance, and could substantially benefit from a large corpus of training data for these tasks.

#### Relevance 1440

Label: 

#### Passage 1441

Retrieved by: Dense

> Here we characterize three properties of the explanation corpus as they relate to developing methods of explainable inference: knowledge frequency, explanation overlap, and tablestore growth.

#### Relevance 1441

Label: 

### Hybrid

#### Passage 1443

Retrieved by: Hybrid

> For a given question, annotators identified the central concept the question was testing, as well as the inference required to correctly answer the question, then began progressively constructing the explanation graph. Sentences in the graph were added by querying the tablestore based on keywords, which retrieved both single sentences/table rows, as well as entire explanations that had been previously annotated. If any knowledge required to build an explanation did not exist in the tablestore, this was added to an appropriate table, then added to the explanation.
> 
> New tables were regularly added, most commonly for property knowledge surrounding a particular topic (e.g. whether a particular material is recyclable). Because explanations are stored as lists of unique identifiers to table rows, tables and table rows could regularly be refactored, elaborated, or entirely reorganized without requiring existing explanations to be rewritten. We found this was critical for consistency and ensuring good organization throughout corpus construction.
> 
> One of the central difficulties with evaluating explanation authoring is determining metrics for interannotator agreement, as many correct explanations are possible for a given question, and there are many different wordings that an annotator might choose to express a given piece of knowledge in the tablestore. Similarly, the borders between different levels of explanatory depth are fuzzy, suggesting that one annotator may express their explanation with more or less specificity than another.
> 
> To address these difficulties we included two methods to increase consistency. First, as a passive intervention during the explanation generation process, annotators are presented with existing explanations that can be drawn from to compose a new explanation, where these existing explanations share many of the same query terms being used to construct the new explanation. Second, as an active intervention, each explanation goes through four review passes to ensure consistency. The first two passes are completed by the original annotator, before checking a flag on the annotation tool signifying that the question is ready for external review. A second annotator then checks the question for completeness and consistency with existing explanations, and composes a list of suggested edits and revisions. The fourth and final pass is completed by the original annotator, who implements these suggested revisions. This review process is expensive,

#### Relevance 1443

Label: 

## Question 0190

Paper: Method for Aspect-Based Sentiment Annotation Using Rhetorical Analysis

> what domain do the opinions fall under?

### Common Retrieved Chunks

#### Passage 1444

Retrieved by: BM25, Dense, Hybrid

> A sentiment analysis can be made at the level of (1) the whole document, (2) the individual sentences, or (what is currently seen as the most attractive approach) (3) at the level of individual fragments of text. Regarding document level analysis BIBREF8 , BIBREF9 - the task at this level is to classify whether a full opinion expresses a positive, negative or neutral attitude. For example, given a product review, the model determines whether the text shows an overall positive, negative or neutral opinion about the product. The biggest disadvantage of document level analysis is an assumption that each document expresses views on a single entity. Thus, it is not applicable to documents which evaluate or compare multiple objects. As for sentence level analysis BIBREF10 - The task at this level relates to sentences and determines whether each sentence expressed a positive, negative, or neutral opinion. This level of analysis is closely related to subjectivity classification which distinguishes sentences (called objective sentences) that express factual information from sentences (called subjective sentences) that express subjective views and opinions. However, we should note that subjectivity is not equivalent to sentiment as many objective sentences can imply opinions. With feature/aspect level analysis BIBREF11 - both the document level and the sentence level analyses do not discover what exactly people liked and did not like. A finer-grained analysis can be performed at aspect level. Aspect level was earlier called feature/aspect level. Instead of looking at language constructs (documents, paragraphs, sentences, clauses or phrases), aspect level directly looks at the opinion itself. It is based on the idea that an opinion consists of a sentiment (positive or negative) and a target (of opinion). As a result, we can aggregate the opinions. For example, the phone display gathers positive feedback, but the battery is often rated negatively. The aspect-based level of analysis is much more complex since it requires more advanced knowledge representation than at the level of entire documents only. Also, the documents often consist of multiple sentences, so saying that the document is positive provides only partial information. In the literature, there exists some initial work related to aspects. There exist initial solutions that use SVM-based algorithms BIBREF12 or

#### Relevance 1444

Label: 

#### Passage 1446

Retrieved by: BM25, Dense, Hybrid

> Rhetorical analysis seeks to uncover the coherence structure underneath the text, which has been shown to be beneficial for many Natural Language Processing (NLP) applications including text summarization and compression BIBREF1 , machine translation evaluation BIBREF2 , sentiment analysis BIBREF3 , and others. Different formal theories of discourse analysis have been proposed. Martin BIBREF4 proposed discourse relations based on discourse connectives (e.g., because, but) expressed in the text. Danlos BIBREF5 extended sentence grammar and formalize discourse structure. Rhetorical Structure Theory or RST - used in our experiments - was proposed by Mann and Thompson BIBREF6 . The method proposed by them is perhaps the most influential theory of discourse in computational linguistics. Moreover, it was initially intended to be used in text generation tasks, but it became popular for parsing the structure of a text BIBREF7 . Rhetorical Structure Theory represents texts by hierarchical structures with labels. This is a tree structure, which comprises Discourse Trees (DTs). Presented at Figure FIGREF3 this Discourse Tree is a representation of the following text:
> 
> The goal of discourse analysis in our method is the segmentation of the text for the basic units of discourse structures EDU (Elementary Discourse Units) and connecting them to determine semantic relations. The analysis is performed separately for each source document, and as the output we get Discourse Trees (DT) such as in Figure FIGREF3 . At this stage, existing discourse parsers will model the structure and the labels of a DT separately. They do not take into account the sequential dependencies between the DT constituents. Then existing discourse parsers will apply greedy and sub-optimal parsing algorithms and build a Discourse Tree. During this stage, and to cope with the mentioned limitation The inferred (posterior) probabilities can be used from CRF parsing models in a probabilistic CKY-like bottom-up parsing algorithm BIBREF14 which is non-greedy and optimal. Finally, discourse parsers do not discriminate between intra-sentential parsing (i.e., building the DTs for individual sentences) and multi-sentential parsing (i.e., building a DT for the whole document) BIBREF0 . Hence, this part of the analysis will extract for us distributed information about the relationship between different EDUs from parsed texts. Then we assign sentiment orientation to each EDU.

#### Relevance 1446

Label: 

#### Passage 1447

Retrieved by: BM25, Dense, Hybrid

> Modern society is an information society bombarded from all sides by an increasing number of different pieces of information. The 21st century has brought us the rapid development of media, especially in the internet ecosystem. This change has caused the transfer of many areas of our lives to virtual reality. New forms of communication have been established. Their development has created the need for analysis of related data. Nowadays, unstructured information is available in digital form, but how can we analyse and summarise billions of newly created texts that appear daily on the internet? Natural language analysis techniques, statistics and machine learning have emerged as tools to help us. In recent years, particular attention has focused on sentiment analysis. This area is defined as the study of opinions expressed by people as well as attitudes and emotions about a particular topic, product, event, or person. Sentiment analysis determines the polarisation of the text. It answers the question as to whether a particular text is a positive, negative, or neutral one.
> 
> Our goal is to build a comprehensive set of techniques for preparing and analysing texts containing opinions and generating user-friendly descriptive reports in natural language - Figure FIGREF1 . In this paper, we describe briefly the whole workflow and present a prototype implementation. Currently, existing solutions for sentiment annotation offer mostly analysis on the level of entire documents, and if you go deeper to the level of individual product features, they are only superficial and poorly prepared for the analysis of large volumes of data. This can especially be seen in scientific articles where the analysis is carried out on a few hundred reviews only. It is worth mentioning that this task is extremely problematic because of the huge diversity of languages and the difficulty of building a single solution that can cover all the languages used in the world. Natural language analysis often requires additional pre-processing steps, especially at the stage of preparing the data for analysis, and steps specific for each language. Large differences can be seen in the analysis of the Polish language (a highly inflected language) and English (a grammatically simpler one). We propose a solution that will cover several languages,

#### Relevance 1447

Label: 

#### Passage 1449

Retrieved by: Dense, Hybrid

> We implemented our framework in Python. The first computational step was to load the dataset and parse it into individual documents. Next, each document was processed through the Discourse Parser BIBREF18 and transformed into a Discourse Tree (DT). Then we extracted Elementary Discourse Units (EDUs) from the DT and each EDU was processed through the Logistic Regression sentiment algorithm. All neutral EDUs were taken off from consideration to ensure that the discovered aspects are correlated with authors' emotions. The remaining EDUs were processed through part-of-speech tagger to extract nouns and noun phrases which we decided to treat as potential aspects. The result of this step was a set of Aspect-based Discourse Trees (ADTs). Then, from each ADT relations between aspects were extracted using breadth-first search, and an Aspect-Rhetorical Relation Graph (ARRG) was created by using aspects and relations such as nodes and edges respectively. Next, we evaluated the importance of aspects using a PageRank algorithm. Our approach resulted in complete list of aspects sorted by PageRank score. We applied a user-selected importance threshold to filter trivial aspects.

#### Relevance 1449

Label: 

### BM25

#### Passage 1445

Retrieved by: BM25

> The work was partially supported by the National Science Centre grants DEC-2016/21/N/ST6/02366 and DEC-2016/21/D/ST6/02948, and from the European Union’s Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No 691152 (RENOIR project).

#### Relevance 1445

Label: 

#### Passage 1448

Retrieved by: BM25

> In Table TABREF18 there are presented some examples of the results of our approach compared with the annotated data from Bing Liu's dataset. In the first sentence, the results of the analysis differ because we decided to treat only nouns or noun phrases as aspects, while annotators also accepted verbs. In some cases, such as sentences 2 or 4, our approach generated more valuable aspects than the annotators found, but in some cases, like sentence 5, we found fewer. This is possibly the result of our method of filtering valuable aspects - if some aspects were not frequent enough in the dataset, we can treat them as void. In cases where there is neither aspect nor sentiment in the dataset, such as sentence 6, we measure sentiment as well, as one of our analysis steps.
> 
> Figure FIGREF19 shows the agreement between our aspects and that of the dataset. We assumed two aspects as equal when they were textually the same. We made some experiments using text distance metrics, such as the Jaro-Winkler distance, but the results did not differ significantly from an exact matching. We fitted the importance factor value (on the X axis) so as to enrich final aspects set: a higher factor resulted in a larger aspects set and a higher value of precision metric, with slowly decreasing recall. First results (blue line on charts) were not satisfactory, so we removed a sentiment filtering step of analysis (orange line on chart), which doubled the precision value, with nearly the same value of recall. The level of precision for whole dataset (computer, router, and speaker) was most of the time at the same level. However, the recall of router was significantly worse than speaker and computer sets.

#### Relevance 1448

Label: 

### Dense

#### Passage 1450

Retrieved by: Dense

> We have proposed a comprehensive flow of analysing aspects and assigning sentiment orientation to them. The advantages of such an analysis are that: it is a grammatically-based and coherent solution, it shows opinion distribution, it doesn't need any aspect ontology, it is not limited to the number of aspects and really important, it doesn't need training data (unsupervised method). The method proved it has a big potential in generating summary overviews for aspect and sentiment distribution across analysed documents. In our next steps, we want to improve the aspect extraction phase, probably using neural network approaches. Moreover, we want to expand the analysis of the Polish language.

#### Relevance 1450

Label: 

### Hybrid

#### Passage 1451

Retrieved by: Hybrid

> The proposed Rhetorical and Sentiment Analysis flow is divided into four main tasks:
> 
> The overall characteristics and flow organisation can be seen in Figure FIGREF9 . Each of the mentioned steps of the proposed method is described in the following subsections.

#### Relevance 1451

Label: 

## Question 0191

Paper: Text Summarization with Pretrained Encoders

> What is novel about their document-level encoder?

### Common Retrieved Chunks

#### Passage 1453

Retrieved by: BM25, Dense, Hybrid

> Language model pretraining has advanced the state of the art in many NLP tasks ranging from sentiment analysis, to question answering, natural language inference, named entity recognition, and textual similarity. State-of-the-art pretrained models include ELMo BIBREF1, GPT BIBREF2, and more recently Bidirectional Encoder Representations from Transformers (Bert; BIBREF0). Bert combines both word and sentence representations in a single very large Transformer BIBREF3; it is pretrained on vast amounts of text, with an unsupervised objective of masked language modeling and next-sentence prediction and can be fine-tuned with various task-specific objectives.
> 
> In most cases, pretrained language models have been employed as encoders for sentence- and paragraph-level natural language understanding problems BIBREF0 involving various classification tasks (e.g., predicting whether any two sentences are in an entailment relationship; or determining the completion of a sentence among four alternative sentences). In this paper, we examine the influence of language model pretraining on text summarization. Different from previous tasks, summarization requires wide-coverage natural language understanding going beyond the meaning of individual words and sentences. The aim is to condense a document into a shorter version while preserving most of its meaning. Furthermore, under abstractive modeling formulations, the task requires language generation capabilities in order to create summaries containing novel words and phrases not featured in the source text, while extractive summarization is often defined as a binary classification task with labels indicating whether a text span (typically a sentence) should be included in the summary.
> 
> We explore the potential of Bert for text summarization under a general framework encompassing both extractive and abstractive modeling paradigms. We propose a novel document-level encoder based on Bert which is able to encode a document and obtain representations for its sentences. Our extractive model is built on top of this encoder by stacking several inter-sentence Transformer layers to capture document-level features for extracting sentences. Our abstractive model adopts an encoder-decoder architecture, combining the same pretrained Bert encoder with a randomly-initialized Transformer decoder BIBREF3. We design a new training schedule which separates the optimizers of the encoder and the decoder in order to accommodate the fact that the former is pretrained while the latter must be trained from scratch. Finally, motivated by previous work showing that

#### Relevance 1453

Label: 

#### Passage 1454

Retrieved by: BM25, Dense, Hybrid

> In this paper, we showcased how pretrained Bert can be usefully applied in text summarization. We introduced a novel document-level encoder and proposed a general framework for both abstractive and extractive summarization. Experimental results across three datasets show that our model achieves state-of-the-art results across the board under automatic and human-based evaluation protocols. Although we mainly focused on document encoding for summarization, in the future, we would like to take advantage the capabilities of Bert for language generation.

#### Relevance 1454

Label: 

#### Passage 1456

Retrieved by: BM25, Hybrid

> Although Bert has been used to fine-tune various NLP tasks, its application to summarization is not as straightforward. Since Bert is trained as a masked-language model, the output vectors are grounded to tokens instead of sentences, while in extractive summarization, most models manipulate sentence-level representations. Although segmentation embeddings represent different sentences in Bert, they only apply to sentence-pair inputs, while in summarization we must encode and manipulate multi-sentential inputs. Figure FIGREF2 illustrates our proposed Bert architecture for Summarization (which we call BertSum).
> 
> In order to represent individual sentences, we insert external [cls] tokens at the start of each sentence, and each [cls] symbol collects features for the sentence preceding it. We also use interval segment embeddings to distinguish multiple sentences within a document. For $sent_i$ we assign segment embedding $E_A$ or $E_B$ depending on whether $i$ is odd or even. For example, for document $[sent_1, sent_2, sent_3, sent_4, sent_5]$, we would assign embeddings $[E_A, E_B, E_A,E_B, E_A]$. This way, document representations are learned hierarchically where lower Transformer layers represent adjacent sentences, while higher layers, in combination with self-attention, represent multi-sentence discourse.
> 
> Position embeddings in the original Bert model have a maximum length of 512; we overcome this limitation by adding more position embeddings that are initialized randomly and fine-tuned with other parameters in the encoder.

#### Relevance 1456

Label: 

#### Passage 1457

Retrieved by: Dense, Hybrid

> We use a standard encoder-decoder framework for abstractive summarization BIBREF6. The encoder is the pretrained BertSum and the decoder is a 6-layered Transformer initialized randomly. It is conceivable that there is a mismatch between the encoder and the decoder, since the former is pretrained while the latter must be trained from scratch. This can make fine-tuning unstable; for example, the encoder might overfit the data while the decoder underfits, or vice versa. To circumvent this, we design a new fine-tuning schedule which separates the optimizers of the encoder and the decoder.
> 
> We use two Adam optimizers with $\beta _1=0.9$ and $\beta _2=0.999$ for the encoder and the decoder, respectively, each with different warmup-steps and learning rates:
> 
> where $\tilde{lr}_{\mathcal {E}}=2e^{-3}$, and $\operatorname{\operatorname{warmup}}_{\mathcal {E}}=20,000$ for the encoder and $\tilde{lr}_{\mathcal {D}}=0.1$, and $\operatorname{\operatorname{warmup}}_{\mathcal {D}}=10,000$ for the decoder. This is based on the assumption that the pretrained encoder should be fine-tuned with a smaller learning rate and smoother decay (so that the encoder can be trained with more accurate gradients when the decoder is becoming stable).
> 
> In addition, we propose a two-stage fine-tuning approach, where we first fine-tune the encoder on the extractive summarization task (Section SECREF8) and then fine-tune it on the abstractive summarization task (Section SECREF13). Previous work BIBREF4, BIBREF23 suggests that using extractive objectives can boost the performance of abstractive summarization. Also notice that this two-stage approach is conceptually very simple, the model can take advantage of information shared between these two tasks, without fundamentally changing its architecture. We name the default abstractive model BertSumAbs and the two-stage fine-tuned model BertSumExtAbs.

#### Relevance 1457

Label: 

#### Passage 1458

Retrieved by: Dense, Hybrid

> Let $d$ denote a document containing sentences $[sent_1, sent_2, \cdots , sent_m]$, where $sent_i$ is the $i$-th sentence in the document. Extractive summarization can be defined as the task of assigning a label $y_i \in \lbrace 0, 1\rbrace $ to each $sent_i$, indicating whether the sentence should be included in the summary. It is assumed that summary sentences represent the most important content of the document.
> 
> With BertSum, vector $t_i$ which is the vector of the $i$-th [cls] symbol from the top layer can be used as the representation for $sent_i$. Several inter-sentence Transformer layers are then stacked on top of Bert outputs, to capture document-level features for extracting summaries:
> 
> where $h^0=\mathrm {PosEmb}(T)$; $T$ denotes the sentence vectors output by BertSum, and function $\mathrm {PosEmb}$ adds sinusoid positional embeddings BIBREF3 to $T$, indicating the position of each sentence.
> 
> The final output layer is a sigmoid classifier:
> 
> where $h^L_i$ is the vector for $sent_i$ from the top layer (the $L$-th layer ) of the Transformer. In experiments, we implemented Transformers with $L=1, 2, 3$ and found that a Transformer with $L=2$ performed best. We name this model BertSumExt.
> 
> The loss of the model is the binary classification entropy of prediction $\hat{y}_i$ against gold label $y_i$. Inter-sentence Transformer layers are jointly fine-tuned with BertSum. We use the Adam optimizer with $\beta _1=0.9$, and $\beta _2=0.999$). Our learning rate schedule follows BIBREF3 with warming-up ($ \operatorname{\operatorname{warmup}}=10,000$):

#### Relevance 1458

Label: 

### BM25

#### Passage 1452

Retrieved by: BM25

> contains 226,711 news articles accompanied with a one-sentence summary, answering the question “What is this article about?”. We used the splits of BIBREF22 for training, validation, and testing (204,045/11,332/11,334) and followed the pre-processing introduced in their work. Input documents were truncated to 512 tokens.
> 
> Aside from various statistics on the three datasets, Table TABREF12 also reports the proportion of novel bi-grams in gold summaries as a measure of their abstractiveness. We would expect models with extractive biases to perform better on datasets with (mostly) extractive summaries, and abstractive models to perform more rewrite operations on datasets with abstractive summaries. CNN/DailyMail and NYT are somewhat abstractive, while XSum is highly abstractive.

#### Relevance 1452

Label: 

#### Passage 1455

Retrieved by: BM25

> We also analyzed the output of abstractive systems by calculating the proportion of novel n-grams that appear in the summaries but not in the source texts. The results are shown in Figure FIGREF33. In the CNN/DailyMail dataset, the proportion of novel n-grams in automatically generated summaries is much lower compared to reference summaries, but in XSum, this gap is much smaller. We also observe that on CNN/DailyMail, BertExtAbs produces less novel n-ngrams than BertAbs, which is not surprising. BertExtAbs is more biased towards selecting sentences from the source document since it is initially trained as an extractive model. The supplementary material includes examples of system output and additional ablation studies.

#### Relevance 1455

Label: 

### Dense

#### Passage 1459

Retrieved by: Dense

> a new training schedule which separates the optimizers of the encoder and the decoder in order to accommodate the fact that the former is pretrained while the latter must be trained from scratch. Finally, motivated by previous work showing that the combination of extractive and abstractive objectives can help generate better summaries BIBREF4, we present a two-stage approach where the encoder is fine-tuned twice, first with an extractive objective and subsequently on the abstractive summarization task.
> 
> We evaluate the proposed approach on three single-document news summarization datasets representative of different writing conventions (e.g., important information is concentrated at the beginning of the document or distributed more evenly throughout) and summary styles (e.g., verbose vs. more telegraphic; extractive vs. abstractive). Across datasets, we experimentally show that the proposed models achieve state-of-the-art results under both extractive and abstractive settings. Our contributions in this work are three-fold: a) we highlight the importance of document encoding for the summarization task; a variety of recently proposed techniques aim to enhance summarization performance via copying mechanisms BIBREF5, BIBREF6, BIBREF7, reinforcement learning BIBREF8, BIBREF9, BIBREF10, and multiple communicating encoders BIBREF11. We achieve better results with a minimum-requirement model without using any of these mechanisms; b) we showcase ways to effectively employ pretrained language models in summarization under both extractive and abstractive settings; we would expect any improvements in model pretraining to translate in better summarization in the future; and c) the proposed models can be used as a stepping stone to further improve summarization performance as well as baselines against which new proposals are tested.

#### Relevance 1459

Label: 

### Hybrid

None

## Question 0192

Paper: Semantic Web for Machine Translation: Challenges and Directions

> What are the opportunities presented by the use of Semantic Web technologies in Machine Translation?

### Common Retrieved Chunks

#### Passage 1460

Retrieved by: BM25, Dense, Hybrid

> data at Web scale. Presently, these approaches have begun to address the drawbacks of rule-based approaches. However, some problems that had already been solved for linguistics based methods reappeared. The majority of these problems are connected to the issue of ambiguity, including syntactic and semantic variations BIBREF0 . Nowadays, a novel SMT paradigm has arisen called NMT which relies on NN algorithms. NMT has been achieving impressive results and is now the state-of-the-art in MT approaches. However, NMT is still a statistical approach sharing some semantic drawbacks from other well-defined SMT approaches BIBREF5 .
> 
> One possible solution to address the remaining issues of MT lies in the use of SWT, which have emerged over recent decades as a paradigm to make the semantics of content explicit so that it can be used by machines. It is believed that explicit semantic knowledge made available through these technologies can empower MT systems to supply translations with significantly better quality while remaining scalable. In particular, the disambiguated knowledge about real-world entities, their properties and their relationships made available on the LD Web can potentially be used to infer the right meaning of ambiguous sentences or words.
> 
> According to our survey BIBREF6 , the obvious opportunity of using SWT for MT has already been studied by a number of approaches, especially w.r.t. the issue of ambiguity. In this paper, we present the challenges and opportunities in the use of SWT in MT for translating texts.

#### Relevance 1460

Label: 

#### Passage 1461

Retrieved by: BM25, Hybrid

> output often has poor quality, immediately deteriorating the target text readability. Therefore, we suggest recognizing such entities before the translation process and first linking them to a reference knowledge base. Afterwards, the type of entities would be agglutinated along with their labels and their translations from a reference knowledge base. For instance, in NMT, the idea is to include in the training set for the aforementioned word “Kiwi", “Kiwi.animal.link, Kiwi.person.link, Kiwi.food.link" then finally to align them with the translations in the target text. For example, in SMT, the additional information can be included by XML or by an additional model. In contrast, in NMT, this additional information can be used as parameters in the training phase. This method would also contribute to OOV mistakes regarding names. This idea is supported by BIBREF11 where the authors encoded the types of entities along with the words to improve the translation of sentences between Chinese-English. Recently, Moussallem et al. BIBREF15 have shown promising results by applying a multilingual entity linking algorithm along with knowledge graph embeddings into the translation phase of a neural machine translation model for improving the translation of entities in texts. Their approach achieved significant and consistent improvements of +3 BLEU, METEOR and CHRF3 on average on the newstest datasets between 2014 and 2018 for WMT English-German translation task.
> 
> Non-standard speech. The non-standard language problem is a rather important one in the MT field. Many people use the colloquial form to speak and write to each other on social networks. Thus, when MT systems are applied on this context, the input text frequently contains slang, MWE, and unreasonable abbreviations such as “Idr = I don't remember.” and “cya = see you”. Additionally, idioms contribute to this problem, decreasing the translation quality. Idioms often have an entirely different meaning than their separated word meanings. Consequently, most translation outputs of such expressions contain errors. For a good translation, the MT system needs to recognize such slang and try to map it to the target language. Some SMT systems like Google or Bing have recognition patterns over non-standard speech from old translations through the Web using SMT approaches. In rare cases SMT can solve this problem, but considering

#### Relevance 1461

Label: 

#### Passage 1463

Retrieved by: BM25, Hybrid

> real benefit of SW comes from its capacity to provide unseen knowledge about emergent data, which appears every day. Therefore, we suggest performing the topic-modelling technique over the source text to provide a necessary context before translation. Instead of applying the topic-modeling over the entire text, we would follow the principle of communication (i.e from 3 to 5 sentences for describing an idea and define a context for each piece of text. Thus, at the execution of a translation model in a given SMT, we would focus on every word which may be a homonymous or polysemous word. For every word which has more than one translation, a SPARQL query would be required to find the best combination in the current context. Thus, at the translation phase, the disambiguation algorithm could search for an appropriate word using different SW resources such as DBpedia, in consideration of the context provided by the topic modelling. The goal is to exploit the use of more than one SW resource at once for improving the translation of ambiguous terms. The use of two or more SW resources simultaneously has not yet been investigated.
> 
> On the other hand, there is also a syntactic disambiguation problem which as yet lacks good solutions. For instance, the English language contains irregular verbs like “set” or “put”. Depending on the structure of a sentence, it is not possible to recognize their verbal tense, e.g., present or past tense. Even statistical approaches trained on huge corpora may fail to find the exact meaning of some words due to the structure of the language. Although this challenge has successfully been dealt with since NMT has been used for European languages, implementations of NMT for some non-European languages have not been fully exploited (e.g., Brazilian Portuguese, Latin-America Spanish, Zulu, Hindi) due to the lack of large bilingual data sets on the Web to be trained on. Thus, we suggest gathering relationships among properties within an ontology by using the reasoning technique for handling this issue. For instance, the sentence “Anna usually put her notebook on the table for studying" may be annotated using a certain vocabulary and represented by triples. Thus, the verb “put", which is represented

#### Relevance 1463

Label: 

#### Passage 1464

Retrieved by: BM25, Dense, Hybrid

> Alongside increasing globalization comes a greater need for readers to understand texts in languages foreign to them. For example, approximately 48% of the pages on the Web are not available in English. The technological progress of recent decades has made both the distribution and access to content in different languages ever simpler. Translation aims to support users who need to access content in a language in which they are not fluent BIBREF0 .
> 
> However, translation is a difficult task due to the complexity of natural languages and their structure BIBREF0 . In addition, manual translation does not scale to the magnitude of the Web. One remedy for this problem is MT. The main goal of MT is to enable people to assess content in languages other than the languages in which they are fluent BIBREF1 . From a formal point of view, this means that the goal of MT is to transfer the semantics of text from an input language to an output language BIBREF2 .
> 
> Although MT systems are now popular on the Web, they still generate a large number of incorrect translations. Recently, Popović BIBREF3 has classified five types of errors that still remain in MT systems. According to research, the two main faults that are responsible for 40% and 30% of problems respectively, are reordering errors and lexical and syntactic ambiguity. Thus, addressing these barriers is a key challenge for modern translation systems. A large number of MT approaches have been developed over the years that could potentially serve as a remedy. For instance, translators began by using methodologies based on linguistics which led to the family of RBMT. However, RBMT systems have a critical drawback in their reliance on manually crafted rules, thus making the development of new translation modules for different languages even more difficult.
> 
> SMT and EBMT were developed to deal with the scalability issue in RBMT BIBREF4 , a necessary characteristic of MT systems that must deal with data at Web scale. Presently, these approaches have begun to address the drawbacks of rule-based approaches. However, some problems that had already been solved for linguistics based methods reappeared. The majority of these problems are connected to the issue of

#### Relevance 1464

Label: 

#### Passage 1465

Retrieved by: Dense, Hybrid

> Based on the surveyed works on our research BIBREF6 , SWT have mostly been applied at the semantic analysis step, rather than at the other stages of the translation process, due to their ability to deal with concepts behind the words and provide knowledge about them. As SWT have developed, they have increasingly been able to resolve some of the open challenges of MT. They may be applied in different ways according to each MT approach.
> 
> Disambiguation. Human language is very ambiguous. Most words have multiple interpretations depending on the context in which they are mentioned. In the MT field, WSD techniques are concerned with finding the respective meaning and correct translation to these ambiguous words in target languages. This ambiguity problem was identified early in MT development. In 1960 Bar-Hillel BIBREF1 stated that an MT system is not able to find the right meaning without a specific knowledge. Although the ambiguity problem has been lessened significantly since the contribution of Carpuat and subsequent works BIBREF13 , this problem still remains a challenge. As seen in Moussallem et al. BIBREF6 , MT systems still try to resolve this problem by using domain specific language models to prefer domain specific expressions, but when translating a highly ambiguous sentence or a short text which covers multiple domains, the languages models are not enough.
> 
> SW has already shown its capability for semantic disambiguation of polysemous and homonymous words. However, SWT were applied in two ways to support the semantic disambiguation in MT. First, the ambiguous words were recognized in the source text before carrying out the translation, applying a pre-editing technique. Second, SWT were applied to the output translation in the target language as a post-editing technique. Although applying one of these techniques has increased the quality of a translation, both techniques are tedious to implement when they have to translate common words instead of named entities, then be applied several times to achieve a successful translation.
> 
> The real benefit of SW comes from its capacity to provide unseen knowledge about emergent data, which appears every day. Therefore, we suggest performing the topic-modelling technique over the source text to provide a necessary context before translation. Instead of applying

#### Relevance 1465

Label: 

### BM25

#### Passage 1462

Retrieved by: BM25

> provided by the German Wikipedia version are not contained in the Portuguese one. Therefore, the semantic structure (i.e., triples) provided by DBpedia versions of these respective Wikipedia versions would be able to help translate from German to Portuguese. For example, the terms contained in triples would be translated to a given target language using a dictionary containing domain words. This dictionary may be acquired in two different ways. First, by performing localisation, as in the work by J. P. McCrae BIBREF17 which translates the terms contained in a monolingual ontology, thus generating a bilingual ontology. Second, by creating embeddings of both DBpedia versions in order to determine the similarity between entities through their vectors. This insight is supported by some recent works, such as Ristoski et al. BIBREF18 , which creates bilingual embeddings using RDF based on Word2vec algorithms. Therefore, we suggest investigating an MT approach mainly based on SWT using NN for translating KBs. Once the KBs are translated, we suggest including them in the language models for improving the translation of entities.
> 
> Besides C. Shi et al BIBREF11 , Arčan and Buitelaar BIBREF19 presented an approach to translate domain-specific expressions represented by English KBs in order to make the knowledge accessible for other languages. They claimed that KBs are mostly in English, therefore they cannot contribute to the problem of MT to other languages. Thus, they translated two KBs belonging to medical and financial domains, along with the English Wikipedia, to German. Once translated, the KBs were used as external resources in the translation of German-English. The results were quite appealing and the further research into this area should be undertaken. Recently, Moussallem et al BIBREF20 created THOTH, an approach which translates and enriches knowledge graphs across languages. Their approach relies on two different recurrent neural network models along with knowledge graph embeddings. The authors applied their approach on the German DBpedia with the German translation of the English DBpedia on two tasks: fact checking and entity linking. THOTH showed promising results with a translation accuracy of 88.56 while being capable of improving two NLP tasks with its enriched-German KG .

#### Relevance 1462

Label: 

### Dense

#### Passage 1466

Retrieved by: Dense

> The most problematic unresolved MT challenges, from our point of view, which are still experienced by the aforementioned MT approaches are the following:
> 
> Additionally, there are five MT open challenges posed by Lopez and Post BIBREF12 which we describe more generically below.
> 
> (1) Excessive focus on English and European languages as one of the involved languages in MT approaches and poor research on low-resource language pairs such as African and/or South American languages. (2) The limitations of SMT approaches for translating across domains. Most MT systems exhibit good performance on law and the legislative domains due to the large amount of data provided by the European Union. In contrast, translations performed on sports and life-hacks commonly fail, because of the lack of training data. (3) How to translate the huge amount of data from social networks that uniquely deal with no-standard speech texts from users (e.g., tweets). (4) The difficult translations among morphologically rich languages. This challenge shares the same problem with the first one, namely that most research work focuses on English as one of the involved languages. Therefore, MT systems which translate content between, for instance, Arabic and Spanish are rare. (5) For the speech translation task, the parallel data for training differs widely from real user speech.
> 
> The challenges above are clearly not independent, which means that addressing one of them can have an impact on the others. Since NMT has shown impressive results on reordering, the main problem turns out to be the disambiguation process (both syntactically and semantically) in SMT approaches BIBREF0 .

#### Relevance 1466

Label: 

#### Passage 1467

Retrieved by: Dense

> In this extended abstract, we detailed the results of a systematic literature review of MT using SWT for improving the translation of natural language sentences. Our goal was to present the current open MT translation problems and how SWT can address these problems and enhance MT quality. Considering the decision power of SWT, they cannot be ignored by future MT systems. As a next step, we intend to continue elaborating a novel MT approach which is capable of simultaneously gathering knowledge from different SW resources and consequently being able to address the ambiguity of named entities and also contribute to the OOV words problem. This insight relies on our recent works, such as BIBREF15 , which have augmented NMT models with the usage of external knowledge for improving the translation of entities in texts. Additionally, future works that can be expected from fellow researchers, include the creation of multilingual linguistic ontologies describing the syntax of rich morphologically languages for supporting MT approaches. Also, the creation of more RDF multilingual dictionaries which can improve some MT steps, such as alignment.

#### Relevance 1467

Label: 

### Hybrid

None

## Question 0193

Paper: A Neural Approach to Irony Generation

> What experiments are conducted?

### Common Retrieved Chunks

#### Passage 1468

Retrieved by: BM25, Dense, Hybrid

> Although our model outperforms other style transfer baselines according to automatic and human evaluation results, there are still some failure cases because irony generation is still a very challenging task. We would like to share the issues we meet during our experiments and our solutions to some of them in this section.
> 
> No Change: As mentioned above, many style transfer models, such as DualRL, tend to make few changes to the input sentence and output the same sentence. Actually, this is a common issue for unsupervised style transfer systems and we also meet it during our experiments. The main reason for the issue is that rewards for content preservation are too prominent and rewards for style accuracy cannot work well. In contrast, in order to guarantee the readability and fluency of the output sentence, we also cannot emphasize too much on rewards for style accuracy because it may cause some other issues such as word repetition mentioned below. A method to solve the problem is tuning hyperparameters and this is also the method we implement in this work. As for content preservation, maybe MLE methods such as back-translation are not enough because they tend to force models to generate specific words. In the future, we should further design some more suitable methods to control content preservation for models without disentangling style and content representations, such as DualRL and ours.
> 
> Word Repetition: During our experiments, we observe that some of the outputs prefer to repeat the same word as shown in Table TABREF38 . This is because reinforcement learning rewards encourage the model to generate words which can get high scores from classifiers and even back-translation cannot stop it. Our solution is that we can lower the probability of decoding a word in decoders if the word has been generated in the previous time steps during testing. We also try to implement this method during training time but obtain worse performances because it may limit the effects of training. Some previous studies utilize language models to control the fluency of the output sentence and we also try this method. Nonetheless, pre-training a language model with tweets and using it to generate rewards is difficult because tweets

#### Relevance 1468

Label: 

#### Passage 1469

Retrieved by: BM25, Hybrid

> In this section, we describe some additional experiments on the transformation from ironic sentences to non-ironic sentences. Sometimes ironies are hard to understand and may cause misunderstanding, for which our task also explores the transformation from ironic sentences to non-ironic sentences.
> 
> As shown in Table TABREF46 , we also conduct automatic evaluations and the conclusions are similar to those of the transformation from non-ironic sentences to ironic sentences. As for human evaluation results in Table TABREF47 , our model still can achieve the second-best results in sentiment and content preservation. Nevertheless, DualRL system and ours get poor performances in irony accuracy. The reason may be that the other four baselines tend to generate common and even not fluent sentences which are irrelevant to the input sentences and are hard to be identified as ironies. So annotators usually mark these output sentences as non-ironic sentences, which causes these models to obtain better performances than DualRL and ours but much poorer results in sentiment and content preservation. Some examples are shown in Table TABREF52 .

#### Relevance 1469

Label: 

#### Passage 1471

Retrieved by: BM25, Hybrid

> effects of training. Some previous studies utilize language models to control the fluency of the output sentence and we also try this method. Nonetheless, pre-training a language model with tweets and using it to generate rewards is difficult because tweets are more casual and have more noise. Rewards from that kind of language model are usually not accurate and may confuse the model. In the future, we should come up with better methods to model language fluency with the consideration of irony accuracy, sentiment and content preservation, especially for tweets.
> 
> Improper Words: As ironic style is hard for our model to learn, it may generate some improper words which make the sentence strange. As the example shown in the Table TABREF38 , the sentiment word in the input sentence is “wonderful" and the model should change it into a negative word such as “sad" to make the output sentence ironic. However, the model changes “friday" and “fifa" which are not related to ironic styles. We have not found a very effective method to address this issue and maybe we should further explore stronger models to learn ironic styles better.

#### Relevance 1471

Label: 

#### Passage 1475

Retrieved by: Dense, Hybrid

> In order to evaluate sentiment preservation, we use the absolute value of the difference between the standardized sentiment score of the input sentence and that of the generated sentence. We call the value as sentiment delta (senti delta). Besides, we report the sentiment accuracy (Senti ACC) which measures whether the output sentence has the same sentiment polarity as the input sentence based on our standardized sentiment classifiers. The BLEU score BIBREF25 between the input sentences and the output sentences is calculated to evaluate the content preservation performance. In order to evaluate the overall performance of different models, we also report the geometric mean (G2) and harmonic mean (H2) of the sentiment accuracy and the BLEU score. As for the irony accuracy, we only report it in human evaluation results because it is more accurate for the human to evaluate the quality of irony as it is very complicated.
> 
> We first sample 50 non-ironic input sentences and their corresponding output sentences of different models. Then, we ask four annotators who are proficient in English to evaluate the qualities of the generated sentences of different models. They are required to rank the output sentences of our model and baselines from the best to the worst in terms of irony accuracy (Irony), Sentiment preservation (Senti) and content preservation (Content). The best output is ranked with 1 and the worst output is ranked with 6. That means that the smaller our human evaluation value is, the better the corresponding model is.

#### Relevance 1475

Label: 

#### Passage 1476

Retrieved by: Dense, Hybrid

> Style Transfer: As irony is a complicated style and hard to model with some specific style attribute words, we mainly focus on studies without editing style attribute words.
> 
> Some studies are trying to disentangle style representation from content representation. In BIBREF12 , authors leverage adversarial networks to learn separate content representations and style representations. In BIBREF13 and BIBREF6 , researchers combine variational auto-encoders (VAEs) with style discriminators.
> 
> However, some recent studies BIBREF11 reveal that the disentanglement of content and style representations may not be achieved in practice. Therefore, some other research studies BIBREF9 , BIBREF10 strive to separate content and style by removing stylistic words. Nonetheless, many non-ironic sentences do not have specific stylistic words and as a result, we find it difficult to transfer non-ironic sentences to ironic sentences through this way in practice.
> 
> Besides, some other research studies do not disentangle style from content but directly learn representations of sentences. In BIBREF8 , authors propose a dual reinforcement learning framework without separating content and style representations. In BIBREF7 , researchers utilize a machine translation model to learn a sentence representation preserving the meaning of the sentence but reducing stylistic properties. In this method, the quality of generated sentences relies on the performance of classifiers to a large extent. Meanwhile, such models are usually sensitive to parameters and difficult to train. In contrast, we combine a pre-training process with reinforcement learning to build up a stable language model and design special rewards for our task.
> 
> Irony Detection: With the development of social media, irony detection becomes a more important task. Methods for irony detection can be mainly divided into two categories: methods based on feature engineering and methods based on neural networks.
> 
> As for methods based on feature engineering, In BIBREF1 , authors investigate pragmatic phenomena and various irony markers. In BIBREF14 , researchers leverage a combination of sentiment, distributional semantic and text surface features. Those models rely on hand-crafted features and are hard to implement.
> 
> When it comes to methods based on neural networks, long short-term memory (LSTM) BIBREF15 network is widely used and is very efficient for irony detection. In BIBREF16 , a tweet is divided into two segments and a subtract

#### Relevance 1476

Label: 

### BM25

#### Passage 1470

Retrieved by: BM25

> In this paper, we first systematically define irony generation based on style transfer. Because of the lack of irony data, we make use of twitter and build a large-scale dataset. In order to control irony accuracy, sentiment preservation and content preservation at the same time, we also design a combination of rewards for reinforcement learning and incorporate reinforcement learning with a pre-training process. Experimental results demonstrate that our model outperforms other generative models and our rewards are effective. Although our model design is effective, there are still many errors and we systematically analyze them. In the future, we are interested in exploring these directions and our work may extend to other kinds of ironies which are more difficult to model.

#### Relevance 1470

Label: 

#### Passage 1472

Retrieved by: BM25

> In this section, we describe how we build our dataset with tweets. First, we crawl over 2M tweets from twitter using GetOldTweets-python. We crawl English tweets from 04/09/2012 to /12/18/2018. We first remove all re-tweets and use langdetect to remove all non-English sentences. Then, we remove hashtags attached at the end of the tweets because they are usually not parts of sentences and will confuse our language model. After that, we utilize Ekphrasis to process tweets. We remove URLs and restore remaining hashtags, elongated words, repeated words, and all-capitalized words. To simplify our dataset, We replace all “ INLINEFORM0 money INLINEFORM1 " and “ INLINEFORM2 time INLINEFORM3 " tokens with “ INLINEFORM4 number INLINEFORM5 " token when using Ekphrasis. And we delete sentences whose lengths are less than 10 or greater than 40. In order to restore abbreviations, we download an abbreviation dictionary from webopedia and restore abbreviations to normal words or phrases according to the dictionary. Finally, we remove sentences which have more than two rare words (appearing less than three times) in order to constrain the size of vocabulary. Finally, we get 662,530 sentences after pre-processing.
> 
> As neural networks are proved effective in irony detection, we decide to implement a neural classifier in order to classify the sentences into ironic and non-ironic sentences. However, the only high-quality irony dataset we can obtain is the dataset of Semeval-2018 Task 3 and the dataset is pretty small, which will cause overfitting to complex models. Therefore, we just implement a simple one-layer RNN with LSTM cell to classify pre-processed sentences into ironic sentences and non-ironic sentences because LSTM networks are widely used in irony detection. We train the model with the dataset of Semeval-2018 Task 3. After classification, we get 262,755 ironic sentences and 399,775 non-ironic sentences. According to our observation, not all non-ironic sentences are suitable to be transferred into ironic sentences. For example, “just hanging out . watching . is it monday yet" is hard to transfer because it does not have an explicit sentiment polarity. So we remove all interrogative sentences from the non-ironic sentences and only obtain the sentences which have words expressing strong sentiments. We evaluate the sentiment polarity of each

#### Relevance 1472

Label: 

### Dense

#### Passage 1473

Retrieved by: Dense

> The policy gradient algorithm BIBREF21 is a simple but widely-used algorithm in reinforcement learning. It is used to maximize the expected reward INLINEFORM0 . The objective function to minimize is defined as: DISPLAYFORM0
> 
> where INLINEFORM0 , INLINEFORM1 is the reward of INLINEFORM2 and INLINEFORM3 is the input size.

#### Relevance 1473

Label: 

#### Passage 1474

Retrieved by: Dense

> to implement.
> 
> When it comes to methods based on neural networks, long short-term memory (LSTM) BIBREF15 network is widely used and is very efficient for irony detection. In BIBREF16 , a tweet is divided into two segments and a subtract layer is implemented to calculate the difference between two segments in order to determine whether the tweet is ironic. In BIBREF17 , authors utilize a recurrent neural network with Bi-LSTM and self-attention without hand-crafted features. In BIBREF18 , researchers propose a system based on a densely connected LSTM network.

#### Relevance 1474

Label: 

### Hybrid

None

## Question 0194

Paper: Learning variable length units for SMT between related languages via Byte Pair Encoding

> Which translation model do they employ?

### Common Retrieved Chunks

#### Passage 1477

Retrieved by: BM25, Dense, Hybrid

> The improved performance of BPE units compared to word-level and morpheme-level representations is easy to explain: with a limited vocabulary they address the problem of data sparsity. But character level models also have a limited vocabulary, yet they do not improve translation performance except for very close languages. Character level models learn character mappings effectively, which is sufficient for translating related languages which are very close to each other (translation is akin to transliteration in these cases). But they are not sufficient for translating related languages that are more divergent. In this case, translating cognates, morphological affixes, non-cognates etc. require a larger context. So, BPE and OS units — which provide more context — outperform character units.
> 
> A study of the correlation between lexical similarity and translation quality makes this evident (See Table TABREF32 ). We see that character models work best when the source and target sentences are lexically very similar. The additional context decouples OS and BPE units from lexical similarity. Words and morphemes show the least correlation since they do not depend on lexical similarity.
> 
> Why does BPE performs better than OS which also provides a larger contextual window for translation? While orthographic syllables represent just approximate syllables, we observe that BPE units also represent higher level semantic units like frequent morphemes, suffixes and entire words. Table TABREF33 shows a few examples for some Indian languages. So, BPE level models can learn semantically similar translation mappings in addition to lexically similar mappings. In this way, BPE units enable the translation models to balance the use of lexical similarity with semantic similarity. This further decouples the translation quality from lexical similarity as seen from the table. BPE units also have an additional degree of freedom (choice of vocabulary size), which allows tuning for best translation performance. This could be important when larger parallel corpora are available, allowing larger vocabulary sizes.

#### Relevance 1477

Label: 

#### Passage 1478

Retrieved by: BM25, Dense, Hybrid

> Since we are concerned with low resource scenarios, a desirable property of subword units is robustness of the translation models to change of translation domain. kunchukuttan2016orthographic have shown that OS level models are robust to domain change. Since BPE units are learnt from a specific corpus, it is not guaranteed that they would also be robust to domain changes. To study the behaviour of BPE unit trained models, we also tested the translation models trained on tourism & health domains on an agriculture domain test set of 1000 sentences (see Table TABREF27 for results). In this cross-domain translation scenario, the BPE level model outperforms the OS-level and word-level models for most language pairs. The Konkani-Marathi pair alone shows a degradation using the OS level model. The BPE model is almost on par with the OS level model for Telugu-Malayalam and Hindi-Malayalam.

#### Relevance 1478

Label: 

#### Passage 1479

Retrieved by: BM25, Hybrid

> In the experiments discussed so far, we learnt the BPE vocabulary separately for the source and target languages. In this section, we describe our experiments with jointly learning BPE vocabulary over source and target language corpora as suggested by sennrich2016neural. The idea is to learn an encoding that is consistent across source and target languages and therefore helps alignment. We expect a significant number of common BPE units between related languages. If source and target languages use the same writing system, then a joint model is created by learning BPE over concatenated source and target language corpus. If the writing systems are different, then we transliterate one corpus to another by one-one character mappings. This is possible between Indic scripts. But this scheme cannot be applied between Urdu and Indic scripts as well as between Korean Hangul and Japanese Kanji scripts.
> 
> Table TABREF31 shows the results of the joint BPE model for language pairs where such a model is built. We do not see any major improvement over the monolingual BPE model due to the joint BPE model.

#### Relevance 1479

Label: 

#### Passage 1482

Retrieved by: Dense, Hybrid

> We trained translation systems over the following basic units: character, morpheme, word, orthographic syllable and BPE unit. In this section, we summarize the languages and writing systems chosen for our experiments, the datasets used and the experimental configuration of our translation systems, and the evaluation methodology.

#### Relevance 1482

Label: 

#### Passage 1483

Retrieved by: Dense, Hybrid

> There are two broad set of approaches that have been explored in the literature for translation between related languages that leverage lexical similarity between source and target languages.
> 
> The first approach involves transliteration of source words into the target languages. This can done by transliterating the untranslated words in a post-processing step BIBREF8 , BIBREF9 , a technique generally used for handling named entities in SMT. However, transliteration candidates cannot be scored and tuned along with other features used in the SMT system. This limitation can be overcome by integrating the transliteration module into the decoder BIBREF10 , so both translation and transliteration candidates can be evaluated and scored simultaneously. This also allows transliteration vs. translation choices to be made.
> 
> Since a high degree of similarity exists at the subword level between related languages, the second approach looks at translation with subword level basic units. Character-level SMT has been explored for very closely related languages like Bulgarian-Macedonian, Indonesian-Malay, Spanish-Catalan with modest success BIBREF11 , BIBREF12 , BIBREF13 . Unigram-level learning provides very little context for learning translation models BIBREF14 . The use of character n-gram units to address this limitation leads to data sparsity for higher order n-grams and provides little benefit BIBREF13 . These results were demonstrated primarily for very close European languages. kunchukuttan2016orthographic proposed orthographic syllables, a linguistically-motivated variable-length unit, which approximates a syllable. This unit has outperformed character n-gram, word and morpheme level models as well as transliteration post-editing approaches mentioned earlier. They also showed orthographic syllables can outperform other units even when: (i) the lexical distance between related languages is reasonably large, (ii) the languages do not have a genetic relation, but only a contact relation.
> 
> Recently, subword level models have also generated interest for neural machine translation (NMT) systems. The motivation is the need to limit the vocabulary of neural MT systems in encoder-decoder architectures BIBREF15 . It is in this context that Byte Pair Encoding, a data compression method BIBREF5 , was adapted to learn subword units for NMT BIBREF6 . Other subword units for NMT have also been proposed: character BIBREF16 , Huffman encoding based units BIBREF17 , wordpieces BIBREF18 , BIBREF19 . Our hypothesis is that such

#### Relevance 1483

Label: 

### BM25

#### Passage 1480

Retrieved by: BM25

> The utility of orthographic syllables as translation units is limited to languages that use writing systems which represent vowels. Alphabetic and abugida writing systems fall into this category. On the other hand, logographic writing systems (Japanese Kanji, Chinese) and abjad writing systems (Arabic, Hebrew, Syriac, etc.) do not represent vowels. To be more precise, abjad writing systems may represent some/all vowels depending on language, pragmatics and conventions. Syllabic writing systems like Korean Hangul do not explicitly represent vowels, since the basic unit (the syllable) implicitly represents the vowels. The major advantage of Byte Pair Encoding is its writing system independence and our results show that BPE encoded units are useful for translation involving abjad (Urdu uses an extended Arabic writing system), logographic (Japanese Kanji) and syllabic (Korean Hangul) writing systems. For language pairs involving Urdu, there is an 18% average improvement over word-level and 12% average improvement over morpheme-level translation accuracy. For Japanese-Korean language pairs, an average improvement of 6% in translation accuracy over a word-level baseline is observed.

#### Relevance 1480

Label: 

#### Passage 1481

Retrieved by: BM25

> The above mentioned results for BPE units do not explore optimal values of the number of merge operations. This is the only hyper-parameter that has to be selected for BPE. We experimented with number of merge operations ranging from 1000 to 4000 and the translation results for these are shown in Table TABREF25 . Selecting the optimal value of merge operations lead to a modest, average increase of 1.6% and maximum increase of 3.5% in the translation accuracy over B INLINEFORM0 across different language pairs .
> 
> We also experimented with higher number of merge operations for some language pairs, but there seemed to be no benefit with a higher number of merge operations. Compared to the number of merge operations reported by sennrich2016neural in a more general setting for NMT (60k), the number of merge operations is far less for translation between related languages with limited parallel corpora. We must bear in mind that their goal was different: available parallel corpus was not an issue, but they wanted to handle as large a vocabulary as possible for open-vocabulary NMT. Yet, the low number of merge operations suggest that BPE encoding captures the core vocabulary required for translation between related tasks.

#### Relevance 1481

Label: 

### Dense

#### Passage 1484

Retrieved by: Dense

> We show that translation units learnt using BPE can outperform all previously proposed translation units, including the best-performing orthographic syllables, for SMT between related languages when limited parallel corpus is available. Moreover, BPE encoding is writing system independent, hence it can be applied to any language. Experimentation on a large number of language pairs spanning diverse language families and writing systems lend strong support to our results. We also show that BPE units are more robust to change in translation domain. They perform better for morphologically rich languages and extremely data scarce scenarios.
> 
> BPE seems to be beneficial because it enables discovery of translation mappings at various levels simultaneously (syllables, suffixes, morphemes, words, etc. ). We would like to further pursue this line of work and investigate better translation units. This is also a question relevant to translation with subwords in NMT. NMT between related languages using BPE and similar encodings is also an obvious direction to explore.
> 
> Given the improved performance of the BPE-unit, tasks involving related languages viz. pivot based MT, domain adaptation BIBREF14 and translation between a lingua franca and related languages BIBREF38 can be revisited with BPE units.

#### Relevance 1484

Label: 

### Hybrid

None

## Question 0195

Paper: Multilingual and Unsupervised Subword Modeling for Zero-Resource Languages

> Which intrisic measures do they use do evaluate obtained representations?

### Common Retrieved Chunks

#### Passage 1486

Retrieved by: BM25, Dense, Hybrid

> bnfs cae utd
> 
> In this work we investigated different representations obtained using data from the target language alone (i.e., fully unsupervised) and from multilingual supervised systems trained on labeled data from non-target languages. We found that the cae, a recent neural approach to unsupervised subword modeling, learns complementary information to the more traditional approach of vtln. This suggests that vtln should also be considered by other researchers using neural approaches. On the other hand, our best results were achieved using multilingual bnfs. These results are competitive with state-of-the-art features learned from target language data only BIBREF17 , BIBREF18 , but have the advantage of a much smaller dimensionality. In addition, it is easy to control the dimensionality of the bnfs, unlike in the nonparametric models of BIBREF17 , BIBREF18 , and this allowed us to use them in the downstream task of word segmentation and clustering. We observed consistent improvements from bnfs across all metrics in this downstream task, and other work demonstrates that these features are also useful for downstream keyword spotting in settings with very small amounts of labeled data BIBREF45 . We also showed that it is theoretically possible to further improve bnfs with language-specific fine-tuning, and we hope to explore models that can do this more reliably than the cae in the future.
> 
> Finally, our qualitative analysis showed that both cae features and bnfs tend to vary much less over time than traditional PLPs, supporting the idea that they are better at capturing phonetic information rather than small variations in the acoustics. Although this property helps explain the better performance on intrinsic measures and the segmentation task, it harms performance for utd, where the system seems heavily tuned towards PLPs. Therefore, our work also points to the need for term discovery systems that are more robust to different types of input features.

#### Relevance 1486

Label: 

#### Passage 1488

Retrieved by: BM25, Dense, Hybrid

> Table TABREF36 compares MFCCs, cae features (with and without vtln) and bnfs as input to the system of BIBREF4 . It shows that both vtln and bnfs help on all metrics, with improvements ranging from small to more substantial and bnfs clearly giving the most benefit. The effects of vtln are mostly confined to reducing both gender and speaker purity of the identified clusters (which is desirable) while maintaining the performance on other metrics. This means that the learned representations have become more invariant to variation in speaker and gender, which is exactly what vtln aims to do. However, this appears to be insufficient to also help other metrics, aligning with the experiments in BIBREF4 that indicate that improvements on the other metrics are hard to obtain.
> 
> On the other hand, bnfs result in better performance across all metrics. While some of these improvements are small, they are very consistent across all metrics. This shows that the bnfs are also useful for down-stream tasks in zero-resource settings. It especially demonstrates that such bnfs which are trained on high-resource languages without seeing any target language speech at all are a strong alternative to fully unsupervised features for practical scenarios or could in turn be used to improve unsupervised systems trained on the target language speech data.

#### Relevance 1488

Label: 

#### Passage 1489

Retrieved by: BM25, Hybrid

> we expand upon that work in several ways. First, we include new results on the corpora and evaluation measures used in the zrsc, to allow more direct comparisons with other work. In doing so, we also provide the first set of results on identical systems evaluated using both the same-different and ABX evaluation measures. This permits the two measures themselves to be better compared. Finally, we provide both a qualitative analysis of the differences between the different features we extract, and a quantitative evaluation on the downstream target-language task of unsupervised full-coverage speech segmentation and clustering using the system of BIBREF4 . This is the first time that multilingual features are used in such a system, which performs a complete segmentation of input speech into hypothesized words. As in our intrinsic evaluations, we find that the multilingual bnfs consistently outperform the best unsupervised cae features, which in turn outperform or do similarly to MFCCs.

#### Relevance 1489

Label: 

#### Passage 1491

Retrieved by: Dense, Hybrid

> is similar to our cae.
> 
> These systems score better than all of our features, but are not directly comparable for several reasons. Firstly, it is unclear how these systems were optimized, since there was no separate development set in zrsc 2015. Secondly, our features are all 39-dimensional to be directly comparable with MFCCs, whereas the other two systems have higher dimensionality (and indeed the winning system from zrsc 2017 was even greater, with more than 1000 dimensions BIBREF17 ). Such higher dimensional features may be useful in some circumstances, but lower dimensional features are often more efficient to work with and we don't know whether the competing systems would work as well with fewer dimensions.
> 
> The bnfs are in any case competitive with the higher dimensional features, and have the advantage that they can be built using standard Kaldi scripts and do not require any training on the target language, so can easily be deployed to new languages. The competitive result of BIBREF42 also shows that in general a system trained on word pairs discovered from a utd system can perform very well.

#### Relevance 1491

Label: 

#### Passage 1492

Retrieved by: Dense, Hybrid

> INLINEFORM5 and INLINEFORM6 are from the same and INLINEFORM7 from a different speaker.
> 
> The ABX evaluation includes all such minimal pair phoneme triplets of the evaluation corpus. These pairs therefore rarely correspond to full words, making it a somewhat abstract task whose results may be difficult to interpret when summarizing it as a single final metric. ABX can however be very suitable for more fine-grained analysis of speech phenomena by including only specific phonetic contrasts in the evaluation BIBREF41 . In contrast, the same-different task always compares whole words and directly evaluates how good feature representations are at telling whether two utterances are the same word or not. Thus it has an immediate link to applications like spoken term detection and it allows easier error analysis. It is also faster to prepare the same-different evaluation set and run the evaluation. We wish to verify that the ABX and same-different measures correlate well, to better compare studies that use only one of them and to allow choosing the task that is more appropriate for the situation at hand.
> 
> Table TABREF22 shows results on the Xitsonga and Buckeye English corpora. Here we compare ABX error rates computed with the zrsc 2015 BIBREF0 evaluation scripts with ap on the same-different task. To the best of our knowledge, this is the first time such a comparison has been made. The results on both tasks correlate well, especially when looking at the ABX cross-speaker error rate because the same-different evaluation as described in Section SECREF11 also focuses on cross-speaker pairs. As might be expected vtln only improves cross-speaker, but not within-speaker ABX error rates.
> 
> For comparison we also include ABX results of the official zrsc 2015 topline BIBREF0 , which are posteriorgrams obtained from a supervised speech recognition system, the current state-of-the-art system BIBREF18 which even outperforms the topline for English, and the system of BIBREF42 which is the most recent form of the ABNet BIBREF12 , an architecture that is similar to our cae.
> 
> These systems score better than all of our features, but are not directly comparable for several reasons. Firstly, it is unclear how these systems were optimized, since there was no separate development set in zrsc

#### Relevance 1492

Label: 

### BM25

#### Passage 1485

Retrieved by: BM25

> We use the GlobalPhone corpus of speech read from news articles BIBREF20 . We chose 6 languages from different language families as zero-resource languages on which we evaluate the new feature representations. That means our models do not have any access to the transcriptions of the training data, although transcriptions still need to be available to run the evaluation. The selected languages and dataset sizes are shown in Table TABREF8 . Each GlobalPhone language has recordings from around 100 speakers, with 80% of these in the training sets and no speaker overlap between training, development, and test sets.
> 
> For baseline features, we use Kaldi BIBREF21 to extract MFCCs+ INLINEFORM0 + INLINEFORM1 and PLPs+ INLINEFORM2 + INLINEFORM3 with a window size of 25 ms and a shift of 10 ms, and we apply per-speaker cmn. We also evaluated MFCCs and PLPs with vtln. The acoustic model used to extract the warp factors was a diagonal-covariance gmm with 1024 components. A single GMM was trained unsupervised on each language's training data.
> 
> To train the cae, we obtained utd pairs using a freely available utd system BIBREF22 and extracted 36k word pairs for each target language. Published results with this system use PLP features as input, and indeed our preliminary experiments confirmed that MFCCs did not work as well. We therefore report results using only PLP or PLP+VTLN features as input to utd. Following BIBREF23 , BIBREF2 , we train the cae model by first pre-training an autoencoder with eight 100-dimensional layers and a final layer of size 39 layer-wise on the entire training data for 5 epochs with a learning rate of INLINEFORM0 . We then fine-tune the network with same-word pairs as weak supervision for 60 epochs with a learning rate of INLINEFORM1 . Frame pairs are presented to the cae using either MFCC, MFCC+VTLN, or BNF representation, depending on the experiment (preliminary experiments indicated that PLPs performed worse than MFCCs, so MFCCs are used as the stronger baseline). Features are extracted from the final hidden layer of the cae as shown in Figure FIGREF6 .
> 
> To provide an upper bound on cae performance, we also report results using gold standard same-word pairs for cae training.

#### Relevance 1485

Label: 

#### Passage 1487

Retrieved by: BM25

> We retrained the cae and BNF models to return 13-dimensional features with all other parameters unchanged to be consistent with the experiments of BIBREF4 and for computational reasons. We also did not tune any hyperparameters of the BES-GMM for our new input features. Nonetheless, our baseline cae results do not exactly correspond to the ones in BIBREF4 because for example the MFCC input features have been extracted with a different toolkit and we used a slightly different training procedure.
> 
> We use several metrics to compare the resulting segmented word tokens to ground truth forced alignments of the data. By mapping every discovered word token to the ground truth word with which it overlaps most, average cluster purity can be calculated as the total proportion of correctly mapped tokens in all clusters. More than one cluster may be mapped to the same ground truth word type. In a similar way, we can calculate unsupervised word error rate (WER), which uses the same cluster-to-word mapping but also takes insertions and deletions into account. Here we consider two ways to perform the cluster mapping: many-to-one, where more than one cluster can be assigned the same word label (as in purity), or one-to-one, where at most one cluster is mapped to a ground truth word type (accomplished in a greedy fashion). We also compute the gender and speaker purity of the clusters, where we want to see clusters that are as diverse as possible on these measures, i.e., low purity. To explicitly evaluate how accurate the model performs segmentation, we compare the proposed word boundary positions to those from forced alignments of the data (falling within a single true phoneme from the boundary). We calculate boundary precision and recall, and report the resulting word boundary F-scores. We also calculate word token F-score, which requires that both boundaries from a ground truth word token be correctly predicted.

#### Relevance 1487

Label: 

### Dense

#### Passage 1490

Retrieved by: Dense

> All experiments in this section are evaluated using the same-different task BIBREF26 , which tests whether a given speech representation can correctly classify two speech segments as having the same word type or not. For each word pair in a pre-defined set INLINEFORM0 the dtw cost between the acoustic feature vectors under a given representation is computed. Two segments are then considered a match if the cost is below a threshold. Precision and recall at a given threshold INLINEFORM1 are defined as INLINEFORM2
> 
> where INLINEFORM0 is the number of sw, swdp or all discovered matches at that threshold and INLINEFORM1 is the number of actual swdp pairs in INLINEFORM2 . We can compute a precision-recall curve by varying INLINEFORM3 . The final evaluation metric is the ap or the area under that curve. We generate evaluation sets of word pairs for the GlobalPhone development and test sets from all words that are at least 5 characters and 0.5 seconds long, except that we now also include different-word pairs.
> 
> Previous work BIBREF26 , BIBREF2 calculated recall with all sw pairs for easier computation because their test sets included a negligible number of swsp pairs. In our case the smaller number of speakers in the GlobalPhone corpora results in up to 60% of sw pairs being from the same speaker. We therefore always explicitly compute the recall only for swdp pairs to focus the evaluation of features on their speaker invariance.

#### Relevance 1490

Label: 

### Hybrid

None

## Question 0196

Paper: Phrase Table as Recommendation Memory for Neural Machine Translation

> what were the evaluation metrics?

### Common Retrieved Chunks

#### Passage 1493

Retrieved by: BM25, Hybrid

> A natural question arises that whether it is more beneficial to incorporate a phrase translation table than the translation lexicons. From Table 1, we can conclude that both translation lexicons and phrase translation table can improve NMT system's translation quality. In CH-EN translation, Arthur improves the baseline NMT system with 0.81 BLEU points, while our method improves the baseline NMT system with 2.23 BLEU points. In EN-JA translation, Arthur improves the baseline NMT system with 0.73 BLEU points, while our method improves the baseline NMT system with 1.96 BLEU points. Therefore, it is very obvious that phrase information is more effective than lexicon information when we use them to improve the NMT system.
> 
> Fig. 4 shows an illustrative example. In this example, baseline NMT mistranslates “dianli (electricity) anquan (safe)” into “coal”. Arthur partially fixes this error and it can correctly translate “dianli (electrical)” into “electrical”, but the source word “anquan (safe)” is still missed. Fortunately, this mistake is fixed by our proposed method. The reason behind this is that Arthur uses information from translation lexicons, which makes the system only fix the translation mistake of an individual lexicon (in this example, it is “dianli (electrical)”), while our method uses the information from phrases, which makes the system can not only obtain the correct translation of the individual lexicon but also capture local lexicon reordering and fixed collocation etc.
> 
> Besides the BLEU score, we also conduct a subjective evaluation to validate the benefit of incorporating a phrase table in NMT. The subjective evaluation is conducted on CH-EN translation. As our method tries to solve the problem that NMT system cannot reflect the true meaning of the source sentence, the criterion of the subjective evaluation is the faithfulness of translation results. Specifically, five human evaluators, who are native Chinese and expert in English, are asked to evaluate the translations of 500 source sentences randomly sampled from the test sets without knowing which system a translation is selected from. The score ranges from 0 to 5. For a translation result, the higher its score is, the more faithful it is. Table 2 shows the average results of five subjective evaluations on CH-EN translation. As shown in Table 2，the

#### Relevance 1493

Label: 

#### Passage 1494

Retrieved by: BM25, Hybrid

> We use the Zoph_RNN toolkit to implement all our described methods. In all experiments, the encoder and decoder include two stacked LSTM layers. The word embedding dimension and the size of hidden layers are both set to 1,000. The minibatch size is set to 128. We limit the vocabulary to 30K most frequent words for both the source and target languages. Other words are replaced by a special symbol “UNK”. At test time, we employ beam search and beam size is set to 12. We use case-insensitive 4-gram BLEU score as the automatic metric BIBREF21 for translation quality evaluation.

#### Relevance 1494

Label: 

#### Passage 1497

Retrieved by: BM25, Hybrid

> The last step is to combine the bonus value with the conditional probability of the baseline NMT model (Eq.(2)). Specifically, we add the bonuses to the words on the basis of original NMT score (Eq. (3)) as follows: DISPLAYFORM0
> 
> where INLINEFORM0 is calculated by Eq. (11). INLINEFORM1 is the bonus weight, and specifically, it is the result of sigmoid function ( INLINEFORM2 ), where INLINEFORM3 is a learnable parameter, and this sigmoid function ensures that the final weight falls between 0 and 1.

#### Relevance 1497

Label: 

#### Passage 1499

Retrieved by: Dense, Hybrid

> from. The score ranges from 0 to 5. For a translation result, the higher its score is, the more faithful it is. Table 2 shows the average results of five subjective evaluations on CH-EN translation. As shown in Table 2，the faithfulness of translation results produced by our method is better than Arthur and baseline NMT system.

#### Relevance 1499

Label: 

### BM25

#### Passage 1495

Retrieved by: BM25

> The past several years have witnessed a significant progress in Neural Machine Translation (NMT). Most NMT methods are based on the encoder-decoder architecture BIBREF0 , BIBREF1 , BIBREF2 and can achieve promising translation performance in a variety of language pairs BIBREF3 , BIBREF4 , BIBREF5 .
> 
> However, recent studies BIBREF6 , BIBREF7 show that NMT often generates words that make target sentences fluent, but unfaithful to the source sentences. In contrast, traditional Statistical Machine Translation (SMT) methods tend to rarely make this kind of mistakes. Fig. 1 shows an example that NMT makes mistakes when translating the phrase “jinkou dafu xiahua (the sharp decline in imports)” and the phrase “maoyi shuncha (the trade surplus)”, but SMT can produce correct results when translating these two phrases. BIBREF6 argues that the reason behind this is the use of distributed representations of words in NMT makes systems often generate words that seem natural in the context, but do not reflect the content of the source sentence. Traditional SMT can avoid this problem as it produces the translations based on phrase mappings.
> 
> Therefore, it will be beneficial to combine SMT and NMT to alleviate the previously mentioned problem. Actually, researchers have made some effective attempts to achieve this goal. Earlier studies were based on the SMT framework, and have been deeply discussed in BIBREF8 . Later, the researchers transfers to NMT framework. Specifically, coverage mechanism BIBREF9 , BIBREF10 , SMT features BIBREF11 , BIBREF12 , BIBREF13 , BIBREF14 , BIBREF15 and translation lexicons BIBREF6 , BIBREF16 , BIBREF17 have been fully explored. In contrast, phrase translation table, as the core of SMT, has not been fully studied. Recently, BIBREF18 and BIBREF19 explore the possibility of translating phrases in NMT. However, the “phrase” in their approaches are different from that used in phrase-based SMT. In BIBREF18 's models, the phrase pair must be a one-to-one mapping with a source phrase having a unique target phrase (named entity translation pairs). In BIBREF19 's models, the source side of a phrase pair must be a chunk. Therefore, it is still a big challenge to incorporate any phrase pair in the phrase table into NMT system to alleviate the unfaithfulness problem.
> 
> In this

#### Relevance 1495

Label: 

#### Passage 1496

Retrieved by: BM25

> word is worthy to recommend. In order to facilitate the calculation of the bonus value (section 3.2), we also need to maintain the origin of each recommendation word. Here, the origin of a recommendation word contains two parts: 1) the phrase pair this word belongs to and 2) the phrase translation probability between the source and target phrases. Formally, for a recommendation word INLINEFORM0 , we can denote it by: DISPLAYFORM0
> 
> where INLINEFORM0 denotes the INLINEFORM1 -th phrase pair the recommendation word INLINEFORM2 belongs to (some words may belong to different phrase pairs and INLINEFORM3 denotes the number of phrase pairs). INLINEFORM4 is the source phrase and INLINEFORM5 is the target phrase. INLINEFORM6 is the phrase translation probability between the source and target phrases. Take Fig. 2 as an example. When the partial translation is “he”, word “settled” can be recommended according to algorithm 1. Word “settled” is contained in two phrase pairs and the translation probabilities are respectively 0.6 and 0.4. Thus, we can denote the word "settled" as follows: DISPLAYFORM0

#### Relevance 1496

Label: 

### Dense

#### Passage 1498

Retrieved by: Dense

> In this section, we describe the experiments to evaluate our proposed methods.

#### Relevance 1498

Label: 

#### Passage 1500

Retrieved by: Dense

> We also conduct another experiment to find out whether or not our methods are still effective when much more sentence pairs are available. Therefore, the CH-EN experiments on millions of sentence pairs are conducted and Table 3 reports the results. We can conclude from Table 3 that our model can also improve the NMT translation quality on all of the test sets and the average improvement is up to 1.83 BLEU points.

#### Relevance 1500

Label: 

#### Passage 1501

Retrieved by: Dense

> We test the proposed methods on Chinese-to-English (CH-EN) translation and English-to-Japanese (EN-JA) translation. In CH-EN translation, we test the proposed methods with two data sets: 1) small data set, which includes 0.63M sentence pairs; 2) large-scale data set, which contains about 2.1M sentence pairs. NIST 2003 (MT03) dataset is used for validation. NIST2004-2006 (MT04-06) and NIST 2008 (MT08) datasets are used for testing. In EN-JA translation, we use KFTT dataset, which includes 0.44M sentence pairs for training, 1166 sentence pairs for validation and 1160 sentence pairs for testing.

#### Relevance 1501

Label: 

#### Passage 1502

Retrieved by: Dense

> The next task is to calculate the bonus value for each recommendation word. For a recommendation word INLINEFORM0 denoted by Eq. (8), its bonus value is calculated as follows:
> 
> Step1: Extracting each phrase translation probability INLINEFORM0 .
> 
> Step2: For each phrase pair INLINEFORM0 , we convert the attention weight INLINEFORM1 in NMT (Eq. (6)) between target word INLINEFORM2 and source word INLINEFORM3 to phrase alignment probability INLINEFORM4 between target word INLINEFORM5 and source phrase INLINEFORM6 as follows: DISPLAYFORM0
> 
> where INLINEFORM0 is the number of words in phrase INLINEFORM1 . As shown in Eq. (10), our conversion method is making an average of word alignment probability INLINEFORM2 whose source word INLINEFORM3 belongs to source phrase INLINEFORM4 .
> 
> Step3: Calculating the bonus value for each recommendation word as follows: DISPLAYFORM0
> 
> From Eq. (11), the bonus value is determined by two factors, i.e., 1) alignment information INLINEFORM0 and 2) translation probability INLINEFORM1 . The process of involving INLINEFORM2 is important because the bonus value will be influenced by different source phrases that systems focus on. And we take INLINEFORM3 into consideration with a hope that the larger INLINEFORM4 is, the larger its bonus value is.

#### Relevance 1502

Label: 

### Hybrid

#### Passage 1503

Retrieved by: Hybrid

> NMT contains two parts, encoder and decoder, where encoder transforms the source sentence INLINEFORM0 into context vectors INLINEFORM1 . This context set is constructed by INLINEFORM2 stacked Long Short Term Memory (LSTM) BIBREF20 layers. INLINEFORM3 can be calculated as follows: DISPLAYFORM0
> 
> The decoder generates one target word at a time by computing the probability of INLINEFORM0 as follows: DISPLAYFORM0
> 
> where INLINEFORM0 is the score produced by NMT: DISPLAYFORM0
> 
> and INLINEFORM0 is the attention output: DISPLAYFORM0
> 
> the attention model calculates INLINEFORM0 as the weighted sum of the source-side context vectors: DISPLAYFORM0 DISPLAYFORM1
> 
> INLINEFORM0 is computed using the following formula: DISPLAYFORM0

#### Relevance 1503

Label: 

## Question 0197

Paper: Real-World Conversational AI for Hotel Bookings

> Where does their information come from?

### Common Retrieved Chunks

#### Passage 1504

Retrieved by: BM25, Dense, Hybrid

> Our chatbot system tries to find a desirable hotel for the user, through an interactive dialogue. First, the bot asks a series of questions, such as the dates of travel, the destination city, and a budget range. After the necessary information has been collected, the bot performs a search and sends a list of matching hotels, sorted based on the users' preferences; if the user is satisfied with the results, he can complete the booking within the chat client. Otherwise, the user may continue talking to the bot to further narrow down his search criteria.
> 
> At any point in the conversation, the user may request to talk to a customer support agent by clicking an “agent” or “help” button. The bot also sends the conversation to an agent if the user says something that the bot does not understand. Thus, the bot handles the most common use cases, while humans handle a long tail of specialized and less common requests.
> 
> The hotel search is backed by a database of approximately 100,000 cities and 300,000 hotels, populated using data from our partners. Each database entry contains the name of the city or hotel, geographic information (e.g., address, state, country), and various metadata (e.g., review score, number of bookings).

#### Relevance 1504

Label: 

#### Passage 1505

Retrieved by: BM25, Dense, Hybrid

> For queries identified as search intent, we perform named entity recognition (NER) to extract spans from the query representing names of hotels and cities. Recently, neural architectures have shown to be successful for NER BIBREF9, BIBREF10. Typically, they are trained on the CoNLL-2003 Shared Task BIBREF11 which features four entity types (persons, organizations, locations, and miscellaneous).
> 
> Our NER model instead identifies hotel and location names, for example:
> 
> “double room in the cosmopolitan, las vegas for Aug 11-16”,
> 
> “looking for a resort in Playa del carmen near the beach”.
> 
> We use SpaCy to train custom NER models. The model initialized with SpaCy's English NER model, then fine-tuned using our data, consisting of 21K messages labelled with hotel and location entities. Our first model treats hotels and locations as separate entities, while our second model merges them and considers both hotels and locations as a single combined entity type. All models are evaluated by their precision, recall, and F1 scores for each entity type. The results are shown in Table TABREF14.
> 
> The combined NER model achieves the best accuracy, significantly better than the model with separate entity types. This is expected, since it only needs to identify entities as either hotel or location, without needing to distinguish them. The model is ineffective at differentiating between hotel and location names, likely because this is not always possible using syntactic properties alone; sometimes, world knowledge is required that is not available to the model.

#### Relevance 1505

Label: 

#### Passage 1506

Retrieved by: BM25, Hybrid

> Each of our three models is evaluated by internal cross-validation using the metrics described above; however, the conversational AI system as a whole is validated using external metrics: agent handoff rate and booking completion rate. The agent handoff rate is the proportion of conversations that involve a customer support agent; the booking completion rate is the proportion of conversations that lead to a completed hotel booking. Both are updated on a daily basis.
> 
> External metrics serve as a proxy for our NLP system's performance, since users are more likely to request an agent and less likely to complete their booking when the bot fails. Thus, an improvement in these metrics after a model deployment validates that the model functions as intended in the real world. However, both metrics are noisy and are affected by factors unrelated to NLP, such as seasonality and changes in the hotel supply chain.

#### Relevance 1506

Label: 

#### Passage 1507

Retrieved by: BM25, Dense, Hybrid

> We collect labelled training data from two sources. First, data for the intent model is extracted from conversations between users and customer support agents. To save time, the model suggests a pre-written response to the user, which the agent either accepts by clicking a button, or composes a response from scratch. This action is logged, and after being checked by a professional annotator, is added to our training data.
> 
> Second, we employ professional annotators to create training data for each of our models, using a custom-built interface. A pool of relevant messages is selected from past user conversations; each message is annotated once and checked again by a different annotator to minimize errors. We use the PyBossa framework to manage the annotation processes.

#### Relevance 1507

Label: 

#### Passage 1508

Retrieved by: BM25, Dense, Hybrid

> The information retrieval (IR) system takes a user search query and matches it with the best location or hotel entry in our database. It is invoked when the intent model detects a search intent, and the NER model recognizes a hotel or location named entity. This is a non-trivial problem because the official name of a hotel often differs significantly from what a user typically searches. For example, a user looking for the hotel “Hyatt Regency Atlanta Downtown” might search for “hyatt hotel atlanta”.
> 
> We first apply NER to extract the relevant parts of the query. Then, we use ElasticSearch to quickly retrieve a list of potentially relevant matches from our large database of cities and hotels, using tf-idf weighted n-gram matching. Finally, we train a neural network to rank the ElasticSearch results for relevancy, given the user query and the official hotel name.
> 
> Deep learning has been applied to short text ranking, for example, using LSTMs BIBREF13, or CNN-based architectures BIBREF14, BIBREF15. We experiment with several neural architectures, which take in the user query as one input and the hotel or city name as the second input. The model is trained to classify the match as relevant or irrelevant to the query. We compare the following models:
> 
> Averaged GloVe + feedforward: We use 100-dimensional, trainable GloVe embeddings BIBREF16 trained on Common Crawl, and produce sentence embeddings for each of the two inputs by averaging across all tokens. The sentence embeddings are then given to a feedforward neural network to predict the label.
> 
> BERT + fine-tuning: We follow the procedure for BERT sentence pair classification. That is, we feed the query as sentence A and the hotel name as sentence B into BERT, separated by a [SEP] token, then take the output corresponding to the [CLS] token into a final linear layer to predict the label. We initialize the weights with the pretrained checkpoint and fine-tune all layers for 3 epochs (Figure FIGREF19).
> 
> The models are trained on 9K search messages, with up to 10 results from ElasticSearch and annotations for which results are valid matches. Each training row is expanded into multiple message-result pairs, which are fed as instances to the network. For the

#### Relevance 1508

Label: 

### BM25

None

### Dense

#### Passage 1509

Retrieved by: Dense

> Our conversational AI uses machine learning for three separate, cascading tasks: intent classification, named entity recognition (NER), and information retrieval (IR). That is, the intent model is run on all messages, NER is run on only a subset of messages, and IR is run on a further subset of those. In this section, we give an overview of each task's model and evaluation metrics.

#### Relevance 1509

Label: 

### Hybrid

None

## Question 0198

Paper: KeyVec: Key-semantics Preserving Document Representations

> which document understanding tasks did they evaluate on?

### Common Retrieved Chunks

#### Passage 1510

Retrieved by: BM25, Dense, Hybrid

> To verify the effectiveness, we evaluate the KeyVec model on two text understanding tasks that take continuous distributed vectors as the representations for documents: document retrieval and document clustering.

#### Relevance 1510

Label: 

#### Passage 1511

Retrieved by: BM25, Hybrid

> In recent years, the use of word representations, such as word2vec BIBREF0 , BIBREF1 and GloVe BIBREF2 , has become a key “secret sauce” for the success of many natural language processing (NLP), information retrieval (IR) and machine learning (ML) tasks. The empirical success of word embeddings raises an interesting research question: Beyond words, can we learn fixed-length distributed representations for pieces of texts? The texts can be of variable-length, ranging from paragraphs to documents. Such document representations play a vital role in a large number of downstream NLP/IR/ML applications, such as text clustering, sentiment analysis, and document retrieval, which treat each piece of text as an instance. Learning a good representation that captures the semantics of each document is thus essential for the success of such applications.
> 
> In this paper, we introduce KeyVec, a neural network model that learns densely distributed representations for documents of variable-length. In order to capture semantics, the document representations are trained and optimized in a way to recover key information of the documents. In particular, given a document, the KeyVec model constructs a fixed-length vector to be able to predict both salient sentences and key words in the document. In this way, KeyVec conquers the problem of prior embedding models which treat every word and every sentence equally, failing to identify the key information that a document conveys. As a result, the vectorial representations generated by KeyVec can naturally capture the topics of the documents, and thus should yield good performance in downstream tasks.
> 
> We evaluate our KeyVec on two text understanding tasks: document retrieval and document clustering. As shown in the experimental section SECREF5 , KeyVec yields generic document representations that perform better than state-of-the-art embedding models.

#### Relevance 1511

Label: 

#### Passage 1512

Retrieved by: BM25, Hybrid

> In the document clustering task, we aim to cluster the academic papers by the venues in which they are published. There are a total of 850 academic papers, and 186 associated venues which are used as ground-truth for evaluation. Each academic paper is represented as a vector of 100 dimensions.
> 
> To compare embedding methods in academic paper clustering, we calculate F1, V-measure (a conditional entropy-based clustering measure BIBREF11 ), and ARI (Adjusted Rand index BIBREF12 ). As shown in Table TABREF18 , similarly to document retrieval, Paragraph Vector performed better than word2vec averagings in clustering documents, while our KeyVec consistently performed the best among all the compared methods.

#### Relevance 1512

Label: 

#### Passage 1513

Retrieved by: BM25, Dense, Hybrid

> The goal of the document retrieval task is to decide if a document should be retrieved given a query. In the experiments, our document pool contained 669 academic papers published by IEEE, from which top- INLINEFORM0 relevant papers are retrieved. We created 70 search queries, each composed of the text in a Wikipedia page on a field of study (e.g., https://en.wikipedia.org/wiki/Deep_learning). We retrieved relevant papers based on cosine similarity between document embeddings of 100 dimensions for Wikipedia pages and academic papers. For each query, a good document-embedding model should lead to a list of academic papers in one of the 70 fields of study.
> 
> Table TABREF15 presents P@10, MAP and MRR results of our KeyVec model and competing embedding methods in academic paper retrieval. word2vec averaging generates an embedding for a document by averaging the word2vec vectors of its constituent words. In the experiment, we used two different versions of word2vec: one from public release, and the other one trained specifically on our own academic corpus (113 GB). From Table TABREF15 , we observe that as a document-embedding model, Paragraph Vector gave better retrieval results than word2vec averagings did. In contrast, our KeyVec outperforms all the competitors given its unique capability of capturing and embedding the key information of documents.

#### Relevance 1513

Label: 

#### Passage 1514

Retrieved by: BM25, Dense, Hybrid

> The Neural Encoder computes document-level embeddings based on the salient sentences identified by the Reader. In order to capture the topics of a document and the importance of its individual sentences, we perform a weighted pooling over the constituent sentences, with the weights specified by INLINEFORM0 , which gives the document-level embedding INLINEFORM1 through a INLINEFORM2 transformation:
> 
> DISPLAYFORM0
> 
> where INLINEFORM0 is a trainable weight matrix, and INLINEFORM1 is a trainable bias vector.
> 
> Weighted pooling functions are commonly used as the attention mechanism BIBREF8 in neural sequence learning tasks. The “share” each sentence contributes to the final embedding is proportional to its probability of being a salient sentence. As a result, INLINEFORM0 will be dominated by salient sentences with high INLINEFORM1 , which preserves the key information in a document, and thus allows long documents to be encoded and embedded semantically.

#### Relevance 1514

Label: 

### BM25

None

### Dense

#### Passage 1515

Retrieved by: Dense

> To optimize Reader, we take a surrogate approach to heuristically generate a set of salient sentences from a document collection, which constitute a training dataset for learning the probabilities of salient sentences INLINEFORM0 parametrized by INLINEFORM1 . More specifically, given a training set INLINEFORM2 of documents (e.g., body-text of research papers) and their associated summaries (e.g., abstracts) INLINEFORM3 , where INLINEFORM4 is a gold summary of document INLINEFORM5 , we employ a state-of-the-art sentence similarity model, DSSM BIBREF9 , BIBREF10 , to find the set of top- INLINEFORM6 sentences INLINEFORM8 in INLINEFORM9 , such that the similarity between INLINEFORM10 and any sentence in the gold summary INLINEFORM11 is above a pre-defined threshold. Note that here we assume each training document is associated with a gold summary composed of sentences that might not come from INLINEFORM12 . We make this assumption only for the sake of generating the set of salient sentences INLINEFORM13 which is usually not readily available.
> 
> The log likelihood objective of the Neural Reader is then given by maximizing the probability of INLINEFORM0 being the set of key sentences, denoted as INLINEFORM1 :
> 
> DISPLAYFORM0
> 
> where INLINEFORM0 is the set of non-key sentences. Intuitively, this likelihood function gives the probability of each sentence in the generated key sentence set INLINEFORM1 being a key sentence, and the rest of sentences being non-key ones.

#### Relevance 1515

Label: 

#### Passage 1516

Retrieved by: Dense

> The Neural Reader learns to understand the topics of every given input document with paying attention to the salient sentences. It computes a dense representation for each sentence in the given document, and derives its probability of being a salient sentence. The identified set of salient sentences, together with the derived probabilities, will be used by the Neural Encoder to generate a document-level embedding.
> 
> Since the Reader operates in embedding space, we first represent discrete words in each sentence by their word embeddings. The sentence encoder in Reader then derives sentence embeddings from the word representations to capture the semantics of each sentence. After that, a Recurrent Neural Network (RNN) is employed to derive document-level semantics by consolidating constituent sentence embeddings. Finally, we identify key sentences in every document by computing the probability of each sentence being salient.
> 
> Specifically, for the INLINEFORM0 -th sentence INLINEFORM1 with INLINEFORM2 words, Neural Reader maps each word INLINEFORM3 into a word embedding INLINEFORM4 . Pre-trained word embeddings like word2vec or GloVe may be used to initialize the embedding table. In our experiments, we use domain-specific word embeddings trained by word2vec on our corpus.
> 
> Given the set of word embeddings for each sentence, Neural Reader then derives sentence-level embeddings INLINEFORM0 using a sentence encoder INLINEFORM1 :
> 
> DISPLAYFORM0
> 
> where INLINEFORM0 is implemented by a Convolutional Neural Network (CNN) with a max-pooling operation, in a way similar to BIBREF6 . Note that other modeling choices, such as an RNN, are possible as well. We used a CNN here because of its simplicity and high efficiency when running on GPUs. The sentence encoder generates an embedding INLINEFORM1 of 150 dimensions for each sentence.
> 
> Given the embeddings of sentences INLINEFORM0 in a document INLINEFORM1 , Neural Reader computes the probability of each sentence INLINEFORM2 being a key sentence, denoted as INLINEFORM3 .
> 
> We employ a Long Short-Term Memory (LSTM) BIBREF7 to compose constituent sentence embeddings into a document representation. At the INLINEFORM0 -th time step, LSTM takes as input the current sentence embedding INLINEFORM1 , and computes a hidden state INLINEFORM2 . We place an LSTM in both directions, and concatenate the outputs of the two LSTMs. For the INLINEFORM3 -th sentence, INLINEFORM4 is

#### Relevance 1516

Label: 

### Hybrid

None

## Question 0199

Paper: Multi-News: a Large-Scale Multi-Document Summarization Dataset and Abstractive Hierarchical Model

> What is the size of Multi-news dataset?

### Common Retrieved Chunks

#### Passage 1517

Retrieved by: BM25, Hybrid

> Following the setting from BIBREF11 , we report ROUGE BIBREF37 scores, which measure the overlap of unigrams (R-1), bigrams (R-2) and skip bigrams with a max distance of four words (R-SU). For the neural abstractive models, we truncate input articles to 500 tokens in the following way: for each example with INLINEFORM0 source input documents, we take the first 500 INLINEFORM1 tokens from each source document. As some source documents may be shorter, we iteratively determine the number of tokens to take from each document until the 500 token quota is reached. Having determined the number of tokens per source document to use, we concatenate the truncated source documents into a single mega-document. This effectively reduces MDS to SDS on longer documents, a commonly-used assumption for recent neural MDS papers BIBREF10 , BIBREF38 , BIBREF11 . We chose 500 as our truncation size as related MDS work did not find significant improvement when increasing input length from 500 to 1000 tokens BIBREF38 . We simply introduce a special token between source documents to aid our models in detecting document-to-document relationships and leave direct modeling of this relationship, as well as modeling longer input sequences, to future work. We hope that the dataset we introduce will promote such work. For our Hi-MAP model, we applied a 1-layer bidirectional LSTM network, with the hidden state dimension 256 in each direction. The sentence representation dimension is also 256. We set the INLINEFORM2 to calculate the MMR value in Equation SECREF21 .
> 
> As our focus was on deep methods for MDS, we only tested several non-neural baselines. However, other classical methods deserve more attention, for which we refer the reader to Hong14 and leave the implementation of these methods on Multi-News for future work.

#### Relevance 1517

Label: 

#### Passage 1518

Retrieved by: BM25, Dense, Hybrid

> The number of collected Wayback links for summaries and their corresponding cited articles totals over 250,000. We only include examples with between 2 and 10 source documents per summary, as our goal is MDS, and the number of examples with more than 10 sources was minimal. The number of source articles per summary present, after downloading and processing the text to obtain the original article text, varies across the dataset, as shown in Table TABREF4 . We believe this setting reflects real-world situations; often for a new or specialized event there may be only a few news articles. Nonetheless, we would like to summarize these events in addition to others with greater news coverage.
> 
> We split our dataset into training (80%, 44,972), validation (10%, 5,622), and test (10%, 5,622) sets. Table TABREF5 compares Multi-News to other news datasets used in experiments below. We choose to compare Multi-News with DUC data from 2003 and 2004 and TAC 2011 data, which are typically used in multi-document settings. Additionally, we compare to the single-document CNNDM dataset, as this has been recently used in work which adapts SDS to MDS BIBREF11 . The number of examples in our Multi-News dataset is two orders of magnitude larger than previous MDS news data. The total number of words in the concatenated inputs is shorter than other MDS datasets, as those consist of 10 input documents, but larger than SDS datasets, as expected. Our summaries are notably longer than in other works, about 260 words on average. While compressing information into a shorter text is the goal of summarization, our dataset tests the ability of abstractive models to generate fluent text concise in meaning while also coherent in the entirety of its generally longer output, which we consider an interesting challenge.

#### Relevance 1518

Label: 

#### Passage 1519

Retrieved by: BM25, Dense, Hybrid

> Our dataset, which we call Multi-News, consists of news articles and human-written summaries of these articles from the site newser.com. Each summary is professionally written by editors and includes links to the original articles cited. We will release stable Wayback-archived links, and scripts to reproduce the dataset from these links. Our dataset is notably the first large-scale dataset for MDS on news articles. Our dataset also comes from a diverse set of news sources; over 1,500 sites appear as source documents 5 times or greater, as opposed to previous news datasets (DUC comes from 2 sources, CNNDM comes from CNN and Daily Mail respectively, and even the Newsroom dataset BIBREF6 covers only 38 news sources). A total of 20 editors contribute to 85% of the total summaries on newser.com. Thus we believe that this dataset allows for the summarization of diverse source documents and summaries.

#### Relevance 1519

Label: 

#### Passage 1520

Retrieved by: BM25, Hybrid

> In Table TABREF30 and Table TABREF31 we report ROUGE scores on DUC 2004 and Multi-News datasets respectively. We use DUC 2004, as results on this dataset are reported in lebanoff18mds, although this dataset is not the focus of this work. For results on DUC 2004, models were trained on the CNNDM dataset, as in lebanoff18mds. PG-BRNN and CopyTransformer models, which were pretrained by OpenNMT on CNNDM, were applied to DUC without additional training, analogous to PG-Original. We also experimented with training on Multi-News and testing on DUC data, but we did not see significant improvements. We attribute the generally low performance of pointer-generator, CopyTransformer and Hi-MAP to domain differences between DUC and CNNDM as well as DUC and Multi-News. These domain differences are evident in the statistics and extractive metrics discussed in Section 3.
> 
> Additionally, for both DUC and Multi-News testing, we experimented with using the output of 500 tokens from extractive methods (LexRank, TextRank and MMR) as input to the abstractive model. However, this did not improve results. We believe this is because our truncated input mirrors the First-3 baseline, which outperforms these three extractive methods and thus may provide more information as input to the abstractive model.
> 
> Our model outperforms PG-MMR when trained and tested on the Multi-News dataset. We see much-improved model performances when trained and tested on in-domain Multi-News data. The Transformer performs best in terms of R-1 while Hi-MAP outperforms it on R-2 and R-SU. Also, we notice a drop in performance between PG-original, and PG-MMR (which takes the pre-trained PG-original and applies MMR on top of the model). Our PG-MMR results correspond to PG-MMR w Cosine reported in lebanoff18mds. We trained their sentence regression model on Multi-News data and leave the investigation of transferring regression models from SDS to Multi-News for future work.
> 
> In addition to automatic evaluation, we performed human evaluation to compare the summaries produced. We used Best-Worst Scaling BIBREF39 , BIBREF40 , which has shown to be more reliable than rating scales BIBREF41 and has been used to evaluate summaries BIBREF42 , BIBREF32 . Annotators were presented with the same input that the systems saw at testing time; input documents were truncated, and we separated input

#### Relevance 1520

Label: 

#### Passage 1524

Retrieved by: Dense, Hybrid

> summarization datasets to MDS BIBREF11 , BIBREF12 , BIBREF13 .
> 
> However, data sparsity has largely been the bottleneck of the development of neural MDS systems. The creation of large-scale multi-document summarization dataset for training has been restricted due to the sparsity and cost of human-written summaries. liu18wikisum trains abstractive sequence-to-sequence models on a large corpus of Wikipedia text with citations and search engine results as input documents. However, no analogous dataset exists in the news domain. To bridge the gap, we introduce Multi-News, the first large-scale MDS news dataset, which contains 56,216 articles-summary pairs. We also propose a hierarchical model for neural abstractive multi-document summarization, which consists of a pointer-generator network BIBREF1 and an additional Maximal Marginal Relevance (MMR) BIBREF14 module that calculates sentence ranking scores based on relevancy and redundancy. We integrate sentence-level MMR scores into the pointer-generator model to adapt the attention weights on a word-level. Our model performs competitively on both our Multi-News dataset and the DUC 2004 dataset on ROUGE scores. We additionally perform human evaluation on several system outputs.
> 
> Our contributions are as follows: We introduce the first large-scale multi-document summarization datasets in the news domain. We propose an end-to-end method to incorporate MMR into pointer-generator networks. Finally, we benchmark various methods on our dataset to lay the foundations for future work on large-scale MDS.

#### Relevance 1524

Label: 

### BM25

#### Passage 1521

Retrieved by: BM25

> We report the percentage of n-grams in the gold summaries which do not appear in the input documents as a measure of how abstractive our summaries are in Table TABREF6 . As the table shows, the smaller MDS datasets tend to be more abstractive, but Multi-News is comparable and similar to the abstractiveness of SDS datasets. Grusky:18 additionally define three measures of the extractive nature of a dataset, which we use here for a comparison. We extend these notions to the multi-document setting by concatenating the source documents and treating them as a single input. Extractive fragment coverage is the percentage of words in the summary that are from the source article, measuring the extent to which a summary is derivative of a text: DISPLAYFORM0
> 
> where A is the article, S the summary, and INLINEFORM0 the set of all token sequences identified as extractive in a greedy manner; if there is a sequence of source tokens that is a prefix of the remainder of the summary, that is marked as extractive. Similarly, density is defined as the average length of the extractive fragment to which each summary word belongs: DISPLAYFORM0
> 
> Finally, compression ratio is defined as the word ratio between the articles and its summaries: DISPLAYFORM0
> 
> These numbers are plotted using kernel density estimation in Figure FIGREF11 . As explained above, our summaries are larger on average, which corresponds to a lower compression rate. The variability along the x-axis (fragment coverage), suggests variability in the percentage of copied words, with the DUC data varying the most. In terms of y-axis (fragment density), our dataset shows variability in the average length of copied sequence, suggesting varying styles of word sequence arrangement. Our dataset exhibits extractive characteristics similar to the CNNDM dataset.

#### Relevance 1521

Label: 

### Dense

#### Passage 1522

Retrieved by: Dense

> As discussed above, large scale datasets for multi-document news summarization are lacking. There have been several attempts to create MDS datasets in other domains. zopf18mds introduce a multi-lingual MDS dataset based on English and German Wikipedia articles as summaries to create a set of about 7,000 examples. liu18wikisum use Wikipedia as well, creating a dataset of over two million examples. That paper uses Wikipedia references as input documents but largely relies on Google search to increase topic coverage. We, however, are focused on the news domain, and the source articles in our dataset are specifically cited by the corresponding summaries. Related work has also focused on opinion summarization in the multi-document setting; angelidis18opinions introduces a dataset of 600 Amazon product reviews.

#### Relevance 1522

Label: 

#### Passage 1523

Retrieved by: Dense

> In this paper we introduce Multi-News, the first large-scale multi-document news summarization dataset. We hope that this dataset will promote work in multi-document summarization similar to the progress seen in the single-document case. Additionally, we introduce an end-to-end model which incorporates MMR into a pointer-generator network, which performs competitively compared to previous multi-document summarization models. We also benchmark methods on our dataset. In the future we plan to explore interactions among documents beyond concatenation and experiment with summarizing longer input documents.

#### Relevance 1523

Label: 

### Hybrid

None

## Question 0200

Paper: Generating Personalized Recipes from Historical User Preferences

> Where do they get the recipes from?

### Common Retrieved Chunks

#### Passage 1525

Retrieved by: BM25, Dense, Hybrid

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

#### Relevance 1525

Label: 

#### Passage 1526

Retrieved by: BM25, Hybrid

> For training and evaluation, we provide our model with the first 3-5 ingredients listed in each recipe. We decode recipe text via top-$k$ sampling BIBREF7, finding $k=3$ to produce satisfactory results. We use a hidden size $d_h=256$ for both the encoder and decoder. Embedding dimensions for vocabulary, ingredient, recipe, techniques, and caloric level are 300, 10, 50, 50, and 5 (respectively). For prior recipe attention, we set $k=20$, the 80th %-ile for the number of user interactions. We use the Adam optimizer BIBREF28 with a learning rate of $10^{-3}$, annealed with a decay rate of 0.9 BIBREF29. We also use teacher-forcing BIBREF30 in all training epochs.
> 
> In this work, we investigate how leveraging historical user preferences can improve generation quality over strong baselines in our setting. We compare our personalized models against two baselines. The first is a name-based Nearest-Neighbor model (NN). We initially adapted the Neural Checklist Model of BIBREF0 as a baseline; however, we ultimately use a simple Encoder-Decoder baseline with ingredient attention (Enc-Dec), which provides comparable performance and lower complexity. All personalized models outperform baseline in BPE perplexity (tab:metricsontest) with Prior Name performing the best. While our models exhibit comparable performance to baseline in BLEU-1/4 and ROUGE-L, we generate more diverse (Distinct-1/2: percentage of distinct unigrams and bigrams) and acceptable recipes. BLEU and ROUGE are not the most appropriate metrics for generation quality. A `correct' recipe can be written in many ways with the same main entities (ingredients). As BLEU-1/4 capture structural information via n-gram matching, they are not correlated with subjective recipe quality. This mirrors observations from BIBREF31, BIBREF8.
> 
> We observe that personalized models make more diverse recipes than baseline. They thus perform better in BLEU-1 with more key entities (ingredient mentions) present, but worse in BLEU-4, as these recipes are written in a personalized way and deviate from gold on the phrasal level. Similarly, the `Prior Name' model generates more unigram-diverse recipes than other personalized models and obtains a correspondingly lower BLEU-1 score.
> 
> Qualitative Analysis: We present sample outputs for a cocktail recipe in tab:samplerecipes, and additional recipes in the appendix. Generation quality progressively improves from generic baseline output to a blended cocktail produced by our best performing model. Models

#### Relevance 1526

Label: 

#### Passage 1529

Retrieved by: BM25, Dense, Hybrid

> lower BLEU-1 score.
> 
> Qualitative Analysis: We present sample outputs for a cocktail recipe in tab:samplerecipes, and additional recipes in the appendix. Generation quality progressively improves from generic baseline output to a blended cocktail produced by our best performing model. Models attending over prior recipes explicitly reference ingredients. The Prior Name model further suggests the addition of lemon and mint, which are reasonably associated with previously consumed recipes like coconut mousse and pork skewers.
> 
> Personalization: To measure personalization, we evaluate how closely the generated text corresponds to a particular user profile. We compute the likelihood of generated recipes using identical input specifications but conditioned on ten different user profiles—one `gold' user who consumed the original recipe, and nine randomly generated user profiles. Following BIBREF8, we expect the highest likelihood for the recipe conditioned on the gold user. We measure user matching accuracy (UMA)—the proportion where the gold user is ranked highest—and Mean Reciprocal Rank (MRR) BIBREF32 of the gold user. All personalized models beat baselines in both metrics, showing our models personalize generated recipes to the given user profiles. The Prior Name model achieves the best UMA and MRR by a large margin, revealing that prior recipe names are strong signals for personalization. Moreover, the addition of attention mechanisms to capture these signals improves language modeling performance over a strong non-personalized baseline.
> 
> Recipe Level Coherence: A plausible recipe should possess a coherent step order, and we evaluate this via a metric for recipe-level coherence. We use the neural scoring model from BIBREF33 to measure recipe-level coherence for each generated recipe. Each recipe step is encoded by BERT BIBREF34. Our scoring model is a GRU network that learns the overall recipe step ordering structure by minimizing the cosine similarity of recipe step hidden representations presented in the correct and reverse orders. Once pretrained, our scorer calculates the similarity of a generated recipe to the forward and backwards ordering of its corresponding gold label, giving a score equal to the difference between the former and latter. A higher score indicates better step ordering (with a maximum score of 2). tab:coherencemetrics shows that our personalized models achieve average recipe-level coherence scores of 1.78-1.82, surpassing the baseline at 1.77.
> 
> Recipe

#### Relevance 1529

Label: 

#### Passage 1530

Retrieved by: Dense, Hybrid

> We collect a novel dataset of 230K+ recipe texts and 1M+ user interactions (reviews) over 18 years (2000-2018) from Food.com. Here, we restrict to recipes with at least 3 steps, and at least 4 and no more than 20 ingredients. We discard users with fewer than 4 reviews, giving 180K+ recipes and 700K+ reviews, with splits as in tab:recipeixnstats.
> 
> Our model must learn to generate from a diverse recipe space: in our training data, the average recipe length is 117 tokens with a maximum of 256. There are 13K unique ingredients across all recipes. Rare words dominate the vocabulary: 95% of words appear $<$100 times, accounting for only 1.65% of all word usage. As such, we perform Byte-Pair Encoding (BPE) tokenization BIBREF25, BIBREF26, giving a training vocabulary of 15K tokens across 19M total mentions. User profiles are similarly diverse: 50% of users have consumed $\le $6 recipes, while 10% of users have consumed $>$45 recipes.
> 
> We order reviews by timestamp, keeping the most recent review for each user as the test set, the second most recent for validation, and the remainder for training (sequential leave-one-out evaluation BIBREF27). We evaluate only on recipes not in the training set.
> 
> We manually construct a list of 58 cooking techniques from 384 cooking actions collected by BIBREF15; the most common techniques (bake, combine, pour, boil) account for 36.5% of technique mentions. We approximate technique adherence via string match between the recipe text and technique list.

#### Relevance 1530

Label: 

#### Passage 1531

Retrieved by: Dense, Hybrid

> Our raw data consists of 270K recipes and 1.4M user-recipe interactions (reviews) scraped from Food.com, covering a period of 18 years (January 2000 to December 2018). See tab:int-stats for dataset summary statistics, and tab:samplegk for sample information about one user-recipe interaction and the recipe involved.

#### Relevance 1531

Label: 

### BM25

#### Passage 1527

Retrieved by: BM25

> We prepared a set of 15 pairwise comparisons per evaluation session, and collected 930 pairwise evaluations (310 per personalized model) over 62 sessions. For each pair, users were given a partial recipe specification (name and 3-5 key ingredients), as well as two generated recipes labeled `A' and `B'. One recipe is generated from our baseline encoder-decoder model and one recipe is generated by one of our three personalized models (Prior Tech, Prior Name, Prior Recipe). The order of recipe presentation (A/B) is randomly selected for each question. A screenshot of the user evaluation interface is given in fig:exeval. We ask the user to indicate which recipe they find more coherent, and which recipe best accomplishes the goal indicated by the recipe name. A screenshot of this survey interface is given in fig:exeval2.

#### Relevance 1527

Label: 

#### Passage 1528

Retrieved by: BM25

> and (2) techniques seen therein (defined in data). BIBREF19, BIBREF20, BIBREF21 explore similar schemes for personalized recommendation.
> 
> Prior Recipe Attention: We obtain the set of prior recipes for a user $u$: $R^+_u$, where each recipe can be represented by an embedding from a recipe embedding layer $\mathcal {R}$ or an average of the name tokens embedded by $\mathcal {V}$. We attend over the $k$-most recent prior recipes, $R^{k+}_u$, to account for temporal drift of user preferences BIBREF22. These embeddings are used in the `Prior Recipe' and `Prior Name' models, respectively.
> 
> Given a recipe representation $\mathbf {r} \in \mathbb {R}^{d_r}$ (where $d_r$ is recipe- or vocabulary-embedding size depending on the recipe representation) the prior recipe attention context $\mathbf {a}_{t}^{r_u}$ is calculated as
> 
> Prior Technique Attention: We calculate prior technique preference (used in the `Prior Tech` model) by normalizing co-occurrence between users and techniques seen in $R^+_u$, to obtain a preference vector $\rho _{u}$. Each technique $x$ is embedded via a technique embedding layer $\mathcal {X}$ to $\mathbf {x}\in \mathbb {R}^{d_x}$. Prior technique attention is calculated as
> 
> where, inspired by copy mechanisms BIBREF23, BIBREF24, we add $\rho _{u,x}$ for technique $x$ to emphasize the attention by the user's prior technique preference.
> 
> Attention Fusion Layer: We fuse all contexts calculated at time $t$, concatenating them with decoder GRU output and previous token embedding:
> 
> We then calculate the token probability:
> 
> and maximize the log-likelihood of the generated sequence conditioned on input specifications and user preferences. fig:ex shows a case where the Prior Name model attends strongly on previously consumed savory recipes to suggest the usage of an additional ingredient (`cilantro').

#### Relevance 1528

Label: 

### Dense

#### Passage 1532

Retrieved by: Dense

> In this paper, we propose a novel task: to generate personalized recipes from incomplete input specifications and user histories. On a large novel dataset of 180K recipes and 700K reviews, we show that our personalized generative models can generate plausible, personalized, and coherent recipes preferred by human evaluators for consumption. We also introduce a set of automatic coherence measures for instructional texts as well as personalization metrics to support our claims. Our future work includes generating structured representations of recipes to handle ingredient properties, as well as accounting for references to collections of ingredients (e.g. “dry mix").
> 
> Acknowledgements. This work is partly supported by NSF #1750063. We thank all reviewers for their constructive suggestions, as well as Rei M., Sujoy P., Alicia L., Eric H., Tim S., Kathy C., Allen C., and Micah I. for their feedback.

#### Relevance 1532

Label: 

### Hybrid

None
