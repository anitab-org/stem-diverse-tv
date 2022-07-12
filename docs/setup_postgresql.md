---
title: Setup PostgreSQL
slug: /Guidelines/setup_postgresql
---
Install PostgreSQL with the corresponding installer for your OS: https://www.postgresql.org/download/

Log into PostgreSQL with the `psql` client, then run:

```
CREATE USER <USERNAME> WITH PASSWORD <PASSWORD> CREATEDB;
CREATE DATABASE <DB_NAME> WITH OWNER <USERNAME> ENCODING 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
```

After this, set your `.env` file with the same `<USERNAME>`, `<PASSWORD>` and `<DB_NAME>` from the step before:

```
DB_TYPE=postgres
DB_USERNAME=<USERNAME>
DB_PASSWORD=<PASSWORD>
DB_ENDPOINT=localhost
DB_NAME=<DB_NAME>
```