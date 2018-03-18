In order to recognize language, cmusphinx requires:

* an acoustic model
* a (single) dictionary of words, containing pronunciation
* a (single) language model, containing occurrence probability for words and sequences of words

We assume someone else has already created the acoustic model.

Talking about dictionary and language model, we consider a good idea to combine LiSpeak-specific dictionaries and generic ones.
We can use e.g. lm_combine or ngram -mix-lm.

This online tool generates a language model from a corpus: http://www.speech.cs.cmu.edu/tools/lmtool-new.html
It creates also a dictionary, but you can ignore it, as language is supposed to be English AFAIK.


