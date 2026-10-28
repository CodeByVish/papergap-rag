# Passage relevance annotation

Annotator: 

Judge whether the passage provides information that helps answer the question, including useful partial evidence. Topic overlap alone is not sufficient. Judge only the supplied question and passage.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Do not change record numbers, questions or passages. Work independently without consulting another annotator or reference answers.

## Record 0501

Paper: A Lost Croatian Cybernetic Machine Translation Program

### Question

> What is the reason this research was not adopted in the 1960s?

### Passage

> they did not elaborate this part.
> 
> Finka BIBREF20 notes that Matković, in his dissertation from 1957, considered the use of bigrams and trigrams to “help model the word context”. It is not clear whether Finka means character bigrams, which was computationally feasible at the time, or word bigrams, which was not feasible, but the suggestion of modelling the word context does point in this direction. Even though the beginnings of using character bigrams can be traced back to Claude Shannon BIBREF21, using character-level bigrams in natural language processing was studied extensively only by Gilbert and Moore BIBREF22. It can be argued, that in a sense, Matković predated these results, but his research and ideas were not known in the west, and he was not cited. The successful use of word bigrams in text classification had to wait until BIBREF23. The long time it took to get from character to words was mainly due to computational limitations, but Matković's ideas are not to be dismissed lightly on account of computational complexity, since the idea of using word bigrams was being explored by the Croatian group–perhaps the reason for considering such an idea was the lack of a computer and the underestimation of the memory requirements. The whole process described above is illustrated in Fig. 1.
> 
> Several remarks are in order. First, the group seemed to think that encodings would be needed, but it seems that entropy-based encodings and calculations added no real benefits (i.e. added no benefit that would not be offset by the cost of calculating the codes). In addition, Finka and Laszlo BIBREF10 seem to place great emphasis on lemmatization instead of stemming, which, if they had constructed a prototype, they would have noticed it to be very hard to tackle with the technology of the age. Nevertheless, the idea of proper lemmatization would probably be replaced with moderately precise hard-coded stemming, made with the help of the "inverse dictionary", which Finka and Laszlo proposed as one of the key tasks in their 1962 paper. This paper also highlights the need for a frequency count and taking only the most frequent words, which is an approach that later became widely used in the natural

### Relevance

Label: 

## Record 0502

Paper: A Lost Croatian Cybernetic Machine Translation Program

### Question

> What is the reason this research was not adopted in the 1960s?

### Passage

> entropy by Matković, and Matković's idea was simple: conduct a statistical analysis to determine the most frequent letters and assign them the shortest binary code. So A would get 101, while F would get 11010011 BIBREF11. Building on that, Laszlo suggested that, when making an efficient machine translation system, one has to take into account not just the letter frequencies but also the redundancies of some of the letters in a word BIBREF16. This suggests that the strategy would be as follows: first make a thesaurus, and pick a representative for each meaning, then stem or lemmatize the words, then remove the needless letters from words (i.e. letters that carry little information, such as vowels, but being careful not to equate two different words), and then encode the words in binary strings, using the letter frequencies. After that, the texts are ready for translation, but unfortunately, the translation method is never explicated. Nevertheless, it is hinted that it should be "cybernetic", which, along with what we have presented earlier, would most probably mean artificial neural networks. This is highlighted by the following passage (BIBREF11, p. 117):
> 
> "A man who spends 50 years in a lively and multifaceted mental activity hears a billion and a half words. For a machine to have an ability comparable to such an intellectual, not just in terms of speed but also in terms of quality, it has to have a memory and a language sense of the same capacity, and for that - which is paramount - it has to have in-built conduits for concept association and the ability to logically reason and verify, in a word, the ability to learn fast."
> 
> Unfortunately, this idea of using machine learning was never fully developed, and the Croatian group followed the Soviet approach(es) closely. Pranjić BIBREF17 analyses and extrapolates five basic ideas in the Soviet Machine Translation program, which were the basis for the Croatian approach:
> 
> Separation of the dictionary from the MT algorithm
> 
> Separation of the understanding and generation modules of the MT algorithms
> 
> All words need to be lemmatized
> 
> The word lemma should be the key of the dictionary, but other forms of the word must be placed as a

### Relevance

Label: 

## Record 0503

Paper: A Lost Croatian Cybernetic Machine Translation Program

### Question

> What is the reason this research was not adopted in the 1960s?

### Passage

> In this paper, we are exploring the historical significance of Croatian machine translation research group. The group was active in 1950s, and it was conducted by Bulcsu Laszlo, Croatian linguist, who was a pioneer in machine translation during the 1950s in Yugoslavia.
> 
> To put the research of the Croatian group in the right context, we have to explore the origin of the idea of machine translation. The idea of machine translation is an old one, and its origin is commonly connected with the work of Rene Descartes, i.e. to his idea of universal language, as described in his letter to Mersenne from 20.xi.1629 BIBREF0. Descartes describes universal language as a simplified version of the language which will serve as an “interlanguage” for translation. That is, if we want to translate from English to Croatian, we will firstly translate from English to an “interlanguage”, and then from the “interlanguage” to Croatian. As described later in this paper, this idea had been implemented in the machine translation process, firstly in the Indonesian-to-Russian machine translation system created by Andreev, Kulagina and Melchuk from the early 1960s.
> 
> In modern times, the idea of machine translation was put forth by the philosopher and logician Yehoshua Bar-Hillel (most notably in BIBREF1 and BIBREF2), whose papers were studied by the Croatian group. Perhaps the most important unrealized point of contact between machine translation and cybernetics happened in the winter of 1950/51. In that period, Bar-Hillel met Rudolf Carnap in Chicago, who introduced to him the (new) idea of cybernetics. Also, Carnap gave him the contact details of his former teaching assistant, Walter Pitts, who was at that moment with Norbert Wiener at MIT and who was supposed to introduce him to Wiener, but the meeting never took place BIBREF3. Nevertheless, Bar-Hillel was to stay at MIT where he, inspired by cybernetics, would go to organize the first machine translation conference in the world in 1952 BIBREF3.
> 
> The idea of machine translation was a tempting idea in the 1950s. The main military interest in machine translation as an intelligence gathering tool (translation of scientific papers, daily press, technical reports, and everything the intelligence services could get their hands on) was sparked by the

### Relevance

Label: 

## Record 0504

Paper: A Lost Croatian Cybernetic Machine Translation Program

### Question

> What is the reason this research was not adopted in the 1960s?

### Passage

> delineate that the major figures of machine translation of the time were N. Andreev of the Leningrad State University, O. Kulagina and I. Melchuk of the Steklov Mathematical Institute. There is information on an Indonesian-to-Russian machine translation system by Andreev, Kulagina and Melchuk from the early 1960s, but it is reported that the system was ultimately a failure, in the same way early USA systems were. The system had statistical elements set forth by Andreev, but the bulk was logical and knowledge-heavy processing put forth by Kulagina and Melchuk. The idea was to have a logical intermediate language, under the working name “Interlingua”, which was the connector of both natural languages, and was used to model common-sense human knowledge. For more details, see BIBREF6.
> 
> In the USSR, there were four major approaches to machine translation in the late 1950s BIBREF7. The first one was the research at the Institute for Precise Mechanics and Computational Technology of the USSR Academy of Sciences. Their approach was mostly experimental and not much different from today's empirical methods. They evaluated the majority of algorithms known at the time algorithms over meticulously prepared datasets, whose main strength was data cleaning, and by 1959 they have built a German-Russian machine translation prototype. The second approach, as noted by Mulić BIBREF7, was championed by the team at the Steklov Mathematical Institute of the USSR Academy of Sciences led by A. A. Reformatsky. Their approach was mainly logical, and they extended the theoretical ideas of Bar-Hillel BIBREF2 to build three algorithms: French-Russian, English-Russian and Hungarian-Russian. The third and perhaps the most successful approach was the one by A. A. Lyapunov, O. S. Kulagina and R. L. Dobrushin. Their efforts resulted in the formation of the Mathematical Linguistics Seminar at the Faculty of Philology in Moscow in 1956 and in Leningrad in 1957. Their approach was mainly information-theoretic (but they also tried logic-based approaches BIBREF7), which was considered cybernetic at that time. This was the main role model for the Croatian efforts from 1957 onwards. The fourth, and perhaps most influential, was the approach at the Experimental Laboratory of the Leningrad University championed by N. D. Andreev BIBREF7. Here, the algorithms for Indonesian-Russian, Arabic-Russian,

### Relevance

Label: 

## Record 0505

Paper: A Lost Croatian Cybernetic Machine Translation Program

### Question

> What is the reason this research was not adopted in the 1960s?

### Passage

> a tempting idea in the 1950s. The main military interest in machine translation as an intelligence gathering tool (translation of scientific papers, daily press, technical reports, and everything the intelligence services could get their hands on) was sparked by the Soviet advance in nuclear technology, and would later be compounded by the success of Vostok 1 (termed by the USA as a “strategic surprise”). In the nuclear age, being able to read and understand what the other side was working on was of crucial importance BIBREF4. Machine translation was quickly absorbed in the program of the Dartmouth Summer Research Project on Artificial Intelligence in 1956 (where Artificial Intelligence as a field was born), as one of the five core fields of artificial intelligence (later to be known as natural language processing). One other field was included here, the “nerve nets” as they were known back then, today commonly known as artificial neural networks. What is also essential for our discussion is that the earliest programming language for artificial intelligence, Lisp, was invented in 1958 by John McCarthy BIBREF5. But let us take a closer look at the history of machine translation. In the USA, the first major wave of government and military funding for machine translation came in 1954, and the period of abundancy lasted until 1964, when the National Research Council established the Automatic Language Processing Advisory Committee (ALPAC), which was to assess the results of the ten years of intense funding. The findings were very negative, and funding was almost gone BIBREF4, hence the ALPAC report became the catalyst for the first “AI Winter”.
> 
> One of the first recorded attempts of producing a machine translation system in the USSR was in 1954 BIBREF6, and the attempt was applauded by the Communist party of the Soviet Union, by the USSR Committee for Science and Technology and the USSR Academy of Sciences. The source does not specify how this first system worked, but it does delineate that the major figures of machine translation of the time were N. Andreev of the Leningrad State University, O. Kulagina and I. Melchuk of the Steklov Mathematical Institute. There is information on an Indonesian-to-Russian machine translation system by Andreev,

### Relevance

Label: 

## Record 0506

Paper: Progress and Tradeoffs in Neural Language Models

### Question

> What is a commonly used evaluation metric for language models?

### Passage

> We trained the QRNNs with PyTorch (0.4.0; commit 1807bac) on a Titan V GPU. To evaluate the models under a resource-constrained environment, we deployed them on a Raspberry Pi 3 (Model B) running Raspbian Stretch (4.9.41-v7+). The Raspberry Pi (RPi) is not only a standard platform, but also a close surrogate to mobile phones, using the same Cortex-A7 in many phones. We then transferred the trained models to the RPi, using the same frameworks for evaluation. We plugged the RPi into a Watts Up Pro meter, a power meter that can be read programatically over USB at a frequency of 1 Hz. For the QRNNs, we used the first 350 words of the test set, and averaged the ms/query and mJ/query. For KN-5, we used the entire test set for evaluation, since the latency was much lower. To adjust for the base power load, we subtracted idle power draw from energy usage.
> 
> For a different perspective, we further evaluated all the models under a desktop environment, using an i7-4790k CPU and Titan V GPU. Because the base power load for powering a desktop is much higher than running neural language models, we collected only latency statistics. We used the entire test set, since the QRNN runs quickly.
> 
> In addition to energy and latency, another consideration for the NLP developer selecting an operating point is the cost of underlying hardware. For our setup, the RPi costs $35 USD, the CPU costs $350 USD, and the GPU costs $3000 USD.

### Relevance

Label: 

## Record 0507

Paper: Progress and Tradeoffs in Neural Language Models

### Question

> What is a commonly used evaluation metric for language models?

### Passage

> about 7 ms/query and 6 mJ/query for PTB (Table 2 , row 1), and 264 ms/q and 229 mJ/q on WT103 (row 5). Taking 220 ms/query and consuming 300 mJ/query, AWD-LSTM and ptb-qrnn are still viable for mobile phones: The modern smartphone holds upwards of 10,000 joules BIBREF22 , and the latency is within usability standards BIBREF23 . Nevertheless, the models are still 49 $\times $ slower and 32 $\times $ more power-hungry than KN-5. The wt103-qrnn model is completely unusable on phones, taking over 1.2 seconds per next-word prediction. Neural models achieve perplexity drops of 60–80% and R@3 increases of 22–34%, but these improvements come at a much higher cost in latency and energy usage.
> 
> In Table 2 (last two columns), the desktop yields very different results: the neural models on PTB (rows 2–3) are 9 $\times $ slower than KN-5, but the absolute latency is only 8 ms/q, which is still much faster than what humans perceive as instantaneous BIBREF23 . If a high-end commodity GPU is available, then the models are only twice as slow as KN-5 is. From row 5, even better results are noted with wt103-qrnn: On the CPU, the QRNN is only 60% slower than KN-5 is, while the model is faster by 11 $\times $ on a GPU. These results suggest that, if only latency is considered under a commodity desktop environment, the QRNN model is humanly indistinguishable from the KN-5 model, even without using GPU acceleration.

### Relevance

Label: 

## Record 0508

Paper: Progress and Tradeoffs in Neural Language Models

### Question

> What is a commonly used evaluation metric for language models?

### Passage

> We conducted our experiments on Penn Treebank (PTB; BIBREF12 ) and WikiText-103 (WT103; BIBREF13 ). Preprocessed by BIBREF14 , PTB contains 887K tokens for training, 70K for validation, and 78K for test, with a vocabulary size of 10,000. On the other hand, WT103 comprises 103 million tokens for training, 217K for validation, and 245K for test, spanning a vocabulary of 267K unique tokens.
> 
> For the neural language model, we used a four-layer QRNN BIBREF10 , which achieves state-of-the-art results on a variety of datasets, such as WT103 BIBREF11 and PTB. To compare against more common LSTM architectures, we also evaluated AWD-LSTM BIBREF4 on PTB. For the non-neural approach, we used a standard five-gram model with modified Kneser-Ney smoothing BIBREF15 , as explored in BIBREF16 on PTB. We denote the QRNN models for PTB and WT103 as ptb-qrnn and wt103-qrnn, respectively.
> 
> For each model, we examined word-level perplexity, R@3 in next-word prediction, latency (ms/q), and energy usage (mJ/q). To explore the perplexity–recall relationship, we collected individual perplexity and recall statistics for each sentence in the test set.

### Relevance

Label: 

## Record 0509

Paper: Progress and Tradeoffs in Neural Language Models

### Question

> What is a commonly used evaluation metric for language models?

### Passage

> BIBREF3 , but to our knowledge no one has examined the performances tradeoffs. With deployment on a mobile device in mind, we evaluate energy usage and inference latency on a Raspberry Pi (which shares the same ARM architecture as nearly all smartphones today). We find that a 2.5 $\times $ reduction in perplexity on PTB comes at a staggering cost in terms of performance: inference with NLMs takes 49 $\times $ longer and requires 32 $\times $ more energy. Furthermore, we find that impressive reductions in perplexity translate into at best modest improvements in next-word prediction, which is arguable a better metric for evaluating software keyboards on a smartphone. The contribution of this paper is the first known elucidation of this quality–performance tradeoff. Note that we refrain from prescriptive recommendations: whether or not a tradeoff is worthwhile depends on the application. Nevertheless, NLP engineers should arguably keep these tradeoffs in mind when selecting a particular operating point.

### Relevance

Label: 

## Record 0510

Paper: Progress and Tradeoffs in Neural Language Models

### Question

> What is a commonly used evaluation metric for language models?

### Passage

> BIBREF3 evaluate recent neural language models; however, their focus is not on the computational footprint of each model, but rather the perplexity. To further reduce perplexity, many neural language model extensions exist, such as continuous cache pointer BIBREF5 and mixture of softmaxes BIBREF6 . Since our focus is on comparing “core” neural and non-neural approaches, we disregard these extra optimizations techniques in all of our models.
> 
> Other work focus on designing lightweight models for resource-efficient inference on mobile devices. BIBREF7 explore LSTMs BIBREF8 with binary weights for language modeling; BIBREF9 examine shallow feedforward neural networks for natural language processing.
> 
> AWD-LSTM. BIBREF4 show that a simple three-layer LSTM, with proper regularization and optimization techniques, can achieve state of the art on various language modeling datasets, surpassing more complex models. Specifically, BIBREF4 apply randomized backpropagation through time, variational dropout, activation regularization, embedding dropout, and temporal activation regularization. A novel scheduler for optimization, non-monotonically triggered ASGD (NT-ASGD) is also introduced. BIBREF4 name their three-layer LSTM model trained with such tricks, “AWD-LSTM.”
> 
> Quasi-Recurrent Neural Networks. Quasi-recurrent neural networks (QRNNs; BIBREF10 ) achieve current state of the art in word-level language modeling BIBREF11 . A quasi-recurrent layer comprises two separate parts: a convolution layer with three weights, and a recurrent pooling layer. Given an input $\mathbf {X} \in \mathbb {R}^{k \times n}$ , the convolution layer is $
> \mathbf {Z} = \tanh (\mathbf {W}_z \cdot \mathbf {X})\\
> \mathbf {F} = \sigma (\mathbf {W}_f \cdot \mathbf {X})\\
> \mathbf {O} = \sigma (\mathbf {W}_o \cdot \mathbf {X})
> $
> 
> where $\sigma $ denotes the sigmoid function, $\cdot $ represents masked convolution across time, and $\mathbf {W}_{\lbrace z, f, o\rbrace } \in \mathbb {R}^{m \times k \times r}$ are convolution weights with $k$ input channels, $m$ output channels, and a window size of $r$ . In the recurrent pooling layer, the convolution outputs are combined sequentially: $
> \mathbf {c}_t &= \mathbf {f}_t \odot \mathbf {c}_{t-1} + (1 -
> \mathbf {f}_t) \odot \mathbf {z}_t\\
> \mathbf {h}_t &= \mathbf {o}_t \odot \mathbf {c}_t
> $
> 
> Multiple QRNN layers can be stacked for deeper hierarchical representation, with the output $\mathbf {h}_{1:t}$ being fed as the input into the subsequent layer: In language modeling, a four-layer QRNN is a

### Relevance

Label: 

## Record 0511

Paper: GitHub Typo Corpus: A Large-Scale Multilingual Dataset of Misspellings and Grammatical Errors

### Question

> Which repositories did they collect from?

### Passage

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

### Relevance

Label: 

## Record 0512

Paper: GitHub Typo Corpus: A Large-Scale Multilingual Dataset of Misspellings and Grammatical Errors

### Question

> Which repositories did they collect from?

### Passage

