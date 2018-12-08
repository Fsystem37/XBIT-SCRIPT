from urllib.request import urlopen
import urllib
i_face = ("""

##     ## ########  #### ######## 
 ##   ##  ##     ##  ##     ##    
  ## ##   ##     ##  ##     ##    
   ###    ########   ##     ##    
  ## ##   ##     ##  ##     ##    
 ##   ##  ##     ##  ##     ##    
##     ## ########  ####    ##    
""")
print(i_face)
url = input('Informe a Url: ')
f = urllib.request.urlopen(url)
A = str(f.read())

pergunta = input("Deseja Criar Um Arquivo de Texto? (S) | (N): ")
if pergunta == "S":
	Arquivo = open('Url-xbit.txt', 'w')
	Arquivo.write(A)
	Arquivo.close()
elif pergunta == "N":
	print("OK")
