#!/bin/bash

if [[ "$1" == "h" ]]; then
  echo "Usage: pokefetch [mode]"
  echo "Modes:"
  echo "  thm   - Thumbnails"
  echo "  thbc  - Thumbnails (compressed)"
  echo "  hr    - High-resolution images"
  echo "  st    - Standard images"
  echo "  c     - Center image in terminal (use with any mode)"
  echo "  n?    - ? = pokemon index number"
  echo "  h     - Show this help message"
  exit 0
fi

CENTER=false
if [[ "$1" == "c" ]]; then
  CENTER=true
  MODE="thm"
  shift
else
  MODE="$1"
fi

OUTPUT=$(python3 /home/suresh/gitclones/Pokemon/pokemonimage.py "$MODE")

NAME=$(echo "$OUTPUT" | cut -d',' -f1)
IMAGE_PATH=$(echo "$OUTPUT" | cut -d',' -f2)
IMAGE_PATH="${IMAGE_PATH/#\~/$HOME}"

echo -e "\033[1;36m ${NAME^^}\033[0m\n"

if $CENTER; then
  kitty +kitten icat --align center "$IMAGE_PATH"
else
  kitty +kitten icat --align left "$IMAGE_PATH"
fi
