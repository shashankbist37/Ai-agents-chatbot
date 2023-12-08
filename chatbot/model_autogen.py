import autogen
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryMemory
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

conversation= {}

config_list = [
    {
        "model": "gpt-3.5-turbo" ,
        "api_key": "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",
    }
]

llm_config_proxy = {
    "seed": 42,  # change the seed for different trials
    "temperature": 0,
    "config_list": config_list,
    "request_timeout": 600
}

def conversation_start():
        # Define a unique model name based on the role and conversation ID
    model = "gpt-3.5-turbo"    

    llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name=model, temperature=1, max_tokens=75)

        # Create a new conversation instance for each unique combination of role and ID
    memory = ConversationSummaryMemory(memory_key="chat_history", return_messages=True, llm=llm, max_token_limit=550)

    conversation = LLMChain(
            llm=llm,
            memory=memory
        )
    return conversation

def Conversation(responce):
  response_ai = conversation({"question": responce})
  return response_ai["answer"]


def multiagent(responce):
    print(responce)
    llm_config_assistant = {
        "temperature": 0,
            "functions": [
            {
                "name": "Conversation",
                "description": "There is conversation between ai and user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "question": {
                            "type": "string",
                            "description": "The answer is given by the user",
                        }
                    },
                    "required": ["responce"],
                },
                
            }
        ],
        "config_list": config_list,
        "timeout": 120,
    }



    Convo = autogen.AssistantAgent(
        name="Convo",
        llm_config=llm_config_assistant,
        system_message="You will Talk with the user and convincing to give details. these are the details to extract Name, email, phone no, Address, Date of birth, Education.",
    )
    Verifier = autogen.AssistantAgent(
        name="Verifier",
        llm_config=llm_config_assistant,
        system_message="You will verify the these details Name, email, phone no, Address, Date of birth, Education. by asking some relevant question"
    )
    formater = autogen.AssistantAgent(
        name="formater",
        llm_config=llm_config_assistant,
        system_message="after getting all the details you will get these details Name, email, phone no, Address, Date of birth, Education. and format the data and store it "
    )
    user_proxy = autogen.UserProxyAgent(
        name="user_proxy",
        human_input_mode="Never",
        max_consecutive_auto_reply=0,
        llm_config=llm_config_assistant,
   )

    groupchat = autogen.GroupChat(agents=[user_proxy, Convo, Verifier,formater], messages=[], max_round=12)
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config_assistant)



    responce_ai=user_proxy.initiate_chat(
        manager,
        message=responce
    )
    print(responce_ai)

    return responce_ai