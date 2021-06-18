EXP2
---  

## data 
original images are /flower from nerf, and generating sketches from https://imagetosketch.com/  
[colmap](https://gist.github.com/kwea123/f0e8f38ff2aa94495dbfe7ae9219f75c)to prepare camera poses for data  
the reason that i use colmap is that i can not follow the steps due to some errors on server. ##[to be done]##  

## train 
# for flower_sketch2
``` shell
python train.py \ 
    --dataset_name llff \
    --root_dir data/nerf_llff_data/flower_sketch2 \ # data root dir
    --N_importance 64 --img_wh 400 300 \ # 400 300 should be propotioned to the original images in data root dir
    --num_epochs 30 --batch_size 1024 \
    --optimizer adam --lr 5e-4 \
    --lr_scheduler cosine \   
    --exp_name flower_sketch2_exp  # this will be in the folder ckpts, which is loaded in the next test step
```  
# for flower (orignal)
``` shell
python train.py \
    --dataset_name llff \
    --root_dir data/nerf_llff_data/flower \
    --N_importance 64 --img_wh 400 300 \
    --num_epochs 30 --batch_size 1024 \
    --optimizer adam --lr 5e-4 \
    --lr_scheduler cosine \
    --exp_name flower_exp
```  

## test  
```shell
python eval.py \    
--root_dir data/nerf_llff_data/flower_sketch2 \    
--dataset_name llff --scene_name flower_sketch2 \  # scene_name will be the folder in result\llff\, all the synthesized images and the .gif are stored here
--img_wh 400 300 --N_importance 64 \
--ckpt_path ckpts/flower_sketch2_exp/epoch=29.ckpt # choose a .ckpt to load
```  

```shell
python eval.py \
--root_dir data/nerf_llff_data/flower \
--dataset_name llff --scene_name flower \
--img_wh 400 300 --N_importance 64 \
--ckpt_path ckpts/flower_exp/epoch=29.ckpt
``` 
# download the result

`scp -i .ssh/mtilab-fu.pem -r ubuntu@IP:~/workspace/nerf_pl/results/llff/flower E:\NeRF\results\llff`


