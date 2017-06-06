# cifar10

# src 

https://github.com/tensorflow/models/tutorials/image/cifar10

# train data

放在我的百度云盘： 我的文档/data/cifar10

# run 

docker images:  bootstrapper:5000/liuqs_public/tensorflow:1.1.0-gpu

使用可以参考： https://github.com/k8sp/k8s-tensorflow.git 

# train 

使用 cifar10_train.py 做训练，初始没有训练数据，他会下载训练数据到 /tmp目录下，并解压缩。
使用的是 cpu 做数据的训练。 将训练数据 cifar10_train 保存下来，使用 tensorborad 可以看到训练中的参数。

# tensorborad 

```bash
pip install tensorborad

tensorboard --logdir cifar10_train/
```

# reference

[卷积神经网络](http://wiki.jikexueyuan.com/project/tensorflow-zh/tutorials/deep_cnn.html)


