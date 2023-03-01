#!/usr/bin/env python    
# -*- coding: utf-8 -*-
#

import sys

def main():
	
	category = sys.argv[1]
	inp=sys.argv[2]
	out=sys.argv[3]
	
	#define the FSA
	fsa ={
			0:[('V1',1),('C1',2)],
			1:[('C1',2)],
			2:[('C2',3),('V2',4),('T',5),('V3',6),('C3',9),('V1',7),('C1',8)],
			3:[('V2',4),('T',5),('V3',6),('C3',9)],
			4:[('T',5),('V3',6),('C3',9),('V1',7),('C1',8)],
			5:[('V3',6),('C3',9),('V1',7),('C1',8)],
			6:[('C3',9),('V1',7),('C1',8)],
			7:1,
			8:2,
			9:0
			}
	
	#map category file to dict	
	cat_chars=catMatch(category)
	
	s_text=''			#variable for segmented text
	current_index=0
	
	with open(inp, 'r', encoding='utf8') as openfile:
		for line in openfile:
			for char in line:
				for (category,value) in fsa[current_index]:
					if char in cat_chars[category]:
						current_index=value
						break
							
				if current_index == 7 or current_index == 8:
					#break syllable before character
					s_text=s_text+' '+char
					#move to next state
					current_index=fsa[current_index]
					
				elif current_index == 9:
					s_text=s_text+char+' '
					#move to next state
					current_index=fsa[current_index]
					
				else:
					s_text=s_text+char 
					
			#write to segmented text to the output file		
			with open(out,'w',encoding='utf8') as outFile:
				outFile.write(s_text)
				
#function to map category to a list of members in a dictionary
def catMatch(category):
	with open(category, 'r', encoding='utf8') as f: 
		cat={k: v for line in f for (k, v) in [line.strip().split(" ",1)]}	
	return cat
	
if __name__ == "__main__":
	main()
