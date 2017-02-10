import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random

myID, game_map = hlt.get_init()
hlt.send_init("SaltBot")
CARDINALS = [NORTH, EAST, SOUTH, WEST]

def findNearestOther(square):
  direction = NORTH
  maxDistance = min(game_map.width,game_map.height)/2

  for thisDirection in CARDINALS:
    distance = 0
    current = square
    site = game_map.get_target(current, thisDirection)
    while ((site.owner == myID) and (distance < maxDistance)):
      distance += 1
      current = site
      site = game_map.get_target(current, thisDirection)

    if distance < maxDistance:
      direction = thisDirection
      maxDistance = distance

  return direction

def assignMove(square):
  squareIsBorder = False
  for direction, neighbor in enumerate(game_map.neighbors(square)):
    if neighbor.owner != myID:
      squareIsBorder=True
      if neighbor.strength < square.strength:
        return Move(square,direction)

  if square.strength < 5 * square.production:
    return Move(square, STILL)
  elif not squareIsBorder:
    return Move(square, findNearestOther(square))
  else:
    return Move(square,STILL)

while True:
    game_map.get_frame()
    moves = [assignMove(square) for square in game_map if square.owner == myID]
    hlt.send_frame(moves)
