import json
import pprint
import csv

with open('probes-per-country-per-date.json', 'r') as handle:
    parsed = json.load(handle)

pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(parsed)

max = 0

for i in parsed:
#	print i,len(parsed[i])
	if max < len(parsed[i]):
		max = len(parsed[i])
		max_date = i
#print "max is", max, "for day ", max_date

#country_array = "["
#for key in sorted(parsed[max_date]):
#    country_array = country_array + key + ","
#country_array = country_array + "]"
#print country_array

#for key, value in parsed[max_date].iteritems() :
#    print key, value

country_array = ["AD","AE","AL","AM","AO","AQ","AR","AT","AU","AX","AZ","BA","BD","BE","BF","BG","BH","BI","BJ","BL","BR","BT","BW","BY","CA","CG","CH","CI","CL","CM","CN","CO","CR","CU","CW","CY","CZ","DE","DJ","DK","DO","DZ","EC","EE","ES","ET","FI","FO","FR","GA","GB","GD","GE","GF","GG","GH","GI","GM","GP","GQ","GR","GT","GU","HK","HN","HR","HU","ID","IE","IL","IM","IN","IQ","IR","IS","IT","JE","JM","JO","JP","KE","KG","KN","KR","KW","KY","KZ","LA","LB","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","MN","MQ","MT","MU","MV","MW","MX","MY","MZ","NA","NC","NE","NG","NI","NL","NO","NP","NZ","PE","PG","PH","PK","PL","PR","PT","PY","QA","RE","RO","RS","RU","RW","SA","SC","SD","SE","SG","SI","SJ","SK","SM","SN","SS","SV","SZ","TG","TH","TJ","TM","TN","TO","TR","TT","TW","TZ","UA","UG","US","UY","VE","VN","VU","WS","ZA","ZM","ZW"]

def keyCheck(key, arr, default):
    if key in arr.keys():
        return arr[key]
    else:
        return default

#data = "["
#for i in sorted(parsed):
##	data = data + i + ","
#	rowdata = "["
#	country_sum = 0
#	country_count = 0
#	for country in country_array:
#		country_count = keyCheck(country,parsed[i],0)
#		country_sum = country_sum + country_count
#		if country is "ZW":
#			rowdata = rowdata + str(country_count)
#		else:
#			rowdata = rowdata + str(country_count) + "," 
#		#print country, keyCheck(country,parsed[i],0)
#	rowdata = rowdata + "],\n"
#	if country_sum < 500:
#		rowdata = ""
#	data = data + rowdata
#data = data + "]"
#
#print data
#

#Read country/continent CSV and make map 

ccmap = {}

with open('country_continent.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for rows in reader:
        k = rows[0]
        v = rows[1]
        ccmap[k] = v

#pp.pprint(ccmap) 


data = "["
for i in sorted(parsed):
#	data = data + i + ","
        continent_count = {'EU':0, 'AS':0, 'NA':0, 'OC':0, 'AF':0, 'SA':0, 'AN':0}
	rowdata = "["
	country_sum = 0
	country_count = 0
	for country in country_array:
		country_count = keyCheck(country,parsed[i],0)
		country_sum = country_sum + country_count
		continent_count[ccmap[country]] += country_count
	for continent in sorted(continent_count):
		if continent is "SA":
			rowdata = rowdata + str(continent_count[continent])
		else:
			rowdata = rowdata + str(continent_count[continent]) + "," 
		#
	rowdata = rowdata + "],\n"
	if country_sum < 500:
		rowdata = ""
	data = data + rowdata
data = data + "]"

print data
