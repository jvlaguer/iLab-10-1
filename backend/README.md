# MedVisor Backend

This repository contains the files for the backend code for MedVisor.

---

## Prerequisites:

- Python Version 3.12.4

- `.env` File

Create a `.env` file at the root directory. Populate with following fields:
```
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
AWS_DEFAULT_REGION=""
```
Ask the team for aws credentials and try not to download from s3 unless necessary.

## Running Locally:

To run this project locally, install the needed dependencies by entering the
following command:

```shell
pip install -r requirements.txt
```

To launch the development server, enter the following command.
```shell
# runs the dev server
gunicorn --bind 0.0.0.0:5000 backend.app:app
```

## Tech Stack:

- Uses Python and Flask

## Notes

- `app.py` is where the main app logic resides.
- The  root directory is the iLab-10-1 folder.
