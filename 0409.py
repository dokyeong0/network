users = [
    {'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
    {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
    {'name': 'Princess', 'phone': '555-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}
]

print("전화번호가 8로 끝나는 사용자 이름:")
for user in users:
    if user['phone'].endswith('8'):
        print(user['name'])

print("\n이메일이 없는 사용자 이름:")
for user in users:
    if not user['email']:
        print(user['name'])

def print_contact_info(name):
    for user in users:
        if user['name'] == name:
            print(f"전화번호: {user['phone']}")
            print(f"이메일: {user['email']}")
            return
    print("이름이 없습니다.")

input_name = input("\n사용자 이름을 입력하세요: ")
print_contact_info(input_name)


def parse_string(string, separator1='&', separator2='='):
    pairs = string.split(separator1)
    result_dict = {}
    for pair in pairs:
        key, value = pair.split(separator2)
        result_dict[key] = value
    return result_dict

sample_string = 'led=on&motor=off&switch=off'
parsed_dict = parse_string(sample_string)
print("\n분리된 딕셔너리:")
print(parsed_dict)
