def hiName():
  name = input('Enter your name: ')
  return f"Hello {name.title()}"

def grossPay(h, r):
  h = int(input('Enter Hours: '))
  h = float(input('Enter Rate: '))
  return h * r

def multiFunc():
  width = float(input('Enter width: '))
  height = float(input('Enter height: '))
  dubbleDiv = width // height
  div = width / height
  ar = []
  ar.append(dubbleDiv)
  ar.append(div)
  return ar