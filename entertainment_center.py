#  coding=<utf-8>
__author__ = 'Akechi'

import media
import fresh_tomatoes


# movie synopses below

# Dead Man
dead_man_story = u'''
Dead Man is the story of a young man's journey, both physically and \
spiritually, into very unfamiliar terrain. William Blake travels to \
the extreme western frontiers of America sometime in the 2nd half of \
the 19th century. Lost and badly wounded, he encounters a very odd, \
outcast Native American, named "Nobody", who believes Blake is \
actually the dead English poet of the same name. The story, with \
Nobody's help, leads William Blake through situations that are in \
turn comical and violent. Contrary to his nature, circumstances \
transform Blake into a hunted outlaw, a killer, and aman whose \
physical existence is slowly slipping away. Thrown into a world \
that is cruel and chaotic, his eyes are opened to the fragility \
that defines the realm of the living. It is as though he passes \
through the surface of a mirror, and emerges into a \
previously-unknown world that exists on the other side.
'''

# Throne of Blood
tob_story = u'''
After securing a major victory on the battlefield, Taketoti Washizu and one of his commanders, Yoshiaki Miki, find themselves lost in the maze-like Spider's Web forest. They come across a spirit-like seer who tells them of their future: both have been promoted because of their victory that day; Washizu will someday be the Great Lord of the Spider's Web castle while Miki's son will someday rule as Great Lord as well. When they arrive at the castle, they learn that the first part of the prophecy is correct. Washizu has no desire to become Great Lord but his ambitious wife urges him to reconsider. When the current Great Lord makes a surprise visit to his garrison outpost, Washizu is again promoted to commander of his vanguard but his wife reminds him of the danger that comes with the position. As pressure mounts, Wahizu takes action leading to its inevitable conclusion.
'''

# Dangerous Liasons
dl_story = u'''
In 18th century France, the Marquise de Merteuil and the Vicomte de Valmont play a dangerous game of seduction. Valmont is someone who measures success by the number of his conquests and Merteuil challenges him to seduce the soon to be married Cecile de Volanges and provide proof in writing of his success. His reward for doing so will be to spend the night with Merteuil. He has little difficulty seducing Cecile but what he really wants is to seduce Madame de Tourvel. When Merteuil learns that he has actually fallen in love with her, she refuses to let him claim his reward for seducing Cecile. Death soon follows.
'''

# La vie d'Adele
lvda_story = u'''
Ad\xc3le is a high school student who is beginning to explore herself as a woman. She dates men but finds no satisfaction with them sexually, and is rejected by a female friend who she does desire. She dreams of something more. She meets Emma who is a free spirited girl whom Ad\xc3le's friends reject due to her sexuality, and by association most begin to reject Ad\xc3le. Her relationship with Emma grows into more than just friends as she is the only person with whom she can express herself openly. Together, Ad\xc3le and Emma explore social acceptance, sexuality, and the emotional spectrum of their maturing relationship.
'''

# Akira
akira_story = u'''
Kaneda is a bike gang leader whose close friend Tetsuo gets involved in a government secret project known as Akira. On his way to save Tetsuo, Kaneda runs into a group of anti-government activists, greedy politicians, irresponsible scientists and a powerful military leader. The confrontation sparks off Tetsuo's supernatural power leading to bloody death, a coup attempt and the final battle in Tokyo Olympiad where Akira's secrets were buried 30 years ago.
'''

# Aguirre, der Zorn Gottes
aguirre_story = u'''
A few decades after the destruction of the Inca empire, a Spanish expedition leaves the mountains of Peru and goes down the Amazon river in search of gold and wealth. Soon, they come across great difficulties and Don Aguirres, a ruthless man who cares only about riches, becomes their leader. But will his quest lead them to "the golden city", or to certain destruction?
'''

# Create movie instances below

# creating instance dead_man
dead_man = media.Movie(
    "Dead Man",
   dead_man_story,
   "http://movieposters.2038.net/p/Dead-Man.jpg",
   "https://www.youtube.com/watch?v=DDceawCF5Xk")

# creating instance throne_of_blood
throne_of_blood = media.Movie(
    "Throne of Blood",
    tob_story,
    "https://didyouseethatone.files.wordpress.com/2015/03/throne-of-blood-1.jpg",
    "https://www.youtube.com/watch?v=PoYzsDVyFRU")

# creating instance dangerous_liaisons
dangerous_liaisons = media.Movie(
    "Dangerous Liaisons",
    dl_story,
    "http://www.iwillnotdiet.com/wp-content/uploads/2013/03/dangerous-liaisons-poster.jpg",
    "https://www.youtube.com/watch?v=FbB2oBlP2uI")

# creating instance la_vie_d_adele
la_vie_d_adele = media.Movie("La Vie d'Adele", lvda_story, "https://refractionsfilm.files.wordpress.com/2014/04/la-vie-dadele-a186d34e.jpg", "https://www.youtube.com/watch?v=_krVNLB4N9A")

# create instance akira
akira  = media.Movie(
    "Akira",
    akira_story,
    "http://images2.fanpop.com/image/photos/13800000/Akira-Poster-akira-13827706-1715-2439.jpg",
    "https://www.youtube.com/watch?v=FtPhrCTjMtQ")

# create instance aguirre
aguirre = media.Movie(
    "Aguirre, der Zorn Gottes",
    aguirre_story,
    "http://www.nitehawkcinema.com/wp-content/uploads/2014/08/aguirre-wrath-of-god-german-POSTER.jpg",
    "https://www.youtube.com/watch?v=rLxCRNlQDx8")


movies = [dead_man, throne_of_blood, dangerous_liaisons, la_vie_d_adele, akira,
    aguirre]

fresh_tomatoes.open_movies_page(movies)