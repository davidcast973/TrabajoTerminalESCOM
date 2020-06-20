text= tituloPropuesto
texto= list()
for c in text:
   if c not in non_words:
      texto.append(c)
   elif c == '\n':
      texto.append(' ')

caracteres= ''.join(texto)
tokens = word_tokenize(caracteres)
if not tokens:
   w2v= ','.join([str(0) for x in range(300)])
else:
   w2v= [0 for x in range(300)]
   for w in tokens:
      #print(len(tokens),tokens)
      #print(len(w2v),w2v)
      if w in model:
         w2v+= model[w]

w2vc= ','.join(str(w) for w in w2v)

w2vc.split(',')

