# About: Creates multiple histograms based on when your files were modified
# Author: Matt Popovich
# Date Created: December 23, 2019
# Tested Python Version: 2.7.10



# --- Imports ---
import os.path, time
import datetime 



# --- Functions ---
# Returns epoch time the file_path was last modified 
def parse_file(file_path):
	file_epoch = os.path.getmtime(file_path)



# Returns an array of epoch times from files in folder, produce histograms 
def parse_folder(data_dir): 
	print("Parsing folder: " + str(data_dir))
	filesArr = os.listdir(data_dir)

	folder_times = [] 



	for dirpath, _, filenames in os.walk(data_dir):
		print(str(dirpath))
		print(str(filenames))
		for d in dirpath:
			new_dir = True 
			for f in filenames:
				if new_dir: 
					print("new dir: " + d) 
				print("Parsing file/folder: " + str(f))
				abs_path = dirpath + '/' + f

				if os.path.isdir(abs_path):
					print("is dir") 
					folder_times.append(parse_folder(abs_path))
				elif os.path.isfile(abs_path): 
					print("is file")
					folder_times.append(parse_file(abs_path))
				else: 
					print("ERROR: File path '" + str(abs_path) + "' is neither a file or folder...")

				new_dir = False

	#generate_histogram(data_dir, folder_times)

	return folder_times


def generate_histogram(data_dir, folder_times):
	folder_name = os.path.basename(data_dir)

	datetime.datetime.fromtimestamp(os.path.getmtime(var)).strftime('%Y-%m-%d %H:%M:%S')






# --- Declarations --- 
dataDir = '/Volumes/FAT32_4/2019 TrailCam'



# --- Main Code ---
parse_folder(dataDir) 



		



