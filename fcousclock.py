import time

def focus_clock(minutes):
    seconds = minutes * 60

    for i in range(seconds, 0, -1):
        mins, secs = divmod(i, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(timer_display, end='\r')
        time.sleep(1)

    print("Time's up! Stay focused and take a break.")

if __name__ == "__main__":
    focus_time = int(input("请输入专注时长（分钟）："))
    focus_clock(focus_time)
