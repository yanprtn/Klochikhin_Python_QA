def run():
  a = list(map(int, input('Enter numbers space-separated: ').split()))
  print('Multiples of 3: ')
  for x in a:
      if x % 3 == 0: print(x)