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
});
