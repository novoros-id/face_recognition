import pickle
import numpy as np

with open("embeddings/embeddings_prev.pkl", "rb") as f_prev:
    (saved_embeds_prev, names_prev) = pickle.load(f_prev)
    for i in names_prev:
        print (i)