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
def exponential_fit(x,Amp,xoffset,expo,offset):
    offset=0
    return Amp*1.*((x-xoffset)**expo)+offset
    #return Amp*1.*(x**a)+b


bitcoinwerte=pd.read_csv("btcusd_1-min_data.csv")

#np.savez("bitcoin.npz", bitcoinwerte.to_numpy())
bitcoinwerte["Zeiten"] = bitcoinwerte["Timestamp"]
bitcoinwerte["Zeiten"] = pd.to_datetime(bitcoinwerte['Timestamp'],unit='s')
bitcoinwerte_tag = bitcoinwerte[::1440]# )-1.325412e+09)/(24*60*60)
print("bitcoinwerte_tag",bitcoinwerte_tag)

#plt.figure(dpi=150, figsize=(10,6))
fig, ax1 = plt.subplots(dpi=150, figsize=(10,6))
#ax2 = ax1.twinx()

counter =np.array(range(len(bitcoinwerte_tag["Open"][::])))

parameters, covariance = curve_fit(exponential_fit, np.array(counter), np.array(bitcoinwerte_tag["Open"][::])  , 
    #p0=[ 4.41445307e-01 ,-2.49999845e+04 , 1.91248104e+00 ,-2.50000000e+14],

    bounds=Bounds(
    lb=[0.00001,-500,1,0],
    ub=[0.9,0,3,10])

)

print(parameters)

ax1.plot(counter,bitcoinwerte_tag["Open"][::])
ax1.plot(counter,exponential_fit(np.array(counter),parameters[0],parameters[1],parameters[2],parameters[3]))
ax1.plot(counter,exponential_fit(np.array(counter),parameters[0],parameters[1],parameters[2]*1.05,parameters[3]))
ax1.plot(counter,exponential_fit(np.array(counter),parameters[0],parameters[1],parameters[2]*0.95,parameters[3]))


ax1.set_ylabel("Dollar")
ax1.set_xlabel("Zeit")
ax1.set_yscale("log")   
ax1.set_ylim((0.1,200000))

ax1.grid()

plt.savefig("Bitcoin Schlauch.png")