> Spelling correction BIBREF0, BIBREF1, BIBREF2 and grammatical error correction (GEC) BIBREF3 are two fundamental tasks that have important implications for downstream NLP tasks and for education in general. In recent years, the use of statistical machine translation (SMT) and neural sequence-to-sequence (seq2seq) models has been becoming increasingly popular for solving these tasks. Such modern NLP models are usually data hungry and require a large amount of parallel training data consisting of sentences before and after the correction. However, only relatively small datasets are available for these tasks, compared to other NLP tasks such as machine translation. This is especially the case for spelling correction, for which only a small number of datasets consisting of individual misspelled words are available, including the Birkbeck spelling error corpus and a list of typos collected from Twitter.
> 
> Due to this lack of large-scale datasets, many research studies BIBREF4, BIBREF2, BIBREF5 resort to automatic generation of artificial errors (also called pseudo-errors). Although such methods are efficient and have seen some success, they do not guarantee that generated errors reflect the range and the distribution of true errors made by humans BIBREF6.
> 
> As one way to complement this lack of resources, Wikipedia has been utilized as a rich source of textual edits, including typos BIBREF7, BIBREF8, BIBREF9. However, the edits harvested from Wikipedia are often very noisy and diverse in their types, containing edits from typos to adding and modifying information. To make the matters worse, Wikipedia suffers from vandalism, where articles are edited in a malicious manner, which requires extensive detection and filtering.
> 
> In order to create a high-quality, large-scale dataset of misspelling and grammatical errors (collectively called typos in this paper), we leverage the data from GitHub, the largest platform for hosting and sharing repositories maintained by git, a popular version control system commonly used for software development. Changes made to git repositories (called commits, see Section 3 for the definition) are usually tagged with commit messages, making detection of typos a trivial task. Also, GitHub suffers less from vandalism, since commits in many repositories are code reviewed, a process where every change is manually reviewed by other team members before merged into the repository. This guarantees that the

### Relevance

Label: 

## Record 0513

Paper: GitHub Typo Corpus: A Large-Scale Multilingual Dataset of Misspellings and Grammatical Errors

### Question

> Which repositories did they collect from?

### Passage

> The second step for collecting typos is to extract commits and edits from the eligible repositories. This step is more straightforward—for each eligible repository, we cloned it using the GitPython library and enumerated all the commits in the master branch. A commit is considered eligible if the commit message contains the string typo in it. For each eligible commit, we then take the diff between the commit and its parent, scan the result sequentially, and collect all the pairs of a deletion line and a subsequent insertion line as an edit, unless the commit contains more than 10 edits, which is a sign of a non-typo commit. See the first box in Figure FIGREF3 for an illustration. As a result, we collected a total of 335,488 commits and 685,377 edits. The final dataset (see the second box in Figure FIGREF3 for a sample) is formatted in JSONL (JSON per line), where each line corresponds to a single commit with its metadata (its repository, commit hash, commit message, as well as a list of edits) in JSON, a format easily parsable by any programming language.

### Relevance

Label: 

## Record 0514

Paper: GitHub Typo Corpus: A Large-Scale Multilingual Dataset of Misspellings and Grammatical Errors

### Question

> Which repositories did they collect from?

### Passage

> The first step for collecting typos is to collect as many eligible GitHub repositories as possible from which commits and edits are extracted. A repository must meet some criteria in order to be included in the corpus, such as size (it needs to big enough to contain at least some amount of typo edits), license (it has to be distributed under a permissive license to allow derived work), and quality (it has to demonstrate some signs of quality, such as the number of stars).
> 
> Although GitHub provides a set of APIs (application programming interfaces) that allow end-users to access its data in a programmatic manner, it doesn't allow flexible querying on the repository meta data necessary for our data collection purposes. Therefore, we turn to GH Archive, which collects all the GitHub event data and make them accessible through flexible APIs. Specifically, we collected every repository from GH Archive that:
> 
> Has at least one pull request or pull request review comment event between November 2017 and September 2019,
> 
> Has 50 or more starts,
> 
> Has a size between 1MB and 1GB, and
> 
> Has a permissive license.
> 
> Note the “and” in the list above—a repository needs to meet all the conditions mentioned above to be eligible. The first two criteria (pull request events and the number of starts) are a sign of a quality repository. As for the license, we allowed apache-2.0 (Apache License 2.0), mit (MIT License), bsd-3-clause (BSD 3-Clause License), bsd-2-clause (BSD 2-Clause License), cc0-1.0 (Creative Commons Zero v1.0 Universal), unlicense (Unlicense), cc-by-4.0 (Creative Commons Attribution 4.0), and bsl-1.0 (Boost Software License 1.0 (BSL-1.0). A repository's number of stars, size, and license are determined as of the event in the first condition.
> 
> This resulted in a total of 43,462 eligible repositories.

### Relevance

Label: 

## Record 0515

Paper: GitHub Typo Corpus: A Large-Scale Multilingual Dataset of Misspellings and Grammatical Errors

### Question

> Which repositories did they collect from?

### Passage

> This section describes the process for collecting a large amount of typos from GitHub, which consists two steps: 1) collecting target repositories that meet some criteria and 2) collecting commits and edits from them. See Figure FIGREF15 for the overview of the typo-collecting process.

### Relevance

Label: 

## Record 0516

Paper: Phrase Table as Recommendation Memory for Neural Machine Translation

### Question

> by how much did their system improve?

### Passage

> In section 2 we described how the standard NMT models calculate the probability of the next target word (Eq. (2)). Our goal in this paper is to improve the accuracy of this probability estimation by incorporating information from phrase tables. Our main idea is to find the recommendable words and increase their probabilities at each decoding time step. Thus, three questions arise:
> 
> 1) Which words are worthy to recommend at each decoding step?
> 
> 2) How to determine an appropriate bonus value for each recommendable word?
> 
> 3) How to integrate the bonus value into NMT?
> 
> In this section, we will describe the specific methods to answer above three questions. As the basis of our work, we first introduce two definitions used by our methods.
> 
> Definition 1 (prefix of phrase): the prefix of a phrase is a word sequence which begins with the first word of the phrase and ends with any word of the phrase. Note that the prefix string can be empty. For a phrase INLINEFORM0 , this phrase contains four prefixes: INLINEFORM1 .
> 
> Definition 2 (suffix of partial translation): the suffix of the partial translation INLINEFORM0 is a word sequence, which begins with any word belonging to INLINEFORM1 , and ends with INLINEFORM2 . Similarly, the suffix string can also be empty. For partial translation INLINEFORM3 , there are four suffixes INLINEFORM4 .

### Relevance

Label: 

## Record 0517

Paper: Phrase Table as Recommendation Memory for Neural Machine Translation

### Question

> by how much did their system improve?

### Passage

> BIBREF19 's models, the source side of a phrase pair must be a chunk. Therefore, it is still a big challenge to incorporate any phrase pair in the phrase table into NMT system to alleviate the unfaithfulness problem.
> 
> In this paper, we propose an effective method to incorporate a phrase table as recommendation memory into the NMT system. To achieve this, we add bonuses to the words in recommendation set to help NMT make better predictions. Generally, our method contains three steps. 1) In order to find out which words are worthy to recommend, we first derive a candidate target phrase set by searching the phrase table according to the input sentence. After that, we construct a recommendation word set at each decoding step by matching between candidate target phrases and previously translated target words by NMT. 2) We then determine the specific bonus value for each recommendable word by using the attention vector produced by NMT and phrase translation probability extracted from phrase table. 3) Finally we integrate the word bonus value into the NMT system to improve the final results.
> 
> In this paper, we make the following contributions:
> 
> 1) We propose a method to incorporate the phrase table as recommendation memory into NMT system. We design a novel approach to find from the phrase table the target words worthy of recommendation, calculate their recommendation scores and use them to promote NMT to make better predictions.
> 
> 2) Our empirical experiments on Chinese-English translation and English-Japanese translation tasks show the efficacy of our methods. For Chinese-English translation, we can obtain an average improvement of 2.23 BLEU points. For English-Japanese translation, the improvement can reach 1.96 BLEU points. We further find that the phrase table is much more beneficial than bilingual lexicons to NMT.

### Relevance

Label: 

## Record 0518

Paper: Phrase Table as Recommendation Memory for Neural Machine Translation

### Question

> by how much did their system improve?

### Passage

> We also conduct another experiment to find out whether or not our methods are still effective when much more sentence pairs are available. Therefore, the CH-EN experiments on millions of sentence pairs are conducted and Table 3 reports the results. We can conclude from Table 3 that our model can also improve the NMT translation quality on all of the test sets and the average improvement is up to 1.83 BLEU points.

### Relevance

Label: 

## Record 0519

Paper: Phrase Table as Recommendation Memory for Neural Machine Translation

### Question

> by how much did their system improve?

### Passage

> When constructing the word recommendation set, our current methods are adding the next word of the match part into recommendation set. In order to test the validity of this strategy, we compare the current strategy with another system, in which, we can add all words in candidate target phrase set into recommendation set without matching. We denote this system by system(no matching), whose results are reported in line 5 in Table 1. From the results, we can conclude that in both CH-EN translation and EN-JA translation, system(no matching) can boost the baseline system, while the improvements are much smaller than our methods. It indicates that the matching between the phrase and partial translation is quite necessary for our methods.
> 
> As we discussed in Section 3.1, we allow the prefix and suffix to be an empty string to make first word of each phrase into the word recommendation set. To show effectiveness of this setting, we also implement another system as a comparison. In the system, the first words of each phrase are not included in the recommendation set (we denote the system by system(no first)). The results of this system are reported in line 6 in Table 1. As shown in Table 1, our methods performs better than system(no first)) on both CH-EN translation and EN-JA translation. This result shows that the first word of the target phrase is also important for our method and is worthy to recommend.

### Relevance

Label: 

## Record 0520

Paper: Phrase Table as Recommendation Memory for Neural Machine Translation

### Question

> by how much did their system improve?

### Passage

> We compare our method with other relevant methods as follows:
> 
> 1) Moses: It is a widely used phrasal SMT system BIBREF22 .
> 
> 2) Baseline: It is the baseline attention-based NMT system BIBREF23 , BIBREF24 .
> 
> 3) Arthur: It is the state-of-the-art method which incorporates discrete translation lexicons into NMT model BIBREF6 . We choose automatically learned lexicons and bias method. We implement the method on the base of the baseline attention-based NMT system. Hyper parameter INLINEFORM0 is 0.001, the same as that reported in their work.

### Relevance

Label: 

## Record 0521

Paper: Diverse Few-Shot Text Classification with Multiple Metrics

### Question

> Do they compare with the MAML algorithm?

### Passage

> Few Shot Learning FSL BIBREF0 , BIBREF1 , BIBREF2 aims to learn classifiers for new classes with only a few training examples per class. Recent deep learning based FSL approaches mainly fall into two categories: (1) metric-based approaches BIBREF3 , BIBREF4 , BIBREF5 , which aims to learn generalizable metrics and corresponding matching functions from multiple training tasks. These approaches essentially learn one metric for all tasks, which is sub-optimal when the tasks are diverse. (2) optimization-based approaches BIBREF6 , BIBREF7 , BIBREF8 , which aims to learn to optimize model parameters (by either predicting the parameter updates or directly predicting the model parameters) given the gradients computed from few-shot examples.
> 
> Previous FSL research usually adopts the $k$ -shot, $N$ -way setting, where all the few-shot tasks have the same number of $N$ class labels, and each label has $k$ training instances. Moreover, these few-shot tasks are usually constructed by sampling from one huge dataset, thus all the tasks are guaranteed to be related to each other. However, in real-world applications, the few-shot learning tasks could be diverse: there are different tasks with varying number of class labels and they are not guaranteed to be related to each other. As a result, a single meta-model or metric-model is usually not sufficient to handle all the few-shot tasks.
> 
> Task Clustering Previous task clustering methods measure the task relationships in terms of similarities among single-task model parameters BIBREF11 , BIBREF12 ; or jointly assign task clusters and train model parameters for each cluster to minimize the overall training loss BIBREF13 , BIBREF14 , BIBREF25 . These methods usually work on convex models but do not fit the deep networks, mainly because of (i) the parameters of deep networks are very high-dimensional and their similarities are not necessarily related to the functional similarities; and (ii) deep networks have flexible representation power so they may overfit to arbitrary cluster assignment if we consider training loss alone. Moreover, these methods require identical class label sets across different tasks, which does not hold in most of the realistic settings.

### Relevance

Label: 

## Record 0522

Paper: Diverse Few-Shot Text Classification with Multiple Metrics

### Question

> Do they compare with the MAML algorithm?

### Passage

> We compare our method to the following baselines: (1) Single-task CNN: training a CNN model for each task individually; (2) Single-task FastText: training one FastText model BIBREF23 with fixed embeddings for each individual task; (3) Fine-tuned the holistic MTL-CNN: a standard transfer-learning approach, which trains one MTL-CNN model on all the training tasks offline, then fine-tunes the classifier layer (i.e. $\mathrm {M}^{(cls)}$ Figure 1 (a)) on each target task; (4) Matching Network: a metric-learning based few-shot learning model trained on all training tasks; (5) Prototypical Network: a variation of matching network with different prediction function as Eq. 9 ; (6) Convex combining all single-task models: training one CNN classifier on each meta-training task individually and taking the encoder, then for each target task training a linear combination of all the above single-task encoders with Eq. ( 24 ). This baseline can be viewed as a variation of our method without task clustering. We initialize all models with pre-trained 100-dim Glove embeddings (trained on 6B corpus) BIBREF24 .
> 
> In all experiments, we set both $p_1$ and $p_2$ parameters in ( 16 ) to $0.5$ . This strikes a balance between obtaining enough observed entries in $\textbf {Y}$ , and ensuring that most of the retained similarities are consistent with the cluster membership. The window/hidden-layer sizes of CNN and the initialization of embeddings (random or pre-trained) are tuned during the cluster-encoder training phase, with the validation sets of meta-training tasks. We have the CNN with window size of 5 and 200 hidden units. The single-metric FSL baselines have 400 hidden units in the CNN encoders. On sentiment classification, all cluster-encoders use random initialized word embeddings for sentiment classification, and use Glove embeddings as initialization for intent classification, which is likely because the training sets of the intent tasks are usually small.
> 
> Since all the sentiment classification tasks are binary classification based on our dataset construction. A CNN classifier with binary output layer can be also trained as the cluster-encoder for each task cluster. Therefore we compared CNN classifier, matching network, and prototypical network on Amazon review, and found that CNN classifier performs similarly well as prototypical network. Since some of the Amazon review data is quite large

### Relevance

Label: 

## Record 0523

Paper: Diverse Few-Shot Text Classification with Multiple Metrics

### Question

> Do they compare with the MAML algorithm?

### Passage

> Table 1 shows the main results on (i) the 12 few-shot product sentiment classification tasks by leveraging the learned knowledge from the 57 previously observed tasks from other product domains; and (ii) the 10 few-shot dialog intent classification tasks by leveraging the 165 previously observed tasks from other clients' data.
> 
> Due to the limited training resources, all the supervised-learning baselines perform poorly. The two state-of-the-art metric-based FSL approaches, matching network (4) and prototypical network (5), do not perform better compared to the other baselines, since the single metric is not sufficient for all the diverse tasks. On intent classification where tasks are further diverse, all the single-metric or single-model methods (3-5) perform worse compared to the single-task CNN baseline (1). The convex combination of all the single training task models is the best performing baseline overall. However, on intent classification it only performs on par with the single-task CNN (1), which does not use any meta-learning or transfer learning techniques, mainly for two reasons: (i) with the growth of the number of meta-training tasks, the model parameters grow linearly, making the number of parameters (165 in this case) in Eq.( 24 ) too large for the few-shot tasks to fit; (ii) the meta-training tasks in intent classification usually contain less training data, making the single-task encoders not generalize well.
> 
> In contrast, our RobustTC-FSL gives consistently better results compared to all the baselines. It outperforms the baselines in previous work (1-5) by a large margin of more than 6% on the sentiment classification tasks, and more than 3% on the intent classification tasks. It is also significantly better than our proposed baseline (6), showing the advantages of the usage of task clustering.
> 
> Although the RobustTC-FSL improves over baselines on intent classification, the margin is smaller compared to that on sentiment classification, because the intent classification tasks are more diverse in nature. This is also demonstrated by the training accuracy on the target tasks, where several tasks fail to find any cluster that could provide a metric that suits their training examples. To deal with this problem, we propose an improved algorithm to automatically discover whether a target task belongs to none of the task-clusters. If the

### Relevance

Label: 

## Record 0524

Paper: Diverse Few-Shot Text Classification with Multiple Metrics

### Question

> Do they compare with the MAML algorithm?

### Passage

> fail to find any cluster that could provide a metric that suits their training examples. To deal with this problem, we propose an improved algorithm to automatically discover whether a target task belongs to none of the task-clusters. If the task doesn't belong to any of the clusters, it cannot benefit from any previous knowledge thus falls back to single-task CNN. The target task is treated as “out-of-clusters” when none of the clusters could achieve higher than 20% accuracy (selected on meta-validation tasks) on its training data. We call this method Adaptive RobustTC-FSL, which gives more than 5% performance boost over the best RobustTC-FSL result on intent classification. Note that the adaptive approach makes no difference on the sentiment tasks, because they are more closely related so re-using cluster-encoders always achieves better results compared to single-task CNNs.

### Relevance

Label: 

## Record 0525

Paper: Diverse Few-Shot Text Classification with Multiple Metrics

### Question

> Do they compare with the MAML algorithm?

### Passage

> model on $D^{valid}_j$ to get the accuracy as the transfer-performance $\textbf {S}_{ij}$ . The score shows how the representations learned on task $i$ can be adapted to task $j$ , thus indicating the similarity between tasks.
> 
> In text classification tasks, transferring an encoder with fine-tuned word embeddings from one task to another is difficult as there can be a significant difference between the two vocabularies. Hence, while learning the single-task CNN classifiers, we always make the word embeddings fixed.
> 
> [t] InputInput OutputOutput $K$ task clusters $C_{1:K}$ Learning of Single-Task Models: train single-task models $\mathrm {M}_i$ for each task $\mathrm {T}_i$ Evaluation of Transfer-Performance Matrix: get performance matrix $\mathbf {\textbf {S}}$ (Section UID12 ) Score Filtering: Filter the uncertain scores in $\textbf {S}$ and construct the symmetric matrix $\textbf {Y}$ using Eq. ( 16 ) Matrix Completion: Complete the similar matrix $\textbf {X}$ from $\textbf {Y}$ using Eq. ( 18 ) Task Clustering: $C_{1:K}$ =SpectralClustering $C_{1:K}$0 RobustTC: Robust Task Clustering based on Matrix Completion
> 
> Directly using the transfer performance for task clustering may suffer from both efficiency and accuracy issues. First, evaluation of all entries in the matrix $\textbf {S}$ involves conducting the source-target transfer learning $O(n^2)$ times, where $n$ is the number of meta-training tasks. For a large number of diverse tasks where the $n$ can be larger than 1,000, evaluation of the full matrix is unacceptable (over 1M entries to evaluate). Second, the estimated cross-task performance (i.e. some $\textbf {S}_{ij}$ or $\textbf {S}_{ji}$ scores) is often unreliable due to small data size or label noise. When the number of the uncertain values is large, they can collectively mislead the clustering algorithm to output an incorrect task-partition. To address the aforementioned challenges, we propose a novel task clustering algorithm based on the theory of matrix completion BIBREF21 . Specifically, we deal with the huge number of entries by randomly sample task pairs to evaluate the $\textbf {S}_{ij}$ and $\textbf {S}_{ji}$ scores. Besides, we deal with the unreliable entries and asymmetry issue by keeping only task pairs $(i,j)$ with consistent $\textbf {S}_{ij}$ and $O(n^2)$0 scores. as will be introduced in Eq. ( 16 ). Below, we describe our method in detail.
> 
> First, we use only reliable

