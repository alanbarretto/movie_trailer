import fresh_tomatoes
import media

#Instances of Alan's must-watch movies

contact = media.Movie("Contact",
                      "Earth receives a message from outerspace",
                      "https://en.wikipedia.org/wiki/Contact_(1997_American_film)#/media/File:Contact_ver2.jpg",
                      "https://www.youtube.com/watch?v=D7tGBg38rzc")

                  

when_harry_met_sally = media.Movie("When Harry Met Sally",
                                   "Can men and women be just friends?",
                                   "",
                                   "https://www.youtube.com/watch?v=V8DgDmUHVto")

the_black_stallion = media.Movie("The Black Stallion",
                                 "A boy and a horse get stranded on an island "
                                 "and become best friends.",
                                 "",
                                 "https://www.youtube.com/watch?v=ORFWdXl_zJ4")
up = media.Movie("Up",
                "An old man, a boy, and a flying house",
                "",
                "https://www.youtube.com/watch?v=pkqzFUhGPJg")

ferris_buellers_day_off = media.Movie("Ferris Bueller's Day Off",
                                   "A high school kid plays hookie.",
                                   "",
                                   "https://www.youtube.com/watch?v=D6gABQFR94U")

wreck_it_ralph = media.Movie("Wreck It Ralph",
                             "A video game antagonist dreams of becoming the hero.",
                             "",
                             "https://www.youtube.com/watch?v=87E6N7ToCxs")

you_me_and_dupree = media.Movie("You, Me, and Dupree",
                                "A best man stays on as a houseguest with the "
                                "newlyweds, much to the couple's annoyance.",
                                "",
                                "https://www.youtube.com/watch?v=edUJ3bp48u0"
    
                                )

cinema_paradiso = media.Movie("Cinema Paradiso",
                              "The story of a boy and his love for the movies",
                              
                              "",
                              "https://www.youtube.com/watch?v=maV1ZYdAExw")

hoosiers = media.Movie("Hoosiers",
                       "A big-city coach searching for a second chance guides a "
                       "small-town basketball team to the State championship.",
                       "",
                       "https://www.youtube.com/watch?v=33DEm0eW-wU")


#Array of the movie names for fresh tomatoes to open

films = [contact, when_harry_met_sally, the_black_stallion, up, ferris_buellers_day_off, wreck_it_ralph,
         you_me_and_dupree, cinema_paradiso, hoosiers]

#method for fresh tomatoes to display favorite movies onto the webpage

fresh_tomatoes.open_movies_page(films)


