# Dodatki ZSP6

Osiem działających demonstracji funkcjonalności dla Zespołu Szkół Ponadpodstawowych nr 6 w Tomaszowie Mazowieckim. Projekt służy wspólnemu sprawdzeniu pomysłów i ustaleniu zakresu wdrożenia oraz wyceny. Każdy moduł ma osobną stronę, opis zastosowania, instrukcję testowania i własne testy logiki.

Wszystkie demonstracje są w jednym repozytorium `Dodatki-ZSP6`. Katalogi `moduly/<nazwa>` zawierają samodzielny HTML, CSS, JavaScript i logo. Można je rozwijać, wyceniać i przenosić oddzielnie. Nie wymagają kodu głównych wizualizacji ani pozostałych modułów. W głównej wizualizacji ZSP6 dodatki nie są już prezentowane w sidebarze.

## Wybierz funkcjonalność

| Moduł | Do czego służy | Pliki i dokumentacja |
| --- | --- | --- |
| Asystent wyboru kierunku | Prowadzi od zainteresowania do konkretnej oferty i zasad rekrutacji. | [Demonstracja](moduly/asystent-kierunku/) · [Opis i testy](moduly/asystent-kierunku/README.md) |
| Osobista checklista rekrutacji | Porządkuje kroki, zapamiętuje postęp dla obu szkół i eksportuje listę. | [Demonstracja](moduly/checklista-rekrutacji/) · [Opis i testy](moduly/checklista-rekrutacji/README.md) |
| Dni otwarte i spotkania | Pokazuje termin oraz pobiera plik ICS do osobistego kalendarza. | [Demonstracja](moduly/dni-otwarte/) · [Opis i testy](moduly/dni-otwarte/README.md) |
| Biblioteka dokumentów | Wyszukuje rzeczywiste materiały szkoły i filtruje je według odbiorcy. | [Demonstracja](moduly/biblioteka-dokumentow/) · [Opis i testy](moduly/biblioteka-dokumentow/README.md) |
| Portfolio uczniów | Filtruje prace według dziedziny i udostępnia powiększony podgląd. | [Demonstracja](moduly/portfolio-uczniow/) · [Opis i testy](moduly/portfolio-uczniow/README.md) |
| Panel ucznia i rodzica | Dostosowuje skróty do roli i pozwala przypinać potrzebne odnośniki. | [Demonstracja](moduly/panel-ucznia-rodzica/) · [Opis i testy](moduly/panel-ucznia-rodzica/README.md) |
| Sprawy sekretariatu | Wyjaśnia, jak przygotować się do wybranej sprawy, i pobiera instrukcję. | [Demonstracja](moduly/sprawy-sekretariatu/) · [Opis i testy](moduly/sprawy-sekretariatu/README.md) |
| Edytor aktualności | Pokazuje podgląd wpisu i eksportuje szkic do korekty. | [Demonstracja](moduly/edytor-aktualnosci/) · [Opis i testy](moduly/edytor-aktualnosci/README.md) |

Na GitHubie odnośnik „Demonstracja” otwiera katalog źródłowy. Po uruchomieniu projektu przez HTTP te same ścieżki otwierają interfejsy. Strona `index.html` jest wspólnym spisem funkcjonalności.

## Jak ocenić zakres i wycenę

Najpierw otwórz moduł, wykonaj instrukcję „Przetestuj sam” i sprawdź, czy rozwiązuje rzeczywistą potrzebę szkoły. Następnie ustal, czy potrzebna jest tylko funkcja widoczna w demonstracji, czy także panel edycji, konta, powiadomienia lub połączenia z innymi systemami.

[Zakres do wyceny](docs/ZAKRES-WYCENY.md) opisuje dla każdego modułu działanie, korzyści, wymagania wdrożenia i rozszerzenia. Nie zawiera automatycznie naliczanych ani przykładowych cen. [Instrukcja testowania](docs/TESTOWANIE.md) zbiera scenariusze z oczekiwanymi wynikami.

## Uruchomienie lokalne

Projekt jest statyczny. Podgląd wymaga serwera HTTP, ponieważ interakcje używają modułów JavaScript. Nie wymaga instalacji pakietów npm, bazy danych ani frameworka.

Z katalogu głównego repozytorium:

```bash
python3 -m http.server 8000
```

