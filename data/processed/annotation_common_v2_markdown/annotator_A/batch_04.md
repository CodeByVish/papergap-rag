# Passage relevance annotation

Annotator: 

Enter your name or agreed identifier after `Annotator:`.

Judge whether each passage helps answer the question, including useful partial evidence. Topic overlap alone is insufficient.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Preserve all content and record numbers. Work independently; do not exchange labels before submission. Algorithm sources are disclosed.

## Question 0061

Paper: A Human-AI Loop Approach for Joint Keyword Discovery and Expectation Estimation in Micropost Event Detection

> What type of classifiers are used?

### Common Retrieved Chunks

#### Passage 471

Retrieved by: BM25, Dense, Hybrid

> Event detection on microblogging platforms such as Twitter aims to detect events preemptively. A main task in event detection is detecting events of predetermined types BIBREF0, such as concerts or controversial events based on microposts matching specific event descriptions. This task has extensive applications ranging from cyber security BIBREF1, BIBREF2 to political elections BIBREF3 or public health BIBREF4, BIBREF5. Due to the high ambiguity and inconsistency of the terms used in microposts, event detection is generally performed though statistical machine learning models, which require a labeled dataset for model training. Data labeling is, however, a long, laborious, and usually costly process. For the case of micropost classification, though positive labels can be collected (e.g., using specific hashtags, or event-related date-time information), there is no straightforward way to generate negative labels useful for model training. To tackle this lack of negative labels and the significant manual efforts in data labeling, BIBREF1 (BIBREF1, BIBREF3) introduced a weak supervision based learning approach, which uses only positively labeled data, accompanied by unlabeled examples by filtering microposts that contain a certain keyword indicative of the event type under consideration (e.g., `hack' for cyber security). Another key technique in this context is expectation regularization BIBREF6, BIBREF7, BIBREF1. Here, the estimated proportion of relevant microposts in an unlabeled dataset containing a keyword is given as a keyword-specific expectation. This expectation is used in the regularization term of the model's objective function to constrain the posterior distribution of the model predictions. By doing so, the model is trained with an expectation on its prediction for microposts that contain the keyword. Such a method, however, suffers from two key problems:
> 
> Due to the unpredictability of event occurrences and the constantly changing dynamics of users' posting frequency BIBREF8, estimating the expectation associated with a keyword is a challenging task, even for domain experts;
> 
> The performance of the event detection model is constrained by the informativeness of the keyword used for model training. As of now, we lack a principled method for discovering new keywords and improve the model performance.
> 
> To address the above issues, we advocate a human-AI loop approach for discovering informative keywords and estimating their expectations reliably. Our approach iteratively leverages 1) crowd

#### Relevance 471

Label: 

#### Passage 472

Retrieved by: BM25, Dense, Hybrid

> Datasets. We perform our experiments with two predetermined event categories: cyber security (CyberAttack) and death of politicians (PoliticianDeath). These event categories are chosen as they are representative of important event types that are of interest to many governments and companies. The need to create our own dataset was motivated by the lack of public datasets for event detection on microposts. The few available datasets do not suit our requirements. For example, the publicly available Events-2012 Twitter dataset BIBREF20 contains generic event descriptions such as Politics, Sports, Culture etc. Our work targets more specific event categories BIBREF21. Following previous studies BIBREF1, we collect event-related microposts from Twitter using 11 and 8 seed events (see Section SECREF2) for CyberAttack and PoliticianDeath, respectively. Unlabeled microposts are collected by using the keyword `hack' for CyberAttack, while for PoliticianDeath, we use a set of keywords related to `politician' and `death' (such as `bureaucrat', `dead' etc.) For each dataset, we randomly select 500 tweets from the unlabeled subset and manually label them for evaluation. Table TABREF25 shows key statistics from our two datasets.
> 
> Comparison Methods. To demonstrate the generality of our approach on different event detection models, we consider Logistic Regression (LR) BIBREF1 and Multilayer Perceptron (MLP) BIBREF2 as the target models. As the goal of our experiments is to demonstrate the effectiveness of our approach as a new model training technique, we use these widely used models. Also, we note that in our case other neural network models with more complex network architectures for event detection, such as the bi-directional LSTM BIBREF17, turn out to be less effective than a simple feedforward network. For both LR and MLP, we evaluate our proposed human-AI loop approach for keyword discovery and expectation estimation by comparing against the weakly supervised learning method proposed by BIBREF1 (BIBREF1) and BIBREF17 (BIBREF17) where only one initial keyword is used with an expectation estimated by an individual expert.
> 
> Parameter Settings. We empirically set optimal parameters based on a held-out validation set that contains 20% of the test data. These include the hyperparamters of the target model, those of our proposed probabilistic model, and the parameters used for training the target model. We explore MLP with 1, 2

#### Relevance 472

Label: 

#### Passage 473

Retrieved by: BM25, Hybrid

> we lack a principled method for discovering new keywords and improve the model performance.
> 
> To address the above issues, we advocate a human-AI loop approach for discovering informative keywords and estimating their expectations reliably. Our approach iteratively leverages 1) crowd workers for estimating keyword-specific expectations, and 2) the disagreement between the model and the crowd for discovering new informative keywords. More specifically, at each iteration after we obtain a keyword-specific expectation from the crowd, we train the model using expectation regularization and select those keyword-related microposts for which the model's prediction disagrees the most with the crowd's expectation; such microposts are then presented to the crowd to identify new keywords that best explain the disagreement. By doing so, our approach identifies new keywords which convey more relevant information with respect to existing ones, thus effectively boosting model performance. By exploiting the disagreement between the model and the crowd, our approach can make efficient use of the crowd, which is of critical importance in a human-in-the-loop context BIBREF9, BIBREF10. An additional advantage of our approach is that by obtaining new keywords that improve model performance over time, we are able to gain insight into how the model learns for specific event detection tasks. Such an advantage is particularly useful for event detection using complex models, e.g., deep neural networks, which are intrinsically hard to understand BIBREF11, BIBREF12. An additional challenge in involving crowd workers is that their contributions are not fully reliable BIBREF13. In the crowdsourcing literature, this problem is usually tackled with probabilistic latent variable models BIBREF14, BIBREF15, BIBREF16, which are used to perform truth inference by aggregating a redundant set of crowd contributions. Our human-AI loop approach improves the inference of keyword expectation by aggregating contributions not only from the crowd but also from the model. This, however, comes with its own challenge as the model's predictions are further dependent on the results of expectation inference, which is used for model training. To address this problem, we introduce a unified probabilistic model that seamlessly integrates expectation inference and model training, thereby allowing the former to benefit from the latter while resolving the inter-dependency between the two.
> 
> To the best of our knowledge, we are

#### Relevance 473

Label: 

#### Passage 475

Retrieved by: BM25, Hybrid

> selected with the highest disagreement (Eq. DISPLAY_FORM7), whose likelihood of being event-related as predicted by the model is $99.9\%$, is shown as an example below:
> 
> RT @xxx: Hong Kong securities brokers hit by cyber attacks, may face more: regulator #cyber #security #hacking https://t.co/rC1s9CB
> 
> This micropost contains keywords that can better indicate the relevance to a cyber security event than the initial keyword `hack', e.g., `securities', `hit', and `attack'.
> 
> Note that when the keyword-specific expectation $e^{(t)}$ in Equation DISPLAY_FORM7 is high, the selected microposts will be the ones that contain keywords indicating the irrelevance of the microposts to an event category. Such keywords are also useful for model training as they help improve the model's ability to identify irrelevant microposts.
> 
> To identify new keywords in the selected microposts, we again leverage crowdsourcing, as humans are typically better than machines at providing specific explanations BIBREF18, BIBREF19. In the crowdsourcing task, workers are first asked to find those microposts where the model predictions are deemed correct. Then, from those microposts, workers are asked to find the keyword that best indicates the class of the microposts as predicted by the model. The keyword most frequently identified by the workers is then used as the initial keyword for the following iteration. In case multiple keywords are selected, e.g., the top-$N$ frequent ones, workers will be asked to perform $N$ micropost classification tasks for each keyword in the next iteration, and the model training will be performed on multiple keyword-specific expectations.

#### Relevance 475

Label: 

#### Passage 476

Retrieved by: Dense, Hybrid

> Given a set of labeled and unlabeled microposts, our goal is to extract informative keywords and estimate their expectations in order to train a machine learning model. To achieve this goal, our proposed human-AI loop approach comprises two crowdsourcing tasks, i.e., micropost classification followed by keyword discovery, and a unified probabilistic model for expectation inference and model training. Figure FIGREF6 presents an overview of our approach. Next, we describe our approach from a process-centric perspective.
> 
> Following previous studies BIBREF1, BIBREF17, BIBREF2, we collect a set of unlabeled microposts $\mathcal {U}$ from a microblogging platform and post-filter, using an initial (set of) keyword(s), those microposts that are potentially relevant to an event category. Then, we collect a set of event-related microposts (i.e., positively labeled microposts) $\mathcal {L}$, post-filtering with a list of seed events. $\mathcal {U}$ and $\mathcal {L}$ are used together to train a discriminative model (e.g., a deep neural network) for classifying the relevance of microposts to an event. We denote the target model as $p_\theta (y|x)$, where $\theta $ is the model parameter to be learned and $y$ is the label of an arbitrary micropost, represented by a bag-of-words vector $x$. Our approach iterates several times $t=\lbrace 1, 2, \ldots \rbrace $ until the performance of the target model converges. Each iteration starts from the initial keyword(s) or the new keyword(s) discovered in the previous iteration. Given such a keyword, denoted by $w^{(t)}$, the iteration starts by sampling microposts containing the keyword from $\mathcal {U}$, followed by dynamically creating micropost classification tasks and publishing them on a crowdsourcing platform.
> 
> Micropost Classification. The micropost classification task requires crowd workers to label the selected microposts into two classes: event-related and non event-related. In particular, workers are given instructions and examples to differentiate event-instance related microposts and general event-category related microposts. Consider, for example, the following microposts in the context of Cyber attack events, both containing the keyword `hack':
> 
> Credit firm Equifax says 143m Americans' social security numbers exposed in hack
> 
> This micropost describes an instance of a cyber attack event that the target model should identify. This is, therefore, an event-instance related micropost and should be considered as a positive example. Contrast this with the

#### Relevance 476

Label: 

### BM25

#### Passage 474

Retrieved by: BM25

> To demonstrate the cost-effectiveness of using crowdsourcing for obtaining new keywords and consequently, their expectations, we compare the performance of our approach with an approach using crowdsourcing to only label microposts for model training at the same cost. Specifically, we conducted an additional crowdsourcing experiment where the same cost used for keyword discovery in our approach is used to label additional microposts for model training. These newly labeled microposts are used with the microposts labeled in the micropost classification task of our approach (see Section SECREF2: Micropost Classification) and the expectation of the initial keyword to train the model for comparison. The model trained in this way increases AUC by 0.87% for CyberAttack, and by 1.06% for PoliticianDeath; in comparison, our proposed approach increases AUC by 33.42% for PoliticianDeath and by 15.23% for CyberAttack over the baseline presented by BIBREF1). These results show that using crowdsourcing for keyword discovery is significantly more cost-effective than simply using crowdsourcing to get additional labels when training the model.

#### Relevance 474

Label: 

### Dense

#### Passage 477

Retrieved by: Dense

> Event Detection. The techniques for event extraction from microblogging platforms can be classified according to their domain specificity and their detection method BIBREF0. Early works mainly focus on open domain event detection BIBREF25, BIBREF26, BIBREF27. Our work falls into the category of domain-specific event detection BIBREF21, which has drawn increasing attention due to its relevance for various applications such as cyber security BIBREF1, BIBREF2 and public health BIBREF4, BIBREF5. In terms of technique, our proposed detection method is related to the recently proposed weakly supervised learning methods BIBREF1, BIBREF17, BIBREF3. This comes in contrast with fully-supervised learning methods, which are often limited by the size of the training data (e.g., a few hundred examples) BIBREF28, BIBREF29.
> 
> Human-in-the-Loop Approaches. Our work extends weakly supervised learning methods by involving humans in the loop BIBREF13. Existing human-in-the-loop approaches mainly leverage crowds to label individual data instances BIBREF9, BIBREF10 or to debug the training data BIBREF30, BIBREF31 or components BIBREF32, BIBREF33, BIBREF34 of a machine learning system. Unlike these works, we leverage crowd workers to label sampled microposts in order to obtain keyword-specific expectations, which can then be generalized to help classify microposts containing the same keyword, thus amplifying the utility of the crowd. Our work is further connected to the topic of interpretability and transparency of machine learning models BIBREF11, BIBREF35, BIBREF12, for which humans are increasingly involved, for instance for post-hoc evaluations of the model's interpretability. In contrast, our approach directly solicits informative keywords from the crowd for model training, thereby providing human-understandable explanations for the improved model.

#### Relevance 477

Label: 

#### Passage 478

Retrieved by: Dense

> a held-out validation set that contains 20% of the test data. These include the hyperparamters of the target model, those of our proposed probabilistic model, and the parameters used for training the target model. We explore MLP with 1, 2 and 3 hidden layers and apply a grid search in 32, 64, 128, 256, 512 for the dimension of the embeddings and that of the hidden layers. For the coefficient of expectation regularization, we follow BIBREF6 (BIBREF6) and set it to $\lambda =10 \times $ #labeled examples. For model training, we use the Adam BIBREF22 optimization algorithm for both models.
> 
> Evaluation. Following BIBREF1 (BIBREF1) and BIBREF3 (BIBREF3), we use accuracy and area under the precision-recall curve (AUC) metrics to measure the performance of our proposed approach. We note that due to the imbalance in our datasets (20% positive microposts in CyberAttack and 27% in PoliticianDeath), accuracy is dominated by negative examples; AUC, in comparison, better characterizes the discriminative power of the model.
> 
> Crowdsourcing. We chose Level 3 workers on the Figure-Eight crowdsourcing platform for our experiments. The inter-annotator agreement in micropost classification is taken into account through the EM algorithm. For keyword discovery, we filter keywords based on the frequency of the keyword being selected by the crowd. In terms of cost-effectiveness, our approach is motivated from the fact that crowdsourced data annotation can be expensive, and is thus designed with minimal crowd involvement. For each iteration, we selected 50 tweets for keyword discovery and 50 tweets for micropost classification per keyword. For a dataset with 80k tweets (e.g., CyberAttack), our approach only requires to manually inspect 800 tweets (for 8 keywords), which is only 1% of the entire dataset.

#### Relevance 478

Label: 

### Hybrid

None

## Question 0062

Paper: Author Profiling for Hate Speech Detection

> What is the drawback to methods that rely on textual cues?

### Common Retrieved Chunks

#### Passage 479

Retrieved by: BM25, Dense, Hybrid

> We conduct a qualitative analysis of system errors and the cases where author profiling leads to the correct classification of previously misclassified examples. Table 3 shows examples of hateful tweets from the dataset that are misclassified by the lr method, but are correctly classified upon the addition of author profiling features, i.e., by the lr + auth method. It is worth noting that some of the wins scored by the latter are on tweets that are part of a larger hateful discourse or contain links to hateful content while not explicitly having textual cues that are indicative of hate speech per se. The addition of author profiling features may then be viewed as a proxy for wider discourse information, thus allowing us to correctly resolve the cases where lexical and semantic features alone are insufficient.
> 
> However, a number of hateful tweets still remain misclassified despite the addition of author profiling features. According to our analysis, many of these tend to contain urls to hateful content, e.g., “@salmonfarmer1: Logic in the world of Islam http://t.co/6nALv2HPc3" and “@juliarforster Yes. http://t.co/ixbt0uc7HN". Since Twitter shortens all urls into a standard format, there is no indication of what they refer to. One way to deal with this limitation could be to additionally maintain a blacklist of links. Another source of system errors is the deliberate obfuscation of words by authors in order to evade detection, e.g., “Kat, a massive c*nt. The biggest ever on #mkr #cuntandandre". Current hate speech detection methods, including ours, do not directly attempt to address this issue. While this is a challenge for bag-of-word based methods such as lr, we hypothesize that neural networks operating at the character level may be helpful in recognizing obfuscated words.
> 
> We further conducted an analysis of the author embeddings generated by node2vec, in order to validate that they capture the relevant aspects of the community graph. We visualized the author embeddings in 2-dimensional space using t-sne BIBREF24 , as shown in Figure 2 . We observe that, as in the community graph, there are a few densely populated regions in the visualization that represent authors in closely knit groups who exhibit similar characteristics. The other regions are largely sparse with

#### Relevance 479

Label: 

#### Passage 480

Retrieved by: BM25, Dense, Hybrid

> This work is licensed under a Creative Commons Attribution 4.0 International License.
> 
> License details: http://creativecommons.org/licenses/by/4.0/. Hate speech, a term used to collectively refer to offensive language, racist comments, sexist remarks, etc., is omnipresent in social media. Users on social media platforms are at risk of being exposed to content that may not only be degrading but also harmful to their mental health in the long term. Pew Research Center highlighted the gravity of the situation via a recently released report BIBREF0 . As per the report, 40% of adult Internet users have personally experienced harassment online, and 60% have witnessed the use of offensive names and expletives. Expectedly, the majority (66%) of those who have personally faced harassment have had their most recent incident occur on a social networking website or app. While most of these websites and apps provide ways of flagging offensive and hateful content, only 8.8% of the victims have actually considered using such provisions. These statistics suggest that passive or manual techniques for curbing propagation of hateful content (such as flagging) are neither effective nor easily scalable BIBREF1 . Consequently, the efforts to automate the detection and moderation of such content have been gaining popularity in natural language processing (nlp) BIBREF2 , BIBREF3 .
> 
> Several approaches to hate speech detection demonstrate the effectiveness of character-level bag-of-words features in a supervised classification setting BIBREF4 , BIBREF5 , BIBREF6 . More recent approaches, and currently the best performing ones, utilize recurrent neural networks (rnns) to transform content into dense low-dimensional semantic representations that are then used for classification BIBREF1 , BIBREF7 . All of these approaches rely solely on lexical and semantic features of the text they are applied to. Waseem and Hovy c53cecce142c48628b3883d13155261c adopted a more user-centric approach based on the idea that perpetrators of hate speech are usually segregated into small demographic groups; they went on to show that gender information of authors (i.e., users who have posted content) is a helpful indicator. However, Waseem and Hovy focused only on coarse demographic features of the users, disregarding information about their communication with others. But previous research suggests that users who subscribe to particular stereotypes that promote hate speech tend to form

#### Relevance 480

Label: 

#### Passage 481

Retrieved by: BM25, Dense, Hybrid

> Author profiling has been leveraged in several ways for a variety of purposes in nlp. For instance, many studies have relied on demographic information of the authors. Amongst these are Hovy et al. hovy2015demographic and Ebrahimi et al. ebrahimi2016personalized who extracted age and gender-related information to achieve superior performance in a text classification task. Pavalanathan and Eisenstein pavalanathan2015confounds, in their work, further showed the relevance of the same information to automatic text-based geo-location. Researching along the same lines, Johannsen et al. johannsen2015cross and Mirkin et al. mirkin2015motivating utilized demographic factors to improve syntactic parsing and machine translation respectively.
> 
> While demographic information has proved to be relevant for a number of tasks, it presents a significant drawback: since this information is not always available for all authors in a social network, it is not particularly reliable. Consequently, of late, a new line of research has focused on creating representations of users in a social network by leveraging the information derived from the connections that they have with other users. In this case, node representations (where nodes represent the authors in the social network) are typically induced using neural architectures. Given the graph representing the social network, such methods create low-dimensional representations for each node, which are optimized to predict the nodes close to it in the network. This approach has the advantage of overcoming the absence of information that the previous approaches face. Among those that implement this idea are Yang et al. yang2016toward, who used representations derived from a social graph to achieve better performance in entity linking tasks, and Chen and Ku chen2016utcnn, who used them for stance classification.
> 
> A considerable amount of literature has also been devoted to sentiment analysis with representations built from demographic factors BIBREF10 , BIBREF12 . Other tasks that have benefited from social representations are sarcasm detection BIBREF13 and political opinion prediction BIBREF14 .

#### Relevance 481

Label: 

#### Passage 482

Retrieved by: BM25, Hybrid

> helpful indicator. However, Waseem and Hovy focused only on coarse demographic features of the users, disregarding information about their communication with others. But previous research suggests that users who subscribe to particular stereotypes that promote hate speech tend to form communities online. For example, Zook zook mapped the locations of racist tweets in response to President Obama's re-election to show that such tweets were not uniformly distributed across the United States but formed clusters instead. In this paper, we present the first approach to hate speech detection that leverages author profiling information based on properties of the authors' social network and investigate its effectiveness.
> 
> Author profiling has emerged as a powerful tool for NLP applications, leading to substantial performance improvements in several downstream tasks, such as text classification, sentiment analysis and author attribute identification BIBREF8 , BIBREF9 , BIBREF10 . The relevance of information gained from it is best explained by the idea of homophily, i.e., the phenomenon that people, both in real life as well as on the Internet, tend to associate more with those who appear similar. Here, similarity can be defined along various axes, e.g., location, age, language, etc. The strength of author profiling lies in that if we have information about members of a community $c$ defined by some similarity criterion, and we know that the person $p$ belongs to $c$ , we can infer information about $p$ . This concept has a straightforward application to our task: knowing that members of a particular community are prone to creating hateful content, and knowing that the author p is connected to this community, we can leverage information beyond linguistic cues and more accurately predict the use of hateful/non-hateful language from $p$ . The questions that we seek to address here are: are some authors, and the respective communities that they belong to, more hateful than the others? And can such information be effectively utilized to improve the performance of automated hate speech detection methods?
> 
> In this paper, we answer these questions and develop novel methods that take into account community-based profiling features of authors when examining their tweets for hate speech. Experimenting with a dataset of $16k$ tweets, we show that the

#### Relevance 482

Label: 

#### Passage 484

Retrieved by: Dense, Hybrid

> We perform 10-fold stratified cross validation (cv), as suggested by Forman and Scholz Forman:10, to evaluate all seven methods described in the previous section. Following previous research BIBREF7 , BIBREF23 , we report the average weighted precision, recall, and f $_1$ scores for all the methods. The average weighted precision is calculated as:
> 
> $$\nonumber \frac{\sum _{i=1}^{10}\; (w_r\cdot \textrm {P}_r^i + w_s\cdot \textrm {P}_s^i + w_n\cdot \textrm {P}_n^i)}{10}$$   (Eq. 16)
> 
> where $\textrm {P}_r^i, \textrm {P}_s^i, \textrm {P}_n^i$ are precision scores on the racism, sexism, and none classes from the $i^{th}$ fold of the cv. The values $w_r$ , $w_s$ , and $w_n$ are the proportions of the racism, sexism, and none classes in the dataset respectively; since we use stratification, these proportions are constant ( $w_r=0.12$ , $w_s=0.19$ , $w_n=0.69$ ) across all folds. Average weighted recall and f $_1$ are calculated in the same manner.
> 
> The results are presented in Table 1 . For all three baseline methods (lr, ws, and hs), the addition of author profiling features significantly improves performance ( $p < 0.05$ under 10-fold cv paired t-test). The lr + auth method yields the highest performance of f $_1$ $=87.57$ , exceeding its respective baseline by nearly 4 points. A similar trend can be observed for the other methods as well. These results point to the importance of community-based information and author profiling in hate speech detection and demonstrate that our approach can further improve the performance of existing state-of-the-art methods.
> 
> In Table 2 , we further compare the performance of the different methods on the racism and sexism classes individually. As in the previous experiments, the scores are averaged over 10 folds of cv. Of particular interest are the scores for the sexism class where the f $_1$ increases by over 10 points upon the addition of author profiling features. Upon analysis, we find that such a substantial increase in performance stems from the fact that many of the 527 unique authors of the sexist tweets are closely connected in the community graph. This allows for their penchant for sexism to be expressed in their respective author profiles.
> 
> The author profiling features on their own (auth) achieve impressive results overall and

#### Relevance 484

Label: 

### BM25

#### Passage 483

Retrieved by: BM25

