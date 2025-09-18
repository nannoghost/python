import random

def generate_random_numbers(filename, start, end, count):

    try:
        # إنشاء الأرقام
        random_numbers = [random.randint(start, end) for _ in range(count)]
        
        # حفظ الأرقام في ملف
        with open(filename, 'w', encoding='utf-8') as file:
            for number in random_numbers:
                file.write(f"{number}\n")
        
        print(f"✅ created {count} random numbers to '{filename}'")
        print(f"🔢 from {start} to {end}")
        
        # (اختياري) عرض بعض الإحصائيات
        print(f"📊 min: {min(random_numbers)}")
        print(f"📊 max: {max(random_numbers)}")
        print(f"📊 sum: {sum(random_numbers) / len(random_numbers):.2f}")
        
    except Exception as e:
        print(f"❌ حدث خطأ: {e}")

# كيفية استخدام الدالة
if __name__ == "__main__":
    generate_random_numbers(
        filename="random_nubers.txt", # اسم الملف
        start=100,                        # الحد الأدنى
        end=1500,                         # الحد الأقصى
        count=50000                       # الكمية
    )