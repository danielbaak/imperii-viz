__author__ = 'fritz'
import csv
from location.models import Location
import sys

def parse_geonames_cities(file_path):
    csv.field_size_limit(sys.maxsize)
    with open(file_path, newline='', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t', quoting=csv.QUOTE_NONE)
        csv_reader.__next__()
        categories = []
        # because rakuten does not sort its category list we read it in, remove the empty strings from a row
        # and then sort it after row length to read parent categories first and their child after so we can
        # build the relationships
        for row in csv_reader:
            try:
                l = Location(name=row[1], latitude=row[4], longitude=row[5])
                l.save()
            except Exception:
                print(row)