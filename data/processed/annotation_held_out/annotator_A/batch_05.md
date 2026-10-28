# Passage relevance annotation

Annotator: 

Judge whether the passage provides information that helps answer the question, including useful partial evidence. Topic overlap alone is not sufficient. Judge only the supplied question and passage.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Do not change record numbers, questions or passages. Work independently without consulting another annotator or reference answers.

## Record 0401

Paper: NeuronBlocks: Building Your NLP DNN Models Like Playing Lego

### Question

> What neural network modules are included in NeuronBlocks?

### Passage

> We recognize the following major functional categories of neural network components. Each category covers as many commonly used modules as possible. The Block Zoo is an open framework, and more modules can be added in the future.
> 
> [itemsep= -0.4em,topsep = 0.3em, align=left, labelsep=-0.6em, leftmargin=1.2em]
> 
> Embedding Layer: Word/character embedding and extra handcrafted feature embedding such as pos-tagging are supported.
> 
> Neural Network Layers: Block zoo provides common layers like RNN, CNN, QRNN BIBREF2 , Transformer BIBREF3 , Highway network, Encoder Decoder architecture, etc. Furthermore, attention mechanisms are widely used in neural networks. Thus we also support multiple attention layers, such as Linear/Bi-linear Attention, Full Attention BIBREF4 , Bidirectional attention flow BIBREF5 , etc. Meanwhile, regularization layers such as Dropout, Layer Norm, Batch Norm, etc are also supported for improving generalization ability.
> 
> Loss Function: Besides of the loss functions built in PyTorch, we offer more options such as Focal Loss BIBREF6 .
> 
> Metrics: For classification task, AUC, Accuracy, Precision/Recall, F1 metrics are supported. For sequence labeling task, F1/Accuracy are supported. For knowledge distillation task, MSE/RMSE are supported. For MRC task, ExactMatch/F1 are supported.

### Relevance

Label: 

## Record 0402

Paper: NeuronBlocks: Building Your NLP DNN Models Like Playing Lego

### Question

> What neural network modules are included in NeuronBlocks?

### Passage

> The Neuronblocks is built on PyTorch. The overall framework is illustrated in Figure FIGREF16 . It consists of two layers: the Block Zoo and the Model Zoo. In Block Zoo, the most commonly used components of deep neural networks are categorized into several groups according to their functions. Within each category, several alternative components are encapsulated into standard and reusable blocks with a consistent interface. These blocks serve as basic and exchangeable units to construct complex network architectures for different NLP tasks. In Model Zoo, the most popular NLP tasks are identified. For each task, several end-to-end network templates are provided in the form of JSON configuration files. Users can simply browse these configurations and choose one or more to instantiate. The whole task can be completed without any coding efforts.

### Relevance

Label: 

## Record 0403

Paper: NeuronBlocks: Building Your NLP DNN Models Like Playing Lego

### Question

> What neural network modules are included in NeuronBlocks?

### Passage

> Deep Neural Networks (DNN) have been widely employed in industry for solving various Natural Language Processing (NLP) tasks, such as text classification, sequence labeling, question answering, etc. However, when engineers apply DNN models to address specific NLP tasks, they often face the following challenges.
> 
> The above challenges often hinder the productivity of engineers, and result in less optimal solutions to their given tasks. This motivates us to develop an NLP toolkit for DNN models, which facilitates engineers to develop DNN approaches. Before designing this NLP toolkit, we conducted a survey among engineers and identified a spectrum of three typical personas.
> 
> To satisfy the requirements of all the above three personas, the NLP toolkit has to be generic enough to cover as many tasks as possible. At the same time, it also needs to be flexible enough to allow alternative network architectures as well as customized modules. Therefore, we analyzed the NLP jobs submitted to a commercial centralized GPU cluster. Table TABREF11 showed that about 87.5% NLP related jobs belong to a few common tasks, including sentence classification, text matching, sequence labeling, MRC, etc. It further suggested that more than 90% of the networks were composed of several common components, such as embedding, CNN/RNN, Transformer and so on.
> 
> Based on the above observations, we developed NeuronBlocks, a DNN toolkit for NLP tasks. The basic idea is to provide two layers of support to the engineers. The upper layer targets common NLP tasks. For each task, the toolkit contains several end-to-end network templates, which can be immediately instantiated with simple configuration. The bottom layer consists of a suite of reusable and standard components, which can be adopted as building blocks to construct networks with complex architecture. By following the interface guidelines, users can also contribute to this gallery of components with their own modules.
> 
> The technical contributions of NeuronBlocks are summarized into the following three aspects.

### Relevance

Label: 

## Record 0404

Paper: NeuronBlocks: Building Your NLP DNN Models Like Playing Lego

### Question

> What neural network modules are included in NeuronBlocks?

### Passage

> In this paper, we introduce NeuronBlocks, a DNN toolkit for NLP tasks built on PyTorch. NeuronBlocks targets three types of engineers, and provides a two-layer solution to satisfy the requirements from all three types of users. To be more specific, the Model Zoo consists of various templates for the most common NLP tasks, while the Block Zoo supplies a gallery of alternative layers/modules for the networks. Such design achieves a balance between generality and flexibility. Extensive experiments have verified the effectiveness of this approach. NeuronBlocks has been widely used in a product team of a commercial search engine, and significantly improved the productivity for developing NLP DNN approaches.
> 
> As an open-source toolkit, we will further extend it in various directions. The following names a few examples.

### Relevance

Label: 

## Record 0405

Paper: NeuronBlocks: Building Your NLP DNN Models Like Playing Lego

### Question

> What neural network modules are included in NeuronBlocks?

### Passage

> There are several general-purpose deep learning frameworks, such as TensorFlow, PyTorch and Keras, which have gained popularity in NLP community. These frameworks offer huge flexibility in DNN model design and support various NLP tasks. However, building models under these frameworks requires a large overhead of mastering these framework details. Therefore, higher level abstraction to hide the framework details is favored by many engineers.
> 
> There are also several popular deep learning toolkits in NLP, including OpenNMT BIBREF0 , AllenNLP BIBREF1 etc. OpenNMT is an open-source toolkit mainly targeting neural machine translation or other natural language generation tasks. AllenNLP provides several pre-built models for NLP tasks, such as semantic role labeling, machine comprehension, textual entailment, etc. Although these toolkits reduce the development cost, they are limited to certain tasks, and thus not flexible enough to support new network architectures or new components.

### Relevance

Label: 

## Record 0406

Paper: Clinical Information Extraction via Convolutional Neural Network

### Question

> What dataset did they use to evaluate?

### Passage

> All of the tasks were evaluated using the standard metrics of precision(P), recall(R) and INLINEFORM0 : DISPLAYFORM0
> 
> where INLINEFORM0 is the set of items predicted by the system and INLINEFORM1 is the set of items manually annotated by the humans. Applying these metrics of the tasks only requires a definition of what is considered an "item" for each task. For evaluating the spans of event expressions, items were tuples of character offsets. Thus, system only received credit for identifying events with exactly the same character offsets as the manually annotated ones. For evaluating the attributes of event expression types, items were tuples of (begin, end, value) where begin and end are character offsets and value is the value that was given to the relevant attribute. Thus, systems only received credit for an event attribute if they both found an event with correct character offsets and then assigned the correct value for that attribute BIBREF10 .

### Relevance

Label: 

## Record 0407

Paper: Clinical Information Extraction via Convolutional Neural Network

### Question

> What dataset did they use to evaluate?

### Passage

> The major advantage of our system is that we only leverage NLTK tokenization and a POS tagger to preprocess our training dataset. When implementing our neural network based clinical information extraction system, we found it is not easy to construct high quality training data due to the noisy format of clinical notes. Choosing the proper tokenizer is quite important for span identification. After several experiments, we found "RegexpTokenizer" can match our needs. This tokenizer can generate spans for each token via sophisticated regular expression like below,

### Relevance

Label: 

## Record 0408

Paper: Clinical Information Extraction via Convolutional Neural Network

### Question

> What dataset did they use to evaluate?

### Passage

> We use the Clinical TempEval corpus as the evaluation dataset. This corpus was based on a set of 600 clinical notes and pathology reports from cancer patients at the Mayo Clinic. These notes were manually de-identified by the Mayo Clinic to replace names, locations, etc. with generic placeholders, but time expression were not altered. The notes were then manually annotated with times, events and temporal relations in clinical notes. These annotations include time expression types, event attributes and an increased focus on temporal relations. The event, time and temporal relation annotations were distributed separately from the text using the Anafora standoff format. Table TABREF19 shows the number of documents, event expressions in the training, development and testing portions of the 2016 THYME data.

### Relevance

Label: 

## Record 0409

Paper: Clinical Information Extraction via Convolutional Neural Network

### Question

> What dataset did they use to evaluate?

### Passage

> learn hidden feature representations directly from raw clinical notes. More specifically, one method first extract a window of surrounding words for the candidate word. Then, we attach each word with their part-of-speech tag and shape information as extra features. Then our system deploys a temporal convolution neural network to learn hidden feature representations. Finally, our system uses Multilayer Perceptron (MLP) to predict event spans. Note that we use the same model to predict event attributes.

### Relevance

Label: 

## Record 0410

Paper: Clinical Information Extraction via Convolutional Neural Network

### Question

> What dataset did they use to evaluate?

### Passage

> The way we use temporal convlution neural network for event span and attribute classification is similar with the approach proposed by BIBREF0 . Generally speaking, we can consider a word as represented by INLINEFORM0 discrete features INLINEFORM1 , where INLINEFORM2 is the dictionary for the INLINEFORM3 feature. In our scenario, we just use three features such as token mention, pos tag and word shape. Note that word shape features are used to represent the abstract letter pattern of the word by mapping lower-case letters to “x”, upper-case to “X”, numbers to “d”, and retaining punctuation. We associate to each feature a lookup table. Given a word, a feature vector is then obtained by concatenating all lookup table outputs. Then a clinical snippet is transformed into a word embedding matrix. The matrix can be fed to further 1-dimension convolutional neural network and max pooling layers. Below we will briefly introduce core concepts of Convoluational Neural Network (CNN).
> 
> Temporal Convolution applies one-dimensional convolution over the input sequence. The one-dimensional convolution is an operation between a vector of weights INLINEFORM0 and a vector of inputs viewed as a sequence INLINEFORM1 . The vector INLINEFORM2 is the filter of the convolution. Concretely, we think of INLINEFORM3 as the input sentence and INLINEFORM4 as a single feature value associated with the INLINEFORM5 -th word in the sentence. The idea behind the one-dimensional convolution is to take the dot product of the vector INLINEFORM6 with each INLINEFORM7 -gram in the sentence INLINEFORM8 to obtain another sequence INLINEFORM9 : DISPLAYFORM0
> 
> Usually, INLINEFORM0 is not a single value, but a INLINEFORM1 -dimensional word vector so that INLINEFORM2 . There exist two types of 1d convolution operations. One was introduced by BIBREF9 and also known as Time Delay Neural Networks (TDNNs). The other one was introduced by BIBREF0 . In TDNN, weights INLINEFORM3 form a matrix. Each row of INLINEFORM4 is convolved with the corresponding row of INLINEFORM5 . In BIBREF0 architecture, a sequence of length INLINEFORM6 is represented as: DISPLAYFORM0
> 
> where INLINEFORM0 is the concatenation operation. In general, let INLINEFORM1 refer to the concatenation of words INLINEFORM2 . A convolution operation involves a filter INLINEFORM3 , which is applied to a window of

### Relevance

Label: 

## Record 0411

Paper: A Multi-task Learning Model for Chinese-oriented Aspect Polarity Classification and Aspect Term Extraction

### Question

> In what four Chinese review datasets does LCF-ATEPC achieves state of the art?

### Passage

> The ATE and APC subtasks were treated as independent tasks in previous studies. Moreover, the multi-task learning model for ATE and APC subtasks has not attracted enough attention from researchers. Besides, the researches concerning the Chinese language-oriented ABSA task are not sufficient and urgent to be proposed and developed. To address the above problems, this paper proposes a multi-task learning model LCF-ATEPC for aspect-based sentiment analysis based on the MHSA and the LCF mechanisms and applies the pre-trained BERT to the ATE sub-tasks for the first time. Not only for the Chinese language, but the models proposed in this paper are multilingual and applicable to the classic English review sentiment analysis task, such as the SemEval-2014 task4. The proposed model can automatically extract aspects from reviews and infer aspects' polarity. Empirical results on 3 commonly English datasets and four Chinese review datasets for ABSA tasks show that, compared with all models based on basic BERT, the LCF-ATEPC model achieves state-of-the-art performance on ATE and APC tasks.

### Relevance

Label: 

## Record 0412

Paper: A Multi-task Learning Model for Chinese-oriented Aspect Polarity Classification and Aspect Term Extraction

### Question

> In what four Chinese review datasets does LCF-ATEPC achieves state of the art?

### Passage

> We compare the LCF-ATEPC model to current state-of-the-art methods. Experimental results show that the proposed model achieves state-of-the-art performance both in the ATE and APC tasks.
> 
> ATAE-LSTM BIBREF6 is a classical LSTM-based network for the APC task, which applies the attention mechanism to focus on the important words in the context. Besides, ATAE-LSTM appends aspect embedding and the learned features to make full use of the aspect features. The ATAE-LSTM can be adapted to the Chinese review datasets.
> 
> ATSM-S BIBREF29 is a baseline model of the ATSM variations for Chinese language-oriented ABSA task. This model learns the sentence and aspect terms at three perspectives of granularity.
> 
> GANN is novel neural network model for APC task aimed to solve the shortcomings of traditional RNNs and CNNs. The GANN applied the Gate Truncation RNN (GTR) to learn informative aspect-dependent sentiment clue representations. GANN obtained the state-of-the-art APC performance on the Chinese review datasets.
> 
> AEN-BERT BIBREF9 is an attentional encoder network based on the pretrained BERT model, which aims to solve the aspect polarity classification.
> 
> BERT-PT BIBREF37 is a BERT-adapted model for Review Reading Comprehension (RRC) task, a task inspired by machine reading comprehension (MRC), it could be adapted to aspect-level sentiment classification task.
> 
> BERT-BASE BIBREF16 is the basic pretrained BERT model. We adapt it to ABSA multi-task learning, which equips the same ability to automatically extract aspect terms and classify aspects polarity as LCF-ATEPC model.
> 
> BERT-SPC BIBREF9 is a pretrained BERT model designed for the sentence-pair classification task. Consistent with the basic BERT model, we implemented this model for ABSA multitasking.
> 
> BERT-ADA BIBREF33 is a domain-adapted BERT-based model proposed for the APC task, which fine-tuned the BERT-BASE model on task-related corpus. This model obtained state-of-the-art accuracy on the Laptops dataset.
> 
> LCF-ATEPC is the multi-task learning model for the ATE and APC tasks, which is based on the the BERT-SPC model and local context focus mechanism.
> 
> LCF-ATE are the variations of the LCF-ATEPC model which only optimize for the ATE task.
> 
> LCF-APC are the variations of LCF-ATEPC and it only optimize for the APC task during training process.

### Relevance

Label: 

## Record 0413

Paper: A Multi-task Learning Model for Chinese-oriented Aspect Polarity Classification and Aspect Term Extraction

### Question

> In what four Chinese review datasets does LCF-ATEPC achieves state of the art?

### Passage

> (NER) task, the ATE task is a sequence labeling task, which aims to extract aspects from the reviews or tweet. In most researches BIBREF13, BIBREF14, BIBREF15, the ATE task is studied independently, away from the APC task. The ATE task first segments a review into separate tokens and then infers whether the tokens belong to any aspect. The tokens may be labeled in different forms in different studies, but most of the studies have adopted the IOB label to annotate tokens.
> 
> Aiming to automatically extract aspects from the text efficiently and analyze the sentiment polarity of aspects simultaneously, this paper proposes a multi-task learning model for aspect-based sentiment analysis. Multilingual processing is an important research orientation of natural language processing. The LCF-ATEPC model proposed in this paper is a novel multilingual and multi-task-oriented model. Apart from achieving state-of-the-art performance in commonly used SemEval-2014 task4 datasets, the experimental results in four Chinese review datasets also validate that this model has a strong ability to expand and adapt to the needs of multilingual task. The proposed model is based on multi-head self-attention (MHSA) and integrates the pre-trained BERT BIBREF16 and the local context focus mechanism, namely LCF-ATEPC. By training on a small amount of annotated data of aspect and their polarity, the model can be adapted to a large-scale dataset, automatically extracting the aspects and predicting the sentiment polarities. In this way, the model can discover the unknown aspects and avoids the tedious and huge cost of manually annotating all aspects and polarities. It is of great significance for the field-specific aspect-based sentiment analysis.
> 
> The main contributions of this article are as follows:
> 
> For the first time, this paper studies the multi-task model of APC subtask and ATE subtask for multilingual reviews, which provides a new idea for the research of Chinese aspect extraction.
> 
> This paper firstly applies self-attention and local context focus techniques to aspect word extraction task, and fully explore their potential in aspect term extraction task.
> 
> The LCF-ATEPC model proposed in this paper integrates the pre-trained BERT model, significantly improves both the performance of ATE task and APC subtask, and achieves new state-of-the-art performance especially the F1 score of ATE task. Besides, we adopted

