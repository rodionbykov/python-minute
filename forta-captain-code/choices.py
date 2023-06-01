import random

choices=["Heads", "Tails"]
coinToss=random.choice(choices)
print(coinToss)

animals=["cat", "dog", "horse", "fish", "frog", "toad", "snake", "elephant", "bat", "spider"]
adj=["Big", "Strong", "Small", "Smelly", "Ugly", "Beautifull", "Handsome", "Weak", "Black", "Brown", "Blue", "Green", "Hungry", "Full"]
print(f"{random.choice(adj)} {random.choice(animals)}")