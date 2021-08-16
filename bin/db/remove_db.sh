#!/usr/bin/env bash 

# $HANDYTECH_DB not defined.
if [ -z "$HANDYTECH_DB" ]; then
	printf "Error: HANDYTECH_DB not defined.\n" >&2
	exit 1 
fi

if [ -f $HANDYTECH_DB ]; then
    printf "Removing db %s\n" $HANDYTECH_DB
    rm $HANDYTECH_DB
else
    printf "Db %s not exist\n" $HANDYTECH_DB
fi
