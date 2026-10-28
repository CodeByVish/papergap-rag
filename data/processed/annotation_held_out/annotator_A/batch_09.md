# Passage relevance annotation

Annotator: 

Judge whether the passage provides information that helps answer the question, including useful partial evidence. Topic overlap alone is not sufficient. Judge only the supplied question and passage.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Do not change record numbers, questions or passages. Work independently without consulting another annotator or reference answers.

## Record 0801

Paper: Question Answering based Clinical Text Structuring Using Pre-trained Language Model

### Question

> Is all text in this dataset a question, or are there unrelated sentences in between questions?

### Passage

> Our dataset is annotated based on Chinese pathology reports provided by the Department of Gastrointestinal Surgery, Ruijin Hospital. It contains 17,833 sentences, 826,987 characters and 2,714 question-answer pairs. All question-answer pairs are annotated and reviewed by four clinicians with three types of questions, namely tumor size, proximal resection margin and distal resection margin. These annotated instances have been partitioned into 1,899 training instances (12,412 sentences) and 815 test instances (5,421 sentences). Each instance has one or several sentences. Detailed statistics of different types of entities are listed in Table TABREF20.
> 
> In the following experiments, two widely-used performance measures (i.e., EM-score BIBREF34 and (macro-averaged) F$_1$-score BIBREF35) are used to evaluate the methods. The Exact Match (EM-score) metric measures the percentage of predictions that match any one of the ground truth answers exactly. The F$_1$-score metric is a looser metric measures the average overlap between the prediction and ground truth answer.

### Relevance

Label: 

## Record 0802

Paper: Question Answering based Clinical Text Structuring Using Pre-trained Language Model

### Question

> Is all text in this dataset a question, or are there unrelated sentences in between questions?

### Passage

> a great benefit for specific task. Meanwhile, the model performance on other tasks which are not trained in the final stage was also improved from around 0 to 60 or 70 percent. This proves that there is commonality between different tasks and our proposed QA-CTS task make this learnable. In conclusion, to achieve the best performance for a specific dataset, pre-training the model in multiple datasets and then fine tuning the model on the specific dataset is the best way.

### Relevance

Label: 

## Record 0803

Paper: Question Answering based Clinical Text Structuring Using Pre-trained Language Model

### Question

> Is all text in this dataset a question, or are there unrelated sentences in between questions?

### Passage

> In this paper, we present a question answering based clinical text structuring (QA-CTS) task, which unifies different clinical text structuring tasks and utilize different datasets. A novel model is also proposed to integrate named entity information into a pre-trained language model and adapt it to QA-CTS task. Initially, sequential results of named entity recognition on both paragraph and query texts are integrated together. Contextualized representation on both paragraph and query texts are transformed by a pre-trained language model. Then, the integrated named entity information and contextualized representation are integrated together and fed into a feed forward network for final prediction. Experimental results on real-world dataset demonstrate that our proposed model competes favorably with strong baseline models in all three specific tasks. The shared task and shared model introduced by QA-CTS task has also been proved to be useful for improving the performance on most of the task-specific datasets. In conclusion, the best way to achieve the best performance for a specific dataset is to pre-train the model in multiple datasets and then fine tune it on the specific dataset.

### Relevance

Label: 

## Record 0804

Paper: Question Answering based Clinical Text Structuring Using Pre-trained Language Model

### Question

> Is all text in this dataset a question, or are there unrelated sentences in between questions?

### Passage

> Recently, some works focused on pre-trained language representation models to capture language information from text and then utilizing the information to improve the performance of specific natural language processing tasks BIBREF24, BIBREF25, BIBREF26, BIBREF27 which makes language model a shared model to all natural language processing tasks. Radford et al. BIBREF24 proposed a framework for fine-tuning pre-trained language model. Peters et al. BIBREF25 proposed ELMo which concatenates forward and backward language models in a shallow manner. Devlin et al. BIBREF26 used bidirectional Transformers to model deep interactions between the two directions. Yang et al. BIBREF27 replaced the fixed forward or backward factorization order with all possible permutations of the factorization order and avoided using the [MASK] tag which causes pretrain-finetune discrepancy that BERT is subject to.
> 
> The main motivation of introducing pre-trained language model is to solve the shortage of labeled data and polysemy problem. Although polysemy problem is not a common phenomenon in biomedical domain, shortage of labeled data is always a non-trivial problem. Lee et al. BIBREF28 applied BERT on large-scale biomedical unannotated data and achieved improvement on biomedical named entity recognition, relation extraction and question answering. Kim et al. BIBREF29 adapted BioBERT into multi-type named entity recognition and discovered new entities. Both of them demonstrates the usefulness of introducing pre-trained language model into biomedical domain.

### Relevance

Label: 

## Record 0805

Paper: Question Answering based Clinical Text Structuring Using Pre-trained Language Model

### Question

> Is all text in this dataset a question, or are there unrelated sentences in between questions?

### Passage

> To investigate how shared task and shared model can benefit, we split our dataset by query types, train our proposed model with different datasets and demonstrate their performance on different datasets. Firstly, we investigate the performance on model without two-stage training and named entity information.
> 
> As indicated in Table TABREF30, The model trained by mixed data outperforms 2 of the 3 original tasks in EM-score with 81.55% for proximal resection margin and 86.85% for distal resection margin. The performance on tumor size declined by 1.57% score in EM-score and 3.14% score in F$_1$-score but they were still above 90%. 0.69% and 0.37% score improvement in EM-score was brought by shared model for proximal and distal resection margin prediction. Meanwhile F$_1$-score for those two tasks declined 3.11% and 0.77% score.
> 
> Then we investigate the performance on model with two-stage training and named entity information. In this experiment, pre-training process only use the specific dataset not the mixed data. From Table TABREF31 we can observe that the performance on proximal and distal resection margin achieved the best performance on both EM-score and F$_1$-score. Compared with Table TABREF30, the best performance on proximal resection margin improved by 6.9% in EM-score and 7.94% in F$_1$-score. Meanwhile, the best performance on distal resection margin improved by 5.56% in EM-score and 6.32% in F$_1$-score. Other performances also usually improved a lot. This proves the usefulness of two-stage training and named entity information as well.
> 
> Lastly, we fine tune the model for each task with a pre-trained parameter. Table TABREF32 summarizes the result. (Add some explanations for the Table TABREF32). Comparing Table TABREF32 with Table TABREF31, using mixed-data pre-trained parameters can significantly improve the model performance than task-specific data trained model. Except tumor size, the result was improved by 0.52% score in EM-score, 1.39% score in F$_1$-score for proximal resection margin and 2.6% score in EM-score, 2.96% score in F$_1$-score for distal resection margin. This proves mixed-data pre-trained parameters can lead to a great benefit for specific task. Meanwhile, the model performance on other tasks which are not trained in the final stage was also improved from around 0 to 60 or 70 percent. This proves that there is commonality between different

### Relevance

Label: 

## Record 0806

Paper: Creative GANs for generating poems, lyrics, and metaphors

### Question

> Which datasets are used?

### Passage

