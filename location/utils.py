__author__ = 'fritz'
from django.db import IntegrityError
import csv
from location.models import Location
import sys


def parse_geonames_cities(file_path):
    """Parse the geonames cities1000.txt and save each line as a location with the gps coordinates"""
    csv.field_size_limit(sys.maxsize)
    with open(file_path, newline='', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t', quoting=csv.QUOTE_NONE)
        csv_reader.__next__()
        for row in csv_reader:
            try:
                l = Location(name=row[1], latitude=row[4], longitude=row[5])
                l.save()
            except IntegrityError:
                print(row)