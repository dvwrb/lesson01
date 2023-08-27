import random
def _get_all_names() -> list[str]:
    with open('names.txt',mode='r',encoding='utf-8') as file:
        names:list[str] = []
        for line in file:
            #names.append(line)
            line = line.rstrip('\n')
            names.append(line)
        return names
    
def _get_randon_names(nums:int) -> list[str]:
    names = _get_all_names()
    random_list = random.choices(names,k=nums)
    return random_list

def get_students(student_num:int) -> list[list]:
    names = _get_randon_names(nums=student_num)
    students :list[list] = []
    for i in range(student_num):
        one_student = [random.randint(50,100) for _ in range(5)]
        name = names[i]
        one_student = [name] + one_student
        students.append(one_student)
    return students 