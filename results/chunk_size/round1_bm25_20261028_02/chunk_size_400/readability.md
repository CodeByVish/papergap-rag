# Readability Review

## Source sample: 1

### Source text

Paper: 1708.08615; section: 0; paragraphs: [2]; character span: 0:747 (within sampled paragraph).

Original section context:

```text
Automatic speech recognition (ASR) systems have seen remarkable advances over the last half-decade from the use of deep, convolutional and recurrent neural network architectures, enabled by a combination of modeling advances, available training data, and increased computational resources. Given these advances, our research group recently embarked on an effort to reach human-level transcription accuracy using state-of-the-art ASR techniques on one of the genres of speech that has historically served as a difficult benchmark task: conversational telephone speech (CTS). About a decade ago, CTS recognition had served as an evaluation task for government-sponsored work in speech recognition, predating the take-over of deep learning approaches and still largely in the GMM-HMM modeling framework BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 . It had proven to be a hard problem, due to the variable nature of conversational pronunciations, speaking styles, and regional accents. Seide at al. BIBREF6 demonstrated that deep networks as acoustic models could achieve significant improvements over GMM-HMM models on CTS data, and more recently researchers at IBM had achieved results on this task that represented a further significant advance BIBREF7 , BIBREF8 over those from a decade ago.

The goal of reaching “human parity” in automatic CTS transcription raises the question of what should be considered human accuracy on this task. We operationalized the question by submitting the chosen test data to the same vendor-based transcription pipeline that is used at Microsoft for production data (for model training and internal evaluation purposes), and then comparing the results to ASR system output under the NIST scoring protocol. Using this methodology, and incorporating state-of-the-art convolutional and recurrent network architectures for both acoustic modeling BIBREF9 , BIBREF10 , BIBREF7 , BIBREF11 , BIBREF12 , BIBREF13 , BIBREF14 and language modeling BIBREF15 , BIBREF16 , BIBREF17 , BIBREF18 with extensive use of model combination, we obtained a machine error rate that was very slightly below that of the human transcription process (5.8% versus 5.9% on Switchboard data, and 11.0% versus 11.3% on CallHome English data) BIBREF19 . Since then, Saon et al. have reported even better results, along with a separate transcription experiment that puts the human error rate, on the same test data, at a lower point than measured by us (5.1% for Switchboard, 6.8% for CallHome) BIBREF20 .

In this paper, we address the question whether there are major qualitative differences between the results of human transcriptions of conversational speech and those obtained by ASR systems, based on a detailed analysis of the data and system output from our human parity experiment BIBREF19 . The question becomes important if ASR is to replace humans as the first step in fully automatic speech understanding systems—if machine transcription errors are qualitatively different from humans then we would have to worry about the possible effects on downstream processing, and mitigation techniques so as to still achieve an overall “natural” user experience (e.g., in real-time conversational speech translation, such as in the Skype application).

We start by discussing why human error rate on this task must themselves be considered a moving target. Next we ask whether speech that is difficult for ASR also tends to be hard for humans to transcribe (and vice-versa), and whether the speaker overlap with the training data that is found in a portion of the test data has a noticeable effect on the result, as was suggested in BIBREF20 . We then look at the most frequent word error types exhibited by the two transcription systems (human and machine), and finally report on a very preliminary but still informative experiment to see if humans could tell apart the transcription source (again, human versus machine), based on the errors they make.
```

### Chunks (ID and text)

Passage ID: `qasper-passage-v1-dd5f5e46b52e58cfd87906c2f54e2c70cb9e5f9eb8e004ef726490f2a850ff62`

```text
Automatic speech recognition (ASR) systems have seen remarkable advances over the last half-decade from the use of deep, convolutional and recurrent neural network architectures, enabled by a combination of modeling advances, available training data, and increased computational resources. Given these advances, our research group recently embarked on an effort to reach human-level transcription accuracy using state-of-the-art ASR techniques on one of the genres of speech that has historically served as a difficult benchmark task: conversational telephone speech (CTS). About a decade ago, CTS recognition had served as an evaluation task for government-sponsored work in speech recognition, predating the take-over of deep learning approaches and still largely in the GMM-HMM modeling framework BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 , BIBREF4 , BIBREF5 . It had proven to be a hard problem, due to the variable nature of conversational pronunciations, speaking styles, and regional accents. Seide at al. BIBREF6 demonstrated that deep networks as acoustic models could achieve significant improvements over GMM-HMM models on CTS data, and more recently researchers at IBM had achieved results on this task that represented a further significant advance BIBREF7 , BIBREF8 over those from a decade ago.

The goal of reaching “human parity” in automatic CTS transcription raises the question of what should be considered human accuracy on this task. We operationalized the question by submitting the chosen test data to the same vendor-based transcription pipeline that is used at Microsoft for production data (for model training and internal evaluation purposes), and then comparing the results to ASR system output under the NIST scoring protocol. Using this methodology, and incorporating state-of-the-art convolutional and recurrent network architectures for both acoustic modeling BIBREF9 , BIBREF10 , BIBREF7 , BIBREF11 , BIBREF12 , BIBREF13 , BIBREF14 and language modeling BIBREF15 , BIBREF16 , BIBREF17 , BIBREF18 with extensive use of model combination, we obtained a machine error rate that was very slightly below that of the human transcription process (5.8% versus 5.9% on Switchboard data, and 11.0% versus 11.3% on CallHome English data) BIBREF19 . Since then, Saon et al. have reported even better results, along with a separate transcription experiment that puts the human error rate, on the same test data, at a lower point than measured by us (5.1% for Switchboard, 6.8% for CallHome) BIBREF20 .

In this paper, we address the question whether there are major qualitative differences between the results of human transcriptions of
```

