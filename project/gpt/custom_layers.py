# gpt/custom_layers.py

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers


class PositionalEncoding(layers.Layer):
    def __init__(self, max_len, d_model, trainable=False, dtype=None, **kwargs):
        super(PositionalEncoding, self).__init__(trainable=trainable, dtype=dtype, **kwargs)
        self.max_len = max_len
        self.d_model = d_model

        pos = np.arange(max_len)[:, np.newaxis]
        i = np.arange(d_model)[np.newaxis, :]

        angle_rates = 1 / np.power(10000, (2 * (i // 2)) / d_model)
        angle_rads = pos * angle_rates

        angle_rads[:, 0::2] = np.sin(angle_rads[:, 0::2])
        angle_rads[:, 1::2] = np.cos(angle_rads[:, 1::2])

        self.pos_encoding = tf.cast(angle_rads[np.newaxis, ...], dtype=tf.float32)

    def call(self, x):
        return x + self.pos_encoding[:, :tf.shape(x)[1], :]

    def get_config(self):
        config = super().get_config()
        config.update({
            'max_len': self.max_len,
            'd_model': self.d_model,
        })
        return config


class CausalSelfAttention(layers.Layer):
    def __init__(self, num_heads, key_dim, dropout=0.1, trainable=True, dtype=None, **kwargs):
        super().__init__(**kwargs)
        self.num_heads = num_heads
        self.key_dim = key_dim
        self.attn = layers.MultiHeadAttention(num_heads=num_heads, key_dim=key_dim)
        self.dropout = layers.Dropout(dropout)

    def call(self, x):
        seq_len = tf.shape(x)[1]
        causal_mask = tf.linalg.band_part(tf.ones((seq_len, seq_len)), -1, 0)
        attn_output = self.attn(query=x, value=x, attention_mask=causal_mask[tf.newaxis, tf.newaxis, :, :])
        return x + self.dropout(attn_output)

    def get_config(self):
        config = super().get_config()
        config.update({
            'num_heads': self.num_heads,
            'key_dim': self.key_dim,
        })
        return config