'''
Дадено е податочно множество на документи од спорт (спорт) и наука (science). Потребно е да се најдат најсличните 4
документи на документ кој се чита од стандарден влез (test_doc). Сличноста на документите се одредува според клучни
зборови пронајдени со методот tf-idf, односно сличноста се однесува на бројот на заеднички клучни зборови. Колку е
поголем бројот на заеднички клучни зборови, толку тој документ е посличен со моменталниот документ.

Секој од документите треба да се престави со tf-idf вектор, од кој треба да се извлечат зборовите со tf-idf вредност
поголема од 0 како клучни зборови. За документот кој се чита од стандарден влез потребно е да се извлечат клучните
зборови и да се спореди со документите од податочното множество (да се најде бројот на заеднички клучни зборови).
На стандарден излез испечатете ги индексите на 4те најслични документи од множеството за тренирање, како и заедничните
клучни зборови (сортирани алфабетски).
'''


from tf_idf_changed_for_exercise6 import *

data=[
("""What Are We Searching for on Mars?
Martians terrified me growing up. I remember watching the 1996 movie Mars Attacks! and fearing that the Red Planet harbored hostile alien neighbors. Though I was only 6 at the time, I was convinced life on Mars meant little green men wielding vaporizer guns. There was a time, not so long ago, when such an assumption about Mars wouldn’t have seemed so far-fetched.
Like a child watching a scary movie, people freaked out after listening to “The War of the Worlds,” the now-infamous 1938 radio drama that many listeners believed was a real report about an invading Martian army. Before humans left Earth, humanity’s sense of what—or who—might be in our galactic neighborhood was, by today’s standards, remarkably optimistic.
""",
"science"),
("""Mountains of Ice are Melting, But Don't Panic (Op-Ed)
If the planet lost the entire West Antarctic ice sheet, global sea level would rise 11 feet, threatening nearly 13 million people worldwide and affecting more than $2 trillion worth of property. 
Ice loss from West Antarctica has been increasing nearly three times faster in the past decade than during the previous one — and much more quickly than scientists predicted.
This unprecedented ice loss is occurring because warm ocean water is rising from below and melting the base of the glaciers, dumping huge volumes of additional water — the equivalent of a Mt. Everest every two years — into the ocean.
""",
"science"),
("""Some scientists think we'll find signs of aliens within our lifetimes. Here's how.
Finding extraterrestrial life is the essence of science fiction. But it's not so far-fetched to predict that we might find evidence of life on a distant planet within a generation.
"With new telescopes coming online within the next five or ten years, we'll really have a chance to figure out whether we're alone in the universe," says Lisa Kaltenegger, an astronomer and director of Cornell's new Institute for Pale Blue Dots, which will search for habitable planets. "For the first time in human history, we might have the capability to do this."
""",
"science"),
("""'Magic' Mushrooms in Royal Garden: What Is Fly Agaric?
Hallucinogenic mushrooms are perhaps the last thing you'd expect to find growing in the Queen of England's garden.
Yet a type of mushroom called Amanita muscaria — commonly known as fly agaric, or fly amanita — was found growing in the gardens of Buckingham Palace by the producers of a television show, the Associated Press reported on Friday (Dec. 12).
A. muscaria is a bright red-and-white mushroom, and the fungus is psychoactive when consumed.
""",
"science"),
("""Upcoming Parks : 'Lost Corner' Finds New Life in Sandy Springs
At the corner of Brandon Mill Road, where Johnson Ferry Road turns into Dalrymple Road, tucked among 24 forested acres, sits an early 20th Century farmhouse. A vestige of Sandy Springs' past, the old home has found new life as the centerpiece of Lost Forest Preserve. While the preserve isn't slated to officially debut until some time next year, the city has opened the hiking trails to the public until construction begins on the permanent parking lot (at the moment the parking lot is a mulched area). The new park space includes community garden plots, a 4,000-foot-long hiking trail and an ADA-accessible trail through the densely wooded site. For Atlantans seeking an alternate escape to serenity (or those who dig local history), it's certainly worth a visit.
""",
"science"),
("""Stargazers across the world got a treat this weekend when the Geminids meteor shower gave the best holiday displays a run for their money.
The meteor shower is called the "Geminids" because they appear as though they are shooting out of the constellation of Gemini. The meteors are thought to be small pieces of an extinct comment called 3200 Phaeton, a dust cloud revolving around the sun. Phaeton is thought to have lost all of its gas and to be slowly breaking apart into small particles.
Earth runs into a stream of debris from 3200 Phaethon every year in mid-December, causing a shower of meteors, which hit its peak over the weekend.
""",
"science"),
("""Envisioning a River of Air
By the classification rules of the world of physics, we all know that the Earth's atmosphere is made of gas (rather than liquid, solid, or plasma). But in the world of flying it's often useful to think
""",
"science"),
("""Following Sunday's 17-7 loss to the Seattle Seahawks, the San Francisco 49ers were officially eliminated from playoff contention, and they have referee Ed Hochuli to blame. OK, so they have a lot of folks to point the finger at for their 7-7 record, but Hochuli's incorrect call is the latest and easiest scapegoat.
"""
,"sport"),
("""Kobe Bryant and his teammates have an odd relationship. That makes sense: Kobe Bryant is an odd guy, and the Los Angeles Lakers are an odd team.
They’re also, for the first time this season, the proud owners of a three-game winning streak. On top of that, you may have heard, Kobe Bryant passed Michael Jordan on Sunday evening to move into third place on the NBA’s all-time scoring list. 
"""
,"sport"),
("""The Patriots continued their divisional dominance and are close to clinching home-field advantage throughout the AFC playoffs. Meanwhile, both the Colts and Broncos again won their division titles with head-to-head wins.The Bills' upset of the Packers delivered a big blow to Green Bay's shot at clinching home-field advantage throughout the NFC playoffs. Detroit seized on the opportunity and now leads the NFC North.
"""
,"sport"),
("""If you thought the Washington Redskins secondary was humbled by another scintillating performance from New Yorks Giants rookie wide receiver sensation Odell Beckham Jr., think again.In what is becoming a weekly occurrence, Beckham led NFL highlight reels on Sunday, collecting 12 catches for 143 yards and three touchdowns in Sunday's 24-13 victory against an NFC East rival. 
"""
,"sport")
,("""That was two touchdowns and 110 total yards for the three running backs. We break down the fantasy implications.The New England Patriots' rushing game has always been tough to handicap. Sunday, all three of the team's primary running backs put up numbers, and all in different ways, but it worked for the team, as the Patriots beat the Miami Dolphins, 41-13.
"""
,"sport"),
("""General Santos (Philippines) (AFP) - Philippine boxing legend Manny Pacquiao vowed to chase Floyd Mayweather into ring submission after his US rival offered to fight him next year in a blockbuster world title face-off. "He (Mayweather) has reached a dead end. He has nowhere to run but to fight me," Pacquiao told AFP late Saturday, hours after the undefeated Mayweather issued the May 2 challenge on US television. The two were long-time rivals as the "best pound-for-pound" boxers of their generation, but the dream fight has never materialised to the disappointment of the boxing world.
"""
,"sport"),
("""When St. John's landed Rysheed Jordan, the consensus was that he would be an excellent starter.
So far, that's half true.
Jordan came off the bench Sunday and tied a career high by scoring 24 points to lead No. 24 St. John's to a 74-53 rout of Fordham in the ECAC Holiday Festival.
''I thought Rysheed played with poise,'' Red Storm coach Steve Lavin said. ''Played with the right pace. Near perfect game.''
"""
,"sport"),
("""Five-time world player of the year Marta scored three goals to lead Brazil to a 3-2 come-from-behind win over the U.S. women's soccer team in the International Tournament of Brasilia on Sunday. Carli Lloyd and Megan Rapinoe scored a goal each in the first 10 minutes to give the U.S. an early lead, but Marta netted in the 19th, 55th and 66th minutes to guarantee the hosts a spot in the final of the four-team competition.
"""
,"sport")
]