### Relevance

Label: 

## Record 0526

Paper: Transfer Learning for Low-Resource Neural Machine Translation

### Question

> How did they constrain training using the parameters?

### Passage

> should be modified during training of the child model. Freezing certain portions of the parent model and fine tuning others can be considered a hard approximation to a tight prior or strong regularization applied to some of the parameters. We also experiment with ordinary L2 regularization, but find it does not significantly improve over the parameter freezing described above.
> 
> Our method results in large Bleu increases for a variety of low resource languages. In one of the four language pairs our NMT system using transfer beats a strong SBMT baseline. Not only do these transfer models do well on their own, they also give large gains when used for rescoring $n$ -best lists ( $n = 1000$ ) from the SBMT system. Section "Experiments" details these results.

### Relevance

Label: 

## Record 0527

Paper: Transfer Learning for Low-Resource Neural Machine Translation

### Question

> How did they constrain training using the parameters?

### Passage

> Neural machine translation (NMT) BIBREF0 is a promising paradigm for extracting translation knowledge from parallel text. NMT systems have achieved competitive accuracy rates under large-data training conditions for language pairs such as English-French. However, neural methods are data-hungry and learn poorly from low-count events. This behavior makes vanilla NMT a poor choice for low-resource languages, where parallel data is scarce. Table 1 shows that for 4 low-resource languages, a standard string-to-tree statistical MT system (SBMT) BIBREF1 , BIBREF2 strongly outperforms NMT, even when NMT uses the state-of-the-art local attention plus feed-input techniques from luong2015effective.
> 
> In this paper, we give a method for substantially improving NMT results on these languages. Neural models learn representations of their input that are often useful across tasks. Our key idea is to first train a high-resource language pair, then use the resulting trained network (the parent model) to initialize and constrain training for our low-resource language pair (the child model). We find that we can optimize our results by fixing certain parameters of the parent model, letting the rest be fine-tuned by the child model. We report NMT improvements from transfer learning of 5.6 Bleu on average, and we provide an analysis of why the method works. The final NMT system approaches strong SBMT baselines in in all four language pairs, and exceeds SBMT performance in one of them. Furthermore, we show that NMT is an exceptional re-scorer of `traditional' MT output; even NMT that on its own is worse than SBMT is consistently able to improve upon SBMT system output when incorporated as a re-scoring model.
> 
> We start by a brief description of our NMT model in Section "NMT Background" . Section "Transfer Results" gives some background on transfer learning and explains how we use it to improve machine translation performance. Our main experiments translating Hausa, Turkish, Uzbek and Urdu into English with the help of a French-English parent model are presented in Section "Experiments" . Section "Analysis" explores alternatives to our model to enhance understanding. We find that the choice of parent language pair affects performance, and provide an empirical upper bound on transfer performance using an artificial language. We experiment with English-only language models, copy models, and

### Relevance

Label: 

## Record 0528

Paper: Transfer Learning for Low-Resource Neural Machine Translation

### Question

> How did they constrain training using the parameters?

### Passage

> In all the above experiments, only the target input and output embeddings are fixed during training. In this section we analyze what happens when different parts of the model are fixed, in order to see what yields optimal performance. Figure 2 shows a diagram of the components of a sequence-to-sequence model. Table 7 shows how we begin to allow more components of the child NMT model to be trained and see the effect on performance in the model. We see that the optimal setting for transferring from French-English to Uzbek-English in terms of Bleu performance is to allow all of the components of the child model to be trained except for the input and output target embeddings.
> 
> Even though we use this setting for our main experiments, the optimum setting is likely to be language- and corpus-dependent. For Turkish, experiments show that freezing target attention parameters as well gives slightly better results. For parent-child models with closely related languages we expect freezing, or strongly regularizing, more components of the model to give better results.

### Relevance

Label: 

## Record 0529

Paper: Transfer Learning for Low-Resource Neural Machine Translation

### Question

> How did they constrain training using the parameters?

### Passage

> Transfer learning uses knowledge from a learned task to improve the performance on a related task, typically reducing the amount of required training data BIBREF9 , BIBREF10 . In natural language processing, transfer learning methods have been successfully applied to speech recognition, document classification and sentiment analysis BIBREF11 . Deep learning models discover multiple levels of representation, some of which may be useful across tasks, which makes them particularly suited to transfer learning BIBREF12 . For example, cirecsan2012transfer use a convolutional neural network to recognize handwritten characters and show positive effects of transfer between models for Latin and Chinese characters. Ours is the first study to apply transfer learning to neural machine translation.
> 
> The transfer learning approach we use is simple and effective. We first train an NMT model on a dataset where there is a large amount of bilingual data (e.g., French-English), which we call the parent model. Next, we initialize an NMT model with the already-trained parent model. This new model is then trained on a dataset with very little bilingual data (e.g., Uzbek-English), which we call the child model. This means that the low-data NMT model will not start with random weights, but with the weights from the parent model.
> 
> A justification for this approach is that in scenarios where we have limited training data, we need a strong prior distribution over models. The parent model trained on a large amount of bilingual data can be considered an anchor point, the peak of our prior distribution in model space. When we train the child model initialized with the parent model, we fix parameters likely to be useful across tasks so that they will not be changed during child-model training. In the French-English to Uzbek-English example, as a result of the initialization, the English word embeddings from the parent model are copied, but the Uzbek words are initially mapped to random French embeddings. The English embeddings should be kept but the Uzbek embeddings should be modified during training of the child model. Freezing certain portions of the parent model and fine tuning others can be considered a hard approximation to a tight prior or strong regularization applied to some of the parameters. We

### Relevance

Label: 

## Record 0530

Paper: Transfer Learning for Low-Resource Neural Machine Translation

### Question

> How did they constrain training using the parameters?

### Passage

> To evaluate how well our transfer method works we apply it to a variety of low-resource languages, both stand-alone and for re-scoring a strong SBMT baseline. We report large Bleu increases across the board with our transfer method.
> 
> For all of our experiments with low-resource languages we use French as the parent source language and for child source languages we use Hausa, Turkish, Uzbek, and Urdu. The target language is always English. Table 1 shows parallel training data set sizes for the child languages, where the language with the most data has only 1.8m English tokens. For comparison, our parent French-English model uses a training set with 300 million English tokens and achieves 26 Bleu on the development set. Table 1 also shows the SBMT system scores along with the NMT baselines that do not use transfer. There is a large gap between the SBMT and NMT systems without using our transfer method.
> 
> The SBMT system used in this paper is a string-to-tree statistical machine translation system BIBREF2 , BIBREF1 . In this system there are two count-based 5-gram language models. One is trained on the English side of the WMT 2015 English-French dataset and the other is trained on the English side of the low-resource bitext. Additionally, the SBMT models use thousands of sparsely-occurring, lexicalized syntactic features BIBREF13 .
> 
> For our NMT system, we use development sets for Hausa, Turkish, Uzbek, and Urdu to tune the learning rate, parameter initialization range, dropout rate and hidden state size for all the experiments. For training we use a minibatch size of 128, hidden state size of 1000, a target vocabulary size of 15K and a source vocabulary size of 30K. The child models are trained with a dropout probability of 0.5 as in dropout. The common parent model is trained with a dropout probability of 0.2. The learning rate used for both child and parents is 0.5 with a decay rate of 0.9 when the development perplexity does not improve. The child models are all trained for 100 epochs. We re-scale the gradient when the gradient norm is greater than 5. The initial parameter range is $[$ -0.08, +0.08 $]$ .

### Relevance

Label: 

## Record 0531

Paper: Bringing Structure into Summaries: Crowdsourcing a Benchmark Corpus of Concept Maps

### Question

> How do the authors define a concept map?

### Passage

> Concept-map-based MDS is defined as follows: Given a set of related documents, create a concept map that represents its most important content, satisfies a specified size limit and is connected.
> 
> We define a concept map as a labeled graph showing concepts as nodes and relationships between them as edges. Labels are arbitrary sequences of tokens taken from the documents, making the summarization task extractive. A concept can be an entity, abstract idea, event or activity, designated by its unique label. Good maps should be propositionally coherent, meaning that every relation together with the two connected concepts form a meaningful proposition.
> 
> The task is complex, consisting of several interdependent subtasks. One has to extract appropriate labels for concepts and relations and recognize different expressions that refer to the same concept across multiple documents. Further, one has to select the most important concepts and relations for the summary and finally organize them in a graph satisfying the connectedness and size constraints.

### Relevance

Label: 

## Record 0532

Paper: Bringing Structure into Summaries: Crowdsourcing a Benchmark Corpus of Concept Maps

### Question

> How do the authors define a concept map?

### Passage

> Having a manageable number of propositions, an annotator then applied a few straightforward transformations that correct common errors of the Open IE system. First, we break down propositions with conjunctions in either of the arguments into separate propositions per conjunct, which the Open IE system sometimes fails to do. And second, we correct span errors that might occur in the argument or relation phrases, especially when sentences were not properly segmented. As a result, we have a set of high quality propositions for our concept map, consisting of, due to the first transformation, 56.1 propositions per topic on average.

### Relevance

Label: 

## Record 0533

Paper: Bringing Structure into Summaries: Crowdsourcing a Benchmark Corpus of Concept Maps

### Question

> How do the authors define a concept map?

### Passage

> Some attempts have been made to automatically construct concept maps from text, working with either single documents BIBREF14 , BIBREF9 , BIBREF15 , BIBREF16 or document clusters BIBREF17 , BIBREF18 , BIBREF19 . These approaches extract concept and relation labels from syntactic structures and connect them to build a concept map. However, common task definitions and comparable evaluations are missing. In addition, only a few of them, namely Villalon.2012 and Valerio.2006, define summarization as their goal and try to compress the input to a substantially smaller size. Our newly proposed task and the created large-cluster dataset fill these gaps as they emphasize the summarization aspect of the task.
> 
> For the subtask of selecting summary-worthy concepts and relations, techniques developed for traditional summarization BIBREF20 and keyphrase extraction BIBREF21 are related and applicable. Approaches that build graphs of propositions to create a summary BIBREF22 , BIBREF23 , BIBREF24 , BIBREF25 seem to be particularly related, however, there is one important difference: While they use graphs as an intermediate representation from which a textual summary is then generated, the goal of the proposed task is to create a graph that is directly interpretable and useful for a user. In contrast, these intermediate graphs, e.g. AMR, are hardly useful for a typical, non-linguist user.
> 
> For traditional summarization, the most well-known datasets emerged out of the DUC and TAC competitions. They provide clusters of news articles with gold-standard summaries. Extending these efforts, several more specialized corpora have been created: With regard to size, Nakano.2010 present a corpus of summaries for large-scale collections of web pages. Recently, corpora with more heterogeneous documents have been suggested, e.g. BIBREF26 and BIBREF27 . The corpus we present combines these aspects, as it has large clusters of heterogeneous documents, and provides a necessary benchmark to evaluate the proposed task.
> 
> For concept map generation, one corpus with human-created summary concept maps for student essays has been created BIBREF28 . In contrast to our corpus, it only deals with single documents, requires a two orders of magnitude smaller amount of compression of the input and is not publicly available .
> 
> Other types of information representation that also model concepts and their relationships are knowledge bases, such as

### Relevance

Label: 

## Record 0534

Paper: Bringing Structure into Summaries: Crowdsourcing a Benchmark Corpus of Concept Maps

### Question

> How do the authors define a concept map?

### Passage

> As concept maps consist of propositions expressing the relation between concepts (see Figure FIGREF2 ), we need to impose such a structure upon the plain text in the document clusters. This could be done by manually annotating spans representing concepts and relations, however, the size of our clusters makes this a huge effort: 2288 sentences per topic (69k in total) need to be processed. Therefore, we resort to an automatic approach.
> 
> The Open Information Extraction paradigm BIBREF38 offers a representation very similar to the desired one. For instance, from
> 
> Students with bad credit history should not lose hope and apply for federal loans with the FAFSA.
> 
> Open IE systems extract tuples of two arguments and a relation phrase representing propositions:
> 
> (s. with bad credit history, should not lose, hope)
> 
> (s. with bad credit history, apply for, federal loans with the FAFSA)
> 
> While the relation phrase is similar to a relation in a concept map, many arguments in these tuples represent useful concepts. We used Open IE 4, a state-of-the-art system BIBREF39 to process all sentences. After removing duplicates, we obtained 4137 tuples per topic.
> 
> Since we want to create a gold-standard corpus, we have to ensure that we produce high-quality data. We therefore made use of the confidence assigned to every extracted tuple to filter out low quality ones. To ensure that we do not filter too aggressively (and miss important aspects in the final summary), we manually annotated 500 tuples sampled from all topics for correctness. On the first 250 of them, we tuned the filter threshold to 0.5, which keeps 98.7% of the correct extractions in the unseen second half. After filtering, a topic had on average 2850 propositions (85k in total).

### Relevance

Label: 

## Record 0535

Paper: Bringing Structure into Summaries: Crowdsourcing a Benchmark Corpus of Concept Maps

### Question

> How do the authors define a concept map?

### Passage

> Likert-scale tasks and 0.69 (Spearman 0.66) for comparison tasks. This shows that the approach, despite the subjectiveness of the task, allows us to collect reliable annotations.
> 
> In addition to the reliability studies, we extrinsically evaluated the annotations in the task of summary evaluation. For each of the 58 peer summaries in TAC2008, we calculated a score as the sum of the importance estimates of the propositions it contains. Table TABREF13 shows how these peer scores, averaged over the three topics, correlate with the manual responsiveness scores assigned during TAC in comparison to ROUGE-2 and Pyramid scores. The results demonstrate that with both task designs, we obtain importance annotations that are similarly useful for summary evaluation as pyramid annotations or gold-standard summaries (used for ROUGE).
> 
> Based on the pilot study, we conclude that the proposed crowdsourcing scheme allows us to obtain proper importance annotations for propositions. As workers are not required to read all documents, the annotation is much more efficient and scalable as with traditional methods.

### Relevance

Label: 

## Record 0536

Paper: A Discrete CVAE for Response Generation on Short-Text Conversation

### Question

> How does discrete latent variable has an explicit semantic meaning to improve the CVAE on short-text conversation?

### Passage

> latent variables, the model is expected to decode diverse responses. Due to the advantage of the CVAE in modeling the response generation process, we focus on improving the performance of the CVAE-based response generation models.
> 
> Although the CVAE has achieved impressive results on many generation problems BIBREF16, BIBREF17, recent results on response generation show that the CVAE-based generation models still suffer from the low output diversity problem. That is multiple sampled latent variables result in responses with similar semantic meanings. To address this problem, extra guided signals are often used to improve the basic CVAE. BIBREF14 zhao2017learning use dialogue acts to capture the discourse variations in multi-round dialogues as guided knowledge. However, such discourse information can hardly be extracted for short-text conversation.
> 
> In our work, we propose a discrete CVAE (DCVAE), which utilizes a discrete latent variable with an explicit semantic meaning in the CVAE for short-text conversation. Our model mitigates the low output diversity problem in the CVAE by exploiting the semantic distance between the latent variables to maintain good diversity between the sampled latent variables. Accordingly, we propose a two-stage sampling approach to enable efficient selection of diverse variables from a large latent space assumed in the short-text conversation task.
> 
> To summarize, this work makes three contributions: (1) We propose a response generation model for short-text conversation based on a DCVAE, which utilizes a discrete latent variable with an explicit semantic meaning and could generate high-quality responses. (2) A two-stage sampling approach is devised to enable efficient selection of diverse variables from a large latent space assumed in the short-text conversation task. (3) Experimental results show that the proposed DCVAE with the two-stage sampling approach outperforms various kinds of generation models under both automatic and human evaluations, and generates more high-quality responses. All our code and datasets are available at https://ai.tencent.com/ailab/nlp/dialogue.

### Relevance

Label: 

## Record 0537

Paper: A Discrete CVAE for Response Generation on Short-Text Conversation

### Question

> How does discrete latent variable has an explicit semantic meaning to improve the CVAE on short-text conversation?

### Passage

> In this paper, we have presented a novel response generation model for short-text conversation via a discrete CVAE. We replace the continuous latent variable in the standard CVAE by an interpretable discrete variable, which is set to a word in the vocabulary. The sampled latent word has an explicit semantic meaning, acting as a guide to the generation of informative and diverse responses. We also propose to use a two-stage sampling approach to enable efficient selection of diverse variables from a large latent space, which is very essential for our model. Experimental results show that our model outperforms various kinds of generation models under both automatic and human evaluations.

### Relevance

Label: 

## Record 0538

Paper: A Discrete CVAE for Response Generation on Short-Text Conversation

### Question

> How does discrete latent variable has an explicit semantic meaning to improve the CVAE on short-text conversation?

### Passage

> Following previous CVAE-based generation models BIBREF14, we introduce a latent variable $z$ for each input sequence and our goal is to maximize the lower bound on the conditional data log-likelihood $p(\mathbf {y}|\mathbf {x})$, where $\mathbf {x}$ is the input query sequence and $\mathbf {y}$ is the target response sequence:
> 
> Here, $p(z|\mathbf {x})$/$q(z|\mathbf {y},\mathbf {x})$/$p(\mathbf {y}|\mathbf {x},z)$ is parameterized by the prior/posterior/generation network respectively. $D_{KL}(q(z|\mathbf {y},\mathbf {x})||p(z|\mathbf {x}))$ is the Kullback-Leibler (KL) divergence between the posterior and prior distribution. Generally, $z$ is set to follow a Gaussian distribution in both the prior and posterior networks. As mentioned in the related work, directly using the above CVAE formulation causes the low output diversity problem. This observation is also validated in the short-text conversation task in our experiments.
> 
> Now, we introduce our basic discrete CVAE formulation to alleviate the low output diversity problem. We change the continuous latent variable $z$ to a discrete latent one with an explicit interpretable meaning, which could actively control the generation of the response. An intuitive way is to connect each latent variable with a word in the vocabulary. With a sampled latent $z$ from the prior (in testing)/posterior network (in training), the generation network will take the query representation together with the word embedding of this latent variable as the input to decode the response. Here, we assume that a single word is enough to drive the generation network to output diverse responses for short text conversation, in which the response is generally short and compact.
> 
> A major advantage of our DCVAE is that for words with far different meanings, their word embeddings (especially that we use a good pre-trained word embedding corpus) generally have a large distance and drive the generation network to decode scattered responses, thus improve the output diversity. In the standard CVAE, $z$'s assumed in a continuous space may not maintain the semantic distance as in the embedding space and diverse $z$'s may point to the same semantic meaning, in which case the generation network is hard to train well with such confusing information. Moreover, we can make use of the semantic distance between latent variables to perform better sampling to approximate the objective during optimization, which will

### Relevance

Label: 

## Record 0539

Paper: A Discrete CVAE for Response Generation on Short-Text Conversation

### Question

> How does discrete latent variable has an explicit semantic meaning to improve the CVAE on short-text conversation?

### Passage

> A few works indicate that it is worth trying to apply the CVAE to dialogue generation which is originally used in image generation BIBREF16, BIBREF17 and optimized with the variational lower bound of the conditional log-likelihood. For task-oriented dialogues, BIBREF22 wen2017latent use the latent variable to model intentions in the framework of neural variational inference. For chit-chat multi-round conversations, BIBREF23 serban2017hierarchical model the generative process with multiple levels of variability based on a hierarchical sequence-to-sequence model with a continuous high-dimensional latent variable. BIBREF14 zhao2017learning make use of the CVAE and the latent variable is used to capture discourse-level variations. BIBREF24 gu2018dialogwae propose to induce the latent variables by transforming context-dependent Gaussian noise. BIBREF15 shen2017conditional present a conditional variational framework for generating specific responses based on specific attributes. Yet, it is observed in other tasks such as image captioning BIBREF25 and question generation BIBREF26 that the CVAE-based generation models suffer from the low output diversity problem, i.e. multiple sampled variables point to the same generated sequences. In this work, we utilize a discrete latent variable with an interpretable meaning to alleviate this low output diversity problem on short-text conversation.
> 
> We find that BIBREF27 zhao2018unsupervised make use of a set of discrete variables that define high-level attributes of a response. Although they interpret meanings of the learned discrete latent variables by clustering data according to certain classes (e.g. dialog acts), such latent variables still have no exact meanings. In our model, we connect each latent variable with a word in the vocabulary, thus each latent variable has an exact semantic meaning. Besides, they focus on multi-turn dialogue generation and presented an unsupervised discrete sentence representation learning method learned from the context while our concentration is primarily on single-turn dialogue generation with no context information.

### Relevance

Label: 

## Record 0540

Paper: A Discrete CVAE for Response Generation on Short-Text Conversation

### Question

> How does discrete latent variable has an explicit semantic meaning to improve the CVAE on short-text conversation?

### Passage

> Open-domain response generation BIBREF0, BIBREF1 for single-round short text conversation BIBREF2, aims at generating a meaningful and interesting response given a query from human users. Neural generation models are of growing interest in this topic due to their potential to leverage massive conversational datasets on the web. These generation models such as encoder-decoder models BIBREF3, BIBREF2, BIBREF4, directly build a mapping from the input query to its output response, which treats all query-response pairs uniformly and optimizes the maximum likelihood estimation (MLE). However, when the models converge, they tend to output bland and generic responses BIBREF5, BIBREF6, BIBREF7.
> 
> Many enhanced encoder-decoder approaches have been proposed to improve the quality of generated responses. They can be broadly classified into two categories (see Section SECREF2 for details): (1) One that does not change the encoder-decoder framework itself. These approaches only change the decoding strategy, such as encouraging diverse tokens to be selected in beam search BIBREF5, BIBREF8; or adding more components based on the encoder-decoder framework, such as the Generative Adversarial Network (GAN)-based methods BIBREF9, BIBREF10, BIBREF11 which add discriminators to perform adversarial training; (2) The second category modifies the encoder-decoder framework directly by incorporating useful information as latent variables in order to generate more specific responses BIBREF12, BIBREF13. However, all these enhanced methods still optimize the MLE of the log-likelihood or the complete log-likelihood conditioned on their assumed latent information, and models estimated by the MLE naturally favor to output frequent patterns in training data.
> 
> Instead of optimizing the MLE, some researchers propose to use the conditional variational autoencoder (CVAE), which maximizes the lower bound on the conditional data log-likelihood on a continuous latent variable BIBREF14, BIBREF15. Open-domain response generation is a one-to-many problem, in which a query can be associated with many valid responses. The CVAE-based models generally assume the latent variable follows a multivariate Gaussian distribution with a diagonal covariance matrix, which can capture the latent distribution over all valid responses. With different sampled latent variables, the model is expected to decode diverse responses. Due to the advantage of the CVAE in modeling the response generation process, we focus on improving the performance of the CVAE-based response generation models.
> 
> Although the CVAE has achieved

### Relevance

Label: 

## Record 0541

Paper: Character-Level Question Answering with Attention

### Question

> What word level and character level model baselines are used?

### Passage

> Our work is motivated by three major threads of research in machine learning and natural language processing: semantic-parsing for open-domain question answering, character-level language modeling, and encoder-decoder methods.
> 
> Semantic parsing for open-domain question answering, which translates a question into a structured KB query, is a key component in question answering with a KB. While early approaches relied on building high-quality lexicons for domain-specific databases such as GeoQuery BIBREF7 , recent work has focused on building semantic parsing frameworks for general knowledge bases such as Freebase BIBREF1 , BIBREF8 , BIBREF0 , BIBREF9 , BIBREF2 .
> 
> Semantic parsing frameworks for large-scale knowledge bases have to be able to successfully generate queries for the millions of entities and thousands of predicates in the KB, many of which are unseen during training. To address this issue, recent work relies on producing embeddings for predicates and entities in a KB based on their textual descriptions BIBREF8 , BIBREF0 , BIBREF1 , BIBREF10 . A general interaction function can then be used to measure the semantic relevance of these embedded KB entries to the question and determine the most likely KB query.
> 
> Most of these approaches use word-level embeddings to encode entities and predicates, and therefore might suffer from the out-of-vocabulary (OOV) problem when they encounter unseen words during test time. Consequently, they often rely on significant data augmentation from sources such as Paralex BIBREF2 , which contains 18 million question-paraphrase pairs scraped from WikiAnswers, to have sufficient examples for each word they encounter BIBREF11 , BIBREF1 , BIBREF0 .
> 
> As opposed to word-level modeling, character-level modeling can be used to handle the OOV issue. While character-level modeling has not been applied to factoid question answering before, it has been successfully applied to information retrieval, machine translation, sentiment analysis, classification, and named entity recognition BIBREF12 , BIBREF13 , BIBREF6 , BIBREF14 , BIBREF15 , BIBREF16 , BIBREF17 , BIBREF18 , BIBREF19 . Moreover, gflstm demonstrate that gated-feedback LSTMs on top of character-level embeddings can capture long-term dependencies in language modeling.
> 
> Lastly, encoder-decoder networks have been applied to many structured machine learning tasks. First introduced in sutskever2014sequence, in an encoder-decoder network, a source sequence is first encoded with a recurrent neural

### Relevance

Label: 

## Record 0542

Paper: Character-Level Question Answering with Attention

### Question

> What word level and character level model baselines are used?

### Passage

> the mention of a predicate that is interrupted by entity mentions. We also note that predicate attention often peaks at the padding symbols after the last character of the question, possibly because sentence endings carry extra information that further help disambiguate predicate mentions. In certain scenarios, the network may only have sufficient information to build a semantic representation of the predicate after being ensured that it reached the end of a sentence. Finally, certain words in the question help identify both the entity and the predicate. For example, consider the word university in the question What type of educational institution is eastern new mexico university (Figure 2c). Although it is a part of the entity mention, it also helps disambiguate the predicate. However, previous semantic parsing-based QA approaches BIBREF10 , BIBREF1 assume that there is a clear separation between the predicate and entity mentions in the question. In contrast, the proposed model does not need to make this hard categorization, and attends the word university when predicting both the entity and predicate.

### Relevance

Label: 

## Record 0543

Paper: Character-Level Question Answering with Attention

### Question

> What word level and character level model baselines are used?

### Passage

> We evaluate the proposed model on the SimpleQuestions dataset BIBREF0 . The dataset consists of 108,442 single-relation questions and their corresponding (topic entity, predicate, answer entity) triples from Freebase. It is split into 75,910 train, 10,845 validation, and 21,687 test questions. Only 10,843 of the 45,335 unique words in entity aliases and 886 out of 1,034 unique predicates in the test set were present in the train set. For the proposed dataset, there are two evaluation settings, called FB2M and FB5M, respectively. The former uses a KB for candidate generation which is a subset of Freebase and contains 2M entities, while the latter uses subset of Freebase with 5M entities.
> 
> In our experiments, the Memory Neural Networks (MemNNs) proposed in babidataset serve as the baselines. For training, in addition to the 76K questions in the training set, the MemNNs use 3K training questions from WebQuestions BIBREF27 , 15M paraphrases from WikiAnswers BIBREF2 , and 11M and 12M automatically generated questions from the KB for the FB2M and FB5M settings, respectively. In contrast, our models are trained only on the 76K questions in the training set.
> 
> For our model, both layers of the LSTM-based question encoder have size 200. The hidden layers of the LSTM-based decoder have size 100, and the CNNs for entity and predicate embeddings have a hidden layer of size 200 and an output layer of size 100. The CNNs for entity and predicate embeddings use a receptive field of size 4, $\lambda =5$ , and $m=100$ . We train the models using RMSProp with a learning rate of $1e^{-4}$ .
> 
> In order to make the input character sequence long enough to fill up the receptive fields of multiple CNN layers, we pad each predicate or entity using three padding symbols $P$ , a special start symbol, and a special end symbol. For instance, $Obama$ would become $S_{start}PPP ObamaPPPS_{end}$ . For consistency, we apply the same padding to the questions.

### Relevance

Label: 

## Record 0544

Paper: Character-Level Question Answering with Attention

### Question

> What word level and character level model baselines are used?

### Passage

> We randomly sampled 50 questions where the best-performing model generated the wrong KB query and categorized the errors. For 46 out of the 50 examples, the model predicted a predicate with a very similar alias to the true predicate, i.e. /music/release/track vs. /music/release/track_list. For 21 out of the 50 examples, the model predicted the wrong entity, e.g., Album vs. Still Here for the question What type of album is still here?. Finally, for 18 of the 50 examples, the model predicted the wrong entity and predicate, i.e. (Play, /freebase/equivalent_topic/equivalent_type) for the question which instrument does amapola cabase play? Training on more data, augmenting the negative sample set with words from the question that are not an entity mention, and having more examples that disambiguate between similar predicates may ameliorate many of these errors.

### Relevance

Label: 

## Record 0545

Paper: Character-Level Question Answering with Attention

### Question

> What word level and character level model baselines are used?

### Passage

> Following babidataset, we report results on the SimpleQuestions dataset in terms of SQ accuracy, for both FB2M and FB5M settings in Table 1. SQ accuracy is defined as the percentage of questions for which the model generates a correct KB query (i.e., both the topic entity and predicate are correct). Our single character-level model achieves SQ accuracies of 70.9% and 70.3% on the FB2M and FB5M settings, outperforming the previous state-of-art results by 8.2% and 6.4%, respectively. Compared to the character-level model, which only has 1.2M parameters, our word-level model has 19.9M parameters, and only achieves a best SQ accuracy of 53.9%. In addition, in contrast to previous work, the OOV issue is much more severe for our word-level model, since we use no data augmentation to cover entities unseen in the train set.

### Relevance

Label: 

## Record 0546

Paper: UTCNN: a Deep Learning Model of Stance Classificationon on Social Media Text

### Question

> What are the baselines?

### Passage

> hold the same stance to like them – is reliable, we examine the likes from authors of different stances. Posts in FBFans dataset are used for this analysis. We calculate the like statistics of each distinct author from these 32,595 posts. As the numbers of authors in the Sup, Neu and Uns stances are largely imbalanced, these numbers are normalized by the number of users of each stance. Table TABREF13 shows the results. Posts with stances (i.e., not neutral) attract users of the same stance. Neutral posts also attract both supportive and neutral users, like what we observe in supportive posts, but just the neutral posts can attract even more neutral likers. These results do suggest that users prefer posts of the same stance, or at least posts of no obvious stance which might cause annoyance when reading, and hence support the user modeling in our approach.
> 
> The CreateDebate dataset was collected from an English online debate forum discussing four topics: abortion (ABO), gay rights (GAY), Obama (OBA), and marijuana (MAR). The posts are annotated as for (F) and against (A). Replies to posts in this dataset are also labeled with stance and hence use the same data format as posts. The labeling results are shown in the right-hand side of Table TABREF12 . We observe that the dataset is more balanced than the FBFans dataset. In addition, there are 977 unique users in the dataset. To compare with Hasan and Ng's work, we conducted five-fold cross-validation and present the annotation results as the average number of all folds BIBREF9 , BIBREF5 .
> 
> The FBFans dataset has more integrated functions than the CreateDebate dataset; thus our model can utilize all linguistic and extra-linguistic features. For the CreateDebate dataset, on the other hand, the like and comment features are not available (as there is a stance label for each reply, replies are evaluated as posts as other previous work) but we still implemented our model using the content, author, and topic information.

### Relevance

Label: 

## Record 0547

Paper: UTCNN: a Deep Learning Model of Stance Classificationon on Social Media Text

### Question

> What are the baselines?

### Passage

> As shown in Figure FIGREF4 , we use a general CNN BIBREF3 and two semantic transformations for document composition . We are given a document with an engaged user INLINEFORM0 , a topic INLINEFORM1 , and its composite INLINEFORM2 words, each word INLINEFORM3 of which is associated with a word embedding INLINEFORM4 where INLINEFORM5 is the vector dimension. For each word embedding INLINEFORM6 , we apply two dot operations as shown in Equation EQREF6 : DISPLAYFORM0
> 
> where INLINEFORM0 models the user reading preference for certain semantics, and INLINEFORM1 models the topic semantics; INLINEFORM2 and INLINEFORM3 are the dimensions of transformed user and topic embeddings respectively. We use INLINEFORM4 to model semantically what each user prefers to read and/or write, and use INLINEFORM5 to model the semantics of each topic. The dot operation of INLINEFORM6 and INLINEFORM7 transforms the global representation INLINEFORM8 to a user-dependent representation. Likewise, the dot operation of INLINEFORM9 and INLINEFORM10 transforms INLINEFORM11 to a topic-dependent representation.
> 
> After the two dot operations on INLINEFORM0 , we have user-dependent and topic-dependent word vectors INLINEFORM1 and INLINEFORM2 , which are concatenated to form a user- and topic-dependent word vector INLINEFORM3 . Then the transformed word embeddings INLINEFORM4 are used as the CNN input. Here we apply three convolutional layers on the concatenated transformed word embeddings INLINEFORM5 : DISPLAYFORM0
> 
> where INLINEFORM0 is the index of words; INLINEFORM1 is a non-linear activation function (we use INLINEFORM2 ); INLINEFORM5 is the convolutional filter with input length INLINEFORM6 and output length INLINEFORM7 , where INLINEFORM8 is the window size of the convolutional operation; and INLINEFORM9 and INLINEFORM10 are the output and bias of the convolution layer INLINEFORM11 , respectively. In our experiments, the three window sizes INLINEFORM12 in the three convolution layers are one, two, and three, encoding unigram, bigram, and trigram semantics accordingly.
> 
> After the convolutional layer, we add a maximum pooling layer among convolutional outputs to obtain the unigram, bigram, and trigram n-gram representations. This is succeeded by an average pooling layer for an element-wise average of the three maximized convolution outputs.

### Relevance

Label: 

## Record 0548

Paper: UTCNN: a Deep Learning Model of Stance Classificationon on Social Media Text

### Question

> What are the baselines?

### Passage

> We start with the experimental dataset and then describe the training process as well as the implementation of the baselines. We also implement several variations to reveal the effects of features: authors, likers, comment, and commenters. In the results section we compare our model with related work.

### Relevance

Label: 

## Record 0549

Paper: UTCNN: a Deep Learning Model of Stance Classificationon on Social Media Text

### Question

> What are the baselines?

### Passage

> We tested the proposed UTCNN on two different datasets: FBFans and CreateDebate. FBFans is a privately-owned, single-topic, Chinese, unbalanced, social media dataset, and CreateDebate is a public, multiple-topic, English, balanced, forum dataset. Results using these two datasets show the applicability and superiority for different topics, languages, data distributions, and platforms.
> 
> The FBFans dataset contains data from anti-nuclear-power Chinese Facebook fan groups from September 2013 to August 2014, including posts and their author and liker IDs. There are a total of 2,496 authors, 505,137 likers, 33,686 commenters, and 505,412 unique users. Two annotators were asked to take into account only the post content to label the stance of the posts in the whole dataset as supportive, neutral, or unsupportive (hereafter denoted as Sup, Neu, and Uns). Sup/Uns posts were those in support of or against anti-reconstruction; Neu posts were those evincing a neutral standpoint on the topic, or were irrelevant. Raw agreement between annotators is 0.91, indicating high agreement. Specifically, Cohen’s Kappa for Neu and not Neu labeling is 0.58 (moderate), and for Sup or Uns labeling is 0.84 (almost perfect). Posts with inconsistent labels were filtered out, and the development and testing sets were randomly selected from what was left. Posts in the development and testing sets involved at least one user who appeared in the training set. The number of posts for each stance is shown on the left-hand side of Table TABREF12 . About twenty percent of the posts were labeled with a stance, and the number of supportive (Sup) posts was much larger than that of the unsupportive (Uns) ones: this is thus highly skewed data, which complicates stance classification. On average, 161.1 users were involved in one post. The maximum was 23,297 and the minimum was one (the author). For comments, on average there were 3 comments per post. The maximum was 1,092 and the minimum was zero.
> 
> To test whether the assumption of this paper – posts attract users who hold the same stance to like them – is reliable, we examine the likes from authors of different stances. Posts in FBFans dataset are used for this analysis. We calculate the like statistics of each distinct author from these 32,595

### Relevance

Label: 

## Record 0550

Paper: UTCNN: a Deep Learning Model of Stance Classificationon on Social Media Text

### Question

> What are the baselines?

### Passage

> We pit our model against the following baselines: 1) SVM with unigram, bigram, and trigram features, which is a standard yet rather strong classifier for text features; 2) SVM with average word embedding, where a document is represented as a continuous representation by averaging the embeddings of the composite words; 3) SVM with average transformed word embeddings (the INLINEFORM0 in equation EQREF6 ), where a document is represented as a continuous representation by averaging the transformed embeddings of the composite words; 4) two mature deep learning models on text classification, CNN BIBREF3 and Recurrent Convolutional Neural Networks (RCNN) BIBREF0 , where the hyperparameters are based on their work; 5) the above SVM and deep learning models with comment information; 6) UTCNN without user information, representing a pure-text CNN model where we use the same user matrix and user embeddings INLINEFORM1 and INLINEFORM2 for each user; 7) UTCNN without the LDA model, representing how UTCNN works with a single-topic dataset; 8) UTCNN without comments, in which the model predicts the stance label given only user and topic information. All these models were trained on the training set, and parameters as well as the SVM kernel selections (linear or RBF) were fine-tuned on the development set. Also, we adopt oversampling on SVMs, CNN and RCNN because the FBFans dataset is highly imbalanced.

### Relevance

Label: 

## Record 0551

Paper: A Transformer-based approach to Irony and Sarcasm detection

### Question

> How are the three different forms defined in this work?

### Passage

> in most of the cases, are characterized by an oppositeness to the literal language context. It is crucial to distinguish between the literal meaning of an expression considered as a whole from its constituents’ words and phrases. As literal meaning is assumed to be invariant in all context at least in its classical conceptualization BIBREF25, it is exactly this separation of an expression from its context that permits and opens the road to computational approaches in detecting and characterizing FL utterance.
> 
> We may identify three common FL expression forms namely, irony, sarcasm and metaphor. In this paper, figurative expressions, and especially ironic or sarcastic ones, are considered as a way of indirect denial. From this point of view, the interpretation and ultimately identification of the indirect meaning involved in a passage does not entail the cancellation of the indirectly rejected message and its replacement with the intentionally implied message (as advocated in BIBREF26, BIBREF27). On the contrary ironic/sarcastic expressions presupposes the processing of both the indirectly rejected and the implied message so that the difference between them can be identified. This view differs from the assumption that irony and sarcasm involve only one interpretation BIBREF28, BIBREF29. Holding that irony activates both grammatical / explicit as well as ironic / involved notions provides that irony will be more difficult to grasp than a non-ironic use of the same expression.
> 
> Despite that all forms of FL are well studied linguistic phenomena BIBREF28, computational approaches fail to identify the polarity of them within a text. The influence of FL in sentiment classification emerged both on SemEval-2014 Sentiment Analysis task BIBREF12 and BIBREF19. Results show that Natural Language Processing (NLP) systems effective in most other tasks see their performance drop when dealing with figurative forms of language. Thus, methods capable of detecting, separating and classifying forms of FL would be valuable building blocks for a system that could ultimately provide a full-spectrum sentiment analysis of natural language.
> 
> In literature we encounter some major drawbacks of previous studies and we aim to resolve with our proposed method:
> 
> Many studies tackle figurative language by utilizing a wide range of engineered features (e.g. lexical and sentiment based features) BIBREF30, BIBREF31, BIBREF0, BIBREF32,

### Relevance

Label: 

## Record 0552

Paper: A Transformer-based approach to Irony and Sarcasm detection

### Question

> How are the three different forms defined in this work?

### Passage

> we encounter some major drawbacks of previous studies and we aim to resolve with our proposed method:
> 
> Many studies tackle figurative language by utilizing a wide range of engineered features (e.g. lexical and sentiment based features) BIBREF30, BIBREF31, BIBREF0, BIBREF32, BIBREF33, BIBREF34 making classification frameworks not feasible.
> 
> Several approaches search words on large dictionaries which demand large computational times and can be considered as impractical BIBREF0, BIBREF34
> 
> Many studies exhausting preprocess the input texts, including stemming, tagging, emoji processing etc. that tend to be time consuming especially in large datasets BIBREF35, BIBREF36.
> 
> Many approaches attempt to create datasets using social media API’s to automatically collect data rather than exploiting their system on benchmark datasets, with proven quality. To this end, it is impossible to be compared and evaluated BIBREF35, BIBREF37, BIBREF36.
> 
> To tackle the aforementioned problems, we propose an end-to-end methodology containing none hand crafted engineered features or lexicon dictionaries, a preprocessing step that includes only de-capitalization and we evaluate our system on several benchmark dataset. To the best of our knowledge, this is the first time that an unsupervised pre-trained Transformer method is used to capture figurative language in many of its forms.
> 
> The rest of the paper is structured as follows, in Section SECREF2 we present the related work on the field of FL detection, in Section SECREF3 we present our proposed method along with several state-of-the-art models that achieve high performance in a wide range of NLP tasks which will be used to compare performance, the results of our experiments are presented in Section SECREF4, and finally our conclusion is in Section SECREF5.

### Relevance

Label: 

## Record 0553

Paper: A Transformer-based approach to Irony and Sarcasm detection

### Question

> How are the three different forms defined in this work?

### Passage

> In this study, we propose the first transformer based methodology, leveraging the pre-trained RoBERTa model combined with a recurrent convolutional neural network, to tackle figurative language in social media. Our network is compared with all, to the best of our knowledge, published approaches under four different benchmark dataset. In addition, we aim to minimize preprocessing and engineered feature extraction steps which are, as we claim, unnecessary when using overly trained deep learning methods such as transformers. In fact, hand crafted features along with preprocessing techniques such as stemming and tagging on huge datasets containing thousands of samples are almost prohibited in terms of their computation cost. Our proposed model, RCNN-RoBERTa, achieve state-of-the-art performance under six metrics over four benchmark dataset, denoting that transfer learning non-literal forms of language. Moreover, RCNN-RoBERTa model outperforms all other state-of-the-art approaches tested including BERT, XLnet, ELMo, and USE under all metric, some by a large factor.

### Relevance

Label: 

## Record 0554

Paper: A Transformer-based approach to Irony and Sarcasm detection

### Question

> How are the three different forms defined in this work?

### Passage

> Although the NLP community have researched all aspects of FL independently, none of the proposed systems were evaluated on more than one type. Related work on FL detection and classification tasks could be categorized into two main categories, according to the studied task: (a) irony and sarcasm detection, and (b) sentiment analysis of FL excerpts. Even if sarcasm and irony are not identical phenomenons, we will present those types together, as they appear in the literature.

### Relevance

Label: 

## Record 0555

Paper: A Transformer-based approach to Irony and Sarcasm detection

### Question

> How are the three different forms defined in this work?

### Passage

> text lack in detecting sentiment polarity on sarcastic and ironic expressions, as already signified in the relevant “SemEval-2014 Sentiment Analysis task 9” BIBREF12. Moreover, lacking of facial expressions and voice tone require context aware approaches to tackle such a challenging task and overcome its ambiguities BIBREF13. As sentiment is the emotion behind customer engagement, SA finds its realization in automated customer aware services, elaborating over user’s emotional intensities BIBREF14. Most of the related studies utilize single turn texts from topic specific sources, such as Twitter, Amazon, IMDB etc. Hand crafted and sentiment-oriented features, indicative of emotion polarity, are utilized to represent respective excerpt cases. The formed data are then fed traditional machine learning classifiers (e.g. SVM, Random Forest, multilayer perceptrons) or DL techniques and respective complex neural architectures, in order to induce analytical models that are able to capture the underlying sentiment content and polarity of passages BIBREF15, BIBREF16, BIBREF17.
> 
> The linguistic phenomenon of figurative language (FL) refers to the contradiction between the literal and the non-literal meaning of an utterance BIBREF18. Literal written language assigns ‘exact’ (or ‘real’) meaning to the used words (or phrases) without any reference to putative speech figures. In contrast, FL schemas exploit non-literal mentions that deviate from the exact concept presented by the used words and phrases. FL is rich of various linguistic phenomena like ‘metonymy’ reference to an entity stands for another of the same domain, a more general case of ‘synonymy’; and ‘metaphors’ systematic interchange between entities from different abstract domains BIBREF19. Besides the philosophical considerations, theories and debates about the exact nature of FL, findings from the neuroscience research domain present clear evidence on the presence of differentiating FL processing patterns in the human brain BIBREF20, BIBREF21, BIBREF22, BIBREF23, BIBREF14, even for woman-man attraction situations! BIBREF24. A fact that makes FL processing even more challenging and difficult to tackle. Indeed, this is the case of pragmatic FL phenomena like irony and sarcasm that main intention of in most of the cases, are characterized by an oppositeness to the literal language context. It is crucial to distinguish between the literal meaning of an expression considered as a whole from its constituents’ words and phrases. As literal meaning

### Relevance

Label: 

## Record 0556

Paper: Measuring Compositional Generalization: A Comprehensive Method on Realistic Data

### Question

> What three machine architectures are analyzed?

### Passage

> The mean accuracies of the three architectures on CFQ are shown in Figure FIGREF28(a) and Table TABREF29. We make three main observations:
> 
> All models achieve an accuracy larger than 95% on a random split, and this is true even if they are trained on 10 times fewer training instances (see Appendix SECREF15 for a more detailed analysis on the performance with varying training size).
> 
> The mean accuracy on the MCD splits is below 20% for all architectures, which means that even a large train set (about 96k instances) with a similar distribution of atoms between train and test is not sufficient for these architectures to perform well on the test distribution.
> 
> For all architectures, there is a strong negative correlation between the compound divergence and the mean accuracy.
> 
> This suggests that the baseline models are able to capture the superficial structure of the dataset, but fail to capture the compositional structure. We find it surprising that varying the compound divergence gives direct control of the (mean) accuracy, even though the examples in train and test look similar (see Appendix SECREF91). This means that compound divergence seems to capture the core difficulty for these ML architectures to generalize compositionally.
> 
> Note that the experiment based on output-length exhibits a worse accuracy than what we would expect based on its compositional divergence. One explanation for this is that the test distribution varies from the training distribution in other ways than compound divergence (namely in output length and a slightly higher atom divergence), which seems to make this split particularly difficult for the baseline architectures. To analyze the influence of the length ratio further, we compute the correlation between length ratios and accuracy of the baseline systems and compare it to the correlation between compound divergence and accuracy. We observe $R^2$ correlation coefficients between 0.11 and 0.22 for the input and output length ratios and between 0.81 and 0.88 for the compound divergence. This shows that despite the known phenomenon that the baseline systems struggle to generalize to longer lengths, the compound divergence seems to be a stronger explanation for the accuracy on different splits than the lengths ratios.
> 
> Error analysis. We perform an analysis of the errors for

### Relevance

Label: 

## Record 0557

Paper: Measuring Compositional Generalization: A Comprehensive Method on Realistic Data

### Question

> What three machine architectures are analyzed?

### Passage

> In this paper we presented what is (to the best of our knowledge) the largest and most comprehensive benchmark for compositional generalization on a realistic NLU task. It is based on a new dataset generated via a principled rule-based approach and a new method of splitting the dataset by optimizing the divergence of atom and compound distributions between train and test sets. The performance of three baselines indicates that in a simple but realistic NLU scenario, state-of-the-art learning systems fail to generalize compositionally even if they are provided with large amounts of training data and that the mean accuracy is strongly correlated with the compound divergence.
> 
> We hope our work will inspire others to use this benchmark as a yardstick to advance the compositional generalization capabilities of learning systems and achieve high accuracy at high compound divergence. Some specific directions that we consider promising include applying unsupervised pretraining on the input language or output queries and the use of more diverse or more targeted learning architectures, such as syntactic attention BIBREF7. We also believe it would be interesting to apply the DBCA approach to other domains such as visual reasoning, e.g. based on clevr BIBREF3.
> 
> In the area of compositionality benchmarks, we are interested in determining the performance of current architectures on the end-to-end task that expects a natural language answer given a natural language question in CFQ. We would like also to extend our approach to broader subsets of language understanding, including use of ambiguous constructs, negations, quantification, comparatives, additional languages, and other vertical domains.

### Relevance

Label: 

## Record 0558

Paper: Measuring Compositional Generalization: A Comprehensive Method on Realistic Data

### Question

> What three machine architectures are analyzed?

### Passage

> dataset split for measuring compositional generalization and to construct splits that are ideally suited for this purpose (Section SECREF2).
> 
> We present the Compositional Freebase Questions (CFQ) , a simple yet realistic and large NLU dataset that is specifically designed to measure compositional generalization using the DBCA method, and we describe how to construct such a dataset (Section SECREF3).
> 
> We use the DBCA method to construct a series of experiments for measuring compositionality on CFQ and scan BIBREF2 and to quantitatively compare these experiments to other compositionality experiments (Section SECREF4).
> 
> We analyze the performance of three baseline ML architectures on these experiments and show that these architectures fail to generalize compositionally, and perhaps more surprisingly, that compound divergence between train and test sets is a good predictor of the test accuracy (Section SECREF5).

### Relevance

Label: 

## Record 0559

Paper: Measuring Compositional Generalization: A Comprehensive Method on Realistic Data

### Question

> What three machine architectures are analyzed?

### Passage

> Below we qualitatively analyze a number of instances the models fail on. We anonymize the MIDs in the same way as the data is provided to the models (see Section SECREF5). We first select queries on which all machine learning systems fail in all replicated runs (about 5k instances out of a total of about 12k), and then randomly select queries from this list. In the following we discuss a few cases in more detail. Note that, for readability, we use the following abbreviations for the sparql properties in Query 1:
> 
> ns:people.person.child = ns:people.person.children|
> 
> ns:fictional_universe.fictional_character.children|
> 
> ns:organization.organization.child/
> 
> ns:organization.organization_relationship.child
> 
> ns:people.person.sibling = ns:people.person.siblings/
> 
> ns:people.siblingrelationship.sibling|
> 
> ns:fictionaluniverse.fictionalcharacter.siblings/
> 
> ns:fictionaluniverse.
> 
> siblingrelationshipoffictionalcharacters.siblings
> 
> Query 1: “What sibling of M0 was M1' s parent?”
> 
> Golden (correct) sparql query:
> 
> SELECT DISTINCT ?x0 WHERE {
> 
> ?x0 ns:people.person.child M1 .
> 
> ?x0 ns:people.person.sibling M0 .
> 
> FILTER ( ?x0 != M0 )
> 
> }
> 
> Inferred (system) sparql query:
> 
> SELECT DISTINCT ?x0 WHERE {
> 
> ?x0 ns:people.person.sibling ?x1 .
> 
> ?x0 ns:people.person.sibling M0 .
> 
> ?x1 ns:people.person.child M1 .
> 
> FILTER ( ?x0 != ?x1 )
> 
> }
> 
> Analysis. The meaning of the sparql query generated by the system is “What sibling of M0 was a sibling of M1's parent?”, which is incorrect. We next analyze the train set, in order to show that we believe enough information has been provided in the train set for the question to be answered correctly.
> 
> Some subqueries of the query and their occurrences are shown in Table TABREF140. While the exact subquery “What sibling” does not occur at training, the two words have been shown separately in many instances: the subqueries “sibling of Mx”, and “Mx's parent” occur 2,331 and 1,222 times, respectively. We can analyze this example in more detail by comparing parts of the rule tree of this example with those shown at training. As can be read from the table, similar sentences have been shown during training. Some examples are:
> 
> What was executive produced by and written by a sibling of M0?
> 
> What costume designer did M1's parent employ?
> 
> What cinematographer was a film editor that M2 and M3 married?
> 
> What film director was a character influenced by M2?
> 
> Query 2: “Did a male film director edit and direct M0 and M1?”
> 
> Golden (correct) sparql query:
> 
> SELECT

### Relevance

Label: 

## Record 0560

Paper: Measuring Compositional Generalization: A Comprehensive Method on Realistic Data

### Question

> What three machine architectures are analyzed?

### Passage

> Figure FIGREF150 shows a scatter plot of accuracy vs. compound divergence for the three baseline architectures (see Section SECREF5) on existing splits of the scan data. These splits are discussed in BIBREF2 and BIBREF6, and the exact split data is available. (Data splits obtained from https://github.com/brendenlake/SCAN). We map these splits onto the re-created scan data, which enables us to measure the atom and compound divergences. The authors present a total of six split experiments (some with several sub-experiments):
> 
> BIBREF2:
> 
> simple (random)
> 
> by action sequence length
> 
> adding a primitive and adding a primitive along with complex combinations
> 
> BIBREF6:
> 
> adding a template
> 
> adding template fillers
> 
> adding more training examples of fillers (fewshot)
> 
> In the plot, we omit some data points that are too close to be distinguished easily. The point labels have the form `(abbreviated experiment name)<(parameter)>@(number of samples) (baseline system abbreviation) [(train set size fraction), (split atom divergence)]'. The train set size fraction is given as a percentage of the overall data size. The baseline system abbreviations are LSTM, T for Transformer, UT for Universal Transformer, T/UT where both transformer models are indistinguishable, and empty where all three systems perform indistinguishably. The abbreviated experiment name is one of the names in italics above.
> 
> We can observe a strong dependency of the accuracies on the compound divergence of the data split. Again, this seems to indicate that the compound divergence is correlated with accuracy for these baseline architectures. One difference to the data shown in Figure FIGREF28(b) is that for this set of experiments the accuracy drops faster with increasing compound divergence. One explanation for this effect is that the experiments are directly aimed at highlighting one specific potentially problematic scenario for learning. E.g. in the experiment `primitive<jump>' (with very low accuracies for all three systems) the jump command is shown exactly in one combination (namely alone) in the training data while it occurs in all test examples in arbitrary combinations.
> 
> This is reflected in the higher atom divergence value of 0.08 for this split, as well as in all other splits that exhibit a low accuracy at a low compound divergence in Figure FIGREF150. Note that BIBREF2 already compare the experiment `primitive<jump>' to the experiment `primitive<turn

