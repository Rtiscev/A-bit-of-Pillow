from PIL import Image, ImageChops

im = Image.open("images/im6.jpg")
im2 = Image.open("images/im7.jpg")

im_invert = ImageChops.difference(im, im2).show()
# im_invert.show()


