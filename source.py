import random as rd
import webbrowser
import sys
import time



#dictionary for country and capital in north america
north_america_dic={'Antigua and Barbuda':'Saint Johns','Bahamas':'Nassau','Barbados':'Bridgetown',
                   'Belize':'Belmopan','Canada':'Ottawa','Costa Rica':'San Jose',
                   'Cuba':'Havana','Dominica':'Roseau','Dominican Republic':'Santo Domingo',
                   'El Salvador':'San Salvador','Grenada':'Saint Georges','Guatemala':'Guatemala City',
                  'Haiti':'Port-au-Prince','Honduras':'Tegucigalpa','Jamaica':'Kingston',
                  'Mexico':'Mexico City','Nicaragua':'Managua','Panama':'Panama City',
                  'Saint Kitts and Nevis':'Basseterre','Saint Lucia':'Castries',
                  'Saint Vincent and the Grenadines':'Kingstown',
                  'Trinidad and Tobago':'Port of Spain',
                  'United States of America':'Washington DC'}

#dictionary for country and capital in south america
sourth_america_dic={'Argentina':'Buenos Aires','Bolivia':'Sucre La Paz','Brazil':'Brasilia',
                    'Chile':'Santiago','Colombia':'Bogota','Ecuador':'Quito','Guyana':'Georgetown',
                    'Paraguay':'Asuncion','Peru':'Lima','Suriname':'Paramaribo',
                    'Uruguay':'Montevideo','Venezuela':'Caracas'}

#dictionary for country and capital in austrlia
australia_dic={'Australia':'Canberra','Fiji':'Suva','Kiribati':'Tarawa',
               'Marshall Islands':'Majuro','Micronesia':'Palikir','Nauru':'Yaren District',
              'New Zealand':'Wellington','Palau':'Ngerulmud','Papua New Guinea':'Port Moresby',
              'Samoa':'Apia','Solomon Islands':'Honiara','Tonga':'Nukualofa','Tuvalu':'Funafuti',
              'Vanuatu':'Port Vila'}

#dictionary for country and capital un asia
asia_dic={'Afghanistan':'Kabul','Armenia':'Yerevan','Azerbaijan':'Baku','Bahrain':'Manama','Bangladesh':'Dhaka',
   'Bhutan':'Thimphu','Brunei':	'Bandar Seri Begawan','Cambodia':'Phnom Penh','China':'Beijing','Cyprus':'Nicosia',
   'Georgia':'Tbilisi','India':'New Delhi','Indonesia':'Jakarta','Iran':'Tehran','Iraq':'Baghdad','Israel':'Jerusalem',
   'Japan':'Tokyo','Jordan':'Amman','Kazakhstan':'Nur-Sultan','Kuwait':	'Kuwait City','Kyrgyzstan':'Bishkek',
   'Laos':'Vientiane','Lebanon':'Beirut','Malaysia':'Kuala Lumpur','Maldives':'Male','Mongolia':'Ulaanbaatar',
   'Myanmar':'Naypyidaw', 'Nepal':'Kathmandu','North Korea':'Pyongyang','Oman':	'Muscat','Pakistan':'Islamabad',
   'Philippines':'Manila','Qatar':'Doha','Russia':'Moscow','Saudi Arabia':'Riyadh','Singapore':'Singapore',
   'South Korea':'Seoul','Sri Lanka':'Sri Jayawardenepura Kotte','Syria':'Damascus','Taiwan':'Taipei','Tajikistan':'Dushanbe',
   'Thailand':'Bangkok','Timor-Leste':'Dili','Turkey':'Ankara','Turkmenistan':'Ashgabat','United Arab Emirates':'Abu Dhabi',
   'Uzbekistan':'Tashkent','Vietnam':'Hanoi','Yemen':'Sana'}

