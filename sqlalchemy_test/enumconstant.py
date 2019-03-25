from enum import Enum

class StatusConstant(Enum):
    aa = 'q'
    bb = 'w'
    cc = 'e'
#print type(StatusConstant)
print(type(StatusConstant.aa))
print(type(StatusConstant.aa.name))
print(type(StatusConstant.aa.value))
print(isinstance(StatusConstant.aa,StatusConstant))
print(type(StatusConstant.__members__))
print(dir(StatusConstant.__members__))
for i in StatusConstant.__members__.keys():
    print(i)
    
for i in StatusConstant.__members__.values():
    print(i)

#print StatusConstant.aa.value
#print StatusConstant.aa.name
