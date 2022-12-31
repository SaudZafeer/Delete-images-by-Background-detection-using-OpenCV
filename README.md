# Delete-images-by-Background-detection-using-AI:
## ABOUT:
Suppose you have a folder that contains thousands of images and you only want delete those images which are having #FAFAFA Hex Color or RGB: 250, 250, 250 or ALABASTER, GREY background, so obviously you'll never waste your valuable time to delete those images one by one by reading their properties, Right?!. let this AI based program handle this task.
## HOW DOES IT WORK:
By reading the python code you will see that first we need to import required libraries that are responsible to run the code.
1)Then you will see i created a function name "get_color(x,y)", The purpose of this function is to retrun the RBG values of "x" and "y" co-ordinates. Remember "x" and "y" are the co-ordinates of the images that are stored in your folder.
2)Do make sure to provide 'x' and 'y' co-ordinates of such location where your background is clear to detect.
Now once you have pass your co-ordinates the program will detect if that part of images contains #FAFAFA Hex Color or RGB: 250, 250, 250 or ALABASTER, GREY background. If yes the program will delete those files/image and keep only those files/image which are having different RBG values.
## WHAT IF FOLDER CONTAINS SOME CRASH IMAGES?:
Remember this program needs to open the file/image first in order to detect or delete to those crash images, and since we know that crash images could not be open, this program will automatically move those crash images into another folder.
All you need is to create a folder for crash image and pass the path of the folder to the code
## HOW YOU CAN CHANGE RBG VALUES OF YOUR CHOICE:
Lets say you don't want to delete RBG: 250,250,250 but want to delete some other RBG values of images.
Simply just go to the line no 29 and change the RBG values in "if" condition.
## Installation:
1-Open visual studio code or any code editor select a folder where you want to clone the repo.
2-Clone the Repo
```sh
https://github.com/SaudZafeer/Delete-images-by-Background-detection-using-Artificial-Intelligence-.git
```
2-Install all the required packages After cloning the code just open your terminal and copy paste the line below to get the requirement file to run the code.
```sh
pip install -r requirnments.txt
```
3-How To Create Requirnment.txt
```sh
pip freeze > Requirnment.txt
```
## Challenges:
The worst challenge was to get the co-ordinates of those images.
