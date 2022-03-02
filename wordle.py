from enum import Enum
import random

# not sure what this is about. Is there a nicer way to do this?
class Colour(Enum):
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    NORMAL = "\033[0m"

def _get_colour(pos, submission_word, target_word):
    """Return colour of letter based on proximity to correct answer"""
    char = submission_word[pos]
    if char == target_word[pos]:
        # it's in the right place
        return Colour.GREEN
    elif char not in target_word:
        # it's not in the word at all
        return Colour.RED
    else:
        # it's in the word but not in this place
        submission_inds = [i for i, c in enumerate(submission_word) if c == char]
        target_inds = [i for i, c in enumerate(target_word) if c == char]
        if len(submission_inds) > len(target_inds):
            # we've guessed the letter too many times
            if submission_inds.index(pos) > len(target_inds):
                return Colour.RED
            else:
                return Colour.YELLOW
        else:
            # we've guessed it no more than the number of occurrences therefore all yellow
            return Colour.YELLOW

def _evaluate_submission(submission_word, target_word):
    """quick description"""
    printable = []
    for ind, char in enumerate(submission_word):
        colour = _get_colour(ind, submission_word, target_word)
        printable += [colour.value, char]
    printable.append(Colour.NORMAL.value)
    print("".join(printable))
    return target_word == submission_word

def _validate_submission(submission):
    """Checks submission for length and alphabetic and uppercase"""
    valid = len(submission) == 5 and submission.isalpha() and submission.isupper()
    if not valid:
        print("Please enter a valid word.") 
    return valid

def play_wordle(num_guesses=6):
    """Play a five round game of wordle"""
    with open("words.txt") as f:
        all_five_letter_words = [w.replace("\n", "") for w in f.readlines()]
    
    target_word = random.choice(all_five_letter_words)
    turn_counter = 0
    guessed = False
    while turn_counter < num_guesses and not guessed:
        turn_counter += 1
        valid_submission = False
        while not valid_submission:
            submission = input("({}/{}): Enter a 5 character word: ".format(turn_counter, num_guesses)).upper()
            valid_submission = _validate_submission(submission)
        guessed = _evaluate_submission(submission, target_word)
        if guessed:
            print("Well done!")

    if not guessed:
        print(f"Sorry, the target word was {target_word}. Try again.")

if __name__ == "__main__":
    play_wordle()






