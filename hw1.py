from PIL import Image
from numpy import asarray
import numpy as np

def read(img):
    # load the image
    image = Image.open(img)
    # convert image to numpy array
    data = asarray(image)
    # print(data.shape)
    # 轉為陣列
    image2 = Image.fromarray(data)
    print(image2.mode)
    # 灰度图像 => L
    # print(image2.size)
    # print(data)
    # print(len(data))
    return data

def noise_mean(arr):
    clean_img = []
    ls = []
    for row in range(len(arr)):
        for col in range(len(arr)):
            # print(row, col)
            if row == len(arr) - 1 and col == len(arr) - 1:
                mean = int(arr[row][col]) 
                mean = mean / 2
                ls.append(mean)
            elif row == len(arr) - 1:
                mean = int(arr[row][col]) + int(arr[row][col+1]) 
                mean = int(mean) / 2
                ls.append(mean)
            elif col == len(arr) - 1:
                mean = int(arr[row][col]) + int(arr[row+1][col]) 
                mean = int(mean) / 2
                ls.append(mean)
            else:
                mean = int(arr[row][col]) + int(arr[row][col+1]) + int(arr[row+1][col]) + int(arr[row+1][col+1])
                mean = int(mean) / 4
                ls.append(mean)
            mean = 0
        clean_img.append(ls)
        ls = []
    np_arr = np.array(clean_img)
    print(np_arr.shape)

    return np_arr
      
if __name__ == '__main__':
    arr = read('noise_img.jpg')
    img_arr = noise_mean(arr)
    data = Image.fromarray(img_arr)
    data = data.convert("L")
      
    # saving the final output 
    # as a PNG file
    data.save('clean.png')
'''
python處理圖像時，可能會涉及到兩幅圖像的像素值之間的加法和減法。另外值得注意的是，圖像的像素值是ubyte類型的，ubyte類型的數據范圍是0~255

***加減需 轉換型態 整數***

'''