> Language models can be optimized to recognize syntax and semantics with great accuracy BIBREF0. However, the output generated can be repetitive and generic leading to monotonous or uninteresting responses (e.g “I don't know”) regardless of the input BIBREF1. While application of attention BIBREF2, BIBREF3 and advanced decoding mechanisms like beam search and variation sampling BIBREF4 have shown improvements, it does not solve the underlying problem. In creative text generation, the objective is not strongly bound to the ground truth—instead the objective is to generate diverse, unique or original samples. We attempt to do this through a discriminator which can give feedback to the generative model through a cost function that encourages sampling of creative tokens. The contributions of this paper are in the usage of a GAN framework to generate creative pieces of writing. Our experiments suggest that generative text models, while very good at encapsulating semantic, syntactic and domain information, perform better with external feedback from a discriminator for fine-tuning objectiveless decoding tasks like that of creative text. We show this by evaluating our model on three very different creative datasets containing poetry, metaphors and lyrics.
> 
> Previous work on handling the shortcomings of MLE include length-normalizing sentence probability BIBREF5, future cost estimation BIBREF6, diversity-boosting objective function BIBREF7, BIBREF1 or penalizing repeating tokens BIBREF8. When it comes to poetry generation using generative text models, Zhang and Lapata BIBREF9, Yi et al. BIBREF10 and Wang et al. BIBREF11 use language modeling to generate Chinese poems. However, none of these methods provide feedback on the quality of the generated sample and hence, do not address the qualitative objective required for creative decoding. For the task of text generation, MaskGAN BIBREF12 uses a Reinforcement Learning signal from the discriminator, FMD-GAN BIBREF13 uses an optimal transport mechanism as an objective function. GumbelGAN BIBREF14 uses Gumbel-Softmax distribution that replaces the non-differentiable sample from a categorical distribution with a differentiable sample to propagate stronger gradients. Li et al. BIBREF1 use a discriminator for a diversity promoting objective. Yu et al. BIBREF15 use SeqGAN to generate poetry and comment on the performance of SeqGAN over MLE in human evaluations, encouraging our study of GANs for creative text generation. However, these studies do

### Relevance

Label: 

## Record 0807

Paper: Creative GANs for generating poems, lyrics, and metaphors

### Question

> Which datasets are used?

### Passage

> In this section, we report our results on computational metrics, hyperparameters and training configurations for our models. Table TABREF4 shows the results of the perplexity score evaluation of the evaluated models, Table TABREF5 shows hyperparameters for each encoding method and Table TABREF6 shows our training parameters. In Table TABREF6, the values for Gutenberg dataset in columns, GumbelGAN and Creative-GAN are empty as we only pretrain our LMs with the Gutenberg dataset

### Relevance

Label: 

## Record 0808

Paper: Creative GANs for generating poems, lyrics, and metaphors

### Question

> Which datasets are used?

### Passage

> Evaluating creative generation tasks is both critical and complex BIBREF26. Along the lines of previous research on evaluating text generation tasks BIBREF26, we report the perplexity scores of our test set on the evaluated models in the Supplementary Section, Table TABREF4 Our model shows improvements over baseline and GumbelGAN. Common computational methods like BLEU BIBREF27 and perplexity are at best a heuristic and not strong indicators of good performance in text generation models BIBREF28. Particularly, since these scores use target sequences as a reference, it has the same pitfalls as relying on MLE. The advantages in this approach lie in the discriminator's ability to influence the generator to explore other possibilities. Sample outputs for our model can be found on our website .

### Relevance

Label: 

## Record 0809

Paper: Creative GANs for generating poems, lyrics, and metaphors

### Question

> Which datasets are used?

### Passage

> a corpus of 14950 metaphor sentences retrieved from a metaphor database website and (3) a corpus of 1500 song lyrics ranging across genres. The mix of linguistic styles within this corpus offers the potential for interesting variation during the generation phase. We use the same pre-processing as in earlier work BIBREF19, BIBREF23. We reserve 10% of our data for test set and another 10% for our validation set.
> 
> We first pre-train our generator on the Gutenberg dataset BIBREF24 for 20 epochs and then fine-tune BIBREF19 them to our target datasets with a language modeling objective. The discriminator's encoder is initialized to the same weights as our fine-tuned language model. Once we have our fine-tuned encoders for each target dataset, we train in an adversarial manner. The discriminator objective here is to score the quality of the creative text. The discriminator is trained for 3 iterations for every iteration of the generator, a practice seen in previous work BIBREF25. Creative-GAN relies on using the reward from the discriminator BIBREF12, BIBREF15 for backpropagation. We follow a similar training procedure for GumbelGAN. Outputs are generated through sampling over a multinomial distribution for all methods, instead of $argmax$ on the log-likelihood probabilities, as sampling has shown to produce better output quality BIBREF4. Please refer to Supplementary Section Table TABREF6 for training parameters of each dataset and Table TABREF5 for hyperparameters of each encoder. We pick these values after experimentation with our validation set. Training and output generation code can be found online.

### Relevance

Label: 

## Record 0810

Paper: Creative GANs for generating poems, lyrics, and metaphors

### Question

> Which datasets are used?

### Passage

> Using GANs, we can train generative models in a two-player game setting between a discriminator and a generator, where the discriminator (a binary classifier) learns to distinguish between real and fake data samples and the generator tries to fool the discriminator by generating authentic and high quality output BIBREF16. GANs have shown to be successful in image generation tasks BIBREF17 and recently, some progress has been observed in text generation BIBREF13, BIBREF12, BIBREF15. Our generator is a language model trained using backpropagation through time BIBREF18. During the pre-training phase we optimize for MLE and during the GAN training phase, we optimize on the creativity reward from the discriminator. The discriminator's encoder has the same architecture as the generator encoder module with the addition of a pooled decoder layer. The decoder contains 3 $[Dense Batch Normalization,ReLU]$ blocks and an addtional $Sigmoid$ layer. The discriminator decoder takes the hidden state at the last time step of a sequence concatenated with both the max-pooled and mean-pooled representation of the hidden states BIBREF19 and outputs a number in the range $[0,1]$. The difficulty of using GANs in text generation comes from the discrete nature of text, making the model non-differentiable hence, we update parameters for the generator model with policy gradients as described in Yu BIBREF15.
> 
> We utilize AWD-LSTM BIBREF20 and TransformerXL BIBREF21 based language models. For model hyperparameters please to refer to Supplementary Section Table TABREF5. We use Adam optimizer BIBREF22 with $\beta 1= 0.7$ and $\beta 2= 0.8$ similar to BIBREF19 and use a batch size of 50. Other practices for LM training were the same as BIBREF21 and BIBREF20 for Transformer-XL and AWD-LSTM respectively. We refer to our proposed GAN as Creative-GAN and compare it to a baseline (a language model equivalent to our pre-trained generator) and a GumbelGAN model BIBREF14 across all proposed datasets. We use three creative English datasets with distinct linguistic characteristics: (1) A corpus of 740 classical and contemporary English poems, (2) a corpus of 14950 metaphor sentences retrieved from a metaphor database website and (3) a corpus of 1500 song lyrics ranging across genres. The mix of linguistic styles within this corpus offers the potential for interesting variation during the generation

### Relevance

Label: 

## Record 0811

Paper: Automatic Language Identification in Texts: A Survey

### Question

> what are the off-the-shelf systems discussed in the paper?

### Passage

> any off-the-shelf system.
> 
> whatthelang is a recent language identifier written in Python, which utilizes the FastText NN-based text classification algorithm. It supports 176 languages.
> 
> implements an off-the-shelf classifier trained using Wikipedia data, covering 122 languages. Although not described as such, the actual classification algorithm used is a linear model, and is thus closely related to both NB and a cosine-based vector space model.
> 
> In addition to the above-mentioned general-purpose language identifiers, there have also been efforts to produce pre-trained language identifiers targeted specifically at Twitter messages. is a Twitter-specific tool with built-in models for 19 languages. It uses a document representation based on tries BIBREF401 . The algorithm is a LR classifier using all possible substrings of the data, which is important to maximize the available information from the relatively short Twitter messages.
> 
> BIBREF152 provides a comparison of 8 off-the-shelf language identifiers applied without re-training to Twitter messages. One issue they report is that comparing the accuracy of off-the-shelf systems is difficult because of the different subset of languages supported by each system, which may also not fully cover the languages present in the target data. The authors choose to compare accuracy over the full set of languages, arguing that this best reflects the likely use-case of applying an off-the-shelf system to new data. They find that the best individual systems are , and , but that slightly higher accuracy can be attained by a simple voting-based ensemble classifier involving these three systems.
> 
> In addition to this, commercial or other closed-source language identifiers and language identifier services exist, of which we name a few. The Polyglot 3000 and Lextek Language Identifier are standalone language identifiers for Windows. Open Xerox Language Identifier is a web service with available REST and SOAP APIs.

### Relevance

Label: 

## Record 0812

Paper: Automatic Language Identification in Texts: A Survey

### Question

> what are the off-the-shelf systems discussed in the paper?

### Passage

> An “off-the-shelf” language identifier is software that is distributed with pre-trained models for a number of languages, so that a user is not required to provide training data before using the system. Such a setup is highly attractive to many end-users of automatic whose main interest is in utilizing the output of a language identifier rather than implementing and developing the technique. To this end, a number of off-the-shelf language identifiers have been released over time. Many authors have evaluated these off-the-shelf identifiers, including a recent evaluation involving 13 language identifiers which was carried out by BIBREF400 . In this section, we provide a brief summary of open-source or otherwise free systems that are available, as well as the key characteristics of each system. We have also included dates of when the software has been last updated as of October 2018.
> 
> TextCat is the most well-known Perl implementation of the out-of-place method, it lists models for 76 languages in its off-the-shelf configuration; the program is not actively maintained. TextCat is not the only example of an off-the-shelf implementation of the out-of-place method: other implementations include libtextcat with 76 language models, JTCL with 15 languages, and mguesser with 104 models for different language-encoding pairs. The main issue addressed by later implementations is classification speed: TextCat is implemented in Perl and is not optimized for speed, whereas implementations such as libtextcat and mguesser have been specifically written to be fast and efficient. whatlang-rs uses an algorithm based on character trigrams and refers the user to the BIBREF7 article. It comes pre-trained with 83 languages.
> 
> is the language identifier embedded in the Google Chrome web browser. It uses a NB classifier, and script-specific classification strategies. assumes that all the input is in UTF-8, and assigns the responsibility of encoding detection and transcoding to the user. uses Unicode information to determine the script of the input. also implements a number of pre-processing heuristics to help boost performance on its target domain (web pages), such as stripping character sequences like .jpg. The standard implementation supports 83 languages, and an extended model is also available, that supports 160 languages.
> 
> is a Java library that implements a language identifier based on a

### Relevance

Label: 

## Record 0813

Paper: Automatic Language Identification in Texts: A Survey

### Question

> what are the off-the-shelf systems discussed in the paper?

### Passage

> As discussed in standardevaluation, the objective comparison of different methods for is difficult due to the variation in the data that different authors have used to evaluate methods. BIBREF32 emphasize this by demonstrating how the performance of a system can vary according to the data used for evaluation. This implies that comparisons of results reported by different authors may not be meaningful, as a strong result in one paper may not translate into a strong result on the dataset used in a different paper. In other areas of research, authors have proposed standardized corpora to allow for the objective comparison of different methods.
> 
> Some authors have released datasets to accompany their work, to allow for direct replication of their experiments and encourage comparison and standardization. datasets lists a number of datasets that have been released to accompany specific publications. In this list, we only include corpora that were prepared specifically for research, and that include the full text of documents. Corpora of language-labelled Twitter messages that only provide document identifiers are also available, but reproducing the full original corpus is always an issue as the original Twitter messages are deleted or otherwise made unavailable.
> 
> One challenge in standardizing datasets for is that the codes used to label languages are not fully standardized, and a large proportion of labeling systems only cover a minor portion of the languages used in the world today BIBREF381 . BIBREF382 discuss this problem in detail, listing different language code sets, as well as the internal structure exhibited by some of the code sets. Some standards consider certain groups of “languages” as varieties of a single macro-language, whereas others consider them to be discrete languages. An example of this is found in South Slavic languages, where some language code sets refer to Serbo-Croatian, whereas others make distinctions between Bosnian, Serbian and Croatian BIBREF98 . The unclear boundaries between such languages make it difficult to build a reference corpus of documents for each language, or to compare language-specific results across datasets.
> 
> Another challenge in standardizing datasets for is the great deal of variation that can exist between data in the same language. We examine this in greater detail in openissues:encoding, where we

### Relevance

Label: 

## Record 0814

Paper: Automatic Language Identification in Texts: A Survey

### Question

> what are the off-the-shelf systems discussed in the paper?

### Passage

> This article has presented a comprehensive survey on language identification of digitally-encoded text. We have shown that is a rich, complex, and multi-faceted problem that has engaged a wide variety of research communities. accuracy is critical as it is often the first step in longer text processing pipelines, so errors made in will propagate and degrade the performance of later stages. Under controlled conditions, such as limiting the number of languages to a small set of Western European languages and using long, grammatical, and structured text such as government documents as training data, it is possible to achieve near-perfect accuracy. This led many researchers to consider a solved problem, as argued by BIBREF2 . However, becomes much harder when taking into account the peculiarities of real-world data, such as very short documents (e.g. search engine queries), non-linguistic “noise” (e.g. HTML markup), non-standard use of language (e.g. as seen in social media data), and mixed-language documents (e.g. forum posts in multilingual web forums).
> 
> Modern approaches to are generally data-driven and are based on comparing new documents with models of each target language learned from data. The types of models as well as the sources of training data used in the literature are diverse, and work to date has not compared and evaluated these in a systematic manner, making it difficult to draw broader conclusions about what the “best” method for actually is. We have attempted to synthesize results to date to identify a set of “best practices”, but these should be treated as guidelines and should always be considered in the broader context of a target application.
> 
> Existing work on serves to illustrate that the scope and depth of the problem are much greater than they may first appear. In openissues, we discussed open issues in , identifying the key challenges, and outlining opportunities for future research. Far from being a solved problem, aspects of make it an archetypal learning task with subtleties that could be tackled by future work on supervised learning, representation learning, multi-task learning, domain adaptation, multi-label classification and other subfields of machine learning. We hope that this paper can serve as a reference point for future work in the area, both for

### Relevance

Label: 

## Record 0815

Paper: Automatic Language Identification in Texts: A Survey

### Question

> what are the off-the-shelf systems discussed in the paper?

### Passage

> While one line of research into has focused on pushing the boundaries of how many languages are supported simultaneously by a single system BIBREF382 , BIBREF36 , BIBREF153 , another has taken a complementary path and focused on in groups of similar languages. Research in this area typically does not make a distinction between languages, varieties and dialects, because such terminological differences tend to be politically rather than linguistically motivated BIBREF424 , BIBREF382 , BIBREF5 , and from an NLP perspective the challenges faced are very similar.
> 
> for closely-related languages, language varieties, and dialects has been studied for Malay–Indonesian BIBREF332 , Indian languages BIBREF114 , South Slavic languages BIBREF377 , BIBREF98 , BIBREF4 , BIBREF425 , Serbo-Croatian dialects BIBREF426 , English varieties BIBREF278 , BIBREF45 , Dutch–Flemish BIBREF53 , Dutch dialects (including a temporal dimension) BIBREF427 , German Dialects BIBREF428 Mainland–Singaporean–Taiwanese Chinese BIBREF429 , Portuguese varieties BIBREF5 , BIBREF259 , Spanish varieties BIBREF70 , BIBREF147 , French varieties BIBREF430 , BIBREF431 , BIBREF432 , languages of the Iberian Peninsula BIBREF388 , Romanian dialects BIBREF120 , and Arabic dialects BIBREF41 , BIBREF78 , BIBREF433 , BIBREF75 , BIBREF434 , the last of which we discuss in more detail in this section. As to off-the-shelf tools which can identify closely-related languages, BIBREF79 released a system trained to identify 27 languages, including 10 language varieties. Closely-related languages, language varieties, and dialects have also been the focus of a number of shared tasks in recent years as discussed in evaluation:sharedtasks.
> 
> Similar languages are a known problem for existing language identifiers BIBREF332 , BIBREF435 . BIBREF34 identify language pairs from the same language family that also share a common script and the same encoding, as the most difficult to discriminate. BIBREF98 report that achieves only 45% accuracy when trained and tested on 3-way Bosnian/Serbian/Croatian dataset. BIBREF278 found that methods are not competitive with conventional word-based document categorization methods in distinguishing between national varieties of English. BIBREF332 reports that a character trigram model is able to distinguish Malay/Indonesian from English, French, German, and Dutch, but handcrafted rules are needed to distinguish between Malay and Indonesian. One kind of rule is the use of “exclusive words” that are known to occur in

### Relevance

Label: 

## Record 0816

Paper: YEDDA: A Lightweight Collaborative Text Span Annotation Tool

### Question

> how many sentences did they annotate?

### Passage

> There exists a range of text span annotation tools which focus on different aspects of the annotation process. Stanford manual annotation tool is a lightweight tool but does not support result analysis and system recommendation. Knowtator BIBREF6 is a general-task annotation tool which links to a biomedical onto ontology to help identify named entities and relations. It supports quality control during the annotation process by integrating simple inter-annotator evaluation, while it cannot figure out the detailed disagreed labels. WordFreak BIBREF3 adds a system recommendation function and integrates active learning to rank the unannotated sentences based on the recommend confidence, while the post-annotation analysis is not supported.
> 
> Web-based annotation tools have been developed to build operating system independent annotation environments. Gate BIBREF11 includes a web-based with collaborative annotation framework which allows users to work collaboratively by annotating online with shared text storage. Brat BIBREF7 is another web-based tool, which has been widely used in recent years, it provides powerful annotation functions and rich visualization ability, while it does not integrate the result analysis function. Anafora BIBREF4 and Atomic BIBREF5 are also web-based and lightweight annotation tools, while they don't support the automatic annotation and quality analysis either. WebAnno BIBREF12 , BIBREF13 supports both the automatic annotation suggestion and annotation quality monitoring such as inter-annotator agreement measurement, data curation, and progress monitoring. It compares the annotation disagreements only for each sentence and shows the comparison within the interface, while our system can generate a detailed disagreement report in .pdf file through the whole annotated content. Besides, those web-based annotation tools need to build a server through complex configurations and some of the servers cannot be deployed on Windows systems.
> 
> The differences between Yedda and related work are summarised in Table TABREF2 . Here “Self Consistency” represents whether the tool works independently or it relies on pre-installed packages. Compared to these tools, Yedda provides a lighter but more systematic choice with more flexibility, efficiency and less dependence on system environment for text span annotation. Besides, Yedda offers administrator useful toolkits for evaluating the annotation quality and analyze the detailed disagreements within annotators.

### Relevance

Label: 

## Record 0817

Paper: YEDDA: A Lightweight Collaborative Text Span Annotation Tool

### Question

> how many sentences did they annotate?

### Passage

> The client is designed to accelerate the annotation process as much as possible. It supports shortcut annotation to reduce the user operation time. Command line annotation is designed to annotate multi-span in batch. In addition, the client provides system recommendations to lessen the workload of duplicated span annotation.
> 
> Figure FIGREF4 shows the interface of annotator client on an English entity annotation file. The interface consists of 5 parts. The working area in the up-left which shows the texts with different colors (blue: annotated entities, green: recommended entities and orange: selected text span). The entry at the bottom is the command line which accepts annotation command. There are several control buttons in the middle of the interface, which are used to set annotation model. The status area is below the control buttons, it shows the cursor position and the status of recommending model. The right side shows the shortcut map, where shortcut key “a” or “ INLINEFORM0 ” means annotating the text span with “Artificial” type and the same for other shortcut keys. The shortcut map can be configured easily. Details are introduced as follows.
> 
> Yedda provides the function of annotating text span by selecting using mouse and press shortcut key to map the selection into a specific label. It is a common annotation process in many annotation tools BIBREF7 , BIBREF11 . It binds each label with one custom shortcut key, this is shown in the “Shortcuts map Labels” part of Figure FIGREF4 . The annotator needs only two steps to annotate one text span, i.e. “select and press”. The annotated file updates simultaneously with each key pressing process.
> 
> Yedda also support the command line annotation function (see the command entry in the bottom of Figure FIGREF4 ) which can execute multi-span annotation at once. The system will parse the command automatically and convert the command into multi-span annotation instructions and execute in batch. It is quite efficient for the tasks of character-based languages (such as Chinese and Japanese) with high entity density. The command follows a simple rule which is INLINEFORM0 , where ` INLINEFORM1 ' are the length of the entities and ` INLINEFORM2 ' is the corresponding shortcut key. For example, command

### Relevance

Label: 

## Record 0818

Paper: YEDDA: A Lightweight Collaborative Text Span Annotation Tool

### Question

> how many sentences did they annotate?

### Passage

> Natural Language Processing (NLP) systems rely on large-scale training data BIBREF0 for supervised training. However, manual annotation can be time-consuming and expensive. Despite detailed annotation standards and rules, inter-annotator disagreement is inevitable because of human mistakes, language phenomena which are not covered by the annotation rules and the ambiguity of language itself BIBREF1 .
> 
> Existing annotation tools BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 mainly focus on providing a visual interface for user annotation process but rarely consider the post-annotation quality analysis, which is necessary due to the inter-annotator disagreement. In addition to the annotation quality, efficiency is also critical in large-scale annotation task, while being relatively less addressed in existing annotation tools BIBREF6 , BIBREF7 . Besides, many tools BIBREF6 , BIBREF4 require a complex system configuration on either local device or server, which is not friendly to new users.
> 
> To address the challenges above, we propose Yedda , a lightweight and efficient annotation tool for text span annotation. A snapshot is shown in Figure FIGREF4 . Here text span boundaries are selected and assigned with a label, which can be useful for Named Entity Recognition (NER) BIBREF8 , word segmentation BIBREF9 , chunking BIBREF10 ,etc. To keep annotation efficient and accurate, Yedda provides systematic solutions across the whole annotation process, which includes the shortcut annotation, batch annotation with a command line, intelligent recommendation, format exporting and administrator evaluation/analysis.
> 
> Figure FIGREF1 shows the general framework of Yedda. It offers annotators with a simple and efficient Graphical User Interface (GUI) to annotate raw text. For the administrator, it provides two useful toolkits to evaluate multi-annotated text and generate detailed comparison report for annotator pair. Yedda has the advantages of being:
> 
> • INLINEFORM0 Convenient: it is lightweight with an intuitive interface and does not rely on specific operating systems or pre-installed packages.
> 
> • INLINEFORM0 Efficient: it supports both shortcut and command line annotation models to accelerate the annotating process.
> 
> • INLINEFORM0 Intelligent: it offers user with real-time system suggestions to avoid duplicated annotation.
> 
> • INLINEFORM0 Comprehensive: it integrates useful toolkits to give the statistical index of analyzing multi-user annotation results and generate detailed content comparison for annotation pairs.
> 
> This paper is organized as follows: Section 2

### Relevance

Label: 

## Record 0819

Paper: YEDDA: A Lightweight Collaborative Text Span Annotation Tool

### Question

> how many sentences did they annotate?

### Passage

> We have presented a lightweight but systematic annotation tool, Yedda, for annotating the entities in text and analyzing the annotation results efficiently. In order to reduce the workload of annotators, we are going to integrate active learning strategy in our system recommendation part in the future. A supervised sequence labeling model (such as CRF) is trained based on the annotated text, then unannotated sentences with less confidence (predicted by this model) are reordered in the front to ensure annotators only annotate the most confusing sentences.

### Relevance

Label: 

## Record 0820

Paper: YEDDA: A Lightweight Collaborative Text Span Annotation Tool

### Question

> how many sentences did they annotate?

### Passage

> Here we compare the efficiency of our system with four widely used annotation tools. We extract 100 sentences from CoNLL 2003 English NER BIBREF8 training data, with each sentence containing at least 4 entities. Two undergraduate students without any experience on those tools are invited to annotate those sentences. Their average annotation time is shown in Figure FIGREF25 , where “Yedda+R” suggests annotation using Yedda with the help of system recommendation. The inter-annotator agreements for those tools are closed, which around 96.1% F1-score. As we can see from the figure, our Yedda system can greatly reduce the annotation time. With the help of system recommendation, the annotation time can be further reduced. We notice that “Yedda+R” has larger advantage with the increasing numbers of annotated sentences, this is because the system recommendation gives better suggestions when it learns larger annotated sentences. The “Yedda+R” gives 16.47% time reduction in annotating 100 sentences.

### Relevance

Label: 

## Record 0821

Paper: Learning Twitter User Sentiments on Climate Change with Limited Labeled Data

### Question

> What methodology is used to compensate for limited labelled data?

### Passage

> We henceforth refer to a tweet affirming climate change as a “positive" sample (labeled as 1 in the data), and a tweet denying climate change as a “negative" sample (labeled as -1 in the data). All data were downloaded from Twitter in two separate batches using the “twint" scraping tool BIBREF5 to sample historical tweets for several different search terms; queries always included either “climate change" or “global warming", and further included disaster-specific search terms (e.g., “bomb cyclone," “blizzard," “snowstorm," etc.). We refer to the first data batch as “influential" tweets, and the second data batch as “event-related" tweets.
> 
> The first data batch consists of tweets relevant to blizzards, hurricanes, and wildfires, under the constraint that they are tweeted by “influential" tweeters, who we define as individuals certain to have a classifiable sentiment regarding the topic at hand. For example, we assume that any tweet composed by Al Gore regarding climate change is a positive sample, whereas any tweet from conspiracy account @ClimateHiJinx is a negative sample. The assumption we make in ensuing methods (confirmed as reasonable in Section SECREF2 ) is that influential tweeters can be used to label tweets in bulk in the absence of manually-labeled tweets. Here, we enforce binary labels for all tweets composed by each of the 133 influential tweeters that we identified on Twitter (87 of whom accept climate change), yielding a total of 16,360 influential tweets.
> 
> The second data batch consists of event-related tweets for five natural disasters occurring in the U.S. in 2018. These are: the East Coast Bomb Cyclone (Jan. 2 - 6); the Mendocino, California wildfires (Jul. 27 - Sept. 18); Hurricane Florence (Aug. 31 - Sept. 19); Hurricane Michael (Oct. 7 - 16); and the California Camp Fires (Nov. 8 - 25). For each disaster, we scraped tweets starting from two weeks prior to the beginning of the event, and continuing through two weeks after the end of the event. Summary statistics on the downloaded event-specific tweets are provided in Table TABREF1 . Note that the number of tweets occurring prior to the two 2018 sets of California fires are relatively small. This is because the magnitudes of these wildfires were relatively unpredictable, whereas

### Relevance

Label: 

## Record 0822

Paper: Learning Twitter User Sentiments on Climate Change with Limited Labeled Data

### Question

> What methodology is used to compensate for limited labelled data?

### Passage

> post-event.
> 
> There are several caveats in our work: first, tweet sentiment is rarely binary (this work could be extended to a multinomial or continuous model). Second, our results are constrained to Twitter users, who are known to be more negative than the general U.S. population BIBREF9 . Third, we do not take into account the aggregate effects of continued natural disasters over time. Going forward, there is clear demand in discovering whether social networks can indicate environmental metrics in a “nowcasting" fashion. As climate change becomes more extreme, it remains to be seen what degree of predictive power exists in our current model regarding climate change sentiments with regards to natural disasters.

### Relevance

Label: 

## Record 0823

Paper: Learning Twitter User Sentiments on Climate Change with Limited Labeled Data

### Question

> What methodology is used to compensate for limited labelled data?

### Passage

> Our first goal is to train a sentiment analysis model (on training and validation datasets) in order to perform classification inference on event-based tweets. We experimented with different feature extraction methods and classification models. Feature extractions examined include Tokenizer, Unigram, Bigram, 5-char-gram, and td-idf methods. Models include both neural nets (e.g. RNNs, CNNs) and standard machine learning tools (e.g. Naive Bayes with Laplace Smoothing, k-clustering, SVM with linear kernel). Model accuracies are reported in Table FIGREF3 .
> 
> The RNN pre-trained using GloVe word embeddings BIBREF6 achieved the higest test accuracy. We pass tokenized features into the embedding layer, followed by an LSTM BIBREF7 with dropout and ReLU activation, and a dense layer with sigmoid activation. We apply an Adam optimizer on the binary crossentropy loss. Implementing this simple, one-layer LSTM allows us to surpass the other traditional machine learning classification methods. Note the 13-point spread between validation and test accuracies achieved. Ideally, the training, validation, and test datasets have the same underlying distribution of tweet sentiments; the assumption made with our labeling technique is that the influential accounts chosen are representative of all Twitter accounts. Critically, when choosing the influential Twitter users who believe in climate change, we highlighted primarily politicians or news sources (i.e., verifiably affirming or denying climate change); these tweets rarely make spelling errors or use sarcasm. Due to this skew, the model yields a high rate of false negatives. It is likely that we could lessen the gap between validation and test accuracies by finding more “real" Twitter users who are climate change believers, e.g. by using the methodology found in BIBREF4 .

### Relevance

Label: 

## Record 0824

Paper: Learning Twitter User Sentiments on Climate Change with Limited Labeled Data

### Question

> What methodology is used to compensate for limited labelled data?

### Passage

> downloaded event-specific tweets are provided in Table TABREF1 . Note that the number of tweets occurring prior to the two 2018 sets of California fires are relatively small. This is because the magnitudes of these wildfires were relatively unpredictable, whereas blizzards and hurricanes are often forecast weeks in advance alongside public warnings. The first (influential tweet data) and second (event-related tweet data) batches are de-duplicated to be mutually exclusive. In Section SECREF2 , we perform geographic analysis on the event-related tweets from which we can scrape self-reported user city from Twitter user profile header cards; overall this includes 840 pre-event and 5,984 post-event tweets.
> 
> To create a model for predicting sentiments of event-related tweets, we divide the first data batch of influential tweets into training and validation datasets with a 90%/10% split. The training set contains 49.2% positive samples, and the validation set contains 49.0% positive samples. We form our test set by manually labeling a subset of 500 tweets from the the event-related tweets (randomly chosen across all five natural disasters), of which 50.0% are positive samples.

### Relevance

Label: 

## Record 0825

Paper: Learning Twitter User Sentiments on Climate Change with Limited Labeled Data

### Question

> What methodology is used to compensate for limited labelled data?

### Passage

