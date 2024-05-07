import argparse
import os
import random
import zipfile
import pandas
import yaml
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.models import Model
import time


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
    parser.add_argument('-m', '--model_path', default='damo/text-to-video-synthesis' ,type=str)
    argv = parser.parse_args()

    with open(argv.prompt_path, 'r') as f:
        prompt_dict = yaml.load(f, yaml.FullLoader)

    classlist = prompt_dict.keys()
    video_num = argv.generate_video_num
    savepath = argv.save_path + f'_{video_num}'

    Ls = []
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    p = pipeline('text-to-video-synthesis', argv.model_path)
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
            text = {'text': prompt_texts[ri]}
            output_video_path = p(input=text, output_video=f'{save}/{cls}_{i}.mp4')[OutputKeys.OUTPUT_VIDEO]
            Ls.append({'class': cls, 'gen_video': f'{cls}_{i}', 'prompt_id': ri})
    zipDir(savepath, savepath+'.zip')
    savelist(Ls, savepath)
