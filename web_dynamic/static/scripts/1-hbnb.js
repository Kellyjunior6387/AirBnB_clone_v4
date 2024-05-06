$(document).ready(function() {
  let checkedAmenities = {};

  $('input[type="checkbox"]').change(function() {
    if (this.checked) {
      checkedAmenities[$(this).data('amenity_id')] = $(this).data('amenity_name');
    } else {
      delete checkedAmenities[$(this).data('amenity_id')];
    }
    let lst = Object.values(checkedAmenities);
    if (lst.length > 0) {
      $('div.amenities > h4').text(Object.values(checkedAmenities).join(', '));
    } else {
      $('div.amenities > h4').html('&nbsp;');
    }
  });
});