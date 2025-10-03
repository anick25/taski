import pytest

from api.models import Task


@pytest.mark.django_db
def test_task_str_returns_title():
    task = Task.objects.create(title='Test task', description='Sample description')

    assert str(task) == 'Test task'