> the ones that do not get tuned lie closely clustered around the oov token, to which unseen words in the test set are mapped.
> 
> Word-sum (ws). As a third baseline, we adopt the “lstm+glove+gbdt" method of Badjatiya et al. Badjatiya:17, which achieves state-of-the-art results on the Twitter dataset we are using. The authors first utilize an lstm to task-tune glove-initialized word embeddings by propagating the error back from an lr layer. They then train a gradient boosted decision tree (gbdt) classifier to classify texts based on the average of the embeddings of constituent words. We make two minor modifications to this method: we use a 2-layer gru instead of the lstm to tune the embeddings, and we train the gbdt classifier on the l $_2$ -normalized sum of the embeddings instead of their average. Although the authors achieved state-of-the-art results on Twitter by initializing embeddings randomly rather than with glove (which is what we do here), we found the opposite when performing a 10-fold stratified cross-validation (cv). A possible explanation of this lies in the authors' decision to not use stratification, which for such a highly imbalanced dataset can lead to unexpected outcomes BIBREF18 . Furthermore, the authors train their lstm on the entire dataset (including the test set) without any early stopping criterion, which leads to over-fitting of the randomly-initialized embeddings.
> 
> Author profile (auth). In order to test whether community-based information of authors is in itself sufficient to correctly classify the content produced by them, we utilize just the author profiles we generated to train a gbdt classifier.
> 
> Char n-grams + author profile (lr + auth). This method builds upon the lr baseline by appending author profile vectors on to the character n-gram count vectors for training the lr classifier.
> 
> Hidden-state + author profile (hs + auth) and Word-sum + author profile (ws + auth). These methods are identical to the char n-grams + author profile method except that here we append the author profiling features on to features derived from the hidden-state and word-sum baselines respectively and feed them to a gbdt classifier.

#### Relevance 483

Label: 

### Dense

#### Passage 485

Retrieved by: Dense

> detection methods?
> 
> In this paper, we answer these questions and develop novel methods that take into account community-based profiling features of authors when examining their tweets for hate speech. Experimenting with a dataset of $16k$ tweets, we show that the addition of such profiling features to the current state-of-the-art methods for hate speech detection significantly enhances their performance. We also release our code (including code that replicates previous work), pre-trained models and the resources we used in the public domain.

#### Relevance 485

Label: 

### Hybrid

None

## Question 0063

Paper: Predicting the Type and Target of Offensive Posts in Social Media

> What is the definition of offensive language?

### Common Retrieved Chunks

#### Passage 486

Retrieved by: BM25, Hybrid

> Level C categorizes the targets of insults and threats as individual (IND), group (GRP), and other (OTH).
> 
> Individual (IND): Posts targeting an individual. It can be a a famous person, a named individual or an unnamed participant in the conversation. Insults and threats targeted at individuals are often defined as cyberbulling.
> 
> Group (GRP): The target of these offensive posts is a group of people considered as a unity due to the same ethnicity, gender or sexual orientation, political affiliation, religious belief, or other common characteristic. Many of the insults and threats targeted at a group correspond to what is commonly understood as hate speech.
> 
> Other (OTH): The target of these offensive posts does not belong to any of the previous two categories (e.g. an organization, a situation, an event, or an issue).

#### Relevance 486

Label: 

#### Passage 487

Retrieved by: BM25, Dense, Hybrid

> This paper presents OLID, a new dataset with annotation of type and target of offensive language. OLID is the official dataset of the shared task SemEval 2019 Task 6: Identifying and Categorizing Offensive Language in Social Media (OffensEval) BIBREF16 . In OffensEval, each annotation level in OLID is an independent sub-task. The dataset contains 14,100 tweets and is released freely to the research community. To the best of our knowledge, this is the first dataset to contain annotation of type and target of offenses in social media and it opens several new avenues for research in this area. We present baseline experiments using SVMs and neural networks to identify the offensive tweets, discriminate between insults, threats, and profanity, and finally to identify the target of the offensive messages. The results show that this is a challenging task. A CNN-based sentence classifier achieved the best results in all three sub-tasks.
> 
> In future work, we would like to make a cross-corpus comparison of OLID and datasets annotated for similar tasks such as aggression identification BIBREF2 and hate speech detection BIBREF8 . This comparison is, however, far from trivial as the annotation of OLID is different.

#### Relevance 487

Label: 

#### Passage 488

Retrieved by: BM25, Dense, Hybrid

> Offensive content has become pervasive in social media and a reason of concern for government organizations, online communities, and social media platforms. One of the most common strategies to tackle the problem is to train systems capable of recognizing offensive content, which then can be deleted or set aside for human moderation. In the last few years, there have been several studies published on the application of computational methods to deal with this problem. Most prior work focuses on a different aspect of offensive language such as abusive language BIBREF0 , BIBREF1 , (cyber-)aggression BIBREF2 , (cyber-)bullying BIBREF3 , BIBREF4 , toxic comments INLINEFORM0 , hate speech BIBREF5 , BIBREF6 , BIBREF7 , BIBREF8 , BIBREF9 , BIBREF10 , and offensive language BIBREF11 . Prior work has focused on these aspects of offensive language in Twitter BIBREF3 , BIBREF7 , BIBREF8 , BIBREF11 , Wikipedia comments, and Facebook posts BIBREF2 .
> 
> Recently, Waseem et. al. ( BIBREF12 ) acknowledged the similarities among prior work and discussed the need for a typology that differentiates between whether the (abusive) language is directed towards a specific individual or entity or towards a generalized group and whether the abusive content is explicit or implicit. Wiegand et al. ( BIBREF11 ) followed this trend as well on German tweets. In their evaluation, they have a task to detect offensive vs not offensive tweets and a second task for distinguishing between the offensive tweets as profanity, insult, or abuse. However, no prior work has explored the target of the offensive language, which is important in many scenarios, e.g., when studying hate speech with respect to a specific target.
> 
> Therefore, we expand on these ideas by proposing a a hierarchical three-level annotation model that encompasses:
> 
> Using this annotation model, we create a new large publicly available dataset of English tweets. The key contributions of this paper are as follows:

#### Relevance 488

Label: 

#### Passage 490

Retrieved by: BM25, Dense, Hybrid

> In the OLID dataset, we use a hierarchical annotation model split into three levels to distinguish between whether language is offensive or not (A), and type (B) and target (C) of the offensive language. Each level is described in more detail in the following subsections and examples are shown in Table TABREF10 .

#### Relevance 490

Label: 

#### Passage 491

Retrieved by: Dense, Hybrid

> Level A discriminates between offensive (OFF) and non-offensive (NOT) tweets.
> 
> Not Offensive (NOT): Posts that do not contain offense or profanity;
> 
> Offensive (OFF): We label a post as offensive if it contains any form of non-acceptable language (profanity) or a targeted offense, which can be veiled or direct. This category includes insults, threats, and posts containing profane language or swear words.

#### Relevance 491

Label: 

### BM25

#### Passage 489

Retrieved by: BM25

> The data included in OLID has been collected from Twitter. We retrieved the data using the Twitter API by searching for keywords and constructions that are often included in offensive messages, such as `she is' or `to:BreitBartNews'. We carried out a first round of trial annotation of 300 instances with six experts. The goal of the trial annotation was to 1) evaluate the proposed tagset; 2) evaluate the data retrieval method; and 3) create a gold standard with instances that could be used as test questions in the training and test setting annotation which was carried out using crowdsourcing. The breakdown of keywords and their offensive content in the trial data of 300 tweets is shown in Table TABREF14 . We included a left (@NewYorker) and far-right (@BreitBartNews) news accounts because there tends to be political offense in the comments. One of the best offensive keywords was tweets that were flagged as not being safe by the Twitter `safe' filter (the `-' indicates `not safe'). The vast majority of content on Twitter is not offensive so we tried different strategies to keep a reasonable number of tweets in the offensive class amounting to around 30% of the dataset including excluding some keywords that were not high in offensive content such as `they are` and `to:NewYorker`. Although `he is' is lower in offensive content we kept it as a keyword to avoid gender bias. In addition to the keywords in the trial set, we searched for more political keywords which tend to be higher in offensive content, and sampled our dataset such that 50% of the the tweets come from political keywords and 50% come from non-political keywords. In addition to the keywords `gun control', and `to:BreitbartNews', political keywords used to collect these tweets are `MAGA', `antifa', `conservative' and `liberal'. We computed Fliess' INLINEFORM0 on the trial set for the five annotators on 21 of the tweets. INLINEFORM1 is .83 for Layer A (OFF vs NOT) indicating high agreement. As to normalization and anonymization, no user metadata or Twitter IDs have been stored, and URLs and Twitter mentions have been substituted to placeholders. We follow prior work in related areas (burnap2015cyber,davidson2017automated) and annotate our data using

#### Relevance 489

Label: 

### Dense

#### Passage 492

Retrieved by: Dense

> similar properties and the hierarchical annotation model proposed in this paper aims to capture this. Considering that, for example, an insult targeted at an individual is commonly known as cyberbulling and that insults targeted at a group are known as hate speech, we pose that OLID's hierarchical annotation model makes it a useful resource for various offensive language identification sub-tasks.

#### Relevance 492

Label: 

### Hybrid

None

## Question 0064

Paper: Represent, Aggregate, and Constrain: A Novel Architecture for Machine Reading from Noisy Sources

> what is the size of the dataset?

### Common Retrieved Chunks

#### Passage 493

Retrieved by: BM25, Dense, Hybrid

> The Stanford Plane Crash Dataset BIBREF15 is a small data set consisting of 80 plane crash events, each paired with a set of related news articles. Of these events, 40 are reserved for training, and 40 for testing, with the average cluster containing more than 2,000 mentions. Gold labels for each cluster are derived from Wikipedia infoboxes and cover up to 15 slots, of which 8 are used in evaluation (Figure TABREF54 ).
> 
> We follow the same entity normalization procedure as reschke2014, limit the cluster size to the first 200 documents, and further reduce the number of duplicate documents to prevent biases in aggregation. We partition out every fifth document from the training set to be used as development data, primarily for use in an early stopping criterion. We also construct additional clusters from the remaining training documents, and use this to increase the size of the development set.

#### Relevance 493

Label: 

#### Passage 495

Retrieved by: BM25, Hybrid

> Results are presented in Table TABREF44 . In comparison to previous work, our any configuration of our RAC architecture with sum-based aggregation outperforms the best existing systems by a minimum of 9.8 F INLINEFORM0 . In comparison to the various Mention-CNN systems, it is clear that this improvement is not a result of different features or the use of pre-trained word embeddings, or even the representational power of the CNN-based embeddings. Rather, it is attributable to training end-to-end with aggregation and a cluster-level loss function.
> 
> With respect to aggregation, sum-based methods consistently outperform their max counterparts, indicating that exploiting the redundancy of information in news clusters is beneficial to the task. The topic-based aggregation is statistically significant improvement over standard sum aggregation (p INLINEFORM0 ), and produces the highest performing unconstrained system.
> 
> Date-based aggregation did not yield a statistically significant improvement over sum aggregation. We hypothesize that the method is sound, but accurate datelines could only be extracted for 31 INLINEFORM0 documents. We did not modify the aggregation weights ( INLINEFORM1 ) for the remaining documents, minimizing the effect of this approach.
> 
> The EE-AS Reader has the lowest overall performance, which one can attribute to pooling evidence in a manner that is poorly suited to this problem domain. By placing a softmax over each document's beliefs, what is an advantage in the cloze-style QA setting here becomes a liability: the model is forced to predict a value for every slot, for every each document, even when few are truly mentioned.

#### Relevance 495

Label: 

#### Passage 496

Retrieved by: BM25, Hybrid

> present in the cluster, is determining whether to predict any value at all. A common solution for handling such missing values is the use of a threshold, below which the model returns null. However, even a separate threshold for each slot would not fully capture the nature of the problem.
> 
> Determining whether a value is missing is a trade-off between two factors: (1) how strongly the mention-level scores support a non-null answer, and (2) how much general information regarding that event and that slot is given. We incorporate both factors by extending the definition of INLINEFORM0 and its use in Eq. EQREF9 –Eq. to include not only mentions, but all words. Each non-mention word is treated as a mention of the null value: DISPLAYFORM0
> 
> where INLINEFORM0 is the set of mentions. The resulting null score varies according to both the cluster size and its content. Smaller clusters with fewer documents require less evidence to predict a non-null value, while larger clusters must accumulate more evidence for a particular candidate or a null value will be proposed instead.
> 
> The exact words contained in the cluster also have an effect. For example, clusters with numerous mentions of killed, died, dead, will have a higher INLINEFORM0 Fatalities INLINEFORM1 , requiring the model to be more confident in its answer for that slot during training. Additionally, this provides a mechanism for driving down INLINEFORM2 when INLINEFORM3 is not strongly associated with INLINEFORM4 .

#### Relevance 496

Label: 

#### Passage 497

Retrieved by: BM25, Dense, Hybrid

> We evaluate configurations of our proposed architecture across three measures. The first is a modified version of standard precision, recall, and F INLINEFORM0 , as proposed by reschke2014. It deviates from the standard protocol by (1) awarding full recall for any slot when a single predicted value is contained in the gold slot, (2) only penalizing slots for which there are findable gold values in the text, and (3) limiting candidate values to the set of entities proposed by the Stanford NER system and included in the data set release. Eight of the fifteen slots are used in evaluation. Similarly, the second evaluation measure we present is standard precision, recall, and F INLINEFORM1 , specifically for null values.
> 
> We also evaluate the models using mean reciprocal rank (MRR). When calculating the F INLINEFORM0 -based evaluation measure we decode the model by taking the single highest-scoring value for each slot. However, this does not necessarily reflect the quality of the overall value ranking produced by the model. For this reason we include MRR, defined as: DISPLAYFORM0
> 
> where rank INLINEFORM0 is the rank position of the first correct value for a given cluster and slot pair INLINEFORM1 , and INLINEFORM2 , the number of such pairs, is INLINEFORM3 , the product of the total number of clusters with the total number of predicted slots.

#### Relevance 497

Label: 

#### Passage 499

Retrieved by: Dense, Hybrid

> We randomly selected 15 development set instances which our best model predicts incorrectly. Of these, we find three were incorrectly labeled in the gold data as errors from the distance supervision hypothesis (i.e., “zero chance” being labeled for 0 survivors, when the number of survivors was not mentioned in the cluster), and should not be predicted. Six were clearly expressed and should be predictable, with highly correlated keywords present in the context window, but were assigned low scores by the model. We belief a richer representation which combines the generalization of CNNs with the discrete signal of n-gram features BIBREF18 may solve some of these issues.
> 
> Four of the remaining errors appear to be due to aggregation errors. Specifically, the occurrence of a particular punctuation mark with far greater than average frequency resulted in it being predicted for three slots. While these could be filtered out, a more general solution may be to build a representation based on the actual mention (“Ryanair”), in addition to its context. This may reduce the scores of these mentions to such an extent that they are removed from consideration.
> 
> Table TABREF54 shows the accuracy of the model on each slot type. The model is struggles with predicting the Injuries and Survivors slots. The nature of news media leads these slots to be discussed less frequently, with their mentions often embedded more deeply in the document, or expressed textually. For instance, it is common to express INLINEFORM0 =Survivors, INLINEFORM1 as “no survivors”, but it is impossible to predict a 0 value in this case, under the current problem definition.

#### Relevance 499

Label: 

### BM25

#### Passage 494

Retrieved by: BM25

> A pointer network uses a softmax to normalize a vector the size of the input, to create an output distribution over the dictionary of inputs BIBREF23 . This assumes that the input vector is the size of the dictionary, and that each occurrence is scored independently of others. If an element appears repeatedly throughout the input, each occurrence is in competition not only with other elements, but also with its duplicates.
> 
> Here the scoring and aggregation steps of our proposed architecture can together be viewed as a pointer network where there is a redundancy in the input which respects an underlying grouping. Here the softmax normalizes the scores over the input vector, and the aggregation step again yields an output distribution over the dictionary of the input.

#### Relevance 494

Label: 

### Dense

#### Passage 498

Retrieved by: Dense

> For each mention INLINEFORM0 we construct a representation INLINEFORM1 of the mention in its context. This representation functions as a general “reading” or encoding of the mention, irrespective of the type of slots for which it will later be considered. This differs from some previous machine reading research where the model provides a query-specific reading of the document, or reads the document multiple times when answering a single query BIBREF0 . As in previous work, an embedding of a mention's context serves as its representation. We construct an embedding matrix INLINEFORM2 , using pre-trained word embeddings, where INLINEFORM3 is the dimensionality of the embeddings and INLINEFORM4 the number of words in the cluster. These are held fixed during training. All mentions are masked and receive the same one-hot vector in place of a pretrained embedding. From this matrix we embed the context using a two-layer convolutional neural network (CNN), with a detailed discussion of the architecture parameters provided in Section SECREF4 . CNNs have been used in a similar manner for a number of information extraction and classification tasks BIBREF6 , BIBREF7 and are capable of producing rich sentence representations BIBREF8 .
> 
> Having produced a representation INLINEFORM0 for each mention INLINEFORM1 , a slot-specific attention mechanism produces INLINEFORM2 , representing the compatibility of mention INLINEFORM3 with slot INLINEFORM4 . Let INLINEFORM5 be the representation matrix composed of all INLINEFORM6 , and INLINEFORM7 is the index of INLINEFORM8 into INLINEFORM9 . We create a separate embedding, INLINEFORM10 , for each slot INLINEFORM11 , and utilize it to attend over all mentions in the cluster as follows: DISPLAYFORM0
> 
> The mention-level scores reflect an interpretation of the value's encoding with respect to the slot. The softmax normalizes the scores over each slot, supplying the attention, and creating competition between mentions. This encourages the model to attend over mentions with the most characteristic contexts for each slot.

#### Relevance 498

Label: 

#### Passage 500

Retrieved by: Dense

> For values mentioned repeatedly throughout the news cluster, mention scores must be aggregated to produce a single value-level score. In this section we describe (1) how the right aggregation method can better reflect how the gold labels are applied to the data, (2) how domain knowledge can be incorporated into aggregation, and (3) how aggregation can be used as a dynamic approach to identifying missing information.
> 
> In the traditional view of distant supervision BIBREF9 , if a mention is found in an external knowledge base it is assumed that the mention is an expression of its role in the knowledge base, and it receives the corresponding label. This assumption does not always hold, and the resulting spurious labels are frequently cited as a source of training noise BIBREF10 , BIBREF11 . However, an aggregation over all mention scores provides a more accurate reflection of how distant supervision labels are applied to the data.
> 
> If one were to assign a label to each mention and construct a loss using the mention-level scores ( INLINEFORM0 ) directly, it would recreate the hard labeling of the traditional distant supervision training scenario. Instead, we relax the distant supervision assumption by using a loss on the value-level scores ( INLINEFORM1 ), with aggregation to pool beliefs from one to the other. This explicitly models the way in which cluster-wide labels are applied to mentions, and allows for spuriously labeled mentions to receive lower scores, “explaining away” the cluster's label by assigning a higher score to a mention with a more suitable representation.
> 
> Two natural choices for this aggregation are max and sum. Formally, under max aggregation the value-level scores for a value INLINEFORM0 and slot INLINEFORM1 are computed as: DISPLAYFORM0
> 
> And under sum aggregation: DISPLAYFORM0
> 
> If the most clearly expressed mentions correspond to correct values, max aggregation can be an effective strategy BIBREF10 . If the data set is noisy with numerous spurious mentions, a sum aggregation favoring values which are expressed both clearly and frequently may be the more appropriate choice.
> 
> The aforementioned aggregation methods combine mention-level scores uniformly, but for many domains one may have prior knowledge regarding which mentions should more heavily contribute to the aggregate score.

#### Relevance 500

Label: 

### Hybrid

None

## Question 0065

Paper: UG18 at SemEval-2018 Task 1: Generating Additional Training Data for Predicting Emotion Intensity in Spanish

> What subtasks did they participate in?

### Common Retrieved Chunks

#### Passage 501

Retrieved by: BM25, Dense, Hybrid

> Due to some large differences between our results on the dev and test set of this task, we performed a small error analysis in order to see what caused these differences. For EI-Reg-anger, the gold labels were compared to our own predictions, and we manually checked 50 instances for which our system made the largest errors.
> 
> Some examples that were indicative of the shortcomings of our system are shown in Table TABREF20 . First of all, our system did not take into account capitalization. The implications of this are shown in the first sentence, where capitalization intensifies the emotion used in the sentence. In the second sentence, the name Imperator Furiosa is not understood. Since our texts were lowercased, our system was unable to capture the named entity and thought the sentence was about an angry emperor instead. In the third sentence, our system fails to capture that when you are so angry that it makes you laugh, it results in a reduced intensity of the angriness. Finally, in the fourth sentence, it is the figurative language me infla la vena (it inflates my vein) that the system is not able to understand.
> 
> The first two error-categories might be solved by including smart features regarding capitalization and named entity recognition. However, the last two categories are problems of natural language understanding and will be very difficult to fix.

#### Relevance 501

Label: 

#### Passage 502

Retrieved by: BM25, Dense, Hybrid

> To conclude, the present study described our submission for the Semeval 2018 Shared Task on Affect in Tweets. We participated in four Spanish subtasks and our submissions ranked second, second, fourth and fifth place. Our study aimed to investigate whether the automatic generation of additional training data through translation and semi-supervised learning, as well as the creation of stepwise ensembles, increase the performance of our Spanish-language models. Strong support was found for the translation and semi-supervised learning approaches; our best models for all subtasks use either one of these approaches. These results suggest that both of these additional data resources are beneficial when determining emotion intensity (for Spanish). However, the creation of a stepwise ensemble from the best models did not result in better performance compared to simply averaging the models. In addition, some signs of overfitting on the dev set were found. In future work, we would like to apply the methods (translation and semi-supervised learning) used on Spanish on other low-resource languages and potentially also on other tasks.

#### Relevance 502

Label: 

#### Passage 503

Retrieved by: BM25, Hybrid

> Most lexical resources for sentiment analysis are in English. To still be able to benefit from these sources, the lexicons in the AffectiveTweets package were translated to Spanish, using the machine translation platform Apertium BIBREF5 .
> 
> All lexicons from the AffectiveTweets package were translated, except for SentiStrength. Instead of translating this lexicon, the English version was replaced by the Spanish variant made available by BIBREF6 .
> 
> For each subtask, the optimal combination of lexicons was determined. This was done by first calculating the benefits of adding each lexicon individually, after which only beneficial lexicons were added until the score did not increase anymore (e.g. after adding the best four lexicons the fifth one did not help anymore, so only four were added). The tests were performed using a default SVM model, with the set of word embeddings described in the previous section. Each subtask thus uses a different set of lexicons (see Table TABREF1 for an overview of the lexicons used in our final ensemble). For each subtask, this resulted in a (modest) increase on the development set, between 0.01 and 0.05.

#### Relevance 503

Label: 

#### Passage 506

Retrieved by: Dense, Hybrid

> To boost performance, the SVM, LSTM, and feed-forward models were combined into an ensemble. For both the LSTM and feed-forward approach, three different models were trained. The first model was trained on the training data (regular), the second model was trained on both the training and translated training data (translated) and the third one was trained on both the training data and the semi-supervised data (silver). Due to the nature of the SVM algorithm, semi-supervised learning does not help, so only the regular and translated model were trained in this case. This results in 8 different models per subtask. Note that for the valence tasks no silver training data was obtained, meaning that for those tasks the semi-supervised models could not be used.
> 
> Per task, the LSTM and feed-forward model's predictions were averaged over 10 prediction runs. Subsequently, the predictions of all individual models were combined into an average. Finally, models were removed from the ensemble in a stepwise manner if the removal increased the average score. This was done based on their original scores, i.e. starting out by trying to remove the worst individual model and working our way up to the best model. We only consider it an increase in score if the difference is larger than 0.002 (i.e. the difference between 0.716 and 0.718). If at some point the score does not increase and we are therefore unable to remove a model, the process is stopped and our best ensemble of models has been found. This process uses the scores on the development set of different combinations of models. Note that this means that the ensembles for different subtasks can contain different sets of models. The final model selections can be found in Table TABREF17 .

#### Relevance 506

Label: 

#### Passage 508

Retrieved by: Dense, Hybrid

> One of the aims of this study was to see if using semi-supervised learning is beneficial for emotion intensity tasks. For this purpose, the DISC BIBREF0 corpus was used. This corpus was created by querying certain emotion-related words, which makes it very suitable as a semi-supervised corpus. However, the specific emotion the tweet belonged to was not made public. Therefore, a method was applied to automatically assign the tweets to an emotion by comparing our scraped tweets to this new data set.
> 
> First, in an attempt to obtain the query-terms, we selected the 100 words which occurred most frequently in the DISC corpus, in comparison with their frequencies in our own scraped tweets corpus. Words that were clearly not indicators of emotion were removed. The rest was annotated per emotion or removed if it was unclear to which emotion the word belonged. This allowed us to create silver datasets per emotion, assigning tweets to an emotion if an annotated emotion-word occurred in the tweet.
> 
> Our semi-supervised approach is quite straightforward: first a model is trained on the training set and then this model is used to predict the labels of the silver data. This silver data is then simply added to our training set, after which the model is retrained. However, an extra step is applied to ensure that the silver data is of reasonable quality. Instead of training a single model initially, ten different models were trained which predict the labels of the silver instances. If the highest and lowest prediction do not differ more than a certain threshold the silver instance is maintained, otherwise it is discarded.
> 
> This results in two parameters that could be optimized: the threshold and the number of silver instances that would be added. This method can be applied to both the LSTM and feed-forward networks that were used. An overview of the characteristics of our data set with the final parameter settings is shown in Table TABREF14 . Usually, only a small subset of data was added to our training set, meaning that most of the silver data is not used in the experiments. Note that since only the emotions were annotated, this method is only applicable to

#### Relevance 508

Label: 

### BM25

#### Passage 504

Retrieved by: BM25

> Understanding the emotions expressed in a text or message is of high relevance nowadays. Companies are interested in this to get an understanding of the sentiment of their current customers regarding their products and the sentiment of their potential customers to attract new ones. Moreover, changes in a product or a company may also affect the sentiment of a customer. However, the intensity of an emotion is crucial in determining the urgency and importance of that sentiment. If someone is only slightly happy about a product, is a customer willing to buy it again? Conversely, if someone is very angry about customer service, his or her complaint might be given priority over somewhat milder complaints.
> 
> BIBREF0 present four tasks in which systems have to automatically determine the intensity of emotions (EI) or the intensity of the sentiment (Valence) of tweets in the languages English, Arabic, and Spanish. The goal is to either predict a continuous regression (reg) value or to do ordinal classification (oc) based on a number of predefined categories. The EI tasks have separate training sets for four different emotions: anger, fear, joy and sadness. Due to the large number of subtasks and the fact that this language does not have many resources readily available, we only focus on the Spanish subtasks. Our work makes the following contributions:
> 
> Our submissions ranked second (EI-Reg), second (EI-Oc), fourth (V-Reg) and fifth (V-Oc), demonstrating that the proposed method is accurate in automatically determining the intensity of emotions and sentiment of Spanish tweets. This paper will first focus on the datasets, the data generation procedure, and the techniques and tools used. Then we present the results in detail, after which we perform a small error analysis on the largest mistakes our model made. We conclude with some possible ideas for future work.

#### Relevance 504

Label: 

#### Passage 505

Retrieved by: BM25

> Table TABREF18 shows the results on the development set of all individuals models, distinguishing the three types of training: regular (r), translated (t) and semi-supervised (s). In Tables TABREF17 and TABREF18 , the letter behind each model (e.g. SVM-r, LSTM-r) corresponds to the type of training used. Comparing the regular and translated columns for the three algorithms, it shows that in 22 out of 30 cases, using translated instances as extra training data resulted in an improvement. For the semi-supervised learning approach, an improvement is found in 15 out of 16 cases. Moreover, our best individual model for each subtask (bolded scores in Table TABREF18 ) is always either a translated or semi-supervised model. Table TABREF18 also shows that, in general, our feed-forward network obtained the best results, having the highest F-score for 8 out of 10 subtasks.
> 
> However, Table TABREF19 shows that these scores can still be improved by averaging or ensembling the individual models. On the dev set, averaging our 8 individual models results in a better score for 8 out of 10 subtasks, while creating an ensemble beats all of the individual models as well as the average for each subtask. On the test set, however, only a small increase in score (if any) is found for stepwise ensembling, compared to averaging. Even though the results do not get worse, we cannot conclude that stepwise ensembling is a better method than simply averaging.
> 
> Our official scores (column Ens Test in Table TABREF19 ) have placed us second (EI-Reg, EI-Oc), fourth (V-Reg) and fifth (V-Oc) on the SemEval AIT-2018 leaderboard. However, it is evident that the results obtained on the test set are not always in line with those achieved on the development set. Especially on the anger subtask for both EI-Reg and EI-Oc, the scores are considerably lower on the test set in comparison with the results on the development set. Therefore, a small error analysis was performed on the instances where our final model made the largest errors.

#### Relevance 505

Label: 

### Dense

#### Passage 507

Retrieved by: Dense

> Usually, only a small subset of data was added to our training set, meaning that most of the silver data is not used in the experiments. Note that since only the emotions were annotated, this method is only applicable to the EI tasks.

#### Relevance 507

Label: 

### Hybrid

None

## Question 0066

Paper: CoVoST: A Diverse Multilingual Speech-To-Text Translation Corpus

> How was the dataset collected?

### Common Retrieved Chunks

#### Passage 509

Retrieved by: BM25, Dense, Hybrid

> Common Voice BIBREF10 is a crowdsourcing speech recognition corpus with an open CC0 license. Contributors record voice clips by reading from a bank of donated sentences. Each voice clip was validated by at least two other users. Most of the sentences are covered by multiple speakers, with potentially different genders, age groups or accents.
> 
> Raw CoVo data contains samples that passed validation as well as those that did not. To build CoVoST, we only use the former one and reuse the official train-development-test partition of the validated data. As of January 2020, the latest CoVo 2019-06-12 release includes 29 languages. CoVoST is currently built on that release and covers the following 11 languages: French, German, Dutch, Russian, Spanish, Italian, Turkish, Persian, Swedish, Mongolian and Chinese.
> 
> Validated transcripts were sent to professional translators. Note that the translators had access to the transcripts but not the corresponding voice clips since clips would not carry additional information. Since transcripts were duplicated due to multiple speakers, we deduplicated the transcripts before sending them to translators. As a result, different voice clips of the same content (transcript) will have identical translations in CoVoST for train, development and test splits.
> 
> In order to control the quality of the professional translations, we applied various sanity checks to the translations BIBREF11. 1) For German-English, French-English and Russian-English translations, we computed sentence-level BLEU BIBREF12 with the NLTK BIBREF13 implementation between the human translations and the automatic translations produced by a state-of-the-art system BIBREF14 (the French-English system was a Transformer big BIBREF15 separately trained on WMT14). We applied this method to these three language pairs only as we are confident about the quality of the corresponding systems. Translations with a score that was too low were manually inspected and sent back to the translators when needed. 2) We manually inspected examples where the source transcript was identical to the translation. 3) We measured the perplexity of the translations using a language model trained on a large amount of clean monolingual data BIBREF14. We manually inspected examples where the translation had a high perplexity and sent them back to translators accordingly. 4) We computed the ratio of English characters in the translations. We manually inspected examples

