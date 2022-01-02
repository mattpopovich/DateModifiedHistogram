# About: Displays a 24hr histogram based on when the files in the folder 
# 		 selected were modified
# Author: Matt Popovich (https://mattpopovich.com/)
# Date Created: December 23, 2019
# Tested Python Version: 3.7.4


# --- Imports ---
import os.path
import time
import datetime 
import matplotlib.pyplot as plt
import numpy as np

from tkinter.filedialog import askdirectory


# --- Functions ---
# Returns epoch time the file_path was last modified 
def parse_file(file_path):
	file_epoch = os.path.getmtime(file_path)
	# print("Parsing file: " + str(file_path) + " with epoch: " + str(file_epoch))
	return file_epoch


# Returns an array of epoch times from files in data_dir
def parse_folder(data_dir): 
	# print("Parsing folder: " + str(data_dir))
	filesArr = os.listdir(data_dir)

	folder_times = [] 

	for file_name in os.listdir(data_dir):
		if file_name[0] == '.':
			print("Skipping file: " + str(file_name))
			continue # Skip processing this file
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

	return folder_times

# Plots histogram given numpy array of epoch times in folder_times
def generate_histogram(data_dir, folder_times):
	folder_name = os.path.basename(data_dir)

	file_seconds = []

	for t in folder_times:
		# print("t: " + str(t))
		H = int(datetime.datetime.fromtimestamp(t).strftime('%H'))
		M = int(datetime.datetime.fromtimestamp(t).strftime('%M'))
		S = int(datetime.datetime.fromtimestamp(t).strftime('%S'))
		# print("H: {}, M: {}, S: {}".format(H, M, S))
		total_minutes = (H * 60) + M
		total_seconds = (total_minutes * 60) + S
		file_seconds.append(total_seconds)

	sec_in_hour = 60 * 60
	sec_in_day = sec_in_hour * 24

	# print("file_seconds: " + str(file_seconds))

	file_hours = np.array(file_seconds) / sec_in_hour

	print("file_hours: " + str(file_hours))

	num_bins = 23
	n, bins, patches = plt.hist(file_hours, num_bins)
	print("n: " + str(n))
	print("len n: " + str(len(n)))
	print("bins: " + str(bins))
	print("len bins: " + str(len(bins)))
	print("patches: " + str(patches))
	plt.xlabel('Hour of the day')
	plt.ylabel('Occurrences')
	plt.title(folder_name)
	plt.xticks(np.arange(0, 25, 1))
	plt.show()


# --- Declarations --- 
dataDir = askdirectory()


# --- Main Code ---
folder_times = parse_folder(dataDir) 
print("folder_times for folder '" + dataDir + "' = " + str(len(folder_times)))
# print("folder_times values: " + str(folder_times))

generate_histogram(dataDir, folder_times)

