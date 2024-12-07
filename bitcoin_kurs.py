import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


bitcoinwerte=pd.read_csv("btcusd_1-min_data.csv")

#np.savez("bitcoin.npz", bitcoinwerte.to_numpy())
bitcoinwerte["Zeiten"] = bitcoinwerte["Timestamp"]
bitcoinwerte["Zeiten"] = pd.to_datetime(bitcoinwerte['Timestamp'],unit='s')
bitcoinwerte_tag = bitcoinwerte[::1440]
print("bitcoinwerte_tag",bitcoinwerte_tag)

#plt.figure(dpi=150, figsize=(10,6))
fig, ax1 = plt.subplots(dpi=150, figsize=(10,6))
ax2 = ax1.twinx()

ax1.plot(bitcoinwerte_tag["Zeiten"][::],bitcoinwerte_tag["Open"][::])
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


