import random
import numpy as np
import torch as th
from torch import nn
import logging
from os.path import join
logging.disable(logging.ERROR) # reduce clutter, remove if something doesn't work to see the error logs.


class NatureCNN(nn.Module):
    """
    CNN from DQN nature paper:
        Mnih, Volodymyr, et al.
        "Human-level control through deep reinforcement learning."
        Nature 518.7540 (2015): 529-533.

    Nicked from stable-baselines3:
        https://github.com/DLR-RM/stable-baselines3/blob/master/stable_baselines3/common/torch_layers.py

    :param input_shape: A three-item tuple telling image dimensions in (C, H, W)
    :param output_dim: Dimensionality of the output vector
    """

    def __init__(self, input_shape, output_dim):
        super().__init__()
        n_input_channels = input_shape[0]
        self.cnn = nn.Sequential(
            nn.Conv2d(n_input_channels, 32, kernel_size=8, stride=4, padding=0),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=4, stride=2, padding=0),
            nn.ReLU(),
            nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=0),
            nn.ReLU(),
            nn.Flatten(),
        )

        # Compute shape by doing one forward pass
        with th.no_grad():
            n_flatten = self.cnn(th.zeros(1, *input_shape)).shape[1]

        self.linear = nn.Sequential(
            nn.Linear(n_flatten, 512),
            nn.ReLU(),
            nn.Linear(512, output_dim)
        )

    def forward(self, observations: th.Tensor) -> th.Tensor:
        return self.linear(self.cnn(observations))

class ResearchPotatoWrapper():
    def __init__(self, model_dir):

        modelname = "research_potato.pth"
        kmeans_modelname = "centroids_for_research_potato.npy"

        self.kmeans_filepath = join(model_dir,kmeans_modelname)
        self.model_filepath = join(model_dir,modelname)
        # use gpu if available.
        self.dev = th.device("cuda:0" if th.cuda.is_available() else "cpu")
        # load and count centroids
        self.action_centroids = np.load(self.kmeans_filepath)
        self.num_actions = self.action_centroids.shape[0]
        # setup network
        self.network = NatureCNN((3, 64, 64), self.num_actions).to(self.dev)
        self.network.load_state_dict(th.load(self.model_filepath,map_location=self.dev))
        
        # list of descrete actions to sample from (usually [0..99]
        self.action_list = np.arange(self.num_actions)
    
    def predict_action(self,obs):
        # Process the action:
        #   - Add/remove batch dimensions
        #   - Transpose image (needs to be channels-last)
        #   - Normalize image
        obs = th.from_numpy(obs['pov'].transpose(2, 0, 1)[None].astype(np.float32) / 255).to(self.dev)
        
        #forward
        logits = self.network(obs)
        # softmax(logits) = probabilities
        probs = th.softmax(logits,dim=1)[0]
        # to numpy. overwrite old tensor
        probs = probs.detach().cpu().numpy()
        # sample
        discrete_action = np.random.choice(self.action_list,p=probs)
        # get nearest centroid
        action = self.action_centroids[discrete_action]

        # get dict for env
        minerl_action = {"vector":action}

        return minerl_action

