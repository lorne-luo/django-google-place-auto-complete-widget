# SUMMARY
A widget to enable Google Place Autocomplete for a form field. More inforation:https://developers.google.com/maps/documentation/javascript/examples/places-autocomplete-addressform

# CONFIGURE
1. Add GOOGLE_PLACE_AUTOCOMPLETE_KEY in your settings.

# EXAMPLE
```python
from google_place_auto_complete_widget.widgets import GooglePlaceAutocompleteWidget
    
residential_address = forms.CharField(required=True, max_length=50, label=_(RESIDENTIAL_ADDRESS_LABEL),
                                          widget=GooglePlaceAutocompleteWidget(
                                              attrs={'placeholder': ''},
                                              options={
                                                  'types': ['address'],
                                                  'componentRestrictions': {'country': 'au'},
                                              }))
```