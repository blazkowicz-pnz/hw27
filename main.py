import json
import csv

import regex as regex
def converter(csv_file, json_file):
    res = []
    with open(csv_file, encoding="utf-8") as csvf:
        for row in csv.DictReader(csvf):
            if "Id" in row:
                row["pk"] = int(row["Id"])
                del (row["Id"])
            else:
                row["pk"] = int(row["id"])
                del (row["id"])


            if "is_published" in row:
                if row["is_published"] == "TRUE":
                    row["is_published"] = "true"
                else:
                    row["is_published"] = "false"
            res.append(row)



    with open(json_file, "w", encoding="utf-8") as jsf:
        jsf.write(json.dumps(res, ensure_ascii=False, ))
    return res


converter(csv_file="categories.csv", json_file="cat.json")