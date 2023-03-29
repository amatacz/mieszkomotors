document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    
    var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth',
      initialDate: '2023-03-29',
      editable: true,
      eventLimit: true,
      headerToolbar: {
        left: 'prev, next, today',
        center: 'title',
        right: 'dayGridMonth, timeGridWeek, timeGridDay'
      },
      eventSources:
        [
          {
            url: '/api/v1/car_events/',
            color: 'gold',
            textColor: 'black',
          },
          {
            url: '/api/v1/insurance_events/',
            color: 'darkblue',
            textColor: 'white',
          }
        ],
      eventClick: function(info) {
        alert('Event: ' + info.event.title + ' Date: ' + info.event.start);      
        // change the border color just for fun
        info.el.style.backgroundColor = 'lightgray';
      }

    });

    calendar.render();
  });