### Relevance

Label: 

## Record 0414

Paper: A Multi-task Learning Model for Chinese-oriented Aspect Polarity Classification and Aspect Term Extraction

### Question

> In what four Chinese review datasets does LCF-ATEPC achieves state of the art?

### Passage

> extraction task.
> 
> The LCF-ATEPC model proposed in this paper integrates the pre-trained BERT model, significantly improves both the performance of ATE task and APC subtask, and achieves new state-of-the-art performance especially the F1 score of ATE task. Besides, we adopted the domain-adapted BERT model trained on the domain-related corpus to the ABSA joint-task learning model. The experimental results show that the domain-adapted BERT model significantly promotes the performance of APC tasks on the three datasets, especially the Restaurant dataset.
> 
> We designed and applied dual labels for the input sequence applicable for the SemEval-2014 and Chinese review datasets of ABSA joint-task, the aspect term label, and the sentiment polarity label, respectively. The dual label improves the learning efficiency of the proposed model.

### Relevance

Label: 

## Record 0415

Paper: A Multi-task Learning Model for Chinese-oriented Aspect Polarity Classification and Aspect Term Extraction

### Question

> In what four Chinese review datasets does LCF-ATEPC achieves state of the art?

### Passage

> Table TABREF70 are the experimental results of LCF-ATEPC models on four Chinese review datasets.

### Relevance

Label: 

## Record 0416

Paper: Unsupervised Learning of Sentence Embeddings using Compositional n-Gram Features

### Question

> Do they report results only on English data?

### Passage

> of how one predicts the content of the sentence (the question) but a good measure of how the next sentence in the sequence (the answer) is predicted.
> 
> Unsupervised Similarity Evaluation Results. In Table TABREF19 , we see that our Sent2Vec models are state-of-the-art on the majority of tasks when comparing to all the unsupervised models trained on the Toronto corpus, and clearly achieve the best averaged performance. Our Sent2Vec models also on average outperform or are at par with the C-PHRASE model, despite significantly lagging behind on the STS 2014 WordNet and News subtasks. This observation can be attributed to the fact that a big chunk of the data that the C-PHRASE model is trained on comes from English Wikipedia, helping it to perform well on datasets involving definition and news items. Also, C-PHRASE uses data three times the size of the Toronto book corpus. Interestingly, our model outperforms C-PHRASE when trained on Wikipedia, as shown in Table TABREF21 , despite the fact that we use no parse tree information. Official STS 2017 benchmark. In the official results of the most recent edition of the STS 2017 benchmark BIBREF35 , our model also significantly outperforms C-PHRASE, and in fact delivers the best unsupervised baseline method.
> 
> For the Siamese C-BOW model trained on the Toronto corpus, supervised evaluation as well as similarity evaluation results on the SICK 2014 dataset are unavailable.
> 
> Macro Average. To summarize our contributions on both supervised and unsupervised tasks, in Table TABREF21 we present the results in terms of the macro average over the averages of both supervised and unsupervised tasks along with the training times of the models. For unsupervised tasks, averages are taken over both Spearman and Pearson scores. The comparison includes the best performing unsupervised and semi-supervised methods described in Section SECREF3 . For models trained on the Toronto books dataset, we report a 3.8 INLINEFORM0 points improvement over the state of the art. Considering all supervised, semi-supervised methods and all datasets compared in BIBREF16 , we report a 2.2 INLINEFORM1 points improvement.
> 
> We also see a noticeable improvement in accuracy as we use larger datasets like Twitter and Wikipedia. We furthermore see that the Sent2Vec models are faster

### Relevance

Label: 

## Record 0417

Paper: Unsupervised Learning of Sentence Embeddings using Compositional n-Gram Features

### Question

> Do they report results only on English data?

### Passage

> and all datasets compared in BIBREF16 , we report a 2.2 INLINEFORM1 points improvement.
> 
> We also see a noticeable improvement in accuracy as we use larger datasets like Twitter and Wikipedia. We furthermore see that the Sent2Vec models are faster to train when compared to methods like SkipThought and DictRep, owing to the SGD optimizer allowing a high degree of parallelizability.
> 
> We can clearly see Sent2Vec outperforming other unsupervised and even semi-supervised methods. This can be attributed to the superior generalizability of our model across supervised and unsupervised tasks.
> 
> Comparison with BIBREF4 . We also compare our work with BIBREF4 who also use additive compositionality to obtain sentence embeddings. However, in contrast to our model, they use fixed, pre-trained word embeddings to build a weighted average of these embeddings using unigram probabilities. While we couldn't find pre-trained state of the art word embeddings trained on the Toronto books corpus, we evaluated their method using GloVe embeddings obtained from the larger Common Crawl Corpus, which is 42 times larger than our twitter corpus, greatly favoring their method over ours.
> 
> In Table TABREF22 , we report an experimental comparison to their model on unsupervised tasks. In the table, the suffix W indicates that their down-weighting scheme has been used, while the suffix R indicates the removal of the first principal component. They report values of INLINEFORM0 as giving the best results and used INLINEFORM1 for all their experiments. We observe that our results are competitive with the embeddings of BIBREF4 for purely unsupervised methods. It is important to note that the scores obtained from supervised task-specific PSL embeddings trained for the purpose of semantic similarity outperform our method on both SICK and average STS 2014, which is expected as our model is trained purely unsupervised.
> 
> In order to facilitate a more detailed comparison, we also evaluated the unsupervised Glove + WR embeddings on downstream supervised tasks and compared them to our twitter models. To use BIBREF4 's method in a supervised setup, we precomputed and stored the common discourse vector INLINEFORM0 using 2 million random Wikipedia sentences. On an average, our models outperform their unsupervised models by a significant margin, this despite the fact that they used

### Relevance

Label: 

## Record 0418

Paper: Unsupervised Learning of Sentence Embeddings using Compositional n-Gram Features

### Question

> Do they report results only on English data?

### Passage

> In Tables TABREF18 and TABREF19 , we compare our results with those obtained by BIBREF16 on different models. Table TABREF21 in the last column shows the dramatic improvement in training time of our models (and other C-BOW-inspired models) in contrast to neural network based models. All our Sent2Vec models are trained on a machine with 2x Intel Xeon E5 INLINEFORM0 2680v3, 12 cores @2.5GHz.
> 
> Along with the models discussed in Section SECREF3 , this also includes the sentence embedding baselines obtained by simple averaging of word embeddings over the sentence, in both the C-BOW and skip-gram variants. TF-IDF BOW is a representation consisting of the counts of the 200,000 most common feature-words, weighed by their TF-IDF frequencies. To ensure coherence, we only include unsupervised models in the main paper. Performance of supervised and semi-supervised models on these evaluations can be observed in Tables TABREF29 and TABREF30 in the supplementary material.
> 
> Downstream Supervised Evaluation Results. On running supervised evaluations and observing the results in Table TABREF18 , we find that on an average our models are second only to SkipThought vectors. Also, both our models achieve state of the art results on the CR task. We also observe that on half of the supervised tasks, our unigrams + bigram model is the best model after SkipThought. Our models are weaker on the MSRP task (which consists of the identification of labelled paraphrases) compared to state-of-the-art methods. However, we observe that the models which perform very strongly on this task end up faring very poorly on the other tasks, indicating a lack of generalizability. On rest of the tasks, our models perform extremely well. The SkipThought model is able to outperform our models on most of the tasks as it is trained to predict the previous and next sentences and a lot of tasks are able to make use of this contextual information missing in our Sent2Vec models. For example, the TREC task is a poor measure of how one predicts the content of the sentence (the question) but a good measure of how the next sentence in the sequence (the answer) is predicted.
> 
> Unsupervised Similarity Evaluation Results. In Table TABREF19 , we see that our Sent2Vec

### Relevance

Label: 

## Record 0419

Paper: Unsupervised Learning of Sentence Embeddings using Compositional n-Gram Features

### Question

> Do they report results only on English data?

### Passage

> C-BOW BIBREF0 , BIBREF1 aims to predict a chosen target word given its fixed-size context window, the context being defined by the average of the vectors associated with the words at a distance less than the window size hyper-parameter INLINEFORM0 . If our system, when restricted to unigram features, can be seen as an extension of C-BOW where the context window includes the entire sentence, in practice there are few important differences as C-BOW uses important tricks to facilitate the learning of word embeddings. C-BOW first uses frequent word subsampling on the sentences, deciding to discard each token INLINEFORM1 with probability INLINEFORM2 or alike (small variations exist across implementations). Subsampling prevents the generation of n-grams features, and deprives the sentence of an important part of its syntactical features. It also shortens the distance between subsampled words, implicitly increasing the span of the context window. A second trick consists of using dynamic context windows: for each subsampled word INLINEFORM3 , the size of its associated context window is sampled uniformly between 1 and INLINEFORM4 . Using dynamic context windows is equivalent to weighing by the distance from the focus word INLINEFORM5 divided by the window size BIBREF9 . This makes the prediction task local, and go against our objective of creating sentence embeddings as we want to learn how to compose all n-gram features present in a sentence. In the results section, we report a significant improvement of our method over C-BOW.

### Relevance

Label: 

## Record 0420

Paper: Unsupervised Learning of Sentence Embeddings using Compositional n-Gram Features

### Question

> Do they report results only on English data?

### Passage

> We discuss existing models which have been proposed to construct sentence embeddings. While there is a large body of works in this direction – several among these using e.g. labelled datasets of paraphrase pairs to obtain sentence embeddings in a supervised manner BIBREF12 , BIBREF3 , BIBREF13 to learn sentence embeddings – we here focus on unsupervised, task-independent models. While some methods require ordered raw text i.e., a coherent corpus where the next sentence is a logical continuation of the previous sentence, others rely only on raw text i.e., an unordered collection of sentences. Finally, we also discuss alternative models built from structured data sources.

### Relevance

Label: 

## Record 0421

Paper: Attributed Multi-Relational Attention Network for Fact-checking URL Recommendation

### Question

> What dataset is used?

### Passage

> In this section, we describe a dataset, baselines, experimental setting, and experimental results. In the experiments, we seek to answer the following research questions:
> 
> RQ1: What is the performance of our model and baselines?
> 
> RQ2: How beneficial is each submodule of our model?
> 
> RQ3: How effective is our attention mechanisms?
> 
> RQ4: What is sensitivity of our model with regard to hyperparameters?

### Relevance

Label: 

## Record 0422

Paper: Attributed Multi-Relational Attention Network for Fact-checking URL Recommendation

### Question

> What dataset is used?

### Passage

> We adopt the leave-one-out evaluation protocol to evaluate the performance of our model and baselines. The leave-one-out evaluation protocol has been widely used in top-K recommendation tasks. In particular, we held the latest interaction of each user as the test set and used the remaining interactions for training. Each testing instance was paired with 99 randomly sampled negative instances. Each recommendation model ranks the 100 instances according to its predicted results. The ranked list is judged by Hit Ratio (HR) BIBREF49 and Normalized Discount Cumulative Gain (NDCG) BIBREF50 at the position 10. HR@10 is a recall-based metric, measuring the percentage of the testing item being correctly recommended in the top-10 position. NDCG@10 is a ranked evaluation metric which considers the position of the correct hit in the ranked result. Since both modules in our framework introduce randomness, we repeat each experiment 5 times with different weight initialization and randomly selecting neighbors. We report the average score of the best performance in each training process for both metrics to ensure the robustness of our framework.

### Relevance

Label: 

## Record 0423

Paper: Attributed Multi-Relational Attention Network for Fact-checking URL Recommendation

### Question

> What dataset is used?

### Passage

> We evaluate our proposed model on a Twitter dataset obtained from the authors of BIBREF12. The interaction behavior collected in the dataset is consistent with our definition in SECREF3. As they did for their study, we only kept users who have at least three interactions (i.e., posting at least three fact-checking messages containing fact-checking URLs). We conducted additional preprocessing step by removing users whose posts are non-English, or their tweets were inaccessible, because some of our baselines require a fact-checker's tweets. Our final dataset consists of 11,576 users (i.e, fact-checkers), 4,732 fact-checking URLs and 63,429 interactions. The dataset also contains each user's social network information. Note that each user's social relationship is restricted within available users in the dataset. And we further take available feature values of both user and URL into consideration. For instance, a category of referred fact-checking article and the name of corresponding fact-checking website reveals linguistic characteristics such as writing style and topical interest of each URL; while the number of followers and number of followees of each user indicates the credibility and influence of the fact-checker. Statistics of the final dataset is presented in Table TABREF65.

### Relevance

Label: 

## Record 0424

Paper: Attributed Multi-Relational Attention Network for Fact-checking URL Recommendation

### Question

> What dataset is used?

### Passage

> Let $\mathcal {U} = \lbrace u_1,u_2,...,u_n\rbrace $ denotes a set of fact-checkers on social media, and use $\mathcal {C} = \lbrace c_1,c_2,...,c_m\rbrace $ to index fact-checking URLs. We construct user-URL interaction matrix $Y = \lbrace y_{ij} | u\in \mathcal {U}, v \in \mathcal {C} \rbrace $ according to users' fact-checking behavior, where
> 
> each value of 1 for $y_{ij}$ indicates the existence of implicit interaction between target user $i$ and target URL $j$. Each user $u_i$ and each URL $c_j$ associate with a set of attributes. The goal of the recommendation task is to recommend top-N URLs from the URL set $\mathcal {C}$ to each user.
> 
> We also construct the entire dataset as a heterogeneous graph, which is a special kind of information network that consists of either multiple types of objects or different types of links, or both.

### Relevance

Label: 

## Record 0425

Paper: Attributed Multi-Relational Attention Network for Fact-checking URL Recommendation

### Question

> What dataset is used?

### Passage

> of high-order connectivity in user-item bipartite graph by performing embedding propagation.
> 
> Table TABREF66 presents characteristics of baselines and our model, showing what information each model utilizes. Note that even though CMN and NAIS both utilize co-occurrence context, CMN only utilizes user co-occurrence context whereas NAIS looks into URL co-occurrence context.

### Relevance

Label: 

## Record 0426

Paper: Forget Me Not: Reducing Catastrophic Forgetting for Domain Adaptation in Reading Comprehension

### Question

> What is the training objective in the method introduced in this paper?

### Passage

> We first pre-train a general domain RC model on squad, our source domain. Given the pre-trained model, we then perform fine-tuning (finetune) on the msmarco and bioasq data sets: 7 target domains in total. By fine-tuning we mean taking the pre-trained model parameters as initial parameters and update them accordingly based on data from the new domain. To reduce forgetting on the source domain (squad), we experiment with incorporating auxiliary penalty terms (e.g. L2 between new and old parameters) to the standard cross entropy loss to regularise the fine-tuning process.
> 
> We explore 3 modern RC models in our experiments: QANet BIBREF10; decaNLP BIBREF11; and BERT BIBREF12. QANet is a Transformer-based BIBREF26 comprehension model, where the encoder consists of stacked convolution and self-attention layers. The objective of the model is to predict the position of the starting and ending indices of the answer words in the context. decaNLP is a recurrent network-based comprehension model trained on ten NLP tasks simultaneously, all casted as a question-answer problem. Much of decaNLP's flexibility is due to its pointer-generator network, which allows it to generate words by extracting them from the question or context passages, or by drawing them from a vocabulary. BERT is a deep bi-directional encoder model based on Transformers. It is pre-trained on a large corpus in an unsupervised fashion using a masked language model and next-sentence prediction objective. To apply BERT to a specific task, the standard practice is to add additional output layers on top of the pre-trained BERT and fine-tune the whole model for the task. In our case for RC, 2 output layers are added: one for predicting the start index and another the end index. BIBREF12 demonstrates that this transfer learning strategy produces state-of-the-art performance on a range of NLP tasks. For RC specifically, BERT (BERT-Large) achieved an F1 score of 93.2 on squad, outperforming human performance by 2 points.
> 
> Note that BERT and QANet RC models are extractive models (goal is to predict 2 indices), while decaNLP is a generative model (goal is to generate the correct word sequence). Also, unlike QANet and decaNLP, BERT is not designed specifically for RC. It represents a growing trend in the literature where large

### Relevance

Label: 

## Record 0427

Paper: Forget Me Not: Reducing Catastrophic Forgetting for Domain Adaptation in Reading Comprehension

### Question

> What is the training objective in the method introduced in this paper?

### Passage