Passage ID: `qasper-passage-v1-3d3901e9f732265198344f0db7d5bafc23d85923163e8a25b10300d7d9fee09f`

```text
the same test data, at a lower point than measured by us (5.1% for Switchboard, 6.8% for CallHome) BIBREF20 .

In this paper, we address the question whether there are major qualitative differences between the results of human transcriptions of conversational speech and those obtained by ASR systems, based on a detailed analysis of the data and system output from our human parity experiment BIBREF19 . The question becomes important if ASR is to replace humans as the first step in fully automatic speech understanding systems—if machine transcription errors are qualitatively different from humans then we would have to worry about the possible effects on downstream processing, and mitigation techniques so as to still achieve an overall “natural” user experience (e.g., in real-time conversational speech translation, such as in the Skype application).

We start by discussing why human error rate on this task must themselves be considered a moving target. Next we ask whether speech that is difficult for ASR also tends to be hard for humans to transcribe (and vice-versa), and whether the speaker overlap with the training data that is found in a portion of the test data has a noticeable effect on the result, as was suggested in BIBREF20 . We then look at the most frequent word error types exhibited by the two transcription systems (human and machine), and finally report on a very preliminary but still informative experiment to see if humans could tell apart the transcription source (again, human versus machine), based on the errors they make.
```

### Evaluation results

| Passage ID | Result | Reason |
| --- | --- | --- |
| `qasper-passage-v1-dd5f5e46b52e58cfd87906c2f54e2c70cb9e5f9eb8e004ef726490f2a850ff62` | pending | |
| `qasper-passage-v1-3d3901e9f732265198344f0db7d5bafc23d85923163e8a25b10300d7d9fee09f` | pending | |

## Source sample: 2

### Source text

Paper: 1708.08615; section: 3; paragraphs: [1]; character span: 0:319 (within sampled paragraph).

Original section context:

```text
We note in passing that machine and human transcription WERs do not differ significantly according the Wilcoxon and Matched Pairs Sentence Segment Word Error tests as applied by NIST, nor do they differ according to a Sign test comparing error counts at the utterance level.

A first high-level question regarding the relation between word errors by machine and human transcribers is whether difficulty in one predicts difficulty in the other. Figure FIGREF1 shows scatter plots of speaker-level error rates (machine vs. human), separated by corpus. Each corpus subset has 40 conversation sides.

Clearly the errors at that level are correlated, with INLINEFORM0 for SWB and INLINEFORM1 for CH. This suggests that properties of the speech, either as a function of the content, the speaker, or the channel (each speaker occurs in exactly one test conversation), cause errors for both machine and human transcription.

We observe that the CH data has two speakers with outlier machine error rates (37.5% and 64.7% WER, solid red dots in Figure FIGREF1 ). These correspond to secondary speakers in their respective conversation sides, each with only a fraction of the speech of the dominant speaker. Note that the ASR system processes each conversation assuming only a single speaker per side. If we remove these outliers, the machine-human error correlation on CH increases to INLINEFORM0 . With secondary speakers excluded, we can also observe that the machine error rates cluster tighter than the human ones in both corpora (SWB: machine INLINEFORM1 vs. human INLINEFORM2 ; CH: machine INLINEFORM3 vs. human INLINEFORM4 ).

In BIBREF20 it was sugggested that one of the reasons for the much higher error rate on CH compared to SWB was that 36 of the 40 SWB test speakers occur in the portion of the SWB corpus that is used in training (due to what we surmise to be an oversight in the selection of the NIST 2000 test set). To assess this hypothesis we singled out the four speakers in the SWB portion that are not found in the training set; these are shown as solid black circles in Figure FIGREF1 . At first, it seems that the speaker-averaged WER for the “seen” speakers (machine WER 5.9%) is indeed much lower than for the speakers not found in training (7.5%). However, we can safely attribute this to bad luck and small sample size. The average machine WER of 7.5% for “unseen” speakers is well within one standard deviation of the “seen” speakers' WER distribution ( INLINEFORM0 ), and more tellingly, almost exactly the same relative difference in WERs between “seen” and “unseen” speakers is observed for human transcriptions (6.0% versus 7.7%). Clearly the human transcribers did not have the benefit of training on the “seen” speakers, so the difference must be due to the intrinsic difficulty of the speakers, which affects both transcription systems.
```

