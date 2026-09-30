# MAS 610 XML Reporting

Python solution for generating a schema-valid XML submission from MAS 610 Excel reporting templates, covering:

- Appendix B1 – Statement of Financial Position: Assets
- Appendix B2 – Statement of Financial Position: Liabilities and Equity

## Approach

The solution implements the following processing pipeline:

```text
MAS XML–Excel Mapping
        ↓
Extract mapping metadata
        ↓
mapping.json
        ↓
Read values from MAS Excel submission template
        ↓
Structured Python records
        ↓
Generate MAS-compliant XML
        ↓
Validate generated XML against MAS XSD
```

The design separates the mapping, value extraction, XML generation and schema validation into individual processing stages.

This allows the Excel-to-XML mapping to remain data-driven while keeping the MAS XML structure and validation logic separate.

## Mapping Structure

The MAS XML–Excel mapping is first converted into a structured JSON representation.

Each mapped reporting item is represented internally in a structure similar to:

```python
{
    "sheet": "B1(1)",
    "cell": "C8",
    "metric": "B1_Amount",
    "datatype": "...",
    "dimensions": {
        "Bk_Sfp_Assets": "CashBalances"
    },
    "value": 1000
}
```

The mapping captures:

- Source worksheet
- Source cell
- MAS metric
- Datatype
- MAS dimension
- Dimension member
- Reported value

This separates Excel cell locations from the XML-generation logic.

## XML Generation

The XML hierarchy is constructed according to the MAS 610 XML Schema Definition (XSD).

For Appendix B1, each mapped asset amount and dimension combination is converted into the corresponding B1 repeat-group structure.

For Appendix B2, each mapped liability/equity amount and dimension combination is converted into the corresponding B2 repeat-group structure.

The MAS XML hierarchy is explicitly modelled in the XML generator, while the reporting values and dimensions are populated dynamically from the extracted mapping records.

## Validation

The generated XML is validated against the MAS XSD using `lxml.etree.XMLSchema`.

The validation step checks, among other schema constraints:

- XML hierarchy and element placement
- Required attributes
- Datatypes
- Permitted dimension values/enumerations
- Numeric value constraints

Validation errors are reported with their XML line number and the corresponding schema-validation message.

XML generation and validation are kept as separate processing stages so that generation logic and validation controls remain independently testable.

## Assumptions

- The supplied MAS Excel reporting template corresponds to the supplied XML–Excel mapping.
- The implementation scope is limited to Appendix B1 and Appendix B2.
- The MAS XSD is treated as the authoritative definition of the required XML structure and schema constraints.
- Blank source values are omitted where the XSD permits the corresponding XML element to be optional.
- Input Excel files retain the expected worksheet names and cell structure.
- Source files are placed in the expected `input_data` directory.

## Project Structure

```text
MAS-610-XML-Reporting/
│
├── input_data/
│   ├── parameters.py
│   └── MAS source files
│
├── output/
│   ├── mapping.json
│   └── generated XML
│
├── src/
│   ├── driver_process.py
│   ├── create_excel_xml_mapping.py
│   ├── extract_values.py
│   ├── create_xml.py
│   └── validate_xml.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Repository

The project is hosted in the public GitHub repository:

`Hillary-cpp/MAS-610-XML-Reporting`

Because the repository is public, no special repository access is required to clone it.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Hillary-cpp/MAS-610-XML-Reporting.git
cd MAS-610-XML-Reporting
```

### 2. Create a virtual environment

On Windows:

```bash
py -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

The virtual environment itself is not stored in the repository and should be recreated locally using the steps above.

## Running the Process

Run the driver from the project root:

```bash
python -m src.driver_process
```

The driver orchestrates the end-to-end process:

```text
Mapping extraction
      ↓
Value extraction
      ↓
XML generation
      ↓
XSD validation
```

Generated artifacts are written to the `output` directory.

## Output


The process generates:

- `mapping.json` – structured Excel-to-MAS mapping generated from the MAS mapping workbook.
- `output_xml_file.xml` – generated MAS 610 XML submission covering B1 and B2.

The generated XML is subsequently validated against the MAS XSD. The validation status and any schema validation errors are displayed in the console.

A successful validation confirms that the generated XML conforms to the supplied MAS XML schema for the implemented scope.