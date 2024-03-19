
import random

class GuessTheNumberGame:
  def __init__(self):
    self.target_number = random.randint(1, 100)
    self.guesses_left = 10
    self.game_over = False

  def process_guess(self, guess):
    """Process a player's guess, returning feedback and remaining guesses."""
    if self.game_over:
      return "Game over. Please start a new game to play again.", 0

    self.guesses_left -= 1
    if guess < self.target_number:
      feedback = "Higher"
    elif guess > self.target_number:
      feedback = "Lower"
    else:
      feedback = f"Correct! The number was {self.target_number}."
      self.game_over = True

    if self.guesses_left == 0 and not feedback.startswith("Correct"):
      feedback += f" Out of guesses! The number was {self.target_number}."
      self.game_over = True

    return feedback, self.guesses_left

  def get_game_status(self):
    """Check if the game is over and how many guesses are left."""
    return self.game_over, self.guesses_left
