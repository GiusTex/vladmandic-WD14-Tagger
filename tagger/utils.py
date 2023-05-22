import os

from typing import List, Dict
from pathlib import Path

from modules import shared, scripts
from preload import default_ddp_path
from tagger.preset import Preset
from tagger.interrogator import Interrogator, DeepDanbooruInterrogator, WaifuDiffusionInterrogator

preset = Preset(Path(scripts.basedir(), 'presets'))

interrogators: Dict[str, Interrogator] = {}


def refresh_interrogators() -> List[str]:
    global interrogators
    interrogators = {
        'wd14-convnextv2-v2': WaifuDiffusionInterrogator(
            'wd14-convnextv2-v2',
            repo_id='SmilingWolf/wd-v1-4-convnextv2-tagger-v2',
            revision='v2.0'
        ),
        'wd14-vit-v2': WaifuDiffusionInterrogator(
            'wd14-vit-v2',
            repo_id='SmilingWolf/wd-v1-4-vit-tagger-v2',
            revision='v2.0'
        ),
        'wd14-convnext-v2': WaifuDiffusionInterrogator(
            'wd14-convnext-v2',
            repo_id='SmilingWolf/wd-v1-4-convnext-tagger-v2',
            revision='v2.0'
        ),
        'wd14-swinv2-v2': WaifuDiffusionInterrogator(
            'wd14-swinv2-v2',
            repo_id='SmilingWolf/wd-v1-4-swinv2-tagger-v2',
            revision='v2.0'
        ),
        'wd14-convnextv2-v2-git': WaifuDiffusionInterrogator(
            'wd14-convnextv2-v2',
            repo_id='SmilingWolf/wd-v1-4-convnextv2-tagger-v2',
        ),
        'wd14-vit-v2-git': WaifuDiffusionInterrogator(
            'wd14-vit-v2-git',
            repo_id='SmilingWolf/wd-v1-4-vit-tagger-v2'
        ),
        'wd14-convnext-v2-git': WaifuDiffusionInterrogator(
            'wd14-convnext-v2-git',
            repo_id='SmilingWolf/wd-v1-4-convnext-tagger-v2'
        ),
        'wd14-swinv2-v2-git': WaifuDiffusionInterrogator(
            'wd14-swinv2-v2-git',
            repo_id='SmilingWolf/wd-v1-4-swinv2-tagger-v2'
        ),
        'wd14-vit': WaifuDiffusionInterrogator(
            'wd14-vit',
            repo_id='SmilingWolf/wd-v1-4-vit-tagger'),
        'wd14-convnext': WaifuDiffusionInterrogator(
            'wd14-convnext',
            repo_id='SmilingWolf/wd-v1-4-convnext-tagger'
        ),
    }

    # Where to look for the model folder
    username = os.getenv('USERNAME')
    deepdanbooru_projects_path = f"C:/Users/{username}/.cache/huggingface/hub/models--SmilingWolf--wd-v1-4-vit-tagger-v2/snapshots/1f3f3e8ae769634e31e1ef696df11ec37493e4f2"
    # create folder if it doesn't exist
    os.makedirs(deepdanbooru_projects_path, exist_ok=True)

    # Load model
    for path in os.scandir(deepdanbooru_projects_path):
        if not path.is_dir():
            continue

        if not Path(path, 'project.json').is_file():
            continue

        interrogators[path.name] = DeepDanbooruInterrogator(path.name, path)

    return sorted(interrogators.keys())


def split_str(s: str, separator=',') -> List[str]:
    return [x.strip() for x in s.split(separator) if x]
