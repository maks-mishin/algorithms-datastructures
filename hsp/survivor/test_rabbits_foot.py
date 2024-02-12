import unittest

from tasks.rabbits_foot import TheRabbitsFoot


class TestRabbitsFoot(unittest.TestCase):
    def test_rabbit_foot(self):
        self.assertEqual(
            TheRabbitsFoot("отдай мою кроличью лапку", True),
            "омоюу толл дюиа акчп йрьк"
        )
        self.assertEqual(
            TheRabbitsFoot("омоюу толл дюиа акчп йрьк", False),
            "отдаймоюкроличьюлапку"
        )

    def test_encrypt(self):
        data = [
            ['отдай мою кроличью лапку', 'омоюу толл дюиа акчп йрьк'],
            ['', ''],
            [' ', ''],
            [' ф', 'ф'],
            ['аб', 'а б'],
            ['абв', 'ав б'],
            ['а б в   г', 'ав бг'],
            ['шифрование это просто', 'швэо иатс фнот рипо оер'],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(TheRabbitsFoot(dataset[0], True), dataset[1])

    def test_decrypt(self):
        data = [
            ['омоюу толл дюиа акчп йрьк', 'отдаймоюкроличьюлапку'],
            ['', ''],
            [' ', ''],
            ['ф', 'ф'],
            ['а б', 'аб'],
            ['ав б', 'абв'],
            ['ав бг', 'абвг'],
            ['швэо иатс фнот  рипо оер', 'шифрованиеэтопросто'],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(TheRabbitsFoot(dataset[0], False), dataset[1])


if __name__ == "__main__":
    unittest.main()