> Reading comprehension (RC) is the task of answering a question given a context passage. Related to Question-Answering (QA), RC is seen as a module in the full QA pipeline, where it assumes a related context passage has been extracted and the goal is to produce an answer based on the context. In recent years, the creation of large-scale open domain comprehension data sets BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, BIBREF5 has spurred the development of a host of end-to-end neural comprehension systems with promising results.
> 
> In spite of these successes, it is difficult to train these modern comprehension systems on narrow domain data (e.g. biomedical), as these models often have a large number of parameters. A better approach is to transfer knowledge via fine-tuning, i.e. by first pre-training the model using data from a large source domain and continue training it with examples from the small target domain. It is an effective strategy, although a fine-tuned model often performs poorly when it is re-applied to the source domain, a phenomenon known as catastrophic forgetting BIBREF6, BIBREF7, BIBREF8, BIBREF9. This is generally not an issue if the goal is to optimise purely for the target domain, but in real-word applications where model robustness is an important quality, over-optimising for a development set often leads to unexpected poor performance when applied to test cases in the wild.
> 
> In this paper, we explore strategies to reduce forgetting for comprehension systems during domain adaption. Our goal is to preserve the source domain's performance as much as possible, while keeping target domain's performance optimal and assuming no access to the source data. We experiment with a number of auxiliary penalty terms to regularise the fine-tuning process for three modern RC models: QANet BIBREF10, decaNLP BIBREF11 and BERT BIBREF12. We observe that combining different auxiliary penalty terms results in the best performance, outperforming benchmark methods that require source data.
> 
> Technically speaking, the methods we propose are not limited to domain transfer for reading comprehension. We also show that the methodology can be used for transferring to entirely different tasks. With that said, we focus on comprehension here because it is a practical problem in real world applications, where the target domain often

### Relevance

Label: 

## Record 0428

Paper: Forget Me Not: Reducing Catastrophic Forgetting for Domain Adaptation in Reading Comprehension

### Question

> What is the training objective in the method introduced in this paper?

### Passage

> Observing that the model tends to focus on optimising for the target domain/task in early iterations (as the penalty term has a very small value), we explore using a dynamic $\lambda $ scale that starts at a larger value that decays over time. With just simple linear decay, we found substantial improvement in +ewc for recovering squad's performance, although the results are mixed for other penalties (particularly for +ewcn). We therefore only report results that are based on static $\lambda $ values in this paper. With that said, we contend that this might be an interesting avenue for further research, e.g. by exploring more complex decay functions.
> 
> To validate the assumption made by gem BIBREF20, we conduct gradient analysis for the auxiliary penalty terms. During fine-tuning, at each step $t$, we calculate the gradient cosine similarity $sim(g_t, g_t^{\prime })$, where $g_t=\frac{\partial \mathcal {L}(f_{\theta _t}, M)}{\partial \theta _t}$, $g_t^{\prime }=\frac{\partial \mathcal {L}(f_{\theta _t}, (x, y))}{\partial \theta _t}$, $M$ is a memory containing squad examples, and $x$/$y$ is training data/label from the current domain. We smooth the scores by averaging over every 1K steps, resulting in 20 cosine similarity values for 20K steps. Figure FIGREF26 plots the gradient cosine similarity for our models in ms -fn.
> 
> Curiously, our best performing model +all produces the lowest cosine similarity at most steps (the only exception is between 0-1K steps). finetune, on the other hand, maintains relatively high similarity throughout. Similar trends are found for other domains. These observations imply that the inspiration gem draw on — i.e. catastrophic forgetting can be reduced by constraining a positive dot product between $g_t$ and $g_t^{\prime }$ — is perhaps not as empirically effective as intuition might tell us, and that our auxiliary penalty methods represent an alternative (and very different) direction to preserving source performance.

### Relevance

Label: 

## Record 0429

Paper: Forget Me Not: Reducing Catastrophic Forgetting for Domain Adaptation in Reading Comprehension

### Question

> What is the training objective in the method introduced in this paper?

### Passage

> In previous experiments, we fine-tune a pre-trained model to each domain independently. With continuous learning, we seek to investigate the performance of finetune and its four variants (+l2, +cd, +ewcn and +all) when they are applied to a series of fine-tuning on multiple domains. For the remainder of experiments in the paper, we test only with decaNLP.
> 
> When computing the penalties, we consider the last trained model as the source model. Figure FIGREF11 demonstrates the performance of the models on the development set of squad and test sets of ms -bm and ms -cp when they are adapted to ms -bm, ms -cp, ms -fn, ms -ms, ms -fm and ms -lw in sequence. We exclude plots for the latter domains as they are similar to that of ms -cp.
> 
> Including the pre-training on squad, all models are trained for a total of 170K iterations: squad from 0–44K, ms -bm from 45K–65K, ms -cp from 66K–86K, ms -fn from 87K–107K, ms -ms from 108K–128K, ms -fm from 129K–149K and ms -lw from 150K–170K.
> 
> We first look at the recovery for squad in Figure FIGREF11. +all (black line; legend in Figure FIGREF11) trails well above all other models after a series of fine-tuning, followed by +ewcn and +cd, while finetune produces the most forgetting. At the end of the continuous learning, +all recovers more than 5 F1 points compared to finetune. We see a similar trend for ms -bm (Figure FIGREF11), although the difference is less pronounced. The largest gap between finetune and +all occurs when we fine-tune for ms -fm (iteration 129K–149K). Note that we are not trading off target performance when we first tune for ms -bm (iteration 45K–65K), where finetune and +all produces comparable F1.
> 
> For ms -cp (Figure FIGREF11), we first notice that there is considerably less forgetting overall (ms -cp performance ranges from 65–75 F1, while squad performance in Figure FIGREF11 ranges from 45–75 F1). This is perhaps unsurprising, as the model is already generally well-tuned (e.g. it takes less iterations to reach optimal performance for ms -cp compared to ms -bm and squad). Most models perform similarly here. +all produces stronger recovery when fine-tuning on ms -fm (129K–149K) and ms

### Relevance

Label: 

## Record 0430

Paper: Forget Me Not: Reducing Catastrophic Forgetting for Domain Adaptation in Reading Comprehension

### Question

> What is the training objective in the method introduced in this paper?

### Passage

> We first pre-train QANet and decaNLP on squad, tuning their hyper-parameters based on its development partition. For BERT, we fine-tune the released pre-trained model on squad by adding 2 additional output layers to predict the start/end indices (we made no changes to the hyper-parameters). We initialise word vectors of QANet and decaNLP with pre-trained GloVe embeddings BIBREF27 and keep them fixed during training. We also freeze the input embeddings for BERT. To measure performance, we use the standard macro-averaged F1 as the evaluation metric, which measures the average overlap of word tokens between prediction and ground truth answer. Our pre-trained QANet, decaNLP and BERT achieve an F1 score of 80.47, 75.50 and 87.62 respectively on the development partition of squad. Note that the test partition of squad is not released publicly, and so all reported squad performance in the paper is on the development set.
> 
> Given the pre-trained squad models, we fine-tune them on the msmarco and bioasq domains. We test vanilla fine-tuning (finetune) and 5 variants of fine-tuning with auxiliary penalty terms: (1) EWC (+ewc); normalised EWC (+ewcn); cosine distance (+cd); L2 (+l2); and combined normalised EWC, cosine distance and L2 (+all). As a benchmark, we also perform fine-tuning with gradient episodic memory (gem), noting that this approach uses the first $m$ examples from squad ($m = 256$ in our experiments).
> 
> To find the best hyper-parameter configuration, we tune it based on the development partition for each target domain. For a given domain, finetune and its variants (+ewc, +ewcn, +cd, +l2 and +all) all share the same hyper-parameter configuration. Detailed hyper-parameter settings are given in the supplementary material.
> 
> As a baseline, we train QANet, decaNLP and BERT from scratch (scratch) using the target domain data. As before, we tune their hyper-parameters based on development performance. We present the full results in Table TABREF10.
> 
> For each target domain, we display two F1 scores: the source squad development performance (“squad”); and the target domain's test performance (“Test”). We first compare the performance between scratch and finetune. Across all domains for QANet, decaNLP and BERT, finetune substantially improves the target domain's performance compared to scratch. The largest improvement is seen in bioasq for QANet, where its F1

### Relevance

Label: 

## Record 0431

Paper: Reducing Gender Bias in Neural Machine Translation as a Domain Adaptation Problem

### Question

> What three languages are used in the translation experiments?

### Passage

> WinoMT provides an evaluation framework for translation from English to eight diverse languages. We select three pairs for experiments: English to German (en-de), English to Spanish (en-es) and English to Hebrew (en-he). Our selection covers three language groups with varying linguistic properties: Germanic, Romance and Semitic. Training data available for each language pair also varies in quantity and quality. We filter training data based on parallel sentence lengths and length ratios.
> 
> For en-de, we use 17.6M sentence pairs from WMT19 news task datasets BIBREF30. We validate on newstest17 and test on newstest18.
> 
> For en-es we use 10M sentence pairs from the United Nations Parallel Corpus BIBREF31. While still a large set, the UNCorpus exhibits far less diversity than the en-de training data. We validate on newstest12 and test on newstest13.
> 
> For en-he we use 185K sentence pairs from the multilingual TED talks corpus BIBREF32. This is both a specialized domain and a much smaller training set. We validate on the IWSLT 2012 test set and test on IWSLT 2014.
> 
> Table TABREF29 summarises the sizes of datasets used, including their proportion of gendered sentences and ratio of sentences in the English source data containing male and female stopwords. A gendered sentence contains at least one English gendered stopword as used by BIBREF5.
> 
> Interestingly all three datasets have about the same proportion of gendered sentences: 11-12% of the overall set. While en-es appears to have a much more balanced gender ratio than the other pairs, examining the data shows this stems largely from sections of the UNCorpus containing phrases like `empower women' and `violence against women', rather than gender-balanced professional entities.
> 
> For en-de and en-es we learn joint 32K BPE vocabularies on the training data BIBREF33. For en-he we use separate source and target vocabularies. The Hebrew vocabulary is a 2k-merge BPE vocabulary, following the recommendations of BIBREF34 for smaller vocabularies when translating into lower-resource languages. For the en-he source vocabulary we experimented both with learning a new 32K vocabulary and with reusing the joint BPE vocabulary trained on the largest set – en-de – which lets us initialize the en-he system with the pre-trained en-de model. The latter resulted in higher BLEU and faster training.

### Relevance

Label: 

## Record 0432

Paper: Reducing Gender Bias in Neural Machine Translation as a Domain Adaptation Problem

### Question

> What three languages are used in the translation experiments?

### Passage

> Finally, in Table TABREF41, we apply the gender inflection transducer to the commercial system translations listed in Table TABREF36. We find rescoring these lattices with our strongest debiasing model (line 5 of Table TABREF40) substantially improves WinoMT accuracy for all systems and language pairs.
> 
> One interesting observation is that WinoMT accuracy after rescoring tends to fall in a fairly narrow range for each language relative to the performance range of the baseline systems. For example, a 25.5% range in baseline en-de accuracy becomes a 3.6% range after rescoring. This suggests that our rescoring approach is not limited as much by the bias level of the baseline system as by the gender-inflection transducer and the models used in rescoring. Indeed, we emphasise that the large improvements reported in Table TABREF41 do not require any knowledge of the commercial systems or the data they were trained on; we use only the translation hypotheses they produce and our own rescoring model and transducer.

### Relevance

Label: 

## Record 0433

Paper: Reducing Gender Bias in Neural Machine Translation as a Domain Adaptation Problem

### Question

> What three languages are used in the translation experiments?

### Passage

> Table TABREF37 compares our baseline model with the results of unregularised fine-tuning on the counterfactual sets described in Section SECREF10.
> 
> Fine-tuning for one epoch on original, a subset of the original data with gendered English stopwords, gives slight improvement in WinoMT accuracy and $\Delta G$ for all language pairs, while $\Delta S$ worsens. We suggest this set consolidates examples present in the full dataset, improving performance on gendered entities generally but emphasizing stereotypical roles.
> 
> On the FTrans original set $\Delta G$ increases sharply relative to the original set, while $\Delta S$ decreases. We suspect this set suffers from bias amplification BIBREF3 introduced by the baseline system during forward-translation. The model therefore over-predicts male entities even more heavily than we would expect given the gender makeup of the adaptation data's source side. Over-predicting male entities lowers $\Delta S$ artificially.
> 
> Adapting to FTrans swapped increases accuracy and decreases both $\Delta G$ and $\Delta S$ relative to the baseline for en-de and en-es. This is the desired result, but not a particularly strong one, and it is not replicated for en-he. The balanced set has a very similar effect to the FTrans swapped set, with a smaller test BLEU difference from the baseline.
> 
> One consistent result from Table TABREF37 is the largest improvement in WinoMT accuracy corresponding to the model predicting male and female entities in the closest ratio. However, the best ratios for models adapted to these datasets are 2:1 or higher, and the accuracy improvement is small.
> 
> The purpose of EWC regularization is to avoid catastrophic forgetting of general translation ability. This does not occur in the counterfactual experiments, so we do not apply EWC. Moreover, WinoMT accuracy gains are small with standard fine-tuning, which allows maximum adaptation: we suspect EWC would prevent any improvements.
> 
> Overall, improvements from fine-tuning on counterfactual datasets (FTrans swapped and balanced) are present. However, they are not very different from the improvements when fine-tuning on equivalent non-counterfactual sets (original and FTrans original). Improvements are also inconsistent across language pairs.

### Relevance

Label: 

## Record 0434

Paper: Reducing Gender Bias in Neural Machine Translation as a Domain Adaptation Problem

### Question

> What three languages are used in the translation experiments?

### Passage

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

### Relevance

Label: 

## Record 0435

Paper: Reducing Gender Bias in Neural Machine Translation as a Domain Adaptation Problem

### Question

> What three languages are used in the translation experiments?

### Passage

> In lines 7-9 of Table TABREF40 we consider lattice-rescoring the baseline output, using three models debiased on the handcrafted data.
> 
> Line 7 rescores the general test set hypotheses (line 1) with a model adapted to handcrafted data that has no source language profession vocabulary overlap with the test set (line 3). This scheme shows no BLEU degradation from the baseline on any language and in fact a slight improvement on en-he. Accuracy improvements on WinoMT are only slightly lower than for decoding with the rescoring model directly, as in line 3.
> 
> In line 8, lattice rescoring with the non-converged model adapted to handcrafted data (line 4) likewise leaves general BLEU unchanged or slightly improved. When lattice rescoring the WinoMT challenge set, 79%, 76% and 49% of the accuracy improvement is maintained on en-de, en-es and en-he respectively. This corresponds to accuracy gains of up to 30% relative to the baselines with no general translation performance loss.
> 
> In line 9, lattice-rescoring with the converged model of line 5 limits BLEU degradation to 0.2 BLEU on all languages, while maintaining 85%, 82% and 58% of the WinoMT accuracy improvement from the converged model for the three language pairs. Lattice rescoring with this model gives accuracy improvements over the baseline of 36%, 38% and 24% for en-de, en-es and en-he.
> 
> Rescoring en-he maintains a much smaller proportion of WinoMT accuracy improvement than en-de and en-es. We believe this is because the en-he baseline is particularly weak, due to a small and non-diverse training set. The baseline must produce some inflection of the correct entity before lattice rescoring can have an effect on gender bias.

### Relevance

Label: 

## Record 0436

Paper: Gender Representation in French Broadcast Corpora and Its Impact on ASR Performance

### Question

> How big is imbalance in analyzed corpora?

### Passage

> This section is organized as follows: we first present the data we are working on. In a second time we explain how we proceed to describe the gender representation in our corpus and introduce the notion of speaker's role. The third subsection introduces the ASR system and metrics used to evaluate gender bias in performance.

### Relevance

Label: 

## Record 0437

Paper: Gender Representation in French Broadcast Corpora and Its Impact on ASR Performance

### Question

> How big is imbalance in analyzed corpora?

### Passage

> This paper has investigated gender bias in ASR performance through the following research questions: i) what is the proportion of men and women in French radio and TV media data ? ii) what is the impact of the observed disparity on ASR performance ? iii) is this as simple as a problem of gender proportion in the training data or are other factors entangled ? Our contributions are the following:
> 
> Descriptive analysis of the broadcast data used to train our ASR system confirms the already known disparity, where 65% of the speakers are men, speaking more than 75% of the time.
> 
> When investigating WER scores according to gender, speaker's role and speech type, huge variations are observed. We conclude that gender is clearly a factor of variation in ASR performance, with a WER increase of 24% for women compared to men, exhibiting a clear gender bias.
> 
> Gender bias varies across speaker's role and speech spontaneity level. Performance for Punctual speakers respectively spontaneous speech seems to reinforce this gender bias with a WER increase of 27.2% respectively 31.8% between male and female speakers.
> 
> We found that an ASR system trained on unbalanced data regarding gender produces gender bias performance. Therefore, in order to create fair systems it is necessary to take into account the representation problems in society that are going to be encapsulated in the data. Understanding how women under-representation in broadcast data can lead to bias in ASR performances is the key to prevent re-implementing and reinforcing discrimination already existing in our societies. This is in line with the concept of “Fairness by Design" proposed by BIBREF31.
> 
> Gender, race, religion, nationality are all characteristics that we deem unfair to classify on, and these ethical standpoints needs to be taken into account in systems' design. Characteristics that are not considered as relevant in a given task can be encapsulated in data nonetheless, and lead to bias performance. Being aware of the demographic skews our data set might contain is a first step to track the life cycle of a training data set and a necessary step to control the tools we develop.

### Relevance

Label: 

## Record 0438