#dictionary for country and capital un afrika
afrika_dic={'Algeria':'Algiers','Angola':'Luanda','Benin':'Porto-Novo','Botswana':'Gaborone','Burkina Faso':'Ouagadougou',
            'Burundi':'Gitega','Cabo Verde':'Praia','Cameroon':'Yaounde','Central African Republic':'Bangui','Chad':'NDjamena',
            'Comoros':'Moroni','Congo':'Kinshasa','Congo Republic':'Brazzaville','Cote dIvoire':'Yamoussoukro','Djibouti':'Djibouti',
           'Egypt':'Cairo','Equatorial Guinea':'Malabo','Eritrea':'Asmara','Eswatini':'Mbabane Lobamba','Ethiopia':'Addis Ababa',
           'Gabon':'Libreville','Gambia':'Banjul','Ghana':'Accra','Guinea':'Conakry','Guinea-Bissau':'Bissau','Kenya':'Nairobi',
           'Lesotho':'Maseru','Liberia':'Monrovia','Libya':'Tripoli','Madagascar':'Antananarivo','Malawi':'Lilongwe','Mali':'Bamako',
           'Mauritania':'Nouakchott','Mauritius':'Port Louis','Morocco':'Rabat','Mozambique':'Maputo','Namibia':'Windhoek','Niger':'Niamey',
           'Nigeria':'Abuja','Rwanda':'Kigali','Sao Tome and Principe':	'Sao Tome','Senegal':'Dakar',
           'Seychelles':'Victoria','Sierra Leone':'Freetown','Somalia':'Mogadishu',
           'South Africa':'Pretoria Cape Town Bloemfontein','South Sudan':'Juba','Sudan':'Khartoum',
           'Tanzania':'Dodoma','Togo':'Lome','Tunisia':'Tunis','Uganda':'Kampala','Zambia':'Lusaka',
           'Zimbabwe':'Harare'}

#dictionary for country and capital un europe
europe_dic={'Albania':'Tirana','Andorra':'Andorra la Vella','Armenia':'Yerevan','Austria':'Vienna',
            'Azerbaijan':'Baku','Belarus':'Minsk','Belgium':'Brussels','Bosnia and Herzegovina':'Sarajevo',
            'Bulgaria':'Sofia','Croatia':'Zagreb','Cyprus':'Nicosia','Czechia':'Prague',
            'Denmark':'Copenhagen','Estonia':'Tallinn','Finland':'Helsinki','France':'Paris',
            'Georgia':'Tbilisi','Germany':'Berlin','Greece':'Athens','Hungary':'Budapest',
            'Iceland':'Reykjavik','Ireland':'Dublin','Italy':'Rome','Kazakhstan':'Nur-Sultan',
            'Kosovo':'Pristina','Latvia':'Riga','Liechtenstein':'Vaduz','Lithuania':'Vilnius',
            'Luxembourg':'Luxembourg','Malta':'Valletta','Moldova':'Chisinau','Monaco':'Monaco',
            'Montenegro':'Podgorica','Netherlands':'Amsterdam','North Macedonia':'Skopje',
            'Norway':'Oslo','Poland':'Warsaw','Portugal':'Lisbon','Romania':'Bucharest',
            'Russia':'Moscow','San Marino':'San Marino','Serbia':'Belgrade','Slovakia':'Bratislava',
            'Slovenia':'Ljubljana','Spain':'Madrid','Sweden':'Stockholm',
            'Switzerland':'Bern','Turkey':'Ankara','Ukraine':'Kyiv','United Kingdom':'London'}

