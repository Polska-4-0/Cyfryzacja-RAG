# Analiza dokumentów dotyczących proponowanej strategii cyfryzacji do roku 2035

Orygninalne dwa dokumenty pdf dostępne są na stronie [Ministerstwa Cyfryzacji](https://www.gov.pl/web/cyfryzacja/strategia-cyfryzacji-polski-do-2035-roku)
w paragrafie Materiały. 

To repozytorium zawiera kopię dokumentów w formacie pdf jak i ich wersję w formacie tekstowy.

dokumenty/Strategia_Cyfryzacji_Państwa_Projekt_do_konsultacji_społecznych.pdf
dokumenty/Strategia_Cyfryzacji_Polski_28_10_2024_prezentacja.pdf


## Konwersja formatu pdf do tekstu

Do analizy tekstu użyta komendy pdftotext  

pdftotext dokumenty/Strategia_Cyfryzacji_Państwa_Projekt_do_konsultacji_społecznych.pdf dokumenty/Strategia_Cyfryzacji_Państwa_Projekt_do_konsultacji_społecznych.tks

pdftotext dokumenty/Strategia_Cyfryzacji_Polski_28_10_2024_prezentacja.pdf dokumenty/Strategia_Cyfryzacji_Polski_28_10_2024_prezentacja.tks


## RAG używając LightRAG i ollama

[LightRAG](https://github.com/HKUDS/LightRAG)


### Installacja modelu Bielik v2.3 dla ollama

ollama pull  SpeakLeash/bielik-11b-v2.3-instruct:Q8_0

### Kod 

python kod/cyfryzacja-rag_ollama.py


## Tekst ze strony Ministerstwa Cyfryzacji z dnia 28.10.2024


Strategia Cyfryzacji Polski do 2035 roku

28.10.2024

Wicepremier i minister cyfryzacji Krzysztof Gawkowski zaprezentował projekt Strategii Cyfryzacji Polski. To pierwszy tak kompleksowy dokument w historii naszego kraju, który ma być planem transformacji cyfrowej na najbliższe 10 lat. Główny cel: poprawa jakości życia obywateli dzięki cyfryzacji. Dokument trafia właśnie do konsultacji społecznych.

W ostatnich latach cyfryzacja przestaje być postrzegana jako odrębny obszar działalności państwa czy sektor gospodarki podobny do wielu innych. Coraz częściej dostrzegany jest jej horyzontalny charakter, oddziałujący na niemal wszystkie obszary funkcjonowania społeczeństwa, państwa i gospodarki. Sfera technologii cyfrowych jest kluczowym polem nasilającej się rywalizacji geopolitycznej, a inwestycje w tej dziedzinie pośrednio lub bezpośrednio przekładają się na poziom bezpieczeństwa państwa.

Przed Polską realizacja kluczowych celów na najbliższą dekadę. Cele te muszą uwzględniać między innymi zmieniający się krajobraz bezpieczeństwa państwa i środowiska międzynarodowego, aktualne trendy i wyzwania w obszarze technologii i jej regulacji, a także specyfikę polskiego społeczeństwa i gospodarki.

Polskie ambicje i działania wpisują się w kontekst zauważalnego w ostatnich latach wzrostu znaczenia cyfryzacji na liście priorytetów Unii Europejskiej. Nasz plan na najbliższe 10 lat jest ambitny i obejmuje każdy element funkcjonowania Państwa, życie obywatela oraz działania przedsiębiorstwa.

– Wyzwania stojące przed Polską w obszarach konkurencyjności gospodarki, demografii, bezpieczeństwa państwa i jego obywateli czy zdrowia sprawiają, że intensywne inwestowanie w cyfryzację w wielu obszarach przestaje być kwestią wyboru. Staje się koniecznością, bez której pozycja naszego kraju wyraźnie osłabnie. Jeśli jednak cyfryzacji zostanie nadany odpowiadający jej znaczeniu priorytet, zyskają nie tylko poszczególni obywatele i obywatelki – których jakość życia się poprawi – ale i Polska jako całość – powiedział wicepremier i minister cyfryzacji Krzysztof Gawkowski.



Kluczowe założenia nowego podejścia do cyfryzacji

    Koniec z silosowością – która sprawia, że poszczególne części administracji nie widzą się wzajemnie, podwyższa koszty i radykalnie utrudnia budowę korzystnych dla obywateli rozwiązań;
    Pieniądze, ludzie i lepsza organizacja – ludzie, którzy tworzą potencjał cyfrowy państwa nie mogą tego robić za płacę minimalną;
    Współpraca – międzynarodowa, ale też między państwem a akademią, społeczeństwem i biznesem. Współpraca, w której wszyscy – również międzynarodowe korporacje – dokładają swoje cegiełki do budowy wspólnego dobra;
    Obywatele – nowe rozwiązania nigdy nie mogą być wprowadzane kosztem bezpieczeństwa, zarówno w odniesieniu do cyberbezpieczeństwa, jak i do praw podstawowych;
    Sprawiedliwa transformacja cyfrowa – rozwijające się cyfrowe państwo musi dbać o klimat, prawa pracowników platformowych i wsparcie osób, których miejsca pracy są zagrożone przez technologię. Nie może też myśleć, że technologia sama rozwiąże wszystkie problemy;
    Bezpieczeństwo – w cyberprzestrzeni, w wykorzystaniu AI, w bezpiecznym korzystaniu z technologii w ogóle – przede wszystkim przez dzieci.

Pierwszy taki dokument

Strategia to ponadsektorowy dokument strategiczny w dziedzinie informatyzacji państwa, określający nadrzędny cel, jakim jest poprawa jakości życia obywateli poprzez cyfryzację do 2035 r. Jego realizacja możliwa jest tylko dzięki interwencji w szeregu obszarów, wykraczających poza tradycyjnie definiowany dział administracji – informatyzacja.

Zaplanowane do realizacji cele obejmują szerokie spektrum zagadnień, począwszy od kwestii horyzontalnych, poprzez płaszczyznę państwa i jego obywateli, na gospodarce i rozwoju technologii kończąc.

Takie podejście pozwoliło na stworzenie nowoczesnej, przekrojowej i odpowiadającej na aktualne wyzwania wizji rozwoju cyfrowego, bazującej na aktualnych trendach europejskich i globalnych, wynikającej z diagnozy aktualnego stanu informatyzacji państwa oraz odpowiadającej na formułowane oczekiwania społeczne.

Wdrażanie strategii nie może się odbywać w oderwaniu od otoczenia strategicznego, zarówno krajowego, jak i unijnego. Sformułowane w strategii cele znajdują odzwierciedlenie i są uszczegółowione w szeregu już obowiązujących dokumentów lub będą spójne z nowymi wersjami dokumentów będących aktualnie w opracowaniu, tj. Strategia Cyberbezpieczeństwa RP, Narodowy Plan Szerokopasmowy, Program Rozwoju Kompetencji Cyfrowych, Program Otwierania Danych, Polityka Rozwoju Sztucznej Inteligencji czy Polityka Cyfrowej Transformacji Edukacji.
Co chcemy osiągnąć do 2035 roku

    W roku 2035 przynajmniej podstawowe kompetencje cyfrowe będzie miało 85% obywateli;
    100% projektów IT o publicznym zastosowaniu realizowanych zgodnie z jednolitymi standardami i rekomendacjami architektonicznymi Architektury Informacyjnej Państwa;
    100% podmiotów realizujących zadania publiczne pracuje na systemie elektronicznego zarządzania dokumentami;
    100% spraw prowadzonych przez te podmioty załatwiana jest elektronicznie;
    20 mln Polaków posiada portfel tożsamości cyfrowej;
    Wszystkie kluczowe e-usługi dostępne w aplikacji mObywatel;
    100 jednostek chorobowych diagnozowanych wspomagająco z wykorzystaniem AI;
    Przynajmniej 1,5 mln specjalistów ICT;
    100% jednostek administracji publicznej udostępniających e-płatności;
    50% firm wykorzystujących narzędzia AI;
    5% PKB na cyfryzację od 2035 roku.

Dokument powstał w Ministerstwie Cyfryzacji we współpracy z innymi urzędami administracji rządowej oraz z uwzględnieniem postulatów interesariuszy społecznych i środowisk biznesowych. Zastąpi on Program Zintegrowanej Informatyzacji Państwa i będzie stanowić podstawę strategiczną dla wydatkowania europejskich funduszy przeznaczonych na cyfryzację, a tym samym będzie wyznaczał kierunek negocjacji obejmujących nadchodzącą perspektywę finansową.

Dokument trafia właśnie do konsultacji społecznych, wszelkie uwagi zgłaszać można poprzez adres mailowy: konsultacje.strategia@cyfra.gov.pl.

Materiały

Strategia Cyfryzacji Państwa. Projekt do konsultacji społecznych
Strategia​_Cyfryzacji​_Państwa​_Projekt​_do​_konsultacji​_społecznych.pdf 9.96MB
Strategia Cyfryzacji Polski. Prezentacja
Strategia​_Cyfryzacji​_Polski​_28​_10​_2024​_prezentacja.pdf 5.64MB 
