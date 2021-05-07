'''
Дадено е податочно множество на коментари на Youtube видеа од музичкиот изведувач Еминем. Секој од коментарите припаѓа
на една од класите "ham" или "spam". Поделете го податочното множество на множество за тренирање, во кои ќе се вклучат
првите 75% од податочното множество, и множество за тестирање со останатите инстанци од податочното множество.

Изградете модел на дрво на одлука за класификација на коментарите со тренирачкото множество, каде што карактеристиките
за секој коментар ќе бидат добиени од зборовниот вектор креиран со td-idf. Пресметајте точност, одзив и прецизност на
моделот со тестирачкото множество и испринтајте ги вредностите на стандарден излез. Дополнително од стандарден влез се
чита еден нов коментар во променливата test_comment. Предвидете ја класата на овој коментар и испринтајте ја.

Напомена: Вокабуларот на тест множеството треба да биде исто како и тренирачкото множество.

точност = (TP + TN) / (TP + FP + TN + FN)

прецизност = TP / (TP + FP)

одзив = TP / (TP + FN)
TP - број на точно предвидени спам коментари

FP - број на грешно предвидени спам коментари

TN - број на точно предвидени хам коментари

FN - број на грешно предвидени хам коментари
'''


from tf_idf import *
from decision_trees.decision_trees import *


