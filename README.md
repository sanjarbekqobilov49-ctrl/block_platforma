<<<<<<< HEAD
# Blog Platforma

Mini-ijtimoiy tarmoq ko'rinishidagi blog platformasi. Foydalanuvchilar post joylaydi, izoh qoldiradi, like bosadi va profillariga kiradi.

## Imkoniyatlar

- Postlar CRUD (yaratish, o'qish, tahrirlash, o'chirish)
- Izoh qoldirish
- Like bosish/olish
- Foydalanuvchi profili
- Qidiruv (title/content bo'yicha)
- Pagination
- REST API

## O'rnatish

```bash
# Virtual muhit yaratish
python -m venv venv
venv\Scripts\activate

# Kerakli paketlarni o'rnatish
pip install -r requirements.txt

# Migratsiyalarni bajarish
python manage.py migrate

# Superuser yaratish
python manage.py createsuperuser

# Ishga tushirish
python manage.py runserver
```

## API Usage

| Method | URL | Vazifasi |
|--------|-----|----------|
| GET | /api/posts/ | Barcha postlar |
| POST | /api/posts/ | Post yaratish |
| GET | /api/posts/<id>/ | Bir postni ko'rish |
| PUT/PATCH | /api/posts/<id>/ | Tahrirlash |
| DELETE | /api/posts/<id>/ | O'chirish |
| POST | /api/posts/<id>/comment/ | Izoh qoldirish |
| POST | /api/posts/<id>/like/ | Like bosish |

## Screenshots

### Home Page
![home](screenshots/home.png)

### Post Detail
![detail](screenshots/detail.png)

## Loyiha tuzilmasi

```
blog_project/
 ├─ blog_app/       # Asosiy app (modellar, viewlar)
 ├─ api/            # DRF API
 ├─ templates/      # HTML shablonlar
 ├─ static/         # CSS fayllar
 ├─ media/          # Yuklangan rasmlar
 └─ manage.py
```
=======
# block_platforma
Mini-ijtimoiy tarmoq ko'rinishidagi blog platformasi. Foydalanuvchilar post joylaydi, izoh qoldiradi, like bosadi va profillariga kiradi.
>>>>>>> 3cc6e8f38337b24567f8b35db8ad5b0fbc554a7a
