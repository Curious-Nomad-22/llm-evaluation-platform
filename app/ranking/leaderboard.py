from utils.score_parser import extract_score


def rank_models(df):

    ranked_df = df.copy()

    clarity_scores = []
    completeness_scores = []
    conciseness_scores = []
    final_scores = []

    for _, row in ranked_df.iterrows():

        quality_text = row["Quality Scores"]

        clarity = extract_score(
            quality_text,
            "Clarity"
        )

        completeness = extract_score(
            quality_text,
            "Completeness"
        )

        conciseness = extract_score(
            quality_text,
            "Conciseness"
        )

        final_score = (
            clarity * 3
            + completeness * 4
            + conciseness * 2
            + row["Tokens/Sec"] * 0.05
            - row["Latency"] * 2
        )

        clarity_scores.append(clarity)
        completeness_scores.append(completeness)
        conciseness_scores.append(conciseness)
        final_scores.append(round(final_score, 2))

    ranked_df["Clarity"] = clarity_scores
    ranked_df["Completeness"] = completeness_scores
    ranked_df["Conciseness"] = conciseness_scores
    ranked_df["Final Score"] = final_scores

    ranked_df = ranked_df.sort_values(
        by="Final Score",
        ascending=False
    )

    columns_to_show = [
    "Model",
    "Final Score",
    "Clarity",
    "Completeness",
    "Conciseness",
    "Latency",
    "Tokens/Sec",
    "Total Tokens"
]

    return ranked_df[columns_to_show]