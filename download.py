import argparse
from huggingface_hub import snapshot_download

parser = argparse.ArgumentParser()
parser.add_argument("--model", type=str, default="model", help="huggingface model name")
args = parser.parse_args()

model = args.model
print(model)
huggingface-cli download model