# SafeHerAgent

SafeHerAgent is a Python-based personal assistant/automation agent designed to streamline tasks and provide intelligent assistance. It leverages a modular design for easy extension and integration with other Python tools.SafeHer is an AI safety assistant that chats, alerts authorities, shares location, and activates a camera when danger is detected.

## Features

- Python agent framework
- Easy integration with external modules
- Modular structure for scalable development
- Configurable environment via `.env` file
- Logs actions and events for debugging

## Project Structure

safeher_agent/
├── agent.py       # Main agent logic
├── __init__.py    # Package initializer
├── __pycache__/   # Compiled Python files
├── .env           # Configuration file
└── README.md      # Project documentation

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Parvathy-Prakash/SafeHerAgent.git
## Usage

1. Navigate to the project folder:
   ```bash
   cd safeher_agent
2.Make sure you have Python installed (3.8+ recommended) and any dependencies:

pip install -r requirements.txt


(If you don't have a requirements.txt, install any needed packages manually, e.g., pip install python-dotenv)

3.Run the agent:

python agent.py
## Contributing

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, open an issue first to discuss what you would like to change.
## License

This project is licensed under the MIT License.

## Future Plans

- Add AI-based natural language understanding
- Integrate with external APIs for automation
- Expand modular plugin system for easier feature addition
- Provide a GUI for non-technical users

