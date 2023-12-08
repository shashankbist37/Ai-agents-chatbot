# Chatbot Project

This GitHub repository contains code for a chatbot project aimed at solving a problem through two different approaches. The primary goal is to facilitate a conversational interface using two chatbot agents and also extract relevant information through formatting. Additionally, an attempt was made to implement the Microsoft Autogen architecture, although it remains incomplete due to tight deadlines.

## Approach 1: Dual-Agent Chatbot

The first approach involves employing two chatbot agents for a dynamic conversation. One agent manages the conversation, while the other is responsible for formatting and extracting data. The conversation is initiated through the frontend, where users can input messages. The data is then processed and formatted accordingly.

## Approach 2: Microsoft Autogen Architecture

The second approach explores the use of the Microsoft Autogen architecture. Unfortunately, due to time constraints, the implementation is not fully completed. This architecture was chosen with the expectation that fine-tuning the model would yield more efficient results compared to the current implementation using the ChatGPT 3.5 Turbo base model.

## Model Fine-Tuning

As of now, the project utilizes the ChatGPT 3.5 Turbo base model without fine-tuning. Future work involves fine-tuning the model to enhance its performance and achieve more accurate and context-aware responses.

## Technologies Used

- Python
- Streamlit for frontend interface
- Flask for API to connect frontend with backend
- Microsoft Autogen (Work in Progress)
- Langchian
- LLM (Language Model)
- OpenAI (ChatGPT 3.5 Turbo)

## Getting Started

1. Clone the repository: `git clone https://github.com/yourusername/your-repo.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file in the project root directory.
4. Add your OpenAI API key to the `.env` file: `OPENAI_API_KEY=your-api-key`
5. Run the Streamlit app: `streamlit run demo_Langchain.py`

Note: Additional setup might be required for the Microsoft Autogen architecture, and this feature is a work in progress.

Feel free to explore, contribute, and provide feedback on ways to improve the project.
