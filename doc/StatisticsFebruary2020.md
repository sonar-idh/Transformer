# Diese Statistiken wurden für Evaluation I (HU) zusammengefasst.
## M1 Anzahl der Datensätze* je Datendump 

| Datendump | Anzahl     |
|-----------|------------|
| GND       | 8.295.047  |
| DNB       | 19.926.573 |
| ZDB       | 1.908.334  |
| KPE       | 4.386.173  |
| ZDB-Dubletten| 541.840    |

*Ein Record entspricht einem Datensatz. `IsilTerm`und `ChronTerm` sind nicht in Records, sondern in Datenfeldern kodiert. So werden diese Entitätentypen hier nicht beschrieben. `IsilTerm`und `ChronTerm` sind in M4 gezählt.


## M2 Anzahl der relevanten Datenfelder (nach Datenmodell) je Datendump

| **Datendumps** | **Felder** |          |         |         |         |         |         |         |       |        |                               |
|----------------|------------|----------|---------|---------|---------|---------|---------|---------|-------|--------|-------------------------------|
|                | *1XX*      | *500*     | *510*    | *511*   | *530*   | *550*    | *551*    | *548*    |       |        | alle Referenzen zu Normdaten  |
| Personen       | 5.087.660  | 418.986   | 728.633  | 226     | 2.303   | 5.346.145| 2.149.797| 4.280.577|       |        | 12.926.667                      |
| Körperschaften | 1.487.711  | 14.863    | 676.128  | 433     | 2.323   | 305.986  | 1.122.308| 257.432  |       |        | 2.379.473                       |
| Kongresse      | 814.044    | 917       | 37.862   | 40.747  | 12      | 32.562   | 712.906  | 672.480  |       |        | 1.497.486                       |
| Werke          | 385.300    | 387.861   | 26.603   | 311     | 35.327  | 63.977   | 25.007   | 182.122  |       |        | 721.208                        |
| Sachbegriffe   | 212.135    | 2.906     | 3.670    | 18      | 133     | 211.654  | 12.176   | 7.315    |       |        | 237.872                        |
| Geografika     | 308.197    | 9.184     | 3.423    | 24      | 27      | 115.747  | 179.360  | 47.535   |       |        | 355.300                        |
| **GND**        | 8.295.047  | 834.717   | 1.476.319| 41.759  | 40.125  | 6.076.071| 4.201.554| 5.447.461|       |        | 18.118.006                      |
|                |            | *100*     | *700*    | *110*   | *710*   | *111*    | *711*    | *130*    | *730* | *751*    | alle Referenzen zu Normdaten  |
| ZDB            | 1.908.334  | 837       | 21.639   | 636.950 | 421.080 | 38.779   | 6.390    | 3.527    | 9     | 201.252 | 1.330.463                       |
|                |            | *770*     | *772*     | *775*     | *776*     | *780*     | *785*     |         |       |        | alle Referenzen zu Titeldaten |
| ZDB            |            | 86.261    | 97.922   | 10.018   | 392.555  | 444.440  | 497.262  |         |       |        | 1.528.458                       |
|                |            |  |      |      |      |      |      |         |       |        | alle Referenzen zu Norm-, Titeldaten (ohne Referenzen, die von ZDB-Dubletten ausgehen) |
| DNB1 ohne ZDB-Dubletten| 4.641.089  |   |  |   |   |    |     |     |  |   | 5.622.857                     |
| DNB2 ohne ZDB-Dubletten| 4.884.568  |   |  |   |   |    |     |     |  |   | 6.090.258                     |
| DNB3 ohne ZDB-Dubletten| 4.901.158  |   |  |   |   |    |     |     |  |   | 7.294.607                     |
| DNB4 ohne ZDB-Dubletten| 4.957.918  |   |  |   |   |    |     |     |  |   | 12.528.896                    |
| **DNB** ohne ZDB-Dubletten | 19.384.733 |   |  |   |   |    |     |     |  |   | 31.536.618                    |
|                | *archdesc*  | *persname*| *corpname* | *geogname* | *subject* | *level*   |    |     |  |     | alle Referenzen  |
| KPE            | 26.752      | 6.007.129 | 850.794    | 1.151.174  | 174.788   | 4.359.421 |  |   |  |   | 12.543.306 |

          

