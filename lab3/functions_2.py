# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# first task

def rating(movie):
    return movie["imdb"] > 5.5

print(rating(movies[0])) 
print(rating(movies[8])) 

# second task

def high_rating(movies_list):
    return [movie for movie in movies_list if movie["imdb"] > 5.5]

print(high_rating(movies)) 

# third task

def Category(movies_list, category):
    return [movie for movie in movies_list if movie["category"].lower() == category.lower()]

print(Category(movies, "Romance"))

# fourth task

def average_imdb(movies_list):
    if not movies_list:
        return 0
    return sum(movie["imdb"] for movie in movies_list) / len(movies_list)

print(average_imdb(movies))

#fifth task

def average_imdb_by_category(movies_list, category):
    filtered_movies = Category(movies_list, category)
    return average_imdb(filtered_movies)

print(average_imdb_by_category(movies, "Romance")) 