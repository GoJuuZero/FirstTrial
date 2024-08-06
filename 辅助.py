import json
import os


def document_read(path):
    if not os.path.exists(path):
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return {}
    return data


def document_write(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def add_entry_to_list(path, list_name, entry):
    data = document_read(path)
    if list_name in data:
        data[list_name].append(entry)
    else:
        data[list_name] = [entry]
    document_write(path, data)


def fz(i, path):
    data = document_read("fz.json")
    if path in data and int(i) < len(data[path]):
        return data[path][int(i)]
    else:
        return None


for i in range(5):
    bata = {
        fz(str(i), fz(str(i), "zj2")): {
            "0": fz(str(i), "l1"),
            "1": fz(str(i), "l2"),
            "2": fz(str(i), "l3"),
        },
        "解析": fz(str(i), "xj"),
        "城市":fz(str(i), fz(str(i), "zj2"))

    }
    add_entry_to_list('地铁题库.json', i, bata)

# 检查新条目是否已成功添加
print(json.dumps(document_read('fz.json'), ensure_ascii=False, indent=4))
