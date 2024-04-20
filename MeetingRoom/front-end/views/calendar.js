document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',  // 初始視圖設為月視圖
        events: [  // 這裡可以添加你的事件數據
            {
                title: '會議',
                start: '2024-04-01',
                end: '2024-04-02'
            },
            // 更多事件...
        ]
    });

    calendar.render();
});
