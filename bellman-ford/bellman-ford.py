class Edge:
    def __init__(self, u, v, weight):
        self.u = u  # ต้นทาง
        self.v = v  # ปลายทาง
        self.weight = weight  # น้ำหนักของขอบ

def bellman_ford(vertices, edges, source):
    # กำหนดค่าเริ่มต้นของระยะทางจากต้นทางไปยังโหนดอื่น ๆ เป็น Infinity
    distance = {v: float('inf') for v in vertices}
    distance[source] = 0  # ระยะทางจากต้นทางถึงตัวเองเป็น 0

    # ทำการ Relax ขอบทั้งหมด (V - 1) ครั้ง
    for i in range(len(vertices) - 1):
        print(f"รอบที่ {i + 1}")
        for edge in edges:
            if distance[edge.u] + edge.weight < distance[edge.v]:
                distance[edge.v] = distance[edge.u] + edge.weight
                print(f"อัปเดตระยะทาง {edge.u} → {edge.v} = {distance[edge.v]}")

    # ตรวจสอบวงจรลูปติดลบ
    for edge in edges:
        if distance[edge.u] + edge.weight < distance[edge.v]:
            print("ตรวจพบวงจรลูปติดลบ (Negative cycle)!")
            return None

    return distance


# 🔗 ตัวอย่างกราฟ
vertices = ['A', 'B', 'C', 'D']
edges = [
    Edge('A', 'B', 4),
    Edge('A', 'C', 5),
    Edge('B', 'C', -3),
    Edge('C', 'D', 2)
]

# 🔁 เรียกใช้ฟังก์ชัน Bellman-Ford จากโหนด A
distances = bellman_ford(vertices, edges, 'A')

# 📊 แสดงผลลัพธ์
if distances:
    print("\nผลลัพธ์ระยะทางจาก A:")
    for v in vertices:
        print(f"ระยะทางไป {v} = {distances[v]}")

