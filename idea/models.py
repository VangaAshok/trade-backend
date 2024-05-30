from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related

# Create your models here.


class Idea(models.Model):
    IDEA_TYPE_STOCK = "S"
    IDEA_TYPE_BITCOIN = "B"
    IDEA_TYPE_CHOICES = ((IDEA_TYPE_STOCK, "Stock"), (IDEA_TYPE_BITCOIN, "Bitcoin"))

    RISK_CATEGORY_LOW = "L"
    RISK_CATEGORY_MEDIUM = "M"
    RISK_CATEGORY_HIGH = "H"
    RISK_CATEGORY_CHOICES = (
        (RISK_CATEGORY_LOW, "Low"),
        (RISK_CATEGORY_MEDIUM, "Medium"),
        (RISK_CATEGORY_HIGH, "High"),
    )

    CURRENCY_TYPE_INDIAN_RUPEE = "IR"
    CURRENCY_TYPE_AMERICAN_DOLLAR = "AD"
    CURRENCY_TYPE_CHOICES = (
        (CURRENCY_TYPE_INDIAN_RUPEE, "RUPEE"),
        (CURRENCY_TYPE_AMERICAN_DOLLAR, "DOLLAR"),
    )

    idea_type = models.CharField(max_length=1, choices=IDEA_TYPE_CHOICES)
    name_of_the_idea = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        User, related_name="created_by_user", on_delete=models.SET_NULL, null=True
    )
    risk_category = models.CharField(max_length=1, choices=RISK_CATEGORY_CHOICES)
    stoploss_at = models.DecimalField(max_digits=15, decimal_places=2)

    currency_in = models.CharField(max_length=2, choices=CURRENCY_TYPE_CHOICES)
    book_profit_near = models.DecimalField(max_digits=15, decimal_places=2)
    up_or_down_side_in_percent = models.DecimalField(max_digits=4, decimal_places=2)
    subscriber = models.ManyToManyField(User, related_name="ideas", blank=True)
