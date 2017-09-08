# GENERATIVE ADVERSARIAL NETWORK-BASED POSTFILTER FOR STATISTICAL PARAMETRIC SPEECH SYNTHESIS

# data 

1. 大约 13~14h 的含静音的数据集。

1. SYN(合成语音) 和 NAT(自然语音) 特征是对齐的。

1. 22KHz, mono, mel-cepestrum

# Notes

1. 尝试 FCN 上输入变成语音，但是这种实现需要 batch_size 为 1， 且不能有 Padding 的数据。

1. 在切除静音的数据集上测试，会出现开头 80 帧左右的数值很小，导致合成的语音语谱图上只有 pitch 的能量。

1. 在含静音的数据集上测试，使用 slipping window + 50% overlap，固定输入 41(MCC)x200(frames) ， 可以收敛。

1. 使用 NAT 的 F0 且最终结果好于 SYN 的语音，但是差于 NATUARE 的语音。但是，使用 NAT F0 会出现部分基频模糊现象。更改为 SYN F0 后此问题消失。  

1. Inference 时使用分帧 inference 的方式，最后拼接成整个语音。在每帧的连接处的语谱图上有一条竖线。更改为整段语音 inference 后，此问题解决。

# impartant 

1. dcgan loss

	* single gpu with batch size 128, lr=1e-4
	* Enforced
	* the best one

1. lsgan loss

	* double gpu with batch size 128, lr=1e-4 (maybe 256 batch size is good)
	* Enforced
	* unvoice has some high energe in low dimension. 
	* some nosie

1. wgan-gp loss

	* Enforced, but has some big value in time dimension.
	* unvoice has some high energe in low dimension. 
	* some nosie

1. 200 frames slipping windown and 50% overlap of feautre.

1. No Batch Norm is good. 

1. Z-score pre-prosess of data is good.

1. D and G learning rate = 1e-4; batch_size = 128 is work. 100K step is perfered. 

1. 不含静音的数据集可以工作，含静音的数据集没有测试。

# Reference

1. [DIGITS-GAN](https://github.com/NVIDIA/DIGITS)
   This is the repo framework

	* [GAN-mnist](https://github.com/NVIDIA/DIGITS/blob/master/examples/gan/network-mnist.py)

	* [Model Exmaples](https://github.com/NVIDIA/DIGITS/tree/master/examples)

	* [Model Template](https://github.com/NVIDIA/DIGITS/tree/master/digits/tools/tensorflow)

1. [DCGAN](https://github.com/carpedm20/DCGAN-tensorflow/)

1. [SEGAN: Speech Enhancement Generative Adversarial Network](https://github.com/santi-pdp/segan)

	* `4.2 SEGAN's setup is a good guide to this work.`

# Author 
1. NTT Corporation. 

1. [Takuhiro Kaneko](http://www.kecl.ntt.co.jp/people/kaneko.takuhiro/index.html)

1. [Generative Adversarial Network-based Postfilter for STFT Spectrograms](http://www.kecl.ntt.co.jp/people/kaneko.takuhiro/projects/ganp_stft/index.html)
# TODO


