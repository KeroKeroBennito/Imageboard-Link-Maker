import requests, clipboard, os, platform
from bs4 import BeautifulSoup

def main():
    while True:
        print("--- Brit/pol/ Paste Generator ---")
        print("1. Sites")
        print("2. Extras")
        print("3. Print Out Paste")
        print("4. Quit")
        print("\nPress 'i' for instructions (Please Read if First Use)")

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
        elif selection == "i":
            clear_screen()
            insmenu()
        else:
            print("Please Enter a Valid Input")
            clear_screen()


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
        else:
            print("Please Enter a Valid Input")
            clear_screen()

def extrasubmenu():
    while True:
        print("--- Brit/pol/ Paste Generator - Extras ---")
        print("1. No Trolling Addendum")
        print("2. Industrial Society (and its consequences")
        print("3. Main Menu")

        selection = input("Enter a selection: ")

        if selection == "1":
            rules = "------------------------------------------------------------------------\n" \
                    "Rules For General:\n1.) Ignore all off topic posts and off topic image posts.\n2.) Ignore " \
                    "all derailing posts.\nBy not replying to off topic posts and images, you will keep the threads " \
                    "on track and in keeping with the general "\
                    "\nBritish politics format. Please use this template for all new threads. "
            extras.append(rules)
            dupezapper()
            clear_screen()
            main()
        if selection == "2":
            rules = ">INDUSTRIAL SOCIETY AND ITS FUTURE\nhttps://www.washingtonpost.com/wp-srv/national/longterm/unabomber/manifesto.text.htm??noredirect=on" \
                    "\nhttps://theanarchistlibrary.org/library/fc-industrial-society-and-its-future" \
                    "\nhttps://archive.org/details/IndustrialSocietyAndItsFuture-TheUnabombersManifesto \n"\
                    "\n>TECHNOLOGICAL SLAVERY" \
                    "\nhttps://archive.org/details/tk-Technological-Slavery/page/n1\n" \
                    "\n>ANTI-TECH REVOLUTION: WHY AND HOW" \
                    "\nhttps://archive.org/details/KaczynskiAntiTechRevolutionWhyAndHow_201803 "
            extras.append(rules)
            dupezapper()
            clear_screen()
            main()
        elif selection == "3":
            clear_screen()
            main()
        else:
            print("Please Enter a Valid Input")
            clear_screen()


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
        articles.append({title})
        arti_wlinks.append({ftitle: flink})
        i += 1
        if i > 8:
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
                print("--- Clearing Articles ---")
                submenu()
            elif selection == "main":
                clear_screen()
                print("--- Returning to Main Menu with Links ---")
                main()
            elif selection == "more":
                clear_screen()
                print("--- Returning to News Site Menu ---")
                submenu()
            elif selection == "extras":
                clear_screen()
                print("--- Moving to Extras Menu ---")
                extrasubmenu()
            elif selection == "done":
                print("--- Proceeding to Final Review ---")
                size_check(articles, arti_wlinks)
            else:
                print("Please Enter a Valid Input")

def size_check(articles, arti_wlinks):
    #print("Size Check Pass")
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
    #print("final print function pass")
    printout = str(arti_wlinks)
    fprintout = printout.replace("[", "").replace("]", "").replace("{", "").replace("}", "\n").replace("'", "")\
        .replace('"', "").replace(", ", "\n").replace(": ", "\n").replace("*", ",").replace("#",":")
    #print(len(extras))
    if len(extras) == 1:
        #print("--- Extras Detected ---")
        fextras = str(extras)
        fextras = fextras.replace("[", "").replace("]", "").replace("{", "").replace("'", "").replace("\\n", "\n")
        print(fprintout + "\n" + fextras)
        clipboard.copy(fprintout + fextras)
    else:
        #print("--- No Extras Detected ---")
        print(fprintout)
        clipboard.copy(fprintout)

    print("\nThank You for using Brit/pol/ Paste maker!")
    print("Your output has been copied to your clipboard!")
    exit(0)

def clear_screen():
    os.system(clear_command)

def dupezapper():
    if len(extras) > 1:
        extras.pop(1)

def insmenu():
    while True:
        print("--- Brit/pol/ Paste Generator - Instructions ---\n"
              "--- General Navigation ---\n"
              "Disclaimer: This Program is still in beta\n"
              "1. During normal navigation the number keys (Usually ranging between 1 - 8)\n"
              "2. After a number is selected press enter to confirm your choice\n\n"
              "--- Article Reviewer ---\n"
              "When using the Article Reviewer there are four extra commands\n"
              "1. 'clear' - This will clear your current article list and return you to the News site menu\n"
              "2. 'more' - This will return you to the news site with your links\n"
              "3. 'main' - This will return you to the Main Menu with your links\n"
              "4. 'done' - This will push your links through the Final Paste\n"
              "5. 'extras' - This will push you to the Extras Menu\n"
              "The Article Reviewer only currently takes 1 input number at a time\n"
              "The Number selected will be deleted from the list\n\n"
              "--- Extras Menu ---\n"
              "The Extras Menu is Under Construction\n"
              "Currently there are only two pastes to pick from\n"
              "You will only be allowed to print one prompt from the extras menu\n"
              "Only your most recent pick will be saved to the print out\n\n"
              "--- Future Plans ---\n"
              "-- Add an 'all sites' option in the news site menus\n"
              "--- The Article Reviewer is already able to handle X Number of articles")

        selection = input("\nPress Enter to return to Main Menu...\n:")
        clear_screen()
        main()




articles = []
arti_wlinks = []
extras = []

if platform.system() == 'Windows':
    clear_command = 'cls'
    #print("Windows")
else:
    #print("Linux/UNIX")
    clear_command = 'clear'

main()
