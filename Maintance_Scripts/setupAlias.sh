#!/bin/bash

NEW_ALIASES=(
  "alias setup='~/GNGC-CYBER-RANGE/setup.sh'"
  "alias update='cd ~ && rm -r GNGC-CYBER-RANGE/ && git clone https://github.com/Fox2low/GNGC-CYBER-RANGE'"
  "alias start='~/GNGC-CYBER-RANGE/start.sh'"
  "alias stop='~/GNGC-CYBER-RANGE/stop.sh'"
  "alias restart='~/GNGC-CYBER-RANGE/stop.sh && ~/GNGC-CYBER-RANGE/start.sh'"
)

append_aliases() {
  for alias_line in "${NEW_ALIASES[@]}"; do
    if grep -qF "$alias_line" ~/.bashrc; then
      echo "Alias already exists: $alias_line"
    else
      echo -e "\n# Custom Aliases" >> ~/.bashrc
      echo "$alias_line" >> ~/.bashrc
      echo "Alias added to ~/.bashrc: $alias_line"
    fi
  done

  source ~/.bashrc
}

append_aliases

