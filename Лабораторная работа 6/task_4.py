import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file, delimiter=",", new_line="\n") -> list[dict]:
    with open(file) as f:
        data_ = f.readlines()
        headers_ = data_[0].strip(new_line).split(delimiter)
        info_ = [item.strip(new_line).split(delimiter) for item in data_[1:]]
        dictlist_ = [dict(zip(headers_, item)) for item in info_]
        return dictlist_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
