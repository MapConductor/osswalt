from generator.caller import LlmCaller


def main():
    caller = LlmCaller()
    system_prompt = "You are a helpful assistant."
    user_prompt = "What is the capital of Japan?"
    response = caller.call(system_prompt, user_prompt)
    print(response)


if __name__ == "__main__":
    main()
