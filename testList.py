import sys

listOdd = [1,3,5,7,9]
listEmpty = []
listNumber = [1,2,3]
listStrings = ['Life', 'is', 'very', 'thankful']
listNumberStrings = [1,2,'Life','Savior']
listHasList = [1,2,['Life','Savior']]

print (listNumber[0])
print (listStrings[1], listStrings[-1])
print (listNumberStrings[2], listNumberStrings[-1])
print (listHasList[2], listHasList[-1],listHasList[-1][0], listHasList[-1][1][0])
# list slicing 나누기
print (listHasList[1:])
print (listHasList[0:1])

print ("listOdd has ", listOdd.count(5), " 5s")

num_even = [i for i in range(10) if i % 2 == 0]
num_odd = [i for i in range(10) if i % 2 == 1]

print ("even:", num_even, ", odd:", num_odd, sep='\n')

nVersionPython = sys.version
print(sys.version, sys.version_info, sys.api_version, sep='\n')
print(sys.version_info.major)
if sys.version_info.major == 2:
    nIntMax = sys.maxint   # for 2.x
else:
    nIntMax = sys.maxsize   # for 3.x
nIntMaxNext = nIntMax * 2
print (type(nIntMax), nIntMax, '\n', type(nIntMaxNext), nIntMaxNext)
strTest = 'hi' \
'kay' \
'tey' \
'say'
print (strTest)