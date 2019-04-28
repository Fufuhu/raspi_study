from django.urls import path
from raspi.views.stream_view import StreamView
from raspi.views.filtered_stream_view import FilteredStreamView

urlpatterns = [
    path('filtered', FilteredStreamView.as_view(), name="filtered_stream"),
    path('', StreamView.as_view(), name="stream"),
]