if __name__ == '__main__':
    test_doc = input()

    docs = [torka[0] for torka in data]   # we need only docs(sentences)
    df = calculate_document_frequencies(docs) # frequency of occurrence of each word
    n = len(docs)                    # how many documents
    vocab = get_vocabulary(docs)     # all words that are used in the docs

    vec_input = process_document(test_doc, df, n, vocab)   # make a vector from the document given on input
    keywords_input = []         # here we will store key words from the sentence given on input
    for tuple in vec_input:      # for each word given in the vector of tuples that process_document created ---> if tf_idf value for the word is > 0 we say that is keyword
        if tuple[1] > 0:
            keywords_input.append(tuple[0])

    main_list = []      # list of lists where every inner list contains common word for every document sequentially with the document from input
    document = 0      # iterator that will be used to fill in the dictionary where we will store the information needed like this  {indeks_na_dok: br_zaednicki_zborovi_so_vlez, indeks_na_dok: br_zaednicki_zborovi_so_vlez, indeks_na_dok: br_zaednicki_zborovi_so_vlez.. }
    dict = {}
    for doc in docs:   # iterate doc by doc
        counter = 0         # counter of how many common words has every sentence from the list of docs with the sentence given on input
        pom = []        # list that will store the common words with the input for each sentence, but only the words without tf_idf values
        keywords_data = []     # here we will store every word they has tf_idf > 0 (is keyword)
        vec_data = process_document(doc, df, n, vocab)  # list of tuples (word, tf_idf_value)
        for tuple in vec_data:     # take out the keywrods from the tuples
            if tuple[1] > 0:
                keywords_data.append(tuple[0])
        for zbor in keywords_input:             # for each keyword from the sentence on input
            if zbor in keywords_data:         # if the same word is in the keywords of the current sentence in the list
                counter += 1
                pom.append(zbor)    # because we need to print each common keyword we store them
        main_list.append(pom)        # out of the for loop we append that list of common words and we create the main list of lists which contains common words for the input with every given sentence in the docs list
        dict[document] = counter         # store that document index as a key and how many common words has with the input as a value
        document += 1                # go to the next sentence in the docs


    sorted_list = sorted(dict.items(), key=lambda x: x[1], reverse=True)  # we need 4 docs that have the most common words with the input because of that we sort the created dictionary by value in descending order
    for item in sorted_list[:4]:     # now we iterate that sorted dict that is casted to list because of .items()
        out = ""
        index = item[0]                 # item[0] is the index of the document
        for el in main_list[index]:     # and now we iterate the inner list that is on position 'index' in the main list (this list contains the common words for that specific document and the input)
            out += el + " "             # we append each word to output string with space between
        print(f"Dokument #{index}: {out[:-1]}")     # ad the end we print the index of the document and the string that has appendend common words

