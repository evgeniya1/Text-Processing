import nltk
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer

lemmatizer = WordNetLemmatizer()
#nltk.download('wordnet')
#nltk.download("punkt")
#nltk.download('averaged_perceptron_tagger')
#nltk.download('vader_lexicon')


def lemma_me(sentence):
  sentence_tokens = nltk.word_tokenize(sentence.lower())
  pos_tags = nltk.pos_tag(sentence_tokens)

  sentence_lemmas = []

  for token, pos_tag in zip(sentence_tokens, pos_tags):
    pos_tag_ = pos_tag[1][0].lower()
    if pos_tag_ in ['n', 'v', 'a', 'r']:
      lemma = lemmatizer.lemmatize(token, pos=pos_tag_)
      sentence_lemmas.append(lemma)

  return sentence_lemmas

with open('sentences.txt', 'r') as file:
  text = file.read()

question='What are vegetables?'

#extract sentences from the text
sentence_tokens = nltk.sent_tokenize(text)
sentence_tokens.append(question)

tv = TfidfVectorizer(tokenizer = lemma_me)
tf = tv.fit_transform(sentence_tokens)

import pandas as pd

df = pd.DataFrame(tf.toarray(), columns=tv.get_feature_names_out())

print(df)

#find simularity
from sklearn.metrics.pairwise import cosine_similarity
values = cosine_similarity(tf[-1], tf[:-1])

print(values)

index_max = values.argmax()
closest_sentence = sentence_tokens[index_max]

print(closest_sentence)
