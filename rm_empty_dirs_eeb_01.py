#! /usr/bin/python

'''
removes empty directories

Directories that contain neither files nor subdirectories
are listed and optionally removed.

a start path should be supplied as the first argument to the script

To remove empty nested directories, the script can be run repeatedly.

January 2021
ebaetscher@protonmail.com
'''

import os, sys
from pathlib import Path
import shutil

#hard_code_start_path = Path(r'/home/eb/Documents/FPA2_acerS3/AIRC/R24_macaque')
#dicoms_path = hard_code_start_path / r'R24_study_dicoms'

def remove_empty_dirs(start_path):
	if start_path.is_dir():
		dirs = []
		empty_dirs = []

		for path_i in list(start_path.rglob('*')):
			if path_i.is_dir():
				dirs.append(path_i)
				if len(list(path_i.iterdir())) < 1:
					empty_dirs.append(path_i)
			
		if len(empty_dirs) < 1:
			print('no empty dirs under start_path')
		
		else:
			print(empty_dirs)

			print("do you want to remove the above dirs?")
			input_i = input("(y / n):")
			#print(input_i)
			if input_i == 'y':
				for empty_dir_i in empty_dirs:
					empty_dir_i.rmdir()
				print("dirs removed")
			else:
				print("dirs not removed")

	else:
		print('remove_empty_dirs function takes a')
		print('path to a dir as argument')

def main():
	try:
		start_path = Path(sys.argv[1])
	except IndexError:
		print('no argument given')
		print('please give path to search for empty dirs')
		return
	
	remove_empty_dirs(start_path)
	

if __name__ == '__main__':
	main()
	print('done')
