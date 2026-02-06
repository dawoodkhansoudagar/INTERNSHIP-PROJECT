import webbrowser

def do_action(command):
    command = command.lower().strip()

    if "chatgpt" in command or "chat GPT" in command or "chat gpt" in command:
        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT"

    # Check if user said "open something"
    if command.startswith("open "):
        site_name = command.replace("open ", "").strip()

        # If user already said .com keep it, otherwise add .com
        if not site_name.startswith("http"):
            url = f"https://www.{site_name}.com"
        else:
            url = site_name

        try:
            webbrowser.open(url)
            return f"Opening {site_name}"
        except:
            return "Sorry, I couldn't open that website."

    return None
