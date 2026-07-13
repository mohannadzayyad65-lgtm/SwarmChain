from block import Block
import time
import random

class Node:
    def __init__(self, name: str, stake: float = 1000.0):
        self.name = name
        self.stake = stake
        self.reputation = 1.0
        self.chain = []
        self.pheromone_influence = 1.0 + (stake / 10000)  # كلما زاد Stake زاد التأثير

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
        
        # تعزيز الفيرومون حسب Stake
        boost = 5.0 * self.pheromone_influence
        new_block.pheromone += boost
        print(f"🟢 {self.name} (Stake: {self.stake}) أضاف كتلة {new_block.index} | الفيرومون: {new_block.pheromone:.2f}")
