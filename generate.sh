# Modelscope video generate
python3 video_generate/Modelscope.py -p prompts/prompt.yml -s output -n 100 -m Modelscope pre-train path

# Zeroscope video generate 
python3 video_generate/Zodelscope.py -p prompts/prompt.yml -s output -n 100 -m Zodelscope pre-train path

# svd video generate
python3 video_generate/svd/video_gen.py -p image path

# i2vgen video generate
python3 video_generate/i2vgen-xl/inference.py --cfg video_generate/i2vgen-xl/configs/i2vgen_xl_infer.yaml