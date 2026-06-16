# Water Quality Checker

A small Python script that reads groundwater quality readings from a CSV file and checks them against Bangladesh's ECR-2023 drinking water standards.

This was built while working through the **Python Data Structures** course (University of Michigan, Coursera) to apply what I learned about dictionaries, file reading and writing, and tuples in a real water resources context related to my work in environmental and water resources engineering.

## What it does

- Reads sample readings (TDS, pH, iron, chloride, turbidity) from `sample_data.csv`
- Groups the readings by parameter using a dictionary
- Sorts the readings for each parameter to find the highest and lowest values
- Flags any reading that falls outside the ECR-2023 limit
- Writes a plain text summary to `report.txt`

## How to run it

```
python3 water_quality_checker.py
```

This will read `sample_data.csv` and generate `report.txt` with the summary.

## Files

- `water_quality_checker.py` — main script
- `sample_data.csv` — sample groundwater data (modeled loosely on Gopalganj district data)
- `report.txt` — generated automatically when you run the script

## Notes

The data here is sample data for demonstration. The ECR-2023 limits used in the script (TDS, manganese, pH, turbidity, EC, chloride, iron, total hardness, total alkalinity, sulphate) match Bangladesh's official drinking water standards.
