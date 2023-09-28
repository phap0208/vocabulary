import tkinter as tk
import random
from tkinter import messagebox
import mysql.connector

def show_study_vocabulary_window():
    study_vocabulary_window = tk.Toplevel()
    study_vocabulary_window.title("Học từ vựng")
    study_vocabulary_window.geometry("400x300")  # Đặt kích thước cửa sổ

    label_word = tk.Label(study_vocabulary_window, text="Từ vựng:", font=("Arial", 16))
    label_word.pack()

    word_display = tk.Label(study_vocabulary_window, font=("Arial", 24, "bold"))
    word_display.pack()

    label_meaning = tk.Label(study_vocabulary_window, text="Nghĩa:", font=("Arial", 16))
    label_meaning.pack()

    meaning_display = tk.Label(study_vocabulary_window, font=("Arial", 18))
    meaning_display.pack()

    def load_random_word():
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="vocabulary"
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM vocabulary")
            all_words = cursor.fetchall()

            if not all_words:
                messagebox.showinfo("Thông báo", "Không có từ vựng nào trong cơ sở dữ liệu.")
                return

            random_word = random.choice(all_words)
            word_display.config(text=random_word[1])
            meaning_display.config(text=random_word[2])

            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi: {str(e)}")

    load_random_word()

    btn_next = tk.Button(study_vocabulary_window, text="Từ tiếp theo", font=("Arial", 14), command=load_random_word)
    btn_next.pack()

    study_vocabulary_window.mainloop()
