#A* search implementation using class method

class romania_map:
    def __init__(self):
        self.h_info = {
        "Arad":366, "Mehadia":241, "Bucharest":0, "Neamt":234, "Craiova":160,
        "Oradea":380, "Drobeta":242, "Pitesti":100, "Eforie":161, "Rimnicu Vilcea":193,
        "Fagaras":176, "Sibiu":253, "Giurgiu":77, "Timisoara":329, "Hirsova":151,"Urziceni":80,
        "Iasi":226, "Vaslui":199, "Lugoj":244, "Zerind":374}

        self.road = {
        "Arad":[("Zerind",75),("Sibiu",140),("Timisoara",118)],
        "Mehadia":[("Lugoj",70),("Drobeta",75)],
        "Bucharest":[("Giurgiu",90),("Urziceni",85),("Fagaras",211),("Pitesti",101)],
        "Neamt":[("Iasi",87)],
        "Craiova":[("Pitesti",138),("Rimnicu Vilcea",146),("Drobeta",120)],
        "Oradea":[("Zerind",71),("Sibiu",151)],
        "Drobeta":[("Mehadia",75),("Craiova",120)],
        "Pitesti":[("Bucharest",101),("Craiova",138),("Rimnicu Vilcea",97)],
        "Eforie":[("Hirsova",86)],
        "Rimnicu Vilcea":[("Sibiu",80),("Pitesti",97),("Craiova",146)],
        "Fagaras":[("Sibiu",99),("Bucharest",211)],
        "Sibiu":[("Fagaras",99),("Rimnicu Vilcea",80),("Arad",140),("Oradea",151)],
        "Giurgiyu":[("Bucharest",90)],
        "Timisoara":[("Arad",118),("Lugoj",111)],
        "Hirsova":[("Eforie",86),("Urziceni",98)],
        "Urziceni":[("Hirsova",98),("Bucharest",85)],
        "Iasi":[("Neamt",87),("vaslui",92)],
        "Vaslui":[("Iasi",92),("Urziceni",142)],
        "Lugoj":[("Timisoara",111),("Mehadia",70)],
        "Zerind":[("Oradea",71),("Arad",75)]
        }

    def astar_search(self, start, goal):
        opened_list = {start:(0 + self.h_info[start], 0, [])} #(f, g, path)
        closed_list = set()

        while opened_list:
            current = min(opened_list, key=lambda city: opened_list[city][0]) #finding city with lowest f then pop it
            f, g, path = opened_list.pop(current)

            if current == goal:
                return path + [current]

            if current in closed_list: #skip if already visited
                continue

            closed_list.add(current)

            for neighbour, cost, in self.road.get(current, []):
                if neighbour in closed_list:
                    continue
                new_g = g + cost
                new_f = new_g + self.h_info[neighbour]
                opened_list[neighbour] = (new_f, new_g, path + [current])

        return None
    
#Our main
Romania = romania_map()

Start = "Arad"
Goal = "Bucharest"
shortest_path = Romania.astar_search(Start, Goal)

if shortest_path:
    print(f"Shortest path from {Start} city to {Goal} city is: {shortest_path}")
else:
    print(f"No path available from {Start} city to {Goal} city!")
