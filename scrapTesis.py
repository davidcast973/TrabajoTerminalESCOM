import requests
import pickle
from bs4 import BeautifulSoup
import re

# Obtiene info de un total de 680 tesis
# No de tesis = paginas * 20
# PAGINAS MAX = 34

n = 0
paginas = 34
todasLasTesis= list()
for i in range(paginas):
	print("https://tesis.ipn.mx/handle/123456789/18977/recent-submissions?offset="+str(n))
	URL1 = "https://tesis.ipn.mx/handle/123456789/18977/recent-submissions?offset="+str(n)
	page = requests.get(URL1)

	soup = BeautifulSoup(page.content, 'html.parser')

	descriptionTesisDiv = soup.find_all('div', class_='artifact-description')

	titulosTesis = []
	idTesis = []
	tesis = []
	for tesisDiv in descriptionTesisDiv:
		titulosDiv = tesisDiv.find_all('div', class_='artifact-title')
		for titDiv in titulosDiv:
			titulosA = titDiv.find_all('a')
			link = titDiv.find('a')['href']
			idTesis.append(link.split("/")[3])
			for titulo in titulosA:
				titulosTesis.append(titulo.text)

	for indice, id in enumerate(idTesis):
		URL2 = 'https://tesis.ipn.mx/handle/123456789/'+id+'?show=full'
		page = requests.get(URL2)

		soup = BeautifulSoup(page.content, 'html.parser')
		tdTags = soup.find_all('td')
		print("...")
		autor = ""
		directores = ""
		resumen = ""
		creacion = ""
		for num, tdT in enumerate(tdTags, start=1):
			cadena = str(tdT)
			cadena = cadena[23:]
			cadena = cadena[:-5]
			#Autores
			if cadena == "dc.contributor.author":
				cadena = str(tdTags[num])
				autor = cadena[4:]
				autor = autor[:-5]
			#Fecha de creacion
			if cadena == "dc.date.created":
				cadena = str(tdTags[num])
				creacion = cadena[4:]
				creacion = creacion[:-5]
			#Resumen 26
			if cadena == "dc.description.abstract":
				cadena = str(tdTags[num])
				resumen = cadena[14:]
				posABS = resumen.find("ABSTRACT")-4
				resumen = resumen[:posABS]
			#Directores
			if cadena == "dc.contributor.advisor":
				cadena = str(tdTags[num])
				directores = cadena[4:]
				directores = directores[:-5]
		tesis.append([id, titulosTesis[indice], autor, directores, resumen, creacion])
	n+=20
	todasLasTesis+=tesis

print(len(todasLasTesis))

archivo= open('Reusumenes.pickle','wb')
pickle.dump(todasLasTesis,archivo)
archivo.close()