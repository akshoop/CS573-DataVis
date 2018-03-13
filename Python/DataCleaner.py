import googlemaps, csv
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyAbiBckU53i8-1vedv-PQDouZOX-8fE2Ro')

def getLocation(address):
    # Geocoding an address
    geocode_result = gmaps.geocode(address)
    if(geocode_result != []):
        return(geocode_result[0]['geometry']['location']['lat'], geocode_result[0]['geometry']['location']['lng'])
    else:
        return (0, 0)

def getAddr(record):
    addr = record[16].strip(' ')
    if len(addr) > 0:
        addr += ' '
    addr += record[18].strip(' ') + ', ' + record[19].strip(' ') + " " + record[20].strip(' ')
    return addr

def newRecord(BusinessName, ClosingTime, Capacity, Phone, Address, Location, LocationComment):
    return {'BusinessName': BusinessName, 'ClosingTime': ClosingTime,
            'Capacity': Capacity, 'Phone': Phone, 'Address': Address,
            'Location': Location, 'LocationComment': LocationComment }

def writeRecordsToCSV(records, filename):
    with open(filename, 'w') as csvfile:
        fieldnames = ['BusinessName', 'ClosingTime', 'Capacity', 'Phone', 'Address', 'Location', 'LocationComment']
        writer = csv.DictWriter(csvfile, lineterminator='\n', fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(record)

def getRecords(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        records = list(reader)
        newRecords = []
        i = 1
        for record in records:
            BusinessName = record[14]
            ClosingTime = record[11]
            Capacity = record[13]
            Phone = record[15]
            Address = getAddr(record)
            Location = getLocation(Address)
            LocationComment = record[4]
            newRecords.append(newRecord(BusinessName, ClosingTime, Capacity, Phone, Address, Location, LocationComment))
            print("Processing: {0:55} {1:5}/{2:<5}".format(BusinessName, i, len(records)))
            i += 1
        return newRecords

#writeRecordsToCSV(getRecords('test.csv'), 'licenses.csv')
writeRecordsToCSV(getRecords('../CSV/liquor-licenses-orig.csv'), 'licenses.csv')

