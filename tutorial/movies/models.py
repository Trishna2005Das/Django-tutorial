from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.ManyToManyField(Genre, related_name='movies')
    rating = models.FloatField()
    poster_url = models.URLField(blank=True, null=True)
    trailer_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    # the above __str__ method is used to display the title of the movie when we print the movie object. It is a string representation of the movie object. If we do otherswise, the object will be printed as <Movie object (id)>

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlists')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='watchlists')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.user.username}'s Watchlist - {self.movie.title}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()  # Range: 1 to 5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.movie.title}"
