"""
	Hay que descargar primero los Stopwords antes de seleccionar el idioma español con:
	nltk.download('stopwords')
"""

import pickle as p # Serializar
from nltk.corpus import stopwords # Tokenizar
from nltk import word_tokenize # Tokenizar
from string import punctuation # Tokenizar
from inscripcionTesis.models import Tesis as T
import gensim # Word2Vec
from sklearn.metrics.pairwise import cosine_similarity as cs # Similitud coseno

model = gensim.models.KeyedVectors.load_word2vec_format('sbw_vectors.bin', binary=True) # Word2Vec

file= open('todasTesis.pickle','rb')
resumenes= p.load(file)
file.close()

spanish_stopwords= stopwords.words('spanish')

#Para remover la puntuacion
non_words = list(punctuation)
#Agregamos puntuacion usada en el idioma español
non_words.extend(['¿','¡'])
non_words.extend(map(str,range(10)))

cont= 0
for x in resumenes:
	caracteres= ''.join([c for c in x[4] if c not in non_words])
	
	#AQUI SE NECESITA PRIMERO LA DESCARGA
	tokens = word_tokenize(caracteres)
	#tokens_filtrados = [token for token in tokens if token not in spanish_stopwords]
	if not tokens:
		w2v= [0 for x in range(300)]
	else:
		w2v= [0 for x in range(300)]
		for w in tokens:
			#print(len(tokens),tokens)
			#print(len(w2v),w2v)
			if w in model:
				w2v+= model[w]
	print(len(w2v),w2v)
	tesis= T()
	tesis.numeroTesis= int(x[0]) if x[0]!= '' else 0
	tesis.nombreTesis= x[1] if x[1]!= '' else ""
	tesis.alumnoAps= x[2].split(', ')[0] if x[2]!= '' else ""
	tesis.alumno= x[2].split(', ')[1] if x[2]!= '' else ""
	tesis.director1Aps= x[3].split(', ')[0] if x[3]!= '' else ""
	tesis.director1= x[3].split(', ')[1] if x[3]!= '' else ""
	tesis.abstrac= x[4] if x[4]!= '' else ""
	tesis.diaCreacion= x[5] if x[5]!= '' else '1920-01-01'
	tesis.valorW2V= w2v
	tesis.save()
	if cont<2:
		cont+= 1
	else:
		break
