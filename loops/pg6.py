# 6)	Print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight.
for hour in range(24):
    if hour == 0:
        print("12 Midnight")
    elif hour == 12:
        print("12 Noon")
    elif hour < 12:
        print(f"{hour} AM")
    else:
        print(f"{hour - 12} PM")