Paper: Gender Representation in French Broadcast Corpora and Its Impact on ASR Performance

### Question

> How big is imbalance in analyzed corpora?

### Passage

> The ever growing use of machine learning in science has been enabled by several progresses among which the exponential growth of data available. The quality of a system now depends mostly on the quality and quantity of the data it has been trained on. If it does not discard the importance of an appropriate architecture, it reaffirms the fact that rich and large corpora are a valuable resource. Corpora are research contributions which do not only allow to save and observe certain phenomena or validate a hypothesis or model, but are also a mandatory part of the technology development. This trend is notably observable within the NLP field, where industrial technologies, such as Apple, Amazon or Google vocal assistants now reach high performance level partly due to the amount of data possessed by these companies BIBREF9.
> 
> Surprisingly, as data is said to be “the new oil", few data sets are available for ASR systems. The best known are corpora like TIMIT BIBREF10, Switchboard BIBREF11 or Fisher BIBREF12 which date back to the early 1990s. The scarceness of available corpora is justified by the fact that gathering and annotating audio data is costly both in terms of money and time. Telephone conversations and broadcast recordings have been the primary source of spontaneous speech used. Out of all the 130 audio resources proposed by LDC to train automatic speech recognition systems in English, approximately 14% of them are based on broadcast news and conversation. For French speech technologies, four corpora containing radio and TV broadcast are the most widely used: ESTER1 BIBREF13, ESTER2 BIBREF14, ETAPE BIBREF15 and REPERE BIBREF16. These four corpora have been built alongside evaluation campaigns and are still, to our knowledge, the largest French ones of their type available to date.

### Relevance

Label: 

## Record 0439

Paper: Gender Representation in French Broadcast Corpora and Its Impact on ASR Performance

### Question

> How big is imbalance in analyzed corpora?

### Passage

> The ASR system used in this work is described in BIBREF25. It uses the KALDI toolkit BIBREF26, following a standard Kaldi recipe. The acoustic model is based on a hybrid HMM-DNN architecture and trained on the data summarized in Table . Acoustic training data correspond to 100h of non-spontaneous speech type (mostly broadcast news) coming from both radio and TV shows. A 5-gram language model is trained from several French corpora (3,323M words in total) using SRILM toolkit BIBREF27. The pronunciation model is developed using the lexical resource BDLEX BIBREF28 as well as automatic grapheme-to-phoneme (G2P) transcription to find pronunciation variants of our vocabulary (limited to 80K). It is important to re-specify here, for further analysis, that our Kaldi pipeline follows speaker adaptive training (SAT) where we train and decode using speaker adapted features (fMLLR-adapted features) in per-speaker mode. It is well known that speaker adaptation acts as an effective procedure to reduce mismatch between training and evaluation conditions BIBREF29, BIBREF26.

### Relevance

Label: 

## Record 0440

Paper: Gender Representation in French Broadcast Corpora and Its Impact on ASR Performance

### Question

> How big is imbalance in analyzed corpora?

### Passage

> Our data consists of two sets used to train and evaluate our automatic speech recognition system. Four major evaluation campaigns have enabled the creation of wide corpora of French broadcast speech: ESTER1 BIBREF13, ESTER2 BIBREF14, ETAPE BIBREF15 and REPERE BIBREF16. These four collections contain radio and/or TV broadcasts aired between 1998 and 2013 which are used by most academic researchers in ASR. Show duration varies between 10min and an hour. As years went by and speech processing research was progressing, the difficulty of the tasks augmented and the content of these evaluation corpora changed. ESTER1 and ESTER2 mainly contain prepared speech such as broadcast news, whereas ETAPE and REPERE consists also of debates and entertainment shows, spontaneous speech introducing more difficulty in its recognition.
> 
> Our training set contains 27,085 speech utterances produced by 2,506 speakers, accounting for approximately 100 hours of speech. Our evaluation set contains 74,064 speech utterances produced by 1,268 speakers for a total of 70 hours of speech. Training data by show, medium and speech type is summarized in Table and evaluation data in Table . Evaluation data has a higher variety of shows with both prepared (P) and spontaneous (S) speech type (accented speech from African radio broadcast is also included in the evaluation set).

### Relevance

Label: 

## Record 0441

Paper: Automated News Suggestions for Populating Wikipedia Entity Pages

### Question

> What baseline model is used?

### Passage

> Here we show the evaluation setup for ASP task and discuss the results with a focus on three main aspects, (i) the overall performance across the years, (ii) the entity class specific performance, and (iii) the impact on entity profile expansion by suggesting missing sections to entities based on the pre-computed templates.
> 
> Baselines. To the best of our knowledge, we are not aware of any comparable approach for this task. Therefore, the baselines we consider are the following:
> 
> S1: Pick the section from template INLINEFORM0 with the highest lexical similarity to INLINEFORM1 : S1 INLINEFORM2
> 
> S2: Place the news into the most frequent section in INLINEFORM0
> 
> Learning Models. We use Random Forests (RF) BIBREF23 and Support Vector Machines (SVM) BIBREF24 . The models are optimized taking into account the features in Table TABREF31 . In contrast to the AEP task, here the scale of the number of instances allows us to learn the SVM models. The SVM model is optimized using the INLINEFORM0 loss function and uses the Gaussian kernels.
> 
> Metrics. We compute precision P as the ratio of news for which we pick a section INLINEFORM0 from INLINEFORM1 and INLINEFORM2 conforms to the one in our ground-truth (see Section SECREF40 ). The definition of recall R and F1 score follows from that of precision.
> 
> Figure FIGREF66 shows the overall performance and a comparison of our approach (when INLINEFORM0 is optimized using SVM) against the best performing baseline S2. With the increase in the number of training instances for the ASP task the performance is a monotonically non-decreasing function. For the year 2009, we optimize the learning objective of INLINEFORM1 with around 8% of the total instances, and evaluate on the rest. The performance on average is around P=0.66 across all classes. Even though for many classes the performance is already stable (as we will see in the next section), for some classes we improve further. If we take into account the years between 2010 and 2012, we have an increase of INLINEFORM2 P=0.17, with around 70% of instances used for training and the remainder for evaluation. For the remaining years the total improvement is INLINEFORM3 P=0.18 in contrast to the performance at year 2009.

### Relevance

Label: 

## Record 0442

Paper: Automated News Suggestions for Populating Wikipedia Entity Pages

### Question

> What baseline model is used?

### Passage

> In this section we outline the evaluation plan to verify the effectiveness of our learning approaches. To evaluate the news suggestion problem we are faced with two challenges.
> 
> What comprises the ground truth for such a task ?
> 
> How do we construct training and test splits given that entity pages consists of text added at different points in time ?
> 
> Consider the ground truth challenge. Evaluating if an arbitrary news article should be included in Wikipedia is both subjective and difficult for a human if she is not an expert. An invasive approach, which was proposed by Barzilay and Sauper BIBREF8 , adds content directly to Wikipedia and expects the editors or other users to redact irrelevant content over a period of time. The limitations of such an evaluation technique is that content added to long-tail entities might not be evaluated by informed users or editors in the experiment time frame. It is hard to estimate how much time the added content should be left on the entity page. A more non-invasive approach could involve crowdsourcing of entity and news article pairs in an IR style relevance assessment setup. The problem of such an approach is again finding knowledgeable users or experts for long-tail entities. Thus the notion of relevance of a news recommendation is challenging to evaluate in a crowd setup.
> 
> We take a slightly different approach by making an assumption that the news articles already present in Wikipedia entity pages are relevant. To this extent, we extract a dataset comprising of all news articles referenced in entity pages (details in Section SECREF40 ). At the expense of not evaluating the space comprising of news articles absent in Wikipedia, we succeed in (i) avoiding restrictive assumptions about the quality of human judgments, (ii) being invasive and polluting Wikipedia, and (iii) deriving a reusable test bed for quicker experimentation.
> 
> The second challenge of construction of training and test set separation is slightly easier and is addressed in Section SECREF46 .

### Relevance

Label: 

## Record 0443

Paper: Automated News Suggestions for Populating Wikipedia Entity Pages

### Question

> What baseline model is used?

### Passage

