import torch
from transformers import pipeline

print(torch.__version__)
print(pipeline("question-answering"))
