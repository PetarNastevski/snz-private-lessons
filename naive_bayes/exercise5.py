'''
Во променливата data дадено е податочно множество од коментари за филмови кои се означени со сентимент. Документот може
да има негативен (0) или позитивен (1) сентимент. Направете два класификатори на Наивен баес. Првиот класификатор треба
да ја користи функцијата get_words (од дадената рамка) за поделба на документот на зборови. Вториот класификатор треба
да ги дели зборовите на истиот начин, но како резултат од функцијата се враќаат само зборовите кои се наоѓаат во листата
на зборови words_to_include.

Од стандарден влез се чита еден коментар за кој треба да се одреди сентиментот (променлива comment). Предодредена класа
при класификацијата е 'unknown'. На излез испринтајте ги предвидените класи за сентимент со двата класификатори.
'''


from naive_bayes import *


data = [('A very, very, very slow-moving, aimless movie about a distressed, drifting young man.', 0),
        ('Not sure who was more lost - the flat characters or the audience, nearly half of whom walked out.', 0),
        ('Attempting artiness with black & white and clever camera angles, the movie disappointed - became even more ridiculous - as the acting was poor and the plot and lines almost non-existent.',
        0), ('Very little music or anything to speak of.', 0),
        ('The best scene in the movie was when Gerardo is trying to find a song that keeps running through his head.',
        1), (
        "The rest of the movie lacks art, charm, meaning... If it's about emptiness, it works I guess because it's empty.",
        0), ('Wasted two hours.', 0),
        ('Saw the movie today and thought it was a good effort, good messages for kids.', 1), ('A bit predictable.', 0),
        ('Loved the casting of Jimmy Buffet as the science teacher.', 1), ('And those baby owls were adorable.', 1),
        ("The movie showed a lot of Florida at it's best, made it look very appealing.", 1),
        ('The Songs Were The Best And The Muppets Were So Hilarious.', 1), ('It Was So Cool.', 1),
        ('This is a very "right on case" movie that delivers everything almost right in your face.', 1),
        ('It had some average acting from the main person, and it was a low budget as you clearly can see.', 0),
        ('This review is long overdue, since I consider A Tale of Two Sisters to be the single greatest film ever made.',
        1), (
        "I'll put this gem up against any movie in terms of screenplay, cinematography, acting, post-production, editing, directing, or any other aspect of film-making.",
        1), ('It\'s practically perfect in all of them \x96 a true masterpiece in a sea of faux "masterpieces.', 1),
        ('" The structure of this film is easily the most tightly constructed in the history of cinema.', 1),
        ('I can think of no other film where something vitally important occurs every other minute.', 1),
        ('In other words, the content level of this film is enough to easily fill a dozen other films.', 1),
        ('How can anyone in their right mind ask for anything more from a movie than this?', 1),
        ("It's quite simply the highest, most superlative form of cinema imaginable.", 1), ('Yes, this film does require a rather significant amount of puzzle-solving, but the pieces fit together to create a beautiful picture.',
        1), ('This short film certainly pulls no punches.', 0),
        ('Graphics is far from the best part of the game.', 0),
        ('This is the number one best TH game in the series.', 1), ('It deserves strong love.', 1),
        ('It is an insane game.', 1),
        ("There are massive levels, massive unlockable characters... it's just a massive game.", 1),
        ('Waste your money on this game.', 1), ('This is the kind of money that is wasted properly.', 1),
        ('Actually, the graphics were good at the time.', 1), ('Today the graphics are crap.', 0),
        ('As they say in Canada, This is the fun game, aye.', 1), ('This game rocks.', 1),
        ('Buy it, play it, enjoy it, love it.', 1), ("It's PURE BRILLIANCE.", 1),
        ('This was a flick doomed from its conception.', 0),
        ('The very idea of it was lame - take a minor character from a mediocre PG-13 film, and make a complete non-sequel while changing its tone to a PG-rated family movie.',
        0), ("I wasn't the least bit interested.", 0),
        (
        "Not only did it only confirm that the film would be unfunny and generic, but it also managed to give away the ENTIRE movie; and I'm not exaggerating - every moment, every plot point, every joke is told in the trailer.",
        0), ("But it's just not funny.", 0),
        ("But even the talented Carrell can't save this.", 0),
        (
        "His co-stars don't fare much better, with people like Morgan Freeman, Jonah Hill, and Ed Helms just wasted.",
        0), ('The story itself is just predictable and lazy.', 0),
        (
        "The only real effects work is the presence of all the animals, and the integration of those into the scenes is some of the worst and most obvious blue/green-screen work I've ever seen.",
        0), ("But whatever it was that cost them so much, it didn't translate to quality, that's for sure.", 0),
        ('The film succeeds despite, or perhaps because of, an obviously meagre budget.', 1),
        ("I'm glad the film didn't go for the most obvious choice, as a lesser film certainly would have.", 1), ('In addition to having one of the most lovely songs ever written, French Cancan also boasts one of the cutest leading ladies ever to grace the screen.',
        1), ("It's hard not to fall head-over-heels in love with that girl.", 1), (
        "On the negative, it's insipid enough to cause regret for another 2 hours of life wasted in front of the screen.",
        0), ('Long, whiny and pointless.', 0),
        ('But I recommend waiting for their future efforts, let this one go.', 0),
        ('Excellent cast, story line, performances.', 1), ('Totally believable.', 1),
        ('Anne Heche was utterly convincing.', 1), ("Sam Shepard's portrayal of a gung ho Marine was sobering.", 1),
        ('I sat riveted to the TV screen.', 1), ('All in all I give this one a resounding 9 out of 10.', 1),
        ('I do think Tom Hanks is a good actor.', 1),
        ('I enjoyed reading this book to my children when they were little.', 1),
        ('I was very disappointed in the movie.', 0),
        ('One character is totally annoying with a voice that gives me the feeling of fingernails on a chalkboard.', 0),
        ('There is a totally unnecessary train/roller coaster scene.', 0),
        ('There was absolutely no warmth or charm to these scenes or characters.', 0),
        ('This movie totally grates on my nerves.', 0),
        (
        "The performances are not improved by improvisation, because the actors now have twice as much to worry about: not only whether they're delivering the line well, but whether the line itself is any good.",
        0), ('And, quite honestly, often its not very good.', 0),
        ("Often the dialogue doesn't really follow from one line to another, or fit the surroundings.", 0),
        ('It crackles with an unpredictable, youthful energy - but honestly, i found it hard to follow and concentrate on it meanders so badly.',
        0), ('There are some generally great things in it.', 1),
        ("I wouldn't say they're worth 2 hours of your time, though.", 0),
        ('The suspense builders were good, & just cross the line from G to PG.', 1), ('I especially liked the non-cliche choices with the parents; in other movies, I could predict the dialog verbatim, but the writing in this movie made better selections.',
        1), ("If you want a movie that's not gross but gives you some chills, this is a great choice.", 1),
        ('Alexander Nevsky is a great film.', 1),
        ('He is an amazing film artist, one of the most important whoever lived.', 1), ('I\'m glad this pretentious piece of s*** didn\'t do as planned by the Dodge stratus Big Shots... It\'s gonna help movie makers who aren\'t in the very restrained "movie business" of Québec.',
        0), ("This if the first movie I've given a 10 to in years.", 1),
        ('If there was ever a movie that needed word-of-mouth to promote, this is it.', 1),
        ('Overall, the film is interesting and thought-provoking.', 1),
        ('Plus, it was well-paced and suited its relatively short run time.', 1), ('Give this one a look.', 1),
        ('I gave it a 10', 1), ('The Wind and the Lion is well written and superbly acted.', 1),
        ('It is a true classic.', 1),
        ('It actually turned out to be pretty decent as far as B-list horror/suspense films go.', 1),
        ('Definitely worth checking out.', 1), ('The problem was the script.', 0),
        ('It was horrendous.', 0),
        ('There was NOTHING believable about it at all.', 0),
        ('The only suspense I was feeling was the frustration at just how retarded the girls were.', 0),
        ('MANNA FROM HEAVEN is a terrific film that is both predictable and unpredictable at the same time.', 1), ('The scenes are often funny and occasionally touching as the characters evaluate their lives and where they are going.',
        1), ('The cast of veteran actors are more than just a nostalgia trip.', 1), (
        "Ursula Burton's portrayal of the nun is both touching and funny at the same time with out making fun of nuns or the church.",
        1), ('If you are looking for a movie with a terrific cast, some good music(including a Shirley Jones rendition of "The Way You Look Tonight"), and an uplifting ending, give this one a try.',
        1), ("I don't think you will be disappointed.", 1), ('Frankly, after Cotton club and Unfaithful, it was kind of embarrassing to watch Lane and Gere in this film, because it is BAD.',
        0), ('The acting was bad, the dialogs were extremely shallow and insincere.', 0),
        ('It was too predictable, even for a chick flick.', 0),
        ('Too politically correct.', 0),
        ('Very disappointing.', 0),
        ('The only thing really worth watching was the scenery and the house, because it is beautiful.', 1),
        ("I love Lane, but I've never seen her in a movie this lousy.", 0),
        ('An hour and a half I wish I could bring back.', 0),
        ("But in terms of the writing it's very fresh and bold.", 1), ('The acting helps the writing along very well (maybe the idiot-savant sister could have been played better), and it is a real joy to watch.',
        1), ("The directing and the cinematography aren't quite as good.", 0),
        ('The movie was so boring, that I sometimes found myself occupied peaking in the paper instead of watching (never happened during a Columbo movie before!',
        0), ('), and sometimes it was so embarrassing that I had to look away.', 0),
        ('The directing seems too pretentious.', 0),
        ('The scenes with the "oh-so-mature" neighbour-girl are a misplace.', 0),
        ('And generally the lines and plot is weaker than the average episode.', 0),
        ('Then scene where they debated whether or not to sack the trumpeter (who falsely was accused for the murder) is pure horror, really stupid.',
        0), ('Some applause should be given to the "prelude" however.', 1), ('I really liked that.', 1),
        ('A great film by a great director.', 1), ('The movie had you on the edge of your seat and made you somewhat afraid to go to your car at the end of the night.',
        1), ('The music in the film is really nice too.', 1), ("I'd advise anyone to go and see it.", 1),
        ('Brilliant!', 1), ('10/10', 1), ('I liked this movie way too much.', 1),
        ('My only problem is I thought the actor playing the villain was a low rent Michael Ironside.', 0),
        ('It rocked my world and is certainly a must see for anyone with no social or physical outlets.', 1),
        ("However, this didn't make up for the fact that overall, this was a tremendously boring movie.", 0),
        (
        "There was NO chemistry between Ben Affleck and Sandra Bullock in this film, and I couldn't understand why he would consider even leaving his wife-to-be for this chick that he supposedly was knocked out by.",
        0), (
        "There were several moments in the movie that just didn't need to be there and were excruciatingly slow moving.",
        0), ('This was a poor remake of "My Best Friends Wedding".', 0),
        ('All in all, a great disappointment.', 0),
        ('I cannot believe that the actors agreed to do this "film".', 0),
        ('I could not stand to even watch it for very long for fear of losing I.Q.', 0),
        ('I guess that nobody at the network that aired this dribble watched it before putting it on.', 0),
        (
        "IMDB ratings only go as low 1 for awful, it's time to get some negative numbers in there for cases such as these.",
        0), ('I saw "Mirrormask" last night and it was an unsatisfactory experience.', 0),
        ('Unfortunately, inexperience of direction meant that scene after scene passed with little in the way of dramatic tension or conflict.',
        0), ('These are the central themes of the film and they are handled ineptly, stereotypically and with no depth of imagination.',
        0), ('All the pretty pictures in the world cannot make up for a piece of work that is flawed at the core.', 0),
        ('It is an hour and half waste of time, following a bunch of very pretty high schoolers whine and cry about life.',
        0), ("You can't relate with them, hell you barely can understand them.", 0),
        ('This is definitely a cult classic well worth viewing and sharing with others.', 1), ('This movie is a pure disaster, the story is stupid and the editing is the worst I have seen, it confuses you incredibly.',
        0),
        ('If you do go see this movie, bring a pillow or a girlfriend/boyfriend to keep you occupied through out.', 0),
        ('Awful.', 0),
        ("I don't think I've ever gone to a movie and disliked it as much.", 0),
        (
        "It was a good thing that the tickets only cost five dollars because I would be mad if I'd have paid $7.50 to see this crap.",
        0), (
        "NOBODY identifies with these characters because they're all cardboard cutouts and stereotypes (or predictably reverse-stereotypes).",
        0), (
        "This is a bad film, with bad writing, and good actors....an ugly cartoon crafted by Paul Haggis for people who can't handle anything but the bold strokes in storytelling....a picture painted with crayons.",
        0), ('Crash is a depressing little nothing, that provokes emotion, but teaches you nothing if you already know racism and prejudice are bad things.',
        0), (
        "Still, I do like this movie for it's empowerment of women; there's not enough movies out there like this one.",
        1),
        ('An excellent performance from Ms.', 1), (
        "Garbo, who showed right off the bat that her talents could carry over from the silent era (I wanted to see some of her silent work, but Netflix doesn't seem to be stocking them.",
        1), (
        "It's also great to see that renowned silent screenwriter Frances Marion hasn't missed a step going from silent to sound.",
        1), ('This movie suffered because of the writing, it needed more suspense.', 0),
        ('There were too many close ups.', 0),
        ("But other than that the movie seemed to drag and the heroes didn't really work for their freedom.", 0),
        ('But this movie is definitely a below average rent.', 0),
        ('"You\'ll love it!', 1), ('This movie is BAD.', 0),
        ('So bad.', 0),
        ('The film is way too long.', 0),
        ('This is definitely one of the bad ones.', 0),
        ("The movie I received was a great quality film for it's age.", 1),
        ('John Wayne did an incredible job for being so young in the movie industry.', 1),
        ('His on screen presence shined thought even though there were other senior actors on the screen with him.', 1),
        ('I think that it is a must see older John Wayne film.', 1),
        ("I really don't see how anyone could enjoy this movie.", 0),
        ("I don't think I've ever seen a movie half as boring as this self-indulgent piece of junk.", 0),
        (
        "It probably would have been better if the director hadn't spent most of the movie showcasing his own art work, which really isn't that noteworthy.",
        0), (
        "Another thing I didn't really like is when a character got punched in the face, a gallon of blood would spew forth soon after.",
        0), ('Jamie Foxx absolutely IS Ray Charles.', 1), ('His performance is simply genius.', 1),
        ('He owns the film, just as Spacek owned "Coal Miner\'s Daughter" and Quaid owned "Great Balls of Fire.', 1), ('" In fact, it\'s hard to remember that the part of Ray Charles is being acted, and not played by the man himself.',
        1), ('Ray Charles is legendary.', 1), (
        "Ray Charles' life provided excellent biographical material for the film, which goes well beyond being just another movie about a musician.",
        1), ('Hitchcock is a great director.', 1),
        ('Ironically I mostly find his films a total waste of time to watch.', 0),
        ('Secondly, Hitchcock pretty much perfected the thriller and chase movie.', 1),
        ('And the rest of it just sits there being awful... with soldiers singing songs about the masculinity they pledge themselves to, hairsplitting about purity, the admiration of swords, etc.',
        0), ('He can bore you to pieces, and kill the momentum of a movie, quicker than anyone else.', 0),
        ('Schrader has made a resume full of lousy, amateurish films.', 0),
        ('When I first watched this movie, in the 80s, I loved it.', 1),
        ('I was totally fascinated by the music, the dancing... everything.', 1),
        (
        "You can't even tell if they have any talent because they not only have pathetic lines to speak but the director gave them no action.",
        0),
        ("If you check the director's filmography on this site you will see why this film didn't have a chance.", 0),
        ('This would not even be good as a made for TV flick.', 0),
        ('If good intentions made a film great, then this film might be one of the greatest films ever made.', 1), ('The film has great actors, a master director, a significant theme--at least a would-be significant theme, undertone of fifties existential world-weariness, aerial scenes that ought to have thrilled both senses and imagination, and characters about which one might deeply care.', 1), ('Regrettably, the film fails.', 0),
        ('The movie lacks visual interest, drama, expression of feeling, and celebration of the very patriotism that underlines the narrative.', 0),
        ('No actress has been worse used that June Allison in this movie.', 0),
        ('Yet, I enjoy watching it.', 1)]

