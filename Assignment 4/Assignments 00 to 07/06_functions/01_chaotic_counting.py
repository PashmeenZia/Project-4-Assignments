import random

STOP_PROBABILITY = 0.25  # 25% chance to randomly stop

def feeling_lazy():
    """Returns True randomly based on STOP_PROBABILITY."""
    return random.random() < STOP_PROBABILITY

def moody_counter():
    """Counts from 1 to 15, but may stop early depending on mood."""
    for i in range(1, 16):
        if feeling_lazy():
            print("😴 Okay, I'm done counting for now!")
            return
        print(i, end=" ")

def main():
    print("🤔 Let's see how far I feel like counting today (1 to 15)...")
    moody_counter()
    print("\n🎉 That’s all for now!")

if __name__ == '__main__':
    main()
