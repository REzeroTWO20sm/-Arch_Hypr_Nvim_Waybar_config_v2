#!/bin/bash

STATE_FILE="$XDG_RUNTIME_DIR/keyboard.status"

if [ -f "$STATE_FILE" ]; then
    USER_SET_FREQ=$(cat "$STATE_FILE")
else
    USER_SET_FREQ_GHZ="N/A"
fi

# Возвращаем JSON с установленной частотой
echo "${USER_SET_FREQ}"
