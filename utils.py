from colored import cprint

menu_text = """1. Barcha o‘quvchilarni ko‘rish
2. O‘quvchi qo‘shish
3. O‘quvchi ma’lumotlarini tahrirlash
4. O‘quvchini o‘chirish
5. O‘quvchini ID orqali qidirish
6. O‘quvchini ism orqali qidirish
7. O‘quvchiga baho qo‘shish
8. O‘quvchining baholarini ko‘rish
9. O‘rtacha bahoni ko‘rish
10. O‘quvchilar reytingi
11. Eng yuqori natijali o‘quvchi
0. Chiqish"""


def show_menu() -> None:
    cprint(
        text="===== STUDENT MANAGEMENT SYSTEM =====", fore_256="cyan", back_256="white"
    )
    print(menu_text)


def break_line() -> None:
    cprint(
        text="-" * 100, fore_256="black", back_256="yellow"
    )


def get_valid_integer(prompt, min_val=None, max_val=None):
    """Foydalanuvchidan to'g'ri butun son kiritishni talab qilish."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                cprint(f"Xatolik! Qiymat {min_val} dan kichik bo'lmasligi kerak.", "red")
                continue
            if max_val is not None and value > max_val:
                cprint(f"Xatolik! Qiymat {max_val} dan katta bo'lmasligi kerak.", "red")
                continue
            return value
        except ValueError:
            cprint("Xatolik! Iltimos, faqat butun son kiriting.", "red")


def get_non_empty_string(prompt):
    """Bo'sh bo'lmagan matn kiritishni talab qilish."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        cprint("Xatolik! Maydon bo'sh bo'lishi mumkin emas.", "red")


def find_student_by_id(students, student_id):
    """ID bo'yicha o'quvchini qidirish va uning indeksini qaytarish."""
    for index, student in enumerate(students):
        if student["id"] == student_id:
            return index, student
    return None, None


def find_students_by_name(students, name):
    """Ism bo'yicha o'quvchilarni qidirish."""
    found_students = [student for student in students if student["name"].lower() == name.lower()]
    return found_students