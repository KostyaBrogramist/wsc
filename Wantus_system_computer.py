import os
import pygame
import random
from time import sleep
from googletrans import Translator


Admin_user=0

def out_red(text):
  print("\033[31m{}".format(text))

arr = []

print("Ящик работает!")

sleep(1)

print("Wantus(противник Windows)")

sleep(1)

name = input("Введите ваше имя:\n")
arr.append(name)

print("Добро пожаловать в систему пароля!")

#while True:

password = input("Введите пароль:\n")

if password == '1234':
  out_red("Неверно!")
  exit()

elif password == os.getenv('SECRET_PASSWORD'):
  print('''
Внимание!
Вы выполнили вход в аккаунт администратора!''')

  while True:
    Admin_work=int(input("""
Выберите действие:
1. Выйти из аккаунта администратора
"""))
    
    if Admin_work == 1:
      break
      
    else:
      out_red("Ошибка404!")
      exit()
    
else:
  print("Верно!")

print("""
!LOADING!
""")

sleep(2)

print("Добро пожаловать!")

sleep(1)

while True:

  functions = input("""
Выбирайте функцию:
1. Посмотреть папки
2. Я забыл(а) имя
3. Калькулятор
4. Переводчик с английского на русский и наоборот(Могут возникнуть ошибки)
5. Крестики нолики(Сделано с ChatGP)
6. Змейка(Сделано с ChatGPT)
7. Мем недели
8. Квест месяца
9. Затестить приложение в разработке
10. Terminal
11. Выйти\n
""")

  if functions == "1":
    while True:
      functions2 = input("""Выберите:
1. Папка сценарий
2. Папка Python
3. Папка Minecraft
4. Выйти\n""")

      if functions2 == "4":
        break
      elif functions2 == "1":
        print("""Пепукап: За что мне проклятье!?
Какетуп: За имя!\n""")
      elif functions2 == "2":
        print("""print("Hello world")""")
      elif functions2 == "3":
        print('Вы не в аккаунте')
      else:
        out_red("Ошибка!")
        exit()

  elif functions == '2':
    print('Ваше имя:', arr)

  elif functions == '3':
    
    allowed_chars = '01234567890+-*/()'

    running = True
    while running:
      try:
        query = input(f"Введите пример (для выхода просто нажмите enter) (разрешенные символы '{allowed_chars}'):\n")
        for c in query:
          if c not in allowed_chars:
            raise SyntaxError
          if c == 'q':
            running = False
        
        if not running:
          break

        if query == '':
          break
        
        res = None
        exec("res = " + query)

        print(res)
      except SyntaxError:
        print('Invalid input')

  elif functions == '4':

    def translate_text(text, dest_lang, src_lang):
      translator = Translator()
      translated_text = translator.translate(text, dest=dest_lang, src=src_lang)
      return translated_text.text
    input_lang = input("Выберите язык оригинала (1 - Русский, 2 - Английский): ")
    if input_lang == '1':
      source_lang = 'ru'
      dest_lang = 'en'
      text_to_translate = input("Введите текст для перевода с русского на английский: ")
      translated_text = translate_text(text_to_translate, dest_lang, source_lang)
      print("Переведенный текст: ", translated_text)
    elif input_lang == '2':
      source_lang = 'en'
      dest_lang = 'ru'
      text_to_translate = input("Enter the text to translate from English to Russian: ")
      translated_text = translate_text(text_to_translate, dest_lang, source_lang)
      print("Translated text: ", translated_text)
    else:
      print("Неверный выбор языка оригинала.")
    
  elif functions == '5':

    def draw_board(board):
        for row in board:
            print("|".join(row))
            print("-----")

    def check_winner(board):
        for row in board:
            if row.count(row[0]) == len(row) and row[0] != ' ':
                return True

        for col in range(len(board[0])):
            if all(board[row][col] == board[0][col] and board[row][col] != ' ' for row in range(len(board))):
                return True

        if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
            return True

        return False

    def is_board_full(board):
        return all(all(cell != ' ' for cell in row) for row in board)

    def player_move(board, player):
        row = int(input(f"Игрок {player}, выберите строку (0, 1, 2): "))
        col = int(input(f"Игрок {player}, выберите столбец (0, 1, 2): "))

        if board[row][col] == ' ':
            board[row][col] = player
            return True
        else:
            print("Эта клетка уже занята. Попробуйте еще раз.")
            return False

    def computer_move(board):
        # Проверяем, есть ли выигрышные ходы для компьютера
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    # Проверяем, может ли компьютер выиграть, сделав ход в эту клетку
                    board[i][j] = 'O'
                    if check_winner(board):
                        return i, j
                    board[i][j] = ' '  # Отменяем ход

        # Проверяем, есть ли выигрышные ходы у игрока и блокируем их
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    # Проверяем, может ли игрок выиграть, сделав ход в эту клетку
                    board[i][j] = 'X'
                    if check_winner(board):
                        return i, j
                    board[i][j] = ' '  # Отменяем ход

        # Если нет выигрышных ходов, делаем случайный ход
        available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
        if available_moves:
            return random.choice(available_moves)
        else:
            return None

    def main():
        print("Добро пожаловать в игру Крестики-Нолики!")

        while True:
            print("\nМеню:")
            print("1. Игра на двух игроков")
            print("2. Игра против компьютера")
            print("3. Выйти из игры")

            choice = input("Выберите вариант (1, 2 или 3): ")

            if choice == '1':
                play_two_players()
            elif choice == '2':
                play_vs_computer()
            elif choice == '3':
                print("До свидания! До следующей игры!")
                break
            else:
                print("Неверный ввод. Пожалуйста, введите 1, 2 или 3.")

    def play_two_players():
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = 'X'

        while True:
            draw_board(board)
            player_move_success = player_move(board, current_player)

            if player_move_success:
                if check_winner(board):
                    draw_board(board)
                    print(f"Игрок {current_player} выиграл!")
                    break
                elif is_board_full(board):
                    draw_board(board)
                    print("Ничья!")
                    break
                else:
                    current_player = 'O' if current_player == 'X' else 'X'

    def play_vs_computer():
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = 'X'

        while True:
            draw_board(board)

            if current_player == 'X':
                player_move_success = player_move(board, current_player)
            else:
                print("Ход компьютера:")
                computer_move_result = computer_move(board)
                if computer_move_result is not None:
                    row, col = computer_move_result
                    board[row][col] = current_player
                    player_move_success = True
                else:
                    print("Ничья!")
                    break

            if player_move_success:
                if check_winner(board):
                    draw_board(board)
                    print(f"Игрок {current_player} выиграл!")
                    break
                elif is_board_full(board):
                    draw_board(board)
                    print("Ничья!")
                    break
                else:
                    current_player = 'O' if current_player == 'X' else 'X'

    if __name__ == "__main__":
        main()

  elif functions == '6':
    
    pygame.init()

    # Определение цветов
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    dis_width = 600
    dis_height = 400
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Змейка на Python')

    clock = pygame.time.Clock()

    snake_block = 10
    snake_speed = 15

    font_style = pygame.font.SysFont(None, 30)

    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])

    def gameLoop():
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
                dis.fill(black)
                message("Ты проиграл! Нажми Q-выход или C-снова играть", red)
                our_snake(snake_block, snake_List)
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
            dis.fill(black)
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_List.append(snake_head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_head:
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
  
  elif functions == '7':
    print("""
Кот 1: Наташ, ты спишь?
Кот 2: Уже 6 часов утра, Наташ
Кот 3: Вставай, мы там всё уронили
Кот 4: Мы уронили вообще всё, Наташ, честно
""")

  elif functions == '8':
    KvestMesyaca = input(
'Как с англиского переводиться баг?\n')

    if KvestMesyaca == 'жук':
      print('Правильно!')

    else:
      print('Неправильно!')

  elif functions == '9':
    
    while True:

    
      shop = input('''
Выбирайте:
1. выход\n''')

      if shop == '1':
        break

      else:
        out_red("Ошибка404!")
        exit()
        
  elif functions == '10':

    print('To exit, write: exit')

    sleep(1)

    while True:
      
      terminal = input(name + ':')
        
      if terminal == 'exit':
        break
  
      elif terminal == 'help':
  
          print('''
Comands:
1.exit-for exit 
2.help-for help
3.open_wirtual_box-allows you to create a virtual computer
4.amongus-more good don't use this comand
''')

      elif terminal == 'open_wirtual_box':

        open_box_settind = input("""
Choose version:
0. WANTUS LOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOL
1. WANTUS DEMO
2. WANTUS 0.0.0.1
3. WANTUS FOR SCHOOLS
""")

        if open_box_settind == '0':
          print('Wantus Lololololololololololololololololololololololol is working')

          sleep(1)

          input('''
Выбирайте функцию:
1.lol
2.Lol
3.LOl
4.LOL
5.LOL!
6.LOLOLOLOLOL
7.LOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLO
''')
          
          print('!YOU HAVE BEEN HACKED!')

          exit()

        elif open_box_settind == '1':

          print('Wantus Demo работает!')

          sleep(1)

          while True:
          
            wirtual_box_1=input('''
Выбирайте функцию:
1.Купить полную версию
2.Выйти\n''')

            if wirtual_box_1 =="1":
              print("Простите, все продано")

            elif wirtual_box_1 == "2":
              break

            else:
              out_red("ERROR404")
              exit()

        elif open_box_settind == '2':
          print('Wantus 0.0.0.1 работает!')

          sleep(1)

          while True:

            wirtual_box_2=input('''
Выбирайте функцию:
1.Папки
2.Калькулятор
3.Выйти\n''')

            if wirtual_box_2 == "1":
              while True:
                functions2 = input("""Выбирайте:
1.Папка сценарий
2.Папка Python
3.Папка Minecraft
4.Выйти\n""")

                if functions2 == "4":
                  break
                elif functions2 == "1":
                  print("""Пепукап: За что мне проклятье!?
Какетуп: За имя!\n""")
                elif functions2 == "2":
                  print("""print("Hello world")""")
                elif functions2 == "3":
                  print('Вы не в аккаунте')
                else:
                  out_red("Ошибка!")
                  exit()

            elif wirtual_box_2 =='2':
              running = True
              allowed_chars = '01234567890+-*/()'
              while running:
                try:
                  query = input(f"Введите пример (для выхода просто нажмите enter) (разрешенные символы '{allowed_chars}'):\n")
                  for c in query:
                    if c not in allowed_chars:
                      raise SyntaxError
                    if c == 'q':
                      running = False

                  if not running:
                    break

                  if query == '':
                    break

                  res = None
                  exec("res = " + query)

                  print(res)
                except SyntaxError:
                  print('Invalid input')

            elif wirtual_box_2 =='3':
              break
            
            else:
              out_red("Ошибка404!")
              exit()

        elif open_box_settind == '3':

          print('Sorry,this version in work.')
        
        else:
          out_red("Ошибка404!")
          exit()
      
      elif terminal == 'amongus':
              
        print('!IMPOSTER VIRUS START!')
                  
        sleep(1)
  
        print('Antivirus:!ATTENTION! FAILED TO REMOVE THE VIRUS')
  
        sleep(10)
  
        out_red("WANTUS doesn't answer")
        exit()
    
      else:
        out_red("ERROR404")
        exit()

  elif functions == '11':
    out_red("Выход...")
    exit()

  else:
    out_red("Ошибка404!")
    exit()
#importos;)
