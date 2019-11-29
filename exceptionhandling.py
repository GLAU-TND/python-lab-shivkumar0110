
print('start')
try:
    h=eval(input('enter the value'))
    print('data',10/h)
except ValueError as e:
    print('value not valid')
except EOFError as e:
    print('end of file')
except(ZeroDivisionError,TypeError,AttributeError) as e:
    print('Unknown error',e)
    
finally:
    print('end')


