import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 解決剛才提到的 CORS 問題
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_directory_tree(path: str):
    name = os.path.basename(path)
    # 建立基礎節點
    item = {
        "name": name,
        "type": "directory" if os.path.isdir(path) else "file",
        "path": path
    }
    # 如果是資料夾，遞迴找子項目
    if os.path.isdir(path):
        item["children"] = [
            get_directory_tree(os.path.join(path, x)) 
            for x in os.listdir(path) if not x.startswith('.') # 排除隱藏檔
        ]
    return item

@app.get("/files")
def read_files():
    # 讀取目前專案下的 data 資料夾
    root_path = "./data" 
    if not os.path.exists(root_path):
        return {"error": "請先建立 data 資料夾"}
    return get_directory_tree(root_path)

if __name__ == "__main__":
    # 直接在這裡寫死 Port，讓你用 python main.py 就能啟動
    uvicorn.run(app, host="127.0.0.1", port=3009)