### Chunks (ID and text)

Passage ID: `qasper-passage-v1-0d41563b175aa927989c9f261deb2814142c969bf488b1192b39cada17e93894`

```text
We note in passing that machine and human transcription WERs do not differ significantly according the Wilcoxon and Matched Pairs Sentence Segment Word Error tests as applied by NIST, nor do they differ according to a Sign test comparing error counts at the utterance level.

A first high-level question regarding the relation between word errors by machine and human transcribers is whether difficulty in one predicts difficulty in the other. Figure FIGREF1 shows scatter plots of speaker-level error rates (machine vs. human), separated by corpus. Each corpus subset has 40 conversation sides.

Clearly the errors at that level are correlated, with INLINEFORM0 for SWB and INLINEFORM1 for CH. This suggests that properties of the speech, either as a function of the content, the speaker, or the channel (each speaker occurs in exactly one test conversation), cause errors for both machine and human transcription.

We observe that the CH data has two speakers with outlier machine error rates (37.5% and 64.7% WER, solid red dots in Figure FIGREF1 ). These correspond to secondary speakers in their respective conversation sides, each with only a fraction of the speech of the dominant speaker. Note that the ASR system processes each conversation assuming only a single speaker per side. If we remove these outliers, the machine-human error correlation on CH increases to INLINEFORM0 . With secondary speakers excluded, we can also observe that the machine error rates cluster tighter than the human ones in both corpora (SWB: machine INLINEFORM1 vs. human INLINEFORM2 ; CH: machine INLINEFORM3 vs. human INLINEFORM4 ).

In BIBREF20 it was sugggested that one of the reasons for the much higher error rate on CH compared to SWB was that 36 of the 40 SWB test speakers occur in the portion of the SWB corpus that is used in training (due to what we surmise to be an oversight in the selection of the NIST 2000 test set). To assess this hypothesis we singled out the four speakers in the SWB portion that are not found in the training set; these are shown as solid black circles in Figure FIGREF1 . At first, it seems that the speaker-averaged WER for the “seen” speakers (machine WER 5.9%) is indeed much lower than for the speakers not found in training (7.5%). However, we can safely attribute this to bad luck and small sample size. The average machine WER of 7.5% for “unseen” speakers
```

### Evaluation results

| Passage ID | Result | Reason |
| --- | --- | --- |
| `qasper-passage-v1-0d41563b175aa927989c9f261deb2814142c969bf488b1192b39cada17e93894` | pending | |

## Source sample: 3

### Source text

Paper: 1606.05320; section: 3; paragraphs: [4]; character span: 0:18 (within sampled paragraph).

Original section context:

```text
The HMM training procedure is as follows:

Initialization of HMM hidden states:

(Discrete HMM) Random multinomial draw for each time step (i.i.d. across time steps).

(Continuous HMM) K-means clusters fit on LSTM states, to speed up convergence relative to random initialization.

At each iteration:

Sample states using Forward Filtering Backwards Sampling algorithm (FFBS, BIBREF7 ).

Sample transition parameters from a Multinomial-Dirichlet posterior. Let $n_{ij}$ be the number of transitions from state $i$ to state $j$ . Then the posterior distribution of the $i$ -th row of transition matrix $T$ (corresponding to transitions from state $i$ ) is: $T_i \sim \text{Mult}(n_{ij} | T_i) \text{Dir}(T_i | \alpha )$ 

where $\alpha $ is the Dirichlet hyperparameter.

(Continuous HMM) Sample multivariate normal emission parameters from Normal-Inverse-Wishart posterior for state $i$ : $ \mu _i, \Sigma _i \sim N(y|\mu _i, \Sigma _i) N(\mu _i |0, \Sigma _i) \text{IW}(\Sigma _i) $ 

(Discrete HMM) Sample the emission parameters from a Multinomial-Dirichlet posterior.

Evaluation:

We evaluate the methods on how well they predict the next observation in the validation set. For the HMM models, we do a forward pass on the validation set (no backward pass unlike the full FFBS), and compute the HMM state distribution vector $p_t$ for each time step $t$ . Then we compute the predictive likelihood for the next observation as follows: $ P(y_{t+1} | p_t) =\sum _{x_t=1}^n \sum _{x_{t+1}=1}^n p_{tx_t} \cdot T_{x_t, x_{t+1}} \cdot P(y_{t+1} | x_{t+1})$ 

where $n$ is the number of hidden states in the HMM.
```

### Chunks (ID and text)

Passage ID: `qasper-passage-v1-777dfbf8390064980c0c5af0cb7d35f6c7e6e6e1ac474cffb14aa8b92abba28e`

