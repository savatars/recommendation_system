import csv
from mysite.models import features #Change App Name

with open('final_out.csv') as csvfile:   #Change file location
	reader=csv.DictReader(csvfile)
	for row in reader:
			p = features(customerId=row['customerId'],recommendedProducts=row['recommendedProducts'])
			p.save()
			
