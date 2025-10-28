from adventure.utils import read_events_from_file
import random
from rich.prompt import Prompt
from rich import print

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[bright_red]You stand still, unsure what to do. The forest swallows you.[/bright_red]"

def left_path(event):
    return "[bright_cyan][b]You walk left.[/b] " + event + "[/bright_cyan]"

def right_path(event):
    return "[green3][b]You walk right.[/b] " + event + "[/green3]"

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    print("[grey37]You wake up in a dark forest. You can go left or right.[/grey37]")
    while True:
        choice = Prompt.ask("[b]\nWhich direction do you choose? ([i]left[/i]/[i]right[/i]/[i]exit[/i])[/b]")
        choice = choice.strip().lower()
        if choice == 'exit':
            break
        
        print(step(choice, events))
