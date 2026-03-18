# setting this up as a function which can be imported easily into another python script
def combine_grids(grid, material):
  # setting up empty grid to be returned in case of success
  resulting_grid = [
    ["","","",""],
    ["","","",""],
    ["","","",""],
    ["","","",""]
  ]
  
  # first loops through each square of the resulting grid with nested loops for x and y axis
  for xi in range (0,4):
    for yi in range (0,4):
    #   print(f"grid result for xi: {xi} and yi: {yi} grid: {grid[yi][xi]}")
    #   print(f"material result for xi: {xi} and yi: {yi} grid: {grid[yi][xi]}")
      if (grid[yi][xi] != "" and material[yi][xi] != ""):
        print(f"conflict in spot x: {xi} and y: {yi}")
        return("Can't combine due to overlap")
      elif (grid[yi][xi] != ""):
        resulting_grid[yi][xi] = grid[yi][xi]
      elif (material[yi][xi] != ""):
        resulting_grid[yi][xi] = material[yi][xi]
  return(resulting_grid)
