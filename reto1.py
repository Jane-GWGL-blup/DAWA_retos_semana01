#Reto1 Formato de 12 horas a formato de 24 horas

date=input("Ingrese alguna fecha en formato de 12 horas:\n")

def timeConversion(t):
   if t[-2:] == "AM" :
      if t[:2] == "12":
          return str("00" + t[2:-2])
      else:
          return t[:-2]
   else:
      if t[-2:]== "PM" and t[:2] == "12":
          return t[:-2]
      else:
          return str(int(t[:2]) + 12) + t[2:8]

print(timeConversion(date))
