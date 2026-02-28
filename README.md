# Sport App - Örnek

Bu depoya basit bir lig puan hesaplama örneği eklendi.

## Çalıştırma

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

## İçerik

- `calculate_points(wins, draws, losses)`: 3-1-0 sistemine göre puan hesaplar.
- `goal_difference(goals_for, goals_against)`: averaj hesaplar.
- `total_matches(wins, draws, losses)`: toplam oynanan maç sayısını hesaplar.
- Negatif, bool ve hatalı tip girişleri için doğrulama içerir.
