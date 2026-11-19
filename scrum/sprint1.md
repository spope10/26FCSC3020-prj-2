
# Sprint 1: User Registration and Login

## Sprint Goal
Set up the Flask application and implement user registration
and login with basic security and database support.

## Sprint Planning

| Task | Story Points | Status |
|---|---:|---|
| US#1: User Registration | 5 | Completed |
| Login and Logout | 2 | Completed |
| UML Diagrams | 3 | Completed |
| Total | 10 | |

## Individual Scrum Notes

### November 19, 2026

Completed:
- Created the GitHub repository and dev branch.
- Set up the Python virtual environment.
- Installed Flask and required packages.
- Created the Flask application and SQLite database.
- Implemented registration, login, and logout.
- Tested duplicate email validation.
- Prepared UML class, use case, and sequence diagrams.

Challenges:
- Fixed a missing route registration in __init__.py.
- Corrected an indentation error.
- Fixed an import error in forms.py.

Next:
- Review Sprint 1 code and documentation.
- Verify UML diagrams.
- Prepare the Sprint 1 release.

## Sprint Review

The Flask application runs locally. Users can register as
participants or organizers and log in using their email
and password. Passwords are stored as hashes.

Manual tests passed for registration, login, logout,
homepage display, user role display, and duplicate emails.

## Sprint Retrospective

What went well:
I was able to use what I learned from my previous Flask
assignments to build the registration system.

What was challenging:
I had some issues with indentation, imports, and routes.
I fixed them by checking the error messages and reviewing
the code.

What I will improve:
For the next sprint, I will test each feature before
moving to the next one and keep my code organized.
