import csv
import json

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
closeBrace = ']'

#string writer
def writeString():

	outString = typeString + "[" + str(longi) + "," + str(lat) + "]" + '\n'+ closeBracket1+ '\n'+propertyString 
	outString += '\n' + nameString + '"' + nameVal + '",' + "\n"+ addString + '"' + addVal + '",' 
	outString += "\n"+ phoneString + '"' + phoneVal + '",' + "\n"+ emailString + '"' + emailVal + '",' 
	outString += "\n"+ webString + '"' + webVal + '"' + "\n"
	outString +=closeBracket2+'\n'+closeBracket1+'\n'
	written.write(outString)



#csv handling
written = open("mbtestjson3.json","w")
outString = featureCollectionString + '\n' 
written.write(outString)
i=0
j=0

with open("mb_for_geojson_RAW10.csv",'rU') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			nameVal=row['NAME']
			emailVal=row['EMAIL']
			phoneVal=row['PHONE']
			webVal=row['WEB PAGE']
			addVal=row['ADDRESS']
			lat=row['latitude']
			longi=row['longitude']
			
			if (lat=='' or longi ==''):
				lat = '32'
				longi='-115'
				writeString();
			
			if (nameVal.find('"') != -1):
				i=i+1
				nameVal=nameVal.strip('"')
				j=j+1
				writeString();
			
			else:
				writeString();
				
#outofloop
outString2=closeBrace+'\n'+closeBracket2
print(i+j)
written.write(outString2)
written.close()