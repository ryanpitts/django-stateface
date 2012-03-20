'''
A simple templatetag for rendering icons from ProPublica's awesome StateFace
font project.

    http://propublica.github.com/stateface/

This tag assumes you have the StateFace font installed on your webserver,
and a @font-face declaration and CSS class something like:

    @font-face {
        font-family: 'StateFaceRegular';
        src: url('<YOUR_PATH_HERE>/stateface-regular-webfont.eot');
        src: url('<YOUR_PATH_HERE>/stateface-regular-webfont.eot?#iefix') format('embedded-opentype'),
             url('<YOUR_PATH_HERE>/stateface-regular-webfont.woff') format('woff'),
             url('<YOUR_PATH_HERE>/stateface-regular-webfont.ttf') format('truetype'),
             url('<YOUR_PATH_HERE>/stateface-regular-webfont.svg#StateFaceRegular') format('svg');
        font-weight: normal;
        font-style: normal;
    }

    i.stateface {font-family: 'StateFaceRegular'; font-style: normal;}
    
Adjust the `templates/stateface/stateface_icon.html` as you see fit, to change
the CSS class, use a different HTML element to contain the shape, whatever.

USAGE:

In your Django templates, render a state shape icon by feeding this tag with
a string or a context variable.

    {% render_stateface_icon 'WA' %}
    {% render_stateface_icon restaurant.city.state.abbr %}

'''
from django import template

register = template.Library()

STATE_KEY_DICT = {
  "GA": "J",
  "OR": "k",
  "OK": "j",
  "OH": "i",
  "DC": "y",
  "DE": "H",
  "VA": "s",
  "VT": "t",
  "LA": "R",
  "AR": "C",
  "AZ": "D",
  "AK": "A",
  "AL": "B",
  "SD": "o",
  "SC": "n",
  "IA": "L",
  "IN": "O",
  "IL": "N",
  "ID": "M",
  "FL": "I",
  "ND": "b",
  "NC": "a",
  "NY": "h",
  "NM": "f",
  "NJ": "e",
  "NH": "d",
  "NV": "g",
  "NE": "c",
  "CT": "G",
  "CO": "F",
  "CA": "E",
  "US": "z",
  "UT": "r",
  "KY": "Q",
  "KS": "P",
  "RI": "m",
  "HI": "K",
  "PA": "l",
  "WY": "x",
  "WI": "v",
  "WV": "w",
  "WA": "u",
  "MT": "Z",
  "MO": "X",
  "MS": "Y",
  "MN": "W",
  "MI": "V",
  "MA": "S",
  "MD": "T",
  "ME": "U",
  "TX": "q",
  "TN": "p"
}

@register.inclusion_tag('stateface/stateface_icon.html', takes_context=True)
def render_stateface_icon(context, postal_code):
    state_key = context.get('postal_code', None)
    if state_key:
        # have we been passed a var?
        return {'state_key': STATE_KEY_DICT[state_key]}
    else:
        # nope, we've been passed a string
        return {'state_key': STATE_KEY_DICT[postal_code]}
    