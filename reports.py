from database import load_data
from utils import get_valid_integer, find_student_by_id
from students import view_students
from colored import cprint

def calculate_average(grades_dict):
    """Berilgan fanlar baholari lug'atidan umumiy va fan kesimidagi o'rtacha bahoni hisoblash."""
    if not grades_dict:
        return 0.0, {}
    
    total_sum = 0
    total_count = 0
    subject_averages = {}
    
    for subject, grades in grades_dict.items():
        if grades:
            subj_avg = sum(grades) / len(grades)
            subject_averages[subject] = round(subj_avg, 2)
            total_sum += sum(grades)
            total_count += len(grades)
        else:
            subject_averages[subject] = 0.0
            
    overall_avg = round(total_sum / total_count, 2) if total_count > 0 else 0.0
    return overall_avg, subject_averages

def show_average_grades():
    """O'rtacha bahoni ko'rsatish."""
    students, _ = load_data()
    if not students:
        cprint("\nO'quvchilar mavjud emas.", "yellow")
        return
        
    view_students()
    student_id = get_valid_integer("\nO'rtacha bahosini ko'rmoqchi bo'lgan o'quvchi ID sini kiriting: ")
    _, student = find_student_by_id(students, student_id)
    
    if student is None:
        cprint(f"Xatolik! ID {student_id} bo'yicha o'quvchi topilmadi.", "red")
        return
        
    cprint(f"\n--- {student['name'].upper()}NING O'RTACHA BAHOLARI ---", "cyan")
    if not student['grades']:
        cprint("Baholar mavjud emas.", "yellow")
        return
        
    overall_avg, subject_averages = calculate_average(student['grades'])
    
    print("Fanlar kesimida:")
    for subj, avg in subject_averages.items():
        print(f"  - {subj}: {avg}")
        
    cprint(f"\nUmumiy o'rtacha baho: {overall_avg}", "green")

def get_ranked_students():
    """O'quvchilarni umumiy o'rtacha bahosi bo'yicha kamayish tartibida saralash."""
    students, _ = load_data()
    ranked_list = []
    
    for s in students:
        overall_avg, _ = calculate_average(s['grades'])
        has_grades = bool(s['grades'])
        ranked_list.append({
            "student": s,
            "overall_avg": overall_avg,
            "has_grades": has_grades
        })
        
    ranked_list.sort(key=lambda x: (x['has_grades'], x['overall_avg']), reverse=True)
    return ranked_list

def show_student_rankings():
    """O'quvchilar reytingi."""
    ranked = get_ranked_students()
    if not ranked:
        cprint("\nO'quvchilar mavjud emas.", "yellow")
        return
        
    cprint("\n--- O'QUVCHILAR REYTINGI ---", "cyan")
    print(f"{'O\'rn':<5} | {'Ismi':<20} | {'Guruh':<10} | {'Umumiy O\'rtacha':<15}")
    print("-" * 55)
    
    for idx, item in enumerate(ranked, 1):
        s = item['student']
        avg_str = str(item['overall_avg']) if item['has_grades'] else "Baholar yo'q"
        print(f"{idx:<5} | {s['name']:<20} | {s['group']:<10} | {avg_str:<15}")

def show_top_student():
    """Eng yuqori natijali o'quvchi."""
    ranked = get_ranked_students()
    if not ranked:
        cprint("\nO'quvchilar mavjud emas.", "yellow")
        return
        
    if not ranked[0]['has_grades']:
        cprint("\nHech bir o'quvchida baholar mavjud emas.", "yellow")
        return
        
    top_avg = ranked[0]['overall_avg']
    top_students = [item for item in ranked if item['has_grades'] and item['overall_avg'] == top_avg]
    
    cprint("\n--- ENG YUQORI NATIJALI O'QUVCHI(LAR) ---", "green")
    cprint(f"Eng yuqori o'rtacha baho: {top_avg}", "light_green")
    for item in top_students:
        s = item['student']
        print(f"- {s['name']} (Guruh: {s['group']}, ID: {s['id']})")