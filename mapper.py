import copy
import json
from format import format
from variables import variables

vars = []
for var in format.values():
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
    newObj = copy.deepcopy(format)

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