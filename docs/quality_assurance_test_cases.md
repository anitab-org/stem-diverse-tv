This document contains some examples of test cases for each feature implemented on the backend.

## Categories

### Get sections related to a category

**Service:** GET /categories/{id}/sections

| Test Case       | Outcome |
| ------------- | ------------- |
| Fetch sections for an existing category id | Success |
| Fetch sections for a non-existing category id | Fail |