# Risk Assessment Report Generator

## Author
Andrew Zeidler

## Description
This project analyzes scenario-based data to assess risk levels using rule-based decision logic. The script processes structured inputs from a CSV file or user-provided inputs, calculates a risk score based on multiple environmental and operational factors, and classifies each scenario as LOW, MODERATE, or HIGH risk.

The tool is designed to demonstrate how structured data can be combined with decision logic to support risk-based assessments.

## Features
- Reads and processes structured CSV data
- Calculates risk scores using conditional logic
- Classifies scenarios into LOW, MODERATE, or HIGH risk
- Writes a formatted risk assessment report to a text file
- Allows users to assess an individual scenario through interactive input
- Supports optional report generation based on user selection

## Purpose
This project was developed to demonstrate foundational programming and analytical skills, including:
- Data ingestion from CSV files
- Data cleaning and preprocessing
- Use of dictionaries and lists for structured data storage
- Conditional logic for decision-making
- Aggregation and summary of results
- File output generation
- Interactive user input handling

The project models how multiple variables can be combined to inform decision-making under uncertain or complex conditions.

## Files
- `risk_analyzer.py` — main Python script
- `risk_data.csv` — sample dataset
- `risk_report.txt` — generated report file (created after running the script)

## How to Run

1. Ensure the following files are in the same directory:
   - `risk_analyzer.py`
   - `risk_data.csv`

2. Open a terminal in that directory

3. Run the script:

```bash
python risk_analyzer.py