### Relevance

Label: 

## Record 0561

Paper: Unsupervised Learning of Style-sensitive Word Vectors

### Question

> How large is the dataset?

### Passage

> Analyzing and generating natural language texts requires the capturing of two important aspects of language: what is said and how it is said. In the literature, much more attention has been paid to studies on what is said. However, recently, capturing how it is said, such as stylistic variations, has also proven to be useful for natural language processing tasks such as classification, analysis, and generation BIBREF1 , BIBREF2 , BIBREF3 .
> 
> This paper studies the stylistic variations of words in the context of the representation learning of words. The lack of subjective or objective definitions is a major difficulty in studying style BIBREF4 . Previous attempts have been made to define a selected aspect of the notion of style (e.g., politeness) BIBREF5 , BIBREF6 , BIBREF7 , BIBREF8 , BIBREF9 , BIBREF10 ; however, it is not straightforward to create strict guidelines for identifying the stylistic profile of a given text. The systematic evaluations of style-sensitive word representations and the learning of style-sensitive word representations in a supervised manner are hampered by this. In addition, there is another trend of research forward controlling style-sensitive utterance generation without defining the style dimensions BIBREF11 , BIBREF12 ; however, this line of research considers style to be something associated with a given specific character, i.e., a persona, and does not aim to capture the stylistic variation space.
> 
> The contributions of this paper are three-fold. (1) We propose a novel architecture that acquires style-sensitive word vectors (Figure 1 ) in an unsupervised manner. (2) We construct a novel dataset for style, which consists of pairs of style-sensitive words with each pair scored according to its stylistic similarity. (3) We demonstrate that our word vectors capture the stylistic similarity between two words successfully. In addition, our training script and dataset are available on https://jqk09a.github.io/style-sensitive-word-vectors/.

