import cv2
import os
import shutil

def get_color(x, y):
    font = cv2.FONT_HERSHEY_SIMPLEX
    b = img[y, x, 0]
    g = img[y, x, 1]
    r = img[y, x, 2]
    print(r,g,b)
    cv2.putText(img, str(b) + ',' +
                str(g) + ',' + str(r),
                (x,y), font, 1,
                (255, 255, 0), 2)
    
    return r,g,b
 
# driver function
if __name__=="__main__":
    
    # reading the image
    folder = r"D:\Saud\Folder\Images"
    #creating loop to iterate through photos
    for filename in os.listdir(folder):
        img = cv2.imread(r"D:\Saud\Folder\Images\%s"%(filename), 1)
        try:
            r,g,b = get_color(x = 32,y = 18)
            if r == 250 and g == 250 and b == 250:
                print("#FAFAFA")
                os.remove(os.path.join(folder,filename))
            else:
                print("Keeping the file")
        except:
            shutil.move(filename, r"D:\Saud\Folder\Crash_images")
    cv2.destroyAllWindows()
