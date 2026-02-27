# Sport App - Örnek

Bu depoya basit bir lig puan hesaplama örneği eklendi.

## Çalıştırma

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

## İçerik

- `calculate_points(wins, draws, losses)`: 3-1-0 sistemine göre puan hesaplar.
- `goal_difference(goals_for, goals_against)`: averaj hesaplar.
- Negatif ve hatalı tip girişleri için doğrulama içerir.
