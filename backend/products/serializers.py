from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import unique_title_validator

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk')
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[unique_title_validator])
    #name = serializers.CharField(source='title', read_only=True)
    class Meta:
        model = Product
        fields = ['url', 'edit_url','id', 'title', 'content', 
        'price', 'sale_price', 'my_discount']
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists:
    #         raise serializers.ValidationError(f'{value} is already in')
    #     return value
    # def create(self, validated_data):
    #     #return Product.objects.create(**validated_data)
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     return obj
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     #instance.title = validated_data.get('title')
    #     return super().update(instance, validated_data)
    def get_edit_url(self,obj):
        #return f"/api/products/{obj.id}"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-update", kwargs={"pk":obj.id}, request=request)
    def get_my_discount(self,obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()