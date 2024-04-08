class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)
        self.employeeID = employeeID
    
    def getID(self):
        return self.employeeID


employee = Employee("IoT", 65, 2018)

print("이름:", employee.getName())
print("나이:", employee.getAge())
print("ID:", employee.getID())



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
