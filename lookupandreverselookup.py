#Copyright {2015} {Ramkumar Gopalkrishna}

#Load  3 digit abbreveations and Country names, use it for looks ups within text,
#Also reverse lookup the dictiorny so both the formats looks up give positive results

#Data used from http://www.worldatlas.com/aatlas/ctycodes.htm

myDict = {}

for lines in open("data/abrcountry.txt"):
        fields = lines.split('\t')
        myDict[fields[2]]=fields[0].lower()

revDict = dict(map(reversed, myDict.iteritems()))

strToGet = list('IND,India,United Kingdom,Australia,AUS,Moved Boxes in'.split(','))

for value in  map(lambda x: myDict.get(x.upper(), revDict.get(x.lower(),x.lower() + ' : Not Found')),strToGet):
        print str(list(value)[0].upper())+str(''.join(list(value)[1:]))
        

#End-of-File
