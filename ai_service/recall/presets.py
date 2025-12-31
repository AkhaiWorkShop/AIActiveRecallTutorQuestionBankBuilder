PRESET_LATIHAN = {
    "answer_type": "definition",
    "intent_required": False,
    "semantic_weight": 0.5,
    "concept_weight": 0.5,
    "min_coverage": 0.25
}

PRESET_UJIAN = {
    "answer_type": "definition",
    "intent_required": True,
    "semantic_weight": 0.4,
    "concept_weight": 0.6,
    "min_coverage": 0.5
}

PRESETS = {
    "LATIHAN": PRESET_LATIHAN,
    "UJIAN": PRESET_UJIAN
}
