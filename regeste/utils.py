__author__ = 'fritz'
import os
import xml.etree.ElementTree as ET
import time, datetime
from location.models import Location
from person.models import Person
from .models import RegesteUniMainz, Regeste, Department, Issue, Volume


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
            if len(Location.objects.filter(latitude=lat, longitude=long[1:])) == 0:
                loc = Location(latitude=lat, longitude=long[1:], name=place_of_issue).save()
            else:
                loc = Location.objects.filter(latitude=lat, longitude=long[1:])[0]
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

        if len(Department.objects.filter(department_id=department)) == 0:
            dep = Department(department_id=department)
            dep.save()
        else:
            dep = Department.objects.get(department_id=department)
        if len(Volume.objects.filter(volume_id=volume, department=dep)) == 0:
            vol = Volume(volume_id=volume, department=dep)
            vol.save()
        else:
            vol = Volume.objects.filter(volume_id=volume, department=dep)[0]
        if len(Issue.objects.filter(issue_id=issue, volume=vol)) == 0:
            iss = Issue(issue_id=issue, volume=vol)
            iss.save()
        else:
            iss = Issue.objects.filter(issue_id=issue, volume=vol)[0]
        if len(Person.objects.filter(name=issuer)) == 0:
            person = Person(name=issuer)
            person.save()
        else:
            person = Person.objects.filter(name=issuer)[0]

        mainz = RegesteUniMainz(uri=uri, exchange=exchange)
        mainz.save()
        date = None
        if issue_date is not None and issue_date.get("value"):
            date = date_to_posix_timestamp(issue_date.get("value"))
        Regeste(title=title,
                issue=iss,
                place_of_issue=loc,
                issuer=person,
                issue_date=date,
                abstract=abstract,
                analysis=analysis,
                addenda=addenda,
                uni_mainz=mainz).save()
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