<!---
| DNB1           |            | 2901479  | 1768497 | 192091  | 519693  | 10354   | 5516    | 1269    | 23850 | 49315  | 5472064                       |
| DNB2           |            | 2922515  | 2067008 | 156934  | 440676  | 34484   | 75334   | 834     | 64134 | 10226  | 5772145                       |
| DNB3           |            | 2462668  | 2966802 | 86030   | 703198  | 12440   | 32940   | 7222    | 24457 | 13427  | 6309184                       |
| DNB4           |            | 2726426  | 6990761 | 82805   | 1886076 | 9525    | 1165    | 20422   | 737   | 908    | 11718825                      |
| **DNB insg.**  |            | 24806156 |         | 4067503 |         | 181758  |         | 142925  |       | 73876  | 29272218                      |
| **ZDB insg.**  |            | 22476    |         | 1058030 |         | 45169   |         | 3536    |       | 201252 | 1330463                       |
| **DNB+ZDB**    |            |          |         |         |         |         |         |         |       |        | 30602681                      |
| DNB1           |            | 44509    | 22403   | 58402   | 389444  | 120981  | 146438  |         |       |        | 782177                        |
| DNB2           |            | 4612     | 6461    | 26278   | 323314  | 55280   | 47534   |         |       |        | 463479                        |
| DNB3           |            | 3957     | 9694    | 28116   | 1027165 | 36743   | 16298   |         |       |        | 1121973                       |
| DNB4           |            | 3099     | 7816    | 74386   | 717106  | 33326   | 2874    |         |       |        | 838607                        |
| **DNB insg.**  |            | 56177    | 46374   | 187182  | 2457029 | 246330  | 213144  |         |       |        | 3206236                       |
| **DNB+ZDB**    |            | 142438   | 144296  | 197200  | 2849584 | 690770  | 710406  |         |       |        | 4734694                       |
| **insg**    |            |    |   |   |  |   |   |         |       |        |                        |
--->



## M3 Anzahl der <span style="color: grey;">gültigen</span> Referenzen je Datenfeld (gemäß Datenmodell für Relation) und Datendump

