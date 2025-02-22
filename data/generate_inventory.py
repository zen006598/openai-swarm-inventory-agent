from tinydb import TinyDB
import random

db = TinyDB('inventory_db.json')

if len(db) == 0:

    names = ["T恤", "牛仔褲", "夾克", "毛衣", "短褲", "襯衫", "連衣裙", "運動褲", "外套", "背心"]
    sizes = ["S", "M", "L", "XL"]
    colors = ["紅色", "藍色", "黑色", "綠色", "黃色", "白色", "灰色", "紫色", "橙色", "粉色"]

    clothes = []
    for i in range(1, 101):
        item = {
            "id": i,
            "name": random.choice(names),
            "size": random.choice(sizes),
            "color": random.choice(colors),
            "quantity": random.randint(10, 100)
        }
        clothes.append(item)

    db.insert_multiple(clothes)
    print("模擬資料已成功插入 inventory_db.json")