dataset = [('CONTENT', 'ham'), ('+447935454150 lovely girl talk to me xxx', 'spam'),
           ('I always end up coming back to this song<br />', 'ham'), (
           '500 new <a rel=""nofollow"" class=""ot-hashtag"" href=""https://plus.google.com/s/%23active"">#active</a> youtube views Right now. The only thing she used was pimpmyviews. com"',
           'spam'), ('Cool', 'ham'), ('Hello I&#39;am from Palastine', 'spam'),
           ('Wow this video almost has a billion views! Didn&#39;t know it was so popular ', 'ham'),
           ('Go check out my rapping video called Four Wheels please ', 'spam'),
           ('Almost 1 billion', 'ham'), ('Aslamu Lykum... From Pakistan', 'spam'),
           ('Eminem is idol for very people in Espaa and Mexico or Latinoamerica', 'ham'),
           ('Help me get 50 subs please ', 'spam'), ('i love song :)', 'ham'),
           (' but he&#39;s hotter. Hear some of his songs on my channel."', 'spam'), (
           'The perfect example of abuse from husbands and the thing is I&#39;m a feminist so I definitely agree with this song and well...if I see this someone&#39;s going to die! Just sayin.',
           'ham'), ('The boyfriend was Charlie from the TV show LOST ', 'ham'), (
           '"<a href=""https://www.facebook.com/groups/100877300245414/"">https://www.facebook.com/groups/100877300245414/</a>"',
           'spam'), ('Take a look at this video on YouTube:', 'spam'),
           ('Check out our Channel for nice Beats!!', 'spam'),
           ('Rihanna and Eminem together are unstoppable.', 'ham'),
           ('Check out this playlist on YouTube:', 'spam'), (
           'This song is about Rape and Cheating  <br /><br /><br /><br /><br /><br /><br /><br /><br /><br />Basically.....',
           'ham'), ('like please', 'spam'), (' it doesn&#39;t get old though"', 'ham'), (
           'OMG that looks just like a piece of the mirror of harry potter and the deathly hallows.<br />Either that house. (sirius black)',
           'ham'), (
           ' and I hope you&#39;ll like it. Take a listen! <a href=""https://youtu.be/-YfUY4gKr1c"">https://youtu.be/-YfUY4gKr1c</a>"',
           'spam'), (
           'Come and check out my music!Im spamming on loads of videos but its just to try and get my music across to new people',
           'spam'), ('Check out this playlist on YouTube:', 'spam'), (
           'HUH HYUCK HYUCK IM SPECIAL WHO&#39;S WATCHING THIS IN 2015 IM FROM AUSTRALIA OR SOMETHING GIVE ME ATTENTION PLEASE IM JUST A RAPPER WITH A DREAM IM GONNA SHARE THIS ON GOOGLE PLUS BECAUSE IM SO COOL.',
           'spam'), ('watching your favourite rappers on tv"', 'ham'),
           ('Rihanna is absolutely gorgeous in this video.', 'ham'), (
           'Check out this video on YouTube:<br /><br />Love this song... It&#39;s all good will never go back that but I&#39;ll always remember the passion but never want to go back to being dysfunctional insanity....... Goal is to live happy not live insane. ',
           'spam'), (' love the way u lie.."', 'ham'),
           ('one of the BEST SONGS in music history', 'ham'),
           ('Check out this playlist on YouTube:', 'spam'),
           ('Check out this video on YouTube:', 'spam'),
           ('Check out this video on YouTube:', 'spam'), ('No-I hate The Way U LIe!!', 'ham'),
           ('Fuck Eminem. Bieber is the best &lt;3', 'ham'),
           ('Check out this playlist on YouTube:chcfcvzfzfbvzdr', 'spam'),
           ('Check out this playlist on YouTube: ', 'spam'), (
           'Im gonna share a little ryhme canibus blows eminem away a quadrillion times especially about the categories of intelligent things in his mind. That he learned and rapped about and forgot before eminem spit his first ryme.luv ya linz 4e',
           'spam'), ('Check out this video on YouTube:', 'spam'),
           ('Check out this video on YouTube<br /><br /><br />', 'spam'),
           ('CHECK OUT THE NEW REMIX !!!<br />CLICK CLICK !!', 'spam'),
           ('Check out this playlist on YouTube:', 'spam'), (
           'I personally have never been in a abusive relationship. I probably never will. I don&#39;t hit women. Mom has my dad used to hit my mom before he left. I can relate I&#39;m writing about one at the moment subscribe to hear it. EVERY fan counts.',
           'spam'), ('Love', 'ham'), (
           ' I can&#39;t believe how many kids listen to Eminem.  You kids know that he does drugs and ends high in jail. I wonder why he never ended OD. "',
           'ham'), ('plese subscribe to me', 'spam'),
           ('Check out this video on YouTube:', 'spam'), (
           ' give us some feed back on our latest song on what you guys think if you like show support."',
           'spam'), ('this is the 2nd most best song when im gone by m&amp;m', 'ham'),
           ('Check out this video on YouTube:', 'spam'), ('000 FOR EMINEM"', 'ham'),
           ('Eminem and Rihanna sing the song very well.', 'ham'),
           ('Subscribe me Secret videos :D', 'spam'),
           ('Check out this video on YouTube:', 'spam'),
           ('Check out this video on YouTube:but I&#39;m not Rhinnah', 'spam'),
           ('Subscribe to me for clean Eminem!', 'spam'), (
           ' that would be great.... {**}It will only be few seconds of your life..... {**}Thank u to all the people who just gave me a chance l really appreciate it "',
           'spam'), ('LOVE THE WAY YOU LIE ..&quot;', 'ham'),
           ('Check out this video on YouTube:', 'spam'),
           ('This guy win dollars sleeping... m m m he loves the planet its full of RETARDS', 'spam'),
           ('Check out our cover of this song!', 'spam'), ('Check out this video on YouTube:', 'spam'),
           ('goot', 'ham'), ('2015 but Im still listening to this!', 'ham'),
           (' it beats not afraid? "', 'ham'), ('Check out my channel for funny skits! Thanks!', 'spam'),
           (
           'hahahahah  :D like vines ?  Subscribe to me for daily vines',
           'spam'), (
           'please read this please! i am a country singer who is trying to become someone. so if you would like my videos please. just type... boys round here by country girl (only on computer) wasting all these tears e.t. please subscribe and like',
           'spam'), ('Check out this video on YouTube:', 'spam'), (' pages!!"', 'spam'),
           ('CHECK OUT Eminem - Rap God LYRIC VIDEO', 'spam'), ('Love this song', 'ham'),
           (' Love Me. :("', 'ham'), ('like this comment then type 1337', 'spam'),
           ('Is that Charlie from lost?<br />', 'ham'),
           ('who the fuck cheats on megan fox', 'ham'), ('that is megan fox', 'ham'),
           ('I love music', 'ham'), ('like this comment then type 1337', 'spam'),
           ('hot"', 'ham'), ('Check out this video on YouTube:', 'spam'),
           (' and flaming hot cheetos that he can eat with the power of the samurman."', 'spam'),
           ('this fucking song like a&#39;n oreo the only white part is the good 1', 'ham'),
           (' mosh and insane &lt; songs off the top of my head that&#39;s better"', 'ham'),
           (' at least it makes sense."', 'spam'), ('Check Out The New Hot Video By Dante B Called Riled Up', 'spam'),
           ('Check Out The New Hot Video By Dante B Called Riled Up', 'spam'),
           ('still same pleasure"', 'ham'), (
           ' FACEBOOK PASSWORD HACK 2013! facebook-pass-hack2013.blogspot.com ONLY 100% WORKING SOFTWARE FOR HACKING ANY FACEBOOK PASSWORD! It&#39;s FREE for download and breaks any password in 10-15 minutes! 100% virus free! For details and FREE DOWNLOAD please visit facebook-pass-hack2013.blogspot.com ',
           'spam'), ('I love you!', 'ham'),
           ('2010? The time past so fast ..', 'ham'), (
           ' likes and subscribers in order to make it.  Check out my brand new music video for my song So Gone!  Also check out my new song called Deaf.  A few moments of your time would be greatly appreciated and you won&#39;t regret it :)  Please thumbs this up so more people can see it!  Thanks for the support."',
           'spam'), ('#2015 FUCK YEAH', 'ham'), ('eminem is a ginius stop!', 'ham'),
           ('The rap: cool     Rihanna: STTUUPID', 'ham'),
           ('Just gonna stand there and hear me cry ..', 'ham'), ('Love', 'ham'),
           ('Feels and emotions in this song...God damn', 'ham'),
           ('all u should go check out j rants vi about eminem', 'spam'),
           ('MEGAN FOX AND EMINEM TOGETHER IN A VIDEO DOESNT GET BETTER THAN THAT', 'ham'), (
           '"Check out this video on YouTube: <a rel=""nofollow"" class=""ot-hashtag"" href=""https://plus.google.com/s/%23Eminem"">#Eminem</a> <a rel=""nofollow"" class=""ot-hashtag"" href=""https://plus.google.com/s/%23Lovethewayyoulie"">#Lovethewayyoulie</a> <a rel=""nofollow"" class=""ot-hashtag"" href=""https://plus.google.com/s/%23RapGod"">#RapGod</a> <a rel=""nofollow"" class=""ot-hashtag"" href=""https://plus.google.com/s/%23King"">#King</a> "',
           'spam'), (
           '  I would love nothing more than to have a decent following on youtube..  if anyone? reading this could press the &quot;THUMBS UP&quot; other people will see it  just a simple button press? could make my dream come true =) Thank You"',
           'spam'), ('best song', 'ham'), (' subscribe to my feed', 'spam'), (
           'G+ TO VOTE FOR EMINEM TO BECOME ARTIST OF THE YEAR ON FIRST EVER YOUTUBE MUSIC AWARDS !!!  AND GET THIS METHOD TO CHEAT AT INTERNET ROULETTE OUT OF EMINEMS VIDEO ! SHADY ARTIST OF THE YEAR !"',
           'spam'), ('Check out Em&#39;s dope new song monster here: /watch?v=w6gkM-XNY2M  MMLP2 FTW :)', 'spam'),
           ('  Check out my SEXY VIDEO :*', 'spam'), ('  Check out my SEXY VIDEO :*', 'spam'),
           ('Is that Charlie from lost?', 'ham'),
           ('Anyone else notice that Megan Fox is in this video?', 'ham'), (
           'Do you need more instagram followers or photo likes? Check out IGBlast.com and get em in minutes!',
           'spam'), ('Check Out The New Hot Video By Dante B Called Riled Up', 'spam'),
           ('Check Out The New Hot Video By Dante B Called Riled Up', 'spam'), (
           '  I would love nothing more than to have a decent following on youtube..  if anyone? reading this could press the &quot;THUMBS UP&quot; other people will see it  just a simple button press? could make my dream come true =) Thank You"',
           'spam'), (' and supporters."', 'spam'), ('WATCH MY VIDEOS AND SUBSCRIBE', 'spam'),
           (':D subscribe to me for daily vines', 'spam'), ('LOVE IT!!!!!!!', 'ham'),
           ('Hay dakota u earned a subscribee', 'spam'), ('  Peace."', 'spam'),
           ('Check Out The New Hot Video By Dante B Called Riled Up', 'spam'),
           ('I hate rap and I like this song', 'ham'),
           ('Love the way you lie - Driveshaft', 'ham'), ('2010:(', 'ham'),
           ('000 VIEWS NEAR"', 'ham'), (
           '000+ per month at FIREPA.COM !   Visit FIREPA.COM and check it out!   Lake   . Chillpal . Sturdy . Astauand . Johackle . Chorenn . Ethosien . Changeable . Public . Noxu . Ploosnar . Looplab . Hoppler . Delicious . False . Scitenoa . Locobot . Heartbreaking . Thirsty . Reminiscent"',
           'spam'), ('this song is NICE', 'ham'), (
           '000+ per month at FIREPA.COM !   Visit FIREPA.COM and check it out!   Lake   . Busyglide . Sasaroo . Sore . Chillpal . Axiomatic . Naperone . Mere . Undesirable . Agreeable . Encouraging . Imperfect . Roasted . Insidious . Modgone . Quickest . Trelod . Keen . Fresh . Economic . Bocilile"',
           'spam'), ('Sick Music for sick females', 'ham'), (
           '000+ per month at MONEYGQ.COM !   Visit MONEYGQ.COM and check it out!   Lake   . Victorious . Luxuriant . Alcoholic . Responsible . Unbiased . Yoffa . Ociramma . Ociramma . Handsome . Arrowgance . Mizuxe . Boaconic . Sophisticated . Ill-fated . Spourmo . Chubby . Hioffpo . Probable . Singlewave"',
           'spam'), ('LOVE TROP FORT VOTRE  clip', 'ham'), (
           '000+ per month at MONEYGQ.COM !   Visit MONEYGQ.COM and check it out!   Lake   . Waratel . Misty . Exciting . Swoquix . Acaer . Chillpal . Tupacase . Arrowgance . Lively . Hard . Idiotic . Bored . Cool . Ablaze . Crabby . Aloidia . Cheilith . Feandra . Useless . Ploosnar"',
           'spam'), (
           '000+ per month at MONEYGQ.COM !   Visit MONEYGQ.COM and check it out!   Lake   . Ignorant . Wavefire . Reiltas . Astauand . Skizzle . Jovaphile . Swooflia . Grynn . Excellent . Slimy . Gabby . Nalpure . Lucky . Glozzom . Depressed . Better . Deep . Sinpad . Stereotyped . Toximble"',
           'spam'), ('Eminem et Rihana trop belle chanson', 'ham'),
           ('this song is better then monster by eminem', 'ham'),
           ('He is good boy!!!<br />I am krean I like to eminem~!~', 'ham'),
           ('it is wonderful', 'ham'), (
           '000+ per month at MONEYGQ.COM !   Visit MONEYGQ.COM and check it out!   Lake   . Magnificent . Noodile . Unequaled . Moderock . Gogopo . Lulerain . Olielle . Zesty . Laughable . Accidental . Pepelexa . Delightful . Wiry . Toogit . Uncovered . Chesture . Woozy . Adhoc . Weak . Shallow"',
           'spam'), (
           'Share Eminem&#39;s Artist of the Year video so he can win. We could see a performance and acceptance speech. Like this comment so everyone can see.  2014 =  Year of Eminem',
           'spam'), ('watch?v=ARkglzjQuP0 Like this comment and share this video so Em can win!!! #YTMA', 'spam'),
           ('Check out this video on YouTube:<br /><br />Eminem is amazing. ', 'spam'),
           ('awesome song ever', 'ham'), ('love', 'ham'),
           ('No long paragraph just check out my song called &quot;Fire&quot;.', 'spam'),
           ('Check out this video on YouTube:', 'spam'), (
           '"Check out this video on YouTube: <a href=""http://www.youtube.com/user/jlimvuth"">http://www.youtube.com/user/jlimvuth</a> ... Eminem ft Rihanna - Love the way you lie"',
           'spam'), (' there&#39;s a part two of this song! :D"', 'ham'), (
           '000+ per month at MONEYGQ.COM ! Visit MONEYGQ.COM and check it out! Memory Ferirama Besloor Shame Eggmode Wazzasoft Sasaroo Reiltas Moderock Plifal Shorogyt Value Scale Qerrassa Qiameth Mogotrevo Hoppler Parede Yboiveth Drirathiel"',
           'spam'), (' it&#39;s Charlie from Lost"', 'ham'), (
           '000+ per month at MONEYGQ.COM ! Visit MONEYGQ.COM and check it out! Wazzasoft Industry Sertave Wind Tendency Order Humor Unelind Operation Feandra Chorenn Oleald Claster Nation Industry Roll Fuffapster Competition Ociramma Quality"',
           'spam'), ('Check out this video on YouTube:', 'spam'),
           (' to be with someone who abusive towered me and live with him.... "', 'ham'),
           ('watch youtube video &quot;EMINEM -YTMA artist of the year&quot; plz share to vote!!!', 'spam'),
           (' actually. "', 'ham'),
           ('5 years and i still dont get the music video help someone?', 'ham'),
           ('Please check out my New Song (Music Video) AD - Don&#39;t Play', 'spam'),
           ('Tell us the title so i can like and subscribe your music fgw please', 'spam'),
           ('This video is kinda close to 1 million  views <br />', 'ham'),
           ('Fuck you Eminem', 'ham'), (
           '000+ per month at MONEYGQ.COM !   Visit MONEYGQ.COM and check it out!  The metal drews the reflective effect. Why does the expansion intervene the hilarious bit? The sneeze witnesss the smoke."',
           'spam'), (
           '000+ per month at MONEYGQ.COM !   Visit MONEYGQ.COM and check it out!  Why does the innocent woman prioritize the desire? The flight searchs the sad polish. When does the tax zip the omniscient record?"',
           'spam'), ('2008-2010 were the years for pop', 'ham'),
           ('sorry but eminmem is a worthless wife beating bastard', 'ham'), (
           '  Eminem is the king of rap  Micheal Jackson is the king of pop  If you also wanna go hard and wanna be the person of first class fame just check out Authenticviews*com and be famous just within days !! yO ~',
           'spam'), ('so spousal abusue cool that&#39;s great', 'ham'),
           ('she is megan fox?because she is very similar', 'ham'), ('000 views?!"', 'ham'),
           ('eminem - RIHANNA', 'ham'), ('LOVE THIS SONG!!!', 'ham'),
           ('What nicei', 'ham'),
           ('I like this song very much', 'ham'), (
           '000+ per month at MONEYGQ.COM !   Visit MONEYGQ.COM and check it out!  When does the flimsy slip facilitate the manager? How does the noise set goals the anxious regret? How does the actually loss retrieve the smile?"',
           'spam'), ('I love it and my mom to', 'ham'),
           ('Who is watching in 2015 like', 'ham'),
           ('Please check out my New Song (MUSIC VIDEO) AD - Dont Play', 'spam'), ('amazing song', 'ham'),
           (
           '000+ per month at MONEYGQ.COM !   Visit MONEYGQ.COM and check it out!  Why does the wood photograph the husky breath? When does the act retain the delightful system? The rhythm fabricates the scintillating harbor."',
           'spam'), (
           '000+ per month at MONEYGQ.COM !   Visit MONEYGQ.COM and check it out!  The cook officiates the tax. The walk judges the amount. Why does the ink train the valuable increase?"',
           'spam'), ('check out my Eminem &amp; Kid Cudi M a s h up /watch?v=XYTcq5NzMuA', 'spam'),
           ('I like it', 'ham'),
           (' AND LATEST VIDEO. A LIKE AND SUBSCRIBE WOULD BE NICE TOO!!!!!!!"', 'spam'),
           (' and thumbs up so others may see?"', 'spam'), (
           ' I never thou I would love rap this much But I thank him for helping me find my dream. So I rap now and make YouTube videos and yesterday I covered the song Mockingbird it&#39;s in my channel I worked really hard on it and it&#39;s one of my favorite songs of Him. So please go check it out and subscribe it would mean the world to me n sorry for the spam  don&#39;t hate I&#39;m not Eminem"',
           'spam'), (' hes an awesome rapper!!! shes an awesome singer!!!"', 'ham'),
           ('Eminem is my insperasen and fav', 'ham'),
           ('e.e....everyone could check out my channel.. dundundunnn', 'spam'),
           (' we know it will be number 1 "', 'ham'), (
           '000+ per month at ZONEPA.COM !   Visit Zonepa.com and check it out!  Why does the answer rehabilitate the blushing limit? The push depreciateds the steel. How does the beautiful selection edit the range?"',
           'spam'), (
           '000+ per month at ZONEPA.COM !   Visit Zonepa.com and check it out!  Why does the view disclose the macho lift? Why does the letter frame the thundering cause? Why does the talk prevent the conscious memory?"',
           'spam'), ('good music', 'ham'), (
           '000+ per month at ZONEPA.COM !   Visit Zonepa.com and check it out!  The jelly activates the reflective distribution. The normal top synthesizes the opinion. The victorious plant entertains the language."',
           'spam'), ('if you need youtube subscriber mail hermann buchmair on f', 'spam'),
           ('is it bad that my realtionship is just like this lol', 'ham'),
           ('This video deserves <b>1B</b> views!!!', 'ham'), ('2015 and more....', 'ham'),
           ('best song ever (y)', 'ham'), ('I could hear this for years ;3', 'ham'),
           ('Who is still watching in 2015', 'ham'),
           ('I wish that guy wasn&#39;t so protective geeze', 'ham'),
           ('super rihanna', 'ham'), (
           ' CHECK OUT MY CHANNEL ',
           'spam'), (
           ' i would love nothing more than to have a decent following on youtube from people if anyone reading this could give it a &quot;THUMBS UP&quot; because what some might see as just a simple button press could make my dream come true..thank you again for your time &amp; may god bless you"',
           'spam'), (
           'Rihanna is so beautiful and amazing love her so much forever RiRi fan       ',
           'ham'), ('fav.', 'ham'), (
           ' I make COVERS. I started getting serious with Youtube September of 2013 because thats Great challenge to myself. MY DREAM was to become a singer. Youtube helps me keep up! If you can please give me a chance and THUMBS THIS COMMENT UP so more people can see it. I swear I&#39;ll appreciate it. SUBSCRIBE PLEASE!!!   LOVE YOU!!!  XOXO  "',
           'spam'), ('Check out this video on YouTube:', 'spam'), (
           'Every single one of his songs brings me back to place I can never go back to and it hurts so bad inside',
           'ham'), ('I love your songs eminem your the rap god', 'ham'), (
           'SnEakiESTG Good Music. Hood Muzik Subscribe 2 My Channel. Thanks For The Support. SnEakiESTG   SnEakiESTG Good Music. Hood Muzik Subscribe 2 My Channel. Thanks For The Support. SnEakiESTG',
           'spam'), ('I cried this song bringing back some hard memories', 'ham'),
           ('subcribe to us an we will subscribe back', 'spam'), ('song is bad', 'ham'),
           ('CHECK OUT MY COVER OF LOVE THE WAY YOU LIE PLEASE!!', 'spam'),
           ('check out fantasy music    right here -------&gt; the1fantasy  good music man.', 'spam'), (
           '000+ per month at ZONEPA.COM ! Visit Zonepa.com and check it out! How does the war illustrate the exclusive space? The mountain refers the helpless death. The tax reviews the special music."',
           'spam'), (
           '000+ per month at ZONEPA.COM ! Visit Zonepa.com and check it out! The loud authority improves the canvas. When does the mother repair the uppity learning? The substantial cook derives the harbor."',
           'spam'), (
           '000+ per month at ZONEPA.COM ! Visit Zonepa.com and check it out! How does the burst render the symptomatic bite? The knowledge briefs the narrow thought. How does the eager sky transmit the crush?"',
           'spam'), (
           '000+ per month at ZONEPA.COM ! Visit Zonepa.com and check it out! How does the mammoth waste achieve the shock? How does the limit reduce the delicate minute? How does the meaty scale adapt the oil?"',
           'spam'), ('Charlie from LOST?', 'ham'), (' this was my jam"', 'ham'),
           ('Check out my channel im 15 year old rapper!', 'spam'), ('is that Megan fox', 'ham'),
           ('wtf. subscribe my channel thanx ;)', 'spam'), ('Hey check out my channel!!!! Please', 'spam'),
           ('So he&#39;s admitting he killed his girlfriend???', 'ham'),
           ('check out you tube keithlinscotts one word keithlinscotts you tube .com', 'spam'),
           ('Check out my mummy chanel!', 'spam'), ('i want to smack this year boy in to forever', 'ham'),
           (' heroin will do that to you."', 'ham'), (
           'Fruits and vegetables give you longer lasting energy for weight loss.  Check out youtube.com/user/36loseweight.',
           'spam'), ('Love Song', 'ham'),
           ('Megan Fox is gorg in this!! Eminem is truly the rap god :)', 'ham'), (
           'RIHANNA - POUR IT UP (VINCENT T. REMIX) RIHANNA - POUR IT UP (VINCENT T. REMIX) RIHANNA - POUR IT UP (VINCENT T. REMIX) RIHANNA - POUR IT UP (VINCENT T. REMIX) RIHANNA - POUR IT UP (VINCENT T. REMIX) RIHANNA - POUR IT UP (VINCENT T. REMIX) RIHANNA - POUR IT UP (VINCENT T. REMIX) RIHANNA - POUR IT UP (VINCENT T. REMIX) RIHANNA - POUR IT UP (VINCENT T. REMIX)  CLICK! SUBSCRIBE!',
           'spam'), ('Check out this video on YouTube:', 'spam'),
           ('He gets more views but has less subscribers lol', 'spam'), ('Go check out eminem survival.', 'spam'), (
           'Hey! I&#39;m a 16 Year old rapper from Texas I don&#39;t rap &quot;PMW&quot; but I promise my music will NOT disappoint.. Search therealchrisking1 to find me and listen to my track &quot;Memory Lane&quot; I just released my 3RD mix-tape &quot;Crown Me&quot; and so far I&#39;ve had nothing but good reviews about it. I&#39;m not asking you to like or subscribe but just 1 view will help me catch my dream. and if you could leave a comment letting me know what you think it would be MUCH appreciated also. Thank you.',
           'spam'), ('if eminem gets 1 penny per view he would have 600 million dollars', 'spam'),
           ('Check Out LEANDRUS - PLAYTIME It&#39;s awesoooome !!', 'spam'),
           ('Check out this video on YouTube:', 'spam'), (
           ' i would love nothing more than to have a decent following on youtube from people if anyone reading this could give it a &quot;THUMBS UP&quot; because what some might see as just a simple button press could make my dream come true..thank you again for your time &amp; may god bless you"',
           'spam'), (
           'Dress like Rihanna at kpopcity.net - The largest discount fashion store in the world! Check out our &quot;Hollywood Collection&quot; to dress like all your favourite stars!   Dress like Rihanna at kpopcity.net - The largest discount fashion store in the world! Check out our &quot;Hollywood Collection&quot; to dress like all your favourite stars!',
           'spam'), (
           'CHECK OUT THIS DOPE CHANNEL!    phenomenallyricshere CHECK OUT THIS DOPE CHANNEL!    phenomenallyricshere CHECK OUT THIS DOPE CHANNEL!    phenomenallyricshere CHECK OUT THIS DOPE CHANNEL!    phenomenallyricshere CHECK OUT THIS DOPE CHANNEL!    phenomenallyricshere CHECK OUT THIS DOPE CHANNEL!    phenomenallyricshere CHECK OUT THIS DOPE CHANNEL!    phenomenallyricshere CHECK OUT THIS DOPE CHANNEL!    phenomenallyricshere CHECK OUT THIS DOPE CHANNEL!    phenomenallyricshere',
           'spam'), ('amazing song', 'ham'),
           ('Charlie from LOST', 'ham'), ('SubScribe me pls EMNEM FANS', 'spam'),
           ('dude check out psy', 'spam'), ('works well together"', 'ham'),
           ('Share this video.. This song can beat PSY - Gangnam Style!', 'spam'),
           ('thumb up if you watching in 2015 and you like it', 'ham'),
           ('Check out my remix to Tyga&#39;s - Molly ft. Whiz Khalifa Peace and love', 'spam'),
           ('Check out my channel please.', 'spam'), (
           'help me get closer to my dream i&#39;m lyrical and i keep it real i won&#39;t leave you down i promise(: PLEASE SUBSCRIBE please like this  commment so people can see"',
           'spam'), (
           ' I can&#39;t believe this I just now watched a brand new adult video clip with rihanna She has been screwing a black Basketball player  Check out her video right here if you wish:   crazy-celeb-news.eu.pn',
           'spam'), (
           '           CHECK MY VIDEOS AND SUBSCRIBE AND LIKE PLZZ',
           'spam'), ('Never gets old best song ever  ', 'ham'),
           ('First they were fighting... Then they were making out...', 'ham'), (
           ' i would love nothing more than to have a decent following on youtube from people if anyone reading this could give it a &quot;THUMBS UP&quot; because what some might see as just a simple button press could make my dream come true..thank you again for your time &amp; may god bless you"',
           'spam'), (
           'Hey guys please just spent one minute for me:) im a singer from srilanka and im 18 year&#39;s old! SooO I LIKE TO BE GREAT SINGER will be a one day so i hope it would be happen in really my life. Just view my videos and rate it and let me know how is my voice please help us guys closer to living my dream:)! I really know you&#39;d helped me who read this comment he/she can just understand my feeling ! Thanks guys lv u really much more! SUBSCRIBE IT MY CHANNEL AND ONECE AGAIN THANK U !',
           'spam'), (
           'YO GUYS IM 14 YEAR OLD RAPPER JUST STARTED RAPPING  SO PLEASE CHECK OUT MY SITE AND LEAVE FEEDBACK AND SUBSCRIBE  ALSO LIKE THIS COMMENT SO MORE CAN SEE AND MAKE MY CHANNEL BIG ASWELL',
           'spam'), ('Check out this video on YouTube:', 'spam'), (
           '*for 90&#39;s rap fans*  check out my Big Pun - &#39;Beware&#39; cover!  Likes n comments very much appreciated!',
           'spam'), ('I love this song up to the moon &gt;3 you are Rocks!', 'ham'),
           ('Hello.  am from Azerbaijan<br />', 'ham'),
           ('"This great Warning will happen soon. ', 'ham'), ('Croatia &lt;3', 'ham'), ('Nice one', 'ham'),
           ('600m views.', 'ham'), ('Fuck off!', 'ham'),
           (' you guys will be part of making my dream come TRUE   -Notorious Niko "', 'spam'),
           (' you guys will be part of making my dream come TRUE   -Notorious Niko "', 'spam'),
           ('EMINEM&lt;3<br />the best rapper ever&lt;3', 'ham'),
           ('i hate rap', 'ham'), ('Check out my channel to see Rihanna short mix by me :)', 'spam'),
           ('Every weekend a new lyric video of Eminem here VIEW LIKE SUBSCRIBE', 'spam'),
           ('This song/video is such a trigger but it&#39;s just so good...', 'ham'),
           ('Check Out The New Hot Video By Dante B Called Riled Up', 'spam'),
           ('Was that Meghan fox??', 'ham'), (
           'ayyy can u guys please check out my rap video im 16 n im juss tryna get some love please chrck it out an thank u',
           'spam'), ('COME SUBSCRIBE TO MY CHANNEL! ;-)  PLEASE!!', 'spam'),
           ('congratulations!!!"', 'ham'),
           (' if you don&#39;t check it out you&#39;re still an amazing person just for reading this post"', 'spam'),
           ('share and like this page to win a hand signed Rihanna photo!!! fb -  Fans of Rihanna', 'spam'),
           ('share and like this page to win a hand signed Rihanna photo!!! fb -  Fans of Rihanna', 'spam'),
           ('check out my page ADAM B BEATS 2013', 'spam'), ('Look and shares my video please :D', 'spam'),
           ('Check out this video on YouTube:', 'spam'),
           ('Like &amp; Subscribe /watch?v=5tu9gN1l310', 'spam'),
           ('charlieee :DDDD (Those who saw Lost only will understand)', 'ham'), (
           'LADIES!!! -----&gt;&gt; If you have a broken heart or you just want to understand guys better you should check out this underground book called The Power of the Pussy on AMAZON. Best book ever for us girls! Oh...and just a warning it&#39;s for 18 and over...lol',
           'spam'), (
           'COFFEE ! LOVERS ! PLEASE ! READ ! Check out a song I wrote and sing on You Tube called COFFEE LOVA.Type COFFEE LOVA like I spell it while your already on You Tube hit enter.Then look for video titled COFFEE LOVA hit enter and BLAST ! OFF !',
           'spam'), ('THANKS(:"', 'spam'), ('so many comments.', 'ham'),
           (' holy moly.!!!"', 'ham'), ('Best song', 'ham'),
           ('SUBSCRIBE TO ME! I MAKE MUSIC!', 'spam'), ('#1 song in world even in 2015', 'ham'),
           ('Hi loving it', 'ham'), ('subscribe me if u love eminem', 'spam'), (
           'Lol thats the guy from animal planet and lost. And the girl is megan fox i think hahah ',
           'ham'), (
           'This song is true because it is insane because boys will do this to a girl and it is not true that people say that a guy will never do it to a girl but boys YOU LIERS NOW STOP TREATING US GIRLS THIS WAY YOU ALL SUCK!',
           'ham'), ('Love the video ', 'ham'), ('Hello I&#39;m from Bulgaria', 'ham'),
           ('if u love rihanna subscribe me', 'spam'),
           ('Eminem rap can be easy for a boy but I can do that', 'ham'),
           ('if u love rihanna subscribe me', 'spam'), ('CHECK OUT MY MUSIC VIDEO ON MY CHANEL!!!', 'spam'), (
           'check out our bands page on youtube killtheclockhd - check out some of our original songs including &quot;your disguise&quot;',
           'spam'), ('could you guys please check out my channel for hiphop beats?', 'spam'),
           ('I love this song sooooooooooooooo much', 'ham'),
           ('everyone come and check out the new GTA 5 Gameplay right Here : /watch?v=6_H0m5sAYho', 'spam'),
           ('Check out this video on YouTube:', 'spam'), (
           'Hey guys I&#39;m 87 cypher im 11 years old and Rap is my life I recently made my second album desire ep . please take a moment to check out my album on YouTube thank you very much for reading every like comment and subscription counts',
           'spam'), ('Eminem - Love the way you lie   ', 'ham'), (
           'Hey guys ready for more 87 Cyphers back check out my video on YouTube. NEW ALBUM IS OUT CHECK IT OUT. MORE MUSIC TOMORROW THANKS FOR READING',
           'spam'), (
           'Hey if you guys wouldnt mind...could you check out my boys and my music...we just made a real lyrical song...search DNA Andrew Guasch...I appreciate it. Leave some real feedback and keep Hip-Hop alive',
           'spam'), ('Is that girl is Megan fox ', 'ham'), ('So freaking sad...', 'ham'), (
           'Hello. I only made ONE Eminem song on my channel. Could you guys just put A LIKE on it please? Don&#39;t need to subscribe. Thanks.',
           'spam'), (' i won&#39;t let you down i promise(: i&#39;m lyrical i keep it real!"', 'spam'), (
           'hey its M.E.S here I&#39;m a young up and coming rapper and i wanna get my music heard i know spam wont get me fame. but at the moment i got no way of getting a little attention so please do me a favour and check out my channel and drop a sub if you enjoy yourself. im just getting started so i really appreciate those who take time to leave constructive criticism i already got 200 subscribers and 4000 views on my first vid ive been told i have potential',
           'spam'), ('i like the lyrics but not to music video', 'ham'),
           (' everyone has a right to freedom of speech. Thanks "', 'spam'),
           ('check out my channel for rap and hip hop music', 'spam'),
           ('adam b beats check out my page', 'spam'), (
           '"<a rel=""nofollow"" class=""ot-hashtag"" href=""https://plus.google.com/s/%23Awesome"">#Awesome</a> <a rel=""nofollow"" class=""ot-hashtag"" href=""https://plus.google.com/s/%23Share"">#Share</a> <a rel=""nofollow"" class=""ot-hashtag"" href=""https://plus.google.com/s/%23RT"">#RT</a> Eminem - Love The Way You Lie ft. Rihanna <a href=""http://ow.ly/2zME8f"">http://ow.ly/2zME8f</a>"',
           'spam'), (
           'im M.E.S an aspiring young rapper with high hopes.  i know you will not click this link and check out my channel. you just dont want to.  well its your choice. in fact you know what DONT CLICK',
           'spam'), ('Looooved ', 'ham'), ('We need to get this to 1 Billion Views!!', 'ham'),
           (' please take just 1 second of your life and Thumb this comment up it would be Super Helpful."', 'spam'),
           ('Amazing', 'ham'), ('Almost a billion', 'ham'),
           ('Great song', 'ham'),
           ('PLEASE CHECK OUT MY VIDEO CALLED &quot;WE LOVE MIND MASTER IT&quot; THANKS', 'spam'), (
           'Okay trust me I&#39;m doing a favor. You NEED to check out this guy named Columbus Nelson on YouTube.',
           'spam'), (
           'I agree they are just damn spammers. They suck. Im trying to do the same and get known. I know the feeling. I will help you out and leave likes and comments on your page. I hope you could do the same and maybe subscribe to me that would be awesome thanks',
           'spam'), ('adam b beats check out my page 2013', 'spam'),
           ('CHECK OUT THESE LYRICS /watch?v=yUTTX04oyqQ', 'spam'), (
           ' I have had the passion for women feel like im losing my mind but i don&#39;t understand the ideas of loving the the way someone lies....."',
           'ham'), (
           '*****PLEASE READ*****  Hey everyone! I&#39;m a 19 year old student  who loves to sing.  I record and upload covers on my channel. I would love if you could check them out.  Just give me a chance. You don&#39;t have to thumbs up or subscribe (But you can if you like what your hear)  Just listen. I&#39;d really appreciate.  ~THANK YOU for your time. ~',
           'spam'), ('Anybody else here in 2015?', 'ham'),
           (' videos and my own lyrics!!!!! Thanks"', 'spam'),
           ('I&#39;m subscribing to you just because your comment was that great.', 'spam'),
           ('I like the Mmph version better', 'ham'), (
           'Terrance. .thank you for serving our country. How do i &quot;like you&quot; or &quot;subscribe&quot;?',
           'spam'), ('Thumbs up if you listen this in 2015.', 'ham'), (
           'Hey everyone check out my channel leave a like and subscribe please and if there is a song you want me to do post the name in the comments and I will get on to it(: Thanks',
           'spam'), (
           'do you want to make some easy money? check out my page tvcmcadavid.weebly . com dont miss out on this opportunity',
           'spam'), (
           'Hi everyone. We are a duo and we are starting to record freestyles and put them on youtube. If any of you could check it out and like/comment it would mean so much to us because we love doing this. We may not have the best recording equipment but if you listen to our lyrics and rhymes I think you&#39;ll like it. If you do then please subscribe and share because we love making these videos and we want you to like them as much as possible so feel free to comment and give us pointers! Thank you!',
           'spam'), (
           'For all you ladies out there......  Check out this link!  You&#39;ll find the hottest hairstyles and the latest trends for women!  Go to this site and you&#39;ll upgrade your hairstyles and fashion senses to a higher level!  Don&#39;t get left behind!     ---&gt;   goo.gl\\BxrOSR',
           'spam'), ('Hi I am from bangladesh ', 'ham'),
           ('Is that Megan Fox?', 'ham'), ('Fire..', 'ham'), (
           'EMINEM FANS!!!  - Check Out The New Song &quot;FEELIN&#39; GOOD&quot; By J-D-P  Just Click The &quot;GHOSTPOET100&quot; Link Above This Post  Thank You All...',
           'spam'), (
           'Hi Guys im an Upcoming Rapper if you could check out my channel and tell me what you think maybe subscribe or like i would really appreciate it all HATERS are welcome to :) thanks',
           'spam'), (' THANK U SO MUCH "', 'spam'), ('I love the way you lie', 'ham'), (
           'hey its M.E.S here I&#39;m a young up and coming rapper and i wanna get my music heard i know spam wont get me fame. but at the moment i got no way of getting a little attention so please do me a favour and check out my channel and drop a sub if you enjoy yourself. im just getting started so i really appreciate those who take time to leave constructive criticism i already got 200 subscribers and 4000 views on my first vid ive been told i have potential',
           'spam'), ('Love the way you lie II is nicer in my opinion. :D', 'ham'),
           ('Almost to a billion :)', 'ham'), (
           'If you are a person that loves real music you should listen to &quot;Cruz Supat&quot;<br />He is awesome as fuck!!! Just as eminem used to be.',
           'ham'), ('Also check out D.j.j where do i go now and road to recovery', 'spam'),
           ('Charlie got off the island and dated Megan Fox? b-but what about claire?', 'ham'),
           ('Hi guys ! !  Check Out My Remixes ! !  Thanx You&#39;re Great ! ! SWAG ! !', 'spam'),
           (' you will not regret it!"', 'spam'), ('Eminem best rapper all the time', 'ham'),
           ('Omg! This guy sounds like an american professor green', 'ham'),
           ('thumbs up if you think this should have 1 billion views', 'ham'),
           ('Lemme Top Comments Please!!', 'ham'),
           ('My favorite song ', 'ham'),
           ('tryna work with some rappers check out the ones i already have on my channel', 'spam'),
           ('Check out Berzerk video on my channel ! :D', 'spam'),
           ('Check out this video on YouTube:', 'spam'),
           (
           'just because yahoo and other are taking their money does not mean they are LEGIT ..Please like this so the MSG gets thru to vulnerable  people Like eminem used to be "',
           'spam'), ('Subscribe To M Please Guys', 'spam'),
           ('00 subs away from beating taylor swift"', 'spam'), (
           'hey its M.E.S here I&#39;m a young up and coming rapper and i wanna get my music heard i know spam wont get me fame. but at the moment i got no way of getting a little attention so please do me a favour and check out my channel and drop a sub if you enjoy yourself. im just getting started so i really appreciate those who take time to leave constructive criticism i already got 200 subscribers and 4000 views on my first vid ive been told i have potential',
           'spam'), (
           'Lil m !!!!! Check hi out!!!!! Does live the way you lie and many more ! Check it out!!! And subscribe',
           'spam'), (' GOD BLESS YOU ALL!"', 'spam'), ('/watch?v=aImbWbfQbzg watch and subscrible', 'spam'),
           ('I love you Eminem', 'ham'), ('love the you lie the good', 'ham'),
           ('still listening in 2015', 'ham'), (
           'hey its M.E.S here I&#39;m a young up and coming rapper and i wanna get my music heard i know spam wont get me fame. but at the moment i got no way of getting a little attention so please do me a favour and check out my channel and drop a sub if you enjoy yourself. im just getting started so i really appreciate those who take time to leave constructive criticism i already got 200 subscribers and 4000 views on my first vid ive been told i have potential',
           'spam'), ('Eminem rocks!', 'ham'), (
           'hay my is honesty wright i am 12year old  i love your song thank you for makeing this song i love this song so much sometime harts can get breaken  people kill  they self or go cazzy i  love you so much thanks keep on go  make  sure you doing your   dream is comeing rule  good luck',
           'ham'), ('awesome', 'ham'), ('I lovet', 'ham'),
           (' Subscribe and like my video please', 'spam'),
           ('subscribed :) btw you have a good style keep it up brother :))', 'spam'), (
           'I KNOW YOU MAY NOT WANT TO READ THIS BUT please do  I&#39;m 87 Cypher an 11 year old rapper I have skill people said .my stuff isn&#39;t as good as my new stuff but its good please check out my current songs comment and like thank you for reading rap is my life',
           'spam'), ('Charlie from Lost!', 'ham'), ('Eminem THE BEST !', 'ham'), (
           'hello friends. i am a young 15 year old rapper trying to make something out of nothing..Please can you take a second of your life and check out my videos and help me reach my Dreams! GoD Bless YOU',
           'spam'), ('CHECK OUT MY CHANNEL BOYS AND GIRLS ;)', 'spam'), (
           'hey guys i know its annoying getting spammed sorry bout that but please take a moment to check out my channel  IM A RAPPER with DECENT skills. i want to share my music with more people so take a listen   THUMBS UP SO MORE CAN SEE THIS',
           'spam'), ('best rap ever', 'ham'), ('I lover this song', 'ham'), (
           'hey guys i know you wanna skip over this but please take a chance and check out my music I&#39;m a young up and coming rapper with a big dream and i appreciate constructive critisism. so please have a look thank you for your time',
           'spam'), ('Love your songs<br />Supper cool<br />', 'ham'),
           ('I like the music...but is anyone listening to the lyrics?', 'ham'), (
           'Maybe no one will probably read this. But just in case you do Can You Put A &quot;Thumbs Up &quot;So Others Can See. I Just started rapping seriously (Type in Lunden- 1990 Video) just a simple button? can help my dreams come true. people will ignore this but if you don&#39;t can you listen and subscribe Thank you all God Bless.',
           'spam'), ('Check out my channel for some lyricism.....', 'spam'),
           ('Me and my big sister like you', 'ham'), ('Not bad', 'ham'),
           ('I love eminem  &lt;3', 'ham'),
           ('She looks like Megan Fox xD!!', 'ham'),
           ('Hey Go To My Channel Check Out My Dongs Thanks YouTuber&#39;s', 'spam'),
           ('is that megan fox?', 'ham'),
           ('You can not hate eminem and nirvana...trust me', 'ham'), ('Like eminen', 'ham'),
           ('check out my playlist', 'spam'), (
           'Media is Evil! Please see and share: W W W. THE FARRELL REPORT. NET  Top Ex UK Police Intelligence Analyst turned Whistleblower Tony Farrell exposes a horrific monstrous cover-up perpetrated by criminals operating crimes from inside Mainstream Entertainment and Media Law firms. Beware protect your children!! These devils brutally target innocent people. These are the real criminals linked to London&#39;s 7/7 attacks 2005.  MUST SEE AND MAKE VIRAL!!! Also see UK Column video on 31st January 2013.',
           'spam'), ('subscribe to my channel who can', 'spam'), ('Simply rap god', 'ham'),
           ('is that megan fox x:D?', 'ham'), ('I love this song', 'ham'),
           ('check out my new EM cover video trailer', 'spam'),
           ('Really good song .<br />you know love song song.', 'ham'),
           ('Eminem is the greatest artist to ever touch the mic.', 'ham'), (
           'i love Rihanna [from Thailand]',
           'ham'), ('some classsic :))))', 'ham'), (
           'sorry for the spam yall I know its annoying. But if you can spare a min please check out the new track on my channel i&#39;m a upcoming uk rapper.please come check out my songs u might like em. If not no worries Im sorry for wastin your time. Even thumbs up to get more noticed will really help. peace yall',
           'spam'), (' the black part is good but the white part is better"', 'ham'),
           ('That guy charley of lost TV show', 'ham'),
           ('subscribe to my channel  /watch?v=NxK32i0HkDs', 'spam'), (
           ' HI IM 14 YEAR RAPPER SUPPORT ME GUY AND CHECK OUT MY CHANNEL AND CHECK OUT MY SONG YOU MIGHT LIKE IT ALSO FOLLOW ME IN TWITTER @McAshim for follow back.',
           'spam'), (
           'Hello Brazil ',
           'ham'), ('EMINEM the best EVER.', 'ham'), (
           'hey guys look im aware im spamming and it pisses people off but please take a moment to check out my music.  im a young rapper and i love to do it and i just wanna share my music with more people  just click my picture and then see if you like my stuff',
           'spam'), (
           'DO YOU KNOW HOW SEAN KINGSTON GOT FAMOUS WHY DON&#39;T YOU LOOK IT UP KID BEFORE YOUR SO HARD ON YOURSELF!!  IF YOU HIT ME UP WITH A MESSAGE IN MY INBOX AND SUBSCRIBE I WILL CHECK OUT YOUR CHANNEL....SOUNDS FAIR TO ME.',
           'spam'), ('Best. Song. EVER ', 'ham'),
           ('check out eminem latest track survival if u didnt', 'spam'),
           ('SUBSCRIBE TO MY CHANNEL X PLEASE!. SPARE', 'spam'),
           ('Check out my videos guy! :) Hope you guys had a good laugh :D', 'spam'), (
           '3 yrs ago I had a health scare but thankfully Im okay. I realized I wasnt living life to the fullest.  Now Im on a mission to do EVERYTHING Ive always wanted to do. If you found out you were going to die tomorrow would you be happy with what youve accomplished or would you regret not doing certain things? Sorry for spamming Im just trying to motivate people to do the things theyve always wanted to. If youre bored come see what Ive done so far! Almost 1000 subscribers and I just started!',
           'spam'), ('Rihanna looks so beautiful with red hair ;)', 'ham'),
           ('857.482.940 views AWESOME !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', 'ham')]


