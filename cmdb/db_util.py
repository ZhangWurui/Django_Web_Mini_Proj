from cmdb import models

def searchAllFilmReview():
    film_reviews = models.Article.objects.filter(categories='F')
    return film_reviews
