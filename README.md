# Calculator

This is a simple web calculator application built with Flask. It allows users to perform basic operations, such as: addition, subtraction, multiplication, and division.
![Calculator](https://raw.githubusercontent.com/Pegoku/Calculator/main/img/image.png)

## Features

- Perform addition, subtraction, multiplication, and division
- Clear the input field
- Display the result of the calculation (what a normal calculator should do)

## Installation

1. Clone this repository: `git clone https://github.com/Pegoku/Calculator.git`
2. Navigate to the project directory: `cd Calculator`
3. Install the required packages: `pip install -r requirements.txt`
4. Run the application: `python start.py`

## Docker

This application can also be run using Docker. Here are the steps to do so:

1. Build the Docker image: `docker build -t calc .`
2. Run the Docker container mounting the folder where the db will be stored: `docker run -p 5000:5000 calc` 

After running these commands, you can access the application at `http://localhost:5000`.

## Usage

Open your web browser and navigate to `http://localhost:5000` to start using the application.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
