from django.shortcuts import render, get_object_or_404
from django import forms
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views import View
from .models import *
from django.contrib.auth.decorators import login_required
from inscripcionTesis.models import Tesis as T
from usuario.models import Alumno as A
import gensim # Word2Vec
from sklearn.metrics.pairwise import cosine_similarity as CS # Similitud coseno
from nltk import word_tokenize
from string import punctuation
#DEVELOPfrom datetime import datetime # Castear a fecha AAAA-MM-DD

#DEVELOPmodel = gensim.models.KeyedVectors.load_word2vec_format('sbw_vectors.bin', binary=True) # Word2Vec

non_words = list(punctuation)
non_words.extend(['¿','¡','\n','\r'])
non_words.extend(map(str,range(10)))

todasLasTesis= T.objects.order_by('-numeroTesis')

def vertesis(request):
	allTesis= T.objects.order_by('-numeroTesis')
	numAllTesis= len(allTesis)
	cantPag= list(range(1,(numAllTesis//18)+1))
	modPag= list(range(1,(numAllTesis%18)+1))

	bandera = 1
	if (Alumno.objects.filter(username= request.user).count()) > 0:
		bandera = 1
	elif (Profesor.objects.filter(username= request.user).count()) > 0:
		bandera = 2
	elif (PersonalAdministrativo.objects.filter(username= request.user).count()) > 0:
		bandera = 3

	return render(request, 'tesis/vertesis.html', {'tipoUsuario': bandera, 'allTesis': allTesis, 'numAllTesis':numAllTesis, 'cantPag':cantPag, 'modPag':modPag,})

@login_required(login_url='/cuenta/login/')
def inscripcionTesisInicio(request):
	alumnoActual= A.objects.get(username= request.user)
	tesisInscritas= T.objects.filter(alumno= alumnoActual.nombre, alumnoAps= alumnoActual.apellido)

	bandera = 1
	if (Alumno.objects.filter(username= request.user).count()) > 0:
		bandera = 1
	elif (Profesor.objects.filter(username= request.user).count()) > 0:
		bandera = 2
	elif (PersonalAdministrativo.objects.filter(username= request.user).count()) > 0:
		bandera = 3
	return render(request, "tesis/inscripcionTesisInicio.html",{
		'tipoUsuario': bandera,
		'numPaso': 1,
		'tesisInscritas':tesisInscritas,
		})

# Regresa sugerencias[n][[CS()],[numeroTesis],[nombre director]]
def obtenerProfesoresSugeridos(texto):
	limpiarTexto= list()
	for c in texto:
	   if c not in non_words:
	      limpiarTexto.append(c)
	   elif c == '\n':
	      limpiarTexto.append(' ')

	caracteres= ''.join(limpiarTexto)
	tokens = word_tokenize(caracteres)
	#DEVELOPif not tokens:
	   #DEVELOPw2v= ','.join([str(0) for x in range(300)])
	#DEVELOPelse:
	   #DEVELOPw2v= [0 for x in range(300)]
	   #DEVELOPfor w in tokens:
	      #DEVELOP#print(len(tokens),tokens)
	      #DEVELOP#print(len(w2v),w2v)
	      #DEVELOPif w in model:
	         #DEVELOPw2v+= model[w]

	w2v= [-0.096409306, -0.021046208, -0.22753316, 0.098436356, -0.0928205, 0.113128826, -0.60705185, 0.15077896, 1.0891678, 0.27758944, 0.08118385, -0.52199644, 0.2142125, 0.4737003, 0.7450613, 0.35756505, -0.3630991, 0.5287377, -0.6868741, 0.16151257, -0.14739354, -0.4477498, 0.4508404, 0.5513687, 0.23969051, -0.27262893, -0.43244356, 0.19658107, 0.5283035, 1.8136064, 0.52293646, 0.20957188, 0.15975109, -0.47241706, 0.4224497, -0.67884684, -0.08411095, 0.40812775, -0.5161344, 0.3998546, 0.5021685, 1.0931462, -0.21282157, -0.66638666, -0.37983236, -0.36729708, -0.07958993, -0.48455882, -0.6189636, 0.52724123, 0.14896446, 0.33031532, 0.050798982, 1.0736632, -0.01710312, 0.1909203, -0.35827106, -0.9352342, 0.59927565, 0.49823815, -0.6235958, 0.11259886, -0.8139814, 0.20294999, -0.17132846, 0.22071904, -0.8198136, 0.5863507, -1.0979121, 0.7679998, 0.22642621, 0.20709006, 0.34719154, 0.42714596, 0.29465342, 0.7687768, -0.3764652, 0.58030266, -0.88539827, -0.2738966, 0.17569628, 0.5514991, -0.039156027, 0.043003768, -0.0990822, -0.64594024, -0.15191922, 0.33681402, 0.516894, 0.3166411, -0.1541146, -0.38006973, 0.6749842, 0.7162946, -0.6242641, 0.3341194, 0.14012179, 0.8534963, -0.14643677, 0.87748945, -0.4613105, -0.82035327, -0.26547852, 0.65358865, 1.0461828, -0.0013594776, -0.40785944, -0.051784977, -0.09004267, -0.19674361, 0.19589123, -0.010658674, 0.3999068, -0.5093777, -0.30810574, 0.11782781, -0.121625066, 0.35097888, -0.28758144, -0.20866935, -0.8853166, 0.62087977, -1.3786982, -0.73089576, 0.027938738, 0.17646894, -0.0251306, 0.025014453, 0.69856846, -0.13202733, 0.079900734, 0.37248108, -0.9082765, -0.240356, -0.2627582, 0.4759973, -0.2938515, -0.09216596, 0.5688052, 0.07393474, -0.55338, -0.41678149, 0.06785919, 0.42643282, -0.4822983, -0.14455485, 0.32330683, -0.44836196, 1.0146493, -0.48013324, 0.16655983, -0.35773462, -0.020053023, -0.1896812, -0.029243633, -0.15511337, 0.6046752, 0.2957911, -0.9817063, -0.7346073, -0.18638012, -0.6211578, 0.34182683, -0.31065026, -0.010593016, 0.24844225, -0.9164189, 0.49355552, 0.7783028, -0.52990764, 0.05142221, -0.9150039, 0.3847145, -0.30614483, -0.041397065, -0.3377262, -0.41570884, -0.47868425, -0.3241465, 0.1557335, 1.035065, 0.501608, 0.34758818, 0.09415336, -0.44754583, 0.5127064, 0.32977206, -1.2377539, -0.6420507, -0.010460526, -0.5326121, 0.13478467, 0.63224304, -0.26395178, 0.08096886, 0.83804464, 0.28680986, 0.10070562, 0.5324281, 0.17558128, -1.2271272, 0.26869816, 0.09867278, 0.40347445, 0.48944837, -0.06124668, -0.13452289, -0.5287368, -0.13503948, 0.23638932, -0.43084797, -0.53517187, -0.14067009, -0.45290545, 0.065126576, 0.51279986, -1.0133327, 0.26427895, -0.31422508, 0.13375519, -0.15753588, 0.15280114, 0.018989466, 0.025513232, -1.2266507, 0.23805138, 0.6849649, -0.05795823, -0.29081622, -0.21631493, 0.61381066, -0.13193007, 0.15280621, 0.3996118, -0.8903821, 0.3456732, -0.22276625, -0.8854252, -0.4464345, 0.35212713, 1.4041559, -0.30559027, 0.24956706, -0.7061893, -0.42629474, 0.078896806, -0.6600071, -0.5751982, -0.44767407, -0.47678703, 0.73951674, 0.3192112, 0.83220816, -0.17027286, -0.502949, 0.34461233, 0.47630793, -0.080276966, -0.2187569, -0.70663476, 0.7466506, 1.2376378, 0.18759355, 0.11424187, -0.6322607, -0.5644554, 0.09720684, 0.87655765, 0.114420414, 0.92271876, 0.09655694, -0.02437076, 0.5102837, 0.12042217, -0.009238854, -0.20222318, -0.21517947, -0.18241616, 0.3106741, -1.0400568, -1.3095424, 0.16099681, -0.73245895, -0.035369493, 1.3121213, -0.793995, 0.5429869, 0.59093463, 0.12937048, -0.4382204, -0.1265043, -0.17177156, -0.30547705, 0.1509597, -0.6474984, -0.27082726, 0.13895161, -0.49737573, -0.7086221, 0.66729176]

	sugerencias= []
	for t in todasLasTesis:
		if t.abstrac != '':
			sugerencias.append([CS([w2v],[[float(x) for x in t.valorW2V.split(',')]])[0][0],t.numeroTesis,'Dr. '+t.director1+' '+t.director1Aps])

	sugerencias.sort(reverse=True)
	return sugerencias

def mostrarNProfesores(sugerencias, ignorarProfesor= [], nProfesores=10):
	mostrar10=[]
	distintos=[]
	cont= 0
	for s in sugerencias:
		if cont == nProfesores:
			break
		if (s[2] != '') and ((s[2] not in ignorarProfesor) and (s[2] not in distintos)):
			mostrar10.append(s)
			distintos.append(s[2])
			cont+= 1
	return mostrar10

def tesisSimilares(request):
	tituloPropuesto= request.POST['tituloPropuesto']

	sugerencias= obtenerProfesoresSugeridos(tituloPropuesto)

	mostrar10= mostrarNProfesores(sugerencias)

	bandera = 1
	if (Alumno.objects.filter(username= request.user).count()) > 0:
		bandera = 1
	elif (Profesor.objects.filter(username= request.user).count()) > 0:
		bandera = 2
	elif (PersonalAdministrativo.objects.filter(username= request.user).count()) > 0:
		bandera = 3
	return render(request, "tesis/inscripcionTesisInicio.html",
		{
			'tipoUsuario': bandera,
			'tituloPropuesto':tituloPropuesto,
			'top10':mostrar10,
			'sugerencias': sugerencias,
			'numPaso':2,
		})

def seleccionarDirector1(request):
	tituloPropuesto= request.POST['tituloPropuesto2']
	numTesisSeleccionada= int(request.POST['director1Seleccionado'])

	if numTesisSeleccionada != 0:
		buscar= T.objects.get(numeroTesis= numTesisSeleccionada)
		nombreDirector1= 'Dr. '+buscar.director1+' '+buscar.director1Aps
	else:
		nombreDirector1= 'Dr. '+'Nadie Desconocido Misterio'
		print('No se seleccionó un primer director')

	sugerencias= obtenerProfesoresSugeridos(tituloPropuesto)
	filtrarProfesores= [nombreDirector1]
	mostrar10= mostrarNProfesores(sugerencias,filtrarProfesores)

	bandera = 1
	if (Alumno.objects.filter(username= request.user).count()) > 0:
		bandera = 1
	elif (Profesor.objects.filter(username= request.user).count()) > 0:
		bandera = 2
	elif (PersonalAdministrativo.objects.filter(username= request.user).count()) > 0:
		bandera = 3
	return render(request, "tesis/inscripcionTesisInicio.html",
		{
			'tipoUsuario': bandera,
			'tituloPropuesto':tituloPropuesto,
			'top10':mostrar10,
			'sugerencias': sugerencias,
			'numTesisDirector1':numTesisSeleccionada ,
			'nombreDirector1':nombreDirector1,
			'numPaso': 3,
		})

def seleccionarDirector2(request):
	tituloPropuesto= request.POST['tituloPropuesto3']
	numTesisDirector1= int(request.POST['numTesDir1'])
	director1= T.objects.get(numeroTesis= numTesisDirector1)
	nombreDirector1= 'Dr. '+director1.director1+' '+director1.director1Aps
	numTesisSeleccionada= int(request.POST['director2Seleccionado'])

	if numTesisSeleccionada != 0:
		buscar= T.objects.get(numeroTesis= numTesisSeleccionada)
		nombreDirector2= 'Dr. '+buscar.director1+' '+buscar.director1Aps
	else:
		nombreDirector2= 'Dr. '+'Nadie Desconocido Misterio'
		print('No se seleccionó un segundo director')

	sugerencias= obtenerProfesoresSugeridos(tituloPropuesto)
	filtrarProfesores= [nombreDirector1,nombreDirector2]
	mostrar10= mostrarNProfesores(sugerencias,filtrarProfesores)
	print(filtrarProfesores)

	bandera = 1
	if (Alumno.objects.filter(username= request.user).count()) > 0:
		bandera = 1
	elif (Profesor.objects.filter(username= request.user).count()) > 0:
		bandera = 2
	elif (PersonalAdministrativo.objects.filter(username= request.user).count()) > 0:
		bandera = 3
	return render(request, "tesis/inscripcionTesisInicio.html",
		{
			'tipoUsuario': bandera,
			'tituloPropuesto':tituloPropuesto,
			'top10':mostrar10,
			'sugerencias': sugerencias,
			'nombreDirector1':nombreDirector1,
			'numTesisDirector1':numTesisDirector1 ,
			'nombreDirector2':nombreDirector2,
			'numTesisDirector2':numTesisSeleccionada,
			'numPaso': 4,
		})

def omitirProfesor(request):
	bandera = 1
	if (Alumno.objects.filter(username= request.user).count()) > 0:
		bandera = 1
	elif (Profesor.objects.filter(username= request.user).count()) > 0:
		bandera = 2
	elif (PersonalAdministrativo.objects.filter(username= request.user).count()) > 0:
		bandera = 3
	return render(request, "tesis/inscripcionTesisInicio.html",  {'tipoUsuario': bandera, 'numPaso': 4})

def seleccionarCT1(request):
	tituloPropuesto= request.POST['tituloPropuesto4']
	numTesisDirector1= int(request.POST['numTesDir1'])
	director1= T.objects.get(numeroTesis= numTesisDirector1)
	nombreDirector1= 'Dr. '+director1.director1+' '+director1.director1Aps
	numTesisDirector2= int(request.POST['numTesDir2'])
	director2= T.objects.get(numeroTesis= numTesisDirector2)
	nombreDirector2= 'Dr. '+director2.director1+' '+director2.director1Aps
	numTesisSeleccionada= int(request.POST['comiteSeleccionado1'])

	if numTesisSeleccionada != 0:
		buscar= T.objects.get(numeroTesis= numTesisSeleccionada)
		nombreMiembro1= 'Dr. '+buscar.director1+' '+buscar.director1Aps
	else:
		nombreMiembro1= 'Dr. '+'Nadie Desconocido Misterio'
		print('No se seleccionó un segundo director')

	sugerencias= obtenerProfesoresSugeridos(tituloPropuesto)
	filtrarProfesores= [nombreDirector1,nombreDirector2,nombreMiembro1]
	mostrar10= mostrarNProfesores(sugerencias,filtrarProfesores)
	print(str(len(sugerencias)),filtrarProfesores)

	bandera = 1
	if (Alumno.objects.filter(username= request.user).count()) > 0:
		bandera = 1
	elif (Profesor.objects.filter(username= request.user).count()) > 0:
		bandera = 2
	elif (PersonalAdministrativo.objects.filter(username= request.user).count()) > 0:
		bandera = 3
	return render(request, "tesis/inscripcionTesisInicio.html",
		{
			'tipoUsuario': bandera,
			'tituloPropuesto':tituloPropuesto,
			'top10':mostrar10,
			'sugerencias': sugerencias,
			'nombreDirector1':nombreDirector1,
			'numTesisDirector1':numTesisDirector1 ,
			'nombreDirector2':nombreDirector2,
			'numTesisDirector2':numTesisDirector2,
			'nombreMiembro1':nombreMiembro1,
			'numTesisCT1':numTesisSeleccionada,
			'numPaso': 5,
		})

def seleccionarCT2(request):
	tituloPropuesto= request.POST['tituloPropuesto5']
	numTesisDirector1= int(request.POST['numTesDir1'])
	director1= T.objects.get(numeroTesis= numTesisDirector1)
	nombreDirector1= 'Dr. '+director1.director1+' '+director1.director1Aps
	numTesisDirector2= int(request.POST['numTesDir2'])
	director2= T.objects.get(numeroTesis= numTesisDirector2)
	nombreDirector2= 'Dr. '+director2.director1+' '+director2.director1Aps
	numTesisComite1= int(request.POST['numTesCT1'])
	miembroCT1= T.objects.get(numeroTesis= numTesisComite1)
	nombreMiembroCT1= 'Dr. '+miembroCT1.director1+' '+miembroCT1.director1Aps
	numTesisSeleccionada= int(request.POST['comiteSeleccionado2'])

	if numTesisSeleccionada != 0:
		buscar= T.objects.get(numeroTesis= numTesisSeleccionada)
		nombreMiembroCT2= 'Dr. '+buscar.director1+' '+buscar.director1Aps
	else:
		nombreMiembroCT2= 'Dr. '+'Nadie Desconocido Misterio'
		print('No se seleccionó un segundo director')

	sugerencias= obtenerProfesoresSugeridos(tituloPropuesto)
	filtrarProfesores= [
		nombreDirector1,
		nombreDirector2,
		nombreMiembroCT1,
		nombreMiembroCT2,
		]
	mostrar10= mostrarNProfesores(sugerencias,filtrarProfesores)

	bandera = 1
	if (Alumno.objects.filter(username= request.user).count()) > 0:
		bandera = 1
	elif (Profesor.objects.filter(username= request.user).count()) > 0:
		bandera = 2
	elif (PersonalAdministrativo.objects.filter(username= request.user).count()) > 0:
		bandera = 3
	return render(request, "tesis/inscripcionTesisInicio.html", {
			'tipoUsuario': bandera,
			'tituloPropuesto':tituloPropuesto,
			'top10':mostrar10,
			'sugerencias': sugerencias,
			'nombreDirector1':nombreDirector1,
			'numTesisDirector1':numTesisDirector1 ,
			'nombreDirector2':nombreDirector2,
			'numTesisDirector2':numTesisDirector2,
			'nombreMiembro1':nombreMiembroCT1,
			'numTesisCT1':numTesisComite1,
			'nombreMiembro2':nombreMiembroCT2,
			'numTesisCT2':numTesisSeleccionada,
			'numPaso': 6,
			})

def seleccionarCT3(request):
	tituloPropuesto= request.POST['tituloPropuesto6']
	numTesisDirector1= int(request.POST['numTesDir1'])
	director1= T.objects.get(numeroTesis= numTesisDirector1)
	nombreDirector1= 'Dr. '+director1.director1+' '+director1.director1Aps
	numTesisDirector2= int(request.POST['numTesDir2'])
	director2= T.objects.get(numeroTesis= numTesisDirector2)
	nombreDirector2= 'Dr. '+director2.director1+' '+director2.director1Aps
	numTesisComite1= int(request.POST['numTesCT1'])
	miembroCT1= T.objects.get(numeroTesis= numTesisComite1)
	nombreMiembroCT1= 'Dr. '+miembroCT1.director1+' '+miembroCT1.director1Aps
	numTesisComite2= int(request.POST['numTesCT2'])
	miembroCT2= T.objects.get(numeroTesis= numTesisComite2)
	nombreMiembroCT2= 'Dr. '+miembroCT2.director1+' '+miembroCT2.director1Aps
	numTesisSeleccionada= int(request.POST['comiteSeleccionado3'])

	if numTesisSeleccionada != 0:
		buscar= T.objects.get(numeroTesis= numTesisSeleccionada)
		nombreMiembroCT3= 'Dr. '+buscar.director1+' '+buscar.director1Aps
	else:
		nombreMiembroCT3= 'Dr. '+'Nadie Desconocido Misterio'
		print('No se seleccionó un segundo director')

	sugerencias= obtenerProfesoresSugeridos(tituloPropuesto)
	filtrarProfesores= [
		nombreDirector1,
		nombreDirector2,
		nombreMiembroCT1,
		nombreMiembroCT2,
		nombreMiembroCT3,
		]
	mostrar10= mostrarNProfesores(sugerencias,filtrarProfesores)

	bandera = 1
	if (Alumno.objects.filter(username= request.user).count()) > 0:
		bandera = 1
	elif (Profesor.objects.filter(username= request.user).count()) > 0:
		bandera = 2
	elif (PersonalAdministrativo.objects.filter(username= request.user).count()) > 0:
		bandera = 3
	return render(request, "tesis/inscripcionTesisInicio.html",
		{
			'tipoUsuario': bandera,
			'tituloPropuesto':tituloPropuesto,
			'top10':mostrar10,
			'sugerencias': sugerencias,
			'nombreDirector1':nombreDirector1,
			'numTesisDirector1':numTesisDirector1 ,
			'nombreDirector2':nombreDirector2,
			'numTesisDirector2':numTesisDirector2,
			'nombreMiembro1':nombreMiembroCT1,
			'numTesisCT1':numTesisComite1,
			'nombreMiembro2':nombreMiembroCT2,
			'numTesisCT2':numTesisComite2,
			'nombreMiembro3':nombreMiembroCT3,
			'numTesisCT3':numTesisSeleccionada,
			'numPaso': 7,
		})

def seleccionarCT4(request):
	tituloPropuesto= request.POST['tituloPropuesto7']
	numTesisDirector1= int(request.POST['numTesDir1'])
	director1= T.objects.get(numeroTesis= numTesisDirector1)
	nombreDirector1= 'Dr. '+director1.director1+' '+director1.director1Aps
	numTesisDirector2= int(request.POST['numTesDir2'])
	director2= T.objects.get(numeroTesis= numTesisDirector2)
	nombreDirector2= 'Dr. '+director2.director1+' '+director2.director1Aps
	numTesisComite1= int(request.POST['numTesCT1'])
	miembroCT1= T.objects.get(numeroTesis= numTesisComite1)
	nombreMiembroCT1= 'Dr. '+miembroCT1.director1+' '+miembroCT1.director1Aps
	numTesisComite2= int(request.POST['numTesCT2'])
	miembroCT2= T.objects.get(numeroTesis= numTesisComite2)
	nombreMiembroCT2= 'Dr. '+miembroCT2.director1+' '+miembroCT2.director1Aps
	numTesisComite3= int(request.POST['numTesCT3'])
	miembroCT3= T.objects.get(numeroTesis= numTesisComite3)
	nombreMiembroCT3= 'Dr. '+miembroCT3.director1+' '+miembroCT3.director1Aps
	numTesisSeleccionada= int(request.POST['comiteSeleccionado4'])

	if numTesisSeleccionada != 0:
		buscar= T.objects.get(numeroTesis= numTesisSeleccionada)
		nombreMiembroCT4= 'Dr. '+buscar.director1+' '+buscar.director1Aps
	else:
		nombreMiembroCT4= 'Dr. '+'Nadie Desconocido Misterio'
		print('No se seleccionó un segundo director')

	sugerencias= obtenerProfesoresSugeridos(tituloPropuesto)
	filtrarProfesores= [
		nombreDirector1,
		nombreDirector2,
		nombreMiembroCT1,
		nombreMiembroCT2,
		nombreMiembroCT3,
		nombreMiembroCT4,
		]
	mostrar10= mostrarNProfesores(sugerencias,filtrarProfesores)

	bandera = 1
	if (Alumno.objects.filter(username= request.user).count()) > 0:
		bandera = 1
	elif (Profesor.objects.filter(username= request.user).count()) > 0:
		bandera = 2
	elif (PersonalAdministrativo.objects.filter(username= request.user).count()) > 0:
		bandera = 3
	return render(request, "tesis/inscripcionTesisInicio.html",{
			'tipoUsuario': bandera,
			'tituloPropuesto':tituloPropuesto,
			'top10':mostrar10,
			'sugerencias': sugerencias,
			'nombreDirector1':nombreDirector1,
			'numTesisDirector1':numTesisDirector1 ,
			'nombreDirector2':nombreDirector2,
			'numTesisDirector2':numTesisDirector2,
			'nombreMiembro1':nombreMiembroCT1,
			'numTesisCT1':numTesisComite1,
			'nombreMiembro2':nombreMiembroCT2,
			'numTesisCT2':numTesisComite2,
			'nombreMiembro3':nombreMiembroCT3,
			'numTesisCT3':numTesisComite3,
			'nombreMiembro4':nombreMiembroCT4,
			'numTesisCT4':numTesisSeleccionada,
			'numPaso': 8,
		})

def registrarTesis(request):
	tituloPropuesto= request.POST['tituloPropuesto8']
	numTesisDirector1= int(request.POST['numTesDir1'])
	director1= T.objects.get(numeroTesis= numTesisDirector1)
	nombreDirector1= 'Dr. '+director1.director1+' '+director1.director1Aps
	numTesisDirector2= int(request.POST['numTesDir2'])
	director2= T.objects.get(numeroTesis= numTesisDirector2)
	nombreDirector2= 'Dr. '+director2.director1+' '+director2.director1Aps
	numTesisComite1= int(request.POST['numTesCT1'])
	miembroCT1= T.objects.get(numeroTesis= numTesisComite1)
	nombreMiembroCT1= 'Dr. '+miembroCT1.director1+' '+miembroCT1.director1Aps
	numTesisComite2= int(request.POST['numTesCT2'])
	miembroCT2= T.objects.get(numeroTesis= numTesisComite2)
	nombreMiembroCT2= 'Dr. '+miembroCT2.director1+' '+miembroCT2.director1Aps
	numTesisComite3= int(request.POST['numTesCT3'])
	miembroCT3= T.objects.get(numeroTesis= numTesisComite3)
	nombreMiembroCT3= 'Dr. '+miembroCT3.director1+' '+miembroCT3.director1Aps
	numTesisComite4= int(request.POST['numTesCT4'])
	miembroCT4= T.objects.get(numeroTesis= numTesisComite4)
	nombreMiembroCT4= 'Dr. '+miembroCT4.director1+' '+miembroCT4.director1Aps
	numTesisSeleccionada= int(request.POST['comiteSeleccionado5'])

	if numTesisSeleccionada != 0:
		buscar= T.objects.get(numeroTesis= numTesisSeleccionada)
		nombreMiembroCT5= 'Dr. '+buscar.director1+' '+buscar.director1Aps
	else:
		nombreMiembroCT5= 'Dr. '+'Nadie Desconocido Misterio'
		print('No se seleccionó un segundo director')

	bandera = 1
	if (Alumno.objects.filter(username= request.user).count()) > 0:
		bandera = 1
	elif (Profesor.objects.filter(username= request.user).count()) > 0:
		bandera = 2
	elif (PersonalAdministrativo.objects.filter(username= request.user).count()) > 0:
		bandera = 3
	return render(request, "tesis/inscripcionTesisInicio.html",{
			'tipoUsuario': bandera,
			'tituloPropuesto':tituloPropuesto,
			'nombreDirector1':nombreDirector1,
			'numTesisDirector1':numTesisDirector1 ,
			'nombreDirector2':nombreDirector2,
			'numTesisDirector2':numTesisDirector2,
			'nombreMiembro1':nombreMiembroCT1,
			'numTesisCT1':numTesisComite1,
			'nombreMiembro2':nombreMiembroCT2,
			'numTesisCT2':numTesisComite2,
			'nombreMiembro3':nombreMiembroCT3,
			'numTesisCT3':numTesisComite3,
			'nombreMiembro4':nombreMiembroCT4,
			'numTesisCT4':numTesisComite4,
			'nombreMiembro5':nombreMiembroCT5,
			'numTesisCT5':numTesisSeleccionada,
			'numPaso': 9,
		})

def guardarTesis(request):
	numTesisDirector1= int(request.POST['numTesDir1'])
	director1= T.objects.get(numeroTesis= numTesisDirector1)
	nombreDirector1= 'Dr. '+director1.director1+' '+director1.director1Aps
	numTesisDirector2= int(request.POST['numTesDir2'])
	director2= T.objects.get(numeroTesis= numTesisDirector2)
	nombreDirector2= 'Dr. '+director2.director1+' '+director2.director1Aps
	numTesisComite1= int(request.POST['numTesCT1'])
	miembroCT1= T.objects.get(numeroTesis= numTesisComite1)
	nombreMiembroCT1= 'Dr. '+miembroCT1.director1+' '+miembroCT1.director1Aps
	numTesisComite2= int(request.POST['numTesCT2'])
	miembroCT2= T.objects.get(numeroTesis= numTesisComite2)
	nombreMiembroCT2= 'Dr. '+miembroCT2.director1+' '+miembroCT2.director1Aps
	numTesisComite3= int(request.POST['numTesCT3'])
	miembroCT3= T.objects.get(numeroTesis= numTesisComite3)
	nombreMiembroCT3= 'Dr. '+miembroCT3.director1+' '+miembroCT3.director1Aps
	numTesisComite4= int(request.POST['numTesCT4'])
	miembroCT4= T.objects.get(numeroTesis= numTesisComite4)
	nombreMiembroCT4= 'Dr. '+miembroCT4.director1+' '+miembroCT4.director1Aps
	numTesisComite5= int(request.POST['numTesCT5'])
	miembroCT5= T.objects.get(numeroTesis= numTesisComite5)
	nombreMiembroCT5= 'Dr. '+miembroCT5.director1+' '+miembroCT5.director1Aps

	nuevaTesis= T()
	nuevaTesis.numeroTesis= todasLasTesis[0].numeroTesis+1
	nuevaTesis.nombreTesis= request.POST['tituloPropuesto8']
	nuevaTesis.director1Aps= director1.director1Aps
	nuevaTesis.director1= director1.director1
	try:
		if request.POST['numTesDir2']: 
			numTesisDirector2= int(request.POST['numTesDir2'])
			director2= T.objects.get(numeroTesis= numTesisDirector2)
	except:
		print('No tiene segundo director.')
	nuevaTesis.director2Aps= director2.director1Aps
	nuevaTesis.director2= director2.director1
	nuevaTesis.diaCreacion= datetime.now().strftime("%Y-%m-%d")
	alumnoActual= A.objects.get(username= request.user)
	nuevaTesis.alumnoAps= alumnoActual.apellido # 'Castellanos Castro'
	nuevaTesis.alumno= alumnoActual.nombre # 'David'
	nuevaTesis.save()

	bandera = 1
	if (Alumno.objects.filter(username= request.user).count()) > 0:
		bandera = 1
	elif (Profesor.objects.filter(username= request.user).count()) > 0:
		bandera = 2
	elif (PersonalAdministrativo.objects.filter(username= request.user).count()) > 0:
		bandera = 3
	return render(request, "tesis/inscripcionTesisInicio.html",{
			'tipoUsuario': bandera,
			'tesisInscrita': nuevaTesis,
		})