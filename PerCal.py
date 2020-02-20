import itertools
"""
Given an MxN grid of integers and a point in the 0-based grid,
calculate the perimeter of the largest island to which that point belongs.
An island is a group of horizontally and vertically contiguous cells with the same value.
Example:
Grid:
---—*****———-----
| 0 * 1 * 0 | 0 |
—---*—--*———-----
| 2 * 1 * 0 | 1 |
—---*--—*****—---
| 0 * 1 | 1 * 0 |
—---*********—---
| 1 | 0 | 0 | 3 |
——————-----------
Given point: (1, 1)
The perimeter here is denoted in *'s, and would be 10.
@param grid: an MxN array of integers
@param point: (x,y) tuple where x is the coordinate which corresponds to the row and y corresponds to the column
@return: perimeter
"""

grid = [[0, 1, 0, 0], [2,1,0,1], [0, 1, 1, 0], [1,0,0,3]] # this is a 2D grid
point = [1,1] # this point is a reference key pair, [x,y] x is the index of the row, y ios the index of the column

def calculatePerimeter(grid, point):
   perimeter = 0
   # Your code goes here
   start_point = grid[point[0]][point[1]] #finds the value we need

   island_keys = get_island_keys([], start_point, grid, point)

   for point in island_keys:
     perimeter += get_square_perimeter(start_point, grid, point)

   print("Perimeter: " + str(perimeter))
   print("Island Keys: " + str(island_keys))
   
   return perimeter

def get_square_perimeter(start_value, grid, point):
  square_perimeter = 4
  x = point[0]
  y = point[1]

  try:
    if start_value == grid[x][y-1]: #left
      square_perimeter -= 1
    if start_value == grid[x][y+1]: #right
        square_perimeter -= 1
    if start_value == grid[x-1][y]: #up
        square_perimeter -= 1
    if start_value == grid[x+1][y]: #down
        square_perimeter -= 1
  except IndexError:
    pass

  return square_perimeter

def get_island_keys(island_keys, start_value, grid, point):
  x = point[0]
  y = point[1]

  island_keys.append(point)
  
  #Try/Catch to check wether a point is withing the Matrix Confines
  
  try:
    if start_value == grid[x][y-1] and [x,y-1] not in island_keys: #left
        get_island_keys(island_keys, start_value, grid, [x,y-1])
    if start_value == grid[x][y+1] and [x,y+1] not in island_keys: #right
        get_island_keys(island_keys, start_value, grid, [x,y+1])
    if start_value == grid[x-1][y] and [x-1,y] not in island_keys: #up
        get_island_keys(island_keys, start_value, grid, [x-1,y])
    if start_value == grid[x+1][y] and [x,y-1] not in island_keys: #down
        get_island_keys(island_keys, start_value, grid, [x+1,y])
  except IndexError:
    pass


  island_keys.sort()
      # Remove duplicate Keys fromt he List using itertools
  return list(island_keys for island_keys,_ in itertools.groupby(island_keys))

calculatePerimeter(grid, point)
