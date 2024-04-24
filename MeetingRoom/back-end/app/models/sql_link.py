import mysql.connector
from config import db  # 引用資料庫配置文件
# 連線資料庫
print("資料庫連線成功")
# 建立cusor物件來對資料庫下指令
cursor = db.cursor()


def create_reservation(reservation):
    cursor = db.cursor()

    # 創建reservations表
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reservations (
        id INT AUTO_INCREMENT PRIMARY KEY,
        roomName VARCHAR(255) NOT NULL,
        date DATE NOT NULL,
        startTime TIME NOT NULL,
        endTime TIME NOT NULL
    );
    """)

    # 插入新的預約資料
    insert_query = """
    INSERT INTO reservations (roomName, date, startTime, endTime)
    VALUES (%s, %s, %s, %s);
    """
    cursor.execute(insert_query, (reservation['roomName'], reservation['date'],
                   reservation['startTime'], reservation['endTime']))

    db.commit()
    db.close()

    return {"message": "Successfully reserved the room."}


# 取得所有数据库数据
cursor.execute('SELECT * FROM Meetings')

# 關閉資料庫連線
# db.close()
# # 檢視資料庫資料
# data = cursor.execute('select *from product; ')
# com.commit()  # =>執行
# print("%s顯示成功", (data))
# 關閉資料庫連線
# com.close()
