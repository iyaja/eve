from .ralamb import Ralamb
from .lookahead import Lookahead
from .radam import RAdam
from .eve import EVE

def ralamb(params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=0):
  ralamb = Ralamb(params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=0)
  return ralamb

def ranger(params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=0):
  radam = RAdam(params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=0)
  return Lookahead(radam)

def rangerlars(params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=0):
  ralamb = Ralamb(params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=0)
  return Lookahead(ralamb)

def eve(params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=0, diffgrad=True):
  eve_base = EVE(params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=0, diffgrad=True)
  return Lookahead(eve_base)