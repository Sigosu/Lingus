import json
import requests
import pandas as pd
import datetime

class Lingus(object):
    def __init__(self,
                 username:str,
                 userid:str,
                 userpassword:str):

        self.username = username
        self.identifier = userid
        self.password = userpassword
        self.json_raw = None
        self.session_login()

    def return_user(self):
        data = {
            'owner': self.check_owner(),
            'premium': self.get_premium(),
            'username': self.username,
            'name': self.get_fullname(),
            'league': self.get_league(),
            'active': self.get_langauge_string(),
            'a_crowns': self.get_current_crowns(),
            'a_mastered': self.get_current_mastered(),
            'a_code' : self.get_active_lessoncode(),
            'a_level': self.get_active_level(),
            'level_progress': self.get_level_progress(),
            'lessons_c': self.get_num_sessions_completed(),
            'lessons_u': self.get_active_lessons_unlocked(),
            'streak': self.get_streak(),
            'XP_total': self.get_total_xp(),
            'XP_active': self.get_active_xp(),
            'XP_recent': self.get_recent_xp(),
            'lessons_2w': self.get_lessons_last_two_weeks(),
            'lesson_last': self.get_last_lesson(),
            'lesson_up_name': self.get_upcoming_lesson_name(),
            'lesson_up_level': self.get_upcoming_lesson_skill_level(),
            'lingots': self.get_lingots(),
            'crystals': self.get_gems()
        }
        return data

    def session_login(self):
        login_data = {
            'identifier' : self.identifier,
            'password' : self.password
        }
        url = 'https://www.duolingo.com/2017-06-30/login?fields='
        headers = {'content-type': 'application/json'}
        with requests.Session() as s:
            s.post(url, headers = headers, data = json.dumps(login_data))
            user_url = 'https://www.duolingo.com/users/' + self.username
            r = s.get(user_url, headers = headers)
            response = r.status_code
            if response == 200:
                parsed = json.loads(r.content)
                self.json_raw = parsed
                return parsed
            elif response == 401:
                raise Exception("Couldn't authorize, status code: "+ str(response))
            elif response == 404:
                raise Exception("There is no account named " + self.username + ", status code:"+ str(response))

    def get_readable(self):
        json_readable = json.dumps(self.json_raw, indent=4, sort_keys=True)
        return json_readable
    def get_fullname(self):
        return self.json_raw['fullname']
    def get_data(self):
        df = pd.DataFrame(self.json_raw['language_data'])
        df = df.drop(index=['calendar'])
        return df
    def get_active_lessons_unlocked(self):
        language_data = self.get_data()
        lessons_unlocked = language_data.loc['num_skills_learned'][self.get_active_lessoncode()]
        return lessons_unlocked
    def get_upcoming_lesson_name(self):
        language_data = self.get_data()
        next_lesson = language_data.loc['next_lesson'][self.get_active_lessoncode()]
        return next_lesson['skill_title']
    def get_skills(self):
        language_data = self.get_data()
        skills = language_data.loc['skills'][self.get_active_lessoncode()]
        skills = pd.DataFrame(skills)
        pd.set_option('display.max_columns', 50)
        skills = skills.drop(columns=['language_string', 'explanation', 'words', 'description', 'index',
                                      'known_lexemes', 'comment_data', 'path', 'language', 'bonus',
                                      'num_translation_nodes', 'achievements'])
        return skills
    def get_upcoming_lesson_skill_level(self):
        skills = self.get_skills()
        skilllevel = skills.loc[skills['title']==self.get_upcoming_lesson_name()]
        return skilllevel['levels_finished'].item()
    def get_current_crowns(self):
        crowns = self.get_skills()
        crown_count = 0
        for index, row in crowns.iterrows():
            crown_count += row['levels_finished']
        return crown_count
    def get_current_mastered(self):
        crowns = self.get_skills()
        crown_count = 0
        for index, row in crowns.iterrows():
            if row['levels_finished']==row['num_levels']:
                crown_count+=1
        return crown_count
    def check_owner(self):
        status = bool
        try:
            if not self.json_raw['filter_stream']:
                status = True
        except KeyError:
            status = False
        return status
    def get_tracking_properies(self):
        if self.check_owner():
            df = pd.DataFrame(self.json_raw['tracking_properties'])
            df = df.drop_duplicates(subset=['username'])
            pd.set_option('display.max_columns', 20)
            return df
        else:
            raise Exception("You can't access this data as you are not the owner of the inspected account")
    def get_premium(self):
        df = self.get_tracking_properies()
        df = df.iloc[0]["has_item_premium_subscription"]
        return df
    def get_league(self):
        df = self.get_tracking_properies()
        df = df.iloc[0]["leaderboard_league"]
        league_reference = {
            '0': "Bronze",
            '1': "Silver",
            '2': "Gold",
            '3': "Sapphire",
            '4': "Ruby",
            '5': "Emerald",
            '6': "Amethyst",
            '7': "Pearl",
            '8': "Obsidian",
            '9': "Diamond",
        }
        league = league_reference[str(df)]
        return league
    def get_lingots(self):
        df = self.get_tracking_properies()
        df = df.iloc[0]['lingots']
        return df
    def get_gems(self):
        df = self.get_tracking_properies()
        df = df.iloc[0]['gems']
        return df
    def get_num_sessions_completed(self):
        df = self.get_tracking_properies()
        df = df.iloc[0]['num_sessions_completed']
        return df
    def get_languages(self):
        df = pd.DataFrame(self.json_raw['languages'])
        df = df.loc[df['learning'] == True]
        pd.set_option('display.max_columns', 20)
        df = df.reset_index(drop=True)
        return df
    def get_active_languages(self):
        df = self.get_languages()
        active = df.loc[df['current_learning'] == True]
        active = active.reset_index(drop=True)
        return active
    def get_langauge_string(self):
        df = self.get_languages()
        lesson_string = df.iloc[0]['language_string']
        return lesson_string
    def get_active_level(self):
        df = self.get_active_languages()
        df = df.iloc[0]['level']
        return df
    def get_level_progress(self):
        current_xp = self.get_active_xp()
        needed_xp = self.get_active_languages()
        needed_xp = needed_xp.iloc[0]['to_next_level']
        level_xp = current_xp + needed_xp
        level_progress = current_xp/level_xp * 100
        return round(level_progress, 2)
    def get_active_lessoncode(self):
        df = self.get_active_languages()
        df = df.iloc[0]['language']
        return df
    def get_total_xp(self):
        df = self.get_languages()
        total_xp = 0
        for index, row in df.iterrows():
            total_xp += row['points']
        return total_xp
    def get_active_xp(self):
        df = self.get_active_languages()
        active_xp = df.iloc[0]['points']
        return active_xp
    def get_calendar(self):
        pd.set_option('display.max_rows', 100)
        return pd.DataFrame(self.json_raw['calendar'])
    def get_recent_xp(self):
        df = self.get_calendar()
        recent_xp = 0
        for index, row in df.iterrows():
            recent_xp += row['improvement']
        return recent_xp
    def get_last_lesson(self):
        df = self.get_calendar()
        last_event = df.iloc[-1]['datetime']
        last_event_date = datetime.datetime.fromtimestamp(last_event/1000).strftime("%H:%M:%S, %m/%d/%Y")
        return last_event_date
    def get_lessons_last_two_weeks(self):
        df = self.get_calendar()
        last_two_weeks = len(df)
        return last_two_weeks
    def get_streak(self):
        df = self.get_active_languages()
        streak = df.iloc[0]['streak']
        return streak