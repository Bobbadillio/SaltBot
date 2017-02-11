#!/bin/bash

for i in `seq 1 10`;
do
  if hash python3 2>/dev/null; then
      halite -d "30 30" "python3 MyBot.py" "python3 RandomBot.py" > game$i.log
  else
      halite -d "30 30" "python MyBot.py" "python RandomBot.py" > game$i.log
  fi
done
