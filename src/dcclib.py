from typing import Union
from os import system, name
from shutil import get_terminal_size

class DynamicCenteredConsole:
    """
    A class to manage and display text in the center of the terminal screen.
    It handles text updates, clears the screen, and centers the text both horizontally and vertically.
    """

    def __init__(self):
        """
        Initializes the CentredConsole object by setting up the chunks list and
        determining the terminal size (width and height).
        """
        self.chunks: list[str] = []  # List to hold text chunks
        self.max_width, self.max_height = get_terminal_size()  # Terminal dimensions

    @staticmethod
    def clear_console() -> None:
        """
        Clears the terminal screen. The method works cross-platform.
        On Windows, it runs the 'cls' command, while on other platforms (Linux/macOS),
        it runs the 'clear' command.
        """
        system("cls" if name == "nt" else "clear")

    def update(self, data: Union[str, list[str]]) -> None:
        """
        Updates the console with new text or text chunks. The text is then centered both
        horizontally and vertically on the terminal screen.

        Args:
            data (Union[str, list[str]]): A string or a list of strings to display.
        """
        # Add the new data to the chunks list
        if isinstance(data, list):
            self.chunks.extend(data)  # Add list of strings
        elif isinstance(data, str):
            self.chunks.append(data)  # Add a single string

        # Concatenate all text chunks into a single string
        concatenated = "\n".join(self.chunks)

        # Calculate vertical space required for centering
        space_needed = self.max_height - len(concatenated.splitlines())
        top_margin = space_needed // 2
        bottom_padding = space_needed - top_margin

        # Clear the screen before displaying the updated text
        self.clear_console()

        # Print the text with vertical and horizontal centering
        print("\033[1;32m\n" * top_margin + "\n".join(
            [line.center(self.max_width) for line in concatenated.splitlines()]
        ) + "\n" * bottom_padding)
