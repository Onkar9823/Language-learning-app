import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Vocabulary data
vocabulary = {
    'birds': {
        'English': ['Sparrow', 'Peacock', 'Parrot', 'Eagle', 'Owl', 'Crow', 'Pigeon', 'Duck', 'Swan', 'Flamingo', 'Penguin', 'Seagull', 'Woodpecker', 'Kingfisher', 'Hummingbird', 'Robin', 'Canary', 'Dove', 'Hawk', 'Falcon'],
        'Hindi': ['गौरैया', 'मोर', 'तोता', 'गरुड़', 'उल्लू', 'कौआ', 'कबूतर', 'बत्तख', 'हंस', 'राजहंस', 'पेंगुइन', 'समुद्री बगुला', 'कठफोड़वा', 'रामचिरैया', 'हमिंगबर्ड', 'रॉबिन', 'कैनरी', 'फाख्ता', 'बाज़', 'शाहीन'],
        'Marathi': ['चिमणी', 'मोर', 'पोपट', 'गरुड', 'घुबड', 'कावळा', 'पारवा', 'बदक', 'हंस', 'राजहंस', 'पेंग्विन', 'समुद्री बगळा', 'कठफोडा', 'रामचिरैया', 'हमिंगबर्ड', 'रॉबिन', 'कॅनरी', 'फाक्ता', 'बाज', 'शाहीन']
    },
    'flowers': {
        'English': ['Rose', 'Lily', 'Tulip', 'Sunflower', 'Daisy', 'Marigold', 'Lotus', 'Jasmine', 'Orchid', 'Lavender', 'Hibiscus', 'Daffodil', 'Chrysanthemum', 'Bougainvillea', 'Poppy', 'Carnation', 'Iris', 'Peony', 'Violet', 'Magnolia'],
        'Hindi': ['गुलाब', 'कुमुदिनी', 'ट्यूलिप', 'सूरजमुखी', 'गुलबहार', 'गेंदा', 'कमल', 'चमेली', 'ऑर्किड', 'लैवेंडर', 'गुड़हल', 'नरगिस', 'गुलदाउदी', 'बोगनवेलिया', 'पोस्ता', 'कार्नेशन', 'आईरिस', 'पियोनी', 'बनफूल', 'चंपा'],
        'Marathi': ['गुलाब', 'कमळ', 'ट्यूलिप', 'सूर्यफूल', 'गुलबहार', 'झेंडू', 'कमळ', 'चमेली', 'ऑर्किड', 'लॅव्हेंडर', 'जास्वंद', 'नरगिस', 'गुलदाउदी', 'बोगनवेल', 'पोस्त', 'कार्नेशन', 'आईरिस', 'पियोनी', 'वायलेट', 'चंपा']
    },
    'fruits': {
        'English': ['Apple', 'Banana', 'Mango', 'Orange', 'Grapes', 'Pineapple', 'Strawberry', 'Watermelon', 'Papaya', 'Guava', 'Peach', 'Cherry', 'Pomegranate', 'Kiwi', 'Lemon', 'Lychee', 'Blueberry', 'Raspberry', 'Blackberry', 'Coconut'],
        'Hindi': ['सेब', 'केला', 'आम', 'संतरा', 'अंगूर', 'अनानास', 'स्ट्रॉबेरी', 'तरबूज', 'पपीता', 'अमरूद', 'आड़ू', 'चेरी', 'अनार', 'कीवी', 'नींबू', 'लीची', 'ब्लूबेरी', 'रास्पबेरी', 'ब्लैकबेरी', 'नारियल'],
        'Marathi': ['सफरचंद', 'केळ', 'आंबा', 'संत्रा', 'द्राक्ष', 'अननस', 'स्ट्रॉबेरी', 'कलिंगड', 'पपई', 'पेरू', 'सफरचंद', 'चेरी', 'डाळिंब', 'कीवी', 'लिंबू', 'लीची', 'ब्लूबेरी', 'रास्पबेरी', 'ब्लॅकबेरी', 'नारळ']
    },
    'animals': {
        'English': ['Lion', 'Tiger', 'Elephant', 'Dog', 'Cat', 'Horse', 'Cow', 'Goat', 'Sheep', 'Monkey', 'Deer', 'Rabbit', 'Bear', 'Wolf', 'Fox', 'Giraffe', 'Zebra', 'Kangaroo', 'Panda', 'Leopard'],
        'Hindi': ['शेर', 'बाघ', 'हाथी', 'कुत्ता', 'बिल्ली', 'घोड़ा', 'गाय', 'बकरी', 'भेड़', 'बंदर', 'हिरण', 'खरगोश', 'भालू', 'भेड़िया', 'लोमड़ी', 'जिराफ', 'ज़ेबरा', 'कंगारू', 'पांडा', 'तेंदुआ'],
        'Marathi': ['सिंह', 'वाघ', 'हत्ती', 'कुत्रा', 'मांजर', 'घोडा', 'गाय', 'शेळी', 'मेंढी', 'माकड', 'हरिण', 'ससा', 'अस्वल', 'लांडगा', 'कोल्हा', 'जिराफ', 'झेब्रा', 'कांगारू', 'पांडा', 'बिबट्या']
    },
    'countries': {
        'English': ['India', 'USA', 'China', 'Japan', 'Germany', 'France', 'Italy', 'Brazil', 'Canada', 'Australia', 'Russia', 'UK', 'South Africa', 'Mexico', 'Spain', 'Argentina', 'Egypt', 'Turkey', 'Saudi Arabia', 'Indonesia'],
        'Hindi': ['भारत', 'अमेरिका', 'चीन', 'जापान', 'जर्मनी', 'फ्रांस', 'इटली', 'ब्राजील', 'कनाडा', 'ऑस्ट्रेलिया', 'रूस', 'यूके', 'दक्षिण अफ्रीका', 'मेक्सिको', 'स्पेन', 'अर्जेंटीना', 'मिस्र', 'तुर्की', 'सऊदी अरब', 'इंडोनेशिया'],
        'Marathi': ['भारत', 'अमेरिका', 'चीन', 'जपान', 'जर्मनी', 'फ्रान्स', 'इटली', 'ब्राझील', 'कॅनडा', 'ऑस्ट्रेलिया', 'रशिया', 'यूके', 'दक्षिण आफ्रिका', 'मेक्सिको', 'स्पेन', 'अर्जेंटिना', 'इजिप्त', 'तुर्की', 'सौदी अरेबिया', 'इंडोनेशिया']
    }
}