> case, we consider the comparative relevance of the news article to the different entities occurring in it. As an example, let us consider the meeting of the Sudanese bishop Elias Taban with Hillary Clinton. Both entities are salient for the meeting. However, in Taban's Wikipedia page, this meeting is discussed prominently with a corresponding news reference, whereas in Hillary Clinton's Wikipedia page it is not reported at all. We believe this is not just an omission in Clinton's page but mirrors the fact that for the lesser known Taban the meeting is big news whereas for the more famous Clinton these kind of meetings are a regular occurrence, not all of which can be reported in what is supposed to be a selection of the most important events for her. Therefore, if two entities co-occur, the news is more relevant for the entity with the lower a priori authority.
> 
> The a priori authority of an entity (denoted by INLINEFORM0 ) can be measured in several ways. We opt for two approaches: (i) probability of entity INLINEFORM1 occurring in the corpus INLINEFORM2 , and (ii) authority assessed through centrality measures like PageRank BIBREF16 . For the second case we construct the graph INLINEFORM3 consisting of entities in INLINEFORM4 and news articles in INLINEFORM5 as vertices. The edges are established between INLINEFORM6 and entities in INLINEFORM7 , that is INLINEFORM8 , and the out-links from INLINEFORM9 , that is INLINEFORM10 (arrows present the edge direction).
> 
> Starting from a priori authority, we proceed to relative authority by comparing the a priori authority of co-occurring entities in INLINEFORM0 . We define the relative authority of INLINEFORM1 as the proportion of co-occurring entities INLINEFORM2 that have a higher a priori authority than INLINEFORM3 (see Equation EQREF28 . DISPLAYFORM0
> 
> As we might run the danger of not suggesting any news articles for entities with very high a priori authority (such as Clinton) due to the strict inequality constraint, we can relax the constraint such that the authority of co-occurring entities is above a certain threshold.
> 
> News Domain Authority. The news domain authority addresses two main aspects. Firstly, if bundled together with the relative authority feature, we can ensure that dependent on

### Relevance

Label: 

## Record 0444

Paper: Automated News Suggestions for Populating Wikipedia Entity Pages

### Question

> What baseline model is used?

### Passage

> and 2012, we have an increase of INLINEFORM2 P=0.17, with around 70% of instances used for training and the remainder for evaluation. For the remaining years the total improvement is INLINEFORM3 P=0.18 in contrast to the performance at year 2009.
> 
> On the other hand, the baseline S1 has an average precision of P=0.12. The performance across the years varies slightly, with the year 2011 having the highest average precision of P=0.13. Always picking the most frequent section as in S2, as shown in Figure FIGREF66 , results in an average precision of P=0.17, with a uniform distribution across the years.
> 
> Here we show the performance of INLINEFORM0 decomposed for the different entity classes. Specifically we analyze the 27 classes in Figure FIGREF42 . In Table TABREF68 , we show the results for a range of years (we omit showing all years due to space constraints). For illustration purposes only, we group them into four main classes ( INLINEFORM1 Person, Organization, Location, Event INLINEFORM2 ) and into the specific sub-classes shown in the second column in Table TABREF68 . For instance, the entity classes OfficeHolder and Politician are aggregated into Person–Politics.
> 
> It is evident that in the first year the performance is lower in contrast to the later years. This is due to the fact that as we proceed, we can better generalize and accurately determine the correct fit of an article INLINEFORM0 into one of the sections from the pre-computed templates INLINEFORM1 . The results are already stable for the year range INLINEFORM2 . For a few Person sub-classes, e.g. Politics, Entertainment, we achieve an F1 score above 0.9. These additionally represent classes with a sufficient number of training instances for the years INLINEFORM3 . The lowest F1 score is for the Criminal and Television classes. However, this is directly correlated with the insufficient number of instances.
> 
> The baseline approaches for the ASP task perform poorly. S1, based on lexical similarity, has a varying performance for different entity classes. The best performance is achieved for the class Person – Politics, with P=0.43. This highlights the importance of our feature choice and that the ASP cannot be considered as a linear function, where the maximum similarity

### Relevance

Label: 

## Record 0445

Paper: Automated News Suggestions for Populating Wikipedia Entity Pages

### Question

> What baseline model is used?

### Passage

> between the language models INLINEFORM5 and the entity overlap in INLINEFORM6 and INLINEFORM7 .
> 
> Here we introduce the evaluation setup and analyze the results for the article–entity (AEP) placement task. We only report the evaluation metrics for the `relevant' news-entity pairs. A detailed explanation on why we focus on the `relevant' pairs is provided in Section SECREF16 .
> 
> Baselines. We consider the following baselines for this task.
> 
> B1. The first baseline uses only the salience-based features by Dunietz and Gillick BIBREF11 .
> 
> B2. The second baseline assigns the value relevant to a pair INLINEFORM0 , if and only if INLINEFORM1 appears in the title of INLINEFORM2 .
> 
> Learning Models. We use Random Forests (RF) BIBREF23 . We learn the RF on all computed features in Table TABREF21 . The optimization on RF is done by splitting the feature space into multiple trees that are considered as ensemble classifiers. Consequently, for each classifier it computes the margin function as a measure of the average count of predicting the correct class in contrast to any other class. The higher the margin score the more robust the model.
> 
> Metrics. We compute precision P, recall R and F1 score for the relevant class. For example, precision is the number of news-entity pairs we correctly labeled as relevant compared to our ground truth divided by the number of all news-entity pairs we labeled as relevant.
> 
> The following results measure the effectiveness of our approach in three main aspects: (i) overall performance of INLINEFORM0 and comparison to baselines, (ii) robustness across the years, and (iii) optimal model for the AEP placement task.
> 
> Performance. Figure FIGREF55 shows the results for the years 2009 and 2013, where we optimized the learning objective with instances from year INLINEFORM0 and evaluate on the years INLINEFORM1 (see Section SECREF46 ). The results show the precision–recall curve. The red curve shows baseline B1 BIBREF11 , and the blue one shows the performance of INLINEFORM2 . The curve shows for varying confidence scores (high to low) the precision on labeling the pair INLINEFORM3 as `relevant'. In addition, at each confidence score we can compute the corresponding recall for the `relevant' label. For high confidence scores on labeling the

### Relevance

Label: 

## Record 0446

Paper: Time to Take Emoji Seriously: They Vastly Improve Casual Conversational Models

### Question

> What corpus did they use?

### Passage

> The prevalent use of emoji—and their text-based precursors—is mostly unaddressed in current natural language processing (NLP) tasks. The support of the Unicode Standard BIBREF0 for emoji characters in 2010 ushered in a wide-spread, international adoption of these graphical elements in casual contexts. Interpreting the meaning of these characters has been challenging however, since they take on multiple semantic roles BIBREF1.
> 
> Whether or not emoji are used depends on the context of a text or conversation, with more formal settings generally being less tolerating. So is the popular aligned corpus Europarl BIBREF2 naturally devoid of emoji. Technical limitations, like no Unicode support, also limit its use. This in turn affects commonly used corpora, tokenizers, and pre-trained networks.
> 
> Take for example the Ubuntu Dialog Corpus by BIBREF3, a commonly used corpus for multi-turn systems. This dataset was collected from an Internet Relay Chat (IRC) room casually discussing the operating system Ubuntu. IRC nodes usually support the ASCII text encoding, so there's no support for graphical emoji. However, in the 7,189,051 utterances, there are only 9946 happy emoticons (i.e. :-) and the cruelly denosed :) version) and 2125 sad emoticons.
> 
> Word embeddings are also handling emoji poorly: Word2vec BIBREF4 with the commonly used pre-trained Google News vectors doesn't support the graphical emoji at all and vectors for textual emoticons are inconsistent. As another example with contextualized word embeddings, there are also no emoji or textual emoticons in the vocabulary list of BERT BIBREF5 by default and support for emoji is only recently added to the tokenizer. The same is true for GPT-2 BIBREF6. As all downstream systems, ranging from multilingual résumé parsing to fallacy detection BIBREF7, rely on the completeness of these embeddings, this lack of emoji support can affect the performance of some of these systems.
> 
> Another challenge is that emoji usage isn't static. Think of shifting conventions, different cultures, and newly added emoji to the Unicode list. Several applications also use their own custom emoji, like chat application Slack and streaming service Twitch. This becomes an issue for methods that leverage the Unicode description BIBREF8 or that rely on manual annotations BIBREF9.
> 
> Our contribution with this paper is two-fold: firstly, we argue that the current use—or

### Relevance

Label: 

## Record 0447

Paper: Time to Take Emoji Seriously: They Vastly Improve Casual Conversational Models

### Question

> What corpus did they use?

### Passage

> Inspired by the work on word representations, BIBREF8 presented Emoji2vec. This system generates a vector representation that's even compatible with the Word2vec representations, so they can be used together. This compatibility makes it easy to quickly incorporate Emoji2vec in existing systems that use Word2vec.
> 
> The main drawback is that the emoji representations are trained on the Unicode descriptions. As a consequence, the representations only capture a limited meaning and do not account for shifting or incorrect use of emoji in the real world. For example, a peach emoji could be considered a double entendre, due to the resemblance to a woman's posterior. This is of course mentioned nowhere in the Unicode description. Which shows that the meaning of an emoji is how users interpret it, so also accidental incorrect use can cause issues BIBREF10.
> 
> In spirit, BIBREF11 is similar to our work. Their system, DeepMoji, illustrates the importance of emoji for sentiment, emotion, and sarcasm classification. For these tasks, they used a dataset of 1246 million tweets containing at least one emoji. However, the authors use the emoji in those tweets not for the DeepMoji model input, but as an target label. With a slightly better agreement score than humans on the sentiment task, this supports our hypothesis that emoji carry the overall meaning of an utterance.
> 
> BIBREF12 focus on a predicting one emoji based on the textual content. Interestingly, they looked into both English and Spanish tweets and compared a range of systems for a shared task at SemEval 2018: Multilingual Emoji Prediction. This shared task shows that emoji are getting more attention, but how their task is set up also highlights the current lack of high quality datasets with emoji.
> 
> The same shared task was tackled by BIBREF13 and a year later by BIBREF14, which made use of a pre-processor and tokenizer from BIBREF15. This tokenizer replaces some emoji and emoticons by tokens related to their meaning. So is \o/ replaced with <happy>. Naturally, this approach suffers from the same issues as described before. And even though it's really useful to have some basic, out-of-the-box support for emoticons thanks to this work, we think that this strategy is too reducing to capture subtle

### Relevance

Label: 

## Record 0448

Paper: Time to Take Emoji Seriously: They Vastly Improve Casual Conversational Models

### Question

> What corpus did they use?

### Passage

> Emoji are commonly used in casual settings, like on social media or in casual conversations. In conversations—as opposed to relatively context-free social media posts—an emoji alone can be an utterance by itself. And with a direct impact for some applications, like customer support, we focus on conversational datasets. We hope the conversational community has the most direct benefit from these emoji-enabled models. Of course, the conclusions we'll draw don't have to be limited to this field.
> 
> Table TABREF1 gives an overview of frequently used and interesting conversational datasets. The lacuna of emoji-rich reference datasets was already mentioned in Section SECREF1 and is in our opinion one of the factors that emoji remain fairly underutilized.
> 
> For our models, we'll use a customer support dataset with a relatively high usage of emoji. The dataset contains 2000 tuples collected by BIBREF24 that are sourced from Twitter. They provide conversations, which consist of at least one question and one free-form answer. Some conversations are longer, in this case we ignored the previous context and only looked at the last tuple. This dataset illustrates that even when contacting companies, Twitter users keep using emoji relatively often, 8.75% of all utterances.
> 
> The tweets were filtered on hyper links and personal identifiers, but Unicode emoji characters were preserved. As emoji are frequently used on Twitter, this resulted in a dataset with 170 of the 2000 tuples containing at least one emoji character.

### Relevance

Label: 

## Record 0449

Paper: Time to Take Emoji Seriously: They Vastly Improve Casual Conversational Models

### Question

> What corpus did they use?

### Passage

> Naturally, this approach suffers from the same issues as described before. And even though it's really useful to have some basic, out-of-the-box support for emoticons thanks to this work, we think that this strategy is too reducing to capture subtle nuances.
> 
> An analysis on the use of emoji on a global scale is done by BIBREF16. For this, the authors used geo-tagged tweets, which also allowed them to correlate the popularity of certain emoji with development indicators. This shows that the information encoded by emoji—and of course the accompanying tweet—is not limited to sentiment or emotion. Also BIBREF17 analyze the uses of emoji on social networks. Their approach consists of finding information networks between emoji and English words with LINE BIBREF18.
> 
> An interesting aspect of emoji usage is analyzed by BIBREF19. In this work, the correlation between the use of Fitzpatrick skin tone BIBREF20 modifiers and the perceived skin tone of the user. This research shows that users are inclined to use representing emoji for themselves. BIBREF19 reported that no negative sentiment was associated with specific skin tone modifiers.

### Relevance

Label: 

## Record 0450

Paper: Time to Take Emoji Seriously: They Vastly Improve Casual Conversational Models

### Question

> What corpus did they use?

### Passage

> We start from 12-headed multilingual BERT (bert-base-multilingual-cased), which has 110M parameters. For the model with emoji support, the number of tokens is increased, so new vectors are appended at the end of the embeddings matrix. We then continue training on the language modeling task. We use the default configuration as is also used by BIBREF5 where randomly selected tokens are replaced by:
> 
> a mask token: 80% chance,
> 
> another random word: 10% chance,
> 
> the original word: 10% chance.
> 
> This model is trained for 100 epochs with the Adam BIBREF35 optimizer. The learning rate is set to the commonly used $lr=5\cdot 10^{-5}$ and $\epsilon = 10^{-8}$. No hyper-parameter tuning was done, as the results are acceptable on their own and are sufficient to allow conclusions for this paper. The loss is cross entropy BIBREF36.
> 
> We then fine-tune both models, with and without emoji tokenization, on the sentence prediction task with a training set of 70%. We again use the Adam optimizer with the same settings and with binary cross entropy. In this case, the training was limited to 10 epochs. To mitigate the need for weighting and other class imbalance issues, we trained with pairs of positive and negative candidates. This is in contract to the evaluation, where 99 negative candidates are used. However, since each candidate is considered on its own merit during evaluation, this discrepancy won't affect the performance.
> 
> For the formulation of the fine-tuning task, we use the same approach as BIBREF5. The first input sentence is joined with the second sentence, separated by a special [SEP] token, as can be seen in Figure FIGREF5. The model, with a specialized head for next sentence prediction, then outputs a correlation score.

### Relevance

Label: 

## Record 0451

Paper: Enhancing PIO Element Detection in Medical Text Using Contextualized Embedding

### Question

> what boosting techniques were used?

### Passage

> They have pushed the state of the art of text representation and information retrieval. More specifically, these techniques enhanced NLP algorithms through the use of contextualized text embeddings at word, sentence, and paragraph levels BIBREF6 , BIBREF7 , BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 .
> 
> More recently, jin2018pico proposed a bidirectional long short term memory (LSTM) model to simultaneously extract PIO components from PubMed abstracts. To our knowledge, that study was the first in which a deep learning framework was used to extract PIO elements from PubMed abstracts.
> 
> In the present paper, we build a dataset of PIO elements by improving the methodology found in BIBREF12 . Furthermore, we built a multi-label PIO classifier, along with a boosting framework, based on the state of the art text embedding, BERT. This embedding model has been proven to offer a better contextualization compared to a bidirectional LSTM model BIBREF9 .

### Relevance

Label: 

## Record 0452

Paper: Enhancing PIO Element Detection in Medical Text Using Contextualized Embedding

### Question

> what boosting techniques were used?

### Passage

> In this paper, we presented an improved methodology to extract PIO elements, with reduced ambiguity, from abstracts of medical papers. The proposed technique was used to build a dataset of PIO elements that we call PICONET. We further proposed a model of PIO elements classification using state of the art BERT embedding. It has been shown that using the contextualized BioBERT embedding improved the accuracy of the classifier. This result reinforces the idea of the importance of embedding contextualization in subsequent classification tasks in this specific context.
> 
> In order to enhance the accuracy of the model, we investigated an ensemble method based on the LGBM algorithm. We trained the LGBM model, with the above models as base learners, to optimize the classification by learning a linear combination of the predicted probabilities, for the three classes, with the TF-IDF and QIEF scores. The results indicate that these text features were adequate for boosting the contextualized classification model. We compared the performance of the classifier when using the features with one of the base learners and the case where we combine the base learners along with the features. We obtained the best performance in the latter case.
> 
> The present work resulted in the creation of a PIO elements dataset, PICONET, and a classification tool. These constitute an important component of our system of automatic mining of medical abstracts. We intend to extend the dataset to full medical articles. The model will be modified to take into account the higher complexity of full text data and more efficient features for model boosting will be investigated.

### Relevance

Label: 

## Record 0453

Paper: Enhancing PIO Element Detection in Medical Text Using Contextualized Embedding

### Question

> what boosting techniques were used?

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

## Record 0454

Paper: Enhancing PIO Element Detection in Medical Text Using Contextualized Embedding

### Question

> what boosting techniques were used?

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

## Record 0455

Paper: Enhancing PIO Element Detection in Medical Text Using Contextualized Embedding

### Question

> what boosting techniques were used?

### Passage

> BERT (Bidirectional Encoder Representations from Transformers) is a deep bidirectional attention text embedding model. The idea behind this model is to pre-train a bidirectional representation by jointly conditioning on both left and right contexts in all layers using a transformer BIBREF13 , BIBREF9 . Like any other language model, BERT can be pre-trained on different contexts. A contextualized representation is generally optimized for downstream NLP tasks.
> 
> Since its release, BERT has been pre-trained on a multitude of corpora. In the following, we describe different BERT embedding versions used for our classification problem. The first version is based on the original BERT release BIBREF9 . This model is pre-trained on the BooksCorpus (800M words) BIBREF14 and English Wikipedia (2,500M words). For Wikipedia, text passages were extracted while lists were ignored. The second version is BioBERT BIBREF15 , which was trained on biomedical corpora: PubMed (4.5B words) and PMC (13.5B words).

### Relevance

Label: 

## Record 0456

Paper: A Resource for Studying Chatino Verbal Morphology

### Question

> What system is used as baseline?

### Passage

> Chatino is a group of languages spoken in Oaxaca, Mexico. Together with the Zapotec language group, the Chatino languages form the Zapotecan branch of the Otomanguean language family. There are three main Chatino languages: Zenzontepec Chatino (ZEN, ISO 639-2 code czn), Tataltepec Chatino (TAT, cta), and Eastern Chatino (ISO 639-2 ctp, cya, ctz, and cly) (E.Cruz 2011 and Campbell 2011). San Juan Quiahije Chatino (SJQ), the language of the focus of this study, belongs to Eastern Chatino, and is used by about 3000 speakers.

### Relevance

Label: 

## Record 0457

Paper: A Resource for Studying Chatino Verbal Morphology

### Question

> What system is used as baseline?

### Passage

> Morphological analysis is the task of creating a morphosyntactic description for a given word. It can be framed in a context-agnostic manner (as in our case) or within a given context, as for instance for the SIGMORPHON 2019 second shared task BIBREF11. We trained an encoder-decoder model that receives the form as character-level input, encodes it with a BiLSTM encoder, and then an attention enhanced decoder BIBREF14 outputs the corresponding sequence of morphological tags, implemented in DyNet. The baseline results are shown in Table . The exact-match accuracy of 67% is lower than the average accuracy that context-aware systems can achieve, and it highlights the challenge that the complexity of the tonal system of SJQ Chatino can pose.

### Relevance

Label: 

## Record 0458

Paper: A Resource for Studying Chatino Verbal Morphology

### Question

> What system is used as baseline?

### Passage

> Lemmatization is the task of retrieving the underlying lemma from which an inflected form was derived. Although in some languages the lemma is distinct from all forms, in SJQ Chatino the lemma is defined as the completive third-person singular form. As a computational task, lemmatization entails producing the lemma given an inflected form (and possibly, given a set of morphological tags describing the input form). Popular approaches tackle it as a character-level edit sequence generation task BIBREF15, or as a character-level sequence-to-sequence task BIBREF16. For our baseline lemmatization systems we follow the latter approach. We trained a character level encoder-decoder model, similar to the above-mentioned inflection system, implemented in DyNet.
> 
> The baseline results, with and without providing gold morphological tags along with the inflected form as input, are outlined in Table . We find that automatic lemmatization in SJQ Chatino achieves fairly high accuracy even with our simple baseline models (89% accuracy, $0.27$ average Levenshtein distance) and that providing the gold morphological tags provides a performance boost indicated by small improvements on both metrics. It it worth noting, though, that these results are also well below the $94--95\%$ average accuracy and $0.13$ average Levenshtein distance that lemmatization models achieved over 107 treebanks in 66 languages for the SIGMORPHON 2019 shared task BIBREF11.

### Relevance

Label: 

## Record 0459

Paper: A Resource for Studying Chatino Verbal Morphology

### Question

> What system is used as baseline?

### Passage

> Our work builds and expands upon previous work on Indigenous languages of the Americas specifically focusing on the complexity of their morphology. Among other works similar to ours, BIBREF17 focused on the morphology of Dene verbs, BIBREF18 on Arapaho verbs, BIBREF19 on Shipibo-Konibo, and BIBREF20 on Saint Lawrence Island and Central Siberian Yupik. BIBREF21 describe an approach for elicit complete inflection paradigms, with experiments in languages like Nahuatl. Our resource is the first one for SJQ Chatino, but it also provides an exciting new data point in the computational study of morphological analysis, lemmatization, and inflection, as it is the first one in a tonal language with explicit tonal markings in the writing system. In a similar vein, the Oto-Manguean Inflectional Class Database BIBREF22 provides a valuable resource for studying the verbal morphology of Oto-Manguean languages (including a couple of other Chatino variants: Yaitepec and Zenzotepec Chatino) but not in a format suitable for computational experiments.

### Relevance

Label: 

## Record 0460

Paper: A Resource for Studying Chatino Verbal Morphology

### Question

> What system is used as baseline?

### Passage

> Eastern Chatino languages , including SJQ Chatino, are intensively tonal BIBREF2, BIBREF3. Tones mark both lexical and grammatical distinctions in Eastern Chatino languages.
> 
> In SJQ Chatino, there are eleven tones. Three different systems for representing tone distinctions are employed in the literature: the S-H-M-L system of BIBREF2; the numeral system of BIBREF4; and the alphabetic system of BIBREF3. The correspondences among these three systems are given in Table . For present purposes, we will use numeral representations of the second sort. The number 1 represents a high pitch, 4 represents a low pitch, and double digits represent contour tones.

### Relevance

Label: 

## Record 0461

Paper: Selecting Artificially-Generated Sentences for Fine-Tuning Neural Machine Translation

### Question

> Which data-selection algorithms do they use?

### Passage

> The improvement of NMT models can be performed by fine-tuning BIBREF7, BIBREF8, i.e. train the models for additional epochs using a small set of in-domain data. Alternatively, BIBREF9 train models using smaller but more in-domain sentences in each epoch of the training process.
> 
> The use of the test set to retrieve relevant sentences for fine-tuning the model has been explored by BIBREF10, adapting a different model for each sentence in the test set, or BIBREF11, BIBREF12 where they adapt the model for the complete test set using transductive data-selection algorithms.

### Relevance

Label: 

## Record 0462

Paper: Selecting Artificially-Generated Sentences for Fine-Tuning Neural Machine Translation

### Question

> Which data-selection algorithms do they use?

### Passage

> The data used for training Machine Translation (MT) models consist mainly of a set of parallel sentences (a set of sentence-pairs in which each sentence is paired with its translation). As Neural Machine Translation (NMT) models typically achieve best performance when using large sets of parallel sentences, they can benefit from the sentences created by Natural Language Generation (NLG) systems. Although artificial data is expected to be of lower quality than authentic sentences, it still can help the model to learn how to better generalize over the training instances and produce better translations.
> 
> A popular technique used to create artificial data is the back-translation technique BIBREF0, BIBREF1. This consists of generating sentences in the source language by translating monolingual sentences in the target language. Then, these sentences in both languages are paired and can be used to augment the original parallel training set used to build better NMT models.
> 
> Nonetheless, if synthetic data are not in the same domain as the test set, it can also hurt the performance. For this reason, we explore an alternative approach to better use the artificially-generated training instances to improve NMT models. In particular, we propose that instead of blindly adding back-translated sentences into the training set they can be considered as candidate sentences for a data-selection algorithm to decide which sentence-pairs should be used to fine-tune the NMT model. By doing that, instead of increasing the number of training instances in a motivated manner, the generated sentences provide us with more chances of obtaining relevant parallel sentences (and still use smaller sets for fine-tuning).
> 
> As we want to build task-specific NMT models, in this work we explore two data-selection algorithms that are classified as Transductive Algorithms (TA): Infrequent N-gram Recovery (INR) and Feature Decay Algorithms (FDA). These methods use the test set $S_{test}$ (the document to be translated) as the seed to retrieve sentences. In transductive learning BIBREF2 the goal is to identify the best training instances to learn how to classify a given test set. In order to select these sentences, the TAs search for those n-grams in the test set that are also present in the source side of the candidate sentences.
> 
> Although augmenting the candidate

### Relevance

Label: 

## Record 0463

Paper: Selecting Artificially-Generated Sentences for Fine-Tuning Neural Machine Translation

### Question

> Which data-selection algorithms do they use?

### Passage

> In this work, we have presented how artificially generated sentences can be used to augment a set of candidate sentences so data-selection algorithms have a wider variety of sentences to select from. The TA-selected sets have been evaluated according to how useful they are for improving NMT models.
> 
> We have presented three methods of creating such hybrid data: (i) by allowing the TA decide whether to select authentic or synthetic data (hybr); (ii) by performing independent executions of the TA on authentic and synthetic sets (batch); and (iii) using an MT-generated seed to select monolingual sentences so only the extracted subset is back-translated (online).
> 
> The experiments showed that artificially-generated sentences can be as competitive as authentic data, as models built with different proportions of authentic and synthetic data achieve similar or even better performance than those fine-tuned with authentic pairs only. On one hand, those sentences whose target-sides could hurt the performance of NMT (such as sentences in a different language to that expected) causes the back-translated sentence to also contain unnatural n-grams and so TAs would not select them. On the other hand, if the source-side sentence is not an accurate translation of the target side (the problem of comparable corpus), the back-translated counterpart can be a better alternative to use as training data.
> 
> In the future, we want to explore other language pairs and other transductive algorithms. Another limitation of this work is that we have augmented the candidate pool with synthetic sentences generated by a single model. We propose to explore whether using several models for generating the synthetic sentences (including different approaches such as combining statistical and neural model BIBREF30) to augment the candidate pool can cause the selected data to further improve NMT models.

### Relevance

Label: 

## Record 0464

Paper: Selecting Artificially-Generated Sentences for Fine-Tuning Neural Machine Translation

### Question

> Which data-selection algorithms do they use?

### Passage

> The proposal of BIBREF0 showed that NMT models can be improved by back-translating a set of (monolingual) sentences in the target side into the source side using an MT model. Other uses of monolingual target-side sentences include building the parallel set by using a NULL token in the source side BIBREF0 or creating language models to improve the decoder BIBREF3.
> 
> BIBREF4 improve the model used for back-translation by training this model with increasing amounts of artificial sentences. They iteratively improve the models creating artificial sentences of better quality.
> 
> Similarly to this paper, the use of artificially-generated sentences to fine-tuned models has also been explored by BIBREF5 where they select monolingual authentic sentences in the source-side and translate them into the target language, or the work of BIBREF6 where they use back-translated sentences only to adapt the models.

### Relevance

Label: 

## Record 0465

Paper: Selecting Artificially-Generated Sentences for Fine-Tuning Neural Machine Translation

### Question

> Which data-selection algorithms do they use?

### Passage

> The work presented in this paper is based on two main concepts: the generation of synthetic sentences, and the selection of sentences from a set $S$ of candidates.

### Relevance

Label: 

## Record 0466

Paper: SAMSum Corpus: A Human-annotated Dialogue Dataset for Abstractive Summarization

### Question

> Do authors propose some better metric than ROUGE for measurement of abstractive dialogue summarization?

### Passage

> This paper is a step towards abstractive summarization of dialogues by (1) introducing a new dataset, created for this task, (2) comparison with news summarization by the means of automated (ROUGE) and human evaluation.
> 
> Most of the tools and the metrics measuring the quality of text summarization have been developed for a single-speaker document, such as news; as such, they are not necessarily the best choice for conversations with several speakers.
> 
> We test a few general-purpose summarization models. In terms of human evaluation, the results of dialogues summarization are worse than the results of news summarization. This is connected with the fact that the dialogue structure is more complex – information is spread in multiple utterances, discussions, questions, more typos and slang words appear there, posing new challenges for summarization. On the other hand, dialogues are divided into utterances, and for each utterance its author is assigned. We demonstrate in experiments that the models benefit from the introduction of separators, which mark utterances for each person. This suggests that dedicated models having some architectural changes, taking into account the assignation of a person to an utterance in a systematic manner, could improve the quality of dialogue summarization.
> 
> We show that the most popular summarization metric ROUGE does not reflect the quality of a summary. Looking at the ROUGE scores, one concludes that the dialogue summarization models perform better than the ones for news summarization. In fact, this hypothesis is not true – we performed an independent, manual analysis of summaries and we demonstrated that high ROUGE results, obtained for automatically-generated dialogue summaries, correspond with lower evaluation marks given by human annotators. An interesting example of the misleading behavior of the ROUGE metrics is presented in Table TABREF35 for Dialogue 4, where a wrong summary – 'paul and cindy don't like red roses.' – obtained all ROUGE values higher than a correct summary – 'paul asks cindy what color flowers should buy.'. Despite lower ROUGE values, news summaries were scored higher by human evaluators. We conclude that when measuring the quality of model-generated summaries, the ROUGE metrics are more indicative for news than for dialogues, and a new metric should be designed to measure the quality

### Relevance

Label: 

## Record 0467

Paper: SAMSum Corpus: A Human-annotated Dialogue Dataset for Abstractive Summarization

### Question

> Do authors propose some better metric than ROUGE for measurement of abstractive dialogue summarization?

### Passage

> ROUGE is a standard way of evaluating the quality of machine generated summaries by comparing them with reference ones. The metric based on n-gram overlapping, however, may not be very informative for abstractive summarization, where paraphrasing is a keypoint in producing high-quality sentences. To quantify this conjecture, we manually evaluated summaries generated by the models for 150 news and 100 dialogues. We asked two linguists to mark the quality of every summary on the scale of $-1$, 0, 1, where $-1$ means that a summarization is poor, extracts irrelevant information or does not make sense at all, 1 – it is understandable and gives a brief overview of the text, and 0 stands for a summarization that extracts only a part of relevant information, or makes some mistakes in the produced summary.
> 
> We noticed a few annotations (7 for news and 4 for dialogues) with opposite marks (i.e. one annotator judgement was $-1$, whereas the second one was 1) and decided to have them annotated once again by another annotator who had to resolve conflicts. For the rest, we calculated the linear weighted Cohen's kappa coefficient BIBREF22 between annotators' scores. For news examples, we obtained agreement on the level of $0.371$ and for dialogues – $0.506$. The annotators' agreement is higher on dialogues than on news, probably because of structures of those data – articles are often long and it is difficult to decide what the key-point of the text is; dialogues, on the contrary, are rather short and focused mainly on one topic.
> 
> For manually evaluated samples, we calculated ROUGE metrics and the mean of two human ratings; the prepared statistics is presented in Table TABREF27. As we can see, models generating dialogue summaries can obtain high ROUGE results, but their outputs are marked as poor by human annotators. Our conclusion is that the ROUGE metric corresponds with the quality of generated summaries for news much better than for dialogues, confirmed by Pearson's correlation between human evaluation and the ROUGE metric, shown in Table TABREF28.

### Relevance

Label: 

## Record 0468

Paper: SAMSum Corpus: A Human-annotated Dialogue Dataset for Abstractive Summarization

### Question

> Do authors propose some better metric than ROUGE for measurement of abstractive dialogue summarization?

### Passage

> The baseline commonly used in the news summarization task is Lead-3 BIBREF4, which takes three leading sentences of the document as the summary. The underlying assumption is that the beginning of the article contains the most significant information. Inspired by the Lead-n model, we propose a few different simple models:
> 
> MIDDLE-n, which takes n utterances from the middle of the dialogue,
> 
> LONGEST-n, treating only n longest utterances in order of length as a summary,
> 
> LONGER-THAN-n, taking only utterances longer than n characters in order of length (if there is no such long utterance in the dialogue, takes the longest one),
> 
> MOST-ACTIVE-PERSON, which treats all utterances of the most active person in the dialogue as a summary.
> 
> Results of the evaluation of the above models are reported in Table TABREF9. There is no obvious baseline for the task of dialogues summarization. We expected rather low results for Lead-3, as the beginnings of the conversations usually contain greetings, not the main part of the discourse. However, it seems that in our dataset greetings are frequently combined with question-asking or information passing (sometimes they are even omitted) and such a baseline works even better than the MIDDLE baseline (taking utterances from the middle of a dialogue). Nevertheless, the best dialogue baseline turns out to be the LONGEST-3 model.

### Relevance

Label: 

## Record 0469

Paper: SAMSum Corpus: A Human-annotated Dialogue Dataset for Abstractive Summarization

### Question

> Do authors propose some better metric than ROUGE for measurement of abstractive dialogue summarization?

### Passage

> news summaries were scored higher by human evaluators. We conclude that when measuring the quality of model-generated summaries, the ROUGE metrics are more indicative for news than for dialogues, and a new metric should be designed to measure the quality of abstractive dialogue summaries.

### Relevance

Label: 

## Record 0470

Paper: SAMSum Corpus: A Human-annotated Dialogue Dataset for Abstractive Summarization

### Question

> Do authors propose some better metric than ROUGE for measurement of abstractive dialogue summarization?

### Passage

> The results for the news summarization task are shown in Table TABREF25 and for the dialogue summarization – in Table TABREF26. In both domains, the best models' ROUGE-1 exceeds 39, ROUGE-2 – 17 and ROUGE-L – 36. Note that the strong baseline for news (Lead-3) is outperformed in all three metrics only by one model. In the case of dialogues, all tested models perform better than the baseline (LONGEST-3).
> 
> In general, the Transformer-based architectures benefit from training on the joint dataset: news+dialogues, even though the news and the dialogue documents have very different structures. Interestingly, this does not seem to be the case for the Pointer Generator or Fast Abs RL model.
> 
> The inclusion of a separation token between dialogue utterances is advantageous for most models – presumably because it improves the discourse structure. The improvement is most visible when training is performed on the joint dataset.
> 
> Having compared two variants of the Fast Abs RL model – with original utterances and with enhanced ones (see Section SECREF11), we conclude that enhancing utterances with information about the other interlocutors helps achieve higher ROUGE values.
> 
> The largest improvement of the model performance is observed for LightConv and DynamicConv models when they are complemented with pretrained embeddings from the language model GPT-2, trained on enormous corpora.
> 
> It is also worth noting that some models (Pointer Generator, Fast Abs RL), trained only on the dialogues corpus (which has 16k dialogues), reach similar level (or better) in terms of ROUGE metrics than models trained on the CNN/DM news dataset (which has more than 300k articles). Adding pretrained embeddings and training on the joined dataset helps in achieving significantly higher values of ROUGE for dialogues than the best models achieve on the CNN/DM news dataset.
> 
> According to ROUGE metrics, the best performing model is DynamicConv with GPT-2 embeddings, trained on joined news and dialogue data with an utterance separation token.

### Relevance

Label: 

## Record 0471

Paper: Counterfactual Data Augmentation for Mitigating Gender Stereotypes in Languages with Rich Morphology

### Question

> Why does not the approach from English work on other languages?

### Passage

> One of the biggest challenges faced by modern natural language processing (NLP) systems is the inadvertent replication or amplification of societal biases. This is because NLP systems depend on language corpora, which are inherently “not objective; they are creations of human design” BIBREF0 . One type of societal bias that has received considerable attention from the NLP community is gender stereotyping BIBREF1 , BIBREF2 , BIBREF3 . Gender stereotypes can manifest in language in overt ways. For example, the sentence he is an engineer is more likely to appear in a corpus than she is an engineer due to the current gender disparity in engineering. Consequently, any NLP system that is trained such a corpus will likely learn to associate engineer with men, but not with women BIBREF4 .
> 
> To date, the NLP community has focused primarily on approaches for detecting and mitigating gender stereotypes in English BIBREF5 , BIBREF6 , BIBREF7 . Yet, gender stereotypes also exist in other languages because they are a function of society, not of grammar. Moreover, because English does not mark grammatical gender, approaches developed for English are not transferable to morphologically rich languages that exhibit gender agreement BIBREF8 . In these languages, the words in a sentence are marked with morphological endings that reflect the grammatical gender of the surrounding nouns. This means that if the gender of one word changes, the others have to be updated to match. As a result, simple heuristics, such as augmenting a corpus with additional sentences in which he and she have been swapped BIBREF9 , will yield ungrammatical sentences. Consider the Spanish phrase el ingeniero experto (the skilled engineer). Replacing ingeniero with ingeniera is insufficient—el must also be replaced with la and experto with experta.
> 
> In this paper, we present a new approach to counterfactual data augmentation BIBREF10 for mitigating gender stereotypes associated with animate nouns (i.e., nouns that represent people) for morphologically rich languages. We introduce a Markov random field with an optional neural parameterization that infers the manner in which a sentence must change when altering the grammatical gender of particular nouns. We use this model as part of a four-step process, depicted in fig:pipeline, to reinflect entire sentences

### Relevance

Label: 

## Record 0472

Paper: Counterfactual Data Augmentation for Mitigating Gender Stereotypes in Languages with Rich Morphology

### Question

> Why does not the approach from English work on other languages?

### Passage

> In contrast to previous work, we focus on mitigating gender stereotypes in languages with rich morphology—specifically languages that exhibit gender agreement. To date, the NLP community has focused on approaches for detecting and mitigating gender stereotypes in English. For example, BIBREF5 proposed a way of mitigating gender stereotypes in word embeddings while preserving meanings; BIBREF10 studied gender stereotypes in language models; and BIBREF13 introduced a novel Winograd schema for evaluating gender stereotypes in co-reference resolution. The most closely related work is that of BIBREF9 , who used CDA to reduce gender stereotypes in co-reference resolution; however, their approach yields ungrammatical sentences in morphologically rich languages. Our approach is specifically intended to yield grammatical sentences when applied to such languages. BIBREF29 also focused on morphologically rich languages, specifically Arabic, but in the context of gender identification in machine translation.

### Relevance

Label: 

## Record 0473

Paper: Counterfactual Data Augmentation for Mitigating Gender Stereotypes in Languages with Rich Morphology

### Question

> Why does not the approach from English work on other languages?

### Passage

> conjunctions. For example, consider the phrase él es un ingeniero y escritor (he is an engineer and a writer). Replacing ingeniero with ingeniera does not necessarily result in escritor being changed to escritora. This is because two nouns do not normally need to have the same gender when they are conjoined. Moreover, our MRF does not include co-reference information, so it cannot tell that, in this case, both nouns refer to the same person. Note that including co-reference information in our MRF would create cycles and inference would no longer be exact. Additionally, the lack of co-reference information means that, for Spanish, our approach fails to convert nouns that are noun-modifiers or indirect objects of verbs.
> 
> Somewhat surprisingly, the neural parameterization does not outperform the linear parameterization. We proposed the neural parameterization to allow parameter sharing among edges with different parts of speech and labels; however, this parameter sharing does not seem to make a difference in practice, so the linear parameterization is sufficient.

### Relevance

Label: 

## Record 0474

Paper: Counterfactual Data Augmentation for Mitigating Gender Stereotypes in Languages with Rich Morphology

### Question

> Why does not the approach from English work on other languages?

### Passage

> We presented a new approach for converting between masculine-inflected and feminine-inflected noun phrases in morphologically rich languages. To do this, we introduced a Markov random field with an optional neural parameterization that infers the manner in which a sentence must change to preserve morpho-syntactic agreement when altering the grammatical gender of particular nouns. To the best of our knowledge, this task has not been studied previously. As a result, there is no existing annotated corpus of paired sentences that can be used as “ground truth.” Despite this limitation, we evaluated our approach both intrinsically and extrinsically, achieving promising results. For example, we demonstrated that our approach reduces gender stereotyping in neural language models. Finally, we also identified avenues for future work, such as the inclusion of co-reference information.

### Relevance

Label: 

## Record 0475

Paper: Counterfactual Data Augmentation for Mitigating Gender Stereotypes in Languages with Rich Morphology

### Question

> Why does not the approach from English work on other languages?

### Passage

> To the best of our knowledge, this task has not been studied previously. As a result, there is no existing annotated corpus of paired sentences that can be used as “ground truth.” We therefore annotated Spanish and Hebrew sentences ourselves, with annotations made by native speakers of each language. Specifically, for each language, we extracted sentences containing animate nouns from that language's UD treebank. The average length of these extracted sentences was 37 words. We then manually inspected each sentence, intervening on the gender of the animate noun and reinflecting the sentence accordingly. We chose Spanish and Hebrew because gender agreement operates differently in each language. We provide corpus statistics for both languages in the top two rows of tab:data.
> 
> We created a hard-coded INLINEFORM0 to serve as a baseline for each language. For Spanish, we only activated, i.e. set to a number greater than zero, values that relate adjectives and determiners to nouns; for Hebrew, we only activated values that relate adjectives and verbs to nouns. We created two separate baselines because gender agreement operates differently in each language.
> 
> To evaluate our approach, we held all morpho-syntactic subtags fixed except for gender. For each annotated sentence, we intervened on the gender of the animate noun. We then used our model to infer which of the remaining tags should be updated (updating a tag means swapping the gender subtag because all morpho-syntactic subtags were held fixed except for gender) and reinflected the lemmata. Finally, we used the annotations to compute the tag-level INLINEFORM0 score and the form-level accuracy, excluding the animate nouns on which we intervened.
> 
> We present the results in tab:intrinsic. Recall is consistently significantly lower than precision. As expected, the baselines have the highest precision (though not by much). This is because they reflect well-known rules for each language. That said, they have lower recall than our approach because they fail to capture more subtle relationships.
> 
> For both languages, our approach struggles with conjunctions. For example, consider the phrase él es un ingeniero y escritor (he is an engineer and a writer). Replacing ingeniero with ingeniera does not necessarily result in escritor being changed to escritora. This is because two nouns do not

### Relevance

Label: 

## Record 0476

Paper: Compositional Neural Machine Translation by Removing the Lexicon from Syntax

### Question

> Does having constrained neural units imply word meanings are fixed across different context?

### Passage

> The first experiment by BIBREF4 BIBREF4 included a dataset of 14 training pairs and 10 test pairs. In the dataset, an input is a sequence of words from an artificial language created by the authors. An output is a sequence of colored dots. Because the dataset is so small, we use the train set as the validation set. The input and output dictionary are 7 and 4 words, respectively (not including the stop, “$<s>$,” token). In their paper, the authors argue that it is clear that the words have meanings. Four of the words correspond to unique output tokens, and three of them correspond to functions of the output tokens (for example, repeating the same dot three times). The dataset showcases the contrast between human and standard neural network responses. Their paper shows that humans had high accuracy on the test set, whereas standard neural models scored essentially zero exact matches.
> 
> The LLA-LSTM model that we tested appears to achieve only insignificantly higher results in Table TABREF4. However, it has learned, from just 14 training examples, how to map some of the words to BIBREF4's interpretation of their context-invariant meanings. This is shown in Figure FIGREF6 (a). In the figure, “dax,” “lug,” “wif,” and “zup” are interpreted correctly to mean “r,” “g,” “b,” and “y,” respectively. Here, the letters correspond to the types of unique dots, which are red, green, blue, and yellow, respectively. The other words, “fep,” “kiki,” and “blicket,” are taken by BIBREF4 to have functional meanings, and so are correctly not associated strongly with any of the output tokens. The exceptions are two erroneous associations between “kiki” and blue and “blicket” and green. Also, every sentence has a stop token, so the LLA units learned that the context-invariant meanings of each word include it. The LLA units can handle cases where a word corresponds to multiple output tokens, and the output tokens need not be monolithic in the output sequence. As shown in tests from all of the other domains, these output token correspondences may or may not be relevant depending on the specific context of a word, but the recurrent component of the architecture is capable of determining which to use.

### Relevance

Label: 

## Record 0477

Paper: Compositional Neural Machine Translation by Removing the Lexicon from Syntax

### Question

> Does having constrained neural units imply word meanings are fixed across different context?

### Passage

> Studies of Broca's and Wernicke's aphasia provide evidence that our brains understand an utterance by creating separate representations for word meaning and word arrangement BIBREF0. There is a related thesis about human language, present across many theories of semantics, which is that syntactic categories are partially agnostic to the identity of words BIBREF1. This regularity in how humans derive meaning from an utterance is applicable to the task of natural language translation. This is because, by definition, translation necessitates the creation of a meaning representation for an input. According to the cognitive and neural imperative, we introduce new units to regularize an artificial neural encoder and decoder BIBREF2. These are called the Lexicon and Lexicon-Adversary units (collectively, LLA). Tests are done on a diagnostic task, and naturalistic tasks including semantic parsing, syntactic parsing, and English to Mandarin Chinese translation. We evaluate a Long Short-Term Memory (LSTM) BIBREF3 encoder and decoder, with and without the LLA units, and show that the LLA version achieves superior translation performance. In addition, we examine our model's weights, and its performance when some of its neurons are damaged. We find that the model exhibits the knowledge and the lack thereof expected of a Broca's aphasic BIBREF0 when one module's weights are corrupted. It also exhibits that expected of a Wernicke's aphasic BIBREF0 when another module's weights are corrupted.

### Relevance

Label: 

## Record 0478

Paper: Compositional Neural Machine Translation by Removing the Lexicon from Syntax

### Question

> Does having constrained neural units imply word meanings are fixed across different context?

### Passage

> are several percentage points. In the few scenarios where the LLA-LSTM model does not improve upon the standard model, the discrepancy between the models is small. The discrepancy is also small when the LLA-LSTM model with no adversary performs better than the LLA-LSTM model. Table TABREF4 displays the test results across the domains.
> 
> Additionally, we provide evidence that the model learns knowledge of a separation between syntax and the lexicon that is similar to that of a human. Figure FIGREF6 displays the learned $\sigma (w)$ embeddings for some input words, across the domains. To avoid cherry-picking the results, we chose the input words arbitrarily, subject to the following constraint. We considered each word to typically have a different syntactic category than the other choices from that domain. This constraint was used to present a diverse selection of words. Table TABREF5 displays the output behavior of models that we damaged to resemble the damage that causes aphasia. To avoid cherry-picking the results, we arbitrarily chose an input for each domain, subject to the following constraint. The input is not in the train set and the undamaged LLA-LSTM model produces a translation that we judge to be correct. For all inputs that we chose, damage to the analog of Broca's area (the LSTMs) results in an output that describes content only if it is described by the input. However, the output does not show understanding of the input's syntax. In the naturalistic domains, damage to the analog of Wernicke's area (the Lexicon Unit) results in an output with incorrect content that would be acceptable if the input had different words but the same syntax. These knowledge distortions are precisely those that are expected in the respective human aphasics BIBREF0. We also provide corpus-level results from the damaged models by presenting mean precision on the test sets. Because the output languages in all of our domains use tokens to represent meanings in many cases, it is expected that the analog to Wernicke's area is responsible for maintaining a high precision.

### Relevance

Label: 

## Record 0479

Paper: Compositional Neural Machine Translation by Removing the Lexicon from Syntax

### Question

> Does having constrained neural units imply word meanings are fixed across different context?

### Passage

> There is evidence that generic attention mechanisms for machine translation already utilize the thesis that words have meanings that are independent of syntax. They learn correspondences between output tokens and a hidden state produced immediately after an encoder reads a particular input word BIBREF14. But the same mechanism is not at play in our model. Generic attention mechanisms do not necessarily impose a constraint on the input's syntax representation. Additionally, typical objective functions do not explicitly link input words with invariance in the output. Finally, one does not need to choose either LLA units or attention. LLA units can be incorporated into recurrent neural network systems with attention or other machine transduction architectures such as transformers BIBREF15.
> 
> Recent work has incorporated some of the ideas in our paper into a neural machine translation model with the use of a specific attention mechanism BIBREF16. But the authors only demonstrate success on a single artificial dataset with a lexicon of about ten words, and they did not explore the effects of damaging parts of their model. Their optimization procedure also does not prohibit context-invariant lexical information from passing through the recurrent portion of their model. This incorrectly allows the possibility for a representation to be learned that gives every input word its own syntactic category. Lastly, their architecture provides a softer constraint than the one that we demonstrate, as information from several input words can aggregate and pass through the non-recurrent module that they use.
> 
> There are other attempts to incorporate theories about human language to regularize a transduction model, but many have not scaled to the level of generality that the LLA units and some attention architectures show. These include synchronous grammars BIBREF17, data augmentation BIBREF18, Meta learning BIBREF19, and hard-coded maps or copying capabilities from input to output BIBREF20 BIBREF21. All require hard-coded rules that are often broken by the real world.

### Relevance

Label: 

## Record 0480

Paper: Compositional Neural Machine Translation by Removing the Lexicon from Syntax

### Question

> Does having constrained neural units imply word meanings are fixed across different context?

### Passage

> Neural and cognitive theories provide an imperative for computational models to understand human language by separating representations of word meanings from those of syntax. Using this constraint, we introduced new neural units that can provide this separation for the purpose of translating human languages. When added to an LSTM encoder and decoder, our units showed improvements in all of our experiment domains over the typical model. The domains were a small artificial diagnostic dataset, semantic parsing, syntactic parsing, and English to Mandarin Chinese translation. We also showed that the model learns a representation of human language that is similar to that of our brains. When damaged, the model displays the same knowledge distortions that aphasics do.

### Relevance

Label: 

## Record 0481

Paper: Multi-modal Dense Video Captioning

### Question

> What ASR system do they use?

### Passage

> useful caption for it. Also, other types of videos as instruction videos, sport videos, or video lectures could be challenging for a captioning model.
> 
> In contrast, we build our model to utilize video frames, raw audio signal, and the speech content in the caption generation process. To this end, we deploy automatic speech recognition (ASR) system BIBREF11 to extract time-aligned captions of what is being said (similar to subtitles) and employ it alongside with video and audio representations in the transformer model.
> 
> The proposed model is assessed using the challenging ActivityNet Captions BIBREF2 benchmark dataset, where we obtain competitive results to the current state-of-the-art. The subsequent ablation studies indicate a substantial contribution from audio and speech signals. Moreover, we retrieve and perform breakdown analysis by utilizing previously unused video category tags provided with the original YouTube videos BIBREF12. The program code of our model and the evaluation approach will be made publicly available.

### Relevance

Label: 

## Record 0482

Paper: Multi-modal Dense Video Captioning

### Question

> What ASR system do they use?

### Passage

> In this section, we briefly outline the workflow of our method referred to as Multi-modal Dense Video Captioning (MDVC) which is shown in Fig. FIGREF5. The goal of our method is to temporally localize events on a video and to produce a textual description for each of them. To this end, we apply a two-stage approach.
> 
> Firstly, we obtain the temporal event locations. For this task, we employ the Bidirectional Single-Stream Temporal action proposals network (Bi-SST) proposed in BIBREF5. Bi-SST applies 3D Convolution network (C3D) BIBREF44 to video frames and extracts features that are passed to subsequent bi-directional LSTM BIBREF45 network. The LSTM accumulates visual cues over time and predicts confidence scores for each location to be start/end point of an event. Finally, a set of event proposals (start/end times) is obtained and passed to the second stage for caption generation.
> 
> Secondly, we generate the captions given a proposal. To produce inputs from audio, visual, and speech modalities, we use Inflated 3D convolutions (I3D) BIBREF46 for visual and VGGish network BIBREF47 for audio modalities. For speech representation as a text, we employ an external ASR system BIBREF11. To represent the text into a numerical form, we use a similar text embedding which is used for caption encoding. The features are, then, fed to individual transformer models along with the words of a caption from the previous time steps. The output of the transformer is passed into a generator which fuses the outputs from all modalities and estimates a probability distribution over the word vocabulary. After sampling the next word, the process is repeated until a special end token is obtained. Fig. FIGREF1 illustrates an example modality and the corresponding event captions.

### Relevance

Label: 

## Record 0483

Paper: Multi-modal Dense Video Captioning

### Question

> What ASR system do they use?

### Passage

> In Table TABREF37, we present a comparison with another body of methods BIBREF8, BIBREF9 which were not included in the main comparison as they were using Reinforcement Learning (RL) approach to directly optimize the non-differentiable metric (METEOR). We believe that our method could also benefit from these as the ablation studies BIBREF8, BIBREF9 show significant gains obtained by applying them. As it was anticipated, in general, methods which employ reinforcement learning perform better in terms of METEOR. Interestingly, our model still outperforms BIBREF8 which uses RL in the captioning module.

### Relevance

Label: 

## Record 0484

Paper: Multi-modal Dense Video Captioning

### Question

> What ASR system do they use?

### Passage

> We perform our experiments using ActivityNet Captions dataset BIBREF2 that is considered as the standard benchmark for dense video captioning task. The dataset contains approximately 20k videos from YouTube and split into 50/25/25 % parts for training, validation, and testing, respectively. Each video, on average, contains 3.65 temporally localized captions, around 13.65 words each, and two minutes long. In addition, each video in the validation set is annotated twice by different annotators. We report all results using the validation set (no ground truth is provided for the test set).
> 
> The dataset itself is distributed as a collection of links to YouTube videos, some of which are no longer available. Authors provide pre-computed C3D features and frames at 5fps, but these are not suitable for our experiments. At the time of writing, we found 9,167 (out of 10,009) training and 4,483 (out of 4,917) validation videos which is, roughly, 91 % of the dataset. Out of these 2,798 training and 1,374 validation videos (approx. 28 %) contain at least one speech segment. The speech content was obtained from the closed captions (CC) provided by the YouTube ASR system which can be though as subtitles.

### Relevance

Label: 

## Record 0485

Paper: Multi-modal Dense Video Captioning

### Question

> What ASR system do they use?

### Passage

> Before training, we pre-calculate the features for both audio and visual modalities. In particular, the audio features were extracted using VGGish BIBREF47 which was trained on AudioSet BIBREF55. The input to the VGGish model is a $96\times 64$ log mel-scaled spectrogram extracted for non-overlapping $0.96$ seconds segments. The log mel-scaled spectrogram is obtained by applying Short-Time Fourier Transform on a 16 kHz mono audio track using a periodic Hann window with 25 ms length with 10 ms overlap. The output is a 128-d feature vector after an activation function and extracted before a classification layer. Therefore, the input to MDVC is a matrix with dimension $T_j^a \times 128$ where $T_j^a$ is the number of features proposal $p_j$ consists of.
> 
> The visual features were extracted using I3D BIBREF46 network which inputs a set of 24 RGB and optical flow frames extracted at 25 fps. The optical flow is extracted with PWC-Net BIBREF58. First, each frame is resized such that the shortest side is 256 pixels. Then, the center region is cropped to obtain $224\times 224$ frames. Both RGB and flow stacks are passed through the corresponding branch of I3D. The output of each branch are summed together producing 1024-d features for each stack of 24 frames. Hence, the resulting matrix has the shape: $T_j^v\times 1024$, where $T_j^v$ is the number of features required for a proposal $p_j$.
> 
> We use 24 frames for I3D input to temporally match with the input of the audio modality as $\frac{24}{25} = 0.96$. Also note that I3D was pre-trained on the Kinetics dataset with inputs of 64 frames, while we use 24 frames. This is a valid approach since we employ the output of the second to the last layer after activation and average it on the temporal axis.
> 
> The input for speech modality is represented by temporally allocated text segments in the English language (one could think of them as subtitles). For a proposal $ p_j $, we pick all segments that both: a) end after the proposal starting point, and b) start before the proposal ending point. This provides us with sufficient coverage of what has been said during the proposal segment. Similarly to captions, each word in a

