# Author: Ricky Bhatti
# License: Refer to the LICENSE file.

import os
import pandas # TODO: Create a requirements.txt file.

# clear_screen: Method to clear the screen.
clear_screen = lambda: os.system("cls" if os.name == "nt" else "clear")

# main: The main method of the script.
def main():
    clear_screen()
    
    return

# Script was run directly, run the main function.
if __name__ == "__main__":
    main()