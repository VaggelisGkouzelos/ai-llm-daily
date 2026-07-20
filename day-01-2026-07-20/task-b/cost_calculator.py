"""
Task B — Υπολογιστής κόστους LLM API
Ημέρα 1

Στόχος: δεδομένου ενός prompt και μιας απάντησης, υπολόγισε πόσο κοστίζει
η κλήση σε κάθε μοντέλο — και πόσο θα κόστιζε σε κλίμακα παραγωγής.

Γιατί έχει σημασία: αυτό είναι το πρώτο εργαλείο που φτιάχνει κανείς
όταν στήνει ένα LLM feature. Η διαφορά κόστους ανάμεσα σε μοντέλα
είναι συχνά 15x — και συνήθως το φθηνό αρκεί.
"""

# --- Τιμές μοντέλων ---
# Δολάρια ανά 1.000.000 tokens. Ένα dict μέσα σε dict.
# Το "input" = ό,τι στέλνεις. Το "output" = ό,τι απαντάει το μοντέλο.
# (Οι τιμές αλλάζουν συχνά — τσέκαρέ τες στα docs του κάθε provider.)
MODEL_PRICES = {
    "gpt-4o-mini":     {"input": 0.15,  "output": 0.60},
    "gpt-4o":          {"input": 2.50,  "output": 10.00},
    "claude-sonnet-4": {"input": 3.00,  "output": 15.00},
    "claude-haiku-4":  {"input": 0.80,  "output": 4.00},
}


def estimate_tokens(text):
    """Ίδια συνάρτηση με το Task A — κανόνας του 4."""
    # TODO 1: Αντίγραψε τη λογική από το Task A.
    pass


def calculate_cost(input_tokens, output_tokens, model_name):
    """
    Υπολογίζει το κόστος μίας κλήσης σε δολάρια.

    Φόρμουλα:
        (input_tokens  / 1_000_000) * τιμή_input
      + (output_tokens / 1_000_000) * τιμή_output
    """
    # TODO 2: Πάρε τις τιμές του μοντέλου από το MODEL_PRICES.
    #   prices = MODEL_PRICES[model_name]
    #   Μετά prices["input"] και prices["output"].

    # TODO 3: Εφάρμοσε τη φόρμουλα και κάνε return το σύνολο.
    #   Σημείωση: το 1_000_000 στην Python είναι απλά 1000000 —
    #   οι κάτω παύλες είναι για να διαβάζεται.
    pass


def compare_models(prompt_text, expected_output_tokens):
    """Τυπώνει σύγκριση κόστους για όλα τα μοντέλα."""
    # TODO 4: Υπολόγισε τα input tokens από το prompt_text.

    print("=== Υπολογισμός κόστους ===")
    # TODO 5: Τύπωσε πόσα input και output tokens υποθέτουμε.

    # TODO 6: Κάνε loop σε όλα τα μοντέλα του MODEL_PRICES και για καθένα
    #         τύπωσε: κόστος ανά κλήση και κόστος για 10.000 κλήσεις.
    #
    # Βοήθεια για loop σε dict:
    #   for model_name in MODEL_PRICES:
    #       ...
    #
    # Βοήθεια για μορφοποίηση αριθμών σε f-string:
    #   f"${cost:.6f}"   -> 6 δεκαδικά, π.χ. $0.000338
    #   f"${total:.2f}"  -> 2 δεκαδικά, π.χ. $3.38
    #   f"{name:<16}"    -> στοιχίζει το κείμενο σε 16 χαρακτήρες πλάτος
    pass


# --- Σενάριο δοκιμής ---
# Φαντάσου ένα chatbot υποστήριξης πελατών.
SAMPLE_PROMPT = (
    "You are a customer support assistant for an online electronics store. "
    "Be concise, polite, and always confirm the order number before "
    "discussing order details. If you don't know something, say so.\n\n"
    "Customer: My order arrived damaged. What are my options?"
)

EXPECTED_OUTPUT_TOKENS = 500  # μια τυπική απάντηση μερικών παραγράφων


# TODO 7: Κάλεσε την compare_models() με τα δύο παραπάνω.


# --- BONUS ---
# TODO 8: Βρες ποιο μοντέλο είναι το φθηνότερο και τύπωσε πόσες φορές
#         φθηνότερο είναι από το ακριβότερο.
#         (Απάντηση για να τσεκάρεις: γύρω στο 25x)
