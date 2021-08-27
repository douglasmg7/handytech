#! /usr/bin/env bash

[[ -z "$GS" ]] && printf "error: GS enviorment not defined.\n" >&2 && exit 1 
[[ -z "$ZUNKAPATH" ]] && printf "error: ZUNKAPATH enviorment not defined.\n" >&2 && exit 1 
[[ -z "$HANDYTECH_XML" ]] && printf "error: HANDYTECH_XML enviorment not defined.\n" >&2 && exit 1 
[[ -z "$HANDYTECH_DB" ]] && printf "error: HANDYTECH_DB enviorment not defined.\n" >&2 && exit 1 
[[ -z "$HANDYTECH_HOST" ]] && printf "error: HANDYTECH_HOST enviorment not defined.\n" >&2 && exit 1 
[[ -z "$HANDYTECH_USER" ]] && printf "error: HANDYTECH_USER enviorment not defined.\n" >&2 && exit 1 
[[ -z "$HANDYTECH_PASS" ]] && printf "error: HANDYTECH_PASS enviorment not defined.\n" >&2 && exit 1 

# Script not exist.
[[ ! -f $GS/handytech/run.sh ]] && printf "error: script $GS/handytech/run.sh not exist.\n" >&2 && exit 1 
[[ ! -f $GS/handytech/service_uninstall.sh ]] && printf "error: script $GS/handytech/service_uninstall.sh not exist.\n" >&2 && exit 1

# Uninstall handytech timer and service.
$GS/handytech/service_uninstall.sh

# Create log dir.
mkdir -p $ZUNKAPATH/log/handytech

# Create handytech timer.
echo "creating '/lib/systemd/system/handytech.timer'..."
sudo bash -c 'cat << EOF > /lib/systemd/system/handytech.timer
[Unit]
Description=handytech timer

[Timer]
OnCalendar=*-*-* 00:00:01
OnCalendar=*-*-* 01:00:00
OnCalendar=*-*-* 02:00:00
OnCalendar=*-*-* 03:00:00
OnCalendar=*-*-* 04:00:00
OnCalendar=*-*-* 05:00:00
OnCalendar=*-*-* 06:00:00
OnCalendar=*-*-* 07:00:00
OnCalendar=*-*-* 08:00:00
OnCalendar=*-*-* 09:00:00
OnCalendar=*-*-* 10:00:00
OnCalendar=*-*-* 11:00:00
OnCalendar=*-*-* 12:00:00
OnCalendar=*-*-* 13:00:00
OnCalendar=*-*-* 14:00:00
OnCalendar=*-*-* 15:00:00
OnCalendar=*-*-* 16:00:00
OnCalendar=*-*-* 17:00:00
OnCalendar=*-*-* 18:00:00
OnCalendar=*-*-* 19:00:00
OnCalendar=*-*-* 20:00:00
OnCalendar=*-*-* 21:00:00
OnCalendar=*-*-* 22:00:00
OnCalendar=*-*-* 23:00:00

Persistent=true

[Install]
WantedBy=timers.target
EOF'

# Create handytech service.
echo "creating '/lib/systemd/system/handytech.service'..."
sudo \
    GS=$GS \
    ZUNKAPATH=$ZUNKAPATH \
    HANDYTECH_XML=$HANDYTECH_XML \
    HANDYTECH_DB=$HANDYTECH_DB \
    HANDYTECH_HOST=$HANDYTECH_HOST \
    HANDYTECH_USER=$HANDYTECH_USER \
    HANDYTECH_PASS=$HANDYTECH_PASS \
    bash -c 'cat << EOF > /lib/systemd/system/allnations.service
[Unit]
Description=allnations

[Service]
Type=oneshot
User=douglasmg7
Environment="GS=$GS"
Environment="ZUNKAPATH=$ZUNKAPATH"
Environment="HANDYTECH_XML=$HANDYTECH_XML"
Environment="HANDYTECH_DB=$HANDYTECH_DB"
Environment="HANDYTECH_HOST=$HANDYTECH_HOST"
Environment="HANDYTECH_USER=$HANDYTECH_USER"
Environment="HANDYTECH_PASS=$HANDYTECH_PASS"
ExecStart=$GS/handytech/run.sh
EOF'

sudo systemctl start handytech.timer
sudo systemctl enable handytech.timer
