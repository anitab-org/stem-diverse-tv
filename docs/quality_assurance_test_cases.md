This document contains some examples of test cases for each feature implemented on the backend. 

**Tools:**

- Test the REST API with Swagger UI provided in the link of the deployed server.

- Test the REST API using Postman (if you feel comfortable with this).
 
**Notes:**

- Outcome *Fail* means the test case has no effect in the database, so no changes are done in the data. An error message should be returned. 

- Outcome *Success* means that the test case was successful and had an effect in the database, so this change/effect should be reflected in the database.

# Access to unrestricted APIs

- This part deals with the possible test cases while accessing Unrestricted APIs.

## Categories 
 
- The only unrestricted APIs are: GET/categories/all,  GET/categories/{id}/sections

### Get all sections

**Service:** GET/categories/all

**Parameters:** None

| Test Case | Outcome |
| --------- | --------- |
| Fetch sections for all existing category ids | Success |
