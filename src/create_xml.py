# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 17:29:26 2026

@author: rmili
"""

from lxml import etree


def add_item(parent, name, value):
    """
    Add an MAS item element.

    Example:
        <B1_Amount type="item">
            <value>1000</value>
        </B1_Amount>
    """

    item = etree.SubElement(parent, name)
    item.set("type", "item")

    value_element = etree.SubElement(item, "value")

    if value is not None:
        value_element.text = str(value)


def create_xml(records, output_file):
    """
    Create MAS 610 XML for Appendix B1 and B2.

    Parameters
    ----------
    records : list[dict]
        Records produced by extract_values().

    output_file : str
        Path of XML file to create.
    """

    # -------------------------------------------------
    # Root structure
    # -------------------------------------------------

    root = etree.Element("BU_MS610")

    submission = etree.SubElement(
        root,
        "BU_MS610"
    )

    # -------------------------------------------------
    # Split records into B1 and B2
    # -------------------------------------------------

    b1_records = [
        record
        for record in records
        if record["sheet"].startswith("B1")
    ]

    b2_records = [
        record
        for record in records
        if record["sheet"].startswith("B2")
    ]

    # -------------------------------------------------
    # B1 - Statement of Financial Position: Assets
    # -------------------------------------------------

    if b1_records:

        b1 = etree.SubElement(
            submission,
            "B1"
        )
        b1.set("type", "group")

        b1_list = etree.SubElement(
            b1,
            "BU_MS610_B1"
        )
        b1_list.set("type", "list")

        for record in b1_records:

            group = etree.SubElement(
                b1_list,
                "BU_MS610_B1_x0020_Repeat_x0020_Group"
            )
            group.set("type", "group")

            # Amount
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

    # -------------------------------------------------
    # B2 - Statement of Financial Position:
    #      Liabilities and Equity
    # -------------------------------------------------

    if b2_records:

        b2 = etree.SubElement(
            submission,
            "B2"
        )
        b2.set("type", "group")

        b2_list = etree.SubElement(
            b2,
            "BU_MS610_B2"
        )
        b2_list.set("type", "list")

        for record in b2_records:

            group = etree.SubElement(
                b2_list,
                "BU_MS610_B2_x0020_Repeat_x0020_Group"
            )
            group.set("type", "group")

            # Amount
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

    # -------------------------------------------------
    # Write XML
    # -------------------------------------------------

    tree = etree.ElementTree(root)

    tree.write(
        output_file,
        pretty_print=True,
        xml_declaration=True,
        encoding="UTF-8"
    )