"""
Gretchen is directing a new play with M scenes performed by N actors, where each actor only 
appears in exactly one scene. To ensure that the distribution is perfect, she performs the following actions:

Assign actor Ni to scene Mi.

Count the number of scenes having less than P actors assigned to them.
Given a list of actions, determine the distribution of actors in Gretchen's play.

Input Format:

The first line contains three space-separated integers, M, N, and Q, respectively; M is the number of scenes, 
N is the number of actors, and Q is the number of actions Gretchen plans to perform. N and M use zero-based indexing.

The second line contains NN space-separated integers; 
the ithith integer represents the scene, Mi, that actor Ni is initially assigned to.

The QQ subsequent lines describe Gretchen's actions; each of these lines starts with an integer, 
A, which corresponds to Action 1 or Action 2 (as detailed in the Problem Statement).

When A=1 (Action 1), it will be followed by two space-separated integers, 
NiNi and Mi, respectively; this action says to assign actor Ni to scene MiMi.

When A=2 (Action 2), it will be followed by a single integer, P; 
this action says to count the number of segments having <P actors assigned to them.

Note: All Action 1 actions are permanent, so each Action 1 affects all future actions.

Constraints: 

1 ≤ M , N, Q ≤ 105
0 <= Mi <= M−1
0 <= Ni <= N−1
1 <= P <= N

Output Format:

For each Action 2, print the number of scenes having <P<P actors on a new line.

Sample Input:

5 5 6
0 1 2 3 4
2 2
1 0 2
2 2
2 1
1 3 1
2 2

Sample Output:

5
4
1
3
"""


first_line = map(int, str(raw_input()).split(' '))
second_line = map(int, str(raw_input()).split(' '))

# M is num scenes
M = first_line[0]

# N is num actors
N = first_line[1]

# Q is num actions
Q = first_line[2]

ACTIONS = []
for i in range(Q):
    ACTIONS.append(map(int, str(raw_input()).split(' ')))

    
def run_play(n, m, q, actions, initial_distro):
    # First assign scenes to actors
    play_dist = {str(i): [] for i in range(m)} # key/value will be actor_number: scene_number
    
    actor_num = 0
    for scene_num in initial_distro:
        play_dist[str(actor_num)] = str(scene_num)
        actor_num += 1
    
    for action in actions:
        
        if int(action[0]) == 1:
            actor_num = str(action[1])
            scene_num = str(action[2])
            play_dist[actor_num] = scene_num
            
        if int(action[0]) == 2:
            P = int(action[1])
            values = play_dist.values()
            counts = [values.count(str(i)) for i in range(m)]
            print len(filter(lambda count: count < P, counts))
            
            
        
                    
run_play(N, M, Q, ACTIONS, second_line)