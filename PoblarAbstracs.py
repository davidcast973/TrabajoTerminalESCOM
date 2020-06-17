"""
Hay que descargar primero los Stopwords antes de seleccionar el idioma español con:
   nltk.download('stopwords')
"""

from nltk.corpus import stopwords
from nltk import word_tokenize
from inscripcionTesis.models import Tesis as T
import pickle as p

#AQUI SE NECESITA PRIMERO LA DESCARGA
spanish_stopwords= stopwords.words('spanish')



file= open('../Resumenes.pickle','rb')
resumenes= p.load(file)
file.close()

for x in resumenes:
   tesis= T()
   tesis.numeroTesis= int(x[0]) if x[0]!= '' else 00000
   tesis.nombreTesis= x[1] if x[1]!= '' else  ""
   tesis.alumnoAps= x[2].split(', ')[0] if x[2]!= '' else  ""
   tesis.alumno= x[2].split(', ')[1] if x[2]!= '' else  ""
   tesis.director1Aps= x[3].split(', ')[0] if x[3]!= '' else  ""
   tesis.director1= x[3].split(', ')[1] if x[3]!= '' else  ""
   tesis.abstrac= x[4] if x[]!= '' else  ""
   tesis.diaCreacion= x[5] if x[]!= '' else '1920-01-01'
   tesis.save()