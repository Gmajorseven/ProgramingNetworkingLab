class Router:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}  # เพื่อนบ้าน: {router_name: cost}
        self.routing_table = {name: (0, name)}  # {destination: (cost, next_hop)}

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor.name] = cost
        self.routing_table[neighbor.name] = (cost, neighbor.name)

    def update_routing_table(self, neighbor):
        updated = False
        for dest, (neighbor_cost, next_hop) in neighbor.routing_table.items():
            if dest == self.name:
                continue
            new_cost = self.neighbors[neighbor.name] + neighbor_cost
            if dest not in self.routing_table or new_cost < self.routing_table[dest][0]:
                self.routing_table[dest] = (new_cost, neighbor.name)
                updated = True
        return updated

    def print_table(self):
        print(f"Routing Table of {self.name}:")
        for dest, (cost, next_hop) in sorted(self.routing_table.items()):
            print(f"  {dest} -> {cost} via {next_hop}")
        print("")

# สร้าง Router
A = Router('A')
B = Router('B')
C = Router('C')
D = Router('D')

# สร้างลิงก์เชื่อมต่อ
A.add_neighbor(B, 1)
B.add_neighbor(A, 1)

B.add_neighbor(C, 1)
C.add_neighbor(B, 1)

A.add_neighbor(D, 5)
D.add_neighbor(A, 5)

# จัดกลุ่มเป็น Network
network = [A, B, C, D]

# เริ่ม Simulation
rounds = 5
print("เริ่มต้น Simulation...\n")
for r in range(rounds):
    print(f"--- รอบที่ {r + 1} ---")
    updates = 0
    for router in network:
        for neighbor_name in router.neighbors:
            neighbor = next(r for r in network if r.name == neighbor_name)
            if router.update_routing_table(neighbor):
                updates += 1
    for router in network:
        router.print_table()
    if updates == 0:
        print("ตาราง Routing คงที่แล้ว หยุด Simulation\n")
        break