#### Relevance 509

Label: 

#### Passage 514

Retrieved by: Dense, Hybrid

> large amount of clean monolingual data BIBREF14. We manually inspected examples where the translation had a high perplexity and sent them back to translators accordingly. 4) We computed the ratio of English characters in the translations. We manually inspected examples with a low ratio and sent them back to translators accordingly. 5) Finally, we used VizSeq BIBREF16 to calculate similarity scores between transcripts and translations based on LASER cross-lingual sentence embeddings BIBREF17. Samples with low scores were manually inspected and sent back for translation when needed.
> 
> We also sanity check the overlaps of train, development and test sets in terms of transcripts and voice clips (via MD5 file hashing), and confirm they are totally disjoint.

#### Relevance 514

Label: 

#### Passage 515

Retrieved by: Dense, Hybrid

> Basic statistics for CoVoST and TT are listed in Table TABREF2 including (unique) sentence counts, speech durations, speaker demographics (partially available) as well as vocabulary and token statistics (based on Moses-tokenized sentences by sacreMoses) on both transcripts and translations. We see that CoVoST has over 327 hours of German speeches and over 171 hours of French speeches, which, to our knowledge, corresponds to the largest corpus among existing public ST corpora (the second largest is 110 hours BIBREF18 for German and 38 hours BIBREF19 for French). Moreover, CoVoST has a total of 18 hours of Dutch speeches, to our knowledge, contributing the first public Dutch ST resource. CoVoST also has around 27-hour Russian speeches, 37-hour Italian speeches and 67-hour Persian speeches, which is 1.8 times, 2.5 times and 13.3 times of the previous largest public one BIBREF7. Most of the sentences (transcripts) in CoVoST are covered by multiple speakers with potentially different accents, resulting in a rich diversity in the speeches. For example, there are over 1,000 speakers and over 10 accents in the French and German development / test sets. This enables good coverage of speech variations in both model training and evaluation.

#### Relevance 515

Label: 

#### Passage 516

Retrieved by: Dense, Hybrid

> We convert raw MP3 audio files from CoVo and TT into mono-channel waveforms, and downsample them to 16,000 Hz. For transcripts and translations, we normalize the punctuation, we tokenize the text with sacreMoses and lowercase it. For transcripts, we further remove all punctuation markers except for apostrophes. We use character vocabularies on all the tasks, with 100% coverage of all the characters. Preliminary experimentation showed that character vocabularies provided more stable training than BPE. For MT, the vocabulary is created jointly on both transcripts and translations. We extract 80-channel log-mel filterbank features, computed with a 25ms window size and 10ms window shift using torchaudio. The features are normalized to 0 mean and 1.0 standard deviation. We remove samples having more than 3,000 frames or more than 256 characters for GPU memory efficiency (less than 25 samples are removed for all languages).

#### Relevance 516

Label: 

### BM25

#### Passage 510

Retrieved by: BM25

> For simplicity, we use the same model architecture for ASR and ST, although we do not leverage ASR models to pretrain ST model encoders later. Table TABREF18 shows the word error rate (WER) and character error rate (CER) for ASR models. We see that French and German perform the best given they are the two highest resource languages in CoVoST. The other languages are relatively low resource (especially Turkish and Swedish) and the ASR models are having difficulties to learn from this data.

#### Relevance 510

Label: 

#### Passage 511

Retrieved by: BM25

> and Spanish, resulting in a total of 9.3 hours of speech. Both corpora are created at the sentence level and do not require additional alignments or segmentation. Using the official Common Voice train-development-test split, we also provide baseline models, including, to our knowledge, the first end-to-end many-to-one multilingual ST models. CoVoST is released under CC0 license and free to use. The Tatoeba evaluation samples are also available under friendly CC licenses. All the data can be acquired at https://github.com/facebookresearch/covost.

#### Relevance 511

Label: 

#### Passage 512

Retrieved by: BM25

> Tatoeba (TT) is a community built language learning corpus having sentences aligned across multiple languages with the corresponding speech partially available. Its sentences are on average shorter than those in CoVoST (see also Table TABREF2) given the original purpose of language learning. Sentences in TT are licensed under CC BY 2.0 FR and part of the speeches are available under various CC licenses.
> 
> We construct an evaluation set from TT (for French, German, Dutch, Russian and Spanish) as a complement to CoVoST development and test sets. We collect (speech, transcript, English translation) triplets for the 5 languages and do not include those whose speech has a broken URL or is not CC licensed. We further filter these samples by sentence lengths (minimum 4 words including punctuations) to reduce the portion of short sentences. This makes the resulting evaluation set closer to real-world scenarios and more challenging.
> 
> We run the same quality checks for TT as for CoVoST but we do not find poor quality translations according to our criteria. Finally, we report the overlap between CoVo transcripts and TT sentences in Table TABREF5. We found a minimal overlap, which makes the TT evaluation set a suitable additional test set when training on CoVoST.

#### Relevance 512

Label: 

#### Passage 513

Retrieved by: BM25

> End-to-end speech-to-text translation (ST) has attracted much attention recently BIBREF2, BIBREF3, BIBREF4, BIBREF5, BIBREF6 given its simplicity against cascading automatic speech recognition (ASR) and machine translation (MT) systems. The lack of labeled data, however, has become a major blocker for bridging the performance gaps between end-to-end models and cascading systems. Several corpora have been developed in recent years. post2013improved introduced a 38-hour Spanish-English ST corpus by augmenting the transcripts of the Fisher and Callhome corpora with English translations. di-gangi-etal-2019-must created the largest ST corpus to date from TED talks but the language pairs involved are out of English only. beilharz2019librivoxdeen created a 110-hour German-English ST corpus from LibriVox audiobooks. godard-etal-2018-low created a Moboshi-French ST corpus as part of a rare language documentation effort. woldeyohannis provided an Amharic-English ST corpus in the tourism domain. boito2019mass created a multilingual ST corpus involving 8 languages from a multilingual speech corpus based on Bible readings BIBREF7. Previous work either involves language pairs out of English, very specific domains, very low resource languages or a limited set of language pairs. This limits the scope of study, including the latest explorations on end-to-end multilingual ST BIBREF8, BIBREF9. Our work is mostly similar and concurrent to iranzosnchez2019europarlst who created a multilingual ST corpus from the European Parliament proceedings. The corpus we introduce has larger speech durations and more translation tokens. It is diversified with multiple speakers per transcript/translation. Finally, we provide additional out-of-domain test sets.
> 
> In this paper, we introduce CoVoST, a multilingual ST corpus based on Common Voice BIBREF10 for 11 languages into English, diversified with over 11,000 speakers and over 60 accents. It includes a total 708 hours of French (Fr), German (De), Dutch (Nl), Russian (Ru), Spanish (Es), Italian (It), Turkish (Tr), Persian (Fa), Swedish (Sv), Mongolian (Mn) and Chinese (Zh) speeches, with French and German ones having the largest durations among existing public corpora. We also collect an additional evaluation corpus from Tatoeba for French, German, Dutch, Russian and Spanish, resulting in a total of 9.3 hours of speech. Both corpora are created at the sentence level and do not require additional alignments or segmentation. Using the official Common Voice train-development-test split, we also provide baseline models, including,

#### Relevance 513

Label: 

### Dense

#### Passage 517

Retrieved by: Dense

> As we can see from Table TABREF2, CoVoST is diversified with a rich set of speakers and accents. We further inspect the speaker demographics in terms of sample distributions with respect to speaker counts, accent counts and age groups, which is shown in Figure FIGREF6, FIGREF7 and FIGREF8. We observe that for 8 of the 11 languages, at least 60% of the sentences (transcripts) are covered by multiple speakers. Over 80% of the French sentences have at least 3 speakers. And for German sentences, even over 90% of them have at least 5 speakers. Similarly, we see that a large portion of sentences are spoken in multiple accents for French, German, Dutch and Spanish. Speakers of each language also spread widely across different age groups (below 20, 20s, 30s, 40s, 50s, 60s and 70s).

#### Relevance 517

Label: 

### Hybrid

#### Passage 518

Retrieved by: Hybrid

> In CoVoST, large portion of transcripts are covered by multiple speakers with different genders, accents and age groups. Besides the standard corpus-level BLEU scores, we also want to evaluate model output variance on the same content (transcript) but different speakers. We hence propose to group samples (and their sentence BLEU scores) by transcript, and then calculate average per-group mean and average coefficient of variation defined as follows:
> 
> and
> 
> where $G$ is the set of sentence BLEU scores grouped by transcript and $G^{\prime } = \lbrace g | g\in G, |g|>1, \textrm {Mean}(g) > 0 \rbrace $.
> 
> $\textrm {BLEU}_{MS}$ provides a normalized quality score as oppose to corpus-level BLEU or unnormalized average of sentence BLEU. And $\textrm {CoefVar}_{MS}$ is a standardized measure of model stability against different speakers (the lower the better). Table TABREF24 shows the $\textrm {BLEU}_{MS}$ and $\textrm {CoefVar}_{MS}$ of our ST models on CoVoST test set. We see that German and Persian have the worst $\textrm {CoefVar}_{MS}$ (least stable) given their rich speaker diversity in the test set and relatively small train set (see also Figure FIGREF6 and Table TABREF2). Dutch also has poor $\textrm {CoefVar}_{MS}$ because of the lack of training data. Multilingual models are consistantly more stable on low-resource languages. Ru+Fr, Tr+Fr, Fa+Fr and Zh+Fr even have better $\textrm {CoefVar}_{MS}$ than all individual languages.

#### Relevance 518

Label: 

## Question 0067

Paper: Episodic Memory in Lifelong Language Learning

> Do they compare against other models?

### Common Retrieved Chunks

#### Passage 519

Retrieved by: BM25, Hybrid

> In this section, we evaluate our proposed model against several baselines on text classification and question answering tasks.

#### Relevance 519

Label: 

#### Passage 520

Retrieved by: BM25, Hybrid

> We compare the following models in our experiments:
> 
> Enc-Dec: a standard encoder-decoder model without any episodic memory module.
> 
> A-GEM BIBREF9 : Average Gradient Episodic Memory model that defines constraints on the gradients that are used to update model parameters based on retrieved examples from the memory. In its original formulation, A-GEM requires dataset identifiers and randomly samples examples from previous datasets. We generalize it to the setting without dataset identities by randomly sampling from the episodic memory module at fixed intervals, similar to our method.
> 
> Replay: a model that uses stored examples for sparse experience replay without local adaptation. We perform experience replay by sampling 100 examples from the memory and perform a gradient update after every 10,000 training steps, which gives us a 1% replay rate.
> 
> MbPA BIBREF7 : an episodic memory model that uses stored examples for local adaptation without sparse experience replay. The original MbPA formulation has a trainable key network. Our MbPA baseline uses a fixed key network since MbPA with a trainable key network performs significantly worse.
> 
> MbPA INLINEFORM0 : an episodic memory model with randomly retrieved examples for local adaptation (no key network).
> 
> MbPA++: our episodic memory model described in § SECREF2 .
> 
> MTL: a multitask model trained on all datasets jointly, used as a performance upper bound.

#### Relevance 520

Label: 

#### Passage 521

Retrieved by: BM25, Dense, Hybrid

> We consider a continual (lifelong) learning setup where a model needs to learn from a stream of training examples INLINEFORM0 . We assume that all our training examples in the series come from multiple datasets of the same task (e.g., a text classification task, a question answering task), and each dataset comes one after the other. Since all examples come from the same task, the same model can be used to make predictions on all examples. A crucial difference between our continual learning setup and previous work is that we do not assume that each example comes with a dataset descriptor (e.g., a dataset identity). As a result, the model does not know which dataset an example comes from and when a dataset boundary has been crossed during training. The goal of learning is to find parameters INLINEFORM1 that minimize the negative log probability of training examples under our model: INLINEFORM2
> 
> Our model consists of three main components: (i) an example encoder, (ii) a task decoder, and (iii) an episodic memory module. Figure FIGREF6 shows an illustration of our complete model. We describe each component in detail in the following.

#### Relevance 521

Label: 

#### Passage 523

Retrieved by: BM25, Dense, Hybrid

> our best model can be improved further by choosing relevant examples for sparse experience replay as well. We leave investigations of such methods to future work.
> 
> Comparing to the performance of the multitask model MTL—which is as an upper bound on achievable performance—we observe that there is still a gap between continual models and the multitask model. MbPA++ has the smallest performance gap. For text classification, MbPA++ outperforms single-dataset models in terms of averaged performance (70.6 vs. 60.7), demonstrating the success of positive transfer. For question answering, MbPA++ still lags behind single dataset models (62.0 vs. 66.0). Note that the collection of single-dataset models have many more parameters since there is a different set of model parameters per dataset. See Appendix SECREF8 for detailed results of multitask and single-dataset models.
> 
> Figure FIGREF34 shows INLINEFORM0 score and accuracy of various models on the test set corresponding to the first dataset seen during training as the models are trained on more datasets. The figure illustrates how well each model retains its previously acquired knowledge as it learns new knowledge. We can see that MbPA++ is consistently better compared to other methods.

#### Relevance 523

Label: 

#### Passage 525

Retrieved by: Dense, Hybrid

> The models are trained in one pass on concatenated training sets, and evaluated on the union of the test sets. To ensure robustness of models to training dataset orderings, we evaluate on four different orderings (chosen randomly) for each task. As the multitask model has no inherent dataset ordering, we report results on four different shufflings of combined training examples. We show the exact orderings in Appendix SECREF6 . We tune the local adaptation learning rate using the first dataset ordering for each task and only run the best setting on the other orderings.
> 
> A main difference between these two tasks is that in text classification the model acquires knowledge about new classes as training progresses (i.e., only a subset of the classes that corresponds to a particular dataset are seen at each training interval), whereas in question answering the span predictor works similarly across datasets.
> 
> Table TABREF33 provides a summary of our main results. We report (macro-averaged) accuracy for classification and INLINEFORM0 score for question answering. We provide complete per-dataset (non-averaged) results in Appendix SECREF7 . Our results show that A-GEM outperforms the standard encoder-decoder model Enc-Dec, although it is worse than MbPA on both tasks. Local adaptation (MbPA) and sparse experience replay (Replay) help mitigate catastrophic forgetting compared to Enc-Dec, but a combination of them is needed to achieve the best performance (MbPA++).
> 
> Our experiments also show that retrieving relevant examples from memory is crucial to ensure that the local adaptation phase is useful. Comparing the results from MbPA++ and MbPA INLINEFORM0 , we can see that the model that chooses neighbors randomly is significantly worse than the model that finds and uses similar examples for local adaptation. We emphasize that having a fixed key network is crucial to prevent representation drift. The original MbPA formulation that updates the key network during training results in a model that only performs slightly better than MbPA INLINEFORM1 in our preliminary experiments. Our results suggest that our best model can be improved further by choosing relevant examples for sparse experience replay as well. We leave investigations of such methods to future work.
> 
> Comparing to the performance of the multitask model MTL—which is as an upper bound

#### Relevance 525

Label: 

### BM25

#### Passage 522

Retrieved by: BM25

> The ability to continuously learn and accumulate knowledge throughout a lifetime and reuse it effectively to adapt to a new problem quickly is a hallmark of general intelligence. State-of-the-art machine learning models work well on a single dataset given enough training examples, but they often fail to isolate and reuse previously acquired knowledge when the data distribution shifts (e.g., when presented with a new dataset)—a phenomenon known as catastrophic forgetting BIBREF0 , BIBREF1 .
> 
> The three main approaches to address catastrophic forgetting are based on: (i) augmenting the loss function that is being minimized during training with extra terms (e.g., a regularization term, an optimization constraint) to prevent model parameters learned on a new dataset from significantly deviating from parameters learned on previously seen datasets BIBREF2 , BIBREF3 , BIBREF4 , (ii) adding extra learning phases such as a knowledge distillation phase, an experience replay BIBREF5 , BIBREF6 , and (iii) augmenting the model with an episodic memory module BIBREF7 . Recent methods have shown that these approaches can be combined—e.g., by defining optimization constraints using samples from the episodic memory BIBREF8 , BIBREF9 .
> 
> In language learning, progress in unsupervised pretraining BIBREF10 , BIBREF11 , BIBREF12 has driven advances in many language understanding tasks BIBREF13 , BIBREF14 . However, these models have been shown to require a lot of in-domain training examples, rapidly overfit to particular datasets, and are prone to catastrophic forgetting BIBREF15 , making them unsuitable as a model of general linguistic intelligence.
> 
> In this paper, we investigate the role of episodic memory for learning a model of language in a lifelong setup. We propose to use such a component for sparse experience replay and local adaptation to allow the model to continually learn from examples drawn from different data distributions. In experience replay, we randomly select examples from memory to retrain on. Our model only performs experience replay very sparsely to consolidate newly acquired knowledge with existing knowledge in the memory into the model. We show that a 1% experience replay to learning new examples ratio is sufficient. Such a process bears some similarity to memory consolidation in human learning BIBREF16 . In local adaptation, we follow Memory-based Parameter Adaptation BIBREF7

#### Relevance 522

Label: 

### Dense

#### Passage 524

Retrieved by: Dense

