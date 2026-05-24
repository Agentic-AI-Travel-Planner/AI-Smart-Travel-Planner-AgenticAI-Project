# 🌍 AutoGen Travel Planner

An intelligent multi-agent system for comprehensive trip planning using AutoGen v0.4 with real-time web search capabilities powered by Tavily.

## ✨ Features

- **🤖 Multi-Agent Collaboration**: Travel Planner and Researcher agents working together
- **🔍 Real-Time Web Search**: Live travel information using Tavily search integration
- **🗺️ Comprehensive Itineraries**: Detailed day-by-day travel plans with current recommendations
- **🏨 Current Travel Data**: Real-time information about hotels, restaurants, and attractions
- **🔄 Round-Robin Team Workflow**: Structured agent collaboration for optimal results

## 🏗️ Architecture

The system consists of two specialized agents:

- **Travel Planner Agent**: Creates detailed itineraries using real-time web search
- **Researcher Agent**: Provides supplementary research and information

These agents collaborate in a Round-Robin team setup to deliver comprehensive travel plans.

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API key
- Tavily API key (for web search)

### Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd TRAVEL_PLANNER
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv travel_env
   source travel_env/bin/activate  # On Windows: travel_env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the root directory:

   ```bash
   # OpenAI Configuration
   OPENAI_API_KEY=your_openai_api_key_here

   # Tavily Search Configuration
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

### Getting API Keys

- **OpenAI API Key**: Get from [OpenAI Platform](https://platform.openai.com/api-keys)
- **Tavily API Key**: Sign up at [Tavily.com](https://tavily.com/) and get your API key

### Running the Application

```bash
python main.py
```

The system will start planning a 5-day trip to Paris (default). You can modify the query in `main.py` to plan different trips.

## 📁 Project Structure

```
TRAVEL_PLANNER/
├── agents/                 # Agent definitions
│   ├── planner.py         # Travel planning agent with web search
│   └── researcher.py      # Research agent for supplementary info
├── config/                # Configuration and settings
│   └── settings.py        # API keys and model configuration
├── models/                # AI model configurations
│   └── openAIModel.py     # OpenAI client setup
├── teams/                 # Team workflow definitions
│   └── travel_team.py     # Round-robin team configuration
├── utils/                 # Utility functions and tools
│   ├── tools.py          # LangChain tools integration (Tavily)
│   └── utils.py          # Helper functions
├── tests/                 # Unit tests
│   └── agents_test.py    # Agent testing
├── main.py               # Application entry point
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🔧 Configuration

### Model Settings (`config/settings.py`)

- **Model**: `gpt-4o-mini` (configurable)
- **Max Turns**: 7 (configurable)
- **Termination**: Automatic based on completion

### Tool Integration (`utils/tools.py`)

- **Tavily Search**: Real-time web search for travel information
- **LangChain Integration**: Seamless tool integration with AutoGen

## 🛠️ Technical Details

### Dependencies

- **autogen-agentchat**: Core AutoGen framework
- **autogen-ext[openai]**: OpenAI integration
- **langchain-tavily**: Tavily search tool
- **autogen-ext[langchain]**: LangChain tools adapter

### Agent Capabilities

- **Travel Planner**:
  - Real-time web search for travel information
  - Itinerary creation and optimization
  - Current pricing and availability data
- **Researcher**:
  - Supplementary research
  - Data validation and enrichment

## 📝 Example Output

The system provides detailed travel itineraries including:

- Day-by-day activity suggestions
- Restaurant and hotel recommendations
- Tourist attraction information
- Practical travel tips
- Booking suggestions with current availability

## 🧪 Testing

Run the test suite:

```bash
python -m pytest tests/
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

### Getting Help

- Check the AutoGen documentation: [AutoGen Docs](https://microsoft.github.io/autogen/)
- Review Tavily API documentation: [Tavily Docs](https://docs.tavily.com/)
