# %%
# !pip install --upgrade timm

# %%
# !git clone https://github.com/isl-org/ZoeDepth.git


# %%
import torch
from zoedepth.utils.misc import get_image_from_url, colorize
from PIL import Image
import matplotlib.pyplot as plt

import numpy as np
from torchvision.transforms import ToTensor
from PIL import Image
from zoedepth.utils.misc import get_image_from_url, colorize
import torch

from zoedepth.models.builder import build_model
from zoedepth.utils.config import get_config
from pprint import pprint



zoe = torch.hub.load(".", "ZoeD_N", source="local", pretrained=True)
     

# %%
zoe = zoe.to('cuda')

# %%
#@title Predicting depth from a url image
import pdb
img_url = "http://static1.squarespace.com/static/6213c340453c3f502425776e/62f2452bc121595f4d87c713/62f3c63c5eec2b12a333f851/1661442296756/Screenshot+2022-08-10+at+15.55.27.png?format=1500w" #@param {type:"string"}
img = get_image_from_url(img_url)

pdb.set_trace()
depth = zoe.infer_pil(img)


colored_depth = colorize(depth)
fig, axs = plt.subplots(1,2, figsize=(15,7))
for ax, im, title in zip(axs, [img, colored_depth], ['Input', 'Predicted Depth']):
  ax.imshow(im)
  ax.axis('off')
  ax.set_title(title)

# %%



