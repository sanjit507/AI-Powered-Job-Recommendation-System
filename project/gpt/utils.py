# gpt/utils.py

import pickle
import os
from tensorflow.keras.models import load_model
from .custom_layers import PositionalEncoding, CausalSelfAttention

MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'gpt_model', 'gpt_small.keras')
TOKENIZER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'gpt_model', 'tokenizer.pkl')

model = load_model(MODEL_PATH, custom_objects={
    "PositionalEncoding": PositionalEncoding,
    "CausalSelfAttention": CausalSelfAttention,
})

with open(TOKENIZER_PATH, 'rb') as f:
    tokenizer = pickle.load(f)


def get_model_and_tokenizer():
    return model, tokenizer