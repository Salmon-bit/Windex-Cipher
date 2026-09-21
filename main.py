import tkinter
import customtkinter as ctk
import data


WINDEX_ALPHABET = "!AaBbCcDdEeFf123456"
MAIN_ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789., !?:;@/\\|_+-'\"#₽&()*~`•√π÷×§∆£€$¢^°={}©®™✓[]<>абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСИУФХЦЧШЩЪЫЬЭЮЯ"
DIVIDER = len(WINDEX_ALPHABET) - 1
SEPARATOR = ":"


def encode(text: str) -> str:
	indexes = []
	for s in text:
		num = MAIN_ALPHABET.index(s) + 1
		print(num)
		if num <= DIVIDER:
			indexes.append((0, num))
		elif num % DIVIDER == 0:
			indexes.append((num // DIVIDER, 0))
		else:
			indexes.append((num // DIVIDER, num % DIVIDER))
	output = []
	for i in indexes:
		ap = ""
		for n in i:
			print(n)
			ap += WINDEX_ALPHABET[n]
		output.append(ap)
	
	return SEPARATOR.join(output)


def decode(text: str) -> str:
	if text[-1] == SEPARATOR:
		text = text[:-1]
	input = text.split(SEPARATOR)
	output = ""
	for i in input:
		k = WINDEX_ALPHABET.index(i[0]) * DIVIDER
		n = WINDEX_ALPHABET.index(i[1])
		k += n
		m = MAIN_ALPHABET[k - 1]
		output += m
	
	return output


class Main(ctk.CTk):
    def __init__(self):
        global WINDEX_ALPHABET, MAIN_ALPHABET, SEPARATOR
        super().__init__()

        self.geometry("300x535")
        self.title("Windex Cipher")

        try:
            dat = data.get_settings()
        except FileNotFoundError:
            data.save_default_data()
            dat = data.get_settings()
        try:
            WINDEX_ALPHABET = dat["windex_alphabet"]
            MAIN_ALPHABET = dat["main_alphabet"]
            SEPARATOR = dat["separator"]
        except KeyError:
            data.save_default_data()
            dat = data.get_settings()

            WINDEX_ALPHABET = dat["windex_alphabet"]
            MAIN_ALPHABET = dat["main_alphabet"]
            SEPARATOR = dat["separator"]

        print("Loaded data succefully!")

        self.encode_var = tkinter.BooleanVar(value=True)
        
        self.title_label = ctk.CTkLabel(master=self, text="Windex Cipher")
        self.input_tb = ctk.CTkTextbox(master=self) 
        self.radio_frame = ctk.CTkFrame(master=self)
        self.encode_rb = ctk.CTkRadioButton(master=self.radio_frame, variable=self.encode_var, value=True, text="Закодировать")
        self.decode_rb = ctk.CTkRadioButton(master=self.radio_frame, variable=self.encode_var, value=False, text="Декодировать")
        self.output_lebel = ctk.CTkLabel(master=self, text="Вывод:")
        self.output_tb = ctk.CTkTextbox(master=self)
        self.output_tb.configure(state="disabled")
        self.submit_btn = ctk.CTkButton(master=self, text="Преобразовать", command=self.process)

        self.place_stuff()

    def place_stuff(self):
        self.title_label.pack()
        self.input_tb.pack()
        self.radio_frame.pack(pady=5)
        self.encode_rb.grid(column=0, row=0, padx=5, pady=5)
        self.decode_rb.grid(column=1, row=0, padx=(0, 5), pady=5)
        self.output_lebel.pack()
        self.output_tb.pack()
        self.submit_btn.pack(pady=5)

    def process(self):
        self.output_tb.configure(state="normal")
        try:
            if self.encode_var.get():
                self.output_tb.delete("0.0", "end")
                self.output_tb.insert("0.0", encode(self.input_tb.get("0.0", "end").strip()))
            else:
                self.output_tb.delete("0.0", "end")
                self.output_tb.insert("0.0", decode(self.input_tb.get("0.0", "end").strip()))
       except:
            self.output_tb.delete("0.0", "end")
            self.output_tb.insert("0.0", "Не удалось успешно закодировать/декодировать информацию.\nВ ваших входниых данных, возможно, ошибка.")
        self.output_tb.configure(state="disabled")

    
if __name__ == "__main__":
    win = Main()
    win.mainloop()
