# Repo Organization
As of right now, the outer repo is completely empty as we are working on rendering for the simulator for this project. Once that is complete, there will be info in the outer repo. All things related to this course will live in this folder. 

# Project Background
This project is part of emerge lab, and autonomous vehicle lab. Our lab as successfully published it first paper near spring break. The focus of that paper was augmenting PPO loss to create more human-like agents. 

Here is the motivation for human-like agents. Traditionally trained agents, even if they have a high success rate and low crash rate, have a tendency to drive aggressively. This is bad for 2 main reasons:
- it would drive weirdly and is thus not suitable for deployment into the real world
- it is not suitable to emulate human behavior in simulation and thus cannot be background agents to help train new policies.

We observed that traditonal RL was not able to produce enough rules to capture all weird driving situations and imitation learning produced horrible non-dynamic results. 

The solution proposed in the paper is augmenting PPO with a KL divergence to a human-imitation model. While the human imitation model was terrible, it seemed to have aspects that were useful in avoiding weird driving. 

All of this was explored using nocturne, a 2D RL driving simulation.

This project serves as a sequel in two ways:
- a new simulation: GPUDrive
- further augments PPO with preference learning

## GPUDrive
GPUDrive is built off of madrona which in turn uses an entity component system and runs off the GPU. The result is insanely fast performance. One aspect of this project is finishing the development of GPUDrive, especially the ability to produce renderings of scenes. This is what is currently being worked on. GPUDrive lives in a seperate repo from the repo in which this repo was forked from. 

## Preference Learning
The idea is to show a gorup of driving agents to humans and let them select which they believe to be driving more human lik . Then from there is the hope is that this contribution will lead to the creation of superior drivign agents in a similar manner to the KL divergence example given above. As a lab we believe this is possible as fellow researchers in the NYU Game Innovation Lab have used preference learning for video game map generation. 

# Planned Deliverables
Here is a list of all possible deliveriables:
- rendering tutorial for nocturne and gpudrive
- entity component model toy example
- PPO and reinforcement learning toy example
- preference learning toy example
- agent training tutorial on the HPC*
- actual preference learning project code

Due to the extended time span of this project, I am unsure of when the actual preference learning code will be deliverable. All of the toy example projects will serve as examples of the core concepts of this project to act as tutorials if the actual code ends up being delayed. I will very likely not be making every single one of them as that is a lot and I rather spend time contributing to the core project, not toy examples. If the professor has a particular preference for a toy example, I will focus more on that. 

*Agent training on the HPC may not be possible as it depends if I get an opportunity to train agents. Currently our lab has been strugglign to access the HPC at all (I will jokingly blame professor for stealing all of the GPUs for the course project). The allocation for the course project is not sufficient to train agents (we usually use 24 GPUs for an entire day)