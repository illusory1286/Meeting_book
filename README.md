## 學習筆記 - 課程內容紀錄

**課程名稱：**
會議室預約系統

**日期：**
113/4/19

**課程目的：**
製作會議預約系統

**內容摘要：**
1. [概述](#概述)
2. [重點紀錄](#重點紀錄)
3. [問題與討論](#問題與討論)
4. [下一步行動](#下一步行動)



專案結構
```
.
├── back-end
│   └── app
│       ├── 123.ipynb
│       ├── __pycache__
│       │   └── main.cpython-312.pyc
│       ├── api
│       ├── database.py
│       ├── models
│       │   ├── __pycache__
│       │   │   └── main.cpython-312.pyc
│       │   └── main.py
│       ├── services
│       └── view_models
├── front-end
│   ├── styles
│   │   ├── calendar.css
│   │   └── style.css
│   └── views
│       ├── calendar.html
│       ├── calendar.js
│       ├── index.html
│       └── scripts.js
├── notes
│   ├── git.md
│   ├── images
│   │   └── img_0.png
│   └── note.md
└── tests

```

### 概述
簡要描述本次課程的主題和目標。

### 重點紀錄
4/19
- NodeJs服務器
  1. [導入http模組](#導入http模組)

  ```NodeJs
  const http=require("http")
  ```
  2. 使用http模塊,用回調函數參數(request,response)

  ```
  const server =http.createServer((request,response)=>{
    response.end("Welcone My World")
  })
  ```
  3. 創一個伺服器監聽
  ```
  const port=3000;
  const ip="127.0.0.1"
  server.listen(port,ip,()=>{
      console.log(`server is running at http://${ip}:${port}`)
  })
  ```

4/22
1.前端卡控
```js
    if(startTime === endTime){
        reservationItem.textContent = "預約資訊："+`${roomName} - ${date} ${startTime}-${endTime}`;
        reservationList.appendChild(reservationItem);
    }
    else if(startTime > endTime){
        alert("開始時間不可大於結束時間");
    }
```

2.連線資料庫(確認連線)

```python
  import mysql.connector
  from config import db  # 引用資料庫配置文件
  # 連線資料庫
  print("資料庫連線成功")
  # 建立cusor物件來對資料庫下指令
  cursor = db.cursor()    
  # 取得所有数据库数据
  cursor.execute('SELECT * FROM Meetings')

  # 關閉資料庫連線
  db.close()
```


4/23
1.前後資料串接
2.git檔案commit
### 問題與討論
4/19
- 介紹中斷點
- 介紹基本輸入輸出
    1. 導入http模組
    2. http模組,使用回調函並賦予兩個參數(request,response)
    3. 創一個伺服器監聽

4/22 CORS跨域問題
```python
  from fastapi import FastAPI
  from fastapi.middleware.cors import CORSMiddleware

  app = FastAPI()

  # 添加CORS中間件
  app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],  # 允許所有來源訪問，你也可以指定特定的來源
      allow_credentials=True,
      allow_methods=["*"],  # 允許所有HTTP方法
      allow_headers=["*"],  # 允許所有標頭
  )

```


### 下一週作業
創建 github 專案 (以會議室預約系統為例)
前端 (切版)
後端設計 (restful api)
資料庫規劃
檔案架構規劃





