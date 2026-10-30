from utils import show_menu, break_line
from students import add_student, view_students, edit_student, delete_student, search_by_id, search_by_name
from grades import add_grade, view_grades
from reports import show_average_grades, show_student_rankings, show_top_student
from colored import cprint

def main() -> None:
    while True:
        show_menu()
        choice = input("> ").strip()
        break_line()

        if choice == "1":
            view_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            edit_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_by_id()
        elif choice == "6":
            search_by_name()
        elif choice == "7":
            add_grade()
        elif choice == "8":
            view_grades()
        elif choice == "9":
            show_average_grades()
        elif choice == "10":
            show_student_rankings()
        elif choice == "11":
            show_top_student()
        elif choice == "0":
            cprint("Dasturdan chiqildi. Xayr!", "red")
            break
        else:
            cprint("Xatolik! Noto'g'ri raqam kiritildi. Qaytadan urinib ko'ring.", "red")
        
        input("\nDavom etish uchun Enter tugmasini bosing...")

if __name__ == "__main__":
    main()