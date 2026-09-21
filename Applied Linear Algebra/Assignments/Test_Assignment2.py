from Assignment2 import get_word_vector
import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")
def test_emptyTags():
    res = get_word_vector(model,[])
    assert res==([],[])