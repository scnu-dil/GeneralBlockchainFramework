

from moduels.Tianwen import Tianwen

record = {
    "item_Element": "SDFSDFDSFSDF",
    "item_N_line": "item_N_line",
    "item_O_XH": "item_O_XH",
    "item_O_XFe": "item_O_XFe",
    "item_O_loge": "item_O_loge",
    "item_C_XH": "item_C_XH",
    "item_C_XFe": "item_C_XFe",
    "item_C_loge": "item_C_loge"
}

tianwen = Tianwen()

txhash = tianwen.set(record["item_Element"], record["item_N_line"], record["item_O_XH"], record["item_O_XFe"], record["item_O_loge"], record["item_C_XH"], record["item_C_XFe"], record["item_C_loge"])
if txhash is None:
    print("txhash is None")
    exit(0)

response = tianwen.get(record["item_Element"])
print ("txhash: ", txhash, "response: ", response)






