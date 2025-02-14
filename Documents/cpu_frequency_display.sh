#!/bin/bash

# Получение текущей установленной частоты
CURRENT_FREQ=$(cpupower frequency-info -fm | grep -oP '\d+\.\d+' | awk '{print int($1 * 1000000)}')

CURRENT_FREQ_GHZ=$(awk "BEGIN {printf \"%.2f\", $CURRENT_FREQ / 1000000}")

# Возвращаем JSON с текущей частотой
echo "{\"text\": \"${CURRENT_FREQ_GHZ}\", \"tooltip\": \"Current CPU frequency\"}"
