# Telegram Weather Bot

This project is a Telegram bot that provides weather information for various cities. The bot is developed using Python
and the `aiogram` library, and it is packaged in a Docker container for easy deployment.

## Installation

### Requirements

- Python 3.7+
- Docker

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/weather-bot.git
   cd weather-bot

2. Build in Docker image
    ```bash
    docker build -t bot .
3. Run docker-compose
   ```bash
   docker-compose up

## Usage

Find your bot in Telegram using its username.
Send the command /start to initiate interaction with the bot.
Enter the name of a city to get the current weather information.