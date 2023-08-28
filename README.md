# Connor Tom Discord Bot

This project contains a Discord bot written in Python that performs various tasks using the Discord API, Azure Blob Storage, and other modules. The bot can be used to manage birthdays, track user activities, and more.

## Table of Contents

- [Getting Started](#getting-started)
- [Features](#features)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with this Discord bot project, follow these steps:

1. Clone the repository to your local machine.
2. Make sure you have Python and the required dependencies installed (see [Dependencies](#dependencies)).
3. Set up the required environment variables (see [Configuration](#configuration)).
4. Run the `main.py` script to start the bot.

## Features

- **Birthday Management:** The bot can help manage birthdays by setting and retrieving birthday information for users.

- **Activity Tracking:** The bot can track user activities and provide relevant information.

- **Azure Blob Storage Integration:** The project integrates with Azure Blob Storage to store and retrieve data.

## Usage

The bot responds to certain commands within Discord channels. Here are some example commands:

- `$test`: Check if the bot is online.
- `$setbirthday`: Set your birthday in the system.
- `$getbirthday`: Get your saved birthday information.
- `$track @user`: Start tracking the activity of a user.

For a full list of available commands and their descriptions, refer to the source code.

## Dependencies

The project relies on the following dependencies:

- `discord`: Discord API library.
- `azure-storage-blob`: Azure Blob Storage client library.
- `dotenv`: Load environment variables from a `.env` file.

To install the required dependencies, you can use the following command:

```bash
pip install discord azure-storage-blob python-dotenv
```

## Configuration

Before running the bot, you need to set up the required environment variables. Create a `.env` file in the project directory and add the following variables:

- `AZURE_BLOB_CONNECTION_STRING`: Azure Blob Storage connection string.
- `AZURE_STORAGE_ACCOUNT_NAME`: Azure Storage account name.
- `DISCORD_TOKEN`: Discord bot token.

Replace the placeholders with your actual values.

## Contributing

Contributions to this project are welcome! If you find any issues or have ideas for improvements, feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize the content based on your project's specifics. Make sure to replace placeholders with actual information and provide any additional details that might be relevant to users who want to use or contribute to your bot project.