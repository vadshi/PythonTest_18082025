import unittest
from Day_2.Solutions.decrypt import decrypt


class TestDecrypt(unittest.TestCase):
    """Тесты для функции decrypt"""
    
    def test_basic_decryption(self):
        """Тест базовой расшифровки"""
        self.assertEqual(decrypt('070411111426152419071413'), 'hello python')
    
    def test_single_character(self):
        """Тест одного символа"""
        self.assertEqual(decrypt('00'), 'a')
        self.assertEqual(decrypt('25'), 'z')
        self.assertEqual(decrypt('26'), ' ')
    
    def test_multiple_characters(self):
        """Тест нескольких символов"""
        # 'a' + пробел + 'z'
        self.assertEqual(decrypt('002625'), 'a z')
        # 'b' + пробел + 'z' + пробел + 'a'
        self.assertEqual(decrypt('0126252600'), 'b z a')
    
    def test_all_alphabet(self):
        """Тест всего алфавита"""
        # a-z
        alphabet_codes = ''.join([f"{i:02d}" for i in range(26)])
        expected = ''.join([chr(ord('a') + i) for i in range(26)])
        self.assertEqual(decrypt(alphabet_codes), expected)
    
    def test_with_spaces(self):
        """Тест с пробелами"""
        self.assertEqual(decrypt('0726072607'), 'h h h')
        self.assertEqual(decrypt('262626'), '   ')
    
    def test_empty_string(self):
        """Тест пустой строки"""
        self.assertEqual(decrypt(''), '')
    
    def test_odd_length(self):
        """Тест нечетной длины строки"""
        with self.assertRaises(ValueError) as context:
            decrypt('123')
        self.assertIn('четной', str(context.exception))
        
        with self.assertRaises(ValueError):
            decrypt('1')
    
    
    def test_out_of_range_codes(self):
        """Тест кодов вне диапазона"""
        test_cases = [
            ('27', '27'),  # больше 26
            ('99', '99'),  # намного больше
            ('50', '50')   # среднее значение
        ]
        
        for code, expected_in_error in test_cases:
            with self.subTest(code=code):
                # Создаем валидную строку с невалидным кодом
                test_input = code + '00'  # невалидный код + валидный
                with self.assertRaises(ValueError) as context:
                    decrypt(test_input)
                error_msg = str(context.exception)
                self.assertIn(expected_in_error, error_msg)
                self.assertIn('00-26', error_msg)
    
    def test_negative_codes(self):
        """Тест отрицательных кодов"""
        with self.assertRaises(ValueError):
            decrypt('-1-2')  # отрицательные числа
    
    def test_boundary_values(self):
        """Тест граничных значений"""
        # Корректные граничные значения
        self.assertEqual(decrypt('00'), 'a')   # нижняя граница
        self.assertEqual(decrypt('26'), ' ')   # верхняя граница
        
        # Некорректные граничные значения
        with self.assertRaises(ValueError):
            decrypt('27')   # сразу за верхней границей
        
        with self.assertRaises(ValueError):
            decrypt('-1')   # сразу за нижней границей
    
    def test_long_string(self):
        """Тест длинной строки"""
        long_code = '00' * 1000  # 2000 символов
        expected = 'a' * 1000
        self.assertEqual(decrypt(long_code), expected)
    
    def test_mixed_valid_invalid(self):
        """Тест смешанных валидных и невалидных данных"""
        # Невалидные символы в середине
        with self.assertRaises(ValueError):
            decrypt('0007abc825')
        
        # Невалидный код в середине
        with self.assertRaises(ValueError):
            decrypt('00073025')  # 30 - невалидный код


class TestEdgeCases(unittest.TestCase):
    """Тесты крайних случаев"""
    
    def test_only_spaces(self):
        """Только пробелы"""
        self.assertEqual(decrypt('26' * 10), ' ' * 10)
    
    def test_alternating_chars(self):
        """Чередование букв и пробелов"""
        self.assertEqual(decrypt('0026002600'), 'a a a')
    
    def test_specific_word(self):
        """Конкретное слово"""
        self.assertEqual(decrypt('1815000204'), 'space')


if __name__ == '__main__':
    unittest.main(verbosity=2)