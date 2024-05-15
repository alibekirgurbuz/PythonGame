import pygame
import random

# Kullanıcı verilerini saklamak için listeler
users = []

# Kullanıcı sınıfı tanımlama
class User:
    def __init__(self, first_name, last_name, age, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password

# Kullanıcı kayıt fonksiyonu
def register():
    print("Kullanıcı Kayıt")
    first_name = input("Ad: ")
    last_name = input("Soyad: ")
    age = input("Yaş: ")
    email = input("E-posta: ")
    password = input("Şifre: ")
    
    # Yeni kullanıcıyı oluşturma ve listeye ekleme
    new_user = User(first_name, last_name, age, email, password)
    users.append(new_user)
    print("Kayıt başarılı!")

# Kullanıcı giriş fonksiyonu
def login():
    print("Kullanıcı Girişi")
    email = input("E-posta: ")
    password = input("Şifre: ")
    
    for user in users:
        if user.email == email and user.password == password:
            print(f"Hoş geldiniz, {user.first_name}!")
            return True
    print("E-posta veya şifre yanlış!")
    return False

# Sayı tahmin oyunu (3 hak ile)
def sayi_tahmin_oyunu():
    print("Sayı Tahmin Oyunu")
    secret_number = random.randint(1, 100)
    attempts = 3
    while attempts > 0:
        guess = int(input("1 ile 100 arasında bir sayı tahmin edin: "))
        if guess < secret_number:
            print("Daha büyük bir sayı tahmin edin.")
        elif guess > secret_number:
            print("Daha küçük bir sayı tahmin edin.")
        else:
            print("Tebrikler, doğru tahmin!")
            return
        attempts -= 1
        print(f"Kalan hak: {attempts}")
    print(f"Hakkınız bitti! Doğru sayı: {secret_number}")

# Taş-Kağıt-Makas oyunu
def tas_kagit_makas():
    print("Taş-Kağıt-Makas")
    choices = ["taş", "kağıt", "makas"]
    computer_choice = random.choice(choices)
    user_choice = input("Seçiminizi yapın (taş, kağıt, makas): ").lower()
    
    if user_choice == computer_choice:
        print(f"Berabere! Bilgisayar da {computer_choice} seçti.")
    elif (user_choice == "taş" and computer_choice == "makas") or \
         (user_choice == "kağıt" and computer_choice == "taş") or \
         (user_choice == "makas" and computer_choice == "kağıt"):
        print(f"Kazandınız! Bilgisayar {computer_choice} seçti.")
    else:
        print(f"Kaybettiniz! Bilgisayar {computer_choice} seçti.")

# Kelime tahmin oyunu (Adam Asmaca)
def kelime_tahmin_oyunu():
    print("Kelime Tahmin Oyunu (Adam Asmaca)")
    words = ["python", "programlama", "geliştirici", "bilgisayar", "veritabanı"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6
    
    while attempts > 0:
        guess = input("Bir harf tahmin edin: ").lower()
        if guess in guessed_letters:
            print("Bu harfi zaten tahmin ettiniz.")
            continue
        guessed_letters.append(guess)
        if guess in secret_word:
            print("Doğru tahmin!")
        else:
            attempts -= 1
            print(f"Yanlış tahmin! Kalan deneme hakkı: {attempts}")
        
        word_display = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        print("Kelime: ", word_display)
        
        if "_" not in word_display:
            print("Tebrikler, kelimeyi doğru tahmin ettiniz!")
            break
    else:
        print(f"Kaybettiniz! Kelime: {secret_word}")

# Yılan oyunu
def yilan_oyunu():
    pygame.init()

    # Renk tanımlamaları
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    # Oyun ekranı boyutları
    dis_width = 800
    dis_height = 600

    # Yılan ve yemek boyutları
    snake_block = 10
    snake_speed = 15

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Yılan Oyunu')

    clock = pygame.time.Clock()

    font_style = pygame.font.SysFont(None, 50)
    score_font = pygame.font.SysFont(None, 35)

    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])

    def gameLoop():  # Oyun ana fonksiyonu
        game_over = False
        game_close = False

        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_List = []
        Length_of_snake = 1

        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close == True:
                dis.fill(blue)
                message("Kaybettin! Q-Quit veya C-Continue", red)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(blue)
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)
            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()

    gameLoop()

# 21 Oyunu (Blackjack)
def blackjack():
    print("21 Oyunu (Blackjack)")
    def deal_card():
        cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        return random.choice(cards)

    def calculate_score(hand):
        score = 0
        ace_count = 0
        for card in hand:
            if card in ["J", "Q", "K"]:
                score += 10
            elif card == "A":
                ace_count += 1
                score += 11
            else:
                score += int(card)
        while ace_count > 0 and score > 21:
            score -= 10
            ace_count -= 1
        return score

    user_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]
    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    while user_score < 21:
        print(f"Sizin eliniz: {user_hand}, Toplam: {user_score}")
        action = input("Kart çekmek istiyor musunuz? (e/h): ")
        if action == "e":
            user_hand.append(deal_card())
            user_score = calculate_score(user_hand)
        else:
            break

    while computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"Bilgisayarın eli: {computer_hand}, Toplam: {computer_score}")

    if user_score > 21:
        print("Siz kaybettiniz! Eliniz 21'i geçti.")
    elif computer_score > 21 or user_score > computer_score:
        print("Tebrikler, kazandınız!")
    elif user_score < computer_score:
        print("Bilgisayar kazandı!")
    else:
        print("Berabere!")

# Ana menü
def main_menu():
    while True:
        print("\nAna Menü")
        print("1. Kayıt Ol")
        print("2. Giriş Yap")
        print("3. Çıkış")
        choice = input("Seçiminiz: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            if login():
                oyun_menu()
        elif choice == "3":
            print("Çıkış yapıldı.")
            break
        else:
            print("Geçersiz seçim!")

# Oyun menüsü
def oyun_menu():
    while True:
        print("\nOyun Menüsü")
        print("1. Sayı Tahmin Oyunu")
        print("2. Taş-Kağıt-Makas")
        print("3. Kelime Tahmin Oyunu (Adam Asmaca)")
        print("4. Yılan Oyunu")
        print("5. 21 Oyunu (Blackjack)")
        print("6. Çıkış")
        choice = input("Seçiminiz: ")
        
        if choice == "1":
            sayi_tahmin_oyunu()
        elif choice == "2":
            tas_kagit_makas()
        elif choice == "3":
            kelime_tahmin_oyunu()
        elif choice == "4":
            yilan_oyunu()
        elif choice == "5":
            blackjack()
        elif choice == "6":
            break
        else:
            print("Geçersiz seçim!")

# Programı başlatma
if __name__ == "__main__":
    main_menu()
