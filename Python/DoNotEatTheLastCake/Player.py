class Player:
  def __init__(self, cakes):
    "constructor"
    
  # Decide who move first - player or opponent (return true if player)
  def firstmove(self, cakes):
    # games with < 2 cakes are unwinnable when going first because the starting player can always be forced into a loss condition:
    # 1 cakes
    # - pick 1 (lose, they ate the cake!)
    # - pick 2 or 3 (invalid move)
    #
    # 2 cakes
    # - pick 1 (lose, they created stalemate)
    # - pick 2 (lose, they ate the cake)
    # - pick 3 (invalid move)

    # games with remainder of 2 are unwinnable when going first because player 1 can always be forced into a loss condition:
    # e.g. 6 cakes
    # 1. p1 (5) -> c3 (2) -> (lose, stalemate)
    # 2. p2 (4) -> c3 (1) -> (lose, must eat cake)
    # 3. p3 (3) -> c2 (1) -> (lose, must eat cake)
    return True if cakes > 2 and cakes % 4 != 2 else False

  # Decide the number of cakes to eat on your turn  
  def move(self, cakes, last):
    # cakes % 4 == 0 -> choose 3, opponent must choose 2 or 1:
    #   if 1, they're in losing position, 
    #   if 2, then we pick 1 next turn to put them in losing position
    # cakes % 4 == 1 -> choose 3, opponent in losing position 
    # cakes % 4 == 2 -> not possible because of starting player's choice
    # cakes % 4 == 3 -> choose 1, computer in losing position
    return 3 if cakes % 4 < 3 else 1