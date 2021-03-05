import aisd1
import math


def Dijkstra(vertices, edges, start_v):
    d = []
    poprzednik = []
    for i in range(vertices):
        d.append(math.inf)
        poprzednik.append(None)
    d[start_v] = 0
    Q = aisd1.PriorityQueue()
    for vert in range (vertices):
        vertex = aisd1.QueueItem(vert, d[vert])
        Q.enqueue(vertex)
    while Q.__len__() != 0:
        u = Q.pop()
        for edge in edges[u.value]:
            v = edge[0]
            if d[v] > d[u.value] + edge[1]:
                d[v] = d[u.value] + edge[1]
                poprzednik[v] = u.value
                Q.priority(v, d[v])

    for vert in range (vertices):
        print(vert, d[vert])

    paths(vertices, d, poprzednik, start_v, edges)

def paths(vertices, d, poprzednik, start_v, edges):
    for vertex in range(vertices):
        print("Ścieżka do " + str(vertex) + ": ")
        v = vertex
        w = poprzednik[vertex]
        while v != start_v and w != None:
            edge_vw = None
            for edge in edges[w]:
                if edge[0] == v:
                    edge_vw = edge
            print(v, edge_vw[1])
            v = w
            w = poprzednik[w]


def main():
    n = int(input())
    m = int(input())
    edges = []
    for i in range(n):
        edges.append([])
    for i in range(m):
        line = input().split()
        u = int(line[0])
        v = int(line[1])
        w = float(line[2])
        edges[u].append((v, w))
    start_v = int(input())
    Dijkstra(n, edges, start_v)




if __name__ == "__main__":
    main()