# Compressor
Image Compressor using Linear Algebra and File Directory Scanning

1. When you run the file, the script will ask you to specify a directory.
   For example, /Users/Daniel/Pictures would bring a user called Daniel to the 
   "Pictures" folder on their computer.

2. All image files in that directory will be identified. The script will ask
   you each time it identifies an image if you want to compress that image.
   If yes, a new compressed image will be created in the same directory.
   
3. A technique called Singular Value Decomposition (SVD) was used to compress
   the images. NumPy, a popular data science library has a function for this.
