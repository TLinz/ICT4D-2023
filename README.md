# ICT4D-2023
# EasyVote

EasyVote is a web-based application that allows users to create and manage polls, and receive votes through phone calls using Voxeo's VoiceXML service.

## Features

- User authentication: Users can log in with their credentials.
- Poll management: Users can create, view, and delete polls. Multiple polls can be managed.
- Vote submission via phone calls: Users can call the provided phone number and vote using their phone's keypad.
- Vote results: Users can view the poll results on the web interface, with real-time updates.

## Setup

### Requirements

- Python 3.6 or higher
- Django 3.2 or higher
- SQLite

### Installation

1. Clone the repository:
 git clone https://github.com/yourusername/telephone-voting-app.git
 
2. Install the required packages:

cd voting-app
pip install -r requirements.txt

3. Run the database migrations:

python manage.py migrate

4. Start the development server:

python manage.py runserver


EasyVote should now be accessible at `http://127.0.0.1:8000/`.

### Deployment

To deploy EasyVote on a production server, follow the Django deployment documentation: https://docs.djangoproject.com/en/3.2/howto/deployment/

## Usage

1. Open the application in your web browser and log in using your credentials.
2. Create a new poll by clicking the "Create Poll" button.
3. Share the generated phone number with the voters.
4. Voters can call the provided phone number and vote using their phone's keypad(not yet, because voxeo is currently having some problems with successful dialing).
5. View the real-time poll results by clicking the "View Results" button.
## Not done
1. Not yet deployed on cloud servers
2.Not yet able to count voting data in real time as the voxeo website is out of order and cannot be dialed



