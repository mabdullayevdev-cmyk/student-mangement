from utils import get_valid_integer, get_non_empty_string, find_student_by_id
from database import load_data, save_data
from students import view_students
from colored import cprint

def add_grade():
    """O'quvchiga baho qo'shish."""
    students, next_id = load_data()
    if not students:
        cprint("\nO'quvchilar mavjud emas.", "yellow")
        return
        
    view_students()
    student_id = get_valid_integer("\nBaho qo'shmoqchi bo'lgan o'quvchi ID sini kiriting: ")
    _, student = find_student_by_id(students, student_id)
    
    if student is None:
        cprint(f"Xatolik! ID {student_id} bo'yicha o'quvchi topilmadi.", "red")
        return
        
    subject = get_non_empty_string("Fan nomini kiriting: ")
    grade = get_valid_integer("Bahoni kiriting (1 dan 5 gacha): ", min_val=1, max_val=5)
    
    if subject not in student['grades']:
        student['grades'][subject] = []
        
    student['grades'][subject].append(grade)
    save_data(students, next_id)
    cprint(f"Muvaffaqiyatli! {student['name']} uchun {subject} faniga {grade} bahosi qo'shildi.", "green")

def view_grades():
    """O'quvchining baholarini ko'rish."""
    students, _ = load_data()
    if not students:
        cprint("\nO'quvchilar mavjud emas.", "yellow")
        return
        
    view_students()
    student_id = get_valid_integer("\nBaholarini ko'rmoqchi bo'lgan o'quvchi ID sini kiriting: ")
    _, student = find_student_by_id(students, student_id)
    
    if student is None:
        cprint(f"Xatolik! ID {student_id} bo'yicha o'quvchi topilmadi.", "red")
        return
        
    cprint(f"\n--- {student['name'].upper()}NING BAHOLARI ---", "cyan")
    if not student['grades']:
        cprint("Bu o'quvchida hali baholar mavjud emas.", "yellow")
        return
        
    for subject, grades_list in student['grades'].items():
        print(f"- {subject}: {', '.join(map(str, grades_list))}")