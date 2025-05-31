def test(ip):
  
  if(ip[0] >= 0 and ip[0] <= 127):
    return "The IP address belongs to class : A"
   
  elif (ip[0] >=128 and ip[0] <= 191):
    return "The IP address belongs to class : B"
   
  elif (ip[0] >= 192 and ip[0] <= 223):
    return "The IP address belongs to class : C"
   
  elif (ip[0] >= 224 and ip[0] <= 239):
    return "The IP address belongs to class : D"
   
  else:
    return "The IP address belongs to class : E"

ip = "10.0.0.1"
ip = [int(i) for i in ip]  
print(test(ip))