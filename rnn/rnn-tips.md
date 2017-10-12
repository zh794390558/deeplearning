# RNN tips

## regularizing

### Normalization

* [Layer Normalization](https://arxiv.org/abs/1607.06450)

* [Regularizing Recurrent Networks—On Injected Noise and Norm-based Methods](https://pdfs.semanticscholar.org/44a4/7c2bee3ea51c17bd8d16a64053c18856d427.pdf)

  method of regularizing for RNN

### Dropout 

* [Recurrent Neural Network Regularization](https://arxiv.org/abs/1409.2329)

  Zaremba et al. (2014) 
  Dropout to LSTM; The main idea is to apply the dropout operator only to the non-recurrent connections

* [Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks](https://arxiv.org/abs/1506.03099)

  Bengio et al. (2015) 
  scheduled sampling
  sampling decoder output and groud-truth to input of next decoder step

* [Recurrent Dropout without Memory Loss](https://arxiv.org/abs/1603.05118)

  Semeniuta et al.(2016)

  Pham et al. (2013) and Zaremba et al. (2014) have shown that LSTMs can be effectively regularized by using dropout in forward connections. While this already allows for effective regularization of recurrent networks, it is intuitive that introducing dropout also in the hidden state may force it to create more robust representations
  Moon et al. (2015) have extended the idea of dropping neurons in forward direction and proposed to drop cell states as well showing good results on a Speech Recognition task. 
  Bluche et al. (2015) carry out a study to find where dropout is most effective, e.g. input-to-hidden or hidden-to-output connections
  Bengio et al. (2015) have proposed an algorithm called scheduled sampling to improve performance of recurrent networks on sequence-to-sequence labeling tasks. A disadvantage of this work is that the scheduled sampling is specifically tailored to this kind of tasks, what makes it impossible to use in, for example, sequence-to-label tasks

  The authors conclude that it is more beneficial to use it once in the correct spot, rather than to put it everywhere
  The main contribution of this paper is a new recurrent dropout technique, which is most useful in gated recurrent architectures such as LSTMsand GRUs.
  We demonstrate that applying dropout to arbitrary vectors in LSTM cells may lead to loss of memory thus hindering the ability of the network to encode long-term information
  (i) while is straight-forward to use dropout in vanilla RNNs due to their strong similarity with the feed-forward architectures, its application to LSTM networks is not so straightforward. We demonstrate that recurrent dropout is most effective when applied to hidden state update vectors in LSTMs rather than to hidden states; (ii) we observe an improvement in the network’s performance when our recurrent dropout is coupled with the standard forward dropout, though the extent of this improvement depends on the values of dropout rates; (iii) contrary to our expectations, networks trained with per-step and persequence mask sampling produce similar results when using our recurrent dropout method, both being better than the dropout scheme proposed by Moon et al. (2015).


## Learning Rate

* [Learning Rate Warmup](https://arxiv.org/pdf/1706.03762.pdf)

## Length Penalty

* [Length Penalty]( https://arxiv.org/abs/1609.08144 )

