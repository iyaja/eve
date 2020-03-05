# EVE: The EVer Evolving Deep Learning Optimizer

![Upload Python Package](https://github.com/iyaja/eve/workflows/Upload%20Python%20Package/badge.svg) [![HitCount](http://hits.dwyl.com/iyaja/eve.svg)](http://hits.dwyl.com/iyaja/eve)

EVE is a new optimizer library built on top of PyTorch that combines the best of multiple state-of-the-art optimizer algorithms into one flexible, infinitely customizable super-optimizer.

The goal of EVE is not to provide one final, static optimizer, but rather an interface to a PyTorch optimizer that will continue to implement the latest, well-tested methods from modern research.

The current implementation of EVE is able to beat Adam and other near state-of-the-art optimizers without a significant increase in compute time. Below are some inital results from EVE.

## 5 Epoch Training Run on Imagenette with ResNet18

### Adam (Final Accuracy = 40.00%)

|epoch |	train_loss |	valid_loss |	accuracy |	time|
|------|------------|------------|----------|-----|
|0 |	2.479557 |	9.522848 |	0.129936 |	00:33|
|1 |	2.223202 |	2.041943 |	0.433121 |	00:33|
|2 |	2.529300 |	2.300190 |	0.212994 |	00:34|
|3 |	2.018234 |	1.866597 |	0.347261 |	00:35|
|4 |	1.780924 |	1.732265 |	**0.400000** |	00:35|

### EVE (Final Accuracy = 70.62%)

|epoch |	train_loss |	valid_loss |	accuracy |	time|
|------|------------|------------|----------|-----|
|0 |	2.396812 |	2.617368 |	0.335287 |	00:39
|1 |	2.170482 |	1.626544 |	0.478726 |	00:39
|2 |	1.526003 |	1.672156 |	0.501146 |	00:39
|3 |	0.956125 |	0.949652 |	0.696306 |	00:39
|4 |	0.567583 |	0.949395 |	**0.706242** |	00:39
 
## 5 Epoch Training Run on CIFAR10 with ResNet18
 
 ### Adam (Final Accuracy = 51.86%)
 
|epoch |	train_loss |	valid_loss |	accuracy |	time|
|------|------------|------------|----------|-----|
|0 |	1.975239 |	1.939689 |	0.392900 |	00:46|
|1 |	3.909453 |	5.174701 |	0.200900 |	00:47|
|2 |	1.880459 |	2.725230 |	0.369800 |	00:47|
|3 |	1.455202 |	3.867605 |	0.489100 |	00:46|
|4 |	1.334342 |	8.826218 |	**0.518600** |	00:46|
 
### EVE (Final Accuracy = 72.86%)

|epoch |	train_loss |	valid_loss |	accuracy |	time|
|------|------------|------------|----------|-----|
|0 |	2.000495 |	1.659529 |	0.399000 |	01:23|
|1 |	1.320091 |	1.335047 |	0.522200 |	01:23|
|2 |	1.095541 |	1.465448 |	0.500100 |	01:24|
|3 |	0.843848 |	0.877310 |	0.694000 |	01:23|
|4 |	0.606318 |	0.797719 |	0.728600 |	01:24|
 
 Here are a few animations demonstrating EVE's convergence properties on simple functions:

 2D Convex Surface             |  2D Non-Convex Surface          | 3D Surface with Saddle Point 
:-------------------------:|:-------------------------:|:-------------------------:
![](images/convex_eve.gif)  |  ![](images/non_convex_eve.gif) | ![](images/3d_surface_eve.gif)

## Installation and Getting Started

The simplest way to use EVE in your PyTorch models is to install it using pip:

```
pip install eve-optimizer
```

Then, the main EVE optimizer can be imported as follows:

```
from eve.optimizers import eve
```

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
