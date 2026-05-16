def evaluate_response(client, answer):

    evaluation_prompt = f"""
    Evaluate the following AI response.

    Score from 1-10 for:
    1. Clarity
    2. Completeness
    3. Conciseness

    Return ONLY numbers in this format:

    Clarity: X
    Completeness: X
    Conciseness: X

    Response:
    {answer}
    """

    evaluation = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": evaluation_prompt
            }
        ]
    )

    return evaluation.choices[0].message.content