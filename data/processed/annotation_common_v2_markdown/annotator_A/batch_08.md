# Passage relevance annotation

Annotator: 

Enter your name or agreed identifier after `Annotator:`.

Judge whether each passage helps answer the question, including useful partial evidence. Topic overlap alone is insufficient.

0 — Not relevant

1 — Relevant

Fill in only `Label: 0` or `Label: 1`. Preserve all content and record numbers. Work independently; do not exchange labels before submission. Algorithm sources are disclosed.

## Question 0141

Paper: Reverse-Engineering Satire, or"Paper on Computational Humor Accepted Despite Making Serious Advances"

> Where can I access the dataset?

### Common Retrieved Chunks

#### Passage 1075

Retrieved by: BM25, Hybrid

> Humor is key to human cognition and holds questions and promise for advancing artificial intelligence. We focus on the humorous genre of satirical news headlines and present Unfun.me, an online game for collecting pairs of satirical and similarbutseriouslooking headlines, which precisely reveal the humorcarrying words and the semantic structure in satirical news headlines. We hope that future work will build on these initial results, as well as on the dataset that we publish with this paper BIBREF9 , in order to make further progress on understanding satire and, more generally, the role of humor in intelligence.

#### Relevance 1075

Label: 

#### Passage 1076

Retrieved by: BM25, Hybrid

> r(h^{\prime }) = \frac{1}{n} \sum _{i=1}^n p_{B_i}(h^{\prime }),
> \;\;\;\;
> s(h,h^{\prime }) = 1-\frac{d(h,h^{\prime })}{\max \lbrace |h|,|h^{\prime }|\rbrace },$$   (Eq. ) $h$0
> 
> where, in turn, $|x|$ is the number of tokens (i.e., words) in a string $x$ , and $d(h,h^{\prime })$ , the tokenbased edit distance BIBREF7 between $h$ and $h^{\prime }$ , i.e., the minimum number of insertions, deletions, and substitutions by which $h$ can be transformed into $h^{\prime }$ , considering as the basic units of a string its tokens, rather than its characters. The geometric mean was chosen in Eq. 2 because it is zero whenever one of the two factors is zero (which is not true for the more standard arithmetic mean): a modified headline that seems very serious, but has nothing to do with the original, should not receive any points, nor should a headline that is nearly identical to the original, but retains all its humor.
> 
> Reward for task 2. Since player $B$ 's very purpose is to determine whether $h^{\prime }$ is without humor, we do not have a groundtruth rating for $h^{\prime }$ . In order to still be able to reward player $B$ for participating in task 2, and to incentivize her to indicate her true opinion about $h^{\prime }$ , we also ask her for her belief $p_B(g)$ regarding a headline $g$ for which we do have the ground truth of “serious” vs. “satirical”. The reward $R_B(g)$ that player $B$ receives for rating headline $g$ is then
> 
> $$R_B(g) = {\left\lbrace \begin{array}{ll}
> \log (p_B(g)) & \text{if $g$ is serious,}\\
> \log (1-p_B(g)) & \text{if $g$ is satirical.}\\
> \end{array}\right.}$$   (Eq. 3)
> 
> Note that this is a proper scoring rule BIBREF8 , i.e., player $B$ maximizes her expected reward by indicating her true belief. This would not be true for the more straightforward scoring formula without logarithms, which would drive players to report beliefs of 0 or 1 instead of their true beliefs. Also, as $h^{\prime }$ and $g$ are shown in random order, $B$ does not know which is which, and her optimal strategy is to indicate her true belief on both.
> 
> Overall game flow. Whenever a user wants to play, we generate a type-1 task with probability $\alpha

#### Relevance 1076

Label: 

#### Passage 1077

Retrieved by: BM25, Hybrid

> (83% of all pairs, cf. Fig. "Semantic analysis of aligned corpus" ), seriousness ratings correlate positively with edit distance. In particular, it seems harder to remove the humor by changing one word than by changing two words, whereas the marginal effect is negligible when allowing for even larger edits. The positive correlation does not hold for the much smaller number (17%) of pairs with an edit distance above 5. Inspecting the data, we find that this is caused by headlines so inherently absurd that even large edits cannot manage to remove the humor from them.
> 
> Seriousness ratings. Recall that, in task 2, players attribute seriousness ratings to modified headlines $h^{\prime }$ , as well as to unmodified serious or satirical headlines $g$ . We find that, in all three cases, the distribution of seriousness ratings is bimodal, with extreme values close to 0 or 1 being most common. Hence, we binarize ratings into two levels, “satirical” (rating below 0.5) and “serious” (rating above 0.5).
> 
> In order to see how people rate serious, satirical, and modified headlines, respectively, Table 1 aggregates ratings by headline (considering only the 1,806 headlines with at least two ratings) and splits the headlines into three groups: “consensus serious” (over 50% “serious” ratings), “no consensus” (exactly 50%), and “consensus satirical” (under 50%).
> 
> We make two observations. First, modified headlines $h^{\prime }$ (column 3 of Table 1 ) are distributed roughly evenly over the three groups; i.e., there are about as many headlines from which the humor has been successfully removed (“consensus serious”) as not (“consensus satirical”). The most useful modified headlines for our purposes are those from the “consensus serious” group, as they likely do not carry the humor of the original $h$ anymore. Hence, we shall restrict our subsequent analyses to the corresponding 654 successful pairs. Second, the ratings are heavily skewed toward the ground truth for unmodified serious (column 1) and satirical (column 2) headlines; i.e., players can typically well distinguish serious from satirical headlines (but cf. discussion in Sec. "Discussion and future work" ).
> 
> Insertions, deletions, substitutions. When computing the edit distance $d(h,h^{\prime })$ using dynamic programming, we can also keep track of an optimal sequence of edit operations

#### Relevance 1077

Label: 

#### Passage 1082

Retrieved by: Dense, Hybrid

> distinguish serious from satirical headlines (but cf. discussion in Sec. "Discussion and future work" ).
> 
> Insertions, deletions, substitutions. When computing the edit distance $d(h,h^{\prime })$ using dynamic programming, we can also keep track of an optimal sequence of edit operations (insertions, deletions, substitutions) for transforming $h$ into $h^{\prime }$ BIBREF7 . In Fig. "Discussion and future work" , we plot the distribution of edit operations, macroaveraged over all pairs. We see that substitutions clearly dominate (61%), followed by deletions (34%), with insertions being very rare (5%).
> 
> Pairs with edit distance 1 are particularly interesting, as they are the most similar, as well as the most frequent (Fig. "Semantic analysis of aligned corpus" , footnote UID9 ). Also, the optimal edit sequence may not be unique in general, but for edit distance 1 it is. Hence, Fig. "Discussion and future work" also displays the distribution over edit operations for pairs with edit distance 1 only. Here, substitutions dominate even more (77%), and insertions are even rarer (2%).
> 
> Reversing the direction of the editing process, we hence conclude that writers of satirical headlines tend to work overwhelmingly by substituting words in (hypothetical) similarbutserious headlines, and to a certain degree by adding words, but very rarely by deleting words.

#### Relevance 1082

Label: 

#### Passage 1084

Retrieved by: Dense, Hybrid

> the two realms of human psychiatry and biblical lore into a single headline. Only the satirical headline $H(x)$ itself (red box in Table 3 ) is explicit to the reader, whereas $x^{\prime }$ and $P$ (and thus all the other 3 boxes) need to be inferred. A main advantage of our method is that it also makes $x^{\prime }$ explicit and thereby facilitates inferring $P$ and thus the semantic structure that induces humor (as in Table 3 ).
> 
> We emphasize that the script opposition that invalidates the logical step from $P(x)$ to $H(x)$ is not arbitrary, but must be along certain dimensions essential to human existence and contrasting “good” vs. “bad” (Table 3 ). Interestingly, in typical jokes, the “good” side is explicit and the “bad” side must be inferred, whereas in satirical headlines, either the “good” or the “bad” side may be explicit. And indeed, as shown by the examples of Table 3 (where the “good” side is marked in bold), satirical headlines differ from typical jokes in that they tend to make the “bad” side explicit.
> 
> Single vs. multiple edit operations. A large fraction of all headlines from The Onion—and an overwhelming fraction of those in singlesubstitution pairs—can be analyzed with the falseanalogy template of Table 3 (and we indeed encourage the reader to apply it to the examples of Table 3 ). Additionally, many of the pairs with two substitutions also follow this template. H3 in Table 3 , which plays on the opposition of the Federal Reserve being a serious institution vs. Cash4Gold being a dubious enterprise exploiting its customers, exemplifies how, whenever multiple substitutions are applied, they all need to follow the same opposition (e.g., Fed : Cash4Gold = $85 million : $85 = serious : dubious).

#### Relevance 1084

Label: 

### BM25

#### Passage 1078

Retrieved by: BM25

