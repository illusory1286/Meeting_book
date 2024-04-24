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

    // 檢查必填字段是否都已填寫
    if (roomName === "" || date === "" || startTime === "" || endTime === "") {
        alert("請填寫所有必填字段！");
        return;
    }

    // 使用 fetch 請求將預約資料發送到後端 API
    // 發送預約請求到FastAPI後端
    fetch('http://127.0.0.1:8000/reserve', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(reservation),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Reservation failed. Please try again.');
    });
    console.log("預約資料:", reservation);


    // 清空輸入框
    document.getElementById("roomName").value = "";
    document.getElementById("date").value = "";
    document.getElementById("startTime").value = "";
    document.getElementById("endTime").value = "";

    // 更新預約清單（這裡只是示例，實際應用中需要從後端 API 獲取預約清單）
    const reservationList = document.getElementById("reservationList");
    const reservationItem = document.createElement("li");
    if(startTime === endTime){
        reservationItem.textContent = "預約資訊："+`${roomName} - ${date} ${startTime}-${endTime}`;
        reservationList.appendChild(reservationItem);
    }
    else if(startTime > endTime){
        alert("開始時間不可大於結束時間");
    }
    
}



function login(){
    // 登入成功後延遲一段時間再跳轉至新頁面
    setTimeout(function() {
        window.location.href = 'http://127.0.0.1:5000/page';
    }, 1000); // 2000毫秒 (2秒) 的延遲
}