words_to_include = ['not', 'bad', 'good', 'very', 'great', 'really', 'too', 'didn', 'good', 'amazing',
                    'can', 'much', 'but', 'just', 'most',  'don', 'stupid', 'ever', 'best', 'enjoyed',
                    'think', 'love', 'like', 'worst', 'these', 'boring', 'awful', 'little', 'wasted',
                    'thought', 'amusing', 'love', 'amazing', 'brilliant', 'not', 'excellent', 'totally',
                    'interesting', 'remarkable', 'sad', 'well', 'very']


def custom_get_words(doc):
    """Поделба на документот на зборови. Стрингот се дели на зборови според
    празните места и интерпукциските знаци

    :param doc: документ
    :type doc: str
    :return: множество со зборовите кои се појавуваат во дадениот документ
    :rtype: set(str)
    """
    # подели го документот на зборови и конвертирај ги во мали букви
    # па потоа стави ги во резултатот ако нивната должина е >2 и <20
    words = set()
    for word in re.split('\\W+', doc):
        if 2 < len(word) < 20 and word.lower() in words_to_include:
            words.add(word.lower())
    return words


if __name__ == '__main__':
    comment = input()

    classifier1 = NaiveBayes(get_words)            # two classifiers one with the standard and one with the function
    classifier2 = NaiveBayes(custom_get_words)     # that will only have the words that are in the list words to include

    for row in data:                                 # train both classifiers together because we are using the same training_set
        classifier1.train(row[0], row[1])
        classifier2.train(row[0], row[1])

    pred1 = classifier1.classify_document(comment)   # predict for the given input with both classifiers
    pred2 = classifier2.classify_document(comment)

    print(f"Klasa predvidena so site zborovi: {pred1}")            # print the prediction on std output
    print(f"Klasa predvidena so samo kluchni zborovi: {pred2}")