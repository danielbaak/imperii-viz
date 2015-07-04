__author__ = 'fritz'
import csv
from person.models import Person


def read_fredrick_text_file():
    with open("testdaten.txt", newline='', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t', quoting=csv.QUOTE_NONE)
        csv_reader.__next__()
        categories = []
        # because rakuten does not sort its category list we read it in, remove the empty strings from a row
        # and then sort it after row length to read parent categories first and their child after so we can
        # build the relationships
        for row in csv_reader:
            p = Person.objects.get(id=row[0])
            p.image_url = row[1]
            p.summary = row[2]
            p.save()
