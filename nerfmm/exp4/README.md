exp4
---  

#### trajecory  
make_trajectory.py  
then apply canny edges: edges.py  

#### upload  
`scp -i .ssh/mtilab-fu.pem -r E:\opencv\data\bunny_trj2_canney ubuntu@13.114.38.153:~/workspace/nerfmm/data_dir/any_folder_demo/`

#### train  
```python
python tasks/any_folder/train.py \
--base_dir='data_dir' \
--scene_name='any_folder_demo/'
```  
#### val
```python
python tasks/any_folder/spiral.py \
--scene_name='any_folder_demo/bunny_trj2_canney' \
--ckpt_dir='logs/any_folder/any_folder_demo/bunny_trj2_canney/lr_0.001_gpu0_seed_17_resize_1_Nsam_128_Ntr_img_-1_freq_10__210816_1648'
```  
```python  
python tasks/any_folder/vis_learned_poses.py \
--scene_name='any_folder_demo/bunny_trj2_canney' \
--ckpt_dir='logs/any_folder/any_folder_demo/bunny_trj2_canney/lr_0.001_gpu0_seed_17_resize_1_Nsam_128_Ntr_img_-1_freq_10__210816_1648'
```  

#### download  
`scp -i .ssh/mtilab-fu.pem -r ubuntu@13.114.38.153:~/workspace/nerfmm/logs/any_folder/any_folder_demo/bunny_trj2_canney/lr_0.001_gpu0_seed_17_resize_1_Nsam_128_Ntr_img_-1_freq_10__210816_1648/render_spiral E:/`  
`scp -i .ssh/mtilab-fu.pem ubuntu@13.114.38.153:~/workspace/nerfmm/tasks/any_folder/saved_poses/bunny_trj2.npz E:/`
