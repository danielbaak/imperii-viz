__author__ = 'fritz'
import os
import xml.etree.ElementTree as ET
import time,datetime
from location.models import Location
from person.models import Person
from .models import RegesteUniMainz, Regeste, Department, Issue, Volume
from .tasks import data_mining_regeste
from django.db import IntegrityError


def parse_folder(path):
    for root, dirpath, files in os.walk(path, ):
        for file in files:
            parse_xml(os.path.join(root, file))

#ElementTree
def parse_xml(xml_file_path):
    try:
        loc = None
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        title = root.find(".//title").text
        issue = root.find(".//idno[@n='issue']").text
        volume = root.find(".//idno[@n='volume']").text
        department = root.find(".//idno[@n='department']").text
        place_of_issue = root.find(".//placeName").text
        location = root.find(".//geo")
        if location is not None:
            location = location.text
            lat, long = location.split(",")
            try:
                loc, created = Location.objects.get_or_create(latitude=float(lat), longitude=float(long[1:]), name=str(place_of_issue))
            except IntegrityError:
                loc = Location.objects.filter(latitude=lat, longitude=long[1:], name=place_of_issue).first()
        issuer = root.find(".//persName").text
        issue_date = root.find(".//issueDate")[0]
        abstract = root.find(".//abstract")
        analysis = root.find(".//diplomaticAnalysis")
        if abstract is not None:
            abstract = get_xml_child_content(abstract)

        if analysis is not None:
            analysis = get_xml_child_content(analysis)

        addenda = root.find(".//addenda")
        if addenda is not None:
            addenda = get_xml_child_content(addenda)
        uri = root.find(".//idno[@n='uri']").text
        exchange = root.find(".//idno[@n='exchange']").text

        dep, created = Department.objects.get_or_create(department_id=int(department))
        vol, created = Volume.objects.get_or_create(volume_id=int(volume), department=dep)
        try:
            iss, created = Issue.objects.get_or_create(issue_id=int(issue), volume=vol)
        except IntegrityError:
            iss = Issue.objects.filter(issue_id=int(issue), volume=vol).first()
        try:
            person, created = Person.objects.get_or_create(name=str(issuer))
        except IntegrityError:
            person = Person.objects.filter(name=str(issuer)).first()
        try:
            mainz, created = RegesteUniMainz.objects.get_or_create(uri=uri, exchange=exchange)
            date = None
            if issue_date is not None and issue_date.get("value"):
                date = date_to_posix_timestamp(issue_date.get("value"))
            r, created = Regeste.objects.get_or_create(title=title,
                                              issue=iss,
                                              place_of_issue=loc,
                                              issuer=person,
                                              issue_date=date,
                                              abstract=abstract,
                                              analysis=analysis,
                                              addenda=addenda,
                                              uni_mainz=mainz)

            data_mining_regeste.delay(r)
        except IntegrityError:
            pass


    except ET.ParseError:
        pass
    except AttributeError:
        pass


def get_xml_child_content(node):
    if len(list(node)) == 0:
        if node.text is not None:
            return node.text
        else:
            return ""
    else:
        out = ""
        for child in list(node):
            out += get_xml_child_content(child)
    return out


def date_to_posix_timestamp(string):
    try:
        string = string.replace("-00", "-01")
        return int(time.mktime(datetime.datetime.strptime(string, "%Y-%m-%d").timetuple()))
    except ValueError:
        print(string)
        return None
