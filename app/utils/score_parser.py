import re


def extract_score(text, metric):

    pattern = rf"{metric}:\s*(\d+)"

    match = re.search(pattern, text)

    if match:
        return int(match.group(1))

    return 0