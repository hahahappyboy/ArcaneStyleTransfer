import torch, PIL
import cv2
import pystuck
import os
from facenet_pytorch import MTCNN
from torchvision import transforms
import torch, PIL
from tqdm.notebook import tqdm
import gradio as gr
import torch
from PIL import Image

means = [0.485, 0.456, 0.406]
stds = [0.229, 0.224, 0.225]
img_transforms = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(means,stds)])

t_stds = torch.tensor(stds).cuda().half()[:,None,None]
t_means = torch.tensor(means).cuda().half()[:,None,None]

def tensor2im(var):
    return var.mul(t_stds).add(t_means).mul(255.).clamp(0, 255).permute(1, 2, 0)

def proc_pil_img(input_image, model):
    transformed_image = img_transforms(input_image)[None, ...].cuda().half()

    with torch.no_grad():
        result_image = model(transformed_image)[0]
        print(result_image.shape)
        output_image = tensor2im(result_image)
        output_image = output_image.detach().cpu().numpy().astype('uint8')
        output_image = PIL.Image.fromarray(output_image)
    return output_image

def file_name(file_dir):
    img_path_list = []
    for root, dirs, files in os.walk(file_dir):

        for file in files:
             img_path_list.append((os.path.join(root, file),file))
    return img_path_list

if __name__ == '__main__':
    file_dir = './datasets'
    save_dir = './result'
    os.makedirs(save_dir,exist_ok=True)
    img_path_list = file_name(file_dir)
    img_list = []
    modelv4 = torch.jit.load('./ArcaneGANv0.4.jit').eval().cuda().half()
    for (img_path,img_name) in img_path_list:
        print(img_path)
        im = Image.open(img_path).convert('RGB')
        # im = im.resize((512, 512))
        save_path = img_path.replace(file_dir,save_dir)
        res = proc_pil_img(im, modelv4)
        res.save(save_path)



