# How to obtain a refresh token
1. Obtain a `code` at https://pms.rentalready.io/o/authorize/?response_type=code&client_id=CLIENT_ID&redirect_uri=REDIRECT_URI, substituting your own client_id and redirect_uri. This code is valid for 1 minute.
2. Obtain the refresh token using the code from step 1. cURL example:
```bash
curl --location 'https://pms.rentalready.io/o/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=rhzC0DCM9GGWaxsP9o2saW4TTeify0N8ubtOMfSc' \
--data-urlencode 'client_secret=K1PjsXjAblwr9ZjHyIlIHwvVleajACNfTwv4glSs4yzvwAv7HEmsQIuEFGEY4w8lbc8LG5MT6WFPhYIremWkfbxY1ppvPkossTkjB4ARHG18diq3l7YzvFx1PG1iscKm' \
--data-urlencode 'code=ghfKquIP5fTyd8aRfRgDGiVbV9HW9R' \
--data-urlencode 'grant_type=authorization_code' \
--data-urlencode 'redirect_uri=https://pms.rentalready.io/api/swagger-oauth2-redirect'
```
