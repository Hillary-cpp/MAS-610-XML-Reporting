# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 17:02:20 2026

@author: rmili
"""


import json
from openpyxl import load_workbook


def extract_values(excel_file, mapping_file):
    """
    Extract reporting values from the MAS Excel submission workbook.

    Parameters
    ----------
    excel_file : str
        Path to the MAS Excel submission template containing report values.

    mapping_file : str
        Path to the JSON mapping generated from the MAS mapping workbook.

    Returns
    -------
    list[dict]
        Reporting records containing worksheet, cell, metric, datatype,
        dimensions and the corresponding Excel value.
    """
    
    # Load mapping
    with open(mapping_file, "r", encoding="utf-8") as f:
        mapping = json.load(f)

    # Load actual MAS submission Excel
    workbook = load_workbook(excel_file, data_only=True)

    results = []
    
    # Use each mapping entry to locate its corresponding value in the
    # submission workbook while preserving the associated MAS metadata.
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