# Diffusion Generated Video Dataset and Detection Benchmark

## Video samples  
Modelscope video  
![image](asserts/cat_1017.gif)  
Zeroscope video  
![image](asserts/Fireworks_nw_1007.gif)  
SVD video  
![image](asserts/i2v-sd-00068.gif)  
I2VGen-xl video 
![image](asserts/0000001.gif)
---
---

## Datasets

If you want to download the dataset, please mail for us zhengtp@mail.hfut.edu.cn  

## Video generate

Please refer

`generate.sh`

## Video evaluation

We use `EvalCrafter` and `AIGCBench` to evaluate the video generation quantity  
You can see the code in `metrics/EvalCrafter` and `metrics/AIGCBench`

## Detection
The detection method we follow the `SlowFast`
## Citation
```bibtex
@article{郑天鹏 2024 扩散模型生成视频数据集及其检测基准研究,
title={扩散模型生成视频数据集及其检测基准研究},
author={郑天鹏 and 陈雁翔 and 温心哲 and 李严成 and 王志远},
journal={中国图象图形学报},
pages={1-13},
year={2024},
doi={10.11834/jig.240259},
}
```