### Relevance

Label: 

## Record 0486

Paper: Distant supervision for emotion detection using Facebook reactions

### Question

> What was their performance on emotion detection?

### Passage

> Three datasets annotated with emotions are commonly used for the development and evaluation of emotion detection systems, namely the Affective Text dataset, the Fairy Tales dataset, and the ISEAR dataset. In order to compare our performance to state-of-the-art results, we have used them as well. In this Section, in addition to a description of each dataset, we provide an overview of the emotions used, their distribution, and how we mapped them to those we obtained from Facebook posts in Section SECREF7 . A summary is provided in Table TABREF8 , which also shows, in the bottom row, what role each dataset has in our experiments: apart from the development portion of the Affective Text, which we used to develop our models (Section SECREF4 ), all three have been used as benchmarks for our evaluation.

### Relevance

Label: 

## Record 0487

Paper: Distant supervision for emotion detection using Facebook reactions

### Question

> What was their performance on emotion detection?

### Passage

> In Table TABREF26 we report the results of our model on the three datasets standardly used for the evaluation of emotion classification, which we have described in Section SECREF3 .
> 
> Our B-M model relies on subsets of Facebook pages for training, which were chosen according to their performance on the development set as well as on the observation of emotions distribution on different pages and in the different datasets, as described in Section SECREF4 . The feature set we use is our best on the development set, namely all the features plus Google-based embeddings, but excluding the lexicon. This makes our approach completely independent of any manual annotation or handcrafted resource. Our model's performance is compared to the following systems, for which results are reported in the referred literature. Please note that no other existing model was re-implemented, and results are those reported in the respective papers.

