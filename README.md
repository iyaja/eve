# EVE: The EVer Evolving Deep Learning Optimizer

 2D Convex Surface             |  2D Non-Convex Surface          | 3D Surface with Saddle Point 
:-------------------------:|:-------------------------:|:-------------------------:
![](assets/convex_eve.gif)  |  ![](assets/non_convex_eve.gif) | ![](assets/3d_surface_eve.gif)

EVE is a new optimizer library built on top of PyTorch that combines the best of multiple state-of-the-art optimizer algorithms into one flexible, infinitely customizable super-optimizer.

The goal of EVE is not to provide one final, static optimizer, but rather an interface to a PyTorch optimizer that will continue to implement the latest, well-tested methods from modern research.

At present, EVE implements (and combines) the following algorithms:
- [Adam](https://arxiv.org/abs/1412.6980)
- [RAdam](https://arxiv.org/abs/1908.03265v1)
- [LARS](https://arxiv.org/abs/1708.03888)
- [LookAhead](https://arxiv.org/abs/1907.08610)

We are currently working on adding in the following variants as well:
- [LAMB](https://arxiv.org/abs/1904.00962)
- [DiffGrad](https://arxiv.org/abs/1909.11015)
- [AdaMod](https://arxiv.org/abs/1910.12249)
- [DeepMemory](https://github.com/lessw2020/Best-Deep-Learning-Optimizers/tree/master/DeepMemory)
- Marina
