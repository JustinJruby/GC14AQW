import ephem

gatech = ephem.Observer()               
gatech.lon, gatech.lat = '45.54593', '-62.6034'
gatech.date = '2013/09/10 03:13:56' 
vega = ephem.star('Vega')
vega.compute(gatech)  
vega.az

gatech.date = '2013/09/10 03:23:56' 
kochab = ephem.star('Kochab') 
kochab.compute(gatech) 
kochab.az

gatech.date = '2013/09/10 03:33:56' 
altair = ephem.star('Altair')
altair.compute(gatech) 
altair.az

gatech.date = '2013/09/10 03:43:56' 
alde = ephem.star('Aldebaran')
alde.compute(gatech) 
alde.az

gatech.date = '2013/09/10 03:53:56' 
fom = ephem.star('Fomalhaut')
fom.compute(gatech) 
fom.az