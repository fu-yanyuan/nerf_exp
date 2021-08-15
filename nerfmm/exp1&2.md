exp1&2
---

COLMAP does not work on sketch data.  
Try to use nerfmm to get the result without pre-computed camera parameters

### EXP1  
data: flower_sketch (llff/flower operated by online algorithms)

train  
```
python tasks/any_folder/train.py \
--base_dir='data_dir' \
--scene_name='any_folder_demo/flower_sketch'
```  

render novel views
```
python tasks/any_folder/spiral.py \
--base_dir='data_dir' \
--scene_name='any_folder_demo/flower_sketch' \
--ckpt_dir='logs/any_folder/any_folder_demo/flower_sketch/lr_0.001_gpu0_seed_17_resize_4_Nsam_128_Ntr_img_-1_freq_10__210701_1514'
```  
<p align="center"><img src="results/img.gif?raw=true" alt="Comparison"></p>  

visualize estimated poses in 3D
```python
python tasks/any_folder/vis_learned_poses.py \
--base_dir='data_dir' \
--scene_name='any_folder_demo/flower_sketch' \
--ckpt_dir='logs/any_folder/any_folder_demo/flower_sketch/lr_0.001_gpu0_seed_17_resize_4_Nsam_128_Ntr_img_-1_freq_10__210701_1514'
```


###EXP2  
data: armadillo(stanford 3D scanning repository)  
  - donwnload 3D .ply files from [models](https://gfx.cs.princeton.edu/proj/sugcon/models/)
  - download suggestive contour software: [rtsc](https://gfx.cs.princeton.edu/proj/sugcon/)
  - `./rtsc MODEL.ply` to get the sketch results, and I just simply PRT_SC to get the sketch images.
  - upload data to aws-ec2: `scp -i .ssh/XXX.pem -r E:\NeRF\mydata\armadillo ubuntu@IP:~/workspace/nerfmm/data_dir/any_folder_demo/`


train  
```
python tasks/any_folder/train.py \
--base_dir='data_dir' \
--scene_name='any_folder_demo/armadillo'
```

render novel views  
```  
python tasks/any_folder/spiral.py \
--base_dir='data_dir' \
--scene_name='any_folder_demo/armadillo' \
--ckpt_dir='logs/any_folder/any_folder_demo/armadillo/lr_0.001_gpu0_seed_17_resize_4_Nsam_128_Ntr_img_-1_freq_10__210709_1547'
```  
download results:  
`scp -i .ssh/XXX.pem -r
ubuntu@IP:~/workspace/nerfmm/logs/any_folder/any_folder_demo/armadillo/lr_0.001_gpu0_seed_17_resize_4_Nsam_128_Ntr_img_-1_freq_10__210709_1547/render_spiral E:\NeRF\results\armadillo`





