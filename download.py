import argparse
from huggingface_hub import hf_hub_download

parser = argparse.ArgumentParser()
parser.add_argument("--model", type=str, default="model", help="huggingface model name")
args = parser.parse_args()

model = args.model
print(model)
hf_hub_download(repo_id=model)