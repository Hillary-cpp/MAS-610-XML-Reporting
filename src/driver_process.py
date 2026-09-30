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


"""
Main driver for the MAS 610 Excel-to-XML conversion process.

The module orchestrates the end-to-end reporting workflow:

1. Extract MAS XML-to-Excel mapping metadata from the mapping workbook.
2. Read reporting values from the MAS Excel submission template.
3. Convert the extracted records into MAS 610 XML format.
4. Validate the generated XML against the official MAS XSD schema.

Configuration such as input/output file paths and worksheets is
maintained separately in input_data.parameters.
"""

## Step 1: Extract MAS mapping metadata from Excel cell comments.

extract_mapping(
    input_file=MAPPING_FILE,
    sheet_names=SHEETS,
    output_file=OUTPUT_FILE
)

# Step 2: Read submission values using the generated cell mapping.
records = extract_values(SUBMISSION_EXCEL_FILE,OUTPUT_FILE )

# Step 3: Generate the MAS 610 XML submission.
create_xml(records,XML_OUTPUT_FILE )

# Step 4: Validate the generated XML against the MAS XSD.
validate_xml(
    XML_OUTPUT_FILE,
    XSD_FILE
)