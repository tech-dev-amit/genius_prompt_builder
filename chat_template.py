with open("openai.txt", encoding="utf-8") as f:
    instructions = f.read()

def generate_prompt_template(task):
    template = f"""Based on the following instructions, help me write a good prompt TEMPLATE for the following task:

    {task}

    Notably, this prompt TEMPLATE expects that additional information will be provided by the end user of the prompt you are writing. For the piece(s) of information that they are expected to provide, please write the prompt in a format where they can be formatted into as if a Python f-string.

    When you have enough information to create a good prompt, return the prompt in the following format:\n\n```prompt\n\n...\n\n```

    Instructions for a good prompt:

    {instructions}
    """

    template = template.format(task=task, instructions=instructions)
    return template
