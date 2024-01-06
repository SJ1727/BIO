def init_board_to_pos(n):
    return (n // 5, n % 5)

def add_to_surroundings(pos, p_poses):
    for diff in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new = (pos[0]+diff[0], pos[1]+diff[1])
        if p_poses.get(new) is None:
            p_poses[new] = 1
        else:
            p_poses[new] += 1

positions_with_people = dict()
p, s, n = list(map(lambda x: int(x), input().split()))
steps = list(map(lambda x: int(x), input().split()))

p -= 1
index = 0
for i in range(n):
    p_pos = init_board_to_pos(p)
    
    if positions_with_people.get(p_pos) is None:
        positions_with_people[p_pos] = 1
    else:
        positions_with_people[p_pos] += 1

    p += steps[index % len(steps)]
    p %= 25
    index += 1

for _ in range(n):
    for k, v in dict(positions_with_people).items():
        if v >= 4:
            positions_with_people[k] -= 4
            add_to_surroundings(k, positions_with_people)


for i in range(5):
    for j in range(5):
        if positions_with_people.get((i, j)) is None:
            print("0 ", end="")
        else:
            print(positions_with_people[(i, j)], end=" ")
    print()