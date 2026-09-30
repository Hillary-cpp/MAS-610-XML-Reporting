# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:28:49 2026

@author: rmili
"""

from lxml import etree




def validate_xml(xml_file, xsd_file):
    """
    Validate an XML submission against the MAS 610 XSD.

    Parameters
    ----------
    xml_file : str
        Path to the generated MAS XML submission.

    xsd_file : str
        Path to the MAS XSD schema file.

    Returns
    -------
    bool
        True when the XML conforms to the XSD; otherwise False.

    Notes
    -----
    Validation failures are printed from the lxml schema error log,
    including the XML line number and validation message.
    """

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