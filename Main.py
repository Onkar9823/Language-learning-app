import tkinter as tk
from tkinter import messagebox

# Sample vocabulary data
vocabulary = {
    "Animals": {"English": ["Dog", "Cat", "Cow", "Elephant", "Tiger"],
                "Hindi": ["कुत्ता", "बिल्ली", "गाय", "हाथी", "बाघ"],
                "Marathi": ["कुत्रा", "मांजर", "गाय", "हत्ती", "वाघ"]},
    "Flowers": {"English": ["Rose", "Lily", "Tulip", "Sunflower", "Daisy"],
                "Hindi": ["गुलाब", "कुमुदिनी", "ट्यूलिप", "सूरजमुखी", "गुलबहार"],
                "Marathi": ["गुलाब", "कमळ", "ट्यूलिप", "सूर्यफूल", "झेंडू"]},
    "Fruits": {"English": ["Apple", "Banana", "Mango", "Orange", "Grapes"],
               "Hindi": ["सेब", "केला", "आम", "संतरा", "अंगूर"],
               "Marathi": ["सफरचंद", "केळी", "आंबा", "संत्रा", "द्राक्षे"]},
    "Birds": {"English": ["Sparrow", "Peacock", "Parrot", "Crow", "Pigeon"],
              "Hindi": ["गौरैया", "मोर", "तोता", "कौआ", "कबूतर"],
              "Marathi": ["चिमणी", "मोर", "पोपट", "कावळा", "कबूतर"]},
    "Countries": {"English": ["India", "USA", "China", "Japan", "Germany"],
                  "Hindi": ["भारत", "अमेरिका", "चीन", "जापान", "जर्मनी"],
                  "Marathi": ["भारत", "अमेरिका", "चीन", "जपान", "जर्मनी"]}
}
# Function to play audio pronunciation
def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


# Function to display welcome animation
def welcome_animation():
    welcome_label = tk.Label(root, text="Welcome", font=("Helvetica", 24), fg="blue")
    welcome_label.pack()
    for i in range(10):
        welcome_label.place(x=50 + i*10, y=50 + i*10)
        root.update()
        root.after(100)
    welcome_label.destroy()

# Function to display exit animation
def exit_animation():
    exit_label = tk.Label(root, text="Goodbye!", font=("Helvetica", 24), fg="red")
    exit_label.pack()
    for i in range(10):
        exit_label.place(x=50 + i*10, y=50 + i*10)
        root.update()
        root.after(100)
    root.destroy()

# Function to create quiz
def create_quiz():
    quiz_window = tk.Toplevel(root)
    quiz_window.title("Quiz")
    tk.Label(quiz_window, text="Quiz Part").pack()

# Function to search vocabulary
def search_vocabulary():
    search_term = search_entry.get()
    result = ""
    for category, words in vocabulary.items():
        for lang, word_list in words.items():
            if search_term in word_list:
                result += f"{category} ({lang}): {search_term}\n"
    messagebox.showinfo("Search Result", result)

# Main application window
root = tk.Tk()
root.title("Language Learning App")

# Welcome animation
welcome_animation()

# Vocabulary section
vocab_frame = tk.Frame(root)
vocab_frame.pack()

tk.Label(vocab_frame, text="Vocabulary", font=("Helvetica", 18)).pack()
for category, words in vocabulary.items():
    tk.Label(vocab_frame, text=category, font=("Helvetica", 14)).pack()
    for lang, word_list in words.items():
        tk.Label(vocab_frame, text=f"{lang}: {', '.join(word_list)}").pack()

# Language selection checkboxes
input_lang = tk.StringVar(value="English")
output_lang = tk.StringVar(value="English")

tk.Label(root, text="Input Language:").pack()
for lang in ["English", "Hindi", "Marathi"]:
    tk.Radiobutton(root, text=lang, variable=input_lang, value=lang).pack()

tk.Label(root, text="Output Language:").pack()
for lang in ["English", "Hindi", "Marathi"]:
    tk.Radiobutton(root, text=lang, variable=output_lang, value=lang).pack()

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Submit", bg="black", fg="white").pack(side=tk.LEFT)
tk.Button(button_frame, text="Next", bg="black", fg="white").pack(side=tk.LEFT)
tk.Button(button_frame, text="Back", bg="black", fg="white").pack(side=tk.LEFT)
tk.Button(button_frame, text="Exit", bg="black", fg="white", command=exit_animation).pack(side=tk.LEFT)

# Quiz button
tk.Button(root, text="Quiz", command=create_quiz).pack()

# Search bar
search_frame = tk.Frame(root)
search_frame.pack()
search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT)
tk.Button(search_frame, text="Search", command=search_vocabulary).pack(side=tk.LEFT)

root.mainloop()
