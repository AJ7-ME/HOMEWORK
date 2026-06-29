import random

MOVES = ["rock", "paper", "scissors"]

BEATS = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}
class AIPlayer:
    def __init__(self):
        self.player_history = []

    def choose_move(self):
        if len(self.player_history) < 3:
            return random.choice(MOVES)

        frequency = {move: self.player_history.count(move) for move in MOVES}
        common_move = max(frequency, key=frequency.get) # Find the most common move

        counter_move = BEATS[common_move]
        if random.random() < 0.2:
            return random.choice(MOVES)
        return counter_move
    
def get_winner(player, ai):
    if player == ai:
        return "tie"
    elif BEATS[player] == ai:
        return "ai"
    else:
        return "player"

def main():
    ai = AIPlayer()

    player_score = 0
    ai_score = 0

    print("🎮 Welcome to Rock Paper Scissors!")
    print("Type 'quit' to stop playing.\n")

    while True:
        player = input("Choose rock, paper, or scissors: ").lower().strip()

        if player == "quit":
            break

        if player not in MOVES:
            print("Invalid move. Try again.\n")
            continue

        ai_move = ai.choose_move()
        ai.player_history.append(player)

        print(f"AI chose: {ai_move}")

        result = get_winner(player, ai_move)

        if result == "player":
            player_score += 1
            print("You win this round! ")
        elif result == "ai":
            ai_score += 1
            print("AI wins this round! ")
        else:
            print("It's a tie! ")

        print(f"Score -> You: {player_score} | AI: {ai_score}\n")

    print("\n Final Score")
    print(f"You: {player_score} | AI: {ai_score}")
    print("Thanks for playing!")
#vv common for all python pygame stuff
if __name__ == "__main__":
    main()