> We use publicly available text classification datasets from BIBREF22 to evaluate our models (http://goo.gl/JyCnZq). This collection of datasets includes text classification datasets from diverse domains such as news classification (AGNews), sentiment analysis (Yelp, Amazon), Wikipedia article classification (DBPedia), and questions and answers categorization (Yahoo). Specifically, we use AGNews (4 classes), Yelp (5 classes), DBPedia (14 classes), Amazon (5 classes), and Yahoo (10 classes) datasets. Since classes for Yelp and Amazon datasets have similar semantics (product ratings), we merge the classes for these two datasets. In total, we have 33 classes in our experiments. These datasets have varying sizes. For example, AGNews is ten times smaller than Yahoo. We create a balanced version all datasets used in our experiments by randomly sampling 115,000 training examples and 7,600 test examples from all datasets (i.e., the size of the smallest training and test sets). We leave investigations of lifelong learning in unbalanced datasets to future work. In total, we have 575,000 training examples and 38,000 test examples.
> 
> We use three question answering datasets: SQuAD 1.1 BIBREF23 , TriviaQA BIBREF24 , and QuAC BIBREF25 . These datasets have different characteristics. SQuAD is a reading comprehension dataset constructed from Wikipedia articles. It includes almost 90,000 training examples and 10,000 validation examples. TriviaQA is a dataset with question-answer pairs written by trivia enthusiasts and evidence collected retrospectively from Wikipedia and the Web. There are two sections of TriviaQA, Web and Wikipedia, which we treat as separate datasets. The Web section contains 76,000 training examples and 10,000 (unverified) validation examples, whereas the Wikipedia section has about 60,000 training examples and 8,000 validation examples. QuAC is an information-seeking dialog-style dataset where a student asks questions about a Wikipedia article and a teacher answers with a short excerpt from the article. It has 80,000 training examples and approximately 7,000 validation examples.

#### Relevance 524

Label: 

#### Passage 526

Retrieved by: Dense

> We show results of a single dataset model that is only trained on a particular dataset in Table TABREF56 .

#### Relevance 526

Label: 

### Hybrid

None

## Question 0068

Paper: Aggressive, Repetitive, Intentional, Visible, and Imbalanced: Refining Representations for Cyberbullying Classification

> What agreement measure is used?

### Common Retrieved Chunks

#### Passage 527

Retrieved by: BM25, Dense, Hybrid

> Timeline similarity is used to indicate common interests and shared topics of conversation between the author and target timelines. High similarity scores might reflect users' familiarity with one another, or suggest that they occupy similar social positions. This can be used to distinguish cyberbullying from harmless banter between friends and associates. To compute this metric, we represent the author and target timelines as TF-IDF vectors $\vec{A}$ and $\vec{T}$. We then take the cosine similarity between the vectors as
> 
> A cosine similarity of 1 means that users' timelines had identical counts across all weighted terms; a cosine similarity of 0 means that their timelines did not contain any words in common. We expect higher similarity scores between friends and associates.
> 
> In Figure FIGREF44 (a), we see that the timelines were significantly less similar when the target was in a position of greater power ($D=0.294$). This is not surprising, since power can be derived from such differences between social groups. We do not observe the same dissimilarity when the author was more powerful ($p=0.58$). What we do observe is likely caused by noise from extreme class imbalance and low inter-annotator agreement on labels for author power.
> 
> Turning to Figure FIGREF44 (b), we see that aggressive messages were less likely to harbor harmful intent if they were sent between users with similar timelines ($D=0.285$). Aggressive banter between friends is generally harmless, so again, this confirms our intuitions.

#### Relevance 527

Label: 

#### Passage 530

Retrieved by: BM25, Hybrid

> Network features have been shown to improve text-based models BIBREF6, BIBREF25, and they can help classifiers distinguish between bullies and victims BIBREF32. These features may also capture some of the more social aspects of cyberbullying, such as power imbalance and visibility among peers. However, many centrality measures and clustering algorithms require detailed network representations. These features may not be scalable for real-world applications. We propose a set of low-complexity measurements that can be used to encode important higher-order relations at scale. Specifically, we measure the relative positions of the author and target accounts in the directed following network by computing modified versions of Jaccard's similarity index as we now explain.

#### Relevance 530

Label: 

#### Passage 531

Retrieved by: BM25, Dense, Hybrid

> To construct realistic and competitive baseline models, we consider a set of standard text-based features that have been used widely throughout the literature. Specifically, we use the NLTK library BIBREF36 to construct unigrams, bigrams, and trigrams for each labeled message. This parallels the work of BIBREF8, BIBREF7, and BIBREF26. Following BIBREF30, we incorporate counts from the Linguistic Inquiry and Word Count (LIWC) dictionary to measure the linguistic and psychological processes that are represented in the text BIBREF37. We also use a modified version of the Flesch-Kincaid Grade Level and Flesch Reading Ease scores as computed in BIBREF35. Lastly, we encode the sentiment scores for each message using the Valence Aware Dictionary and sEntiment Reasoner (VADER) of BIBREF38.

#### Relevance 531

Label: 

#### Passage 532

Retrieved by: Dense, Hybrid

> To more clearly represent the social relationship between the author and target users, we consider the messages sent between them as follows:
> 
> Downward mention count: How many messages has the author sent to the target?
> 
> Upward mention count: How many messages has the target sent to the author?
> 
> Mention overlap: Let $M_a$ be the set of all accounts mentioned by author $a$, and let $M_t$ be the set of all accounts mentioned by target $t$. We compute the ratio $\frac{|M_a \cap M_t|}{|M_a \cup M_t|}$.
> 
> Multiset mention overlap: Let $\hat{M}_a$ be the multiset of all accounts mentioned by author $a$ (with repeats for each mention), and let $\hat{M}_t$ be the multiset of all accounts mentioned by target $t$. We measure $\frac{|\hat{M}_a \cap ^{*} \hat{M}_t|}{|\hat{M}_a \cup \hat{M}_t|}$ where $\cap ^{*}$ takes the multiplicity of each element to be the sum of the multiplicity from $\hat{M}_a $ and the multiplicity from $\hat{M}_b$
> 
> The direct mention count measures the history of repeated communication between the author and the target. For harmful messages, downward overlap is higher ($D=0.178$) and upward overlap is lower ($D=0.374$) than for harmless messages, as shown in Figure FIGREF38. This means malicious authors tend to address the target repeatedly while the target responds with relatively few messages.
> 
> Mention overlap is a measure of social similarity that is based on shared conversations between the author and the target. Multiset mention overlap measures the frequency of communication within this shared space. These features may help predict visibility among peers, or repeated aggression due to pile-on bullying situations. We see in Figure FIGREF38 that repeated aggression is linked to slightly greater mention overlap ($D=0.07$, $p=0.07$), but the trend is significant only for multiset mention overlap ($D=0.08$, $p=0.03$).

#### Relevance 532

Label: 

#### Passage 533

Retrieved by: Dense, Hybrid

> review these examples, we gave them a short 7-question quiz to test their knowledge. Workers were given only one quiz attempt, and they were expected to score at least 6 out of 7 questions correctly before they could proceed to the paid HIT. Workers were then paid $\$0.12$ for each thread that they annotated.
> 
> We successfully recruited 170 workers to label all 6,897 available threads in our dataset. They labeled an average of 121.7 threads and a median of 7 threads each. They spent an average time of 3 minutes 50 seconds, and a median time of 61 seconds per thread. For each thread, we collected annotations from three different workers, and from this data we computed our reliability metrics using Fleiss's Kappa for inter-annotator agreement as shown in Table TABREF17.
> 
> We determined ground truth for our data using a 2 out of 3 majority vote as in BIBREF12. If the message thread was missing or a target user could not be identified, we removed the entry from the dataset, since later we would need to draw our features from both the thread and the target profile. After filtering in this way, we were left with 5,537 labeled tweets.

#### Relevance 533

Label: 

### BM25

#### Passage 528

Retrieved by: BM25

> This material is based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Agreement No. HR0011890019, and by the National Science Foundation (NSF) under Grant No. 1659886 and Grant No. 1553579.

#### Relevance 528

Label: 

#### Passage 529

Retrieved by: BM25

> Our study focuses on the Twitter ecosystem and a small part of its network. The initial sampling of tweets was based on a machine learning classifier of aggressive English language. This classifier has an F1 score of 0.90 BIBREF35. Even with this filter, only 0.7% of tweets were deemed by a majority of MTurk workers as cyberbullying (Table TABREF17). This extreme class imbalance can disadvantage a wide range of machine learning models. Moreover, the MTurk workers exhibited only moderate inter-annotator agreement (Table TABREF17). We also acknowledge that notions of harmful intent and power imbalance can be subjective, since they may depend on the particular conventions or social structure of a given community. For these reasons, we recognize that cyberbullying still has not been unambiguously defined. Moreover, their underlying constructs are difficult to identify. In this study, we did not train workers to recognize subtle cues for interpersonal popularity, nor the role of anonymity in creating a power imbalance.
> 
> Furthermore, because we lack the authority to define cyberbullying, we cannot assert a two-way implication between cyberbullying and the five criteria outlined here. It may be possible for cyberbullying to exist with only one criterion present, such as harmful intent. Our five criteria also might not span all of the dimensions of cyberbullying. However, they are representative of the literature in both the social science and machine learning communities, and they can be used in weighted combinations to accommodate new definitions.
> 
> The main contribution of our paper is not that we solved the problem of cyberbullying detection. Instead, we have exposed the challenge of defining and measuring cyberbullying activity, which has been historically overlooked in the research community.

#### Relevance 529

Label: 

### Dense

#### Passage 534

Retrieved by: Dense

> To detect repeated aggression, we again employ the hate speech and offensive language classifier of BIBREF35. Each message is given a binary label according to the classifier-assigned class: aggressive (classified as hate speech or offensive language) or non-aggressive (classified as neither hate speech nor offensive language). From these labels, we derive the following features.
> 
> Aggressive message count: Count the messages in the thread classified as aggressive
> 
> Aggressive author message count: Count the author's messages that were classified as aggressive
> 
> Aggressive user count: Of the users who posted a reply in the thread after the author first commented, count how many had a message classified as aggressive

#### Relevance 534

Label: 

### Hybrid

None

## Question 0069

Paper: Bringing Structure into Summaries: Crowdsourcing a Benchmark Corpus of Concept Maps

> How were crowd workers instructed to identify important elements in large document collections?

### Common Retrieved Chunks

#### Passage 535

Retrieved by: BM25, Hybrid

> Multi-document summarization (MDS), the transformation of a set of documents into a short text containing their most important aspects, is a long-studied problem in NLP. Generated summaries have been shown to support humans dealing with large document collections in information seeking tasks BIBREF0 , BIBREF1 , BIBREF2 . However, when exploring a set of documents manually, humans rarely write a fully-formulated summary for themselves. Instead, user studies BIBREF3 , BIBREF4 show that they note down important keywords and phrases, try to identify relationships between them and organize them accordingly. Therefore, we believe that the study of summarization with similarly structured outputs is an important extension of the traditional task.
> 
> A representation that is more in line with observed user behavior is a concept map BIBREF5 , a labeled graph showing concepts as nodes and relationships between them as edges (Figure FIGREF2 ). Introduced in 1972 as a teaching tool BIBREF6 , concept maps have found many applications in education BIBREF7 , BIBREF8 , for writing assistance BIBREF9 or to structure information repositories BIBREF10 , BIBREF11 . For summarization, concept maps make it possible to represent a summary concisely and clearly reveal relationships. Moreover, we see a second interesting use case that goes beyond the capabilities of textual summaries: When concepts and relations are linked to corresponding locations in the documents they have been extracted from, the graph can be used to navigate in a document collection, similar to a table of contents. An implementation of this idea has been recently described by BIBREF12 .
> 
> The corresponding task that we propose is concept-map-based MDS, the summarization of a document cluster in the form of a concept map. In order to develop and evaluate methods for the task, gold-standard corpora are necessary, but no suitable corpus is available. The manual creation of such a dataset is very time-consuming, as the annotation includes many subtasks. In particular, an annotator would need to manually identify all concepts in the documents, while only a few of them will eventually end up in the summary.
> 
> To overcome these issues, we present a corpus creation method that effectively combines automatic preprocessing, scalable crowdsourcing and high-quality expert annotations. Using it, we can avoid

#### Relevance 535

Label: 

#### Passage 536

Retrieved by: BM25, Dense, Hybrid

> We break down the task of importance annotation to the level of single propositions. The goal of our crowdsourcing scheme is to obtain a score for each proposition indicating its importance in a document cluster, such that a ranking according to the score would reveal what is most important and should be included in a summary. In contrast to other work, we do not show the documents to the workers at all, but provide only a description of the document cluster's topic along with the propositions. This ensures that tasks are small, simple and can be done quickly (see Figure FIGREF4 ).
> 
> In preliminary tests, we found that this design, despite the minimal context, works reasonably on our focused clusters on common educational topics. For instance, consider Figure FIGREF4 : One can easily say that P1 is more important than P2 without reading the documents.
> 
> We distinguish two task variants:
> 
> Instead of enforcing binary importance decisions, we use a 5-point Likert-scale to allow more fine-grained annotations. The obtained labels are translated into scores (5..1) and the average of all scores for a proposition is used as an estimate for its importance. This follows the idea that while single workers might find the task subjective, the consensus of multiple workers, represented in the average score, tends to be less subjective due to the “wisdom of the crowd”. We randomly group five propositions into a task.
> 
> As an alternative, we use a second task design based on pairwise comparisons. Comparisons are known to be easier to make and more consistent BIBREF32 , but also more expensive, as the number of pairs grows quadratically with the number of objects. To reduce the cost, we group five propositions into a task and ask workers to order them by importance per drag-and-drop. From the results, we derive pairwise comparisons and use TrueSkill BIBREF35 , a powerful Bayesian rank induction model BIBREF34 , to obtain importance estimates for each proposition.

#### Relevance 536

Label: 

#### Passage 537

Retrieved by: BM25, Hybrid

> Likert-scale tasks and 0.69 (Spearman 0.66) for comparison tasks. This shows that the approach, despite the subjectiveness of the task, allows us to collect reliable annotations.
> 
> In addition to the reliability studies, we extrinsically evaluated the annotations in the task of summary evaluation. For each of the 58 peer summaries in TAC2008, we calculated a score as the sum of the importance estimates of the propositions it contains. Table TABREF13 shows how these peer scores, averaged over the three topics, correlate with the manual responsiveness scores assigned during TAC in comparison to ROUGE-2 and Pyramid scores. The results demonstrate that with both task designs, we obtain importance annotations that are similarly useful for summary evaluation as pyramid annotations or gold-standard summaries (used for ROUGE).
> 
> Based on the pilot study, we conclude that the proposed crowdsourcing scheme allows us to obtain proper importance annotations for propositions. As workers are not required to read all documents, the annotation is much more efficient and scalable as with traditional methods.

#### Relevance 537

Label: 

#### Passage 540

Retrieved by: Dense, Hybrid

> documents, while only a few of them will eventually end up in the summary.
> 
> To overcome these issues, we present a corpus creation method that effectively combines automatic preprocessing, scalable crowdsourcing and high-quality expert annotations. Using it, we can avoid the high effort for single annotators, allowing us to scale to document clusters that are 15 times larger than in traditional summarization corpora. We created a new corpus of 30 topics, each with around 40 source documents on educational topics and a summarizing concept map that is the consensus of many crowdworkers (see Figure FIGREF3 ).
> 
> As a crucial step of the corpus creation, we developed a new crowdsourcing scheme called low-context importance annotation. In contrast to traditional approaches, it allows us to determine important elements in a document cluster without requiring annotators to read all documents, making it feasible to crowdsource the task and overcome quality issues observed in previous work BIBREF13 . We show that the approach creates reliable data for our focused summarization scenario and, when tested on traditional summarization corpora, creates annotations that are similar to those obtained by earlier efforts.
> 
> To summarize, we make the following contributions: (1) We propose a novel task, concept-map-based MDS (§ SECREF2 ), (2) present a new crowdsourcing scheme to create reference summaries (§ SECREF4 ), (3) publish a new dataset for the proposed task (§ SECREF5 ) and (4) provide an evaluation protocol and baseline (§ SECREF7 ). We make these resources publicly available under a permissive license.

#### Relevance 540

Label: 

#### Passage 541

Retrieved by: Dense, Hybrid

> Lloret.2013 describe several experiments to crowdsource reference summaries. Workers are asked to read 10 documents and then select 10 summary sentences from them for a reward of $0.05. They discovered several challenges, including poor work quality and the subjectiveness of the annotation task, indicating that crowdsourcing is not useful for this purpose.
> 
> To overcome these issues, we introduce a new task design, low-context importance annotation, to determine summary-worthy parts of documents. Compared to Lloret et al.'s approach, it is more in line with crowdsourcing best practices, as the tasks are simple, intuitive and small BIBREF30 and workers receive reasonable payment BIBREF31 . Most importantly, it is also much more efficient and scalable, as it does not require workers to read all documents in a cluster.

#### Relevance 541

Label: 

### BM25

#### Passage 538

Retrieved by: BM25

> In this final step, we connect the set of important propositions to form a graph. For instance, given the following two propositions
> 
> (student, may borrow, Stafford Loan)
> 
> (the student, does not have, a credit history)
> 
> one can easily see, although the first arguments differ slightly, that both labels describe the concept student, allowing us to build a concept map with the concepts student, Stafford Loan and credit history. The annotation task thus involves deciding which of the available propositions to include in the map, which of their concepts to merge and, when merging, which of the available labels to use. As these decisions highly depend upon each other and require context, we decided to use expert annotators rather than crowdsource the subtasks.
> 
> Annotators were given the topic description and the most important, ranked propositions. Using a simple annotation tool providing a visualization of the graph, they could connect the propositions step by step. They were instructed to reach a size of 25 concepts, the recommended maximum size for a concept map BIBREF6 . Further, they should prefer more important propositions and ensure connectedness. When connecting two propositions, they were asked to keep the concept label that was appropriate for both propositions. To support the annotators, the tool used ADW BIBREF40 , a state-of-the-art approach for semantic similarity, to suggest possible connections. The annotation was carried out by graduate students with a background in NLP after receiving an introduction into the guidelines and tool and annotating a first example.
> 
> If an annotator was not able to connect 25 concepts, she was allowed to create up to three synthetic relations with freely defined labels, making the maps slightly abstractive. On average, the constructed maps have 0.77 synthetic relations, mostly connecting concepts whose relation is too obvious to be explicitly stated in text (e.g. between Montessori teacher and Montessori education).
> 
> To assess the reliability of this annotation step, we had the first three maps created by two annotators. We casted the task of selecting propositions to be included in the map as a binary decision task and observed an agreement of 84% ( INLINEFORM0 ). Second, we modeled the decision which concepts to join as a binary decision

#### Relevance 538

Label: 

#### Passage 539

Retrieved by: BM25

> To verify the proposed approach, we conducted a pilot study on Amazon Mechanical Turk using data from TAC2008 BIBREF36 . We collected importance estimates for 474 propositions extracted from the first three clusters using both task designs. Each Likert-scale task was assigned to 5 different workers and awarded $0.06. For comparison tasks, we also collected 5 labels each, paid $0.05 and sampled around 7% of all possible pairs. We submitted them in batches of 100 pairs and selected pairs for subsequent batches based on the confidence of the TrueSkill model.
> 
> Following the observations of Lloret.2013, we established several measures for quality control. First, we restricted our tasks to workers from the US with an approval rate of at least 95%. Second, we identified low quality workers by measuring the correlation of each worker's Likert-scores with the average of the other four scores. The worst workers (at most 5% of all labels) were removed.
> 
> In addition, we included trap sentences, similar as in BIBREF13 , in around 80 of the tasks. In contrast to Lloret et al.'s findings, both an obvious trap sentence (This sentence is not important) and a less obvious but unimportant one (Barack Obama graduated from Harvard Law) were consistently labeled as unimportant (1.08 and 1.14), indicating that the workers did the task properly.
> 
> For Likert-scale tasks, we follow Snow.2008 and calculate agreement as the average Pearson correlation of a worker's Likert-score with the average score of the remaining workers. This measure is less strict than exact label agreement and can account for close labels and high- or low-scoring workers. We observe a correlation of 0.81, indicating substantial agreement. For comparisons, the majority agreement is 0.73. To further examine the reliability of the collected data, we followed the approach of Kiritchenko.2016 and simply repeated the crowdsourcing for one of the three topics. Between the importance estimates calculated from the first and second run, we found a Pearson correlation of 0.82 (Spearman 0.78) for Likert-scale tasks and 0.69 (Spearman 0.66) for comparison tasks. This shows that the approach, despite the subjectiveness of the task, allows us to collect reliable annotations.
> 
> In addition to the reliability studies, we extrinsically evaluated the annotations in the task

#### Relevance 539

Label: 

### Dense

#### Passage 542

Retrieved by: Dense

> This section presents the corpus construction process, as outlined in Figure FIGREF16 , combining automatic preprocessing, scalable crowdsourcing and high-quality expert annotations to be able to scale to the size of our document clusters. For every topic, we spent about $150 on crowdsourcing and 1.5h of expert annotations, while just a single annotator would already need over 8 hours (at 200 words per minute) to read all documents of a topic.

#### Relevance 542

Label: 

#### Passage 543

Retrieved by: Dense

> Given the propositions identified in the previous step, we now applied our crowdsourcing scheme as described in § SECREF4 to determine their importance. To cope with the large number of propositions, we combine the two task designs: First, we collect Likert-scores from 5 workers for each proposition, clean the data and calculate average scores. Then, using only the top 100 propositions according to these scores, we crowdsource 10% of all possible pairwise comparisons among them. Using TrueSkill, we obtain a fine-grained ranking of the 100 most important propositions.
> 
> For Likert-scores, the average agreement over all topics is 0.80, while the majority agreement for comparisons is 0.78. We repeated the data collection for three randomly selected topics and found the Pearson correlation between both runs to be 0.73 (Spearman 0.73) for Likert-scores and 0.72 (Spearman 0.71) for comparisons. These figures show that the crowdsourcing approach works on this dataset as reliably as on the TAC documents.
> 
> In total, we uploaded 53k scoring and 12k comparison tasks to Mechanical Turk, spending $4425.45 including fees. From the fine-grained ranking of the 100 most important propositions, we select the top 50 per topic to construct a summary concept map in the subsequent steps.

#### Relevance 543

Label: 

### Hybrid

None

## Question 0070

Paper: A Large-Scale Test Set for the Evaluation of Context-Aware Pronoun Translation in Neural Machine Translation

> what are the baselines?

### Common Retrieved Chunks

#### Passage 544

Retrieved by: BM25, Dense, Hybrid

> We consider the following recurrent baselines:
> 
> baseline Our baseline model is a standard bidirectional RNN model with attention, trained with Nematus. It operates on the sentence level and does not see any additional context. The input and output embeddings of the decoder are tied, encoder embeddings are not.
> 
> concat22 We concatenate each sentence with one preceding sentence, for both the source and target side of the corpus. Then we train on this new data set without any changes to the model architecture. This very simple method is inspired by BIBREF5 .
> 
> The following models are taken, or slightly adapted, from BIBREF9 . For this reason, we give only a very short description of them here and the reader is referred to their work for details.
> 
> s-hier A multi-encoder architecture with hierarchical attention. This model has access to one additional context: the previous source sentence. It is read by a separate encoder, and attended to by an additional attention network. The output of the resulting two attention vectors is combined with yet another attention network.
> 
> s-t-hier Identical to s-hier, except that it considers two additional contexts: the previous source sentence and previous target sentence. Both are read by separate encoders, and sequences from all encoders are combined with hierarchical attention.
> 
> s-hier-to-2 The model has an additional encoder for source context, whereas the target side of the corpus is concatenated, in the same way as for concat22. This model achieved the best results in BIBREF9 .
> 
> For each variant, we also introduce and test weight tying: we share the parameters of embedding matrices between encoders that read the same kind of text (source or target side).

#### Relevance 544

Label: 

#### Passage 545

Retrieved by: BM25, Hybrid

> Contrastive evaluation is different from conventional evaluation of machine translation in that it does not require any translation. Rather than testing a model's ability to translate, it is a method to test a model's ability to discriminate between given good and bad translations.
> 
> We exploit the fact that NMT systems are in fact language models of the target language, conditioned on source text. Like language models, NMT systems can be used to compute a model score (the negative log probability) for an existing translation. Contrastive evaluation, then, means to compare the model score of two pairs of inputs: INLINEFORM0 and INLINEFORM1 . If the model score of the actual reference translation is higher, we assume that this model can detect wrong pronoun translations.
> 
> However, this does not mean that systems actually produce the reference translation when given the source sentence for translation. An entirely different target sequence might rank higher in the system's beam during decoding. The only conclusion permitted by contrastive evaluation is whether or not the reference translation is more probable than a contrastive variant.
> 
> If the model score of the reference is indeed higher, we refer to this outcome as a “correct decision” by the model. The model's decision is only correct if the reference translation has a higher score than any contrastive translation. In our evaluation, we aggregate model decisions on the whole test set and report the overall percentage of correct decisions as accuracy.
> 
> During scoring, the model is provided with reference translations as target context, while during translation, the model needs to predict the full sequence. It is an open question to what extent performance deteriorates when context is itself predicted, and thus noisy. We highlight that the same problem arises for sentence-level NMT, and has been addressed with alternative training strategies BIBREF27 .

#### Relevance 545

Label: 

#### Passage 546

Retrieved by: BM25, Hybrid

> Even though machine translation has improved considerably with the advent of neural machine translation (NMT) BIBREF0 , BIBREF1 , the translation of pronouns remains a major issue. They are notoriously hard to translate since they often require context outside the current sentence.
> 
> As an example, consider the sentences in Figure FIGREF1 . In both languages, there is a pronoun in the second sentence that refers to the European Central Bank. When the second sentence is translated from English to German, the translation of the pronoun it is ambiguous. This ambiguity can only be resolved with context awareness: if a translation system has access to the previous English sentence, the previous German translation, or both, it can determine the antecedent the pronoun refers to. In this German sentence, the antecedent Europäische Zentralbank dictates the feminine gender of the pronoun sie.
> 
> It is unfortunate, then, that current NMT systems generally operate on the sentence level BIBREF2 , BIBREF3 , BIBREF4 . Documents are translated sentence-by-sentence for practical reasons, such as line-based processing in a pipeline and reduced computational complexity. Furthermore, improvements of larger-context models over baselines in terms of document-level metrics such as BLEU or RIBES have been moderate, so that their computational overhead does not seem justified, and so that it is hard to develop more effective context-aware architectures and empirically validate them.
> 
> To address this issue, we present an alternative way of evaluating larger-context models on a test set that allows to specifically measure a model's capability to correctly translate pronouns. The test suite consists of pairs of source and target sentences, in combination with contrastive translation variants (for evaluation by model scoring) and additional linguistic and contextual information (for further analysis). The resource is freely available. Additionally, we evaluate several context-aware models that have recently been proposed in the literature on this test set, and extend existing models with parameter tying.
> 
> The main contributions of our paper are:
> 
> Section SECREF2 explains how our paper relates to existing work on context-aware models and the evaluation of pronoun translation. Section SECREF3 describes our test suite. The context-aware models we use in our experiments are detailed in Section SECREF4 . We discuss our experiments in Section SECREF5

#### Relevance 546

Label: 

#### Passage 548

Retrieved by: BM25, Dense, Hybrid

> pairs and antecedent distance in the test set.
> 
> For each sentence pair in the resulting test set, we introduce contrastive translations. A contrastive translation is a translation variant where the correct pronoun is swapped with an incorrect one. For an example, see Table TABREF19 , where the pronoun it in the original translation corresponds to sie because the antecedent bat is a feminine noun in German (Fledermaus). We produce wrong translations by replacing sie with one of the other pronouns (er, es).
> 
> Note that, by themselves, these contrastive translations are grammatically correct if the antecedent is outside the current sentence. The test set also contains pronouns with an antecedent in the same sentence (antecedent distance 0). Those examples do not require any additional context for disambiguation and we therefore expect the sentence-level baseline to perform well on them.
> 
> We take extra care to ensure that the resulting contrastive translations are grammatically correct, because ungrammatical sentences are easily dismissed by an NMT system. For instance, if there are any possessive pronouns (such as seine) in the sentence, we also change their gender to match the personal pronoun replacement.
> 
> The German coreference resolution system does not resolve es because most instances of es in German are either non-referential forms, or they refer to a clause instead of a nominal antecedent. We limit the test set to nominal antecedents, as these are the only ambiguous cases with respect to translation. For this reason, we have to rely entirely on the English coreference links for the extraction of sentence pairs with it INLINEFORM0 es, as opposed to pairs with it INLINEFORM1 er and it INLINEFORM2 sie where we have coreference chains in both languages.
> 
> Our extraction process respects document boundaries, to ensure we always search for the right context. We extract additional information from the annotated documents, such as the distance (in sentences) between pronouns and their antecedents, the document of origin, lemma, morphology and dependency information if available.

#### Relevance 548

Label: 

#### Passage 550

Retrieved by: Dense, Hybrid

> We automatically create a test set from the OpenSubtitles corpus BIBREF22 . The goal is to provide a large number of difficult test cases where an English pronoun has to be translated to a German pronoun.
> 
> The most challenging cases are translating it to either er, sie or es, depending on the grammatical gender of the antecedent. Not only is the translation of it ambiguous, there is also class imbalance in the training data (see Table TABREF18 ). There is roughly a 30% probability that it is aligned to es, which makes it difficult to learn to translate er and sie. We use parsing and automatic co-reference resolution to find translation pairs that satisfy our constraints.
> 
> To provide a basis for filtering with constraints, we tokenize the whole data set with the Moses tokenizer, generate symmetric word alignments with fast_align BIBREF23 , parse the English text with CoreNLP BIBREF24 , parse the German text with ParZu BIBREF25 and perform coreference resolution on both sides. The coreference chains are obtained with the neural model of CoreNLP for English, and with CorZu for German BIBREF26 , respectively.
> 
> Then we opt for high-precision, aggressive filtering, according to the following protocol: for each pair of sentences INLINEFORM0 in English and German, extract iff
> 
> INLINEFORM0 contains the English pronoun it, and INLINEFORM1 contains a German pronoun that is third person singular (er, sie or es), as indicated by their part-of-speech tags;
> 
> those pronouns are aligned to each other;
> 
> both pronouns are in a coreference chain;
> 
> their nominal antecedents in the coreference chain are aligned on word level.
> 
> This removes most candidate pairs, but is necessary to overcome the noise introduced by our preprocessing pipeline, most notably coreference resolution. From the filtered set, we create a balanced test set by randomly sampling 4000 instances of each of the three translations of it under consideration (er, sie, es). We do not balance antecedent distance. See Table TABREF25 for the distribution of pronoun pairs and antecedent distance in the test set.
> 
> For each sentence pair in the resulting test set, we introduce contrastive translations. A contrastive translation is a translation variant where the correct pronoun is swapped with an incorrect one. For an

#### Relevance 550

Label: 

### BM25

#### Passage 547

Retrieved by: BM25

> All remaining models are based on the Transformer architecture BIBREF2 . A Transformer avoids recurrence completely: it follows an encoder-decoder architecture using stacked self-attention and fully connected layers for both the encoder and decoder.
> 
> baseline A standard context-agnostic Transformer. All model parameters are identical to a Transformer-base in BIBREF2 .
> 
> concat22 A simple concatentation model where only the training data is modified, in the same way as for the recurrent concat22 model.
> 
> concat21 Trained on data where the preceding sentence is concatenated to the current one only on the source side. This model is also taken from BIBREF5 .
> 
> BIBREF8 A more sophisticated context-aware Transformer that uses source context only. It has a separate encoder for source context, but all layers except the last one are shared between encoders. A source and context sentence are first encoded independently, and then a single attention layer and a gating function are used to produce a context-aware representation of the source sentence. Such restricted interaction with context is shown to be beneficial for analysis of contextual phenomena captured by the model. For details the reader is referred to their work.

#### Relevance 547

Label: 

### Dense

#### Passage 549

Retrieved by: Dense

> Contrastive evaluation requires a large set of suitable examples that involve the translation of pronouns. As additional goals, our test set is designed to 1) focus on hard cases, so that it can be used as a benchmark to track progress in context-aware translation and 2) allow for fine-grained analysis.
> 
> Section SECREF14 describes how we extract our data set. Section SECREF26 explains how, given a set of contrastive examples, contrastive evaluation works.

