# Five Love Languages Quiz (Arabic/English)

# ربط كل اختيار بلغة حب
love_languages = {
    "A": {"en": "Words of Affirmation", "ar": "كلمات التقدير"},
    "B": {"en": "Quality Time", "ar": "الوقت النوعي"},
    "C": {"en": "Receiving Gifts", "ar": "تبادل الهدايا"},
    "D": {"en": "Acts of Service", "ar": "أعمال الخدمة"},
    "E": {"en": "Physical Touch", "ar": "اللمسات الجسدية"}
}

# الأسئلة بالإنجليزي
questions_en = [
    ("When someone expresses love to you, what touches you the most?",
     ["A) Says nice things about me",
      "B) Spends quality time with me without interruptions",
      "C) Gives me a gift, even a small one",
      "D) Helps me with something practical",
      "E) Hugs me or holds my hand"]),

    ("What do you miss the most if it’s not present in a relationship?",
     ["A) Words of encouragement and praise",
      "B) Time spent together",
      "C) Surprises or gifts",
      "D) Someone taking responsibilities off my shoulders",
      "E) Touches and hugs"]),

    ("When you want to show love to someone, what do you usually do?",
     ["A) Compliment or encourage them",
      "B) Spend quality time with them",
      "C) Give them a gift",
      "D) Help them with something",
      "E) Hug them or show physical closeness"]),

    ("When you are upset or stressed, what comforts you the most?",
     ["A) Someone telling me uplifting words",
      "B) Someone sitting with me and listening",
      "C) Someone giving me a small gift as encouragement",
      "D) Someone helping me finish what I have to do",
      "E) Someone hugging me"]),

    ("On special occasions (like your birthday), what matters to you the most?",
     ["A) Sweet words or a heartfelt message",
      "B) Spending time together and celebrating",
      "C) A meaningful gift",
      "D) Someone preparing and organizing everything for me",
      "E) A touch or a special hug"])
]

# الأسئلة بالعربي
questions_ar = [
    ("لما حد يعبّرلك عن الحب، إيه اللي يلمسك أكتر؟",
     ["A) يقولي كلام حلو عني",
      "B) يقضي معايا وقت مميز من غير مقاطعات",
      "C) يجيبلي هدية حتى لو صغيرة",
      "D) يساعدني في حاجة عملية",
      "E) يحضني أو يمسكني من إيدي"]),

    ("إيه أكتر حاجة بتفتقدها لو مش موجودة في العلاقة؟",
     ["A) كلمات تشجيع ومدح",
      "B) وقت يقضيه معايا",
      "C) مفاجآت أو هدايا",
      "D) حد يشيل عني بعض المسؤوليات",
      "E) لمسات واحتضان"]),

    ("لما تحب تعبّر عن حبك لحد، إيه أكتر حاجة بتعملها تلقائي؟",
     ["A) تمدحه أو تشجعه",
      "B) تخصص وقت معاه",
      "C) تجيب له هدية",
      "D) تساعده في حاجة",
      "E) تحضنه أو تبين قرب جسدي"]),

    ("لو زعلان أو مضغوط، إيه اللي يريحك أكتر؟",
     ["A) حد يقولي كلام يرفع معنوياتي",
      "B) حد يقعد معايا ويسمعني",
      "C) حد يجيبلي هدية بسيطة كتشجيع",
      "D) حد يساعدني يخلص اللي ورايا",
      "E) حد يحضني"]),

    ("في المناسبات (زي عيد ميلادك)، إيه اللي يهمك أكتر؟",
     ["A) كلمة حلوة ورسالة صادقة",
      "B) يقعد معايا ونحتفل سوا",
      "C) هدية معبرة",
      "D) إنه يساعدني ويحضر كل حاجة",
      "E) لمسة أو حضن مميز"])
]

# اختيار اللغة
lang = input(" Choose A Language (أختار اللغة) (ar عربي / en English): ").strip().lower()

if lang in ["ar", "عربي"]:
    lang = "ar"
    questions = questions_ar
    print("\n💖 أهلا بيك في اختبار لغات الحب الخمسة 💖\n")
    print("جاوب باختيار الحرف (مثلاً: A أو A,E).\n")
else:
    lang in ["en", "English"]
    lang = "en"
    questions = questions_en
    print("\n💖 Welcome to the 5 Love Languages Quiz 💖\n")
    print("Please answer each question by typing the letter(s) of your choice (e.g. A or A,E).\n")

# النتائج
scores = {lang_key[lang]: 0 for lang_key in love_languages.values()}

# طرح الأسئلة
for i, (q, choices) in enumerate(questions, 1):
    print(f"Question {i}: {q}")
    for choice in choices:
        print("   ", choice)
    answer = input("Your answer: ").upper().replace(" ", "")
    print()

    for ch in answer.split(","):
        if ch in love_languages:
            scores[love_languages[ch][lang]] += 1

# عرض النتائج
if lang == "ar":
    print("✨ نتائجك في لغات الحب ✨\n")
else:
    print("✨ Your Love Language Results ✨\n")

for lang_name, score in scores.items():
    print(f"{lang_name}: {score}")

max_score = max(scores.values())
top_languages = [lang_name for lang_name, score in scores.items() if score == max_score]

if lang == "ar":
    print("\n💡 لغات الحب الأساسية عندك:", ", ".join(top_languages))
else:
    print("\n💡 Your primary love language(s):", ", ".join(top_languages))