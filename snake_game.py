import random
import customtkinter as custom

class Snake:
    def __init__(self, width: int, height : int):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self.body = [(3, 7), (4, 7), (5, 7)]
        self.direction = "d"
        self.alive = True

    def head(self):
        return self.body[-1]

    def take_step(self, apple_pos):
        x ,y = self.head()
        nh = None
        if self.direction == 'w': # UP
            nh = (x, y-1)
        elif self.direction == 's': # DOWN
            nh = (x,y+1)
        elif self.direction == 'a': # LEFT
           nh = (x-1, y)
        elif self.direction == 'd': # RIGHT
           nh = (x+1, y)

        nx, ny = nh
        if nx < 0 or nx >= self.width or ny < 0 or ny >= self.height:
            self.alive = False
            return "OUT_OF_BOUNDS"

        if nh in self.body:
            print("Game over you bit yourself")
            self.alive = False
            return "SELF_COLLISION"

        if nh ==apple_pos:
            self.body.append(nh)
            return "ATE_APPLE"

        else:
            self.body = self.body[1:] + [nh]
            return "MOVED"


class App(custom.CTk):
    def __init__(self):
        super().__init__()
        self.title("SNAKE")
        self.geometry("600x700")
        custom.set_appearance_mode("dark")

        #game constants
        self.CELL_SIZE = 30
        self.GRID_WIDTH = 15
        self.GRID_HEIGHT = 15
        self.SPEED = 100 #miliseconds between moves

        # Snake and Apple
        self.snake = Snake(self.GRID_WIDTH, self.GRID_HEIGHT)
        self.apple_pos = (0,0)
        self.score = 0
        self.running = False

        #UI elements
        self.score_label = custom.CTkLabel(self, text=f"Score: {self.score}", font=("Arial", 20))
        self.score_label.pack(pady=10)

        #canvas
        self.canvas = custom.CTkCanvas(self, width=self.GRID_WIDTH*self.CELL_SIZE, height=self.GRID_HEIGHT*self.CELL_SIZE,bg="#242424")
        self.canvas.pack(pady=20)

        #start
        self.start_button = custom.CTkButton(self, text="START GAME", command=self.start_game)
        self.start_button.pack(pady=10)

        # bind keys
        self.bind("<w>", lambda e: self.change_dir("w"))
        self.bind("<s>", lambda e: self.change_dir("s"))
        self.bind("<a>", lambda e: self.change_dir("a"))
        self.bind("<d>", lambda e: self.change_dir("d"))

    def start_game(self):
        self.snake.reset()
        self.score = 0
        self.score_label.configure(text="Score: 0", text_color="white")

        self.generate_apple()
        self.running = True
        self.start_button.configure(state="disabled", text="Playing...")

        self.render_canvas()
        self.after(500, self.game_loop)

    def generate_apple(self):
        snake_set = set(self.snake.body)
        open_space = [(x, y) for x in range(self.GRID_WIDTH) for y in range(self.GRID_HEIGHT) if (x, y) not in snake_set]
        if open_space:
            self.apple_pos = random.choice(open_space)
        else:
            self.running= False
            self.score_label.configure(text="YOU WIN! BOARD FULL", text_color="#FFD700")

    def change_dir(self, new_dir):
        opposites = {"w": "s", "s": "w", "a": "d", "d": "a"}
        if new_dir != opposites.get(self.snake.direction):
            self.snake.direction = new_dir

    def game_loop(self):
        if self.snake.alive and self.running:
            result = self.snake.take_step(self.apple_pos)
            if result == "ATE_APPLE":
                self.score +=10
                self.score_label.configure(text=f"SCORE {self.score}", text_color="#FFD700")
                self.generate_apple()
            elif result in ["OUT_OF_BOUNDS", 'SELF_COLLISION']:
                self.running = False
                self.score_label.configure(text="GAME OVER", text_color="#FFD700")
                self.start_button.configure(state="normal", text="Restart Game")
                return

            self.render_canvas()
            self.after(self.SPEED, self.game_loop)

    def render_canvas(self):
        self.canvas.delete("all")

        # Draw Apple (Red Circle)
        ax, ay = self.apple_pos
        padding = 5
        self.canvas.create_oval(
            ax * self.CELL_SIZE + padding, ay * self.CELL_SIZE + padding,
            (ax + 1) * self.CELL_SIZE - padding, (ay + 1) * self.CELL_SIZE - padding,
            fill="#ff4d4d", outline=""
        )

        # Draw Snake
        for i, (x, y) in enumerate(self.snake.body):
            # Head is a different color (Green), body is Blue
            is_head = (i == len(self.snake.body) - 1)
            color = "#2fa572" if is_head else "#1f6aa5"

            self.canvas.create_rectangle(
                x * self.CELL_SIZE, y * self.CELL_SIZE,
                (x + 1) * self.CELL_SIZE, (y + 1) * self.CELL_SIZE,
                fill=color, outline="#1a1a1a"
            )

if __name__ == '__main__':
    app = App()
    app.mainloop()