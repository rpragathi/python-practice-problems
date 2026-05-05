Loan Default Analysis Using NumPy

Project Overview:

The purpose of this project is to demonstrate practical proficiency in NumPy by performing structured numerical analysis on a real-world loan default dataset. Instead of using machine learning libraries, I focused entirely on NumPy operations to highlight strong fundamentals in array manipulation, boolean masking, vectorized computation, statistical analysis, and basic linear algebra. The dataset contains borrower information such as Age, Income, LoanAmount, CreditScore, MonthsEmployed, NumCreditLines, InterestRate, LoanTerm, DTIRatio, and a target variable indicating whether the loan defaulted. I began by loading the dataset, selecting numerical features, and converting them into NumPy arrays. After verifying shapes and data types, I analyzed using boolean masks and calculated the overall default rate, observing that the dataset is imbalanced, which is common in financial risk data.Next, I compared defaulters and non-defaulters using vectorized mean calculations. The analysis showed that defaulters tend to be younger, have lower income, face higher interest rates, and have shorter employment duration. These patterns align with practical financial risk expectations.I then computed a full correlation matrix using NumPy and extracted correlations with the target variable. Age and InterestRate showed the strongest relationships with default, while LoanTerm had almost no linear impact. Overall, correlations were relatively small, suggesting that default risk is influenced by multiple moderate factors rather than a single dominant variable.To further demonstrate NumPy capabilities, I performed risk segmentation using threshold-based and percentile-based filtering, comparing default rates across income and credit score groups. I also standardized the features using broadcasting and computed the covariance matrix to analyze inter-feature relationships.Finally, I compared loop-based and vectorized computations to highlight performance differences and reinforce why NumPy’s vectorized operations are preferred for scalable numerical workloads.

Key findings:
- Younger borrowers show higher default tendency.
- Higher interest rates are associated with higher default risk.
- Lower income and shorter employment duration increase risk.
- Loan term has almost no linear relationship with default.
- No single feature strongly predicts default (all correlations are small).
- Default behavior appears to be influenced by multiple moderate financial factors rather than one dominant variable.

