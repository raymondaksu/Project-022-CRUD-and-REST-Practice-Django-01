from django.urls import path
from .views import StudentGetUpdateDelete, StudentList, home_api, student_get_update_delete, student_list_create_api
# student_list_api, student_create_api, Student(mixin)

urlpatterns = [
    path("home-api/", home_api),
    path("list-create-api/", student_list_create_api),
    path("<int:id>/", student_get_update_delete),
    # path("list-api/", student_list_api),
    # path("create-api/", student_create_api),
    # path("list-create-api/", StudentList.as_view()),
    # path("<int:id>/", StudentGetUpdateDelete.as_view(), name='detail'),
    # path("<int:id>/", Student.as_view(), name='detail'), #(mixin)
]
