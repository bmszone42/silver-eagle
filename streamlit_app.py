# Import necessary libraries
import streamlit as st
import math

# Constants
# Effective exhaust velocity (m/s), typical for chemical rockets
EXHAUST_VELOCITY = 4500  
# Mass of the rocket structure (kg), arbitrary
STRUCTURE_MASS = 50000  

# Function to calculate the range of the rocket
def calculate_range(velocity, payload_mass, fuel_mass):
    # Check if input values are non-negative
    if velocity < 0 or payload_mass < 0 or fuel_mass < 0:
        st.error('Input values must be non-negative.')
        return
    if fuel_mass == 0:
        st.error('Fuel mass must be greater than zero.')
        return
    # Calculate initial and final mass of the rocket
    initial_mass = payload_mass + fuel_mass + STRUCTURE_MASS
    final_mass = payload_mass + STRUCTURE_MASS
    # Try to calculate delta_v using the Tsiolkovsky rocket equation
    try:
        delta_v = EXHAUST_VELOCITY * math.log(initial_mass / final_mass)
    except ValueError:
        st.error('Invalid input values.')
        return
    # Calculate the time and range of the rocket
    time = velocity / delta_v
    range = velocity * time
    return round(range)

# Function to calculate the required fuel mass for a given range
def calculate_fuel(velocity, range, payload_mass):
    # Check if input values are non-negative and velocity is greater than zero
    if velocity <= 0 or range < 0 or payload_mass < 0:
        st.error('Input values must be non-negative and velocity must be greater than zero.')
        return
    # Calculate the time and delta_v
    time = range / velocity
    delta_v = velocity / time
    # Try to calculate the initial mass of the rocket
    try:
        initial_mass = math.exp(delta_v / EXHAUST_VELOCITY) * (payload_mass + STRUCTURE_MASS)
    except OverflowError:
        st.error('The required fuel mass is too large to calculate.')
        return
    # Calculate the required fuel mass
    fuel_mass = initial_mass - payload_mass - STRUCTURE_MASS
    # Check if the calculated fuel mass is non-negative
    if fuel_mass < 0:
        st.error('The specified range is not achievable with the given velocity and payload mass.')
        return
    return round(fuel_mass)

# Set the title of the Streamlit app
st.title('Rocket Range Calculator')

# Display some instructions for the user
st.write('''
Please enter the velocity in meters per second (m/s), the payload mass and fuel mass in kilograms (kg), and the range in meters (m).
Note that this is a simplified model and the actual range or fuel requirements of a rocket could be different due to factors not taken into account in this model, such as air resistance and gravity.
''')

# Let the user choose what to calculate
option = st.selectbox('What do you want to calculate?', ('Range', 'Fuel'))

# Depending on the user's choice, display the appropriate input fields and calculate the result
if option == 'Range':
    velocity = st.number_input('Enter the velocity of the rocket (m/s)', value=2000.0)
    payload_mass = st.number_input('Enter the payload mass (kg)', value=1000.0)
    fuel_mass = st.number_input('Enter the fuel mass (kg)', value=10000.0)
    range = calculate_range(velocity, payload_mass, fuel_mass)
    if range is not None:
        st.write(f'The range of the rocket is {range} meters.')
else:
    velocity = st.number_input('Enter the velocity of the rocket (m/s)', value=2000.0)
    range = st.number_input('Enter the range (m)', value=10000.0)
    payload_mass = st.number_input('Enter the payload mass (kg)', value=1000.0)
    fuel_mass = calculate_fuel(velocity, range, payload_mass)
    if fuel_mass is not None:
        st.write(f'The required fuel mass is {fuel_mass} kg.')
