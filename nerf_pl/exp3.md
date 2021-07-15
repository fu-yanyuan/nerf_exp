EXP3-Sobel and Canny edge detection
---

#### data  
apply sobel and canney edge detection algorithms to llff/flower  

#### train  
```python
import subprocess

command1 = ['python', 'train.py', 
            '--dataset_name', 'llff',
            '--root_dir', 'data/nerf_llff_data/llff_flower_canney',
            '--N_importance', '64',
            '--num_epochs', '30',
            '--batch_size', '1024',
            '--optimizer', 'adam', '--lr', '5e-4',
            '--lr_scheduler', 'cosine',
            '--exp_name', 'flower_canney_exp']
subprocess.run(command1)

command2 = ['python', 'train.py', 
            '--dataset_name', 'llff',
            '--root_dir', 'data/nerf_llff_data/llff_flower_sobel',
            '--N_importance', '64',
            '--num_epochs', '30',
            '--batch_size', '1024',
            '--optimizer', 'adam', '--lr', '5e-4',
            '--lr_scheduler', 'cosine',
            '--exp_name', 'flower_sobel_exp']
subprocess.run(command2)
```  
> 'You must set @img_wh to have the same aspect ratio as ({W}, {H}) !'

#### test  
```python
# test
command3 = ['python', 'eval.py', 
            '--dataset_name', 'llff',
            '--scene_name', 'flower_sobel',
            '--root_dir', 'data/nerf_llff_data/llff_flower_sobel',
            '--N_importance', '64',
            '--ckpt_path', 'ckpts/flower_sobel_exp/epoch=4.ckpt']
subprocess.run(command3)

command4 = ['python', 'eval.py', 
            '--dataset_name', 'llff',
            '--scene_name', 'flower_canney',
            '--root_dir', 'data/nerf_llff_data/llff_flower_canney',
            '--N_importance', '64',
            '--ckpt_path', 'ckpts/flower_canney_exp/epoch=29.ckpt']
subprocess.run(command4)
```  

#### result  
<p align="center"><img src="results/flower_canney.gif?raw=true" alt="Comparison"></p>


