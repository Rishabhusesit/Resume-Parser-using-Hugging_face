# import pandas as pd

# def rank_candidates(results):
#     df = pd.DataFrame(results)
#     df["score"] = df["match_score"].astype(float)
#     df = df.sort_values(by="score", ascending=False)
#     return df.to_dict(orient="records")
# pass
import pandas as pd

def rank_candidates(results):
    """
    Ranks candidates based on their match score.

    Args:
        results (list of dict): List of candidates with "match_score".

    Returns:
        list: Sorted candidates in descending order of match score.
    """
    if not results:
        return {"error": "No candidates to rank"}

    df = pd.DataFrame(results)
    df["score"] = df["match_score"].astype(float)
    df = df.sort_values(by="score", ascending=False)

    return df.to_dict(orient="records")
