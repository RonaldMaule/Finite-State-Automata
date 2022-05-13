from DFA_lib import DFA
import sys

# Check for proper command line arguments
if not (len(sys.argv) == 2 or len(sys.argv) == 3):
	raise RuntimeError("Formatting error. Program called with: DFA.py [config_file] [input]")

config_file = sys.argv[1]
if len(sys.argv) == 3:	# Allow for "" as input
	input = sys.argv[2]
else:
	input = ""

user_dfa = DFA(config_file)
if user_dfa.Run(input):
	print(f"DFA accepted the string: {input}")
else:
	print(f"DFA rejected the string: {input}")