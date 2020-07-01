"""
   Hay que descargar primero los Stopwords antes de seleccionar el idioma español con:
   nltk.download('stopwords')
"""

import pickle as p # Serializar
from nltk.corpus import stopwords # Tokenizar
from nltk import word_tokenize, download # Tokenizar
from string import punctuation # Tokenizar
from inscripcionTesis.models import Tesis as T
import gensim # Word2Vec
from sklearn.metrics.pairwise import cosine_similarity as cs # Similitud coseno
from datetime import datetime # Castear a fecha AAAA-MM-DD
from os import system as os

model = gensim.models.KeyedVectors.load_word2vec_format('sbw_vectors.bin', binary=True) # Word2Vec

file= open('todasTesis.pickle','rb')
resumenes= p.load(file)
file.close()

#QUITARSTOPdownload('stopwords') #Descargar elementos necesarios para el filtrado de stopwords
#QUITARSTOPspanish_stopwords= stopwords.words('spanish')

non_words = list(punctuation)
non_words.extend(['¿','¡','\n','\r'])
non_words.extend(map(str,range(10)))

for x in resumenes:
   texto= list()
   for c in tex:
      if c not in non_words:
         texto.append(c)
      elif c == '\n':
         texto.append(' ')

   caracteres= ''.join(texto)
   tokens = word_tokenize(caracteres)
   if not tokens:
      w2v= ','.join([str(0) for x in range(300)])
   else:
      w2v= [0 for x in range(300)]
      for w in tokens:
         if w in model:
            w2v+= model[w]
   tesis= T()
   tesis.numeroTesis= int(x[0]) if x[0]!= '' else 0
   tesis.nombreTesis= x[1] if x[1]!= '' else ""
   tesis.alumnoAps= x[2].split(', ')[0] if x[2]!= '' else ""
   tesis.alumno= x[2].split(', ')[1] if x[2]!= '' else ""
   tesis.director1Aps= x[3].split(', ')[0] if x[3]!= '' else ""
   tesis.director1= x[3].split(', ')[1] if x[3]!= '' else ""
   tesis.abstrac= x[4] if x[4]!= '' else ""
   if len(x[5])==10:   # AAAA-MM-DD -> 10 o DD/MM/AAAA
      if '-' in [c for c in x[5]]:
         tesis.diaCreacion= x[5]
      else:
         tesis.diaCreacion= str(datetime.strptime(x[5], '%d/%m/%Y'))[:11]
   elif len(x[5])==7:   # AAAA-MM -> 7
      tesis.diaCreacion= x[5]+'-01'
   elif len(x[5])==4:   # AAAA -> 4
      tesis.diaCreacion= x[5]+'-01-01'
   elif len(x[5])==8:   # AAAA- MM -> 8
      tesis.diaCreacion= x[5][:5]+x[5][6:]+'-01'
   elif len(x[5])==0 or len(x[5])==9 :   #  -> 0 o 'sin fecha' -> 9
      tesis.diaCreacion= '1920-01-01'
   #tesis.diaCreacion= x[5] if x[5]!= '' else '1920-01-01'
   tesis.valorW2V= ','.join([str(w) for w in w2v])
   tesis.save()
