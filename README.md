# Weighted coin bet sizing Monte Carlo simulation

Here's the problem:
You are given a weighted coin that lands heads-up x% of the time. You are given an infinitely divisible dollar—you can divide it into millicents, nanocents, and so on, as you wish. You must select a bet size. If the coin comes up heads, your pot grows by your bet size. If not, your pot shrinks by your bet size.  

What is the bet size that, while avoiding the risk of losing it all (i.e., without betting everything on heads round one, since that's against the spirit of the problem), minimizes the number of rounds that it takes on average to double the pot? If your bet size is too small, you barely crawl toward 2x. If it is too big, then every loss hurts too badly. How do you negotiate this trade-off? And how does this answer change as the coin is more and more one-sided?