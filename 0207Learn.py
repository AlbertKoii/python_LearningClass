import requests
import urllib3
import json
# code runner 可以用於跑程式

urllib3.disable_warnings()
# print ("Hello my 0207 learning python class!")

# https://opendata.tycg.gov.tw/datalist/5ca2bfc7-9ace-4719-88ae-4034b9a5a55c
# https://opendata.tycg.gov.tw/api/v1/dataset.api_access?rid=08274d61-edbe-419d-8fcc-7a643831283d&format=json&limit=400

url = "https://opendata.tycg.gov.tw/api/v1/dataset.api_access?rid=08274d61-edbe-419d-8fcc-7a643831283d&format=json&limit=400"
response = requests.get(url, verify=False)
datas = response.json()
# print("datas" , datas)


def respCatch () :
    for data in datas:
        # 1. 抓出字串形式的 sbi_detail
        sbi_string = data.get("sbi_detail")
        
        if sbi_string:
            # 2. 關鍵：把字串解析成真正的字典
            qty = json.loads(sbi_string)
            
            # 3. 現在就可以正常取值了
            yb2 = qty.get("yb2")
            eyb = qty.get("eyb")

            yb2Transfer = type(yb2) == int()
            print ("yb2Transfer" , yb2Transfer)
            print(f"站點: {data.get('sna')}, yb2: {yb2}, eyb: {eyb}")
# respCatch()

def ubikedATA ():
    count = 0 
    dataArray = []
    
    for data in datas:
        if data["sareaen"] == "Zhongli Dist." :
            count += 1
            dataCheck = [] 
            area = data["sareaen"]
            ar = data["ar"]
            sbi = data["sbi"]
            bemp = data["bemp"]

            dataCheck = [area, ar, sbi, data["bemp"]]
            print (
f''' 
場站 : {ar},
地點: {area} ,
場站目前車輛數: {sbi}
空位數量 : {bemp}
'''
                )
            dataArray.append(dataCheck)
        
            if count >= 10 :
                print("--- 已達到 10 筆，停止抓取 ---")
                break
    print ("所有資料總和", dataArray)

# ubikedATA()
    

# 下面是目前位置 :
# mylocation : 24.95634695094952, 121.24195097379541
# upper location : 24.97254345891089, 121.24317907322221


# 緯度
lat = 24.95634695094952
# 經度
lng = 121.24195097379541



# 差異經度、緯度(lng , lat)
diff = 0.01

def trackgps ():
    print ("開始作業gps function ")
    
    # 抓到api 資訊
    response = requests.get(url , verify=False)
    datas = response.json()



    for data in datas:

        curr_lat = float(data['lat'])
        curr_lng = float(data['lng'])
        
        lat_max, lat_min = lat + diff, lat - diff
        lng_max, lng_min = lng + diff, lng - diff

        # print ("checklat_plus" , checklat_plus , "|   typeof " , type(checklat_plus) )
        # print ("checklat_minus" , checklat_minus , "|   typeof " , type(checklat_minus) )
        # print ("checklat_plus" , checklng_plus , "|   typeof " , type(checklng_plus) )
        # print ("checklat_minus" , checklng_minus , "|   typeof " , type(checklng_minus) )

        if (lat_min < curr_lat < lat_max) and (lng_min < curr_lng < lng_max):
            print(f"📍 發現目標在範圍內！ ID: {data.get('sna', 'data lost')} , 位置: {data.get('ar','data lost')}")
            print(f"目前座標: ({curr_lat}, {curr_lng})")

        
           
         
    # print("datas type" , type(datas))
# trackgps ()

    
    