|  RelationTo    | PerName  | CorpName | MeetName | UniTitle | TopicTerm | GeoName | ChronTerm | IsilTerm | Resource | alle Referenzen |
|----------------|----------|----------|----------|----------|-----------|---------|-----------|----------|----------|-----------------|
| Personen       | 347.542   | 669.514   | 201      | 2.280     | 4.053.424   | 1.825.148 | 4.280.076   | 10.175.320 | 0        | 21.353.505        |
| Körperschaften | 13.732    | 599.392   | 433      | 2.322     | 300.628    | 1.105.113 | 257.406    | 2.975.422  | 0        | 5.254.448         |
| Kongresse      | 903      | 36.363    | 40.538    | 12       | 32.344     | 642.751  | 672.473    | 1.628.088  | 0        | 3.053.472         |
| Werke          | 380.672   | 26.457    | 311      | 35.122    | 63.605     | 24.907   | 182.039    | 770.600   | 0        | 1.483.713         |
| Sachbegriffe   | 2.793     | 3.539     | 18       | 133      | 211.268    | 12.020   | 7.314      | 424.270   | 0        | 661.355          |
| Geografikum    | 8.966     | 3.338     | 24       | 27       | 115.639    | 178.214  | 47.533     | 616.394   | 0        | 970.135          |
| DNB1           | 2.767.510  | 455.698   | 10.921    | 286      | 0         | 1       | 0         | 9.042.687  | 345.603   | 12.622.706        |
| DNB2           | 2.719.587  | 538.140   | 109.634   | 216      | 0         | 2       | 0         | 9.667.793  | 359.917   | 13.395.289        |
| DNB3           | 1.877.913  | 366.914   | 45.260    | 3.564     | 0         | 1       | 0         | 7.379.815  | 558.583   | 10.232.050        |
| DNB4           | 670.203   | 500.959   | 10.671    | 10.033    | 0         | 60      | 0         | 5.692.564  | 284.804   | 7.169.294         |
| <span style="color:blue">GND</span>  | <span style="color:blue">754.608</span>   | <span style="color:blue">1.338.603</span>  | <span style="color:blue">41.525</span>    | <span style="color:blue">39.896</span>    | <span style="color:blue">4.776.908</span>   | <span style="color:blue">3.788.153</span> | <span style="color:blue">5.446.841</span>   | <span style="color:blue">16.590.094</span> | <span style="color:blue">0</span>        | <span style="color:blue">32.776.628</span>    |
| <span style="color:blue">DNB</span>            | <span style="color:blue">8.035.213</span>  | <span style="color:blue">1.861.711</span>  | <span style="color:blue">176.486</span>   | <span style="color:blue">14.099</span>    | <span style="color:blue">0</span>         | <span style="color:blue">64</span>      | <span style="color:blue">0</span>         | <span style="color:blue">31.782.859</span> | <span style="color:blue">1.548.907</span>  | <span style="color:blue">43.419.339</span>        |
| <span style="color:blue">ZDB</span>            | <span style="color:blue">16.610</span>    | <span style="color:blue">1.057.662</span>  | <span style="color:blue">45.169</span>    | <span style="color:blue">3</span>        | <span style="color:blue">0</span>         | <span style="color:blue">201.168</span>  | <span style="color:blue">0</span>         | <span style="color:blue">2.856.175</span>  | <span style="color:blue">1.479.072</span>  | <span style="color:blue">5.655.859</span>         |
| <span style="color:blue">KPE</span>            | <span style="color:blue">5.824.034</span>  | <span style="color:blue">841.214</span>   | <span style="color:blue">0</span>        | <span style="color:blue">0</span>        | <span style="color:blue">174.709</span>    | <span style="color:blue">1.151.171</span> | <span style="color:blue">0</span>         | <span style="color:blue">4.327.785</span>  | <span style="color:blue">4.359.421</span>  | <span style="color:blue">16.678.334</span>        |
| **Normdaten**  | 754.608   | 1.338.603  | 41.525    | 39.896    | 4.776.908   | 3.788.153 | 5.446.841   | 16.590.094 | 0        | **32.776.628**    |
| **Titeldaten** | 13.875.857 | 3.760.587  | 221.655   | 14.102    | 174.709    | 1.352.403 | 0         | 38.966.819 | 7.387.400  | **65.753.532**    |
| **alle Daten** | 14.630.465 | 5.099.190  | 263.180   | 53.998    | 4.951.617   | 5.140.556 | 5.446.841   | 55.556.913 | 7.387.400  | **98.530.160**    |


## M4 Anzahl der gemäß M3 referenzierten, gültigen Entitäten je Entitätentyp und Datendump

