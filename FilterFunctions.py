from PIL import Image

def convert_image(input_image):
    img1 = Image.open(input_image)
    grey_scale_img = img1.convert("L")
    return grey_scale_img