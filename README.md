
<!--
I finally solved the problem. I did cd rl_gym../gym_collision... and then  git push --set-upstream --force origin main
finally pushed the recursive module to git

        px = agent[0]
        py = agent[1]
        gx = agent[2]
        gy = agent[3]
        pref_speed = agent[4]
        radius = agent[5]
-->


This code is an extension of the gym-collision-avoidance project. To install the original gym environment, please refer to the documentation.

To incorporate a new policy, follow these steps:

Add the name, sensor type, and other information of the new policy in /gym-collision-avoidance/gym_collision_avoidance/experiments/src/env_utils.py.

Add the new policy to ./gym_collision_avoidance/envs/policies.

Import the new policy in test cases, e.g., from gym_collision_avoidance.envs.policies.MPC import MPC.
# Decentralized Multi-agent collision avoidance control algorithm in MPC with message communication
This research seeks to address a fundamental question: Can enhancing agents' awareness of each other's future motions and leveraging this information for trajectory planning lead to safer and more efficient driving, ultimately reducing collisions? 

We investigate how an agent's ability to perceive the plans of others influences its performance relative to agents without this capability. Furthermore, we aim to understand the cumulative impact of progressively integrating more vehicle-to-vehicle (V2V) communication among agents. By systematically increasing the prevalence of this communication feature until it is universally adopted, we analyze its effects on the overall system of systems.
<img src=(https://github.com/iastate/multiagents/assets/95378237/d655a2eb-fbb2-4c4e-9f1a-72c37022c10f) width="200">

# Comparison between Linear Prediction and Static Prediction
https://github.com/iastate/multiagents/assets/95378237/d655a2eb-fbb2-4c4e-9f1a-72c37022c10f
In this experiment, we tested two commonly used strategies for vehicle path prediction. We found that although widely used in practice, applying the linear prediction method to every agent in a multi-agent system can lead to catastrophic outcomes.

1. **Taking the agent as static:**
$$\mathbf{x}(t_0 + \Delta t) = \mathbf{x}(t_0)$$
3. **Assuming the agent is continuing its current behavior and using linear prediction:**
$$\( \vec x(t_0+\Delta t) = \vec x(t_0) + \vec{v}(0) \cdot \Delta t \)$$, especially for a short time horizon.

In our experiment, the time step (\( \Delta t \)) for each iteration is 0.1s, and the prediction horizon is 10, so the total prediction horizon is 1s.

## Table of Collision Percentage

| static / linear prediction | 2 agents | 3 agents |
|-----------------------------|----------|----------|
| 1 m/s                        | 0%/60.2% | 0.316%/66.04% |
| 2 m/s                        | 0.802%/80.56% | 0%/88.13% |
| 3 m/s                        | 6.012%/83.57% | 2.605%/100% |
| 4 m/s                        | 36.673%/83.17% | 51.904%/100% |

## Experiment Details

Include any additional details about the experiment, methodology, or results here.

## Usage

Provide instructions or code snippets for using any associated software or scripts.

## License

Specify the license under which your experiment or code is distributed.
ion multiagent systems is symmetrically  to oscillation and diverge. 
\end{document}
 