> In Figure FIGREF8 , we see that overall sentiment averages rarely show movement post-event: that is, only Hurricane Florence shows a significant difference in average tweet sentiment pre- and post-event at the 1% level, corresponding to a 0.12 point decrease in positive climate change sentiment. However, controlling for the same group of users tells a different story: both Hurricane Florence and Hurricane Michael have significant tweet sentiment average differences pre- and post-event at the 1% level. Within-cohort, Hurricane Florence sees an increase in positive climate change sentiment by 0.21 points, which is contrary to the overall average change (the latter being likely biased since an influx of climate change deniers are likely to tweet about hurricanes only after the event). Hurricane Michael sees an increase in average tweet sentiment of 0.11 points, which reverses the direction of tweets from mostly negative pre-event to mostly positive post-event. Likely due to similar bias reasons, the Mendocino wildfires in California see a 0.06 point decrease in overall sentiment post-event, but a 0.09 point increase in within-cohort sentiment. Methodologically, we assert that overall averages are not robust results to use in sentiment analyses.
> 
> We now comment on the two events yielding similar results between overall and within-cohort comparisons. Most tweets regarding the Bomb Cyclone have negative sentiment, though sentiment increases by 0.02 and 0.04 points post-event for overall and within-cohort averages, respectively. Meanwhile, the California Camp Fires yield a 0.11 and 0.27 point sentiment decline in overall and within-cohort averages, respectively. This large difference in sentiment change can be attributed to two factors: first, the number of tweets made regarding wildfires prior to the (usually unexpected) event is quite low, so within-cohort users tend to have more polarized climate change beliefs. Second, the root cause of the Camp Fires was quickly linked to PG&E, bolstering claims that climate change had nothing to do with the rapid spread of fire; hence within-cohort users were less vocally positive regarding climate change post-event.
> 
> There are several caveats in our work: first, tweet sentiment is rarely binary (this work could be extended to a multinomial or continuous model). Second, our results are constrained to Twitter users, who are known to be more negative

### Relevance

Label: 

## Record 0826

Paper: Exploring Hate Speech Detection in Multimodal Publications

### Question

> How many tweats does MMHS150k contains, 150000?

### Passage

> are considered as non-hate.
> 
> WZ-LS BIBREF5: A combination of Wassem datasets BIBREF4, BIBREF3 labeled as racism, sexism, neither or both that make a total of $18,624$ tweets.
> 
> Semi-Supervised BIBREF9: Contains $27,330$ general hate speech Twitter tweets crawled in a semi-supervised manner.
> 
> Although often modern social media publications include images, not too many contributions exist that exploit visual information. Zhong et al. BIBREF12 worked on classifying Instagram images as potential cyberbullying targets, exploiting both the image content, the image caption and the comments. However, their visual information processing is limited to the use of features extracted by a pre-trained CNN, the use of which does not achieve any improvement. Hosseinmardi et al. BIBREF13 also address the problem of detecting cyberbullying incidents on Instagram exploiting both textual and image content. But, again, their visual information processing is limited to use the features of a pre-trained CNN, and the improvement when using visual features on cyberbullying classification is only of 0.01%.

### Relevance

Label: 

## Record 0827

Paper: Exploring Hate Speech Detection in Multimodal Publications

### Question

> How many tweats does MMHS150k contains, 150000?

### Passage

> Existing hate speech datasets contain only textual data. Moreover, a reference benchmark does not exists. Most of the published datasets are crawled from Twitter and distributed as tweet IDs but, since Twitter removes reported user accounts, an important amount of their hate tweets is no longer accessible. We create a new manually annotated multimodal hate speech dataset formed by $150,000$ tweets, each one of them containing text and an image. We call the dataset MMHS150K, and made it available online . In this section, we explain the dataset creation steps.

### Relevance

Label: 

## Record 0828

Paper: Exploring Hate Speech Detection in Multimodal Publications

### Question

> How many tweats does MMHS150k contains, 150000?

### Passage

> The objective of this work is to build a hate speech detector that leverages both textual and visual data and detects hate speech publications based on the context given by both data modalities. To study how the multimodal context can boost the performance compared to an unimodal context we evaluate different models: a Feature Concatenation Model (FCM), a Spatial Concatenation Model (SCM) and a Textual Kernels Model (TKM). All of them are CNN+RNN models with three inputs: the tweet image, the tweet text and the text appearing in the image (if any).

### Relevance

Label: 

## Record 0829

Paper: Exploring Hate Speech Detection in Multimodal Publications

### Question

> How many tweats does MMHS150k contains, 150000?

### Passage

> Social Media platforms such as Facebook, Twitter or Reddit have empowered individuals' voices and facilitated freedom of expression. However they have also been a breeding ground for hate speech and other types of online harassment. Hate speech is defined in legal literature as speech (or any form of expression) that expresses (or seeks to promote, or has the capacity to increase) hatred against a person or a group of people because of a characteristic they share, or a group to which they belong BIBREF0. Twitter develops this definition in its hateful conduct policy as violence against or directly attack or threaten other people on the basis of race, ethnicity, national origin, sexual orientation, gender, gender identity, religious affiliation, age, disability, or serious disease.
> 
> In this work we focus on hate speech detection. Due to the inherent complexity of this task, it is important to distinguish hate speech from other types of online harassment. In particular, although it might be offensive to many people, the sole presence of insulting terms does not itself signify or convey hate speech. And, the other way around, hate speech may denigrate or threaten an individual or a group of people without the use of any profanities. People from the african-american community, for example, often use the term nigga online, in everyday language, without malicious intentions to refer to folks within their community, and the word cunt is often used in non hate speech publications and without any sexist purpose. The goal of this work is not to discuss if racial slur, such as nigga, should be pursued. The goal is to distinguish between publications using offensive terms and publications attacking communities, which we call hate speech.
> 
> Modern social media content usually include images and text. Some of these multimodal publications are only hate speech because of the combination of the text with a certain image. That is because, as we have stated, the presence of offensive terms does not itself signify hate speech, and the presence of hate speech is often determined by the context of a publication. Moreover, users authoring hate speech tend to intentionally construct publications where the text is not enough to determine they are hate speech.

### Relevance

Label: 

## Record 0830

Paper: Exploring Hate Speech Detection in Multimodal Publications

### Question

> How many tweats does MMHS150k contains, 150000?

### Passage

> Table TABREF31 shows the F-score, the Area Under the ROC Curve (AUC) and the mean accuracy (ACC) of the proposed models when different inputs are available. $TT$ refers to the tweet text, $IT$ to the image text and $I$ to the image. It also shows results for the LSTM, for the Davison method proposed in BIBREF7 trained with MMHS150K, and for random scores. Fig. FIGREF32 shows the Precision vs Recall plot and the ROC curve (which plots the True Positive Rate vs the False Positive Rate) of the different models.
> 
> First, notice that given the subjectivity of the task and the discrepancies between annotators, getting optimal scores in the evaluation metrics is virtually impossible. However, a system with relatively low metric scores can still be very useful for hate speech detection in a real application: it will fire on publications for which most annotators agree they are hate, which are often the stronger attacks. The proposed LSTM to detect hate speech when only text is available, gets similar results as the method presented in BIBREF7, which we trained with MMHS150K and the same splits. However, more than substantially advancing the state of the art on hate speech detection in textual publications, our key purpose in this work is to introduce and work on its detection on multimodal publications. We use LSTM because it provides a strong representation of the tweet texts.
> 
> The FCM trained only with images gets decent results, considering that in many publications the images might not give any useful information for the task. Fig. FIGREF33 shows some representative examples of the top hate and not hate scored images of this model. Many hate tweets are accompanied by demeaning nudity images, being sexist or homophobic. Other racist tweets are accompanied by images caricaturing black people. Finally, MEMES are also typically used in hate speech publications. The top scored images for not hate are portraits of people belonging to minorities. This is due to the use of slur inside these communities without an offensive intention, such as the word nigga inside the afro-american community or the word dyke inside the lesbian community. These results show that images can be effectively used to discriminate between

### Relevance

Label: 

## Record 0831

Paper: Visualizing and Measuring the Geometry of BERT

### Question

> How were the feature representations evaluated?

### Passage

> Neural networks for language processing have advanced rapidly in recent years. A key breakthrough was the introduction of transformer architectures BIBREF0 . One recent system based on this idea, BERT BIBREF1 , has proven to be extremely flexible: a single pretrained model can be fine-tuned to achieve state-of-the-art performance on a wide variety of NLP applications. This suggests the model is extracting a set of generally useful features from raw text. It is natural to ask, which features are extracted? And how is this information represented internally?
> 
> Similar questions have arisen with other types of neural nets. Investigations of convolutional neural networks BIBREF2 , BIBREF3 have shown how representations change from layer to layer BIBREF4 ; how individual units in a network may have meaning BIBREF5 ; and that “meaningful” directions exist in the space of internal activation BIBREF6 . These explorations have led to a broader understanding of network behavior.
> 
> Analyses on language-processing models (e.g., BIBREF7 , BIBREF8 , BIBREF9 , BIBREF10 , BIBREF11 ) point to the existence of similarly rich internal representations of linguistic structure. Syntactic features seem to be extracted by RNNs (e.g., BIBREF7 , BIBREF9 ) as well as in BERT BIBREF11 , BIBREF12 , BIBREF13 , BIBREF10 . Inspirational work from Hewitt and Manning BIBREF8 found evidence of a geometric representation of entire parse trees in BERT's activation space.
> 
> Our work extends these explorations of the geometry of internal representations. Investigating how BERT represents syntax, we describe evidence that attention matrices contain grammatical representations. We also provide mathematical arguments that may explain the particular form of the parse tree embeddings described in BIBREF8 . Turning to semantics, using visualizations of the activations created by different pieces of text, we show suggestive evidence that BERT distinguishes word senses at a very fine level. Moreover, much of this semantic information appears to be encoded in a relatively low-dimensional subspace.

### Relevance

Label: 

## Record 0832

Paper: Visualizing and Measuring the Geometry of BERT

### Question

> How were the feature representations evaluated?

### Passage

> We have presented a series of experiments that shed light on BERT's internal representations of linguistic information. We have found evidence of syntactic representation in attention matrices, with certain directions in space representing particular dependency relations. We have also provided a mathematical justification for the squared-distance tree embedding found by Hewitt and Manning.
> 
> Meanwhile, we have shown that just as there are specific syntactic subspaces, there is evidence for subspaces that represent semantic information. We also have shown how mistakes in word sense disambiguation may correspond to changes in internal geometric representation of word meaning. Our experiments also suggest an answer to the question of how all these different representations fit together. We conjecture that the internal geometry of BERT may be broken into multiple linear subspaces, with separate spaces for different syntactic and semantic information.
> 
> Investigating this kind of decomposition is a natural direction for future research. What other meaningful subspaces exist? After all, there are many types of linguistic information that we have not looked for.
> 
> A second important avenue of exploration is what the internal geometry can tell us about the specifics of the transformer architecture. Can an understanding of the geometry of internal representations help us find areas for improvement, or refine BERT's architecture?
> 
> Acknowledgments: We would like to thank David Belanger, Tolga Bolukbasi, Jasper Snoek, and Ian Tenney for helpful feedback and discussions.

### Relevance

Label: 

## Record 0833

Paper: Visualizing and Measuring the Geometry of BERT

### Question

> How were the feature representations evaluated?

### Passage

> Penn Treebank with associated dependency parse trees (see Section "Geometry of word senses" ). We then extracted the token embeddings produced by BERT-large in layer 16 (following BIBREF8 ), transformed by the Hewitt and Manning’s “structural probe” matrix $B$ , yielding a set of points in 1024-dimensional space. We used PCA to project to two dimensions. (Other dimensionality-reduction methods, such as t-SNE and UMAP BIBREF24 , were harder to interpret.)
> 
> To visualize the tree structure, we connected pairs of points representing words with a dependency relation. The color of each edge indicates the deviation from true tree distance. We also connected, with dotted line, pairs of words without a dependency relation but whose positions (before PCA) were far closer than expected. The resulting image lets us see both the overall shape of the tree embedding, and fine-grained information on deviation from a true power-2 embedding.
> 
> Two example visualizations are shown in Figure 2 , next to traditional diagrams of their underlying parse trees. These are typical cases, illustrating some common patterns; for instance, prepositions are embedded unexpectedly close to words they relate to. (Figure 7 shows additional examples.)
> 
> A natural question is whether the difference between these projected trees and the canonical ones is merely noise, or a more interesting pattern. By looking at the average embedding distances of each dependency relation (see Figure 3 ) , we can see that they vary widely from around 1.2 ( $compound:prt$ , $advcl$ ) to 2.5 ( $mwe$ , $parataxis$ , $auxpass$ ). Such systematic differences suggest that BERT's syntactic representation has an additional quantitative aspect beyond traditional dependency grammar.

### Relevance

Label: 

## Record 0834

Paper: Visualizing and Measuring the Geometry of BERT

### Question

> How were the feature representations evaluated?

### Passage

> As in BIBREF8 , we are interested in finding representations of dependency grammar relations BIBREF17 . While BIBREF8 analyzed context embeddings, another natural place to look for encodings is in the attention matrices. After all, attention matrices are explicitly built on the relations between pairs of words.
> 
> To formalize what it means for attention matrices to encode linguistic features, we use an attention probe, an analog of edge probing BIBREF11 . An attention probe is a task for a pair of tokens, $(token_i, token_j)$ where the input is a model-wide attention vector formed by concatenating the entries $a_{ij}$ in every attention matrix from every attention head in every layer. The goal is to classify a given relation between the two tokens. If a linear model achieves reliable accuracy, it seems reasonable to say that the model-wide attention vector encodes that relation. We apply attention probes to the task of identifying the existence and type of dependency relation between two words.
> 
> The data for our first experiment is a corpus of parsed sentences from the Penn Treebank BIBREF18 . This dataset has the constituency grammar for the sentences, which was translated to a dependency grammar using the PyStanfordDependencies library BIBREF19 . The entirety of the Penn Treebank consists of 3.1 million dependency relations; we filtered this by using only examples of the 30 dependency relations with more than 5,000 examples in the data set. We then ran each sentence through BERT-base, and obtained the model-wide attention vector (see Figure 1 ) between every pair of tokens in the sentence, excluding the $[SEP]$ and $[CLS]$ tokens. This and subsequent experiments were conducted using PyTorch on MacBook machines.
> 
> With these labeled embeddings, we trained two L2 regularized linear classifiers via stochastic gradient descent, using BIBREF20 . The first of these probes was a simple linear binary classifier to predict whether or not an attention vector corresponds to the existence of a dependency relation between two tokens. This was trained with a balanced class split, and 30% train/test split. The second probe was a multiclass classifier to predict which type of dependency relation exists between two tokens, given the dependency relation’s existence. This probe was trained with distributions outlined

### Relevance

Label: 

## Record 0835

Paper: Visualizing and Measuring the Geometry of BERT

### Question

> How were the feature representations evaluated?

### Passage

> Our first experiment is an exploratory visualization of how word sense affects context embeddings. For data on different word senses, we collected all sentences used in the introductions to English-language Wikipedia articles. (Text outside of introductions was frequently fragmentary.) We created an interactive application, which we plan to make public. A user enters a word, and the system retrieves 1,000 sentences containing that word. It sends these sentences to BERT-base as input, and for each one it retrieves the context embedding for the word from a layer of the user's choosing.
> 
> The system visualizes these 1,000 context embeddings using UMAP BIBREF24 , generally showing clear clusters relating to word senses. Different senses of a word are typically spatially separated, and within the clusters there is often further structure related to fine shades of meaning. In Figure 4 , for example, we not only see crisp, well-separated clusters for three meanings of the word “die,” but within one of these clusters there is a kind of quantitative scale, related to the number of people dying.
> 
> See Appendix "Additional word sense visualizations" for further examples. The apparent detail in the clusters we visualized raises two immediate questions. First, is it possible to find quantitative corroboration that word senses are well-represented? Second, how can we resolve a seeming contradiction: in the previous section, we saw how position represented syntax; yet here we see position representing semantics.

### Relevance

Label: 

## Record 0836

Paper: A Context-Aware Approach for Detecting Check-Worthy Claims in Political Debates

### Question

> What models are trained?

### Passage

> In the experiments above, we have been trying to predict whether a sentence is check-worthy in general, i.e., with respect to at least one source; this is how we trained and this is how we evaluated our models. Here, we want to evaluate how well our models perform at finding sentences that contain claims that would be judged as worthy for fact-checking with respect to each of the individual sources. The purpose is to see to what extent we can make our system potentially useful for a particular medium.
> 
> Another interesting question is whether we should use our generic system or we should retrain with respect to the target medium. Table TABREF31 shows the results for such a comparison, and it further compares to CB Platform. We can see that for all nine media, our model outperforms CB Platform in terms of MAP and P@50; this is also true for the other measures in most cases.
> 
> Moreover, we can see that training on all media is generally preferable to training on the target medium only, which shows that they do follow some common principles for selecting what is check-worthy; this means that a general system could serve journalists in all nine, and possibly other, media. Overall, our model works best on PolitiFact, which is a reputable source for fact checking, as this is their primary expertise. We also do well on NPR, NYT, Guardian, and FactCheck, which is quite encouraging.

### Relevance

Label: 

## Record 0837

Paper: A Context-Aware Approach for Detecting Check-Worthy Claims in Political Debates

### Question

> What models are trained?

### Passage

> We experimented with two learning algorithms. The first one is an SVM classifier with an RBF kernel. The second one is a deep feed-forward neural network (FNN) with two hidden layers (with 200 and 50 neurons, respectively) and a softmax output unit for the binary classification. We used ReLU BIBREF25 as the activation function and we trained the network with Stochastic Gradient Descent BIBREF26.
> 
> The models were trained to classify sentences as positive if one or more media had fact-checked a claim inside the target sentence, and negative otherwise. We then used the classifier scores to rank the sentences with respect to check-worthiness.
> 
> We tuned the parameters and we evaluated the performance using 4-fold cross-validation, using each of the four debates in turn for testing while training on the remaining three ones.
> 
> For evaluation, we used ranking measures such as Precision at $k$ ($P@k$) and Mean Average Precision (MAP). As Table TABREF7 shows, most media rarely check more than 50 claims per debate. NPR and PolitiFact are notable exceptions, the former going up to 99; yet, on average there are two claims per sentence, which means that there is no need to fact-check more than 50 sentences even for them. Thus, we report $P@k$ for $k \in \lbrace 5, 10, 20, 50\rbrace $.
> 
> MAP is the mean of the Average Precision across the four debates. The average precision for a debate is computed as follows:
> 
> where $n$ is the number of sentences to rank in the debate, $P(k)$ is the precision at $k$ and $rel(k)=1$ if the utterance at position $k$ is check-worthy, and it is 0 otherwise.
> 
> We also measure the recall at the $R$-th position of returned sentences for each debate. $R$ is the number of relevant documents for that debate and the metric is known as $R$-Precision ($R$-Pr).

### Relevance

Label: 

## Record 0838

Paper: A Context-Aware Approach for Detecting Check-Worthy Claims in Political Debates

### Question

> What models are trained?

### Passage

