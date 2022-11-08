#!/usr/bin/python3
import argparse
import requests

def send(title, body):
  requests.post('http://ntfy.sh/lizquickping',
    headers={
      'Title': title.encode('utf-8'),
    },
    data=body.encode('utf-8'),
  ).raise_for_status()

parser = argparse.ArgumentParser(description='Send a notification using ntfy.sh')

parser.add_argument(
  '--title', '-t',
  metavar='X',
  default='ᓚᘏᗢ meow',
  type=str,
  help='Top text of the notification',
  dest='title')

parser.add_argument(
  '--body', '-b', 
  metavar='Y',
  default='Stuff just happened',
  type=str,
  help='Body of the notification',
  dest='body')

args = parser.parse_args()

send(
  title=args.title,
  body=args.body,
)

# https://ntfy.sh/docs/