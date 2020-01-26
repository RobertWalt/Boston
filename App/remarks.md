## Anmerkungen zur Data Engineering Challenge
### Mögliche Verbesserungen
#### Model
* Flexibilität bezüglich der betrachteten Features. SalePrice, LotArea, BldgType sind meist hard-gecoded. Schöner wäre die Übergabe der Features.
* Intensivere Evaluation der Performance des Regression Models. Aktuell nur über OOB score nach dem Training möglich.  
* One-hot encoding von BldgType erfordert die Übergabe der neu erstellten Features vom Training zur Prediction. Momentan wird das etwas umständlich über model_data.json realisiert.
* Evaluation der geringen Signifikanz des Features BldgType für SalePrice.

#### Web App
* Verbessertes Design
* Verbesserte Navigation
* Web App Testing


