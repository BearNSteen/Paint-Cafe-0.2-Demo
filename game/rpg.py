import random

class Character:

	def __init__(self, name, align, tree=None):
		self._name = name
		self._alignment = align
		# align 1 is good, align 2 is enemy
		if align == 1:
			self._level = 1
			self._maxhp = tree[self._level][0]
			self._health = tree[self._level][0]
			self._strength = tree[self._level][1]
			self._defense = tree[self._level][2]
			self._maatk = tree[self._level][3]
			self._madef = tree[self._level][4]
			self._speed = tree[0][1]
			self._luck = tree[0][2]
			self._xp = 0
			self._attacks = tree[0][3]
			if tree == None:
				print("Character has no tree. This is an error.")
			else:
				self._tree = tree
		elif align == 2:
			self._health = tree[1]
			self._strength = tree[2]
			self._defense = tree[3]
			self._maatk = tree[4]
			self._madef = tree[5]
			self._speed = tree[6]
			self._luck = tree[7]
			self._xp = tree[8]
			self._attacks = [Attack('Punch', 5, 'Light'), None, None, None]

	def get_name(self):
		return self._name

	def get_hp(self):
		return self._health

	def get_strength(self):
		return self._strength

	def get_defense(self):
		return self._defense

	def get_magic_attack(self):
		return self._maatk

	def get_magic_defense(self):
		return self._madef

	def get_speed(self):
		return self._speed

	def get_luck(self):
		return self._luck

	def get_attacks(self):
		return self._attacks

	def get_xp(self):
		return self._xp

	def gain_xp(self, xp):
		self._xp += xp
		if self._xp >= self._tree[self._level][5]:
			self.level_up
			return True
		return None

	def get_alignment(self):
		return self._alignment

	def level_up(self):
		self._level += 1
		self._health = self._tree[self._level][0]
		self._strength = self._tree[self._level][1]
		self._defense = self._tree[self._level][2]
		self._maatk = self._tree[self._level][3]
		self._madef = self._tree[self._level][4]

class Attack():

	def __init__(self, name, damage, element):
		self._name = name
		self._damage = damage
		self._element = element

	def get_name(self):
		return self._name

	def get_damage(self):
		return self._damage

	def get_element(self):
		return self._element


def compute_damage(fighter, attack, target):
	"""
	Returns the amount of damage that the attack should deal.
	"""
	damage = attack.get_damage()
	processed_dmg = damage + fighter.get_strength() - target.get_defense()
	if processed_dmg < 0:
		final_damage = 0
	else:
		final_damage = processed_dmg
	return final_damage

def turn_order(party, enemy):
    speeds = []
    for member in party:
        speeds.append([member.get_name(), member.get_speed(), member])
    for baddie in enemy:
        if baddie != None:
            speeds.append([baddie.get_name(), baddie.get_speed(), baddie])
    counter = 10
    turn_order = []
    while counter != 0:
    	this_turn = []
        for unit in speeds:
            if unit[1] == counter:
                this_turn.append(unit)
        if len(this_turn) > 0:    
            if len(this_turn) > 1:
                random.shuffle(this_turn)
                for unit in this_turn:
                    turn_order.append(unit)
            else:
                turn_order.append(this_turn[0])
        counter -= 1
    return turn_order

# Notes on trees:
# The first line in a tree [0] is the character's element.
# The lines following [1] are each level of that character's development.

# Dane Tree
dane_tree = [
	# Element, Speed, Luck
	["Bright", 3, 5, [Attack("Slice", 10, "Bright"), None, None, None]],
	#Level 1
	[20, 10, 10, 0, 0, 10],
	#Level 2
	[26, 12, 12, 0, 0, 20],
	#Level 3
	[32, 14, 14, 0, 0, 30]
]


# Ellie Tree
ellie_tree = [
	# Element, Speed, Luck
	["Night", 7, 5, [Attack("Blast", 15, "Night"), None, None, None]],
	#Level 1
	[10, 2, 2, 10, 10, 10],
	#Level 2
	[14, 2, 2, 10, 10, 15],
	#Level 3
	[18, 2, 2, 10, 10, 20]
]

westra_tree = [
	# Element, Speed, Luck
	["Heat", 5, 5, [Attack("Bolt", 15, "Heat"), None, None, None]],
	#Level 1
	[15, 0, 0, 12, 12, 10],
	#Level 2
	[20, 0, 0, 15, 15, 15],
	#Level 3
	[25, 0, 0, 18, 18, 20]
]

rock_tree = [
	# Element, Speed, Luck
	["Mist", 8, 5, [Attack("Stab", 15, "Mist"), None, None, None]],
	#Level 1
	[15, 12, 4, 0, 0, 10],
	#Level 2
	[18, 15, 5, 0, 0, 15],
	#Level 3
	[21, 18, 6, 0, 0, 20]
]

player_tree = [
	# Element, Speed, Luck
	["Bright", 3, 5, [Attack("Slice", 10, "Bright"), None, None, None]],
	#Level 1
	[20, 10, 10, 0, 0, 10],
	#Level 2
	[26, 12, 12, 0, 0, 15],
	#Level 3
	[32, 14, 14, 0, 0, 20]
]

rock_char = Character("Rock", 1, rock_tree)
dane_char = Character("Dane", 1, dane_tree)
ellie_char = Character("Ellie", 1, ellie_tree)
westra_char = Character("Westra", 1, westra_tree)

# Attack - Defense - Magic - Magic Defense - Speed - Luck - XP
# Enemies - 	   Element	HP  	A 	D 	M 	MD 	S 	L 	XP
heat_goblin 	= ["Heat", 	10, 	5, 	5, 	0, 	0, 	4, 	5, 	5	]
wet_goblin 		= ["Wet",	10, 	7,	3,	0,	3,	6,	5, 	5	]
grass_goblin	= ["Soil",	10, 	3,	3,	0, 	10, 5, 	5, 	5	]
big_goblin		= ["Dark",	300,	10,	10,	0,	15,	8,	5,	20	]
