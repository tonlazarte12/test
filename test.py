import torch

a = torch.tensor([1, 2, 3], device='cuda:0')
print(a.size())