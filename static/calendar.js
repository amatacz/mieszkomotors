document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');
  
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    navLinks: true,
    height: "auto",
    headerToolbar: {
      left: 'prev,next,today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay'
    },
    eventSources:
      [
        {
          url: '/api/v1/car_events/',
          backgroundColor: '#ffed47',
          textColor: 'black',
        },
        {
          url: '/api/v1/insurance_events/',
          backgroundColor: '#3717b5',
          textColor: 'white',
        }
      ],
    eventClick: function(info) {
      console.log("log2")

      alert('Event: ' + info.event.title + ' Date: ' + info.event.start);      
    },
    eventDidMount: function(arg) {
      console.log("log")
      $(arg.el).popover({
          title: arg.event.title,
          content: arg.event.extendedProps.description,
          trigger: 'hover',
          placement: 'top',
          container: 'body',
          html: true,
          template: `<div class="popover" role="tooltip"><div class="arrow"></div><h3 class="popover-header bg-dark text-white"></h3><div class="popover-body"></div></div>`
      });
    },
  });
  calendar.render();
});