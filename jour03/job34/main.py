#En analysant à nouveau le fichier “data.txt”, établissez des statistiques synthétisant le
#nombre de mots par phrase. Produisez un histogramme présentant ces statistiques,
#puis, à l’aide de votre générateur de mot, créez un générateur de phrases à consonance
#de “Lorem Ipsum”.

import matplotlib.pyplot as plt

with open("data.txt", "r") as f:
    sentences = f.readlines()

word_counts = [len(sentence.split()) for sentence in sentences]
plt.hist(word_counts, bins=range(0, 30, 2), color='blue')
plt.title('Distribution du nombre de mots par phrase')
plt.xlabel('Nombre de mots')
plt.ylabel('Fréquence')
plt.show()
