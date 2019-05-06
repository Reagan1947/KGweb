relationDict = [{'rel': 'wom' , 'type': 'wwe'},{'type':'woee'}]
for i in range(len(relationDict)):
    relationName = relationDict[i]['rel']['type']
    print(relationName)