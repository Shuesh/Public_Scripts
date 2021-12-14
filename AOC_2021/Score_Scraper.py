import requests
from bs4 import BeautifulSoup as bs


def main():
    user_stats = Get_User_Ranks()

    #Get the HTML from the Advent of Code stats page
    page = requests.get('https://adventofcode.com/2021/stats')
    #parse the HTML using BeautifulSoup
    soup = bs(page.content, 'html.parser')

    #Select all of the anchors that 
    stats_both = soup.select("pre a")

    clean_stats = []
    
    for day in stats_both:
        clean_stats.append([int(day.contents[0]),int(day.contents[1].contents[0].strip()),int(day.contents[3].contents[0].strip())])

    for index,day in enumerate(clean_stats):
        percent_two_star = Percent_2_Stars(day[1],day[2])
        clean_stats[index].append(percent_two_star)

    user_stats = Get_User_Ranks()
    pass

def Percent_2_Stars(two_stars, one_star):
    total = two_stars + one_star
    percent_two_stars = float(two_stars) / float(total)
    percentage = round(percent_two_stars * 100, 2)

    return percentage
    

def OAuth():
    github_auth = requests.post('https://github.com/login/device/code')


def Get_User_Ranks():
    user_page = requests.get('https://adventofcode.com/2021/leaderboard/self')
    user_soup = bs(user_page.content, 'html.parser')

    user_stats = user_soup.select("pre text")

    return user_stats


if __name__ == '__main__':
    main()