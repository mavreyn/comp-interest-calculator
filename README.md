# Compound Interest Tables Calculator

I coded this calculator in the second semester of my freshman year in college when I needed to take economics. This actually did save a lot of time and I flew through the homework in that class!

This was designed to produce maximal output under minimal keystokes, so there are no instructions or menus in the program. But I made it for myself so I was comfortable with that, and I knew how everything worked

## Use

Run `CompIntTables.py` and the program will prepare to receive input. To perform basic TVM functions, type the two letter function name, then the interest rate (in percent), then the number of periods (optionally the amount)
The program will return the factor to five decimal places (no amount provided) and the solution to 2 decimal places (cents)(amount provided)

Function parts: `f` future, `p` present, `a` annuity, `g` gradient

- For example: to get the future value from a present value of $4000 at 2% for 7 years, type `fp 2 7 4000` and the program returns `4594.74`
- Factor: To get the factor listed at the back of the book for the annuity equivalent of receiving a future deposit with an interest rate of 1% 15 years from present, type `af 1 15` and the program returns `0.06212`

After each entry with an amount, the program will store the results in a list such as `[135.33, 109.5]` which is displayed after each calculation. If an interest rate has already been declared when calculating an amount to store, the program will retain this information, which can be used for last entry adjustments. 

- To replace the last entry with an equivalent amount shifted by a number of terms, type `.` followed by the year shift. In the case of the above list, typing `.-3` will change the list to `[135.33, 106.28]`
- To enter an amount into the list, simply type `=` followed by the amount
- To delete the last entry, type `del`
- To finish the problem, type `sum` and the program will print the sum of the list and clear it for the next problem