> Table TABREF21 shows the performance of our models when using all features described in Section SECREF4: see the SVM$_{All}$ and the FNN$_{All}$ rows. In order to put the numbers in perspective, we also show the results for five increasingly competitive baselines.
> 
> First, there is a random baseline, followed by an SVM classifier based on a bag-of-words representation with TF.IDF weights learned on the training data. Then come three versions of the ClaimBuster system: CB-Platform uses scores from the online demo, which we accessed on December 20, 2016, and SVM$_{CBfeat}$ and FNN$_{CBfeat}$ are our re-implementations, trained on our dataset.
> 
> We can see that all systems perform well above the random baseline. The three versions of ClaimBuster also outperform the TF.IDF baseline on most measures. Moreover, our reimplementation of ClaimBuster performs better than the online platform in terms of MAP. This is expected as their system is trained on a different dataset and it may suffer from testing on slightly out-of-domain data. At the same time, this is reassuring for our implementation of the features, and allows for a more realistic comparison to the ClaimBuster system.
> 
> More importantly, both the SVM and the FNN versions of our system consistently outperform all three versions of ClaimBuster on all measures. This means that the extra information coded in our model, mainly more linguistic, structural, and contextual features, has an important contribution to the overall performance.
> 
> We can further see that the neural network model, FNN$_{All}$, clearly outperforms the SVM model: consistently on all measures. As an example, with the precision values achieved by FNN$_{All}$, the system would rank on average 4 positive examples in the list of its top-5 choices, and also 14-15 in the top-20 list. Considering the recall at the first $R$ sentences, we will be able to encounter 43% of the total number of check-worthy sentences. This is quite remarkable given the difficulty of the task.

### Relevance

Label: 

## Record 0839

Paper: A Context-Aware Approach for Detecting Check-Worthy Claims in Political Debates

### Question

> What models are trained?

### Passage

> The feature groups in this subsection contain a mixture of sentence- and of contextual-level features. For example, if we use a discourse parser to parse the target sentence only, any features we extract from the parse would be sentence-level. However, if we parse an entire segment, we would also have contextual features.
> 
> Topics (300+3 S+C features): Some topics are more likely to be associated with check-worthy claims, and thus we have features modeling the topics in the target sentence as well as in the surrounding context. We trained a Latent Dirichlet Allocation (LDA) topic model BIBREF22 on all political speeches and debates in The American Presidency Project using all US presidential debates in the 2007–2016 period. We had 300 topics, and we used the distribution over the topics as a representation for the target sentence. We further modeled the context using cosines with such representations for the previous, the current, and the next segment.
> 
> Embeddings (300+3 S+C features): We also modeled semantics using word embeddings. We used the pre-trained 300-dimensional Google News word embeddings by BIBREF23 to compute an average embedding vector for the target sentence, and we used the 300 coordinates of that vector. We also modeled the context as the cosine between that vector and the vectors for three segments: the previous, the current, and the following one.
> 
> Discourse (2+18 S+C features): We saw above that contradiction can signal the presence of check-worthy claims, and contradiction can be expressed by a discourse relation such as Contrast. As other discourse relations such as Background, Cause, and Elaboration can also be useful, we used a discourse parser BIBREF24 to parse the entire segment, and we focused on the relationship between the target sentence and the other sentences in its segment; this gave rise to 18 contextual indicator features. We further analyzed the internal structure of the target sentence —how many nuclei and how many satellites it contains—, which gave rise to two sentence-level features.
> 
> Contradictions (1+4 S+C features): Many claims selected for fact-checking contain contradictions to what has been said earlier, as in the example below (from the 3rd presidential debate):
> 
> We model this by counting the negations in the target sentence as found in

### Relevance

Label: 

## Record 0840

Paper: A Context-Aware Approach for Detecting Check-Worthy Claims in Political Debates

### Question

> What models are trained?

### Passage

> The previous work that is most relevant to our work here is that of BIBREF9, who developed the ClaimBuster system, which assigns each sentence in a document a score, i.e., a number between 0 and 1 showing how worthy it is of fact-checking. The system is trained on their own dataset of about eight thousand debate sentences (1,673 of them check-worthy), annotated by students, university professors, and journalists. Unfortunately, this dataset is not publicly available and it contains sentences without context as about 60% of the original sentences had to be thrown away due to lack of agreement.
> 
> In contrast, we develop a new publicly-available dataset, based on manual annotations of political debates by nine highly-reputed fact-checking sources, where sentences are annotated in the context of the entire debate. This allows us to explore a novel approach, which focuses on the context.
> 
> Note also that the ClaimBuster dataset is annotated following guidelines from BIBREF9 rather than a real fact-checking website; yet, it was evaluated against CNN and PolitiFact BIBREF10. In contrast, we train and evaluate directly on annotations from fact-checking websites, and thus we learn to fit them better.
> 
> Beyond the document context, it has been proposed to mine check-worthy claims on the Web. For example, BIBREF11 searched for linguistic cues of disagreement between the author of a statement and what is believed, e.g., “falsely claimed that X”. The claims matching the patterns go through a statistical classifier, which marks the text of the claim. This procedure can be used to acquire a dataset of disputed claims from the Web.
> 
> Given a set of disputed claims, BIBREF12 approached the task as locating new claims on the Web that entail the ones that have already been collected. Thus, the task can be conformed as recognizing textual entailment, which is analyzed in detail in BIBREF13.
> 
> Finally, BIBREF14 argued that the top terms in claim vs. non-claim sentences are highly overlapping, which is a problem for bag-of-words approaches. Thus, they used a Convolutional Neural Network, where each word is represented by its embedding and each named entity is replaced by its tag, e.g., person, organization, location.

### Relevance

Label: 

## Record 0841

Paper: Can neural networks understand monotonicity reasoning?

### Question

> What NLI models do they analyze?

### Passage

> Natural language inference (NLI), also known as recognizing textual entailment (RTE), has been proposed as a benchmark task for natural language understanding. Given a premise $P$ and a hypothesis $H$ , the task is to determine whether the premise semantically entails the hypothesis BIBREF0 . A number of recent works attempt to test and analyze what type of inferences an NLI model may be performing, focusing on various types of lexical inferences BIBREF1 , BIBREF2 , BIBREF3 and logical inferences BIBREF4 , BIBREF5 .
> 
> Concerning logical inferences, monotonicity reasoning BIBREF6 , BIBREF7 , which is a type of reasoning based on word replacement, requires the ability to capture the interaction between lexical and syntactic structures. Consider examples in ( "Introduction" ) and ( "Introduction" ).
> 
> All [ workers $\leavevmode {\color {blue!80!black}\downarrow }$ ] [joined for a French dinner $\leavevmode {\color {red!80!black}\uparrow }$ ] All workers joined for a dinner All new workers joined for a French dinner Not all [new workers $\leavevmode {\color {red!80!black}\uparrow }$ ] joined for a dinner Not all workers joined for a dinner
> 
> A context is upward entailing (shown by [... $\leavevmode {\color {red!80!black}\uparrow }$ ]) that allows an inference from ( "Introduction" ) to ( "Introduction" ), where French dinner is replaced by a more general concept dinner. On the other hand, a downward entailing context (shown by [... $\leavevmode {\color {blue!80!black}\downarrow }$ ]) allows an inference from ( "Introduction" ) to ( "Introduction" ), where workers is replaced by a more specific concept new workers. Interestingly, the direction of monotonicity can be reversed again by embedding yet another downward entailing context (e.g., not in ( "Introduction" )), as witness the fact that ( "Introduction" ) entails ( "Introduction" ). To properly handle both directions of monotonicity, NLI models must detect monotonicity operators (e.g., all, not) and their arguments from the syntactic structure.
> 
> For previous datasets containing monotonicity inference problems, FraCaS BIBREF8 and the GLUE diagnostic dataset BIBREF9 are manually-curated datasets for testing a wide range of linguistic phenomena. However, monotonicity problems are limited to very small sizes (FraCaS: 37/346 examples and GLUE: 93/1650 examples). The limited syntactic patterns and vocabularies in previous test sets are obstacles in accurately evaluating

### Relevance

Label: 

## Record 0842

Paper: Can neural networks understand monotonicity reasoning?

### Question

> What NLI models do they analyze?

### Passage

> accuracy on problems annotated with reverse tags was apparently better without HELP because all examples are upward inferences embedded in a downward environment twice.
> 
> Table 9 also shows that accuracy on conditionals was better on upward inferences than that on downward inferences. This indicates that BERT might fail to capture the monotonicity property that conditionals create a downward entailing context in their scope while they create an upward entailing context out of their scope.
> 
> Regarding lexical knowledge, the data augmentation technique improved the performance much better on downward inferences which do not require lexical knowledge. However, among the 394 problems for which all models provided wrong answers, 244 problems are non-lexical inference problems. This indicates that some non-lexical inference problems are more difficult than lexical inference problems, though accuracy on non-lexical inference problems was better than that on lexical inference problems.

### Relevance

Label: 

## Record 0843

Paper: Can neural networks understand monotonicity reasoning?

### Question

> What NLI models do they analyze?

### Passage

> datasets for testing a wide range of linguistic phenomena. However, monotonicity problems are limited to very small sizes (FraCaS: 37/346 examples and GLUE: 93/1650 examples). The limited syntactic patterns and vocabularies in previous test sets are obstacles in accurately evaluating NLI models on monotonicity reasoning.
> 
> To tackle this issue, we present a new evaluation dataset that covers a wide range of monotonicity reasoning that was created by crowdsourcing and collected from linguistics publications (Section "Dataset" ). Compared with manual or automatic construction, we can collect naturally-occurring examples by crowdsourcing and well-designed ones from linguistics publications. To enable the evaluation of skills required for monotonicity reasoning, we annotate each example in our dataset with linguistic tags associated with monotonicity reasoning.
> 
> We measure the performance of state-of-the-art NLI models on monotonicity reasoning and investigate their generalization ability in upward and downward reasoning (Section "Results and Discussion" ). The results show that all models trained with SNLI BIBREF4 and MultiNLI BIBREF10 perform worse on downward inferences than on upward inferences.
> 
> In addition, we analyzed the performance of models trained with an automatically created monotonicity dataset, HELP BIBREF11 . The analysis with monotonicity data augmentation shows that models tend to perform better in the same direction of monotonicity with the training set, while they perform worse in the opposite direction. This indicates that the accuracy on monotonicity reasoning depends solely on the majority direction in the training set, and models might lack the ability to capture the structural relations between monotonicity operators and their arguments.

### Relevance

Label: 

## Record 0844

Paper: Can neural networks understand monotonicity reasoning?

### Question

> What NLI models do they analyze?

### Passage

> We also collect monotonicity inference problems from previous manually curated datasets and linguistics publications. The motivation is that previous linguistics publications related to monotonicity reasoning are expected to contain well-designed inference problems, which might be challenging problems for NLI models.
> 
> We collected 1,184 examples from 11 linguistics publications BIBREF19 , BIBREF20 , BIBREF21 , BIBREF22 , BIBREF23 , BIBREF24 , BIBREF25 , BIBREF26 , BIBREF27 , BIBREF28 , BIBREF29 . Regarding previous manually-curated datasets, we collected 93 examples for monotonicity reasoning from the GLUE diagnostic dataset, and 37 single-premise problems from FraCaS.
> 
> Both the GLUE diagnostic dataset and FraCaS categorize problems by their types of monotonicity reasoning, but we found that each dataset has different classification criteria. Thus, following GLUE, we reclassified problems into three types of monotone reasoning (upward, downward, and non-monotone) by checking if they include (i) the target monotonicity operator in both the premise and the hypothesis and (ii) the phrase replacement in its argument position. In the GLUE diagnostic dataset, there are several problems whose gold labels are contradiction. We regard them as non-entailment in that the premise does not semantically entail the hypothesis.

### Relevance

Label: 

## Record 0845

Paper: Can neural networks understand monotonicity reasoning?

### Question

> What NLI models do they analyze?

### Passage

> We merged the human-oriented dataset created via crowdsourcing and the linguistics-oriented dataset created from linguistics publications to create the current version of the monotonicity entailment dataset (MED). Table 4 shows some examples from the MED dataset. We can see that our dataset contains various phrase replacements (e.g., conjunction, relative clauses, and comparatives). Table 5 reports the statistics of the MED dataset, including 5,382 premise-hypothesis pairs (1,820 upward examples, 3,270 downward examples, and 292 non-monotone examples). Regarding non-monotone problems, gold labels are always non-entailment, whether a hypothesis is more specific or general than its premise, and thus almost all non-monotone problems are labeled as non-entailment. The size of the word vocabulary in the MED dataset is 4,023, and overlap ratios of vocabulary with previous standard NLI datasets is 95% with MultiNLI and 90% with SNLI.
> 
> We assigned a set of annotation tags for linguistic phenomena to each example in the test set. These tags allow us to analyze how well models perform on each linguistic phenomenon related to monotonicity reasoning. We defined 6 tags (see Table 4 for examples):
> 
> lexical knowledge (2,073 examples): inference problems that require lexical relations (i.e., hypernyms, hyponyms, or synonyms)
> 
> reverse (240 examples): inference problems where a propositional object is embedded in a downward environment more than once
> 
> conjunction (283 examples): inference problems that include the phrase replacement by adding conjunction (and) to the hypothesis
> 
> disjunction (254 examples): inference problems that include the phrase replacement by adding disjunction (or) to the hypothesis
> 
> conditionals (149 examples): inference problems that include conditionals (e.g., if, when, unless) in the hypothesis
> 
> negative polarity items (NPIs) (338 examples): inference problems that include NPIs (e.g., any, ever, at all, anything, anyone, anymore, anyhow, anywhere) in the hypothesis

### Relevance

Label: 

## Record 0846

Paper: Diachronic Topics in New High German Poetry

### Question

> What is the corpus used in the study?

### Passage

> We have shown the viability of Latent Dirichlet Allocation for a visualization of topic trends (the evolution of what people talk about in poetry). While most topics are easily interpretable and show a clear trend, others are quite noisy. For an exploratory experiment, the classification into time slots and for authors attribution is very promising, however far from perfect. It should be investigated whether using stanzas instead of whole poems only improves results because of more available data. Also, it needs to be determined if better topic models can deliver a better baseline for diachronic change in poetry, and if better style features will outperform semantics. Finally, only selecting clear trending and peaking topics (through co-variance) might further improve the results.

### Relevance

Label: 

## Record 0847

Paper: Diachronic Topics in New High German Poetry

### Question

> What is the corpus used in the study?

### Passage

> To test whether topic models can be used for dating poetry or attributing authorship, we perform supervised classification experiments with Random Forest Ensemble classifiers. We find that we obtain better results by training and testing on stanzas instead of full poems, as we have more data available. Also, we use 50 year slots (instead of 25) to ease the task.
> 
> For each document we determine a class label for a time slot. The slot 1575–1624 receives the label 0, the slot 1625–1674 the label 1, etc.. In total, we have 7 classes (time slots).
> 
> As a baseline, we implement rather straightforward style features, such as line length, poem length (in token, syllables, lines), cadence (number of syllables of last word in line), soundscape (ratio of closed to open syllables, see BIBREF5), and a proxy for metre, the number of syllables of the first word in the line.
> 
> We split the data randomly 70:30 training:testing, where a 50:50 shows (5 points) worse performance. We then train Random Forest Ensemble classifiers and perform a grid search over their parameters to determine the best classifier. Please note that our class sizes are quite imbalanced.
> 
> The Style baseline achieves an Accuracy of 83%, LDA features 89% and a combination of the two gets 90%. However, training on full poems reduces this to 42—52%.
> 
> The most informative features (by information gain) are: Topic11 (.067), Topic 37 (.055), Syllables Per Line (.046), Length of poem in syllables (.031), Topic19 (.029), Topic98 (.025), Topic27 ('virtue') (.023), and Soundscape (.023).
> 
> For authorship attribution, we also use a 70:30 random train:test split and use the author name as class label. We only choose the most frequent 180 authors. We find that training on stanzas gives us 71% Accuracy, but when trained on full poems, we only get 13% Accuracy. It should be further investigated is this is only because of a surplus of data.

### Relevance

Label: 

## Record 0848

Paper: Diachronic Topics in New High German Poetry

### Question

> What is the corpus used in the study?

### Passage

> We retrieve the most important (likely) words for all 100 topics and interpret these (sorted) word lists as aggregated topics, e.g. topic 27 (figure 2) contains: Tugend (virtue), Kunst (art), Ruhm (fame), Geist (spirit), Verstand (mind) and Lob (praise). This topic as a whole describes the concept of ’artistic virtue’.
> 
> In certain clusters (topics) we find poetic residuals, such that rhyme words often cluster together (as they stand in proximity), e.g. topic 52 with: Mund (mouth), Grund (cause, ground), rund (round).
> 
> To discover trends of topics over time, we bin our documents into time slots of 25 years width each. See figure 1 for a plot of the number of documents per bin. The chosen binning slots offer enough documents per slot for our experiments. To visualize trends of singular topics over time, we aggregate all documents d in slot s and add the probabilities of topic t given d and divide by the number of all d in s. This gives us the average probability of a topic per timeslot. We then plot the trajectories for each single topic. See figures 2–6 for a selection of interpretable topic trends. Please note that the scaling on the y-axis differ for each topic, as some topics are more pronounced in the whole dataset overall.
> 
> Some topic plots are already very revealing. The topic ‘artistic virtue’ (figure 2, left) shows a sharp peak around 1700—1750, outlining the period of Enlightenment. Several topics indicate Romanticism, such as ‘flowers’ (figure 2, right), ‘song’ (figure 3, left) or ‘dust, ghosts, depths’ (not shown). The period of 'Vormärz' or 'Young Germany' is quite clear with the topic ‘German Nation’ (figure 3, right). It is however hardly distinguishable from romantic topics.
> 
> We find that the topics 'Beautiful Girls' (figure 4, left) and 'Life & Death' (figure 4, right) are always quite present over time, while 'Girls' is more prounounced in Romanticism, and 'Death' in Barock.
> 
> We find that the topic 'Fire' (figure 5, left) is a fairly modern concept, that steadily rises into modernity, possibly because of the trope 'love is fire'. Next to it, the topic 'Family' (figure 5, right) shows wild fluctuation over time.
> 
> Finally, figure 6 shows topics that

### Relevance

Label: 

## Record 0849

Paper: Diachronic Topics in New High German Poetry

### Question

> What is the corpus used in the study?

### Passage

> The Digital Library in the TextGrid Repository represents an extensive collection of German texts in digital form BIBREF3. It was mined from http://zeno.org and covers a time period from the mid 16th century up to the first decades of the 20th century. It contains many important texts that can be considered as part of the literary canon, even though it is far from complete (e.g. it contains only half of Rilke’s work). We find that around 51k texts are annotated with the label ’verse’ (TGRID-V), not distinguishing between ’lyric verse’ and ’epic verse’. However, the average length of these texts is around 150 token, dismissing most epic verse tales. Also, the poems are distributed over 229 authors, where the average author contributed 240 poems (median 131 poems). A drawback of TGRID-V is the circumstance that it contains a noticeable amount of French, Dutch and Latin (over 400 texts). To constrain our dataset to German, we filter foreign language material with a stopword list, as training a dedicated language identification classifier is far beyond the scope of this work.

