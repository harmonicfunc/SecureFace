# SecureFace Access Control System

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5.1-blue.svg)](https://opencv.org/releases/)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-green.svg)

The SecureFace Access Control System is a small-scale project designed to enhance security and streamline access control in a office environment using facial recognition technology. This system replaces traditional access cards with face detection and recognition to provide a convenient and secure way to grant access to authorized personnel.

![System Demo](demo.gif)

## Features

- **Basic Face Detection:** Utilizes Haar Cascade for detecting faces in real-time.
- **Facial Recognition:** Integrates a lightweight facial recognition model to recognize authorized individuals.
- **User Registration:** Allows for the registration of authorized users through a simple user interface with image capture.
- **Access Logging:** Maintains access logs for monitoring and security purposes.
- **User-Friendly Interface:** Offers an intuitive dashboard for system configuration and monitoring.
- **Testing and Documentation:** Ensures system reliability through rigorous testing and provides comprehensive user and administrator documentation.

## Getting Started

Follow these instructions to set up and run the SecureFace Access Control System on your local machine.

### Prerequisites

- Python 3.x
- OpenCV
- Additional Python packages (requirements.txt)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sanskaromar/secureface.git
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. Access the dashboard by opening your web browser and navigating to `http://localhost:5000`.

## Documentation

For detailed usage instructions, refer to the [User Documentation](docs/user-doc.md) and [Administrator Documentation](docs/admin-doc.md).

## Contributing

We welcome contributions from the community! Please see our [Contribution Guidelines](CONTRIBUTING.md) for more details on how to get involved.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The project makes use of the Haar Cascade and facial recognition technologies.
- We thank the open-source community for their contributions to the libraries and tools used in this project.

---