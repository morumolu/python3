import tkinter as tk


class TableData(object):
    def __init__(self):
        a = {'A1', 'A2'}
        b = {'B1', 'B2'}
        s = ['S1', 'S2', 'S3']
        self.hands = (a, b)
        self.offices = [list(), list()]
        self.street = s
        self.deck = list()
        self.discard = list()


class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.window_width = 1024
        self.window_height = 800
        self.tag2pos = {}
        self.board = tk.Canvas(self, width=self.window_width, height=self.window_height, bg="Green")
        self.title("FAMIGLIA")
        self.geometry("{}x{}".format(self.window_width, self.window_height))
        self.resizable(width=0, height=0)
        self.table = TableData()
        self.set_widgets()

    def set_widgets(self):
        self.board.pack()

        for index, tag in enumerate(self.table.hands[0]):
            x = 10 + 40 * index
            y = 10
            pos = (x, y, x + 40, y + 60)
            self.board.create_rectangle(*pos, fill="Peach Puff3", tags=tag)
            self.board.create_text(x + 20, y + 20,
                                   font=("Helvetica", 10, "bold"),
                                   text=tag,
                                   tags=tag)
            self.tag2pos[tag] = pos

        for index, tag in enumerate(self.table.hands[1]):
            x = 10 + 40 * index
            y = 70
            pos = (x, y, x + 40, y + 60)
            self.board.create_rectangle(*pos, fill="Peach Puff3", tags=tag)
            self.board.create_text(x + 20, y + 20,
                                   font=("Helvetica", 10, "bold"),
                                   text=tag,
                                   tags=tag)
            self.tag2pos[tag] = pos

        for index, tag in enumerate(self.table.street):
            x = 10 + 40 * index
            y = 210
            pos = (x, y, x + 40, y + 60)
            self.board.create_rectangle(*pos, fill="Peach Puff3", tags=tag)
            self.board.create_text(x + 20, y + 20,
                                   font=("Helvetica", 10, "bold"),
                                   text=tag,
                                   tags=tag)
            self.tag2pos[tag] = pos

        self.binding()

    def update_board(self, tag):
        pos = self.tag2pos[tag]
        self.board.create_rectangle(pos, fill="Peach Puff3", tags=tag)
        self.board.create_text(pos[0] + 20, pos[1] + 20,
                               font=("Helvetica", 10, "bold"),
                               text="AAA",
                               tags=tag)

    def binding(self):
        for tag in self.tag2pos.keys():
            self.board.tag_bind(tag, "<ButtonPress-1>", self.board_pressed)

    def board_pressed(self, event):
        _id = self.board.find_closest(event.x, event.y)
        tag = self.board.gettags(_id[0])[0]
        print("Tag {} pressed".format(tag))
        self.update_board(tag)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
