# Screen Critic API

## Opis

ScreenCriticAPI to RESTful API, które umożliwia dostęp do bazy danych filmów, recenzji oraz profili użytkowników.

## Instalacja

```bash
git clone https://github.com/grzegorzpustulka/screenCriticApi.git
cd screenCriticApi

# Instalacja zależności
pip install -r requirements.txt

# Uruchomienie serwera
uvicorn screen_critic.main:app
```

## Automatyczna dokumentacja API

```http
http://localhost:8000/docs
```

## Jak zacząć
1. Uruchom API, postępuj zgodnie z instrukcjami instalacji.
2. Otwórz przeglądarkę lub narzędzie do wysyłania zapytań HTTP (np. Postman, Curl).
3. Wykonaj żądania HTTP, korzystając z dostępnych ścieżek API (zobacz sekcję "Funkcje" poniżej).

## Funkcje
###  Moduł autyzacji
#### Logowanie (`/auth/login`)

- Endpoint umożliwiający użytkownikom logowanie do aplikacji. Użytkownicy mogą podać swoją nazwę użytkownika i hasło, a następnie otrzymują token dostępu, który można używać do dostępu do chronionych zasobów API. W przypadku niepoprawnych danych logowania, zostanie zwrócony błąd HTTP 400.

**Przykład użycia:**

```bash
curl -X POST http://localhost:8000/auth/login -H "Content-Type: application/x-www-form-urlencoded" -d "username=testuser&password=secretpassword"
```
**Przykładowa odpowiedź:**

```json
{
    "access_token": "jwt-token",
    "token_type": "bearer"
}
```

#### Rejestracja (`/auth/signup`)

- Endpoint umożliwiający użytkownikom logowanie do aplikacji. Użytkownicy mogą podać swoją nazwę użytkownika i hasło, a następnie otrzymują token dostępu, który można używać do dostępu do chronionych zasobów API. W przypadku niepoprawnych danych logowania, zostanie zwrócony błąd HTTP 400.

**Przykład użycia:**

```bash
curl -X POST http://localhost:8000/auth/signup -H "Content-Type: application/json" -d '{"username": "newuser", "password": "newpassword", "email": "example@gmail.com", "first_name": "John", "last_name": "Doe"}'
```
**Przykładowa odpowiedź:**

```json
{
    "id": "0a4a942b-82de-429b-90a7-0ca99ceca00d",
    "username": "newuser",
    "email": "example@gmail.com",
    "first_name": "John",
    "last_name": "Doe",
    "rank": "user"
}
```

#### Odczyt danych o zalogowanym użytkowniku (`/auth/me`)

- Endpoint umożliwiający użytkownikom logowanie do aplikacji. Użytkownicy mogą podać swoją nazwę użytkownika i hasło, a następnie otrzymują token dostępu, który można używać do dostępu do chronionych zasobów API. W przypadku niepoprawnych danych logowania, zostanie zwrócony błąd HTTP 400.

**Przykład użycia:**

```bash
curl -X GET http://localhost:8000/auth/me -H "Authorization: Bearer jwt-token"
```
**Przykładowa odpowiedź:**

```json
{
    "id": "0a4a942b-82de-429b-90a7-0ca99ceca00d",
    "username": "newuser",
    "email": "example@gmail.com",
    "first_name": "John",
    "last_name": "Doe",
    "rank": "user"
}
```

#### Usuwanie konta użytkownika (`/auth/delete`)

- Endpoint ten umożliwia użytkownikom usunięcie swojego konta z aplikacji. Po wykonaniu tego żądania, konto użytkownika zostaje trwale usunięte, a użytkownik zostaje wylogowany z aplikacji. Endpoint zwraca kod stanu HTTP 204 (No Content) w przypadku sukcesu.

**Przykład użycia:**

```bash
curl -X DELETE http://localhost:8000/auth/delete -H "Authorization: Bearer jwt-token"
```
**Przykładowa odpowiedź:**

```
HTTP/1.1 204 No Content
```

###  Moduł filmów
#### Wyświetlenie wszystkich dostępnych filmów (`/movie/search`)

- Endpoint umożliwiający wyszukiwanie wszystkich filmów.

**Ścieżka:** `/movie/search`

**Metoda:** `GET`

**Przykład użycia:**

```bash
curl -X GET http://localhost:8000/movie/search
```

#### Wyszukiwanie Filmów po Nazwie (`/movie/name/{movie_name}`)

- Endpoint umożliwiający wyszukiwanie filmów po nazwie.

**Ścieżka:** `/movie/name/{movie_name}`

**Metoda:** `GET`

**Przykład użycia:**

