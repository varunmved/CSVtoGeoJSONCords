featureCollectionString = """{
  "type": "FeatureCollection",
  "features": ["""

typeString = """{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": """
  
propertyString=  """"properties": {"""

nameString = '"Name": '
addString = '"Address": '
phoneString = '"Phone Number": '
emailString = '"Email": '
webString = '"Web Page": '

closeBracket1 = '  },'
closeBracket2 = '  }'
closeLastBracket = '}'

nameVal = "John Company"
addVal = "6842 asdfa asdfa, asfdadf, asfdasdfa, 23432"
phoneVal= "(916)-234-2343"
emailVal = "johnnycheese@gmail.com"
webVal = "ayylmoa.com"

lat = 38.1232
longi = -123.21321



outString = featureCollectionString + '\n' + typeString + "[" + str(lat) + "," + str(longi) + "]" + '\n'+ closeBracket1+ '\n'+propertyString + '\n' + nameString + '"' + nameVal + '"' + "\n"+ addString + '"' + addVal + '"' + "\n"+ phoneString + '"' + phoneVal + '"' + "\n"+ emailString + '"' + emailVal + '"' + "\n"+ webString + '"' + webVal + '"' + "\n"

print(outString)