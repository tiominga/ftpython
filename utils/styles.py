from tkinter import PhotoImage

class Style():

    @staticmethod
    def label():
        return {"font":"Arial 12","fg":"blue"}

    @staticmethod
    def button():
        return {"width":"20","height":"1","fg":"white","bg":"blue","font":"Arial 10 bold","anchor":"e"}

    @staticmethod
    def button_ok():
        # image = "static/images/ok.png" "image":PhotoImage(file=image),
        return {"width":"10","height":"5","fg":"white","bg":"blue","font":"Arial 10 bold","anchor":"e"}

    @staticmethod
    def panel():
        return {"bg":"red","bd":"2", "relief":"solid"}