from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from home.models import Product, Tag

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    tag_names = PrimaryKeyRelatedField(many=True, write_only=True, queryset=Tag.objects.all())

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        tags = validated_data.pop('tag_names')
        product = Product.objects.create(**validated_data)
        for tag in tags:
            product.tags.add(tag)
        return product
    
    def update(self, instance, validated_data):
        tags = validated_data.pop('tag_names')
        for item in validated_data:
            if Product._meta.get_field(item):
                setattr(instance, item, validated_data[item])
        instance.tags.clear()
        for tag in tags:
            instance.tags.add(tag)
        instance.save()
        return instance


