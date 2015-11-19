#Copyright {2015} {Ramkumar Gopalkrishna}

#Load  3 digit abbreveations and Country names, use it for looks ups within text,
#Also reverse lookup the dictiorny so both the formats looks up give positive results


mydict = {}

for lines in open("data/abrcountry.txt"):
        fields = lines.split('\t')
        mydict[fields[2]]=fields[0].lower()

revdict = dict(map(reversed, mydict.iteritems()))

strtoget = list('IND,India,United Kingdom,Australia,AUS,Moved Boxes in'.split(','))

for value in  map(lambda x: mydict.get(x.upper(), revdict.get(x.lower(),x.lower() + ' : Not Found')),strtoget):
        print str(list(value)[0].upper())+str(''.join(list(value)[1:]))
