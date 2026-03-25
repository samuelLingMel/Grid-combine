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
example_grid2 = [
    ["metal","","ruby",""],
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

example_material3 = [
    ["ruby"],
    ["ruby"],
    ["ruby"],
    ["ruby"]
]

example_material4 = [
    ["ruby","ruby","ruby","ruby"]
]

example_material5 = [
    ["ruby","ruby"],
    ["ruby","ruby"]
]

example_material6 = [
    ["ruby", ""],
    ["","ruby"],
    ["","ruby"],
    ["","ruby"]
]

print(f"1. Positive test case")
print(combine_grids(example_grid, example_material))

print(f"2. Negative test case")
# Negative test case overlapping nodes
combine_grids(example_grid, example_material2)

print(f"3. testing coord and non 4x4 grid material vertical")
print(combine_grids(example_grid, example_material3, (2,0)))

print(f"4. testing coord and non 4x4 grid material horizontal")
print(combine_grids(example_grid, example_material4, (0,2)))

print(f"5. neg testing coord and non 4x4 grid material")
print(combine_grids(example_material, example_material4, (0,2)))

print(f"6. positive testing coord and non 4x4 grid material horizontal 3")
print(combine_grids(example_grid, example_material4, (0,3)))

print(f"7. positive testing coord and non 4x4 grid material")
print(combine_grids(example_grid, example_material5, (2,2)))

print(f"8. positive testing coord and non 4x4 grid material fit into spaces")
print(combine_grids(example_grid2, example_material6, (1,0)))

print(f"9. negative testing coord mat not fitting within 4x4 vertically")
print(combine_grids(example_grid, example_material6, (2,2)))

print(f"10. negative testing coord mat not fitting within 4x4 horizontally")
print(combine_grids(example_grid, example_material4, (2,2)))
