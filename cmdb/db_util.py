from cmdb import models

def searchAllFilmReview():
    film_reviews = models.Article.objects.filter(categories='F')
    return film_reviews

def searchFilmReviewById(id):
    film_review = models.Article.objects.filter(id=id)
    return film_review
    