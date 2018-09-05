from rest_framework import serializers
from .models import Category, SubCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = "__all__"
        exclude = ['timestamp', 'updated', ]


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        # fields = "__all__"
        # exclude = ['category', ]
        exclude = ['timestamp', 'updated', ]

