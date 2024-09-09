
    # Add other categories...


class LanguageLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Language Learning App')
        self.root.geometry('400x300')  # Set window size

        # Create a canvas for animation
        self.canvas = tk.Canvas(root, width=400, height=300, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Display the animation
        self.show_welcome_animation()

    def show_welcome_animation(self):
        # Draw a text on the canvas
        self.text = self.canvas.create_text(200, 150, text='Welcome to Language World', font=('Arial', 24, 'bold'), fill='blue')

        # Animate the text appearance
        self.animate_text()

    def animate_text(self):
        # Initial delay and increment
        self.alpha = 0
        self.text_id = self.canvas.after(100, self.update_text_opacity)

    def update_text_opacity(self):
        # Increment opacity
        if self.alpha < 1.0:
            self.alpha += 0.05
            # Change the text color based on opacity
            self.canvas.itemconfig(self.text, fill=self.get_color_with_alpha('blue', self.alpha))
            self.text_id = self.canvas.after(100, self.update_text_opacity)
        else:
            # Start the main application after animation
            self.canvas.after(500, self.show_main_app)

    def get_color_with_alpha(self, color, alpha):
        # Create a color with transparency
        r, g, b = self.canvas.winfo_rgb(color)
        r = int(r * alpha / 65535)
        g = int(g * alpha / 65535)
        b = int(b * alpha / 65535)
        return f'#{r:02x}{g:02x}{b:02x}'

    def show_main_app(self):
        # Destroy the canvas and create the main app
        self.canvas.destroy()
        self.create_main_ui()
