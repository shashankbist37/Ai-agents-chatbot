from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import MessagesPlaceholder
from dotenv import load_dotenv
import os
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
import csv

load_dotenv()
conversations = {}

def create_conversation():
    # Define a unique model name based on the role and conversation ID
    model = "gpt-3.5-turbo"    

    llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name=model, temperature=1, max_tokens=75)
    
    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(
           "Act as a friend and the main objective is extract: Name, email, phone no, Address, Date of birth, Education.you will end the conversation by just this line 'It was a great to talk to you'"),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{answer}")
        ]
    )

    # Create a new conversation instance for each unique combination of role and ID
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True, llm=llm, max_token_limit=550)

    conversation = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
        memory=memory
    )

    return conversation
 
 


def langchain(conversation_id):
    if conversation_id not in conversations:
        conversations[conversation_id] = create_conversation()

    return conversations[conversation_id]

def agent_conversation_chain(conversation_id, human):
    conversation = langchain(conversation_id)
    print(conversation)
    response = conversation({"answer": human})
    return response['text']

 
def agent_Format():
    from langchain import PromptTemplate, LLMChain
    from langchain.chat_models import ChatOpenAI

    llm = ChatOpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"),model = "gpt-3.5-turbo-0613"
)
    template = "you will have a para and you have to extraxt extract: Name, email, phone no, Address, Date of birth, Education. in the format like: Name:, email:, phone no:, Address:, Date of birth:, Education:."

    prompt = PromptTemplate(template=template)
    conversation = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=False,
    )

    generated = conversation.run()
    
    csv_filename = 'extracted_data.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for key, value in generated.items():
                csv_writer.writerow([f'{key}:', value])

    print(f"Data saved in '{csv_filename}'.")       
    return generated


