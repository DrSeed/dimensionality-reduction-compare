import os, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
os.makedirs("figures",exist_ok=True); os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(8)
X=np.vstack([rng.normal(m,1,(80,30)) for m in (0,5,10,15)]); lab=np.repeat(range(4),80)
p=PCA(2).fit_transform(X); t=TSNE(2,perplexity=30,init="pca",random_state=0).fit_transform(X)
fig,ax=plt.subplots(1,2,figsize=(10,4))
for a,e,ti in [(ax[0],p,"PCA"),(ax[1],t,"t-SNE")]:
    for k in range(4): a.scatter(e[lab==k,0],e[lab==k,1],s=10)
    a.set_title(ti)
fig.suptitle("PCA vs t-SNE on the same data (demo data)")
plt.tight_layout(); plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write("4 clusters, PCA vs tSNE\n"); print("ok")