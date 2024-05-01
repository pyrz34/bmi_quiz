import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300,height=300)
window.config(padx=30,pady=30)


def calculate_bmi(event = None):
    try:
        weight = float(weight_input.get())
        height = float(height_input.get())
        bmi = weight / ((height / 100) ** 2)
        result_label.config(text=f"Your BMI is : {bmi:.2f}")

        if bmi < 18.5:
            result_label.config(text=f"Your BMI is :{bmi: .2f}. You are underweight")
        elif bmi >= 18.5 and bmi <= 24.9:
            result_label.config(text=f"Your BMI is : {bmi:.2f}.You are normal")
        elif bmi >= 25 and bmi <= 29.9:
            result_label.config(text=f"Your BMI is : {bmi:.2f}.You are over weight")
        elif bmi >= 30 and bmi <= 34.9:
            result_label.config(text=f"Your BMI is : {bmi:.2f}.You are obesity(Class 1")
        elif bmi >= 35 and bmi <= 39.9:
            result_label.config(text=f"Your BMI is : {bmi:.2f}. You are obesity(Class 2")
        else:
            result_label.config(text=f"Your BMI is : {bmi:.2f}.You are extreme obesity")


    except ValueError:
        result_label.config(text="please enter valid number.")





weight_label =tkinter.Label(text="enter your weight (kg)")
weight_label.pack()

weight_input = tkinter.Entry(width=10)
weight_input.pack()
weight_input.bind("<Return>",calculate_bmi)#enter tuşuna basıldığında komut alsın

height_label =tkinter.Label(text="enter your height (cm)")
height_label.pack()

height_input = tkinter.Entry(width=10)
height_input.pack()
height_input.bind("<Return>",calculate_bmi)

button_clicked = tkinter.Button(text="calculate",command=calculate_bmi)
button_clicked.pack()

result_label =tkinter.Label(text="")
result_label.pack()




window.mainloop()