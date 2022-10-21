import sys

def simple_ping(message: str):
  $(curl -d @(message) ntfy.sh/lizquickping)

if sys.argv[1] == 'simple':
  simple_ping(sys.argv[2])

# https://ntfy.sh/docs/