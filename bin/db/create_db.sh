#!/usr/bin/env bash 

# ZUNKAPATH not defined.
if [ -z "$ZUNKAPATH" ]; then
	printf "error: ZUNKAPATH not defined.\n" >&2
	exit 1 
fi

# HANDYTECH_DB not defined.
if [ -z "$HANDYTECH_DB" ]; then
	printf "error: HANDYTECH_DB not defined.\n" >&2
	exit 1 
fi

# Create db if not exist.
if [[ ! -f $HANDYTECH_DB ]]; then
	echo Creating $HANDYTECH_DB
    mkdir -p $ZUNKAPATH/db
    sqlite3 $HANDYTECH_DB < $(dirname $0)/tables.sql
fi
