#!/usr/bin/env bash

# ZUNKAPATH must be defined.
[[ -z "$ZUNKAPATH" ]] && printf "error: ZUNKAPATH enviorment not defined.\n" >&2 && exit 1 
[[ -z "$HANDYTECH_HOST" ]] && printf "error: HANDYTECH_HOST enviorment not defined.\n" >&2 && exit 1 
[[ -z "$HANDYTECH_USER" ]] && printf "error: HANDYTECH_USER enviorment not defined.\n" >&2 && exit 1 
[[ -z "$HANDYTECH_PASS" ]] && printf "error: HANDYTECH_PASS enviorment not defined.\n" >&2 && exit 1 

# Create dir if not exist.
XML_PATH=$ZUNKAPATH/xml/handytech
mkdir -p $XML_PATH

NOW=$(date +%Y-%m-%dT%H:%M:%S-03:00)

# Last downloaded XML file.
FILE_LAST=$XML_PATH/handytech_products_to_process.xml

# Will not download products information if last file not processed yet.
if [ -f $FILE_LAST ]; then
    echo "Nothing to do, last file wasn't processed yet."
    exit 0
fi

# XML file backup.
FILE_BACKUP=$XML_PATH/handytech_products_${NOW}.xml

# Download xml file.
URL=${HANDYTECH_HOST}/xml
curl -v $URL > $FILE_BACKUP

# Get created file size.
if [[ -f $FILE_BACKUP ]]; then
    FILE_SIZE=$(stat -c%s $FILE_BACKUP)
else
    FILE_SIZE=0
fi

# If a valid size, copy as last xml file to process.
# echo size: $FILE_SIZE
if [[ "$FILE_SIZE" -gt "1000" ]]; then
    cp $FILE_BACKUP $FILE_LAST
fi