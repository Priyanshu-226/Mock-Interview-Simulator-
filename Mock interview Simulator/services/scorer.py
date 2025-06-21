def evaluate_intro(text: str, role: str):
    clarity = 8
    relevance = 9 if role.lower() in text.lower() else 6
    confidence = 7
    fluency = 8
    english = 9
    total = clarity + relevance + confidence

    return {
        "scores": {
            "Clarity": clarity,
            "Relevance": relevance,
            "Confidence": confidence,
            "Fluency": fluency,
            "English Proficiency": english,
            "Total": total,
        },
        "feedback": {
            "Strengths": "Good relevance to role.",
            "Improvement": "Work on tone and flow.",
        }
    }