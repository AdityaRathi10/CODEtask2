from nltk.chat.util import Chat, reflections #install required packges

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name?",
        ["I am a bot created by Aditya rathi. you can call me Avadh!",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you! How about you?",]
    ],
    [
        r"I am fine|I'm good|I'm doing well",
        ["That's great to hear!",]
    ],
    [
        r"how can you help me",
        ["I can help you with any questions you have about data science, machine learning, and artificial intelligence. I can also help you with any coding questions you have.",]
    ],
    [
        r"who created you",
        ["I was created by Aditya Rathi",]
    ],
    [
        r"quit|exit",
        ["Goodbye! Have a great day!",]
    ],
    [
        r"about you|what is your name|tell me about you",
        ["Hey! I am an chatbot created by Adityarathi based on NPL",]
    ],
]

def chatbot():
    print("Hi, I'm a chatbot created by Aditya Rathi. How can I help you?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()