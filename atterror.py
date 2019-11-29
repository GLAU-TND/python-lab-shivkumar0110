class Attributes(object):
    a = 2
    print (a)

try:
    object = Attributes()
    print (object.attribute)
except AttributeError as e:
    print ("Attribute Exception Raised.",e)


try:
    x = 12.4
    y = '33'
    z=x+y

except TypeError as e:
    print("Infinity",e)    


try:
    x = float('shiv')
except ValueError as e:
    print("You should have given a float" ,e)