```text
The HMM training procedure is as follows:

Initialization of HMM hidden states:

(Discrete HMM) Random multinomial draw for each time step (i.i.d. across time steps).

(Continuous HMM) K-means clusters fit on LSTM states, to speed up convergence relative to random initialization.

At each iteration:

Sample states using Forward Filtering Backwards Sampling algorithm (FFBS, BIBREF7 ).

Sample transition parameters from a Multinomial-Dirichlet posterior. Let $n_{ij}$ be the number of transitions from state $i$ to state $j$ . Then the posterior distribution of the $i$ -th row of transition matrix $T$ (corresponding to transitions from state $i$ ) is: $T_i \sim \text{Mult}(n_{ij} | T_i) \text{Dir}(T_i | \alpha )$

where $\alpha $ is the Dirichlet hyperparameter.

(Continuous HMM) Sample multivariate normal emission parameters from Normal-Inverse-Wishart posterior for state $i$ : $ \mu _i, \Sigma _i \sim N(y|\mu _i, \Sigma _i) N(\mu _i |0, \Sigma _i) \text{IW}(\Sigma _i) $

(Discrete HMM) Sample the emission parameters from a Multinomial-Dirichlet posterior.

Evaluation:

We evaluate the methods on how well they predict the next observation in the validation set. For the HMM models, we do a forward pass on the validation set (no backward pass unlike the full FFBS), and compute the HMM state distribution vector $p_t$ for each time step $t$ . Then we compute the predictive likelihood for the next observation as follows: $ P(y_{t+1} | p_t) =\sum _{x_t=1}^n \sum _{x_{t+1}=1}^n p_{tx_t} \cdot T_{x_t, x_{t+1}} \cdot P(y_{t+1} | x_{t+1})$

where $n$ is the number of hidden states in the HMM.
```

### Evaluation results

| Passage ID | Result | Reason |
| --- | --- | --- |
| `qasper-passage-v1-777dfbf8390064980c0c5af0cb7d35f6c7e6e6e1ac474cffb14aa8b92abba28e` | pending | |

## Source sample: 4

### Source text

Paper: 1606.05320; section: 5; paragraphs: [2]; character span: 0:859 (within sampled paragraph).

Original section context:

```text
We test the models on several text data sets on the character level: the Penn Tree Bank (5M characters), and two data sets used by BIBREF4 , Tiny Shakespeare (1M characters) and Linux Kernel (5M characters). We chose $k=20$ for the continuous HMM based on a PCA analysis of the LSTM states, as the first 20 components captured almost all the variance.

Table 1 shows the predictive log likelihood of the next text character for each method. On all text data sets, the hybrid algorithm performs a bit better than the standalone LSTM with the same LSTM state dimension. This effect gets smaller as we increase the LSTM size and the HMM makes less difference to the prediction (though it can still make a difference in terms of interpretability). The hybrid algorithm with 20 HMM states does better than the one with 10 HMM states. The joint hybrid algorithm outperforms the sequential hybrid on Shakespeare data, but does worse on PTB and Linux data, which suggests that the joint hybrid is more helpful for smaller data sets. The joint hybrid is an order of magnitude slower than the sequential hybrid, as the SGD-based HMM is slower to train than the FFBS-based HMM.

We interpret the HMM and LSTM states in the hybrid algorithm with 10 LSTM state dimensions and 10 HMM states in Figures 3 and 3 , showing which features are identified by the HMM and LSTM components. In Figures 3 and 3 , we color-code the training data with the 10 HMM states. In Figures 3 and 3 , we apply k-means clustering to the LSTM state vectors, and color-code the training data with the clusters. The HMM and LSTM states pick up on spaces, indentation, and special characters in the data (such as comment symbols in Linux data). We see some examples where the HMM and LSTM complement each other, such as learning different things about spaces and comments on Linux data, or punctuation on the Shakespeare data. In Figure 2 , we see that some individual LSTM hidden state dimensions identify similar features, such as comment symbols in the Linux data.
```

### Chunks (ID and text)

Passage ID: `qasper-passage-v1-2a7ac1f3d86283ad64d947ef7578298ec8f375567b6daf955a60b90fd364fbe5`

