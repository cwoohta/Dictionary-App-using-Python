import tkinter as tk
import json

def translate_word():
    word = word_entry.get().lower()
    if word in dictionary:
        translation = dictionary[word]
    else:
        translation = "Không tìm thấy từ này trong từ điển."
    translation_label.config(text=translation)

def add_word():
    word = new_word_entry.get().lower()
    translation = new_translation_entry.get()
    dictionary[word] = translation
    save_dictionary()
    new_word_entry.delete(0, tk.END)
    new_translation_entry.delete(0, tk.END)
    new_word_entry.focus()

def save_dictionary():
    with open('dictionary.json', 'w') as file:
        json.dump(dictionary, file)

# Tạo cửa sổ ứng dụng
window = tk.Tk()
window.title("Dictionary App")

# Đọc dữ liệu từ file JSON
with open('dictionary.json', 'r',encoding='utf-8') as file:
    dictionary = json.load(file)

# Tạo các thành phần giao diện
word_label = tk.Label(window, text="Từ:", font=("Helvetica", 16))
word_label.pack()

word_entry = tk.Entry(window, font=("Helvetica", 16))
word_entry.pack()

translate_button = tk.Button(window, text="Dịch", command=translate_word, font=("Helvetica", 16))
translate_button.pack()

translation_label = tk.Label(window, text="", font=("Helvetica", 16))
translation_label.pack()

# Thêm chức năng thêm từ mới
new_word_label = tk.Label(window, text="Từ mới:", font=("Helvetica", 16))
new_word_label.pack()

new_word_entry = tk.Entry(window, font=("Helvetica", 16))
new_word_entry.pack()

new_translation_label = tk.Label(window, text="Bản dịch:", font=("Helvetica", 16))
new_translation_label.pack()

new_translation_entry = tk.Entry(window, font=("Helvetica", 16))
new_translation_entry.pack()

add_button = tk.Button(window, text="Thêm từ", command=add_word, font=("Helvetica", 16))
add_button.pack()

# Trang trí app
window.configure(bg="#f5f5f5")  # Màu nền của cửa sổ
word_label.configure(fg="#333333")  # Màu chữ của nhãn "Từ"
word_entry.configure(bg="#ffffff")  # Màu nền của ô nhập liệu "Từ"
translate_button.configure(bg="#ffffff", fg="#333333")  # Màu nền và màu chữ của nút "Dịch"
translation_label.configure(bg="#f5f5f5", bd=1, relief="solid")  # Màu nền và hiệu ứng viền của nhãn kết quả dịch
new_word_label.configure(fg="#333333")  # Màu chữ của nhãn "Từ mới"
new_word_entry.configure(bg="#ffffff")  # Màu nền của ô nhập liệu "Từ mới"
new_translation_label.configure(fg="#333333")  # Màu chữ của nhãn "Bản dịch"
new_translation_entry.configure(bg="#ffffff")  # Màu nền của ô nhập liệu "Bản dịch"

# Khởi chạy ứng dụng
window.mainloop()