> After characterizing aligned pairs syntactically, we now move to the semantic level. We first analyze the aligned pairs obtained from Unfun.me and later discuss our findings in the broader context of established theories of humor (Sec. "Discussion and future work" ).
> 
> Example. Before a more general analysis, let us first consider again our running example (Sec. "Introduction" ), God diagnosed with bipolar disorder. This satirical headline works by blending two realms that are fundamentally opposed—the human and the divine—by talking about God as a human. Although the literally described situation is impossible (God is perfect and cannot possibly have a disease), the line still makes sense by expressing a crucial commonality between bipolar humans and God, namely that both may act unpredictably. But for humans, being unpredictable (due to bipolarity) is a sign of imperfection, whereas for God it is a sign of perfection (“The Lord moves in mysterious ways”), and it is this opposition that makes the line humorous.
> 
> The main advantage of our aligned corpus is that it lets us generalize this ad-hoc analysis of a particular example to a large and representative set of satirical headlines by pinpointing the essential, humorcarrying words in every headline: if the humor has been successfully removed from a headline $h$ by altering certain words, then we know that these very words are key to making $h$ funny.
> 
> This is especially true for singlesubstitution pairs; e.g., in the running example, God was replaced by Bob Dylan (a particular human), giving rise to the serioussounding Bob Dylan diagnosed with bipolar disorder. The automatically extracted chunk pair {God, Bob Dylan} surfaces both the crucial commonality in the context of the headline (unpredictability) and the crucial opposition (God vs. human; unpredictability as a good vs. bad trait).
> 
> While the semantic analysis of original vs. substituted chunks may be difficult to automate, having access to explicit chunk pairs tremendously facilitates a largescale human analysis. Conducting such an analysis revealed that the above pattern of a crucial commonality combined with a crucial opposition occurs in a large fraction of satirical headlines, and particularly in nearly all singlesubstitution pairs.
> 
> Script opposition. The crucial opposition has been called script opposition by humor theorists (cf.

#### Relevance 1078

Label: 

#### Passage 1079

Retrieved by: BM25

> Here we introduce Unfun.me, our game for collecting pairs of satirical and similarbutseriouslooking headlines. The game, available online at http://unfun.me and visually depicted in Fig. 1 , challenges players in two tasks.
> 
> Task 1: Unfun the headline! This is the core task where the reverseengineering of satire happens (left panel in Fig. 1 ). A player, $A$ , is given a satirical headline $h$ and is asked to turn it into a headline $h^{\prime }$ that could conceivably have been published by a serious news outlet, by changing as few words as possible.
> 
> Task 2: Real or not? Whether on purpose or not, player $A$ may have done a bad job in task 1, and $h^{\prime }$ may still be humorous. Detecting and filtering such cases is the purpose of task 2 (right panel in Fig. 1 ), where $h^{\prime }$ is shown to another player, $B$ , who is asked to indicate her belief $p_B(h^{\prime })$ that $h^{\prime }$ comes from a serious news outlet using a slider bar ranging from 0% to 100%. We shall refer to $p_B(h^{\prime })$ as $B$ 's seriousness rating of $h^{\prime }$ . For reasons that will become clear below, player $B$ also indicates her belief $h^{\prime }$0 for a second, unmodified headline $h^{\prime }$1 (unrelated to $h^{\prime }$2 ) that originates from either a serious or a satirical news outlet. The two headlines $h^{\prime }$3 and $h^{\prime }$4 are presented in random order, in order to avoid biases.
> 
> For the purpose of incentivizing players to make highquality contributions, we reward them as follows.
> 
> Reward for task 1. As player $A$ is supposed to remove the humor from $h$ via a minimal modification, his reward $R_A(h,h^{\prime })$ increases (1) with the average rating $r(h^{\prime })$ that the modified headline $h^{\prime }$ receives from all $n$ players $B_1, \dots , B_n$ who rate it and (2) with the similarity $s(h,h^{\prime })$ of $h$ and $h^{\prime }$ :
> 
> $$\text{where}
> \;\;\;\;
> r(h^{\prime }) = \frac{1}{n} \sum _{i=1}^n p_{B_i}(h^{\prime }),
> \;\;\;\;
> s(h,h^{\prime }) = 1-\frac{d(h,h^{\prime })}{\max \lbrace |h|,|h^{\prime }|\rbrace },$$   (Eq. ) $h$0
> 
> where, in turn, $|x|$ is the number of tokens (i.e., words) in a string $x$ , and $d(h,h^{\prime })$

#### Relevance 1079

Label: 

### Dense

#### Passage 1080

Retrieved by: Dense

> 2,801 $(h,h^{\prime })$ pairs collected in task 1, $h$ follows that pattern in 21% of all cases.
> 
> Chunk-based edit distance. Recomputing edit distances at the chunk level, rather than the token level, we obtain the chunkbased edit distance distribution of Fig. "Conclusion" . It resembles the tokenbased edit distance distribution of Fig. "Semantic analysis of aligned corpus" , with the difference that the smallest possible distance of 1 is even more prevalent (52% vs. 33% of pairs), due to the fact that modifying a single chunk frequently corresponds to modifying multiple tokens. Since, moreover, the vast majority (97%) of all singlechunk edits are substitutions, we now focus on 254 $(h,h^{\prime })$ pairs where exactly one chunk of $h$ has been modified (henceforth singlesubstitution pairs). This accounts for about half of all successful pairs (after discarding pairs that were problematic for the chunker).
> 
> Dominance of noun phrases. We now ask which syntactic chunk types (noun phrases, verb phrases, etc.) are modified to remove humor. In doing so, we need to be careful, as some chunk types are more common a priori than others; e.g., 59% of all chunks in original satirical headlines are noun phrases, 20%, verb phrases, etc. We therefore compare the empirical distribution of modified chunks with this prior distribution, via the ratio of the two (termed lift). Table 2 shows that noun phrases constitute 89% of the modified chunks (lift 1.52), whereas all other chunk types are less frequent than under the prior. We conclude that the humor of satirical news headlines tends to reside in noun phrases.
> 
> Micro-punchlines. We now ask where in terms of location within a headline the humor tends to reside. To answer this question, we compute the position of the modified chunk in each headline's chunk sequence and plot the distribution of modified positions in Fig. 3 . We see that, regardless of headline length, modifications to the last chunk are particularly overrepresented. This is an important finding: we have previously (Sec. "Introduction" ) argued that satirical headlines consist of a punchline only, with minimal narrative structure, and indeed it was this very intuition that led us to investigate headlines in isolation. Given Fig. 3 , we need

#### Relevance 1080

Label: 

#### Passage 1081

Retrieved by: Dense

> Next, we go one level deeper and ask: what parts of a satirical headline should be modified in order to remove the humor from it, or conversely, what parts of a serious headline should be modified in order to add humor? We first tackle this question from a syntactic perspective, before moving to a deeper, semantic perspective in Sec. "Semantic analysis of aligned corpus" .
> 
> From tokens to chunks. We analyze syntax at an intermediate level of abstraction between simple sequences of part-of-speech (POS) tags and complex parse trees, by relying on a chunker (also called shallow parser). We use OpenNLP's maximum entropy chunker BIBREF10 , after retraining it to better handle pithy, headlinestyle text. The chunker takes POStagged text as input and groups subsequent tokens into meaningful phrases (chunks) without inferring the recursive structure of parse trees; e.g., our running example (Sec. "Introduction" ) is chunked as [NP Bob Dylan] [VP diagnosed] [PP with] [NP bipolar disorder] (chunk labels expanded in Table 2 ). Chunks are handy because they abstract away lowlevel details; e.g., changing God to Bob Dylan requires a tokenbased edit distance of 2, but a chunkbased distance of only 1, where the latter is more desirable because it more closely captures the conceptual modification of one entity being replaced by another entity.
> 
> Chunking all 9,159 original headlines from our The Onion corpus, we find the most frequent chunk pattern to be NP VP NP PP NP (4.8%; e.g., H2 in Table 3 ), followed by NP VP NP (4.3%; e.g., H4) and NP VP PP NP (3.3%; e.g., H9).
> 
> To control for syntactic effects, it is useful to study a large number of pairs $(h,h^{\prime })$ where all original headlines $h$ follow a fixed syntactic pattern. We therefore gave priority to headlines of the most frequent pattern (NP VP NP PP NP) for a certain time period when sampling satirical headlines as input to task 1, such that, out of all 2,801 $(h,h^{\prime })$ pairs collected in task 1, $h$ follows that pattern in 21% of all cases.
> 
> Chunk-based edit distance. Recomputing edit distances at the chunk level, rather than the token level, we obtain the chunkbased edit distance distribution of

#### Relevance 1081

Label: 

#### Passage 1083

Retrieved by: Dense

> The most widely accepted theory of verbal humor is the so-called General Theory of Verbal Humor by Attardo and Raskin attardo1991script, an extension of Raskin's raskin1985semantic Semantic-Script Theory of Humor, which we summarize when discussing our findings in its context in Sec. "Discussion and future work" .
> 
> Much follow-up work has built on these theories; see the excellent primer edited by Raskin raskin2008primer. Here, we focus on contributions from computer science, where most work has been on the detection of humor in various forms, e.g., irony BIBREF11 , BIBREF12 , sarcasm BIBREF13 , BIBREF14 , and satire BIBREF15 , BIBREF16 , sometimes with the goal of deciding which of two texts is funnier BIBREF17 . These works use documents or sentences as the smallest unit of analysis, whereas we operate at a finer granularity, analyzing the very words causing the switch from serious to funny.
> 
> Another cluster of work has considered the generation of humor, mostly via fixed templates such as acronyms BIBREF18 , puns BIBREF19 , BIBREF20 , twoliners BIBREF21 , or crossreference ambiguity BIBREF22 .
> 
> Finally, our work also relates to efforts of constructing humor corpora BIBREF23 , BIBREF24 . Here, too, we increase the granularity by actively generating new data, rather than compiling humorous texts that have already been produced. Crucially, ours is a corpus of aligned pairs, rather than individual texts, which enables entirely novel analyses that were infeasible before.

#### Relevance 1083

Label: 

### Hybrid

None

## Question 0142

Paper: A hybrid text normalization system using multi-head self-attention for mandarin

> What models do they compare to?

### Common Retrieved Chunks

#### Passage 1085

Retrieved by: BM25, Dense, Hybrid

> The rule-based TN model can handle the TN task alone and is the baseline in our experiments. It has the same idea as in BIBREF8 but has a more complicated system of rules with priorities. The model contains 45 different groups and about 300 patterns as sub-groups, each of which uses a keyword with regular expressions to match the preceding and following texts. Each pattern also has a priority value. During normalization, each sentence is fed as input and the NSW will be matched by the regular expressions. The model tries to match patterns with longer context and slowly decrease the context length until a match is found. If there are multiple pattern matches with the same length, the one with a higher priority will be chosen for the NSW. The model has been developed on abundant test data and bad cases. The advantage of the rule-based system is the flexibility, since one can simply add more special cases when they appear, such as new units. However, improving the performance of this system on more general cases becomes a bottleneck. For example, in a report of a football game, it cannot transform “1-3” to score if there are no keywords like “score” or “game” close to it.

#### Relevance 1085

Label: 

#### Passage 1087

Retrieved by: BM25, Dense, Hybrid

> models with bi-LSTM, bi-GRU with attention are proposed in BIBREF9, BIBREF10. Zhang and Sproat proposed a contextual seq2seq model, which uses a sliding-window and RNN with attentionBIBREF8. In this model, bi-directional GRU is used in both encoder and decoder, and the context words are labeled with “$\langle $self$\rangle $”, helping the model distinguish the NSW and the context.
> 
> However, seq2seq models have several downsides when directly applied in Mandarin TN tasks. As mentioned in BIBREF8, the sequence output directly from a seq2seq model can lead to unrecoverable errors. The model sometimes changes the context words which should be kept the same. Our experiments produce similar errors. For example, “Podnieks, Andrew 2000” is transformed to “Podncourt, Andrew Two Thousand”, changing “Podnieks” to “Podncourt”. These errors cannot be detected by the model itself. In BIBREF11, rules are applied to two specific categories to resolve silly errors, but this method is hard to apply to all cases. Another challenge in Mandarin is the word segmentation since words are not separated by spaces and the segmentation could depend on the context. Besides, some NSW may have more than one SFW in Mandarin, making the seq2seq model hard to train. For example, “UTF8gbsn两千零八年” and “UTF8gbsn二零零八年” are both acceptable SFW for “2008UTF8gbsn年”. The motivation of this paper is to combine the advantages of a rule-based model for its flexibility and a neural model to enhance the performance on more general cases. To avoid the problems of seq2seq models, we consider the TN task as a multi-class classification problem with carefully designed patterns for the neural model.
> 
> The contributions of this paper include the following. First, this is the first known TN system for Mandarin which uses a neural model with multi-head self-attention. Second, we propose a hybrid system combining a rule-based model and a neural model. Third, we experiment with different approaches to deal with imbalanced dataset in the TN task.
> 
> The paper is organized as follows. Section SECREF2 introduces the detailed structure of the proposed hybrid system and its training and inference. In Section SECREF3, the performance of different system configurations is evaluated on different datasets. And the conclusion is given in Section SECREF4.

#### Relevance 1087

Label: 

#### Passage 1088

Retrieved by: BM25, Dense, Hybrid

> For sentence embedding, pre-trained embedding models are used to boost training. We experiment on a word-to-vector (w2v) model trained on Wikipedia corpus and a trained Bidirectional Encoder Representations from Transformers (BERT) model. The experimental result is in SECREF11.
> 
> The experiments show that using a fixed context window achieves better performance than padding to the maximum length of all sentences. And padding with 1's gives a slightly better performance than with 0's. During inference, all NSW patterns in one sentence need to be processed simultaneously before transforming to SFW to keep their original context.

#### Relevance 1088

Label: 

#### Passage 1090

Retrieved by: Dense, Hybrid

> Table TABREF12 compares the highest pattern accuracy on the test set of 7 different neural model setups. Model 2-7's configuration differences are compared with Model 1: 1) proposed configuration; 2) replace w2v with BERT; 3) replace padding with 1's to 0's; 4) replace the context window length of 30 with maximum sentence length; 5) replace the loss with Cross Entropy (CE) loss; 6) remove mask; 7) apply data expansion.
> 
> Overall, w2v model has a better performance than BERT. A possible reason is that the model with BERT overfits the training data. The result also shows that data expansion does not give us better accuracy even though we find the model becomes more robust and has better performance on the lower proportioned patterns. This is because it changes the pattern distribution and the performance on the top proportioned patterns decreases a little, resulting in a large number of misclassifications. This is a tradeoff between a robust and a high-accuracy model, and we choose Model 1 for the following test since our golden set uses accuracy as the metric.
> 
> The neural model with the proposed configuration is evaluated on the test set of each pattern group. The test dataset has the same distribution as training data and precision/recall are evaluated on each pattern group. The $F_1$ score is the harmonic mean of precision and recall. The results of the top proportioned patterns are shown in Table TABREF13.
> 
> The proposed hybrid TN system is tested on our internal golden set of NSW-SFW pairs. It would be considered as an error if any character of the transformed and ground-truth sentences is different. The golden set has 67853 sentences, each of which contains 1-10 NSW strings. The sentence accuracy and pattern accuracy are listed in Table TABREF14. On sentence-level, the accuracy increases by 1.5%, which indicates an improvement of correctness on over 1000 sentences. The improvement is mainly on ambiguous NSW that don't have obvious keywords for rules to match and in long sentences.

#### Relevance 1090

Label: 

#### Passage 1091

Retrieved by: Dense, Hybrid

> The neural TN model is trained alone with inputs of labeled sentences and outputs of pattern groups. And the inference is on the entire hybrid TN system in Fig1, which takes the original text with NSW as input and text with SFW as output.
> 
> The training data is split into 36 different classes, each of which has its own NSW-SFW transformation. The distribution of the dataset is the same with the NSW in our internal news corpus and is imbalanced, which is one of the challenges for our neural model. The approaches to deal with the imbalanced dataset are discussed in the next section.

#### Relevance 1091

Label: 

### BM25

#### Passage 1086

Retrieved by: BM25

> Text Normalization (TN) is a process to transform non-standard words (NSW) into spoken-form words (SFW) for disambiguation. In Text-To-Speech (TTS), text normalization is an essential procedure to normalize unreadable numbers, symbols or characters, such as transforming “$20” to “twenty dollars” and “@” to “at”, into words that can be used in speech synthesis. The surrounding context is the determinant for ambiguous cases in TN. For example, the context will decide whether to read “2019” as year or a number, and whether to read “10:30” as time or the score of a game. In Mandarin, some cases depend on language habit instead of rules- “2” can either be read as “r” or “ling” and “1” as “y” or “yo”.
> 
> Currently, based on the traditional taxonomy approach for NSWBIBREF0, the Mandarin TN tasks are generally resolved by rule-based systems which use keywords and regular expressions to determine the SFW of ambiguous wordsBIBREF1, BIBREF2. These systems typically classify NSW into different pattern groups, such as abbreviations, numbers, etc., and then into sub-groups, such as phone number, year, etc., which has corresponding NSW-SFW transformations. ZhouBIBREF3 and JiaBIBREF4 proposed systems which use maximum entropy (ME) to further disambiguate the NSW with multiple pattern matches. For the NSW given the context constraints, the highest probability corresponds to the highest entropy. LiouBIBREF5 proposed a system of data-driven models which combines a rule-based and a keyword-based TN module. The second module classifies preceding and following words around the keywords and then trains a CRF model to predict the NSW patterns based on the classification results. There are some other hybrid systemsBIBREF6, BIBREF7 which use NLP models and rules separately to help normalize hard cases in TN.
> 
> For recent NLP studies, sequence-to-sequence (seq2seq) models have achieved impressive progress in TN tasks in English and RussianBIBREF8, BIBREF9. Seq2seq models typically encode sequences into a state vector, which is decoded into an output vector from its learnt vector representation and then to a sequence. Different seq2seq models with bi-LSTM, bi-GRU with attention are proposed in BIBREF9, BIBREF10. Zhang and Sproat proposed a contextual seq2seq model, which uses a sliding-window and RNN with attentionBIBREF8. In this model, bi-directional GRU is used in both encoder and decoder, and

#### Relevance 1086

Label: 

#### Passage 1089

Retrieved by: BM25

> In this paper, we propose a TN system for Mandarin using multi-head self-attention. This system aims to improve the performance of the rule-based model combining with the advantages of a neural model. For a highly developed rule-based model, improving the accuracy on general cases becomes a bottleneck, but a neural model can help overcome this problem. From the results on the test data, the proposed system improves the accuracy on NSW-SFW transformation by over 1.5% on sentence-level and still has a potential to improve further. This is an obvious improvement based on the fully developed rules, which can hardly improve anymore.
> 
> The future work includes other aspects of model explorations. Mandarin word segmentation methods will be applied to replace the character-wise embedding with word-level embedding. More sequence learning models and attention mechanisms will be experimented. And more labeled dataset in other corpus will be supplemented for training.

#### Relevance 1089

Label: 

### Dense

None

### Hybrid

None

## Question 0143

Paper: Mining Supervisor Evaluation and Peer Feedback in Performance Appraisals

> What clustering algorithms were used?

### Common Retrieved Chunks

#### Passage 1092

Retrieved by: BM25, Dense, Hybrid

> After identifying sentences in each class, we can now answer question (1) in Section SECREF1 . From 12742 sentences predicted to have label STRENGTH, we extract nouns that indicate the actual strength, and cluster them using a simple clustering algorithm which uses the cosine similarity between word embeddings of these nouns. We repeat this for the 9160 sentences with predicted label WEAKNESS or SUGGESTION as a single class. Tables TABREF15 and TABREF16 show a few representative clusters in strengths and in weaknesses, respectively. We also explored clustering 12742 STRENGTH sentences directly using CLUTO BIBREF19 and Carrot2 Lingo BIBREF20 clustering algorithms. Carrot2 Lingo discovered 167 clusters and also assigned labels to these clusters. We then generated 167 clusters using CLUTO as well. CLUTO does not generate cluster labels automatically, hence we used 5 most frequent words within the cluster as its labels. Table TABREF19 shows the largest 5 clusters by both the algorithms. It was observed that the clusters created by CLUTO were more meaningful and informative as compared to those by Carrot2 Lingo. Also, it was observed that there is some correspondence between noun clusters and sentence clusters. E.g. the nouns cluster motivation expertise knowledge talent skill (Table TABREF15 ) corresponds to the CLUTO sentence cluster skill customer management knowledge team (Table TABREF19 ). But overall, users found the nouns clusters to be more meaningful than the sentence clusters.

#### Relevance 1092

Label: 

#### Passage 1093

Retrieved by: BM25, Dense, Hybrid

> In this paper, we presented an analysis of the text generated in Performance Appraisal (PA) process in a large multi-national IT company. We performed sentence classification to identify strengths, weaknesses and suggestions for improvements found in the supervisor assessments and then used clustering to discover broad categories among them. As this is non-topical classification, we found that SVM with ADWS kernel BIBREF18 produced the best results. We also used multi-class multi-label classification techniques to match supervisor assessments to predefined broad perspectives on performance. Logistic Regression classifier was observed to produce the best results for this topical classification. Finally, we proposed an ILP-based summarization technique to produce a summary of peer feedback comments for a given employee and compared it with manual summaries.
> 
> The PA process also generates much structured data, such as supervisor ratings. It is an interesting problem to compare and combine the insights from discovered from structured data and unstructured text. Also, we are planning to automatically discover any additional performance attributes to the list of 15 attributes currently used by HR.

#### Relevance 1093

Label: 

#### Passage 1094

Retrieved by: BM25, Dense, Hybrid

> We considered a dataset of 100 employees, where for each employee multiple peer comments were recorded. Also, for each employee, a manual summary was generated by an HR personnel. The summaries generated by our ILP-based approach were compared with the corresponding manual summaries using the ROUGE BIBREF22 unigram score. For comparing performance of our ILP-based summarization algorithm, we explored a few summarization algorithms provided by the Sumy package. A common parameter which is required by all these algorithms is number of sentences keep in the final summary. ILP-based summarization requires a similar parameter K, which is automatically decided based on number of total candidate phrases. Assuming a sentence is equivalent to roughly 3 phrases, for Sumy algorithms, we set number of sentences parameter to the ceiling of K/3. Table TABREF51 shows average and standard deviation of ROUGE unigram f1 scores for each algorithm, over the 100 summaries. The performance of ILP-based summarization is comparable with the other algorithms, as the two sample t-test does not show statistically significant difference. Also, human evaluators preferred phrase-based summary generated by our approach to the other sentence-based summaries.

#### Relevance 1094

Label: 

#### Passage 1095

Retrieved by: BM25, Dense, Hybrid

> the presence of negative words / phrases like lacking, diffident, slow learner, less focused, etc. The SUGGESTION pattern not only looks for keywords like should, needs to but also for POS based pattern like “a verb in the base form (VB) in the beginning of a sentence”.
> 
> We randomly selected 2000 sentences from the supervisor assessment corpus and manually tagged them (dataset D1). This labelled dataset contained 705, 103, 822 and 370 sentences having the class labels STRENGTH, WEAKNESS, SUGGESTION or OTHER respectively. We trained several multi-class classifiers on this dataset. Table TABREF10 shows the results of 5-fold cross-validation experiments on dataset D1. For the first 5 classifiers, we used their implementation from the SciKit Learn library in Python (scikit-learn.org). The features used for these classifiers were simply the sentence words along with their frequencies. For the last 2 classifiers (in Table TABREF10 ), we used our own implementation. The overall accuracy for a classifier is defined as INLINEFORM0 , where the denominator is 2000 for dataset D1. Note that the pattern-based approach is unsupervised i.e., it did not use any training data. Hence, the results shown for it are for the entire dataset and not based on cross-validation.

#### Relevance 1095

Label: 

#### Passage 1096

Retrieved by: BM25, Dense, Hybrid

> in a large multi-national IT company.
> 
> The rest of the paper is organized as follows. Section SECREF2 summarizes related work. Section SECREF3 summarizes the PA dataset used in this paper. Section SECREF4 applies sentence classification algorithms to automatically discover three important classes of sentences in the PA corpus viz., sentences that discuss strengths, weaknesses of employees and contain suggestions for improving her performance. Section SECREF5 considers the problem of mapping the actual targets mentioned in strengths, weaknesses and suggestions to a fixed set of attributes. In Section SECREF6 , we discuss how the feedback from peers for a particular employee can be summarized. In Section SECREF7 we draw conclusions and identify some further work.

#### Relevance 1096

Label: 

### BM25

None

### Dense

None

### Hybrid

None

## Question 0144

Paper: Multilingual Twitter Sentiment Classification: The Role of Human Annotators

> Which measures of inter-annotator agreement are used?

### Common Retrieved Chunks

#### Passage 1097

Retrieved by: BM25, Hybrid

> is to use 10-fold cross-validation. The whole labeled set is partitioned into 10 folds, one is set apart for testing, and the remaining nine are used to train the model and evaluate it on the test fold. The process is repeated 10 times until each fold is used for testing exactly once. The reported evaluation results are the average of 10 tests, and the confidence intervals are estimated from standard deviations.
> 
> We constructed and evaluated six different classification models for each labeled language dataset. The results for the application datasets are extracted from the original papers. Our classifiers are all based on Support Vector Machines (SVM) BIBREF12 , and for reference we also constructed a Naive Bayes classifier BIBREF13 . Detailed results are in the Classification models performance subsection in Methods. When comparing the classifiers' performance with the Friedman-Nemenyi test BIBREF14 , BIBREF15 , it turns out that there is no statistically significant difference between most of them (see the Friedman-Nemenyi test subsection in Methods). For subsequent analyses and comparisons, we selected the TwoPlaneSVMbin classifier that is always in the group of top classifiers according to two most relevant evaluation measures.
> 
> The main results of this paper are summarized in Fig FIGREF8 . It shows a comparison of the self-agreement, the inter-annotator agreement, and the TwoPlaneSVMbin classifier performance, for the 13 language datasets and the four application datasets.
> 
> The self-agreement for most of the datasets is above 0.6. The exceptions, Albanian and Spanish, indicate low quality annotators which should be eliminated from further considerations. In the applications corpus, the Emojis dataset is the only one with the self-agreement lower than the inter-annotator agreement, due to a high number of low quality Spanish annotations included. The other three application datasets have relatively high self-agreement (0.7–0.9, due to more carefully selected annotators), and higher variability (due to a lower number of tweets annotated twice, 2–4% only).
> 
> The inter-annotator agreement varies a lot, and is always lower than the self-agreement, except for Emojis. The high inter-annotator agreement for Facebook(it) is consistent with the high self-agreement. Values below 0.2 (Albanian and Spanish) indicate low quality annotators, consistent with the low self-agreement. Values in the range between 0.3–0.4 (Ser/Cro/Bos, Bulgarian,

#### Relevance 1097

Label: 

#### Passage 1099

Retrieved by: BM25, Hybrid

> Determining sentiment expressed in a tweet is not an easy task, and depends on subjective judgment of human annotators. Annotators often disagree between themselves, and even an individual is not always consistent with her/himself. There are several reasons for disagreements, such as: inherent difficulty of the task (e.g., estimating the “sentiment” about the future stock movement), different vocabularies used in different domains (e.g., financial markets vs. environmental issues), topic drift in time (e.g., events which abruptly shift the topic of discussions on Twitter), or simply a poor quality of the annotator's work. In the data we analyze, we observe all the above issues, try to identify them by computational means, and draw lessons how the annotation process should be conducted in the future.
> 
> During the manual sentiment labeling of tweets, a fraction of tweets (about 15%) was intentionally duplicated to be annotated twice, either by the same annotator or by two different annotators (see details in the Datasets subsection in Methods). From multiple annotations of the same annotator we compute the self-agreement, and from multiple annotations by different annotators we compute the inter-annotator agreement (abbreviated as inter-agreement). The confidence intervals for the agreements are estimated by bootstrapping BIBREF11 . The detailed results are in the Annotator agreements subsection in Methods. It turns out that the self-agreement is a good measure to identify low quality annotators, and that the inter-annotator agreement provides a good estimate of the objective difficulty of the task, unless it is too low.
> 
> To manually label over 1.6 million tweets requires a considerable effort. The purpose of this effort is to use the labeled data to built sentiment classification models for each of the 13 languages. A classification model can then be applied to unlabeled data in various application scenarios, as was the case with our four application datasets.
> 
> A classification model can be build by any suitable supervised machine learning method. To evaluate the model, a standard approach in machine learning is to use 10-fold cross-validation. The whole labeled set is partitioned into 10 folds, one is set apart for testing, and the remaining nine are used to train the model and evaluate it on the test fold. The process is

#### Relevance 1099

Label: 

#### Passage 1101

Retrieved by: BM25, Dense, Hybrid

> the self-agreement, except for Emojis. The high inter-annotator agreement for Facebook(it) is consistent with the high self-agreement. Values below 0.2 (Albanian and Spanish) indicate low quality annotators, consistent with the low self-agreement. Values in the range between 0.3–0.4 (Ser/Cro/Bos, Bulgarian, and German) indicate a problem with the annotation process, and are discussed in more detail in the next subsection.
> 
> The classifier performance is typically in the range between 0.4–0.6. Notable exceptions are Albanian and Spanish, with the performance barely above random, but very close to the inter-annotator agreement. More interesting are the datasets with a relatively low performance, around 0.4, that cannot be explained by low quality annotations alone: Ser/Cro/Bos, Bulgarian, German, Portuguese, and Environment. They are analyzed in the next subsections.
> 
> The main hypothesis of this paper is that the inter-annotator agreement approximates an upper bound for a classifier performance. In Fig FIGREF8 we observe three such cases where the classifier performance, in the range 0.4–0.6, approaches its limit: Polish, Slovenian, and DJIA30. There are also three cases where there still appears a gap between the classifier performance and the inter-annotator agreement: English, Facebook(it), and Environment. In order to confirm the hypothesis, we analyze the evolution of the classifiers performance through time and check if the performance is still improving or was the plateau already reached. This is not always possible: There are datasets where only one annotator was engaged and for which there is no inter-annotator agreement (Russian, Swedish, Hungarian, Slovak, and Portuguese). For them we can only draw analogies with the multiply annotated datasets and speculate about the conclusions.
> 
> In the next two subsection we first analyze the language datasets, and then the four application datasets.

#### Relevance 1101

Label: 

#### Passage 1102

Retrieved by: Dense, Hybrid

> Table TABREF35 gives the results of the annotator agreements in terms of the four evaluation measures. The self-agreement is computed from the tweets annotated twice by the same annotator, and the inter-annotator agreement from the tweets annotated twice by two different annotators, where possible. The 95% confidence intervals for INLINEFORM0 are computed from 1,000 bootstrap samples.
> 
> Note that the Albanian and Spanish datasets have very low INLINEFORM0 agreement values. All the results for INLINEFORM1 , reported here and throughout the paper, refer to the INLINEFORM2 instance, for the reasons outlined in the next subsection.

#### Relevance 1102

Label: 

#### Passage 1104

Retrieved by: Dense, Hybrid

> for the Bulgarian dataset (Fig FIGREF14 , chart on the right). The classifier's peak performance is reached even earlier, at 40,000 tweets ( INLINEFORM0 is 0.378), but the inter-annotator agreement is also considerably lower, more than 10% points below the Slovenian ( INLINEFORM1 is 0.367). In such cases, when the inter-annotator agreement is “too low” (our estimate is when INLINEFORM2 INLINEFORM3 ), the inter-annotator agreement is a poor estimator of the difficulty of the task, and should not be used as a performance approximation. Instead, one could analyze the reasons for the disagreements, as we do with cases in the following paragraphs.
> 
> The inter-annotator agreement for the German dataset is low, INLINEFORM0 is 0.344. The classifier's performance is higher already with the initial small datasets, and soon starts dropping (Fig FIGREF16 , chart on the left). It turns out that over 90% of the German tweets were labeled by two annotators only, dubbed annotator A and B. The annotation quality of the two annotators is very different, the self-agreement INLINEFORM1 for the annotator A is 0.590, and for the annotator B is 0.760. We consider the German tweets labeled by A and B separately (Fig FIGREF16 , charts in the middle and on the right). The lower quality A dataset reaches its maximum at 30,000 tweets, while the performance of the higher quality B dataset is still increasing. There was also a relatively high disagreement between the two annotators which resulted in a low classifier's performance. A conclusions drawn from this dataset, as well as from the Bulgarian, is that one should constantly monitor the self- and inter-annotator agreements, and promptly notify the annotators as soon as the agreements drop too low.
> 
> Fig FIGREF17 gives the results on the joint Ser/Cro/Bos dataset. We observe a low inter-annotator agreement ( INLINEFORM0 is 0.329) and a high variability of the classifier's performance.
> 
> The three languages, Serbian, Croatian, and Bosnian, are very similar and difficult to distinguish in short Twitter posts. However, we argue that the reason for poor performance is not in mixing the three languages, but in different annotation quality. Serbian (73,783 tweets) was annotated by 11 annotators, where two of them account for over 40%

#### Relevance 1104

Label: 

### BM25

#### Passage 1098

Retrieved by: BM25

> We present an analysis of over 1.6 million sentiment annotated Twitter posts, by far the largest set made publicly available until now. The labeled datasets are used to train sentiment classification models, and our analysis focuses on four main aspects: quality, quantity and sampling of the training data, and performance of the classifiers. Our main conclusion is that the choice of a particular classifier type is not so important, but that the training data has a major impact on the results.
> 
> There are several specific research questions we address:
> 
> (1) What is the nature and proper formalization of the sentiment classification problem, in particular, are the sentiment values ordered or not? We show that there is strong evidence that the sentiment values, negative, neutral, and positive, are perceived as ordered by human annotators (see subsection on Ordering of sentiment values in Methods).
> 
> (2) Which evaluation measures should be used to properly quantify the data quality and classifiers performance? In all the experiment, we compute values for four evaluation measures ( INLINEFORM0 , INLINEFORM1 , INLINEFORM2 , and INLINEFORM3 ). Since there is evidence that sentiment values are ordered, INLINEFORM4 and INLINEFORM5 are the most appropriate as they take the ordering into account.
> 
> (3) How to estimate the quality of the training data? We propose to invest an extra effort to label a portion of tweets twice, and then to compute the annotator self-agreement and the inter-annotator agreement. The self-agreement yields a useful indication when to exclude low quality annotators, and the inter-annotator agreement approximates an upper bound on the performance of sentiment classifiers.
> 
> (4) How to select the most appropriate classifier? Our results show that there are no statistically significant differences between the top classifiers. As a consequence, one should better direct the efforts into higher training data quality.
> 
> (5) What are acceptable levels of annotators agreement? On the basis of the 17 datasets analyzed, we propose the following rule-of-thumb: for self-agreement, INLINEFORM0 INLINEFORM1 , and for the inter-annotator agreement, INLINEFORM2 INLINEFORM3 .
> 
> (6) How many posts should be labeled with sentiment for training? We cannot provide conclusive answers here. It seems that 20,000 high-quality annotations already provide reasonable performance. The peak performance depends on

#### Relevance 1098

Label: 

#### Passage 1100

Retrieved by: BM25

> To label the 1.6 million tweets in the 13 languages, 83 native speakers were engaged, and an estimated effort of 38 person-months was spent. Can one reduce the efforts and focus them on more problematic datasets instead? It seems, for example, that the annotation of over 200,000 Polish tweets was an overkill. Worse, the annotation of over 250,000 Spanish tweets was largely a waste of efforts, due to the poor annotation quality.
> 
> We perform a post-hoc analysis of the 13 language datasets by measuring the performance of the sentiment classifiers through time. We emulate the evolution of the performance by feeding increasingly large labeled sets into the classifier training process. The labeled sets are ordered by the post time of the tweets, so one can detect potential topic shifts during the Twitter discussions. At each stage, the labeled set is increased by 10,000 tweets, and the set accumulated so far is used for training and testing the classifier. After each stage, the evaluation by 10-fold cross-validation is performed and the results are reported in the following charts. The final stage, when all the labeled sets are exhausted, corresponds to the results reported in Fig FIGREF8 . In subsequent figures, the x-axis denotes labeled sets increases by 10,000 tweets, the y-axis denotes the TwoPlaneSVMbin classifier performance measured by INLINEFORM0 , and the error bars are the 95% confidence intervals estimated from 10-fold cross-validations. The inter-annotator agreement is represented by a blue line—it is constant and is computed from all the available data.
> 
> We identify five cases, characterized by different relations between the classifier performance and the inter-annotator agreement: (i) a performance gap still exists, (ii) a performance limit is approached, (iii) low inter-annotator agreement, (iv) topic shift, and (v) very low annotation quality.
> 
> Fig FIGREF11 (chart on the left) shows the evolution of the English classifier performance, as it is fed increasingly large training sets. On top (in blue) is the inter-annotator agreement line ( INLINEFORM0 = 0.613). The classifier's INLINEFORM1 is increasing from the initial 0.422 to 0.516, but is still considerably below the inter-annotator agreement. Despite the relatively large training set (around 90,000 labeled tweets) there is still a performance gap and even more

#### Relevance 1100

Label: 

### Dense

#### Passage 1103

Retrieved by: Dense

> and for the inter-annotator agreement, INLINEFORM2 INLINEFORM3 .
> 
> (6) How many posts should be labeled with sentiment for training? We cannot provide conclusive answers here. It seems that 20,000 high-quality annotations already provide reasonable performance. The peak performance depends on the inter-annotator agreement and we estimate that around 100,000 annotations are needed. However, more important than sheer quantity is the quality, and domain- and topic-specific coverage of the posts, as demonstrated on several use-cases.
> 
> This gives the following directions for the short-term future work. The annotation process has to be redesigned to allow for systematic monitoring of the annotation quality. In particular, more than one annotator per language/domain has to be engaged. We propose an increased overhead of posts to be labeled twice, from 15% to 20%, both by individuals as well as by two different annotators. The posts to be labeled multiple times could be based on their “importance” as measured by their retweet count BIBREF9 , for example. The self- and the inter-annotator agreements have to be continuously monitored and warnings issued when they drop below the selected thresholds. Extreme disagreements (as measured by INLINEFORM0 ) should be promptly directed to a “master” annotator who has to resolve the disagreement and issue a proper annotation together with a brief guideline. After each batch of a few thousand annotations, a classification model should be trained and its performance evaluated. This would help in monitoring the progress towards the inter-annotator agreement as well as in detecting possible abrupt topic shifts.
> 
> There is a number of open research questions to be addressed. One is how to combine the lexicon-based and machine learning approaches to sentiment classification. In BIBREF5 , authors already showed that the combination of both outperforms the individual approaches. However, sentiment lexicons are rarely available for languages other than English and require considerable efforts to construct. For several languages, one could use the data published by Dodds et al. BIBREF2 . For the languages covered in this study, one can construct a basic sentiment lexicon from the annotated tweets, in the analogy to derivation of the emoji sentiment lexicon BIBREF10 .
> 
> Another research direction, with the potential of considerable performance improvements, is the construction

#### Relevance 1103

Label: 

#### Passage 1105

Retrieved by: Dense

> In general, the agreement can be estimated between any two methods of generating data. One of the main ideas of this work is to use the same measures to estimate the agreement between the human annotators as well as the agreement between the results of automated classification and the “gold standard”. There are different measures of agreement, and to get robust estimates we apply four well-known measures from the fields of inter-rater agreement and machine learning.
> 
> Krippendorff's Alpha-reliability ( INLINEFORM0 ) BIBREF6 is a generalization of several specialized agreement measures. It works for any number of annotators, and is applicable to different variable types and metrics (e.g., nominal, ordered, interval, etc.). INLINEFORM1 is defined as follows: INLINEFORM2
> 
> where INLINEFORM0 is the observed disagreement between annotators, and INLINEFORM1 is a disagreement, expected by chance. When annotators agree perfectly, INLINEFORM2 INLINEFORM3 , and when the level of agreement equals the agreement by chance, INLINEFORM4 INLINEFORM5 . The two disagreement measures are defined as follows: INLINEFORM6
> 
> INLINEFORM0
> 
> The arguments, INLINEFORM0 , and INLINEFORM1 , refer to the frequencies in a coincidence matrix, defined below. INLINEFORM2 is a difference function between the values of INLINEFORM3 and INLINEFORM4 , and depends on the metric properties of the variable. INLINEFORM5 (and INLINEFORM6 ) is a discrete sentiment variable with three possible values: negative ( INLINEFORM7 ), neutral (0), or positive (+). We consider two options: either the sentiment variable INLINEFORM8 is nominal or ordered. This gives rise to two instance of INLINEFORM9 , INLINEFORM10 (nominal, when INLINEFORM11 is unordered) and INLINEFORM12 (interval, when INLINEFORM13 is ordered), corresponding to two difference functions INLINEFORM14 : INLINEFORM15
> 
> INLINEFORM0
> 
> Note that in the case of the interval difference function, INLINEFORM0 assigns a disagreement of 1 between the neutral and the negative or positive sentiment, and a disagreement of 2 between the extremes, i.e., the negative and positive sentiment. The corresponding disagreements INLINEFORM1 and INLINEFORM2 between the extreme classes are then four times larger than between the neighbouring classes.
> 
> A coincidence matrix tabulates all pairable values of INLINEFORM0 from two annotators into a INLINEFORM1 -by- INLINEFORM2 square matrix, where INLINEFORM3 is the number of possible values of INLINEFORM4 . In the case of sentiment annotations, we

#### Relevance 1105

Label: 

### Hybrid

None

## Question 0145

Paper: Semantic Product Search

> What were the baseline methods?

### Common Retrieved Chunks

#### Passage 1106

Retrieved by: BM25, Dense, Hybrid

> A critical decision when employing a vector space model is defining a match, especially in product search where there is an important tradeoff between precision and recall. For example, accessories like mounts may also be relevant for the query “led tv.”
> 
> Pruning results based on a threshold is a common practice to identify the match set. Pointwise loss functions, such as mean squared error (MSE) or mean absolute error (MAE), require an additional step post-training to identify the threshold. Pairwise loss functions do not provide guarantees on the magnitude of scores (only on relative ordering) and thus do not work well in practice with threshold-based pruning. Hence, we started with a pointwise 2-part hinge loss function as shown in Equation ( EQREF11 ) that maximizes the similarity between the query and a purchased product while minimizing the similarity between a query and random products. Define INLINEFORM0 , and let INLINEFORM1 if product INLINEFORM2 is purchased in response to query INLINEFORM3 , and INLINEFORM4 otherwise. Furthermore let INLINEFORM5 , and INLINEFORM6 for some predefined thresholds INLINEFORM7 and INLINEFORM8 and INLINEFORM9 . The two part hinge loss can be defined as DISPLAYFORM0
> 
> Intuitively, the loss ensures that when INLINEFORM0 then INLINEFORM1 is less than INLINEFORM2 and when INLINEFORM3 then INLINEFORM4 is above INLINEFORM5 . After some empirical tuning on a validation set, we set INLINEFORM6 and INLINEFORM7 .
> 
> As shown in Table TABREF26 , the 2-part hinge loss improved offline matching performance by more than 2X over the MSE baseline. However in Figure FIGREF12 , a large overlap in score distribution between positives and negatives can be seen. Furthermore, the score distribution for negatives appeared bimodal. After manually inspecting the negative training examples that fell in this region, we uncovered that these were products that were impressed but not purchased by the customer. From a matching standpoint, these products are usually valid results to show to customers. To improve the model's ability to distinguish positives and negatives considering these two classes of negatives, we introduced a 3-part hinge loss: DISPLAYFORM0
> 
> where INLINEFORM0 , INLINEFORM1 , and INLINEFORM2 denote indicators signifying if the product INLINEFORM3 was purchased, not impressed and not purchased, and impressed (but not purchased) in

#### Relevance 1106

Label: 

#### Passage 1110

Retrieved by: BM25, Dense, Hybrid

> Finally, in Table TABREF30 , we compare the results of our model to four baselines: DSSM BIBREF12 , Match Pyramid BIBREF18 , ARC-II BIBREF15 , and our model with frozen, randomly initialized embeddings. We only use word unigrams or character trigrams in our model, as it is not immediately clear how to extend the bag-of-tokens approach to methods that incorporate ordering. We compare the performance of using the 3-part L2 hinge loss to the original loss presented for each model. Across all baselines, matching performance of the model improves using the 3-part L2 hinge loss. ARC-II and Match Pyramid ranking performance is similar or lower when using the 3-part loss. Ranking performance improves for DSSM, possibly because the original approach uses only random negatives to approximate the softmax normalization. More complex models, like Match Pyramid and ARC-II, had significantly lower matching and ranking performance while taking significantly longer to train and evaluate. These models are also much harder to tune and tend to overfit.
> 
> The embeddings in our model are trained end-to-end. Previous experiments using other methods, including Glove and word2vec, to initialize the embeddings yielded poorer results than end-to-end training. When comparing our model with randomly initialized to one with trained embeddings, we see that end-to-end training results in over a 3X improvement in Recall@100 and MAP.

#### Relevance 1110

Label: 

#### Passage 1111

Retrieved by: Dense, Hybrid

> We define two evaluation subtasks: matching and ranking.
> 
> Matching: The goal of the matching task is to retrieve all relevant documents from a large corpus for a given query. In order to measure the matching performance, we first sample a set of 20K queries. We then evaluate the model's ability to recall purchased products from a sub-corpus of 1 million products for those queries. Note that the 1 million product corpus contains purchased and impressed products for every query from the evaluation period as well as additional random negatives. We tune the model hyperparameters to maximize Recall@100 and Mean Average Precision (MAP).
> 
> Ranking: The goal of this task is to order a set of documents by relevance, defined as purchase count conditioned on the query. The set of documents contains purchased and impressed products. We report standard information retrieval ranking metrics, such as Normalized Discounted Cumulative Gain (NDCG) and Mean Reciprocal Rank (MRR).

#### Relevance 1111

Label: 

#### Passage 1112

Retrieved by: Dense, Hybrid

> for ranking, these methods report limited success on ad hoc retrieval tasks BIBREF24 and only achieve a sub-50% Recall@100 and MAP on our product matching dataset, as shown with the ARC-II and Match Pyramid baselines in Table TABREF30 .
> 
> While we frequently evaluate our hypotheses on interaction matrix-based methods, we find that a factorized model architecture achieves comparable performance while only requiring constant memory per product. Hence, we only present our experiments as it pertains to factorized models in this paper. Although latent factor models improve ranking metrics due to their ability to memorize associations between the query and the product, we exclude it from this paper as we focus on the matching task. Our choice of model architecture was informed by empirical experiments while constrained by the cost per query and our ability to respond within 20 milliseconds for thousands of queries per second.

#### Relevance 1112

Label: 

#### Passage 1113

Retrieved by: Dense, Hybrid

> In this section, we present the durable learnings from thousands of experiments. We fix the embedding dimension to 256, weight matrix initialization to Xavier initialization BIBREF29 , batch size to 8192, and the optimizer to ADAM with the configuration INLINEFORM0 for all the results presented. We refer to the hinge losses defined in Section SECREF10 with INLINEFORM1 and INLINEFORM2 as the L1 and L2 variants respectively. Unigram tokenization is used in Table TABREF26 and Table TABREF27 , as the relative ordering of results does not change with other more sophisticated tokenizations.
> 
> We present the results of different loss functions in Table TABREF26 . We see that the L2 variant of each loss consistently outperforms the L1. We hypothesize that L2 variants are robust to outliers in cosine similarity. The 3-part hinge loss outperforms the 2-part hinge loss in matching metrics in all experiments although the two loss functions have similar ranking performance. By considering impressed negatives, whose text is usually more similar to positives than negatives, separately from random negatives in the 3-part hinge loss, the scores for positives and random negatives become better separated, as shown in Section SECREF10 . The model can better differentiate between positives and random negatives, improving Recall and MAP. Because the ranking task is not distinguishing between relevant and random products but instead focuses on ordering purchased and impressed products, it is not surprising that the 2-part and 3-part loss functions have similar performance.
> 
> In Table TABREF27 , we present the results of using LSTM, GRU, and averaging to aggregate the token embeddings. Averaging performs similar to or slightly better than recurrent units with significantly less training time. As mentioned in Section SECREF8 , in the product search setting, queries and product titles tend to be relatively short, so averaging is sufficient to capture the short-range dependencies that exist in queries and product titles. Furthermore, recurrent methods are more expressive but introduce specialization between the query and title. Consequently, local word-level matching between the query and the product title may not be not captured as well.
> 
> In Table TABREF28 , we compare the performance of using different tokenization methods. We use average pooling and the 3-part L2 hinge loss.

#### Relevance 1113

Label: 

### BM25

#### Passage 1107

Retrieved by: BM25

> There is a rich literature in natural language processing (NLP) and information retrieval (IR) on capturing the semantics of queries and documents. Word2vec BIBREF4 garnered significant attention by demonstrating the use of word embeddings to capture semantic structure; synonyms cluster together in the embedding space. This technique was successfully applied to document ranking for web search with the DESM model BIBREF5 . Building from the ideas in word2vec, BIBREF6 trained neural word embeddings to find neighboring words to expand queries with synonyms. Ultimately, based on these recent advancements and other key insights, the state-of-the-art models for semantic search can generally be classified into three categories:
> 
> BIBREF7 introduced Latent Semantic Analysis (LSA), which computes a low-rank factorization of a term-document matrix to identify semantic concepts and was further refined by BIBREF8 , BIBREF9 and extended by ideas from Latent Dirichlet Allocation (LDA) BIBREF10 in BIBREF11 . In 2013, BIBREF12 published the seminal paper in the space of factorized models by introducing the Deep Semantic Similarity Model (DSSM). Inspired by LSA and Semantic Hashing BIBREF13 , DSSM involves training an end-to-end deep neural network with a discriminative loss to learn a fixed-width representation for queries and documents. Fully connected units in the DSSM architecture were subsequently replaced with Convolutional Neural Networks (CNNs) BIBREF14 , BIBREF15 and Recurrent Neural Networks (RNNs) BIBREF16 to respect word ordering. In an alternate approach, which articulated the idea of interaction models, BIBREF17 introduced the Deep Relevance Matching Model (DRMM) which leverages an interaction matrix to capture local term matching within neural approaches which has been successfully extended by MatchPyramid BIBREF18 and other techniques BIBREF19 , BIBREF20 , BIBREF21 , BIBREF22 , BIBREF23 . Nevertheless, these interaction methods require memory and computation proportional to the number of words in the document and hence are prohibitively expensive for online inference. In addition, Duet BIBREF24 combines the approaches of DSSM and DRMM to balance the importance of semantic and lexical matching. Despite obtaining state-of-the-art results for ranking, these methods report limited success on ad hoc retrieval tasks BIBREF24 and only achieve a sub-50% Recall@100 and MAP on our product matching dataset, as shown with the ARC-II and Match Pyramid baselines in Table TABREF30 .
> 
> While

#### Relevance 1107

Label: 

#### Passage 1108

Retrieved by: BM25

> Our neural network architecture is shown in Figure FIGREF9 . As in the distributed arm of the Duet model, our first model component is an embedding layer that consists of INLINEFORM0 parameters where INLINEFORM1 is the vocabulary and INLINEFORM2 is the embedding dimension. Each row corresponds to the parameters for a word. Unlike Duet, we share our embeddings across the query and product. Intuitively, sharing the embedding layer in a Siamese network works well, capturing local word-level matching even before training these networks. Our experiments in Table UID37 confirm this intuition. We discuss the specifics of our query and product representation in Section SECREF4 .
> 
> To generate a fixed length embedding for the query ( INLINEFORM0 ) and the product ( INLINEFORM1 ) from individual word embeddings, we use average pooling after observing little difference (<0.5%) in both MAP and Recall@100 relative to recurrent approaches like LSTM and GRU (see Table TABREF27 ). Average pooling also requires far less computation, reducing training time and inference latency. We reconciled this departure from state-of-the-art solutions for Question Answering and other NLP tasks through an analysis that showed that, unlike web search, both query and product information tend to be shorter, without long-range dependencies. Additionally, product search queries do not contain stop words and typically require every query word (or its synonym) to be present in the product.
> 
> Queries typically have fewer words than the product content. Because of this, we observed a noticeable difference in the magnitude of query and product embeddings. This was expected as the query and the product models were shared with no additional parameters to account for this variance. Hence, we introduced Batch Normalization layers BIBREF25 after the pooling layers for the query and the product arms. Finally, we compute the cosine similarity between INLINEFORM0 and INLINEFORM1 . During online A/B testing, we precompute INLINEFORM2 for all the products in the catalog and use a INLINEFORM3 -Nearest Neighbors algorithm to retrieve the most similar products to a given query INLINEFORM4 .

#### Relevance 1108

Label: 

#### Passage 1109

Retrieved by: BM25

> In this section, we describe our tokenization methodology, or the procedure by which we break a string into a sequence of smaller components such as words, phrases, sub-words, or characters. We combine word unigram, word n-gram, and character trigram features into a bag of n-grams and use hashing to handle the large vocabulary size, similar to the fastText approach BIBREF26 .
> 
> This is the basic form of tokenization where the input query or product title is tokenized into a list of words. For example, the word unigrams of "artistic iphone 6s case" are ["artistic", "iphone", "6s", "case"].
> 
> In a bag of words model like ours, word unigrams lose word ordering. Instead of using LSTMs or CNNs to address this issue, we opted for INLINEFORM0 -grams as in BIBREF27 . For example, the word bigrams of "artistic iphone 6s case" are ["artistic#iphone", "iphone#6s", "6s#case"] and the trigrams are ["artistic#iphone#6s", "iphone#6s#case"]. These INLINEFORM1 -grams capture phrase-level information; for example if “for iphone” exists in the query, the model can infer that the customer's intention is to search for iphone accessories rather than iphone — an intent not captured by a unigram model.
> 
> Character trigram embeddings were proposed by the DSSM paper BIBREF12 . The string is broken into a list of all three-character sequences. For the example "artistic iphone 6s case", the character trigrams are ["#ar", "art", "rti", "tis", "ist", "sti", "tic", "ic#", "c#i", "#ip", "iph", "pho", "hon", "one", "ne#", "e#6", "#6s", "6s#", "s#c", "#ca", "cas", "ase", "se#"]. Character trigrams are robust to typos (“iphione” and “iphonr”) and handle compound words (“amazontv” and “firetvstick”) naturally. Another advantage in our setting is the ability to capture similarity of model parts and sizes.
> 
> It is computationally infeasible to maintain a vocabulary that includes all the possible word INLINEFORM0 -grams as the dictionary size grows exponentially with INLINEFORM1 . Thus, we maintain a "short" list of several tens or hundreds of thousands of INLINEFORM2 -grams based on token frequency. A common practice for most NLP applications is to mask the input or use the embedding from the 0th location when an out-of-vocabulary word is encountered. Unfortunately, in Siamese networks, assigning all unknown words to the same shared embedding location results

#### Relevance 1109

Label: 

### Dense

None

### Hybrid

None

## Question 0146

Paper: Incorporating Word and Subword Units in Unsupervised Machine Translation Using Language Model Rescoring

> What are the post-processing approaches applied to the output?

### Common Retrieved Chunks

#### Passage 1114

Retrieved by: BM25, Hybrid

> In this paper, we propose to combine word-level and subword-level input representation in unsupervised NMT training on a morphologically rich language pair, German-Czech, without using any parallel data. Our results show the effectiveness of using language model rescoring to choose more fluent translation candidates. A series of pre-processing and post-processing approaches improve the quality of final translations, particularly to replace unknown words with possible relevant target words.

#### Relevance 1114

Label: 

#### Passage 1115

Retrieved by: BM25, Dense, Hybrid

> We note that in the corpus, there are tokens representing quantity or date. Therefore, we delexicalize the tokens using two special tokens: (1) <NUMBER> to replace all the numbers that express a specific quantity, and (2) <DATE> to replace all the numbers that express a date. Then, we retrieve these numbers in the post-processing. There are two advantages of data pre-processing. First, replacing numbers with special tokens can reduce vocabulary size. Second, the special tokens are more easily processed by the model.

#### Relevance 1115

Label: 

#### Passage 1117

Retrieved by: BM25, Dense, Hybrid

> In the pre-processing, we use the special tokens <NUMBER> and <DATE> to replace numbers that express a specific quantity and date respectively. Therefore, in the post-processing, we need to restore those numbers. We simply detect the pattern <NUMBER> and <DATE> in the original source sentences and then replace the special tokens in the translated sentences with the corresponding numbers detected in the source sentences. In order to make the replacement more accurate, we will detect more complicated patterns like <NUMBER> / <NUMBER> in the original source sentences. If the translated sentences also have the pattern, we replace this pattern <NUMBER> / <NUMBER> with the corresponding numbers in the original source sentences.

#### Relevance 1117

Label: 

#### Passage 1119

Retrieved by: Dense, Hybrid

> Ensemble methods have been shown very effective in many natural language processing tasks BIBREF20, BIBREF21. We apply an ensemble method by taking the top five translations from word-level and subword-level NMT, and rescore all translations using our pre-trained Czech language model mentioned in §SECREF18. Then, we select the best translation with the lowest perplexity.

#### Relevance 1119

Label: 

### BM25

#### Passage 1116

Retrieved by: BM25

> Machine translation (MT) has achieved huge advances in the past few years BIBREF1, BIBREF2, BIBREF3, BIBREF4. However, the need for a large amount of manual parallel data obstructs its performance under low-resource conditions. Building an effective model on low resource data or even in an unsupervised way is always an interesting and challenging research topic BIBREF5, BIBREF6, BIBREF7. Recently, unsupervised MT BIBREF8, BIBREF9, BIBREF0, BIBREF10, BIBREF11, which can immensely reduce the reliance on parallel corpora, has been gaining more and more interest.
> 
> Training cross-lingual word embeddings BIBREF0, BIBREF12 is always the first step of the unsupervised MT models which produce a word-level shared embedding space for both the source and target, but the lexical coverage can be an intractable problem. To tackle this issue, BIBREF13 provided a subword-level solution to overcome the out-of-vocabulary (OOV) problem.
> 
> In this work, the systems we implement for the German-Czech language pair are built based on the previously proposed unsupervised MT systems, with some adaptations made to accommodate the morphologically rich characteristics of German and Czech BIBREF14. Both word-level and subword-level neural machine translation (NMT) models are applied in this task and further tuned by pseudo-parallel data generated from a phrase-based statistical machine translation (PBSMT) model, which is trained following the steps proposed in BIBREF10 without using any parallel data. We propose to train BPE embeddings for German and Czech separately and align those trained embeddings into a shared space with MUSE BIBREF0 to reduce the combinatorial explosion of word forms for both languages. To ensure the fluency and consistency of translations, an additional Czech language model is trained to select the translation candidates generated through beam search by rescoring them. Besides the above, a series of post-processing steps are applied to improve the quality of final translations. Our contribution is two-fold:
> 
> We propose a method to combine word and subword (BPE) pre-trained input representations aligned using MUSE BIBREF0 as an NMT training initialization on a morphologically-rich language pair such as German and Czech.
> 
> We study the effectiveness of language model rescoring to choose the best sentences and unknown word replacement (UWR) procedure to reduce the drawback of OOV words.
> 
> This paper is organized as follows: in Section SECREF2, we

#### Relevance 1116

Label: 

#### Passage 1118

Retrieved by: BM25

> For all the models mentioned above that work under a lower-case setting, a recaser implemented with Moses BIBREF22 is applied to convert the translations to the real cases.

#### Relevance 1118

Label: 

### Dense

#### Passage 1120

Retrieved by: Dense

> Step 2 and Step 3 are repeated until all the context words have been searched. After removing all the punctuation and the context words in the candidate list, the replacement word is the one that most frequently appears in the candidate list. If no candidate word is found, we just remove the <UNK> without adding a word.

#### Relevance 1120

Label: 

#### Passage 1121

Retrieved by: Dense

> We further fine-tune the NMT models mentioned above on the pseudo-parallel data generated by a PBSMT model. We choose the best PBSMT model and mix the pseudo-parallel data from the NMT models and the PBSMT model, which are used for back-translation. The intuition is that we can use the pseudo-parallel data produced by the PBSMT model as the supplementary translations in our NMT model, and these can potentially boost the robustness of the NMT model by increasing the variety of back-translation data.

#### Relevance 1121

Label: 

### Hybrid

#### Passage 1122

Retrieved by: Hybrid

> The settings of the word-level NMT and subword-level NMT are the same, except the vocabulary size. We use a vocabulary size of 50k in the word-level NMT setting and 40k in the subword-level NMT setting for both German and Czech. In the encoder and decoder, we use a transformer BIBREF3 with four layers and a hidden size of 512. We share all encoder parameters and only share the first decoder layer across two languages to ensure that the latent representation of the source sentence is robust to the source language. We train auto-encoding and back-translation during each iteration. As the training goes on, the importance of language modeling become a less important compared to back-translation. Therefore the weight of auto-encoding ($\lambda $ in equation (DISPLAY_FORM7)) is decreasing during training.

#### Relevance 1122

Label: 

## Question 0147

Paper: Quoref: A Reading Comprehension Dataset with Questions Requiring Coreferential Reasoning

> What crowdsourcing platform did they obtain the data from?

### Common Retrieved Chunks

#### Passage 1123

Retrieved by: BM25, Dense, Hybrid

> Unlike traditional coreference annotations in datasets like those of BIBREF4, BIBREF10, BIBREF11 and BIBREF7, which aim to obtain complete coreference clusters, our questions require understanding coreference between only a few spans. While this means that the notion of coreference captured by our dataset is less comprehensive, it is also less conservative and allows questions about coreference relations that are not marked in OntoNotes annotations. Since the notion is not as strict, it does not require linguistic expertise from annotators, making it more amenable to crowdsourcing.

#### Relevance 1123

Label: 

#### Passage 1124

Retrieved by: BM25, Dense, Hybrid

> We crowdsourced questions about these paragraphs on Mechanical Turk. We asked workers to find two or more co-referring spans in the paragraph, and to write questions such that answering them would require the knowledge that those spans are coreferential. We did not ask them to explicitly mark the co-referring spans. Workers were asked to write questions for a random sample of paragraphs from our pool, and we showed them examples of good and bad questions in the instructions (see Appendix ). For each question, the workers were also required to select one or more spans in the corresponding paragraph as the answer, and these spans are not required to be same as the coreferential spans that triggered the questions. We used an uncased base BERT QA model BIBREF9 trained on SQuAD 1.1 BIBREF0 as an adversary running in the background that attempted to answer the questions written by workers in real time, and the workers were able to submit their questions only if their answer did not match the adversary's prediction. Appendix further details the logistics of the crowdsourcing tasks. Some basic statistics of the resulting dataset can be seen in Table .

#### Relevance 1124

Label: 

#### Passage 1125

Retrieved by: BM25, Dense, Hybrid

> Paragraphs and other longer texts typically make multiple references to the same entities. Tracking these references and resolving coreference is essential for full machine comprehension of these texts. Significant progress has recently been made in reading comprehension research, due to large crowdsourced datasets BIBREF0, BIBREF1, BIBREF2, BIBREF3. However, these datasets focus largely on understanding local predicate-argument structure, with very few questions requiring long-distance entity tracking. Obtaining such questions is hard for two reasons: (1) teaching crowdworkers about coreference is challenging, with even experts disagreeing on its nuances BIBREF4, BIBREF5, BIBREF6, BIBREF7, and (2) even if we can get crowdworkers to target coreference phenomena in their questions, these questions may contain giveaways that let models arrive at the correct answer without performing the desired reasoning (see §SECREF3 for examples).
> 
> We introduce a new dataset, Quoref , that contains questions requiring coreferential reasoning (see examples in Figure FIGREF1). The questions are derived from paragraphs taken from a diverse set of English Wikipedia articles and are collected using an annotation process (§SECREF2) that deals with the aforementioned issues in the following ways: First, we devise a set of instructions that gets workers to find anaphoric expressions and their referents, asking questions that connect two mentions in a paragraph. These questions mostly revolve around traditional notions of coreference (Figure FIGREF1 Q1), but they can also involve referential phenomena that are more nebulous (Figure FIGREF1 Q3). Second, inspired by BIBREF8, we disallow questions that can be answered by an adversary model (uncased base BERT, BIBREF9, trained on SQuAD 1.1, BIBREF0) running in the background as the workers write questions. This adversary is not particularly skilled at answering questions requiring coreference, but can follow obvious lexical cues—it thus helps workers avoid writing questions that shortcut coreferential reasoning.
> 
> Quoref contains more than 15K questions whose answers are spans or sets of spans in 3.5K paragraphs from English Wikipedia that can be arrived at by resolving coreference in those paragraphs. We manually analyze a sample of the dataset (§SECREF3) and find that 78% of the questions cannot be answered without resolving coreference. We also show (§SECREF4) that the best system performance is 49.1% $F_1$, while the estimated human performance is 87.2%. These findings

#### Relevance 1125

Label: 

#### Passage 1126

Retrieved by: BM25, Hybrid

> We scraped paragraphs from Wikipedia pages about English movies, art and architecture, geography, history, and music. For movies, we followed the list of English language films, and extracted plot summaries that are at least 40 tokens, and for the remaining categories, we followed the lists of featured articles. Since movie plot summaries usually mention many characters, it was easier to find hard Quoref questions for them, and we sampled about 60% of the paragraphs from this category.

#### Relevance 1126

Label: 

#### Passage 1128

Retrieved by: Dense, Hybrid

> To better understand the phenomena present in Quoref , we manually analyzed a random sample of 100 paragraph-question pairs. The following are some empirical observations.

#### Relevance 1128

Label: 

### BM25

#### Passage 1127

Retrieved by: BM25

> We found that 78% of the manually analyzed questions cannot be answered without coreference resolution. The remaining 22% involve some form of coreference, but do not require it to be resolved for answering them. Examples include a paragraph that mentions only one city, “Bristol”, and a sentence that says “the city was bombed”. The associated question, Which city was bombed?, does not really require coreference resolution from a model that can identify city names, making the content in the question after Which city unnecessary.

#### Relevance 1127

Label: 

### Dense

#### Passage 1129

Retrieved by: Dense

> We present Quoref , a focused reading comprehension benchmark that evaluates the ability of models to resolve coreference. We crowdsourced questions over paragraphs from Wikipedia, and manual analysis confirmed that most cannot be answered without coreference resolution. We show that current state-of-the-art reading comprehension models perform poorly on this benchmark, significantly lower than human performance. Both these findings provide evidence that Quoref is an appropriate benchmark for coreference-aware reading comprehension.

#### Relevance 1129

Label: 

### Hybrid

None

## Question 0148

Paper: Adversarial Training for Aspect-Based Sentiment Analysis with BERT

> How are adversarial examples generated?

### Common Retrieved Chunks

#### Passage 1130

Retrieved by: BM25, Hybrid

> Understanding what people are talking about and how they feel about it is valuable especially for industries which need to know the customers' opinions on their products. Aspect-Based Sentiment Analysis (ABSA) is a branch of sentiment analysis which deals with extracting the opinion targets (aspects) as well as the sentiment expressed towards them. For instance, in the sentence The spaghetti was out of this world., a positive sentiment is mentioned towards the target which is spaghetti. Performing these tasks requires a deep understanding of the language. Traditional machine learning methods such as SVM BIBREF2, Naive Bayes BIBREF3, Decision Trees BIBREF4, Maximum Entropy BIBREF5 have long been practiced to acquire such knowledge. However, in recent years due to the abundance of available data and computational power, deep learning methods such as CNNs BIBREF6, BIBREF7, BIBREF8, RNNs BIBREF9, BIBREF10, BIBREF11, and the Transformer BIBREF12 have outperformed the traditional machine learning techniques in various tasks of sentiment analysis. Bidirectional Encoder Representations from Transformers (BERT) BIBREF13 is a deep and powerful language model which uses the encoder of the Transformer in a self-supervised manner to learn the language model. It has been shown to result in state-of-the-art performances on the GLUE benchmark BIBREF14 including text classification. BIBREF1 show that adding domain-specific information to this model can enhance its performance in ABSA. Using their post-trained BERT (BERT-PT), we add adversarial examples to further improve BERT's performance on Aspect Extraction (AE) and Aspect Sentiment Classification (ASC) which are two major tasks in ABSA. A brief overview of these two sub-tasks is given in Section SECREF3.
> 
> Adversarial examples are a way of fooling a neural network to behave incorrectly BIBREF15. They are created by applying small perturbations to the original inputs. In the case of images, the perturbations can be invisible to human eye, but can cause neural networks to output a completely different response from the true one. Since neural nets make mistakes on these examples, introducing them to the network during the training can improve their performance. This is called adversarial training which acts as a regularizer to help the network generalize better BIBREF0. Due to the discrete nature of text, it is not feasible to produce perturbed examples from

#### Relevance 1130

Label: 

#### Passage 1131

Retrieved by: BM25, Dense, Hybrid

> Our model is depicted in Figure FIGREF1. As can be seen, we create adversarial examples from BERT embeddings using the gradient of the loss. Then, we feed the perturbed examples to the BERT encoder to calculate the adversarial loss. In the end, the backpropagation algorithm is applied to the sum of both losses.
> 
> BERT Word Embedding Layer. The calculation of input embeddings in BERT is carried out using three different embeddings. As shown in Figure FIGREF2, it is computed by summing over token, segment, and position embeddings. Token embedding is the vector representation of each token in the vocabulary which is achieved using WordPiece embeddings BIBREF31. Position embeddings are used to preserve the information about the position of the words in the sentence. Segment embeddings are used in order to distinguish between sentences if there is more than one (e.g. for question answering task there are two). Words belonging to one sentence are labeled the same.
> 
> BERT Encoder. BERT encoder is constructed by making use of Transformer blocks from the Transformer model. For $\mathbf {BERT_{BASE}}$, these blocks are used in 12 layers, each of which consists of 12 multi-head attention blocks. In order to make the model aware of both previous and future contexts, BERT uses the Masked Language Model (MLM) where $15\%$ of the input sentence is masked for prediction.
> 
> Fully Connected Layer and Loss Function. The job of the fully connected layer in the architecture is to classify the output embeddings of BERT encoder into sentiment classes. Therefore, its size is $768\times 3$ where the first element is the hidden layers' size of BERT encoder and the second element is the number of classes. For the loss function, we use cross entropy loss implemented in Pytorch.
> 
> Adversarial Examples. Adversarial examples are created to attack a neural network to make erroneous predictions. There are two main types of adversarial attacks which are called white-box and black-box. White-box attacks BIBREF32 have access to the model parameters, while black-box attacks BIBREF33 work only on the input and output. In this work, we utilize a white-box method working on the embedding level. In order to create adversarial examples, we utilize the formula used by BIBREF16, where the

#### Relevance 1131

Label: 

#### Passage 1132

Retrieved by: BM25, Dense, Hybrid

> parameters, while black-box attacks BIBREF33 work only on the input and output. In this work, we utilize a white-box method working on the embedding level. In order to create adversarial examples, we utilize the formula used by BIBREF16, where the perturbations are created using gradient of the loss function. Assuming $p(y|x;\theta )$ is the probability of label $y$ given the input $x$ and the model parameters $\theta $, in order to find the adversarial examples the following minimization problem should be solved:
> 
> where $r$ denotes the perturbations on the input and $\hat{\theta }$ is a constant copy of $\theta $ in order not to allow the gradients to propagate in the process of constructing the artificial examples. Solving the above minimization problem means that we are searching for the worst perturbations while trying to minimize the loss of the model. An approximate solution for Equation DISPLAY_FORM3 is found by linearizing $\log p(y|x;\theta )$ around $x$ BIBREF0. Therefore, the following perturbations are added to the input embeddings to create new adversarial sentences in the embedding space.
> 
> where
> 
> and $\epsilon $ is the size of the perturbations. In order to find values which outperform the original results, we carried out an ablation study on five values for epsilon whose results are presented in Figure FIGREF7 and discussed in Section SECREF6. After the adversarial examples go through the network, their loss is calculated as follows:
> 
> $- \log p(y|x + r_{adv};\theta )$
> 
> Then, this loss is added to the loss of the real examples in order to compute the model's loss.

#### Relevance 1132

Label: 

#### Passage 1133

Retrieved by: BM25, Dense, Hybrid

> In this paper, we introduced the application of adversarial training in Aspect-Based Sentiment Analysis. The experiments with our proposed architecture show that the performance of the post-trained BERT on aspect extraction and aspect sentiment classification tasks are improved by utilizing adversarial examples during the network training. As future work, other white-box adversarial examples as well as black-box ones will be utilized for a comparison of adversarial training methods for various sentiment analysis tasks. Furthermore, the impact of adversarial training in the other tasks in ABSA namely Aspect Category Detection and Aspect Category Polarity will be investigated.

#### Relevance 1133

Label: 

#### Passage 1134

Retrieved by: BM25, Dense, Hybrid

> during the training can improve their performance. This is called adversarial training which acts as a regularizer to help the network generalize better BIBREF0. Due to the discrete nature of text, it is not feasible to produce perturbed examples from the original inputs. As a workaround, BIBREF16 apply this technique to the word embedding space for text classification. Inspired by them and building on the work of BIBREF1, we experiment with adversarial training for ABSA.
> 
> Our contributions are twofold. First, by carrying out an ablation study on the number of training epochs and the values for dropout in the classification layer, we show that there are values that outperform the specified ones for BERT-PT. Second, we introduce the application of adversarial training in ABSA by proposing a novel architecture which combines adversarial training with the BERT language model for AE and ASC tasks. Our experiments show that the proposed model outperforms the best performance of BERT-PT in both tasks.

#### Relevance 1134

Label: 

### BM25

None

### Dense

#### Passage 1135

Retrieved by: Dense

> (STN) which highlights more important information with respect to a given aspect. BIBREF29 approach the aspect extraction in an unsupervised way. Functioning the same way as an autoencoder, their model has been designed to reconstruct sentence embeddings in which aspect-related words are given higher weights through attention mechanism.
> 
> While adversarial training has been utilized for sentence classification BIBREF16, its effects have not been studied in ABSA. Therefore, in this work, we study the impact of applying adversarial training to the powerful BERT language model.

#### Relevance 1135

Label: 

### Hybrid

None

## Question 0149

Paper: Dice Loss for Data-imbalanced NLP Tasks

> What are method's improvements of F1 w.r.t. baseline BERT tagger for Chinese POS datasets?

### Common Retrieved Chunks

#### Passage 1136

Retrieved by: BM25, Dense, Hybrid

> Table shows experimental results on NER datasets. For English datasets including CoNLL2003 and OntoNotes5.0, our proposed method outperforms BERT-MRCBIBREF38 by +0.29 and +0.96 respectively. We observe huge performance boosts on Chinese datasets, achieving F1 improvements by +0.97 and +2.36 on MSRA and OntoNotes4.0, respectively. As far as we are concerned, we are setting new SOTA performances on all of the four NER datasets.

#### Relevance 1136

Label: 

#### Passage 1137

Retrieved by: BM25, Dense, Hybrid

> Table presents the experimental results on the POS task. As can be seen, the proposed DSC loss outperforms the best baseline results by a large margin, i.e., outperforming BERT-tagger by +1.86 in terms of F1 score on CTB5, +1.80 on CTB6 and +2.19 on UD1.4. As far as we are concerned, we are achieving SOTA performances on the three datasets. Weighted cross entropy and focal loss only gain a little performance improvement on CTB5 and CTB6, and the dice loss obtains huge gain on CTB5 but not on CTB6, which indicates the three losses are not consistently robust in resolving the data imbalance issue. The proposed DSC loss performs robustly on all the three datasets.

#### Relevance 1137

Label: 

#### Passage 1138

Retrieved by: BM25, Dense, Hybrid

> We use the following baselines:
> 
> Joint-POS: shao2017character jointly learns Chinese word segmentation and POS.
> 
> Lattice-LSTM: lattice2018zhang constructs a word-character lattice.
> 
> Bert-Tagger: devlin2018bert treats part-of-speech as a tagging task.

#### Relevance 1138

Label: 

#### Passage 1139

Retrieved by: BM25, Dense, Hybrid

> Part-of-speech tagging (POS) is the task of assigning a label (e.g., noun, verb, adjective) to each word in a given text. In this paper, we choose BERT as the backbone and conduct experiments on three Chinese POS datasets. We report the span-level micro-averaged precision, recall and F1 for evaluation. Hyperparameters are tuned on the corresponding development set of each dataset.

#### Relevance 1139

Label: 

#### Passage 1140

Retrieved by: BM25, Dense, Hybrid

> We use the following baselines:
> 
> ELMo: a tagging model from peters2018deep.
> 
> Lattice-LSTM: lattice2018zhang constructs a word-character lattice, only used in Chinese datasets.
> 
> CVT: from kevin2018cross, which uses Cross-View Training(CVT) to improve the representations of a Bi-LSTM encoder.
> 
> Bert-Tagger: devlin2018bert treats NER as a tagging task.
> 
> Glyce-BERT: wu2019glyce combines glyph information with BERT pretraining.
> 
> BERT-MRC: The current SOTA model for both Chinese and English NER datasets proposed by xiaoya2019ner, which formulate NER as machine reading comprehension task.

#### Relevance 1140

Label: 

### BM25

None

### Dense

None

### Hybrid

None

## Question 0150

Paper: Going Beneath the Surface: Evaluating Image Captioning for Grammaticality, Truthfulness and Diversity

> Which existing models are evaluated?

### Common Retrieved Chunks

#### Passage 1141

Retrieved by: BM25, Dense, Hybrid

> Evaluation metrics are required as a proxy for performance in real applications. As such, they should, as far as possible, allow measurement of fundamental aspects of the performance of models on tasks. In this work, we propose the GTD evaluation framework as a supplement to standard image captioning evaluation which explicitly focuses on grammaticality, truthfulness and diversity. We developed the ShapeWorldICE evaluation suite to allow in-depth and fine-grained inspection of model behaviors. We have empirically verified that GTD captures different aspects of performance to existing metrics by evaluating image captioning models on the ShapeWorldICE suite. We hope that this framework will shed light on important aspects of model behaviour and that this will help guide future research efforts.
> 
> While performing the evaluation experiments on the LRCN1u model, we noticed that caption agreement does not always improve as the training loss decreases. Ideally, the training objective should be in accordance with how a model is eventually evaluated. In future work, we plan to investigate the feasibility of deliberately encoding the GTD signal in the training process, for instance, by implementing a GTD-aware loss. We also plan to extend the existing ShapeWorldICE benchmark to include more linguistic constructions (such as relative clauses, compound sentences and coreference). By doing so, we hope to reveal how well existing image captioning models cope with complex generation tasks.

#### Relevance 1141

Label: 

#### Passage 1142

Retrieved by: BM25, Hybrid

> using a set of reference captions to approximate the content of an image. We argue that, while existing metrics have undeniably been useful for real-world captioning evaluation, their focus on approximate surface comparison limits deeper insights into the learning process and eventual behavior of captioning models.
> 
> To address this problem, we propose a set of principled evaluation criteria which evaluate image captioning models for grammaticality, truthfulness and diversity (GTD). These criteria correspond to necessary requirements for image captioning systems: (a) that the output is grammatical, (b) that the output statement is true with respect to the image, and (c) that outputs are diverse and mirror the variability of training captions.
> 
> Practical evaluation of GTD is currently only possible on synthetic data. We construct a range of datasets designed for image captioning evaluation. We call this diagnostic evaluation benchmark ShapeWorldICE (ShapeWorld for Image Captioning Evaluation). We illustrate the evaluation of specific image captioning models on ShapeWorldICE. We empirically demonstrate that the existing metrics BLEU and SPICE do not capture true caption-image agreement in all scenarios, while the GTD framework allows a fine-grained investigation of how well existing models cope with varied visual situations and linguistic constructions.
> 
> We believe that as a supplementary evaluation method to real-world metrics, the GTD framework provides evaluation insights that are sufficiently interesting to motivate future work.

#### Relevance 1142

Label: 

#### Passage 1143

Retrieved by: BM25, Dense, Hybrid

> We develop a variety of ShapeWorldICE datasets, with a similar idea to the “skill tasks” in the bAbI framework BIBREF22. Table TABREF4 gives an overview for different ShapeWorldICE datasets we use in this paper. We consider three different types of captioning tasks, each of which focuses on a distinct aspect of reasoning abilities. Existential descriptions examine whether a certain object is present in an image. Spatial descriptions identify spatial relationships among visual objects. Quantification descriptions involve count-based and ratio-based statements, with an explicit focus on inspecting models for their counting ability. We develop two variants for each type of dataset to enable different levels of visual complexity or specific aspects of the same reasoning type. All the training and test captions sampled in this work are in English.
> 
> Each dataset variant consists of around 200k training instances and 4,096 validation instances, plus 4,096 test instances. Each training instance consists of an image and a reference caption. At test time, only the test images are available to the evaluated models. Underlying world models are kept from the models and are used for later GTD evaluation. For each test instance, we sample ten reference captions of the same distribution as the training captions to enable the comparison of our proposed metrics to BLEU and SPICE. We fine-tune our model hyperparameters based on the performance on the validation set. All reported results are measured on the test split with the parameters yielding the best validation performance.

#### Relevance 1143

Label: 

#### Passage 1146

Retrieved by: Dense, Hybrid

> Recently, many synthetic datasets have been proposed as diagnostic tools for deep learning models, such as CLEVR BIBREF21 for visual question answering (VQA), the bAbI tasks BIBREF22 for text understanding and reasoning, and ShapeWorld BIBREF11 for visually grounded language understanding. The primary motivation is to reduce complexity which is considered irrelevant to the evaluation focus, to enable better control over the data, and to provide more detailed insights into strengths and limitations of existing models.
> 
> In this work, we develop the evaluation datasets within the ShapeWorld framework. ShapeWorld is a controlled data generation framework consisting of abstract colored shapes (see Figure FIGREF1 for an example). We use ShapeWorld to generate training and evaluation data for two major reasons. ShapeWorld supports customized data generation according to user specification, which enables a variety of model inspections in terms of language construction, visual complexity and reasoning ability. Another benefit is that each training and test instance generated in ShapeWorld is returned as a triplet of $<$image, caption, world model$>$. The world model stores information about the underlying microworld used to generate an image and a descriptive caption, internally represented as a list of entities with their attributes, such as shape, color, position. During data generation, ShapeWorld randomly samples a world model from a set of available entities and attributes. The generated world model is then used to realize a corresponding instance consisting of image and caption. The world model gives the actual semantic information contained in an image, which allows evaluation of caption truthfulness.

#### Relevance 1146

Label: 

#### Passage 1148

Retrieved by: Dense, Hybrid

> An essential criterion for an image captioning model is that the captions generated are grammatically well-formed. Fully accurate assessment of grammaticality in a general context is itself a difficult task, but becomes more feasible in a very constrained context like our diagnostic language data. We take parseability with the English Resource Grammar BIBREF23 as a surrogate for grammaticality, meaning that a sentence is considered grammatically well-formed if we obtain a parse using the ERG.
> 
> The ERG is a broad-coverage grammar based on the head-driven phrase structure grammar (HPSG) framework. It is linguistically precise: sentences only parse if they are valid according to its hand-built rules. It is designed to be general-purpose: verified coverage is around 80% for Wikipedia, and over 90% for corpora with shorter sentences and more limited vocabulary (for details see BIBREF24 flickinger2011accuracy). Since the ShapeWorld training data – the only language source for models to learn from – is generated using the same grammar, the ERG has $\sim $100% coverage of grammaticality in the model output space.

#### Relevance 1148

Label: 

### BM25

#### Passage 1144

Retrieved by: BM25

> Automatically generating text to describe the content of images, also known as image captioning, is a multimodal task of considerable interest in both the computer vision and the NLP communities. Image captioning can be framed as a translation task from an image to a descriptive natural language statement. Many existing captioning models BIBREF0, BIBREF1, BIBREF2, BIBREF3 follow the typical encoder-decoder framework where a convolutional network is used to condense images into visual feature representations, combined with a recurrent network for language generation. While these models demonstrate promising results, quantifying image captioning performance remains a challenging problem, in a similar way to other generative tasks BIBREF4, BIBREF5.
> 
> Evaluating candidate captions for human preference is slow and laborious. To alleviate this problem, many automatic evaluation metrics have been proposed, such as BLEU BIBREF6, METEOR BIBREF7, ROUGE BIBREF8 and CIDEr BIBREF9. These n-gram-based metrics evaluate captioning performance based on surface similarity between a candidate caption and reference statements. A more recent evaluation metric for image captioning is SPICE BIBREF10, which takes into account semantic propositional content of generated captions by scoring a caption based upon a graph-based semantic representation transformed from reference captions.
> 
> The rationale behind these evaluation metrics is that human reference captions serve as an approximate target and comparing model outputs to this target is a proxy for how well a system performs. Thus, a candidate caption is not directly evaluated with respect to image content, but compared to a set of human statements about that image.
> 
> However, in image captioning, visual scenes with multiple objects and relations correspond to a diversity of valid descriptions. Consider the example image and captions from the ShapeWorld framework BIBREF11 shown in Figure FIGREF1. The first three captions are true statements about the image and express relevant ideas, but describe different objects, attributes and spatial relationships, while the fourth caption is wrong despite referring to the same objects as in the third caption. This casts doubt on the sufficiency of using a set of reference captions to approximate the content of an image. We argue that, while existing metrics have undeniably been useful for real-world captioning evaluation, their focus on approximate surface comparison limits deeper insights into the learning process

#### Relevance 1144

Label: 

#### Passage 1145

Retrieved by: BM25

> While grammaticality and truthfulness are essential requirements for image captions, these criteria alone can easily be “gamed” by specializing on a small set of generic statements which are true most of the time. In the context of abstract shapes, such captions include examples like “There is a shape” or “At least zero shapes are blue” (which is technically true even if there is no blue shape). This motivates the third fundamental requirement of captioning output to be diverse.
> 
> As ShapeWorldICE exploits a limited size of open-class words, we emphasize the diversity in ShapeWorldICE at the sentence level rather than the word level. Since the ground-truth reference captions in ShapeWorld are randomly sampled, we take the sampled captions accompanying the test images as a proxy for optimal caption diversity, and compare it with the empirical output diversity of the evaluated model on these test images. Practically, we look at language constructions used and compute the corresponding diversity score as the ratio of observed number versus optimal number:
> 
> Language constructions here correspond to reduced caption representations which only record whether an object is described by shape (e.g., “square”), color (e.g., “red shape”) or color-shape combination (e.g., “red square”). So the statement “A square is red” and “A circle is blue” are considered the same, while “A shape is red” is different.

#### Relevance 1145

Label: 

### Dense

#### Passage 1147

Retrieved by: Dense

> We train and evaluate the Show&Tell and LRCN1u models on the ShapeWorldICE datasets. Here we discuss in detail the diagnostic results of these experiments. During training, we periodically record model output on the test images, to be able to analyze the development of our evaluation metrics throughout the process. We also compute BLEU-4 scores and SPICE scores of generated captions for comparison, using 10 reference captions per test image.
> 
> LRCN1u exhibits clearly superior performance in terms of truthfulness. We start off by comparing performance of the Show&Tell model and the LRCN1u model, see Figure FIGREF8. While both models learn to produce grammatical sentences early on, it can be seen that LRCN1u is clearly superior in terms of truthfulness, achieving 100% halfway through training, whereas Show&Tell only slowly reaches around 90% by the end of 100k iterations. This indicates that incorporating visual features at every generation step is beneficial for producing true captions. The diversity ratios of captions generated by two models both increase substantially as the training progresses, with LRCN1u exhibiting a slightly greater caption diversity at the end of training.
> 
> We observed similar results on other ShapeWorldICE datasets that we experimented with, validating the superiority of LRCN1u over Show&Tell on ShapeWorldICE. Consequently, we decided to focus on the LRCN1u architecture in subsequent evaluations, where we report detailed results with respect to the GTD framework on a variety of datasets.
> 
> Correlation between the BLEU/SPICE scores and the ground truth. From the learning curves shown in Figure FIGREF9, we find low or no correlation between the BLEU/SPICE scores and caption truthfulness.
> 
> On Existential-OneShape, the BLEU curve follows the trend of the truthfulness curve in general, indicating that BLEU is able to capture caption truthfulness well in this simple scenario. However, while BLEU reports equivalent model performance on Existential-MultiShapes and Spatial-MultiShapes, the truthfulness metric demonstrates very different results. The BLEU score for generated Existential-MultiShapes captions increases rapidly at the beginning of training and then plateaus despite the continuous increase in truthfulness ratio. Captions generated on Spatial-MultiShapes attain a relatively high BLEU score from an early stage of training, but exhibit low agreement ($<$0.6 truthfulness ratio) with ground-truth visual scenes. In the case of Spatial-MultiShapes, spatial descriptors for

#### Relevance 1147

Label: 

### Hybrid

None

## Question 0151

Paper: Improving Distributed Representations of Tweets - Present and Future

> How do they encourage understanding of literature as part of their objective function?

### Common Retrieved Chunks

#### Passage 1149

Retrieved by: BM25, Hybrid

> Twitter is a widely used microblogging platform, where users post and interact with messages, “tweets”. Understanding the semantic representation of tweets can benefit a plethora of applications such as sentiment analysis BIBREF0 , BIBREF1 , hashtag prediction BIBREF2 , paraphrase detection BIBREF3 and microblog ranking BIBREF4 , BIBREF5 . However, tweets are difficult to model as they pose several challenges such as short length, informal words, unusual grammar and misspellings. Recently, researchers are focusing on leveraging unsupervised representation learning methods based on neural networks to solve this problem. Once these representations are learned, we can use off-the-shelf predictors taking the representation as input to solve the downstream task BIBREF6 , BIBREF7 . These methods enjoy several advantages: (1) they are cheaper to train, as they work with unlabelled data, (2) they reduce the dependence on domain level experts, and (3) they are highly effective across multiple applications, in practice.
> 
> Despite this, there is a lack of prior work which surveys the tweet-specific unsupervised representation learning models. In this work, we attempt to fill this gap by investigating the models in an organized fashion. Specifically, we group the models based on the objective function it optimizes. We believe this work can aid the understanding of the existing literature. We conclude the paper by presenting interesting future research directions, which we believe are fruitful in advancing this field by building high-quality tweet representation learning models.

#### Relevance 1149

Label: 

#### Passage 1150

Retrieved by: BM25, Hybrid

> There are various models spanning across different model architectures and objective functions in the literature to compute tweet representation in an unsupervised fashion. These models work in a semi-supervised way - the representations generated by the model is fed to an off-the-shelf predictor like Support Vector Machines (SVM) to solve a particular downstream task. These models span across a wide variety of neural network based architectures including average of word vectors, convolutional-based, recurrent-based and so on. We believe that the performance of these models is highly dependent on the objective function it optimizes – predicting adjacent word (within-tweet relationships), adjacent tweet (inter-tweet relationships), the tweet itself (autoencoder), modeling from structured resources like paraphrase databases and weak supervision. In this section, we provide the first of its kind survey of the recent tweet-specific unsupervised models in an organized fashion to understand the literature. Specifically, we categorize each model based on the optimized objective function as shown in Figure FIGREF1 . Next, we study each category one by one.

#### Relevance 1150

Label: 

#### Passage 1151

Retrieved by: BM25, Dense, Hybrid

> In this work we study the problem of learning unsupervised tweet representations. We believe our survey of the existing works based on the objective function can give vital perspectives to researchers and aid their understanding of the field. We also believe the future research directions studied in this work can help in breaking the barriers in building high quality, general purpose tweet representation models.

#### Relevance 1151

Label: 

#### Passage 1152

Retrieved by: BM25, Dense, Hybrid

> Motivation: In recent times, building representation models based on supervision from richly structured resources such as Paraphrase Database (PPDB) BIBREF19 (containing noisy phrase pairs) has yielded high quality sentence representations. These methods work by maximizing the similarity of the sentences in the learned semantic space.
> 
> Models: CHARAGRAM BIBREF20 embeds textual sequences by learning a character-based compositional model that involves addition of the vectors of its character n-grams followed by an elementwise nonlinearity. This simpler architecture trained on PPDB is able to beat models with complex architectures like CNN, LSTM on SemEval 2015 Twitter textual similarity task by a large margin. This result emphasizes the importance of character-level models that address differences due to spelling variation and word choice. The authors in their subsequent work BIBREF21 conduct a comprehensive analysis of models spanning the range of complexity from word averaging to LSTMs for its ability to do transfer and supervised learning after optimizing a margin based loss on PPDB. For transfer learning, they find models based on word averaging perform well on both the in-domain and out-of-domain textual similarity tasks, beating LSTM model by a large margin. On the other hand, the word averaging models perform well for both sentence similarity and textual entailment tasks, outperforming the LSTM. However, for sentiment classification task, they find LSTM (trained on PPDB) to beat the averaging models to establish a new state of the art. The above results suggest that structured resources play a vital role in computing general-purpose embeddings useful in downstream applications.

#### Relevance 1152

Label: 

#### Passage 1153

Retrieved by: BM25, Dense, Hybrid

> Motivation: Every tweet is assumed to have a latent topic vector, which influences the distribution of the words in the tweet. For example, though the appearance of the phrase catch the ball is frequent in the corpus, if we know that the topic of a tweet is about “technology”, we can expect words such as bug or exception after the word catch (ignoring the) instead of the word ball since catch the bug/exception is more plausible under the topic “technology”. On the other hand, if the topic of the tweet is about “sports”, then we can expect ball after catch. These intuitions indicate that the prediction of neighboring words for a given word strongly relies on the tweet also.
> 
> Models: BIBREF8 's work is the first to exploit this idea to compute distributed document representations that are good at predicting words in the document. They propose two models: PV-DM and PV-DBOW, that are extensions of Continuous Bag Of Words (CBOW) and Skip-gram model variants of the popular Word2Vec model BIBREF9 respectively – PV-DM inserts an additional document token (which can be thought of as another word) which is shared across all contexts generated from the same document; PV-DBOW attempts to predict the sampled words from the document given the document representation. Although originally employed for paragraphs and documents, these models work better than the traditional models: BOW BIBREF10 and LDA BIBREF11 for tweet classification and microblog retrieval tasks BIBREF12 . The authors in BIBREF12 make the PV-DM and PV-DBOW models concept-aware (a rich semantic signal from a tweet) by augmenting two features: attention over contextual words and conceptual tweet embedding, which jointly exploit concept-level senses of tweets to compute better representations. Both the discussed works have the following characteristics: (1) they use a shallow architecture, which enables fast training, (2) computing representations for test tweets requires computing gradients, which is time-consuming for real-time Twitter applications, and (3) most importantly, they fail to exploit textual information from related tweets that can bear salient semantic signals.

#### Relevance 1153

Label: 

### BM25

None

### Dense

#### Passage 1154

Retrieved by: Dense

> In this section we present the future research directions which we believe can be worth pursuing to generate high quality tweet embeddings.

#### Relevance 1154

Label: 

#### Passage 1155

Retrieved by: Dense

> Motivation: To capture rich tweet semantics, researchers are attempting to exploit a type of sentence-level Distributional Hypothesis BIBREF10 , BIBREF13 . The idea is to infer the tweet representation from the content of adjacent tweets in a related stream like users' Twitter timeline, topical, retweet and conversational stream. This approach significantly alleviates the context insufficiency problem caused due to the ambiguous and short nature of tweets BIBREF0 , BIBREF14 .
> 
> Models: Skip-thought vectors BIBREF15 (STV) is a widely popular sentence encoder, which is trained to predict adjacent sentences in the book corpus BIBREF16 . Although the testing is cheap as it involves a cheap forward propagation of the test sentence, STV is very slow to train thanks to its complicated model architecture. To combat this computational inefficiency, FastSent BIBREF17 propose a simple additive (log-linear) sentence model, which predicts adjacent sentences (represented as BOW) taking the BOW representation of some sentence in context. This model can exploit the same signal, but at a much lower computational expense. Parallel to this work, Siamase CBOW BIBREF18 develop a model which directly compares the BOW representation of two sentence to bring the embeddings of a sentence closer to its adjacent sentence, away from a randomly occurring sentence in the corpus. For FastSent and Siamese CBOW, the test sentence representation is a simple average of word vectors obtained after training. Both of these models are general purpose sentence representation models trained on book corpus, yet give a competitive performance over previous models on the tweet semantic similarity computation task. BIBREF14 's model attempt to exploit these signals directly from Twitter. With the help of attention technique and learned user representation, this log-linear model is able to capture salient semantic information from chronologically adjacent tweets of a target tweet in users' Twitter timeline.

#### Relevance 1155

Label: 

### Hybrid

None

## Question 0152

Paper: Building a Massive Corpus for Named Entity Recognition Using Free Open Data Sources

> Does the SESAME dataset include discontiguous entities?

### Common Retrieved Chunks

#### Passage 1158

Retrieved by: BM25, Dense, Hybrid

> By following the above methodology on the Portuguese Wikipedia and DBpedia, we create a massive silver standard dataset for NER. We call this dataset SESAME (Silver-Standard Named Entity Recognition dataset). We then proceed to study relevant statistics of SESAME, with the goal of:
> 
> Acknowledging inconsistencies in the corpus, e.g. sentence sizes
> 
> Raising information relevant to the calibration and evaluation of model performance e.g. proportion of each entity type and of each annotation source (DBpedia or auxiliary NER system)
> 
> We only consider sentences that have annotated entities. After all, sentences with only parser extraction entities do not take advantage of the human discernment invested in the structuring of the data of DBpedia.

#### Relevance 1158

Label: 

#### Passage 1159

Retrieved by: BM25, Dense, Hybrid

> Complex models such as deep neural networks have pushed progress in a wide range of machine learning applications, and enabled challenging tasks to be successfully solved. However, large amounts of human-annotated data are required to train such models in the supervised learning framework, and remain the bottleneck in important applications such as Named Entity Recognition (NER). We presented a method to generate a massively-sized labeled dataset for NER in an automatic fashion, without human labor involved in labeling – we do this by exploiting structured data in Wikipedia and DBpedia to detect mentions to named entities in articles.
> 
> Following the proposed method, we generate SESAME, a dataset for Portuguese NER. Although not a gold standard dataset, it allows for training of data-hungry predictors in a weakly-supervised fashion, alleviating the need for manually-annotated data. We show experimentally that SESAME can be used to train competitive NER predictors, or improve the performance of NER models when used alongside gold-standard data. We hope to increase interest in the study of automatic generation of silver-standard datasets, aimed at distant learning of complex models. Although SESAME is a dataset for the Portuguese language, the underlying method can be applied to virtually any language that is covered by Wikipedia.

#### Relevance 1159

Label: 

#### Passage 1161

Retrieved by: Dense, Hybrid

> SESAME consists of 87,769,158 tokens in total. The count and proportion of each entity tag (not a named entity, organization, person, location) is given in TABREF45.
> 
> Not surprisingly, the vast majority of words are not related to an entity mention at all. The statistics among words that are part of an entity mention are given in Table TABREF46, where over half of the entity mentions are of the type location.
> 
> Table TABREF47 shows a size comparison between SESAME and popular datasets for Portuguese NER.

#### Relevance 1161

Label: 

#### Passage 1162

Retrieved by: Dense, Hybrid

> In order to have a fair evaluation of our model, we use human-annotated datasets as validation and test sets.
> 
> We use the first HAREM and miniHAREM corpus, produced by the Linguateca project BIBREF15, as gold standard for model evaluation. We split the dataset in the following manner:
> 
> Validation: 20% of the first HAREM
> 
> Test: 80% of the first HAREM, plus the mini HAREM corpus
> 
> Another alternative is to use the Paramopama corpus which is larger than the HAREM and miniHAREM datasets. However, it was built using an automatic refinement process over the WikiNER corpus, hence being a silver standard dataset. We opted for the smaller HAREM datasets as they have been manually annotated, rendering the evaluation fair.
> 
> The HAREM corpus follows a different format than the one of SESAME: it uses a markup structure, without a proper tokenization of sentences and words. To circumvent this, we convert it to BIO format by applying the same tokenization process used for generating our dataset.

#### Relevance 1162

Label: 

### BM25

#### Passage 1156

Retrieved by: BM25

> Since our approach consists of matching raw text to a list of entity names, it does not account for context in which the entity was mentioned. For example, while under a specific context a country entity can exert the role of an organization, our method will tag it as a location regardless of the context. Therefore, our approach delimits an entity mention as a semantic object that does not vary in according to the context of the sentence.

#### Relevance 1156

Label: 

#### Passage 1157

Retrieved by: BM25

> Wikipedia guidelines include sets of suggested sections, such as early life (for person entities), references, further reading, and so on. Some of the sections have the purpose of listing related resources, not corresponding to a well structured text and, therefore, can be removed with the intent to reduce noise. In particular, we remove the following sections from each article: “references”, “see also”, “bibliography”, and “external links”.
> 
> After removing noisy elements, the Wikitext of each article is converted to raw text. This is achieved through the tool MWparser BIBREF11.

#### Relevance 1157

Label: 

#### Passage 1160

Retrieved by: BM25

> We performed extensive search over neural network architectures along with grid search over hyperparameter values. The model that yielded the best results consists of: (1) a word-level input layer, which computes pre-trained word embeddings BIBREF20 along with morphological features extracted by a character-level convolutional layer BIBREF21, (2) a bidirectional LSTM BIBREF22, (3) two fully-connected layers, and (4) a conditional random field (CRF). Table TABREF55 contains the optimal found hyperparameters for the network.
> 
> Additionally, the baseline was developed on a balanced re-sample of SESAME with a total of 1,216,976 sentences. The model also receives additional categorical features for each word, signalizing whether it: (1) starts with a capital letter, (2) has capitalized letters only, (3) has lowercase letters only, (4) contains digits, (5) has mostly digits ($>$ 50%) and (6) has digits only.
> 
> With the goal of evaluating whether SESAME can be advantageous for training NER classifiers, we compare the performance of the neural network trained with and without it. More specifically, we train neural networks on the HAREM2 BIBREF23 dataset, on SESAME, and on the union of the two – Table TABREF56 shows the test performance on the first HAREM corpus. As we can see, while SESAME alone is not sufficient to replace a human-annotated corpus (the $F_1$ score of the network trained on the SESAME is lower than the one trained on the HAREM2 corpus), it yields a boost of $1.5$ in the $F_1$ score when used together with the HAREM2 dataset.

#### Relevance 1160

Label: 

### Dense

#### Passage 1163

Retrieved by: Dense

> To circumvent mentioned entities which are not present in DBpedia, we use an auxiliary NER system to detect such mentions. More specifically, we use the Polyglot BIBREF12 system, a model trained on top of a dataset generated from Wikipedia.
> 
> Each mention's tag also specifies whether the mention was detected using DBpedia or by Polyglot. The following convention was adopted for the tags:
> 
> Annotated (Anot) - Matched exactly with one of the the entity's names in DBpedia
> 
> Predicted (Pred) - Extracted by Polyglot
> 
> Therefore, in our previous example, we have:
> 
> A predicted entity will be discarded entirely if it conflicts with an annotated one, since we aim to maximize the entities tagged using human-constructed resources as knowledge base.

#### Relevance 1163

Label: 

### Hybrid

#### Passage 1164

Retrieved by: Hybrid

> To construct a strong baseline for NER on the generated SESAME dataset and validate the quality of datasets generated following our method, we use a deep neural network that proved to be successful in many NLP tasks. Furthermore, we check whether adding the generated corpus to its training dataset provides performance boosts in NER benchmarks.

#### Relevance 1164

Label: 

## Question 0153

Paper: Addressee and Response Selection in Multi-Party Conversations with Speaker Interaction RNNs

> what are the previous state of the art systems?

### Common Retrieved Chunks

#### Passage 1165

Retrieved by: BM25, Hybrid

> SI-RNN jointly models who says what to whom by updating speaker embeddings in a role-sensitive way. It provides state-of-the-art addressee and response selection, which can instantly help retrieval-based dialog systems. In the future, we also consider using SI-RNN to extract sub-conversations in the unlabeled conversation corpus and provide a large-scale disentangled multi-party conversation data set.

#### Relevance 1165

Label: 

#### Passage 1167

Retrieved by: BM25, Hybrid

> In this subsection, we explain in detail how INLINEFORM0 / INLINEFORM1 / INLINEFORM2 update speaker embeddings according to their roles at each time step (Algorithm SECREF4 lines 19-26).
> 
> As shown in Figure FIGREF17 , INLINEFORM0 / INLINEFORM1 / INLINEFORM2 are all GRU-based units. INLINEFORM3 updates the sender embedding from the previous sender embedding INLINEFORM4 , the previous addressee embedding INLINEFORM5 , and the utterance embedding INLINEFORM6 : INLINEFORM7
> 
> The update, as illustrated in the upper part of Figure FIGREF17 , is controlled by three gates. The INLINEFORM0 gate controls the previous sender embedding INLINEFORM1 , and INLINEFORM2 controls the previous addressee embedding INLINEFORM3 . Those two gated interactions together produce the sender embedding proposal INLINEFORM4 . Finally, the update gate INLINEFORM5 combines the proposal INLINEFORM6 and the previous sender embedding INLINEFORM7 to update the sender embedding INLINEFORM8 . The computations in INLINEFORM9 (including gates INLINEFORM10 , INLINEFORM11 , INLINEFORM12 , the proposal embedding INLINEFORM13 , and the final updated embedding INLINEFORM14 ) are formulated as: INLINEFORM15
> 
> where INLINEFORM0 INLINEFORM1 are learnable parameters. INLINEFORM2 uses the same formulation with a different set of parameters, as illustrated in the middle of Figure FIGREF17 . In addition, we update the observer embeddings from the utterance. INLINEFORM3 is implemented as the traditional GRU unit in the lower part of Figure FIGREF17 . Note that the parameters in INLINEFORM4 / INLINEFORM5 / INLINEFORM6 are not shared. This allows SI-RNN to learn role-dependent features to control speaker embedding updates. The formulations of INLINEFORM7 and INLINEFORM8 are similar.

#### Relevance 1167

Label: 

#### Passage 1170

Retrieved by: Dense, Hybrid

> We thank the members of the UMichigan-IBM Sapphire Project and all the reviewers for their helpful feedback. This material is based in part upon work supported by IBM under contract 4915012629. Any opinions, findings, conclusions or recommendations expressed above are those of the authors and do not necessarily reflect the views of IBM.

#### Relevance 1170

Label: 

#### Passage 1171

Retrieved by: Dense, Hybrid

> Data Set. We use the Ubuntu Multiparty Conversation Corpus BIBREF4 and summarize the data statistics in Table TABREF24 . same The whole data set (including the Train/Dev/Test split and the false response candidates) is publicly available. The data set is built from the Ubuntu IRC chat room where a number of users discuss Ubuntu-related technical issues. The log is organized as one file per day corresponding to a document INLINEFORM0 . Each document consists of (Time, SenderID, Utterance) lines. If users explicitly mention addressees at the beginning of the utterance, the addresseeID is extracted. Then a sample, namely a unit of input (the dialog context and the current sender) and output (the addressee and response prediction) for the task, is created to predict the ground-truth addressee and response of this line. Note that samples are created only when the addressee is explicitly mentioned for clear, unambiguous ground-truth labels. False response candidates are randomly chosen from all other utterances within the same document. Therefore, distractors are likely from the same sub-conversation or even from the same sender but at different time steps. This makes it harder than BIBREF22 lowe2015ubuntu where distractors are randomly chosen from all documents. If no addressee is explicitly mentioned, the addressee is left blank and the line is marked as a part of the context.
> 
> Baselines. Apart from Dynamic-RNN, we also include several other baselines. Recent+TF-IDF always selects the most recent speaker (except the responding speaker INLINEFORM0 ) as the addressee and chooses the response to maximize the tf-idf cosine similarity with the context. We improve it by using a slightly different addressee selection heuristic (Direct-Recent+TF-IDF): select the most recent speaker that directly talks to INLINEFORM1 by an explicit addressee mention. We select from the previous 15 utterances, which is the longest context among all the experiments. This works much better when there are multiple concurrent sub-conversations, and INLINEFORM2 responds to a distant message in the context. We also include another GRU-based model Static-RNN from BIBREF4 ouchi-tsuboi:2016:EMNLP2016. Unlike Dynamic-RNN, speaker embeddings in Static-RNN are based on the order of speakers and are fixed. Furthermore, inspired by BIBREF30 zhou16multi and BIBREF19 serban2016building, we implement Static-Hier-RNN, a hierarchical version of Static-RNN. It first builds

#### Relevance 1171

Label: 

#### Passage 1173

Retrieved by: Dense, Hybrid

> We follow a data-driven approach to dialog systems. BIBREF5 singh1999reinforcement, BIBREF6 henderson2008hybrid, and BIBREF7 young2013pomdp optimize the dialog policy using Reinforcement Learning or the Partially Observable Markov Decision Process framework. In addition, BIBREF8 henderson2014second propose to use a predefined ontology as a logical representation for the information exchanged in the conversation. The dialog system can be divided into different modules, such as Natural Language Understanding BIBREF9 , BIBREF10 , Dialog State Tracking BIBREF11 , BIBREF12 , and Natural Language Generation BIBREF13 . Furthermore, BIBREF14 wen2016network and BIBREF15 bordes2017learning propose end-to-end trainable goal-oriented dialog systems.
> 
> Recently, short text conversation has been popular. The system receives a short dialog context and generates a response using statistical machine translation or sequence-to-sequence networks BIBREF16 , BIBREF17 , BIBREF18 , BIBREF19 , BIBREF20 , BIBREF21 . In contrast to response generation, the retrieval-based approach uses a ranking model to select the highest scoring response from candidates BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 . However, these models are single-turn responding machines and thus still are limited to short contexts with only two speakers. As for larger context, BIBREF22 lowe2015ubuntu propose the Next Utterance Classification (NUC) task for multi-turn two-party dialogs. BIBREF4 ouchi-tsuboi:2016:EMNLP2016 extend NUC to multi-party conversations by integrating the addressee detection problem. Since the data is text based, they use only textual information to predict addressees as opposed to relying on acoustic signals or gaze information in multimodal dialog systems BIBREF23 , BIBREF24 .
> 
> Furthermore, several other papers are recently presented focusing on modeling role-specific information given the dialogue contexts BIBREF25 , BIBREF26 , BIBREF27 . For example, BIBREF25 meng2017towards combine content and temporal information to predict the utterance speaker. By contrast, our SIRNN explicitly utilizes the speaker interaction to maintain speaker embeddings and predicts the addressee and response by joint selection.

#### Relevance 1173

Label: 

### BM25

#### Passage 1166

Retrieved by: BM25

> Real-world conversations often involve more than two speakers. In the Ubuntu Internet Relay Chat channel (IRC), for example, one user can initiate a discussion about an Ubuntu-related technical issue, and many other users can work together to solve the problem. Dialogs can have complex speaker interactions: at each turn, users play one of three roles (sender, addressee, observer), and those roles vary across turns.
> 
> In this paper, we study the problem of addressee and response selection in multi-party conversations: given a responding speaker and a dialog context, the task is to select an addressee and a response from a set of candidates for the responding speaker. The task requires modeling multi-party conversations and can be directly used to build retrieval-based dialog systems BIBREF0 , BIBREF1 , BIBREF2 , BIBREF3 .
> 
> The previous state-of-the-art Dynamic-RNN model from BIBREF4 ouchi-tsuboi:2016:EMNLP2016 maintains speaker embeddings to track each speaker status, which dynamically changes across time steps. It then produces the context embedding from the speaker embeddings and selects the addressee and response based on embedding similarity. However, this model updates only the sender embedding, not the embeddings of the addressee or observers, with the corresponding utterance, and it selects the addressee and response separately. In this way, it only models who says what and fails to capture addressee information. Experimental results show that the separate selection process often produces inconsistent addressee-response pairs.
> 
> To solve these issues, we introduce the Speaker Interaction Recurrent Neural Network (SI-RNN). SI-RNN redesigns the dialog encoder by updating speaker embeddings in a role-sensitive way. Speaker embeddings are updated in different GRU-based units depending on their roles (sender, addressee, observer). Furthermore, we note that the addressee and response are mutually dependent and view the task as a joint prediction problem. Therefore, SI-RNN models the conditional probability (of addressee given the response and vice versa) and selects the addressee and response pair by maximizing the joint probability.
> 
> On a public standard benchmark data set, SI-RNN significantly improves the addressee and response selection accuracy, particularly in complex conversations with many speakers and responses to distant messages many turns in the past. Our code and data set are available online.

#### Relevance 1166

Label: 

#### Passage 1168

Retrieved by: BM25

> While Dynamic-RNN can track the speaker status by capturing who says what in multi-party conversation, there are still some issues. First, at each time step, only the sender embedding is updated from the utterance. Therefore, other speakers are blind to what is being said, and the model fails to capture addressee information. Second, while the addressee and response are mutually dependent, Dynamic-RNN selects them independently. Consider a case where the responding speaker is talking to two other speakers in separate conversation threads. The choice of addressee is likely to be either of the two speakers, but the choice is much less ambiguous if the correct response is given, and vice versa. Dynamic-RNN often produces inconsistent addressee-response pairs due to the separate selection. See Table TABREF30 for examples.
> 
> In contrast to Dynamic-RNN, the dialog encoder in SI-RNN updates embeddings for all the speakers besides the sender at each time step. Speaker embeddings are updated depending on their roles: the update of the sender is different from the addressee, which is different from the observers. Furthermore, the update of a speaker embedding is not only from the utterance, but also from other speakers. These are achieved by designing variations of GRUs for different roles. Finally, SI-RNN selects the addressee and response jointly by maximizing the joint probability.
> 
> [t] Dialog Encoder in SI-RNN [1] Input INLINEFORM0 : INLINEFORM1 INLINEFORM2 where INLINEFORM3 // Initialize speaker embeddings INLINEFORM4 INLINEFORM5 //Update speaker embeddings INLINEFORM6 // Update sender, addressee, observers INLINEFORM7 INLINEFORM8 INLINEFORM9 // Compute utterance embedding INLINEFORM10 INLINEFORM11 // Update sender embedding INLINEFORM12 // Update addressee embedding INLINEFORM13 // Update observer embeddings INLINEFORM14 INLINEFORM15 // Return final speaker embeddings Output INLINEFORM16 for INLINEFORM17

#### Relevance 1168

Label: 

#### Passage 1169

Retrieved by: BM25

> For fair and meaningful quantitative comparisons, we follow BIBREF4 ouchi-tsuboi:2016:EMNLP2016's evaluation protocols. SI-RNN improves the overall accuracy on the addressee and response selection task. Two ablation experiments further analyze the contribution of role-sensitive units and joint selection respectively. We then confirm the robustness of SI-RNN with the number of speakers and distant responses. Finally, in a case study we discuss how SI-RNN handles complex conversations by either engaging in a new sub-conversation or responding to a distant message.
> 
> Overall Result. As shown in Table TABREF23 , SI-RNN significantly improves upon the previous state-of-the-art. In particular, addressee selection (ADR) benefits most, with different number of candidate responses (denoted as RES-CAND): around 12% in RES-CAND INLINEFORM0 and more than 10% in RES-CAND INLINEFORM1 . Response selection (RES) is also improved, suggesting role-sensitive GRUs and joint selection are helpful for response selection as well. The improvement is more obvious with more candidate responses (2% in RES-CAND INLINEFORM2 and 4% in RES-CAND INLINEFORM3 ). These together result in significantly better accuracy on the ADR-RES metric as well.
> 
> Ablation Study. We show an ablation study in the last rows of Table TABREF23 . First, we share the parameters of INLINEFORM0 / INLINEFORM1 / INLINEFORM2 . The accuracy decreases significantly, indicating that it is crucial to learn role-sensitive units to update speaker embeddings. Second, to examine our joint selection, we fall back to selecting the addressee and response separately, as in Dynamic-RNN. We find that joint selection improves ADR and RES individually, and it is particularly helpful for pair selection ADR-RES.
> 
> Number of Speakers. Numerous speakers create complex dialogs and increased candidate addressee, thus the task becomes more challenging. In Figure FIGREF27 (Upper), we investigate how ADR accuracy changes with the number of speakers in the context of length 15, corresponding to the rows with T=15 in Table TABREF23 . Recent+TF-IDF always chooses the most recent speaker and the accuracy drops dramatically as the number of speakers increases. Direct-Recent+TF-IDF shows better performance, and Dynamic-RNNis marginally better. SI-RNN is much more robust and remains above 70% accuracy across all bins. The advantage is more obvious for bins with more speakers.
> 
> Addressing Distance. Addressing distance is the time difference from the responding speaker

#### Relevance 1169

Label: 

### Dense

#### Passage 1172

Retrieved by: Dense

> performance, and Dynamic-RNNis marginally better. SI-RNN is much more robust and remains above 70% accuracy across all bins. The advantage is more obvious for bins with more speakers.
> 
> Addressing Distance. Addressing distance is the time difference from the responding speaker to the ground-truth addressee. As the histogram in Figure FIGREF27 (Lower) shows, while the majority of responses target the most recent speaker, many responses go back five or more time steps. It is important to note that for those distant responses, Dynamic-RNN sees a clear performance decrease, even worse than Direct-Recent+TF-IDF. In contrast, SI-RNN handles distant responses much more accurately.
> 
> same
> 
> Case Study. Examples in Table TABREF30 show how SI-RNN can handle complex multi-party conversations by selecting from 10 candidate responses. In both examples, the responding speakers participate in two or more concurrent sub-conversations with other speakers.
> 
> Example (a) demonstrates the ability of SI-RNN to engage in a new sub-conversation. The responding speaker “wafflejock" is originally involved in two sub-conversations: the sub-conversation 1 with “codepython", and the ubuntu installation issue with “theoletom". While it is reasonable to address “codepython" and “theoletom", the responses from other baselines are not helpful to solve corresponding issues. TF-IDF prefers the response with the “install" key-word, yet the response is repetitive and not helpful. Dynamic-RNN selects an irrelevant response to “codepython". SI-RNN chooses to engage in a new sub-conversation by suggesting a solution to “releaf" about Ubuntu dedicated laptops.
> 
> Example (b) shows the advantage of SI-RNN in responding to a distant message. The responding speaker “nicomachus" is actively engaged with “VeryBewitching" in the sub-conversation 1 and is also loosely involved in the sub-conversation 2: “chingao" mentions “nicomachus" in the most recent utterance. SI-RNN remembers the distant sub-conversation 1 and responds to “VeryBewitching" with a detailed answer. Direct-Recent+TF-IDF selects the ground-truth addressee because “VeryBewitching" talks to “nicomachus", but the response is not helpful. Dynamic-RNN is biased to the recent speaker “chingao", yet the response is not relevant.

#### Relevance 1172

Label: 

#### Passage 1174

Retrieved by: Dense

> model Static-RNN from BIBREF4 ouchi-tsuboi:2016:EMNLP2016. Unlike Dynamic-RNN, speaker embeddings in Static-RNN are based on the order of speakers and are fixed. Furthermore, inspired by BIBREF30 zhou16multi and BIBREF19 serban2016building, we implement Static-Hier-RNN, a hierarchical version of Static-RNN. It first builds utterance embeddings from words and then uses high-level RNNs to process utterance embeddings.
> 
> Implementation Details For a fair comparison, we follow the hyperparameters from BIBREF4 ouchi-tsuboi:2016:EMNLP2016, which are chosen based on the validation data set. We take a maximum of 20 words for each utterance. We use 300-dimensional GloVe word vectors, which are fixed during training. SI-RNN uses 50-dimensional vectors for both speaker embeddings and hidden states. Model parameters are initialized with a uniform distribution between -0.01 and 0.01. We set the mini-batch size to 128. The joint cross-entropy loss function with 0.001 L2 weight decay is minimized by Adam BIBREF31 . The training is stopped early if the validation accuracy is not improved for 5 consecutive epochs. All experiments are performed on a single GTX Titan X GPU. The maximum number of epochs is 30, and most models converge within 10 epochs.

#### Relevance 1174

Label: 

### Hybrid

None

## Question 0154

Paper: Transforming Wikipedia into Augmented Data for Query-Focused Summarization

> How does their BERT-based model work?

### Common Retrieved Chunks

#### Passage 1175

Retrieved by: BM25, Hybrid

> In this paper, we propose to automatically construct a large-scale query-focused summarization dataset WikiRef using Wikipedia articles and the corresponding references. The statements, supporting citations and article title along with section titles of the statements are used as summaries, documents and queries respectively. The WikiRef dataset serves as a means of data augmentation on DUC benchmarks. It also is shown to be a eligible query-focused summarization benchmark. Moreover, we develop a BERT-based extractive query-focused summarization model to extract summaries from the documents. The model makes use of the query-sentence relationships and sentence-sentence relationships jointly to score sentences. The results on DUC benchmarks show that our model with data augmentation outperforms the state-of-the-art. As for future work, we would like to model relationships among documents for multi-document summarization.

#### Relevance 1175

Label: 

#### Passage 1176

Retrieved by: BM25, Dense, Hybrid

> Figure FIGREF2 gives an overview of our BERT-based extractive query-focused summmarization model. For each sentence, we use BERT to encode its query relevance, document context and salient meanings into a vector representation. Then the vector representations are fed into a simple output layer to predict the label or estimate the score of each sentence.

#### Relevance 1176

Label: 

#### Passage 1180

Retrieved by: Dense, Hybrid

> of the query and the document as input. The query-sentence and sentence-sentence relationships are jointly modeled by the self-attention mechanism BIBREF12. The model is fine-tuned to utilize the general language representations of BERT BIBREF13.
> 
> Experimental results on three DUC benchmarks show that the model achieves competitive performance by fine-tuning and outperforms previous state-of-the-art summarization models with data augmentation. Meanwhile, the results demonstrate that we can use WikiRef as a large-scale dataset to advance query-focused summarization research.

#### Relevance 1180

Label: 

#### Passage 1181

Retrieved by: Dense, Hybrid

> We follow standard practice to alternately train our model on two years of data and test on the third. The oracle scores used in model training are Rouge-2 recall of sentences. In this paper, we score a sentence by only considering the query and the its document. Then we rank sentences according to the estimated scores across documents within a cluster. For each cluster, we fetch the top-ranked sentences iteratively into the output summary with redundancy constraint met. A sentence is redundant if more than half of its bigrams appear in the current output summary.
> 
> The WikiRef dataset is used as augmentation data for DUC datasets in two steps. We first fine-tune BERT on the WikiRef dataset. Subsequently, we use the DUC datasets to further fine-tune parameters of the best pre-trained model.

#### Relevance 1181

Label: 

#### Passage 1183

Retrieved by: Dense, Hybrid

> Table TABREF22 shows the Rouge scores of comparison methods and our proposed method. Fine-tuning BERT on DUC datasets alone outperforms previous best performing summarization systems on DUC 2005 and 2006 and obtains comparable results on DUC 2007. Our data augmentation method further advances the model to a new state of the art on all DUC benchmarks. We also notice that models pre-trained on the augmentation data achieve reasonable performance without further fine-tuning model parameters. It implies the WikiRef dataset reveals useful knowledge shared by the DUC datatset. We pre-train models on augmentation data under both sentence classification and sentence regression supervision. The experimental results show that both supervision types yield similar performance.

#### Relevance 1183

Label: 

### BM25

#### Passage 1177

Retrieved by: BM25

> BIBREF10 is the contextual relation-based neural summarization system that improves sentence scoring by utilizing contextual relations among sentences.

#### Relevance 1177

Label: 

#### Passage 1178

Retrieved by: BM25

> For summary evaluation, we use Rouge BIBREF16 as our automatic evaluation metric. Rouge is the official metrics of the DUC benchmarks and widely used for summarization evaluation. Rouge-N measures the summary quality by counting overlapping N-grams with respect to the reference summary. Whereas Rouge-L measures the longest common subsequence. To compare with previous work on DUC datasets, we report the Rouge-1 and Rouge-2 recall computed with official parameters that limits the length to 250 words. On the WikiRef dataset, we report Rouge-1, Rouge-2 and Rouge-L scores.

#### Relevance 1178

Label: 

#### Passage 1179

Retrieved by: BM25

> We first train our extractive summarization model on the WikiRef dataset through sentence classification. And we need the ground-truth binary labels of sentences to be extracted. However, we can not find the sentences that exactly match the reference summary for most examples. To solve this problem, we use a greedy algorithm similar to BIBREF17 zhou-etal-2018-neural-document to find an oracle summary with document sentences that maximizes the Rouge-2 F1 score with respect to the reference summary. Given a document of $n$ sentences, we greedily enumerate the combination of sentences. For documents that contain numerous sentences, searching for an global optimal combination of sentences is computationally expensive. Meanwhile it is unnecessary since the reference summaries contain no more than four sentences. So we stop searching when no combination with $i$ sentences scores higher than the best the combination with $i$-1 sentences.
> 
> We also train an extractive summarization model through sentence regression. For each sentence, the oracle score for training is the Rouge-2 F1 score.
> 
> During inference, we rank sentences according to their predicted scores. Then we append the sentence one by one to form the summary if it is not redundant and scores higher than a threshold. We skip the redundant sentences that contain overlapping trigrams with respect to the current output summary as in BIBREF18 ft-bert-extractive. The threshold is searched on the development set to obtain the highest Rouge-2 F1 score.

#### Relevance 1179

Label: 

### Dense

#### Passage 1182

Retrieved by: Dense

> uses the same structure as the BERT with randomly initialized parameters.

#### Relevance 1182

Label: 

### Hybrid

None

## Question 0155

Paper: Predicting the Type and Target of Offensive Posts in Social Media

> How many annotators participated?

### Common Retrieved Chunks

#### Passage 1184

Retrieved by: BM25, Dense, Hybrid

> indicating high agreement. As to normalization and anonymization, no user metadata or Twitter IDs have been stored, and URLs and Twitter mentions have been substituted to placeholders. We follow prior work in related areas (burnap2015cyber,davidson2017automated) and annotate our data using crowdsourcing using the platform Figure Eight. We ensure data quality by: 1) we only received annotations from individuals who were experienced in the platform; and 2) we used test questions to discard annotations of individuals who did not reach a certain threshold. Each instance in the dataset was annotated by multiple annotators and inter-annotator agreement has been calculated. We first acquired two annotations for each instance. In case of 100% agreement, we considered these as acceptable annotations, and in case of disagreement, we requested more annotations until the agreement was above 66%. After the crowdsourcing annotation, we used expert adjudication to guarantee the quality of the annotation. The breakdown of the data into training and testing for the labels from each level is shown in Table TABREF15 .

