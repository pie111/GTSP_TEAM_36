function initMap(){
    const directionsRenderer=new google.maps.DirectionsRenderer();
    const directionsService= new google.maps.DirectionsService();
    const map=new google.maps.Map(document.getElementById("map"),{
        zoom: 14,
        center:{lat: 37.77,lng: -122.447} 
    });

    directionsRenderer.setMap(map);
    displayRoute(directionsService, directionsRenderer);
    
}

function displayRoute(directionsService,directionsRenderer){
    const mode="DRIVING";

    directionsService
    .route({
        origin: document.getElementById("from").value,
        destination: document.getElementById("to").value,


        travelMode: google.maps.TravelMode[mode],
    })
    .then((response) => {
        directionsRenderer.setDirections(response); 
    })

    .catch((e)=> window.alert("Direction request failed " ));

}