```text
We test the models on several text data sets on the character level: the Penn Tree Bank (5M characters), and two data sets used by BIBREF4 , Tiny Shakespeare (1M characters) and Linux Kernel (5M characters). We chose $k=20$ for the continuous HMM based on a PCA analysis of the LSTM states, as the first 20 components captured almost all the variance.

Table 1 shows the predictive log likelihood of the next text character for each method. On all text data sets, the hybrid algorithm performs a bit better than the standalone LSTM with the same LSTM state dimension. This effect gets smaller as we increase the LSTM size and the HMM makes less difference to the prediction (though it can still make a difference in terms of interpretability). The hybrid algorithm with 20 HMM states does better than the one with 10 HMM states. The joint hybrid algorithm outperforms the sequential hybrid on Shakespeare data, but does worse on PTB and Linux data, which suggests that the joint hybrid is more helpful for smaller data sets. The joint hybrid is an order of magnitude slower than the sequential hybrid, as the SGD-based HMM is slower to train than the FFBS-based HMM.

We interpret the HMM and LSTM states in the hybrid algorithm with 10 LSTM state dimensions and 10 HMM states in Figures 3 and 3 , showing which features are identified by the HMM and LSTM components. In Figures 3 and 3 , we color-code the training data with the 10 HMM states. In Figures 3 and 3 , we apply k-means clustering to the LSTM state vectors, and color-code the training data with the clusters. The HMM and LSTM states pick up on spaces, indentation, and special characters in the data (such as comment symbols in Linux data). We see some examples where the HMM and LSTM complement each other, such as learning different things about spaces and comments on Linux data, or punctuation on the Shakespeare data. In Figure 2 , we see that some individual LSTM hidden state dimensions identify similar features, such as comment symbols in the Linux data.
```

### Evaluation results

| Passage ID | Result | Reason |
| --- | --- | --- |
| `qasper-passage-v1-2a7ac1f3d86283ad64d947ef7578298ec8f375567b6daf955a60b90fd364fbe5` | pending | |

## Source sample: 5

### Source text

Paper: 1904.12087; section: 3; paragraphs: [1]; character span: 0:288 (within sampled paragraph).

Original section context:

```text
Our submission to the CLI shared task is a system based on a meta-classifier trained on several SVM models. Meta-classifiers BIBREF16 and ensemble learning methods have proved to deliver competitive performance not only in language identification BIBREF5 , BIBREF6 but also in many other text classification tasks BIBREF17 , BIBREF18 .

The meta-classifier is an adaptation of previous submissions to VarDial shared tasks described in BIBREF6 . It is essentially a bagging ensemble trained on the outputs of linear SVM classifiers. As features, the system uses the following character n-gram and character skip-gram features:

character $n$ -grams of order 1–5;

1-skip character bigrams and trigrams;

2-skip character bigrams and trigrams;

3-skip character bigrams and trigrams.

Each feature class is used to train a single linear SVM classifier using LIBLINEAR BIBREF19 . The outputs of these SVM classifiers on the training data are then used to train the meta-classifier.
```

### Chunks (ID and text)

Passage ID: `qasper-passage-v1-d233302cee6f9b4872bed7e5d01752ab9952baec17e824e1390884bc96066f0e`

```text
Our submission to the CLI shared task is a system based on a meta-classifier trained on several SVM models. Meta-classifiers BIBREF16 and ensemble learning methods have proved to deliver competitive performance not only in language identification BIBREF5 , BIBREF6 but also in many other text classification tasks BIBREF17 , BIBREF18 .

The meta-classifier is an adaptation of previous submissions to VarDial shared tasks described in BIBREF6 . It is essentially a bagging ensemble trained on the outputs of linear SVM classifiers. As features, the system uses the following character n-gram and character skip-gram features:

character $n$ -grams of order 1–5;

1-skip character bigrams and trigrams;

2-skip character bigrams and trigrams;

3-skip character bigrams and trigrams.

Each feature class is used to train a single linear SVM classifier using LIBLINEAR BIBREF19 . The outputs of these SVM classifiers on the training data are then used to train the meta-classifier.
```

### Evaluation results

| Passage ID | Result | Reason |
| --- | --- | --- |
| `qasper-passage-v1-d233302cee6f9b4872bed7e5d01752ab9952baec17e824e1390884bc96066f0e` | pending | |

## Source sample: 6

### Source text

Paper: 1904.12087; section: 4; paragraphs: [0]; character span: 0:328 (within sampled paragraph).

Original section context:

```text
Table 2 showcases the results obtained by our team (PZ in bold) and the best submission by each of the eight teams which participating in the CLI shared task. Even though the competition allowed the use of other datasets (open submission), we have used only the dataset provided by the shared task organizers to train our model.

Our submission was ranked 4th in the shared task, only a few percentage points below the top-3 systems: NRC-CNRC, tearsofjoy, and Twist Bytes. The meta-classifier achieved much higher performance at distinguishing between these Mesopotamian languages and dialects than the neural model by ghpaetzold, which ranked 6th in the competition. We present this neural model in more detail comparing its performance to our meta-classifier in Section "Comparison to a Neural Model" .
```

### Chunks (ID and text)

Passage ID: `qasper-passage-v1-fe09ede3a0ecbb55ff9d0eaf00f99c80453541b66cd42429ca9b07906afcfea1`