#### Relevance 1184

Label: 

#### Passage 1185

Retrieved by: BM25, Hybrid

> Level C categorizes the targets of insults and threats as individual (IND), group (GRP), and other (OTH).
> 
> Individual (IND): Posts targeting an individual. It can be a a famous person, a named individual or an unnamed participant in the conversation. Insults and threats targeted at individuals are often defined as cyberbulling.
> 
> Group (GRP): The target of these offensive posts is a group of people considered as a unity due to the same ethnicity, gender or sexual orientation, political affiliation, religious belief, or other common characteristic. Many of the insults and threats targeted at a group correspond to what is commonly understood as hate speech.
> 
> Other (OTH): The target of these offensive posts does not belong to any of the previous two categories (e.g. an organization, a situation, an event, or an issue).

#### Relevance 1185

Label: 

#### Passage 1186

Retrieved by: BM25, Dense, Hybrid

> The data included in OLID has been collected from Twitter. We retrieved the data using the Twitter API by searching for keywords and constructions that are often included in offensive messages, such as `she is' or `to:BreitBartNews'. We carried out a first round of trial annotation of 300 instances with six experts. The goal of the trial annotation was to 1) evaluate the proposed tagset; 2) evaluate the data retrieval method; and 3) create a gold standard with instances that could be used as test questions in the training and test setting annotation which was carried out using crowdsourcing. The breakdown of keywords and their offensive content in the trial data of 300 tweets is shown in Table TABREF14 . We included a left (@NewYorker) and far-right (@BreitBartNews) news accounts because there tends to be political offense in the comments. One of the best offensive keywords was tweets that were flagged as not being safe by the Twitter `safe' filter (the `-' indicates `not safe'). The vast majority of content on Twitter is not offensive so we tried different strategies to keep a reasonable number of tweets in the offensive class amounting to around 30% of the dataset including excluding some keywords that were not high in offensive content such as `they are` and `to:NewYorker`. Although `he is' is lower in offensive content we kept it as a keyword to avoid gender bias. In addition to the keywords in the trial set, we searched for more political keywords which tend to be higher in offensive content, and sampled our dataset such that 50% of the the tweets come from political keywords and 50% come from non-political keywords. In addition to the keywords `gun control', and `to:BreitbartNews', political keywords used to collect these tweets are `MAGA', `antifa', `conservative' and `liberal'. We computed Fliess' INLINEFORM0 on the trial set for the five annotators on 21 of the tweets. INLINEFORM1 is .83 for Layer A (OFF vs NOT) indicating high agreement. As to normalization and anonymization, no user metadata or Twitter IDs have been stored, and URLs and Twitter mentions have been substituted to placeholders. We follow prior work in related areas (burnap2015cyber,davidson2017automated) and annotate our data using

#### Relevance 1186

Label: 

#### Passage 1188

Retrieved by: BM25, Hybrid

> Offensive content has become pervasive in social media and a reason of concern for government organizations, online communities, and social media platforms. One of the most common strategies to tackle the problem is to train systems capable of recognizing offensive content, which then can be deleted or set aside for human moderation. In the last few years, there have been several studies published on the application of computational methods to deal with this problem. Most prior work focuses on a different aspect of offensive language such as abusive language BIBREF0 , BIBREF1 , (cyber-)aggression BIBREF2 , (cyber-)bullying BIBREF3 , BIBREF4 , toxic comments INLINEFORM0 , hate speech BIBREF5 , BIBREF6 , BIBREF7 , BIBREF8 , BIBREF9 , BIBREF10 , and offensive language BIBREF11 . Prior work has focused on these aspects of offensive language in Twitter BIBREF3 , BIBREF7 , BIBREF8 , BIBREF11 , Wikipedia comments, and Facebook posts BIBREF2 .
> 
> Recently, Waseem et. al. ( BIBREF12 ) acknowledged the similarities among prior work and discussed the need for a typology that differentiates between whether the (abusive) language is directed towards a specific individual or entity or towards a generalized group and whether the abusive content is explicit or implicit. Wiegand et al. ( BIBREF11 ) followed this trend as well on German tweets. In their evaluation, they have a task to detect offensive vs not offensive tweets and a second task for distinguishing between the offensive tweets as profanity, insult, or abuse. However, no prior work has explored the target of the offensive language, which is important in many scenarios, e.g., when studying hate speech with respect to a specific target.
> 
> Therefore, we expand on these ideas by proposing a a hierarchical three-level annotation model that encompasses:
> 
> Using this annotation model, we create a new large publicly available dataset of English tweets. The key contributions of this paper are as follows:

#### Relevance 1188

Label: 

#### Passage 1190

Retrieved by: Dense, Hybrid

> similar properties and the hierarchical annotation model proposed in this paper aims to capture this. Considering that, for example, an insult targeted at an individual is commonly known as cyberbulling and that insults targeted at a group are known as hate speech, we pose that OLID's hierarchical annotation model makes it a useful resource for various offensive language identification sub-tasks.

#### Relevance 1190

Label: 

### BM25

#### Passage 1187

Retrieved by: BM25

> We assess our dataset using traditional and deep learning methods. Our simplest model is a linear SVM trained on word unigrams. SVMs have produced state-of-the-art results for many text classification tasks BIBREF13 . We also train a bidirectional Long Short-Term-Memory (BiLSTM) model, which we adapted from the sentiment analysis system of sentimentSystem,rasooli2018cross and altered to predict offensive labels instead. It consists of (1) an input embedding layer, (2) a bidirectional LSTM layer, (3) an average pooling layer of input features. The concatenation of the LSTM's and average pool layer is passed through a dense layer and the output is passed through a softmax function. We set two input channels for the input embedding layers: pre-trained FastText embeddings BIBREF14 , as well as updatable embeddings learned by the model during training. Finally, we also apply a Convolutional Neural Network (CNN) model based on the architecture of BIBREF15 , using the same multi-channel inputs as the above BiLSTM.
> 
> Our models are trained on the training data, and evaluated by predicting the labels for the held-out test set. The distribution is described in Table TABREF15 . We evaluate and compare the models using the macro-averaged F1-score as the label distribution is highly imbalanced. Per-class Precision (P), Recall (R), and F1-score (F1), also with other averaged metrics are also reported. The models are compared against baselines of predicting all labels as the majority or minority classes.

#### Relevance 1187

Label: 

### Dense

#### Passage 1189

Retrieved by: Dense

> In the OLID dataset, we use a hierarchical annotation model split into three levels to distinguish between whether language is offensive or not (A), and type (B) and target (C) of the offensive language. Each level is described in more detail in the following subsections and examples are shown in Table TABREF10 .

#### Relevance 1189

Label: 

#### Passage 1191

Retrieved by: Dense

> The results of the offensive target identification experiment are reported in Table TABREF20 . Here the systems were trained to distinguish between three targets: a group (GRP), an individual (IND), or others (OTH). All three models achieved similar results far surpassing the random baselines, with a slight performance edge for the neural models.
> 
> The performance of all systems for the OTH class is 0. This poor performances can be explained by two main factors. First, unlike the two other classes, OTH is a heterogeneous collection of targets. It includes offensive tweets targeted at organizations, situations, events, etc. making it more challenging for systems to learn discriminative properties of this class. Second, this class contains fewer training instances than the other two. There are only 395 instances in OTH, and 1,075 in GRP, and 2,407 in IND.

#### Relevance 1191

Label: 

### Hybrid

None

## Question 0156

Paper: Represent, Aggregate, and Constrain: A Novel Architecture for Machine Reading from Noisy Sources

> what metrics are used to evaluate the models?

### Common Retrieved Chunks

#### Passage 1192

Retrieved by: BM25, Dense, Hybrid

> We evaluate configurations of our proposed architecture across three measures. The first is a modified version of standard precision, recall, and F INLINEFORM0 , as proposed by reschke2014. It deviates from the standard protocol by (1) awarding full recall for any slot when a single predicted value is contained in the gold slot, (2) only penalizing slots for which there are findable gold values in the text, and (3) limiting candidate values to the set of entities proposed by the Stanford NER system and included in the data set release. Eight of the fifteen slots are used in evaluation. Similarly, the second evaluation measure we present is standard precision, recall, and F INLINEFORM1 , specifically for null values.
> 
> We also evaluate the models using mean reciprocal rank (MRR). When calculating the F INLINEFORM0 -based evaluation measure we decode the model by taking the single highest-scoring value for each slot. However, this does not necessarily reflect the quality of the overall value ranking produced by the model. For this reason we include MRR, defined as: DISPLAYFORM0
> 
> where rank INLINEFORM0 is the rank position of the first correct value for a given cluster and slot pair INLINEFORM1 , and INLINEFORM2 , the number of such pairs, is INLINEFORM3 , the product of the total number of clusters with the total number of predicted slots.

#### Relevance 1192

Label: 

#### Passage 1194

Retrieved by: BM25, Hybrid

> Results are presented in Table TABREF44 . In comparison to previous work, our any configuration of our RAC architecture with sum-based aggregation outperforms the best existing systems by a minimum of 9.8 F INLINEFORM0 . In comparison to the various Mention-CNN systems, it is clear that this improvement is not a result of different features or the use of pre-trained word embeddings, or even the representational power of the CNN-based embeddings. Rather, it is attributable to training end-to-end with aggregation and a cluster-level loss function.
> 
> With respect to aggregation, sum-based methods consistently outperform their max counterparts, indicating that exploiting the redundancy of information in news clusters is beneficial to the task. The topic-based aggregation is statistically significant improvement over standard sum aggregation (p INLINEFORM0 ), and produces the highest performing unconstrained system.
> 
> Date-based aggregation did not yield a statistically significant improvement over sum aggregation. We hypothesize that the method is sound, but accurate datelines could only be extracted for 31 INLINEFORM0 documents. We did not modify the aggregation weights ( INLINEFORM1 ) for the remaining documents, minimizing the effect of this approach.
> 
> The EE-AS Reader has the lowest overall performance, which one can attribute to pooling evidence in a manner that is poorly suited to this problem domain. By placing a softmax over each document's beliefs, what is an advantage in the cloze-style QA setting here becomes a liability: the model is forced to predict a value for every slot, for every each document, even when few are truly mentioned.

#### Relevance 1194

Label: 

#### Passage 1195

Retrieved by: BM25, Hybrid

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

#### Relevance 1195

Label: 

#### Passage 1196

Retrieved by: BM25, Dense, Hybrid

> The Stanford Plane Crash Dataset BIBREF15 is a small data set consisting of 80 plane crash events, each paired with a set of related news articles. Of these events, 40 are reserved for training, and 40 for testing, with the average cluster containing more than 2,000 mentions. Gold labels for each cluster are derived from Wikipedia infoboxes and cover up to 15 slots, of which 8 are used in evaluation (Figure TABREF54 ).
> 
> We follow the same entity normalization procedure as reschke2014, limit the cluster size to the first 200 documents, and further reduce the number of duplicate documents to prevent biases in aggregation. We partition out every fifth document from the training set to be used as development data, primarily for use in an early stopping criterion. We also construct additional clusters from the remaining training documents, and use this to increase the size of the development set.

#### Relevance 1196

Label: 

#### Passage 1197

Retrieved by: Dense, Hybrid

> We randomly selected 15 development set instances which our best model predicts incorrectly. Of these, we find three were incorrectly labeled in the gold data as errors from the distance supervision hypothesis (i.e., “zero chance” being labeled for 0 survivors, when the number of survivors was not mentioned in the cluster), and should not be predicted. Six were clearly expressed and should be predictable, with highly correlated keywords present in the context window, but were assigned low scores by the model. We belief a richer representation which combines the generalization of CNNs with the discrete signal of n-gram features BIBREF18 may solve some of these issues.
> 
> Four of the remaining errors appear to be due to aggregation errors. Specifically, the occurrence of a particular punctuation mark with far greater than average frequency resulted in it being predicted for three slots. While these could be filtered out, a more general solution may be to build a representation based on the actual mention (“Ryanair”), in addition to its context. This may reduce the scores of these mentions to such an extent that they are removed from consideration.
> 
> Table TABREF54 shows the accuracy of the model on each slot type. The model is struggles with predicting the Injuries and Survivors slots. The nature of news media leads these slots to be discussed less frequently, with their mentions often embedded more deeply in the document, or expressed textually. For instance, it is common to express INLINEFORM0 =Survivors, INLINEFORM1 as “no survivors”, but it is impossible to predict a 0 value in this case, under the current problem definition.

#### Relevance 1197

Label: 

### BM25

#### Passage 1193

Retrieved by: BM25

> We evaluate on four categories of architecture:
> 
> reschke2014 proposed several methods for event extraction in this scenario. We compare against three notable examples drawn from this work:
> 
> [leftmargin=*]
> 
> Reschke CRF: a conditional random field model.
> 
> Reschke Noisy-OR: a sequence tagger with a "Noisy-OR" form of aggregation that discourages the model from predicting the same value for multiple slots.
> 
> Reschke Best: a sequence tagger using a cost-sensitive classifier, optimized with SEARN BIBREF17 , a learning-to-search framework.
> 
> Each of these models uses features drawn from dependency trees, local context (unigram/part-of-speech features for up to 5 neighboring words), sentence context (bag-of-word/part-of-speech), words/part-of-speech of words occurring within the value, as well as the entity type of the mention itself.
> 
> The representation and scoring components of our architecture, with an additional slot for predicting a null value. The INLINEFORM0 scores are used when constructing the loss and during decoding. These scores can also be aggregated in a max/sum manner after decoding, but such aggregation is not incorporated during training.
> 
> Representation, scoring, and aggregation components, trained end-to-end with a cluster-level loss. Null values are predicted as described in Sec. UID18 .
> 
> kadlec2016 present AS Reader, a state-of-the-art model for cloze-style QA. Like our architecture, AS Reader aggregates mention-level scores, pooling evidence for each answer candidate. However, in cloze-style QA an entity is often mentioned in complementary contexts throughout the text, but are frequently in similar contexts in news cluster extraction.
> 
> We tailor AS Reader to event extraction to illustrate the importance of choosing an aggregation which reflects how the gold labels are applied to the data. EE-AS Reader is implemented by applying Eq. EQREF9 and Eq. to each document, as opposed to clusters, as documents are analogous to sentences in the cloze-style QA task. We then concatenate the resulting vectors, and apply sum aggregation as before.

#### Relevance 1193

Label: 

### Dense

#### Passage 1198

Retrieved by: Dense

> Effective aggregation techniques can be crucial for identifying accurate information from noisy sources. Figure FIGREF1 depicts an example of our problem scenario. An IR component fetches several documents based on the query, and sample sentences are shown for each document. The goal is to extract the correct value, of which there may be many mentions in the text, for each slot. Sentences in INLINEFORM0 express a target slot, the number of fatalities, but the mention corresponds to an incorrect value. This is a common mistake in early news reports. Documents INLINEFORM1 and INLINEFORM2 also express this slot, and with mentions of the correct value, but with less certainty.
> 
> A model which focuses on a single high-scoring mention, at the expense of breadth, will make an incorrect prediction. In comparison, a model which learns to correctly accumulate evidence for each value across multiple mentions over the entire cluster can identify the correct information, circumventing this problem. Figure FIGREF1 (bottom) shows how this pooling of evidence can produce the correct cluster-level prediction.

#### Relevance 1198

Label: 

#### Passage 1199

Retrieved by: Dense

> present in the cluster, is determining whether to predict any value at all. A common solution for handling such missing values is the use of a threshold, below which the model returns null. However, even a separate threshold for each slot would not fully capture the nature of the problem.
> 
> Determining whether a value is missing is a trade-off between two factors: (1) how strongly the mention-level scores support a non-null answer, and (2) how much general information regarding that event and that slot is given. We incorporate both factors by extending the definition of INLINEFORM0 and its use in Eq. EQREF9 –Eq. to include not only mentions, but all words. Each non-mention word is treated as a mention of the null value: DISPLAYFORM0
> 
> where INLINEFORM0 is the set of mentions. The resulting null score varies according to both the cluster size and its content. Smaller clusters with fewer documents require less evidence to predict a non-null value, while larger clusters must accumulate more evidence for a particular candidate or a null value will be proposed instead.
> 
> The exact words contained in the cluster also have an effect. For example, clusters with numerous mentions of killed, died, dead, will have a higher INLINEFORM0 Fatalities INLINEFORM1 , requiring the model to be more confident in its answer for that slot during training. Additionally, this provides a mechanism for driving down INLINEFORM2 when INLINEFORM3 is not strongly associated with INLINEFORM4 .

#### Relevance 1199

Label: 

### Hybrid

None

## Question 0157

Paper: Named Entities in Medical Case Reports: Corpus and Experiments

> How many documents are in the new corpus?

### Common Retrieved Chunks

#### Passage 1200

Retrieved by: BM25, Dense, Hybrid

> The automatic processing of medical texts and documents plays an increasingly important role in the recent development of the digital health area. To enable dedicated Natural Language Processing (NLP) that is highly accurate with respect to medically relevant categories, manually annotated data from this domain is needed. One category of high interest and relevance are medical entities. Only very few annotated corpora in the medical domain exist. Many of them focus on the relation between chemicals and diseases or proteins and diseases, such as the BC5CDR corpus BIBREF0, the Comparative Toxicogenomics Database BIBREF1, the FSU PRotein GEne corpus BIBREF2 or the ADE (adverse drug effect) corpus BIBREF3. The NCBI Disease Corpus BIBREF4 contains condition mention annotations along with annotations of symptoms. Several new corpora of annotated case reports were made available recently. grouin-etal-2019-clinical presented a corpus with medical entity annotations of clinical cases written in French, copdPhenotype presented a corpus focusing on phenotypic information for chronic obstructive pulmonary disease while 10.1093/database/bay143 presented a corpus focusing on identifying main finding sentences in case reports.
> 
> The corpus most comparable to ours is the French corpus of clinical case reports by grouin-etal-2019-clinical. Their annotations are based on UMLS semantic types. Even though there is an overlap in annotated entities, semantic classes are not the same. Lab results are subsumed under findings in our corpus and are not annotated as their own class. Factors extend beyond gender and age and describe any kind of risk factor that contributes to a higher probability of having a certain disease. Our corpus includes additional entity types. We annotate conditions, findings (including medical findings such as blood values), factors, and also modifiers which indicate the negation of other entities as well as case entities, i. e., entities specific to one case report. An overview is available in Table TABREF3.

#### Relevance 1200

Label: 

#### Passage 1201

Retrieved by: BM25, Dense, Hybrid

> We present a new corpus, developed to facilitate the processing of case reports. The corpus focuses on five distinct entity types: cases, conditions, factors, findings and modifiers. Where applicable, relationships between entities are also annotated. Additionally, we annotate discontinuous entities with a special relationship type (discontinuous). The corpus presented in this paper is the very first of its kind and a valuable addition to the scarce number of corpora available in the field of biomedical NLP. Its complexity, given the discontinuous nature of entities and a high number of nested and multi-label entities, poses new challenges for NLP methods applied for NER and can, hence, be a valuable source for insights into what entities “look like in the wild”. Moreover, it can serve as a playground for new modelling techniques such as the resolution of discontinuous entities as well as multi-task learning given the combination of entities and their relations. We provide an evaluation of four distinct NER systems that will serve as robust baselines for future work but which are, as of yet, unable to solve all the complex challenges this dataset holds. A functional service based on the presented corpus is currently being integrated, as a NER service, in the QURATOR platform BIBREF20.

#### Relevance 1201

Label: 

#### Passage 1202

Retrieved by: BM25, Dense, Hybrid

> The corpus consists of 53 documents, which contain an average number of 156.1 sentences per document, each with 19.55 tokens on average. The corpus comprises 8,275 sentences and 167,739 words in total. However, as mentioned above, only case presentation sections, headings and abstracts are annotated. The numbers of annotated entities are summarized in Table TABREF24.
> 
> Findings are the most frequently annotated type of entity. This makes sense given that findings paint a clinical picture of the patient's condition. The number of tokens per entity ranges from one token for all types to 5 tokens for cases (average length 3.1), nine tokens for conditions (average length 2.0), 16 tokens for factors (average length 2.5), 25 tokens for findings (average length 2.6) and 18 tokens for modifiers (average length 1.4) (cf. Table TABREF24). Examples of rather long entities are given in Table TABREF25.
> 
> Entities can appear in a discontinuous way. We model this as a relation between two spans which we call “discontinuous” (cf. Figure FIGREF26). Especially findings often appear as discontinuous entities, we found 543 discontinuous finding relations. The numbers for conditions and factors are lower with seven and two, respectively. Entities can also be nested within one another. This happens either when the span of one annotation is completely embedded in the span of another annotation (fully-nested; cf. Figure FIGREF12), or when there is a partial overlapping between the spans of two different entities (partially-nested; cf. Figure FIGREF12). There is a high number of inter-sentential relations in the corpus (cf. Table TABREF27). This can be explained by the fact that the case entity occurs early in each document; furthermore, it is related to finding and factor annotations that are distributed across different sentences.
> 
> The most frequently annotated relation in our corpus is the has-relation between a case entity and the findings related to that case. This correlates with the high number of finding entities. The relations contained in our corpus are summarized in Table TABREF27.

#### Relevance 1202

Label: 

#### Passage 1203

Retrieved by: BM25, Dense, Hybrid

> We evaluate the corpus using Named Entity Recognition (NER), i. e., the task of finding mentions of concepts of interest in unstructured text. We focus on detecting cases, conditions, factors, findings and modifiers in case reports (cf. Section SECREF6). We approach this as a sequence labeling problem. Four systems were developed to offer comparable robust baselines.
> 
> The original documents are pre-processed (sentence splitting and tokenization with ScispaCy). We do not perform stop word removal or lower-casing of the tokens. The BIO labeling scheme is used to capture the order of tokens belonging to the same entity type and enable span-level detection of entities. Detection of nested and/or discontinuous entities is not supported. The annotated corpus is randomized and split in five folds using scikit-learn BIBREF9. Each fold has a train, test and dev split with the test split defined as .15% of the train split. This ensures comparability between the presented systems.

#### Relevance 1203

Label: 

#### Passage 1204

Retrieved by: BM25, Hybrid

> The annotation was performed using WebAnno BIBREF7, a web-based tool for linguistic annotation. The annotators could choose between a pre-annotated version or a blank version of each text. The pre-annotated versions contained suggested entity spans based on string matches from lists of conditions and findings synonym lists. Their quality varied widely throughout the corpus. The blank version was preferred by the annotators. We distribute the corpus in BioC JSON format. BioC was chosen as it allows us to capture the complexities of the annotations in the biomedical domain. It represented each documents properties ranging from full text, individual passages/sentences along with captured annotations and relationships in an organized manner. BioC is based on character offsets of annotations and allows the stacking of different layers.

#### Relevance 1204

Label: 

### BM25

None

### Dense

#### Passage 1205

Retrieved by: Dense

> We asked medical doctors experienced in extracting knowledge related to medical entities from texts to annotate the entities described above. Initially, we asked four annotators to test our guidelines on two texts. Subsequently, identified issues were discussed and resolved. Following this pilot annotation phase, we asked two different annotators to annotate two case reports according to our guidelines. The same annotators annotated an overall collection of 53 case reports.
> 
> Inter-annotator agreement is calculated based on two case reports. We reach a Cohen's kappa BIBREF6 of 0.68. Disagreements mainly appear for findings that are rather unspecific such as She no longer eats out with friends which can be seen as a finding referring to “avoidance behaviour”.

#### Relevance 1205

Label: 

### Hybrid

None

## Question 0158

Paper: Self-Attention Enhanced Selective Gate with Entity-Aware Embedding for Distantly Supervised Relation Extraction

> By how much do they outperform previous state-of-the-art in terms of top-n precision?

### Common Retrieved Chunks

#### Passage 1206

Retrieved by: BM25, Dense, Hybrid

> We first compare our proposed SeG with aforementioned approaches in Table TABREF19 for top-N precision (i.e., P@N). As shown in the top panel of the table, our proposed model SeG can consistently and significantly outperform baseline (i.e., PCNN+ATT) and all recently-promoted works in terms of all P@N metric. Compared to PCNN with selective attention (i.e., PCNN+ATT), our proposed SeG can significantly improve the performance by 23.6% in terms of P@N mean for all sentences; even if a soft label technique is applied (i.e., PCNN+ATT+SL) to alleviate wrongly labeled problem, our performance improvement is also very significant, i.e., 7.8%.
> 
> Compared to previous state-of-the-art approaches (i.e., PCNN+HATT and PCNN+BAG-ATT), the proposed model can also outperform them by a large margin, i.e., 10.3% and 5.3% , even if they propose sophisticated techniques to handle the noisy training data. These verify the effectiveness of our approach over previous works when solving the wrongly labeled problem that frequently appears in distantly supervised relation extraction.
> 
> Moreover, for proposed approach and comparative ones, we also show AUC curves and available numerical values in Figure FIGREF31 and Table TABREF32 respectively. The empirical results for AUC are coherent with those of P@N, which shows that, our proposed approach can significantly improve previous ones and reach a new state-of-the-art performance by handling wrongly labeled problem using context-aware selective gate mechanism. Specifically, our approach substantially improves both PCNN+HATT and PCNN+BAG-ATT by 21.4% in aspect of AUC for precision-recall.

#### Relevance 1206

Label: 

#### Passage 1207

Retrieved by: BM25, Dense, Hybrid

> AUC and top-n precision metrics for distantly supervised relation extraction task, and also verify the significance of each proposed module. Particularly, the proposed framework can achieve AUC of 0.51, which outperforms selective attention baseline by 0.14 and improves previous state-of-the-art approach by 0.09.

#### Relevance 1207

Label: 

#### Passage 1209

Retrieved by: BM25, Hybrid

> Previous works of relation extraction mainly employ a piecewise convolutional neural network (PCNN) BIBREF3 to obtain contextual representation of sentences due to its capability of capturing local features, less computation and light-weight structure. However, some previous works BIBREF13 find that CNNs cannot reach state-of-the-art performance on a majority of natural language processing benchmarks due to a lack of measuring long-term dependency, even if stacking multiple modules. This motivates us to enhance the PCNN with another neural module, which is capable of capturing long-term or global dependencies to produce complementary and more powerful sentence representation.
> 
> Hence, we employ a self-attention mechanism in our model due to its parallelizable computation and state-of-the-art performance. Unlike existing approaches that sequentially stack self-attention and CNN layers in a cascade form BIBREF9, BIBREF14, we arrange these two modules in parallel so they can generate features describing both local and long-term relations for the same input sequence. Since each bag may contain many sentences (up to 20), a light-weight networks that can can efficiently process these sentences simultaneously is more preferable, such as PCNN that is the most popular module for relation extraction. For this reason, there is only one light-weight self-attention layer in our model. This is contrast to BIBREF9 yu2018qanet and BIBREF14 wu2019pay who stack both modules many times repeatedly. Our experiments show that two modules arranged in parallel manner consistently outperform stacking architectures that are even equipped with additional residual connections BIBREF15). The comparative experiments will be elaborated in Section SECREF34 and SECREF35.

