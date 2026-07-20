"""ΛΥΣΗ — Task B. Κοίτα το μόνο αφού παλέψεις 15+ λεπτά."""

MODEL_PRICES = {
    "gpt-4o-mini":     {"input": 0.15,  "output": 0.60},
    "gpt-4o":          {"input": 2.50,  "output": 10.00},
    "claude-sonnet-4": {"input": 3.00,  "output": 15.00},
    "claude-haiku-4":  {"input": 0.80,  "output": 4.00},
}


def estimate_tokens(text):
    return round(len(text) / 4)


def calculate_cost(input_tokens, output_tokens, model_name):
    prices = MODEL_PRICES[model_name]
    input_cost = (input_tokens / 1_000_000) * prices["input"]
    output_cost = (output_tokens / 1_000_000) * prices["output"]
    return input_cost + output_cost


def compare_models(prompt_text, expected_output_tokens):
    input_tokens = estimate_tokens(prompt_text)

    print("=== Υπολογισμός κόστους ===")
    print(f"Prompt: {input_tokens} tokens | Απάντηση: {expected_output_tokens} tokens")
    print()

    for model_name in MODEL_PRICES:
        cost = calculate_cost(input_tokens, expected_output_tokens, model_name)
        monthly = cost * 10_000
        print(f"{model_name:<16} ${cost:.6f} ανά κλήση  |  ${monthly:.2f} για 10.000 κλήσεις")


SAMPLE_PROMPT = (
    "You are a customer support assistant for an online electronics store. "
    "Be concise, polite, and always confirm the order number before "
    "discussing order details. If you don't know something, say so.\n\n"
    "Customer: My order arrived damaged. What are my options?"
)

EXPECTED_OUTPUT_TOKENS = 500

compare_models(SAMPLE_PROMPT, EXPECTED_OUTPUT_TOKENS)


# BONUS
input_tokens = estimate_tokens(SAMPLE_PROMPT)
costs = {}
for model_name in MODEL_PRICES:
    costs[model_name] = calculate_cost(input_tokens, EXPECTED_OUTPUT_TOKENS, model_name)

cheapest = min(costs, key=costs.get)
priciest = max(costs, key=costs.get)
ratio = costs[priciest] / costs[cheapest]

print()
print(f"Φθηνότερο: {cheapest} (${costs[cheapest]:.6f})")
print(f"Ακριβότερο: {priciest} (${costs[priciest]:.6f})")
print(f"Διαφορά: {ratio:.1f}x")
