import json #json.dumps
import sys  #sys.stdout

dictConfig = { 'name':'sr', 'age':39}

print ("dictConfig = %s" % dictConfig)
print ("dictConfig type = %s" % type(dictConfig))
print ("====================")
dictConfig['hobby'] = 'game'
dictConfig['Lord'] = 'YHWH'

# convert dictionary to json using json.dump
jsonConfig = json.dumps(dictConfig)

print ("jsonConfig = %s" % jsonConfig, sep='=', end='$\r\n', file=sys.stdout, flush=True)
print ("jsonConfig type = %s" % type(jsonConfig))

dictConfig2 = json.loads(jsonConfig)
print (f'dictConfig2 = {dictConfig2}\ndictConfig2 type = {type(dictConfig2)}')