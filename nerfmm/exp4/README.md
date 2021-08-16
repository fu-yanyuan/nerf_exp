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
