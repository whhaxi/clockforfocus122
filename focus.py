import time

def focus_timer(minutes):
    """Start a focus timer for specified minutes."""
    seconds = minutes * 60
    for i in range(seconds, 0, -1):
        m, s = divmod(i, 60)
        time_str = f"{m:02d}:{s:02d}"
        print(time_str, end="\r")
        time.sleep(1)
    print("Time up! Take a break.")

# Example usage: start a 25-minute focus session
focus_timer(25)
