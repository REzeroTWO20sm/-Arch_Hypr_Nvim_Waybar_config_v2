   #!/bin/bash

   MIN_FREQ=1400000
   MID_FREQ=1700000
   MAX_FREQ=2000000

   STATE_FILE="/tmp/cpu_frequency_state"

   if [ ! -f "$STATE_FILE" ]; then
       echo "$MIN_FREQ" > "$STATE_FILE"
   fi

   CURRENT_STATE=$(cat "$STATE_FILE")

   case "$CURRENT_STATE" in
       "$MIN_FREQ")
           NEW_FREQ="$MID_FREQ"
           ;;
       "$MID_FREQ")
           NEW_FREQ="$MAX_FREQ"
           ;;
       *)
           NEW_FREQ="$MIN_FREQ"
           ;;
   esac

   sudo cpupower frequency-set -f "$NEW_FREQ" &>/dev/null
   
   echo "$NEW_FREQ" > "$STATE_FILE"

   NEW_FREQ_GHZ=$(awk "BEGIN {printf \"%.2f\", $NEW_FREQ / 1000000}")

   # Сформируйте JSON строку соблюдая порядок и формат
   echo "{\"text\": \"GHz\", \"tooltip\": \"Tap to change CPU frequency\"}"
   
