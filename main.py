"""
1.példa

szam = 1
while szam <= 10:
  print(szam)
  szam = szam + 1

"""
"""
2.példa
szamlalo = 4
while szamlalo <= 5:
  print('Programozni jó!')
  szamlalo = szamlalo + 1

  """
"""
  3.példa
folytatja = True
while folytatja:
      print('Vidd ki a szemetet!')
      valasz = input('Mondjam még egyszer? (i/n)')
      if valasz == 'n':
          folytatja = False
print('>> Program vége! <<')

"""
"""
4.példa
szam = int(input('Adj meg egy számot 5 és 10 között! '))
while not 5 <= szam <= 10:
      szam = int(input('Helytelen érték! Adj meg egy számot 5 és 10 között! '))
  
print('Rendben!')

"""
"""
5.példa
szo = input('Adj meg szavakat! Ha kilépnél, aszó helyett csak egy ENTER-t üss! ')

szo = None
while szo != '':
  szo = input('Adj meg szavakat! Ha kilépnél, aszó helyett csak egy ENTER-t üss! ')    
  
print('Program vége!')

"""