### Relevance

Label: 

## Record 0562

Paper: Unsupervised Learning of Style-sensitive Word Vectors

### Question

> How large is the dataset?

### Passage

> To verify that our models capture the stylistic similarity, we evaluated our style-sensitive vector $\mbox{$x$}_{w_t}$ by comparing to other word vectors on a novel artificial task matching human stylistic similarity judgments. For this evaluation, we constructed a novel dataset with human judgments on the stylistic similarity between word pairs by performing the following two steps. First, we collected only style-sensitive words from the test corpus because some words are strongly associated with stylistic aspects BIBREF15 , BIBREF16 and, therefore, annotating random words for stylistic similarity is inefficient. We asked crowdsourced workers to select style-sensitive words in utterances. Specifically, for the crowdsourced task of picking “style-sensitive” words, we provided workers with a word-segmented utterance and asked them to pick words that they expected to be altered within different situational contexts (e.g., characters, moods, purposes, and the background cultures of the speaker and listener.). Then, we randomly sampled $1,000$ word pairs from the selected words and asked 15 workers to rate each of the pairs on five scales (from $-2$ : “The style of the pair is different” to $+2$ : “The style of the pair is similar”), inspired by the syntactic/semantic similarity dataset BIBREF17 , BIBREF18 . Finally, we picked only word pairs featuring clear worker agreement in which more than 10 annotators rated the pair with the same sign, which consisted of random pairs of highly agreeing style-sensitive words. Consequently, we obtained 399 word pairs with similarity scores. To our knowledge, this is the first study that created an evaluation dataset to measure the lexical stylistic similarity.
> 
> In the task of selecting style-sensitive words, the pairwise inter-annotator agreement was moderate (Cohen's kappa $\kappa $ is $0.51$ ). In the rating task, the pairwise inter-annotator agreement for two classes ( $\lbrace -2, -1\rbrace $ or $\lbrace +1, +2\rbrace $ ) was fair (Cohen's kappa $\kappa $ is $0.23$ ). These statistics suggest that, at least in Japanese, native speakers share a sense of style-sensitivity of words and stylistic similarity between style-sensitive words.
> 
> We used this evaluation dataset to compute the Spearman rank correlation ( $\rho _{style}$ ) between the cosine similarity scores between the learned word vectors $\cos (\mbox{$v$}_{w}, \mbox{$v$}_{w^{\prime }})$ and the human judgements. Table

