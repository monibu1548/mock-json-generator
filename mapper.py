import copy
import json
from format import format
from variables import variables

formatObject = json.loads(format)
vars = []
for var in formatObject.values():
    if var[0] is '#' and var[-1] is '#':
        vars.append(var.replace("#", ""))

dataSet = {}
for var in vars:
    dataSet[var] = variables[var]

caseCnt = 1
for var in vars:
    caseCnt *= len(variables[var])

objs = []

for idx in range(caseCnt):
    newObj = copy.deepcopy(formatObject)

    currentAge = 1
    for var in vars:
        cnt = len(dataSet[var])
        index = int(idx / currentAge) % cnt
        value = dataSet[var][index]
        newObj[var] = value
        currentAge *= cnt
    objs.append(newObj)

jsonStr = json.dumps(objs)
print(jsonStr)