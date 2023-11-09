import sys, os, io, traceback, json, subprocess, argparse, glob, re, numpy as np, sklearn, matplotlib.pyplot as plt, open3d as o3d
import laspy, copy, pandas as pd
import trimesh
from jakteristics import FEATURE_NAMES, extension, las_utils, utils
from pathlib import Path
from tqdm import tqdm
from pathlib import Path
import ifcopenshell
import ifcopenshell.util.element
import ifcopenshell.util.placement
import ifcopenshell.util.representation
from ifcopenshell import geom

data_dir = Path(__file__).parent / "data"
  
def compute_features(input_path, output_path):
    '''
        FEATURE_NAMES = [
            "eigenvalue_sum",
            "omnivariance",
            "eigenentropy",
            "anisotropy",
            "planarity",
            "linearity",
            "PCA1",
            "PCA2",
            "surface_variation",
            "sphericity",
            "verticality",
            "nx",
            "ny",
            "nz",
            "number_of_neighbors",
            "eigenvalue1",
            "eigenvalue2",
            "eigenvalue3",
            "eigenvector1x",
            "eigenvector1y",
            "eigenvector1z",
            "eigenvector2x",
            "eigenvector2y",
            "eigenvector2z",
            "eigenvector3x",
            "eigenvector3y",
            "eigenvector3z",
        ]   
    '''
    
    xyz = las_utils.read_las_xyz(input_path)
    features = extension.compute_features(xyz, 0.1, feature_names=FEATURE_NAMES)
    print(features)
    
    las_utils.write_with_extra_dims(input_path, output_path, features, FEATURE_NAMES)

def main():
    global data_dir

    parser = argparse.ArgumentParser()
    parser.add_argument('--input_pcd', default="sample.las", type=str, required=False)
    parser.add_argument('--output', default="output.las", type=str, required=False)
    args = parser.parse_args()
    
    compute_features(args.input_pcd, args.output)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_exc()