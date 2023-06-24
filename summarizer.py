import json

with open('json/item_catalogue.json', 'r') as fin, \
     open('csv/items.csv', 'w') as fout:

    item_catelogue = json.load(fin)
    fout.write("Item ID,Item Name\n")
    for item in item_catelogue["Items"] :
        itemid = item["ItemId"]["$numberInt"] if "ItemId" in item else "0"
        itemname = item["Name"]
        fout.write(f"{itemid},{itemname}\n")
