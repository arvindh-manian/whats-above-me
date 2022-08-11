const createCalendar = () => {
    var calendarEl = $("#calendar")[0];
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: [
            {
                id: 'a',
                title: 'my event',
                start: '2022-08-08'
            }
        ]
    });
    calendar.render();
}

const getEvents = (time_zone) => {
    return [
        {
            title: "my event",
            start: "2022-08-08"
        }
    ]
}

document.addEventListener('DOMContentLoaded', function() {
    createCalendar();
});
