from torch.utils.data import Dataset
import torch
from torch.nn.functional import one_hot


class DelDataset(Dataset):
    def __init__(self, scripts):
        self.data = list(map(lambda  x: x[2:-1], scripts))

        # TODO:일단 PoC로 하나의 캐릭터 대사만 사용함. 나중에 맞춰서 개선할 필요 존재
        # 이 때 one-hot encoding이 된 형태를 사용해야 함
        self.label =  one_hot(torch.ones(len(scripts)).long()).cuda()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return torch.tensor(self.data[idx]).cuda().long(), self.label[idx]


class GenDataset(Dataset):
    def __init__(self, scripts):

        self.data_in = list(map(lambda  x: x[2:-1], scripts))
        self.data_out = list(map(lambda x: x[2:], scripts))
        self.label =  one_hot(torch.ones(len(scripts)).long()).cuda()

        # TODO:일단 PoC로 하나의 캐릭터 대사만 사용함. 나중에 맞춰서 개선할 필요 존재
        # 이 때 one-hot encoding이 된 형태를 사용해야 함

    def __len__(self):
        return len(self.data_in)

    def __getitem__(self, idx):
        seq_in = torch.tensor(self.data_in[idx]).cuda().long()
        seq_out = torch.tensor(self.data_out[idx]).cuda().long()
        return seq_in, self.label[idx]