#### Relevance 1209

Label: 

#### Passage 1210

Retrieved by: BM25, Dense, Hybrid

> Following previous works BIBREF3, BIBREF5, BIBREF6, BIBREF4, we use precision-recall (PR) curves, area under curve (AUC) and top-N precision (P@N) as metrics in our experiments on the held-out test set from the NYT dataset. To directly show the perfomance on one sentence bag, we also calculate the accuracy of classification (Acc.) on non-NA sentences.

#### Relevance 1210

Label: 

### BM25

#### Passage 1208

Retrieved by: BM25

> In this paper, we propose a brand-new framework for distantly supervised relation extraction, i.e., selective gate (SeG) framework, as a new alternative to previous ones. It incorporates an entity-aware embedding module and a self-attention enhanced selective gate mechanism to integrate task-specific entity information into word embedding and then generates a complementary context-enriched representation for PCNN. The proposed framework has certain merits over previously prevalent selective attention when handling wrongly labeled data, especially for a usual case that there are only one sentence in the most of bags. The experiments conduct on popular NYT dataset show that our model SeG can consistently deliver a new benchmark in state-of-the-art performance in terms of all P@N and precision-recall AUC. And further ablation study and case study also demonstrate the significance of the proposed modules to handle wrongly labeled data and thus set a new state-of-the-art performance for the benchmark dataset. In the future, we plan to incorporate an external knowledge base into our framework, which may further boost the prediction quality by overcoming the problems with a lack of background information as discussed in our error analysis.

