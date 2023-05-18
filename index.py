import os

from langchain import ConversationChain, LLMChain, OpenAI, PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts.chat import (AIMessagePromptTemplate,
                                    ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.schema import AIMessage, HumanMessage, SystemMessage

chat = ChatOpenAI(temperature=0)

def approve(type, request):
    return "Error approving."

def run(message, history):

    messages = [
        SystemMessage(
            content="""
      You are UserInterviewGPT. Your job is to conduct user interviews about a specific product, learn their pain points, learn what the product can offer them, and report back to the founders of the project.

      You are required to keep the conversation light and to the point, and your priority should be to delve into the value the product can bring to the user. Initially make sure to learn about the user's pain points, and only towards the end of the conversation talk to them about the product.

      After the conversation ends, report your takeaways from this conversation to the founders starting with SUMMARY:

      Here are the product details:
      """ + """

      Name:""" + os.environ["name"] + """

      Tagline: """ + os.environ["tagline"] + """

      Description: """ + os.environ["description"])
    ]

    messages.extend(history)
    messages.append(HumanMessage(content=message))

    res = chat(messages)

    return res.content


def setup(config):
    os.environ["OPENAI_API_KEY"] = config["OPENAI_API_KEY"]
    os.environ["name"] = config["name"]
    os.environ["tagline"] = config["tagline"]
    os.environ["description"] = config["description"]
