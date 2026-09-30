# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 17:02:20 2026

@author: rmili
"""


import json
from openpyxl import load_workbook


def extract_values(excel_file, mapping_file):

    # Load mapping
    with open(mapping_file, "r", encoding="utf-8") as f:
        mapping = json.load(f)

    # Load actual MAS submission Excel
    workbook = load_workbook(excel_file, data_only=True)

    results = []

    for item in mapping:

        sheet = item["sheet"]
        cell = item["cell"]

        value = workbook[sheet][cell].value

        results.append({
            "sheet": sheet,
            "cell": cell,
            "metric": item["metric"],
            "datatype": item["datatype"],
            "dimensions": item["dimensions"],
            "value": value
        })

    return results