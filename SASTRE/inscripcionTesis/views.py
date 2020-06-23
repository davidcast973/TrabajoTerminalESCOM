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
from datetime import datetime # Castear a fecha AAAA-MM-DD

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
#DEVELOP	tokens = word_tokenize(caracteres)
#DEVELOP	if not tokens:
#DEVELOP	   w2v= ','.join([str(0) for x in range(300)])
#DEVELOP	else:
#DEVELOP	   w2v= [0 for x in range(300)]
#DEVELOP	   for w in tokens:
#DEVELOP	      #print(len(tokens),tokens)
#DEVELOP	      #print(len(w2v),w2v)
#DEVELOP	      if w in model:
#DEVELOP	         w2v+= model[w]

	w2v= [0.919521618518047,-5.655392378335819,8.857106631621718,-9.068047257127546,-7.206783882342279,9.541452264413238,-11.495914850383997,-0.9195252464269288,26.368830962572247,-10.517578852828592,3.0800743082072586,-1.8356365880463272,15.166360976872966,-22.750919521553442,15.980451593757607,2.580012279446237,-0.05734285805374384,4.95901564945234,-1.4832114436430857,13.687714587431401,-3.8934499688402866,-14.797070475528017,3.4808384058997035,24.23331611743197,1.6324695160146803,-12.198768595229922,-6.71034404123202,23.51800588471815,2.9144578874111176,33.3215943002142,10.533382883528247,-17.068242801586166,-7.27630093623884,1.2519142623059452,6.010551201557973,-11.560171821154654,-13.50402878690511,-2.6832703853433486,-8.053791098529473,2.152409076457843,13.646590041287709,14.071059139270801,-8.218982818216318,-13.201403229031712,-9.912946669166558,-15.944560995674692,3.02906703093322,-6.570450018858537,4.673147986410186,26.778979364782572,-4.334427568886895,26.30386399710551,-2.1767658308381215,24.284712959779426,-5.284415603615344,9.454239248298109,-14.425504278275184,-24.39116131514311,17.86376755638048,9.163385020452552,-3.577472985140048,6.457123226369731,-14.254489335115068,-3.399302866891958,-0.9840802801772952,12.727240856038406,-16.223211791948415,21.550431976094842,-21.024741346016526,11.996426870231517,-14.228267350234091,-11.878309563733637,5.6153041599318385,10.411447883583605,-16.023220209404826,23.938924965797924,-8.918646527919918,1.8872132902033627,-18.721693641971797,-3.713543468620628,2.802860939875245,2.5071348515339196,13.195137077418622,11.742874868446961,-1.1722607191186398,-11.431788894289639,2.7550653335056268,3.3835702675860375,20.77726275799796,3.9075189190916717,-0.4641563744517043,-1.41887749126181,18.640941524179652,8.25496930393274,-15.218398159602657,-0.19867992150830105,7.577847653068602,0.7574641971295932,1.4982602330856025,23.204629733460024,-20.735638620331883,-21.1826398500707,-9.808373474515975,28.033054292667657,12.610515058971941,-8.381551862461492,-7.5951761174655985,-29.043418218847364,4.216829553479329,21.479723239317536,8.264180459314957,16.16881265398115,8.338298331131227,9.478541505988687,-6.071195448981598,-13.674346211366355,20.449628556147218,-2.159767056349665,-13.177057500462979,-20.036432911467273,-7.349274783860892,7.914631284496863,-20.452875721850432,-8.03183538466692,-12.776001769991126,13.365600112010725,3.37143591651693,-5.700060204835609,11.070145700359717,-3.8251567236729898,13.517300252337009,8.033270400192123,-11.716496289664065,-8.90775855933316,-18.632203249726444,17.085478253895417,-1.1386036083567888,-21.69995303172618,10.190814631059766,-2.2216058063786477,-2.341089215129614,-3.749665734823793,1.3302643173374236,-4.923016739543527,-13.517179524642415,-0.804653403814882,2.1288050378207117,-20.001314454944804,34.37097400682978,-7.705550142331049,18.06791309406981,-2.1501732069882564,-14.78747841672157,-15.216731749475002,-2.602575145487208,-14.476501494238619,21.45811263844371,-2.738478451035917,-11.05663039488718,-5.406685204710811,2.184078960795887,-18.203426758758724,23.005908912047744,4.605826102779247,-1.1543212664546445,-5.3793374467641115,-8.000462382566184,13.07287330366671,12.806493933312595,-15.708762224589009,15.066155534004793,-23.777920237742364,7.312962990661617,-2.18239350640215,15.28783403255511,-29.99226542748511,-2.283058332162909,-4.750743099488318,-6.427671832119813,8.83392061269842,17.775251217070036,19.399573844275437,16.983794975094497,-3.442557512084022,-5.890876665012911,7.473767196119297,-4.5850100598763674,-21.21170545462519,-7.245732369250618,-3.3934179237112403,-18.121638755314052,7.164465148583986,4.1143266701838,-9.13453134172596,0.013822168577462435,28.816228980664164,4.9342038771137595,14.501864884863608,1.3372694374993443,-4.132059666328132,-28.873432498425245,-6.595603640191257,0.0387746961787343,1.875400136981625,-2.096763345383806,-11.627391760761384,6.71972236293368,-5.421510066371411,3.539558637654409,13.733308704104275,-18.97296290565282,-15.649424536852166,-10.157577629142907,-1.7818061970174313,11.026236679404974,14.3547309943242,-13.248220071429387,17.303019581129774,-6.815530427498743,0.33355115117228706,-0.791028555482626,-2.275318529631477,7.263757145963609,-0.968046696158126,-20.189136611123104,-0.6603473932482302,9.029577531851828,-0.7440944493282586,-15.346301747951657,-7.63299653690774,4.422706549987197,10.156599347479641,4.174954362213612,11.140966556500643,-24.820622803177685,13.69131074170582,5.977688507176936,-10.13846655114321,-23.333306641783565,10.161355562857352,39.23668587044813,-3.7895008369814605,-3.02378842048347,-14.974292503669858,-33.918703213334084,-5.945044026244432,-16.994425708428025,-11.103196190437302,-4.136539125815034,12.9734417127911,13.12821773532778,9.513007749337703,9.464485181495547,-1.3540730951353908,-14.67915000882931,-5.91494885092834,-0.3952127208467573,2.3954977452522144,-16.793200029991567,-9.454867062915582,16.770860678050667,26.48955664038658,1.8539565520477481,-1.3160688770003617,-5.551603138796054,-6.8385250743012875,-4.240851801354438,5.519789717891399,-3.595195559435524,27.551894512260333,-7.515286184148863,18.37388602993451,14.43403303285595,8.79227093388181,2.664475101279095,2.2978756189113483,10.211953612044454,10.478360910899937,4.580228716833517,-7.993507374892943,-22.238915755246126,-1.4478002544492483,-20.636866115033627,12.964724677731283,24.643043372780085,-5.905895092757419,12.142054036841728,6.033664743008558,2.841751545900479,-18.70812687650323,-5.230171243660152,12.52426943127648,-8.316388849634677,-0.2682298766449094,-14.090470737894066,-22.052424714667723,0.30955483112484217,-27.43562521133572,-0.053252513287588954,-2.0686346073634923]

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