#### Relevance 1208

Label: 

### Dense

#### Passage 1211

Retrieved by: Dense

> we observe a notable performance drop after stacking PCNN and self-attention in Table TABREF36. This verifies that our model combining self-attention mechanism and PCNN in parallel can achieve a satisfactory result.
> 
> To further empirically evaluate the performance of our method in solving one-sentence bag problem, we extract only the one-sentence bags from NYT's training and test sets, which occupy 80% of the original dataset. The evaluation and comparison results in Table TABREF33 show that compared to PCNN+ATT, the AUC improvement (+0.13) between our model and PCNN+ATT on one-sentence bags is higher than the improvement of full NYT dataset, which verifies SeG's effectiveness on one-sentence bags. In addition, PCNN+ATT shows a light decrease compared with PCNN, which can also support the claim that selective attention is vulnerable to one-sentence bags.

#### Relevance 1211

Label: 

#### Passage 1212

Retrieved by: Dense

> This research was funded by the Australian Government through the Australian Research Council (ARC) under grants LP180100654 partnership with KS computer. We also acknowledge the support of NVIDIA Corporation and Google Cloud with the donation of GPUs and computation credits respectively.

#### Relevance 1212

Label: 

### Hybrid

#### Passage 1213

Retrieved by: Hybrid

> To further verify the effectiveness of each module in the proposed framework, we conduct an extensive ablation study in this section. In particular, SeG w/o Ent denotes removing entity-aware embedding, SeG w/o Gate denotes removing selective gate and concatenating two representations from PCNN and self-attention, SeG w/o Gate w/o Self-Attn denotes removing self-attention enhanced selective gate. In addition, we also replace the some parts of the proposed framework with baseline module for an in-depth comparison. SeG+ATT denotes replacing mean-pooing with selective attention, and SeG w/ stack denotes using stacked PCNN and self-attention rather than in parallel.
> 
> The P@N results are listed in the bottom panel of Table TABREF19, and corresponding AUC results are shown in Table TABREF36 and Figure FIGREF37. According to the results, we find that our proposed modules perform substantially better than those of the baseline in terms of both metrics. Particularly, by removing entity-aware embedding (i.e, SeG w/o Ent) and self-attention enhanced selective gate (i.e., SeG w/o Gate w/o Self-Attn), it shows 11.5% and 1.8% decreases respectively in terms of P@N mean for all sentences. Note that, when dropping both modules above (i.e., SeG w/o ALL), the framework will be degenerated as selective attention baseline BIBREF5, which again demonstrates that our proposed framework is superior than the baseline by 15% in terms of P@N mean for all sentences.
> 
> To verify the performance of selective gate modul when handling wrongly labeled problem, we simply replace the selective gate module introduced in Eq.(DISPLAY_FORM15) with selective attention module, namely, SeG+Attn w/o Gate, and instead of mean pooling in Eq.(DISPLAY_FORM15), we couple selective gate with selective attention to fulfill aggregation instead mean-pooling, namely, SeG+Attn. Across the board, the proposed SeG still deliver the best results in terms of both metrics even if extra selective attention module is applied.
> 
> Lastly, to explore the influence of the way to combine PCNN with self-attention mechanism, we stack them by following the previous works BIBREF9, i.e., SeG w/ Stack. And we observe a notable performance drop after stacking PCNN and self-attention in Table TABREF36. This verifies that our model combining self-attention mechanism and PCNN in parallel can achieve a satisfactory result.
> 
> To further empirically evaluate the performance of our method

