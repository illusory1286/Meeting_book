from fastapi import FastAPI, Query, Response, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# from sql_link import create_reservation


app = FastAPI()
# 添加CORS中間件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允許所有來源訪問，你也可以指定特定的來源
    allow_credentials=True,
    allow_methods=["*"],  # 允許所有HTTP方法
    allow_headers=["*"],  # 允許所有標頭
)


class Reservation(BaseModel):
    roomName: str
    date: str
    startTime: str
    endTime: str


@app.get('/user')
async def user(
    *,
    user_id: int = Query(..., title="The ID of the user to get", gt=0)
):
    return {'user_id': user_id}


# @app.post("/reserve")
# def reserve_room(reservation: Reservation, response: Response):
#     # 在這裡實現預約邏輯
#     print("Received reservation request:")
#     print(f"Room Name: {reservation.roomName}")
#     print(f"Date: {reservation.date}")
#     print(f"Start Time: {reservation.startTime}")
#     print(f"End Time: {reservation.endTime}")

    # # # 將預約資料傳遞給create_reservation函數以更新資料庫
    # result = create_reservation(reservation.model_dump())
    # message = result.get("message", "Failed to reserve the room.")
    # # message = "Successfully reserved the room."
    # return {"message": message}

    # # 設置HTTP回應的狀態碼和內容
    # if "Successfully" in message:
    #     response.status_code = status.HTTP_200_OK
    # else:
    #     response.status_code = status.HTTP_400_BAD_REQUEST

    # return {"message": message}


@app.post("/reserve")
def reserve_room(reservation: Reservation, response: Response):
    # 在這裡實現預約邏輯
    print("Received reservation request:")
    print(f"Room Name: {reservation.roomName}")
    print(f"Date: {reservation.date}")
    print(f"Start Time: {reservation.startTime}")
    print(f"End Time: {reservation.endTime}")

    # 調用create_reservation函數以更新資料庫
    # result = create_reservation(reservation.model_dump())
    # message = result.get("message", "Failed12312 to reserve the room.")

    # 設置HTTP回應的狀態碼和內容
    if "Successfully" in message:
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST

    return {"message": message}
