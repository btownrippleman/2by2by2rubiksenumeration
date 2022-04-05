from tkinter import *
from tkinter import messagebox

def clear_all_values(entries,root):
   for entry in entries:
      ent = entries[entry]
      ent.delete(0,END)

def showWarning(msg="Please enter in appropriate values"):
   messagebox.showwarning(message=msg)

def calculate_pay(entries,outputs):
   try:
      payrate = float(entries["Rate of Pay"].get())
      hours_worked = float(entries["Hours worked"].get())
      regular_pay = payrate * hours_worked
      print(regular_pay)
      outputs["Regular Pay"]["label_value"].config(text=str(regular_pay))
      overtime_hours = float(entries["Overtime Hours"].get())
      overtime_pay = 0
      if isinstance(overtime_hours, float):
         overtime_pay = payrate*1.5 * overtime_hours
         outputs["Overtime Pay"]["label_value"].config(text=str(overtime_pay))
      outputs["Total Pay"]["label_value"].config(text=str(overtime_pay+regular_pay))
   except:
      showWarning()

def populate_form(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, anchor='w',width=22, text=field)
      ent = Entry(row)
      ent.insert(0,"0")
      row.pack(side = TOP, fill = X, padx = 5 , pady = 15,anchor='w')
      lab.pack(side = TOP,anchor='w')
      ent.pack(side = LEFT)
      entries[field] = ent
   return entries
def makeoutputs(root, outputs):
   entries = {}
   for field in outputs:
      row = Frame(root)
      lab = Label(row, anchor='w',width=22, text=field)
      label_value = Label(row, anchor='w',width=22)
      row.pack(side = TOP, fill = X, padx = 5 , pady = 15,anchor='w')
      lab.pack(side = LEFT,anchor='w')
      label_value.pack(side=RIGHT)
      entries[field] = {"row":row,"label":lab, "label_value":label_value}
   return entries

if __name__ == '__main__':
   fields = ('First Name', 'Last Name', 'Rate of Pay', 'Hours worked', 'Overtime Hours')
   outputs = ("Overtime Pay", "Regular Pay", "Total Pay")
   root = Tk()
   root.title("Payment Calculator")
   ents = populate_form(root, fields)
   outs = makeoutputs(root, outputs)
   root.bind('<Return>', (lambda event, e = ents: fetch(e)))
   root.bind('<Return>', (lambda event, e = outs: fetch(e)))

   b1 = Button(root, text = 'Calculate Pay',
      command=(lambda e = ents: calculate_pay(e,outs)))
   b1.pack(side = LEFT, padx = 5, pady = 45)
   b2 = Button(root, text='Clear',
   command=lambda e = ents: clear_all_values(e,root))
   b2.pack(side = LEFT, padx = 5, pady = 45)
   b3 = Button(root, text = 'Exit', command = root.quit)
   b3.pack(side = LEFT, padx = 5, pady = 45)
   root.mainloop()