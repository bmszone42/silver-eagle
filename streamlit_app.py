import streamlit as st
import math

# Constants
EXHAUST_VELOCITY = 4500  # m/s, typical for chemical rockets
STRUCTURE_MASS = 50000  # kg, arbitrary

def calculate_range(velocity, payload_mass, fuel_mass):
    if velocity < 0 or payload_mass < 0 or fuel_mass < 0:
        st.error('Input values must be non-negative.')
        return
    initial_mass = payload_mass + fuel_mass + STRUCTURE_MASS
    final_mass = payload_mass + STRUCTURE_MASS
    try:
        delta_v = EXHAUST_VELOCITY * math.log(initial_mass / final_mass)
    except ValueError:
        st.error('Invalid input values.')
        return
    time = velocity / delta_v
    range = velocity * time
    return range

def calculate_fuel(velocity, range, payload_mass):
    if velocity <= 0 or range < 0 or payload_mass < 0:
        st.error('Input values must be non-negative and velocity must be greater than zero.')
        return
    time = range / velocity
    delta_v = velocity / time
    try:
        initial_mass = math.exp(delta_v / EXHAUST_VELOCITY) * (payload_mass + STRUCTURE_MASS)
    except OverflowError:
        st.error('The required fuel mass is too large to calculate.')
        return
    fuel_mass = initial_mass - payload_mass - STRUCTURE_MASS
    if fuel_mass < 0:
        st.error('The specified range is not achievable with the given velocity and payload mass.')
        return
    return fuel_mass

st.title('Rocket Range Calculator')

st.write('''
Please enter the velocity in meters per second (m/s), the payload mass and fuel mass in kilograms (kg), and the range in meters (m).
Note that this is a simplified model and the actual range or fuel requirements of a rocket could be different due to factors not taken into account in this model, such as air resistance and gravity.
''')

option = st.selectbox('What do you want to calculate?', ('Range', 'Fuel'))

if option == 'Range':
    velocity = st.number_input('Enter the velocity of the rocket (m/s)', value=0.0)
    payload_mass = st.number_input('Enter the payload mass (kg)', value=0.0)
    fuel_mass = st.number_input('Enter the fuel mass (kg)', value=0.0)
    range = calculate_range(velocity, payload_mass, fuel_mass)
    if range is not None:
        st.write(f'The range of the rocket is {range} meters.')
else:
    velocity = st.number_input('Enter the velocity of the rocket (m/s)', value=0.0)
    range = st.number_input('Enter the range (m)', value=0.0)
    payload_mass = st.number_input('Enter the payload mass (kg)', value=0.0)
    fuel_mass = calculate_fuel(velocity, range, payload_mass)
    if fuel_mass is not None:
        st.write(f'The required fuel mass is {fuel_mass} kg.')