#### Relevance 549

Label: 

#### Passage 551

Retrieved by: Dense

> The BLEU scores in Table TABREF30 show a moderate improvement for most context-aware systems. This suggests that the architectural changes for the context-aware models do not degrade overall translation quality. The contrastive evaluation on our test set on the other hand shows a clear increase in the accuracy of pronoun translation: The best model s-hier-to-2.tied achieves a total of +16 percentage points accuracy on the test set over the baseline, see Table TABREF31 .
> 
> Table TABREF32 shows that context-aware models perform better than the baseline when the antecedent is outside the current sentence. In our experiments, all context-aware models consider one preceding sentence as context. The evaluation according to the distance of the antecedent in Table TABREF35 confirms that the subset of sentences with antecedent distance 1 benefits most from the tested context-aware models (up to +20 percentage points accuracy). However, we note two surprising patterns:
> 
> The first observation can be explained by the distribution of German pronouns in the test set. The further away the antecedent, the higher the percentage of it INLINEFORM0 es cases, which are the majority class, and thus the class that will be predicted most often if evidence for other classes is lacking. We speculate that this is due to our more permissive extraction heuristics for it INLINEFORM1 es.
> 
> We attribute the second observation to the existence of coreference chains where the preceding sentence contains a pronoun that refers to the same nominal antecedent as the pronoun in the current sentence. Consider the example in Table TABREF36 : The nominal antecedent of it in the current sentence is door, Tür in German with feminine gender. The nominal antecedent occurs two sentences before the current sentence, but the German sentence in between contains the pronoun sie, which is a useful signal for the context-aware models, even though they cannot know the nominal antecedent.
> 
> Note that only models aware of target-side context can benefit from such circumstances: The s-hier models as well as the Transformer model by BIBREF8 only see source side context, which results in lower accuracy if the distance to the antecedent is INLINEFORM0 1, see Table TABREF35 .
> 
> While such coreference chains complicate the interpretation of the results, we

#### Relevance 551

Label: 

### Hybrid

None

## Question 0071

Paper: Named Entity Recognition for Nepali Language

> Which models are used to solve NER for Nepali?

### Common Retrieved Chunks

#### Passage 552

Retrieved by: BM25, Dense, Hybrid

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

#### Relevance 552

Label: 

#### Passage 554

Retrieved by: BM25, Dense, Hybrid

> There has been a handful of research on Nepali NER task based on approaches like Support Vector Machine and gazetteer listBIBREF11 and Hidden Markov Model and gazetteer listBIBREF9,BIBREF10.
> 
> BIBREF11 uses SVM along with features like first word, word length, digit features and gazetteer (person, organization, location, middle name, verb, designation and others). It uses one vs rest classification model to classify each word into different entity classes. However, it does not the take context word into account while training the model. Similarly, BIBREF9 and BIBREF10 uses Hidden Markov Model with n-gram technique for extracting POS-tags. POS-tags with common noun, proper noun or combination of both are combined together, then uses gazetteer list as look-up table to identify the named entities.
> 
> Researchers have shown that the neural networks like CNNBIBREF12, RNNBIBREF13, LSTMBIBREF14, GRUBIBREF15 can capture the semantic knowledge of language better with the help of pre-trained embbeddings like word2vecBIBREF16, gloveBIBREF17 or fasttextBIBREF18.
> 
> Similar approaches has been applied to many South Asian languages like HindiBIBREF6, IndonesianBIBREF7, BengaliBIBREF19 and In this paper, we present the neural network architecture for NER task in Nepali language, which doesn't require any manual feature engineering nor any data pre-processing during training. First we are comparing BiLSTMBIBREF14, BiLSTM+CNNBIBREF20, BiLSTM+CRFBIBREF1, BiLSTM+CNN+CRFBIBREF2 models with CNN modelBIBREF0 and Stanford CRF modelBIBREF21. Secondly, we show the comparison between models trained on general word embeddings, word embedding + character-level embedding, word embedding + part-of-speech(POS) one-hot encoding and word embedding + grapheme clustered or sub-word embeddingBIBREF22. The experiments were performed on the dataset that we created and on the dataset received from ILPRL lab. Our extensive study shows that augmenting word embedding with character or grapheme-level representation and POS one-hot encoding vector yields better results compared to using general word embedding alone.

#### Relevance 554

Label: 

#### Passage 555

Retrieved by: BM25, Dense, Hybrid

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

#### Relevance 555

Label: 

#### Passage 556

Retrieved by: BM25, Dense, Hybrid

> The authors of this paper would like to express sincere thanks to Bal Krishna Bal, Kathmandu University Professor for providing us the POS-tagged Nepali NER data.

#### Relevance 556

Label: 

#### Passage 557

Retrieved by: Dense, Hybrid

> Since, we there was no publicly available standard Nepali NER dataset and did not receive any dataset from the previous researchers, we had to create our own dataset. This dataset contains the sentences collected from daily newspaper of the year 2015-2016. This dataset has three major classes Person (PER), Location (LOC) and Organization (ORG). Pre-processing was performed on the text before creation of the dataset, for example all punctuations and numbers besides ',', '-', '|' and '.' were removed. Currently, the dataset is in standard CoNLL-2003 IO formatBIBREF25.
> 
> Since, this dataset is not lemmatized originally, we lemmatized only the post-positions like Ek, kO, l, mA, m, my, jF, sg, aEG which are just the few examples among 299 post positions in Nepali language. We obtained these post-positions from sanjaalcorps and added few more to match our dataset. We will be releasing this list in our github repository. We found out that lemmatizing the post-positions boosted the F1 score by almost 10%.
> 
> In order to label our dataset with POS-tags, we first created POS annotated dataset of 6946 sentences and 16225 unique words extracted from POS-tagged Nepali National Corpus and trained a BiLSTM model with 95.14% accuracy which was used to create POS-tags for our dataset.
> 
> The dataset released in our github repository contains each word in newline with space separated POS-tags and Entity-tags. The sentences are separated by empty newline. A sample sentence from the dataset is presented in table FIGREF13.

#### Relevance 557

Label: 

### BM25

#### Passage 553

Retrieved by: BM25

> In this section, we present the details regarding evaluation and comparison of our models with other baselines.
> 
> Table TABREF25 shows the study of various embeddings and comparison among each other in OurNepali dataset. Here, raw dataset represents such dataset where post-positions are not lemmatized. We can observe that pre-trained embeddings significantly improves the score compared to randomly initialized embedding. We can deduce that Skip Gram models perform better compared CBOW models for word2vec and fasttext. Here, fastText_Pretrained represents the embedding readily available in fastText website, while other embeddings are trained on the Nepali National Corpus as mentioned in sub-section SECREF11. From this table TABREF25, we can clearly observe that model using fastText_Skip Gram embeddings outperforms all other models.
> 
> Table TABREF35 shows the model architecture comparison between all the models experimented. The features used for Stanford CRF classifier are words, letter n-grams of upto length 6, previous word and next word. This model is trained till the current function value is less than $1\mathrm {e}{-2}$. The hyper-parameters of neural network experiments are set as shown in table TABREF30. Since, word embedding of character-level and grapheme-level is random, their scores are near.
> 
> All models are evaluated using CoNLL-2003 evaluation scriptBIBREF25 to calculate entity-wise precision, recall and f1 score.

#### Relevance 553

Label: 

### Dense

None

### Hybrid

None

## Question 0072

Paper: Named Entities in Medical Case Reports: Corpus and Experiments

> How was annotation performed?

### Common Retrieved Chunks

#### Passage 558

Retrieved by: BM25, Dense, Hybrid

> The annotation was performed using WebAnno BIBREF7, a web-based tool for linguistic annotation. The annotators could choose between a pre-annotated version or a blank version of each text. The pre-annotated versions contained suggested entity spans based on string matches from lists of conditions and findings synonym lists. Their quality varied widely throughout the corpus. The blank version was preferred by the annotators. We distribute the corpus in BioC JSON format. BioC was chosen as it allows us to capture the complexities of the annotations in the biomedical domain. It represented each documents properties ranging from full text, individual passages/sentences along with captured annotations and relationships in an organized manner. BioC is based on character offsets of annotations and allows the stacking of different layers.

#### Relevance 558

Label: 

#### Passage 560

Retrieved by: BM25, Dense, Hybrid

> Case reports are standardized in the CARE guidelines BIBREF5. They represent a detailed description of the symptoms, signs, diagnosis, treatment, and follow-up of an individual patient. We focus on documents freely available through PubMed Central (PMC). The presentation of the patient's case can usually be found in a dedicated section or the abstract. We perform a manual annotation of all mentions of case entities, conditions, findings, factors and modifiers. The scope of our manual annotation is limited to the presentation of a patient's signs and symptoms. In addition, we annotate the title of the case report.

#### Relevance 560

Label: 

#### Passage 561

Retrieved by: BM25, Dense, Hybrid

> We asked medical doctors experienced in extracting knowledge related to medical entities from texts to annotate the entities described above. Initially, we asked four annotators to test our guidelines on two texts. Subsequently, identified issues were discussed and resolved. Following this pilot annotation phase, we asked two different annotators to annotate two case reports according to our guidelines. The same annotators annotated an overall collection of 53 case reports.
> 
> Inter-annotator agreement is calculated based on two case reports. We reach a Cohen's kappa BIBREF6 of 0.68. Disagreements mainly appear for findings that are rather unspecific such as She no longer eats out with friends which can be seen as a finding referring to “avoidance behaviour”.

#### Relevance 561

Label: 

#### Passage 562

Retrieved by: BM25, Dense, Hybrid

> The corpus consists of 53 documents, which contain an average number of 156.1 sentences per document, each with 19.55 tokens on average. The corpus comprises 8,275 sentences and 167,739 words in total. However, as mentioned above, only case presentation sections, headings and abstracts are annotated. The numbers of annotated entities are summarized in Table TABREF24.
> 
> Findings are the most frequently annotated type of entity. This makes sense given that findings paint a clinical picture of the patient's condition. The number of tokens per entity ranges from one token for all types to 5 tokens for cases (average length 3.1), nine tokens for conditions (average length 2.0), 16 tokens for factors (average length 2.5), 25 tokens for findings (average length 2.6) and 18 tokens for modifiers (average length 1.4) (cf. Table TABREF24). Examples of rather long entities are given in Table TABREF25.
> 
> Entities can appear in a discontinuous way. We model this as a relation between two spans which we call “discontinuous” (cf. Figure FIGREF26). Especially findings often appear as discontinuous entities, we found 543 discontinuous finding relations. The numbers for conditions and factors are lower with seven and two, respectively. Entities can also be nested within one another. This happens either when the span of one annotation is completely embedded in the span of another annotation (fully-nested; cf. Figure FIGREF12), or when there is a partial overlapping between the spans of two different entities (partially-nested; cf. Figure FIGREF12). There is a high number of inter-sentential relations in the corpus (cf. Table TABREF27). This can be explained by the fact that the case entity occurs early in each document; furthermore, it is related to finding and factor annotations that are distributed across different sentences.
> 
> The most frequently annotated relation in our corpus is the has-relation between a case entity and the findings related to that case. This correlates with the high number of finding entities. The relations contained in our corpus are summarized in Table TABREF27.

#### Relevance 562

Label: 

#### Passage 563

Retrieved by: Dense, Hybrid

> We annotate the following entities:
> 
> case entity marks the mention of a patient. A case report can contain more than one case description. Therefore, all the findings, factors and conditions related to one patient are linked to the respective case entity. Within the text, this entity is often represented by the first mention of the patient and overlaps with the factor annotations which can, e. g., mark sex and age (cf. Figure FIGREF12).
> 
> condition marks a medical disease such as pneumothorax or dislocation of the shoulder.
> 
> factor marks a feature of a patient which might influence the probability for a specific diagnosis. It can be immutable (e. g., sex and age), describe a specific medical history (e. g., diabetes mellitus) or a behaviour (e. g., smoking).
> 
> finding marks a sign or symptom a patient shows. This can be visible (e. g., rash), described by a patient (e. g., headache) or measurable (e. g., decreased blood glucose level).
> 
> negation modifier explicitly negate the presence of a certain finding usually setting the case apart from common cases.
> 
> We also annotate relations between these entities, where applicable. Since we work on case descriptions, the anchor point of these relations is the case that is described. The following relations are annotated:
> 
> has relations exist between a case entity and factor, finding or condition entities.
> 
> modifies relations exist between negation modifiers and findings.
> 
> causes relations exist between conditions and findings.
> 
> Example annotations are shown in Figure FIGREF16.

#### Relevance 563

Label: 

### BM25

#### Passage 559

Retrieved by: BM25

> Conditional Random Fields (CRF) BIBREF10 are a standard approach when dealing with sequential data in the context of sequence labeling. We use a combination of linguistic and semantic features, with a context window of size five, to describe each of the tokens and the dependencies between them. Hyper-parameter optimization is performed using randomized search and cross validation. Span-based F1 score is used as the optimization metric.

#### Relevance 559

Label: 

### Dense

None

### Hybrid

None

## Question 0073

Paper: Hard but Robust, Easy but Sensitive: How Encoder and Decoder Perform in Neural Machine Translation

> How do they determine that a decoder handles an easier task than the encoder?

### Common Retrieved Chunks

#### Passage 564

Retrieved by: BM25, Hybrid

> In this paper, we conducted a series of experiments to compare the characteristics of the encoder and decoder in NMT. We found that the decoder handles an easier task than the encoder, and the decoder is more sensitive to the input noise than the encoder. We further investigated why the decoder is more sensitive and the task it handles is easier, by analyzing the dependence of the decoder, and comparing the sensitivity to the input with non-autoregressive NMT. We hope our analyses inspire future research on NMT.
> 
> For future work, we will study the encoder-decoder framework in other machine learning tasks, such as text summarization, question answering and image captioning.

#### Relevance 564

Label: 

#### Passage 566

Retrieved by: BM25, Hybrid

> Given the observations in Section SECREF3 and SECREF4, we find that the decoder is more sensitive to the input tokens compared with the encoder, and the task that decoder handles is easier. In this section, we give an explanation on this phenomenon. More details on experimental configurations are described in supplementary materials (Section 1.3). Besides, we also investigate which kind of input tokens the encoder and decoder are more sensitive to, from the perspective of Part-Of-Speech (POS), and show the results in the supplementary materials (Section 2) due to space limitation.

#### Relevance 566

Label: 

#### Passage 567

Retrieved by: BM25, Dense, Hybrid

> From the analyses in the last two subsections, it can be seen that increasing the layer of encoder brings more gains than increasing the layer of the decoder, and encoder needs more training time than the decoder, which demonstrate that the encoder of the NMT model handles a more difficult task than the decoder.

#### Relevance 567

Label: 

#### Passage 568

Retrieved by: BM25, Hybrid

> In general, the encoder and decoder perform different functionalities in an NMT model. In this section, we compare the characteristics between the encoder and decoder by analyzing the difficulty of the corresponding task they handle in NMT. We investigate the task difficulty by comparing the training effort of the encoder and decoder from two perspectives: the number of layers and the convergence speed for the encoder and decoder respectively.
> 
> We train the Transformer BIBREF3 on IWSLT14 German$\leftrightarrow $English (De$\leftrightarrow $En) and Romanian$\leftrightarrow $English (Ro$\leftrightarrow $En) translation. The translation quality is measured by BLEU score. More details on datasets, model configurations and evaluation metrics can be found in the supplementary materials (Section 1.1).

#### Relevance 568

Label: 

#### Passage 571

Retrieved by: Dense, Hybrid

> We further investigate the difficulty of the task for the encoder and decoder by comparing their convergence speed. Encoder (decoder) that needs more training time indicates the task that encoder (decoder) handles is more difficult.
> 
> We evaluate the convergence speed for the encoder by initializing the model with the parameters of a well-trained decoder and fixing them during training, and initializing other components with random variables. We follow the opposite practice when evaluating the convergence speed for the decoder. We show the BLEU scores along the training process on all the four datasets in Figure FIGREF6, which demonstrates that the decoder converges faster than the encoder.

#### Relevance 571

Label: 

### BM25

#### Passage 565

Retrieved by: BM25

> The encoder-decoder based framework BIBREF0, BIBREF1, BIBREF2 is the dominant approach for neural machine translation (NMT) BIBREF3, BIBREF4. Although the encoder and decoder usually adopt the same model structure (RNN BIBREF5, CNN BIBREF6 or self-attention BIBREF3, BIBREF7) and the same number of layers, they perform different functionalities: the encoder extracts the hidden representations of the source sentence, and the decoder generates target tokens conditioned on the source hidden representations as well as the previous generated tokens.
> 
> While most existing works focus on the design and improvement of encoder-decoder framework for NMT BIBREF8, BIBREF6, BIBREF3, BIBREF9 as well as its detailed analyses BIBREF10, BIBREF11, BIBREF12, BIBREF13, few works concentrate on the characteristics and functionalities of the encoder and the decoder, which are valuable to understand this popular framework and improve its performance in NMT. Therefore, in this paper, we conduct a study and aim to understand the characteristics of the encoder and the decoder in NMT. We observe some interesting phenomena:
> 
> The decoder handles an easier task than the encoder. 1) We find that adding more layers to the encoder achieves larger improvements than adding more layers to the decoder. 2) We also compare the training time of the encoder and decoder by fixing the parameters of a well-trained decoder (encoder), and just update the parameters of the encoder (decoder). We found that the decoder converges faster than the encoder. These two results suggest that the decoder handles an easier task than the encoder in NMT.
> 
> The decoder is more sensitive to the input noise than the encoder. We randomly add different level of noise to the input of the encoder and decoder respectively during inference, and find that adding noise to the input of the decoder leads to better accuracy drop than that of the encoder.
> 
> We further analyze why the decoder is more sensitive by masking the previous tokens, and comparing autoregressive NMT with the non-autoregressive counterpart. We find that the preceding tokens in the decoder provide strong conditional information, which partially explain the previous two observations on the decoder.
> 
> We believe our studies on the different characteristics of the encoder and decoder will inspire the following research on the encoder-decoder framework as well

#### Relevance 565

Label: 

### Dense

#### Passage 569

Retrieved by: Dense

> We investigate the task difficulty by comparing the training effort of the encoder and decoder from two perspectives in the paper: 1) We vary the number of layers for the encoder and decoder respectively. All models are trained with the same configuration as described before except for the number of layers. 2) For training the encoder side, we initialize the decoder side with the parameters of a well-trained decoder, and initialize other components with random variable. For training decoder side, we follow the opposite operation.

