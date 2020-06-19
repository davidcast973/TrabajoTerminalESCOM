from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
import nltk
nltk.download('punkt')
nltk.download('wordnet')
#Descaga Open Multilingual WordNet
nltk.download('omw')
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk import word_tokenize
import spacy
from string import punctuation
import re
import os
from .models import *
from usuario.models import Alumno, Profesor
from ofertaEducativa.models import SituacionEscolar, UnidadAprendizaje
from evaluaciones.models import Cuestionario
#Librerias para graficar
import matplotlib.pyplot as plt
import numpy as np

import os.path as path
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
		tokensNormalizados = normalizarTexto(cuestionarios)
		noTokens = len(tokensNormalizados)
		#Analisis con diccionario SEL
		if not (path.exists("evaluaciones/static/img/graficaSEL.png")):
			etiquetasXEmocion = [0,0,0,0,0,0]
			noEtiquetasSEL = 0
			sentimientos = ["Alegria","Enojo","Miedo","Repulsion","Tristesa","Sorpresa"]
			etiquetasSEL = etiquetarTokens(tokensNormalizados,1)
			for etiqueta in etiquetasSEL:
				if etiqueta != "None":
					noEtiquetasSEL += 1
				if etiqueta[0] == "Alegría\n":
					etiquetasXEmocion[0] += 1
				if etiqueta[0] == "Enojo\n":
					etiquetasXEmocion[1] += 1
				if etiqueta[0] == "Miedo\n":
					etiquetasXEmocion[2] += 1
				if etiqueta[0] == "Repulsión\n":
					etiquetasXEmocion[3] += 1
				if etiqueta[0] == "Tristeza\n":
					etiquetasXEmocion[4] += 1
				if etiqueta[0] == "Sorpresa\n":
					etiquetasXEmocion[5] += 1
			plt.pie(etiquetasXEmocion, labels=sentimientos, autopct="%0.1f %%")
			plt.savefig('evaluaciones/static/img/graficaSEL.png')
			plt.close()

		#Analisis con diccionario FullStrenght
		if not (path.exists("evaluaciones/static/img/graficaFULL.png")):
			noEtiquetasFull = 0
			etiquetasFullXPolaridad = [0,0]
			etiquetasFull = etiquetarTokens(tokensNormalizados,2)
			for etiqueta in etiquetasFull:
				if etiqueta != "None":
					noEtiquetasFull += 1
				if etiqueta == "pos\n":
					etiquetasFullXPolaridad[0] += 1
				if etiqueta == "neg\n":
					etiquetasFullXPolaridad[1] += 1
			x = np.array(["Positiva"])
			y = np.array([etiquetasFullXPolaridad[0]])
			x2 = np.array(["Negativa"])
			y2 = np.array([etiquetasFullXPolaridad[1]])
			plt.bar(x,y,align="center")
			plt.bar(x2,y2,color="r", align="center")
			plt.legend("Positivas", "Negativas")
			plt.savefig('evaluaciones/static/img/graficaFULL.png')
			plt.close()

		#Analisis con diccionario Medium Strenght
		if not (path.exists("evaluaciones/static/img/graficaMED.png")):
			noEtiquetasMed = 0
			polaridad = ["Positiva", "Negativa"]
			etiquetasMedXPolaridad = [0,0]
			etiquetasMed = etiquetarTokens(tokensNormalizados,3)
			for etiqueta in etiquetasMed:
				if etiqueta != "None":
					noEtiquetasMed += 1
				if etiqueta == "pos\n":
					etiquetasMedXPolaridad[0] += 1
				if etiqueta == "neg\n":
					etiquetasMedXPolaridad[1] += 1
			plt.pie(etiquetasMedXPolaridad, labels=polaridad, autopct="%0.1f %%")
			plt.savefig('evaluaciones/static/img/graficaMED.png')
			plt.close()

		preguntas = Pregunta.objects.all()
		valoracion = ["Totalmente en desacuerdo","En desacuerdo","Más o menos de acuerdo","De acuerdo","Totalmente de acuerdo"]
		respuestas = []
		# Las siguientes condiciones se realiza para no estar generando graficas en cada consulta y mejorar el tiempo de carga
		# suponiendo que se fije un periodo de tiempo para evaluar a los maestros, una vez terminado ese periodo, el sistema generará
		# las gráficas solo una vez.
		if not (path.exists("evaluaciones/static/img/grafica1.png")):
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
		if not (path.exists("evaluaciones/static/img/grafica2.png")):
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
		if not (path.exists("evaluaciones/static/img/grafica3.png")):
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
		if not (path.exists("evaluaciones/static/img/grafica4.png")):
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
		if not (path.exists("evaluaciones/static/img/grafica5.png")):
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
		if not (path.exists("evaluaciones/static/img/grafica6.png")):
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
		if not (path.exists("evaluaciones/static/img/grafica7.png")):
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
		if not (path.exists("evaluaciones/static/img/grafica8.png")):
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
		if not (path.exists("evaluaciones/static/img/grafica9.png")):
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
		if not (path.exists("evaluaciones/static/img/grafica10.png")):
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
		if not (path.exists("evaluaciones/static/img/grafica11.png")):
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
		return render(request, 'detalleEvaluacion.html', {'cuestionarios': cuestionarios, 'preguntas': preguntas, 'tokensNormalizados':tokensNormalizados, 'noTokens': noTokens})
	else:
		mensaje = "Lo sentimos este módulo esta disponible solo para profesores"
		return render(request, 'detalleEvaluacion.html', {'mensaje': mensaje})
	return render(request, 'detalleEvaluacion.html', {'cuestionarios': cuestionarios})

