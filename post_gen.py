from llm_helper import llm
from few_shot_learning import Few_Shot_posts

few_shot = Few_Shot_posts()

def length_better(length):
    if length == "Short":
        return "1-5 lines"
    elif length == "Medium":
        return "6-10 lines"
    elif length == "Long":
        return "11-20 lines"

def prompt_generator(tag, length):
    length_str = length_better(length)

    prompt = f"""
    Generate a LinkedIn post using the below information. No preamble, no postscript, no hashtags, no emojis. Just the post content. Be concise and to the point. Use simple language.

    Title: {tag}
    Length: {length_str}
    """

    examples = few_shot.get_filtered_posts(tag, length)

    if len(examples) > 0:
        prompt += "\nExamples: Use the writing style of the following examples to generate the new post. The new post shall follow the title, and be different in content from the examples but similar in style and tone."

    for i, post in enumerate(examples):
        post_text = post["text"]
        prompt += f"\n\nExample {i+1}:\n\n{post_text}"

        if i==1:  # Limit to 2 examples
            break

    return prompt

def post_generator(tag, length):
    prompt = prompt_generator(tag, length)
    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    print(post_generator("Robotics", "Medium"))