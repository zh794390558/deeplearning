#include "cstdio"
#include "iostream"
#include "fstream"
#include "vector"
#include "sstream"
#include "string"
#include "math.h"
using namespace std;
#define N 500
#define delta 0.0001
#define alpha 0.1
#define cin fin
struct Data
{
    vector<int> feature;
    int y;
    Data(vector<int> feature,int y):feature(feature),y(y) {}
};
struct Parament
{
    vector<double> w;
    double b;
    Parament() {}
    Parament(vector<double> w,double b):w(w),b(b) {}
};
vector<Data> dataSet;
Parament parament;
void read()
{
    ifstream fin("traindata.txt");
    int id,fea,cls,cnt=0;
    string line;
    while(getline(cin,line))
    {
        stringstream sin(line);
        vector<int> feature;
        sin>>id;
        while(sin>>fea) feature.push_back(fea);
        cls=feature.back();feature.pop_back();
        dataSet.push_back(Data(feature,cls));
    }
    parament=Parament(vector<double>(dataSet[0].feature.size(),0.0),0.0);
}
double calcInner(Parament param,Data data)
{
    double ret=0.0;
    for(int i=0;i<data.feature.size();i++) ret+=(param.w[i]*data.feature[i]);
    return ret+param.b;
}
double sigmoid(Parament param,Data data)
{
    double inner=calcInner(param,data);
    return exp(inner)/(1+exp(inner));
}
double calcLW(Parament param)
{
    double ret=0.0;
    for(int i=0;i<dataSet.size();i++)
    {
        double h=sigmoid(param,dataSet[i]);
        ret+=(dataSet[i].y*log(h))+(1-dataSet[i].y)*log(1-h);
    }
    return ret;
}
void gradient(Parament &param,int iter)
{
    /*batch
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
    for(int j=0;j<dataSet.size();j++)
    {
        double ret=0.0,h=sigmoid(param,dataSet[j]);
        double ALPHA=(double)0.1/(iter+j+1)+0.1;
        for(int i=0;i<param.w.size();i++)
            param.w[i]+=ALPHA*(dataSet[j].y-h)*dataSet[j].feature[i];
        param.b+=alpha*(dataSet[j].y-h);
    }
}
bool samewb(Parament p1,Parament p2)
{
    for(int i=0;i<p1.w.size();i++)
        if(fabs(p2.w[i]-p1.w[i])>delta) return false;
    if(fabs(p2.b-p1.b)>delta) return false;
    return true;
}
void classify()
{
    ifstream fin("testdata.txt");
    int id,fea,cls;
    string line;
    while(getline(cin,line))
    {
        stringstream sin(line);
        vector<int> feature;
        sin>>id;
        while(sin>>fea) feature.push_back(fea);
        cls=feature.back();feature.pop_back();
        double p1=sigmoid(parament,Data(feature,cls)),p0=1-p1;
        cout<<"id:"<<id<<"  origin:"<<cls<<" classify:";
        if(p1>=p0) cout<<" 1"<<endl;
        else cout<<" 0"<<endl;
    }
}
void mainProcess()
{
    double objLW=calcLW(parament),newLW;
    Parament old=parament;
    int iter=0;
    gradient(parament,iter);
    newLW=calcLW(parament);
    while(fabs(newLW-objLW)>delta||!samewb(old,parament))
    {
        objLW=newLW;
        old=parament;
        gradient(parament,iter);
        newLW=calcLW(parament);
        iter++;
        if(iter%5==0) cout<<"iter: "<<iter<<"  target value: "<<newLW<<endl;
    }
    cout<<endl<<endl;
}
int main()
{
    read();
    mainProcess();
    classify();
}