|                | PerName | CorpName | MeetName | UniTitle | TopicTerm | GeoName | ChronTerm | IsilTerm | Resource | alle Referenzen |
|----------------|---------|----------|----------|----------|-----------|---------|-----------|----------|----------|-----------------|
| Personen       | 12.505   | 265.434   | 318      | 2.296     | 9.317      | 60.692   | 50.771     | 2        | 0        | 401.335          |
| Körperschaften | 5.310    | 2.828     | 19       | 26       | 2.850      | 71.353   | 11.755     | 2        | 0        | 94.143           |
| Kongresse      | 785     | 16.463    | 32.623    | 12       | 1.420      | 20.929   | 33.622     | 2        | 0        | 105.856          |
| Werke          | 167.985  | 123.295   | 142      | 2.076     | 14.696     | 71.354   | 468.728    | 2        | 0        | 848.278          |
| Sachbegriffe   | 1.679    | 1.484     | 15       | 85       | 50.887     | 4.261    | 3.127      | 2        | 0        | 61.540           |
| Geografikum    | 87.689   | 7.836     | 184      | 2.270     | 5.613      | 1.849    | 13.533     | 2        | 0        | 118.976          |
| DNB1           | 532.527  | 94.653    | 8.375     | 222      | 0         | 1       | 0         | 2        | 344.214   | 979.994          |
| DNB2           | 624.286  | 131.374   | 90.716    | 144      | 0         | 2       | 0         | 6        | 334.580   | 1.181.108         |
| DNB3           | 538.724  | 76.051    | 37.323    | 2.773     | 0         | 1       | 0         | 6        | 545.850   | 1.200.728         |
| DNB4           | 261.215  | 52.143    | 9.142     | 6.523     | 0         | 46      | 0         | 7        | 283.309   | 612.385          |
| <span style="color:blue">GND</span>           | <span style="color:blue">256.515</span>  | <span style="color:blue">347.857</span>   | <span style="color:blue">33.143</span>    | <span style="color:blue">6.598</span>     | <span style="color:blue">60.994</span>     | <span style="color:blue">127.253</span>  | <span style="color:blue">537.054</span>    | <span style="color:blue">2</span>        | <span style="color:blue">0</span>        | <span style="color:blue">1.369.416</span>         |
| <span style="color:blue">DNB</span>            | <span style="color:blue">1.443.639</span> | <span style="color:blue">281.644</span>   | <span style="color:blue">139.829</span>   | <span style="color:blue">9.181</span>     | <span style="color:blue">0</span>         | <span style="color:blue">50</span>      | <span style="color:blue">0</span>         | <span style="color:blue">7</span>        | <span style="color:blue">1.499.266</span>  | <span style="color:blue">3.373.616</span>         |
| <span style="color:blue">ZDB</span>            | <span style="color:blue">8.819</span>    | <span style="color:blue">387.313</span>   | <span style="color:blue">34.690</span>    | <span style="color:blue">3</span>        | <span style="color:blue">0</span>         | <span style="color:blue">20.864</span>   | <span style="color:blue">0</span>         | <span style="color:blue">2</span>        | <span style="color:blue">911.248</span>   | <span style="color:blue">1.362.939</span>         |
| <span style="color:blue">KPE</span>            | <span style="color:blue">284.544</span>  | <span style="color:blue">45.486</span>    | <span style="color:blue">0</span>        | <span style="color:blue">0</span>        | <span style="color:blue">5.811</span>      | <span style="color:blue">6.157</span>    | <span style="color:blue">0</span>         | <span style="color:blue">602</span>      | <span style="color:blue">4.326.296</span>  | <span style="color:blue">4.668.896</span>         |
| **Normdaten**  | 256.515  | 347.857   | 33.143    | 6.598     | 60.994     | 127.253  | 537.054    | 2        | 0        | **1.369.416**         |
| **Titeldaten** | 1.618.500 | 618.029   | 173.319   | 9.184     | 5.811      | 24.079   | 0         | 609      | 6.730.526  | **9.180.057**         |
| **alle Daten**     | 1.759.713 | 741.388   | 190.412   | 15.673    | 63.429     | 129.411  | 537.054    | 611      | 6730526  | **10.168.217**        |

## M5 Anzahl der als fehlerhaft identifizierten Datensätze je Datendump


| Datendump | ohne gültige Identifikatoren | fehlende Normdaten (Tn) | fehlende Titeldaten |
|-----------|-----------|-------------------------|---------------------|
| GND       | 1.929.635 | 37                      | 0                   |
| DNB (ohne ZDB-Dubletten)      | 9.677.777 | 10.099.596              | 30.475              |
| ZDB       | 52.766    | 5.520                   | 70                  |
| KPE       | 62        | 192.870                 | 0                   |

- In der KPE 1.447.006 Relationen gefunden, die nicht zu Entitäten aus der GND waren (z.B. @source='SLA')

## M6 Anzahl der Dubletten je Datendump auf Ebene eines Datensatzes (zu DNB übertragene ZDB-Datensätze). 

