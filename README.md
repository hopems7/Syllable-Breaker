# Syllable-Breaker
This program processes Thai text. It takes three arguments consisting of a category file, the input file used to test the program, and the designated output file. There are two functions: main and a function to map the category file into a dictionary. In main, an FSA is created and used to break syllables. The program loops through the input file line by line, breaking syllables depending on the FSA state. The segmented output is then written to the output file. 
