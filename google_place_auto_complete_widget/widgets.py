import json

from django.conf import settings
from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe


class GooglePlaceAutocompleteWidget(TextInput):
    template_name = 'templates/google_place_auto_complete_widget/widget.html'

    class Media:
        js = (
            'static/google_place_auto_complete_widget/js/widget.js',
            'https://maps.googleapis.com/maps/api/js?key=%s&libraries=places&callback=initGooglePlaceAutocompleteWidget' % settings.GOOGLE_PLACE_AUTOCOMPLETE_KEY,
        )

    def __init__(self, options={}, *args, **kwargs):
        super(GooglePlaceAutocompleteWidget, self).__init__(*args, **kwargs)
        self.options = options

    def get_context(self, name, value, attrs):
        try:
            attrs['id']
        except (KeyError, TypeError):
            raise TypeError("GooglePlaceAutocompleteWidget cannot be rendered without an 'id' attribute")

        context = super(GooglePlaceAutocompleteWidget, self).get_context(name, value, attrs)
        context['options'] = mark_safe(json.dumps(self.options))
        context['widget']['attrs']['data-googleplaceautocompletewidget'] = ''
        return context
