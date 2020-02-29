from .ralamb import Ralamb
from .lookahead import Lookahead

def ralamb(params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=0):
  ralamb = Ralamb(params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=0)
  return ralamb

def rangerlars(params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=0):
  ralamb = Ralamb(params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=0)
  return Lookahead(ralamb)
