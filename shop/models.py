from django.db import models

from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)

    # slug 필드란? : 상품명 등을 이용해 URL을 만드는 방식이다.
    # allow_unicode : 영문을 제외한 다른 언어도 값을 사용할 수 있도록 허용
    # db_index=True 를 할 시 카테고리 정보가 저장되는 테이블은 이 이름을 열로 설정한다.
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    # 아래와 같은 Meta 클래스 내의 내용은 SEO를 위해 만드는 필드이다. 추가사항은 구글 메뉴얼 참조
    class Meta:
        ordering = ['name', ]
        # verbose_name = admin에 객체가 단수일 때 보여지는 값
        verbose_name = 'category'
        # verbose_name_plural = admin에 객체가 복수일 때 보여지는 값
        verbose_name_plural = 'categoryies'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_in_category', args=[self.slug])


class Product(models.Model):
    # 카테고리가 사라져도 상품은 남아있어야 하므로 SET_NULL
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products")
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)

    # 제품가격과 재고, 쇼핑몰에서는 필수 값이다.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    # 상품을 사용자들에게 보여줄지 결정
    available_display = models.BooleanField('Display', default=True)
    # 상품이 지금 구입가능한지 결정
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', ]
        # DB 검색을 할 때 사용하는 색인을 id와 slug를 묶어서 만들어줌
        index_together = [['id', 'slug']]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
