#!/usr/bin/env bash 

# HANDYTECH_DB not defined.
if [ -z "$HANDYTECH_DB" ]; then
	printf "error: HANDYTECH_DB not defined.\n" >&2
	exit 1 
fi

# Updating db.
echo Updating $HANDYTECH_DB
sqlite3 $HANDYTECH_DB < $(dirname $0)/update-tables.sql
