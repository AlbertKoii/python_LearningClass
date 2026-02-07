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
    response.raise_for_status() # 檢查連線是否成功
    datas = response.json()



    for data in datas:

        # print ("data['lat']" , type(data['lat']))
        curr_lat = float(data['lat'])
        curr_lng = float(data['lng'])
        
        lat_max, lat_min = lat + diff, lat - diff
        lng_max, lng_min = lng + diff, lng - diff


        if (lat_min <= curr_lat <= lat_max) and (lng_min <= curr_lng <= lng_max):
            print(f"""發現目標在範圍內！ ID: {data.get('sna', 'data lost')} , 
                  位置: {data.get('ar','data lost')}""")
            print(f"目前座標: ({curr_lat}, {curr_lng})")

        
           
         
    # print("datas type" , type(datas))
# trackgps ()

    


# 學習gemini (large language model): 

# reference of skill agent 
# gemini-dev-orchestrator/
# ├── .env                        # 核心配置 (GEMINI_API_KEY, DB_PATH, LOG_LEVEL)
# ├── .gitignore                  # 排除 venv, node_modules, vector_db 等
# ├── Makefile                    # 業界標準入口：make init, make dev, make test
# ├── requirements.txt            # Python 套件：google-generativeai, chromadb, pydantic
# │
# ├── agent_engine/               # 【Python】Agent 決策核心
# │   ├── __init__.py
# │   ├── orchestrator.py         # 主循環：接收指令、規劃步驟、觸發工具
# │   ├── tools_registry.py       # 工具適配器：將 Python Skills 轉為 Gemini JSON Schema
# │   ├── memory_rse.py           # RAG 引擎：負責 Embedding 向量化與語意檢索
# │   └── logger.py               # 追蹤 Token 消耗與 Agent 思考路徑
# │
# ├── skills/                     # 【Python】原子化技能包 (Agent 的手腳)
# │   ├── __init__.py
# │   ├── workspace_ops.py        # 檔案 CRUD：限定在 ./workspace 範圍內
# │   ├── web_researcher.py       # RAG Skill：搜尋開發規範或既有 TS 代碼庫
# │   ├── js_executor.py          # JS 執行器：封裝 npm, npx, node 命令
# │   └── git_handler.py          # 版本管理：自動 Commit, Rollback 分支
# │
# ├── knowledge_base/             # 【Knowledge】RAG 資料來源
# │   ├── coding_standards/       # 你的 React/TS/Node 撰寫規範
# │   ├── component_templates/    # 既有的 UI 組件設計模式 (Design Patterns)
# │   └── project_context.md      # 當前專案的大地圖與核心邏輯說明
# │
# ├── vector_db/                  # 【Persistence】ChromaDB 向量數據存放處
# │
# ├── scripts/                    # 【DevOps】輔助腳本
# │   ├── ingest.py               # 啟動前將 knowledge_base 同步至向量庫
# │   └── bootstrap.py            # 初始化環境、檢查 node/python 版本
# │
# └── workspace/                  # 【Target Project】真正的 React/TS/Node 專案
#     ├── package.json
#     ├── tsconfig.json           # Agent 必須通過此配置的型別檢查
#     ├── frontend/               # React + TypeScript App
#     │   └── src/
#     └── backend/                # Node.js + Express/Nest.js


# google vision == 圖片辨識(早期非llm)