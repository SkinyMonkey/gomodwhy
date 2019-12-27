#!/usr/local/bin/python3

import sys
from pprint import pprint

def from_stdin():
    graph = {}

    for line in sys.stdin:
        (parent, child) = line.strip().split(' ')
        if graph.get(child) == None:
            graph[child] = { parent : "" }
        else:
            graph[child][parent] = ""

    return graph

def _why(graph, pkg):
    print(pkg)
    tabs = 0
    while True:
        if graph.get(pkg):
            pkg = list(graph[pkg].items())[0][0]
            print('\t' * tabs, pkg)
            tabs = tabs + 1
        else:
            break

def why(graph, pkg):
    count = 0
    for key in graph.keys():
        if key.find(pkg) >= 0:
            if count > 0:
                print("---------------------------------------------------------------------------------")
            _why(graph, key)
            count += 1

def main():
    g = from_stdin()

    for module in sys.argv[1:]:
        why(g, module)

if __name__ == '__main__':
    main()
