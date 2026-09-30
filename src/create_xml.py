# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 17:29:26 2026

@author: rmili
"""

from lxml import etree


def add_item(parent, name, value):
    """
    Add a populated MAS item element to an XML parent.

    No element is created when the supplied value is None.

    Parameters
    ----------
    parent : lxml.etree._Element
        Parent XML element.

    name : str
        MAS XML element name.

    value : object
        Value to write to the nested <value> element.
    """

    if value is None:
        return

    item = etree.SubElement(
        parent,
        name
    )
    item.set("type", "item")

    value_element = etree.SubElement(
        item,
        "value"
    )

    value_element.text = str(value)


def create_xml(records, output_file):
    """
    Generate an MAS 610 XML submission for Appendices B1 and B2.

    Parameters
    ----------
    records : list[dict]
        Structured reporting records produced by extract_values().
        Each record contains its source sheet, metric, dimensions and value.

    output_file : str
        Destination path for the generated XML file.

    Notes
    -----
    The XML hierarchy is explicitly modelled from the MAS XSD. B1 and B2
    records are separated using their source worksheet and represented
    through their corresponding MAS repeat-group structures.
    """

    # =========================================================
    # ROOT
    # =========================================================

    root = etree.Element(
        "BU_MS610",
        type="schema",
        guid="d041ac61-ff6b-43f1-981f-5dc1b671b545",
        versionNumber="4"
    )

    submission = etree.SubElement(
        root,
        "BU_MS610"
    )
    submission.set("type", "group")

    # Build the A1 hierarchy required by the MAS XSD before B1/B2.
    # =========================================================
    # A1 STRUCTURE
    # =========================================================

    a1_outer = etree.SubElement(
        submission,
        "A1"
    )
    a1_outer.set("type", "group")

    a1_list = etree.SubElement(
        a1_outer,
        "A1"
    )
    a1_list.set("type", "list")

    a1_group = etree.SubElement(
        a1_list,
        "A1_x0020_Repeat_x0020_Group"
    )
    a1_group.set("type", "group")


    # =========================================================
    # ROUTE RECORDS TO B1 / B2
    # =========================================================
    
    # Route extracted records to the relevant MAS appendix based on
    # their source worksheet. 
    ''' 
    For every extracted record
        ↓
    check source sheet
        ↓
    B1 → B1 records
    B2 → B2 records
    '''

    b1_records = []
    b2_records = []
    
    for record in records:
       sheet = record["sheet"]
    
       if sheet.startswith("B1"):
            b1_records.append(record)
    
       elif sheet.startswith("B2"):
            b2_records.append(record)

    # =========================================================
    # B1 - ASSETS
    # =========================================================

    if b1_records:

        b1 = etree.SubElement(
            a1_group,
            "B1"
        )
        b1.set("type", "group")

        b1_list = etree.SubElement(
            b1,
            "BU_MS610_B1"
        )
        b1_list.set("type", "list")

        # Each mapped B1 record is represented as one B1 repeat group.
        for record in b1_records:

            group = etree.SubElement(
                b1_list,
                "BU_MS610_B1_x0020_Repeat_x0020_Group"
            )
            group.set("type", "group")

            # Amount
            if record["value"] is not None:
                add_item(
                    group,
                    "B1_Amount",
                    record["value"]
                )

            # Asset dimension
            asset = record["dimensions"].get(
                "Bk_Sfp_Assets"
            )

            add_item(
                group,
                "Bk_Sfp_Assets",
                asset
            )


    # =========================================================
    # B2 - LIABILITIES AND EQUITY
    # =========================================================

    if b2_records:

        b2 = etree.SubElement(
            a1_group,
            "B2"
        )
        b2.set("type", "group")

        b2_list = etree.SubElement(
            b2,
            "BU_MS610_B2"
        )
        b2_list.set("type", "list")
        
        # Each mapped B2 record is represented as one B2 repeat group.
        for record in b2_records:

            group = etree.SubElement(
                b2_list,
                "BU_MS610_B2_x0020_Repeat_x0020_Group"
            )
            group.set("type", "group")

            # Amount
            if record["value"] is not None:
                add_item(
                    group,
                    "B2_Amount",
                    record["value"]
                    )

            # Liability / equity dimension
            liability = record["dimensions"].get(
                "Bk_Sfp_Liabilities"
            )

            add_item(
                group,
                "Bk_Sfp_Liabilities",
                liability
            )


    # =========================================================
    # WRITE XML
    # =========================================================

    tree = etree.ElementTree(root)

    tree.write(
        output_file,
        pretty_print=True,
        xml_declaration=True,
        encoding="UTF-8"
    )