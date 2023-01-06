import requests
import clipboard
import os
import platform
from bs4 import BeautifulSoup

def main():
    while True:
        print("--- Brit/pol/ Paste Generator ---")
        print("1. Sites")
        print("2. Extras")
        print("3. Print Out Paste")
        print("4. Quit")

        selection = input("Enter a selection (1-4): ")

        if selection == "1":
            clear_screen()
            submenu()
        elif selection == "2":
            clear_screen()
            extrasubmenu()
        elif selection == "3":
            clear_screen()
            size_check(articles, arti_wlinks)
        elif selection == "4":
            exit(0)
        else:
            print("Please Enter a Valid Input")


def submenu():
    while True:
        print("--- Brit/pol/ Paste Generator - Sites ---")
        print("1. BBC News")
        print("2. The Guardian")
        print("3. Independent")
        print("4. Daily Mail")
        print("5. Return to main menu")

        selection = input("Select a Site or Return to Menu (1-5): ")
        if selection == "1":
            print("BBC News Print Out")
            selected_url = "http://feeds.bbci.co.uk/news/uk/rss.xml"
            rss_scraper(selected_url)
        elif selection == "2":
            print("The Guardian Print Out")
            selected_url = "https://www.theguardian.com/uk-news/rss"
            rss_scraper(selected_url)
        elif selection == "3":
            print("The Independent Print out")
            selected_url = "https://www.independent.co.uk/news/uk/rss"
            rss_scraper(selected_url)
        elif selection == "4":
            print("Daily Mail Print out")
            selected_url = "https://www.dailymail.co.uk/home/index.rss"
            rss_scraper(selected_url)
        elif selection == "5":
            main()


def extrasubmenu():
    while True:
        print("--- Brit/pol/ Paste Generator - Extras ---")
        print("1. No Trolling Addendum")
        print("2. Self-Improvement General")
        print("3. Buy Guns")
        print("4. Main Menu")

        selection = input("Enter a selection: ")

        if selection == "1":
            print("Socialism edition \n \n \n Socialism Test")
        if selection == "2":
            print("")
        elif selection == "4":
            main()


def rss_scraper(url):
    print("RSS/XML scraper Function Pass")
    xml = requests.get(url).text
    soup = BeautifulSoup(xml, 'xml')
    items = soup.find_all('item')
    i = 1

    for item in items:
        title = item.find('title').text
        link = item.find('link').text
        flink = link.replace("?at_medium=RSS&at_campaign=KARANGA", "").replace("?ns_mchannel=rss&ns_campaign=1490&ito=1490", "")
        ftitle = ">" + title.replace(",", "*").replace(":", "#")
        #print(f'{i}. {title}')
        #print(flink)
        articles.append({title})
        arti_wlinks.append({ftitle: flink})
        i += 1
        if i > 8:
            #print(articles)
            reviewer(articles, arti_wlinks)

def reviewer(articles, arti_wlinks):
    while True:
        clear_screen()
        print("--- Brit/pol/ Paste Generator - Article Selector ---")
        for i, title in enumerate(articles):
            print(f'{i + 1}. {title}')

        selection = input(f"\nInput Number 1 - {len(articles)} : ")

        try:
            selection = int(selection)
            if isinstance(selection, int):
                if 0 < selection <= len(articles):
                    articles.pop(selection - 1)
                    arti_wlinks.pop(selection - 1)
                else:
                    print("Invalid Number")
        except ValueError:
            if selection == "clear":
                articles.clear()
                clear_screen()
                print("--- Returning to Main Menu ---")
                main()
            elif selection == "main":
                print("--- Returning to Main Menu with Links --- \n")
                main()
            elif selection == "more":
                print("--- Returning to Sites Submenu --- \n")
                clear_screen()
                submenu()
            elif selection == "done":
                print("--- Proceeding to Final Review ---")
                size_check(articles, arti_wlinks)
            else:
                print("please enter a valid input (was identified as a string)")

def size_check(articles, arti_wlinks):
    print("Size Check Pass")
    if len(articles) >= 8:
        print("This paste contains over 8 articles, do you wish to continue?")

        selection = input("y/n: ")
        if selection == "y":
            finalprint(arti_wlinks)
        elif selection == "n":
            reviewer(articles, arti_wlinks)
        else:
            print("Please Enter a valid input")
    else:
        finalprint(arti_wlinks)


def finalprint(arti_wlinks):
    print("final print function pass")
    printout = str(arti_wlinks)
    fprintout = printout.replace("[", "").replace("]", "").replace("{", "").replace("}", "\n").replace("'", "")\
        .replace('"', "").replace(", ", "\n").replace(": ", "\n").replace("*", ",").replace("#",":")
    print(fprintout)
    clipboard.copy(fprintout)
    print("\nThank You for using Brit/pol/ Paste maker!")
    print("Your output has been copied to your clipboard!")
    exit(0)

def clear_screen():
    os.system(clear_command)


articles = []
arti_wlinks = []
extras = []

if platform.system() == 'Windows':
    clear_command = 'cls'
    print("Windows")
else:
    print("Linux/UNIX")
    clear_command = 'clear'

main()
