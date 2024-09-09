import tkinter as tk
from tkinter import messagebox

class LanguageLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Language Learning App')
        self.root.iconbitmap('icon.ico')  # Set the app icon

        # Create checkboxes for language selection
        self.language = tk.StringVar(value='en')
        tk.Checkbutton(root, text='English', variable=self.language, onvalue='en', font=('Arial', 12)).pack(pady=5)
        tk.Checkbutton(root, text='Marathi', variable=self.language, onvalue='mr', font=('Arial', 12)).pack(pady=5)
        tk.Checkbutton(root, text='Hindi', variable=self.language, onvalue='hi', font=('Arial', 12)).pack(pady=5)

        # Create entry for user input
        tk.Label(root, text='Enter type (animals, birds, flowers, countries, alphabets):', font=('Arial', 12)).pack(pady=5)
        self.entry = tk.Entry(root, font=('Arial', 12))
        self.entry.pack(pady=5)

        # Create button to display vocabulary
        tk.Button(root, text='Get Vocabulary', command=self.get_vocabulary, font=('Arial', 12), bg='blue', fg='white').pack(pady=10)

    def get_vocabulary(self):
        input_type = self.entry.get().strip().lower()
        language = self.language.get()

        if input_type in vocabulary:
            items = vocabulary[input_type]
            translation = {word: data.get(language, word) for word, data in items.items()}
            output = "\n".join(f"{word.capitalize()}: {trans}" for word, trans in translation.items())
            messagebox.showinfo('Vocabulary', output)
        else:
            messagebox.showerror('Error', 'Invalid type entered. Please use animals, birds, flowers, countries, or alphabets.')

if __name__ == "__main__":
    vocabulary = {
        # Your vocabulary data here
    }
    root = tk.Tk()
    app = LanguageLearningApp(root)
    root.mainloop()
