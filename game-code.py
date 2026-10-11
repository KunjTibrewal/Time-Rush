import threading
import os
import sys
import random
import ctypes



def extra_time():
    pass

#LIFELINES

def fifty_fifty(q_data):
    correct_opt = q_data[5]  # Correct option number (1-4)
    wrong_options = [
        i for i in range(1, 5)
        if i != correct_opt and q_data[i] is not None]
    eliminated = random.sample(wrong_options, 2)

    for i in eliminated:
        q_data[i] = None

def switch_question(q_data, current_idx, used_questions, Easy_que, Medium_que, Hard_que):
    if current_idx < 5:
        question_pool = Easy_que
        used_set = used_questions["easy"]
    elif current_idx < 10:
        question_pool = Medium_que
        used_set = used_questions["medium"]
    else:
        question_pool = Hard_que
        used_set = used_questions["hard"]

    available = [
        i for i in range(len(question_pool))
        if i not in used_set
    ]

    if not available:
        print(f"\n{C_RED}No unused questions available!{C_RESET}")
        input("Press ENTER to continue...")
        return

    new_idx = random.choice(available)
    used_set.add(new_idx)
    q_data[:] = question_pool[new_idx]
    print(f"\n{C_GREEN}Question switched successfully!{C_RESET}")
    input("Press ENTER to continue...")



