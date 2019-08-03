from IPython.display import HTML
myhtml = HTML("""<html>
  <head>
    <title>Simple Map</title>
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">
    <style>    
    .container2 { height:500px !important; };
      /* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
      #map {
        height: 100%;
      }
      /* Optional: Makes the sample page fill the window. */
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>
    <div id="map" class="container2"></div>
    <script>
      var map;
      function initMap() {

        //Customitzar google maps - https://mapstyle.withgoogle.com/
        var styledMapType = new google.maps.StyledMapType(
         [
         {
          "featureType": "administrative.province",
          "stylers": [
          {
            "visibility": "off"
          }
          ]
        },
        {
          "featureType": "poi",
          "stylers": [
          {
            "visibility": "off"
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
          "featureType": "road.highway",
          "elementType": "geometry.fill",
          "stylers": [
          {
            "color": "#d1,d1d1"
          }
          ]
        },
        {
          "featureType": "road.highway",
          "elementType": "geometry.stroke",
          "stylers": [
          {
            "color": "#b8b8b8"
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
          "featureType": "transit",
          "stylers": [
          {
            "visibility": "off"
          }
          ]
        },
        {
          "featureType": "water",
          "elementType": "geometry.fill",
          "stylers": [
          {
            "saturation": -55
          }
          ]
        }
        ],
        {name: 'Styled Map'});

        map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: 50.8660773, lng: 20.6285677},
          zoom: 4,
          streetViewControl: false,
          fullscreenControl: false,
          mapTypeControl: false,
          mapTypeControlOptions: {
            mapTypeIds: ['roadmap', 'satellite', 'hybrid', 'terrain',
            'styled_map']
          }
        });

        //Associate the styled map with the MapTypeId and set it to display.
        map.mapTypes.set('styled_map', styledMapType);
        map.setMapTypeId('styled_map');
      }
    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCwABJwV-V_3M9R2mxQFUGlbaa8SGMLaN4&callback=initMap"
    async defer></script>
  </body>
</html>""") #make the html object
myhtml
