#https://github.com/ideoforms/python-twitter-examples/blob/master/twitter-search-geo.py
#https://stackoverflow.com/questions/41859308/tweepy-twitter-api-rate-limit-exceeded?rq=1
import tweepy

import sys
import csv

# create API object
auth = tweepy.auth.OAuthHandler("ygvQwLaaLaozqyAw5X4oPQa2g", "f4JjDLicqf6uLhoqxAKNni72FHCCN9Uh0QBo2FiibhbhF1Iqsm")
auth.set_access_token("3026160142-ylCI7PAYDXZqOdYBlvLwLTn2kMzqAChA5ONSGOt", "tpEqPhNoDf4RQcb4Uqq1b8s17iwYs3ZF9muagD3SwqqBO")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def getLocations(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        records = list(reader)
        locationData = []
        i = 0
        for record in records:
            Location = eval(record[5])
            locationData.append(Location)
            i += 1
        return locationData

def getTweets(locationData):
    max_range = 1 #search range in kilometres
    min_results = 1
    row = ["user", "id", "text", "created_at"]

    i = 0
    for location in locationData:
        latitude = location[0]
        longitude = location[1]

        outfile = "location" + str(i) + ".csv"
        csvfile = open(outfile, "w")
        csvWriter = csv.writer(csvfile, lineterminator='\n')
        #csvWriter.writerow(row)

        if i == 12:
            csvfile.close()

        else:
            result_count = 0
            last_id = None

            while result_count < min_results:
                for result in tweepy.Cursor(api.search, q = "", geocode = "%s,%s,%dkm" % (latitude, longitude, max_range)).items(50):
                    user = result.user.screen_name
                    ID = result.user.id
                    text = result.text.encode('ascii', 'replace')
                    created = result.created_at

                    row = [user, ID, text, created]
                    csvWriter.writerow(row)
                    result_count += 1
            csvfile.close()
        i += 1


getTweets(getLocations('licenses.csv'))
