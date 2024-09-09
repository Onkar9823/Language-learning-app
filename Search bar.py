def search_vocabulary(self):
    query = self.search_entry.get().lower()
    results = {word: data for word, data in vocabulary.items() if query in word.lower()}
    # Display results
