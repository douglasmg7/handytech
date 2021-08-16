#!/usr/bin/env bash 

if [ -z "$1" ]
  then
    echo "Usage: $0 file.sql"
    exit
fi


# HANDYTECH_DB not defined.
if [ -z "$HANDYTECH_DB" ]; then
	printf "error: HANDYTECH_DB not defined.\n" >&2
	exit 1 
fi


# Create db if not exist.
if [[ ! -f $HANDYTECH_DB ]]; then
    printf "Not found db %s\n" $HANDYTECH_DB
    exit 1
fi

# sqlite3 $HANDYTECH_DB < $(dirname $0)/tables.sql
sqlite3 $HANDYTECH_DB < $1
