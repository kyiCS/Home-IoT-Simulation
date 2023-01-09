# Smart-Home-IoT-Simulation
By Trebor Bearden, Adrian Hilton, Kali Mcintire, Trevin Rodda, and Kelvin Yi.
*************
This web application was created by 5 UAB students as our final Capstone project. In this project, we wanted to creata a web app that simulates an IoT smart home. Our tech stack includes PostgreSQL for the database, Flask for the backend, and plain JS/HTML/CSS for the frontend. 

### Features:
- Randomized historical data generation
- Monthly/Yearly graph displays for power and water usage
- Real-time smart home overview
- Dynamic thermostat with OpenWeatherMap API
- Event simulation (Run Dishwasher, Run Washing Machine, etc.)
- Ability to toggle ON/OFF for devices
- Passcode access

*************

To run this program, download the `src` folder. Download the requirements in the `requirements.txt`, and `flask run` in the terminal.

You will need to insert your own OpenWeatherMap API key in the `home.py` file. You can make a free account on the website and get the key there.

#### Screenshots:
![main](/main.PNG)
![graph](/graph.png)
