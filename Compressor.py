import numpy as np
from PIL import Image
import os

def chooseFiles():

        # This function scans the specified directory for image files. Below are lists of supported file formats and accepted responses.         
        source_dir = input("Please specify the directory of the images you would like to compress (/Users/username/etc/etc): ")
        supportedTypes = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", 
        ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", 
        ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
        confirmations = ["Y", "y", "yes", "Yes", "ya", "Ya", "YES"]

        with os.scandir(source_dir) as entries:
            for entry in entries:            
                if any(entry.name.endswith(ending) for ending in supportedTypes):
                    answer = input("Do you want to create a compressed version of: " + entry.name + "? (Y/N): ")
                    if answer in confirmations:
                        compress(entry.path)
                    else:
                        print("Ok, I will not compress " + entry.name)
            print("Finished!")


def compress(image_path):

    image = Image.open(image_path)                              # Opens the image
    imageMatrix = np.array(list(image.getdata(band=0)), float)  # Puts the pixel values in a list
    imageMatrix.shape = (image.size[1], image.size[0])          # Shapes the image using proportions of original image
    imageMatrix = np.matrix(imageMatrix)                        # Converts the 2D Array into a NumPy Matrix
    U, D, V = np.linalg.svd(imageMatrix) # NumPy SVD function that returns 3 Matrices (U, V: Orthogonal, D: 1D Singular Values)
    reconstimg = np.matrix(U[:, :1]) * np.diag(D[:1]) * np.matrix(V[:1, :])
    # Reconstructs the image using only the first singular value. Column 1 of U is multiplied by the first singular value (Diagonal Matrix)
    # The result is multiplied by row 1 of V. The result matrix is a low-rank approximation of the image. It contains the main features.
    
    filename = image_path.split(".")
    name = filename[0]
    ending = filename[1]

    image.save(f"{name}Compressed.{ending}")
    print("Image Compressed!")


chooseFiles()