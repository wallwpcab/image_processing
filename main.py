# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



# from PIL import Image
#
# # def crop(image_path, coords, saved_loacation):
# #  print_hi("hello")
#  # image_obj = image.open(image_path)
#
#
#  # print_hi("hello")
# image = Image.open('demo_image.jpg')
#
#  # print_hi("hello")
#
# image.save('new_image.png')
# image.show()
# image_obj = image.open(image_path)
# cropped_image = image_obj.crop(coords)
# cropped_image.save(saved_location)
# cropped_image.show()
#
#
# print(image.format)  # Output: JPEG # The file format of the source file.
#
# print(image.mode)  # Output: RGB  # The pixel format used by the image. Typical values are "1", "L", "RGB", or "CMYK."
#
# print(image.size)  # Output: (1920, 1280) # Image size, in pixels. The size is given as a 2-tuple (width, height).
#
# print(image.palette)  # Output: None  # Colour palette table, if any.
#
# image = Image.open('demo_image.jpg')
# image.save('new_image.png')
#
# image = Image.open('demo_image.jpg')
# new_image = image.resize((400, 400))
# new_image.save('image_400.jpg')
#
# print(image.size)  # Output: (1920, 1280)
# print(new_image.size)  # Output: (400, 400)
#
# image = Image.open('demo_image.jpg')
# box = (200, 300, 700, 600)
# cropped_image = image.crop(box)
# cropped_image.save('cropped_image.jpg')
#
# # Print size of cropped image
# print(cropped_image.size)  # Output: (500, 300)
# image = Image.open('demo_image.jpg')
# red, green, blue = image.split()
# print(image.mode)  # Output: RGB
# print(red.mode)  # Output: L
# print(green.mode)  # Output: L
# print(blue.mode)  # Output: L
# new_image = Image.merge("RGB", (green, red, blue))
# new_image.save('new_image.jpg')
# print(new_image.mode)  # Output: RGB
#
#
# if __name__ == '__main__':
#     image = 'demo_image.jpg'
#     # crop(image, (161, 166, 706, 1050), 'cropped.jpg')
#
# #  from PIL import image
# #
# # def crop(image_path, coords, saved_location):
# #     """
# #     @param image_path: the path to the image to edit
# #     @param coords: a tuple of x/y coordinates (x1, y1, x2, y2)
# #     @param saved_location: path to save the cropped image
# #     """



# #

from PIL import Image
img = Image.open(r"C:\Intel\Logs\image.png")

left = 0
top = 50
right = 510
bottom = 292

img_res = img.crop((left, top, right, bottom))

img_res.show()