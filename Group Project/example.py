import sys

# main.py
# Travis test!
print("What feature would you like to try today?: ")
print("1. Minimum spanning tree using Kruskal's producing graph output\n"
      "2. Shortest path using BFS\n"
      "3. Shortest path using Dijkstra's\n"
      "4. Modify nodes, edges and weights for an adjacency matrix\n"
      "5. Convert adjacency matrix back into .csv")
alg = int(input("Enter the integer corresponding to the feature "))

try:
    while 1 <= alg <= 5:
        if alg == 1:
            import minimizeFeature

            sys.exit(1)
        elif alg == 2:
            import bfs

            sys.exit(1)
        elif alg == 3:
            import DijkstraShortestPath

            sys.exit(1)
        elif alg == 4:
            import GraphClass

            sys.exit(1)
        elif alg == 5:
            import PdGraphUtil

            sys.exit(1)
except:
    print("provide input from the available features")
