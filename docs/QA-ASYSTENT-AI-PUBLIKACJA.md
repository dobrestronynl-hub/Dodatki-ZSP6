# Publikacja asystenta AI i uproszczonego katalogu

Data weryfikacji: 23.11.2026. **Wynik: opublikowane i sprawdzone pod publicznymi adresami.**

## Wersja

- Repozytorium źródłowe: `dobrestronynl-hub/Dodatki-ZSP6`, kod modułu w commicie `6501e252552a69541a4da3ec407a5c09f61316bc`.
- [Walidacja kodu w GitHub Actions](https://github.com/dobrestronynl-hub/Dodatki-ZSP6/actions/runs/45139680821): `completed / success`.
- Repozytorium publikujące: `dobrestronynl-hub/ZSP6`, commit `db6b0bc75fbd126cc2fc0d379f62294838c1b5c6`.
- [GitHub Pages](https://github.com/dobrestronynl-hub/ZSP6/actions/runs/45139721174): `completed / success`.
- Pliki HTML, CSS, MJS i logo nowego modułu w kopii publikacyjnej są identyczne z odpowiednikami źródłowymi. Główne wizualizacje szkoły nie były zmieniane w tym wdrożeniu.

## Publiczne adresy

- [Katalog dodatków](https://dobrestronynl-hub.github.io/ZSP6/dodatki/).
- [Asystent AI szkoły](https://dobrestronynl-hub.github.io/ZSP6/dodatki/moduly/asystent-ai/index.html).

Adresy zostały otwarte w przeglądarce po zakończeniu publikacji. Katalog zawiera osiem funkcji, z asystentem AI na pierwszym miejscu. Nie zawiera sekcji `#wdrozenie`, sekcji `.testing` ani odnośników do edytora aktualności. Dawny bezpośredni adres edytora pokazuje stronę GitHub Pages „404 / File not found”.

## Sprawdzenie publicznego asystenta

1. Własne pytanie „Interesuje mnie fotografia” pokazuje technika fotografii i multimediów.
2. Dopowiedzenie „A jakie dokumenty?” zachowuje kontekst tego kierunku i prowadzi do rekrutacji.
3. Podgląd „Pokaż na stronie” prezentuje tę samą rozmowę w widżecie. Zamknięcie i ponowne otwarcie zachowuje obie wiadomości.
4. „Zapisz rozmowę” pobiera rzeczywisty TXT. Odczytano plik, potwierdzając kontekst, oznaczenie demonstracji i oficjalny odnośnik do rekrutacji.
5. „Nowa rozmowa” usuwa wątek, zeruje kontekst i wyłącza eksport do momentu zadania kolejnego pytania.
6. Przy rozmowie cały czas widoczna jest informacja o demonstracji bez modelu AI.

[Zapis obserwacji online](qa/ai-publication-results.json) · [Lokalny raport logiki, interfejsu i układu](../moduly/asystent-ai/QA.md)

Lokalna kontrola obejmowała 32 zaliczone testy Node, w tym 22 asystenta, oraz 18 sprawdzeń układu w sześciu szerokościach dla katalogu, rozmowy i widżetu. Rozdzielenie lokalnego QA i powyższej weryfikacji online pozwala odróżnić wynik testów od faktycznej dostępności publikacji.

## Zakres demonstracji

Publikacja nie dodaje modelu AI, serwera rozmów ani integracji z systemami szkoły. Publiczny podgląd prezentuje lokalną bazę odpowiedzi, kontekst, odnośniki i interakcje przyszłego asystenta. Pełna integracja AI i aktualizowanej wiedzy jest opisana w [README modułu](../moduly/asystent-ai/README.md). Testy układu nie zastępują formalnego audytu dostępności ani testów na fizycznym telefonie.
