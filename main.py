import requests, clipboard
from bs4 import BeautifulSoup


def main():
    while True:
        print("Brit/pol/ Paste Generator")
        print("1. Sites")
        print("2. Extras")
        print("3. Print Out Paste")
        print("4. Quit")

        selection = input("Enter a selection: ")

        if selection == "1":
            submenu()
        elif selection == "2":
            extrasubmenu()
        elif selection == "3":
            finalprint()
        elif selection == "4":
            exit(0)
        else:
            print("Please Enter a Valid Input")

def submenu():
    while True:
        print("Brit/pol/ Paste Generator - Sites")
        print("1. BBC News")
        print("2. The Guardian")
        print("3. Independent")
        print("4. Daily Mail")
        print("5. Return to main menu")

        selection = input("Select a Site or Return to Menu (1-4):")
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
        print("Brit/pol/ Paste Generator - Extras")
        print("1. No Trolling Addendum")
        print("2. Self-Improvement General")
        print("3. Buy Guns")
        print("4. Main Menu")

        selection = input ("Enter a selection: ")

        if selection == "1":
            print("Socialism edition \n \n \n Socialism Test")
        if selection == "2":
            print("")
        elif selection == "4":
            main()

def rss_scraper(url):
    url
    xml = requests.get(url).text
    soup = BeautifulSoup(xml, 'xml')
    items = soup.find_all('item')
    i = 1

    for item in items:
        title = item.find('title').text
        link = ">" + item.find('link').text
        flink = link.replace("?at_medium=RSS&at_campaign=KARANGA", "")
        print(f'{i}. {title}')
        print(flink)
        articles.append({title})
        i += 1
        if i > 8:
            print(articles)
            reviewer(articles)

def reviewer(articles):
    while True:
        for i, title in enumerate(articles):
            print(i + 1, title)

        selection = input("\ntest prompt: ")

        try:
            selection = int(selection)
            if isinstance(selection, int):
                if 0 < selection <= len(articles):
                    articles.pop(selection - 1)
                else:
                    print("Invalid Number")
        except ValueError:
            if selection == "clear":
                articles.clear()
                main()
            elif selection == "done":
                print("exiting program")
                main()
                    #exit(0)
            else:
                print("please enter a valid input (was identified as a string)")

def finalprint():
    print("Function Pass")
    printout = str(articles)
    fprintout = printout.replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("'", "").replace('"', "").replace(", ", "\n").replace(": ", "\n").replace("-", ",")
    print(fprintout)
    #clipboard.copy(printout)
    print("\n\nThanks for using Brit/pol/ Paste maker!")
    print("Your output has been copied to your clipboard!")
    exit(0)

articles = []
main()


#pyperclip.copy(finalprint)