import requests
from bs4 import BeautifulSoup as bs


def main():
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

    

def Percent_2_Stars(two_stars, one_star):
    total = two_stars + one_star
    percent_two_stars = float(two_stars) / float(total)
    percentage = percent_two_stars * 100

    return percentage
    

def Get_User_Ranks()




if __name__ == '__main__':
    main()