```bash
curl -X GET http://localhost:8000/movie/name/Avatar
```

#### Wyszukiwanie Filmów po id (`/movie/id/{id_movie}`)

- Endpoint umożliwiający wyszukiwanie filmu po ID.

**Ścieżka:** `/movie/id/{id_movie}`

**Metoda:** `GET`

**Przykład użycia:**

```bash
curl -X GET http://localhost:8000/movie/id/0a4a942b-82de-429b-90a7-0ca99ceca00d
```

#### Wyszukiwanie Kategorii Filmów (`/movie/categories`)

- Endpoint umożliwiający wyszukiwanie filmu po ID.

**Ścieżka:** `/movie/categories`

**Metoda:** `GET`

**Przykład użycia:**

```bash
curl -X GET http://localhost:8000/movie/categories
```

#### Losowy Film z Danej Kategorii (`/movie/random/{category_id}`)

- Endpoint umożliwiający wybieranie losowego filmu z danej kategorii.

**Ścieżka:** `/movie/random/{category_id}`

**Metoda:** `GET`

**Przykład użycia:**

```bash
curl -X GET http://localhost:8000/movie/random/0a4a942b-82de-429b-90a7-0ca99ceca00d
```

## Jak uruchomić testy

```bash
pytest
```

## Jak uruchomić pre-commit

```bash
pre-commit install
```

## Wzorce projektowe

- [x] Dependency Injection (DI)
- [x] Session per request
- [x] Singleton
- [x] Decorator
- [x] Repository
- [x] Data Transfer Object (DTO)
- [x] Factory method
- [x] Command
- [x] Active Record


## opis wzorców

#### Dependency Injection (DI)
- Użycie Depends w FastAPI, jak w funkcjach get_db czy get_current_user, jest przykładem wstrzykiwania zależności. Pozwala to na oddzielenie logiki tworzenia obiektów (np. sesji bazy danych) od ich wykorzystania w kontrolerach i innych częściach aplikacji.
#### Session per Request
-  Funkcja get_db, która tworzy i zwraca sesję SQLAlchemy, a następnie zamyka ją po zakończeniu żądania, jest implementacją wzorca "Session per Request". To zapewnia, że każde żądanie HTTP ma swoją własną sesję do interakcji z bazą danych.
#### Singleton
- Dekorator @lru_cache() stosowany w funkcji get_settings to przykład wzorca Singletona. Zapewnia on, że konfiguracja (ustawienia) jest ładowana tylko raz i jest ponownie używana przez cały cykl życia aplikacji.
#### Decorator
- Dekoratory FastAPI, takie jak @router.post("/signup"), są przykładami wzorca dekoratora. Rozszerzają one standardowe funkcje o dodatkową funkcjonalność, taką jak routing czy walidacja danych wejściowych.
#### Repository
- Klasa CRUDBase działa jako wzorzec repozytorium, zapewniając abstrakcyjny interfejs do operacji CRUD na modelach danych. Oddziela to logikę dostępu do danych od logiki biznesowej.
#### Data Transfer Object (DTO)
- Modele Pydantic, takie jak UserCreate i UserRead, są przykładami DTO. Są używane do przenoszenia danych między warstwami aplikacji, na przykład od klienta API do serwera i z powrotem.
#### Factory method
-  Fabryki, takie jak UserFactory, MovieFactory itd., są przykładem wzorca metody fabrykującej. Są one używane do tworzenia instancji obiektów, co jest szczególnie przydatne w testach i inicjalizacji danych.
#### Command
- Klasa CreateObjectCommand jest realizacją wzorca Command. Używana jest do enkapsulacji i centralizacji logiki tworzenia i zapisywania obiektów w bazie danych. Poprzez przyjęcie sesji bazy danych, fabryki obiektów i argumentów niezbędnych do stworzenia obiektu, CreateObjectCommand oddziela proces tworzenia obiektu od szczegółów jego trwałego zapisu. Metoda execute tej klasy wykonuje całą sekwencję akcji wymaganych do utworzenia i zapisania obiektu w bazie danych.
#### Active Record
- Modele SQLAlchemy, które zawierają zarówno dane, jak i metody do ich manipulacji (np. zapis, odczyt, aktualizacja, usuwanie), są przykładem wzorca Active Record.

## Autor
- Grzegorz Pustułka
- Adres e-mail: kontakt.pustulka@gmail.com
- [GitHub](https://github.com/GrzegorzPustulka)
- [LinkedIn](https://www.linkedin.com/in/grzegorzpustulka/)

## Licencja
- Ten projekt jest udostępniany na licencji MIT - szczegóły znajdują się w pliku [LICENSE.md](LICENSE.md)
