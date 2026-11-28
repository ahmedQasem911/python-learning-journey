# ----------------------------------------------------------
# Smart Alarm
# Asks for the day of the week for tomorrow. If tomorrow is a
# weekday (anything other than Friday or Saturday), it tells
# the user to set the alarm to 8:00 a.m. If tomorrow is Friday
# or Saturday, no alarm is needed, so nothing is printed.
# ----------------------------------------------------------

LINE_WIDTH = 50

print("=" * LINE_WIDTH)
print("Smart Alarm".center(LINE_WIDTH))
print("=" * LINE_WIDTH)

tomorrow = input("Enter the day of the week for tomorrow: ").strip().capitalize()

if tomorrow not in ("Friday", "Saturday"):
    print("Set alarm to 8:00 a.m.")
