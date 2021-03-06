import sys
import random
# make boss determinist
random.seed(0)

HQ = 0
ME = 0

VOID = "#"
NEUTRAL = "."
OWN_ACTIVE_CELL = "O"
OWN_INACTIVE_CELL = "o"
OWNED_CELL = [OWN_ACTIVE_CELL, OWN_INACTIVE_CELL]
OPPONENT_ACTIVE_CELL = "X"
OPPONENT_INACTIVE_CELL = "x"

COST_UNIT = 10
WIDTH = HEIGHT = 12

def clamp_coordinates(x):
	return min(WIDTH-1, max(0, x))

nb_mines = int(input())
for i in range(nb_mines):
	x, y = [int(j) for j in input().split()]

# game loop
while True:
	gold = int(input())
	income = int(input())

	opponent_gold = int(input())
	opponent_income = int(input())

	my_hq_pos = None
	en_hq_pos = None

	for i in range(HEIGHT):
		line = list(input())

	building_count = int(input())
	for i in range(building_count):
		owner, buildingType, x, y = [int(j) for j in input().split()]

		if buildingType == HQ and owner == ME:
			my_hq_pos = (x,y)
		if buildingType == HQ and owner != ME:
			en_hq_pos = (x,y)

	actions = ["WAIT"]

	my_units_count = 0
	unit_count = int(input())
	for i in range(unit_count):
		owner, unitId, level, x, y = [int(j) for j in input().split()]

		if owner == ME:
			my_units_count += 1
			actions.append("MOVE {} {} {}".format(unitId, clamp_coordinates(x+random.choice([1, -1])), clamp_coordinates(y+random.choice([1, -1]))))

	# only one unit for wood 3 boss
	if my_units_count == 0 and gold >= COST_UNIT:
		if my_hq_pos[0] == 0:
			spawn_point_x = 1
			spawn_point_y = 0
		else:
			spawn_point_x = my_hq_pos[0]-1
			spawn_point_y = my_hq_pos[1]
		actions.append("TRAIN 1 {} {}".format(spawn_point_x, spawn_point_y))
	print(";".join(actions))
