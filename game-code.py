import threading

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
success = check_input_timeout(5)


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

