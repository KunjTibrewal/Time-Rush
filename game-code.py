import threading
import os
import sys
import random

def fifty_fifty():
    pass
def switch_question():
    pass
def ask_the_audience():
    pass
def extra_time():
    pass


def check_input_timeout(time_limit):
    result = {"text": None}
    def target_func():
        try:
            result["text"] = input("Please enter your response : ")
        except Exception:
            pass
    print(f"You have {time_limit} seconds to provide your Answer")
    input_thread = threading.Thread(target=target_func)
    input_thread.daemon = True
    input_thread.start()   
    input_thread.join(timeout=float(time_limit))
    if input_thread.is_alive():
        print("\nYour time is over!")
        return False
    else:
        print(f"\nThank you! You entered: {result['text']}")
        return True


#LIFELINES


lifeline = {1: ["50-50", True, fifty_fifty],                            #[0]=LIFELINE 
            2: ["Switch the question", True, switch_question],          #[1]=AVAILABLITY
            3: ["Ask the audience", True, ask_the_audience],            #[2]=FUNCTION
            4: ["Extra time", True, extra_time]}

def lifelines(a):
    if lifeline[int(a)][1]:
        lifeline[int(a)][1] = False
        lifeline[int(a)][2]()
    else:
        print("You have already used the",lifeline[int(a)][0],".")




# Safe initialization for ANSI colors on Windows CMD
if sys.platform == "win32":
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:
        os.system("")

# ---------------------------------------------------------
#  COLOR DEFINITIONS
# ---------------------------------------------------------
C_RESET   = "\033[0m"
C_BOLD    = "\033[1m"
C_GOLD    = "\033[1;33m"
C_CYAN    = "\033[1;36m"
C_GREEN   = "\033[1;32m"
C_RED     = "\033[1;31m"
C_BLUE    = "\033[1;34m"
C_MUTED   = "\033[1;30m"

# ---------------------------------------------------------
# QUESTION BANK (NESTED LIST STRUCTURE)
# Structure: [ Question_String, Option_1, Option_2, Option_3, Option_4, Correct_Option_Index (1-4) ]
# ---------------------------------------------------------
Q_List1 = [
    [
        "Which programming language is known as the 'Snake' language?",
        "C++",
        "Java",
        "Python",
        "Ruby",
        3
    ],
    [
        "What is the time complexity of searching in a balanced BST?",
        "O(1)",
        "O(log N)",
        "O(N)",
        "O(N^2)",
        2
    ],
    [
        "In KBC, what is the highest cash prize usually offered?",
        "1 Crore",
        "5 Crore",
        "7 Crore",
        "10 Crore",
        3
    ],
    [
        "Which keyword is used to declare a function in Python?",
        "func",
        "def",
        "function",
        "create",
        2
    ]
]

PRIZE_TREE = ["₹ 10,000", "₹ 50,000", "₹ 1,00,000", "₹ 7 CRORE"]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ---------------------------------------------------------
# UI RENDERING
# ---------------------------------------------------------
def render_ui(q_data, current_q_idx):
    clear_screen()
    question_text = q_data[0]
    options = [q_data[1], q_data[2], q_data[3], q_data[4]]

    # Header
    print(f"{C_GOLD}{C_BOLD}" + "=" * 78 + f"{C_RESET}")
    print(f"{C_GOLD}{C_BOLD}   T I M E   R U S H   --   K B C   T E R M I N A L   E D I T I O N{C_RESET}".center(88))
    print(f"{C_GOLD}{C_BOLD}" + "=" * 78 + f"{C_RESET}\n")

    # HUD Stats
    print(f"  {C_CYAN}Current Prize:{C_RESET} {PRIZE_TREE[current_q_idx]}".ljust(45) + 
          f"{C_BOLD}Question:{C_RESET} {current_q_idx + 1} / {len(Q_List1)}".rjust(35))
    print()

    # Question Frame
    print(f"  {C_BLUE}/" + "=" * 72 + f"\\{C_RESET}")
    print(f" {C_BLUE}/" + f"  {C_BOLD}{question_text}{C_RESET}".center(80) + f"{C_BLUE}\\{C_RESET}")
    print(f"  {C_BLUE}\\" + "=" * 72 + f"/{C_RESET}\n")

    # Options Grid
    opt_labels = ["A", "B", "C", "D"]
    formatted_opts = []

    for i in range(4):
        text = options[i]
        formatted_opts.append(f"{C_CYAN}[{opt_labels[i]}]:{C_RESET} {C_BOLD}{text:<22}{C_RESET}")

    print(f"    {formatted_opts[0].ljust(48)} {formatted_opts[1]}")
    print()
    print(f"    {formatted_opts[2].ljust(48)} {formatted_opts[3]}")
    print("\n" + f"{C_MUTED}" + "-" * 78 + f"{C_RESET}")

    # Lifelines Section Display
    print(f"  {C_GOLD}{C_BOLD}LIFELINES:{C_RESET}  "
          f"{C_GOLD}[1]{C_RESET} 50-50   |   "
          f"{C_GOLD}[2]{C_RESET} Switch Question   |   "
          f"{C_GOLD}[3]{C_RESET} Audience Poll   |   "
          f"{C_GOLD}[4]{C_RESET} Extra Time")
    print(f"{C_MUTED}" + "-" * 78 + f"{C_RESET}")

    # Money Ladder
    ladder_str = f"{C_BOLD}LADDER:{C_RESET} "
    for idx, prize in enumerate(PRIZE_TREE):
        if idx == current_q_idx:
            ladder_str += f"{C_GOLD}► {prize} ◄{C_RESET}  "
        elif idx < current_q_idx:
            ladder_str += f"{C_GREEN}{prize}{C_RESET}  "
        else:
            ladder_str += f"{C_MUTED}{prize}{C_RESET}  "
    print(ladder_str)
    print(f"{C_MUTED}" + "-" * 78 + f"{C_RESET}\n")