### Relevance

Label: 

## Record 0850

Paper: Diachronic Topics in New High German Poetry

### Question

> What is the corpus used in the study?

### Passage

> 5, left) is a fairly modern concept, that steadily rises into modernity, possibly because of the trope 'love is fire'. Next to it, the topic 'Family' (figure 5, right) shows wild fluctuation over time.
> 
> Finally, figure 6 shows topics that are most informative for the downstream classification task: Topic 11 'World, Power, Time' (left) is very clearly a Barock topic, ending at 1750, while topic 19 'Heaven, Depth, Silence' is a topic that rises from Romanticism into Modernity.

### Relevance

Label: 

## Record 0851

Paper: Argumentation Mining in User-Generated Web Discourse

### Question

> Do they report results only on English data?

### Passage

> The goal of this study was to select documents suitable for a fine-grained analysis of arguments. In a preliminary study on annotating argumentation using a small sample (50 random documents) of forum posts and comments from the raw corpus, we found that many documents convey no argumentation at all, even in discussions about controversies. We observed that such contributions do not intend to persuade; these documents typically contain story-sharing, personal worries, user interaction (asking questions, expressing agreement), off-topic comments, and others. Such characteristics are typical to on-line discussions in general, but they have not been examined with respect to argumentation or persuasion. Indeed, we observed that there are (1) documents that are completely unrelated and (2) documents that are related to the topic, but do not contain any argumentation. This issue has been identified among argumentation theorist; for example as external relevance by Paglieri.Castelfranchia.2014. Similar findings were also confirmed in related literature in argumentation mining, however never tackled empirically BIBREF53 , BIBREF8 These documents are thus not suitable for analyzing argumentation.
> 
> In order to filter documents that are suitable for argumentation annotation, we defined a binary document-level classification task. The distinction is made between either persuasive documents or non-persuasive (which includes all other sorts of texts, such as off-topic, story sharing, unrelated dialog acts, etc.).
> 
> The two annotated categories were on-topic persuasive and non-persuasive. Three annotators with near-native English proficiency annotated a set of 990 documents (a random subset of comments and forum posts) reaching 0.59 Fleiss' INLINEFORM0 . The final label was selected by majority voting. The annotation study took on average of 15 hours per annotator with approximately 55 annotated documents per hour. The resulting labels were derived by majority voting. Out of 990 documents, 524 (53%) were labeled as on-topic persuasive. We will refer to this corpus as gold data persuasive.
> 
> We examined all disagreements between annotators and discovered some typical problems, such as implicitness or topic relevance. First, the authors often express their stance towards the topic implicitly, so it must be inferred by the reader. To do so, certain common-ground knowledge is required. However, such knowledge heavily depends on many aspects, such as the reader's familiarity with the topic or

### Relevance

Label: 

## Record 0852

Paper: Argumentation Mining in User-Generated Web Discourse

### Question

> Do they report results only on English data?

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

## Record 0853

Paper: Argumentation Mining in User-Generated Web Discourse

### Question

> Do they report results only on English data?

### Passage

> This section presents experiments conducted on the annotated corpora introduced in section SECREF4 . We put the main focus on identifying argument components in the discourse. To comply with the machine learning terminology, in this section we will use the term domain as an equivalent to a topic (remember that our dataset includes six different topics; see section SECREF38 ).
> 
> We evaluate three different scenarios. First, we report ten-fold cross validation over a random ordering of the entire data set. Second, we deal with in-domain ten-fold cross validation for each of the six domains. Third, in order to evaluate the domain portability of our approach, we train the system on five domains and test on the remaining one for all six domains (which we report as cross-domain validation).

### Relevance

Label: 

## Record 0854

Paper: Argumentation Mining in User-Generated Web Discourse

### Question

> Do they report results only on English data?

### Passage

> Let us begin with summarizing answers to the research questions stated in the introduction. First, as we showed in section UID55 , existing argumentation theories do offer models for capturing argumentation in user-generated content on the Web. We built upon the Toulmin's model and proposed some extensions.
> 
> Second, as compared to the negative experiences with annotating using Walton's schemes (see sections UID52 and SECREF31 ), our modified Toulmin's model offers a trade-off between its expressiveness and annotation reliability. However, we found that the capabilities of the model to capture argumentation depend on the register and topic, the length of the document, and inherently on the literary devices and structures used for expressing argumentation as these properties influenced the agreement among annotators.
> 
> Third, there are aspects of online argumentation that lack their established theoretical counterparts, such as rhetorical questions, figurative language, narratives, and fallacies in general. We tried to model some of them in the pathos dimension of argument (section UID103 ), but no satisfying agreement was reached. Furthermore, we dealt with a step that precedes argument analysis by filtering documents given their persuasiveness with respect to the controversy. Finally, we proposed a computational model based on machine learning for identifying argument components (section SECREF108 ). In this identification task, we experimented with a wide range of linguistically motivated features and found that (1) the largest feature set (including n-grams, structural features, syntactic features, topic distribution, sentiment distribution, semantic features, coreference feaures, discourse features, and features based on word embeddings) performs best in both in-domain and all-data cross validation, while (2) features based only on word embeddings yield best results in cross-domain evaluation.
> 
> Since there is no one-size-fits-all argumentation theory to be applied to actual data on the Web, the argumentation model and an annotation scheme for argumentation mining is a function of the task requirements and the corpus properties. Its selection should be based on the data at hand and the desired application. Given the proposed use-case scenarios (section SECREF1 ) and the results of our annotation study (section SECREF51 ), we recommend a scheme based on Toulmin's model for short documents, such as comments or forum posts.

### Relevance

Label: 

## Record 0855

Paper: Argumentation Mining in User-Generated Web Discourse

### Question

> Do they report results only on English data?

### Passage

> identified. The complete predictions along with the gold data are publicly available.
> 
> SVMhmm offers many hyper-parameters with suggested default values, from which three are of importance. Parameter INLINEFORM0 sets the order of dependencies of transitions in HMM, parameter INLINEFORM1 sets the order of dependencies of emissions in HMM, and parameter INLINEFORM2 represents a trading-off slack versus magnitude of the weight-vector. For all experiments, we set all the hyper-parameters to their default values ( INLINEFORM3 , INLINEFORM4 , INLINEFORM5 ). Using the best performing feature set from Table TABREF139 , we experimented with a grid search over different values ( INLINEFORM6 , INLINEFORM7 , INLINEFORM8 ) but the results did not outperform the system trained with default parameter values.
> 
> The INLINEFORM0 scores might seem very low at the first glance. One obvious reason is the actual performance of the system, which gives a plenty of room for improvement in the future. But the main cause of low INLINEFORM2 numbers is the evaluation measure — using 11 classes on the token level is very strict, as it penalizes a mismatch in argument component boundaries the same way as a wrongly predicted argument component type. Therefore we also report two another evaluation metrics that help to put our results into a context.
> 
> Krippendorff's INLINEFORM0 — It was also used for evaluating inter-annotator agreement (see section UID75 ).
> 
> Boundary similarity BIBREF125 — Using this metric, the problem is treated solely as a segmentation task without recognizing the argument component types.
> 
> As shown in Table TABREF157 (the Macro- INLINEFORM0 scores are repeated from Table TABREF139 ), the best-performing system achieves 0.30 score using Krippendorf's INLINEFORM1 , which is in the middle between the baseline and the human performance (0.48) but is considered as poor from the inter-annotator agreement point of view BIBREF54 . The boundary similarity metrics is not directly suitable for evaluating argument component classification, but reveals a sub-task of finding the component boundaries. The best system achieved 0.32 on this measure. Vovk2013MT used this measure to annotate argument spans and his annotators achieved 0.36 boundary similarity score. Human annotators in BIBREF125 reached 0.53 boundary similarity score.
> 
> The overall performance of the system is also affected by the accuracy

### Relevance

Label: 

## Record 0856

Paper: Semantic Product Search

### Question

> What dataset is used for training?

### Passage

> In this section, we present the durable learnings from thousands of experiments. We fix the embedding dimension to 256, weight matrix initialization to Xavier initialization BIBREF29 , batch size to 8192, and the optimizer to ADAM with the configuration INLINEFORM0 for all the results presented. We refer to the hinge losses defined in Section SECREF10 with INLINEFORM1 and INLINEFORM2 as the L1 and L2 variants respectively. Unigram tokenization is used in Table TABREF26 and Table TABREF27 , as the relative ordering of results does not change with other more sophisticated tokenizations.
> 
> We present the results of different loss functions in Table TABREF26 . We see that the L2 variant of each loss consistently outperforms the L1. We hypothesize that L2 variants are robust to outliers in cosine similarity. The 3-part hinge loss outperforms the 2-part hinge loss in matching metrics in all experiments although the two loss functions have similar ranking performance. By considering impressed negatives, whose text is usually more similar to positives than negatives, separately from random negatives in the 3-part hinge loss, the scores for positives and random negatives become better separated, as shown in Section SECREF10 . The model can better differentiate between positives and random negatives, improving Recall and MAP. Because the ranking task is not distinguishing between relevant and random products but instead focuses on ordering purchased and impressed products, it is not surprising that the 2-part and 3-part loss functions have similar performance.
> 
> In Table TABREF27 , we present the results of using LSTM, GRU, and averaging to aggregate the token embeddings. Averaging performs similar to or slightly better than recurrent units with significantly less training time. As mentioned in Section SECREF8 , in the product search setting, queries and product titles tend to be relatively short, so averaging is sufficient to capture the short-range dependencies that exist in queries and product titles. Furthermore, recurrent methods are more expressive but introduce specialization between the query and title. Consequently, local word-level matching between the query and the product title may not be not captured as well.
> 
> In Table TABREF28 , we compare the performance of using different tokenization methods. We use average pooling and the 3-part L2 hinge loss.

### Relevance

Label: 

## Record 0857

Paper: Semantic Product Search

### Question

> What dataset is used for training?

### Passage

> There is a rich literature in natural language processing (NLP) and information retrieval (IR) on capturing the semantics of queries and documents. Word2vec BIBREF4 garnered significant attention by demonstrating the use of word embeddings to capture semantic structure; synonyms cluster together in the embedding space. This technique was successfully applied to document ranking for web search with the DESM model BIBREF5 . Building from the ideas in word2vec, BIBREF6 trained neural word embeddings to find neighboring words to expand queries with synonyms. Ultimately, based on these recent advancements and other key insights, the state-of-the-art models for semantic search can generally be classified into three categories:
> 
> BIBREF7 introduced Latent Semantic Analysis (LSA), which computes a low-rank factorization of a term-document matrix to identify semantic concepts and was further refined by BIBREF8 , BIBREF9 and extended by ideas from Latent Dirichlet Allocation (LDA) BIBREF10 in BIBREF11 . In 2013, BIBREF12 published the seminal paper in the space of factorized models by introducing the Deep Semantic Similarity Model (DSSM). Inspired by LSA and Semantic Hashing BIBREF13 , DSSM involves training an end-to-end deep neural network with a discriminative loss to learn a fixed-width representation for queries and documents. Fully connected units in the DSSM architecture were subsequently replaced with Convolutional Neural Networks (CNNs) BIBREF14 , BIBREF15 and Recurrent Neural Networks (RNNs) BIBREF16 to respect word ordering. In an alternate approach, which articulated the idea of interaction models, BIBREF17 introduced the Deep Relevance Matching Model (DRMM) which leverages an interaction matrix to capture local term matching within neural approaches which has been successfully extended by MatchPyramid BIBREF18 and other techniques BIBREF19 , BIBREF20 , BIBREF21 , BIBREF22 , BIBREF23 . Nevertheless, these interaction methods require memory and computation proportional to the number of words in the document and hence are prohibitively expensive for online inference. In addition, Duet BIBREF24 combines the approaches of DSSM and DRMM to balance the importance of semantic and lexical matching. Despite obtaining state-of-the-art results for ranking, these methods report limited success on ad hoc retrieval tasks BIBREF24 and only achieve a sub-50% Recall@100 and MAP on our product matching dataset, as shown with the ARC-II and Match Pyramid baselines in Table TABREF30 .
> 
> While

### Relevance

Label: 

## Record 0858

Paper: Semantic Product Search

### Question

> What dataset is used for training?

### Passage

> for ranking, these methods report limited success on ad hoc retrieval tasks BIBREF24 and only achieve a sub-50% Recall@100 and MAP on our product matching dataset, as shown with the ARC-II and Match Pyramid baselines in Table TABREF30 .
> 
> While we frequently evaluate our hypotheses on interaction matrix-based methods, we find that a factorized model architecture achieves comparable performance while only requiring constant memory per product. Hence, we only present our experiments as it pertains to factorized models in this paper. Although latent factor models improve ranking metrics due to their ability to memorize associations between the query and the product, we exclude it from this paper as we focus on the matching task. Our choice of model architecture was informed by empirical experiments while constrained by the cost per query and our ability to respond within 20 milliseconds for thousands of queries per second.

### Relevance

Label: 

## Record 0859

Paper: Semantic Product Search

### Question

> What dataset is used for training?

### Passage

> We use 11 months of search logs as training data and 1 month as evaluation. We sample 54 billion query-product training pairs. We preprocess these sampled pairs to 650 million rows by grouping the training data by query-product pairs over the entire time period and using the aggregated counts as weights for the pairs. We also decrease the training time by 3X by preprocessing the training data into tokens and using mmap to store the tokens. More details on our best practices for reducing training time can be found in Section SECREF6 .
> 
> For a given customer query, each product is in exactly one of three categories: purchased, impressed but not purchased, or random. For each query, we target a ratio of 6 impressed and 7 random products for every query-product purchase. We sample this way to train the model for both matching and ranking, although in this paper we focus on matching. Intuitively, matching should differentiate purchased and impressed products from random ones; ranking should differentiate purchased products from impressed ones.
> 
> We choose the most frequent words to build our vocabulary, referred to as INLINEFORM0 . Each token in the vocabulary is assigned a unique numeric token id, while remaining tokens are assigned 0 or a hashing based identifier. Queries are lowercased, split on whitespace, and converted into a sequence of token ids. We truncate the query tokens at the 99th percentile by length. Token vectors that are smaller than the predetermined length are padded to the right.
> 
> Products have multiple attributes, like title, brand, and color, that are material to the matching process. We evaluated architectures to embed every attribute independently and concatenate them to obtain the final product representation. However, large variability in the accuracy and availability of structured data across products led to 5% lower recall than simply concatenating the attributes. Hence, we decided to use an ordered bag of words of these attributes.

### Relevance

Label: 

## Record 0860

Paper: Semantic Product Search

### Question

> What dataset is used for training?

### Passage

> Our neural network architecture is shown in Figure FIGREF9 . As in the distributed arm of the Duet model, our first model component is an embedding layer that consists of INLINEFORM0 parameters where INLINEFORM1 is the vocabulary and INLINEFORM2 is the embedding dimension. Each row corresponds to the parameters for a word. Unlike Duet, we share our embeddings across the query and product. Intuitively, sharing the embedding layer in a Siamese network works well, capturing local word-level matching even before training these networks. Our experiments in Table UID37 confirm this intuition. We discuss the specifics of our query and product representation in Section SECREF4 .
> 
> To generate a fixed length embedding for the query ( INLINEFORM0 ) and the product ( INLINEFORM1 ) from individual word embeddings, we use average pooling after observing little difference (<0.5%) in both MAP and Recall@100 relative to recurrent approaches like LSTM and GRU (see Table TABREF27 ). Average pooling also requires far less computation, reducing training time and inference latency. We reconciled this departure from state-of-the-art solutions for Question Answering and other NLP tasks through an analysis that showed that, unlike web search, both query and product information tend to be shorter, without long-range dependencies. Additionally, product search queries do not contain stop words and typically require every query word (or its synonym) to be present in the product.
> 
> Queries typically have fewer words than the product content. Because of this, we observed a noticeable difference in the magnitude of query and product embeddings. This was expected as the query and the product models were shared with no additional parameters to account for this variance. Hence, we introduced Batch Normalization layers BIBREF25 after the pooling layers for the query and the product arms. Finally, we compute the cosine similarity between INLINEFORM0 and INLINEFORM1 . During online A/B testing, we precompute INLINEFORM2 for all the products in the catalog and use a INLINEFORM3 -Nearest Neighbors algorithm to retrieve the most similar products to a given query INLINEFORM4 .

### Relevance

Label: 

## Record 0861

Paper: #MeTooMA: Multi-Aspect Annotations of Tweets Related to the MeToo Movement

### Question

> Do the tweets come from a specific region?

### Passage

> This paper introduces a new dataset containing tweets related to the #MeToo movement. It may involve opinions over socially stigmatized issues or self-reports of distressing incidents. Therefore, it is necessary to examine the social impact of this exercise, the ethics of the individuals concerned with the dataset, and it's limitations.
> 
> Mental health implications: This dataset open sources posts curated by individuals who may have undergone instances of sexual exploitation in the past. While we respect and applaud their decision to raise their voices against their exploitation, we also understand that their revelations may have been met with public backlash and apathy in both the virtual as well as the real world. In such situations, where the social reputation of both accuser and accused may be under threat, mental health concerns become very important. As survivors recount their horrific episodes of sexual harassment, it becomes imperative to provide them with therapeutic care BIBREF25 as a safeguard against mental health hazards. Such measures, if combined with the integration of mental health assessment tools in social media platforms, can make victims of sexual abuse feel more empowered and self-contemplative towards their revelations.
> 
> Use of MeTooMA dataset for population studies: We would like to mention that there have been no attempts to conduct population-centric analysis on the proposed dataset. The analysis presented in this dataset should be seen as a proof of concept to examine the instances of #MeToo movement on Twitter. The authors acknowledge that learning from this dataset cannot be used as-is for any direct social interventions. Network sampling of real-world users for any experimental work beyond this dataset would require careful evaluation beyond the observational analysis presented herein. Moreover, the findings could be used to assist already existing human knowledge. Experiences of the affected communities should be recorded and analyzed carefully, which could otherwise lead to social stigmatization, discrimination and societal bias. Enough care has been ensured so that this work does not come across as trying to target any specific individual for their personal stance on the issues pertaining to the social theme at hand. The authors do not aim to vilify individuals accused in the #MeToo cases in any manner. Our work tries to

### Relevance

Label: 

## Record 0862

Paper: #MeTooMA: Multi-Aspect Annotations of Tweets Related to the MeToo Movement

### Question

> Do the tweets come from a specific region?

### Passage

