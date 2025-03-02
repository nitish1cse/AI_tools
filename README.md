# Email and Chat Assistant Projects

A collection of AI-powered tools for email summarization and customer support using OpenAI's GPT models.

## Projects Overview

### 1. Email Summarizer (`email_summary.py`)
Fetches and summarizes emails from Gmail using OpenAI's GPT model.

**Key Features:**
- Gmail API integration with OAuth2 authentication
- Email search and filtering by sender, date, or query
- Attachment detection and handling
- Markdown-formatted email summaries
- Error handling and token management

**Usage:**
```python
# Get emails from specific sender
emails = get_emails_from_sender("example@gmail.com", 5)

# Search emails with filters
search_emails(query="important", max_results=10, days=7)

# Get summary of emails
summary = summarise("sender@example.com")
```

### 2. Customer Support Chatbot (`customer_support_chatbot.py`)
AI chatbot for customer support using Gradio interface.

**Key Features:**
- Interactive chat interface with Gradio
- Context-aware responses using GPT-3.5
- Custom system prompts
- Chat history management
- Error handling and retry options

**Usage:**
```python
# Launch the chatbot interface
python customer_support_chatbot.py
```

### 3. Frontend Application (`frontend/`)
React-based frontend using Material-UI for email summarization.

**Components:**
- `App.jsx`: Main application component with Material-UI interface
- `main.jsx`: Application entry point
- `vite.config.js`: Vite configuration with API proxy
- `index.html`: HTML template

**Features:**
- Clean Material Design interface
- Real-time summary generation
- Error handling and loading states
- Responsive layout
- Dark/light theme support

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

## Project Structure
```
my_code/
├── email_summary.py           # Gmail integration and summarization
│   ├── authenticate_gmail()   # Handles OAuth2 authentication
│   ├── get_email_content()   # Retrieves email content
│   ├── search_emails()       # Searches emails with filters
│   └── summarise()          # Generates email summaries
│
├── customer_support_chatbot.py  # AI chatbot
│   ├── chat()               # Main chat function
│   └── system_message       # Chatbot configuration
│
├── frontend/                 # React frontend
│   ├── src/
│   │   ├── App.jsx         # Main UI component
│   │   └── main.jsx        # Entry point
│   ├── package.json        # Dependencies
│   ├── vite.config.js      # Build configuration
│   └── index.html          # HTML template
│
└── README.md                # Project documentation
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
- React 18
- Material-UI 5
- Vite 5
- pnpm

## Development

### Running the Applications

1. Email Summarizer:
```bash
python email_summary.py
```

2. Customer Support Chatbot:
```bash
python customer_support_chatbot.py
```

3. Frontend:
```bash
cd frontend
pnpm dev
```

### API Endpoints
- `/summarize`: POST endpoint for email summarization
- `/health`: GET endpoint for health check

## License
MIT
