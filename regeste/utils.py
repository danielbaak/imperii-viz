__author__ = 'fritz'
import os

def parse_folder(path):
    for root, subFolders, files in os.walk(path):
        for file in files:
            with open (file, "r") as xml_file:
                data=xml_file.readlines()
                print(data)

def parse_xml(xml_sting):
    root = ET.fromstring(xml_sting)