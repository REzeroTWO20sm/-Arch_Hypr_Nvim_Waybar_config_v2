#!/bin/bash

STATE_FILE="/tmp/cpu_frequency_state"

if [ -f "$STATE_FILE" ]; then
    USER_SET_FREQ=$(cat "$STATE_FILE")
    USER_SET_FREQ_GHZ=$(awk "BEGIN {printf \"%.2f\", $USER_SET_FREQ / 1000000}")
else
    USER_SET_FREQ_GHZ="N/A"
fi

# Возвращаем JSON с установленной частотой
echo "{\"text\": \"${USER_SET_FREQ_GHZ}GHz\", \"tooltip\": \"Frequency from STATE_FILE\"}"
