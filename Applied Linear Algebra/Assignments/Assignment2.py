import re
import numpy as np

import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")

TAGS = ["research", "innovation", "education", "university", "students",
"faculty", "campus", "engineering", "medicine", "technology", "curriculum", "collaboration", "publication",
"laboratory", "scholarship", "mentorship", "internship", "entrepreneurship", "accreditation", "alumni"]

def get_word_vector(model,tags):
    dropped_words =[]
    wor_vectors=[]

    for tag in tags:
        try:
            tv = model[tag]
            wor_vectors.append(tv)
        except:
            dropped_words.append(tag)
            wor_vectors.append(None)

    return (dropped_words,wor_vectors)


def main():
    vec = get_word_vector(model,TAGS)
    print("Dropped vectors are: ",vec[0])
    print("The number of present tags are: ",len(vec[1]))

if __name__ =="__main__":
    main()