#!/bin/bash

brightness=$(brightnessctl get)  # Получение текущего уровня яркости
max_brightness=$(brightnessctl max)  # Получение максимального уровня яркости
percent=$((brightness * 100 / max_brightness))  # Вычисление процента яркости

echo "{\"text\": \"$percent%\", \"tooltip\": \"BrightnessLevel: $percent%\"}"