#### Relevance 569

Label: 

#### Passage 570

Retrieved by: Dense

> The consistent observations above suggest that the decoder is much more sensitive to the input noise than the encoder. Intuitively, the encoder aims at extracting abstract representations of the source sentence instead of depending on certain input tokens for prediction as the decoder does, demonstrating that the encoder is more robust than the decoder.

#### Relevance 570

Label: 

#### Passage 572

Retrieved by: Dense

> the decoder provide strong conditional information, which partially explain the previous two observations on the decoder.
> 
> We believe our studies on the different characteristics of the encoder and decoder will inspire the following research on the encoder-decoder framework as well as improve the performance on NMT and other encoder-decoder based tasks.

#### Relevance 572

Label: 

### Hybrid

None

## Question 0074

Paper: Exploiting Token and Path-based Representations of Code for Identifying Security-Relevant Commits

> How long is the dataset?

### Common Retrieved Chunks

#### Passage 573

Retrieved by: BM25, Hybrid

> that learns from path-based representations of code and claimed by BIBREF3 to be suitable for a wide range of source code classification tasks, performs worse than our logistic regression baseline.
> 
> In this study, we seek to answer the following research questions:
> 
> [leftmargin=*]
> 
> RQ1: Can we effectively identify security-relevant commits using only the commit diff? For this research question, we do not use any of the commit metadata such as the commit message or information about the author. We treat source code changes like unstructured text without using path-based representations from the abstract syntax tree.
> 
> RQ2: Does extracting class-level features before and after the change instead of using only the commit diff improve the identification of security-relevant commits? For this research question, we test the hypothesis that the source code of the entire Java class contains more information than just the commit diff and could potentially improve the performance of our model.
> 
> RQ3: Does exploiting path-based representations of Java source code before and after the change improve the identification of security-relevant commits? For this research question, we test whether code2vec, a state-of-the-art model that learns from path-based representations of code, performs better than our model that treats source code as unstructured text.
> 
> RQ4: Is mining commits using regular expression matching of commit messages an effective means of data augmentation for improving the identification of security-relevant commits? Since labelling commits manually is an expensive task, it is not easy to build a dataset large enough to train deep learning models. For this research question, we explore if collecting coarse data samples using a high-precision approach is an effective way to augment the ground-truth dataset.
> 
> The main contributions of this paper are:
> 
> [leftmargin=*]
> 
> Novel hierarchical deep learning models for the identification of security-relevant commits based on either the diff or the modified source code of the Java classes.
> 
> A comparative analysis of how various deep learning models perform across different input representations and how various regularization techniques help with the generalization of our models.
> 
> We envision that this work would ultimately allow for monitoring open-source repositories in real-time, in order to automatically detect security-relevant changes such as vulnerability fixes.

#### Relevance 573

Label: 

#### Passage 574

Retrieved by: BM25, Dense, Hybrid

> The lexer and tokenizer we use from the javalang library target Java 8. We are not able to verify that all the projects and their forks in this study are using the same version of Java. However, we do not expect considerable differences in syntax between Java 7 and Java 8 except for the introduction of lambda expressions.
> 
> There is also a question of to what extent the 635 publicly disclosed vulnerabilities used for evaluation in this study represent the vulnerabilities found in real-world scenarios. While creating larger ground-truth datasets would always be helpful, it might not always be possible. To reduce the possibility of bias in our results, we ensure that we don't train commits from the same projects that we evaluate our models on. We also discard any commits belonging to the set of evaluation projects that are mined using regular expression matching.
> 
> We directly train code2vec on our dataset without pre-training it, in order to assess how well path-based representations perform for learning on code, as opposed to token-level representations on which H-CNN and HR-CNN are based. However, BIBREF16 pre-trained their model on 10M Java classes. It is possible that the performance of code2vec is considerably better than the results in Table TABREF22 after pre-training. Furthermore, our findings apply only to this particular technique to capturing path-based representations, not the approach in general. However, we leave both issues for future work.

#### Relevance 574

Label: 

#### Passage 576

Retrieved by: BM25, Dense, Hybrid

> This section details the methodology used in this study to build the training dataset, the models used for classification and the evaluation procedure. All of the experiments are conducted on Python 3.7 running on an Intel Core i7 6800K CPU and a Nvidia GTX 1080 GPU. All the deep learning models are implemented in PyTorch 0.4.1 BIBREF21, while Scikit-learn 0.19.2 BIBREF22 is used for computing the tf–idf vectors and performing logistic regression.
> 
> For training our classification models, we use a manually-curated dataset of publicly disclosed vulnerabilities in 205 distinct open-source Java projects mapped to commits fixing them, provided by BIBREF23. These repositories are split into training, validation, and test splits containing 808, 265, and 264 commits, respectively. In order to minimize the occurrence of duplicate commits in two of these splits (such as in both training and test), commits from no repository belong to more than one split. However, 808 commits may not be sufficient to train deep learning models. Hence, in order to answer RQ4, we augment the training split with commits mined using regular expression matching on the commit messages from the same set of open-source Java projects. This almost doubles the number of commits in the training split to 1493. We then repeat our experiments for the first three research questions on the augmented dataset, and evaluate our trained models on the same validation and test splits.
> 
> We also compare the quality of randomly-initialized embeddings with pre-trained ones. Since the word2vec embeddings only need unlabelled data to train, the data collection and preprocessing stage is straightforward. GitHub, being a very large host of source code, contains enough code for training such models. However, a significant proportion of code in GitHub does not belong to engineered software projects BIBREF24. To reduce the amount of noise in our training data, we filter repositories based on their size, commit history, number of issues, pull requests, and contributors, and build a corpus of the top 1000 Java repositories. We limit the number of repositories to 1000 due to GitHub API limitations. It is worth noting that using a larger training corpus might provide better results. For instance, code2vec is pre-trained on a corpus that is ten

#### Relevance 576

Label: 

#### Passage 577

Retrieved by: BM25, Dense, Hybrid

> and after the change improve the identification of security-relevant commits?
> 
> Table TABREF22, row 10, shows that training the modified code2vec model to identify security-aware commits from scratch results in a model that performs worse than the LR baseline. The model only achieves an accuracy of 63.8% on the test split, with an $\text{F}_1$score of 72.7%, which is two points less than that of LR. The code2vec model performs much worse compared to H-CNN and HR-CNN with randomly-initialized embeddings. Hence, learning from a path-based representation of the Java classes before and after the change does not improve the identification of security-relevant commits—at least with the code2vec approach.
> 
> RQ4: Is mining commits using regular expression matching of commit messages an effective means of data augmentation for improving the identification of security-relevant commits?
> 
> The results in Table TABREF22, rows 11 to 20, show that collecting coarse data samples using regular expression matching for augmenting the ground-truth training set is not effective in increasing the performance of our models. This could possibly be due to the coarse data samples being too noisy or the distribution of security-relevant commits in the coarse dataset not matching that of the unseen dataset. The latter might have been due to the high-precision mining technique used, capturing only a small subset of security vulnerabilities.

#### Relevance 577

Label: 

#### Passage 578

Retrieved by: Dense, Hybrid

> We modify our model accordingly for every research question, based on changes in the input representation. To benchmark the performance of our deep learning models, we compare them against a logistic regression (LR) baseline that learns on one-hot representations of the Java tokens extracted from the commit diffs. For all of our models, we employ dropout on the fully-connected layer for regularization. We use Adam BIBREF25 for optimization, with a learning rate of 0.001, and batch size of 16 for randomly initialized embeddings and 8 for pre-trained embeddings.
> 
> For RQ1, we use a hierarchical CNN (H-CNN) with either randomly-initialized or pre-trained word embeddings in order to extract features from the commit diff. We represent the commit diff as a concatenation of 300-dimensional vectors for each corresponding token from that diff. This resultant matrix is then passed through three temporal convolutional layers in parallel, with filter windows of size 3, 5, and 7. A temporal max-pooling operation is applied to these feature maps to retain the feature with the highest value in every map. We also present a regularized version of this model (henceforth referred to as HR-CNN) with embedding dropout applied on the inputs, and DropBlock on the activations of the convolutional layers.
> 
> For RQ2, we made a modification to both the H-CNN and HR-CNN models in order to extract features from the source code for the Java classes before and after the commit. Both of these models use a siamese architecture between the two CNN-based encoders as shown in Figure FIGREF20. We then concatenate the results from both of these encoders and pass it through a fully-connected layer followed by softmax for prediction.
> 
> For RQ3, we adapt the code2vec model used by BIBREF16 for predicting method names into a model for predicting whether a commit is security-relevant by modifying the final layer. We then repeat our experiments on both the ground-truth and augmented dataset.

#### Relevance 578

Label: 

### BM25

#### Passage 575

Retrieved by: BM25

> While building usable embeddings for source code that capture the complex characteristics involving both syntax and semantics is a challenging task, such embeddings have direct downstream applications in tasks such as semantic code clone detection, code captioning, and code completion BIBREF14, BIBREF15. In the same vein as BIBREF4, neural networks have been used for representing snippets of code as continuous distributed vectors BIBREF16. They represent a code snippet as a bag of contexts and each context is represented by a context vector, followed by a path-attention network that learns how to aggregate these context vectors in a weighted manner.
> 
> A number of other code embedding techniques are also available in the literature. BIBREF17 learn word embeddings from abstractions of traces obtained from the symbolic execution of a program. They evaluate their learned embeddings on a benchmark of API-usage analogies extracted from the Linux kernel and achieved 93% top-1 accuracy. BIBREF18 describe a pipeline that leverages deep learning for semantic search of code. To achieve this, they train a sequence-to-sequence model that learns to summarize Python code by predicting the corresponding docstring from the code blob, and in the process provide code representations for Python.

#### Relevance 575

Label: 

### Dense

#### Passage 579

Retrieved by: Dense

> Java repositories. We limit the number of repositories to 1000 due to GitHub API limitations. It is worth noting that using a larger training corpus might provide better results. For instance, code2vec is pre-trained on a corpus that is ten times larger.
> 
> To extract token-level features for our model, we use the lexer and tokenizer provided as a part of the Python javalang library. We ensure that we only use the code and not code comments or metadata, as it is possible for comments or commit messages to include which vulnerabilities are fixed, as shown in Figure FIGREF12. Our models would then overfit on these features rather than learning the features from the code. For extracting path-based representations from Java code, we use ASTMiner.

#### Relevance 579

Label: 

### Hybrid

None

## Question 0075

Paper: Analyzing ASR pretraining for low-resource speech-to-text translation

> What languages did they use?

### Common Retrieved Chunks

#### Passage 580

Retrieved by: BM25, Dense, Hybrid

> Although our main focus is monolingual pretraining, we also looked briefly at multilingual pretraining, inspired by recent work on multilingual ASR BIBREF28, BIBREF29 and evidence that multilingual pretraining followed by fine-tuning on a distinct target language can improve ASR on the target language BIBREF10, BIBREF30, BIBREF31. These experiments did not directly compare pretraining using a similar amount of monolingual data, but such a comparison was done by BIBREF32, BIBREF33 in their work on learning feature representations for a target language with no transcribed data. They found a benefit for multilingual vs monolingual pretraining given the same amount of data.
> 
> Following up on this work, we tried pretraining using 124 hours of multilingual data (all GlobalPhone languages except Chinese), roughly the amount of data in our large Chinese models. We combined all the data together and trained an ASR model using a common target BPE with 6k merge operations, then transferred only the encoder to the AST model. However, we did not see a benefit to the multilingual training (Table TABREF7, final row); in fact the resulting AST model was slightly worse than the zh-ai-large model (BLEU of 13.3 vs 14.6). Other configurations of multilingual training might still outperform their monolingual counterparts, but we leave this investigation as future work.

#### Relevance 580

Label: 

#### Passage 581

Retrieved by: BM25, Hybrid

> This paper explored what factors help pretraining for low-resource AST. We performed careful comparisons to tease apart the effects of language relatedness and data size, ultimately finding that rather than either of these, the WER of the pre-trained ASR model is likely the best direct predictor of AST performance. Given equivalent amounts of data, we did not find multilingual pretraining to help more than monolingual pretraining, but we did find an added benefit from using speed perturbation to augment the AST data. Finally, analysis of the pretrained models suggests that those models with better WER are transparently encoding more language-universal phonetic information in the later RNN layers, and this appears to help with AST.

#### Relevance 581

Label: 

#### Passage 582

Retrieved by: BM25, Dense, Hybrid

> Low-resource automatic speech-to-text translation (AST) has recently gained traction as a way to bring NLP tools to under-represented languages. An end-to-end approach BIBREF0, BIBREF1, BIBREF2, BIBREF3, BIBREF4, BIBREF5, BIBREF6 is particularly appealing for source languages with no written form, or for endangered languages where translations into a high-resource language may be easier to collect than transcriptions BIBREF7. However, building high-quality end-to-end AST with little parallel data is challenging, and has led researchers to explore how other sources of data could be used to help.
> 
> A number of methods have been investigated. Several of these use transcribed source language audio and/or translated source language text in a multitask learning scenario BIBREF8, BIBREF3, BIBREF5 or to pre-train parts of the model before fine-tuning on the end-to-end AST task BIBREF3. Others assume, as we do here, that no additional source language resources are available, in which case transfer learning using data from language(s) other than the source language is a good option. In particular, several researchers have shown that low-resource AST can be improved by pretraining on an ASR task in some other language, then transferring the encoder parameters to initialize the AST model. For example, Bansal et al. BIBREF4 showed that pre-training on either English or French ASR improved their Spanish-English AST system (trained on 20 hours of parallel data) and Tian BIBREF9 got improvements on an 8-hour Swahili-English AST dataset using English ASR pretraining.
> 
> Overall these results show that pretraining helps, but leave open the question of what factors affect the degree of improvement. For example, does language relatedness play a role, or simply the amount of pretraining data? Bansal et al. showed bigger AST gains as the amount of English pretraining data increased from 20 to 300 hours, and also found a slightly larger improvement when pretraining on 20 hours of English versus 20 hours of French, but they pointed out that the Spanish data contains many English code-switched words, which could explain the latter result. In related work on multilingual pretraining for low-resource ASR, Adams et al. BIBREF10 showed that pre-training on more languages helps, but it is not clear whether the improvement is due to including more languages, or just more data.
> 
> To

#### Relevance 582

Label: 

#### Passage 584

Retrieved by: BM25, Dense, Hybrid

> result. In related work on multilingual pretraining for low-resource ASR, Adams et al. BIBREF10 showed that pre-training on more languages helps, but it is not clear whether the improvement is due to including more languages, or just more data.
> 
> To begin to tease apart these issues, we focus here on monolingual pretraining for low-resource AST, and investigate two questions. First, can we predict what sort of pretraining data is best for a particular AST task? Does it matter if the pretraining language is related to the AST source language (defined here as part of the same language family, since phonetic similarity is difficult to measure), or is the amount of pretraining data (or some other factor) more important? Second, can pretraining be effectively combined with other methods, such as data augmentation, in order to further improve AST results?
> 
> To answer these questions, we use the same AST architecture and Spanish-English parallel data as Bansal et al. BIBREF4, but pretrain the encoder using a number of different ASR datasets: the 150-hour AISHELL corpus of Chinese as well as seven GlobalPhone languages, each with about 20 hours of data. We find that pretraining on a larger amount of data from an unrelated language is much better than pretraining on a smaller amount of data from a related language. Moreover, even when controlling for the amount of data, the WER of the ASR model from pretraining seems to be a better predictor of final AST performance than does language relatedness. Indeed, we show that there is a very strong correlation between the WER of the pretraining model and BLEU score of the final AST model—i.e., the best pretraining strategy may simply be to use datasets and methods that will yield the lowest ASR WER during pretraining. However, we also found that AST results can be improved further by augmenting the AST data using standard speed perturbation techniques BIBREF11. Our best results using non-English pretraining data improve the test set BLEU scores of an AST system trained on 20 hours of parallel data from 10.2 to 14.3, increasing to 15.8 with data augmentation.
> 
> Finally, we analyze the representations learned by the models and show that better performance seems to

#### Relevance 584

Label: 

#### Passage 585

Retrieved by: Dense, Hybrid

> Since we focus on investigating factors that might affect the AST improvements over the baseline when pretraining, we have chosen ASR datasets for pretraining that contrast in the number of hours and/or in the language similarity with Spanish. Statistics for each dataset are in the left half of Table TABREF7, with further details below.
> 
> To look at a range of languages with similar amounts of data, we used GlobalPhone corpora from seven languages BIBREF15, each with around 20 hours of speech: Mandarin Chinese (zh), Croatian (hr), Czech (cs), French (fr), Polish (pl), Portuguese (pt), and Swedish (sv). French and Portuguese, like the source language (Spanish), belong to the Romance family of languages, while the other languages are less related—especially Chinese, which is not an Indo-European language. GlobalPhone consists of read speech recorded using similar conditions across languages, and the transcriptions for Chinese are Romanized, with annotated word boundaries.
> 
> To explore the effects of using a large amount of pretraining data from an unrelated language, we used the AISHELL-1 corpus of Mandarin Chinese BIBREF16, which contains 150 hours of read speech. Transcriptions with annotated word boundaries are available in both Hanzi (Chinese characters) and Romanized versions, and we built models with each. To compare to the GlobalPhone data, we also created a 20-hour subset of the Romanized AISHELL (zh-ai-small) by randomly selecting utterances from a subset of the speakers (81, roughly the number present in most of the GlobalPhone datasets).
> 
> Finally, to reproduce one of the experiments from BIBREF4, we pre-trained one model using 300 hours of Switchboard English BIBREF17. This data is the most similar to the AST speech data in terms of style and channel (both are conversational telephone speech). However, as noted by BIBREF4, the Fisher Spanish speech contains many words that are actually in English (code-switching), so pretraining on English may provide an unfair advantage relative to other languages.

#### Relevance 585

Label: 

### BM25

#### Passage 583

Retrieved by: BM25

> Our baseline 20-hour AST system obtains a BLEU score of 10.3 (Table TABREF7, first row), 0.5 BLEU point lower than that reported by BIBREF4. This discrepancy might be due to differences in subsampling from the 160-hour AST dataset to create the 20-hour subset, or from Kaldi parameters when computing the MFCCs.
> 
> WERs for our pre-trained models (Table TABREF7) vary from 22.5 for the large AISHELL dataset with Romanized transcript to 80.5 for Portuguese GlobalPhone. These are considerably worse than state-of-the-art ASR systems (e.g., Kaldi recipes can achieve WER of 7.5 on AISHELL and 26.5 on Portuguese GlobalPhone), but we did not optimize our architecture or hyperparameters for the ASR task since our main goal is to analyze the relationship between pretraining and AST performance (and in order to use pretraining, we must use a seq2seq model with the architecture as for AST).

#### Relevance 583

Label: 

### Dense

#### Passage 586

Retrieved by: Dense

> AST results for our pre-trained models are given in Table TABREF7. Pretraining improves AST performance in every case, with improvements ranging from 0.2 (pt-gp) to 4.3 (zh-ai-large). These results make it clear that language relatedness does not play a strong role in predicting AST improvements, since on the similar-sized GlobalPhone datasets, the two languages most related to Spanish (French and Portuguese) yield the highest and lowest improvements, respectively. Moreover, pretraining on the large Chinese dataset yields a bigger improvement than either of these—4.3 BLEU points. This is nearly as much as the 6 point improvement reported by BIBREF4 when pretraining on 100 hours of English data, which is especially surprising given not only that Chinese is very different from Spanish, but also that the Spanish data contains some English words.
> 
> This finding seems to suggest that data size is more important than language relatedness for predicting the effects of pretraining. However, there are big differences even amongst the languages with similar amounts of pretraining data. Analyzing our results further, we found a striking correlation between the WER of the initial ASR model and the BLEU score of the AST system pretrained using that model, as shown in Figure FIGREF11. Therefore, although pretraining data size clearly influences AST performance, this appears to be mainly due to its effect on WER of the ASR model. We therefore hypothesize that WER is a better direct predictor of AST performance than either data size or language relatedness.

#### Relevance 586

Label: 

### Hybrid

None

## Question 0076

Paper: Open Event Extraction from Online Text using a Generative Adversarial Network

> What baseline approaches does this approach out-perform?

### Common Retrieved Chunks

#### Passage 587

Retrieved by: BM25, Dense, Hybrid

> To evaluate the performance of the proposed approach, we use the evaluation metrics such as precision, recall and F-measure. Precision is defined as the proportion of the correctly identified events out of the model generated events. Recall is defined as the proportion of correctly identified true events. For calculating the precision of the 4-tuple, we use following criteria:
> 
> (1) Do the entity/organization, location, date/person and keyword that we have extracted refer to the same event?
> 
> (2) If the extracted representation contains keywords, are they informative enough to tell us what happened?
> 
> Table TABREF35 shows the event extraction results on the three datasets. The statistics are obtained with the default parameter setting that INLINEFORM0 is set to 5, number of hidden units INLINEFORM1 is set to 200, and INLINEFORM2 contains three fully-connected layers. The event number INLINEFORM3 for three datasets are set to 25, 25 and 35, respectively. The examples of extracted events are shown in Table. TABREF36 .
> 
> It can be observed that K-means performs the worst over all three datasets. On the social media datasets, AEM outpoerforms both LEM and DPEMM by 6.5% and 1.7% respectively in F-measure on the FSD dataset, and 4.4% and 3.7% in F-measure on the Twitter dataset. We can also observe that apart from K-means, all the approaches perform worse on the Twitter dataset compared to FSD, possibly due to the limited size of the Twitter dataset. Moreover, on the Google dataset, the proposed AEM performs significantly better than LEM and DPEMM. It improves upon LEM by 15.5% and upon DPEMM by more than 30% in F-measure. This is because: (1) the assumption made by LEM and DPEMM that all words in a document are generated from a single event is not suitable for long text such as news articles; (2) DPEMM generates too many irrelevant events which leads to a very low precision score. Overall, we see the superior performance of AEM across all datasets, with more significant improvement on the for Google datasets (long text).
> 
> We next visualize the detected events based on the discriminative features learned by the trained INLINEFORM0 network in AEM. The t-SNE BIBREF16 visualization results on the datasets are shown in Figure FIGREF19

#### Relevance 587

Label: 

#### Passage 588

Retrieved by: BM25, Dense, Hybrid

> In this section, we firstly describe the datasets and baseline approaches used in our experiments and then present the experimental results.

#### Relevance 588

Label: 

#### Passage 591

Retrieved by: BM25, Hybrid