#dictionary mix
mix_dic = {'Albania':'Tirana','Andorra':'Andorra la Vella','Armenia':'Yerevan','Austria':'Vienna',
            'Azerbaijan':'Baku','Belarus':'Minsk','Belgium':'Brussels','Bosnia and Herzegovina':'Sarajevo',
            'Bulgaria':'Sofia','Croatia':'Zagreb','Cyprus':'Nicosia','Czechia':'Prague',
            'Denmark':'Copenhagen','Estonia':'Tallinn','Finland':'Helsinki','France':'Paris',
            'Georgia':'Tbilisi','Germany':'Berlin','Greece':'Athens','Hungary':'Budapest',
            'Iceland':'Reykjavik','Ireland':'Dublin','Italy':'Rome','Kazakhstan':'Nur-Sultan',
            'Kosovo':'Pristina','Latvia':'Riga','Liechtenstein':'Vaduz','Lithuania':'Vilnius',
            'Luxembourg':'Luxembourg','Malta':'Valletta','Moldova':'Chisinau','Monaco':'Monaco',
            'Montenegro':'Podgorica','Netherlands':'Amsterdam','North Macedonia':'Skopje',
            'Norway':'Oslo','Poland':'Warsaw','Portugal':'Lisbon','Romania':'Bucharest',
            'Russia':'Moscow','San Marino':'San Marino','Serbia':'Belgrade','Slovakia':'Bratislava',
            'Slovenia':'Ljubljana','Spain':'Madrid','Sweden':'Stockholm',
            'Switzerland':'Bern','Turkey':'Ankara','Ukraine':'Kyiv','United Kingdom':'London','Algeria':'Algiers','Angola':'Luanda','Benin':'Porto-Novo','Botswana':'Gaborone','Burkina Faso':'Ouagadougou',
            'Burundi':'Gitega','Cabo Verde':'Praia','Cameroon':'Yaounde','Central African Republic':'Bangui','Chad':'NDjamena',
            'Comoros':'Moroni','Congo':'Kinshasa','Congo Republic':'Brazzaville','Cote dIvoire':'Yamoussoukro','Djibouti':'Djibouti',
           'Egypt':'Cairo','Equatorial Guinea':'Malabo','Eritrea':'Asmara','Eswatini':'Mbabane Lobamba','Ethiopia':'Addis Ababa',
           'Gabon':'Libreville','Gambia':'Banjul','Ghana':'Accra','Guinea':'Conakry','Guinea-Bissau':'Bissau','Kenya':'Nairobi',
           'Lesotho':'Maseru','Liberia':'Monrovia','Libya':'Tripoli','Madagascar':'Antananarivo','Malawi':'Lilongwe','Mali':'Bamako',
           'Mauritania':'Nouakchott','Mauritius':'Port Louis','Morocco':'Rabat','Mozambique':'Maputo','Namibia':'Windhoek','Niger':'Niamey',
           'Nigeria':'Abuja','Rwanda':'Kigali','Sao Tome and Principe':	'Sao Tome','Senegal':'Dakar',
           'Seychelles':'Victoria','Sierra Leone':'Freetown','Somalia':'Mogadishu',
           'South Africa':'Pretoria Cape Town Bloemfontein','South Sudan':'Juba','Sudan':'Khartoum',
           'Tanzania':'Dodoma','Togo':'Lome','Tunisia':'Tunis','Uganda':'Kampala','Zambia':'Lusaka',
           'Zimbabwe':'Harare','Afghanistan':'Kabul','Armenia':'Yerevan','Azerbaijan':'Baku','Bahrain':'Manama','Bangladesh':'Dhaka',
   'Bhutan':'Thimphu','Brunei':	'Bandar Seri Begawan','Cambodia':'Phnom Penh','China':'Beijing','Cyprus':'Nicosia',
   'Georgia':'Tbilisi','India':'New Delhi','Indonesia':'Jakarta','Iran':'Tehran','Iraq':'Baghdad','Israel':'Jerusalem',
   'Japan':'Tokyo','Jordan':'Amman','Kazakhstan':'Nur-Sultan','Kuwait':	'Kuwait City','Kyrgyzstan':'Bishkek',
   'Laos':'Vientiane','Lebanon':'Beirut','Malaysia':'Kuala Lumpur','Maldives':'Male','Mongolia':'Ulaanbaatar',
   'Myanmar':'Naypyidaw', 'Nepal':'Kathmandu','North Korea':'Pyongyang','Oman':	'Muscat','Pakistan':'Islamabad',
   'Philippines':'Manila','Qatar':'Doha','Russia':'Moscow','Saudi Arabia':'Riyadh','Singapore':'Singapore',
   'South Korea':'Seoul','Sri Lanka':'Sri Jayawardenepura Kotte','Syria':'Damascus','Taiwan':'Taipei','Tajikistan':'Dushanbe',
   'Thailand':'Bangkok','Timor-Leste':'Dili','Turkey':'Ankara','Turkmenistan':'Ashgabat','United Arab Emirates':'Abu Dhabi',
   'Uzbekistan':'Tashkent','Vietnam':'Hanoi','Yemen':'Sana','Australia':'Canberra','Fiji':'Suva','Kiribati':'Tarawa',
               'Marshall Islands':'Majuro','Micronesia':'Palikir','Nauru':'Yaren District',
              'New Zealand':'Wellington','Palau':'Ngerulmud','Papua New Guinea':'Port Moresby',
              'Samoa':'Apia','Solomon Islands':'Honiara','Tonga':'Nukualofa','Tuvalu':'Funafuti',
              'Vanuatu':'Port Vila','Argentina':'Buenos Aires','Bolivia':'Sucre La Paz','Brazil':'Brasilia',
                    'Chile':'Santiago','Colombia':'Bogota','Ecuador':'Quito','Guyana':'Georgetown',
                    'Paraguay':'Asuncion','Peru':'Lima','Suriname':'Paramaribo',
                    'Uruguay':'Montevideo','Venezuela':'Caracas','Antigua and Barbuda':'Saint Johns','Bahamas':'Nassau','Barbados':'Bridgetown',
                   'Belize':'Belmopan','Canada':'Ottawa','Costa Rica':'San Jose',
                   'Cuba':'Havana','Dominica':'Roseau','Dominican Republic':'Santo Domingo',
                   'El Salvador':'San Salvador','Grenada':'Saint Georges','Guatemala':'Guatemala City',
                  'Haiti':'Port-au-Prince','Honduras':'Tegucigalpa','Jamaica':'Kingston',
                  'Mexico':'Mexico City','Nicaragua':'Managua','Panama':'Panama City',
                  'Saint Kitts and Nevis':'Basseterre','Saint Lucia':'Castries',
                  'Saint Vincent and the Grenadines':'Kingstown',
                  'Trinidad and Tobago':'Port of Spain',
                  'United States of America':'Washington DC'}
