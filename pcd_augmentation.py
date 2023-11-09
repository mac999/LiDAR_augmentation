# name: pcd_augmentation
# author: taewook kang (laputa99999@gmail.com)
# date: 2023.09.20
# description: perform data augmentation on a given dataset
# version: 0.2
#
import sys, os, io, traceback, json, subprocess, argparse, glob, re, numpy as np
import open3d as o3d

def noising(data, prob):
	if np.random.uniform() < prob:
		data[:,:3] += np.random.normal(0, 0.01, size=data[:,:3].shape)

def scaling(data, prob):
	if np.random.uniform() < prob:
		data[:,:3] *= np.random.uniform(0.9, 1.1)

def translating(data, prob):
	if np.random.uniform() < prob:
		data[:,:2] += np.random.normal(0, 0.01, size=data[:,:2].shape)

def rotating(data, prob):
	if np.random.uniform() < prob:
		angle = np.random.uniform(0, 360)
		rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
		data[:,:2] = data[:,:2].dot(rotation_matrix)

def rgb_noising(data, prob):
	if np.random.uniform() < prob:
		data[:,3:] += np.random.randint(-5,5,size=data[:,3:].shape)

def rgb_light_effect(data, prob):
	if np.random.uniform() < prob:
		data[:,3:] += np.random.normal(0, 20, size=data[:,3:].shape)
		data[:,3:] = np.clip(data[:,3:], 0, 255)

# def LoD
# def LiDAR simulation

def main():
	parser = argparse.ArgumentParser(description='Perform data augmentation on a given dataset.')
	parser.add_argument('--input_folder', type=str, default="./input", help='the path to the input folder')
	parser.add_argument('--output_folder', type=str, default="./output", help='the path to the output folder')
	parser.add_argument('--noising', type=float, default=0.5, help='the probability of performing noising (default: 0.50)')
	parser.add_argument('--scaling', type=float, default=0.5, help='the probability of performing scaling (default: 0.50)')
	parser.add_argument('--translating', type=float, default=0.0, help='the probability of performing translating (default: 0.50)')
	parser.add_argument('--rotating', type=float, default=0.5, help='the probability of performing rotating (default: 0.50)')
	parser.add_argument('--rgb_noising', type=float, default=0.5, help='the probability of performing RGB noising (default: 0.50)')
	parser.add_argument('--rgb_light_effect', type=float, default=0.5, help='the probability of performing RGB light effect (default: 0.50)')
	parser.add_argument('--aug_num', type=int, default=50, help='number of the augmentation of each class')
	args = parser.parse_args()
	
	os.makedirs(args.output_folder, exist_ok=True)

	# get files in the input folder
	input_files = os.listdir(args.input_folder)
	for fname in input_files:
		path = os.path.join(args.input_folder, fname)
		# pcd = o3d.io.read_point_cloud(path, format='xyzrgb')
		# pcd = np.asarray(pcd.points)
		pcd_data = np.loadtxt(path, delimiter=' ')
		pcd_count = len(pcd_data)
		if pcd_count == 0:
			continue

		noising(pcd_data, args.noising)
		scaling(pcd_data, args.scaling)
		translating(pcd_data, args.translating)
		rotating(pcd_data, args.rotating)
		rgb_noising(pcd_data, args.rgb_noising)
		rgb_light_effect(pcd_data, args.rgb_light_effect)

		name = fname.split('.')[0]
		ext = fname.split('.')[1]
		
		pcd_data[:,3:] = pcd_data[:,3:].astype(int)

		output_file_path = os.path.join(args.output_folder, name + ".pcd") # ".xyzrgb")

		pcd = o3d.geometry.PointCloud()
		pcd.points = o3d.utility.Vector3dVector(pcd_data[:,:3])
		pcd.colors = o3d.utility.Vector3dVector(pcd_data[:,3:] / 255.0)
		o3d.io.write_point_cloud(output_file_path, pcd) #, write_ascii = True, format='xyzrgb')

		print("Saved {} points to {}".format(pcd_count, output_file_path))
		
if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		traceback.print_exc()
