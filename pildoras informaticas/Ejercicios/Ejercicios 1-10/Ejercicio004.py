def suma(num1, num2):  
  print(num1+num2)

suma(2,3)#5

def resta(num1=0,num2=0):#con esto no necesito pasarle los dos parametros
  print(num1-num2)

resta(1,5)#-4

resta(1)

def multi(num1,num2):
  restultado=num1*num2
  return restultado

print(multi(3,4))#12
