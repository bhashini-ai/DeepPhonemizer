import torch
from dp.phonemizer import Phonemizer

phonemizer = Phonemizer.from_checkpoint('models/en_us_cmudict_forward.pt')
model = phonemizer.predictor.model
torch.jit.save(torch.jit.script(model), 'models/torchscript_model.pt')
