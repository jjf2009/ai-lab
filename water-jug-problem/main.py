from collections import deque

def water_jug_bfs(m, n, d):
    if d < 0 or d > max(m, n):
        return -1

    queue = deque([(0, 0, 0)])
    visited = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    visited[0][0] = True

    while queue:
        a, b, count = queue.popleft()

        if (a == d) or (b == d):
            return count

        state1 = (m, b)
        if not visited[state1[0]][state1[1]]:
            visited[state1[0]][state1[1]] = True
            queue.append((state1[0], state1[1], count + 1))

        state2 = (a, n)
        if not visited[state2[0]][state2[1]]:
            visited[state2[0]][state2[1]] = True
            queue.append((state2[0], state2[1], count + 1))

        state3 = (0, b)
        if not visited[state3[0]][state3[1]]:
            visited[state3[0]][state3[1]] = True
            queue.append((state3[0], state3[1], count + 1))

    
        state4 = (a, 0)
        if not visited[state4[0]][state4[1]]:
            visited[state4[0]][state4[1]] = True
            queue.append((state4[0], state4[1], count + 1))


        pour_amount = min(a, n - b)
        state5 = (a - pour_amount, b + pour_amount)
        if not visited[state5[0]][state5[1]]:
            visited[state5[0]][state5[1]] = True
            queue.append((state5[0], state5[1], count + 1))

        pour_amount2 = min(b, m - a)
        state6 = (a + pour_amount2, b - pour_amount2)
        if not visited[state6[0]][state6[1]]:
            visited[state6[0]][state6[1]] = True
            queue.append((state6[0], state6[1], count + 1))

    return -1


def water_jug_dfs(m, n, d):
    if d < 0 or d > max(m, n):
        return -1

    stack = [(0, 0, 0)]
    visited = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    visited[0][0] = True

    while stack:
        a, b, count = stack.pop()

        if (a == d) or (b == d):
            return count

        state1 = (m, b)
        if not visited[state1[0]][state1[1]]:
            visited[state1[0]][state1[1]] = True
            stack.append((state1[0], state1[1], count + 1))

        state2 = (a, n)
        if not visited[state2[0]][state2[1]]:
            visited[state2[0]][state2[1]] = True
            stack.append((state2[0], state2[1], count + 1))

        state3 = (0, b)
        if not visited[state3[0]][state3[1]]:
            visited[state3[0]][state3[1]] = True
            stack.append((state3[0], state3[1], count + 1))

        state4 = (a, 0)
        if not visited[state4[0]][state4[1]]:
            visited[state4[0]][state4[1]] = True
            stack.append((state4[0], state4[1], count + 1))

        pour_amount = min(a, n - b)
        state5 = (a - pour_amount, b + pour_amount)
        if not visited[state5[0]][state5[1]]:
            visited[state5[0]][state5[1]] = True
            stack.append((state5[0], state5[1], count + 1))

        pour_amount2 = min(b, m - a)
        state6 = (a + pour_amount2, b - pour_amount2)
        if not visited[state6[0]][state6[1]]:
            visited[state6[0]][state6[1]] = True
            stack.append((state6[0], state6[1], count + 1))

    return -1


jug1_cap = 5
jug2_cap = 3
target_C = 2

count = water_jug_bfs(jug1_cap, jug2_cap, target_C)
if count != -1:
    print("BFS: Goal state achieved in", count, "steps")
else:
    print("BFS: Goal not achieved")

count = water_jug_dfs(jug1_cap, jug2_cap, target_C)
if count != -1:
    print("DFS: Goal state achieved in", count, "steps")
else:
    print("DFS: Goal not achieved")
