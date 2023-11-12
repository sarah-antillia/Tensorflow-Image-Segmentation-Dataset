import os
import glob
from re import A
import shutil
from PIL import Image, ImageOps, ImageFilter
import cv2
import traceback
import numpy as np

class ImageMaskDatasetGenerator:
  
  def __init__(self, resize=312, cropsize=128):
    self.RESIZE  = resize
     
    self.resize_ratio = 1
    self.blur_mask    = True
    self.CROPSIZE    = cropsize

  def crop_image(self, image):
    w, h = image.size
    left  = (w - self.CROPSIZE)//2
    upper = (h - self.CROPSIZE)//2
    right = left  + self.CROPSIZE
    lower = upper + self.CROPSIZE

    return  image.crop( (left, upper, right, lower))

  # cropped = img.crop( (left, upper, right, lower) )
  def augment(self, image, output_dir, filename):
    # 2023/07/22
    ANGLES = [30, 90, 120, 150, 180, 210, 240, 270, 300, 330]

    for angle in ANGLES:
      rotated_image = image.rotate(angle)
      output_filename = "rotated_" + str(angle) + "_" + filename
      rotated_image_file = os.path.join(output_dir, output_filename)
      cropped  =  self.crop_image(rotated_image)
      cropped.save(rotated_image_file)
      print("=== Saved {}".format(rotated_image_file))
    # Create mirrored image
    mirrored = ImageOps.mirror(image)
    output_filename = "mirrored_" + filename
    image_filepath = os.path.join(output_dir, output_filename)
    cropped = self.crop_image(mirrored)
    cropped.save(image_filepath)
    print("=== Saved {}".format(image_filepath))
        
    # Create flipped image
    flipped = ImageOps.flip(image)
    output_filename = "flipped_" + filename

    image_filepath = os.path.join(output_dir, output_filename)
    cropped = self.crop_image(flipped)

    cropped.save(image_filepath)
    print("=== Saved {}".format(image_filepath))


  def resize_to_square(self, image):
     w, h  = image.size
     pixel = image.getpixel((w-2, h-2))
     background = Image.new("RGB", (self.RESIZE, self.RESIZE), pixel)
     bigger = w
     if h > bigger:
       bigger = h
     x = (self.RESIZE - w) // 2
     y = (self.RESIZE - h) // 2
     background.paste(image, (x, y))
     return background
  

  def create(self, categorized_input_dir, mask_color,  
                            categorized_images_dir, categorized_masks_dir, debug=False):

    if os.path.exists(categorized_images_dir):
      shutil.rmtree(categorized_images_dir)
    if not os.path.exists(categorized_images_dir):
      os.makedirs(categorized_images_dir)

    if os.path.exists(categorized_masks_dir):
      shutil.rmtree(categorized_masks_dir)
    if not os.path.exists(categorized_masks_dir):
      os.makedirs(categorized_masks_dir)

    xpattern = categorized_input_dir + "/*-d.bmp"
    mask_files = glob.glob(xpattern)
    if mask_files == None or len(mask_files) == 0:
      print("FATAL ERROR: Not found mask files")
      return

    for mask_file in mask_files:
      basename = os.path.basename(mask_file)
      image_file = basename.replace("-d.bmp", ".BMP")

      image_filepath = os.path.join(categorized_input_dir, image_file)
      print("--- image_filepath {}".format(image_filepath))
      image = Image.open(image_filepath)
      w, h = image.size
      rw   = w * self.resize_ratio
      rh   = h * self.resize_ratio
      image = image.resize((rw, rh))
      image_file = image_file.replace(".BMP", ".jpg")
      image_output_filepath = os.path.join(categorized_images_dir, image_file)
      squared_image = self.resize_to_square(image)
      # Save the cropped_square_image
      cropped = self.crop_image(squared_image)
      cropped.save(image_output_filepath)
      print("--- Saved cropped_square_image {}".format(image_output_filepath))

      self.augment(squared_image, categorized_images_dir, image_file)
   
      print("--- mask_file {}".format(mask_file)) 

      mask  = Image.open(mask_file).convert("RGB")
      w, h = mask.size
      rw   = w * self.resize_ratio
      rh   = h * self.resize_ratio
      mask = mask.resize((rw, rh))
      xmask = self.create_mono_color_mask(mask, mask_color= mask_color)
   
      # Blur mask 
      if self.blur_mask:
        print("---blurred ")
        xmask = xmask.filter(ImageFilter.BLUR)
      
      if debug:
        xmask.show()
        input("XX")   
      out_mask_file = image_file
      mask_output_filepath = os.path.join(categorized_masks_dir, out_mask_file)

      squared_mask = self.resize_to_square(xmask)
      cropped_mask = self.crop_image(squared_mask)
      cropped_mask.save(mask_output_filepath)

      print("--- Saved cropped_squared_mask {}".format(mask_output_filepath))
      self.augment(squared_mask, categorized_masks_dir, out_mask_file)


  def create_mono_color_mask(self, mask, mask_color=(255, 255, 255)):
    rw, rh = mask.size    
    xmask = Image.new("RGB", (rw, rh))
    #print("---w {} h {}".format(rw, rh))

    for i in range(rw):
      for j in range(rh):
        color = mask.getpixel((i, j))
        (r, g, b) = color
        # If color is blue
        if b == 255:
          xmask.putpixel((i, j), mask_color)

    return xmask
  

if __name__ == "__main__":
  try:
    categories_colors = [
      ["carcinoma_in_situ",   (255,    0,   0)],
      ["light_dysplastic",    (  0,  255,   0)],
      ["moderate_dysplastic", (  0,    0, 255)],
      ["normal_columnar",     (255,  255,   0)],
      ["normal_intermediate", (255,    0, 255)],
      ["normal_superficiel",  (  0,  255, 255)],
      ["severe_dysplastic",   (255,  255, 255)],
    ]
    base_dir   = "./New database pictures"
    output_dir = "./Smear2005-master"
    

    dataset = ImageMaskDatasetGenerator()
    for category_color in categories_colors:
      [category, mask_color] = category_color
      categorized_input_dir  = os.path.join(base_dir, category)
      categorized_output_dir = os.path.join(output_dir, category)
      categorized_images_dir = os.path.join(categorized_output_dir, "images")
      categorized_masks_dir  = os.path.join(categorized_output_dir, "masks")
      
      dataset.create(categorized_input_dir, mask_color, categorized_images_dir, categorized_masks_dir)

  except:
    traceback.print_exc()
    pass

"""
INPUT
./New database pictures
├─carcinoma_in_situ
├─light_dysplastic
├─moderate_dysplastic
├─normal_columnar
├─normal_intermediate
├─normal_superficiel
└─severe_dysplastic

"""
"""
1 Resize all bmp image ans mask to 256x356
2 Rotate, flipp, mirror those files to augment those resized image and mask files

"""


"""
OUPUT
./Smear2005-master
├─carcinoma_in_situ
│  ├─images
│  └─masks
├─light_dysplastic
│  ├─images
│  └─masks
├─moderate_dysplastic
│  ├─images
│  └─masks
├─normal_columnar
│  ├─images
│  └─masks
├─normal_intermediate
│  ├─images
│  └─masks
├─normal_superficiel
│  ├─images
│  └─masks
└─severe_dysplastic
    ├─images
    └─masks
"""