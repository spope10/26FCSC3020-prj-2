
# Sprint Planning

Date/Time: November 20, 2026 (time not recorded)

Participants: Soni Pope (individual project)

Goal Statement:
Implement competition and challenge management for organizers.
Complete User Stories 2, 3, and 4 with input validation,
role-based access control, and manual testing.

# Daily Scrums

## 11/20/2026 - Time not recorded

Participants: Soni Pope

Work Completed:
- Implemented the organizer's competition list (US2).
- Added competition creation with date validation (US3).
- Created the Challenge model and ChallengeForm (US4).
- Implemented challenge creation and organizer ownership checks.
- Added the Add Challenge link to My Competitions.
- Tested challenge creation and database persistence.
- Verified participants cannot create challenges.
- Verified another organizer cannot modify Soni's competition.
- Verified that zero-point challenges are rejected.
- Committed features on separate branches and merged them into dev.

Blockers:
- Encountered a 403 Forbidden error while testing challenge creation.
- Verified the competition ownership and restarted Flask.
- Confirmed the correct organizer could access the form.

# Sprint Review

Date/Time: Not yet recorded

Participants: Soni Pope

Completed User Stories:
- US2: Organizer views their competitions.
- US3: Organizer creates competitions.
- US4: Organizer adds challenges to their competitions.

Testing:
- Verified organizer-only access to competition management.
- Verified competition date validation.
- Verified challenge creation and database persistence.
- Verified participant and organizer ownership restrictions.
- Verified zero-point validation.

Git:
- Feature branches merged into dev.
- Changes pushed to GitHub.
- Main branch not yet updated.

# Sprint Retrospective

Date/Time: Not yet recorded

Participants: Soni Pope

What Went Well:
- Completed the planned competition and challenge features.
- Tested each feature before committing.
- Used separate feature branches to organize development.

What Could Improve:
- Check the active login account before testing protected routes.
- Verify database changes immediately after submitting forms.

Next Steps:
- Review Sprint 2 documentation and UML diagrams.
- Update the Sprint 2 burndown chart.
- Merge dev into main after Sprint 2 is complete.
