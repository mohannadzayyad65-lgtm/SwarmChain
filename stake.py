from node import Node

class StakedNode(Node):
    def __init__(self, name: str, stake: float = 1000.0):
        super().__init__(name)
        self.stake = stake          # كمية الرهان (Stake)
        self.reputation = 1.0       # سمعة مرتبطة بالفيرومون

    def slash(self, amount: float):
        self.stake = max(0, self.stake - amount)
        self.reputation *= 0.7
        print(f"⚠️  {self.name} تم خصم {amount} من Stake | Stake المتبقي: {self.stake}")

# مثال
if __name__ == "__main__":
    node = StakedNode("Validator-A", stake=5000)
    node.add_block(["Test Tx"])
    node.slash(500)   # عقاب
    print(f"Stake: {node.stake} | Reputation: {node.reputation:.2f}")
