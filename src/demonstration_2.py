"""
You are given a 2d grid of `"1"`s and `"0"`s that represents a "map". The
`"1"`s represent land and the `"0"s` represent water.

You need to write a function that, given a "map" as an argument, counts the
number of islands. Islands are defined as adjacent pieces of land that are
connected horizontally or vertically. You can also assume that the edges of the
map are surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

-Edges create relationships to vertices
-it's a graph bc there are edges and vertices
-try depth first traversal and find maybe 1 island
"""

grid = {
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]
  }

def get_neighbors(grid, start_row, start_col):
  #check up
  if start_row > 0 and grid[start_row -1][start_col] == 1:
    neighbors.add((start_row -1, start_col))

  #check down
  if start_row < len(grid)-1 and grid[start_row +1][start_col] == 1:
    neighbors.add((start_row +1, start_col))

  #check left
  if start_col > 0 and grid[start_row][start_col - 1] == 1:
    neighbors.add((start_row, start_col -1))

  #check right
  if start_col < len(grid[start_row])-1 and grid[start_row][start_col + 1] == 1:
    neighbors.add((start_row, start_col +1))

  return neighbors
print(get_neighbors(grid, 3, 3))

  






def dft_helper(grid, start_row, start_col, visited):
  # This will traverse the grid
  stack = []
  visited = set()

  stack.append((start_row, start_col))
  while len(stack)>0:
    current_row, current_col = stack.pop()
    #pop item off stack
    if (current_row, current_col) in visited:
      continue

    visited.add((current_row, current_col))

    for neighbor in get_neighbors(grid, current_row, current_col):
      stack.append(neighbor)



def numIslands(grid):
  num_islands = 0
  #Loop through each item in the array
  #two loops, row and column
  visited = set()
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      current_item = grid[row][col]
      if current_item == 1 and (row, col) not in visited:
      # The current item is a 1! We found land
      # Traverse teh grid, starting from current row/ col
        dft_helper(grid, row, col, visited)
        num_islands +=1
    
  return num_islands


  

  print(numIslands(grid))


    

