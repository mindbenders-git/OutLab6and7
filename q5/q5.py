import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv('data.csv')
Distinct_Ins=data['instance'].unique()
Distinct_Ins=data['instance'].unique()
Distinct_Algo=data['algorithm'].unique()
Distinct_epsilon=data['epsilon'].unique()
DF=data
df=DF.groupby('instance',axis=0)
inst=list()
for i in Distinct_Ins:
    inst.append(df.get_group(i))
for j in range(0,len(inst)):
    isn1algo=dict()
    inst1=inst[j].groupby('algorithm',axis=0)
    for k in Distinct_Algo:
        isn1algo[k]=inst1.get_group(k)
    #isn1algo[0].head(50)
    Ep1=aeg=isn1algo['epsilon-greedy']['epsilon'].unique()
    aeg=isn1algo['epsilon-greedy'].groupby('epsilon',axis=0)
    epgreedy=dict()
    for l in Ep1:
        epgreedy[l]=aeg.get_group(l)
    for ep in Ep1:
        greedyep=greedyep1=epgreedy[ep].groupby('horizon',axis=0)
        plt.plot(greedyep.mean()['regret'],'o-',label='greedy-epsilon'+str(ep))
    for alg in Distinct_Algo:
        if alg!='epsilon-greedy':
            algor=isn1algo[alg].groupby('horizon',axis=0)
            plt.plot(algor.mean()['regret'],'o-',label=alg,)


    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("horizon")
    plt.ylabel("regret")
    plt.title('horizon vs regret for various algorithms')
    plt.legend(loc='best',bbox_to_anchor =(1, .8))
    plt.grid()
    plt.savefig('instance'+str(j+1),facecolor='w',transparent=True,bbox_inches='tight')
    plt.close()