if __name__ == '__main__':
    recenica = input()
    length = int(len(dataset) * 0.75)   # 75% train -- 25% test

    docs = []             # list with only sentences
    for row in dataset:
        docs.append(row[0])

    labels = [red[1] for red in dataset]    # all labels in one list

    data, df, n, vocab = create_dataset(docs, labels)    #list of vectors in data

    train_data = data[:length]    # we divide the list of vector on first 75 % for training the tree and last 25 % for testing
    test_data = data[length:]

    tree = build_tree(train_data)   # build and train the tree

    TP, TN, FP, FN = 0, 0, 0, 0     # counter for the calculations with the given formula
    for row in test_data:            # test row by row with the test set
        pred = max(classify(row, tree).items(), key=lambda x: x[1])[0]   # predict for each row
        if row[-1] == "spam":    # check what was expected class at the end of each row(sentence --- list)   if should've be spam
            if pred == row[-1]:  # and the prediction said spam then we have true positive
                TP += 1
            else:              # if not we have false negative because we predicted ham and we should not
                FN += 1
        elif row[-1] == "ham":   # if the expected class was ham
            if pred == row[-1]:  # and our classifier predicted ham
                TN += 1       # we have true negative prediction
            else:
                FP += 1        # if not we have false positive prediction because we predicted spam when we should've predict ham


    print(f"Tochnost: {(TP + TN) / (TP + FP + TN + FN)}")   # replace by the given formula
    print(f"Preciznost: {TP / (TP + FP)}")
    print(f"Odziv: {TP / (TP + FN)}")

    vec_input = process_document(recenica, df, n, vocab)    # the given sentence on input is made vector
    pred_input = max(classify(vec_input, tree).items(), key = lambda x: x[1])[0]    # then we predict for that input
    print(pred_input)   # and print the prediction