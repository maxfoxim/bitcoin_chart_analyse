import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit,Bounds

"""
To Do:
200 Tage Trend
Mustererkennung

https://codefinity.com/blog/Creating-Crypto-Graphs-in-Python

https://www.geeksforgeeks.org/bitcoin-price-prediction-using-machine-learning-in-python/
"""
def exponential_fit(x,Amp,a,b):
    return Amp*1.*(x**a)+b


bitcoinwerte=pd.read_csv("btcusd_1-min_data.csv")

#np.savez("bitcoin.npz", bitcoinwerte.to_numpy())
bitcoinwerte["Zeiten"] = bitcoinwerte["Timestamp"]
bitcoinwerte["Zeiten"] = pd.to_datetime(bitcoinwerte['Timestamp'],unit='s')
bitcoinwerte_tag = bitcoinwerte[::1440]
print("bitcoinwerte_tag",bitcoinwerte_tag)

#plt.figure(dpi=150, figsize=(10,6))
fig, ax1 = plt.subplots(dpi=150, figsize=(10,6))
ax2 = ax1.twinx()

counter =np.array(range(len(bitcoinwerte_tag["Open"][::])))

parameters, covariance = curve_fit(exponential_fit, np.array(counter), np.array(bitcoinwerte_tag["Open"][::]),   
    bounds=Bounds(
    lb=[-10,0.1,-100],
    ub=[10,10,100],
))

print(parameters)

ax1.plot(counter,bitcoinwerte_tag["Open"][::])
ax1.plot(counter,exponential_fit(np.array(counter),parameters[0],parameters[1],parameters[2]))

ax1.set_ylabel("Dollar")
ax1.set_xlabel("Zeit")
ax1.set_yscale("log")   
ax1.set_ylim((0.1,200000))

ax1.grid()

bitcoinwerte_tag_diff = bitcoinwerte_tag[::].set_index('Zeiten').diff()

prop = ( bitcoinwerte_tag_diff["Open"]/bitcoinwerte_tag["Open"].values ) * 100
print(bitcoinwerte_tag_diff,"Länge Prop",len(prop))
ax2.plot(bitcoinwerte_tag_diff.index,prop,color="r")
ax2.set_ylabel("Änderung")
ax2.set_xlabel("Zeit")
ax2.set_yticks([-20,-10,0,10,20]) 
ax2.set_ylim((-20,150))
#ax2.grid()

plt.show()


