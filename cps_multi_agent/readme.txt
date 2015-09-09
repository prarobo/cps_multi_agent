
I have modified the state labels to describe multiple agents. For instance the initial state from which the game starts (see game_init.png) is given as:

E0_33_R0_10_R1_20_T_E0

E0 - Adversary0
33 - Position of adversary (3,3)
R0 - Agent0
10 - Position of agent0 (1,0)
R1 - Agent1
20 - Position of agent1 (2,0)
T - Turn
E0 - Name of the player with current turn, adversary0 in this case

If there are more that 2 agents, there will be R2_xx, etc to this string before the T_ part of the state label.
