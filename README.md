# DemoApp

This demo provides endpoints for interacting with Hugging Face models for chat and text summarization. It uses the Hugging Face API to perform these tasks and is designed to be run locally( was just trying out to familiarize myself with HF and how it works).

## Features

- **Chat Endpoint**: Allows users to interact with a chat model.
- **Summarize Endpoint**: Provides text summarization using a pre-trained model.

## Requirements

- Python 3.8 or higher
- FastAPI
- Hugging Face Hub
- Requests

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi uvicorn huggingface_hub requests
   ```

4. **Set Environment Variables**:
   Make sure you have an Hugging Face API key. Set it in your environment:
   ```bash
   export HF_API_KEY=<your-huggingface-api-key>
   ```

   On Windows:
   ```cmd
   set HF_API_KEY=<your-huggingface-api-key>
   ```

## Running the Application

To start the FastAPI server, run:

```bash
uvicorn main:app --reload
```

Replace `main` with the name of your Python file if it's different.

## Endpoints

- **`POST /chat/`**: Interact with the chat model.
  - **Request Body**: 
    ```json
    {
      "text": "Your message here"
    }
    ```
  - **Response**: 
    ```json
    {
      "response": "Model's response here"
    }
    ```

- **`POST /summarize/`**: Summarize the provided text.
  - **Request Body**:
    ```json
    {
      "text": "Text to be summarized"
    }
    ```
  - **Response**:
    ```json
    {
      "summary": "Summary of the provided text"
    }
    ```

## Notes
- If you encounter any issues, make sure your Hugging Face API key is correct and that you have set it properly in your environment.

---

