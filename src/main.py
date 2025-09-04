import logging
from generator import DocumentGenerator
from evaluator import DocumentEvaluator
from writer import ContentWriter

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

SAMPLE_CODE_SNIPPET = """
def calculate_sum(a: int, b: int) -> int:
    \"\"\"
    Calculates the sum of two integers.
    \"\"\"
    return a + b
"""

MAX_ATTEMPTS = 3
SCORE_THRESHOLD = 80


def main():
    generator = DocumentGenerator(SAMPLE_CODE_SNIPPET)
    evaluator = DocumentEvaluator()
    writer = ContentWriter()

    feedback = None
    generated_doc = ""

    for attempt in range(MAX_ATTEMPTS):
        logging.info(f"--- Attempt {attempt + 1} of {MAX_ATTEMPTS} ---")

        # 1. Generate document
        logging.info("Generating document...")
        generated_doc = generator.generate(feedback=feedback)
        logging.info(f"Document generated: {generated_doc}")

        # 2. Evaluate document
        logging.info("Evaluating document...")
        score, feedback = evaluator.evaluate(generated_doc)

        if score >= SCORE_THRESHOLD:
            logging.info(f"Score {score} >= {SCORE_THRESHOLD}. Evaluation passed.")
            break
        else:
            logging.warning(f"Score {score} < {SCORE_THRESHOLD}. Retrying with feedback.")
            if attempt == MAX_ATTEMPTS - 1:
                logging.error("Max attempts reached. Failed to generate a satisfactory document.")
                return

    # 3. Write the final document
    logging.info("Writing final document...")
    writer.write(generated_doc, "final_document.md")
    logging.info("Process completed successfully.")


if __name__ == "__main__":
    main()
