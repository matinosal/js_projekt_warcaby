# js_projekt_warcaby
Okno z siatką przycisków 8x8 oraz przyciskiem do resetowania gry. Przyciski reprezentują pola planszy do gry w warcaby.   
Pola puste - przyciski bez tekstu.  
Pola z pionkami gracza 1 - przycisk z tekstem "C".  
Pola z pionkami gracza 2 - przycisk z tekstem "B".  
Damki oznaczane są dodatkową literą d ("Cd" , "Bd").  
Nad planszą wyświetlana jest informacja "Tura gracza x", gdzie x to numer gracza.  
Gracz wybiera pionka (tekst pola zmiania się z "C" na "[C]" lub z "B" na "[B]"), a potem pole, na które chce wykonać ruch. Jeśli ruch jest dozwolony, pionek jest przestawiany.  
Jeśli nie to wyświetlany jest komunikat "ruch niedozwolony".  
Zasady takie jak w warcabach (dowolny wariant). Zwykłe pionki i damki mają być obiekatami dwóch różnych klas dziediczących po klasie Pionek.  
Gdy gra się kończy wyświetlane jest okienko z napisem "Wygrał gracz 1" lub "Wygrał gracz 2", zależnie od tego kto wygrał grę. Możliwe jest resetowanie planszy bez zamykania głównego okna.

# Testy

1.Wykonanie po dwa ruchy przez każdego z graczy.  
3.Niepowodzenie błednego ruchu pionkiem.  
4.Wykonanie bicia pojedynczego pionka.  
5.Wykonanie bicia przynajmniej dwóch pionków.  
6.Zamiana piona w damkę  
7.Bicie damką  
8.Wygrana gracza grającego pionkami czarnymi  
9.Rozpoczęcie nowej gry po zwycięstwie jednego z graczy  

Wskazane jest przygotowanie specjalnych początkowych rozstawień pionków dla testów 4,5,6,7,8
