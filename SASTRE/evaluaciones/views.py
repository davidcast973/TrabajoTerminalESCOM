from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
from string import punctuation
import os
from django.conf import settings
from .models import *

# Create your views here.

@login_required(login_url='/cuenta/login/')
def evaluarProfesor(request):
	preguntas = Pregunta.objects.all()
	return render(request, 'evaluarProfesor.html', {'preguntas': preguntas})

@login_required(login_url='/cuenta/login/')
def materiasCursadas(request):
	return render(request, 'listadoMaterias.html')

@login_required(login_url='/cuenta/login/')
def etiquetadoTexto(request):
	mensaje = "Prueba"
	#lista de stopwors a utilizar
	spanish_stopwords  = stopwords.words('spanish')

	#Stemmer en español
	stemmer = SnowballStemmer('spanish')

	#Para remover la puntuacion
	non_words = list(punctuation)
	#Agregamos puntuacion usada en el idioma español
	non_words.extend(['¿','¡'])
	non_words.extend(map(str,range(10)))

	palabrasEtiquetadas = 0
	palabrasTotal = 0
	diccionario = {}
	palabrasEtiquetadas = 0

	#Se abre el diccionario de sentimeintos y se guarda
	with open(os.path.join(settings.BASE_DIR, 'evaluaciones/static/dictionaries/SEL.txt'),'r') as diccionarioSentimientos:
		mensaje = "Prueba: Se logro leer el diccionario"
		for palabra in diccionarioSentimientos:
			diccionario.update({palabra.split("	")[0] : palabra.split("	")[2]})

	#Se abren los archivos de texto con las opiniones
	for i in range(1,2):
		textoEtiquetado = {}
		archivo = "WebScraping/opiniones" + str(i) + ".txt"
		txtEtiquetado = "txtEtiquetado" + str(i) + ".txt"
		with open(archivo,'r') as f:
			for linea in f:
				print (len(linea))
				tokens = word_tokenize(linea)
				print (tokens)
				#for palabra in linea.split():
					#palabrasTotal +=1
					#if (diccionario.get(palabra) != None):
						#palabrasEtiquetadas += 1
						#print (palabra)
						#textoEtiquetado.update({palabra : diccionario.get(palabra)})
		#print(txtEtiquetado)
		#f=open(txtEtiquetado,"w+")
		#f.write(str(textoEtiquetado))
		#f.close()


	#print ("Palabras diferentes =", len(palabrasDiferentesTxt))
	#print (palabrasDiferentesTxt)
	#print (diccionario.get('xd'))
	#print ("Textos etiquetados",i)
	#print ("Se etiquetaron",palabrasEtiquetadas,"palabras de", palabrasTotal,"palabras en los textos, un total de",(palabrasEtiquetadas*100)/palabrasTotal,"%")
	#print (textoEtiquetado)
	return render(request, 'evaluarProfesor.html', {'mensaje': mensaje})

#Funcion para eliminar stopwords
def quitar_stopwords(tokens):
	tokens_filtrados = [token for token in tokens if token not in spanish_stopwords]
	return tokens_filtrados

#Funcion para reducir una palabra a su raiz
def stem_tokens(tokens, stemmer):
	stemmed = []
	for item in tokens:
		stemmed.append(stemmer.stem(item))
	return stemmed

#Funcion para generar tokens a partir del texto
def tokenize(text):
	#Remover la puntuación
	text = ''.join([c for c in text if c not in non_words])
	#Remover caracteres repetidos
	text = re.sub(r'(.)\1+', r'\1\1', text)
	#Generar tokens
	tokens = word_tokenize(text)

	#Stemming
	try:
		stems = stem_tokens(tokens, stemmer)
	except Exception as e:
		print(e)
		print(text)
		stems = ['']

	return stems