days = {
    'January': 31, 'February': 28, 'March': 31, 'April': 30,
    'May': 31, 'June': 30, 'July': 31, 'August': 31,
    'September': 30, 'October': 31, 'November': 30,
    'December': 31
}

def print_days(month):
    if month in days:
        print(f"{month}은 {days[month]}일까지 있습니다.")
    else:
        print("잘못된 입력입니다.")

print("알파벳 순서로 모든 월:")
for month in sorted(days):
    print(month)

print("\n일수가 31인 월:")
for month, days_in_month in days.items():
    if days_in_month == 31:
        print(month)


print("\n월의 일수를 기준으로 오름차순으로 (key-value) 쌍:")
sorted_days = sorted(days.items(), key=lambda x: x[1])
for month, days_in_month in sorted_days:
    print(f"{month}: {days_in_month}일")


def print_days_short(month_short):
    for month, days_in_month in days.items():
        if month.startswith(month_short):
            print(f"{month}: {days_in_month}일")

user_input = input("월을 입력하세요: ")
if len(user_input) == 3:
    print_days_short(user_input.capitalize())
else:
    print_days(user_input.capitalize())
