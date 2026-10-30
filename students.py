from utils import get_valid_integer, get_non_empty_string, find_student_by_id
from database import load_data, save_data
from colored import cprint

def add_student():
    """Yangi o'quvchi qo'shish."""
    students, next_id = load_data()
    
    cprint("\n--- YANGI O'QUVCHI QO'SHISH ---", "cyan")
    name = get_non_empty_string("O'quvchining ismi: ")
    age = get_valid_integer("O'quvchining yoshi: ", min_val=1, max_val=120)
    group = get_non_empty_string("Guruh nomi (masalan, Python-01): ")
    
    new_student = {
        "id": next_id,
        "name": name,
        "age": age,
        "group": group,
        "grades": {}
    }
    
    students.append(new_student)
    save_data(students, next_id + 1)
    cprint(f"Muvaffaqiyatli! O'quvchi qo'shildi (ID: {next_id}).", "green")

def view_students():
    """Barcha o'quvchilarni ko'rish."""
    students, _ = load_data()
    if not students:
        cprint("\nO'quvchilar ro'yxati bo'sh.", "yellow")
        return
    
    cprint("\n--- O'QUVCHILAR RO'YXATI ---", "cyan")
    print(f"{'ID':<5} | {'Ismi':<20} | {'Yoshi':<5} | {'Guruh':<10}")
    print("-" * 45)
    for s in students:
        print(f"{s['id']:<5} | {s['name']:<20} | {s['age']:<5} | {s['group']:<10}")

def edit_student():
    """O'quvchi ma'lumotlarini tahrirlash."""
    students, next_id = load_data()
    if not students:
        cprint("\nTahrirlash uchun o'quvchilar mavjud emas.", "yellow")
        return
    
    view_students()
    student_id = get_valid_integer("\nTahrirlamoqchi bo'lgan o'quvchi ID raqamini kiriting: ")
    index, student = find_student_by_id(students, student_id)
    
    if student is None:
        cprint(f"Xatolik! ID {student_id} bo'yicha o'quvchi topilmadi.", "red")
        return
    
    print(f"\nJoriy ma'lumotlar: Ism: {student['name']}, Yosh: {student['age']}, Guruh: {student['group']}")
    print("O'zgartirmoqchi bo'lmagan maydonlarni bo'sh qoldirib Enter bosing.")
    
    new_name = input(f"Yangi ism [{student['name']}]: ").strip()
    if new_name:
        student['name'] = new_name
        
    new_age_str = input(f"Yangi yosh [{student['age']}]: ").strip()
    if new_age_str:
        try:
            new_age = int(new_age_str)
            if new_age > 0:
                student['age'] = new_age
            else:
                cprint("Yosh musbat bo'lishi kerak. Eski yosh saqlandi.", "yellow")
        except ValueError:
            cprint("Noto'g'ri format. Eski yosh saqlandi.", "yellow")
            
    new_group = input(f"Yangi guruh [{student['group']}]: ").strip()
    if new_group:
        student['group'] = new_group
        
    save_data(students, next_id)
    cprint("O'quvchi ma'lumotlari muvaffaqiyatli yangilandi!", "green")

def delete_student():
    """O'quvchini o'chirish."""
    students, next_id = load_data()
    if not students:
        cprint("\nO'chirish uchun o'quvchilar mavjud emas.", "yellow")
        return
    
    view_students()
    student_id = get_valid_integer("\nO'chirmoqchi bo'lgan o'quvchi ID raqamini kiriting: ")
    index, student = find_student_by_id(students, student_id)
    
    if student is None:
        cprint(f"Xatolik! ID {student_id} bo'yicha o'quvchi topilmadi.", "red")
        return
    
    students.pop(index)
    save_data(students, next_id)
    cprint(f"ID {student_id} bo'lgan o'quvchi muvaffaqiyatli o'chirildi.", "green")

def search_by_id():
    """O'quvchini ID bo'yicha qidirish."""
    students, _ = load_data()
    if not students:
        cprint("\nMa'lumotlar bazasi bo'sh.", "yellow")
        return
        
    student_id = get_valid_integer("Qidirilayotgan o'quvchi ID sini kiriting: ")
    _, student = find_student_by_id(students, student_id)
    
    if student:
        cprint("\n--- TOPILDI ---", "green")
        print(f"ID: {student['id']}")
        print(f"Ism: {student['name']}")
        print(f"Yosh: {student['age']}")
        print(f"Guruh: {student['group']}")
    else:
        cprint(f"ID {student_id} bo'yicha o'quvchi topilmadi.", "red")

def search_by_name():
    """O'quvchini ism orqali qidirish."""
    students, _ = load_data()
    if not students:
        cprint("\nMa'lumotlar bazasi bo'sh.", "yellow")
        return
        
    query = get_non_empty_string("Qidirilayotgan ism (yoki uning qismi): ").lower()
    matched = [s for s in students if query in s['name'].lower()]
    
    if matched:
        cprint(f"\n--- QIDIRUV NATIJALARI ({len(matched)} ta topildi) ---", "green")
        print(f"{'ID':<5} | {'Ismi':<20} | {'Yoshi':<5} | {'Guruh':<10}")
        print("-" * 45)
        for s in matched:
            print(f"{s['id']:<5} | {s['name']:<20} | {s['age']:<5} | {s['group']:<10}")
    else:
        cprint("Bunday ismli o'quvchi topilmadi.", "yellow")