### Relevance

Label: 

## Record 0488

Paper: Distant supervision for emotion detection using Facebook reactions

### Question

> What was their performance on emotion detection?

### Passage

> For years, on Facebook people could leave comments to posts, and also “like” them, by using a thumbs-up feature to explicitly express a generic, rather underspecified, approval. A “like” could thus mean “I like what you said", but also “I like that you bring up such topic (though I find the content of the article you linked annoying)".
> 
> In February 2016, after a short trial, Facebook made a more explicit reaction feature available world-wide. Rather than allowing for the underspecified “like” as the only wordless response to a post, a set of six more specific reactions was introduced, as shown in Figure FIGREF1 : Like, Love, Haha, Wow, Sad and Angry. We use such reactions as proxies for emotion labels associated to posts.
> 
> We collected Facebook posts and their corresponding reactions from public pages using the Facebook API, which we accessed via the Facebook-sdk python library. We chose different pages (and therefore domains and stances), aiming at a balanced and varied dataset, but we did so mainly based on intuition (see Section SECREF4 ) and with an eye to the nature of the datasets available for evaluation (see Section SECREF5 ). The choice of which pages to select posts from is far from trivial, and we believe this is actually an interesting aspect of our approach, as by using different Facebook pages one can intrinsically tackle the domain-adaptation problem (See Section SECREF6 for further discussion on this). The final collection of Facebook pages for the experiments described in this paper is as follows: FoxNews, CNN, ESPN, New York Times, Time magazine, Huffington Post Weird News, The Guardian, Cartoon Network, Cooking Light, Home Cooking Adventure, Justin Bieber, Nickelodeon, Spongebob, Disney.
> 
> Note that thankful was only available during specific time spans related to certain events, as Mother's Day in May 2016.
> 
> For each page, we downloaded the latest 1000 posts, or the maximum available if there are fewer, from February 2016, retrieving the counts of reactions for each post. The output is a JSON file containing a list of dictionaries with a timestamp, the post and a reaction vector with frequency values, which indicate how many users used that reaction in response to the post (Figure FIGREF3

### Relevance

Label: 

## Record 0489

Paper: Distant supervision for emotion detection using Facebook reactions

### Question

> What was their performance on emotion detection?

### Passage

> The Late Night Show, as the target audience is likely to feel very differently about the same issue. This also brings up theoretical issues related more generally to the definition of the emotion detection task, as it's strongly dependent on personal traits of the audience. Also, in this work, pages initially selected on availability and intuition were further grouped into sets to make training data according to performance on development data, and label distribution. Another criterion to be exploited would be vocabulary overlap between the pages and the datasets.
> 
> Lastly, we could develop single models for each emotion, treating the problem as a multi-label task. This would even better reflect the ambiguity and subjectivity intrinsic to assigning emotions to text, where content could be at same time joyful or sad, depending on the reader.

### Relevance

Label: 

## Record 0490

Paper: Distant supervision for emotion detection using Facebook reactions

### Question

> What was their performance on emotion detection?

### Passage

> Task 14 at SemEval 2007 BIBREF7 was concerned with the classification of emotions and valence in news headlines. The headlines where collected from several news websites including Google news, The New York Times, BBC News and CNN. The used emotion labels were Anger, Disgust, Fear, Joy, Sadness, Surprise, in line with the six basic emotions of Ekman's standard model BIBREF8 . Valence was to be determined as positive or negative. Classification of emotion and valence were treated as separate tasks. Emotion labels were not considered as mututally exclusive, and each emotion was assigned a score from 0 to 100. Training/developing data amounted to 250 annotated headlines (Affective development), while systems were evaluated on another 1000 (Affective test). Evaluation was done using two different methods: a fine-grained evaluation using Pearson's r to measure the correlation between the system scores and the gold standard; and a coarse-grained method where each emotion score was converted to a binary label, and precision, recall, and f-score were computed to assess performance. As it is done in most works that use this dataset BIBREF3 , BIBREF4 , BIBREF9 , we also treat this as a classification problem (coarse-grained). This dataset has been extensively used for the evaluation of various unsupervised methods BIBREF2 , but also for testing different supervised learning techniques and feature portability BIBREF10 .

### Relevance

Label: 

## Record 0491

Paper: Lancaster A at SemEval-2017 Task 5: Evaluation metrics matter: predicting sentiment from financial news headlines

### Question

> Which evaluation metrics do they use?

### Passage

> We first present our findings on the best performing parameters and features for the SVRs. These were determined by cross validation (CV) scores on the provided training data set using cosine similarity as the evaluation metric. We found that using uni-grams and bi-grams performs best and using only bi-grams to be the worst. Using the Unitok tokeniser always performed better than simple whitespace tokenisation. The binary presence of tokens over frequency did not alter performance. The C parameter was tested for three values; 0.01, 0.1 and 1. We found very little difference between 0.1 and 1, but 0.01 produced much poorer results. The eplison parameter was tested for 0.001, 0.01 and 0.1 the performance did not differ much but the lower the higher the performance but the more likely to overfit. Using word replacements was effective for all three types (company, positive and negative) but using a value N=10 performed best for both positive and negative words. Using target aspects also improved results. Therefore, the best SVR model comprised of: Unitok tokenisation, uni- and bi- grams, word representation, C=0.1, eplison=0.01, company, positive, and negative word replacements and target aspects. DISPLAYFORM0
> 
> The main evaluation over the test data is based on the best performing SVR and the two BLSTM models once trained on all of the training data. The result table TABREF28 shows three columns based on the three evaluation metrics that the organisers have used. Metric 1 is the original metric, weighted cosine similarity (the metric used to evaluate the final version of the results, where we were ranked 5th; metric provided on the task website). This was then changed after the evaluation deadline to equation EQREF25 (which we term metric 2; this is what the first version of the results were actually based on, where we were ranked 4th), which then changed by the organisers to their equation as presented in BIBREF18 (which we term metric 3 and what the second version of the results were based on, where we were ranked 5th).
> 
> As you can see from the results table TABREF28 , the difference between the metrics is quite substantial. This is due to the system's optimisation being based on metric 1 rather

### Relevance

Label: 

## Record 0492

Paper: Lancaster A at SemEval-2017 Task 5: Evaluation metrics matter: predicting sentiment from financial news headlines

### Question

> Which evaluation metrics do they use?

### Passage

> results were based on, where we were ranked 5th).
> 
> As you can see from the results table TABREF28 , the difference between the metrics is quite substantial. This is due to the system's optimisation being based on metric 1 rather than 2. Metric 2 is a classification metric for sentences with one aspect as it penalises values that are of opposite sign (giving -1 score) and rewards values with the same sign (giving +1 score). Our systems are not optimised for this because it would predict scores of -0.01 and true value of 0.01 as very close (within vector of other results) with low error whereas metric 2 would give this the highest error rating of -1 as they are not the same sign. Metric 3 is more similar to metric 1 as shown by the results, however the crucial difference is that again if you get opposite signs it will penalise more. We analysed the top 50 errors based on Mean Absolute Error (MAE) in the test dataset specifically to examine the number of sentences containing more than one aspect. Our investigation shows that no one system is better at predicting the sentiment of sentences that have more than one aspect (i.e. company) within them. Within those top 50 errors we found that the BLSTM systems do not know which parts of the sentence are associated to the company the sentiment is with respect to. Also they do not know the strength/existence of certain sentiment words.

