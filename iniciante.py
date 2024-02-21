number = int(input())
qtd_horas = int(input())
valor = float(input())
salary = qtd_horas * valor
print("NUMBER =",number)
print(f"SALARY = U$ {salary:.2f}")


nome = input()
sal_fixo = float(input())
vendas = float(input())

total = sal_fixo + (vendas * 0.15)

print(f'TOTAL = R$ {total:.2f}')

raio = int(input())
pi = 3.14159
volume = (4/3) * pi * raio**3
print(f'VOLUME = {volume:.3f}')

values = [int(x) for x in input().split()]
maior = values[0]
for valor in values:
    if  valor > maior:
        maior = valor
print(maior,"eh o maior")

import math
valor_x = [float(x) for x in input().split()]
valor_y = [float(y) for y in input().split()]
x1 = valor_x[0]
y1 = valor_x[1]
x2 = valor_y[0]
y2 = valor_y[1]
distancia = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
print(f"{distancia:.4f}")

velocidade = int(input())
saida = velocidade * 2
print(saida, 'minutos')


valor = int(input())
notas_100 = valor//100
notas_50 = valor % 100 // 50
notas_20 = (valor % 100) % 50 // 20
notas_10 = ((valor % 100) % 50) % 20 // 10
notas_5 = (((valor % 100) % 50) % 20) % 10 // 5
notas_2 = ((((valor % 100) % 50) % 20) % 10) % 5 // 2
notas_1 = (((((valor % 100) % 50) % 20) % 10) % 5 ) % 2 // 1
print(valor)
print(notas_100,'nota(s) de R$ 100,00')
print(notas_50,'nota(s) de R$ 50,00')
print(notas_20,'nota(s) de R$ 20,00')
print(notas_10,'nota(s) de R$ 10,00')
print(notas_5,'nota(s) de R$ 5,00')
print(notas_2,'nota(s) de R$ 2,00')
print(notas_1,'nota(s) de R$ 1,00')


valores = input().split()
a, b, c = map(float, valores)
delta = b*b-4*a*c
delta_r = delta ** 0.5
if a == 0.0 or delta < 0.0:
    print('Impossivel calcular')
else:
    x1 = ((- b + delta_r) / (2 * a))
    x2 = ((- b - delta_r) / (2 * a))
    print('R1 = 'f'{x1:.5f}')
    print('R2 = 'f'{x2:.5f}')

valor = float(input())

if valor >= 0 and valor <= 25:
    print('Intervalo [0,25]')
elif valor > 25 and valor <=50:
    print('Intervalo (25,50]')
elif valor > 50 and valor <= 75:
    print('Intervalo (50,75]')
elif valor > 75 and valor <= 100:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')

cidade = [
    {"ddd": 61, "destination": "Brasilia"},
    {"ddd": 71, "destination": "Salvador"},
    {"ddd": 11, "destination": "Sao Paulo"},
    {"ddd": 21, "destination": "Rio de Janeiro"},
    {"ddd": 32, "destination": "Juiz de Fora"},
    {"ddd": 19, "destination": "Campinas"},
    {"ddd": 27, "destination": "Vitoria"},
    {"ddd": 31, "destination": "Belo Horizonte"}
]
codigo = int(input())
ddd_encontrado = False  
for cidade_info in cidade:
    if codigo == cidade_info['ddd']:
        print(cidade_info['destination'])
        ddd_encontrado = True
        break 
if not ddd_encontrado:
    print("DDD nao cadastrado")

codigo  = int(input())
if codigo == 61:
    print("Brasilia")
elif codigo == 71:
    print("Salvador")
elif codigo == 11:
    print("Sao Paulo")
elif codigo == 21:
    print("Rio de Janeiro")
elif codigo == 32:
    print("Juiz de fora") 
elif codigo == 19:
    print("Campinas")
elif codigo == 27:
    print("Vitoria")
elif codigo == 31:
    print("Belo Horizonte")
else:
    print("DDD nao encontrado")   


valores = input().split()
a, b, c, d = map(float, valores)
media = (a*2 + b*3 + c*4 + d*1)/10
if media >= 7.0:
    print("Media:", f'{media:.1f}')
    print("Aluno aprovado.")
elif media >=5.0 and media <= 6.9:
    print("Media:",f'{media:.1f}')
    print("Aluno em exame.")
    exame = float(input())
    resultado = (media + exame) / 2
    print("Nota do exame:",f'{exame:.1f}')
    if resultado >= 5.0:
        print("Aluno aprovado.")
        print("Media final:", f'{resultado:.1f}')
    else:
        print("Aluno aprovado.")
        print("Media final:",f'{resultado:.1f}')
else:
    print("Media:", f'{media:.1f}')
    print("Aluno reprovado.")

num = int(input())
contador = 1
while contador <= num:
    if contador%2 == 1:
        print(contador) 
    contador += 1

valor1 = float(input())
valor2 = float(input())
valor3 = float(input())
valor4 = float(input())
valor5 = float(input())
valor6 = float(input())

lista_valor = [valor1, valor2, valor3, valor4, valor5, valor6]
valor_positivo = []
for valor in lista_valor:
    if valor >= 0:
       valor_positivo.append(valor)
print(len(valor_positivo), 'valores positivos')

