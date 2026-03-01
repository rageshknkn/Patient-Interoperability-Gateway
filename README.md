# Patient-Interoperability-Gateway
 a Django service that ingests standard healthcare data (FHIR), sanitizes it for HIPAA compliance, and exposes it securely to downstream services

 ⚙️ Installation & Setup
Follow these steps to set up the project locally.

1. Environment Configuration
Create a dedicated virtual environment named env and activate it to manage dependencies:

Windows:

Bash
python -m venv env
env\Scripts\activate
macOS/Linux:

Bash
python3 -m venv env
source env/bin/activate
2. Install Required Packages
Install the core framework and security-related libraries:

Bash
pip install django pillow djangorestframework djangorestframework-simplejwt django-cryptography
3. Database Initialization
Run the migration commands to set up your database tables and handle the unique resourceId logic:

Bash
python manage.py makemigrations
python manage.py migrate
📡 API Endpoints
The API is versioned and accessible at: http://127.0.0.1:8000/api/v1/

1. Patient Intake (Create)
Endpoint: POST /api/v1/patient-intake/

Description: Registers a new patient record.

Note: The resourceId must be unique.

Request Body Example:

JSON
{
    "resourceType": "Patient",
    "resourceId": "100-200",
    "passportNumber": "4GFG4568899",
    "name": [{
        "use": "official",
        "family": "Chalmers",
        "given": ["Peter", "James"]
    }],
    "gender": "male",
    "birthDate": "1980-12-25",
    "identifier": [{
        "system": "http://hl7.org/fhir/sid/us-ssn",
        "value": "000-12-3456"
    }],
    "telecom": [{
        "system": "phone",
        "value": "(555) 555-5555",
        "use": "home"
    }],
    "active": true
}
2. Get Patient by ID
Endpoint: GET /api/v1/patients/<resourceId>/

Description: Retrieves a specific patient profile using their unique Resource ID.

Example: http://127.0.0.1:8000/api/v1/patients/100-200/

🛠 Running the Server
Launch the development server with the following command:

Bash
python manage.py runserver
