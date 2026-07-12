from node import Node
import time

class SwarmNetwork:
    def __init__(self):
        self.nodes = []
    
    def add_node(self, name: str):
        node = Node(name)
        self.nodes.append(node)
        print(f"➕ Node {name} added to the swarm")
        return node

    def simulate_consensus(self, transactions: list[str]):
        print("\n🔄 بدء التوافق الجماعي...\n")
        for node in self.nodes:
            node.add_block(transactions[:])
            time.sleep(0.5)  # محاكاة زمن الانتشار

# تشغيل الشبكة
if __name__ == "__main__":
    network = SwarmNetwork()
    
    network.add_node("Validator-1")
    network.add_node("Validator-2")
    network.add_node("Validator-3")
    
    network.simulate_consensus(["Alice pays Bob 10 PHERO", "Bob pays Charlie 5 PHERO"])
    
    print("\n✅ SwarmNetwork تعمل بنجاح! الفيرومون يعمل.")