| Datenfile | Anzahl  |
|-----------|---------|
| DNB1      | 340.554 |
| DNB2      | 97.075  |
| DNB3      | 80.485  |
| DNB4      | 23.726  |
| DNB       | 541.840 |


## M7 Anzahl der Dubletten (nach Datenmodell) je Datendump auf Ebene eines Datenfeldes/Unterfeldes. 

| Datendump/Felder |       |       |       |       |       |       |       |       |       |             |
|------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------------|
|                  | *500* | *510* | *511* | *530* | *550* | *551* | *548* |       |       | **5XX**     |
| Personen         | 56    | 128   | 0     | 1     | 879   | 423   | 54    |       |       | 1.541        |
| Körperschaften   | 3     | 47    | 0     | 0     | 15    | 42    | 7     |       |       | 114         |
| Kongresse        | 0     | 7     | 4     | 0     | 4     | 14    | 5     |       |       | 34          |
| Werke            | 18    | 0     | 0     | 2     | 10    | 0     | 66    |       |       | 96          |
| Sachbegriffe     | 0     | 0     | 0     | 0     | 4     | 1     | 1     |       |       | 6           |
| Geografika       | 0     | 0     | 0     | 0     | 1     | 7     | 1     |       |       | 9           |
| GND              | 77    | 182   | 4     | 3     | 913   | 487   | 134   |       |       | 1.800        |
|                  | *100* | *700* | *110* | *710* | *111* | *711* | *130* | *730* | *751* | **1XX/7XX** |
| ZDB              | 0     | 0     | 1     | 20    | 0     | 0     | 0     | 0     | 83    | 104         |
|                  | *770* | *772* | *775* | *776* | *780* | *785* |       |       |       | **7XX**     |
| ZDB              | 30    | 27    | 3     | 74    | 79    | 564   |       |       |       | 777         |
|                  |       |       |       |       |       |       |       |       |       | alle Referenzen   |
| DNB1 ohne ZDB-Dubletten|       |       |       |       |       |       |       |       |       | 369         |
| DNB2 ohne ZDB-Dubletten|       |       |       |       |       |       |       |       |       | 3.246       |
| DNB3 ohne ZDB-Dubletten|       |       |       |       |       |       |       |       |       | 49.225      |
| DNB4 ohne ZDB-Dubletten|       |       |       |       |       |       |       |       |       | 39.450      |
| DNB ohne ZDB-Dubletten |       |       |       |       |       |       |       |       |       | 92.290       |

<!---|                  | *100* | *700* | *110* | *710* | *111* | *711* | *130* | *730* | *751* | **1XX/7XX** |
| ~~DNB1~~             | ~~50~~    | ~~2~~     | ~~0~~     | ~~318~~   | ~~0~~     | ~~0~~     | ~~0~~     | ~~1~~     | ~~21~~    | ~~392~~         |
| ~~DNB2~~             | ~~29~~    | ~~24~~    | ~~0~~     | ~~113~~   | ~~0~~     | ~~0~~     | ~~0~~     | ~~0~~     | ~~1~~     | ~~167~~         |
| ~~DNB3~~             | ~~70~~    | ~~32~~    | ~~1~~     | ~~78~~    | ~~0~~     | ~~3~~~~     | ~~0~~     | ~~0~~     | ~~2~~     | ~~186~~         |
| ~~DNB4~~             | ~~111~~   | ~~2010~~     | ~~1~~     | ~~63~~    | ~~0~~     | ~~0~~     | ~~0~~     | ~~0~~     | ~~2~~     | ~~2187~~         |
| ~~DNB~~              | ~~260~~   | ~~2068~~    | ~~2~~     | ~~572~~   | ~~0~~     | ~~3~~     | ~~0~~     | ~~1~~     | ~~26~~    | ~~2932~~         |
|                  | *770* | *772* | *775* | *776* | *780* | *785* |       |       |       | **7XX**     |
| ~~DNB1~~             | ~~20~~    | ~~14~~    | ~~1~~     | ~~21~~    | ~~7~~     | ~~8~~     |       |       |       | ~~71~~          |
| ~~DNB2~~             | ~~3~~     | ~~2~~     | ~~0~~     | ~~3090~~  | ~~5~~     | ~~2~~     |       |       |       | ~~3102~~        |
| ~~DNB3~~             | ~~1~~     | ~~2~~     | ~~1~~     | ~~48992~~ | ~~71~~    | ~~83~~    |       |       |       | ~~49150~~       |
| ~~DNB4~~             | ~~1~~     | ~~5~~     | ~~3~~     | ~~37246~~ | ~~10~~    | ~~2~~     |       |       |       | ~~37267~~       |
| ~~DNB~~              | ~~25~~    | ~~23~~    | ~~5~~     | ~~89349~~ | ~~93~~    | ~~95~~    |       |       |       | ~~89590~~       |
| DNB+ZDB          | 260   | 59    | 3     | 592   | 0     | 3     | 0     | 1     | 109   | 1027        |--->
<!---| DNB+ZDB          | 55    | 50    | 8     | 89423 | 172   | 659   |       |       |       | 90367       |--->

