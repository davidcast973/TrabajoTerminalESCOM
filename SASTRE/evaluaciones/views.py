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
from django.contrib.auth.models import User
from usuario.models import Alumno, Profesor
from ofertaEducativa.models import SituacionEscolar, UnidadAprendizaje
from evaluaciones.models import Cuestionario
from django.core.exceptions import ObjectDoesNotExist
#Librerias para graficar
import matplotlib.pyplot as plt

# Create your views here.

@login_required(login_url='/cuenta/login/')
def evaluacionProfesorInicio(request):
	user = request.user
	if (Alumno.objects.filter(username= user).count()) > 0:		#Verifica si es un alumno
		situacionEscolar = SituacionEscolar.objects.filter(usuario=user, evaluacionProfesor=False)
		if (SituacionEscolar.objects.filter(usuario=user, evaluacionProfesor=False).count()) > 0:
			return render(request, 'listadoMaterias.html', {'situacionEscolar': situacionEscolar})
		else:
			mensaje = "Ya has evaluado a todos tus profesores"
		return render(request, 'listadoMaterias.html', {'mensaje': mensaje})
	else:
		mensaje = "Lo sentimos este módulo esta disponible solo para alumnos"
		return render(request, 'listadoMaterias.html', {'mensaje': mensaje})
	return render(request, 'listadoMaterias.html', {'mensaje': ['Se presento un error']})

@login_required(login_url='/cuenta/login/')
def evaluarProfesor(request):
	preguntas = Pregunta.objects.all()
	user = request.user
	if (Alumno.objects.filter(username= user).count()) > 0:		#Verifica si es un alumno
		sitEscId = request.POST['profesorUDAId']
		situacionEscolar = SituacionEscolar.objects.filter(usuario=user, pk=sitEscId)
		return render(request, 'evaluarProfesor.html', {'preguntas': preguntas, 'situacionEscolar': situacionEscolar})
	else:
		mensaje = "Lo sentimos este módulo esta disponible solo para alumnos"
		return render(request, 'evaluarProfesor.html', {'mensaje': mensaje})
	return render(request, 'evaluarProfesor.html', {'mensaje': ["Se presento un error"]})

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

@login_required(login_url='/cuenta/login/')
def guardarEvaluacion(request):
	materiaEvaluada = SituacionEscolar.objects.get(pk=request.POST['materiaInscritaId'])
	materiaEvaluada.evaluacionProfesor = True
	materiaEvaluada.save()
	respuestas = [ r for r in request.POST.values() ]
	user = request.user
	UA = UnidadAprendizaje.objects.get(pk=request.POST['UA'])
	profesorUDA = Profesor.objects.get(pk=request.POST['profesorUDA'])
	bandera = 1
	r1=respuestas[4]
	r2=respuestas[5]
	r3=respuestas[6]
	r4=respuestas[7]
	r5=respuestas[8]
	r6=respuestas[9]
	r7=respuestas[10]
	r8=respuestas[11]
	r9=respuestas[12]
	r10=respuestas[13]
	r11=respuestas[14]
	r12=respuestas[15]
	cuestionario = Cuestionario.objects.create_cuestionario(user, UA, profesorUDA, bandera, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12)
	cuestionario.save()
	situacionEscolar = SituacionEscolar.objects.filter(usuario=user, evaluacionProfesor=False)
	return render(request, 'listadoMaterias.html', {'situacionEscolar': situacionEscolar})

@login_required(login_url='/cuenta/login/')
def resultadoEvaluacionesInicio(request):
	user = request.user
	if (Profesor.objects.filter(username= user).count()) > 0:		#Verifica si es un profesor
		profesorId = Profesor.objects.get(username=user)
		materias = Cuestionario.objects.filter(profesorUDA=profesorId).distinct('UA')
		return render(request, 'resultadoEvaluaciones.html', {'materias': materias})
	else:
		mensaje = "Lo sentimos este módulo esta disponible solo para profesores"
		return render(request, 'resultadoEvaluaciones.html', {'mensaje': mensaje})
	return render(request, 'resultadoEvaluaciones.html', {'materias': materias})

