<img width="1440" height="900" alt="Screenshot 2026-01-27 at 12 05 58 PM" src="https://github.com/user-attachments/assets/ffd94ab1-bc4b-4577-b7ee-bdefa90586c1" />
Commnd : python -m pip install -r requirements.txt

To make this work every time you open a terminal (permanent), follow these steps:

Open your Zsh configuration file:

Bash

nano ~/.zshrc
Scroll to the bottom and paste this line:

Bash

export OPENAI_API_KEY='your_actual_api_key_here'
Save and exit: Press Control + O, then Enter, then Control + X.

Apply the changes:

Bash

source ~/.zshrc

Run the application : python financial_agent.py
<img width="1440" height="900" alt="Screenshot 2026-01-19 at 6 17 43 PM" src="https://github.com/user-attachments/assets/20de41e9-f6e3-4977-b598-312c28ba5d87" />
