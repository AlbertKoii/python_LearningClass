import json
print ('測驗11')


# json1 = {
#   "firstName": "Jane",
#   "lastName": "Doe",
#   "hobbies": ["running", "singing"],
#   "age": 35,
#   "children": [ 
#       {
#         "firstName": "Alice",
#         "toy": "Teddy bear",
#         "age": 6
#       },

#       {
#         "firstName": "Bob",
#         "toy": "Megatron",
#         "age": 8
#       }
#   ],
# }

# checkLit = [
#     "firstName",
#     "lastName",
#     "hobbies",
#     "age",
# ]



# def deep_search(data, target_key):
#     # 情況 1：如果目前的資料是字典
#     if isinstance(data, dict):
#         for key, value in data.items():
#             if key == target_key:
#                 print(f"找到標籤 [{key}]，內容是: {value}")
#             # 【關鍵】不管有沒有找到，都把 Value 丟回去再查一次（萬一裡面還有字典或清單）
#             deep_search(value, target_key)
            
#     # 情況 2：如果目前的資料是清單 (像你的 children)
#     elif isinstance(data, list):
#         for item in data:
#             # 【關鍵】把清單裡的每個東西拿出來，再丟回去查
#             deep_search(item, target_key)

# # 執行看看
# deep_search(json1, "age")




# erercise 2 of json file
json2 = [
    {
        "firstName": "Jane",
        "lastName": "Doe",
        "hobbies": ["running", "singing"],
        "age": 35,
        "children": [
            {
                "firstName": "Alice",
                "toy": "Teddy bear",
                "age": 6
            },

            {
                "firstName": "Bob",
                "toy": "Megatron",
                "age": 8
            }
        ],   
    },

    {
        "firstName": "Edward",
        "lastName": "Stark",
        "hobbies": ["running", "singing"],
        "age": 25,
        "children": [
            {
                "firstName": "Jon Snow",
                "toy": "car",
                "age": 15
            },

            {
                "firstName": "Rob Stark",
                "toy": "Optimus Prime",
                "age": 20
            },

            {
                "firstName": "Arya Stark",
                "toy": "Needle",
                "age": 12
            },

            {
                "firstName": "Sansa Stark",
                "toy": "Flowers",
                "age": 15
            }
        ],   
    },


    {
        "firstName": "Stephen",
        "lastName": "Maximo",
        "hobbies": ["running", "singing"],
        "age": 28,
        "children": [
            {
                "firstName": "James",
                "toy": "Shark",
                "age": 10
            },

            {
                "firstName": "Jessica",
                "toy": "water gun",
                "age": 7
            },
            
            {
                "firstName": "Amy",
                "toy": "T-rex",
                "age": 5
            }
        ],   
    },
]



def checkInner(): 
    for dataJson2 in json2: 
        family_kids = [] 

        parent_name = f"{dataJson2['firstName']} {dataJson2['lastName']}"
        print(f"\n--- 正在處理家長：{parent_name} ---") 
        childList = dataJson2["children"]

        for child in childList:
            kid_info = {
                "name": child["firstName"],
                "age": child["age"],
                "toy": child["toy"]
            }
            family_kids.append(kid_info)

        print(f"{parent_name} 共有 {len(family_kids)} 個小朋友：")
        
        for kid in family_kids:
            print(f"  - 名字: {kid['name']}, 年齡: {kid['age']}, 玩具: {kid['toy']}")

checkInner()

