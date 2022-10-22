#!/usr/bin/xonsh
import argparse

def send(title, body):
  $(curl ntfy.sh/lizquickping \
    --silent \
    -H @(f'Title: {title}') \
    -d @(body) 
  )

parser = argparse.ArgumentParser(description='Send a message to the ntfy.sh service')

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