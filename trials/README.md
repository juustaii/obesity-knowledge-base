# Clinical Trials

This folder contains data on active and completed clinical trials related to obesity management.

## Naming Convention

```
[TRIAL_ID]_[BRIEF_NAME].md
```

## Example Files to Add

- NCT04234556_GLP1_Weight_Loss_Trial.md
- NCT03987373_Bariatric_Interventions.md
- NCT04567890_Metabolic_Endpoints.md

## Data Format

For each trial, include:
- Trial ID (NCT number)
- Official title
- Status (Recruiting, Active, Completed)
- Phase
- Enrollment
- Primary outcome
- Secondary outcomes
- Inclusion/exclusion criteria
- Study locations
- Sponsor/Investigator
- Last updated date

## JSON Template

```json
{
  "trial_id": "NCT########",
  "title": "Trial Title",
  "status": "Recruiting",
  "phase": "Phase 3",
  "enrollment": 500,
  "primary_outcome": "Weight loss at 52 weeks",
  "secondary_outcomes": [
    "Metabolic parameters",
    "Quality of life"
  ],
  "keywords": ["obesity", "treatment"]
}
```
