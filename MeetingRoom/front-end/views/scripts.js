function reserveRoom() {
    const roomName = document.getElementById("roomName").value;
    const date = document.getElementById("date").value;
    const startTime = document.getElementById("startTime").value;
    const endTime = document.getElementById("endTime").value;

    const reservation = {
        roomName: roomName,
        date: date,
        startTime: startTime,
        endTime: endTime
    };

    // 這裡可以使用 AJAX 請求將預約資料發送到後端 API
    console.log("預約資料:", reservation);


    // 清空輸入框
    document.getElementById("roomName").value = "";
    document.getElementById("date").value = "";
    document.getElementById("startTime").value = "";
    document.getElementById("endTime").value = "";

    // 更新預約清單（這裡只是示例，實際應用中需要從後端 API 獲取預約清單）
    const reservationList = document.getElementById("reservationList");
    const reservationItem = document.createElement("li");
    reservationItem.textContent = `${roomName} - ${date} ${startTime}-${endTime}`;
    reservationList.appendChild(reservationItem);
}
