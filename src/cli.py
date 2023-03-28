import argparse
from rich.console import Console
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from skrf.io.touchstone import Touchstone

console = Console()

def command1(args):
    console.print(f"Running command 1 with arguments {args}")

def command2(args):
    console.print(f"Running command 2 with arguments {args}")

def main():
    parser = argparse.ArgumentParser(description='My CLI Tool')
    subparsers = parser.add_subparsers()

    # Command 1
    parser_command1 = subparsers.add_parser('command1', help='Command 1 help')
    parser_command1.add_argument('arg1', metavar='arg1', type=str, help='Command 1 argument 1')
    parser_command1.add_argument('arg2', metavar='arg2', type=int, help='Command 1 argument 2')
    parser_command1.set_defaults(func=command1)

    # Command 2
    parser_command2 = subparsers.add_parser('command2', help='Command 2 help')
    parser_command2.add_argument('arg1', metavar='arg1', type=float, help='Command 2 argument 1')
    parser_command2.add_argument('--arg2', type=bool, help='Command 2 argument 2', default=False)
    parser_command2.set_defaults(func=command2)

    args = parser.parse_args()

    # Check if any arguments were passed
    if not vars(args):
        # Create menu items
        menu_items = {
            '1': 'Run Command 1',
            '2': 'Run Command 2',
            'q': 'Quit',
        }

        # Create completer for menu items
        completer = WordCompleter(list(menu_items.keys()))

        while True:
            # Print menu
            console.print("[bold]Welcome to My CLI Tool![/bold]\n")
            for key, value in menu_items.items():
                console.print(f"  [bold]{key}[/bold]. {value}")

            # Prompt user for input
            user_input = prompt("Please enter your choice: ", completer=completer)

            # Execute user's choice
            if user_input == '1':
                command1(['arg1_value', 42])
            elif user_input == '2':
                command2([3.14, True])
            elif user_input == 'q':
                console.print("Goodbye!")
                break

            console.print("\n")

        return

    args.func(args)

if __name__ == '__main__':
    file = Touchstone('./ring_slot.s2p')
    print(file)

