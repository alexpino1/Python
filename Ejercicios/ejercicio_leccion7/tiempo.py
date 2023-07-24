import time


def main():
    current_time = time.localtime()
    hour = current_time.tm_hour

    if hour >= 19:
        print("Es hora de ir a casa !")
    else:
        print("No es hora de ir a casa .")
        end_of_workday = time.mktime(time.strptime("19:01", "%H:%M"))
        remaining_seconds = end_of_workday - time.mktime(current_time)
        remaining_hours, remaining_minutes = divmod(remaining_seconds, 3600)
        remaining_minutes //= 60
        print(f"Remaining work time: {int(remaining_hours)} hours and {int(remaining_minutes)} minutes.")

if __name__ == "__main__":
    main()