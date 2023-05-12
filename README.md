# Rocket Range Calculator

This is a Streamlit application that calculates the range of a rocket based on its velocity, payload mass, and fuel mass. It can also calculate the required fuel mass for a given range.

## Installation

1. Clone this repository.
2. Install the required Python packages using pip:

pip install -r requirements.txt


## Usage

To run the application, use the following command:

streamlit run app.py


Then, open your web browser to the address shown in the terminal (usually http://localhost:8501).

## Features

- Calculate the range of a rocket based on its velocity, payload mass, and fuel mass.
- Calculate the required fuel mass for a given range.
- Interactive sliders to adjust the input parameters.
- Error messages for invalid input values.

## Limitations

This application uses a simplified model of rocket motion and does not take into account factors such as air resistance and gravity. Therefore, the actual range or fuel requirements of a rocket could be different from the calculated values.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

Please note that you'll need to create a requirements.txt file that lists the Python packages required to run your application. In this case, it would be:

streamlit
matplotlib

You can create this file in the same directory as your Streamlit application.

