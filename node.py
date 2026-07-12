from block import Block
import time
import random

class Node:
    def __init__(self, name: str):
        self.name = name
        self.chain: list[Block] = []
        self.pheromone_influence = 1.0  # قدرة العقدة على تعزيز الفيرومون

    def add_block(self, transactions: list[str]):
        previous_hash = self.chain[-1].calculate_hash() if self.chain else "0" * 64
        new_block = Block(
            index=len(self.chain),
            previous_hash=previous_hash,
            timestamp=time.time(),
            transactions=transactions,
            pheromone=1.0
        )
        new_block.mine_block(difficulty=3)
        self.chain.append(new_block)
        
        # تعزيز الفيرومون
        new_block.pheromone += 8 * self.pheromone_influence
        print(f"🟢 {self.name} أضاف كتلة {new_block.index} | فيرومون: {new_block.pheromone:.2f}")

# مثال تشغيل
if __name__ == "__main__":
    node1 = Node("Node-A")
    node1.add_block(["Tx1", "Tx2"])
    print("✅ تم إنشاء أول عقدة بنجاح!")