mix_dic['Kiribati']='South Tarawa'



#list for country in asia
countries_in_the_world=list(mix_dic.keys())

#for guess
guess_city=[]
guess_letter=[]
alphabet = "abcdefghijklmnopqrstuvwxyz "

print("Countries Game!!\n")
#to start
while True:
    name = input("Please enter Your name\n").strip()#strip for remove space
    if name == '':
        print("You can't do that!")
    else:
        print("Nice to meet you ",name)
        print()
        break

#to begining play
print("Well, that's perfect moment to play\n", )
while True:
    gameChoice = input("Would You?\n").upper()
    if gameChoice == "YES" or gameChoice == "Y":
        break
    elif gameChoice == "NO" or gameChoice == "N":
        print("Have a nice day")
        time.sleep(5)
        sys.exit()
    else:
        print("Please Answer only Yes or No")
        continue

#the role
while True:
    print("I will tell you country and you guess what har capital !! ")
    time.sleep(3)
    ok = input("Do you understand?\n").upper()
    if ok == "YES" or ok == "Y":
        break
    elif ok == "NO" or ok == "N":
        continue
    else:
        print("Please Answer only Yes or No")
        continue

#my play
while True:
    guess_city=[]
    guess_letter=[]
    rand_own_country=str(rd.choice(countries_in_the_world))
    print("My choice is the country  : ",rand_own_country)
    print()
    print("What is her capital city ? \n")
    time.sleep(3)

    #the city
    secret_city=mix_dic[rand_own_country].lower()
    #length
    len_city = len(secret_city)
    
    # print for num of letter in city
    for letter in secret_city: 
     guess_city.append("-")
    print(guess_city)

    #for guess
    cont=0
    while cont < len_city :#times
        guess=input("Enter a letter from a-z\n").lower()
        if guess not in alphabet:#guess not a letter
            print("Only number from a-z or space")
        elif guess not in secret_city:
            print(guess_city)
            print("Wrong guess!\n Try again!")
            print()
            cont+=1
        else:
            cont+=1
            guess_letter.append(guess)
            if guess in secret_city:
                print("You guessed correctly!")
                for i in range(0,len_city):
                    if secret_city[i]==guess:#for save
                        guess_city[i]=guess#to copy
                print(guess_city)
                print()
                if not '-' in guess_city:
                    print("You woner!")
                    break

    print()
    print("The capital city is : ",secret_city)
    time.sleep(3)
    #open web of contry
    print()
    wikipedia_web="https://en.wikipedia.org/wiki/"
    address = wikipedia_web + rand_own_country#wikipedia and contry
    print()
    print("Let's get more information about the country\n")

    while True:
        Choice = input("Do you want to?\n").upper()
        if Choice == "YES" or Choice == "Y":
            webbrowser.open(address)
        elif Choice == "NO" or Choice == "N":
            ok = input("Do you want one more game??\n").upper()
            if ok == "YES" or ok == "Y":
                print("Good choice !!!")
                time.sleep(2)
                print("I will tell you country and you guess what har capital !! ")
                print()
                time.sleep(3)
                break
            elif ok == "NO" or ok == "N": 
               print("Maybe next time\n Bye Bye !!!")
               time.sleep(5)
               sys.exit()
        else:
            print("Please Answer only Yes or No")
            continue

              
                

   
            

           
       
    




