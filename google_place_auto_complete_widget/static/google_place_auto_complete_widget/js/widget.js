// All autocomplete instances which you can use for binding 'place_changed' event
var googlePlaceAutocompleteWidgetInstances = {};

// Init function which will get called by google api js callback when loaded
function initGooglePlaceAutocompleteWidget() {
  $(document).ready(function () {
      
    // Turn off the filed auto-fill form the browser. 
    // In Chrome, autocomplete = off does not work. Need to set it to be new-password
    // However, we cannot simply specify the autocomplete=new-password in HTML since the Google place autocomplete will change that attribute to be off. 
    $("[data-googleplaceautocompletewidget]").on('focus', function (e) {
       $(this).attr('autocomplete', "new-password");
      });

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



