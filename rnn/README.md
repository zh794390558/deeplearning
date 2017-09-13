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
