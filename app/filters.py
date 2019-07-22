from django_filters import FilterSet
from django_filters import filters

from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):

    name = filters.CharFilter(label='タイトル', lookup_expr='contains')
    size = filters.CharFilter(label='サイズ', lookup_expr='contains')

    order_by = MyOrderingFilter(

        fields=(
            ('name', 'name'),
            ('size', 'size'),
            ('category', 'category'),
            ('status', 'status'),
            ('created_at', 'created_at'),

        ),
        field_labels={
            'name': 'タイトル',
            'size': 'サイズ',
            'category': 'カテゴリー',
            'status': 'ステータス',
            'created_at': '登録日時',
        },
        label='並び順'
    )

    class Meta:
        model = Item
        fields = ('name', 'category', 'status',)