valor1 = int(input())
valor2 = int(input())
valor3 = int(input())
valor4 = int(input())
valor5 = int(input())
lista_valor = [valor1, valor2, valor3, valor4, valor5]
par = 0
impar = 0
positivo = 0
negativo = 0
for valor in lista_valor:
    if valor > 0:
        positivo+=1
    elif valor < 0:
        negativo+=1    
    if valor %2 == 0:
        par +=1
    else:
        impar +=1  
print(par, 'valor(es) par(es)')
print(impar, 'valor(es) impar(es)')
print(positivo, 'valor(es) positivo(s)')
print(negativo, 'valor(es) negativo(s)')



valor1 = float(input())
valor2 = float(input())
valor3 = float(input())
valor4 = float(input())
valor5 = float(input())
valor6 = float(input())

lista_valor = [valor1, valor2, valor3, valor4, valor5, valor6]
valor_positivo = []
for valor in lista_valor:
    if valor >= 0:
       valor_positivo.append(valor)
print(len(valor_positivo), 'valores positivos')
print(f'{sum(valor_positivo)/len(valor_positivo):.1f}')

valor1 = input().lower()

if valor1 == 'vertebrado':
    valor2 = input().lower()
    
    if valor2 =='ave':
        valor3 = input().lower()
        
        if valor3 == 'carnivoro':
            print('aguia')
        elif valor3 =='onivoro':
            print('pomba')
            
    elif valor2 == 'mamifero':
        valor3 = input().lower()
        if valor3 =='onivoro':
            print('homem')
            
        elif valor3 == 'herbivoro':
            print('vaca')   
            
elif valor1 == 'invertebrado':
    valor2 = input().lower()
    
    if valor2 =='inseto':
        valor3 = input().lower()
        if valor3 =='hematofago':
            print('pulga')
        
        elif valor3 =='herbivoro':
            print('lagarta')
            
    elif valor2 == 'anelideo':
        valor3 = input().lower()
        
        if valor3 == 'hematofago':
            print('sanguessuga')
            
        elif valor3 == 'onivoro':
            print('minhoca')
    
valor1 = int(input())
valor2 = int(input())
valor3 = int(input()) 
valor4 = int(input())
valor5 = int(input())
lista_valor = [valor1, valor2, valor3, valor4, valor5]
contador_par = 0
for val in lista_valor:
    if val %2 == 0:
        contador_par+=1
print(contador_par, 'valores pares')

valor = float(input())

if valor >= 0 and valor <= 2000.00:
    print('Isento')
elif valor > 2000 and valor <= 3000.00:
    print(valor*0.08)
elif valor > 3000.00 and valor <=4500.00:
    print(valor*0.18)
elif valor > 4500.00:
    print(valor*0.28)

valores = input().split()
inicio, fim = map(int, valores)
if inicio < fim:
    print('O JOGO DUROU',fim - inicio,'HORA(S)')  
elif inicio == fim:
    print('O JOGO DUROU',24,'HORA(S)')
elif inicio < 24 and fim < inicio:
    print('O JOGO DUROU',(24 - inicio) + fim,'HORA(S)')



valor1 = int(input())
valor2 = int(input())
valores =[]
if valor1 < valor2:
    for i in range(valor1 +1, valor2):
        valores.append(i)
    for val in valores:
        if val %5 == 2 or val %5 == 3:
            print(val)
else:
    for i in range(valor2 +1, valor1):
        valores.append(i)
    for val in valores:
        if val %5 == 2 or val %5 == 3:
            print(val)


valor1 =  int(input())
valor2 = int(input())
lista_valores = []
if valor1<valor2:
    for i in range(valor1, valor2+1):
        if i % 13 != 0:
            lista_valores.append(i)
else:
    for i in range(valor2, valor1+1):
        if i % 13 != 0:
            lista_valores.append(i)
print(sum(lista_valores))

r1 = int(input())
r2 = int(input())
r3 = int(input())
r4 = int(input())
r5 = int(input())
r6 = int(input())
lista = [r1, r2, r3, r4, r5, r6]

for l in lista:
    if l == 0:
        print('vai ter copa!')
    elif l > 0:
        print('vai ter duas!')

while True:
    try:
        l = int(input())
        if l == 0:
            print('vai ter copa!')
        elif l > 0:
            print('vai ter duas!')
    except EOFError:
        break


while True:
    try:
        palavra = input()
        if len(palavra) >= 10:
            print('palavrao')
        else:
            print('palavrinha') 
    except EOFError:
        break

qtd = int(input())
contador = 0
qtd_resposta = []
lista_resposta = []
while contador < qtd:
    r = input()
    contador +=1
    qtd_resposta.append(contador)
    lista_resposta.append(r)
for i in range(0, len(lista_resposta)):
    print(f'resposta {qtd_resposta[i]}: {lista_resposta[i]}')
    
    
valor = input()
contador = 0
for i in range(0, len(valor)):
    if valor[i] == '1' and valor[int(i)+1] == '3':     
        contador += 1
if contador > 0:
    print(valor, 'es de Mala Suerte')
else:
    print(valor, 'NO es de Mala Suerte')
        


valor = input()
if '13' in valor:
    print(valor, 'es de Mala Suerte')
else:
    print(valor, 'NO es de Mala Suerte')