### Relevance

Label: 

## Record 0563

Paper: Unsupervised Learning of Style-sensitive Word Vectors

### Question

> How large is the dataset?

### Passage

> Let $w_{t}$ denote the target word (token) in the corpora and $\mathcal {U}_t = \lbrace w_1, \dots , w_{t-1}, w_t, w_{t+1},\dots , w_{\vert \mathcal {U}_t \vert }\rbrace $ denote the utterance (word sequence) including $w_t$ . Here, $w_{t+d}$ or $w_{t-d} \in \mathcal {U}_t$ is a context word of $w_t$ (e.g., $w_{t+1}$ is the context word next to $w_{t}$ ), where $d\in \mathbb {N}_{>0}$ is the distance between the context words and the target word $w_t$ .
> 
> For each word (token) $w$ , bold face $\mbox{$v$}_{w}$ and $\tilde{\mbox{$v$}}_{w}$ denote the vector of $w$ and the vector predicting the word $w$ . Let $\mathcal {V}$ denote the vocabulary.

### Relevance

Label: 

## Record 0564

Paper: Unsupervised Learning of Style-sensitive Word Vectors

### Question

> How large is the dataset?

### Passage

> CBOW is designed to learn the semantic and syntactic aspects of words from their nearby context BIBREF13 . However, an interesting problem is determining the location where the stylistic aspects of words can be captured. To address this problem, we start with the assumption that a style persists throughout each single utterance in a dialog, that is, the stylistic profile of a word in an utterance must be consistent with other words in the same utterance. Based on this assumption, we propose extending CBOW to use all the words in an utterance as context,
> 
> $$ := \lbrace w_{t\pm d} \in \mathcal {U}_t \mid 1\le d\rbrace 
> \text{,}$$   (Eq. 7)
> 
> instead of only the nearby words. Namely, we expand the context window from a fixed width to the entire utterance. This training strategy is expected to lead to learned word vectors that are more sensitive to style rather than to other aspects. We refer to this version as CBOW-all-ctx.

### Relevance

Label: 

## Record 0565

Paper: Unsupervised Learning of Style-sensitive Word Vectors

### Question

> How large is the dataset?

### Passage

> Finally, to further understand what types of features our CBOW-sep-ctx model acquired, we show some words with the four most similar words in Table 2 . Here, for English readers, we also report a result for English. The English result also shows an example of the performance of our model on another language. The left side of Table 2 (for stylistic vector $\mbox{$x$}$ ) shows the results. We found that the Japanese word “UTF8ipxm拙者 (I; classical)” is similar to “UTF8ipxmござる (be; classical)” or words containing it (the second row of Table 2 ). The result looks reasonable, because words such as “UTF8ipxm拙者 (I; classical)” and “UTF8ipxmござる (be; classical)” are typically used by Japanese Samurai or Ninja. We can see that the vectors captured the similarity of these words, which are stylistically consistent across syntactic and semantic varieties. Conversely, the right side of the table (for the syntactic/semantic vector $\mbox{$y$}$ ) shows that the word “UTF8ipxm拙者 (I; classical)” is similar to the personal pronoun (e.g., “UTF8ipxm僕 (I; male, childish)”). We further confirmed that 15 the top similar words are also personal pronouns (even though they are not shown due to space limitations). These results indicate that the proposed CBOW-sep-ctx model jointly learns two different types of lexical similarities, i.e., the stylistic and syntactic/semantic similarities in the different parts of the vectors. However, our stylistic vector also captured the topic similarity, such as “UTF8ipxmサンタ (Santa Clause)” and “UTF8ipxmトナカイ (reindeer)” (the fourth row of Table 2 ). Therefore, there is still room for improvement in capturing the stylistic similarity.

### Relevance

Label: 

## Record 0566

Paper: Evaluating Multimodal Representations on Sentence Similarity: vSTS, Visual Semantic Textual Similarity Dataset

### Question

> What is the size of the dataset?

### Passage

> The dataset is derived from a subset of the caption pairs already annotated in the Semantic Textual Similarity Task (see below). We selected some caption pairs with their similarity annotations, and added the images corresponding to each caption. While the human annotators had access to only the text, we provide the system with both the caption and corresponding image, to check whether the visual representations can be exploited by the system to solve a text understanding and inference task.
> 
> As the original dataset contained captions referring to the same image, and the task would be trivial for pairs of the same image, we filtered those out, that is, we only consider caption pairs that refer to different images. In total, the dataset comprises 829 instances, each instance containing a pair of images and their description, as well as a similarity value that ranges from 0 to 5. The instances are derived from the following datasets:
> 
> Subset 2014 This subset is derived from the Image Descriptions dataset which is a subset of the PASCAL VOC-2008 dataset BIBREF16 . PASCAL VOC-2008 dataset consists of 1,000 images and has been used by a number of image description systems. In total, we obtained 374 pairs (out of 750 in the original file).
> 
> Subset 2015 The subset is derived from Image Descriptions dataset, which is a subset of 8k-picture of Flickr. 8k-Flicker is a benchmark collection for sentence-based image description, consisting of 8,000 images that are each paired with five different captions which provide clear descriptions of the salient entities and events. We obtained 445 pairs (out of 750 in the original).
> 
> Score distribution Due to the caption pairs are generated from different images, strong bias towards low scores is expected (see Figure FIGREF3 ). We measured the score distribution in the two subsets separately and jointly, and see that the two subsets follow same distribution. As expected, the most frequent score is 0 (Table TABREF2 ), but the dataset still shows wide range of similarity values, with enough variability.

### Relevance

Label: 

## Record 0567

Paper: Evaluating Multimodal Representations on Sentence Similarity: vSTS, Visual Semantic Textual Similarity Dataset

### Question

> What is the size of the dataset?

### Passage

> Experimental setting We split the vSTS dataset into development and test partitions, sampling 50% at random, while preserving the overall score distributions. In addition, we used part of the text-only STS benchmark dataset as a training set, discarding the examples that overlap with vSTS.
> 
> STS Models We checked four models of different complexity and modalities. The baseline is a word overlap model (overlap), in which input texts are tokenized with white space, vectorized according to a word index, and similarity is computed as the cosine of the vectors. We also calculated the centroid of Glove word embeddings BIBREF17 (caverage) and then computed the cosine as a second text-based model. The third text-based model is the state of the art Decomposable Attention Model BIBREF18 (dam), trained on the STS benchmark dataset as explained above. Finally, we use the top layer of a pretrained resnet50 model BIBREF19 to represent the images associated to text, and use the cosine for computing the similarity of a pair of images (resnet50).
> 
> Model combinations We combined the predictions of text based models with the predictions of the image based model (see Table TABREF4 for specific combinations). Models are combined using addition ( INLINEFORM0 ), multiplication ( INLINEFORM1 ) and linear regression (LR) of the two outputs. We use 10-fold cross-validation on the development test for estimating the parameters of the linear regressor.
> 
> Results Table TABREF4 shows the results of the single and combined models. Among single models, as expected, dam obtains the highest Pearson correlation ( INLINEFORM0 ). Interestingly, the results show that images alone are valid to predict caption similarity (0.61 INLINEFORM1 ). Results also show that image and sentence representations are complementary, with the best results for a combination of DAM and RESNET50 representations. These results confirm our hypotheses, and more generally, show indications that in systems that work with text describing the real world, the representation of the real world helps to better understand the text and do better inferences.

### Relevance

Label: 

## Record 0568

Paper: Evaluating Multimodal Representations on Sentence Similarity: vSTS, Visual Semantic Textual Similarity Dataset

### Question

> What is the size of the dataset?

### Passage

> to study whether better sentence representations can be built when having access to corresponding images, e.g. a caption and its image, in contrast with having access to the text alone. This dataset is based on a subset of the STS benchmark BIBREF1 , more specifically, the so called STS-images subset, which contains pairs of captions. Note that the annotations are based on the textual information alone. vSTS extends the existing subset with images, and aims at being a standard dataset to test the contribution of visual information when evaluating sentence representations.
> 
> In addition we show that the dataset allows to explore two hypothesis: H1) whether the image representations alone are able to predict caption similarity; H2) whether a combination of image and text representations allow to improve the text-only results on this similarity task.

### Relevance

Label: 

## Record 0569

Paper: Evaluating Multimodal Representations on Sentence Similarity: vSTS, Visual Semantic Textual Similarity Dataset

### Question

> What is the size of the dataset?

### Passage

> The success of word representations (embeddings) learned from text has motivated analogous methods to learn representations of longer sequences of text such as sentences, a fundamental step on any task requiring some level of text understanding BIBREF0 . Sentence representation is a challenging task that has to consider aspects such as compositionality, phrase similarity, negation, etc. In order to evaluate sentence representations, intermediate tasks such as Semantic Textual Similarity (STS) BIBREF1 or Natural Language Inference (NLI) BIBREF2 have been proposed, with STS being popular among unsupervised approaches. Through a set of campaigns, STS has produced several manually annotated datasets, where annotators measure the similarity among sentences, with higher scores for more similar sentences, ranging between 0 (no similarity) to 5 (semantic equivalence). Human annotators exhibit high inter-tagger correlation in this task.
> 
> In another strand of related work, tasks that combine representations of multiple modalities have gained increasing attention, including image-caption retrieval, video and text alignment, caption generation, and visual question answering. A common approach is to learn image and text embeddings that share the same space so that sentence vectors are close to the representation of the images they describe BIBREF3 , BIBREF4 . BIBREF5 provides an approach that learns to align images with descriptions. Joint spaces are typically learned combining various types of deep learning networks such us recurrent networks or convolutional networks, with some attention mechanism BIBREF6 , BIBREF7 , BIBREF8 .
> 
> The complementarity of visual and text representations for improved language understanding have been shown also on word representations, where embeddings have been combined with visual or perceptual input to produce grounded representations of words BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 , BIBREF13 , BIBREF14 , BIBREF15 . These improved representation models have outperformed traditional text-only distributional models on a series of word similarity tasks, showing that visual information coming from images is complementary to textual information.
> 
> In this paper we present Visual Semantic Textual Similarity (vSTS), a dataset which allows to study whether better sentence representations can be built when having access to corresponding images, e.g. a caption and its image, in contrast with having access to the text alone. This dataset is based on a subset of the STS

### Relevance

Label: 

## Record 0570

Paper: Evaluating Multimodal Representations on Sentence Similarity: vSTS, Visual Semantic Textual Similarity Dataset

### Question

> What is the size of the dataset?

### Passage

> We introduced the vSTS dataset, which contains caption pairs with human similarity annotations, where the systems can also access the actual images. The dataset aims at being a standard dataset to test the contribution of visual information when evaluating the similarity of sentences.
> 
> Experiments confirmed our hypotheses: image representations are useful for caption similarity and they are complementary to textual representations, as results improve significantly when two modalities are combined together.
> 
> In the future we plan to re-annotate the dataset with scores which are based on both the text and the image, in order to shed light on the interplay of images and text when understanding text.

### Relevance

Label: 

## Record 0571

Paper: Variational Transformers for Diverse Response Generation

### Question

> What three conversational datasets are used for evaluation?

### Passage

> are one-to-one multi-turn conversation datasets. In PersonaChat (Persona), the conversations are revolve around personas which are established by four to six persona sentences. While in Empathetic-Dialogues (ED), the conversation are mostly about situation that happened to one of the speaker and another speaker is trying to understand the feeling and reply accordingly. Both datasets are about modeling social skills and the goal is to make user more engaging. Therefore, we combine the train/validation/test set of two datasets.

### Relevance

Label: 

## Record 0572

Paper: Variational Transformers for Diverse Response Generation

### Question

> What three conversational datasets are used for evaluation?

### Passage

> In the human evaluation, we prepare multiple-choice questions for human evaluators and the answers are the generation results from the five models (Seq2Seq, CVAE, Transformer, GVT, and SVT). we first randomly sample 100 dialogues and their corresponding responses from our models and the baselines. For each response, we assign three human annotators to select the most coherent (on topic) response to the context (multiple answers are allowed). In addition, annotators also need to choose the best response correlated to the given emoji label in Mojitalk and the most engaging response in PersonaChat and Empathetic-Dialogues. If there is no response that satisfies the evaluators, they can choose “all answers are bad", which means none of the answer is chosen. We compute the rate that each model is chosen to quantify generation quality regarding to the human standard.

### Relevance

Label: 

## Record 0573

Paper: Variational Transformers for Diverse Response Generation

### Question

> What three conversational datasets are used for evaluation?

### Passage

> The CVAE framework BIBREF22 represents a dyadic conversation via three random variables: the input condition $c$, including conversation context and meta features (meta features can be ignored when not available); a latent variable $z$; and the target response $x$. A CVAE can be efficiently trained with Stochastic Gradient Variational Bayes (SGVB) BIBREF23 by maximizing the variational lower bound of $x$ given c, according to:
> 
> The typical CVAE consists of a prior network $p_{\theta }(z | c)$, which is used to approximate $p(z | c)$, a recognition network $p_{\phi }(z | c, x)$, which is used to approximate posterior distribution $q(z | c, x)$, and a decoder $p_{\theta }(x | z, c)$, which is used to approximate $p(x | z, c)$. By assuming z follows multivariate Gaussian distribution with a diagonal co-variance matrix, the evidence lower bound (ELBO) can be written as
> 
> where $\mathcal {L}_{REC}$ denotes the reconstruction loss and $\mathcal {L}_{KL}$ denotes the Kullback-Leibler (KL) divergence between the posterior and prior.
> 
> In dialogue generation tasks, previous works BIBREF2, BIBREF16 apply RNN encoders (with GRU or LSTM cell) to encode dialogue contexts and responses separately. The condition $c$ is represented by the concatenation of the last hidden state of the context encoder and the meta features (e.g., topic, emotion), while the response $x$ is represented by the last hidden state of response encoder. Then the prior network $p_{\theta }(z | c)$ and the recognition network $p_{\phi }(z | c, x)$ parameterized by multi-layer perceptrons (MLPs) are applied to approximate the means and the log variances of the prior latent distribution $\mathcal {N}\left(z ; \mu ^{\prime }, \sigma ^{\prime 2} \mathbf {I}\right)$ and posterior latent distribution $\mathcal {N}\left(z ; \mu , \sigma ^{2} \mathbf {I}\right)$. With the reparameterization trick BIBREF23, we can obtain samples of the prior latent variable (for testing) from $\mathcal {N}\left(z ; \mu ^{\prime }, \sigma ^{\prime 2} \mathbf {I}\right)$ and samples of the posterior latent variable (for training) from $\mathcal {N}\left(z ; \mu , \sigma ^{2} \mathbf {I}\right)$. Finally, an RNN decoder use $z$ and $c$ as the initial state to predicts the response $x$.
> 
> The vanishing latent variable problem BIBREF24 is a common issue in RNN-based CVAEs. That is, the powerful autoregressive

### Relevance

Label: 

## Record 0574

Paper: Variational Transformers for Diverse Response Generation

### Question

> What three conversational datasets are used for evaluation?

### Passage

> Conversational systems has been widely studied BIBREF5, BIBREF6, BIBREF7, BIBREF8. Compare to rule-based systems BIBREF5, BIBREF6, sequence-to-sequence conversation models achieve superior performance in terms of scalable training and generalization ability BIBREF7. However, it has been pointed out that encoder-decoder models tend to generate generic and repetitive responses like “I am sorry" BIBREF9. To address this issue, there have been three main lines of work. The first is adding additional information (e.g., persona) as input to guild model generate more informative responses BIBREF10, BIBREF11. The second modifies the learning objective to promote more diverse generation BIBREF9, and the third integrates stochastic latent variables into Seq2Seq models by using the CVAE framework BIBREF12, BIBREF2. Our work comes within this third line introducing a novel model, the Variational Transformer, to improve dialogue response generation.

### Relevance

Label: 

## Record 0575

Paper: Variational Transformers for Diverse Response Generation

### Question

> What three conversational datasets are used for evaluation?

### Passage

> The automatic evaluation results are shown in Table TABREF35. Transformer-based models have significantly lower perplexity compared to RNN-based models which indicate that the global receptive field performed by multi-head self-attention boost the modeling capacity. However, deterministic Seq2Seq and Transformer models tends to generate generic responses which leads to a low diversity score. Meanwhile incorporating a stochastic latent variable into both models (CVAE and GVT) promote more diverse generation results and boost the diversity scores such as Dist-1, Dist-2, and Dist-3.
> 
> Compare to baseline models, the GVT achieves relatively lower reconstruction PPL, which suggests that the global latent variable contains rich latent information (e.g., topic) for response generation. Meanwhile, the sequential latent variables of the SVT encode fine-grained latent information and further improve the reconstruction PPL.
> 
> On the other hand, SVT achieves the highest score in terms of two semantic relevance-oriented metrics such as $\textbf {EMB}_\textbf {FT}$ and $\textbf {EMB}_\textbf {BERT}$ in MojiTalk dataset, while in the combined dataset of Persona and ED, we observe performance drop of SVT compare to other models. This is because both Persona and ED are well designed and have lower entropy than MojiTalk which collected from Twitter. We hypothesize that the sequential latent variables have no advantage in term of similarity to single, fixed "gold response" when model low entropy response. Indeed, in open domain dialogue response generation, automatic metric is not always aligned with the human judgement BIBREF28. In contrast, human evaluation result reported in Table TABREF35 demonstrates the generations of SVT are closer to the human standard in terms of coherence, invoked emotion and engagedness.

### Relevance

Label: 

## Record 0576

Paper: Bridging the Gap for Tokenizer-Free Language Models

### Question

> How many parameters does the model have?

### Passage

> used for their ability to produce pretrained representations that will be fine-tuned for a downstream task BIBREF11, BIBREF12, BIBREF13, BIBREF14. Since word-based LMs use closed vocabulary and sub-word models adopt a segmentation that targets the pretraining corpus, there is little space to adapt the vocabulary or optimize the segmentation to fit the final task data distribution.
> 
> The rest of this paper is organized as follows. In Section SECREF2, we describe our model architecture, which is a vanilla deep transformer byte-level LM. Section SECREF3 describes the lm1b dataset and our evaluation methodology. Section SECREF4 presents our results and how our model compares to the previous work. In Section SECREF5 we analyze the representations learned by the network at different depths using word-similarity benchmarks. For this analysis to be feasible we propose a strategy to extract word representations from a character model.
> 
> To summarize our contributions:
> 
> We develop a competitive tokenizer-free language model on a large scalable dataset.
> 
> We probe the performance of our model's learned intermediate representations on word similarity tasks.

