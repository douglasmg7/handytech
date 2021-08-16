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

# Populate db if exist.
if [[ -f $HANDYTECH_DB ]]; then
	printf "Populating db %s/%s\n" $HANDYTECH_DB
    sqlite3 $HANDYTECH_DB < $(dirname $0)/data.sql
else
	printf "Error: db %s not exist\n" $HANDYTECH_DB >&2
fi
