# Get normal URL-parsing calls.

try:
    from urllib.parse import parse_qsl
    from urllib.parse import urlencode
except ImportError:
    # Python 3
    from urllib.parse import parse_qsl, urlencode

# Get a normal string type.

try:
    # Python 2
    str = str
except NameError:
    # Python 3
    str = str
