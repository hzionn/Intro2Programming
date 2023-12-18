"""
Problem Solving

Construct algorithm with given constraints to solve the problem.
Print out your calculation.
"""

# declare constants
TOTAL_WIDTH = 100
TILE_WIDTH = 5

# first and last one have to be black tile
# then place black and white interchangeably
n_pairs = int((TOTAL_WIDTH - TILE_WIDTH) / (2 * TILE_WIDTH))
print(f"number of pairs: {n_pairs}")

n_tiles = 1 + (2 * n_pairs)
print(f"number of tiles: {n_tiles}")

total_gap = TOTAL_WIDTH - n_tiles * TILE_WIDTH
print(f"total gap: {total_gap}")

each_gap = total_gap / 2
print(f"each gap: {each_gap}")
