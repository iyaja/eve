# EVE: The EVer Evolving Deep Learning Optimizer

 2D Convex Surface             |  2D Non-Convex Surface          | 3D Surface with Saddle Point 
:-------------------------:|:-------------------------:|:-------------------------:
![](images/convex_eve.gif)  |  ![](images/non_convex_eve.gif) | ![](images/3d_surface_eve.gif)

EVE is a new optimizer library built on top of PyTorch that combines the best of multiple state-of-the-art optimizer algorithms into one flexible, infinitely customizable super-optimizer.

The goal of EVE is not to provide one final, static optimizer, but rather an interface to a PyTorch optimizer that will continue to implement the latest, well-tested methods from modern research.

## Installation and Getting Started

The simplest way to use EVE in your PyTorch models is to install it using pip:

```pip install eve-optimizer```

Then, the main EVE optimizer can be imported as follows:

```from eve.optimizers import eve```

This will import a function that returns a `torch.optim.Optimizer` object, which can be used in the usual way.

The EVE library also provides a direct interface to other optimizers (like Ranger, RAdam, etc.) that were used in part or were built upon to create the main EVE optimizer. These can also be accessed from `eve.optimizers` in the same way.

## What Exactly is EVE?
At present, EVE implements (and combines) the following algorithms:
- [Adam](https://arxiv.org/abs/1412.6980)
- [RAdam](https://arxiv.org/abs/1908.03265v1)
- [LARS](https://arxiv.org/abs/1708.03888)
- [LAMB](https://arxiv.org/abs/1904.00962)
- [LookAhead](https://arxiv.org/abs/1907.08610)
- [DiffGrad](https://arxiv.org/abs/1909.11015)

We are currently working on adding in the following variants as well:
- [AdaMod](https://arxiv.org/abs/1910.12249)
- [DeepMemory](https://github.com/lessw2020/Best-Deep-Learning-Optimizers/tree/master/DeepMemory)
- Marina
