You can find some tagger models [here](https://huggingface.co/models?sort=downloads&search=tagger), and some DeepDanbooru tagger models [here](https://github.com/KichangKim/DeepDanbooru/releases).

- #### *DeepDanbooru*
      1. Various model files can be found below.
         - [DeepDanbooru models](https://github.com/KichangKim/DeepDanbooru/releases)
         - [e621 model by 🐾Zack🐾#1984](https://discord.gg/BDFpq9Yb7K)
            *(link contains NSFW contents!)*

      1. Move the project folder containing the model and config to `models/deepdanbooru`

      1. The file structure should look like:
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
