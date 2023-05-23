### Changing model
You can find some tagger models [here](https://huggingface.co/models?sort=downloads&search=tagger), and some DeepDanbooru tagger models [here](https://github.com/KichangKim/DeepDanbooru/releases).

- #### *tagger models*
  For now, if you want to change the tagger model used, you have to change the default one:
  - select the desired model from tagger>interrogator:

    ![image](https://github.com/GiusTex/vladmandic-WD14-Tagger/assets/112352961/6c41d15a-b071-4330-8317-223cede6507d)

    ![image](https://github.com/GiusTex/vladmandic-WD14-Tagger/assets/112352961/73cf216e-bf08-4af2-85f6-bfa58bcb46d1)

    Drop or upload a random image to tag and click "Interrogate". The script will download the model here `C:\Users\YourName\.cache\huggingface\hub\models--author-ModelName`:

    ![image](https://github.com/GiusTex/vladmandic-WD14-Tagger/assets/112352961/57d5f421-85b2-4256-86cb-c834d016ec7d)
  
    (a new folder with the model name will appear, the one there is the default one).
  
    Now you can choose one of the following ways:
    
   - change the `model.onnx` and `selected_tags.csv` inside the default model path `C:\Users\YourName\.cache\huggingface\hub\models--SmilingWolf--wd-v1-4-vit-tagger-v2\snapshots\1f3f3e8ae769634e31e1ef696df11ec37493e4f2` 
  
     or
  
   - change the default model path inside `VladDiffusion\extensions\vladmandic-WD14-Tagger\preload.py` at line 6, and inside `VladDiffusion\extensions\vladmandic-WD14-Tagger\tagger\utils.py` at line 66 with your 
     desired path model.
  #### Thing to remember:
    > For now you can't change the model from within the webui (we use it just to download the model), otherwise every time you select "Interrogate" the script will download the model, since the model path isn't 
     updated. We have to change the default model manually, as explained above.
  
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
