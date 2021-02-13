import xml.etree.ElementTree as ET
import writer_list as wl
import math

def processData(filepath):

	tree = ET.parse(filepath)
	root = tree.getroot()
	general = root.find('General')
	form = general.find('Form')
	writerId = form.get('writerID')
	writerGender = wl.WRITER_LIST[writerId]
	strokeSet = root.find('StrokeSet')
	strokeList = strokeSet.findall('Stroke')
	numberOfStrokes = len(strokeList)
	totalAngleDeviation = 0
	totalTime = 0

	for stroke in strokeList:

		startTime = float(stroke.get('start_time'))
		endTime = float(stroke.get('end_time'))
		time = round((endTime-startTime),2)
		coordList = []
		pointsList = stroke.findall('Point')

		totalTime = totalTime + time

		for point in pointsList:
			xCoord = int(point.get('x'))
			yCoord = int(point.get('y'))
			coordList.append([xCoord,yCoord])

		if(len(coordList)>2):
			deviationPerStroke = processAverageDeviation(coordList)
			totalAngleDeviation = totalAngleDeviation + deviationPerStroke

	avgDeviation = totalAngleDeviation/numberOfStrokes
	avgTime = totalTime/numberOfStrokes

	return avgDeviation,avgTime,writerGender


def processAverageDeviation(pointsList):
	angleList = []
	for n in range(2,(len(pointsList))):
		# print(str(x1)+" "+str(x2)+" "+str(x3)+" "+str(y1)+" "+str(y2)+" "+str(y3))
		angle = getAngle(pointsList[n-2],pointsList[n-1],pointsList[n])
		angleList.append(angle)
	numberOfAngles = len(angleList)
	avgAngle = float(sum(angleList)/numberOfAngles)
	strokeDeviation = 0
	for angle in angleList:
		strokeDeviation = strokeDeviation + abs(avgAngle-angle)
	avgstrokeDeviation = strokeDeviation/numberOfAngles
	# print(avgDeviation)

	return avgstrokeDeviation
	


def getAngle(a, b, c):
    angle = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return angle + 360 if angle < 0 else angle