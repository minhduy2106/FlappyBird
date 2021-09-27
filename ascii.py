import PIL.Image
import os

#ascii characters used to build the output next
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", "n", "M", "D", "O"]

#resize image according to a new width
def resize_image(image, new_width=75):
    (width, height) = image.size
    ratio = height / float(width)
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

#convert each pixel to grayscale
def grayify(image):
    return image.convert("L") 

#pixel to ASCII characters
def pixel_to_ascii(image, range_width = 75):
    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[pixel_value//range_width] for pixel_value in pixels_in_image]
    return "".join(pixels_to_chars)

#convert pixels to a string of ASCII characters
def image_to_ascii(image, new_width = 75):
    image = resize_image(image)
    image = grayify(image)
    pixels_to_chars = pixel_to_ascii(image)
    len_pixels_to_chars = len(pixels_to_chars)
    image_ascii = [pixels_to_chars[index : index + new_width] for index in range(0,len_pixels_to_chars, new_width)]
    return "\n".join(image_ascii)


def main():
    path = input("Enter a valid pathname to an image : \n")

    try:
        image = PIL.Image.open(path)
    except:
        print(path,"is not a valid path name")

    print(image_to_ascii(image))
    with open("be.docs", "w") as file:
        file.write(image_to_ascii(image))


main()