## M8 Anzahl der gültigen Referenzen, die von Dubletten ausgehen, vgl. M6. 

In M2, M5, M7 wird Anzahl von entsprechenden Elementen für DNB ohne ZDB-Dubletten gezählt.


## N1 Anzahl der Knoten: 

34.511.952
    
## N2 Anzahl der Knoten je Datendump

| Datendump     | Anzahl     |
|---------------|------------|
| GND           | 8.295.047  |
| DNB           | 19.384.733 |
| ZDB           | 1.908.334  |
| KPE           | 4.386.173  |
| ChronTerm GND | 537.054    |
| IsilTerm      | 611        |

## N3 Anzahl der Knoten je Entitätentyp

| Entitaetentyp | Anzahl     |
|---------------|------------|
| CorpName      | 1.487.711  |
| GeoName       | 308.197    |
| MeetName      | 814.044    |
| PerName       | 5.087.660  |
| TopicTerm     | 212.135    |
| UniTitle      | 385.300    |
| ChronTerm     | 537.054    |
| IsilTerm      | 611        |
| Resource      | 25.679.240 |


## N4 Anzahl der Kanten

98.530.160

## N5 Anzahl der Kanten je Datendump

| Datendump | Anzahl (ohne `RelationToIsilTerm`) | Anzahl (mit `RelationToIsilTerm`)|
|-----------|------------|------------|
| GND       | 16.186.534 | 32.776.628 |
| ZDB       | 2.799.684  | 5.655.859  | 
| DNB       | 11.636.480 | 43.419.339 |
| KPE       | 12.350.549 | 16.678.334 |


## N6 Anzahl der Kanten je Relationentyp gemäß Datenmodell

| Relationentyp       | Anzahl     |
|---------------------|------------|
| RelationToPerName   | 14.630.465 |
| RelationToCorpName  | 5.099.190  |
| RelationToMeetName  | 263.180    |
| RelationToUniTitle  | 53.998     |
| RelationToTopicTerm | 4.951.617  |
| RelationToGeoName   | 5.140.556  |
| RelationToChronTerm | 5.446.841  |
| RelationToIsil      | 55.556.913 |
| RelationToResource  | 7.387.400  |


## N7 Anzahl der Kanten je Relationentyp gemäß Datenmodell und Datendump

| RelationTo | PerName   | CorpName  | MeetName | UniTitle | TopicTerm | GeoName   | ChronTerm | IsilTerm   | Resource  |
|------------|-----------|-----------|----------|----------|-----------|-----------|-----------|------------|-----------|
| GND        | 754.608   | 1.338.603 | 41.525   | 39.896   | 4.776.908 | 3.788.153 | 5.446.841 | 16.590.094 | 0         |
| DNB        | 8.035.213 | 1.861.711 | 176.486  | 14.099   | 0         | 64        | 0         | 31.782.859 | 1.548.907 |
| ZDB        | 16.610    | 1.057.662 | 45.169   | 3        | 0         | 201.168   | 0         | 2.856.175  | 1.479.072 |
| KPE        | 5.824.034 | 841.214   | 0        | 0        | 174.709   | 1.151.171 | 0         | 4.327.785  | 4.359.421 |


