from tkinter import *
import tkinter as tk
import random
from tkinter.font import Font

#Projekt Jezyki Skryptowe
#Informatyka NS RMS sem. III
#Filip Kozlik


class Game:
    #Konstruktor
    def __init__(self):
        #ustawienia okna
        self.window = Tk()
        self.window.title("JS Filip Kozlik")
        self.font = Font(family="Courier", size=32, weight="bold")

        #ustawienia gry
        self.AI_mode = False
        self.AI_level = 1 #domyslny poziom AI
        self.player_x_turn = True
        self.game_over = False
        self.number_of_turns = 0

        #ustawienia przyciskow
        self.create_buttons()

        #ustawienia menu
        self.menu_bar = tk.Menu(self.window)
        self.game_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.AI_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_conf()
        self.window.config(menu=self.menu_bar)

        #mainloop
        self.window.mainloop()

    
    #Stworzenie przyciskow
    def create_buttons(self):
        #stworzenie przyciskow
        self.but1 = Button(self.window, text=" ", padx=25, pady=15, font=self.font, command= lambda: self.place_mark(self.but1))
        self.but2 = Button(self.window, text=" ", padx=25, pady=15, font=self.font, command= lambda: self.place_mark(self.but2))
        self.but3 = Button(self.window, text=" ", padx=25, pady=15, font=self.font, command= lambda: self.place_mark(self.but3))
        self.but4 = Button(self.window, text=" ", padx=25, pady=15, font=self.font, command= lambda: self.place_mark(self.but4))
        self.but5 = Button(self.window, text=" ", padx=25, pady=15, font=self.font, command= lambda: self.place_mark(self.but5))
        self.but6 = Button(self.window, text=" ", padx=25, pady=15, font=self.font, command= lambda: self.place_mark(self.but6))
        self.but7 = Button(self.window, text=" ", padx=25, pady=15, font=self.font, command= lambda: self.place_mark(self.but7))
        self.but8 = Button(self.window, text=" ", padx=25, pady=15, font=self.font, command= lambda: self.place_mark(self.but8))
        self.but9 = Button(self.window, text=" ", padx=25, pady=15, font=self.font, command= lambda: self.place_mark(self.but9))

        #dodanie pozycji przyciskow
        self.but1.grid(row=0, column=0)
        self.but2.grid(row=0, column=1)
        self.but3.grid(row=0, column=2)
        self.but4.grid(row=1, column=0)
        self.but5.grid(row=1, column=1)
        self.but6.grid(row=1, column=2)
        self.but7.grid(row=2, column=0)
        self.but8.grid(row=2, column=1)
        self.but9.grid(row=2, column=2)

        #stworzenie listy przyciskow
        self.button_list = [self.but1,self.but2,self.but3,self.but4,self.but5,self.but6,self.but7,self.but8,self.but9]

    #Konfiguracja menu
    def menu_conf(self):
        # Konfiguracja paska menu - GAME
        self.game_menu.add_command(label="Reset Game", command=self.reset_game)
        self.game_menu.add_separator()
        self.game_menu.add_command(label="Exit", command=self.window.quit)

        # Kondiguracja paska menu - AI
        self.AI_menu.add_command(label="Simple AI", command=self.simple_AI)
        self.AI_menu.add_command(label="Medium AI", command=self.medium_AI)
        self.AI_menu.add_command(label="Hard AI", command=self.hard_AI)
        self.AI_menu.add_separator()
        self.AI_menu.add_command(label="Turn Off AI", command=self.AI_off)

        # dodanie menu AI do okna
        self.menu_bar.add_cascade(label="AI", menu=self.AI_menu)

        # Dodanie paska menu do okna
        self.menu_bar.add_cascade(label="Game", menu=self.game_menu)

    #Postawienie znaczka X lub O
    def place_mark(self, temp_button):
        #Czlowiek vs Czlowiek
         #tura gracza X
        if self.player_x_turn:
            temp_button["text"] = "X"
            self.player_x_turn = False

        #tura gracza O
        else:
            temp_button["text"] = "O"
            self.player_x_turn = True

        #ustawienie przycisku na zablokowany po jego wybraniu
        temp_button["state"] = tk.DISABLED
        self.check_for_win()

        #Czlowiek vs Komputer
        if self.AI_mode and not self.game_over and not self.player_x_turn:
            #self.check_for_win()
            self.AI()

    #Reguly wygranej
    def check_for_win(self):
        #sprawdzenie rzedow
        #1
        if self.but1["text"] == self.but2["text"] and self.but2["text"] == self.but3["text"] and self.but1["text"] != " ":
            self.but1.config(bg="blue")
            self.but2.config(bg="blue")
            self.but3.config(bg="blue")
            self.game_over = True
            self.disable_buttons()
        #2
        if self.but4["text"] == self.but5["text"] and self.but5["text"] == self.but6["text"] and self.but4["text"] != " ":
            self.but4.config(bg="blue")
            self.but5.config(bg="blue")
            self.but6.config(bg="blue")
            self.game_over = True
            self.disable_buttons()

        #3
        if self.but7["text"] == self.but8["text"] and self.but8["text"] == self.but9["text"] and self.but7["text"] != " ":
            self.but7.config(bg="blue")
            self.but8.config(bg="blue")
            self.but9.config(bg="blue")
            self.game_over = True
            self.disable_buttons()

        #sprawdzenie kolumn
        #1
        if self.but1["text"] == self.but4["text"] and self.but4["text"] == self.but7["text"] and self.but1["text"] != " ":
            self.but1.config(bg="yellow")
            self.but4.config(bg="yellow")
            self.but7.config(bg="yellow")
            self.game_over = True
            self.disable_buttons()

        #2
        if self.but2["text"] == self.but5["text"] and self.but5["text"] == self.but8["text"] and self.but2["text"] != " ":
            self.but2.config(bg="yellow")
            self.but5.config(bg="yellow")
            self.but8.config(bg="yellow")
            self.game_over = True
            self.disable_buttons()

        #3
        if self.but3["text"] == self.but6["text"] and self.but6["text"] == self.but9["text"] and self.but3["text"] != " ":
            self.but3.config(bg="yellow")
            self.but6.config(bg="yellow")
            self.but9.config(bg="yellow")
            self.game_over = True
            self.disable_buttons()

        
        #sprawdzenie przekatnych
        #1
        if self.but1["text"] == self.but5["text"] and self.but5["text"] == self.but9["text"] and self.but1["text"] != " ":
            self.but1.config(bg="red")
            self.but5.config(bg="red")
            self.but9.config(bg="red")
            self.game_over = True
            self.disable_buttons()

        #2
        if self.but3["text"] == self.but5["text"] and self.but5["text"] == self.but7["text"] and self.but3["text"] != " ":
            self.but3.config(bg="red")
            self.but5.config(bg="red")
            self.but7.config(bg="red")
            self.game_over = True
            self.disable_buttons()

        #Sprawdzenie remisu
        elif not self.game_over and self.number_empty() == 0:
            self.game_over = True

        #W przypadku zakonczenie gry, wylacz pozostale przyciski
        if self.game_over:
            self.disable_buttons()

    #wylaczanie przyciskow
    def disable_buttons(self):
        for button in self.button_list:
            button['state'] = tk.DISABLED

    #wlaczanie przyciskow
    def enable_all_buttons(self):
        for button in self.button_list:
            button['state'] = tk.NORMAL

    #zresetowanie koloru tła
    def reset_background_color(self):
        for button in self.button_list:
            button.config(bg="white smoke")

    #zresetowanie textu
    def reset_text(self):
        for button in self.button_list:
            button['text'] = ' '

    #zresetwoanie poczatkowych wartosci
    def reset_var(self):
        self.player_x_turn = True
        self.game_over = False
        self.number_of_turns = 0
        self.AI_mode = False

    #restart gry
    def reset_game(self):
        self.reset_background_color()
        self.reset_text()
        self.reset_var()
        self.enable_all_buttons()

    #SZTUCZNA INTELIGENCJA

    #Wylaczenie trybu AI
    def AI_off(self):
        self.AI_mode = False
        self.reset_game()

    #proste AI
    def simple_AI(self):
        self.AI_mode = True
        self.AI_level = 1

    #srednio trudne AI
    def medium_AI(self):
        self.AI_mode = True
        self.AI_level = 2


    #Trudne AI
    def hard_AI(self):
        self.AI_mode = True
        self.AI_level = 3


    #wolne miejsce na planszy
    def number_empty(self):
        empty = 0
        for button in self.button_list:
            if button['text'] == " ":
                empty += 1
        return empty

    #Blokowanie gracza X
    def block_X(self):
        #Pierwszy rzad
        if (self.but1["text"] == " ") and (self.but2["text"] == "X") and (self.but3["text"] == "X"):
            self.place_mark(self.but1)
        elif (self.but1["text"] == "X") and (self.but2["text"] == " ") and (self.but3["text"] == "X"):
            self.place_mark(self.but2)
        elif (self.but1["text"] == "X") and (self.but2["text"] == "X") and (self.but3["text"] == " "):
            self.place_mark(self.but3)

        #Drugi rzad
        elif (self.but4["text"] == " ") and (self.but5["text"] == "X") and (self.but6["text"] == "X"):
            self.place_mark(self.but4)
        elif (self.but4["text"] == "X") and (self.but5["text"] == " ") and (self.but6["text"] == "X"):
            self.place_mark(self.but5)
        elif (self.but4["text"] == "X") and (self.but5["text"] == "X") and (self.but6["text"] == " "):
            self.place_mark(self.but6)

        #Trzeci rzad
        elif (self.but7["text"] == " ") and (self.but8["text"] == "X") and (self.but9["text"] == "X"):
            self.place_mark(self.but7)
        elif (self.but7["text"] == "X") and (self.but8["text"] == " ") and (self.but9["text"] == "X"):
            self.place_mark(self.but8)
        elif (self.but7["text"] == "X") and (self.but8["text"] == "X") and (self.but9["text"] == " "):
            self.place_mark(self.but9)

        #Pierwsza kolumna
        elif (self.but1["text"] == " ") and (self.but4["text"] == "X") and (self.but7["text"] == "X"):
            self.place_mark(self.but1)
        elif (self.but1["text"] == "X") and (self.but4["text"] == " ") and (self.but7["text"] == "X"):
            self.place_mark(self.but4)
        elif (self.but1["text"] == "X") and (self.but4["text"] == "X") and (self.but7["text"] == " "):
            self.place_mark(self.but7)

        #Druga Kolumna
        elif (self.but2["text"] == " ") and (self.but5["text"] == "X") and (self.but8["text"] == "X"):
            self.place_mark(self.but2)
        elif (self.but2["text"] == "X") and (self.but5["text"] == " ") and (self.but8["text"] == "X"):
            self.place_mark(self.but5)
        elif (self.but2["text"] == "X") and (self.but5["text"] == "X") and (self.but8["text"] == " "):
            self.place_mark(self.but8)

        #Trzecia Kolumna
        elif (self.but3["text"] == " ") and (self.but6["text"] == "X") and (self.but9["text"] == "X"):
            self.place_mark(self.but3)
        elif (self.but3["text"] == "X") and (self.but6["text"] == " ") and (self.but9["text"] == "X"):
            self.place_mark(self.but6)
        elif (self.but3["text"] == "X") and (self.but6["text"] == "X") and (self.but9["text"] == " "):
            self.place_mark(self.but9)

        #Pierwsza Przekatna
        elif (self.but1["text"] == " ") and (self.but5["text"] == "X") and (self.but9["text"] == "X"):
            self.place_mark(self.but1)
        elif (self.but1["text"] == "X") and (self.but5["text"] == " ") and (self.but9["text"] == "X"):
            self.place_mark(self.but5)
        elif (self.but1["text"] == "X") and (self.but5["text"] == "X") and (self.but9["text"] == " "):
            self.place_mark(self.but9)

        #Druga Przekatna
        elif (self.but3["text"] == " ") and (self.but5["text"] == "X") and (self.but7["text"] == "X"):
            self.place_mark(self.but3)
        elif (self.but3["text"] == "X") and (self.but5["text"] == " ") and (self.but7["text"] == "X"):
            self.place_mark(self.but5)
        elif (self.but3["text"] == "X") and (self.but5["text"] == "X") and (self.but7["text"] == " "):
            self.place_mark(self.but7)

        #Jakikolwiek inny przypadek
        else:
            AI_move = random.randint(1, self.number_empty())
            self.place_in_free_space(AI_move)

    #Postawienia wygrywajacego znaku przez Trudne AI
    def place_O_To_Win(self):
        # Pierwszy rzad
        if (self.but1["text"] == " ") and (self.but2["text"] == "O") and (self.but3["text"] == "O"):
            self.place_mark(self.but1)
        elif (self.but1["text"] == "O") and (self.but2["text"] == " ") and (self.but3["text"] == "O"):
            self.place_mark(self.but2)
        elif (self.but1["text"] == "O") and (self.but2["text"] == "O") and (self.but3["text"] == " "):
            self.place_mark(self.but3)

        # Drugi rzad
        elif (self.but4["text"] == " ") and (self.but5["text"] == "O") and (self.but6["text"] == "O"):
            self.place_mark(self.but4)
        elif (self.but4["text"] == "O") and (self.but5["text"] == " ") and (self.but6["text"] == "O"):
            self.place_mark(self.but5)
        elif (self.but4["text"] == "O") and (self.but5["text"] == "O") and (self.but6["text"] == " "):
            self.place_mark(self.but6)

        # Trzeci rzad
        elif (self.but7["text"] == " ") and (self.but8["text"] == "O") and (self.but9["text"] == "O"):
            self.place_mark(self.but7)
        elif (self.but7["text"] == "O") and (self.but8["text"] == " ") and (self.but9["text"] == "O"):
            self.place_mark(self.but8)
        elif (self.but7["text"] == "O") and (self.but8["text"] == "O") and (self.but9["text"] == " "):
            self.place_mark(self.but9)

        # Pierwsza kolumna
        elif (self.but1["text"] == " ") and (self.but4["text"] == "O") and (self.but7["text"] == "O"):
            self.place_mark(self.but1)
        elif (self.but1["text"] == "O") and (self.but4["text"] == " ") and (self.but7["text"] == "O"):
            self.place_mark(self.but4)
        elif (self.but1["text"] == "O") and (self.but4["text"] == "O") and (self.but7["text"] == " "):
            self.place_mark(self.but7)

        # Druga Kolumna
        elif (self.but2["text"] == " ") and (self.but5["text"] == "O") and (self.but8["text"] == "O"):
            self.place_mark(self.but2)
        elif (self.but2["text"] == "O") and (self.but5["text"] == " ") and (self.but8["text"] == "O"):
            self.place_mark(self.but5)
        elif (self.but2["text"] == "O") and (self.but5["text"] == "O") and (self.but8["text"] == " "):
            self.place_mark(self.but8)

        # Trzecia Kolumna
        elif (self.but3["text"] == " ") and (self.but6["text"] == "O") and (self.but9["text"] == "O"):
            self.place_mark(self.but3)
        elif (self.but3["text"] == "O") and (self.but6["text"] == " ") and (self.but9["text"] == "O"):
            self.place_mark(self.but6)
        elif (self.but3["text"] == "O") and (self.but6["text"] == "O") and (self.but9["text"] == " "):
            self.place_mark(self.but9)

        # Pierwsza Przekatna
        elif (self.but1["text"] == " ") and (self.but5["text"] == "O") and (self.but9["text"] == "O"):
            self.place_mark(self.but1)
        elif (self.but1["text"] == "O") and (self.but5["text"] == " ") and (self.but9["text"] == "O"):
            self.place_mark(self.but5)
        elif (self.but1["text"] == "O") and (self.but5["text"] == "O") and (self.but9["text"] == " "):
            self.place_mark(self.but9)

        # Druga Przekatna
        elif (self.but3["text"] == " ") and (self.but5["text"] == "O") and (self.but7["text"] == "O"):
            self.place_mark(self.but3)
        elif (self.but3["text"] == "O") and (self.but5["text"] == " ") and (self.but7["text"] == "O"):
            self.place_mark(self.but5)
        elif (self.but3["text"] == "O") and (self.but5["text"] == "O") and (self.but7["text"] == " "):
            self.place_mark(self.but7)

    #Obsluga AI
    def AI(self):
        if self.number_empty() == 8:
            #Obsluga pierwszego ruchu AI
            if self.but5["text"] == " ":
                self.place_mark(self.but5)
            else:
                self.place_mark(self.but1)

        #AI pierwszego poziomu
        elif self.AI_level == 1:
            self.place_in_free_space(random.randint(1,self.number_empty()))

        #AI drugiego poziomu
        elif self.AI_level == 2:
            self.block_X()

        #AI 3 poziomu
        elif self.AI_level == 3:
            self.place_O_To_Win()
            self.check_for_win()
            if not self.game_over:
                self.block_X()


    #Postawienie znaczku na wolnym losowym miejscu
    def place_in_free_space(self, AI_move):
        free_space = 0
        for button in self.button_list:
            if button['text'] == " ":
                free_space += 1
                if free_space == AI_move:
                    self.place_mark(button)

#Obsluga pliku tekstowego - wczytanie nazwy gracza
def txt_File_Handling():
     try:
        my_File = open("data.txt", "rt")
        content = my_File.read()
        print("Current player: ", content)
        my_File.close()
     except:
        print("An error has occured!")



txt_File_Handling()
Game()