# ---------------------------------------------------------
# GAME FLOW
# ---------------------------------------------------------
def play_game():
    # Randomize questions every run
    questions = Q_List1.copy()
    random.shuffle(questions)

    current_idx = 0

    while current_idx < len(questions):
        q_data = questions[current_idx]
        correct_opt = q_data[5]

        while True:
            render_ui(q_data, current_idx)

            user_input = input(f"Enter choice ({C_CYAN}A, B, C, D{C_RESET}) or Lifeline ({C_GOLD}1-4{C_RESET}): ").strip().upper()

            # Handle Lifelines (Input 1, 2, 3, 4)
            lifelines_map = {
                "1": "50-50",
                "2": "Switch Question",
                "3": "Audience Poll",
                "4": "Extra Time"
            }

            if user_input in lifelines_map:
                lifeline_name = lifelines_map[user_input]
                print(f"\n{C_GOLD}{C_BOLD}>>> Lifeline [{user_input}] {lifeline_name} Selected! <<<{C_RESET}")
                # ---------------------------------------------------------
                # YOUR FRIEND CAN INSERT LIFELINE CODE HERE FOR OPTIONS 1-4
                # ---------------------------------------------------------
                input(f"{C_CYAN}Press ENTER to continue...{C_RESET}")
                continue

            # Handle Answers (Input A, B, C, D)
            opt_map = {"A": 1, "B": 2, "C": 3, "D": 4}
            if user_input in opt_map:
                chosen_opt = opt_map[user_input]

                if chosen_opt == correct_opt:
                    print(f"\n{C_GREEN}{C_BOLD}CORRECT ANSWER! You won {PRIZE_TREE[current_idx]}!{C_RESET}")
                    input(f"{C_CYAN}Press ENTER for the next question...{C_RESET}")
                    current_idx += 1
                    break
                else:
                    correct_letter = [k for k, v in opt_map.items() if v == correct_opt][0]
                    show_error_screen(f"WRONG ANSWER! The correct answer was [{correct_letter}].")
                    return
            else:
                print(f"\n{C_RED}Invalid choice! Please select A, B, C, D or Lifeline 1, 2, 3, 4.{C_RESET}")
                input(f"{C_CYAN}Press ENTER to try again...{C_RESET}")

    show_victory_screen()

# ---------------------------------------------------------
# SCREENS (ERROR & VICTORY)
# ---------------------------------------------------------
def show_error_screen(reason):
    clear_screen()
    print(f"\n{C_RED}{C_BOLD}" + "!" * 60)
    print("   G A M E   O V E R")
    print(f"   Reason: {reason}")
    print("!" * 60 + f"{C_RESET}\n")
    input(f"{C_CYAN}Press ENTER to return to the main menu...{C_RESET}")

def show_victory_screen():
    clear_screen()
    print(f"\n{C_GOLD}{C_BOLD}" + "★" * 65)
    print("   C O N G R A T U L A T I O N S ! ! !")
    print("   YOU HAVE CONQUERED TIME RUSH AND WON 7 CRORE!")
    print("★" * 65 + f"{C_RESET}\n")
    input(f"{C_CYAN}Press ENTER to return to the main menu...{C_RESET}")

def main():
    while True:
        clear_screen()
        print(f"{C_GOLD}{C_BOLD}" + "=" * 60 + f"{C_RESET}")
        print(f"{C_GOLD}{C_BOLD}      WELCOME TO TIME RUSH - KBC TERMINAL GAME{C_RESET}")
        print(f"{C_GOLD}{C_BOLD}" + "=" * 60 + f"{C_RESET}\n")
        print(f"  {C_CYAN}[1]{C_RESET} Start Game")
        print(f"  {C_CYAN}[2]{C_RESET} Exit\n")

        choice = input("Select an option (1-2): ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            clear_screen()
            print(f"{C_GOLD}Thanks for playing Time Rush! Goodbye!{C_RESET}")
            break

if __name__ == "__main__":
    main()