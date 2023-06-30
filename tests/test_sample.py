from ..main import Tom

class TestClass:

    tom = Tom()

    def test_tom_name(self):
        assert self.tom.name == 'Tom'

    def test_tom_is_poor(self):
        assert self.tom.money == 0.0
