import courses

def answer_generator(option: int):
    print(f"Para a {option}ª opção, você pode escolher os seguintes cursos:")

    for i, c in enumerate(courses.courses):
        print(f"[ {i} ] {c}")
    
    while True:
        try:
            ret = int(input("Qual opção você escolhe? "))
            if not (0 <= ret <= len(courses.courses) - 1):
                print("Opção inválida!")
                continue
        except:
            print("Opção inválida!")
            continue
        else:
            return ret
