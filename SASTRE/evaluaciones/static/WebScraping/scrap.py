#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import sys
import io
import re

htmlMisProfes = ""
l = io.open('htmlMisProfes.txt','r', encoding="utf-8")
for linea in l:
	htmlMisProfes += linea
dataPrincipal = htmlMisProfes
soupP = BeautifulSoup(dataPrincipal,'html.parser')
nProfesores = len(soupP.select('td.visible-xs > a'))
print("No. profesores =",nProfesores)

ligaAnterior = ""
k = 1;
for a in soupP('a', href=re.compile("https://www.misprofesores.com")):
	if (k <= nProfesores):	#nProfesores
		if (a['href'] != ligaAnterior):
			print("Liga = ",a['href'])
			url = a['href']

			r = requests.get(url)
			data = r.text

			soup = BeautifulSoup(data,'html.parser')

			opiniones = ''
			paginasOpinion = len(soup.select('ul.pagination > li')) - 2
			#print("Paginas de opinion =",paginasOpinion)

			for pagina in range(1,paginasOpinion+1):
				if pagina == 1:
					url2 = url
					#print("\t\tVisitando: ",url2)
				else:
					url2 = url + "?pag=" +str(pagina)
					#print("\t\tVisitando: ",url2)
				r2 = requests.get(url2)
				data2 = r2.text
				soup2 = BeautifulSoup(data2,'html.parser')
				for tag in soup2('p', class_ = 'commentsParagraph'):
					opiniones += tag.contents[0].encode("raw_unicode_escape").decode("utf-8").strip() + "\n"

			nombreArchivo = "opiniones" + str(k) + ".txt"
			f=open(nombreArchivo,"w+")
			f.write(opiniones.lower(). replace(".",""))
			f.close()

			k += 1


		ligaAnterior = a['href']

"""
url = "https://www.misprofesores.com/profesores/Rafael-Aguilar-Garcia_32564"

r = requests.get(url)
data = r.text

soup = BeautifulSoup(data,'html.parser')

opiniones = ''
paginasOpinion = len(soup.select('ul.pagination > li')) - 2

for pagina in range(1,paginasOpinion+1):
	if pagina == 1:
		url = "https://www.misprofesores.com/profesores/Rafael-Aguilar-Garcia_32564"
	else:
		url = "https://www.misprofesores.com/profesores/Rafael-Aguilar-Garcia_32564?pag="+str(pagina)
	r2 = requests.get(url)
	data2 = r2.text
	soup2 = BeautifulSoup(data2,'html.parser')
	for tag in soup2('p', class_ = 'commentsParagraph'):
		opiniones += tag.contents[0].encode("raw_unicode_escape").decode("utf-8").strip() + "\n"

#print(opiniones)

f=open("opiniones.txt","w+")
f.write(opiniones.lower(). replace(".",""))
f.close()
"""