#Chuyển đổi file text từ định dạng txt sang định dạng JSON
import datetime
import json

file_name = "TuDien_AnhViet108856.txt"

response = ""
with open(file_name, "r", encoding="utf-8") as file:
    response = file.read()

#Xử lí dữ liệu 
data = {}
lines = response.replace(" /", "\n-/").split("\n")

word = ""
meanings = []
for line in lines:
    if line.startswith("-/") or line.startswith("*") or line.startswith("-") or line.startswith("="):
        meaning = line[0:].strip().replace("-/", "\nPhiên âm:/").replace("*", "\nLoại Từ:").replace("-", "\nNghĩa:").replace("=", "\nVí Dụ:")

        if word:
            meanings.append(meaning)
        else:
            word = meaning

    elif line.startswith("@"):
        if word:
            data[word] = meanings.copy()
            meanings.clear()
        word = line[1:].strip()
        
# Lưu ý nếu word còn giá trị sau khi kết thúc vòng lặp, lưu meanings vào data
if word:
    data[word] = meanings.copy()

# Lưu dữ liệu thành file JSON
json_data = json.dumps(data, ensure_ascii=False)

# Ghi dữ liệu vào file json
with open('dictionary.json', 'w', encoding='utf-8') as file:
    file.write(json_data)

print("Chuyển đổi thành công. Đã lưu dữ liệu thành file json.")

file_dic = "dictionary.json"

# Đọc dữ liệu từ file JSON
with open(file_dic, 'r', encoding='utf-8') as file:
    data = json.load(file)

#Chương trình dịch Anh-Việt gồm 2 chức năng : Tra từ và Thêm từ
import json

def load_dictionary(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as json_file:
            dictionary = json.load(json_file)
    except FileNotFoundError:
        dictionary = {}
    
    return dictionary

def save_dictionary(dictionary, file_name):
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(dictionary, json_file, indent=4, ensure_ascii=False)

def translate_word(dictionary, word):
    if word in dictionary:
        return dictionary[word]
    else:
        return "Không tìm thấy từ này trong từ điển."

def add_word(dictionary, word, translation):
    dictionary[word] = translation
    return dictionary

file_name = 'dictionary.json'
dictionary = load_dictionary(file_name)
#Ghi nội dung đã tra cứu ra file txt
def LichSu(CheDo,NoiDung):
    f=open("NhatKy.txt",mode=CheDo,encoding='utf-8')
    f.write(f"{NoiDung}\n")
    f.close()

while True:
    print("===== Từ điển Anh-Việt =====")
    print("1. Dịch từ")
    print("2. Thêm từ")
    print("3. Thoát")

    choice = input("Nhập lựa chọn của bạn: ")

    if choice == "1":
        word = input("Nhập từ cần dịch: ")
        translation = translate_word(dictionary, word)
        ND = str(datetime.datetime.now())+":"+word+":"+str(translation)
        LichSu('a',ND)
        print(f"Nghĩa của từ '{word}' là: {translation}")
    elif choice == "2":
        word = input("Nhập từ mới: ")
        translation = input("Nhập nghĩa của từ mới: ")
        dictionary = add_word(dictionary, word, translation)
        save_dictionary(dictionary, file_name)
        ND = str(datetime.datetime.now())+":"+word+":"+str(translation)
        LichSu('a',ND)
        print(f"Từ '{word}' đã được thêm vào từ điển.")
    elif choice == "3":
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