#### Relevance 1213

Label: 

## Question 0159

Paper: Exploiting Token and Path-based Representations of Code for Identifying Security-Relevant Commits

> What regularization methods are used?

### Common Retrieved Chunks

#### Passage 1214

Retrieved by: BM25, Hybrid

> There exist a handful of papers in software engineering that perform commit classification to identify security vulnerabilities or fixes. BIBREF19 describe an efficient vulnerability identification system geared towards tracking large-scale projects in real time using latent information underlying commit messages and bug reports in open-source projects. While BIBREF19 classify commits based on the commit message, we use only the commit diff or the corresponding source code as features for our model. BIBREF2 propose a machine learning approach to identify security-relevant commits. However, they treat source code as documents written in natural language and use well-known document classification methods to perform the actual classification. BIBREF20 conduct an analysis to identify which security vulnerabilities can be discovered during code review, or what characteristics of developers are likely to introduce vulnerabilities.

#### Relevance 1214

Label: 

#### Passage 1215

Retrieved by: BM25, Dense, Hybrid

> The lexer and tokenizer we use from the javalang library target Java 8. We are not able to verify that all the projects and their forks in this study are using the same version of Java. However, we do not expect considerable differences in syntax between Java 7 and Java 8 except for the introduction of lambda expressions.
> 
> There is also a question of to what extent the 635 publicly disclosed vulnerabilities used for evaluation in this study represent the vulnerabilities found in real-world scenarios. While creating larger ground-truth datasets would always be helpful, it might not always be possible. To reduce the possibility of bias in our results, we ensure that we don't train commits from the same projects that we evaluate our models on. We also discard any commits belonging to the set of evaluation projects that are mined using regular expression matching.
> 
> We directly train code2vec on our dataset without pre-training it, in order to assess how well path-based representations perform for learning on code, as opposed to token-level representations on which H-CNN and HR-CNN are based. However, BIBREF16 pre-trained their model on 10M Java classes. It is possible that the performance of code2vec is considerably better than the results in Table TABREF22 after pre-training. Furthermore, our findings apply only to this particular technique to capturing path-based representations, not the approach in general. However, we leave both issues for future work.

