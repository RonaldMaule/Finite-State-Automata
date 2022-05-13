A configuration file contains the start state on the first line and the final states on the second line (seperated by commas). After that, each line specifies a transitions of the form: current_state, input_character, next state.

Important to note:
  Whitespace is ignored in the configuration files. However, state names cannot contain whitespace.
  
  '#' denotes a comment and everything after is ignored.
  
  Any characters can be used to denote an input character in the transitions (except whitespace). These can only be one character long.
  
  Any strings can be used to name a state as long as they do not contain whitespace. It is possible to use the same character in the input and as a state name but this is not recommended.

Please refer to the example configuration file. Also, please refer to the test cases at the bottom of DFA_lib to see examples of how to use the DFA object.
