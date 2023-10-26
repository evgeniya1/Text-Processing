import nltk
from nltk.stem import WordNetLemmatizer

#nltk.download('wordnet')
#nltk.download("punkt")
#nltk.download('averaged_perceptron_tagger')

x = 'was'
y = 'is'

lemmatizer = WordNetLemmatizer()
lemma_x = lemmatizer.lemmatize(x, pos='v')
lemma_y = lemmatizer.lemmatize(y, pos='v')

# print(x == y)
# print(lemma_x == lemma_y)

#lemmatization of sentences
sentences = ['i liked apples of', 'apples are red', 'apples are green']

sentence_tokens = nltk.word_tokenize(sentences[0].lower())
pos_tags = nltk.pos_tag(sentence_tokens)

sentence_lemmas = []

for token, pos_tag in zip(sentence_tokens, pos_tags):
  pos_tag_ = pos_tag[1][0].lower()
  if pos_tag_ in ['n', 'v', 'a', 'r']:
    lemma = lemmatizer.lemmatize(token, pos=pos_tag_)
    sentence_lemmas.append(lemma)

print(sentence_tokens)
print(sentence_lemmas)
