$(document).ready(function() {
  var maxDisplayedAmenities = 3;
  // Listen for changes on each input checkbox tag
  $('input[type="checkbox"]').change(function() {
    var selectedAmenities = [];

    // Loop through each checked checkbox and store Amenity ID in the array
    $('input[type="checkbox"]:checked').each(function() {
      selectedAmenities.push($(this).data('name'));
    });
    var displayAmenities = selectedAmenities.slice(0, maxDisplayedAmenities);
    var overflowCount = selectedAmenities.length - maxDisplayedAmenities;

    // Update the h4 tag inside the Amenities section with the list of Amenities checked
    if (overflowCount > 0) {
      $('.amenities h4').text(displayAmenities.join(', ') + ' ... (+' + overflowCount + ' more)');
    } else {
      $('.amenities h4').text(displayAmenities.join(', '));
    }

  });
  $.get('http://127.0.0.1:5001/api/v1/status/', function (data) {
    if (data.status === 'OK') {
      $('#api_status').addClass('available');
    } else {
      $('#api_status').removeClass('available');
    }
  });
  $.ajax({
    type: 'POST',
    url: 'http://127.0.0.1:5001/api/v1/places_search',
    data: '{}',
    dataType: 'json',
    contentType: 'application/json',
    success: function (data) {
      for (let i = 0; i < data.length; i++) {
        let place = data[i];
        $('.places ').append('<article><h2>' + place.name + '</h2><div class="price_by_night">$' + place.price_by_night + '</div><div class="information"><div class="max_guest"><div class="guest_image"></div><p>' + place.max_guest + '</p></div><div class="number_rooms"><div class="bed_image"></div><p>' + place.number_rooms + '</p></div><div class="number_bathrooms"><div class="bath_image"></div><p>' + place.number_bathrooms + '</p></div></div><div class="description"><p>' + place.description + '</p></div></article>');
      }
    }
  });
  $('button').click(function() {
    var selectedAmenities = [];

    // Loop through each checked checkbox and store Amenity ID in the array
    $('input[type="checkbox"]:checked').each(function() {
      selectedAmenities.push($(this).data('id'));
    });

    // Make a POST request to places_search with the list of checked amenities
    $.ajax({
      type: 'POST',
      url: 'http://127.0.0.1:5001/api/v1/places_search',
      data: JSON.stringify({ amenities: selectedAmenities }),
      dataType: 'json',
      contentType: 'application/json',
      success: function (data) {
        // Clear existing content
        $('.places').empty();

        // Update the places section with the response data
      for (let i = 0; i < data.length; i++) {
        let place = data[i];
        $('.places ').append('<article><h2>' + place.name + '</h2><div class="price_by_night">$' + place.price_by_night + '</div><div class="information"><div class="max_guest"><div class="guest_image"></div><p>' + place.max_guest + '</p></div><div class="number_rooms"><div class="bed_image"></div><p>' + place.number_rooms + '</p></div><div class="number_bathrooms"><div class="bath_image"></div><p>' + place.number_bathrooms + '</p></div></div><div class="description"><p>' + place.description + '</p></div></article>');
      }
      },
      error: function(xhr, textStatus, errorThrown) {
        console.error('Error:', errorThrown); // Log any errors
      }
    });
  });
});
