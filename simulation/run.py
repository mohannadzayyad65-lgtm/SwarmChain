from dataclasses import dataclass

@dataclass
class Chain:
    name: str
    pheromone: float = 10.0
    reward: float = 10.0

def calculate_probability(chains, alpha=2.0, beta=1.0):
    scores = [(c.pheromone ** alpha) * (c.reward ** beta) for c in chains]
    total = sum(scores)
    return [score / total * 100 if total > 0 else 0 for score in scores]

def simulate(rounds=12):
    chains = [
        Chain("A (الصحيحة)", 10.0, 12.0),
        Chain("B (مشبوهة)", 10.0, 10.0),
        Chain("C (سبام)", 10.0, 5.0)
    ]
    
    print("الدورة | A      | B     | C     | احتمال A")
    print("-" * 55)
    
    for r in range(rounds):
        if r < 7:
            chains[0].pheromone += 13
            chains[1].pheromone += 3.5
            chains[2].pheromone += 1
        
        for c in chains:
            c.pheromone *= 0.96
        
        probs = calculate_probability(chains)
        print(f"{r:2d}     | {chains[0].pheromone:6.1f} | {chains[1].pheromone:5.1f} | {chains[2].pheromone:5.1f} | {probs[0]:5.1f}%")

if __name__ == "__main__":
    print("🚀 SwarmChain Simulation\n")
    simulate()
    print("\n✅ المحاكاة انتهت!")
