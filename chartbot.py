import spacy
import random
nlp = spacy.load("en_core_web_sm")

intents = {
    "greeting": [
        "Hi there! How can I help you today?"
    ],
    "goodbye": [
        "Goodbye! Have a great day!"
    ],
    "name": [
        "I'm your friendly assistant Jara."
    ],
    "help": [
        "Of course! I'm here to help Could you please tell me what you need help with? "
    ],
    "weather": [
        "I'm not connected to real-time data, but I hope it's sunny where you are!",
        "Weather updates aren't my specialty... yet."
    ],
    "music": [
        "I love music! Even though I can't hear, I know it's a universal language."
    ],
    "reality": [
        "I'm not human—I'm a virtual assistant built to chat with you."
    ],
    "color": [
        "I like blue  it's calm and intelligent like me"
    ],
    "creator": [
        "I was created by a human developer for the project."
    ],
    "capabilities": [
        "I can answer simple questions, chat casually, and help you learn."
    ],
    "working": [
        "I work using code, logic, and natural language processing — like spaCy!"
    ]
}

def detect_intent(user_message):
    user_message = user_message.lower()
    if any(word in user_message for word in ["hello", "hi", "hey"]):
        return "greeting"
    elif any(word in user_message for word in ["bye", "goodbye", "see you"]):
        return "goodbye"
    elif "your name" in user_message or "who are you" in user_message:
        return "name"
    elif "help" in user_message or "can you do" in user_message:
        return "help"
    elif "weather" in user_message:
        return "weather"
    elif "music" in user_message:
        return "music"
    elif "are you real" in user_message or "are you human" in user_message:
        return "reality"
    elif "color" in user_message:
        return "color"
    elif "who created you" in user_message or "your creator" in user_message:
        return "creator"
    elif "what can you do" in user_message or "abilities" in user_message:
        return "capabilities"
    elif "how do you work" in user_message or "how you work" in user_message:
        return "working"
    else:
        return None
def get_response(intent):
    return random.choice(intents.get(intent, ["Sorry, I didn't understand that."]))
def start_chat():
    print("Jara: Hello! I am your NLP chatbot. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Jara: Goodbye!")
            break
        doc = nlp(user_input)
        intent = detect_intent(user_input)
        reply = get_response(intent)
        print("Jara:", reply)
if __name__ == "__main__":
    start_chat()