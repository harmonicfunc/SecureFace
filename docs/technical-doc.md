# SecureFace Access Control System

This technical documentation provides insights into the structure and components of the SecureFace Access Control System, enabling users and developers to understand and contribute to the project effectively.

**Table of Contents**
- [1. Introduction](#1-introduction)
- [2. Project Structure](#2-project-structure)
- [3. System Components](#3-system-components)
  - [3.1. Main Application](#31-main-application-mainpy)
  - [3.2. Security System](#32-security-system-security_systempy)
  - [3.3. Training Model](#33-training-model-train_modelpy)
- [4. Dependencies](#4-dependencies)
- [5. Installation and Setup](#5-installation-and-setup)
- [6. Usage](#6-usage)
- [7. Testing](#7-testing)
  - [7.1 Running Tests](#71-running-tests)
  - [7.2 Writing Tests](#72-writing-tests)
- [8. Contributions](#8-contributions)
- [9. License](#9-license)

## 1. Introduction
The SecureFace Access Control System is designed to enhance security and access control within an office environment using facial recognition technology. This system replaces traditional access cards with face detection and recognition, providing a secure and convenient way to grant access to authorized personnel.

## 2. Project Structure
The project follows a well-organized directory structure for easy navigation and maintenance:

```
SecureFace
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE.md
├── README.md
├── app
│   ├── access_logs.log
│   ├── authorized_persons.csv
│   ├── haar_face.xml
│   ├── label_to_name.csv
│   ├── security_system.py
│   └── trained_models
│       ├── trained_face_model.yml
│       └── trained_face_model_LBPH.xml
├── docs
│   ├── project_description.md
│   └── technical-doc.md
├── main.py
├── predicted_val_data
│   ├── ben_afflek
│   │   ├── 1.jpg
│   │   ├── ...
│   │   └── n.jpg
│   │
│   │   ...
│   │
│   └── [User Name]
│       ├── 1.jpg
│   │   ├── ...
│   │   └── n.jpg
├── requirements.txt
├── tests
│   └── test_security_system.py
├── train_model
│   ├── train_data
│   │   ├── Ben Afflek
│   │   │   ├── 1.jpg
│   │   │   ├── ...
│   │   │   └── n.jpg
│   │   │
│   │   │   ...
│   │   │
│   │   ├── [User Name]
│   │   │   ├── 1.jpg
│   │   │   ├── ...
│   │   │   └── n.jpg
│   │   │
│   │   │   ...
│   │   │
│   │   └── Mindy Kaling
│   │       ├── 1.jpg
│   │   │   ├── ...
│   │   │   └── n.jpg
│   └── train_model.py
└── val_data
    ├── ben_afflek
    │   ├── 1.jpg
    │   ├── ...
    │   └── n.jpg
    │
    │   ...
    │
    └── [User Name]
        ├── 1.jpg
        ├── ...
        └── n.jpg
```

## 3. System Components

### 3.1. Main Application (main.py)
- Entry point of the system.
- Provides a CLI interface for user interactions.
- Allows users to train a new face recognition model, load an existing model, and choose between real-time detection and batch processing options.

### 3.2. Security System (security_system.py)
- Implements face detection and recognition.
- Uses the Haar Cascade classifier for face detection.
- Utilizes a trained facial recognition model for recognizing authorized individuals.
- Logs access attempts in `access_logs.log`.
- Allows customization of the recognition algorithm.

### 3.3. Training Model (train_model.py)
- Trains the facial recognition model.
- Loads training data from the `train_data` directory.
- Supports three recognition algorithms: LBPH, Eigen, and Fisher.
- Saves the trained model in `trained_models` directory.
- Stores label-to-name mapping in `label_to_name.csv`.

## 4. Dependencies
- Python 3.x
- OpenCV
- Additional Python packages specified in `requirements.txt`

## 5. Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/sanskaromar/secureface.git
   ```

2. Navigate to the project directory:
   ```bash
   cd secureface
   ```

3. Create a virtual environment (recommended for isolation):
   ```bash
   # On Windows
   python -m venv venv

   # On macOS and Linux
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   ```bash
   # On Windows
   .\venv\Scripts\activate

   # On macOS and Linux
   source venv/bin/activate
   ```

5. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

By following these steps, you'll create a virtual environment, activate it, and install the necessary dependencies for the SecureFace Access Control System.

## 6. Usage
1. Run the application:
   ```bash
   python main.py
   ```
2. Access the CLI interface to train a model or load an existing one.
3. Choose between real-time detection and batch processing.

## 7. Testing

Testing is an essential part of maintaining the reliability and correctness of the SecureFace Access Control System. We use Python's `unittest` framework to write and run tests.

### 7.1 Running Tests

To run the tests, navigate to the project's root directory and execute the following command:

```bash
python -m unittest discover tests
```

This command will discover and run all the test cases located in the tests directory. Ensure that you have set up the necessary test images and configurations before running the tests.

Alternatively, you can run the tests in `test_security_system.py` using any of the following commands:

```bash
python -m unittest tests/test_security_system.py
python -m unittest tests.test_security_system
```

### 7.2 Writing Tests
We encourage contributions to our test suite to cover various aspects of the system's functionality. If you'd like to contribute tests, please refer to the tests directory for examples of existing test cases.

For more details on writing and contributing tests, see our [Contribution Guidelines](CONTRIBUTING.md).

## 8. Contributions
Contributions to the project are welcome. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute.

## 9. License
This project is licensed under the MIT License. See [LICENSE](LICENSE.md) for details.