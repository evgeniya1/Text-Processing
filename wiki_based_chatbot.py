import nltk
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import wikipedia

lemmatizer = WordNetLemmatizer()


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


text = wikipedia.page('Vegetables').content

#text = 'Originally, vegetables were collected from the wild by hunter-gatherers. Vegetables are all plants. Vegetables can be eaten either raw or cooked.'

question = ''


def process(text, question):
  #extract sentences from the text
  sentence_tokens = nltk.sent_tokenize(text)
  sentence_tokens.append(question)

  tv = TfidfVectorizer(tokenizer=lemma_me)
  tf = tv.fit_transform(sentence_tokens)
  #find simularity
  values = cosine_similarity(tf[-1], tf[:-1])
  index_max = values.argmax()
  closest_sentence = sentence_tokens[index_max]
  #print(closest_sentence)
  if values.max() > 0.3:
    return closest_sentence


for i in range(5):
  question = input("Hi, what do you want to know?\n")
  output = process(text, question)

  if output:
    print(output)
  elif question == 'quit':
    break
  else:
    print("I do not know")
