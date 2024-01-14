- usage: python asm.py<file>, read in<file> from command line parameter

- replace '...' occurances with ASCII code(s)
- delete ; comments
- replace ; with space
- process and cut preprocessor commands like #org
- cut & store <label>: definitions in a <label>  => line number dictionary
- split line into a list where each list element represents a byte
- replace mnemonics with opcodes
- replace 16-bit words with LSB MSB

- insert a placeholder after each label referance for the address MSB
- calculate the adress of each line
- updae dictionary from <label> => linenumber to <label> => address

- replace 'label referance + placeholder' with adress 'MSB LSB'
- check if remaining elements are numeric, if not display error message

- print out the result

