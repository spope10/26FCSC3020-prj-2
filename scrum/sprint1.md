

# Sprint 1: User Registration and Login

**Project:** CTF Competition Platform  
**Course:** CSC3020 Software Engineering Fundamentals  
**Instructor:** Professor Thyago Mota  
**Start Date:** November 10, 2026  
**End Date:** November 19, 2026  
**Duration:** 10 calendar days  
**Team:** Individual project (approved by Professor Mota)

## Sprint Goal

Set up the Flask application and implement user registration
and login with basic security and database support.

## Sprint Planning

| Task | Story Points | Status |
|---|---:|---|
| US1: User Registration | 5 | Completed |
| Login and Logout | 2 | Completed |
| UML Diagrams | 3 | Completed |
| **Total** | **10** | **Completed** |

## Individual Scrum Notes

### November 10, 2026

Started Sprint 1 and reviewed the project requirements.
The main goal was to build the Flask application and
implement user registration and authentication.

### November 19, 2026

**Completed:**
- Created the GitHub repository and dev branch.
- Set up the Python virtual environment.
- Installed Flask and required packages.
- Created the Flask application and SQLite database.
- Implemented registration, login, and logout.
- Added password hashing and duplicate email validation.
- Tested the registration and login features.
- Prepared UML class, use case, and sequence diagrams.
- Committed and pushed Sprint 1 code to the dev branch.

**Challenges:**
- Fixed a missing route registration in `__init__.py`.
- Corrected an indentation error.
- Fixed an import error in `forms.py`.

**Next:**
- Complete the Sprint 1 burndown chart.
- Verify the documentation and UML diagrams.
- Merge dev into main.
- Begin Sprint 2.

## Sprint Review

Sprint 1 focused on building the foundation of the CTF
Competition Platform.

The Flask application runs locally and uses a SQLite
database. Users can register as participants or organizers
and log in using their email and password. Passwords are
stored as hashes instead of plain text.

### Manual Testing Results

| Test | Expected Result | Result |
|---|---|---|
| Open homepage | Homepage displays | Passed |
| Register participant | Account created | Passed |
| Login | User logs in successfully | Passed |
| Display user role | Correct role appears | Passed |
| Register duplicate email | Error message appears | Passed |
| Logout | User logs out successfully | Passed |

All six manual tests passed.

### Sprint Goal Result

The main Sprint 1 goal was achieved. User registration,
login, and logout are working. The UML diagrams are
also prepared.

## Sprint Retrospective

### What Went Well

I was able to use what I learned from my previous Flask
assignments to build the registration system. I became
more comfortable working with Flask, SQLAlchemy, and
user authentication.

### What Was Challenging

I had some issues with indentation, imports, and route
registration. I fixed them by checking the error messages,
reviewing the code, and testing the application again.

### What I Will Improve

For Sprint 2, I will test each feature before moving to
the next one. I will also keep my code organized and use
feature branches for new development.

## Sprint 1 Burndown

**Total Planned Story Points:** 10  
**Completed Story Points:** 10  
**Remaining Story Points:** 0

The burndown chart is maintained in
`scrum/Burndown Chart Template.xlsx`.

Daily completion values will be entered based on actual
progress rather than estimated completion dates.

## Sprint 1 Summary

Sprint 1 established the basic Flask application,
database connection, and user authentication system.

The next sprint will focus on allowing organizers to
create competitions and add challenges.
