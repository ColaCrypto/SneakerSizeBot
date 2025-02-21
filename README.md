# SneakerSizeBot 🤖👟

**SneakerSizeBot** is a Telegram bot designed to help customers check the availability of sneaker sizes. The bot was developed to handle customer requests efficiently and quickly, providing information on available sizes and shoe models.

## Key Features 🚀

- **Size Availability Check**: The bot allows users to select a specific size and view the available sneaker models for that size.
- **Simple Interaction**: Users can interact with the bot using simple and intuitive commands.
- **Request Management**: The bot is designed to handle customer requests automatically, reducing manual workload.

## How to Use the Bot 🤔

1. **Start the Bot**: Type `/start` to launch the bot and view the welcome message.
2. **Check Available Sizes**: Type `/taglie` to display a menu with all available sizes.
3. **Select a Size**: Click on one of the available sizes to view the sneaker models available for that size.
4. **Help**: Type `/aiuto` to get instructions on how to use the bot.

## Available Commands 📜

- `/start`: Starts the bot and displays the welcome message.
- `/taglie`: Shows a menu with all available sizes.
- `/aiuto`: Provides instructions on how to use the bot.
- `/amicistretti`: Special command for close friends.

## Installation and Configuration 🛠️

### Prerequisites

- Python 3.x
- Python Libraries: `python-telegram-bot``

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/SneakerSizeBot.git
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a Constants.py file and insert your Telegram API token:
   ```python
   API_KEY = 'your-api-token'
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

## File Descriptions 📂

- **main.py**: The main script that runs the Telegram bot. It handles commands, user interactions, and displays available sneaker models based on selected sizes.
- **Constants.py**: Contains the Telegram bot API key. This file should not be shared publicly as it contains sensitive information.
- **Responses.py**: Handles predefined responses for user messages. It processes user input and provides appropriate replies.

## Sensitive Data 🔒

The Constants.py file contains the Telegram bot API token, which is sensitive information. Do not share this file publicly. If you want to share the code, make sure to remove or obscure the token.

## Contributions 🤝

If you'd like to contribute to the project, feel free to fork the repository and submit a pull request. All contributions are welcome!

## License 📄

This project is released under the MIT License. See the LICENSE file for more details.
