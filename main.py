import pyautogui
import pyperclip
import time

from google import genai
from google.genai import types
import myApiKeys # Local file which contains Gemini api key

def is_last_message_from(chat_text, name):
    message = chat_text.strip().split('/2025]')[-1]

    # Check if the sender is the specified name
    if f"{name}:" in message:
        print("Last message is from", name)
        return True
    else:
        print("Last message is NOT from", name)
        return False

# Click the icon
pyautogui.click(878, 1052)
time.sleep(2)

# Continue watching for messages until we exit manually
while True:
    # Drag to select text
    pyautogui.moveTo(681, 246)
    pyautogui.mouseDown()
    pyautogui.moveTo(1831, 920, duration=0.5)
    pyautogui.mouseUp()

    # Copy to clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)

    pyautogui.click(681, 720)

    # Retrieve clipboard contents
    chat_history = pyperclip.paste()

    # Print or use the variable
    print("Copied Text:", chat_history)

    if is_last_message_from(chat_history, "Jio Rk"): # AI will be check and response on message if message is form specific sender only

        client = genai.Client(api_key=myApiKeys.gKey)

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
            system_instruction="You are a real person named Rajesh Kumar. You have to analyze the chat history and respond accordingly as a real response. You can understand both Hindi & English. Response should be short, not too descriptive. Don't include your name or date, time in the response, it looks unrealistic."),
            contents=chat_history
        )
        
        # Printing the AI response
        print(response.text)
        
        # Assigning AI response to a variable
        autoResponse = response.text

        # Copy AI (bot) response
        pyperclip.copy(autoResponse)

        # Click on the input area
        pyautogui.click(833, 974)
        time.sleep(0.3)

        # Paste the autoResponse from the AI (bot)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)

        # Press Enter
        pyautogui.press('enter')