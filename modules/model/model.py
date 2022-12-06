import torch
import torch.nn as nn

from flows4ad.modules.embedding import get_embedding_instace
from flows4ad.modules.flow import get_flow_instace


class GeneralModel(nn.Module):
    def __init__(self, model_config):
        super().__init__()
        self.config = model_config

        self.embedding = get_embedding_instace(self.config.embedding_config)
        self.flow = get_flow_instace(self.config.flow_config)
    
    def forward(self, x, **kwargs):
        x_embedded = self.embedding(x)
        x_transformed, log_det = self.flow(x_embedded, **kwargs)

        return x_transformed, log_det