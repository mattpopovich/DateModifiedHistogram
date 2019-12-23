# About: Creates multiple histograms based on when your files were modified
# Author: Matt Popovich
# Date Created: December 23, 2019
# Tested Python Version: 3.7.4



# --- Imports ---
import os.path
import time
import datetime 



# --- Functions ---
# Returns epoch time the file_path was last modified 
def parse_file(file_path):
	# print("Parsing file: " + str(file_path))
	file_epoch = os.path.getmtime(file_path)
	return file_epoch



# Returns an array of epoch times from files in folder, produce histograms 
def parse_folder(data_dir): 
	# print("Parsing folder: " + str(data_dir))
	filesArr = os.listdir(data_dir)

	folder_times = [] 



	for file_name in os.listdir(data_dir):
		abs_path = data_dir + '/' + file_name

		# print("Parsing file/folder: " + str(abs_path))

		if os.path.isdir(abs_path):
			# print("is dir")
			for f in parse_folder(abs_path):
				folder_times.append(f)
		elif os.path.isfile(abs_path):
			# print("is file")
			folder_times.append(parse_file(abs_path))
		else:
			print("ERROR: File path '" + str(abs_path) + "' is neither a file or folder...")

		new_dir = False

	#generate_histogram(data_dir, folder_times)
	print("folder_times for folder '" + data_dir + "' = " + str(len(folder_times)))
	print("folder_times values: " + str(folder_times))
	return folder_times


def generate_histogram(data_dir, folder_times):
	folder_name = os.path.basename(data_dir)

	datetime.datetime.fromtimestamp(os.path.getmtime(var)).strftime('%Y-%m-%d %H:%M:%S')






# --- Declarations --- 
dataDir = '/Volumes/FAT32_4/2019 TrailCam/test'



# --- Main Code ---
parse_folder(dataDir) 



		



