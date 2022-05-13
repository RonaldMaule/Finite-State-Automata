from Transitions import TransitionSet as TSet

class DFA:
	def __init__(self, config_file:str = None) -> None:
		self.delta = TSet()		# Transistions
		self.q0 = None			# Start state
		self.F = set()			# Final states

		if config_file is None:
			raise RuntimeError("Must specify a configuration file when initializing a DFA.")
		
		self.Setup(config_file)
	
	# Read in start state, final state, and transitions
	def Setup(self, config_file:str) -> None:
		with open(config_file, 'r') as conf:
			line = conf.readline().split('#')	# Ignore comments

			if line[0].isspace() or line[0] == '':
				raise RuntimeError("No start state specified.")
				
			self.q0 = line[0].strip()			# Set start state

			line = conf.readline().split('#')			# Ignore comments
			f_states = line[0].split(',')				# Set final states
			self.F = {x.strip() for x in f_states}		# Ignore whitespace

			while init_line := conf.readline():
				line = init_line.split('#')				# Ignore comments
				if line[0].isspace() or line[0] == '': continue		# Ignore empty lines
				
				line = line[0].split(',')
				line = [x.strip() for x in line]		# Convert line to [curr_state, char, next_state]

				if len(line) != 3:
					raise RuntimeError(f"Formatting error in the following line: {init_line}")

				self.delta.add(line)
	
	def Run(self, input:str = "") -> bool:
		init_in = input			# Save input for error handling

		curr_state = self.q0
		while input:	# Run through input moving from state to state
			char = input[0]

			try:		# Find next state and set it to current state
				chars_dict = self.delta.get(curr_state)
				curr_state = chars_dict[char]
			except KeyError:
				raise KeyError(f"No transitions from state {curr_state} with letter {char} for input {init_in}.")
			
			input = input[1:]		# Remove rightmost char from input string
		
		if curr_state in self.F:	# If we halt in final state then accept else reject
			return True
		else:
			return False

if __name__ == "__main__":
	try:
		bad = DFA()
		raise Exception("Initializing without config_file did not raise RuntimeError")
	except RuntimeError:
		pass

	test = DFA("config_ex.txt")

	try:
		test.Run("hello")
		raise Exception("No KeyError when using a transition that does not exist.")
	except KeyError:
		pass

	assert test.Run("ba") is True
	assert test.Run("bbb") is True
	assert test.Run("") is False
	assert test.Run("aaa") is False