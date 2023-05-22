from argparse import ArgumentParser
import os

# Where to look for the model folder
username = os.getenv('USERNAME')
default_ddp_path = f"C:/Users/{username}/.cache/huggingface/hub/models--SmilingWolf--wd-v1-4-vit-tagger-v2/snapshots/1f3f3e8ae769634e31e1ef696df11ec37493e4f2"

def preload(parser: ArgumentParser):
    parser.add_argument(
        '--deepdanbooru-projects-path',
        type=str,
        help='Path to directory with DeepDanbooru project(s).',
        default=default_ddp_path
    )