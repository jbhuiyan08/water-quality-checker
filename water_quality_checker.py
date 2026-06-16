"""
Water Quality Checker
A small Python tool that reads groundwater quality readings from a CSV file,
organizes them by parameter using a dictionary, and checks each reading
against Bangladesh's ECR-2023 drinking water standards.

Built while practicing the concepts from the "Python Data Structures"
course (University of Michigan): dictionaries, file reading and writing,
and tuples for sorting and multi-step tasks.
"""

import csv

# ECR-2023 drinking water standards (Bangladesh).
# pH is handled separately below since it's a range, not a single limit.
ECR_STANDARDS = {
    "TDS": 1000,
    "Manganese": 0.4,
    "Turbidity": 5,
    "EC": 1000,
    "Chloride": 250,
    "Iron": 1,
    "Total_Hardness": 500,
    "Total_Alkalinity": 500,
    "Sulphate": 250,
}

PH_RANGE = (6.5, 8.5)


def load_data(filename):
    """Read the CSV file and group readings into a dictionary keyed by
    parameter name. Each value is a list of (sample_id, location, value)
    tuples."""
    data = {}
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            param = row["Parameter"]
            value = float(row["Value"])
            entry = (row["Sample_ID"], row["Location"], value)
            data.setdefault(param, []).append(entry)
    return data


def analyze_parameter(param, readings):
    """Sort readings by value and flag anything outside the ECR-2023 limit."""
    sorted_readings = sorted(readings, key=lambda r: r[2], reverse=True)
    values = [r[2] for r in readings]
    average = sum(values) / len(values)

    if param == "pH":
        low, high = PH_RANGE
        flagged = [r for r in readings if r[2] < low or r[2] > high]
        limit_text = f"{low}-{high}"
    else:
        limit = ECR_STANDARDS.get(param)
        flagged = [r for r in readings if limit and r[2] > limit]
        limit_text = limit if limit else "not defined"

    return {
        "average": average,
        "highest": sorted_readings[0],
        "lowest": sorted_readings[-1],
        "limit": limit_text,
        "flagged": flagged,
    }


def write_report(results, output_file):
    """Write a plain text summary report to a new file."""
    with open(output_file, "w") as f:
        f.write("Water Quality Summary Report\n")
        f.write("Reference standard: ECR-2023 (Bangladesh)\n\n")

        for param, info in results.items():
            f.write(f"{param}\n")
            f.write(f"  Average: {info['average']:.2f}\n")
            f.write(
                f"  Highest: {info['highest'][2]} at {info['highest'][1]} "
                f"(Sample {info['highest'][0]})\n"
            )
            f.write(
                f"  Lowest: {info['lowest'][2]} at {info['lowest'][1]} "
                f"(Sample {info['lowest'][0]})\n"
            )
            f.write(f"  ECR-2023 limit: {info['limit']}\n")

            if info["flagged"]:
                f.write(f"  Outside limit in {len(info['flagged'])} sample(s):\n")
                for sample_id, location, value in info["flagged"]:
                    f.write(f"    - {location} (Sample {sample_id}): {value}\n")
            else:
                f.write("  All samples within limit\n")
            f.write("\n")


def main():
    data = load_data("sample_data.csv")
    results = {param: analyze_parameter(param, readings) for param, readings in data.items()}
    write_report(results, "report.txt")
    print("Done. Check report.txt for the summary.")


if __name__ == "__main__":
    main()
