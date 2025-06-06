# gpt/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_model_and_tokenizer
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import logging

logger = logging.getLogger(__name__)

model, tokenizer = get_model_and_tokenizer()

MAX_SEQ_LENGTH = 100
NUM_TOKENS = 50
TEMPERATURE = 0.7


def generate_text(seed_text):
    token_seq = tokenizer.texts_to_sequences([seed_text])[0]
    token_seq = token_seq[-MAX_SEQ_LENGTH:]

    for _ in range(NUM_TOKENS):
        padded = pad_sequences([token_seq], maxlen=MAX_SEQ_LENGTH, padding='pre')
        preds = model.predict(padded, verbose=0)[0, -1]

        preds = np.log(preds + 1e-9) / TEMPERATURE
        preds = np.exp(preds) / np.sum(np.exp(preds))

        next_token_id = np.random.choice(len(preds), p=preds)
        token_seq.append(next_token_id)

        if len(token_seq) > MAX_SEQ_LENGTH:
            token_seq = token_seq[-MAX_SEQ_LENGTH:]

    return tokenizer.sequences_to_texts([token_seq])[0]


def chat_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        logger.info(f"User: {user_input}")
        response = generate_text(user_input)
        logger.info(f"Bot: {response}")
        return JsonResponse({'response': response})
    return render(request, 'gpt/chat.html')


def test_generate(request):
    seed_text = "object-oriented programming"
    response = generate_text(seed_text)
    return JsonResponse({'response': response})