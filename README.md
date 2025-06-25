# 🚀 Automation Dashboard

A powerful multi-purpose automation system featuring both GUI and TUI interfaces. This project integrates social media, messaging, cloud services, data science tasks, and more into a single dashboard environment to simplify digital workflows.

> Note: This project was previously named "Menu Project". All files, directories, and references may still reflect the old name. Please consider "Menu Project" and "Automation Dashboard" as the same project for all purposes.

---

## 📂 Directory Structure

```
Automation-Dashboard--main
│   README.md                             # Project overview and instructions
|   requirements.txt                      # List of Python dependencies for Automation Dashboard
│   menu_project_app_GUI.py               # GUI version of the dashboard
│   menu_project_app_TUI.py               # Text UI version
│   module_internet.py                    # Handles internet-related features
│   module_os.py                          # OS-level automation
│   module_remote_os.py                   # Remote OS automation
│   module_sim.py                         # SIM-related automation
│   module_social_media.py                # Social media automation (e.g., WhatsApp, Telegram)
│   Menu Base Project Automation Dashboard(1).mp4  # Demo video
│
├───static
│   ├───audio
│   │   output.mp3                        # Audio output from TTS module
│   │   ...
│   └───css
│       style.css                         # Basic styling for HTML templates
│       ...
│
└───templates                             # HTML templates for various automation tasks
    ├── index.html                        # Main dashboard
    ├── whatsapp.html                     # WhatsApp automation UI
    ├── whatsapp_test_001.html
    ├── docker_launch.html                # Docker container launch form
    ├── email.html                        # Email sending interface
    ├── google_search.html                # Google search automation
    ├── secure_your_laptop.html           # System security tasks
    ├── ...
    # Other templates include:
    # - Various test versions (e.g., *_test_00X.html)
    # - AWS, SMS, Instagram, Telegram, TTS, Phone Call UIs, etc.
```
---
## 🎬 Demo Video

