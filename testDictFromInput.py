user_name = 'sr'
print ("Hello " + user_name + '!!')

dictSensorAirData = {'Temp': 30, 'Hum': 40}
print (dictSensorAirData)

dictSensorPowerSupplyData = {'Temp': 20, 'Hum': 50}
dictSensorMultiprocessorData = {'Temp': 10, 'Hum': None}
dictSensorAir = {'name': 'air', 'data':dictSensorAirData}
dictSensorPowerSupply = {'name': 'powersupply', 'data':dictSensorPowerSupplyData}
dictSensorMultiprocessor = {'name': 'multiprocessor', 'data':dictSensorMultiprocessorData}
dictSensor = {
    'air': {
        'temp': 30,
        'hum': 40
    },
    'powersupply': {
        'temp': 20,
        'hum': 50
    },
    'multiprocessor': {
        'temp': 10,
        'hum': None
    }
}
#dictSensor
for key, value in dictSensor.items():
    #print ("\t", key)
    #for keyv, valuev in value:
    #    print ("keyv:", keyv, "value:", valuev)
    print ("key:", key, "\tvalue:", value)

print ("len(dictSensor)=", len(dictSensor))
print ("is 'air' in keys of dictSensor?", ("air" in dictSensor.keys()))        # key 목록에서 air 가 존재하는지 출력
print ("is 'air' not in keys of dictSensor?", ("air" not in dictSensor.keys()))    # key 목록에서 air 가 없는지 출력
#print ("is 'temp' in keys of dictSensor?", ("temp" in dictSensor.values().keys()))        # key 목록에서 air 가 존재하는지 출력


# dictSensor[4] creates KeyError
print("get(1)=", dictSensor.get(1))
print("get(1, 'NA')=", dictSensor.get(1, 'NA'))

# 코딩도장 https://dojang.io/mod/quiz/review.php?attempt=965035&cmid=2217
# v1
'''
testkeys = input().split()
testvalues = input().split()
testdict = dict()

for key in range(len(testkeys)):
    testdict[testkeys[key]] = testvalues[key]

for key, value in testdict.items():
    print ("key:", key, "\tvalue:", value)

print (testdict)
'''
# 실패 아래 안내가 있음
'''
input().split()을 사용한 뒤 변수 한 개에 저장하면 입력값을 리스트로 저장할 수 있습니다. 이때 문자열과 숫자가 두 줄로 입력된다고 했으므로 input().split()를 두 번 사용해야 합니다. 그리고 숫자는 실수라고 했으므로 map에 float를 사용하여 실수로 변환해줍니다.

리스트 두 개가 준비되었으면 리스트를 zip에 넣은 뒤 다시 dict에 넣어서 딕셔너리로 만듭니다. 그리고 이 딕셔너리를 print로 출력하면 됩니다.
'''
# v2
testkeys = input().split()
testvalues = map(float, input().split())
testdict = dict(zip(testkeys, testvalues))
print (testdict)