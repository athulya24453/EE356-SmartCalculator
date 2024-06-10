from tkinter import *

class ScientificCalculator:
    def __init__(self):
        self.tk_calc = Tk()
        self.tk_calc.configure(bg="#293C4A", bd=10)
        self.tk_calc.title("Smart Calculator")
        self.tk_calc.geometry("330x500")

        self.calc_operator = ""
        self.text_input = StringVar()

        self.text_display = Entry(self.tk_calc, font=('sans-serif', 20, 'bold'), textvariable=self.text_input,
                                  bd=5, insertwidth=5, bg='#BBB', justify='right')
        self.text_display.grid(columnspan=5, padx=10, pady=15)

        self.button_params = {'bd': 5, 'fg': '#BBB', 'bg': '#3C3636', 'font': ('sans-serif', 15, 'bold')}
        self.button_params_main = {'bd': 5, 'fg': '#000', 'bg': '#BBB', 'font': ('sans-serif', 20, 'bold')}

        # Configure rows and columns to have equal weight
        for i in range(10):  # Adjusted to 10 because there are 10 rows
            self.tk_calc.grid_rowconfigure(i, weight=1)
            self.tk_calc.grid_columnconfigure(i, weight=1)

        self.create_buttons()

    def button_click(self, char):
        self.calc_operator += str(char)
        self.text_input.set(self.calc_operator)

    def button_clear_all(self):
        self.calc_operator = ""
        self.text_input.set("")

    def button_delete(self):
        text = self.calc_operator[:-1]
        self.calc_operator = text
        self.text_input.set(text)

    def sign_change(self):
        if self.calc_operator[0] == '-':
            temp = self.calc_operator[1:]
        else:
            temp = '-' + self.calc_operator
        self.calc_operator = temp
        self.text_input.set(temp)

    def percent(self):
        temp = str(eval(self.calc_operator + '/100'))
        self.calc_operator = temp
        self.text_input.set(temp)

    def button_equal(self):
        try:
            temp_op = str(eval(self.calc_operator))
            self.text_input.set(temp_op)
            self.calc_operator = temp_op
        except Exception as e:
            self.text_input.set("Error")
            self.calc_operator = ""

    def create_buttons(self):
        # Buttons

        #--1st row--
        abs_value = Button(self.tk_calc, self.button_params, text='abs', command=lambda: self.button_click('abs(')).grid(row=1, column=0, sticky="nsew")
        modulo = Button(self.tk_calc, self.button_params, text='mod', command=lambda: self.button_click('%')).grid(row=1, column=1, sticky="nsew")
        eulers_num = Button(self.tk_calc, self.button_params, text='e', command=lambda: self.button_click('e')).grid(row=1, column=2, sticky="nsew")

        #--2nd row--
        sine = Button(self.tk_calc, self.button_params, text='sin', command=lambda: self.button_click('sin(')).grid(row=2, column=0, sticky="nsew")
        cosine = Button(self.tk_calc, self.button_params, text='cos', command=lambda: self.button_click('cos(')).grid(row=2, column=1, sticky="nsew")
        pi_num = Button(self.tk_calc, self.button_params, text='π', command=lambda: self.button_click('π')).grid(row=2, column=2, sticky="nsew")

        #--3rd row--
        second_power = Button(self.tk_calc, self.button_params, text='x\u00B2', command=lambda: self.button_click('**2')).grid(row=3, column=0, sticky="nsew")
        third_power = Button(self.tk_calc, self.button_params, text='x\u00B3', command=lambda: self.button_click('**3')).grid(row=3, column=1, sticky="nsew")
        nth_power = Button(self.tk_calc, self.button_params, text='x^n', command=lambda: self.button_click('**')).grid(row=3, column=2, sticky="nsew")

        #--4th row--
        square_root = Button(self.tk_calc, self.button_params, text='\u00B2\u221A', command=lambda: self.button_click('sqrt(')).grid(row=4, column=0, sticky="nsew")
        third_root = Button(self.tk_calc, self.button_params, text='\u00B3\u221A', command=lambda: self.button_click('cbrt(')).grid(row=4, column=1, sticky="nsew")
        nth_root = Button(self.tk_calc, self.button_params, text='\u221A', command=lambda: self.button_click('**(1/')).grid(row=4, column=2, sticky="nsew")

        #--5th row (Arrow keys in a curved shape)--
        up_arrow = Button(self.tk_calc, self.button_params, text='↑', command=lambda: self.button_click('↑')).grid(row=5, column=1, sticky="nsew")
        left_arrow = Button(self.tk_calc, self.button_params, text='←', command=lambda: self.button_click('←')).grid(row=6, column=0, sticky="nsew")
        right_arrow = Button(self.tk_calc, self.button_params, text='→', command=lambda: self.button_click('→')).grid(row=6, column=2, sticky="nsew")
        down_arrow = Button(self.tk_calc, self.button_params, text='↓', command=lambda: self.button_click('↓')).grid(row=7, column=1, sticky="nsew")

        #--6th row--
        button_7 = Button(self.tk_calc, self.button_params_main, text='7', command=lambda: self.button_click('7')).grid(row=8, column=0, sticky="nsew")
        button_8 = Button(self.tk_calc, self.button_params_main, text='8', command=lambda: self.button_click('8')).grid(row=8, column=1, sticky="nsew")
        button_9 = Button(self.tk_calc, self.button_params_main, text='9', command=lambda: self.button_click('9')).grid(row=8, column=2, sticky="nsew")
        delete_one = Button(self.tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'), text='DEL', command=self.button_delete, bg='#db701f').grid(row=8, column=3, sticky="nsew")
        delete_all = Button(self.tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'), text='AC', command=self.button_clear_all, bg='#db701f').grid(row=8, column=4, sticky="nsew")

        #--7th row--
        button_4 = Button(self.tk_calc, self.button_params_main, text='4', command=lambda: self.button_click('4')).grid(row=9, column=0, sticky="nsew")
        button_5 = Button(self.tk_calc, self.button_params_main, text='5', command=lambda: self.button_click('5')).grid(row=9, column=1, sticky="nsew")
        button_6 = Button(self.tk_calc, self.button_params_main, text='6', command=lambda: self.button_click('6')).grid(row=9, column=2, sticky="nsew")
        mul = Button(self.tk_calc, self.button_params_main, text='*', command=lambda: self.button_click('*')).grid(row=9, column=3, sticky="nsew")
        div = Button(self.tk_calc, self.button_params_main, text='/', command=lambda: self.button_click('/')).grid(row=9, column=4, sticky="nsew")

        #--8th row--
        button_1 = Button(self.tk_calc, self.button_params_main, text='1', command=lambda: self.button_click('1')).grid(row=10, column=0, sticky="nsew")
        button_2 = Button(self.tk_calc, self.button_params_main, text='2', command=lambda: self.button_click('2')).grid(row=10, column=1, sticky="nsew")
        button_3 = Button(self.tk_calc, self.button_params_main, text='3', command=lambda: self.button_click('3')).grid(row=10, column=2, sticky="nsew")
        add = Button(self.tk_calc, self.button_params_main, text='+', command=lambda: self.button_click('+')).grid(row=10, column=3, sticky="nsew")
        sub = Button(self.tk_calc, self.button_params_main, text='-', command=lambda: self.button_click('-')).grid(row=10, column=4, sticky="nsew")

        #--9th row--
        button_0 = Button(self.tk_calc, self.button_params_main, text='0', command=lambda: self.button_click('0')).grid(row=11, column=0, sticky="nsew")
        point = Button(self.tk_calc, self.button_params_main, text='.', command=lambda: self.button_click('.')).grid(row=11, column=1, sticky="nsew")
        exp = Button(self.tk_calc, self.button_params_main, text='EXP', font=('sans-serif', 16, 'bold'), command=lambda: self.button_click('E')).grid(row=11, column=2, sticky="nsew")
        equal = Button(self.tk_calc, self.button_params_main, text='=', command=self.button_equal).grid(row=11, columnspan=2, column=3, sticky="nsew")

    def run(self):
        self.tk_calc.mainloop()

# Instantiate the ScientificCalculator class and run the GUI
calculator = ScientificCalculator()
calculator.run()
