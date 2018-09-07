// All autocomplete instances which you can use for binding 'place_changed' event
var googlePlaceAutocompleteWidgetInstances = {};

// Init function which will get called by google api js callback when loaded
function initGooglePlaceAutocompleteWidget() {
  $(document).ready(function () {
    var inputs = document.querySelectorAll('[data-googleplaceautocompletewidget]');

    inputs.forEach(function (input) {
      var id = input.id;
      var options = JSON.parse(document.getElementById('options_' + id).innerHTML);

      autocomplete = new google.maps.places.Autocomplete(input, options);

      googlePlaceAutocompleteWidgetInstances[id] = autocomplete;

      autocomplete.addListener('place_changed', fillAddress);
    });
  });
}



