leader_all = []
with open('leaderboards.txt', 'r') as leader:
    for i in leader:
        
        leader_all.append(i.strip().split(' '))
        
print(leader_all)
