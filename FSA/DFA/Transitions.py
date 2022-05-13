class TransitionSet:
	def __init__(self):
		self.s = dict()		# dict of {curr_state : {char : next_state}}
	
	def add(self, tran:str):
		curr_state = tran[0]
		char = tran[1]
		next_state = tran[2]

		temp = dict()		# dict of {char : next_state}
		if curr_state in self.s:
			temp = self.s[curr_state]
			if char in temp:
				raise RuntimeError(f"Transition from {curr_state} with letter {char} already exists.")

		temp[char] = next_state

		self.s[curr_state] = temp
	
	def get(self, key: str):
		return self.s[key]
	
	def print(self):
		for curr, vals in self.s.items():
			print(f"{curr}")
			for key, value in vals.items():
				print(f"\t{key} : {value}")

if __name__ == "__main__":
	test = TransitionSet()

	x1 = ["q0",'a',"q1"]
	x2 = ["q5", 'b', "q0"]
	x3 = ["q0", 'b',"q1"]
	x4 = ["q0",'a',"q3"]

	print(f"Adding {x1}")
	test.add(x1)
	print(f"Adding {x2}")
	test.add(x2)
	print(f"Adding {x3}")
	test.add(x3)
	print(f"Adding {x4}")
	try:
		test.add(x4)
		raise Exception("Adding x4 did not raise a RuntimeError")
	except RuntimeError:
		pass