#### Relevance 1215

Label: 

#### Passage 1216

Retrieved by: BM25, Dense, Hybrid

> by BIBREF30, just as research in NLP changed focus from brittle rule-based expert systems to statistical methods, software engineering research should augment traditional methods that consider only the formal structure of programs with information about the statistical properties of code. Ongoing research on pre-trained code embeddings that don't require a labelled dataset for training is a step in the right direction. Drawing parallels with the recent history of NLP research, we are hoping that further study in the domain of code embeddings will considerably accelerate progress in tackling software problems with deep learning.

#### Relevance 1216

Label: 

#### Passage 1217

Retrieved by: BM25, Hybrid

> In this study, we propose a novel hierarchical deep learning model for the identification of security-relevant commits and show that deep learning has much to offer when it comes to commit classification. We also make a case for pre-training word embeddings on tokens extracted from Java code, which leads to performance improvements. We are able to further improve the results using a siamese architecture connecting two CNN-based encoders to represent the modified files before and after a commit.
> 
> Network architectures that are effective on a certain task, such as predicting method names, are not necessarily effective on related tasks. Thus, choices between neural models should be made considering the nature of the task and the amount of training data available. Based on the model's ability to predict method names in files across different projects, BIBREF16 claim that code2vec can be used for a wide range of programming language processing tasks. However, for predicting the security relevance of commits, H-CNN and HR-CNN appear to be much better than code2vec.
> 
> A potential research direction would be to build language models for programming languages based on deep language representation models. Neural networks are becoming increasingly deeper and complex in the NLP literature, with significant interest in deep language representation models such as ELMo, GPT, and BERT BIBREF26, BIBREF27, BIBREF28. BIBREF28 show strong empirical performance on a broad range of NLP tasks. Since all of these models are pre-trained in an unsupervised manner, it would be easy to pre-train such models on the vast amount of data available on GitHub.
> 
> Deep learning models are known for scaling well with more data. However, with less than 1,000 ground-truth training samples and around 1,800 augmented training samples, we are unable to exploit the full potential of deep learning. A reflection on the current state of labelled datasets in software engineering (or the lack thereof) throws light on limited practicality of deep learning models for certain software engineering tasks BIBREF29. As stated by BIBREF30, just as research in NLP changed focus from brittle rule-based expert systems to statistical methods, software engineering research should augment traditional methods that consider only the formal structure of programs with information about the statistical properties of code.

