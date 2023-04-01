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
            eventDisplay: 'block',
          },
          {
            url: '/api/v1/insurance_events/',
            color: '#378006',

          }
        ],
      eventClick: function(info) {
        alert('Event: ' + info.event.title + ' Date: ' + info.event.start);      
        info.el.style.backgroundColor = 'lightgray';
      }

    });

    calendar.render();
  });