from rest_framework import serializers
from .models import Idea
from django.contrib.auth.models import User


class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = [
            "id",
            "idea_type",
            "risk_category",
            "currency_in",
            "name_of_the_idea",
            "stoploss_at",
            "book_profit_near",
            "up_or_down_side_in_percent",
            "created_by",
        ]


class IdeaListSerializer(serializers.ModelSerializer):
    idea_type = serializers.CharField(source="get_idea_type_display")
    risk_category = serializers.CharField(source="get_risk_category_display")
    currency_in = serializers.CharField(source="get_currency_in_display")
    subscribers_count = serializers.IntegerField(
        source="subscriber.count", read_only=True
    )
    created_by = serializers.StringRelatedField(read_only=True)
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Idea
        fields = [
            "id",
            "idea_type",
            "risk_category",
            "currency_in",
            "name_of_the_idea",
            "stoploss_at",
            "book_profit_near",
            "up_or_down_side_in_percent",
            "created_by",
            "subscribers_count",
            "is_subscribed",
        ]

    def get_is_subscribed(self, obj: Idea):

        if self.context["user"] in obj.subscriber.all():
            return True
        return False


class IdeaSubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ["subscriber"]

    def update(self, instance: Idea, validated_data):
        instance.subscriber.add(self.context.get("user"))
        instance.save()
        print(instance)
        return instance
