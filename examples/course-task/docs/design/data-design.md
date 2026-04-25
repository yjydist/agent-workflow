# Data Design

## users

| Field | Type | Constraint |
|---|---|---|
| id | bigint | primary key |
| email | varchar(255) | unique, not null |
| password_hash | varchar(255) | not null |
| created_at | datetime | not null |
| updated_at | datetime | not null |

## courses

| Field | Type | Constraint |
|---|---|---|
| id | bigint | primary key |
| user_id | bigint | index, not null |
| name | varchar(100) | not null |
| created_at | datetime | not null |
| updated_at | datetime | not null |

## tasks

| Field | Type | Constraint |
|---|---|---|
| id | bigint | primary key |
| user_id | bigint | index, not null |
| course_id | bigint | index, not null |
| title | varchar(100) | not null |
| description | text | nullable |
| status | varchar(20) | pending/done |
| due_time | datetime | nullable |
| created_at | datetime | not null |
| updated_at | datetime | not null |
