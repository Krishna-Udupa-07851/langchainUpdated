from importlib.metadata import version
from langchain.messages import HumanMessage

message = HumanMessage(content="what does langchain do?")

print(version("langchain"))
print(version("langchain-core"))
print(message)