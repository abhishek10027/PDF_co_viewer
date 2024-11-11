# PDF_co_viewer


A real-time synchronized PDF viewer built with Flask, Socket.IO, and PDF.js. This application allows a presenter or teacher to control the pages of a PDF file remotely, while all connected viewers see the same page in real-time.



## Features

- **Real-Time Synchronization**: When the presenter changes the page, it updates instantly for all connected viewers.
- **Seamless Experience**: Simple and intuitive controls for a smooth viewing experience.
- **Cross-Platform**: Works on any modern web browser.

## Use Case

This co-viewer is ideal for remote presentations, online classrooms, or any scenario where a group needs to follow along with a PDF document in sync with a presenter.

## Project Structure
```plaintext
pdf-co-viewer/
├── app.py                      # Main Flask app and Socket.IO setup
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html              # HTML template for the main viewer page, client-side JavaScript for integrating Socket.IO and PDF.js to handle real-time synchronization
                                # PDF rendering, and custom CSS styles for the viewer interface.
└── README.md                   # Instructions and documentation

```

## Getting Started

### Prerequisites

- Python 3.x
- Node.js (for Socket.IO if you are modifying it, otherwise not required)
- A modern web browser

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abhishek10027/PDF_co_viewer/tree/main.git
   cd pdf-co-viewer
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # For Linux/Mac
   .\venv\Scripts\activate    # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Open the application**:
   - Visit `http://localhost:5000` in your browser.
   - To simulate multiple users, open the link in multiple tabs or different devices.

### Usage

- **Page Navigation**: Use the **Previous** and **Next** buttons to navigate through the PDF. When the presenter changes the page, all connected users see the change in real-time.
- **Real-Time Sync**: Socket.IO is used to synchronize page changes across all clients.

## Technologies Used

- **Flask**: For backend web server and routing.
- **Socket.IO**: For real-time, bi-directional communication.
- **PDF.js**: For rendering PDF files within the browser.
- **HTML/CSS/JavaScript**: For the frontend.