### Relevance

Label: 

## Record 0577

Paper: Bridging the Gap for Tokenizer-Free Language Models

### Question

> How many parameters does the model have?

### Passage

> We sample random byte sequences of length 512. This sampling process does not respect the sentence boundary. Therefore, one example might span complete and partial sentences. We dropout both timesteps of self-attention layers and features of relu activations across timesteps with a probability of 0.3. We use the Adam optimizer BIBREF15 with initial learning rate $10^{-4}$ and batch size 1024. The training runs for two million steps, and at every 10,000 steps we decay the learning rate geometrically by 0.99.

### Relevance

Label: 

## Record 0578

Paper: Bridging the Gap for Tokenizer-Free Language Models

### Question

> How many parameters does the model have?

### Passage

> Language models (LMs) assign a probability distribution over a sequence $x_{0:t}$ by factoring out the joint probability from left to right as follows
> 
> Instead of reading in the tokenized input text, our model reads raw utf-8 bytes. For English text in the ASCII range, this is equivalent to processing characters as individual tokens. Non-ASCII characters (e.g. accented characters, or non-Latin scripts) are typically two or three utf-8 bytes. We use a standard “transformer decoder” (a stack of transformer layers with a causal attention mask) to process the sequence $x_{0:i-1}$ and predict the following byte $x_i$. The model's prediction is an estimate of the probability distribution over all possible 256 byte values. Our input byte embedding matrix has dimensionality 256. Our byte-level transformer model has 40 standard transformer layers with hidden size 1024, filter size 8192, and 16 heads. The model has around 836M parameters, of which only 66K are byte embeddings.

### Relevance

Label: 

## Record 0579

Paper: Bridging the Gap for Tokenizer-Free Language Models

### Question

> How many parameters does the model have?

### Passage

> Table TABREF7 shows the perplexity of several models on lm1b. We observe that tokenizer-free LM performance improves significantly (40.6 to 23.0) when the model capacity is increased from 0.2B to 0.8B parameters. With sufficient capacity our byte-level LM is competitive with word based models (ranging from 21.8 to 28.0). Note, our model is able to achieve comparable performance without any explicit signal of word boundaries.
> 
> Because of the large symbol space that word-based LMs address, they rely on sparse operations running on heterogeneous devices to run efficiently (e.g. running sparse embedding lookups on CPU as opposed to GPU/TPU). By contrast, byte LMs are dense, and all operations can be executed on specialized accelerators efficiently. We expect that with advances in accelerated hardware, byte-level text processing will become a popular choice.
> 
> Of all the baseline models we reference, only BIBREF4 uses recurrence to model arbitrary length history. This technique could be added to tokenizer-free models as well. Indeed, we expect this approach to be particularly well-suited to byte and character models where text gets mapped onto longer token sequences, as BIBREF4 show that adding recurrence increases the length of context their model can effectively use.

### Relevance

Label: 

## Record 0580

Paper: Bridging the Gap for Tokenizer-Free Language Models

### Question

> How many parameters does the model have?

### Passage

> There are no large scale datasets that are heavily studied for both word and character language modeling. Typically, a specific dataset will be considered under just one level of segmentation. For our efforts to be comparable with the literature, we use a word LM dataset. This puts our model at a disadvantage; the dataset is tokenized and our model will not utilize the given word boundary information. Our approach is able to model rare words and estimate their appropriate likelihoods, however, they have been replaced with a special token to produce closed vocabulary text that is appropriate for word-level modeling. Hence, the metrics we report are meant to provide a lower bound on the utility of our approach in realistic settings.

### Relevance

Label: 

## Record 0581

Paper: Speeding up Context-based Sentence Representation Learning with Non-autoregressive Convolutional Decoding

### Question

> Which downstream tasks are considered?

### Passage

> Our model is highly asymmetric in terms of both the training pairs and the model structure. Specifically, our model has an RNN as the encoder, and a CNN as the decoder. During training, the encoder takes the INLINEFORM0 -th sentence INLINEFORM1 as the input, and then produces a fixed-dimension vector INLINEFORM2 as the sentence representation; the decoder is applied to reconstruct the paired target sequence INLINEFORM3 that contains the subsequent contiguous words. The distance between the generated sequence and the target one is measured by the cross-entropy loss at each position in INLINEFORM4 . An illustration is in Figure FIGREF4 . (For simplicity, we omit the subscript INLINEFORM5 in this section.)
> 
> 1. Encoder: The encoder is a bi-directional Gated Recurrent Unit (GRU, BIBREF7 ). Suppose that an input sentence INLINEFORM0 contains INLINEFORM1 words, which are INLINEFORM2 , and they are transformed by an embedding matrix INLINEFORM3 to word vectors. The bi-directional GRU takes one word vector at a time, and processes the input sentence in both the forward and backward directions; both sets of hidden states are concatenated to form the hidden state matrix INLINEFORM7 , where INLINEFORM8 is the dimension of the hidden states INLINEFORM9 ( INLINEFORM10 ).
> 
> 2. Representation: We aim to provide a model with faster training speed and better transferability than existing algorithms; thus we choose to apply a parameter-free composition function, which is a concatenation of the outputs from a global mean pooling over time and a global max pooling over time, on the computed sequence of hidden states INLINEFORM0 . The composition function is represented as DISPLAYFORM0
> 
> where INLINEFORM0 is the max operation on each row of the matrix INLINEFORM1 , which outputs a vector with dimension INLINEFORM2 . Thus the representation INLINEFORM3 . 3. Decoder: The decoder is a 3-layer CNN to reconstruct the paired target sequence INLINEFORM4 , which needs to expand INLINEFORM5 , which can be considered as a sequence with only one element, to a sequence with INLINEFORM6 elements. Intuitively, the decoder could be a stack of deconvolution layers. For fast training speed, we optimised the architecture to make it possible to use fully-connected layers and convolution layers in the decoder, since generally, convolution layers

### Relevance

Label: 

## Record 0582

Paper: Speeding up Context-based Sentence Representation Learning with Non-autoregressive Convolutional Decoding

### Question

> Which downstream tasks are considered?

### Passage

> We studied hyperparameters in our model design based on three out of 10 downstream tasks, which are SICK-R, SICK-E BIBREF17 , and STS14 BIBREF18 . The first model we created, which is reported in Section SECREF2 , is a decent design, and the following variations didn't give us much performance change except improvements brought by increasing the dimensionality of the encoder. However, we think it is worth mentioning the effect of hyperparameters in our model design. We present the Table TABREF21 in the supplementary material and we summarise it as follows:
> 
> 1. Decoding the next sentence performed similarly to decoding the subsequent contiguous words.
> 
> 2. Decoding the subsequent 30 words, which was adopted from the skip-thought training code, gave reasonably good performance. More words for decoding didn't give us a significant performance gain, and took longer to train.
> 
> 3. Adding more layers into the decoder and enlarging the dimension of the convolutional layers indeed sightly improved the performance on the three downstream tasks, but as training efficiency is one of our main concerns, it wasn't worth sacrificing training efficiency for the minor performance gain.
> 
> 4. Increasing the dimensionality of the RNN encoder improved the model performance, and the additional training time required was less than needed for increasing the complexity in the CNN decoder. We report results from both smallest and largest models in Table TABREF16 .

### Relevance

Label: 

## Record 0583

Paper: Speeding up Context-based Sentence Representation Learning with Non-autoregressive Convolutional Decoding

### Question

> Which downstream tasks are considered?

### Passage

> Learning distributed representations of sentences is an important and hard topic in both the deep learning and natural language processing communities, since it requires machines to encode a sentence with rich language content into a fixed-dimension vector filled with real numbers. Our goal is to build a distributed sentence encoder learnt in an unsupervised fashion by exploiting the structure and relationships in a large unlabelled corpus.
> 
> Numerous studies in human language processing have supported that rich semantics of a word or sentence can be inferred from its context BIBREF0 , BIBREF1 . The idea of learning from the co-occurrence BIBREF2 was recently successfully applied to vector representation learning for words in BIBREF3 and BIBREF4 .
> 
> A very recent successful application of the distributional hypothesis BIBREF0 at the sentence-level is the skip-thoughts model BIBREF5 . The skip-thoughts model learns to encode the current sentence and decode the surrounding two sentences instead of the input sentence itself, which achieves overall good performance on all tested downstream NLP tasks that cover various topics. The major issue is that the training takes too long since there are two RNN decoders to reconstruct the previous sentence and the next one independently. Intuitively, given the current sentence, inferring the previous sentence and inferring the next one should be different, which supports the usage of two independent decoders in the skip-thoughts model. However, BIBREF6 proposed the skip-thought neighbour model, which only decodes the next sentence based on the current one, and has similar performance on downstream tasks compared to that of their implementation of the skip-thoughts model.
> 
> In the encoder-decoder models for learning sentence representations, only the encoder will be used to map sentences to vectors after training, which implies that the quality of the generated language is not our main concern. This leads to our two-step experiment to check the necessity of applying an autoregressive model as the decoder. In other words, since the decoder's performance on language modelling is not our main concern, it is preferred to reduce the complexity of the decoder to speed up the training process. In our experiments, the first step is to check whether “teacher-forcing” is required during training if we stick to using an

### Relevance

Label: 

## Record 0584

Paper: Speeding up Context-based Sentence Representation Learning with Non-autoregressive Convolutional Decoding

### Question

> Which downstream tasks are considered?

### Passage

> Table TABREF16 presents the results on 9 evaluation tasks of our proposed RNN-CNN models, and related work. The “small RNN-CNN” refers to the model with the dimension of representation as 1200, and the “large RNN-CNN” refers to that as 4800. The results of our “large RNN-CNN” model on SNLI is presented in Table TABREF19 .
> 
> Our work was inspired by analysing the skip-thoughts model BIBREF5 . The skip-thoughts model successfully applied this form of learning from the context information into unsupervised representation learning for sentences, and then, BIBREF29 augmented the LSTM with proposed layer-normalisation (Skip-thought+LN), which improved the skip-thoughts model generally on downstream tasks. In contrast, BIBREF11 proposed the FastSent model which only learns source and target word embeddings and is an adaptation of Skip-gram BIBREF3 to sentence-level learning without word order information. BIBREF9 applied a CNN as the encoder, but still applied LSTMs for decoding the adjacent sentences, which is called CNN-LSTM.
> 
> Our RNN-CNN model falls in the same category as it is an encoder-decoder model. Instead of decoding the surrounding two sentences as in skip-thoughts, FastSent and the compositional CNN-LSTM, our model only decodes the subsequent sequence with a fixed length. Compared with the hierarchical CNN-LSTM, our model showed that, with a proper model design, the context information from the subsequent words is sufficient for learning sentence representations. Particularly, our proposed small RNN-CNN model runs roughly three times faster than our implemented skip-thoughts model on the same GPU machine during training.
> 
> Proposed by BIBREF30 , BYTE m-LSTM model uses a multiplicative LSTM unit BIBREF31 to learn a language model. This model is simple, providing next-byte prediction, but achieves good results likely due to the extremely large training corpus (Amazon Review data, BIBREF26 ) that is also highly related to many of the sentiment analysis downstream tasks (domain matching).
> 
> We experimented with the Amazon Book review dataset, the largest subset of the Amazon Review. This subset is significantly smaller than the full Amazon Review dataset but twice as large as BookCorpus. Our RNN-CNN model trained on the Amazon Book review dataset resulted in performance improvement on all single-sentence classification tasks relative to that achieved with training under BookCorpus.
> 
> Unordered sentences are also useful for

### Relevance

Label: 

## Record 0585

Paper: Speeding up Context-based Sentence Representation Learning with Non-autoregressive Convolutional Decoding

### Question

> Which downstream tasks are considered?

### Passage

> dataset but twice as large as BookCorpus. Our RNN-CNN model trained on the Amazon Book review dataset resulted in performance improvement on all single-sentence classification tasks relative to that achieved with training under BookCorpus.
> 
> Unordered sentences are also useful for learning representations of sentences. ParagraphVec BIBREF32 learns a fixed-dimension vector for each sentence by predicting the words within the given sentence. However, after training, the representation for a new sentence is hard to derive, since it requires optimising the sentence representation towards an objective. SDAE BIBREF11 learns the sentence representations with a denoising auto-encoder model. Our proposed RNN-CNN model trains faster than SDAE does, and also because we utilised the sentence-level continuity as a supervision which SDAE doesn't, our model largely performs better than SDAE.
> 
> Another transfer approach is to learn a supervised discriminative classifier by distinguishing whether the sentence pair or triple comes from the same context. BIBREF33 proposed a model that learns to classify whether the input sentence triplet contains three contiguous sentences. DiscSent BIBREF34 and DisSent BIBREF35 both utilise the annotated explicit discourse relations, which is also good for learning sentence representations. It is a very promising research direction since the proposed models are generally computational efficient and have clear intuition, yet more investigations need to be done to augment the performance.
> 
> Supervised training for transfer learning is also promising when a large amount of human-annotated data is accessible. BIBREF14 proposed the InferSent model, which applies a bi-directional LSTM as the sentence encoder with multiple fully-connected layers to classify whether the hypothesis sentence entails the premise sentence in SNLI BIBREF13 , and MultiNLI BIBREF36 . The trained model demonstrates a very impressive transferability on downstream tasks, including both supervised and unsupervised. Our RNN-CNN model trained on Amazon Book Review data in an unsupervised way has better results on supervised tasks than InferSent but slightly inferior results on semantic relatedness tasks. We argue that labelling a large amount of training data is time-consuming and costly, while unsupervised learning provides great performance at a fraction of the cost. It could potentially be leveraged to initialise or more generally augment the costly human labelling, and make the overall system less costly and more efficient.

### Relevance

Label: 

## Record 0586

Paper: Learning Hierarchy-Aware Knowledge Graph Embeddings for Link Prediction

### Question

> How are entities mapped onto polar coordinate system?

### Passage

> To model the semantic hierarchies in knowledge graphs, we propose a novel hierarchy-aware knowledge graph embedding model—HAKE—which maps entities into the polar coordinate system. Experiments show that our proposed HAKE significantly outperforms several existing state-of-the-art methods on benchmark datasets for the link prediction task. A further investigation shows that HAKE is capable of modeling entities at both different levels and the same levels in the semantic hierarchies.

### Relevance

Label: 

## Record 0587

Paper: Learning Hierarchy-Aware Knowledge Graph Embeddings for Link Prediction

### Question

> How are entities mapped onto polar coordinate system?

### Passage

> distance between phases instead of using $\Vert \textbf {h}_p+\textbf {r}_p-\textbf {t}_p\Vert _1$, as phases have periodic characteristic. This distance function shares the same formulation with that of pRotatE BIBREF7.
> 
> Combining the modulus part and the phase part, HAKE maps entities into the polar coordinate system, where the radial coordinate and the angular coordinates correspond to the modulus part and the phase part, respectively. That is, HAKE maps an entity $h$ to $[\textbf {h}_m;\textbf {h}_p]$, where $\textbf {h}_m$ and $\textbf {h}_p$ are generated by the modulus part and the phase part, respectively, and $[\,\cdot \,; \,\cdot \,]$ denotes the concatenation of two vectors. Obviously, $([\textbf {h}_m]_i,[\textbf {h}_p]_i)$ is a 2D point in the polar coordinate system. Specifically, we formulate HAKE as follows:
> 
> The distance function of HAKE is:
> 
> where $\lambda \in \mathbb {R}$ is a parameter that learned by the model. The corresponding score function is
> 
> When two entities have the same moduli, then the modulus part $d_{r,m}(\textbf {h}_m,\textbf {t}_m)=0$. However, the phase part $d_{r,p}(\textbf {h}_p,\textbf {t}_p)$ can be very different. By combining the modulus part and the phase part, HAKE can model the entities in both the category (a) and the category (b). Therefore, HAKE can model semantic hierarchies of knowledge graphs.
> 
> When evaluating the models, we find that adding a mixture bias to $d_{r,m}(\textbf {h},\textbf {t})$ can help to improve the performance of HAKE. The modified $d_{r,m}(\textbf {h},\textbf {t})$ is given by:
> 
> where $0<\textbf {r}^{\prime }_m<1$ is a vector that have the same dimension with $\textbf {r}_m$. Indeed, the above distance function is equivalent to
> 
> where $/$ denotes the element-wise division operation. If we let $\textbf {r}_m\leftarrow (1-\textbf {r}_m^{\prime })/(\textbf {r}_m+\textbf {r}_m^{\prime })$, then the modified distance function is exactly the same as the original one when compare the distances of different entity pairs. For notation convenience, we still use $d_{r,m}(\textbf {h},\textbf {t})=\Vert \textbf {h}_m\circ \textbf {r}_m-\textbf {t}_m\Vert _2$ to represent the modulus part. We will conduct ablation studies on the bias in the experiment section.

### Relevance

Label: 

## Record 0588

Paper: Learning Hierarchy-Aware Knowledge Graph Embeddings for Link Prediction

### Question

> How are entities mapped onto polar coordinate system?

### Passage

> In this part, to further show that HAKE can capture the semantic hierarchies between entities, we visualize the embeddings of several entity pairs.
> 
> We plot the entity embeddings of two models: the previous state-of-the-art RotatE and our proposed HAKE. RotatE regards each entity as a group of complex numbers. As a complex number can be seen as a point on a 2D plane, we can plot the entity embeddings on a 2D plane. As for HAKE, we have mentioned that it maps entities into the polar coordinate system. Therefore, we can also plot the entity embeddings generated by HAKE on a 2D plane based on their polar coordinates. For a fair comparison, we set $k=500$. That is, each plot contains 500 points, and the actual dimension of entity embeddings is 1000. Note that we use the logarithmic scale to better display the differences between entity embeddings. As all the moduli have values less than one, after applying the logarithm operation, the larger radii in the figures will actually represent smaller modulus.
> 
> Figure FIGREF29 shows the visualization results of three triples from the WN18RR dataset. Compared with the tail entities, the head entities in Figures FIGREF29a, FIGREF29b, and FIGREF29c are at lower levels, similar levels, higher levels in the semantic hierarchy, respectively. We can see that there exist clear concentric circles in the visualization results of HAKE, which demonstrates that HAKE can effectively model the semantic hierarchies. However, in RotatE, the entity embeddings in all three subfigures are mixed, making it hard to distinguish entities at different levels in the hierarchy.

### Relevance

Label: 

## Record 0589

Paper: Learning Hierarchy-Aware Knowledge Graph Embeddings for Link Prediction

### Question

> How are entities mapped onto polar coordinate system?

### Passage