## Ergebnis M2-M5-M7=N5

| Dok-Nummer | Erläuterung                                                   | Operation    | GND        | DNB ohne ZDB | ZDB       | KPE        |
|------------|---------------------------------------------------------------|--------------|------------|--------------|-----------|------------|
| M2         | Anzahl der relevanten Datenfelder für Referenzen              | Gegeben      | 18.118.006 | 31.536.618   | 2.858.921 | 12.543.306 |
| M5.1       | Anzahl der Referenzen zu Entitäten ohne ID                    | Substraktion | 1.929.635  | 9.677.777    | 52.766    | 55         |
| M5.2       | Anzahl der Referenzen zu nicht-individualisierten Datensätzen | Substraktion | 37         | 10.130.071   | 5.590     | 192.702    |
| M7         | Anzahl der Dubletten aus Datenfeldern                         | Substraktion | 1.800      | 92.290       | 881       | 0          |
| ~M8~         | ~Anzahl aller Referenzen aus DNB-Dubletten~                     | ~Substraktion~ | ~0~          | ~entfällt~     | ~0~         | ~0~          |
|            | Ergebnis                                                      | Berechnet    | 16.186.534 | 11.636.480   | 2.799.684 | 12.350.549 |
| N5         | Kanten (ohne `RelationToIsilTerm`)                            | Gegeben      | 16.186.534 | 11.636.480   | 2.799.684 | 12.350.549 |


### GND Personen

- Anzahl Knoten 9.367.736, davon 5.087.660 Knoten für Personen und 4.280.075 für Zeitausdrücke
- Anzahl Kanten 11.178.185
- Anzahl Relationen zu Entitäten mit veralteten Identifikatoren 145
- Anzahl Relationen zu ungültigen Entitäten 1.746.910
- Anzahl Relationen zu nicht-individualisierten Datensätzen 31

### GND Körperschaften

- Anzahl Knoten 1.745.117, davon 1.487.711 Knoten für Körperschaften und 257.406 für Zeitausdrücke
- Anzahl Kanten 2.279.026
- Anzahl Relationen zu Entitäten mit veralteten Identifikatoren 3
- Anzahl Relationen zu ungültigen Entitäten 100.332
- Anzahl Relationen zu nicht-individualisierten Datensätzen 1

### GND Kongresse

- Anzahl Knoten 1.486.517, davon 814.044 Knoten für Kongresse und 672.473 für Zeitausdrücke
- Anzahl Kanten 1.425.384
- Anzahl Relationen zu Entitäten mit veralteten Identifikatoren 0
- Anzahl Relationen zu ungültigen Entitäten 72.068
- Anzahl Relationen zu nicht-individualisierten Datensätzen 0

### GND Werke

- Anzahl Knoten 567.339, davon 385.300 Knoten für Werke und 182.039 für Zeitausdrücke
- Anzahl Kanten 713.113
- Anzahl Relationen zu Entitäten mit veralteten Identifikatoren 11
- Anzahl Relationen zu ungültigen Entitäten 7.995
- Anzahl Relationen zu nicht-individualisierten Datensätzen 4

### GND Sachbegriffe

- Anzahl Knoten 219.449, davon 212.135 Knoten für Sachbegriffe und 7.314 für Zeitausdrücke
- Anzahl Kanten 237.085
- Anzahl Relationen zu Entitäten mit veralteten Identifikatoren 0
- Anzahl Relationen zu ungültigen Entitäten 781
- Anzahl Relationen zu nicht-individualisierten Datensätzen 0


### GND Geografika

