from wordcloud import WordCloud

import matplotlib.pyplot as plt

filename = "words.txt"
with open(filename) as f:
    mytext = f.read()
mytext

wordcloud = WordCloud().generate(mytext)

%pylab inline
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