> rotations, can model relation patterns including symmetry/antisymmetry, inversion, and composition. However, many existing models fail to model semantic hierarchies in knowledge graphs.
> 
> Semantic hierarchy is a ubiquitous property in knowledge graphs. For instance, WordNet BIBREF10 contains the triple [arbor/cassia/palm, hypernym, tree], where “tree” is at a higher level than “arbor/cassia/palm” in the hierarchy. Freebase BIBREF11 contains the triple [England, /location/location/contains, Pontefract/Lancaster], where “Pontefract/Lancaster” is at a lower level than “England” in the hierarchy. Although there exists some work that takes the hierarchy structures into account BIBREF12, BIBREF13, they usually require additional data or process to obtain the hierarchy information. Therefore, it is still challenging to find an approach that is capable of modeling the semantic hierarchy automatically and effectively.
> 
> In this paper, we propose a novel knowledge graph embedding model—namely, Hierarchy-Aware Knowledge Graph Embedding (HAKE). To model the semantic hierarchies, HAKE is expected to distinguish entities in two categories: (a) at different levels of the hierarchy; (b) at the same level of the hierarchy. Inspired by the fact that entities that have the hierarchical properties can be viewed as a tree, we can use the depth of a node (entity) to model different levels of the hierarchy. Thus, we use modulus information to model entities in the category (a), as the size of moduli can reflect the depth. Under the above settings, entities in the category (b) will have roughly the same modulus, which is hard to distinguish. Inspired by the fact that the points on the same circle can have different phases, we use phase information to model entities in the category (b). Combining the modulus and phase information, HAKE maps entities into the polar coordinate system, where the radial coordinate corresponds to the modulus information and the angular coordinate corresponds to the phase information. Experiments show that our proposed HAKE model can not only clearly distinguish the semantic hierarchies of entities, but also significantly and consistently outperform several state-of-the-art methods on the benchmark datasets.
> 
> Notations Throughout this paper, we use lower-case letters $h$, $r$, and $t$ to represent head entities, relations, and tail entities, respectively. The triplet $(h,r,t)$ denotes a fact in knowledge graphs. The corresponding boldface lower-case letters $\textbf {h}$, $\textbf {r}$

### Relevance

Label: 

## Record 0590

Paper: Learning Hierarchy-Aware Knowledge Graph Embeddings for Link Prediction

### Question

> How are entities mapped onto polar coordinate system?

### Passage

> Another related problem is how to model hierarchy structures in knowledge graphs. Some recent work considers the problem in different ways. BIBREF25 embed entities and categories jointly into a semantic space and designs models for the concept categorization and dataless hierarchical classification tasks. BIBREF13 use clustering algorithms to model the hierarchical relation structures. BIBREF12 proposed TKRL, which embeds the type information into knowledge graph embeddings. That is, TKRL requires additional hierarchical type information for entities.
> 
> Different from the previous work, our work
> 
> considers the link prediction task, which is a more common task for knowledge graph embeddings;
> 
> can automatically learn the semantic hierarchy in knowledge graphs without using clustering algorithms;
> 
> does not require any additional information other than the triples in knowledge graphs.

### Relevance

Label: 

## Record 0591

Paper: Phrase Table as Recommendation Memory for Neural Machine Translation

### Question

> what datasets did they use?

### Passage

> We test the proposed methods on Chinese-to-English (CH-EN) translation and English-to-Japanese (EN-JA) translation. In CH-EN translation, we test the proposed methods with two data sets: 1) small data set, which includes 0.63M sentence pairs; 2) large-scale data set, which contains about 2.1M sentence pairs. NIST 2003 (MT03) dataset is used for validation. NIST2004-2006 (MT04-06) and NIST 2008 (MT08) datasets are used for testing. In EN-JA translation, we use KFTT dataset, which includes 0.44M sentence pairs for training, 1166 sentence pairs for validation and 1160 sentence pairs for testing.

### Relevance

Label: 

## Record 0592

Paper: Phrase Table as Recommendation Memory for Neural Machine Translation

### Question

> what datasets did they use?

### Passage

> We use the Zoph_RNN toolkit to implement all our described methods. In all experiments, the encoder and decoder include two stacked LSTM layers. The word embedding dimension and the size of hidden layers are both set to 1,000. The minibatch size is set to 128. We limit the vocabulary to 30K most frequent words for both the source and target languages. Other words are replaced by a special symbol “UNK”. At test time, we employ beam search and beam size is set to 12. We use case-insensitive 4-gram BLEU score as the automatic metric BIBREF21 for translation quality evaluation.

### Relevance

Label: 

## Record 0593

Paper: Phrase Table as Recommendation Memory for Neural Machine Translation

### Question

> what datasets did they use?

### Passage

> BIBREF19 's models, the source side of a phrase pair must be a chunk. Therefore, it is still a big challenge to incorporate any phrase pair in the phrase table into NMT system to alleviate the unfaithfulness problem.
> 
> In this paper, we propose an effective method to incorporate a phrase table as recommendation memory into the NMT system. To achieve this, we add bonuses to the words in recommendation set to help NMT make better predictions. Generally, our method contains three steps. 1) In order to find out which words are worthy to recommend, we first derive a candidate target phrase set by searching the phrase table according to the input sentence. After that, we construct a recommendation word set at each decoding step by matching between candidate target phrases and previously translated target words by NMT. 2) We then determine the specific bonus value for each recommendable word by using the attention vector produced by NMT and phrase translation probability extracted from phrase table. 3) Finally we integrate the word bonus value into the NMT system to improve the final results.
> 
> In this paper, we make the following contributions:
> 
> 1) We propose a method to incorporate the phrase table as recommendation memory into NMT system. We design a novel approach to find from the phrase table the target words worthy of recommendation, calculate their recommendation scores and use them to promote NMT to make better predictions.
> 
> 2) Our empirical experiments on Chinese-English translation and English-Japanese translation tasks show the efficacy of our methods. For Chinese-English translation, we can obtain an average improvement of 2.23 BLEU points. For English-Japanese translation, the improvement can reach 1.96 BLEU points. We further find that the phrase table is much more beneficial than bilingual lexicons to NMT.

### Relevance

Label: 

## Record 0594

Paper: Phrase Table as Recommendation Memory for Neural Machine Translation

### Question

> what datasets did they use?

### Passage

> In this work, we focus on integrating the phrase translation table of SMT into NMT. And there have been several effective works to combine SMT and NMT.
> 
> Using coverage mechanism. BIBREF9 and BIBREF10 improved the over-translation and under-translation problems in NMT inspired by the coverage mechanism in SMT.
> 
> Extending beam search. BIBREF25 extended the beam search method with SMT hypotheses. BIBREF13 improved the beam search by using the SMT lattices.
> 
> Combining SMT features and results. BIBREF12 presented a log-linear model to integrate SMT features (translation model and the language model) into NMT. BIBREF26 and BIBREF27 proposed a supervised attention model for NMT to minimize the alignment disagreement between NMT and SMT. BIBREF11 proposed a method that incorporates the translations of SMT into NMT with an auxiliary classifier and a gating function. BIBREF28 proposed a neural combination model to fuse the NMT translation results and SMT translation results.
> 
> Incorporating translation lexicons. BIBREF6 , BIBREF17 attempted to integrate NMT with the probabilistic translation lexicons. BIBREF16 moved forward further by incorporating a bilingual dictionaries in NMT.
> 
> In above works, integrating the phrase translation table of SMT into NMT has not been fully studied.
> 
> Translating phrase in NMT. The most related works are BIBREF18 and BIBREF19 . Both methods attempted to explore the possibility of translating phrases as a whole in NMT. In their models, NMT can generate a target phrase in phrase memory or a word in vocabulary by using a gate. However, their “phrases” are different from that are used in phrase-based SMT. BIBREF18 's models only support a unique translation for a source phrase. In BIBREF19 's models, the source side of a phrase pair must be a chunk. Different from above two methods, our model can use any phrase pair in the phrase translation table and promising results can be achieved.

### Relevance

Label: 

## Record 0595

Paper: Phrase Table as Recommendation Memory for Neural Machine Translation

### Question

> what datasets did they use?

### Passage

> The past several years have witnessed a significant progress in Neural Machine Translation (NMT). Most NMT methods are based on the encoder-decoder architecture BIBREF0 , BIBREF1 , BIBREF2 and can achieve promising translation performance in a variety of language pairs BIBREF3 , BIBREF4 , BIBREF5 .
> 
> However, recent studies BIBREF6 , BIBREF7 show that NMT often generates words that make target sentences fluent, but unfaithful to the source sentences. In contrast, traditional Statistical Machine Translation (SMT) methods tend to rarely make this kind of mistakes. Fig. 1 shows an example that NMT makes mistakes when translating the phrase “jinkou dafu xiahua (the sharp decline in imports)” and the phrase “maoyi shuncha (the trade surplus)”, but SMT can produce correct results when translating these two phrases. BIBREF6 argues that the reason behind this is the use of distributed representations of words in NMT makes systems often generate words that seem natural in the context, but do not reflect the content of the source sentence. Traditional SMT can avoid this problem as it produces the translations based on phrase mappings.
> 
> Therefore, it will be beneficial to combine SMT and NMT to alleviate the previously mentioned problem. Actually, researchers have made some effective attempts to achieve this goal. Earlier studies were based on the SMT framework, and have been deeply discussed in BIBREF8 . Later, the researchers transfers to NMT framework. Specifically, coverage mechanism BIBREF9 , BIBREF10 , SMT features BIBREF11 , BIBREF12 , BIBREF13 , BIBREF14 , BIBREF15 and translation lexicons BIBREF6 , BIBREF16 , BIBREF17 have been fully explored. In contrast, phrase translation table, as the core of SMT, has not been fully studied. Recently, BIBREF18 and BIBREF19 explore the possibility of translating phrases in NMT. However, the “phrase” in their approaches are different from that used in phrase-based SMT. In BIBREF18 's models, the phrase pair must be a one-to-one mapping with a source phrase having a unique target phrase (named entity translation pairs). In BIBREF19 's models, the source side of a phrase pair must be a chunk. Therefore, it is still a big challenge to incorporate any phrase pair in the phrase table into NMT system to alleviate the unfaithfulness problem.
> 
> In this

### Relevance

Label: 

## Record 0596

Paper: Supervised and Unsupervised Transfer Learning for Question Answering

### Question

> How different is the dataset size of source and target?

### Passage

> The results are shown in Table 3 . As expected, the more training data is used for fine-tuning, the better the model's performance is. We also observe that the extent of improvement from using 0% to 25% of target training data is consistently larger than using from 25% to 50%, 50% to 75%, and 75% to 100%. Using the QACNN fine-tuned on TOEFL-manual as an example, the accuracy of the QACNN improves by 2.7% when varying the training size from 0% to 25%, but only improves by 0.9%, 0.5%, and 0.7% when varying the training size from 25% to 50%, 50% to 75%, and 75% to 100%, respectively.
> 
> We also vary the size of MovieQA for pre-training to study how large the source dataset should be to make transfer learning feasible. The results are shown in Table 4 . We find that even a small amount of source data can help. For example, by using only 25% of MovieQA for pre-training, the accuracy increases 6.3% on MC160. This is because 25% of MovieQA training set (2,462 examples) is still much larger than the MC160 training set (280 examples). As the size of the source dataset increases, the performance of QACNN continues to improve.
> 
> We are interested in understanding what types of questions benefit the most from transfer learning. According to the official guide to the TOEFL test, the questions in TOEFL can be divided into 3 types. Type 1 questions are for basic comprehension of the story. Type 2 questions go beyond basic comprehension, but test the understanding of the functions of utterances or the attitude the speaker expresses. Type 3 questions further require the ability of making connections between different parts of the story, making inferences, drawing conclusions, or forming generalizations. We used the split provided by BIBREF33 , which contains 70/18/34 Type 1/2/3 questions. We compare the performance of the QACNN and MemN2N on different types of questions in TOEFL-manual with and without pre-training on MovieQA, and show the results in Figure 2 . From Figure 2 we can observe that for both the QACNN and MemN2N, their performance on all three types of questions improves after pre-training, showing that the effectiveness of

### Relevance

Label: 

## Record 0597

Paper: Supervised and Unsupervised Transfer Learning for Question Answering

### Question

> How different is the dataset size of source and target?

### Passage

> Transfer learning BIBREF7 is a vital machine learning technique that aims to use the knowledge learned from one task and apply it to a different, but related, task in order to either reduce the necessary fine-tuning data size or improve performance. Transfer learning, also known as domain adaptation, has achieved success in numerous domains such as computer vision BIBREF8 , ASR BIBREF9 , BIBREF10 , and NLP BIBREF11 , BIBREF12 . In computer vision, deep neural networks trained on a large-scale image classification dataset such as ImageNet BIBREF13 have proven to be excellent feature extractors for a broad range of visual tasks such as image captioning BIBREF14 , BIBREF15 , BIBREF16 and visual question answering BIBREF17 , BIBREF18 , BIBREF19 , BIBREF20 , among others. In NLP, transfer learning has also been successfully applied to tasks like sequence tagging BIBREF21 , syntactic parsing BIBREF22 and named entity recognition BIBREF23 , among others.
> 
> The procedure of transfer learning in this work is straightforward and includes two steps. The first step is to pre-train the model on one MCQA dataset referred to as the source task, which usually contains abundant training data. The second step is to fine-tune the same model on the other MCQA dataset, which is referred to as the target task, that we actually care about, but that usually contains much less training data. The effectiveness of transfer learning is evaluated by the model's performance on the target task.
> 
> In supervised transfer learning, both the source and target datasets provide the correct answer to each question during pre-training and fine-tuning, and the QA model is guided by the correct answer to optimize its objective function in a supervised manner in both stages.
> 
> We also consider unsupervised transfer learning where the correct answer to each question in the target dataset is not available. In other words, the entire process is supervised during pre-training, but unsupervised during fine-tuning. A self-labeling technique inspired by BIBREF26 , BIBREF24 , BIBREF25 is used during fine-tuning on the target dataset. We present the proposed algorithm for unsupervised transfer learning in Algorithm "Conclusion and Future Work" . [!htbp] Unsupervised QA Transfer Learning [1] Source dataset with correct answer to each question;

### Relevance

Label: 

## Record 0598

Paper: Supervised and Unsupervised Transfer Learning for Question Answering

### Question

> How different is the dataset size of source and target?

### Passage

> was fine-tuned. Note that for training the QACNN, we followed the same procedure as in BIBREF35 , whereby pre-trained GloVe word vectors BIBREF37 were used to initialize the embedding layer, which were not updated during training. Thus, the embedding layer does not depend on the training set, and the effective vocabularies are the same.
> 
> It is interesting to see that fine-tuning the entire QACNN doesn't necessarily produce the best result. For MC500, the accuracy of QACNN drops by 4.6% compared to just fine-tuning the last two fully-connected layers (rows (f) vs. (e)). We conjecture that this is due to the amount of training data of the target datasets - when the training set of the target dataset is too small, fine-tuning all the parameters of a complex model like QACNN may result in overfitting. This discovery aligns with other domains where transfer learning is well-studied such as object recognition BIBREF38 .
> 
> We expected to see that a MemN2N, when trained directly on the target dataset without pre-training on MovieQA, would outperform a MemN2N pre-trained on MovieQA without fine-tuning on the target dataset (rows (g) vs. (h)), since the model is evaluated on the target dataset. However, for the QACNN this is surprisingly not the case - QACNN pre-trained on MovieQA without fine-tuning on the target dataset outperforms QACNN trained directly on the target dataset without pre-training on MovieQA (rows (b) vs. (a)). We attribute this to the limited size of the target dataset and the complex structure of the QACNN.
> 
> We conducted experiments to study the relationship between the amount of training data from the target dataset for fine-tuning the model and the performance. We first pre-train the models on MovieQA, then vary the training data size of the target dataset used to fine-tune them. Note that for QACNN, we only fine-tune the last two fully-connected layers instead of the entire model, since doing so usually produces the best performance according to Table 2 . The results are shown in Table 3 . As expected, the more training data is used for fine-tuning, the better the model's performance is. We also observe that the extent of improvement from using 0% to 25% of target training

### Relevance

Label: 

## Record 0599

Paper: Supervised and Unsupervised Transfer Learning for Question Answering

### Question

> How different is the dataset size of source and target?

### Passage

> In this paper we demonstrate that a simple transfer learning technique can be very useful for the task of multi-choice question answering. We use a QACNN and a MemN2N as QA models, with MovieQA as the source task and a TOEFL listening comprehension test and MCTest as the target tasks. By pre-training on MovieQA, the performance of both models on the target datasets improves significantly. The models also require much less training data from the target dataset to achieve similar performance to those without pre-training. We also conduct experiments to study the influence of transfer learning on different types of questions, and show that the effectiveness of transfer learning is not limited to specific types of questions. Finally, we show that by a simple iterative self-labeling technique, transfer learning is still useful, even when the correct answers for target QA dataset examples are not available, through quantitative results and visual analysis.
> 
> One area of future research will be generalizing the transfer learning results presented in this paper to other QA models and datasets. In addition, since the original data format of the TOEFL listening comprehension test is audio instead of text, it is worth trying to initialize the embedding layer of the QACNN with semantic or acoustic word embeddings learned directly from speech BIBREF39 , BIBREF40 , BIBREF41 instead of those learned from text BIBREF42 , BIBREF37 .

### Relevance

Label: 

## Record 0600

Paper: Supervised and Unsupervised Transfer Learning for Question Answering

### Question

> How different is the dataset size of source and target?

### Passage

> So far, we have studied the property of supervised transfer learning for QA, which means that during pre-training and fine-tuning, both the source and target datasets provide the correct answer for each question. We now conduct unsupervised transfer learning experiments described in Section "Conclusion and Future Work" (Algorithm "Conclusion and Future Work" ), where the answers to the questions in the target dataset are not available. We used QACNN as the QA model and all the parameters $(E, W_{CNN}^{(1)}, W_{CNN}^{(2)}, W_{FC}^{(1)},$ and $W_{FC}^{(2)})$ were updated during fine-tuning in this experiment. Since the range of the testing accuracy of the TOEFL-series (TOEFL-manual and TOEFL-ASR) is different from that of MCTest (MC160 and MC500), their results are displayed separately in Figure UID29 and Figure UID30 , respectively.
> 
> From Figure UID29 and Figure UID30 we can observe that without ground truth in the target dataset for supervised fine-tuning, transfer learning from a source dataset can still improve the performance through a simple iterative self-labeling mechanism. For TOEFL-manual and TOEFL-ASR, QACNN achieves the highest testing accuracy at Epoch 7 and 8, outperforming its counterpart without fine-tuning by approximately 4% and 5%, respectively. For MC160 and MC500, the QACNN achieves the peak at Epoch 3 and 6, outperforming its counterpart without fine-tuning by about 2% and 6%, respectively. The results also show that the performance of unsupervised transfer learning is still worse than supervised transfer learning, which is not surprising, but the effectiveness of unsupervised transfer learning when no ground truth labels are provided is validated.
> 
> To better understand the unsupervised transfer learning process of QACNN, we visualize the changes of the word-level attention map during training Epoch 1, 4, 7, and 10 in Figure 4 . We use the same question from TOEFL-manual as shown in Table 1 as an example. From Figure 4 we can observe that as the training epochs increase, the QACNN focuses more on the context in the story that is related to the question and the correct answer choice. For example, the correct answer is related to “class project”. In Epoch 1 and 4, the model does not focus on the phrase “class representation”, but the model attends on the phrase in Epoch 7

### Relevance

Label: 
