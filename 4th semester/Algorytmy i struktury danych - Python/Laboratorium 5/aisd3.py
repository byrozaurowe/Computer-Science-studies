import aisd1
import sys
import math
import unionfind as u


def Prim(edges, n):
    tree = []
    key = [math.inf for i in range (n)]
    vis = [False for i in range (n)]

    Q = aisd1.PriorityQueue()
    Q.enqueue(aisd1.QueueItem(0, 0))
    while Q.__len__() > 0:
        curV = Q.pop()
        if vis[curV.value] == True:
            continue
        tree.append(curV)
        vis[curV.value] = True
        for u in range(n):
            if edges[u][curV.value]:
                if vis[u] == False and key[u] > edges[u][curV.value]:
                    item = aisd1.QueueItem(u, edges[u][curV.value])
                    item.sec_vert = curV.value
                    Q.enqueue(item)
                    key[u] = edges[u][curV.value]
    sum_weight = 0
    for i in range (1, len(tree)):
        print(tree[i].value, "-", tree[i].sec_vert)
        sum_weight += tree[i].priority
    print("Łączna waga: ", sum_weight)


def main():
    alg = sys.argv[1]
    n = int(input())
    m = int(input())
    edges = []
    for i in range(n):
        edges.append([])
        for j in range(n):
            if i == j:
                edges[i].append(None)
            else:
                edges[i].append(None)
    for i in range(m):
        line = input().split()
        u = int(line[0])
        v = int(line[1])
        w = float(line[2])
        edges[u][v] = w
        edges[v][u] = w

    if alg == "-p":
        Prim(edges, n)

if __name__ == "__main__":
    main()