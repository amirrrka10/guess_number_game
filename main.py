import random

def play_game():

    secret_number = random.randint(1, 100)
    max_attempts = 5
    attempts = 0
    won = False

    ranks = {
        1: "نمونه ای",
        2: "بسیار خوبی",
        3: "خوب",
        4: "قبول",
        5: "با شانس بردی!"
    }

    print("\n========== بازی حدس اعداد ==========")
    print("من یک عدد بین 1 تا 100 انتخاب کرده‌ام.")
    print("شما 5 فرصت برای حدس زدن دارید.")
    print("====================================")

    while attempts < max_attempts:

        print("\nتلاش", attempts + 1, "از", max_attempts)
        print("جان باقی‌مانده:", max_attempts - attempts)

        user_input = input("حدس شما: ").strip()

        if not user_input.isdigit():
            print("خطا! لطفا فقط عدد صحیح وارد کنید.")
            continue

        guess = int(user_input)

        if guess < 1 or guess > 100:
            print("عدد باید بین 1 تا 100 باشد.")
            continue

        attempts += 1

        if guess == secret_number:
            won = True
            print("\nآفرین! شما برنده شدید.")
            print("رتبه شما:", ranks[attempts])
            break

        if guess > secret_number:
            print("کوچک‌تر وارد کن.")
        else:
            print("بزرگ‌تر وارد کن.")

        difference = abs(guess - secret_number)

        if difference <= 5:
            print("خیلی نزدیکی!")
        elif difference <= 15:
            print("نزدیکی، ولی هنوز فاصله داری!")
        else:
            print("خیلی دوری!")

    if not won:
        print("\nمتاسفانه فرصت‌های شما تمام شد و باختید.")
        print("عدد مخفی برابر بود با:", secret_number)


while True:

    play_game()

    print("\nآیا می خواهید دوباره بازی کنید؟")
    answer = input("بله / خیر: ").strip()

    if answer == "بله" or answer.lower() == "yes":
        print("\nبازی جدید شروع شد!")

    elif answer == "خیر" or answer.lower() == "no":
        print("\nممنون از بازی شما. خداحافظ!")
        break

    else:
        print("پاسخ نامعتبر است. برنامه پایان می یابد.")
        break