#Esta función procesa el texto y lo normaliza para su posterior uso
def normalizarTexto(cuestionarios):
	#lista de stopwors a utilizar
	spanish_stopwords  = stopwords.words('spanish')
	#Para remover la puntuacion
	non_words = list(punctuation)
	#Agregamos puntuacion usada en el idioma español
	non_words.extend(['¿','¡'])
	non_words.extend(map(str,range(10)))
	#Guardamos las opiniones
	opiniones = ""
	
	for cuestionario in cuestionarios:
		#Convertir a minusculas
		opiniones += str(cuestionario.r12).lower()
		opiniones += " "
	#Remover la puntuación y caracteres especiales
	text = ''.join([c for c in opiniones if c not in non_words])
	#Generar tokens
	tokens = word_tokenize(text)
	#Removemos stopwords
	tokensFiltrados = [token for token in tokens if token not in spanish_stopwords]
	#Corregimos palabras sintactica y sematicamente
	tokensCorregidos = removerCaracteresRepetidos(tokensFiltrados)
	cadenaTokens = " ".join(tokensCorregidos)
	#Lematizamos los tokens
	tokensLematizados = lematizar(cadenaTokens)

	return tokensLematizados

#Esta función corrige palabras sintactica y semanticamente considerando su significado
def removerCaracteresRepetidos(tokens):
	patronRepetido = re.compile(r'(\w*)(\w)\2(\w*)')
	sustitucion = r'\1\2\3'
	
	def reemplazar(palabraAntigua):
		if wordnet.synsets(palabraAntigua,lang="spa"):
			return palabraAntigua
		nuevaPalabra = patronRepetido.sub(sustitucion, palabraAntigua)
		return reemplazar(nuevaPalabra) if nuevaPalabra != palabraAntigua else nuevaPalabra
	
	tokensCorregidos = [reemplazar(palabra) for palabra in tokens]
	return tokensCorregidos

#Esta función lematiza los tokens
def lematizar(texto):
	nlp = spacy.load('es') 
	doc = nlp(texto)
	return [palabra.lemma_ for palabra in doc]

def etiquetarTokens(tokens, dic):
	diccionarioSEL = {}
	diccionarioFull = {}
	diccionarioMedium = {}

	def etiquetarSEL(token):
		#Se abre el diccionario SEL de sentimeintos y se guarda
		with open('evaluaciones/static/dictionaries/SEL.txt','r') as diccionarioSentimientos:
			for palabra in diccionarioSentimientos:
				if (diccionarioSEL.get(palabra.split("	")[0]) != None):
					if (diccionarioSEL.get(palabra.split("	")[0])[1] < float(palabra.split("	")[1])):
						diccionarioSEL.update({palabra.split("	")[0] : [palabra.split("	")[2], float(palabra.split("	")[1])]})
				else:
					diccionarioSEL.update({palabra.split("	")[0] : [palabra.split("	")[2], float(palabra.split("	")[1])]})

		if (diccionarioSEL.get(token) != None):
			return diccionarioSEL.get(token)
		else:
			return "None"

	def etiquetarFull(token):
		#Se abre el diccionario fullStrengthLexicon de sentimeintos y se guarda
		with open('evaluaciones/static/dictionaries/fullStrengthLexicon.txt','r') as diccionarioFullS:
			for palabra in diccionarioFullS:
				diccionarioFull.update({palabra.split("	")[0] : palabra.split("	")[2]})

		if (diccionarioFull.get(token) != None):
			return diccionarioFull.get(token)
		else:
			return "None"

	def etiquetarMedium(token):
		#Se abre el diccionario mediumStrengthLexicon de sentimeintos y se guarda
		with open('evaluaciones/static/dictionaries/mediumStrengthLexicon.txt','r') as diccionarioM:
			for palabra in diccionarioM:
				diccionarioMedium.update({palabra.split("	")[0] : palabra.split("	")[2]})

		if (diccionarioMedium.get(token) != None):
			return diccionarioMedium.get(token)
		else:
			return "None"

	if dic == 1:
		etiquetasTokens = [etiquetarSEL(token) for token in tokens]
	elif dic == 2:
		etiquetasTokens = [etiquetarFull(token) for token in tokens]
	else:
		etiquetasTokens = [etiquetarMedium(token) for token in tokens]
	return etiquetasTokens