### Relevance

Label: 

## Record 0493

Paper: Lancaster A at SemEval-2017 Task 5: Evaluation metrics matter: predicting sentiment from financial news headlines

### Question

> Which evaluation metrics do they use?

### Passage

> We created two different Bidirectional BIBREF14 Long Short-Term Memory BIBREF15 using the Python Keras library BIBREF16 with tensor flow backend BIBREF17 . We choose an LSTM model as it solves the vanishing gradients problem of Recurrent Neural Networks. We used a bidirectional model as it allows us to capture information that came before and after instead of just before, thereby allowing us to capture more relevant context within the model. Practically, a BLSTM is two LSTMs one going forward through the tokens the other in reverse order and in our models concatenating the resulting output vectors together at each time step.
> 
> The BLSTM models take as input a headline sentence of size L tokens where L is the length of the longest sentence in the training texts. Each word is converted into a 300 dimension vector using the word2vec model trained over the financial text. Any text that is not recognised by the word2vec model is represented as a vector of zeros; this is also used to pad out the sentence if it is shorter than L.
> 
> Both BLSTM models have the following similar properties:
> 
> Gradient clipping value of 5 - This was to help with the exploding gradients problem.
> 
> Minimised the Mean Square Error (MSE) loss using RMSprop with a mini batch size of 32.
> 
> The output activation function is linear.
> 
> The main difference between the two models is the use of drop out and when they stop training over the data (epoch). Both models architectures can be seen in figure FIGREF18 .
> 
> The BLSTMs do contain drop out in both the input and between the connections of 0.2 each. Finally the epoch is fixed at 25.
> 
> As can be seen from figure FIGREF18 , the drop out of 0.5 only happens between the layers and not the connections as in the SLSTM. Also the epoch is not fixed, it uses early stopping with a patience of 10. We expect that this model can generalise better than the standard one due to the higher drop out and that the epoch is based on early stopping which relies on a validation set to know when to stop training.

### Relevance

Label: 

## Record 0494

Paper: Lancaster A at SemEval-2017 Task 5: Evaluation metrics matter: predicting sentiment from financial news headlines

### Question

> Which evaluation metrics do they use?

### Passage

> In this short paper, we have described our implemented solutions to SemEval Task 5 track 2, utilising both SVR and BLSTM approaches. Our results show an improvement of around 5% when using LSTM models relative to SVR. We have shown that this task can be partially represented as an aspect based sentiment task on a domain specific problem. In general, our approaches acted as sentence level classifiers as they take no target company into consideration. As our results show, the choice of evaluation metric makes a great deal of difference to system training and testing. Future work will be to implement aspect specific information into an LSTM model as it has been shown to be useful in other work BIBREF9 .

### Relevance

Label: 

## Record 0495

Paper: Lancaster A at SemEval-2017 Task 5: Evaluation metrics matter: predicting sentiment from financial news headlines

### Question

> Which evaluation metrics do they use?

### Passage

> The objective of Task 5 Track 2 of SemEval semeval20175 was to predict the sentiment of news headlines with respect to companies mentioned within the headlines. This task can be seen as a finance-specific aspect-based sentiment task BIBREF0 . The main motivations of this task is to find specific features and learning algorithms that will perform better for this domain as aspect based sentiment analysis tasks have been conducted before at SemEval BIBREF1 .
> 
> Domain specific terminology is expected to play a key part in this task, as reporters, investors and analysts in the financial domain will use a specific set of terminology when discussing financial performance. Potentially, this may also vary across different financial domains and industry sectors. Therefore, we took an exploratory approach and investigated how various features and learning algorithms perform differently, specifically SVR and BLSTMs. We found that BLSTMs outperform an SVR without having any knowledge of the company that the sentiment is with respect to. For replicability purposes, with this paper we are releasing our source code and the finance specific BLSTM word embedding model.

### Relevance

Label: 

## Record 0496

Paper: Multilingual Sentiment Analysis: An RNN-Based Framework for Limited Data

### Question

> what dataset was used for training?

### Passage

> Building effective machine learning models for text requires data and different resources such as pre-trained word embeddings and reusable lexicons. Unfortunately, most of these resources are not entirely transferable to different domains, tasks or languages. Sentiment analysis is one such task that requires additional effort to transfer knowledge between languages.
> 
> In this paper, we studied the research question: Can we build reusable sentiment analysis models that can be utilized for making inferences in different languages without requiring separate models and resources for each language? To that end, we built a recurrent neural network model in the language that had largest data available. We took a general-to-specific model building strategy where the larger corpus that had reviews from different domains was first used to train the RNN model and a smaller single-domain corpus of sentiment reviews was used to specialize the model on the given domain. During scoring time, we used corpora for the given domain in different languages and translated them to English to be able to classify sentiments with the trained model. Experimental results showed that the proposed multilingual approach outperforms both the majority baseline and the lexicon-based baseline.
> 
> In this paper we made the sentiment analysis model specific to a single domain. For future work, we would like to investigate the effectiveness of our model on different review domains including hotel reviews and on different problems such as detecting stance.

### Relevance

Label: 

## Record 0497

Paper: Multilingual Sentiment Analysis: An RNN-Based Framework for Limited Data

### Question

> what dataset was used for training?

### Passage

> One of the crucial elements while using machine translation is to have highly accurate translations. It is likely that non-English words would not have word embeddings, which will dramatically affect the effectiveness of the system. We analyzed the effect of incorrect translations into our approach. To that end, we extracted all wrong predictions from the test set and computed the ratio of misclassifications that have non-English words in them. We first extracted all misclassifications for a given language and for each observation in the misclassification set, we iterated through each token to check if the token is in English. In this way, we counted the number of observations that contained at least one non-English word and divided that with the size of the misclassifications set. We used this ratio to investigate the effect of machine translation errors.
> 
> We found that 25.84% of Dutch, 21.76% of Turkish, 24.46% Spanish, and 10.71% of Russian reviews that were misclassified had non-English words in them. These non-English words might be causing the misclassifications. However, a large portion of the missclassifications is not caused due to not-translated words. At the end, the machine translation errors has some but not noticeable effects on our model. Therefore, we can claim that machine translation preserves most of the information necessary for sentiment analysis.
> 
> We also evaluated our model with an English corpus BIBREF27 to see its performance without any interference from machine translation errors. Using the English data for testing, the model achieved 87.06% accuracy where a majority baseline was 68.37% and the lexicon-based baseline was 60.10%.
> 
> Considering the improvements over the majority baseline achieved by the RNN model for both non-English (on the average 22.76% relative improvement; 15.82% relative improvement on Spanish, 72.71% vs. 84.21%, 30.53% relative improvement on Turkish, 56.97% vs. 74.36%, 37.13% relative improvement on Dutch, 59.63% vs. 81.77%, and 7.55% relative improvement on Russian, 79.60% vs. 85.62%) and English test sets (27.34% relative improvement), we can draw the conclusion that our model is robust to handle multiple languages. Building separate models for each language requires both labeled and unlabeled data. Even though having lots of labeled data in every language is the perfect case, it is unrealistic. Therefore, eliminating

### Relevance

Label: 

## Record 0498

Paper: Multilingual Sentiment Analysis: An RNN-Based Framework for Limited Data

### Question

> what dataset was used for training?

### Passage

> Two sets of corpora are used in this study, both are publicly available. The first set consists of English reviews and the second set contains restaurant reviews from four different languages (Spanish, Turkish, Dutch, Russian). We focus on polarity detection in reviews, therefore all datasets in this study have two class values (positive, negative).
> 
> With the goal of building a generalizable sentiment analysis model, we used three different training sets as provided in Table TABREF5 . One of these three datasets (Amazon reviews BIBREF23 , BIBREF24 ) is larger and has product reviews from several different categories including book reviews, electronics products reviews, and application reviews. The other two datasets are to make the model more specialized in the domain. In this paper we focus on restaurant reviews as our domain and use Yelp restaurant reviews dataset extracted from Yelp Dataset Challenge BIBREF25 and restaurant reviews dataset as part of a Kaggle competition BIBREF26 .
> 
> For evaluation of the multilingual approach, we use four languages. These datasets are part of SemEval-2016 Challenge Task 5 BIBREF27 , BIBREF28 . Table TABREF7 shows the number of observations in each test corpus.

### Relevance

Label: 

## Record 0499

Paper: Multilingual Sentiment Analysis: An RNN-Based Framework for Limited Data

### Question

> what dataset was used for training?

### Passage

> In order to eliminate the need to find data and build separate models for each language, we propose a multilingual approach where a single model is built in the language where the largest resources are available. In this paper we focus on English as there are several sentiment analysis datasets in English. To make the English sentiment analysis model as generalizable as possible, we first start by training with a large dataset that has product reviews for different categories. Then, using the trained weights from the larger generic dataset, we make the model more specialized for a specific domain. We further train the model with domain-specific English reviews and use this trained model to score reviews that share the same domain from different languages. To be able to employ the trained model, test sets are first translated to English via machine translation and then inference takes place. Figure FIGREF1 shows our multilingual sentiment analysis approach. It is important to note that this approach does not utilize any resource in any of the languages of the test sets (e.g., word embeddings, lexicons, training set).
> 
> Deep learning approaches have been successful in many applications ranging from computer vision to natural language processing BIBREF20 . Recurrent neural network (RNN) including Long Short Term Memory (LSTM) and Gated Recurrent Units (GRU) are subsets of deep learning algorithms where the dependencies between tokens can be used by the model. These models can also be used with variable length input vectors which makes them suitable for text input. LSTM and GRU models allow operations of sequences of vectors over time and have the capability to `remember' previous information BIBREF20 . RNN have been found useful for several natural language processing tasks including language modeling, text classification, machine translation. RNN can also utilize pre-trained word embeddings (numeric vector representations of words trained on unlabeled data) without requiring hand-crafted features. Therefore in this paper, we employ an RNN architecture that takes text and pre-trained word embeddings as inputs and generates a classification result. Word embeddings represent words as numeric vectors and capture semantic information. They are trained in an unsupervised fashion making it useful for our task.
> 
> The sentiment analysis model that is

### Relevance

Label: 

## Record 0500

Paper: Multilingual Sentiment Analysis: An RNN-Based Framework for Limited Data

### Question

> what dataset was used for training?

### Passage

> With the steady growth in the commercial websites and social media venues, the access to users' reviews have become easier. As the amount of data that can be mined for opinion increased, commercial companies' interests for sentiment analysis increased as well. Sentiment analysis is an important part of understanding user behavior and opinions on products, places, or services.
> 
> Sentiment analysis has long been studied by the research community, leading to several sentiment-related resources such as sentiment dictionaries that can be used as features for machine learning models BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 . These resources help increase sentiment analysis accuracies; however, they are highly dependent on language and require researchers to build such resources for every language to process.
> 
> Feature engineering is a large part of the model building phase for most sentiment analysis and emotion detection models BIBREF4 . Determining the correct set of features is a task that requires thorough investigation. Furthermore, these features are mostly language and dataset dependent making it even further challenging to build models for different languages. For example, the sentiment and emotion lexicons, as well as pre-trained word embeddings are not completely transferable to other languages which replicates the efforts for every language that users would like to build sentiment classification models on. For languages and tasks where the data is limited, extracting these features, building language models, training word embeddings, and creating lexicons are big challenges. In addition to the feature engineering effort, the machine learning models' parameters also need to be tuned separately for each language to get the optimal results.
> 
> In this paper, we take a different approach. We build a reusable sentiment analysis model that does not utilize any lexicons. Our goal is to evaluate how well a generic model can be used to mine opinion in different languages where data is more limited than the language where the generic model is trained on. To that end, we build a training set that contains reviews from different domains in English (e.g., movie reviews, product reviews) and train a recurrent neural network (RNN) model to predict polarity of those reviews. Then focusing on a domain, we make the model specialized in that domain

### Relevance

Label: 
