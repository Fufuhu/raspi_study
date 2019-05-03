from django.urls import path
from raspi.views.base_view import BaseView
from raspi.views.stream_view import StreamView
from raspi.views.filtered_stream_view import FilteredStreamView
from raspi.views.logo_stream_view import LogoStreamView
from raspi.views.snapshot_view import SnapView

urlpatterns = [
    path('snapshot', SnapView.as_view(), name="snap"), 
    path('filtered', FilteredStreamView.as_view(), name="filtered_stream"),
    path('stream', StreamView.as_view(), name='stream'),
    path('logo', LogoStreamView.as_view(), name='logo_stream'),
    path('', BaseView.as_view(), name="base"),
]