@login_required(login_url='/cuenta/login/')
def evaluacionDetalle(request):
	user = request.user
	if (Profesor.objects.filter(username= user).count()) > 0:		#Verifica si es un profesor
		profesorId = Profesor.objects.get(username=user)
		cuestionarios = Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'])
		preguntas = Pregunta.objects.all()
		valoracion = ["Totalmente en desacuerdo","En desacuerdo","Más o menos de acuerdo","De acuerdo","Totalmente de acuerdo"]
		respuestas = []
		#Grafica respuesta uno
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r1=1).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r1=2).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r1=3).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r1=4).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r1=5).count())
		plt.pie(respuestas, labels=valoracion, autopct="%0.1f %%")
		plt.savefig('evaluaciones/static/img/grafica1.png')
		plt.close()
		respuestas = []
		#Grafica respuesta dos
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r2=1).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r2=2).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r2=3).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r2=4).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r2=5).count())
		plt.pie(respuestas, labels=valoracion, autopct="%0.1f %%")
		plt.savefig('evaluaciones/static/img/grafica2.png')
		plt.close()
		respuestas = []
		#Grafica respuesta tres
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r3=1).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r3=2).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r3=3).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r3=4).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r3=5).count())
		plt.pie(respuestas, labels=valoracion, autopct="%0.1f %%")
		plt.savefig('evaluaciones/static/img/grafica3.png')
		plt.close()
		respuestas = []
		#Grafica respuesta cuatro
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r4=1).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r4=2).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r4=3).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r4=4).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r4=5).count())
		plt.pie(respuestas, labels=valoracion, autopct="%0.1f %%")
		plt.savefig('evaluaciones/static/img/grafica4.png')
		plt.close()
		respuestas = []
		#Grafica respuesta cinco
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r5=1).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r5=2).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r5=3).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r5=4).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r5=5).count())
		plt.pie(respuestas, labels=valoracion, autopct="%0.1f %%")
		plt.savefig('evaluaciones/static/img/grafica5.png')
		plt.close()
		respuestas = []
		#Grafica respuesta seis
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r6=1).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r6=2).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r6=3).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r6=4).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r6=5).count())
		plt.pie(respuestas, labels=valoracion, autopct="%0.1f %%")
		plt.savefig('evaluaciones/static/img/grafica6.png')
		plt.close()
		respuestas = []
		#Grafica respuesta siete
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r7=1).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r7=2).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r7=3).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r7=4).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r7=5).count())
		plt.pie(respuestas, labels=valoracion, autopct="%0.1f %%")
		plt.savefig('evaluaciones/static/img/grafica7.png')
		plt.close()
		respuestas = []
		#Grafica respuesta ocho
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r8=1).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r8=2).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r8=3).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r8=4).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r8=5).count())
		plt.pie(respuestas, labels=valoracion, autopct="%0.1f %%")
		plt.savefig('evaluaciones/static/img/grafica8.png')
		plt.close()
		respuestas = []
		#Grafica respuesta nueve
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r9=1).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r9=2).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r9=3).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r9=4).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r9=5).count())
		plt.pie(respuestas, labels=valoracion, autopct="%0.1f %%")
		plt.savefig('evaluaciones/static/img/grafica9.png')
		plt.close()
		respuestas = []
		#Grafica respuesta diez
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r10=1).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r10=2).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r10=3).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r10=4).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r10=5).count())
		plt.pie(respuestas, labels=valoracion, autopct="%0.1f %%")
		plt.savefig('evaluaciones/static/img/grafica10.png')
		plt.close()
		respuestas = []
		#Grafica respuesta once
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r11=1).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r11=2).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r11=3).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r11=4).count())
		respuestas.append(Cuestionario.objects.filter(profesorUDA=profesorId, UA=request.POST['UAId'], r11=5).count())
		plt.pie(respuestas, labels=valoracion, autopct="%0.1f %%")
		plt.savefig('evaluaciones/static/img/grafica11.png')
		plt.close()
		respuestas = []
		return render(request, 'detalleEvaluacion.html', {'cuestionarios': cuestionarios, 'preguntas': preguntas})
	else:
		mensaje = "Lo sentimos este módulo esta disponible solo para profesores"
		return render(request, 'detalleEvaluacion.html', {'mensaje': mensaje})
	return render(request, 'detalleEvaluacion.html', {'cuestionarios': cuestionarios})