#### Relevance 1217

Label: 

#### Passage 1218

Retrieved by: BM25, Dense, Hybrid

> We modify our model accordingly for every research question, based on changes in the input representation. To benchmark the performance of our deep learning models, we compare them against a logistic regression (LR) baseline that learns on one-hot representations of the Java tokens extracted from the commit diffs. For all of our models, we employ dropout on the fully-connected layer for regularization. We use Adam BIBREF25 for optimization, with a learning rate of 0.001, and batch size of 16 for randomly initialized embeddings and 8 for pre-trained embeddings.
> 
> For RQ1, we use a hierarchical CNN (H-CNN) with either randomly-initialized or pre-trained word embeddings in order to extract features from the commit diff. We represent the commit diff as a concatenation of 300-dimensional vectors for each corresponding token from that diff. This resultant matrix is then passed through three temporal convolutional layers in parallel, with filter windows of size 3, 5, and 7. A temporal max-pooling operation is applied to these feature maps to retain the feature with the highest value in every map. We also present a regularized version of this model (henceforth referred to as HR-CNN) with embedding dropout applied on the inputs, and DropBlock on the activations of the convolutional layers.
> 
> For RQ2, we made a modification to both the H-CNN and HR-CNN models in order to extract features from the source code for the Java classes before and after the commit. Both of these models use a siamese architecture between the two CNN-based encoders as shown in Figure FIGREF20. We then concatenate the results from both of these encoders and pass it through a fully-connected layer followed by softmax for prediction.
> 
> For RQ3, we adapt the code2vec model used by BIBREF16 for predicting method names into a model for predicting whether a commit is security-relevant by modifying the final layer. We then repeat our experiments on both the ground-truth and augmented dataset.

#### Relevance 1218

Label: 

### BM25

None

### Dense

#### Passage 1219

Retrieved by: Dense

> We learn token-level vectors for code using the CBOW architecture BIBREF4, with negative sampling and a context window size of 5. Using CBOW over skip-gram is a deliberate design decision. While skip-gram is better for infrequent words, we felt that it is more important to focus on the more frequent words (inevitably, the keywords in a programming language) when it comes to code. Since we only perform minimal preprocessing on the code (detailed below), the most infrequent words will usually be variable identifiers. Following the same line of reasoning, we choose negative sampling over hierarchical-softmax as the training algorithm.
> 
> We do not normalize variable identifiers into generic tokens as they could contain contextual information. However, we do perform minimal preprocessing on the code before training the model. This includes:
> 
> The removal of comments and whitespace when performing tokenization using a lexer.
> 
> The conversion of all numbers such as integers and floating point units into reserved tokens.
> 
> The removal of tokens whose length is greater than or equal to 64 characters.
> 
> Thresholding the size of the vocabulary to remove infrequent tokens.

#### Relevance 1219

Label: 

#### Passage 1220

Retrieved by: Dense

> In computational linguistics, there has been a lot of effort over the last few years to create a continuous higher dimensional vector space representation of words, sentences, and even documents such that similar entities are closer to each other in that space BIBREF4, BIBREF5, BIBREF6. BIBREF4 introduced word2vec, a class of two-layer neural network models that are trained on a large corpus of text to produce word embeddings for natural language. Such learned distributed representations of words have accelerated the application of deep learning techniques for natural language processing (NLP) tasks BIBREF7.
> 
> BIBREF8 show that convolutional neural networks (CNNs) can achieve state-of-the-art results in single-sentence sentiment prediction, among other sentence classification tasks. In this approach, the vector representations of the words in a sentence are concatenated vertically to create a two-dimensional matrix for each sentence. The resulting matrix is passed through a CNN to extract higher-level features for performing the classification. BIBREF9 introduce the hierarchical attention network (HAN), where a document vector is progressively built by aggregating important words into sentence vectors, and then aggregating important sentences vectors into document vectors.
> 
> Deep neural networks are prone to overfitting due to the possibility of the network learning complicated relationships that exist in the training set but not in unseen test data. Dropout prevents complex co-adaptations of hidden units on training data by randomly removing (i.e. dropping out) hidden units along with their connections during training BIBREF10. Embedding dropout, used by BIBREF11 for neural language modeling, performs dropout on entire word embeddings. This effectively removes a proportion of the input tokens randomly at each training iteration, in order to condition the model to be robust against missing input.
> 
> While dropout works well for regularizing fully-connected layers, it is less effective for convolutional layers due to the spatial correlation of activation units in convolutional layers. There have been a number of attempts to extend dropout to convolutional neural networks BIBREF12. DropBlock is a form of structured dropout for convolutional layers where units in a contiguous region of a feature map are dropped together BIBREF13.

#### Relevance 1220

Label: 

### Hybrid

None

## Question 0160

Paper: Mapping Languages and Demographics with Georeferenced Corpora

> Which websites were used in the web crawl?

### Common Retrieved Chunks

#### Passage 1221

Retrieved by: BM25, Dense, Hybrid

> Data comes from two sources of digital texts: web pages from the Common Crawl and social media from Twitter. Starting with the web-crawled data, we can compare this dataset to previous georeferenced web corpora BIBREF12, BIBREF13. The basic pipeline is to process all text within $<p>$ tags, removing boilerplate content, navigation content, and noisy text. We view each web page as a document containing the remaining material. Documents are then deduplicated by site, by time, and by location.
> 
> Language samples are geo-located using country-specific top-level domains: the assumption is that a language sample from a web-site under the .ca domain originated from Canada. This approach to regionalization does not assume that whoever produced that language sample was born in Canada or represents a traditional Canadian dialect group. Rather, the assumption is only that the sample represents someone in Canada who is producing language data. Previous work has shown that there is a significant relationship between domain-level georeferencing and traditionally-collected linguistic data BIBREF14.
> 
> Some countries are not available because their top-level domains are used for other purposes (i.e., .ai, .fm, .io, .ly, .ag, .tv). Domains that do not contain geographic information are also removed from consideration (e.g., .com sites). The Common Crawl dataset covers 2014 through the end of 2017, totalling 81.5 billion web pages. As shown in Table 1, after processing this produces a corpus of 16.65 billion words. Table 1 also shows the number of countries represented in the web corpus against the number of countries in the ground-truth UN dataset and in the collected Twitter corpus. Countries may be missing from the web dataset (i) because their domains are used for a different purpose or (ii) their domains are not widely used or the country does not produce a significant amount of data on the open internet.
> 
> In isolation, web-crawled data provides one observation of global language use. Another common source of data used for this purpose is Twitter BIBREF15, BIBREF16, BIBREF17, BIBREF18, BIBREF19, BIBREF20, BIBREF21). A spatial search is used to collect tweets from within a 50km radius of 10k cities. This search avoids biasing the selection by using language-specific keywords or hashtags. The Twitter data covers the period from May of

#### Relevance 1221

Label: 

#### Passage 1222

Retrieved by: BM25, Dense, Hybrid

> How well does the amount of data correspond with the population density of each country? In this section we compare the number of words in each corpus with the UN population estimates. These datasets cover 199 countries in total, although the web-crawled data only represents 166 countries and the Twitter data only represents 169 countries.
> 
> The Pearson correlations between different measures per country are shown in Table 4. There are five measures per country: the size of the web-crawled and social media corpora in words, the UN population estimates, population adjusted by per capita GDP, and population adjusted by access to the internet. The purpose of these different weightings is to take into consideration the fact that some countries may produce more digital text per person than others.
> 
> First, we notice that there is very little relationship between the two corpora ($r=0.05$). This is interesting in and of itself because, given the systematic attempt to find georeferenced texts, we would expect a fairly high correlation here. But this shows that the data comes from different places (c.f., Figures 2 and 3). Because the collection methods were designed with this purpose in mind, it is unlikely that this low correlation is caused by the methods themselves rather than reflecting the fact that these datasets represent different populations. In other words, this is a strong indication that web data and Twitter data represent two different populations regardless of variations in the collection methods employed in this study.
> 
> Second, GDP-weighting and internet-usage-weighting have different effects on the two datasets. When adjusted for GDP, the correlation between Twitter data and population raises from $r=0.39$ to $r=0.60$, a fairly strong relationship and higher than when adjusted by internet usage. But when population is adjusted for GDP, the correlation between web-crawled data and population lowers from $r=0.39$ to $r=0.28$. In other words, economic information does not help to weight the web data towards actual ground-truth population density.
> 
> For web-crawled data, internet access provides a much better population weighting ($r=0.49$). This is perhaps not surprising because the internet usage statistics are directly relevant to the production of websites. But it is surprising that general internet access is not a good predictor of

#### Relevance 1222

Label: 

#### Passage 1223

Retrieved by: BM25, Dense, Hybrid

> In recent years there has been an increasing amount of research investigating the use of unstructured geographic information, such as user-generated social media content and textual web data, for geographical analysis. Such unstructured data sources can provide information about places that is difficult to measure through traditional sensor observations. Aggregated representations of places that are extracted from textual corpora, e.g., give us insight into what people feel and think about places, potentially providing a much richer understanding of human geography BIBREF0, BIBREF1. It can also give insight into the relationships between places and human behavior BIBREF2, BIBREF3. However, a recurring issue with this kind of big data, and user-generated content in general, is the question of how representative these data sets are compared to the populations that we wish to study BIBREF4. There exists little previous empirical work to establish how representative web corpora are with respect to different geographic regions of the world (c.f. BIBREF5, BIBREF6). In this paper we describe such a computational experiment using language identification models on two global-scale corpora.
> 
> How well does language data represent both regional population densities and the social characteristics of regional populations? To answer this question, we collect and analyze two large global-scale datasets: web-crawled data from the Common Crawl (16.65 billion words) and social media data from Twitter (4.14 billion words). This paper evaluates demographic-type information that is derived from these datasets, information which traditionally has been collected using survey-instruments as part of a census.
> 
> When labeled with a language identification model, this data provides a representation of both (i) how much language a particular country produces, a proxy for population density and (ii) the mix of languages used in a country, a proxy for population demographics. These corpus-based representations are compared against four ground-truth baselines. First, the UN country-level population estimates BIBREF7. Second, because not all populations have equal access to internet technologies, we use per capita GDP BIBREF8 and internet-usage statistics BIBREF9 to adjust raw populations. Third, the UN country-level census aggregations are used to represent what languages are used in each country BIBREF10 and, where these are not available, the World Factbook BIBREF11 estimations are used. The goal is to measure how

#### Relevance 1223

Label: 

#### Passage 1225

Retrieved by: BM25, Dense, Hybrid

> BIBREF19, BIBREF20, BIBREF21). A spatial search is used to collect tweets from within a 50km radius of 10k cities. This search avoids biasing the selection by using language-specific keywords or hashtags. The Twitter data covers the period from May of 2017 until early 2019. This creates a corpus containing 1,066,038,000 tweets, all connected with the city from which they were collected. Because the language identification component only provides reliable predictions for samples containing at least 50 characters, the corpus is pruned to that length threshold (this removes approximately 250 million tweets). As shown in Table 1, this produces a corpus containing 4.14 billion words.
> 
> Each of these datasets rests on different assumptions and, as a result, is subject to different confounds. For example, using top-level domains to determine the country of origin for web pages is likely to over-represent countries like Estonia that use their TLD extensively and to under-represent countries like the United States that do not traditionally use their TLD. The Twitter dataset relies on georeferenced tweets, but not all users have GPS-enabled devices. For example, we might expect that countries with a lower per capita GDP have a lower percent of georeferenced tweets, in addition to having fewer tweets overall. The goal here is to establish a baseline of how well these corpora represent actual populations.

#### Relevance 1225

Label: 

#### Passage 1226

Retrieved by: Dense, Hybrid

> Analyses and models based on digital texts, especially from Twitter, often come with uncertainty about the underlying populations that those texts represent. This paper has systematically collected Twitter and web-data from locations around the world without language-specific searches that would bias the collection. The purpose is to understand how well these data sets correspond with what we know about global populations from ground-truth sources, providing a method for evaluating different data collection techniques.
> 
> The first important finding is that patterns from Twitter and web-crawled data diverge significantly in their representation of the world's population. This simply reflects the fact that data drawn from Twitter and web pages will likely represent people from different places. Why? We have also seen that Twitter data matches populations better when population numbers are weighted by GDP and worse when weighted by internet-usage statistics. This implies that Twitter as a platform represents more wealthy populations than general web-crawled data. An alternate interpretation is that the Twitter collection here is based on urban areas, which tend to have more wealthy populations. Would the same bias be found with a rural-centered collection procedure? That is a secondary problem in this context because the goal is to develop ground-truth population-centered baselines that could be used to evaluate different Twitter collection methods.
> 
> The second important finding is that, given what ground-truth language-use data is available, there are in general very few false positives: cases where the corpora suggest a language is frequently used in a country but census-based data does not. While uncommon, there are more false positives in Twitter data. This is significant because it means that, in general, these corpora do not predict language use that is not actually present.
> 
> But the third important finding is that, given what ground-truth language-use data is available, there remain a number of countries where these corpora do not represent all the language produced by the local populations: not all languages from censuses are found in digital texts. In this case Twitter has fewer missing languages.

#### Relevance 1226

Label: 

### BM25

#### Passage 1224

Retrieved by: BM25

> access provides a much better population weighting ($r=0.49$). This is perhaps not surprising because the internet usage statistics are directly relevant to the production of websites. But it is surprising that general internet access is not a good predictor of Twitter usage. Overall, we see that there is a definite relationship between populations and the amount of digital text produced per country, but there are clear regional biases.
> 
> What countries are specifically over-represented and under-represented in the two datasets? We first find the relative share of each dataset for each country. For example, what percentage of the web-corpus is from India? This assumes the total world population and the total corpus size as constants and finds the share of that total from each country. We then subtract the population estimates from the corpus-based estimates. In other words, we first normalize each representation (corpus size and population) and then find the difference between the normalized measures. This allows us to take into account the very different counts (words vs. persons).
> 
> If the result is negative, then a particular country is under-represented. For example, the share of the corpus from India has values of -0.1730 (CC) and -0.1421 (TW). This means that language from India is under-represented given what we would expect its population to produce. On the other hand, if the result is positive, then a particular country is over-represented. For example, Estonia is over-represented in the web-crawled data (0.0290) as is Australia in the Twitter data (0.0226) These numbers mean that there is 2.9% more language data from Estonia on the web than expected given the population of Estonia; and there is 17.3% less language data from India on the web than expected given the population of India.
> 
> Countries are shown by their representation in Twitter (Figure 2) and the web corpus (Figure 3), with red indicating over-representation: there is more corpus data than population size would predict. The imbalance between Twitter data and population is caused by a clear over-representation of the US, Canada, western Europe, Russia, and South America. But the imbalance between web-crawled data and population has a very different geographic pattern: there is less extreme over-representation but more under-representation. Specifically, under-representation

#### Relevance 1224

Label: 

### Dense

None

### Hybrid

None
