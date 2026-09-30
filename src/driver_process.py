# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:50:43 2026

@author: rmili
"""

from input_data.parameters import MAPPING_FILE, SHEETS, OUTPUT_FILE,SUBMISSION_EXCEL_FILE, XML_OUTPUT_FILE, XSD_FILE
from src.create_excel_xml_mapping import extract_mapping
from src.read_submission_excel import extract_values
from src.create_xml import create_xml
from src.validate_xml import validate_xml
import json
from openpyxl import load_workbook 



# 1) first step: create mapping based on MAS provided Excel templates and mapping files

extract_mapping(
    input_file=MAPPING_FILE,
    sheet_names=SHEETS,
    output_file=OUTPUT_FILE
)

#2) extract values from Exel submission files and output to a list of dictionaries that contains sheet name, cell name, metric name, value etc
records = extract_values(SUBMISSION_EXCEL_FILE,OUTPUT_FILE )

#3) convert the list of dictionaries from the previous step to XML file
create_xml(records,XML_OUTPUT_FILE )

#4) validate XML output file
validate_xml(
    XML_OUTPUT_FILE,
    XSD_FILE
)