from langchain_core.prompts import SystemMessagePromptTemplate
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage
from constants import GROQ_MODEL

model = init_chat_model(GROQ_MODEL)

conversation = [
    SystemMessage("You help customers of a small online shop. Order A17 shipped on 3 March. Order C40 is waiting for stock. Answer in one short sentence, using only these facts."),
    HumanMessage("Where is my order A17?"),
]

response = model.invoke(conversation)

conversation.append(response)
conversation.append(HumanMessage("And C40?"))

response = model.invoke(conversation)

conversation.append(response)
conversation.append(HumanMessage("What about order B22?"))

response = model.invoke(conversation)

for message in conversation:
    message.pretty_print()
    print(message.type, end="\n\n")

print(response.text)
