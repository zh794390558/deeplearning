/**
 * 
 * @name:
 *  softmax regression
 *  
 * @describe:
 *    Softmax回归是Logistic回归的泛化版本，用于解决线性多类（K类）的分类问题。
 *    Logistic回归可以看作是Softmax回归在K=2时的特例。Softmax函数即是K分类版的Logistc函数。
 * 
 * @site:
 *     http://www.cnblogs.com/neopenx/p/4316611.html
 * */

#include "cstdio"
#include "iostream"
#include "fstream"
#include "vector"
#include "sstream"
#include "string"
#include "math.h"

using namespace std;

#define M 500   /* dataset size*/
#define delta 0.0001 /* threshold for convergence */
#define alpha 0.1  /*learning rate*/
#define K 2        /* K-fold */
#define Dim dataSet[0].feature.size() /* data dim or feature size, N */
#define cin fin

struct Data
{
    vector<double> feature; /* X */
    int y;
    Data(vector<double> feature,int y) : feature(feature), y(y) {}
};

struct Parament
{
    vector<double> w; /*weight*/
    double b;         /*bias*/
    Parament() {}
    Parament(vector<double> w, double b) : w(w), b(b) {}
};

vector<Data> dataSet;  /* X, y */
vector<Parament> parament; /* W, b */

void read()
{
    ifstream fin("fullTrain.txt");
    double fea; int cls;
    string line;
    while(getline(cin,line))
    {
        stringstream sin(line);
        vector<double> feature;
        while(sin>>fea) feature.push_back(fea);
        cls=feature.back();feature.pop_back();
        dataSet.push_back(Data(feature, cls));
    }
    for(int i=0; i<K; i++) parament.push_back(Parament(vector<double>(Dim, 0.0) , 0.0));
}

double calcInner(Parament param, Data data)
{
    /* W.dot(X) + b*/
    double ret=0.0;
    for(int i=0; i < data.feature.size(); i++) ret += (param.w[i] * data.feature[i]);
    return ret + param.b;
}

/* Probility per class (K-fold) */
double calcProb(int j, Data data)
{
    double ret=0.0, spec=0.0;
    for(int l=1; l <= K; l++)
    {
        double tmp = exp(calcInner(parament[l-1], data));
        if(l==j) spec = tmp;
        ret += tmp;
    }
    return spec / ret;
}

/* loss function */
double calcLW()
{
    double ret=0.0;
    for(int i=0; i<dataSet.size(); i++)
    {
        double prob=calcProb(dataSet[i].y, dataSet[i]);
        ret+=log(prob);
    }
    return ret;
}

/* Gradient Up */
void gradient(int iter)
{
    /*batch (logistic)
      for(int i=0;i<param.w.size();i++)
      {
      double ret=0.0;
      for(int j=0;j<dataSet.size();j++)
      {
      double ALPHA=(double)0.1/(iter+j+1)+0.1;
      ret+=ALPHA*(dataSet[j].y-sigmoid(param,dataSet[j]))*dataSet[j].feature[i];
      }
      param.w[i]+=ret;
      }
      for(int i=0;i<dataSet.size();i++) ret+=alpha*(dataSet[i].y-sigmoid(param,dataSet[i]));
      */
    //random
    for(int j=0; j < dataSet.size(); j++)
    {
        double ret=0.0, prob=0.0;
        /* learning rate [0.1, 0.11] */
        double ALPHA = (double)0.1 / (iter + j + 1) + 0.1;
        for(int k=1; k <= K; k++)
        {
            /* gradient of loss fucntion */
            prob=((dataSet[j].y==k ? 1:0) - calcProb(k, dataSet[j]));
            /*update weight*/
            for(int i=0;i<Dim;i++) parament[k-1].w[i] += ALPHA * prob * dataSet[j].feature[i];
            /*updata bias*/
            parament[k-1].b += ALPHA * prob;
        }
    }
}

/* prediction */
void classify()
{
    ifstream fin("fullTest.txt");
    double fea; int cls, no=0;
    string line;
    while(getline(cin,line))
    {
        stringstream sin(line);
        vector<double> feature;
        while(sin>>fea) feature.push_back(fea);
        cls=feature.back(); feature.pop_back();
        int bestClass =-1; double bestP=-1;
        for(int i=1; i<=K; i++)
        {
            /* probility per class */
            double p = calcProb(i, Data(feature,cls));
            /* max probility is the class */
            if(p>bestP) { bestP=p; bestClass=i;}
        }
        cout<<"Test:"<<++no<<"  origin:"<<cls<<" classify:"<<bestClass<<endl;
    }
}

/* fit or train */
void mainProcess()
{
    double objLW = calcLW(), newLW;
    int iter=0;
    gradient(iter);
    newLW = calcLW();
    /* convergence */
    while(fabs(newLW-objLW) > delta)
    {
        objLW = newLW;
        gradient(iter);
        newLW = calcLW();
        iter++; /* gradient up */
        if(iter%5==0) cout<<"iter: "<<iter<<"  target value: "<<newLW<<endl;
    }
    cout<<endl<<endl;
}

int main(void)
{
    /* get dataset */
    read();
    /* tarin */
    mainProcess();
    /*predication*/
    classify();

    return 0;
}

