# **Insights throughout the project**
## What factors are most likely to influence a player to transfer from their current school?
According to our xgboost model, the factors (and their corresponding importance score) most likely to influence a player's transfer decision are their destination school's 2023 win percentage (0.9157), their destination school's NIL collective amount (.0241), their original school's NIL collective amount (0.0102), and their position (0.0101). 

Our model had an overall mean squared error of 0.0764, meaning that roughly 7.64% of the variation in our data can be explained by these factors. This suggests that while there is some impact, there are likely many other factors that impact a player's decision to transfer to and from their schools. Each player is unique and likely has unique factors and priorities that need to be considered in a case-by-case manner.

## Which schools lose/gain the most players from the transfer portal?
The top five schools that lose the most players through the transfer portal are Colorado, Tennessee, Mississippi State, Florida State, and Ole Miss. The top five schools that gain the most players through the transfer portal are Texas State, Colorado, SMU, UMASS, and Arizona State. Interestingly enough, two of these schools (SMU and Arizona State) made their first-ever College Football Playoff appearances with rosters built largely from transfer portal players. 

## Which MW players are at risk of transferring in/out according to our model?
Players most likely to transfer out:
                                   transfer_likelihood
Garrett Beckman (OL UNLV)          0.263794
Sir Oliver Everett (DB UNLV)       0.231141
Tyleek Collins (WR UNLV)           0.284072
Kenyon Oblad (QB UNLV)             0.336212
Jalen Graves (DL UNLV)             0.220343

Players most likely to transfer in:
                                   transfer_likelihood
Daviyon McDaniel (OL UNLV)         0.973844
Tate Martell (QB UNLV)             1.034532
Jordan Jakes (WR Valdosta State)   1.028604

