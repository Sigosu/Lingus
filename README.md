# Deprecated and discontinued

## Lingus

## [PyPI](https://pypi.org/project/Lingus/0.0.1/)

Lingus is an unofficial Duolingo API that can allow users to view data that isn't necesairly accesible from the profile page.<br/>
It consists of two types of functions: [owner dependent](#owner-dependent-functions) and [owner independent](#owner-independent-functions) . Owner depented functions show data that can only be viewed if the inspected user is the one that has signed in, while the other ones show data accesible to everyone, regardless of authorization. 

## Instalation
```
$ pip install Lingus
```

## Function overwiew

#### Creating a user

```
#import Lingus
user = lingus.Lingus("SampleUsername", "SampleEmail@email.com", "samplepassword123")
```
The first value ("SampleUsername") specifies what account will be inspected. It does not have to be the account that belongs to the signed-in user, but that will only allow you to use [owner independent functions](#owner-independent-functions).

### Owner dependent functions:

- [return_user](#return_user)
- [get_tracking_properties](#get_tracking_properties)
- [get_premium](#get_premium)
- [get_league](#get_league)
- [get_lingots](#get_lingots)
- [get_gems](#get_gems)
- [get_num_sessions_completed](#get_num_sessions_completed)

#### return_user

Returns a dictionary containing various information on the user
```
# Example use
lingus  = duolingo.Duolingo('samplename', '...')
print(lingo.get_user_info())
# Sample Response
{
            'owner': True
            'premium': False
            'username': "Anonero"
            'name': "Anon"
            'league': "Diamond"
            'active': "Russian"
            'a_crowns': 25
            'a_mastered': 6
            'a_code' : Ru
            'a_level': 18
            'level_progress': 75.00 
            'lessons_c': 300
            'lessons_u': 13
            'streak': 56
            'XP_total': 13454
            'XP_active': 12354
            'XP_recent': 4325
            'lessons_2w': 95
            'lesson_last': "21:39:28, 01/17/2022" 
            'lesson_up_name': "Genitive Case - 1"
            'lesson_up_level': 1
            'lingots': 346
            'crystals': 2634
}
```
#### get_tracking_properties
Returns a Pandas DataFrame with a bunch of data about the user, such as some of the data in [return_user](#return_user).

#### get_premium
Returns a boolean of whether the user owns Duolingo Plus or not.

#### get_league
Returns a string with the name of the League the user is currently in.

#### get_lingots
Returns an int with the amount of lingots the user owns.

#### get_gems
Returns an int with the amount of gems the user owns.

#### get_num_sessions_completed
Returns an int with the amount of lessons the user has completed

### Owner independent functions
- [session_login](#session_login)
- [get_readable](#get_readable)
- [get_fullname](#get_fullname)
- [get_data](#get_data)
- [get_active_lessons_unlocked](#get_active_lessons_unlocked)
- [get_upcoming_lesson_name](#get_upcoming_lesson_name)
- [get_skills](#get_skills)
- [get_upcoming_lesson_skill_level](#get_upcoming_lesson_skill_level)
- [get_current_crowns](#get_current_crowns)
- [get_current_mastered](#get_current_mastered)
- [_get_languages](#_get_languages)
- [get_active_languages](#get_active_languages)
- [get_langauge_string](#get_langauge_string)
- [get_active_level](#get_active_level)
- [get_level_progress](#get_level_progress)
- [get_active_lessoncode](#get_active_lessoncode)
- [get_total_xp](#get_total_xp)
- [get_active_xp](#get_active_xp)
- [get_calendar](#get_calendar)
- [get_recent_xp](#get_recent_xp)
- [get_last_lesson](#get_last_lesson)
- [get_lessons_last_two_weeks](#get_lessons_last_two_weeks)
- [get_streak](#get_streak)

#### session_login
Returns an unformatted dictonary containing all of the data avaliable about the user.

#### get_readable
Returns json formatted into a readable string with all of the data on the user.

#### get_fullname
Returns a string with the users account name (not to be confused with username).

#### get_data
Returns a Pandas DataFrame with a bunch of owner-independent data about the user, such as some of the data in [return_user](#return_user).

#### get_active_lessons_unlocked
Returns an int with the amount of lessons the user has unlocked in his active language

#### get_upcoming_lesson_name
Returns a string with the name of the lessons that is considered the users 'next' by Duolingo

#### get_upcoming_lesson_skill_level
Returns an int with the level of the lesson hinted in [get_upcoming_lesson_name](#get_upcoming_lesson_name)

#### get_skills
Returns a Pandas DataFrame with a bunch of owner-independent data about the users skills, such as some of the data in return_user.

#### get_current_crowns
Returns an int with the amount of crowns the user has unlocked.

#### get_current_mastered
Returns an int with the amount of legendary crowns the user has unlocked.

#### _get_languages
Returns a Pandas DataFrame with data about all languages avaliable on the platform, regardless of whether the user is studying them or not.

#### get_active_languages
Returns a Pandas DataFrame like [_get_languages](#_get_languages) only with data about languages the user is studying.

#### get_langauge_string
Returns a string of the language that the user has set as "active".

#### get_active_level
Returns an int with the level of the language the user has set as active.

#### get_level_progress
Returns a float with the percentage towards the next [level](#get_active_level).

#### get_active_lessoncode
Returns a 2-letter string containing the lessoncode of the language the user has set as active.

#### get_total_xp
Returns an int with the total amount of xp sumed up from all of the languages the user has studied.

#### get_active_xp
Returns an int with the amount of XP in users active language.

#### get_calendar
Returns a Pandas DataFrame with a bunch of data about the users lessons from tha past two weeks.

#### get_recent_xp
Returns an int with the XP the user has gained over the past two weeks.

#### get_last_lesson
Returns a string with the date and time of users last lesson but only if it was within the last two weeks.

#### get_lessons_last_two_weeks
Returns an int with the amount of lessons the user has completed in the last two weeks.

#### get_streak
Returns an int with the users current streak.
