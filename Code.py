import tkinter as tk
from tkinter import messagebox

# Expanded Vocabulary Data
vocabulary = {
    'animals': {
        'lion': {'en': 'lion', 'mr': 'सिह', 'hi': 'सिंह'},
        'tiger': {'en': 'tiger', 'mr': 'वाघ', 'hi': 'टाइगर'},
        'elephant': {'en': 'elephant', 'mr': 'हत्ती', 'hi': 'हाथी'},
        'giraffe': {'en': 'giraffe', 'mr': 'जिराफ', 'hi': 'जिराफ'},
        'zebra': {'en': 'zebra', 'mr': 'झेब्रा', 'hi': 'ज़ेब्रा'},
        'bear': {'en': 'bear', 'mr': 'उरुस', 'hi': 'भालू'},
        'wolf': {'en': 'wolf', 'mr': 'गोलू', 'hi': 'भेड़िया'},
        'deer': {'en': 'deer', 'mr': 'हरिण', 'hi': 'हिरण'},
        'rabbit': {'en': 'rabbit', 'mr': 'खरगोष', 'hi': 'खरगोश'},
        'kangaroo': {'en': 'kangaroo', 'mr': 'कांगारू', 'hi': 'कंगारू'},
        'fox': {'en': 'fox', 'mr': 'कोकण', 'hi': 'गीदड़'},
        'panda': {'en': 'panda', 'mr': 'पांडा', 'hi': 'पांडा'},
        'horse': {'en': 'horse', 'mr': 'घोडा', 'hi': 'घोड़ा'},
        'camel': {'en': 'camel', 'mr': 'उंट', 'hi': 'ऊंट'},
        'rhinoceros': {'en': 'rhinoceros', 'mr': 'गेंड', 'hi': 'गैंडा'},
        'hippopotamus': {'en': 'hippopotamus', 'mr': 'हिप्पो', 'hi': 'हिप्पो'},
        'monkey': {'en': 'monkey', 'mr': 'माकड', 'hi': 'बंदर'},
        'gorilla': {'en': 'gorilla', 'mr': 'गोरिला', 'hi': 'गोरिला'},
        'chimpanzee': {'en': 'chimpanzee', 'mr': 'चिंपांझी', 'hi': 'चिंपांजी'},
        'squirrel': {'en': 'squirrel', 'mr': 'गिलहरी', 'hi': 'गिलहरी'},
        'otter': {'en': 'otter', 'mr': 'उदर', 'hi': 'उदर'},
        'beaver': {'en': 'beaver', 'mr': 'बीवर', 'hi': 'बीवर'},
        'platypus': {'en': 'platypus', 'mr': 'प्लाटीपस', 'hi': 'प्लैटिपस'},
        'hedgehog': {'en': 'hedgehog', 'mr': 'हेजगॉग', 'hi': 'हेजहोग'},
        'seal': {'en': 'seal', 'mr': 'सील', 'hi': 'सील'},
        'walrus': {'en': 'walrus', 'mr': 'वालरस', 'hi': 'वालरस'},
        'dolphin': {'en': 'dolphin', 'mr': 'डॉल्फिन', 'hi': 'डॉल्फिन'},
        'shark': {'en': 'shark', 'mr': 'शार्क', 'hi': 'शार्क'},
        'whale': {'en': 'whale', 'mr': 'तुतारी', 'hi': 'व्हेल'},
        'octopus': {'en': 'octopus', 'mr': 'अष्टपदी', 'hi': 'ऑक्टोपस'},
        'jellyfish': {'en': 'jellyfish', 'mr': 'जेलीफिश', 'hi': 'जेलीफिश'},
    },
    'birds': {
        'sparrow': {'en': 'sparrow', 'mr': 'गोड', 'hi': 'गौरैया'},
        'eagle': {'en': 'eagle', 'mr': 'गरुड', 'hi': 'गिद्ध'},
        'parrot': {'en': 'parrot', 'mr': 'टिको', 'hi': 'तोता'},
        'owl': {'en': 'owl', 'mr': 'घुबड', 'hi': 'उल्लू'},
        'peacock': {'en': 'peacock', 'mr': 'मोर', 'hi': 'मोर'},
        'pigeon': {'en': 'pigeon', 'mr': 'पाया', 'hi': 'कबूतर'},
        'hawk': {'en': 'hawk', 'mr': 'हॉक', 'hi': 'बाज'},
        'vulture': {'en': 'vulture', 'mr': 'गिद्ध', 'hi': 'गिद्ध'},
        'swallow': {'en': 'swallow', 'mr': 'स्वालो', 'hi': 'स्वालो'},
        'finch': {'en': 'finch', 'mr': 'फिंच', 'hi': 'फिंच'},
        'robin': {'en': 'robin', 'mr': 'रॉबिन', 'hi': 'रॉबिन'},
        'cardinal': {'en': 'cardinal', 'mr': 'कार्डिनल', 'hi': 'कार्डिनल'},
        'dove': {'en': 'dove', 'mr': 'कबूतर', 'hi': 'कबूतर'},
        'flamingo': {'en': 'flamingo', 'mr': 'फ्लेमिंगो', 'hi': 'फ्लेमिंगो'},
        'penguin': {'en': 'penguin', 'mr': 'पेंग्विन', 'hi': 'पेंग्विन'},
        'ostrich': {'en': 'ostrich', 'mr': 'ऑस्ट्रेलियन', 'hi': 'उल्लू'},
        'albatross': {'en': 'albatross', 'mr': 'अल्बाट्रॉस', 'hi': 'अल्बाट्रॉस'},
        'heron': {'en': 'heron', 'mr': 'हेरॉन', 'hi': 'हेरॉन'},
        'crane': {'en': 'crane', 'mr': 'क्रेन', 'hi': 'क्रेन'},
        'flamingo': {'en': 'flamingo', 'mr': 'फ्लेमिंगो', 'hi': 'फ्लेमिंगो'},
        'kookaburra': {'en': 'kookaburra', 'mr': 'कूकाबुरा', 'hi': 'कूकाबुरा'},
        'woodpecker': {'en': 'woodpecker', 'mr': 'वूडपेकर', 'hi': 'वूडपेकर'},
        'toucan': {'en': 'toucan', 'mr': 'टूकेन', 'hi': 'टूकेन'},
        'puffin': {'en': 'puffin', 'mr': 'पफिन', 'hi': 'पफिन'},
        'kingfisher': {'en': 'kingfisher', 'mr': 'किंगफिशर', 'hi': 'किंगफिशर'},
        'sparrowhawk': {'en': 'sparrowhawk', 'mr': 'स्पैरोहॉक', 'hi': 'स्पैरोहॉक'},
        'cuckoo': {'en': 'cuckoo', 'mr': 'कूकू', 'hi': 'कूकू'},
    },
    'flowers': {
        'rose': {'en': 'rose', 'mr': 'गुलाब', 'hi': 'गुलाब'},
        'tulip': {'en': 'tulip', 'mr': 'ट्यूलिप', 'hi': 'ट्यूलिप'},
        'sunflower': {'en': 'sunflower', 'mr': 'सूरजमुखी', 'hi': 'सूरजमुखी'},
        'lily': {'en': 'lily', 'mr': 'कमल', 'hi': 'लिली'},
        'orchid': {'en': 'orchid', 'mr': 'ऑर्किड', 'hi': 'ऑर्किड'},
        'daisy': {'en': 'daisy', 'mr': 'डेजी', 'hi': 'डेजी'},
        'lily of the valley': {'en': 'lily of the valley', 'mr': 'लिली ऑफ द वैली', 'hi': 'लिली ऑफ द वैली'},
        'peony': {'en': 'peony', 'mr': 'पेनी', 'hi': 'पिओनी'},
        'chrysanthemum': {'en': 'chrysanthemum', 'mr': 'गेंदे', 'hi': 'गेंदे'},
        'marigold': {'en': 'marigold', 'mr': 'झेंडू', 'hi': 'गेंदे'},
        'poppy': {'en': 'poppy', 'mr': 'पॉपपी', 'hi': 'पॉपपी'},
        'dahlia': {'en': 'dahlia', 'mr': 'डालिया', 'hi': 'डालिया'},
        'begonia': {'en': 'begonia', 'mr': 'बिगोनिया', 'hi': 'बिगोनिया'},
        'geranium': {'en': 'geranium', 'mr': 'जेरानियम', 'hi': 'जेरानियम'},
        'hibiscus': {'en': 'hibiscus', 'mr': 'हिबिस्कस', 'hi': 'हिबिस्कस'},
        'jasmine': {'en': 'jasmine', 'mr': 'चमेली', 'hi': 'चमेली'},
        'lilac': {'en': 'lilac', 'mr': 'लीलाक', 'hi': 'लिलक'},
        'snapdragon': {'en': 'snapdragon', 'mr': 'स्नॅपड्रॅगन', 'hi': 'स्नॅपड्रॅगन'},
        'petunia': {'en': 'petunia', 'mr': 'पेटुनिया', 'hi': 'पेटुनिया'},
        'zinnia': {'en': 'zinnia', 'mr': 'झिनिया', 'hi': 'झिनिया'},
        'camellia': {'en': 'camellia', 'mr': 'कैमेलिया', 'hi': 'कैमेलिया'},
        'freesia': {'en': 'freesia', 'mr': 'फ्रीसिया', 'hi': 'फ्रीसिया'},
        'cyclamen': {'en': 'cyclamen', 'mr': 'सायक्लेमेन', 'hi': 'सायक्लेमेन'},
        'dandelion': {'en': 'dandelion', 'mr': 'डँडेलियन', 'hi': 'डँडेलियन'},
        'lotus': {'en': 'lotus', 'mr': 'कमळ', 'hi': 'कमल'},
        'water lily': {'en': 'water lily', 'mr': 'जलकमळ', 'hi': 'जल-लिली'},
        'heather': {'en': 'heather', 'mr': 'हेदर', 'hi': 'हेदर'},
        'lupine': {'en': 'lupine', 'mr': 'लुपाइन', 'hi': 'लुपाइन'},
        'bluebell': {'en': 'bluebell', 'mr': 'ब्लूबेल', 'hi': 'ब्लू बेल'},
        'columbine': {'en': 'columbine', 'mr': 'कोलंबाइन', 'hi': 'कोलंबाइन'},
        'foxglove': {'en': 'foxglove', 'mr': 'फॉक्सग्लोव', 'hi': 'फॉक्सग्लोव'},
    },
    'countries': {
        'afghanistan': {'en': 'Afghanistan', 'mr': 'अफगाणिस्तान', 'hi': 'अफ़गानिस्तान'},
        'albania': {'en': 'Albania', 'mr': 'अल्बानिया', 'hi': 'अल्बानिया'},
        'algeria': {'en': 'Algeria', 'mr': 'अल्जीरिया', 'hi': 'अल्जीरिया'},
        'andorra': {'en': 'Andorra', 'mr': 'अँडोरा', 'hi': 'अंडोरा'},
        'angola': {'en': 'Angola', 'mr': 'अँगोला', 'hi': 'अंगोला'},
        'argentina': {'en': 'Argentina', 'mr': 'अर्जेन्टिना', 'hi': 'अर्जेंटीना'},
        'australia': {'en': 'Australia', 'mr': 'ऑस्ट्रेलिया', 'hi': 'ऑस्ट्रेलिया'},
        'austria': {'en': 'Austria', 'mr': 'ऑस्ट्रिया', 'hi': 'ऑस्ट्रिया'},
        'belgium': {'en': 'Belgium', 'mr': 'बेल्जियम', 'hi': 'बेल्जियम'},
        'brazil': {'en': 'Brazil', 'mr': 'ब्राझील', 'hi': 'ब्राजील'},
        'canada': {'en': 'Canada', 'mr': 'कॅनडा', 'hi': 'कनाडा'},
        'chile': {'en': 'Chile', 'mr': 'चिली', 'hi': 'चिली'},
        'china': {'en': 'China', 'mr': 'चीन', 'hi': 'चीन'},
        'colombia': {'en': 'Colombia', 'mr': 'कोलंबिया', 'hi': 'कोलंबिया'},
        'croatia': {'en': 'Croatia', 'mr': 'क्रोएशिया', 'hi': 'क्रोएशिया'},
        'cuba': {'en': 'Cuba', 'mr': 'क्युबा', 'hi': 'क्यूबा'},
        'cyprus': {'en': 'Cyprus', 'mr': 'साइप्रस', 'hi': 'साइप्रस'},
        'czech republic': {'en': 'Czech Republic', 'mr': 'चेक गणतंत्र', 'hi': 'चेक गणतंत्र'},
        'denmark': {'en': 'Denmark', 'mr': 'डेनमार्क', 'hi': 'डेनमार्क'},
        'egypt': {'en': 'Egypt', 'mr': 'इजिप्त', 'hi': 'मिस्र'},
        'estonia': {'en': 'Estonia', 'mr': 'एस्टोनिया', 'hi': 'एस्टोनिया'},
        'finland': {'en': 'Finland', 'mr': 'फिनलंड', 'hi': 'फिनलैंड'},
        'france': {'en': 'France', 'mr': 'फ्रान्स', 'hi': 'फ्रांस'},
        'germany': {'en': 'Germany', 'mr': 'जर्मनी', 'hi': 'जर्मनी'},
        'greece': {'en': 'Greece', 'mr': 'ग्रीस', 'hi': 'ग्रीस'},
        'hungary': {'en': 'Hungary', 'mr': 'हंगरी', 'hi': 'हंगरी'},
        'iceland': {'en': 'Iceland', 'mr': 'आयलंड', 'hi': 'आइसलैंड'},
        'india': {'en': 'India', 'mr': 'भारत', 'hi': 'भारत'},
        'indonesia': {'en': 'Indonesia', 'mr': 'इंडोनेशिया', 'hi': 'इंडोनेशिया'},
        'iran': {'en': 'Iran', 'mr': 'ईरान', 'hi': 'ईरान'},
        'iraq': {'en': 'Iraq', 'mr': 'इराक', 'hi': 'इराक'},
        'ireland': {'en': 'Ireland', 'mr': 'आयरलंड', 'hi': 'आयरलैंड'},
        'italy': {'en': 'Italy', 'mr': 'इटली', 'hi': 'इटली'},
        'japan': {'en': 'Japan', 'mr': 'जपान', 'hi': 'जापान'},
        'jordan': {'en': 'Jordan', 'mr': 'जॉर्डन', 'hi': 'जॉर्डन'},
        'kenya': {'en': 'Kenya', 'mr': 'केनिया', 'hi': 'केन्या'},
        'latvia': {'en': 'Latvia', 'mr': 'लातविया', 'hi': 'लातविया'},
        'lebanon': {'en': 'Lebanon', 'mr': 'लेबनान', 'hi': 'लेबनान'},
        'lithuania': {'en': 'Lithuania', 'mr': 'लिथुआनिया', 'hi': 'लिथुआनिया'},
        'luxembourg': {'en': 'Luxembourg', 'mr': 'लक्समबर्ग', 'hi': 'लक्ज़मबर्ग'},
        'malaysia': {'en': 'Malaysia', 'mr': 'मलेशिया', 'hi': 'मलेशिया'},
        'mexico': {'en': 'Mexico', 'mr': 'मेक्सिको', 'hi': 'मेक्सिको'},
        'netherlands': {'en': 'Netherlands', 'mr': 'नेदरलँड', 'hi': 'नीदरलैंड'},
        'new zealand': {'en': 'New Zealand', 'mr': 'न्यूझीलंड', 'hi': 'न्यूज़ीलैंड'},
        'nigeria': {'en': 'Nigeria', 'mr': 'नायजेरिया', 'hi': 'नाइजीरिया'},
        'norway': {'en': 'Norway', 'mr': 'नॉर्वे', 'hi': 'नॉर्वे'},
        'pakistan': {'en': 'Pakistan', 'mr': 'पाकिस्तान', 'hi': 'पाकिस्तान'},
        'peru': {'en': 'Peru', 'mr': 'पेरू', 'hi': 'पेरू'},
        'poland': {'en': 'Poland', 'mr': 'पोलेड', 'hi': 'पोलैंड'},
        'portugal': {'en': 'Portugal', 'mr': 'पुर्तगाल', 'hi': 'पुर्तगाल'},
        'romania': {'en': 'Romania', 'mr': 'रोमेनिया', 'hi': 'रोमेनिया'},
        'russia': {'en': 'Russia', 'mr': 'रशिया', 'hi': 'रूस'},
        'saudi arabia': {'en': 'Saudi Arabia', 'mr': 'सऊदी अरेबिया', 'hi': 'सऊदी अरब'},
        'south africa': {'en': 'South Africa', 'mr': 'दक्षिण अफ्रीका', 'hi': 'दक्षिण अफ्रीका'},
        'spain': {'en': 'Spain', 'mr': 'स्पेन', 'hi': 'स्पेन'},
        'sweden': {'en': 'Sweden', 'mr': 'स्वीडन', 'hi': 'स्वीडन'},
        'switzerland': {'en': 'Switzerland', 'mr': 'स्वित्झर्लंड', 'hi': 'स्विट्जरलैंड'},
        'turkey': {'en': 'Turkey', 'mr': 'टर्की', 'hi': 'तुर्की'},
        'ukraine': {'en': 'Ukraine', 'mr': 'युक्रेन', 'hi': 'यूक्रेन'},
        'united kingdom': {'en': 'United Kingdom', 'mr': 'युनायटेड किंगडम', 'hi': 'संयुक्त राज्य'},
        'united states': {'en': 'United States', 'mr': 'संयुक्त राज्य अमेरिका', 'hi': 'संयुक्त राज्य अमेरिका'},
        'venezuela': {'en': 'Venezuela', 'mr': 'वेनेझुएला', 'hi': 'वेनेज़ुएला'},
        'vietnam': {'en': 'Vietnam', 'mr': 'वियतनाम', 'hi': 'वियतनाम'},
    },
    'alphabets': {
        'a': {'en': 'a', 'mr': 'अ', 'hi': 'अ'},
        'b': {'en': 'b', 'mr': 'ब', 'hi': 'ब'},
        'c': {'en': 'c', 'mr': 'क', 'hi': 'क'},
        'd': {'en': 'd', 'mr': 'ड', 'hi': 'ड'},
        'e': {'en': 'e', 'mr': 'ई', 'hi': 'ई'},
        'f': {'en': 'f', 'mr': 'फ', 'hi': 'फ'},
        'g': {'en': 'g', 'mr': 'ग', 'hi': 'ग'},
        'h': {'en': 'h', 'mr': 'ह', 'hi': 'ह'},
        'i': {'en': 'i', 'mr': 'इ', 'hi': 'इ'},
        'j': {'en': 'j', 'mr': 'ज', 'hi': 'ज'},
        'k': {'en': 'k', 'mr': 'क', 'hi': 'क'},
        'l': {'en': 'l', 'mr': 'ल', 'hi': 'ल'},
        'm': {'en': 'm', 'mr': 'म', 'hi': 'म'},
        'n': {'en': 'n', 'mr': 'न', 'hi': 'न'},
        'o': {'en': 'o', 'mr': 'ओ', 'hi': 'ओ'},
        'p': {'en': 'p', 'mr': 'प', 'hi': 'प'},
        'q': {'en': 'q', 'mr': 'क', 'hi': 'क'},
        'r': {'en': 'r', 'mr': 'र', 'hi': 'र'},
        's': {'en': 's', 'mr': 'स', 'hi': 'स'},
        't': {'en': 't', 'mr': 'त', 'hi': 'त'},
        'u': {'en': 'u', 'mr': 'उ', 'hi': 'उ'},
        'v': {'en': 'v', 'mr': 'व', 'hi': 'व'},
        'w': {'en': 'w', 'mr': 'व', 'hi': 'व'},
        'x': {'en': 'x', 'mr': 'क्स', 'hi': 'क्स'},
        'y': {'en': 'y', 'mr': 'य', 'hi': 'य'},
        'z': {'en': 'z', 'mr': 'ज', 'hi': 'ज'},
    }
}

class LanguageLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Language Learning App')

        # Create checkboxes for language selection
        self.language = tk.StringVar(value='en')
        tk.Checkbutton(root, text='English', variable=self.language, onvalue='en').pack()
        tk.Checkbutton(root, text='Marathi', variable=self.language, onvalue='mr').pack()
        tk.Checkbutton(root, text='Hindi', variable=self.language, onvalue='hi').pack()

        # Create entry for user input
        tk.Label(root, text='Enter type (animals, birds, flowers, countries, alphabets):').pack()
        self.entry = tk.Entry(root)
        self.entry.pack()

        # Create button to display vocabulary
        tk.Button(root, text='Get Vocabulary', command=self.get_vocabulary).pack()

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
    root = tk.Tk()
    app = LanguageLearningApp(root)
    root.mainloop()