```text
Table 2 showcases the results obtained by our team (PZ in bold) and the best submission by each of the eight teams which participating in the CLI shared task. Even though the competition allowed the use of other datasets (open submission), we have used only the dataset provided by the shared task organizers to train our model.

Our submission was ranked 4th in the shared task, only a few percentage points below the top-3 systems: NRC-CNRC, tearsofjoy, and Twist Bytes. The meta-classifier achieved much higher performance at distinguishing between these Mesopotamian languages and dialects than the neural model by ghpaetzold, which ranked 6th in the competition. We present this neural model in more detail comparing its performance to our meta-classifier in Section "Comparison to a Neural Model" .
```

### Evaluation results

| Passage ID | Result | Reason |
| --- | --- | --- |
| `qasper-passage-v1-fe09ede3a0ecbb55ff9d0eaf00f99c80453541b66cd42429ca9b07906afcfea1` | pending | |

## Source sample: 7

### Source text

Paper: 1901.03860; section: 1; paragraphs: [2]; character span: 0:354 (within sampled paragraph).

Original section context:

```text
In the past, Hidden Markov Models (HMM) BIBREF6 , BIBREF7 , BIBREF8 have been used to solve the CSKS problem. But since the HMM techniques use Viterbi algorithms(computationally expensive) a faster approach is required.

Owning to the popularity of deep learning, many recent works such as BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 , BIBREF13 have used deep learning techniques for many speech processing tasks. In tasks such as ASR, Hannun et al. BIBREF3 proposed a RNN based model to transcribe speech into text. Even for plain keyword spotting, BIBREF1 , BIBREF2 , BIBREF14 , BIBREF15 , BIBREF16 , BIBREF17 have proposed various deep learning architectures to solve the task. But to the best of our knowledge, no past work has deployed deep learning for spotting keywords in continuous speech.

Recently, a lot of work is being done on training deep learning models with limited training data. Out of them, few-shot techniques as proposed by BIBREF18 , BIBREF4 have become really popular. Pons et al. BIBREF16 proposed a few-shot technique using prototypical networks BIBREF4 and transfer leaning BIBREF19 , BIBREF20 to solve a different audio task.

We took inspiration from these works to design our experiments to solve the CSKS task.
```

### Chunks (ID and text)

Passage ID: `qasper-passage-v1-291e5f5e7d09909b2664cdd54941bc0084f69f24971fb910a7309e5ed66c6eae`

```text
In the past, Hidden Markov Models (HMM) BIBREF6 , BIBREF7 , BIBREF8 have been used to solve the CSKS problem. But since the HMM techniques use Viterbi algorithms(computationally expensive) a faster approach is required.

Owning to the popularity of deep learning, many recent works such as BIBREF9 , BIBREF10 , BIBREF11 , BIBREF12 , BIBREF13 have used deep learning techniques for many speech processing tasks. In tasks such as ASR, Hannun et al. BIBREF3 proposed a RNN based model to transcribe speech into text. Even for plain keyword spotting, BIBREF1 , BIBREF2 , BIBREF14 , BIBREF15 , BIBREF16 , BIBREF17 have proposed various deep learning architectures to solve the task. But to the best of our knowledge, no past work has deployed deep learning for spotting keywords in continuous speech.

Recently, a lot of work is being done on training deep learning models with limited training data. Out of them, few-shot techniques as proposed by BIBREF18 , BIBREF4 have become really popular. Pons et al. BIBREF16 proposed a few-shot technique using prototypical networks BIBREF4 and transfer leaning BIBREF19 , BIBREF20 to solve a different audio task.

We took inspiration from these works to design our experiments to solve the CSKS task.
```

### Evaluation results

| Passage ID | Result | Reason |
| --- | --- | --- |
| `qasper-passage-v1-291e5f5e7d09909b2664cdd54941bc0084f69f24971fb910a7309e5ed66c6eae` | pending | |

## Source sample: 8

### Source text

Paper: 1901.03860; section: 3; paragraphs: [0]; character span: 0:1480 (within sampled paragraph).

Original section context:

```text
Our dataset consisted of keyword instances but the algorithm trained using this data needs to classify keywords in fragments of running conversations. To address this, we simulate the continuous speech scenario, both for keyword containing audio and background fragments, by using publicly available audio data which consisted of podcasts audio, songs, and audio narration files. For simulating fragments with keywords, we extract two random contiguous chunks from these publicly available audio files and insert the keyword either in the beginning, in the middle or in the end of the chunks, thus creating an audio segment of 2 seconds. Random 2 second segments taken from publicly available audio are used to simulate segments with no keywords(also referred to as background elsewhere in the paper). These artificially simulated audio chunks from train/validation set of pure keyword utterances were used to train/validate the model. Since the test data is quite noisy, we further used various kinds of techniques such as time-shift, pitch-shift and intensity variation to augment the data. Furthermore we used the same strategy as Tang et al. BIBREF2 of caching the data while training deep neural network on batches and artificially generating only 30% data which goes into a batch. By following these techniques, we could increase the data by many folds which not only helped the model to generalise better but also helped reduce the data preparation time during every epoch.
```

### Chunks (ID and text)

