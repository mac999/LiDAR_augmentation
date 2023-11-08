# pcd_augmentation
Point Cloud Data (Scan) Augmentation</br>
<p align="center">
<img height="300" src="https://github.com/mac999/pcd_augmentation/blob/main/doc/test1.PNG"/>
</p>

# version
0.1: initial veraasion

# run
python [options]</br>
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

# description
Point Cloud Data (Scan) Augmentation for the purpose of improving diversity of scan dataset and saving labeing cost.




