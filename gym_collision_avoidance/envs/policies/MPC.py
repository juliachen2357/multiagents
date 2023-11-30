import numpy as np
from gym_collision_avoidance.envs.util import wrap
import math
#import cvxpy as cp
#import sympy as sp
#import do_mpc
from matplotlib import rcParams
import matplotlib.pyplot as plt
from scipy.optimize import Bounds
from scipy.optimize import minimize
class MPC(object):

    def __init__(self, str="MPC"):
        self.str = str
        self.is_still_learning = False
        self.is_external = False
        self.is_external = False
    def l2normsq(x, y):
        return (x[0]-y[0])**2 + (x[1]-y[1])**2
    def l2norm(x, y):
        return math.sqrt(MPC.l2normsq(x,y))       
    def near_goal_smoother(self, dist_to_goal, pref_speed, heading, raw_action):
        kp_v = 0.5;kp_r = 1
        if dist_to_goal < 2.0:
            near_goal_action = np.empty((2,1))
            pref_speed = max(min(kp_v * (dist_to_goal-0.1), pref_speed), 0.0)
            near_goal_action[0] = min(raw_action[0], pref_speed)
            turn_amount = max(min(kp_r * (dist_to_goal-0.1), 1.0), 0.0) * raw_action[1]
            near_goal_action[1] = wrap(turn_amount + heading)
        if dist_to_goal < 0.3:
            near_goal_action = np.array([0., 0.])
        else:
            near_goal_action = raw_action
        return near_goal_action    
    def find_next_action(self, obs, agents, i,message):
          # Prediction horizon
        #x=np.array([obs.pos_global_frame])
        N = 10
        k1=10
        Traj=np.zeros((1,N*2))[0]
        Traj[0]=agents[i].pos_global_frame[0]
        Traj[N]=agents[i].pos_global_frame[1]
        bounds = Bounds(-2,2)
        dt=0.1
        discount_factor=0.7
        def obj_fun(arg):

            Traj=np.zeros((1,N*2))[0]
            Traj[0]=agents[i].pos_global_frame[0]
            Traj[N]=agents[i].pos_global_frame[1]
            res=0
            for num in range(1,N):
                Traj[num]=Traj[num-1]+arg[num-1]*np.cos(arg[N-1+num-1]+agents[i].heading_global_frame)*0.1
                Traj[N+num]=Traj[N+num-1]+arg[num-1]*np.sin(arg[N-1+num-1]+agents[i].heading_global_frame)*0.1
            for l in range(0,N):
                res=res+discount_factor*0.7**l*MPC.l2norm(np.array([Traj[l],Traj[N+l]]),agents[i].goal_global_frame)
                if False:
                    for ag in range(len(agents)):
                            if ag!=i and ag in message:
                                res=res+discount_factor*0.7**l*0.1/(0.0001+MPC.l2norm([Traj[l],Traj[N+l]],[message[ag][l],message[ag][l+int(len(message[ag])/2)]]))**8
                            elif ag!=i:
                                res=res+discount_factor*0.7**l*0.1/(0.0001+MPC.l2norm([Traj[l],Traj[N+l]],agents[ag].pos_global_frame))**8

                else:
                    for ag in range(len(agents)):
                        if ag!=i:
                            res=res+k1*discount_factor*0.7**l*0.1/(0.0001+MPC.l2norm([Traj[l],Traj[N+l]],agents[ag].pos_global_frame))**8


                
            return res
        v=np.zeros((1,(2*(N-1))))[0]
        res = minimize(obj_fun,v,method='nelder-mead',options={'xtol': 1e-8, 'disp': True},bounds=bounds)
        arg=res.x
        


        Traj=np.zeros((1,N*2))[0]
        Traj[0]=agents[i].pos_global_frame[0]
        Traj[N]=agents[i].pos_global_frame[1]
        for num in range(1,N):
                Traj[num]=Traj[num-1]+v[num-1]*np.cos(arg[N-1+num-1]+agents[i].heading_global_frame)*0.1
                Traj[N+num]=Traj[N+num-1]+v[num-1]*np.sin(arg[N-1+num-1]+agents[i].heading_global_frame)*0.1
            
        return self.near_goal_smoother(obs['dist_to_goal'], arg[0], arg[N], [ arg[0], arg[N]]),Traj

        

        







