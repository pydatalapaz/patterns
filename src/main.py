import tkinter as tk
from bad import imprimir_factura


if __name__ == "__main__":
    page = tk.Tk()
    tk.Button(page, text="BUTTON", command=imprimir_factura).pack()
    tk.Text(page)
    page.mainloop()