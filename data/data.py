import pickle
import pandas as pd

file = open('data/viz_df.p', 'rb')
viz_df = pickle.load(file)
file.close()

comps = ['pc1', 'pc2', 'pc3', 'pc4', 'pc5', 'pc6']
text_data = ['sample', 'url', 'date']
col_options = [dict(label=x, value=x) for x in comps]
sentiment = ['w_protest', 'w_econ', 'w_gov', 'w_poli', 'protest_ratio', 'econ_ratio', 'gov_ratio', 'poli_ratio']
sent_options = [dict(label=x, value=x) for x in sentiment]
dimensions = ["x", "y", "z"]
models = ['Hierarchical', 'K-Means', 'Mean Shift', 'Spectral']