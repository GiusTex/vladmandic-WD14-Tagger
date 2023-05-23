You can find some tagger models [here](https://huggingface.co/models?sort=downloads&search=tagger), and some DeepDanbooru tagger models [here](https://github.com/KichangKim/DeepDanbooru/releases).

- #### *tagger models*
  For now, if you want to change the tagger model used, you have to:
  - change the model.onnx and selected_tags.csv inside `C:\Users\YourName\.cache\huggingface\hub\models--SmilingWolf--wd-v1-4-vit-tagger-v2\snapshots\1f3f3e8ae769634e31e1ef696df11ec37493e4f2` with your desired model
  
    or
  
  - change the path inside `VladDiffusion\extensions\vladmandic-WD14-Tagger\preload.py` at line 6, and inside `VladDiffusion\extensions\vladmandic-WD14-Tagger\tagger\utils.py` at line 66 with your desired path model.
 
- #### *DeepDanbooru tagger*
 1. Various model files can be found below.
    - [DeepDanbooru models](https://github.com/KichangKim/DeepDanbooru/releases)
    - [e621 model by 🐾Zack🐾#1984](https://discord.gg/BDFpq9Yb7K)
    
    *(link contains NSFW contents!)*

   2. Move the project folder containing the model and config to `models/deepdanbooru`

   3. The file structure should look like:
         ```
         models/
         └╴deepdanbooru/
           ├╴deepdanbooru-v3-20211112-sgd-e28/
           │ ├╴project.json
           │ └╴...
           │
           ├╴deepdanbooru-v4-20200814-sgd-e30/
           │ ├╴project.json
           │ └╴...
           │
           ├╴e621-v3-20221117-sgd-e32/
           │ ├╴project.json
           │ └╴...
           │
           ...
         ```
