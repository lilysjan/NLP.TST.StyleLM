from torch.utils import Dataset
import torch

class KoGPTDataset(Dataset):
  def __init__(self, eos, sos, tk, data):
    self.eos = eos
    self.sos = sos
    self.tokenizer = tk

    data = list(map(lambda x: f"{sos}{x}{eos}", data))

    self.data = list(map(lambda x: tk.encode(x), data))
  

  def __len__(self):
      return len(self.data)

  def __getitem__(self, idx):
      return torch.tensor(self.data[idx]).cuda().long()