> To validate the effectiveness of AEM for extracting events from social media (e.g. Twitter) and news media sites (e.g. Google news), three datasets (FSD BIBREF12 , Twitter, and Google datasets) are employed. Details are summarized below:
> 
> FSD dataset (social media) is the first story detection dataset containing 2,499 tweets. We filter out events mentioned in less than 15 tweets since events mentioned in very few tweets are less likely to be significant. The final dataset contains 2,453 tweets annotated with 20 events.
> 
> Twitter dataset (social media) is collected from tweets published in the month of December in 2010 using Twitter streaming API. It contains 1,000 tweets annotated with 20 events.
> 
> Google dataset (news article) is a subset of GDELT Event Database INLINEFORM0 , documents are retrieved by event related words. For example, documents which contain `malaysia', `airline', `search' and `plane' are retrieved for event MH370. By combining 30 events related documents, the dataset contains 11,909 news articles.
> 
> We choose the following three models as the baselines:
> 
> K-means is a well known data clustering algorithm, we implement the algorithm using sklearn toolbox, and represent documents using bag-of-words weighted by TF-IDF.
> 
> LEM BIBREF13 is a Bayesian modeling approach for open-domain event extraction. It treats an event as a latent variable and models the generation of an event as a joint distribution of its individual event elements. We implement the algorithm with the default configuration.
> 
> DPEMM BIBREF14 is a non-parametric mixture model for event extraction. It addresses the limitation of LEM that the number of events should be known beforehand. We implement the model with the default configuration.
> 
> For social media text corpus (FSD and Twitter), a named entity tagger specifically built for Twitter is used to extract named entities including locations from tweets. A Twitter Part-of-Speech (POS) tagger BIBREF15 is used for POS tagging and only words tagged with nouns, verbs and adjectives are retained as keywords. For the Google dataset, we use the Stanford Named Entity Recognizer to identify the named entities (organization, location and person). Due to the `date' information not being provided in the Google dataset, we further divide the non-location named entities into two categories (`person' and `organization') and employ a quadruple <organization,

#### Relevance 591

Label: 

#### Passage 593

Retrieved by: Dense, Hybrid

> As a neural-based generative model, Generative Adversarial Nets BIBREF3 have been extensively researched in natural language processing (NLP) community.
> 
> For text generation, the sequence generative adversarial network (SeqGAN) proposed in BIBREF4 incorporated a policy gradient strategy to optimize the generation process. Based on the policy gradient, Lin et al. lin2017adversarial proposed RankGAN to capture the rich structures of language by ranking and analyzing a collection of human-written and machine-written sentences. To overcome mode collapse when dealing with discrete data, Fedus et al. fedus2018maskgan proposed MaskGAN which used an actor-critic conditional GAN to fill in missing text conditioned on the surrounding context. Along this line, Wang et al. wang2018sentigan proposed SentiGAN to generate texts of different sentiment labels. Besides, Li et al. li2018learning improved the performance of semi-supervised text classification using adversarial training, BIBREF5 , BIBREF6 designed GAN-based models for distance supervision relation extraction.
> 
> Although various GAN based approaches have been explored for many applications, none of these approaches tackles open-domain event extraction from online texts. We propose a novel GAN-based event extraction model called AEM. Compared with the previous models, AEM has the following differences: (1) Unlike most GAN-based text generation approaches, a generator network is employed in AEM to learn the projection function between an event distribution and the event-related word distributions (entity, location, keyword, date). The learned generator captures event-related patterns rather than generating text sequence; (2) Different from LEM and DPEMM, AEM uses a generator network to capture the event-related patterns and is able to mine events from different text sources (short and long). Moreover, unlike traditional inference procedure, such as Gibbs sampling used in LEM and DPEMM, AEM could extract the events more efficiently due to the CUDA acceleration; (3) The discriminative features learned by the discriminator of AEM provide a straightforward way to visualize the extracted events.

#### Relevance 593

Label: 

### BM25

#### Passage 589

Retrieved by: BM25

> With the increasing popularity of the Internet, online texts provided by social media platform (e.g. Twitter) and news media sites (e.g. Google news) have become important sources of real-world events. Therefore, it is crucial to automatically extract events from online texts.
> 
> Due to the high variety of events discussed online and the difficulty in obtaining annotated data for training, traditional template-based or supervised learning approaches for event extraction are no longer applicable in dealing with online texts. Nevertheless, newsworthy events are often discussed by many tweets or online news articles. Therefore, the same event could be mentioned by a high volume of redundant tweets or news articles. This property inspires the research community to devise clustering-based models BIBREF0 , BIBREF1 , BIBREF2 to discover new or previously unidentified events without extracting structured representations.
> 
> To extract structured representations of events such as who did what, when, where and why, Bayesian approaches have made some progress. Assuming that each document is assigned to a single event, which is modeled as a joint distribution over the named entities, the date and the location of the event, and the event-related keywords, Zhou et al. zhou2014simple proposed an unsupervised Latent Event Model (LEM) for open-domain event extraction. To address the limitation that LEM requires the number of events to be pre-set, Zhou et al. zhou2017event further proposed the Dirichlet Process Event Mixture Model (DPEMM) in which the number of events can be learned automatically from data. However, both LEM and DPEMM have two limitations: (1) they assume that all words in a document are generated from a single event which can be represented by a quadruple INLINEFORM0 entity, location, keyword, date INLINEFORM1 . However, long texts such news articles often describe multiple events which clearly violates this assumption; (2) During the inference process of both approaches, the Gibbs sampler needs to compute the conditional posterior distribution and assigns an event for each document. This is time consuming and takes long time to converge.
> 
> To deal with these limitations, in this paper, we propose the Adversarial-neural Event Model (AEM) based on adversarial training for open-domain event extraction. The principle idea is to use a generator network to learn the projection function

#### Relevance 589

Label: 

#### Passage 590

Retrieved by: BM25

> In this paper, we have proposed a novel approach based on adversarial training to extract the structured representation of events from online text. The experimental comparison with the state-of-the-art methods shows that AEM achieves improved extraction performance, especially on long text corpora with an improvement of 15% observed in F-measure. AEM only requires a fraction of training time compared to existing Bayesian graphical modeling approaches. In future work, we will explore incorporating external knowledge (e.g. word relatedness contained in word embeddings) into the learning framework for event extraction. Besides, exploring nonparametric neural event extraction approaches and detecting the evolution of events over time from news articles are other promising future directions.

#### Relevance 590

Label: 

### Dense

#### Passage 592

Retrieved by: Dense

> improvement on the for Google datasets (long text).
> 
> We next visualize the detected events based on the discriminative features learned by the trained INLINEFORM0 network in AEM. The t-SNE BIBREF16 visualization results on the datasets are shown in Figure FIGREF19 . For clarity, each subplot is plotted on a subset of the dataset containing ten randomly selected events. It can be observed that documents describing the same event have been grouped into the same cluster.
> 
> To further evaluate if a variation of the parameters INLINEFORM0 (the number of discriminator iterations per generator iteration), INLINEFORM1 (the number of units in hidden layer) and the structure of generator INLINEFORM2 will impact the extraction performance, additional experiments have been conducted on the Google dataset, with INLINEFORM3 set to 5, 7 and 10, INLINEFORM4 set to 100, 150 and 200, and three INLINEFORM5 structures (3, 4 and 5 layers). The comparison results on precision, recall and F-measure are shown in Figure FIGREF20 . From the results, it could be observed that AEM with the 5-layer generator performs the best and achieves 96.7% in F-measure, and the worst F-measure obtained by AEM is 85.7%. Overall, the AEM outperforms all compared approaches acorss various parameter settings, showing relatively stable performance.
> 
> Finally, we compare in Figure FIGREF37 the training time required for each model, excluding the constant time required by each model to load the data. We could observe that K-means runs fastest among all four approaches. Both LEM and DPEMM need to sample the event allocation for each document and update the relevant counts during Gibbs sampling which are time consuming. AEM only requires a fraction of the training time compared to LEM and DPEMM. Moreover, on a larger dataset such as the Google dataset, AEM appears to be far more efficient compared to LEM and DPEMM.

#### Relevance 592

Label: 

#### Passage 594

Retrieved by: Dense

> The real document INLINEFORM0 and fake document INLINEFORM1 shown in Figure FIGREF4 could be viewed as random samples from two distributions INLINEFORM2 and INLINEFORM3 , and each of them is a joint distribution constituted by four Dirichlet distributions (corresponding to entity distribution, location distribution, keyword distribution and date distribution). The training objective of AEM is to let the distribution INLINEFORM4 (produced by INLINEFORM5 network) to approximate the real data distribution INLINEFORM6 as much as possible.
> 
> To compare the different GAN losses, Kurach kurach2018gan takes a sober view of the current state of GAN and suggests that the Jansen-Shannon divergence used in BIBREF3 performs more stable than variant objectives. Besides, Kurach also advocates that the gradient penalty (GP) regularization devised in BIBREF8 will further improve the stability of the model. Thus, the objective function of the proposed AEM is defined as: DISPLAYFORM0
> 
> where INLINEFORM0 denotes the discriminator loss, INLINEFORM1 represents the gradient penalty regularization loss, INLINEFORM2 is the gradient penalty coefficient which trade-off the two components of objective, INLINEFORM3 could be obtained by sampling uniformly along a straight line between INLINEFORM4 and INLINEFORM5 , INLINEFORM6 denotes the corresponding distribution.
> 
> The training procedure of AEM is presented in Algorithm SECREF15 , where INLINEFORM0 is the event number, INLINEFORM1 denotes the number of discriminator iterations per generator iteration, INLINEFORM2 is the batch size, INLINEFORM3 represents the learning rate, INLINEFORM4 and INLINEFORM5 are hyper-parameters of Adam BIBREF11 , INLINEFORM6 denotes INLINEFORM7 . In this paper, we set INLINEFORM8 , INLINEFORM9 , INLINEFORM10 . Moreover, INLINEFORM11 , INLINEFORM12 and INLINEFORM13 are set as 0.0002, 0.5 and 0.999.
> 
> [!h] Training procedure for AEM [1] INLINEFORM0 , INLINEFORM1 , INLINEFORM2 , INLINEFORM3 , INLINEFORM4 , INLINEFORM5 , INLINEFORM6 the trained INLINEFORM7 and INLINEFORM8 . Initial INLINEFORM9 parameters INLINEFORM10 and INLINEFORM11 parameter INLINEFORM12 INLINEFORM13 has not converged INLINEFORM14 INLINEFORM15 Sample INLINEFORM16 , Sample a random INLINEFORM17 Sample a random number INLINEFORM18 INLINEFORM19 INLINEFORM20 INLINEFORM21 INLINEFORM22 INLINEFORM23 INLINEFORM24 Sample INLINEFORM25 noise INLINEFORM26 INLINEFORM27

#### Relevance 594

Label: 

### Hybrid

#### Passage 595

Retrieved by: Hybrid

> Recently there has been much interest in event extraction from online texts, and approaches could be categorized as domain-specific and open-domain event extraction.
> 
> Domain-specific event extraction often focuses on the specific types of events (e.g. sports events or city events). Panem et al. panem2014structured devised a novel algorithm to extract attribute-value pairs and mapped them to manually generated schemes for extracting the natural disaster events. Similarly, to extract the city-traffic related event, Anantharam et al. anantharam2015extracting viewed the task as a sequential tagging problem and proposed an approach based on the conditional random fields. Zhang zhang2018event proposed an event extraction approach based on imitation learning, especially on inverse reinforcement learning.
> 
> Open-domain event extraction aims to extract events without limiting the specific types of events. To analyze individual messages and induce a canonical value for each event, Benson et al. benson2011event proposed an approach based on a structured graphical model. By representing an event with a binary tuple which is constituted by a named entity and a date, Ritter et al. ritter2012open employed some statistic to measure the strength of associations between a named entity and a date. The proposed system relies on a supervised labeler trained on annotated data. In BIBREF1 , Abdelhaq et al. developed a real-time event extraction system called EvenTweet, and each event is represented as a triple constituted by time, location and keywords. To extract more information, Wang el al. wang2015seeft developed a system employing the links in tweets and combing tweets with linked articles to identify events. Xia el al. xia2015new combined texts with the location information to detect the events with low spatial and temporal deviations. Zhou et al. zhou2014simple,zhou2017event represented event as a quadruple and proposed two Bayesian models to extract events from tweets.

#### Relevance 595

Label: 

## Question 0077

Paper: Sentiment Analysis of Code-Mixed Indian Languages: An Overview of SAIL_Code-Mixed Shared Task @ICON-2017

> what was the baseline?

### Common Retrieved Chunks

#### Passage 596

Retrieved by: BM25, Dense, Hybrid

> The baseline systems are developed by randomly assigning any of the sentiment values to each of the test instances. Then, similar evaluation techniques are applied to the baseline system and the results are presented in Table TABREF29 .

#### Relevance 596

Label: 

#### Passage 598

Retrieved by: BM25, Hybrid

> were automatically annotated with the help of different dictionaries whereas the sentiment tags were manually annotated. The submitted systems are ranked using the macro average f-score.
> 
> The paper is organized as following manner. Section SECREF2 describes the NLP in Indian languages mainly related to code-mixing and sentiment analysis. The detailed statistics of the dataset and evaluation are described in Section SECREF3 . The baseline systems and participant's system description are described in Section SECREF4 . Finally, conclusion and future research are drawn in Section SECREF5 .

#### Relevance 598

Label: 

#### Passage 599

Retrieved by: BM25, Dense, Hybrid

> This paper presents the details of shared task held during the ICON 2017. The competition presents the sentiment identification task from HI-EN and BN-EN code-mixed datasets. A random baseline system obtained macro average f-score of 0.331 and 0.339 for HI-EN and BN-EN datasets, respectively. The best performing team obtained maximum macro average f-score of 0.569 and 0.526 for HI-EN and BN-EN datasets, respectively. The team used word and character level n-grams as features and SVM for sentiment classification. We plan to enhance the current dataset and include more data pairs in the next version of the shared task. In future, more advanced task like aspect based sentiment analysis and stance detection can be performed on code-mixed dataset.

#### Relevance 599

Label: 

#### Passage 601

Retrieved by: Dense, Hybrid

> The baseline systems achieved better scores compared to CEN@AMRIT and SVNIT teams for HI-EN dataset; and AMRITA_CEN, CEN@Amrita and SVNIT teams for BN-EN dataset. IIIT-NBP team has achieved the maximum macro average f-score of 0.569 across all the sentiment classes for HI-EN dataset. IIIT-NBP also achieved the maximum macro average f-score of 0.526 for BN-EN dataset. Two way classification of HI-EN dataset achieved the maximum macro average f-score of 0.707, 0.666, and 0.663 for positive, negative, and neutral, respectively. Similarly, the two way classification of BN-EN dataset achieved the maximum average f-score of 0.641, 0.677, and 0.621 for positive, negative, and neutral, respectively. Again, the f-measure achieved using HI-EN dataset is better than BN-EN. The obvious reason for such result is that there are more instances in HI-EN than BN-EN dataset.
> 
> Most of the teams used the n-gram based features and it resulted in better macro average f-score. Most teams used the sklearn for identifying n-grams. IIITH-NBP team is only team to use character n-grams. Word embeddings is another important feature used by several teams. For word embeddings, Gensim and fastText are used. JU_KS team has used sentiment lexicon based features for BN-EN dataset only. BITMesra team has used emoji dictionary annotated with sentiment. Hashtags are considered to be one of the most important features for sentiment analysis BIBREF16 , however they removed hashtags during sentiment identification.
> 
> Apart from the features, most of the teams used machine learning algorithms like SVM, Naïve Bayes. It is observed that the deep learning models are quite successful for many NLP tasks. CFIL team have used the deep learning framework however the deep learning based system did not perform well as compared to machine learning based system. The main reason for the above may be that the training datasets provided are not sufficient to built a deep learning model.

#### Relevance 601

Label: 

#### Passage 603

Retrieved by: Dense, Hybrid

> This subsection describes the details of systems submitted for the shared task. Six teams have submitted their system details and those are described below in order of decreasing f-score.
> 
> IIIT-NBP team used features like GloVe word embeddings with 300 dimension and TF-IDF scores of word n-grams (one-gram, two-grams and tri-grams) as well as character n-grams (n varying from 2 to 6). Sklearn BIBREF15 package is used to calculate the TF-IDF. Finally, two classifiers: ensemble voting (consisting of three classifiers - linear SVM, logistic regression and random forests) and linear SVM are used for classification.
> 
> JU_KS team used n-gram and sentiment lexicon based features. Small sentiment lexicons are manually prepared for both English and Bengali words. However, no sentiment lexicon is used for Hindi language. Bengali sentiment lexicon consists of a collection of 1700 positive and 3750 negative words whereas English sentiment lexicon consists of 2006 positive and 4783 negative words. Finally, Naïve Bayes multinomial is used to classify and system results are presented in Table TABREF29 .
> 
> BIT Mesra team submitted systems for only HI-EN dataset. During preprocessing, they removed words having UN language tags, URLs, hashtags and user mentions. An Emoji dictionary was prepared with sentiment tags. Finally, they used SVM and Naïve Bayes classifiers on uni-gram and bi-gram features to classify sentiment of the code-mixed HI-EN dataset only.
> 
> NLP_CEN_AMRITA team have used different distributional and distributed representation. They used Document Term Matrix with N-gram varying from 1 to 5 for the representation and Support Vector Machines (SVM) as a classifier to make the final prediction. Their system performed well for n-grams range 5 and minimum document frequency 2 using the linear kernel.
> 
> CFIL team uses simple deep learning for sentiment analysis on code-mixed data. The fastText tool is used to create word embeddings on sentiment corpus. Additionally, Convolutional Neural Networks was used to extract sub-word features. Bi-LSTM layer is used on word embedding and sub-word features together with max-pooling at the output which is again sent to a softmax layer for prediction. No additional features are used and hyper-parameters are selected after dividing training corpus to 70% and 30%.
> 
> Subway team submitted systems for HI-EN dataset only. Initially, words other than HI and

#### Relevance 603

Label: 

### BM25

#### Passage 597

Retrieved by: BM25

> With the rise of social media and user-generated data, information extraction from user-generated text became an important research area. Social media has become the voice of many people over decades and it has special relations with real time events. The multilingual user have tendency to mix two or more languages while expressing their opinion in social media, this phenomenon leads to generate a new code-mixed language. So far, many studies have been conducted on why the code-mixing phenomena occurs and can be found in Kim kim2006reasons. Several experiments have been performed on social media texts including code-mixed data. The first step toward information gathering from these texts is to identify the languages present. Till date, several language identification experiments or tasks have been performed on several code-mixed language pairs such as Spanish-English BIBREF5 , BIBREF6 , French-English BIBREF7 , Hindi-English BIBREF0 , BIBREF1 , Hindi-English-Bengali BIBREF8 , Bengali-English BIBREF1 . Many shared tasks have also been organized for language identification of code-mixed texts. Language Identification in Code-Switched Data was one of the shared tasks which covered four language pairs such as Spanish-English, Modern Standard Arabic and Arabic dialects, Chinese-English, and Nepalese-English. In the case of Indian languages, Mixed Script Information Retrieval BIBREF9 shared task at FIRE-2015 was organized for eight code-mixed Indian languages such as Bangla, Gujarati, Hindi, Kannada, Malayalam, Marathi, Tamil, and Telugu mixed with English.
> 
> The second step is the identification of Part-of-Speech (POS) tags in code-mixed data and only handful of experiments have been performed in it such as Spanish-English BIBREF10 , Hindi-English BIBREF11 . POS Tagging for Code-mixed Indian Social Media shared task was organized for language pairs such as Bengali-English, Hindi-English, and Telugu-English. However, to best of the authors' knowledge no tasks on POS tagging were found on other code-mixed Indian languages. Again, Named Entity Recognition (NER) of code-mixed language shared task was organized for identifying named entities in Hindi-English and Tamil-English code-mixed data BIBREF12 .
> 
> Sentiment analysis or opinion mining from code-mixed data is one of the difficult tasks and the reasons are listed below.
> 
> Sentiment analysis of Hindi-English code-mixed was performed by Joshi et al. JoshiPSV16 which used sub-word level representations in LSTM architecture to perform it. This

#### Relevance 597

Label: 

#### Passage 600

Retrieved by: BM25

> mining from code-mixed data is one of the difficult tasks and the reasons are listed below.
> 
> Sentiment analysis of Hindi-English code-mixed was performed by Joshi et al. JoshiPSV16 which used sub-word level representations in LSTM architecture to perform it. This is one of the initial tasks in sentiment analysis of HI-EN code-mixed dataset. There are several applications on code-mixed data which depends on sentiment analysis such as stance detection, aspect based sentiment analysis. However, there are several tasks available on sentiment analysis of Indian language tweets BIBREF13 , BIBREF14 . The shared task on sentiment analysis in Indian languages (SAIL) tweets focused on sentiment analysis of three Indian languages: Bengali, Hindi, and Tamil BIBREF13 .

#### Relevance 600

Label: 

### Dense

#### Passage 602

Retrieved by: Dense

> This section describes statistics of the dataset and the evaluation procedure. Preparing a gold standard dataset is the first step towards achieving good accuracy. Several tasks in the field of NLP suffer from lack of gold standard dataset. In the case of Indian languages, there is no such code-mixed dataset available for research purpose. Thus, we developed the dataset and the details are provided below.

#### Relevance 602

Label: 

### Hybrid

None

## Question 0078

Paper: From English To Foreign Languages: Transferring Pre-trained Language Models

> What metrics are used for evaluation?

### Common Retrieved Chunks

#### Passage 605

Retrieved by: BM25, Dense, Hybrid

> All the RAMEN models are built from English and tuned on English for zero-shot cross-lingual tasks. It is reasonable to expect RAMENs do well in those tasks as we have shown in our experiments. But are they also a good feature extractor for supervised tasks? We offer a partial answer to this question by evaluating our model for supervised dependency parsing on UD datasets.
> 
> We used train/dev/test splits provided in UD to train and evaluate our RAMEN-based parser. Table TABREF38 summarizes the results (LAS) of our supervised parser. For a fair comparison, we choose mBERT as the baseline and all the RAMEN models are initialized from aligned fastText vectors. With the same architecture of 12 Transformer layers, RAMEN$_{\textsc {base}}$+BERT performs competitive to mBERT and outshines mBERT by +1.2 points for Vietnamese. The best LAS results are obtained by RAMEN$_{\textsc {large}}$+RoBERTa with 24 Transformer layers. Overall, our results indicate the potential of using contextual representations from RAMEN for supervised tasks.

#### Relevance 605

Label: 

#### Passage 606

Retrieved by: BM25, Hybrid

> In all the experiments, we tune RAMEN$_{\textsc {base}}$ for 175,000 updates and RAMEN$_{\textsc {large}}$ for 275,000 updates where the first 25,000 updates are for language specific parameters. The sequence length is set to 256. The mini-batch size are 64 and 24 when tuning language specific parameters using RAMEN$_{\textsc {base}}$ and RAMEN$_{\textsc {large}}$ respectively. For tuning bilingual LMs, we use a mini-batch size of 64 for RAMEN$_{\textsc {base}}$ and 24 for RAMEN$_{\textsc {large}}$ where half of the batch are English sequences and the other half are foreign sequences. This strategy of balancing mini-batch has been used in multilingual neural machine translation BIBREF23, BIBREF24.
> 
> We optimize RAMEN$_{\textsc {base}}$ using Lookahead optimizer BIBREF25 wrapped around Adam with the learning rate of $10^{-4}$, the number of fast weight updates $k=5$, and interpolation parameter $\alpha =0.5$. We choose Lookahead optimizer because it has been shown to be robust to the initial parameters of the based optimizer (Adam). For Adam optimizer, we linearly increase the learning rate from $10^{-7}$ to $10^{-4}$ in the first 4000 updates and then follow an inverse square root decay. All RAMEN$_{\textsc {large}}$ models are optimized with Adam due to memory limit.
> 
> When fine-tuning RAMEN on XNLI and UD, we use a mini-batch size of 32, Adam's learning rate of $10^{-5}$. The number of epochs are set to 4 and 50 for XNLI and UD tasks respectively. All experiments are carried out on a single Tesla V100 16GB GPU. Each RAMEN$_{\textsc {base}}$ model is trained within a day and each RAMEN$_{\textsc {large}}$ is trained within two days.

#### Relevance 606

Label: 

#### Passage 607

Retrieved by: BM25, Hybrid

> We build on top of RAMEN a graph-based dependency parser BIBREF27. For the purpose of evaluating the contextual representations learned by our model, we do not use part-of-speech tags. Contextualized representations are directly fed into Deep-Biaffine layers to predict arc and label scores. Table TABREF34 presents the Labeled Attachment Scores (LAS) for zero-shot dependency parsing.
> 
> We first look at the fairest comparison between mBERT and monolingually initialized RAMEN$_{\textsc {base}}$+BERT. The latter outperforms the former on five languages except Arabic. We observe the largest gain of +5.2 LAS for French. Chinese enjoys +3.1 LAS from our approach. With similar architecture (12 or 24 layers) and initialization (using monolingual or parallel data), RAMEN+RoBERTa performs better than RAMEN+BERT for most of the languages. Arabic and Hindi benefit the most from bigger models. For the other four languages, RAMEN$_{\textsc {large}}$ renders a modest improvement over RAMEN$_{\textsc {base}}$.

#### Relevance 607

Label: 

#### Passage 610

Retrieved by: Dense, Hybrid

> We evaluate our approach for six target languages: French (fr), Russian (ru), Arabic (ar), Chinese (zh), Hindi (hi), and Vietnamese (vi). These languages belong to four different language families. French, Russian, and Hindi are Indo-European languages, similar to English. Arabic, Chinese, and Vietnamese belong to Afro-Asiatic, Sino-Tibetan, and Austro-Asiatic family respectively. The choice of the six languages also reflects different training conditions depending on the amount of monolingual data. French and Russian, and Arabic can be regarded as high resource languages whereas Hindi has far less data and can be considered as low resource.
> 
> For experiments that use parallel data to initialize foreign specific parameters, we use the same datasets in the work of BIBREF6. Specifically, we use United Nations Parallel Corpus BIBREF18 for en-ru, en-ar, en-zh, and en-fr. We collect en-hi parallel data from IIT Bombay corpus BIBREF19 and en-vi data from OpenSubtitles 2018. For experiments that use only monolingual data to initialize foreign parameters, instead of training word-vectors from the scratch, we use the pre-trained word vectors from fastText BIBREF14 to estimate word translation probabilities (Eq. DISPLAY_FORM13). We align these vectors into a common space using orthogonal Procrustes BIBREF20, BIBREF15, BIBREF16. We only use identical words between the two languages as the supervised signal. We use WikiExtractor to extract extract raw sentences from Wikipedias as monolingual data for fine-tuning target embeddings and bilingual LMs (§SECREF15). We do not lowercase or remove accents in our data preprocessing pipeline.
> 
> We tokenize English using the provided tokenizer from pre-trained models. For target languages, we use fastBPE to learn 30,000 BPE codes and 50,000 codes when transferring from BERT and RoBERTa respectively. We truncate the BPE vocabulary of foreign languages to match the size of the English vocabulary in the source models. Precisely, the size of foreign vocabulary is set to 32,000 when transferring from BERT and 50,000 when transferring from RoBERTa.
> 
> We use XNLI dataset BIBREF9 for classification task and Universal Dependencies v2.4 BIBREF21 for parsing task. Since a language might have more than one treebank in Universal Dependencies, we use the following treebanks: en_ewt (English), fr_gsd (French), ru_syntagrus (Russian) ar_padt (Arabic), vi_vtb (Vietnamese), hi_hdtb (Hindi), and zh_gsd (Chinese).

#### Relevance 610

Label: 

#### Passage 611

Retrieved by: Dense, Hybrid

> We evaluate the performance of RAMEN+RoBERTa$_{\textsc {base}}$ (initialized from monolingual data) at each training steps: initialization of word embeddings (0K update), fine-tuning target embeddings (25K), and fine-tuning the model on both English and target language (at each 25K updates). The results are presented in Figure FIGREF40.
> 
> Without fine-tuning, the average accuracy of XLNI is 39.7% for a three-ways classification task, and the average LAS score is 3.6 for dependency parsing. We see the biggest leap in the performance after 50K updates. While semantic similarity task profits significantly at 25K updates of the target embeddings, syntactic task benefits with further fine-tuning the encoder. This is expected since the target languages might exhibit different syntactic structures than English and fine-tuning encoder helps to capture language specific structures. We observe a substantial gain of 19-30 LAS for all languages except French after 50K updates.
> 
> Language similarities have more impact on transferring syntax than semantics. Without tuning the English encoder, French enjoys 50.3 LAS for being closely related to English, whereas Arabic and Hindi, SOV languages, modestly reach 4.2 and 6.4 points using the SVO encoder. Although Chinese has SVO order, it is often seen as head-final while English is strong head-initial. Perhaps, this explains the poor performance for Chinese.

#### Relevance 611

Label: 

### BM25

#### Passage 604

Retrieved by: BM25

> We create a bilingual LM by plugging foreign language specific parameters to the pre-trained English LM (Figure FIGREF7). The new model has two separate embedding layers and output layers, one for English and one for foreign language. The encoder layer in between is shared. We then fine-tune this model using English and foreign monolingual data. Here, we keep tuning the model on English to ensure that it does not forget what it has learned in English and that we can use the resulting model for zero-shot transfer (§SECREF3). In this step, the encoder parameters are also updated so that in can learn syntactic aspects (i.e., word order, morphological agreement) of the target languages.

#### Relevance 604

Label: 

#### Passage 608

Retrieved by: BM25

> Pre-trained models BIBREF0, BIBREF1 have received much of attention recently thanks to their impressive results in many down stream NLP tasks. Additionally, multilingual pre-trained models enable many NLP applications for other languages via zero-short cross-lingual transfer. Zero-shot cross-lingual transfer has shown promising results for rapidly building applications for low resource languages. BIBREF2 show the potential of multilingual-BERT BIBREF0 in zero-shot transfer for a large number of languages from different language families on five NLP tasks, namely, natural language inference, document classification, named entity recognition, part-of-speech tagging, and dependency parsing.
> 
> Although multilingual models are an important ingredient for enhancing language technology in many languages, recent research on improving pre-trained models puts much emphasis on English BIBREF3, BIBREF4, BIBREF5. The current state of affairs makes it difficult to translate advancements in pre-training from English to non-English languages. To our best knowledge, there are only three available multilingual pre-trained models to date: (1) the multilingual-BERT (mBERT) that supports 104 languages, (2) cross-lingual language model BIBREF6 that supports 100 languages, and (3) Language Agnostic SEntence Representations BIBREF7 that supports 93 languages. Among the three models, LASER is based on neural machine translation approach and strictly requires parallel data to train.
> 
> Do multilingual models always need to be trained from scratch? Can we transfer linguistic knowledge learned by English pre-trained models to other languages? In this work, we develop a technique to rapidly transfer an existing pre-trained model from English to other languages in an energy efficient way BIBREF8. As the first step, we focus on building a bilingual language model (LM) of English and a target language. Starting from a pre-trained English LM, we learn the target language specific parameters (i.e., word embeddings), while keeping the encoder layers of the pre-trained English LM fixed. We then fine-tune both English and target model to obtain the bilingual LM. We apply our approach to autoencoding language models with masked language model objective and show the advantage of the proposed approach in zero-shot transfer. Our main contributions in this work are:
> 
> We propose a fast adaptation method for obtaining a bilingual BERT$_{\textsc {base}}$ of English and a target language within a day using one Tesla V100 16GB GPU.
> 
> We evaluate our bilingual

#### Relevance 608

Label: 

### Dense

#### Passage 609

Retrieved by: Dense

> Table TABREF32 shows the XNLI test accuracy. For reference, we also include the scores from the previous work, notably the state-of-the-art system XLM BIBREF6. Before discussing the results, we spell out that the fairest comparison in this experiment is the comparison between mBERT and RAMEN$_{\textsc {base}}$+BERT trained with monolingual only.
> 
> We first discuss the transfer results from BERT. Initialized from fastText vectors, RAMEN$_{\textsc {base}}$ slightly outperforms mBERT by 1.9 points on average and widen the gap of 3.3 points on Arabic. RAMEN$_{\textsc {base}}$ gains extra 0.8 points on average when initialized from parallel data. With triple number of parameters, RAMEN$_{\textsc {large}}$ offers an additional boost in term of accuracy and initialization with parallel data consistently improves the performance. It has been shown that BERT$_{\textsc {large}}$ significantly outperforms BERT$_{\textsc {base}}$ on 11 English NLP tasks BIBREF0, the strength of BERT$_{\textsc {large}}$ also shows up when adapted to foreign languages.
> 
> Transferring from RoBERTa leads to better zero-shot accuracies. With the same initializing condition, RAMEN$_{\textsc {base}}$+RoBERTa outperforms RAMEN$_{\textsc {base}}$+BERT on average by 2.9 and 2.3 points when initializing from monolingual and parallel data respectively. This result show that with similar number of parameters, our approach benefits from a better English pre-trained model. When transferring from RoBERTa$_{\textsc {large}}$, we obtain state-of-the-art results for five languages.
> 
> Currently, RAMEN only uses parallel data to initialize foreign embeddings. RAMEN can also exploit parallel data through translation objective proposed in XLM. We believe that by utilizing parallel data during the fine-tuning of RAMEN would bring additional benefits for zero-shot tasks. We leave this exploration to future work. In summary, starting from BERT$_{\textsc {base}}$, our approach obtains competitive bilingual LMs with mBERT for zero-shot XNLI. Our approach shows the accuracy gains when adapting from a better pre-trained model.

#### Relevance 609

Label: 

#### Passage 612

Retrieved by: Dense

> Since pre-trained models operate on subword level, we need to estimate subword translation probabilities. Therefore, we subsample 2M sentence pairs from each parallel corpus and tokenize the data into subwords before running fast-align BIBREF13.
> 
> Estimating subword translation probabilities from aligned word vectors requires an additional processing step since the provided vectors from fastText are not at subword level. We use the following approximation to obtain subword vectors: the vector $_s$ of subword $s$ is the weighted average of all the aligned word vectors $_{w_i}$ that have $s$ as an subword
> 
> where $p(w_j)$ is the unigram probability of word $w_j$ and $n_s = \sum _{w_j:\, s\in w_j} p(w_j)$. We take the top 50,000 words in each aligned word-vectors to compute subword vectors.
> 
> In both cases, not all the words in the foreign vocabulary can be initialized from the English word-embeddings. Those words are initialized randomly from a Gaussian $\mathcal {N}(0, {1}{d^2})$.

#### Relevance 612

Label: 

### Hybrid

None

## Question 0079

Paper: Using General Adversarial Networks for Marketing: A Case Study of Airbnb

> What are the user-defined keywords?

### Common Retrieved Chunks

#### Passage 613

Retrieved by: BM25, Dense, Hybrid

> the real ground-truth of each data point.
> 
> The general framework defined above was inspired largely by the open-source code of Nag Dev, and was built using Pytorch [7]. One key extension to the basic GAN model, however, is the loss function that we apply to the generator, namely the Diehl-Martinez-Kamalu (DMK) Loss which we define below.
> 
> The Diehl-Martinez-Kamalu Loss is a weighted combination of a binary cross entropy loss with a dot-product attention metric of each user-defined keyword with the model’s generated output. Formally, the binary cross entropy (BCE) loss for one example is defined as: $ BCE(x,y) = y \cdot logx + (1-y) \cdot log(1-x), $
> 
> where x is defined as the predicted label for each sample and y is the true label (i.e. real versus fake data). The DMK loss then calculates an additional term, which corresponds to the dot-product attention of each word in the generated output with each keyword specified by the user. To illustrate by example, say a user desires the generated output to contain the keywords, $\lbrace subway, manhattan\rbrace $ . The model then converts each of these keywords to their corresponding glove vectors. Let us define the following notation $e(‘apple’)$ is the GloVe representation of the word apple, and let us suppose that $g$ is the vector of word embeddings generated by the generator. That is, $g_1$ is the first word embedding of the generator’s output. Let us also suppose $k$ is a vector of the keywords specified by the user. In our examples, $k$ is always in $R^{1}$ with $k_1$ one equaling of $‘subway’$ or $‘parking’$ . The dot-product term of the DMK loss then calculates $e(‘apple’)$0 . Weighing this term by some hyper-parameter, $e(‘apple’)$1 , then gives us the entire definition of the DMK loss: $e(‘apple’)$2 $e(‘apple’)$3

#### Relevance 613

Label: 

#### Passage 614

Retrieved by: BM25, Dense, Hybrid

> tuning the model’s parameters.
> 
> Nonetheless, GANs have continued to show their value particularly in the domain of text-generation. Of particular interest for our purposes, Radford et al. propose synthesizing images from text descriptions [3]. The group demonstrates how GANs can produce images that correspond to a user-defined text description. It thus seems feasible that by using a similar model, we can produce text samples that are conditioned upon a set of user-specified keywords.
> 
> We were similarly influenced by the work of Radford et. al, who argue for the importance of layer normalization and data-specific trained word embeddings for text generation [9] and sentiment analysis categorization. These findings lead us to question whether it is possible to employ recurrent neural networks with long short-term memory gates, as defined by Mikolov et al., to categorize product descriptions into categories based on the product's popularity [6].

#### Relevance 614

Label: 

#### Passage 615

Retrieved by: BM25, Dense, Hybrid

> of clean data. With over 40,000 listings, we did not expect to see such poor attention to orthography in what are essentially public advertisements of the properties. In this way, our decision to use a window size of 5, a minimum occurrence count of 2, and a dimensionality of 50 when training our GloVe vectors was ad hoc.
> 
> Seeking to create a model which could generate and discriminate a “high-occupancy listing description”, we wanted to evaluate the capabilities of a generative adversarial network trained on either the standard binary cross-entropy loss or the DMK loss proposed above. Common to both models was the decision to alternate between training the generator for 50 steps and the discriminator for 2000 steps. We leave further tuning of the models to future research as each occasionally falls into unideal local optima within 20 iterations. One potential culprit is the step imbalance between generator and discriminator – should either learn at a much faster rate than the other, one component is liable to be “defeated" and cease to learn the training data.
> 
> Qualitatively the network trained on the DMK loss shows great promise. With respect to the two experiments presented here, we have shown that it is possible to introduce a measure of suggestion in the text produced by the generator. While this model is also subject to a rapid deadlock between generator and discriminator, it is interesting to see how the introduction of keywords is gradual and affects the proximal tokens included in the output. This behavior was made possible by paying close attention to the hyperparameter $\gamma $ , the weight given to the dot product attention term of the DMK loss. After manual tuning, we settle on $\gamma =0.00045$ for this weight. Below, we illustrate model outputs using different values of Gamma. As is apparent, for a hyper-parameter value less than roughly $\gamma = 0.0004$ , the model tends to ignore the importance of the keyword weights. Conversely, with a $\gamma $ value higher than $0.0005$ , the model tends towards overweighting the representation of the keywords in the model output.

#### Relevance 615

Label: 

#### Passage 616

Retrieved by: BM25, Dense, Hybrid

> In seeking to answer the question of whether the occupancy rate of a listing could be extracted from the listing’s summary, we ran a number of experiments on our first model. Two parameterizations which we present here are (1) whether the word vectors used in the embedding layer are trained on our corpus or come pretrained from Wikipedia and Gigaword and (2) whether ensembling or the final hidden state in isolation are used to make a prediction for the sequence. Common to all experiments was our decision to use an Adam optimizer, 16 LSTM units, 50-dimensional GloVe vectors, and a 70-30 split in train and test data.
> 
> Over ten epochs, the model parameterization which performs the best uses GloVe vectors trained on a corpus consisting of all listing descriptions and ensembling to make its class prediction. As a result, our findings are well in-line with those presented by Radford et. al who underscore the importance of training word embeddings on a data-specific corpus for best results on generative tasks [9].
> 
> That said, these results, though they do show a marginal increase in dev accuracy and a decrease in CE loss, suggest that perhaps listing description is not too predictive of occupancy rate given our parameterizations. While the listing description is surely an influential metric in determining the quality of a listing, other factors such as location, amenities, and home type might play a larger role in the consumer's decision. We were hopeful that these factors would be represented in the price per bedroom of the listing – our control variable – but the relationship may not have been strong enough.
> 
> However, should a strong relationship actually exist and there be instead a problem with our method, there are a few possibilities of what went wrong. We assumed that listings with similar occupancy rates would have similar listing descriptions regardless of price, which is not necessarily a strong assumption. This is coupled with an unexpected sparseness of clean data. With over 40,000 listings, we did not expect to see such poor attention to orthography in what are essentially public advertisements of the properties. In this way, our decision to use a window size of 5, a

#### Relevance 616

Label: 

#### Passage 618

Retrieved by: Dense, Hybrid

> Prior to building our generative model, we sought to gain a better understanding of how less and more popular listing descriptions differed in their writing style. We defined a home’s popularity via its occupancy rate metric, which we describe in the Data section. Using this popularity heuristic, we first stratified our dataset into groupings of listings at similar price points (i.e. $0-$30, $30-$60, ...). Importantly, rather than using the home’s quoted price, we relied on the price per bedroom as a better metric for the cost of the listing. Having clustered our listings into these groupings, we then selected the top third of listings by occupancy rate, as part of the ‘high popularity’ group. Listings in the middle and lowest thirds by occupancy rate were labeled ‘medium popularity’ and ‘low popularity’ respectively. We then combined all of the listings with high/medium/low popularity together for our final data set.

#### Relevance 618

Label: 

### BM25

#### Passage 617

Retrieved by: BM25

> Fortunately, we believe that the introduction of unsupervised generative language models presents a way in which to tackle this particular shortcoming of peer-to-peer markets. In 2014, Ian Goodfellow et. al proposed the general adversarial network (GAN) [5]. The group showcased how this generative model could learn to artificially replicate data patterns to an unprecedented realistic degree [5]. Since then, these models have shown tremendous potential in their ability to generate photo-realistic images and coherent text samples [5].
> 
> The framework that GANs use for generating new data points employs an end-to-end neural network comprised of two models: a generator and a discriminator [5]. The generator is tasked with replicating the data that is fed into the model, without ever being directly exposed to the real samples. Instead, this model learns to reproduce the general patterns of the input via its interaction with the discriminator.
> 
> The role of the discriminator, in turn, is to tell apart which data points are ‘real’ and which have been created by the generator. On each run through the model, the generator then adapts its constructed output so as to more effectively ‘trick’ the discriminator into not being able to distinguish the real from the generated data. The end-to-end nature of the model then forces both the generator and discriminator to learn in parallel [7]. While GAN models have shown great potential in their ability to generate realistic data samples, they are notoriously difficult to train. This difficulty arises from two-parts: 1) First, it is difficult to tune the hyper-parameters correctly for the adversarial model to continue learning throughout all of the training epochs [5]. Since both the discriminator and generator are updated via the same gradient, it is very common for the model to fall into a local minima before completing all of the defined training cycles. 2) GANs are computationally expensive to train, given that both models are updated on each cycle in parallel [5]. This compounds the difficulty of tuning the model’s parameters.
> 
> Nonetheless, GANs have continued to show their value particularly in the domain of text-generation. Of particular interest for our purposes, Radford et al. propose synthesizing images from text descriptions [3]. The group demonstrates how GANs can

#### Relevance 617

Label: 

### Dense

None

### Hybrid

None

## Question 0080

Paper: A Neural Approach to Irony Generation

> How did the authors find ironic data on twitter?

### Common Retrieved Chunks

#### Passage 619

Retrieved by: BM25, Hybrid

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

#### Relevance 619

Label: 

#### Passage 620

Retrieved by: BM25, Dense, Hybrid

> specifically designed model based on unsupervised style transfer to explore irony generation.
> 
> In this paper, in order to address the lack of irony data, we first crawl over 2M tweets from twitter to build a dataset with 262,755 ironic and 112,330 non-ironic tweets. Then, due to the lack of parallel data, we propose a novel model to transfer non-ironic sentences to ironic sentences in an unsupervised way. As ironic style is hard to model and describe, we implement our model with the control of classifiers and reinforcement learning. Different from other studies in style transfer, the transformation from non-ironic to ironic sentences has to preserve sentiment polarity as mentioned above. Therefore, we not only design an irony reward to control the irony accuracy and implement denoising auto-encoder and back-translation to control content preservation but also design a sentiment reward to control sentiment preservation.
> 
> Experimental results demonstrate that our model achieves a high irony accuracy with well-preserved sentiment and content. The contributions of our work are as follows:

#### Relevance 620

Label: 

#### Passage 622

Retrieved by: BM25, Dense, Hybrid

> In this paper, we first systematically define irony generation based on style transfer. Because of the lack of irony data, we make use of twitter and build a large-scale dataset. In order to control irony accuracy, sentiment preservation and content preservation at the same time, we also design a combination of rewards for reinforcement learning and incorporate reinforcement learning with a pre-training process. Experimental results demonstrate that our model outperforms other generative models and our rewards are effective. Although our model design is effective, there are still many errors and we systematically analyze them. In the future, we are interested in exploring these directions and our work may extend to other kinds of ironies which are more difficult to model.

#### Relevance 622

Label: 

#### Passage 623

Retrieved by: BM25, Dense, Hybrid

> be ignored". Although there is “love" in the generated sentence, the speaker still expresses his or her negative sentiment by irony. We also make some explorations in the transformation from ironic sentences to non-ironic sentences at the end of our work. Because of the lack of previous work and baselines on irony generation, we implement our model based on style transfer. Our work will not only provide the first large-scale irony dataset but also make our model as a benchmark for the irony generation.
> 
> Recently, unsupervised style transfer becomes a very popular topic. Many state-of-the-art studies try to solve the task with sequence-to-sequence (seq2seq) framework. There are three main ways to build up models. The first is to learn a latent style-independent content representation and generate sentences with the content representation and another style BIBREF6 , BIBREF7 . The second is to directly transfer sentences from one style to another under the control of classifiers and reinforcement learning BIBREF8 . The third is to remove style attribute words from the input sentence and combine the remaining content with new style attribute words BIBREF9 , BIBREF10 . The first method usually obtains better performances via adversarial training with discriminators. The style-independent content representation, nevertheless, is not easily obtained BIBREF11 , which results in poor performances. The second method is suitable for complex styles which are difficult to model and describe. The model can learn the deep semantic features by itself but sometimes the model is sensitive to parameters and hard to train. The third method succeeds to preserve content but cannot work for some complex styles such as democratic and republican. Sentences with those styles usually do not have specific style attribute words. Unfortunately, due to the lack of large irony dataset and difficulties of modeling ironies, there has been little work trying to generate ironies based on seq2seq framework as far as we know. Inspired by methods for style transfer, we decide to implement a specifically designed model based on unsupervised style transfer to explore irony generation.
> 
> In this paper, in order to address the lack of irony data, we first crawl over 2M tweets from twitter to build a dataset with 262,755 ironic and

#### Relevance 623

Label: 

#### Passage 624

Retrieved by: Dense, Hybrid

> In this section, we describe how we build our dataset with tweets. First, we crawl over 2M tweets from twitter using GetOldTweets-python. We crawl English tweets from 04/09/2012 to /12/18/2018. We first remove all re-tweets and use langdetect to remove all non-English sentences. Then, we remove hashtags attached at the end of the tweets because they are usually not parts of sentences and will confuse our language model. After that, we utilize Ekphrasis to process tweets. We remove URLs and restore remaining hashtags, elongated words, repeated words, and all-capitalized words. To simplify our dataset, We replace all “ INLINEFORM0 money INLINEFORM1 " and “ INLINEFORM2 time INLINEFORM3 " tokens with “ INLINEFORM4 number INLINEFORM5 " token when using Ekphrasis. And we delete sentences whose lengths are less than 10 or greater than 40. In order to restore abbreviations, we download an abbreviation dictionary from webopedia and restore abbreviations to normal words or phrases according to the dictionary. Finally, we remove sentences which have more than two rare words (appearing less than three times) in order to constrain the size of vocabulary. Finally, we get 662,530 sentences after pre-processing.
> 
> As neural networks are proved effective in irony detection, we decide to implement a neural classifier in order to classify the sentences into ironic and non-ironic sentences. However, the only high-quality irony dataset we can obtain is the dataset of Semeval-2018 Task 3 and the dataset is pretty small, which will cause overfitting to complex models. Therefore, we just implement a simple one-layer RNN with LSTM cell to classify pre-processed sentences into ironic sentences and non-ironic sentences because LSTM networks are widely used in irony detection. We train the model with the dataset of Semeval-2018 Task 3. After classification, we get 262,755 ironic sentences and 399,775 non-ironic sentences. According to our observation, not all non-ironic sentences are suitable to be transferred into ironic sentences. For example, “just hanging out . watching . is it monday yet" is hard to transfer because it does not have an explicit sentiment polarity. So we remove all interrogative sentences from the non-ironic sentences and only obtain the sentences which have words expressing strong sentiments. We evaluate the sentiment polarity of each

#### Relevance 624

Label: 

### BM25

#### Passage 621

Retrieved by: BM25

> to implement.
> 
> When it comes to methods based on neural networks, long short-term memory (LSTM) BIBREF15 network is widely used and is very efficient for irony detection. In BIBREF16 , a tweet is divided into two segments and a subtract layer is implemented to calculate the difference between two segments in order to determine whether the tweet is ironic. In BIBREF17 , authors utilize a recurrent neural network with Bi-LSTM and self-attention without hand-crafted features. In BIBREF18 , researchers propose a system based on a densely connected LSTM network.

#### Relevance 621

Label: 

### Dense

#### Passage 625

Retrieved by: Dense

> The irony is a kind of figurative language, which is widely used on social media BIBREF0 . The irony is defined as a clash between the intended meaning of a sentence and its literal meaning BIBREF1 . As an important aspect of language, irony plays an essential role in sentiment analysis BIBREF2 , BIBREF0 and opinion mining BIBREF3 , BIBREF4 .
> 
> Although some previous studies focus on irony detection, little attention is paid to irony generation. As ironies can strengthen sentiments and express stronger emotions, we mainly focus on generating ironic sentences. Given a non-ironic sentence, we implement a neural network to transfer it to an ironic sentence and constrain the sentiment polarity of the two sentences to be the same. For example, the input is “I hate it when my plans get ruined" which is negative in sentiment polarity and the output should be ironic and negative in sentiment as well, such as “I like it when my plans get ruined". The speaker uses “like" to be ironic and express his or her negative sentiment. At the same time, our model can preserve contents which are irrelevant to sentiment polarity and irony. According to the categories mentioned in BIBREF5 , irony can be classified into 3 classes: verbal irony by means of a polarity contrast, the sentences containing expression whose polarity is inverted between the intended and the literal evaluation; other types of verbal irony, the sentences that show no polarity contrast between the literal and intended meaning but are still ironic; and situational irony, the sentences that describe situations that fail to meet some expectations. As ironies in the latter two categories are obscure and hard to understand, we decide to only focus on ironies in the first category in this work. For example, our work can be specifically described as: given a sentence “I hate to be ignored", we train our model to generate an ironic sentence such as “I love to be ignored". Although there is “love" in the generated sentence, the speaker still expresses his or her negative sentiment by irony. We also make some explorations in the transformation from ironic sentences to non-ironic sentences at the end of our

#### Relevance 625

Label: 

### Hybrid

None
