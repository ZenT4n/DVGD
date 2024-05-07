import argparse

import torch
import os
import random
import time
import yaml
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video
import pandas
import zipfile

def zipDir(dirpath, outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')

        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()


def savelist(savelist, savepath):
    pd = pandas.DataFrame(savelist)
    savename = os.path.join(savepath, 'gen_info.txt')
    pd.to_csv(savename, index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-p', '--prompt_path', default='prompt.yml', type=str)
    parser.add_argument('-s', '--save_path', default='outputs', type=str)
    parser.add_argument('-n', '--generate_video_num', type=int)
    parser.add_argument('-m', '--model_path', default='zeroscope_v2_576w' ,type=str)
    argv = parser.parse_args()

    with open(argv.prompt_path, 'r') as f:
        prompt_dict = yaml.load(f, yaml.FullLoader)

    classlist = prompt_dict.keys()
    video_num = argv.generate_video_num
    savepath = argv.save_path + f'_{video_num}'

    if torch.cuda.is_available():
        device_count = torch.cuda.device_count()
        print(f"当前系统中可用的GPU数量为：{device_count}")
    else:
        print("未检测到可用的GPU")

    with open('prompt.yml', 'r') as f:
        prompt_dict = yaml.load(f, yaml.FullLoader)
    classlist = prompt_dict.keys()

    if not os.path.exists(savepath):
        os.mkdir(savepath)
    pipe = DiffusionPipeline.from_pretrained(argv.model_path, torch_dtype=torch.float16)
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe.enable_model_cpu_offload()

    Ls = []
    for cls in classlist:
        num_vi = 0
        save = os.path.join(savepath, cls)
        if not os.path.exists(save):
            os.mkdir(save)
        else:  # this part can delete, because it will pass code next render we can't get more video
            num_vi = len(os.listdir(save))
            if num_vi == video_num:
                continue
        prompt_texts = prompt_dict[cls]
        n = len(prompt_texts)
        print(f'Creating {cls} video -- {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')
        for i in range(num_vi, video_num):
            ri = random.randint(0, n - 1)
            prompt = prompt_texts[ri]
            video_frames = pipe(prompt, num_inference_steps=30, height=256, width=256, num_frames=24).frames
            video_path = export_to_video(video_frames, output_video_path=f'{save}/{cls}_nw_{i}.mp4')
            Ls.append({'class': cls, 'gen_video': f'{cls}_{i}', 'prompt_id': ri})
    print(f'Finish {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')
    zipDir(savepath, savepath+'.zip')
    savelist(Ls, savepath)