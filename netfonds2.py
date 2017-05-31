#!/usr/bin/env python3

from urllib.request import urlopen
import time
import datetime
#import sys

#sys.setdefaultencoding("ISO-8859-1")

def pullData(stock):
    try:
        fileLine = stock+'.txt'
        urlToVisit = 'http://norma.netfonds.no/paperhistory.php?paper='+stock+'&csv_format=csv'
        sourceCode = urlopen(urlToVisit).read().decode("ISO-8859-1")
        splitSource = sourceCode.split('\n')

        for eachLine in splitSource:
            splitLine = eachLine.split(',')
            if len(splitLine)==9:
                if 'quote' not in eachLine:
                    saveFile = open(fileLine,'a')
                    lineToWrite = eachLine+'\n'
                    saveFile.write(lineToWrite)

        print('Pulled',stock)
        print('sleeping')
        time.sleep(1)

    except Exception as e:
        print('main loop',str(e))

pullData("TEL")
