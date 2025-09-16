import csv
import json

data = []

with open("source.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        entry = {
            "Number": row.get("Number", ""),
            "Company": row.get("Company", ""),
            "Country": row.get("Country", ""),
            "Revenue_nominal": row.get("Revenue_nominal", ""),
            "Revenue_abbrev": row.get("Revenue_abbrev", "")
        }
        data.append(entry)

with open("data.json", "w", encoding="utf-8") as jsonfile:
    json.dump(data, jsonfile, indent=2)

print("Processed source.csv into data.json.")