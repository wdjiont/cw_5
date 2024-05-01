from src.dbmanager import DBManager


def user_interaction():
    print(" Привет!\n"
          " Выберите команду:\n"
          " 1 - Список всех компаний и количесво их вакансий\n 2 - Список всех вакансий с информацией по каждой\n 3 - "
          "Узнать среднюю зарплату \n 4 - Списсок вакансий, у которых зарплата выше средней\n "
          "5 - Поискать по ключевому "
          "слову\n")

    while True:
        user_input = input()
        if user_input in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("Попробуйте еще раз")

    if user_input == "1":
        all_companies = DBManager("course_work5").get_companies_and_vacancies_count()
        print(all_companies)
    elif user_input == "2":
        all_vacancies = DBManager("course_work5").get_all_vacancies()
        print(all_vacancies)
    elif user_input == "3":
        avg_salary = DBManager("course_work5").get_avg_salary()
        print(avg_salary)
    elif user_input == "4":
        high_salary = DBManager("course_work5").get_vacancies_with_higher_salary()
        print(high_salary)
    elif user_input == "5":
        keyword_input = input("Введите ключевое слово ")
        vacancy_with_keyword = DBManager("course_work5").get_vacancies_with_keyword(keyword_input)
        print(vacancy_with_keyword)


if __name__ == '__main__':
    while True:
        user_interaction()
        user_choice = input("Продолжить? (да/нет): ")
        if user_choice.lower() != "да":
            break
