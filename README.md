# vasvill-2022-02-szorgalmi

A szorgalmi feladat megírni egy ellenőrző függvényt, ami megmondja, hogy az adott állás békés-e vagy sem. 

A szereplők: 
 - `F` - kigyúrt Fradi drukker
 - `f` - normál Fradi drukker
 - `D` - kigyúrt Dortmund drukker
 - `d` - normál Dortmund drukker
 - `R` - rendőr
 - `r` - rab / gyilkos

Egy állapot akkor nem békés, ha:
 - kigyúrt drukker mellett van másik csapat normál drukkere annak kigyúrt drukkere nélkül
 - rab mellett van valaki rendőr nélkül

Az állapotokat leíró dictionary formátuma a következő:

```python
{
    'bal' : [ 'F', 'f' , 'f', 'D', 'd' ],
    'jobb' : [ 'd', 'R', 'r' ],
    'csonak_bal' : True
}
```

A listákon belül az elemek sorrendje tetszőleges lehet, és a kód feltételezheti, hogy helyes az állapot, azaz mindenki szerepel, és annyiszor, amennyiszer kell. (Tehát nincs egy oldalon két rednőr pl.)

A feladatot a megadott függvényben kell implementálni, a függvény csak a kapott állapottal dolgozhat.

További szorgalmi feladatok:
 - `helyes_allapot` - olyan függvény, mely megnézi, hogy létszámot tekintve helyes-e az állapot (azzal nem foglalkozik, hogy el lehet-e oda jutni a kezdőállapotból.)
 - `helyes_lépés` - két állapot között megadja, hogy át lehet-e menni az egyikből a másikba egy lépésben.