"""ΛΥΣΗ — Task A. Κοίτα το μόνο αφού παλέψεις 15+ λεπτά."""


def count_characters(text):
    return len(text)


def count_words(text):
    return len(text.split())


def estimate_tokens(text):
    return round(len(text) / 4)


def analyze(text):
    print(f"Κείμενο: {text}")
    print(f"  Χαρακτήρες: {count_characters(text)}")
    print(f"  Λέξεις: {count_words(text)}")
    print(f"  Tokens (εκτίμηση): {estimate_tokens(text)}")
    print()


sample_prompts = [
    "Explain what a large language model is.",
    "Summarize the following article in three bullet points.",
    "You are a helpful assistant. Answer only in JSON format.",
]

for p in sample_prompts:
    analyze(p)


# BONUS
longest = sample_prompts[0]
for p in sample_prompts:
    if estimate_tokens(p) > estimate_tokens(longest):
        longest = p

print(f"Μεγαλύτερο prompt ({estimate_tokens(longest)} tokens): {longest}")