Passage ID: `qasper-passage-v1-d73ebc5d29d41795fea32c97a182b158f91865470801b4f8db83fc1440ca1d99`

```text
Our dataset consisted of keyword instances but the algorithm trained using this data needs to classify keywords in fragments of running conversations. To address this, we simulate the continuous speech scenario, both for keyword containing audio and background fragments, by using publicly available audio data which consisted of podcasts audio, songs, and audio narration files. For simulating fragments with keywords, we extract two random contiguous chunks from these publicly available audio files and insert the keyword either in the beginning, in the middle or in the end of the chunks, thus creating an audio segment of 2 seconds. Random 2 second segments taken from publicly available audio are used to simulate segments with no keywords(also referred to as background elsewhere in the paper). These artificially simulated audio chunks from train/validation set of pure keyword utterances were used to train/validate the model. Since the test data is quite noisy, we further used various kinds of techniques such as time-shift, pitch-shift and intensity variation to augment the data. Furthermore we used the same strategy as Tang et al. BIBREF2 of caching the data while training deep neural network on batches and artificially generating only 30% data which goes into a batch. By following these techniques, we could increase the data by many folds which not only helped the model to generalise better but also helped reduce the data preparation time during every epoch.
```

### Evaluation results

| Passage ID | Result | Reason |
| --- | --- | --- |
| `qasper-passage-v1-d73ebc5d29d41795fea32c97a182b158f91865470801b4f8db83fc1440ca1d99` | pending | |

## Source sample: 9

### Source text

Paper: 1811.00942; section: 0; paragraphs: [0]; character span: 0:437 (within sampled paragraph).

Original section context:

```text
Deep learning has unquestionably advanced the state of the art in many natural language processing tasks, from syntactic dependency parsing BIBREF0 to named-entity recognition BIBREF1 to machine translation BIBREF2 . The same certainly applies to language modeling, where recent advances in neural language models (NLMs) have led to dramatically better approaches as measured using standard metrics such as perplexity BIBREF3 , BIBREF4 .

Specifically focused on language modeling, this paper examines an issue that to our knowledge has not been explored: advances in neural language models have come at a significant cost in terms of increased computational complexity. Computing the probability of a token sequence using non-neural techniques requires a number of phrase lookups and perhaps a few arithmetic operations, whereas model inference with NLMs require large matrix multiplications consuming perhaps millions of floating point operations (FLOPs). These performance tradeoffs are worth discussing.

In truth, language models exist in a quality–performance tradeoff space. As model quality increases (e.g., lower perplexity), performance as measured in terms of energy consumption, query latency, etc. tends to decrease. For applications primarily running in the cloud—say, machine translation—practitioners often solely optimize for the lowest perplexity. This is because such applications are embarrassingly parallel and hence trivial to scale in a data center environment.

There are, however, applications of NLMs that require less one-sided optimizations. On mobile devices such as smartphones and tablets, for example, NLMs may be integrated into software keyboards for next-word prediction, allowing much faster text entry. Popular Android apps that enthusiastically tout this technology include SwiftKey and Swype. The greater computational costs of NLMs lead to higher energy usage in model inference, translating into shorter battery life.

In this paper, we examine the quality–performance tradeoff in the shift from non-neural to neural language models. In particular, we compare Kneser–Ney smoothing, widely accepted as the state of the art prior to NLMs, to the best NLMs today. The decrease in perplexity on standard datasets has been well documented BIBREF3 , but to our knowledge no one has examined the performances tradeoffs. With deployment on a mobile device in mind, we evaluate energy usage and inference latency on a Raspberry Pi (which shares the same ARM architecture as nearly all smartphones today). We find that a 2.5 $\times $ reduction in perplexity on PTB comes at a staggering cost in terms of performance: inference with NLMs takes 49 $\times $ longer and requires 32 $\times $ more energy. Furthermore, we find that impressive reductions in perplexity translate into at best modest improvements in next-word prediction, which is arguable a better metric for evaluating software keyboards on a smartphone. The contribution of this paper is the first known elucidation of this quality–performance tradeoff. Note that we refrain from prescriptive recommendations: whether or not a tradeoff is worthwhile depends on the application. Nevertheless, NLP engineers should arguably keep these tradeoffs in mind when selecting a particular operating point.
```

### Chunks (ID and text)

Passage ID: `qasper-passage-v1-94975861cfcc0353f454de9219a14471437bbd99096fc3b772b4c368fc5b1dc9`

