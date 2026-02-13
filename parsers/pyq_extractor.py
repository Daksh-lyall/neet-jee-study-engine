class PYQExtractor:
    def __init__(self, pdf_text):
        self.pdf_text = pdf_text
        self.questions = []

    def extract_questions(self):
        # Logic to extract specific NEET and JEE previous year questions
        # This is a placeholder for the actual extraction logic.
        lines = self.pdf_text.split('\n')
        for line in lines:
            if self._is_valid_question(line):
                self.questions.append(line)

    def _is_valid_question(self, line):
        # Placeholder for the actual validation logic to identify valid questions.
        return line.strip().startswith('Q')

    def get_questions(self):
        return self.questions
