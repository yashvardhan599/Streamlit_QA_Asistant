# Question Answering Project
This project is designed to provide question answering capabilities using a language model. Follow the steps below to set up and run the project.

## Getting Started

### 1. Create a LangChain API Key
To use the language model, you first need to create an API key from the LangChain platform. Follow the instructions on their website to obtain your API key.

### 2. Set Up Your Virtual Environment
Before running the project, you need to set up a virtual environment. Open your terminal and navigate to the project directory, then run the following command to create and activate the virtual environment:


```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install Dependencies
With the virtual environment activated, install the required dependencies using the requirements.txt file:

pip install -r requirements.txt

The requirements.txt file should include all the necessary packages for this project. Ensure that ollama and streamlit are listed in this file.

4. Run the Language Model

Start the language model with the following command:

ollama run llama2

5. Run the Streamlit Application
To start the Streamlit application, run:
# Run program
streamlit run app.py