Otwórz `http://localhost:8000/`. Aby uruchomić tylko jeden moduł, wykonaj tę samą komendę w jego katalogu, na przykład `moduly/asystent-kierunku`. Wtedy moduł otworzy się pod głównym adresem serwera. Odnośnik do wspólnego katalogu dodatków wymaga publikacji całego repozytorium.

## Kontrola i przygotowanie publikacji

W katalogu głównym, z dostępnym Pythonem 3 oraz Node.js obsługującym `node:test`:

```bash
node --test moduly/*/tests.mjs
python3 scripts/check.py
python3 scripts/build.py
```

Pierwsza komenda uruchamia testy logiki wszystkich ośmiu modułów. Kontrola projektu sprawdza strukturę i zależności statyczne, a build przygotowuje katalog `dist/` do publikacji. Komendy nie tworzą kont szkolnych, nie wysyłają wiadomości i nie zapisują danych kandydatów na serwerze.

W każdym module dostępne są `QA.md`, `test-results.txt` i `layout-results.json`. Zawierają wcześniejsze wyniki lokalnego sprawdzenia z 23.11.2026: osiem zestawów testów logiki, główne interakcje i 48 kontroli układu w Chromium. Te raporty nie są potwierdzeniem dostępności dowolnej późniejszej wersji opublikowanej na GitHub Pages. Publikowaną wersję należy sprawdzić po wdrożeniu.

[Raport integracji nowego katalogu](docs/QA-INTEGRACJA.md) zawiera aktualne sprawdzenie dziewięciu stron, nawigacji, sześciu szerokości katalogu i wszystkich ośmiu modułów na małym ekranie, wraz z pomiarami i podglądem.

## Publikacja w GitHub Pages

Cała strona jest gotowa do publikacji bezpośrednio z gałęzi `main`, z katalogu głównego. W ustawieniach repozytorium wybierz **Settings → Pages → Build and deployment**. Ustaw **Source: Deploy from a branch**, **Branch: main**, **Folder: / (root)** i zapisz. Wbudowany proces GitHub Pages opublikuje katalog dodatków i wszystkie osiem modułów. Pierwsze włączenie Pages wymaga dostępu do ustawień repozytorium.

Workflow `Sprawdzenie dodatkow ZSP6` sprawdza pliki, odnośniki, składnię, logikę i build po zmianach w `main` oraz w pull requestach. Nie włącza samodzielnie usługi Pages i nie wymaga sekretów. Katalog `dist/` jest również gotowym pakietem statycznym dla innego hostingu.

Po pierwszej publikacji wykonaj [kontrolę po wdrożeniu](docs/TESTOWANIE.md). Sam zapis plików w repozytorium ani zielony wynik testów nie oznacza, że Pages jest już aktywne.

## Co działa lokalnie, a co wymaga integracji

Wyszukiwanie, filtrowanie, dobór kierunku, podgląd wpisu oraz eksporty TXT i ICS działają w przeglądarce. Checklista i panel skrótów mogą zapisywać ustawienia w `localStorage`; nie synchronizują ich między urządzeniami. Zewnętrzne materiały otwierają rzeczywiste źródła szkoły.

Demonstracje nie składają wniosków, nie rezerwują miejsc, nie zakładają kont, nie wysyłają formularzy i nie publikują wpisów. Funkcje wymagające tych działań są opisane w zakresie docelowego wdrożenia. Materiały przykładowe są oznaczone jako demonstracyjne. Strony mają `noindex,nofollow`.

## Materiały i utrzymanie

Logo pochodzi z materiałów przekazanych do projektu ZSP6. Informacje i odnośniki stanowią migawkę materiałów szkoły sprawdzonych podczas przygotowania projektu 23.11.2026. Nie ma automatycznej synchronizacji z oficjalną witryną. Źródła i ograniczenia są opisane w README modułów oraz, tam gdzie występuje katalog materiałów, w `SOURCES.md`.

Fotografie portfolio są ładowane z serwera szkoły. Przed docelową publikacją należy uzgodnić prawo do wykorzystania materiałów, podpisy i zakres zgód. Projekt nie stwierdza uzyskania takich zgód.

[Główne wizualizacje ZSP6](https://dobrestronynl-hub.github.io/ZSP6/) · [Oficjalna strona szkoły](https://zsp6tom.pl/)
