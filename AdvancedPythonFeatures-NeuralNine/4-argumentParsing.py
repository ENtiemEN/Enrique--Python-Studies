# python3 myscript.py result.txt
# python3 myscript.py -o test.txt -l DEBUG -c

def myfunction(*args, **kwargs):
  print(args[0])
  print(args[1])
  print(kwargs['KEYONE'])
  print(kwargs['KEYTWO'])

myfunction('hey',True,KEYONE="TEST",KEYTWO=7)