# Function to display welcome animation
def welcome_animation():
    messagebox.showinfo("Welcome", "Welcome to Language Learning App")

# Function to display thank you animation
def thank_you_animation():
    messagebox.showinfo("Thank You", "Thank you! Hope you learned something from our app")

# Function to display vocabulary
def display_vocabulary(category, language):
    words = vocabulary[category][language]
    messagebox.showinfo(f"{category.capitalize()} in {language}", "\n".join(words))

# Function to handle submit button
def submit():
    category = category_var.get()
    language = language_var.get()
    display_vocabulary(category, language)

# Create main window
root = tk.Tk()
root.title("Language Learning App")

# Welcome animation
welcome_animation()

# Language selection
language_var = tk.StringVar(value='English')
languages = ['English', 'Hindi', 'Marathi']
for lang in languages:
    tk.Radiobutton(root, text=lang, variable=language_var, value=lang).pack(anchor=tk.W)

# Category selection
category_var = tk.StringVar(value='birds')
categories = ['birds', 'flowers', 'fruits', 'animals', 'countries']
for cat in categories:
    tk.Radiobutton(root, text=cat.capitalize(), variable=category_var, value=cat).pack(anchor=tk.W)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Search bar
search_label = tk.Label(root, text="Search:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()

# Exit button with thank you animation
exit_button = tk.Button(root, text="Exit", command=lambda: [thank_you_animation(), root.quit()])
exit_button.pack()

# Run the application
root.mainloop()
