# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:55:58 2026

@author: rmili
"""

"""this module find all parent nodes of B1 (which according to the first round of check, has a incorrect chain of parents)
"""



from lxml import etree

from input_data.parameters import XSD_FILE

# Deal with the cp1252 encoding issue
with open(XSD_FILE, "r", encoding="cp1252") as f:
    xsd_text = f.read()

root = etree.fromstring(xsd_text.encode("utf-8"))

NS = {"xs": "http://www.w3.org/2001/XMLSchema"}

# Find B1 element
b1 = root.xpath('.//xs:element[@name="B1"]', namespaces=NS)[0]

# Walk upwards
current = b1

while current is not None:

    if current.tag.endswith("element"):
        print(current.get("name"))

    current = current.getparent()