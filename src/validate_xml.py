# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:28:49 2026

@author: rmili
"""

from lxml import etree




def validate_xml(xml_file, xsd_file):

    # Read MAS XSD text using Windows encoding
    with open(xsd_file, "r", encoding="cp1252") as f:
        xsd_text = f.read()

    # Parse XSD
    xsd_doc = etree.fromstring(
        xsd_text.encode("utf-8")
    )

    schema = etree.XMLSchema(xsd_doc)

    # Parse generated XML
    xml_doc = etree.parse(xml_file)

    # Validate
    if schema.validate(xml_doc):
        print("XML is schema-valid.")
        return True

    print("XML validation failed:")

    for error in schema.error_log:
        print(
            f"Line {error.line}: {error.message}"
        )

    return False