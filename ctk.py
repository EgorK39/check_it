import customtkinter


class App(customtkinter.CTk):
    buttons = (('7', '8', '9', '/'),
               ('4', '5', '6', '*'),
               ('1', '2', '3', '-'),
               ('0', '.', 'Удалить', '+')
               )
    activeStr = ''
    stack = []

    def __init__(self):
        super().__init__()
        self.title("Калькулятор")
        self.geometry("400x250")
        self.resizable(True, False)

        self.label = customtkinter.CTkLabel(self, text='0', width=90, font=('', 20))
        self.label.grid(row=1, column=2, sticky="nsew")

        self.button = customtkinter.CTkButton(self, text='Результат', width=100, height=70,
                                              command=lambda text="=": self.click(
                                                  text=text))
        self.button.grid(row=1, column=4, sticky="nsew")
        for i in range(4):
            for k in range(4):
                self.button = customtkinter.CTkButton(self, text=self.buttons[i][k],
                                                      width=90,
                                                      corner_radius=4, fg_color='#ffffff', text_color='#4f4f4f',
                                                      border_color='#4f4f4f', border_width=1,
                                                      command=lambda row=i, col=k: self.click(
                                                          text=self.buttons[row][col]))
                self.button.grid(row=i + 2, column=k + 1, padx=2, pady=2)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def decode(self):
        operand2 = float(self.stack.pop())
        operation = self.stack.pop()
        operand1 = float(self.stack.pop())
        self.calculate(operand1, operand2, operation)
        self.activeStr = ''

    def calculate(self, operand1, operand2, operation):
        result = 0

        if operation == '+':
            result = operand1 + operand2
        if operation == '-':
            result = operand1 - operand2
        if operation == '/':
            result = operand1 / operand2
        if operation == '*':
            result = operand1 * operand2

        self.label.configure(text=str(result))

    def click(self, text):
        if text == 'Удалить':
            self.stack.clear()
            self.activeStr = ''
            self.label.configure(text='0')
        elif '0' <= text <= '9':
            self.activeStr += text
            self.label.configure(text=self.activeStr)
        elif text == '.':
            if self.activeStr.find('.') == -1:
                self.activeStr += text
                self.label.configure(text=self.activeStr)
        else:
            if len(self.stack) >= 2:
                self.stack.append(self.label.cget('text'))
                self.decode()
                self.stack.clear()
                self.stack.append(self.label.cget('text'))
                self.activeStr = ''
                if text != '=':
                    self.stack.append(text)
            else:
                if text == '-' and len(self.stack) == 0 and len(self.activeStr) < 1:
                    self.activeStr += text
                    self.label.configure(text=self.activeStr)
                elif text != '=':
                    self.stack.append(self.label.cget('text'))
                    self.stack.append(text)
                    self.activeStr = ''
                    self.label.configure(text='0')


app = App()
app.mainloop()
