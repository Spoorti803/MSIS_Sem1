import numpy as np


def Attention(X,W_q,b_q):
    Q = W_q @X + b_q
    return Q

d_x, d_attn, l_x = 60, 50, 10

X   = np.random.randn(d_x, l_x)
W_q = np.random.randn(d_attn, d_x)
b_q = np.random.randn(d_attn, 1)

Q = Attention(X, W_q, b_q)
print(Q.shape)   