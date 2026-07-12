from dataclasses import dataclass
from typing import List
import hashlib
import time

@dataclass
class Block:
    index: int
    previous_hash: str
    timestamp: float
    transactions: List[str]
    nonce: int = 0
    pheromone: float = 1.0          # رائحة الفيرومون
    reward: float = 10.0            # المكافأة

    def calculate_hash(self) -> str:
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.transactions}{self.nonce}{self.pheromone}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty: int = 4):
        target = "0" * difficulty
        while self.calculate_hash()[:difficulty] != target:
            self.nonce += 1
        print(f"Block {self.index} mined! Hash: {self.calculate_hash()[:20]}... Pheromone: {self.pheromone:.2f}")

# مثال تشغيل
if __name__ == "__main__":
    genesis = Block(0, "0", time.time(), ["Genesis Block"])
    genesis.mine_block(difficulty=4)
    print("✅ أول بلوك تم تعدينه بنجاح!")