> trying to target any specific individual for their personal stance on the issues pertaining to the social theme at hand. The authors do not aim to vilify individuals accused in the #MeToo cases in any manner. Our work tries to bring out general trends that may help researchers develop better techniques to understand mass unorganized virtual movements.
> 
> Effect on marginalized communities: The authors recognize the impact of the #MeToo movement on socially stigmatized populations like LGBTQIA+. The #MeToo movement provided such individuals with the liberty to express their notions about instances of sexual violence and harassment. The movement acted as a catalyst towards implementing social policy changes to benefit the members of these communities. Hence, it is essential to keep in mind that any experimental work undertaken on this dataset should try to minimize the biases against the minority groups which might get amplified in cases of sudden outburst of public reactions over sensitive media discussions.
> 
> Limitations of individual consent: Considering the mental health aspects of the individuals concerned, social media practitioners should vary of making automated interventions to aid the victims of sexual abuse as some individuals might not prefer to disclose their sexual identities or notions. Concerned social media users might also repeal their social media information if found out that their personal information may be potentially utilised for computational analysis. Hence, it is imperative to seek subtle individual consent before trying to profile authors involved in online discussions to uphold personal privacy.

### Relevance

Label: 

## Record 0863

Paper: #MeTooMA: Multi-Aspect Annotations of Tweets Related to the MeToo Movement

### Question

> Do the tweets come from a specific region?

### Passage

> and dialogue acts. We introduce and annotate three new dialogue acts that are specific to the movement: Allegation, Refutation, and Justification. The dataset also contains geographical information about the tweets: from which country it was posted.
> 
> We expect this dataset would be of great interest and use to both computational and socio-linguists. For computational linguists, it provides an opportunity to model three new complex dialogue acts (allegation, refutation, and justification) and also to study how these acts interact with some of the other linguistic components like stance, hate, and sarcasm. For socio-linguists, it provides an opportunity to explore how a movement manifests in social media across multiple countries.

### Relevance

Label: 

## Record 0864

Paper: #MeTooMA: Multi-Aspect Annotations of Tweets Related to the MeToo Movement

### Question

> Do the tweets come from a specific region?

### Passage

> Over the last couple of years, the MeToo movement has facilitated several discussions about sexual abuse. Social media, especially Twitter, was one of the leading platforms where people shared their experiences of sexual harassment, expressed their opinions, and also offered support to victims. A large portion of these tweets was tagged with a dedicated hashtag #MeToo, and it was one of the main trending topics in many countries. The movement was viral on social media and the hashtag used over 19 million times in a year.
> 
> The MeToo movement has been described as an essential development against the culture of sexual misconduct by many feminists, activists, and politicians. It is one of the primary examples of successful digital activism facilitated by social media platforms. The movement generated many conversations on stigmatized issues like sexual abuse and violence, which were not often discussed before because of the associated fear of shame or retaliation. This creates an opportunity for researchers to study how people express their opinion on a sensitive topic in an informal setting like social media. However, this is only possible if there are annotated datasets that explore different linguistic facets of such social media narratives.
> 
> Twitter served as a platform for many different types of narratives during the MeToo movement BIBREF0. It was used for sharing personal stories of abuse, offering support and resources to victims, and expressing support or opposition towards the movement BIBREF1. It was also used to allege individuals of sexual misconduct, refute such claims, and sometimes voice hateful or sarcastic comments about the campaign or individuals. In some cases, people also misused hashtag to share irrelevant or uninformative content. To capture all these complex narratives, we decided to curate a dataset of tweets related to the MeToo movement that is annotated for various linguistic aspects.
> 
> In this paper, we present a new dataset (MeTooMA) that contains 9,973 tweets associated with the MeToo movement annotated for relevance, stance, hate speech, sarcasm, and dialogue acts. We introduce and annotate three new dialogue acts that are specific to the movement: Allegation, Refutation, and Justification. The dataset also contains geographical information about the tweets: from which country it was posted.
> 
> We expect this dataset

### Relevance

Label: 

## Record 0865

Paper: #MeTooMA: Multi-Aspect Annotations of Tweets Related to the MeToo Movement

### Question

> Do the tweets come from a specific region?

### Passage

> A dialogue act is defined as the function of a speaker's utterance during a conversation BIBREF15, for example, question, answer, request, suggestion, etc. Dialogue Acts have been extensive studied in spoken BIBREF16 and written BIBREF17 conversations and have lately been gaining interest in social media BIBREF18. In this task, we introduced three new dialogue acts that are specific to the MeToo movement: Allegation, Refutation, and Justification.
> 
> Allegation: This category includes tweets that allege an individual or a group of sexual misconduct. The tweet could either be personal opinion or text summarizing allegations made against someone BIBREF19. The annotators were instructed to identify if the tweet includes the hypothesis of allegation based on first-hand account or a verifiable source confirming the allegation. Following is an example of a tweet that qualifies as an Allegation:
> 
> More women accuse [name] of grave sexual misconduct...twitter seethes with anger. #MeToo #pervert.
> 
> Refutation: This category contains tweets where an individual or an organization is denying allegations with or without evidence. Following is an example of a Refutation tweet:
> 
> She is trying to use the #MeToo movement to settle old scores, says [name1] after [name2] levels sexual assault allegations against him.
> 
> Justification: The class includes tweets where the author is justifying their actions. These could be alleged actions in the real world (e.g. allegation of sexual misconduct) or some action performed on twitter (e.g. supporting someone who was alleged of misconduct). Following is an example of a tweet that would be tagged as Justification:
> 
> I actually did try to report it, but he and of his friends got together and lied to the police about it. #WhyIDidNotReport.

### Relevance

Label: 

## Record 0866

Paper: Learning Word Embeddings from the Portuguese Twitter Stream: A Study of some Practical Aspects

### Question

> What new metrics are suggested to track progress?

### Passage

> Producing word embeddings from tweets is challenging due to the specificities of the vocabulary in the medium. We implemented a neural word embedding model that embeds words based on n-gram information extracted from a sample of the Portuguese Twitter stream, and which can be seen as a flexible baseline for further experiments in the field. Work reported in this paper is a preliminary study of trying to find parameters for training word embeddings from Twitter and adequate evaluation tests and gold-standard data.
> 
> Results show that using less than 50% of the available training examples for each vocabulary size might result in overfitting. The resulting embeddings obtain an interesting performance on intrinsic evaluation tests when trained a vocabulary containing the 32768 most frequent words in a Twitter sample of relatively small size. Nevertheless, results exhibit a skewness in the cosine similarity scores that should be further explored in future work. More specifically, the Class Distinction test set revealed to be challenging and opens the door to evaluation of not only similarity between words but also dissimilarities between words of different semantic classes without using absolute score values.
> 
> Therefore, a key area of future exploration has to do with better evaluation resources and metrics. We made some initial effort in this front. However, we believe that developing new intrinsic tests, agnostic to absolute values of metrics and concerned with topological aspects of the embedding space, and expanding gold-standard data with cases tailored for user-generated content, is of fundamental importance for the progress of this line of work.
> 
> Furthermore, we plan to make public available word embeddings trained from a large sample of 300M tweets collected from the Portuguese Twitter stream. This will require experimenting producing embeddings with higher dimensionality (to avoid the cosine skewness effect) and training with even larger vocabularies. Also, there is room for experimenting with some of the hyper-parameters of the model itself (e.g. activation functions, dimensions of the layers), which we know have impact on final results.

### Relevance

Label: 

## Record 0867

Paper: Learning Word Embeddings from the Portuguese Twitter Stream: A Study of some Practical Aspects

### Question

> What new metrics are suggested to track progress?

### Passage

> Despite already providing interesting practical clues for our goal of trying to embed a larger vocabulary using more of the training data we have available, these results also revealed that the intrinsic evaluation metrics we are using are overly sensitive to their corresponding cosine similarity thresholds. This sensitivity poses serious challenges for further systematic exploration of word embedding architectures and their corresponding hyper-parameters, which was also observed in other recent works BIBREF15 .
> 
> By using these absolute thresholds as criteria for deciding similarity of words, we create a dependency between the evaluation metrics and the geometry of the embedded data. If we see the embedding data as a graph, this means that metrics will change if we apply scaling operations to certain parts of the graph, even if its structure (i.e. relative position of the embedded words) does not change.
> 
> For most practical purposes (including training downstream ML models) absolute distances have little meaning. What is fundamental is that the resulting embeddings are able to capture topological information: similar words should be closer to each other than they are to words that are dissimilar to them (under the various criteria of similarity we care about), independently of the absolute distances involved.
> 
> It is now clear that a key aspect for future work will be developing additional performance metrics based on topological properties. We are in line with recent work BIBREF16 , proposing to shift evaluation from absolute values to more exploratory evaluations focusing on weaknesses and strengths of the embeddings and not so much in generic scores. For example, one metric could consist in checking whether for any given word, all words that are known to belong to the same class are closer than any words belonging to different classes, independently of the actual cosine. Future work will necessarily include developing this type of metrics.

### Relevance

Label: 

## Record 0868

Paper: Learning Word Embeddings from the Portuguese Twitter Stream: A Study of some Practical Aspects

### Question

> What new metrics are suggested to track progress?

### Passage

> Word embeddings have great practical importance since they can be used as pre-computed high-density features to ML models, significantly reducing the amount of training data required in a variety of NLP tasks. However, there are several inter-related challenges with computing and consistently distributing word embeddings concerning the:
> 
> Not only the space of possibilities for each of these aspects is large, there are also challenges in performing a consistent large-scale evaluation of the resulting embeddings BIBREF0 . This makes systematic experimentation of alternative word-embedding configurations extremely difficult.
> 
> In this work, we make progress in trying to find good combinations of some of the previous parameters. We focus specifically in the task of computing word embeddings for processing the Portuguese Twitter stream. User-generated content (such as twitter messages) tends to be populated by words that are specific to the medium, and that are constantly being added by users. These dynamics pose challenges to NLP systems, which have difficulties in dealing with out of vocabulary words. Therefore, learning a semantic representation for those words directly from the user-generated stream - and as the words arise - would allow us to keep up with the dynamics of the medium and reduce the cases for which we have no information about the words.
> 
> Starting from our own implementation of a neural word embedding model, which should be seen as a flexible baseline model for further experimentation, our research tries to answer the following practical questions:
> 
> By answering these questions based on a reasonably small sample of Twitter data (5M), we hope to find the best way to proceed and train embeddings for Twitter vocabulary using the much larger amount of Twitter data available (300M), but for which parameter experimentation would be unfeasible. This work can thus be seen as a preparatory study for a subsequent attempt to produce and distribute a large-scale database of embeddings for processing Portuguese Twitter data.

### Relevance

Label: 

## Record 0869

Paper: Learning Word Embeddings from the Portuguese Twitter Stream: A Study of some Practical Aspects

### Question

> What new metrics are suggested to track progress?

### Passage

> We tracked metrics related to the learning process itself, as a function of the vocabulary size to be embedded INLINEFORM0 and of the fraction of training data used (25%, 50%, 75% and 100%). For all possible configurations, we recorded the values of the training and validation loss (cross entropy) after each epoch. Tracking these metrics serves as a minimalistic sanity check: if the model is not able to solve the word prediction task with some degree of success (e.g. if we observe no substantial decay in the losses) then one should not expect the embeddings to capture any of the distributional information they are supposed to capture.

### Relevance

Label: 

## Record 0870

Paper: Learning Word Embeddings from the Portuguese Twitter Stream: A Study of some Practical Aspects

### Question

> What new metrics are suggested to track progress?

### Passage

> pairs of words which are supposed belong to different classes. For Word Equivalence test, we manually collected equivalente pairs, focusing on abbreviations that are popular in Twitters (e.g. “qt" INLINEFORM0 “quanto" or “lx" INLINEFORM1 “lisboa" and on frequent acronyms (e.g. “slb" INLINEFORM2 “benfica"). In total, we compiled 48 equivalence pairs.
> 
> For all these tests we computed a coverage metric. Our embeddings do not necessarily contain information for all the words contained in each of these tests. So, for all tests, we compute a coverage metric that measures the fraction of the gold-standard pairs that could actually be tested using the different embeddings produced. Then, for all the test pairs actually covered, we obtain the success metrics for each of the 3 tests by computing the ratio of pairs we were able to correctly classified as i) being distinct (cosine INLINEFORM0 0.7 or 0.8), ii) belonging to the same class (cosine INLINEFORM1 0.7 or 0.8), and iii) being equivalent (cosine INLINEFORM2 0.85 or 0.95).
> 
> It is worth making a final comment about the gold standard data. Although we do not expect this gold standard data to be sufficient for a wide-spectrum evaluation of the resulting embeddings, it should be enough for providing us clues regarding areas where the embedding process is capturing enough semantics, and where it is not. These should still provide valuable indications for planning how to produce the much larger database of word embeddings.

### Relevance

Label: 

## Record 0871

Paper: Interpreting the Syntactic and Social Elements of the Tweet Representations via Elementary Property Prediction Tasks

### Question

> In what way does each classifier evaluate one of the syntactic or social properties which are salient for a tweet?

### Passage

> In this section we list down the set of proposed elementary property prediction tasks to test the characteristics of a tweet embedding. Table TABREF4 explains all the tasks considered in this study. Note that we use a neural network to build the elementary property prediction task classifier which has the following two layers in order: the representation layer and the softmax layer on top whose size varies according to the specific task. When there are more than one input for a task, we concatenate embeddings for each input.
> 
> [1]https://noisy-text.github.io/norm-shared-task.html

### Relevance

Label: 

## Record 0872

Paper: Interpreting the Syntactic and Social Elements of the Tweet Representations via Elementary Property Prediction Tasks

### Question

> In what way does each classifier evaluate one of the syntactic or social properties which are salient for a tweet?

### Passage

> Research in social media analysis is recently seeing a surge in the number of research works applying representation learning models to solve high-level syntactico-semantic tasks such as sentiment analysis [1], semantic textual similarity computation [2], hashtag prediction [3] and so on. Though the performance of the representation learning models are better than the traditional models for all the tasks, little is known about the core properties of a tweet encoded within the representations. In a recent work, Hill et al. [4] perform a comparison of different sentence representation models by evaluating them for different high-level semantic tasks such as paraphrase identification, sentiment classification, question answering, document retrieval and so on. This type of coarse-grained analysis is opaque as it does not clearly reveal the kind of information encoded by the representations. Our work presented here constitutes the first step in opening the black-box of vector embeddings for social media posts, particularly tweets.
> 
> Essentially we ask the following question: “What are the core properties encoded in the given tweet representation?”. We explicitly group the set of these properties into two categories: syntactic and social. Syntactic category includes properties such as tweet length, the order of words in it, the words themselves, slang words, hashtags and named entities in the tweet. On the other hand, social properties consist of `is reply', and `reply time'. We investigate the degree to which the tweet representations encode these properties. We assume that if we cannot train a classifier to predict a property based on its tweet representation, then this property is not encoded in this representation. For example, the model which preserves the tweet length should perform well in predicting the length given the representation generated from the model. Though these elementary property prediction tasks are not directly related to any downstream application, knowing that the model is good at modeling a particular property (e.g., the social properties) indicates that it could excel in correlated applications (e.g., user profiling task). In this work we perform an extensive evaluation of 9 unsupervised and 4 supervised tweet representation models, using 8 different properties. The most relevant work is that of Adi et al. [5], which investigates three sentence properties in comparing unsupervised

### Relevance

Label: 

## Record 0873

Paper: Interpreting the Syntactic and Social Elements of the Tweet Representations via Elementary Property Prediction Tasks

### Question

> In what way does each classifier evaluate one of the syntactic or social properties which are salient for a tweet?

### Passage

> This work proposed a set of elementary property prediction tasks to understand different tweet representations in an application independent, fine-grained fashion. The open nature of social media not only poses a plethora of opportunities to understand the basic characteristics of the posts, but also helped us draw novel insights about different representation models. We observed that among supervised models, CNN, LSTM and BLSTM encapsulates most of the syntactic and social properties with a great accuracy, while BOW, DSSM, STV and T2V does that among the unsupervised models. Tweet length affects the task prediction accuracies, but we found that all models behave similarly under variation in tweet length. Finally while LDA is insensitive to input word order, CNN, LSTM and BLSTM are extremely sensitive to word order.

### Relevance

Label: 

## Record 0874

Paper: Interpreting the Syntactic and Social Elements of the Tweet Representations via Elementary Property Prediction Tasks

### Question

> In what way does each classifier evaluate one of the syntactic or social properties which are salient for a tweet?

### Passage

> In this work we perform an extensive evaluation of 9 unsupervised and 4 supervised tweet representation models, using 8 different properties. The most relevant work is that of Adi et al. [5], which investigates three sentence properties in comparing unsupervised sentence representation models such as average of words vectors and LSTM auto-encoders. We differ from their work in two ways: (1) While they focus on sentences, we focus on social media posts which opens up the challenge of considering multiple salient properties such as hashtags, named entities, conversations and so on. (2) While they work with only unsupervised representation-learning models, we investigate the traditional unsupervised methods (BOW, LDA), unsupervised representation learning methods (Siamese CBOW, Tweet2Vec), as well as supervised methods (CNN, BLSTM).
> 
> Our main contributions are summarized below.
> 
> The paper is organized as follows. Sections 2 and 3 discuss the set of proposed elementary property prediction tasks and the models considered for this study respectively. Section 4 and 5 presents the experiment setup and result analysis respectively. We conclude the work with a brief summary in Section 5.

### Relevance

Label: 

## Record 0875

Paper: Interpreting the Syntactic and Social Elements of the Tweet Representations via Elementary Property Prediction Tasks

### Question

> In what way does each classifier evaluate one of the syntactic or social properties which are salient for a tweet?

### Passage

> decoder persists useful information in the memory nicely. The second claim is further substantiated by observing the poor performance of SCBOW whose objective is also similar to STV, but with a simpler architecture (i.e., word vector averaging). In future it would be interesting to create such a model for Twitter conversations or chronologically ordered topical tweets so as to directly capture the latent social features from Twitter.

### Relevance

Label: 

## Record 0876

Paper: From FiLM to Video: Multi-turn Question Answering with Multi-modal Context

### Question

> Do they train a different training method except from scheduled sampling?

### Passage

> With the availability of large conversational corpora from sources like Reddit and Twitter, there has been a lot of recent work on end-to-end modelling of dialogue for open domains. BIBREF12 treated dialogue as a machine translation problem where they translate from the stimulus to the response. They observed this to be more challenging than machine translation tasks due the larger diversity of possible responses. Among approaches that just use the previous utterance to generate the current response, BIBREF13 proposed a response generation model based on the encoder decoder framework. BIBREF14 also proposed an encoder-decoder based neural network architecture that uses the previous two utterances to generate the current response. Among discriminative methods (i.e. methods that produce a score for utterances from a set and then rank them), BIBREF15 proposed a neural architecture to select the best next response from a list of responses by measuring their similarity to the dialogue context. BIBREF16 extended prior work on encoder-decoder-based models to multi-turn conversations. They trained a hierarchical model called hred for generating dialogue utterances where a recurrent neural network encoder encodes each utterance. A higher-level recurrent neural network maintains the dialogue state by further encoding the individual utterance encodings. This dialogue state is then decoded by another recurrent decoder to generate the response at that point in time. In followup work, BIBREF17 used a latent stochastic variable to condition the generation process which aided their model in producing longer coherent outputs that better retain the context.
> 
> Datasets and tasks BIBREF10 , BIBREF18 , BIBREF19 have also been released recently to study visual-input based conversations. BIBREF10 train several generative and discriminative deep neural models for the visdial task. They observe that on this task, discriminative models outperform generative models and that models making better use of the dialogue history do better than models that do not use dialogue history at all. Unexpectedly, the performance between models that use the image features and models that do no use these features is not significantly different. As we discussed in Section SECREF1 , this is similar to the issues vqa models faced initially due to the imbalanced nature of the dataset, which leads us to believe that language is a strong

