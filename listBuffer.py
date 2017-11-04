

# create a function that takes a list as input and bufffers by that distance

def listBuffer(inputFile, listDistances, distUnit):
	if distUnit.lower() != 'feet' or distUnit.lower() != 'miles' or distUnit.lower() != 'meters' or distUnit.lower() != 'kilometers':
		print 'you need to go home and learn your measurement units'
		print 'please use:'
		print '    meters'
		print '    kilometers'
		print '    feet'
		print '    miles'


	for i in listDistances:
		bufferDist = str(i)+' '+distUnit
		outputFile = inputFile.replace('.shp', '_'+str(i)+'.shp')
		arcpy.Buffer_analysis(inputFile, outputFile, bufferDist)

		# buffer the distance

