# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:51:26 2026

@author: rmili
"""

"""
Central configuration for the MAS 610 Excel-to-XML process.

The input files are selected from the MAS Notice 610 reference materials
according to their role in the conversion process:

1. XML Schema–Excel Submission Template Mapping
   Used to identify the relationship between Excel cells and MAS XML
   metrics, datatypes and dimensions.

2. MAS 610/1003 Excel Submission Template
   Used as the source workbook from which the actual B1 and B2 reporting
   values are extracted.

3. MAS 610/1003 XML Schema (XSD)
   Used as the authoritative schema for validating the structure,
   datatypes and permitted values of the generated XML submission.

The assessment scope is limited to Appendix B1 and B2.
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