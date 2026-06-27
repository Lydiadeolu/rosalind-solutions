# Key decisions: Python's native dictionary provides O(1) average-time complexity 
# for lookups and insertions, making it incredibly fast. While we could use 
# collections.Counter, implementing a standard dictionary loop directly 
# satisfies the problem's goal of teaching core dictionary mechanics.

def count_word_frequencies(text_string):
    word_counts = {}
    words = text_string.strip().split()
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    return word_counts

if __name__ == "__main__":
    try:
        with open("python_village/Datesetrosalind_ini6 (1).txt") as file:
            content = file.read()
            frequencies = count_word_frequencies(content)
            
            for word, count in frequencies.items():
                print(f"{word} {count}")
            
    except FileNotFoundError:
        # Fallback test example from Rosalind description
        sample_str = "We will win we will win"
        frequencies = count_word_frequencies(sample_str)
        for word, count in frequencies.items():
            print(f"{word} {count}")