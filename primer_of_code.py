import numpy as np
import pickle
import shutil

with open("embeddings/embeddings.pkl", "rb") as f:
    (saved_embeds, names) = pickle.load(f)

    print(saved_embeds.ndim)
    print(saved_embeds.ndim + 1)
    print(len(saved_embeds))
    print(len(names))

    for i in names:
        print (i)

    print(type(saved_embeds))
    print(type(names))

    # print(saved_embeds)
    # print(names)

    # shutil.copyfile("embeddings/embeddings.pkl", "embeddings/embeddings_prev.pkl")
    #
    # print ("-----------------------")
    #
    # new_embeds = np.vstack ((saved_embeds,saved_embeds))
    # new_names = names + names
    #
    # print(new_embeds.ndim)
    #
    # print(len(new_embeds))
    # print(len(new_names))
    #
    # print(type(saved_embeds))
    # print(type(new_names))