exp 3 (4 maybe)
---

### data
[make_trajectory.py]  
and then  
[edge detection](https://github.com/fu-yanyuan/nerf_exp/tree/main/edge_detection)  

### upload
`scp -i .ssh/mtilab-fu.pem -r E:\opencv\data\bunny_canney ubuntu@13.114.38.153:~/workspace/nerfmm/data_dir/any_folder_demo/`  

`scp -i .ssh/mtilab-fu.pem -r E:\opencv\data\bunny_sobel ubuntu@13.114.38.153:~/workspace/nerfmm/data_dir/any_folder_demo/`  

### train  

```python
# exp 2021/08/15 canny and sobel of bunny
print('begin training canny')
train1_args = [
    "python", "tasks/any_folder/train.py", "--scene_name","any_folder_demo/bunny_canney", "--resize_ratio=1"
]
subprocess.run(train1_args)
print("end training 1")

print('begin training sobel')
train2_args = [
    "python", "tasks/any_folder/train.py", "--scene_name", "any_folder_demo/bunny_so", "--resize_ratio=1"
]
subprocess.run(train2_args)
print("end training 2")
```
### val  

```python
python tasks/any_folder/spiral.py \
--base_dir='data_dir' \
--scene_name='any_folder_demo/bunny_canney' \
--ckpt_dir='logs/any_folder/any_folder_demo/bunny_canney/lr_0.001_gpu0_seed_17_resize_1_Nsam_128_Ntr_img_-1_freq_10__210814_1803'
```  
```python
python tasks/any_folder/spiral.py \
--scene_name='any_folder_demo/bunny_sobel' \
--ckpt_dir='logs/any_folder/any_folder_demo/bunny_sobel/lr_0.001_gpu0_seed_17_resize_1_Nsam_128_Ntr_img_-1_freq_10__210815_0051'
```

```python
python tasks/any_folder/vis_learned_poses.py \
--base_dir='data_dir' --scene_name='any_folder_demo/bunny_canney' \
--ckpt_dir='logs/any_folder/any_folder_demo/bunny_canney/lr_0.001_gpu0_seed_17_resize_1_Nsam_128_Ntr_img_-1_freq_10__210814_1803'
```

### download  

`scp -i .ssh/mtilab-fu.pem -r ubuntu@13.114.38.153:~/workspace/nerfmm/logs/any_folder/any_folder_demo/bunny_canney/lr_0.001_gpu0_seed_17_resize_1_Nsam_128_Ntr_img_-1_freq_10__210814_1803/render_spiral E:/`

`scp -i .ssh/mtilab-fu.pem -r ubuntu@13.114.38.153:~/workspace/nerfmm/logs/any_folder/any_folder_demo/bunny_sobel/lr_0.001_gpu0_seed_17_resize_1_Nsam_128_Ntr_img_-1_freq_10__210815_0051/render_spiral E:/`  

`scp -i .ssh/mtilab-fu.pem ubuntu@13.114.38.153:~/workspace/nerfmm/tasks/any_folder/saved_poses/bunny.npz E:/` 

