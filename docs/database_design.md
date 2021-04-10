---
title: Database Design
slug: /Backend/database_design
---


**VIDEOS TABLE**

|Key   |Type   |
|---|---|
|ID   | unique id  |
|URL   | string  |
|TITLE   |  string |
|PUBLISHED   | int(date)  |
|SOURCE   | string  |
|CHANNEL   | string  |
|DURATION   | int  |
|ARCHIVED   | bool |
|FREE_TO_REUSE   | bool |
|AUTHORISED_TO_REUSE   | bool |


**AUTHOR TABLE**

|Key   |Type   |
|---|---|
|ID   | unique id  |
|NAME   | string  |
|PROFILE_IMAGE | string |

**VIDEO_AUTHOR TABLE**

|Key   |Type   |
|---|---|
|ID   | unique id  |
|VIDEO_ID   | string  |
|AUTHOR_ID   | string  |


**SECTION TABLE**

|Key   |Type   |
|---|---|
|ID   | unique id  |
|TITLE   | string  |

**CATEGORY TABLE**

|Key   |Type   |
|---|---|
|ID   | unique id  |
|TITLE   | string  |

**SECTION_VIDEO TABLE**

|Key   |Type   |
|---|---|
|ID   | unique id  |
|SECTION_ID   | string  |
|VIDEO_ID   | string  |

**CATEGORY_SECTION TABLE**

|Key   |Type   |
|---|---|
|ID   | unique id  |
|CATEGORY_ID   | string  |
|SECTION_ID   | string  |


**USERS TABLE**

|Key   |Type   |
|---|---|
|id | INTEGER | NOT | NULL|
|name | VARCHAR(30)  | 
|username | VARCHAR(30)  | 
|email | VARCHAR(30)  | 
|password_hash | VARCHAR(100)  | 
|registration_date | INT  | 
|terms_and_conditions_checked | BOOLEAN  | 
|access_rights | INT  | 
|is_email_verified | BOOLEAN  | 
|email_verification_date | INT |