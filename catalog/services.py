from django.core.exceptions import ObjectDoesNotExist

from catalog.models import Product


class ProductService:
    @staticmethod
    def get_product_list(category_id):
        try:
            return Product.objects.filter(category_id=category_id, is_published=True)
        except ObjectDoesNotExist:
            return Product.objects.none()
