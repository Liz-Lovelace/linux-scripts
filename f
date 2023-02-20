#!/bin/bash

FILEPATH=$(fzf)
echo $FILEPATH
micro $FILEPATH
