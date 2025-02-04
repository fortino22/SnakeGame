import os
import sys

RESET = "\x1b[0m"
BRIGHT_WHITE = "\x1b[97m"
BLUE = "\x1b[34m"
CYAN = "\x1b[36m"
WHITE = "\x1b[37m"

class Logo:
    def clr(self):
        os.system('cls' if os.name == 'nt' else 'clear') 
        sys.stdout.write("\x1b[?25l")
        sys.stdout.flush()

    def print_logo(self):
        """Displays the static ASCII art with color transitions."""
        ascii_art = [
            "                                     *****#                             ",
            "                           ****                  ,****                  ",
            "                      **%   //*(((#####%%(####((((//    **(             ",
            "                  **/  //((#%%&%&&&&&&%&&&&&&#&&&&&%(#(//   **          ",
            "               %*   /(#(%&&&&&&&&&&&&&,,...&&&&&&&&&&&#&(#///  **       ",
            "             **  /(#%&&&&&&&&&&&&&&,,,,,,,,...&&&&&#&&&&&&&%((/  **     ",
            "           **  /(#&&&&&&&&&&&&&&&,,,,,,,,,,,,,..&&&&#&&&&&&&&&#(// **   ",
            "          *  /(#&&&%#&&&&&&&&&,,,,,,,,,,,,,,,(((&&&&&&&&&&%%#&&&#(/  ** ",
            "        ** *(#%%&&&&&&&&&&#&,,,,,,,#,,,,,,(((&&&&&&&&&&&&&&&&&&&&%#(/ %*        ",
            "       ** /(#&&&&&&&&&&&&,,,,,,,,,,,,,,,(((&&&&&&&&&&&&&&&&&&&&&&&&#(/  *       ",
            "      (* /(#&%#&&&&&&&&,,,,,,,,,,,,,,%((&&&&&,,,...&&&&&&&&&%&&&&##&#(/ %*      ",
            "      *  (#&&%&&&&&&&&,,,,,,,,%,,,,,,(((&&&&&,,,,,,,(..%&&&&&&&&&&&&&&&#(/ *#     ",
            "     ** /(%&&&&&&&,,,,,,,,,,,,,,%((&&&&&,,,,,,,,,,,,,...&&&&&&&&&&&&&%(/  *    ",
            "     ** /#%&&&&&&&&,,,,,,,,,,,,,,,(((&&&&,,,,,,,,,,,%,,(..%&&#&&&&&%&&#(  *    ",
            "     *  (#&&&&&&&&&&&%,,,,,(,,,,,,,,(((&&&&,,,,,,,,,,,,,,,...#&&&&&&&&#(/ *    ",
            "     ** /#%&&&&&&&&&&&&&%,,,,,,,,,,,,,,,,(((&&&&,%,,,,,,,,,,,,(..%&&&%&&#(  *   ",
            "     ** /(%&&&&&&&&&&&&&&&%,,,,,,,,,,(((&&&&&,,,%,,,,,,,,,,,(((&&&&&&%(/  *    ",
            "      *  (#&&%&&&&&&&&&&&&&&&,,,,,%((%&&&&%,,,,,,,,,,,,,,(((&&&&&&&&&#(/ *      ",
            "      /* /(#&##&&&&&&&&&&&&&&&&%(((&&&&&,,,,,,,,,,,,,%,(((&&%&&&&%#&%(/ **      ",
            "       ** /(#&&&&&&&&&&&&&&&&&&&&&&&&%,,,%,,,,,,,,,,(((&&&&&&&&&&&&%(/  *       ",
            "        ** .(#&&&&&&&&&&&&#&&&&&&&&,,,,,,,,,,,,,,,(((&&&&&&&&&&&&&#(/ **        ",
            "          *  /(%&&&%#&&&&&&&&&&&%,,,,,,,,,,,,,%(((&&&&&&&&&%#&&%%(/  **        ",
            "           **  ((%&&&&&&&&&&&&&&&&,,,,,,,,,,,(((&&&&%&&&&&&&&&%#(/ **   ",
            "             **  /(#%&&&&&&&&&&&&&&&&,,,,,(((&&&&&&#&&&&&&&%((/  **     ",
            "                *#/(#(&&&&&&&&&&&&&&&,(((&&&&&&&&&&&%&(#/(/  **         ",
            "                  ***  /*(#%%&&#&&&&&&%&&&&&&%&&&&&%(#((/   **          ",
            "                      ***   ///((###%%%%%(%%###((((/    **              ",
            "                           ****                  %***                   ",
            "                                     #*****                             "
        ]
        
        self.clr()

        for line in ascii_art:
            self.print_colored(line)
        
        print("\n")
        print(f"                  Confront the challenges of learning and outgrow   \n")
        print(f"                          the boundaries together ~ 24-2            \n")

    def print_colored(self, line):
        """Print each line with color."""
        for char in line:
            if char == '*':
                sys.stdout.write(f"{BRIGHT_WHITE}{char}")
            elif char == '&':
                sys.stdout.write(f"{BLUE}{char}")
            elif char == ',':
                sys.stdout.write(f"{CYAN}{char}")
            else:
                sys.stdout.write(f"{WHITE}{char}")
        sys.stdout.write("\n")
        sys.stdout.flush()




