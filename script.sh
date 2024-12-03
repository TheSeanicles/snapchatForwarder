#!/bin/bash
for x in {1760..1895..45}; do
  for y in {760..985..45}; do
    xdotool mousemove --sync $x $y click 3 sleep 0.1 \
    mousemove_relative --sync 0 20 click 1 sleep 0.1
  done
done