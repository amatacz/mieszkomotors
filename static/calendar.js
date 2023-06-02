document.addEventListener('DOMContentLoaded', function() {
  var calendarTest = document.getElementById('calendar')

  /* Create function to initialize the correct view */
  function mobileCheck() {
      if (window.innerWidth >= 768 ) {
          return false;
      } else {
          return true;
      }
  };
  /* Start Full Calendar */
  var calendar = new FullCalendar.Calendar(calendarTest, {
          /* Create new view */
          views: {
              newView: {
                  /* Your responsive view */
                  type: 'dayGridDay',
              }
          },
          /* Choose view when initialize */
          defaultView: mobileCheck() ? "newView" : "dayGridMonth",
          /* Check if window resize and add the new view */
          windowResize: function(view) {
              if (window.innerWidth >= 768 ) {
                  calendar.changeView('dayGridMonth');
                  /* More code */
              } else {
                  calendar.changeView('dayGridDay');
                  /* More code */
              }
          },
          navLinks: true,
          dayMaxEvents: true,
          height: "auto",
          timeZone: 'local',
          locale: 'pl',
          firstDay: 1,
          nowIndicator: true,
          headerToolbar: {
            right: 'prev,next',
          },
          footerToolbar: {
            right: 'today',
            left: 'dayGridMonth,timeGridWeek,timeGridDay'
          },
          businessHours: {
            daysOfWeek: [1, 2, 3, 4, 5],
            startTime: '08:00',
            endTime: '20:00',
          },
      eventSources:
            [
              {
                url: '/api/v1/car_events/',
                backgroundColor: '#ffd400',
                textColor: '#000000',
                borderColor: '#ffffff',
              },
              {
                url: '/api/v1/insurance_events/',
                backgroundColor: '#091661',
                textColor: '#ffffff',
                borderColor: '#ffffff',
            
              },
              {
                url: '/api/v1/generic_events/',
                backgroundColor: '#e1eff1',
                textColor: '#000000',
                borderColor: '#ffffff',
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
