# Domain Model

## Entities

### User

系统用户,可以拥有课程和任务.

### Course

课程,归属于一个 User.

### Task

课程下的任务,归属于一个 User 和一个 Course.

## Relationships

- User 1 - N Course
- Course 1 - N Task
- User 1 - N Task

## State Machines

### Task Status

- pending
- done

Allowed transitions:

- pending -> done
- done -> pending
