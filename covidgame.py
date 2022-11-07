import webbrowser

def TitlePage(): 
    return ('Welcome to: How to Survive COVID-19 for Dummies!')

def GameInfo():
    return ('''In this dire time, it is very stressful to be a Malaysian, 
            especially if you are on the web, where the abundance of fake news 
            and information and the confusion of the masses regarding the pandemic far outweigh their counterparts. 
            Worry not; with this simple "game," all your confusion and worries will be put to ease. ''')
def NameInput():
    return ('First thing first, please give us your name, dear fellow Malaysian.')

print(TitlePage().upper())
print()
print(GameInfo())
print()
print(NameInput())
person = input('Enter your name: ')
print('Hello', person)
print()
print(MainGame())
def MainGame():
    print('''To learn more about the pandemic, please choose one of the following options to continue:
                       (1) To learn more about the necessary prevention method
                       (2) To learn more about the necessary actions if suspected
                       (3) To learn more about the current state of the pandemic globally (statistics),
                       (4) To learn about the mortality of COVID-19''')
    print()
    optiongame = input('Please enter your option number (1-4) :')
    print()
    if optiongame == '1':
        print('You have chosen option ', optiongame)
        print('''Before we are going to display to you about the tips to handle the pandemic, 
              we had a prepare a question for you. 
              The main purpose of the question is just to test your knowledge on the topic at hand.''')
        print('''Question: You have been invited to an event. 
              The event is held in a pretty compacted hall with a large number of attendees. 
              Should you or should you not attend the event?
                       
                       Press 'Y' if you think you should
                       Press 'N' if you think you shouldn't.
                       ''')
        quest1ans=input('Your answer is: ')
        print()
        def option1tip():
            return ('TIPS 1: APPLY SOCIAL DISTANCING - Avoid crowded places as much as you can.')
        if quest1ans == 'Y':
            print('CONGRATULATIONS. You have just exposed yourself to the risk of contracting the pandemic.')
        elif quest1ans == 'N':
            print('GOOD JOB. You have chosen the best option of the two.')
        else:
            print('Invalid input has been submitted.')
        print(option1tip())
        print('TIPS 2 : ALWAYS WASH YOUR HANDS - The most inport precaution step to take in battling the pandemic is the simple action of washing your hands, scientists had explain that it takes 20 seconds of thorough hand-washing for the hands to be virus-free.')
        print('TIPS 3 : MASK IS ONLY FOR THE SICKS - The action of hoarding facemasks not only will be exploited by the industry who had raise the price of the item but also worsens the current situation as researcher explains that the masks works by blocking the viruses to spread out, not by blocking viruses to enter your body, the best solution is to give the sicks the mask.')
        print('TIPS 4 : TRUST ONLY THE AUTHORITIES - The number of wrong informations that is being circulated on the social media is A LOT, it does not only causes harm to the authorities, but also it will be able to cause a mass panic on the community. ')
    elif optiongame == '2':
        print('You have chosen option ',optiongame)
        print('Lets talk about what you need to do if you are suspected to contract the disease. ')
        print('''First you need to know that there are several reasons on how an indiviual can be suspected, they are:
              (1) You have a travel history to "hotspot" countries
              (2) You have a communication history with a COVID-19 patients''')
        print('To test your knowledge on the topic, a question will now be asked')
        print('''Question: Among these 4 countries, 3 of them are being called as COVID-19 "hotspot" countries. If you had travel history to one of these countries, which country travel history will NOT placed you under the suspected group. 
          
                      Press '1' for France
                      Press '2' for Italy
                      Press '3' for Indonesia
                      Press '4' for China
                      ''')
        quest2ans=input('Your answer is (1-4):')
        if quest2ans == '1':
            print('Sorry to inform you, Paris is no longer the city of love, and you are now suspected.')
        elif quest2ans == '2':
            print('Right now is a very bad time to visit "Bel Paese", as it is currently the europe most affected country, and you are now suspected. ')
        elif quest2ans == '3':
            print('CONGRATULATIONS. You had made the correct choice, Indonesia is the only country in the list that is not considered a "hotspot" country. You are not on the suspect list. ')
        elif quest2ans == '4':
            print('Boy oh boy, you had made a very bad choice. For your information as the first country to be affected, and the pandemic place of origin, is the most affected country on earth. You are now on the suspect list.')  
        else:
            print('Invalid input has been submitted.')
    elif optiongame == '3':
        print('You have chosen option ',optiongame)
        print(''' Here are the current situation of the pandemic in Malaysia:-
          
          Day: Monday                         Date: 16/3/2020
          Number of cases(New):553(125)       Number of Death(0)
          ''') 
    elif optiongame == '4':
        print('You have chosen option ',optiongame)
        print('To know more about the mortality rate of the pandemic, we need to know your age ')
        agequest=input('Please input your age: ')
        print('Your age is', agequest, ' years old')
        if (agequest >= '0' and agequest <='19'):
            print('The mortality rate for 0-19 years old are 0.2%')
        elif(agequest >= '20' and agequest <='29'):
            print('The mortality rate for 20-29 years old are 0.2%')
        elif(agequest >= '30' and agequest <='39'):
            print('The mortality rate for 30-39 years old are 0.2%')
        elif(agequest >= '40' and agequest <='49'):
            print('The mortality rate for 40-49 years old are 0.4%')
        elif(agequest >= '50' and agequest <='59'):                
            print('The mortality rate for 0-19 years old are 1.3%')
        elif(agequest >= '60' and agequest <='69'):            
            print('The mortality rate for 0-19 years old are 3.6%')
        elif(agequest >= '70' and agequest <='79'):
            print('The mortality rate for 0-19 years old are 8.0%')
        elif(agequest >= '80'):
            print('The mortality rate for 80 years old and older are 14.8%')
        else:
            print('Invalid input has been submitted.')
        print('Source: https://ourworldindata.org/coronavirus')
    else:
        print('Wrong input has been submitted!')

print('''Source: https://ourworldindata.org/coronavirus
                 https://www.cdc.gov/coronavirus/2019-ncov/community/large-events/mass-gatherings-ready-for-covid-19.html
                 https://lancasteronline.com/video/covid--dos-and-don-ts-what-the-cdc-recommends/video_a384ef55-f5f6-5f5a-bc7b-5e0b2d591c72.html
                 https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(20)30195-X/fulltext''')

continue1 = input('Do you want to continue using another option? (yes/no) :')
while continue1 == 'yes' or continue1 == 'YES':
    MainGame()
