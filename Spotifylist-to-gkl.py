# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 16:23:00 2016

@author: zhang
"""

import csv
import re
import os
csvFile = '201606-09.csv'   #put your csv file name on here
xmlFile = 'myData.xml'

csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
# there must be only one top-level tag
xmlData.write('<csv_data>' + "\n")

rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else: 
        xmlData.write('<row>' + "\n")
        for i in range(len(tags)):
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('</row>' + "\n")
            
    rowNum +=1

xmlData.write('</csv_data>' + "\n")
xmlData.close()

fileHandle = open ( 'myData.xml' ) 
content=fileHandle.read() 
fileHandle.close()  
song = re.compile('<Track_Name>(.*?)</Track_Name>')
artist = re.compile(' <Artist_Name>(.*?)</Artist_Name>')
songs = song.findall(content)
artists=artist.findall(content)
ListName='Default list'   # put your list name
 
f=open('default.kgl','w')  #put your .kgl file name
#f.truncate()

f.writelines('<?xml version="1.0" encoding="windows-1252"?>'+'\n'+'<List ListName="'+ListName+'">'+'\n')

for i in range(len(songs)):
    f=open('default.kgl','a')   # put your .kgl file name
    f.writelines('<File>')
    f.writelines('<FileName> ')
    f.writelines(artists[i]+'-'+songs[i]+'</FileName>')
    f.writelines('</File>')
    f.writelines('\n')
    f.close

f.close
os.remove('myData.xml')   # 最后将作为中间文件的myData.xml 文件删除掉。 delete myData.xml 
print 'succeed'           #目前存在的问题，最后一首歌总是不能够导入到.kgl文件之中，这在原来的版本中没有发生。
		
		


