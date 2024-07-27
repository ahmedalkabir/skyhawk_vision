import urllib.request
import matplotlib.pyplot as plt
from PIL import Image
import torch
from torchvision import transforms, models


url = 'https://pytorch.tips/coffee'
fpath = 'coffee.jpg'
urllib.request.urlretrieve(url, fpath)

img = Image.open('coffee.jpg')
plt.imshow(img)

transform = transforms.Compose([transforms.Resize(256), 
                               transforms.CenterCrop(244),
                               transforms.ToTensor(),
                               transforms.Normalize(
                                   mean=[0.485, 0.456, 0.406],
                                   std=[0.229, 0.224, 0.225])])

img_tensor = transform(img)
batch = img_tensor.unsqueeze(0)
model = models.alexnet(pretrained=True)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.eval()
model.to(device)

