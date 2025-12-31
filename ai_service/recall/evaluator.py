from nlp.text_cleaner import clean_text
from nlp.embedding import embed
from nlp.similarity import cosine_similarity
from recall.concepts import CONCEPT_SYNONYMS
from recall.observer import log_evaluation
from nlp.slang_normalizer import normalize_slang

def detect_answer_type(text: str):
    text = text.lower()
    if any(w in text for w in ["adalah", "ialah", "merupakan"]):
        return "definition"
    return "explanation"


def concept_present(concept: str, student_text: str,
                    semantic_threshold: float = 0.65) -> bool:
    # 1️⃣ Lexical check (exact / substring)
    if concept in student_text:
        return True

    # 2️⃣ Semantic fallback (untuk konsep abstrak)
    score = cosine_similarity(
        embed(concept),
        embed(student_text)
    )
    return score >= semantic_threshold



def evaluate_answer(reference_answer, reference_concepts, student_answer, question_config):
    if not student_answer or len(student_answer.strip()) < 3:
        return {
            "status": "FAIL",
            "final_score": 0.0,
            "feedback": "Jawaban kosong",
            "semantic": 0.0,
            "coverage": 0.0,
            "missing": reference_concepts
        }

    student_type = detect_answer_type(student_answer)
    if question_config.get("intent_required"):
        if student_type != question_config.get("answer_type"):
            return {
                "status": "FAIL",
                "final_score": 0.0,
                "feedback": "Jenis jawaban tidak sesuai",
                "semantic": 0.0,
                "coverage": 0.0,
                "missing": reference_concepts
            }

    ref = clean_text(reference_answer)
    stu = normalize_slang(clean_text(student_answer))

    # 1️⃣ Semantic similarity (global understanding)
    semantic = cosine_similarity(embed(ref), embed(stu))

    # 2️⃣ Concept coverage (semantic-based)
    found, missing = 0, []
    for c in reference_concepts:
        if concept_present(c, stu):
            found += 1
        else:
            missing.append(c)

    coverage = found / len(reference_concepts)

    # 3️⃣ Status determination
    min_cov = question_config.get("min_coverage", 0.3)
    if coverage < min_cov:
        status = "FAIL"
    elif coverage < 1.0:
        status = "PARTIAL"
    else:
        status = "PASS"

    # 4️⃣ Final score
    sw = question_config.get("semantic_weight", 0.6)
    cw = question_config.get("concept_weight", 0.4)
    final_score = round((semantic * sw) + (coverage * cw), 3)

    # 5️⃣ Logging (observer)
    log_evaluation({
        "semantic": round(semantic, 3),
        "coverage": round(coverage, 3),
        "missing": missing,
        "status": status
    })

    return {
        "status": status,
        "final_score": final_score,
        "semantic": round(semantic, 3),
        "coverage": round(coverage, 3),
        "missing": missing
    }
