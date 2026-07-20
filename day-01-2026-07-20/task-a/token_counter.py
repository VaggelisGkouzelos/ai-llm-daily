"""
Task A — Μετρητής tokens
Ημέρα 1

Στόχος: δεδομένου ενός κειμένου, βρες πόσοι χαρακτήρες, πόσες λέξεις
και περίπου πόσα tokens είναι.

Κανόνας του 4: 1 token ~= 4 χαρακτήρες στα αγγλικά.
(Είναι εκτίμηση. Από την Ημέρα 8 θα μετράμε ακριβώς με τη βιβλιοθήκη tiktoken.)

Συμπλήρωσε κάθε # TODO με τη σειρά. Τρέξε το αρχείο μετά από κάθε βήμα.
"""


def count_characters(text):
    """Επιστρέφει πόσους χαρακτήρες έχει το text (μαζί με τα κενά)."""
    # TODO 1: Χρησιμοποίησε τη len() και κάνε return το αποτέλεσμα.
    # Βοήθεια: len("abc") -> 3
    pass


def count_words(text):
    """Επιστρέφει πόσες λέξεις έχει το text."""
    # TODO 2: Σπάσε το text σε λέξεις με .split() και μέτρησέ τες με len().
    # Βοήθεια: "a b c".split() -> ["a", "b", "c"]
    pass


def estimate_tokens(text):
    """Εκτιμά τον αριθμό tokens με τον κανόνα του 4."""
    # TODO 3: Πάρε το μήκος του κειμένου, διαίρεσέ το με 4, στρογγυλοποίησε.
    # Βοήθεια: round(9 / 4) -> 2
    pass


def analyze(text):
    """Τυπώνει μια πλήρη ανάλυση του κειμένου."""
    # TODO 4: Τύπωσε το κείμενο και τα τρία μεγέθη, καλώντας τις συναρτήσεις πάνω.
    # Χρησιμοποίησε f-strings, π.χ.:
    #   print(f"  Χαρακτήρες: {count_characters(text)}")
    pass


# --- Δοκιμαστικά prompts ---
# Αυτά είναι πραγματικά prompts που θα έστελνες σε ένα μοντέλο.
sample_prompts = [
    "Explain what a large language model is.",
    "Summarize the following article in three bullet points.",
    "You are a helpful assistant. Answer only in JSON format.",
]


# TODO 5: Γράψε ένα for-loop που περνάει από κάθε prompt
#         της sample_prompts και καλεί την analyze() για αυτό.
#
# Βοήθεια:
#   for p in sample_prompts:
#       ...


# --- BONUS (αν σου περισσεύει χρόνος) ---
# TODO 6: Βρες ποιο prompt είναι το μεγαλύτερο σε tokens και τύπωσέ το.
#         Ιδέα: κράτα μια μεταβλητή longest και σύγκρινε μέσα στο loop.
