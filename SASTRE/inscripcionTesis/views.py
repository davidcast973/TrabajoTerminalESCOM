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

	# Texto procesado "Arquitectura  para el control de un robot móvil"
	w2v= [-0.5495192315429449, -0.34797058068215847, 0.17619149759411812, -0.16387923061847687, 0.017832474783062935, 0.37431367486715317, -0.7861134121194482, -0.04947494249790907, 2.4136261716485023, 0.42446110025048256, -0.13858842849731445, 0.10039005894213915, 0.28747745673172176, -1.52573361992836, 0.8010595717933029, -0.4194407109171152, -0.38271481916308403, -0.2364682387560606, -0.9983300494495779, 0.6259154640138149, -0.6344516389071941, -0.2599947825074196, 0.37907304015607224, 1.0764406034722924, 0.11531463277060539, -0.4638367835432291, 0.4489955324679613, 1.0842948481440544, 0.22915614396333694, 1.7642535492777824, 0.5208671055734158, -0.6952852830290794, -0.6233508102595806, 0.16224892809987068, 0.505573146045208, -0.16328345984220505, -0.7288663564249873, -0.28638575226068497, -0.024360593408346176, -0.4056930746883154, 1.478009625338018, 1.048297181725502, -0.5938500799238682, -1.2384390719234943, -0.5181473270058632, -0.7534605916589499, 0.39803011156618595, -0.24970252811908722, 0.34823403880000114, 1.6176244542002678, 0.04319642577320337, 1.5401498004212044, 0.39217640459537506, 1.745975285768509, -0.15778553672134876, 0.13008869532495737, -0.30120745999738574, -1.0618054829537868, 1.1181855015456676, 0.1866836603730917, -0.8091611452400684, 1.2270067110657692, -0.7897023288533092, -0.7694542240351439, -0.24537069723010063, 1.2061950042843819, -0.8057251051068306, 1.8014927804470062, -1.431508131325245, -0.02466927468776703, -1.0825082175433636, -0.3226095363497734, 1.243466578423977, 0.9356079529970884, -1.1967629715800285, 1.7799862325191498, -0.8234200589358807, 1.1056316900067031, -0.9884682558476925, -0.8226148595567793, 0.7213230449706316, -0.33653812296688557, 0.7755356356501579, 0.6818945724517107, 0.7180433142930269, -1.1857774686068296, -0.039943158626556396, -0.16391361318528652, 0.7125381492078304, 0.5665239188820124, 0.3690278520807624, -0.5949060246348381, 0.9719165218994021, 0.8353441257750092, -1.3114166893064976, 0.4038510974496603, 0.29381765983998775, -0.33508477779105306, -0.1770523004233837, 1.3989825211465359, -0.40001434506848454, -1.6836966052651405, 0.15831373818218708, 1.32928916066885, 0.8632783368229866, -0.530376935377717, -0.8777562566101551, -1.1523080877959728, -0.15129247546428815, 0.7316274233162403, 0.9452899619936943, 0.34530244627967477, 0.7311264090240002, -0.16745923762209713, 0.18011595401912928, -1.2252395101822913, 1.51938159391284, 0.6675274423323572, -1.4740789914503694, -1.4804717153310776, -1.4567841291427612, 0.8477525701746345, -2.1703840270638466, 0.14944592723622918, -1.0073263575322926, 0.49035055679269135, -0.7938284110277891, 0.3434533029794693, 1.1397138820029795, -0.08528753742575645, 1.1713482178747654, 0.8105442859232426, -1.2834890633821487, 0.21713316347450018, -1.085718385875225, 1.0109353363513947, 0.47202075587119907, -1.2473531607538462, 0.6825273274444044, -0.3267208533361554, -0.4904313161969185, 0.3102813856676221, 0.08020573854446411, -0.42715753697848413, -1.047913022339344, -1.1648286115378141, 0.6124414477963, -1.1755410842597485, 1.9156825952231884, -0.29860353167168796, 0.015243300702422857, 0.8396117342635989, -0.09658524580299854, -0.6798034980893135, 0.0071269311010837555, -0.5358242318034172, 1.1772687239572406, 0.21521308552473783, -1.4862091392278671, -0.801512323319912, -0.14647704793605953, -1.9159007808193564, 1.5080155581235886, -0.6864615008234978, -0.20280596613883972, -0.37046629562973976, -0.772381504997611, 0.6703130872920156, 1.1276600742712617, -1.1924738343805075, 1.4201611801981926, -1.2719166092574596, 0.6812678296118975, 0.40754109248518944, -0.21404590969905257, -2.177492007613182, -0.17574653960764408, -0.27723242808133364, -0.3918653605505824, 0.6962885328102857, 0.8031897228211164, 1.7541121169924736, 1.0528057077899575, -0.3171791471540928, -1.255836233496666, 1.0658508315682411, 0.02235090546309948, -0.6901038065552711, -0.39756869338452816, 0.16768981888890266, -1.104564107954502, 0.2358536198735237, 0.6537619009613991, -0.7429243437945843, 0.45192957296967506, 2.1513650827109814, -0.38777907378971577, 1.4604068002663553, -0.26267874985933304, 0.561637768521905, -2.0024312660098076, -0.004678717348724604, 0.3644426055252552, -0.09757483936846256, 0.32930698804557323, -0.9601285681128502, 0.22456539422273636, -0.25720501132309437, -0.0018901294097304344, 1.3874680357985198, -1.2861711969599128, -0.8098446186631918, -0.6194294085726142, 0.184427740983665, 1.1780861616134644, 0.9420998245477676, -0.34999923035502434, 1.364382155239582, -0.46502075158059597, 0.44519274681806564, 0.2102547213435173, 0.17688840255141258, 0.1330358162522316, -0.046906237956136465, -1.617478497326374, -0.16223960183560848, 0.7313263677060604, -0.031950813718140125, -1.5188035713508725, -1.1635163575410843, 0.5565391608979553, 0.4391230642795563, 0.428314967546612, 0.78179229516536, -2.2697391733527184, 0.7674542926251888, -0.16502764075994492, -0.46327825263142586, -0.3037332408130169, 0.7663750350475311, 2.976121708750725, 0.2881934968754649, 0.8925714248325676, -0.7314782491885126, -1.2455440759658813, 0.00413364265114069, -0.930653068702668, -0.527400472201407, 0.6901715013664216, 0.7144821435213089, 1.0135097559541464, 0.7965917587280273, 0.9194725044071674, 0.257174052298069, -1.322143193334341, -1.3360368283465505, -0.007157790591008961, -0.3276708535850048, -1.051824018592015, -1.0781733691692352, 1.7279136329889297, 1.14709110558033, 0.18587529519572854, 0.20449632359668612, -0.683350894600153, -0.008920329855754972, -0.06508673238568008, 0.757329847663641, 0.23794000688940287, 0.5438607791438699, -0.39510999992489815, 0.6004135617986321, 0.9555276772007346, 0.29173692502081394, -0.07157929427921772, 0.38960835710167885, 0.4362741708755493, 0.7134364256635308, -0.6273416401818395, -1.1095608621835709, -1.8714832048863173, 0.40164102986454964, -1.692255575209856, 0.9756958335638046, 1.8443616926670074, -0.322727934923023, 0.5642646253108978, 0.233043622225523, -0.34436986967921257, -1.3989185690879822, -0.3410388631746173, 0.9516759980469942, -0.7351089930161834, 0.1750214733183384, -0.3434477709233761, -1.8746685907244682, -0.1449584886431694, -2.262067750096321, -0.18061198387295008, -0.11918510682880878]

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