"""___Classes_______________________________________________________________"""


class Assert():

    def AnalyseError(self, *args) -> str:
        error_msg = "\n"
        for a, arg in enumerate(args):
            error_msg += f"argument {a + 1} :\n{arg}\n"
        return error_msg

    def assertEqual(self, a, b) -> None:
        assert a == b, self.AnalyseError(a, b)

    def assertNotEqual(self, a, b) -> None:
        assert a != b, self.AnalyseError(a, b)

    def assertTextEqual(self, text1: str, text2: str, exact: bool = False) -> None:
        if exact:
            self.assertEqual(text1, text2)
        else:
            self.assertEqual(text1.split(), text2.split())

    def assertListEqual(self, list1: list, list2: list) -> None:
        self.assertEqual(len(list1), len(list2))
        for item1, item2 in zip(list1, list2):
            self.assertEqual(item1, item2)

    def assertDictEqual(self, dict1: dict, dict2: dict) -> None:
        self.assertEqual(len(list(dict1.keys())), len(list(dict2.keys())))
        for key, value in dict1.items():
            self.assertIn(key, dict2)
            self.assertEqual(value, dict2[key])

    def assertTrue(self, _bool) -> None:
        assert _bool

    def assertFalse(self, _bool) -> None:
        assert not _bool

    def assertIsInstance(self, obj, _class) -> None:
        assert isinstance(obj, _class)

    def assertIsNotInstance(self, obj, _class) -> None:
        assert not isinstance(obj, _class)

    def assertIn(self, obj: any, array: any) -> None:
        assert obj in array

    def assertNotIn(self, obj, array) -> None:
        assert not obj in array
