import csv
from mysite.models import features #Change App Name

with open('event_small.csv') as csvfile:   #Change file location
	reader=csv.DictReader(csvfile)
	for row in reader:
			p = features(timestamp=row['timestamp'],
visitorid=row['visitorid'],event=row['event'],itemid=row['itemid'])
			p.save()
			
