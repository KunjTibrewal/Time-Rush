import threading
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