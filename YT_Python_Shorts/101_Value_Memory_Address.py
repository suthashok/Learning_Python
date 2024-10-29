# Variable referencing to a value in Python
var1=3*5
print(var1,id(var1))

var2=var1
print(var2,id(var2))

var1=5
print(var1,id(var1))
print(var2,id(var2))