```text
Deep learning has unquestionably advanced the state of the art in many natural language processing tasks, from syntactic dependency parsing BIBREF0 to named-entity recognition BIBREF1 to machine translation BIBREF2 . The same certainly applies to language modeling, where recent advances in neural language models (NLMs) have led to dramatically better approaches as measured using standard metrics such as perplexity BIBREF3 , BIBREF4 .

Specifically focused on language modeling, this paper examines an issue that to our knowledge has not been explored: advances in neural language models have come at a significant cost in terms of increased computational complexity. Computing the probability of a token sequence using non-neural techniques requires a number of phrase lookups and perhaps a few arithmetic operations, whereas model inference with NLMs require large matrix multiplications consuming perhaps millions of floating point operations (FLOPs). These performance tradeoffs are worth discussing.

In truth, language models exist in a quality–performance tradeoff space. As model quality increases (e.g., lower perplexity), performance as measured in terms of energy consumption, query latency, etc. tends to decrease. For applications primarily running in the cloud—say, machine translation—practitioners often solely optimize for the lowest perplexity. This is because such applications are embarrassingly parallel and hence trivial to scale in a data center environment.

There are, however, applications of NLMs that require less one-sided optimizations. On mobile devices such as smartphones and tablets, for example, NLMs may be integrated into software keyboards for next-word prediction, allowing much faster text entry. Popular Android apps that enthusiastically tout this technology include SwiftKey and Swype. The greater computational costs of NLMs lead to higher energy usage in model inference, translating into shorter battery life.

In this paper, we examine the quality–performance tradeoff in the shift from non-neural to neural language models. In particular, we compare Kneser–Ney smoothing, widely accepted as the state of the art prior to NLMs, to the best NLMs today. The decrease in perplexity on standard datasets has been well documented BIBREF3 , but to our knowledge no one has examined the performances tradeoffs. With deployment on a mobile device in mind, we evaluate energy usage and inference latency on a Raspberry Pi (which shares the same ARM architecture as nearly all smartphones today). We find that a 2.5 $\times $ reduction in perplexity on PTB comes at a staggering cost in terms of performance: inference with NLMs takes 49 $\times $ longer and requires 32
```

### Evaluation results

| Passage ID | Result | Reason |
| --- | --- | --- |
| `qasper-passage-v1-94975861cfcc0353f454de9219a14471437bbd99096fc3b772b4c368fc5b1dc9` | pending | |

## Source sample: 10

### Source text

Paper: 1811.00942; section: 2; paragraphs: [2]; character span: 0:259 (within sampled paragraph).

Original section context:

```text
We conducted our experiments on Penn Treebank (PTB; BIBREF12 ) and WikiText-103 (WT103; BIBREF13 ). Preprocessed by BIBREF14 , PTB contains 887K tokens for training, 70K for validation, and 78K for test, with a vocabulary size of 10,000. On the other hand, WT103 comprises 103 million tokens for training, 217K for validation, and 245K for test, spanning a vocabulary of 267K unique tokens.

For the neural language model, we used a four-layer QRNN BIBREF10 , which achieves state-of-the-art results on a variety of datasets, such as WT103 BIBREF11 and PTB. To compare against more common LSTM architectures, we also evaluated AWD-LSTM BIBREF4 on PTB. For the non-neural approach, we used a standard five-gram model with modified Kneser-Ney smoothing BIBREF15 , as explored in BIBREF16 on PTB. We denote the QRNN models for PTB and WT103 as ptb-qrnn and wt103-qrnn, respectively.

For each model, we examined word-level perplexity, R@3 in next-word prediction, latency (ms/q), and energy usage (mJ/q). To explore the perplexity–recall relationship, we collected individual perplexity and recall statistics for each sentence in the test set.
```

### Chunks (ID and text)

Passage ID: `qasper-passage-v1-253bf5a02f8f139ccbafbe85818a2ce05bbe1a45250a454958d3d9703d34d793`

```text
We conducted our experiments on Penn Treebank (PTB; BIBREF12 ) and WikiText-103 (WT103; BIBREF13 ). Preprocessed by BIBREF14 , PTB contains 887K tokens for training, 70K for validation, and 78K for test, with a vocabulary size of 10,000. On the other hand, WT103 comprises 103 million tokens for training, 217K for validation, and 245K for test, spanning a vocabulary of 267K unique tokens.

For the neural language model, we used a four-layer QRNN BIBREF10 , which achieves state-of-the-art results on a variety of datasets, such as WT103 BIBREF11 and PTB. To compare against more common LSTM architectures, we also evaluated AWD-LSTM BIBREF4 on PTB. For the non-neural approach, we used a standard five-gram model with modified Kneser-Ney smoothing BIBREF15 , as explored in BIBREF16 on PTB. We denote the QRNN models for PTB and WT103 as ptb-qrnn and wt103-qrnn, respectively.

For each model, we examined word-level perplexity, R@3 in next-word prediction, latency (ms/q), and energy usage (mJ/q). To explore the perplexity–recall relationship, we collected individual perplexity and recall statistics for each sentence in the test set.
```

### Evaluation results

| Passage ID | Result | Reason |
| --- | --- | --- |
| `qasper-passage-v1-253bf5a02f8f139ccbafbe85818a2ce05bbe1a45250a454958d3d9703d34d793` | pending | |
