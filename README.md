# LLM Engineering Projects

This repository contains various LLM (Large Language Model) based applications using OpenAI's GPT models and other tools.

## Projects

### 1. Email Summary
A Gmail integration tool that fetches and summarizes emails using OpenAI's GPT model.

**Features:**
- Gmail API integration
- Email search and filtering
- Attachment handling
- OpenAI-powered email summarization
- React-based UI with Material Design

**Setup:**
1. Configure Gmail API:
   - Create project in Google Cloud Console
   - Enable Gmail API
   - Set up OAuth consent screen
   - Create credentials
   - Download `credentials.json`

2. Set up environment:
   ```bash
   pip install openai google-auth-oauthlib google-auth-httplib2 google-api-python-client python-dotenv
   ```

3. Create `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

### 2. Customer Support Chatbot
An AI-powered customer support chatbot using OpenAI's GPT model and Gradio interface.

**Features:**
- Interactive chat interface
- Context-aware responses
- Custom system prompts
- Example questions

**Setup:**
