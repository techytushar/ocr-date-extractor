# Contains plotting functions for Jupyter Notebook

import matplotlib.pyplot as plt

def display_img(img, cmap=None):
  # function to display images using plt
  plt.figure(figsize=(8,8))
  plt.imshow(img, cmap=cmap)
  print(img.size)

def plot_random():
  #plotting random images with bounding boxes
  fig, axs = plt.subplots(3, 3, figsize=(15,15))
  for row in range(3):
    for col in range(3):
      idx = random.randint(0,594)
      img = imgs[idx]
      img = rescale_image(img)
      img = np.array(img)
      thresh = threshold(img)
      cnts, bbox = find_bbox(thresh)
      temp_img = img.copy()
      cv2.drawContours(temp_img,[bbox],0,(0,0,255),4)
      axs[row,col].set_title(f'{idx}')
      axs[row,col].imshow(temp_img)
  plt.show()