- Anzahl Knoten 355.730, davon 308.197 Knoten für Geografika und 47.533 für Zeitausdrücke
- Anzahl Kanten 353.741
- Anzahl Relationen zu Entitäten mit veralteten Identifikatoren 0
- Anzahl Relationen zu ungültigen Entitäten 1.549
- Anzahl Relationen zu nicht-individualisierten Datensätzen 1


### ZDB

- Anzahl Knoten 1.908.334 
- Anzahl Kanten 2.799.684
- Anzahl Relationen zu Entitäten mit veralteten Identifikatoren 469
- Anzahl Relationen zu ungültigen Entitäten 52.766
- Anzahl Relationen zu nicht-individualisierten Datensätzen 5.590 (davon 70 zwischen Ressourcen)

### DNB1

- Anzahl Knoten 4.641.089, gegeben 4.981.643, davon **Dubletten 340.554**
- Anzahl Kanten 3.580.019
- Anzahl Relationen zu Entitäten mit veralteten Identifikatoren 1
- Anzahl Relationen zu ungültigen Entitäten 538.984
- Anzahl Relationen zu nicht-individualisierten Datensätzen 1.503.485 (davon 70 zwischen Ressourcen)

### DNB2

- Anzahl Knoten 4.884.568, gegeben 4.981.643, davon **Dubletten 97.075**
- Anzahl Kanten 3.727.496
- Anzahl Relationen zu Entitäten mit veralteten Identifikatoren 0
- Anzahl Relationen zu ungültigen Entitäten 400.467
- Anzahl Relationen zu nicht-individualisierten Datensätzen 1.959.049 (davon 831 zwischen Ressourcen)

### DNB3

- Anzahl Knoten 4.901.158, gegeben 4.981.643, davon **Dubletten 80.485**
- Anzahl Kanten 2.852.235
- Anzahl Relationen zu Entitäten mit veralteten Identifikatoren 50
- Anzahl Relationen zu ungültigen Entitäten 1.384.228
- Anzahl Relationen zu nicht-individualisierten Datensätzen 3.008.919 (davon 6.741 zwischen Ressourcen)



### DNB4

- Anzahl Knoten 4.957.918, gegeben 4.981.644, davon **Dubletten 23.726**
- Anzahl Kanten 1.476.730
- Anzahl Relationen zu Entitäten mit veralteten Identifikatoren 360
- Anzahl Relationen zu ungültigen Entitäten 7.354.098
- Anzahl Relationen zu nicht-individualisierten Datensätzen 3.658.618 (davon 22.833 zwischen Ressourcen)

```
Summe aller Dubletten in der DNB beträgt 340554 + 97075 + 80485 + 23726 = **541840**
Summe aller ungültigen Relationen zwischen Ressourcen beträgt 22833 + 6741 + 831 + 140 = **30545**
```


| Dok-Nummer | Erläuterung                                                   | Operation    | Anzahl     | GND        | DNB          | ZDB       |
|------------|---------------------------------------------------------------|--------------|------------|------------|--------------|-----------|
| M2         | Anzahl der relevanten Datenfelder für Referenzen              | gegeben      | 53.455.381 | 18.118.006 | 32.478.454!! | 2.858.921 |
| M5.1       | Anzahl der Referenzen zu Entitäten ohne ID                    | Substraktion | 11.660.178 | 1.929.635  | 9.677.777!!  | 52.766    |
| M5.2       | Anzahl der Referenzen zu nicht-individualisierten Datensätzen | Substraktion | 10.135.698 | 37         | 10.130.071!! | 5.590     |
| M7         | Anzahl der Dubletten aus Datenfeldern                         | Substraktion | 93.194     | 1800       | 90.513!!     | 881       |
| M8         | Anzahl aller Referenzen aus DNB-Dubletten                     | Substraktion | 941.594    | 0          | 941.594      | 0         |
|            |                                                               | Berechnet    | 30624717   | 16.186.534 | 11.638.499   | 2.799.684 |
| N2         | Kanten (! ohne RelationToIsilTerm)                            | Gegeben      |            | 16.186.534 | 11.636.480   | 2.799.684 |
