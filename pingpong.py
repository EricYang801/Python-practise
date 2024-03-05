import tkinter as tk
import random

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        
        self.x = random.choice([-3, 3])
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.score = 0

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            self.canvas.create_text(250, 200, text="Game Over", font=("Helvetica", 30), fill="red")
            self.x = 0
            self.y = 0
        if self.hit_paddle(pos):
            self.y = -3
            self.score += 1
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 350)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -10

    def turn_right(self, evt):
        self.x = 10

def update_game():
    ball.draw()
    paddle.draw()
    canvas.itemconfig(score_text, text="Score: " + str(ball.score))
    
    if not ball.hit_bottom:
        tk_root.after(20, update_game)
    
tk_root = tk.Tk()
tk_root.title("Game")
canvas = tk.Canvas(tk_root, width=500, height=400, bd=0, highlightthickness=0, bg="white")
canvas.pack()
tk_root.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

score_text = canvas.create_text(50, 20, text="Score: " + str(ball.score), font=("Helvetica", 20), fill="black")

update_game()

tk_root.mainloop()

