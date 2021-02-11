import xml.etree.ElementTree as ET

tree = ET.parse('writer_info.xml')
root = tree.getroot()

dict1 = {}

for writer in root.findall('Writer'):
    writerId = writer.get('name')
    gender = writer.get('Gender')
    dict1[writerId] = gender

file1 = open('writerdata.txt','a')
file1.write(str(dict1))
file1.close()    