def ask_the_audience(q_data, current_idx):
    if current_idx < 5:
        accuracy = 0.95                                                                      #EASY QUESTION AUDIENCE ACCURACY 0.95
    elif current_idx < 10:
        accuracy = 0.85                                                                      #MEDIUM QUESTION AUDIENCE ACCURACY 0.85
    else:
        accuracy = 0.65                                                                      #HARD QUESTION AUDIENCE ACCURACY 0.65
    active_options = [i for i in range(1, 5) if q_data[i] is not None]                       #FOR 50-50 LIFELINE, ELIMINATE OPTIONS
    correct_opt = q_data[5]
    if random.random() < accuracy:
        winner = correct_opt
    else:
        wrong_options = [i for i in active_options if i != correct_opt]
        winner = random.choice(wrong_options)

    while True:
        cuts = sorted(random.sample(range(1, 100), len(active_options) - 1))
        boundaries = [0] + cuts + [100]
        percentages = [boundaries[i + 1] - boundaries[i] for i in range(len(active_options))]
        votes = dict(zip(active_options, percentages))
        if votes[winner] > max(votes[i] for i in active_options if i != winner):
            break

    print(f"\n{C_GOLD}{C_BOLD}       AUDIENCE POLL{C_RESET}")
    print("-" * 40)
    for option in active_options:
        label = "ABCD"[option - 1]
        percentage = votes[option]
        bar = "#" * (percentage // 2)
        print(f"{label} | {bar:<50} {percentage}%")
    print("-" * 40)
    input("Press ENTER to continue...")




lifeline = {1: ["50-50", True, fifty_fifty],                            #[0]=LIFELINE 
            2: ["Switch the question", True, switch_question],          #[1]=AVAILABLITY
            3: ["Ask the audience", True, ask_the_audience],            #[2]=FUNCTION
            4: ["Extra time", True, extra_time]}

def lifelines(a, q_data, current_idx, used_questions, Easy_que, Medium_que, Hard_que):
    if lifeline[int(a)][1]:
        lifeline[int(a)][1] = False
        if int(a) == 2:
            switch_question(q_data, current_idx, used_questions, Easy_que, Medium_que, Hard_que)
        elif int(a) == 3:
            ask_the_audience(q_data, current_idx)
        else:
            lifeline[int(a)][2](q_data)
    else:
        print(f"\n{C_RED}You have already used the {lifeline[int(a)][0]}.{C_RESET}")
        input(f"{C_CYAN}Press ENTER to continue...{C_RESET}")


# Safe initialization for ANSI colors on Windows CMD
if sys.platform == "win32":
    try:
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:
        os.system("")

# ---------------------------------------------------------
# COLOR DEFINITIONS
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
# QUESTION BANKS & SHUFFLE LOGIC
# ---------------------------------------------------------
def select_que_no():
    All_Que, List = [Number for Number in range(10)], []
    while len(List) != 5:
        Select = random.randint(0, len(All_Que) - 1)
        List.append(All_Que[Select])
        Remove = All_Que.pop(Select)
    return List

def Shuffle_Optins(_List_, Correct_Ans):
    question = []
    for Numbers in range(10):
        Suffled_Options = list(set(_List_[Numbers][1:]))
        random.shuffle(Suffled_Options) # Shuffles option order as well
        question.append([_List_[Numbers][0]] + Suffled_Options + [Suffled_Options.index(Correct_Ans[Numbers]) + 1])
    return question

questions_and_options_easy = [
    ["Who was the first President of India?", "Jawaharlal Nehru", "Dr. Rajendra Prasad", "Dr. S. Radhakrishnan", "Dr. Zakir Husain"],
    ["Who is known as the chief architect of the Indian Constitution?", "Mahatma Gandhi", "Jawaharlal Nehru", "Dr. B. R. Ambedkar", "Sardar Vallabhbhai Patel"],
    ["Which article of the Indian Constitution abolishes untouchability?", "Article 14", "Article 17", "Article 19", "Article 21"],
    ["Which Indian state has the longest coastline?", "Tamil Nadu", "Andhra Pradesh", "Gujarat", "Maharashtra"],
    ["Which river is known as the “Sorrow of Bihar”?", "Ganga", "Kosi", "Yamuna", "Godavari"],
    ["Which country has the largest land area in the world?", "Canada", "China", "Russia", "United States"],
    ["What is the SI unit of electric resistance?", "Volt", "Ampere", "Ohm", "Watt"],
    ["What is the chemical symbol for sodium?", "So", "Na", "S", "Sd"],
    ["Where is the headquarters of the World Health Organization (WHO)?", "New York", "Paris", "Geneva", "Vienna"],
    ["Which country gifted the Statue of Liberty to the United States?", "United Kingdom", "France", "Germany", "Spain"]
]
correct_ans_easy = ["Dr. Rajendra Prasad", "Dr. B. R. Ambedkar", "Article 17", "Gujarat", "Kosi", "Russia", "Ohm", "Na", "Geneva", "France"]

questions_and_options_medium = [
    ["Which Indian state was the first to be formed on a linguistic basis after independence?", "Gujarat", "Andhra State", "Kerala", "Karnataka"],
    ["How many Indian states does the Tropic of Cancer pass through?", "6", "8", "9", "10"],
    ["Who discovered penicillin?", "Louis Pasteur", "Alexander Fleming", "Robert Koch", "Edward Jenner"],
    ["Two resistors of 6 ohms and 3 ohms are connected in parallel. What is their equivalent resistance?", "9 ohms", "4.5 ohms", "2 ohms", "3 ohms"],
    ["Which element has the highest electronegativity?", "Oxygen", "Chlorine", "Fluorine", "Nitrogen"],
    ["What is the value of sin^2(x) + cos^2(x)?", "0", "1", "2", "It depends on x"],
    ["How many players are on each team in a standard competitive Valorant match?", "4", "5", "6", "7"],
    ["Which two items are combined to craft a Netherite ingot?", "Iron ingots and diamonds", "Gold ingots and emeralds", "Netherite scraps and gold ingots", "Ancient debris and diamonds"],
    ["A particle moves in a circle at constant speed v. What is the magnitude of the change in its velocity after completing half a revolution?", "0", "v", "2v", "2 times pi times v"],
    ["Which data structure follows the LIFO principle?", "Queue", "Stack", "Linked list", "Priority queue"]
]
correct_ans_medium = ["Andhra State", "8", "Alexander Fleming", "2 ohms", "Fluorine", "1", "5", "Netherite scraps and gold ingots", "2v", "Stack"]

questions_and_options_hard = [
    ["Which composer was popularly known as the \"Mozart of Madras\"?", "Ilaiyaraaja", "A. R. Rahman", "Anirudh Ravichander", "M. S. Viswanathan"],
    ["Which band released the album \"The Dark Side of the Moon\"?", "The Beatles", "Queen", "Pink Floyd", "Led Zeppelin"],
    ["What does the term \"stagflation\" refer to?", "High economic growth with low inflation", "Falling prices with rising employment", "High inflation combined with stagnant economic growth", "A rapid increase in exports"],
    ["Which institution is responsible for monetary policy in India?", "NITI Aayog", "Ministry of Commerce", "Reserve Bank of India", "Securities and Exchange Board of India"],
    ["Which 1975 Bollywood film features the characters Jai and Veeru?", "Deewar", "Zanjeer", "Sholay", "Don"],
    ["Who directed the 2001 film \"Lagaan\"?", "Sanjay Leela Bhansali", "Farhan Akhtar", "Ashutosh Gowariker", "Rajkumar Hirani"],
    ["Which river crosses the Equator twice during its course?", "Amazon", "Congo", "Nile", "Mekong"],
    ["Which of these mountain ranges is generally considered the oldest?", "Himalayas", "Alps", "Andes", "Aravalli Range"],
    ["Which ruler issued the famous Allahabad Pillar inscription praising his conquests?", "Chandragupta Maurya", "Ashoka", "Samudragupta", "Harshavardhana"],
    ["Which ancient Indian university was located in present-day Bihar and became a major centre of Buddhist learning?", "Takshashila", "Nalanda", "Vallabhi", "Kanchipuram"]
]
correct_ans_hard = ["A. R. Rahman", "Pink Floyd", "High inflation combined with stagnant economic growth", "Reserve Bank of India", "Sholay", "Ashutosh Gowariker", "Congo", "Aravalli Range", "Samudragupta", "Nalanda"]

PRIZE_TREE = [
    "₹ 1,000", "₹ 2,000", "₹ 3,000", "₹ 5,000", "₹ 10,000",
    "₹ 20,000", "₹ 40,000", "₹ 80,000", "₹ 1,60,000", "₹ 3,20,000",
    "₹ 6,40,000", "₹ 12,50,000", "₹ 25,00,000", "₹ 50,00,000", "₹ 1,00,00,000"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ---------------------------------------------------------
# UI RENDERING
# ---------------------------------------------------------
def render_ui(q_data, current_q_idx, time_limit, total_questions):
    clear_screen()
    question_text = q_data[0]
    options = [q_data[1], q_data[2], q_data[3], q_data[4]]

    # Header
    print(f"{C_GOLD}{C_BOLD}" + "=" * 78 + f"{C_RESET}")
    print(f"{C_GOLD}{C_BOLD}   T I M E   R U S H  {C_RESET}".center(88))
    print(f"{C_GOLD}{C_BOLD}" + "=" * 78 + f"{C_RESET}\n")

    # HUD Stats & Timer Info
    timer_display = f"{time_limit}s" if time_limit else "Unlimited"
    print(f"  {C_CYAN}Current Prize:{C_RESET} {PRIZE_TREE[current_q_idx]}".ljust(43) + 
          f"{C_BOLD}Time Limit:{C_RESET} {C_GOLD}{timer_display}{C_RESET}".ljust(25) +
          f"{C_BOLD}Q:{C_RESET} {current_q_idx + 1} / {total_questions}")
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
        if text is None:
            formatted_opts.append(" " * 30)
        else:
            formatted_opts.append(
                f"{C_CYAN}[{opt_labels[i]}]:{C_RESET} "
                f"{C_BOLD}{text:<22}{C_RESET}"
            )

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

    # Money Ladder (Showing current active prize window)
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
# TIMED INPUT HELPER
# ---------------------------------------------------------
def get_input_with_timeout(timeout):
    user_ans = [None]

    def target():
        try:
            user_ans[0] = input(f"Enter choice ({C_CYAN}A, B, C, D{C_RESET}) or Lifeline ({C_GOLD}1-4{C_RESET}): ")
        except Exception:
            pass

    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        return "__TIMEOUT__"
    
    return user_ans[0].strip().upper() if user_ans[0] is not None else ""

# ---------------------------------------------------------
# GAME FLOW
# ---------------------------------------------------------
def play_game():
    for item in lifeline.values():
        item[1] = True
    # Extract unique random questions using your custom selection functions[cite: 1]
    Q_No_easy = select_que_no()
    Q_No_medium = select_que_no()
    Q_No_hard = select_que_no()

    Easy_que = Shuffle_Optins(questions_and_options_easy, correct_ans_easy)
    Medium_que = Shuffle_Optins(questions_and_options_medium, correct_ans_medium)
    Hard_que = Shuffle_Optins(questions_and_options_hard, correct_ans_hard)

    # Build the final 15-question set: 5 Easy, 5 Medium, 5 Hard
    questions = [Easy_que[Num] for Num in Q_No_easy] + \
                [Medium_que[Num] for Num in Q_No_medium] + \
                [Hard_que[Num] for Num in Q_No_hard]

    used_questions = {
        "easy": set(Q_No_easy),
        "medium": set(Q_No_medium),
        "hard": set(Q_No_hard)}

    current_idx = 0
    total_questions = len(questions)

    while current_idx < total_questions:
        q_data = questions[current_idx]
        correct_opt = q_data[5]

        # Tiered time limit rules:
        # Questions 1-5 (Easy): 45 seconds
        # Questions 6-10 (Medium): 60 seconds
        # Questions 11-15 (Hard): Unlimited time
        if current_idx < 5:
            time_limit = 45
        elif current_idx < 10:
            time_limit = 60
        else:
            time_limit = None

        while True:
            correct_opt = q_data[5]
            render_ui(q_data, current_idx, time_limit, total_questions)

            if time_limit is None:
                user_input = input(f"Enter choice ({C_CYAN}A, B, C, D{C_RESET}) or Lifeline ({C_GOLD}1-4{C_RESET}): ").strip().upper()
            else:
                user_input = get_input_with_timeout(time_limit)
                if user_input == "__TIMEOUT__":
                    show_error_screen("TIME UP! You ran out of time.")
                    return  # Instantly terminates game back to main menu

            # Handle Lifelines (Input 1, 2, 3, 4)
            lifelines_map = {
                "1": "50-50",
                "2": "Switch Question",
                "3": "Audience Poll",
                "4": "Extra Time"
            }

            if user_input in lifelines_map:
                lifelines(user_input, q_data, current_idx, used_questions, Easy_que, Medium_que, Hard_que)
                continue

            # Handle Answers (Input A, B, C, D)
            opt_map = {"A": 1, "B": 2, "C": 3, "D": 4}
            if user_input in opt_map:
                chosen_opt = opt_map[user_input]
                if q_data[chosen_opt] is None:
                        print(
                            f"\n{C_RED}This option has been eliminated! "
                            f"Please choose a remaining option.{C_RESET}"
                        )
                        input("Press ENTER to continue...")
                        continue

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
    print("    G A M E   O V E R")
    print(f"    Reason: {reason}")
    print("!" * 60 + f"{C_RESET}\n")
    input(f"{C_CYAN}Press ENTER to return to the main menu...{C_RESET}")

def show_victory_screen():
    clear_screen()
    print(f"\n{C_GOLD}{C_BOLD}" + "★" * 65)
    print("    C O N G R A T U L A T I O N S ! ! !")
    print("    YOU HAVE CONQUERED TIME RUSH AND WON 7 CRORE!")
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