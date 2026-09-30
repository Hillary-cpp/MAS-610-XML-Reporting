# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:51:26 2026

@author: rmili
"""


INPUT_PATH ="input_data"
OUTPUT_PATH = "output"
MAPPING_FILE =  '/'.join([INPUT_PATH, "xml-schema-excel-submission-template-mapping-aug-2022.xlsx"])

SHEETS = [
    "B1(1)",
    "B2(1)"
]

OUTPUT_FILE = '/'.join([OUTPUT_PATH, "mapping.json"])

SUBMISSION_EXCEL_FILE = '/'.join([INPUT_PATH, "MAS 6101003  Excel Submission Template Version 32 Dec 2021.xlsx"])
XML_OUTPUT_FILE = '/'.join([OUTPUT_PATH, "output_xml_file.xml"])
XSD_FILE = "input_data/MAS 610_1003 - XML Schema Dec 2021 (Version 3.0).txt"