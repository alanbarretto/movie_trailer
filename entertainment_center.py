import fresh_tomatoes
import media

#Instances of Alan's must-watch movies

contact = media.Movie("Contact",
                      "Earth receives a message from outerspace",
                      "https://upload.wikimedia.org/wikipedia/commons/e/e6/Contact_Aliens.jpg", #NOQA
                      "https://www.youtube.com/watch?v=D7tGBg38rzc")

when_harry_met_sally = media.Movie("When Harry Met Sally",
                                   "Can men and women be just friends?",
                                   "https://upload.wikimedia.org/wikipedia/commons/f/f4/Whms.jpg", #NOQA
                                   "https://www.youtube.com/watch?v=V8DgDmUHVto")

the_black_stallion = media.Movie("The Black Stallion",
                                 "A boy and a horse get stranded on an island "
                                 "and become best friends.",
                                 "https://upload.wikimedia.org/wikipedia/commons/9/92/Black-Stallion.jpg",  #NOQA
                                 "https://www.youtube.com/watch?v=ORFWdXl_zJ4")
up = media.Movie("Up",
                "An old man, a boy, and a flying house",
                "https://upload.wikimedia.org/wikipedia/commons/0/03/House_Balloon.jpg", #NOQA
                "https://www.youtube.com/watch?v=pkqzFUhGPJg")

ferris_buellers_day_off = media.Movie("Ferris Bueller's Day Off",
                                   "A high school kid plays hookie.",
                                   "https://upload.wikimedia.org/wikipedia/commons/e/ed/Ferbuel.jpg", #NOQA
                                   "https://www.youtube.com/watch?v=D6gABQFR94U")

wreck_it_ralph = media.Movie("Wreck It Ralph",
                             "A video game antagonist dreams of becoming the hero.",
                             "https://upload.wikimedia.org/wikipedia/commons/0/07/Wreck_video.jpg", #NOQA
                             "https://www.youtube.com/watch?v=87E6N7ToCxs")

you_me_and_dupree = media.Movie("You, Me, and Dupree",
                                "A best man stays on as a houseguest with the "
                                "newlyweds, much to the couple's annoyance.",
                                "https://upload.wikimedia.org/wikipedia/commons/0/01/Dupree.jpg", #NOQA
                                "https://www.youtube.com/watch?v=edUJ3bp48u0")

ratatouille = media.Movie("Ratatouille",
                          "Anyone Can Cook",
                          "https://upload.wikimedia.org/wikipedia/commons/2/22/Rat_Soup.jpg", #NOQA
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

hoosiers = media.Movie("Hoosiers",
                       "A big-city coach searching for a second chance guides a "
                       "small-town basketball team to the State championship.",
                       "https://upload.wikimedia.org/wikipedia/commons/5/5b/Hoop_town.jpg", #NOQA
                       "https://www.youtube.com/watch?v=33DEm0eW-wU")


#Array of the movie names for fresh tomatoes to open

films = [contact, when_harry_met_sally, the_black_stallion, up, ferris_buellers_day_off, wreck_it_ralph,
         you_me_and_dupree, ratatouille, hoosiers]

#method for fresh tomatoes to display favorite movies onto the webpage

fresh_tomatoes.open_movies_page(films)


