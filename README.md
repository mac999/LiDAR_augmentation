# pcd augmentation with features
Point Cloud Data (Scan) Augmentation</br>
<p align="center">
<img height="200" src="https://github.com/mac999/pcd_augmentation/blob/main/doc/test0.JPG"/>
<img height="200" src="https://github.com/mac999/pcd_augmentation/blob/main/doc/test2.JPG"/>
<img height="200" src="https://github.com/mac999/pcd_augmentation/blob/main/doc/test1.PNG"/>
</p>
</br>
PCD (only LAS) feature generation</br>
<p align="center">
<img height="150" src="https://github.com/mac999/pcd_augmentation/blob/main/doc/test3.JPG"/>
</p>

# version
0.1: initial veraasion
0.2: add PCD features generation source

# run
python pcd_augmentation.py[options]</br>
</br>
--input_folder: default="./input", help='the path to the input folder'</br>
--output_folder: default="./output", help='the path to the output folder'</br>
--noising: default=0.5, help='the probability of performing noising (default: 0.50)'</br>
--scaling: default=0.5, help='the probability of performing scaling (default: 0.50)'</br>
--translating: default=0.0, help='the probability of performing translating (default: 0.50)'</br>
--rotating: default=0.5, help='the probability of performing rotating (default: 0.50)'</br>
--rgb_noising: default=0.5, help='the probability of performing RGB noising (default: 0.50)'</br>
--rgb_light_effect: default=0.5, help='the probability of performing RGB light effect (default: 0.50)'</br>
--aug_num: type=int, default=50, help='number of the augmentation of each class'</br>

python pcd_feature_generation.py[options]</br>
</br>
--input: default="input.las", help='input LAS file'</br>
--output: default="output.las", help='output LAS file'</br>

# description
Point Cloud Data (Scan) Augmentation for the purpose of improving diversity of scan dataset and saving labeing cost.

# license
MIT license



