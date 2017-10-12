# RNN 

## speech 

### seq2seq

* [SPEECH RECOGNITION WITH DEEP RECURRENT NEURAL NETWORKS](https://arxiv.org/abs/1303.5778)

   LSTM, BiRNN, multi-layer BiLSTM, CTC(acoustic-only model), RNN Transducer(jointly trained acoustic and language
model)
   RNN transducer [10] combines a CTC-like network with a separate RNN that predicts each phoneme given the previous ones, thereby yielding a jointly trained acoustic and language model.

* [Sequence to Sequence Learning with Neural Networks](https://www.google.co.jp/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiK3pzrzKHWAhVGxrwKHdCrChwQFggmMAA&url=https%3A%2F%2Fpapers.nips.cc%2Fpaper%2F5346-sequence-to-sequence-learning-with-neural-networks.pdf&usg=AFQjCNHkuuvss8h-_xyrytRBFTKQUb60Sg)

  While the LSTM is capable of solving problems with long term dependencies, we discovered that the LSTM learns much better when the source sentences are reversed.
  We were able to do well on long sentences because we reversed the order of words in the source sentence but not the target sentences in the training and test set.
  As typical neural language models rely on a vector representation for each word, we used a ﬁxed vocabulary for both languages. We used 160,000 of the most frequent words for the source language and 80,000 of the most frequent words for the target language. Every out-of-vocabulary word was replaced with a special “UNK” token

* [Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](https://arxiv.org/abs/1512.02595)

### CNN with RNN

* [Convolutional Neural Networks for Speech Recognition](https://pdfs.semanticscholar.org/86ef/e7769f2b8a0e15ca213ab09881e6705caeb0.pdf)

### CTC

* [Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with Recurrent Neural Networks](https://www.google.co.jp/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwi_6oHGi6HWAhUEvLwKHf08AycQFggmMAA&url=http%3A%2F%2Fciteseerx.ist.psu.edu%2Fviewdoc%2Fdownload%3Fdoi%3D10.1.1.75.6306%26rep%3Drep1%26type%3Dpdf&usg=AFQjCNHPF99UGSi8aSQM3np1OXLwI09gQw)

   CTC:Labelling unsegmented sequence data is a ubiquitous problem in real-world sequence learning.
   Currently, graphical models such as hidden Markov Models (HMMs; Rabiner, 1989), conditional random ﬁelds (CRFs; Laﬀerty et al., 2001) and their variants, are the predominant framework for sequence labeling.
   Drawbacks of HMM and CRF. for standard HMMs, training is generative, even though sequence labelling is discriminative
   The basic idea is to interpret the network outputs as a probability distribution over all possible label sequences, conditioned on a given input sequence.Given this distribution, an objective function can be derived that directly maximises the probabilities of the correct labellings.
   The objective function is derived from the principle of maximum likelihood. That is, minimising it maximises the log likelihoods of the target labellings.

* [Residual Convolutional CTC Networks for Automatic Speech Recognition](https://arxiv.org/pdf/1702.07793.pdf)

### Attention

* [Attention-Based Models for Speech Recognition](https://arxiv.org/abs/1506.07503)

  content-based attention, location-aware attention, Score Normalization: Sharpening and Smoothing

* [Attention-Based End-to-End Speech Recognition in Mandarin](https://arxiv.org/abs/1707.07167)

  By xiaomi, like a summarize 
  Use attention into Mandarin

* [Attention-Based Models for Speech Recognition](https://arxiv.org/abs/1506.07503)

  location-based, content-based and hybrid attention 

* [Listen, Attend and Spell](https://arxiv.org/pdf/1508.01211.pdf)

  本文写的很好，值得一看。有作者训练的经验，模型的理解。方法描述简单清晰。非常适合经验不足的同学看。
  This attention vector can be thought of as skip connections that allow the information and the gradients to flow more effectively in an RNN.
  The attention model was also able to identify the start and end of the utterance properly.

* [END-TO-END ATTENTION-BASED LARGE VOCABULARY SPEECH RECOGNITION](https://arxiv.org/pdf/1508.04395.pdf)
  INTEGRATION WITH A LANGUAGE MODEL(WFST), 
   The last term rT is important, because without it the LM component dominates and the cost L is minimized by too short sequences.
  In this work we apply the windowing at the training stage as well. Which is simlity to Luong's local attention.

* [Advances in Joint CTC-Attention based End-to-End Speech Recognition with a Deep CNN Encoder and RNN-LM](https://arxiv.org/pdf/1706.02737.pdf)

## NMT

* [NEURAL MACHINE TRANSLATION BY JOINTLY LEARNING TO ALIGN AND TRANSLATE](https://arxiv.org/abs/1409.0473)
  Bahdanau attention
  propose Attention 

* [Effective Approaches to Attention-based Neural Machine Translation](https://arxiv.org/pdf/1508.04025v5.pdf)

  Good Paper, simplize Attention

  Luong Attention, Global attention, local attention
  a global approach which always attends to all source words and a local one that only looks at a subset of source words at a time. 
  examine various alignment functions

* [BELU](https://www.google.co.jp/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiTyNe4vMzWAhVLebwKHRh5C3UQFggpMAA&url=http%3A%2F%2Fwww.aclweb.org%2Fanthology%2FP02-1040.pdf&usg=AOvVaw2gUHBOkD7S63VbTz7hAKLx)

  an inexpensive automatic evaluation that is quick, language-independent, and correlates highly with human evaluation
  The closer a machine translation is to a professional human translation, the better it is
  To judge the quality of a machine translation, one measures its closeness to one or more reference human translations according to a numerical metric. Thus, our MT evaluation system requires two ingredients:
   1. a numerical “translation closeness” metric
   2. a corpus of good quality human reference trans- lations
  The main idea is to use a weighted average of variable length phrase matches against the reference translations
  The primary programming task for a BLEU implementor is to compare n-grams of the candidate with the n-grams of the reference translation and count the number of matches. These matches are position-independent. The more the matches, the better the candidate translation is.

