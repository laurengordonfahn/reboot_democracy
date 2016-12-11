function initMap() {
  if ("geolocation" in navigator) {
    /* geolocation is available */
    navigator.geolocation.getCurrentPosition(function(position) {
      setupMap(position.coords.latitude, position.coords.longitude)
      console.log(position.coords.latitude)
      console.log(position.coords.longitude)
    });
  } else {
    setupMap(-25.363, 131.044)
  }
}

function getstarted() {
  $("#overlay").fadeOut(300, function() {
    // console.log($(this))
    $(this).remove();
  });
  $("#intro").fadeOut(200, function() {
  //   $(this).append('<img src="/static/img/getstarted.png">')
    $(this).remove();
  });
  setupPin()
}

function submitForm(el) {
  console.log("submitted")
  console.log(el)
  console.log($(el).find('#fname').val())
  console.log($(el).find('#cause').val())
  var fname = $(el).find('#fname').val()
  var cause = $(el).find('#cause').val()
  // console.log($(el)('[name=fname]').val())
  // console.log(el.('[name=cause]').val())

  var staticinfowindow = new google.maps.InfoWindow({
    content: '<div>Name: '+fname+'<br/>Cause: '+cause+'</div>'
  })

  marker.addListener('click', function() {
    staticinfowindow.open(marker.get('map'), marker)
  })

  marker = null
  infowindow.close()
  console.log(el)
  return false
}

var pinimg
function setupPin() {
  pinimg = $('<img id="#pinimg" class="centered" src="/static/img/dropapin.png">')
  $("body").append(pinimg)
}

var map
function setupMap(lat, long) {
  var uluru = {lat: lat, lng: long};
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 15,
    center: uluru,
    styles: [
      {
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#f5f5f5"
          }
        ]
      },
      {
        "elementType": "labels.icon",
        "stylers": [
          {
            "visibility": "off"
          }
        ]
      },
      {
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#616161"
          }
        ]
      },
      {
        "elementType": "labels.text.stroke",
        "stylers": [
          {
            "color": "#f5f5f5"
          }
        ]
      },
      {
        "featureType": "administrative.land_parcel",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#bdbdbd"
          }
        ]
      },
      {
        "featureType": "poi",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#eeeeee"
          }
        ]
      },
      {
        "featureType": "poi",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#757575"
          }
        ]
      },
      {
        "featureType": "poi.park",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#e5e5e5"
          }
        ]
      },
      {
        "featureType": "poi.park",
        "elementType": "geometry.fill",
        "stylers": [
          {
            "color": "#26b853"
          }
        ]
      },
      {
        "featureType": "poi.park",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#9e9e9e"
          }
        ]
      },
      {
        "featureType": "road",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#ffffff"
          }
        ]
      },
      {
        "featureType": "road.arterial",
        "elementType": "labels",
        "stylers": [
          {
            "visibility": "off"
          }
        ]
      },
      {
        "featureType": "road.arterial",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#757575"
          }
        ]
      },
      {
        "featureType": "road.highway",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#dadada"
          }
        ]
      },
      {
        "featureType": "road.highway",
        "elementType": "labels",
        "stylers": [
          {
            "visibility": "off"
          }
        ]
      },
      {
        "featureType": "road.highway",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#616161"
          }
        ]
      },
      {
        "featureType": "road.local",
        "stylers": [
          {
            "visibility": "off"
          }
        ]
      },
      {
        "featureType": "road.local",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#9e9e9e"
          }
        ]
      },
      {
        "featureType": "transit.line",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#e5e5e5"
          }
        ]
      },
      {
        "featureType": "transit.station",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#eeeeee"
          }
        ]
      },
      {
        "featureType": "water",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#c9c9c9"
          }
        ]
      },
      {
        "featureType": "water",
        "elementType": "geometry.fill",
        "stylers": [
          {
            "color": "#0099a2"
          }
        ]
      },
      {
        "featureType": "water",
        "elementType": "labels.text",
        "stylers": [
          {
            "color": "#ffffff"
          }
        ]
      },
      {
        "featureType": "water",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#ffffff"
          }
        ]
      }
      ]
  });

  // url = 'http://www.google.com/'
  // $.ajax({
  //   dataType: "json",
  //   url: url,
  //   // data: data,
  //   success : function( data, textStatus ) {
  //       console.log('asdfasdfasdf');
  //   },
  // });
  // $.getJSON( {
  //   url  : 'http://www.google.com/',
  //   data : {
  //   },
  //   success : function( data, textStatus ) {
  //       console.log('asdfasdfasdf');
  //   },
  //   error : function (data, textStatus) {
  //       console.log('asdfasdfasdf');
  //   }
  // });

  map.addListener('click', function(e) {
    placeMarkerAndPanTo(e.latLng, map);
  });

  var radius = 60
  markerImage = {
    url: './static/img/handscircle.png',
    size: new google.maps.Size(radius, radius),
    anchor: new google.maps.Point(radius/2, radius/2)
  }

  var uluru = {lat: lat - 0.0005, lng: long - 0.001};
  var marker = new google.maps.Marker({
    position: uluru,
    map: map,
    icon: markerImage
  });
  coordinates.push(uluru)

  var uluru = {lat: lat + 0.0005, lng: long + 0.0005};
  var marker = new google.maps.Marker({
    position: uluru,
    map: map,
    icon: markerImage
  });
  coordinates.push(uluru)
  var uluru = {lat: lat + 0.005, lng: long - 0.004};
  var marker = new google.maps.Marker({
    position: uluru,
    map: map,
    icon: markerImage
  });
  coordinates.push(uluru)

  drawPolyLine()
}

function drawPolyLine() {
  polylinePath = new google.maps.Polyline({
    path: coordinates,
    geodesic: true,
    strokeColor: '#FF0000',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  polylinePath.setMap(map);
}
var polylinePath
var marker
var infowindow
var markerImage
var coordinates = [
]

function placeMarkerAndPanTo(latLng, map) {
  if (marker) {
    marker.setMap(null)
  }
  var radius = 60
  markerImage = {
    url: './static/img/handscircle.png',
    size: new google.maps.Size(radius, radius),
    anchor: new google.maps.Point(radius/2, radius/2)
  }
  marker = new google.maps.Marker({
    position: latLng,
    icon: markerImage,
    map: map,
    draggable:true
  });

  marker.addListener('click', function() {
    infowindow.open(marker.get('map'), marker)
  })
  infowindow = new google.maps.InfoWindow({
    content: $('#nameform').html()
  })
  pinimg.remove()
  map.panTo(latLng);
  infowindow.open(marker.get('map'), marker)

  coordinates.push(latLng)

  drawPolyLine()
}