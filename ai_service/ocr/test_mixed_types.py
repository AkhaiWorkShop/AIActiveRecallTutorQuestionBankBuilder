import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ocr.ocr_engine import run_ocr
import io
import json

# Simulated OCR result logic by piping through the processor
from ocr.ocr_engine import OCRProcessor

raw_text_sim = """24. Contoh kerja sama yang baik adalah25. Apabila temanmu menyanyikan lagu
dari daerahnya,sikapmu adalah....
a. kerja sama membersihkan kelas
a. tidak senang
b. kerja sama menyontek ketika ulang
b. tidak mendengar
c. senang dan menghormati
d. menutup kuping
B. Jawablah pertanyaan-pertanyaan berikut dengan singkat dan tepat!
1. Sebutkan tiga ciri keberagaman budaya daerah di Indonesia!
2. Di Nanggroe Aceh Darussalam terdapat empat bahasa daerah. Sebutkan!
3. Sebutkan kepanjangan istilah SARA!
4. Sebutkan kalimat sapaan dalam bahasa Gorontalo!
5. Sebutkan kalimat sapaan dalam bahasa Cirebon!
3ahosa dneralrtanam adrtmokanm hss acth3ao.acos.taming s.is4n suaagmoipasarergotongm 1 DMowo."""

# Since we can't easily Mock OCRExtractor.extract_text here, 
# let's just test the QuestionParser and run_ocr logic separately or manually.

from ocr.ocr_engine import QuestionParser

parser = QuestionParser()
results = parser.parse(raw_text_sim)

formatted = []
for q in results:
    opts = {k.upper(): v for k,v in q['options'].items()}
    q_type = "MULTIPLE_CHOICE" if len(opts) >= 2 else "ESSAY"
    formatted.append({
        "question_no": q.get('question_number'),
        "type": q_type,
        "question_text": q.get('question_text'),
        "choices": opts
    })

print(json.dumps(formatted, indent=2))
