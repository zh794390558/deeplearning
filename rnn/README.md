# RNN 

1. speech 

* [Attention-Based Models for Speech Recognition](https://arxiv.org/abs/1506.07503)
  location-based, content-based and hybrid attention 

* [SPEECH RECOGNITION WITH DEEP RECURRENT NEURAL NETWORKS](https://arxiv.org/abs/1303.5778)
   LSTM, BiRNN, multi-layer BiLSTM, CTC(acoustic-only model), RNN Transducer(jointly trained acoustic and language
model)
   RNN transducer [10] combines a CTC-like network with a separate RNN that predicts each phoneme given the previous ones, thereby yielding a jointly trained acoustic and language model.

* [Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with Recurrent Neural Networks](https://www.google.co.jp/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwi_6oHGi6HWAhUEvLwKHf08AycQFggmMAA&url=http%3A%2F%2Fciteseerx.ist.psu.edu%2Fviewdoc%2Fdownload%3Fdoi%3D10.1.1.75.6306%26rep%3Drep1%26type%3Dpdf&usg=AFQjCNHPF99UGSi8aSQM3np1OXLwI09gQw)
   CTC:Labelling unsegmented sequence data is a ubiquitous problem in real-world sequence learning.
   Currently, graphical models such as hidden Markov Models (HMMs; Rabiner, 1989), conditional random ﬁelds (CRFs; Laﬀerty et al., 2001) and their variants, are the predominant framework for sequence labeling.
   Drawbacks of HMM and CRF. for standard HMMs, training is generative, even though sequence labelling is discriminative
   The basic idea is to interpret the network outputs as a probability distribution over all possible label sequences, conditioned on a given input sequence.Given this distribution, an objective function can be derived that directly maximises the probabilities of the correct labellings.
   The objective function is derived from the principle of maximum likelihood. That is, minimising it maximises the log likelihoods of the target labellings.

* [Sequence to Sequence Learning with Neural Networks](https://www.google.co.jp/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiK3pzrzKHWAhVGxrwKHdCrChwQFggmMAA&url=https%3A%2F%2Fpapers.nips.cc%2Fpaper%2F5346-sequence-to-sequence-learning-with-neural-networks.pdf&usg=AFQjCNHkuuvss8h-_xyrytRBFTKQUb60Sg)
  While the LSTM is capable of solving problems with long term dependencies, we discovered that the LSTM learns much better when the source sentences are reversed.
  We were able to do well on long sentences because we reversed the order of words in the source sentence but not the target sentences in the training and test set.
  As typical neural language models rely on a vector representation for each word, we used a ﬁxed vocabulary for both languages. We used 160,000 of the most frequent words for the source language and 80,000 of the most frequent words for the target language. Every out-of-vocabulary word was replaced with a special “UNK” token

* [Recurrent Neural Network Regularization](https://arxiv.org/abs/1409.2329)
  Dropout to LSTM; The main idea is to apply the dropout operator only to the non-recurrent connections 

* [Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks](https://arxiv.org/abs/1506.03099)
  
* [Residual Convolutional CTC Networks for Automatic Speech Recognition](https://arxiv.org/pdf/1702.07793.pdf)

* [Convolutional Neural Networks for Speech Recognition](https://pdfs.semanticscholar.org/86ef/e7769f2b8a0e15ca213ab09881e6705caeb0.pdf)

* [Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](https://arxiv.org/abs/1512.02595)

* [NEURAL MACHINE TRANSLATION BY JOINTLY LEARNING TO ALIGN AND TRANSLATE](https://arxiv.org/abs/1409.0473)

* [Attention-Based Models for Speech Recognition](https://arxiv.org/abs/1506.07503)

* [Attention-Based End-to-End Speech Recognition in Mandarin](https://arxiv.org/abs/1707.07167)

* [Advances in Joint CTC-Attention based End-to-End Speech Recognition with a Deep CNN Encoder and RNN-LM](https://arxiv.org/pdf/1706.02737.pdf)

* [Regularizing Recurrent Networks—On Injected Noise and Norm-based Methods](https://pdfs.semanticscholar.org/44a4/7c2bee3ea51c17bd8d16a64053c18856d427.pdf)

* [END-TO-END ATTENTION-BASED LARGE VOCABULARY SPEECH RECOGNITION](https://arxiv.org/pdf/1508.04395.pdf)

* [Listen, Attend and Spell](https://arxiv.org/pdf/1508.01211.pdf)
  本文写的很好，值得一看。有作者训练的经验，模型的理解。方法描述简单清晰。非常适合经验不足的同学看。
  This attention vector can be thought of as skip connections that allow the information and the gradients to flow more effectively in an RNN.
  The attention model was also able to identify the start and end of the utterance properly.
