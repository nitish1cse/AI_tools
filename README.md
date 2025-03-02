# Email and Chat Assistant Projects

A collection of AI-powered tools for email summarization and customer support using OpenAI's GPT models.

## Projects Overview

### 1. Email Summarizer
Fetches and summarizes emails from Gmail using OpenAI's GPT model.

**Key Features:**
- Gmail API integration
- Email search and filtering
- Attachment handling
- AI-powered summarization
- Material UI frontend

### 2. Customer Support Chatbot
AI chatbot for customer support using Gradio interface.

**Key Features:**
- Interactive chat interface
- Context-aware responses
- Custom system prompts

## Setup Instructions

### Prerequisites
- Python 3.7+
- Node.js 16+
- pnpm
- OpenAI API key
- Google Cloud Console credentials

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd my_code
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install frontend dependencies:
```bash
cd frontend
pnpm install
```

4. Environment setup:
```bash
# Create .env file
OPENAI_API_KEY=your_openai_api_key
```

### Gmail API Setup

1. Go to Google Cloud Console
2. Create/select project
3. Enable Gmail API
4. Configure OAuth consent screen
5. Create OAuth 2.0 credentials
6. Download and rename credentials to `credentials.json`

## Running the Applications

### Email Summarizer
```bash
python email_summary.py
```

### Customer Support Chatbot
```bash
python customer_support_chatbot.py
```

### Frontend
```bash
cd frontend
pnpm dev
```

## Project Structure
```
my_code/
├── email_summary.py      # Gmail integration and summarization
├── customer_support_chatbot.py  # AI chatbot
├── frontend/            # React frontend
│   ├── src/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
└── README.md
```

## Dependencies

### Python
```text:requirements.txt
openai
google-auth-oauthlib
google-auth-httplib2
google-api-python-client
python-dotenv
gradio
fastapi
uvicorn
```

### Frontend
- React
- Material-UI
- Vite
- pnpm

## License
MIT
