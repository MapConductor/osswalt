from generator import DocumentGenerator

SAMPLE_CODE_SNIPPET = """
def hello_world():
    print("Hello, world!")
"""


def main():
    response = DocumentGenerator(SAMPLE_CODE_SNIPPET).generate()
    print(response)


if __name__ == "__main__":
    main()
