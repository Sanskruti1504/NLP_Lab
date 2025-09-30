from nltk import ngrams
from nltk.util import ngrams

#unigram model
n = 1
sentence = 'The future of India will be shaped by today’s younger generation who need quality education through digital literacy, making them productive and self-reliant citizens. The digital is the skills required to achieve digital competence and use of Information and Communication Technology (ICT) for work, leisure, learning and communication. It does not replace traditional forms of literacy, instead complements and amplifies the skills that form the foundation of traditional forms.'

unigrams = ngrams(sentence.split(), n)
print(f"\n***********   UNIGRAM    ************************")
for item in unigrams:
    print(item)
#bigram model
n = 2
sentence = 'The future of India will be shaped by today’s younger generation who need quality education through digital literacy, making them productive and self-reliant citizens. Digital literacy is the skills required to achieve digital competence and use of Information and Communication Technology (ICT) for work, leisure, learning and communication. It does not replace traditional forms of literacy, instead complements and amplifies the skills that form the foundation of traditional forms.'

unigrams = ngrams(sentence.split(), n)
print(f"\n***********   BIGRAM    ************************")
for item in unigrams:
    print(item)

#trigram model
n = 3
sentence = 'The future of India will be shaped by today’s younger generation who need quality education through digital literacy, making them productive and self-reliant citizens. Digital literacy is the skills required to achieve digital competence and use of Information and Communication Technology (ICT) for work, leisure, learning and communication. It does not replace traditional forms of literacy, instead complements and amplifies the skills that form the foundation of traditional forms.'
unigrams = ngrams(sentence.split(), n)
print(f"\n***********   TRIGRAM    ************************")
for item in unigrams:
    print(item)

