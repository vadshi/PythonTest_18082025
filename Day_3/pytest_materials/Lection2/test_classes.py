from tasks import Task


class TestEquality:
    def test_equality(self):
        c1 = Task("something", "petr", "todo", 123)
        c2 = Task("something", "petr", "todo", 123)
        assert c1 == c2

    def test_equality_with_diff_ids(self):
        c1 = Task("something", "petr", "todo", 123)
        c2 = Task("something", "petr", "todo", 4567)
        assert c1 == c2

    def test_inequality(self):
        c1 = Task("something", "petr", "todo", 123)
        c2 = Task("completely different", "anna", "done", 123)
        assert c1 != c2