<!-- Add video link or embed code here -->
[Download/Watch Demo Video](https://github.com/Shyam-Kumar-Khatri/Automation-Dashboard-/blob/main/Menu%20Base%20Project%20Automation%20Dashboard(1).mp4)  
<!-- You can upload to YouTube or a hosting platform and link it -->

---

## 🧩 Core Components

### 1. `menu_project_app_GUI.py` – Web-Based Dashboard (Flask GUI)
- Built using Flask with HTML templates.
- Allows users to send messages (WhatsApp, SMS, Email), automate Docker & AWS operations, post to Instagram/Telegram, fetch location, process datasets, and more.
- Uses integrated modules for backend logic like `module_social_media.py`, `module_sim.py`, etc.

### 2. `menu_project_app_TUI.py` – Terminal-Based Menu Interface
- A text-based user interface that accepts simple natural language commands.
- Offers similar functionalities as GUI in a lightweight CLI experience.
- Uses pattern matching to guide execution (e.g., "docker + pull", "whatsapp + send").

---

## 📦 Supporting Modules

| Module                  | Purpose                                                       |
|------------------------|---------------------------------------------------------------|
| `module_social_media.py` | WhatsApp, Email, Instagram, Telegram automation              |
| `module_sim.py`          | Twilio-based SMS and voice calling                           |
| `module_os.py`           | Local automation: webcam access, rainbow text, ASCII art     |
| `module_remote_os.py`    | SSH login & remote file transfer                             |
| `module_internet.py`     | Google Search automation                                     |

---

## 🧬 Project Modules Breakdown

<details>
<summary><strong>menu_project_app_GUI.py</strong></summary>

Main GUI-based application built with Flask.  
Serves as the web interface for interacting with all backend automation modules.

</details>

<details>
<summary><strong>menu_project_app_TUI.py</strong></summary>

Terminal-based user interface that uses pattern-matching commands.  
Provides a simple way to interact with the system via natural language inputs.

</details>

<details>
<summary><strong>module_social_media.py</strong></summary>

Handles all social media automations like:  
- WhatsApp messaging (instant & scheduled)  
- WhatsApp multi-messaging  
- Instagram image uploads  
- Email (instant & scheduled)  
- Telegram integration (if added)  
Technologies used: `pywhatkit`, `pyautogui`, `instagrapi`, `smtplib`, `schedule`, `email`

</details>

<details>
<summary><strong>module_sim.py</strong></summary>

Manages Twilio-based SMS and voice calling functionalities.  
Also includes advanced utilities like message filtering and purpose-based contact management.  
Technologies used: `twilio`, `numpy`

</details>

<details>
<summary><strong>module_os.py</strong></summary>

Handles local system-level automations including:  
- Camera feed access  
- Rainbow text display  
- ASCII-style prints  
Technologies used: `cv2`, `termcolor`, `colorama`

</details>

<details>
<summary><strong>module_remote_os.py</strong></summary>

Supports remote OS automation tasks such as:  
- SSH login to remote servers  
- File transfers via SFTP  
Technologies used: `paramiko`

</details>

<details>
<summary><strong>module_internet.py</strong></summary>

Provides Google Search automation features.  
Technologies used: `googlesearch-python`

</details>

---

## 🛠 Features & Technologies Used

<details>
<summary><strong>💬 WhatsApp Messaging (Instant & Scheduled)</strong></summary>

Send or schedule messages to one or more recipients via WhatsApp.  
Technologies used: `pywhatkit`, `pyautogui`, `keyboard`, `datetime`, `time`

</details>

<details>
<summary><strong>📱 SMS and Voice Call (via Twilio)</strong></summary>

Send SMS or make automated voice calls using Twilio API.  
Technologies used: `twilio`

</details>

<details>
<summary><strong>📧 Email (Instant & Scheduled)</strong></summary>

Send emails instantly or schedule them using SMTP and scheduling libraries.  
Technologies used: `smtplib`, `email`, `schedule`, `time`

</details>

<details>
<summary><strong>📸 Instagram Automation</strong></summary>

Upload photos with captions to Instagram using API.  
Technologies used: `instagrapi`

</details>

<details>
<summary><strong>📨 Telegram Message Automation</strong></summary>

Send automated messages via Telegram using a bot token and chat ID.  
Technologies used: `requests`, `Telegram Bot API`

</details>

<details>
<summary><strong>🔍 Google Search Automation</strong></summary>

Automate Google search queries and fetch results.  
Technologies used: `googlesearch-python`

</details>

<details>
<summary><strong>🐳 Docker Automation</strong></summary>

Pull, run, stop, and remove Docker images and containers through commands.  
Technologies used: `os`, `subprocess`

</details>

<details>
<summary><strong>☁️ AWS Automation</strong></summary>

Manage EC2 instances and S3 buckets (e.g., create, list, terminate).  
Technologies used: `boto3`

</details>

<details>
<summary><strong>🖥️ Remote OS Automation via SSH</strong></summary>

Execute commands and transfer files to remote systems over SSH.  
Technologies used: `paramiko`

</details>

<details>
<summary><strong>🔐 Laptop Security Camera Trigger</strong></summary>

Capture live webcam feed from the system or IP-connected mobile for surveillance purposes.  
Technologies used: `opencv-python`, `cv2`, `IP Webcam Android App (or similar)`
</details>

<details>
<summary><strong>🎥 Live Camera Feed Access</strong></summary>

Access and display real-time video from IP/web camera.  
Technologies used: `opencv-python`

</details>

<details>
<summary><strong>🌈 Colorful Text & ASCII Effects</strong></summary>

Display rainbow-colored terminal text and stylized output.  
Technologies used: `colorama`, `termcolor`

</details>

<details>
<summary><strong>🧠 Machine Learning Operations</strong></summary>

Preprocess data, train and test machine learning models.  
Technologies used: `numpy`, `pandas`, `matplotlib`, `scikit-learn`

</details>

<details>
<summary><strong>🗃️ User Data Tracker</strong></summary>

Collect, manage, and search user info like name, city, college, and life purpose.  
Technologies used: `numpy`

</details>

<details>
<summary><strong>🗣️ Text-to-Speech (Optional)</strong></summary>

Convert written input into spoken audio output.  
Technologies used: `pyttsx3` or `gTTS` (if implemented)

</details>

<details>
<summary><strong>🌐 GUI Interface (Web-Based)</strong></summary>

User-friendly web interface to access all automation features.  
Technologies used: `Flask`, `HTML`, `CSS`, `Bootstrap` , `Javascript`

</details>

<details>
<summary><strong>🖥️ TUI Interface (Terminal-Based)</strong></summary>

Command-line interface using keyword detection and natural language inputs.  
Technologies used: `Python built-in modules`

</details>

---

## 💻 Installation Instructions
To install all dependencies at once, follow these steps:

1. Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```
2. Install all required packages:
```bash
pip install -r requirements.txt
```

---
## 💻 How to Run

### GUI Version:
```bash
python3 menu_project_app_GUI.py
```
Navigate to http://localhost:5000 in your browser.

### TUI Version:
```bash
python3 menu_project_app_GUI.py
```
Follow the command-line prompts.

---
## 🤝 Contribution
Contributions are welcome! Feel free to fork the repo, create issues, or submit pull requests to enhance features or improve UI/UX.

---
## 📬 Contact

For questions, ideas, or feedback, feel free to reach out via email:  
[📧 shyamkk.work@gmail.com](mailto:shyamkk.work@gmail.com)
