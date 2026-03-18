from combine_grid import combine_grids
grid = [
    ["","","",""],
    ["","","",""],
    ["","","",""],
    ["","","",""]
]

example_grid = [
  ["metal","ruby","",""],
  ["","ruby","",""],
  ["","","",""],
  ["","","",""]
]

example_material = [
  ["","","ruby",""],
  ["","","ruby",""],
  ["","","ruby",""],
  ["","","ruby",""]
]

example_material2 = [
  ["","ruby","ruby",""],
  ["","","ruby",""],
  ["","","ruby",""],
  ["","","ruby",""]
]

# Positive test case
print(combine_grids(example_grid, example_material))

# Negative test case overlapping nodes
combine_grids(example_grid, example_material2)