### Relevance

Label: 

## Record 0877

Paper: From FiLM to Video: Multi-turn Question Answering with Multi-modal Context

### Question

> Do they train a different training method except from scheduled sampling?

### Passage

> For a given context embedding INLINEFORM0 at dialogue turn INLINEFORM1 , we minimize the negative log-likelihood of the answer word INLINEFORM2 (vocabulary size), normalized by the number of words INLINEFORM3 in the ground truth response INLINEFORM4 , L(Ct, r) = -1Mm=1MiV( [rt,m=i] INLINEFORM5 ) , where the probabilities INLINEFORM6 are given by the decoder LSTM output, r*t,m-1 ={ll rt,m-1 ; s>0.2, sU(0, 1)
> 
> v INLINEFORM0 ; else . is given by scheduled sampling BIBREF32 , and INLINEFORM1 is a symbol denoting the start of a sequence. We optimize the model using the AMSGrad algorithm BIBREF33 and use a per-condition random search to determine hyperparameters. We train the model using the BLEU-4 score on the validation set as our stopping citerion.

### Relevance

Label: 

## Record 0878

Paper: From FiLM to Video: Multi-turn Question Answering with Multi-modal Context

### Question

> Do they train a different training method except from scheduled sampling?

### Passage

> The avsd challenge tasks we address here are:
> 
> We train our modelname model for Task 1.a and Task 2.a of the challenge and we present the results in Table TABREF9 . Our model outperforms the baseline model released by BIBREF11 on all of these tasks. The scores for the winning team have been released to challenge participants and are also included. Their approach, however, is not public as of yet. We observe the following for our models:
> 
> Since the official test set has not been released publicly, results reported on the official test set have been provided by the challenge organizers. For the prototype test set and for the ablation study presented in Table TABREF24 , we use the same code for evaluation metrics as used by BIBREF11 for fairness and comparability. We attribute the significant performance gain of our model over the baseline to a combination of several factors as described below:
> 
> Our primary architectural differences over the baseline model are: not concatenating the question, answer pairs before encoding them, the auxiliary decoder module, and using the Time-Extended FiLM module for feature extraction. These, combined with using scheduled sampling and running hyperparameter optimization over the validation set to select hyperparameters, give us the observed performance boost.
> 
> We observe that our models generate fairly relevant responses to questions in the dialogues, and models with audio-visual inputs respond to audio-visual questions (e.g. “is there any voices or music ?”) correctly more often.
> 
> We conduct an ablation study on the effectiveness of different components (eg., text, video and audio) and present it in Table TABREF24 . Our experiments show that:

### Relevance

Label: 

## Record 0879

Paper: From FiLM to Video: Multi-turn Question Answering with Multi-modal Context

### Question

> Do they train a different training method except from scheduled sampling?

### Passage

> Our modelname model is based on the hred framework for modelling dialogue systems. In our model, an utterance-level recurrent lstm encoder encodes utterances and a dialogue-level recurrent lstm encoder encodes the final hidden states of the utterance-level encoders, thus maintaining the dialogue state and dialogue coherence. We use the final hidden states of the utterance-level encoders in the attention mechanism that is applied to the outputs of the description, video, and audio encoders. The attended features from these encoders are fused with the dialogue-level encoder's hidden states. An utterance-level decoder decodes the response for each such dialogue state following a question. We also add an auxiliary decoding module which is similar to the response decoder except that it tries to generate the caption and/or the summary of the video. We present our model in Figure FIGREF2 and describe the individual components in detail below.

### Relevance

Label: 

## Record 0880

Paper: From FiLM to Video: Multi-turn Question Answering with Multi-modal Context

### Question

> Do they train a different training method except from scheduled sampling?

### Passage

> The avsd dataset BIBREF28 consists of dialogues collected via amt. Each dialogue is associated with a video from the Charades BIBREF29 dataset and has conversations between two amt workers related to the video. The Charades dataset has multi-action short videos and it provides text descriptions for these videos, which the avsd challenge also distributes as the caption. The avsd dataset has been collected using similar methodology as the visdial dataset. In avsd, each dialogue turn consists of a question and answer pair. One of the amt workers assumes the role of questioner while the other amt worker assumes the role of answerer. The questioner sees three static frames from the video and has to ask questions. The answerer sees the video and answers the questions asked by the questioner. After 10 such qa turns, the questioner wraps up by writing a summary of the video based on the conversation.
> 
> Dataset statistics such as the number of dialogues, turns, and words for the avsd dataset are presented in Table TABREF5 . For the initially released prototype dataset, the training set of the avsd dataset corresponds to videos taken from the training set of the Charades dataset while the validation and test sets of the avsd dataset correspond to videos taken from the validation set of the Charades dataset. For the official dataset, training, validation and test sets are drawn from the corresponding Charades sets.
> 
> The Charades dataset also provides additional annotations for the videos such as action, scene, and object annotations, which are considered to be external data sources by the avsd challenge, for which there is a special sub-task in the challenge. The action annotations also include the start and end time of the action in the video.

### Relevance

Label: 

## Record 0881

Paper: Feature-Dependent Confusion Matrices for Low-Resource NER Labeling with Noisy Labels

### Question

> Did they evaluate against baseline?

### Passage

> We evaluate all models in five low-resource NER settings across different languages. Although the evaluation is performed for NER labeling, the proposed models are not restricted to the task of NER and can potentially be used for other tasks.

### Relevance

Label: 

## Record 0882

Paper: Feature-Dependent Confusion Matrices for Low-Resource NER Labeling with Noisy Labels

### Question

> Did they evaluate against baseline?

### Passage

> In the majority of cases, a cluster size of 10 or 25 was selected on the development set during the hyperparameter search. Increasing the number of clusters introduces smaller clusters for which it is difficult to estimate the noise matrix, due to the limited training resources. On the other hand, decreasing the number of clusters can generalize too much, resulting in loss of information on the noise distribution. For the $\lambda $ parameter, a value of either 0.3 or 0.5 was chosen on the development set giving the group clusters more or equal weight compared to the global confusion matrix. This shows that the feature dependent noise matrices are important and have a positive impact on performance.
> 
> Five confusion matrices for groups and the global matrix in the English data are shown as examples in Figure FIGREF10. One can see that the noise matrix can visibly differ depending on the cluster of the input word. Some of these differences can also be directly explained by flaws in the distant supervision method. The automatic annotation did not label any locations written in all upper-case letters as locations. Therefore, the noise distribution for all upper-cased locations differs from the distribution of other location names (cf. FIGREF10 and FIGREF10). The words April and June are used both as names for a month and as first names in English. This results in a very specific noise distribution with many temporal expressions being annotated as person entities (cf. FIGREF10). Similar to this, first-person names and also Asian words are likely to be labeled as persons by the automatic annotation method (cf. FIGREF10 and FIGREF10).
> 
> All of these groups show traits that are not displayed in the global matrix, allowing the cluster-based models to outperform the other systems.

### Relevance

Label: 

## Record 0883

Paper: Feature-Dependent Confusion Matrices for Low-Resource NER Labeling with Noisy Labels

### Question

> Did they evaluate against baseline?

### Passage

> Most languages, even with millions of speakers, have not been the center for natural language processing and are counted as low-resource for tasks like named entity recognition (NER). Similarly, even for high-resource languages, there exists only few labeled data for most entity types beyond person, location and organization. Distantly- or weakly-supervised approaches have been proposed to solve this issue, e.g., by using lists of entities for labeling raw text BIBREF0, BIBREF1. This allows obtaining large amounts of training data quickly and cheaply. Unfortunately, these labels often contain errors and learning with this noisily-labeled data is difficult and can even reduce overall performance (see, e.g. BIBREF2).
> 
> A variety of ideas have been proposed to overcome the issues of noisy training data. One popular approach is to estimate the relation between noisy and clean, gold-standard labels and use this noise model to improve the training procedure. However, most of these approaches only assume a dependency between the labels and do not take the features into account when modeling the label noise. This may disregard important information. The global confusion matrix BIBREF3 is a simple model which assumes that the errors in the noisy labels just depend on the clean labels.
> 
> Our contributions are as follows: We propose to cluster the input words with the help of additional, unlabeled data. Based on this partition of the feature space, we obtain different confusion matrices that describe the relationship between clean and noisy labels. We evaluate our newly proposed models and related baselines in several low-resource settings across different languages with real, distantly supervised data with non-synthetic noise. The advanced modeling of the noisy labels substantially improves the performance up to 36% over methods without noise-handling and up to 9% over all other noise-handling baselines.

### Relevance

Label: 

## Record 0884

Paper: Feature-Dependent Confusion Matrices for Low-Resource NER Labeling with Noisy Labels

### Question

> Did they evaluate against baseline?

### Passage

> A popular approach is modeling the relationship between noisy and clean labels, i.e., estimating $p(\hat{y}|y)$ where $y$ is the clean and $\hat{y}$ the noisy label. For example, this can be represented as a noise or confusion matrix between the clean and the noisy labels, as explained in Section SECREF3. Having its roots in statistics BIBREF4, this or similar ideas have been recently studied in NLP BIBREF2, BIBREF3, BIBREF5, image classification BIBREF6, BIBREF7, BIBREF8 and general machine learning settings BIBREF9, BIBREF10, BIBREF11. All of these methods, however, do not take the features into account that are used to represent the instances during classification. In BIBREF12 only the noise type depends on $x$ but not the actual noise model. BIBREF13 and BIBREF14 use the learned feature representation $h$ to model $p(\hat{y}|y,h(x))$ for image classification and relation extraction respectively. In the work of BIBREF15, $p(y|\hat{y},h(x))$ is estimated to clean the labels for an image classification task. The survey by BIBREF16 gives a detailed overview about other techniques for learning in the presence of noisy labels.
> 
> Specific to learning noisy sequence labels in NLP, BIBREF2 used a combination of clean and noisy data for low-resource POS tagging. BIBREF17 suggested partial annotation learning to lessen the effects of incomplete annotations and reinforcement learning for filtering incorrect labels for Chinese NER. BIBREF3 used a confusion matrix and proposed to leverage pairs of clean and noisy labels for its initialization, evaluating on English NER. For English NER and Chunking, BIBREF5 also used a confusion matrix but learned it with an EM approach and combined it with multi-task learning. Recently, BIBREF18 studied input from different, unreliable sources and how to combine them for NER prediction.

### Relevance

Label: 

## Record 0885

Paper: Feature-Dependent Confusion Matrices for Low-Resource NER Labeling with Noisy Labels

### Question

> Did they evaluate against baseline?

### Passage

> We follow the BiLSTM architecture from BIBREF3. Only the optimizer was changed for all models to NADAM BIBREF22 as this helped with convergence problems for increasing cluster numbers. The Base is trained only on clean data while Base+Noise is trained on both the clean and the noisy data without noise handling. Global-CM uses a global confusion matrix for all noisy instances to model the noise as proposed by BIBREF3 and presented in Section SECREF3. The same architecture is used for Global-ID-CM, but the confusion matrix is initialized with the identity matrix (instead of Formula DISPLAY_FORM5) and only adapted during training.
> 
> The cluster-based models we propose in Section SECREF4 are Brown-CM and K-Means-CM. We experimented with numbers of clusters of 5, 10, 25 and 50. The models that select only the largest groups $G$ are marked as *-Freq and select either 30% or 50% of the clusters. The interpolation models have the postfix *-IP with $\lambda \in \lbrace 0.3, 0.5, 0.7\rbrace $ . The combination of both is named *-Freq-IP. As for all other hyperparameters, the choice was taken on the development set.
> 
> We implemented the Cleaning BIBREF15 and Dynamic-CM BIBREF14 models. Both were not developed for sequence labeling tasks and therefore needed to be adapted. For the Cleaning model, we followed the instructions by BIBREF3. The embedding and prediction components of the Dynamic-CM model were replaced according to our base model. The output of the dense layer was used as input to the dynamic matrix generation. We experimented with and without their proposed trace loss.
> 
> The training for all models was performed with labels in the IO format. The predicted labels for the test data were converted and evaluated in IOB2 with the official CoNLL evaluation script. The IOB2 format would increase matrix size making the confusion matrix estimation more difficult without adding much information in practice. In preliminary experiments, this decreased performance in particular for low-resource settings.

### Relevance

Label: 

## Record 0886

Paper: Fixed-Size Ordinally Forgetting Encoding Based Word Sense Disambiguation

### Question

> How much lower is the computational cost of the proposed model?

### Passage

> In this paper, we propose a new method for word sense disambiguation problem, which adopts the fixed-size ordinally forgetting encoding (FOFE) to convert variable-length context into almost unique fixed-size representation. A feed forward neural network pseudo language model is trained with FOFE codes of large unlabelled corpus, and used for abstracting the context embeddings of annotated instance to build a k-nearest neighbor classifier for every polyseme. Compared to the high computational cost induced by LSTM model, the fixed-size encoding by FOFE enables the usage of a simple feed forward neural network, which is not only much more efficient but also equivalently promising in numerical performance.

### Relevance

Label: 

## Record 0887

Paper: Fixed-Size Ordinally Forgetting Encoding Based Word Sense Disambiguation

### Question

> How much lower is the computational cost of the proposed model?

### Passage

> an almost unique fixed-size representation, while also retain the positional information for words in the sequence. FOFE has been applied to several NLP problems in the past, such as language model BIBREF5 , named entity recognition BIBREF6 , and word embedding BIBREF7 . The promising results demonstrated by the FOFE approach in these areas inspired us to apply FOFE in solving the WSD problem. In this paper, we will first describe how FOFE is used to encode sequence of any length into a fixed-size representation. Next, we elaborate on how a pseudo language model is trained with the FOFE encoding from unlabelled data for the purpose of context abstraction, and how a classifier for each polyseme is built from context abstractions of its labelled training data. Lastly, we provide the experiment results of our method on several WSD data sets to justify the equivalent performance as the state-of-the-art approach.

### Relevance

Label: 

## Record 0888

Paper: Fixed-Size Ordinally Forgetting Encoding Based Word Sense Disambiguation

### Question

> How much lower is the computational cost of the proposed model?

### Passage

> Words with multiple senses commonly exist in many languages. For example, the word bank can either mean a “financial establishment” or “the land alongside or sloping down to a river or lake”, based on different contexts. Such a word is called a “polyseme”. The task to identify the meaning of a polyseme in its surrounding context is called word sense disambiguation (WSD). Word sense disambiguation is a long-standing problem in natural language processing (NLP), and has broad applications in other NLP problems such as machine translation BIBREF0 . Lexical sample task and all-word task are the two main branches of WSD problem. The former focuses on only a pre-selected set of polysemes whereas the later intends to disambiguate every polyseme in the entire text. Numerous works have been devoted in WSD task, including supervised, unsupervised, semi-supervised and knowledge based learning BIBREF1 . Our work focuses on using supervised learning to solve all-word WSD problem.
> 
> Most supervised approaches focus on extracting features from words in the context. Early approaches mostly depend on hand-crafted features. For example, IMS by BIBREF2 uses POS tags, surrounding words and collections of local words as features. These approaches are later improved by combining with word embedding features BIBREF0 , which better represents the words' semantic information in a real-value space. However, these methods neglect the valuable positional information between the words in the sequence BIBREF3 . The bi-directional Long-Short-Term-Memory (LSTM) approach by BIBREF3 provides one way to leverage the order of words. Recently, BIBREF4 improved the performance by pre-training a LSTM language model with a large unlabelled corpus, and using this model to generate sense vectors for further WSD predictions. However, LSTM significantly increases the computational complexity during the training process.
> 
> The development of the so called “fixed-size ordinally forgetting encoding” (FOFE) has enabled us to consider more efficient method. As firstly proposed in BIBREF5 , FOFE provides a way to encode the entire sequence of words of variable length into an almost unique fixed-size representation, while also retain the positional information for words in the sequence. FOFE has been applied to several NLP problems in the past, such as language model BIBREF5 , named entity recognition BIBREF6 , and word

### Relevance

Label: 

## Record 0889

Paper: Fixed-Size Ordinally Forgetting Encoding Based Word Sense Disambiguation

### Question

> How much lower is the computational cost of the proposed model?

### Passage

> A language model is trained with large unlabelled corpus by BIBREF4 in order to overcome the shortage of WSD training data. A language model represents the probability distribution of a given sequence of words, and it is commonly used in predicting the subsequent word given preceding sequence. BIBREF5 proposed a FOFE-based neural network language model by feeding FOFE code of preceding sequence into FFNN. WSD is different from language model in terms of that the sense prediction of a target word depends on its surrounding sequence rather than only preceding sequence. Hence, we build a pseudo language model that uses both preceding and succeeding sequence to accommodate the purpose of WSD tasks.
> 
> The preceding and succeeding sequences are separately converted into FOFE codes. As shown in Figure FIGREF3 , the words preceding the target word are encoded from left to right as the left FOFE code, and the words succeeding the target word are encoded from right to left as the right FOFE code. The forgetting factor that underlies the encoding direction reflects the reducing relevance of a word due to the increasing distance relative to the target word. Furthermore, the FOFE is scalable to higher orders by merging tailing partial FOFE codes. For example, a second order FOFE of sequence INLINEFORM0 can be obtained as INLINEFORM1 . Lastly, the left and right FOFE codes are concatenated into one single fixed-size vector, which can be fed into an FFNN as an input.
> 
> FFNN is constructed in fully-connected layers. Each layer receives values from previous layer as input, and produces values through a function over weighted input values as its output. FFNN increasingly abstracts the features of the data through the layers. As the pseudo language model is trained to predict the target word, the output layer is irrelevant to WSD task and hence can be discarded. However, the remaining layers still have learned the ability to generalize features from word to context during the training process. The values of the held-out layer (the second last layer) are extracted as context embedding, which provides a nice numerical abstraction of the surrounding context of a target word.

### Relevance

Label: 

## Record 0890

Paper: Fixed-Size Ordinally Forgetting Encoding Based Word Sense Disambiguation

### Question

> How much lower is the computational cost of the proposed model?

### Passage

> The linguistic distribution hypothesis states that words that occur in close contexts should have similar meaning BIBREF8 . It implies that the particular sense of a polyseme is highly related to its surrounding context. Moreover, human decides the sense of a polyseme by firstly understanding its occurring context. Likewise, our proposed model has two stages, as shown in Figure FIGREF3 : training a FOFE-based pseudo language model that abstracts context as embeddings, and performing WSD classification over context embeddings.

### Relevance

Label: 

## Record 0891

Paper: A Neural Approach to Discourse Relation Signal Detection

### Question

> How is the delta-softmax calculated?

### Passage

> model as a black box and manipulating the input to discover relevant features in the data (cf. BIBREF52). We reason that this type of evaluation is more robust than, for example, examining model internal attention weights because such weights are not designed or trained with a reward ensuring they are informative – they are simply trained on the same classification error loss as the rest of the model. Instead, we can withhold potentially relevant information from the model directly: After training is complete, we feed the test data to the model in two forms – as-is, and with each word masked, as shown in SECREF36.
> 
> . Original: <$s$>$ To\quad \ p̄rovide īnformation .. <$sep$>$ .. <$n$>$ Original: \: $<$s$>$ \: \ To \: provide \: information \: ... \: $<$sep$>$ \: ... \: $<$n$>$ \\ Masked1: \: $<$s$>$ \: $<$X$>$ \: provide \: information \: ... \: $<$sep$>$ \: ... \: $<$n$>$ \\ Masked2: \: $<$s$>$ \: \ To \: \ $<$X$>$ \: information \: ... \: $<$sep$>$ \: ... \: $<$n$>$ \\ Masked3: \: $<$s$>$ \: \ To \: provide \: \ $<$X$>$ \: ... \: $<$sep$>$ \: ... \: $<$n$>$ $ Label: purpose
> 
> We reason that, if a token is important for predicting the correct label, masking it will degrade the model's classification accuracy, or at least reduce its reported classification certainty. In SECREF36, it seems reasonable to assume that masking the word `To' has a greater impact on predicting the label purpose than masking the word `provide', and even less so, the following noun `information'. We therefore use reduction in softmax probability of the correct relation as our signaling strength metric for the model. We call this metric ${\Delta }_s$ (for delta-softmax), which can be written as:
> 
> where $rel$ is the true relation of the EDU pair, $t_i$ represents the token at index $i$ of $N$ tokens, and $X_{mask=i}$ represents the input sequence with the masked position $i$ (for $i \in 1 \ldots N$ ignoring separators, or $\phi $, the empty set).
> 
> To visualize the model's predictions, we compare ${\Delta }_s$ for a particular token to two numbers: the maximum ${\Delta }_s$ achieved by any token in the current pair (a measure

### Relevance

Label: 

## Record 0892

Paper: A Neural Approach to Discourse Relation Signal Detection

### Question

> How is the delta-softmax calculated?

### Passage

> The actual performance we are interested in evaluating is the model's ability to extract signals for given discourse relations, rather than its accuracy in predicting the relations. To do so, we must extract anchored signal predictions from the model, which is non-trivial. While earlier work on interpreting neural models has focused on token-wise softmax probability BIBREF50 or attention weights BIBREF51, using contextualized embeddings complicates the evaluation: since word representations are adjusted to reflect neighboring words, the model may assign higher importance to the word standing next to what a human annotator may interpret as a signal. Example SECREF36 illustrates the problem:
> 
> . [RGB]230, 230, 230To [RGB]53, 53, 53provide [RGB]165, 165, 165information [RGB]179, 179, 179on [RGB]175, 175, 175the [RGB]160, 160, 160analytical [RGB]157, 157, 157sample [RGB]187, 187, 187as [RGB]170, 170, 170a [RGB]168, 168, 168whole [RGB]207, 207, 207, $\xrightarrow[\text{pred:preparation}]{\text{gold:purpose}}$ [RGB]168, 168, 168two [RGB]170, 170, 170additional [RGB]164, 164, 164demographic [RGB]175, 175, 175variables [RGB]182, 182, 182are [RGB]165, 165, 165included [RGB]230, 230, 230.
> 
> Each word in SECREF36 is shaded based on the softmax probability assigned to the correct relation of the satellite, i.e. how `convincing' the model found the word in terms of local probability. In addition, the top-scoring word in each sentence is rendered in boldface for emphasis. The gold label for the relation is placed above the arrow, which indicates the direction of the relation (satellite to nucleus), and the model's predicted label is shown under the arrow.
> 
> Intuitively, the strongest signal of the purpose relation in SECREF36 is the initial infinitive marker To – however, the model ranks the adjacent provide higher and almost ignores To. We suspect that the reason for this, and many similar examples in the model evaluated based on relation probabilities, is that contextual embeddings allow for a special representation of the word provide next to To, making it difficult to tease apart the locus of the most meaningful signal.
> 
> To overcome this complication, we use the logic of permutation importance, treating the neural model as a black box and manipulating the input to discover relevant features in the data (cf. BIBREF52). We reason that this type of evaluation is more robust than, for example, examining model internal attention weights because such weights are

### Relevance

Label: 

## Record 0893

Paper: A Neural Approach to Discourse Relation Signal Detection

### Question

> How is the delta-softmax calculated?

### Passage

> which give vector space representations to substrings within each word, means that the model can learn the importance of morphological forms, such as the English gerund's -ing suffix, even for out-of-vocabulary items not seen during training.
> 
> Formally, the input to our system is formed of EDU pairs which are the head units within the respective blocks of discourse units that they belong to, which are in turn connected by an instance of a discourse relation. This means that every discourse relation in the corpus is expressed as exactly one EDU pair. Each EDU is encoded as a (possibly padded) sequence of $n$-dimensional vector representations of each word ${x_1,..,x_T}$, with some added separators which are encoded in the same way and described below. The bidirectional LSTM composes representations and context for the input, and a fully connected softmax layer gives the probability of each relation:
> 
> where the probability of each relation $rel_i$ is derived from the composed output of the function $h$ across time steps $0 \ldots t$, $\delta \in \lbrace b,f\rbrace $ is the direction of the respective LSTMs, $c_t^\delta $ is the recurrent context in each direction and $\theta = {W,b}$ gives the model weights and bias parameters (see BIBREF46 for details). Note that although the output of the system is ostensibly a probability distribution over relation types, we will not be directly interested in the most probable relation as outputted by the classifier, but rather in analyzing the model's behavior with respect to the input word representations as potential signals of each relation.
> 
> In order to capitalize on the system's natural language modeling knowledge, EDU satellite-nucleus pairs are presented to the model in text order (i.e. either the nucleus or the satellite may come first). However, the model is given special separator symbols indicating the positions of the satellite and nucleus, which are essential for deciding the relation type (e.g. cause vs. result, which may have similar cue words but lead to opposite labels), and a separator symbol indicating the transition between satellite and nucleus. This setup is illustrated in SECREF29.
> 
> . $<$s$>$ Sometimes this information is available , $<$sep$>$ but usually not . $<$n$>$
> 
> Label: concession
> 
> In this example, the satellite precedes

### Relevance

Label: 

## Record 0894

Paper: A Neural Approach to Discourse Relation Signal Detection

### Question

> How is the delta-softmax calculated?

### Passage

> 230, 230puppet [RGB]230, 230, 230did [RGB]230, 230, 230not [RGB]230, 230, 230produce [RGB]230, 230, 230any [RGB]230, 230, 230poor [RGB]230, 230, 230descriptions [RGB]230, 230, 230, [RGB]230, 230, 230and [RGB]230, 230, 230in [RGB]230, 230, 230this [RGB]230, 230, 230regard [RGB]230, 230, 230, [RGB]230, 230, 230are [RGB]230, 230, 230not [RGB]230, 230, 230yet [RGB]230, 230, 230adult-like [RGB]230, 230, 230in [RGB]230, 230, 230their [RGB]230, 230, 230SI [RGB]230, 230, 230interpretations [RGB]230, 230, 230. $\xleftarrow[\text{pred:evaluation}]{\text{gold:evaluation}}$ [RGB]230, 230, 230This [RGB]230, 230, 230is [RGB]41, 41, 41unlikely
> 
> The highlighting in SECREF36 illustrates the benefits of the masking based evaluation compared to SECREF36: the token To is now clearly the strongest signal, and the verb is taken to be less important, followed by the even less important object of the verb. This is because removing the initial To hinders classification much more than the removal of the verb or noun. We note also that although the model in fact misclassified this example as preparation, we can still use masking importance to identify To, since the score queried from the model corresponds to a relative decrease in the probability of the correct relation, purpose, even if this was not the highest scoring relation overall.
> 
> In SECREF36 we see the model's ability to correctly predict contrast based on the DM but. Note that despite a rather long sentence, the model does not need any other word nearly as much for the classification. Although the model is not trained explicitly to detect discourse markers, the DM can be recognized due to the fact that masking it leads to a drop of 66% softmax probability (${\Delta }_s$=0.66) of this pair representing the contrast relation. We can also note that a somewhat lower scoring content word is also marked: hard (${\Delta }_s$=0.18). In our gold signaling annotations, this word was marked together with comes naturally as a signal, due to the contrast between the two concepts (additionally, some people is flagged as a signal along with others). The fact that the model finds hard helpful, but does not need the contextual near antonym naturally, suggests that it is merely learning that words in the semantic space near hard may indicate contrast, and not learning about the antonymous relationship – otherwise we would expect

### Relevance

Label: 

## Record 0895

Paper: A Neural Approach to Discourse Relation Signal Detection

### Question

> How is the delta-softmax calculated?

### Passage

> To evaluate the neural model, we would like to know how well ${\Delta }_s$ corresponds to annotators' gold standard labels. This leads to two kinds of problems: the first is that the model is distantly supervised, and therefore does not know about signal types, subtypes, or any aspect of signaling annotation and its relational structure. The second problem is that signaling annotations are categorical, and do not correspond to the ratio-scaled predictions provided by ${\Delta }_s$ (this is in fact one of the motivations for desiring a model-based estimate of signaling strength).
> 
> The first issue means that we can only examine the model's ability to locate signals – not to classify them. Although there may be some conceivable ways of analyzing model output to identify classes such as DMs (which are highly lexicalized, rather than representing broad regions of vector space, as words such as unlikely might), or more contextual relational signals, such as pronouns, this line of investigation is beyond the scope of the present paper. A naive solution to the second problem might be to identify a cutoff point, e.g. deciding that all and only words scoring ${\Delta }_s>$0.15 are predicted to be signals.
> 
> The problem with the latter approach is that sentences can be very different in many ways, and specifically in both length and in levels of ambiguity. Sentences with multiple, mutually redundant cues, may produce lower ${\Delta }_s$ scores compared to shorter sentences with a subset of the same cues. Conversely, in very short sentences with low signal strength, the model may reasonably be expected to degrade very badly with the deletion of almost any word, as the context becomes increasingly incomprehensible.
> 
> For these reasons, we choose to adopt an evaluation metric from the paradigm of information retrieval, and focus on recall@k (recall at rank k, for $k=1,2,3$...). The idea is to poll the model for each sentence in which some signals have been identified, and see whether the model is able to find them if we let it guess using the word with the maximal ${\Delta }_s$ score (recall@1), regardless of how high that score is, or alternatively relax the evaluation criteria and see whether the human annotator's signal

### Relevance

Label: 

## Record 0896

Paper: Method for Aspect-Based Sentiment Annotation Using Rhetorical Analysis

### Question

> what domain do the opinions fall under?

### Passage

> A sentiment analysis can be made at the level of (1) the whole document, (2) the individual sentences, or (what is currently seen as the most attractive approach) (3) at the level of individual fragments of text. Regarding document level analysis BIBREF8 , BIBREF9 - the task at this level is to classify whether a full opinion expresses a positive, negative or neutral attitude. For example, given a product review, the model determines whether the text shows an overall positive, negative or neutral opinion about the product. The biggest disadvantage of document level analysis is an assumption that each document expresses views on a single entity. Thus, it is not applicable to documents which evaluate or compare multiple objects. As for sentence level analysis BIBREF10 - The task at this level relates to sentences and determines whether each sentence expressed a positive, negative, or neutral opinion. This level of analysis is closely related to subjectivity classification which distinguishes sentences (called objective sentences) that express factual information from sentences (called subjective sentences) that express subjective views and opinions. However, we should note that subjectivity is not equivalent to sentiment as many objective sentences can imply opinions. With feature/aspect level analysis BIBREF11 - both the document level and the sentence level analyses do not discover what exactly people liked and did not like. A finer-grained analysis can be performed at aspect level. Aspect level was earlier called feature/aspect level. Instead of looking at language constructs (documents, paragraphs, sentences, clauses or phrases), aspect level directly looks at the opinion itself. It is based on the idea that an opinion consists of a sentiment (positive or negative) and a target (of opinion). As a result, we can aggregate the opinions. For example, the phone display gathers positive feedback, but the battery is often rated negatively. The aspect-based level of analysis is much more complex since it requires more advanced knowledge representation than at the level of entire documents only. Also, the documents often consist of multiple sentences, so saying that the document is positive provides only partial information. In the literature, there exists some initial work related to aspects. There exist initial solutions that use SVM-based algorithms BIBREF12 or

### Relevance

Label: 

## Record 0897

Paper: Method for Aspect-Based Sentiment Annotation Using Rhetorical Analysis

### Question

> what domain do the opinions fall under?

### Passage

> The work was partially supported by the National Science Centre grants DEC-2016/21/N/ST6/02366 and DEC-2016/21/D/ST6/02948, and from the European Union’s Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No 691152 (RENOIR project).

### Relevance

Label: 

## Record 0898

Paper: Method for Aspect-Based Sentiment Annotation Using Rhetorical Analysis

### Question

> what domain do the opinions fall under?

### Passage

> Rhetorical analysis seeks to uncover the coherence structure underneath the text, which has been shown to be beneficial for many Natural Language Processing (NLP) applications including text summarization and compression BIBREF1 , machine translation evaluation BIBREF2 , sentiment analysis BIBREF3 , and others. Different formal theories of discourse analysis have been proposed. Martin BIBREF4 proposed discourse relations based on discourse connectives (e.g., because, but) expressed in the text. Danlos BIBREF5 extended sentence grammar and formalize discourse structure. Rhetorical Structure Theory or RST - used in our experiments - was proposed by Mann and Thompson BIBREF6 . The method proposed by them is perhaps the most influential theory of discourse in computational linguistics. Moreover, it was initially intended to be used in text generation tasks, but it became popular for parsing the structure of a text BIBREF7 . Rhetorical Structure Theory represents texts by hierarchical structures with labels. This is a tree structure, which comprises Discourse Trees (DTs). Presented at Figure FIGREF3 this Discourse Tree is a representation of the following text:
> 
> The goal of discourse analysis in our method is the segmentation of the text for the basic units of discourse structures EDU (Elementary Discourse Units) and connecting them to determine semantic relations. The analysis is performed separately for each source document, and as the output we get Discourse Trees (DT) such as in Figure FIGREF3 . At this stage, existing discourse parsers will model the structure and the labels of a DT separately. They do not take into account the sequential dependencies between the DT constituents. Then existing discourse parsers will apply greedy and sub-optimal parsing algorithms and build a Discourse Tree. During this stage, and to cope with the mentioned limitation The inferred (posterior) probabilities can be used from CRF parsing models in a probabilistic CKY-like bottom-up parsing algorithm BIBREF14 which is non-greedy and optimal. Finally, discourse parsers do not discriminate between intra-sentential parsing (i.e., building the DTs for individual sentences) and multi-sentential parsing (i.e., building a DT for the whole document) BIBREF0 . Hence, this part of the analysis will extract for us distributed information about the relationship between different EDUs from parsed texts. Then we assign sentiment orientation to each EDU.

### Relevance

Label: 

## Record 0899

Paper: Method for Aspect-Based Sentiment Annotation Using Rhetorical Analysis

### Question

> what domain do the opinions fall under?

### Passage

> Modern society is an information society bombarded from all sides by an increasing number of different pieces of information. The 21st century has brought us the rapid development of media, especially in the internet ecosystem. This change has caused the transfer of many areas of our lives to virtual reality. New forms of communication have been established. Their development has created the need for analysis of related data. Nowadays, unstructured information is available in digital form, but how can we analyse and summarise billions of newly created texts that appear daily on the internet? Natural language analysis techniques, statistics and machine learning have emerged as tools to help us. In recent years, particular attention has focused on sentiment analysis. This area is defined as the study of opinions expressed by people as well as attitudes and emotions about a particular topic, product, event, or person. Sentiment analysis determines the polarisation of the text. It answers the question as to whether a particular text is a positive, negative, or neutral one.
> 
> Our goal is to build a comprehensive set of techniques for preparing and analysing texts containing opinions and generating user-friendly descriptive reports in natural language - Figure FIGREF1 . In this paper, we describe briefly the whole workflow and present a prototype implementation. Currently, existing solutions for sentiment annotation offer mostly analysis on the level of entire documents, and if you go deeper to the level of individual product features, they are only superficial and poorly prepared for the analysis of large volumes of data. This can especially be seen in scientific articles where the analysis is carried out on a few hundred reviews only. It is worth mentioning that this task is extremely problematic because of the huge diversity of languages and the difficulty of building a single solution that can cover all the languages used in the world. Natural language analysis often requires additional pre-processing steps, especially at the stage of preparing the data for analysis, and steps specific for each language. Large differences can be seen in the analysis of the Polish language (a highly inflected language) and English (a grammatically simpler one). We propose a solution that will cover several languages,

### Relevance

Label: 

## Record 0900

Paper: Method for Aspect-Based Sentiment Annotation Using Rhetorical Analysis

### Question

> what domain do the opinions fall under?

### Passage

> In Table TABREF18 there are presented some examples of the results of our approach compared with the annotated data from Bing Liu's dataset. In the first sentence, the results of the analysis differ because we decided to treat only nouns or noun phrases as aspects, while annotators also accepted verbs. In some cases, such as sentences 2 or 4, our approach generated more valuable aspects than the annotators found, but in some cases, like sentence 5, we found fewer. This is possibly the result of our method of filtering valuable aspects - if some aspects were not frequent enough in the dataset, we can treat them as void. In cases where there is neither aspect nor sentiment in the dataset, such as sentence 6, we measure sentiment as well, as one of our analysis steps.
> 
> Figure FIGREF19 shows the agreement between our aspects and that of the dataset. We assumed two aspects as equal when they were textually the same. We made some experiments using text distance metrics, such as the Jaro-Winkler distance, but the results did not differ significantly from an exact matching. We fitted the importance factor value (on the X axis) so as to enrich final aspects set: a higher factor resulted in a larger aspects set and a higher value of precision metric, with slowly decreasing recall. First results (blue line on charts) were not satisfactory, so we removed a sentiment filtering step of analysis (orange line on chart), which doubled the precision value, with nearly the same value of recall. The level of precision for whole dataset (computer, router, and speaker) was most of the time at the same level. However, the recall of router was significantly worse than speaker and computer sets.

### Relevance

Label: 
