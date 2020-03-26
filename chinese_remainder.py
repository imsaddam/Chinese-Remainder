

def calculate_euclidian_extended_algorithm(input1, input2):
	if input1 == 0:
		return (input2, 0, 1)
	else:
		gcd, a, b = calculate_euclidian_extended_algorithm(input2 % input1, input1)
		return (gcd, b - (input2//input1) * a, a)

def modular_invers(a, m):
  g, x, y = calculate_euclidian_extended_algorithm(a, m) 
  return x % m 

def restechinois(a, n):
  while 1:
    if len(a) == 1: 
      break
    else:      
      variable1 = modular_invers(n[1], n[0]) * a[0] * n[1] +  modular_invers(n[0], n[1]) * a[1] * n[0] 
      variable2 = n[0] * n[1] 
      a.remove(a[0])
      a.remove(a[0])  
      a = [variable1 % variable2] + a   
      n.remove(n[0])  
      n.remove(n[0]) 
      n = [variable2] + n 
     
  return a[0] 


a = [4, 3] 
n = [5, 7]
restechinois (a, n)
