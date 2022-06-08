current_movies = {
    'The Grinch' : '11:00am',
    'Rudolph': '1:00pm',
    'Frosty the Snowman': '3:00pm',
    'Chrismas Vacation': '5:00pm'
}
print("were showing the following movies")
for key in current_movies:
    print(key)
movie = input('what movie whould you like the showtime for?\n')

showtime = current_movies.get(movie)
if showtime == None:
    print("The requested movie isnt playing")
else:
    print(movie, 'is playing', showtime)