# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename): #filename = name of image you want to open
    pic = Image.open(filename)
    return pic

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(pic): #image, already opened, you want to show
    pic.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(pic, filename):
    pic.save(filename, "jpeg")


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(pic):
    data = pic.getdata()
    new_pixels = []

    darkBlue = (0,51,76)
    red = (217,26,33)
    lightBlue = (112,150,158)
    yellow = (252,227,166)

    for item in data:
        intensity = item[0] + item[1] + item[2]
        if (intensity < 182):
            new_pixels.append(darkBlue)
        elif (intensity >= 182 and intensity <= 364):
            new_pixels.append(red)
        elif (intensity >= 364 and intensity <= 546):
            new_pixels.append(lightBlue)
        elif (intensity > 546):
            new_pixels.append(yellow)

    newpic = pic
    newpic.putdata(new_pixels)
    return newpic

def invertColors(pic):
    data = pic.getdata()
    new_pixels = []

    for item in data:
        newColor = (255-item[0],255-item[1],255-item[2])
        new_pixels.append(newColor)

    newpic = pic
    newpic.putdata(new_pixels)
    return newpic

def grayscale(pic):
    data = pic.getdata()
    new_pixels = []

    for item in data:
        average = ((item[0] + item[1] + item[2])//3)
        newColor = (average,average,average)
        new_pixels.append(newColor)

    newpic = pic
    newpic.putdata(new_pixels)
    return newpic
