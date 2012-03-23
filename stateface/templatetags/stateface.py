'''
A simple templatetag for rendering icons from ProPublica's awesome StateFace
font project.

    http://propublica.github.com/stateface/

In your Django templates, render a state shape icon by feeding this tag
a string or a context variable.

    {% render_stateface_icon 'Washington' %}
    {% render_stateface_icon 'WA' %}
    {% render_stateface_icon 'Wash.' %}
    {% render_stateface_icon restaurant.city.state.abbr %}
    
'''
from django import template

register = template.Library()

STATE_KEY_MAP = [
    ["Alabama", "AL", "Ala.", "B"],
    ["Alaska", "AK", "Alaska", "A"],
    ["Arizona", "AZ", "Ariz.", "D"],
    ["Arkansas", "AR", "Ark.", "C"],
    ["California", "CA", "Calif.", "E"],
    ["Colorado", "CO", "Colo.", "F"],
    ["Connecticut", "CT", "Conn.", "G"],
    ["Delaware", "DE", "Del.", "H"],
    ["District of Columbia", "DC", "D.C.", "y"],
    ["Florida", "FL", "Fla.", "I"],
    ["Georgia", "GA", "Ga.", "J"],
    ["Hawaii", "HI", "Hawaii", "K"],
    ["Idaho", "ID", "Idaho", "M"],
    ["Illinois", "IL", "Ill.", "N"],
    ["Indiana", "IN", "Ind.", "O"],
    ["Iowa", "IA", "Iowa", "L"],
    ["Kansas", "KS", "Kan.", "P"],
    ["Kentucky", "KY", "Ky.", "Q"],
    ["Louisiana", "LA", "La.", "R"],
    ["Maine", "ME", "Maine", "U"],
    ["Maryland", "MD", "Md.", "T"],
    ["Massachusetts", "MA", "Mass.", "S"],
    ["Michigan", "MI", "Mich.", "V"],
    ["Minnesota", "MN", "Minn.", "W"],
    ["Mississippi", "MS", "Miss.", "Y"],
    ["Missouri", "MO", "Mo.", "X"],
    ["Montana", "MT", "Mont.", "Z"],
    ["Nebraska", "NE", "Neb.", "c"],
    ["Nevada", "NV", "Nev.", "g"],
    ["New Hampshire", "NH", "N.H.", "d"],
    ["New Jersey", "NJ", "N.J.", "e"],
    ["New Mexico", "NM", "N.M.", "f"],
    ["New York", "NY", "N.Y.", "h"],
    ["North Carolina", "NC", "N.C.", "a"],
    ["North Dakota", "ND", "N.D.", "b"],
    ["Ohio", "OH", "Ohio", "i"],
    ["Oklahoma", "OK", "Okla.", "j"],
    ["Oregon", "OR", "Ore.", "k"],
    ["Pennsylvania", "PA", "Pa.", "l"],
    ["Rhode Island", "RI", "R.I.", "m"],
    ["South Carolina", "SC", "S.C.", "n"],
    ["South Dakota", "SD", "S.D.", "o"],
    ["Tennessee", "TN", "Tenn.", "p"],
    ["Texas", "TX", "Texas", "q"],
    ["Utah", "UT", "Utah", "r"],
    ["Vermont", "VT", "Vt.", "t"],
    ["Virginia", "VA", "Va.", "s"],
    ["Washington", "WA", "Wash.", "u"],
    ["West Virginia", "WV", "W.Va.", "w"],
    ["Wisconsin", "WI", "Wis.", "v"],
    ["Wyoming", "WY", "Wyo.", "x"],
    ["United States", "US", "U.S.", "z"],
]

@register.inclusion_tag('stateface/stateface_icon.html', takes_context=True)
def render_stateface_icon(context, state_value):
    # check for context variable, fall back to string input
    var = context.get(state_value, state_value)
    
    # find state in map based on full name, postal code or AP abbrevation
    state_list = filter(lambda state: var in state, STATE_KEY_MAP)

    # if we find a state, the last value is the StateFace keycode
    if len(state_list):
        state_key = state_list[0][3]
    else:
        state_key = ''
    return {'state_key': state_key}
